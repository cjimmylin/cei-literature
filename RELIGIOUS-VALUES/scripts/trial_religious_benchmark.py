#!/usr/bin/env python3
"""
Phase 8: Implementation Trial Runner for Religious Values Benchmarks

Runs a standardized trial on a selected benchmark from the Top 15:
1. Sample N items from the benchmark
2. Present to frontier LLMs
3. Score using benchmark's metric
4. Assess ceiling/floor effects, discrimination, implementation difficulty

Usage:
    python trial_religious_benchmark.py --benchmark <name> [--n-samples 30] [--dry-run]

This script provides the FRAMEWORK for trials. Actual API calls to LLMs
require appropriate API keys and should be run manually.

Output: RELIGIOUS-VALUES/trials/YYYYMMDD-trial-RV-T{N}-{name}.md
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
TRIALS_DIR = PROJECT_DIR / "trials"

TODAY = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# Trial template
# ---------------------------------------------------------------------------
TRIAL_TEMPLATE = """# Implementation Trial: {benchmark_name}

**Generated:** {date}
**Trial ID:** RV-T{trial_num}
**Benchmark:** {benchmark_name}
**Paper:** `{filename}`

---

## 1. Benchmark Summary

| Field | Value |
|-------|-------|
| **Tradition** | {tradition} ({family}) |
| **Format** | {format_code} |
| **Dataset Size** | {dataset_size} |
| **Data Source** | {data_source} |
| **Data URL** | {data_url} |
| **Languages** | {languages} |
| **LLMs Previously Tested** | {llms_tested} |
| **Composite Score** | {composite} (RD={rd}, PE={pe}, CI={ci}) |

## 2. Trial Configuration

| Parameter | Value |
|-----------|-------|
| **Samples** | {n_samples} items (stratified if categories available) |
| **Models** | Claude Opus/Sonnet, GPT-4o, Llama-3-70B (minimum) |
| **Prompting** | Zero-shot (baseline) + 3-shot with tradition-specific examples |
| **Scorer** | {scorer_type} |

## 3. Data Acquisition Checklist

- [ ] Downloaded/accessed benchmark data from {data_url}
- [ ] Verified data format and structure
- [ ] Identified sub-categories/difficulty levels
- [ ] Sampled {n_samples} items (stratified)
- [ ] Prepared prompts for each item

## 4. Implementation Steps

### Step 4.1: Data Loading
```python
# Template for loading benchmark data
# Adapt based on actual data format
import json

# For MCQ/MRC format:
# data = json.load(open("path/to/benchmark.json"))
# items = data["questions"][:{{n_samples}}]

# For shared task format:
# with open("path/to/test.tsv") as f:
#     items = [line.strip().split("\\t") for line in f][:{{n_samples}}]
```

### Step 4.2: Prompt Construction
```python
# Zero-shot prompt template
ZERO_SHOT = \"\"\"{{system_prompt}}

Question: {{question}}
{{options_if_mcq}}

Answer:\"\"\"

# Few-shot prompt template (3 examples)
FEW_SHOT = \"\"\"{{system_prompt}}

Here are some examples:

{{example_1}}
{{example_2}}
{{example_3}}

Now answer this question:
Question: {{question}}
{{options_if_mcq}}

Answer:\"\"\"
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
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    # Parse args
    benchmark_name = None
    n_samples = 30
    dry_run = "--dry-run" in sys.argv

    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--benchmark" and i < len(sys.argv) - 1:
            benchmark_name = sys.argv[i + 1]
        elif arg == "--n-samples" and i < len(sys.argv) - 1:
            try:
                n_samples = int(sys.argv[i + 1])
            except ValueError:
                pass

    # Load Top 15
    t15_files = sorted(DATA_DIR.glob("*-religious-values-top15.json"))
    if not t15_files:
        print("ERROR: No Top 15 file found.")
        sys.exit(1)

    with open(t15_files[-1]) as f:
        top15_data = json.load(f)

    top15 = top15_data["top15"]

    if not benchmark_name:
        # List available benchmarks
        print("Available benchmarks (Top 15):")
        for i, e in enumerate(top15, 1):
            print(f"  {i:2d}. {e['short_title'][:60]}")
        print(f"\nUsage: python trial_religious_benchmark.py --benchmark <number or partial title>")
        return

    # Find the benchmark
    target = None
    try:
        idx = int(benchmark_name) - 1
        if 0 <= idx < len(top15):
            target = top15[idx]
    except ValueError:
        # Search by partial title match
        for e in top15:
            if benchmark_name.lower() in e.get("short_title", "").lower():
                target = e
                break

    if not target:
        print(f"ERROR: Benchmark '{benchmark_name}' not found in Top 15.")
        return

    print(f"Generating trial template for: {target['short_title']}")

    # Determine trial number
    existing_trials = sorted(TRIALS_DIR.glob("*-trial-RV-T*.md")) if TRIALS_DIR.exists() else []
    trial_num = len(existing_trials) + 1

    # Generate trial report
    name_slug = target["short_title"][:30].replace(" ", "-").replace("/", "-").lower()
    report = TRIAL_TEMPLATE.format(
        benchmark_name=target.get("short_title", "Unknown"),
        date=TODAY,
        trial_num=trial_num,
        filename=target.get("filename", ""),
        tradition=target.get("D5_primary_tradition", "Unknown"),
        family=target.get("D6_tradition_family", "Unknown"),
        format_code=target.get("P1_format", "Unknown"),
        dataset_size=target.get("P2_dataset_size", "Unknown"),
        data_source=target.get("P3_data_availability", "Unknown"),
        data_url=target.get("DATA_URL", "N/A") or target.get("P3_url", "N/A"),
        languages=target.get("P10_language", "Unknown"),
        llms_tested=target.get("D3_llms_tested", "N/A"),
        composite=f"{target.get('COMPOSITE', 0):.1f}",
        rd=f"{target.get('RD_score', 0):.1f}",
        pe=f"{target.get('PE_score', 0):.1f}",
        ci=f"{target.get('CI_score', 0):.1f}",
        n_samples=n_samples,
        scorer_type=target.get("P8_scorer_type", "Unknown"),
    )

    TRIALS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = TRIALS_DIR / f"{TODAY}-trial-RV-T{trial_num}-{name_slug}.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"Trial template: {out_path}")
    print("Fill in results after running the trial.")


if __name__ == "__main__":
    main()
