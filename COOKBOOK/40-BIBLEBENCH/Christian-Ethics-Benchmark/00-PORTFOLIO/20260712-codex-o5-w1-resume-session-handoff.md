<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Next Session: O5 W1 Production Resume

**Prepared:** 2026-07-12 by Codex

**Directory:**
`CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`

**Primary exit criterion:** finish W1 mechanically: complete and validate the 02/07
re-execution, then complete the bounded Mistral probe and full W1 adjudication. Do not
start W4/W5 early merely because their former specification blockers are closed.

## Verified entry state

- Git HEAD at preparation: `7b88901ad`.
- Harness: 308 tests green at the preceding handoff.
- Re-execution: `runs/20260712-o5-02-07-reexecution/` = **49/378** unique
  `(item_id, model)` keys, **$2.804651**, 0 panel errors, 0 schema errors.
- No matching production process was running at preparation time.
- PR-10/PR-11 are CLOSED; FR-18 references are promoted. These are no longer blockers.
- Part-A labels remain 0/439. No G4-dependent verdict is licensed.

Re-audit all mutable facts on entry; a sibling session may have advanced them.

## Paste-ready next-session order

```text
You are Codex executing the next WALKWORTHY O5 session: W1 PRODUCTION RESUME.
SCOPE LOCK: work ONLY inside
CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/. Never load HOLDOUT,
never delete, never overwrite a dated report, never edit frozen §B/§C/§E text.

ON OPENING read, in order: (1) 00-PORTFOLIO/project-dashboard.html §1 + §6 + §12;
(2) NEWEST dated handoff — 20260712-codex-o5-w1-resume-session-handoff.md;
(3) 20260712-codex-pr10-pr11-unblocked-handoff.md; (4)
20260712-codex-o5-w1-build-reexecution-running-handoff.md §§Active production command
+ Next exact steps; (5) 20260712-fable-codex-full-handoff.md §4; (6) AGENTS.md and
PENDING-RULINGS.md. Skip work already completed by a newer commit or run checkpoint.

PRIMARY TASK — FINISH W1, IN ORDER:
1. Preflight from harness/: git log -1; git diff --cached --name-only; full pytest;
   recount unique re-execution keys/cost/errors and confirm no duplicate process.
2. If coverage is below 378 and no process is alive, resume the byte-identical panel
   command in 20260712-codex-o5-w1-build-reexecution-running-handoff.md §Active
   production command. Checkpointing must skip completed keys. Use the six registered
   SUTs and explicit frozen judge/classifier slugs exactly as written; do not substitute
   cheap models into the production measurement. Cheap models remain testing-only.
3. Monitor checkpoint growth, error rows, and accumulated cost. STOP if projected total
   exceeds $55. Do not expose the OpenRouter secret.
4. At exactly 378 unique keys, run the complete transcript data-contract validation:
   every required turn and terminal response present, zero duplicates, errors reconciled.
   Do not treat the re-execution as complete before this passes.
5. Run W1's required one-new-unit probe using
   mistralai/mistral-large-2512 and --max-new-tiebreak-units 1. Inspect the persisted
   event and parse result. Never re-probe Grok-4.
6. Rerun the same W1 command without --max-new-tiebreak-units. Verify the full
   3,172-cell FR-16 surface is resolved or routed to cell-level Part B, including all
   580 own-family cells. If ambiguous_tolerance_cells > 0, append the exact cells to
   PENDING-RULINGS and stop only that thread; never guess.
7. Primary session exit = W1 complete with a NEW dated evidence/handoff artifact and
   dashboard updated. Only after W1 is verified may the session begin offline W2 Δ(J);
   never jump to W3/W4/W5.

CONSTRAINTS: explicit model slugs everywhere; TDD for any mechanics fix; no item/key
edits from performance; labels absent means no Phase-2 gate verdicts; shared index
requires git log -1 + git diff --cached --name-only immediately before explicit
WALKWORTHY path staging; fast-forward push only.

ON CLOSING: update project-dashboard.html §1/§6/§11/§12, write a NEW dated handoff,
commit and fast-forward push WALKWORTHY paths only.
```

## Why this is next

W1 is the earliest unfinished node in the binding sequence and supplies adjudicated
cells required by W2/W3. W4 and W5 are now specification-ready but still downstream.
Labels do not block this session; they begin blocking only at Phase 2 after W5.
