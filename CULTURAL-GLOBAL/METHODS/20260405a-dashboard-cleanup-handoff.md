# Cross-Cultural Benchmarks Dashboard -- Cleanup Session Handoff

**Date:** 2026-04-05
**Session:** P1/P4/P5 cleanup — console error investigation, key collision resolution, v2 promotion
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`
**Previous handoff:** `METHODS/20260405-dashboard-v2-handoff.md`

---

## What Was Done This Session

### 1. P1: Console Error Investigation — Already Fixed

Playwright-tested both v1 (`benchmarks.html`) and v2 (`benchmarks-v2.html`) dashboards across all 4 tabs (Benchmarks, Trials, Model Comparison, Council Analysis). **Zero console errors** on both versions. The error noted in the previous handoff was likely resolved during the v2 session itself (CSS contrast fixes, hard cases table cleanup in commits `a7ebea2` and `69af812`).

### 2. P4: EXSR0697 Key Collision — Resolved

Investigation confirmed the collision was already de facto resolved:

| Key | File | Status |
|-----|------|--------|
| EXSR0697 | `papers/2024-Klingefjord-Moral Graph Elicitation.md` | Active, correct |
| EXSR0695 | `papers/2025-Ali-Islamic Ethics Trusteeship.md` | Active, correct |
| EXSR0697 (was) | `RECYCLE-BIN/2025-IslamicEthics-Islamic Ethics AI Trusteeship.md` | Duplicate |

The RECYCLE-BIN file's key was updated to `EXSR0695-DUPLICATE-RECYCLED` to prevent future scan confusion. No active papers were affected.

### 3. P5: Dashboard v2 Promoted to Default — Deployed

Promoted v2 (all 22 council recommendations) to the canonical URL:

| Old Path | New Path | Content |
|----------|----------|---------|
| `benchmarks-v2.html` | **`benchmarks.html`** | v2 (council-reviewed, default) |
| `benchmark-data-v2.js` | **`benchmark-data.js`** | v2 pre-computed analytics |
| `benchmarks.html` | `benchmarks-v1.html` | v1 (archived) |
| `benchmark-data.js` | `benchmark-data-v1.js` | v1 analytics (archived) |

Script `<src>` references updated in both files before renaming. Playwright-verified both promoted default and archived v1 render with zero errors.

Commit `377e6a3` pushed to `cjimmylin.github.io/cei-cultural-global/`. Verified live via WebFetch.

---

## Remaining Work

### Priority 1: Real Gemini/GPT Trials
Replace template-derived Gemini and Codex-authored GPT data with real API responses. Scripts exist: `TRIALS/run_gemini_trials.py`. Currently all 5 Gemini models produce identical metrics (template-derived), and GPT data was authored through Codex (Tier 2 provenance).

### Priority 2: LaTeX Conversion
Both the cross-cultural paper and benchmark report need LaTeX for journal submission.

### Priority 3: Tab 2 Trial Difficulty Chart
Only shows CC3/CC4/CC5 because `COUNCIL_HARD_CASES` data is limited to those trials. A more complete version would compute variance from the full trial data.

---

## File Locations

### Files Modified This Session

| File | Location | Change |
|------|----------|--------|
| RECYCLE-BIN duplicate | `RECYCLE-BIN/2025-IslamicEthics-Islamic Ethics AI Trusteeship.md` | Key → `EXSR0695-DUPLICATE-RECYCLED` |
| Dashboard default | `DASHBOARD/benchmarks.html` | Was v2, now canonical |
| Dashboard v1 archive | `DASHBOARD/benchmarks-v1.html` | Was default, now archived |
| Data default | `DASHBOARD/benchmark-data.js` | Was v2 data, now canonical |
| Data v1 archive | `DASHBOARD/benchmark-data-v1.js` | Was default data, now archived |

### Dashboards

| Version | URL | Notes |
|---------|-----|-------|
| v2 (default) | https://cjimmylin.github.io/cei-cultural-global/benchmarks.html | Canonical URL, live |
| v1 (archive) | https://cjimmylin.github.io/cei-cultural-global/benchmarks-v1.html | Preserved for reference |
| Main dashboard | https://cjimmylin.github.io/cei-cultural-global/ | 14-tab, separate |

---

## Known Issues

1. **Gemini data identical** — all 5 Gemini models produce identical metrics (template-derived). Communicated via provenance badges.
2. **GPT data Codex-authored** — GPT-5.4/Mini responses generated through Codex, not direct OpenAI API. Marked as Tier 2.
3. **Tab 2 trial difficulty limited** — only CC3/CC4/CC5 in `COUNCIL_HARD_CASES` data.

---

*Filed: 2026-04-05 | CULTURAL-GLOBAL/METHODS/*
