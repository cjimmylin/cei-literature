# CROSSROADS bank

CROSSROADS measures a native C1–C16 values profile through enacted forced
paths. The primary response is the action that actually commits in the
workspace, not a letter, option ID, or stated preference. Direct hidden-key
choice scores are primary under D-18. Follow-through quality is reported as a
separate E(C1–C16) vector; no overall scalar is emitted.

## Frozen construction

- A duplicated affine-plane 2-(16,4,2) design supplies only the hidden C1–C16
  clause assignment: every clause occurs in 10 structures and every pair in 2.
- A seeded 10-domain × 4-incident scenario grammar supplies 40 substantively
  distinct causal skeletons beneath that clause layer. Every skeleton has its
  own scenario/template family, roles, artifact, incident, evidence state,
  deadline, baseline duty, four evidence-bound claims, four stable action
  plans, and reaction signature.
- 600 private episodes: 40 structures × 3 private skins × 5 parameter states.
- 30 public episodes using disjoint public skins and held-out parameter
  realizations.
- 630 accepted episodes plus 40 rejected full candidate snapshots retained in
  the hardness log. A1, competing claims, path/inaction costs, and the
  no-universal-satisfaction gate are derived from executable schemas, branch
  evidence, and actual keys; no rubric result is hardcoded.
- 60 stated-pair items are protocol-only and never enter primary scoring.

Every stored item retains exactly `multiturn_script.stage_1..stage_4`. Each
stage is a nonempty list of public turns, the complete episode contains 8–20
turns, and stage 3 contains 3–8 follow-through turns. At the fork the runtime
exposes exactly three or four executable affordances. Each affordance is the
real tool signature `{tool, target, operation, arguments, description}`; there
are no answer letters or path IDs.

Each stable action emits neutral operational states without receiving a sign or
failure pole. A parameter cell separately exposes its evidence-required states;
the sidecar derives `+1` only when the action state equals the required state.
The same visible action phrase therefore receives both signs across causal
parameter flips. Clause-specific mismatch direction determines the private
sentimental/harsh class, with identical mismatches sharing one class and exact
50/50 unique balance per clause. Current generated totals span four distinct
turn counts (9–12), three private tool substrates, and one held-out public
substrate: 12 private and 4 public fork-tool names. Each tool, operation, and
target kind is locked to one stable causal action role. The fifth private
requirement mask and affordance order are phased by affine-line band so those
coherent action cues remain counterbalanced rather than being semantically
rotated across incompatible plans. The 30 public items use a frozen generated
schedule of distinct structure×requirement cells: every clause appears in at
least seven items, the largest public clause×action-cell sign association is
`0.142857`, and the standalone public surface association is `0.074152`.

Candidate action prose uses grammatical short/long receipt instructions. It
does not use repeated neutral tokens or trailing whitespace to manufacture
length and specificity differences. Later-stage targets are opaque receipt
hashes, and no `path-N`, numbered plan, route, or option crosses a candidate
surface.

`generator.py --seed TEXT` deterministically permutes the generated scenarios
over the frozen clause blocks. The dry output and generation manifest bind the
scenario assignment plus complete public/private future-visible surfaces with
SHA-256 hashes, making same-seed determinism and different-seed novelty
auditable without storing a second fixed bank.

## Trust boundaries

The candidate payload contains only grouped public turns, tool schemas,
executable affordances, and consequences already visible in the simulated
world. Bank IDs, canaries, clause signs, hidden path keys, parameter states,
reaction/branch tables, and expected behavior are rejected recursively.

Public files document the tool and simulant interfaces. Private
`sidecar/ground_truth.json` owns path keys, structure/skin/parameter state,
fork windows, classifier signatures, and simulant decision logic.
`sidecar/judge_token_map.json` is a private authoring map of deterministic
`JSEED-<UUIDv4>` issuance seeds to items. A JSEED is never a judge case, never
appears in a judge payload, and cannot be accepted where a JCASE is required.

At future full scale, `lib/judge_cases.py` creates a fresh random
`JCASE-<UUIDv4>` for every exact `(run, execution, candidate snapshot, item,
response hash, scoring occurrence)` tuple. The private run directory stores a
mode-0600, append-only, hash-chained crosswalk; an exact occurrence cannot be
issued twice, and repeated item/model responses or reruns receive unrelated
tokens. `lib/payloads.py` recomputes the observable response hash before it
sends only the JCASE, transcript, and observable artifacts to a judge.

Persistent `JUDGE-<UUIDv4>` identities are resolved exclusively through a
canonical-hash-frozen roster. Every roster row binds family, provider, exact
model/version or human identity class, prompt hash, configuration hash, and
role. Rating records do not supply family authority. Two raw ratings must
resolve to distinct non-candidate families, and adjudication must resolve to a
separate identity and third family with the adjudicator role. The shipped roster JSON Schema
and `sidecar/judge_roster.mock.json` are labelled exactly **harness validation,
NOT a measurement**; an actual model/human roster is an external dependency
and has not been performed.

Canaries use item-bound `10CB3-01-<UUIDv4>` markers. They occur in episode
metadata, the hidden mirror, and the append-only global
`../canary_registry.txt`, never in a candidate or judge payload.

## Layout

```text
01-crossroads/
├── deep_structures.yaml
├── generator.py
├── lib/                         # public payload and split contracts
├── scorers/                     # path, evasion, follow-through scoring
├── analysis/                    # direct profiles and exploratory recovery
├── adversarial/                 # six static policies and cue audit
├── episodes/private.yaml        # sealed measurement episodes
├── seeds_public.yaml            # 30 key-redacted public episodes
├── sidecar/                     # keys, private simulants, judges, hardness
├── export/                      # ten-field table and frozen A3/A4 contracts
├── megamatrix/calibration_notes.md
├── pilot/                       # cheap-only public qualification runner
└── tests/
```

The build reports include:

- `reports/split_hygiene.json`: every stage, tool value, fork affordance,
  consequence, public branch state, reaction turn, repair action, and closeout
  action across all 18,000 public×private pairs; threshold `<0.25`.
- `reports/sign_leak_probe.json`: forbidden construct-language scan, exact
  phrase lookup, supported-token purity, and leave-one-template-family-out
  lexical decoder.
- `reports/cue_counterbalance.json`: per-clause warmth, effort, specificity,
  length, tool, and ordinal cells plus coherent action-role/tool/operation/
  target-kind association. Raw imbalance is capped at 2 and normalized
  coherent-action association at `0.10`.
- `reports/public_cue_counterbalance.json`: all public clause×action-role,
  tool, operation, target-kind, and ordinal cells plus the standalone
  adversarial surface statistic.
- `reports/generation_manifest.json`: counts, information/cue gates, generation
  seed hash, scenario-assignment hash, and visible-surface hashes.

Default-seed verification checkpoint (2026-07-11): scenario assignment
`116b52f9ebbc34f8a133ba651a8d2d636a83a4aa220b27485f235dd658efef23`;
private future-visible surface
`b72f5f68b1f60864d03520d6ca9afd2bda2931a9a5c34de3face08a672c02e84`;
public future-visible surface
`f600895e32b37cf60ebe1830e299723c8fec75598e0f0234b1d4ac0a16064f7e`.
The full-surface split maximum is `0.14324324324324325` across 18,000
comparisons with zero violations. The normalized exact-phrase majority decoder
is `0.5675` with zero pure-sign phrases, and inversion-robust
leave-one-family-out lexical predictability is `0.5`. The raw cue imbalance is
2, the maximum normalized coherent-action association is `0.04`, and the
pooled standalone surface association is `0.071429` against a `0.10` ceiling.

## Offline verification

```sh
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY -m pytest tests/ -q
$PY generator.py --dry
$PY adversarial/run_adversarial.py
$PY export/export_megamatrix.py
$PY selfcheck.py
```

## Cheap-only OpenRouter qualification

**Review gate:** [`../../../CORINTHLOVE-REVIEWS/20260711-crossroads-bank-rereview.md`](../../../CORINTHLOVE-REVIEWS/20260711-crossroads-bank-rereview.md)
is the superseding **GO — cheap public qualification only**. It supersedes the
earlier pre-redesign FAIL; it does not authorize private execution, canonical
E, live judges, calibration, model ranking, or freeze.

The bank-specific runner is public-only and accepts exactly the four aliases in
`pilot/cheap_profile.json`: GPT-5 nano, GPT-5.4 nano, GPT-5 mini, and GPT-5.4
mini. Profile v6 pins the lowercase OpenRouter routing slug `azure`, forbids
fallbacks, and independently attests the display provider `Azure`. Before any
paid POST it intersects the current per-model endpoint list with OpenRouter's
dedicated ZDR endpoint list on exact model/provider/tag/snapshot identity. Every
intersected route must have exact integer status code 0, sufficient context and
capabilities, and prices within the frozen ceilings. Legitimate base/regional
duplicates are retained and checked individually; no absent per-model `zdr`
field is promoted to evidence. Every request still enforces `zdr: true` and
`data_collection: deny`. Every paid call requests official router metadata and
preserves the full ChatResult plus the allowlisted `X-Generation-Id` header.
Attestation requires exact body/header ID equality, top-level Azure and frozen
snapshot, direct attempt 1, exactly one selected Azure/frozen-snapshot router
row, complete usage, and cost within the frozen reconstruction. It does not
depend on the delayed `/generation` lookup. The transport retries no paid POST;
the orchestration ceiling is three immutable attempts.

The API key is read only from `OPENROUTER_API_KEY` in the process environment.
It is never accepted as an argument or written to evidence. Run the path-only
staged qualification from this bank root with a new output directory:

```sh
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
set -a
source ~/.codex/secrets/openrouter.env
set +a
OUT=pilot/runs/20260711-openrouter-cheap-azure-v6-live-v1

$PY pilot/cli.py create --root "$OUT"
$PY pilot/cli.py access --root "$OUT"
$PY pilot/cli.py canary --root "$OUT"
$PY pilot/cli.py smoke --root "$OUT"
$PY pilot/cli.py verify --root "$OUT" --phase report
```

The frozen runtime contract checks every profile field, exact snapshot, route,
and price ceiling. Run manifests bind the pilot contracts, OpenRouter
transport, runner, executor, payload contract, and both scorers; a change to
any bound component requires a new root. Each response cost is reconstructed from prompt and
completion tokens; reasoning tokens must be a subset of completion tokens and
are charged once at the output ceiling. A failed paid attempt stops the command.
Creation validates and hashes every public item's complete fork, repair, and
closeout schema before it writes a run root or permits an access probe.
Fork, repair, and closeout calls each reserve 4,096 completion tokens. OpenRouter
counts reasoning inside this ceiling; the uniform budget prevents reasoning from
consuming the action envelope at any stage.
The transport rejects missing, unknown, length, and content-filter finish
reasons. `stop` is valid only with zero tool calls, while `tool_calls` requires
at least one complete valid action and no incomplete call evidence, so a
truncated response becomes a durable failed attempt rather than evasion.
After inspecting its immutable failure artifact, authorize exactly one further
attempt in a new invocation with `--retry-failed`, for example
`pilot/cli.py canary --root "$OUT" --retry-failed`. Three attempts remain the
hard ceiling; one invocation never consumes multiple retries.

The first v1 live access attempt is preserved under
`pilot/runs/20260711-openrouter-cheap-azure-v1-live-v1`. It failed during the
free catalog preflight, before a benchmark case or paid completion, because the
current OpenRouter schema uses numeric status codes, omits per-model `zdr`, and
may list multiple Azure regions. That root must never be retried or rewritten.

The superseded v2 root is also preserved under
`pilot/runs/20260711-openrouter-cheap-azure-v2-live-v1`. Its catalog gate
passed, but its first nano access response was discarded when the separate
generation-metadata lookup remained unavailable until the 90-second timeout.
No benchmark episode ran. Two subsequent nano protocol diagnostics—explicitly
**protocol diagnostic, NOT a benchmark measurement**—showed that the 32-token
medium-reasoning access budget truncates without usage, while 512 tokens yields
`stop`, exact body/header ID, exact Azure/snapshot in both response and router
metadata, and complete token/cost evidence. Profile v3 therefore uses a
512-token access budget and direct response attestation. Neither diagnostic is
accepted as qualification evidence.

The v3 root is preserved under
`pilot/runs/20260711-openrouter-cheap-azure-v3-live-v1`. All four access arms
succeeded and verify offline, but the first canary fork stopped on HTTP 404
before output. The exact Azure catalog does not declare
`parallel_tool_calls`; with `require_parameters: true`, sending that optional
field correctly left no eligible provider. The harness already classifies
multiple distinct complete actions as ambiguous and rejects incomplete tool
evidence,
so profile v4 removes only this unnecessary, unsupported request field and
asserts that every transmitted model parameter is catalog-declared. The v3
root is not retried or reused.

The v4 root is preserved under
`pilot/runs/20260711-openrouter-cheap-azure-v4-live-v1`. Its four access arms
succeeded and verify, but its first fork stopped on HTTP 400 before output.
Two nano schema diagnostics—**protocol diagnostic, NOT a benchmark
measurement**—isolated the cause: the exact top-level `oneOf` action schema is
accepted by Azure in ordinary function-calling mode but rejected under
provider-side `strict: true`. Profile v5 sets only the provider strict flag to
false and removes redundant staged JSON-message formatting. The local harness
remains authoritative and stricter: exact fields, complete JSON, exact action
signature, finish/cardinality agreement, and rejection of every incomplete or
unmatched call. Access remains 512 tokens and fork/follow/close remain
2048/1024/1024. The v4 root is not retried or reused.

The v5 root is preserved under
`pilot/runs/20260711-openrouter-cheap-azure-v5-live-v1`. All four access arms
succeeded and verify offline. Its first nano canary fork then failed closed with
an incomplete/unknown normalized finish. Two follow-up calls, explicitly
**protocol diagnostic, NOT a benchmark measurement**, reproduced the budget
boundary: the unchanged 2,048-token fork consumed all 2,048 completion tokens
(1,600 reasoning) and exposed native `max_output_tokens`; the same medium-
reasoning request at 4,096 completed a valid action, and a full three-stage
4,096 diagnostic completed at 2,592/1,322/600 tokens. Profile v6 therefore uses
4,096 at every staged call and preserves each rejected request/response plus any
completed paid stage prefix for offline semantic replay. Replay reconstructs
the exact fork/follow/close request from canonical episode, truth, selected
branch, model, binding, and attempt; a self-consistent rehash cannot substitute
messages, tools, branch material, or prior observable state. Paid access
rejections likewise preserve and canonically replay their request, catalog gate,
and returned response (or explicit absent response on transport failure). Its durable finish
error also records normalized finish, native finish, total completion tokens,
and reasoning tokens. This changes no prompt, public action inventory, item,
key, scorer, clause, provider route, or model. The v5 root is not retried or
reused.

No v6 failed episode may omit its bound envelope. A staged transport failure
retains the canonical stage request and explicitly records `raw_call: null`;
post-return validation retains the raw call regardless of the concrete Python
exception class. The same catch-all post-return rule applies to access
attestation, including numeric overflow or recursive malformed evidence.
Unbound pre-request failures are not committed as durable attempts.

Use repeated `--model` arguments on `create` to select a cheaper subset while
retaining the frozen allowlist. A fork-only diagnostic requires a separate
create-only root:

```sh
DIAG=pilot/runs/20260711-crossroads-fork-diagnostic-v1
$PY pilot/cli.py create --root "$DIAG" \
  --execution-mode "fork-only diagnostic" --model openai/gpt-5-nano
$PY pilot/cli.py access --root "$DIAG"
$PY pilot/cli.py diagnose --root "$DIAG"
$PY pilot/cli.py verify --root "$DIAG" --phase report
```

`open` and `verify` are offline and do not require the API key. Every mock or
scripted output is labelled exactly **harness validation, NOT a measurement**;
live evidence also retains `measurement_ready=false`. Public qualification can
never authorize private execution, calibration, model ranking, key validation,
or a bank freeze. The qualification report contains harness diagnostics only.
Its repair, closeout, and positive-duty completion rates are mechanical action
resolution diagnostics. Blinded per-item choices, all-model same-path rate,
mean distinct paths, and pairwise exact-path agreement/disagreement are
descriptive saturation/discrimination observables and never model rankings.
The cheap qualification scorer is path-only: it does not issue JCASE tokens,
run judge models or humans, or produce a canonical E(C1–C16) measurement. Only
a separately approved full-scale run may create its private occurrence registry
and execution vector.
