#!/usr/bin/env python3
"""Compile benchmark reference answers once and cache their M2 outputs."""

import argparse
import shutil
import sys

from dotenv import load_dotenv

from eval import default_reference_cache_path, write_reference_cache
from executor import smoke_check_m2

load_dotenv()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a cached set of compiled Macaulay2 reference outputs."
    )
    parser.add_argument(
        "--benchmark",
        default="benchmarks/unified_benchmark.json",
        help="Benchmark JSON path. Default: benchmarks/unified_benchmark.json.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Reference cache output path. Defaults to results/reference_cache/<benchmark>_<hash>.json.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Parallel M2 workers for reference compilation. Default: 4.",
    )
    parser.add_argument(
        "--no-smoke-check",
        action="store_true",
        help="Skip the M2 smoke check before compiling references.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.workers < 1:
        sys.exit("--workers must be at least 1")
    if shutil.which("M2") is None:
        sys.exit("M2 binary not found on PATH.")
    if not args.no_smoke_check:
        ok, message = smoke_check_m2()
        if not ok:
            sys.exit(message)
        print(message)

    output = args.output or default_reference_cache_path(args.benchmark)
    write_reference_cache(args.benchmark, output, workers=args.workers)


if __name__ == "__main__":
    main()
