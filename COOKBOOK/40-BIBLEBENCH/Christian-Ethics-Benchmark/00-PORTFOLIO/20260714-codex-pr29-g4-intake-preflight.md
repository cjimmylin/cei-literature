<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY PR-29 — bundled G4 label-intake preflight

**Date:** 2026-07-14

**Status:** STOPPED FOR ONE OWNER RULING

**Scope:** PUBLIC Part-A human-label intake only; no HOLDOUT, model call, paid work,
item/key edit, frozen-rule change, verdict, or manuscript claim

## 1. Why this preflight exists

The descriptive MVP v0.1 is complete and ratified for private circulation. Human labels
are now the release-grade rate limiter. A read-only entry audit found all 439 Part-A rows
still unsubmitted, so no G4 statistic can run today. The same audit found that the
existing G4 command is not yet capable of completing the frozen gate when labels arrive.

This is one bundled P1 preflight, not a new engineering lane. It prevents the project
from discovering one label-contract gap per later session.

## 2. Evidence: five linked gaps at the same entry point

1. **No deterministic overlap manifest.** The binding protocol fixes overlap sizes—20
   units per ordinary design, 4 dialogues for 02/07, 10 units for 05, and 8 structures
   for 09—but does not identify the exact selected `unit_id` values.
2. **No independent reliability/adjudication schema.** The repository has only Jimmy's
   primary blind CSVs. It has no separate second-labeler/test–retest submission path and
   no lossless record for Jimmy's adjudicated gold on overlap disagreements.
3. **No ceiling ingestion or computation.** `walkworthy.judge_validation` always calls
   `compute_results` with `ceiling=None`; every otherwise valid row renders
   `PENDING-CEILING`. There is no CLI argument for a reliability arm.
4. **Partial designs are accepted.** The join treats every nonblank row as submitted but
   does not require all registered rows and required fields for that design. A partial
   label file can therefore produce a dated report with an undersized `n`.
5. **The registered refusal-detector readout is disconnected.** Q-R1/Q-R2 columns exist
   and `detector_precision_recall` exists, but the CLI does not join or report them.

These are mechanics gaps, not findings about benchmark performance. Coding before the
missing input contract is frozen would guess at a preregistered gate surface.

## 3. Recommended option 1 — freeze one complete intake contract

Ratify all of the following as one indivisible contract:

### A. Deterministic overlap selection

- Select the first `N` physical data rows from each already randomized, blinded Part-A
  CSV; do not redraw or inspect model/judge identity.
- `N = 20` for 01/03/04/06/08/10; `N = 4` for 02/07; `N = 10` for 05; `N = 8` for 09.
- Check in one PUBLIC-only JSON manifest containing design, ordered `unit_id` values,
  source CSV SHA-256, row count, selection rule, and seed provenance.

### B. Independent reliability and gold custody

- Materialize a separate blind CSV for each selected overlap using the same context,
  columns, order, and structured-label syntax as the primary instrument.
- Require one declaration JSON naming `second_labeler` or `test_retest`, opaque labeler
  identifiers, and completion timestamps. `test_retest` must prove at least 14 elapsed
  days and remains subject to the framework's already-required Jimmy ratification.
- Preserve both original submissions unchanged. Record every atomic disagreement in a
  separate append-only JSONL adjudication file with `unit_id`, category, member
  identifier (or null), primary value, reliability value, Jimmy's final gold value,
  and an adjudication flag. Reject missing or extra adjudications.

### C. Fail-closed G4 intake

- Extend the existing offline CLI with explicit reliability-manifest,
  reliability-labels, declaration, and adjudication inputs. No live candidate rejudge
  is added.
- Skip a wholly untouched design; reject a partially filled design. Process a design
  only when every registered primary row, every required label field, every exact
  overlap row, and every required disagreement adjudication is complete.
- Reject duplicate/missing IDs, changed contexts, unexpected rows or fields, judge-pair
  drift, structured-member mismatch, invalid category values, and every HOLDOUT path.
- Compute the frozen per-category human–human ceiling from the untouched independent
  submissions; compute judge-versus-gold from agreement consensus plus Jimmy's explicit
  disagreement adjudications; apply the existing frozen κ forms and branch table.
- Join and report Q-R1/Q-R2 detector precision/recall and the frozen FR-15 contradiction
  readout without changing any threshold.
- Keep immutable dated output and no-overwrite behavior. One complete design may emit a
  truthful report without waiting for its wave, but no incomplete design may emit one.

### D. Implementation boundary

- Implement only after ratification, under RED→GREEN focused tests followed by one full
  suite. Do not create a labeling platform, change items, alter frozen formulas, add a
  model, access credentials, make paid calls, touch G7, or load HOLDOUT.
- After a complete design lands: G4 report → registered branch → available Part B →
  recompute/status → manuscript/PDF update in the same session.

## 4. Option 2

Jimmy supplies a different exact overlap-selection and reliability/adjudication contract.
No G4 intake code changes and no gate report occur until that alternative is complete.

## 5. Exact recommended owner ruling

> Ratify PR-29 option 1 as the complete WALKWORTHY G4 label-intake contract: select the
> registered overlap as the first blinded randomized CSV rows using counts 20 for
> 01/03/04/06/08/10, 4 for 02/07, 10 for 05, and 8 for 09; check in a hashed PUBLIC-only
> overlap manifest and separate same-schema reliability instruments; require an explicit
> second-labeler or eligible ≥14-day test–retest declaration, preserve both independent
> submissions, and record every atomic disagreement in append-only Jimmy-adjudicated
> gold JSONL; extend the existing offline judge-validation CLI to reject partial designs
> and any provenance/schema/member/value mismatch, compute the frozen human–human ceiling
> and judge-versus-adjudicated-gold κ, and report the registered Q-R1/Q-R2 detector readout;
> allow a complete design to convert immediately through G4 → available Part B → frozen
> status → manuscript/PDF, while changing no frozen threshold, item/key, model, spend,
> HOLDOUT boundary, G7 state, MVP §6A result, or public-release authority.

## 6. Current stop

- Primary labels: **0/439 filled**.
- Reliability inputs: **absent**.
- G4 verdicts: **none authorized or emitted**.
- Code changes in this session: **none**.
- Next action: Jimmy may ratify the one line above while continuing wave-1 labels. After
  ratification, Codex may implement the narrow intake bridge before the first completed
  design arrives.
