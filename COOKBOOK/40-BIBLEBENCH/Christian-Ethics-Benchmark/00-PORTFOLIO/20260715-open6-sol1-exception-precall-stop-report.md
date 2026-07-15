# WALKWORTHY OPEN6-SOL1 — exceptional-canary pre-call stop

**Date:** 2026-07-15 (PDT)

**Scope:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`
only

**Claims boundary:** execution custody only; no benchmark result, ranking, gate
verdict, O5 verdict, scale-up, or public-release claim

## Outcome

The owner-authorized exceptional DeepSeek canary was **not sent**. Exact
same-roster/same-ceiling catalog revalidation passed, but the persisted-response
recovery layer interpreted the two historical HTTP-404 attempts under the old
two-attempt rule and raised the historical second-failure stop before control
reached the network delegate. This was an unregistered behavior under the
unattended execution order, so execution stopped without a workaround.

OpenRouter attempt custody remains exactly unchanged: **4 starts, 4 finishes,
1 replay, 2 valid executions, `$0.0320949696` booked, `$0` in flight**. There is
no attempt 5. No Qwen, Gemma, Llama, production-SUT, or production-Sol request
was initiated.

## Authorized exception and offline verification

Jimmy's exact authorization is recorded in
`20260715-jimmy-open6-sol1-deepseek-exception-authorization.md`, SHA-256
`b5ed535ad36a69309fee52e55f4e19a09510c42cf18ef7802f5988cb0be8317f`.

The bounded implementation preserves the original global call, replay-reserve,
concurrency, denominator, payload, roster, price-ceiling, and `$25.00` limits.
It permits a third history entry only for
`or:deepseek/deepseek-v4-pro:WW-01-A01:content:001`, binds the two prior 404s and
their payload hash, and rejects a fourth request. The focused runtime,
orchestrator, and live-driver regression passed **96/96** before catalog access.
Implementation checkpoint: commit `f50d5afbc`.

## Catalog revalidation

The append-only revalidation completed at `2026-07-15T12:46:02Z`:

- logical key: `catalog-revalidation:000001`;
- record SHA-256:
  `c649d72793b6bdd7e1cfe57ef81866a006d02217574ab9787660511575c621c3`;
- catalog-revalidation file SHA-256:
  `59b302d5c9ee2d0d487b3ba31b180511f2ec370578a9056c50142f0487e5ecbd`;
- exact DeepSeek model: `deepseek/deepseek-v4-pro`;
- eligible exact provider: `DeepSeek`;
- observed price: `$0.435/M` input and `$0.87/M` output;
- frozen ceiling: `$0.4785/M` input and `$0.957/M` output.

The materialized exception marker is
`runs/20260714-open6-sol1/deepseek-exception-authorization.json`, SHA-256
`3eafa0cffe461236ac30accc696f661151300745981369b825cf1f7ad0d655dd`.
It binds prior attempt IDs 3 and 4, both status 404, payload SHA-256
`cffdbd3ef829d72761b3a6f7fb017fd30bed52ef4e5febf82e8d54a9d22e3035`,
and maximum additional attempts 1.

## Exact stop

The serial canary invocation was chosen so no later model could start before a
valid exceptional DeepSeek result. Before invoking the delegate, however,
`CachedSutClient._recover_attempt()` called the historical
`_raise_recovered_second_failure()` path. The resulting stop was persisted in
`checkpoints.jsonl` as `resumable-stop:000003`, record SHA-256
`728218f983bca7dff2ddd97327ea3158dc92eb86d5df0026a5a946ecd62434de`,
with reason `unregistered OpenRouter HTTP stop: 404`.

Because the network delegate was never reached, the exceptional authorization
was not financially consumed. It is nevertheless not automatically reusable:
the owner's order requires any unregistered behavior to stop and be documented
once, without an improvised workaround.

## State at stop

- PUBLIC denominator: 2,064 item-model records, unchanged.
- Complete: 2; missing: 2,062; terminal-unresolved records: 0.
- OpenRouter: 4 attempts; 1 replay; `$0.0320949696` booked; `$0` in flight.
- Sol: 2 already-valid non-evidence canary turns; 0 production turns.
- Canary gate artifact: absent.
- Full production: not entered.
- Descriptive supplement/PDF: not produced.
- HOLDOUT: never loaded.
- Substitution, extra request, prompt/key/denominator change: none.

## Disposition

OPEN6-SOL1 remains stopped. Do not rerun the canary or patch the recovery path
under the current authority. PR-30 records two owner choices; the recommended
paper-first disposition is to close OPEN6 permanently and continue the existing
labels → G4 → verdict/status → manuscript/PDF critical path.
