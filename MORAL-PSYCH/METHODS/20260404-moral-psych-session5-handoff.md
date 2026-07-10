# Session 5 Handoff: Moral Psychology Benchmarks Meta-Evaluation

**Date:** 2026-04-04
**Session scope:** Data fixes, ingestion, dashboard deployment, and actual Claude trials
**Status:** 6 benchmark trials complete. Dashboard live on GitHub Pages. 14 papers ingested. Top-15 corrected.

---

## What Was Accomplished (This Session)

### 1. Top-15 Data Fixes (Phase A)
- **TrolleyBench de-duplicated:** Added data_url-based dedup logic to `build_expanded_matrix.py` (line ~361). Duplicate `2025-Zhu-TrolleyBench.md` removed (kept higher-composite entry). Vault paper marked with `duplicate_of` field.
- **Kohlberg DIT re-added:** Added `MANUAL_DATA_OVERRIDES` dict to `build_expanded_matrix.py` for published instruments without GitHub repos. `2024-Khandelwal-Multilingual Defining Issues Test.md` now at **rank 9** (composite 61.23, PD=80).
- Revised top-15 has: trolley(3), mft(4), schwartz(3), kohlberg(4), dyadic(1) — good theory diversity.

### 2. Paper Ingestion (Phase B)
- **14 papers ingested:** EXSR0676–EXSR0689 from `20260403-external-search-merged.json`
- Script: `MORAL-PSYCH/scripts/ingest_moral_psych_discoveries.py`
- Report: `MORAL-PSYCH/20260404-phase2a-ingestion-report.json`
- 5 papers have "Unknown" authors (papers 4, 11, 12, 13, 14) — flagged for manual enrichment
- All 2,329 papers validated (0 errors)

### 3. Dashboard Updates (Phase C–D)
- **data.js regenerated** — 55KB, updated KPI (221 candidates), Kohlberg DIT present, no TrolleyBench duplicate
- **Playwright verified** — all 6 tabs pass, no JS errors (only favicon 404)
- **6 figures generated** to `PAPER/figures/`:
  - fig1-composite-scores.png (119KB) — from dashboard Overview
  - fig2-theory-distribution.png (43KB) — from dashboard Overview
  - fig3-theory-heatmap.png (139KB) — from dashboard Theory Heatmap
  - fig4-implementation-grid.png (169KB) — from dashboard Implementation
  - fig5-construct-validity.png (43KB) — standalone ECharts (A6 distribution)
  - fig6-human-baselines.png (53KB) — standalone ECharts (A5 distribution)
- **Figure references added** to `PAPER/results-mpbench.md`

### 4. GitHub Pages Deployment (Phase E)
- **Repo:** `cjimmylin/cei-moral-psych-dashboard` (public)
- **URL:** https://cjimmylin.github.io/cei-moral-psych-dashboard/
- Playwright-verified on deployed URL — all tabs load, charts render

### 5. Actual Claude Trials (6 benchmarks, ~260 items)
Self-administered by Claude Opus 4.6 via Claude Code chat interface.

| Trial | Benchmark | Theory | Items | Key Result |
|-------|-----------|--------|-------|------------|
| MP2 | MFQ-30 | MFT | 30 | Ind/Bind=2.84 (above US liberals) |
| MP3 | DIT (Kohlberg) | Kohlberg CMD | 60 | P-score=75% (adults 40%, GPT-4 65%) |
| MP4 | MFV Vignettes | MFT | 30 | Ind/Bind=3.1x (converges with MFQ-30) |
| MP5 | ValueCompass | Schwartz | 40 | Transcendence=4.75/5, Power=0 |
| MP6 | EMNLP Teacher | Kohlberg (educator) | 40 | P-score=90%, stage 5.25 |
| MP7 | TrolleyBench | Trolley/Consistency | 60 | ECI=1.00 (perfect consistency) |

**Cross-trial mega-finding:** RLHF creates a distinctive moral response profile — extreme self-transcendence (Care/Fairness/Universalism at ceiling), suppressed binding (Power/Authority/Purity near floor), post-conventional reasoning dominant (75–90% P-score), perfect ethical consistency (ECI=1.0 via strict Doctrine of Double Effect).

**Trial files:** All in `MORAL-PSYCH/TRIALS/`:
- 6 trial JSONs: `20260404-trial-MP{2-7}-*-opus.json`
- Summary: `20260404-trials-summary.json`
- Scoring scripts: `score_mfq30.py`, `score_all_trials.py`

---

## New Files (Session 5)

```
MORAL-PSYCH/
├── scripts/
│   └── ingest_moral_psych_discoveries.py       (NEW — 14-paper ingestion)
├── 20260404-phase2a-ingestion-report.json       (NEW — ingestion report)
├── TRIALS/                                       (NEW directory)
│   ├── 20260404-trial-MP2-mfq30-opus.json       (NEW — MFQ-30 trial)
│   ├── 20260404-trial-MP3-dit-opus.json          (NEW — DIT trial)
│   ├── 20260404-trial-MP4-mfv-opus.json          (NEW — MFV vignettes trial)
│   ├── 20260404-trial-MP5-valuecompass-opus.json  (NEW — ValueCompass trial)
│   ├── 20260404-trial-MP6-emnlp-teacher-opus.json (NEW — EMNLP teacher trial)
│   ├── 20260404-trial-MP7-trolleybench-opus.json  (NEW — TrolleyBench trial)
│   ├── 20260404-trials-summary.json              (NEW — cross-trial summary)
│   ├── score_mfq30.py                            (NEW — MFQ-30 scorer)
│   └── score_all_trials.py                       (NEW — unified scorer)
├── PAPER/
│   ├── figures/
│   │   ├── fig1-composite-scores.png             (NEW)
│   │   ├── fig2-theory-distribution.png          (NEW)
│   │   ├── fig3-theory-heatmap.png               (NEW)
│   │   ├── fig4-implementation-grid.png          (NEW)
│   │   ├── fig5-construct-validity.png           (NEW)
│   │   ├── fig5-construct-validity.html          (NEW — standalone ECharts source)
│   │   ├── fig6-human-baselines.png              (NEW)
│   │   └── fig6-human-baselines.html             (NEW — standalone ECharts source)
│   └── results-mpbench.md                        (MODIFIED — figure refs added)
├── DASHBOARDS/moral-psych-benchmarks/
│   ├── data.js                                   (REGENERATED — corrected top-15)
│   └── generate_dashboard.py                     (UNCHANGED)
└── build_expanded_matrix.py                      (MODIFIED — dedup + Kohlberg override)

papers/
├── 2025-Zhu-TrolleyBench.md                      (MODIFIED — duplicate_of field added)
└── 14 new papers (EXSR0676–EXSR0689)             (NEW)
```

---

## Modified Files (Key Changes)

| File | Change |
|------|--------|
| `build_expanded_matrix.py` | +25 lines: data_url dedup logic + MANUAL_DATA_OVERRIDES dict |
| `papers/2025-Zhu-TrolleyBench.md` | Added `duplicate_of` YAML field |
| `PAPER/results-mpbench.md` | Added 6 figure references (Figures 1–6) |
| `DASHBOARDS/.../data.js` | Regenerated with corrected top-15 |

---

## User Decisions (Binding for Future Sessions)

All Session 3–4 decisions remain in effect, plus:
1. **Self-administration is valid:** Claude Opus can administer benchmarks to itself via chat interface; results are representative model behavior (document system-prompt-active condition)
2. **Subset strategy for large benchmarks:** Use 20–30 representative items rather than full instrument when >100 items
3. **MANUAL_DATA_OVERRIDES pattern:** Published psychometric instruments (DIT, MFQ, PVQ) can be marked data_available=True without a GitHub repo, with documented override_reason

---

## What Remains

### Quick (< 1 hour)
1. **Update dashboard Trials tab** — Modify `generate_dashboard.py` to read `TRIALS/20260404-trials-summary.json` and populate the currently-placeholder Trials tab with actual trial results
2. **Re-deploy to GitHub Pages** — Copy updated data.js to `cjimmylin/cei-moral-psych-dashboard` after Trials tab update
3. **Enrich 5 "Unknown" author papers** — Papers EXSR0679, 0686, 0687, 0688, 0689 need author lookup from PDFs

### Medium (1–3 hours)
4. **BibTeX generation** — Compile full .bib file from all cited papers (~177 refs across all sections)
5. **LaTeX conversion** — Convert all markdown sections to ACL/EMNLP 2026 template. This also handles section numbering, cross-references, and combined single PDF.

### Manual (institutional access needed)
6. **Download 31 paywalled papers** — Hard paywalls (APA, SAGE, Wiley, Science, books). Institutional access required.
7. **Ingest 14 new external finds** — Some of the 14 ingested papers need PDF downloads (arXiv/ACL open-access ones can be automated)

### Future Enhancements
8. **Multi-model replication** — Re-run trials on GPT-4o, Llama-3, Gemini for cross-model comparison
9. **Bare API replication** — Re-run trials without system prompt to control for context effects
10. **Theory pie chart cosmetic fix** — data.js shows "222 Candidates" in pie title but KPI says 221

---

## Critical Dependencies

All Session 4 dependencies remain, plus:
1. **Trial data:** `TRIALS/20260404-trials-summary.json` — master file for dashboard integration
2. **Scoring scripts:** `TRIALS/score_all_trials.py` — unified scorer for all 6 trials
3. **Ingestion script:** `MORAL-PSYCH/scripts/ingest_moral_psych_discoveries.py` — reusable for future batches
4. **GitHub Pages repo:** `cjimmylin/cei-moral-psych-dashboard` — push updated files to redeploy
