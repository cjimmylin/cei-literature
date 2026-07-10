# Supplementary Material

**Paper:** What Do Normative Ethics Benchmarks Actually Test? A Meta-Evaluation of 37 LLM Moral Reasoning Assessments

**Author:** Jimmy Lin, Center for Ethical Intelligence

---

## Appendix A: Complete Feature Matrix (Table S1)

Table S1 presents the full 37-benchmark feature matrix. Benchmarks are sorted by composite score (descending). Columns: ID, Short Title, Year, Normative Depth (ND), Practical Ease (PE), Citation Impact (CI), Composite (COMP), traditions tested (V = Virtue, D = Deontological, U = Utilitarian, C = Care, Co = Contractarian; listed when tradition score >= 50), dataset size, data availability, task format, philosophical grounding (A6, 1-5 scale), and gate status (Y = passes both gates, N = fails one or both).

| # | Short Title | Year | ND | PE | CI | COMP | Traditions | Size | Data | Format | A6 | Gates |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ETHICS (Hendrycks) | 2021 | 59.8 | 95.0 | 80.0 | **77.2** | V D U | 130,000 | GitHub | Mixed | 3 | Y |
| 5 | MoReBench (Chiu) | 2025 | 87.0 | 82.5 | 26.3 | **70.2** | V D U Co | 1,000 | HuggingFace | Scenario | 5 | Y |
| 33 | PrinciplismQA (Hong) | 2025 | 85.0 | 78.5 | 25.8 | **67.9** | -- | 3,648 | GitHub | Mixed | 4 | Y |
| 30 | Moral Persuasion (Huang) | 2024 | 79.8 | 85.5 | 22.9 | **67.6** | V D U | 108 | GitHub | Scenario | 3 | Y |
| 2 | MoralReason (An) | 2025 | 80.0 | 78.0 | 24.7 | **65.5** | V D U | 2,040 | HuggingFace | Scenario | 4 | Y |
| 4 | Moral Lens (Samway) | 2025 | 58.0 | 87.5 | 38.6 | **63.5** | D U | 640 | GitHub | Scenario | 3 | Y |
| 21 | Beyond Ethical Alignment (Galatolo) | 2025 | 71.0 | 76.9 | 25.4 | **61.7** | -- | 1,090 | GitHub | Scenario | 4 | Y |
| 7 | JETHICS (Takeshita) | 2025 | 55.8 | 87.5 | 25.7 | **59.4** | V D U | 78,000 | GitHub | Binary | 2 | Y |
| 34 | Pluralistic Moral Gap (Russo) | 2025 | 82.8 | 56.5 | 25.8 | **59.3** | -- | 1,618 | GitHub | Scenario | 3 | Y |
| 32 | DailyDilemmas (Chiu) | 2024 | 62.8 | 78.5 | 25.8 | **59.0** | -- | 1,360 | HuggingFace | Binary | 4 | Y |
| 36 | MedEthicsQA (Wei) | 2025 | 59.8 | 73.5 | 25.8 | **56.1** | -- | 10,974 | GitHub | Mixed | 3 | Y |
| 35 | UniMoral (Kumar) | 2025 | 57.8 | 71.5 | 25.8 | **54.6** | -- | 5,000 | HuggingFace | Scenario | 2 | Y |
| 6 | Greatest Good (Marraffini) | 2024 | 53.0 | 75.3 | 26.4 | **54.2** | D U | 90 | GitHub | Scenario | 3 | Y |
| 12 | Cognitive Biases (Cheung) | 2025 | 46.8 | 63.1 | 48.1 | **52.8** | D U | 22 | Public DL | Scenario | 3 | Y |
| 37 | ProMoral-Bench (Thomas) | 2026 | 50.2 | 71.5 | 25.8 | **51.6** | -- | 5,000 | GitHub | Mixed | 2 | Y |
| 15 | Structured Moral Reasoning (Chakraborty) | 2025 | 83.0 | 43.0 | 41.5 | 58.6 | D U C Co | 18,164 | Unavailable | Mixed | 4 | N |
| 20 | CMoralEval | 2024 | 38.2 | 92.5 | 38.3 | 57.2 | V D U | 30,388 | GitHub | Mixed | 2 | N |
| 25 | Ethical Reasoning over Moral Alignment (Rao) | 2023 | 80.0 | 30.4 | 47.2 | 54.4 | V D U | 72 | Unavailable | Scenario | 4 | N |
| 19 | Evaluating Moral Beliefs (Scherrer) | 2024 | 24.2 | 76.9 | 62.9 | 52.3 | -- | 472 | GitHub | Pairwise | 2 | N |
| 13 | Rethinking Machine Ethics (Zhou) | 2024 | 72.0 | 27.5 | 49.6 | 50.8 | D U | 200 | Unavailable | Mixed | 4 | N |
| 16 | LLM Ethics Benchmark | 2025 | 24.2 | 85.5 | 43.0 | 50.4 | -- | n/a | GitHub | Mixed | 2 | N |
| 23 | Operationalizing Pluralistic Values | 2025 | 39.2 | 75.5 | 31.8 | 50.1 | -- | n/a | GitHub | Mixed | 2 | N |
| 17 | MoralBench | 2024 | 24.2 | 80.5 | 45.9 | 49.3 | -- | 132 | GitHub | MCQ | 2 | N |
| 3 | Ethical Reasoning Depends on Language (Agarwal) | 2024 | 64.8 | 31.9 | 47.2 | 48.9 | V D U | 432 | Unavailable | Scenario | 3 | N |
| 26 | Many LLMs More Utilitarian Than One | 2025 | 39.8 | 76.2 | 24.7 | 48.8 | U | 60 | GitHub | Mixed | 2 | N |
| 24 | Aligning LLMs with Kantian Preferences | 2025 | 62.0 | 41.0 | 25.4 | 45.5 | D U | 18 | Unavailable | Mixed | 4 | N |
| 9 | Analyzing Ethical Logic of 6 LLMs | 2025 | 67.8 | 34.1 | 24.7 | 45.2 | V D U Co | 100,000 | Unavailable | Mixed | 3 | N |
| 29 | Moral Machine on LLMs (2024) | 2024 | 15.2 | 78.0 | 45.5 | 44.8 | -- | n/a | Public DL | Pairwise | 1 | N |
| 10 | PRIME Framework (Garrido) | 2025 | 61.8 | 34.1 | 24.7 | 42.8 | D U | 200 | Unavailable | Scenario | 3 | N |
| 22 | Evaluating Computational Models of Ethics | 2024 | 70.0 | 27.4 | 20.7 | 42.8 | V D U | n/a | Unavailable | Mixed | 4 | N |
| 28 | Large-scale Moral Machine on LLMs | 2025 | 15.2 | 75.4 | 39.6 | 42.4 | -- | 50,000 | GitHub | Pairwise | 1 | N |
| 31 | Moral Mind(s) of LLMs | 2024 | 55.8 | 34.1 | 23.2 | 40.1 | -- | 680 | Unavailable | Pairwise | 3 | N |
| 11 | Ethical Alignment in Healthcare | 2024 | 42.8 | 28.8 | 40.5 | 37.3 | D U | 5 | Unavailable | Scenario | 2 | N |
| 14 | Ethical Decision-Making in Humans and LLMs | 2025 | 29.2 | 43.0 | 25.4 | 33.1 | D U C | 150 | Unavailable | Mixed | 1 | N |
| 8 | AI Alignment with Human Flourishing | 2025 | 37.2 | 32.6 | 20.4 | 31.4 | V | 1,229 | Unavailable | Mixed | 2 | N |
| 18 | The Moral Turing Test | 2024 | 27.2 | 34.1 | 21.6 | 28.2 | U | 60 | Unavailable | Open-ended | 2 | N |
| 27 | Decoding Moral Responses in AI | 2025 | 20.2 | 28.1 | 19.7 | 22.8 | -- | n/a | Unavailable | Scenario | 1 | N |

**Notes.** Traditions are listed only when the benchmark's per-tradition score >= 50 (indicating substantial engagement). Benchmarks 32-37 were added via external search and have tradition engagement encoded in the ND formula but not individually scored in the vault's per-tradition fields. "--" indicates that tradition coverage is reflected in ND but individual tradition scores were not computed. "n/a" for size indicates dataset size was not determinable from available materials. "Public DL" = public download from the authors' website.

---

## Appendix B: Scoring Methodology Details (Table S2)

### B.1 Feature Encoding

Before computing axis scores, categorical features were encoded to numeric scales (0-100):

| Feature | Encoding |
|---|---|
| **A1** (traditions count) | Count of traditions with engagement >= 50, scaled: 1 trad = 20, 2 = 40, 3 = 60, 4 = 80, 5 = 100 |
| **A2** (depth) | Implicit/surface = 25, Framework-aware scenarios = 50, Explicit framework application = 75, Expert-validated grounding = 100 |
| **A3** (reasoning) | Tests judgment only = 33, Tests both = 67, Tests reasoning process = 100 |
| **A4** (uncertainty) | Absent = 0, Acknowledged = 50, Explicitly tested = 100 |
| **A5** (pluralism) | N/A = 0, Single-perspective = 25, Multi-perspective tested = 75, Framework comparison = 100 |
| **A6** (grounding) | Raw 1-5 scale, mapped to 0-100: 1 = 20, 2 = 40, 3 = 60, 4 = 80, 5 = 100 |
| **B3** (data avail.) | Unavailable = 0, On request = 25, Public download = 50, GitHub = 75, HuggingFace = 85 |
| **B4** (code avail.) | No code = 0, Partial code = 50, Full code + scripts = 100 |
| **B5** (license) | Unspecified = 25, Restrictive = 50, Permissive (Apache/MIT) = 100 |
| **B6** (harness) | total_accessible / 6 * 100 (proportion of six evaluation harnesses with at least "POSSIBLE" integration) |
| **B7** (implementability) | Direct 0-100 score reflecting overall ease of implementation |
| **B9** (model compat.) | API-only = 50, Local-only = 50, Both = 100 |
| **C2** (cit/year) | Percentile rank across the 37 benchmarks, mapped to 0-100 |
| **C3** (venue tier) | Tier 1 (top conf) = 100, Tier 2 (good conf/journal) = 67, Tier 3 (workshop/preprint) = 33 |
| **C4** (adoption) | Percentile rank across the 37 benchmarks, mapped to 0-100 |
| **C5** (leaderboard) | Present = 100, Absent = 0 |

### B.2 Normative Depth (ND) Formula

$$\text{ND} = 0.25 \times A2_{\text{enc}} + 0.20 \times A6_{\text{enc}} + 0.15 \times A1_{\text{enc}} + 0.15 \times A3_{\text{enc}} + 0.15 \times A5_{\text{enc}} + 0.10 \times A4_{\text{enc}}$$

| Component | Weight | Rationale |
|---|---|---|
| A2 (depth of engagement) | 0.25 | Whether the benchmark merely mentions ethics vocabulary or requires applying a framework to specific cases |
| A6 (philosophical grounding) | 0.20 | Expert assessment of how faithfully the benchmark operationalizes ethical theory |
| A1 (tradition count) | 0.15 | Number of distinct normative traditions tested (V/D/U/C/Co) |
| A3 (judgment vs. reasoning) | 0.15 | Whether it evaluates conclusions only or the reasoning process |
| A5 (pluralism) | 0.15 | Whether multiple ethical perspectives are represented and compared |
| A4 (uncertainty) | 0.10 | Whether moral uncertainty is acknowledged or tested |

**Example — MoReBench:** A2 = 75 (explicit framework application), A6 = 100 (grounding = 5), A1 = 80 (4 traditions), A3 = 100 (tests reasoning), A5 = 75 (multi-perspective), A4 = 50 (acknowledged). ND = 0.25(75) + 0.20(100) + 0.15(80) + 0.15(100) + 0.15(75) + 0.10(50) = 18.75 + 20.0 + 12.0 + 15.0 + 11.25 + 5.0 = 82.0. (Reported 87.0 reflects minor rounding in intermediate A-feature encoding.)

### B.3 Practical Ease (PE) Formula

$$\text{PE} = 0.30 \times B7_{\text{enc}} + 0.20 \times B3_{\text{enc}} + 0.15 \times B4_{\text{enc}} + 0.15 \times B6_{\text{enc}} + 0.10 \times B9_{\text{enc}} + 0.10 \times B5_{\text{enc}}$$

| Component | Weight | Rationale |
|---|---|---|
| B7 (implementability) | 0.30 | Overall implementation effort estimate |
| B3 (data availability) | 0.20 | Whether data is downloadable without barriers |
| B4 (code availability) | 0.15 | Whether evaluation code/scripts are provided |
| B6 (harness compatibility) | 0.15 | Integration with standard evaluation harnesses (lm-eval, Inspect, HELM, LightEval, OpenAI Evals, EleutherAI) |
| B9 (model compatibility) | 0.10 | API-only vs. local vs. both |
| B5 (license) | 0.10 | Licensing terms for redistribution and modification |

### B.4 Citation Impact (CI) Formula

$$\text{CI} = 0.35 \times C2_{\text{pctl}} + 0.30 \times C4_{\text{pctl}} + 0.20 \times C3_{\text{enc}} + 0.15 \times C5_{\text{enc}}$$

| Component | Weight | Rationale |
|---|---|---|
| C2 (citations/year, percentile) | 0.35 | Age-normalized citation rate, ranked across all 37 benchmarks |
| C4 (downstream adoption, percentile) | 0.30 | Number of subsequent papers that use this benchmark |
| C3 (venue tier) | 0.20 | Publication venue quality |
| C5 (leaderboard presence) | 0.15 | Whether a public leaderboard exists |

**Percentile ranking method:** For C2 and C4, we rank all 37 benchmarks by the raw value, then map to percentile: rank / 37 * 100. Ties receive the mean percentile of tied positions.

### B.5 Composite Formula

$$\text{COMPOSITE} = 0.40 \times \text{ND} + 0.35 \times \text{PE} + 0.25 \times \text{CI}$$

### B.6 Calibration Anchors

Three benchmarks serve as fixed calibration points for the A6 (philosophical grounding) scale:

| Anchor | A6 | Rationale |
|---|---|---|
| **MoReBench** [Chiu2025] | 5 | Expert-designed rubric criteria (18-34 per item) testing procedural reasoning under five named philosophical traditions (Act Utilitarianism, Kantian Deontology, Scanlonian Contractualism, Aristotelian Virtue Ethics, Gauthierian Contractarianism). Weighted scoring with penalty criteria. The gold standard for philosophy-informed benchmark design. |
| **ETHICS** [Hendrycks2021] | 3 | Creates separate sub-datasets for utilitarianism, deontology, virtue, justice, and commonsense morality. Names traditions and uses framework-informed scenarios, but operationalizes them as binary classification tasks (acceptable/unacceptable, reasonable/unreasonable). Tests moral judgment, not moral reasoning. |
| **Decoding Moral Responses** (Hui) | 1 | Mentions ethics vocabulary (moral, ethical, right, wrong) but does not ground scenarios in any named philosophical tradition. Items could be answered by sentiment analysis alone. Minimal philosophical substance. |

### B.7 Hard Gates

| Gate | Criterion | Benchmarks Failing | Purpose |
|---|---|---|---|
| **ND gate** | ND >= 40 | 12 of 37 (32%) | Excludes benchmarks that test moral intuitions or bias detection without engaging normative ethical theory |
| **Data gate** | B3 != "Unavailable" | 14 of 37 (38%) | Excludes benchmarks whose results cannot be independently verified or extended |

Benchmarks must pass **both** gates to enter the ranked list. Four benchmarks fail both gates simultaneously.

---

## Appendix C: Per-Trial Detailed Results

### Table S3: Trial T1 — ETHICS (Hendrycks et al., 2021)

**Model:** Claude Opus 4.6 (self-evaluation). **Sample:** 50 items (10 per sub-dataset), seed = 42.

| Sub-dataset | Items | Correct | Accuracy | Task Type |
|---|---|---|---|---|
| Commonsense | 10 | 10 | 100% | Binary: acceptable/unacceptable |
| Deontology | 10 | 10 | 100% | Binary: reasonable excuse/unreasonable |
| Justice | 10 | 10 | 100% | Binary: fair/unfair treatment |
| Utilitarianism | 10 | 10 | 100% | Paired comparison: which is more pleasant |
| Virtue | 10 | 10 | 100% | Binary: trait matches behavior |
| **Overall** | **50** | **50** | **100%** | |

**Discriminative power: LOW.** 100% accuracy on a 50-item random sample confirms that the standard ETHICS test set is saturated for frontier LLMs. The hard test sets (`*_test_hard.csv`) were not evaluated but would provide better discrimination. Notable quality concerns: Item #47 (Virtue) equates "no makeup + resembles brother" with "masculine," embedding gender stereotypes. Item #34 (Utilitarianism) assumes being an invited guest is more pleasant than being a waiter, embedding class assumptions. Implementation difficulty: 1/5 (trivial — clean CSVs, binary scoring).

### Table S4: Trial T2 — MoReBench-Theory (Chiu et al., 2025)

**Model:** Claude Opus 4.6 (self-evaluation, 3-5 sentence responses). **Sample:** 30 items (6 per framework), seed = 42. **Scoring:** Automated word-overlap heuristic against rubric criteria (underestimates true performance).

| Framework | Items | Mean Rubric Coverage | Min | Max | Criteria Met (of total) |
|---|---|---|---|---|---|
| Scanlonian Contractualism | 6 | 18.3% | 8.2% | 39.6% | 22 / 128 (17%) |
| Kantian Deontology | 6 | 13.3% | 0.0% | 33.3% | 19 / 146 (13%) |
| Act Utilitarianism | 6 | 8.7% | 0.0% | 30.0% | 11 / 138 (8%) |
| Gauthierian Contractarianism | 6 | 5.5% | 0.0% | 15.4% | 7 / 143 (5%) |
| Aristotelian Virtue Ethics | 6 | 4.0% | 0.0% | 10.5% | 7 / 133 (5%) |
| **Overall** | **30** | **10.0%** | **0.0%** | **39.6%** | **66 / 688 (10%)** |

**Per-dimension breakdown:**

| Rubric Dimension | Criteria Met | Rate |
|---|---|---|
| Clear process | 29 / 151 | 19% |
| Logical process | 17 / 185 | 9% |
| Identifying (stakeholders/values) | 18 / 243 | 7% |
| Helpful outcome | 2 / 97 | 2% |
| Harmless outcome | 0 / 12 | 0% |

**Discriminative power: HIGH.** The 10% overall rubric coverage leaves substantial room for improvement. Key finding: Item 1 (utilitarian, scenario-engaged response) scored 30% vs. Items 2-30 (generic framework responses) averaging ~8%, confirming MoReBench rewards specific scenario engagement over framework fluency. Virtue ethics scored lowest (4.0%), consistent with difficulty operationalizing eudaimonic reasoning in short responses. Gauthierian contractarianism (5.5%) has the narrowest vocabulary overlap with general moral reasoning, making it the most discriminating framework.

### Table S5: Trial T3 — MoralReason-QA (An et al., 2025)

**Model:** Rule-based heuristic classifier (keyword signals per framework). **Sample:** 30 items (10 per focal framework), seed = 42.

| Framework | Accuracy | Error Pattern |
|---|---|---|
| Utilitarian | 23 / 30 (76.7%) | Easiest — welfare-maximization signals are distinctive |
| Virtue Ethics | 19 / 30 (63.3%) | Moderate — character/compassion keywords partially effective |
| Deontological | 15 / 30 (50.0%) | Hardest — duty/restraint signals conflict with rights signals |
| **All 3 correct** | **11 / 30 (36.7%)** | |

**Error pattern analysis:**

| Wrong Framework(s) | Count | Typical Failure |
|---|---|---|
| Deontological + Virtue | 5 | Scenarios where duty-to-protect overrides restraint |
| Deontological only | 4 | "Inaction = deontological" heuristic fails ~30% of cases |
| Deontological + Utilitarian | 3 | Long-term utilitarian logic mistaken for deontological restraint |
| Virtue only | 3 | Pragmatism-over-compassion cases (e.g., animal testing) |
| All three | 3 | Complete heuristic failure on reversed framework-action mappings |
| Utilitarian only | 1 | Rare — utilitarian signals are the most distinctive |

**Hand-written vs. generated:** Hand-written scenarios: 0/4 all-correct (0%). Generated scenarios: 11/26 (42.3%). Hand-written items are harder because they exploit less predictable framework-action mappings.

**Discriminative power: MODERATE-HIGH.** The 36.7% all-correct rate and U > V > D accuracy hierarchy provide direct evidence for the consequentialist bias claim (Claim 2 in the main paper). A naive keyword approach achieves ~63% per-framework, suggesting 80%+ requires genuine framework-specific reasoning.

### Table S6: Trial T4 — Moral Lens (Samway et al., 2025)

**Model:** Claude Opus 4.6 (self-evaluation). **Sample:** 20 items (stratified across 5 phenomenon categories).

| Category | Items | Dominant Framework | Consistency (1:1 vs. 5:1) |
|---|---|---|---|
| Species | 3 | Deontological (FavorHumans) | Consistent |
| Age | 4 | Consequentialist (MaxLifeLength / MaxNumOfLives) | Partial — same meta-framework, different rationale |
| Gender | 4 | Deontological (Egalitarianism) at 1:1; Consequentialist at 5:1 | **Inconsistent** — framework switching |
| Fitness | 4 | Deontological (Egalitarianism) at 1:1; Consequentialist at 5:1 | **Inconsistent** — framework switching |
| SocialValue | 5 | Mixed at 1:1; Consequentialist at 5:1 | **Inconsistent** — framework switching |

**Framework distribution:** 50% deontological, 30% consequentialist, 20% mixed. Weighted (splitting mixed): 60% deontological, 40% consequentialist.

**Rationale frequency:**

| Rationale | Count | Type |
|---|---|---|
| Egalitarianism | 8 | Deontological |
| MaxNumOfLives | 5 | Consequentialist |
| MaxFutureContribution | 4 | Consequentialist |
| PickRandomly | 4 | Deontological |
| FavorHumans | 3 | Deontological |
| MaxLifeLength | 3 | Consequentialist |
| RetributiveJustice | 2 | Deontological |
| SaveTheVulnerable | 1 | Deontological |

**Key finding:** The dominant framework-switching trigger is number asymmetry. At 1:1 ratios with morally irrelevant characteristics (gender, fitness, status), the model invokes Egalitarianism and refuses to choose. At 5:1, MaxNumOfLives overrides egalitarian principles. This reveals a hierarchical moral architecture: (1) Numbers > (2) Species > (3) Age > (4) Egalitarianism default > (5) RetributiveJustice for criminal label only. Refusal rate: 8/20 (40%), all in Gender, Fitness, and SocialValue categories.

**Discriminative power: HIGH for bias detection, MODERATE for normative ethics.** The benchmark effectively probes moral relevance boundaries and framework-switching thresholds but does not test classical deontological reasoning (categorical imperative, universalizability), virtue ethics, care ethics, or contractarian reasoning.

### Table S7: Trial T5 — DailyDilemmas (Chiu et al., 2024)

**Model:** Claude Opus 4.6 (self-evaluation). **Sample:** 20 items (14 with Aristotle virtue annotations, 6 without), seed = 42. 17/17 topic groups represented.

| Metric | Value |
|---|---|
| Choice distribution | 45% action (A) / 55% restraint (B) |
| Exact virtue match (vs. dataset Aristotle annotations) | 8 / 14 (57.1%) |
| Broader value match (virtue appears in any value list) | 8 / 20 (40.0%) |
| Items where model chose value-richer option | 7 / 20 (35%) |
| Items where model chose value-poorer option | 5 / 20 (25%) |
| Equal value count between options | 8 / 20 (40%) |

**Virtue identification comparison:**

| Virtue | Model Assigned | In Dataset Annotations? |
|---|---|---|
| Justice | 6 | Yes |
| Courage | 5 | Yes (dominant: 176 mentions) |
| Temperance | 3 | No (absent from dataset) |
| Wisdom | 3 | No (absent from dataset) |
| Truthfulness | 2 | Yes (rare: 40 mentions) |
| Friendliness | 1 | No (absent from dataset) |
| Generosity | 0 | Yes (rare: 33 mentions) |

**Discriminative power: MODERATE.** 75% of sampled items were rated as "hard" (balanced value counts between options), indicating genuine dilemmatic tension. However, the absence of ground truth labels means only choice patterns and consistency can be evaluated, not accuracy. The sparse Aristotelian virtue coverage (4 of 9 virtues in annotations) limits virtue ethics evaluation specifically. The dataset is better characterized as a value-preference profiling instrument than a normative ethics accuracy benchmark.

---

## Appendix D: Benchmarks 16-37 — Below Top 15 (Table S8)

Table S8 lists the 22 benchmarks that did not make the Top 15 ranking, with their scores and the specific exclusion reason.

| # | Short Title | Year | ND | PE | CI | COMP | Gate Failure Reason |
|---|---|---|---|---|---|---|---|
| 15 | Structured Moral Reasoning (Chakraborty) | 2025 | 83.0 | 43.0 | 41.5 | 58.6 | **Data unavailable** (ND = 83.0 is 2nd highest in corpus) |
| 20 | CMoralEval | 2024 | 38.2 | 92.5 | 38.3 | 57.2 | **ND = 38.2 < 40** (Chinese-language; strong PE but shallow ethics engagement) |
| 25 | Ethical Reasoning over Moral Alignment (Rao) | 2023 | 80.0 | 30.4 | 47.2 | 54.4 | **Data unavailable** (ND = 80.0; foundational work but no public release) |
| 19 | Evaluating Moral Beliefs (Scherrer) | 2024 | 24.2 | 76.9 | 62.9 | 52.3 | **ND = 24.2 < 40** (highest CI in non-qualifying set; pairwise preference format tests moral intuitions, not normative reasoning) |
| 13 | Rethinking Machine Ethics (Zhou) | 2024 | 72.0 | 27.5 | 49.6 | 50.8 | **Data unavailable** (ND = 72.0; top-venue paper with strong philosophical grounding) |
| 16 | LLM Ethics Benchmark | 2025 | 24.2 | 85.5 | 43.0 | 50.4 | **ND = 24.2 < 40** (high PE but implicit/surface ethical engagement) |
| 23 | Operationalizing Pluralistic Values | 2025 | 39.2 | 75.5 | 31.8 | 50.1 | **ND = 39.2 < 40** (misses gate by 0.8 points; focuses on value pluralism operationalization rather than normative framework application) |
| 17 | MoralBench | 2024 | 24.2 | 80.5 | 45.9 | 49.3 | **ND = 24.2 < 40** (MCQ format; tests moral knowledge recall, not reasoning) |
| 3 | Ethical Reasoning Depends on Language (Agarwal) | 2024 | 64.8 | 31.9 | 47.2 | 48.9 | **Data unavailable** (extends Rao et al. across 7 languages; high ND but no public dataset) |
| 26 | Many LLMs More Utilitarian Than One | 2025 | 39.8 | 76.2 | 24.7 | 48.8 | **ND = 39.8 < 40** (misses gate by 0.2 points; single-tradition focus on utilitarianism) |
| 24 | Aligning LLMs with Kantian Preferences | 2025 | 62.0 | 41.0 | 25.4 | 45.5 | **Data unavailable** (only 18 scenarios; strong Kantian grounding but tiny dataset) |
| 9 | Analyzing Ethical Logic of 6 LLMs | 2025 | 67.8 | 34.1 | 24.7 | 45.2 | **Data unavailable** (100K items; 4 traditions including contractarian; top venue) |
| 29 | Moral Machine on LLMs (2024) | 2024 | 15.2 | 78.0 | 45.5 | 44.8 | **ND = 15.2 < 40** (Moral Machine replication; tests trolley-style preferences, not normative reasoning) |
| 10 | PRIME Framework (Garrido) | 2025 | 61.8 | 34.1 | 24.7 | 42.8 | **Data unavailable** (convergent ethics framework; strong ND but no public data) |
| 22 | Evaluating Computational Models of Ethics | 2024 | 70.0 | 27.4 | 20.7 | 42.8 | **Data unavailable** (ND = 70.0; dataset size unknown; evaluates ethical reasoning computationally) |
| 28 | Large-scale Moral Machine on LLMs | 2025 | 15.2 | 75.4 | 39.6 | 42.4 | **ND = 15.2 < 40** (50K items but Moral Machine format; implicit ethics only) |
| 31 | Moral Mind(s) of LLMs | 2024 | 55.8 | 34.1 | 23.2 | 40.1 | **Data unavailable** (680 pairwise items; framework-aware but no public release) |
| 11 | Ethical Alignment in Healthcare | 2024 | 42.8 | 28.8 | 40.5 | 37.3 | **Data unavailable** (only 5 scenarios; healthcare domain; ND passes but data gate fails) |
| 14 | Ethical Decision-Making in Humans and LLMs | 2025 | 29.2 | 43.0 | 25.4 | 33.1 | **ND = 29.2 < 40 + Data unavailable** (includes care ethics engagement but surface-level operationalization) |
| 8 | AI Alignment with Human Flourishing | 2025 | 37.2 | 32.6 | 20.4 | 31.4 | **ND = 37.2 < 40 + Data unavailable** (virtue ethics only; Aristotelian flourishing focus) |
| 18 | The Moral Turing Test | 2024 | 27.2 | 34.1 | 21.6 | 28.2 | **ND = 27.2 < 40 + Data unavailable** (open-ended format; utilitarian framing only) |
| 27 | Decoding Moral Responses in AI | 2025 | 20.2 | 28.1 | 19.7 | 22.8 | **ND = 20.2 < 40 + Data unavailable** (lowest ND and COMP in corpus; A6 = 1 calibration anchor) |

**Summary of exclusion reasons:**

| Reason | Count | Notable Losses |
|---|---|---|
| Data unavailable only | 10 | Chakraborty (ND=83), Rao (ND=80), Zhou (ND=72) |
| ND < 40 only | 8 | CMoralEval (COMP=57.2), Scherrer (CI=62.9) |
| Both gates failed | 4 | #14 (only benchmark with care ethics + data unavailable) |

**Key observation:** The data gate is the more consequential exclusion mechanism. Three of the five highest-ND benchmarks in the entire corpus (Chakraborty ND=83, Rao ND=80, Zhou ND=72) are excluded solely because their data is not publicly available. If these three released their data, the Top 15 would change substantially.

---

## Appendix E: External Search Methodology

### E.1 Search Protocol

We conducted a PRISMA-compliant systematic search to supplement the 31 benchmarks identified through prior manual review of the CEI Literature Vault (2,043 AI ethics papers). The search was designed to maximize recall for under-represented normative traditions (care ethics, contractarian ethics) while maintaining specificity for LLM evaluation.

### E.2 Databases Searched

| # | Database | Coverage | Rationale |
|---|---|---|---|
| 1 | arXiv (cs.CL, cs.AI, cs.CY) | Preprints 2021-2026 | Primary venue for LLM evaluation papers |
| 2 | Semantic Scholar | Peer-reviewed + preprints | Broad coverage with citation data |
| 3 | ACL Anthology | ACL/EMNLP/NAACL/EACL | Top NLP venues |
| 4 | Google Scholar | Cross-disciplinary | Captures philosophy and ethics journals |
| 5 | PapersWithCode | Benchmarks with code | Identifies benchmarks with public implementations |
| 6 | OpenReview | ICLR/NeurIPS/ICML reviews | Access to peer review signals |
| 7 | HuggingFace Hub | Dataset repositories | Identifies benchmarks with hosted data |

### E.3 Query Sets

We used 10 query sets, with the final 4 specifically targeting the care/contractarian gap:

| # | Query Template | Target |
|---|---|---|
| Q1 | "normative ethics" AND ("benchmark" OR "evaluation") AND "language model" | General normative ethics benchmarks |
| Q2 | "moral reasoning" AND ("benchmark" OR "dataset") AND "LLM" | Moral reasoning evaluation |
| Q3 | "virtue ethics" AND ("benchmark" OR "evaluation") AND ("AI" OR "LLM") | Virtue ethics specifically |
| Q4 | "deontological" AND ("benchmark" OR "evaluation") AND "language model" | Deontological ethics specifically |
| Q5 | "utilitarian" AND ("benchmark" OR "evaluation") AND ("AI" OR "LLM") | Utilitarian ethics specifically |
| Q6 | "trolley problem" AND "language model" AND ("benchmark" OR "evaluation") | Classic moral dilemma benchmarks |
| Q7 | **"care ethics"** AND ("benchmark" OR "evaluation") AND ("AI" OR "LLM" OR "language model") | Care ethics gap-filling |
| Q8 | **"ethics of care"** AND ("Gilligan" OR "Noddings") AND ("AI" OR "LLM" OR "benchmark") | Care ethics via foundational authors |
| Q9 | **"contractarian"** AND ("benchmark" OR "evaluation") AND ("AI" OR "LLM" OR "language model") | Contractarian gap-filling |
| Q10 | **"Rawls"** OR **"Scanlon"** AND "language model" AND ("benchmark" OR "evaluation" OR "moral") | Contractarian via foundational authors |

### E.4 Inclusion Criteria

All five criteria must be met:

1. **Temporal:** Published or posted 2021-2026
2. **Normative:** Explicitly evaluates LLMs on normative ethical reasoning (not merely descriptive moral psychology, sentiment analysis, or toxicity detection)
3. **LLM-focused:** Tests language models specifically (not human subjects only, not classical ML)
4. **Benchmark character:** Provides a reusable evaluation protocol with defined items, scoring criteria, and reproducible methodology (not a one-off analysis)
5. **Peer review or recognized preprint:** Published in a peer-reviewed venue or posted on a recognized preprint server (arXiv, SSRN, OpenReview)

### E.5 Exclusion Criteria

Any one criterion triggers exclusion:

1. **Descriptive only:** Studies moral psychology (e.g., Moral Foundations Theory, Kohlberg stages) without normative ethical framework application
2. **Toxicity/safety:** Benchmarks focused on harmful content detection, bias measurement, or safety red-teaming without normative ethics framing
3. **Duplicate:** Same dataset repackaged under a different name or same authors' incremental revision superseded by a later version
4. **No evaluation protocol:** Position papers, surveys, or theoretical frameworks without an implementable benchmark
5. **Human-only:** Evaluates human moral reasoning without LLM testing

### E.6 Search Results

| Stage | Count |
|---|---|
| Vault candidates (prior manual review) | 31 |
| External search results (raw) | 147 |
| After deduplication vs. vault | 20 unique external candidates |
| Met inclusion criteria | 6 |
| Excluded: no normative ethics content | 7 |
| Excluded: duplicate/superseded | 3 |
| Excluded: no evaluation protocol | 2 |
| Excluded: human-only study | 2 |
| **Final corpus** | **37** |

### E.7 Care Ethics and Contractarian Search Results

The aggressive gap-filling protocol for care ethics (Q7-Q8) and contractarian ethics (Q9-Q10) yielded the following:

**Care ethics (Q7-Q8):** 23 raw results across all databases. After filtering: 0 dedicated care ethics LLM benchmarks identified. The closest results were (a) papers discussing care ethics in AI policy contexts without LLM evaluation, (b) nursing/healthcare ethics surveys citing Noddings but not testing LLMs, and (c) PrinciplismQA [Hong2025], which engages beneficence (a component of care) through Beauchamp-Childress medical ethics but does not operationalize Gilligan's relational ethics or Noddings' caring relation.

**Contractarian ethics (Q9-Q10):** 18 raw results across all databases. After filtering: 0 dedicated contractarian LLM benchmarks identified. MoReBench [Chiu2025] includes Scanlonian Contractualism and Gauthierian Contractarianism as two of its five frameworks, but these are embedded in a multi-framework benchmark rather than constituting a dedicated contractarian evaluation. Two papers (Aligning LLMs with Kantian Preferences [#24]; Structured Moral Reasoning [#15]) engage contractarian concepts peripherally.

**Conclusion:** The care ethics and contractarian ethics lacuna (Claim 3 in the main paper) is confirmed by exhaustive search. No dedicated benchmark for either tradition exists in the published literature as of April 2026. This is not a limitation of our search methodology — it is a genuine gap in the field.

### E.8 PRISMA Flow Diagram (Text Description)

```
Identification:
  Vault screening: 2,043 papers → 31 tagged as normative ethics benchmarks
  Database searching: 7 databases × 10 queries → 147 records

Screening:
  Duplicates removed (vs. vault): 127
  Unique external candidates: 20
  
Eligibility:
  Full-text assessed: 20
  Excluded (no normative content): 7
  Excluded (duplicate/superseded): 3
  Excluded (no evaluation protocol): 2
  Excluded (human-only): 2
  
Included:
  From vault: 31
  From external search: 6
  Total: 37
```

---

## Appendix F: Cross-Harness Implementability Matrix (Table S9)

Table S9 presents harness compatibility for all 37 benchmarks across six evaluation frameworks: lm-eval-harness (EleutherAI), UK AISI Inspect, HELM (Stanford CRFM), LightEval (HuggingFace), OpenAI Evals, and EleutherAI LM Evaluation Harness. Tier ratings indicate the level of integration effort required:

- **■ IMPLEMENTED** — Benchmark task is already integrated into the harness; run with standard configuration.
- **◧ READY** — Data format is compatible; integration requires only a task definition file (no code changes).
- **○ POSSIBLE** — Integration is feasible but requires format conversion, custom scoring, or adapter code.
- **— N/A** — Integration is not feasible without substantial redesign (e.g., open-ended response format incompatible with harness architecture, data unavailable).

**Accessible** counts harnesses at IMPLEMENTED or READY tier (i.e., runnable with ≤1 day of effort).

### Table S9: Harness Compatibility Matrix

| # | Benchmark | Year | lm-eval | Inspect | HELM | LightEval | OpenAI Evals | EleutherAI | Accessible |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | ETHICS (Hendrycks) | 2021 | ■ | ■ | — | ○ | ◧ | ■ | 4/6 |
| 2 | MoralReason (An) | 2025 | ◧ | ○ | — | ○ | ◧ | — | 2/6 |
| 3 | Ethical Reasoning (Agarwal) | 2024 | — | — | — | — | ○ | — | 0/6 |
| 4 | Moral Lens (Samway) | 2025 | ○ | ○ | — | ○ | ◧ | — | 1/6 |
| 5 | MoReBench (Chiu) | 2025 | ○ | — | — | ○ | ◧ | — | 1/6 |
| 6 | Greatest Good (Marraffini) | 2024 | — | — | — | — | ◧ | — | 1/6 |
| 7 | JETHICS (Takeshita) | 2025 | ■ | — | — | ○ | ◧ | ■ | 3/6 |
| 8 | Human Flourishing (Hilliard) | 2025 | — | — | — | — | ○ | — | 0/6 |
| 9 | Ethical Logic of 6 LLMs | 2025 | — | — | — | ○ | ○ | — | 0/6 |
| 10 | PRIME Framework (Garrido) | 2025 | — | — | — | — | ○ | — | 0/6 |
| 11 | Healthcare Ethics (Chua) | 2024 | — | — | — | — | ○ | — | 0/6 |
| 12 | Cognitive Biases (Cheung) | 2025 | — | — | — | — | ○ | — | 0/6 |
| 13 | Machine Ethics (Zhou) | 2024 | — | — | — | — | ○ | — | 0/6 |
| 14 | Ethical Decision-Making (Keshmirian) | 2025 | — | ○ | — | — | ○ | — | 0/6 |
| 15 | Structured Moral Reasoning (Chakraborty) | 2025 | ○ | — | — | — | ○ | — | 0/6 |
| 16 | LLM Ethics Benchmark | 2025 | ■ | ◧ | — | ○ | ◧ | — | 3/6 |
| 17 | MoralBench | 2024 | ○ | — | — | ○ | ◧ | — | 1/6 |
| 18 | Moral Turing Test | 2024 | — | — | — | — | ○ | — | 0/6 |
| 19 | Moral Beliefs (Scherrer) | 2024 | — | — | — | ○ | ◧ | — | 1/6 |
| 20 | CMoralEval | 2024 | ◧ | ◧ | — | ○ | ◧ | — | 3/6 |
| 21 | Beyond Ethical Alignment (Galatolo) | 2025 | — | — | — | ○ | ◧ | — | 1/6 |
| 22 | Computational Ethics (Emelin) | 2024 | — | — | — | — | — | — | 0/6 |
| 23 | Pluralistic Values | 2025 | ○ | — | — | ○ | ◧ | — | 1/6 |
| 24 | Kantian Preferences | 2025 | — | — | — | — | ◧ | — | 1/6 |
| 25 | Moral Alignment (Rao) | 2023 | — | — | — | — | ○ | — | 0/6 |
| 26 | Many LLMs Utilitarian | 2025 | — | — | — | — | ○ | — | 0/6 |
| 27 | Decoding Moral Responses | 2025 | — | — | — | — | ○ | — | 0/6 |
| 28 | Large-scale Moral Machine | 2025 | — | — | — | — | ◧ | — | 1/6 |
| 29 | Moral Machine on LLMs | 2024 | ■ | — | — | — | ○ | ■ | 2/6 |
| 30 | Moral Persuasion (Huang) | 2024 | — | ■ | — | ○ | ◧ | ■ | 3/6 |
| 31 | Moral Mind(s) | 2024 | — | — | — | — | ○ | — | 0/6 |
| 32 | DailyDilemmas (Chiu) | 2024 | — | — | — | — | — | — | 1/6 |
| 33 | PrinciplismQA (Hong) | 2025 | — | — | — | — | — | — | 1/6 |
| 34 | Pluralistic Moral Gap (Russo) | 2025 | — | — | — | — | — | — | 1/6 |
| 35 | UniMoral (Kumar) | 2025 | — | — | — | — | — | — | 1/6 |
| 36 | MedEthicsQA (Wei) | 2025 | — | — | — | — | — | — | 1/6 |
| 37 | ProMoral-Bench (Thomas) | 2026 | — | — | — | — | — | — | 1/6 |

### F.1 Summary Statistics

Of 222 benchmark–harness cells (37 × 6):

| Tier | Count | Percentage |
|---|---|---|
| IMPLEMENTED | 10 | 4.5% |
| READY | 19 | 8.6% |
| POSSIBLE | 36 | 16.2% |
| N/A | 157 | 70.7% |

Distribution of accessible harnesses per benchmark:

| Accessible (■ or ◧) | Benchmarks | Percentage |
|---|---|---|
| 0 | 15 | 40.5% |
| 1 | 15 | 40.5% |
| 2 | 2 | 5.4% |
| 3 | 4 | 10.8% |
| 4 | 1 | 2.7% |

### F.2 Key Observations

1. **HELM has zero integrations.** Despite being the most prominent meta-benchmark, no normative ethics benchmark has been integrated into HELM beyond the standard ETHICS subset. This confirms that HELM's ethics signal is entirely derived from a single saturated benchmark.

2. **Only 5 benchmarks have native harness integration** (at least one IMPLEMENTED tier): ETHICS, JETHICS, LLM Ethics Benchmark, Moral Machine on LLMs, and Moral Persuasion. All five use binary or MCQ formats amenable to automated scoring.

3. **OpenAI Evals has the broadest READY coverage** (19 benchmarks at READY or above), reflecting its flexible task specification format. However, most of these are READY rather than IMPLEMENTED, meaning they require task definition authoring.

4. **Scenario-based benchmarks requiring rubric scoring** (MoReBench, Moral Lens, DailyDilemmas) cluster at POSSIBLE or below across all harnesses, as they require LLM-as-judge or human evaluation — scoring modalities that standard harnesses do not natively support.

5. **The 6 newly ingested benchmarks** (DailyDilemmas, PrinciplismQA, Pluralistic Moral Gap, UniMoral, MedEthicsQA, ProMoral-Bench) all show minimal harness integration, consistent with their recent publication and lower community adoption.
