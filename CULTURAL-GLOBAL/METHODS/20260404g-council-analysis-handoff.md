# Cross-Cultural Benchmarks -- Council Analysis Dashboard Session Handoff

**Date:** 2026-04-04
**Session:** 12-member expert council cross-provider analysis + dashboard Tab 4 + council critique
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`
**Previous handoff:** `METHODS/20260404c-multimodel-dashboard-handoff.md`

---

## What Was Done This Session

### 1. 12-Member Expert Council Cross-Model Analysis (Markdown)

Created `METHODS/20260404-council-cross-model-analysis.md` (~4,550 words) — a comprehensive analysis by the existing 12-member expert council (from `COUNCIL/20260404-benchmark-council.md`) repurposed for cross-provider benchmark methodology critique.

**Key contributions:**
- 3-tier provenance framework: Tier 1 (Authentic: 3 Claude models), Tier 2 (Codex-Authored: 2 GPT models), Tier 3 (Simulated: 5 Gemini models)
- Effective N analysis: nominal N=10, effective N≈5 (5 Gemini models are identical copies)
- Provider-level findings with exact metrics embedded
- 6 council recommendations (unanimous on 5, near-unanimous on R2)
- Full 12-member vote table

### 2. Dashboard Tab 4: "Council Analysis"

Added a complete 4th tab to the benchmark dashboard with:

| Element | Count | Details |
|---------|-------|---------|
| KPI cards | 4 | Effective N (≈5), Providers (3), Items (3,800), Confidence (Low-Med) |
| Charts | 5 | MFQ by Provider, Provenance Quality, Response Heatmap, RLHF Radar, Engagement Depth |
| Tables | 1 | Top 10 Highest-Variance Items ("Hard Cases") |
| Descriptions | 8 | Expert-council interpretive text for every element |
| Recommendations | 1 | 6 council recommendations panel |

**Data constants added to benchmark-data.js (9 new):**
`COUNCIL_AVAILABLE`, `COUNCIL_META`, `COUNCIL_MFQ_PROVIDER`, `COUNCIL_PROVENANCE`, `COUNCIL_TRIAL_HEATMAP`, `COUNCIL_RLHF_RADAR`, `COUNCIL_ENGAGEMENT`, `COUNCIL_HARD_CASES`, `COUNCIL_PROVIDERS`

### 3. Council Visual Critique & Fixes

The council reviewed all 4 tabs and identified 6 issues:

| Fix | Tab | Detail |
|-----|-----|--------|
| RLHF radar polygons collapsed | Council | Dynamic max from data (+20% headroom) instead of hardcoded 100 |
| Provenance chart unintuitive | Council | Inverted to quality score (3=best=long bar) with star labels |
| Hard cases table light background | Council | Explicit hex dark theme (#1c2128, #1e2530) on table and scroll-box |
| Variance not highlighted | Council | Color-coded: red (>1.0), orange (>0.5) |
| Trials tab lacked KPI cards | Trials | Added 4 KPIs (trials, items, closest country, MFQ ratio) + description |
| No cross-tab narrative | Footer | Added "Reading This Dashboard" connecting all 4 tabs |

### 4. Citation Cleanup

Removed all individual council member citations (e.g., "(Sorensen & Kontopodis)") from dashboard descriptions per user request. Expert perspectives preserved as direct statements.

### 5. GitHub Pages Deployments

3 commits pushed to `cjimmylin/cei-cultural-global`:
- `2af8d99` — Council Analysis tab
- `6d968bb` — Council critique fixes
- `3a7db19` — Remove member citations

**Live URL:** https://cjimmylin.github.io/cei-cultural-global/benchmarks.html

---

## Remaining Work

### Priority 1: EXSR0697 Key Collision
Still unresolved from Session 6a. `EXSR0697` collision between Islamic Ethics Trusteeship and Klingefjord Moral Graph.

### Priority 2: Real Gemini API Trials
Council R1 (unanimous): Replace all 5 template-derived Gemini trials with actual Gemini API responses. Script exists: `TRIALS/run_gemini_trials.py`.

### Priority 3: Direct GPT API Trials
Council R2 (11/12): Replace Codex-authored GPT-5.4 and GPT-5.4-Mini trials with direct OpenAI API calls.

### Priority 4: LaTeX Conversion
Both the cross-cultural paper and benchmark report need LaTeX for submission.

### Priority 5: Non-English Prompt Expansion
Council R3: All 10 benchmarks administered in English only.

---

## File Locations

### Files Created This Session
| File | Location | Purpose |
|------|----------|---------|
| Council analysis markdown | `METHODS/20260404-council-cross-model-analysis.md` | 4,550-word expert council analysis |
| Screenshots | `screenshots/council-*.png`, `screenshots/critique-*.png`, `screenshots/final-*.png` | Dashboard verification |

### Files Modified This Session
| File | Change |
|------|--------|
| `SCRIPTS/generate_benchmark_tab.py` | Added comparison data loading, 9 COUNCIL_* constants, Tab 4 HTML + JS, Trials KPIs, cross-tab footer, visual fixes, citation removal |
| `DASHBOARD/benchmarks.html` | Regenerated (68.7KB → 99.5KB) |
| `DASHBOARD/benchmark-data.js` | Regenerated (50.5KB → 62.5KB) |

### Dashboard
- **Live:** https://cjimmylin.github.io/cei-cultural-global/benchmarks.html
- **Local:** `DASHBOARD/benchmarks.html`
- **Generator:** `SCRIPTS/generate_benchmark_tab.py`
- **Data:** `DASHBOARD/benchmark-data.js`

---

## Known Issues

1. **Playwright browser instability** — Chrome browser repeatedly lost connection during verification. Singleton lock files caused "Browser is already in use" errors. Workaround: `rm -rf /Users/jimmy.lin/Library/Caches/ms-playwright/mcp-chrome-*/` between sessions.
2. **Hard cases table background** — Despite explicit hex dark colors in CSS, the table body may still render slightly lighter than surrounding cards in some browsers. CSS specificity or Bootstrap overrides may be the cause.
3. **Gemini data is simulated** — All 5 Gemini models in the comparison produce identical metrics. Dashboard provenance chart and descriptions communicate this, but the underlying data remains template-derived.

---

*Filed: 2026-04-04 | CULTURAL-GLOBAL/METHODS/*
