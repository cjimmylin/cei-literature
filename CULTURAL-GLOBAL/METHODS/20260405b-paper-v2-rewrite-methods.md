# Methods: Paper V2 Rewrite — Integrated Three-Study Design

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/PAPER-V2/`

## Data and Materials

The paper V2 integrates content from two previously separate documents into a unified three-study design:

1. **Primary corpus analysis paper** (`PAPER/00-abstract.md` through `10-references.md`): 9 section files totaling ~12,992 words covering 2,329 papers across 34 normative dimensions, gold standard validation (520 papers), WEIRD score operationalization, and regional cluster analysis.

2. **Benchmark meta-evaluation report** (`STATISTICS/20260404-benchmark-analysis-report.md`): ~10,000-word report covering 218 benchmarks, 96-feature taxonomy, TOPSIS/ELECTRE III rankings, 10 self-administration trials (CC1-CC10, 380 items), and multi-model replication across 10 LLMs from 3 providers.

3. **Supporting data**: Council deliberation documents (`COUNCIL/`), cross-model analysis (`METHODS/20260404-council-cross-model-analysis.md`), 80 trial JSON files (`TRIALS/`), pre-computed dashboard analytics (`DASHBOARD/benchmark-data.js`).

4. **Existing figures**: 12 PNG files in `PAPER/figures/` generated during Sessions 1-5 using matplotlib/seaborn from the analysis pipeline.

## Procedure

### Paper Architecture Design
A plan was developed and approved specifying: (a) fully integrated narrative merging corpus analysis and benchmark evaluation into one paper, (b) "triple bind" framing as the narrative climax, (c) target venue of Nature Human Behaviour / Science / PNAS, (d) fresh 12-member expert council, (e) new `PAPER-V2/` output directory.

### Council Composition
A fresh 12-member council was designed to balance tradition-specific expertise (Confucian, Islamic, Ubuntu, Indigenous, Cross-Cultural Psychology, Buddhist/Dharmic) with methodological and narrative expertise (AI Safety, Bibliometrics, Decolonial Studies, Science Communication, AI Governance, Philosophy of Science). The council operates under three standing rules: tradition veto authority (Tier 1 specialists), anti-essentialization mandate ("scholars argue X" not "tradition holds X"), and internal diversity acknowledgment.

### Section Writing
Sections were written using parallel agent dispatch for independent sections (Methods, Study 1, Study 2 written simultaneously) and sequential writing for dependent sections (Study 3, Synthesis, Discussion, Conclusion, Abstract written after earlier sections were complete). Each section drew on specific source files:

- **Methods** (02-methods.md): Synthesized from `PAPER/03-methodology.md` + benchmark report Sections 3.1-3.5 + trial protocol documentation
- **Study 1 Results** (03-results-corpus.md): Consolidated from `PAPER/04-results-regional.md` through `07-results-gaps.md` (4 files → 1)
- **Study 2 Results** (04-results-benchmarks.md): Extracted from benchmark report Sections 4-7 and 9
- **Study 3 Results** (05-results-trials.md): Extracted from benchmark report Sections 8-9 + `METHODS/20260404-council-cross-model-analysis.md`
- **Synthesis** (06-results-synthesis.md): New content connecting all three studies
- **Discussion** (07-discussion.md): Expanded from `PAPER/08-discussion.md` + benchmark report Section 10-11
- **Conclusion** (08-conclusion.md): Expanded from `PAPER/09-conclusion.md`
- **References** (09-references.md): Merged from `PAPER/10-references.md` + benchmark report references

### Figure Generation
Six new figures were generated using matplotlib 3.9.4 with the Okabe-Ito colorblind-safe palette:

- **Fig 5** (benchmark-landscape-clusters): Donut chart + grouped bar comparison of cluster feature profiles
- **Fig 6** (concept-coverage-gaps): Horizontal stacked bar showing 3/44 measured concepts across 7 traditions
- **Fig 7** (cultural-map-position): Scatter plot on Inglehart-Welzel axes with Claude star marker and dashed <15% population boundary
- **Fig 8** (mfq-profile-comparison): 4-group bar chart (Claude, Liberal, Conservative, Non-WEIRD) across 5 MFQ foundations
- **Fig 9** (rlhf-conflict-taxonomy): Dual-panel — horizontal bars for conflict counts + heatmap for tradition impact matrix
- **Fig 10** (triple-bind-diagram): Three-circle diagram with directional arrows showing self-reinforcing cycle

Four existing figures (world map, heatmap, dendrogram, correspondence biplot) were copied unchanged. Seven existing figures were moved to supplementary.

### Table Generation
Table PDFs were generated using fpdf2 2.8.4. Main tables PDF contains 10 tables across 3 landscape pages. Supplementary tables PDF was expanded from 2 to 8 tables across 8 pages, including the full TOPSIS top 50 rankings, RLHF conflict breakdown by category × trial, representative conflict examples, and cross-model agreement matrices.

### Combined PDF Assembly
A combined PDF was assembled using fpdf2 with Arial Unicode font support, rendering all 8 text sections as formatted markdown-to-PDF, embedding all 17 figures (10 main + 7 supplementary) as inline images with captions, and including section-break banners, headers, footers, and a title page with table of contents. The resulting document is 75 pages, 3.3 MB.

### Quality Assurance
Anti-essentialization was verified by grepping all markdown files for prohibited formulations ("Islam holds," "Confucianism says," "tradition holds," "culture believes"). Zero violations were found (3 matches were meta-references to the anti-essentialization rule itself or model-framing descriptions, all appropriate in context).

## Computational Environment

- **Python:** 3.9 (via `.venv`)
- **fpdf2:** 2.8.4 (PDF generation with Unicode support)
- **matplotlib:** 3.9.4 (figure generation)
- **numpy:** 2.0.2 (numerical computation)
- **seaborn:** 0.13.2 (statistical visualization)
- **Pillow:** (image handling for PDF embedding)
- **Font:** Arial Unicode TTF (`/Library/Fonts/Arial Unicode.ttf`)
- **Platform:** macOS Darwin 25.3.0

## Limitations and Decisions

1. **Introduction not rewritten**: Per user instruction, the v1 introduction (12.8K words) was carried forward without modification. This creates a coherence gap — the intro references a 20-member council and doesn't frame the three-study design. This is the highest-priority remaining task.

2. **Word count variation**: Study 3 Results (2,817 words) and Discussion (3,199 words) came in below initial targets (3,500-4,500 and 4,500-5,500 respectively). Content is complete but denser than estimated due to effective use of tables for data presentation.

3. **Table PDF Unicode limitation**: The main tables PDF uses Helvetica (no Unicode support), which cannot render non-Latin characters. The combined PDF uses Arial Unicode and renders correctly. For journal submission, LaTeX with proper font support will resolve this.

4. **Figure style**: New figures use matplotlib defaults with Okabe-Ito palette. Journal submission may require design polish (higher DPI, consistent font sizing, potential vector format output).

5. **Parallel agent rate limits**: Two of three parallel writing agents hit API rate limits during the session. The affected sections (Study 3, Discussion) were written directly rather than by agents, resulting in the same quality but slightly different prose style.
