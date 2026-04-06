# Methods: Dashboard v4 Parallel-Agent Bug Resolution

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`

## Data and Materials

The dashboard v4 consists of 7 source files: `generate_dashboard.py` (generator), `_tab_annotations.py` (annotations), `index.html` (structure), `style.css` (styling), `app.js` (rendering), `charts.js` (ECharts), and `data.js` (pre-computed output). These were produced by 5 parallel agents in 2 phases.

## Procedure

### Bug Detection

Dashboard v4 exhibited three symptoms after deployment:
1. Infinite loading splash (splash never hidden)
2. All chart containers empty across all tabs
3. Hidden Gems rendered as narrow stacked cards in sidebar

### Diagnostic Process

Since Playwright browser automation was unavailable (stale browser context), diagnosis proceeded through static code analysis:

1. **Splash persistence**: Identified that `init()` ran ~20 render functions before the splash-hide line. Any uncaught exception would prevent execution from reaching `splash.classList.add('hidden')`. Fix: wrapped init body in try-catch, moved splash-hide outside the try block.

2. **Empty charts**: Cross-referenced script loading order in `index.html` — discovered `charts.js` was never loaded. Only `data.js` and `app.js` were included as `<script>` tags. All `chartXxx()` functions were undefined.

3. **Tab-specific chart failure**: After adding `charts.js`, overview charts rendered but other tabs remained empty. Identified that `setupTabs()` queried `[data-bs-toggle="tab"]` but HTML used `data-bs-toggle="pill"` (Bootstrap pills navigation). Selector mismatch meant tab show events never fired.

4. **Uninitialized containers**: Systematic cross-reference of HTML `id="chart-*"` attributes against `app.js` `getElementById('chart-*')` calls revealed 6 containers in HTML with no initialization code. The HTML agent added these containers independently of the JS agent.

5. **Hidden Gems overflow**: The container was inside `col-lg-4` (33% width) but rendered 8 cards using `col-md-4 col-lg-3` grid — each card occupied the full narrow column width, creating a very tall stack with long titles.

### Verification Approach

Each fix was verified through:
- `node -c app.js` (syntax validation)
- Python cross-reference scripts comparing HTML IDs against JS references
- DATA key existence checks (all 41 referenced DATA.xxx keys confirmed in data.js)
- Chart function cross-reference (all chart functions called in app.js confirmed defined in charts.js)

## Analysis

### Parallel Agent Divergence Pattern

The root cause of all bugs was **contract mismatch between independently-written files**:

| Mismatch | HTML Agent | JS Agent | Fix |
|----------|-----------|----------|-----|
| Script loading | Wrote `charts.js` | Expected it loaded | Added `<script>` tag |
| Tab toggle | Used `data-bs-toggle="pill"` | Queried `data-bs-toggle="tab"` | Query both selectors |
| Chart containers | Added 37 containers | Wired 31 of them | Added missing 6 |
| Gems layout | Placed in `col-lg-4` sidebar | Rendered as wide grid cards | Compact list layout |

This pattern is systemic in parallel agent dashboard construction: agents share a specification but make independent implementation choices at the boundaries.

## Computational Environment

- Node.js for JavaScript syntax checking (`node -c`)
- Python 3.9 for cross-reference analysis scripts
- GitHub Pages for deployment (1-2 min propagation delay)

## Limitations and Decisions

1. **No visual QA possible**: Playwright browser context was dead throughout the debugging session. All fixes were made through static code analysis without seeing the rendered dashboard.
2. **Some chart functions may still fail at runtime**: The cross-reference confirms all function names exist, but runtime data shape mismatches between `data.js` keys and what chart functions expect can only be detected in a browser console.
3. **Compact Hidden Gems trade-off**: Truncating titles to 50 characters loses information. The full title is available on hover (`title` attribute) but may not be discoverable on mobile.
