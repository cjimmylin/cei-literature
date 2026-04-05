# NormEval Feature Count Reconciliation -- Session 16 Handoff

**Date:** 2026-04-05
**Session:** Feature count reconciliation (41 vs 44 vs 46)
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260405e-normeval-session15-handoff.md`

---

## What Was Done This Session

### Feature Count Reconciliation

Resolved the feature count discrepancy identified as Priority 4 in the Session 15 handoff. The `DATA_FEATURE_DEFINITIONS` array in `data.js` contains exactly **41 feature objects** (26 v1 + 15 v2), verified by enumeration:

- v1 (26): A1-A8 (8), B1-B9 (9), C1-C5 (5), D1-D4 (4)
- v2 (15): A9-A13 (5), B10-B12 (3), D5-D6 (2), E1-E5 (5)

**Root cause:** Appendix I listed the original Citation Impact axis as "C1-C4" (4 features), omitting C5 (Leaderboard Presence) which is also v1. This made v1 appear as 25 features, leading to the claim that 18 new features brought the total to 44. The dashboard subtitle's "46 (26+20)" was an even older planning-phase number.

### Files Modified (16 edits across 7 files)

**Dashboard v2 (DASHBOARD-v2/):**
- `index.html` — 7 edits: subtitle (46→41, 26+20→26+15), tab explainer (46→41, 26+20→26+15), feature table heading (44→41), version legend (18→15), 3 council analysis passages (44→41, 18→15)
- `app.js` — 1 edit: KPI card (26+20→26+15)
- `data.js` — 2 edits: comment (44→41), resolution text (20→15)

**Dashboard v1 (DASHBOARD/):**
- `index.html` — 2 edits: subtitle (46→41, 26+20→26+15), tab explainer (46→41, 26+20→26+15)
- `app.js` — 1 edit: KPI card (26+20→26+15)
- `data.js` — 1 edit: resolution text (20→15)

**Paper v2 (PAPER-v2/supplement/):**
- `appendix-I-v2-features.md` — 6 edits: C1-C4→C1-C5, 18→15 (×3), 44→41 (×2), 54×18→54×15, 54×44→54×41

**Session docs (METHODS/):**
- `20260405b-normeval-session12-methods.md` — 1 edit: 46→41 features

### Files NOT Modified (correct decisions)

- **Paper abstract/methods/discussion:** References to "26 features" are correct — they describe the v1 core framework
- **"44/114 items" and "44 of 54 benchmarks":** These are trial item and benchmark counts, not feature counts
- **Historical session docs** (METHODS/ date-prefixed): Immutable per Rule 3

---

## Remaining Work

### Priority 1: LaTeX conversion
NeurIPS 2026 template or target journal format. Markdown is ready; needs typesetting.

### Priority 2: Cross-reference audit
Automated check that every `Figure N` / `Table N` / `Section N.N` in text has a corresponding file/section.

### Priority 3: Temperature sensitivity test
Gemini models at non-zero temperature to disambiguate shared infrastructure vs. deterministic decoding.

### Priority 4: Dashboard v3 redeployment
The v3 dashboard at `cjimmylin.github.io/cei-normeval-dashboard-v3/` needs to be updated with the corrected feature counts. The local `DASHBOARD-v2/` source files are fixed but the deployed version still shows the old numbers.

### Priority 5: Dashboard v1/v2 redeployment
Similarly, `cei-normeval-dashboard/` and `cei-normeval-dashboard-v2/` need updated deployments.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v2 (local) | `DASHBOARD-v2/` | Source files with corrected counts |
| Dashboard v1 (local) | `DASHBOARD/` | Source files with corrected counts |
| Appendix I | `PAPER-v2/supplement/appendix-I-v2-features.md` | v2 feature expansion appendix |
| Feature definitions | `DASHBOARD-v2/data.js` (line ~7571) | Ground truth: 41 objects |
| Previous handoff | `METHODS/20260405e-normeval-session15-handoff.md` | Session 15 |

## Known Issues

1. **Deployed dashboards stale** — All three deployed versions (v1, v2, v3) on GitHub Pages still show the old feature counts. Need `git push` to each deployment repo.
2. **Figures S1-S2 reference** — Appendix I now correctly references "54×15 heatmap" but the actual supplementary figures (if they exist as generated images) may still show the old "18 v2 features" label.

---

*Filed: 2026-04-05 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
