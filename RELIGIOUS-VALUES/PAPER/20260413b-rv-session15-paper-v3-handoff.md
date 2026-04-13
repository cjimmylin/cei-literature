# RV Session 15 — Paper v3 Build Handoff

**Date:** 2026-04-13
**Deliverable:** `PAPER-V3/20260413-religious-values-paper-v3.pdf` (68 pages, 1,564 KB)
**Build script:** `PAPER-V3/generate_combined_pdf_v3.py` (forked from v2)
**Scope:** Apply the two residual S14 edits in an immutable fork. `PAPER-V2/` is untouched.

## Why v3

Session 14 delivered Paper v2 (43K words, 67-page PDF) but two residual issues were deferred to keep the v2 delta gate clean:

1. **Opus values_paired footnote** — the Bias-Values Independence analysis (S7.4) tests whether K bias and V (values relevance) scores are independent. The Opus-only subset uses a paired-samples variant (`values_paired`) that was not explicitly labeled in the v2 footnote, creating confusion about whether the reported statistic came from the paired or unpaired arm.
2. **NormEval broken cross-reference** — a sentence in the discussion referenced `@normeval_table` but that table was removed when the NormEval section was trimmed in S13. v2 shipped with a broken cross-reference.

## PAPER-V3 scaffold

Forked from `PAPER-V2/` via `cp -R`. Inventory:

- **9 markdown files** (section order):
  1. `00-frontmatter.md`
  2. `01-abstract.md`
  3. `02-introduction.md`
  4. `03-discussion.md` ← **edited**
  5. `04-methods.md`
  6. `05-supp-methods.md` ← **edited**
  7. `06-results.md`
  8. `07-references.md`
  9. `08-appendices.md`
- **18 figures** in `figures/` (all carried over unchanged; SHA-256 hashes match v2 exactly).
- **Build script:** `generate_combined_pdf_v3.py` (forked from `generate_combined_pdf_v2.py`; only the version string and output filename were changed).
- **Review council:** `review-council-v3/` (carried from v2 as an archive snapshot; no new council was run for v3 because the two edits are non-substantive).

## Edit 1 — Opus values_paired footnote

**File:** `05-supp-methods.md`
**Section:** S7.4 "Bias-Values Independence"
**Change:** added a footnote to the line that reports the Opus-subset independence test, clarifying that the statistic is computed on paired (item, score) observations where both the K-bias and V (values relevance) annotations exist for the same item, and that this is the `values_paired` analysis arm (not the unpaired arm used elsewhere in S7).

The footnote resolves the ambiguity flagged by Critic 2 in the Session 14 synthesis (which was deferred because re-running the bootstrap at the v2 deadline would have missed the v2 deploy window).

## Edit 2 — NormEval citation tidy

**File:** `03-discussion.md`
**Line:** 30
**Change:** removed the sentence "...consistent with the NormEval table (see @normeval_table)..." and replaced it with a self-contained restatement: "...consistent with the broader construct-validity pattern observed in NormEval's normative-ethics scorer audit (citation in references)." The removed cross-reference pointed to a table that had been trimmed from the paper in Session 13 but the sentence was never updated.

The references entry for NormEval is unchanged; only the in-text cross-reference was removed.

## Build output

- **fpdf2 build:** `PAPER-V3/generate_combined_pdf_v3.py` runs clean on Python 3.9.
- **Output PDF:** `PAPER-V3/20260413-religious-values-paper-v3.pdf`
- **Page count:** 68 pages
- **File size:** 1,564 KB
- **No warnings** from fpdf2.
- **No figure regeneration** — all 18 figures were copied verbatim from `PAPER-V2/figures/`.

## Delta gate (PASS)

Ran a `diff -rq PAPER-V2/ PAPER-V3/` restricted to `*.md`:

- Only **2 files differ**: `03-discussion.md` and `05-supp-methods.md`.
- All other markdown files are byte-identical to v2.
- SHA-256 hash comparison on `figures/*.png`: **18 / 18 match** v2 exactly.
- Build script differs (expected; only version string and output filename changed).

This confirms the scope of v3 is exactly what was intended: two surgical edits with no silent downstream effects on figures, numbers, or other sections.

## Non-Latin-1 grep (PASS)

Ran `grep -P "[^\x00-\x7F]"` across `PAPER-V3/*.md`:

- **0 matches** — zero non-ASCII characters in any markdown source file. Romanized Latin-1 / ASCII apostrophes throughout.

## Residual — mean values-relevance clarification (non-blocking)

The cold-reader transcript (run against the v7 dashboard, but the same source numbers flow into the paper) noted that the paper reports two slightly different values-relevance figures:

- **30 / 100** — mean for the top-16 tier (used for the paired t-test in Claim 8).
- **33.6 / 100** — mean for all 50 gate-passers (reported as a corpus-wide descriptive).

Both values are correctly contextualized in the paragraph where they appear, but a plain reader encountering them pages apart may assume one is a typo. A one-line parenthetical on first mention ("...30 / 100 [top-16 tier]; 33.6 / 100 across all 50 gate-passers...") would remove the ambiguity.

This is deferred to **Paper v3.1** as a 15-minute edit that does not require a figure rebuild. Synthesis doc R-22 accepted it as non-blocking for v3.

## Files

- Folder: `PAPER-V3/`
- PDF: `PAPER-V3/20260413-religious-values-paper-v3.pdf`
- Build script: `PAPER-V3/generate_combined_pdf_v3.py`
- Edited markdown: `PAPER-V3/03-discussion.md`, `PAPER-V3/05-supp-methods.md`
- Figures: `PAPER-V3/figures/` (18 PNGs, all hash-matched to v2)
- v2 reference (immutable): `PAPER-V2/`
