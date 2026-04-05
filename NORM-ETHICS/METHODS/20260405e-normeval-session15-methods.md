# Methods: NormEval Dashboard v3 — Feature Reference Table and Composite Scoring Display

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The feature definitions were extracted from two authoritative sources within the NormEval project:

1. **Appendix A: Complete Feature Matrix** (`PAPER-v2/supplement/appendix-A-feature-matrix.md`) — defines 26 v1 features across 4 axes (Normative Depth A1-A8, Practical Ease B1-B9, Citation Impact C1-C5, Metadata D1-D4), including encoding schemes, calibration anchors, and the complete 54-benchmark scoring matrix.

2. **Appendix I: V2 Feature Expansion** (`PAPER-v2/supplement/appendix-I-v2-features.md`) — defines 15 v2 features across 3 extended axes and 1 new axis (Extended Normative Depth A9-A13, Extended Practical Ease B10-B12, Extended Metadata D5-D6, Empirical Quality E1-E5), including distributional summaries and scoring anchors.

The composite scoring formula and its component weights were drawn from Section 3.3 of the paper and the existing dashboard's `DATA_COMPOSITE_SCORING` constant.

The dashboard codebase (v2, `DASHBOARD-v2/`) provided the implementation baseline: `data.js` (7,566 lines, pre-computed analytics), `app.js` (table rendering, tab switching), `charts.js` (ECharts visualization), `style.css` (dark theme), and `index.html` (10-tab structure).

## Procedure

### Feature Reference Table Design

A simulated 12-member expert council was convened to design the feature reference table. The council comprised perspectives from psychometrics, philosophy of science, ML evaluation, normative ethics, information science, and cross-cultural ethics. The design process proceeded as follows:

1. **Feature catalog compilation.** All 41 features were catalogued from Appendices A and I with their IDs, names, axis memberships, scale types, encoding schemes, composite weights (where applicable), and corpus distribution summaries.

2. **Column selection.** The council recommended 8 columns: ID, Feature Name, Axis, Scale, Description, Composite Weight, Corpus Distribution, and Version. The rationale was that users need to (a) identify features by their paper codes, (b) understand what each feature measures, (c) know how it enters the composite formula, and (d) see the empirical distribution across the 54-benchmark corpus.

3. **Interactive filter design.** Three filters were implemented: axis dropdown (5 axes), version dropdown (v1/v2), and composite-only checkbox. These support three primary use cases: exploring features by axis (for researchers working on a specific dimension), comparing v1 vs v2 features (for understanding the expansion), and identifying composite-contributing features (for understanding the ranking formula).

4. **Expert analysis composition.** The 12-member council produced analysis covering: (a) why 44 features are needed (design-vs-performance gap), (b) which audiences each axis serves, (c) which features dominate the composite, and (d) what the distributions reveal about the field's blind spots.

### Composite Scoring Equation Display

1. **Formula extraction.** The composite scoring formula and sub-axis weight formulas were extracted from the paper and verified against the `DATA_COMPOSITE_SCORING` computation in `data.js`.

2. **Two-panel layout design.** The equation section was designed as a two-column layout: left panel shows the mathematical formulas and gate conditions; right panel explains the design rationale for each weight choice. The rationale was structured as four items corresponding to the three axis weights and the gate mechanism.

3. **Council expert analysis.** A separate 12-member council addressed: (a) the value judgment embedded in weight choices, (b) within-axis construct priorities, (c) empirical support for the gate mechanism, and (d) the deliberate exclusion of v2 features from the composite to avoid circular dependency.

### Implementation

All changes were made to the existing v2 dashboard source files:

- `data.js`: Appended `DATA_FEATURE_DEFINITIONS` constant (41 objects, 11 fields each) after the existing `DATA_MAHALANOBIS` constant.
- `app.js`: Added `renderFeatureRefTable()` function with DOM rendering, filter event listeners, and summary counter. Called on `DOMContentLoaded`.
- `style.css`: Added CSS classes for `.feature-ref-table`, `.axis-badge` (5 axis colors), `.version-badge` (v1/v2), `.scoring-equation-box`, `.equation-main`, `.equation-sub`, `.equation-gates`, `.rationale-item`, and corresponding print media overrides.
- `index.html`: Inserted feature table structure between the heatmap and existing expert analysis in Tab 3; inserted scoring equation section before the scatter/sensitivity charts in Tab 5.

### Deployment

The dashboard was deployed as a new version (v3) to preserve all previous versions:

1. Created public repository `cjimmylin/cei-normeval-dashboard-v3` via GitHub CLI.
2. Copied all dashboard files (HTML, CSS, JS, fonts) to a temporary directory.
3. Committed and pushed to `main` branch.
4. Enabled GitHub Pages via the GitHub API (`source.branch=main`, `source.path=/`).

## Analysis

No new statistical analysis was performed in this session. The feature definitions, composite weights, and distributional summaries were drawn from pre-existing data in the paper appendices and the dashboard's pre-computed `data.js`.

Structural validation was performed:
- **Data integrity:** Node.js script verified all 41 feature objects contain all 11 required fields (0 validation errors), correct axis distribution (ND: 13, PE: 12, CI: 5, META: 6, EQ: 5), and correct version distribution (v1: 26, v2: 15).
- **JavaScript syntax:** `app.js` parsed without errors via Node.js syntax validation.
- **HTML balance:** 196 opening `<div>` tags matched 196 closing `</div>` tags; all 10 tab panes properly closed.
- **Cross-reference integrity:** All HTML element IDs referenced in JS (`feature-ref-tbody`, `filter-feature-axis`, etc.) confirmed present; all CSS classes referenced in HTML confirmed defined.

## Computational Environment

- **JavaScript runtime:** Node.js v24.13.1 (for validation only)
- **Dashboard tech stack:** ECharts 5, Bootstrap 5.3, self-hosted Inter + JetBrains Mono fonts
- **Deployment:** GitHub Pages (static files, no build step)
- **Python HTTP server:** Used for local testing (port 8766)
- **Playwright:** Attempted for visual verification but browser context was closed (structural validation used as fallback)

## Limitations and Decisions

1. **Feature count discrepancy.** The paper's Appendix I introduction states "18 new features" but only defines 15 (A9-A13, B10-B12, D5-D6, E1-E5). The dashboard subtitle claims "46 features (26 v1 + 20 v2)." The feature table faithfully represents the 41 features that are actually defined and documented. The discrepancy requires investigation.

2. **No visual verification.** Playwright's browser context was unrecoverable in this session. All validation was structural (syntax, DOM balance, data integrity). Manual browser verification is recommended before citing specific visual elements.

3. **Static vs. dynamic rendering.** The feature definitions are documentation, not computed data. A hardcoded HTML table would have been simpler but would duplicate information and resist filtering. The JS-rendered approach from a data constant maintains the dashboard's "fat data, thin client" architecture while enabling interactivity.

4. **Version isolation via separate repos.** Each dashboard version gets its own repository rather than using branches or subdirectories within a single repo. This ensures previous versions remain permanently accessible at stable URLs for academic citation.
