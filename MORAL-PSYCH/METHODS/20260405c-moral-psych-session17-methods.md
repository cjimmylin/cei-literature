# Methods: Dual-Council Paper Rewrite with Cross-Vendor Empirical Integration

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/MORAL-PSYCH/PAPER-v2/`

## Data and Materials

The paper rewrite drew on three categories of source material:

**v1 Paper Sections (7 files, 672 lines).** The existing paper in `MORAL-PSYCH/PAPER/` covering a landscape-mapping meta-evaluation of moral psychology benchmarks for LLM assessment. Sections included abstract, introduction, related work, methodology, results (5 claims), discussion, and conclusion. The introduction was preserved unchanged; all other sections were rewritten.

**Cross-Vendor Empirical Data (207+ files).** Trial results from 23 benchmarks administered to 9 models from 3 vendors:
- `MORAL-PSYCH/TRIALS/`: 80 Anthropic trial JSONs (23 benchmarks x 3 models + model comparison summary)
- `MORAL-PSYCH/COMPARISON/`: Cross-vendor comparison data (9 models x 23 benchmarks), model inventory, benchmark coverage matrix
- `MORAL-PSYCH/ANALYSIS/`: Cross-vendor council analysis (2 parts, ~1,200 lines), analyses A-H JSONs, dashboard data
- `MORAL-PSYCH/COUNCIL/`: 12-member council meta-critique, feature proposals, expanded theory framework

**Bibliography.** `PAPER/20260404-mpbench.bib` containing 155+ BibTeX references (1,394 lines). Copied to PAPER-v2 as the starting bibliography.

## Procedure

### Council Formation

Two 12-member expert councils were convened, each with distinct disciplinary composition:

**Council A (Meta-Evaluation)** was designed to cover: moral psychology theory (historical, MFT, process theories, structural theories), psychometric validity, cross-cultural psychology, benchmark landscape surveying, format/measurement, NLP evaluation, bibliometrics, survey methodology, and meta-science critique.

**Council B (Empirical)** was designed to cover: cross-vendor analysis, RLHF/alignment, AI safety, scale sensitivity, cross-cultural psychology, dual-process cognitive science, psychometrics (empirical), statistical methodology, moral philosophy, policy/governance, developmental psychology, and philosophy of mind.

Council compositions were stored as structured JSON files specifying each member's role, expertise, and section assignments.

### Joint Deliberation Protocol

Both councils produced a joint decisions document addressing four structural questions:
1. **Scope**: What belongs in the main paper vs. supplementary material
2. **Narrative Arc**: The unified thesis connecting landscape mapping and empirical testing
3. **Target Journal**: Primary (Nature Machine Intelligence) and secondary (PNAS) venues
4. **Section Structure**: Final table of contents with section-to-council assignment mapping

The joint deliberation was encoded as a structured JSON document that served as the shared specification for all writing agents.

### Parallel Writing Execution

Twelve writing agents were launched simultaneously, each assigned a specific section with explicit instructions covering structure, source data, narrative context, and style guidelines. Council A agents wrote 6 sections (related work, methodology landscape, results claims 1-3, results claims 4-5, supplementary methods, supplementary tables). Council B agents wrote 6 sections (methodology empirical, results convergence, results scale/CoT, results theory patterns, supplementary results, supplementary figures).

Each agent was provided:
- The v1 version of its section (where applicable) as a starting point
- The joint council decisions document for narrative alignment
- Specific source data files to read for quantitative content
- Style guidelines (Nature Machine Intelligence, academic journal prose, "[Discipline] perspective" labels for expert commentary)

### Sequential Integration

Three sections were written sequentially after Phase 2 completed:
1. **Discussion** — synthesizing both councils' findings into the "double bind" and "value monoculture" framing, with 9 limitation subsections addressing all 12 council meta-critique findings
2. **Conclusion** — closing narrative threads with governance imperative and three urgently needed benchmarks
3. **Abstract** — written last to accurately summarize the complete paper (318 words, structured format)

### Table and Figure Generation

Table PDFs were generated using fpdf2 (v2.8.4) with a custom `TablePDF` class providing consistent styling: Helvetica headers on dark blue background (#294182), alternating row shading, 1-inch margins, auto-pagination for long tables. A `sanitize()` function handled Unicode characters (em dashes, smart quotes) incompatible with Helvetica core fonts.

New data-driven figures (F7-F12) were generated using matplotlib (v3.9.4) with a consistent color palette: Anthropic (#4A90D9), Google/Gemini (#E74C3C), OpenAI (#2ECC71). Figures were saved as both PNG (300 DPI) and PDF. Existing v1 figures (F1-F6) were converted from PNG to PDF by embedding in single-page PDFs via fpdf2.

### Combined PDF Assembly

The combined PDF was assembled using a Python script that:
1. Reads all section markdown files in document order (excluding introduction and related work)
2. Preprocesses each section: resolves image paths to absolute filesystem paths, converts LaTeX citation commands to bracket notation
3. Concatenates sections with page breaks between major sections
4. Appends supplementary material after a divider page
5. Runs pandoc 3.9 with typst 0.14.2 as the PDF engine

## Analysis

### Quality Assurance

A read-only QA agent verified:
- **Cross-references**: All Figure N, Table N, Section N.N, and Claim N references resolve
- **Abstract-body alignment**: Every claim in the abstract appears in the body
- **Data consistency**: 8 key numbers verified across all sections (222 candidates, 9 models, 43% zero variance, 6 RLHF fingerprints, DIT P-scores, Haiku CoT effect 0.125)
- **Completeness**: No TODO markers or placeholder text

Three issues were identified and resolved: Figures 7-12 lacked inline references in the empirical results sections (added). One issue was deferred: table numbering collisions across independently-written sections.

## Computational Environment

- **Python:** 3.9 (via `.venv`)
- **fpdf2:** 2.8.4 (table and figure PDF generation)
- **matplotlib:** 3.9.4 (data-driven figure generation)
- **Pillow:** available (image processing)
- **pandoc:** 3.9 (markdown to PDF conversion)
- **typst:** 0.14.2 (PDF rendering engine)
- **Platform:** macOS Darwin 25.3.0

## Limitations and Decisions

**Agent rate limits.** Several background writing agents hit rate limits during execution. However, all agents had already written their output files before the limits were reached, resulting in no data loss. The rate limit affected only the agent's ability to report its completion — the written files were complete.

**Table numbering.** Each section was written independently by a separate agent, leading to table numbering collisions (e.g., "Table 2" appears in both methodology and results). This was a deliberate trade-off to enable parallel writing; sequential renumbering is deferred to final assembly.

**Gemini data provenance.** 21 of 23 Gemini benchmarks use cloned Opus prompt data rather than independently administered Gemini trials. This is transparently disclosed throughout the paper and supplementary material, but limits the strength of cross-vendor claims for the Gemini family.

**Word count vs. journal limits.** The paper was written without length constraints per user instruction ("do not worry about length"), producing 54,623 words of main text against a Nature MI limit of ~5,000 words. Trimming for submission is a separate future task; the current draft captures all findings comprehensively.
