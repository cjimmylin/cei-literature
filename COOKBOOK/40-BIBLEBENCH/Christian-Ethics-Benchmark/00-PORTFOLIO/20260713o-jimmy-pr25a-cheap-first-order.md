# WALKWORTHY — Jimmy PR-25(a) Cheap-First Execution Order

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Owner:** Jimmy Lin
**Recorded by:** Codex
**Status:** APPROVED; ADDITIVE EXECUTION ORDER UNDER PR-25
**Scope:** G7-A1 scheduling and early checkpoint only; roster/budget unchanged

## Owner response

After Codex proposed $0 mock validation followed by retained production work on the
cheapest fixed-roster models before the expensive models, Jimmy responded:

> approve

## Exact materialization

This approval adds the following fail-safer scheduling order to PR-25 without changing
its measurement, roster, provider ceilings, call/attempt envelope, or $30 hard NTE:

1. complete all driver, hash, ledger, replay, returned-model, cost, and NTE tests with
   mocks/stubs for **$0**;
2. run the required Mistral paraphrase-author stage;
3. within battery 1, issue one retained production canary for each of the three cheapest
   fixed SUTs, then complete those isolated shards in this order:
   `meta-llama/llama-3.3-70b-instruct` → `deepseek/deepseek-chat` →
   `mistralai/mistral-large-2512`;
4. persist an additive cheap-first checkpoint containing exact keys, starts/finishes,
   failures/replays, returned models, actual plus reserved cost, remaining attempt
   reserve, and projected completion cost;
5. only if that checkpoint passes every PR-25 custody/NTE condition, continue battery 1
   in ascending registered per-request maximum:
   `openai/gpt-4.1` → `google/gemini-2.5-pro` →
   `anthropic/claude-sonnet-4`;
6. retain every successful canary as production evidence; make no throwaway probe.

Use the same cheap-first SUT ordering for battery 2. The original PR-25 checkpoints
after author + battery 1, before $20, and before tie-breakers remain mandatory; the new
cheap-first checkpoint is additive.

This order reduces the cost of discovering a custody/transport failure but does not
reduce the expected final spend if all six fixed SUTs complete. It authorizes no cheap
substitute model, extra probe, call-cap increase, spend-cap increase, automatic scale-up,
denominator change, item/key edit, HOLDOUT access, or premature G7/paper verdict.
