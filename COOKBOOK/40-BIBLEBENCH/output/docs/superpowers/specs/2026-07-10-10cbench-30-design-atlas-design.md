# 10CBench 30-Design Research Atlas - Design

**Date:** 2026-07-10  
**Status:** Approved for implementation in conversation  
**Audience:** AI evaluation researchers, psychometricians, benchmark builders, and technically sophisticated collaborators

## Communication job

By the end, research collaborators should understand the distinct measurement question, experimental mechanism, main evidence product, strongest contribution, and principal validity risk of all thirty 10CBench designs, because the three generations form a cumulative program rather than thirty interchangeable scenario sets.

## Scope and source boundary

The atlas covers exactly:

- v1 direct constructs: SOVEREIGN, EFFIGY, NAMEDROP, FALLOW, GRAVITAS, UPSTREAM, TRIAD, PROVENANCE, WITNESS, APPETITE.
- v2 orthogonal constructs: TURNCOAT, GOLEM, PROXY, SELAH, HEIRLOOM, KEEPER, PARAMOUR, SKIM, PALTER, ZEROSUM.
- v3 whole-code methodologies: TABLETS, VILLAGE, PRISM, TACIT, CASUIST, LOOPHOLE, VERNACULAR, DISCORD, ASSEMBLY, PREFACE.

Authoritative sources are the three portfolio files and their thirty design briefs under `TENCOMMANDMENTS/`, `TENCOMMANDMENTS-v2/`, and `TENCOMMANDMENTS-v3/`. The v3 design numbers are portfolio sequence numbers, not commandment mappings; v3 must therefore appear as its own whole-code section.

## Narrative architecture

The final atlas contains 39 slides:

1. Minimal cover.
2. One canon, three measurement questions.
3-4. v1/v2 commandment maps for clauses 1-5 and 6-10.
5. v1 section divider.
6-15. Ten v1 profiles.
16. v2 section divider.
17-26. Ten v2 profiles.
27. v3 section divider explaining whole-code methods.
28-37. Ten v3 profiles.
38. Cross-generation synthesis.
39. Shared-stack and build-strategy close.

Every profile includes: design name and generation; concise construct claim; experimental mechanism; concrete source-grounded illustrative case; two strengths; two limitations; and a visible repository-relative source path.

## Visual system

The atlas preserves the existing 10CBench deck's neutral research-grid language: 16:9 white canvas, dark ink, blue v1 accents, purple v2 accents, and amber v3 accents. Profiles use flat editorial composition, generous margins, a claim title, two evidence regions, and a strengths/limits band. Minimum body type is 16 px; titles must remain one line where intended. No decorative imagery is required because the comparison is conceptual and text-led.

## Deliverables

- `output/10cbench-30-designs-overview.md`
- `output/10cbench-30-designs-overview.pptx`
- `output/pdf/10cbench-30-designs-overview.pdf`

The existing `output/10cbench-20-designs-overview.*` files remain unchanged as historical artifacts.

## Quality gates

- Exactly 39 Markdown slides, 39 PPTX slides, and 39 PDF pages.
- Exactly thirty design-profile slides, with all thirty codenames present once as profile titles.
- All visible claims trace to an existing portfolio or design file.
- No placeholders, production notes, malformed glyphs, or unsupported empirical-result claims.
- Presentation overflow diagnostics pass.
- Every final PDF page is rendered and visually inspected at full size; no clipping, overlap, unreadable text, or broken glyphs remain.
- PDF text is searchable and all thirty profile titles are recoverable.

## Non-goals

- No benchmark execution or model calls.
- No edits to source design briefs.
- No claim that scaffold-stage v3 designs have live results.
- No staging, commit, push, or pull request.

