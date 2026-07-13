# WCF-Bench T4 zero-paid preflight implementation plan

**Date:** 2026-07-13
**Design:** `20260713f-codex-t4-zero-paid-preflight-design.md`
**Execution mode:** fresh implementation agent, then independent specification review,
then independent quality review. Fixes are limited to named blockers.

## Task 1 — Failing contract tests

Add `04-HARNESS/tests/test_t4_preflight.py` with the minimum tests required to prove:

1. default mode has no network and no writes;
2. metadata mode exposes only the two authorized OpenRouter GET seams and cannot reach a
   completion endpoint;
3. R59.2 primary/fallback/pin/dedup/anti-leak/n<8 behavior;
4. exact-source capability normalization, missingness, PCA orientation, and frontier;
5. deterministic disjoint 23/100 G5c sample;
6. frozen-bank base, variant, G5b, G5c, and ladder call counts;
7. fail-loud catalog pricing and exact subtotal/cap/top-up arithmetic;
8. five-cheapest base-shard ordering and membership;
9. runtime arithmetic from the immutable T3 timestamps;
10. exclusive immutable writes, canary presence, and secret non-disclosure.

**Done when:** focused tests fail for missing behavior.
**Do not:** modify bank, prompts, judge manifest, existing runs, or unrelated harness code.

## Task 2 — Minimal controller

Add `04-HARNESS/t4_preflight.py`. Reuse existing loader, routing, perturbation, prompt,
manifest, and `mvp` metadata/pricing functions. Implement only the pure interfaces and
thin metadata retrieval boundary specified by the design.

The controller must:

- parse the official LMArena dataset and strict alias map;
- freeze exact official capability rows, leaving unsupported metrics missing;
- resolve roster/frontier/cheap shard mechanically;
- build the exact request schedule, cost plan, runtime, cap/top-up, and branch table;
- write the five frozen artifacts into a new dated directory;
- reject an existing output directory;
- never instantiate a completion client or send a POST.

**Done when:** focused tests pass.
**Do not:** build the paid T4 runner, gate computations, result report, new abstractions, or
dependency changes.

## Task 3 — Specification review and named fixes

A fresh reviewer compares code and tests only against R59.1–R60.3, Jimmy's authorization,
and the dated design. It returns `PASS` or a short list of blocking mismatches. The
implementation agent fixes only those named blockers; re-review verifies only the fixes.

**Done when:** specification review passes.
**Stop rule:** a new potential blocker after the second fix cycle is escalated to Jimmy;
there is no third autonomous cycle.

## Task 4 — Quality review and named fixes

A fresh quality reviewer checks safety, determinism, immutable writes, secret handling,
source provenance, numerical correctness, and test sufficiency. It must not reopen design
or request polish. The implementation agent fixes only named blockers; re-review verifies
only those fixes.

**Done when:** quality review passes under the same two-cycle limit.

## Task 5 — Zero-paid R40.1 execution

Run focused tests and the full offline suite. Then, and only then:

1. source the OpenRouter credential without echoing it;
2. perform the authorized `/api/v1/auth/key` and `/api/v1/models` GETs;
3. retrieve official public capability sources;
4. create a new `07-PILOTS/20260713-t4-preflight-*` directory exclusively;
5. freeze the capability CSV, catalog snapshot, run manifest, cost plan, and report;
6. verify no completion request or paid inference occurred;
7. source-review all exact models, prices, forecasts, caps, top-up, runtime, and branch
   disclosures.

**Done when:** immutable preflight artifacts exist and reproduce the returned ratification
terms.
**Do not:** authorize or execute phase one, select a truncation branch, or infer a paid cap.

## Task 6 — Session close

Update only the execution-plan progress authorized by actual completion, append a dated
handoff, and update every required LIVE dashboard surface. Source-verify the dashboard
under the established local-file browser exception. Run final verification, inspect
`git log -1`, stage explicit WCF paths only, commit, and fast-forward push.

Close with the exact roster, five-cheapest shard, phase-one/full calls and forecast cost,
runtime, current balance/top-up, and minimum required caps for Jimmy's next ratification.
