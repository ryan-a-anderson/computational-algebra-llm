#!/usr/bin/env python3
"""Run a pass@k benchmark sweep over a set of models."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from eval import default_reference_cache_path, load_reference_cache, print_leaderboard, run_evaluation
from executor import smoke_check_m2
from providers import CALLERS, DEFAULT_MODELS
from run_artifacts import assert_compatible_run, rebuild_run_artifacts

load_dotenv()


def preflight_model_calls(provider: str, models: list[str], temperature: float) -> None:
    """Make a tiny API call per model so unsupported IDs fail before a full sweep."""
    caller = CALLERS[provider]
    prompt = "In Macaulay2, compute 1 plus 1."
    print(f"\nPreflighting {len(models)} {provider} model call(s)...")
    failures: list[tuple[str, str]] = []
    for model in models:
        try:
            raw, _ = caller(model, prompt, temperature=temperature, max_tokens=32)
            preview = " ".join((raw or "").split())[:80]
            print(f"  OK   {model:<55} {preview}")
        except Exception as exc:
            failures.append((model, str(exc)))
            print(f"  FAIL {model:<55} {exc}")
    if failures:
        formatted = "\n".join(f"  - {model}: {error}" for model, error in failures)
        sys.exit(f"API preflight failed for {len(failures)} model(s):\n{formatted}")


def preflight_oracle_call(provider: str, model: str) -> None:
    caller = CALLERS[provider]
    print(f"\nPreflighting oracle grader: {provider}/{model}")
    try:
        raw, _ = caller(
            model,
            'Return only this JSON: {"correct": true, "reason": "ok"}',
            system_prompt='Return only valid JSON: {"correct": boolean, "reason": string}',
            temperature=0,
            max_tokens=64,
        )
        preview = " ".join((raw or "").split())[:80]
        print(f"  OK   {provider}/{model} {preview}")
    except Exception as exc:
        sys.exit(f"Oracle grader preflight failed for {provider}/{model}: {exc}")


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
        default=[1, 5, 10, 15, 20],
        help="k values for pass@k. Default: 1 5 10 15 20.",
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
        "--samples-per-request",
        type=int,
        default=1,
        help="Requested same-prompt completions per provider call when supported. Default: 1.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=2048,
        help="Maximum generated tokens per sample. Default: 2048.",
    )
    parser.add_argument(
        "--force-rerun",
        action="store_true",
        help="Rerun model outputs even when matching result files already exist in the run folder.",
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
        "--skip-api-preflight",
        action="store_true",
        help="Skip tiny model API calls before launching the sweep.",
    )
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Only test model and oracle API calls, then exit.",
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
    if args.samples_per_request < 1:
        sys.exit("--samples-per-request must be at least 1")
    if args.max_tokens < 1:
        sys.exit("--max-tokens must be at least 1")
    if any(k < 1 for k in args.pass_k):
        sys.exit("--pass-k values must be at least 1")
    if any(k > args.num_samples for k in args.pass_k):
        sys.exit("--pass-k values must be <= --num-samples")
    temperatures = args.temperature
    if any(t < 0 for t in temperatures):
        sys.exit("--temperature values must be nonnegative")
    models = args.models or DEFAULT_MODELS[args.provider]
    if args.oracle_grader and args.grader_provider not in CALLERS:
        sys.exit(f"Unknown grader provider '{args.grader_provider}'")
    if not args.skip_api_preflight:
        preflight_model_calls(args.provider, models, temperature=temperatures[0])
        if args.oracle_grader:
            preflight_oracle_call(args.grader_provider, args.grader_model)
        if args.preflight_only:
            print("\nAPI preflight passed.")
            return
    elif args.preflight_only:
        sys.exit("--preflight-only cannot be used with --skip-api-preflight")

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
        "samples_per_request": args.samples_per_request,
        "max_tokens": args.max_tokens,
        "top_p": None,
        "seed_policy": "provider_default_unseeded",
        "reference_cache": reference_cache,
        "compile_references": bool(args.compile_references),
        "oracle_grader": bool(args.oracle_grader),
        "grader_provider": args.grader_provider if args.oracle_grader else None,
        "grader_model": args.grader_model if args.oracle_grader else None,
        "grader_criteria": args.grader_criteria if args.oracle_grader else None,
    }
    config_path = output_dir / "run_config.json"
    if config_path.exists():
        existing_config = json.loads(config_path.read_text())
        try:
            assert_compatible_run(existing_config, config)
        except ValueError as exc:
            sys.exit(str(exc))
        merged_models = list(dict.fromkeys(existing_config.get("models", []) + models))
        config["models"] = merged_models
    config_path.write_text(json.dumps(config, indent=2))

    if not args.compile_references:
        reference_records = load_reference_cache(args.benchmark, reference_cache)
        failed_count = sum(1 for record in reference_records.values() if record.get("reference_failed"))
        total_questions = len(reference_records)
        valid_questions = total_questions - failed_count
        planned_calls = valid_questions * args.num_samples * len(models) * len(temperatures)
        avoided_calls = failed_count * args.num_samples * len(models) * len(temperatures)
        print(
            "\nRun plan:"
            f"\n  questions={total_questions} valid={valid_questions} reference_failed={failed_count}"
            f"\n  models_this_invocation={len(models)} temperatures={len(temperatures)}"
            f"\n  planned benchmark samples={planned_calls}"
            f"\n  skipped reference-failed samples={avoided_calls}"
            f"\n  samples_per_request={args.samples_per_request}"
        )

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
            samples_per_request=args.samples_per_request,
            max_tokens=args.max_tokens,
            skip_existing_models=not args.force_rerun,
        )
        all_results.update(temp_results)

    artifacts = rebuild_run_artifacts(output_dir)
    print(f"\nSummary written to {artifacts['summary_json']}")
    print(f"Samples CSV written to {artifacts['samples_csv']}")
    print(f"pass@k CSV written to {artifacts['pass_at_k_csv']}")
    summary = json.loads(Path(artifacts["summary_json"]).read_text())
    print_leaderboard(summary)


if __name__ == "__main__":
    main()
