# NormEval Dashboard Deployment — Session 17 Handoff

**Date:** 2026-04-05
**Session:** Deploy corrected feature counts to all three GitHub Pages dashboards
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260405f-normeval-session16-handoff.md`

---

## What Was Done This Session

### Issue 1: GitHub Pages Dashboard Redeployment

All three NormEval dashboards on GitHub Pages were updated with corrected feature counts (41 features = 26 v1 + 15 v2, replacing stale 46/44/18/20 numbers).

**v1 (`cjimmylin.github.io/cei-normeval-dashboard/`):**
- Cloned repo to `/tmp/cei-normeval-dashboard/`
- Copied corrected files from local `DASHBOARD/` source (3 files: `index.html`, `app.js`, `data.js`)
- 4 line changes: subtitle, tab explainer, KPI card, data.js resolution text
- Committed (`8f19539`) and pushed to `main`

**v2 (`cjimmylin.github.io/cei-normeval-dashboard-v2/`):**
- Cloned repo to `/tmp/cei-normeval-dashboard-v2/`
- Copied corrected files from local `DASHBOARD-v2/` source (4 files: `index.html`, `app.js`, `data.js`, `style.css`)
- 774 lines changed — includes count fixes PLUS all Session 13–16 improvements (Tab 11 feature reference table, additional council analysis)
- The deployed repo had been at Session 12 (`28fbea5`), 3 sessions behind
- Committed (`91e0a7f`) and pushed to `main`

**v3 (`cjimmylin.github.io/cei-normeval-dashboard-v3/`):**
- Cloned repo to `/tmp/cei-normeval-dashboard-v3/`
- v3 content is identical to v2 except for a `fonts/` directory (self-hosted WCAG fonts)
- Copied corrected v2 source files over (3 files: `index.html`, `app.js`, `data.js`)
- 10 line changes across 7 locations: subtitle, tab explainer, feature reference heading (44→41), version legend (18→15), 3 council analysis passages, KPI card, data.js comment
- Committed (`4b119d6`) and pushed to `main`

All three GitHub Pages builds confirmed `in_progress` after push.

### Issue 2: Supplementary Figures S1–S2

Inspected both supplementary figures visually:
- **Figure S1** (`PAPER-v2/figures/figS1-pca-clusters.png`): PCA scatter plot with PC1/PC2 axes — no feature count labels. Clean.
- **Figure S2** (`PAPER-v2/figures/figS2-temporal-trends.png`): Three-panel temporal trend plot (ND, PE, CI over time) — no feature count labels. Clean.

**No action needed.** The handoff's concern about "18 v2 features" labels in image files was unfounded.

---

## Remaining Work

### Priority 1: LaTeX conversion
NeurIPS 2026 template or target journal format. Markdown is ready; needs typesetting.

### Priority 2: Cross-reference audit
Automated check that every `Figure N` / `Table N` / `Section N.N` in text has a corresponding file/section.

### Priority 3: Temperature sensitivity test
Gemini models at non-zero temperature to disambiguate shared infrastructure vs. deterministic decoding.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v1 (deployed) | `cjimmylin.github.io/cei-normeval-dashboard/` | GitHub Pages, commit `8f19539` |
| Dashboard v2 (deployed) | `cjimmylin.github.io/cei-normeval-dashboard-v2/` | GitHub Pages, commit `91e0a7f` |
| Dashboard v3 (deployed) | `cjimmylin.github.io/cei-normeval-dashboard-v3/` | GitHub Pages, commit `4b119d6` |
| Dashboard v1 (local source) | `DASHBOARD/` | Corrected in Session 16 |
| Dashboard v2 (local source) | `DASHBOARD-v2/` | Corrected in Session 16 |
| Figure S1 | `PAPER-v2/figures/figS1-pca-clusters.png` | PCA benchmark clustering |
| Figure S2 | `PAPER-v2/figures/figS2-temporal-trends.png` | Temporal trends (ND/PE/CI) |
| Previous handoff | `METHODS/20260405f-normeval-session16-handoff.md` | Session 16 |

## Known Issues

None identified. All three dashboards deployed with correct counts; supplementary figures confirmed clean.

---

*Filed: 2026-04-05 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
