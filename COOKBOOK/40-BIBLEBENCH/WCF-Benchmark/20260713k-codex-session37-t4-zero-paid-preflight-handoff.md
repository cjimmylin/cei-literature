# WCF-Bench Codex session 37 handoff — T4 zero-paid preflight

**Date:** 2026-07-13
**Scope:** offline T4 controller plus the authorized zero-paid R40.1 auth/catalog preflight
**Paid inference:** not authorized, not attempted, `$0` spent
**Paper-first allocation:** empirical 0% · paper 0% · infrastructure 70% · governance/admin 30%

## Paper-facing state

PPP-1 remains the immediate owner-ratified paper milestone. This session did not replace,
amend, start, or satisfy PPP-1 or registered T4. It removed the roster, price, cost, and
runtime uncertainty for the later confirmatory T4 and stopped before any inference call.

## Completed

- Added the metadata-only controller `04-HARNESS/t4_preflight.py` and 14 focused contract
  tests in `04-HARNESS/tests/test_t4_preflight.py`.
- Froze the official capability/source registry in
  `20260713h-t4-preflight-source-inputs.json`, including the eight higher-rated formula
  rows excluded for exact-identity/configuration or preview reasons.
- Passed one specification review and one quality review. The quality review's three
  named blockers were fixed in the final bounded cycle: complete roster-resolution
  evidence, per-request-class rendered-byte/fixed-2048 ceilings, and actual catalog-GET
  timestamps. Named-blocker re-review passed with no new blocker.
- Performed exactly the authorized metadata boundary: `GET /api/v1/auth/key` and
  `GET /api/v1/models`. The controller has no completion endpoint. The snapshot returned
  343 catalog models and `$63.01088785899992` limit remaining.
- Exclusively created the immutable five-file packet at
  `07-PILOTS/20260713-t4-zero-paid-preflight/`.
- Verified the focused suite at 14/14 and the full offline harness at 690/690.

## Frozen ratification terms

The R59.2 roster is:

1. `openai/gpt-5.5`
2. `deepseek/deepseek-v4-pro`
3. `qwen/qwen3.7-plus`
4. `moonshotai/kimi-k2.6`
5. `meta-llama/llama-4-maverick`
6. `deepseek/deepseek-chat`
7. `mistralai/mistral-large-2512`
8. `meta-llama/llama-3.1-8b-instruct`
9. `cohere/command-a`
10. `amazon/nova-pro-v1`

The five-cheapest base shard is `meta-llama/llama-3.1-8b-instruct`,
`meta-llama/llama-4-maverick`, `deepseek/deepseek-chat`,
`deepseek/deepseek-v4-pro`, and `qwen/qwen3.7-plus`.

| Scope | Logical calls | Forecast | Minimum 80%-safe cap | Top-up | Baseline runtime | Planning band |
|---|---:|---:|---:|---:|---:|---:|
| Five-cheapest base shard | 4,610 | $63.234201 | $79.05 | $16.04 | 11h 51m | 9h 29m–15h 48m |
| Full T4 | 16,698 | $278.788647 | $348.49 | $285.48 | 42h 54m | 34h 19m–57h 12m |

The full cap exceeds R59.5's `$300` planning ceiling. `drop_p6` also exceeds it at a
`$338.82` cap. The first cumulative within-ceiling branch is `drop_p6 + drop_p3`:
13,333 calls, `$220.024017` forecast, `$275.04` cap, `$212.03` top-up. No branch was
selected. The final EPISODE-halving branch still requires Jimmy's separate ruling because
it conflicts with the registered “base cells are never dropped” clause.

## Open owner decision

`PENDING-QUESTIONS.md` now asks Jimmy to choose, when T4 returns after PPP-1, between an
explicitly raised ceiling/full `$348.49` cap and the first registered within-`$300`
branch. This is a ratification question only; it grants no paid-call authority.

## Next session

On session open: load `project-dashboard.html` (Live-status first).

The immediate paper-first action remains the separately authorized PPP-1 zero-paid
preflight, followed by its own paid-run ratification. Do not infer that this T4 metadata
authorization or manifest applies to PPP-1. Do not run any T4 shard without a new written
scope, budget, cap, top-up, and paid-call authorization.

On session close: update the dashboard per `AGENTS.md §The project dashboard`, then
open/reload it in the browser and leave the verified next-session view open for Jimmy.
