#!/usr/bin/env python3
"""Run a pass@k benchmark sweep over a set of models."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from csv_exports import write_run_csvs
from eval import default_reference_cache_path, generate_summary, print_leaderboard, run_evaluation
from executor import smoke_check_m2
from providers import DEFAULT_MODELS

load_dotenv()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a Macaulay2 pass@k model sweep.")
    parser.add_argument(
        "--benchmark",
        default="benchmarks/unified_benchmark.json",
        help="Benchmark JSON path. Default: benchmarks/unified_benchmark.json.",
    )
    parser.add_argument(
        "--provider",
        default="tinker",
        help="Provider to benchmark. Default: tinker.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=None,
        help="Models to benchmark. Defaults to the provider's configured model list.",
    )
    parser.add_argument(
        "--output-root",
        default="results/runs",
        help="Root directory for timestamped run folders. Default: results/runs.",
    )
    parser.add_argument(
        "--run-name",
        default=None,
        help="Optional run folder name. Defaults to a timestamp.",
    )
    parser.add_argument(
        "--num-samples",
        type=int,
        default=30,
        help="Samples per problem. Default: 30.",
    )
    parser.add_argument(
        "--temperature",
        nargs="+",
        type=float,
        default=[0.7],
        help="One or more sampling temperatures. Default: 0.7.",
    )
    parser.add_argument(
        "--pass-k",
        nargs="+",
        type=int,
        default=[1, 5, 10],
        help="k values for pass@k. Default: 1 5 10.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Delay between task submissions. Default: 0.0.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Parallel sample evaluation workers per model. Default: 4.",
    )
    parser.add_argument(
        "--reference-cache",
        default=None,
        help=(
            "Compiled reference cache path. Defaults to "
            "results/reference_cache/<benchmark>_<hash>.json."
        ),
    )
    parser.add_argument(
        "--compile-references",
        action="store_true",
        help="Compile references during this run instead of loading a cache. Default: require cache.",
    )
    parser.add_argument(
        "--oracle-grader",
        action="store_true",
        help="Use binary oracle grading on deterministic mismatches.",
    )
    parser.add_argument(
        "--grader-provider",
        default="openai",
        help="Oracle provider. Default: openai.",
    )
    parser.add_argument(
        "--grader-model",
        default="gpt-5-2",
        help="Oracle model. Default: gpt-5-2.",
    )
    parser.add_argument(
        "--grader-criteria",
        default="default",
        choices=["default", "strict"],
        help="Oracle criteria. Default: default.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.provider not in DEFAULT_MODELS:
        sys.exit(f"Unknown provider '{args.provider}'")
    if args.num_samples < 1:
        sys.exit("--num-samples must be at least 1")
    if args.workers < 1:
        sys.exit("--workers must be at least 1")
    if any(k < 1 for k in args.pass_k):
        sys.exit("--pass-k values must be at least 1")
    if any(k > args.num_samples for k in args.pass_k):
        sys.exit("--pass-k values must be <= --num-samples")
    temperatures = args.temperature
    if any(t < 0 for t in temperatures):
        sys.exit("--temperature values must be nonnegative")
    ok, message = smoke_check_m2()
    if not ok:
        sys.exit(message)
    print(message)
    reference_cache = args.reference_cache or str(default_reference_cache_path(args.benchmark))
    if not args.compile_references and not Path(reference_cache).exists():
        sys.exit(
            f"Reference cache not found: {reference_cache}\n"
            "Build it first with:\n"
            f"  python eval-pipeline/build_reference_cache.py "
            f"--benchmark {args.benchmark} --output {reference_cache} --workers {args.workers}\n"
            "Or rerun the sweep with --compile-references to compile references inline."
        )

    models = args.models or DEFAULT_MODELS[args.provider]
    run_name = args.run_name or datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_root) / run_name
    output_dir.mkdir(parents=True, exist_ok=True)

    oracle_config = None
    if args.oracle_grader:
        oracle_config = {
            "provider": args.grader_provider,
            "model": args.grader_model,
            "criteria": args.grader_criteria,
            "cache_dir": str(output_dir / "oracle_cache"),
        }

    config = {
        "benchmark": args.benchmark,
        "provider": args.provider,
        "models": models,
        "num_samples": args.num_samples,
        "temperature": temperatures[0] if len(temperatures) == 1 else None,
        "temperatures": temperatures,
        "pass_k": args.pass_k,
        "delay": args.delay,
        "workers": args.workers,
        "reference_cache": reference_cache,
        "compile_references": bool(args.compile_references),
        "oracle_grader": bool(args.oracle_grader),
        "grader_provider": args.grader_provider if args.oracle_grader else None,
        "grader_model": args.grader_model if args.oracle_grader else None,
        "grader_criteria": args.grader_criteria if args.oracle_grader else None,
    }
    (output_dir / "run_config.json").write_text(json.dumps(config, indent=2))

    all_results = {}
    for temperature in temperatures:
        print(f"\n### Temperature {temperature:g} ###")
        temp_results = run_evaluation(
            providers=[args.provider],
            model_overrides=models,
            benchmark_path=args.benchmark,
            output_dir=str(output_dir),
            delay=args.delay,
            execute_mode=True,
            num_samples=args.num_samples,
            temperature=temperature,
            oracle_config=oracle_config,
            workers=args.workers,
            reference_cache_path=None if args.compile_references else reference_cache,
            require_reference_cache=not args.compile_references,
            label_suffix=f" (T={temperature:g})" if len(temperatures) > 1 else "",
        )
        all_results.update(temp_results)

    summary = generate_summary(
        all_results,
        execute_mode=True,
        metric_names=["pass_at_k", "accuracy"],
        pass_k=args.pass_k,
    )
    summary_file = output_dir / "summary.json"
    summary_file.write_text(json.dumps(summary, indent=2))
    print(f"\nSummary written to {summary_file}")
    csv_paths = write_run_csvs(output_dir, all_results, summary)
    print(f"Samples CSV written to {csv_paths['samples_csv']}")
    print(f"pass@k CSV written to {csv_paths['pass_at_k_csv']}")
    print_leaderboard(summary)


if __name__ == "__main__":
    main()
