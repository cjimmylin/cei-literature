# Religious Values Benchmark Paper -- Session 13 Handoff

**Date:** 2026-04-05
**Session:** Full paper v2 rewrite (Methods through Conclusion + Supplementary) with 12-member writing council
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`
**Previous handoff:** `PAPER/20260405a-rv-session12-handoff.md` (Session 12: Claim 8, 3 caveats, dashboard v6)

---

## What Was Done This Session

### 1. Full Paper v2 Rewrite (PAPER-V2/ directory)

Created a complete rewrite of all paper sections **except** Introduction (Section 1) and Related Work (Section 2), driven by a fresh 12-member expert writing council optimized for academic paper production.

**Total output:** 43,490 words across 9 markdown files + 2 PDFs + 8 new figures.

#### Main Body Sections (25,442 words)

| File | Section | Words | Key Content |
|------|---------|-------|-------------|
| `00-abstract.md` | Abstract | 858 | Structured (Background/Methods/Results/Conclusions), all 8 claims, cross-vendor with caveats |
| `01-methods.md` | Section 3 | 6,451 | 7 subsections: corpus assembly, feature matrix, composite scoring, meta-evaluation, trial protocol (65-item + T2), statistical plan, limitations |
| `02-results.md` | Section 4 | 8,755 | 6 subsections: landscape, tiered ranking (25 benchmarks), tradition coverage (14 traditions), claim robustness (8 claims), cross-model validity, cross-vendor replication |
| `03-discussion.md` | Section 5 | 7,689 | 9 subsections: tradition asymmetry, knowledge vs reasoning, rubric ceiling paradox (NEW), cross-vendor divergence (NEW), values relevance failure, infrastructure barrier, gap strategies, transparency, limitations |
| `04-conclusion.md` | Section 6 | 1,689 | 4 calls to action (added: cross-vendor evaluation standards), 5 future work items |

#### Supplementary Materials (18,048 words)

| File | Content | Words |
|------|---------|-------|
| `05-supp-methods.md` | 7 sections: CV battery design, T2 sampling, cross-model admin, cross-vendor admin, bootstrap algorithm, statistical tests, response length analysis | 3,993 |
| `06-supp-results.md` | 8 sections: per-tradition gradients, rubric breakdown, T2 beginner/advanced, bias-values correlations, void factors, leave-one-out, WEIRD-neutral weighting, sensitivity extended | 4,866 |
| `07-supp-tables.md` | Tables S1-S10 with descriptions | 5,374 |
| `08-supp-figures.md` | Figures S1-S8 specifications and descriptions | 3,815 |

### 2. New Figures Generated (8 files)

| Figure | File | Content |
|--------|------|---------|
| Fig 10 | `fig10-cross-model-gradient.png` | K<R<V grouped bar (Claude family) |
| Fig 11 | `fig11-rubric-heatmap.png` | 9-model x 4-dimension rubric scores |
| Fig 12 | `fig12-t2-accuracy.png` | T2 accuracy horizontal bar (9 models) |
| Fig 13 | `fig13-vendor-radar.png` | Vendor capability radar (3 vendors) |
| Fig S4 | `fig-s4-tradition-gradient.png` | 3x3 small multiples (per-tradition K<R<V) |
| Fig S5 | `fig-s5-cross-vendor-length.png` | All 9 models log-scale response lengths |
| Fig S7 | `fig-s7-t2-beginner-advanced.png` | Beginner vs Advanced accuracy |
| Fig S8 | `fig-s8-year-distribution.png` | 401-candidate temporal distribution |

Style: matplotlib/seaborn, 300 DPI, Okabe-Ito colorblind-safe palette.

### 3. PDFs Generated (3 files)

| PDF | Size | Pages | Content |
|-----|------|-------|---------|
| `20260405-religious-values-paper-v2.pdf` | 1.6 MB | 67 | **Combined PDF**: title page + abstract + methods + results + discussion + conclusion + all supplementary, with embedded figures and formatted tables |
| `tables-and-figures.pdf` | 2.2 MB | ~20 | 6 tables + 13 figures (9 existing + 4 new) |
| `supp-tables-and-figures.pdf` | 1.2 MB | ~12 | 5 tables + 6 figures |

### 4. Writing Council Composition

Fresh 12-member council (no fabricated expert names -- all use "[Discipline] perspective" labels):

| # | Label | Mandate |
|---|-------|---------|
| 1 | Islamic Ethics | fara'id/Maqasid precision, T2 interpretation |
| 2 | Comparative Religion | Anti-essentialization, tradition coverage |
| 3 | Psychometrics | Statistical claims, rubric ceiling, T2 discrimination |
| 4 | Benchmark Design | Methodology standards, meta-evaluation criteria |
| 5 | Decolonial Studies | Epistemic injustice framing, CARE Principles |
| 6 | Cross-Cultural NLP | Cross-vendor methodology, language bias |
| 7 | Science Communication | Narrative arc, readability, audience calibration |
| 8 | Statistics | p-values, effect sizes, bootstrap CIs |
| 9 | Philosophy of AI | "Understanding" vs pattern-matching, construct validity |
| 10 | Indigenous Data Governance | 8-tradition void framing, community sovereignty |
| 11 | Journal Editor | Structure, flow, reviewer objections |
| 12 | Dharmic Philosophy | Dharmic traditions not exoticized |

### 5. Quality Checks Passed

- **Anti-essentialization:** 0 violations across all 43K words (grep confirmed)
- **Cross-vendor caveats:** 3 caveats (T2 blinding, scorer bias, Gemini provenance) present in Methods, Results, AND Discussion
- **Data consistency:** All statistics match `data/20260404-claim-robustness-tests.json` and `COMPARISON/results/model-comparison.json`

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| All v2 files | `RELIGIOUS-VALUES/PAPER-V2/` | New paper version directory |
| Combined PDF | `PAPER-V2/20260405-religious-values-paper-v2.pdf` | 67-page combined document |
| Council doc | `PAPER-V2/council-composition.md` | 12-member council specification |
| Figure generator | `PAPER-V2/generate_figures_v2.py` | matplotlib script for 8 new figures |
| PDF generator | `PAPER-V2/generate_pdf.py` | fpdf2 script for tables+figures PDFs |
| Combined PDF gen | `PAPER-V2/generate_combined_pdf.py` | fpdf2 script for 67-page combined PDF |
| New figures | `PAPER-V2/figures/` | 8 PNG files, 300 DPI |
| Live dashboard | `cjimmylin.github.io/cei-rv-dashboard/` | Dashboard v6 (from Session 12) |

---

## Remaining Work (Session 14+)

### Priority 1: Introduction and Related Work Update
`PAPER/introduction-religious-values.md` and `PAPER/section2-litreview-part1.md` / `part2.md` were excluded from this rewrite. They should be updated to:
- Reference the cross-model and cross-vendor findings in the framing
- Add citations for any new literature discovered in sessions 7-13
- Update the "Our Contribution in Context" subsection (2.6) to reflect 4 (not 3) calls to action

### Priority 2: Narrative Arc Review
Read all sections in sequence (Intro -> Related Work -> Methods -> Results -> Discussion -> Conclusion) and verify:
- Smooth transitions at section boundaries
- Forward/backward references are consistent
- No redundancy between sections
- Figure/table numbers are sequential

### Priority 3: Bibliography Update
`PAPER/religious-values-benchmarks.bib` (83 entries, 667 lines) needs:
- Any new citations added by the writing agents that aren't in the .bib
- Verification that all \cite{Key} references in v2 text have matching .bib entries
- Add Fricker2007, TuckYang2012, Sorensen2024 if not already present

### Priority 4: LaTeX Conversion
Convert the complete paper (v1 intro + v2 body + supplementary) to LaTeX for NeurIPS 2026 D&B submission.

### Priority 5: Cross-Vendor Replication Extension
Administer 65-item battery + T2 to additional models (GPT-4o, Llama) using matched protocols (blind, interactive API).

---

## Known Issues

1. **Year distribution annotation:** Fig S8 shows 76% from 2024-2026, but spine says 73%. The 73% figure may be for gate-passers specifically; 76% is for all 401 candidates. Verify against source data.
2. **Header shows "Abstract"** in the running header of the combined PDF across all pages -- this is a minor bug in the section tracking in `generate_combined_pdf.py`.
3. **LaTeX math not fully rendered** in combined PDF -- fpdf2 core fonts can't render LaTeX; math expressions appear as `\chi^2`, `\geq`, etc. rather than symbols. The markdown source files have correct LaTeX.
4. **Introduction/Related Work gap** -- v2 sections reference content from Intro/Related Work that hasn't been updated yet. Forward references to "Section 2.5" etc. should be verified after Intro is finalized.
5. **Table 2 truncation** -- some benchmark names in Table 2 (tiered ranking) are truncated in the PDF due to column width constraints. The markdown source has full names.

---

*Filed: 2026-04-05 | CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/*
