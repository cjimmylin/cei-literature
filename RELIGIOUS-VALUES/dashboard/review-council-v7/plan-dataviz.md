# Data Visualization Plan: RV Dashboard v7

**Version:** 7.0
**Author:** Data Visualization Architect (council role)
**Date:** 2026-04-13
**Canonical data:** `claims_canonical.json`
**DOM skeleton:** `dom-skeleton.html`
**ECharts version:** 5.5.0 (pin exactly; do NOT use 5.5.1 referenced in skeleton — correct skeleton to 5.5.0)

---

## 0. Architecture Notes

- **Fat data, thin client.** The Python generator (`scripts/generate-dashboard-v7.py`) pre-computes all analytics and emits a `data.js` file as JS constants. `app.js` does rendering only.
- **Two-file split for v7.** v7 separates data (`data.js`) from renderer (`app.js`) — not a monolithic HTML file like v4/v6. The DOM skeleton (`dom-skeleton.html`) becomes `index.html` after CSS injection.
- **JS brace rule.** `data.js` and `app.js` are standalone `.js` files — use SINGLE `{` `}` throughout. Only Python f-string-emitted HTML/JS snippets need doubled braces.
- **Vendor labels.** All cross-vendor labels for simulated vendors must carry the `simulated-tag` CSS class and the exact prefix `Simulated:`. Anthropic (Claude) is NOT simulated; no prefix. See encoding table in Section 3.
- **Alt text.** The Python generator must pre-compute `alt_text` strings for each chart and embed them in `data.js`. The `app.js` renderer assigns these to `aria-label` on each ECharts container after `echarts.init()`.
- **No deletions.** Do not delete any files; route discards to `RECYCLE-BIN/`.

---

## 1. Frozen Legacy Block — v6 Charts to Inherit Unchanged

These 16 chart render calls map directly from the v4/v6 generator. In v7 they are placed in a `LEGACY` namespace within `app.js` and MUST NOT be modified during v7 development. The only permitted change is updating `echarts.init()` target IDs to match the v7 DOM skeleton (which are identical to v6 IDs, so no changes are needed).

| # | Render Function (v6 name) | ECharts Chart Type | Target DOM ID | Tab |
|---|---------------------------|--------------------|---------------|-----|
| L1 | `renderOverview()` → tradition bar | Bar (horizontal) | `chart-tradition-bar` | 1 |
| L2 | `renderOverview()` → family pie | Pie | `chart-family-pie` | 1 |
| L3 | *(no funnel in v6; skeleton allocates `chart-funnel`)* | Funnel | `chart-funnel` | 1 |
| L4 | `renderSensitivity()` → bootstrap CI | Custom bar+errbar (bar + markLine) | `chart-boot-ci` | 2 |
| L5 | `renderSensitivity()` → weight sensitivity | Bar | `chart-weight-sens` | 2 |
| L6 | `renderSensitivity()` → gate threshold | Line (dual y-axis) | `chart-gate-threshold` | 2 |
| L7 | *(tier table — static HTML table in v6; promote to ECharts heatmap in v7 if needed, else keep HTML)* | Table / Heatmap | `chart-tier-table` | 3 |
| L8 | *(composite bar — rendered in v6 as part of ranking section)* | Bar | `chart-composite-bar` | 3 |
| L9 | `renderVoid()` → radar | Radar | `chart-radar` | 4 |
| L10 | `renderVoid()` → readiness bar | Bar | `chart-readiness` | 4 |
| L11 | *(void grid — not explicitly a separate echarts call in v6; add as static grid or ECharts scatter)* | Scatter / Custom grid | `chart-void-grid` | 4 |
| L12 | `renderClaims()` → claim evidence summary | Bar (neg-log-p) | `chart-claims` | 5 |
| L13 | `renderCrossvendor()` → K<R<V length gradient | Bar (grouped) | `chart-cv-length` | 6 |
| L14 | `renderCrossvendor()` → rubric heatmap | Heatmap | `chart-cv-rubric` | 6 |
| L15 | `renderCrossvendor()` → T2 bar | Bar | `chart-cv-t2` | 6 |
| L16 | `renderCrossvendor()` → vendor radar | Radar | `chart-cv-radar` | 6 |
| L17 | `renderCrossvendor()` → bias-values scatter | Scatter | `chart-cv-biasvalues` | 6 |

**Total legacy charts: 17** (L3, L7, L11 were DOM-present in skeleton but not fully implemented in v6 — implement them fresh in v7 as part of the legacy block using the same analytical logic).

> Implementation note: `renderValues()` (chart-a3-hist, chart-a1-bar) existed in v6 but the Tab 5 skeleton in v7 replaces the "Values" sub-tab with a dedicated claims/robustness layout. The a3/a1 charts should be included as inline stat callouts in Tab 5 annotation prose rather than standalone ECharts panels, unless a DOM slot is added. Do not create new DOM IDs without updating the skeleton.

---

## 2. New Charts for v7 — Full Specifications

### N1. Claim 8 Forest Plot
**Target DOM ID:** `chart-claim8-forest`
**Tab:** 5 — Claims & Robustness
**ECharts chart type:** Custom series (`type: 'custom'`) with `renderItem` drawing horizontal CI whiskers, plus a `markLine` for the null-hypothesis reference line (H0: effect = 0 or H0: mean A3 = 50).

**Data source fields from `claims_canonical.json`:**
```
claims[7].tests[*]  (C8, 4 sub-tests)
  → test_name       (y-axis label)
  → effect_size     (point estimate for t-test; null for binomial/Wilcoxon rows)
  → statistic       (use as point when effect_size is null)
  → p_value         (encode significance via point color/size)
  → significant     (boolean — color: green if true, grey if false)
  → n               (display in tooltip)
```

Derived in Python generator:
- For t-test row: x-position = `effect_size` (-1.232), error bar width from t-distribution (df=n-1=15, 95% CI = effect ± t_crit × SE). SE = |effect| / |t-statistic| = 1.232 / 4.93 ≈ 0.250. CI: [-1.232 ± 1.753×0.250] = approximately [-1.670, -0.794].
- For Wilcoxon and binomial rows: no numeric effect size available; render as diamond-only (no CI whiskers), x-position = standardized z-score derived from p-value direction.
- Reference vertical line at x=0 (null).
- Claim 8 is the featured claim: use `#54A24B` (green) fill, larger point radius (8px vs 5px for C1 forest), bold test label.

**Visual encoding rationale:** Forest plot is the canonical way to display multi-test convergence. Four independent tests all supporting the same direction (values relevance failure) are more convincing than a single test. The highlighted C8 panel communicates that this is the paper's "banner" result (d=−1.23, mean A3=30/100).

**Pre-computed alt text (embed in data.js):**
> "Forest plot showing four convergent statistical tests for Claim 8: values relevance failure. One-sample t-test: d=−1.23 (p<0.001); Wilcoxon signed-rank: W=5 (p<0.001); binomial above 50: 3/16 (p=0.011); binomial above 75: 0/16 (p<0.001). All four tests support rejection of the null."

---

### N2. Claim 1 Forest Plot
**Target DOM ID:** `chart-claim1-forest`
**Tab:** 5 — Claims & Robustness
**ECharts chart type:** Same custom series as N1, but simpler (2 sub-tests only).

**Data source fields:**
```
claims[0].tests[*]  (C1, 2 sub-tests)
  → test_name         ("vs uniform", "vs proportional to corpus")
  → effect_size       (Cramer's V: 0.526, 0.305)
  → p_value           (0.0, 0.000562)
  → significant       (both true)
  → df                (both df=5)
  → n                 (both n=47)
```

Derived in Python generator:
- Cramer's V has approximate 95% CI from non-central chi-squared. For V=0.526, n=47, df=5: CI ≈ [0.38, 0.65]. For V=0.305: CI ≈ [0.16, 0.44]. Compute using: `lambda_nc_low = chi2.ppf(0.025, df, nc=stat)`, etc. — or use Wilson-Hilferty approximation. Pre-compute in Python and embed in data.js.
- Reference vertical line at x=0.
- Both tests green (significant).

**Pre-computed alt text:**
> "Forest plot for Claim 1: tradition asymmetry. Two chi-squared goodness-of-fit tests. Vs. uniform: Cramer's V=0.53 (p<0.001). Vs. proportional to corpus: Cramer's V=0.30 (p<0.001). Both confirm Islam's disproportionate dominance."

---

### N3. P-Value Strip Chart (All 8 Claims)
**Target DOM ID:** `chart-pvalue-strip`
**Tab:** 5 — Claims & Robustness
**ECharts chart type:** Scatter (`type: 'scatter'`) on a single horizontal axis (−log₁₀ p), one row per claim, y encoded as claim number.

**Data source fields:**
```
claims[*]
  → claim_id          (y-axis label)
  → tests[0].p_value  (primary test p-value per claim)
  → verdict           ("supported" | "revised" | "not_significant")
  → plain_english     (tooltip)
```

Derived in Python generator:
- x = `−log₁₀(p_value)` for each claim's primary test. If p=0.0, use p=1e-15.
- Color by verdict: `#54A24B` supported, `#F58518` revised, `#8b949e` not_significant.
- Significance threshold line at x=`−log₁₀(0.05)` ≈ 1.301 (dashed).
- Bonferroni-corrected threshold line at x=`−log₁₀(0.05/8)` ≈ 2.204 (dotted).
- Symbol size = 14 for all points (uniform).
- Tooltip: claim title + plain_english + verdict badge.

**Visual encoding rationale:** A strip chart on the -log₁₀(p) axis lets readers see immediately which claims clear both the nominal and Bonferroni thresholds in a single glance. Verdict color prevents confusion between "not significant" and "revised."

**Pre-computed alt text:**
> "Strip chart of −log₁₀ p-values for all 8 claims. C1, C2, C3, C8 exceed the Bonferroni threshold. C4, C6 are revised (non-significant but interpretation inverted). C5, C7 are non-significant."

---

### N4. Vendor Typology Grid
**Target DOM ID:** `chart-vendor-typology-grid`
**Tab:** 6 — Simulated Scorer Study
**ECharts chart type:** NOT an ECharts chart. This is a **CSS grid of three `card-rv--typology` div cards** rendered by the `app.js` renderer using `innerHTML`. Each card contains: mode label, simulated label (with `simulated-tag` span), key metrics table, gradient badge, and description paragraph.

> Rationale: The three behavioral modes (Differentiated Engagement, Compressed Accuracy, Template Refusal) are qualitative archetypes. A card layout communicates categorical distinctness better than any continuous chart type. ECharts cannot improve on a well-styled HTML card.

**Data source fields:**
```
cross_vendor_typology.*
  → label                     (card title)
  → simulated_label           (sub-label, wrapped in simulated-tag if simulated=true)
  → simulated                 (boolean — controls simulated-tag rendering)
  → description               (card body paragraph)
  → key_metrics.*             (rendered as a mini key-value table)
    → mean_rubric_knowledge
    → mean_rubric_reasoning
    → mean_rubric_values
    → mean_knowledge_length (or mean_t2_accuracy as proxy)
    → gradient_holds_all
    → bias_score_range        (for template_refusal only)
```

**Vendor label rendering rule:**
| vendor | simulated | rendered label |
|--------|-----------|----------------|
| Anthropic | false | `Claude family (Opus, Sonnet, Haiku)` — no tag |
| OpenAI (simulated) | true | `<span class="simulated-tag">Simulated:</span> Claude-roleplaying-OpenAI-scorer (Codex, Codex-Mini)` |
| Gemini (simulated) | true | `<span class="simulated-tag">Simulated:</span> Claude-roleplaying-Gemini-scorer (4 Gemini models, backfilled)` |

**Pre-computed alt text (embed in data.js as `typology_grid_alt`):**
> "Three vendor behavioral typology cards. Differentiated Engagement (Anthropic/Claude): K=1.0, R=1.0, V=0.978, gradient holds. Simulated: Compressed Accuracy (OpenAI): K=0.967, R=0.917, V=0.883, gradient absent. Simulated: Template Refusal (Gemini): K=0.0, R=0.0, V=0.05, bias 0.57-1.0."

---

### N5. T2 Span Strip Chart
**Target DOM ID:** `chart-t2-span-strip`
**Tab:** 6 — Simulated Scorer Study
**ECharts chart type:** Bar (`type: 'bar'`, horizontal) with color encoding by vendor, sorted descending by `t2_overall`.

**Data source fields:**
```
t2_span.per_model[*]
  → model           (y-axis label — use short slug from MODEL_SLUGS map)
  → vendor          (color)
  → simulated       (boolean — append "(Simulated)" to label if true)
  → t2_overall      (primary bar length, 0–1 scale → display as %)
  → t2_beginner     (secondary bar or tooltip)
  → t2_advanced     (secondary bar or tooltip)
t2_span.min_accuracy   → annotated on chart as floor value
t2_span.max_accuracy   → annotated as ceiling value
t2_span.span_pp        → title annotation "93.3 pp span"
```

**Visual encoding:**
- x-axis: 0–100% (T2 accuracy).
- y-axis: 9 model slugs, sorted descending by `t2_overall`.
- Bar color by vendor using `VENDOR_COLORS` map: Anthropic=#4C78A8, OpenAI(simulated)=#F58518, Gemini(simulated)=#E45756.
- Simulated models: render bar with 30% opacity fill + solid border (hatch effect communicates uncertainty).
- Reference line at x=93.3 (span width annotation).
- markPoint on floor (gemini-2.5-pro, 6.7%) and ceiling (claude-opus-4-6, 100%).
- Tooltip: show `t2_beginner` and `t2_advanced` breakdown.
- Title: "T2 Arabic MCQ Accuracy — 93.3 pp Span (6.7%→100%)"

**Pre-computed alt text:**
> "Horizontal bar chart of T2 Arabic MCQ accuracy across 9 models. Claude Opus and Sonnet: 100%. GPT-Codex (Simulated): 100%. Claude Haiku: 76.7%. GPT-Codex-Mini (Simulated): 86.7%. Gemini models (Simulated) range 6.7%–20%. Total span: 93.3 percentage points."

---

### N6. Rubric Ceiling Heatmap
**Target DOM ID:** `chart-rubric-ceiling-heatmap`
**Tab:** 6 — Simulated Scorer Study
**ECharts chart type:** Heatmap (`type: 'heatmap'`) with a `visualMap` component.

**Data source fields:**
```
rubric_ceiling.matrix[*]
  → model               (y-axis: short slug)
  → vendor              (y-axis group separator)
  → simulated           (boolean)
  → rubric_knowledge    (K column)
  → rubric_reasoning    (R column)
  → rubric_values       (V column)
  → rubric_bias         (Bias column)
  → at_ceiling          (boolean — used to render annotation cell overlay)
rubric_ceiling.threshold  (0.93 — reference line / annotation)
```

**Visual encoding:**
- x-axis: 4 rubric dimensions ["K", "R", "V", "Bias"] in order.
- y-axis: 9 model slugs (sorted: Claude models first, then OpenAI simulated, then Gemini simulated). y-axis labels include `(Sim.)` suffix for simulated=true models.
- Cell value: rubric score 0.0–1.0.
- `visualMap`: continuous, range [0, 1], colormap: `['#E45756', '#ffffff', '#54A24B']` (red=0, white=0.5, green=1). Invert: cells near 0.93 threshold displayed with a thin border highlight.
- Cells where `at_ceiling=true` AND value ≥ 0.93: render star symbol in top-right corner of cell using `label: { show: true, formatter: '★' }`.
- Title: "Rubric Score Matrix — ≥0.93 Ceiling Highlighted"
- `visualMap` must set `seriesIndex: []` on any decorative overlay to prevent it overriding `itemStyle.color` (per known bug in MEMORY.md).
- Grid separator: add a horizontal `markLine` between the last Anthropic model and first OpenAI model row, and between last OpenAI and first Gemini row, using `{yAxis: 2.5}` and `{yAxis: 4.5}` respectively (0-indexed).

**Pre-computed alt text:**
> "Heatmap of rubric scores (Knowledge, Reasoning, Values, Bias) for 9 models. Claude models (3): all cells ≥0.93, shown in green with star. OpenAI-simulated (2): mostly green except Values column (0.87-0.90). Gemini-simulated (4): all K/R/V cells 0.0 (red); Bias cells 0.57-1.0."

---

### N7. K < R < V Response-Length Gradient Visualization
**Target DOM ID:** `chart-cv-length` (REPLACES the v6 grouped bar chart with an enhanced version)

> **Note:** `chart-cv-length` already exists in v6 (L13). In v7, this DOM ID is RE-USED but the chart implementation is upgraded from a simple grouped bar to a **slope chart** that makes the K→R→V gradient direction visually explicit. This is the ONE exception to the "frozen legacy" rule — the DOM ID is the same but the chart type changes. Mark in `app.js` as `// UPGRADED from v6`.

**ECharts chart type:** Line (`type: 'line'`) with `smooth: false`, one series per model, x-axis = ["K", "R", "V"], y-axis = mean response length (characters).

**Data source fields:**
```
cross_vendor_typology.*.key_metrics
  → mean_knowledge_length   (K point)
  → mean_reasoning_length   (R point)
  → mean_values_length      (V point)
  → gradient_holds_all      (boolean — solid line if true, dashed if false)
(aggregate per vendor, not per model — 3 lines total)
```

Alternatively, use per-model data if `model-comparison.json` provides per-model K/R/V lengths. The v6 generator already pre-computes `cv_k_lengths`, `cv_r_lengths`, `cv_v_lengths` arrays per model — use those, generating one line per model (9 lines total), colored by vendor.

**Visual encoding:**
- 9 lines (one per model), x-axis = K / R / V (3 points).
- Lines where `gradient_holds=true` (Claude models): solid, full opacity.
- Lines where `gradient_holds=false` (OpenAI simulated, Gemini simulated): dashed, 50% opacity.
- Gemini simulated models: lines are nearly flat near 0 (compressed to axis) — visually dramatic contrast.
- Log scale on y-axis optional if OpenAI simulated lengths (79–443) vs Claude (1463–6572) cause visual compression; prefer log scale to prevent Gemini lines from disappearing.
- markArea for "gradient zone" (monotonically increasing K→R→V) shaded green at low opacity.
- Legend entries include vendor color coding.
- Title: "K < R < V Response Length Gradient"

**Pre-computed alt text:**
> "Slope chart showing mean response length across Knowledge, Reasoning, and Values items for 9 models. Claude models show steep upward slope (1463→4378→6572 chars). OpenAI-simulated: compressed flat (80→443→438). Gemini-simulated: flat near zero. Only Claude family exhibits the K<R<V gradient."

---

## 3. Chart Count and Tab Allocation

### Summary by Tab

| Tab | Tab Label | Chart IDs | Legacy (L) | New (N) | Total |
|-----|-----------|-----------|------------|---------|-------|
| 1 | Overview | chart-funnel, chart-tradition-bar, chart-family-pie | L1, L2, L3 | — | 3 |
| 2 | Landscape | chart-boot-ci, chart-weight-sens, chart-gate-threshold | L4, L5, L6 | — | 3 |
| 3 | Ranking | chart-tier-table, chart-composite-bar | L7, L8 | — | 2 |
| 4 | Tradition Coverage | chart-radar, chart-readiness, chart-void-grid | L9, L10, L11 | — | 3 |
| 5 | Claims & Robustness | chart-claims, chart-claim8-forest, chart-claim1-forest, chart-pvalue-strip | L12 | N1, N2, N3 | 4 |
| 6 | Simulated Scorer Study | chart-vendor-typology-grid, chart-cv-length, chart-cv-rubric, chart-cv-t2, chart-t2-span-strip, chart-rubric-ceiling-heatmap, chart-cv-radar, chart-cv-biasvalues | L13↑, L14, L15, L16, L17 | N4, N5, N6, N7 | 8 |

**Grand total: 23 chart/panel units across 6 tabs.**
- Legacy frozen: 17 (of which L13 is upgraded as N7 — same DOM ID)
- Net new DOM panels: 6 (N1 chart-claim8-forest, N2 chart-claim1-forest, N3 chart-pvalue-strip, N4 chart-vendor-typology-grid, N5 chart-t2-span-strip, N6 chart-rubric-ceiling-heatmap)
- Upgraded: 1 (N7/L13 chart-cv-length)

---

## 4. Data.js Constants Required for New Charts

The Python generator must emit these additional constants beyond the v6 set:

```javascript
// From claims_canonical.json → claims array
const CLAIMS_V7 = { /* full normalized claims array with verdict, plain_english */ };

// For N1: C8 forest plot
const C8_FOREST = {
  tests: [...],          // 4 sub-tests with derived CIs
  highlight_color: "#54A24B",
  null_line: 0,
  alt_text: "..."
};

// For N2: C1 forest plot
const C1_FOREST = {
  tests: [...],          // 2 sub-tests with derived Cramer's V CIs
  highlight_color: "#54A24B",
  alt_text: "..."
};

// For N3: p-value strip
const PVALUE_STRIP = {
  claims: [...],         // [{claim_id, neg_log_p, verdict, plain_english}, ...]
  sig_threshold: 1.301,  // -log10(0.05)
  bonferroni_threshold: 2.204,  // -log10(0.05/8)
  alt_text: "..."
};

// For N4: typology grid (rendered as HTML cards, not ECharts)
const TYPOLOGY_GRID = {
  modes: [...],          // 3 mode objects from cross_vendor_typology
  alt_text: "..."
};

// For N5: T2 span strip
const T2_SPAN = { /* full t2_span object from claims_canonical.json */ };

// For N6: rubric ceiling heatmap
const RUBRIC_CEILING = { /* full rubric_ceiling object from claims_canonical.json */ };
```

---

## 5. Render Function Map for app.js

```javascript
// Tab 5 — new render functions
function renderClaim8Forest()  { /* N1 — chart-claim8-forest */ }
function renderClaim1Forest()  { /* N2 — chart-claim1-forest */ }
function renderPvalueStrip()   { /* N3 — chart-pvalue-strip  */ }

// Tab 6 — new render functions
function renderTypologyGrid()  { /* N4 — chart-vendor-typology-grid (HTML, not ECharts) */ }
function renderT2SpanStrip()   { /* N5 — chart-t2-span-strip */ }
function renderRubricCeiling() { /* N6 — chart-rubric-ceiling-heatmap */ }
// N7 replaces renderCrossvendor() length section — refactor existing function

// Lazy-init pattern (re-render on tab show to avoid ECharts zero-size bug)
document.querySelectorAll('[data-bs-toggle="tab"]').forEach(tab => {
  tab.addEventListener('shown.bs.tab', e => {
    const target = e.target.getAttribute('href');
    if (target === '#tab-claims') {
      renderClaim8Forest(); renderClaim1Forest(); renderPvalueStrip();
    }
    if (target === '#tab-crossvendor') {
      renderTypologyGrid(); renderT2SpanStrip(); renderRubricCeiling();
    }
  });
});
```

---

## 6. Known Risk Table

| Risk | Mitigation |
|------|-----------|
| ECharts heatmap `visualMap` overrides `itemStyle.color` on decorative series | Set `seriesIndex: []` on any non-data visualMap (per MEMORY.md bug) |
| C8 CI derivation for binomial/Wilcoxon rows (no CI in source data) | Render as diamond-only point without whiskers; tooltip explains absence |
| `const DATA_*` in `data.js` not attached to `window` | Use `typeof DATA_X === 'undefined'` guard; or use `window.DATA_X =` assignment syntax |
| Gemini T2 bars compressed near zero — invisible in linear scale | Use log y-axis on T2 strip chart with explicit `min: 1` floor |
| Typology grid DOM injection may conflict with Bootstrap tab animation | Use `tab.addEventListener('shown.bs.tab', ...)` not `show.bs.tab` to avoid rendering into hidden container |
| Dark theme Bootstrap table text invisible | Apply `color: var(--text)` explicitly to table class; do not rely on Bootstrap defaults |

---

## 7. File Deliverables

All files must live inside `RELIGIOUS-VALUES/`:

| File | Path | Purpose |
|------|------|---------|
| Generator | `scripts/generate-dashboard-v7.py` | Reads `claims_canonical.json` + legacy data files → emits `data.js` |
| Data | `dashboard/v7/data.js` | Pre-computed JS constants |
| Renderer | `dashboard/v7/app.js` | Chart render functions |
| Styles | `dashboard/v7/styles.css` | CSS injected into skeleton |
| HTML | `dashboard/v7/index.html` | Assembled from `dom-skeleton.html` + CSS |

Reports and logs must use `YYYYMMDD-` prefix; no overwriting of existing v6 output.
