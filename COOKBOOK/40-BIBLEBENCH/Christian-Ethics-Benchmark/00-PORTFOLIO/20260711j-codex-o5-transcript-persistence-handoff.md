<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — O5 Codex handoff: forward transcript persistence complete

**Date:** 2026-07-11. **Executor:** Codex. **Scope:** WALKWORTHY only.
**State:** the forward mechanics needed for a future 02/07 re-execution now retain every
captured turn. O5 itself remains paused at the PR-9 pre-call gate; no W1 adjudication,
model probe, paid re-execution, downstream phase, or gate verdict ran.

## 1. Re-entry audit

This continuation did not assume the prior Codex handoff was current. It read the living
dashboard, newest handoff, PR-9, and Claude's subsequent committed changes. Claude added:

- the living `00-PORTFOLIO/project-dashboard.html` and its mandatory update protocol;
- dashboard-aware Codex transition/re-entry prompts;
- `20260711i-fable-pr9-adjudication-boot-prompt.md` for a future Fable ruling session.

Those commits did **not** rule PR-9, recover transcripts, change the selector, authorize
spend, or implement W1. WALKWORTHY was clean on entry; all 10 blind label CSVs remained
byte-identical to Git HEAD. Baseline: **274 passed**.

## 2. Root cause and bounded fix

The full data-flow trace confirmed a single lossy boundary:

1. `executors._run_scripted` already captured every branch-selected user prompt, model
   response, turn index, branch state, refusal hint, and terminal exchange in memory.
2. Both judges scored those in-memory turn units.
3. `run.score_item` manually serialized only the first response, turn count, and terminal
   response. Turns 2…N were discarded before `panel.py` wrote `scored_items.jsonl`.

The forward-only fix adds an explicit `_serialize_administration` helper. New records now
retain:

- all legacy fields unchanged: `label`, `kind`, first-turn `response`, `n_turns`, and
  terminal-response alias `terminal`;
- `system`;
- ordered `turns[]` entries with `index`, `user_text`, `response`, `branch_state`, and
  `refused_hint`;
- `terminal_user_text` and `terminal_response`.

Explicit `getattr` defaults preserve the existing duck-typed `score_item` test surface.
No prompt, branching, judging, refusal/outcome logic, metric, schema, selector, model,
manifest, checkpoint key, or historical artifact changed. The immutable O4 JSONL remains
unmodified and its 723 missing responses remain unrecoverable.

## 3. TDD and verification evidence

- RED: `tests/test_transcript_persistence.py` collected the 02 and 07 fixture cases; both
  failed with the expected missing serialized transcript fields after legacy aliases
  had already matched.
- GREEN: the same focused file passed **2/2**.
- Related regression slice (`transcript_persistence`, `executors`, `pr3`, `panel`):
  **37/37 passed**.
- Full suite: **276/276 passed**.
- Independent spec review: PASS.
- Independent code-quality review: ready to commit; no Critical/Important issues.

No OpenRouter call occurred; spend = $0. HOLDOUT and sibling benchmarks were not accessed.

## 4. Files changed

- `harness/walkworthy/run.py`
- `harness/tests/test_transcript_persistence.py` (NEW)
- `00-PORTFOLIO/project-dashboard.html` (required living update, in place)
- this NEW dated handoff

No existing dated report/handoff, blind label, frozen rule, design item, O4 run artifact,
or `PENDING-RULINGS.md` entry was overwritten.

## 5. One blocker; authorization still required

**Active blocker:** PR-9 remains open. The user's statement that the working limit reset
licensed this offline continuation, but it did not specify a ruling on the three
methodological/spend choices below. Codex therefore did not infer one.

To resume W1, Jimmy/Fable must still log:

1. whether to authorize a NEW immutable six-SUT 02/07 re-execution (estimated in the
   dashboard at ~$10–15) or supply recovered transcripts;
2. whether W1 covers the full §B `needs_adjudication` surface and how the 20 parse/arbiter
   pendings route (PR-9 item 2, Fable-delegable or Jimmy-direct);
3. whether to authorize the frozen Grok-4 reliability probe despite the earlier
   cheap-model-only direction, or accept the Mistral fallback plus Part-B sizing.

**Next exact re-entry command:**

```bash
sed -n '/## PR-9/,/^---$/p' 00-PORTFOLIO/PENDING-RULINGS.md
```

After the rulings land: run the 276-test baseline, create a NEW immutable re-execution
directory if authorized, verify its full-turn data contract before any tie-break call,
and resume W1—never skip to W2.
