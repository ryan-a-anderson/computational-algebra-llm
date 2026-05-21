#!/usr/bin/env python3
"""Rebuild aggregate artifacts from completed model result JSON files."""

import argparse
from pathlib import Path

from run_artifacts import rebuild_run_artifacts


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild run summary and CSV artifacts.")
    parser.add_argument("run_dir", help="Path to a run directory under results/runs.")
    args = parser.parse_args()

    result = rebuild_run_artifacts(Path(args.run_dir))
    print(f"Summary written to {result['summary_json']}")
    print(f"Samples CSV written to {result['samples_csv']}")
    print(f"pass@k CSV written to {result['pass_at_k_csv']}")
    print(f"Included {len(result['models'])} completed model result file(s).")


if __name__ == "__main__":
    main()
