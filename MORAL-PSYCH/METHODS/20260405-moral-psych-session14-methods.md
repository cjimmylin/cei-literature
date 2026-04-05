# Methods: Cross-Vendor Dashboard Expansion for Moral Psychology Benchmarks

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`

## Data and Materials

The dashboard draws on 207 trial JSON files (23 benchmarks x 9 models) stored in `MORAL-PSYCH/TRIALS/` and vendor-specific subdirectories. The nine models span three vendors: Anthropic (Claude Opus, Sonnet, Haiku), Google (Gemini 2.5 Flash, 2.5 Flash-Lite, 2.5 Pro, 3.1 Pro), and OpenAI (GPT-5 Codex, GPT Mini). All trials were administered on 2026-04-04.

The cross-vendor comparison data was pre-computed in `COMPARISON/20260404-cross-vendor-comparison.json`, containing per-benchmark model values with extracted primary metrics via dot-path resolution (e.g., `profile_interpretation.ratio` for MFQ-30, `scoring.P_score` for DIT).

## Procedure

The dashboard generator (`generate_dashboard.py`) was modified to expand the model comparison analytics from 3 Anthropic models to all 9 tested models. The expansion followed the existing "fat data, thin client" architecture where Python pre-computes all analytics and emits `data.js` as JavaScript constants; the browser performs zero computation.

The data contract was changed from named field access (e.g., `opus`, `sonnet`, `haiku` keys) to a dictionary keyed by model identifier (e.g., `data: {"anthropic_opus": [...], "anthropic_sonnet": [...], ...}`). This matched the structure already used by the cross-vendor analysis (Tab 12), ensuring internal consistency.

For the Trials tab (Tab 5), a model selector dropdown was added that allows users to switch the displayed model without page reload. The chart re-renders on selection change using ECharts' `setOption` with `notMerge=true` to prevent option accumulation.

For the Model Comparison tab (Tab 11), four chart functions were converted from hardcoded three-series rendering to loop-based rendering that iterates over the `modelKeys` array. Visual differentiation was applied: vendor-lead models (Opus, Gemini Flash, Codex) received 3px solid lines in the radar chart, while secondary models received 1.5px dashed lines with reduced area opacity (0.05) to maintain readability with 9 overlapping series.

The trial table was expanded from 3 to 9 model columns with dynamically generated table headers. Column colors match the per-model color assignments used throughout the dashboard for visual consistency.

## Analysis

Four sub-analytics were computed for each of the 9 models:

1. **MFT Foundation Profiles**: Five-foundation radar values (Care, Fairness, Loyalty, Authority, Sanctity) approximated from MP4 (Moral Foundations Vignettes) care score using fixed ratios (Fairness = care x 0.95, Loyalty = care x 0.65, Authority = care x 0.55, Sanctity = care x 0.45).

2. **Kohlberg P-Scores**: Direct extraction from MP3 (DIT-1) and MP6 (Teacher DIT) primary metrics across all 9 models.

3. **Classification Accuracy**: Direct extraction from MP10 (MoralCode), MP20 (M3oralBench), and MP22 (TracingMF) accuracy metrics.

4. **Dual Process**: Direct extraction from MP7 (TrolleyBench ECI) and MP-DP (Dual Process CoT effect).

Bar chart widths were reduced from 30px to 14px maximum to accommodate 9 grouped bars per benchmark category. ECharts scroll legends (`type: 'scroll'`) were used for all Tab 11 charts to handle the expanded legend without overflow.

## Computational Environment

- Python 3.9 (via `.venv`)
- ECharts 5, Bootstrap 5.3 (client-side)
- Dashboard served locally via `python3 -m http.server 8765` for Playwright verification
- Playwright MCP plugin for automated browser testing

## Limitations and Decisions

1. **MFT foundation approximation**: Per-foundation Likert scores are not available in the cross-vendor comparison JSON. Foundation profiles were approximated from the care baseline using fixed multipliers. Actual per-foundation values would require reading raw trial JSON files (207 files), which was deferred.

2. **Tab 5 single-model view**: A grouped bar chart showing all 9 models simultaneously (207 bars) was rejected in favor of a dropdown selector, as the visual density would be unreadable. The trade-off is that cross-model comparison on Tab 5 requires manual switching; Tab 11 provides the simultaneous comparison.

3. **Annotation text not updated**: The expert council annotations in `_tab_annotations.py` still reference the 3-model Anthropic comparison. These were not updated in this session to avoid scope creep; the annotations are substantive expert commentary that should be reviewed by the council rather than auto-modified.
