# Methods: Full Paper v2 Rewrite with Expert Writing Council

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`

## Data and Materials

### Source Documents

The rewrite drew on the following source materials from the Religious Values benchmark project:

- **Current paper:** `PAPER/full-paper-religious-values.md` (125,975 bytes, ~15,000 words across 385 lines)
- **Paper spine:** `PAPER/spine-religious-values.md` (8 claims, terminology glossary, citation keys, figure/table assignments)
- **Claims JSON:** `data/20260404-claim-robustness-tests.json` (8 claims with full statistical test results)
- **Cross-model data:** `data/20260404-cross-model-comparison.json` (3 models x 3 traditions, response length gradient, rubric scores, bias-values correlations)
- **Cross-model report:** `PAPER/20260404-cross-model-construct-validity-report.md` (executive summary, 5 sections)
- **Cross-vendor data:** `COMPARISON/results/model-comparison.json` (9 models, per-model metrics) and `COMPARISON/results/vendor-comparison.json` (3 vendors, aggregated metrics)
- **Cross-vendor council analysis:** `reports/20260404-cross-vendor-council-analysis.md` (12-member panel, 10 sections, 5,723 words)
- **Session methods documents:** `PAPER/20260404b-rv-session8-methods.md` (cross-model protocol), `PAPER/20260404d-rv-session10-methods.md` (cross-vendor protocol), `PAPER/20260405a-rv-session12-methods.md` (Claim 8, methodological caveats)
- **Bibliography:** `PAPER/religious-values-benchmarks.bib` (83 entries, 667 lines)
- **Existing figures:** `PAPER/figures/` (10 PNGs), `PAPER/fig-prisma-flow.png`
- **Existing supplement:** `PAPER/supplement-religious-values.md` (Tables S3 and S5)
- **Session handoffs:** 12 handoff documents from sessions 1-12

### Writing Council

A fresh 12-member expert writing council was convened specifically for the paper production task. The council was organized around academic writing competencies rather than the tradition-specific review structure used in previous sessions. Council members used "[Discipline] perspective" labels rather than fabricated expert names (per project convention). Council operating rules included: tradition veto for members 1, 2, 12; cross-cutting epistemic injustice mandate for member 5; narrative arc ownership for member 7; reviewer objection anticipation for member 11; and a universal anti-essentialization rule prohibiting constructions like "Islam believes X."

## Procedure

### Phase 1: Source Material Review

The orchestrating agent read the complete current paper (all 385 lines across 6 sections), the paper spine with 8 claims, the claims JSON with full statistical test results, the cross-model construct validity report, the cross-vendor council analysis, the vendor and model comparison JSONs, all three session methods documents (sessions 8, 10, 12), the existing supplement, and the bibliography. This comprehensive reading phase ensured all empirical data from 12 prior sessions was available in context before any writing began.

### Phase 2: Plan Development

An implementation plan was written to the plan file (`warm-toasting-shore.md`) specifying: section structure for each of 9 output files, data sources per section, council leads per section, subsection outlines with target word counts, figure/table assignments, and a 5-wave execution strategy. The user made four key decisions via interactive questions:
1. Exclude both Introduction (Section 1) and Related Work (Section 2)
2. Integrate cross-vendor data into the main paper with prominent caveat framing
3. Write at full comprehensive length (no page constraints), trim to NeurIPS 8pp later
4. Convene a fresh 12-member writing council optimized for academic production

### Phase 3: Parallel Agent Execution

Writing was executed via parallel background agents, each receiving a comprehensive prompt containing all relevant data embedded inline (the "fat data" approach -- agents did not need to read dozens of JSON files). Agents wrote markdown files directly to `PAPER-V2/`.

**Wave 1:** Council composition (written directly) + Abstract (written directly)
**Wave 2:** Methods agent (background) + Results agent (background)
**Wave 3:** Discussion agent (background) + Conclusion agent (background)
**Wave 4:** Supplementary Methods, Results, Tables, Figures agents (4 background agents)

Eight agents were dispatched in total. Four completed with full verification logs; four completed their file writes before encountering rate limits on verification steps. All 9 markdown files (10 including council doc) were successfully written.

### Phase 4: Figure Generation

Eight new figures were generated via a Python script (`generate_figures_v2.py`) using matplotlib 3.9.4, seaborn 0.13.2, and numpy 2.0.2. All figures use the Okabe-Ito colorblind-safe palette, 300 DPI resolution, serif fonts for axis labels, and academic styling. Figures were saved as PNGs to `PAPER-V2/figures/`.

### Phase 5: PDF Generation

Three PDFs were generated using fpdf2 2.8.4:

1. **`tables-and-figures.pdf`** (2.2 MB): Standalone tables and figures PDF containing 6 formatted tables (Tables 1, 3, 4, 5, 6, and tradition coverage) plus 13 figures (9 existing from `PAPER/figures/` + 4 new from `PAPER-V2/figures/`).

2. **`supp-tables-and-figures.pdf`** (1.2 MB): Supplementary tables (S3, S6, S8, S9, S10) and supplementary figures (S1, S3, S4, S5, S7, S8).

3. **`20260405-religious-values-paper-v2.pdf`** (1.6 MB, 67 pages): Combined PDF rendering all 9 markdown sections into a single document with title page, embedded figures, formatted tables, and consistent header/footer styling. The combined PDF generator (`generate_combined_pdf.py`) parsed markdown line-by-line, handling headers (4 levels), bold-lead paragraphs, bulleted and numbered lists, blockquote formulas, markdown tables (with alternating row colors and auto-pagination), horizontal rules, and inline figure references. Unicode characters unsupported by fpdf2 core fonts (em dashes, smart quotes, mathematical symbols) were sanitized to latin-1 equivalents.

### Phase 6: Quality Verification

Three automated quality checks were performed:
1. **Anti-essentialization grep:** Searched all v2 markdown files for "Islam believes", "Christianity believes", "Hinduism believes", "Judaism believes" -- zero violations found (the only match was the rule definition itself in `council-composition.md`).
2. **Caveat distribution:** Grepped for "caveat|blinding|scorer bias|Gemini provenance|backfilled" in the Discussion section -- 6 occurrences confirmed, ensuring caveats are distributed across sections.
3. **Visual PDF verification:** Title page, abstract, methods (with PRISMA flow), results (with tiered ranking tables and new figures), discussion, and cross-vendor sections were visually inspected via PDF page reads.

## Analysis

No new statistical analysis was performed in this session. All statistics were drawn from existing data files (claims JSON, cross-model comparison, cross-vendor comparison) and reproduced verbatim in the rewritten text. The rewrite organized, expanded, and contextualized existing findings rather than generating new ones.

## Computational Environment

- **Platform:** macOS Darwin 25.3.0
- **Python:** 3.9 (`.venv/bin/python3`)
- **matplotlib:** 3.9.4
- **seaborn:** 0.13.2
- **numpy:** 2.0.2
- **fpdf2:** 2.8.4
- **Claude Code:** Opus 4.6 (1M context) as orchestrator with max effort
- **Agent models:** 8 background agents via Claude Code subagent framework
- **No external API calls:** All writing via Claude Code agents; no Semantic Scholar, arXiv, or other API access

## Limitations and Decisions

1. **Agent rate limits:** 4 of 8 background agents hit rate limits during post-write verification steps. All agents completed their primary file writes before the limit; only verification logs were truncated. File completeness was confirmed via section heading grep and word count.

2. **LaTeX in PDF:** fpdf2 core fonts (Helvetica) cannot render LaTeX mathematical notation. The combined PDF contains raw LaTeX strings (e.g., `\chi^2`, `\geq`) where the markdown source uses `$...$` delimited math. The markdown source files are the authoritative versions; the PDF is for reading convenience.

3. **Figure embedding heuristic:** The combined PDF generator uses a keyword-matching heuristic to insert figures near their first textual reference. This produces reasonable but not optimal placement; some figures appear slightly after their first mention rather than precisely at the reference point.

4. **Bold text limitation:** fpdf2 core fonts do not support inline bold within a paragraph. Bold-lead paragraphs (e.g., "**Stage 1:** description") are rendered as plain text with the label prepended. The visual distinction between label and body is lost in the PDF but preserved in the markdown.

5. **Section exclusion:** Introduction and Related Work were excluded per user decision. This means the combined PDF starts at Section 3 (Methods) with no preceding framing. Forward references from Results/Discussion to Sections 1-2 have not been verified against the current Introduction text.

6. **Writing agent independence:** Each agent wrote independently without reading other agents' output. Cross-section consistency (e.g., Discussion referring to specific Results subsection numbers) was ensured by providing identical data and structural specifications in all agent prompts, but minor inconsistencies may exist at section boundaries.
