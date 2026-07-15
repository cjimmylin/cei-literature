# Jimmy Authorization Record — Pilot 2 Residual Cross-Seam FIX

**Date:** 2026-07-15
**Status:** FIX AUTHORIZED · EXACT RESIDUALS ONLY

Jimmy selected **FIX** at the Session-58 specification re-review gate recorded in
`20260715t-wcf-pilot2-s58-spec-rereview-stop.md`.

Jimmy then explicitly directed Codex to authorize and execute the shortest path to
empirical execution described in the side-thread progress summary. Under the existing
gates, this confirms execution through the residual FIX, both reviews, and one
public-catalog-only zero-paid preflight. Empirical inference still requires the separate
amount-specific approval that can be requested only after the refreshed cap exists.

## Authorized corrections

One exact residual correction cycle may add regression tests and the minimum code needed
for only these seven residuals:

1. Accept a valid preflight manifest whose refreshed pinned-endpoint prices are below the
   frozen design ceilings, and use its frozen `max_price` in SUT requests.
2. Return the required balance in the zero-paid preflight packet without accessing an
   account balance.
3. Reject internal `prepare_run` and `execute` entry points when paid-inference authority
   remains false.
4. Require a registered balance check before live transport construction.
5. Require all five sequential first real cells to pass before model shards begin.
6. Add the full-run judge driver that builds route-specific calls, dynamically batches,
   invokes the existing Codex-OAuth adapter, and immediately persists valid verdicts.
7. Accept the correct 1,130 scorable-cell report geometry while keeping the 20 contested
   cells separate from the 1,110 scalar-eligible cells.

After the correction, the same specification reviewer inspects only these residuals. A
fresh quality reviewer may run only after specification PASS. If both pass, the existing
plan authorizes one public-catalog-only zero-paid preflight and a stop at the refreshed
amount-specific gate.

## Unchanged boundaries

This FIX does not alter the five-SUT roster, provider pins, reasoning settings, 1,740
logical judge decisions, existing scorer arithmetic, judge prompts, bank, claim boundary,
Pilot 1, PPP-1, or the accepted paper.

It authorizes no credential or balance access, Codex-OAuth task, OpenRouter inference,
paid call, top-up, cap, substitution, fallback, perturbation, rerun, ranking, release or
publication claim, T4 work, or accepted-manuscript change.

The permanent label remains:

> **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**
