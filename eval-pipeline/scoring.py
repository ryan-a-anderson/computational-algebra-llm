"""Scoring logic for Macaulay2 LLM evaluation."""

import re
from difflib import SequenceMatcher


def _normalize_code(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"```[^\n]*\n?", "", text)
    text = re.sub(r"```", "", text)
    return text.strip().lower()


def _normalize_output(text: str) -> str:
    """Normalize for comparison: strip per-line whitespace, collapse runs of blank lines,
    remove leading/trailing blank lines. Internal blank lines are kept (collapsed to one)
    so M2 matrix formatting survives minor spacing differences."""
    lines = [l.strip() for l in text.splitlines()]
    collapsed: list[str] = []
    prev_blank = False
    for l in lines:
        if not l:
            if not prev_blank:
                collapsed.append(l)
            prev_blank = True
        else:
            collapsed.append(l)
            prev_blank = False
    while collapsed and not collapsed[0]:
        collapsed.pop(0)
    while collapsed and not collapsed[-1]:
        collapsed.pop()
    result = "\n".join(collapsed).lower()
    result = re.sub(r",\s+", ",", result)
    return result


def normalize_reference_code(value: str | list[str] | None) -> str:
    """Normalize benchmark reference code across older JSON schema variants."""
    if value is None:
        return ""
    if isinstance(value, list):
        return "\n".join(str(part) for part in value)
    return str(value)


def outputs_match(actual_output: str | None, correct_output: str | None) -> bool:
    """Return whether an executed output matches the benchmark target."""
    return bool(correct_output) and actual_output is not None and (
        _normalize_output(actual_output) == _normalize_output(correct_output)
    )


def compute_scores(
    model_code: str,
    correct_answer: str | list[str],
    correct_output: str,
    category: str = "",
    actual_output: str | None = None,
) -> dict:
    """Compute scores for one question.

    Execution mode (actual_output provided):
      - debugging: composite = fuzzy match on code string
      - all others: composite = binary output_match
    Static mode (actual_output=None): output_match is False (no execution run).
    """
    code_fuzzy = round(
        SequenceMatcher(
            None,
            _normalize_code(model_code),
            _normalize_code(normalize_reference_code(correct_answer)),
        ).ratio(),
        4,
    )

    # output_match compares actual M2 execution output against the expected output
    output_match = outputs_match(actual_output, correct_output)

    if actual_output is not None:
        is_debugging = category.strip().lower() == "debugging"
        composite = code_fuzzy if is_debugging else (1.0 if output_match else 0.0)
        return {
            "execution_match": output_match,
            "output_match": output_match,
            "code_fuzzy_score": code_fuzzy,
            "composite_score": round(composite, 4),
        }

    # Static mode — no execution, so output_match is always False
    norm_resp = _normalize_code(model_code)
    norm_ans = _normalize_code(normalize_reference_code(correct_answer))
    exact = norm_resp == norm_ans
    if exact:
        composite = 1.0
    else:
        composite = round(code_fuzzy * 0.5, 4)
    return {
        "exact_match": exact,
        "output_match": output_match,
        "fuzzy_score": code_fuzzy,
        "composite_score": composite,
    }
