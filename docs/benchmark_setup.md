# Benchmark Setup Guide

This guide describes the local setup needed to run the Macaulay2 eval pipeline from WSL/Linux.

## 1. Use WSL/Linux

Open the repo in a WSL terminal. The project path usually looks like:

```bash
cd "/mnt/c/Users/CB/OneDrive/Documents/UCLA Math Research/computational-algebra-llm"
```

The eval pipeline expects Linux commands and a Linux Macaulay2 install.

## 2. Install Python 3.12 and Create a Venv

On Ubuntu/WSL:

```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3.12-dev
```

Create or recreate the project venv:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

Verify:

```bash
which python
python --version
```

Expected shape:

```text
.../computational-algebra-llm/.venv/bin/python
Python 3.12.x
```

## 3. Install Macaulay2

On Ubuntu/WSL:

```bash
sudo apt install -y macaulay2
```

Verify that `M2` is on the Linux path and can run:

```bash
which M2
echo '1+1' | M2 --no-readline --silent --stop
```

Expected output includes:

```text
o1 = 2
```

## 4. Configure API Keys

Create or edit `.env` in the repo root:

```text
TINKER_API_KEY=...
ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...
DEEPSEEK_API_KEY=...
KIMI_API_KEY=...
```

Only keys for providers you use are required. Tinker runs need `TINKER_API_KEY`.

## 5. Build the Reference Cache

Build a reference-output cache whenever `benchmarks/unified_benchmark.json` changes:

```bash
python eval-pipeline/build_reference_cache.py \
  --benchmark benchmarks/unified_benchmark.json \
  --workers 4
```

The default cache path is:

```text
results/reference_cache/unified_benchmark_<hash>.json
```

If the sweep reports a missing cache with a specific path, build that exact file:

```bash
python eval-pipeline/build_reference_cache.py \
  --benchmark benchmarks/unified_benchmark.json \
  --output results/reference_cache/unified_benchmark_<hash>.json \
  --workers 4
```

Do not start a full sweep if important benchmark questions show `reference_failed`; inspect and fix the benchmark reference first.

## 6. Preflight a Model

Preflight checks model availability before spending on a full run:

```bash
python eval-pipeline/run_benchmark_sweep.py \
  --benchmark benchmarks/unified_benchmark.json \
  --models Qwen/Qwen3-32B \
  --temperature 0.5 \
  --oracle-grader \
  --grader-provider tinker \
  --grader-model Qwen/Qwen3-32B \
  --preflight-only
```

## 7. Run a Full Sweep

Example Tinker run:

```bash
python eval-pipeline/run_benchmark_sweep.py \
  --benchmark benchmarks/unified_benchmark.json \
  --models Qwen/Qwen3-32B \
  --num-samples 50 \
  --temperature 0.5 \
  --pass-k 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 \
  --workers 6 \
  --samples-per-request 5 \
  --delay 0 \
  --oracle-grader \
  --grader-provider tinker \
  --grader-model Qwen/Qwen3-32B \
  --run-name tinker_qwen32b_t05_k1_20
```

Results are written to:

```text
results/runs/<run-name>/
```

Important files:

- `run_config.json`
- `<provider>_<model>_results.json`
- `summary.json`
- `samples.csv`
- `pass_at_k.csv`

## 8. Resume, Merge, and Finalize Runs

Reusing the same `--run-name` lets you add more models to one run folder. Existing model result files are skipped unless `--force-rerun` is passed.

If a run is interrupted, rebuild aggregate artifacts from completed result JSON files:

```bash
python eval-pipeline/finalize_run.py results/runs/<run-name>
```

The analysis notebook can combine separate runs by editing `RUN_NAMES` in:

```text
notebooks/analyze_pass_at_k.ipynb
```

## 9. Common Checks

Activate the venv:

```bash
source .venv/bin/activate
```

Check Python and M2:

```bash
which python
python --version
which M2
echo '1+1' | M2 --no-readline --silent --stop
```

Check Git state:

```bash
git status
```
