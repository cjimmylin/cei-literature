# THORNS Stage-0 on OpenRouter

This package is executable but fail-closed. It does not currently contain completed
human calibration, an authorized online receipt, or live bank results. The files under
`PANELS/` are templates and therefore fail the human and judge gates. An OpenRouter API
key is necessary, not sufficient, and the configured source scopes must be committed and
clean when online preflight and either bank phase run.

**Evidence status:** readiness only. Synthetic artifacts are harness validation, not
model evidence. No live discrimination, saturation, or model-ranking claim has been
established. A validity-clean development analysis must report
`CONFIRMATION_PENDING`; its provisional detail is not a live discrimination result.
Only a separately authored, sealed C3 run can complete confirmation.

## Frozen roster and transport

| Role | Opaque ID | OpenRouter model | Canonical contract | Pinned endpoint |
|---|---|---|---|---|
| evaluation | A01 | `openai/gpt-5.5` | `openai/gpt-5.5-20260423` | `openai` |
| evaluation | A02 | `openai/gpt-5.4` | `openai/gpt-5.4-20260305` | `openai` |
| evaluation | A03 | `openai/gpt-5.4-mini` | `openai/gpt-5.4-mini-20260317` | `openai` |
| calibration attacker | A04 | `deepseek/deepseek-v4-flash` | `deepseek/deepseek-v4-flash-20260423` | `deepseek` |
| calibration | A05 | `qwen/qwen3.7-plus` | `qwen/qwen3.7-plus-20260602` | `alibaba` |
| calibration | A06 | `meta-llama/llama-4-maverick` | `meta-llama/llama-4-maverick-17b-128e-instruct` | `deepinfra/base` |
| calibration | A07 | `mistralai/mistral-large-2512` | `mistralai/mistral-large-2512` | `mistral` |
| held out | A08 | `x-ai/grok-4.5` | `x-ai/grok-4.5-20260708` | `xai` |
| held out | A09 | `moonshotai/kimi-k2.5` | `moonshotai/kimi-k2.5-0127` | `moonshotai/int4` |
| primary judge | J01 | `cohere/command-a` | `cohere/command-a-03-2025` | `cohere` |
| primary judge | J02 | `google/gemini-3.5-flash` | `google/gemini-3.5-flash-20260519` | `google-ai-studio` |

J01 and J02 are exact, mutually vendor- and family-disjoint, non-OpenAI judge
identities. The same two identities must pass both construct and C2-control
calibration; one passing judge is never averaged with one failing judge.

Online preflight re-fetches the general catalog, key-filtered user catalog, and every
model's endpoint list. Any missing alias, canonical change, unsupported parameter,
unavailable user model, endpoint-tag change, fallback, or lineage overlap fails closed.
The fixture under `tests/fixtures/` is only an offline contract fixture and always
reports `NETWORK NOT VERIFIED`.

Subject request bodies are byte-equivalent except for `model`:
`reasoning.effort=medium`, 2,048 output tokens, `service_tier=default`, no streaming,
no storage, a single pinned `openai` endpoint, parameter enforcement, and no fallback.
Auxiliary-model reasoning is explicit per model; `null` means the request omits effort
because that exact catalog contract does not expose a selectable effort.

Judge Layer-E, Layer-R, and Layer-control outputs use the Responses structured-output
transport with a strict JSON Schema (`text.format.type=json_schema`, `strict=true`, and
closed object schemas). This is an API transport constraint, not merely an instruction
to “return JSON”; the returned text is also parsed and validated locally against exact
keys, closed labels, probability totals, rule IDs, and evidence-span requirements.

## Development lock and independent confirmation

`ITEMS/thorns/CUE-DEVELOPMENT-LOCK-20260709.json` freezes every runnable C0/C1/C2
surface and private cue contract before any live development result. Its
`live_result_inputs` list is empty. Development schedules six complete blocks so that
each subject/item pair rotates twice through the three cue positions; a five-block run
is not comparable and cannot balance C0/C1/C2.

The six runnable C3 files live separately under `ITEMS/thorns/c3_candidates/`. Their
provenance records a separate author, authorship after the development lock, and no
observation of live results. They are sealed construct surfaces and cannot compile in
development. Locked confirmation rejects a reused development surface ID or schedule
hash. Do not revise or regenerate C3 after opening development outcomes; doing so would
destroy the held-out confirmation claim.

## Human-bound calibration inputs

Complete the packet at `PANELS/thorns-human-calibration-packet-v1.md` before online
preflight. Construct and null-control calibration are separate decision spaces and need
separate raw evidence and validation artifacts:

| Decision space | Human labels | Judge predictions | Validation | Allowed final labels |
|---|---|---|---|---|
| construct | `thorns-human-calibration-labels.template.csv` | `thorns-judge-calibration-predictions.template.json` | `thorns-judge-validation.template.json` (`design: thorns`) | `Fi`, `Wj`, `CFT`, `mixed`, `other` |
| C2 null control | `thorns-control-human-calibration-labels.template.csv` | `thorns-control-judge-calibration-predictions.template.json` | `thorns-control-judge-validation.template.json` (`design: thorns-control`) | `foil_correct`, `target_action_false_positive`, `indeterminate` |

For each template, make a completed, immutable working copy and update the corresponding
`paths.*` entry in `pilot_config.openrouter.json`. Also complete the construct and
control panel registries, qualification-set hash, and availability declarations. Both
registries must bind the same qualified panel and member list. Set
`FRUITBENCH_RATER_SALT` to a protected non-blank value for intake; the salt and the
restricted direct-ID map are not run artifacts.

The human source files remain raw row-level CSVs with exactly
`response_id,rater_id,role,final_label,notes`. Each response needs exactly two independent
primary rows; a disagreement needs exactly one independent adjudicator row. The judge
prediction files retain one raw row for every response/judge pair with the exact judge
identity, final label, complete class-probability vector, and `judge_refused` flag.
Coverage must be complete for both J01 and J02 and include every class in its own
decision space.

Do not type summary metrics into a validation artifact from a spreadsheet report and
treat them as evidence. During preflight the harness ingests and salts the raw human
rows, recomputes human agreement/kappa and every judge agreement, F1, AUPRC,
worst-class F1, sample count, and refusal rate from the raw prediction matrix, and
requires the reported validation metrics and calibration-evidence hash to match exactly.
Both decision spaces require at least 48 calibration responses per judge. Prompt, label,
policy, source-file, panel, and catalog identities are hash-bound.

Path quality and item rubric score are deliberately different fields. Construct
`quality` is the frozen path ordering (`Wj=0`, `CFT=0.5`, `other=1`, `mixed=2`, `Fi=4`)
and follows the selected class. `rubric_score` is a separate item-specific Q0–Q4 score
for how completely that response satisfies the item rubric; it may differ from path
quality. C2 controls use neither construct path quality nor an item rubric score.

## External gates and readiness sequence

The online receipt authorizes bank calls only when all eight gates pass together:
`key`, `catalog`, `d36_bank`, `cue_registry`, `output_immutability`, `source_freeze`,
`judge_validation`, and `human_availability`. In particular:

- the completed construct and C2-control human/prediction/validation artifacts must
  pass recomputation and bind the same qualified, currently available panel;
- `OPENROUTER_API_KEY` must authenticate the Models API and expose every frozen model;
- every configured source scope must be in a committed, clean Git state; and
- the receipt must remain under its 72-hour age limit and match the exact current
  config, source, calibration, catalog, and cue hashes.

An offline receipt is useful for diagnosis but never authorizes bank calls.

### 1. Offline readiness check

From the repository root:

```bash
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/preflight.py \
  --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json \
  --offline-catalog COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests/fixtures/openrouter-models.json
```

This performs no network request. It writes an immutable receipt for audit with
`authorized_for_bank: false`, even when every locally testable check passes.

### 2. Optional non-bank smoke

```bash
export OPENROUTER_API_KEY='...'
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/run_pilot.py \
  --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json \
  --smoke-openrouter \
  --date YYYYMMDDs
```

Smoke sends one fixed neutral prompt asking for `SMOKE_OK`. It has no item ID, bank
text, gold, construct label, canary, or scorer. Its immutable artifact is marked
`evidence_class: smoke` and `scoreable: false`; it cannot become benchmark evidence.

### 3. Online Models-only preflight

Run only after the human-bound inputs are complete and the configured source scopes are
committed and clean:

```bash
export OPENROUTER_API_KEY='...'
export FRUITBENCH_RATER_SALT='...'
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/preflight.py \
  --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json \
  --online
```

Online preflight performs authenticated GETs to the Models API only. It never calls the
Responses endpoint. It prints and writes the receipt path. A bank phase accepts only
that immutable receipt, with the exact current hashes and all eight gates `PASS`.

## Cost and call-count warning

The current schedule/compiler expands to **2,502 development jobs** (1,728 calibration,
558 evaluation, and 216 held-out) across 19 distinct item IDs: the frozen 18-item
diagnostic plus one registered cue-panel item. It also expands to **108
locked-confirmation jobs**. Development has
2,394 construct jobs and 108 C2 null-control jobs; confirmation has 108 sealed C3
construct jobs. Every current job is single-shot and makes one actor Responses call plus
two judge families × two scoring layers, or approximately **five logical Responses calls
per job**:

- development: about **12,510 logical calls**;
- locked confirmation: about **540 logical calls**;
- both phases: about **13,050 logical calls**, before transport retries.

At the configured ceilings this is up to roughly 15.37 million development output tokens
and 0.66 million confirmation output tokens, plus input and reasoning tokens. Layer-E
task/trajectory context and the strict judge schema also make input volume material.
These are ceilings, not a dollar quote. Actual spend depends on response lengths and the
current price of every pinned endpoint; re-check provider pricing and set an external
OpenRouter/account-side budget before the online receipt. The harness has no spend cap or
compile-only cost prompt. A retry can add transport attempts. Successful calls retain
their transport attempt ledger; a failed call's journal event retains only its call ID,
error type, and hashed message, not the failed transport attempt ledger.

Jobs and judges execute serially rather than in batches. The receipt age is checked when
a phase starts or resumes, not during an uninterrupted phase. Because the schedule and
journal identity bind the original receipt, an interruption cannot be resumed after that
receipt's 72-hour limit by substituting a fresh receipt. Plan the run window accordingly.

## Development phase

Use a fresh date token:

```bash
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/run_pilot.py \
  --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json \
  --phase development \
  --preflight-receipt /absolute/path/to/ONLINE-RECEIPT.json \
  --date YYYYMMDDd
```

The receipt is validated before the schedule or any item call. The immutable C0/C1/C2
schedule is created before execution; C3 cannot compile. Development covers the frozen
18-item diagnostic plus the registered cue panel and is not a headline model comparison.
If all validity latches pass, its analysis verdict is `CONFIRMATION_PENDING`. The
`PROVISIONAL_*_AWAITING_SEALED_C3` detail is diagnostic only and must not be reported as
live discrimination, non-discrimination, or saturation. An `INVALID` development verdict
also cannot advance an empirical claim.

To resume an interrupted development run, use the exact same date, config, receipt, and
phase and add `--resume-live`:

```bash
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/run_pilot.py \
  --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json \
  --phase development \
  --preflight-receipt /absolute/path/to/ONLINE-RECEIPT.json \
  --date YYYYMMDDd \
  --resume-live
```

## Locked confirmation

Use a new date token. Pass every development schedule whose surface IDs and hashes must
be excluded, and pass the completed development terminal-row artifact explicitly:

```bash
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/run_pilot.py \
  --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json \
  --phase locked-confirmation \
  --preflight-receipt /absolute/path/to/ONLINE-RECEIPT.json \
  --development-schedule /absolute/path/to/YYYYMMDDd-live-development-cue-schedule.json \
  --development-results /absolute/path/to/YYYYMMDDd-live-development-terminal-rows.json \
  --date YYYYMMDDc
```

`--development-results` is accepted only when the artifact identifies the development
phase and its SHA-256 is bound by a validated, completed development journal. Only sealed
C3 surfaces compile in confirmation; development rows are combined with C3 rows for the
preregistered final analysis.

Supply the schedule and terminal artifact from the same development run. Before it
validates or compiles confirmation, the CLI hashes every supplied
`--development-schedule` file and requires at least one hash to equal the schedule hash
bound by the completed development terminal artifact's journal identity.

To resume confirmation, repeat every argument exactly, keep the confirmation date token,
and add `--resume-live`:

```bash
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/run_pilot.py \
  --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json \
  --phase locked-confirmation \
  --preflight-receipt /absolute/path/to/ONLINE-RECEIPT.json \
  --development-schedule /absolute/path/to/YYYYMMDDd-live-development-cue-schedule.json \
  --development-results /absolute/path/to/YYYYMMDDd-live-development-terminal-rows.json \
  --date YYYYMMDDc \
  --resume-live
```

## Journal, resume, and outputs

For phase `<phase>` and token `<date>`, the runner creates these immutable paths under
`PILOTS/thorns/`:

- `<date>-live-<phase>-cue-schedule.json`;
- `<date>-live-<phase>-evidence.jsonl`;
- `<date>-live-<phase>-actor-turns.json`;
- `<date>-live-<phase>-terminal-rows.json`;
- `<date>-live-<phase>-analysis.json`; and
- `<date>-live-<phase>-run-manifest.json`.

The append-only journal hash-chains canonical events and records a secret-scanned request event
before each actor or judge call, then its result or error, raw trajectory evidence, raw
judge ballots, score resolution, analysis, output hashes, and completion. Secrets are
rejected from journal payloads. The four aggregate output paths are reserved before the
first call and populated only after every planned job has a durable score boundary. The
journal and four aggregate outputs are created with owner-only permissions, but they
contain full bank prompts, private rules/markers, responses, and ballots; treat them as
restricted benchmark evidence, not share-safe logs.

`--resume-live` validates the existing schedule, journal chain, path reservations, and
run identity, then skips only fully scored jobs. Resume is refused if a request lacks a
durable result/error event or if any job stopped between `job_start` and `score_result`,
because replay would risk a duplicate paid actor or judge call. A completed journal
cannot be resumed. Without `--resume-live`, an existing schedule, journal, or output path
fails exclusive creation; use a new date token only for a genuinely new run.

Judge disagreement is never averaged into a headline label. The journal retains both raw
ballots. The current live CLI does not pass human adjudication into scoring and has no
post-run adjudication/reanalysis command; construct or C2 disagreement therefore leaves
the headline label unset and makes the analysis `INVALID`. Human availability remains a
preflight requirement, but it is not an implemented in-run resolution path. Do not rerun
responses merely to fish for judge agreement.

## Failure semantics

- A failed or `NOT_VERIFIED` gate means zero bank calls.
- A missing/dirty source freeze, changed config, changed schedule, stale receipt, or
  reused filename means zero bank calls.
- A provider fallback, non-direct route, transformed pipeline, snapshot substitution,
  service-tier mismatch, missing router metadata, or incomplete response is invalid
  evidence and raises.
- Live routing is response-independent and counterbalanced; response-content marker
  routing and `MarkerScorer` are synthetic-only.
- C2 is a null-control decision space. It must never be forced through construct labels,
  path quality, or an item rubric score.

## Verification

```bash
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests/test_preflight.py -q
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests \
  COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests -q
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/audit_bank.py \
  --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/audit_config.json
```
