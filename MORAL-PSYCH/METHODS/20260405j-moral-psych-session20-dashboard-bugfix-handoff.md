# Moral Psychology Benchmarks — Session 20 Dashboard Bug Fix Handoff

**Date:** 2026-04-05
**Session:** 20 (continued) — Dashboard v4 Bug Fixes
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`
**Previous handoff:** `METHODS/20260405i-moral-psych-session20-handoff.md`

---

## What Was Done This Session

### Dashboard v4 Bug Fixes (3 commits)

After the initial v4 dashboard deployment, three bugs were identified and fixed:

1. **Missing `charts.js` script tag** (commit `395c026`): The `index.html` loaded `data.js` and `app.js` but never included `<script src="charts.js">`. All 30+ chart functions were undefined, causing every ECharts container to render empty. The overview appeared to load but all charts were blank.

2. **Bootstrap pill vs tab selector mismatch** (commit `fe61f95`): The HTML used `data-bs-toggle="pill"` (Bootstrap pills navigation) but `setupTabs()` in app.js queried only for `data-bs-toggle="tab"`. Tab show events never fired, so charts on non-overview tabs were never initialized. Only the overview tab worked because it was explicitly initialized in `init()`. Fix: query for both selectors.

3. **6 uninitialized chart containers** (commit `0fc631e`): The HTML agent added extra chart containers (`chart-feature-weights`, `chart-validity-theory`, `chart-theory-heatmap`, `chart-cultural-breakdown`, `chart-convergence-mini`, `chart-cultural-mini`) that the JS agent didn't wire in the `tabCharts` lifecycle. Fix: added all 6 to their respective tab handlers.

4. **Hidden Gems layout overflow** (commit `761b46c`): The Hidden Gems container was inside a `col-lg-4` sidebar with 8 gem cards using `col-md-4 col-lg-3` grid — creating an extremely narrow, tall stack. Fix: replaced grid cards with a compact list layout (score badge + truncated title + metadata per row).

5. **Init try-catch** (commit `9d9ac21`): Wrapped the entire `init()` body in try-catch so the loading splash always hides even if a render function throws. Errors logged to console for debugging.

### Root Cause Pattern

All bugs stem from **parallel agent divergence** — the HTML, JS, and CSS agents worked from the same spec but made independent decisions:
- HTML agent chose Bootstrap pills (visual), JS agent assumed tabs (semantic)
- HTML agent added extra chart containers, JS agent only wired the ones in the plan
- HTML agent placed gems in a narrow sidebar, JS agent rendered them as wide grid cards

---

## Remaining Work

### Priority 1: Visual QA (Playwright Dead This Session)
Playwright browser context was completely stale — all navigate/run_code calls failed with "Target page, context or browser has been closed." Manual browser testing needed for:
- All 10 tabs rendering charts correctly
- Dark/light theme toggle
- Guided narrative tour scroll behavior
- Claim card → tab navigation
- Ranking table filters
- Feature matrix heatmap

### Priority 2: Additional Empty Charts
Some chart containers may still render empty if their chart functions fail silently (e.g., missing data keys, wrong data structure). Check browser console (F12) for `[MPBench v4] Init error:` messages and any uncaught ECharts errors on each tab.

### Priority 3: Combined Manuscript PDF
`PAPER-v4/scripts/build_combined_pdf.py` not yet written — need to combine all 9 section markdowns + 4 supplementary into a single PDF.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v4 | `DASHBOARDS/moral-psych-benchmarks-v4/` | All dashboard files |
| Dashboard v4 live | `cjimmylin.github.io/cei-moral-psych-dashboard-v4/` | GitHub Pages |
| Dashboard v4 repo | `github.com/cjimmylin/cei-moral-psych-dashboard-v4` | Deployment repo |

## Known Issues

1. **Playwright dead** — cannot do automated visual QA. Restart Claude Code session or clear Chrome profiles to restore.
2. **Some chart containers may still be empty** — depends on whether chart functions in charts.js match the data.js structure exactly. Only browser console can confirm.
3. **`data.js` aiDisclosure** still contains "expert panel" text — fixed in app.js fallback but data.js source unchanged.
4. **Hidden Gems titles still long** — truncated to 50 chars with hover for full title, but some titles may still wrap awkwardly.

---

*Filed: 2026-04-05 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
