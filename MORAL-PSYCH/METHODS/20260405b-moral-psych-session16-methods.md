# Methods: Dashboard v2 Bug Fix Implementation

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/MORAL-PSYCH/DASHBOARDS/moral-psych-benchmarks-v2/`

## Data and Materials

The dashboard is a self-contained static site (HTML + CSS + JavaScript) serving pre-computed data from `data.js` (3.57 MB). Charts are rendered using ECharts 5 with Bootstrap 5.3 for layout. The dashboard presents a meta-evaluation of 292 moral psychology benchmarks across 9 large language models from 3 vendors (Anthropic, Google, OpenAI).

## Procedure

### Theme Re-render (Fix 1)

ECharts does not support live theme switching on instantiated chart objects. The existing approach disposed and re-created charts on the active tab when the theme toggled, but left inactive tabs stale — they would render with the previous theme's colors until the user navigated away and back.

A version-counter pattern was introduced:

1. A monotonic `_version` counter on the `ThemeManager` object increments on each theme toggle.
2. A `_paneVersions` map records which `_version` each tab pane was last rendered at.
3. On `shown.bs.tab` events, the existing `initCharts(paneId)` function (which already disposes and re-creates charts) was augmented with a version comparison. If the pane's recorded version differs from the current `_version`, `_syncThemeConstants()` is called to update module-level color constants (`DARK_TEXT`, `GRID_LINE`) before chart factory functions execute.
4. After chart creation, the pane's version is recorded.

This ensures all tabs eventually pick up the correct theme on first show, without the cost of pre-rendering hidden tabs.

### Print Modes (Fix 2)

A print button dropdown was added to the navbar with two modes:

- **Current Tab mode:** JavaScript adds a `.print-target` class to the active `.tab-pane` element and sets `body[data-print-mode="current"]`. A CSS rule `body[data-print-mode="current"] .tab-pane:not(.print-target) { display: none !important; }` hides all non-targeted tabs.
- **All Tabs mode:** Sets `body[data-print-mode="all"]`, which defers to existing print CSS rules that show all panes with `page-break-before: always` between them.

Both modes set `body.dataset.printDate` to the current locale date string before calling `window.print()`. A `window.afterprint` event listener removes all temporary attributes and classes.

An `@page { margin: 1.5cm; }` rule was added for consistent print margins across browsers.

### Data Transparency Callouts (Fixes 3–4)

Two reusable CSS classes were created (`.data-callout-warning`, `.data-callout-info`) with theme-aware backgrounds and colored left borders (amber for warnings, blue for informational), respecting both dark and light themes.

- **Gemini provenance callout:** A static HTML `div` was added at the top of the Cross-Vendor Analysis tab (Tab 12), explaining that 21 of 23 Gemini benchmarks reflect Opus values rather than independently administered trials. The callout references the existing "Cloned" badges in the trial table.
- **Opus-only callout:** A dynamically generated `div` was inserted into the Benchmark Scores tab (Tab 5) above the MFQ-30 Radar and Moral Machine charts, explaining that these benchmarks produce rich multi-dimensional outputs that were only collected for the initial Opus trial.

## Computational Environment

- Static site: no build step, no server-side processing
- ECharts 5 (CDN), Bootstrap 5.3 (CDN), Inter font (Google Fonts)
- Deployment: GitHub Pages from `main` branch root
- Effective transfer size: ~800KB (gzip-compressed 3.57MB data.js)

## Limitations and Decisions

1. **Version counter vs. full re-render:** Pre-rendering all tabs on theme toggle was rejected as wasteful — with 12 tabs, this would create and destroy ~30 ECharts instances unnecessarily. The lazy version-check approach defers re-rendering to the moment of actual tab visibility.
2. **Print dialog vs. dropdown:** A modal with per-tab checkboxes was considered but rejected in favor of the simpler two-option dropdown, which covers the dominant use cases (print what I see, or print everything).
3. **Callouts vs. data fixes:** The data transparency callouts document known scope boundaries rather than attempting to fix them (which would require running actual Gemini API trials). This was a deliberate UX decision — transparency about limitations is preferred to incomplete data.
