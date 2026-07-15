# WCF-Bench Open-First MVP — Owner Decision Packet

**Date:** 2026-07-14 (America/Los_Angeles)  
**Status:** PROVISIONAL · RESERVED FOR JIMMY · NO R-NUMBER ASSIGNED  
**Empirical status:** NO RUN · NO OAUTH CANARY · NO PAID INFERENCE

> **EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Outcome

The authorized public-only preflight completed and failed closed. It made seven public
metadata GETs, accessed no credential or auth endpoint, invoked no Codex judge, made no
inference request, and spent `$0`. No executable manifest exists.

The exact six model slugs remain present in the public catalog. Their refreshed catalog
rows and prices are:

| Family | Exact slug | Canonical slug | Input / output per 1M |
|---|---|---|---:|
| MiniMax | `minimax/minimax-m3` | `minimax/minimax-m3-20260531` | `$0.30 / $1.20` |
| GLM | `z-ai/glm-5.2` | `z-ai/glm-5.2-20260616` | `$0.896 / $2.816` |
| DeepSeek | `deepseek/deepseek-v4-pro` | `deepseek/deepseek-v4-pro-20260423` | `$0.435 / $0.87` |
| Qwen | `qwen/qwen3.7-max` | `qwen/qwen3.7-max-20260520` | `$1.25 / $3.75` |
| Google | `google/gemma-4-31b-it` | `google/gemma-4-31b-it-20260402` | `$0.12 / $0.35` |
| Meta | `meta-llama/llama-4-maverick` | `meta-llama/llama-4-maverick-17b-128e-instruct` | `$0.20 / $0.80` |

Snapshot SHA-256:
`64f7409fb47ee5631e7ef1f86888e8565196aec51dec03dce937cd4c7295e199`.

## Exact cost and call forecast

The conservative SUT price ceiling uses 2,221 prompt units and 2,048 completion tokens
for every response. It is a ceiling, not expected spend.

| SUT | 230 first attempts | 252-attempt envelope |
|---|---:|---:|
| MiniMax M3 | `$0.718497000` | `$0.787222800` |
| GLM 5.2 | `$1.784152320` | `$1.954810368` |
| DeepSeek V4 Pro | `$0.632015850` | `$0.692469540` |
| Qwen3.7 Max | `$2.404937500` | `$2.634975000` |
| Gemma 4 31B | `$0.226163600` | `$0.247796640` |
| Llama 4 Maverick | `$0.478998000` | `$0.524815200` |
| **Total** | **`$6.244764270`** | **`$6.842089548`** |

- Proposed 80%-utilization cap, rounded up to cents: **`$8.56`**.
- Likely actual OpenRouter spend remains approximately **`$2–$4`**.
- OpenRouter first attempts: **1,380**; bounded SUT-attempt envelope: **1,512**.
- Judge geometry: **2,088** logical decisions in **264** initial OAuth tasks; the
  absolute all-records-fail twice envelope is **792** task attempts.
- OpenRouter balance and top-up: **unknown and not checked**, because credential access
  was not authorized.
- OAuth incremental API bill: `$0` only if the saved ChatGPT allowance is available.
  Current allowance/quota state was not accessed.
- Remaining active runtime after all gates pass: provisionally **7–19 hours**
  (2–5 generation, 3–10 sequential judging, 2–4 analysis); calendar time can be longer
  if OAuth limits reset. The canary must replace this with a measured forecast.

## Why the preflight is non-executable

1. MiniMax, GLM, DeepSeek, Qwen, and Gemma expose a reasoning capability but do not
   explicitly advertise effort `none`. GLM and DeepSeek advertise only `high/xhigh`.
   The exact frozen `reasoning.effort="none"` contract therefore cannot be proven.
2. None of the 72 public endpoint rows for the six models contains a
   `data_collection` field. OpenRouter can enforce `data_collection="deny"` in the
   request, but the frozen design additionally required public endpoint proof.
3. The batched judge prompt contains a not-yet-generated SUT response. The current
   preflight correctly refuses to call that prompt measured before response evidence
   exists; an executable preflight needs an owner-approved conservative offline ceiling.

The immutable failure report lists the reasoning blocker first for five models and the
endpoint blocker for Llama because validation stops at each model's first failure. The
endpoint snapshots establish that the missing data-policy field applies to all six.

## New quality-review P1s after the permitted fix cycle

The specification review named four blockers. One bounded implementation fix cycle
closed all four, and the same reviewer returned PASS on only those blockers. The fresh
quality review then found three new P1s:

1. The proposed Codex subprocess inherits the parent environment except for two named
   variables, so unrelated secrets such as an OpenRouter key could reach the subprocess
   before post-hoc tool-event rejection.
2. A terminal stop in one of the three SUT shards does not cancel the other two; an
   offline barrier probe observed 40 additional cells after the first simulated stop.
3. The budget controller separates authorization from accounting without a lock or
   reservation. Three concurrent calls can all authorize against the same remaining
   balance and exceed the cap before the overrun is detected.

The binding second-cycle rule requires Jimmy to choose **fix, disclose-and-run, narrow,
or defer**. Codex may not begin another implementation cycle by itself.

## Recommended bounded ruling

**FIX** is the only recommended path. `Disclose-and-run` is incompatible with secret
containment, immediate-stop semantics, and the strict cap. A narrow one-shard run still
needs environment containment and atomic accounting, so it does not eliminate the
required fixes.

Suggested exact approval text:

> I authorize one bounded Open-First MVP second-cycle FIX only. Preserve the exact six
> SUTs, 230/226/4 split, 2,048-token SUT ceiling, one-run boundary, no substitutions,
> and exact exploratory/non-quotable label. Amend reasoning suppression to
> `reasoning.enabled=false` only for catalog rows with `mandatory=false`; accept
> request-enforced `data_collection="deny"` plus `require_parameters=true` as the
> data-policy gate; and derive conservative pre-response judge prompt ceilings offline.
> Fix only the three named P1s: allowlisted OAuth subprocess environment, immediate
> cross-shard terminal cancellation, and atomic budget reservation/accounting. Re-review
> only those named changes and refresh the public preflight. If they pass, Codex may
> access OpenRouter auth/balance metadata and run only the registered 16-record
> zero-dollar OAuth canary. No paid OpenRouter inference, top-up, model substitution,
> empirical run, rerun, T4, or manuscript replacement is authorized. Return the canary,
> measured quota/time forecast, balance/top-up state, and exact amount-specific paid
> authorization request.

Jimmy may instead state `DEFER` to leave the pilot non-executable and preserve the
accepted exploratory MVP as the stopping point.

## Evidence

- `07-PILOTS/20260714-open-first-mvp-zero-paid-preflight/`
- `20260714l-wcf-open-first-mvp-pilot-design.md`
- `20260714m-wcf-open-first-mvp-offline-implementation-plan.md`
- Focused tests: 49 passed.
- Full offline suite: 782 passed in 114.96 seconds; only non-failing pytest temporary
  cleanup warnings.

