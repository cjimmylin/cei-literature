# WALKWORTHY — Jimmy PR-28 Runtime-Materialization Ruling

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Ruler:** Jimmy
**Recorded by:** Codex
**Status:** RATIFIED + CLOSED
**Scope:** Exact mechanical materialization of the frozen G7 paraphrase-author contract

## Binding ruling

Jimmy supplied the following ruling verbatim:

> Ratify PR-28 option 1: materialize the ratified G7 author contract by defining
> `key_direction_summary` as `json.dumps(item.key, ensure_ascii=False, sort_keys=True,
> separators=(",", ":"))`; implement L8 with exact no-flags regex
> `(?<!\w)(?:[1-3]\s+)?[A-Z][A-Za-z]*\.?(?:\s+[A-Z][A-Za-z]*\.?){0,2}\s+\d{1,3}(?::\d{1,3}(?:[-–]\d{1,3})?)?(?!\w)`
> and fail only on matches newly introduced versus the corresponding original fields;
> add append-only `validation_pending` after transport so an unsubmitted Jimmy review
> remains pending and consumes no replay, while an explicit review-complete submission
> makes any omitted, malformed, mismatched, non-boolean, refusing, or uncertain required
> result `false`; first parser/Gate-A/semantic failure permits the one byte-identical
> replay, second failure becomes unresolved without replacement, and only all-true
> validation completes the logical key; retain full author/review custody outside the
> body-free spend ledger and keep every PR-18/25/25(a)/26/27 model, call, replay, cost,
> checkpoint, concurrency, denominator, HOLDOUT, substitution, scale-up, and $30 NTE
> boundary unchanged.

## Operational effect

1. PR-28 is closed. The three formerly undefined runtime details now have exact,
   owner-ratified mechanical definitions.
2. Codex may implement the frozen author prompt/parser, Gate A, registered L1–L9 lint,
   Jimmy's PUBLIC-only semantic-review packet, and the append-only validation lifecycle
   under RED→GREEN TDD.
3. A transport-valid author response is not logically complete. It books cost, releases
   the in-flight reservation, and enters `validation_pending` until parser, Gate A, and
   every applicable explicit Jimmy semantic result are all true.
4. Absence of a Jimmy submission is pending and consumes no replay. A submitted review
   is fail-closed under the exact ruling.
5. The first validation failure permits exactly one byte-identical author replay. The
   second failure is unresolved; there is no third call, substitution, item replacement,
   text repair, or denominator change.
6. Full author and human-review custody remains outside the body-free spend ledger.

This ruling adds no call, model, spend, scale-up, or downstream authorization. All frozen
PR-18, PR-25/25(a), PR-26, and PR-27 boundaries remain unchanged.
