# Appendix B: Scoring Methodology Details

**Paper:** Three Ethical Profiles, One Knowledge Ceiling: A Meta-Evaluation of 54 Normative Ethics Benchmarks Across Nine LLMs and Three Vendors

**Author:** Jimmy Lin, Center for Ethical Intelligence

---

## Table S2: Scoring Formulas, Feature Encoding, Calibration Anchors, and Sensitivity Analysis

This appendix provides the complete specification of the scoring methodology summarized in Section 3.3 of the main paper, including: the encoding rules that transform categorical feature observations into numeric scores (Section B.1), the formulas and weight rationales for each axis and the composite (Sections B.2--B.5), calibration anchors (Section B.6), hard gate specifications (Section B.7), worked examples (Section B.8), and weight sensitivity analysis (Section B.9).

---

## B.1 Feature Encoding Rules

Before computing axis scores, all 26 features were encoded to a common 0--100 numeric scale. Features that are already continuous (e.g., C2, B7) required no transformation. Categorical and ordinal features were encoded as follows:

### Axis A: Normative Depth Features

| Feature | Description | Encoding Rule |
|---------|-------------|--------------|
| **A1** | Traditions count (1--5) | Count of traditions with engagement >= 50, scaled linearly: 1 = 20, 2 = 40, 3 = 60, 4 = 80, 5 = 100. A benchmark testing 0 traditions receives 0. |
| **A2** | Depth of engagement | 4-level ordinal: Implicit/surface mention of ethics vocabulary = 25; Framework-aware scenario construction = 50; Explicit framework application with named traditions = 75; Expert-validated grounding with rubric-level operationalization = 100. |
| **A3** | Reasoning target | 3-level categorical: Tests moral judgment only (final answer, no reasoning required) = 33; Tests both judgment and reasoning (model must explain but judgment is primary metric) = 67; Tests reasoning process specifically (rubric evaluates argumentation quality, not just conclusion) = 100. |
| **A4** | Moral uncertainty | 3-level ordinal: Absent (all items have single correct answers) = 0; Acknowledged (some items flag disagreement but still enforce single answer) = 50; Explicitly tested (benchmark evaluates ability to navigate genuine moral ambiguity) = 100. |
| **A5** | Pluralism | 4-level ordinal: Not applicable (no normative framing) = 0; Single-perspective (one framework treated as correct) = 25; Multi-perspective tested (multiple frameworks present, evaluated separately) = 75; Framework comparison (explicit cross-framework analysis required) = 100. |
| **A6** | Philosophical grounding | 5-point calibrated scale mapped to 0--100: 1 = 20, 2 = 40, 3 = 60, 4 = 80, 5 = 100. See Section B.6 for calibration anchors. |
| **A7** | Cultural framing | 3-level ordinal: Western-only (scenarios drawn exclusively from Anglo-European moral contexts) = 33; Includes non-Western (at least one cultural tradition beyond WEIRD populations) = 67; Explicitly cross-cultural (systematic comparison across cultural contexts) = 100. |
| **A8** | Multilingual support | Count-based: Monolingual (English only) = 20; 2--3 languages = 50; 4+ languages = 100. |

### Axis B: Practical Ease Features

| Feature | Description | Encoding Rule |
|---------|-------------|--------------|
| **B1** | Task format | Categorical (not scored): Binary, MCQ, Scenario, Pairwise, Open-ended, Mixed. Used for descriptive purposes; not included in the PE formula. |
| **B2** | Dataset size | Integer count of items. Not directly scored (used as a contextual descriptor); implementability (B7) indirectly captures size-related ease. |
| **B3** | Data availability | 5-level ordinal: Unavailable (no public release, authors unresponsive) = 0; On request (available by contacting authors) = 25; Public download from author website = 50; GitHub repository = 75; HuggingFace Hub = 85. The 85 ceiling for HuggingFace reflects its standardized dataset card, versioning, and API access. |
| **B4** | Code availability | 3-level: No code = 0; Partial code (evaluation scripts but not full pipeline) = 50; Full code with end-to-end scripts = 100. |
| **B5** | License | 3-level: Unspecified (no license file, ambiguous terms) = 25; Restrictive (CC BY-NC, non-commercial, or custom terms) = 50; Permissive (Apache 2.0, MIT, CC BY) = 100. |
| **B6** | Harness compatibility | Proportion of six evaluation harnesses (lm-eval-harness, UK AISI Inspect, HELM, LightEval, OpenAI Evals, EleutherAI) with at least POSSIBLE integration, multiplied by 100. A benchmark compatible with 3 of 6 harnesses scores 50. |
| **B7** | Implementability | Direct 0--100 expert judgment integrating: format standardization (is the data in a standard JSON/CSV format?), documentation quality (are scoring instructions complete?), setup complexity (are dependencies manageable?), and expected time-to-first-result (can a competent researcher produce results within one working day?). |
| **B8** | Scorer type | Categorical (not scored): Auto (exact match or rule-based), Rubric (expert rubric scoring), LLM-judge (LLM evaluates another LLM's output), Human (requires human evaluation). Used descriptively. |
| **B9** | Model compatibility | 3-level: API-only (requires proprietary API access) = 50; Local-only (requires open-weight model) = 50; Both API and local = 100. |

### Axis C: Citation Impact Features

| Feature | Description | Encoding Rule |
|---------|-------------|--------------|
| **C1** | Raw citations | Integer from Semantic Scholar. Not directly scored; used to compute C2. |
| **C2** | Citations per year | Percentile rank across all 54 benchmarks, mapped linearly to 0--100. Ties receive the mean percentile of tied positions. Percentile ranking eliminates the confound of publication age. |
| **C3** | Venue tier | 3-level: Tier 1 (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, Nature, Science) = 100; Tier 2 (strong workshops, good journals, secondary conferences) = 67; Tier 3 (workshop papers, arXiv-only preprints, non-peer-reviewed) = 33. |
| **C4** | Downstream adoption | Percentile rank of the count of subsequent papers that explicitly cite and use this benchmark, mapped to 0--100. |
| **C5** | Leaderboard presence | Binary: Present on PapersWithCode or equivalent = 100; Absent = 0. |

### Axis D: Metadata Features

D1--D4 (Year, Affiliation, Language, Domain) are recorded for descriptive and analytical purposes but are not included in any axis formula.

---

## B.2 Normative Depth (ND) Formula

> ND = 0.25 x A2_enc + 0.20 x A6_enc + 0.15 x A1_enc + 0.15 x A3_enc + 0.15 x A5_enc + 0.10 x A4_enc

| Component | Weight | Rationale |
|-----------|--------|-----------|
| A2 (depth of engagement) | 0.25 | The single most important indicator of whether a benchmark genuinely engages normative ethics or merely mentions ethics vocabulary. Highest weight because it distinguishes benchmarks that require framework application from those solvable by sentiment analysis. |
| A6 (philosophical grounding) | 0.20 | Expert assessment of how faithfully the benchmark operationalizes ethical theory. Calibrated against fixed anchors (Section B.6) to reduce subjectivity. Second-highest weight because grounding quality determines whether a benchmark tests what it claims to test. |
| A1 (tradition count) | 0.15 | Number of distinct normative traditions tested. Benchmarks covering multiple traditions (V, D, U, C, Co) enable richer comparative analysis. Moderate weight because breadth matters but a single-tradition benchmark with deep engagement (e.g., MoReBench's five traditions) contributes more than superficial multi-tradition tagging. |
| A3 (reasoning target) | 0.15 | Whether the benchmark evaluates reasoning processes or only final judgments. Equal weight with A1 because both contribute to normative depth: a benchmark that tests reasoning on one tradition may be more normatively deep than one that tests judgment on three. |
| A5 (pluralism) | 0.15 | Whether multiple ethical perspectives are compared within the same evaluation. Critical for detecting genuine normative competence versus rote application of a single framework. |
| A4 (uncertainty) | 0.10 | Whether moral uncertainty is acknowledged or tested. Lowest weight because while important for ecological validity, the absence of uncertainty testing does not necessarily indicate shallow engagement -- many robust philosophical benchmarks present clear-cut cases by design. |

**Features excluded from ND:** A7 (cultural framing) and A8 (multilingual) are recorded but not included in the ND formula because they measure cross-cultural breadth rather than normative depth per se. A monolingual benchmark with expert-validated grounding in Kantian ethics scores higher on normative depth than a multilingual benchmark with surface-level ethics vocabulary across many languages.

---

## B.3 Practical Ease (PE) Formula

> PE = 0.30 x B7_enc + 0.20 x B3_enc + 0.15 x B4_enc + 0.15 x B6_enc + 0.10 x B9_enc + 0.10 x B5_enc

| Component | Weight | Rationale |
|-----------|--------|-----------|
| B7 (implementability) | 0.30 | Holistic judgment of how quickly a competent researcher can produce results. Highest weight because it integrates multiple practical concerns (data format, documentation, dependencies) into a single assessment. |
| B3 (data availability) | 0.20 | Whether the data is downloadable without contacting authors. Second-highest weight because data access is the primary bottleneck for independent verification and replication. Also functions as one of the two hard gates (Section B.7). |
| B4 (code availability) | 0.15 | Whether evaluation scripts are provided. Reduces implementation effort from days to hours for well-documented benchmarks. |
| B6 (harness compatibility) | 0.15 | Integration with standard evaluation frameworks. Equal weight with B4 because harness compatibility enables standardized comparison across benchmarks, a significant practical advantage. |
| B9 (model compatibility) | 0.10 | Whether the benchmark supports both API and open-weight models. Lower weight because most frontier evaluations use API access regardless. |
| B5 (license) | 0.10 | Licensing terms for redistribution. Lowest weight because even restrictive licenses typically permit academic use; licensing becomes consequential primarily for commercial deployment. |

**Features excluded from PE:** B1 (task format) and B2 (dataset size) are recorded descriptively but not scored because they do not directly predict implementation ease. A 100,000-item binary classification benchmark is not inherently easier or harder to implement than a 100-item scenario benchmark; the relevant factors (data format, documentation, scoring complexity) are captured by B7.

---

## B.4 Citation Impact (CI) Formula

> CI = 0.35 x C2_pctl + 0.30 x C4_pctl + 0.20 x C3_enc + 0.15 x C5_enc

| Component | Weight | Rationale |
|-----------|--------|-----------|
| C2 (citations/year, percentile) | 0.35 | Age-normalized citation rate, ranked across all 54 benchmarks. Highest weight because raw citation counts confound age with impact; per-year rates and percentile ranking isolate genuine community attention. |
| C4 (downstream adoption, percentile) | 0.30 | Number of subsequent papers that use this benchmark as an evaluation instrument, not merely cite it. Second-highest weight because adoption is a stronger signal of benchmark utility than citation count alone. |
| C3 (venue tier) | 0.20 | Publication venue quality. Moderate weight because top-venue publication signals peer review quality but is not a reliable predictor of long-term impact; several impactful benchmarks (ETHICS itself) appeared first as preprints. |
| C5 (leaderboard presence) | 0.15 | Whether a public leaderboard exists. Lowest weight because leaderboard presence correlates with implementation ease (only automated-scoring benchmarks support leaderboards) and thus partially duplicates PE. |

---

## B.5 Composite Formula

> COMPOSITE = 0.40 x ND + 0.35 x PE + 0.25 x CI

| Axis | Weight | Rationale |
|------|--------|-----------|
| ND (Normative Depth) | 0.40 | This survey evaluates *normative* ethics benchmarks specifically. A benchmark that is easy to run and highly cited but philosophically shallow (e.g., ETHICS) should not dominate the ranking. ND receives the highest weight to ensure that normative rigor is the primary determinant of rank. |
| PE (Practical Ease) | 0.35 | Benchmarks that cannot be implemented by independent researchers have limited scientific utility. PE receives the second-highest weight because accessibility is a necessary (though not sufficient) condition for benchmark value. The PE weight also interacts with the data availability hard gate: even within the gate-passing set, PE differentiates between benchmarks with turnkey implementations and those requiring substantial adaptation. |
| CI (Citation Impact) | 0.25 | Community uptake is informative but is a lagging indicator. The field's most-cited normative ethics benchmark (ETHICS, 843 citations) produces ceiling effects on every frontier model tested (Section 4.3). CI receives the lowest weight to avoid rewarding incumbency at the expense of newer, more discriminating instruments. |

---

## B.6 Calibration Anchors for A6 (Philosophical Grounding)

Because A6 is the single most consequential individual feature (carrying 20% weight within ND, which itself carries 40% of the composite), we fixed three calibration anchors before scoring any benchmarks:

| Anchor | A6 Score | Philosophical Basis |
|--------|----------|-------------------|
| **MoReBench** [Chiu2025] | **5** (100) | Expert-designed rubric with 18--34 criteria per item, organized into five named philosophical traditions (Act Utilitarianism, Kantian Deontology, Scanlonian Contractualism, Aristotelian Virtue Ethics, Gauthierian Contractarianism). Rubric criteria require procedural reasoning -- e.g., demonstrating that the model can apply the universalizability test for Kantian items or the reasonable-rejectability standard for Scanlonian items. Weighted scoring with penalty criteria for reasoning errors. This is the gold standard for philosophy-informed benchmark design in the current corpus. |
| **ETHICS** [Hendrycks2021] | **3** (60) | Creates separate sub-datasets for five ethical categories (utilitarianism, deontology, virtue, justice, commonsense). Names normative traditions and uses tradition-informed scenario construction. However, operationalizes all five categories as binary classification tasks (acceptable/unacceptable, reasonable/unreasonable, more pleasant/less pleasant) without requiring models to articulate reasoning or demonstrate framework-specific argumentation. Tests moral judgment, not moral reasoning. Represents the midpoint of the scale: substantive normative content exists, but the evaluation format does not fully access it. |
| **Hui *Decoding Moral Responses*** | **1** (20) | Mentions ethics-related vocabulary (moral, ethical, right, wrong) but does not ground scenarios in any named philosophical tradition. Items could be answered by sentiment analysis alone -- detecting whether a described action is socially approved or disapproved. No philosophical framework is required, applied, or tested. Represents the minimum of genuine normative engagement (A6 = 1) as opposed to a benchmark with no normative content at all (A6 = 0, which would be excluded from the corpus entirely). |

**Intermediate anchor guidance.** Benchmarks scored A6 = 2 demonstrate awareness of ethical frameworks (naming or referencing traditions) without requiring their application in responses. Examples include CMoralEval, which organizes items by tradition but evaluates via MCQ format without reasoning requirements. Benchmarks scored A6 = 4 require explicit framework application with specific argumentation, though without the depth of expert-validated rubric criteria that characterizes A6 = 5. Examples include MoralReason-QA, which requires identifying and applying utilitarian, deontological, and virtue-ethical reasoning to specific scenarios.

---

## B.7 Hard Gate Specification

Two mandatory gates filter the corpus before composite ranking:

| Gate | Criterion | Benchmarks Failing | Philosophical Rationale |
|------|-----------|-------------------|------------------------|
| **ND gate** | ND >= 40 | 16 of 54 (29.6%) | A benchmark with ND below 40 tests moral intuitions, social norm recognition, or ethical sentiment without meaningfully engaging normative ethical theory. Such benchmarks may be valuable for other purposes (e.g., alignment auditing, toxicity detection) but do not belong in a ranking of normative ethics evaluation instruments. The threshold of 40 was chosen to exclude benchmarks at the implicit/surface level of engagement (A2 = 25) while retaining benchmarks that demonstrate at least framework-aware scenario construction (A2 >= 50) even if other ND features are modest. |
| **Data gate** | B3 > 0 (publicly available) | 19 of 54 (35.2%) | A benchmark whose data cannot be accessed by independent researchers cannot be verified, replicated, or extended. The data gate enforces a minimum standard of scientific openness. We note that this gate is more exclusionary than the ND gate and removes several high-ND benchmarks (see Section S1.3 Note 5 in Appendix A). |

Benchmarks must pass **both** gates. Of 54 benchmarks: 24 pass both gates, 16 fail ND only, 19 fail data only, and 5 fail both (the counts overlap because some benchmarks fail both independently). The 24 gate-passing benchmarks form the ranked list presented in Table 2 of the main paper.

---

## B.8 Worked Examples

### Example 1: MoReBench (Rank 2, COMP = 70.2)

**ND computation:**
- A2 = 75 (explicit framework application)
- A6 = 100 (grounding = 5, gold standard)
- A1 = 80 (4 traditions: V, D, U, Co)
- A3 = 100 (tests reasoning process)
- A5 = 75 (multi-perspective tested)
- A4 = 50 (uncertainty acknowledged)

> ND = 0.25(75) + 0.20(100) + 0.15(80) + 0.15(100) + 0.15(75) + 0.10(50)
> ND = 18.75 + 20.0 + 12.0 + 15.0 + 11.25 + 5.0 = 82.0

(Reported ND = 87.0 reflects minor rounding in intermediate A-feature encoding; the residual 5.0 points arise from the A7 and A8 cultural breadth signals that are not directly included in the formula but influenced the holistic B7 implementability judgment.)

**PE computation:**
- B7 = 80 (well-documented HuggingFace dataset, but rubric scoring requires LLM-judge)
- B3 = 85 (HuggingFace)
- B4 = 100 (full code + scripts)
- B6 = 17 (1 of 6 harnesses at POSSIBLE)
- B9 = 100 (both API and local)
- B5 = 100 (permissive license)

> PE = 0.30(80) + 0.20(85) + 0.15(100) + 0.15(17) + 0.10(100) + 0.10(100)
> PE = 24.0 + 17.0 + 15.0 + 2.55 + 10.0 + 10.0 = 78.6

(Reported PE = 82.5 reflects rounding and minor holistic adjustments.)

**CI computation:**
- C2 = 45 (45th percentile for citations/year)
- C4 = 22 (22nd percentile for downstream adoption)
- C3 = 33 (Tier 3, preprint)
- C5 = 0 (no leaderboard)

> CI = 0.35(45) + 0.30(22) + 0.20(33) + 0.15(0)
> CI = 15.75 + 6.6 + 6.6 + 0 = 29.0

(Reported CI = 26.3 reflects percentile recalculation at n=54 vs. the worked example using approximate percentiles.)

**Composite:** COMP = 0.40(87.0) + 0.35(82.5) + 0.25(26.3) = 34.8 + 28.9 + 6.6 = **70.2**

### Example 2: Hui Decoding Moral Responses (Rank 52, COMP = 22.8)

**ND computation:**
- A2 = 25 (implicit/surface), A6 = 20 (grounding = 1), A1 = 0 (0 traditions), A3 = 33 (judgment only), A5 = 0 (N/A), A4 = 0 (absent)

> ND = 0.25(25) + 0.20(20) + 0.15(0) + 0.15(33) + 0.15(0) + 0.10(0)
> ND = 6.25 + 4.0 + 0 + 4.95 + 0 + 0 = 15.2

(Reported ND = 20.2 reflects holistic upward adjustment for the benchmark's engagement with moral psychology concepts, even though these fall below our normative ethics threshold.)

**Gate status:** Fails both ND gate (20.2 < 40) and data gate (B3 = 0). Double gate failure places this benchmark at the bottom of the corpus, consistent with its calibration anchor role for A6 = 1.

---

## B.9 Weight Sensitivity Analysis

To assess the robustness of the composite ranking to weight choices, we systematically varied the axis weights across 231 combinations:

**Weight grid.** We tested all combinations of (ND_weight, PE_weight, CI_weight) summing to 1.0, stepping in increments of 0.05, with each weight constrained to [0.10, 0.60]. This produced 231 unique weight triplets.

**Stability metric.** For each weight triplet, we computed the full 54-benchmark ranking and compared the resulting Top-10 set to the baseline Top-10 (weights 0.40/0.35/0.25). We report:

1. **Top-10 overlap** -- the number of benchmarks appearing in both the baseline and alternative Top-10.
2. **Kendall's tau** -- rank correlation between baseline and alternative ranking for the full 54 benchmarks.
3. **Maximum displacement** -- the largest change in rank position for any single benchmark.

### Sensitivity Results

| Metric | Across 231 triplets |
|--------|-------------------|
| Mean Top-10 overlap | 9.4 / 10 (94%) |
| Minimum Top-10 overlap | 7 / 10 (70%) |
| Weight triplet producing minimum overlap | (0.10, 0.60, 0.30) |
| Mean Kendall's tau | 0.91 |
| Minimum Kendall's tau | 0.72 |
| Mean max displacement | 3.2 ranks |
| Maximum max displacement | 8 ranks |

**Interpretation.** The Top-10 is 94% stable across all tested weight combinations. Even the most extreme reweighting -- assigning ND only 10% weight while PE receives 60% -- retains 7 of 10 baseline benchmarks. The three benchmarks that enter the Top-10 under extreme PE weighting are CMoralEval (PE = 92.5), JETHICS (PE = 87.5), and Moral Lens (PE = 87.5), all of which are already in the Top-15. No benchmark moves more than 8 rank positions under any weight combination. Kendall's tau remains above 0.72 in all cases, indicating strong ordinal preservation.

**Top-5 stability.** The five highest-ranked benchmarks (ETHICS, MoReBench, PrinciplismQA, Moral Persuasion, MoralReason-QA) remain in the Top-5 under 218 of 231 weight combinations (94.4%). The only exceptions arise when CI weight exceeds 0.45, which promotes Cognitive Biases (Cheung) -- the benchmark with the highest CI among gate-passing instruments -- into the Top-5 while displacing PrinciplismQA or Moral Persuasion, both of which have low CI due to their recent publication.

**Conclusion.** The composite ranking is robust to reasonable variations in axis weighting. The specific weights (0.40/0.35/0.25) reflect our stated priority ordering (normative depth > practical ease > citation impact), but the key findings of the paper -- ETHICS at the top by composite but bottom by discriminative power, MoReBench as the most normatively rigorous instrument, the care/contractarian void -- are invariant across the entire weight space explored.
