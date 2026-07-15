# WCF-Bench Pilot 2 Session-64 quality-custody stop

**Date:** 2026-07-15

**Permanent label:** **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Outcome

Jimmy authorized the exact LIVE SEAM FIX. A fresh implementation agent completed the
bounded TDD correction. The first specification review found three named P1s; the same
implementer corrected only those findings, and the named specification re-review passed.
A fresh quality review then found two new P1s. The binding second-cycle stop therefore
fired before credential/private-balance access, OAuth, provider inference, run-directory
creation, or spend.

## New P1-A — completed-run custody is not tied to SUT evidence

`require_completed_run_evidence()` validates phase markers, reservation totals, checkpoint
count, and checkpoint shape, but does not require each checkpoint to match its exact
`sut_request`, raw `sut_response`, cost settlement, attempt identity, response hash, and
model/cost evidence. The positive fixture can therefore synthesize 1,150 checkpoints plus
PASS markers without any SUT requests or responses and still reach judging and analysis.
That can admit non-run data into the empirical packet.

## New P1-B — concurrent processes can bypass the cumulative cap

The run state uses a process-local thread lock and reconstructs spend independently for each
CLI invocation. There is no exclusive run-directory lease before balance validation,
transport construction, or phase dispatch. Two simultaneous phase processes can reserve
against the same prior spend and issue duplicate paid request identities before later
evidence validation detects corruption. The judge output creation path has the same
check-then-append race. This can violate the strict cumulative `$28.13` NTE and evidence
custody.

## Smallest bounded correction

An exact **QUALITY CUSTODY FIX** would add only:

1. completed-run cross-validation that binds every response/error checkpoint to the exact
   request, raw response or registered transport/error record, attempt identity, settlement,
   response hash, model identity, and cost evidence already persisted by the runner; and
2. one exclusive OS-level lease for the shared immutable run directory, acquired before any
   balance/transport/phase or judge dispatch and held for the complete process, failing
   closed on concurrent access.

Use test-first regressions for fabricated checkpoints and concurrent process acquisition,
then one named-only specification re-review and one named-only quality re-review. Do not
change roster, protocol, cap, providers, reasoning, prompts, scorers, geometry, retries,
concurrency within the registered three shards, labels, or claims. P2/P3 findings remain
deferred.

## Owner gate

Jimmy chooses exact **QUALITY CUSTODY FIX**, **DISCLOSE-AND-RUN**, or **DEFER**. The
recommended default is **QUALITY CUSTODY FIX** because disclosure or claim narrowing does
not itself protect the strict spend cap or prevent fabricated evidence from passing the
completion gate.

The existing strict cumulative `$28.13` authority remains recorded but paused and
unconsumed. If the exact bounded correction and both named re-reviews pass, it resumes at
the private-balance gate without a new amount-specific ruling. Any additional new P1 stops.

Session live calls/spend: zero / `$0.00`. Empirical execution remains 0%.
