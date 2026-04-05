# Cross-Vendor Dashboard Review — Expert Council

**Date:** 2026-04-04
**Scope:** Tab 12 (Cross-Vendor Analysis) of Moral Psychology Benchmarks Meta-Evaluation Dashboard
**Council:** 12 members | **Benchmarks reviewed:** 23 | **Models:** 9 (3 vendors)

## Summary Assessment

The Cross-Vendor Analysis tab successfully presents the most important finding of the multi-model benchmark study: cross-vendor moral homogeneity. The 6 KPI cards, 6 ECharts visualizations, council highlights, 8-item conclusions accordion, and 23x9 trial comparison table form a coherent analytical narrative. Expert annotations below each chart provide accessible interpretation.

However, the council identified 12 specific issues affecting readability, statistical rigor, and visual clarity. Of these, 10 have been implemented (R1-R6, R8, R9, R10, R12) and 2 are deferred as future enhancements requiring new data (R7, R11).

---

## Recommendations

### R1: Radar Chart Overplotting [IMPLEMENTED]
**Proposed by:** Dr. Okafor (#2, Moral Philosophy)
**Problem:** 9 overlapping polygons with minimal differentiation made the radar unreadable.
**Fix:** Line width coded by model size (3px flagship, 1.5px smallest), dashed lines for smaller models, hover emphasis (width 4 + opacity 0.15), "Click legend to toggle" instruction, enhanced tooltip showing all 8 dimension values.

### R2: Scale Sensitivity X-Axis Misalignment [IMPLEMENTED]
**Proposed by:** Dr. Ruiz (#11, Developmental Psychology)
**Problem:** Gemini's 4-point x-axis applied to all vendors. Anthropic (3 models) and OpenAI (2 models) data was misaligned with trailing zeros.
**Fix:** 3-grid layout — each vendor gets its own correctly-sized x-axis with vendor name as colored axis title.

### R3: Convergence Scatter Origin Clustering [IMPLEMENTED]
**Proposed by:** Dr. Krishnamurthy (#8, Statistics)
**Problem:** ~6 ceiling benchmarks at (0,0) created an unreadable blob at the origin.
**Fix:** 2-series split — "Discriminating" (blue, large symbols) vs "Ceiling (zero var.)" (gray, small symbols) with distinct label styling.

### R4: Discrimination Bar Ceiling Labels [IMPLEMENTED]
**Proposed by:** Dr. Chen (#1, Psychometrics)
**Problem:** Zero-CV bars were invisible against the dark background (#444 on #0f0f1a).
**Fix:** "CEILING" text label on zero-CV bars. Red dashed markLine at CV=0.05 threshold labeled "High discrimination."

### R5: Convergence Scatter Diagonal Reference [IMPLEMENTED]
**Proposed by:** Dr. Krishnamurthy (#8, Statistics)
**Problem:** Without a y=x reference line, readers cannot determine whether between-vendor or within-vendor variance dominates for each benchmark.
**Fix:** Added dashed diagonal line (y=x) from origin to max variance. Points above the line = between-vendor dominance; below = within-vendor dominance.

### R6: Trial Table Conditional Formatting [IMPLEMENTED]
**Proposed by:** Dr. Chen (#1, Psychometrics)
**Problem:** 207 cells of numbers with no visual hierarchy. Ceiling rows indistinguishable from informative rows.
**Fix:** Ceiling rows (all 9 values identical) dimmed to 45% opacity with warning indicator. Max values bolded, min values italicized with reduced opacity.

### R7: Heatmap 9-Model Granularity [DEFERRED]
**Proposed by:** Dr. Volkov (#9, AI Industry)
**Problem:** Vendor-averaged heatmap (3 columns) loses per-model granularity.
**Status:** Deferred — requires dashboard redesign for 9-column heatmap with adequate label space. The 23x9 trial table serves this purpose for now.

### R8: KPI Fraction Context [IMPLEMENTED]
**Proposed by:** Dr. Al-Rashid (#5, Computational Linguistics)
**Problem:** "6" without denominator is ambiguous — 6 of what?
**Fix:** KPI cards now show "6/23" (Ceiling Benchmarks) and "17/23" (Discriminating) with fraction format.

### R9: Theory Coverage Variance Indicators [IMPLEMENTED]
**Proposed by:** Dr. Watanabe (#4, Cross-Cultural Psychology)
**Problem:** Grouped bars show vendor means but not spread. Cannot tell if bars represent consensus or outlier-driven averages.
**Fix:** Enhanced tooltip formatter shows all 3 vendor values plus computed range with qualitative labels ("homogeneous" < 0.01, "low spread" < 0.1, "notable spread" >= 0.1).

### R10: Accordion Inline Styles [IMPLEMENTED]
**Proposed by:** Dr. Chen (#1, Psychometrics)
**Problem:** Conclusions accordion used inline JavaScript styles creating maintenance burden and inconsistency risk.
**Fix:** Replaced inline styles with `.cv-accordion-item` and `.cv-accordion-btn` CSS classes in style.css. Accordion arrow filter adjusted for dark theme.

### R11: Human Baseline References [DEFERRED]
**Proposed by:** Dr. Ruiz (#11, Developmental Psychology)
**Problem:** No human population norms shown for comparison on any chart. Without human baselines, it's impossible to assess whether model profiles are "normal" or aberrant.
**Status:** Deferred — requires curating population norms from original benchmark publications (MFQ-30 human means, DIT population P-scores, etc.). High-value future enhancement.

### R12: Mobile Tab Scrolling [IMPLEMENTED]
**Proposed by:** Dr. Al-Rashid (#5, Computational Linguistics)
**Problem:** 12 tab buttons overflow on mobile screens (<768px) without horizontal scrolling.
**Fix:** Added CSS media query: `.nav-tabs { overflow-x: auto; flex-wrap: nowrap; }` with touch-friendly scrolling for mobile devices.

---

## Implementation Summary

| # | Recommendation | Status | Files Changed |
|---|---------------|--------|---------------|
| R1 | Radar overplotting | Implemented | charts.js |
| R2 | Scale x-axis misalignment | Implemented | charts.js |
| R3 | Convergence origin clustering | Implemented | charts.js |
| R4 | Discrimination ceiling labels | Implemented | charts.js |
| R5 | Convergence diagonal reference | Implemented | charts.js |
| R6 | Trial table conditional formatting | Implemented | app.js, style.css |
| R7 | Heatmap 9-model granularity | Deferred | — |
| R8 | KPI fraction context | Implemented | app.js |
| R9 | Theory coverage variance | Implemented | charts.js |
| R10 | Accordion CSS classes | Implemented | app.js, style.css |
| R11 | Human baseline references | Deferred | — |
| R12 | Mobile tab scrolling | Implemented | style.css |

**10/12 recommendations implemented. 2 deferred as future enhancements.**
