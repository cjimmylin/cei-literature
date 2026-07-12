# CROSSROADS pilot and qualification protocol

## Interim offline gate

Before any live call: all 630 items have A1/A2 decisions; 40 rejections remain
logged; path-classifier/evasion fixtures pass; planted profile recovery passes;
all six static policies have complete C1–C16 support and are defeated by a
predeclared profile criterion: evasion at least 0.10, at least one clause at or
at or below 0.25, or at least 12 clauses in the neutral 0.40–0.60 band. A few
negative key entries alone never count as defeat. The surface audit computes
each clause separately and has absolute association at most 0.10 in every
clause×feature cell for warmth, effort, specificity, response length, tool
identity, and ordinal position; public and
private skins/parameter regions and normalized text are disjoint; all canary,
judge, export, and scope checks pass. Human key validation is required before
the full private pilot, not faked for qualification.

## Cheap public qualification

The future bank-specific runner may use only separately authorized cheap
OpenRouter models. It must not import another bank's response schema, access
artifact, scoring contract, or runner module.

Execution order is strict:

1. Freeze an exact bank-specific model/provider/price/routing profile. Before
   any paid POST, intersect the per-model endpoint catalog with OpenRouter's
   dedicated ZDR endpoint catalog on exact model/provider/tag/snapshot
   identity and validate every eligible route independently. Then run one-stage
   access probes. Access is not a measurement.
2. Freeze six public canaries by constrained set cover: union C1–C16, all six
   fallback families, and every public substrate. Minimize item count at six;
   ties use lexicographic item ID. Run every model on these six.
3. Verify every stage journal, artifact hash, tool log, provider identity, and
   whole-root closure. A durable failure requires explicit retry; maximum three
   attempts. One invocation writes at most one new attempt for a failed arm;
   after inspecting its immutable failure, a new invocation must pass
   `--retry-failed`. Crash-resumed successful work is reused.
4. Run all 30 public episodes, reusing the six canary model-episode artifacts.
5. Report path resolution, evasion, path entropy, clause-profile dispersion,
   between-model profile distance, surface-cue decoding, and the mechanical
   selected-branch repair, closeout, and positive-duty completion rates. Also
   preserve blinded per-item model choices, all-model same-path count/rate,
   mean distinct resolved paths per item, and pairwise exact-path
   agreement/disagreement with non-jointly-resolved counts. These are
   descriptive saturation/discrimination diagnostics only. Never call them
   rankings, correctness AUCs, or E(C1–C16) measurements.

Every stage write is create-only, canonical JSON, flushed and fsynced before
its append-only journal terminal event. Credentials are out-of-band and
recursively rejected from artifacts. Requests bind the public bank hash,
profile hash, tool schema hash, scorer hashes, item/model/attempt, prior
observable transcript, and no future/private text. Verification replays
semantics from raw stage and tool evidence and rejects missing or extra files.
The runtime freezes every profile field, snapshot, route, and price ceiling;
the manifest also binds the pilot contracts, transport, runner, executor,
payload contract, and both scorers.
Each paid response is attested directly from its full ChatResult, exact
`X-Generation-Id`, top-level provider/snapshot, official direct-attempt router
selection, usage, and reconstructed cost. Qualification does not depend on a
later `/generation` record.
With `require_parameters: true`, every transmitted model parameter must also
appear in the exact eligible Azure endpoint capability set. Unsupported
optional controls are forbidden rather than silently ignored.
Provider-side strict schema enforcement is disabled for the top-level `oneOf`
action inventory because Azure rejects that combination. The complete schema
is still sent, and the local executor is the authoritative fail-closed
validator of exact fields, canonical arguments, action signatures, finish
reason, and call completeness.
It reconstructs the maximum call cost from prompt and completion tokens;
reasoning tokens must be contained within completion tokens and are never
double-counted.

Qualification explicitly sets `authorizes_private_execution=false`,
`authorizes_calibration=false`, `authorizes_freeze=false`, and
`authorizes_model_ranking=false`. The complete private pilot uses a separately
approved shared model panel and the full pre-registered
discrimination/reliability gates.

The canonical cheap gate is labelled `path-only staged qualification`. After
the committed fork, it reveals only the selected branch's public state and two
repair affordances; after that action it reveals one disjoint closeout
affordance. Every stage includes the prior observable transcript. Raw
matched/mismatched branch-state references never cross the model boundary.
The resulting repair/closeout rates are mechanical harness diagnostics only.

## Full-scale judge-case issuance (not performed)

Cheap public qualification is path-only. It neither issues blind judge cases
nor estimates E(C1–C16), and its reports must not imply either operation.

A future separately authorized full-scale runner performs these steps only
after candidate execution is durably closed:

1. Canonicalize the observable transcript and artifacts and compute their
   SHA-256 digest.
2. Resolve the private item-specific `JSEED-<UUIDv4>` from
   `sidecar/judge_token_map.json`; the seed never leaves the runner.
3. Call `OccurrenceCaseRegistry.issue_case` with run ID, execution ID, exact
   candidate snapshot, candidate family, response hash, and scoring occurrence.
   The default UUID factory is cryptographic `uuid4`; test injection is the
   only deterministic mode.
4. Store the returned random `JCASE-<UUIDv4>` and complete occurrence tuple in
   `pilot/runs/<run>/private/judge_case_registry.jsonl`. The registry is
   mode 0600, append-only, fsynced, hash-chained, collision-checked, and rejects
   duplicate occurrence issuance.
5. Recompute and verify the response hash while building a payload containing
   exactly JCASE, observable transcript, and observable artifacts.
6. Load a separately frozen roster by its expected canonical SHA-256. Resolve
   every raw or adjudicator JUDGE identity and role from that roster; reject
   unknown, rebound, same-candidate-family, same-raw-family, or raw/adjudicator
   family-overlap identities.
7. Preserve both raw ratings, roster hash, IRR inputs, and any separately roled
   adjudication. Never replace raw evidence with consensus.

The included roster is a mock schema fixture labelled **harness validation,
NOT a measurement**. No actual judge or human roster and no full-scale
execution vector currently exist.
