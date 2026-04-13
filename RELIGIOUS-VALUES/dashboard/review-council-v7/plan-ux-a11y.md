# UX/IA + Accessibility Plan — Religious Values Benchmark Dashboard v7

**Author:** UX/IA Designer + Accessibility Auditor (council agent)
**Date:** 2026-04-13
**Target file:** `dashboard/review-council-v7/dom-skeleton.html` → assembled `20260413-religious-values-dashboard-v7.html`
**Standard:** WCAG 2.1 AA minimum throughout

---

## 1. Reading Order — Recommended Tab Progression

### Recommended sequence for first-time readers

```
Overview → Ranking → Tradition Coverage → Claims & Robustness → Landscape → Simulated Scorer Study
```

**Rationale:**

| Step | Tab | Why here |
|------|-----|----------|
| 1 | **Overview** | Sets context: 401 → 47 screening funnel, tradition bar, family pie. Answers "what is this dataset?" |
| 2 | **Ranking** | Shows the primary deliverable immediately — tiered benchmark table and composite bar. Readers want the answer before the methodology. |
| 3 | **Tradition Coverage** | Contextualises the ranking: why 8 traditions have zero viable benchmarks, radar + readiness charts, void grid. Directly follows the ranking so gaps are interpretable. |
| 4 | **Claims & Robustness** | Presents the 8 statistical claims that justify the ranking. Forest plots and p-value strip are most meaningful after the reader has seen the ranked data. |
| 5 | **Landscape** | Deep methodological content — bootstrap CIs, weight sensitivity, gate thresholds. Place after claims so readers who want details can drill down; readers who don't can stop. |
| 6 | **Simulated Scorer Study** | Auxiliary meta-evaluation. Vendor typology, K < R < V gradient, T2 accuracy. Positioned last because it evaluates the evaluation, not the primary finding. |

**Current DOM order** (Overview, Landscape, Ranking, Tradition, Claims, Simulated) does NOT match this recommended reading order. The tab labels should remain in DOM order for code stability, but the **visual left-to-right tab sequence** must be reordered in the `<ul class="nav nav-tabs">` block:

```
nav-overview | nav-ranking | nav-traditions | nav-claims | nav-landscape | nav-crossvendor
```

Update `aria-selected`, `show active` classes, and `tabindex` accordingly to match.

---

## 2. Progressive Disclosure — Layering Detail

### Principle
Each tab follows a three-layer hierarchy: **Summary card → Chart → Methodology note**. Never show raw methodology before the finding.

### Layer definitions

**Layer 1 — Summary cards (always visible on tab load)**
- Stat cards (`.card-stat`) with a single large number, label, and one-sentence plain-English finding.
- Maximum 4 per tab. No tooltips required at this layer.
- Example for Ranking tab: "Top-tier benchmarks: 15 | Islam leads: 9/15"

**Layer 2 — Charts (visible on tab load, below fold on mobile)**
- ECharts containers as in current skeleton. Each must have a visible `<h3 class="chart-title">` (not just an ECharts internal title, which screen readers cannot access).
- Each chart container gets a `<details class="chart-note">` element immediately below it for Layer 3 content. Default state: `open` on desktop, `closed` on mobile (`@media (max-width: 767px) details.chart-note { display: none }`). Provide a "Show methodology note" `<summary>` trigger.

**Layer 3 — Methodology notes (collapsed by default)**
- `<details>/<summary>` pattern. Content: sample size, test used, p-value interpretation, caveats.
- The caveat ribbon (global, always visible) handles cross-cutting caveats. Tab-level notes handle chart-specific ones.
- Do NOT repeat ribbon caveats verbatim in chart notes — reference them by number (e.g., "See Caveat 2: Same-Vendor Scorer Bias above").

### Annotation pattern
Use the `ANNOTATIONS` dict from the Python generator (established in S9/S10 learnings). Each chart ID maps to `{title, subtitle, methodology_note, alt_text}`. This prevents free-hand content drift between tabs.

---

## 3. Mobile Responsiveness — Bootstrap 5.3 Breakpoints

### Breakpoint strategy

| Viewport | Behaviour |
|----------|-----------|
| xs–sm (< 576px) | Single column. All `.col-lg-*` and `.col-md-*` collapse to full width. Tab labels truncate to icon + number (use `aria-label` for full name). Caveat ribbon stacks vertically: 3 cards → 1 column. |
| md (768–991px) | 2-column grid where skeleton has `.col-lg-6`. `.col-lg-4` (Overview 3-up) → 2 + 1 stacked. Landscape sensitivity charts stack. |
| lg+ (≥ 992px) | Full layout as designed. 3-up Overview, 2-up Landscape/Traditions/Claims/Simulated. |

### Specific collapse rules

- **Tab navigation**: On xs/sm, convert tab bar to a `<select>` dropdown or scrollable horizontal tabs with `overflow-x: auto; white-space: nowrap` on the `<ul>`. Do NOT wrap tabs to two rows — that doubles height and confuses tab panel association.
- **`.tab-sub` subtitle spans**: Hide with `d-none d-md-inline` on xs/sm to prevent label overflow.
- **Caveat ribbon**: `col-md-4` → stacks to `col-12` on xs. On xs, collapse all 3 caveat cards into a single `<details>` accordion titled "3 Methodological Caveats" with a warning icon.
- **Chart containers**: Fixed pixel heights in the skeleton (e.g., `height:650px` for `chart-boot-ci`) must become `min-height` with a lower mobile floor. Add responsive overrides:
  ```css
  @media (max-width: 767px) {
    #chart-boot-ci { height: 400px !important; overflow-y: auto; }
    #chart-tier-table { min-height: 350px !important; }
    .chart-container { padding: 10px; }
  }
  ```
- **Vendor typology grid** (`#chart-vendor-typology-grid`, 3 mode cards): On xs, vertical stack. On md+, 3-column row.

---

## 4. WCAG AA Compliance — Contrast and Theme

### Minimum contrast ratios
- Body text (< 18px normal / < 14px bold): **4.5:1** against background
- Large text (≥ 18px normal or ≥ 14px bold): **3:1**
- UI components and focus indicators: **3:1**

### v6 color audit — pass/fail against WCAG AA

| Token | Value | On bg-primary `#0d1117` | Ratio | Result |
|-------|-------|------------------------|-------|--------|
| `--text-primary` | `#e6edf3` | dark bg | ~15.6:1 | PASS |
| `--text-secondary` | `#8b949e` | dark bg | ~5.1:1 | PASS (body text) |
| `--accent-blue` | `#4C78A8` | dark bg | ~4.1:1 | FAIL at small text |
| `--text-chart-label` | `#c9d1d9` | dark bg | ~11.2:1 | PASS |
| `.badge-void` text | `#F58518` | `rgba(245,133,24,0.2)` badge bg | ~3.1:1 | MARGINAL — verify |
| `.badge-active` text | `#79b8f8` | `rgba(76,120,168,0.2)` badge bg | ~4.9:1 | PASS |

**Action items:**
- Replace `--accent-blue: #4C78A8` with `#6A9FD4` (ratio ~6.2:1 on dark bg) for interactive text, nav links, and claim numbers. Keep the original for chart fill colours where WCAG does not apply.
- Add a dedicated `--link-color` token distinct from the chart fill accent.
- `.nav-tabs .nav-link.active`: current colour `#4C78A8` on `#161b22` bg = ~3.9:1. Increase to `#6A9FD4`.

### Dual-theme (dark/light) support

**CSS custom property pattern** (extend v6 `:root` block):
```css
:root {
  /* dark theme (default) */
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --bg-card: #1c2128;
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --border: #30363d;
  --link-color: #6A9FD4;
}
[data-theme="light"] {
  --bg-primary: #ffffff;
  --bg-secondary: #f6f8fa;
  --bg-card: #ffffff;
  --text-primary: #1f2328;
  --text-secondary: #57606a;
  --border: #d0d7de;
  --link-color: #0969da;
}
```

**Do NOT** set `data-theme="light"` on `<html>` as default. Let CSS `:root` dark theme load first; JS reads `localStorage.getItem('rv-theme')` and applies `data-theme` attribute on `<html>` before first paint (inline `<script>` in `<head>`, before stylesheets):

```html
<script>
  (function(){
    var t = localStorage.getItem('rv-theme');
    if (t) document.documentElement.setAttribute('data-theme', t);
  })();
</script>
```

### Table dark-theme override (Bootstrap conflict)
Bootstrap 5.3 sets `table { color: #212529 }` which makes dark-theme table text invisible. Override:
```css
table.dark-table, table.dark-table td, table.dark-table th {
  color: var(--text-primary);
}
```
Use explicit hex `#1c2128` (not `var(--bg-card)`) for `.dark-table` row backgrounds — `var()` does not reliably override Bootstrap specificity on `<table>` elements.

---

## 5. Keyboard Navigation

### Tab order
1. Skip-to-content link (see below)
2. Theme toggle button
3. Tab navigation `<ul role="tablist">` — arrow-key navigation within tablist (Bootstrap handles this natively)
4. Caveat ribbon cards (tabindex=0 per card, or treat ribbon as a single focus stop)
5. Active tab panel content (charts, tables, `<details>` toggles)
6. Footer (if present)

### Tab navigation keyboard contract
Bootstrap 5.3 tab components implement the ARIA authoring practices tablist pattern:
- Left/Right arrow keys move focus between tabs (roving tabindex)
- Enter/Space activates the focused tab
- Tab key moves focus OUT of the tablist into the tab panel

**Verify** that Bootstrap's `bootstrap.bundle.min.js` correctly wires keyboard events to the `role="tablist"` / `role="tab"` / `aria-controls` attributes already in the skeleton. No custom JS required for basic keyboard navigation.

### Focus indicators
Do NOT rely on browser defaults in dark themes — they are often invisible. Add:
```css
:focus-visible {
  outline: 2px solid var(--link-color);
  outline-offset: 2px;
  border-radius: 2px;
}
/* Remove for mouse users only */
:focus:not(:focus-visible) {
  outline: none;
}
```
This satisfies WCAG 2.4.11 (Focus Appearance, AA in WCAG 2.2) and keeps the dark theme clean for mouse users.

### `<details>` / `<summary>` keyboard
Native `<details>` elements are keyboard-accessible by default (Space/Enter toggles). No additional ARIA needed. Ensure `<summary>` has a visible focus indicator via the `:focus-visible` rule above.

---

## 6. Skip-to-Content Link

Place as the very first child of `<body>`, before the caveat ribbon:

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 1rem;
  background: var(--link-color);
  color: #fff;
  padding: 0.5rem 1rem;
  border-radius: 0 0 4px 4px;
  font-weight: 600;
  z-index: 9999;
  transition: top 0.1s;
}
.skip-link:focus {
  top: 0;
}
```

Add `id="main-content"` to the first meaningful content region. Since the caveat ribbon is persistent context, the skip link should target the tab navigation `<ul>` or the active tab panel — use `id="mainTabs"` as the target:

```html
<a href="#mainTabs" class="skip-link">Skip to navigation</a>
```

Also add a second skip link if the caveat ribbon is verbose:

```html
<a href="#tab-overview" class="skip-link" style="left:9rem;">Skip ribbon</a>
```

---

## 7. Screen Reader Support — ARIA Labels for Charts

### Rule
Every `<div class="chart-container">` must have:
1. A visible `<h3 class="chart-title">` as the first child (not inside the ECharts canvas)
2. `role="img"` on the ECharts container div
3. `aria-label` on the ECharts container div with pre-computed alt text
4. A `<p class="sr-only" id="chart-{id}-desc">` with the full alt text, referenced via `aria-describedby`

**Pattern** (to be emitted by Python generator `generate_chart_block()`):

```html
<div class="card-rv">
  <h3 class="chart-title">{chart_title}</h3>
  <div id="{chart_id}"
       class="chart-container"
       style="height:{height}px"
       role="img"
       aria-label="{alt_text_short}"
       aria-describedby="{chart_id}-desc">
  </div>
  <p class="sr-only" id="{chart_id}-desc">{alt_text_long}</p>
  <details class="chart-note">
    <summary>Show methodology note</summary>
    <p>{methodology_note}</p>
  </details>
</div>
```

**`sr-only` CSS** (include in stylesheet):
```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}
```

### Pre-computed alt text — source of truth
Alt text strings must be generated by the Python `data.js` generator, not handwritten in HTML. The generator reads from an `ANNOTATIONS` dict keyed by chart ID. Each entry has:
- `title`: visible chart heading
- `alt_short`: ≤ 80 chars, for `aria-label`
- `alt_long`: full description, for `aria-describedby` paragraph
- `methodology_note`: collapsed `<details>` content

The generator emits these as a `const CHART_ANNOTATIONS = { ... }` constant in `data.js`. `app.js` reads `CHART_ANNOTATIONS[chartId]` and calls `container.setAttribute('aria-label', ann.alt_short)` after ECharts initialises.

---

## 8. Tradition-Specific Alt Text Template

**5-part structure:**

```
{chart_type} showing {tradition_name} tradition {direction_phrase} with {numeric_value} {metric_description}.
```

### Parts

| Part | Description | Example |
|------|-------------|---------|
| 1. Chart type | Literal chart type in plain English | "Heatmap", "Bar chart", "Radar chart", "Forest plot" |
| 2. Tradition name | Full tradition name from controlled vocabulary | "Islamic", "Buddhist", "Christian", "Hindu", "Jewish", "Confucian", "Indigenous", "Secular" |
| 3. Benchmark name | Name of the specific benchmark or metric being displayed | "benchmark coverage", "composite score", "readiness index" |
| 4. Numeric value | The key data point, always with units | "9 of 15 top benchmarks", "score 72.4", "4 of 14 dimensions" |
| 5. Direction of finding | Plain English direction/significance | "scoring highest", "ranking third", "showing zero viable benchmarks", "tied with Buddhist tradition" |

**Template string:**
```
{chart_type} showing {tradition_name} {benchmark_name} with {numeric_value}, {direction_phrase}.
```

**Concrete examples:**

- Heatmap showing Islamic tradition benchmark coverage with 9 of 15 top benchmarks, scoring highest among all traditions.
- Bar chart showing Buddhist tradition composite score with 43.2 points, ranking fourth of fourteen traditions.
- Radar chart showing Indigenous tradition readiness index with 0 of 14 dimensions covered, indicating zero viable benchmarks.
- Forest plot showing Jewish tradition claim 1 effect size with d = 0.34 (95% CI [0.18, 0.51]), statistically significant at p < 0.01.

**Generator implementation** — in `generate_tradition_alt(chart_type, tradition, benchmark_name, numeric_value, direction)`:
```python
def generate_tradition_alt(chart_type, tradition, benchmark_name, numeric_value, direction):
    return (
        f"{chart_type} showing {tradition} tradition {benchmark_name} "
        f"with {numeric_value}, {direction}."
    )
```
Call this function for every tradition-level chart and store output in `ANNOTATIONS`.

---

## 9. Caveat Ribbon ARIA

### Correct markup

The current skeleton uses `role="complementary"` and `aria-label="Methodological caveats"`. Per WCAG and the ARIA spec, `role="note"` is more semantically precise for methodological caveats. Update to:

```html
<aside id="caveat-ribbon"
       class="caveat-ribbon"
       role="note"
       aria-label="Methodological caveats — read before interpreting charts">
```

**Why `role="note"` over `role="complementary"`:**
- `complementary` (`<aside>` implicit role) is a landmark. Screen readers announce it as a navigation destination, which encourages users to tab to it repeatedly.
- `role="note"` explicitly signals non-navigational advisory content. Screen readers announce it inline during reading flow without listing it as a landmark.
- However, `role="note"` removes the landmark, making the ribbon un-jumpable from the screen reader landmarks menu. If landmark discoverability is important, keep `role="complementary"` (the `<aside>` default) but add `aria-label` to distinguish it from other complementary regions.

**Recommended compromise:** Keep `<aside>` (preserves landmark), override role to `complementary` with a descriptive label:
```html
<aside id="caveat-ribbon"
       class="caveat-ribbon"
       aria-label="Methodological caveats">
```

### DOM placement
The caveat ribbon is already placed BEFORE the tab navigation in `dom-skeleton.html` (lines 16–36). This is correct. Screen readers in document order will encounter the ribbon before the tabs, so users receive caveat context before chart data. **Do not move it.**

### Individual caveat card markup

```html
<div class="card-rv card-rv--caveat"
     id="caveat-cav1"
     role="note"
     aria-label="Caveat 1: T2 Blinding Asymmetry">
  <p class="caveat-label"><strong>Caveat 1</strong> — T2 Blinding Asymmetry</p>
  <p class="caveat-body"><!-- description --></p>
</div>
```

Using `role="note"` on individual cards (not the outer `<aside>`) is appropriate here because the cards are discrete advisory items within the landmark region.

### On xs/sm mobile accordion
When the 3-card ribbon collapses to a single `<details>`:
```html
<details id="caveat-mobile-accordion" class="d-md-none">
  <summary role="button" aria-expanded="false">
    3 Methodological Caveats (tap to expand)
  </summary>
  <!-- caveat cards -->
</details>
<div class="d-none d-md-block" id="caveat-desktop-grid">
  <!-- 3-column grid as in skeleton -->
</div>
```

---

## 10. Theme Toggle — Version-Counter Pattern for ECharts

### Problem
When a user switches themes on an inactive tab, the ECharts instance on that tab was never rendered with the new theme. Calling `chart.setOption()` before the tab is visible triggers a 0×0 render.

### Solution: version-counter pattern

**Established in `memory/20260405h-echarts-theme-version-counter.md`**. Implementation for v7:

```javascript
// In app.js
let themeVersion = 0;
const chartInstances = {}; // chartId → echarts instance
const chartRenderedVersion = {}; // chartId → version when last rendered

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('rv-theme', theme);
  themeVersion++;

  // Re-render charts on ACTIVE tab only
  const activePanel = document.querySelector('.tab-pane.active');
  if (!activePanel) return;
  activePanel.querySelectorAll('.chart-container[id]').forEach(el => {
    const id = el.id;
    if (chartInstances[id]) {
      reRenderChart(id, theme);
      chartRenderedVersion[id] = themeVersion;
    }
  });
}

// Called when a tab becomes visible (Bootstrap 'shown.bs.tab' event)
document.getElementById('mainTabs').addEventListener('shown.bs.tab', function(e) {
  const panelId = e.target.getAttribute('href'); // e.g. "#tab-ranking"
  const panel = document.querySelector(panelId);
  if (!panel) return;
  panel.querySelectorAll('.chart-container[id]').forEach(el => {
    const id = el.id;
    if (chartRenderedVersion[id] !== themeVersion) {
      reRenderChart(id, currentTheme());
      chartRenderedVersion[id] = themeVersion;
    }
  });
});

function reRenderChart(id, theme) {
  if (chartInstances[id]) {
    echarts.dispose(chartInstances[id]);
  }
  const el = document.getElementById(id);
  chartInstances[id] = echarts.init(el, theme === 'light' ? 'light' : null);
  // Re-apply the stored option
  if (chartOptions[id]) {
    chartInstances[id].setOption(chartOptions[id]);
  }
}
```

**ECharts theme names:**
- Dark: pass `null` or `undefined` (use CSS custom properties for colours in `option`)
- Light: pass `'light'` to `echarts.init()`

**Toggle button HTML:**
```html
<button id="theme-toggle"
        class="btn btn-sm btn-outline-secondary ms-auto"
        aria-label="Toggle light/dark theme"
        aria-pressed="false">
  <span class="theme-icon">☀</span>
</button>
```

Update `aria-pressed` in JS when toggling. Place button in the header row, right-aligned. Do not use a `<div>` — native `<button>` provides keyboard and screen reader support without extra ARIA.

---

## 11. Implementation Checklist for CSS/HTML/JS Agents

### CSS agent
- [ ] Define `:root` dark vars + `[data-theme="light"]` override block
- [ ] Replace `--accent-blue` with `--link-color: #6A9FD4` for interactive elements
- [ ] Add `.sr-only` utility class
- [ ] Add `.skip-link` with `:focus` reveal
- [ ] Add `:focus-visible` outline rule
- [ ] Add mobile overrides for chart heights and caveat ribbon
- [ ] Override Bootstrap table color conflict: `table.dark-table { color: var(--text-primary) }`
- [ ] Use explicit hex `#1c2128` for table row backgrounds (not `var(--bg-card)`)

### HTML agent
- [ ] Add skip-to-content link as first `<body>` child
- [ ] Reorder tab `<li>` sequence: Overview → Ranking → Tradition → Claims → Landscape → Simulated
- [ ] Update `aria-selected` and `show active` on reordered tabs
- [ ] Change caveat ribbon to `<aside aria-label="Methodological caveats">` (no `role` override needed, `<aside>` = complementary landmark)
- [ ] Add `role="note"` to each caveat card `<div>`
- [ ] Add `<h3 class="chart-title">` before each ECharts container
- [ ] Add `role="img" aria-label="{alt_short}" aria-describedby="{id}-desc"` to each ECharts div
- [ ] Add `<p class="sr-only" id="{id}-desc">{alt_long}</p>` after each ECharts div
- [ ] Add `<details class="chart-note"><summary>Show methodology note</summary>...</details>` after each sr-only paragraph
- [ ] Add `id="mainTabs"` target for skip link (already present in skeleton)
- [ ] Add inline `<script>` in `<head>` for theme persistence before stylesheet load
- [ ] Add mobile caveat accordion (`d-md-none` / `d-none d-md-block` pair)
- [ ] Add `<button id="theme-toggle" aria-pressed="false" aria-label="...">` in header

### JS agent (app.js)
- [ ] Implement `themeVersion` counter + `chartRenderedVersion` map
- [ ] Wire `shown.bs.tab` event for lazy re-render on inactive tabs
- [ ] Wire `theme-toggle` button with `applyTheme()`, `aria-pressed` update, and icon swap
- [ ] Read `CHART_ANNOTATIONS` from `data.js` and set `aria-label` on each chart container after init
- [ ] Store each chart's `option` in `chartOptions[id]` before calling `setOption()` to enable re-render

### Python generator (data.js)
- [ ] Add `ANNOTATIONS` dict with all chart IDs as keys
- [ ] Each annotation: `{title, alt_short, alt_long, methodology_note}`
- [ ] Use `generate_tradition_alt()` function for all tradition-level charts
- [ ] Emit `const CHART_ANNOTATIONS = { ... };` before other constants in `data.js`

---

## 12. Verification Steps (post-assembly)

1. **Contrast check**: Run axe-core or WAVE against both light and dark themes. Zero AA violations required.
2. **Keyboard audit**: Tab through entire dashboard with mouse disconnected. Confirm skip link, tab navigation, theme toggle, and all `<details>` elements are reachable.
3. **Screen reader spot-check**: VoiceOver (macOS) — navigate to each chart, confirm `role="img"` is announced with alt text.
4. **Mobile check**: Chrome DevTools at 375px. Confirm tab bar is scrollable (not wrapping), caveat accordion shows, chart heights are sensible.
5. **Theme toggle + inactive tab**: Switch to Ranking tab, toggle theme, switch to Landscape tab — verify charts render in new theme.
6. **Playwright screenshot**: `python3 -m http.server 8765` from dashboard dir; capture both themes at 1440px and 375px widths.
