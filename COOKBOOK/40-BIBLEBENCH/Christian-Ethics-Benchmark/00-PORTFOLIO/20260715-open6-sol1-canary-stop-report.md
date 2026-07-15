# WALKWORTHY OPEN6-SOL1 — live-canary stop report

**Date:** 2026-07-15 (PDT)

**Status:** STOPPED at the required six-SUT canary gate

**Claims class:** execution-custody report only; no benchmark result, ranking,
gate verdict, release determination, or public-release claim

## 1. Outcome

OPEN6-SOL1 passed every required offline gate and both non-evidence Sol OAuth
canaries, but it did not pass the registered six-model OpenRouter canary gate.
The exact `deepseek/deepseek-v4-pro` canary returned HTTP 404 on both its first
request and its single byte-identical replay. The live driver therefore stopped
before the remaining SUT canaries, full PUBLIC production, Sol routing, or Sol
judging.

No substitution, third attempt, concurrency increase, item/key/denominator
change, HOLDOUT access, automatic scale-up, O5 verdict, public release, or
workaround occurred.

## 2. Offline gates completed before live access

- Final serial OPEN6 regression: **127/127 passed** in 366.32 seconds.
- Independent P1 reviews: orchestrator, judge runner, and live driver all
  **APPROVED**, with no open P0/P1/P2 in the reviewed execution scope.
- Immutable manifest: 344 runnable PUBLIC items; SHA-256
  `4e21b2ecc9726fd92cbdb9c3b4efa44e2cf1fb37070e0dce714c35705dcff64c`.
- Catalog snapshot: all six exact slugs had at least one eligible provider under
  their registered ceiling; file SHA-256
  `7f11cde7939cbd8d5f0eee420a8bdb4046f5887f5cc84a2b28c52ab09fa61996`.
- Complete production-engine fake run: **2,064** item-model executions,
  **5,886** SUT calls, **1,722** classifier routes, **5,370** judge units,
  **10,008** category cells, and **227** valid judge batches; immutable resume
  passed; `$0`, no credential, and `holdout_loaded=false`.

## 3. Live canary custody

### Sol OAuth canaries

| Canary | Attempts | Result |
|---|---:|---|
| frozen classifier | 1 | PASS |
| frozen 24-unit judge batch | 1 | PASS |

Both used exact `gpt-5.6-sol` at the registered medium-reasoning OAuth route.
There was no replay and no production Sol turn.

### OpenRouter promoted SUT canaries

| Exact model | Attempts | Outcome | Booked custody |
|---|---:|---|---:|
| `minimax/minimax-m3` | 1 | PASS; exact returned model and reported cost | `$0.00233754` |
| `z-ai/glm-5.2` | 1 | PASS; exact returned model and reported cost | `$0.0028695576` |
| `deepseek/deepseek-v4-pro` | 2 | HTTP 404 twice; single replay exhausted | `$0.026887872` registered maximum |
| `qwen/qwen3.5-397b-a17b` | 0 | not initiated after stop | `$0` |
| `google/gemma-4-31b-it` | 0 | not initiated after stop | `$0` |
| `meta-llama/llama-4-maverick` | 0 | not initiated after stop | `$0` |

OpenRouter totals at stop: **4 attempts**, **1 replay**, **2 valid SUT calls / 2
valid item-model executions**, **$0.0320949696 booked exposure**, of which
**$0.026887872** is registered-max custody for missing reported cost on the two
404 responses; **$0 inflight**. The `$15` soft checkpoint was not reached and the
`$25` hard NTE was never approached.

## 4. Checkpoint and missing surface

The append-only checkpoint is
`runs/20260714-open6-sol1/unattended-stops.jsonl`, logical key
`stop:74ae25e67fddfaae9b0bf1be47fdefd6`.

- stop reason: `unregistered OpenRouter HTTP stop: 404`;
- complete item-model keys: **2**;
- missing item-model keys: **2,062**;
- permanent canary failure: exact DeepSeek first PUBLIC logical request after its
  one registered replay;
- full-judge plan: not entered;
- canary gate artifact: intentionally absent because all six SUT canaries did
  not pass;
- full PUBLIC production, Sol routing, and Sol judging: **not started**.

Read-only status command:

```bash
cd harness
../../../../../.venv/bin/python -m walkworthy.open6_sol1_live status \
  --benchmark-root .. \
  --manifest ../runs/20260714-open6-sol1/manifest.json \
  --run-dir ../runs/20260714-open6-sol1
```

The checkpoint also retains the mechanically generated resume command. Do not
run it under the current contract: the required DeepSeek canary exhausted its
one replay, so the six-SUT entry gate cannot become PASS without a new explicit
owner amendment. The existing authorization permits no third attempt,
substitution, provider workaround, or failed-canary waiver.

## 5. Claims conformance

- No per-model or per-design performance statistic was computed.
- No descriptive supplement or PDF was assembled from two promoted canaries.
- No model ranking, stability, reliability, G4, O5, gate, or release claim is
  licensed.
- The hash-frozen private MVP v0.1 manuscript and PDF remain byte-unchanged.
- Human labels remain the release-grade critical path independently of this
  stopped exploratory pilot.
