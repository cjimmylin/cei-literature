# WCF-Bench Open-First MVP — Session-55 First-Response Gate Stop

**Date:** 2026-07-15
**Status:** AUTOMATIC STOP · IMMUTABLE PARTIAL EVIDENCE · OWNER DECISION REQUIRED

> **EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Exact stop

The corrected public runtime endpoint gate passed for all six exact model slugs, and the
fresh sanitized balance check showed `$285.317507401` remaining against the frozen `$8.57`
inner cap. The one immutable execution then started three concurrent first cells.

The MiniMax first response reported **2,385 reasoning tokens** despite the frozen
`reasoning.enabled=false` request parameter. The registered first-response guard raised:

`TerminalStop: first cell reported reasoning tokens`

The process exited with code 2. No later cell, retry, judge task, analysis, or supplement
was started.

## Immutable evidence and spend

The run directory is:

`07-PILOTS/20260715-open-first-mvp-live/`

It contains the copied frozen manifest, run identity, eight raw-evidence rows, and one
checkpoint row. Three first-cell requests were issued concurrently:

| SUT | Persisted outcome | Response-attributed cost | Gate state |
|---|---|---:|---|
| `minimax/minimax-m3` | response, length-finished, 2,385 reasoning tokens | `$0.00254634000` | terminal reasoning-leak stop |
| `z-ai/glm-5.2` | response, first-response validation PASS | `$0.00377913307` | persisted checkpoint |
| `deepseek/deepseek-v4-pro` | OpenRouter error code 404; no usage/cost metadata | not reported | no retry after cancellation |

Total response-attributed spend is **`$0.00632547307`**. An immediate sanitized post-stop
auth check reported the same account usage value as the pre-run check; because the account
is shared and the auth figure may lag, the immutable response-attributed ledger is the
controlling run spend record. No top-up occurred.

## Why execution cannot continue under existing authority

Reasoning-token leakage is an explicit automatic stop in Jimmy's overnight authority. The
exact roster, frozen parameter contract, one immutable execution boundary, and prohibition
on substitutions, fallbacks, protocol changes, and reruns leave no authorized continuation.
The error-only DeepSeek first response is retained as missing/error evidence and was not
investigated beyond its persisted status.

## Owner decision

Choose one:

- **DEFER:** close the Open-First adjunct at this immutable failed gate; retain the accepted
  exploratory MVP and paper unchanged.
- **NEW STUDY:** separately authorize and freeze a changed roster or reasoning contract and
  a new execution. This is a protocol change and a new study, not a resume or rerun of the
  immutable Session-55 execution.

**Suggested default: DEFER.** The accepted exploratory MVP and paper are already complete;
changing the roster or reasoning contract now would reopen infrastructure without rescuing
the registered exact-protocol pilot.

No T4, ranking, release, publication, accepted-manuscript, or quotation authority follows
from this partial run.
