# Methods: Feature Count Reconciliation

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The primary data source was the `DATA_FEATURE_DEFINITIONS` constant in `DASHBOARD-v2/data.js`, which serves as the single machine-verifiable source of truth for all feature metadata. Each of the 41 feature objects contains 11 fields: `id`, `name`, `axis`, `axisLabel`, `scale`, `type`, `description`, `compositeWeight`, `inComposite`, `distribution`, and `version`.

Secondary sources included all files under `NORM-ETHICS/` containing feature count references: two dashboard directories (`DASHBOARD/`, `DASHBOARD-v2/`), two paper directories (`PAPER/`, `PAPER-v2/`), and session documentation under `METHODS/` and `STATISTICS/`.

## Procedure

1. **Ground truth enumeration.** All 41 feature objects in `DATA_FEATURE_DEFINITIONS` were read and categorized by version tag. The verified distribution was:
   - v1 (26 features): A1-A8 (Normative Depth, 8), B1-B9 (Practical Ease, 9), C1-C5 (Community Impact, 5), D1-D4 (Metadata, 4)
   - v2 (15 features): A9-A13 (5), B10-B12 (3), D5-D6 (2), E1-E5 (Empirical Quality, 5)

2. **Discrepancy identification.** A comprehensive search across all `NORM-ETHICS/` files was conducted using regex patterns matching feature count variants (41, 44, 46) and version split variants (15, 18, 20 v2). Each match was classified as either (a) a feature count error requiring correction, (b) a non-feature reference using the same number (e.g., "44/114 items" referring to trial items at ceiling), or (c) a historical session document exempt from modification.

3. **Root cause analysis.** The discrepancy originated in Appendix I, Section I.1, which enumerated the original v1 axes as "Citation Impact (C1-C4)" — omitting C5 (Leaderboard Presence), which is also a v1 feature. This made v1 appear as 25 features, leading to the claim that 18 new v2 features brought the total to 44. The dashboard subtitle's "46 (26 v1 + 20 v2)" represented an even earlier planning-phase count, likely from before some proposed v2 features were dropped.

4. **Correction.** 16 edits were applied across 7 living documents (3 dashboard v2 files, 3 dashboard v1 files, 1 paper appendix, 1 methods document). All edits were verified against the ground truth of 41 features (26 v1 + 15 v2). Historical session documents (date-prefixed files under `METHODS/` and `STATISTICS/`) were not modified per the project's report immutability rule.

5. **Verification.** A post-correction search confirmed that no stale feature counts remain in any living documents. All remaining matches of "44 features" or "18 v2" appear exclusively in historical session documentation.

## Limitations and Decisions

- **Historical documents preserved.** Six session documents under `METHODS/` and two under `STATISTICS/` still contain the old counts (44, 46, 18, 20). These were intentionally left unmodified as they represent historical snapshots of what was believed at each session. The correction is documented in this methods file and the session 16 handoff.

- **Deployed dashboards not updated.** The three GitHub Pages deployments (v1, v2, v3) were not redeployed as part of this session. The local source files are corrected; redeployment requires pushing to each deployment repository.

- **Supplementary figures.** If Figures S1 and S2 (referenced in Appendix I) exist as pre-generated images with "18 v2 features" labels, they would need regeneration. This was not verified in this session.
