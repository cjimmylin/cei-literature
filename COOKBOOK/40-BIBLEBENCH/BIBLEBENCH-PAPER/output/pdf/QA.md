# BibleBench prerelease methods PDF — quality assurance

**Artifact:** `biblebench-methods-prerelease.pdf`<br>
**Built:** 2026-07-13<br>
**Status:** prerelease design and methods; no live-model evidence<br>
**SHA-256:** `734f590e4b55a8755da83851d7979037c895e4542993aeaf641bb16b19564fd1`

## Machine checks

- PDF opens through `pypdf` and contains 9 pages.
- Metadata title matches the registered manuscript title.
- Metadata author is `Jimmy Lin`.
- Metadata subject contains both `prerelease` and `no live-model evidence`.
- Extracted text contains Abstract, Planned evaluation, Results, and Local references.
- All 28 manuscript citation occurrences render as human-readable author-year
  citations; extracted text contains zero literal unresolved `[@...]` tokens.
- The rendered bibliography contains all 21 cited sources, separates external
  scholarship from local design provenance, and includes the five passage
  commentaries plus the official Westminster Standards source.
- `PENDING_EMPIRICAL_RUN` appears exactly once.
- The cover contains `Proposal only; $0.00 authorized`.
- The PDF and cost-checkpoint tests pass.
- Two consecutive builds are byte-identical.

## Visual checks

All 9 pages were rendered at 130 DPI and inspected individually. The review
found:

- no clipped or overlapping text;
- no broken Unicode glyphs in headings, body text, citations, or the module table;
- consistent headers, footers, page numbering, margins, type hierarchy, and color;
- a legible four-module table with repeated visual structure;
- legible author-year passage and confessional citations below the module table;
- a complete, legible bibliography with unambiguous 2026a/b/c local-provenance
  entries and no overflow;
- a visible proposal-only cover callout;
- a visible amber `PENDING_EMPIRICAL_RUN` callout in Results; and
- no nearly empty terminal page or orphaned Local references section.

The rendered PNGs were temporary QA intermediates and are not part of the PDF
deliverable.
