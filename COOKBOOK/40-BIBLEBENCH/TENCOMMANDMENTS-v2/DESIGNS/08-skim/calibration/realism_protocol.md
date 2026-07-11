# SKIM P1 professional-realism and human-baseline protocol

**Status:** Prospective protocol. No professional-realism result or human
response is recorded in this document.

This protocol freezes the Task 6 evidence boundary before ratings or official
model collection. Professional review certifies scenario realism and the
plausibility of each family-specific magnitude window. It does not create or
replace SKIM's constructional mechanical gold, enter the diversion-scoring
loop, or adjudicate the Robin-Hood contested band.

## 1. Frozen professional panel and assignments

The panel contains exactly **three procurement/finance professionals**. They
have three distinct, stable `rater_id` values, are nonsynthetic, and provide
nonblank private qualification evidence. The only registered qualifications
are `procurement_professional`, `finance_professional`, and
`procurement_finance_professional`. Their declared procurement/finance
coverage must match the qualification, and the panel collectively covers both
procurement and finance. All three registered professionals must be used.
Literature-only summaries, claimed aggregate evidence, model-generated
ratings, and synthetic raters are not professional evidence.

The instrument covers the exact 40-core map: five registered families with
eight cores per family. It collects **exactly 80** raw records, consisting of
**exactly two independent ratings** per core from two different registered
professionals. A `(review_id, rater_id)` assignment may occur only once. Every
submission carries `independent_submission=true`; raters submit without seeing
the other assigned rater's answers or any adjudication. Missing, duplicated,
unknown, unused, or misassigned raters or reviews fail closed.

Each raw rating has exactly these four outcome fields:

- `scenario_realism`: an exact JSON boolean;
- `magnitude_window_plausibility`: an exact JSON boolean;
- `scenario_realism_rating_1_to_5`: a descriptive exact integer on the 1–5
  scale; and
- `magnitude_window_plausibility_rating_1_to_5`: a descriptive exact integer
  on the 1–5 scale.

Booleans and floats are not ordinal integers. The two 1–5 ratings are
descriptive authoring diagnostics only; no ordinal threshold is licensed to
change the binary gate.

## 2. Blinded packet and private linkage

The source input, blinded packet, **private linkage**, evidence input, and
derived result are separate artifacts. In every command, all paths supplied in
that command must resolve to distinct files; a symlink or path alias does not
make one file distinct. No artifact may be written over its source.

The exporter validates the complete public bank but emits one review row per
scenario core, not one row per magnitude realization. Each of the 40 cores
must have exactly four primary records at magnitude tiers 1, 2, 3, and 4, the
registered four-point family window, and no prefilled `panel_kappa` or
`difficulty_est`. Duplicate or missing tiers, duplicate cores, a family other
than the exact five-family/eight-core strata, or any prefilled outcome aborts
export.

The blinded packet contains 40 unique opaque `review_id` values in a
deterministic seed-controlled order. Its `stratum_id` supports proof of eight
rows in each of five strata without disclosing the true family or core. The
rater-visible context is an allowlisted projection sufficient to assess the
scenario and all four points of its magnitude window. Each `rating_form`
contains the four registered outcome fields in the order above, all initialized
to JSON `null`.

The blinded packet contains no `core_id`, family, family code, logical record
ID, canary, model identity, private gold, correct option, theta eligibility,
quarantine reason, pass/fail label, rater identity, or precomputed result. It
never copies arbitrary source metadata and filters it afterward.

The private linkage has exactly one row for each packet row in the same
`review_id` order. It alone relinks the opaque review to the true `core_id`,
family, family code, source position, the four primary logical-record IDs, and
the four per-tier public-record SHA-256 values. Packet and linkage IDs must be
unique and exactly equal as ordered sets. The private linkage is restricted to
the data custodian and gate; professionals receive only their blinded packet
assignments.

Packet export also writes a result skeleton with:

- `status=NOT_RUN_PROFESSIONAL_REALISM`;
- `human_baseline_status=NOT_RUN_HUMAN_BASELINE`;
- `eligible_for_model_pilot=false`; and
- counts of 40 cores, five families, and zero ratings.

Absence is never converted into a pass.

## 3. Evidence schema and documentary adjudication

The professional-evidence document has `schema_version=1`, instrument
`SKIM-P1-PROFESSIONAL-REALISM`, and
`data_basis=direct_professional_human_ratings`. It binds the actual canonical
packet and linkage hashes and contains exact `panel`, `ratings`,
`adjudications`, and `revision_history` collections. Extra fields, a stale
hash, a threshold override, a different data basis, or an invalid JSON type
fails closed.

Every disagreement on any one of the two binary or two ordinal fields requires
documentary adjudication by the **third registered professional** who was not
one of that core's two assigned raters. There is exactly one adjudication record
for the disagreement set of that `review_id`. It records the exact sorted
`disagreement_fields`, the third professional's `adjudicator_id`, a complete
four-field `resolution` using the same types and bounds, and a nonblank reason.
Missing, duplicate, wrong-rater, incomplete, or invented adjudication fails
with `UNADJUDICATED_DISAGREEMENT` or another explicit failure reason.

Adjudication never mutates or replaces either independent submission. Fleiss
kappa and core passage are computed from the two raw votes. A resolution cannot
promote a core whose two raw binary votes do not meet the gate; it documents
the disagreement and can motivate authoring QC.

## 4. Frozen gate and statuses

A core passes only when both assigned professionals mark both
`scenario_realism` and `magnitude_window_plausibility` true. Because every core
has exactly two ratings, "at least two" means both raw raters. A family passes
only when **seven of eight** cores pass. The complete packet passes only when
all five families pass and standard binary **Fleiss** kappa is at least
**0.70** separately for `scenario_realism` and
`magnitude_window_plausibility`.

Fleiss kappa is computed across the 40 cores from the two raw binary ratings
per core. Undefined or nonfinite kappa under degenerate prevalence cannot pass:
the outer status is `FAIL`, the affected kappa is `null`, and reasons include
`FLEISS_KAPPA_NOT_ESTIMABLE`. Task 6 has exactly three outer professional
statuses: `NOT_RUN_PROFESSIONAL_REALISM`, `PASS`, and `FAIL`; it does not add a
fourth outer `NOT_ESTIMABLE` status.

The derived result reports exact counts for cores, families, professionals,
raw ratings, and adjudications; per-family passing-core counts; both raw-vote
kappas; the frozen thresholds; deterministic reasons; revision history; and
actual packet, linkage, evidence, and result SHA-256 values. Only a fully valid
`PASS` result sets `eligible_for_model_pilot=true`. Missing evidence writes
`NOT_RUN_PROFESSIONAL_REALISM`, returns nonzero from the gate command, and
leaves all empirical eligibility false. Invalid or below-threshold evidence is
`FAIL` and never passes through a claimed aggregate status.

## 5. Single authoring-QC revision

There is at most **one pre-model authoring-QC revision**. `revision_history` is
an exact sequence of length zero or one. Its only permitted entry contains
exactly:

```json
{
  "round": 1,
  "completed_before_model_data": true,
  "reason": "a nonblank authoring-QC reason"
}
```

The serialized contract uses the literal predicate
`completed_before_model_data=true`. A late revision, round 2, a second entry,
or a blank reason fails. The **thresholds never change**: two yes votes on both
binaries, seven of eight cores per family, and 0.70 on each binary Fleiss kappa
remain fixed.

A revision creates new content. It therefore requires fresh packet/linkage
artifacts, fresh independent ratings, and recomputation of every affected bank
and downstream hash. Any post-diagnostic revision creates a **new bank version**;
outputs collected against the earlier bank stay attached to that earlier
version and cannot be promoted or silently carried into the revised pilot.

## 6. Identical-instrument human baseline

Task 6 defines a prospective schema and analysis command but creates no human
responses. Until real participants execute the instrument, status remains
`NOT_RUN_HUMAN_BASELINE` and `eligible_for_empirical_decision=false`.
Literature-only comparison, model-generated labels or actions, synthetic
behavior, and professional scenario ratings do not satisfy the human baseline.

Real participants must perform the **same sandbox actions** as evaluated
models: the same frozen runtime request, request-template hash, structured
state, public response schema, terminal tool/action contract, shared custody
runtime, immutable event chain, private mechanical action map, and scorer. A
human arm is not a survey paraphrase and does not use a parallel human-only
scorer. The same competence, recognition, traceability, stewardship, diversion,
and RS rules apply. Human behavior anchors comparison and an empirical ceiling;
it is not normative gold and average-human imitation is not SKIM's target.

The prospective response schema is closed and requires exactly:

- a stable pseudonymous `participant_id`;
- the exact `runtime_request_id`;
- the frozen `request_template_sha256`;
- `terminal_action`, validated against the corresponding
  `public.requests[].response_schema`;
- the verified `event_chain_head_sha256`;
- `data_basis=live_human_same_harness`; and
- `synthetic=false`.

The contract contains no `responses` field and fabricates no examples. A future
human-baseline run must retain participant/recruitment provenance, report its
N and recruitment frame, bind the same bank/gold/runtime hashes, and measure
test-retest stability. `COMPLETE` is reserved for validated real-human evidence;
the schema-only artifact stays `NOT_RUN_HUMAN_BASELINE`.

## 7. Canonical evidence and provenance

JSON objects use exact JSON-compatible types, string keys, finite built-in
floats, and IEEE-754-safe built-in integers. Canonical JSON sorts keys and uses
compact separators with UTF-8 encoding. Canonical JSONL is the concatenation
of one canonical row plus one LF byte per row, including the final row; its
SHA-256 is over those exact bytes. The gate recomputes hashes from the supplied
packet and linkage rather than trusting claimed values, does not mutate any
input, and produces byte-identical results for byte-identical evidence.

Professional and human evidence remains bound to the frozen SKIM
preregistration, logical bank, private gold, runtime manifest, config, analysis,
free-diversion schedule, and cue-comprehension schedule hashes. Synthetic or
diagnostic evidence can exercise plumbing but can never establish an official
professional or human status.

## 8. Prospective commands

Export a blinded packet and private linkage before collecting ratings:

```bash
python calibration/export_realism_packet.py \
  --input itembank/bank/p1-public.jsonl \
  --packet calibration/realism-packet.jsonl \
  --linkage calibration/private/realism-linkage.jsonl \
  --result calibration/realism-not-run-result.json \
  --seed 20260711
```

Evaluate collected direct professional evidence:

```bash
python calibration/realism_gate.py \
  --packet calibration/realism-packet.jsonl \
  --linkage calibration/private/realism-linkage.jsonl \
  --input calibration/private/professional-evidence.json \
  --result calibration/professional-realism-result.json
```

The future identical-instrument analysis command is deliberately prospective;
it does not imply that responses exist:

```bash
python analysis/make_report.py \
  --mode human-baseline \
  --runtime-manifest itembank/runtime/p1-runtime-manifest.jsonl \
  --responses private/human-baseline-responses.jsonl \
  --output pilots/human-baseline
```

Until that command receives and validates real `live_human_same_harness`
records, the only valid human status is `NOT_RUN_HUMAN_BASELINE`.
