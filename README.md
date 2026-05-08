# Macaulay2 LLM Eval

A pipeline for evaluating and comparing multiple LLMs on [Macaulay2](https://macaulay2.com/) programming tasks. Models are prompted to produce correct Macaulay2 code, optionally executed through the M2 interpreter, and scored on output correctness or code similarity.

## Project structure

```text
computational-algebra-llm/
├── eval-pipeline/
│   ├── eval.py          # main entry point — evaluation loop, summary, leaderboard
│   ├── providers.py     # API callers and default model lists for each provider
│   ├── scoring.py       # scoring logic (execution match, fuzzy similarity)
│   └── executor.py      # runs model output through the M2 interpreter
├── macaulay2_benchmark.json   # benchmark questions
├── requirements.txt           # dependencies
├── results/                   # output directory (created on first run)
└── .env                       # API keys (not committed)
```

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API keys

Copy the example env file and fill in your keys:

```bash
cp .env.example .env
```

Edit `.env`:

```text
ANTHROPIC_API_KEY=...     # https://console.anthropic.com/
OPENAI_API_KEY=...        # https://platform.openai.com/
HUGGINGFACE_API_KEY=...   # https://huggingface.co/settings/tokens
DEEPSEEK_API_KEY=...      # https://platform.deepseek.com/
KIMI_API_KEY=...          # https://platform.moonshot.cn/
TINKER_API_KEY=...        # Thinking Machines Tinker
```

You only need keys for the providers you intend to run.

## Macaulay2 installation

Execution mode (`--execute`) requires the `M2` binary on your `PATH`.

### macOS

```bash
brew install macaulay2
```

### Linux (Debian/Ubuntu)

```bash
sudo apt install macaulay2
```

### Verify M2 works

```bash
echo '1+1' | M2 --no-readline --silent --stop
```

Expected output: `o1 = 2`

## Running the eval

All commands are run from the project root with the venv active. The main script is `eval-pipeline/eval.py`.

### Flags

| Flag | Default | Description |
| --- | --- | --- |
| `--benchmark PATH` | _(required)_ | Path to benchmark JSON |
| `--providers PROVIDER...` | `all` | One or more providers, or `all` |
| `--models MODEL...` | provider defaults | Override model list (applies to every selected provider) |
| `--output-dir DIR` | `results/` | Directory for per-model JSON files and `summary.json` |
| `--execute` | off | Run model code through M2 and score on runtime output |
| `--m2-smoke-check` | off | Verify M2 can execute `1+1` before running |
| `--num-samples N` | `1` | Number of samples per question/model; sweep runner defaults to `30` |
| `--temperature T` | `0.0` | Generation temperature; use nonzero values for pass@k |
| `--metrics METRIC...` | `accuracy` | Aggregate metrics to compute: `accuracy`, `pass_at_k` |
| `--pass-k K...` | `1` | k values for `pass_at_k` |
| `--workers N` | `1` | Parallel sample evaluation workers per model |
| `--oracle-grader` | off | Use a binary LLM oracle on execution-output mismatches |
| `--grader-provider PROVIDER` | `openai` | Provider for the oracle grader |
| `--grader-model MODEL` | `gpt-5-2` | Model for the oracle grader |
| `--grader-criteria CRITERIA` | `default` | Oracle criteria: `default`, `strict` |
| `--delay SECONDS` | `0.5` | Sleep between task submissions to avoid rate limits |

Available providers: `anthropic`, `openai`, `mistral`, `deepseek`, `kimi`, `tinker`

### Examples

#### Single provider with default models

```bash
python eval-pipeline/eval.py \
  --benchmark macaulay2_benchmark.json \
  --providers anthropic
```

#### Multiple providers

```bash
python eval-pipeline/eval.py \
  --benchmark macaulay2_benchmark.json \
  --providers anthropic openai deepseek
```

#### All providers

```bash
python eval-pipeline/eval.py \
  --benchmark macaulay2_benchmark.json \
  --providers all
```

#### Specific models

```bash
python eval-pipeline/eval.py \
  --benchmark macaulay2_benchmark.json \
  --providers anthropic \
  --models claude-opus-4-7 claude-sonnet-4-6
```

#### Execution mode with custom output directory

```bash
python eval-pipeline/eval.py \
  --benchmark macaulay2_benchmark.json \
  --providers anthropic openai \
  --execute \
  --output-dir results/run1 \
  --delay 1.0
```

#### pass@k with binary oracle grading

```bash
python eval-pipeline/eval.py \
  --benchmark benchmarks/unified_benchmark.json \
  --providers tinker \
  --models Qwen/Qwen3-32B \
  --execute \
  --num-samples 30 \
  --temperature 0.7 \
  --metrics pass_at_k accuracy \
  --pass-k 1 5 10 \
  --workers 4 \
  --oracle-grader \
  --grader-provider openai \
  --grader-model gpt-5-2 \
  --grader-cache-dir results/oracle_cache
```

#### Tinker model sweep

For a full pass@k sweep over one or more Tinker models, use the convenience runner:

```bash
python eval-pipeline/run_benchmark_sweep.py \
  --benchmark benchmarks/unified_benchmark.json \
  --models Qwen/Qwen3-8B Qwen/Qwen3-32B meta-llama/Llama-3.3-70B-Instruct \
  --num-samples 30 \
  --temperature 0.7 \
  --pass-k 1 5 10 \
  --workers 4
```

Use `--delay` to pace task submission if the provider rate limits concurrent requests.

Each run writes to `results/runs/<timestamp>/` with:

- `run_config.json`: arguments and run metadata
- `summary.json`: model-level and per-question metrics
- `<provider>_<model>_results.json`: full per-sample records for each model
- `samples.csv`: flat audit table with prompts, raw model outputs, preflight status, raw/cleaned compiled outputs, reference compiled outputs, correctness, and token usage
- `pass_at_k.csv`: per-question and aggregate pass@k table

Execution scoring compiles each reference answer once and compares cleaned model output against the cleaned reference output. Obvious non-code responses, markdown, and thinking traces are rejected before M2 execution and count as incorrect samples.

Results are written to `<output-dir>/<provider>_<model>_results.json` and a `summary.json` with leaderboard data is printed at the end.

## Scoring

### Execution mode (`--execute`)

Each model response is executed through the M2 interpreter and the actual output is compared against the expected output.

- **Non-debugging categories**: composite score = 1.0 if output matches exactly, 0.0 otherwise (`execution_match`).
- **Debugging category**: composite score = fuzzy similarity between model code and the reference answer (`code_fuzzy_score`), regardless of execution result.

### Static mode (no `--execute`)

Model code is compared directly against the reference answer without running it:

- **Exact match** (normalized): composite = 1.0
- **Output mention** (expected output string appears in model response): composite = 0.7
- **Fuzzy similarity** (SequenceMatcher ratio): composite = fuzzy × 0.5

Output normalization strips markdown fences, `<think>` tags, and normalizes whitespace before comparison.
