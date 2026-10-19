# RULINGS APPLIED — 2026-10-19c: d02 dropped from v4.0; d07 parse fix authorized before D1

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-10-19
**Predecessors:** `RULINGS-APPLIED-20261018b`, `-20261019a`, `-20261019b`; execution report
`20261019c-rejudge-package-execution-report.md`. Newest ruling wins.

---

## Owner choices (2026-10-19, after reading the execution report)

| Line | Question | Owner's choice |
|---|---|---|
| D3 | Should d02 (P-PRESSURE) stay in v4.0? | **"Drop from v4.0 (Recommended)"** |
| D1 | What next on the judging architecture? | **"Fix d07, then decide (Recommended)"** |

The other D1 choices offered were the $0 referee check (Stage 3), both, or pausing v4.

## RULING 1 — D3: d02 leaves v4.0

- d02 (P-PRESSURE) is not part of the v4.0 instrument. It may return in a later version once its
  judging is repaired.
- Its stored responses and ledgers stay as a test bed for judging work.
- The v4 ship rule does not depend on d02 (`20260731o` §3), so nothing else changes.
- D4–D7 remain open.

## RULING 2 — D1 interim: find and fix judge-a's d07 parse failures, then re-measure

Under the anchored q2, judge-a (`openai/gpt-4.1-nano`) parsed 618 of 750 turns, and the failures
fell on the harder turns (report §4). The cause is not visible, because the tool did not store raw
replies. This ruling authorizes, in order:

1. **Diagnostic micro-run.** Judge-a only, anchored prompt as run, on at most 20 of the 132 failed
   turns. Raw replies are stored. New log root `logs/d07fix-20261019/diag/`.
2. **The fix.** It may change only the output-format instruction or the parser. The anchored q2
   block (`20260802e` §6) keeps its wording; models, items and the analysis stay the same. The fix
   is committed, with its tests, before step 3.
3. **Full Stage 1b re-run.** Both judges, all 750 stored turns, the fixed prompt or parser, raw
   replies stored. New log root `logs/d07fix-20261019/stage1b-fixed/`. Calibration micro-run
   first, as the tool always does.

**Spend:** **$1.00 hard ceiling** for steps 1–3 together, projection and actual. This is separate
from the closed $3.00 package, which ended at $0.5840. Stop and report on any breach.
Zero SUT calls; the holdout is never read.

**Read-outs** (defined now, before any call):
- R1 and R4 exactly as in `20261018d` §3, with its §4 labels.
- The dropped-versus-kept check from report §4, if any turns still fail.
- **v4.0 condition:** the anchored q2 may enter the v4.0 instrument only if the R4 label is
  "effective" **and** the complete-case fraction is at least 0.85 (spec `20260731j` §4.2).

**After the re-run** a dated report is written, and D1 returns to the owner.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
