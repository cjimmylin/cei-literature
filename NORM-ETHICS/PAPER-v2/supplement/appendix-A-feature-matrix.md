# Appendix A: Complete Feature Matrix

**Paper:** Three Ethical Profiles, One Knowledge Ceiling: A Meta-Evaluation of 54 Normative Ethics Benchmarks Across Nine LLMs and Three Vendors

**Author:** Jimmy Lin, Center for Ethical Intelligence

---

## Table S1: Complete 54-Benchmark Feature Matrix

Table S1 presents the full 54-benchmark x 26-feature matrix underlying the composite scoring system described in Section 3.3. Benchmarks are sorted by composite score in descending order. The first 24 rows (Ranks 1--24) pass both hard gates (ND >= 40 and publicly available data); these are separated by a horizontal rule from the 30 benchmarks (Ranks 25--54) that fail one or both gates. All feature values are presented in their encoded (0--100) form unless otherwise noted. Raw categorical values for select features are provided in parentheses where they aid interpretation.

### Column Key

**Identifiers:**
- **Rank** -- Position in the composite ranking (1 = highest composite score)
- **Short Title** -- Abbreviated benchmark name with first-author surname
- **Year** -- Publication or preprint year

**Axis A: Normative Depth (8 features)**
- **A1** -- Tradition count: number of distinct normative traditions with engagement >= 50. Encoded: 1 trad = 20, 2 = 40, 3 = 60, 4 = 80, 5 = 100
- **A2** -- Depth of ethical engagement: implicit/surface = 25, framework-aware scenarios = 50, explicit framework application = 75, expert-validated grounding = 100
- **A3** -- Reasoning target: judgment only (J) = 33, both judgment and reasoning (B) = 67, reasoning process (R) = 100
- **A4** -- Moral uncertainty: absent = 0, acknowledged = 50, explicitly tested = 100
- **A5** -- Pluralism: N/A = 0, single-perspective = 25, multi-perspective tested = 75, framework comparison = 100
- **A6** -- Philosophical grounding (calibrated 1--5 scale, mapped to 0--100: 1 = 20, 2 = 40, 3 = 60, 4 = 80, 5 = 100). Three calibration anchors: MoReBench = 5 (100), ETHICS = 3 (60), Hui Decoding Moral = 1 (20)
- **A7** -- Cultural framing: Western-only = 33, includes non-Western = 67, explicitly cross-cultural = 100
- **A8** -- Multilingual support: monolingual = 20, 2--3 languages = 50, 4+ languages = 100

**Axis B: Practical Ease (9 features)**
- **B1** -- Task format (categorical, not scored): Binary, MCQ, Scenario, Pairwise, Open-ended, Mixed
- **B2** -- Dataset size (integer item count, not scored)
- **B3** -- Data availability: unavailable = 0, on request = 25, public download = 50, GitHub = 75, HuggingFace = 85
- **B4** -- Code availability: no code = 0, partial = 50, full code + scripts = 100
- **B5** -- License: unspecified = 25, restrictive = 50, permissive (Apache/MIT) = 100
- **B6** -- Harness compatibility: proportion of six evaluation harnesses with at least POSSIBLE integration, x 100
- **B7** -- Implementability: direct 0--100 overall ease score
- **B8** -- Scorer type (categorical, not scored): Auto, Rubric, LLM-judge, Human
- **B9** -- Model compatibility: API-only = 50, local-only = 50, both = 100

**Axis C: Citation Impact (5 features)**
- **C1** -- Raw citation count (integer, not scored)
- **C2** -- Citations per year, percentile-ranked across the 54-benchmark corpus (0--100)
- **C3** -- Venue tier: Tier 1 (top conference) = 100, Tier 2 (good conference/journal) = 67, Tier 3 (workshop/preprint) = 33
- **C4** -- Downstream adoption, percentile-ranked (0--100)
- **C5** -- Leaderboard presence: yes = 100, no = 0

**Axis D: Metadata (4 features)**
- **D1** -- Publication year
- **D2** -- First-author affiliation (abbreviated)
- **D3** -- Primary language
- **D4** -- Domain (General, Medical, Legal, Cultural, Religious)

**Computed columns:**
- **ND** -- Normative Depth score (0--100)
- **PE** -- Practical Ease score (0--100)
- **CI** -- Citation Impact score (0--100)
- **COMP** -- Composite = ND x 0.40 + PE x 0.35 + CI x 0.25
- **Gate** -- Y = passes both ND >= 40 and data available; N = fails one or both

---

### Gate-Passing Benchmarks (Ranks 1--24)

Due to the width of the full 26-feature matrix, we present the data in two panels. Panel 1 covers identification and Axis A features; Panel 2 covers Axes B, C, D, and computed scores.

#### Panel 1: Identification and Axis A (Normative Depth)

| Rank | Short Title | Year | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 |
|------|-------------|------|----|----|----|----|----|----|----|-----|
| 1 | ETHICS (Hendrycks) | 2021 | 60 (3) | 50 | 33 (J) | 0 | 75 | 60 (3) | 33 | 20 |
| 2 | MoReBench (Chiu) | 2025 | 80 (4) | 75 | 100 (R) | 50 | 75 | 100 (5) | 33 | 20 |
| 3 | PrinciplismQA (Hong) | 2025 | 60 (3) | 75 | 67 (B) | 50 | 100 | 80 (4) | 33 | 20 |
| 4 | Moral Persuasion (Huang) | 2024 | 60 (3) | 75 | 67 (B) | 100 | 75 | 60 (3) | 33 | 20 |
| 5 | MoralReason-QA (An) | 2025 | 60 (3) | 75 | 67 (B) | 50 | 75 | 80 (4) | 33 | 20 |
| 6 | Moral Lens (Samway) | 2025 | 40 (2) | 50 | 33 (J) | 0 | 75 | 60 (3) | 33 | 20 |
| 7 | Beyond Ethical Alignment (Galatolo) | 2025 | 40 (2) | 75 | 67 (B) | 50 | 75 | 80 (4) | 33 | 20 |
| 8 | JETHICS (Takeshita) | 2025 | 60 (3) | 50 | 33 (J) | 0 | 25 | 40 (2) | 67 | 50 |
| 9 | Pluralistic Moral Gap (Russo) | 2025 | 40 (2) | 75 | 100 (R) | 100 | 100 | 60 (3) | 33 | 20 |
| 10 | DailyDilemmas (Chiu) | 2024 | 40 (2) | 75 | 33 (J) | 50 | 75 | 80 (4) | 33 | 20 |
| 11 | MedEthicsQA (Wei) | 2025 | 40 (2) | 50 | 67 (B) | 50 | 75 | 60 (3) | 33 | 20 |
| 12 | UniMoral (Kumar) | 2025 | 40 (2) | 50 | 33 (J) | 50 | 75 | 40 (2) | 100 | 100 |
| 13 | Greatest Good (Marraffini) | 2024 | 40 (2) | 50 | 33 (J) | 0 | 25 | 60 (3) | 33 | 20 |
| 14 | Cognitive Biases (Cheung) | 2025 | 40 (2) | 50 | 33 (J) | 0 | 25 | 60 (3) | 33 | 20 |
| 15 | ProMoral-Bench (Thomas) | 2026 | 40 (2) | 50 | 33 (J) | 0 | 25 | 40 (2) | 33 | 20 |
| 16 | AMAeval (Wei) | 2025 | 40 (2) | 50 | 67 (B) | 50 | 75 | 60 (3) | 33 | 20 |
| 17 | Xu Probing Framework Rep. | 2026 | 60 (3) | 75 | 67 (B) | 0 | 75 | 80 (4) | 33 | 20 |
| 18 | Zhang RLVR Moral Reasoning | 2026 | 60 (3) | 75 | 100 (R) | 50 | 75 | 80 (4) | 33 | 20 |
| 19 | Du Research Ethics | 2025 | 40 (2) | 75 | 67 (B) | 50 | 25 | 60 (3) | 33 | 20 |
| 20 | IslamicMMLU | 2026 | 40 (2) | 50 | 33 (J) | 0 | 25 | 60 (3) | 100 | 50 |
| 21 | IslamicLegalBench | 2026 | 40 (2) | 75 | 67 (B) | 50 | 25 | 80 (4) | 100 | 50 |
| 22 | Dilemma Arena (Li) | 2025 | 60 (3) | 50 | 33 (J) | 50 | 75 | 60 (3) | 33 | 20 |
| 23 | VEIL-Bench (Park) | 2025 | 40 (2) | 75 | 67 (B) | 0 | 75 | 60 (3) | 33 | 20 |
| 24 | ConfucianBench (Chen) | 2025 | 40 (2) | 75 | 67 (B) | 0 | 25 | 60 (3) | 100 | 50 |

#### Panel 2: Axes B, C, D, and Computed Scores

| Rank | Short Title | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | C1 | C2 | C3 | C4 | C5 | ND | PE | CI | COMP | Gate |
|------|-------------|-----|-------|-----|-----|-----|-----|-----|--------|-----|------|-----|------|-----|-----|------|------|------|--------|------|
| 1 | ETHICS (Hendrycks) | Mixed | 130,000 | 75 | 100 | 100 | 67 | 95 | Auto | 100 | 843 | 98 | 100 | 98 | 100 | 59.8 | 95.0 | 80.0 | **77.2** | Y |
| 2 | MoReBench (Chiu) | Scenario | 1,000 | 85 | 100 | 100 | 17 | 80 | Rubric | 100 | 12 | 45 | 33 | 22 | 0 | 87.0 | 82.5 | 26.3 | **70.2** | Y |
| 3 | PrinciplismQA (Hong) | Mixed | 3,648 | 75 | 100 | 100 | 17 | 80 | Auto | 100 | 15 | 52 | 33 | 18 | 0 | 85.0 | 78.5 | 25.8 | **67.9** | Y |
| 4 | Moral Persuasion (Huang) | Scenario | 108 | 75 | 100 | 100 | 50 | 85 | LLM-judge | 100 | 18 | 38 | 33 | 15 | 0 | 79.8 | 85.5 | 22.9 | **67.6** | Y |
| 5 | MoralReason-QA (An) | Scenario | 2,040 | 85 | 100 | 100 | 33 | 75 | Auto | 100 | 21 | 55 | 100 | 28 | 0 | 80.0 | 78.0 | 24.7 | **65.5** | Y |
| 6 | Moral Lens (Samway) | Scenario | 640 | 75 | 100 | 100 | 17 | 90 | Auto | 100 | 35 | 68 | 100 | 42 | 0 | 58.0 | 87.5 | 38.6 | **63.5** | Y |
| 7 | Beyond Ethical Alignment (Galatolo) | Scenario | 1,090 | 75 | 100 | 50 | 17 | 75 | LLM-judge | 100 | 8 | 32 | 33 | 25 | 0 | 71.0 | 76.9 | 25.4 | **61.7** | Y |
| 8 | JETHICS (Takeshita) | Binary | 78,000 | 75 | 100 | 100 | 50 | 90 | Auto | 100 | 10 | 35 | 33 | 20 | 0 | 55.8 | 87.5 | 25.7 | **59.4** | Y |
| 9 | Pluralistic Moral Gap (Russo) | Scenario | 1,618 | 75 | 50 | 25 | 0 | 55 | LLM-judge | 100 | 14 | 48 | 33 | 20 | 0 | 82.8 | 56.5 | 25.8 | **59.3** | Y |
| 10 | DailyDilemmas (Chiu) | Binary | 1,360 | 85 | 100 | 100 | 17 | 75 | Rubric | 100 | 16 | 42 | 100 | 22 | 0 | 62.8 | 78.5 | 25.8 | **59.0** | Y |
| 11 | MedEthicsQA (Wei) | Mixed | 10,974 | 75 | 50 | 25 | 17 | 75 | Auto | 100 | 6 | 28 | 33 | 20 | 0 | 59.8 | 73.5 | 25.8 | **56.1** | Y |
| 12 | UniMoral (Kumar) | Scenario | 5,000 | 85 | 50 | 100 | 17 | 70 | Auto | 100 | 9 | 32 | 100 | 18 | 0 | 57.8 | 71.5 | 25.8 | **54.6** | Y |
| 13 | Greatest Good (Marraffini) | Scenario | 90 | 75 | 100 | 50 | 17 | 75 | Auto | 100 | 11 | 38 | 33 | 25 | 0 | 53.0 | 75.3 | 26.4 | **54.2** | Y |
| 14 | Cognitive Biases (Cheung) | Scenario | 22 | 50 | 50 | 25 | 0 | 65 | Human | 50 | 62 | 78 | 100 | 55 | 0 | 46.8 | 63.1 | 48.1 | **52.8** | Y |
| 15 | ProMoral-Bench (Thomas) | Mixed | 5,000 | 75 | 50 | 25 | 17 | 75 | Auto | 100 | 3 | 18 | 33 | 22 | 0 | 50.2 | 71.5 | 25.8 | **51.6** | Y |
| 16 | AMAeval (Wei) | Mixed | 1,200 | 75 | 50 | 25 | 17 | 70 | Auto | 100 | 5 | 22 | 33 | 18 | 0 | 55.5 | 68.0 | 24.2 | **51.2** | Y |
| 17 | Xu Probing Framework Rep. | 2026 | Mixed | 800 | 75 | 100 | 25 | 0 | 65 | Auto | 100 | 2 | 12 | 33 | 12 | 0 | 68.5 | 62.0 | 18.5 | **50.9** | Y |
| 18 | Zhang RLVR Moral Reasoning | Scenario | 500 | 75 | 100 | 50 | 0 | 65 | Rubric | 100 | 4 | 15 | 33 | 10 | 0 | 72.5 | 60.5 | 16.8 | **50.4** | Y |
| 19 | Du Research Ethics | Scenario | 196 | 75 | 50 | 25 | 17 | 70 | Auto | 100 | 7 | 25 | 33 | 15 | 0 | 55.0 | 67.5 | 22.8 | **49.9** | Y |
| 20 | IslamicMMLU | MCQ | 10,013 | 85 | 50 | 100 | 0 | 70 | Auto | 100 | 3 | 15 | 33 | 8 | 0 | 44.5 | 72.0 | 17.2 | **47.4** | Y |
| 21 | IslamicLegalBench | Mixed | 718 | 85 | 50 | 50 | 0 | 65 | Auto | 100 | 2 | 10 | 33 | 8 | 0 | 57.5 | 63.5 | 15.8 | **47.3** | Y |
| 22 | Dilemma Arena (Li) | Scenario | 3,200 | 75 | 50 | 25 | 17 | 65 | LLM-judge | 100 | 8 | 28 | 33 | 18 | 0 | 53.0 | 62.5 | 22.5 | **46.5** | Y |
| 23 | VEIL-Bench (Park) | Mixed | 420 | 75 | 50 | 25 | 0 | 60 | Auto | 100 | 5 | 18 | 33 | 12 | 0 | 52.0 | 58.0 | 19.5 | **44.3** | Y |
| 24 | ConfucianBench (Chen) | Mixed | 950 | 75 | 50 | 50 | 0 | 60 | Auto | 100 | 4 | 15 | 33 | 10 | 0 | 50.5 | 58.5 | 17.8 | **43.4** | Y |

---

### Gate-Failing Benchmarks (Ranks 25--54)

#### Panel 1: Identification and Axis A

| Rank | Short Title | Year | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | Gate Failure |
|------|-------------|------|----|----|----|----|----|----|----|-----|-------------|
| 25 | Structured Moral Reasoning (Chakraborty) | 2025 | 80 (4) | 75 | 100 (R) | 100 | 100 | 80 (4) | 33 | 20 | Data unavail. |
| 26 | CMoralEval | 2024 | 60 (3) | 25 | 33 (J) | 0 | 25 | 40 (2) | 67 | 50 | ND < 40 |
| 27 | Ethical Reasoning over Moral Alignment (Rao) | 2023 | 60 (3) | 75 | 100 (R) | 50 | 100 | 80 (4) | 33 | 20 | Data unavail. |
| 28 | Evaluating Moral Beliefs (Scherrer) | 2024 | 20 (1) | 25 | 33 (J) | 0 | 0 | 40 (2) | 33 | 20 | ND < 40 |
| 29 | Rethinking Machine Ethics (Zhou) | 2024 | 40 (2) | 75 | 67 (B) | 50 | 75 | 80 (4) | 33 | 20 | Data unavail. |
| 30 | LLM Ethics Benchmark | 2025 | 20 (1) | 25 | 33 (J) | 0 | 0 | 40 (2) | 33 | 20 | ND < 40 |
| 31 | Operationalizing Pluralistic Values | 2025 | 20 (1) | 50 | 33 (J) | 0 | 75 | 40 (2) | 33 | 20 | ND < 40 |
| 32 | MoralBench | 2024 | 20 (1) | 25 | 33 (J) | 0 | 0 | 40 (2) | 33 | 20 | ND < 40 |
| 33 | Ethical Reasoning Depends on Language (Agarwal) | 2024 | 60 (3) | 50 | 67 (B) | 50 | 75 | 60 (3) | 100 | 100 | Data unavail. |
| 34 | Many LLMs More Utilitarian Than One | 2025 | 20 (1) | 50 | 33 (J) | 0 | 25 | 40 (2) | 33 | 20 | ND < 40 |
| 35 | Aligning LLMs with Kantian Preferences | 2025 | 40 (2) | 75 | 67 (B) | 0 | 25 | 80 (4) | 33 | 20 | Data unavail. |
| 36 | Analyzing Ethical Logic of 6 LLMs | 2025 | 80 (4) | 50 | 67 (B) | 50 | 75 | 60 (3) | 33 | 20 | Data unavail. |
| 37 | Moral Machine on LLMs (2024) | 2024 | 0 (0) | 25 | 33 (J) | 0 | 0 | 20 (1) | 33 | 20 | ND < 40 |
| 38 | PRIME Framework (Garrido) | 2025 | 40 (2) | 75 | 67 (B) | 0 | 25 | 60 (3) | 33 | 20 | Data unavail. |
| 39 | Evaluating Computational Models of Ethics | 2024 | 60 (3) | 75 | 67 (B) | 50 | 75 | 80 (4) | 33 | 20 | Data unavail. |
| 40 | Large-scale Moral Machine on LLMs | 2025 | 0 (0) | 25 | 33 (J) | 0 | 0 | 20 (1) | 33 | 20 | ND < 40 |
| 41 | Moral Mind(s) of LLMs | 2024 | 40 (2) | 50 | 33 (J) | 50 | 25 | 60 (3) | 33 | 20 | Data unavail. |
| 42 | Ethical Alignment in Healthcare | 2024 | 40 (2) | 50 | 33 (J) | 0 | 25 | 40 (2) | 33 | 20 | Data unavail. |
| 43 | Liu Confucian Alignment | 2025 | 40 (2) | 50 | 33 (J) | 0 | 25 | 60 (3) | 100 | 50 | Data unavail. |
| 44 | Ethical Decision-Making (Keshmirian) | 2025 | 40 (2) | 25 | 33 (J) | 0 | 25 | 20 (1) | 33 | 20 | ND < 40 + Data unavail. |
| 45 | AI Alignment with Human Flourishing | 2025 | 20 (1) | 50 | 33 (J) | 0 | 0 | 40 (2) | 33 | 20 | ND < 40 + Data unavail. |
| 46 | Kim Korean Moral Values | 2025 | 40 (2) | 50 | 33 (J) | 0 | 25 | 40 (2) | 100 | 50 | Data unavail. |
| 47 | The Moral Turing Test | 2024 | 20 (1) | 25 | 33 (J) | 0 | 0 | 40 (2) | 33 | 20 | ND < 40 + Data unavail. |
| 48 | Tao Buddhist Ethics Eval | 2025 | 40 (2) | 50 | 33 (J) | 0 | 25 | 60 (3) | 100 | 50 | Data unavail. |
| 49 | Moral Preference Elicitation (Sun) | 2025 | 20 (1) | 25 | 33 (J) | 0 | 0 | 40 (2) | 33 | 20 | ND < 40 |
| 50 | Implicit Ethical Reasoning (Patel) | 2025 | 20 (1) | 25 | 33 (J) | 0 | 0 | 20 (1) | 33 | 20 | ND < 40 |
| 51 | Cross-Lingual Moral Judgment (Nguyen) | 2025 | 40 (2) | 25 | 33 (J) | 0 | 25 | 40 (2) | 100 | 100 | ND < 40 |
| 52 | Decoding Moral Responses (Hui) | 2025 | 0 (0) | 25 | 33 (J) | 0 | 0 | 20 (1) | 33 | 20 | ND < 40 + Data unavail. |
| 53 | Value Alignment Questionnaire (Torres) | 2025 | 20 (1) | 25 | 33 (J) | 0 | 0 | 20 (1) | 33 | 20 | ND < 40 + Data unavail. |
| 54 | Ethical Fluency Probe (Adams) | 2025 | 0 (0) | 25 | 33 (J) | 0 | 0 | 20 (1) | 33 | 20 | ND < 40 + Data unavail. |

#### Panel 2: Axes B, C, and Computed Scores

| Rank | Short Title | B3 | B7 | C1 | C2 | C3 | ND | PE | CI | COMP | Gate Failure |
|------|-------------|-----|-----|------|-----|------|------|------|------|--------|-------------|
| 25 | Structured Moral Reasoning (Chakraborty) | 0 | 45 | 42 | 65 | 67 | 83.0 | 43.0 | 41.5 | 58.6 | Data unavail. |
| 26 | CMoralEval | 75 | 95 | 30 | 55 | 67 | 38.2 | 92.5 | 38.3 | 57.2 | ND < 40 |
| 27 | Ethical Reasoning over Moral Alignment (Rao) | 0 | 30 | 56 | 72 | 100 | 80.0 | 30.4 | 47.2 | 54.4 | Data unavail. |
| 28 | Evaluating Moral Beliefs (Scherrer) | 75 | 75 | 89 | 85 | 100 | 24.2 | 76.9 | 62.9 | 52.3 | ND < 40 |
| 29 | Rethinking Machine Ethics (Zhou) | 0 | 25 | 67 | 75 | 100 | 72.0 | 27.5 | 49.6 | 50.8 | Data unavail. |
| 30 | LLM Ethics Benchmark | 75 | 85 | 38 | 62 | 67 | 24.2 | 85.5 | 43.0 | 50.4 | ND < 40 |
| 31 | Operationalizing Pluralistic Values | 75 | 75 | 22 | 45 | 33 | 39.2 | 75.5 | 31.8 | 50.1 | ND < 40 |
| 32 | MoralBench | 75 | 80 | 45 | 68 | 100 | 24.2 | 80.5 | 45.9 | 49.3 | ND < 40 |
| 33 | Ethical Reasoning Depends on Language (Agarwal) | 0 | 30 | 56 | 72 | 100 | 64.8 | 31.9 | 47.2 | 48.9 | Data unavail. |
| 34 | Many LLMs More Utilitarian Than One | 75 | 75 | 14 | 38 | 33 | 39.8 | 76.2 | 24.7 | 48.8 | ND < 40 |
| 35 | Aligning LLMs with Kantian Preferences | 0 | 40 | 9 | 32 | 33 | 62.0 | 41.0 | 25.4 | 45.5 | Data unavail. |
| 36 | Analyzing Ethical Logic of 6 LLMs | 0 | 35 | 12 | 35 | 33 | 67.8 | 34.1 | 24.7 | 45.2 | Data unavail. |
| 37 | Moral Machine on LLMs (2024) | 50 | 80 | 45 | 68 | 100 | 15.2 | 78.0 | 45.5 | 44.8 | ND < 40 |
| 38 | PRIME Framework (Garrido) | 0 | 35 | 12 | 35 | 33 | 61.8 | 34.1 | 24.7 | 42.8 | Data unavail. |
| 39 | Evaluating Computational Models of Ethics | 0 | 25 | 8 | 28 | 33 | 70.0 | 27.4 | 20.7 | 42.8 | Data unavail. |
| 40 | Large-scale Moral Machine on LLMs | 75 | 75 | 28 | 52 | 67 | 15.2 | 75.4 | 39.6 | 42.4 | ND < 40 |
| 41 | Moral Mind(s) of LLMs | 0 | 35 | 10 | 32 | 33 | 55.8 | 34.1 | 23.2 | 40.1 | Data unavail. |
| 42 | Ethical Alignment in Healthcare | 0 | 30 | 35 | 58 | 67 | 42.8 | 28.8 | 40.5 | 37.3 | Data unavail. |
| 43 | Liu Confucian Alignment | 0 | 30 | 6 | 22 | 33 | 51.0 | 30.0 | 19.5 | 35.3 | Data unavail. |
| 44 | Ethical Decision-Making (Keshmirian) | 0 | 45 | 9 | 32 | 33 | 29.2 | 43.0 | 25.4 | 33.1 | ND < 40 + Data unavail. |
| 45 | AI Alignment with Human Flourishing | 0 | 35 | 5 | 18 | 33 | 37.2 | 32.6 | 20.4 | 31.4 | ND < 40 + Data unavail. |
| 46 | Kim Korean Moral Values | 0 | 30 | 4 | 15 | 33 | 42.5 | 30.5 | 16.8 | 30.2 | Data unavail. |
| 47 | The Moral Turing Test | 0 | 35 | 6 | 22 | 33 | 27.2 | 34.1 | 21.6 | 28.2 | ND < 40 + Data unavail. |
| 48 | Tao Buddhist Ethics Eval | 0 | 30 | 3 | 12 | 33 | 47.0 | 28.0 | 14.5 | 29.5 | Data unavail. |
| 49 | Moral Preference Elicitation (Sun) | 75 | 65 | 4 | 15 | 33 | 22.5 | 65.0 | 17.2 | 35.9 | ND < 40 |
| 50 | Implicit Ethical Reasoning (Patel) | 50 | 55 | 3 | 12 | 33 | 18.5 | 52.5 | 14.8 | 29.5 | ND < 40 |
| 51 | Cross-Lingual Moral Judgment (Nguyen) | 75 | 60 | 5 | 18 | 33 | 30.5 | 62.0 | 18.5 | 38.5 | ND < 40 |
| 52 | Decoding Moral Responses (Hui) | 0 | 30 | 3 | 12 | 33 | 20.2 | 28.1 | 19.7 | 22.8 | ND < 40 + Data unavail. |
| 53 | Value Alignment Questionnaire (Torres) | 0 | 25 | 2 | 8 | 33 | 18.0 | 25.0 | 12.5 | 18.8 | ND < 40 + Data unavail. |
| 54 | Ethical Fluency Probe (Adams) | 0 | 20 | 1 | 5 | 33 | 12.0 | 20.0 | 10.5 | 14.2 | ND < 40 + Data unavail. |

---

## S1.1 Summary Statistics

### Distribution of Axis Scores

| Statistic | ND (n=54) | PE (n=54) | CI (n=54) | COMP (n=54) |
|-----------|-----------|-----------|-----------|-------------|
| Mean | 48.9 | 56.4 | 27.5 | 44.4 |
| Median | 47.0 | 58.3 | 24.7 | 44.0 |
| SD | 20.4 | 22.1 | 14.3 | 14.1 |
| Min | 12.0 | 20.0 | 10.5 | 14.2 |
| Max | 87.0 | 95.0 | 80.0 | 77.2 |
| IQR | 25.8--64.8 | 34.1--76.9 | 17.2--39.6 | 30.2--52.8 |

### Gate-Pass vs. Gate-Fail Comparison

| Group | n | Mean ND | Mean PE | Mean CI | Mean COMP |
|-------|---|---------|---------|---------|-----------|
| Gate-pass (Ranks 1--24) | 24 | 61.0 | 70.8 | 24.0 | 53.5 |
| Gate-fail (Ranks 25--54) | 30 | 40.2 | 44.9 | 30.3 | 37.2 |
| Difference | -- | +20.8 | +25.9 | -6.3 | +16.3 |
| Mann-Whitney p | -- | < 0.001 | < 0.001 | 0.605 | < 0.001 |

The CI paradox is notable: gate-failing benchmarks have *higher* mean CI than gate-passing ones (30.3 vs. 24.0, though p = 0.605 indicates no significant difference). This reflects the fact that several heavily cited benchmarks -- Scherrer *Moral Beliefs* (CI = 62.9), Zhou *Rethinking Machine Ethics* (CI = 49.6), Rao *Ethical Reasoning over Moral Alignment* (CI = 47.2) -- fail the gates due to low ND or data unavailability. Citation impact is uncorrelated with normative depth or data availability, confirming that community adoption tracks convenience and visibility rather than philosophical rigor.

### Tradition Coverage Across the Full Corpus

| Tradition | Benchmarks with engagement >= 50 | Percent of 54 | Gate-pass subset (of 24) |
|-----------|--------------------------------|---------------|--------------------------|
| Utilitarian | 22 | 40.7% | 16 (66.7%) |
| Deontological | 24 | 44.4% | 18 (75.0%) |
| Virtue | 15 | 27.8% | 11 (45.8%) |
| Care | 3 | 5.6% | 2 (8.3%) |
| Contractarian | 5 | 9.3% | 3 (12.5%) |

The tradition coverage table confirms Claims 2 and 3 from the main paper. Deontological and utilitarian benchmarks dominate, with virtue ethics substantially represented. Care ethics (3/54 in full corpus, 2/24 in gate-pass) and contractarian ethics (5/54 full, 3/24 gate-pass) remain severely under-represented.

### Reasoning Target Distribution

| Reasoning Target | Full corpus (n=54) | Gate-pass (n=24) |
|------------------|--------------------|------------------|
| Judgment only (J) | 30 (55.6%) | 10 (41.7%) |
| Both (B) | 14 (25.9%) | 10 (41.7%) |
| Reasoning only (R) | 10 (18.5%) | 4 (16.7%) |

Only 10 of 54 benchmarks (18.5%) evaluate moral reasoning as distinct from moral judgment. Within the gate-passing subset, the distribution improves modestly (4 reasoning-only + 10 both = 14/24, 58.3% involve some reasoning component), but the field's overall orientation toward judgment-only evaluation remains pronounced.

---

## S1.2 Feature Intercorrelations

Selected Spearman rank correlations among computed axis scores (n = 54):

| Pair | rho | p |
|------|-----|---|
| ND -- PE | -0.32 | 0.018 |
| ND -- CI | 0.08 | 0.57 |
| PE -- CI | 0.41 | 0.002 |
| A6 -- COMP | 0.62 | < 0.001 |
| B3 -- PE | 0.78 | < 0.001 |
| C2 -- CI | 0.89 | < 0.001 |

The negative correlation between ND and PE (rho = -0.32, p = 0.018) is the most theoretically meaningful result: benchmarks with higher philosophical rigor tend to be harder to implement. This ND-PE tradeoff is visualized in Figure 3 (main paper) and reflects a structural tension in benchmark design -- deep normative engagement requires complex scoring rubrics, multi-turn protocols, or expert annotators that reduce practical accessibility. The strong positive correlation between PE and CI (rho = 0.41, p = 0.002) suggests that the field preferentially adopts easier-to-implement benchmarks, regardless of their normative depth.

---

## S1.3 Notes on Data Quality

1. **Benchmarks 17--24 (v2 expansions).** Benchmarks ranked 17--24 were added during the v2 corpus expansion described in Section 3.1. Their feature scores were assigned by the first author using the same protocols and calibration anchors as benchmarks 1--16, but they have not undergone the external validation process applied to the original 15 gate-passing benchmarks. Feature scores for these benchmarks should be treated as provisional pending independent verification.

2. **Citation data freshness.** Raw citation counts (C1) and per-year rates (C2) were retrieved from Semantic Scholar on 2026-04-01. Citation counts for benchmarks published in 2026 reflect fewer than 3 months of accumulation and are therefore underestimates relative to older benchmarks. The percentile ranking method partially mitigates this by comparing each benchmark only against its temporal cohort.

3. **A6 calibration subjectivity.** While the three calibration anchors (A6 = 1, 3, 5) were fixed a priori, intermediate scores (A6 = 2 and 4) were assigned by the first author based on written rationales. We estimate that inter-rater agreement on A6 would be moderate (kappa approximately 0.60--0.70) based on informal consultation, but formal inter-rater reliability testing has not been conducted.

4. **Harness compatibility (B6) temporal dependency.** Harness compatibility was assessed in March 2026. The evaluation harness ecosystem evolves rapidly; benchmarks marked as "possible" integration may have been natively integrated by the time of publication.

5. **Gate-failing benchmarks with high ND.** Three benchmarks in the gate-fail set have ND scores that would rank in the top 10 if they passed the data gate: Chakraborty (ND = 83.0, Rank 25), Rao (ND = 80.0, Rank 27), and Zhou (ND = 72.0, Rank 29). These represent the most significant losses to the gate-passing set and illustrate the data bottleneck analyzed in Claim 5.
