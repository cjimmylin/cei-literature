# Moral Psychology Benchmarks — Session 21 Handoff

**Date:** 2026-04-05
**Session:** 21 — Dashboard v4 Bug Fixes + Narrative Annotations
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`
**Previous handoff:** `METHODS/20260405j-moral-psych-session20-dashboard-bugfix-handoff.md`

---

## What Was Done This Session

### Playwright Visual QA — Full 10-Tab Audit

Systematically examined all 10 dashboard tabs plus 3 Explorer sub-tabs using Playwright. Took full-page screenshots and checked browser console for JS errors. Only error: harmless favicon 404.

### Bug Fixes (6 total, 4 commits to main)

1. **`[object Object]` model cards** (Methodology tab) — `app.js:1102`: Data uses `display` property but renderer accessed `m.name`, falling back to `m` (the whole object). Fix: `m.display || m.name || m`.

2. **Empty Triple Bind Summary heatmap** (Discussion tab) — `charts.js:1068`: ECharts heatmap silently requires numeric values in the third data element. Data had text strings `[ci, ri, "MFT 73%\nquality rate"]`. Fix: changed to `[ci, ri, ri]` (numeric row index for visualMap coloring), text pulled via formatter from `cellData` array. Also changed `dimension: 1` → `dimension: 2`, added `inverse: true` on yAxis, adjusted grid margins.

3. **Empty Discussion Recommendations section** — `app.js:873-919`: HTML had `discussion-recs-container` but no JS function populated it. Added `renderDiscussionRecs()` function and call in init.

4. **HTML ID mismatch** — `index.html:593`: Container `rf-ann-discriminatingInstruments` didn't match data key `discriminating`. Fixed to `rf-ann-discriminating`.

5. **Blank Explorer sub-tab charts** (Scree Plot, Feature Importance, UMAP, Treemap, Health Scorecard) — `app.js:2058-2070`: All 5 Explorer charts initialized when parent tab shows, but only the active sub-tab (Feature Structure) is visible. Charts in hidden Bootstrap pill sub-tabs render into zero-size canvases. Fix: added resize handler in `shown.bs.tab` event that finds all ECharts instances within the newly-visible sub-tab pane via `[_echarts_instance_]` selector and calls `.resize()`.

6. **Ranking tier/theory filters returning 0 results** — `app.js:1295`: Theory filter missing `!== 'all'` exclusion. When `theoryVal="all"`, the filter tried to find literal "all" in `r.theories`, rejecting every row. Fix: added `theoryVal !== 'all'` check matching the tier filter pattern.

### Narrative Annotations (12 new, ~12KB added)

Filled all 12 previously empty annotation containers across 7 tabs:

| Tab | Key | Type | Content |
|-----|-----|------|---------|
| Methodology | `featureWeights` | Chart | PD/PE/CI weight rationale, expert ranking validation (ρ=0.91) |
| Claims 1-3 | `theoryAbsence` | Chart | Process-level benchmark gap |
| Claims 1-3 | `theoryHeatmap` | Chart | Theory×tier count matrix analysis |
| Claims 1-3 | `validityTheory` | Chart | Validity by theory, psychometric lineage |
| Claims 4-6 | `culturalBreakdown` | Chart | Cultural coverage by vendor |
| Discussion | `bindSummary` | Chart | Heatmap grid explanation |
| Discussion | `themes` | Card | 7 themes narrative arc |
| Discussion | `recommendations` | Card | Priority structure rationale |
| Ranking | `table` | Card | Usage guide by tier |
| Features | `table` | Card | Heatmap color coding guide |
| Explorer | `featImportance` | Chart | Feature contribution analysis |
| RLHF | `discriminating` | — | ID mismatch fix enabled existing data |

Updated `_tab_annotations.py` (source of truth) and regenerated `tabAnnotations` section in `data.js` (62KB → 74KB).

---

## Remaining Work

### Priority 1: GitHub Pages Deployment Verification
Hard-refresh the live site and verify all fixes render correctly. The 4 commits have been pushed to main.

### Priority 2: Combined Manuscript PDF
`PAPER-v4/scripts/build_combined_pdf.py` not yet written — need to combine all 9 section markdowns + 4 supplementary into a single PDF.

### Priority 3: Hash-Based Navigation QA
Some charts may not initialize when navigating directly via URL hash (e.g., `#tab=pane-discussion`). The Bootstrap tab show event may not fire for the initial hash-routed tab on page load. Needs testing.

### Priority 4: `data.js` aiDisclosure Cleanup
`data.js` still contains "expert panel" text in the `aiDisclosure` field. Fixed in `app.js` fallback but source data unchanged.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v4 | `DASHBOARDS/moral-psych-benchmarks-v4/` | All dashboard files |
| Dashboard live | `cjimmylin.github.io/cei-moral-psych-dashboard-v4/` | GitHub Pages |
| Dashboard repo | `github.com/cjimmylin/cei-moral-psych-dashboard-v4` | Deployment repo |
| Annotations source | `DASHBOARDS/moral-psych-benchmarks-v4/_tab_annotations.py` | Python dict → data.js |
| Previous handoff | `METHODS/20260405j-moral-psych-session20-dashboard-bugfix-handoff.md` | Prior session |

## Known Issues

1. **Hash navigation may skip chart init** — charts on the initially-hashed tab may not render if the `shown.bs.tab` event doesn't fire for the default tab on page load.
2. **`data.js` aiDisclosure** still says "expert panel" — patched in app.js fallback but data source unchanged.
3. **Hidden Gems titles** may still wrap awkwardly despite 50-char truncation.
4. **N=1 per model per benchmark** — all cross-vendor differences are point estimate comparisons without inferential statistics.

---

*Filed: 2026-04-05 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
