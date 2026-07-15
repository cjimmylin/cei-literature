# WCF-Bench Open-First MVP — Session 50 Quality Escalation

**Date:** 2026-07-14 (America/Los_Angeles)
**Status:** PROVISIONAL · RESERVED FOR JIMMY · NO R-NUMBER ASSIGNED
**Empirical status:** NO REFRESHED PREFLIGHT · NO AUTH · NO OAUTH · NO INFERENCE

> **EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Outcome

Jimmy's bounded FIX was implemented with TDD by a fresh implementation agent. The
same specification reviewer re-reviewed only its three named P1s and returned PASS.
A fresh quality reviewer then found two new P1s. The binding second-cycle rule therefore
stopped work before a refreshed public preflight, credential access, OAuth, inference,
or spend.

The checkpoint closes the previously named contract, secret-environment, general
cancellation, and concurrent-reservation gaps. Focused tests are **64/64 green** and
the complete offline harness is **797/797 green**. These results do not override the
two reproduced quality blockers below and do not make the pilot executable.

## New quality-review P1s

1. **Reservation-failure cancellation gap.** In
   `04-HARNESS/open_first_mvp_run.py`, a `budget.reserve()` `TerminalStop` releases the
   shared start lock before reacquiring it to publish cancellation. The reviewer
   deterministically observed another shard enter a cell in that gap. The smallest
   correction is to set cancellation while still holding the start lock and then
   release the lock once.
2. **Settlement failure can be discarded.** If a cell already raised and budget
   settlement also fails, the settlement `TerminalStop` is discarded, cancellation
   remains false, and the reservation remains conservatively held without a terminal
   budget signal. The reviewer reproduced a charged `$2` exception against a `$1`
   reservation yielding the original cell error, `spent_usd=0`, and
   `reserved_usd=1`. The smallest correction is to make settlement failure always
   terminal and publish cancellation while preserving the original cell error as
   context.

## Recommended bounded ruling

**FIX** is recommended. Both changes are small, directly registered strict-stop/strict-
cap requirements. Disclose-and-run is not compatible with the pilot's terminal-stop
and budget-containment contract. Jimmy may instead state **DEFER** to retain the
accepted exploratory MVP and leave this adjunct non-executable.

Suggested exact approval text:

> I authorize one final named-blocker FIX only for the two Session-50 quality P1s.
> Set cancellation while still holding the shared start lock when reservation fails,
> and make every settlement failure a TerminalStop that publishes cancellation even
> when a cell error already exists, preserving that original error as context. Add
> only the two deterministic regressions, re-review only those two blockers, and
> refresh the public-only preflight if and only if both pass. No credential access,
> OpenRouter auth/balance call, OAuth canary, paid inference, top-up, substitution,
> empirical run, rerun, T4, gate, ranking, or manuscript change is authorized.

## Unchanged forecast and authority

The last immutable public packet remains
`07-PILOTS/20260714-open-first-mvp-zero-paid-preflight/`, with `$6.244764270`
no-retry, `$6.842089548` bounded attempt envelope, and an unratified `$8.56` proposed
cap. No new metadata snapshot or executable manifest was created in Session 50. Spend
was `$0`.
