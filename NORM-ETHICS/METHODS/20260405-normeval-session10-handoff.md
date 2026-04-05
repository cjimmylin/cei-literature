# NormEval Dashboard — Session 10 Handoff

**Date:** 2026-04-05
**Session:** Fix 4 Known Issues + Multi-Vendor Framing Update
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260404e-normeval-session9-handoff.md`

---

## What Was Done This Session

### Part A: Fix 4 Known Issues from Session 9

Resolved all four "Known Issues" listed in the Session 9 handoff:

#### 1. Playwright/Chrome Conflict on macOS
Created `DASHBOARD/test_dashboard.py` — a Playwright test runner that uses **bundled Chromium** (`p.chromium.launch()` with no `channel` argument), completely bypassing the system Chrome installation. Includes:
- Threaded HTTP server startup (Playwright requires HTTP, not `file://`)
- Per-tab screenshot capture with lazy-render wait times
- `Cache-Control: no-cache` header injection via `context.route()`
- CLI interface: `python3 test_dashboard.py` (all tabs) or `python3 test_dashboard.py 9` (single tab)
- Retina screenshots (2x device scale factor)

#### 2. CSS Caching in Playwright's Chromium
Added `?v=20260405` cache-busting query strings to all 5 local asset references in `index.html`:
- `style.css?v=20260405`
- `data.js?v=20260405`
- `data_cross_vendor.js?v=20260405`
- `charts.js?v=20260405`
- `app.js?v=20260405`

#### 3. Codex Wrapper Confound for GPT-5 Models
- Added `†` suffix to GPT-5 and GPT-5m labels across all chart data in `data_cross_vendor.js` (models list, heatmap labels, IH scaling models, CBR models, per-trial data keys)
- Added visible footnote in `index.html`: "† GPT-5 and GPT-5-mini were tested via Codex agent wrapper, not directly."

#### 4. Haiku T13 IH Single-Administration (n=1)
- Added `‡` suffix to Haiku label in the IH scaling chart data
- Modified `renderCVIHChart()` in `charts.js` to apply 50% opacity + dashed orange border to the Haiku‡ bar, visually distinguishing it from multi-administration results
- Added visible footnote in `index.html`: "‡ Haiku T13 IH score is from a single administration (n=1, no variance estimate)."

### Part B: Multi-Vendor Framing Update

Updated text across 4 tabs and `data.js` to reflect that the study now covers 9 models from 3 vendors, not just Claude:

| Tab | Changes |
|-----|---------|
| **1 (Overview)** | Intro now mentions "validated across 9 models from 3 vendors"; conclusion adds cross-vendor confirmation of 3 profiles |
| **6 (Trials)** | "Originally administered to Opus... subsequently replicated across 9 models from 3 vendors" |
| **6 Expert** | Ceiling effect heading updated to "real — and universal" with cross-vendor sentence |
| **8 (Cross-Model)** | Forward reference: "For cross-vendor extension, see Tab 10"; conclusion adds GPT-5/Gemini IH data confirming gradient is not Claude-specific |
| **8 Expert** | New "Cross-vendor validation (Tab 10)" paragraph in Safety Implications block |
| **data.js** | 4 Cross-Model findings broadened from "Claude family" → "all models/vendors" (F2, F4, F6, T9) |

### Part C: GitHub Pages Deployment

Pushed updated files to `cjimmylin/cei-normeval-dashboard` (commit `df1665b`).

**Live:** https://cjimmylin.github.io/cei-normeval-dashboard/

---

## Remaining Work

### Priority 1: Paper text revision
Update paper text (`PAPER/main-body-normeval.md`) to incorporate:
- Cross-vendor findings (F1-F7) from the council analysis
- "3 effective profiles, not 8 models" framing
- Gemini identity finding with responsible disclosure language
- † and ‡ caveats in relevant prose

### Priority 2: LaTeX conversion
NeurIPS 2026 template (8pp main + unlimited appendix). Paper text is in markdown.

### Priority 3: Temperature sensitivity test
Council recommendation #2: test Gemini at non-zero temperature to distinguish shared infrastructure from deterministic decoding.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard (live) | https://cjimmylin.github.io/cei-normeval-dashboard/ | GitHub Pages |
| Dashboard HTML | `DASHBOARD/index.html` | 10 tabs, cache-bust params, footnotes |
| Dashboard charts | `DASHBOARD/charts.js` | Haiku‡ visual treatment in IH chart |
| Cross-vendor data | `DASHBOARD/data_cross_vendor.js` | † and ‡ labels in chart data |
| Main data | `DASHBOARD/data.js` | Updated cross-model findings text |
| Test runner | `DASHBOARD/test_dashboard.py` | Playwright automated screenshots |
| Screenshots | `DASHBOARD/screenshots/` | Captured 00-overview.png, 09-crossvendor.png |
| Council analysis | `METHODS/20260404-cross-vendor-council-analysis.md` | 12-member expert deliberation |
| Previous handoff | `METHODS/20260404e-normeval-session9-handoff.md` | Session 9 (cross-vendor + annotations) |

## Known Issues

1. **T1-T5 not replicated across vendors** — original Opus trials T1-T5 (~5 items each) were not replicated cross-vendor. Low priority for paper.
2. **Codex wrapper confound (documented)** — GPT-5 values now carry † caveat but the underlying confound remains. Direct API access to GPT-5 would be needed to resolve.
3. **Haiku T13 n=1 (documented)** — single administration with no variance estimate. Now visually marked with ‡ but additional trials would strengthen the finding.

---

*Filed: 2026-04-05 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
