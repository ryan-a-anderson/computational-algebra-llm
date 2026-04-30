"""Scoring logic for Macaulay2 LLM evaluation."""

import re
from difflib import SequenceMatcher


def normalize(text: str) -> str:
    """Strip think tags, fences, whitespace; lowercase — for comparison."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"```[^\n]*\n?", "", text)
    text = re.sub(r"```", "", text)
    return text.strip().lower()


def compute_scores(model_response: str, correct_answer: str, correct_output: str) -> dict:
    norm_resp = normalize(model_response)
    norm_ans = normalize(correct_answer)

    exact = norm_resp == norm_ans
    output_match = (
        bool(correct_output)
        and correct_output.strip().lower() in model_response.lower()
    )
    fuzzy = round(SequenceMatcher(None, norm_resp, norm_ans).ratio(), 4)

    if exact:
        composite = 1.0
    elif output_match:
        composite = 0.7
    else:
        composite = round(fuzzy * 0.5, 4)

    return {
        "exact_match": exact,
        "output_match": output_match,
        "fuzzy_score": fuzzy,
        "composite_score": composite,
    }
