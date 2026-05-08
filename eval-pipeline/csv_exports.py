"""CSV export helpers for benchmark runs."""

import csv
import json
from pathlib import Path
from typing import Any


SAMPLE_COLUMNS = [
    "model",
    "question_id",
    "sample_index",
    "category",
    "difficulty",
    "prompt",
    "correct_answer",
    "correct_output",
    "reference_code",
    "reference_output",
    "reference_raw_output",
    "reference_execution_error",
    "reference_failed",
    "raw_response",
    "model_response",
    "code_only_violation",
    "preflight_error",
    "raw_actual_output",
    "actual_output",
    "correct",
    "judge",
    "execution_error",
    "error",
    "prompt_tokens",
    "completion_tokens",
    "total_tokens",
    "oracle_correct",
    "oracle_reason",
    "oracle_error",
    "oracle_provider",
    "oracle_model",
    "oracle_criteria",
]


PASS_AT_K_BASE_COLUMNS = [
    "model",
    "question_id",
    "num_samples",
    "num_correct",
    "num_attempted_samples",
    "num_reference_failed_samples",
]


def _jsonish(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return json.dumps(value, ensure_ascii=False)


def flatten_samples(all_results: dict[str, list[dict]]) -> list[dict]:
    """Flatten per-model sample JSON records for CSV export."""
    rows: list[dict] = []
    for model_label, results in all_results.items():
        for result in results:
            usage = result.get("usage") or {}
            oracle = result.get("oracle") or {}
            rows.append(
                {
                    "model": model_label,
                    "question_id": result.get("question_id"),
                    "sample_index": result.get("sample_index"),
                    "category": result.get("category"),
                    "difficulty": result.get("difficulty"),
                    "prompt": result.get("prompt"),
                    "correct_answer": _jsonish(result.get("correct_answer")),
                    "correct_output": result.get("correct_output"),
                    "reference_code": result.get("reference_code"),
                    "reference_output": result.get("reference_output"),
                    "reference_raw_output": result.get("reference_raw_output"),
                    "reference_execution_error": result.get("reference_execution_error"),
                    "reference_failed": result.get("reference_failed"),
                    "raw_response": result.get("raw_response"),
                    "model_response": result.get("model_response"),
                    "code_only_violation": result.get("code_only_violation"),
                    "preflight_error": result.get("preflight_error"),
                    "raw_actual_output": result.get("raw_actual_output"),
                    "actual_output": result.get("actual_output"),
                    "correct": result.get("correct"),
                    "judge": result.get("judge"),
                    "execution_error": result.get("execution_error"),
                    "error": result.get("error"),
                    "prompt_tokens": usage.get("prompt_tokens"),
                    "completion_tokens": usage.get("completion_tokens"),
                    "total_tokens": usage.get("total_tokens"),
                    "oracle_correct": oracle.get("correct"),
                    "oracle_reason": oracle.get("reason"),
                    "oracle_error": result.get("oracle_error"),
                    "oracle_provider": oracle.get("provider"),
                    "oracle_model": oracle.get("model"),
                    "oracle_criteria": oracle.get("criteria"),
                }
            )
    return rows


def flatten_pass_at_k(summary: dict) -> list[dict]:
    """Flatten per-question and aggregate pass@k data for CSV export."""
    rows: list[dict] = []
    pass_cols = [f"pass@{k}" for k in summary.get("pass_k", [])]

    for model_label, questions in summary.get("by_question", {}).items():
        for question_id, values in questions.items():
            row = {
                "model": model_label,
                "question_id": question_id,
                "num_samples": values.get("num_samples"),
                "num_correct": values.get("num_correct"),
                "num_attempted_samples": values.get("num_samples"),
                "num_reference_failed_samples": 0,
            }
            for col in pass_cols:
                row[col] = values.get(col)
            rows.append(row)

    for model_label, values in summary.get("models", {}).items():
        row = {
            "model": model_label,
            "question_id": "__aggregate__",
            "num_samples": values.get("num_samples"),
            "num_correct": values.get("num_correct"),
            "num_attempted_samples": values.get("num_attempted_samples"),
            "num_reference_failed_samples": values.get("num_reference_failed_samples"),
        }
        for col in pass_cols:
            row[col] = values.get(col)
        rows.append(row)

    for model_label, questions in summary.get("reference_failed", {}).items():
        for question_id, count in questions.items():
            rows.append(
                {
                    "model": model_label,
                    "question_id": question_id,
                    "num_samples": 0,
                    "num_correct": 0,
                    "num_attempted_samples": count,
                    "num_reference_failed_samples": count,
                }
            )

    return rows


def _write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_run_csvs(output_dir: str | Path, all_results: dict[str, list[dict]], summary: dict) -> dict:
    """Write standard CSV artifacts for a benchmark run."""
    out = Path(output_dir)
    pass_cols = [f"pass@{k}" for k in summary.get("pass_k", [])]
    samples_path = out / "samples.csv"
    pass_at_k_path = out / "pass_at_k.csv"

    _write_csv(samples_path, flatten_samples(all_results), SAMPLE_COLUMNS)
    _write_csv(
        pass_at_k_path,
        flatten_pass_at_k(summary),
        PASS_AT_K_BASE_COLUMNS + pass_cols,
    )
    return {
        "samples_csv": str(samples_path),
        "pass_at_k_csv": str(pass_at_k_path),
    }
