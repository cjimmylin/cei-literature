# WALKWORTHY — PR-25(a) Cheap-First G7-A1 Execution Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Status:** PR-25(a) APPROVED; CHEAP-FIRST G7-A1 EXECUTION NEXT
**Scope:** Additive scheduling/custody order only; no model, surface, or budget change

## Outcome

Jimmy responded `approve` to the proposed cheap-first risk-control sequence.
`20260713o-jimmy-pr25a-cheap-first-order.md` records the binding materialization.

The exact PR-25 G7-A1 roster, hashes, provider ceilings, 9,709 planned logical calls,
971 replay reserve, 10,680 POST cap, concurrency ≤2, and $30 hard NTE remain unchanged.
The approved execution order is now:

1. mock/stub driver and custody validation for $0;
2. required Mistral paraphrase-author stage;
3. battery-1 retained canaries followed by complete isolated shards:
   Llama 3.3 70B → DeepSeek Chat → Mistral Large 2512;
4. additive cheap-first custody/cost checkpoint;
5. only after checkpoint PASS: GPT-4.1 → Gemini 2.5 Pro → Claude Sonnet 4;
6. mandatory end-of-battery-1 checkpoint;
7. repeat the cheap-first SUT order for battery 2, then follow the unchanged pre-$20,
   frozen P1, pre-tie, and conditional tie-breaker stages.

Every successful canary is retained as production evidence. There is no throwaway
probe, substitute model, added model, or automatic scale-up.

## Session boundary

This approval-record session made no credential access, live request, spend, code
change, HOLDOUT access, label/item/key edit, or G7 verdict. Execution remains next.

## Paper-facing progress and next trigger

PR-25(a) reduces the financial exposure before the expensive fixed SUTs without
changing scientific sufficiency. The next paper-facing artifact remains the validated
pair of 438-cell G7 perturbation surfaces plus complete frozen P1/Part-B routing.
Human labels independently remain the critical path for G4 and verdict assembly.

## Next session

Run dashboard §12 exactly. Establish the $0 driver baseline first, then execute the
retained cheap-first production order with the additive checkpoint. Stop rather than
starting GPT-4.1/Gemini/Claude if any custody, cost, reserve, returned-model, or
projected-NTE condition fails.

On session close: update `00-PORTFOLIO/project-dashboard.html`, write a NEW dated
handoff, and commit/push WALKWORTHY paths only with explicit pathspecs.
