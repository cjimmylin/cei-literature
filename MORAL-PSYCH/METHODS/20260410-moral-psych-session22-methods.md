# Methods: Dashboard Layout Audit and Fix

**Date:** 2026-04-10
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`

## Data and Materials

- Dashboard v4 source files: `DASHBOARDS/moral-psych-benchmarks-v4/` (index.html, app.js, charts.js, data.js, style.css)
- Bootstrap 5.3.3 CSS framework (CDN-loaded)
- ECharts 5.5.0 charting library (CDN-loaded)

## Procedure

A systematic code-level audit was conducted on all 10 dashboard tabs to identify containers where JavaScript-rendered card elements used Bootstrap column classes (`col-md-6`, `col-lg-4`) but the parent container lacked the required `row` class.

1. **Enumerated all JS-populated containers** in `index.html` by searching for container IDs referenced in `app.js` render functions.

2. **Cross-referenced each container's HTML class list** against its corresponding `app.js` renderer to determine whether the renderer creates `col-*` children.

3. **Classified containers** into three categories:
   - Grid containers (require `row` class): those whose JS renderers create `col-*` wrapper divs
   - Accordion containers: use Bootstrap accordion pattern, vertical by design
   - Metric-block containers: use custom `.metric-block` CSS class, not Bootstrap grid

4. **Applied fix** to all three grid containers missing the `row g-3` class. The `g-3` gutter utility provides 1rem spacing in both axes via CSS `gap`.

5. **Deployed** the updated `index.html` to the GitHub Pages repository via `gh repo clone`, file copy, commit, and push.

## Analysis

No statistical analysis was performed. The audit was a binary classification of 15 JS-populated containers into "needs row class" vs "does not need row class" based on the column class patterns in their respective renderer functions.

## Computational Environment

- macOS Darwin 25.3.0
- Python 3.x HTTP server for local preview (`python3 -m http.server 8765`)
- GitHub CLI (`gh`) for repo cloning and verification
- Playwright MCP plugin (non-functional this session due to stale browser context)

## Limitations and Decisions

- Visual verification was not possible via Playwright due to a stuck browser context. The fix was verified by code inspection only — confirming that Bootstrap's `row` class enables `display: flex; flex-wrap: wrap` which activates `col-*` responsive breakpoints.
- The audit covered only containers populated by `app.js`. Static HTML sections (chart rows with `row g-4`) were already correct and not re-audited.
