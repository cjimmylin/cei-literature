# WALKWORTHY O5 — PR-10 / PR-11 Unblocked Handoff

**Date:** 2026-07-12
**Executor:** Codex
**Scope:** WALKWORTHY only
**Status:** PR-10 and PR-11 CLOSED; FR-18 references PROMOTED; W4/W5 specification
blockers cleared; binding O5 execution remains at the 02/07 re-execution step.

## 1. Jimmy authority recorded

Jimmy supplied the exact requested line:

> Ratify PR-10 and PR-11 as recommended. G5 reference sets approved for gate use
> (FR-18(a)/(b) ratified).

It is preserved as R-J13/R-J14/R-J15 in
`00-PORTFOLIO/20260712-jimmy-PR10-PR11-ruling.md`. `PENDING-RULINGS.md` marks both
PRs RATIFIED/CLOSED. PR-7 remains open only as a next-cycle amendment question.

## 2. PR-11 implementation — design-09 G5 numeric rubric

`harness/walkworthy/rubrics.py` now exposes `g5_spec_for()` separately from the primary
`spec_for()` registry. Design 09's G5-only rubric contains exactly six ordinal
`[0, 0.5, 1]` categories:

- `wrong_naming`
- `debt_obligation_accuracy`
- `floor_compliance`
- `attitudinal_heart_duty`
- `reasoning_method_quality`
- `pastoral_concreteness`

Every category carries explicit 0/0.5/1 anchors. Design 09's original primary per-seat
rubric (`floor_compliance`, `owes_direction`) is unchanged. The frozen G5 `> 0.5`
comparison is unchanged.

## 3. FR-18 promotion

The corrected, reviewed DRAFT snapshots were copied without deleting or overwriting the
source files into the tracked run configuration:

- `harness/config/g5/20260712-06-references.md`
- `harness/config/g5/20260712-09-references.md`
- `harness/config/g5/manifest.json`

The manifest records source and promoted SHA-256 checksums plus R-J15 authority. The
existing directed pre-gate lint now targets these promoted copies and remains 20/20
GREEN. The gitignored source DRAFTs remain intact. No live G5 call was made.

## 4. PR-10 implementation — deterministic L7 rotation

New files:

- `harness/walkworthy/l7_name_inventory.json` — versioned 80-entry inventory: four
  male and four female fictional names from each of the ten PUBLIC design seed banks.
- `harness/walkworthy/l7_names.py` — pure deterministic selection and replacement.
- `harness/tests/test_l7_names.py` — provenance and mapping contract.

The selector excludes entries sourced from the target design, requires the caller's
complete target-design name set and excludes it, preserves explicit apparent gender,
selects by SHA-256 of `(design, item_id, role_index)`, prevents reuse within the target
design allocation, and fails closed if no eligible name remains. Exact-token
replacement changes supplied personal names only; titles, pronouns, and unsupplied
surnames remain unchanged. No HOLDOUT path was loaded and no live G7 call was made.

## 5. TDD and verification evidence

RED evidence observed before implementation:

- design-09 G5 test failed because `rubrics.g5_spec_for` did not exist;
- L7 module/inventory test failed because no module existed;
- behavior suite then failed because the L7 API did not exist;
- promoted-reference lint failed because the tracked run-configuration files did not
  exist.

GREEN evidence:

```text
tests/test_gates_and_schemas.py  16 passed
tests/test_l7_names.py            6 passed
tests/test_g5_reference_lint.py   2 passed
full harness suite              308 passed in 36.58s
```

The full suite emitted the same non-fatal macOS pytest temporary-directory cleanup
warnings seen in prior sessions. Exit status was zero.

Dashboard QA: the in-app browser correctly refused the local `file://` URL under its
safety policy, so no workaround was attempted. Local `lxml`/BeautifulSoup parsing
confirmed the title, all 12 section headings, required live/next-session anchors,
updated state text, and zero script tags.

Guardrail audit: no frozen §B/§C/§E file changed; no `DESIGNS/` or HOLDOUT path changed;
no deletion occurred; no item/key/verdict changed; no OpenRouter/model call occurred;
all additions are inside WALKWORTHY.

## 6. Live production checkpoint (observed, not advanced here)

`runs/20260712-o5-02-07-reexecution/` currently contains:

- 49 / 378 unique `(item_id, model)` records;
- `$2.804651` summed per-record cost;
- 0 panel errors and 0 schema errors;
- no matching production process running at session close.

This session did not resume the paid run because its delegated task was to close the two
specification blockers and produce an auditable commit. The prior run artifacts remain
checkpointed and resumable.

## 7. Next exact steps (binding order unchanged)

1. Read this handoff, the dashboard, and
   `20260712-codex-o5-reexecution-resumed-g5-pregate-handoff.md` for the exact resume
   command. Re-audit current coverage before launching.
2. Resume the authorized 02/07 run to 378 unique keys. Keep all six SUTs plus frozen
   judges/classifier explicit; STOP if projected total exceeds `$55`.
3. Verify every required turn and terminal transcript against the data-contract test.
4. Run the one-new-unit Mistral W1 production probe, inspect its checkpoint, then finish
   W1 over the full 3,172-cell surface.
5. Continue W2 → W3 → W4 G5 → W5 G7 in order. W4/PR-11/promotion and W5/PR-10 are no
   longer blockers; use the tracked configuration and registered functions above.
6. If labels remain absent at Phase 2, stop after Phase 1 and report
   **“O5 blocked on labeling.”** Never assemble verdicts without G4.

## 8. Persistent guardrails

Never load HOLDOUT; never delete; never overwrite reports; never edit frozen gate text;
always pass judge/classifier/tie-breaker models explicitly; use TDD; stage only explicit
WALKWORTHY pathspecs after auditing `git log -1` and the shared index; fast-forward push
only. Anything outside registered rulings goes to `PENDING-RULINGS.md`, never a guess.
