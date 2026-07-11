# CORINTHLOVE 30-Design Research Atlas — Deck Design

## Communication job

By the end, researchers and technical audiences should understand how the 30 CORINTHLOVE designs differ, what each design measures, how each experiment works, where it is strongest or weakest, and which concrete situations would exercise it, because the portfolio is organized as three complementary generations of behavioral measurement rather than as 30 disconnected scenario sets.

## Audience and purpose

- Primary audience: AI evaluation researchers, alignment researchers, psychometricians, agent-benchmark developers, and technically sophisticated reviewers.
- Purpose: neutral technical reference and portfolio map, not a fundraising or promotional presentation.
- Central takeaway: v1 measures levels and thresholds, v2 measures dynamics and social embedding, and v3 triangulates a whole-passage behavioral profile and studies its properties.

## Source boundary

The deck will use only the CORINTHLOVE source tree:

- `CORINTHLOVE/DESIGNS/00-10cbench-portfolio.md` and its available design briefs.
- `CORINTHLOVE-v2/00-corinthlove-v2-portfolio.md` and briefs 01–10.
- `CORINTHLOVE-v3/00-corinthlove-v3-portfolio.md` and briefs 01–10.
- Binding gate amendments and current build handoffs where status or limitations depend on them.

No sibling BibleBench portfolio will be referenced. The unverified “moral compactness” statistic remains excluded. Every slide will cite its design brief or portfolio source in a compact footer.

## Narrative and slide architecture

The complete atlas will contain 42 slides:

1. Minimal title slide.
2. The research question: how can love be measured as enacted behavior?
3. Three generations solve three different measurement problems.
4. How to read each design slide.
5. v1 divider: levels, thresholds, curves, and frontiers.
6–15. v1 designs 01–10.
16. v2 divider: dynamics, causal deltas, trajectories, and social systems.
17–26. v2 designs 01–10.
27. v3 divider: whole-profile triangulation and property studies.
28–37. v3 designs 01–10.
38. Thirty designs mapped by unit of analysis and temporal scale.
39. Measurement trade-offs: realism, causal identification, mechanical scoring, and infrastructure cost.
40. Portfolio strengths, shared risks, and complementary coverage.
41. Current build status and cross-version priority path.
42. Source map, caveats, and research-use notes.

The sequence is cumulative: define the measurement problem, explain the three-generation architecture, examine every design, then synthesize the methodological trade-offs and current state.

## Standard design-slide anatomy

Every one of the 30 design slides will contain:

1. Codename, design number, generation, passage anchor, and secular construct.
2. A one-sentence claim-style title explaining the design’s distinct measurement contribution.
3. Experimental design: actors, manipulation, observation window, and scored behavior.
4. Primary metric or model, using the design’s exact terminology.
5. One concrete illustrative case rendered in two or three concise beats.
6. Two or three strengths focused on validity, discrimination, or interpretability.
7. Two or three limitations focused on confounds, infrastructure, annotation burden, saturation, or external validity.
8. Maturity status: design-only, brief available, built, live-tested, deferred, or superseded.

Examples derived from design briefs will be labeled **Illustrative case**. They will never be described as validated bank items unless the source artifacts support that claim.

## Critical treatment

- Strengths and limitations will be analytical rather than promotional.
- v1 designs 08 and 09 will be identified as portfolio-specified but lacking full briefs.
- v1 design 10 NOISYGONG will be marked superseded, with its construct-validation role transferred to the re-scoped v3 analysis.
- v3 designs 07–10 will be described as property studies where the gate amendments reclassify them, not as first-order trait-method cells.
- Human-rater, simulation, long-horizon, multilingual, and multi-agent dependencies will be stated explicitly.
- Proposed anti-saturation mechanisms will be distinguished from empirically demonstrated model discrimination.
- CHARITROC and DIMGLASS status will reflect the available build and live-validation evidence at production time.

## Visual system

- Direction: Research Atlas with concrete examples.
- Canvas: 16:9 widescreen.
- Base: deep navy background with warm off-white typography.
- Generation accents: v1 blue, v2 green, v3 amber.
- Typography: large claim-style titles, compact technical body text, monospaced metric labels, and consistent source footers.
- Composition: flat editorial layouts with strong alignment and generous margins; avoid dashboard-card density.
- Design slides will vary between a left-case/right-method composition and a top-method/bottom-critique composition while preserving the same information hierarchy.
- Native geometric marks may clarify timelines, paired arms, trajectories, or profile vectors; diagrams will be used only when they materially improve understanding.

## Deliverables

Final files will be written under `CORINTHLOVE/DECKS/`:

- `corinthlove-30-design-research-atlas.md` — complete slide-oriented Markdown source.
- `corinthlove-30-design-research-atlas.pdf` — complete 42-slide PDF.
- `corinthlove-v1-design-atlas.pdf` — v1 divider plus its ten designs.
- `corinthlove-v2-design-atlas.pdf` — v2 divider plus its ten designs.
- `corinthlove-v3-design-atlas.pdf` — v3 divider plus its ten designs.

An artifact-tool PowerPoint rendering intermediary may be retained in the output folder for reproducibility, but Markdown and PDF are the requested primary deliverables.

## Production and verification

1. Extract and normalize all 30 design records from the portfolios and available briefs.
2. Author the complete Markdown deck first.
3. Check that the Markdown has exactly 42 slide sections and exactly 30 design slides.
4. Generate the visual deck from the same normalized content using the bundled presentation runtime.
5. Export the complete PDF, then split the three generation PDFs from the verified complete deck.
6. Render every PDF page to PNG.
7. Inspect the full-deck montage for narrative and visual consistency.
8. Inspect every page individually at full size for clipping, overlap, wrapping, unreadable footers, and incorrect generation styling.
9. Extract PDF text and verify that every codename appears, design counts are exact, and no placeholders remain.
10. Run final Markdown/PDF file, page-count, and checksum checks before delivery.

## Acceptance criteria

- Exactly 30 design slides and 42 total slides.
- Every design includes design, metric, concrete example, strengths, limitations, status, and source.
- Every requested PDF renders without clipping, overlap, missing glyphs, or unreadable text.
- The complete PDF has 42 pages; each generation PDF contains its divider and ten design slides.
- No unsupported empirical claim is presented as measured fact.
- No `TODO`, `TBD`, placeholder, hidden production note, or uncited design summary remains.
