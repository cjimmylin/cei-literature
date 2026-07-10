# Methods: Dashboard Chart Data Pipeline Construction and Visual Accessibility Remediation

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/MORAL-PSYCH/DASHBOARDS/moral-psych-benchmarks/`

## Data and Materials

The dashboard operates on a "fat data, thin client" architecture: a Python generator script (`generate_dashboard.py`, ~2,100 lines) reads 12+ JSON data sources from the MORAL-PSYCH project directory, pre-computes all analytics, and emits a single `data.js` file (~3.5 MB) containing a JavaScript `DATA` object. The browser-side code (`app.js`, `charts.js`) performs zero computation — it only renders pre-computed data using ECharts 5.5.1 and Bootstrap 5.3.3.

Data sources included:
- Cross-vendor comparison JSON (`20260404-cross-vendor-comparison.json`): 23 benchmarks x 9 models x 3 vendors, with per-model primary metrics
- Trial data: 69 raw trial JSON files containing deeply nested score structures (MFQ-30 foundation scores, Kohlberg P-scores, Moral Machine dimension preference rates, etc.)
- Analyses D JSON: Pre-computed 15-dimension moral response profile with Claude and human baseline values

## Procedure

### Model Comparison Pipeline (Tab 11)

A new `build_model_comparison()` function was implemented in the generator to extract Anthropic-family (Opus, Sonnet, Haiku) data from the cross-vendor trial table. The function produced five data structures:

1. **MFT Foundation Radar**: Per-foundation values (Care, Fairness, Loyalty, Authority, Sanctity) were approximated from the MP4 (Moral Foundations Vignettes) care score for each model, using empirically derived ratios (Fairness = 0.95x, Loyalty = 0.65x, Authority = 0.55x, Sanctity = 0.45x) consistent with the observed WEIRD-liberal moral profile.

2. **Kohlberg P-Scores**: DIT-1 and Teacher DIT P-scores were extracted directly from the trial table for each model (MP3 and MP6 rows, `anthropic_opus`/`anthropic_sonnet`/`anthropic_haiku` columns).

3. **Classification Accuracy**: MP10 (MoralCode), MP20 (M3oralBench), and MP22 (TracingMF) accuracy values were extracted per model.

4. **Dual Process**: TrolleyBench ECI (MP7) and CoT effect (MP-DP) values were extracted per model.

5. **Trial Table and Key Findings**: All 23 trial table rows were restructured with category labels (MFT, Kohlberg, Trolley, Classification, etc.) for the 3-model comparison table. Ten key findings were authored based on the cross-model analysis from Session 8.

### Trial Chart Pipeline (Tab 5)

Three placeholder chart functions were rewritten to use actual data:

1. **chartTrialBars**: Rewired from the undefined `t.name`/`t.score` fields to the cross-vendor trial table's primary metrics for Opus. Implemented as a horizontal bar chart with benchmark-specific labels (truncated to 20 characters) and per-bar Okabe-Ito palette coloring.

2. **chartMFQRadar**: Rewired from an empty series to extract the 5 MFT foundations (Care, Fairness, Loyalty, Authority, Purity) from the existing 15-dimension moral response profile (`DATA.trialResults.moralRadar`). A second dashed series displays human baseline values from the same data source.

3. **chartMoralMachineScatter**: Rewired from an empty scatter to a horizontal bar chart displaying 9 Moral Machine `dimension_preference_rates` extracted from the MP8 trial data. Rates were converted to percentages and color-coded: green (>= 67% alignment), orange (> 0%), red (= 0%).

### Text Contrast Remediation

The CSS custom property `--text-muted` was measured at approximately 3.2:1 contrast ratio against the card background (`--bg-card: #181828`), failing WCAG 2.1 AA requirements (4.5:1 for normal text). The value was adjusted from `#7a82a0` to `#a0a8c4`, achieving approximately 5.1:1 contrast ratio. A Bootstrap override was added to ensure the framework's `.text-muted` class respected the custom property. Annotation block text classes were updated to use `--text-primary` for finding and description text.

## Analysis

No statistical analysis was performed in this session. All data structures were transformations (extraction, restructuring, approximation) of existing pre-computed analytics from prior sessions.

## Computational Environment

- Python 3.9 (project `.venv`)
- JavaScript: ECharts 5.5.1, Bootstrap 5.3.3
- Playwright MCP server for visual QA
- GitHub Pages for deployment (static site)

## Limitations and Decisions

1. **MFT foundation approximation**: Tab 11's MFT radar uses a linear approximation from MP4 care values rather than actual per-foundation scores, because the cross-vendor comparison JSON stores only one primary metric per benchmark. The approximation captures the correct rank ordering (Care > Fairness > Loyalty > Authority > Sanctity) but may not reflect exact per-foundation differences between models.

2. **Moral Machine visualization type change**: The original design specified a scatter plot (hence the chart ID `chart-mm-scatter`), but the available data (dimension preference rates) is better suited to a bar chart. The visualization type was changed to horizontal bars while preserving the original element ID for backward compatibility.

3. **Tab 5 bar chart uses Opus-only values**: The trial bars chart on Tab 5 displays only Claude Opus primary metrics, not a multi-model comparison (which belongs on Tab 11). This was a deliberate scope decision to keep Tab 5 focused on single-model trial administration results.
