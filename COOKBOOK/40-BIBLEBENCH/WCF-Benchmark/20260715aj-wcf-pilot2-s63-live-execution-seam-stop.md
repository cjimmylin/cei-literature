# WCF-Bench Pilot 2 Session-63 live-execution seam stop

**Date:** 2026-07-15

**Permanent label:** **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Outcome

Jimmy authorized `PROCEED` under the strict cumulative `$28.13` OpenRouter NTE and the
registered gated sequence. Before credential access, a read-only command-path review found
three new execution-integration P1s. The registered automatic stop therefore fired before
private balance access, OAuth, provider calls, bank inference, run-directory creation, or
spend.

## Reproduced blockers

### P1-A — no append-only authorization binder

The immutable v3 manifest SHA256 is
`b5227988f67a5eca563e7f76b78e36613e8665d433fda9c37fb1efa048a05870`. Its
`authorization_gate` correctly remains:

- `credential_access=false`
- `oauth_canary=false`
- `paid_inference=false`

`pilot2_live.py` rejects this manifest before transport. No reviewed production command
binds Jimmy's dated `$28.13` authorization record and exact v3 hash into a new append-only
authorized manifest. V3 itself must remain immutable.

### P1-B — registered live gates are not separately invocable

The sole `pilot2_live.py` CLI runs provider canaries, five first bank cells, and the entire
three-shard remainder in one invocation. It has no phase selector or supported pause after
either registered gate. `--resume` is interruption recovery, not a gate transition.
Deliberate interruption is not an acceptable substitute.

### P1-C — no live judge/scoring/analysis driver entry point

`pilot2_analysis.py` exposes tested library functions but no CLI/main. `pilot2_judge.py`
explicitly invokes no task. `pilot2_report.py` can render only after receiving an analysis
JSON, but no reviewed command creates that JSON from the immutable response and judge
evidence. An ad hoc inline Python driver would bypass the reviewed live seam.

## Smallest bounded FIX

One exact TDD implementation cycle may add only:

1. an append-only authorization binder requiring the exact v3 manifest hash, Jimmy's
   `20260715ai` authorization record, exact `$28.13` cap, and explicit false→true gate
   transitions without editing v3;
2. fail-closed phase commands for provider canaries, five first cells, and remaining run,
   all sharing one immutable run directory and permitting the next phase only from persisted
   PASS evidence; and
3. a judge/scoring/analysis driver requiring the immutable run, the exact PASS OAuth canary,
   and the authorized manifest, producing append-only verdict/missing/analysis artifacts for
   the existing report renderer.

The fix may not change roster, providers, prices, cap, reasoning, prompts, scorers,
geometry, retries, concurrency, custody semantics, output labels, or report claims. Use one
fresh implementation agent, one specification review, and one quality review. No credential,
OAuth, inference, or spend may occur until both reviews pass. If they pass, Jimmy's existing
`$28.13` execution authority resumes at the private-balance gate; it does not expand.

## Owner gate

Jimmy chooses exact **LIVE SEAM FIX** or **DEFER**. Any broader or newly surfaced P1 returns
to Jimmy. P2/P3 findings are disclosed and deferred under the paper-first rule.

Session calls/spend: zero / `$0.00`. Empirical execution remains 0%.
