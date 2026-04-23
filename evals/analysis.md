# Macaulay2 Benchmark: Eval Analysis (Round 1)

**Date:** April 22, 2026
**Benchmark:** 25 questions from `unified_benchmark.json`
**Platform:** Tinker (OpenAI-compatible API)
**Evaluator:** Manual scoring by code review (no M2 execution)

---

## 1. Models Evaluated

| Model | Type | Parameters | Tokens Used | Avg Tokens/Q |
|-------|------|------------|-------------|--------------|
| Qwen/Qwen3-8B | Reasoning | 8B | 21,556 | 862 |
| Qwen/Qwen3-32B | Reasoning | 32B | 22,273 | 891 |
| meta-llama/Llama-3.1-8B-Instruct | Instruct | 8B | 5,004 | 200 |
| meta-llama/Llama-3.3-70B-Instruct | Instruct | 70B | 4,976 | 199 |

## 2. Overall Scores

Scoring rubric: **2** = correct or functionally equivalent M2 code, **1** = partially correct (right approach but wrong syntax or minor errors), **0** = wrong, hallucinated, or empty response.

| Model | Correct (2) | Partial (1) | Wrong (0) | Score | Pct |
|-------|-------------|-------------|-----------|-------|-----|
| **Qwen3-32B** | 8 (32%) | 5 (20%) | 12 (48%) | **21/50** | **42%** |
| Qwen3-8B | 6 (24%) | 7 (28%) | 12 (48%) | 19/50 | 38% |
| Llama-3.3-70B | 6 (24%) | 6 (24%) | 13 (52%) | 18/50 | 36% |
| Llama-3.1-8B | 2 (8%) | 6 (24%) | 17 (68%) | 10/50 | 20% |

**Key takeaway:** No model exceeds 42%. All four models struggle substantially with Macaulay2, which is unsurprising given M2's niche status and minimal representation in training corpora.

## 3. Failure Mode Analysis

### 3.1 Qwen3 Models: Token Budget Exhaustion

The Qwen3 models (both 8B and 32B) produce extended `<think>` reasoning chains before answering. With a 1024 max-token limit, **8-9 out of 25 questions received empty responses** because the model exhausted its token budget during reasoning without ever producing an answer.

- Qwen3-8B: 8 empty responses (32%)
- Qwen3-32B: 9 empty responses (36%)

This is an artifact of the eval setup, not necessarily a capability gap. Increasing `max_tokens` to 2048+ would likely recover many of these. However, it does highlight a practical concern: reasoning models are expensive for eval workloads (4x the token usage of instruct models for the same questions).

### 3.2 Llama Models: Confident Hallucination

Both Llama models always produce a response (0 empty) but frequently hallucinate M2 syntax:

**Llama-3.1-8B common errors:**
- Invents nonexistent functions: `freeModule()`, `seq()`, `cat` (string concat)
- Uses Python-like syntax: `QQ[x,y,z] mod 5`, `p.rawInternalRep()`
- Confuses M2 with other CAS systems (e.g., Sage, Mathematica patterns)

**Llama-3.3-70B common errors:**
- Overwrites built-in types: `ZZ = ZZ/101` (destroys the integer ring)
- Invents functions: `qr()`, `expand`, `decompose` (instead of `primaryDecomposition`)
- Adds unnecessary package loads: `needsPackage "LegacyExamples"`, `loadPackage "LinearAlgebra"`

### 3.3 Universal Failure: The `**` vs `^` Debugging Task (cb_2)

All four models scored 0 on cb_2, which asks to identify that M2 uses `^` for exponentiation, not `**` (Python convention). Both Llama models left the `**` operator unchanged. The Qwen models either gave empty responses or only partially addressed the problem. This is a critical M2-specific syntactic distinction that no model has learned.

### 3.4 Universal Failure: String Concatenation Operators (cb_6, cb_7)

M2 uses `|` for horizontal and `||` for vertical string concatenation. All four models scored 0 on both questions. Common confusions:
- Qwen3-8B used `||` for horizontal (swapped)
- Qwen3-32B used `||` for horizontal and `++` for vertical
- Llama models hallucinated `cat`, `concatenate()`, or other non-M2 functions

## 4. Category-Level Performance

| Category | Qwen3-8B | Qwen3-32B | Llama-3.1-8B | Llama-3.3-70B | Avg |
|----------|----------|-----------|--------------|---------------|-----|
| Basic (SL) | 1.33 | 1.33 | 0.67 | 1.33 | 1.17 |
| Basic M2 Calcs | 0.78 | 0.78 | 0.67 | 0.89 | 0.78 |
| Basic M2 I/O | 1.00 | 1.33 | 0.00 | 0.00 | 0.58 |
| Basic m2 I/O (cb) | 0.25 | 0.75 | 0.25 | 0.50 | 0.44 |
| Debugging | 0.33 | 0.33 | 0.00 | 0.00 | 0.17 |
| Flow Control | 1.00 | 0.00 | 0.00 | 2.00 | 0.75 |
| Package Importing | 2.00 | 2.00 | 0.00 | 1.00 | 1.25 |
| Package Imports | 0.00 | 0.00 | 1.00 | 1.00 | 0.50 |

**Strongest category:** Package Importing (SL-3) and Basic algebra tasks (SL-2, SL-4) where the M2 syntax closely mirrors standard mathematical notation.

**Weakest category:** Debugging (0.17 avg). Models cannot identify M2-specific syntax errors, suggesting they lack a grounded model of M2's grammar distinct from Python/Sage/Mathematica.

## 5. Hardest and Easiest Questions

### Hardest (score = 0/8 across all models)
| Question | Category | Why it's hard |
|----------|----------|---------------|
| cb_2 | Debugging | Requires knowing `^` vs `**` distinction |
| cb_6 | Basic I/O | Requires knowing `\|` = horizontal concat |
| cb_7 | Basic I/O | Requires knowing `\|\|` = vertical concat |
| sf_2 | Debugging | Requires `debug Core` + `raw R` — obscure internal API |
| RA_1 | Basic Calcs | Requires `genericMatrix` with indexed variables and `flatten` |
| RA_3 | Basic Calcs | Requires `QRDecomposition` (exact case) + `clean` function |

### Easiest (score >= 5/8)
| Question | Category | Score | Why it's easier |
|----------|----------|-------|-----------------|
| SL-2 | Basic | 7/8 | Standard quotient ring + kernel — close to textbook math |
| sf_9 | Basic Calcs | 6/8 | List addition — simple, transferable syntax |
| SL-3 | Package Importing | 5/8 | `primaryDecomposition` is well-documented |
| SL-4 | Basic | 5/8 | Partial derivatives + ideal — standard math operations |
| RA_4 | Basic Calcs | 5/8 | `gcd()` is universal across CAS systems |

## 6. Model-Specific Observations

### Qwen3-32B (Best overall: 42%)
- Best at M2-specific syntax (only model to get `restart`, `3!^2`)
- Strong on algebraic geometry tasks (SL-2, SL-3, SL-4 all correct)
- Major weakness: empty responses from reasoning token exhaustion
- Would likely improve significantly with higher max_tokens

### Qwen3-8B (38%)
- Similar profile to Qwen3-32B but weaker on M2 idioms
- Tends to use verbose/non-standard syntax (`factorial()` instead of `!`)
- Good algebraic intuition (SL-3, SL-4 correct)

### Llama-3.3-70B (36%)
- Only model to correctly use `viewHelp`, `apply(L, f)`, `scan(L, print)`
- Strong on functional programming patterns
- Critical flaw: frequently overwrites `ZZ` with `ZZ = ZZ/n`
- Uses `decompose()` instead of `primaryDecomposition` — close but wrong function

### Llama-3.1-8B (20%)
- Worst overall by a wide margin
- Frequently hallucinates syntax from other languages
- Only model to get `f = (x, y) -> x * y` exactly right (sf_5)
- Unreliable for any M2-specific task

## 7. Implications for the Benchmark

### Benchmark Strengths
- Good coverage of difficulty levels: some questions are universally easy (SL-2), others universally hard (cb_2)
- Category diversity tests different M2 competencies
- The hardest questions (debugging, string ops) test genuine M2-specific knowledge vs. general CAS transfer

### Benchmark Concerns
- **Category naming inconsistency:** "Basic m2 input and output" vs "Basic M2 I/O" vs "Basic" — should be normalized
- **Ambiguous scoring:** Some prompts accept multiple valid approaches (e.g., `help` vs `viewHelp`), making automated scoring difficult
- **RA_5 is broken** in the source JSON and was excluded
- **cb_3 is empty** in the source and was excluded
- **Small sample size:** 25 questions gives limited statistical power per category

### Scoring Methodology Note
This analysis uses **manual code review scoring** without M2 execution. A response was scored as correct (2) if the code would plausibly produce the expected output in M2, and partial (1) if the approach was right but syntax was wrong. Future eval rounds should include automated M2 execution to validate outputs.

## 8. Recommendations for Next Steps

1. **Increase max_tokens to 2048+** for Qwen3 models to eliminate empty responses
2. **Add automated M2 execution** to validate model outputs against expected results
3. **Normalize categories** across benchmark files
4. **Fix RA_5** (broken JSON) and fill in cb_3 (empty question)
5. **Add more questions** in weak categories (Debugging, Flow Control) where n is currently small
6. **Test with fine-tuned models** — baseline open-source performance is low enough that fine-tuning on M2 documentation and examples would likely yield large gains
7. **Consider few-shot prompting** — providing 1-2 M2 examples in the system prompt could significantly help models distinguish M2 syntax from Python/Sage
