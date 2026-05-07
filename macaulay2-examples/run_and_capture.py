#!/usr/bin/env python3
"""
Run all Macaulay2 examples in raw_examples/yulia-m2/, capture output,
and write results to a markdown file and a JSON file for fine-tuning.
"""

import json
import os
import re  # still used for restart stripping
import subprocess
import sys
import time
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent / "raw_examples" / "yulia-m2"
OUTPUT_MD = Path(__file__).parent / "m2_training_data.md"
OUTPUT_JSON = Path(__file__).parent / "m2_training_data.json"
M2_BINARY = "M2"
TIMEOUT_SECONDS = 90

def strip_m2_header(output: str) -> str:
    lines = output.splitlines()
    filtered = [
        l for l in lines
        if not l.startswith("Macaulay2, version ")
        and l.strip() != 'Type "help" to see useful commands'
    ]
    return "\n".join(filtered).strip()


def run_m2_file(filepath: Path) -> dict:
    code = filepath.read_text(encoding="utf-8")
    # Remove restart commands — they kill the session when piping stdin
    code_clean = re.sub(r"^\s*restart\s*$", "", code, flags=re.MULTILINE)

    start = time.time()
    try:
        result = subprocess.run(
            [M2_BINARY, "--no-prompts"],
            input=code_clean,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
        elapsed = time.time() - start
        raw_output = result.stdout + (("\n-- STDERR --\n" + result.stderr) if result.stderr.strip() else "")
        output = strip_m2_header(raw_output)
        status = "success"
    except subprocess.TimeoutExpired:
        elapsed = TIMEOUT_SECONDS
        output = f"-- TIMED OUT after {TIMEOUT_SECONDS}s --"
        status = "timeout"
    except Exception as e:
        elapsed = time.time() - start
        output = f"-- ERROR: {e} --"
        status = "error"

    return {
        "filename": filepath.name,
        "code": code,
        "code_clean": code_clean,
        "output": output,
        "status": status,
        "elapsed": round(elapsed, 2),
    }


def write_markdown(results: list[dict]) -> None:
    lines = [
        "# Macaulay2 Examples: Input & Output\n",
        f"Generated from `raw_examples/yulia-m2/` — {len(results)} files.\n",
        "Each section shows the source code and its Macaulay2 output.\n\n",
        "---\n",
    ]

    for r in results:
        status_icon = {"success": "✓", "timeout": "⏱", "error": "✗"}.get(r["status"], "?")
        lines.append(f"## {r['filename']}\n")
        lines.append(f"**Status:** {status_icon} {r['status']} ({r['elapsed']}s)\n\n")
        lines.append("### Input\n\n```macaulay2\n")
        lines.append(r["code"].rstrip())
        lines.append("\n```\n\n")
        lines.append("### Output\n\n```\n")
        lines.append(r["output"].rstrip() if r["output"] else "(no output)")
        lines.append("\n```\n\n---\n\n")

    OUTPUT_MD.write_text("".join(lines), encoding="utf-8")
    print(f"Markdown written to {OUTPUT_MD}")


def write_json(results: list[dict]) -> None:
    training_examples = []
    for r in results:
        if r["status"] == "timeout" or not r["output"].strip():
            continue
        training_examples.append({
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an expert Macaulay2 programmer specializing in computational algebra. "
                        "When given Macaulay2 code, execute it mentally and produce the exact output "
                        "that Macaulay2 would return, including all intermediate results and type annotations."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"What is the output of the following Macaulay2 code?\n\n"
                        f"```macaulay2\n{r['code'].strip()}\n```"
                    ),
                },
                {
                    "role": "assistant",
                    "content": f"```\n{r['output'].strip()}\n```",
                },
            ],
            "metadata": {
                "filename": r["filename"],
                "status": r["status"],
                "elapsed": r["elapsed"],
            },
        })

    OUTPUT_JSON.write_text(json.dumps(training_examples, indent=2), encoding="utf-8")
    print(f"JSON written to {OUTPUT_JSON} ({len(training_examples)} training examples)")


def main():
    m2_files = sorted(EXAMPLES_DIR.glob("*.m2"))
    if not m2_files:
        print(f"No .m2 files found in {EXAMPLES_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(m2_files)} .m2 files. Running with {TIMEOUT_SECONDS}s timeout each...\n")
    results = []
    for i, fp in enumerate(m2_files, 1):
        print(f"[{i:2d}/{len(m2_files)}] {fp.name} ... ", end="", flush=True)
        r = run_m2_file(fp)
        results.append(r)
        icon = {"success": "✓", "timeout": "⏱", "error": "✗"}.get(r["status"], "?")
        print(f"{icon} ({r['elapsed']}s)")

    write_markdown(results)
    write_json(results)

    success = sum(1 for r in results if r["status"] == "success")
    timeouts = sum(1 for r in results if r["status"] == "timeout")
    errors = sum(1 for r in results if r["status"] == "error")
    print(f"\nDone: {success} success, {timeouts} timeout, {errors} error")


if __name__ == "__main__":
    main()
