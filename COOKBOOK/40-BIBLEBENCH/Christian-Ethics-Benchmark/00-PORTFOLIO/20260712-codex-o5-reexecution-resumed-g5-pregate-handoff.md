<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — O5 re-execution resumed; G5 pre-gate mechanics complete

**Date:** 2026-07-12

**Scope:** WALKWORTHY only. HOLDOUT never loaded. No item/key/gate/verdict edits.

**Status:** Authorized 02/07 production re-execution resumed and still running. W1 live
adjudication has not started. The expressly authorized G5 pre-gate parallel mechanics
are complete, but live G5 remains blocked on Jimmy promotion plus PR-11.

## Production checkpoint at handoff

- Run: `runs/20260712-o5-02-07-reexecution/`
- Exact coverage: **34/378 unique `(item_id, model)` keys**, zero duplicates
- Current model: `openai/gpt-4.1` (34 records)
- Spend: **$2.212787**, 1,020 calls, **0 error rows**
- Transcript contract on current records: **34 records / 306 turns / 0 terminals**,
  every recorded response present
- Observed cost projection remains below the binding **>$55 STOP** threshold
- The process was alive at close. If it stops, resume the byte-identical panel command
  from the preceding handoff; checkpointing skips completed keys.

Do not treat the run as complete until it reaches exactly 378 unique keys, final errors
are reconciled, and the complete turn+terminal contract passes.

## G5 directed pre-gate lane completed (no live G5 calls)

Implemented `harness/walkworthy/g5_reference_lint.py` under RED→GREEN TDD and ran it on
both reviewed local DRAFT sets:

- exactly 10 public 06 pairs + 10 public 09 pairs;
- 06 CHECK 1–5 machine-checkable portions;
- 09 L-2…L-6 structural checks;
- rendered 09 D01 verification/fix logged in the DRAFT;
- 06 K03 classified mechanically as a **verdict split**, not FR-18(a)'s K01 method
  special case; and
- directed trims reduced 06 D01 to **1.0186** and L03 to **1.0958**.

Fresh full regression: **301/301 passed in 49.31 s** (exit 0; same pre-existing macOS
pytest temporary-directory cleanup warning).

Immutable evidence:
`00-PORTFOLIO/20260712-codex-G5-pre-gate-lint-report.md`.

The corrected `20260712-G5-06/09-references-DRAFT.md` files remain intentionally
gitignored and unpromoted. Live G5 was not run.

## New STOP threads parked (not guessed)

### PR-10 — L7 source/mapping missing

R-J4 authorizes formalizing an L7 rotation list, but the WALKWORTHY scope contains no
actual canonical diverse-name list or role/gender/title mapping. PR-10 asks Jimmy to
supply a source or authorize the deterministic cross-design inventory default. W5 is
blocked; other lanes are unaffected.

### PR-11 — design-09 G5 numeric computation undefined

Frozen G5 uses “>0.5 points per rubric category.” The executable 09 rubric contains a
categorical `owes_direction` with no numeric distance, while the reviewed DRAFT's six
qualitative audit categories have no registered `ScoringSpec`. PR-11 asks Jimmy to
choose/register the computation. G5 driver/live scoring is stopped; W1/W2/W3 continue.

Even after PR-11, live G5 separately requires the existing promotion line:
“G5 reference sets approved for gate use (FR-18(a)/(b) ratified).”

## Shared-index event

Concurrent sibling commit `aa0477933` broadly swept the worktree while this session ran.
It included the G5 linter/test/report, PR-10, and active run manifest/error ledger. This
session did not rewrite that commit. PR-11, this handoff, and dashboard updates remain
the paths for the next explicit WALKWORTHY commit.

## Next exact steps

1. Finish/resume the exact 02/07 run to 378 keys; monitor cost/errors.
2. Run the final transcript-contract/coverage/cost validation.
3. Run the explicit one-new-unit W1 production probe from the preceding handoff, inspect
   the checkpointed event, then rerun without the one-unit cap to complete W1.
4. If W1 observes `ambiguous_tolerance_cells > 0`, append exact cells to
   `PENDING-RULINGS.md` and stop only that thread. Otherwise emit cell-aware Part B and
   verify all 3,172 cells are resolved or routed.
5. Continue W2 → W3 in order. Do not run W4 G5 until promotion + PR-11 are resolved. Do
   not run W5 until PR-10 is resolved. Labels are still absent; no Phase-2 verdicts.
