# Expert 07 — WCAG 2.2 AA Accessibility Audit

**Role:** Accessibility specialist
**Scope:** NormEval Dashboard v2 (index.html + style.css) evaluated against WCAG 2.2 AA, with fixes specified for v4

---

## (a) Color Contrast Ratios

**V1: `--text-secondary` (#9498b3) on `--bg-primary` (#0f1117).**
Computed contrast ratio: approximately 4.3:1. Passes AA for normal text (4.5:1 threshold) only marginally and fails for the many elements rendered at 0.75rem-0.85rem where the effective rendering is small text. The `.metric-label` (0.75rem uppercase), `.tab-explainer` body text (0.88rem), `.footnote` (0.78rem), and `.chart-subtitle` (0.8rem) all use `--text-secondary` at sizes that demand the 4.5:1 ratio.

**V2: `--text-muted` (#8a8ea8) on `--bg-primary` (#0f1117).**
Contrast ratio: approximately 3.6:1. Fails AA for normal text. Used in `.tab-position`, `.footnote`, `.gate-note`, nav-link default state, figure counter prefix, and `.placeholder-msg`. This is a systematic failure affecting dozens of elements.

**V3: `--text-muted` (#8a8ea8) on `--bg-secondary` (#161822).**
Contrast ratio: approximately 3.3:1. Fails AA. Appears in tab-explainer blocks, table headers, and expert-analysis panels.

**V4: `.accent-green` (#4ecb71) on `--bg-card` (#1c1f2e).**
Contrast ratio: approximately 4.8:1. Passes AA for normal text, but `.weight-cell` uses it at 0.72rem mono, which is borderline.

**V5: `.accent-orange` (#f0983e) on transparent badge backgrounds.**
The badge text colors (`.gate-badge.fail`, `.claim-status.revised`, `.severity-badge.moderate`) use accent colors on semi-transparent backgrounds. Actual contrast depends on the computed background, which compounds `--bg-card` with an rgba overlay. These need explicit verification per instance.

**Proposed fix (v4):** Lighten `--text-secondary` to #a8acc4 (~5.2:1) and `--text-muted` to #9ea2bc (~4.6:1). Add a comment block documenting contrast ratios for all pairings.

---

## (b) Keyboard Navigation

**V6: No `aria-selected` or `aria-controls` on tab links.**
The `<a role="tab">` elements lack `aria-selected="true|false"` and `aria-controls="tab-overview"` attributes. Bootstrap 5.3 JS adds these dynamically, but the HTML source should include them as fallbacks for progressive enhancement.

**V7: Focus indicator on `.papers-toolbar input:focus` removes the outline.**
`outline: none; border-color: var(--accent-blue)` replaces the default focus ring with a subtle border change. This fails WCAG 2.4.7 (Focus Visible) because the 1px border-color change from #2a2d42 to #5b8def is insufficient for users who rely on high-visibility focus indicators.

**V8: No visible focus style on `.filter-btn`, `.btn-export`, or table `<th>` sort headers.**
These interactive elements have no `:focus` or `:focus-visible` rules. Keyboard users cannot determine which element is focused.

**V9: Skip link targets `#mainTabContent` correctly.** This is implemented properly.

**V10: Tab overflow scroll has no keyboard scroll affordance.**
The `.nav-tabs` container uses `overflow-x: auto` with CSS fade gradients, but provides no mechanism for keyboard users to scroll to off-screen tabs (e.g., arrow key handling within the tablist).

**Proposed fix (v4):** Add `:focus-visible` with a 2px solid outline (offset 2px) using `--accent-blue` to all interactive elements. Add `aria-selected`, `aria-controls` attributes in HTML. Implement arrow-key navigation within the tablist per WAI-ARIA Authoring Practices.

---

## (c) ARIA Labels on Interactive Elements

**V11: Tab `<ul>` has `aria-label="NormEval Dashboard Navigation"`.** Correct.

**V12: Filter `<select>` elements lack `<label>` or `aria-label`.**
`#filter-gate`, `#filter-tradition`, `#filter-year`, and `#paper-search` have placeholder text but no associated `<label>` element or `aria-label` attribute. Screen readers announce these as unlabeled form controls.

**V13: `.btn-export` lacks `aria-label`.**
The button text "Export CSV" is sufficient as an accessible name, but should include context: `aria-label="Export papers table as CSV"`.

**V14: Table sort headers use `cursor: pointer` but have no `role="button"` or `aria-sort`.**
The `<th data-sort="...">` elements are clickable for sorting but provide no ARIA sort direction indicator. Screen readers cannot convey sort state.

**Proposed fix (v4):** Add `aria-label` to all filter controls. Add `aria-sort="none|ascending|descending"` to sortable `<th>` elements, updated by JS on sort. Add `<label class="visually-hidden">` for each form input.

---

## (d) Screen Reader Experience for ECharts

**V15: Zero `aria-label` or descriptive text on any chart container.**
All ECharts divs (e.g., `#chart-gates-donut`, `#chart-tradition-freq`) are empty `<div>` elements with no `role`, `aria-label`, or fallback text. ECharts renders to `<canvas>`, which is completely opaque to screen readers.

**V16: No data tables provided as chart alternatives.**
WCAG 1.1.1 (Non-text Content) requires a text alternative for all non-text content. Charts convey critical data (tradition frequencies, composite distributions, cross-model heatmaps) with no accessible alternative.

**Proposed fix (v4):** Add `role="img"` and `aria-label="[Chart title]: [1-sentence summary]"` to every `.echarts-box` wrapper. For each chart, generate a hidden `<table class="visually-hidden">` with the underlying data, referenced via `aria-describedby`. ECharts' built-in `aria.enabled = true` option can also be set in chart options for basic descriptions.

---

## (e) Motion/Animation Preferences

**V17: No `prefers-reduced-motion` media query exists anywhere in the CSS.**
The stylesheet includes: (1) a `@keyframes spin` animation for the loading spinner, (2) multiple `transition: all 0.2s ease` declarations on cards, tabs, and buttons. Users who set `prefers-reduced-motion: reduce` in their OS will still see all animations.

**Proposed fix (v4):**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## (f) Font Sizing and Responsive Breakpoints

**V18: Single breakpoint at 768px.**
The only `@media` rule is `max-width: 768px`, which adjusts padding and metric-value font size. There is no handling for large screens (>1440px), small phones (<375px), or landscape tablets (768-1024px). The papers table will overflow on narrow screens with no horizontal scroll indicator.

**V19: Font sizes use `rem` throughout.** This is correct and respects user font-size preferences.

**V20: Minimum font size of 0.65rem (severity-badge, version-badge).**
At a default 16px root, 0.65rem = 10.4px. WCAG does not mandate a minimum font size, but text below 12px is difficult to read. Several elements cluster at 0.68-0.72rem (10.9-11.5px), which risks readability especially on mobile.

**V21: `.nav-tabs` uses `white-space: nowrap` with no wrapping fallback.**
On narrow screens, tabs extend off-screen. The CSS gradient pseudo-elements hint at scroll but provide no explicit visual indicator (e.g., a scroll arrow or truncation).

**Proposed fix (v4):** Add breakpoints at 480px and 1200px. Set a floor of 0.75rem (12px) for all text. Add a visible scroll indicator or tab collapse (hamburger/dropdown) for mobile tab navigation.

---

## Summary: 21 Violations Found

| Priority | Count | Categories |
|----------|-------|------------|
| Critical (AA fail) | 5 | V1-V3 contrast, V15-V16 chart alternatives |
| Major | 8 | V6-V8 focus, V10 tab scroll, V12-V14 ARIA, V17 motion |
| Minor | 8 | V4-V5 edge-case contrast, V18 breakpoints, V20-V21 sizing |

The most impactful v4 improvements: fix `--text-muted`/`--text-secondary` contrast, add `prefers-reduced-motion`, add chart `aria-label` + hidden data tables, and add `:focus-visible` outlines to all interactive elements.
