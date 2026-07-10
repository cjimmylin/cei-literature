# Expert 2: Claims & Statistical Consistency Audit

**Auditor:** Claims & Statistical Consistency Auditor
**Date:** 2026-04-12
**Files reviewed:** 00-abstract.md, 01-methods.md, 02-results.md, 03-discussion.md, 04-conclusion.md, 07-supp-tables.md

---

## Finding 1
**Location:** 02-results.md (Table 2, lines 37-49) vs. 02-results.md:85 and 00-abstract.md:7 and 03-discussion.md:9
**Severity:** CRITICAL
**Category:** Count
**Issue:** The Tier 1 table lists 9 Islamic benchmarks (ELQV, Domain-Specific LLMs, AceGPT, Religious Hate Speech Taxonomy, PapersPlease, Challenging Transformer-based, PRISM Alignment, Sometimes the Model doth Preach, HAQA and QUQA), but the prose states "8 of 11 Tier 1 benchmarks" across the abstract, results (line 85), and discussion (line 9). The actual count from Table 2 is 9 of 11 Islamic Tier 1 entries.
**Recommendation:** Either correct the prose to "9 of 11 Tier 1 benchmarks" everywhere (abstract, results, discussion), or reclassify one Tier 1 benchmark (e.g., Religious Hate Speech Taxonomy) to a different tradition. Verify which is the intended count and reconcile across all occurrences.
**Quote:** "Islam dominates Tier 1, contributing 8 of 11 entries." (02-results.md:85)

---

## Finding 2
**Location:** 02-results.md:15 vs. 01-methods.md:15 (PRISMA flow)
**Severity:** MAJOR
**Category:** Count
**Issue:** Gate-passer intermediate count is inconsistent. Methods (PRISMA flow, line 15) states "47 pass both hard gates ... 2 removed post-review ... yielding 45 gate-passers." Results (line 15) states "the two hard gates together eliminate 355 of 401 candidates (88.5%), leaving only 46 gate-passers. (The final count of 45 reflects the post-review removal of BuddhismEval...)" Since 401-355=46, the Results section implies 46 initial gate-passers with only 1 removal (BuddhismEval), while Methods says 47 initial with 2 removals (Break the Checkbox + BuddhismEval). The Results text at line 15 accounts only for BuddhismEval, omitting Break the Checkbox from the post-review removal narrative.
**Recommendation:** Harmonize: either 401-354=47 initially (then 2 removed = 45) or 401-355=46 initially. If 47 is correct, change "355" to "354" and "88.5%" to "88.3%" in Results. Also add Break the Checkbox to the removal note in Results line 15. If 46 is correct, update the PRISMA flow in Methods.
**Quote:** "the two hard gates together eliminate 355 of 401 candidates (88.5%), leaving only 46 gate-passers" (02-results.md:15)

---

## Finding 3
**Location:** 07-supp-tables.md:232 vs. 02-results.md:160, 00-abstract.md:7, 03-discussion.md:9
**Severity:** MINOR
**Category:** Statistic
**Issue:** The chi-squared statistic and Cramer's V are reported with different precision across files. Table S9 reports chi-sq = 64.957 and V = 0.526 (3 decimal places). The main text (Results Table 4, abstract, discussion) rounds to chi-sq = 64.96 and V = 0.53 (2 decimal places). While these are consistent within rounding, the reader may notice the mismatch between 0.526 in the supplement and 0.53 in the main text.
**Recommendation:** Standardize precision. Report V = 0.53 everywhere in main text and V = 0.526 in the supplement, or use V = 0.53 uniformly with a note that Table S9 carries additional precision.
**Quote:** Table S9: "V = 0.526"; Results Table 4: "$V$ = 0.53"

---

## Finding 4
**Location:** 07-supp-tables.md:240 vs. 02-results.md:203
**Severity:** MINOR
**Category:** Statistic
**Issue:** The Cohen's d for Claim 8 is reported as d = -1.232 in Table S9 but d = -1.23 in Results (line 203), abstract, and discussion. Similarly, the p-value is p = 0.0002 in Table S9 but p = 0.000181 in Results. Both are consistent within rounding (0.0002 vs. 0.000181; -1.232 vs. -1.23), but the different precision levels across files could create confusion during peer review.
**Recommendation:** Use d = -1.23 consistently in main text, d = -1.232 in Table S9. Use p = 0.0002 or p < 0.001 consistently in main text; the exact p = 0.000181 in Results (line 203) adds unnecessary extra precision compared to other citations of the same value. Standardize.
**Quote:** Table S9: "d = $-$1.232"; Results: "Cohen's $d$ = $-$1.23"

---

## Finding 5
**Location:** 02-results.md:203 vs. 03-discussion.md:77
**Severity:** MINOR
**Category:** PValue
**Issue:** The Claim 8 t-test p-value is reported with different precision. Results (line 203) gives the exact p = 0.000181. Discussion (line 77) reports p < 0.001. The Wilcoxon p-value is similarly p = 0.00061 in Results but p < 0.001 in Discussion. While both representations are correct, the Results section gives exact values only for Claim 8, while reporting p < 0.001 for Claims 1 and 3. This inconsistency in reporting convention within Results is distracting.
**Recommendation:** For consistency within the Results section, report all p-values either as exact values or as inequality bounds. The current approach (exact for C8 but inequality for C1/C3) suggests C8 received different treatment.
**Quote:** Results: "p = 0.000181" (C8) vs. "p < 0.001" (C1, C3)

---

## Finding 6
**Location:** 01-methods.md:218 and 07-supp-tables.md:226
**Severity:** MINOR
**Category:** PValue
**Issue:** The paper uses Bonferroni correction (alpha_adj = 0.05/8 = 0.00625) throughout, never BH-FDR. Methods Section 3.6 states the correction; Table S9 labels a "Bonferroni" column. The correction is consistently applied and correctly described. However, the task mandate asked whether BH-FDR is referenced -- it is not. Only Bonferroni is used. This is internally consistent; no error here.
**Recommendation:** No action needed. Bonferroni is more conservative than BH-FDR and is consistently described and applied. The choice is defensible given only 8 comparisons.
**Quote:** "the Bonferroni-corrected threshold of alpha_adj = 0.05 / 8 = 0.00625" (01-methods.md:218)

---

## Finding 7
**Location:** 02-results.md:171 (Claim 1 discussion)
**Severity:** MINOR
**Category:** EffectSize
**Issue:** V = 0.53 is correctly labeled "large effect" in the Claim 1 discussion: "The Cramer's V = 0.53 indicates a large effect under both Cohen's conventions and the benchmarks appropriate for a 14-category test." This is consistent with the conventions stated in Methods (line 216): V >= 0.5 is large. No inconsistency found.
**Recommendation:** No action needed.
**Quote:** "Cramer's V = 0.53 indicates a large effect" (02-results.md:171)

---

## Finding 8
**Location:** 02-results.md:203, 03-discussion.md:77, 07-supp-tables.md:249
**Severity:** MINOR
**Category:** EffectSize
**Issue:** d = -1.23 is consistently labeled "large effect" across all occurrences. Results: "Cohen's d = -1.23 (large effect)". Discussion: "The effect size of d = -1.23 is large by any conventional standard." Table S9 notes: "The large effect size (d = -1.232)..." Consistent with Methods conventions (d >= 0.8 is large). No inconsistency.
**Recommendation:** No action needed.
**Quote:** "Cohen's d = -1.23 (large effect)" (02-results.md:203)

---

## Finding 9
**Location:** 00-abstract.md:7
**Severity:** MAJOR
**Category:** Count
**Issue:** The abstract states "28 of 47 gate-passing candidates" for Islam. This uses the pre-removal count of 47. But the abstract also says "401 benchmark candidates" were assembled and "47" passed gates. This is consistent with the Methods PRISMA flow (47 initial, 2 removed = 45 final). However, the statistical tests in Table S9 all use n = 47, which means the tests were run on the pre-removal sample. This is not inherently wrong (the tests were designed before post-review removal), but the paper should be clearer about whether statistical claims apply to n=47 or n=45.
**Recommendation:** Add a brief note in Section 4.4 or 3.6 explicitly stating that all 8 statistical tests use the pre-removal sample of n=47, and that post-review removal of 2 benchmarks does not affect the test conclusions.
**Quote:** "28 of 47 gate-passing candidates" (abstract)

---

## Finding 10
**Location:** 02-results.md:209 vs. 00-abstract.md:5
**Severity:** MINOR
**Category:** Count
**Issue:** The Results section (line 209) describes the construct validity battery as "15 Knowledge items, 15 Reasoning items, 25 Values items, and 10 Bias items" totaling 65. The abstract says "65-item construct validity battery (Knowledge, Reasoning, Values, and Bias items across Islam, Christianity, and Hinduism)." Methods (line 147-151) says "45 construct validity items and 20 bias-values discrimination items" where the 45 = 5K+5R+5V per 3 traditions = 45 items, plus 20 bias-values = 65 total. But Results says 15K + 15R + 25V + 10B = 65. The discrepancy is that Methods describes "5 Values per tradition = 15 Values items" but Results says "25 Values items." The 25 apparently includes the 10 values items from the matched bias-values pairs (15 core + 10 paired = 25).
**Recommendation:** Clarify in Methods that the 25 Values items comprise 15 construct-validity Values items + 10 matched-pair Values items. The current Methods description ("45 construct validity items and 20 bias-values discrimination items") is consistent but the decomposition in Results (15K + 15R + 25V + 10B) implicitly merges paired Values into the V count. Add a parenthetical note.
**Quote:** Methods: "45 construct validity items and 20 bias-values discrimination items"; Results: "15 Knowledge items, 15 Reasoning items, 25 Values items, and 10 Bias items"

---

## Finding 11
**Location:** 02-results.md (Table 2, Tier 2 line 57)
**Severity:** MINOR
**Category:** Count
**Issue:** The Antisemitism Detection benchmark (Tier 2) has p = 0.840, which is above the Tier 2 cutoff of 0.30 <= p < 0.80. With p = 0.840, this benchmark should be in Tier 1 (p >= 0.80), not Tier 2. Either the p-value or the tier assignment is incorrect.
**Recommendation:** Verify the bootstrap inclusion probability for Antisemitism Detection. If p = 0.840 is correct, move it to Tier 1 (making 12 Tier 1 benchmarks). If it belongs in Tier 2, correct the p-value.
**Quote:** "Antisemitism Detection | 2022 | Christianity | MIX | 44.1 | [36.2, 52.8] | 0.840" (02-results.md, Tier 2 table)

---

## Finding 12
**Location:** 03-discussion.md:57-58 and throughout
**Severity:** MINOR
**Category:** Caveat
**Issue:** The three methodological caveats are consistently characterized across all mentions: (1) T2 blinding asymmetry, (2) same-vendor scorer bias, (3) Gemini backfilled protocol. The caveats are mentioned in Methods 3.5.6, Results 4.6, Discussion 5.4, Discussion 5.9, Conclusion, and Table S7 notes. The characterizations are consistent and not subject to drift.
**Recommendation:** No action needed. The caveats are well-managed.
**Quote:** N/A

---

## Finding 13
**Location:** 03-discussion.md:141
**Severity:** MINOR
**Category:** Drift
**Issue:** When summarizing Claims 1-4 and 8 in the "Methodological Transparency" section (5.8), the discussion correctly hedges REVISED and MARGINAL claims and presents SUPPORTED claims as strong. No interpretive drift detected. SUPPORTED claims are described with confident language ("survive the robustness battery"), MARGINAL with appropriate hedging ("above conventional significance thresholds"), and REVISED claims are presented as informative revisions rather than failures.
**Recommendation:** No action needed. The framing accurately matches verdict strength.
**Quote:** N/A

---

## Finding 14
**Location:** 01-methods.md:15 (PRISMA flow) and 02-results.md:121 (Table 2 text)
**Severity:** MAJOR
**Category:** Count
**Issue:** The PRISMA flow states "25 tiered benchmarks (11 Tier 1, 4 Tier 2, 10 Tier 3)." The Tier 2 table has 4 entries, but Antisemitism Detection (p = 0.840) should be Tier 1 per the tier definitions. If Antisemitism Detection moves to Tier 1, the count becomes 12 Tier 1, 3 Tier 2, 10 Tier 3 = 25 total. This cascading count error from Finding 11 affects the PRISMA flow and all mentions of "11 Tier 1" throughout the paper.
**Recommendation:** Resolve the Antisemitism Detection tier assignment (Finding 11 above), then update all tier counts accordingly.
**Quote:** "25 tiered benchmarks: 11 Tier 1, 4 Tier 2, and 10 Tier 3" (01-methods.md:121)

---

## Finding 15
**Location:** 07-supp-tables.md:242
**Severity:** MINOR
**Category:** Table-Prose
**Issue:** Table S9 shows C8c (binomial >= 50) has Bonferroni status "FAIL" but outcome "SUPPORTED (alpha = 0.05)." This is internally consistent (p = 0.011 passes at alpha = 0.05 but fails Bonferroni at 0.00625). However, in Results (line 203), the p = 0.011 is simply reported without noting the Bonferroni failure. The text says "A binomial test on the proportion achieving A3 >= 50 yields 3 of 16 (p = 0.011)" without flagging that this specific sub-test does not survive Bonferroni correction.
**Recommendation:** Add a parenthetical in Results line 203 noting that C8c does not survive Bonferroni correction, while the three other C8 sub-tests do. This maintains the transparency standard established by Table S9.
**Quote:** "A binomial test on the proportion achieving A3 >= 50 yields 3 of 16 (p = 0.011)" (02-results.md:203)

---

## Finding 16
**Location:** 07-supp-tables.md:232-243 vs. 02-results.md:158-167 (Table 4)
**Severity:** MINOR
**Category:** Table-Prose
**Issue:** Table 4 in Results reports C1b statistics inline within the Claim 1 prose (chi-sq = 21.84, V = 0.30, p = 0.0006) at line 171, but Table 4 itself only shows C1a (chi-sq = 64.96). Table S9 shows both C1a and C1b as separate rows. Table 4 and Table S9 are thus consistent for the rows they share, and the additional C1b data appears only in Table S9 and the prose. No actual conflict.
**Recommendation:** No action needed. Table 4 is a summary; Table S9 is complete. The relationship is correctly described.
**Quote:** N/A

---

## Finding 17
**Location:** 07-supp-tables.md:243 vs. 02-results.md:203
**Severity:** MINOR
**Category:** Statistic
**Issue:** Table S9 reports C8d (binomial >= 75) p = 0.00002. Results reports the same as p = 0.000015. These are inconsistent: 0.00002 vs. 0.000015. One or both may be rounded differently from the true value.
**Recommendation:** Verify the exact p-value from the computation and standardize across both locations. If the exact value is 0.0000153..., Table S9 should round to 0.00002 and Results to 0.000015 -- both are defensible roundings but the mismatch should be noted or unified.
**Quote:** Table S9: "0.00002"; Results: "p = 0.000015"

---

## Finding 18
**Location:** 07-supp-tables.md:20 and throughout
**Severity:** MINOR
**Category:** Count
**Issue:** Table S1 reports "47 gate-passers" in the COMPOSITE row interpretation, consistent with the pre-removal count. Table S9 uses n=47 for C1-C5 tests. This is internally consistent -- all statistical tests use the pre-removal sample. No mismatch.
**Recommendation:** No action needed; see Finding 9 for the recommendation to add an explicit note about the pre-removal sample.
**Quote:** N/A

---

## Claim Tracking Matrix

| Claim | Verdict | 00-abstract | 01-methods | 02-results | 03-discussion | 04-conclusion | 07-supp-tables |
|-------|---------|-------------|------------|------------|---------------|---------------|----------------|
| C1: Tradition Asymmetry | SUPPORTED | chi-sq=64.96, V=0.53 | p<0.001 (line 218) | chi-sq=64.96, V=0.53, p<0.001 (Table 4, line 160, 171) | chi-sq=64.96, V=0.53, p<0.001 (line 9, 141) | Referenced (line 3) | chi-sq=64.957, V=0.526 (Table S9) |
| C2: Knowledge-Reasoning Conflation | SUPPORTED | p=0.0015 | p=0.0015 (line 218) | 13/47, p=0.0015 (Table 4, line 161, 175) | p=0.0015 (line 141) | p=0.0015 (line 17) | k=13, p=0.0015 (Table S9) |
| C3: Data Availability Bottleneck | SUPPORTED | Mentioned | p<0.001 (line 218) | 47/47, p<0.001 (Table 4, line 162, 179) | Mentioned (line 141) | Mentioned | k=47, p<0.001 (Table S9) |
| C4: Structural Epistemic Injustice | REVISED | Mentioned | Not significant (line 218) | Pseudo-R2=0.068, p=0.112 (Table 4, line 163, 183) | p=0.112 (line 147) | Referenced | Pseudo-R2=0.068, p=0.112 (Table S9) |
| C5: Field Recency | MARGINAL | Not mentioned by verdict | Not significant (line 218) | 28/47, p=0.121 (Table 4, line 164, 189) | p=0.121 (line 143) | Not mentioned | k=28, p=0.121 (Table S9) |
| C6: WEIRD Bias | REVISED | Mentioned | Not significant (line 218) | OR=0.58, p=0.090 (Table 4, line 165, 193) | p=0.090 (line 149) | Not mentioned | OR=0.580, p=0.090 (Table S9) |
| C7: Bias-Values Conflation | REVISED | r=0.288, p=0.68 | Not significant (line 218) | 10/23, p=0.678 (Table 4, line 166, 197) | p=0.68 (line 151) | Not mentioned | k=10, p=0.678 (Table S9) |
| C8: Values Relevance Failure | SUPPORTED | t=-4.93, d=-1.23 | d=-1.23 (line 252) | t=-4.93, p=0.000181, d=-1.23 (Table 4, line 167, 203) | t=-4.93, d=-1.23, p<0.001 (line 77, 141, 173) | Not mentioned directly | t=-4.93, p=0.0002, d=-1.232 (Table S9) |

### Verdict Consistency Summary

All 8 claims maintain consistent verdicts across every file:
- SUPPORTED: C1, C2, C3, C8 -- consistent everywhere
- REVISED: C4, C6, C7 -- consistent everywhere
- MARGINAL: C5 -- consistent everywhere

### Key Discrepancies Requiring Resolution (Ranked by Severity)

1. **CRITICAL:** Tier 1 Islamic count: 9 (per Table 2) vs. 8 (per prose in abstract, results, discussion) -- Finding 1
2. **MAJOR:** Antisemitism Detection p=0.840 placed in Tier 2 but Tier 1 threshold is p>=0.80 -- Finding 11/14
3. **MAJOR:** Gate-passer intermediate count: 46 (02-results.md:15) vs. 47 (01-methods.md:15, PRISMA) -- Finding 2
4. **MAJOR:** Statistical tests all use n=47 (pre-removal) without explicit justification -- Finding 9
5. **MINOR:** C8d p-value: 0.00002 (Table S9) vs. 0.000015 (Results) -- Finding 17
6. **MINOR:** Precision variation in V (0.53 vs 0.526) and d (-1.23 vs -1.232) across main text and supplement -- Findings 3, 4
7. **MINOR:** C8c Bonferroni failure not flagged in Results prose -- Finding 15
