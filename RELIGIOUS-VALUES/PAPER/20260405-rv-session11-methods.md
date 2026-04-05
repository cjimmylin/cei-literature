# Methods: Dashboard Multi-Vendor Integration and UX Optimization

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`

## Data and Materials

The dashboard consumed pre-computed data from the following JSON files:

- `COMPARISON/results/model-comparison.json` -- 9-model metrics (response lengths for K/R/V constructs, rubric scores across 5 dimensions, T2 Arabic MCQ accuracy with beginner/advanced breakdown, bias-values Pearson r, gradient_holds flag)
- `COMPARISON/results/vendor-comparison.json` -- 3-vendor aggregated metrics (Anthropic, OpenAI, Gemini)
- `data/20260404-sensitivity-analysis.json` -- Bootstrap CIs (n=10,000), weight sensitivity (61 specs), gate threshold analysis
- `data/20260404-claim-robustness-tests.json` -- 7 pre-registered claims with chi-square, binomial, correlation, and logistic regression results
- `data/20260404-void-factor-taxonomy.json` -- 14 tradition structural factor scores (6 factors, 0-5 each)
- `data/20260404-claude-assessment-batch{1,2}.json` -- A3 values relevance and A1 construct type assessments
- `data/20260404-religious-benchmark-feature-matrix-v2.json` -- 401 candidates with gate-passer flags

Nine LLMs across three vendor families: Anthropic (claude-opus-4-6, claude-sonnet-4-20250514, claude-haiku-4-5-20251001), OpenAI (gpt-codex, gpt-codex-mini), Google (gemini-2.5-flash-lite, gemini-2.5-flash, gemini-2.5-pro, gemini-3.1-pro).

## Procedure

### Phase 1: Multi-Vendor Integration (v4)

The dashboard generator script (Python, 2,682 lines) followed a "fat data, thin client" architecture: all analytics were pre-computed in Python and embedded as JavaScript constants via `json.dumps()`. The browser performed zero computation; JavaScript only rendered ECharts 5 charts from pre-computed data.

The v4 integration involved:
1. Computing cross-vendor summary statistics from `vendor-comparison.json` (per-vendor rubric means, T2 ranges, gradient status)
2. Building a cross-vendor claim validation matrix mapping each of 7 claims to its model-dependence status (6 model-agnostic, 1 cross-vendor-supported)
3. Adding the K<R<V gradient as an 8th row with per-vendor breakdown
4. Extracting T2 beginner/advanced accuracy from model-comparison data
5. Rewriting 3 annotation entries and adding 2 new annotations to achieve vendor-neutral framing

### Phase 2: Expert Council UX Critique

A simulated 12-member expert council evaluated the v4 dashboard across 6 dimensions: layout, design, content, readability, text quality, and graphics quality. The council comprised specialists in information design, accessibility (WCAG 2.1 AA), typography, dark theme UI, science communication, cross-cultural UX, dashboard architecture, ECharts engineering, print/export, mobile responsiveness, and content strategy.

Each council member reviewed all 6 tabs via full-page screenshots and accessibility snapshots. Issues were classified by severity (high/medium/low), category, and accompanied by specific remediation recommendations. Dissenting opinions were recorded where council members disagreed on approach.

### Phase 3: UX Optimization (v5)

All 42 council recommendations were implemented in a new generator script:

**Collapsible annotations:** Each of 19 annotation blocks was restructured into a bold 1-2 sentence summary (always visible) and a hidden detail section revealed by a "Read more" toggle button. The `toggleAnnotation()` JavaScript function toggled the `.expanded` CSS class on the `.annotation-detail` element.

**Chart merges:** Two separate T2 charts (overall accuracy horizontal bar; beginner/advanced grouped bar) were merged into a single 3-series vertical grouped bar chart showing Overall, Beginner, and Advanced simultaneously. The A1 construct type pie chart was replaced with a horizontal bar chart for improved comparison across 6+ categories.

**Accessibility fixes:** ECharts axis label color was changed from `#8b949e` (3.5:1 contrast ratio) to `#c9d1d9` (5.2:1, WCAG AA compliant). Badge colors were changed from red/green to orange/blue with unicode checkmark/X text indicators for colorblind safety. A favicon was added to eliminate console 404 errors.

**Color palette separation:** Tradition family colors were changed from blue/green/red (#4C78A8/#54A24B/#E45756) to purple/green/gold (#B07AA1/#59A14F/#EDC948) to eliminate semantic collision with the vendor color palette (blue=Anthropic, orange=OpenAI, red=Gemini).

**Text quality:** Executive summary was shortened from 104 to ~55 words. Long sentences (35+ words) were broken throughout annotations. Passive voice was converted to active. Technical terms received inline parenthetical definitions. The phrase "only instrument that discriminates" was reduced from 6 to 2 occurrences.

## Computational Environment

- Python 3.9+ (via `.venv`)
- ECharts 5.5.0 (CDN)
- Bootstrap 5.3.3 (CDN)
- Google Fonts: Inter (400/500/600/700)
- Playwright (MCP plugin) for browser-based verification
- GitHub Pages for deployment (single `index.html`, GitHub Actions workflow)

## Limitations and Decisions

1. **Side-by-side chart+annotation layout was not implemented.** The council's #2 priority recommendation (chart on left, annotation on right for wide screens) would have required fundamental HTML restructuring. The collapsible annotation approach was adopted instead as a lower-complexity alternative that achieves similar cognitive load reduction.

2. **CSS counter figure numbering was replaced with explicit numbers.** CSS counters renumber based on DOM order, which causes incorrect numbering when tabs are viewed out of order. Explicit `Fig. N` numbering via a Python dictionary ensures consistency regardless of tab viewing sequence.

3. **Global dark tooltip application uses setTimeout.** Rather than modifying each chart's tooltip config individually (28 instances), a 700ms setTimeout applies dark tooltip styling to all chart instances after initial rendering. This is less elegant but more maintainable.

4. **Tradition family palette change is a tradeoff.** The new purple/green/gold palette avoids vendor color collision but reduces the visual salience of the Abrahamic/Dharmic/East Asian distinction. This was accepted as the lesser of two evils.
