# Methods: NormEval Dashboard v2 UX Council Review and Implementation

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The NormEval dashboard (v1, 10 tabs) served as the baseline for review. Full-page screenshots of all 10 tabs were captured using Playwright's bundled Chromium at 2x device scale factor (2880x1800 effective resolution). The CSS design system (style.css, 405 lines), JavaScript rendering logic (app.js, 827 lines; charts.js, 1034 lines), HTML structure (index.html, 721 lines), and pre-computed data constants (data.js, 177KB; data_cross_vendor.js, 10KB) were analyzed.

## Procedure

### Phase 1: Expert Council Assembly

A 12-perspective interdisciplinary review panel was constructed covering: Information Design, Academic Publishing UX, Web Accessibility (WCAG), Data Journalism, Dark-Mode UI Design, Typography and Readability, ECharts/Charting Libraries, Mobile Responsiveness, Cognitive Load (UX Psychology), Scientific Communication, Color Vision Deficiency, and Print/Export. Each perspective reviewed all 10 tab screenshots and the underlying code.

### Phase 2: Issue Identification and Classification

Issues were classified into 6 categories (Layout, Typography, Color, Interactivity, Content, Accessibility) with severity ratings. Each issue received a specific recommendation with implementation guidance. A priority matrix was constructed: P0 (high impact, low effort), P1 (high impact, medium effort), P2 (accessibility compliance), P3 (polish), P4 (low priority).

### Phase 3: Implementation

A new dashboard version was created by copying all v1 files to `DASHBOARD-v2/`, preserving v1 as a frozen baseline. Four parallel implementation streams addressed CSS (12 changes), charts.js (5 changes), app.js (6 changes), and index.html (9 changes). Changes were verified via automated content checks (12/12 passed) and Playwright screenshot comparison.

Key implementation decisions:
- **CSS figure numbering** used CSS counters (`counter-reset` on `.tab-pane`, `counter-increment` on `.chart-container h3::before`) for zero-JavaScript automatic figure numbers.
- **CVD-safe colors** replaced red (#ef5b5b) and green (#4ecb71) with blue (#5b8def) and orange (#f0983e) for the Knowledge vs Judgment chart, ensuring accessibility for the ~8% of males with red-green color blindness.
- **Tab explainer reordering** placed the Key finding/conclusion first (inverted pyramid structure) across all 10 tabs, following data journalism conventions.
- **max-width constraints** (80ch on tab-explainers, 72ch on expert blocks) were initially implemented per council recommendation but subsequently removed in favor of increased horizontal padding, as the max-width approach created visible background gaps in the dark-theme container layout.

### Phase 4: Deployment

Dashboard v2 was deployed to a separate GitHub Pages repository (`cjimmylin/cei-normeval-dashboard-v2`) to preserve v1 as a comparison baseline.

## Analysis

No new statistical analysis was performed. All changes were to the presentation layer. The underlying benchmark data, trial results, and cross-vendor comparison data remained unchanged.

Verification: 12 automated content checks confirmed presence of all new features (skip link, ARIA, tab position, expert class, footnote class, cross-tab links, expand toggle, etc.). Playwright screenshots of all 10 tabs confirmed visual rendering.

## Computational Environment

- macOS Darwin 25.3.0
- Python 3.9, Playwright (bundled Chromium)
- Node.js v24.13.1
- GitHub CLI for repository operations
- ECharts 5.5.1, Bootstrap 5.3.3

## Limitations and Decisions

1. **2 of 28 recommendations skipped:** Column layout consistency (P4, functional as-is) and per-trial table filters (P4, table has only 10 rows).
2. **Print stylesheet limitation:** ECharts canvas-rendered charts cannot be printed. The print stylesheet shows a placeholder message directing readers to the online version.
3. **max-width trade-off:** The council recommended max-width constraints for text readability, but this conflicted with the dark-theme container-fills-width design pattern. Increased padding was used as an alternative.
4. **Separate deployment:** v2 uses a new repo rather than replacing v1, enabling A/B comparison and preserving the original as a baseline.
