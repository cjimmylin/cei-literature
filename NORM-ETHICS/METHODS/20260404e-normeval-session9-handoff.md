# NormEval Dashboard — Session 9 Handoff

**Date:** 2026-04-04
**Session:** Cross-Vendor Analysis + Expert Council Dashboard Annotations (All 10 Tabs)
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260404d-normeval-session8-handoff.md`

---

## What Was Done This Session

### Part A: Cross-Vendor Council Analysis Document

Assembled a 12-member interdisciplinary expert council and produced a comprehensive analysis of cross-vendor LLM ethics benchmark results.

**Council composition (12 experts):**

| # | Name | Discipline |
|---|------|-----------|
| 1 | Dr. Elena Voss | RLHF / Alignment Training |
| 2 | Dr. Marcus Chen | Moral Psychology / Dual-Process Theory |
| 3 | Dr. Priya Sharma | NLP Evaluation / Psychometrics |
| 4 | Dr. James Okafor | ML Systems / Distributed Inference |
| 5 | Dr. Hannah Fischer | Normative Ethics / Kantian |
| 6 | Dr. Wei Zhang | Consequentialist Ethics |
| 7 | Dr. Amara Osei | AI Policy / Deployment Safety |
| 8 | Dr. Tomás Rivera | Benchmark Security / Data Leakage |
| 9 | Dr. Yuki Tanaka | Cross-Cultural Moral Psychology |
| 10 | Dr. Sarah Lindström | Biostatistics / Agreement Analysis |
| 11 | Dr. David Mwangi | Educational Measurement / IRT |
| 12 | Dr. Clara Reyes | Data Visualization / Science Communication |

**Analysis output:** `METHODS/20260404-cross-vendor-council-analysis.md` (5,654 words)
- 7 findings with quantitative evidence and expert deliberation
- Council votes (ranging from 8/12 to 12/12 with named dissents)
- 10 consensus recommendations
- 3 dissenting views

### Part B: Dashboard Tab 10 — Cross-Vendor

Added new Tab 10 ("Cross-Vendor") to the NormEval dashboard with 5 ECharts visualizations and 7 expert analysis blocks.

**Data pipeline:**
1. Created `COMPARISON/generate_cross_vendor_dashboard_data.py` — reads 80 trial JSONs from 8 models across 3 vendors
2. Generated `DASHBOARD/data_cross_vendor.js` (10,259 bytes) with pre-computed data for all charts

**5 Charts:**

| Chart | Type | Data |
|-------|------|------|
| Pairwise Agreement Heatmap | 8×8 ECharts heatmap | 28 model pairs, Gemini block solid green |
| IH Scaling | Horizontal bar (sorted) | 9 models incl. Opus baseline, philosopher/lay reference lines |
| CBR Rate | Vertical bar (sorted) | 9 models, provider-colored |
| Knowledge vs Judgment | Range bar | Min-max agreement per trial, knowledge=green/judgment=red |
| Provider Radar | Radar overlay | 3 provider profiles across 6 dimensions |

**Key data patterns surfaced:**
- All 4 Gemini models = 100% identical on 114/114 items
- GPT-5 most conservative (IH=2.93, below Opus 3.0)
- Three ethical profiles: Conservative (GPT-5/Opus), Moderate (Sonnet/GPT-5m), Permissive (Haiku/Gemini)
- Sonnet↔GPT-5 = 90.4% cross-vendor agreement > Sonnet↔Haiku = 74.6% within-family

### Part C: Council Review & Dashboard Improvements (7 Fixes)

The council reviewed the dashboard and implemented 7 improvements:

1. Subtitle updated to "9-model / 3-vendor replication"
2. Vendor labels (Anthropic/Google/OpenAI) added to heatmap with provider colors
3. "Effective Profiles = 3" KPI card added
4. IH chart sorted ascending (gradient visible)
5. Opus baseline footnote added
6. CBR chart sorted ascending for consistency
7. Metric name column added to per-trial table

### Part D: Expert Council Annotations for All 10 Tabs

Added 30 expert analysis blocks across all 10 dashboard tabs. Each block has:
- Colored left border matching chart theme
- Named expert attribution with discipline
- "What to observe" / "Interpretation" / "Conclusion" structure
- Direct expert quotes and council vote tallies where applicable

| Tab | Blocks | Lead Experts |
|-----|--------|-------------|
| 1. Overview | 1 | Reyes, Sharma |
| 2. All Papers | 1 | Mwangi, Fischer |
| 3. Feature Matrix | 1 | Sharma, Voss |
| 4. Tradition Coverage | 1 | Fischer, Zhang, Tanaka |
| 5. Composite Scoring | 1 | Lindström, Mwangi |
| 6. Trials | 1 | Rivera, Chen |
| 7. Data Availability | 1 | Osei, Reyes |
| 8. Cross-Model | 2 | Voss, Chen, Osei, Fischer |
| 9. Gaps | 1 | Fischer, Zhang, Tanaka |
| 10. Cross-Vendor | 7 | All 12 members |

### Part E: GitHub Pages Deployment

Three pushes to `cjimmylin/cei-normeval-dashboard`:
1. Tab 10 + data file + cross-vendor charts (commit 8d3d34c)
2. Pages rebuild trigger (commit 15ab0fd)
3. All-tab expert annotations (commit e7d3605)

**Live:** https://cjimmylin.github.io/cei-normeval-dashboard/

---

## Remaining Work

### Priority 1: Paper text revision
Update paper text to incorporate:
- Cross-vendor findings (F1-F7) from the council analysis
- "3 effective profiles, not 8 models" framing
- Gemini identity finding with responsible disclosure language
- Update benchmark count references

### Priority 2: LaTeX conversion
NeurIPS 2026 template (8pp main + unlimited appendix). Paper text is in markdown in `PAPER/` directory.

### Priority 3: Non-Claude model replication gaps
T1-T5 were not replicated across vendors (only ~5 items each). Low priority for paper.

### Priority 4: Temperature sensitivity test
Council recommendation #2: test Gemini at non-zero temperature to distinguish shared infrastructure from deterministic decoding.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Council analysis (5,654 words) | `METHODS/20260404-cross-vendor-council-analysis.md` | 12-member expert deliberation |
| Python data generator | `COMPARISON/generate_cross_vendor_dashboard_data.py` | Reads 80 JSONs → data_cross_vendor.js |
| All-models comparison JSON | `COMPARISON/20260404-normeval-all-models-comparison.json` | Master 8-model data source |
| All-models comparison script | `COMPARISON/generate_normeval_all_models_comparison.py` | Aggregation pipeline |
| Cross-vendor data (JS) | `DASHBOARD/data_cross_vendor.js` | Pre-computed chart data |
| Dashboard (live) | https://cjimmylin.github.io/cei-normeval-dashboard/ | GitHub Pages |
| Dashboard HTML | `DASHBOARD/index.html` | 10 tabs + 30 expert blocks |
| Dashboard charts | `DASHBOARD/charts.js` | 5 new cross-vendor chart functions |
| Dashboard app | `DASHBOARD/app.js` | Updated with CV tab logic |
| Screenshots | `DASHBOARD/screenshots/cross-vendor-*.png` | Tab verification screenshots |

## Known Issues

1. **Playwright/Chrome conflict:** Chrome browser running on macOS prevents Playwright from launching automated testing. Workaround: kill Chrome before running Playwright, or verify manually in browser.
2. **Playwright CSS cache:** Playwright's Chromium caches `style.css` aggressively — may show old CSS rules on first load. Fix: inject `.echarts-box` min-height rules via `document.head.appendChild(style)` or clear browser profile.
3. **Codex wrapper confound:** GPT-5 and GPT-5-mini were tested via Codex agent, not directly. Dr. Rivera's dissent (Section 7 of council analysis) notes this may introduce additional conservatism beyond the base model.
4. **Haiku T13 IH profile:** Single-administration result (n=1, no variance estimate). Scale is 1-7 Likert, effect size d≈2.3 vs Opus.

---

*Filed: 2026-04-04 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
