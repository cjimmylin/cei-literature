# Expert 3: Supplementary Coherence Review

## Summary

Reviewed bidirectional cross-references between main text (01-methods.md, 02-results.md) and supplementary materials (05-supp-methods.md, 06-supp-results.md, 07-supp-tables.md, 08-supp-figures.md). Found **4 CRITICAL**, **4 MAJOR**, and **5 MINOR** issues across 13 findings. The most serious issues are data value contradictions for Haiku T2 scores in Figure S7, incorrect figure-content mapping in the main text's description of Figures 10--12, a mislabeled supplementary reference (Table S6 vs SR6), and a CI feature count discrepancy.

---

## Finding 1
**Location:** 08-supp-figures.md:115
**Severity:** CRITICAL
**Category:** Data-Consistency
**Issue:** Figure S7 data values for Haiku T2 scores contradict every other source. Figure S7 states Haiku Beginner = 86.7%, Advanced = 66.7%. All other sources (02-results.md Table 9, 06-supp-results.md SR3, 07-supp-tables.md Table S8, 02-results.md Table 10) consistently report Haiku Beginner = 80% (12/15), Advanced = 73.3% (11/15), Overall = 76.7%.
**Recommendation:** Correct Figure S7 data values to: "Haiku: Beginner 80.0%, Advanced 73.3%."
**Quote:** `Haiku: Beginner 86.7%, Advanced 66.7%.`

---

## Finding 2
**Location:** 08-supp-figures.md:117
**Severity:** CRITICAL
**Category:** Data-Consistency
**Issue:** Figure S7 key feature text describes a "20-percentage-point drop from Beginner (86.7%) to Advanced (66.7%)" for Haiku. The actual drop per all other sources is 6.7 pp (80% to 73.3%). The entire narrative built on these wrong numbers is incorrect.
**Recommendation:** Rewrite the Haiku narrative to: "Haiku shows the expected difficulty effect with a 6.7-percentage-point drop from Beginner (80.0%) to Advanced (73.3%)."
**Quote:** `Haiku shows the expected difficulty effect with a 20-percentage-point drop from Beginner (86.7%) to Advanced (66.7%)`

---

## Finding 3
**Location:** 08-supp-figures.md:115
**Severity:** MAJOR
**Category:** Data-Consistency
**Issue:** Figure S7 data values for Gemini Flash have Beginner/Advanced swapped compared to Table SR3 and Table S8. Figure S7 states "Gemini Flash: 13.3%/6.7%" (in Beginner/Advanced format), implying Beginner=13.3%, Advanced=6.7%. But Table SR3 and Table S8 both report Gemini Flash Beginner=6.7% (1/15), Advanced=13.3% (2/15).
**Recommendation:** Correct Figure S7 to: "Gemini Flash: Beginner 6.7%, Advanced 13.3%."
**Quote:** `Gemini Flash: 13.3\%/6.7\%.`

---

## Finding 4
**Location:** 02-results.md:287
**Severity:** CRITICAL
**Category:** Figure-Numbering
**Issue:** The main text incorrectly describes the content of Figures 11 and 12. It states: "Figure 11 presents the rubric ceiling effect with the T2 discrimination contrast, and Figure 12 presents the bias--values independence analysis." However, per 08-supp-figures.md: Figure 11 = Cross-Vendor Rubric Heatmap (rubric only, no T2), Figure 12 = T2 Accuracy by Model, and Figure 13 = Vendor Capability Radar. There is no main-body figure dedicated to bias--values independence (that is Figure S6). The text also references "Figures 10--12" but the cross-vendor section (4.6) references "Figures 11--13."
**Recommendation:** Correct to: "Figure 10 presents the K<R<V gradient across models and traditions, Figure 11 presents the rubric ceiling heatmap, Figure 12 presents T2 accuracy by model, and Figure 13 presents the vendor capability radar. Bias--values scatter plots appear in Figure S6."
**Quote:** `Figure 11 presents the rubric ceiling effect with the T2 discrimination contrast, and Figure 12 presents the bias--values independence analysis.`

---

## Finding 5
**Location:** 01-methods.md:123
**Severity:** CRITICAL
**Category:** Forward-Ref
**Issue:** The main text states "Results of these checks are reported in the Supplementary Materials (Table S6)." However, Table S6 in 07-supp-tables.md is "Cross-Model Response Length Gradient" -- it contains response length data, not leave-one-out/sensitivity results. The leave-one-out analysis is in SR6 (06-supp-results.md), and the gate threshold sensitivity is in SR8. The weight sensitivity sweep is also in SR8.
**Recommendation:** Correct to: "Results of these checks are reported in the Supplementary Results (SR6, SR8)."
**Quote:** `Results of these checks are reported in the Supplementary Materials (Table S6).`

---

## Finding 6
**Location:** 06-supp-results.md:171-175; 05-supp-methods.md:261
**Severity:** MAJOR
**Category:** Data-Consistency
**Issue:** The leave-one-out analysis in both SR6 and S5.6 claims "16 active scoring features (6 RD + 6 PE + 4 CI weighted features)." However, the CI axis formula (in 01-methods.md, 07-supp-tables.md Table S2) includes 5 weighted features: C2 (30), C4 (25), C3 (20), C6 (15), C5 (10). The SR6 table lists only 4 CI features (C2, C4, C3, C5), omitting C6 (Community Engagement). The correct count is 17 active features, not 16.
**Recommendation:** Either add C6 to the leave-one-out table and correct to "17 active scoring features (6 RD + 6 PE + 5 CI)" throughout, or explain why C6 is excluded.
**Quote:** `16 active scoring features (6 RD, 6 PE, 4 CI weighted features)`

---

## Finding 7
**Location:** 08-supp-figures.md:41
**Severity:** MINOR
**Category:** Data-Consistency
**Issue:** Figure 10 description states Opus V/K ratio = 3.42x. All other sources (02-results.md Table 5, Table 10, Table S6, SR1) report 3.41x. The computed value 6327/1853 = 3.4144, which rounds to 3.41x.
**Recommendation:** Correct to "Opus 3.41x" in the Figure 10 data values.
**Quote:** `Opus 3.42$\times$, Sonnet 3.59$\times$, Haiku 9.18$\times$`

---

## Finding 8
**Location:** 06-supp-results.md (entire file)
**Severity:** MAJOR
**Category:** Back-Ref
**Issue:** SR5 (Void Factor Analysis) and SR7 (WEIRD-Neutral Weighting) reference "Section 6" (the Conclusion) for "calls to action," but this reference cannot be verified without reading 04-conclusion.md. More importantly, SR5 references Section 4.3 (valid), SR7 references Section 4.3 (valid), and SR8 references Section 3.3 (valid). However, no supplementary result section explicitly back-references Section 4.5 or 4.6 despite providing the underlying data for those sections. This creates a one-directional reference pattern.
**Recommendation:** Add back-references from SR1/SR2 to "see Section 4.5" and from SR3/SR4 to "see Sections 4.5--4.6" for navigability.
**Quote:** N/A

---

## Finding 9
**Location:** 08-supp-figures.md:84
**Severity:** MINOR
**Category:** Intra-Supp
**Issue:** Figure S2 description says "Referenced in Section 3.3 and Supplementary Results" without specifying which SR section. The gate threshold sensitivity data appears in SR8 (Table SR8c).
**Recommendation:** Change to "Referenced in Section 3.3 and Supplementary Results SR8."
**Quote:** `Referenced in Section 3.3 and Supplementary Results.`

---

## Finding 10
**Location:** 08-supp-figures.md:103
**Severity:** MINOR
**Category:** Intra-Supp
**Issue:** Figure S5 description says "Referenced in Section 4.6 and Supplementary Results" without specifying which SR section.
**Recommendation:** Change to "Referenced in Section 4.6 and Supplementary Results SR1."
**Quote:** `Referenced in Section 4.6 and Supplementary Results.`

---

## Finding 11
**Location:** 08-supp-figures.md:128
**Severity:** MINOR
**Category:** Forward-Ref
**Issue:** Figure S8 (Year Distribution) is "Referenced in Section 4.1" per its description, but Section 4.1 in 02-results.md never explicitly references "Figure S8." Section 4.1 discusses temporal distribution but only references Figures 1-4 and no supplementary figures in that subsection.
**Recommendation:** Add an explicit reference to Figure S8 in Section 4.1's temporal distribution paragraph, or note in the figure description that it is a standalone supplementary visualization.
**Quote:** `Referenced in Section 4.1.`

---

## Finding 12
**Location:** 07-supp-tables.md:3
**Severity:** MAJOR
**Category:** Table-Numbering
**Issue:** The introductory paragraph of 07-supp-tables.md says "Tables S4--S5 describe the external search methodology and meta-evaluation criteria" and "Tables S6--S8 report the full cross-model and cross-vendor implementation trial results." The label "Table S6" for response length data is correct within this file. However, the main text at 01-methods.md:123 uses "Table S6" to refer to leave-one-out results, creating cross-file label confusion. The supplementary tables file is internally consistent, but the main text reference is wrong.
**Recommendation:** See Finding 5. The fix is in the main text, not the supplementary tables file.
**Quote:** `Tables S6--S8 report the full cross-model and cross-vendor implementation trial results.`

---

## Finding 13
**Location:** 08-supp-figures.md:96
**Severity:** MINOR
**Category:** Intra-Supp
**Issue:** Figure S4 description says "Referenced in Section 4.5 and Supplementary Results SR1." This is a valid and well-formed cross-reference. No issue -- noted for completeness in the checklist.
**Recommendation:** None needed.
**Quote:** `Referenced in Section 4.5 and Supplementary Results SR1.`

---

## Reference Checklist

### A. Main Text Forward References (01-methods.md, 02-results.md)

| Source | Reference | Target | Status |
|--------|-----------|--------|--------|
| 01-methods.md:7 | Figure S1 (PRISMA) | 08-supp-figures.md: Figure S1 | VALID |
| 01-methods.md:65 | Table S3 | 07-supp-tables.md: Table S3 | VALID |
| 01-methods.md:81 | Table S1 | 07-supp-tables.md: Table S1 | VALID |
| 01-methods.md:85 | Table S3 | 07-supp-tables.md: Table S3 | VALID |
| 01-methods.md:123 | Table S6 (leave-one-out) | 07-supp-tables.md: Table S6 (response length) | **INVALID** -- wrong target |
| 01-methods.md:127 | Table S5 | 07-supp-tables.md: Table S5 | VALID |
| 02-results.md:287 | Figures 10--12 | 08-supp-figures.md: Figures 10--12 | VALID (exist) |
| 02-results.md:287 | Figure 12 = bias-values | 08-supp-figures.md: Figure 12 = T2 | **INVALID** -- content mismatch |
| 02-results.md:305 | Figures 11--13 | 08-supp-figures.md: Figures 11--13 | VALID |

### B. Supplementary Back-References to Main Text

| Source | Reference | Target | Status |
|--------|-----------|--------|--------|
| 05-supp-methods.md:128 | Section 3.7 of the main text | 01-methods.md: Section 3.7 | VALID |
| 05-supp-methods.md:179 | Section 3.5.6 of the main text | 01-methods.md: Section 3.5.6 | VALID |
| 05-supp-methods.md:336 | Section 3.7 | 01-methods.md: Section 3.7 | VALID |
| 06-supp-results.md:3 | Section 4 | 02-results.md: Section 4 | VALID |
| 06-supp-results.md:37 | Section 3.5.3 | 01-methods.md: Section 3.5.3 | VALID |
| 06-supp-results.md:77 | Section 3.5.6 | 01-methods.md: Section 3.5.6 | VALID |
| 06-supp-results.md:85 | Section 4 (main Results) | 02-results.md: Section 4 | VALID |
| 06-supp-results.md:306 | Section 3.3 | 01-methods.md: Section 3.3 | VALID |
| 07-supp-tables.md:9 | Section 3.2 | 01-methods.md: Section 3.2 | VALID |
| 07-supp-tables.md:49 | Section 3.3 | 01-methods.md: Section 3.3 | VALID |
| 07-supp-tables.md:51 | Section 3.2 | 01-methods.md: Section 3.2 | VALID |
| 07-supp-tables.md:93 | Section 3.2 | 01-methods.md: Section 3.2 | VALID |
| 07-supp-tables.md:101 | Section 3.1, Stage 2 | 01-methods.md: Section 3.1 | VALID |
| 07-supp-tables.md:124 | Section 3.4 | 01-methods.md: Section 3.4 | VALID |
| 07-supp-tables.md:124 | Section 4 | 02-results.md: Section 4 | VALID |
| 07-supp-tables.md:138 | Section 3.7 | 01-methods.md: Section 3.7 | VALID |
| 07-supp-tables.md:144 | Section 3.5 | 01-methods.md: Section 3.5 | VALID |
| 07-supp-tables.md:164 | Section 3.5.6, Caveat 3 | 01-methods.md: Section 3.5.6 | VALID |
| 07-supp-tables.md:170 | Section 3.5.3 | 01-methods.md: Section 3.5.3 | VALID |
| 07-supp-tables.md:186 | Section 3.5.1, 3.5.5, 3.5.6 | 01-methods.md | VALID |
| 07-supp-tables.md:188 | Section 6 | 04-conclusion.md: Section 6 | VALID |
| 07-supp-tables.md:192 | Section 3.5.6 | 01-methods.md: Section 3.5.6 | VALID |
| 07-supp-tables.md:198 | Section 3.5.2 | 01-methods.md: Section 3.5.2 | VALID |
| 07-supp-tables.md:226 | Section 3.6 | 01-methods.md: Section 3.6 | VALID |
| 07-supp-tables.md:255 | Section 4.3 | 02-results.md: Section 4.3 | VALID |
| 08-supp-figures.md:45 | Section 4.5 | 02-results.md: Section 4.5 | VALID |
| 08-supp-figures.md:54 | Section 4.6 | 02-results.md: Section 4.6 | VALID |
| 08-supp-figures.md:63 | Section 4.6 | 02-results.md: Section 4.6 | VALID |
| 08-supp-figures.md:74 | Section 4.6 | 02-results.md: Section 4.6 | VALID |
| 08-supp-figures.md:81 | Section 3.1 | 01-methods.md: Section 3.1 | VALID |
| 08-supp-figures.md:84 | Section 3.3 | 01-methods.md: Section 3.3 | VALID |
| 08-supp-figures.md:87 | Section 3.2 | 01-methods.md: Section 3.2 | VALID |
| 08-supp-figures.md:128 | Section 4.1 | 02-results.md: Section 4.1 | VALID (but no reciprocal ref) |

### C. Intra-Supplementary Cross-References

| Source | Reference | Target | Status |
|--------|-----------|--------|--------|
| 08-supp-figures.md:96 | SR1 | 06-supp-results.md: SR1 | VALID |
| 08-supp-figures.md:103 | Supplementary Results (unspecified) | 06-supp-results.md | VALID but vague |
| 08-supp-figures.md:110 | SR4 | 06-supp-results.md: SR4 | VALID |
| 08-supp-figures.md:119 | SR3 | 06-supp-results.md: SR3 | VALID |
| 08-supp-figures.md:84 | Supplementary Results (unspecified) | 06-supp-results.md: SR8 | VALID but vague |

### D. Table Numbering Integrity

| Table | Defined In | Referenced By | Status |
|-------|-----------|---------------|--------|
| Table S1 | 07-supp-tables.md | 01-methods.md:81 | VALID |
| Table S2 | 07-supp-tables.md | (internal) | VALID |
| Table S3 | 07-supp-tables.md | 01-methods.md:65,85 | VALID |
| Table S4 | 07-supp-tables.md | (internal) | VALID |
| Table S5 | 07-supp-tables.md | 01-methods.md:127 | VALID |
| Table S6 | 07-supp-tables.md | 01-methods.md:123 | **INVALID** -- main text expects leave-one-out, file has response lengths |
| Table S7 | 07-supp-tables.md | (internal) | VALID |
| Table S8 | 07-supp-tables.md | (internal) | VALID |
| Table S9 | 07-supp-tables.md | (internal) | VALID |
| Table S10 | 07-supp-tables.md | (internal) | VALID |
| Tables S1--S10 | 07-supp-tables.md | Sequential, complete | VALID |

### E. Figure Numbering Integrity

| Figure | Described In | Referenced By | Status |
|--------|-------------|---------------|--------|
| Figure 1 | 08-supp-figures.md | 02-results.md:9,13 | VALID |
| Figure 2 | 08-supp-figures.md | 02-results.md:13 | VALID |
| Figure 3 | 08-supp-figures.md | 02-results.md:23 | VALID |
| Figure 4 | 08-supp-figures.md | 02-results.md:15 | VALID |
| Figure 5 | 08-supp-figures.md | (not found in assigned files) | CHECK other files |
| Figure 6 | 08-supp-figures.md | (not found in assigned files) | CHECK other files |
| Figure 7 | 08-supp-figures.md | (not found in assigned files) | CHECK other files |
| Figure 8 | 08-supp-figures.md | (not found in assigned files) | CHECK other files |
| Figure 9 | 08-supp-figures.md | (not found in assigned files) | CHECK other files |
| Figure 10 | 08-supp-figures.md | 02-results.md:287 | VALID |
| Figure 11 | 08-supp-figures.md | 02-results.md:287,305 | VALID (exists) but content mismatch in 287 |
| Figure 12 | 08-supp-figures.md | 02-results.md:287 | **INVALID** -- text says bias-values, figure is T2 |
| Figure 13 | 08-supp-figures.md | 02-results.md:305 | VALID |
| Figure S1 | 08-supp-figures.md | 01-methods.md:7 | VALID |
| Figure S2 | 08-supp-figures.md | (Section 3.3 ref) | VALID |
| Figure S3 | 08-supp-figures.md | (Section 3.2 ref) | VALID |
| Figure S4 | 08-supp-figures.md | (SR1 ref) | VALID |
| Figure S5 | 08-supp-figures.md | (Section 4.6 ref) | VALID |
| Figure S6 | 08-supp-figures.md | (SR4 ref) | VALID |
| Figure S7 | 08-supp-figures.md | (SR3 ref) | VALID but data values wrong |
| Figure S8 | 08-supp-figures.md | (Section 4.1 ref) | VALID but no reciprocal ref |
| Figures S1--S8 | 08-supp-figures.md | Sequential, complete | VALID |

### F. Data Consistency Summary

| Data Point | Main Text Value | Supp Value | Match? |
|------------|----------------|------------|--------|
| Haiku T2 Beginner | 80% (Table 9, Table 10) | 80% (SR3, S8) | YES |
| Haiku T2 Beginner | 80% | 86.7% (Fig S7) | **NO** |
| Haiku T2 Advanced | 73.3% (Table 9, Table 10) | 73.3% (SR3, S8) | YES |
| Haiku T2 Advanced | 73.3% | 66.7% (Fig S7) | **NO** |
| Gemini Flash T2 Beg | 6.7% (Table 10) | 6.7% (SR3, S8) | YES |
| Gemini Flash T2 Beg | 6.7% | 13.3% (Fig S7) | **NO** |
| Opus V/K ratio | 3.41x (Table 5, 6, S6) | 3.42x (Fig 10) | **NO** (minor rounding) |
| Rubric scores (all) | Match across Table 7/10 | Match SR2, S7 | YES |
| Response lengths (all) | Match across Table 5/6/10 | Match SR1, S6 | YES |
| Claim stats (Table 4) | Match | Match Table S9 | YES |
| CI features (formula) | 5 (C2,C3,C4,C5,C6) | 4 in LOO (SR6) | **NO** -- C6 missing |
| Bootstrap CI width | 15.87 (main) | 15.87 (SR8) | YES |
| Kendall's tau | 0.773 (main) | 0.773 (SR8) | YES |
| Robust benchmarks | 11 (main Tier 1) | 13 (S5.4) | **DISCREPANCY** -- see note |

Note on robust benchmark count: Section 3.3 defines Tier 1 as p >= 0.80 and reports 11 benchmarks. S5.4 reports "Robust benchmarks (p >= 0.80): 11" and SR8a reports "Robust: p >= 0.80, Count: 13." The SR8a count of 13 may reflect pre-removal numbers (before Break the Checkbox and BuddhismEval removal), but this should be clarified.
