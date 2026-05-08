"""Macaulay2 code executor."""

import re
import shutil
import subprocess


def run_m2(code: str, timeout: int = 15) -> tuple[str, str]:
    """Execute M2 code, return (cleaned_output, raw_output).

    cleaned_output contains only the last expression's result (for scoring).
    raw_output contains the full session transcript (for debugging).
    Raises FileNotFoundError if M2 is not on PATH.
    Returns ("", error_message) on timeout or subprocess error.
    """
    m2_bin = shutil.which("M2")
    if m2_bin is None:
        raise FileNotFoundError("M2 binary not found on PATH")

    try:
        proc = subprocess.run(
            [m2_bin, "--no-readline", "--silent", "--stop"],
            input=code,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        raw = proc.stdout
        if proc.returncode != 0 and proc.stderr:
            raw = (raw + "\n" + proc.stderr).strip()
    except subprocess.TimeoutExpired:
        return "", f"TIMEOUT after {timeout}s"
    except Exception as exc:
        return "", f"SUBPROCESS_ERROR: {exc}"

    return _clean_m2_output(raw), raw


def smoke_check_m2(timeout: int = 10) -> tuple[bool, str]:
    """Check that M2 is on PATH and can execute a tiny expression."""
    try:
        output, raw = run_m2("1+1", timeout=timeout)
    except FileNotFoundError as exc:
        return False, str(exc)

    if output.strip() == "2":
        return True, "M2 smoke check passed: 1+1 -> 2"
    return False, f"M2 smoke check failed. cleaned_output={output!r}; raw_output={raw!r}"


def _trim_blank_edges(lines: list[str]) -> str:
    """Join lines, preserving internal blank lines but stripping leading/trailing ones."""
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def _clean_m2_output(raw: str) -> str:
    """Return cleaned output for the last M2 expression only.

    Parses oN blocks and discards everything except the final one so
    intermediate results don't pollute scoring. Falls back to all
    non-input-echo lines when no oN block is found (e.g., a top-level
    error before any expression completes).
    """
    # blocks: list of (n, kind, lines) where kind is '=' or ':'
    blocks: list[tuple[str, str, list[str]]] = []
    current_lines: list[str] | None = None
    current_n: str = ""
    current_kind: str = ""

    for line in raw.splitlines():
        if re.match(r"^i\d+ :", line):
            continue
        m = re.match(r"^o(\d+) ([=:])", line)
        if m:
            if current_lines is not None:
                blocks.append((current_n, current_kind, current_lines))
            current_n = m.group(1)
            current_kind = m.group(2)
            stripped = re.sub(r"^o\d+ [=:] ?", "", line)
            current_lines = [stripped] if stripped.strip() else []
        elif current_lines is not None:
            current_lines.append(line)

    if current_lines is not None:
        blocks.append((current_n, current_kind, current_lines))

    if not blocks:
        lines = [
            line.strip() for line in raw.splitlines()
            if not re.match(r"^i\d+ :", line)
        ]
        return _trim_blank_edges(lines)

    last_n = blocks[-1][0]
    last_blocks = [(kind, lines) for n, kind, lines in blocks if n == last_n]
    value_blocks = [lines for kind, lines in last_blocks if kind == "="]
    chosen = value_blocks[-1] if value_blocks else last_blocks[-1][1]
    return _trim_blank_edges([line.strip() for line in chosen])
