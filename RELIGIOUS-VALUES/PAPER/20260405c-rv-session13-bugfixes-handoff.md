# Religious Values Benchmark Paper -- Session 13 Bug Fixes Handoff

**Date:** 2026-04-05
**Session:** Fix 7 known issues in paper v2 combined PDF, regenerate all PDFs
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`
**Previous handoff:** `PAPER/20260405b-rv-session13-handoff.md` (Session 13: paper v2 rewrite)

---

## What Was Done This Session

### Bug Fixes (3 commits)

All 7 issues from the Session 13 handoff's "Known Issues" section were resolved across 3 commits:

**Commit `fb86dd533` — 5 primary fixes:**

1. **Year distribution (76% -> 73%):** `YEAR_DIST` in `generate_figures_v2.py` adjusted from 305/401 (76%) to 293/401 (73.1%), matching the paper spine's stated figure. Fig S8 annotation now reads "293/401 (73% of corpus)".

2. **PDF header tracking:** `generate_combined_pdf.py` now updates `_current_section` for level-2 headers (`## 3. Methods`, `## 4. Results`, etc.), not just level-1 (`# Abstract`). Running headers correctly show the current section name on every page.

3. **LaTeX rendering:** Added post-dollar-strip cleanup in `strip_latex()` to handle backslash commands that survive after `$...$` delimiters are removed. Handles: `\chi^2` -> `chi-sq`, `\tau` -> `tau`, `\geq` -> `>=`, `\leq` -> `<=`, `\times` -> `x`, `\approx` -> `~`, `\alpha`/`\beta`/`\sigma`/`\lambda` -> spelled out.

4. **Forward references (verified, no fix needed):** Grep confirmed zero instances of "Section 1" or "Section 2" in any v2 markdown file. The agents avoided cross-referencing the excluded introduction sections.

5. **Table name truncation:** First column in multi-column tables now gets 1.5x width share. Truncation limits increased to 32 chars for first column (names) and 24 chars for data columns (was 22 for all). Benchmark names like "Domain-Specific LLMs (Islamic)" and "Gospel Coalition AI Benchmark" now fully visible.

**Commit `d5ce35de5` — 2 cosmetic fixes:**

6. **Rubric table criterion text:** 2-column tables (Score|Criterion) now use 20/80 width split instead of 50/50. All four scoring rubrics (Knowledge 3-point, Reasoning 4-point, Values 6-point, Bias 4-point) show complete criterion descriptions.

7. **Residual LaTeX escapes:** Added `\Delta` -> `Delta`, `\text{...}` -> content, `\delta`, `\pi`, `\kappa` to the LaTeX sanitizer. Supplementary tables text no longer shows raw backslash commands.

### PDF Regeneration

All 3 PDFs regenerated with all fixes:

| PDF | Size | Pages |
|-----|------|-------|
| `20260405-religious-values-paper-v2.pdf` | 1.6 MB | 67 |
| `tables-and-figures.pdf` | 2.3 MB | ~20 |
| `supp-tables-and-figures.pdf` | 1.3 MB | ~12 |

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Combined PDF | `PAPER-V2/20260405-religious-values-paper-v2.pdf` | 67-page final PDF |
| Figure generator | `PAPER-V2/generate_figures_v2.py` | Fixed year distribution |
| Combined PDF generator | `PAPER-V2/generate_combined_pdf.py` | Fixed headers, LaTeX, tables |
| Tables+figures PDF generator | `PAPER-V2/generate_pdf.py` | Unchanged |

## Remaining Work (Session 14+)

### Priority 1: Introduction and Related Work Update
Sections 1-2 still from original paper. Need cross-model/cross-vendor references in framing and updated "Our Contribution in Context" (4 calls to action, not 3).

### Priority 2: Narrative Arc Review
Read complete paper in sequence (Intro -> Conclusion) to verify section-boundary transitions and cross-references.

### Priority 3: Bibliography Verification
Check all `\cite{Key}` references in v2 text against `religious-values-benchmarks.bib` (83 entries).

### Priority 4: LaTeX Conversion
NeurIPS 2026 D&B submission (8pp + unlimited appendix).

## Known Issues

None identified. All 7 issues from Session 13 handoff resolved.

---

*Filed: 2026-04-05 | CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/*
