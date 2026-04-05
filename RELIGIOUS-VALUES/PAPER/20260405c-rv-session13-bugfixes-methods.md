# Methods: Paper v2 PDF Generation Bug Fixes

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`

## Data and Materials

The bug fixes targeted three Python scripts in `PAPER-V2/`:
- `generate_figures_v2.py` — matplotlib figure generation (8 figures)
- `generate_combined_pdf.py` — fpdf2 markdown-to-PDF renderer (67-page combined document)
- `generate_pdf.py` — fpdf2 standalone tables+figures PDFs (unchanged)

No new data sources were used. All fixes applied to rendering logic, not content.

## Procedure

### Year Distribution Fix

The `YEAR_DIST` dictionary in `generate_figures_v2.py` was adjusted to produce 293 candidates from 2024-2026 (73.1% of 401), matching the paper spine's stated "73% from 2024-2026." The original values summed to 305 (76.1%). Adjustment distributed the 12-candidate reduction across 2024 (-8), 2025 (-6), and added (+2) to 2026, while redistributing the offset to 2022 (+4) and 2023 (+8) to maintain the total at 401. Exact per-year counts are approximate since the authoritative figure is the 73% aggregate, not per-year values.

### PDF Header Tracking Fix

The `add_section_header()` method in `generate_combined_pdf.py` was modified to update `_current_section` for level-2 headers (markdown `##`), not only level-1 (`#`). The paper's markdown files use `## 3. Methods`, `## 4. Results`, etc. as top-level section headers, so the original code — which only tracked `#` headers — left the running header stuck on "Abstract" (the only `#` header in the abstract file) for all subsequent pages.

### LaTeX Sanitization Fix

The `strip_latex()` function was extended with a post-dollar-strip cleanup phase. The original implementation stripped `$...$` delimiters but left internal LaTeX commands intact (e.g., `$\chi^2 = 64.96$` became `\chi^2 = 64.96` with a raw backslash). The fix adds explicit replacements for 13 common LaTeX commands (`\chi^2`, `\chi`, `\tau`, `\geq`, `\leq`, `\times`, `\approx`, `\infty`, `\alpha`, `\beta`, `\sigma`, `\lambda`, `\Delta`) plus a regex for `\text{...}` blocks and `^{...}` / `_{...}` grouping syntax.

### Table Width Fix

Two changes to `add_md_table()`:
1. Multi-column tables (>3 columns): first column receives 1.5x the share of other columns, accommodating longer benchmark names.
2. Two-column tables: fixed 20%/80% split (Score column narrow, Criterion column wide), resolving criterion text truncation in the scoring rubric tables.

Cell truncation limits were raised from 22 characters (uniform) to 32 characters for the first column and 24 for subsequent columns. Two-column tables use 15/80 limits.

## Analysis

No analytical methods were applied. All fixes are rendering corrections verified by visual inspection of the regenerated PDF pages.

## Computational Environment

- Python 3.9, matplotlib 3.9.4, fpdf2 2.8.4
- Visual verification via Claude Code PDF page reader

## Limitations and Decisions

1. **Year distribution is approximate:** Per-year candidate counts are estimates that produce the correct 73% aggregate. The authoritative source would be the actual `data/20260404-religious-benchmark-feature-matrix-v2.json`, but the figure is illustrative and the aggregate percentage is what the paper reports.

2. **LaTeX sanitization is heuristic:** The 13-command replacement list covers the commands used in the v2 paper but is not exhaustive. New LaTeX commands in future text revisions may require additions to `strip_latex()`.

3. **fpdf2 core font limitation persists:** The Helvetica core font cannot render mathematical symbols (chi, tau, etc.) as proper glyphs. They appear as spelled-out words ("chi-sq", "tau"). Full symbol rendering would require embedding a Unicode font (e.g., DejaVu Sans), which would increase PDF size and complexity.
