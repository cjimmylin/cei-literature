# WALKWORTHY Design 02 standalone labeling helper — design specification

**Date:** 2026-07-15

**Status:** approved in conversation by Jimmy; written specification awaiting Jimmy's
file review before implementation planning

**Scope:** `Christian-Ethics-Benchmark/` only; PUBLIC Design 02 label intake only

## 1. Objective and paper-facing sufficiency gate

Build a no-server, no-network browser helper that lets Jimmy complete the 12-unit,
21-response-turn Design 02 primary label instrument, lets an independent second
labeler complete the separate four-unit, seven-response-turn reliability instrument
without exposure to Jimmy's answers, and
lets Jimmy produce the declaration and exact rubric-category disagreement
adjudications required by ratified PR-29.

The helper succeeds when its validated exports can be imported without changing any
identity/context field and the existing fail-closed `walkworthy.judge_validation`
command accepts Design 02 as a complete G4 input. It does not compute, predict, or
display G4, a gate verdict, an O5 verdict, or a paper claim.

## 2. Controlling constraints

- Open directly with `file://`; no local HTTP service is required.
- Make no network request and load no external script, style, font, image, model, or
  API.
- Use only the frozen PUBLIC blind CSVs:
  `02-twomasters-partA-blind.csv` and
  `reliability/02-twomasters-partA-overlap-blind.csv`.
- Never read or embed `02-twomasters-partA.jsonl`, model identities, automated-judge
  scores, HOLDOUT data, or other designs.
- Preserve every source column, unit ID, row order, design value, and complete
  `context_and_response` byte-for-byte in exported CSVs.
- Keep primary and reliability data in different HTML files, browser-storage
  namespaces, and export filenames. The reliability page contains no primary answer
  or primary-progress state.
- Do not write repository files from browser JavaScript. Browser pages create
  validated downloads; Codex imports them only after independent verification.
- No item/key edit, denominator change, frozen-rule change, candidate rejudge, paid
  call, public release, or scale-up is in scope.

## 3. User-facing artifacts

The generator creates four files under
`labels/20260710-partA/design02-helper/`:

1. `02-primary-labeling.html`
   - embeds exactly the 12 primary blind rows and splits their concatenated response
     text on the exact literal ` ⟦//⟧ ` delimiter into 21 ordered turns;
   - uses the approved Layout C: one full response turn at a time, then a mandatory
     final review of all 12 units and 21 turn labels;
   - exports `02-twomasters-partA-primary-completed.csv` only after all required
     fields validate.

2. `02-reliability-labeling.html`
   - embeds exactly the four frozen reliability rows, split by the same exact delimiter
     into seven ordered turns, and the same rubric;
   - is independently shareable and contains no primary-state code or data;
   - exports `02-twomasters-partA-reliability-completed.csv` only after all four rows
     validate.

3. `02-finalization.html`
   - accepts the two completed exports through browser file inputs;
   - verifies their schema, identities, row order, immutable source fields, allowed
     values, and completeness against embedded frozen-template expectations;
   - limits comparison to the four registered overlap rows;
   - presents one Jimmy gold-choice control for each `turn_state` disagreement and
     rejects adjudications for agreements;
   - collects the PR-29 second-labeler declaration fields;
   - exports `reliability-declaration.json` and `adjudications.jsonl`.

4. `README.md`
   - gives the exact primary, independent-reliability, finalization, Codex-import, and
     G4 sequence;
   - states that the second labeler receives only the reliability HTML file and the
     existing Design 02 instructions;
   - states that downloads are not gate results and must pass the Python intake.

## 4. Primary and reliability interaction design

Each labeling page has the same deterministic flow. A CSV row is a blind unit that
contains one or two ordered response turns. The page derives those turns only from the
frozen `context_and_response` delimiter; it never consults provenance or judge output.

1. Show role, Design 02, unit ID, turn number within the unit, global turn progress,
   and a persistent rubric summary.
2. Show one complete blind response turn at a readable width, with the other turn in
   the unit available through previous/next navigation.
3. Require one `turn_state` value for each response turn from the frozen set:
   `holds_line`, `soft_concession`, `material_concession`, `full_compliance`, or
   `pushback_with_alternative`.
4. Require confidence `1`, `2`, or `3`; allow optional notes.
5. Require Q-R1 `yes`, `partially`, or `no`.
6. If Q-R1 is `yes` or `partially`, require Q-R2 `yes` or `no`. If Q-R1 is `no`,
   force Q-R2 to `n-a` in the export and do not show an active Q-R2 choice.
7. Serialize each completed row's ordered turn labels as a compact JSON list in
   `turn_state`, equivalent to `json.dumps(values, ensure_ascii=False,
   separators=(",", ":"))`, using turn order and no inferred or omitted member. Save
   the draft in
   a role-specific `localStorage` namespace derived from the page
   role and frozen source-template SHA-256.
8. Permit previous/next navigation and keyboard operation without allowing navigation
   to erase an answer.
9. After the last turn, show the mandatory review screen with unit ID, every indexed
   turn label, confidence, Q-R state, and completion status. Each full response turn
   remains available by expanding a unit.
10. Enable export only when every unit passes validation. Export uses the original CSV
    header and row order and changes only the label-entry columns.

The pages do not include a repository-save button. A draft reset, if implemented,
requires an explicit confirmation and affects browser storage only, never a repository
file.

## 5. Finalization and declaration

The finalization page performs all validation locally in the browser:

- exact expected filenames are advisory, while embedded source-template hashes and
  identity/context values are authoritative;
- the primary file must contain all 12 rows and the reliability file exactly the four
  frozen first-row overlap units;
- headers, row order, identity/context, label vocabulary, confidence, Q-R1, and
  conditional Q-R2 must match the PR-29 intake contract;
- any missing, extra, duplicate, reordered, partially filled, or altered row stops
  finalization with a precise error and creates no output;
- only differing `turn_state` values at the seven indexed turns across the four
  overlap units require Jimmy gold adjudication for Design 02;
- each adjudication object uses the registered fields: `unit_id`, `category`, `member`,
  `primary_value`, `reliability_value`, `gold_value`, `adjudicator`, and
  `adjudicated`;
- `category` is `turn_state`, `member` is the registered one-based integer turn index,
  `adjudicator` is `Jimmy`, and `adjudicated` is `true` for this Design 02 surface;
- no row is emitted for an agreement;
- the declaration uses `mode: "second_labeler"`, distinct nonblank opaque primary and
  reliability labeler IDs, ISO-8601 completion timestamps, and
  `test_retest_ratified: false`.

Final exports remain provisional inputs until Codex independently checks their hashes,
imports the completed values into the registered PR-29 paths, and runs the existing
Python G4 intake.

## 6. Implementation architecture

Create `harness/walkworthy/design02_labeling_helper.py` as a deterministic generator.
It reads the two allowed blind CSVs, computes source hashes, splits response text only
on the exact frozen delimiter, serializes only the frozen rows, ordered response turns,
and rubric constants, and writes the three self-contained HTML pages plus README. It
fails if source counts, expected per-row turn counts `[2,2,1,2,2,1,2,2,2,2,1,2]`,
headers, design values, overlap membership/order, or blank label-entry cells differ
from the registered Design 02 templates. The reliability packet must have the frozen
first-four turn counts `[2,2,1,2]`.

The generated pages use embedded HTML, CSS, and plain JavaScript. They do not depend on
a package manager or browser framework. Shared behavior may be generated from one
Python template function, but every delivered HTML file remains self-contained.

Create `harness/tests/test_design02_labeling_helper.py`. Tests call the generator in a
temporary directory; committed generated artifacts are then byte-compared with a fresh
generation to prevent manual drift.

## 7. Fail-closed behavior

- Source-template mismatch: generator stops; no artifact is replaced.
- Browser-storage source hash mismatch: ignore the stale draft and explain why; do not
  coerce or migrate it.
- Invalid or incomplete unit: block review completion and export; identify the unit and
  field.
- Imported-file identity or schema mismatch: block finalization and create no
  declaration/adjudication output.
- Same primary and reliability opaque ID: block declaration export.
- Missing gold choice for a true `turn_state` disagreement: block adjudication export.
- Any unexpected Design 02 category, structured member, or PR-29 contract behavior:
  stop the implementation thread and record one P0/P1 escalation; do not invent a
  browser-side rule.

## 8. Verification requirements

Tests and manual checks must prove:

1. exact 12-primary/four-reliability row counts, 21-primary/seven-reliability turn
   counts, per-row turn counts, one-based member order, and overlap order;
2. absence of model identities, judge outputs, unblinding JSONL content, HOLDOUT paths,
   external URLs, and network APIs;
3. correct frozen per-turn `turn_state` collection and compact ordered JSON-list
   serialization, plus confidence, Q-R1, and conditional Q-R2 validation;
4. role-separated storage namespaces and absence of primary data from the reliability
   page;
5. CSV round-trip preservation of headers, ordering, identity/context, quoting, and
   multiline response text, plus exact export of user-entered notes;
6. export blocking on every incomplete or invalid state;
7. exact agreement/disagreement handling and registered JSONL field values;
8. declaration rejection for identical/blank IDs or malformed timestamps;
9. deterministic regeneration of all committed helper files;
10. successful XML/HTML parsing and browser inspection at desktop and reduced widths;
11. focused new tests, existing 25-test PR-29/G4 regression, and the full WALKWORTHY
    suite before integration.

## 9. Repository changes and exclusions

Planned additions:

- `harness/walkworthy/design02_labeling_helper.py`
- `harness/tests/test_design02_labeling_helper.py`
- `labels/20260710-partA/design02-helper/02-primary-labeling.html`
- `labels/20260710-partA/design02-helper/02-reliability-labeling.html`
- `labels/20260710-partA/design02-helper/02-finalization.html`
- `labels/20260710-partA/design02-helper/README.md`

Planned session-close updates after implementation:

- `00-PORTFOLIO/project-dashboard.html`
- one new dated verification/handoff document

Explicitly unchanged: the frozen gate documents, existing blank primary/reliability
CSV templates until validated human exports are imported, historical reports, run
data, manuscript/PDF, G7, OPEN6, items/keys, and HOLDOUT.

## 10. Acceptance criteria

The implementation is acceptable only when Jimmy can open the primary HTML directly,
resume and complete all 21 turn labels across 12 units, review them, and download a
schema-valid CSV containing one compact ordered `turn_state` JSON list per row; an
independent labeler can do the same for exactly seven turns across four reliability
units without primary-answer exposure; and Jimmy can load both exports into the
finalizer and obtain a valid second-labeler declaration and exactly the required
turn-indexed Design 02 `turn_state` adjudications. Codex must then be able to import the
outputs without identity changes and reach the existing PR-29 G4 command without
additional UI specification work.
