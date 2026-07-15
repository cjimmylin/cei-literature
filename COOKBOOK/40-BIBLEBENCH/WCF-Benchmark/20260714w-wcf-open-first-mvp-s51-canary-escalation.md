# WCF-Bench Open-First MVP — Session 51 OAuth Canary Escalation

**Date:** 2026-07-14  
**Status:** STOPPED · NEW P1 · OWNER RULING REQUIRED  
**Spend:** `$0.00` OpenRouter · `0` Codex-OAuth tasks · `0` inference calls

> **EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## What passed before the stop

- Jimmy's two named Session-50 custody fixes passed fresh specification and quality
  re-review.
- Jimmy amended the provider-price gate to require at least one eligible endpoint at or
  below the frozen ceiling. The minimal TDD correction passed fresh specification and
  quality review; its one P2-only diagnostic-message imprecision is disclosed and deferred.
- The new append-only public preflight at
  `07-PILOTS/20260714-open-first-mvp-authorized-preflight-v2/` is
  **EXECUTABLE-MANIFEST-INPUT** for the exact six-model roster.
- Forecast: `$6.254185070` no-retry, `$6.852411468` registered SUT-attempt envelope,
  `$8.57` proposed cap. Public snapshot hash:
  `f7755b9a22f2b1e81ed3ebb5825af3390235776a0f6d25858e19a14801f7afe1`.
- Sanitized balance check found `$298.376107379` remaining; `codex login status` reported
  the existing ChatGPT login. No top-up was needed or performed.

## New P1

The fresh specification review of the zero-dollar canary seam reproduced a retry-boundary
violation in `04-HARNESS/open_first_mvp_oauth_canary.py`:

1. an eight-record OPEN batch may return zero valid records on the initial attempt and the
   adapter's two registered missing/malformed-record retries;
2. after those three attempts are exhausted, `run_canary()` converts the remaining missing
   IDs into a generic mechanical error; and
3. the generic handler then grants the separate four-record fallback.

The deterministic reproduction incorrectly passed after task sizes
`[8, 8, 8, 4, 4, 4, 4]`. The same records therefore exceeded the frozen “at most two
retries” rule. This is a protocol P1, not a mechanical P2/P3 disclosure.

## Smallest bounded correction

Permit the four-record fallback only when the initial eight-record attempt fails as a true
process-level mechanical batch failure before the adapter begins missing-record retries.
If the adapter exhausts its initial plus two missing/malformed-record attempts, return FAIL
with no batch-four fallback. Add one deterministic regression for this exact case; then run
named-only specification and quality re-reviews.

## Owner choice

- **FIX:** authorize only the correction and regression above plus named-only reviews. If
  both pass, resume the already-registered balance/canary/live-run sequence under the same
  cumulative `$10.00` cap.
- **DEFER:** keep the executable manifest and all offline work, mark the canary seam
  non-executable, and return to the accepted exploratory-MVP stop.

Recommended: **FIX**. It is a small, deterministic retry-accounting correction that is
required before any OAuth task; no roster, protocol, price, prompt, or spending change is
needed.
