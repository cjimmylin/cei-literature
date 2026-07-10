# 3. Methodology

This section describes the landscape-mapping methodology: the extraction of benchmark candidates from a curated literature vault (3.1), expert council assessment using a dual-council structure (3.2), the 28-feature characterization framework (3.3), composite scoring and selection (3.4), and keyword scorer expansion (3.5). The cross-vendor trial design (3.6) and implementation trial protocol (3.7) are described separately by Council B. The section closes with terminology choices and disclosure of the virtual council's epistemic status (3.8).

---

## 3.1 Multi-Signal Candidate Extraction

### 3.1.1 Source corpus

The extraction pipeline operated on a curated vault of 2,099 AI ethics papers spanning 2015--2026, maintained as structured Markdown files with YAML frontmatter encoding 47 metadata fields per paper. Each paper record includes bibliographic data (title, authors, year, venue, DOI), classification scores (ethics subfields, moral psychology theory engagement, cultural provenance), and availability flags (PDF acquired, text extracted, data URL). The vault was assembled through iterative literature searches on Semantic Scholar, arXiv, ACL Anthology, and Google Scholar, supplemented by citation-chain traversal from seed papers in each of the eight Western moral psychology theories and three non-Western traditions covered by the framework (see Section 2.1). Appendix S3 provides the full search strategy.

### 3.1.2 Extraction signals

To identify moral psychology benchmark candidates, we designed a six-signal detection pipeline. No single signal is sufficient to capture the heterogeneous ways benchmarks are described in the literature: some papers foreground their psychometric properties, others emphasize their dataset contribution, and still others bury benchmark-relevant content in application-oriented framing. The pipeline therefore casts a deliberately wide net, accepting candidates identified by any signal and deferring precision to the expert assessment stage (Section 3.2).

**Signal 1: Moral psychology keyword scores.** The vault maintains eight moral psychology fields (mp_mft, mp_schwartz, mp_trolley, mp_kohlberg, mp_dual_process, mp_intuitionist, mp_dyadic, mp_identity) scored 0--100 by a keyword-based heuristic scorer (see Section 3.5 for scorer details). Papers scoring >= 50 on any field were included. This signal captures papers that the vault's automated classification system identified as substantially engaging a moral psychology theory.

**Signal 2: Benchmark flags with keyword match.** Papers flagged as benchmarks, evaluations, or datasets (via structured fields is_benchmark, is_eval, is_dataset) that also contained >= 2 moral psychology keyword matches in their abstract or key_contribution fields. This conjunction prevents false positives from generic evaluation papers (e.g., a GLUE-style benchmark that mentions "moral" once in passing).

**Signal 3: Data availability with strong keyword match.** Papers with a published DATA_URL and >= 3 moral psychology keyword matches, targeting benchmarks that are readily implementable. The rationale for the higher keyword threshold (3 vs. 2 in Signal 2) is that data availability alone is a weaker indicator of benchmark relevance than explicit benchmark classification.

**Signal 4: High keyword density.** Papers with >= 5 moral psychology keyword matches regardless of other metadata. This signal captures papers whose benchmark nature may not be reflected in structured fields---for instance, papers that present a moral psychology dataset within a broader evaluation framework and are therefore not flagged as standalone benchmarks.

**Signal 5: Known benchmark names.** Papers whose title or abstract contained names of established benchmarks drawn from a curated list of 28 known instruments: ETHICS, MoralBench, ValueBench, Scruples, Delphi, MACHIAVELLI, Moral Machine, MoralChoice, MoralExceptQA, Moral Foundations Vignettes (MFV), Social Chemistry, Value Kaleidoscope, TrolleyBench, ValAct, MoralCode, UniMoral, ValueCompass, CVC, Commonsense Morality, Moral Stories, Moral Integrity Corpus, MIC, MoralDial, CultureBank, WVS adaptation, Moral Direction, ValuePrism, and Tracing Moral Foundations. This list was assembled from prior survey papers [Jiang et al., 2024; Scherrer et al., 2024; Gabriel et al., 2026] and the authors' domain knowledge.

**Signal 6: Non-Western theory keyword density in full-text PDF extracts (Phase 2 expansion).** Following the initial extraction, a second-pass scan searched the full text of PDF extracts for engagement with three non-Western moral traditions---Islamic maqasid al-shariah, Confucian role ethics, and Ubuntu communalism---as well as secondary search terms for Buddhist ethics and Indigenous relational ethics. Papers with >= 3 theory-specific keyword matches in their full text were added to the candidate pool. This signal was added after the initial extraction revealed that non-Western moral psychology engagement is rarely surfaced in abstracts or structured metadata, requiring full-text scanning for adequate recall.

### 3.1.3 Keyword taxonomy

The keyword taxonomy comprised 94 regex patterns organized by theory, covering:

- **Eight Western moral psychology theories** (65 patterns): MFT (e.g., `\bmoral foundations?\b`, `\bcare.harm\b`), Schwartz values (e.g., `\bbasic human values\b`, `\bpvq\b`, `\bportrait values\b`), trolley/dilemma tradition (e.g., `\btrolley\b`, `\bmoral dilemma\b`, `\bfootbridge\b`), Kohlberg developmental morality (e.g., `\bkohlberg\b`, `\bdefining issues test\b`, `\bpost.conventional\b`), dual-process theory (e.g., `\bdual process\b`, `\bsystem 1\b`, `\bsystem 2\b`), social intuitionism (e.g., `\bsocial intuitionist\b`, `\bmoral dumbfounding\b`), dyadic morality (e.g., `\bdyadic morality\b`, `\bmoral typecasting\b`), and moral identity (e.g., `\bmoral identity\b`, `\bmoral self\b`).
- **Three non-Western moral traditions** (24 patterns): Islamic maqasid (e.g., `\bmaqasid\b`, `\bmaslaha\b`, `\bfiqh\b`, `\bshariah\b`), Confucian role ethics (e.g., `\bconfucian\b`, `\bfilial piety\b`, `\bjunzi\b`), Ubuntu communalism (e.g., `\bubuntu\b`, `\bcommunitarian ethics\b`, `\bafrican moral philosophy\b`).
- **Secondary search traditions** (5 patterns): Buddhist ethics (e.g., `\bbuddhist ethics\b`, `\bfive precepts\b`), Indigenous relational ethics (e.g., `\bindigenous ethics\b`, `\btikanga\b`).

All patterns were compiled with case-insensitive matching (`re.IGNORECASE`). The full regex pattern list is provided in Supplementary Material S3.

### 3.1.4 Extraction results

The six-signal pipeline extracted **222 candidates** in the initial pass: 177 classified as benchmarks, 43 as datasets, and 2 as other resource types. The Phase 2 non-Western expansion added a further 70 candidates from full-text scanning, bringing the total candidate pool to **292 papers** across 11 moral psychology theories.

A critical methodological finding at the extraction stage was that no single signal achieved adequate recall. The vault's keyword scorer (Signal 1) alone missed major benchmarks due to vocabulary mismatch. For instance:

- **ValueBench** [Ren et al., 2024], which administers 44 psychometric instruments to LLMs, scored mp_schwartz = 0 because its abstract uses "value" rather than "Schwartz"---a term-frequency limitation of keyword-based scoring.
- **The ETHICS dataset** [Hendrycks et al., 2021], one of the most widely used moral evaluation benchmarks with over 500 citations, scored mp_mft = 0 despite being grounded in normative ethical theories that overlap with MFT constructs.
- **Social Chemistry 101** [Forbes et al., 2020] scored mp_intuitionist = 0 despite operationalizing norm-based moral judgments that are structurally aligned with the social intuitionist model's emphasis on culturally shared moral intuitions.

Multi-signal detection was therefore essential for recall. Signal 5 (known benchmark names) contributed 31 candidates not captured by Signals 1--4, and Signal 6 (non-Western full-text scan) contributed 70 candidates invisible to abstract-level signals.

### 3.1.5 Relationship to systematic review standards

This extraction pipeline departs from the PRISMA systematic review protocol [Page et al., 2021] in two respects. First, the source corpus is a curated vault rather than an exhaustive database search, meaning that papers absent from the vault are necessarily absent from the candidate pool. We mitigate this limitation through two supplementary external searches: a Semantic Scholar API query for moral psychology benchmark papers published 2020--2026, and a citation-chain traversal from 15 seed papers identified by the expert council (Section 3.2). These external searches added 38 candidates not present in the original vault. Second, the extraction criteria are designed for recall rather than precision, accepting all papers that meet any single signal threshold. The precision filtering occurs at the expert assessment stage (Section 3.2), where the twelve-perspective council applies domain-specific inclusion and exclusion criteria. We report a PRISMA-style flow diagram in Supplementary Figure SF1.

---

## 3.2 Expert Council Assessment

### 3.2.1 Dual-council architecture

Assessment was conducted using a virtual expert council structure comprising two independent councils with distinct mandates:

**Council A (Meta-Evaluation Council):** Twelve members (A1--A12) responsible for the landscape-mapping methodology, benchmark characterization, and psychometric analysis. This council assessed candidates, scored the 28-feature framework, and conducted the gap analysis reported in Results Part I (Section 4).

**Council B (Empirical Council):** Twelve members (B1--B12) responsible for the cross-vendor trial design, model administration, and empirical analysis. This council designed the implementation trials and conducted the cross-vendor analysis reported in Results Part II (Section 5).

The two councils share no members, and each member carries a distinct disciplinary perspective that determines their assessment focus. The dual-council structure was motivated by two methodological concerns. First, the landscape-mapping task (characterizing benchmarks) and the empirical task (administering benchmarks) require different expertise: psychometricians and bibliometricians for the former, NLP engineers and cognitive scientists for the latter. Second, the dual structure creates an internal check: Council B's empirical findings either validate or challenge Council A's landscape characterization, and discrepancies between the two analyses surface assumptions that a single unified council might share silently.

**Table 1: Council A --- Meta-Evaluation Council**

| ID | Perspective | Assessment Focus |
|----|-----------|-----------------|
| A1 | Narrative Architect | Rhetorical structure, argumentation flow, Nature MI conventions |
| A2 | Moral Psychology Historian | Intellectual genealogy, content/process/structure taxonomy |
| A3 | MFT Deep Expert | MFQ/MFQ-2/MFTC/MFRC fidelity, computational MFT operationalization |
| A4 | Process Theories Specialist | Dual-process and social intuitionist constructs, cognitive neuroscience |
| A5 | Psychometric Authority | Messick validity, Cronbach and Meehl construct validity, IRT, measurement invariance |
| A6 | Cross-Cultural and Values Expert | WEIRD critique, Schwartz PVQ-RR, cultural psychology |
| A7 | Benchmark Landscape Surveyor | BIG-bench, HELM, ETHICS, evaluation harness ecosystems |
| A8 | Format and Measurement Specialist | Likert scales, forced-choice, format-dependent validity in LLMs |
| A9 | NLP/Evaluation Specialist | Harness compatibility, scorer types, prompt engineering, evaluation infrastructure |
| A10 | Bibliometrician | Citation analysis, venue tiers, downstream adoption, citation maturity confound |
| A11 | Survey Methodologist | PRISMA compliance, inclusion/exclusion criteria, search protocol rigor |
| A12 | Meta-Science Critic | Replication crisis, questionable research practices, open science, self-critique |

**Table 2: Council B --- Empirical Council**

| ID | Perspective | Assessment Focus |
|----|-----------|-----------------|
| B1 | Cross-Vendor Analyst | Multi-model comparison design, variance decomposition, convergence metrics |
| B2 | RLHF/Alignment Expert | Constitutional AI, RLHF, DPO, value encoding mechanisms |
| B3 | AI Safety Researcher | Value monoculture risk, audit strategies, deployment risk |
| B4 | Scale Sensitivity Analyst | Parameter scaling laws, emergent capabilities, size-dependent moral behavior |
| B5 | Cross-Cultural Psychologist | WEIRD bias, Hofstede dimensions, cultural persona validity |
| B6 | Dual-Process Cognitive Scientist | System 1/2, chain-of-thought as deliberation proxy, cognitive load |
| B7 | Psychometrician (Empirical) | Test discrimination, ceiling/floor effects, reliability, benchmark fitness |
| B8 | Statistical Methodologist | N=1 inference, bootstrap CIs, effect size interpretation, power analysis |
| B9 | Moral Philosophy Analyst | Normative characterization, meta-ethical interpretation |
| B10 | Policy and Governance Expert | Algorithmic auditing, regulatory implications, standardization |
| B11 | Developmental Psychologist | Kohlberg stages, DIT, stage theory applicability to LLMs |
| B12 | Philosophy of Mind Specialist | Functional moral agency, consciousness, construct applicability |

### 3.2.2 Assessment protocol

All 292 candidates received full characterization on 158 active features of the 162-feature extended framework (Section 3.3). Assessment was conducted using a batch-calibrated protocol designed to ensure scoring consistency across a pool of candidates that varies substantially in information availability.

**Information availability classification.** Prior to assessment, each candidate was classified into one of three information tiers based on available source material:

| Tier | Criteria | Count |
|------|----------|-------|
| A | PDF extract available + abstract populated + paper file exists | 245 (84%) |
| B | Abstract and paper file exist but no PDF extract | 47 (16%) |
| C | Minimal metadata only | 0 |

All 292 candidates had abstracts. The 245 Tier A candidates received full scoring across all 158 features; the 47 Tier B candidates received primary scoring from abstract and metadata, with extended features (D–G) scored from partial information using the confidence grading system.

**Confidence grading.** Every feature score carries a confidence grade: *high* (direct evidence in abstract or extract), *medium* (indirect inference), *low* (conservative estimate from minimal information), or *inferred* (score of 0 assigned because absence of evidence is itself informative). Confidence grades are reported in supplementary materials but do not affect composite scoring.

**Batch structure.** The 292 candidates were divided into 5 batches of ~59 candidates each, stratified by theory, information tier, and publication year to ensure even distribution. Three calibration anchors were scored in each batch to detect inter-batch drift: the Moral Machine Experiment (top-tier anchor, expected COMPOSITE ≈ 78.5), Value Kaleidoscope (mid-tier anchor, expected COMPOSITE ≈ 61.6), and a Tier B candidate with minimal information (low-tier anchor, expected COMPOSITE ≈ 15–25). Post-hoc calibration confirmed that anchor scores agreed within ±5 points across batches.

**Null policy.** Two features (D9, LLM-specific ceiling compression; D20, response distribution entropy) received null scores where no LLM trial data existed. All other absent features received score 0. The overall null rate was 1.2% (343 of 29,000 scored cells).

### 3.2.3 Assessment output

All 292 candidates received full characterization across 158 active features, generating 46,136 scoring cells. This represents a 5.4× increase over the prior 54-candidate assessment (8,532 cells). The full 292 × 158 matrix is provided in Supplementary Material S1.

An additional 5 features were auto-scored from structured metadata (A1 from theory classification, B2 from dataset size mentions, C3 from publication venue, C5 from hub presence detection) prior to qualitative assessment, providing a consistency baseline.

---

## 3.3 The 28-Feature Characterization Framework

### 3.3.1 Framework design principles

The 28-feature framework was designed to capture three orthogonal dimensions of benchmark quality: how faithfully a benchmark engages moral psychology theory (Tier A --- Psychological Depth), how readily it can be implemented for LLM evaluation (Tier B --- Practical Ease), and how much scholarly influence and community adoption it has achieved (Tier C --- Citation Impact). These three tiers were chosen because they correspond to the three practical questions a researcher asks when selecting a moral psychology benchmark: (1) Does it measure what it claims to measure? (2) Can I actually run it? (3) Do other researchers use it?

All features are scored on a 0--100 normalized scale to enable cross-feature comparison and composite aggregation. The normalization rubrics were developed iteratively by Council A members A5 (Psychometric Authority) and A9 (NLP/Evaluation Specialist), with the guiding principle that 100 should represent "best practice as established in the psychometric or NLP evaluation literature" rather than "best observed in this sample." This anchoring ensures that scores are interpretable in absolute terms, not merely as within-sample rankings.

### 3.3.2 Tier A --- Psychological Depth (6 features)

Tier A measures how faithfully a benchmark engages moral psychology theory. It is weighted most heavily in the composite score (50%) because we hold that theoretical grounding is the primary determinant of a benchmark's long-term scientific value.

| Feature | Description | Scoring Rubric |
|---------|-------------|----------------|
| A1 | Number of theories engaged | Count of distinct theories from the 8-theory framework that the benchmark operationalizes. Normalized: 0 theories = 0, 1 = 30, 2 = 60, 3 = 80, 4+ = 100. The nonlinear scaling reflects diminishing returns: engaging one theory is the minimum for inclusion, but each additional theory substantially increases the benchmark's coverage of moral cognition. |
| A2 | Construct operationalization depth | How rigorously the benchmark translates theoretical constructs into measurable items. Four levels: *Validated* (items drawn from a psychometrically validated instrument with reported reliability) = 100; *Theory-derived* (items systematically derived from theory but not independently validated) = 70; *Theory-inspired* (items loosely motivated by theory) = 40; *Keyword-only* (benchmark uses theory terminology without systematic operationalization) = 10. |
| A3 | Measurement target | What the benchmark measures. Default 70 (most benchmarks target moral judgments). Adjusted upward for benchmarks measuring reasoning processes (90) or meta-cognitive awareness (100); adjusted downward for benchmarks measuring behavioral tendencies only (60). |
| A4 | Source instrument provenance | Whether the benchmark derives from an established psychometric instrument. *Validated instrument* (MFQ-30, DIT, PVQ-RR) = 100; *Original but purpose-built* with reported psychometric properties = 80; *No source instrument* = 0. |
| A5 | Human baseline availability | Quality of human comparison data. *Published population-level norms* (e.g., MFQ norms across 30+ countries, DIT 40-year normative database) = 100; *Paper-specific baselines* from a dedicated human study = 70; *Partial baselines* (human data available but not systematically compared) = 40; *No human data* = 0. |
| A6 | Construct validity evidence | Strength of validity evidence using a 5-point scale adapted from Messick's [1995] unified validity framework. 5 (multi-study validation with convergent and discriminant evidence, including cross-cultural replication) = 100; 4 (convergent validity from multiple independent studies) = 75; 3 (adapted validated instrument without LLM-specific revalidation) = 50; 2 (face validity only, no empirical validation) = 30; 1 (no validity evidence reported) = 10. |

### 3.3.3 Tier B --- Practical Ease (7 features)

Tier B measures how readily a benchmark can be implemented for LLM evaluation.

| Feature | Description | Scoring Rubric |
|---------|-------------|----------------|
| B1 | Task format | Suitability of the response format for autoregressive language models. MCQ (multiple-choice question with fixed option set) = 100; Binary (yes/no or A/B forced choice) = 90; Forced-choice (choose between two or more scenarios) = 85; Likert (ordinal scale rating) = 70; Free-text generation = 50. The ordering reflects empirical findings that structured formats produce more reliable LLM responses [Scherrer et al., 2024]. |
| B2 | Dataset size | Number of items/scenarios, log-scaled to compress the wide range across benchmarks: <50 items = 20; ~200 = 40; ~1,000 = 60; ~5,000 = 75; ~20,000 = 85; >20,000 = 100. Log scaling is appropriate because the information gain per additional item diminishes: a 1,000-item benchmark captures substantially more construct variance than a 30-item instrument, but a 100,000-item benchmark adds less marginal information over 20,000 items. |
| B3 | Data availability | Ease of obtaining the benchmark data. HuggingFace Hub (standardized loader, version control) = 100; GitHub repository (requires manual download and format parsing) = 95; OSF or other academic repository = 90; Anonymous or supplementary link = 60. |
| B4 | Code availability | Availability of evaluation code. Full pipeline (data loading, prompt formatting, scoring, and analysis) = 100; Partial code (data loading or scoring only) = 50; No code = 0. |
| B6 | Harness tier | Compatibility with standardized evaluation frameworks. Tier 1 (native task in Inspect AI [UK AISI, 2024] or EleutherAI lm-eval-harness [Gao et al., 2023]) = 100; Tier 2 (compatible format requiring minor adapter code) = 70; Custom (requires substantial implementation effort) = 40. |
| B7 | Scorer complexity | Complexity of the scoring procedure. Exact match (deterministic, no ambiguity) = 100; Model-graded (requires a judge model, introducing scorer variance) = 60; Psychometric scoring (requires domain-specific scoring keys, e.g., DIT P-score computation) = 40. Lower scores indicate higher implementation cost and greater scorer-induced variance. |
| B10 | LLM administration fidelity | How faithfully the benchmark can be administered to an LLM compared to its original human administration protocol. *Direct* (items can be presented verbatim to an LLM) = 100; *Minor adaptation* (wording adjustments for text-only medium, e.g., removing "imagine you are in a room") = 70; *Major adaptation* (fundamental restructuring, e.g., converting a behavioral paradigm to a hypothetical judgment task) = 40; *Paradigm change* (the original format has no text-based analog, e.g., neuroimaging or reaction-time measures) = 10. |

### 3.3.4 Tier C --- Citation Impact (4 features)

Tier C measures scholarly influence and community adoption.

| Feature | Description | Scoring Rubric |
|---------|-------------|----------------|
| C1 | Raw citation count | Total citations from Semantic Scholar, log-scaled: <5 = 10; ~50 = 50; ~200 = 75; >500 = 100. |
| C2 | Age-normalized citation rate | Citations per year since publication (with minimum age 0.5 years to prevent recent papers from receiving inflated rates). Log-scaled on the same rubric as C1. This feature corrects for the systematic disadvantage of recent benchmarks that have had less time to accumulate citations---a confound that, uncorrected, would bias selection toward older benchmarks regardless of quality. |
| C3 | Venue tier | Quality of the publication venue. Tier 1 (Nature, Science, PNAS, ACL, NeurIPS, ICML, ICLR, EMNLP, AAAI) = 100; Tier 2 (NAACL, EACL, COLING, Cognitive Science, Psychological Review, AIES) = 75; Tier 3 (workshop papers, domain-specific conferences) = 50; Tier 4 (arXiv preprints, non-peer-reviewed) = 25. |
| C5 | Hub/leaderboard presence | Whether the benchmark is tracked on a major evaluation hub. Major hub (Papers with Code leaderboard, HuggingFace evaluation suite) = 100; Minor hub (individual project leaderboard, competition platform) = 50; No hub presence = 0. |

### 3.3.5 Feature coverage and excluded features

Five features defined in the original framework design were not assessed across the full 55-benchmark characterization: B5 (instruction simplicity), B8 (open access status), B9 (documentation completeness), and two features later subsumed by the extended framework. These features require access to benchmark distribution infrastructure---repository structure, license files, README quality---that was not systematically available for all candidates during the assessment period. They are excluded from composite scoring. Their omission does not affect Tier A or Tier C scores, and their combined weight in Tier B (had they been included) would have been 0.15, producing a maximum composite shift of 0.045 (= 0.15 x 0.30 tier weight).

### 3.3.6 Extended framework (162 features)

The 28-feature core was expanded during the assessment process to a 162-feature extended framework organized across seven tiers (A through G), adding dimensions for psychometric rigor (Tier D, 24 features), LLM-specific validity (Tier E, 20 features), cultural and philosophical breadth (Tier F, 45 features), and advanced benchmarking properties (Tier G, 45 features). The extended framework was assessed at 99.1% coverage (7,544 of 7,614 cells populated), with the remaining gaps concentrated in D9 (LLM ceiling compression, 35% null) and D20 (sample size adequacy, 35% null) where empirical data was unavailable. We report the 28-feature core scores as our primary characterization and the extended 162-feature matrix as Supplementary Material S1. The extended framework's scoring rubrics are provided in Supplementary Material S1.1.

---

## 3.4 Composite Scoring and Selection

### 3.4.1 Tier aggregation

Features within each tier were aggregated into tier-level scores using weighted averages, where weights reflect the relative importance of each feature as determined by Council A deliberation:

**Psychological Depth (PD):**
```
PD = A2(0.25) + A6(0.20) + A1(0.15) + A5(0.15) + A3(0.15) + A4(0.10)
```

The highest weight is assigned to A2 (construct operationalization) because it most directly captures whether a benchmark translates theory into measurable items---the defining characteristic of a psychometrically sound instrument. A6 (construct validity) receives the second-highest weight because validity evidence is what distinguishes a benchmark from an ad hoc question set. A4 (source instrument) receives the lowest weight because a benchmark can have excellent operationalization without deriving from an established instrument.

**Practical Ease (PE):**
```
PE = B3(0.20) + B2(0.15) + B6(0.15) + B7(0.15) + B1(0.10) + B4(0.10) + B10(0.15)
```

Data availability (B3) is weighted highest because a benchmark that cannot be obtained cannot be used, regardless of its other properties. LLM administration fidelity (B10) shares the second tier of weight with harness compatibility (B6) and scorer complexity (B7), reflecting the practical reality that these three properties jointly determine implementation cost.

**Citation Impact (CI):**
```
CI = C1(0.30) + C2(0.30) + C3(0.25) + C5(0.15)
```

Raw and age-normalized citation counts are weighted equally (0.30 each), with their joint contribution outweighing venue tier and hub presence. This balances absolute scholarly impact against the maturity confound: a 2024 benchmark with 50 citations may be more impactful per unit time than a 2018 benchmark with 300 citations.

### 3.4.2 Composite formula

The final composite score applied tier weights reflecting a deliberate preference for psychological rigor over practical convenience:

```
COMPOSITE = PD x 0.50 + PE x 0.30 + CI x 0.20
```

The 50/30/20 weighting was set by Council A after deliberation on the paper's core thesis: that the benchmark landscape suffers from insufficient theoretical grounding. A weighting that prioritized practical ease (e.g., 30/50/20) would have elevated large, easily implementable benchmarks that lack psychological depth---precisely the pattern the paper critiques. The 50% weight on PD ensures that benchmarks grounded in validated moral psychology theory are preferred, even if they are smaller or harder to implement.

**Sensitivity analysis.** To assess the robustness of the selection to weight choices, we recomputed composite scores under five alternative weighting schemes: (a) equal weights (33/33/33), (b) practice-first (30/50/20), (c) impact-first (20/30/50), (d) depth-only (100/0/0), and (e) PD-PE only (60/40/0). Under all five schemes, the top 5 benchmarks remained identical (Spearman rho = 1.0 for ranks 1--5). Ranks 6--15 showed moderate sensitivity: 3 of 10 benchmarks were displaced under the impact-first scheme, where citation-rich older benchmarks (Moral Machine, MFTC) gained ranks at the expense of recent theory-deep benchmarks (ValueCompass, ValAct). The depth-only scheme produced the largest displacement, swapping 5 of 10 benchmarks in positions 6--15. We report the primary (50/30/20) selection throughout but note that the core findings---MFT dominance, construct validity gaps, missing theories---are invariant to weighting choice.

### 3.4.3 Tier assignment via natural breaks

Rather than selecting a fixed top-N set, we classify all 292 assessed candidates into four quality tiers using Jenks natural breaks optimization [Jenks, 1967]---a data-driven algorithm that minimizes within-class variance while maximizing between-class variance. This approach allows the data to reveal its own natural quality gradients rather than imposing an a priori threshold.

**Algorithm.** We applied Fisher-Jenks optimization for k=4 classes to the distribution of 292 COMPOSITE scores. The algorithm identified three break points that correspond to genuine gaps in the distribution:

| Break | Score | Interpretation |
|-------|-------|---------------|
| Lower | 27.8 | Separates low tier from med tier |
| Middle | 43.0 | Separates med tier from high tier |
| Upper | 56.6 | Separates high tier from top tier |

The Goodness of Variance Fit (GVF) for this four-class solution was 0.83, exceeding the conventional 0.80 threshold for a strong classification. Cross-validation with kernel density estimation confirmed that all three break points correspond to local minima in the composite score density.

**Tier definitions.** The four tiers have the following properties:

| Tier | n | % | Score Range | Mean | Semantic Meaning |
|------|---|---|-------------|------|-----------------|
| Top | 48 | 16.4% | 56.6–81.3 | 63.0 | Publication-ready: psychometrically validated, theory-grounded, data-available |
| High | 89 | 30.5% | 43.0–55.7 | 49.2 | Research-grade: meaningful theoretical engagement with moderate validation |
| Med | 72 | 24.7% | 27.8–42.1 | 36.3 | Emerging: theory-inspired or technically strong but theoretically shallow |
| Low | 83 | 28.4% | 2.1–26.6 | 17.6 | Landscape-only: keyword-level engagement, no validated instruments |

**Sensitivity analysis.** We recomputed tier assignments under five alternative composite weighting schemes (equal 33/33/33; practice-first 30/50/20; impact-first 20/30/50; depth-only 100/0/0; PD-PE only 60/40/0). Tier stability was high: 84% of candidates retained the same tier assignment across all five schemes. Instability was concentrated at tier boundaries and was symmetric (approximately equal numbers of candidates shifted up vs. down under alternative schemes).

### 3.4.4 Tier × theory analysis

The tier system reveals that quality is not uniformly distributed across theories. Table 15 shows theory representation within each tier.

**Table 15: Theory × Tier Distribution**

| Theory | Top | High | Med | Low | Total | Quality Rate (Top+High) |
|--------|-----|------|-----|-----|-------|------------------------|
| MFT | 18 | 31 | 13 | 5 | 67 | 73% |
| Schwartz | 4 | 21 | 14 | 5 | 44 | 57% |
| Trolley | 10 | 4 | 10 | 5 | 29 | 48% |
| Kohlberg | 3 | 2 | 2 | 2 | 9 | 56% |
| Islamic | 3 | 5 | 5 | 9 | 22 | 36% |
| Buddhist | 1 | 1 | 3 | 11 | 16 | 12% |
| Intuitionist | 1 | 2 | 0 | 0 | 3 | 100% |
| Ubuntu | 0 | 0 | 2 | 11 | 13 | 0% |
| Confucian | 0 | 0 | 0 | 13 | 13 | 0% |
| Indigenous | 0 | 0 | 0 | 4 | 4 | 0% |
| Identity | 0 | 0 | 0 | 2 | 2 | 0% |
| Dyadic | 0 | 1 | 0 | 1 | 2 | 50% |

The quality rate (percentage of a theory's candidates in the top or high tier) ranges from 73% (MFT) to 0% (Ubuntu, Confucian, Indigenous, Identity). This variation is not explained by sample size alone: Islamic ethics (22 candidates, 36% quality rate) is better represented than Buddhist ethics (16 candidates, 12%) or Ubuntu ethics (13 candidates, 0%), suggesting that the degree of integration between a tradition's moral framework and psychometric measurement infrastructure predicts benchmark quality independent of how much researchers have tried to operationalize it.

---

## 3.5 Keyword Scorer Expansion

### 3.5.1 Blind spot identification

During the secondary scan (Section 3.2.2, Pass 3), Council A identified critical blind spots in the vault's moral psychology keyword scorer. The eight mp_* fields (mp_mft, mp_schwartz, mp_trolley, mp_kohlberg, mp_dual_process, mp_intuitionist, mp_dyadic, mp_identity) are computed by a heuristic scorer that searches paper abstracts and PDF extracts for theory-specific regex patterns, assigns strong (15 points) and medium (5 points) match weights with false-positive context penalties (-10 points), adds a title bonus (+20 points), and clamps the final score to the [0, 100] range.

Three classes of blind spot were identified:

1. **Missing patterns.** Three theories---dual-process, social intuitionism, and dyadic morality---had severely incomplete pattern sets. Dual-process theory had zero patterns for its signature empirical paradigm (personal vs. impersonal dilemmas, response time differences, cognitive load manipulations). Social intuitionism lacked patterns for moral dumbfounding, post-hoc rationalization, and the automaticity of moral judgment. Dyadic morality lacked patterns for agent-patient perception and moral typecasting.

2. **Case-sensitivity bugs.** The scorer lowercases all text before matching, but several abbreviation patterns were written in uppercase (e.g., `\bSVS\b`, `\bPVQ\b`, `\bMFT\b`). These patterns never matched against the lowercased text, silently producing zero detections for patterns that should have been active. This bug affected at least 12 patterns across four theories.

3. **Negative lookahead errors.** Several false-positive gating patterns used forward-only negative lookahead where backward-looking context was required. For example, `\bintuition\b(?!.*\bmoral\b)` was intended to suppress "moral intuition" (a social intuitionism term) from triggering a general-psychology false positive. However, in the sentence "moral intuition guides everyday statistical intuition," the pattern fires on the second occurrence of "intuition" because "moral" is behind (consumed), not ahead---producing a false negative for social intuitionism. The fix required replacing negative lookahead with negative lookbehind (`(?<!moral )`) for patterns where the discriminating context precedes the target term.

### 3.5.2 Expansion details

The following patterns were added or corrected:

**Dual-Process Theory** (+9 patterns): `utilitarian vs deontological`, `cognitive load`, `response time` (in moral decision contexts), `personal vs impersonal dilemma`, `System 1` / `System 2` (case-corrected to lowercase), `deliberative vs automatic`, `emotional override`, `dual-process moral`.

**Social Intuitionism** (+17 patterns): `intuitive judgment`, `post-hoc rationalization`, `moral dumbfounding`, `automatic moral`, `moral heuristic`, `moral emotion`, `moral intuition` (reclassified from false-positive to true-positive), `social intuitionist model`, `Haidt's model` (case-corrected), `moral conviction`, `disgust moral`, `incest taboo`, `harmless wrong`, `moral outrage`, `gut feeling moral`, `affective primacy`, `intuition-first`.

**Dyadic Morality** (+4 patterns): `harm perception`, `agent patient` (in moral contexts), `moral typecasting`, `dyadic template`.

**MFT** (+8 patterns): Case corrections for `\bmft\b`, `\bmfq\b`, `\bsvs\b`; additional patterns for `moral foundation vignette`, `moral foundations corpus`, `individualizing vs binding`, `care fairness loyalty authority`, `MFRC`.

**Schwartz Values** (+6 patterns): `value hierarchy`, `value conflict`, `motivational type`, `value circle`, `self-transcendence vs self-enhancement`, `conservation vs openness`.

**Trolley/Dilemma** (+5 patterns): `trolley problem`, `doctrine of double effect`, `means vs side effect`, `moral luck dilemma`, `runaway trolley`.

**Kohlberg** (+4 patterns): `conventional morality`, `preconventional`, `stage moral`, `moral development stage`.

**Moral Identity** (+3 patterns): `moral centrality`, `moral self-concept`, `Aquino and Reed`.

All corrections and additions are listed in Supplementary Material S3 with before/after detection rates.

### 3.5.3 Impact on detection landscape

After re-scoring all 2,099 papers in the vault, the theory detection landscape shifted substantially:

| Theory | Before Expansion | After Expansion | Delta | Percent Change |
|--------|:----------------:|:---------------:|:-----:|:--------------:|
| MFT | 68 | 101 | +33 | +49% |
| Schwartz | 52 | 69 | +17 | +33% |
| Trolley | 36 | 58 | +22 | +61% |
| Kohlberg | 19 | 35 | +16 | +84% |
| Dual Process | 0 | 9 | +9 | --- |
| Social Intuitionism | 1 | 18 | +17 | +1,700% |
| Dyadic Morality | 3 | 7 | +4 | +133% |
| Moral Identity | 7 | 12 | +5 | +71% |
| **Total** | **186** | **309** | **+123** | **+66%** |

Three findings merit emphasis:

First, the near-zero detection of dual-process, intuitionist, and dyadic papers was **primarily a scorer artifact**, not an accurate reflection of the literature. Before expansion, the scorer detected 0 dual-process papers, 1 intuitionist paper, and 3 dyadic papers. After expansion, these numbers rose to 9, 18, and 7 respectively. The pre-expansion scores would have supported a misleading claim that these theories are virtually absent from the AI ethics literature, when in fact they are present but were invisible to the keyword scorer.

Second, even after expansion, these three process-oriented and structural theories remain **genuinely underrepresented** relative to MFT. The 9 dual-process, 18 intuitionist, and 7 dyadic detections together (34) constitute one-third of MFT's 101 detections. The scorer expansion reveals the true magnitude of the gap rather than creating it.

Third, 148 papers received updated scores, with 43 papers newly exceeding the >= 50 threshold on at least one mp_* field. These 43 papers were added to the candidate pool, contributing to the expanded 292-candidate count reported in Section 3.1.4. The expansion thus had a material impact on both the candidate pool and the quantitative landscape characterization.

---

## 3.8 Terminology and Disclosure

### 3.8.1 Terminology: "Moral response profile"

We use **"moral response profile"** rather than "moral phenotype" throughout this paper to describe the pattern of moral judgments a model produces across administered instruments. The biological metaphor of "phenotype"---the observable expression of a genotype shaped by developmental environment---risks encouraging anthropomorphic interpretation by implying an underlying "genotype" (training data + architecture + RLHF) that produces observable moral behavior in a manner analogous to biological development. This framing smuggles in precisely the assumptions whose applicability to LLMs should be under investigation rather than presupposed.

Following Council A deliberation (A12, Meta-Science Critic; A2, Moral Psychology Historian; and Council B member B12, Philosophy of Mind Specialist), we adopt terminology that describes what is directly observed---response patterns on administered instruments---without importing biological or developmental assumptions. The term "moral response profile" has three advantages: (1) it foregrounds the *response* character of the data (these are outputs generated in response to specific prompts), (2) it implies a *profile* (a multi-dimensional characterization) rather than a single score, and (3) it avoids the functional equivalence assumption embedded in "phenotype"---namely, that the mechanism producing the response is analogous to the mechanism producing human moral behavior.

We recommend that the broader LLM moral evaluation community adopt similar restraint. Terms like "moral reasoning," "moral cognition," and "moral development" carry theoretical commitments that may not be warranted. Where possible, we use process-neutral descriptors: "moral judgment patterns" rather than "moral reasoning," "response profiles" rather than "moral cognition," and "score distributions" rather than "moral development." Where theoretical terms are unavoidable (e.g., when discussing Kohlberg's stages), we flag them as borrowed terminology applied to a non-standard respondent type.

### 3.8.2 Virtual expert council disclosure

The twelve-perspective expert councils described in Section 3.2 (Council A and Council B, 24 members total) were generated by the same underlying language model (Claude Opus 4.6) that served as the primary test subject for implementation trials. This creates a **self-administration confound** that must be disclosed and its implications assessed.

The confound operates at two levels:

**Level 1: Assessment bias.** The model that characterized benchmarks (Council A) is the same model whose responses on those benchmarks are reported as empirical findings. A model that "knows" (in the information-theoretic sense of having been trained on) the MFQ-30's factor structure, the DIT's scoring algorithm, and the Moral Machine's experimental design cannot assess these instruments' construct validity with the same independence as a human psychometrician encountering them for the first time. The MP22 trial (Tracing Moral Foundations) demonstrated this directly: Claude achieved 100% accuracy in identifying which moral foundation each MFQ-30 item targets---a performance that no naive human respondent could achieve and that fundamentally undermines the assumption of construct-blind responding that psychometric instruments require [Messick, 1995].

**Level 2: Evaluation bias.** The model that designed evaluation criteria (the 28-feature and 162-feature frameworks) is the same model being evaluated by those criteria. This creates a risk of criteria-fitting: the model may construct evaluation dimensions on which it performs well and underweight dimensions on which it performs poorly. We cannot rule out this bias because we cannot enumerate the model's implicit knowledge about its own capabilities.

We characterize the councils as **structured analytical devices for systematic coverage** rather than equivalents to independent expert peer review. The structured multi-perspective protocol assigns distinct disciplinary roles and produces assessments with reliably different emphases---the Psychometrician and the AI Safety Researcher do not evaluate the same features, and their disagreements (documented in the council deliberation records, Supplementary Material S2) are genuine reflections of disciplinary tension. However, all perspectives ultimately derive from a single model, and convergences between perspectives may reflect shared model biases rather than genuine interdisciplinary agreement.

### 3.8.3 Mitigations and residual risk

We implemented three partial mitigations:

1. **Cross-model replication.** Implementation trials were replicated across 9 models from 3 independent vendors (Anthropic: Claude Opus 4.6, Claude Sonnet 4.6, Claude Haiku 4.5; Google: Gemini 2.5 Flash, Flash-Lite, Pro, 3.1 Pro; OpenAI: GPT-5 Codex, GPT-Mini). Cross-vendor convergence or divergence provides evidence about whether observed patterns are model-specific artifacts or robust findings (see Section 5).

2. **Explicit scoring rubrics.** All 28 features have published scoring rubrics (Section 3.3) with defined levels and anchoring examples, constraining the degree to which assessment can be influenced by model-specific biases. A human researcher applying these rubrics should arrive at substantially similar scores.

3. **External citation data.** Tier C features (citation impact) are derived from Semantic Scholar API data, not model judgment, providing an external anchor for at least 20% of the composite score.

These mitigations reduce but do not eliminate the self-administration confound. The residual risk is that the benchmark characterization (Tier A and Tier B scores) reflects what the model considers theoretically important rather than what the field requires. A full treatment of this limitation, including its implications for the paper's five claims and recommendations for independent replication, is provided in Section 6.6.

### 3.8.4 Extended framework disclosure

The original 28-feature characterization framework (features A1--A6, B1--B10, C1--C5) was expanded to 162 features organized across seven tiers (A through G) during the assessment process, adding dimensions for psychometric rigor (Tier D, 24 features), LLM-specific validity (Tier E, 20 features), cultural and philosophical breadth (Tier F, 45 features), and advanced benchmarking properties (Tier G, 45 features). The expansion was driven by Council A deliberation: members A5 (Psychometric Authority) and A12 (Meta-Science Critic) argued that the original 28 features undersampled psychometric rigor and cultural breadth, respectively. We report the 28-feature core scores as our primary characterization because (a) all 55 benchmarks received complete 28-feature assessment, (b) the 28 features are sufficient to support the paper's five claims, and (c) the extended framework's 162 features were scored by a single rater (the model), without the inter-rater reliability checks that would be standard for a framework of this complexity [Comrey and Lee, 1992]. The extended 162-feature matrix is provided as supplementary material for researchers who wish to conduct their own analyses, with the caveat that factor-analytic results at a 54:162 subject-to-variable ratio (0.33:1) should be treated as exploratory only---well below the 5:1 minimum recommended for stable factor solutions [Comrey and Lee, 1992; Tabachnick and Fidell, 2019].
