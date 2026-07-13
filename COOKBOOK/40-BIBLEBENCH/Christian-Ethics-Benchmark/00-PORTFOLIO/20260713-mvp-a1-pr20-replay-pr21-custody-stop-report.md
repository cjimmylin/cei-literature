# WALKWORTHY — MVP-A1 PR-20 Replay / PR-21 Custody Stop Report

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Run:** `runs/20260713-mvp-a1/`
**Status:** STOPPED — attempt 915 is HTTP 200 without persisted `usage.cost`

> Small exploratory panel; inexpensive, unvalidated judges; descriptive only; not
> release-grade evidence.

## Paper-facing progress

PR-20 is ratified and mechanically discharged for the original judge defect. The
`WW-05-A03` / Mistral / OpenAI item-unit response was replayed once with the exact same
model, prompt construction, 256-token cap, and provider ceiling. The replay is recorded in
the new append-only `verdicts-replays.jsonl`; it has zero defects. The original defective
record remains unchanged in `verdicts.jsonl`.

OpenAI judging advanced from 27 to 63 base verdict records and from 79 to 163 logical
scoring units. The run still has no complete Judge-1 surface, pre-Meta checkpoint, Meta
production call, summary, or scored output. No judge-derived MVP result is interpretable.

## New custody stop

Attempt 915 targeted the next exact missing key:

- item: `WW-01-A05`;
- SUT: `google/gemini-2.5-flash-lite`;
- judge: `openai/gpt-4.1-nano`;
- role/unit: judge / item;
- registered maximum: $0.0025024.

OpenRouter returned HTTP 200, but the response lacked `usage.cost`. The runner stopped
inside the attempt ledger before accepting the response or writing a verdict. The raw
response is not persisted and cannot be reconstructed, priced, or scored. Attempt 915 has
a durable `attempt_started` event and no `attempt_finished` event.

| Custody measure | Value |
|---|---:|
| Starts | 915 |
| Finishes | 914 |
| Finished-ledger exposure | $0.432642163 |
| Attempt-915 unresolved maximum reservation | $0.0025024 |
| Total conservative exposure | **$0.435144563** |
| OpenAI base verdict records / logical units | 63 / 163 |
| Successful PR-20 replays / replay units | 1 / 1 |
| Meta production attempts | 0 |

No model substitution, missing-cost inference, response reuse, score inference, HOLDOUT
access, or O5 mutation occurred.

## Disposition

PR-21 records the unregistered choice. Recommended option 1 books attempt 915 at its
registered maximum under a distinct missing-cost custody basis, keeps its response unusable,
and permits one identical-payload retry from the existing reserve. A repeated missing-cost
response for that payload stops permanently. Until Jimmy rules, no ledger completion or
paid resume is authorized.
