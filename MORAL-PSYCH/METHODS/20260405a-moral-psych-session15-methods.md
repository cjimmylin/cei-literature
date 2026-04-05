# Methods: Dashboard UX Evaluation and Revision

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/MORAL-PSYCH/DASHBOARDS/moral-psych-benchmarks-v2/`

## Data and Materials

The evaluation was conducted on the Moral Psychology Benchmarks Meta-Evaluation Dashboard (v1), a 12-tab static HTML dashboard presenting 292 benchmark candidates, 23 administered trials, and 9 models across 3 vendors (Anthropic, Google, OpenAI). The dashboard was built with ECharts 5.x, Bootstrap 5.3, and a Python-generated `data.js` (3.5MB) following a "fat data, thin client" architecture.

Trial data sources included per-model JSON files in `MORAL-PSYCH/TRIALS/` for Anthropic models, `TRIALS/gemini-*/` for Google models, and `Codex/TRIALS/` + `Codex-mini/TRIALS/` for OpenAI models. Cross-vendor comparison data was pre-aggregated in `20260404-cross-vendor-comparison.json`.

## Procedure

### UX Evaluation

A structured expert council review was simulated using 12 disciplinary perspectives: information architecture, data visualization, typography, interaction design, accessibility (WCAG), content strategy, academic communication, performance, visual consistency, mobile/responsive design, color/theme design, and print/export. Each perspective generated domain-specific observations following a strengths/issues/recommendations format.

Full-page screenshots of all 12 tabs were captured using Playwright browser automation (`mcp__plugin_playwright`) at 1280px viewport width. Accessibility snapshots (DOM tree analysis) supplemented visual inspection. Console errors were monitored throughout.

The evaluation produced 20 discrete issues organized into a priority matrix: 1 critical, 5 high, 8 medium, 6 low.

### Cross-Vendor Data Provenance Audit

To validate the cross-vendor comparison claims, a deep JSON comparison was performed across all 23 benchmarks for each non-Anthropic model. For each benchmark, the trial result JSON was loaded and compared field-by-field against the Opus reference, excluding only the `"model"` field.

Detection criterion: if all 4 Gemini model variants produced values identical to Opus on every field, the benchmark was classified as `"cloned"`. Otherwise it was classified as `"real"`.

Results: 21/23 benchmarks were cloned for Gemini models (only MP4 MF Vignettes and MP9 MFTC had independent data). OpenAI models showed 0/23 clones — all benchmarks had distinct trial responses.

### Dashboard Revision

A new version (v2) was created by copying the v1 source to `moral-psych-benchmarks-v2/` and implementing all 20 recommendations through 5 phases:

1. **Phase 1** (Critical): Provenance detection in `generate_dashboard.py` (comparison of Gemini vs Opus values per benchmark); scale group classification for mixed-metric charts.

2. **Phase 2** (3 parallel workstreams):
   - 2A: Python annotation quality — glossary definitions, AI disclosure, benchmark citations, duplicate title suppression
   - 2B: HTML/CSS accessibility — colorblind-safe palette (Okabe-Ito derived), non-color Feature Matrix encoding (H/M/L badges + border-pattern differentiation), tab renaming, mobile scrolling, annotation line-length constraints
   - 2C: JS interaction — URL hash deep-linking, loading splash indicator, "(Opus only)" labels

3. **Phase 3** (4 parallel tasks): Light/dark theme toggle with localStorage persistence, comprehensive print stylesheet (35 rules), CSV/JSON data export, provenance UI (badges + muted rows + KPI card)

4. **Phase 4**: Glossary tooltip rendering, AI disclosure in executive summary and footer, duplicate chart title suppression via `baseTheme(elId)` parameterization

5. **Phase 5**: Playwright verification of all 20 fixes across feature matrix, model comparison, cross-vendor, theme toggle, hash routing, and subtab chart rendering.

## Analysis

### Provenance Detection Algorithm

For each benchmark B in the 23-benchmark battery:
1. Extract the primary metric value for `anthropic_opus` as the reference value R
2. For each of the 4 Gemini model keys, extract the primary metric value G_i
3. If G_1 = G_2 = G_3 = G_4 = R, classify B as `"cloned"`; otherwise `"real"`

This simple equality test was sufficient because cloned data was a byte-level copy with only the model field changed, producing exact floating-point matches.

### Scale Group Classification

Benchmarks were classified into two scale groups based on typical value ranges:
- **Percentage** (0-100 scale): P_score, accuracy metrics, rate metrics where max > 5, ECI, decisive_count
- **Ratio** (0-5 scale): foundation scores, means, ratios, gaps, overall scores where max <= 5

Distribution: 19 ratio, 4 percentage.

### Theme-Aware Chart Rendering

The light theme toggle required converting ECharts color constants (`DARK_TEXT`, `DARK_BG`, `GRID_LINE`) from `const` to `var` declarations to enable runtime mutation. A `getThemeColors()` function reads `document.documentElement.getAttribute('data-theme')` and returns theme-appropriate values. On toggle, `ThemeManager._refreshCharts()` syncs the mutable constants and disposes/re-creates all active chart instances via the existing `TAB_CHARTS` registry.

## Computational Environment

- Python 3.9 (homebrew, `/opt/homebrew/bin/python3`)
- ECharts 5.x (CDN)
- Bootstrap 5.3.3 (CDN)
- Playwright MCP plugin for browser automation and verification
- GitHub Pages for static site deployment
- No external APIs called during this session

## Limitations and Decisions

1. **Provenance detection is binary** — benchmarks are either "cloned" (all 4 Gemini models identical to Opus) or "real". Partial cloning (some Gemini models real, others cloned) was not observed but is not tested for.

2. **Tab 5 model switching was descoped** — MFQ-30 radar and Moral Machine scatter data exists only for Opus in the current data pipeline. Rather than generating synthetic per-model data, these charts were labeled "(Opus only)".

3. **Data splitting was deferred** — GitHub Pages serves gzip compression, making the 3.5MB `data.js` ~800KB effective transfer. The complexity of a core/detail split with deferred rendering was not justified by the performance gain.

4. **Light theme chart rendering** — Charts only fully re-render with new theme colors when their tab is active. Charts on inactive tabs update when the user navigates to them. This is acceptable because ECharts instances are disposed on tab hide and re-created on tab show.

5. **Glossary tooltips use innerHTML replacement** — This is safe because `DATA.glossary` values are controlled strings from the Python generator, not user input. The regex matches whole-word boundaries and wraps only the first occurrence per term.
