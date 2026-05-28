#!/usr/bin/env python3
"""Macaulay2 LLM evaluation pipeline."""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, as_completed, wait
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from csv_exports import write_run_csvs
from providers import ALL_PROVIDERS, BATCH_CALLERS, CALLERS, DEFAULT_MODELS, clean_response
from metrics import compute_metrics, compute_pass_at_k_by_question
from scoring import compute_scores, normalize_reference_code, outputs_match

load_dotenv()

_BATCH_SUPPORT_CACHE: dict[str, bool] = {}


def _error_scores(execute_mode: bool) -> dict:
    if execute_mode:
        return {"execution_match": False, "code_fuzzy_score": 0.0, "composite_score": 0.0}
    return {"exact_match": False, "output_match": False, "fuzzy_score": 0.0, "composite_score": 0.0}


def _question_id(question: dict) -> str:
    return question.get("id") or question.get("problem_ID") or question.get("question_id")


def _has_m2_error(raw_output: str) -> bool:
    lowered = raw_output.lower()
    return " error:" in lowered or re.search(r"^stdio:", lowered, flags=re.MULTILINE) is not None or "--backtrace:" in lowered


def _strip_m2_transcript(text: str) -> tuple[str, bool]:
    """Keep input lines from a copied M2 transcript and drop output/type lines."""
    changed = False
    kept: list[str] = []
    for line in text.splitlines():
        prompt = re.match(r"^\s*i\d+\s*:\s?(.*)$", line)
        if prompt:
            kept.append(prompt.group(1))
            changed = True
            continue
        if re.match(r"^\s*o\d+\s*[=:]", line):
            changed = True
            continue
        if re.match(r"^\s*\S+\s*:\s*(?:Ring|Type|List|Sequence|Matrix|HashTable|Ideal|Module|String)\b", line):
            changed = True
            continue
        kept.append(line)
    return "\n".join(kept).strip(), changed


def extract_code(response: str) -> dict:
    """Deterministically remove wrappers/reasoning without repairing code."""
    text = response.strip()
    if not text:
        return {
            "extracted_code": "",
            "extraction_method": "empty",
            "extraction_error": "empty response",
            "code_only_violation": False,
        }

    method_parts: list[str] = []
    working = text

    fence = re.search(r"```(?:m2|macaulay2|text)?\s*(.*?)```", working, flags=re.DOTALL | re.IGNORECASE)
    if fence:
        working = fence.group(1).strip()
        method_parts.append("fenced_code")
    else:
        without_think = re.sub(r"<think>.*?</think>\s*", "", working, flags=re.DOTALL | re.IGNORECASE).strip()
        if without_think != working:
            working = without_think
            method_parts.append("think_removed")
        elif re.search(r"<think\b", working, flags=re.IGNORECASE):
            return {
                "extracted_code": "",
                "extraction_method": "unclosed_think",
                "extraction_error": "unclosed thinking tag",
                "code_only_violation": True,
            }

    label_patterns = [
        r"^\s*(?:macaulay2\s+code|m2\s+code|code|command|answer|expected response)\s*:?\s*",
        r"^\s*(?:the\s+command\s+is|the\s+answer\s+is)\s*:?\s*",
        r"^\s*(?:you can run|run|use|type)\s*:?\s*",
    ]
    before_labels = working
    for pattern in label_patterns:
        working = re.sub(pattern, "", working, flags=re.IGNORECASE)
    working = working.strip()
    if working != before_labels.strip():
        method_parts.append("label_removed")

    transcript_stripped, transcript_changed = _strip_m2_transcript(working)
    if transcript_changed:
        working = transcript_stripped
        method_parts.append("m2_transcript_stripped")

    wrapper_patterns = [
        r"^\s*(?:here is the code|here's the code|the code is|the code|expected response|here is|here's)\s*:?\s*",
        r"^\s*(?:sure|okay),?\s*",
    ]
    before_wrappers = working
    for pattern in wrapper_patterns:
        working = re.sub(pattern, "", working, flags=re.IGNORECASE)
    working = working.strip()
    if working != before_wrappers.strip():
        method_parts.append("wrapper_removed")

    prose_markers = [
        r"^\s*(let me|i can|we need|to solve)\b",
        r"\b(the user|the question|this code|explanation|reasoning)\b",
    ]
    lowered = working.lower()
    for pattern in prose_markers:
        if re.search(pattern, lowered, flags=re.MULTILINE):
            return {
                "extracted_code": working,
                "extraction_method": "+".join(method_parts) if method_parts else "raw",
                "extraction_error": "prose remains after extraction",
                "code_only_violation": True,
            }

    if not working:
        return {
            "extracted_code": "",
            "extraction_method": "+".join(method_parts) if method_parts else "empty",
            "extraction_error": "empty extracted code",
            "code_only_violation": True,
        }

    method = "+".join(method_parts) if method_parts else "raw"
    return {
        "extracted_code": working,
        "extraction_method": method,
        "extraction_error": None,
        "code_only_violation": working != text,
    }


def compile_reference(question: dict) -> dict:
    """Compile the benchmark reference answer once and return grading target metadata."""
    reference_code = normalize_reference_code(question.get("correct_answer"))
    record = {
        "question_id": _question_id(question),
        "reference_code": reference_code,
        "reference_output": None,
        "reference_raw_output": None,
        "reference_execution_error": None,
        "reference_failed": False,
    }
    try:
        from executor import run_m2

        reference_output, reference_raw_output = run_m2(reference_code)
        record["reference_output"] = reference_output
        record["reference_raw_output"] = reference_raw_output
        if not reference_output and reference_raw_output.startswith(("TIMEOUT", "SUBPROCESS_ERROR")):
            record["reference_execution_error"] = reference_raw_output
            record["reference_failed"] = True
        elif _has_m2_error(reference_raw_output):
            record["reference_execution_error"] = reference_raw_output
            record["reference_failed"] = True
    except Exception as exc:
        record["reference_execution_error"] = str(exc)
        record["reference_failed"] = True
    return record


def benchmark_digest(benchmark_path: str | Path) -> str:
    return hashlib.sha256(Path(benchmark_path).read_bytes()).hexdigest()


def default_reference_cache_path(
    benchmark_path: str | Path,
    cache_root: str | Path = "results/reference_cache",
) -> Path:
    benchmark = Path(benchmark_path)
    return Path(cache_root) / f"{benchmark.stem}_{benchmark_digest(benchmark)[:12]}.json"


def _cli_quote(value: str | Path) -> str:
    text = str(value)
    if re.search(r"\s", text):
        return f'"{text}"'
    return text


def compile_reference_records(questions: list[dict], workers: int = 1) -> dict[str, dict]:
    reference_records: dict[str, dict] = {}
    reference_workers = max(1, min(workers, len(questions)))
    print(f"Compiling {len(questions)} reference answers with M2 (workers={reference_workers})...")
    with ThreadPoolExecutor(max_workers=reference_workers) as pool:
        futures = {
            pool.submit(compile_reference, question): _question_id(question)
            for question in questions
        }
        for future in as_completed(futures):
            qid = futures[future]
            record = future.result()
            reference_records[qid] = record
    return reference_records


def print_reference_failures(questions: list[dict], reference_records: dict[str, dict]) -> None:
    for question in questions:
        qid = _question_id(question)
        record = reference_records[qid]
        if record["reference_failed"]:
            print(f"  {qid:<14} reference_failed")


def _print_sample_progress(done_count: int, total: int, qid: str, sample_index: int, result: dict) -> None:
    width = len(str(total))
    prefix = f"  [{done_count:>{width}}/{total}] {qid:<14} sample={sample_index}"
    if result.get("error"):
        print(f"{prefix}  ERROR: {result['error']}", flush=True)
    else:
        print(
            f"{prefix}  correct={'Y' if result['correct'] else 'n'}"
            f"  judge={result['judge']}",
            flush=True,
        )


def write_reference_cache(
    benchmark_path: str | Path,
    output_path: str | Path | None = None,
    workers: int = 1,
) -> Path:
    benchmark = Path(benchmark_path)
    with benchmark.open() as f:
        questions: list[dict] = json.load(f)
    cache_path = Path(output_path) if output_path else default_reference_cache_path(benchmark)
    records = compile_reference_records(questions, workers=workers)
    payload = {
        "schema_version": 1,
        "benchmark_path": str(benchmark),
        "benchmark_sha256": benchmark_digest(benchmark),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "num_questions": len(questions),
        "records": records,
    }
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(payload, indent=2))
    print_reference_failures(questions, records)
    print(f"Reference cache written to {cache_path}")
    return cache_path


def load_reference_cache(
    benchmark_path: str | Path,
    cache_path: str | Path | None = None,
) -> dict[str, dict]:
    benchmark = Path(benchmark_path)
    resolved_cache_path = Path(cache_path) if cache_path else default_reference_cache_path(benchmark)
    if not resolved_cache_path.exists():
        command = (
            f"python eval-pipeline/build_reference_cache.py "
            f"--benchmark {_cli_quote(benchmark)} --output {_cli_quote(resolved_cache_path)}"
        )
        raise FileNotFoundError(
            f"Reference cache not found: {resolved_cache_path}\n"
            f"Build it first with:\n  {command}"
        )
    payload = json.loads(resolved_cache_path.read_text())
    expected_digest = benchmark_digest(benchmark)
    if payload.get("benchmark_sha256") != expected_digest:
        command = (
            f"python eval-pipeline/build_reference_cache.py "
            f"--benchmark {_cli_quote(benchmark)} "
            f"--output {_cli_quote(default_reference_cache_path(benchmark))}"
        )
        raise ValueError(
            f"Reference cache is stale for benchmark: {resolved_cache_path}\n"
            f"Build a fresh cache with:\n  {command}"
        )
    records = payload.get("records")
    if not isinstance(records, dict):
        raise ValueError(f"Malformed reference cache: {resolved_cache_path}")
    with benchmark.open() as f:
        questions: list[dict] = json.load(f)
    missing = [_question_id(question) for question in questions if _question_id(question) not in records]
    if missing:
        raise ValueError(
            f"Reference cache is missing {len(missing)} question records: "
            f"{', '.join(missing[:5])}"
        )
    return records


# ---------------------------------------------------------------------------
# Core evaluation
# ---------------------------------------------------------------------------

def _file_key(provider: str, model: str, label_suffix: str = "") -> str:
    raw = f"{provider}_{model}{label_suffix}"
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", raw).strip("_")


def evaluate_question(
    caller,
    model: str,
    question: dict,
    execute_mode: bool,
    sample_index: int,
    temperature: float,
    oracle_config: dict | None = None,
    reference_record: dict | None = None,
    raw_completion: tuple[str, dict] | None = None,
    max_tokens: int = 2048,
) -> dict:
    reference_record = reference_record or {}
    base = {
        "question_id": _question_id(question),
        "sample_index": sample_index,
        "temperature": temperature,
        "category": question["category"],
        "difficulty": question.get("difficulty"),
        "prompt": question["prompt"],
        "correct_answer": question["correct_answer"],
        "correct_output": question["correct_output"],
        "reference_code": reference_record.get("reference_code"),
        "reference_output": reference_record.get("reference_output"),
        "reference_raw_output": reference_record.get("reference_raw_output"),
        "reference_execution_error": reference_record.get("reference_execution_error"),
        "reference_failed": bool(reference_record.get("reference_failed")),
    }
    try:
        raw_output, usage = raw_completion or caller(
            model,
            question["prompt"],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        extraction = extract_code(raw_output)
        model_output = extraction["extracted_code"]

        actual_output = None
        raw_actual_output = None
        execution_error = None
        oracle_result = None
        oracle_error = None
        correct = False
        judge = "static"
        extraction_error = extraction["extraction_error"]
        code_only_violation = bool(extraction["code_only_violation"])
        if execute_mode and reference_record and not reference_record.get("reference_failed"):
            target_output = reference_record.get("reference_output")
        else:
            target_output = question["correct_output"]

        if execute_mode and reference_record.get("reference_failed"):
            judge = "reference_failed"

        if execute_mode and not reference_record.get("reference_failed") and not extraction_error:
            from executor import run_m2
            actual_output, raw_actual_output = run_m2(model_output)
            if not actual_output and raw_actual_output.startswith(("TIMEOUT", "SUBPROCESS_ERROR")):
                execution_error = raw_actual_output
                actual_output = None
            elif raw_actual_output and _has_m2_error(raw_actual_output):
                execution_error = raw_actual_output

        scores = compute_scores(
            model_output,
            question["correct_answer"],
            target_output,
            category=question.get("category", ""),
            actual_output=actual_output if not reference_record.get("reference_failed") else None,
        )
        if execute_mode:
            scores.setdefault("execution_match", False)
            scores.setdefault("code_fuzzy_score", scores.get("fuzzy_score", 0.0))
        if execute_mode:
            if reference_record.get("reference_failed"):
                correct = False
                judge = "reference_failed"
            elif extraction_error:
                correct = False
                judge = "extraction_failed"
            else:
                correct = bool(outputs_match(actual_output, target_output))
                judge = "deterministic_exact" if correct else "deterministic_mismatch"
            if (
                not correct
                and not extraction_error
                and not reference_record.get("reference_failed")
                and actual_output is not None
                and oracle_config
            ):
                from oracle_grader import grade_output

                try:
                    oracle_result = grade_output(
                        expected_output=target_output,
                        actual_output=actual_output,
                        provider=oracle_config["provider"],
                        model=oracle_config["model"],
                        criteria=oracle_config["criteria"],
                        cache_dir=oracle_config.get("cache_dir"),
                    )
                    correct = bool(oracle_result["correct"])
                    judge = "oracle" if correct else "oracle_reject"
                except Exception as exc:
                    raw_oracle_response = getattr(exc, "raw_response", None)
                    if raw_oracle_response is not None:
                        oracle_result = {
                            "correct": None,
                            "reason": "",
                            "raw_response": raw_oracle_response,
                            "provider": oracle_config["provider"],
                            "model": oracle_config["model"],
                            "criteria": oracle_config["criteria"],
                            "usage": {},
                        }
                    oracle_error = str(exc)
                    judge = "oracle_error"
        else:
            correct = bool(scores.get("exact_match"))
            judge = "static_exact" if correct else "static_mismatch"

        result = {
            **base,
            "model_response": model_output,
            "raw_response": raw_output,
            "usage": usage,
            "scores": scores,
            "correct": correct,
            "judge": judge,
            "extracted_code": model_output,
            "extraction_method": extraction["extraction_method"],
            "extraction_error": extraction_error,
            "code_only_violation": code_only_violation,
            "preflight_error": extraction_error,
            "oracle_error": oracle_error,
        }
        if oracle_result is not None:
            result["oracle"] = oracle_result
        if execute_mode:
            result["actual_output"] = actual_output
            result["raw_actual_output"] = raw_actual_output
            result["execution_error"] = execution_error
        return result

    except Exception as exc:
        result = {
            **base,
            "model_response": None,
            "raw_response": None,
            "usage": {},
            "scores": _error_scores(execute_mode),
            "correct": False,
            "judge": "error",
            "extracted_code": None,
            "extraction_method": None,
            "extraction_error": None,
            "code_only_violation": False,
            "preflight_error": None,
            "error": str(exc),
        }
        if execute_mode:
            result["actual_output"] = None
            result["raw_actual_output"] = None
            result["execution_error"] = None
        return result


def reference_failed_result(
    question: dict,
    sample_index: int,
    temperature: float,
    reference_record: dict,
) -> dict:
    """Return a synthetic sample row for an unusable benchmark reference."""
    return {
        "question_id": _question_id(question),
        "sample_index": sample_index,
        "temperature": temperature,
        "category": question["category"],
        "difficulty": question.get("difficulty"),
        "prompt": question["prompt"],
        "correct_answer": question["correct_answer"],
        "correct_output": question["correct_output"],
        "reference_code": reference_record.get("reference_code"),
        "reference_output": reference_record.get("reference_output"),
        "reference_raw_output": reference_record.get("reference_raw_output"),
        "reference_execution_error": reference_record.get("reference_execution_error"),
        "reference_failed": True,
        "model_response": None,
        "raw_response": None,
        "usage": {},
        "scores": _error_scores(True),
        "correct": False,
        "judge": "reference_failed",
        "extracted_code": None,
        "extraction_method": None,
        "extraction_error": None,
        "code_only_violation": False,
        "preflight_error": None,
        "oracle_error": None,
        "actual_output": None,
        "raw_actual_output": None,
        "execution_error": None,
    }


def evaluate_question_batch(
    provider: str,
    caller,
    model: str,
    question: dict,
    execute_mode: bool,
    sample_indices: list[int],
    temperature: float,
    oracle_config: dict | None,
    reference_record: dict,
    max_tokens: int,
) -> list[dict]:
    """Evaluate one prompt for one or more requested samples."""
    completions: list[tuple[str, dict]] | None = None
    if (
        len(sample_indices) > 1
        and provider in BATCH_CALLERS
        and _BATCH_SUPPORT_CACHE.get(provider, True)
    ):
        try:
            completions = BATCH_CALLERS[provider](
                model,
                question["prompt"],
                len(sample_indices),
                temperature=temperature,
                max_tokens=max_tokens,
            )
            if len(completions) != len(sample_indices):
                completions = None
                _BATCH_SUPPORT_CACHE[provider] = False
            else:
                _BATCH_SUPPORT_CACHE[provider] = True
        except Exception:
            completions = None
            _BATCH_SUPPORT_CACHE[provider] = False

    results = []
    for offset, sample_index in enumerate(sample_indices):
        raw_completion = completions[offset] if completions is not None else None
        results.append(
            evaluate_question(
                caller,
                model,
                question,
                execute_mode,
                sample_index,
                temperature,
                oracle_config,
                reference_record,
                raw_completion=raw_completion,
                max_tokens=max_tokens,
            )
        )
    return results


def run_evaluation(
    providers: list[str],
    model_overrides: list[str] | None,
    benchmark_path: str,
    output_dir: str,
    delay: float,
    execute_mode: bool,
    num_samples: int,
    temperature: float,
    oracle_config: dict | None,
    workers: int = 1,
    reference_cache_path: str | None = None,
    require_reference_cache: bool = False,
    label_suffix: str = "",
    samples_per_request: int = 1,
    max_tokens: int = 2048,
    skip_existing_models: bool = False,
) -> dict[str, list[dict]]:
    with open(benchmark_path) as f:
        questions: list[dict] = json.load(f)
    reference_records: dict[str, dict] = {}
    if execute_mode:
        if require_reference_cache or reference_cache_path:
            cache_path = reference_cache_path or str(default_reference_cache_path(benchmark_path))
            reference_records = load_reference_cache(benchmark_path, cache_path)
            print(f"Loaded reference cache: {cache_path}")
        else:
            reference_records = compile_reference_records(questions, workers=workers)
        print_reference_failures(questions, reference_records)

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    all_results: dict[str, list[dict]] = {}

    for provider in providers:
        models = model_overrides if model_overrides else DEFAULT_MODELS[provider]
        caller = CALLERS[provider]

        for model in models:
            label = f"{provider}/{model}{label_suffix}"
            result_file = out / f"{_file_key(provider, model, label_suffix)}_results.json"
            if skip_existing_models and result_file.exists():
                print(f"\n=== {label} already complete; loading {result_file} ===")
                all_results[label] = json.loads(result_file.read_text())
                continue
            total = len(questions) * num_samples
            active_workers = max(1, min(workers, total))
            print(
                f"\n=== {label} ({len(questions)} questions, {num_samples} samples each, "
                f"workers={active_workers}) ==="
            )

            tasks: list[tuple[int, dict, list[int], dict]] = []
            completed: list[tuple[tuple[int, int], dict]] = []
            order = 0
            for question in questions:
                qid = _question_id(question)
                reference_record = reference_records.get(qid, {})
                if reference_record.get("reference_failed"):
                    for sample_index in range(num_samples):
                        order += 1
                        completed.append(
                            (
                                (order, 0),
                                reference_failed_result(
                                    question,
                                    sample_index,
                                    temperature,
                                    reference_record,
                                ),
                            )
                        )
                    continue
                for start in range(0, num_samples, samples_per_request):
                    order += 1
                    batch_indices = list(range(start, min(start + samples_per_request, num_samples)))
                    tasks.append((order, question, batch_indices, reference_record))

            total_requests = len(tasks)
            with ThreadPoolExecutor(max_workers=active_workers) as pool:
                futures = {}
                task_iter = iter(tasks)
                submitted = 0
                done_count = len(completed)

                def submit_next() -> bool:
                    nonlocal submitted
                    try:
                        order, question, sample_indices, reference_record = next(task_iter)
                    except StopIteration:
                        return False
                    future = pool.submit(
                        evaluate_question_batch,
                        provider,
                        caller,
                        model,
                        question,
                        execute_mode,
                        sample_indices,
                        temperature,
                        oracle_config,
                        reference_record,
                        max_tokens,
                    )
                    futures[future] = (order, _question_id(question), sample_indices)
                    submitted += 1
                    print(
                        f"  submitted requests {submitted}/{total_requests} "
                        f"(in-flight={len(futures)})",
                        end="\r",
                        flush=True,
                    )
                    if delay > 0 and submitted < total:
                        time.sleep(delay)
                    return True

                for _ in range(active_workers):
                    if not submit_next():
                        break

                while futures:
                    done, _ = wait(futures, return_when=FIRST_COMPLETED)
                    for future in done:
                        order, qid, sample_indices = futures.pop(future)
                        batch_results = future.result()
                        for offset, result in enumerate(batch_results):
                            completed.append(((order, offset), result))
                            done_count += 1
                            _print_sample_progress(done_count, total, qid, sample_indices[offset], result)
                        submit_next()

            results = [result for _, result in sorted(completed, key=lambda item: item[0])]

            result_file.write_text(json.dumps(results, indent=2))
            print(f"  -> {result_file}")

            all_results[label] = results

    return all_results


# ---------------------------------------------------------------------------
# Summary generation
# ---------------------------------------------------------------------------

def generate_summary(
    all_results: dict[str, list[dict]],
    execute_mode: bool,
    metric_names: list[str],
    pass_k: list[int],
) -> dict:
    summary: dict = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "execute_mode": execute_mode,
        "metrics_requested": metric_names,
        "pass_k": pass_k,
        "models": {},
        "by_category": {},
        "by_difficulty": {},
    }

    for label, results in all_results.items():
        reference_failed = [r for r in results if r.get("reference_failed")]
        valid = [r for r in results if not r.get("reference_failed")]
        n = len(valid)
        if n == 0:
            continue

        metric_values = compute_metrics(valid, metric_names, pass_k)
        question_count = len({r["question_id"] for r in valid})
        attempted_question_count = len({r["question_id"] for r in results})
        model_summary: dict = {
            "num_questions": question_count,
            "num_attempted_questions": attempted_question_count,
            "num_samples": n,
            "num_attempted_samples": len(results),
            "num_reference_failed_samples": len(reference_failed),
            "num_errors": sum(1 for r in valid if r.get("judge") == "error"),
            "temperature": valid[0].get("temperature") if valid else None,
            **metric_values,
        }

        if execute_mode:
            num_exec_matches = sum(1 for r in valid if r["scores"].get("execution_match"))
            model_summary["num_execution_matches"] = num_exec_matches
            model_summary["execution_match_rate"] = round(num_exec_matches / n, 4)
            model_summary["avg_code_fuzzy_score"] = round(
                sum(r["scores"].get("code_fuzzy_score", r["scores"].get("fuzzy_score", 0.0)) for r in valid) / n, 4
            )
        else:
            model_summary["exact_match_rate"] = round(
                sum(1 for r in valid if r["scores"]["exact_match"]) / n, 4
            )
            model_summary["output_match_rate"] = round(
                sum(1 for r in valid if r["scores"]["output_match"]) / n, 4
            )
            model_summary["avg_fuzzy_score"] = round(
                sum(r["scores"]["fuzzy_score"] for r in valid) / n, 4
            )

        summary["models"][label] = model_summary
        if reference_failed:
            failed_counts: dict[str, int] = {}
            for result in reference_failed:
                failed_counts[result["question_id"]] = failed_counts.get(result["question_id"], 0) + 1
            summary.setdefault("reference_failed", {})[label] = failed_counts
        if "pass_at_k" in metric_names:
            question_pass = compute_pass_at_k_by_question(
                valid,
                pass_k,
            )
            for question_id, values in question_pass.items():
                question_temps = {
                    r.get("temperature")
                    for r in valid
                    if r.get("question_id") == question_id
                }
                if len(question_temps) == 1:
                    values["temperature"] = next(iter(question_temps))
            summary.setdefault("by_question", {})[label] = question_pass

        cats: dict[str, list[bool]] = {}
        diffs: dict[str, list[bool]] = {}
        for r in valid:
            cats.setdefault(r["category"], []).append(bool(r["correct"]))
            diffs.setdefault(r.get("difficulty") or "unknown", []).append(
                bool(r["correct"])
            )

        summary["by_category"][label] = {c: round(sum(v) / len(v), 4) for c, v in cats.items()}
        summary["by_difficulty"][label] = {d: round(sum(v) / len(v), 4) for d, v in diffs.items()}

    return summary


# ---------------------------------------------------------------------------
# Leaderboard display
# ---------------------------------------------------------------------------

def print_leaderboard(summary: dict) -> None:
    models = summary.get("models", {})
    if not models:
        print("No results to display.")
        return

    metric_cols = [
        key
        for key in next(iter(models.values()))
        if key == "accuracy" or key.startswith("pass@")
    ]
    rank_key = metric_cols[0] if metric_cols else "accuracy"
    ranked = sorted(models.items(), key=lambda x: x[1].get(rank_key, 0.0), reverse=True)

    width = 46 + (12 * len(metric_cols))
    print("\n" + "=" * width)
    print("LEADERBOARD")
    print("=" * width)
    header = f"{'#':<4} {'Model':<38}" + "".join(f" {name:>10}" for name in metric_cols)
    print(header)
    print("-" * len(header))
    for rank, (label, s) in enumerate(ranked, 1):
        row = f"{rank:<4} {label:<38}" + "".join(
            f" {s.get(name, 0.0):>10.4f}" for name in metric_cols
        )
        print(row)
    print("=" * width)

    # Per-category breakdown
    by_cat = summary.get("by_category", {})
    all_cats = sorted({c for m in by_cat.values() for c in m})
    if all_cats:
        col = 14
        print("\nBY CATEGORY (avg composite):")
        header = f"{'Model':<38}" + "".join(f"  {c[:col]:>{col}}" for c in all_cats)
        print(header)
        print("-" * len(header))
        for label, cats in by_cat.items():
            row = f"{label:<38}" + "".join(
                f"  {cats.get(c, 0.0):>{col}.4f}" for c in all_cats
            )
            print(row)

    # Per-difficulty breakdown
    by_diff = summary.get("by_difficulty", {})
    all_diffs = sorted({d for m in by_diff.values() for d in m})
    if all_diffs:
        col = 10
        print("\nBY DIFFICULTY (avg composite):")
        header = f"{'Model':<38}" + "".join(f"  {d[:col]:>{col}}" for d in all_diffs)
        print(header)
        print("-" * len(header))
        for label, diffs in by_diff.items():
            row = f"{label:<38}" + "".join(
                f"  {diffs.get(d, 0.0):>{col}.4f}" for d in all_diffs
            )
            print(row)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate LLMs on Macaulay2 benchmark questions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"Available providers: {', '.join(ALL_PROVIDERS)}",
    )
    parser.add_argument(
        "--providers",
        nargs="+",
        default=["all"],
        metavar="PROVIDER",
        help="Providers to run (space-separated), or 'all'. Default: all.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=None,
        metavar="MODEL",
        help=(
            "Override default model list for every selected provider. "
            "Specify model names exactly as the provider's API expects them."
        ),
    )
    parser.add_argument(
        "--benchmark",
        required=True,
        metavar="PATH",
        help="Path to benchmark JSON file (array of question objects).",
    )
    parser.add_argument(
        "--output-dir",
        default="results",
        metavar="DIR",
        help="Directory for result files. Created if absent. Default: results/",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        metavar="SECONDS",
        help="Seconds to sleep between task submissions (default: 0.5).",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        metavar="N",
        help="Parallel sample evaluation workers per model. Default: 1.",
    )
    parser.add_argument(
        "--samples-per-request",
        type=int,
        default=1,
        metavar="N",
        help="Requested same-prompt completions per provider call when supported. Default: 1.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=2048,
        metavar="N",
        help="Maximum generated tokens per sample. Default: 2048.",
    )
    parser.add_argument(
        "--num-samples",
        type=int,
        default=1,
        metavar="N",
        help="Number of samples to generate per question/model. Default: 1.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        metavar="T",
        help="Generation temperature. Use nonzero values for meaningful pass@k. Default: 0.0.",
    )
    parser.add_argument(
        "--metrics",
        nargs="+",
        default=["accuracy"],
        choices=["accuracy", "pass_at_k"],
        help="Aggregate metrics to compute. Default: accuracy.",
    )
    parser.add_argument(
        "--pass-k",
        nargs="+",
        type=int,
        default=[1],
        metavar="K",
        help="k values for pass@k when --metrics includes pass_at_k. Default: 1.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        default=False,
        help="Run model output through M2 and score on runtime output instead of code strings.",
    )
    parser.add_argument(
        "--m2-smoke-check",
        action="store_true",
        default=False,
        help="Before running, verify M2 can execute a tiny expression.",
    )
    parser.add_argument(
        "--reference-cache",
        default=None,
        metavar="PATH",
        help=(
            "Compiled reference cache path for --execute. Defaults to "
            "results/reference_cache/<benchmark>_<hash>.json when --require-reference-cache is set."
        ),
    )
    parser.add_argument(
        "--require-reference-cache",
        action="store_true",
        default=False,
        help="In --execute mode, load compiled references from cache instead of compiling them inline.",
    )
    parser.add_argument(
        "--oracle-grader",
        action="store_true",
        default=False,
        help="Use a binary LLM oracle for execution-output mismatches.",
    )
    parser.add_argument(
        "--grader-provider",
        default="openai",
        metavar="PROVIDER",
        help="Provider for --oracle-grader. Default: openai.",
    )
    parser.add_argument(
        "--grader-model",
        default="gpt-5-2",
        metavar="MODEL",
        help="Model for --oracle-grader. Default: gpt-5-2.",
    )
    parser.add_argument(
        "--grader-criteria",
        default="default",
        choices=["default", "strict"],
        help="Named binary oracle criteria. Default: default.",
    )
    parser.add_argument(
        "--grader-cache-dir",
        default=None,
        metavar="DIR",
        help="Optional cache directory for oracle judgments.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    execute_mode = args.execute
    if execute_mode:
        if shutil.which("M2") is None:
            print(
                "Warning: M2 binary not found on PATH — falling back to static scoring.",
                file=sys.stderr,
            )
            execute_mode = False
        else:
            print("Execution mode enabled (M2 found).")
            if args.m2_smoke_check:
                from executor import smoke_check_m2

                ok, message = smoke_check_m2()
                if not ok:
                    sys.exit(message)
                print(message)

    if args.num_samples < 1:
        sys.exit("--num-samples must be at least 1")
    if args.workers < 1:
        sys.exit("--workers must be at least 1")
    if args.samples_per_request < 1:
        sys.exit("--samples-per-request must be at least 1")
    if args.max_tokens < 1:
        sys.exit("--max-tokens must be at least 1")
    if any(k < 1 for k in args.pass_k):
        sys.exit("--pass-k values must be at least 1")
    if "pass_at_k" in args.metrics and args.num_samples == 1 and any(k > 1 for k in args.pass_k):
        print(
            "Warning: pass@k with k > 1 is not meaningful with --num-samples 1.",
            file=sys.stderr,
        )

    if "all" in args.providers:
        selected = ALL_PROVIDERS
    else:
        selected = []
        for p in args.providers:
            if p not in ALL_PROVIDERS:
                sys.exit(
                    f"Unknown provider '{p}'. "
                    f"Valid choices: {', '.join(ALL_PROVIDERS)}"
                )
            selected.append(p)

    if not os.path.isfile(args.benchmark):
        sys.exit(f"Benchmark file not found: {args.benchmark}")

    oracle_config = None
    if args.oracle_grader:
        if not execute_mode:
            sys.exit("--oracle-grader requires --execute so actual compiled outputs exist")
        if args.grader_provider not in ALL_PROVIDERS:
            sys.exit(
                f"Unknown grader provider '{args.grader_provider}'. "
                f"Valid choices: {', '.join(ALL_PROVIDERS)}"
            )
        oracle_config = {
            "provider": args.grader_provider,
            "model": args.grader_model,
            "criteria": args.grader_criteria,
            "cache_dir": args.grader_cache_dir,
        }

    all_results = run_evaluation(
        providers=selected,
        model_overrides=args.models,
        benchmark_path=args.benchmark,
        output_dir=args.output_dir,
        delay=args.delay,
        execute_mode=execute_mode,
        num_samples=args.num_samples,
        temperature=args.temperature,
        oracle_config=oracle_config,
        workers=args.workers,
        reference_cache_path=args.reference_cache,
        require_reference_cache=args.require_reference_cache,
        samples_per_request=args.samples_per_request,
        max_tokens=args.max_tokens,
    )

    summary = generate_summary(all_results, execute_mode, args.metrics, args.pass_k)
    summary_file = Path(args.output_dir) / "summary.json"
    summary_file.write_text(json.dumps(summary, indent=2))
    print(f"\nSummary written to {summary_file}")
    csv_paths = write_run_csvs(args.output_dir, all_results, summary)
    print(f"Samples CSV written to {csv_paths['samples_csv']}")
    print(f"pass@k CSV written to {csv_paths['pass_at_k_csv']}")

    print_leaderboard(summary)


if __name__ == "__main__":
    main()
