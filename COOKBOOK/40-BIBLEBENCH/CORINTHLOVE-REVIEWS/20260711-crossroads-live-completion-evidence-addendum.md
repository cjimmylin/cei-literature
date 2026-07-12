# CROSSROADS live completion-evidence addendum

Date: 2026-07-11  
Reviewer: fresh independent Codex gate reviewer  
Scope: v6 live-protocol-only delta; no network/model call; no bank-code edit  
Verdict: **GO — fresh cheap-only public qualification root only**

The v6 completion-budget and evidence-preservation direction is justified, and
the full offline suite passes, but one load-bearing replay guarantee is not yet
met. A failed staged request is checked against its own recomputed hash and a
coarse field/budget contract, not rebuilt from the canonical public episode,
hidden branch truth, completed prefix, model, binding, and attempt. Therefore a
request message or tool body can be changed, `request_sha256` recomputed, and
the failed artifact can still pass semantic validation. That is incompatible
with the claimed tamper-resistant semantic replay and blocks an immediate paid
v6 root.

## Evidence

- Full bank suite, run offline with bytecode/cache disabled:
  `230 passed in 54.76s`.
- Profile, manifest, staged-request, and attempt identities are advanced and
  fail closed: `crossroads-cheap-azure-v6`,
  `crossroads-public-qualification-v6`, `crossroads-staged-request-v5`, and
  `crossroads-qualification-attempt-v2`. The manifest binds the changed profile,
  contracts, transport, runner, executor, payload contract, and scorers.
- `executor.py` sets fork, followthrough, and closeout to 4,096 completion
  tokens while retaining medium reasoning. Finish failures preserve normalized
  finish, native finish, completion-token count, and reasoning-token count.
- Rejected staged calls preserve the bound request, raw ChatResult/header
  evidence, validation error, and completed paid stage prefix. Raw calls and
  completed stages are replayed for provider/snapshot/header/router/usage,
  tool decoding, and mechanical action resolution.
- The replay gap is in `executor.py`'s `verify_failure_evidence` (approximately
  lines 791–829) plus `runner.py`'s `_validate_failure_evidence` (approximately
  lines 314–369): the former proves internal request-hash consistency and
  replays the raw rejection, while the latter checks request shape, identity,
  binding, budget, routing, and reasoning. Neither reconstructs the exact
  stage request from bank state. Existing tamper tests change the request
  without recomputing its hash, so they do not cover a rehashed semantic
  substitution.
- Access has the same evidence-boundary weakness: after the paid response is
  returned, `_access_success` calls attestation directly; a post-response
  attestation rejection falls through the generic failure path with
  `failure_evidence: null`, discarding the bound access request and returned raw
  call.
- The immutable v5 root remains unchanged. Its manifest is v5, all four access
  artifacts succeeded with exact Azure snapshots, and its only episode artifact
  is failed nano `CROSSROADS-0601` attempt 1. The journal has no canary-complete
  event; the artifact is `measurement_ready=false`, has no preserved raw
  failure evidence, and explicitly authorizes neither ranking, private
  execution, calibration, nor freeze.

## Exact binding fixes

1. Replace self-consistency-only failed-stage replay with canonical replay.
   Given `(episode, truth, model, binding, attempt)`, reconstruct the fork
   request and each completed prefix in order; derive the selected/evasion
   branch from replayed fork evidence; reconstruct followthrough and closeout
   prior-observable chains; and require exact equality of every stored request
   and request hash before validating the rejected raw call. The runner must
   invoke this bank-aware verifier for every failed episode artifact.
2. Preserve a bound failure envelope for every paid access response rejected
   after return: exact access request and hash, raw response/header evidence,
   and validation error. For a transport failure with no returned response,
   preserve the request and explicitly record that raw response evidence is
   absent. Replay it offline with the same canonical access-request builder.
3. Add rehash-aware regression tests. Mutate, then recompute the stored request
   hash for, at minimum: system/user messages, tool constants/schema,
   `stage_tool_schema_sha256`, prior-observable content/hash, selected-branch
   material, completed-prefix requests/raw calls, access request, and access raw
   response. Each mutation must fail both attempt validation and whole-root
   semantic verification. Rerun the complete suite before creating the root.

## Gate rulings

**Rubric C6 / frozen surfaces:** this is **not** a C6 or frozen-construct
change. It does not add, rename, redefine, or remap C1–C16; alter declared
coverage; change an item, action inventory, hidden key, scorer, or D-18 primary;
or create canonical E. It is a bound transport/evidence-contract revision and
therefore correctly requires a fresh root and versioned identities.

**4,096 at all stages:** **evidence-justified for cheap public qualification.**
The observed 2,048-token fork exhausted its ceiling with 1,600 reasoning
tokens; the otherwise unchanged 4,096 fork completed. The recorded full
three-stage diagnostic used 2,592/1,322/600 completion tokens, so the prior
1,024 followthrough ceiling was also inadequate. Closeout did not itself
exceed 1,024 in that diagnostic, but a uniform 4,096 envelope is a defensible
protocol control against stage-specific reasoning starvation; actual usage and
cost remain attested. This limited diagnostic evidence does not establish a
measurement decoding configuration.

**Authorization boundary:** failed evidence—including a successfully replayed
paid prefix—authorizes only diagnosis, audit, and an explicit retry under the
three-attempt ceiling. It cannot authorize measurement, model ranking,
calibration, private execution, canonical E(C1–C16), expert key validation,
frontier filtering, bank freeze, or publication claims. Nor can a successful
v6 public qualification authorize those activities; separate approval and
their missing substantive evidence remain required.

After fixes 1–3 pass the full suite, **GO** is limited to creation and execution
of one fresh immutable v6 root over the frozen cheap aliases, in access →
six-item canary → public smoke order, stopping on any new failure. Until then,
do not create or fund the v6 qualification root.

## Final disposition — 2026-07-11

**Final verdict: GO — all three conditional fixes are satisfied.** This section
supersedes the provisional `CONDITIONAL GO` language above while retaining it
as the audit history that defined the repair gate. No network or model call was
made during re-review.

1. **Canonical staged-failure replay: closed.**
   `verify_episode_failure_evidence` now rebuilds the fork request from the
   canonical episode/truth/model/binding/attempt tuple, replays the completed
   fork to derive the resolved-or-evasion branch, rebuilds followthrough with
   the exact fork observable, and, when applicable, replays the completed
   followthrough and rebuilds closeout with the exact reaction, stage-3, and
   prior-observable chain. Every completed-prefix and failed-stage request must
   equal that reconstruction and its canonical hash before raw-call validation.
   The runner invokes this bank-aware verifier for failed episode attempts.
2. **Access failure evidence: closed.** Catalog, transport, and attestation
   failures now carry a versioned envelope with the canonical access request
   and hash. Phase-appropriate catalog evidence is preserved; transport failure
   records explicit `raw_call: null`; post-response attestation failure retains
   the raw ChatResult/header evidence. Offline validation reconstructs the
   access request, revalidates catalog evidence where present, and requires the
   retained raw call to reproduce the attestation rejection.
3. **Rehash-aware tamper coverage: closed.** The regression suite rewrites an
   artifact, recomputes its request hash and complete journal chain, and still
   requires both attempt validation and `verify_run` whole-root verification to
   reject substitutions. Covered surfaces include access request/raw response,
   fork messages/tool constants/stage-schema hash, completed-prefix request/raw
   call, selected-branch state, and prior-observable content/hash.

Fresh verification evidence: the pilot subset is **74/74 passing**, and the
complete bank suite is **231/231 passing** (`231 passed in 58.86s`).

Authorization remains exactly narrow: create one new immutable v6 root over
the frozen cheap aliases, then execute access → six-item canary → public smoke,
stopping on any failure. This GO does not authorize measurement, ranking,
calibration, private execution, canonical E(C1–C16), expert key validation,
frontier filtering, bank freeze, or publication claims.

## Final disposition revision 2 — 2026-07-11

**Final verdict: GO — the two failure paths missed by the preceding review are
now closed.** This revision explicitly supersedes the earlier final GO and is
the controlling disposition for the v6 live-protocol delta. No network or
model call was made during this re-review.

1. **No evidence-free durable failure remains.** Runner validation now rejects
   `failure_evidence: null` for every failed access or episode artifact. The
   attempt orchestrator also refuses to commit any newly produced failure that
   lacks bound evidence, so an unrelated pre-envelope exception cannot become
   a durable attempt or silently consume/release a retry slot.
2. **Staged transport failures are bound and replayable.** The staged envelope
   is now `crossroads-rejected-call-v2`, distinguishes `transport` from
   `validation`, preserves the exact canonical stage request and hash, and
   requires `raw_call: null` for a transport exception. Bank-aware replay still
   reconstructs fork/followthrough/closeout and any completed paid prefix
   before accepting the failure artifact.
3. **Post-return exceptions retain evidence.** Both staged response validation
   and access attestation now catch all `Exception` subclasses after a raw call
   returns. Consequently non-`ValueError` failures such as `OverflowError`
   preserve the request, catalog evidence where applicable, raw response and
   headers, and the safe detailed error rather than falling through to a null
   generic failure.
4. **Regression coverage reaches whole-root replay.** The tests exercise an
   access `OverflowError`, staged transport failure with explicit absent raw
   response, and removal of required failure evidence. They rewrite artifact
   bytes and recompute the journal chain before requiring `verify_run` to reject
   the tampered root, in addition to attempt-level rejection.

Fresh scoped verification: **76/76 pilot tests passed in 23.47s**. The current
complete-suite result is **233/233 passing**. No remaining defect was found in
the four paths assigned to this revision.

Authorization remains unchanged and narrow: one fresh immutable v6 root over
the frozen cheap aliases, executed access → six-item canary → public smoke with
fail-stop behavior. This GO still does not authorize measurement, ranking,
calibration, private execution, canonical E(C1–C16), expert key validation,
frontier filtering, bank freeze, or publication claims.
