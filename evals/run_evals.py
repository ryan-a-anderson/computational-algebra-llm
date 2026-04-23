"""
Macaulay2 Benchmark Evaluation Script
Evaluates open-source LLMs on computational algebra questions via Tinker API.
Uses the OpenAI-compatible endpoint at Tinker.
"""

import json
import os
import re
import time
import argparse
from datetime import datetime
from openai import OpenAI

# Tinker API configuration
BASE_URL = "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1"

AVAILABLE_MODELS = [
    "Qwen/Qwen3-8B",
    "Qwen/Qwen3-32B",
    "meta-llama/Llama-3.1-8B-Instruct",
    "meta-llama/Llama-3.3-70B-Instruct",
]

SYSTEM_PROMPT = """You are an expert in computational algebra and the Macaulay2 programming language.
When asked a question about Macaulay2, provide the correct Macaulay2 code to solve the problem.
Return ONLY the Macaulay2 code needed to solve the problem, with no explanation or commentary.
Each line of code should be on its own line. Do not wrap the code in markdown code blocks."""


def create_client(api_key: str) -> OpenAI:
    return OpenAI(base_url=BASE_URL, api_key=api_key)


def evaluate_question(client: OpenAI, model: str, question: dict, max_tokens: int = 1024) -> dict:
    """Send a single benchmark question to a model and return the result."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question["prompt"]},
            ],
            max_tokens=max_tokens,
            temperature=0.0,
        )
        model_output = response.choices[0].message.content
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        }
    except Exception as e:
        model_output = f"ERROR: {e}"
        usage = {}

    # Strip <think>...</think> blocks (e.g. Qwen3 reasoning tokens)
    raw_output = model_output
    if model_output and not model_output.startswith("ERROR"):
        model_output = re.sub(r"<think>.*?</think>\s*", "", model_output, flags=re.DOTALL).strip()
        # Handle case where </think> is missing (truncated thinking)
        if model_output.startswith("<think>"):
            model_output = re.sub(r"<think>.*", "", model_output, flags=re.DOTALL).strip()

    return {
        "question_id": question["id"],
        "category": question["category"],
        "difficulty": question.get("difficulty"),
        "prompt": question["prompt"],
        "correct_answer": question["correct_answer"],
        "correct_output": question["correct_output"],
        "model_response": model_output,
        "raw_response": raw_output if raw_output != model_output else None,
        "usage": usage,
    }


def run_eval(client: OpenAI, model: str, questions: list, delay: float = 1.0) -> list:
    """Run evaluation for a single model across all questions."""
    results = []
    for i, q in enumerate(questions):
        print(f"  [{i+1}/{len(questions)}] {q['id']}: {q['category']}", flush=True)
        result = evaluate_question(client, model, q)
        results.append(result)
        if i < len(questions) - 1:
            time.sleep(delay)
    return results


def main():
    parser = argparse.ArgumentParser(description="Run Macaulay2 benchmark evals on Tinker")
    parser.add_argument("--api-key", default=os.environ.get("TINKER_API_KEY"),
                        help="Tinker API key (or set TINKER_API_KEY env var)")
    parser.add_argument("--models", nargs="+", default=AVAILABLE_MODELS,
                        help="Models to evaluate")
    parser.add_argument("--benchmark", default="../benchmarks/unified_benchmark.json",
                        help="Path to unified benchmark JSON")
    parser.add_argument("--output-dir", default="../evals/results",
                        help="Directory for result files")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Delay between API calls in seconds")
    args = parser.parse_args()

    if not args.api_key:
        print("Error: provide --api-key or set TINKER_API_KEY")
        return

    with open(args.benchmark) as f:
        questions = json.load(f)
    print(f"Loaded {len(questions)} benchmark questions")

    os.makedirs(args.output_dir, exist_ok=True)
    client = create_client(args.api_key)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    all_results = {}
    for model in args.models:
        model_short = model.replace("/", "_")
        print(f"\n{'='*60}")
        print(f"Evaluating: {model}")
        print(f"{'='*60}")

        results = run_eval(client, model, questions, delay=args.delay)
        all_results[model] = results

        # Save per-model results
        outfile = os.path.join(args.output_dir, f"{model_short}_{timestamp}.json")
        with open(outfile, "w") as f:
            json.dump({
                "model": model,
                "timestamp": timestamp,
                "num_questions": len(questions),
                "results": results,
            }, f, indent=2)
        print(f"  Saved to {outfile}")

    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for model, results in all_results.items():
        errors = sum(1 for r in results if r["model_response"].startswith("ERROR"))
        print(f"\n{model}:")
        print(f"  Questions answered: {len(results) - errors}/{len(results)}")
        if results[0].get("usage"):
            total_tokens = sum(r["usage"].get("total_tokens", 0) for r in results if r.get("usage"))
            print(f"  Total tokens used: {total_tokens}")

    # Save combined summary
    summary_file = os.path.join(args.output_dir, f"eval_summary_{timestamp}.json")
    with open(summary_file, "w") as f:
        json.dump({
            "timestamp": timestamp,
            "models": list(all_results.keys()),
            "num_questions": len(questions),
            "all_results": all_results,
        }, f, indent=2)
    print(f"\nCombined results saved to {summary_file}")


if __name__ == "__main__":
    main()
