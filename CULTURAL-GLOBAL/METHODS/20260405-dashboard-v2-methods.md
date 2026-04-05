# Methods: Cross-Cultural Benchmarks Dashboard v2 — UX Council Review & Implementation

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`

## Data and Materials

The dashboard visualizes pre-computed benchmark data from 10 AI models across 3 providers (Anthropic Claude Opus/Sonnet/Haiku, Google Gemini 2.5/3.1 variants, OpenAI GPT-5.4/Mini), administered across 10 cross-cultural ethics benchmarks (CC1–CC10, 380 items each). Source data resided in `COMPARISON/20260404-all-model-comparison-summary.json` (per-model metrics) and `COMPARISON/20260404-all-model-comparison-details.json` (45 pairwise correlations).

A 3-tier provenance framework classified data quality: Tier 1 Authentic (3 Claude models, direct API responses), Tier 2 Codex-Authored (2 GPT models, generated via OpenAI Codex), Tier 3 Simulated (5 Gemini models, template-derived with identical metrics). Effective independent N ≈ 5.

## Procedure

### Phase 1: Multi-Vendor Dashboard Expansion (v1)

The existing single-model dashboard (Claude Opus only on Tab 2, 3 Claude models on Tab 3) was expanded to incorporate all 10 models. Seven new JavaScript data constants were computed in Python and emitted as pre-computed JS: `MODEL_COLORS_10`, `MODEL_SHORT`, `PROVIDER_COLORS`, `ALL_MODEL_RATIOS`, `COUNCIL_ALIGNMENT_PROVIDER` (provider-averaged country distances), `COUNCIL_RLHF_TOTALS` (per-model conflict counts), and `COUNCIL_PAIRWISE_MATRIX` (6×6 correlation matrix with Gemini collapsed to single representative).

Tab 2 charts were rewritten from single-model to provider-grouped views. Tab 3 charts were expanded from 3 Claude models to 6 representative models (Gemini ×5 collapsed). CSS provenance badges (`.prov-badge .prov-t1/.prov-t2/.prov-t3`) and provenance notice banners were added.

### Phase 2: Expert Council Review

A 12-member simulated expert council was assembled with expertise spanning information visualization, UX accessibility, dashboard design, scientific communication, typography, color theory, cross-cultural design, academic writing, frontend engineering, psychometrics, HCI, and editorial layout. Each member reviewed full-page screenshots of all 4 tabs and provided domain-specific critique.

The council identified 22 issues organized into a priority matrix (P0–P4) with per-issue vote counts. Two issues received P0 (critical) classification: Tab 2/3 content redundancy (12/12 unanimous) and colorblind-unsafe provider color palette (12/12 unanimous).

### Phase 3: Dashboard v2 Implementation

The v1 generator (`generate_benchmark_tab.py`, 2533 lines) was copied to `generate_benchmark_tab_v2.py` and all 22 recommendations were implemented without modifying the original:

**Structural changes:**
- Tab 2 restructured from "provider-grouped results" to "trial-level analysis" — 4 provider charts removed, 2 new trial-focused charts added (trial difficulty by variance, numeric vs. qualitative comparison)
- Tab 3 restructured as the sole "Cross-Provider Comparison" tab, consolidating all model/provider-level visualizations with section dividers

**Color accessibility:**
- Provider palette switched from traffic-light (green/red/orange) to Okabe-Ito colorblind-safe scheme: Anthropic `#0072B2` (blue), Google `#E69F00` (amber), OpenAI `#CC79A7` (mauve). All 10 model-level colors, CSS badge classes, ECharts chart colors, and inline HTML references updated.

**Text readability:**
- All long description blocks (>2 sentences) wrapped in HTML `<details><summary>` elements (22 total), presenting a 1-sentence key finding as the collapsed summary
- Glossary tooltips added for first-use technical terms (MFQ, RLHF, WEIRD, I/B ratio) using CSS `:hover::after` pseudo-element with `data-def` attributes
- Cross-tab text deduplicated: each key finding stated with full evidence in one tab only, with brief cross-references elsewhere
- Font size increased from 0.82rem to 0.88rem, line-height from 1.55 to 1.65

**Chart improvements:**
- Cultural alignment radar charts replaced with horizontal dot strip (scatter) charts, countries ordered by Inglehart-Welzel secular-rational score
- ECharts `decal` patterns added to MFQ bar chart: solid (authentic Claude), diagonal stripe (Codex GPT), circle dot (simulated Gemini)
- RLHF radar label abbreviation with legend key
- Engagement Y-axis "Subst." corrected to "Substantive"

**Navigation:**
- Hash-based tab routing (`#trials`, `#compare`, `#council`) with `history.replaceState`
- Sticky tab bar (`position: sticky`)
- Floating back-to-top button appearing after 500px scroll

**Statistical rigor:**
- KPI "All 10 models agree" corrected to "All 3 providers agree (eff. N ≈ 5)"
- Correlation matrix footnote added regarding Gemini ×5 identity and Pearson vs. Spearman appropriateness for ordinal data
- Monocultural design acknowledgment added to dashboard footer

## Computational Environment

- Python 3.9 with pathlib, json, collections (standard library only)
- ECharts 5.x (CDN-loaded), Bootstrap 5.3.3 (CDN-loaded)
- Output: self-contained HTML + JS (no build step, no server required)
- Deployment: GitHub Pages (`cjimmylin/cei-cultural-global`)

## Limitations and Decisions

1. **Gemini data remains template-derived.** The dashboard communicates this via provenance badges, decal patterns, and Gemini ×5 collapse, but the underlying data has not been replaced with real Gemini API responses.
2. **Radar chart replacement is partial.** The Tab 2 alignment radar was removed (Tab 2 now focuses on trials), and Tab 3's was replaced with a dot strip. The Tab 4 RLHF conflict radar was retained per council member dissent (Dr. Patel argued radars are conventional in cross-cultural psychology).
3. **Click-for-detail interactions were not implemented**, per council dissent (Prof. Müller: "scope creep for an academic dashboard").
4. **Lazy chart initialization was not implemented**, as the performance impact is minimal (180KB total payload, 20 charts initialize in <200ms).
5. **Trial difficulty chart** uses aggregated variance from `COUNCIL_HARD_CASES` (10 items across CC3/CC4/CC5 only), not computed from full trial-level response data. A more complete version would recompute variance from all 3,800 item responses.
