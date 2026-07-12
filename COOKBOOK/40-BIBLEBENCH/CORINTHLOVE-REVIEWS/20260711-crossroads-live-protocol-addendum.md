# CROSSROADS live-protocol review addendum

Date: 2026-07-11  
Reviewer: fresh independent Codex subagent  
Scope: post-GO OpenRouter profile, catalog, transport, runner, and evidence revision only  
Verdict: **GO — live cheap-model access may resume in a new v2 root**

This addendum leaves the construct verdict in
`20260711-crossroads-bank-rereview.md` unchanged. I did not reassess or modify
candidate content, C1–C16 keys, scoring, or the judge design. I made no paid
POST, completion, or model call and did not load an API credential. The only
network operations were unauthenticated, read-only GETs to OpenRouter's current
official endpoint catalogs.

## Authorization boundary

The runner may create a **new**
`pilot/runs/20260711-openrouter-cheap-azure-v2-live-v1` root and run its access
phase for exactly these aliases:

- `openai/gpt-5-nano`
- `openai/gpt-5.4-nano`
- `openai/gpt-5-mini`
- `openai/gpt-5.4-mini`

The preserved v1 root must not be opened for execution, retried, rewritten, or
used as v2 evidence. A catalog-gate failure stops before the paid POST. A paid
failure stops that invocation and requires inspection plus an explicit
`--retry-failed` in a later invocation. Canary execution remains contingent on
all four access arms succeeding and the access evidence verifying offline.

This GO authorizes public qualification only. It does not authorize private
episodes, calibration, ranking, canonical E(C1–C16), live judges, key
validation, frontier filtering, bank freeze, or measurement claims.

## Findings

### 1. Frozen cheap allowlist and routing identity — PASS

`cheap_profile.json` and the independent in-code canonical baseline contain
only the four aliases above, with exact snapshots and price ceilings. Any other
alias or any profile-field mutation fails. The request-side provider slug is
lowercase `azure`, while returned evidence must independently report the
display name `Azure`. This matches OpenRouter's current official Azure example
and its base-slug rule: a base slug selects its regional variants.

Every access, fork, follow-through, and closeout body carries the exact frozen
provider object:

```json
{
  "only": ["azure"],
  "order": ["azure"],
  "allow_fallbacks": false,
  "require_parameters": true,
  "data_collection": "deny",
  "zdr": true
}
```

`OpenRouterClient.complete` rejects a body whose provider object differs, so a
caller cannot bypass this routing contract at the transport boundary.

### 2. Exact model/ZDR catalog intersection — PASS

The transport fetches both the per-model endpoint list and OpenRouter's
dedicated, automatically updated ZDR endpoint list. The paid-call gate joins
them on the exact tuple `(model_id, provider_name, tag, name)`. An endpoint is
eligible only when:

- the model ID equals the allowed alias;
- the display provider is exactly `Azure` and the tag is `azure` or
  `azure/<region>`;
- the endpoint name is exactly `Azure | <frozen snapshot>`;
- both catalogs expose the same exact-integer status code `0`;
- both catalogs agree on context, supported parameters, and input/output
  prices;
- the endpoint independently satisfies the minimum context, required
  parameters, and both frozen price ceilings.

No `zdr` property is synthesized from the per-model response. The attestation
instead records exact membership in the dedicated ZDR catalog and preserves
both raw catalog responses. The numeric `0` check is explicitly labelled a
local `exact-integer-zero` admissibility policy; it is never relabelled as a
provider-authored string such as `available`.

The current read-only catalogs passed this exact implementation for all four
models:

| Alias | Eligible exact Azure/ZDR routes | Tags |
|---|---:|---|
| `openai/gpt-5-nano` | 2 | `azure`, `azure/swedencentral` |
| `openai/gpt-5.4-nano` | 1 | `azure` |
| `openai/gpt-5-mini` | 2 | `azure`, `azure/swedencentral` |
| `openai/gpt-5.4-mini` | 1 | `azure` |

The two-region cases are not collapsed or accepted by count alone. Every route
is checked separately, and all eligible routes must be equivalent on model,
provider, snapshot, status, context, full supported-parameter set, and both
prices, differing only in tag and source-list index. Regression tests reject
cross-catalog drift, capability unioning across endpoints, unsupported status
types/values, absent ZDR membership, price drift, and non-equivalent regional
duplicates.

### 3. Completion/provider/snapshot/cost attestation — PASS as a contract;
live evidence pending

After a successful catalog gate, the transport performs one non-retrying POST
and polls `/api/v1/generation` only for its exact request ID. Semantic replay
requires:

- identical nonempty request IDs in completion and generation records;
- the exact frozen snapshot in both records;
- generation `provider_name == "Azure"`;
- identical prompt/completion token counts and total cost across both records;
- response total tokens equal prompt plus completion tokens;
- reasoning tokens, when reported, to agree and remain a subset of completion
  tokens;
- actual cost not to exceed the frozen price-ceiling reconstruction.

Missing/unknown/truncation/content-filter finish reasons, inconsistent tool-call
cardinality, incomplete calls, provider/snapshot drift, token drift, or cost
drift fail before a path result can be accepted. The contract passes with
scripted evidence, but an actual returned provider/snapshot/cost attestation
necessarily remains pending until the newly authorized access phase runs.

### 4. Immutable evidence and version binding — PASS

The failed v1 root independently passes byte-level closure:

```text
valid=true; artifacts=3; journal_entries=3; phases_complete=[]
```

Its only attempt is an immutable, hash-journaled failed access artifact for
`openai/gpt-5-nano`; no phase-complete marker or benchmark-case artifact
exists. The current runtime rejects that root with
`ValueError: qualification manifest version differs`.

New manifests use `crossroads-public-qualification-v2` and bind the profile,
pilot contracts, OpenRouter transport, runner, executor, payload contract,
path classifier, and follow-through scorer. The focused regression confirms
those new bindings. Thus this compatibility revision cannot silently continue
under the v1 root or under a v2 root created with different runtime bytes.

### 5. No construct, candidate, key, or scorer change — PASS

The v1-bound public bank and executable surfaces are byte-identical after the
protocol revision:

```text
bank                    d0bb7f69687a2cabe778a5425047855eb515d8c6519ae58d785288f345f3f4e3
seeds_public            8bba1d68e1377e8ec198199a251c941b4adfb5ad2ae0b9de2de081cd6500a00d
ground_truth            c7305e0da059019be2fbb62914e59efe01058b35a4b01083ab710c86c172b793
staged_tool_contracts   3efd467411412783105c0b5f98bf03ffd92e4591b94e019d9e726e6eee56f1d2
payload_contract        2af17326503fab0622e3ec3ae7e9cd9d0a9a539abec25f59b0ceef5c3cc28780
path_classifier         914c4d18e39df90062310436a191b60c4467ec057135219a7d65c5fa25a78c21
followthrough           2880a745af7d1201a891a7597cd0031e3ff70b1237189d2446b2e7c8470c8167
executor                0e22c6944ccd46f19fab9cd9d517873a5bcb7ab912b58f89b982e4bdb8c72c4e
```

The dry generator also reproduced the GO-reviewed construction exactly:
630 accepted, 600 private, 30 public, 40 rejected, 40 structures, 60 stated
pairs, rank 15, and the same scenario/private/public visible-surface hashes
`116b52...ef23`, `b72f5f...2e84`, and `f60089...f7e`.

## Verification performed

```text
PYTHONDONTWRITEBYTECODE=1 $PY -m pytest \
  tests/test_pilot_contracts.py tests/test_pilot_openrouter.py \
  tests/test_pilot_runner.py -q -p no:cacheprovider
  -> 30 passed in 11.61s

PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/test_pilot_*.py \
  -q -p no:cacheprovider
  -> 62 passed in 12.96s

PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/ -q -p no:cacheprovider
  -> 219 passed in 52.53s

$PY generator.py --dry
  -> 630 accepted; 600 private; 30 public; 40 rejected;
     40 structures; 60 stated pairs; rank 15; reviewed hashes unchanged

read-only GET + current validate_catalog for all four aliases
  -> eligible endpoint counts 2 / 1 / 2 / 1; all passed

verify_evidence_root(pilot/runs/20260711-openrouter-cheap-azure-v1-live-v1)
  -> valid=true; artifacts=3; journal_entries=3; phases_complete=[]
```

## Primary-source checks

- OpenRouter's [provider-routing documentation](https://openrouter.ai/docs/guides/routing/provider-selection)
  documents provider slugs, base-slug regional matching, `only`, `order`,
  `allow_fallbacks`, `require_parameters`, `data_collection`, and per-request
  `zdr`; it also gives `azure` as the Azure routing slug.
- OpenRouter's [ZDR documentation](https://openrouter.ai/docs/guides/features/zdr)
  states that policy is endpoint-specific, conservatively maintained, and that
  the ZDR endpoint list is automatically updated.
- The official [ZDR endpoint API](https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints-zdr)
  exposes endpoint identity, provider/tag, context, supported parameters,
  prices, and numeric status.
- The official [per-model endpoint API](https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints)
  is the other side of the exact join.

## Residual limitations and negative duty

1. No paid call was made in this review, so access, returned-provider/snapshot,
   and actual-cost evidence are not yet empirical. That is the purpose of the
   authorized access phase and is not silently treated as passed.
2. OpenRouter does not document a stable semantic label for integer status
   `0` in the reviewed surface. The bank correctly treats it only as a frozen,
   exact observed admissibility value. Any type/value change fails closed and
   requires another reviewed protocol revision.
3. Generation metadata attests the Azure display provider but not the selected
   regional tag. This is acceptable here only because every route selected by
   the base slug is independently ZDR-listed and statically equivalent. It
   would not support a claim about which Azure region actually served a call.
4. A successful access artifact preserves both raw catalogs. A catalog
   preflight that fails validation is durably recorded as a sanitized failed
   attempt with its exact binding and error, but the raw invalid catalog bodies
   are not attached to that failed artifact. This limits retrospective schema
   diagnosis but does not weaken the paid-call gate: validation raises before
   `complete`, no phase closes, and retry remains explicit.

## Final disposition

**GO.** Live access may resume now, but only by creating the new v2 root and
running the cheap four-model access checkpoint. Preserve the old v1 root. Stop
and review any catalog or access failure before authorizing a retry or moving
to the six-item canary.
