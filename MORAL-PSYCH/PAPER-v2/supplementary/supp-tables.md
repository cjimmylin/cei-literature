# Supplementary Tables

## Supplementary Table 1 (ST1). 28-Feature Core Framework Definition

The 28-feature characterization framework organizes benchmark quality into three tiers: Psychological Depth (Tier A, 6 features), Practical Ease (Tier B, 7 features), and Citation Impact (Tier C, 4 features). Five features originally defined in the framework (B5, B7--B9, C4) were excluded from scoring due to incomplete availability across candidates (see Section 3.3). The 17 scored features are listed below with their normalization scales and composite weights.

### Tier A --- Psychological Depth (6 features, composite weight = 0.50)

| Feature ID | Feature Name | Description | Scale | Weight in Tier |
|:----------:|:-------------|:------------|:------|:--------------:|
| A1 | Theories engaged | Number of distinct moral psychology theories operationalized by the benchmark | 0 theories = 0; 1 = 30; 2 = 60; 3 = 80; 4+ = 100 | 0.15 |
| A2 | Construct operationalization | Degree to which the benchmark faithfully operationalizes a theoretical construct | Validated instrument = 100; Theory-derived = 70; Theory-inspired = 40; Keyword-only = 10 | 0.25 |
| A3 | Measurement target | Specificity of the psychological construct being measured | Default 70; adjusted per expert assessment | 0.15 |
| A4 | Source instrument provenance | Whether the benchmark derives from a previously validated psychometric instrument | Validated = 100; Original = 80; None = 0 | 0.10 |
| A5 | Human baseline availability | Availability of human comparison data for interpreting LLM results | Published population norms = 100; Paper-specific study = 70; Partial = 40; None = 0 | 0.15 |
| A6 | Construct validity evidence | Strength of psychometric validity evidence for the benchmark | 5 (multi-study validated) = 100; 4 (single-study validated) = 75; 3 (adapts validated instrument) = 50; 2 (theory-inspired, no validation) = 30; 1 (keyword-level only) = 10 | 0.20 |

### Tier B --- Practical Ease (7 features, composite weight = 0.30)

| Feature ID | Feature Name | Description | Scale | Weight in Tier |
|:----------:|:-------------|:------------|:------|:--------------:|
| B1 | Task format | Response format required by the benchmark | MCQ = 100; Binary = 90; Forced-choice = 85; Likert = 70; Mixed = 50; Free-text = 50 | 0.10 |
| B2 | Dataset size | Number of items in the benchmark | Log-scaled: <50 = 20; 200 = 40; 1K = 60; 5K = 75; 20K = 85; >20K = 100 | 0.15 |
| B3 | Data availability | Accessibility of benchmark data | HuggingFace = 100; GitHub = 95; OSF = 90; Anonymous link = 60; Paper only = 30 | 0.20 |
| B4 | Code availability | Availability of implementation code | Full pipeline = 100; Partial = 50; None = 0 | 0.10 |
| B6 | Harness tier | Integration readiness with standard LLM evaluation harnesses (lm-eval, Inspect, LightEval, HELM, OpenAI Evals) | Tier 1 (already integrated) = 100; Tier 2 (straightforward port) = 70; Custom required = 40 | 0.15 |
| B7 | Scorer complexity | Complexity of the scoring procedure | Exact match = 100; Log-likelihood = 80; Model-graded = 60; Psychometric = 40 | 0.15 |
| B10 | LLM administration fidelity | How faithfully the instrument can be administered to an LLM compared to a human participant | Direct = 100; Minor adaptation = 70; Major adaptation = 40; Paradigm change = 10 | 0.15 |

### Tier C --- Citation Impact (4 features, composite weight = 0.20)

| Feature ID | Feature Name | Description | Scale | Weight in Tier |
|:----------:|:-------------|:------------|:------|:--------------:|
| C1 | Raw citation count | Total citations from Semantic Scholar | Log-scaled: <5 = 10; 50 = 50; 200 = 75; >500 = 100 | 0.30 |
| C2 | Age-normalized citation rate | Citations per year since publication | Log-scaled from citations/year | 0.30 |
| C3 | Venue tier | Quality tier of publication venue | Tier 1 (Nature, ACL, NeurIPS, ICLR) = 100; Tier 2 (CACM, RSOpen, SPPS) = 75; Tier 3 = 50; Tier 4 (arXiv, workshop) = 25 | 0.25 |
| C5 | Hub/leaderboard presence | Presence on benchmark aggregation platforms | Major hub (HuggingFace, PapersWithCode) = 100; GitHub = 50; None = 0 | 0.15 |

### Composite Scoring Formula

```
PD = A2(0.25) + A6(0.20) + A1(0.15) + A5(0.15) + A3(0.15) + A4(0.10)
PE = B3(0.20) + B2(0.15) + B6(0.15) + B7(0.15) + B1(0.10) + B4(0.10) + B10(0.15)
CI = C1(0.30) + C2(0.30) + C3(0.25) + C5(0.15)

COMPOSITE = PD x 0.50 + PE x 0.30 + CI x 0.20
```

---

## Supplementary Table 2 (ST2). Top-15 Benchmark Selection: Full Scores

The final top-15 benchmarks were selected through a five-step algorithm: (1) hard gates (PD >= 40, data publicly available), (2) deduplication, (3) theory caps (Trolley <= 3, MFT <= 4), (4) greedy selection in descending composite order, and (5) diversity fills (>= 2 Schwartz, >= 1 Kohlberg, >= 1 minority theory). All scores are on 0--100 normalized scales.

| Rank | Benchmark | Year | PD | PE | CI | Composite | Theories | Format | A6 |
|:----:|:----------|:----:|:--:|:--:|:--:|:---------:|:---------|:-------|:--:|
| 1 | Moral Machine (Awad et al., 2018) | 2018 | 75.5 | 74.0 | 92.5 | 78.45 | Trolley | Forced-choice | 5 |
| 2 | Moral Machine on LLMs (Takemoto, 2024) | 2024 | 72.5 | 69.5 | 64.0 | 69.90 | Trolley | Forced-choice | 4 |
| 3 | Crowdsourcing Moral Machines (Awad et al., 2020) | 2020 | 72.5 | 67.4 | 67.0 | 69.87 | Trolley | Forced-choice | 4 |
| 4 | Moral Foundations Twitter Corpus (Hoover et al., 2020) | 2020 | 68.0 | 66.0 | 71.5 | 68.10 | MFT | Multi-label | 4 |
| 5 | Does Moral Code Have a Moral Code? (Fraser et al., 2022) | 2022 | 72.0 | 59.3 | 62.5 | 66.29 | MFT, Schwartz | Binary + MCQ | 3 |
| 6 | Moral Foundations of LLMs (Abdulhai et al., 2024) | 2024 | 85.0 | 62.8 | 12.5 | 63.84 | MFT | Likert | 5 |
| 7 | Differences in Moral Foundations of LLMs (Kirgis, 2024) | 2024 | 80.0 | 65.8 | 20.0 | 63.74 | MFT | Likert | 4 |
| 8 | Value Kaleidoscope (Sorensen et al., 2024) | 2024 | 55.5 | 69.5 | 65.0 | 61.60 | Schwartz | Free-text + MCQ | 3 |
| 9 | Multilingual DIT (Khandelwal et al., 2024) | 2024 | 80.0 | 54.1 | 25.0 | 61.23 | Kohlberg | Scenario rating + ranking | 4 |
| 10 | ValAct-15k (Huang et al., 2026) | 2026 | 75.5 | 61.8 | 12.5 | 58.80 | Schwartz | MCQ | 4 |
| 11 | ValueCompass (Shen et al., 2025) | 2025 | 72.5 | 54.2 | 12.5 | 55.00 | Schwartz, Dyadic | Likert | 4 |
| 12 | CVC (Wu et al., 2025) | 2025 | 51.0 | 73.7 | 26.0 | 52.81 | -- | MCQ + scenario | 3 |
| 13 | TrolleyBench (Zhu, 2025) | 2025 | 56.0 | 59.0 | 32.5 | 52.20 | Kohlberg, Trolley | Binary | 2 |
| 14 | BehaviorBench (Huang et al., 2025) | 2025 | 63.0 | 55.8 | 12.5 | 50.75 | Kohlberg, MFT | Mixed | 3 |
| 15 | EMNLP (Jiang et al., 2025) | 2025 | 61.0 | 45.5 | 12.5 | 46.60 | Kohlberg | Mixed | 3 |

### Score Component Breakdown

| Rank | Benchmark | A1 | A2 | A3 | A4 | A5 | A6 | B1 | B2 | B3 | B4 | B6 | B10 | C1 | C2 | C3 | C5 |
|:----:|:----------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:--:|:--:|:--:|:--:|
| 1 | Moral Machine | 30 | 70 | 70 | 80 | 100 | 100 | 85 | 100 | 70 | 80 | 45 | 100 | 100 | 100 | 100 | 50 |
| 2 | MM on LLMs | 30 | 70 | 70 | 100 | 100 | 75 | 85 | 100 | 70 | 80 | 45 | 70 | 65 | 65 | 70 | 50 |
| 3 | Crowdsourcing MM | 30 | 70 | 70 | 100 | 100 | 75 | 85 | 100 | 70 | 80 | 23 | 100 | 65 | 50 | 70 | 100 |
| 4 | MFTC | 30 | 70 | 70 | 100 | 70 | 75 | 40 | 100 | 90 | 80 | 50 | 40 | 75 | 80 | 70 | 50 |
| 5 | Fraser et al. | 60 | 70 | 70 | 100 | 100 | 50 | 100 | 40 | 70 | 80 | 36 | 70 | 50 | 50 | 70 | 100 |
| 6 | Abdulhai et al. | 30 | 100 | 70 | 100 | 100 | 100 | 70 | 20 | 95 | 80 | 36 | 100 | 0 | 0 | 20 | 50 |
| 7 | Kirgis | 30 | 100 | 70 | 100 | 100 | 75 | 70 | 40 | 95 | 80 | 36 | 100 | 10 | 15 | 20 | 50 |
| 8 | Value Kaleidoscope | 30 | 40 | 70 | 100 | 70 | 50 | 100 | 100 | 100 | 80 | 50 | 10 | 75 | 80 | 20 | 90 |
| 9 | Multilingual DIT | 30 | 100 | 70 | 100 | 100 | 75 | 60 | 20 | 70 | 80 | 27 | 100 | 0 | 0 | 100 | 0 |
| 10 | ValAct-15k | 30 | 100 | 70 | 100 | 70 | 75 | 100 | 85 | 70 | 10 | 30 | 100 | 0 | 0 | 20 | 0 |
| 11 | ValueCompass | 60 | 70 | 70 | 100 | 70 | 75 | 70 | 75 | 70 | 10 | 30 | 70 | 0 | 0 | 20 | 0 |
| 12 | CVC | 0 | 40 | 70 | 100 | 70 | 50 | 100 | 100 | 100 | 80 | 64 | 10 | 10 | 15 | 20 | 90 |
| 13 | TrolleyBench | 60 | 40 | 70 | 100 | 70 | 30 | 90 | 40 | 60 | 80 | 45 | 70 | 0 | 0 | 100 | 50 |
| 14 | BehaviorBench | 60 | 70 | 70 | 100 | 40 | 50 | 50 | 85 | 95 | 80 | 32 | 10 | 0 | 0 | 20 | 50 |
| 15 | EMNLP | 30 | 70 | 70 | 80 | 70 | 50 | 50 | 40 | 70 | 10 | 30 | 70 | 0 | 0 | 20 | 0 |

### Theory Coverage in Top-15

| Theory | Count | Benchmarks |
|:-------|:-----:|:-----------|
| MFT | 5 | Fraser et al., Abdulhai et al., Kirgis, MFTC, BehaviorBench |
| Trolley | 4 | Moral Machine, MM on LLMs, Crowdsourcing MM, TrolleyBench |
| Schwartz | 4 | Fraser et al., Value Kaleidoscope, ValAct-15k, ValueCompass |
| Kohlberg | 4 | Multilingual DIT, TrolleyBench, BehaviorBench, EMNLP |
| Dyadic | 1 | ValueCompass |

---

## Supplementary Table 3 (ST3). Keyword Scorer Expansion: New Patterns

During the benchmark survey (Section 3.5), we identified critical blind spots in the vault's moral psychology keyword scorer. Below we enumerate all regex patterns added during the expansion, organized by theory. Detection counts are before and after re-scoring all 2,099 papers in the vault (threshold: score >= 50).

### Summary of Expansion Impact

| Theory | Papers Detected Before | Papers Detected After | Delta | New Patterns Added |
|:-------|:----------------------:|:---------------------:|:-----:|:------------------:|
| MFT | 68 | 101 | +33 | 0 (existing patterns sufficient; gains from re-scoring with improved engine) |
| Schwartz | 52 | 69 | +17 | 0 (existing patterns sufficient; gains from re-scoring) |
| Trolley | 36 | 58 | +22 | 0 (existing patterns sufficient; gains from re-scoring) |
| Kohlberg | 19 | 35 | +16 | 0 (existing patterns sufficient; gains from re-scoring) |
| Dual Process | 0 | 9 | +9 | 18 (9 strong + 9 medium) |
| Social Intuitionism | 1 | 18 | +17 | 14 (7 strong + 7 medium) |
| Dyadic Morality | 3 | 7 | +4 | 11 (4 strong + 7 medium) |
| Moral Identity | 7 | 12 | +5 | 0 (existing patterns sufficient) |
| **Total** | **186** | **309** | **+123** | **43** |

### Dual Process Theory --- New Patterns (18 patterns)

Prior to expansion, the vault's keyword scorer contained zero patterns for Dual Process Theory. All patterns below are new additions.

| Pattern (regex) | Detection Type | Tier | Rationale |
|:----------------|:---------------|:----:|:----------|
| `\bdual process\b(?=.*\bmoral\b)` | Strong | S | Greene's core framework label in moral context |
| `\bjoshua greene\b` | Strong | S | Primary theorist attribution |
| `\butilitarian vs deontological processing\b` | Strong | S | Signature dual-process prediction |
| `\bsystem 1.*system 2\b` | Strong | S | Kahneman framing commonly applied to moral cognition |
| `\bsystem 2.*system 1\b` | Strong | S | Reverse-order mention of dual systems |
| `\butilitarian vs\.? deontological\b(?=.*\b(?:judg\|reason\|dilemma\|moral)\b)` | Strong | S | Utilitarian-deontological contrast in moral judgment context |
| `\bcognitive load\b(?=.*\bmoral\b)` | Strong | S | Key experimental manipulation in dual-process moral studies |
| `\bpersonal force\b(?=.*\b(?:moral\|dilemma)\b)` | Strong | S | Greene's personal/impersonal distinction |
| `\bpersonal vs\.? impersonal\b(?=.*\bdilemma\b)` | Strong | S | Personal vs. impersonal dilemma framing |
| `\bgreene\b(?=.*\bmoral\b)` | Strong | S | Theorist surname in moral context |
| `\baffect\b(?=.*\bcognition\b)(?=.*\bmoral\b)` | Strong | S | Affect-cognition interaction in moral judgment |
| `\bresponse time\b(?=.*\bmoral\b)` | Strong | S | Response latency as process indicator |
| `\bdual process\b` | Medium | M | Dual-process mention without moral context |
| `\bfast and slow\b(?=.*\bmoral\b)` | Medium | M | Kahneman terminology in moral context |
| `\bautomatic.*deliberat\w*\b(?=.*\bmoral\b)` | Medium | M | Automatic vs. deliberative in moral context |
| `\bautomatic\b(?=.*\bmoral\b)(?=.*\b(?:judg\|reason\|process)\b)` | Medium | M | Automatic moral judgment/reasoning |
| `\bdeliberat\w+\b(?=.*\bmoral\b)(?=.*\b(?:judg\|reason\|process)\b)` | Medium | M | Deliberative moral reasoning |
| `\bsystem 1\b(?=.*\b(?:moral\|intuiti\|dilemma)\b)` | Medium | M | System 1 in moral/intuitive context |
| `\bsystem 2\b(?=.*\b(?:moral\|deliberat\|dilemma)\b)` | Medium | M | System 2 in deliberative context |
| `\beffortful\b(?=.*\bmoral\b)` | Medium | M | Effortful moral processing |
| `\bemotional response\b(?=.*\b(?:utilitarian\|deontological)\b)` | Medium | M | Emotional response in utilitarian/deontological context |

**False-positive suppression patterns:**

| Pattern (regex) | Tier | Rationale |
|:----------------|:----:|:----------|
| `\bdual process\b(?=.*\b(?:cognitive science\|memory\|attention\|perception)\b)(?!.*\bmoral\b)` | FP | Dual-process in non-moral cognitive science |
| `\bfast and slow\b(?!.*\bmoral\b)` | FP | Kahneman without moral context |
| `\bautomatic\b(?!.*\b(?:moral\|ethic\|dilemma\|utilitarian\|deontological)\b)` | FP | Generic "automatic" without ethical context |

### Social Intuitionism --- New Patterns (14 patterns)

Prior to expansion, the vault contained 3 patterns for Social Intuitionism. All patterns below are new additions to the existing base.

| Pattern (regex) | Detection Type | Tier | Rationale |
|:----------------|:---------------|:----:|:----------|
| `\bhaidt\b(?=.*\b(?:intuit\|moral\|foundation\|dumbfound)\b)` | Strong | S | Haidt in intuitionist/moral context |
| `\bpost[- ]hoc rationali[sz]\w+\b(?=.*\bmoral\b)` | Strong | S | Post-hoc rationalization of moral judgments |
| `\bgut feeling\b(?=.*\bmoral\b)` | Strong | S | Intuitive moral "gut feelings" |
| `\bemotion[- ]first\b(?=.*\bmoral\b)` | Strong | S | Emotion-first model of moral judgment |
| `\bmoral heuristic\b` | Strong | S | Moral heuristics (Sunstein, Gigerenzer) |
| `\bmoral sentiment\b(?=.*\b(?:judgment\|intuiti\|reason)\b)` | Strong | S | Moral sentiment in judgment context |
| `\bintuitive judgment\b(?=.*\bmoral\b)` | Medium | M | Intuitive moral judgment |
| `\bmoral sentiment\b` | Medium | M | Moral sentiment (general) |
| `\bhumean\b(?=.*\bmoral\b)` | Medium | M | Humean moral philosophy (reason as slave of passions) |
| `\bsentimentalism\b(?=.*\b(?:moral\|ethic)\b)` | Medium | M | Moral sentimentalism tradition |
| `\bintuitive\b(?=.*\bmoral\b)(?=.*\b(?:judg\|reason\|response)\b)` | Medium | M | Intuitive moral judgment/reasoning |
| `\baffect\b(?=.*\breason\w*\b)(?=.*\bmoral\b)` | Medium | M | Affect-reason interaction in morality |

**False-positive suppression patterns:**

| Pattern (regex) | Tier | Rationale |
|:----------------|:----:|:----------|
| `\bintuition\b(?!.*\b(?:moral\|intuitionist\|dumbfounding\|judgment\|sentiment\|ethic)\b)` | FP | Generic "intuition" without moral context |
| `\bsentiment\b(?!.*\b(?:moral\|ethic\|intuitionist\|humean)\b)` | FP | NLP sentiment analysis (non-moral) |

### Dyadic Morality --- New Patterns (11 patterns)

Prior to expansion, the vault contained 3 patterns for Dyadic Morality. All patterns below are new additions.

| Pattern (regex) | Detection Type | Tier | Rationale |
|:----------------|:---------------|:----:|:----------|
| `\bharm perception\b(?=.*\b(?:moral\|agent\|patient)\b)` | Strong | S | Harm perception in moral agent-patient context |
| `\bschein\b(?=.*\b(?:moral\|dyadic\|gray\|typecasting)\b)` | Strong | S | Chelsea Schein (co-author with Gray) |
| `\bagent[- ]patient\b(?=.*\bharm\b)` | Strong | S | Agent-patient harm dyad |
| `\btheory of dyadic morality\b` | Strong | S | Full theory name |
| `\bmoral dyad\b` | Medium | M | Moral dyad terminology |
| `\bagent and patient\b(?=.*\bmoral\b)` | Medium | M | Agent and patient in moral context |
| `\bmoral patient\b` | Medium | M | Moral patiency concept |
| `\bmoral agent\b(?=.*\bpatient\b)` | Medium | M | Moral agent with patient co-occurrence |
| `\bcomplete moral dyad\b` | Medium | M | Complete moral dyad |
| `\bharm[- ]based moral\w*\b` | Medium | M | Harm-based morality |
| `\bgray\b(?=.*\bschein\b)(?=.*\bmoral\b)` | Medium | M | Gray and Schein in moral context |

**False-positive suppression patterns:**

| Pattern (regex) | Tier | Rationale |
|:----------------|:----:|:----------|
| `\bdyad\b(?!.*\b(?:moral\|typecasting\|kurt gray\|harm\|agent\|patient)\b)` | FP | Generic "dyad" (e.g., parent-child dyad) |
| `\bpatient\b(?!.*\b(?:moral\|agent\|dyad\|typecasting\|harm)\b)` | FP | Medical "patient" |

### Scoring Formula

All theories use the same scoring formula:

```
score = (strong_matches x 15) + (medium_matches x 5) - (fp_context x 10) + title_bonus(20)
score = clamp(score, 0, 100)
```

A paper is classified as engaging a theory when `score >= 50`. The "strong floor" rule ensures that any paper with at least one strong-tier match receives a minimum score of 50.

---

## Supplementary Table 4 (ST4). 222 Candidate Benchmarks: Source Signal Distribution

Candidates were identified through a five-signal detection pipeline applied to 2,099 AI ethics papers. Signal definitions: **S1** = moral psychology score >= 50 on any of 8 mp_* fields; **S2** = benchmark/eval/dataset flag with >= 2 keyword matches; **S3** = published DATA_URL with >= 3 keyword matches; **S4** = >= 5 keyword matches regardless of other metadata; **S5** = known benchmark name in title or abstract.

### Signal Frequency

| Signal | Description | Papers Detected | % of 221 Candidates |
|:------:|:------------|:---------------:|:-------------------:|
| S1 | Moral psychology score >= 50 | 153 | 69.2% |
| S2 | Benchmark flag + keywords | 118 | 53.4% |
| S3 | DATA_URL + keywords | 65 | 29.4% |
| S4 | High keyword density (>= 5) | 8 | 3.6% |
| S5 | Known benchmark name | 0* | -- |

*Note: S5 matches were absorbed into S1--S4 during deduplication. Candidates matching known benchmark names (ETHICS, MoralBench, ValueBench, Scruples, Delphi, MACHIAVELLI, Moral Machine, MoralChoice, MoralExceptQA) were all also detected by other signals.

### Signal Combination Distribution

| Signal Combination | Count | % of 221 | Interpretation |
|:-------------------|:-----:|:--------:|:---------------|
| S1 only | 82 | 37.1% | High mp_* score but not flagged as benchmark or with data |
| S2 only | 32 | 14.5% | Flagged as benchmark with keywords but mp_* score < 50 |
| S1 + S2 | 31 | 14.0% | High mp_* score and benchmark flag |
| S1 + S2 + S3 | 29 | 13.1% | Full convergence: high score, benchmark flag, and public data |
| S2 + S3 | 18 | 8.1% | Benchmark with data but mp_* score < 50 |
| No signal recorded | 11 | 5.0% | Included via manual review or edge-case matching |
| S1 + S2 + S3 + S4 | 6 | 2.7% | Maximum signal convergence (4 signals) |
| S1 + S3 | 5 | 2.3% | High mp_* score with data but not flagged as benchmark |
| S3 only | 5 | 2.3% | Data available with keywords but low score and no flag |
| S2 + S3 + S4 | 2 | 0.9% | Benchmark with data and high keyword density |

### Multi-Signal vs. Single-Signal

| Category | Count | % of 221 |
|:---------|:-----:|:--------:|
| Single signal only | 119 | 53.8% |
| Multiple signals (2+) | 91 | 41.2% |
| No signal recorded | 11 | 5.0% |

### Candidate Type Distribution

| Type | Count | % of 221 |
|:-----|:-----:|:--------:|
| Benchmark | 176 | 79.6% |
| Dataset | 43 | 19.5% |
| Other | 2 | 0.9% |

### Candidate Year Distribution

| Year | Count | Year | Count |
|:----:|:-----:|:----:|:-----:|
| 2015 | 1 | 2022 | 8 |
| 2016 | 1 | 2023 | 27 |
| 2018 | 5 | 2024 | 62 |
| 2019 | 1 | 2025 | 97 |
| 2020 | 6 | 2026 | 10 |
| 2021 | 3 | | |

---

## Supplementary Table 5 (ST5). Assessment Coverage Matrix (55 Benchmarks x Key Features)

All 55 benchmarks receiving full 28-feature characterization are listed below. The table reports seven key features: A1 (theories engaged), A2 (operationalization level, 1--4), A5 (human baseline), A6 (construct validity, 1--5), B1 (task format), B2 (dataset size), and primary theory. Benchmarks are grouped by source: 40 from the primary council assessment and 15 from the secondary "hidden gem" scan.

### Primary Assessment (40 benchmarks)

| # | Benchmark | Theories | A1 | A2 | A5 | A6 | B1 | B2 |
|:-:|:----------|:---------|:--:|:--:|:---|:--:|:---|---:|
| 1 | Moral Machine Experiment (Awad et al., 2018) | Trolley | 1 | 3 | Published norms | 5 | Forced-choice | 40,000,000 |
| 2 | Crowdsourcing Moral Machines (Awad et al., 2020) | Trolley | 1 | 3 | Published norms | 4 | Forced-choice | 40,000,000 |
| 3 | Moral Foundations Vignettes (Clifford et al., 2015) | MFT | 1 | 4 | Published norms | 5 | Scenario rating | 132 |
| 4 | Moral Foundations Twitter Corpus (Hoover et al., 2020) | MFT | 1 | 3 | Paper-specific | 4 | Multi-label | 35,108 |
| 5 | Moral Foundations Reddit Corpus (Trager et al., 2022) | MFT | 1 | 3 | Paper-specific | 4 | Multi-label | 16,123 |
| 6 | Dutch MF Stimulus Database (Hopp et al., 2023) | MFT | 1 | 4 | Paper-specific | 5 | Scenario rating | 240 |
| 7 | Moral Foundations Weibo Corpus (Cao et al., 2024) | MFT | 1 | 3 | Paper-specific | 3 | Multi-label | 25,671 |
| 8 | Moral Foundations of LLMs (Abdulhai et al., 2024) | MFT | 1 | 4 | Published norms | 5 | Likert | 30 |
| 9 | Differences in MF of LLMs (Kirgis, 2024) | MFT | 1 | 4 | Published norms | 4 | Likert | 116 |
| 10 | MFTCXplain (Trager et al., 2025) | MFT | 1 | 3 | Paper-specific | 3 | Multi-turn | 3,000 |
| 11 | LLMs as Moral Hypocrites (Nunes et al., 2024) | MFT | 1 | 4 | Published norms | 4 | Likert + rating | 150 |
| 12 | MoralBench (Ji et al., 2024) | MFT | 1 | 3 | Published norms | 3 | Likert + rating | 162 |
| 13 | M3oralBench (Yan et al., 2024) | MFT | 1 | 3 | Partial | 3 | MCQ | 1,160 |
| 14 | MFD-LLM (Jotautaite et al., 2025) | MFT | 1 | 3 | None | 3 | MCQ | 1,079 |
| 15 | Whose Morality? (Aksoy et al., 2024) | MFT | 1 | 4 | Published norms | 4 | Likert | 36 |
| 16 | Culturally Grounded Personas (Tagarelli et al., 2026) | MFT, Schwartz | 2 | 3 | Published norms | 4 | Likert | 93,312 |
| 17 | Does Moral Code Have a Moral Code? (Fraser et al., 2022) | MFT, Schwartz | 2 | 3 | Published norms | 3 | Binary + MCQ | 100 |
| 18 | Probing Moral Development via DIT (Deng et al., 2023) | Kohlberg | 1 | 4 | Published norms | 4 | Rating + ranking | 9 |
| 19 | Multilingual DIT (Khandelwal et al., 2024) | Kohlberg | 1 | 4 | Published norms | 4 | Rating + ranking | 9 |
| 20 | MultiTP: Multilingual Trolley (Jin et al., 2024) | Trolley | 1 | 3 | Published norms | 4 | Forced-choice | 1,000 |
| 21 | Moral Machine on LLMs (Takemoto, 2024) | Trolley | 1 | 3 | Published norms | 4 | Forced-choice | 50,000 |
| 22 | Large-Scale MM on 52 LLMs (Zaim Bin Ahmad et al., 2025) | Trolley | 1 | 3 | Published norms | 4 | Forced-choice | 50,000 |
| 23 | Revisiting Trolley Problem (Hatemo et al., 2025) | Trolley | 1 | 2 | Paper-specific | 2 | Binary | 852 |
| 24 | Decoding Multilingual Moral Preferences (Vida et al., 2024) | Trolley | 1 | 2 | Published norms | 3 | Forced-choice | 6,500 |
| 25 | Analyzing Ethical Logic of 6 LLMs (Neuman et al., 2025) | MFT, Kohlberg, Trolley | 3 | 2 | None | 1 | Free-text | 12 |
| 26 | PRIME Framework (Neuman et al., 2025) | MFT, Kohlberg, Trolley | 3 | 3 | Partial | 2 | Mixed | 12 |
| 27 | Deontological Decision and Moral Identity (Xu & Ma, 2016) | Identity | 1 | 4 | Paper-specific | 4 | Likert + behavioral | 250 |
| 28 | TrolleyBench (Zhu, 2025) | Kohlberg, Trolley | 2 | 2 | Paper-specific | 2 | Binary | 50 |
| 29 | TrolleyBench (Zhu, 2025) [duplicate entry] | Kohlberg, Trolley | 2 | 2 | Paper-specific | 2 | Binary | 50 |
| 30 | Survey: MFT and PLMs (Zangari et al., 2024) | MFT | 1 | 1 | None | 1 | N/A (survey) | 0 |
| 31 | Value Kaleidoscope (Sorensen et al., 2024) | Schwartz | 1 | 2 | Paper-specific | 3 | Free-text + MCQ | 218,000 |
| 32 | CVC (Wu et al., 2025) | -- | 0 | 2 | Paper-specific | 3 | MCQ + scenario | 250,000 |
| 33 | Tracing MF in LLMs (Yu et al., 2026) | MFT | 1 | 3 | Partial | 3 | Rating + probing | 240 |
| 34 | BehaviorBench (Huang et al., 2025) | Kohlberg, MFT | 2 | 3 | Partial | 3 | Mixed | 5,000 |
| 35 | Interpretable Models for Moral Decisions (Noothigattu et al.) | Trolley | 1 | 2 | Published norms | 3 | Forced-choice | 3,000,000 |
| 36 | Social Chemistry 101 (Forbes et al.) | MFT | 1 | 2 | Paper-specific | 3 | Free-text + categorical | 292,000 |
| 37 | Mapping Moral Reasoning Circuits | MFT | 1 | 3 | None | 2 | Binary | 240 |
| 38 | Assessing LLMs for Moral Value Pluralism (Benkler et al., 2023) | Schwartz | 1 | 3 | Published norms | 3 | Free-text + scoring | 5 |
| 39 | HRI Value Compass (Drukker et al., 2025) | Schwartz | 1 | 2 | None | 2 | N/A (design tool) | 0 |
| 40 | Multilingual DIT [Khandelwal duplicate] | Kohlberg | 1 | 4 | Published norms | 4 | Rating + ranking | 9 |

### Hidden Gem Assessment (15 benchmarks)

| # | Benchmark | Theories | A1 | A2 | A5 | A6 | B1 | B2 |
|:-:|:----------|:---------|:--:|:--:|:---|:--:|:---|---:|
| 41 | EMNLP (Jiang et al., 2025) | Kohlberg | 1 | 3 | Paper-specific | 3 | Mixed | 88 |
| 42 | How Much of a Pluralist is ChatGPT? (2025) | Pluralism, MFT | 2 | 4 | Paper-specific | 4 | Scenario rating | 120 |
| 43 | The Straight and Narrow (Hu et al., 2026) | MFT | 1 | 3 | None | 3 | Scenario rating | 0 |
| 44 | Normative Eval with Everyday Moral Dilemmas (Sachdeva et al., 2025) | MFT | 1 | 2 | Published norms | 3 | MCQ | 10,826 |
| 45 | ValAct-15k (Huang et al., 2026) | Schwartz | 1 | 4 | Paper-specific | 4 | MCQ | 15,000 |
| 46 | Value-Spectrum (Li et al., 2024) | Schwartz | 1 | 3 | None | 2 | MCQ | 50,191 |
| 47 | AdAEM (Duan et al., 2025) | Schwartz | 1 | 3 | None | 3 | MCQ | 12,310 |
| 48 | Pluralistic Moral Gap (Russo et al., 2025) | Other | 1 | 2 | Published norms | 3 | Binary | 1,618 |
| 49 | Insights into Moral Reasoning (Sameer et al., 2025) | MFT, Kohlberg, Intuitionist | 3 | 4 | Paper-specific | 4 | Likert | 2,438 |
| 50 | PVQ-RR on LLMs (Hadar-Shoval et al., 2024) | Schwartz | 1 | 4 | Published norms | 5 | Likert | 57 |
| 51 | Bago et al. (2022) 45-Country Trolley | Trolley, Dual Process, Intuitionist | 3 | 3 | Published norms | 5 | Binary | 27,502 |
| 52 | Staircase of Ethics (Wu, 2025) | MFT, Dual Process | 2 | 3 | None | 3 | Forced-choice | 16,510 |
| 53 | ValueCompass (Shen et al., 2025) | Schwartz, Dyadic | 2 | 3 | Paper-specific | 4 | Likert | 6,272 |
| 54 | GPLA (Ye et al., 2025) | Schwartz | 1 | 3 | None | 4 | Free-text | 693 |
| 55 | UniMoral (Kumar, 2025) | MFT, Kohlberg, Dual Process, Intuitionist | 4 | 3 | Paper-specific | 4 | Mixed | 0 |

### Feature Distribution Summary (55 benchmarks)

**A2 --- Construct Operationalization:**

| Level | Interpretation | Count | % |
|:-----:|:---------------|:-----:|:-:|
| 4 | Validated instrument administered | 16 | 29% |
| 3 | Theory-derived / adapted | 25 | 45% |
| 2 | Theory-inspired, no validation | 12 | 22% |
| 1 | Keyword-level engagement only | 2 | 4% |

**A5 --- Human Baseline Availability:**

| Level | Count | % |
|:------|:-----:|:-:|
| Published norms | 23 | 42% |
| Paper-specific | 18 | 33% |
| Partial | 4 | 7% |
| None | 10 | 18% |

**A6 --- Construct Validity:**

| Score | Interpretation | Count | % |
|:-----:|:---------------|:-----:|:-:|
| 5 | Multi-study validated | 6 | 11% |
| 4 | Single-study validated | 20 | 36% |
| 3 | Adapts validated instrument | 20 | 36% |
| 2 | Theory-inspired, no validation | 7 | 13% |
| 1 | Keyword-level only | 2 | 4% |

**B1 --- Task Format:**

| Format | Count | % |
|:-------|:-----:|:-:|
| Forced-choice / Binary | 14 | 25% |
| MCQ | 8 | 15% |
| Likert | 11 | 20% |
| Scenario rating / ranking | 8 | 15% |
| Multi-label classification | 3 | 5% |
| Free-text (incl. + MCQ) | 5 | 9% |
| Mixed / Multi-turn | 4 | 7% |
| N/A (survey, design tool) | 2 | 4% |

**Theory Engagement (A1):**

| Theories Engaged | Count | % |
|:----------------:|:-----:|:-:|
| 0 | 1 | 2% |
| 1 | 38 | 69% |
| 2 | 9 | 16% |
| 3 | 5 | 9% |
| 4 | 2 | 4% |

**Primary Theory Distribution:**

| Theory | Count (primary or co-primary) |
|:-------|:-----------------------------:|
| MFT | 24 |
| Trolley | 13 |
| Schwartz | 11 |
| Kohlberg | 10 |
| Dual Process | 3 |
| Social Intuitionism | 2 |
| Dyadic Morality | 1 |
| Moral Identity | 1 |
| Other / None | 2 |

*Note: Counts sum to > 55 because benchmarks engaging multiple theories are counted under each.*
