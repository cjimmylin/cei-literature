# SermonMount 20-Design Research Atlas — Deck Design

**Date:** 2026-07-10  
**Status:** Approved in conversation; awaiting written-spec review  
**Audience:** Research collaborators and technically sophisticated readers  
**Communication job:** By the end, research collaborators should understand what each of the twenty SermonMount benchmark designs measures, how it works, where it is strongest and weakest, and how the two portfolios fit together.

## 1. Scope

The atlas covers the ten v1 benchmark designs and ten v2 benchmark designs:

- v1: BLESSED, UNSEEN, PLAINYES, SECONDMILE, TWOMASTERS, LOGSPECK, GOLDGAP, SHEEPSKIN, TELOS, and ROCKSAND.
- v2: PILGRIM, CROSSWINDS, PLUMBLINE, CANTICLE, TESSERA, LEDGER, VILLAGE, SCRIBE, WITNESS, and GLEANING.

The deck gives equal substantive weight to theological rationale and technical methodology. It does not execute, pilot, or alter any benchmark.

## 2. Narrative architecture

The deck is a detailed research atlas of approximately 52 slides:

1. Minimal cover.
2. Why the portfolio contains twenty designs.
3. How v1 and v2 differ and complement one another.
4. How to read each two-slide design profile.
5. v1 section divider.
6. Twenty v1 profile slides: two per design.
7. v1 synthesis: coverage, strengths, overlaps, and gaps.
8. v2 section divider.
9. Twenty v2 profile slides: two per design.
10. v2 synthesis: whole-passage coverage and infrastructure demands.
11. Cross-portfolio complementarity and duplication map.
12. Feasibility and implementation-burden comparison.
13. Current build status and dependency sequence.
14. Recommended research sequencing.
15. Source and interpretation notes.
16. Closing synthesis.

The final slide count may vary by two slides if a comparison table requires splitting for legibility. No individual design profile may be removed or compressed below two slides.

## 3. Repeated design-profile structure

Every design receives two slides with stable information architecture.

### Slide A — Why and what

- Design name, portfolio number, and one-sentence research claim.
- Sermon passage anchor and theological rationale.
- Secular or empirical construct.
- Core methodology and subject-model role.
- Headline metric or evidence product.
- Nearest portfolio boundary or differentiation claim.

### Slide B — How and so what

- A concrete illustrative case grounded in the source design.
- What is manipulated, observed, and scored.
- Two or three major strengths.
- Two or three limitations, validity threats, or implementation risks.
- Feasibility signal: item-bank burden, judge burden, infrastructure burden, and dependency level.

The repeated silhouette supports comparison, while section and synthesis slides vary layout to avoid a monotonous catalog.

## 4. Visual system

The approved style is a neutral research grid derived from the bundled Codex Grid layout system:

- 16:9, 1280 × 720 working canvas.
- White background, black primary type, pale gray evidence fields.
- Restrained light-blue and strong-blue accents only for emphasis and structural comparison.
- Helvetica Neue with Arial-compatible fallback.
- Minimum presentation sizes: 50 px deck title, 35 px slide titles, 24 px subheads, and 16 px body copy.
- Flat, presentation-native composition; no ornamental gradients, heavy shadows, or devotional/manuscript styling.
- Section dividers are sparse. Design profiles use a four-region research layout. Comparison slides use tables or simple matrices only where relationships require them.

The visual treatment deliberately places theological and technical content in one register rather than assigning them different visual authority.

## 5. Source and evaluation policy

The atlas distinguishes three content classes:

1. **Source-grounded claims** — theological anchors, construct definitions, metrics, pilot specifications, and dependencies taken from the design documents.
2. **Illustrative cases** — concise cases reconstructed from instrument sketches or construction instructions and labeled “Illustrative case.”
3. **Critical synthesis** — pros, cons, validity threats, overlap risks, and implementation burden inferred from the documents and labeled as assessment.

Tradition-contested theological claims remain qualified. The deck explains rather than adjudicates theological disputes. It compares v1 focused probes and v2 whole-passage methodologies without presenting either portfolio as inherently superior.

The primary sources are:

- `SERMONMOUNT/DESIGNS/00-sermonmountbench-portfolio.md`
- `SERMONMOUNT/DESIGNS/01-blessed.md` through `10-rocksand.md`
- `SERMONMOUNT-v2/DESIGNS/01-pilgrim.md` through `10-gleaning.md`
- `SERMONMOUNT-v2/DESIGNS/09-witness/README.md`
- `SERMONMOUNT-v2/20260706-PARKED-opus-reentry-prompt.md`

No web research is required unless a source document contains an unresolved external claim that is material to a slide. Any later web-derived claim must use a direct citation and must not replace the repository’s authoritative design language.

## 6. Deliverables

The final output set is:

1. `sermonmount-20-design-research-atlas.md` — canonical Markdown source with slide separators, visible citations, and presenter-readable structure.
2. `sermonmount-20-design-research-atlas.pptx` — editable PowerPoint generated with `@oai/artifact-tool`.
3. `sermonmount-20-design-research-atlas-slides.pdf` — verified widescreen presentation PDF.
4. `sermonmount-20-design-research-atlas-handout.pdf` — verified print-friendly research handout.

Final files live under `SERMONMOUNT-v2/DECKS/`, with PDFs under `SERMONMOUNT-v2/DECKS/output/pdf/`. Scratch rendering, layout JSON, plans, and preview assets remain outside the repository except for the explicitly requested final artifacts.

## 7. Markdown source format

The Markdown source is presentation-oriented and remains useful without rendering:

- YAML metadata at the top.
- `---` separators between slides.
- One H1 slide title per slide.
- Short paragraphs and labeled lists rather than production notes.
- A `Sources` line on every design profile, using repository-relative paths.
- No hidden implementation instructions or unresolved placeholders.

The Markdown is the content authority. Presentation and handout outputs must preserve its claims, examples, assessments, and citations, though line breaks may be shortened for visual fit.

## 8. PDF and rendering strategy

The PowerPoint is generated with the bundled presentation runtime and rendered to a widescreen PDF using the available office/PDF toolchain. The handout is generated separately in a portrait research-document layout so it remains readable when printed; it is not a reduced multi-slide contact sheet.

The handout preserves the same content order and source references but may combine the two slides for a design into a two-page profile.

## 9. Quality assurance

The deliverables are not complete until all checks pass:

- Render every presentation slide to an image and inspect every slide individually at full size.
- Review a deck-level montage for pacing, repetition, and section transitions.
- Run presentation overflow/overlap checks and fix every unintended issue.
- Confirm slide titles do not wrap unexpectedly and body text remains at or above 16 px.
- Render both PDFs to page images and inspect every page.
- Use `pdfinfo` to confirm page size and count.
- Extract text with `pdftotext` or `pypdf` to confirm searchable text and absence of placeholder copy.
- Scan Markdown, PowerPoint-extracted text, and PDFs for `TODO`, `TBD`, lorem ipsum, production instructions, malformed glyphs, and missing design names.
- Verify all twenty designs appear exactly once as two-slide profiles and in the portfolio comparison tables.
- Verify source citations resolve to existing repository files.

## 10. Non-goals and constraints

- No benchmark execution, provider/model calls, secret access, or live evaluation.
- No edits to the twenty source designs or historical WITNESS artifacts.
- No claim that an unpiloted design has empirical results.
- No fabricated quantitative findings.
- No staging, commit, push, or pull request without separate user authorization.
- No source-code or implementation work outside the isolated deck directory.

## 11. Success criteria

The atlas succeeds when a research collaborator can:

1. Explain the distinctive research question and theological anchor of every design.
2. Compare the evidence each design produces.
3. Identify major validity and implementation trade-offs.
4. See where designs complement or duplicate one another.
5. Understand which designs are only specified, which have implementation work, and what dependencies govern the build sequence.
6. Use the Markdown, slide PDF, or handout PDF independently without losing source traceability.
