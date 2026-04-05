# Methods: Cross-Vendor LLM Benchmark Analysis and Dashboard Development

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`

## Data and Materials

### Source Data
Cross-vendor comparison data was loaded from two pre-computed JSON files:
- `COMPARISON/results/model-comparison.json` — 9-model metric table with gradient status, response lengths, rubric scores, bias-values correlations, and T2 accuracy for each model
- `COMPARISON/results/vendor-comparison.json` — vendor-level aggregation (3 vendors: Anthropic, OpenAI, Gemini) with mean metrics

### Models Evaluated
Nine models from three vendor families were included:
- **Anthropic:** Claude Opus 4.6, Sonnet 4, Haiku 4.5
- **OpenAI:** GPT-Codex, Codex-Mini
- **Google:** Gemini 2.5 Flash-Lite, 2.5 Flash, 2.5 Pro, 3.1 Pro

### Benchmark Items
Two benchmark types were administered to all models:
- **Construct Validity Battery:** 65 items across 4 construct types (Knowledge, Reasoning, Values, Bias) × 3 traditions (Islam, Christianity, Hinduism)
- **T2 Arabic MCQ:** 30 Islamic inheritance law (fara'id) items at Beginner (15) and Advanced (15) difficulty levels

## Procedure

### Expert Council Assembly
A 12-member expert council was assembled in a 3-tier structure:
- **Tier 1 — Core Reviewers (4):** Computational theology, LLM safety, cross-cultural NLP, benchmark design
- **Tier 2 — Methodological Auditors (4):** Psychometrics/IRT, applied statistics, computational linguistics, AI evaluation infrastructure
- **Tier 3 — Contextual Critics (4):** Islamic jurisprudence, philosophy of AI, comparative religion, science communication

The council was tasked with analyzing cross-vendor benchmark performance and producing both a written analysis document and a critique of the dashboard visualization.

### Dashboard Development Pipeline
1. **Data loading:** Cross-vendor JSON loaded at generation time by the Python dashboard generator script
2. **Pre-computation:** Response length arrays, rubric heatmap matrix, T2 accuracy arrays, V/K ratios, vendor radar data, and bias-values correlations computed in Python
3. **Embedding:** All analytics embedded as JavaScript constants via `json.dumps()` — browser performs zero computation
4. **Chart generation:** 5 ECharts charts + 1 HTML table added as Tab 6 ("Cross-Vendor LLM")
5. **Annotation enrichment:** 17 existing annotations enhanced + 6 new tab-level conclusion callouts added across all 6 tabs
6. **UX improvements:** Two rounds of council critique produced 15 total improvements (responsive CSS, print styles, figure numbering, save-as-PNG, dataZoom, footer, key findings, etc.)
7. **Citation cleanup:** Individual council member attributions removed; expert perspectives integrated as analytical prose

### Deployment
The dashboard was deployed to GitHub Pages via a GitHub Actions workflow:
- Public repository: `cjimmylin/cei-rv-dashboard`
- Single `index.html` file (self-contained, no external data dependencies beyond CDN libraries)
- Automated deployment on push to `main` branch

## Analysis

### Cross-Vendor Metrics
The following metrics were computed per model and per vendor:
- **K<R<V gradient:** Boolean indicator of whether mean response length follows Knowledge < Reasoning < Values monotonically
- **V/K ratio:** Values mean length / Knowledge mean length (range: 1.03x to 9.18x)
- **Rubric scores:** 5-dimension accuracy (Knowledge, Reasoning, Values, Bias, Values-Paired) on 0.0-1.0 scale
- **T2 accuracy:** Percentage correct on 30-item Arabic MCQ (range: 6.7% to 100%)
- **Bias-values r:** Pearson correlation between bias and values response lengths (independence threshold: r < 0.30)

### Visualization Approach
Charts were selected to maximize the visual salience of the three behavioral modes:
- **Grouped bar with log scale:** Necessary because response lengths span 63-7,026 characters (111x range) — linear scale renders Gemini bars invisible
- **Piecewise heatmap:** Three discrete color bands (0-0.3=red, 0.3-0.7=orange, 0.7-1.0=green) chosen over continuous gradient to make the Claude/Gemini binary split immediately visible
- **Horizontal bar for T2:** Emphasizes the 93.3-percentage-point spread with random-chance baseline marker
- **Radar chart:** Normalizes all metrics to 0-1.0 to enable vendor-level comparison across heterogeneous dimensions

## Computational Environment

- Python 3.9+ (dashboard generator script)
- ECharts 5.5.0 (chart rendering via CDN)
- Bootstrap 5.3.3 (layout via CDN)
- Inter font (typography via Google Fonts CDN)
- GitHub Actions (deployment pipeline)
- GitHub Pages (static hosting)

## Limitations and Decisions

1. **Gemini rubric comparability:** Gemini models' rubric scores were backfilled (computed post hoc), not generated through the same pipeline as Claude/Codex models. This methodological asymmetry may partially account for Gemini's 0.0 scores on K/R/V dimensions.

2. **CSS counter figure numbering:** The `counter-reset` approach auto-numbers figures sequentially within the tab-content div. This means figure numbers change if tabs are reordered — an acceptable trade-off for automatic consistency.

3. **Toolbox application timing:** ECharts toolbox (save-as-PNG) is applied globally via `setTimeout` after DOM initialization and again on each tab show event, to handle lazy-rendered charts that don't exist at page load.

4. **Print stylesheet scope:** The `@media print` stylesheet forces all tab panes to `display: block`, showing all 6 tabs on print. This produces a very long printed document (~20 pages) but ensures complete content capture.

5. **Citation removal decision:** Individual council member citations were removed at user request to create seamless analytical prose. The expert perspectives remain as integrated analysis; the council is referenced generically in the footer and methodology sections.
