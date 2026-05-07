"""Aggregate metrics for benchmark results."""

import itertools
from collections import defaultdict
from math import prod


def estimate_pass_at_k(num_samples: int | list[int], num_correct: list[int], k: int) -> list[float]:
    """Estimate pass@k for each problem."""

    def estimator(n: int, c: int, k_value: int) -> float:
        if n <= 0:
            return 0.0
        if k_value > n:
            k_value = n
        if n - c < k_value:
            return 1.0
        return 1.0 - prod(1.0 - k_value / i for i in range(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return [estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)]


def _samples_by_question(results: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for result in results:
        grouped[result["question_id"]].append(result)
    return dict(grouped)


def compute_accuracy(results: list[dict]) -> dict:
    """Compute sample-level accuracy."""
    if not results:
        return {"accuracy": 0.0, "num_samples": 0, "num_correct": 0}

    num_correct = sum(1 for result in results if result.get("correct") is True)
    return {
        "accuracy": round(num_correct / len(results), 4),
        "num_samples": len(results),
        "num_correct": num_correct,
    }


def compute_pass_at_k(results: list[dict], k_values: list[int]) -> dict:
    """Compute mean pass@k over questions."""
    grouped = _samples_by_question(results)
    if not grouped:
        return {f"pass@{k}": 0.0 for k in k_values}

    counts = [
        (len(samples), sum(1 for sample in samples if sample.get("correct") is True))
        for samples in grouped.values()
    ]
    num_samples = [n for n, _ in counts]
    num_correct = [c for _, c in counts]

    metrics: dict[str, float] = {}
    for k in k_values:
        estimates = estimate_pass_at_k(num_samples, num_correct, k)
        metrics[f"pass@{k}"] = round(sum(estimates) / len(estimates), 4)
    return metrics


def compute_metrics(results: list[dict], metric_names: list[str], pass_k: list[int]) -> dict:
    """Compute selected aggregate metrics from saved per-sample results."""
    metrics: dict = {}
    for name in metric_names:
        if name == "accuracy":
            metrics.update(compute_accuracy(results))
        elif name == "pass_at_k":
            metrics.update(compute_pass_at_k(results, pass_k))
        else:
            raise ValueError(f"Unknown metric '{name}'")
    return metrics
