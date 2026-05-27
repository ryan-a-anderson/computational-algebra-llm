#!/usr/bin/env python3
r"""
MathRepo Macaulay2 Scraper
==========================
Fetches all 26 M2 project pages (+ subpages) from mathrepo.mis.mpg.de
using the Claude API web_fetch tool, then parses markdown into structured JSON.

Usage:
    ANTHROPIC_API_KEY=... python mathrepo_scraper.py
    ANTHROPIC_API_KEY=... python mathrepo_scraper.py --output my_data.json

Output schema per project:
  {
    "project_name": str,
    "url": str,
    "title": str,
    "abstract": str,
    "latex_snippets": [str],   # all \(...\) and \[...\] preserved
    "sections": [
      {
        "heading": str,
        "prose": str,
        "code_blocks": [
          {"language": "m2_session"|"m2_code"|"unknown", "raw": str}
        ]
      }
    ],
    "subpages": [ <same structure, recursively> ]
  }
"""

import argparse
import json
import re
import time
from dataclasses import dataclass, field, asdict
from typing import Optional

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert

BASE = "https://mathrepo.mis.mpg.de"

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# All 26 Macaulay2 projects (from M2.html)
M2_PROJECTS = [
    ("An algorithm for the identifiability of rank-3 tensors",
     f"{BASE}/identifiabilityRank3tensors/index.html",
     ["implementation.html", "example.html"]),

    ("Combinatorics of Correlated Equilibria",
     f"{BASE}/correlated-equilibrium/index.html", []),

    ("Cox Homotopies",
     f"{BASE}/CoxHomotopies/index.html", []),

    ("D-Algebraic Functions",
     f"{BASE}/DAlgebraicFunctions/index.html",
     ["DAlgFunM2.html"]),

    ("Differential Equations for Gaussian Statistical Models",
     f"{BASE}/GaussianMLDeg1/index.html", []),

    ("Four-Dimensional Lie Algebras Revisited",
     f"{BASE}/Lie4/index.html", []),

    ("The Gaussian Moduli",
     f"{BASE}/GaussianModuli/index.html", []),

    ("Hirota Varieties and Rational Nodal Curves",
     f"{BASE}/HirotaVarietyRationalNodalCurve/index.html", []),

    ("The Hessian Discriminant",
     f"{BASE}/HessianDiscriminant/index.html", []),

    ("Identifiability in Continuous Lyapunov Models",
     f"{BASE}/LyapunovIdentifiability/index.html", []),

    ("Invitation to Nonlinear Algebra",
     f"{BASE}/InvitationToNonlinearAlgebra/index.html", []),

    ("Landau Discriminants",
     f"{BASE}/Landau/index.html", []),

    ("Lines on p-adic and real cubic surfaces",
     f"{BASE}/27pAdicLines/index.html", []),

    ("Macaulay2 bootcamp",
     f"{BASE}/M2_bootcamp/index.html",
     ["exercises.html", "transcripts.html"]),

    ("Marginal Independence Models",
     f"{BASE}/MarginalIndependence/index.html", []),

    ("Making waves with Macaulay 2",
     f"{BASE}/makingWaves/index.html", []),

    ("Multiplicity structure of the arc space of a fat point",
     f"{BASE}/MultiplicityStructureOfArcSpaces/index.html", []),

    ("No eleventh conditional Ingleton inequality",
     f"{BASE}/ConditionalIngleton/index.html", []),

    ("Primary Decomposition with Differential Operators",
     f"{BASE}/PrimaryDecompositionWithDifferentialOperators/index.html", []),

    ("Primary Ideals and Their Differential Equations",
     f"{BASE}/PrimaryIdealsandTheirDifferentialEquations/index.html",
     ["Macaulay2Code.html"]),

    ("Self-dual matroids from canonical curves",
     f"{BASE}/selfdual/index.html", []),

    ("Staged tree models with toric structure",
     f"{BASE}/StagedTreesWithToricStructures/index.html", []),

    ("Third-Order Moment Varieties of Linear Non-Gaussian Graphical Models",
     f"{BASE}/ThirdOrderMomentVarieties/index.html", []),

    ("Toric Degenerations of Cubic Surfaces",
     f"{BASE}/ToricDegenerationsCubics/index.html", []),

    ("Vector Spaces of Generalized Euler Integrals",
     f"{BASE}/EulerIntegrals/index.html", []),

    ("Connection Matrices in Macaulay2",
     f"{BASE}/ConnectionMatrices/index.html", []),
]


# ---------------------------------------------------------------------------
# Web fetching
# ---------------------------------------------------------------------------

def _unescape_latex_underscores(md: str) -> str:
    """Undo markdownify's \_ escaping inside LaTeX delimiters."""
    def fix(m):
        return m.group(0).replace(r'\_', '_')
    md = re.sub(r'\\\(.*?\\\)', fix, md, flags=re.DOTALL)
    md = re.sub(r'\\\[.*?\\\]', fix, md, flags=re.DOTALL)
    return md


def fetch_url(url: str) -> Optional[str]:
    """Fetch a URL and return its main content as markdown."""
    try:
        resp = requests.get(url, headers=_HEADERS, timeout=30)
        resp.raise_for_status()
        resp.encoding = 'utf-8'  # server often omits charset; default Latin-1 mangles UTF-8
        soup = BeautifulSoup(resp.text, "html.parser")

        # Strip nav/sidebar/footer elements before converting
        for tag in soup.find_all(["nav", "footer"]):
            tag.decompose()
        for tag in soup.find_all("a", class_="headerlink"):  # heading anchor icons (→ "ï")
            tag.decompose()
        for tag in soup.find_all("div", class_="sphinxsidebar"):
            tag.decompose()
        for tag in soup.find_all("div", attrs={"role": "navigation"}):
            tag.decompose()
        for tag in soup.find_all(attrs={"role": "contentinfo"}):
            tag.decompose()
        for tag in soup.find_all("div", class_=re.compile(r"\bfooter\b")):
            tag.decompose()

        content = (
            soup.find("main") or
            soup.find("div", {"id": "content"}) or
            soup.find("div", {"class": "content"}) or
            soup.find("article") or
            soup.find("body")
        )
        html = str(content) if content else resp.text
        result = md_convert(html, heading_style="ATX", code_language_callback=lambda el: "")
        cutoff = result.find("Project page created:")
        if cutoff != -1:
            result = result[:cutoff]
        result = _unescape_latex_underscores(result)
        return result
    except Exception as exc:
        print(f"  [fetch error] {exc}")
        return None


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

M2_SESSION_RE   = re.compile(r"^\s*i\d+\s*[:\s]", re.MULTILINE)
BUILD_OUTPUT_RE = re.compile(r"^\s*--\s*making example results for", re.MULTILINE)
LATEX_INLINE_RE = re.compile(r"\\\(.*?\\\)", re.DOTALL)
LATEX_BLOCK_RE  = re.compile(r"\\\[.*?\\\]",  re.DOTALL)
CODE_FENCE_RE   = re.compile(r"```(?:[^\n]*)?\n(.*?)```", re.DOTALL)

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

def extract_latex(text: str) -> list[str]:
    found = LATEX_INLINE_RE.findall(text) + LATEX_BLOCK_RE.findall(text)
    return list(dict.fromkeys(found))

def strip_nav(md: str) -> str:
    """Drop the repeated sidebar navigation, keep only the main content."""
    lines = md.split("\n")
    for i, line in enumerate(lines):
        # Main content starts at the first top-level heading that follows nav
        if re.match(r"^# [A-Z\[]", line):
            return "\n".join(lines[i:])
    return md

def clean_prose(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*",     r"\1", text)
    text = re.sub(r"`(.+?)`",       r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^[-*>]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def parse_markdown(project_name: str, url: str, md: str) -> dict:
    md = strip_nav(md)
    latex_all = extract_latex(md)

    # Lift code blocks out, replace with placeholders
    code_store: list[dict] = []
    def save_code(m):
        raw = m.group(1).strip()
        if not raw:
            return ""
        idx = len(code_store)
        code_store.append({"language": classify_code(raw), "raw": raw})
        return f"\n__CODE_{idx}__\n"

    prose_md = CODE_FENCE_RE.sub(save_code, md)

    # Parse sections
    sections = []
    title = ""
    abstract_parts = []
    cur_heading = ""
    cur_prose = []
    cur_codes = []
    in_abstract = True
    PLACEHOLDER = re.compile(r"^__CODE_(\d+)__$")

    def flush():
        nonlocal cur_heading, cur_prose, cur_codes
        prose = clean_prose("\n".join(cur_prose))
        cbs = list(cur_codes)
        if prose or cbs:
            sections.append({
                "heading": cur_heading,
                "prose": prose,
                "code_blocks": cbs,
            })
        cur_heading = ""
        cur_prose = []
        cur_codes = []

    for line in prose_md.split("\n"):
        # h1 — title
        m = re.match(r"^# (.+)", line)
        if m:
            title = clean_prose(m.group(1))
            if in_abstract:
                flush()
                in_abstract = False
            continue

        # h2-h4 — section heading
        m = re.match(r"^#{2,4} (.+)", line)
        if m:
            flush()
            in_abstract = False
            cur_heading = clean_prose(m.group(1))
            continue

        # code placeholder
        m = PLACEHOLDER.match(line.strip())
        if m:
            in_abstract = False
            cur_codes.append(code_store[int(m.group(1))])
            continue

        stripped = line.strip()
        if stripped:
            if in_abstract:
                abstract_parts.append(stripped)
            else:
                cur_prose.append(stripped)

    flush()

    abstract = clean_prose(" ".join(abstract_parts))

    return {
        "project_name": project_name,
        "url": url,
        "title": title or project_name,
        "abstract": abstract,
        "latex_snippets": latex_all,
        "sections": sections,
        "subpages": [],
    }


# ---------------------------------------------------------------------------
# Main scraper
# ---------------------------------------------------------------------------

def scrape(output_path: str = "mathrepo_m2_scraped.json", delay: float = 1.0,
           projects: list[str] | None = None):
    all_results = []

    candidates = M2_PROJECTS
    if projects:
        keywords = [k.lower() for k in projects]
        candidates = [p for p in M2_PROJECTS if any(kw in p[0].lower() for kw in keywords)]
        if not candidates:
            print(f"No projects matched keywords: {projects}")
            return []

    print(f"Scraping {len(candidates)} Macaulay2 project(s)...\n")

    for i, (name, index_url, subpage_names) in enumerate(candidates, 1):
        print(f"[{i:>2}/{len(candidates)}] {name[:60]}")

        # Fetch index page
        time.sleep(delay)
        md = fetch_url(index_url)
        if not md:
            print(f"  WARNING: failed to fetch {index_url}")
            all_results.append({
                "project_name": name, "url": index_url,
                "title": name, "abstract": "[fetch failed]",
                "latex_snippets": [], "sections": [], "subpages": []
            })
            continue

        project = parse_markdown(name, index_url, md)
        base_url = index_url.rsplit("/", 1)[0] + "/"

        # Fetch subpages
        for sp_name in subpage_names:
            sp_url = base_url + sp_name
            print(f"  -> {sp_name}")
            time.sleep(delay)
            sp_md = fetch_url(sp_url)
            if sp_md:
                sp_data = parse_markdown(name, sp_url, sp_md)
                project["subpages"].append(sp_data)

        all_results.append(project)

        # Save incrementally
        with open(output_path, "w") as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)

    # Final stats
    def count_code(results):
        n = 0
        for p in results:
            for s in p["sections"]:
                n += len(s["code_blocks"])
            for sp in p["subpages"]:
                for s in sp["sections"]:
                    n += len(s["code_blocks"])
        return n

    total_code  = count_code(all_results)
    total_latex = sum(len(p["latex_snippets"]) for p in all_results)
    m2_blocks   = sum(
        1 for p in all_results
        for s in p["sections"]
        for cb in s["code_blocks"]
        if cb["language"] in ("m2_code", "m2_session")
    )

    print(f"\n{'='*55}")
    print(f"Projects scraped : {len(all_results)}")
    print(f"Code blocks      : {total_code}  (M2-specific: {m2_blocks})")
    print(f"LaTeX snippets   : {total_latex}")
    print(f"Output           : {output_path}")

    return all_results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape MathRepo Macaulay2 projects")
    parser.add_argument("--output", default="mathrepo_m2_scraped.json",
                        help="Output JSON file path")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Delay between API calls (seconds)")
    parser.add_argument("--projects", nargs="+", metavar="KEYWORD",
                        help="Only scrape projects whose names contain these keywords (case-insensitive)")
    args = parser.parse_args()
    scrape(output_path=args.output, delay=args.delay, projects=args.projects)
