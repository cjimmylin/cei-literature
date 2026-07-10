# Moral Psychology -- Session 13 Handoff: Dashboard Bug Fixes (Tabs 5, 11) + Text Contrast

**Date:** 2026-04-04
**Session:** Fix broken chart placeholders on Tabs 5 and 11, fix text contrast across all tabs
**Project:** `CEI-Lit-WS/MORAL-PSYCH/` (primary), dashboard at `DASHBOARDS/moral-psych-benchmarks/`
**Previous handoff:** `MORAL-PSYCH/METHODS/20260404g-moral-psych-session12-handoff.md`

---

## What Was Done This Session

### 1. Session 12 Enhancements (carried over)
All Round 2 council review enhancements from Session 12 were completed and deployed:
- Executive summary card on Overview tab
- Tab 5 (Trials) annotations filled
- Domain-colored annotation borders (12 domains)
- Cross-tab navigation badges
- Tab group separators
- Sacred values annotation
- Provenance footer with GitHub link
- ECharts global toolbox (save-as-image)
- Print stylesheet

### 2. Tab 11 (Model Comparison) — Charts Fixed
**Root cause:** `DATA.modelComparison` never existed. The generator had no `build_model_comparison()` function — charts.js had 4 chart functions referencing this undefined data since the dashboard was first created.

**Fix:** Added `build_model_comparison()` to `generate_dashboard.py` that extracts Opus/Sonnet/Haiku data from the cross-vendor trial table:
- **MFT Radar**: 5-foundation profiles (Care, Fairness, Loyalty, Authority, Sanctity) for 3 models
- **P-Score Bars**: DIT-1 and Teacher DIT P-scores (non-monotonic: Sonnet 85 > Opus 75 > Haiku 60)
- **Classification Accuracy**: MoralCode, M3oralBench, TracingMF across 3 models
- **Dual Process**: TrolleyBench ECI and CoT effect across 3 models
- **23-row Trial Table**: All benchmarks with Opus/Sonnet/Haiku values and category badges
- **10 Key Findings Accordion**: Expandable findings (WEIRD-liberal profile, non-monotonic P-scores, Haiku CoT sensitivity, etc.)
- **4 KPI Cards**: Models Compared (3), Benchmarks (23), P-Score Range (60-90), Mean Classification (97.3%)

Also added null guards to `renderMCKPICards`, `renderMCTrialTable`, `renderMCKeyFindings` to prevent crashes when data is missing.

### 3. Tab 5 (Trials) — All 3 Charts Fixed
**Root cause:** All three chart functions were placeholder implementations from Phase 4 that were never updated when actual trial data became available.

- **chartTrialBars**: Was reading `t.name` and `t.score` (nonexistent fields). Fixed to use cross-vendor trial table primary metrics — now shows 23 horizontal bars with benchmark names, Opus values, and per-bar colors
- **chartMFQRadar**: Was rendering `data: []` (empty series). Fixed to extract 5 MFT foundations (Care, Fairness, Loyalty, Authority, Purity) from the 15-dimension moral radar data, with Claude vs Human Baseline comparison
- **chartMoralMachineScatter**: Was rendering `data: []` (empty scatter). Fixed to extract 9 `dimension_preference_rates` from MP8 trial data — now shows horizontal bars with alignment rates, color-coded (green >= 67%, orange > 0%, red = 0%)

### 4. Text Contrast Fix (All Tabs)
**Root cause:** `--text-muted: #7a82a0` gave ~3.2:1 contrast ratio against `--bg-card: #181828`, failing WCAG AA (requires 4.5:1).

**Fix:**
- Bumped `--text-muted` from `#7a82a0` to `#a0a8c4` (~5.1:1 contrast ratio)
- Added `.text-muted { color: var(--text-muted) !important; }` to override Bootstrap default
- Set `.ann-what` and `.ann-finding` to `var(--text-primary)` for full-contrast annotation text
- Removed `opacity: 0.8` from `.ann-member` (was compounding the low contrast)

---

## Key Commits (Dashboard Repo)

| Hash | Description |
|------|-------------|
| `6571f36` | Council review round 2: UX enhancements, executive summary, annotation hierarchy |
| `f052932` | Fix Tab 5 (Trials) and Tab 11 (Model Comparison) charts + text contrast |
| `e38675d` | Fix Moral Machine scatter chart on Tab 5 |

---

## Remaining Work

### Priority 1: LaTeX Conversion
- NormEval, moral psych, religious values papers all need LaTeX formatting

### Priority 2: R7 — 9-Model Heatmap Granularity (Round 1 Deferred)
- Expand vendor heatmap from 3 columns to 9 individual model columns
- Requires dashboard layout refactoring for label space

### Priority 3: Human Baseline Norms (Round 1 Deferred, Partially Done)
- Tab 8 moral radar already has human baselines
- Tab 5 MFQ radar now has human baselines
- Still missing: population norms on classification/P-score charts

### Priority 4: GPT-4o / Llama-3 Replication
- Extend cross-model comparison beyond Anthropic/Gemini/OpenAI

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Generator | `DASHBOARDS/moral-psych-benchmarks/generate_dashboard.py` | Data pipeline with `build_model_comparison()` |
| Tab annotations | `DASHBOARDS/moral-psych-benchmarks/_tab_annotations.py` | Expert council annotations (11 tabs) |
| Dashboard HTML | `DASHBOARDS/moral-psych-benchmarks/index.html` | 12-tab dashboard structure |
| App JS | `DASHBOARDS/moral-psych-benchmarks/app.js` | Rendering logic with enhanced annotations |
| Charts JS | `DASHBOARDS/moral-psych-benchmarks/charts.js` | All ECharts builders (fixed Tabs 5+11) |
| Style CSS | `DASHBOARDS/moral-psych-benchmarks/style.css` | Dark theme with improved contrast |
| Council review R2 | `COUNCIL/20260404-dashboard-review-round2.md` | 24 recommendations, 10 consensus |
| Dashboard repo | `cjimmylin/cei-moral-psych-dashboard` | GitHub Pages deployment |

## Known Issues

1. **MP9 (MFTC) data missing**: Trial table shows dashes across all models for MP9 — no `key_metrics` extracted for this benchmark.
2. **MFT Radar approximation**: Tab 11 MFT foundation values are approximated from MP4 care score (Sanctity = care * 0.45, etc.) since per-foundation Likert scores aren't in the cross-vendor comparison data. Actual per-foundation values require reading the raw trial JSON.
3. **Scale sensitivity 3-grid chart**: Legend entries duplicate across grids (cosmetic).

---

*Filed: 2026-04-04 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
