# WCF-Bench Open-First MVP — Session-53 Same-Cell Request Custody Escalation

**Date:** 2026-07-15
**Status:** OPEN OWNER DECISION · STOPPED BEFORE CATALOG, AUTH, OR INFERENCE
**Decision requested:** exact FIX or DEFER

> **EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Decision

Choose one:

- **FIX:** authorize one deterministic regression and the smallest fail-closed correction
  for an unmatched persisted request belonging to the same cell as a recoverable response,
  followed by named-only specification and quality re-reviews.
- **DEFER:** stop the Open-First adjunct and retain the accepted exploratory MVP unchanged.

No paid call may occur before an exact written FIX and both review passes.

## What the authorized Session-52 fix established

The one recovery regression now proves the intended happy path: when a successful,
response-attributed, fully persisted raw response is uniquely paired with its persisted
request and only the later checkpoint write is missing, resume reconstructs the checkpoint
without calling transport. Malformed, errored, uncosted, duplicate-response, and invalid-
identity evidence stops closed. Named specification re-review passed.

## New quality-review P1

Fresh quality review constructed this deterministic history:

1. One persisted request for a cell.
2. One fully persisted successful, costed response paired to that request.
3. A second persisted request for the same cell with different `cell_attempt` and
   `model_attempt` values, but no persisted response.
4. No checkpoint.

Resume reconstructed the successful response's checkpoint and marked the cell complete.
It did not reject the second unmatched request. That request can represent transport that
was already issued but whose response and attributable cost were not durably captured.
Silently accepting the first pair can therefore hide an unaccounted paid attempt and
violates the registered fail-closed evidence-custody boundary.

## Smallest recommended FIX

- Add one deterministic regression for the exact same-cell unmatched-request history.
- Before reconstructing a checkpoint, require that the cell's complete persisted request
  history contains exactly one request and that it is the unique request paired to the
  sole successful response.
- Any additional same-cell request, regardless of attempt identity, raises `CustodyStop`.
- Re-review only this named blocker. Do not reopen roster, prompt, pricing, retry, cap,
  judging, or general live-seam design.

## Evidence and stop state

- Focused live module after the first fix: **12 passed**.
- Complete offline harness: **824 passed in 150.57 seconds**, exit 0; only existing
  non-failing pytest temporary-directory cleanup warnings.
- Specification re-review: **PASS** after the first named correction cycle.
- Quality review: **P1 FAIL** on the deterministic same-cell unmatched-request probe.
- OpenRouter public catalog GETs this session: **0**.
- OpenRouter auth/balance GETs this session: **0**.
- OpenRouter inference calls: **0**.
- New Codex-OAuth tasks: **0**.
- Session OpenRouter spend: **`$0.00`**.

The exact six-model roster, executable v2 manifest, prior 16/16 zero-dollar OAuth canary,
and cumulative `$10.00` outer authority remain unchanged. The new-P1 automatic stop
controls. No top-up, substitution, fallback, perturbation, rerun, T4 work, ranking,
release claim, accepted-manuscript change, or publication claim occurred.
