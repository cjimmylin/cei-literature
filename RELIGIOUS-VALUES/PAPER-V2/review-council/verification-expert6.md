# Expert 6 Verification Report

**Date:** 2026-04-12
**Scope:** Post-edit cross-reference integrity check across all 9 paper files (00-abstract.md through 08-supp-figures.md)

---

## V1: Section References — PASS (with minor notes)

**Zero references to "Section 1" or "Section 2":** Confirmed. No references to Section 1 or Section 2 exist in any of the 9 paper files.

**Broad "Section 4" references:** Three instances found, all acceptable:
1. `03-discussion.md:4` — "The results in Section 4 document the structure..." (Discussion opening referring to the entire Results section — appropriate)
2. `04-conclusion.md:7` — "As documented in Section 4..." (Conclusion referencing entire Results — appropriate)
3. `06-supp-results.md:3` and `:85` — "the main Results section (Section 4)" (Supplementary material referring back to main Results — appropriate)

All other section references use specific subsection numbers (e.g., Section 3.1, Section 4.5, Section 5.6) and resolve to real headings:
- Sections 3.1–3.7: all present in 01-methods.md
- Sections 4.1–4.6: all present in 02-results.md
- Sections 5.1–5.9: all present in 03-discussion.md
- Section 6: present in 04-conclusion.md

**Verdict: PASS.** No broken section references. Broad "Section 4" references are contextually appropriate (referring to the entire Results section from Discussion/Conclusion/Supplementary).

---

## V2: Table References — PASS

**Main text table references:** Tables 1, 2, 5, 9, 10 are referenced in the main text. All resolve to defined tables within the paper files.

**Supplementary table references:** Tables S1–S10 are all defined in 07-supp-tables.md:
- Table S1 (S1a): Feature Matrix Score Distributions — defined line 7
- Table S2 (S2a, S2b): Scoring Formula Coefficients — defined line 24
- Table S3: Format Taxonomy — defined line 72
- Table S4: External Search Results — defined line 99
- Table S5: Meta-Evaluation Criteria — defined line 122
- Table S6: Cross-Model Response Length Gradient — defined line 142
- Table S7: Cross-Vendor Rubric Scores — defined line 168
- Table S8: T2 Arabic MCQ Results — defined line 196
- Table S9: Claim Robustness Battery — defined line 224
- Table S10: Void Factor Analysis — defined line 253

**"(Table S6)" in 01-methods.md check:** Confirmed absent. No "(Table S6)" reference exists in 01-methods.md. The relevant passage at line 123 now reads "Supplementary Results SR6, SR8" — correctly updated.

**Verdict: PASS.** All table references resolve to defined tables.

---

## V3: Figure References — FAIL (1 data error remaining)

**Figure 11/12 descriptions in 02-results.md:** FIXED. Line 287 now correctly reads:
> "Figure 10 presents the K < R < V gradient across models and traditions, Figure 11 presents the cross-vendor rubric heatmap showing the trimodal ceiling/near-ceiling/floor distribution, and Figure 12 presents T2 accuracy by model with the 93.3-percentage-point discrimination spread."

This matches the actual figure definitions in 08-supp-figures.md (Fig 11 = Cross-Vendor Rubric Heatmap, Fig 12 = T2 Accuracy by Model).

**Figure S7 data values:** PARTIALLY FIXED.
- Haiku: Now correctly shows 80.0%/73.3% (line 117), matching SR3 and Table S8. FIXED.
- Gemini Flash: Now correctly shows Beginner 6.7%, Advanced 13.3% (line 117), matching SR3 and Table S8. FIXED.
- **Gemini Pro: Still shows 6.7%/6.7% in Figure S7 (line 117), but SR3 (06-supp-results.md:72) and Table S8 (07-supp-tables.md:211) both report Beginner=0% (0/15), Advanced=13.3% (2/15).** This is a remaining data inconsistency — the 6.7% overall was distributed as 0%/13.3%, not 6.7%/6.7%.

**All main figures (1–13) and supplementary figures (S1–S8) are defined in 08-supp-figures.md** and references in the main text resolve correctly.

**Verdict: FAIL.** One remaining data discrepancy: Figure S7 Gemini Pro Beginner/Advanced values (6.7%/6.7%) conflict with SR3 and Table S8 (0%/13.3%).

---

## V4: Figure Files on Disk — PASS (with expected gaps)

Files present in `PAPER-V2/figures/`:

| File | Status |
|------|--------|
| fig1-tradition-heatmap.png | Present |
| fig2-tradition-distribution.png | Present |
| fig3-rd-vs-pe-scatter.png | Present |
| fig4-data-availability.png | Present |
| fig5-bootstrap-ci-forest.png | Present |
| fig6-void-factor-radar.png | Present |
| fig7-values-relevance-histogram.png | Present |
| fig8-claim-robustness.png | Present |
| fig9-gate-threshold-sensitivity.png | Present |
| fig10-cross-model-gradient.png | Present |
| fig11-rubric-heatmap.png | Present |
| fig12-t2-accuracy.png | Present |
| fig13-vendor-radar.png | Present |
| fig-s3-correlation-heatmap.png | Present |
| fig-s4-tradition-gradient.png | Present |
| fig-s5-cross-vendor-length.png | Present |
| fig-s7-t2-beginner-advanced.png | Present |
| fig-s8-year-distribution.png | Present |

**Figures 1–9:** All present (copied from PAPER/figures/). CONFIRMED.
**Figures 10–13:** All present. CONFIRMED.
**Figures S4, S5, S7, S8:** All present. CONFIRMED.
**Figure S3:** Present. CONFIRMED.

**Expected missing (marked [IMAGE NOT YET GENERATED] in 08-supp-figures.md):**
- Figure S2 (Gate Threshold Sensitivity Curves Extended) — absent, as expected
- Figure S6 (Bias-Values Scatter Plots Per Model) — absent, as expected

**Note:** Figure S1 (PRISMA) is not in `PAPER-V2/figures/` — it exists only at `PAPER/fig-prisma-flow.png`. This is a minor organizational gap but not a breakage since the paper can still reference it.

**Verdict: PASS.** All expected files present; S2 and S6 are correctly documented as not yet generated.

---

## V5: Supplementary Back-References — PASS

SR1–SR4 in 06-supp-results.md now contain back-references to the main text:

| SR Section | Back-Reference | Status |
|------------|---------------|--------|
| SR1 | "see Section 4.5" (line 7) | PRESENT |
| SR2 | "reported in Section 4.5" (line 37) | PRESENT |
| SR3 | "see Sections 4.5--4.6" (line 59) | PRESENT |
| SR4 | "see Sections 4.5--4.6" (line 89) | PRESENT |

**Verdict: PASS.** All SR1–SR4 sections have explicit back-references to Sections 4.5–4.6 of the main text.

---

## V6: Intra-Supplementary Cross-References — PASS

Cross-references between supplementary sections are correctly maintained:

| Source | Target | Status |
|--------|--------|--------|
| SR1 (line 7) | "Section 4.5" | Valid |
| SR2 (line 37) | "Section 3.5.3" (rubric scales) | Valid |
| SR3 (line 59) | "Sections 4.5--4.6" | Valid |
| SR4 (line 89) | "Sections 4.5--4.6" | Valid |
| SR5 (line 113) | "Section 4.3" (implicit via void tradition analysis) | Valid |
| SR6 (line 171) | No explicit back-ref but topic matches Section 4.2 | Acceptable |
| SR7 (line 202) | "Sections 4.3 and 5.6" (implicit via WEIRD analysis) | Valid |
| SR8 (line 233) | Sensitivity analysis matches Section 3.3 | Valid |
| 05-supp-methods.md S1–S7 | "Section 3" (line 3), "Section 3.7" (line 128), "Section 3.5.6" (line 179) | Valid |
| 08-supp-figures.md | Individual figures reference specific sections and SR numbers | Valid |

**Verdict: PASS.** Intra-supplementary cross-references are consistent and resolve correctly.

---

## Summary: 5 of 6 checks PASS

| Check | Result | Details |
|-------|--------|---------|
| V1: Section References | **PASS** | Zero broken refs; broad "Section 4" refs are contextually appropriate |
| V2: Table References | **PASS** | All Table N and Table SN refs resolve; "(Table S6)" correctly replaced |
| V3: Figure References | **FAIL** | Fig 11/12 descriptions fixed; Fig S7 Haiku/Flash fixed; **Gemini Pro Beg/Adv still wrong (6.7%/6.7% vs 0%/13.3%)** |
| V4: Figure Files on Disk | **PASS** | Figs 1–13, S3–S5, S7–S8 present; S2/S6 expected missing |
| V5: Supplementary Back-Refs | **PASS** | SR1–SR4 all reference Sections 4.5–4.6 |
| V6: Intra-Supp Cross-Refs | **PASS** | All supplementary cross-references consistent |

### Remaining Issue (1 item)

**Figure S7 Gemini Pro data error (08-supp-figures.md:117):**
- Current: "Gemini Pro: 6.7%/6.7%"
- Should be: "Gemini Pro: Beginner 0%, Advanced 13.3%"
- Sources: SR3 (06-supp-results.md:72) reports 0/15 Beginner, 2/15 Advanced; Table S8 (07-supp-tables.md:211) confirms 0% / 13.3%.
