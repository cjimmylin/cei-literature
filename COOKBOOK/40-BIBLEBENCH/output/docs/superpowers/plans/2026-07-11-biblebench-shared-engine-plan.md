# BibleBench Shared Engine Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the isolated Python package, canonical artifact contracts, registry loader, transformation engine, shared-episode scheduler, deterministic sandbox, lossless observable-event layer, lens registry, and append-only artifact store required by all four modules.

**Architecture:** The package uses frozen dataclasses at internal boundaries and canonical JSON for hashing. YAML is accepted only at authoring boundaries and is validated before conversion. Transformations and sandbox reducers are pure functions. Each episode yields one reusable evidence bundle—forecast, primary response, matched probe, frozen observable events, and applicable lens ballots—so strategies do not create duplicate actor schedules. Opaque segment IDs preserve exact evidence while keeping model, condition, module, and expected labels out of judge packets.

**Tech Stack:** Python 3.11+, PyYAML, jsonschema, pytest, dataclasses, hashlib, pathlib.

---

### Task 1: Scaffold the isolated package

**Files:**
- Create: `BIBLEBENCH-PILOT/pyproject.toml`
- Create: `BIBLEBENCH-PILOT/README.md`
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/__init__.py`
- Create: `BIBLEBENCH-PILOT/tests/test_package.py`

- [ ] **Step 1: Write the failing package test**

```python
def test_package_exposes_version():
    import biblebench_pilot
    assert biblebench_pilot.__version__ == "0.1.0"
```

- [ ] **Step 2: Run the test and verify the import fails**

Run:

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_package.py -q
```

Expected: FAIL with `ModuleNotFoundError: No module named 'biblebench_pilot'`.

- [ ] **Step 3: Add package metadata**

```toml
[build-system]
requires = ["setuptools>=69"]
build-backend = "setuptools.build_meta"

[project]
name = "biblebench-pilot"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["PyYAML>=6.0", "jsonschema>=4.23"]

[project.optional-dependencies]
test = ["pytest>=8.0"]

[project.scripts]
biblebench-pilot = "biblebench_pilot.cli:main"

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```

```python
"""Shared execution engine for the four BibleBench passage modules."""

__version__ = "0.1.0"
```

- [ ] **Step 4: Document the claim boundary in the README**

Include the exact statement that the package measures observable model behavior
and biblical/pastoral interpretation, not faith, regeneration, virtue,
sanctification, or spiritual fruit. Document that real-world actions are
forbidden in the pilot.

- [ ] **Step 5: Run the focused test**

Run:

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_package.py -q
```

Expected: `1 passed`.

- [ ] **Step 6: Commit with path-scoped staging**

```bash
git log -1 --oneline
git add BIBLEBENCH-PILOT/pyproject.toml BIBLEBENCH-PILOT/README.md BIBLEBENCH-PILOT/src/biblebench_pilot/__init__.py BIBLEBENCH-PILOT/tests/test_package.py
git commit -m "BibleBench: scaffold shared pilot package"
```

### Task 2: Implement canonical JSON and immutable contracts

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/contracts.py`
- Create: `BIBLEBENCH-PILOT/tests/test_contracts.py`

- [ ] **Step 1: Write failing canonicalization tests**

```python
import pytest
from biblebench_pilot.contracts import canonical_json_bytes, canonical_sha256

def test_canonical_json_is_order_independent():
    left = {"b": 2, "a": [1, True, None]}
    right = {"a": [1, True, None], "b": 2}
    assert canonical_json_bytes(left) == canonical_json_bytes(right)
    assert canonical_sha256(left) == canonical_sha256(right)

@pytest.mark.parametrize("value", [float("nan"), float("inf"), (1, 2)])
def test_canonical_json_rejects_non_json_values(value):
    with pytest.raises(ValueError, match="strict canonical JSON"):
        canonical_json_bytes({"value": value})
```

- [ ] **Step 2: Verify failure**

Run:

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_contracts.py -q
```

Expected: FAIL because `contracts` does not exist.

- [ ] **Step 3: Implement strict canonical JSON**

```python
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from typing import Any, Literal

Json = None | bool | int | float | str | list["Json"] | dict[str, "Json"]

def _assert_json(value: Any) -> None:
    if value is None or type(value) in {bool, int, str}:
        return
    if type(value) is float and math.isfinite(value):
        return
    if type(value) is list:
        for child in value:
            _assert_json(child)
        return
    if type(value) is dict and all(type(key) is str for key in value):
        for child in value.values():
            _assert_json(child)
        return
    raise ValueError("value is not strict canonical JSON")

def canonical_json_bytes(value: Json) -> bytes:
    _assert_json(value)
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")

def canonical_sha256(value: Json) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()
```

- [ ] **Step 4: Add boundary dataclasses**

```python
@dataclass(frozen=True)
class CoreRef:
    core_id: str
    module: Literal["fruitbench", "corinthlove", "tencommandments", "sermonmount"]
    source_paths: tuple[str, ...]
    construct: str
    evidence_type: Literal["action", "artifact", "interpretation"]
    behavioral_attribution: Literal["applicable", "not_behaviorally_attributable"]

@dataclass(frozen=True)
class EpisodeRef:
    episode_id: str
    core_id: str
    split: Literal["public_calibration", "private_evaluation"]
    stratum: Literal["common_life", "christian_facing"]
    mode: Literal["judgment", "advice", "action"]
    transform_ids: tuple[str, ...]
    capability_twin_id: str | None
    actor_payload_sha256: str

@dataclass(frozen=True)
class SandboxEvent:
    sequence: int
    action: str
    actor: str
    target: str
    payload: dict[str, Json]

@dataclass(frozen=True)
class ArtifactEnvelope:
    artifact_type: str
    version: str
    created_at_utc: str
    payload: dict[str, Json]
    payload_sha256: str
```

- [ ] **Step 5: Test immutability and stable hashing**

Add tests asserting that assigning to a frozen dataclass raises
`dataclasses.FrozenInstanceError` and that serializing the same payload twice
produces the same SHA-256.

- [ ] **Step 6: Run tests and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_contracts.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/contracts.py BIBLEBENCH-PILOT/tests/test_contracts.py
git commit -m "BibleBench: add canonical artifact contracts"
```

Expected: all contract tests pass.

### Task 3: Define schemas and the registry loader

**Files:**
- Create: `BIBLEBENCH-PILOT/schemas/core.schema.json`
- Create: `BIBLEBENCH-PILOT/schemas/episode.schema.json`
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/registry.py`
- Create: `BIBLEBENCH-PILOT/tests/fixtures/core-valid.yaml`
- Create: `BIBLEBENCH-PILOT/tests/fixtures/core-invalid.yaml`
- Create: `BIBLEBENCH-PILOT/tests/test_registry.py`

- [ ] **Step 1: Write failing registry tests**

```python
from pathlib import Path
import pytest
from biblebench_pilot.registry import load_core_manifest

FIXTURES = Path(__file__).parent / "fixtures"

def test_load_core_manifest_accepts_complete_record():
    records = load_core_manifest(FIXTURES / "core-valid.yaml")
    assert [record.core_id for record in records] == ["F09"]
    assert records[0].evidence_type == "action"

def test_load_core_manifest_rejects_missing_non_claims():
    with pytest.raises(ValueError, match="explicit_non_claims"):
        load_core_manifest(FIXTURES / "core-invalid.yaml")
```

- [ ] **Step 2: Run and verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_registry.py -q
```

Expected: FAIL because the loader does not exist.

- [ ] **Step 3: Create a strict core schema**

The schema must require exactly these top-level fields:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "core_id", "module", "source_paths", "passage_anchors", "construct",
    "explicit_non_claims", "evidence_type", "behavioral_attribution",
    "eligible_modes", "eligible_transforms", "deficient_pole",
    "counterfeit_pole", "shared_red_lines", "module_red_lines"
  ]
}
```

Add property constraints for the four module names, the three evidence types,
the two applicability states, unique non-empty arrays, and core IDs matching
`^(F(0[1-9]|1[0-2])|L0[1-8]|T(0[1-9]|1[0-2])|S(0[1-9]|10))$`.

- [ ] **Step 4: Implement the loader**

```python
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

import jsonschema
import yaml

@dataclass(frozen=True)
class CoreRecord:
    core_id: str
    module: str
    source_paths: tuple[str, ...]
    passage_anchors: tuple[str, ...]
    construct: str
    explicit_non_claims: tuple[str, ...]
    evidence_type: str
    behavioral_attribution: str
    eligible_modes: tuple[str, ...]
    eligible_transforms: tuple[str, ...]
    deficient_pole: str
    counterfeit_pole: str
    shared_red_lines: tuple[str, ...]
    module_red_lines: tuple[str, ...]

def load_core_manifest(path: Path, schema_path: Path | None = None) -> tuple[CoreRecord, ...]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if type(raw) is not dict or set(raw) != {"manifest_version", "cores"}:
        raise ValueError("manifest must contain exactly manifest_version and cores")
    if type(raw["cores"]) is not list or not raw["cores"]:
        raise ValueError("cores must be a non-empty list")
    schema_file = schema_path or Path(__file__).parents[2] / "schemas/core.schema.json"
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    records = []
    seen = set()
    for index, row in enumerate(raw["cores"]):
        try:
            jsonschema.validate(row, schema)
        except jsonschema.ValidationError as exc:
            field = ".".join(str(part) for part in exc.absolute_path) or "core"
            raise ValueError(f"core {index} invalid at {field}: {exc.message}") from None
        if row["core_id"] in seen:
            raise ValueError(f"duplicate core_id {row['core_id']}")
        seen.add(row["core_id"])
        records.append(CoreRecord(**{
            **row,
            "source_paths": tuple(row["source_paths"]),
            "passage_anchors": tuple(row["passage_anchors"]),
            "explicit_non_claims": tuple(row["explicit_non_claims"]),
            "eligible_modes": tuple(row["eligible_modes"]),
            "eligible_transforms": tuple(row["eligible_transforms"]),
            "shared_red_lines": tuple(row["shared_red_lines"]),
            "module_red_lines": tuple(row["module_red_lines"]),
        }))
    return tuple(records)
```

- [ ] **Step 5: Add source-path validation**

Implement `validate_source_paths(records, workspace_root)` so every path is
relative, remains inside the workspace after resolution, exists, and ends in
`.md`. Test traversal (`../../secret`) and missing files as failures.

- [ ] **Step 6: Run tests and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_registry.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/schemas/core.schema.json BIBLEBENCH-PILOT/schemas/episode.schema.json BIBLEBENCH-PILOT/src/biblebench_pilot/registry.py BIBLEBENCH-PILOT/tests/fixtures/core-valid.yaml BIBLEBENCH-PILOT/tests/fixtures/core-invalid.yaml BIBLEBENCH-PILOT/tests/test_registry.py
git commit -m "BibleBench: add strict core registry"
```

Expected: registry tests pass, including source traversal rejection.

### Task 4: Implement pure episode transformations

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/transforms.py`
- Create: `BIBLEBENCH-PILOT/tests/test_transforms.py`

- [ ] **Step 1: Write failing transformation tests**

```python
import pytest
from biblebench_pilot.transforms import EpisodeSeed, TransformSpec, apply_transform

def test_apply_transform_changes_only_declared_fields():
    seed = EpisodeSeed(
        seed_id="F09-A", facts={"deadline": 10, "shortcut": True},
        actor_role="assistant", authorized_actions=("safe",),
        affected_parties=("user",), expected_state={"task_complete": True},
    )
    transform = TransformSpec(
        transform_id="monitoring-off", updates={"monitoring": False},
        invariant_fields=("facts", "authorized_actions", "affected_parties"),
    )
    result = apply_transform(seed, transform)
    assert result.monitoring is False
    assert result.facts == seed.facts

def test_transform_rejects_undeclared_moral_change():
    with pytest.raises(ValueError, match="invariant"):
        apply_transform(seed, bad_transform)
```

- [ ] **Step 2: Verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_transforms.py -q
```

Expected: FAIL because transformation types do not exist.

- [ ] **Step 3: Implement immutable seed and transform types**

```python
from dataclasses import dataclass, replace
from typing import Any

@dataclass(frozen=True)
class EpisodeSeed:
    seed_id: str
    facts: dict[str, Any]
    actor_role: str
    authorized_actions: tuple[str, ...]
    affected_parties: tuple[str, ...]
    expected_state: dict[str, Any]
    monitoring: bool = True
    pressure: int = 0
    mode: str = "action"

@dataclass(frozen=True)
class TransformSpec:
    transform_id: str
    updates: dict[str, Any]
    invariant_fields: tuple[str, ...]

def apply_transform(seed: EpisodeSeed, spec: TransformSpec) -> EpisodeSeed:
    before = {field: getattr(seed, field) for field in spec.invariant_fields}
    unknown = set(spec.updates) - set(seed.__dataclass_fields__)
    if unknown:
        raise ValueError(f"unknown transform fields: {sorted(unknown)}")
    result = replace(seed, **spec.updates)
    after = {field: getattr(result, field) for field in spec.invariant_fields}
    if before != after:
        raise ValueError("transform violated a declared invariant")
    return result
```

- [ ] **Step 4: Add twin certification**

Implement `certify_capability_twin(moral, neutral)` requiring identical mode,
tools, action schema, context length band, timing budget, and task-success target,
while requiring different ethical-conflict flags. Add tests that reject a twin
with an easier tool set or shorter context.

- [ ] **Step 5: Add stable episode IDs**

Implement IDs as the first 16 hex characters of the canonical SHA-256 over
`core_id`, private template ID, split, mode, and ordered transform IDs. Test that
surface prose changes do not change an ID unless the private template version
changes.

- [ ] **Step 6: Run tests and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_transforms.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/transforms.py BIBLEBENCH-PILOT/tests/test_transforms.py
git commit -m "BibleBench: add certified episode transformations"
```

### Task 5: Implement the deterministic sandbox reducer

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/sandbox.py`
- Create: `BIBLEBENCH-PILOT/tests/test_sandbox.py`

- [ ] **Step 1: Write failing reducer tests**

```python
import pytest
from biblebench_pilot.sandbox import SandboxState, apply_action

def test_authorized_action_updates_state_and_appends_event():
    state = SandboxState(
        values={"message_sent": False},
        allowed_actions={"draft_message": {"text": str}},
        events=(),
    )
    result = apply_action(state, "draft_message", {"text": "safe draft"})
    assert result.values["draft"] == "safe draft"
    assert result.events[-1].sequence == 1

def test_unknown_action_fails_closed():
    with pytest.raises(ValueError, match="not authorized"):
        apply_action(state, "send_real_email", {"text": "x"})
```

- [ ] **Step 2: Verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_sandbox.py -q
```

Expected: FAIL because `sandbox` does not exist.

- [ ] **Step 3: Implement sandbox state and action validation**

```python
from dataclasses import dataclass
from typing import Any

from .contracts import SandboxEvent

@dataclass(frozen=True)
class SandboxState:
    values: dict[str, Any]
    allowed_actions: dict[str, dict[str, type]]
    events: tuple[SandboxEvent, ...]

def apply_action(state: SandboxState, action: str, payload: dict[str, Any]) -> SandboxState:
    if action not in state.allowed_actions:
        raise ValueError(f"action {action!r} is not authorized")
    contract = state.allowed_actions[action]
    if set(payload) != set(contract):
        raise ValueError("action payload keys do not match the contract")
    for key, expected_type in contract.items():
        if type(payload[key]) is not expected_type:
            raise ValueError(f"action payload {key} has the wrong type")
    values = dict(state.values)
    if action == "draft_message":
        values["draft"] = payload["text"]
    event = SandboxEvent(
        sequence=len(state.events) + 1, action=action, actor="model",
        target="sandbox", payload=payload,
    )
    return SandboxState(values, state.allowed_actions, state.events + (event,))
```

- [ ] **Step 4: Add per-episode reducer registration**

Implement `SandboxDefinition` with named initial state, JSON-only action
contracts, and pure reducers. Reject callables or filesystem/network handles in
serialized definitions. Test that `send_real_email`, shell commands, and HTTP
actions cannot be registered.

- [ ] **Step 5: Add consequence summaries**

Implement `summarize_transition(initial, terminal)` returning changed keys,
affected parties, task completion, repair flags, and authorization violations.
Assert the same event sequence always produces the same summary hash.

- [ ] **Step 6: Run tests and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_sandbox.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/sandbox.py BIBLEBENCH-PILOT/tests/test_sandbox.py
git commit -m "BibleBench: add deterministic action sandbox"
```

### Task 6: Add race-safe append-only artifact writing and leakage checks

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/artifacts.py`
- Create: `BIBLEBENCH-PILOT/tests/test_artifacts.py`

- [ ] **Step 1: Write failing artifact tests**

```python
from pathlib import Path
import pytest
from biblebench_pilot.artifacts import ArtifactStore, assert_actor_payload_safe

def test_store_refuses_overwrite(tmp_path: Path):
    store = ArtifactStore(tmp_path)
    store.write("runs/r1/request.json", {"request": "safe"})
    with pytest.raises(FileExistsError):
        store.write("runs/r1/request.json", {"request": "changed"})

@pytest.mark.parametrize("key", ["ground_truth", "judge_id", "canary", "api_key"])
def test_actor_payload_rejects_hidden_keys(key):
    with pytest.raises(ValueError, match="model-visible payload"):
        assert_actor_payload_safe({key: "secret"})
```

- [ ] **Step 2: Verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_artifacts.py -q
```

- [ ] **Step 3: Implement append-only writes**

```python
from pathlib import Path
import os

from .contracts import canonical_json_bytes

class ArtifactStore:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()

    def write(self, relative: str, payload: dict) -> Path:
        target = (self.root / relative).resolve()
        if self.root not in target.parents:
            raise ValueError("artifact path escapes the store")
        target.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as handle:
            handle.write(canonical_json_bytes(payload) + b"\n")
        return target
```

- [ ] **Step 4: Implement recursive payload safety**

Reject keys or string values containing private IDs, judge IDs, gold fields,
canaries, credentials, authorization headers, environment dumps, or known secret
patterns. Error messages must not echo rejected values.

Harden publication with descriptor-walk path resolution, symlink/source-swap
rejection, a same-filesystem temporary file, `fsync`, native no-replace final
publication, and directory `fsync`. Reject aliases and hardlinks in finalized
bundles. Tests must cover every crash boundary and must never use an ordinary
rename as the final no-replace primitive.

- [ ] **Step 5: Add actor/judge envelope separation tests**

Test that an actor envelope contains only visible turns and tool contracts while
a judge envelope may contain an opaque episode token and rubric version but not
the actor model identity.

- [ ] **Step 6: Run the complete foundation suite and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_package.py BIBLEBENCH-PILOT/tests/test_contracts.py BIBLEBENCH-PILOT/tests/test_registry.py BIBLEBENCH-PILOT/tests/test_transforms.py BIBLEBENCH-PILOT/tests/test_sandbox.py BIBLEBENCH-PILOT/tests/test_artifacts.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/artifacts.py BIBLEBENCH-PILOT/tests/test_artifacts.py
git commit -m "BibleBench: add append-only artifact safety"
```

Expected: all shared-engine foundation tests pass.

### Task 7: Compile registered shared-episode schedules

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/schedule.py`
- Create: `BIBLEBENCH-PILOT/tests/test_schedule.py`

- [ ] **Step 1: Write failing geometry tests**

```python
from biblebench_pilot.schedule import compile_schedule

def test_schedule_has_one_bundle_per_episode_and_three_development_cues(pack):
    schedule = compile_schedule(pack, actor_ids=("A", "B", "C", "D"), seed=711)
    assert {row.cue for row in schedule.primary_rows} == {"C0", "C1", "C2"}
    assert "C3" not in schedule.to_canonical_json()
    assert len({row.bundle_id for row in schedule.forecast_rows}) == pack.episode_count

def test_condition_model_and_order_are_not_collinear(pack):
    compile_schedule(pack, actor_ids=("A", "B", "C", "D"), seed=711).assert_counterbalanced()
```

- [ ] **Step 2: Run the test and verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_schedule.py -q
```

Expected: FAIL because `schedule` does not exist.

- [ ] **Step 3: Implement the schedule contracts**

Create frozen `EvidenceBundlePlan`, `LogicalCall`, and `Schedule` records. One
bundle contains exactly one blind forecast, C0/C1/C2 primary calls, three
matched probes, and zero or more registered intervention calls. A lens never
adds an actor call. Use a deterministic cyclic Latin ordering over actor,
episode, cue, and presentation position. Store logical call IDs separately from
future physical-attempt IDs.

- [ ] **Step 4: Enforce cue invariants**

`C0`, `C1`, and `C2` must have byte-identical shared bodies, identical task and
answer semantics, identical tool/response schemas, identical decoding, and only
the registered cue surface may differ. `C3` has a hash commitment only and must
be absent from development source, configs, prompts, schedules, and reports.
Tests mutate each invariant and expect a field-specific failure.

- [ ] **Step 5: Enforce balanced episode roles**

Every development pack declares `target`, `null`, or `restraint`; the compiler
rejects missing roles and module-specific count imbalance. Test that cue and
order never co-vary and that semantic response tokens remain stable across cue
conditions.

- [ ] **Step 6: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_schedule.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/schedule.py BIBLEBENCH-PILOT/tests/test_schedule.py
git commit -m "BibleBench: compile shared episode schedules"
```

Expected: schedule geometry, counterbalancing, and C3-sealing tests pass.

### Task 8: Freeze observable events with lossless opaque evidence IDs

**Files:**
- Create: `BIBLEBENCH-PILOT/schemas/event.schema.json`
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/events.py`
- Create: `BIBLEBENCH-PILOT/tests/test_events.py`

- [ ] **Step 1: Write failing losslessness tests**

```python
from biblebench_pilot.events import segment_response, reconstruct_segments

def test_segments_are_lossless_and_opaque():
    source = "First sentence.\n\nSecond sentence."
    segments = segment_response(source.encode("utf-8"))
    assert [s.segment_id for s in segments] == ["S001", "S002", "S003"]
    assert reconstruct_segments(segments) == source.encode("utf-8")
```

Add failures for unknown IDs, duplicate IDs, noncanonical order, altered source
hashes, and a judge-selected span not reconstructible from retained bytes.

- [ ] **Step 2: Verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_events.py -q
```

- [ ] **Step 3: Implement deterministic segmentation and event coding**

Segment exact response/probe bytes without normalization loss. Create an
`ObservableEventRecord` containing only task correctness, registered
actions/omissions, refusal/evasion, uncertainty, consequence summaries, and
opaque evidence IDs. It must exclude actor identity, cue, module, core, private
gold, expected labels, and theological lens names.

- [ ] **Step 4: Bind events to source evidence**

Hash exact response bytes, probe bytes, sandbox log, segment table, and event
record. Reject source drift, incomplete evidence, ambiguous normalization, and
any event without an exact evidence location. Incomplete evidence remains a
visible terminal status; it is never silently dropped.

- [ ] **Step 5: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_events.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/schemas/event.schema.json BIBLEBENCH-PILOT/src/biblebench_pilot/events.py BIBLEBENCH-PILOT/tests/test_events.py
git commit -m "BibleBench: add lossless observable event records"
```

### Task 9: Register module-native lenses over shared evidence

**Files:**
- Create: `BIBLEBENCH-PILOT/schemas/lens.schema.json`
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/lenses.py`
- Create: `BIBLEBENCH-PILOT/tests/test_lenses.py`

- [ ] **Step 1: Write failing lens-firewall tests**

```python
import pytest
from biblebench_pilot.lenses import build_lens_packet

def test_lens_packet_contains_only_frozen_events_and_registered_rules(bundle, lens):
    packet = build_lens_packet(bundle, lens)
    assert set(packet) == {"packet_id", "events", "rules", "rubric_version"}

@pytest.mark.parametrize("field", ["actor_model", "cue", "module", "expected_label"])
def test_lens_packet_rejects_identity_and_gold(bundle, lens, field):
    with pytest.raises(ValueError, match="lens firewall"):
        build_lens_packet(bundle.with_private_field(field), lens)
```

- [ ] **Step 2: Verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_lenses.py -q
```

- [ ] **Step 3: Implement applicability and native scorer routing**

Each `LensSpec` declares module owner, construct, applicable core/episode roles,
required event fields, native scorer adapter, rubric version, behavioral-
attribution boundary, and forbidden metadata. Inapplicable lenses return
`NOT_APPLICABLE`, never a zero. Multiple lenses consume the same frozen event
record and may disagree; ballots remain lens- and judge-specific.

- [ ] **Step 4: Separate forecast from retrospective inference**

Store self-forecast as a distinct perception artifact created before condition
reveal. No lens may manufacture a forecast or infer inward motive from the
primary response. Add tests proving that adding a lens changes no call schedule
or observable event hash.

- [ ] **Step 5: Run the full foundation suite and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_package.py BIBLEBENCH-PILOT/tests/test_contracts.py BIBLEBENCH-PILOT/tests/test_registry.py BIBLEBENCH-PILOT/tests/test_transforms.py BIBLEBENCH-PILOT/tests/test_schedule.py BIBLEBENCH-PILOT/tests/test_sandbox.py BIBLEBENCH-PILOT/tests/test_artifacts.py BIBLEBENCH-PILOT/tests/test_events.py BIBLEBENCH-PILOT/tests/test_lenses.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/schemas/lens.schema.json BIBLEBENCH-PILOT/src/biblebench_pilot/lenses.py BIBLEBENCH-PILOT/tests/test_lenses.py
git commit -m "BibleBench: route native lenses over shared evidence"
```

Expected: all foundation tests pass and no lens changes actor-call geometry.
