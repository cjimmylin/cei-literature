# WALKWORTHY Design 02 labeling helper — specification handoff

**Date:** 2026-07-15

**Agent:** Codex

**Disposition:** conceptual design approved; written specification ready for Jimmy
review; implementation not started

## Paper-facing progress

The rate-limiting paper input remains human labels. This session designed the smallest
offline helper that directly enables the first complete label package: Design 02
primary labels, independent reliability labels, declaration, and turn-indexed
disagreement adjudications.

The authoritative specification is
`20260715-design02-labeling-helper-design.md`. It requires three self-contained
`file://` HTML pages and no local server: a 12-unit/21-turn primary workflow, a separate
four-unit/seven-turn reliability workflow, and a Jimmy finalizer that emits the PR-29
declaration and exact per-turn `turn_state` adjudications.

## Important self-review correction

Design 02 is not one scalar label per CSV row. The existing G4 intake expands a compact
JSON list against one-based stored turn members. The frozen blind CSV contains 12 rows
with turn counts `[2,2,1,2,2,1,2,2,2,2,1,2]`; the registered four-row reliability
packet contains seven turns `[2,2,1,2]`. The specification now requires the UI to split
only on the exact ` ⟦//⟧ ` delimiter, collect one label per response turn, export a
compact ordered JSON list, and put the one-based turn index in each true-disagreement
adjudication.

## Verification performed

- Isolated worktree created from current `origin/main`; unrelated shared-main changes
  were not touched.
- Existing PR-29/G4 baseline: 25/25 tests passed.
- Frozen primary row/turn counts independently read from the blind CSV.
- Existing `judge_validation.py` structured-member and adjudication contracts checked
  directly before finalizing the specification.
- Placeholder, contradiction, and scope review completed; no implementation exists.

## Next trigger

Jimmy reviews the written specification. If approved without changes, Codex writes the
TDD implementation plan; only after that reviewed plan may implementation begin. The
planned implementation directly unlocks Design 02 labeling and does not reopen OPEN6,
G7, model work, or general annotation infrastructure.

## Boundaries

No label value, blank CSV, run data, manuscript/PDF, frozen rule, item/key, gate result,
spend, credential, model output, HOLDOUT path, OPEN6 state, or public-release state was
changed. The temporary visual-companion files are outside the isolated worktree and are
not staged.
