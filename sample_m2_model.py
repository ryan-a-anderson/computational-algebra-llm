#!/usr/bin/env python3
"""
Sample from the fine-tuned m2-qwen3-4b-sft checkpoint on Tinker.
Usage: python3 sample_m2_model.py
"""

import asyncio
import os
import tinker
from tinker_cookbook.renderers import get_renderer

API_KEY = os.environ.get("TINKER_API_KEY", "tml-gnnuOReXJScfM3VqO62Rt9yVagpGPQQneb2ZQ9iYhw310e4QB4HUMf0ReHMrxlQTQAAAA")
MODEL_PATH = "tinker://23cdb1b1-10ca-5496-8afa-323e43af7aa6:train:0/sampler_weights/ephemeral_61"
BASE_MODEL = "Qwen/Qwen3.5-4B"

SYSTEM_PROMPT = (
    "You are an expert Macaulay2 programmer specializing in computational algebra. "
    "When given Macaulay2 code, execute it mentally and produce the exact output "
    "that Macaulay2 would return, including all intermediate results and type annotations."
)

TEST_EXAMPLES = [
    # From training data — should get near-perfect output
    "R = QQ[x,y]; I = ideal(x^2 - y, y^2 - 1); degree I",
    # Novel example — tests generalization
    "R = QQ[x,y,z]; I = ideal(x^2 + y^2 + z^2 - 1, x + y + z); dim I",
    # Another novel one
    "R = QQ[a,b,c]; M = matrix{{a,b},{b,c}}; det M",
]


async def main():
    print("Connecting to Tinker fine-tuned checkpoint...")
    sc = tinker.ServiceClient(api_key=API_KEY)

    sampling_client = await sc.create_sampling_client_async(model_path=MODEL_PATH)
    tokenizer = sampling_client.get_tokenizer()
    renderer = get_renderer("qwen3_5_disable_thinking", tokenizer)
    stop_sequences = renderer.get_stop_sequences()
    params = tinker.SamplingParams(max_tokens=400, temperature=0.1, stop=stop_sequences)

    print(f"Connected. Model path: {MODEL_PATH}\n")
    print("=" * 70)

    for i, code in enumerate(TEST_EXAMPLES, 1):
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"What is the output of the following Macaulay2 code?\n\n```macaulay2\n{code}\n```"},
        ]
        prompt_str = renderer.build_generation_prompt(messages)

        print(f"[Example {i}]")
        print(f"Input:\n  {code}")
        print("Output:")

        result = await sampling_client.sample_async(
            prompt=prompt_str,
            num_samples=1,
            sampling_params=params,
        )
        parsed = renderer.parse_response(result.sequences[0].tokens)
        # parse_response returns (message_dict, bool) or just a string depending on version
        if isinstance(parsed, tuple):
            response = parsed[0].get("content", str(parsed[0]))
        else:
            response = parsed
        print(response)
        print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
