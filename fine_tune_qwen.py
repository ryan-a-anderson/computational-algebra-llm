#!/usr/bin/env python3
"""
Fine-tune Qwen3 4B on Macaulay2 code-generation examples using the Tinker platform.

The model is trained to take a natural-language algebra question and return
correct Macaulay2 code — not to predict M2 output.

Usage:
    python fine_tune_qwen.py [--steps N] [--lr LR] [--rank R]

Generate training data first:
    python macaulay2-examples/generate_training_data.py
    python macaulay2-examples/validate_training_data.py --skip-benchmark
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

import numpy as np
import tinker
from tinker_cookbook.renderers import TrainOnWhat, get_renderer
from tinker_cookbook.supervised.data import conversation_to_datum

# Prefer the validated dataset; fall back to the unvalidated version
_BASE = Path(__file__).parent / "macaulay2-examples"
DATA_PATHS = [
    _BASE / "m2_code_gen_training_validated.json",
    _BASE / "m2_code_gen_training.json",
]
CHECKPOINT_NAME = "m2-qwen3-4b-codegen-v1"

TINKER_API_KEY = os.environ.get("TINKER_API_KEY", "tml-gnnuOReXJScfM3VqO62Rt9yVagpGPQQneb2ZQ9iYhw310e4QB4HUMf0ReHMrxlQTQAAAA")


def parse_args():
    p = argparse.ArgumentParser(description="Fine-tune Qwen3 4B on M2 examples via Tinker")
    p.add_argument("--steps", type=int, default=50, help="Training steps (default: 50)")
    p.add_argument("--lr", type=float, default=1e-4, help="Learning rate (default: 1e-4)")
    p.add_argument("--rank", type=int, default=16, help="LoRA rank (default: 16)")
    p.add_argument("--max-length", type=int, default=512, help="Max token length per example (default: 512)")
    p.add_argument("--dry-run", action="store_true", help="Print data summary and exit without training")
    return p.parse_args()


def load_training_data() -> list[list[dict]]:
    conversations = []
    for path in DATA_PATHS:
        if not path.exists():
            print(f"WARN: {path.name} not found, skipping", file=sys.stderr)
            continue
        with open(path) as f:
            records = json.load(f)
        convs = [r["messages"] for r in records]
        print(f"  {path.name}: {len(convs)} examples")
        conversations.extend(convs)
    if not conversations:
        print("ERROR: no training data found. Run the data-generation scripts first.", file=sys.stderr)
        sys.exit(1)
    print(f"Total: {len(conversations)} training examples")
    return conversations


async def get_base_model(service_client: tinker.ServiceClient) -> str:
    """Return the best available Qwen3 4B model name."""
    try:
        caps = await service_client.get_server_capabilities_async()
        available = getattr(caps, "models", []) or []
        print(f"Available models: {available}")
        for candidate in ["Qwen/Qwen3-4B", "Qwen/Qwen3.5-4B", "Qwen/Qwen3-4B-Instruct"]:
            if candidate in available:
                return candidate
        # Fall back to first Qwen model found
        qwen = [m for m in available if "Qwen" in m and "4B" in m]
        if qwen:
            return qwen[0]
        return "Qwen/Qwen3.5-4B"
    except Exception as e:
        print(f"Could not query server capabilities ({e}), defaulting to Qwen/Qwen3.5-4B")
        return "Qwen/Qwen3.5-4B"


def get_renderer_for_model(model_name: str, tokenizer):
    """Pick the right renderer for the model family."""
    name_lower = model_name.lower()
    if "qwen3.5" in name_lower or "qwen3-5" in name_lower:
        renderer_key = "qwen3_5_disable_thinking"
    elif "qwen3" in name_lower:
        renderer_key = "qwen3_5_disable_thinking"
    else:
        renderer_key = "qwen3_5_disable_thinking"
    print(f"Using renderer: {renderer_key}")
    return get_renderer(renderer_key, tokenizer)


async def main_async(args):
    os.environ.setdefault("TINKER_API_KEY", TINKER_API_KEY)

    conversations = load_training_data()

    if args.dry_run:
        print(f"\n-- Dry run --")
        print(f"Steps: {args.steps}, LR: {args.lr}, LoRA rank: {args.rank}")
        print(f"Max sequence length: {args.max_length}")
        print("\nFirst example:")
        for msg in conversations[0]:
            print(f"  [{msg['role']}]: {msg['content'][:120]}...")
        return

    print("\nConnecting to Tinker...")
    service_client = tinker.ServiceClient(api_key=TINKER_API_KEY)

    base_model = await get_base_model(service_client)
    print(f"Base model: {base_model}")

    print(f"Creating LoRA training client (rank={args.rank})...")
    training_client = await service_client.create_lora_training_client_async(
        base_model=base_model,
        rank=args.rank,
    )
    tokenizer = training_client.get_tokenizer()
    renderer = get_renderer_for_model(base_model, tokenizer)

    print("Tokenizing training data...")
    training_data = [
        conversation_to_datum(
            conv,
            renderer,
            max_length=args.max_length,
            train_on_what=TrainOnWhat.LAST_ASSISTANT_MESSAGE,
        )
        for conv in conversations
    ]
    # Filter out any examples that produced empty training signal
    training_data = [d for d in training_data if d is not None]
    print(f"Tokenized {len(training_data)} examples")

    print(f"\nStarting training: {args.steps} steps, lr={args.lr}\n")
    losses = []
    for step in range(args.steps):
        fwdbwd_future = await training_client.forward_backward_async(training_data, "cross_entropy")
        optim_future = await training_client.optim_step_async(
            tinker.AdamParams(learning_rate=args.lr)
        )
        fwdbwd_result = await fwdbwd_future.result_async()
        await optim_future.result_async()

        logprobs = np.concatenate(
            [out["logprobs"].tolist() for out in fwdbwd_result.loss_fn_outputs]
        )
        weights = np.concatenate(
            [d.loss_fn_inputs["weights"].tolist() for d in training_data]
        )
        loss = -np.dot(logprobs, weights) / weights.sum()
        losses.append(loss)
        print(f"Step {step + 1:3d}/{args.steps}: loss = {loss:.4f}")

    print(f"\nFinal loss: {losses[-1]:.4f}")
    print(f"Saving checkpoint as '{CHECKPOINT_NAME}'...")

    # Save persistent training weights (shows up in user checkpoint list)
    save_future = await training_client.save_state_async(name=CHECKPOINT_NAME)
    save_result = await save_future.result_async()
    print(f"Training weights saved at: {save_result.path}")

    # Also save sampler weights for immediate inference
    sampler_future = await training_client.save_weights_for_sampler_async(
        name=f"{CHECKPOINT_NAME}-sampler"
    )
    sampler_result = await sampler_future.result_async()
    print(f"Sampler weights saved at:  {sampler_result.path}")

    sampling_client = await service_client.create_sampling_client_async(
        model_path=sampler_result.path
    )

    # Quick smoke test
    print("\nRunning smoke test...")
    stop_sequences = renderer.get_stop_sequences()
    params = tinker.SamplingParams(max_tokens=300, temperature=0.2, stop=stop_sequences)
    test_messages = conversations[0][:-1]  # drop the assistant turn
    prompt_str = renderer.build_generation_prompt(test_messages)
    sample_result = await sampling_client.sample_async(
        prompt=prompt_str,
        num_samples=1,
        sampling_params=params,
    )
    print("Model output:")
    parsed = renderer.parse_response(sample_result.sequences[0].tokens)
    response = parsed[0].get("content", str(parsed[0])) if isinstance(parsed, tuple) else parsed
    print(response)


def main():
    args = parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
