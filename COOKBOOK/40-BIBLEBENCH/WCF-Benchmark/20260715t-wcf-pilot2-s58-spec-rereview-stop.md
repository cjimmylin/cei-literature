# WCF-Bench Pilot 2 — Session-58 Specification Re-review Stop

**Date:** 2026-07-15
**Status:** OWNER FIX / DEFER RULING REQUIRED · ZERO-PAID PREFLIGHT NOT RUN

> **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Gate outcome

Jimmy's Session-58 YES ruling authorized route/call-specific structured judge schemas and
the still-unused single four-P1 correction cycle. The implementation agent completed that
cycle with 34/34 focused and 860/860 full offline tests green. The required named-only
specification re-review nevertheless returned **FAIL**:

| Original named P1 | Result |
|---|---|
| `PILOT2-PUBLIC-PREFLIGHT-PACKET` | FAIL |
| `PILOT2-LIVE-EXECUTION-CUSTODY` | FAIL |
| `PILOT2-OAUTH-CANARY-CUSTODY` | PASS |
| `PILOT2-SCORING-SUPPLEMENT` | FAIL |

The route-specific schemas themselves passed: they preserve `348 × 5 = 1,740` logical
judge decisions and replay the unchanged scorers. The remaining failures are cross-seam
P1s inside three original categories.

## Exact residual failures

1. **Public preflight / request consistency**
   - A successful preflight leaves `auth_balance.required_balance_usd` unset instead of
     returning the required balance.
   - The preflight correctly freezes current pinned-endpoint prices when they are below
     the design ceilings, but request construction still demands the static ceiling prices.
     A valid lower-price manifest therefore stops as contract drift.
2. **Live authorization, balance, and first-cell gate**
   - Internal `prepare_run` and `execute` paths accept a manifest whose paid-inference
     authorization remains false; only the CLI wrapper rejects it.
   - The live CLI has no registered balance check before transport creation.
   - The sequential first-cell results are not required to be five PASS results before
     the three model shards start.
3. **Full-run judge driver and report geometry**
   - The structured schemas and analysis exist, but there is no full-run driver that
     builds, dynamically batches, invokes, and immediately persists `judge-verdicts.jsonl`.
   - The report gate expects 1,110 scalar cells, while valid analysis retains all 1,130
     scorable cells, including 20 contested cells that must remain separate from scalar
     aggregation. A valid complete dataset is rejected.

## Why work stopped

The authorized single named-blocker correction cycle is exhausted. Quality review cannot
start after specification FAIL, and the public zero-paid preflight cannot run before both
reviews pass. Continuing would require a second correction cycle not covered by the YES
ruling.

## Requested owner ruling

- **FIX (recommended):** authorize one exact residual correction cycle limited to the
  failures above, with regression tests for lower refreshed prices, required balance,
  internal authorization, balance-before-transport, five first-cell PASS gating, the
  full-run persisted judge driver, and 1,130-cell report acceptance. Then perform the same
  named-only specification re-review and, only after PASS, one fresh quality review.
- **DEFER:** retain the current offline checkpoint as incomplete and do not run Pilot 2
  preflight or execution.

Neither choice authorizes credential access, balance access, OAuth tasks, OpenRouter
inference, paid calls, top-up, or the provisional cap. Under FIX, one public-catalog-only
zero-paid preflight may run only after both reviews pass.

## Calls and spend

- Public metadata calls: zero.
- Auth or balance calls: zero.
- Codex-OAuth judge tasks: zero.
- OpenRouter inference calls: zero.
- Spend: `$0.00`.
