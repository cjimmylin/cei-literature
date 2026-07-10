# Quick Assessment: 25-Feature Subset for Moral Psychology Benchmarks

## Overview

This document defines a practical 25-feature subset of the full 157-feature moral psychology benchmark evaluation framework. The Quick Assessment is designed to take approximately 60 minutes per benchmark (vs 5+ hours for the full framework), while preserving strong correlation with the comprehensive evaluation.

**Selection method:** Variance-based discriminative power across 54 benchmarks
**Correlation with full assessment:** Pearson r = 0.630 (r-squared = 39.7%)
**Rank preservation:** Spearman rho = 0.632
**Estimated scoring time:** ~2.5 min/feature x 25 = ~60 minutes total

## Tier Allocation

| Tier | Name | Selected | Total | Selection Rate |
|------|------|----------|-------|----------------|
| A | Psychological Depth | 2 | 6 | 33% |
| B | Practical Ease | 2 | 6 | 33% |
| C | Citation Impact | 1 | 4 | 25% |
| D | Psychometric Rigor | 4 | 24 | 17% |
| E | LLM-Specific Validity | 6 | 44 | 14% |
| F | Cultural & Philosophical Breadth | 6 | 44 | 14% |
| G | Theory Fidelity & Provenance | 4 | 29 | 14% |
| **Total** | | **25** | **157** | **16%** |

## Selected Features

| # | ID | Tier | Name | Disc. Power | Variance | Non-Null Rate |
|---|-----|------|------|-------------|----------|---------------|
| 1 | A2 | A | Moral foundation coverage | 393.0 | 544.1 | 0.72 |
| 2 | A5 | A | Cultural grounding | 854.2 | 1182.7 | 0.72 |
| 3 | B2 | B | Administration time | 770.6 | 1066.9 | 0.72 |
| 4 | B10 | B | Community adoption | 772.3 | 1069.4 | 0.72 |
| 5 | C3 | C | H-index contribution | 794.0 | 1099.3 | 0.72 |
| 6 | D1 | D | Internal consistency evidence | 803.5 | 803.5 | 1.00 |
| 7 | D3 | D | Factor structure validation | 928.8 | 928.8 | 1.00 |
| 8 | D8 | D | Measurement invariance across populations | 1001.9 | 1001.9 | 1.00 |
| 9 | D21 | D | Sample size adequacy for claims | 805.6 | 805.6 | 1.00 |
| 10 | E26 | E | API compatibility tier | 505.1 | 505.1 | 1.00 |
| 11 | E27 | E | Token budget efficiency | 1193.4 | 1193.4 | 1.00 |
| 12 | E28 | E | Output determinism | 763.7 | 763.7 | 1.00 |
| 13 | E31 | E | Anchor item availability | 549.4 | 549.4 | 1.00 |
| 14 | E34 | E | Demographic sensitivity testing | 748.6 | 748.6 | 1.00 |
| 15 | E40 | E | Moral development trajectory simulation | 864.8 | 864.8 | 1.00 |
| 16 | F1 | F | Stereotype amplification detection | 483.9 | 483.9 | 1.00 |
| 17 | F4 | F | Moral conflict structure | 513.0 | 513.0 | 1.00 |
| 18 | F6 | F | Cultural validation breadth | 536.3 | 536.3 | 1.00 |
| 19 | F9 | F | Language coverage | 559.9 | 559.9 | 1.00 |
| 20 | F41 | F | Moral trade-off explicitness | 465.6 | 465.6 | 1.00 |
| 21 | F44 | F | Moral development sensitivity | 864.8 | 864.8 | 1.00 |
| 22 | G10 | G | Reasoning sophistication capture | 884.9 | 884.9 | 1.00 |
| 23 | G14 | G | Citation hub score (downstream adoption) | 1519.3 | 1519.3 | 1.00 |
| 24 | G16 | G | Replication count | 1432.8 | 1432.8 | 1.00 |
| 25 | G17 | G | Dataset derivative count | 1242.1 | 1242.1 | 1.00 |

## Scoring Rubrics

Each feature is scored on a 0-100 scale. Below are brief rubrics for the 25 selected features.

### A2: Moral foundation coverage

**Tier:** A (Psychological Depth)
**Discriminative power:** 393.0

Breadth of moral foundation coverage (e.g., MFT's 5-6 foundations, Schwartz's values). How many distinct moral dimensions does the benchmark measure?

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### A5: Cultural grounding

**Tier:** A (Psychological Depth)
**Discriminative power:** 854.2

Degree of cultural grounding in benchmark design: WEIRD-only assumptions (low) vs. cross-cultural development with local validation (high).

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### B2: Administration time

**Tier:** B (Practical Ease)
**Discriminative power:** 770.6

Time required to administer the benchmark to one model. Lower time scores higher: <15 min (high) vs. >2 hours (low).

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### B10: Community adoption

**Tier:** B (Practical Ease)
**Discriminative power:** 772.3

Community adoption: unused (low) vs. widely used in published LLM evaluations with active community (high).

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### C3: H-index contribution

**Tier:** C (Citation Impact)
**Discriminative power:** 794.0

Contribution to the lead author's h-index; proxy for the paper's standing in the field.

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### D1: Internal consistency evidence

**Tier:** D (Psychometric Rigor)
**Discriminative power:** 803.5

Whether the benchmark reports internal consistency reliability (Cronbach's alpha, McDonald's omega, or split-half reliability) computed on the huma...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### D3: Factor structure validation

**Tier:** D (Psychometric Rigor)
**Discriminative power:** 928.8

Whether the benchmark's factor structure (e.g., MFT's 5-factor model, Schwartz's circular value structure) has been confirmed through confirmatory ...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### D8: Measurement invariance across populations

**Tier:** D (Psychometric Rigor)
**Discriminative power:** 1001.9

Whether the benchmark has been tested for measurement invariance (configural, metric, scalar) across relevant population groups — cultures, genders...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### D21: Sample size adequacy for claims

**Tier:** D (Psychometric Rigor)
**Discriminative power:** 805.6

Evaluates whether the benchmark's item count and condition count are adequate to support the claims it makes — using power analysis, effect size es...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### E26: API compatibility tier

**Tier:** E (LLM-Specific Validity)
**Discriminative power:** 505.1

Rates how well the benchmark integrates with standard LLM evaluation APIs and harnesses

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### E27: Token budget efficiency

**Tier:** E (LLM-Specific Validity)
**Discriminative power:** 1193.4

Measures the ratio of interpretable signal to total tokens consumed

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### E28: Output determinism

**Tier:** E (LLM-Specific Validity)
**Discriminative power:** 763.7

Whether the benchmark's scoring produces deterministic results given the same model outputs

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### E31: Anchor item availability

**Tier:** E (LLM-Specific Validity)
**Discriminative power:** 549.4

Whether the benchmark includes anchor items — items with known human norms that can be used to calibrate model responses to a common scale

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### E34: Demographic sensitivity testing

**Tier:** E (LLM-Specific Validity)
**Discriminative power:** 748.6

Whether the benchmark tests whether moral judgments vary based on the demographic attributes of the moral actors described in scenarios (race, gend...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### E40: Moral development trajectory simulation

**Tier:** E (LLM-Specific Validity)
**Discriminative power:** 864.8

Evaluates whether the benchmark can characterize the model's position on a moral development trajectory — not just its current moral profile, but w...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### F1: Stereotype amplification detection

**Tier:** F (Cultural & Philosophical Breadth)
**Discriminative power:** 483.9

Whether the benchmark can detect when an LLM overshoots real human cultural profiles — producing a more extreme version of the cultural pattern tha...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### F4: Moral conflict structure

**Tier:** F (Cultural & Philosophical Breadth)
**Discriminative power:** 513.0

Whether the benchmark includes structured moral conflicts where two endorsed values compete (care vs fairness, autonomy vs harm-prevention)

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### F6: Cultural validation breadth

**Tier:** F (Cultural & Philosophical Breadth)
**Discriminative power:** 536.3

Counts the number of distinct cultural clusters (per Inglehart-Welzel or Hofstede regional groupings) in which the benchmark has been validated wit...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### F9: Language coverage

**Tier:** F (Cultural & Philosophical Breadth)
**Discriminative power:** 559.9

Counts the number of languages in which the benchmark has been administered to human participants with published norms

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### F41: Moral trade-off explicitness

**Tier:** F (Cultural & Philosophical Breadth)
**Discriminative power:** 465.6

Evaluates whether the benchmark makes moral trade-offs explicit and tests the model's ability to recognize, articulate, and navigate them

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### F44: Moral development sensitivity

**Tier:** F (Cultural & Philosophical Breadth)
**Discriminative power:** 864.8

Whether the benchmark can detect differences in moral development level (Kohlberg stages, Neo-Kohlbergian schema, or equivalent developmental frame...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### G10: Reasoning sophistication capture

**Tier:** G (Theory Fidelity & Provenance)
**Discriminative power:** 884.9

Whether the benchmark captures the QUALITY of moral reasoning, not just the conclusion reached

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### G14: Citation hub score (downstream adoption)

**Tier:** G (Theory Fidelity & Provenance)
**Discriminative power:** 1519.3

Measures the benchmark's role as a citation hub — whether other benchmarks cite it as a foundation

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### G16: Replication count

**Tier:** G (Theory Fidelity & Provenance)
**Discriminative power:** 1432.8

Counts the number of independent replications of the benchmark (not just re-administrations of the same instrument, but methodological replications...

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

### G17: Dataset derivative count

**Tier:** G (Theory Fidelity & Provenance)
**Discriminative power:** 1242.1

Counts the number of derivative datasets, adaptations, or extensions built on top of the original benchmark

| Score Range | Interpretation |
|-------------|----------------|
| 0-25 | Absent or minimal |
| 26-50 | Partial or emerging |
| 51-75 | Substantial |
| 76-100 | Comprehensive or exemplary |

## Computing the Quick Assessment Composite

1. Score each of the 25 features on the 0-100 scale using the rubrics above
2. Compute the arithmetic mean of all 25 scores
3. The result is the Quick Assessment composite (0-100 scale)

**Formula:** `Quick_Composite = mean(F1, F2, ..., F25)`

All features are equally weighted. If a feature cannot be scored (e.g., data unavailable), exclude it and compute the mean of the remaining features.

## Comparison with Full 157-Feature Assessment

- **Pearson r:** 0.630
- **R-squared:** 39.7% of variance explained
- **Spearman rho:** 0.632 (rank preservation)

### Benchmark Rankings Comparison

| Rank (Quick) | Benchmark | Quick Composite | Full Composite | Rank (Full) |
|-------------|-----------|-----------------|----------------|-------------|
| 1 | Do Moral Judgment and Reasoning Capability of | 61.4 | 66.0 | 8 |
| 2 | Multilingual Defining Issues Test | 61.4 | 61.2 | 19 |
| 3 | The Moral Machine experiment | 59.8 | 78.5 | 1 |
| 4 | Whose Morality Do They Speak? | 51.6 | 62.3 | 15 |
| 5 | Probing the Moral Development of Large Language | 50.6 | 63.2 | 14 |
| 6 | Culturally Grounded Personas in Large Language Models: Characterization and Alignment with Socio-Psychological Value Frameworks | 50.4 | 57.9 | 25 |
| 7 | Language Model Alignment in Multilingual Trolley | 49.6 | 69.3 | 4 |
| 8 | Conscience Conflict: Evaluating Language Models' Moral Understanding | 48.4 | 58.4 | 23 |
| 9 | Crowdsourcing moral machines | 47.6 | 69.9 | 3 |
| 10 | Decoding Multilingual Moral Preferences -- Unveiling LLM's Biases Through the Moral Machine Experiment | 45.6 | 62.0 | 16 |
| 11 | The moral machine experiment on large language | 44.4 | 69.9 | 2 |
| 12 | Does Moral Code Have a Moral Code? | 44.0 | 66.3 | 7 |
| 13 | Moral Foundations of Large Language Models | 43.6 | 63.8 | 11 |
| 14 | MoralBench | 42.2 | 50.0 | 41 |
| 15 | Large-scale moral machine experiment on large | 40.4 | 66.4 | 6 |
| 16 | Building Interpretable Models for Moral Decision-Making | 40.0 | 58.2 | 24 |
| 17 | TrolleyBench -- Evaluating Emergent Moral Reasoning and Consistency in LLMs | 32.8 | 52.2 | 36 |
| 18 | PRIME Framework Convergent Ethics | 30.8 | 50.2 | 39 |
| 19 | Revisiting the Trolley Problem for AI | 30.4 | 45.8 | 47 |
| 20 | Moral Foundations Twitter Corpus | 28.0 | 68.1 | 5 |
| 21 | Analyzing the Ethical Logic of Six Large Language Models | 28.0 | 42.5 | 48 |
| 22 | Assessing LLMs for Moral Value Pluralism | 27.8 | 55.6 | 29 |
| 23 | Model Editing as a Double-Edged Sword | 27.0 | 50.8 | 38 |
| 24 | Social Chemistry 101 | 26.8 | 60.9 | 21 |
| 25 | Are Rules Meant to be Broken? (UniMoral) | 26.2 | 57.0 | 28 |
| 26 | MFTCXplain | 25.2 | 57.9 | 26 |
| 27 | Value Kaleidoscope | 24.2 | 61.6 | 18 |
| 28 | Moral Foundations Vignettes | 22.4 | 64.5 | 9 |
| 29 | Differences in Moral Foundations of LLMs | 22.4 | 63.7 | 12 |
| 30 | The Dutch Moral Foundations Stimulus Database | 22.0 | 62.0 | 17 |
| 31 | The Moral Foundations Reddit Corpus | 21.4 | 61.0 | 20 |
| 32 | Situational factors shape moral judgments in the trolley dilemma | 21.2 | 63.9 | 10 |
| 33 | EMNLP (Educator-role Moral and Normative LLMs Profiling) | 21.2 | 46.6 | 46 |
| 34 | The Moral Foundations Weibo Corpus | 21.0 | 49.8 | 43 |
| 35 | Assessing the Alignment of LLMs With Human Values (PVQ-RR) | 20.8 | 63.3 | 13 |
| 36 | CVC | 20.6 | 52.8 | 35 |
| 37 | Insights into Moral Reasoning of AI | 20.0 | 57.6 | 27 |
| 38 | How Can a Deontological Decision Lead to Moral | 19.4 | 55.2 | 30 |
| 39 | Tracing Moral Foundations in LLMs | 18.2 | 51.0 | 37 |
| 40 | Mapping Moral Reasoning Circuits | 17.6 | 50.1 | 40 |
| 41 | M$^3$oralBench | 16.8 | 54.5 | 32 |
| 42 | Concerns and Values in Human-Robot Interactions | 15.4 | 36.1 | 52 |
| 43 | From Stability to Inconsistency | 14.0 | 48.2 | 44 |
| 44 | A survey on moral foundation theory and pre-trained language models: current advances and challenges | AI & SOCIETY | 13.6 | 34.8 | 53 |
| 45 | AdAEM: Adaptively and Automated Extensible Measurement for Value Alignment | 12.0 | 42.2 | 50 |
| 46 | Knowing But Not Doing: Convergent Morality and Divergent Action in LLMs (ValAct-15k) | 10.8 | 58.8 | 22 |
| 47 | ValueCompass: A Framework for Measuring Contextual Value Alignment | 10.8 | 55.0 | 31 |
| 48 | Value-Spectrum | 10.8 | 42.2 | 49 |
| 49 | GPLA: Generative Psycho-Lexical Approach for Constructing Value Systems | 10.8 | 41.5 | 51 |
| 50 | The Staircase of Ethics (Multi-step Moral Dilemmas) | 10.0 | 50.0 | 42 |
| 51 | Normative Evaluation of LLMs with Everyday Moral Dilemmas | 8.8 | 54.2 | 34 |
| 52 | The Pluralistic Moral Gap | 8.8 | 47.8 | 45 |
| 53 | The Straight and Narrow: Do LLMs Possess an Internal Moral Path? | 8.8 | 34.5 | 54 |
| 54 | How Much of a Pluralist is ChatGPT? | 7.5 | 54.2 | 33 |

---

*Generated 2026-04-04 by `build_quick_assessment.py` from 54-benchmark feature matrix.*
*Source: `20260404-extended-feature-matrix-v3.json` | Framework: `20260404-feature-framework-v2.md`*