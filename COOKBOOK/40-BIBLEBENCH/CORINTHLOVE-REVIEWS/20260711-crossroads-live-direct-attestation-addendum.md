# CROSSROADS direct-attestation live-protocol addendum

Date: 2026-07-11  
Reviewer: fresh independent Codex subagent  
Scope: post-v2 direct-completion attestation revision only  
Verdict: **GO — fresh v3 cheap public access root authorized**

This addendum leaves the construct verdict in
`20260711-crossroads-bank-rereview.md` and the catalog/ZDR findings in
`20260711-crossroads-live-protocol-addendum.md` unchanged. I reviewed only the
profile-v3 direct ChatResult evidence path introduced after the v2
`/generation` timeout. I did not edit or reassess candidate content, C1–C16
keys, path scoring, follow-through scoring, or judge design. I loaded no
credential and made no paid POST, completion, or model call. Network use was
limited to unauthenticated, read-only OpenRouter catalogs and official
documentation/OpenAPI.

## Authorization boundary

The runner may create the fresh root

`pilot/runs/20260711-openrouter-cheap-azure-v3-live-v1`

and run its access phase for exactly:

- `openai/gpt-5-nano`
- `openai/gpt-5.4-nano`
- `openai/gpt-5-mini`
- `openai/gpt-5.4-mini`

The v1 and v2 roots remain immutable failure evidence and must not be opened
for execution, retried, rewritten, or treated as v3 evidence. The six-item
canary remains contingent on all four v3 access arms succeeding and the access
root passing offline semantic verification. Any v3 access failure stops the
phase; no retry is authorized until its immutable failure is inspected.

This GO is only for cheap, public qualification. It does not authorize private
episodes, calibration, model ranking, canonical E(C1–C16), live judges, expert
key validation, frontier filtering, bank freeze, or measurement claims.

## Findings

### 1. Cheap allowlist and route enforcement — PASS

`cheap_profile.json` and the independent frozen profile in `contracts.py`
contain only the four aliases above, their exact Azure snapshots, and their
per-token price ceilings. Runtime profile validation is byte-canonical; a
profile field change or non-allowlisted model fails.

Every access, fork, follow-through, and closeout request carries exactly:

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

`OpenRouterClient.complete` independently rejects any different provider
object at the final transport boundary. OpenRouter documents `only`, `order`,
`allow_fallbacks`, `require_parameters`, data-collection denial, and per-call
ZDR in its official [provider-routing documentation](https://openrouter.ai/docs/guides/routing/provider-selection);
with `zdr: true`, only ZDR endpoints are eligible according to the official
[ZDR documentation](https://openrouter.ai/docs/guides/features/zdr). The exact
per-model/dedicated-ZDR catalog intersection from profile v2 is retained.

My unauthenticated read-only catalog replay passed the current catalogs for all
four aliases:

| Alias | Eligible exact Azure/ZDR routes | Tags |
|---|---:|---|
| `openai/gpt-5-nano` | 2 | `azure`, `azure/swedencentral` |
| `openai/gpt-5.4-nano` | 1 | `azure` |
| `openai/gpt-5-mini` | 2 | `azure`, `azure/swedencentral` |
| `openai/gpt-5.4-mini` | 1 | `azure` |

### 2. Direct completion attestation — PASS as a fail-closed contract;
live qualification evidence pending

Every paid non-streaming response must preserve the complete parsed ChatResult
and exactly one allowlisted response header, `X-Generation-Id`. Attestation
then requires all of the following before access or an episode can succeed:

- one nonempty, whitespace-canonical response ID equal to the sole generation
  header value;
- top-level display provider exactly `Azure` and model exactly the frozen
  snapshot;
- router metadata `requested` equal to the allowed alias, `strategy` exactly
  `direct`, and exact-integer `attempt == 1`;
- a nonempty `endpoints.available` list in which every row is Azure and the
  frozen snapshot, with exactly one row marked selected;
- exactly one assistant choice; only `stop` with zero tool calls or
  `tool_calls` with nonempty complete tool evidence can pass;
- complete nonnegative integer token usage, `total = prompt + completion`,
  reasoning contained within completion, and numeric cost no greater than the
  frozen per-token reconstruction.

The transport allowlists only `X-Generation-Id`; authorization, cookies, and
all other response headers are neither returned nor persisted. Credential
keys and recognizable credential values are recursively rejected from every
artifact-facing value.

The direct evidence is aligned with OpenRouter's official sources:

- [router metadata](https://openrouter.ai/docs/guides/features/router-metadata)
  defines the opt-in header, direct strategy, 1-indexed successful attempt,
  candidate rows, and selected endpoint; cache replays omit this metadata and
  therefore cannot satisfy this contract;
- [streaming/API documentation](https://openrouter.ai/docs/api/reference/streaming)
  states that `X-Generation-Id` is returned for all completion endpoints;
- the official [OpenAPI schema](https://openrouter.ai/openapi.json) defines
  `EndpointsMetadata.total` as the whole candidate count and `available` as a
  separate list; its example has `total=3` with one available row. The code
  correctly requires an integer `total >= len(available)`, not false equality;
- the official [Chat response/usage documentation](https://openrouter.ai/docs/api/reference/overview)
  defines non-streaming usage and `total_tokens` as prompt plus completion.

The current OpenAPI marks `usage.cost` optional and does not list the observed
top-level `provider` extension in `ChatResult`. The runner deliberately
requires both rather than weakening evidence when either is absent. That is a
safe compatibility sensitivity: an omission fails the arm and cannot become
qualification evidence.

### 3. The two nano diagnostics justify the v3 access envelope — PASS as
protocol evidence, not benchmark evidence

I treated the two authorized observations supplied to this review as
**protocol diagnostic, NOT a benchmark measurement**; they are not accepted
as qualification artifacts.

- Diagnostic A used the old 32-token medium-reasoning access envelope. It
  returned HTTP 200 with `finish_reason=length`, no usage, and equal body/header
  IDs; its `/generation` lookup remained 404 at 0, 2, 5, 10, 20, and 40-second
  polls. Profile v3 would reject it for truncation and missing usage.
- Diagnostic B used 512 tokens and returned HTTP 200 with `stop`, exact
  body/header identity, top-level Azure and the frozen snapshot, direct
  attempt-1 router metadata selecting Azure/the same snapshot, and usage of
  51 prompt + 387 completion = 438 total tokens. Its reported cost,
  `$0.00015735`, exactly equals the nano ceiling reconstruction:
  `51 × $0.00000005 + 387 × $0.0000004`.

The access request is now frozen at 512 completion tokens. Benchmark stages
remain unchanged at 2,048 fork, 1,024 follow-through, and 1,024 closeout.
Regression tests assert all four values.

### 4. Semantic replay and version binding — PASS

Successful access evidence preserves and revalidates both raw catalogs, their
derived attestation, the exact access request and hash, the full direct
ChatResult/header record, and its derived call attestation. Episode replay
rebuilds every request, tool event/log, selected branch, path classification,
stage completion, usage sum, and report. Whole-root verification first closes
the create-only files and hash journal, then performs this semantic replay
without a credential or network client.

New manifests use `crossroads-public-qualification-v3` with profile
`crossroads-cheap-azure-v3`. Current bindings independently reproduced here
are:

```text
bank                  d0bb7f69687a2cabe778a5425047855eb515d8c6519ae58d785288f345f3f4e3
seeds_public          8bba1d68e1377e8ec198199a251c941b4adfb5ad2ae0b9de2de081cd6500a00d
ground_truth          c7305e0da059019be2fbb62914e59efe01058b35a4b01083ab710c86c172b793
staged_tool_contracts 3efd467411412783105c0b5f98bf03ffd92e4591b94e019d9e726e6eee56f1d2
profile               6026830ee30ad692fcfb3eb812216b308e158f3bc82b1b38a05689967a3b57a3
pilot_contracts       71fc999b5e13d60acf40c1668c6af520d029d2576c02dddb959eaaec87f17272
openrouter_transport  b6971056b13138f19049a9984ee41cfbb52d73a54e079aa45073943f0d9f4f62
runner                7be24ab6812e2396da8cd3c0a6c5ba06430d9c77a9a0cd25e1de399202ad1d06
executor              3dbd1c33f8a64d90817aee9fda24548b583b88b45e7066ddf452c68d9a9b7f2b
payload_contract      2af17326503fab0622e3ec3ae7e9cd9d0a9a539abec25f59b0ceef5c3cc28780
path_classifier       914c4d18e39df90062310436a191b60c4467ec057135219a7d65c5fa25a78c21
followthrough         2880a745af7d1201a891a7597cd0031e3ff70b1237189d2446b2e7c8470c8167
```

Both preserved roots independently close at `valid=true`, 3 artifacts, 3
journal entries, and no completed phase. The current runtime rejects each with
`ValueError: qualification manifest version differs`. The v3 root did not
exist during this review.

### 5. No construct, candidate, key, or scorer revision — PASS

The bank, public episodes, public truth projection, complete staged tool
contracts, payload contract, path classifier, and follow-through scorer match
their v1-bound hashes exactly. A fresh dry build reproduced 630 accepted (600
private + 30 public), 40 rejected, 40 structures, 60 stated pairs, rank 15,
and the reviewed visible-surface hashes:

```text
scenario assignment  116b52f9ebbc34f8a133ba651a8d2d636a83a4aa220b27485f235dd658efef23
private surface      b72f5f68b1f60864d03520d6ca9afd2bda2931a9a5c34de3face08a672c02e84
public surface       f600895e32b37cf60ebe1830e299723c8fec75598e0f0234b1d4ac0a16064f7e
```

The protocol revision changes the profile, transport, runner, and executor
bindings only. The reviewed 108-file bank tree was unchanged during this
review at digest
`1650422bc8eb614f9a994314591ef005dd43bde5b917cb8f1eeb96848e8f8703`.

## Independent verification

```text
PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/test_pilot_*.py \
  -q -p no:cacheprovider
  -> 70 passed in 9.80s

PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/ -q -p no:cacheprovider
  -> 227 passed in 51.96s

$PY generator.py --dry
  -> 630 accepted; 600 private; 30 public; 40 rejected;
     40 structures; 60 stated pairs; rank 15; frozen surface hashes unchanged

unauthenticated current catalog GETs + validate_catalog, four aliases
  -> eligible exact Azure/ZDR counts 2 / 1 / 2 / 1; all passed

verify_evidence_root(v1), verify_evidence_root(v2)
  -> each valid=true; artifacts=3; journal_entries=3; phases_complete=[]

current verify_run(v1), current verify_run(v2)
  -> each rejected: qualification manifest version differs
```

## Residual limitations and negative duty

1. No v3 paid access call existed during this review. The direct contract is
   tested locally and supported by the two nano protocol observations, but
   empirical access/provider/snapshot/usage evidence for all four aliases is
   precisely what the authorized access checkpoint must obtain.
2. The diagnostic response bodies were not persisted as qualification
   artifacts, so I could verify their supplied facts and cost arithmetic but
   not independently replay their raw bytes. They remain protocol diagnostics
   only.
3. If a paid ChatResult reaches the transport but fails `attest_call`, the
   current runner persists a sanitized, identity-bound failure summary rather
   than the full invalid response. This limits forensic reconstruction and may
   require consulting OpenRouter activity for exact spend/schema diagnosis.
   It does not create a false success: no access/episode result is accepted, no
   phase closes, and a later attempt requires an explicit retry. This is
   non-blocking for the access checkpoint, but should remain an explicit
   evidence-retention limitation until invalid raw responses can be safely
   preserved.
4. The official schemas are additive, while the runner intentionally requires
   a stricter observed subset. A provider/header/usage/metadata omission will
   stop the run even if the completion itself is usable. Such an event is a
   protocol-compatibility failure, not a benchmark result and not grounds for
   silently weakening attestation.

## Final disposition

**GO.** Create the fresh v3 root and run the four-model cheap access checkpoint.
Preserve v1 and v2. If and only if all four access artifacts succeed and pass
offline verification, proceed to the already authorized six-item staged
canary. Stop on any catalog, transport, header, provider, snapshot, router,
usage, cost, finish-reason, or semantic-replay failure before considering an
explicit retry.
