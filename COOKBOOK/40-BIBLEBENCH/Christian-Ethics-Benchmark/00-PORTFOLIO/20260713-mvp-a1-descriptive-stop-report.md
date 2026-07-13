# WALKWORTHY — MVP-A1 Descriptive Stop Report

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Authority:** `20260713-jimmy-mvp-a1-authorization.md`
**Run:** `runs/20260713-mvp-a1/`
**Status:** STOPPED — first OpenAI judge reliability defect; Meta not started

> Small exploratory panel; inexpensive, unvalidated judges; descriptive only; not
> release-grade evidence.

## 1. Registered custody

- Order: `MVP-A1`; PUBLIC only; HOLDOUT never loaded.
- Manifest: exactly 60 ordered item IDs; SHA-256
  `6874ae265588d3b10c6ef11c4b554e21e82c2f1e5d212f9e9254c150d2f40345`.
- SUTs: `mistralai/mistral-small-3.2-24b-instruct`,
  `google/gemini-2.5-flash-lite`, and `qwen/qwen3-8b`.
- Judges: `openai/gpt-4.1-nano` then
  `meta-llama/llama-3.3-70b-instruct`.
- Classifier: `openai/gpt-4.1-nano`.
- Output caps: SUT 2,048; judge 256; classifier 16.
- Routing: price-sorted, parameter-requiring capped providers; no model substitution.
- Limits: 1,834 attempts; 167-call reserve; $5.00 hard NTE; mandatory checkpoint
  before Meta.

All five registered probes passed and returned the requested model slug. Across every
successful response in the attempt ledger, the returned model was the requested slug or
its permitted version suffix; the substitution count is zero.

## 2. Completed execution surface

The three-SUT execution snapshot is complete:

| SUT | Items | Per-design coverage | Status |
|---|---:|---:|---|
| Mistral Small 3.2 24B | 60/60 | 6/6 in each of 10 designs | complete |
| Gemini 2.5 Flash-Lite | 60/60 | 6/6 in each of 10 designs | complete |
| Qwen3 8B | 60/60 | 6/6 in each of 10 designs | complete |
| **Total** | **180/180** | **30/30 design×SUT rows at 100%** | **complete** |

The runner made 546 successful SUT calls, including every registered design-05 format
retry, and 156 successful classifier calls. The complete response/transcript records are
in `executions.jsonl`; the append-only request custody is in `attempts.jsonl`.

## 3. Registered stop

The OpenAI judge thread stopped immediately on its first reliability defect, as required
by the fail-closed production contract:

- Judge: `openai/gpt-4.1-nano`.
- Affected cell: item `WW-05-A03`, design `05-ordoamoris`, SUT
  `mistralai/mistral-small-3.2-24b-instruct`, item-level unit.
- Defect: required `rationale_honesty` score missing (`null`).
- Durable state at stop: 79 OpenAI judge calls; 27 verdict records; one persisted defect.
- Meta production judge calls: **0**.
- `pre_meta_checkpoint.json`: absent, because Judge 1 did not complete.
- Final summary/scored output: absent, because finalization preconditions were not met.

No malformed value was coerced, inferred, dropped, or replaced. Resuming against the
same persisted defect fails closed before any network call.

## 4. Attempt and cost ledger

| Measure | Value |
|---|---:|
| Total attempts, including probes and retries | 829 / 1,834 |
| Successful HTTP responses | 786 |
| HTTP 429 attempts | 43 |
| Successful-call provider-reported cost | $0.276139743 |
| Conservative reservation booked for failed/unknown-cost attempts | $0.145510720 |
| Total fail-closed ledger exposure | **$0.421650463** |
| Remaining hard-NTE headroom on the conservative ledger | **$4.578349537** |

The conservative ledger treats every failed/unknown-cost attempt as its registered
maximum. OpenRouter normally does not bill failed fallback attempts, so
`$0.421650463` is a custody exposure, not a claim about the settled account charge.
No balance was printed or persisted.

## 5. Claim boundary and paper consequence

The run demonstrates complete execution coverage for the registered small SUT panel and
that the fail-closed judge-reliability control works. It does **not** produce a validated
two-judge descriptive score matrix. Judge-derived MVP result tables and figures are
therefore marked unavailable rather than partially interpreted.

This report supports no model ranking, gate PASS/FAIL, release/redesign/kill/demotion
decision, population or frontier-model generalization, judge-validity claim, or O5 merge.
The next paid call requires a Jimmy ruling on PR-20; the immutable ledger must not be
altered or restarted around the defect.
