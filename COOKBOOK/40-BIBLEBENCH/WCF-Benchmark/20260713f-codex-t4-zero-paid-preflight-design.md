# WCF-Bench T4 zero-paid preflight controller design

**Date:** 2026-07-13
**Owner:** Codex executor
**Authorization:** Jimmy, in chat: offline controller work plus the zero-paid R40.1
preflight only. OpenRouter auth/catalog metadata and official capability sources are in
scope. Paid inference calls are not authorized.

## Paper-facing outcome

This bounded task removes the last cost/roster uncertainty before the T4 empirical run.
It freezes the full binding R59.2 roster and a five-cheapest-model first execution shard,
then returns exact forecast arithmetic for Jimmy to ratify. It does not produce benchmark
evidence, change the panel, or start T4.

## Scope and stop condition

Build the smallest reproducible preflight-only controller:

- one CLI: `04-HARNESS/t4_preflight.py`;
- one focused test module: `04-HARNESS/tests/test_t4_preflight.py`;
- one new immutable dated artifact directory under `07-PILOTS/`;
- metadata GETs only: OpenRouter `/api/v1/auth/key` and `/api/v1/models`, plus public
  official capability-source retrievals;
- no `OpenRouterModelClient`, no completion request, no POST, and no paid inference.

Stop once the controller has frozen the required artifacts, the offline suite is green,
and an independent specification review plus one independent quality review find no
blocking defect. No live-run controller, G1–G7 report computation, refactor, or optional
polish belongs in this task.

## Binding inputs

The controller implements R59.1–R60.3 without reinterpretation:

- 226 runnable base items; four `dev_set_only` items excluded;
- five formula families: openai, deepseek, qwen/alibaba, moonshotai, meta-llama;
- fallback order: z-ai, nvidia, microsoft;
- exact continuity and mid-tier pins from R59.2;
- anti-leak exclusion of google, x-ai, and anthropic SUTs;
- target roster 10, proceed at 8–10 with disclosure, stop below 8;
- current official LMArena text-overall `rating` is the authorized successor ordering
  field for the memo's historical “text Elo” wording, with the terminology transition
  disclosed in every roster artifact;
- capability values must come from exact official benchmark or exact provider source
  pages. Ambiguous aliases are missing, never borrowed across variants;
- GPQA Diamond is missing when no exact provider-published result exists;
- master seed 1647 and deterministic design-stratified G5c sampling use largest-remainder
  allocation over slug-sorted strata, then seeded sampling;
- R59.5 planning ceiling remains $300; no current paid cap is inferred.

## Controller architecture

Network retrieval is a thin injectable boundary. All roster, PCA, sampling, count, cost,
runtime, branch, and serialization work is pure and hermetically testable.

Core interfaces:

```text
resolve_roster(catalog, arena_rows, alias_rows) -> roster resolution + trace
normalize_capabilities(roster, source_rows) -> frozen capability rows
compute_pc1(capability_rows) -> included rows + PC1 + frontier
select_g5c_samples(items, seeds=1647/1648) -> 23 priming + 100 evaluation
build_call_plan(items, roster, frontier, g5c_plan) -> exact request classes
estimate_cost(call_plan, catalog, token_profile) -> per-class and total forecast
forecast_runtime(call_plan, historical_throughput) -> runtime forecast
forecast_branches(cost_plan, approved_budget=None) -> R59.5 ladder table
write_new_artifacts(output_dir, payloads) -> exclusive immutable writes
```

Any metadata mode must be structurally unable to call a completion endpoint. The default
CLI is a dry plan that neither opens a socket nor writes files. The explicit metadata
preflight flag performs only the authorized GETs and writes only into a new dated path.

## Frozen artifacts

The new preflight directory contains:

1. `capability-battery.csv` — one row per roster model, four component values, exact
   source URLs, retrieval timestamps, source revisions/hashes, exact-name mapping notes,
   missingness, inclusion status, PC1, and provenance canary.
2. `openrouter-catalog-snapshot.json` — only relevant candidate, pin, fallback, and judge
   entries; model id, architecture/modality, preview status, context, pricing, retrieval
   timestamp, source hash, and provenance canary. No credential.
3. `t4-run-manifest.json` — roster formula trace, pins/fallback/dedup decisions, complete
   roster, PC1 frontier, five-cheapest base shard, capability/catalog/bank/judge-manifest
   hashes, item and variant scope, G5c sample IDs, max-token caps, retry policy, exact
   logical-call schedule, cost assumptions, master seed, branch table, and provenance
   canary.
4. `t4-cost-plan.csv` — request classes with model, role, phase, count, token estimate,
   catalog prices, and subtotal.
5. `t4-preflight-report.md` — sanitized R40.1 balance fields, exact roster, current prices,
   phase-one and full forecasts, runtime, required caps/top-up, and truncation conflicts.

Every file is created exclusively. A rerun requires a new dated directory; an existing
artifact is never rewritten.

## Call-count contract

The current frozen bank and scorer imply these exact pre-G5c logical calls:

| Scope | SUT calls | Judge calls | Total |
|---|---:|---:|---:|
| Base, 226 × 10 | 2,260 | 6,960 | 9,220 |
| P3/P4/P6 variants after dev exclusion | 1,480 | 4,510 | 5,990 |
| G5b nearest-neighbor transplant | 0 | 620 | 620 |
| Subtotal before G5c | 3,740 | 12,090 | 15,830 |

G5c adds exactly 200 SUT calls plus the normal judge-call schedule for the frozen
100-item evaluation sample under both unprimed and primed conditions. The final total is
written only after that sample is frozen.

The five-cheapest-model first shard is an execution-order checkpoint inside the same T4
manifest, not a smaller roster or a separate benchmark. It contains all 226 base cells
and their associated judge calls for the five roster models with the lowest forecasted
per-base-cell cost; ties sort by slug. It emits no interim gate result and grants no paid
authority.

## Cost and cap contract

The forecast is an exact deterministic calculation, not a promise of the eventual bill:

- current catalog prompt/completion prices are mandatory and fail loud if absent;
- request counts come from the frozen call schedule;
- prompt/completion token profiles are frozen from immutable WCF per-request evidence,
  grouped by role/request class, using the 95th percentile with nearest-rank selection;
- when a class lacks historical evidence, the controller uses its rendered prompt-byte
  token ceiling plus the client's fixed completion cap and labels that row `ceiling`;
- every subtotal is `count × (prompt_tokens × prompt_price + completion_tokens ×
  completion_price)`;
- response-attributed actuals and key-side reconciliation remain the live-run accounting
  method later; they are not fabricated during preflight.

For any forecast `F`, the minimum ratifiable cap that does not trigger the R59.5 80%
ladder is `ceil_to_cent(F / 0.80)`. Required top-up is
`max(0, required_cap - current_limit_remaining)`. Report both the phase-one and full-run
values, while preserving Jimmy's separate power to choose a lower paid cap and thereby
activate a registered truncation branch.

## Runtime contract

Use the immutable T3 emission timestamps as the measured baseline: 264 logical calls from
2026-07-13 07:17:44 through 07:58:26, or 6.486486 logical calls/minute. Report exact
baseline-throughput runtime for phase one and the full schedule, plus a labeled planning
band at 0.75×–1.25× that throughput. This is a forecast, not a service-level guarantee.

## Registered conflicts and non-decisions

- The perturbation module rejects EPISODE items although the bank labels 20 P3, 8 P4,
  and 16 P6 EPISODE variants. Count them in the registered forecast but flag live
  materialization as unresolved; do not invent a prompt path.
- The final truncation rung says to halve the EPISODE roster while also saying base cells
  are never dropped. Report the prescribed 330-call saving, but do not apply the rung
  without a Jimmy ruling.
- A missing or ambiguous Arena/OpenRouter identity stops that formula slot; it never
  silently selects a merely similar model.
- The preflight reports every branch because no paid budget has yet been approved. It
  does not select a branch of record.

## Acceptance criteria

- Full formula roster and five-cheapest base shard are mechanically traceable.
- Capability CSV and run manifest are immutable, source-complete, and secret-free.
- Exact logical calls, phase-one/full forecasts, runtimes, required caps, balance/top-up,
  and every truncation branch are present.
- Only authorized GET surfaces are reachable in metadata mode.
- No paid inference call occurs.
- Focused tests and the full offline suite pass.
