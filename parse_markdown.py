#!/usr/bin/env python3
"""
Parse MathRepo markdown pages (as returned by web_fetch) into structured JSON.

Input:  A list of {project_name, url, markdown, subpages} dicts.
Output: mathrepo_m2_scraped.json

Code block language classifications:
  "m2_session"    - has i1:, o1: style interactive transcript
  "m2_code"       - has M2 keywords but no session markers
  "build_output"  - M2 build/install log lines (-- making example results...)
  "unknown"       - none of the above
"""

import json
import re
from dataclasses import dataclass, field, asdict
from typing import Optional


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class CodeBlock:
    language: str   # "m2_session" | "m2_code" | "build_output" | "unknown"
    raw: str

@dataclass
class Section:
    heading: str
    prose: str
    code_blocks: list[CodeBlock] = field(default_factory=list)

@dataclass
class ScrapedPage:
    project_name: str
    url: str
    title: str
    abstract: str
    latex_snippets: list[str] = field(default_factory=list)
    sections: list[Section] = field(default_factory=list)
    subpages: list[dict] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

M2_SESSION_RE    = re.compile(r"^\s*i\d+\s*[:\s]", re.MULTILINE)
BUILD_OUTPUT_RE  = re.compile(r"^\s*--\s*making example results for", re.MULTILINE)
LATEX_INLINE_RE  = re.compile(r"\\\(.*?\\\)", re.DOTALL)
LATEX_BLOCK_RE   = re.compile(r"\\\[.*?\\\]",  re.DOTALL)
CODE_FENCE_RE    = re.compile(r"```(?:[^\n]*)?\n(.*?)```", re.DOTALL)

M2_KEYWORDS = [
    # package / environment
    "needsPackage", "installPackage", "loadPackage", "viewHelp",
    "debug Core", "path =",
    # ring / ideal / module
    "ideal ", "ideal(", "ring ", "module ", "matrix ", "matrix{{",
    "kernel ", "cokernel", "QQ[", "ZZ[", "RR[", "CC[", "GF(",
    # operators / syntax
    ":=", "-> ", "=>",
    # common functions
    "res ", "betti ", "hilbert", "primaryDecomposition", "groebnerBasis",
    "makeWA", "netList", "toList", "apply(", "scan(", "select(",
    "mingens", "radical", "saturate", "quotient", "intersect",
    "dim ", "degree ", "genus ", "codim ",
    "substitute", "submatrix", "transpose",
    "for i ", "while ", "new Type",
]

def classify_code(text: str) -> str:
    if M2_SESSION_RE.search(text):
        return "m2_session"
    if BUILD_OUTPUT_RE.search(text):
        return "build_output"
    if any(kw in text for kw in M2_KEYWORDS):
        return "m2_code"
    return "unknown"


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def extract_latex(text: str) -> list[str]:
    found = LATEX_INLINE_RE.findall(text) + LATEX_BLOCK_RE.findall(text)
    return list(dict.fromkeys(found))  # dedupe, preserve order

def strip_nav(md: str) -> str:
    """Drop the repeated sidebar navigation block."""
    lines = md.split("\n")
    for i, line in enumerate(lines):
        if re.match(r"^# [A-Z\[]", line):
            return "\n".join(lines[i:])
    return md

def clean_prose(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)          # bold
    text = re.sub(r"\*(.+?)\*",     r"\1", text)           # italic
    text = re.sub(r"`(.+?)`",       r"\1", text)           # inline code
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links
    text = re.sub(r"^[-*>]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Main parser
# ---------------------------------------------------------------------------

def parse_markdown(project_name: str, url: str, md: str) -> ScrapedPage:
    md = strip_nav(md)
    latex_all = extract_latex(md)

    # Pull code blocks out, replace with placeholders so prose walk is clean
    code_store: list[CodeBlock] = []

    def save_code(m):
        raw = m.group(1).strip()
        if not raw:
            return ""
        idx = len(code_store)
        code_store.append(CodeBlock(language=classify_code(raw), raw=raw))
        return f"\n__CODE_{idx}__\n"

    prose_md = CODE_FENCE_RE.sub(save_code, md)

    PLACEHOLDER = re.compile(r"^__CODE_(\d+)__$")

    sections: list[Section] = []
    title = ""
    abstract_parts: list[str] = []
    cur_heading = ""
    cur_prose: list[str] = []
    cur_codes: list[CodeBlock] = []
    in_abstract = True

    def flush():
        nonlocal cur_heading, cur_prose, cur_codes
        prose = clean_prose("\n".join(cur_prose))
        if prose or cur_codes:
            sections.append(Section(
                heading=cur_heading,
                prose=prose,
                code_blocks=list(cur_codes),
            ))
        cur_heading = ""
        cur_prose.clear()
        cur_codes.clear()

    for line in prose_md.split("\n"):
        # h1 — page title
        m = re.match(r"^# (.+)", line)
        if m:
            title = clean_prose(m.group(1))
            if in_abstract:
                flush()
                in_abstract = False
            continue

        # h2–h4 — section heading
        m = re.match(r"^#{2,4} (.+)", line)
        if m:
            flush()
            in_abstract = False
            cur_heading = clean_prose(m.group(1))
            continue

        # code placeholder
        m = PLACEHOLDER.match(line.strip())
        if m:
            if in_abstract:
                in_abstract = False
                flush()
            cur_codes.append(code_store[int(m.group(1))])
            continue

        stripped = line.strip()
        if stripped.startswith("Project page created:"):
            break
        if stripped:
            if in_abstract:
                abstract_parts.append(stripped)
            else:
                cur_prose.append(stripped)

    flush()

    abstract = clean_prose(" ".join(abstract_parts))

    return ScrapedPage(
        project_name=project_name,
        url=url,
        title=title or project_name,
        abstract=abstract,
        latex_snippets=latex_all,
        sections=sections,
    )


# ---------------------------------------------------------------------------
# Batch processor (called by scraper)
# ---------------------------------------------------------------------------

def process_pages(pages: list[dict]) -> list[dict]:
    """pages = list of {project_name, url, markdown, subpages: [{url, markdown}]}"""
    results = []
    for p in pages:
        main = parse_markdown(p["project_name"], p["url"], p["markdown"])
        for sp in p.get("subpages", []):
            sub = parse_markdown(p["project_name"], sp["url"], sp["markdown"])
            main.subpages.append(asdict(sub))
        results.append(asdict(main))
    return results


# ---------------------------------------------------------------------------
# CLI: pipe in raw JSON, get parsed JSON out
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    raw = json.load(sys.stdin)
    out = process_pages(raw)

    total_code = sum(len(s["code_blocks"]) for p in out for s in p["sections"]) \
               + sum(len(s["code_blocks"]) for p in out for sp in p["subpages"] for s in sp["sections"])
    total_latex = sum(len(p["latex_snippets"]) for p in out)
    by_lang: dict[str, int] = {}
    for p in out:
        for s in p["sections"]:
            for cb in s["code_blocks"]:
                by_lang[cb["language"]] = by_lang.get(cb["language"], 0) + 1

    print(f"Projects    : {len(out)}", file=sys.stderr)
    print(f"Code blocks : {total_code}", file=sys.stderr)
    for lang, n in sorted(by_lang.items()):
        print(f"  {lang:<16}: {n}", file=sys.stderr)
    print(f"LaTeX       : {total_latex}", file=sys.stderr)

    out_path = "mathrepo_m2_scraped.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Written to  : {out_path}", file=sys.stderr)
