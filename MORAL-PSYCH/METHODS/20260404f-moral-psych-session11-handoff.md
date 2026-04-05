# Moral Psychology -- Session 11 Handoff: Cross-Vendor Council Analysis + Dashboard Annotations

**Date:** 2026-04-04
**Session:** 12-member expert council cross-vendor analysis, 3-round dashboard review, all-tab annotations, GitHub Pages deployment
**Project:** `CEI-Lit-WS/MORAL-PSYCH/` (primary), dashboard at `DASHBOARDS/moral-psych-benchmarks/`
**Previous handoff:** `MORAL-PSYCH/METHODS/20260404e-moral-psych-session10-handoff.md`

---

## What Was Done This Session

### 1. 12-Member Expert Council Assembly
Created a cross-disciplinary council to analyze cross-vendor LLM moral psychology benchmarks:
- **File:** `COUNCIL/20260404-cross-vendor-council.json`
- 12 members spanning psychometrics, moral philosophy, AI safety, cross-cultural psychology, NLP, cognitive science, religious studies, statistics, AI industry, policy, developmental psychology, philosophy of mind

### 2. Cross-Vendor Analysis (9 Models x 23 Benchmarks)
Analyzed 207 trial JSON files across 3 vendors (Anthropic: Opus/Sonnet/Haiku; Gemini: 4 models; OpenAI: Codex/Mini):
- **Analysis script:** `scripts/20260404-cross-vendor-analysis.py` (613 lines)
- **Dashboard data:** `ANALYSIS/20260404-cross-vendor-dashboard-data.json` (55 KB)
- **Council analysis:** `ANALYSIS/20260404-cross-vendor-council-analysis.md` (742 lines, ~15,400 words)
  - Part 1: Sections 0-6 (convergence, vendor signatures, scale sensitivity, discrimination, psychometric validity)
  - Part 2: Sections 7-12 (RLHF fingerprinting, theory-specific findings, implications, limitations, appendix)
- **Council review:** `ANALYSIS/20260404-cross-vendor-dashboard-review.md` (12 recommendations, 10 implemented)

### 3. Dashboard Tab 12: Cross-Vendor Analysis
Added new Tab 12 to the 12-tab dashboard with:
- 6 KPI cards (fraction format: "6/23", "17/23")
- 6 ECharts visualizations: radar, heatmap, scale sensitivity, discrimination bar, convergence scatter, theory coverage
- Expert council highlights (6 cards)
- 8-item conclusions accordion (severity-coded: Critical/Major/Moderate)
- 23x9 trial comparison table with conditional formatting

### 4. Three Rounds of Council Dashboard Review
- **Round 1 (10 fixes):** Radar overplotting, scale x-axis misalignment, convergence origin clustering, discrimination ceiling labels, diagonal reference, trial table conditional formatting, KPI fractions, theory variance tooltips, accordion CSS classes, mobile tab scrolling
- **Round 2 (3 fixes):** CRITICAL data quality -- radar min-max normalization (binary 0/100 -> absolute anchors), heatmap per-row normalization (false contrast -> deviation%), convergence scatter (linear -> log scale for MP3 outlier at 40.28)
- **Round 3 (1 fix):** Theory chart scale mixing -- Kohlberg P-score (0-100) averaged with Likert (0-5) values, normalized all to 0-100

### 5. Expert Council Annotations -- ALL 12 Tabs
Added 39 annotation entries across tabs 1-4, 6-11 (Tab 12 had 10 pre-existing). Total: 50 annotations across all 12 tabs.
- Architecture: `_tab_annotations.py` (855 lines) -> `DATA.tabAnnotations` -> `renderTabAnnotations()` (generic, 35 lines)
- Each annotation attributed to a specific council member by domain expertise
- Three types: intro blocks (title + summary), chart blocks (what/finding/interpretation/member), description blocks

### 6. GitHub Pages Deployment
- **URL:** https://cjimmylin.github.io/cei-moral-psych-dashboard/
- **Repo:** `cjimmylin/cei-moral-psych-dashboard`
- 4 commits pushed, all builds successful, verified with curl (HTTP 200)
- Visual QA: 14 screenshots, all charts render, mobile responsive at 375px, no JS errors

---

## Key Findings

1. **Cross-vendor moral homogeneity**: 6/23 benchmarks show identical scores across all 9 models. RLHF alignment training produces convergent moral profiles regardless of vendor.
2. **Within-family > between-vendor variation**: Anthropic's Haiku-Sonnet-Opus spread exceeds any cross-vendor difference.
3. **6 universal RLHF signatures**: WEIRD-liberal bias, purity floor, authority suppression, ECI ceiling, post-conventional default, deontological refusal.
4. **Haiku's unique CoT effect**: Only the smallest Anthropic model shows chain-of-thought sensitivity (0.125 vs 0.0 for all 8 others).
5. **Non-monotonic DIT P-score**: Sonnet (85) > Opus (75) > Haiku (60) -- breaks developmental prediction.

---

## Remaining Work

### Priority 1: LaTeX Conversion
- NormEval, moral psych, religious values papers all need LaTeX formatting

### Priority 2: Human Baseline References (Deferred R11)
- Add human population norms to radar charts and cross-model comparisons
- Requires curating MFQ-30 human means, DIT population P-scores from original publications

### Priority 3: 9-Model Heatmap (Deferred R7)
- Expand vendor heatmap from 3 columns to 9 columns
- Requires dashboard redesign for label space

### Priority 4: GPT-4o / Llama-3 Replication
- Extend cross-model comparison beyond Anthropic/Gemini/OpenAI Codex

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Council JSON | `COUNCIL/20260404-cross-vendor-council.json` | 12 expert personas |
| Analysis script | `scripts/20260404-cross-vendor-analysis.py` | Compute 23x9 metric matrix |
| Dashboard data | `ANALYSIS/20260404-cross-vendor-dashboard-data.json` | Intermediate analytics |
| Council analysis | `ANALYSIS/20260404-cross-vendor-council-analysis.md` | 15,400-word analysis |
| Council review | `ANALYSIS/20260404-cross-vendor-dashboard-review.md` | 12 recommendations |
| Tab annotations | `DASHBOARDS/moral-psych-benchmarks/_tab_annotations.py` | 855 lines, 39 entries |
| Generator | `DASHBOARDS/moral-psych-benchmarks/generate_dashboard.py` | Extended with cross-vendor builder + annotations |
| Dashboard repo | `cjimmylin/cei-moral-psych-dashboard` | GitHub Pages deployment |

## Known Issues

1. **Playwright browser context**: Playwright MCP server lost browser context mid-session; visual QA required launching an agent to get a fresh browser.
2. **Agent plan-mode leaks**: Two agents returned plans instead of executing; required manual implementation of their findings.
3. **MP9 (MFTC) data missing**: Trial table shows dashes across all models for MP9 -- key_metrics may not have been extracted for this benchmark.
4. **Scale sensitivity 3-grid chart**: Legend entries duplicate across grids (same benchmark name appears 3 times). Cosmetic issue.

---

*Filed: 2026-04-04 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
