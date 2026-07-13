# BibleBench Nine Design Reports - Quality Assurance

**Built and inspected:** 2026-07-13

**Status:** `PRE-EMPIRICAL DESIGN REPORT`

## Integrated machine checks

- The registry resolves exactly nine stable PDF filenames and every declared local source.
- Two consecutive builds are byte-identical.
- All 86 pages are nonempty and have searchable text, page numbers, and consistent metadata.
- Every report identifies Jimmy Lin as author and `BibleBench design-report builder` as creator.
- Every cover and page footer states `PRE-EMPIRICAL DESIGN REPORT`.
- Report 4 contains all 30 unique Ten Commandments design identifiers, `01A` through `10C`.
- Citation keys are rendered as human-readable author-year references; no tool tokens, unresolved citation tokens, or incomplete-work markers remain.
- The analysis report retains `PENDING_EMPIRICAL_RUN` and explicitly excludes leaderboards, p-values, composites, best-model claims, cue effects, capability-adjusted attribution, and family-level estimates.
- No PDF contains a model outcome, ranking, composite, or empirical performance claim.

## Artifact register

| PDF | Pages | SHA-256 | Dense page inspected |
|---|---:|---|---:|
| `01-biblebench-consolidated-design-and-methods.pdf` | 9 | `58de1e9164400fa0e881406b00bcf876a2833ffc6fe7ab1546cf3a479a17f854` | 9 |
| `02-fruitbench-design-report.pdf` | 10 | `0726f46fd2f2831aadc01b2d7a46498df845b4deb303b2aef98d6523794b5ed4` | 8 |
| `03-corinthlove-design-report.pdf` | 10 | `77f9ebb27f7bf03db61cc0cf87e4794553f743117af90c887326cf5c7acba453` | 7 |
| `04-10cbench-30-design-atlas.pdf` | 27 | `e59fed54a0b95c46d90527aefb0615760474a9b4900b6248ac7eee0f36b519b1` | 25 |
| `05-sermonmount-design-report.pdf` | 9 | `0e6f9f44ed046885292d9245faf26c5ba2e128d04450f723f0efdfc45943a9c2` | 8 |
| `06-shared-episode-protocol-and-custody.pdf` | 2 | `796c3adcfe831d874c941e13f7ec4b6d707798fe68199b9f2c30784ed81ea02f` | 2 |
| `07-human-adjudication-handbook.pdf` | 12 | `f65cd9a6d3455648851a18d901f8becce51def65f19ddb119ea84ed01ad9efaa` | 10 |
| `08-reproducibility-ethics-and-data-card.pdf` | 4 | `0011e52dec953ac6092f7189bd2dfaa93fc851d77593a7c679592e98d3229399` | 3 |
| `09-analysis-tables-figures-and-claims-boundary.pdf` | 3 | `e80cf0c2d8ec6b6966c6f933db6c1a33e18cff2aff8fd51aa141cb660b928fbe` | 3 |

## Visual inspection

All 86 pages were rendered with Poppler at 110 DPI. Every rendered page was inspected in report-level contact sheets; the dense representative pages listed above were also inspected at original render resolution. Reports 4 and 6 were rerendered in full after the P1 protocol-boundary repairs.

The final inspection found:

- no clipped or overlapping text;
- no blank or nearly empty terminal pages;
- no broken glyphs, black boxes, or unreadable identifiers;
- consistent margins, headers, footers, numbering, color, and type hierarchy;
- legible episode inventories, tables, provenance lines, and bibliography entries;
- correct cover labels and section transitions; and
- clear visible separation between pre-empirical content and the pending empirical phase.

Rendered PNGs and contact sheets are temporary QA intermediates and are not deliverables.
