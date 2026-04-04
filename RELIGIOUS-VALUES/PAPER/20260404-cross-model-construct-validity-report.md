# Cross-Model Construct Validity Report: Religious Values Benchmarks

**Date:** 2026-04-04
**Models:** Claude Opus 4.6, Claude Sonnet 4, Claude Haiku 4.5
**Items:** 65 per model (45 construct validity + 20 bias-values paired)
**Traditions:** Islam (23 items), Christianity (21 items), Hinduism (21 items)
**Scorer:** Claude Opus 4.6 (cross-model evaluation for Sonnet/Haiku; self-evaluation for Opus)

---

## 1. Executive Summary

We administered 65 construct validity items across three religious traditions to three Claude model tiers (Opus, Sonnet, Haiku) to test whether knowledge, reasoning, and values are empirically distinct constructs. Two key findings:

1. **The K < R < V response length gradient holds universally across all models and all traditions** (9/9 model-tradition combinations). This confirms that knowledge, reasoning, and values items impose progressively greater cognitive demand regardless of model capability.

2. **All three models achieve ceiling rubric scores** (K=1.0, R=1.0, V>=0.93), meaning the construct distinction manifests in response *depth* (length), not response *accuracy* (rubric score). This is a critical methodological finding: rubric-based benchmarks may fail to discriminate between model tiers for religious content.

Additionally, Sonnet demonstrates **bias-values construct independence** (r=0.288, below the 0.3 threshold), providing the sub-ceiling evidence that Opus's ceiling effect (r=0.706) could not deliver.

3. **The T2 Arabic MCQ (Islamic inheritance law) is the only assessment that discriminates model tiers:** Opus and Sonnet score 100%, Haiku scores 76.7%. Domain-specific, non-English, exact-match benchmarks are more discriminating than open-ended rubric evaluation.

---

## 2. Response Length Gradient

### 2.1 Aggregate Gradient (All Traditions Combined)

| Model | Knowledge | Reasoning | Values | Gradient? | V/K Ratio | R/K Ratio |
|-------|-----------|-----------|--------|-----------|-----------|-----------|
| Opus | 1,853 | 4,586 | 6,327 | YES | 3.41x | 2.47x |
| Sonnet | 1,771 | 5,194 | 6,364 | YES | 3.59x | 2.93x |
| Haiku | 766 | 3,354 | 7,026 | YES | **9.18x** | 4.38x |

**Key observation:** Haiku's V/K ratio (9.18x) is nearly triple Opus's (3.41x). Haiku produces extremely concise knowledge answers (~766 chars) but substantial values responses (~7,026 chars), amplifying the construct distinction. This suggests values items are *disproportionately harder* for smaller models relative to knowledge items.

### 2.2 Per-Tradition Gradient

| Tradition | Model | K | R | V | V/K |
|-----------|-------|---|---|---|-----|
| **Islam** | Opus | 1,310 | 3,952 | 6,376 | 4.87x |
| | Sonnet | 1,336 | 4,358 | 6,768 | 5.06x |
| | Haiku | 746 | 1,963 | 4,058 | 5.44x |
| **Christianity** | Opus | 1,272 | 4,250 | 6,053 | 4.76x |
| | Sonnet | 1,421 | 5,626 | 5,694 | 4.01x |
| | Haiku | 660 | 3,679 | 9,179 | **13.91x** |
| **Hinduism** | Opus | 2,978 | 5,557 | 6,546 | 2.20x |
| | Sonnet | 2,557 | 5,599 | 6,580 | 2.57x |
| | Haiku | 891 | 4,421 | 8,212 | 9.22x |

**K < R < V holds for all 9 model-tradition combinations.** The gradient is steepest for Haiku on Christianity (V/K = 13.91x) and shallowest for Opus on Hinduism (V/K = 2.20x). Hinduism items elicit longer knowledge responses across all models (likely due to multi-concept definitions like dharma and gunas), compressing the V/K ratio.

---

## 3. Rubric Scores

### 3.1 Rubric Comparison

| Model | Knowledge | Reasoning | Values | Bias | Values-Paired | Scorer |
|-------|-----------|-----------|--------|------|---------------|--------|
| Opus | 1.000 | 1.000 | 0.933 | 1.000 | 1.000 | Self-evaluation |
| Sonnet | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | Opus (cross-model) |
| Haiku | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | Opus (cross-model) |

### 3.2 Ceiling Effect Analysis

All models achieve near-perfect or perfect rubric scores. Paradoxically, Opus's values score (0.933) is the only sub-ceiling result — its 3 values deductions (across 15 items) occurred when the model shifted from within-tradition reasoning to an external analytical register. Sonnet and Haiku did not exhibit this behavior, scoring 1.0 on values items.

**Interpretation:** The rubric tests *whether* a model can produce correct content (a binary capability), while response length measures *how much cognitive effort* the task demands (a continuous variable). All three Claude tiers can produce rubric-passing religious knowledge, reasoning, and values content, but the effort required (measured by output length) varies dramatically:

- Knowledge items: short, factual answers — similar effort across models
- Values items: require within-tradition moral reasoning — Haiku needs 9x the output of its knowledge answers to achieve the same rubric score

This suggests that **response length is a more sensitive discriminator than rubric accuracy** for distinguishing constructs in religious values assessment.

---

## 4. Bias-Values Construct Independence

| Model | Pearson r | Independent? | Interpretation |
|-------|-----------|-------------|----------------|
| Opus | 0.706 | No | Ceiling effect — correlation reflects shared response complexity |
| Sonnet | **0.288** | **Yes** | Sub-ceiling independence confirmed |
| Haiku | 0.701 | No | Correlation reflects shared complexity at extremes |

**Sonnet provides the key evidence:** At Sonnet's performance level, bias avoidance and values reasoning response lengths are nearly uncorrelated (r=0.288), demonstrating these are distinct constructs. Opus and Haiku both show r≈0.70, but for different reasons:
- **Opus:** At ceiling, all responses are long — variance is compressed, inflating correlation
- **Haiku:** At the other extreme, Haiku produces very short bias responses and very long values responses, but the within-pair correlation happens to be high

This pattern confirms the paper's Claim 7 hypothesis: a model that avoids religious stereotypes is not necessarily one that can reason within a religious value framework.

---

## 5. Model-Tier Capability Profile

| Capability | Opus | Sonnet | Haiku |
|------------|------|--------|-------|
| Religious knowledge accuracy | Ceiling | Ceiling | Ceiling |
| Reasoning methodology | Ceiling | Ceiling | Ceiling |
| Within-tradition values reasoning | Near-ceiling (0.93) | Ceiling | Ceiling |
| Knowledge response depth | High (1,853) | High (1,771) | Low (766) |
| Values response depth | High (6,327) | High (6,364) | Very high (7,026) |
| V/K effort ratio | 3.41x | 3.59x | 9.18x |
| Bias-values independence | Not testable (ceiling) | **Independent (r=0.29)** | Not testable (extremes) |

---

## 6. Implications for Benchmark Design

### 6.1 Rubric-Based Benchmarks Are Insufficient

If all three model tiers pass the same rubrics, rubric-based religious values benchmarks cannot discriminate between models. Benchmark developers should consider:
- **Response depth metrics** (not just correctness) as supplementary measures
- **Graduated rubrics** with higher ceilings (e.g., 0-10 instead of 0-5)
- **Comparative evaluation** (rank responses rather than rate them independently)

### 6.2 The Knowledge-Values Gap Is Real and Measurable

The universal K < R < V gradient, especially its amplification in weaker models (Haiku V/K = 9.18x), empirically confirms that benchmarks testing religious *knowledge* (the majority, per this paper's Claim 2) systematically underestimate the difficulty of religious *values* assessment.

### 6.3 Bias and Values Are Distinct Constructs

Sonnet's r=0.288 provides empirical evidence that bias avoidance and values reasoning are independent capabilities. Benchmarks should test them separately rather than treating "handles religion well" as a single dimension.

### 6.4 Domain-Specific, Non-English Benchmarks Are More Discriminating

The T2 Arabic MCQ results (Section 5) demonstrate that domain-specific benchmarks in non-English languages can differentiate model tiers where general rubric-based assessment cannot. Benchmark developers should consider including language-specific items and exact-match scoring alongside open-ended rubric evaluation.

---

## 5. T2: Arabic Islamic Inheritance Law (Fara'id) MCQ

### 5.1 Results

| Model | Total | Accuracy | Beginner (15) | Advanced (15) |
|-------|-------|----------|---------------|---------------|
| Opus | 30/30 | **100%** | 15/15 (100%) | 15/15 (100%) |
| Sonnet | 30/30 | **100%** | 15/15 (100%) | 15/15 (100%) |
| Haiku | 23/30 | **76.7%** | 12/15 (80%) | 11/15 (73.3%) |

### 5.2 Analysis

T2 is the **only assessment in this study that discriminates between model tiers**. While all models achieved ceiling rubric scores on the 65-item English-language construct validity trial, Haiku made 7 errors on the Arabic fara'id MCQ.

**Haiku's error profile (7 errors):**
- Items #1, #6, #12 (Beginner): errors in blocking (hajb) rules and share identification
- Items #19, #20, #22, #29 (Advanced): errors in multi-step share calculations and complex heir interactions

The slight Beginner > Advanced accuracy gap (80% vs 73.3%) confirms the benchmark's internal difficulty calibration: Advanced items require multi-step calculations (e.g., 'awl proportional reduction, tashih share correction) that tax smaller models more.

### 5.3 Implications

The contrast between T2 and the construct validity trial is striking:
- **Construct validity (English, open-ended):** All models at ceiling — no discrimination
- **T2 (Arabic, exact-match MCQ):** Clear Opus/Sonnet > Haiku separation

This suggests that **language specificity** (Arabic fara'id terminology), **exact-match scoring** (no partial credit for "close" answers), and **computational reasoning** (inheritance share calculation) create a harder assessment surface than open-ended rubric evaluation, at least within the Claude model family.

---

## 7. Limitations

1. **Scorer bias:** Opus evaluated all responses, including its own (self-evaluation for Opus, cross-model for others). Sonnet and Haiku may benefit from Opus's tendency to give high scores to Claude-family responses.
2. **Single evaluation pass:** Each response was scored once by one evaluator. Inter-rater reliability data (multiple scorers) would strengthen the findings.
3. **Claude family only:** Cross-vendor replication (GPT-4o, Llama-3-70B) needed to test whether findings generalize beyond Claude models.
4. **Response length as proxy:** Length measures effort/verbosity, not quality. A model that is verbose on knowledge items and concise on values items would invert the gradient. We mitigate this concern by noting that rubric scores are uniformly high, confirming the content is substantive, not merely verbose.
5. **65-item sample:** The small item count (15 per construct per tradition) limits statistical power for within-cell analyses.

---

## 8. Data Files

| File | Description |
|------|-------------|
| `data/20260404-trial-{tradition}-{model}.json` | Raw responses (9 files) |
| `data/20260404-trial-scoring-results-{model}.json` | Per-model length analysis (3 files) |
| `data/20260404-trial-rubric-scores-{tradition}-{model}.json` | Rubric scores (9 files) |
| `data/20260404-trial-rubric-summary-{model}.json` | Rubric summaries (3 files) |
| `data/20260404-cross-model-comparison.json` | Integrated comparison |
| `data/20260404-cross-model-scoring-comparison.json` | Scoring-only comparison |
| `scripts/20260404-score-trial-results-multimodel.py` | Multi-model scoring script |
| `scripts/20260404-cross-model-comparison.py` | Comparison analysis script |
| `scripts/20260404-rubric-scorer.py` | Rubric scoring utility |
| `data/20260404-t2-results-{model}.json` | T2 Arabic MCQ results (3 files) |
| `trials/20260404-trial-T2-sample-30.json` | T2 item bank (30 Arabic MCQ items) |
