# Synthesis Report

**Date:** 2026-04-12
**Input:** 6 expert reports (E1-E6)
**Output:** Deduplicated, prioritized fix list with batch assignments

---

## Validation

| Expert | File | Size | Findings | Status |
|--------|------|------|----------|--------|
| E1 (Transitions) | expert-1-transitions.md | ~14KB | 26 (4C, 12M, 10Mi) | VALID |
| E2 (Claims/Stats) | expert-2-claims.md | ~11KB | 18 (1C, 3M, 14Mi) | VALID |
| E3 (Supplementary) | expert-3-supplementary.md | ~14KB | 13 (4C, 4M, 5Mi) | VALID |
| E4 (Citations) | expert-4-citations.md | ~18KB | 14 (4C, 2M, 8Mi) | VALID |
| E5 (Context) | expert-5-context.md | ~27KB | 50 (2C, 7M, 41Mi) | VALID |
| E6 (Cross-refs) | expert-6-crossrefs.md | ~14KB | 9 (2C, 4M, 3Mi) | VALID |

All 6 reports exist, contain substantive content (>500 bytes each), and include structured findings with severity ratings.

---

## Issue Census

### By Severity x Expert (raw, pre-dedup)

| Expert | CRITICAL | MAJOR | MINOR | Total |
|--------|----------|-------|-------|-------|
| E1 | 4 | 12 | 10 | 26 |
| E2 | 1 | 3 | 14 | 18 |
| E3 | 4 | 4 | 5 | 13 |
| E4 | 4 | 2 | 8 | 14 |
| E5 | 2 | 7 | 41 | 50 |
| E6 | 2 | 4 | 3 | 9 |
| **Raw Total** | **17** | **32** | **81** | **130** |

### By Severity x Category (post-dedup)

| Category | CRITICAL | MAJOR | MINOR | Total |
|----------|----------|-------|-------|-------|
| Data-Consistency | 3 | 1 | 1 | 5 |
| Figure-Numbering/Content | 1 | 0 | 0 | 1 |
| Figure-File (missing/mislocated) | 1 | 0 | 0 | 1 |
| Missing-Bib | 4 | 0 | 0 | 4 |
| Misattributed-Citation | 2 | 0 | 0 | 2 |
| Table-Ref Mismatch | 1 | 0 | 0 | 1 |
| Count Inconsistency | 0 | 3 | 2 | 5 |
| Overclaim | 1 | 2 | 2 | 5 |
| Sec1-2-Dependency | 0 | 5 | 1 | 6 |
| Transition | 0 | 2 | 2 | 4 |
| Unsupported-Claim | 0 | 1 | 7 | 8 |
| Anti-Essentialization | 0 | 0 | 1 | 1 |
| Cross-Ref (broad refs) | 0 | 1 | 3 | 4 |
| Bib-Completeness | 0 | 2 | 3 | 5 |
| Citation-Concentration | 0 | 0 | 2 | 2 |
| P-Value/Stat Precision | 0 | 0 | 5 | 5 |
| Back-Ref (supp) | 0 | 1 | 3 | 4 |
| **Dedup Total** | **13** | **18** | **32** | **63** |

---

## Deduplicated Issues (Prioritized)

### CRITICAL

**C1. Tier 1 Islamic benchmark count: 9 vs 8**
- Sources: E2-F1
- Location: 02-results.md:85, 00-abstract.md:7, 03-discussion.md:9
- Issue: Table 2 lists 9 Islamic benchmarks in Tier 1, but prose says "8 of 11." Must reconcile.
- Fix: Count benchmarks in Table 2, correct prose everywhere (abstract, results, discussion) to match.
- Batch: 3
- Dependencies: Resolving C2 (Antisemitism Detection tier) may change Tier 1 total count.

**C2. Antisemitism Detection (p=0.840) placed in Tier 2 instead of Tier 1**
- Sources: E2-F11, E2-F14
- Location: 02-results.md (Table 2), 01-methods.md:15 (PRISMA)
- Issue: p=0.840 >= 0.80 threshold for Tier 1. Either the p-value or tier assignment is wrong. Cascades to all tier counts (currently "11 Tier 1, 4 Tier 2, 10 Tier 3").
- Fix: Verify bootstrap probability. If p=0.840 is correct, move to Tier 1 and update all tier counts. If Tier 2 is correct, fix p-value.
- Batch: 3
- Dependencies: C1 depends on this resolution. All tier count mentions cascade.

**C3. Figure S7 Haiku T2 data values wrong**
- Sources: E3-F1, E3-F2, E6-F2 (MERGED -- 3 experts flagged overlapping aspects)
- Location: 08-supp-figures.md:115-117
- Issue: Figure S7 states Haiku Beginner=86.7%, Advanced=66.7%. All other sources (Table 9, Table 10, SR3, Table S8) report 80%/73.3%. The "20-percentage-point drop" narrative is also wrong (actual: 6.7pp).
- Fix: Correct data values to Beginner=80.0%, Advanced=73.3%. Rewrite narrative: "6.7-percentage-point drop."
- Batch: 2
- Dependencies: None.

**C4. Figure S7 Gemini Flash Beginner/Advanced swapped**
- Sources: E3-F3
- Location: 08-supp-figures.md:115
- Issue: Figure S7 lists "Gemini Flash: 13.3%/6.7%" but SR3/S8 report Beginner=6.7%, Advanced=13.3%.
- Fix: Correct to "Gemini Flash: Beginner 6.7%, Advanced 13.3%."
- Batch: 2
- Dependencies: None.

**C5. Figure 11/12 content descriptions wrong in main text**
- Sources: E3-F4, E6-F1 (MERGED -- both flagged same mismatch)
- Location: 02-results.md:287
- Issue: Text says Fig 11 = "rubric ceiling + T2 contrast" and Fig 12 = "bias-values independence." Actually Fig 11 = Cross-Vendor Rubric Heatmap, Fig 12 = T2 Accuracy by Model, and bias-values is Figure S6.
- Fix: Correct descriptions to match actual figure content. Add reference to Figure S6 for bias-values.
- Batch: 2
- Dependencies: None.

**C6. Table S6 reference mismatch**
- Sources: E3-F5, E3-F12, E6-Supp (MERGED -- flagged by both E3 and E6)
- Location: 01-methods.md:123
- Issue: Text says "Table S6" for sensitivity/leave-one-out results, but Table S6 is "Cross-Model Response Length Gradient." Actual sensitivity results are in SR6 and SR8.
- Fix: Change "(Table S6)" to "(Supplementary Results SR6, SR8)."
- Batch: 2
- Dependencies: None.

**C7. Missing bib entry: Cohen1988**
- Sources: E4-F1, E5-F9 (MERGED)
- Location: 01-methods.md:216
- Issue: \cite{Cohen1988} has no bib entry. Foundational statistics reference for effect size thresholds.
- Fix: Add @book{Cohen1988, author={Cohen, Jacob}, title={Statistical Power Analysis for the Behavioral Sciences}, year={1988}, edition={2nd}, publisher={Lawrence Erlbaum Associates}}.
- Batch: 1
- Dependencies: None.

**C8. Missing bib entry: Kulkarni2022**
- Sources: E4-F2, E5-F21 (MERGED)
- Location: 02-results.md:124
- Issue: \cite{Kulkarni2022} has no bib entry. References Bhagavad Gita Sentiment Analysis benchmark.
- Fix: Identify exact paper and add bib entry.
- Batch: 1
- Dependencies: None.

**C9. Missing bib entry: Nida1964**
- Sources: E4-F3, E5-F1 (MERGED)
- Location: 01-methods.md:27
- Issue: \cite{Nida1964} has no bib entry. Eugene Nida's foundational translation theory work.
- Fix: Add @book{Nida1964, author={Nida, Eugene A.}, title={Toward a Science of Translating}, year={1964}, publisher={E.J. Brill}}.
- Batch: 1
- Dependencies: None.

**C10. Missing bib entry: Zhang2024**
- Sources: E4-F4, E5-F3 (MERGED)
- Location: 01-methods.md:91
- Issue: \cite{Zhang2024} has no bib entry. Context: "emerging work on theological dialogue systems."
- Fix: Either identify exact paper and add bib entry, or remove citation and rephrase.
- Batch: 1
- Dependencies: None.

**C11. Misattributed citation: ELQV cited as Alharbi2024 (IslamicMMLU)**
- Sources: E5-F14
- Location: 02-results.md:79
- Issue: ELQV \cite{Alharbi2024} but Alharbi2024 is IslamicMMLU. These are different benchmarks.
- Fix: Add correct ELQV bib entry with its own key; fix citation at this location.
- Batch: 1
- Dependencies: New bib entry must be added first.

**C12. Misattributed citation: Francis2015 (Laudato Si') used for Rome Call for AI Ethics**
- Sources: E5-F18
- Location: 02-results.md:116
- Issue: \cite{Francis2015} = Laudato Si' (environmental encyclical), NOT Rome Call for AI Ethics. RomeCall2020 exists in bib but is uncited.
- Fix: Replace \cite{Francis2015} with \cite{RomeCall2020}.
- Batch: 1
- Dependencies: None.

**C13. Figures 1-9 not in PAPER-V2/figures/ directory**
- Sources: E6-F3
- Location: 08-supp-figures.md (all Figs 1-9 reference PAPER/figures/ paths)
- Issue: Figures 1-9 exist only in PAPER/figures/, not PAPER-V2/figures/. Paper is not self-contained.
- Fix: Copy or symlink Figures 1-9 from PAPER/figures/ to PAPER-V2/figures/.
- Batch: 2
- Dependencies: None.

---

### MAJOR

**M1. Gate-passer intermediate count inconsistency (46 vs 47)**
- Sources: E2-F2
- Location: 02-results.md:15 vs 01-methods.md:15
- Issue: Results says "355 eliminated, leaving 46" but Methods PRISMA says "47 initial, 2 removed = 45." Results only mentions BuddhismEval removal, omitting Break the Checkbox.
- Fix: Harmonize arithmetic. If 47 is correct: change "355" to "354" and "88.5%" to "88.3%" in Results. Add Break the Checkbox to removal note.
- Batch: 3
- Dependencies: None.

**M2. Statistical tests use n=47 (pre-removal) without explicit justification**
- Sources: E2-F9
- Location: 02-results.md, 07-supp-tables.md
- Issue: All 8 statistical tests use n=47 but final count is 45. Not documented.
- Fix: Add note in Section 4.4 or 3.6 that all tests use pre-removal sample of n=47.
- Batch: 3
- Dependencies: None.

**M3. CI feature count discrepancy: 4 vs 5 in leave-one-out**
- Sources: E3-F6
- Location: 06-supp-results.md:171-175, 05-supp-methods.md:261
- Issue: LOO analysis claims "16 active features (6 RD + 6 PE + 4 CI)" but CI has 5 weighted features (C2-C6). C6 (Community Engagement) omitted from LOO table.
- Fix: Either add C6 to LOO table and correct to "17 features (6+6+5)" or explain exclusion.
- Batch: 3
- Dependencies: None.

**M4. Robust benchmark count: 11 (main) vs 13 (SR8a)**
- Sources: E3-Data Consistency Summary
- Location: 02-results.md vs 06-supp-results.md (SR8a)
- Issue: Main text says 11 Tier 1 (p>=0.80), SR8a says 13 robust. May reflect pre-removal count.
- Fix: Clarify in SR8a whether count is pre- or post-removal. Reconcile with main text.
- Batch: 3
- Dependencies: C2 (Antisemitism Detection tier) affects this count.

**M5. Figure S2 and Figure S6 missing from disk**
- Sources: E6-F4
- Location: 08-supp-figures.md descriptions exist but no image files
- Issue: Figure S2 (Gate Threshold Sensitivity Extended) and Figure S6 (Bias-Values Scatter Plots Per Model) are described but have no image files anywhere.
- Fix: Generate the figures, or remove descriptions from 08-supp-figures.md.
- Batch: 2
- Dependencies: C5 references Figure S6 for bias-values content.

**M6. "Expert council" undefined entity**
- Sources: E1-F24
- Location: 03-discussion.md:25
- Issue: "The expert council's finding" introduces an undefined entity. Methods describe single-author scoring. If this refers to an AI-mediated review process, it must be described transparently.
- Fix: Replace "The expert council's finding" with "Our analysis finds" or define what "expert council" means in Methods.
- Batch: 3
- Dependencies: None.

**M7. "Cognitive demand" overclaim in Abstract**
- Sources: E1-F18
- Location: 00-abstract.md:7
- Issue: "cognitive demand on generative models" implies causal mechanism. Evidence is only response length (behavioral proxy). Paper itself acknowledges this limitation.
- Fix: Replace "cognitive demand" with "generative effort" or add hedge.
- Batch: 3
- Dependencies: Also fix body text at M8.

**M8. "Cognitive demands" overclaim in body text**
- Sources: E1-F20
- Location: 02-results.md:241
- Issue: Same overclaim as M7 but in Results section.
- Fix: Replace "impose progressively greater cognitive demands" with "elicit progressively more elaborate responses."
- Batch: 3
- Dependencies: Fix alongside M7 for consistency.

**M9. K<R<V gradient called "universal" without qualifier**
- Sources: E1-F19
- Location: 02-results.md:213
- Issue: "The gradient is universal" but it fails for GPT-Codex and Gemini models. Only universal within Claude family.
- Fix: Change to "The gradient is universal within the Claude model family."
- Batch: 3
- Dependencies: None.

**M10. Discussion opening preview omits Sections 5.5 and 5.6**
- Sources: E1-F26
- Location: 03-discussion.md:5
- Issue: Discussion preview mentions specific->structural->actionable but skips 5.5 (Values Relevance Failure) and 5.6 (Publication Infrastructure).
- Fix: Expand preview to mention all major subsections.
- Batch: 3
- Dependencies: None.

**M11. Thesis statement first appears in Discussion (Section 5, para 2)**
- Sources: E1-F16
- Location: 03-discussion.md:5
- Issue: Central thesis ("most benchmarks test knowledge recall...almost none test values reasoning") appears first in Discussion. Needs to be previewed when Introduction is written.
- Fix: When Introduction is written, state thesis as hypothesis. Add note for Section 1 draft.
- Batch: 4 (deferred to Sec 1-2 writing)
- Dependencies: Requires Introduction section.

**M12. NormEval "sister survey" undefined relationship**
- Sources: E1-F6
- Location: 03-discussion.md:29
- Issue: NormEval called "sister survey" with no introduction of the relationship. Cited as \cite{Hendrycks2021} but that's MMLU, not NormEval.
- Fix: Add NormEval bib entry. Clarify relationship in text. Fix citation key.
- Batch: 1 (bib) + 3 (prose)
- Dependencies: C7-C10 pattern (missing bib).

**M13. Hendrycks2021 (MMLU) cited for NormEval 28/37 statistic**
- Sources: E5-F26
- Location: 03-discussion.md:29
- Issue: "28 of 37 benchmarks test moral judgment rather than moral reasoning \cite{Hendrycks2021}" -- MMLU is not the source of this statistic.
- Fix: Replace with NormEval citation or clarify this is the authors' own analysis.
- Batch: 1 (bib) + 3 (prose)
- Dependencies: M12.

**M14. "80% of world's population" uncited**
- Sources: E5-F35
- Location: 00-abstract.md:3
- Issue: Major empirical claim with no citation. PewResearch2017 is in bib and supports this.
- Fix: Add \cite{PewResearch2017} after the claim.
- Batch: 1
- Dependencies: None.

**M15. Conclusion Calls to Action don't cover all Discussion findings**
- Sources: E1-F15
- Location: 04-conclusion.md:13-23
- Issue: Discussion Sections 5.1, 5.3, 5.5, 5.8, 5.9 don't directly motivate any Call to Action. Rubric ceiling paradox (5.3) is a major finding without a corresponding call.
- Fix: Either add a 5th call addressing rubric redesign or explicitly link 5.3 to existing calls.
- Batch: 3
- Dependencies: None.

**M16. Bib entry TuckYang2012 incomplete (cited, missing venue)**
- Sources: E4-F10
- Location: religious-values-benchmarks.bib
- Issue: @misc with no journal. Published in Decolonization: Indigeneity, Education & Society.
- Fix: Change to @article, add journal/volume/pages.
- Batch: 1
- Dependencies: None.

**M17. Bib entry MofenjouPeuriekeu2024 incomplete (uncited, no venue)**
- Sources: E4-F9
- Location: religious-values-benchmarks.bib
- Issue: @misc with no journal/doi/url. Currently uncited.
- Fix: Add venue information or howpublished field.
- Batch: 1
- Dependencies: Lower priority (uncited).

**M18. Supplementary back-references incomplete**
- Sources: E3-F8
- Location: 06-supp-results.md (SR1-SR4)
- Issue: SR1/SR2 lack back-references to Section 4.5; SR3/SR4 lack back-references to 4.5-4.6.
- Fix: Add "see Section 4.5" / "see Sections 4.5-4.6" in relevant SR sections.
- Batch: 2
- Dependencies: None.

---

### MINOR

**Mi1. Precision variation: V=0.53 (main) vs V=0.526 (Table S9)**
- Sources: E2-F3
- Fix: Standardize (V=0.53 in main, V=0.526 in supplement). Add note if needed.
- Batch: 4

**Mi2. Precision variation: d=-1.23 (main) vs d=-1.232 (Table S9)**
- Sources: E2-F4
- Fix: Standardize (d=-1.23 in main, d=-1.232 in supplement).
- Batch: 4

**Mi3. C8d p-value mismatch: 0.00002 (Table S9) vs 0.000015 (Results)**
- Sources: E2-F17
- Fix: Verify exact value and unify.
- Batch: 3

**Mi4. P-value reporting inconsistency within Results (exact for C8, inequality for C1/C3)**
- Sources: E2-F5
- Fix: Standardize convention within Results section.
- Batch: 4

**Mi5. C8c Bonferroni failure not flagged in Results prose**
- Sources: E2-F15
- Fix: Add parenthetical noting C8c does not survive Bonferroni correction.
- Batch: 3

**Mi6. Construct validity battery decomposition unclear (45+20 vs 15K+15R+25V+10B)**
- Sources: E2-F10
- Fix: Add parenthetical in Methods clarifying 25V = 15 core + 10 matched-pair.
- Batch: 3

**Mi7. Opus V/K ratio: 3.42x (Fig 10) vs 3.41x (all other sources)**
- Sources: E3-F7
- Fix: Correct Fig 10 to 3.41x.
- Batch: 2

**Mi8. Figure S2 vague back-reference ("Supplementary Results" unspecified)**
- Sources: E3-F9
- Fix: Change to "Supplementary Results SR8."
- Batch: 2

**Mi9. Figure S5 vague back-reference**
- Sources: E3-F10
- Fix: Change to "Supplementary Results SR1."
- Batch: 2

**Mi10. Figure S8 not reciprocally referenced from Section 4.1**
- Sources: E3-F11
- Fix: Add explicit "Figure S8" reference in Section 4.1 or update figure description.
- Batch: 2

**Mi11. Figures 10-12 referenced in 02-results.md:257 may be dangling**
- Sources: E1-F13
- Note: E6 registry confirms Figs 10-12 exist. However, the reference at line 257 (Section 4.5) may need to say "Supplementary Figures" if these are in the supplement. Cross-check numbering.
- Batch: 2

**Mi12. Section 4 broad reference (should be 4.1 or 4.3)**
- Sources: E6-F5
- Location: 01-methods.md:36
- Fix: Change "Section 4" to "Section 4.1" or "Section 4.3."
- Batch: 2

**Mi13. Table S5 Section 4 broad reference (should be more specific)**
- Sources: E6-F7
- Location: 07-supp-tables.md:123
- Fix: Change "Section 4" to "Sections 4.1-4.4."
- Batch: 2

**Mi14. SR7 references Section 4.3 but 5.6 more precise**
- Sources: E6-F9
- Fix: Add "Section 5.6" alongside existing 4.3 reference.
- Batch: 2

**Mi15. Methods->Results transition abrupt**
- Sources: E1-F2
- Fix: Add bridging sentence at top of Section 4.
- Batch: 4

**Mi16. Conclusion repeats statistics verbatim (3rd time for reader)**
- Sources: E1-F14
- Fix: Condense Central Paradox subsection by ~30%.
- Batch: 4

**Mi17. "Establish proof-of-concept" overclaim**
- Sources: E1-F21
- Location: 02-results.md:373
- Fix: Change "establish" to "provide."
- Batch: 4

**Mi18. "Are required" overclaim for T2 format**
- Sources: E1-F22
- Location: 02-results.md:331
- Fix: Change "are required" to "may be necessary."
- Batch: 4

**Mi19. Rubric keyword hypothesis unsupported**
- Sources: E1-F23
- Location: 03-discussion.md:43
- Fix: Label as hypothesis requiring future empirical validation.
- Batch: 4

**Mi20. Ubuntu/Indigenous essentialization risk**
- Sources: E1-F25
- Location: 02-results.md:140
- Fix: Add qualifier about internal diversity.
- Batch: 4

**Mi21. Section 3.4 forward reference too broad**
- Sources: E1-F10
- Location: 01-methods.md:127
- Fix: Change "Section 4" to "Section 4.1 and Section 4.4, Claim 8."
- Batch: 2

**Mi22. Abstract methods summary skips Section 3.4 (meta-evaluation criteria)**
- Sources: E1-F1
- Fix: Add brief clause about meta-evaluation criteria.
- Batch: 4

**Mi23. Bib entry ZhaoLiu2015 incomplete (uncited)**
- Sources: E4-F11
- Fix: Add venue information.
- Batch: 1

**Mi24. Bib entry Mhlambi2020 wrong type (journal = institution)**
- Sources: E4-F12
- Fix: Change to @techreport with institution field.
- Batch: 1

**Mi25. Bib entry Rosenfeld2021 @article with no journal**
- Sources: E4-F13
- Fix: Add journal={arXiv} to match bib conventions.
- Batch: 1

**Mi26. Abstract field characterization uncited**
- Sources: E5-F36
- Location: 00-abstract.md:3
- Fix: Add \cite{Gabriel2020, Ji2024} for field characterization.
- Batch: 4

**Mi27. Gulf state AI strategies uncited**
- Sources: E5-F37
- Location: 02-results.md:112
- Fix: Add citation or note specific programs.
- Batch: 4

**Mi28. Bar-Ilan Responsa Project uncited**
- Sources: E5-F38
- Location: 02-results.md:118
- Fix: Add citation.
- Batch: 4

**Mi29. IRT terminology uncited**
- Sources: E5-F39
- Location: 03-discussion.md:43
- Fix: Add \cite{Srivastava2024}.
- Batch: 4

**Mi30. MUKURTU CMS and Local Contexts uncited**
- Sources: E5-F40
- Location: 03-discussion.md:131
- Fix: Add URL or citation.
- Batch: 4

**Mi31. Sefaria digital library uncited**
- Sources: E5-F41
- Location: 04-conclusion.md:15
- Fix: Add URL.
- Batch: 4

**Mi32. Chinese Classics Digital Library uncited**
- Sources: E5-F42
- Location: 04-conclusion.md:15
- Fix: Add URL.
- Batch: 4

---

## Deduplication Notes

The following overlapping findings were merged:

1. **Figure S7 Haiku data error**: E3-F1, E3-F2, E6-F2 all flagged incorrect Haiku values in Fig S7. Merged into C3. E3 provided the most detail (both data values and narrative text).

2. **Figure 11/12 content mismatch**: E3-F4 and E6-F1 both flagged the same issue at 02-results.md:287. Merged into C5. E3 provided the corrected mapping.

3. **Table S6 mislabel**: E3-F5, E3-F12, and E6-Supp all flagged the same reference. Merged into C6.

4. **Missing bib entries (Cohen1988, Kulkarni2022, Nida1964, Zhang2024)**: E4 and E5 both independently identified all 4 missing entries. Merged into C7-C10. E4 provided bib-level detail; E5 provided citation context evaluation.

5. **Francis2015 misattribution**: Only E5-F18 flagged this, but it overlaps with E4's scope. Elevated to CRITICAL as a misattribution.

6. **ELQV/Alharbi2024 misattribution**: Only E5-F14 flagged this. Elevated to CRITICAL.

---

## Conflict Resolution

### Conflict 1: Gate-passer count (46 vs 47)
- E2-F2 identified the arithmetic inconsistency: Results says 401-355=46, Methods says 47.
- **Resolution:** The Methods PRISMA flow (47 initial, 2 removed) is the authoritative pipeline description. Results should say 401-354=47 (changing "355" to "354"). The 2 post-review removals (Break the Checkbox + BuddhismEval) then yield 45.

### Conflict 2: Robust benchmark count (11 vs 13)
- E3 noted SR8a reports 13 robust (p>=0.80) vs main text's 11.
- **Resolution:** SR8a likely uses pre-removal count (13 includes 2 removed benchmarks). After removal, 11 remain. Clarify in SR8a. However, C2 (Antisemitism Detection) may change this to 12 if moved to Tier 1. Resolution depends on C2.

### Conflict 3: No inter-expert disagreements
- All experts agreed on severity ratings where findings overlapped. No conflicts required adjudication.

---

## Dependency Map

```
C2 (Antisemitism Detection tier)
  |-> C1 (Islamic Tier 1 count -- final number depends on C2)
  |-> M4 (Robust benchmark count 11 vs 13)
  |-> All prose mentions of "11 Tier 1, 4 Tier 2, 10 Tier 3"

C7-C10 (Missing bib entries)
  |-> E5 citation context fixes (can't verify relevance without entries)

C11 (ELQV misattribution)
  |-> Requires new bib entry for ELQV

M12 (NormEval relationship)
  |-> M13 (Hendrycks2021 wrong source for 28/37 stat)
  |-> Both require NormEval bib entry

M7 (Cognitive demand overclaim, abstract)
  |-> M8 (Same overclaim, body text) -- fix together for consistency

C5 (Figure 11/12 description)
  |-> M5 (Figure S6 missing from disk) -- bias-values figure needed
```

---

## Batch Assignments

### Batch 1 -- Bibliography (Round A, parallel)
**Scope:** Missing bib entries, misattributed citations, bib completeness

| # | Issue | Action |
|---|-------|--------|
| C7 | Cohen1988 missing | Add @book entry |
| C8 | Kulkarni2022 missing | Identify paper, add entry |
| C9 | Nida1964 missing | Add @book entry |
| C10 | Zhang2024 missing | Add entry or remove citation |
| C11 | ELQV misattributed as Alharbi2024 | Add ELQV bib entry, fix citation |
| C12 | Francis2015 -> RomeCall2020 | Replace citation key |
| M12 | NormEval missing from bib | Add NormEval bib entry |
| M14 | "80%" uncited | Add \cite{PewResearch2017} |
| M16 | TuckYang2012 incomplete | Add journal/volume/pages |
| M17 | MofenjouPeuriekeu2024 incomplete | Add venue info |
| Mi23 | ZhaoLiu2015 incomplete | Add venue info |
| Mi24 | Mhlambi2020 wrong type | Change to @techreport |
| Mi25 | Rosenfeld2021 no journal | Add journal={arXiv} |

**13 items. Expected output: updated .bib file + 3 citation fixes in .md files.**

### Batch 2 -- Cross-References (Round A, parallel)
**Scope:** Broken section/table/figure refs, figure file issues, supplementary coherence

| # | Issue | Action |
|---|-------|--------|
| C3 | Fig S7 Haiku data wrong | Fix data values + narrative |
| C4 | Fig S7 Gemini Flash swapped | Fix data values |
| C5 | Fig 11/12 descriptions wrong | Correct descriptions in 02-results.md:287 |
| C6 | Table S6 reference mismatch | Change to SR6/SR8 in 01-methods.md:123 |
| C13 | Figs 1-9 not in PAPER-V2/figures/ | Copy/symlink from PAPER/figures/ |
| M5 | Fig S2, S6 missing from disk | Generate or remove descriptions |
| M18 | SR back-references incomplete | Add Section 4.5/4.6 refs to SR1-SR4 |
| Mi7 | Opus V/K ratio 3.42x -> 3.41x | Fix in Fig 10 description |
| Mi8 | Fig S2 vague back-ref | Specify SR8 |
| Mi9 | Fig S5 vague back-ref | Specify SR1 |
| Mi10 | Fig S8 not reciprocally referenced | Add ref in Section 4.1 |
| Mi11 | Figs 10-12 ref at 02-results.md:257 | Verify numbering context |
| Mi12 | "Section 4" too broad (01-methods.md:36) | Narrow to 4.1 or 4.3 |
| Mi13 | "Section 4" too broad (07-supp-tables.md:123) | Narrow to 4.1-4.4 |
| Mi14 | SR7 ref could add Section 5.6 | Add cross-ref |
| Mi21 | Section 3.4 forward ref too broad | Narrow to 4.1 and 4.4 |

**16 items. Expected output: fixes across 08-supp-figures.md, 02-results.md, 01-methods.md, 06-supp-results.md, 07-supp-tables.md; figure files copied.**

### Batch 3 -- Narrative & Data (Round A, parallel)
**Scope:** Count inconsistencies, tier corrections, overclaims, data corrections, undefined entities

| # | Issue | Action |
|---|-------|--------|
| C1 | Islamic Tier 1 count 8 vs 9 | Reconcile prose with Table 2 |
| C2 | Antisemitism Detection tier | Verify p-value, fix tier or value |
| M1 | Gate-passer count 46 vs 47 | Fix arithmetic in Results |
| M2 | n=47 pre-removal not documented | Add justification note |
| M3 | CI feature count 4 vs 5 | Add C6 to LOO or explain |
| M4 | Robust benchmark count 11 vs 13 | Clarify in SR8a |
| M6 | "Expert council" undefined | Replace or define |
| M7 | "Cognitive demand" overclaim (abstract) | Hedge language |
| M8 | "Cognitive demands" overclaim (body) | Hedge language |
| M9 | "Universal" gradient without qualifier | Add "within Claude family" |
| M10 | Discussion preview incomplete | Expand preview |
| M13 | Hendrycks2021 wrong for NormEval stat | Fix citation (after Batch 1 adds entry) |
| M15 | Calls to Action coverage gap | Link 5.3 to existing calls or add 5th |
| Mi3 | C8d p-value mismatch | Verify and unify |
| Mi5 | C8c Bonferroni failure not flagged | Add parenthetical |
| Mi6 | Battery decomposition unclear | Add clarifying parenthetical |

**16 items. Expected output: fixes across 00-abstract.md, 01-methods.md, 02-results.md, 03-discussion.md, 04-conclusion.md, 05-supp-methods.md, 06-supp-results.md.**

### Batch 4 -- Enhancements (Round B, sequential after Round A)
**Scope:** MINOR hedging, citation density, polish

| # | Issue | Action |
|---|-------|--------|
| M11 | Thesis preview (deferred to Sec 1-2) | Note for Introduction draft |
| Mi1 | V precision variation | Standardize |
| Mi2 | d precision variation | Standardize |
| Mi4 | P-value reporting convention | Standardize |
| Mi15 | Methods->Results transition | Add bridging sentence |
| Mi16 | Conclusion stat repetition | Condense ~30% |
| Mi17 | "Establish" overclaim | Change to "provide" |
| Mi18 | "Are required" overclaim | Change to "may be necessary" |
| Mi19 | Rubric keyword hypothesis | Label as hypothesis |
| Mi20 | Ubuntu/Indigenous essentialization | Add diversity qualifier |
| Mi22 | Abstract skips Sec 3.4 | Add meta-evaluation mention |
| Mi26 | Field characterization uncited | Add citations |
| Mi27 | Gulf state strategies uncited | Add citation/note |
| Mi28 | Bar-Ilan Responsa uncited | Add citation |
| Mi29 | IRT terminology uncited | Add \cite{Srivastava2024} |
| Mi30 | MUKURTU/Local Contexts uncited | Add URL |
| Mi31 | Sefaria uncited | Add URL |
| Mi32 | Chinese Classics uncited | Add URL |

**18 items. Expected output: minor text edits across all main files.**

---

## Execution Plan Summary

| Round | Batches | Items | Parallelizable |
|-------|---------|-------|----------------|
| A | 1 (Bib) + 2 (Cross-refs) + 3 (Narrative) | 13 + 16 + 16 = 45 | Yes (3 parallel) |
| B | 4 (Enhancements) | 18 | Sequential |
| **Total** | | **63** | |

**Note:** Batch 3 issue M13 (Hendrycks2021 fix) has a soft dependency on Batch 1 (NormEval bib entry). The Batch 3 agent should use a placeholder citation key if the Batch 1 agent hasn't completed yet, or the Batch 3 agent should handle M13 last.
