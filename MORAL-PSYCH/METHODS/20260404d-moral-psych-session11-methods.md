# Methods: Cross-Vendor LLM Moral Psychology Benchmark Analysis

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`

## Data and Materials

### Benchmark Battery
Twenty-three psychometric moral psychology benchmarks (MP2-MP22, MP-CC, MP-DM, MP-DP, MP-SI) were administered to nine large language models. Instruments spanned Moral Foundations Theory (MFQ-30, MFV-30, MFTC, Conscience Conflict, TracingMF, MoralCode), Kohlberg stages (DIT-1, EMNLP Teacher DIT), Schwartz Values (ValueCompass, Kaleidoscope, ValAct-15K), trolley/consequentialism (TrolleyBench, Moral Machine), dual-process theory (custom protocol), social intuitionism (custom dumbfounding protocol), cross-cultural reasoning (Cross-Cultural Divergence, Cultural Persona MFQ-30), and multi-theory instruments (UniMoral, Moral Identity Scale, Social Chemistry, M3oralBench, PRIME).

### Models
Nine models from three vendors were tested:
- **Anthropic:** claude-opus-4-6 (large), claude-sonnet-4-6 (medium), claude-haiku-4-5-20251001 (small)
- **Google/Gemini:** gemini-2.5-pro, gemini-3.1-pro, gemini-2.5-flash, gemini-2.5-flash-lite
- **OpenAI:** gpt-5-codex (Codex), gpt-mini (Codex-mini)

### Data Sources
Trial results were stored as structured JSON files (207 total) in `MORAL-PSYCH/TRIALS/` with vendor-specific subdirectories. Pre-computed cross-vendor comparison data was stored in `MORAL-PSYCH/COMPARISON/20260404-cross-vendor-comparison.json`, containing per-benchmark per-model key metrics extracted from all 207 trial files.

## Procedure

### Cross-Vendor Analysis Pipeline
1. **Metric extraction:** For each of 23 benchmarks, a primary scalar metric was identified (e.g., MFQ-30 Ind/Bind ratio, DIT P-score, ValAct gap rate). These were extracted from the comparison JSON's `per_benchmark_comparison[trial_id].model_values[model].key_metrics` structure.

2. **23x9 primary metric matrix:** One numeric value per benchmark per model, with missing data (empty key_metrics) coded as None. MP-DM (Dyadic Morality) had 1 missing model (Haiku).

3. **Vendor family aggregation:** Models were grouped by vendor. Family means were computed for each benchmark (Anthropic: n=3, Gemini: n=4, OpenAI: n=2).

4. **Convergence/divergence decomposition:** For each benchmark, total variance, within-vendor variance (mean of per-vendor variances), and between-vendor variance (variance of vendor means) were computed. Discrimination ratio = between/total.

5. **Benchmark discrimination ranking:** Coefficient of variation (CV = std/|mean|) computed across all 9 models per benchmark. Benchmarks ranked by CV descending.

6. **Scale sensitivity:** Within-family size orderings defined (Haiku→Sonnet→Opus for Anthropic; Flash-Lite→Flash→2.5 Pro→3.1 Pro for Gemini; Mini→Codex for OpenAI). Gradient and monotonicity computed per benchmark per vendor family.

7. **RLHF fingerprinting:** Six universal RLHF signatures identified: WEIRD-liberal bias (Ind/Bind > 2.0), purity floor (~1.0), authority suppression (0.29 win rate), ethical consistency ceiling (ECI = 1.0), post-conventional default (P-scores 60-90), deontological refusal asymmetry (personal 0.1-0.5 vs impersonal 0.9-1.0).

### Expert Council Review
A 12-member interdisciplinary council reviewed all visualizations in three iterative rounds. Council composition: psychometrics, moral philosophy, AI safety, cross-cultural psychology, computational linguistics, cognitive science, religious studies, statistics, AI industry, policy, developmental psychology, philosophy of mind.

Round 1 addressed visual clarity (10 fixes: radar overplotting, scale alignment, origin clustering, ceiling labels, diagonal reference, trial table formatting, KPI fractions, variance tooltips, CSS refactoring, mobile responsiveness). Round 2 addressed data quality (3 critical fixes: radar normalization, heatmap normalization, convergence scaling). Round 3 addressed scale mixing (1 fix: theory coverage normalization).

### Dashboard Annotation
Annotations were authored for all 12 tabs following a structured schema: intro blocks (title + summary), chart annotation blocks (what/finding/interpretation/member), and description blocks. All annotations were attributed to specific council members by domain expertise. The annotation module (`_tab_annotations.py`, 855 lines) was imported by the dashboard generator and serialized to `data.js` for client-side rendering.

## Analysis

### Normalization
Radar chart values were normalized to 0-100 using absolute scale anchors appropriate to each instrument's range (e.g., MFV care: 0-4, DIT P-score: 0-100, Ind/Bind ratio: 0-4, dumbfounding rate: 0-1). This replaced initial min-max normalization across models, which produced degenerate binary values when all models scored identically on a dimension.

Vendor heatmap values were expressed as percentage deviation from the cross-vendor mean per benchmark. This replaced per-row min-max normalization, which amplified negligible differences to a 0-100 scale.

Theory coverage values were normalized to 0-100 using benchmark-specific scale anchors before averaging, preventing instruments on different scales (P-score 0-100 vs Likert 0-5) from dominating the visualization.

Convergence scatter axes used log10 transformation to handle the multi-order-of-magnitude variance range (MP3 at 40.28 vs others at <0.03).

### Ceiling Effect Detection
Benchmarks where all 9 models produced identical scores (within rounding to 3 decimal places) were classified as ceiling effects. Six benchmarks were identified: MP6 (EMNLP Teacher DIT, P=90.0), MP7 (TrolleyBench, ECI=1.0), MP8 (Moral Machine), MP10 (MoralCode), MP11 (Kaleidoscope, accuracy=1.0), MP21 (PRIME).

## Computational Environment

- Python 3.9 (via `.venv`)
- ECharts 5.5.1 (CDN), Bootstrap 5.3.3 (CDN), Google Fonts Inter
- Dashboard generator: Python → data.js (3.5 MB) → static HTML/JS/CSS
- Node.js v24.13.1 (validation only)
- Playwright MCP server (visual QA)
- GitHub Pages (deployment)

## Limitations and Decisions

1. **Single-administration design:** N=1 per model per benchmark. No error bars, confidence intervals, or significance tests. All cross-vendor "differences" are point estimates.
2. **Self-administration confound:** All benchmarks administered by the models to themselves via Claude Opus 4.6 orchestrator. Models with knowledge of test structure (MP22: 100% foundation identification accuracy) cannot be treated as naive respondents.
3. **Orchestrator bias:** Claude Opus 4.6 (Anthropic) orchestrated all trials including Gemini and OpenAI models. Systematic prompt construction biases may favor Anthropic model performance.
4. **Temporal snapshot:** All trials conducted on 2026-04-04. Model weights may have been updated since. Results are snapshots, not stable properties.
5. **Normalization trade-offs:** Absolute scale anchors require manual specification of each instrument's range. Mis-specified anchors could compress or inflate variation. The anchors used were derived from instrument documentation.
