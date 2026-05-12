# =============================================================================
# Macaulay2 Dataset Augmentation Script
# Uses Claude to generate variants of existing M2 examples
# Input:  your existing JSON/JSONL dataset
# Output: augmented_dataset.jsonl (originals + generated variants)
# =============================================================================

import anthropic
import json
import time
import random
from pathlib import Path

# =============================================================================
# CONFIG
# =============================================================================

CONFIG = {
    "input_path":        "m2_dataset.json",       # your existing dataset
    "output_path":       "m2_augmented.jsonl",     # where to save results
    "failed_path":       "m2_augment_failed.jsonl",# examples that failed/were invalid
    "variants_per_example": 5,                     # how many variants per example
    "model":             "claude-sonnet-4-6",
    "max_tokens":        2048,
    "sleep_between_calls": 1.0,                    # seconds, to avoid rate limits
    "max_retries":       2,                        # retries per example on failure
}

# =============================================================================
# SYSTEM PROMPT
# =============================================================================

SYSTEM_PROMPT = """You are an expert in the Macaulay2 computer algebra system and 
computational algebraic geometry. Your task is to generate dataset variants for 
fine-tuning a language model on Macaulay2 programming.

Rules for generating variants:
1. Each variant must ask about the same core concept in a different way, OR make the 
   problem slightly harder (e.g. add a variable, change the coefficient ring, add a constraint)
2. Every answer must be correct, runnable Macaulay2 code or a valid M2 response
3. Do not hallucinate Macaulay2 functions — only use real M2 syntax and built-ins
4. Vary the phrasing naturally — some formal, some casual, some terse
5. Keep difficulty roughly similar to the original unless making a "harder" variant

Output format:
Return ONLY a JSON array. No explanation, no markdown fences, no preamble.
Each object must have exactly these keys:
  - "category": string (same as input or slightly adjusted)
  - "difficulty": null or one of "easy", "medium", "hard"
  - "description": string (one sentence describing what this tests)
  - "prompt": string (the question, starting with "# Macaulay2 programming language question\\n\\n")
  - "correct_answer": array of strings (each string is one valid answer)
  - "correct_output": string or null (expected M2 output if known, else null)
"""

# =============================================================================
# MUTATION PROMPT TEMPLATE
# =============================================================================

def build_user_prompt(example: dict, n_variants: int) -> str:
    # Remove internal fields the LLM doesn't need
    clean = {k: v for k, v in example.items()
             if k in ("category", "difficulty", "description", "prompt",
                      "correct_answer", "correct_output")}
    return (
        f"Generate {n_variants} variants of this Macaulay2 dataset example.\n\n"
        f"Original example:\n{json.dumps(clean, indent=2)}"
    )

# =============================================================================
# VALIDATION
# =============================================================================

REQUIRED_KEYS = {"category", "description", "prompt", "correct_answer"}

def validate_variant(variant: dict, idx: int) -> tuple[bool, str]:
    """Check that a generated variant has the required structure."""
    if not isinstance(variant, dict):
        return False, f"variant {idx} is not a dict"

    missing = REQUIRED_KEYS - variant.keys()
    if missing:
        return False, f"variant {idx} missing keys: {missing}"

    if not isinstance(variant.get("correct_answer"), list):
        return False, f"variant {idx}: correct_answer must be a list"

    if not variant.get("correct_answer"):
        return False, f"variant {idx}: correct_answer is empty"

    if not isinstance(variant.get("prompt"), str) or not variant["prompt"].strip():
        return False, f"variant {idx}: prompt is empty or not a string"

    return True, "ok"


def parse_llm_response(text: str) -> tuple[list[dict] | None, str]:
    """
    Parse the LLM's response into a list of variant dicts.
    Handles minor formatting issues (stray markdown fences, etc.)
    """
    text = text.strip()

    # Strip markdown fences if present
    if text.startswith("```"):
        lines = text.splitlines()
        text = "\n".join(
            line for line in lines
            if not line.strip().startswith("```")
        ).strip()

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        return None, f"JSON parse error: {e}"

    if not isinstance(data, list):
        return None, f"Expected a JSON array, got {type(data).__name__}"

    return data, "ok"

# =============================================================================
# AUGMENTATION LOOP
# =============================================================================

def augment_dataset(config: dict) -> None:
    client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var

    # ── Load input data ──────────────────────────────────────────────────────
    input_path = Path(config["input_path"])
    with open(input_path, "r") as f:
        content = f.read().strip()

    if content.startswith("["):
        originals = json.loads(content)
    else:
        originals = [json.loads(line) for line in content.splitlines() if line.strip()]

    print(f"Loaded {len(originals)} original examples from {input_path}")
    print(f"Generating {config['variants_per_example']} variants each → "
          f"up to {len(originals) * config['variants_per_example']} new examples\n")

    # ── Output files ─────────────────────────────────────────────────────────
    out_path    = Path(config["output_path"])
    failed_path = Path(config["failed_path"])

    # Write originals first (with source tag)
    with open(out_path, "w") as f:
        for i, ex in enumerate(originals):
            ex["id"]     = ex.get("id", f"original_{i:04d}")
            ex["source"] = "original"
            f.write(json.dumps(ex) + "\n")

    print(f"Wrote {len(originals)} originals to {out_path}\n")

    # ── Per-example augmentation ──────────────────────────────────────────────
    total_generated = 0
    total_failed    = 0

    for i, example in enumerate(originals):
        ex_id = example.get("id", f"example_{i}")
        print(f"[{i+1}/{len(originals)}] Augmenting: {ex_id} ({example.get('category', 'unknown')})")

        user_prompt = build_user_prompt(example, config["variants_per_example"])
        variants    = None
        last_error  = ""

        # Retry loop
        for attempt in range(config["max_retries"] + 1):
            try:
                response = client.messages.create(
                    model=config["model"],
                    max_tokens=config["max_tokens"],
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": user_prompt}],
                )
                raw_text = response.content[0].text
                variants, last_error = parse_llm_response(raw_text)

                if variants is not None:
                    break  # success
                else:
                    print(f"  ⚠ Parse failed (attempt {attempt+1}): {last_error}")

            except anthropic.RateLimitError:
                wait = 30 * (attempt + 1)
                print(f"  ⚠ Rate limit hit — waiting {wait}s...")
                time.sleep(wait)
            except anthropic.APIError as e:
                print(f"  ⚠ API error (attempt {attempt+1}): {e}")
                last_error = str(e)
                time.sleep(5)

        if variants is None:
            print(f"  ✗ Failed after {config['max_retries']+1} attempts: {last_error}")
            with open(failed_path, "a") as ff:
                ff.write(json.dumps({"id": ex_id, "error": last_error}) + "\n")
            total_failed += 1
            continue

        # ── Validate & save each variant ──────────────────────────────────────
        saved_count = 0
        for j, variant in enumerate(variants):
            ok, reason = validate_variant(variant, j)
            if not ok:
                print(f"  ⚠ Variant {j} invalid: {reason}")
                with open(failed_path, "a") as ff:
                    ff.write(json.dumps({"id": ex_id, "variant": j,
                                         "error": reason, "data": variant}) + "\n")
                continue

            variant["id"]            = f"{ex_id}_aug_{j:02d}"
            variant["source"]        = "augmented"
            variant["source_original_id"] = ex_id

            with open(out_path, "a") as f:
                f.write(json.dumps(variant) + "\n")

            saved_count += 1

        print(f"  ✓ Saved {saved_count}/{len(variants)} variants")
        total_generated += saved_count

        time.sleep(config["sleep_between_calls"])

    # ── Summary ───────────────────────────────────────────────────────────────
    total = len(originals) + total_generated
    print(f"\n{'='*60}")
    print(f"Done.")
    print(f"  Originals       : {len(originals)}")
    print(f"  Generated       : {total_generated}")
    print(f"  Failed examples : {total_failed}")
    print(f"  Total in dataset: {total}")
    print(f"  Output file     : {out_path}")
    if total_failed:
        print(f"  Failed log      : {failed_path}")
    print(f"{'='*60}")


# =============================================================================
# INSPECT OUTPUT (helper, run separately)
# =============================================================================

def inspect_output(path: str = CONFIG["output_path"], n: int = 3) -> None:
    """Print a random sample of generated examples for manual review."""
    examples = []
    with open(path, "r") as f:
        for line in f:
            ex = json.loads(line)
            if ex.get("source") == "augmented":
                examples.append(ex)

    sample = random.sample(examples, min(n, len(examples)))
    print(f"\n── Sample of {len(sample)} augmented examples ──────────────────\n")
    for ex in sample:
        print(f"ID       : {ex['id']}")
        print(f"Category : {ex.get('category')}")
        print(f"Prompt   : {ex['prompt'][:120]}...")
        print(f"Answer   : {ex['correct_answer']}")
        print()


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    import os

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise EnvironmentError(
            "ANTHROPIC_API_KEY not set. "
            "Export it before running:\n"
            "  export ANTHROPIC_API_KEY=sk-ant-..."
        )

    augment_dataset(CONFIG)

    # Uncomment to review a sample of generated examples after running:
    # inspect_output()