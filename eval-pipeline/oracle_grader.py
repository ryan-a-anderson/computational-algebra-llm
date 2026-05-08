"""Binary LLM oracle grader for output equivalence."""

import hashlib
import json
import os
import re
from pathlib import Path
from uuid import uuid4

from providers import CALLERS

ORACLE_SYSTEM_PROMPT = """You are a strict grader for Macaulay2 benchmark outputs.

Decide whether the actual compiled output is correct relative to the target compiled output.
Return only valid JSON:
{"correct": boolean, "reason": string}

Rules:
- Mark correct only when the actual output has the same mathematical/computational meaning as the target.
- Do not ignore changes to string contents, internal newlines in strings, signs, exponents, coefficients, variable names, matrix shape, list order, object type, or boolean value.
- Ignore only harmless Macaulay2 prompt labels, output labels, type annotations, outer whitespace, and line wrapping.
- Error messages are incorrect unless the target output is also the same error.
- Empty output is incorrect unless the target is also empty.
"""

CRITERIA: dict[str, str] = {
    "default": (
        "Apply the strict grading rules from the system prompt."
    ),
    "strict": (
        "Apply the strict grading rules from the system prompt. Be especially conservative."
    ),
}


class OracleParseError(ValueError):
    def __init__(self, message: str, raw_response: str):
        super().__init__(message)
        self.raw_response = raw_response


def _cache_key(
    provider: str,
    model: str,
    criteria: str,
    expected_output: str,
    actual_output: str,
) -> str:
    payload = json.dumps(
        {
            "provider": provider,
            "model": model,
            "criteria": criteria,
            "expected_output": expected_output,
            "actual_output": actual_output,
        },
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _extract_json(text: str) -> dict:
    text = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL | re.IGNORECASE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        return json.loads(text[start : end + 1])


def grade_output(
    expected_output: str,
    actual_output: str,
    provider: str,
    model: str,
    criteria: str = "default",
    cache_dir: str | None = None,
) -> dict:
    """Return a binary oracle judgment for output equivalence."""
    if provider not in CALLERS:
        raise ValueError(f"Unknown grader provider '{provider}'")
    if criteria not in CRITERIA:
        raise ValueError(f"Unknown oracle criteria '{criteria}'")

    cache_path: Path | None = None
    if cache_dir:
        cache_root = Path(cache_dir)
        cache_root.mkdir(parents=True, exist_ok=True)
        cache_path = cache_root / f"{_cache_key(provider, model, criteria, expected_output, actual_output)}.json"
        if cache_path.exists():
            return json.loads(cache_path.read_text())

    prompt = (
        f"Criteria:\n{CRITERIA[criteria]}\n\n"
        "Target compiled output:\n"
        "<target_output>\n"
        f"{expected_output}\n"
        "</target_output>\n\n"
        "Actual compiled output:\n"
        "<actual_output>\n"
        f"{actual_output}\n"
        "</actual_output>\n"
    )

    raw_response, usage = CALLERS[provider](model, prompt, system_prompt=ORACLE_SYSTEM_PROMPT)
    try:
        parsed = _extract_json(raw_response)
    except Exception as exc:
        raise OracleParseError(str(exc), raw_response) from exc
    result = {
        "correct": bool(parsed["correct"]),
        "reason": str(parsed.get("reason", "")),
        "raw_response": raw_response,
        "provider": provider,
        "model": model,
        "criteria": criteria,
        "usage": usage,
    }
    if cache_path:
        tmp_path = cache_path.with_suffix(f".{os.getpid()}.{uuid4().hex}.tmp")
        tmp_path.write_text(json.dumps(result, indent=2))
        tmp_path.replace(cache_path)
    return result
