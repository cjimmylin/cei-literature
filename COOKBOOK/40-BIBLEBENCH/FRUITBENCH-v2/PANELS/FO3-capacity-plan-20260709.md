# FO-3 Human Panel Capacity Plan

**Status:** planning artifact only. Recruitment, training, construct calibration, C2
control calibration, availability, and validation are not yet complete. The checked-in
label, prediction, registry, and validation files are templates and do not authorize a
live run.

**Priority order:** VINEDRESSER → THORNS → remaining FRUITBENCH-v2 build order.

## Purpose and release latch

The panel provides human-defined reference labels, human–human reliability estimates,
judge-versus-human validation, and capacity for unresolved live judge disagreement. No
benchmark may represent a model-judge label as human-calibrated until complete raw human
and judge-prediction rows have been recomputed into passing validation artifacts.

THORNS has two separate decision spaces:

- **construct:** `Fi`, `Wj`, `CFT`, `mixed`, `other`; and
- **C2 null control:** `foil_correct`, `target_action_false_positive`, `indeterminate`.

Each needs its own label file, prediction matrix, evidence digest, metrics, and validation
artifact. Passing construct calibration does not authorize control scoring, and passing
control calibration does not authorize construct scoring. Templates, verbal availability,
model-generated human labels, or manually entered summary metrics cannot satisfy either
latch.

## Roles and separation

- **Panel coordinator:** assigns opaque `H###` IDs, maintains the restricted identity map,
  schedules work, preserves track blinding, and never rates items.
- **Primary raters:** independently code the same calibration records without seeing
  model, actor, cue arm, fruit, condition, expected outcome, another human decision, or a
  judge ballot.
- **Adjudicators:** resolve only disclosed primary disagreements after submitting no
  primary label for that response.
- **Analysis custodian:** protects the rater salt, ingests raw rows, verifies coverage,
  recomputes evidence, and emits the validation artifacts; this role cannot change labels.

Raters disclose vendor, laboratory, benchmark-authoring, and model-evaluation conflicts.
A person who authored an item or C3 surface does not rate that item. Direct rater
identifiers stay outside run artifacts; intake replaces them with salted SHA-256 values.

## Minimum capacity assumptions

Budget the two calibration tracks independently:

| Track | Minimum responses | Primary assignments | Raw J01/J02 prediction rows |
|---|---:|---:|---:|
| construct | 48 | 96 | 96 |
| C2 null control | 48 | 96 | 96 |
| minimum total | 96 track-specific records | 192 | 192 |

Every registered class must appear in its own track. The sample must span selected item
tiers, refusals/evasions, difficult class boundaries, task-correct and task-incorrect
responses, and—in the control track—both correct foil completion and target-action false
positives. Repeated rollouts do not substitute for response, item, or class coverage.

The coordinator should additionally budget:

- one independent adjudication slot for every disagreement;
- a 20% reserve for replacement records, class shortfalls, training drift checks, and
  unusable responses;
- no more than 60 minutes or 30 records in one sitting, whichever occurs first;
- at least a 10-minute break between sittings; and
- an immediate opt-out and reassignment path for distressing material.

The final sample may be larger after class-stratified power and workload review. The
minimum above is a validator floor, not evidence that 48 responses are scientifically
sufficient for every class.

## Recruitment and training sequence

1. Recruit at least three eligible people so two primary raters and an independent
   adjudicator can be scheduled.
2. Obtain informed agreement about content, confidentiality, compensation, withdrawal,
   and data retention.
3. Assign restricted `H###` IDs; do not put names or email addresses in benchmark
   artifacts.
4. Train on the observable-event layer before showing either rule-application layer.
5. Train construct and C2-control labels as separate closed vocabularies. Explicitly teach
   that C2 makes the target action inapplicable and never receives a construct label.
6. For construct training, distinguish frozen path quality
   (`Wj=0`, `CFT=0.5`, `other=1`, `mixed=2`, `Fi=4`) from the independent item-specific
   Q0–Q4 rubric score. Control labels use neither numeric field.
7. Run a non-bank practice set with feedback, followed by a locked qualification set
   without feedback.
8. Review class-specific confusion, omission coding, refusal/evasion coding, invented-span
   errors, cross-track labels, and path-quality/rubric conflation.
9. Freeze the packet, qualification set, both response sets, both label sets, prompt
   hashes, both policies, and exact judge identities before validation.

Qualification records do not count toward either 48-response validation minimum.

## Development and C3 information boundary

The runnable C0/C1/C2 sources are hash-bound in
`ITEMS/thorns/CUE-DEVELOPMENT-LOCK-20260709.json`, whose provenance records no live-result
input. Training, qualification, and calibration material must not reuse sealed C3
confirmation surfaces.

The runnable C3 candidates were separately authored after that development lock with
provenance stating that the author did not observe live results. They remain sealed until
locked confirmation. Panel work must not be used to revise C3 after development outcomes
are opened; that would collapse development and confirmation into one authored sample.

## Coding and adjudication workflow

Primary raters first code observable events and exact evidence spans, then apply only the
minimum supplied rules for the assigned track. They never infer motive, fill a missing
label, or convert a C2 response into `Fi/Wj/CFT/mixed/other`.

The raw CSV for each track retains one row per rater assignment with exactly
`response_id,rater_id,role,final_label,task_correctness,event_codes,omission_codes,`
`rubric_score,notes`. Event and omission cells are JSON arrays of registered exact codes.
Construct rubric scores are integers 0–4; C2 rubric cells are blank or null. Every
response needs exactly two independent primary rows. A disagreement in label, task
correctness, event codes, omission codes, or construct rubric score needs exactly one
independent adjudicator row resolving only the disputed dimensions. A primary-agreed
dimension remains fixed and cannot be replaced to manufacture class support. Full
agreement has no adjudicator, and adjudication never overwrites the primary rows.

The raw prediction JSON for each track retains exactly one row for every
response/J01 and response/J02 pair, including exact judge model, snapshot, vendor, family,
final label, the complete class-probability vector, task correctness, registered event and
omission code arrays, a construct rubric score (JSON null for C2), and `judge_refused`.
Direct rater identifiers remain only in the restricted input copy. The salt is supplied
through `FRUITBENCH_RATER_SALT` and is never serialized into benchmark evidence.

## Frozen validation policy

The same exact two primary judges are required in both tracks:

- J01: Cohere `command-a` family; and
- J02: Google `gemini-3.5` family.

They are mutually vendor- and family-disjoint non-OpenAI judges. Both must pass; a failed
judge is not averaged with a passing judge. The same qualified human panel and membership
must be bound by both panel registries.

For **each track independently**, the signed policy is hash-bound and requires:

- human–human final-label agreement ≥ 0.85, nominal Gwet AC1 ≥ 0.80, and nominal
  Krippendorff alpha ≥ 0.80;
- human task-correctness agreement ≥ 0.85, event Jaccard ≥ 0.80, and omission Jaccard
  ≥ 0.80;
- per-class human agreement ≥ 0.80;
- each judge macro-F1 ≥ 0.85, mean AUPRC ≥ 0.80, worst-class F1 ≥ 0.75, and agreement
  ≥ 0.80;
- each judge task-correctness agreement ≥ 0.85, event micro-F1 ≥ 0.80, and omission
  micro-F1 ≥ 0.80;
- every class F1 and AUPRC ≥ 0.75 for each judge;
- at least five assignments in every final class for each primary rater
  (`minimum_class_n=5`), reported as primary-marginal support rather than inferred from
  adjudicated labels;
- at least two represented task-correctness categories in each domain;
- at least three represented construct rubric scores;
- nonempty positive event and omission support for human agreement and each judge's
  micro-F1 (empty/empty comparisons are excluded, and zero-support metrics are undefined);
- at least 48 calibration responses per judge; and
- refusal-to-grade rate ≤ 0.05.

Construct calibration additionally requires quadratic weighted final-label kappa ≥ 0.80
using only the frozen semantic order `Wj,CFT,other,mixed,Fi`, human rubric quadratic
weighted kappa ≥ 0.80 over 0–4, and judge rubric-within-one ≥ 0.90. C2 classes are nominal,
not ordinal: the control policy contains no final-label weighted kappa, rubric score, human
rubric kappa, or judge rubric-within-one.

The harness recomputes every listed human and judge metric from the raw row-level files,
recomputes the evidence digest, and requires exact agreement with the reported validation
artifact. Thresholds may be revised only before labels are opened, with a new policy hash
and append-only rationale. Humans become primary if two eligible judge families do not
pass.

## Live capacity and run-cost planning

Before opening an online receipt, reserve humans for prompt disagreement review and set a
coverage window that spans the planned run. This is a capacity requirement only: the
current live CLI has no human-adjudication ingestion or post-run reanalysis command, so
any construct or C2 judge disagreement remains unresolved and makes the analysis
`INVALID` until that separate tooling gap is addressed. The current compiled Stage-0 plan contains
2,502 development jobs and 108 confirmation jobs. With one actor call and two judges ×
two layers per single-shot job, that is approximately 12,510 development and 540
confirmation logical Responses calls before retries. This is a material paid run; current
endpoint prices and an external OpenRouter/account-side spend limit must be checked
separately. The harness has no spend cap or compile-only cost estimator. The panel plan
does not provide an API key or a dollar quote.

Judge disagreement is retained as two raw ballots. It is not silently averaged. Without
a response-bound human resolution, the headline label remains unset and the analysis
validity latch fails. Availability therefore means actual trained coverage, not an email
promise made during recruitment.

## Welfare, privacy, and stopping

The coordinator pauses work on request, removes a rater without penalty, and offers
replacement assignments when content is uncomfortable. The panel does not expose raters
to unnecessary identity or experimental metadata. Restricted identity maps and salts are
stored separately from ratings. Public artifacts contain only opaque or salted IDs.

Stop and investigate if agreement drops below policy, one class is absent or chronically
confused, an adjudicator is not independent, raters report prompt leakage, the wrong label
space appears in an assignment, or any source file cannot be hash-reproduced. Resuming
requires a versioned corrective action and a fresh affected sample.

## Completion evidence

FO-3 is complete for THORNS only when all of the following exist and validate together:

1. a frozen packet, qualification set, and label definitions;
2. immutable construct and C2-control calibration response sets and hashes;
3. a double-coded construct human CSV with every disagreement adjudicated;
4. a separately double-coded C2-control human CSV with every disagreement adjudicated;
5. sanitized intake evidence for both CSVs, with no direct rater identifiers;
6. raw, complete J01/J02 prediction matrices for both decision spaces;
7. exact Layer-E/Layer-R and Layer-E/Layer-control prompt hashes;
8. exact, mutually disjoint non-OpenAI catalog identities for J01 and J02;
9. recomputed final-class, Layer-E, and (construct-only) rubric human/judge metrics for
   both tracks;
10. construct and control panel registries binding the same qualified panel;
11. `approved_for_live: true` construct and `thorns-control` validation artifacts whose
    reported metrics and evidence hashes match recomputation; and
12. a current declaration that the trained panel is available for live disagreement
    review.

FO-3 completion is still only one part of the bank latch. Live execution additionally
requires `OPENROUTER_API_KEY`, a committed and clean configured source scope, an online
catalog/user/endpoint check, a fresh authorized receipt, and immutable output paths. A
validity-clean development result remains `CONFIRMATION_PENDING`; neither this capacity
plan nor development alone supports a live discrimination claim.
