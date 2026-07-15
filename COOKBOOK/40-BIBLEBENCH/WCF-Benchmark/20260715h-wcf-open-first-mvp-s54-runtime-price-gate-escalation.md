# WCF-Bench Open-First MVP — Session-54 Runtime Price-Gate Escalation

**Date:** 2026-07-15
**Status:** OPEN OWNER DECISION · STOPPED BEFORE AUTH, BALANCE, OR INFERENCE
**Decision requested:** exact FIX or DEFER

> **EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Decision

Choose one:

- **FIX:** authorize one TDD regression and the smallest correction making the live
  runtime price gate evaluate current endpoint eligibility against the frozen endpoint
  ceilings, followed by named-only specification and quality reviews.
- **DEFER:** stop the Open-First adjunct and retain the accepted exploratory MVP unchanged.

No credential access, balance check, or paid call may occur before an exact written FIX
and both review passes.

## What completed before the stop

- Jimmy's exact Session-53 same-cell custody FIX was recorded in
  `20260715g-jimmy-open-first-mvp-s53-same-cell-request-fix-authorization-record.md`.
- One TDD regression and the minimal exact-one-request recovery rule passed fresh
  named-only specification and quality reviews with no P1/P2/P3.
- The live module passed 13/13 and the complete offline harness passed 825/825.
- The reviewed correction was committed and pushed to `main` at `6f2511696` before any
  external gate.

## Exact runtime stop

The first registered public runtime validation invoked
`open_first_mvp_run.validate_runtime_catalog()`. That function reads only each model's
aggregate public catalog price through `mvp.price_for()` and compares it directly to the
frozen price ceiling. It raised:

`TerminalStop: runtime price ceiling exceeded: google/gemma-4-31b-it`

The aggregate Gemma row is now `$0.22` prompt / `$0.55` completion per million tokens,
above the frozen `$0.12/$0.37` ceiling.

## Why this is a new P1 rather than an executable price failure

Jimmy's binding provider-price amendment states that a model passes when at least one
parameter-compatible, data-policy-eligible endpoint is available at or below the frozen
prompt/completion ceiling. More expensive endpoints or aggregate catalog rows are excluded
through the registered `max_price`, `require_parameters=true`, and
`data_collection="deny"` request controls; their mere presence is not a blocker.

The registered runtime validator does not fetch or evaluate endpoint rows. A single
public-metadata-only follow-up showed that Gemma still has four current eligible endpoints:

| Provider | Prompt / 1M | Completion / 1M | Within frozen ceiling |
|---|---:|---:|---|
| WandB | `$0.12` | `$0.35` | yes |
| Venice | `$0.12` | `$0.36` | yes |
| Chutes | `$0.12` | `$0.37` | yes |
| DeepInfra | `$0.12` | `$0.37` | yes |

All five other exact models also retained at least one parameter-compatible current
endpoint at or below their frozen ceilings. The exact six-model roster is therefore still
endpoint-executable under the binding owner rule, while the live validator implements a
stricter, contradictory aggregate-row rule.

## Smallest recommended FIX

- Add one regression: an above-ceiling aggregate model row plus a current eligible endpoint
  within the frozen ceiling must pass.
- Make the live public fetch include endpoint rows for all six exact slugs.
- For each model, require at least one current endpoint that supports the frozen parameters,
  satisfies the registered data-policy rule, and is at or below both frozen price ceilings.
- Preserve fail-closed behavior when the exact slug is absent, endpoint metadata is missing,
  endpoint capability is insufficient, or no eligible endpoint remains within the ceiling.
- Preserve the frozen `max_price`, `require_parameters=true`, and
  `data_collection="deny"` request payload unchanged.
- Re-review only this named contract. Do not reopen roster, prices, prompt, cap, retry,
  judging, or general live-seam design.

## Calls, cost, and stop state

- Public OpenRouter metadata GETs: **8** — one initial aggregate catalog validation GET,
  then one aggregate catalog + six endpoint GETs for exact evidence.
- OpenRouter auth/balance GETs: **0**.
- OpenRouter inference calls: **0**.
- New Codex-OAuth tasks: **0**.
- Session OpenRouter spend: **`$0.00`**.
- No output run directory was created.

The exact roster, frozen endpoint ceilings, `$8.57` proposed inner cap, cumulative `$10.00`
outer NTE, retry rules, one-run boundary, judge contract, and permanent label remain
unchanged. No top-up, substitution, fallback, perturbation, rerun, T4, ranking, release,
accepted-paper change, or publication claim occurred.
