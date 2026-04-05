# Moral Psychology -- Session 16 Handoff: Dashboard v2 Bug Fixes

**Date:** 2026-04-05
**Session:** Fix 4 known issues from Session 15 handoff (theme re-render, print, data transparency)
**Project:** `CEI-Lit-WS/MORAL-PSYCH/` (primary), dashboard at `DASHBOARDS/moral-psych-benchmarks-v2/`
**Previous handoff:** `MORAL-PSYCH/METHODS/20260405a-moral-psych-session15-handoff.md`

---

## What Was Done This Session

### 1. Theme Re-render Fix (Issue 3 from S15)

Added a version-counter pattern to `ThemeManager` in `app.js`:
- `_version` counter increments on each theme toggle
- `_paneVersions` map tracks which theme version each tab was last rendered at
- `initCharts()` calls `_syncThemeConstants()` when a tab's version is stale
- Result: switching to any tab after a theme toggle now correctly re-renders charts with the new theme colors — no extra tab switch required

### 2. Print Button with Two Modes (Issue 4 from S15)

Added a Print dropdown to the navbar with two modes:
- **Print Current Tab** — sets `body[data-print-mode="current"]`, adds `.print-target` class to active pane, CSS hides all other panes
- **Print All Tabs** — uses existing CSS rules (show all panes with page breaks)
- `afterprint` event listener cleans up temporary classes/attributes
- Fixed `data-print-date` attribute (was never set, now populated before `window.print()`)
- Added `@page { margin: 1.5cm; }` for consistent print margins

### 3. Gemini Cloned Data Callout (Issue 1 from S15)

Added an amber warning callout at the top of Tab 12 (Cross-Vendor Analysis):
- Explains 21/23 Gemini benchmarks reflect Opus values
- Notes only MP4 and MP9 have real Gemini data
- Includes inline "Cloned" badge matching the trial table badges
- Theme-aware styling (`.data-callout-warning`)

### 4. MFQ/MM Opus-Only Context (Issue 2 from S15)

Added a blue info callout above the MFQ-30 Radar and Moral Machine charts on Tab 5 (Benchmark Scores):
- Explains these benchmarks produce rich multi-dimensional outputs
- Notes per-model trial administration is needed to extend
- Complements existing "(Opus only)" header badges

### 5. Deployment

- Committed as `1aeeaa3` and pushed to `cjimmylin/cei-moral-psych-dashboard-v2`
- GitHub Pages build confirmed: status "built"
- Live at: https://cjimmylin.github.io/cei-moral-psych-dashboard-v2/

---

## Remaining Work

### Priority 1: Independent Gemini Trials
- Re-run 21 cloned Gemini benchmarks with actual Gemini API calls
- Would convert provenance from "cloned" to "real" and validate cross-vendor claims

### Priority 2: MFQ/MM Multi-Model Trials
- Administer MFQ-30 and Moral Machine benchmarks to all 9 models
- Would enable multi-model radar overlay and comparative scatter plots

### Priority 3: Data Splitting (P-1 from S15)
- `data.js` is 3.5MB; could split into core + detail
- Deferred: GitHub Pages serves gzip, effective transfer ~800KB

### Priority 4: LaTeX Conversion
- NormEval, moral psych, and religious values papers all need LaTeX formatting

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v2 | `DASHBOARDS/moral-psych-benchmarks-v2/` | Updated with all 4 fixes |
| app.js | `DASHBOARDS/moral-psych-benchmarks-v2/app.js` | Theme version counter + print logic |
| style.css | `DASHBOARDS/moral-psych-benchmarks-v2/style.css` | Print modes + callout styling |
| index.html | `DASHBOARDS/moral-psych-benchmarks-v2/index.html` | Print dropdown + Gemini callout |
| Bug fix spec | `METHODS/20260405-dashboard-v2-bugfix-spec.md` | Design spec for all 4 fixes |
| V2 repo | `cjimmylin/cei-moral-psych-dashboard-v2` | GitHub Pages deployment |

## Known Issues

1. **21/23 Gemini benchmarks are still cloned data** — now transparently labeled with callout + badges, but underlying data needs independent collection
2. **MFQ/MM still Opus-only** — now explained with info callout, but multi-model trials needed
3. **Theme toggle chart flicker** — active tab charts are disposed and re-created (brief flash), inherent to ECharts' lack of live theme switching

---

*Filed: 2026-04-05 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
