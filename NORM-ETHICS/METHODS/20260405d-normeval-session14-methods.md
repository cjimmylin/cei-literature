# Methods: NormEval Combined PDF Generation

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The combined PDF was generated from 21 markdown source files (10 main body + 10 supplementary + 1 introduction) and 12 publication-quality figures (8 main body + 4 supplementary) produced in Session 13. The markdown files totaled 64,724 words. Figures were sourced from `PAPER-v2/figures/` in both PNG (300 DPI raster) and PDF (vector) formats.

Dashboard data sources remained unchanged from Session 13:
- `DASHBOARD-v2/data.js` (182 KB, 14 pre-computed JavaScript constants)
- `DASHBOARD-v2/data_cross_vendor.js` (16 KB, 8-model cross-vendor data)

## Procedure

### Combined PDF Pipeline

A three-stage pipeline converted markdown sources to a single combined PDF:

**Stage 1: Markdown preprocessing.** Each markdown file was read and preprocessed by a custom `clean_markdown()` function that (a) stripped YAML frontmatter, (b) removed inline image links (figures embedded separately), (c) converted LaTeX-style `\cite{}` commands to bracketed references, and (d) transformed blockquote markers (`>`) into styled HTML `<blockquote>` elements.

**Stage 2: HTML conversion.** Preprocessed markdown was converted to HTML using Python's `markdown` library (v3.9) with three extensions: `tables` (for pipe-delimited markdown tables), `fenced_code` (for code blocks), and `nl2br` (for line break handling). Table elements received inline styling (`border="1" cellpadding="3"`) and header cells received background coloring for readability in the PDF.

**Stage 3: PDF rendering.** HTML content was rendered to PDF using fpdf2 (v2.8.4) with the `write_html()` method. The Arial Unicode MS system font (`/Library/Fonts/Arial Unicode.ttf`) was loaded in four variants (regular, bold, italic, bold-italic) to support full Unicode rendering including em-dashes, daggers, and mathematical symbols. A custom `NormEvalPDF` subclass provided running headers (paper title + current section), page footers (page numbers), and a table-of-contents accumulator.

**Figure embedding.** After each section's text was rendered, the script scanned the original markdown for figure references (`Figure 1` through `Figure S6`) and embedded corresponding PNG files from the `figures/` directory. The tradition heatmap (54 rows) was rendered at reduced width (150mm) to prevent overflow; all other figures used full column width (180mm). Figure captions were rendered in italic beneath each image.

### Bug Fixes

Three issues identified in the Session 13 handoff were resolved:

1. **Figure S5 data parsing.** The `provider_profiles` object in `data_cross_vendor.js` contains a `dimensions` list and a `profiles` dict (keyed by provider name). The original script incorrectly tried to access profile data by indexing into the top-level dict with dimension names. Fixed by reading `pp["profiles"]` and iterating provider entries.

2. **Introduction n=37 references.** The comprehensive introduction was copied from `PAPER/` to `PAPER-v2/` as `introduction-comprehensive-normeval-v2.md`. Six occurrences of stale n=37 statistics were updated: title, abstract, contributions paragraph, roadmap paragraph, and two body text references. All updates were mechanical number changes consistent with the n=54 corpus.

3. **fpdf2 API deprecation.** All `ln=True` parameters in both generation scripts were replaced with `new_x=XPos.LMARGIN, new_y=YPos.NEXT` (fpdf2 v2.5.2+ enum API). The `uni=True` parameter was removed from `add_font()` calls (deprecated since v2.5.1).

## Computational Environment

- Python 3.9 (`.venv/`)
- fpdf2 2.8.4 (PDF generation with HTML rendering)
- markdown 3.9 (markdown→HTML conversion)
- matplotlib 3.9.4, seaborn 0.13.2, numpy 2.0.2 (figure generation)
- Arial Unicode MS font (system TTF, `/Library/Fonts/Arial Unicode.ttf`)
- macOS Darwin 25.3.0

## Limitations and Decisions

1. **HTML rendering fidelity.** fpdf2's `write_html()` supports a subset of HTML (h1-h6, p, b, i, u, a, table, ul, ol, li, blockquote, br, hr). Complex markdown constructs (nested blockquotes, footnotes, definition lists) are rendered as plain text via a fallback path.
2. **No table of contents generated.** The TOC accumulator collects entries but the TOC page itself was not inserted to avoid page number shifts. A future version could use fpdf2's two-pass rendering.
3. **Introduction excluded.** Per user specification, Sections 1–2 (Introduction and Related Work) were omitted from the combined PDF. The updated v2 introduction exists as a separate markdown file.
4. **Font choice.** Arial Unicode MS was chosen over the built-in Helvetica because the paper text contains em-dashes (—), dagger symbols (†), and other Unicode characters that Helvetica's Latin-1 encoding cannot represent.
