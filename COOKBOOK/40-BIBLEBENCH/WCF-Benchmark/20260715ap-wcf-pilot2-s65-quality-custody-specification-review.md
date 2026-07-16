# WCF-Bench Pilot 2 Session-65 quality-custody specification review

**Date:** 2026-07-15

**Scope:** named-only review of the two P1 closures authorized by
`20260715ao-jimmy-pilot2-s64-quality-custody-fix-authorization-record.md`

**Result:** **FAIL — one named-blocker correction cycle invoked**

## P1-A — cumulative settlement evidence is not validated

The completed-run validator binds reservations, requests, raw outcomes, actual response
costs, settlements, hashes, model identities, attempts, checkpoints, missingness, and the
registered geometry. It sums actual settlement amounts, but does not validate the persisted
`cumulative_spend_usd` field. Replacing the first completed fixture settlement's cumulative
value with `-999.0` was accepted and returned all 1,150 checkpoints.

The bounded correction is to validate every cumulative settlement value, in evidence order,
against the running total.

## P1-B — lease identity can change while the run parent is created

The lease path uses the nearest existing parent. If a run directory's parent does not exist
when the first process acquires the lease, then appears while that process still holds it, a
second process derives a different lease file and can acquire concurrently. The reviewer
reproduced `SAME_PATH False` and `CONCURRENT_SECOND_ACQUIRED True` for the same resolved run
directory.

The bounded correction is to derive the lease from the resolved run-directory identity in
one stable, already-existing process-global location, independent of run-parent creation.

## Review boundary

The focused authorized tests passed 9/9, but did not cover these bypasses. No semantic drift
was found outside the named validator and lease wrappers; the registered within-process
`ThreadPoolExecutor(max_workers=3)` remains unchanged. Quality review stays blocked until
both named corrections pass specification re-review.

No public metadata, credential/private-balance access, OAuth, inference, empirical run
directory, or spend occurred.
