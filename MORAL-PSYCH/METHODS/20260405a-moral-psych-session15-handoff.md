# Moral Psychology -- Session 15 Handoff: Dashboard v2 UX Overhaul

**Date:** 2026-04-05
**Session:** Implement all 20 UX review recommendations into a new dashboard version
**Project:** `CEI-Lit-WS/MORAL-PSYCH/` (primary), dashboard at `DASHBOARDS/moral-psych-benchmarks-v2/`
**Previous handoff:** `MORAL-PSYCH/METHODS/20260405-moral-psych-session14-handoff.md`

---

## What Was Done This Session

### 1. Expert Council UX Review (12 Perspectives)

Assembled a 12-perspective expert council to critique the v1 dashboard:
1. Information architecture
2. Data visualization
3. Typography & readability
4. Interaction design
5. Accessibility (WCAG)
6. Content strategy
7. Academic communication
8. Dashboard performance
9. Visual consistency
10. Mobile & responsive design
11. Color & dark theme design
12. Print & export

Produced `20260405-dashboard-ux-review.md` with 20 issues organized into a priority matrix (1 critical, 5 high, 8 medium, 6 low).

### 2. Cross-Vendor Data Investigation

Deep investigation of trial data authenticity revealed:
- **Gemini models**: 21/23 benchmarks are CLONES of Opus data (only MP4 MF Vignettes and MP9 MFTC have real data)
- **OpenAI models**: 23/23 benchmarks have genuinely independent trial data
- Root cause: incomplete trial execution for Gemini, with Opus values used as placeholders

### 3. Dashboard v2 Implementation (All 20 Recommendations)

Created new directory `moral-psych-benchmarks-v2/` and implemented:

**Critical:**
- R-2: Provenance detection — compares Gemini values against Opus, flags clones, adds badges + muted styling + KPI card showing "2/23 REAL DATA"
- V-1: Scale group classification — `scaleGroup` field on all trial data ("ratio" vs "percentage")

**Accessibility:**
- A-1: Non-color encoding in Feature Matrix (H/M/L superscript badges + solid/dashed/dotted borders)
- D-1: Colorblind-safe palette (blue/amber/gray-red replacing green/amber/red)
- I-2: Tab rename (Trials -> Benchmark Scores, Trial Results -> Detailed Analysis)
- M-1: Mobile horizontal tab scrolling at <=992px
- T-5: Annotation line length max-width: 80ch

**Content:**
- C-1: Glossary tooltips (10 terms: WEIRD, RLHF, ECI, MFT, DIT, CoT, MFQ, WLBI, P-score, Ind/Bind)
- C-3: AI disclosure in executive summary + footer
- S-2: Suppress duplicate ECharts internal titles (16 charts)
- R-5: 221 benchmark citations from candidates JSON

**Interaction:**
- X-2: "(Opus only)" labels on MFQ radar + Moral Machine scatter (data only exists for Opus)
- X-5: URL hash deep-linking (#tab=pane-name)
- P-3: Loading splash with animated progress bar

**Enhancement:**
- D-3: Light/dark theme toggle with localStorage persistence + chart re-render
- E-1: Comprehensive print stylesheet (35 rules)
- E-2: CSV/JSON data export (3 options: Feature Matrix, Trials, Full Data)

### 4. V1 Fixes (Pre-v2)

Also fixed in v1 dashboard:
- Tab 11 annotation text updated from Anthropic-only to 9 models / 3 vendors
- All simulated expert names removed -> discipline perspective labels
- Tab 9 subtab chart rendering fix (pass pane ID directly instead of querying DOM)
- 2 remaining inline "Dr." references fixed

### 5. Deployment

- V2 deployed to `cjimmylin/cei-moral-psych-dashboard-v2` (GitHub Pages, status: built)
- V1 remains at `cjimmylin/cei-moral-psych-dashboard` (untouched)

---

## Remaining Work

### Priority 1: Data Splitting (P-1)
- `data.js` is 3.5MB. Could split into `data-core.js` (<1MB) + `data-detail.js` (~2.5MB)
- Deferred: GitHub Pages serves gzip, effective transfer ~800KB

### Priority 2: Independent Gemini Trials
- Re-run the 21 cloned Gemini benchmarks with actual Gemini API calls
- Would convert provenance from "cloned" to "real" and validate cross-vendor claims

### Priority 3: LaTeX Conversion
- NormEval, moral psych, and religious values papers all need LaTeX formatting

### Priority 4: GPT-4o / Llama-3 Replication
- Extend cross-model comparison beyond current 9 models

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v2 | `DASHBOARDS/moral-psych-benchmarks-v2/` | New version with all 20 fixes |
| Dashboard v1 | `DASHBOARDS/moral-psych-benchmarks/` | Original, untouched |
| UX Review | `DASHBOARDS/moral-psych-benchmarks/20260405-dashboard-ux-review.md` | 12-perspective critique |
| Generator | `DASHBOARDS/moral-psych-benchmarks-v2/generate_dashboard.py` | Updated with provenance + glossary + citations |
| Annotations | `DASHBOARDS/moral-psych-benchmarks-v2/_tab_annotations.py` | Updated text density |
| V2 data.js | `DASHBOARDS/moral-psych-benchmarks-v2/data.js` | 3.57MB with new fields |
| V2 repo | `cjimmylin/cei-moral-psych-dashboard-v2` | GitHub Pages deployment |
| V1 repo | `cjimmylin/cei-moral-psych-dashboard` | Original deployment |

## Known Issues

1. **21/23 Gemini benchmarks are cloned data** — provenance badges label this transparently but the underlying data needs independent collection
2. **Tab 5 MFQ radar and Moral Machine scatter are Opus-only** — labeled "(Opus only)" since per-model data doesn't exist
3. **Theme toggle requires tab switch for full chart re-render** — ThemeManager disposes + re-creates active tab charts, but charts on other tabs only update when navigated to
4. **Print stylesheet shows all tabs sequentially** — may produce 30+ page printout; no selective tab printing

---

*Filed: 2026-04-05 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
