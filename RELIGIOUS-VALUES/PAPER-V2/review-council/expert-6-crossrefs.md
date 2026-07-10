# Expert 6: Cross-Reference Integrity Verification

**Scope:** All 9 paper files (00-abstract.md through 08-supp-figures.md)
**Date:** 2026-04-12

---

## Summary

- **Total findings:** 9
- **Critical:** 2
- **Major:** 4
- **Minor:** 3

---

## Finding 1
**Location:** 02-results.md:287
**Severity:** MAJOR
**Category:** Figure-Ref
**Issue:** Figure 11 description in the main text does not match the actual figure. The text says "Figure 11 presents the rubric ceiling effect with the T2 discrimination contrast" but Figure 11 is defined as "Cross-Vendor Rubric Heatmap" in 08-supp-figures.md:47. Additionally, the text says "Figure 12 presents the bias--values independence analysis" but Figure 12 is "T2 Accuracy by Model". The actual bias-values figure is Figure S6.
**Recommendation:** Correct the description at 02-results.md:287 to accurately describe Figure 11 as the cross-vendor rubric heatmap, Figure 12 as T2 accuracy by model, and add a separate reference to Figure S6 for bias-values independence. The original text appears to have swapped/conflated the figure descriptions.
**Quote:** "These findings are depicted in Figures 10--12: Figure 10 presents the K $<$ R $<$ V gradient across models and traditions, Figure 11 presents the rubric ceiling effect with the T2 discrimination contrast, and Figure 12 presents the bias--values independence analysis."

## Finding 2
**Location:** 08-supp-figures.md:117 vs 06-supp-results.md:67-68
**Severity:** MAJOR
**Category:** Figure-Ref
**Issue:** Figure S7 description in 08-supp-figures.md reports Haiku Beginner accuracy as 86.7% and Advanced as 66.7%, but Table SR3 in 06-supp-results.md reports Haiku Beginner as 80% and Advanced as 73.3%. Table S8 in 07-supp-tables.md:206 also reports 80%/73.3%, matching the SR3 data. The Figure S7 description contains incorrect Haiku values.
**Recommendation:** Correct Figure S7 data in 08-supp-figures.md to match the canonical values: Haiku Beginner = 80.0%, Advanced = 73.3%. The 86.7%/66.7% values appear to be transposed from Codex-Mini or otherwise erroneous.
**Quote:** "Haiku: Beginner 86.7%, Advanced 66.7%."

## Finding 3
**Location:** 08-supp-figures.md (disk check)
**Severity:** CRITICAL
**Category:** Figure-Ref
**Issue:** Figures 1-9 are described in 08-supp-figures.md as existing at `PAPER/figures/` paths (not `PAPER-V2/figures/`). On disk, Figures 1-9 exist only in `PAPER/figures/`, not in `PAPER-V2/figures/`. The `PAPER-V2/figures/` directory contains only: fig10, fig11, fig12, fig13, fig-s4, fig-s5, fig-s7, fig-s8. This means Figures 1-9 must be copied or symlinked to PAPER-V2/figures/ for the paper to be self-contained, OR the build pipeline must resolve the cross-directory reference.
**Recommendation:** Copy or symlink Figures 1-9 and Figure S1, S3 from `PAPER/figures/` to `PAPER-V2/figures/` so all figures are co-located with the paper source files.
**Quote:** Source paths like "Source: `PAPER/figures/fig1-tradition-heatmap.png`"

## Finding 4
**Location:** 08-supp-figures.md
**Severity:** CRITICAL
**Category:** Figure-Ref
**Issue:** Three figures described in 08-supp-figures.md do not exist on disk anywhere: Figure S2 (Gate Threshold Sensitivity Curves Extended), Figure S6 (Bias-Values Scatter Plots Per Model), and Figure S1/S3 exist only in `PAPER/figures/`. Figure S2 has no corresponding image file in either PAPER/ or PAPER-V2/ figures directories.
**Recommendation:** Generate Figure S2 and Figure S6, or remove their descriptions from the supplementary figures document if they are not needed. Figure S1 (PRISMA) exists at `PAPER/fig-prisma-flow.png` (not in a figures/ subdirectory), so the source path reference is slightly wrong too.
**Quote:** "**Figure S2. Gate Threshold Sensitivity Curves (Extended).**"

## Finding 5
**Location:** 01-methods.md:36
**Severity:** MINOR
**Category:** Section-Ref
**Issue:** Reference to "Section 4" is overly broad. The text says "data inaccessibility is the single largest barrier to reproducibility in this field (Section 4)" but Section 4 spans 373 lines. The specific relevant subsection is Section 4.1 or Section 4.3.
**Recommendation:** Change "Section 4" to "Section 4.1" or "Section 4.3" for precision.
**Quote:** "P3 receives the highest weight in the PE axis because data inaccessibility is the single largest barrier to reproducibility in this field (Section 4)."

## Finding 6
**Location:** 03-discussion.md:113
**Severity:** MAJOR
**Category:** Section-Ref
**Issue:** Reference to "Section 5.6" in a sentence that itself is within Section 5.7. The text says "The structural analysis in Section 5.6 implies..." which is a backward reference within the same file. This is valid but worth verifying: Section 5.6 is "Publication Infrastructure as the Structural Barrier" at line 93, and Section 5.7 is "Closing the Gaps" at line 111. The reference is correct.
**Recommendation:** No action needed -- this is a valid backward reference within the discussion.
**Quote:** "The structural analysis in Section 5.6 implies that no single strategy can address the tradition asymmetry."

## Finding 7
**Location:** 07-supp-tables.md:123
**Severity:** MINOR
**Category:** Section-Ref
**Issue:** The text references "Section 3.4" correctly for meta-evaluation criteria. However, the same section also references "Section 4" broadly when "Section 4.4" or a specific subsection would be more precise: "These criteria were applied to all gate-passing benchmarks and informed the qualitative assessments reported in Section 4."
**Recommendation:** Change to "Section 4" to "Sections 4.1--4.4" or list the specific subsections where qualitative assessments appear.
**Quote:** "informed the qualitative assessments reported in Section 4."

## Finding 8
**Location:** 07-supp-tables.md:3
**Severity:** MINOR
**Category:** Table-Ref
**Issue:** The introductory paragraph of 07-supp-tables.md says "Tables S6--S8 report the full cross-model and cross-vendor implementation trial results" but Table S6 is "Cross-Model Response Length Gradient" and Table S7 is "Cross-Vendor Rubric Scores" and Table S8 is "T2 Arabic MCQ Results." The description is accurate but could be more precise: S6 covers response lengths, S7 covers rubric scores, and S8 covers T2 results.
**Recommendation:** No action strictly needed -- the description is accurate if slightly vague.
**Quote:** "Tables S6--S8 report the full cross-model and cross-vendor implementation trial results."

## Finding 9
**Location:** 06-supp-results.md:230 (SR7)
**Severity:** MAJOR
**Category:** Section-Ref
**Issue:** SR7 text references "Section 4.3" for the tradition asymmetry diagnosis: "the current baseline weighting partially reproduces the infrastructure advantages that the main paper diagnoses (Section 4.3)." However, Section 4.3 is "Tradition Coverage Patterns" which does discuss infrastructure but the primary diagnosis of infrastructure advantages is also in Section 5.6 of the discussion. The reference is technically valid but Section 5.6 would be more precise.
**Recommendation:** Consider adding "Section 5.6" as an additional cross-reference alongside Section 4.3.
**Quote:** "partially reproduces the infrastructure advantages that the main paper diagnoses (Section 4.3)"

---

## Registry A: Section Registry

| Number | Heading Text | File:Line |
|--------|-------------|-----------|
| 3 | Methods | 01-methods.md:1 |
| 3.1 | Benchmark Corpus Assembly | 01-methods.md:5 |
| 3.2 | Feature Matrix Design | 01-methods.md:19 |
| 3.3 | Composite Scoring and Sensitivity Analysis | 01-methods.md:93 |
| 3.4 | Meta-Evaluation Criteria | 01-methods.md:125 |
| 3.5 | Implementation Trial Protocol | 01-methods.md:143 |
| 3.5.1 | Construct Validity Battery (65 Items) | 01-methods.md:147 |
| 3.5.2 | T2 Arabic MCQ Assessment (30 Items) | 01-methods.md:157 |
| 3.5.3 | Rubric Scoring Protocol | 01-methods.md:163 |
| 3.5.4 | Cross-Model Design (3 Claude Models) | 01-methods.md:176 |
| 3.5.5 | Cross-Vendor Extension (9 Models Total) | 01-methods.md:182 |
| 3.5.6 | Methodological Caveats | 01-methods.md:192 |
| 3.6 | Statistical Analysis Plan | 01-methods.md:202 |
| 3.7 | Limitations of the Methodology | 01-methods.md:226 |
| 4 | Results | 02-results.md:1 |
| 4.1 | Landscape Analysis | 02-results.md:5 |
| 4.2 | Tiered Benchmark Ranking | 02-results.md:27 |
| 4.3 | Tradition Coverage Patterns | 02-results.md:87 |
| 4.4 | Claim Robustness Battery | 02-results.md:152 |
| 4.5 | Cross-Model Construct Validity | 02-results.md:207 |
| 4.6 | Cross-Vendor Replication | 02-results.md:289 |
| 5 | Discussion | 03-discussion.md:1 |
| 5.1 | The Tradition Asymmetry Problem | 03-discussion.md:7 |
| 5.2 | Knowledge Testing vs. Values Reasoning | 03-discussion.md:23 |
| 5.3 | The Rubric Ceiling Paradox | 03-discussion.md:37 |
| 5.4 | Cross-Vendor Divergence and Its Implications | 03-discussion.md:55 |
| 5.5 | Values Relevance Failure | 03-discussion.md:75 |
| 5.6 | Publication Infrastructure as the Structural Barrier | 03-discussion.md:93 |
| 5.7 | Closing the Gaps: Differentiated Strategies | 03-discussion.md:111 |
| 5.8 | Methodological Transparency | 03-discussion.md:137 |
| 5.9 | Limitations | 03-discussion.md:157 |
| 6 | Conclusion | 04-conclusion.md:1 |
| S1 | Construct Validity Battery Design | 05-supp-methods.md:5 |
| S1.1 | Battery Composition | 05-supp-methods.md:7 |
| S1.2 | Item Type Specifications | 05-supp-methods.md:17 |
| S1.3 | Scoring Rubrics | 05-supp-methods.md:27 |
| S1.4 | System Prompts | 05-supp-methods.md:70 |
| S2 | T2 Arabic MCQ Sampling Protocol | 05-supp-methods.md:80 |
| S2.1 | Source Dataset | 05-supp-methods.md:82 |
| S2.2 | Sampling Procedure | 05-supp-methods.md:86 |
| S2.3 | Difficulty Calibration | 05-supp-methods.md:97 |
| S2.4 | Scoring | 05-supp-methods.md:103 |
| S3 | Cross-Model Trial Administration | 05-supp-methods.md:107 |
| S3.1 | Platform and Environment | 05-supp-methods.md:109 |
| S3.2 | Models Tested | 05-supp-methods.md:113 |
| S3.3 | Administration Protocol | 05-supp-methods.md:121 |
| S3.4 | JSON Repair Procedure | 05-supp-methods.md:130 |
| S3.5 | Output Files | 05-supp-methods.md:136 |
| S4 | Cross-Vendor Trial Administration | 05-supp-methods.md:148 |
| S4.1 | Additional Models | 05-supp-methods.md:150 |
| S4.2 | OpenAI Administration | 05-supp-methods.md:163 |
| S4.3 | Gemini Backfilled Protocol | 05-supp-methods.md:169 |
| S4.4 | Rubric Scoring Across Vendors | 05-supp-methods.md:181 |
| S4.5 | Data Aggregation | 05-supp-methods.md:189 |
| S5 | Bootstrap Resampling Algorithm | 05-supp-methods.md:195 |
| S5.1 | Weight Configuration Space | 05-supp-methods.md:197 |
| S5.2 | Weight Sensitivity Sweep | 05-supp-methods.md:207 |
| S5.3 | Bootstrap Confidence Intervals | 05-supp-methods.md:218 |
| S5.4 | Observed Robustness Metrics | 05-supp-methods.md:237 |
| S5.5 | Gate Threshold Sensitivity | 05-supp-methods.md:252 |
| S5.6 | Feature Leave-One-Out | 05-supp-methods.md:259 |
| S6 | Statistical Tests Specification | 05-supp-methods.md:268 |
| S6.1-S6.10 | (8 claim tests + correction + environment) | 05-supp-methods.md:272-384 |
| S7 | Response Length Analysis Protocol | 05-supp-methods.md:386 |
| S7.1-S7.4 | (Metric, gradient, V/K, independence) | 05-supp-methods.md:388-414 |
| SR1 | Per-Tradition x Per-Model Response Length Tables | 06-supp-results.md:5 |
| SR2 | Per-Tradition Rubric Score Breakdown | 06-supp-results.md:35 |
| SR3 | T2 Beginner vs. Advanced Per-Model Breakdown | 06-supp-results.md:57 |
| SR4 | Bias-Values Correlation Matrices | 06-supp-results.md:87 |
| SR5 | Void Factor Analysis | 06-supp-results.md:113 |
| SR6 | Feature Leave-One-Out Analysis | 06-supp-results.md:171 |
| SR7 | WEIRD-Neutral Weighting Scenario | 06-supp-results.md:202 |
| SR8 | Sensitivity Analysis Extended Results | 06-supp-results.md:232 |

**Notes:**
- No Section 1 (Introduction) or Section 2 (Background/Literature Review) headings exist in the paper files. The abstract is unnumbered, and the paper starts at Section 3. No references to "Section 1" or "Section 2" were found -- this is correct since the paper appears to have an unnumbered introduction/background that is not in these files, or the paper begins at Section 3.
- All section references found across all files resolve to valid section numbers in the registry.

---

## Registry B: Table Registry

| Number | Title/Description | File:Line | Referenced (Y/N) |
|--------|------------------|-----------|-----------------|
| Table 1 | 3-Axis Scoring Framework (22 features) | 01-methods.md:55 | Y |
| Table 2 | Benchmark tiers with uncertainty quantification | 02-results.md:31 | Y |
| Table 3 | Tradition coverage analysis (14 traditions) | 02-results.md:91 | Y |
| Table 4 | Claim robustness summary | 02-results.md:156 | Y |
| Table 5 | Aggregate response lengths by construct type and model | 02-results.md:215 | Y |
| Table 6 | Per-tradition response lengths by construct type and model | 02-results.md:225 | Y |
| Table 7 | Rubric scores by construct dimension and model | 02-results.md:247 | Y |
| Table 8 | Bias--values correlations by model | 02-results.md:263 | Y |
| Table 9 | T2 Arabic MCQ accuracy by model and difficulty | 02-results.md:277 | Y |
| Table 10 | Cross-vendor implementation trial results | 02-results.md:307 | Y |
| Table 11 | Bias--values correlations by model (all 3 vendors) | 02-results.md:345 | Y |
| Table S1 | Feature Matrix Score Distributions | 07-supp-tables.md:7 | Y (01-methods.md:81) |
| Table S2 | Scoring Formula Coefficients and Calibration | 07-supp-tables.md:24 | N (not explicitly referenced as "Table S2" in main text) |
| Table S3 | Format Taxonomy (12 Codes) | 07-supp-tables.md:72 | Y (01-methods.md:65,85) |
| Table S4 | External Search Results by Tradition Family | 07-supp-tables.md:99 | N (not explicitly referenced as "Table S4" in main text) |
| Table S5 | Meta-Evaluation Criteria | 07-supp-tables.md:122 | Y (01-methods.md:127) |
| Table S6 | Cross-Model Response Length Gradient | 07-supp-tables.md:142 | Y (01-methods.md:123 -- referenced as "Table S6" but actually the text says "Supplementary Materials (Table S6)" for sensitivity analysis, which is a mismatch -- see below) |
| Table S7 | Cross-Vendor Rubric Scores | 07-supp-tables.md:168 | N (not explicitly referenced as "Table S7" in main text) |
| Table S8 | T2 Arabic MCQ Results by Model and Difficulty | 07-supp-tables.md:196 | N (not explicitly referenced as "Table S8" in main text) |
| Table S9 | Claim Robustness Battery (Full Details) | 07-supp-tables.md:224 | N (not explicitly referenced as "Table S9" in main text) |
| Table S10 | Void Factor Analysis (8 Missing Traditions) | 07-supp-tables.md:253 | N (not explicitly referenced as "Table S10" in main text) |

**Note on Table S6 mismatch:** At 01-methods.md:123, the text says "Results of these checks are reported in the Supplementary Materials (Table S6)." However, the sensitivity analysis results are in SR6 (Feature Leave-One-Out) and SR8 (Sensitivity Analysis Extended). Table S6 is "Cross-Model Response Length Gradient" -- a completely different topic. The correct reference should be to SR6/SR8 or Tables SR6/SR8, not Table S6.

---

## Registry C: Figure Registry

### Main Body Figures

| Number | Description | Defined in File:Line | On Disk in PAPER-V2/figures/ (Y/N) | On Disk in PAPER/figures/ (Y/N) | Referenced (Y/N) |
|--------|-------------|---------------------|-------------------------------------|----------------------------------|-----------------|
| Figure 1 | Tradition Coverage Heatmap | 08-supp-figures.md:11 | N | Y (fig1-tradition-heatmap.png) | Y (02-results.md:9,13) |
| Figure 2 | Candidate Distribution by Tradition Family | 08-supp-figures.md:14 | N | Y (fig2-tradition-distribution.png) | Y (02-results.md:13) |
| Figure 3 | RD vs. PE Scatter Plot | 08-supp-figures.md:17 | N | Y (fig3-rd-vs-pe-scatter.png) | Y (02-results.md:23) |
| Figure 4 | Data Availability by Tradition | 08-supp-figures.md:20 | N | Y (fig4-data-availability.png) | Y (02-results.md:15) |
| Figure 5 | Bootstrap CI Forest Plot | 08-supp-figures.md:23 | N | Y (fig5-bootstrap-ci-forest.png) | Y (02-results.md) |
| Figure 6 | Void Factor Radar | 08-supp-figures.md:26 | N | Y (fig6-void-factor-radar.png) | Y |
| Figure 7 | Values Relevance Histogram | 08-supp-figures.md:29 | N | Y (fig7-values-relevance-histogram.png) | Y |
| Figure 8 | Claim Robustness Summary | 08-supp-figures.md:32 | N | Y (fig8-claim-robustness.png) | Y |
| Figure 9 | Gate Threshold Sensitivity | 08-supp-figures.md:35 | N | Y (fig9-gate-threshold-sensitivity.png) | Y (02-results.md) |
| Figure 10 | Cross-Model K<R<V Grouped Bar | 08-supp-figures.md:38 | Y (fig10-cross-model-gradient.png) | N | Y (02-results.md:287) |
| Figure 11 | Cross-Vendor Rubric Heatmap | 08-supp-figures.md:47 | Y (fig11-rubric-heatmap.png) | N | Y (02-results.md:287,305) |
| Figure 12 | T2 Accuracy by Model | 08-supp-figures.md:56 | Y (fig12-t2-accuracy.png) | N | Y (02-results.md:287) |
| Figure 13 | Vendor Capability Radar | 08-supp-figures.md:65 | Y (fig13-vendor-radar.png) | N | Y (02-results.md:305) |

### Supplementary Figures

| Number | Description | Defined in File:Line | On Disk (Y/N) | Referenced (Y/N) |
|--------|-------------|---------------------|---------------|-----------------|
| Figure S1 | PRISMA Flow Diagram | 08-supp-figures.md:80 | Y (PAPER/fig-prisma-flow.png, NOT in figures/ subdir) | Y (01-methods.md:7) |
| Figure S2 | Gate Threshold Sensitivity (Extended) | 08-supp-figures.md:83 | **N -- MISSING** | N (no reference found in main text) |
| Figure S3 | Correlation Heatmap | 08-supp-figures.md:86 | Y (PAPER/figures/fig-s3-correlation-heatmap.png) | N (no reference in main text) |
| Figure S4 | Per-Tradition K<R<V Gradient (9 Small Multiples) | 08-supp-figures.md:89 | Y (PAPER-V2/figures/fig-s4-tradition-gradient.png) | Y (ref in 08-supp-figures.md:96 to SR1) |
| Figure S5 | Cross-Vendor Response Length (Log Scale) | 08-supp-figures.md:98 | Y (PAPER-V2/figures/fig-s5-cross-vendor-length.png) | Y (ref in 08-supp-figures.md:103) |
| Figure S6 | Bias-Values Scatter Plots (Per Model) | 08-supp-figures.md:105 | **N -- MISSING** | Y (ref in 08-supp-figures.md:110 to SR4) |
| Figure S7 | T2 Beginner vs. Advanced Accuracy | 08-supp-figures.md:112 | Y (PAPER-V2/figures/fig-s7-t2-beginner-advanced.png) | Y (ref in 08-supp-figures.md:119 to SR3) |
| Figure S8 | Year Distribution of 401 Candidates | 08-supp-figures.md:121 | Y (PAPER-V2/figures/fig-s8-year-distribution.png) | Y (ref in 08-supp-figures.md:128 to 4.1) |

---

## Supplementary Issue: Table S6 Reference Mismatch (from Registry B)

**Location:** 01-methods.md:123
**Severity:** MAJOR (added as supplement to findings above)
**Category:** Table-Ref
**Issue:** The text says "Results of these checks are reported in the Supplementary Materials (Table S6)." The four robustness checks described (weight sensitivity sweep, gate threshold sensitivity, feature leave-one-out) correspond to SR6 (Feature Leave-One-Out) and SR8 (Sensitivity Analysis Extended) in the supplementary results, NOT Table S6 (which is the Cross-Model Response Length Gradient table).
**Recommendation:** Change "(Table S6)" to the correct supplementary reference. Options: "(Supplementary Results SR6 and SR8)" or simply "(Supplementary Results)".
**Quote:** "Results of these checks are reported in the Supplementary Materials (Table S6)."

---

## Cross-Reference Validation Summary

### Section References: PASS (with minor notes)
- All "Section X.Y" references resolve to valid sections in the registry
- Zero references to "Section 1" or "Section 2" (correct -- paper starts at Section 3)
- Broad "Section 4" references could be more specific (Finding 5, 7) but are not broken
- Intra-supplementary references (S1.3, S1.4, Section 3.5.6, Section 3.7, etc.) all resolve correctly

### Table References: 1 ERROR
- Main text Tables 1-11: all defined, all referenced -- PASS
- Supplementary Tables S1-S10: all defined -- PASS
- Tables S2, S4, S7, S8, S9, S10 are not explicitly cross-referenced from the main text (acceptable for supplementary material)
- **Table S6 misreference at 01-methods.md:123** -- refers to wrong table (Finding, supplementary issue above)

### Figure References: 2 CRITICAL, 1 MAJOR
- Figures 1-9 exist on disk in PAPER/figures/ but NOT in PAPER-V2/figures/ (Finding 3)
- Figure S2 and Figure S6 are described but have no image files on disk anywhere (Finding 4)
- Figure 11/12 descriptions in 02-results.md:287 do not match actual figure content (Finding 1)
- Figure S7 data values for Haiku are inconsistent with Table SR3/S8 (Finding 2)
- Figure S3 is described but never referenced in any main text section

### Intra-Supplementary References: PASS
- SR sections reference main text sections correctly (Section 3.5.3, 3.5.6, 4, etc.)
- Supplementary methods reference Section S1.3, S1.4 correctly
- SR7 references Section 4.3 (valid, though 5.6 more precise -- Finding 9)
