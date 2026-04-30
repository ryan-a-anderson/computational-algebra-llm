#!/usr/bin/env python3
"""Macaulay2 LLM evaluation pipeline."""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from providers import ALL_PROVIDERS, CALLERS, DEFAULT_MODELS, clean_response
from scoring import compute_scores

load_dotenv()

_ERROR_SCORES = {
    "exact_match": False,
    "output_match": False,
    "fuzzy_score": 0.0,
    "composite_score": 0.0,
}


# ---------------------------------------------------------------------------
# Core evaluation
# ---------------------------------------------------------------------------

def _file_key(provider: str, model: str) -> str:
    safe = model.replace("/", "_").replace(" ", "_")
    return f"{provider}_{safe}"


def evaluate_question(caller, model: str, question: dict) -> dict:
    base = {
        "question_id": question["id"],
        "category": question["category"],
        "difficulty": question.get("difficulty"),
        "prompt": question["prompt"],
        "correct_answer": question["correct_answer"],
        "correct_output": question["correct_output"],
    }
    try:
        raw_output, usage = caller(model, question["prompt"])
        model_output = clean_response(raw_output)
        scores = compute_scores(
            model_output,
            question["correct_answer"],
            question["correct_output"],
        )
        return {
            **base,
            "model_response": model_output,
            "raw_response": raw_output if raw_output != model_output else None,
            "usage": usage,
            "scores": scores,
        }
    except Exception as exc:
        return {
            **base,
            "model_response": None,
            "raw_response": None,
            "usage": {},
            "scores": _ERROR_SCORES,
            "error": str(exc),
        }


def run_evaluation(
    providers: list[str],
    model_overrides: list[str] | None,
    benchmark_path: str,
    output_dir: str,
    delay: float,
) -> dict[str, list[dict]]:
    with open(benchmark_path) as f:
        questions: list[dict] = json.load(f)

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    all_results: dict[str, list[dict]] = {}

    for provider in providers:
        models = model_overrides if model_overrides else DEFAULT_MODELS[provider]
        caller = CALLERS[provider]

        for model in models:
            label = f"{provider}/{model}"
            print(f"\n=== {label} ({len(questions)} questions) ===")
            results: list[dict] = []

            for idx, question in enumerate(questions, 1):
                print(f"  [{idx:>3}/{len(questions)}] {question['id']:<14}", end="", flush=True)
                result = evaluate_question(caller, model, question)
                results.append(result)

                if result.get("error"):
                    print(f"  ERROR: {result['error']}")
                else:
                    s = result["scores"]
                    print(
                        f"  composite={s['composite_score']:.3f}"
                        f"  exact={'Y' if s['exact_match'] else 'n'}"
                        f"  output={'Y' if s['output_match'] else 'n'}"
                    )

                if delay > 0 and idx < len(questions):
                    time.sleep(delay)

            result_file = out / f"{_file_key(provider, model)}_results.json"
            result_file.write_text(json.dumps(results, indent=2))
            print(f"  -> {result_file}")

            all_results[label] = results

    return all_results


# ---------------------------------------------------------------------------
# Summary generation
# ---------------------------------------------------------------------------

def generate_summary(all_results: dict[str, list[dict]]) -> dict:
    summary: dict = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "models": {},
        "by_category": {},
        "by_difficulty": {},
    }

    for label, results in all_results.items():
        valid = [r for r in results if r.get("model_response") is not None]
        n = len(valid)
        if n == 0:
            continue

        composites = [r["scores"]["composite_score"] for r in valid]
        summary["models"][label] = {
            "num_questions": n,
            "num_errors": len(results) - n,
            "avg_composite_score": round(sum(composites) / n, 4),
            "exact_match_rate": round(sum(1 for r in valid if r["scores"]["exact_match"]) / n, 4),
            "output_match_rate": round(sum(1 for r in valid if r["scores"]["output_match"]) / n, 4),
            "avg_fuzzy_score": round(sum(r["scores"]["fuzzy_score"] for r in valid) / n, 4),
        }

        cats: dict[str, list[float]] = {}
        diffs: dict[str, list[float]] = {}
        for r in valid:
            cats.setdefault(r["category"], []).append(r["scores"]["composite_score"])
            diffs.setdefault(r.get("difficulty") or "unknown", []).append(
                r["scores"]["composite_score"]
            )

        summary["by_category"][label] = {
            c: round(sum(v) / len(v), 4) for c, v in cats.items()
        }
        summary["by_difficulty"][label] = {
            d: round(sum(v) / len(v), 4) for d, v in diffs.items()
        }

    return summary


# ---------------------------------------------------------------------------
# Leaderboard display
# ---------------------------------------------------------------------------

def print_leaderboard(summary: dict) -> None:
    models = summary.get("models", {})
    if not models:
        print("No results to display.")
        return

    ranked = sorted(
        models.items(), key=lambda x: x[1]["avg_composite_score"], reverse=True
    )

    W = 84
    print("\n" + "=" * W)
    print("LEADERBOARD")
    print("=" * W)
    print(
        f"{'#':<4} {'Model':<38} {'Composite':>10} {'Exact%':>8} {'Output%':>9} {'Fuzzy':>7}"
    )
    print("-" * W)
    for rank, (label, s) in enumerate(ranked, 1):
        print(
            f"{rank:<4} {label:<38} "
            f"{s['avg_composite_score']:>10.4f} "
            f"{s['exact_match_rate']*100:>7.1f}% "
            f"{s['output_match_rate']*100:>8.1f}% "
            f"{s['avg_fuzzy_score']:>7.4f}"
        )
    print("=" * W)

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
        help="Seconds to sleep between API calls (default: 0.5).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

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

    all_results = run_evaluation(
        providers=selected,
        model_overrides=args.models,
        benchmark_path=args.benchmark,
        output_dir=args.output_dir,
        delay=args.delay,
    )

    summary = generate_summary(all_results)
    summary_file = Path(args.output_dir) / "summary.json"
    summary_file.write_text(json.dumps(summary, indent=2))
    print(f"\nSummary written to {summary_file}")

    print_leaderboard(summary)


if __name__ == "__main__":
    main()
