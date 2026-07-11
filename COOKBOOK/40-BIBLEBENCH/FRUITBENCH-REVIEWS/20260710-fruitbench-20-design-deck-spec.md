# FruitBench 20-Design Overview Deck - Production Specification

**Date:** 2026-07-10  
**Status:** Approved concept; written specification awaiting final user review  
**Audience:** Internal research collaborators and academic conference audiences  
**Scope:** All ten FruitBench v1 designs and all ten FruitBench v2 designs

## 1. Purpose

Create a conference-readable overview of the complete 20-design FruitBench portfolio. The deck must explain how the v1 fruit-major instruments and v2 method-major instruments form a complementary measurement lattice, while giving every design enough space to communicate its construct, method, representative case, advantages, limitations, and current readiness.

The presentation must support internal portfolio decisions and academic discussion. It must not imply empirical validation where only a design scaffold, synthetic harness validation, or preliminary evidence exists.

## 2. Narrative architecture

The deck will use the approved **Hybrid Portfolio Story** structure: conference-style scientific hooks combined with a stable comparison spine.

Planned sequence, approximately 31 slides:

1. Title and program thesis.
2. Why positive-character evaluation matters.
3. The 20-instrument lattice: ten fruit-major and ten method-major designs.
4. Status and evidence legend.
5. FruitBench v1 section opener.
6-15. One full slide for each v1 design.
16. v1 synthesis: shared strengths, gaps, and complementarities.
17. FruitBench v2 section opener.
18-27. One full slide for each v2 design.
28. v1-to-v2 crosswalk showing major triangulation relationships.
29. Portfolio-wide advantages and validity risks.
30. Implementation and validation roadmap.
31. Conclusions and source notes.

The sequence may expand by no more than two slides if source notes or the crosswalk cannot remain readable at conference font sizes.

## 3. Per-design content contract

Every design receives one full slide containing:

1. codename, portfolio, and construct or methodology;
2. a scientific-question headline written for the audience;
3. concise design mechanics;
4. a representative case;
5. the headline metric or estimand;
6. the principal methodological advantage;
7. the principal limitation or validity risk;
8. the nearest complementary v1 or v2 design; and
9. dated implementation/readiness status.

Case examples must be labeled **bank-derived** when taken from an implemented bank and **illustrative** when paraphrased from a design brief. No illustrative case may be described as tested evidence.

## 4. Evidence and readiness language

Readiness is decomposed into separate milestones:

- **DESIGNED:** construct and instrument scaffold documented.
- **P1 BUILT:** item/substrate bank and runnable pilot harness implemented.
- **HARDENING:** a built P1 is undergoing validity, cue, identity, judge, or execution repairs.
- **LIVE-VALIDATED:** required live subjects, eligible judges, human calibration, controls, and registered gates have passed.

Synthetic outputs are labeled as harness validation only. Preliminary model runs are not treated as formal evidence. THORNS and UNFENCED must be described using the latest dated worklist and handoff evidence, including any unresolved human, judge, cue, or live-validity gates.

## 5. Source hierarchy

Content will be derived in this order:

1. individual v1 and v2 design briefs for construct, methodology, metric, and intended P1 case structure;
2. `FRUITBENCH/DESIGNS/00-fruitbench-portfolio.md` and `FRUITBENCH-v2/00-fruitbench-v2-portfolio.md` for portfolio framing and cross-design relationships;
3. the latest dated `FRUITBENCH-REVIEWS` worklist, handoffs, and readiness reports for implementation status;
4. implemented banks and pilot reports for bank-derived examples; and
5. shared FruitBench evidence and validity documents for portfolio-wide caveats.

Conflicts are resolved in favor of the latest binding dated handoff or ruling. Any unresolved conflict is stated rather than silently reconciled.

## 6. Visual system

- **Style:** editorial research presentation, not a dashboard or stock-photo collage.
- **Foundation:** deep navy and warm ivory.
- **v1 accent:** terracotta.
- **v2 accent:** teal or vine green.
- **Status accent:** restrained amber, gray, green, or red according to milestone; color never carries status without text.
- **Typography:** at least 50 pt deck title, 35 pt slide titles, 24 pt subheads, and 16 pt body text.
- **Design-slide composition:** scientific hook at top; method explanation on the left; concrete case on the right; advantage and limitation anchored along the bottom; readiness and source in the footer.
- **Portfolio visuals:** one lattice diagram, one v1-to-v2 crosswalk, and restrained method-specific cues only where they improve comprehension.
- **Accessibility:** adequate contrast, no critical meaning encoded only in color, no clipped or wrapped one-line titles.

## 7. Deliverables

Final files will be placed under `FRUITBENCH-REVIEWS/DECKS/`:

- `fruitbench-20-designs-overview.md` - editable Markdown source with slide boundaries and source notes;
- `fruitbench-20-designs-overview.pptx` - compatibility presentation;
- `fruitbench-20-designs-overview-slides.pdf` - widescreen presentation PDF; and
- `fruitbench-20-designs-overview-handout.pdf` - printer-friendly portrait handout.

The Markdown file is the editorial source of truth. The rendered presentation may shorten visible copy to preserve layout, but it may not change claims, status, or source meaning.

## 8. Production and verification

1. Inventory all 20 briefs and extract structured facts into source notes.
2. Draft the complete Markdown deck first.
3. Check the Markdown against all 20 design briefs and the latest status evidence.
4. Build the PowerPoint presentation from the approved Markdown content using the artifact-tool workflow.
5. Render every slide to images and inspect each at full size.
6. Run overflow and overlap checks; correct all unintended clipping, wrapping, or collisions.
7. Export the widescreen PDF and render every PDF page for visual inspection.
8. Create the printer-friendly handout PDF and render every page for visual inspection.
9. Confirm page counts, headings, slide numbering, status labels, source footers, and all 20 required design slides.

## 9. Acceptance criteria

The work is complete only when:

- all 20 named designs appear exactly once as full design slides;
- every design slide contains all nine required content fields;
- v1 and v2 are correctly distinguished;
- examples are labeled bank-derived or illustrative;
- advantages and limitations are specific to the design;
- readiness claims are dated and evidence-appropriate;
- the Markdown, PowerPoint, slide PDF, and handout PDF agree on substantive claims;
- no slide or PDF page has unintended overflow, overlap, clipping, broken glyphs, or unreadable text; and
- final files contain no placeholders, internal planning notes, or unsupported performance claims.

## 10. Scope exclusions

This deck does not run benchmarks, alter benchmark designs, adjudicate pending governance rulings, fabricate human calibration, or promote preliminary results to formal evidence. It summarizes the portfolio and its documented readiness state.
