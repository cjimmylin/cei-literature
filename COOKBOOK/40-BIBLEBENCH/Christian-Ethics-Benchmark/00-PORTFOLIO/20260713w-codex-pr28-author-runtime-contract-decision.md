# WALKWORTHY — PR-28 Author Runtime Materialization Decision

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Author:** Codex
**Status:** RECOMMENDATION FOR JIMMY; AUTHOR CALLS STOPPED
**Scope:** Mechanical materialization of the ratified PR-26/27 author contract only

## Why a ruling is required

After Jimmy ratified the exact Opus memo and PR-27 option 1, two independent read-only
audits mapped the contract to RED-first tests. They reproduced the full artifact hash and
found three runtime details that the memo names but does not define exactly enough to
encode without judgment:

1. §4.1 requires `key_direction_summary` but fixes neither its source nor serialization.
2. L8 requires a new Scripture-reference scan but fixes neither the accepted book-name
   vocabulary nor the exact pattern.
3. §4.1 says a missing Jimmy response is fail-closed `false`, but does not distinguish an
   explicitly completed review with a missing answer from a review Jimmy has not yet
   performed. Treating mere absence as `false` would spend the single replay immediately.

The third gap also exposes a custody-state requirement: the current ledger marks any
transport-valid HTTP response complete before parser, Gate A, or Jimmy Gate B can reject
it. A post-transport validation state is required to preserve the ratified replay rule.

No credential was sourced and no author call was made.

## Option 1 — recommended: fully mechanical, conservative, no new model or spend

### A. Key direction

`key_direction_summary` is a string containing the exact canonical JSON serialization of
the immutable `Item.key` mapping:

```python
json.dumps(item.key, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
```

Serialization failure is fail-closed. No prose summary or new judgment is generated.

### B. L8 defense-in-depth grammar

Use the following exact Python regular expression with no flags:

```text
(?<!\w)(?:[1-3]\s+)?[A-Z][A-Za-z]*\.?(?:\s+[A-Z][A-Za-z]*\.?){0,2}\s+\d{1,3}(?::\d{1,3}(?:[-–]\d{1,3})?)?(?!\w)
```

L8 is `false` only when the candidate changed fields contain a matched string absent from
the corresponding original fields. The pattern is intentionally conservative and
book-list-free; Gate A independently prohibits new quantities and capitalized name-like
tokens, so L8 is defense in depth rather than a semantic Scripture classifier.

### C. Human-review lifecycle and custody

1. A transport-valid author response books its reported cost, releases its in-flight
   reservation, and enters append-only `validation_pending`; it is not logically complete
   and cannot become perturbed-SUT eligible.
2. Parser or Gate A failure immediately records `validation_failed` and consumes the one
   exact replay when the failed attempt is first.
3. Parser + Gate A success emits the exact PUBLIC-only §4.1 packet and remains pending.
4. Mere absence of a Jimmy response remains pending indefinitely and consumes no replay.
5. Only Jimmy's explicit review-complete submission closes a review. At that point an
   omitted required check, malformed/mismatched output, non-boolean, refusal, or explicit
   uncertainty becomes `false` under §4.1.
6. Any first-attempt semantic `false` records `validation_failed` and permits the one
   byte-identical author replay. Any second-attempt parser, Gate A, or semantic failure
   records `unresolved`; no third call, substitution, edit, replacement, or denominator
   change occurs.
7. Only a validated all-true attempt records logical completion and permits
   materialization. Full author responses and Jimmy review packets/outputs are retained
   append-only outside the spend ledger; the spend ledger retains hashes, status, and
   costs but no prompt/response body.

The existing 9,709 logical / 971 replay / 10,680 POST limits, concurrency two, exact
payload identity, price ceilings, checkpoints, and $30 hard NTE are unchanged.

## Option 2 — remain no-call

Keep the ratified contract and implementation work parked until Jimmy supplies different
exact definitions for all three details. No partial implementation or author call occurs.

## Exact requested ruling

> Ratify PR-28 option 1: materialize the ratified G7 author contract by defining
> `key_direction_summary` as `json.dumps(item.key, ensure_ascii=False, sort_keys=True,
> separators=(",", ":"))`; implement L8 with exact no-flags regex
> `(?<!\w)(?:[1-3]\s+)?[A-Z][A-Za-z]*\.?(?:\s+[A-Z][A-Za-z]*\.?){0,2}\s+\d{1,3}(?::\d{1,3}(?:[-–]\d{1,3})?)?(?!\w)` and fail only on matches newly introduced versus the corresponding original fields; add append-only `validation_pending` after transport so an unsubmitted Jimmy review remains pending and consumes no replay, while an explicit review-complete submission makes any omitted, malformed, mismatched, non-boolean, refusing, or uncertain required result `false`; first parser/Gate-A/semantic failure permits the one byte-identical replay, second failure becomes unresolved without replacement, and only all-true validation completes the logical key; retain full author/review custody outside the body-free spend ledger and keep every PR-18/25/25(a)/26/27 model, call, replay, cost, checkpoint, concurrency, denominator, HOLDOUT, substitution, scale-up, and $30 NTE boundary unchanged.
