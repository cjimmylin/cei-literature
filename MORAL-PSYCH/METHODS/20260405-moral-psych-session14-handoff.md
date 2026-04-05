# Moral Psychology -- Session 14 Handoff: 9-Model Dashboard Expansion (Tabs 5, 11)

**Date:** 2026-04-05
**Session:** Expand dashboard trial results from Opus-only / 3 Anthropic models to all 9 tested models across 3 vendors
**Project:** `CEI-Lit-WS/MORAL-PSYCH/` (primary), dashboard at `DASHBOARDS/moral-psych-benchmarks/`
**Previous handoff:** `MORAL-PSYCH/METHODS/20260404h-moral-psych-session13-handoff.md`

---

## What Was Done This Session

### 1. Python Generator -- `build_model_comparison()` Expanded (3 -> 9 Models)

Rewrote the `build_model_comparison()` function in `generate_dashboard.py` to use all 9 models defined in `_MODEL_ORDER` instead of hardcoded Opus/Sonnet/Haiku.

**Data contract change:** Sub-chart data moved from named keys (`opus`, `sonnet`, `haiku`) to a keyed dict (`data: {model_key: [...]}`) matching the Tab 12 `crossVendor.trialTable` pattern. Added `modelKeys` array to the output for JS iteration.

**Sub-analytics updated:**
- MFT Radar: 9-model foundation profiles from MP4 care baseline
- P-Scores: 9-model Kohlberg DIT values
- Classification Accuracy: 9-model MoralCode/M3oralBench/TracingMF
- Dual Process: 9-model TrolleyBench/DP utilitarian rates
- Trial Table: 23 x 9 matrix with nested `values` dict
- Key Findings: Rewritten for cross-vendor observations (was Anthropic-only)

**Helper added:** `_val()` extracts float from trial row with dash/None handling.

### 2. Tab 5 (Trials) -- Model Selector Dropdown

Added a `<select>` dropdown in the Trial Results card header allowing users to switch between all 9 models. Default: Opus (index 0).

**Implementation:**
- Dropdown populated dynamically from `DATA.crossVendor.models/modelKeys/modelColors`
- `renderBars()` inner function re-renders the bar chart on dropdown change
- Chart title updates dynamically: `'Primary Metric by Benchmark (' + selectedName + ')'`
- Uses `setOption(..., true)` (notMerge) for clean re-render

### 3. Tab 11 (Model Comparison) -- 4 Charts Made Data-Driven

All 4 chart functions converted from hardcoded 3-series to loop-based rendering:

- **`chartMCMFTRadar`**: Vendor-lead models (Opus, Gem Flash, Codex) get 3px solid lines; others get 1.5px dashed. Area opacity reduced to 0.05 for readability.
- **`chartMCPScore`**: 9 grouped bars, `barMaxWidth: 14` (down from 30)
- **`chartMCClassification`**: Same pattern as P-Score
- **`chartMCDualProcess`**: Same pattern as P-Score

All charts now use `legend: { type: 'scroll' }` with `pageTextStyle` for dark theme pagination.

### 4. Tab 11 Trial Table -- Dynamic 9-Column Header

- Static `<thead>` replaced with `<thead id="mc-trial-table-head">` (JS-generated)
- `renderMCTrialTable()` builds header row dynamically from `mc.models/modelColors`
- Body rows loop over `mc.modelKeys` reading from `t.values[mk]`

### 5. Tab 11 KPI Cards -- Generalized

- `renderMCKPICards()` now loops `mc.modelKeys` for mean classification accuracy and P-score range
- "Models Compared" correctly shows 9

### 6. HTML Label Updates

- Card header: "MFT Foundation Profiles: 3 Models" -> "9 Models / 3 Vendors"
- Card header: "23 Benchmarks x 3 Models" -> "23 Benchmarks x 9 Models"

---

## Verification Results

All verified with Playwright:
- Tab 5: Dropdown shows 9 models, switching Opus -> Gem 2.5P updates chart with different values
- Tab 11: All 4 charts render 9 series with scroll legends (paginated "1/2")
- Tab 11: Trial table shows 9 colored model columns with correct data
- Tab 11: KPI cards show "9 MODELS COMPARED", "60-90 P-SCORE RANGE", "96.9% MEAN CLASSIFICATION"
- Tab 12: No regression (unchanged code)
- Only console error: favicon.ico 404 (harmless)

---

## Remaining Work

### Priority 1: LaTeX Conversion
- NormEval, moral psych, religious values papers all need LaTeX formatting

### Priority 2: Tab 11 Annotation Text Update
- Annotation descriptions below the charts still reference "Opus, Sonnet, and Haiku" (from `_tab_annotations.py`)
- Should be updated to reference all 9 models / 3 vendors

### Priority 3: Human Baseline Norms (Partially Done)
- Tab 8 moral radar and Tab 5 MFQ radar have human baselines
- Still missing: population norms on classification/P-score charts

### Priority 4: GPT-4o / Llama-3 Replication
- Extend cross-model comparison beyond current 9 models

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Generator | `DASHBOARDS/moral-psych-benchmarks/generate_dashboard.py` | Data pipeline with 9-model `build_model_comparison()` |
| Charts JS | `DASHBOARDS/moral-psych-benchmarks/charts.js` | ECharts builders (Tab 5 dropdown + Tab 11 loop-based) |
| App JS | `DASHBOARDS/moral-psych-benchmarks/app.js` | Trial table + KPI rendering (dynamic columns) |
| Dashboard HTML | `DASHBOARDS/moral-psych-benchmarks/index.html` | 12-tab structure (dynamic thead) |
| Tab annotations | `DASHBOARDS/moral-psych-benchmarks/_tab_annotations.py` | Expert council annotations (needs text update) |
| Generated data | `DASHBOARDS/moral-psych-benchmarks/data.js` | 3.5MB pre-computed data |
| Dashboard repo | `cjimmylin/cei-moral-psych-dashboard` | GitHub Pages deployment |
| Screenshots | `DASHBOARDS/moral-psych-benchmarks/screenshots/` | Playwright verification captures |

## Known Issues

1. **MP9 (MFTC) data missing**: Trial table shows dashes across all models for MP9 -- no `key_metrics` extracted.
2. **MFT Radar approximation**: Foundation values approximated from MP4 care score (Sanctity = care * 0.45, etc.) since per-foundation Likert scores aren't in the cross-vendor comparison data.
3. **Tab 11 annotation text**: Still references "Opus, Sonnet, and Haiku" instead of all 9 models.
4. **Dashboard not yet pushed**: Changes are local only -- need to push to `cei-moral-psych-dashboard` repo for GitHub Pages.

---

*Filed: 2026-04-05 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
