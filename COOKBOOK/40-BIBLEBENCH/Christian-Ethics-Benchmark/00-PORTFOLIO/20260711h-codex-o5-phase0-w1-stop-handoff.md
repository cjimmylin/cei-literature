<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — O5 Codex handoff: Phase 0 complete; W1 data-contract STOP

**Date:** 2026-07-11. **Executor:** Codex. **Scope:** WALKWORTHY only.
**State:** O5 execution is paused at the W1 pre-call data-contract gate under the
transition package's STOP-AND-ASK rule. This is **not** a gate verdict and is **not**
"O5 blocked on labeling"; Phase 2 was never reached.

## 1. What completed

### Required reading and Phase 0

- Read the transition package, decision framework, validity review, frozen gate memo,
  human-label protocol, PR-3 ruling, and PENDING-RULINGS in the required order.
- Shared-index start point: `eb32a42cd` on `main`; WALKWORTHY was clean at entry.
- Baseline suite: **261 passed**.
- PR-5 verified in `openrouter_backend.py`: empty-200 retry, provider fallbacks, and
  `DEFAULT_MAX_TOKENS = 32768` are present and tested.
- All 10 `labels/20260710-partA/*-partA-blind.csv` files were byte-identical to Git HEAD.
- The Phase-0 G4 placeholder was completed under TDD. `judge_validation.py` now:
  - joins filled blind CSV rows through the unblinding provenance to the immutable panel;
  - compares both distinct, stable stored judges;
  - supports strict scalar and JSON list/dict unit labels;
  - uses the frozen full rubric scales for κ, including 06's median-of-seven readout;
  - renders the protocol's reported-only supplemental rows without treating them as gates;
  - renders missing ceilings as `PENDING-CEILING`, never PASS;
  - rejects malformed joins, empty submissions, HOLDOUT paths, pair drift, and existing
    output paths.
- Exact dry-run command succeeded with two real panel cells (four judge comparisons):

  ```bash
  cd harness
  /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python \
    -m walkworthy.judge_validation \
    --labels /tmp/walkworthy-g4-mock-20260711-codex \
    --out /tmp/g4-dryrun --date 20260711
  ```

  Both rows rendered κ/AC1/raw = 1.00 and `PENDING-CEILING`; no PASS was emitted.
- Final focused suite: **20 passed**. Full Phase-0 boundary suite: **274 passed**.
- Independent spec review: PASS. Independent code-quality re-review: ready to commit.

### Deliberate Phase-0 limitation

No second-labeler/test-retest input format is specified or present, so the CLI cannot
produce a real G4 decision yet. `--candidates` is explicitly unavailable in Phase 0.
Neither limitation was guessed around. Phase 2 must add the actual ceiling/candidate
workflow only after the corresponding label artifacts exist.

## 2. W1 STOP evidence (PR-9)

The immutable O4 run cannot execute the frozen turn-level tie-breaker:

| design | disagreeing turn units | retained response available | missing response |
|---|---:|---:|---:|
| 02-twomasters | 655 | 78 | **577** |
| 07-seventyseven | 252 | 106 | **146** |
| **total** | **907** | **184** | **723** |

`run.score_item` persisted only the first turn and optional terminal response. The O4 run
directory contains only `panel_summary.json` and `scored_items.jsonl`; no recoverable
full-transcript artifact is present there.

The selector also does not represent the unresolved §B surface:

- `refusal_tag == "pending_adjudication"`: exactly **609 records**;
- unresolved cells inside those records: **1,767**;
- all panel `needs_adjudication` cells: **3,172**;
- unresolved cells outside the W1 selector: **1,405**;
- selected pending records with no judge disagreement: **20**.

If Grok-4 fails, Mistral own-family exclusion exceeds 10% in every design (minimum
14/122 = 11.5% on 02), so framework STOP trigger 8 would fire. No live probe was run:
the result is unusable until the data contract is resolved, and Jimmy additionally
directed that OpenRouter testing use only cheap models for now. The frozen tie-breaker
was not silently replaced.

Full questions and evidence are appended as **PR-9** in `PENDING-RULINGS.md`.

## 3. Evidence level and work not performed

- G4 turnkey mechanics: **OFFLINE READY / DRY-RUN PASS only**.
- W1 tie-breaker: **NOT BUILT / NO LIVE PREFLIGHT / NO SPEND**.
- W2–W5: **not executed** because W1 is first and STOP-AND-ASK is binding.
- Phase 2/3: **not entered**; no label inspection was used to issue a verdict.
- O5 gate/release status: **not evaluated**; no item kill, demotion, release claim, or
  refusal-accounting claim was made.

A read-only downstream audit found future prerequisites that should not be rediscovered
as speculative implementation: W4 has only 7/10 committed 06 reference pairs, no 09
opposite-conclusion pairs, and no executable frozen lint; W5 has no machine-readable L7
rotation list and uncovered operational choices. These threads were not advanced because
the W1 STOP controls the active queue.

## 4. Files changed

- `harness/walkworthy/judge_validation.py`
- `harness/tests/test_judge_validation.py`
- `00-PORTFOLIO/PENDING-RULINGS.md` (PR-9 appended)
- this NEW handoff

No blind label file, design item, frozen gate document, existing report, HOLDOUT artifact,
or sibling benchmark was modified. No OpenRouter call was made.

## 5. One blocker; one next command

**Active blocker:** PR-9. Jimmy must disposition transcript recovery/re-execution, the
W1 selector surface/non-tie-breakable records, and the frozen tie-breaker probe versus
the current cheap-model-only direction.

**Next exact re-entry command:**

```bash
sed -n '/## PR-9/,/^---$/p' 00-PORTFOLIO/PENDING-RULINGS.md
```

After PR-9 is ruled and any required transcript artifact exists, rerun the Phase-0 suite,
add a historical-data contract test first, and resume W1—do not start at W2.
