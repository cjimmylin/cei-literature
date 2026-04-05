# NormEval Dashboard — Session 12 Handoff

**Date:** 2026-04-05
**Session:** Resolve 3 remaining council issues + deploy
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260405a-normeval-session11-handoff.md`

---

## What Was Done This Session

### Issue 1.2: Column Layout Consistency

Normalized all 5 remaining asymmetric `col-lg-5`/`col-lg-7` splits to `col-lg-6`/`col-lg-6` across:
- Tab 1: Gate donut + Five Claims
- Tab 4: Tradition heatmap + bar/entropy
- Tab 6: Trial accuracy + difficulty/summary
- Tab 9: Care prototype + Tronto dimensions
- Tab 10: Radar + Seven Findings

Zero asymmetric columns remain (verified with `grep -n 'col-lg-[57]'`).

### Issue 4.2: Per-Trial Table Filters

Added Knowledge/Judgment/Mixed/All toggle filter buttons to both per-trial tables:
- Cross-Model (Tab 8): `cm-per-trial-table` — filters 9 trials by type
- Cross-Vendor (Tab 10): `cv-per-trial-table` — filters 10 trials by type

Type mapping derived from `DATA_CROSS_VENDOR.knowledge_judgment.trials`:
- Knowledge: T6 (PrinciplismQA), T9 (JETHICS), T11 (MedEthicsQA), T15 (ProMoralBench)
- Judgment: T7 (Persuasion), T10 (Pluralistic Gap), T12 (UniMoral), T13 (Greatest Good), T14 (PNAS Biases)
- Mixed: T8 (AMAeval)

Buttons hidden in print mode via CSS.

### Issue 6.5: Google Fonts Self-Hosting

Replaced `@import url('https://fonts.googleapis.com/...')` with 4 local `@font-face` declarations:
- `fonts/inter-latin.woff2` (48KB) — Inter variable font, weights 300–700, latin
- `fonts/inter-latin-ext.woff2` (85KB) — Inter variable font, weights 300–700, latin-ext
- `fonts/jetbrains-mono-latin.woff2` (31KB) — JetBrains Mono, weights 400–500, latin
- `fonts/jetbrains-mono-latin-ext.woff2` (12KB) — JetBrains Mono, weights 400–500, latin-ext

Total: 177KB of self-hosted fonts. Zero external requests to Google CDN.

### ECharts Print Capture

Replaced the `[Interactive chart — view online]` placeholder text with actual static PNG images:
- `beforeprint` handler: forces all 10 tab panes visible, synchronously calls all 9 `render*Charts()` functions, resizes all chart instances, captures each via `getDataURL({pixelRatio: 2})`, injects `<img class="print-chart-img">`
- `afterprint` handler: removes all print images, restores tab pane visibility
- CSS: hides canvas children in print, shows `.print-chart-img`, fallback text for charts that fail to capture
- Verified: all 23 charts captured successfully from any starting tab

### Deployment

Pushed commit `28fbea5` to `cjimmylin/cei-normeval-dashboard-v2` on GitHub. Pages build triggered and deploying.

---

## Remaining Work

### Priority 1: Paper text revision
Update paper text to incorporate cross-vendor findings, "3 effective profiles" framing, Gemini identity disclosure. Reference dashboard v2.

### Priority 2: LaTeX conversion
NeurIPS 2026 template (8pp main + unlimited appendix).

### Priority 3: Temperature sensitivity test
Test Gemini at non-zero temperature to disambiguate shared infrastructure vs deterministic decoding.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v2 (source) | `NORM-ETHICS/DASHBOARD-v2/` | Source files with all fixes |
| Dashboard v2 (live) | https://cjimmylin.github.io/cei-normeval-dashboard-v2/ | GitHub Pages deployment |
| Self-hosted fonts | `NORM-ETHICS/DASHBOARD-v2/fonts/` | 4 woff2 files (177KB total) |
| Dashboard v1 (frozen) | `NORM-ETHICS/DASHBOARD/` | Original 10-tab version |
| Council review | `METHODS/20260405-dashboard-ux-council-review.md` | 28 issues, all resolved |
| S11 handoff | `METHODS/20260405a-normeval-session11-handoff.md` | Previous session |

## Known Issues

None. All 28 council recommendations are now implemented. The 3 remaining items from S11 (paper revision, LaTeX, temperature test) are content work, not dashboard issues.

---

*Filed: 2026-04-05 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
