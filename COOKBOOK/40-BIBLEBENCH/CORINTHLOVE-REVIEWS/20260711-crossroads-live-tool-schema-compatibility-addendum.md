# CROSSROADS tool-schema compatibility addendum

Date: 2026-07-11  
Reviewer: fresh independent Codex subagent  
Scope: profile-v5 staged tool-schema compatibility after the v4 fork failure  
Verdict: **GO — fresh v5 cheap public qualification root authorized**

This addendum leaves the construct GO, endpoint/ZDR review, direct-response
attestation review, and v4 parameter-compatibility review unchanged. I made no
network request, loaded no credential, and made no model call. I reviewed the
bank source, tests, protocol documents, frozen design brief, rubric C6, prior
reviews/addenda, and the preserved v4 evidence root.

## Evidence and diagnosis

The v4 root closes offline at:

```text
valid=true; artifacts=7; journal_entries=8; phases_complete=[access]
```

All four access artifacts succeeded with returned provider `Azure`, their
exact frozen snapshots, complete usage/cost evidence, and `stop`. The only v4
episode artifact is failed nano `CROSSROADS-0601`, attempt 1:

```text
OpenRouterTransportError: OpenRouter completion returned HTTP 400
```

It contains no accepted episode result, and canary never completed. The
current runtime rejects v4 with `qualification manifest version differs`.
Therefore no v4 benchmark response can be pooled with, resumed under, or
silently promoted into v5.

The two authorized nano observations are **protocol diagnostics, NOT benchmark
measurements**. With staged `response_format` removed, `strict:true` still
returned HTTP 400. The otherwise identical messages, action inventory, and
top-level `oneOf` parameters with `strict:false` returned HTTP 200 from Azure
and the exact snapshot. That diagnostic ended `length` at its deliberately
small 512-token ceiling, with 1,712 prompt + 512 completion = 2,224 total and
cost `$0.0002904`; this exactly reconstructs as
`1712×$0.00000005 + 512×$0.0000004`. It proves route/schema acceptance, not a
completed benchmark action. The actual fork ceiling remains 2,048.

## Frozen-surface and C6 ruling

**This is a protocol-compatibility revision, not an impermissible frozen
construct or scoring change.** It does change a bound transport surface, so it
requires a new root and new manifest; it is not byte-identical to v4. The
substantive candidate action inventory and scoring boundary do not change:

- The complete `parameters.oneOf` alternatives, their exact four required
  fields, const values, action signatures, affordances, messages, keys, and
  stage budgets are unchanged. Only provider-side `function.strict` changes
  from true to false; staged `response_format` is removed.
- Recomputing all 30 public items' fork and every branch's repair/closeout
  contract with only `strict` toggled back to true reproduced the v4 manifest's
  exact staged-tool-contract hash
  `3efd467411412783105c0b5f98bf03ffd92e4591b94e019d9e726e6eee56f1d2`.
  The v5 strict-false hash is
  `152805ec726d06a85f899d37ca893e55fc865cbdd870f8c031230e03c0e59604`.
  This isolates the bound tool-contract delta rather than concealing it.
- The bank hash remains
  `d0bb7f69687a2cabe778a5425047855eb515d8c6519ae58d785288f345f3f4e3`;
  public episodes remain `8bba1d68...a00d`, ground truth remains
  `c7305e0d...793f`, payload assembly remains `2af17326...780`, path scoring
  remains `914c4d18...8c21`, and follow-through scoring remains
  `2880a745...8167`.
- The local executor remains authoritative and fail-closed: strict JSON with
  duplicate-key rejection; exactly `tool,target,operation,arguments`; exact
  canonical signature matching; finish/tool-call cardinality agreement; and
  rejection of missing, truncated, incomplete, or partly invalid calls.
  Multiple distinct fork actions remain ambiguous, repeated exact fork actions
  remain idempotent, and multiple repair/closeout actions remain mechanically
  unresolved.

Rubric **C6 passes**. Ground truth, scoring, and the declared coverage map use
exactly frozen `C1` through `C16`; there is no new or renamed clause and no
coverage-map edit. The coverage map remains fixed-before-pilot at SHA-256
`4f9b7c1a125f60389ba7be7b0f727b5f2e4e0d19aa9b57343689f900feb76adb`.
Provider strictness neither changes a clause tag nor changes how an accepted
action maps to its pre-existing hidden key.

Access remains a separate 512-token JSON probe with `response_format`; staged
fork/follow-through/closeout remain 2,048/1,024/1,024. Azure-only routing,
endpoint-level ZDR intersection, no fallback, direct provider/snapshot/header
attestation, usage, and price ceilings are unchanged.

## Independent offline verification

```text
PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/test_pilot_*.py \
  -q -p no:cacheprovider
  -> 71 passed in 10.71s

PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/ -qq -p no:cacheprovider
  -> 228 passed in 48.96s

Focused parser/classifier assertions
  -> duplicate-key rejection PASS
  -> exact four-field decode PASS
  -> repeated fork-path idempotence PASS
  -> repeated repair/closeout action unresolved PASS
```

## Limitations and authorization boundary

The diagnostic response bodies are not qualification artifacts and were not
independently replayable from raw bytes; only the supplied protocol facts and
cost arithmetic were reviewable. The successful strict-false diagnostic ended
at `length`, and it covered one nano route only. Thus it authorizes a guarded
canary attempt, not an assumption that all four models or all three stages will
succeed. Any invalid/nonconforming output remains a durable failed attempt and
must stop the phase.

**GO.** A fresh root named
`pilot/runs/20260711-openrouter-cheap-azure-v5-live-v1` is authorized for only
the frozen four cheap aliases. Preserve v4 unchanged. Execute access, then the
six-item canary, then smoke only after each preceding phase passes offline
verification; stop on any new catalog, transport, schema, finish, provider,
snapshot, usage, cost, or semantic-replay failure.

This remains public path-only qualification, not a measurement. It does not
authorize private episodes, calibration, model ranking, canonical E(C1–C16),
live judges, expert key validation, frontier filtering, or bank freeze.
