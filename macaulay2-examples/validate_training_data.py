#!/usr/bin/env python3
"""
Validate training examples by running the M2 code through Macaulay2.

Reads macaulay2-examples/m2_code_gen_training.json, runs each assistant-turn
code snippet through `M2 --script`, and writes a filtered version that keeps
only examples where:
  - The code exits with return code 0, OR
  - source is "augmented_benchmark" (trusted existing data, not re-validated)

Usage:
    python validate_training_data.py [--timeout N] [--skip-benchmark] [--in FILE] [--out FILE]
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
DEFAULT_INPUT = ROOT / "macaulay2-examples" / "m2_code_gen_training.json"
DEFAULT_OUTPUT = ROOT / "macaulay2-examples" / "m2_code_gen_training_validated.json"
M2_BINARY = "/opt/homebrew/bin/M2"


def run_m2(code: str, timeout: int) -> tuple[bool, str]:
    """Run M2 code snippet. Returns (success, stderr_snippet)."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".m2", delete=False) as f:
        f.write(code + "\nexit 0\n")
        script_path = f.name

    try:
        result = subprocess.run(
            [M2_BINARY, "--script", script_path],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        stderr = result.stderr.strip()
        # M2 exits 0 even on error in some cases, so also check stderr for error markers
        has_error = (
            result.returncode != 0
            or "error:" in stderr.lower()
            or "stdio:error" in stderr.lower()
        )
        return not has_error, stderr[:200]
    except subprocess.TimeoutExpired:
        return False, f"timeout after {timeout}s"
    except Exception as e:
        return False, str(e)
    finally:
        Path(script_path).unlink(missing_ok=True)


def parse_args():
    p = argparse.ArgumentParser(description="Validate M2 code in training data")
    p.add_argument("--timeout", type=int, default=15, help="Seconds per M2 run (default: 15)")
    p.add_argument(
        "--skip-benchmark",
        action="store_true",
        help="Skip validation of augmented_benchmark examples (already trusted)",
    )
    p.add_argument("--in", dest="input", default=str(DEFAULT_INPUT), help="Input JSON file")
    p.add_argument("--out", dest="output", default=str(DEFAULT_OUTPUT), help="Output JSON file")
    return p.parse_args()


def main():
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"ERROR: {input_path} not found. Run generate_training_data.py first.", file=sys.stderr)
        sys.exit(1)

    with open(input_path) as f:
        examples = json.load(f)
    print(f"Loaded {len(examples)} examples from {input_path.name}")

    passed, skipped, failed = [], 0, 0
    total = len(examples)

    for i, ex in enumerate(examples):
        source = ex.get("metadata", {}).get("source", "")
        code = ex["messages"][2]["content"]  # assistant turn

        # Optionally trust benchmark examples without re-running them
        if args.skip_benchmark and source == "augmented_benchmark":
            ex["metadata"]["verified"] = True
            passed.append(ex)
            skipped += 1
            continue

        ok, err = run_m2(code, args.timeout)
        ex["metadata"]["verified"] = ok
        if ok:
            passed.append(ex)
        else:
            failed += 1

        if (i + 1) % 50 == 0 or (i + 1) == total:
            print(f"  [{i+1}/{total}] pass={len(passed)} fail={failed} skip={skipped}")

    print(f"\nResults: {len(passed)} passed, {failed} failed, {skipped} skipped (trusted)")
    print(f"Keeping {len(passed)}/{total} examples ({100*len(passed)//total}%)")

    with open(output_path, "w") as f:
        json.dump(passed, f, indent=2)
    print(f"Saved validated dataset to {output_path}")


if __name__ == "__main__":
    main()
