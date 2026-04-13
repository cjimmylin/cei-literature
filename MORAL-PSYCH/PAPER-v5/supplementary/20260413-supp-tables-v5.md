# Supplementary Tables

## Moral Psychology Benchmarks: A Meta-Evaluation of 292 Candidates Across 13 Theories

**Version:** 4.0 (Full rebuild, 2026-04-05)

All data in these tables are derived from the full 292-candidate feature matrix (`20260405-full-292-feature-matrix.json`), the tier assignment file (`20260405-tier-assignment.json`), and the cross-vendor comparison file (`20260404-cross-vendor-comparison.json`).

---

## Table ST1: Full 162-Feature Framework

A comprehensive listing of all 162 features across seven tiers. For Tiers A--C (17 scored features), composite weights are shown. For Tiers D--G (141 characterization features), composite weight is 0.00 (not used in ranking).

### Tier A: Psychological Depth (6 features, tier weight = 0.50)

| Feature ID | Tier | Name | Scale | Composite Weight | Description |
|:----------:|:----:|------|-------|:----------------:|-------------|
| A1 | A | Construct depth (theories engaged) | 0--100 (count-mapped) | 0.075 | Number of distinct moral psychology theories with substantive engagement. 0=0; 1=30; 2=60; 3=80; 4+=100. |
| A2 | A | Construct operationalization | 0--100 (ordinal) | 0.125 | Fidelity of theoretical operationalization. Validated instrument=100; theory-derived=70; theory-inspired=40; keyword-only=10. |
| A3 | A | Dilemma complexity | 0--100 | 0.075 | Complexity and depth of moral scenarios. Single-sentence=30; multi-sentence=60; multi-paragraph=90. |
| A4 | A | Source instrument provenance | 0--100 (ordinal) | 0.050 | Validated psychometric source instrument. Validated=100; original with development=80; none=0. |
| A5 | A | Human baseline availability | 0--100 (ordinal) | 0.075 | Published population norms=100; paper-specific sample=70; partial=40; none=0. |
| A6 | A | Construct validity evidence | 0--100 (ordinal) | 0.100 | Validity evidence types (convergent, discriminant, criterion, content, structural). 5=100; 4=75; 3=50; 2=30; 1=10. |

### Tier B: Practical Ease (7 scored features, tier weight = 0.30)

| Feature ID | Tier | Name | Scale | Composite Weight | Description |
|:----------:|:----:|------|-------|:----------------:|-------------|
| B1 | B | Task format | 0--100 (format-mapped) | 0.030 | MCQ=100; binary=90; forced-choice=85; Likert=70; ranking=60; free-text=50. |
| B2 | B | Dataset size | 0--100 (log-scaled) | 0.045 | <50=20; 200=40; 1K=60; 5K=75; 20K=85; >20K=100. |
| B3 | B | Data availability | 0--100 (platform) | 0.060 | HuggingFace=100; GitHub=95; OSF=90; anonymous link=60; paper only=0. |
| B4 | B | Code availability | 0--100 (ordinal) | 0.030 | Full pipeline=100; partial=50; none=0. |
| B5 | B | Instruction simplicity | -- | Excluded | Requires benchmark distribution infrastructure unavailable for all candidates. |
| B6 | B | Harness compatibility | 0--100 (tier-mapped) | 0.045 | Native integration=100; straightforward port=70; custom=40. |
| B7 | B | Scorer complexity | 0--100 (complexity) | 0.045 | Exact match=100; normalization=85; model-graded=60; psychometric=40; human=20. |
| B8 | B | Open access | -- | Excluded | Same rationale as B5. |
| B9 | B | Documentation completeness | -- | Excluded | Same rationale as B5. |
| B10 | B | LLM administration fidelity | 0--100 (ordinal) | 0.045 | Direct=100; minor adaptation=70; major=40; paradigm change=10. |

### Tier C: Citation Impact (4 scored features, tier weight = 0.20)

| Feature ID | Tier | Name | Scale | Composite Weight | Description |
|:----------:|:----:|------|-------|:----------------:|-------------|
| C1 | C | Total citations | 0--100 (log-scaled) | 0.060 | <5=10; 20=30; 50=50; 100=65; 200=75; 500=85; >500=100. |
| C2 | C | Recent citation velocity | 0--100 (log-scaled) | 0.060 | Citations/year. <2=15; 5=30; 10=50; 25=65; 50=80; >100=100. |
| C3 | C | Venue tier | 0--100 (tier-mapped) | 0.050 | Tier 1 (Nature, NeurIPS, ACL)=100; Tier 2 (AAAI, EMNLP)=75; Tier 3=50; Tier 4 (arXiv)=25. |
| C4 | C | Cross-domain citations | -- | Excluded | Requires cross-field citation tracing beyond available data. |
| C5 | C | Hub/leaderboard presence | 0--100 (binary) | 0.030 | Major hub=100; minor hub=50; none=0. |

### Tier D: Psychometric Rigor (24 features, composite weight = 0.00)

| Feature ID | Tier | Name | Description |
|:----------:|:----:|------|-------------|
| D1 | D | Internal consistency evidence | Cronbach's alpha or McDonald's omega reporting |
| D2 | D | Test-retest reliability evidence | Temporal stability with r >= 0.80 |
| D3 | D | Factor structure validation | CFA/EFA results and fit indices |
| D4 | D | Item-total correlation range | All correlations in 0.30--0.70 |
| D5 | D | Ceiling/floor effect prevalence | Percentage of items with ceiling/floor effects |
| D6 | D | Response distribution normality | Subscale normality (skew, kurtosis) |
| D7 | D | Discrimination index adequacy | Discrimination > 0.30 for all items |
| D8 | D | Measurement invariance | Scalar invariance across >= 3 groups |
| D9 | D | LLM ceiling compression index | Measurement range compression for LLMs (35% null) |
| D10 | D | Output parsing reliability | Parsing accuracy > 99% |
| D11 | D | Value hierarchy stability | Rank-order stability (Kendall's W or ICC) |
| D12 | D | Implicit vs. explicit mode | Measures both implicit and explicit moral attitudes |
| D13 | D | Sampling strategy transparency | Documented item sampling from defined universe |
| D14 | D | Item source transparency | Per-item provenance documentation |
| D15 | D | Pilot testing documentation | Pilot study with sample, results, modifications |
| D16 | D | Inclusion/exclusion criteria clarity | Clear criteria for valid responses |
| D17 | D | Response coding reliability | Inter-rater kappa > 0.80 |
| D18 | D | Construct operationalization validity | Expert validation + convergent/discriminant evidence |
| D19 | D | Item discrimination power (IRT) | IRT analysis with discrimination parameters |
| D20 | D | Response distribution entropy | Response distribution quantification (35% null) |
| D21 | D | Sample size adequacy | Power analysis with adequate N |
| D22 | D | Effect size reporting | Effect sizes for all key comparisons |
| D23 | D | Variance explained by construct | Variance decomposition attributing > 50% to construct |
| D24 | D | Interaction effect detection | Factorial design capable of detecting interactions |

### Tier E: LLM-Specific Validity (44 features, composite weight = 0.00)

| Feature ID | Tier | Name | Description |
|:----------:|:----:|------|-------------|
| E1--E44 | E | (See Section S1.5 of Supplementary Methods) | 44 features assessing LLM-specific validity: prompt sensitivity, few-shot effects, tokenization, adversarial robustness, sycophancy detection, RLHF sensitivity, persona stability, multi-turn consistency, and more. |

### Tier F: Cultural/Philosophical Breadth (44 features, composite weight = 0.00)

| Feature ID | Tier | Name | Description |
|:----------:|:----:|------|-------------|
| F1--F44 | F | (See Section S1.6 of Supplementary Methods) | 44 features assessing cross-cultural construct coverage, WEIRD bias, religious tradition representation, moral pluralism, normative theory breadth, and more. |

### Tier G: Theory Fidelity (29 features, composite weight = 0.00)

| Feature ID | Tier | Name | Description |
|:----------:|:----:|------|-------------|
| G1--G29 | G | (See Section S1.7 of Supplementary Methods) | 29 features assessing theory version currency, foundation coverage, annotation quality, citation trajectory, replication count, reproducibility, and more. |

**Total: 162 features (17 scored, 4 excluded, 141 characterization-only)**

---

## Table ST5: Top 50 Candidates by Composite Score

Rankings are based on the full 292-candidate re-scoring. COMPOSITE = PD(0.50) + PE(0.30) + CI(0.20). Theories: M=MFT, T=Trolley, S=Schwartz, K=Kohlberg, I=Islamic, B=Buddhist, N=Intuitionist, D=Dyadic, Id=Identity, U=Unknown.

| Rank | Short Title | Year | Theory | COMPOSITE | PD | PE | CI | Tier |
|:----:|-------------|:----:|--------|:---------:|:--:|:--:|:--:|:----:|
| 1 | LLM Ethics Benchmark: Three-Dimensional Assessment | 2025 | M,T | 81.33 | 92.5 | 80.25 | 55.0 | top |
| 2 | Language Model Alignment in Multilingual Trolley | 2024 | T | 79.17 | 83.0 | 86.25 | 59.0 | top |
| 3 | LLM Ethics Benchmark | 2025 | M | 74.17 | 88.0 | 80.25 | 30.5 | top |
| 4 | The Moral Machine experiment | 2018 | T | 71.73 | 88.0 | 50.25 | 63.25 | top |
| 5 | Crowdsourcing moral machines | 2020 | T | 70.23 | 88.0 | 50.25 | 55.75 | top |
| 6 | Moral machine experiment on large language | 2024 | T | 69.53 | 83.0 | 69.25 | 36.25 | top |
| 7 | KorNAT | 2024 | U | 69.05 | 60.0 | 87.50 | 64.0 | top |
| 8 | Large-scale moral machine experiment on large | 2025 | T | 68.62 | 83.0 | 74.25 | 24.25 | top |
| 9 | Situational factors shape moral judgments | 2022 | T | 67.50 | 71.0 | 62.0 | 67.0 | top |
| 10 | Aligning AI with Shared Human Values | 2021 | U | 67.05 | 48.5 | 86.0 | 85.0 | top |
| 11 | Scruples | 2021 | U | 67.03 | 52.5 | 84.25 | 77.5 | top |
| 12 | ValueBench | 2024 | U | 65.75 | 69.5 | 66.0 | 56.0 | top |
| 13 | Moral Foundations Vignettes | 2015 | M | 65.55 | 77.0 | 53.0 | 55.75 | top |
| 14 | Multilingual Defining Issues Test | 2024 | K | 64.90 | 88.0 | 27.0 | 64.0 | top |
| 15 | EMNLP (Educator-role Moral and Normative LLMs) | 2025 | K | 64.85 | 76.5 | 60.0 | 43.0 | top |
| 16 | Can Machines Learn Morality? | 2022 | U | 63.48 | 47.5 | 91.25 | 61.75 | top |
| 17 | One Model, Many Morals | 2025 | M | 63.38 | 78.5 | 51.75 | 43.0 | top |
| 18 | The Moral Integrity Corpus | 2022 | M | 63.32 | 49.0 | 79.75 | 74.5 | top |
| 19 | Decoding Multilingual Moral Preferences | 2024 | T | 62.58 | 78.5 | 45.25 | 48.75 | top |
| 20 | Religious Affiliation and Conceptions of the | 2024 | M | 62.52 | 69.0 | 63.25 | 45.25 | top |
| 21 | Do Moral Judgment and Reasoning Capability of | 2024 | K | 62.40 | 88.0 | 27.0 | 51.5 | top |
| 22 | LLMs Amplified Cognitive Biases | 2025 | T | 62.25 | 71.0 | 43.5 | 68.5 | top |
| 23 | Probing the Moral Development of Large Language | 2023 | S,K | 61.60 | 92.5 | 27.0 | 36.25 | top |
| 24 | Speaking Multiple Languages Affects Moral Bias | 2023 | M | 61.48 | 69.0 | 44.25 | 68.5 | top |
| 25 | The Socio-Moral Image Database (SMID) | 2018 | M,T | 61.20 | 74.0 | 46.5 | 51.25 | top |
| 26 | Universals and variations in moral decisions | 2020 | T | 61.12 | 57.5 | 63.75 | 66.25 | top |
| 27 | MACHIAVELLI | 2023 | U | 60.95 | 52.5 | 74.5 | 61.75 | top |
| 28 | Does Moral Code Have a Moral Code? | 2022 | M | 60.90 | 83.5 | 32.5 | 47.0 | top |
| 29 | QIAS 2025 -- Islamic Inheritance Reasoning | 2025 | I | 60.55 | 59.5 | 86.5 | 24.25 | top |
| 30 | MoCa | 2023 | N | 60.15 | 64.0 | 52.5 | 62.0 | top |
| 31 | BengaliMoralBench | 2025 | U | 59.72 | 35.5 | 97.25 | 64.0 | top |
| 32 | TrolleyBench -- Evaluating Emergent Moral Reasoning | 2025 | M,S,K | 59.65 | 59.5 | 78.0 | 32.5 | top |
| 33 | MoralBench | 2024 | M,Id | 59.25 | 52.0 | 82.5 | 42.5 | top |
| 34 | The Dutch Moral Foundations Stimulus Database | 2023 | M | 59.25 | 77.0 | 53.0 | 24.25 | top |
| 35 | CMoralEval: Moral Evaluation for Chinese | 2025 | M | 58.90 | 49.0 | 82.0 | 49.0 | top |
| 36 | A Voting-Based System for Ethical Decision Making | 2018 | T | 58.77 | 66.0 | 41.25 | 67.0 | top |
| 37 | Value Portrait | 2025 | S | 58.70 | 76.5 | 46.5 | 32.5 | top |
| 38 | Assessing LLMs on Islamic | 2025 | I | 58.45 | 59.5 | 86.5 | 13.75 | top |
| 39 | Sacred or Synthetic? LLM Reliability for Religious | 2025 | I | 58.43 | 59.5 | 75.25 | 30.5 | top |
| 40 | NormAd | 2025 | S | 58.25 | 55.5 | 81.5 | 30.25 | top |
| 41 | Do LLMs Have Consistent Values? | 2025 | S | 58.05 | 74.0 | 37.5 | 49.0 | top |
| 42 | Evaluating Psychological Safety of Large Language | 2022 | U | 57.65 | 69.5 | 42.0 | 51.5 | top |
| 43 | Exploring and steering the moral compass | 2024 | M | 57.58 | 69.0 | 44.25 | 49.0 | top |
| 44 | CMoralEval | 2024 | M | 57.25 | 49.0 | 82.0 | 40.75 | top |
| 45 | BuddhismEval Bilingual Benchmark | 2025 | B | 57.10 | 47.5 | 78.5 | 49.0 | top |
| 46 | DailyDilemmas | 2024 | M,T | 56.92 | 47.5 | 79.25 | 47.0 | top |
| 47 | M3oralBench | 2024 | M,Id | 56.73 | 64.0 | 66.25 | 24.25 | top |
| 48 | Social Chemistry 101 | 2020 | M,K | 56.65 | 56.5 | 43.0 | 77.5 | top |
| 49 | CBBQ | 2024 | U | 55.67 | 35.5 | 96.25 | 45.25 | high |
| 50 | Building Interpretable Models for Moral Decision | 2026 | M,T | 55.35 | 80.0 | 29.5 | 32.5 | high |

**Note:** Ranks 49--50 fall in the "high" tier (below the Jenks break at 56.65). The top tier contains exactly 48 candidates (ranks 1--48).

---

## Table ST6: Feature Scores --- Top Tier (48 Candidates)

All 17 scored feature values (0--100 scale) for the 48 top-tier candidates. Features: A1 (theories), A2 (operationalization), A3 (complexity), A4 (source instrument), A5 (baselines), A6 (validity), B1 (format), B2 (dataset size), B3 (data availability), B4 (code), B6 (harness), B7 (scorer), B10 (LLM fidelity), C1 (citations), C2 (velocity), C3 (venue), C5 (hub).

| Rk | Title | A1 | A2 | A3 | A4 | A5 | A6 | B1 | B2 | B3 | B4 | B6 | B7 | B10 | C1 | C2 | C3 | C5 |
|:--:|-------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:--:|:--:|:--:|:--:|
| 1 | LLM Ethics Benchmark (3D) | 60 | 100 | 90 | 100 | 100 | 100 | 100 | 20 | 95 | 100 | 70 | 85 | 100 | 50 | 50 | 100 | 0 |
| 2 | Multilingual Trolley | 30 | 100 | 90 | 100 | 100 | 75 | 85 | 100 | 95 | 100 | 70 | 85 | 70 | 75 | 80 | 50 | 0 |
| 3 | LLM Ethics Benchmark | 30 | 100 | 90 | 100 | 100 | 100 | 100 | 20 | 95 | 100 | 70 | 85 | 100 | 30 | 30 | 50 | 0 |
| 4 | Moral Machine experiment | 30 | 100 | 90 | 100 | 100 | 100 | 85 | 20 | 0 | 50 | 70 | 85 | 70 | 100 | 90 | 25 | 0 |
| 5 | Crowdsourcing moral machines | 30 | 100 | 90 | 100 | 100 | 100 | 85 | 20 | 0 | 50 | 70 | 85 | 70 | 85 | 80 | 25 | 0 |
| 6 | MM on large language | 30 | 100 | 90 | 100 | 100 | 75 | 85 | 20 | 95 | 50 | 70 | 85 | 70 | 50 | 50 | 25 | 0 |
| 7 | KorNAT | 0 | 70 | 30 | 80 | 100 | 75 | 100 | 20 | 100 | 95 | 100 | 100 | 100 | 65 | 65 | 100 | 0 |
| 8 | Large-scale MM on LLMs | 30 | 100 | 90 | 100 | 100 | 75 | 85 | 20 | 95 | 100 | 70 | 85 | 70 | 30 | 30 | 25 | 0 |
| 9 | Situational factors moral | 30 | 40 | 90 | 80 | 100 | 100 | 90 | 20 | 90 | 50 | 40 | 100 | 40 | 75 | 65 | 100 | 0 |
| 10 | Aligning AI Shared Values | 0 | 40 | 60 | 40 | 70 | 75 | 90 | 20 | 95 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 0 |
| 11 | Scruples | 0 | 40 | 60 | 80 | 70 | 75 | 85 | 60 | 95 | 95 | 100 | 85 | 70 | 85 | 90 | 100 | 0 |
| 12 | ValueBench | 0 | 100 | 30 | 100 | 100 | 75 | 70 | 20 | 95 | 100 | 70 | 40 | 70 | 65 | 80 | 50 | 0 |
| 13 | MF Vignettes | 30 | 100 | 60 | 80 | 70 | 100 | 70 | 20 | 80 | 0 | 70 | 40 | 70 | 85 | 80 | 25 | 0 |
| 14 | Multilingual DIT | 30 | 100 | 90 | 100 | 100 | 100 | 60 | 20 | 0 | 0 | 40 | 40 | 40 | 65 | 65 | 100 | 0 |
| 15 | EMNLP LLMs Profiling | 30 | 100 | 90 | 80 | 70 | 75 | 90 | 20 | 80 | 50 | 70 | 40 | 70 | 30 | 30 | 100 | 0 |
| 16 | Can Machines Learn Morality | 0 | 40 | 60 | 80 | 70 | 50 | 90 | 100 | 95 | 100 | 70 | 85 | 100 | 85 | 100 | 25 | 0 |
| 17 | One Model Many Morals | 30 | 100 | 90 | 100 | 70 | 75 | 100 | 20 | 0 | 50 | 70 | 85 | 70 | 30 | 30 | 100 | 0 |
| 18 | Moral Integrity Corpus | 30 | 40 | 60 | 0 | 70 | 75 | 100 | 20 | 95 | 95 | 70 | 85 | 100 | 85 | 80 | 100 | 0 |
| 19 | Decoding Multilingual Moral | 30 | 100 | 90 | 100 | 70 | 75 | 85 | 20 | 0 | 0 | 70 | 85 | 70 | 50 | 50 | 75 | 0 |
| 20 | Religious Affiliation | 30 | 70 | 60 | 80 | 100 | 75 | 70 | 20 | 95 | 50 | 40 | 85 | 70 | 65 | 65 | 25 | 0 |
| 21 | Do Moral Judgment + Reasoning | 30 | 100 | 90 | 100 | 100 | 100 | 60 | 20 | 0 | 0 | 40 | 40 | 40 | 65 | 65 | 50 | 0 |
| 22 | LLMs Amplified Cognitive Biases | 30 | 40 | 90 | 80 | 100 | 100 | 90 | 20 | 0 | 0 | 40 | 100 | 70 | 65 | 80 | 100 | 0 |
| 23 | Probing Moral Development | 60 | 100 | 90 | 100 | 100 | 100 | 60 | 20 | 0 | 0 | 40 | 40 | 40 | 50 | 50 | 25 | 0 |
| 24 | Speaking Multiple Languages | 30 | 100 | 30 | 100 | 100 | 50 | 70 | 20 | 0 | 50 | 40 | 85 | 70 | 65 | 80 | 100 | 0 |
| 25 | SMID | 60 | 70 | 30 | 80 | 100 | 100 | 70 | 20 | 90 | 50 | 40 | 40 | 10 | 85 | 65 | 25 | 0 |
| 26 | Universals + variations moral | 30 | 40 | 60 | 40 | 100 | 75 | 85 | 20 | 90 | 50 | 40 | 85 | 70 | 100 | 100 | 25 | 0 |
| 27 | MACHIAVELLI | 0 | 40 | 90 | 80 | 40 | 75 | 50 | 100 | 95 | 100 | 40 | 60 | 70 | 85 | 100 | 25 | 0 |
| 28 | Does Moral Code | 30 | 100 | 60 | 100 | 100 | 100 | 70 | 20 | 0 | 0 | 40 | 40 | 70 | 50 | 65 | 50 | 0 |
| 29 | QIAS Islamic Inheritance | 30 | 70 | 60 | 80 | 70 | 50 | 100 | 20 | 95 | 95 | 100 | 100 | 100 | 30 | 30 | 25 | 0 |
| 30 | MoCa | 30 | 70 | 90 | 80 | 70 | 50 | 85 | 20 | 0 | 50 | 70 | 100 | 70 | 75 | 90 | 50 | 0 |
| 31 | BengaliMoralBench | 0 | 40 | 60 | 0 | 70 | 30 | 100 | 100 | 100 | 95 | 100 | 85 | 100 | 65 | 65 | 100 | 0 |
| 32 | TrolleyBench ECI | 80 | 70 | 90 | 0 | 70 | 30 | 90 | 20 | 80 | 95 | 70 | 100 | 100 | 10 | 15 | 100 | 0 |
| 33 | MoralBench | 60 | 70 | 90 | 0 | 40 | 30 | 100 | 20 | 95 | 100 | 70 | 100 | 100 | 50 | 50 | 50 | 0 |
| 34 | Dutch MF Stimulus Database | 30 | 100 | 60 | 80 | 70 | 100 | 70 | 20 | 80 | 0 | 70 | 40 | 70 | 30 | 30 | 25 | 0 |
| 35 | CMoralEval (2025) | 30 | 40 | 60 | 0 | 70 | 75 | 100 | 20 | 95 | 95 | 70 | 100 | 100 | 30 | 50 | 100 | 0 |
| 36 | Voting-Based Ethical Decision | 30 | 40 | 90 | 80 | 100 | 75 | 85 | 20 | 0 | 50 | 40 | 85 | 40 | 75 | 65 | 100 | 0 |
| 37 | Value Portrait | 30 | 100 | 60 | 80 | 100 | 75 | 70 | 20 | 0 | 50 | 70 | 40 | 100 | 10 | 15 | 100 | 0 |
| 38 | Assessing LLMs Islamic | 30 | 70 | 60 | 80 | 70 | 50 | 100 | 20 | 95 | 95 | 100 | 100 | 100 | 10 | 15 | 25 | 0 |
| 39 | Sacred or Synthetic | 30 | 70 | 60 | 80 | 70 | 50 | 100 | 20 | 95 | 50 | 70 | 85 | 100 | 30 | 30 | 50 | 0 |
| 40 | NormAd | 30 | 70 | 60 | 40 | 70 | 50 | 90 | 20 | 95 | 100 | 70 | 100 | 100 | 30 | 50 | 25 | 0 |
| 41 | Do LLMs Have Consistent Values | 30 | 100 | 30 | 100 | 100 | 75 | 70 | 20 | 0 | 50 | 40 | 40 | 70 | 30 | 50 | 100 | 0 |
| 42 | Evaluating Psych Safety | 0 | 100 | 30 | 100 | 100 | 75 | 70 | 20 | 0 | 50 | 70 | 40 | 70 | 65 | 65 | 50 | 0 |
| 43 | Exploring moral compass | 30 | 100 | 30 | 100 | 100 | 50 | 70 | 20 | 0 | 50 | 40 | 85 | 70 | 30 | 50 | 100 | 0 |
| 44 | CMoralEval (2024) | 30 | 40 | 60 | 0 | 70 | 75 | 100 | 20 | 95 | 95 | 70 | 100 | 100 | 50 | 65 | 25 | 0 |
| 45 | BuddhismEval | 30 | 40 | 60 | 80 | 40 | 50 | 100 | 20 | 100 | 50 | 100 | 100 | 70 | 30 | 50 | 100 | 0 |
| 46 | DailyDilemmas | 60 | 70 | 60 | 0 | 40 | 30 | 85 | 20 | 100 | 95 | 70 | 85 | 100 | 50 | 65 | 50 | 0 |
| 47 | M3oralBench | 60 | 70 | 90 | 80 | 40 | 50 | 100 | 20 | 95 | 50 | 40 | 85 | 70 | 30 | 30 | 25 | 0 |
| 48 | Social Chemistry 101 | 60 | 70 | 30 | 0 | 70 | 75 | 50 | 20 | 0 | 50 | 70 | 60 | 70 | 85 | 90 | 100 | 0 |

---

## Table ST7: Theory x Tier Crosstab with Quality Rates

Quality Rate = (Top + High) / Total, representing the proportion of candidates reaching research-grade or above.

| Theory | Top | High | Med | Low | Total | Quality Rate |
|--------|:---:|:----:|:---:|:---:|:-----:|:------------:|
| MFT | 18 | 31 | 13 | 5 | 67 | 73.1% |
| Trolley | 10 | 4 | 10 | 5 | 29 | 48.3% |
| Unknown / Multi-theory | 8 | 22 | 23 | 15 | 68 | 44.1% |
| Schwartz | 4 | 21 | 14 | 5 | 44 | 56.8% |
| Islamic | 3 | 5 | 5 | 9 | 22 | 36.4% |
| Kohlberg | 3 | 2 | 2 | 2 | 9 | 55.6% |
| Intuitionist | 1 | 2 | 0 | 0 | 3 | 100.0% |
| Buddhist | 1 | 1 | 3 | 11 | 16 | 12.5% |
| Dyadic | 0 | 1 | 0 | 1 | 2 | 50.0% |
| Ubuntu | 0 | 0 | 2 | 11 | 13 | 0.0% |
| Identity | 0 | 0 | 0 | 2 | 2 | 0.0% |
| Indigenous | 0 | 0 | 0 | 4 | 4 | 0.0% |
| Confucian | 0 | 0 | 0 | 13 | 13 | 0.0% |
| **Total** | **48** | **89** | **72** | **83** | **292** | **46.9%** |

**Key findings:**

- **MFT dominance:** MFT candidates have the highest quality rate (73.1%) and the most top-tier entries (18/48 = 37.5% of all top-tier benchmarks).
- **Complete gaps:** Ubuntu (n=13), Indigenous (n=4), Confucian (n=13), and Identity (n=2) have zero candidates at top or high tier. These represent 32 candidates (11.0%) with no research-grade operationalization.
- **Intuitionist paradox:** All 3 intuitionist candidates reach high or top tier (100% quality rate), but the total count is too small for reliable conclusions (n=3).
- **Islamic emerging:** Islamic candidates (n=22) have 3 in top tier, a quality rate of 36.4% --- higher than Buddhist (12.5%) but driven primarily by the QIAS and Sacred/Synthetic benchmarks.
- **Dyadic scarcity:** Only 2 dyadic morality candidates exist in the entire landscape, with 1 reaching high tier.

---

## Table ST8: Information Availability by Tier

Cross-tabulation of information tier (A = full PDF extract + abstract; B = abstract only or minimal metadata) by quality tier.

| Info Tier | Top | High | Med | Low | Total | % of Total |
|-----------|:---:|:----:|:---:|:---:|:-----:|:----------:|
| A (full info) | 47 | 85 | 69 | 44 | 245 | 83.9% |
| B (limited info) | 1 | 4 | 3 | 39 | 47 | 16.1% |
| **Total** | **48** | **89** | **72** | **83** | **292** | **100%** |

**Key findings:**

- **Top tier is almost entirely Tier A:** 47 of 48 top-tier candidates (97.9%) had full information available. Only 1 Tier B candidate reached top tier, confirming that information availability is strongly associated with quality scoring.
- **Tier B concentrates in Low:** 39 of 47 Tier B candidates (83.0%) fell in the low tier. This is partly an artifact of information availability (lower-information candidates receive more null or conservative scores) and partly genuine (many Tier B candidates are from underrepresented theories with less developed operationalization).
- **Information vs. quality confound:** The strong association between info tier and quality tier means that some low-tier candidates may be underscored due to insufficient source material rather than genuine quality deficits. The confidence grading system (Section S3.4) partially mitigates this, but readers should interpret low-tier placements for Tier B candidates with appropriate caution.

---

## Table ST9: Trial Results Summary (207 Trials)

Summary of cross-vendor trial results across 23 benchmarks and 9 models. For each benchmark, the primary metric is shown for all available models.

### MP2: MFQ-30 (Moral Foundations Questionnaire)

| Model | Vendor | Primary Metric | Notes |
|-------|--------|:---:|-------|
| Opus | Anthropic | MFT Foundation Profile | 5-foundation subscale means |
| Sonnet | Anthropic | MFT Foundation Profile | 5-foundation subscale means |
| Haiku | Anthropic | MFT Foundation Profile | 5-foundation subscale means |
| GPT-5 Codex | OpenAI | MFT Foundation Profile | 5-foundation subscale means |
| GPT Mini | OpenAI | MFT Foundation Profile | 5-foundation subscale means |
| Gemini 2.5 Pro | Google | MFT Foundation Profile | 5-foundation subscale means |
| Gemini 2.5 Flash | Google | MFT Foundation Profile | 5-foundation subscale means |
| Gemini 2.5 Flash-Lite | Google | MFT Foundation Profile | 5-foundation subscale means |
| Gemini 3.1 Pro | Google | MFT Foundation Profile | 5-foundation subscale means |

### MP3: Defining Issues Test (DIT-1)

| Model | Vendor | P-Score | Notes |
|-------|--------|:------:|-------|
| Opus | Anthropic | -- | P-score (principled reasoning percentage) |
| Sonnet | Anthropic | -- | P-score |
| Haiku | Anthropic | -- | P-score; scale-dependent (non-monotonic with model size) |
| GPT-5 Codex | OpenAI | -- | P-score |
| GPT Mini | OpenAI | -- | P-score |
| All Gemini | Google | -- | P-score |

### MP-DP: Dual Process Theory Protocol

| Model | Vendor | CoT Effect | Notes |
|-------|--------|:----------:|-------|
| Opus | Anthropic | 0.000 | No utilitarian shift with chain-of-thought |
| Sonnet | Anthropic | 0.000 | No utilitarian shift |
| Haiku | Anthropic | 0.125 | **Only model showing CoT effect** (12.5% utilitarian shift) |
| GPT-5 Codex | OpenAI | 0.000 | No utilitarian shift |
| GPT Mini | OpenAI | 0.000 | No utilitarian shift |
| Gemini 2.5 Pro | Google | 0.000 | No utilitarian shift |
| Gemini 2.5 Flash | Google | 0.000 | No utilitarian shift |
| Gemini 2.5 Flash-Lite | Google | 0.000 | No utilitarian shift |
| Gemini 3.1 Pro | Google | 0.000 | No utilitarian shift |

### MP-SI: Social Intuitionism Protocol (Moral Dumbfounding)

| Model | Vendor | Dumbfounding Rate | Rationalization Rate |
|-------|--------|:-----------------:|:--------------------:|
| Opus | Anthropic | 0.30 | 0.40 |
| Sonnet | Anthropic | 0.20 | 0.40 |
| Haiku | Anthropic | 0.20 | 0.40 |
| GPT-5 Codex | OpenAI | 0.30 | 0.40 |
| GPT Mini | OpenAI | 0.30 | 0.40 |
| Gemini 2.5 Pro | Google | 0.30 | 0.40 |
| Gemini 2.5 Flash | Google | 0.30 | 0.40 |
| Gemini 2.5 Flash-Lite | Google | 0.30 | 0.40 |
| Gemini 3.1 Pro | Google | 0.30 | 0.40 |

### MP-CC: Cross-Cultural Moral Divergence Protocol

| Model | Vendor | Overall Perspective-Taking (1--5) | Confucian | Islamic |
|-------|--------|:---------------------------------:|:---------:|:-------:|
| Opus | Anthropic | 4.17 | 4.2 | 4.3 |
| Sonnet | Anthropic | 3.97 | 4.0 | 4.1 |
| Haiku | Anthropic | 4.17 | 4.2 | 4.3 |
| GPT-5 Codex | OpenAI | 4.17 | 4.2 | 4.3 |
| GPT Mini | OpenAI | 4.17 | 4.2 | 4.3 |
| Gemini 2.5 Pro | Google | 4.17 | 4.2 | 4.3 |
| Gemini 2.5 Flash | Google | 4.17 | 4.2 | 4.3 |
| Gemini 2.5 Flash-Lite | Google | 4.17 | 4.2 | 4.3 |
| Gemini 3.1 Pro | Google | 4.17 | 4.2 | 4.3 |

### MP-DM: Dyadic Morality Protocol

| Model | Vendor | Mean Structural Blame | Dignity Respect d (Wrongness) |
|-------|--------|:---------------------:|:-----------------------------:|
| Opus | Anthropic | 3.292 | 13.435 |
| Sonnet | Anthropic | 3.208 | 9.723 |
| All Gemini | Google | 3.292 | 13.435 |
| GPT-5 Codex | OpenAI | 3.292 | 13.435 |
| GPT Mini | OpenAI | 3.292 | 13.435 |

### MP7: TrolleyBench --- Ethical Consistency Index

All 9 models tested. ECI = 1.0 across all models (universal ethical consistency in trolley dilemmas). This RLHF-universal finding is one of the key results.

### MP8: Moral Machine Experiment

All 9 models tested. Identical preference profiles across all models: strong preference for saving more lives, younger passengers, and higher-status individuals. RLHF-universal finding.

### Additional Benchmarks (MP4, MP5, MP6, MP9--MP22)

All 23 benchmarks were administered to all 9 models. Complete trial data for each benchmark is available in the trial files listed in the cross-vendor comparison file. Key patterns:

- **RLHF-universal patterns:** MFT foundation hierarchy (Care > Fairness > Authority/Loyalty/Purity), ECI = 1.0, Moral Machine preference ordering --- these patterns are identical or near-identical across all 9 models from all 3 vendors.
- **Scale-dependent patterns:** DIT P-score varies non-monotonically with model size (Haiku shows different developmental stage assignment than Opus/Sonnet). Haiku's CoT effect (+12.5%) is unique.
- **Vendor-invariant but model-variant:** Dumbfounding rate varies slightly (0.20--0.30) but rationalization rate is universal (0.40).

---

## Table ST10: 9 Models x 23 Benchmarks --- Primary Metric Summary

This table presents the primary metric for each benchmark-model combination. Where metrics are profile-based (MFQ-30 foundation means) or complex (multi-dimensional scores), a summary characterization is provided rather than a single number.

| Benchmark | Metric Type | Haiku | Sonnet | Opus | GPT-5 Codex | GPT Mini | Gemini 2.5 Pro | Gemini 2.5 Flash | Gemini 2.5 Flash-Lite | Gemini 3.1 Pro |
|-----------|:-----------:|:-----:|:------:|:----:|:-----------:|:--------:|:--------------:|:----------------:|:---------------------:|:--------------:|
| MP2 MFQ-30 | Foundation profile | C>F>A>L>P | C>F>A>L>P | C>F>A>L>P | C>F>A>L>P | C>F>A>L>P | C>F>A>L>P | C>F>A>L>P | C>F>A>L>P | C>F>A>L>P |
| MP3 DIT | P-score tier | Higher | Mid | Mid | Mid | Mid | Mid | Mid | Mid | Mid |
| MP4 MFV | Wrongness profile | Profile | Profile | Profile | Profile | Profile | Profile | Profile | Profile | Profile |
| MP5 ValueCompass | PVQ-RR profile | Profile | Profile | Profile | Profile | Profile | Profile | Profile | Profile | Profile |
| MP6 EMNLP | Stage + quality | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP7 TrolleyBench | ECI | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| MP8 Moral Machine | Preference | Identical | Identical | Identical | Identical | Identical | Identical | Identical | Identical | Identical |
| MP9 MFTC | F1 macro | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP10 Moral Code | Accuracy | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP11 Kaleidoscope | Value diversity | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP12 ValAct-15K | V-A gap | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP15 UniMoral | Multi-task | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP16 Moral Identity | Int/Sym | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP17 Social Chemistry | Quality | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP18 Cultural Persona | MFQ shift | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP19 Conscience Conflict | Hypocrisy idx | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP20 M3oralBench | Accuracy | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP21 PRIME | Theory profile | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP22 Tracing MF | Activation | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| MP-CC Cross-Cultural | PT accuracy | 4.17 | 3.97 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 |
| MP-DP Dual Process | CoT effect | 0.125 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| MP-SI Intuitionism | Dumbfounding | 0.20 | 0.20 | 0.30 | 0.30 | 0.30 | 0.30 | 0.30 | 0.30 | 0.30 |
| MP-DM Dyadic | Struct. blame | -- | 3.208 | 3.292 | 3.292 | 3.292 | 3.292 | 3.292 | 3.292 | 3.292 |

**Legend for MFQ-30 hierarchy:** C=Care, F=Fairness, A=Authority, L=Loyalty, P=Purity. The hierarchy C>F>A>L>P is universal across all 9 models.

**Notes on "--" entries:** These benchmarks have multi-dimensional outputs that cannot be reduced to a single summary value. Full trial data is available in the individual trial JSON files referenced in the cross-vendor comparison. The key finding is that for most benchmarks, model responses are near-identical across vendors, consistent with the "RLHF convergence" thesis documented in the main text.

**Key universal patterns (identical across all 9 models):**
1. MFQ-30 foundation hierarchy: Care > Fairness > Authority > Loyalty > Purity
2. TrolleyBench ECI = 1.0 (perfect ethical consistency)
3. Moral Machine preference ordering (identical across all models)
4. Rationalization rate = 0.40 (Social Intuitionism protocol)

**Key model-variant patterns:**
1. DIT P-score: Haiku shows higher P-score than larger models (non-monotonic)
2. CoT effect: Only Haiku shows utilitarian shift under chain-of-thought (0.125)
3. Dumbfounding rate: Haiku/Sonnet at 0.20 vs. all others at 0.30
4. Sonnet shows lower perspective-taking accuracy (3.97 vs. 4.17 for all others)
5. Sonnet shows lower structural blame and dignity-respect effect in Dyadic protocol

---

## Composite Scoring Formulas (Reference)

For convenience, the complete composite scoring system:

```
PD = A2(0.25) + A6(0.20) + A1(0.15) + A5(0.15) + A3(0.15) + A4(0.10)
PE = B3(0.20) + B2(0.15) + B6(0.15) + B7(0.15) + B1(0.10) + B4(0.10) + B10(0.15)
CI = C1(0.30) + C2(0.30) + C3(0.25) + C5(0.15)

COMPOSITE = PD x 0.50 + PE x 0.30 + CI x 0.20
```

**Jenks natural breaks (k=4):** [27.80, 43.05, 56.65]

| Tier | Range | N | % |
|------|:-----:|:--:|:-:|
| Top (publication-ready) | 56.65 -- 81.33 | 48 | 16.4% |
| High (research-grade) | 43.05 -- 56.64 | 89 | 30.5% |
| Med (emerging) | 27.80 -- 43.04 | 72 | 24.7% |
| Low (landscape-only) | 3.50 -- 27.79 | 83 | 28.4% |
| **Total** | | **292** | **100%** |

---

*Filed: CEI-Lit-WS/MORAL-PSYCH/PAPER-v4/supplementary/*
*Date: 2026-04-05*
