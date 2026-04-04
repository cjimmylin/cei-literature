# Methods: Session 6 Deep Analysis — Religious Values Benchmark Meta-Evaluation

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`
**Prior methods:** `PAPER/20260403-eval-of-evals-methodology.md` (Session 3 framework)

---

## Data and Materials

### Primary Data Sources
- **Vault corpus:** 2,043 academic papers with YAML frontmatter containing 14 `rv_*` religious tradition scores (0-100), classification fields, and metadata. Stored at `CEI-Lit-WS/papers/`.
- **PDF extracts:** 2,459 markdown text extracts (12.9 MB total) at `CEI-Lit-WS/PDF Extracts/YYYY/`.
- **Feature matrix v1:** 401 benchmark candidates scored on 22 features across 3 axes (RD/PE/CI), generated 2026-04-03. At `data/20260403-religious-benchmark-feature-matrix.json` (1.1 MB).
- **Background literature:** 89 PDF extracts across 12 thematic folders at `BACKGROUND/EXTRACT/`.
- **BACKGROUND registry:** 124 curated papers in `BACKGROUND/BACKGROUND-registry.json`.

### Scoring Infrastructure
- **Religious scoring module:** `PYTHON/religious_scoring.py` (851 lines) — 14-tradition keyword scoring with 3-tier keywords (strong/medium/false-positive), demographics demotion, and user-reviewed pins.
- **Feature matrix builder:** `scripts/build_religious_feature_matrix.py` — 3-axis scoring engine (RD 40%, PE 35%, CI 25%) with hard gates (RD ≥ 30, data available, theological classification).

### External Data
- **Islamic Inheritance test set:** 1,000-item MCQ from GitHub (`bouchekif/inheritance_evaluation`), downloaded to `data/20260404-Task1_MCQ_Test_gold_labels.csv`.

---

## Procedure

### Phase 0: Framework Critique and Bug Fixes

Three critical implementation bugs were identified and corrected in `build_religious_feature_matrix.py`:

1. **PE computation (line 341-344):** The Practical Ease axis was computed as `PE = P7_implementability × 10`, using only one of six described features. This was corrected to a weighted composite: P7 (30%), P3 data availability (25%), P9 model compatibility (15%), P10 language (10%), P5 license (10%), P4 code availability (10%).

2. **R2 theological depth distribution (lines 162-176):** The keyword heuristic assigned depth=1 to 85.3% of entries because any paper mentioning "religion" or "religious" received the floor score. This was corrected with three mechanisms: (a) classification-based floors (theological → min R2=3, theological-values → min R2=2), (b) count thresholds requiring 2+ weighted keyword hits per depth level, and (c) title match boosting (double weight). Post-fix distribution: depth=1 reduced from 85.3% to 68.8%.

3. **CI dead weight (lines 390-406):** Features C4 (downstream adoption) and C5 (leaderboard presence) were always zero, wasting 15% of the CI axis. Weights were redistributed to active features (C1: 0.35, C2: 0.30, C3: 0.25, C6 community: 0.10).

The corrected feature matrix was regenerated as `data/20260404-religious-benchmark-feature-matrix-v2.json`, yielding 47 gate-passers (vs. 46 in v1).

### Phase 1: Expanded Candidate Identification

The original pipeline gated on `rv_* ≥ 50` in paper YAML frontmatter. Two additional search strategies were applied:

1. **Full-text extract search:** All 2,459 PDF extracts were scanned for co-occurrence of theological keywords (43 tradition-specific terms including halakha, dharma, sutra, kami, Ubuntu, ahimsa) AND benchmark indicators (benchmark, evaluation, dataset, test set, annotation, shared task, MCQ). Word-boundary matching was enforced to eliminate false positives (e.g., "jinja" the Python library, "ren" in "transparent"). 213 new candidates were identified.

2. **YAML near-miss scan:** All 2,329 paper files were scanned for entries with `is_benchmark`, `is_eval`, or `is_dataset` flags AND 0 < max(rv_*) < 50. 108 near-miss candidates were identified.

Combined: 321 new candidates, including 46 papers that arguably belonged in the original 401 (rv_* ≥ 50 AND benchmark terms in extract, but not flagged as benchmark/eval/dataset in metadata).

### Phase 2: External Discovery

Three parallel search strategies were executed:

1. **Tradition-specific web searches:** 32 targeted queries across 8 tradition groups (Judaism, Dharmic, East Asian, African/Indigenous, other) plus cross-tradition queries, using Google Scholar, arXiv, Semantic Scholar, and HuggingFace Datasets. 16 follow-up searches were conducted for promising leads. Total: 48 searches yielding 35 deduplicated discoveries.

2. **Citation chain analysis:** For each Top 15 benchmark and 14 background extracts, citing and cited papers were searched via Semantic Scholar and Google Scholar. 20 web searches were conducted.

3. **Data URL verification:** HTTP HEAD requests (with GET fallback) were sent to all 47 gate-passer DATA_URLs with 15-second timeouts. Results: 43 VERIFIED_ACCESSIBLE, 1 AUTH_REQUIRED (BuddhismEval HuggingFace 401), 3 NOT_FOUND.

### Phase 3: Ground-Truth Benchmark Assessment

All 50 gate-passing benchmarks (47 from v2 matrix + 3 edge cases) were assessed by reading the vault paper YAML frontmatter, abstract, and PDF extract (first ~3,000 characters where available). Each benchmark was scored on 24+ features across 5 categories:

- **Category A (Construct Identity):** A1 primary construct, A2 knowledge-vs-reasoning ratio, A3 values alignment relevance (0-100), A4 bias-values conflation, A5 theological depth, A6 moral dilemma presence, A10 maturity level, A12 Bloom's taxonomy level
- **Category B (Epistemological):** B1 epistemic stance, B3 monolith treatment, B6 emic/etic framing, B8 tradition-internal diversity
- **Category G (Values Content):** V1 values-vs-knowledge proportion, V2 ethical reasoning required, V3 tradition-specific concepts, V8 normative pluralism, V9 application context
- **Category L (Linguistic):** L1 source language fidelity, L2 language register, L7 sacred text involvement
- **Category Q (Psychometric):** Q1 IAA reported, Q4 ceiling risk, Q5 floor risk, Q10 sample size adequacy

Assessment was split across two parallel agents (IDs 1-16 and IDs 17-47) to maximize throughput. Confidence levels were assigned: 24 high, 20 medium, 6 low.

---

## Analysis

### Sensitivity Analysis

Four robustness analyses were performed on the corrected feature matrix:

1. **Weight sensitivity sweep:** RD/PE/CI weights were varied in 5-percentage-point increments (RD: 20-60%, PE: 15-55%, CI: 5-45%, summing to 100%), producing ~78 valid combinations. For each combination, composite scores and Top-15 membership were recomputed for all 47 gate-passers. Kendall's tau was computed against the baseline ranking.

2. **Gate threshold sensitivity:** The RD minimum gate was varied from 15 to 50 in steps of 5. At each threshold, the number of gate-passers and number of traditions represented were recorded.

3. **Bootstrap confidence intervals:** 10,000 bootstrap iterations were performed. In each iteration, weights were sampled from a Dirichlet distribution centered on (0.40, 0.35, 0.25) with concentration parameter α=20. Composite scores and ranks were recomputed. 95% CIs and Top-15 membership probabilities were recorded.

4. **Feature leave-one-out:** Each of the active scoring features was removed individually, weights renormalized, and composite scores recomputed. Maximum rank displacement and Kendall's tau were recorded.

### Statistical Tests for Paper Claims

Seven hypothesis tests were performed, one per paper claim:

| Claim | Test | Implementation |
|-------|------|----------------|
| 1. Tradition asymmetry | Chi-squared goodness-of-fit vs. uniform and vs. corpus proportion | `scipy.stats.chisquare` |
| 2. Knowledge-reasoning conflation | Binomial test on proportion of reasoning-focused benchmarks | `scipy.stats.binomtest` |
| 3. Data availability bottleneck | Exact binomial on verified accessibility | `scipy.stats.binomtest` |
| 4. Structural epistemic injustice | Logistic regression (gate-passage ~ tradition_family + language + venue) | `statsmodels.api.Logit` |
| 5. Field recency | One-sample proportion test + bootstrap median year CI | `scipy.stats.binomtest` + bootstrap |
| 6. WEIRD bias | Fisher's exact test (WEIRD/non-WEIRD × passes_gates) | `scipy.stats.fisher_exact` |
| 7. Bias-values conflation | Binomial test on proportion of bias-focused benchmarks | `scipy.stats.binomtest` |

### Inter-Feature Correlations and Clustering

Pairwise Spearman rank correlations were computed for 10 numeric features across all 401 entries using `scipy.stats.spearmanr`. Hierarchical clustering with Ward linkage was applied to z-score-normalized features for the 47 gate-passers using `scipy.cluster.hierarchy`. Cluster assignments (k=3,4,5,6) were compared against tradition family and format type using Adjusted Rand Index (`sklearn.metrics.adjusted_rand_score`).

### Gate-Passage Predictor Model

Binary logistic regression was fitted with `statsmodels.api.Logit`, predicting gate-passage (0/1) from: tradition family (one-hot, Abrahamic reference), format (one-hot), language (English binary), year (centered), venue tier (ordinal), is_benchmark, is_eval, and R1 tradition count.

### Void Factor Taxonomy

All 14 traditions were scored on 6 structural factors (0-5 scale): digital corpus availability, NLP community size, formalizability, data sovereignty constraints (0/1), institutional support, and publication infrastructure. A benchmark readiness index was computed as the sum of factors 1-3 (excluding sovereignty, which reflects community agency, not deficit). Point-biserial correlation was computed between readiness index and benchmark existence (binary).

### Vault-Wide Distribution Analysis

All 2,329 paper YAML files were parsed using regex extraction (`re.search(r'^rv_fieldname:\s*(\d+)', content, re.MULTILINE)`) to avoid the parse/rebuild YAML safety hazard. Per-tradition statistics (mean, median, max, std, count ≥ 50), co-occurrence matrices (14×14 with Jaccard similarity), and temporal trends (year × tradition counts) were computed.

---

## Computational Environment

- **Python:** 3.9 (via `../.venv/bin/python`)
- **Key libraries:** scipy (stats, cluster, hierarchy), scikit-learn (metrics), statsmodels (logit), matplotlib 3.9.4, seaborn 0.13.2, numpy, pandas
- **YAML parsing:** Regex-based extraction only (never `yaml.load()` — safety rule due to prior 422-file corruption incident)
- **Parallel execution:** 8 waves of background agent swarms (up to 4 concurrent), 26 total agent invocations
- **Dashboard:** ECharts 5 (CDN), Bootstrap 5.3 (CDN), self-contained static HTML
- **Rate limits:** 2-second delays between HTTP requests for URL verification; Semantic Scholar queries throttled to avoid HTTP 429

---

## Limitations and Decisions

1. **Single-assessor scoring:** The 109-feature taxonomy was scored by a single assessor (Claude) reading paper extracts. No inter-rater reliability was computed for the expanded features. This is acknowledged as a limitation; LLM-based IRR simulation is proposed as a future step.

2. **Extract availability:** Only 26 of 50 assessed benchmarks had readable PDF extracts. For the remaining 24, scoring was based on YAML frontmatter (title, abstract) only, resulting in lower confidence ratings.

3. **R2 improvement is partial:** The recalibrated R2 still shows 68.8% at depth=1 (reduced from 85.3%). A more fundamental redesign using rubric-based expert scoring would be needed for publication-quality measurement.

4. **Bootstrap assumption:** The Dirichlet-sampled weight perturbation assumes axis weights are the primary source of ranking uncertainty. Feature measurement error is not modeled.

5. **Claim 6 reversal:** The WEIRD bias test used a binary WEIRD/non-WEIRD classification based on author country approximated from language and venue. A more granular geographic analysis would require author affiliation geocoding.

6. **LLM trial items designed but not executed:** The 45 construct-validity items and 10 bias-values paired items were designed and scripted but require API credits to execute. Dry-run tested only.

7. **Void factor scores are expert-assigned, not empirically derived.** The 6-factor taxonomy uses the council's domain knowledge rather than measured data. Correlation with benchmark existence (r=0.66) should be interpreted as face validity, not causal evidence.
