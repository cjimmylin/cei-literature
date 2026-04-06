# Methods: Manuscript v4 Rewrite and Dashboard v4 Construction

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`

## Data and Materials

The v4 manuscript drew on the following data sources, all produced in Session 19:

- **Full feature matrix** (`20260405-full-292-feature-matrix.json`): 292 benchmark candidates × 17 composite-determining features, with composite scores (PD, PE, CI, COMPOSITE) and Jenks tier assignments (top/high/med/low).
- **Tier assignment** (`ANALYSIS/20260405-tier-assignment.json`): Jenks natural breaks at [27.8, 43.0, 56.6] with GVF=0.83, theory×tier crosstab for 13 theories, and ranked list of all 292 candidates.
- **Cross-vendor comparison** (`COMPARISON/20260404-cross-vendor-comparison.json`): 9 models from 3 vendors (Anthropic, Google, OpenAI) × 23 benchmarks, with coefficient of variation and primary metrics per trial.
- **Trial results** (`TRIALS/20260404-trials-summary-v2.json`): 69 trial files (23 benchmarks × 3 Claude models) with structured scoring.
- **Computational analyses** (`ANALYSIS/20260404-analyses-A-C.json`, `-D.json`, `-E-H.json`): Factor analysis, UMAP clustering, temporal trends, gap analysis, health scorecard.
- **Downward impact analysis** (`METHODS/20260405g-downward-impact-analysis.md`): Claim-by-claim impact assessment from the v3 full-coverage expansion.

## Procedure

### Manuscript v4

The manuscript was rewritten from scratch in three parallel waves:

**Wave 1 (Foundation):** Three agents wrote simultaneously: (1) 15 publication-quality figures via matplotlib/seaborn from JSON data sources, (2) the Methodology section (§3, 8,210 words), and (3) the Introduction + Abstract (4,508 words total). All agents received the same data sources and statistics to ensure consistency.

**Wave 2 (Results):** Four agents wrote the three-part results structure simultaneously: (1) Results Part I Claims 1-3 (7,709 words), (2) Results Part I Claims 4-6 (7,897 words), (3) Results Part II Empirical (10,328 words), (4) Results Part III Integrated (6,770 words). Each agent read the actual JSON data files to extract precise statistics rather than relying on summary documents.

**Wave 3 (Synthesis):** Three agents wrote simultaneously: (1) Discussion (10,699 words, 7 subsections), (2) Conclusion + BibTeX (4,748 words + 168 entries), (3) Supplementary material (15,014 words across 4 files).

Total: 75,883 words across 13 markdown files, 15 figures, 30 main tables, 10 supplementary tables.

### Dashboard v4

The dashboard was constructed in two phases:

**Phase 1 (Data Pipeline):** Two agents wrote simultaneously: (1) `generate_dashboard.py` with 27 builder functions producing 49 data keys in a 530 KB `data.js`, and (2) `_tab_annotations.py` with 65 annotations across 10 tabs, each containing both a visible summary and an expandable manuscript-derived detail section.

**Phase 2 (Frontend):** Three agents wrote simultaneously: (1) `index.html` (1,000 lines) + `style.css` (1,015 lines) with 10-tab structure, guided narrative tour, and triple bind visual identity, (2) `app.js` (2,167 lines) with rendering logic, annotation system, and interactive features, (3) `charts.js` (1,456 lines) with 30+ ECharts visualization functions.

### Narrative Architecture

The v4 advances a "triple bind" thesis — the benchmark landscape is simultaneously theoretically narrow (MFT dominates quality), empirically undiscriminating (models converge), and culturally blind (0% non-Western quality). The three binds form a self-reinforcing system demonstrated through the infrastructure-quality-discrimination pipeline (r=-0.83 between composite quality and cross-model variation).

The 7 claims were derived by expanding the v2's 5 claims with two new findings: C4 (Cultural Quality Cliff) and C6 (Temporal Stagnation). C7 merges v2's cross-vendor convergence and scale sensitivity findings under the "RLHF Moral Fingerprint" framing. Claims were seeded and refined during writing, with the integrated findings section (Part III) connecting all claims through the pipeline thesis.

## Computational Environment

- Python 3.9 (`.venv/bin/python`)
- matplotlib 3.x, seaborn, numpy for figure generation
- pandoc + typst for PDF rendering
- ECharts 5.5.0 (CDN) for interactive dashboard charts
- Bootstrap 5.3.3 (CDN) for dashboard layout
- GitHub Pages for dashboard deployment

## Limitations and Decisions

1. **Full rewrite vs revision:** All prose was written from scratch rather than edited from v2. This ensures narrative consistency with the triple bind thesis but means some v2 passages that were well-crafted may have been replaced with less polished alternatives.

2. **Parallel agent consistency:** Writing in parallel maximizes speed but introduces risk of cross-section inconsistency (e.g., different agents may cite slightly different numbers for the same statistic). A consistency pass is recommended before final publication.

3. **Data-derived vs hardcoded statistics:** Figure generation and results agents read JSON data files directly. However, some statistics in the Introduction and Discussion were provided in agent prompts rather than computed from data, creating a risk of stale numbers if the data changes.

4. **Dashboard visual QA:** The Playwright browser context was unavailable during the session, so visual verification of all 10 dashboard tabs was not completed. Manual browser testing is needed.

5. **BibTeX rebuild:** The 168-entry BibTeX was written from known references rather than extracted from citation commands in the manuscript text. There may be citations in the text that lack BibTeX entries, or entries that are not cited.
