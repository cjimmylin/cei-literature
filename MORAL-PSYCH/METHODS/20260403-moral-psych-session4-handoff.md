# Session 4 Handoff: Moral Psychology Benchmarks Meta-Evaluation

**Date:** 2026-04-03
**Session scope:** PDF generation for remaining paper sections
**Status:** All paper sections now have PDF coverage. Full paper ~35 pages across 3 PDFs.

---

## What Was Accomplished (This Session)

### 1. PDF Generation for Remaining Sections
- Created `build_remaining_pdf.py` script in `PAPER/` directory
- Script concatenates abstract + methodology + results + discussion + conclusion into a single PDF
- Uses **pandoc 3.9 + typst 0.14.2** pipeline (same as `RELIGIOUS-VALUES/PAPER/build_pdf.py` pattern)
- Preprocessing: `\cite{}` → bracketed refs, `\%` → `%`, `\newpage` separators between sections
- Fonts: Georgia (main) + Helvetica Neue (sans), 11pt, 1-inch margins

### 2. Output
- **File:** `PAPER/remaining-sections-mpbench.pdf`
- **Size:** 237.9 KB, 17 pages
- **Sections included:** Abstract (1pp), Methodology (6pp), Results (5pp), Discussion (3pp), Conclusion (2pp)
- All tables rendered correctly (Expert Council, 28-Feature Framework tiers A/B/C, Keyword Expansion, Theory Representation, Construct Validity, Human Baseline, Format Distribution, Theory Gap)
- Bold/italic formatting preserved (unlike earlier fpdf2 attempts)

---

## Complete PDF Inventory

| Section | File | Pages | Size |
|---------|------|-------|------|
| Introduction | `introduction-mpbench.pdf` | 5 | 90 KB |
| Related Work | `related-work-mpbench.pdf` | 13 | 126 KB |
| Abstract + Methods + Results + Discussion + Conclusion | `remaining-sections-mpbench.pdf` | 17 | 238 KB |
| **Total** | **3 PDFs** | **~35** | **454 KB** |

---

## New Files (Session 4)

```
MORAL-PSYCH/PAPER/
├── build_remaining_pdf.py              (NEW — pandoc+typst PDF builder)
├── remaining-sections-mpbench.pdf      (NEW — 17 pages, 238 KB)
```

---

## User Decisions (Binding for Future Sessions)

All Session 3 decisions remain in effect:
1. **Scope:** Standalone project — do NOT reference normative ethics project
2. **Weighting:** 50/30/20 (Psychological Depth / Practical Ease / Citation Impact)
3. **Models:** Claude-only first, expand to GPT-4o/Llama-3 later
4. **Output directory:** All files in `CEI-Lit-WS/MORAL-PSYCH/`
5. **Paper target:** ACL/EMNLP 2026 Datasets & Benchmarks track
6. **Comprehensiveness priority:** User explicitly prioritizes comprehensive coverage over brevity for intro/review

---

## What Remains

### Immediate Next Steps (from Session 3, still pending)
1. **Run actual Claude API trials** — current trials use published baselines; need real Opus/Sonnet runs
2. **De-duplicate TrolleyBench** — v2 top-15 has duplicate entries at ranks 12 + 14
3. **Re-add Kohlberg DIT** — lost all Kohlberg representation in v2 due to `data_url=NA` hard gate
4. **Playwright-verify dashboard** — agent verified, but user should confirm visually

### Background Literature (from Session 3, still pending)
5. **Manual download** of 31 remaining paywalled papers (institutional access needed)
6. **Ingest 14 new external finds** into vault (from Phase 2a search)
7. **Integrate background papers** into paper's bibliography (currently ~100+ citations in intro/review, should cross-reference with BibTeX)

### Paper Finalization
8. **Generate figures** from dashboard exports (6 planned)
9. **BibTeX generation** — compile full reference list from all cited papers
10. **LaTeX conversion** for ACL/EMNLP submission format
11. **Section numbering** and cross-reference consistency across all sections
12. **Combined single PDF** — merge all 3 current PDFs into one unified document with consistent page numbering
13. **PDF rendering improvement** — current pandoc+typst PDFs are clean but could benefit from LaTeX for final submission

### Dashboard Enhancement (from Session 2)
14. **GitHub Pages deployment** — needs public repo (per memory: Free plan requires public)
15. **Re-generate data.js** after actual trials complete (Phase 4 data will change)

---

## Critical Dependencies

1. **Keyword scorer:** `PYTHON/moral_psych_scoring.py` — expanded Session 2, 87 tests
2. **Implementability CSV:** `STATISTICS/20260313-implementability-cross-framework-table-v2.csv`
3. **Python env:** `../.venv/bin/python` (Python 3.9 — needs `from __future__ import annotations`)
4. **PDF extracts:** `PDF Extracts/YYYY/` — used by scorer and trial agents
5. **Background registry:** `BACKGROUND/20260403-background-registry.json` — master list of all 150 papers
6. **Writing council:** `PAPER/20260403-writing-council.json` — 12-member council for intro/review design
7. **Background papers:** Raw PDFs/HTML in `BACKGROUND/{01-12}/` folders (NOT markdown extracts). Each folder has `search-results.json` with metadata.
8. **PDF build script:** `PAPER/build_remaining_pdf.py` — pandoc+typst, regenerate with `../.venv/bin/python MORAL-PSYCH/PAPER/build_remaining_pdf.py`
