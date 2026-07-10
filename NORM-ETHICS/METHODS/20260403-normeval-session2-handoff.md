# Normative Ethics Eval-of-Evals — Session 2 Handoff

**Date:** 2026-04-03
**Status:** Paper editorial fixes complete; 4 figures generated; 123 background papers assembled and extracted
**Previous handoff:** `METHODS/20260403-normeval-session-handoff.md` (Sessions 1-14)
**Project directory:** `CEI-Lit-WS/NORM-ETHICS/`

---

## Executive Summary

Resumed from the Session 1-14 handoff, which left 2 editorial items and recommended next steps. This session completed:

1. **2 editorial fixes** (Rottger citation mismatch, missing Appendix F)
2. **4 publication-quality figures** (tradition heatmap, framework difficulty, ND vs PE scatter, data availability)
3. **123 background papers** assembled via 14-member expert council and 9 parallel search agents across 13 thematic blocks
4. **Text extraction pipeline** — all PDFs extracted to markdown, originals gitignored

---

## Work Completed

### Editorial Fixes

1. **Rottger2024 citation mismatch** — Swapped `\cite{Rottger2024}` (XSTest, exaggerated safety behaviors) → `\cite{Rottger2025}` (SafetyPrompts, AAAI 2025 systematic review of 102 safety evaluation datasets). Updated spine and introduction. XSTest entry retained in bibliography but no longer cited in body.

2. **Appendix F (Table S9)** — Wrote full 37×6 cross-harness implementability matrix with tier symbols (■ IMPLEMENTED, ◧ READY, ○ POSSIBLE, — N/A), summary statistics, and 5 analytical observations. Key finding: HELM has zero normative ethics integrations; 40.5% of benchmarks have zero accessible harnesses.

### Figure Generation

All saved to `PAPER/figures/` at 300 DPI:

| Figure | File | Description |
|--------|------|-------------|
| Fig 1 | `fig1-tradition-heatmap.png` | 37×5 tradition coverage heatmap (care/contractarian void visible) |
| Fig 2 | `fig2-framework-difficulty.png` | U=77% > V=63% > D=50% grouped bars from MoralReason-QA trial |
| Fig 3 | `fig3-nd-vs-pe-scatter.png` | ND vs PE with citation bubble size, ND≥40 gate line, top-5 labeled |
| Fig 4 | `fig4-data-availability.png` | GitHub(17) + HuggingFace(4) + Public(2) vs Unavailable(14) |

### Background Literature Assembly

**14-member expert council** covering: construct validity, benchmark lifecycle, computational ethics, dual-process cognition, care ethics, data contamination, evaluation harnesses, RLHF, documentation standards, cross-cultural psychology, AI ethics surveys, moral philosophy, meta-science, value pluralism.

**13 search blocks** across 4 priority tiers executed by 9 parallel agents:

| Block | Topic | Papers |
|-------|-------|--------|
| A | Construct Validity + Benchmark Lifecycle | 23 (7 vault + 16 external) |
| B | Computational Ethics Foundations | 13 external |
| C | Dual-Process Moral Cognition | 9 (1 vault + 8 external) |
| D | Care Ethics Operationalization | 14 (3 vault + 11 external) |
| E | Data Contamination | 8 external |
| F | RLHF & Consequentialist Bias | 8 external |
| G | Benchmark Documentation Standards | 7 (1 vault + 6 external) |
| H | Cross-Cultural Moral Psychology | 6 (2 vault + 4 external) |
| I | LLM-as-Judge Methodology | 6 (3 vault + 3 external) |
| J | Moral Reasoning vs. Judgment | 6 (2 vault + 4 external) |
| K | Philosophical AI Ethics Surveys | 6 (2 vault + 4 external) |
| L | Value Pluralism / Moral Uncertainty | 4 (1 vault + 3 external) |
| M | Recent 2026 Benchmarks | 6 (2 vault + 4 external) |
| **Total** | | **123 papers (25 vault + 98 external)** |

**Advanced retrieval strategies** recovered 3 papers from the "paywalled" list:
- van Wynsberghe 2016 (CC-BY, curl with redirect following)
- Tronto 1993 (full book PDF from syllabus.pirate.care)
- Graham & Haidt 2009 JPSP (from UNC repository, substitute for paywalled 2007 article)

### Text Extraction & Directory Reorganization

- All 123 PDFs extracted to markdown via PyMuPDF (`BACKGROUND/EXTRACT/`)
- Originals moved to `BACKGROUND/ORIG/` (169 MB, gitignored)
- `.gitignore` excludes `ORIG/`, `01-vault-papers/`, `02-external-papers/`
- Convention documented: **always use `EXTRACT/` for analysis, never `ORIG/`**

---

## Files Created/Modified

### NORM-ETHICS/PAPER/ (modified)
| File | Change |
|------|--------|
| `introduction-normeval.md` | Rottger2024 → Rottger2025 citation |
| `spine-normeval.md` | Updated Rottger citation key |
| `supplement-normeval.md` | Added Appendix F (Table S9 + §F.1-F.2) |
| `integration-report-normeval.md` | Marked 2 blocking items as resolved |
| `figures/fig1-tradition-heatmap.png` | NEW — 37×5 heatmap |
| `figures/fig2-framework-difficulty.png` | NEW — U/V/D bar chart |
| `figures/fig3-nd-vs-pe-scatter.png` | NEW — ND vs PE scatter |
| `figures/fig4-data-availability.png` | NEW — data availability bars |

### NORM-ETHICS/BACKGROUND/ (all new)
| File/Dir | Purpose |
|----------|---------|
| `00-council-and-search-strategy.md` | 14-member council, directory structure, search log |
| `03-bibliography.md` | Master bibliography (123 entries, annotated by block + section) |
| `.gitignore` | Excludes ORIG/, 01-vault-papers/, 02-external-papers/ |
| `EXTRACT/` (123 files) | Markdown text extracts — **use this for all analysis** |
| `ORIG/` (123 files) | Original PDFs (169 MB, gitignored) |

### Root CLAUDE.md (modified)
- Added NormEval row to stats table
- Added EXTRACT path to naming conventions

---

## Key Background Papers by Claim

### Claim 1 (Ceiling Effect) — strongest new support:
- Bowman & Dahl 2021 — "What Will it Take to Fix Benchmarking in NLU?"
- Raji et al. 2021 — "AI and the Everything in the Whole Wide World Benchmark"
- Burden et al. 2025 — 29-reviewer systematic review of construct validity across 445 benchmarks
- Golchin & Surdeanu 2024 — data contamination as alternative explanation

### Claim 2 (Consequentialist Bias) — strongest new support:
- Greene et al. 2001 — fMRI study establishing dual-process moral cognition
- Cushman 2013 — model-free (deontological) vs model-based (utilitarian) framework
- Tennant et al. 2025 — ICLR paper on explicit deontological+utilitarian reward functions

### Claim 3 (Care/Contractarian Void) — strongest new support:
- Held 2006 — foundational care ethics book (full text)
- Tronto 1993 — "Moral Boundaries" (full text)
- Weinberger 2024 — why care ethics resists formalization in AI
- Block M search confirmed: still zero care/contractarian benchmarks as of April 2026

### Claim 4 (Judgment vs Reasoning) — strongest new support:
- Haidt 2001 — "The Emotional Dog and Its Rational Tail" (social intuitionism)
- Rest 1999 — Four Component Model (canonical distinction)
- Musschenga 2009 — moral intuitions vs. expertise vs. reasoning

### Claim 5 (Data Bottleneck) — strongest new support:
- Gebru et al. 2021 — "Datasheets for Datasets"
- Paullada et al. 2021 — "Data and its (Dis)contents"

---

## Recommended Next Steps

1. **Author review of paper + figures** — Read all sections in order. Check that Figures 1-4 match the text descriptions. Verify Appendix F data.

2. **Integrate background citations** — The 123 background papers are organized by which paper section they support (see `03-bibliography.md`). Key additions:
   - Sec 2.1: Add Raji 2021, Bowman 2021, Burden 2025 to related work
   - Sec 5.1: Add contamination literature (Golchin, Jacovi, Xu survey)
   - Sec 5.2: Add Greene 2001/2014, Cushman 2013, Tennant 2025
   - Sec 5.3: Add Held 2006, Tronto 1993, Weinberger 2024
   - Sec 5.5: Add Gebru 2021, Mitchell 2019, Rest 1999

3. **LaTeX conversion** — Convert markdown sections to NeurIPS 2026 template

4. **Cross-model replication** — Run 150 trial items through GPT-4o and Llama-3

5. **Full-scale implementation** — Complete test sets for MoralReason-QA (680 items) and MoReBench (150 items)

---

## Architectural Decisions

- **EXTRACT-only workflow**: All future analysis reads from `BACKGROUND/EXTRACT/*.md`. Original PDFs in `ORIG/` are gitignored (169 MB).
- **Expert council as search methodology**: 14 disciplinary perspectives ensure cross-domain coverage (neuroscience, philosophy, NLP, psychometrics) that keyword search alone would miss.
- **Parallel agent architecture**: 9 agents across 13 blocks — each agent had a focused thematic brief to avoid overlap.
- **Substitution policy**: When a specific paper is paywalled, download the closest open-access equivalent by the same authors (e.g., Graham 2009 JPSP for Haidt 2007).

---

## Dependencies

- **Python venv:** `.venv/bin/python3` (Python 3.9) with `pymupdf` 1.26.5 for PDF extraction
- **matplotlib** 3.9.4 + **seaborn** 0.13.2 for figure generation
- **Feature matrix:** `STATISTICS/20260402-normative-benchmark-feature-matrix.json` (110 KB, 37 papers × 26+ features)
