# BibleBench prerelease methods PDF — quality assurance

**Artifact:** `biblebench-methods-prerelease.pdf`<br>
**Built:** 2026-07-13<br>
**Status:** prerelease design and methods; no live-model evidence<br>
**SHA-256:** `15e10a8d9b2a5876f3edecbe978e026f74ff3fec7b85d9f5019679fcfe4b6872`

## Machine checks

- PDF opens through `pypdf` and contains 9 pages.
- Metadata title matches the registered manuscript title.
- Metadata author is `Jimmy Lin`.
- Metadata subject contains both `prerelease` and `no live-model evidence`.
- Extracted text contains Abstract, Planned evaluation, Results, and Local references.
- `PENDING_EMPIRICAL_RUN` appears exactly once.
- The cover contains `Proposal only; $0.00 authorized`.
- The PDF and cost-checkpoint tests pass.
- Two consecutive builds are byte-identical.

## Visual checks

All 9 pages were rendered at 120 DPI with Poppler and inspected individually and
as a contact sheet. The review found:

- no clipped or overlapping text;
- no broken Unicode glyphs in headings, body text, citations, or the module table;
- consistent headers, footers, page numbering, margins, type hierarchy, and color;
- a legible four-module table with repeated visual structure;
- a visible proposal-only cover callout;
- a visible amber `PENDING_EMPIRICAL_RUN` callout in Results; and
- no nearly empty terminal page or orphaned Local references section.

The rendered PNGs were temporary QA intermediates and are not part of the PDF
deliverable.
