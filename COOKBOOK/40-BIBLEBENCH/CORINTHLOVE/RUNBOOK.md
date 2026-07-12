# CORINTHLOVE Live Qualification Runbook

This runbook contains executable procedure. The active bank and next action are
always defined by `STATUS.md`.

## Environment

Repository scope:

```sh
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH
```

Python:

```sh
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
```

Load the OpenRouter credential only into the process environment. Never print,
persist, interpolate into a command argument, or copy it into a handoff.

```sh
set -a
source "$HOME/.codex/secrets/openrouter.env"
set +a
```

## Active workstream: consolidated core Tier 0

There is no active live bank. The consolidated design and offline Tier-0 plan
are approved. Execute only the read-only adapter, contract, evidence, export,
and synthetic-analysis tasks in
`COOKBOOK/20260711e-corinthlove-consolidated-core-implementation-plan.md`.
Do not create a new OpenRouter root, build a new method bank, or resume the old
one-bank queue during Tier 0.

The CROSSROADS v6 runner remains offline-ready at
`CORINTHLOVE-v3/BANKS/01-crossroads/pilot/cli.py`; its Final disposition
revision 2 review is GO for a future cheap-only public qualification. That
authorization is intentionally paused, not revoked. The v1 through v5 roots
remain immutable protocol evidence and must never be retried or reused.

Preparation and stop-state evidence:
`COOKBOOK/20260711c-corinthlove-consolidation-handoff.md`.

## Prior bank: CHARITROC

The commands below are retained only to verify or resume the completed
CHARITROC evidence roots. They do not define the active queue.

### Required live sequence

Current authorization is cheap-model OpenRouter qualification only. The
flagship panel runner and GPT-5.4 full, GPT-5.5, GPT-5.6 Sol, and other
frontier/expensive models are out of scope. The separate GPT-5.4-mini profile
is authorized only for the 12-item public qualification described below.

Choose a new immutable output root. Do not reuse a root from a different
profile hash or public-bank hash.

```sh
OUT=pilot/runs/YYYYMMDD-openrouter-PROFILE-live-v1
```

Run checkpoints in order:

```sh
$PY pilot/run_cheap_openrouter.py access --out "$OUT" --run-mode live
$PY pilot/run_cheap_openrouter.py verify --out "$OUT" --run-mode live --scope access

$PY pilot/run_cheap_openrouter.py canary --out "$OUT" --run-mode live
$PY pilot/run_cheap_openrouter.py verify --out "$OUT" --run-mode live --scope canary

$PY pilot/run_cheap_openrouter.py smoke --out "$OUT" --run-mode live
$PY pilot/run_cheap_openrouter.py verify --out "$OUT" --run-mode live --scope smoke

$PY pilot/run_cheap_openrouter.py report --out "$OUT" --run-mode live
$PY pilot/run_cheap_openrouter.py verify --out "$OUT" --run-mode live --scope all
```

For the isolated GPT-5.4-mini qualification, use the profile-forcing wrapper
for every checkpoint instead of passing a profile flag:

```sh
OUT=pilot/runs/YYYYMMDD-gpt54-mini-azure-v1-live-v1

$PY pilot/run_gpt54_mini_openrouter.py access --out "$OUT" --run-mode live
$PY pilot/run_gpt54_mini_openrouter.py verify --out "$OUT" --run-mode live --scope access
$PY pilot/run_gpt54_mini_openrouter.py canary --out "$OUT" --run-mode live
$PY pilot/run_gpt54_mini_openrouter.py verify --out "$OUT" --run-mode live --scope canary
$PY pilot/run_gpt54_mini_openrouter.py smoke --out "$OUT" --run-mode live
$PY pilot/run_gpt54_mini_openrouter.py verify --out "$OUT" --run-mode live --scope smoke
$PY pilot/run_gpt54_mini_openrouter.py report --out "$OUT" --run-mode live
$PY pilot/run_gpt54_mini_openrouter.py verify --out "$OUT" --run-mode live --scope all
```

The live cheap output label is `live OpenRouter qualification measurement`.
It does not authorize calibration, freezing, private execution, or a
multi-vendor claim.

### Durable retry rules

Never add a retry flag preemptively. Inspect the durable failure first.

For a classified transient provider-capacity failure:

```sh
$PY pilot/run_cheap_openrouter.py access \
  --out "$OUT" --run-mode live --retry-failed

$PY pilot/run_cheap_openrouter.py canary \
  --out "$OUT" --run-mode live --retry-failed

$PY pilot/run_cheap_openrouter.py smoke \
  --out "$OUT" --run-mode live --retry-failed
```

Observed OpenRouter capacity signature on 2026-07-11:

- HTTP envelope 200;
- streamed provider error code 502;
- `provider_unavailable` / high-demand message;
- no selected endpoint and no `[DONE]` marker;
- zero emitted benchmark tokens;
- runner label `protocol_malformed_sse`;
- later explicit retry succeeds.

Treat that signature as `provider_capacity`, not benchmark failure. Any other
signature must be classified anew.

## Profile and endpoint checks

The verified `cheap-azure-v1` panel contains:

| Alias | Exact Azure snapshot | Input $/M | Output $/M |
|---|---|---:|---:|
| `openai/gpt-5-nano` | `openai/gpt-5-nano-2025-08-07` | 0.05 | 0.40 |
| `openai/gpt-5.4-nano` | `openai/gpt-5.4-nano-20260317` | 0.20 | 1.25 |
| `openai/gpt-5-mini` | `openai/gpt-5-mini-2025-08-07` | 0.25 | 2.00 |

The requested correction is:

| Alias | Exact Azure snapshot | Input $/M | Output $/M |
|---|---|---:|---:|
| `openai/gpt-5.4-mini` | `openai/gpt-5.4-mini-20260317` | 0.75 | 4.50 |

Every live profile must require:

- routing slug `azure` in both `only` and `order`;
- returned display provider `Azure`;
- `allow_fallbacks: false`;
- `require_parameters: true`;
- `data_collection: deny`;
- `zdr: true`;
- exact returned snapshot membership;
- the frozen price ceiling and minimum 400,000-token context.

CROSSROADS profile v2 obtains free preflight evidence from both the per-model
endpoint API and OpenRouter's dedicated ZDR endpoint API. It joins exact
model/provider/tag/snapshot identities, accepts one or more base/regional Azure
rows only when every joined row independently passes numeric-zero status,
context, capability, and price gates, and persists both raw responses for
semantic replay. The per-model API's absent `zdr` field is never interpreted as
affirmative evidence.

CROSSROADS profile v6 additionally requests `X-OpenRouter-Metadata: enabled`
on every paid POST and attests directly from the full ChatResult plus the
allowlisted `X-Generation-Id` response header. Body/header ID, top-level Azure,
exact snapshot, requested alias, direct strategy, exact integer attempt 1,
one selected Azure/exact-snapshot row, usage, finish reason, tool cardinality,
and reconstructed cost must all agree. It does not poll `/generation`. Access
uses 512 completion tokens; fork/follow-through/closeout each use 4,096 because
reasoning tokens count inside the completion ceiling. A rejected paid response
must preserve its bound request/raw call and any completed paid prefix for
offline semantic replay. Rebuild every request from canonical episode, truth,
selected branch, model, binding, and attempt; never accept only a recomputed
self-hash. Paid access transport/attestation failures preserve the canonical
request, catalog gate, and raw call or explicit absence. Finish failures also retain normalized/native reason
and completion/reasoning counts.

Every transmitted model parameter must be declared by the exact eligible Azure
catalog rows. In particular, do not send `parallel_tool_calls`: Azure does not
declare it, and `require_parameters: true` would correctly reject the route.

Staged calls use ordinary (`strict: false`) function calling for the complete
top-level `oneOf` action inventory and omit message `response_format`; Azure
rejects that schema under provider strict mode. The local executor—not the
provider—is the authoritative exact JSON/action/finish/completeness validator.

Freeze the first catalog snapshot within a run root. On resume, semantically
validate and reuse it; do not refetch a volatile catalog payload and compare its
raw hash with the immutable snapshot.

## Failure taxonomy

| Class | Evidence | Action |
|---|---|---|
| Provider capacity | Explicit provider error, no selected endpoint/output | Preserve; explicit retry |
| Protocol compatibility | Valid provider response rejected by parser | Reproduce offline; focused test; narrow fix |
| Integrity | Secret, route, snapshot, future-turn, tool, or identifier violation | Stop; do not retry until explained |
| Benchmark content | Localized cue/truth/family/position/ID artifact | One evidence-supported revision cycle |
| Infrastructure | Crash before terminal artifact | Resume; runner reconciles/abandons incomplete attempt |

## Archived CROSSROADS saturation and redesign analysis

For each CROSSROADS model report path resolution/evasion, path entropy, clause-
profile dispersion, surface-cue decoding, repair resolution, closeout
resolution, and positive-duty completion. Across models report all-model exact
path agreement, mean distinct resolved paths per item, pairwise exact-path
agreement/disagreement, unresolved denominators, and retry/capacity rates
separately from benchmark behavior.

Do not infer final model ordering, correctness, or canonical E(C1–C16) from the
30-item public qualification split. Do not rewrite cues from aggregate path
frequency. A redesign requires a replicated localized artifact. Preserve the
balanced relational cue axes and opaque JSEED/JCASE/JUDGE namespaces when their
decoder, occurrence, and leakage tests pass.

## Verification and handoff

Before completion:

1. Run the active bank's full offline suite once.
2. Run `verify --scope all` in a fresh process.
3. Run the static adversarial filter.
4. Obtain the required adversarial bank review.
5. Record exact commands, counts, hashes, spend reconstruction, retry history,
   limitations, and verdict in the dated handoff.
6. Update `STATUS.md` to the next approved consolidated milestone, not the old
   one-bank queue.

Do not commit or push unless the user explicitly requests it.
