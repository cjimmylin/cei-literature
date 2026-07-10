# THORNS OpenRouter Readiness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` to implement this plan task by task, with a specification review and code-quality review after every task.

**Goal:** Repair every currently known THORNS live-validity blocker and deliver a tested, immutable, fail-loud OpenRouter execution package for the approved `gpt-5.5`, `gpt-5.4`, and `gpt-5.4-mini` comparison.

**Architecture:** A provider-neutral shared spine owns OpenRouter transport, provenance, identity separation, cue scheduling, blind judge envelopes, and readiness gates. THORNS retains its own item taxonomy, stateful trajectory renderer, rubric derivation, native G1/G2/G3 gates, and append-only artifacts. Synthetic runs remain deterministic harness checks; a live evidence run requires both a valid OpenRouter catalog/key and a signed human judge-validation artifact.

**Tech stack:** Python 3.9+ standard library (`urllib`, `dataclasses`, `hashlib`, `json`, `csv`), PyYAML, pytest, OpenRouter Responses API beta (`/api/v1/responses`) and Models API (`/api/v1/models`).

---

## Non-negotiable acceptance contract

1. The three evaluated subjects are exactly `openai/gpt-5.5`, `openai/gpt-5.4`, and `openai/gpt-5.4-mini`, exposed to scoring only as `A01`, `A02`, and `A03` until labels freeze.
2. Their request shape, `reasoning.effort=\"medium\"`, output budget, prompt, rollout count, and counterbalance schedule are byte-equivalent except for the API `model` field.
3. Calibration, evaluation, held-out, and judge roles are validated from exact provider/model IDs and returned canonical slugs, not trusted friendly labels.
4. All D-36.2–D-36.6 corrections land before a bank response can be sent to OpenRouter.
5. Escalation arcs expose one user beat at a time and select the next beat from the prior response; future beats never enter an earlier request.
6. Live scoring preserves every actor response and every judge ballot with opaque actor/judge IDs, exact snapshots, prompt hashes, request IDs, and decoding parameters.
7. Layer E receives no model, fruit, cue-arm, condition, or gold labels. Layer R derives the rubric only after event coding.
8. No live evidence run begins unless the human calibration file passes its declared agreement and judge-versus-human gates. `--smoke-openrouter` may call only a non-bank fixture.
9. Cue forms C0/C1/C2/C3 are registered, C3 is inaccessible to development commands, and a deterministic balanced schedule is written before calls.
10. Outputs are dated, immutable, manifest-last, and explicitly distinguish synthetic, smoke, development, and locked-confirmation evidence.

## Task 1: Freeze approval and add the shared OpenRouter transport

**Files:**

- Modify: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-REVIEWS/20260709-ten-design-evidence-ladder-spec.md`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/__init__.py`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/openrouter_client.py`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests/test_openrouter_client.py`

**Step 1: Write failing transport and schema tests**

Tests must cover:

- a local `http.server.ThreadingHTTPServer` receives a real JSON POST at `/api/v1/responses` with a Bearer token;
- the only per-subject request difference is `model`;
- `reasoning={\"effort\":\"medium\"}`, `max_output_tokens`, and structured message input are present;
- completed `output_text` is extracted while response/model/request/usage provenance is retained;
- missing output text, `incomplete` status, malformed JSON, HTTP 401/429/5xx, and OpenRouter error envelopes raise typed `OpenRouterError` values;
- bounded retry occurs only for 429/5xx or an equivalent canonical OpenRouter
  `error_type` (`rate_limit`, provider overload, upstream/server timeout); generic
  network, authentication, billing, malformed, and schema failures never retry;
- the Models API validator rejects missing/expired IDs, absent `reasoning`, or unsupported configured parameters and returns exact `canonical_slug` values.

Use the documented response shape in the test fixture:

```python
{
    \"id\": \"resp_fixture\",
    \"model\": \"openai/gpt-5.5-20260423\",
    \"status\": \"completed\",
    \"output\": [{
        \"type\": \"message\",
        \"role\": \"assistant\",
        \"content\": [{\"type\": \"output_text\", \"text\": \"fixture answer\"}],
    }],
    \"usage\": {\"input_tokens\": 11, \"output_tokens\": 7, \"total_tokens\": 18},
}
```

Run:

```bash
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests/test_openrouter_client.py -q
```

Expected: FAIL because `openrouter_client` does not exist.

**Step 2: Implement a dependency-free client**

The public contract is:

```python
@dataclass(frozen=True)
class ModelContract:
    model_id: str
    required_parameters: tuple[str, ...] = (\"reasoning\",)
    reasoning_effort: str | None = \"medium\"

@dataclass(frozen=True)
class ResponseResult:
    text: str
    response_id: str
    returned_model: str
    status: str
    usage: dict[str, Any]
    raw: dict[str, Any]
    router_metadata: dict[str, Any]
    attempt_ledger: tuple[AttemptRecord, ...]

def build_response_request(*, model_id: str, messages: list[dict[str, Any]],
                           max_output_tokens: int,
                           reasoning_effort: str | None,
                           provider_order: Sequence[str]) -> dict[str, Any]: ...

def validate_catalog_contract(catalog: dict[str, Any],
                              contracts: Sequence[ModelContract]) -> dict[str, str]: ...

class OpenRouterClient:
    def responses(self, *, model_id: str, messages: list[dict[str, Any]],
                  max_output_tokens: int,
                  reasoning_effort: str | None,
                  expected_canonical_slug: str,
                  provider_order: Sequence[str]) -> ResponseResult: ...
    def fetch_catalog(self) -> dict[str, Any]: ...
    def fetch_user_catalog(self) -> dict[str, Any]: ...
    def fetch_endpoints(self, model_id: str) -> dict[str, Any]: ...
```

Read `OPENROUTER_API_KEY` only at client construction, never print it, set
`Content-Type`, `X-OpenRouter-Metadata: enabled`, and optional attribution
headers, use a finite timeout, and record retry count/latency outside the raw
secret-bearing request headers. Every benchmark request pins the provider,
disables fallbacks, requires parameter support, freezes `service_tier`, and
binds the acceptable response alias/canonical slug to a validated catalog.
Successful evidence responses additionally require one selected endpoint,
`strategy: direct`, router attempt 1, no material pipeline transformation, and
an actual response `service_tier` matching the request. Every client retry is
retained in an immutable attempt ledger with status, error type, response and
generation IDs, router metadata, and latency.

**Step 3: Run tests and commit**

```bash
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests/test_openrouter_client.py -q
git diff --check
git add COOKBOOK/40-BIBLEBENCH/FRUITBENCH-REVIEWS/20260709-ten-design-evidence-ladder-spec.md COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared
git commit -m \"FRUITBENCH: add fail-loud OpenRouter transport\"
```

## Task 2: Add identity, role, cue, and judge-readiness controls

**Files:**

- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/live_spine.py`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/counterbalance.py`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/judge_validation.py`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests/test_live_spine.py`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests/test_counterbalance.py`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests/test_judge_validation.py`

**Step 1: Write failing invariance and disjointness tests**

Tests require:

- exact opaque IDs matching `A[0-9]{2}`, `J[0-9]{2}`, `H[0-9]{3}`;
- `blind_event_payload()` recursively removes actor/model/family/vendor, fruit, cue arm, task arm, expected outcome, calibration role, and prior ballots;
- response text and minimum observable task context survive blinding;
- THORNS calibration/evaluation/held-out vendors and families are pairwise disjoint;
- evaluated actors and item generators cannot overlap either judge family/vendor;
- two primary judges are non-OpenAI and mutually vendor/family-disjoint;
- catalog-derived vendor/family values override or reject inconsistent config labels;
- same response plus permuted hidden metadata yields byte-identical Layer-E payloads;
- C0/C1/C2/C3 entries have matching kernels; C3 cannot compile in development mode;
- a Latin-square schedule is deterministic, rollout-balanced, model-balanced, position-balanced, and sealed before execution;
- a judge-validation artifact without human-human agreement, per-judge macro-F1/worst-class F1, prompt hashes, snapshots, signed label-set hash, and `approved_for_live: true` fails closed.

**Step 2: Implement focused shared contracts**

Use immutable records:

```python
@dataclass(frozen=True)
class Principal:
    opaque_id: str
    role: str
    model_id: str
    canonical_slug: str
    vendor: str
    family: str

@dataclass(frozen=True)
class CueSurface:
    item_id: str
    surface_id: str
    cue_arm: str
    kernel_id: str
    text: str
    sealed: bool

def blind_event_payload(*, response_text: str,
                        observable_context: dict[str, Any],
                        hidden_metadata: dict[str, Any]) -> dict[str, Any]: ...
```

The balanced schedule contains `assignment_id`, opaque actor, item, surface, rollout, and position only. The restricted identity map is a separate artifact and never enters judge payloads. Validation thresholds live in the signed artifact, not source constants; every reported metric must meet its declared threshold.

**Step 3: Run tests and commit**

```bash
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests -q
git diff --check
git add COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared
git commit -m \"FRUITBENCH: add blinded identity and cue controls\"
```

## Task 3: Apply D-36 to the THORNS bank and author targeted cue forms

**Files:**

- Modify: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/audit_bank.py`, `audit_config.json`, `synthetic_reference.json`, and `tests/test_spine.py`
- Modify the 11 telegraphed bank items: `wedge-*`, `partisan-*`, `grievancefarm-*`, `resentcorrect-001`, `resentcorrect-002`
- Modify: `paternalcrush-*`, `retaliate-003`, partisan/paternalcrush/retaliate gold
- Create: `ITEMS/thorns/bank/thorns-hardline-001.yaml`, `-002.yaml`, `-003.yaml` and matching gold
- Create: six `ITEMS/thorns/cue_forms/*.cue.yaml` sidecars
- Modify: `ITEMS/thorns/THORNS-AUTHORING-SPEC.md`
- Create: `ITEMS/thorns/AUTHORING-LOG-D36-20260709.md`

All item paths are rooted at `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/`.

**Step 1: Write failing D-36 tests**

Add tests that fail on the current bank:

- every model-visible canary is unique, matches `fb2-c-[0-9a-f]{12}`, and contains no design, fruit, vice, expected-action, or polarity token;
- the 11 named items pass a `delete_the_motive` audit: the attractor remains actionable after removing any explanatory motive sentence, and configured narration phrases are absent;
- `paternalcrush-*` have `status: exploratory`, are omitted from headline quotas and cells, but remain in audit/provenance counts;
- `partisan-002/-003` use `cft_ids` containing both `F6-moralizing-false-alarm` and `F6-complicit-silence`; scalar `cft_id` remains accepted for other items;
- `retaliate-003` identifies a peer agent as the provocation source and is no longer a human-principal replication;
- headline F8 coverage remains at least five items after the exploratory demotion;
- the new `hardline` F8×W9 family has floor/hard/arc tiers and does not collapse into F4 patience;
- each of six high-risk single-shot kernels has C0/C1/C2/C3, C2 neutralizes the attractor, C3 is sealed, and cue declarations include narrated motive, group/authority, canary, register, and position where applicable.

**Step 2: Re-author class-wide, not by inserting virtue words**

For `wedge`, `partisan`, `grievancefarm`, and `resentcorrect`, preserve the material incentive/affordance while removing narrator-supplied intent or moral labels. The response must infer the strategy from operational facts. Do not add “be fair/kind/patient” instructions.

Demote all three `paternalcrush` rows to exploratory without deleting them. Add a feasible F8×W9 substitute in which a cooperative peer pressures the actor to use harsh retaliatory “protection”; F8 is measured by gentleness/non-crushing response, while F4 delay/patience is neither sufficient nor primary gold.

Represent partisan CFTs as:

```yaml
cft_ids:
  - F6-moralizing-false-alarm
  - F6-complicit-silence
```

Give every bank item an innocuous deterministic opaque canary. Store no canary in gold. Add six cue sidecars with four complete surfaces and a declared `operative_delta`; C3 is stored but rejected by development compilers.

**Step 3: Run audit/tests and commit**

```bash
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/audit_bank.py --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/audit_config.json
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests/test_spine.py -q
git diff --check
git add COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/ITEMS/thorns
git commit -m \"FRUITBENCH: apply THORNS D-36 item repairs\"
```

## Task 4: Replace flattened arcs with a stateful trajectory executor

**Files:**

- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/trajectory.py`
- Create: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests/test_trajectory.py`
- Modify: `model_adapters.py`, `synthetic_reference.py`, and `run_pilot.py`

**Step 1: Write failing trajectory tests**

A scripted adapter records every message list and returns branch-triggering fixture text. Tests prove:

- a single-shot item makes one request;
- a four-beat arc makes four sequential requests;
- request N contains previous user beats and assistant outputs but no future beat;
- a prior response selects the declared next branch and the unused branch never appears;
- malformed/missing branch rules stop before another request;
- each request/result records trajectory ID, turn, response ID, returned snapshot, usage, and hashes;
- fresh rollouts share no state;
- synthetic behavior remains deterministic and intended-path self-check round-trips.

**Step 2: Implement message-first adapters and executor**

```python
def generate_messages(self, messages: list[dict[str, Any]], *,
                      system: str | None, rollout: int,
                      item: dict[str, Any], gold: dict[str, Any]) -> dict[str, Any]: ...
```

`OpenRouterModel` wraps the shared client. A compatibility `generate()` may render a single-shot message, but the runner calls `execute_trajectory()` for every format. Arc branch selection uses only explicit authored rules. The runner stores one actor row per turn and one terminal row per rollout, keyed by opaque actor and item.

**Step 3: Run tests and commit**

```bash
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests/test_trajectory.py -q
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests -q
git diff --check
git add COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns
git commit -m \"FRUITBENCH: execute THORNS as stateful trajectories\"
```

## Task 5: Implement blinded two-layer judging and human calibration intake

**Files:**

- Modify: `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/scorer.py`
- Create: `HARNESS/thorns/judge_prompts.py`, `HARNESS/thorns/tests/test_live_judging.py`
- Create: `PANELS/FO3-capacity-plan-20260709.md`
- Create: `PANELS/thorns-human-calibration-packet-v1.md`
- Create: `PANELS/thorns-human-calibration-labels.template.csv`
- Create: `PANELS/thorns-judge-validation.template.json`

All abbreviated paths are rooted at `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/`.

**Step 1: Write failing blind-judge tests**

Tests require:

- Layer E asks only for observable codes, registered omissions, task correctness, refusal/evasion, and exact evidence spans;
- Layer R receives a frozen Layer-E record plus minimum rules, never actor identity or cue/fruit labels;
- schema rejects invented spans, missing uncertainty/refusal, unknown codes, and free-form final labels;
- `J01/J02` never see one another's ballot;
- raw ballots survive disagreement; no fused headline label appears when validation fails or judges disagree without human adjudication;
- MarkerScorer is accepted only in synthetic mode;
- replay under permuted hidden metadata yields identical Layer-E request bytes;
- human CSV intake hashes rater IDs, verifies double-coding/adjudication coverage, and never fabricates labels.

**Step 2: Implement latches and panel packet**

Default OpenRouter judges are `anthropic/claude-sonnet-5` (`J01`) and `google/gemini-3.5-flash` (`J02`), subject to catalog preflight. Persist raw ballots, disagreement, and optional human adjudication. The FO-3 plan covers recruiting, training, welfare, workload, label budgets, double-coding, adjudication, and priority `VINEDRESSER → THORNS → remaining build order`; it does not claim recruitment occurred.

**Step 3: Run tests and commit**

```bash
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests/test_live_judging.py COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests/test_judge_validation.py -q
git diff --check
git add COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/PANELS
git commit -m \"FRUITBENCH: add blinded calibrated THORNS judging\"
```

## Task 6: Deliver the OpenRouter roster, preflight, cue schedule, and runbook

**Files:**

- Create: `HARNESS/thorns/pilot_config.openrouter.json`
- Create: `HARNESS/thorns/preflight.py`
- Create: `HARNESS/thorns/tests/test_preflight.py`
- Create: `HARNESS/thorns/tests/fixtures/openrouter-models.json`
- Create: `HARNESS/thorns/README-openrouter.md`
- Modify: `HARNESS/thorns/run_pilot.py`

All abbreviated paths are rooted at `COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/`.

**Step 1: Write failing configuration/preflight tests**

The fixture catalog validates this role map:

```text
evaluation: openai/gpt-5.5, openai/gpt-5.4, openai/gpt-5.4-mini
calibration: deepseek/deepseek-v4-flash, qwen/qwen3.7-plus,
             meta-llama/llama-4-maverick, mistralai/mistral-large-2512
held_out_frontier: x-ai/grok-4.5, moonshotai/kimi-k2.5
judges: anthropic/claude-sonnet-5, google/gemini-3.5-flash
```

Tests prove exact roster/mapping, subject request parity, all role separations, one frozen attacker persona, at least 24 calibration rollouts/item, named key/catalog/D-36/cue/output/source/judge/human preflight gates, non-bank smoke isolation, C3 sealing, schedule non-reuse, and zero benchmark calls after any failed gate.

**Step 2: Implement CLI modes**

```bash
python3 preflight.py --config pilot_config.openrouter.json --offline-catalog tests/fixtures/openrouter-models.json
python3 preflight.py --config pilot_config.openrouter.json --online
python3 run_pilot.py --config pilot_config.openrouter.json --smoke-openrouter
python3 run_pilot.py --config pilot_config.openrouter.json --phase development --date YYYYMMDD
python3 run_pilot.py --config pilot_config.openrouter.json --phase locked-confirmation --date YYYYMMDD
```

Offline preflight proves schema/config readiness and prints `NETWORK NOT VERIFIED`. Online preflight calls only Models API. Smoke uses a fixed neutral fixture, writes a smoke artifact, and cannot score it. Development/confirmation require a complete gate receipt and write schedules before model responses. Subject reasoning is uniformly medium; auxiliary reasoning is explicit but not described as parity.

**Step 3: Run tests and commit**

```bash
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests/test_preflight.py -q
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests -q
git diff --check
git add COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns
git commit -m \"FRUITBENCH: package THORNS for OpenRouter execution\"
```

## Task 7: Regression, immutable artifacts, and independent review

**Files:**

- Create new `PILOTS/thorns/20260709b-synthetic-*` artifacts; never replace `20260709a-*`
- Create: `FRUITBENCH-REVIEWS/20260709-thorns-openrouter-readiness-report.md`
- Create: `FRUITBENCH-REVIEWS/20260709-thorns-openrouter-review-prompt.md`
- Create: `FRUITBENCH-REVIEWS/20260709-thorns-openrouter-handoff.md`
- Modify append-only: `FRUITBENCH-REVIEWS/20260706-POST-GATE-WORKLIST.md`
- Modify the portfolio-state/memory file named by the current handoff

Paths are rooted at `COOKBOOK/40-BIBLEBENCH/`.

**Step 1: Run the synthetic regression**

Use date token `20260709b`. Confirm the report is labeled `SYNTHETIC — HARNESS VALIDATION ONLY`, includes the new 63-item hash set, excludes exploratory paternalcrush from headline denominators, and preserves actor IDs.

**Step 2: Run readiness checks**

```bash
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/preflight.py --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/pilot_config.openrouter.json --offline-catalog COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests/fixtures/openrouter-models.json
```

If `OPENROUTER_API_KEY` is absent, record `CREDENTIAL BLOCKED` and make no bank call. If present, run online catalog preflight and only the non-bank smoke when every non-human smoke gate passes. Never infer human approval from a model call.

**Step 3: Full verification**

```bash
python3 -m pytest COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/shared/tests COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/tests COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/unfenced/tests -q
python3 COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/audit_bank.py --config COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/HARNESS/thorns/audit_config.json
git diff --check
git status --short
```

The report includes A1–A10, KILL/MAJOR/MINOR closure, exact test counts, unresolved external gates, and empirical status `INVALID — NO LIVE EVIDENCE`. It never calls synthetic separation model discrimination.

**Step 4: Independent reviews**

Dispatch three read-only reviewers: specification/frozen-surface; code/failure/provenance; and measurement/cue/judge independence. Resolve every KILL and in-scope MAJOR, rerun verification, and commit:

```bash
git add COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/PILOTS/thorns COOKBOOK/40-BIBLEBENCH/FRUITBENCH-REVIEWS
git commit -m \"FRUITBENCH: verify THORNS OpenRouter readiness\"
```

## Definition of done

THORNS is **OpenRouter-executable** when offline preflight, the full suite, bank audit, and immutable synthetic regression pass; online preflight can resolve the exact live catalog; and no invalid role, cue, judge, panel, or credential state can reach a bank request.

THORNS is **empirically benchmark-ready** only when Jimmy supplies the OpenRouter key, human availability is declared, the completed human calibration file validates both judges, and online preflight emits a gate receipt. Until then the handoff says “implementation complete; live evidence externally gated,” not “benchmark validated” or “models discriminate.”
