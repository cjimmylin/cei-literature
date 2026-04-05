# Methods: Paper v2.1 Post-Assembly Numbering Correction

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/MORAL-PSYCH/PAPER-v2/`

## Data and Materials

**Source files:** 12 main-paper section files and 4 supplementary files in Markdown format, assembled from 12 parallel writing agents (Session 17). Combined PDF assembled via pandoc 3.9 with typst 0.14.2 as PDF engine.

**Known defects:** Three mechanical issues identified during Session 17 QA audit: (1) table numbering collisions across independently-written sections, (2) figure references appearing out of document order, (3) a convergence ranking table overflowing its page boundary in the typst-rendered PDF.

## Procedure

### Table Renumbering

A complete table audit was conducted across all 16 Markdown source files. Each table definition (`**Table N:**` or `**Table N.N.N.**`) and each in-text table reference (`Table N`, `(Table N)`) was catalogued with file and line number.

The 25 main-paper tables were assigned global sequential numbers (Table 1 through Table 25) following the assembly order specified in the build script (`build_combined_pdf.py` MAIN_SECTIONS list). Supplementary tables (ST1--ST5, S5.1--S7.3) retained their existing namespace-prefixed numbering as these do not collide with main-paper tables.

Three collisions were resolved:
- **Table 2:** methodology-landscape (Council B) vs. results-claims1-3 (Theory Representation) -- resolved by renumbering the latter to Table 5.
- **Table 4:** methodology-empirical (Nine-Model Inventory) vs. results-claims1-3 (Theory Gap Summary) -- resolved by renumbering the former to Table 3 and the latter to Table 7.
- **Table 5:** methodology-empirical (Benchmark Inventory) vs. results-claims4-5 (Human Baseline) -- resolved by renumbering the former to Table 4 and the latter to Table 8.

All cross-references in running text were updated to match the new numbering. Verification was performed by grep search for orphaned old-style references (`Table 5.\d`, `Table [2-6]:`) across all section and supplementary files.

### Figure Reordering

Figure appearance order in the assembled document was mapped by scanning all `![Figure N:` image tags in document order. The actual sequence was 1, 2, 5, 3, 6, 4, 7--12 -- figures 3--6 were out of order due to the narrative structure placing construct validity (originally Fig 5) before theory gaps (originally Fig 3), and human baselines (originally Fig 6) before implementation status (originally Fig 4).

Figures were renumbered in-place to match appearance order: old Fig 5 became Fig 3, old Fig 3 became Fig 4, old Fig 6 became Fig 5, old Fig 4 became Fig 6. PNG source files were not renamed (filenames are descriptive and are resolved by path, not by figure number). Corresponding figure descriptions in the supplementary figures file were also updated.

### Table Overflow Correction

The convergence ranking table (20 rows, 6 columns) was identified as overflowing page boundaries at approximately page 62 of the typst-rendered PDF. A `\newpage` directive was inserted immediately before the table definition in the Markdown source, which pandoc passes through to typst as a page break. This ensures the table begins at the top of a fresh page with full vertical space available.

## Analysis

No new analytical work was performed. All changes were mechanical (numbering, ordering, pagination) with no alteration to data, narrative, or conclusions.

## Computational Environment

- Python 3.9 (`.venv`)
- pandoc 3.9 with typst 0.14.2 PDF engine
- Build script: `PAPER-v2/scripts/build_combined_pdf.py`
- Output: `20260405-mpbench-v2.1-combined.pdf` (4,211 KB, ~206 pages)

## Limitations and Decisions

**Figure file naming mismatch.** After renumbering, PNG filenames no longer match their figure numbers (e.g., `fig5-construct-validity.png` is now Figure 3). This was a deliberate decision to avoid file-rename complications. The filenames are descriptive and the build script resolves images by path, so this creates no functional issue -- only a minor maintainability inconvenience that can be addressed during a future cleanup pass.

**Previous PDF retained.** The v2.0 combined PDF (`20260405-mpbench-v2-combined.pdf`) was not deleted, preserving the historical snapshot per project convention (CLAUDE.md Rule 3: report immutability).
