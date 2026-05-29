# Running Eval on a Fine-Tuned Tinker Model

Use the eval pipeline with any Tinker model path. For a fine-tuned model, this is usually the sampler weights path printed by `sample_m2_model.py`.

## 1. Get the Tinker Model Path

Run:

```bash
python sample_m2_model.py
```

Copy the printed model path. It should look like:

```text
tinker://.../sampler_weights/...
```

## 2. Preflight the Model

Run a quick preflight before launching a full benchmark:

```bash
python eval-pipeline/run_benchmark_sweep.py \
  --benchmark benchmarks/unified_benchmark.json \
  --models "tinker://.../sampler_weights/..." \
  --temperature 0.5 \
  --oracle-grader \
  --grader-provider tinker \
  --grader-model Qwen/Qwen3-32B \
  --preflight-only
```

## 3. Run the Full Eval

```bash
python eval-pipeline/run_benchmark_sweep.py \
  --benchmark benchmarks/unified_benchmark.json \
  --models "tinker://.../sampler_weights/..." \
  --num-samples 50 \
  --temperature 0.5 \
  --pass-k 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 \
  --workers 6 \
  --samples-per-request 5 \
  --delay 0 \
  --oracle-grader \
  --grader-provider tinker \
  --grader-model Qwen/Qwen3-32B \
  --run-name tinker_finetuned_<name>_t05_k1_20
```

## Notes

- Replace `tinker://.../sampler_weights/...` with the actual Tinker model path.
- Keep the model path in quotes because it contains `:` and `/`.
- `--temperature 0.5` means the run samples at temperature 0.5.
- `--num-samples 50` gives 50 samples per benchmark problem.
- `--pass-k 1 ... 20` computes pass@k for all k from 1 through 20 using the same 50 samples.
- `--samples-per-request 5` asks Tinker for up to 5 same-prompt completions per request when supported.
