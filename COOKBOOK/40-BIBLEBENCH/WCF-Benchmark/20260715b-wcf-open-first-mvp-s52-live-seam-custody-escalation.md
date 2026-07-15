# WCF-Bench Open-First MVP — Session 52 Live-Seam Custody Escalation

**Date:** 2026-07-15
**Status:** STOPPED · NEW P1 · OWNER RULING REQUIRED
**Spend:** `$0.00` OpenRouter · `3` Codex-OAuth canary tasks · `0` inference calls

> **EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## What passed before the stop

- Jimmy's exact Session-51 canary retry-boundary FIX was recorded in
  `20260715a-jimmy-open-first-mvp-s51-canary-fix-authorization-record.md`.
- The one regression failed on the reproduced overrun and passed after the minimal
  correction. Exhausted missing/malformed OPEN records now stop after task sizes
  `[8, 8, 8]` without the four-record fallback; true initial process-level failure still
  receives the registered fallback.
- Fresh named-only specification and quality reviews both passed with no P1 or deferred
  finding.
- The registered zero-dollar Codex-OAuth canary completed **16/16 unique records** in
  **3 tasks**, with no fallback, missing ID, quota warning, tool event, or custody failure.
- A fresh implementation agent built only the minimum offline live SUT seam. Its 11
  focused tests pass; no credential, catalog, balance, or completion request was made.

## New P1

The live seam writes a successful paid response and its authoritative cost to
`raw-evidence.jsonl`, fsyncs that record, and then writes the separate cell checkpoint.
An interruption between those writes creates this state on resume:

1. the response and its cost are durable and counted;
2. the cell is absent from the completed checkpoint set; and
3. the runner may reissue the same already-successful cell as another attempt.

That violates the frozen one-immutable-run/no-rerun boundary and may charge twice for one
cell. It is an evidence-custody and spending P1, not a deferrable mechanical P2/P3.

## Smallest bounded correction

Add one deterministic regression that constructs the response-fsynced/checkpoint-missing
state and proves resume does not call transport for that cell. Make resume recover only a
fully persisted, costed, successful raw response as the completed result; fail closed on
duplicate, malformed, uncosted, errored, or otherwise ambiguous evidence. Then run fresh
named-only specification and quality reviews of this boundary only.

## Owner choice

- **FIX:** authorize only the recovery regression and smallest correction above plus
  named-only reviews. If both pass, resume the already-authorized catalog/balance/live-run
  sequence under the unchanged cumulative `$10.00` cap.
- **DEFER:** preserve the passing zero-dollar canary and offline seam as non-executable
  preparation, and return to the accepted exploratory-MVP stop.

Recommended: **FIX**. No model, prompt, price, roster, retry allowance, judging contract,
claim, or budget change is required.
