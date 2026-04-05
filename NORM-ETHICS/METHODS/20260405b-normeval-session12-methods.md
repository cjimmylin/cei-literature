# Methods: NormEval Dashboard v2 — Final UX Issue Resolution

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The NormEval Dashboard v2 comprises 4 source files (index.html, style.css, app.js, charts.js) plus 2 pre-computed data files (data.js at 183KB, data_cross_vendor.js at 17KB). The dashboard visualizes 54 normative ethics benchmarks scored across 46 features, with cross-model (3 Claude tiers) and cross-vendor (9 models, 3 providers) replication data.

Font assets were obtained from Google Fonts API v20: Inter (variable font, weights 300–700) and JetBrains Mono (weights 400–500), both in woff2 format with latin and latin-ext unicode subsets.

## Procedure

### Column Layout Normalization

A systematic audit of all Bootstrap grid column classes in index.html identified 5 asymmetric `col-lg-5`/`col-lg-7` splits across Tabs 1, 4, 6, 9, and 10. Each was normalized to `col-lg-6`/`col-lg-6` for visual consistency. The change was verified by grepping for residual `col-lg-[57]` patterns.

### Per-Trial Table Filters

A trial type classification map was constructed from `DATA_CROSS_VENDOR.knowledge_judgment.trials`, which classifies each of 10 replicated trials (T6–T15) as "knowledge" (4 trials), "judgment" (5 trials), or "mixed" (1 trial). A reusable `addTrialFilterBar()` function generates toggle buttons (All/Knowledge/Judgment/Mixed) above any per-trial table. The function filters table rows by matching the first cell's text content against the type map. Buttons with no matching trials are automatically omitted.

### Font Self-Hosting

The Google Fonts CSS was fetched with a modern browser user-agent to obtain woff2 URLs. Analysis revealed that Google serves Inter as a variable font (single woff2 per subset covering all requested weights), requiring only 4 files total (2 Inter + 2 JetBrains Mono). Files were downloaded via curl and local `@font-face` declarations replaced the CDN `@import`, using `font-weight: 300 700` range syntax for the variable font.

### ECharts Print Capture

The print capture system uses the `beforeprint`/`afterprint` browser events. On `beforeprint`: (1) all Bootstrap tab panes are forced visible via inline `display: block`, (2) all 9 chart-group render functions are called synchronously to initialize lazy-loaded charts, (3) all chart instances are resized to acquire layout dimensions, (4) each chart's `getDataURL({type: 'png', pixelRatio: 2, backgroundColor: '#1c1f2e'})` is called to produce a base64-encoded PNG, and (5) the PNG is injected as an `<img class="print-chart-img">` child of the chart container. CSS print rules hide canvas elements and show `.print-chart-img` instead. On `afterprint`, images are removed and tab visibility is restored.

## Analysis

Playwright automated testing verified: (1) the Knowledge filter correctly shows 4 trials (T6, T9, T11, T15), (2) the Judgment filter correctly shows 5 trials (T7, T10, T12, T13, T14), (3) all 23 ECharts instances produce valid base64 PNG data via `getDataURL()`, and (4) the `afterprint` cleanup removes all injected images.

## Computational Environment

- Browser testing: Playwright MCP (Chromium)
- HTTP serving: Python 3 `http.server` module (port 8767)
- Font source: Google Fonts API v20 (woff2 format)
- Deployment: GitHub Pages (deploy-from-branch, automatic build on push)

## Limitations and Decisions

1. **Print capture is synchronous.** The `beforeprint` event is synchronous, so all chart rendering must complete before the event handler returns. This works because ECharts `setOption()` is synchronous, but adds ~200ms to the print dialog opening.

2. **Font subsetting limited to latin/latin-ext.** Cyrillic, Greek, and Vietnamese subsets were excluded since the dashboard content is exclusively English. This reduces the font payload from ~400KB to 177KB.

3. **`:has()` CSS selector used for print fallback.** The `:not(:has(.print-chart-img))` selector used for the fallback text requires Safari 15.4+, Chrome 105+, Firefox 121+. Older browsers will show neither the chart image nor the fallback text in print mode.

4. **Mixed trial category.** Only T8 (AMAeval) is classified as "mixed" — it contains both deductive (knowledge-like) and abductive (judgment-like) subtasks. The filter button appears for completeness but filters to a single row.
