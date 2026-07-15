# WCF-Bench Pilot 2 — Session-59 Quality Stop

**Date:** 2026-07-15
**Status:** OWNER EXACT QUALITY FIX / DEFER REQUIRED · PUBLIC PREFLIGHT NOT RUN

> **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Gate outcome

Jimmy authorized the exact seven-residual FIX. TDD reproduced all seven, then reached
8/8 targeted, 41/41 combined Pilot-2, and 867/867 full offline tests green. The same
named specification reviewer passed all seven residuals. The required fresh quality review
then returned **FAIL** with four new reproduced P1s. No public preflight ran.

## Confirmed quality P1s

1. **Interrupted provider canary can reissue and undercount spend.** Resume reconstructs
   reservations and settlements with last-write-wins dictionaries and recognizes canary
   completion only after a PASS marker. An interruption after persisted response and
   settlement but before validation reissues the same request ID. Reproduction produced
   two reservations and two settlements; `$0.006` persisted settlement sum reconstructed
   as `$0.005` on the next resume.
2. **Terminal shard failure does not cancel peers.** A terminal `CustodyStop` in one shard
   leaves the other threads issuing work. Reproduction attempted 687 additional cells
   after the terminal failure.
3. **Ambiguous post-submit transport failure is asserted to cost zero and retried.** The
   canary and cell paths persist and settle `$0.00` after a timeout/URL failure even though
   provider charging is unknowable. Reproduction made three retries, produced a missing
   checkpoint, recorded `$0.00`, and emitted no terminal marker.
4. **Full-run OAuth judging lacks authorization and canary gates.** The judge driver can
   construct the live adapter and invoke batches without loading an amount-authorized
   manifest or requiring the registered OAuth-canary PASS. Reproduction invoked three
   injected batches with an explicitly unauthorized manifest present.

Positive quality findings: public preflight is credential-free; lower refreshed prices
flow into requests; SUT prompts remain blind; only final answers enter judge records; the
OAuth environment allowlist excludes the OpenRouter key.

## Why work stopped

The Session-59 residual FIX authority covered only the prior seven cross-seam regressions.
These four quality P1s are new. Binding paper-first rules require a new owner ruling before
another correction cycle. Quality FAIL blocks the public preflight.

## Requested owner ruling

- **FIX (recommended):** authorize one exact quality correction cycle with regressions for
  canary interrupted-response recovery and additive settlement accounting; shared shard
  cancellation before further transport; fail-closed ambiguous post-submit transport
  cost; and manifest plus OAuth-canary authorization before judge invocation. Re-review
  only these four P1s. No general audit or new adapter.
- **DEFER:** preserve this offline checkpoint and stop Pilot 2 before public preflight.

Under FIX, the public-catalog-only zero-paid preflight may run only after the same fresh
quality reviewer passes these four P1s. Neither choice authorizes credential/balance
access, OAuth tasks, OpenRouter inference, paid calls, top-up, or a cap.

## Calls and spend

- Public metadata calls: zero.
- Auth or balance calls: zero.
- Codex-OAuth judge tasks: zero.
- OpenRouter inference calls: zero.
- Spend: `$0.00`.
