# WALKWORTHY O5 — W1 + W2 complete; PR-16 FR-7 stop handoff

**Date:** 2026-07-13
**Agent:** Codex
**Scope:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/` only

## Outcome

W1 and W2 are complete. W2 triggered the registered FR-7 branch: the Google judge has
significant own-family inflation on designs 05 and 06. W3 and the paper results fill
must not run until Jimmy rules PR-16's three missing materialization mechanics.

No HOLDOUT path was loaded. No file was deleted. Frozen §B/§C/§E and FR documents were
not edited. Existing W1/W2 evidence remains immutable; the living dashboard is the only
in-place report-like edit.

## Jimmy rulings logged verbatim

`00-PORTFOLIO/PENDING-RULINGS.md` now records and closes:

- **PR-14:** record-level frozen `scalar_by_judge`; within-item permutation of the one
  own-family indicator across six SUT cells; 10,000 resamples; seed 20260710;
  one-sided positive-inflation p-value with +1 correction; flag only `p < .01`.
- **PR-15:** all 128 numeric-tolerance ambiguity cells route to Part B; tolerance is
  unchanged; no coerced median and no fourth judge.

PR-13's previously ratified 2,682-group / 3,176-cell surface was used exactly.

## W1 — complete and accepted

Artifact: `runs/20260712-o5-tiebreak/`

- 2,682 groups / 3,176 cells.
- 2,224 Mistral tie-breaker units; 458 own-family units.
- 2,682 event rows and 2,682 unique `(item_id, model, unit_key)` keys.
- 128 PR-15 ambiguity cells now carry `part_b_ambiguous_tolerance`.
- 1,181 total Part-B cells; zero `pending_ruling_ambiguous_tolerance` cells.
- `processed_groups=2682`, `complete=true`.
- Transcript contract unchanged: 378 records / 2,748 turns / 162 terminals.
- Bounded 05 re-parse unchanged: 11 selected / 5 recovered / 6 failed.
- Tracked cost: `$1.1373068`, 2,224 calls, 2,711,620 prompt tokens, 54,928 completion
  tokens. The PR-15 replay used all checkpoints and made zero new calls.

Implementation is fail-closed by default: `--ambiguous-tolerance-policy` defaults to
`stop`; only explicit `part_b` applies Jimmy's PR-15 ruling.

## W2 — complete; two significant flags

Artifact: `runs/20260713-o5-home-advantage/home_advantage.json`

The new offline module `harness/walkworthy/home_advantage.py` implements PR-14 exactly,
requires the frozen explicit judge pair, validates six unique SUT records and one
own-family SUT per item, rejects HOLDOUT/path traversal, and refuses output overwrite.
It produced 20 judge × design rows and two flags:

| design | judge | Δ(J) | permutation p | action |
|---|---|---:|---:|---|
| 05-ordoamoris | google/gemini-2.5-flash | 0.346875 | 0.0000999900 | disqualify on Google-SUT cells |
| 06-crookedpath | google/gemini-2.5-flash | 0.1046082949 | 0.0022997700 | disqualify on Google-SUT cells |

All other rows were non-significant. W2 was offline: no model/API calls and no spend.

## PR-16 — active blocker

FR-7 requires the affected cells to use the surviving OpenAI judge + Mistral. The exact
surface is 63 Google-SUT item units / 249 rubric cells:

- 05: 32 `google/gemini-2.5-pro` items × `rationale_honesty` = 32 cells.
- 06: 31 Google-SUT items × seven criteria = 217 cells.
- Eleven complete, defect-free, byte-identical Mistral unit judgments already exist in
  W1 (2 on 05; 9 on 06); 52 units are missing.
- Eleven affected 06 cells overlap PR-15's fixed Part-B ambiguity list.

The frozen text does not say whether to reuse the 11 judgments, how the replacement
OpenAI+Mistral pair resolves disagreement/defect, or whether FR-7 supersedes the 11
PR-15 overlaps. `PENDING-RULINGS.md` therefore opens PR-16. Recommended one-liner:

> Ratify PR-16 option 1: strike Google on all 249 Google-SUT 05/06 rubric cells; reuse
> 11 existing Mistral unit scores and call only the 52 missing units; adjudicate solely
> under the frozen OpenAI+Mistral two-judge tolerance/mean rule, route disagreements or
> defects to Part B, and let this FR-7 recompute supersede the 11 overlapping PR-15
> ambiguity routes in a new immutable derived run.

Do not start FR-7 materialization or W3 until PR-16 is closed. If Jimmy chooses another
option, require and log its exact contract; never infer one.

## W3 and paper readiness

The W3 renderer was made compliant under TDD but was not run. It now:

- validates the exact complete W1 surface and explicit model provenance;
- refuses to overwrite an existing report;
- publishes §B denominators, exclusion percentages, and FR-1 status per design × model;
- raises `W3 STOP` if design 05 does not recompute to the binding FR-5 G1+G2 failure;
- renders FR-10 strict-identity sensitivity for 04/06/10 and names flips;
- asserts the tie-aware V-13 six-model ranking relationship for 08/09;
- computes FR-13 G8 eligibility/item identities from all six resolved adjudicated
  outcomes and recomputed PR-3 refusal tags.

Once PR-16 is materialized, W3 opens the paper conversion trigger. Under
`20260712-codex-paper-fill-boot-prompt.md`, fill only the W3-licensed portions of
`PAPER/06-results-scaffold.md`: Table 6.1; Table 6.2 G1–G3 statistics; Table 6.4 G9;
and licensed sensitivity prose. Δ(J), G4/G5/G6/G7, statuses, released readouts, and
release claims remain blocked by their named downstream artifacts/sign-offs.

**Paper-facing progress:** corrected W1 evidence and the mandatory Δ(J) validity test
now exist. No paper value was filled because the FR-7 branch must precede W3.

**Next paper-conversion trigger:** a PR-16-compliant derived run followed by the NEW
dated W3 readings file.

**Ancillary work:** only the W3 mechanics required for that immediate next trigger,
plus the required dashboard/handoff/git closure. No refactor or new concurrency
experiment was undertaken.

## Verification

- Focused changed-path suite: 34 passed.
- Full suite: **334 passed in 57.24s**.
- `git diff --check`: clean on changed implementation/ruling paths.
- Known non-failing warning: macOS pytest temporary-directory cleanup race
  (`Directory not empty`), present before these changes.

## Next session

Use dashboard §12. Its paste-ready prompt starts with PR-16, then requires a NEW
append-only FR-7 derived run, exact acceptance checks, W3, and immediate licensed paper
fill. W1 and W2 are complete and must not be rerun.

Labels remain 0/439. Jimmy's wave-1 labels `{02,07,01}` remain the parallel release
critical path; they do not block PR-16/W3.

On session open: load `00-PORTFOLIO/project-dashboard.html` (Live status + §12 first).

On session close: update the dashboard per `AGENTS.md §Project dashboard`, write a NEW
dated handoff, and use shared-index-safe explicit WALKWORTHY pathspecs for commit/push.
