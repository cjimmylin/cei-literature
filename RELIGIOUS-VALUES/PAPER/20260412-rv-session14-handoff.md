# Religious Values Benchmark Paper — Session 14 Handoff

**Date:** 2026-04-12
**Session:** 6-expert council review: narrative arc + bibliography verification
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`
**Previous handoff:** `PAPER/20260405c-rv-session13-bugfixes-handoff.md`

---

## What Was Done This Session

### Council Architecture
A 6-expert review council was assembled, critiqued by a 6-expert meta-council, and then executed across 4 phases:

| Phase | Description | Agents |
|-------|-------------|--------|
| 1. Review | 6 parallel expert agents (read-only) | 6 |
| 2. Synthesis | Deduplication, conflict resolution, priority ranking | 1 |
| 3. Execute | Round A (3 parallel batches) + Round B (1 sequential batch) | 3+1 |
| 4. Verify | Re-run Experts 2, 4, 6 + manual residual fixes | 3 |
| **Total** | | **14 agents** |

### Review Council Experts
1. **Transition Architect** — narrative flow, anti-essentialization, overclaims
2. **Claims & Statistical Consistency** — 8 claims traced, stats, interpretation drift
3. **Supplementary Coherence** — main↔supp correspondence, intra-supp refs
4. **Citation Completeness** — mechanical \cite vs .bib cross-check
5. **Citation Context** — semantic relevance of each citation
6. **Cross-Reference Integrity** — Section/Table/Figure validation

### Issue Census
- **130 raw findings** across 6 experts
- **63 unique issues** after deduplication (13 CRITICAL, 18 MAJOR, 32 MINOR)
- **63/63 resolved** (100%)
- **All 6 verification gates PASS**

### CRITICAL Issues Resolved (13)

| # | Issue | Fix |
|---|-------|-----|
| C1 | Islamic Tier 1 count 8→9 | Reconciled with Table 2 after C2 |
| C2 | Antisemitism Detection (p=0.840) in wrong tier | Moved to Tier 1; all counts updated (12/3/10) |
| C3 | Figure S7 Haiku data wrong (86.7%/66.7%) | Corrected to 80.0%/73.3%, narrative to 6.7pp |
| C4 | Figure S7 Gemini Flash Beg/Adv swapped | Corrected to 6.7%/13.3% |
| C5 | Figure 11/12 descriptions wrong | Corrected to actual content |
| C6 | Table S6 reference mismatch | Changed to SR6/SR8 |
| C7 | Missing bib: Cohen1988 | Added @book entry |
| C8 | Missing bib: Kulkarni2022 | Added @article entry (Chandra & Kulkarni, IEEE Access) |
| C9 | Missing bib: Nida1964 | Added @book entry |
| C10 | Missing bib: Zhang2024 | Added placeholder (needs verification) |
| C11 | ELQV misattributed as Alharbi2024 | New Gaanoun2025 entry; citation fixed |
| C12 | Francis2015 used for Rome Call | Changed to RomeCall2020 |
| C13 | Figures 1-9 not in PAPER-V2/ | Copied from PAPER/figures/ |

### MAJOR Issues Resolved (18)
- Gate-passer count harmonized (354 eliminated, not 355)
- n=47 pre-removal sample justified in text
- CI feature count explained (C6 excluded for zero variance)
- "Expert council" → "Our analysis"
- "Cognitive demand" → "construct complexity" / "generative effort"
- K<R<V "universal" → "universal within the Claude model family"
- Discussion preview expanded to cover 5.5 and 5.6
- NormEval citation fixed (was Hendrycks2021/MMLU)
- PewResearch2017 citation added for 80% claim
- Call to Action 2 expanded to reference rubric ceiling (5.3)
- TuckYang2012 completed (journal/volume/pages)
- Supplementary back-references added (SR1-SR4)
- Gemini Pro S7 data corrected (0%/13.3%)

### MINOR Issues Resolved (32)
- Precision notes added to Table S9
- Overclaim hedging ("establish"→"provide", "are required"→"may be necessary")
- Ubuntu/Indigenous diversity qualifier added
- Abstract expanded with meta-evaluation criteria mention
- 7 citation additions (Gabriel2020, Ji2024, Koppel2011, Srivastava2024, URLs for MUKURTU, Sefaria, Chinese Text Project)
- Conclusion "Central Paradox" condensed ~30%
- Methods→Results bridging sentence added
- Various cross-reference narrowing (broad "Section 4" → specific subsections)

---

## File Locations

### Outputs
| File | Location | Purpose |
|------|----------|---------|
| Combined PDF | `PAPER-V2/20260412-religious-values-paper-v2.pdf` | 68-page final PDF (1.7MB) |
| Council reports | `PAPER-V2/review-council/expert-{1-6}-*.md` | 6 expert review reports |
| Synthesis report | `PAPER-V2/review-council/synthesis-report.md` | Deduplicated issue list |
| Verification reports | `PAPER-V2/review-council/verification-*.md` | Phase 4 verification |

### Modified Files
| File | Changes |
|------|---------|
| `00-abstract.md` | PewResearch2017 + Gabriel2020/Ji2024 citations, meta-eval mention, hedging |
| `01-methods.md` | Tier counts, gate-passer arithmetic, Table S6→SR6/SR8, cross-ref narrowing |
| `02-results.md` | Tier 1 restructured (Antisemitism Detection moved), Fig 11/12 descriptions, overclaim hedging, bridging sentence, citations |
| `03-discussion.md` | "Expert council"→"Our analysis", "cognitive demand"→"construct complexity", NormEval citation, preview expanded, MUKURTU URLs |
| `04-conclusion.md` | Call 2 expanded, "universal" qualified, Sefaria/Chinese Text Project URLs, condensed Central Paradox |
| `05-supp-methods.md` | Tier counts, C6 LOO exclusion note |
| `06-supp-results.md` | SR back-references, SR8a pre-removal note, SR7 cross-ref |
| `07-supp-tables.md` | Table S5 cross-ref narrowed, Table S9 precision note, p-value unified |
| `08-supp-figures.md` | S7 Haiku/Flash/Pro data fixed, S2/S6 [NOT YET GENERATED] notes, V/K ratio, back-ref specificity |
| `PAPER/religious-values-benchmarks.bib` | 5 new entries + 5 fixes = 88 total |

---

## Remaining Work (Session 15+)

### Priority 1: Introduction and Related Work (Sections 1-2)
- 56 uncited bib entries likely reserved for these sections
- Expert 1 produced a Sections 1-2 dependency list (see `review-council/expert-1-transitions.md`)
- TODO comment in `03-discussion.md` marks thesis preview needed

### Priority 2: Zhang2024 Bib Verification
- Placeholder entry for "emerging work on theological dialogue systems"
- Needs author/title/venue verification or citation removal before submission

### Priority 3: Generate Figures S2 and S6
- Figure S2: Gate Threshold Sensitivity Extended (described but no image)
- Figure S6: Bias-Values Scatter Plots Per Model (described but no image)
- Likely need additions to `generate_figures_v2.py`

### Priority 4: LaTeX Conversion
- NeurIPS 2026 D&B submission (8pp + unlimited appendix)
- Bib file ready (88 entries, clean syntax)

---

## Known Issues

1. **Zhang2024** bib entry is a placeholder with TODO comment
2. **Figures S2 and S6** described but not generated as image files
3. **NormEval** referenced as "authors' companion analysis" — if published separately, needs formal citation

---

*Filed: 2026-04-12 | CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/*
