# Methods: Claim 8 Statistical Formalization and Methodological Disclosure

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`

## Data and Materials

Values relevance assessment scores (A3) were drawn from two Claude-assessed feature matrix batches (`data/20260404-claude-assessment-batch1.json`, `data/20260404-claude-assessment-batch2.json`). Each batch contained structured assessments of gate-passing benchmarks across 24 values-relevant dimensions, with A3_values_relevance scored on a 0-100 scale measuring the degree to which a benchmark engages genuine religious values alignment rather than knowledge recall or bias detection.

Sixteen gate-passing benchmarks had complete A3 scores. Scores ranged from 5 to 65, with a median of 27.5.

## Procedure

### Claim 8 Statistical Testing

Four complementary tests were applied to the A3 score distribution to formalize the "values relevance failure" finding previously reported qualitatively in Section 5.3 of the paper:

1. **One-sample t-test** against the scale midpoint (50), testing whether the mean A3 score differed significantly from the theoretical neutral point. Result: t(15) = -4.93, p = 0.000181, two-tailed.

2. **Wilcoxon signed-rank test** against 50, as a non-parametric alternative robust to non-normality. Result: W = 5.0, p = 0.00061.

3. **Binomial test** of the proportion achieving A3 >= 50 against 50%, testing whether a majority of benchmarks meet a minimal values relevance threshold. Result: 3/16 (18.8%), p = 0.011.

4. **Binomial test** of the proportion achieving A3 >= 75 against 50%, testing whether a majority achieve strong values engagement. Result: 0/16 (0.0%), p = 0.000015.

Cohen's d was computed as the standardized mean difference: d = (30.0 - 50) / 16.2 = -1.23, indicating a large effect.

### Methodological Disclosure Protocol

Three methodological caveats were identified from the session handoff's "Known Issues" list and formalized through parallel disclosure in the paper (Section 5.7, appended paragraph) and the dashboard (collapsible annotations with visual caveat badges):

1. **T2 blinding asymmetry:** The original T2 Arabic MCQ trials for three Claude models (Opus, Sonnet, Haiku) were self-evaluated with gold-standard answer labels visible, making reported accuracy figures upper-bound estimates. Subsequent cross-vendor trials (OpenAI, Gemini) followed a blind protocol where gold labels were withheld during model evaluation.

2. **Same-vendor scorer bias:** All rubric-based construct validity scoring was performed by Claude Opus 4.6, including scoring of responses from other Claude-family models (Sonnet, Haiku). RLHF-trained models within the same family may share latent evaluative preferences, potentially inflating rubric scores for same-vendor responses.

3. **Gemini data provenance:** Gemini model results were collected using a backfilled protocol with template-based response extraction rather than the interactive API administration used for Claude and OpenAI models. Uniformly low rubric scores (0.0 on Knowledge, Reasoning, Values) may partly reflect methodological artifact.

### Dashboard Side-by-Side Layout

The side-by-side chart+annotation layout was implemented using Bootstrap 5's responsive grid system. Charts were placed in `col-md-7` containers (58.3% width on screens >= 768px) with annotations in adjacent `col-md-5` containers (41.7% width). The `.annotation-sidebar` class applied `position: sticky; top: 70px` to keep annotations visible while scrolling through tall charts. On screens below 768px, the existing mobile breakpoint rule `[class*="col-md-"] { flex: 0 0 100%; max-width: 100%; }` collapsed the layout to single-column stacking.

## Analysis

No new analytical methods were introduced beyond the four statistical tests described above. All computations used scipy.stats (Python 3.9) via the project's virtual environment.

## Computational Environment

- Python 3.9 (`.venv/bin/python3`)
- scipy.stats: ttest_1samp, wilcoxon, binomtest
- Dashboard: ECharts 5.5.0, Bootstrap 5.3.3, Inter font (Google Fonts CDN)
- Verification: Playwright MCP for browser-based screenshot validation
- Deployment: GitHub Pages via `cjimmylin/cei-rv-dashboard` repository

## Limitations and Decisions

1. **A3 sample size (n=16):** Only 16 of 47 gate-passers had complete A3 assessment from the Claude-assessed feature matrix. The paper's broader figure of 33.6/100 includes additional assessments not captured in the formal JSON batches. The formal test uses the 16 entries with verified A3 scoring. Despite the small sample, the effect size (d=-1.23) is large and all four tests converge on significance.

2. **Scale midpoint as null hypothesis:** Using 50 as the null assumes the A3 scale has a meaningful midpoint. The scale was designed with 50 representing "moderate values engagement," so this assumption is defensible.

3. **Side-by-side layout scope:** The layout was applied to Tabs 2-5 but not Tab 6 (Cross-Vendor), which already used side-by-side chart pairs. Adding annotation sidebars to Tab 6 would have compressed the rubric heatmap and T2 bar chart below readability thresholds.

4. **Caveat badges in collapsible sections:** Methodological caveats are placed inside "Read more" expandable sections. This follows the council's recommendation to use bold summaries + collapsible detail, but means the caveats are not visible by default. The annotation summaries reference the caveats indirectly.
