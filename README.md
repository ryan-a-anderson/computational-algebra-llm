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
| `--delay SECONDS` | `0.5` | Sleep between API calls to avoid rate limits |

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
