#!/usr/bin/env python3
"""
Download Macaulay2 ComputationsBook examples from GitHub and convert them
to the same JSON training format as m2_training_data.json.

Each chapter.m2/test.m2 is paired with its .out.expected file.
The expected output is chunked into windows of CHUNK_SIZE statements
to keep examples within the model's max_length token budget.

Outputs:
  macaulay2-examples/computations_book_training_data.json
  macaulay2-examples/computations_book_training_data.md
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

BASE_URL = "https://raw.githubusercontent.com/Macaulay2/M2/stable/M2/Macaulay2/tests/ComputationsBook"

CHAPTERS = [
    "completeIntersections",
    "constructions",
    "d-modules",
    "exterior-algebra",
    "geometry",
    "monomialIdeals",
    "preface",
    "programming",
    "schemes",
    "solving",
    "toricHilbertScheme",
    "varieties",
]

# Each chapter contributes a "chapter" and a "test" pair
FILE_PAIRS = [("chapter.m2", "chapter.out.expected"), ("test.m2", "test.out.expected")]

# Group this many i/o statement blocks per training example
CHUNK_SIZE = 8

SYSTEM_PROMPT = (
    "You are an expert Macaulay2 programmer specializing in computational algebra. "
    "When given Macaulay2 code, execute it mentally and produce the exact output "
    "that Macaulay2 would return, including all intermediate results and type annotations."
)

OUTPUT_JSON = Path(__file__).parent / "computations_book_training_data.json"
OUTPUT_MD = Path(__file__).parent / "computations_book_training_data.md"


def fetch(url: str) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            raw = resp.read()
            # chapter.out.expected uses \x01 (ctrl-A) as the separator before
            # each "iN :" input-echo line; normalize to \n so the parser handles
            # both chapter and test files identically.
            return raw.replace(b"\x01", b"\n").decode("utf-8")
    except Exception as e:
        print(f"  WARN: could not fetch {url}: {e}")
        return None


def parse_expected_output(expected: str) -> list[dict]:
    """
    Parse an .out.expected file into a list of statement blocks.
    Each block has 'input_echo' (the iN: line) and 'output' (oN= ... oN: lines).
    """
    blocks = []
    # Split on input-prompt lines: "iN : " at the start of a line
    # The format is:  "i1 : <code>\n\no1 = <result>\n\no1 : <type>\n"
    parts = re.split(r"\n(?=i\d+ : )", expected)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Extract the input line (everything from "iN : " to the next blank line or "oN =")
        m = re.match(r"^(i\d+ : )(.*?)(?:\n\n|\n(?=o\d))(.*)", part, re.DOTALL)
        if not m:
            # Block with no output (e.g., pure comment or semicolons)
            input_echo = part
            output = ""
        else:
            input_echo = m.group(1) + m.group(2)
            output = m.group(3).strip()
        blocks.append({"input_echo": input_echo, "output": output})
    return blocks


def chunk_blocks(blocks: list[dict], chunk_size: int) -> list[tuple[str, str]]:
    """
    Group blocks into chunks of chunk_size and return (code_chunk, output_chunk) pairs.
    code_chunk: just the code text (stripping "iN : " prefix)
    output_chunk: the full iN/oN interleaved text
    """
    chunks = []
    for i in range(0, len(blocks), chunk_size):
        window = blocks[i : i + chunk_size]
        # Reconstruct code lines (strip "iN : " prefix)
        code_lines = []
        full_output_lines = []
        for b in window:
            # Strip prompt prefix from input echo for the "code" field
            code = re.sub(r"^i\d+ : ", "", b["input_echo"])
            code_lines.append(code)
            # Full output block
            full_output_lines.append(b["input_echo"])
            if b["output"]:
                full_output_lines.append("")
                full_output_lines.append(b["output"])
            full_output_lines.append("")
        code_chunk = "\n".join(code_lines).strip()
        output_chunk = "\n".join(full_output_lines).strip()
        if code_chunk:
            chunks.append((code_chunk, output_chunk))
    return chunks


def build_example(code: str, output: str, source: str) -> dict:
    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"What is the output of the following Macaulay2 code?\n\n"
                    f"```macaulay2\n{code}\n```"
                ),
            },
            {
                "role": "assistant",
                "content": f"```\n{output}\n```",
            },
        ],
        "metadata": {"source": source, "status": "verified"},
    }


def main():
    examples = []
    md_sections = [
        "# ComputationsBook Training Data\n",
        f"Downloaded from `Macaulay2/M2` stable branch, `tests/ComputationsBook/`.\n\n---\n\n",
    ]

    for chapter in CHAPTERS:
        print(f"[{chapter}]")
        for m2_file, expected_file in FILE_PAIRS:
            m2_url = f"{BASE_URL}/{chapter}/{m2_file}"
            exp_url = f"{BASE_URL}/{chapter}/{expected_file}"

            code_full = fetch(m2_url)
            expected_full = fetch(exp_url)

            if not code_full or not expected_full:
                print(f"  skipping {m2_file} (missing)")
                continue

            blocks = parse_expected_output(expected_full)
            if not blocks:
                print(f"  skipping {m2_file} (no parseable blocks)")
                continue

            chunks = chunk_blocks(blocks, CHUNK_SIZE)
            source_tag = f"{chapter}/{m2_file}"
            print(f"  {m2_file}: {len(blocks)} blocks → {len(chunks)} training chunks")

            for idx, (code_chunk, output_chunk) in enumerate(chunks):
                ex = build_example(code_chunk, output_chunk, f"{source_tag}[chunk{idx}]")
                examples.append(ex)

                md_sections.append(f"## {chapter} / {m2_file} — chunk {idx}\n\n")
                md_sections.append("### Input\n\n```macaulay2\n")
                md_sections.append(code_chunk)
                md_sections.append("\n```\n\n### Output\n\n```\n")
                md_sections.append(output_chunk)
                md_sections.append("\n```\n\n---\n\n")

    OUTPUT_JSON.write_text(json.dumps(examples, indent=2), encoding="utf-8")
    OUTPUT_MD.write_text("".join(md_sections), encoding="utf-8")
    print(f"\nWrote {len(examples)} training examples to {OUTPUT_JSON.name}")
    print(f"Wrote markdown to {OUTPUT_MD.name}")


if __name__ == "__main__":
    main()
