# WALKWORTHY — PR-27 Closed / PR-28 Author-Runtime Stop Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Status:** PR-27 + EXACT OPUS ARTIFACT RATIFIED; PR-28 OPEN; NO CREDENTIAL/CALL/SPEND
**Scope:** WALKWORTHY O5 W5/G7 author-stage implementation only

## Outcome

Jimmy ratified PR-27 option 1 and the complete Opus artifact at exact SHA-256
`59caaa1c055dd1badd16694e078a91a40b18e4e1ebd9f6d15510f89e9f79b320`. The immutable
owner record is `20260713v-jimmy-pr27-contract-ruling.md`. Jimmy is now the non-model,
PUBLIC-only semantic reviewer for `L1_sense`, applicable paired-item `L4`, `L5`, and
`L9`; no model call or spend was added.

Before implementation, the complete baseline passed: **505/505 tests in 135.14 s**. The
only output was the pre-existing macOS pytest temporary-directory cleanup warning; exit
status was zero. The memo hash reproduced exactly.

## Genuine STOP — PR-28

Two parallel read-only audits mapped the frozen contract to production interfaces and
RED-first tests. They independently found three choices the memo names but does not fix:

1. `key_direction_summary` has no exact source/serialization.
2. L8 has no exact Scripture-reference grammar or book/abbreviation set.
3. “missing response = false” does not distinguish an unsubmitted Jimmy review from an
   explicitly closed review with a missing/malformed answer.

The third gap is also a custody-state blocker: `AttemptLedger.finish()` currently marks a
transport-valid response logically complete before parser, Gate A, or Jimmy Gate B can
reject it. This would prevent the ratified same-key replay after a parser/lint failure.

PR-28 recommends canonical JSON of `Item.key`, one exact conservative book-list-free L8
regex, and append-only `validation_pending`: absence waits without consuming a replay;
only an explicit review-complete submission can fail closed. First validation failure
permits one byte-identical replay; second failure becomes unresolved. Full author/review
custody stays outside the body-free spend ledger.

Decision memo: `20260713w-codex-pr28-author-runtime-contract-decision.md`.

## Exact next ruling

> Ratify PR-28 option 1: materialize the ratified G7 author contract by defining
> `key_direction_summary` as `json.dumps(item.key, ensure_ascii=False, sort_keys=True,
> separators=(",", ":"))`; implement L8 with exact no-flags regex
> `(?<!\w)(?:[1-3]\s+)?[A-Z][A-Za-z]*\.?(?:\s+[A-Z][A-Za-z]*\.?){0,2}\s+\d{1,3}(?::\d{1,3}(?:[-–]\d{1,3})?)?(?!\w)` and fail only on matches newly introduced versus the corresponding original fields; add append-only `validation_pending` after transport so an unsubmitted Jimmy review remains pending and consumes no replay, while an explicit review-complete submission makes any omitted, malformed, mismatched, non-boolean, refusing, or uncertain required result `false`; first parser/Gate-A/semantic failure permits the one byte-identical replay, second failure becomes unresolved without replacement, and only all-true validation completes the logical key; retain full author/review custody outside the body-free spend ledger and keep every PR-18/25/25(a)/26/27 model, call, replay, cost, checkpoint, concurrency, denominator, HOLDOUT, substitution, scale-up, and $30 NTE boundary unchanged.

## Custody / spend

- OpenRouter credentials: not sourced or read.
- G7-A1 production run directory: absent.
- Client POSTs: **0**.
- Session spend: **$0.00**.
- No HOLDOUT, labels, item/key/denominator, frozen artifact, historical report, or sibling
  benchmark was edited.
- Subagents were read-only and changed no files.

## Paper-facing progress and next trigger

The exact contract and human reviewer identity are closed, and the implementation blocker
is reduced to one mechanical owner line. No G7 evidence or paper statistic exists yet.
After PR-28, the next paper-facing artifact is the completed 73-item author first-attempt
checkpoint plus Jimmy's semantic-review packet. A fully adjudicated 438-cell surface per
battery remains the G7 evidence trigger; label waves independently trigger G4/PAPER §6.

## Next session

Use dashboard §12. First obtain PR-28 option 1 or an alternative exact materialization.
If ratified, record it immutably; create `test_g7_author_contract.py` first and verify RED;
then implement the minimal author-contract module plus the bounded ledger validation state.
Run focused tests, the full suite once, and recheck all hashes before any credential.
Only then run author first attempts, stop at `validation_pending`, and produce the exact
PUBLIC semantic-review packet for Jimmy. No perturbed-SUT call is permitted in that
session.

On session close: update the dashboard, write a NEW dated handoff, and commit/push only
explicit WALKWORTHY paths with a fast-forward push.
