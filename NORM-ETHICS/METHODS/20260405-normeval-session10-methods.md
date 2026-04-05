# Methods: NormEval Dashboard Issue Resolution and Framing Update

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The NormEval dashboard (v10) is a static HTML/JavaScript application displaying pre-computed analytics for 54 normative ethics benchmarks. Cross-vendor data encompasses 80 trial JSON files from 8 models across 3 vendors (Anthropic: Claude Opus 4.6, Sonnet 4.6, Haiku 4.5; Google: Gemini 2.5 Flash, 2.5 Flash Lite, 2.5 Pro, 3.1 Pro; OpenAI: GPT-5, GPT-5-mini). OpenAI models were accessed via Codex agent wrapper, not directly.

Dashboard technology stack: ECharts 5.5.1, Bootstrap 5.3.3, Google Fonts (Inter, JetBrains Mono). Static site hosted on GitHub Pages.

## Procedure

### Issue Resolution

Four known issues from the Session 9 handoff were addressed:

1. **Playwright browser conflict:** A Python test runner (`test_dashboard.py`) was created using Playwright's bundled Chromium binary (installed via `playwright install chromium` to `~/.cache/ms-playwright/`), which operates independently of the system Chrome installation. The script starts a threaded HTTP server on localhost, navigates to each tab with appropriate render delays (1.5s for lazy ECharts initialization), and captures full-page screenshots at 2x device scale factor.

2. **Browser cache invalidation:** Cache-busting query parameters (`?v=20260405`) were appended to all five local asset references in `index.html`. Additionally, the Playwright test runner injects `Cache-Control: no-cache` and `Pragma: no-cache` headers on all requests via Playwright's request interception API (`context.route()`).

3. **Codex wrapper documentation:** The Unicode dagger symbol (U+2020) was appended to all GPT-5 and GPT-5-mini short labels in `data_cross_vendor.js` across all chart data structures (models list, heatmap labels, IH scaling, CBR rate, per-trial keys). A corresponding footnote was added to the dashboard HTML.

4. **Single-administration caveat:** The Unicode double dagger (U+2021) was appended to the Haiku label specifically in the IH scaling chart data. The `renderCVIHChart()` function in `charts.js` was modified to detect the double-dagger character and apply visual differentiation: 50% alpha opacity (via CSS `#rrggbbaa` notation, appending `80` to the hex color) and a 2px dashed border in the dashboard's caution color (#f0983e).

### Framing Update

Prose across four dashboard tabs (Overview, Trials, Cross-Model, Cross-Vendor) and the pre-computed findings in `data.js` were updated to reflect the multi-vendor scope. The update followed a "concentric ripples" strategy: Tab 10 (Cross-Vendor) already contained the full multi-model narrative; the remaining tabs received forward references and broadened interpretations. Evidence lines (specific numerical citations) were preserved unchanged; interpretation and significance lines were updated to reference cross-vendor confirmation.

## Analysis

No new statistical analysis was performed. All changes were to presentation layer (HTML, CSS, JavaScript) and pre-computed data labels. The underlying trial data and analytics remained unchanged.

Verification was performed via:
- Node.js parsing of `data_cross_vendor.js` to confirm label consistency across all data structures
- Python HTTP server + `urllib` to verify all 9 content checks (cache-bust params, footnotes, framing text)
- Playwright automated screenshots of Tabs 0 and 9 to confirm visual rendering

## Computational Environment

- macOS Darwin 25.3.0
- Python 3.9 (`.venv`)
- Playwright (Python binding) with bundled Chromium
- Node.js v24.13.1 (for data verification)
- GitHub CLI (`gh`) for repository operations

## Limitations and Decisions

1. **Label symbols chosen for academic convention:** Dagger and double-dagger are standard academic footnote markers, chosen over asterisks (already used for Opus baseline) to maintain visual hierarchy: * = baseline, dagger = wrapper confound, double-dagger = single administration.

2. **Haiku double-dagger applied only to IH chart:** The single-administration caveat is specific to T13 (Greatest Good / OUS IH subscale). Other Haiku data points across the dashboard are not affected and retain clean labels.

3. **Cache-bust versioning is manual:** The `?v=YYYYMMDD` approach requires manual updates on each deployment. Content-hashing (e.g., webpack) would be more robust but was not justified for a manually-deployed static dashboard.

4. **Framing update scope:** Only tabs with explicit single-model language were updated. Tabs 2-5 (Feature Matrix, Tradition Coverage, Composite Scoring) and Tab 7 (Data Availability) contain benchmark-level analysis independent of model identity and required no changes.
