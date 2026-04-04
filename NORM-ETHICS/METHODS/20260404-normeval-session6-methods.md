# Methods: NormEval Session 6 — 12-Member Council Analysis

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The primary dataset was a 37-benchmark feature matrix (`STATISTICS/20260402-normative-benchmark-feature-matrix.json`) characterizing normative ethics benchmarks for LLMs across 26 features organized into four axes: Normative Depth (A1-A8), Practical Ease (B1-B9), Citation Impact (C1-C5), and Metadata (D1-D4). The matrix had been assembled in prior sessions through systematic search across seven databases with PRISMA-compliant methodology.

Secondary data included: (a) the 2,043-paper CEI Literature Vault with YAML frontmatter containing ethics scores, benchmark flags, and tradition-level classifications; (b) five prior implementation trial reports (T1-T5, 150 items) using Claude Opus 4.6 as both subject and evaluator; (c) 123 background paper extracts from a 14-member literature review council; and (d) 177-entry bibliography.

## Procedure

### Expert Council Assembly

A 12-member interdisciplinary analysis council was convened, distinct from the 14-member literature review council used for the paper's introduction. Council members spanned statistics, taxonomy/PRISMA methodology, evaluation infrastructure engineering, normative philosophy, cross-cultural sociology, comparative religious ethics, machine learning, data visualization, prompt engineering, library science, peer review, and academic writing. Each member was assigned to specific workstreams based on expertise alignment.

### Parallel Agent Swarm Architecture

Work was organized into 8 workstreams (W1-W8) executed across 4 sequential swarms of 2-3 parallel agents each (11 agents total). Each agent operated on independent data with no shared state, coordinating through output files following a dependency graph:

- **Swarm 1** (3 agents): Self-assessment trials T6-T10 | Computational analysis W1+W2 | Vault mining W3
- **Swarm 2** (3 agents): Trials T11-T15 + expanded | External search W4 | Adversarial peer review W7
- **Swarm 3** (3 agents): Dashboard construction W6 | Care ethics prototype W5-F | v2 feature scoring W3C
- **Swarm 4** (2 agents): Paper improvements W8 | Dashboard finalization W6b

### W1: Computational Analysis

A Python script (`PYTHON/normeval_computational_analysis.py`) was written to perform 10 analyses on the 37x26 feature matrix:

1. **Spearman correlation matrix** across all numeric features, identifying near-redundant pairs (r > 0.8) and anti-correlations
2. **PCA dimensionality reduction** to 3 components with explained variance analysis and cluster visualization
3. **Composite weight sensitivity analysis** sweeping 231 ND/PE/CI weight triplets (5% increments, sum=1.0), testing Top 15 stability
4. **Hypothesis tests** for 5 paper claims: binomial (C1, C4), two-proportion z-test (C2), permutation (C3), Mann-Whitney U (C5)
5. **Power analysis** computing minimum sample sizes at alpha=0.05, power=0.80 for observed effect sizes
6. **Feature importance** via random forest permutation importance with COMPOSITE as target
7. **ND-PE tradeoff regression** (linear model, R-squared, outlier identification)
8. **Shannon entropy** over normalized tradition scores per benchmark
9. **Temporal trend analysis** correlating year with ND, PE, CI
10. **Anomaly detection** via Mahalanobis distance on standardized numeric features

Statistical tests used scipy.stats (spearmanr, mannwhitneyu, binom_test, norm.cdf), sklearn (PCA, RandomForestRegressor), and numpy. The Python venv at `../../.venv/bin/python3` (Python 3.9) provided all dependencies.

### W2: Data Availability Audit

All 37 benchmark URLs from the B3_url field were catalogued by host type (GitHub, HuggingFace, Public Download, None). License information was extracted from the B5_license field and cross-referenced against repository metadata where available.

### W3: Vault Mining

Six search strategies were applied to the 2,043-paper vault:
1. Audit of 63 papers with `normative_ethics_benchmark` field (37 in matrix, 26 not)
2. Ethics score mining: `ethics_overall >= 80` cross-referenced against the 37 known benchmarks
3. Care ethics scan: 15 papers with `care_ethics >= 50` examined for evaluation instruments
4. Non-Western ethics scan: papers with high `nw_confucian`, `nw_ubuntu`, `nw_islamic_ethics`, etc.
5. Benchmark tag cross-reference: `is_benchmark: "Yes"` + `ethics_overall >= 50` not in the 37
6. Keyword scan of titles and abstracts for normative ethics terms

All vault reads used regex extraction from YAML frontmatter (never parse-rebuild round-trips per safety rules).

### W4: External Search

Five strategies targeted papers outside the vault:
1. Forward citation search via Semantic Scholar for papers citing the 5 trial benchmarks
2. arXiv search for post-March 2026 normative ethics benchmarks
3. HuggingFace Hub dataset search for ethics/moral tags
4. Targeted search for non-Western tradition benchmarks
5. Adjacent field scan (AI safety, constitutional AI, legal AI, biomedical ethics)

### W5: Self-Assessment Trials

Claude Opus 4.6 self-evaluated on all 15 gate-passing benchmarks. For benchmarks with accessible data (GREEN triage), items were drawn from published datasets. For benchmarks without direct data URLs (YELLOW), items were constructed from published methodology descriptions, paper examples, and PDF extracts. Each trial used n=30 items (or all items for small datasets), stratified by ethical tradition or domain where applicable.

Two-pass scoring was planned: standardized prompt template for cross-benchmark comparison, plus native benchmark instructions for fidelity. Self-assessment annotations recorded discriminative power, refusal sensitivity, format constraints, ground truth defensibility, cultural assumptions, and contamination risk per benchmark.

Expanded trials increased T1 (ETHICS) and T3 (MoralReason-QA) to n=100, providing tighter confidence intervals on ceiling effect and framework difficulty hierarchy claims.

### W5-F: Care Ethics Prototype

Ten multi-turn dialogue scenarios (3 turns each, 30 total turns) were designed across 5 domains (healthcare, education, family, workplace, community) testing Tronto's four care ethics dimensions: attentiveness, responsibility, competence, and responsiveness. Each scenario featured a power-asymmetric caregiving relationship with evolving dynamics across turns. Scoring used a 0-4 rubric per dimension per turn (max 16 per scenario, 480 total).

### W6: Dashboard

A Python generator (`PYTHON/generate_normeval_dashboard.py`) read 10 JSON data sources and emitted a `data.js` file (130KB) containing pre-computed analytics as JavaScript constants. The browser-side application used ECharts 5 for charts and Bootstrap 5.3 for layout, with 9 tabs: Overview, All Papers Ranking, Feature Matrix, Tradition Coverage, Composite Scoring, Implementation Trials, Data Availability, Cross-Model Comparison (placeholder), and Gaps & Recommendations.

### W7: Adversarial Peer Review

A simulated peer review assessed the paper across 6 dimensions: single-rater bias (A6 scoring), self-evaluation circularity, composite score design, claim scope (all 5 claims individually), NeurIPS D&B compliance, and missing related work. The review used W1 statistical results and T1-T10 trial evidence as input.

### v2 Feature Framework

An expanded 47-feature framework (5 axes) was designed through council deliberation and scored on all 37 benchmarks. New features included: A1+ (10 non-Western tradition sub-scores), A9 (metaethical stance), A10 (temporal depth), A11 (scenario realism), A12 (moral psychology conflation risk), A13 (sacred/secular framing), B10 (contamination risk), B11 (prompt sensitivity), B12 (API accessibility), D4a-c (annotator detail), D5-D6 (version/documentation), and E1-E5 (empirical quality from trial data).

## Analysis

### Statistical Methods
- **Spearman rank correlations** for non-parametric feature associations
- **Principal Component Analysis** (3 components, standardized features)
- **Two-proportion z-test** with Bonferroni correction for framework accuracy comparisons
- **Cohen's h** for effect size of proportion differences
- **Binomial test** for count-based claims (ceiling effect, judgment-vs-reasoning)
- **Mann-Whitney U** for ND distribution comparison (available vs unavailable data)
- **Random forest permutation importance** (100 estimators) for feature contribution to composite
- **Shannon entropy** for tradition coverage diversity measurement
- **Mahalanobis distance** for multivariate outlier detection

### Scoring Formulas
- ND = A2(0.25) + A6(0.20) + A1(0.15) + A3(0.15) + A5(0.15) + A4(0.10)
- PE = B7(0.30) + B3(0.20) + B4(0.15) + B6(0.15) + B9(0.10) + B5(0.10)
- CI = C2(0.35) + C4(0.30) + C3(0.20) + C5(0.15)
- COMPOSITE = ND(0.40) + PE(0.35) + CI(0.25)
- Hard gates: ND >= 40 AND data publicly available

## Computational Environment

- Python 3.9 via `../../.venv/bin/python3`
- Key libraries: numpy, scipy (stats), sklearn (PCA, RandomForestRegressor), json
- Claude Opus 4.6 (1M context) as both analysis engine and self-evaluation subject
- ECharts 5.5.1 + Bootstrap 5.3 (CDN) for dashboard
- Playwright for dashboard verification screenshots

## Limitations and Decisions

1. **Self-evaluation bias:** Claude Opus 4.6 served as both subject and evaluator in all trials. Panickssery et al. (2024) demonstrated LLM evaluators systematically favor their own outputs. Results are framed as preliminary self-assessment pending cross-model replication.

2. **Paper-derived items:** For YELLOW-triaged benchmarks (PrinciplismQA, Pluralistic Moral Gap), items were constructed from published methodology rather than drawn from actual datasets. These trials test the model's understanding of the benchmark's design more than its performance on actual items.

3. **Sample sizes:** n=30 per trial provides adequate power for detecting large effects (Cohen's h > 0.5) but is underpowered for detecting medium effects (h ~ 0.3). The expanded trials (n=100) partially address this for Claims 1 and 2.

4. **Single-rater v2 features:** Several v2 features (A9 metaethical stance, A11 scenario realism, A12 conflation risk) are scored by a single non-human rater (Claude). These require human validation before publication.

5. **Claim 4 discrepancy:** The computational analysis counted 22/37 (59.5%) as testing "judgment only," while the paper spine states 28/37 (75.7%). The discrepancy likely arises from different coding rules for the A3 (reasoning type) field. Resolution requires manual recount with explicit decision criteria.

6. **Care ethics prototype scoring inflation:** The 93.3% aggregate score on the care ethics prototype is almost certainly inflated by self-evaluation. The relative dimension rankings (Attentiveness highest, Competence lowest) may be more informative than absolute scores.
