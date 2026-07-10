# Implementation Trial: Assessing Large Language Models on Islamic

**Generated:** 20260403
**Trial ID:** RV-T1
**Benchmark:** Assessing Large Language Models on Islamic
**Paper:** `2025-Ghaly-Assessing Large Language Models on Islamic.md`

---

## 1. Benchmark Summary

| Field | Value |
|-------|-------|
| **Tradition** | Islam (Abrahamic) |
| **Format** | MCQ |
| **Dataset Size** | 0 |
| **Data Source** | GitHub |
| **Data URL** | https://github.com/bouchekif/inheritance_evaluation |
| **Languages** | Arabic |
| **LLMs Previously Tested** | Gemini, GPT-4, Llama-3, Mistral, o3 |
| **Composite Score** | 48.2 (RD=43.0, PE=80.0, CI=12.0) |

## 2. Trial Configuration

| Parameter | Value |
|-----------|-------|
| **Samples** | 30 items (stratified if categories available) |
| **Models** | Claude Opus/Sonnet, GPT-4o, Llama-3-70B (minimum) |
| **Prompting** | Zero-shot (baseline) + 3-shot with tradition-specific examples |
| **Scorer** | Unknown |

## 3. Data Acquisition Checklist

- [ ] Downloaded/accessed benchmark data from https://github.com/bouchekif/inheritance_evaluation
- [ ] Verified data format and structure
- [ ] Identified sub-categories/difficulty levels
- [ ] Sampled 30 items (stratified)
- [ ] Prepared prompts for each item

## 4. Implementation Steps

### Step 4.1: Data Loading
```python
# Template for loading benchmark data
# Adapt based on actual data format
import json

# For MCQ/MRC format:
# data = json.load(open("path/to/benchmark.json"))
# items = data["questions"][:{n_samples}]

# For shared task format:
# with open("path/to/test.tsv") as f:
#     items = [line.strip().split("\t") for line in f][:{n_samples}]
```

### Step 4.2: Prompt Construction
```python
# Zero-shot prompt template
ZERO_SHOT = """{system_prompt}

Question: {question}
{options_if_mcq}

Answer:"""

# Few-shot prompt template (3 examples)
FEW_SHOT = """{system_prompt}

Here are some examples:

{example_1}
{example_2}
{example_3}

Now answer this question:
Question: {question}
{options_if_mcq}

Answer:"""
```

### Step 4.3: Model Execution
```python
# Run each model on all sampled items
# Record: model_name, item_id, response, latency, tokens_used
# Use appropriate API clients (anthropic, openai, together/vllm for open models)
```

### Step 4.4: Scoring
```python
# Score each response using benchmark's metric
# Common metrics:
# - Exact match (MCQ): response == gold_answer
# - F1 (MRC): token-level F1 between response and gold span
# - Model-graded (open-ended): use GPT-4 or Claude as judge
# - Human evaluation (scenarios): expert scoring on rubric
```

## 5. Results (To Be Filled After Trial)

### 5.1 Accuracy by Model

| Model | Zero-Shot | 3-Shot | Delta |
|-------|-----------|--------|-------|
| Claude Opus | — | — | — |
| Claude Sonnet | — | — | — |
| GPT-4o | — | — | — |
| Llama-3-70B | — | — | — |

### 5.2 Ceiling/Floor Analysis

| Check | Result | Notes |
|-------|--------|-------|
| Any model >90%? | — | Ceiling effect? |
| Any model <20%? | — | Floor effect? |
| Score range | — | Good if 30-80% |
| Score variance | — | Good if >20% |

### 5.3 Error Analysis

| Error Type | Count | % | Example |
|-----------|-------|---|---------|
| Knowledge gap | — | — | — |
| Reasoning failure | — | — | — |
| Cultural misunderstanding | — | — | — |
| Format error | — | — | — |

### 5.4 Implementation Difficulty

| Aspect | Rating (1-5) | Notes |
|--------|-------------|-------|
| Data access | — | — |
| Format adaptation | — | — |
| Scoring setup | — | — |
| Prompt engineering | — | — |
| Overall difficulty | — | — |

## 6. Verdict

**[ ] IMPLEMENT** — Ready for full-scale evaluation
**[ ] MODIFY** — Viable but needs adaptation (describe changes needed)
**[ ] SKIP** — Not suitable for implementation (explain why)

### Justification
_To be filled after trial completion._

## 7. Meta-Evaluation Scores

| Criterion | Score | Notes |
|-----------|-------|-------|
| Content Validity | — / HIGH, MEDIUM, LOW | — |
| Discriminative Power | — / HIGH, MEDIUM, LOW | — |
| Cultural Authenticity | — / NATIVE, CONSULTED, EXTERNAL | — |
| Reproducibility | — / 5 | — |
| Complementarity | — / 5 | — |
| Construct Coverage | — | Knowledge/Reasoning/Values/etc. |
| Annotation Quality | — / EXPERT, MIXED, CROWD, AUTO | — |
