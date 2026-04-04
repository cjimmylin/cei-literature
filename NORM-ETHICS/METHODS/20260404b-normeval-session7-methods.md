# Methods: NormEval Claim 4 Resolution and Corpus Expansion

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

**Source corpus:** 37 normative ethics benchmarks for LLMs (2021-2026) from the v1 feature matrix (`20260402-normative-benchmark-feature-matrix.json`), each scored across 26 features organized into four axes: Normative Depth (ND), Practical Ease (PE), Citation Impact (CI), and Metadata (D).

**Expansion candidates:** 12 papers identified through systematic vault mining of 2,043 papers in the CEI Literature Vault, plus 5 external papers identified via targeted arXiv and Semantic Scholar searches with emphasis on non-Western traditions (Islamic benchmarks) and methodological contributions.

**External paper sources:** arXiv preprints accessed via `https://arxiv.org/pdf/{ID}`. Five papers downloaded: Xu et al. (2603.23659), Zhang et al. (2603.10588), IslamicMMLU (2603.23750), IslamicLegalBench (2602.21226), Du et al. (2505.08106).

## Procedure

### Phase 1: Claim 4 Judgment-vs-Reasoning Recount

A systematic recount was conducted to resolve a factual discrepancy in the manuscript. The feature matrix encodes benchmark reasoning assessment using a three-category classification (`A3_reasoning`):

- **Judgment-only (J):** Benchmark evaluates what the model concludes without assessing reasoning process
- **Both (B):** Benchmark evaluates judgment AND includes some reasoning quality assessment
- **Reasoning-focused (R):** Benchmark primarily evaluates how the model reasons

Each of the 37 benchmarks was reviewed against four decision criteria: (1) `B1_format` as primary indicator (MCQ/binary/pairwise → J), (2) `A2_depth` for framework engagement, (3) `B8_scorer_type` for rubric-based reasoning assessment, and (4) `A3_reasoning_refined` (v2 continuous scale: 25=J, 50=B, 75=framework, 100=procedural). A one-line justification was produced for each coding decision.

The recount confirmed: J=22, B=5, R=10 (total=37). The manuscript's spine stated "28 of 37" while the results body stated "22 of 37" — the discrepancy arose from the spine counting J+B (=27) with an off-by-one arithmetic error.

### Phase 2: Hypothesis Test Revision

Three binomial tests were computed (scipy.stats.binomtest, H₀: p=0.5):

| Framing | k | n | Proportion | p-value | Significant |
|---------|---|---|-----------|---------|-------------|
| Strict (J-only > 50%) | 22 | 37 | 59.5% | 0.162 | No |
| Broad (J+B > 50%) | 27 | 37 | 73.0% | 0.004 | Yes |
| Inverted (R < 50%) | 10 | 37 | 27.0% | 0.004 | Yes |

The inverted framing was adopted for the manuscript: "Only 10 of 37 benchmarks (27%) evaluate moral reasoning quality." Seven references to the erroneous "28 of 37" count were identified and corrected across five paper files.

### Phase 3: External Paper Ingestion

Five papers were downloaded from arXiv with 3-second inter-request delays. PDFs were verified via `%PDF-` header check. Text extraction used `pdftotext -layout` (poppler-utils). For each paper, three files were created: (1) vault paper entry with YAML frontmatter in `papers/YYYY-Author-Title.md`, (2) text extract in `PDF Extracts/YYYY/`, (3) NormEval background copy in `NORM-ETHICS/BACKGROUND/EXTRACT/`.

### Phase 4: Feature Matrix Scoring

All 17 new benchmarks were scored across the full feature schema (60+ dimensions). Scoring was conducted in three parallel batches:
- Batch 1 (IDs 38-43): 6 vault papers — OffTheRails through Basu Multilingual
- Batch 2 (IDs 44-49): 6 vault papers — CVC through Normative Evaluation
- Batch 3 (IDs 50-54): 5 external papers

Each benchmark was scored by reading its vault metadata and PDF extract, then evaluating across Sections A (Normative Depth, 14 features), B (Practical Ease, 12 features), C (Citation Impact, 5 features), D (Metadata, 6 features), and E (Discriminative Power, 5 features). Composite scores were computed using the established formula: COMPOSITE = ND×0.40 + PE×0.35 + CI×0.25. Hard gates applied: ND ≥ 40 AND public data available.

Calibration anchors from the original 37 were maintained: MoReBench (ND=87.0), ETHICS (ND=59.8, PE=95.0), Greatest Good (ND=53.0).

### Phase 5: Expanded Corpus Analysis

The expanded 54-benchmark matrix was analyzed:

1. **Hypothesis tests** — all 5 claims re-tested at n=54 using binomtest and Mann-Whitney U
2. **Spearman correlations** — 8 key numeric features (28 pairs)
3. **Sensitivity analysis** — 18 weight triplets (ND: 20-60%, PE: 20-60%, CI: 10-50%) tested for Top 15 stability
4. **Temporal trends** — Spearman correlation between publication year and ND score

### Phase 6: Dashboard Update and Deployment

The dashboard data generator (`generate_normeval_dashboard.py`) was modified to load the expanded feature matrix. The regenerated `data.js` (172KB) was deployed to a new public GitHub repository (`cjimmylin/cei-normeval-dashboard`) with GitHub Pages enabled.

## Analysis

**Composite scoring formula:**
- ND = A2(0.25) + A6(0.20) + A1(0.15) + A3(0.15) + A5(0.15) + A4(0.10)
- PE = B7(0.30) + B3(0.20) + B4(0.15) + B6(0.15) + B9(0.10) + B5(0.10)
- CI = C2(0.35) + C4(0.30) + C3(0.20) + C5(0.15)
- COMPOSITE = ND×0.40 + PE×0.35 + CI×0.25

**Gate criteria:** ND ≥ 40 (minimum normative depth) AND publicly available data (GitHub, HuggingFace, or equivalent).

**Wilson confidence intervals** computed for all binomial proportions at 95% level.

## Computational Environment

- Python 3.9 (`/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python3`)
- scipy (binomtest, mannwhitneyu, spearmanr), numpy, sklearn
- pdftotext (poppler-utils) for PDF text extraction
- GitHub CLI (`gh`) for repository creation and Pages deployment
- ECharts 5 + Bootstrap 5.3 for dashboard rendering

## Limitations and Decisions

1. **Single-rater scoring:** All 17 new benchmarks scored by a single AI system (Claude Opus 4.6). Inter-rater reliability was not assessed. Mitigation: calibration anchors from original 37 were used to constrain scoring drift.

2. **Citation data staleness:** Citation counts for 2025-2026 papers are inherently low due to recency. CI scores for new benchmarks cluster in the 15-30 range, which may undervalue impactful recent work.

3. **v2 features not extended:** The 18 v2 features (A9-A13, B10-B12, D4a-D6, E1-E5) were scored only for the original 37 benchmarks. The expanded matrix uses v1 schema for IDs 38-54. This means some dashboard visualizations drawing from v2 data show only 37 benchmarks.

4. **IslamicMMLU gate failure:** Despite being a massive benchmark (10,013 items) with HuggingFace leaderboard, IslamicMMLU received ND=30 because it tests factual Islamic knowledge rather than normative ethical reasoning. This reflects a deliberate design choice in the framework to distinguish knowledge evaluation from reasoning evaluation.

5. **Top 15 instability:** With 24 gate-passing benchmarks (up from 15), the Top 15 is no longer perfectly gate-determined. The paper's Session 6 finding — "Top 15 is perfectly gate-determined; composite weights have zero effect" — must be revised. Only 1/18 weight combinations produce the same Top 15.
