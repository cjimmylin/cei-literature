# WALKWORTHY — MVP-A1 PR-21 Custody-Stop Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Status:** PR-20 complete; Judge 1 advanced; paid execution stopped on PR-21

## Paper-facing outcome

- Removed the PR-20 P0 blocker under RED→GREEN TDD.
- Implemented an append-only, exact-unit, one-replay limit for either registered judge.
- Proved a multi-unit replay reuses the identical prompt and changes only the defective
  unit; a second failure stops and later resume makes zero calls.
- Completed the original `WW-05-A03` replay successfully and advanced OpenAI Judge 1 to
  63/180 base records / 163/480 logical units.
- Hit a new evidence-custody P0 at attempt 915: HTTP 200 without `usage.cost`. No verdict
  was written, and no paper result was interpreted.

The next paper-conversion trigger remains a complete zero-unresolved-defect Judge-1 surface
plus a validated pre-Meta checkpoint. Ancillary work was limited to the PR-20 replay seam
because it directly blocked that trigger.

## Verification and immutable state

- Full offline harness: 403/403 passed before paid resume.
- Manifest: 60 PUBLIC items; hash
  `6874ae265588d3b10c6ef11c4b554e21e82c2f1e5d212f9e9254c150d2f40345`.
- SUTs: 180/180; classifier: 156/156; probes: 5/5.
- PR-20 replay: one exact item unit, zero replay defects; original defect retained.
- Attempts: 915 starts / 914 finishes.
- Exposure: $0.432642163 finished + $0.0025024 unresolved reserved = $0.435144563.
- Meta production calls: 0. Checkpoint/summary/scored output: absent.
- HOLDOUT: never loaded. Substitutions: zero. O5: unchanged.

## Next session — PR-21 ruling gate

On session open, read the BibleBench paper-first surfaces (read-only), then local
`00-PORTFOLIO/project-dashboard.html` §1/§12, this handoff, the new PR-21 stop report,
the MVP-A1 authority/order, and PENDING-RULINGS PR-21.

No credential access, ledger repair, retry, checkpoint, Meta call, or results fill is
authorized before Jimmy rules PR-21. Present the exact requested one-liner. If ratified,
implement the special missing-cost finish and one-identical-payload retry under TDD; prove
repeat missing-cost stops before a third call; append the authorized finish for attempt 915;
then resume only the exact missing OpenAI keys. Validate the mandatory checkpoint before
Meta. Preserve 1,834 calls, $5.00 NTE, explicit models/caps/providers, no substitution, and
the descriptive-only claim boundary.

On session close, update the local dashboard, write a NEW dated handoff, and commit/push
only explicit WALKWORTHY paths.
