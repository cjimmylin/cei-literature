# WALKWORTHY — PR-25 O5 G7 Paid-Run Order Decision

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Prepared by:** Codex
**Status:** OWNER RULING REQUIRED; NO CREDENTIAL OR LIVE CALL AUTHORIZED
**Scope:** O5 W5/G7 production execution custody and spend only

## Decision required

PR-18, PR-23, and PR-24 fix the G7 measurement surface but do not authorize paid calls,
provider routing, token caps, retry behavior, attempt reserves, or a spend ceiling. The
exact evidence and calculations are in `20260713j-g7-paid-run-preflight.md`.

### Recommended option 1 — bounded production order

Authorize the fixed six-SUT/frozen-judge/classifier/Mistral-author roster on the exact
manifest hashes, with price-sorted capped same-model provider routes, role-specific
output caps, a 9,709-logical-call plan, 971 exact-replay reserve, concurrency 2, exact
returned-model and `usage.cost` custody, checkpointing, and a $30 hard NTE. Disable
hidden client retries so every POST is ledgered; allow one exact replay per failed,
empty, malformed, or missing-cost key and stop that thread on a second failure. Use the
first retained production request per slug as its canary; make no separate premium
probe. This is the recommended bounded route to G7 evidence.

### Option 2 — remain no-call

Do not authorize G7 execution. Preserve the completed mechanics and manifests, keep G7
PENDING, and continue only the independent human-label → G4 → paper-conversion lane.

## Exact requested ruling

> Ratify PR-25 option 1: authorize WALKWORTHY O5 G7 order G7-A1 on the exact six-SUT,
> frozen `openai/gpt-4.1-mini` + `google/gemini-2.5-flash` judge, explicit
> `openai/gpt-5.6-terra` classifier, and `mistralai/mistral-large-2512`
> paraphrase-author/tie-breaker roster; bind production manifest SHA-256
> `616d2e93491adcb8da9fc00664693cd8c4685a95fc36b6fc09816c32414edf0e` and role-manifest
> SHA-256 `013600bd2f1c34b7353319e98395aa8b1b5b921796d73a840e5ddc2138027480`;
> use price-sorted, parameter-compatible same-model providers capped at the
> 2026-07-13 preflight rates; output caps SUT/author/judge/tie/classifier =
> 32768/4096/256/256/16; maximum 9,709 planned logical calls plus 971 exact-payload
> replay attempts, 10,680 client POSTs total, concurrency at most 2; disable hidden
> retries and ledger every attempt; allow one byte-identical same-model/cap/price-ceiling
> replay per failed, empty, malformed, or missing-cost key, booking the registered
> role/model maximum when cost is missing, and stop that thread on a second failure;
> require exact returned model plus `usage.cost`; checkpoint after authoring + battery 1,
> before $20, and before tie-breakers; enforce a $30.00 hard NTE before every request;
> use each slug's first retained production request as its canary, with no separate
> premium-model probe; no substitution, denominator change, item replacement, HOLDOUT,
> automatic scale-up, or G7/paper verdict before the frozen P1/Part-B path is complete.

Until the one-liner is ratified verbatim, PR-25 is a hard stop for credential access,
retry-mechanics changes, and every live G7 request.
