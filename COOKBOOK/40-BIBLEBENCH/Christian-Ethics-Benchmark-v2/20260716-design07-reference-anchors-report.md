# Design-07 harness-side matched-quality state anchors — closure report (2026-07-16)

## Owner gate outcomes (2026-07-16, in-session, recorded for the PF-003 audit trail)

At the `20260716-pilot-design.md` STOP gate, the owner (Jimmy) ruled:

1. **Pilot spend AUTHORIZED — scope (c): FULL 575 public admins × 5 SUTs, ≈$7.9
   envelope, run as two sequential halves** (single-turn designs ≈$2.3, then
   02/05/07/09 ≈$3.1) with a go/no-go checkpoint between. This is the explicit >$5
   authorization the routine PF-003 gate requires.
2. **Design-07: close the matched-quality-reference residual BEFORE the paid run**
   (overrides the memo's PROVISIONAL-label recommendation). Implemented below.
3. **Both adjudication policy calls RATIFIED:** (i) primaries stay v1-parallel with
   mandatory joint companion reporting; (ii) refusal-taxonomy cells omitted from the
   pilot report (exclusion counts reported instead).

Consequence of (2): the pilot report drops the design-07 PROVISIONAL label; the
remaining 07 caveat is per-turn order-blind judging (adjudication F7), disclosed as a
standing caveat, plus first-use-in-anger disclosure for the new anchors (below).

## What was closed

Reviewer-07 residual (`REVIEWS/20260715-07-seventyseven-v2review.md` §5; carried in
`RULINGS-APPLIED.md` open item 4): the harness half of the design-07 judge-agreement
remedy — bank §5 threat-mitigation row: "coldness and capitulation exemplars supplied;
neutrality check on comfort-heavy vs truth-heavy reference answers of matched quality."

**Main-loop verification before authoring:** neither v1 nor v2 had ever built this.
v1 `harness/config/g5/` holds reference files for designs 06 and 09 only;
`references.py::bank_reference_provider` and `judges.py` contain no design-07 branch.
So closure = authoring new harness content from the bank §5 spec, not porting.

## Implementation

- `walkworthy_inspect/rubrics.py`: design-07 ScoringSpec → `reference_anchored=True`.
- `walkworthy_inspect/scorers.py`: new `_DESIGN07_STATE_ANCHORS` (design-level,
  item-agnostic — zero bank-item content used or paraphrased) served by
  `_references()` for design 07; rendered into every per-turn judge prompt via the
  existing reference block. Five entries, each ≤400 chars (the prompt assembler's
  truncation guard — verified untruncated end-to-end):
  1. **Anchor usage (style-neutrality check)** — classify by moves (wrong named?
     concrete alternative offered?), never tone/eloquence; comfort_only is
     keyed-correct early, failure only at terminal.
  2. **Boundary answer A — comfort_only** and 3. **Boundary answer B —
     faithful_counsel**: a warmth/style **minimal pair with identical opening
     sentences**; B alone names the wrong and moves to an alternative. This forces the
     judge to separate the two chronically-confused states (v1 agreement floor ≈0.222)
     on structure, not style.
  4. **cold_correction exemplar** (names the wrong, never tends the wound) and
  5. **full_validation exemplar** (blesses the vice) — the bank §5 "coldness and
     capitulation exemplars."

Design-level rather than per-item by design: per-item references would be ~54 pieces of
new bank-adjacent content re-opening the ratified 510-item review; state-boundary
calibration is a design-level property, and the per-item discriminators (already in
every 07 item's keyed block, verified reaching the judge prompt via `_keyed_text`)
carry the item-specific half.

## Verification

1. Anchor lengths all ≤400 chars (max 398); all five entries and their closing
   classification notes verified present in a rendered per-turn judge prompt for a real
   public design-07 item (`assemble_rubric_prompt`, unit_label="turn 2").
2. Designs 06/09 reference paths unchanged (06 refs from item extras, 09 refs 3 anchors
   — re-verified post-edit).
3. Mock validation: designs 07 + 02 (shared per-turn scorer path) → both
   `status=success` (`logs/mock-design07-refs/`).

## Disclosure for the pilot report

The anchors' live effect on judge agreement is unmeasured until the pilot's judge-B
re-score (the 07 A-vs-B agreement cell is the designated check — adjudication R4/F2
spirit). The pilot report must note that 07's judge prompt is the one v2 judge-path
surface that intentionally EXTENDS v1 (v1 never built the anchors), so the v1↔v2
judge-path parity claim (`20260715c-`) does not cover the 07 reference block.

## Files changed
- `walkworthy_inspect/rubrics.py` — 07 `reference_anchored=True`.
- `walkworthy_inspect/scorers.py` — `_DESIGN07_STATE_ANCHORS` + `_references()` 07
  branch + docstring.

No changes to banks/, datasets/, metrics, or any existing dated report. v1 untouched.
Canary discipline intact.
