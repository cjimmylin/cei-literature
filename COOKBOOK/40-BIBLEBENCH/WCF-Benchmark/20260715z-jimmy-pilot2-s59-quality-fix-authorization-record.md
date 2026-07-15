# Jimmy authorization record — Pilot 2 Session-59 quality FIX

**Date:** 2026-07-15
**Owner ruling:** `QUALITY FIX`

Jimmy selected the exact `QUALITY FIX` offered at the Session-59 stop. This authorizes one
bounded correction cycle for only the four P1s reproduced in
`20260715x-wcf-pilot2-s59-quality-stop.md`:

1. recover an interrupted provider-canary response and settlement without transport
   reissue, while reconstructing exact additive settlement cost;
2. cancel peer model shards after a terminal shard failure before any further transport
   begins;
3. fail closed on ambiguous post-submit transport failure or timeout rather than asserting
   zero cost and retrying as if no request may have executed; and
4. require manifest paid authorization and a persisted registered OAuth-canary PASS before
   any full-run OAuth judge invocation.

The correction must use failing regressions first and the minimum implementation needed to
make them pass. The same quality reviewer must re-inspect only these four blockers. Any new
P1 stops and returns to Jimmy; P2/P3 findings are disclosed and deferred.

If and only if that named quality re-review passes, the previously authorized sequence may
continue through one public-catalog-only, zero-paid Pilot-2 preflight. That preflight may
return the exact roster, provider pins, prices, call counts, runtime, required balance, and
reservation-safe proposed cap for Jimmy's separate amount-specific authorization.

This ruling does **not** authorize credential access, a private balance check, an OAuth
task, an OpenRouter inference call, a top-up, empirical execution, judging, a rerun, a
substitution, a protocol change, or any spend. It changes no roster, reasoning setting,
prompt, scorer, decision geometry, accepted PPP-1 packet, Pilot-1 evidence, bank item, or
quotability label.

Pilot-2 empirical execution remains **0%** until a later amount-specific paid ruling and
all registered live gates pass.
