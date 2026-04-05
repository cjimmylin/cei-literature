# NormEval Dashboard v3 -- Session 15 Handoff

**Date:** 2026-04-05
**Session:** Feature reference table + composite scoring equation + v3 deployment
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260405d-normeval-session14-handoff.md`

---

## What Was Done This Session

### Feature Reference Table (Tab 3: Feature Matrix)

Added a comprehensive, interactive reference table to the Feature Matrix tab, below the existing heatmap. The table documents all 41 features (26 v1 + 15 v2) across 5 axes with the following columns:

- **ID** (color-coded by axis: A1-A13, B1-B12, C1-C5, D1-D6, E1-E5)
- **Feature Name**
- **Axis** (badge: Normative Depth, Practical Ease, Community Impact, Metadata, Empirical Quality)
- **Scale** (encoding scheme)
- **Description** (full definition with scoring anchors)
- **Composite Weight** (percentage for the 16 features that enter the formula; "—" for others)
- **Corpus Distribution** (key statistic about how the 54 benchmarks distribute)
- **Version** (v1 or v2 badge)

Three interactive filters: axis dropdown, version dropdown, and composite-only checkbox. Live counter shows "Showing X of 41 features."

**12-member council expert analysis** added below the table covering 6 perspectives: psychometrics, philosophy of science, ML evaluation, normative ethics, information science, and cross-cultural ethics. Key themes: why 44 features, the five axes' audiences, which features dominate the composite, and what the corpus distributions reveal about the field's blind spots.

### Composite Scoring Equation (Tab 5: Composite Scoring)

Added a styled equation section at the top of the Composite Scoring tab with two side-by-side panels:

**Left panel (Scoring Equation Box):**
- Main formula: `Composite = ND × 0.40 + PE × 0.35 + CI × 0.25`
- Sub-axis formulas for ND, PE, and CI with individual feature weights
- Hard gates section: ND ≥ 40 and data publicly available (B3 ≥ 50)

**Right panel (Design Rationale Box):**
- Why ND is weighted highest (40%) — philosophical rigor as primary differentiator
- Why PE is weighted second (35%) — usability as prerequisite for real-world impact
- Why CI is weighted lowest (25%) — recency and venue bias mitigation
- Why hard gates instead of soft thresholds — empirical support from sensitivity analysis

**12-member council expert analysis** covering decision science, educational measurement, biostatistics, and philosophy of science perspectives. Key themes: weights encode value judgments, within-axis construct priorities, empirical gate support, and why v2 features are excluded from the composite.

### Dashboard v3 Deployment

Created new public GitHub repository `cjimmylin/cei-normeval-dashboard-v3` and deployed via GitHub Pages. All previous versions remain live:

| Version | URL | Content |
|---------|-----|---------|
| v1 | cjimmylin.github.io/cei-normeval-dashboard/ | Original dashboard |
| v2 | cjimmylin.github.io/cei-normeval-dashboard-v2/ | UX council review |
| **v3** | **cjimmylin.github.io/cei-normeval-dashboard-v3/** | Feature table + scoring equation |

### Implementation Details

- **data.js**: Added `DATA_FEATURE_DEFINITIONS` constant (41 objects with 11 fields each)
- **app.js**: Added `renderFeatureRefTable()` with filter/render logic (90 lines)
- **style.css**: Added `.feature-ref-table`, `.axis-badge`, `.version-badge`, `.scoring-equation-box`, `.rationale-item` styles + print media queries (180 lines)
- **index.html**: Added feature table HTML structure with filters; scoring equation section with two-column layout; two new council expert analyses

---

## Remaining Work

### Priority 1: LaTeX conversion
NeurIPS 2026 template or target journal format. Markdown is ready; needs typesetting.

### Priority 2: Cross-reference audit
Automated check that every `Figure N` / `Table N` / `Section N.N` in text has a corresponding file/section.

### Priority 3: Temperature sensitivity test
Gemini models at non-zero temperature to disambiguate shared infrastructure vs. deterministic decoding.

### Priority 4: Feature count reconciliation
Dashboard subtitle claims "46 features (26 v1 + 20 v2)" but Appendix I defines 15 v2 features (A9-A13, B10-B12, D5-D6, E1-E5) for a total of 41. The 5-feature discrepancy should be investigated and the subtitle corrected if needed.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v3 (local) | `DASHBOARD-v2/` | Source files with v3 changes |
| Dashboard v3 (live) | `cjimmylin.github.io/cei-normeval-dashboard-v3/` | Deployed dashboard |
| Feature definitions | `DASHBOARD-v2/data.js` (line ~7570) | `DATA_FEATURE_DEFINITIONS` constant |
| Feature table renderer | `DASHBOARD-v2/app.js` (line ~871) | `renderFeatureRefTable()` function |
| Feature table CSS | `DASHBOARD-v2/style.css` (line ~631) | Styles for table, badges, equation |
| Previous handoff | `METHODS/20260405d-normeval-session14-handoff.md` | Session 14 |

## Known Issues

1. **Playwright browser context dead** — Could not visually verify via Playwright in this session (browser context closed and unrecoverable). Structural validation (div balance, JS syntax, data integrity) all passed. Manual browser check recommended.
2. **Feature count 41 vs 44/46** — The paper appendix defines 41 features (26 v1 + 15 v2) but the dashboard subtitle says 46 and the appendix introduction says 44. Needs reconciliation.

---

*Filed: 2026-04-05 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
