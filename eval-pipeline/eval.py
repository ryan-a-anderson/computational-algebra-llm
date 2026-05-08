#!/usr/bin/env python3
"""Macaulay2 LLM evaluation pipeline."""

import argparse
import json
import os
import re
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from csv_exports import write_run_csvs
from providers import ALL_PROVIDERS, CALLERS, DEFAULT_MODELS, clean_response
from metrics import compute_metrics, compute_pass_at_k_by_question
from scoring import compute_scores, normalize_reference_code, outputs_match

load_dotenv()


def _error_scores(execute_mode: bool) -> dict:
    if execute_mode:
        return {"execution_match": False, "code_fuzzy_score": 0.0, "composite_score": 0.0}
    return {"exact_match": False, "output_match": False, "fuzzy_score": 0.0, "composite_score": 0.0}


def _question_id(question: dict) -> str:
    return question.get("id") or question.get("problem_ID") or question.get("question_id")


def _has_m2_error(raw_output: str) -> bool:
    lowered = raw_output.lower()
    return " error:" in lowered or "stdio:" in lowered or "--backtrace:" in lowered


def preflight_code_only(response: str) -> tuple[bool, str | None]:
    """Reject obvious non-code responses before sending text to M2."""
    text = response.strip()
    if not text:
        return False, "empty response"
    lowered = text.lower()
    if "```" in text:
        return False, "markdown code fence detected"
    if "<think" in lowered or "</think>" in lowered:
        return False, "thinking tag detected"

    prose_markers = [
        r"^\s*(okay|sure|here is|here's|the code|let me|i can|we need|to solve)\b",
        r"\b(the user|the question|this code|explanation|reasoning)\b",
    ]
    for pattern in prose_markers:
        if re.search(pattern, lowered, flags=re.MULTILINE):
            return False, "explanation/prose detected"
    return True, None


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


# ---------------------------------------------------------------------------
# Core evaluation
# ---------------------------------------------------------------------------

def _file_key(provider: str, model: str) -> str:
    safe = model.replace("/", "_").replace(" ", "_")
    return f"{provider}_{safe}"


def evaluate_question(
    caller,
    model: str,
    question: dict,
    execute_mode: bool,
    sample_index: int,
    temperature: float,
    oracle_config: dict | None = None,
    reference_record: dict | None = None,
) -> dict:
    reference_record = reference_record or {}
    base = {
        "question_id": _question_id(question),
        "sample_index": sample_index,
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
        raw_output, usage = caller(model, question["prompt"], temperature=temperature)
        model_output = raw_output.strip()

        actual_output = None
        raw_actual_output = None
        execution_error = None
        oracle_result = None
        oracle_error = None
        correct = False
        judge = "static"
        code_only_ok = True
        preflight_error = None
        if execute_mode and reference_record and not reference_record.get("reference_failed"):
            target_output = reference_record.get("reference_output")
        else:
            target_output = question["correct_output"]

        if execute_mode and reference_record.get("reference_failed"):
            judge = "reference_failed"
        else:
            code_only_ok, preflight_error = preflight_code_only(raw_output)

        if execute_mode and not reference_record.get("reference_failed") and code_only_ok:
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
            if reference_record.get("reference_failed"):
                correct = False
                judge = "reference_failed"
            elif not code_only_ok:
                correct = False
                judge = "preflight_reject"
            else:
                correct = bool(outputs_match(actual_output, target_output))
                judge = "deterministic_exact" if correct else "deterministic_mismatch"
            if (
                not correct
                and code_only_ok
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
            "code_only_violation": not code_only_ok,
            "preflight_error": preflight_error,
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
            "code_only_violation": False,
            "preflight_error": None,
            "error": str(exc),
        }
        if execute_mode:
            result["actual_output"] = None
            result["raw_actual_output"] = None
            result["execution_error"] = None
        return result


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
) -> dict[str, list[dict]]:
    with open(benchmark_path) as f:
        questions: list[dict] = json.load(f)
    reference_records: dict[str, dict] = {}
    if execute_mode:
        print(f"Compiling {len(questions)} reference answers with M2...")
        for question in questions:
            qid = _question_id(question)
            record = compile_reference(question)
            reference_records[qid] = record
            if record["reference_failed"]:
                print(f"  {qid:<14} reference_failed")

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    all_results: dict[str, list[dict]] = {}

    for provider in providers:
        models = model_overrides if model_overrides else DEFAULT_MODELS[provider]
        caller = CALLERS[provider]

        for model in models:
            label = f"{provider}/{model}"
            total = len(questions) * num_samples
            active_workers = max(1, min(workers, total))
            print(
                f"\n=== {label} ({len(questions)} questions, {num_samples} samples each, "
                f"workers={active_workers}) ==="
            )

            tasks: list[tuple[int, dict, int]] = []
            order = 0
            for question in questions:
                qid = _question_id(question)
                reference_record = reference_records.get(qid, {})
                for sample_index in range(num_samples):
                    order += 1
                    tasks.append((order, question, sample_index, reference_record))

            completed: list[tuple[int, dict]] = []
            with ThreadPoolExecutor(max_workers=active_workers) as pool:
                futures = {}
                for idx, (order, question, sample_index, reference_record) in enumerate(tasks, 1):
                    future = pool.submit(
                        evaluate_question,
                        caller,
                        model,
                        question,
                        execute_mode,
                        sample_index,
                        temperature,
                        oracle_config,
                        reference_record,
                    )
                    futures[future] = (order, _question_id(question), sample_index)
                    if delay > 0 and idx < total:
                        time.sleep(delay)

                for done_count, future in enumerate(as_completed(futures), 1):
                    order, qid, sample_index = futures[future]
                    result = future.result()
                    completed.append((order, result))
                    prefix = f"  [{done_count:>3}/{total}] {qid:<14} sample={sample_index}"
                    if result.get("error"):
                        print(f"{prefix}  ERROR: {result['error']}")
                    else:
                        print(
                            f"{prefix}  correct={'Y' if result['correct'] else 'n'}"
                            f"  judge={result['judge']}"
                        )

            results = [result for _, result in sorted(completed, key=lambda item: item[0])]

            result_file = out / f"{_file_key(provider, model)}_results.json"
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
            **metric_values,
        }

        if execute_mode:
            num_exec_matches = sum(1 for r in valid if r["scores"].get("execution_match"))
            model_summary["num_execution_matches"] = num_exec_matches
            model_summary["execution_match_rate"] = round(num_exec_matches / n, 4)
            model_summary["avg_code_fuzzy_score"] = round(
                sum(r["scores"]["code_fuzzy_score"] for r in valid) / n, 4
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
            summary.setdefault("by_question", {})[label] = compute_pass_at_k_by_question(
                valid,
                pass_k,
            )

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
