"""Helpers for loading completed model outputs and rebuilding run artifacts."""

import json
from pathlib import Path

from csv_exports import write_run_csvs
from eval import _file_key, generate_summary


COMPATIBILITY_KEYS = [
    "benchmark",
    "provider",
    "num_samples",
    "temperatures",
    "pass_k",
    "reference_cache",
    "compile_references",
    "oracle_grader",
    "grader_provider",
    "grader_model",
    "grader_criteria",
    "max_tokens",
    "top_p",
    "seed_policy",
]

COMPATIBILITY_DEFAULTS = {
    "max_tokens": 2048,
    "top_p": None,
    "seed_policy": "provider_default_unseeded",
}


def assert_compatible_run(existing: dict, requested: dict) -> None:
    mismatches = [
        key
        for key in COMPATIBILITY_KEYS
        if existing.get(key, COMPATIBILITY_DEFAULTS.get(key)) != requested.get(
            key,
            COMPATIBILITY_DEFAULTS.get(key),
        )
    ]
    if mismatches:
        details = ", ".join(
            f"{key}: existing={existing.get(key, COMPATIBILITY_DEFAULTS.get(key))!r} "
            f"requested={requested.get(key, COMPATIBILITY_DEFAULTS.get(key))!r}"
            for key in mismatches
        )
        raise ValueError(f"Incompatible existing run configuration: {details}")


def load_completed_results(run_dir: str | Path, config: dict) -> dict[str, list[dict]]:
    run = Path(run_dir)
    provider = config["provider"]
    temperatures = config.get("temperatures") or [config.get("temperature")]
    multi_temp = len(temperatures) > 1
    all_results: dict[str, list[dict]] = {}
    for temperature in temperatures:
        suffix = f" (T={temperature:g})" if multi_temp else ""
        for model in config.get("models", []):
            path = run / f"{_file_key(provider, model, suffix)}_results.json"
            if path.exists():
                all_results[f"{provider}/{model}{suffix}"] = json.loads(path.read_text())
    return all_results


def rebuild_run_artifacts(run_dir: str | Path) -> dict:
    run = Path(run_dir)
    config = json.loads((run / "run_config.json").read_text())
    all_results = load_completed_results(run, config)
    if not all_results:
        raise ValueError(f"No completed model result files found in {run}")
    summary = generate_summary(
        all_results,
        execute_mode=True,
        metric_names=["pass_at_k", "accuracy"],
        pass_k=config["pass_k"],
    )
    (run / "summary.json").write_text(json.dumps(summary, indent=2))
    csv_paths = write_run_csvs(run, all_results, summary)
    return {
        "models": list(all_results),
        "summary_json": str(run / "summary.json"),
        **csv_paths,
    }
