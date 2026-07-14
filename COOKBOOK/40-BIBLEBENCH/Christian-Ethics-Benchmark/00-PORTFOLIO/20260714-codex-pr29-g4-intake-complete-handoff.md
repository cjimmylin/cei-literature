<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — PR-29 G4 intake implementation handoff

**Date:** 2026-07-14

**Agent:** Codex

**Disposition:** PR-29 ratified, implemented, and verified; labels remain the trigger

## Paper-facing progress

This session removed the last known P1 mechanics blocker between completed human labels
and a frozen-formula G4 report. It did not emit a G4 result or change the manuscript:
all 439 primary Part-A rows remain blank.

Jimmy ratified PR-29 option 1 verbatim. Immutable ruling:
`20260714-jimmy-pr29-g4-intake-ruling.md`.

## Implemented contract

`harness/walkworthy/judge_validation.py` now:

- rejects a partially filled primary or reliability design;
- accepts wholly untouched designs as out of the current report;
- validates the exact manifest, row order, identity/context, schemas, provenance,
  structured members, category values, declaration, and adjudication surface;
- supports distinct second-labeler and ratified ≥14-day test–retest modes;
- preserves both independent label submissions and requires Jimmy-adjudicated gold for
  every atomic disagreement while rejecting missing or extra adjudications;
- computes the frozen human–human ceiling and judge-versus-gold κ, including design 06's
  median-of-seven rule;
- reports AC1/raw agreement plus Q-R1 detector precision/recall and the FR-15 Q-R2
  contradiction readout; and
- preserves legacy primary-only diagnostics as `PENDING-CEILING`, never G4 PASS.

No candidate rejudge or live-call path was added.

## Frozen PUBLIC overlap packet

Location: `labels/20260710-partA/reliability/`

- 10 separate same-schema blind instruments;
- 146 whole overlap units: 20 for 01/03/04/06/08/10, 4 for 02/07, 10 for 05, 8 for 09;
- every ordered unit ID, source-template hash, label-invariant identity/context hash,
  and reliability-instrument hash recorded in `overlap-manifest.json`;
- manifest SHA-256:
  `41370641bf5de8e9512ce11ac31181930548a7030bd5be026d72443be20f3abb`;
- all reliability label fields verified blank at materialization.

Instructions and an exact declaration template are in the same directory.

## Verification

- RED: 4/4 focused tests failed on the absent contract; a later focused custody test
  also proved the loader initially accepted a tampered overlap count.
- GREEN: existing + PR-29 focused G4 tests passed 25/25, including independent
  enforcement of the registered per-design overlap counts.
- Final full suite: **554/554 passed**.
- Production manifest counts, individual instrument hashes, blankness, and total 146
  units verified independently.
- Frozen descriptive MVP manuscript/PDF were not changed.

The pytest run emitted only the repository's existing macOS temporary-directory cleanup
warning after success; it did not affect test results or repository files.

## Next paper-conversion trigger

Jimmy continues wave 1 `{02,07,01}` and its independent reliability arm. Once one design
has complete primary + reliability + declaration + disagreement-adjudication inputs,
Codex runs G4 → the registered branch → available Part B → recompute/status → immediate
manuscript/PDF update. Do not wait for the rest of the wave.

## Memory consolidated

- A statistical function is not an executable gate until every registered input has a
  fail-closed custody path through the rendered report.
- Freeze independent-label instruments before either labeler sees the other's work.
- Preserve a safe diagnostic mode only when it cannot self-promote to PASS.
- With the bridge complete, further agent work before labels would be off-path; the
  rate-limiting step is now human labor, not engineering.

No HOLDOUT access, credential access, live call, paid work, model addition, G7 work,
item/key edit, frozen-rule edit, O5 verdict, MVP §6A change, or public release occurred.
