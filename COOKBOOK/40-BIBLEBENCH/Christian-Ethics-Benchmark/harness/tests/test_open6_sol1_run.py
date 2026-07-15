"""Offline orchestration tests for the full-PUBLIC OPEN6-SOL1 SUT phase."""

from __future__ import annotations

import json
import subprocess
import sys
import threading
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import pytest

from walkworthy.clients import Message, MockModelClient, ModelResponse


def _runmod():
    from walkworthy import open6_sol1_run

    return open6_sol1_run


@dataclass(frozen=True)
class _PilotResult:
    response: ModelResponse
    body: dict
    payload: dict
    attempt_ids: tuple = (1,)


class FakePilotClient:
    """In-memory delegate with the exact runtime client's public seam."""

    def __init__(self, slug, tracker=None, disposition=0.7, item_map=None):
        self.slug = slug
        self.mock = MockModelClient(slug, seed=7, disposition=disposition,
                                    refusal_rate=0, family=slug.split("/", 1)[0])
        self.calls = []
        self.tracker = tracker
        self.item_map = item_map or {}

    def complete(self, logical_key, messages, system=None, response_validator=None):
        if self.tracker:
            self.tracker.enter(self.slug)
        try:
            response = self.mock.complete(messages, system=system)
            if response_validator is not None:
                probe_body = {"model": self.slug, "choices": [
                    {"message": {"content": response.text}}],
                    "usage": {"cost": 0.00001}}
                if response_validator(response, probe_body) is not True:
                    item_id = logical_key.split(":")[-3]
                    allocation = self.item_map[item_id].extras["allocation"]
                    budget = float(allocation["budget"])
                    tokens = list(allocation["tokens"])
                    if not tokens:
                        tokens = ["block"]
                    each = budget / len(tokens)
                    response = ModelResponse(
                        "allocation: {" + ", ".join(
                            f"{token}: {each:.6f}" for token in tokens) + "}",
                        self.slug, self.slug.split("/", 1)[0])
            body = {
                "model": self.slug,
                "choices": [{"message": {"content": response.text}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 4,
                          "cost": 0.00001},
            }
            self.calls.append({
                "logical_key": logical_key,
                "messages": [(m.role, m.content) for m in messages],
                "system": system,
                "response_validator": response_validator,
            })
            if response_validator is not None:
                assert response_validator(response, body) is True
            return _PilotResult(response, body, {
                "model": self.slug,
                "messages": [{"role": m.role, "content": m.content}
                             for m in messages],
                "max_tokens": 2048,
            })
        finally:
            if self.tracker:
                self.tracker.exit(self.slug)


class FakeSolClient:
    def __init__(self):
        self.calls = []
        self._lock = threading.Lock()

    def classify_state(self, logical_key, design, opaque_key,
                       allowed_states, assistant_response):
        with self._lock:
            self.calls.append((logical_key, design, opaque_key,
                               tuple(allowed_states), assistant_response))
        state = allowed_states[0]
        return type("SolResult", (), {
            "value": {"state": state},
            "prompt": f"prompt:{logical_key}",
            "schema": {"type": "object"},
            "final_text": json.dumps({"state": state}),
            "trace_jsonl": '{"type":"turn.completed","usage":{}}\n',
            "cli_version": "fake",
            "usage": {},
            "attempt_ids": (1,),
        })()


class ConcurrencyTracker:
    def __init__(self):
        self.active = 0
        self.max_active = 0
        self.active_by_model = Counter()
        self.max_by_model = Counter()
        self._lock = threading.Lock()

    def enter(self, model):
        with self._lock:
            self.active += 1
            self.active_by_model[model] += 1
            self.max_active = max(self.max_active, self.active)
            self.max_by_model[model] = max(
                self.max_by_model[model], self.active_by_model[model])
        time.sleep(0.0002)

    def exit(self, model):
        with self._lock:
            self.active -= 1
            self.active_by_model[model] -= 1


def _manifest(benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import build_manifest, write_or_validate_manifest

    path = tmp_path / "frozen-manifest.json"
    write_or_validate_manifest(path, build_manifest(benchmark_root))
    return path


def _catalog_raw(manifest_path):
    frozen = json.loads(Path(manifest_path).read_text())
    return {
        "fetched_at": "2026-07-14T12:00:00Z",
        "source_urls": ["https://openrouter.ai/api/v1/models"],
        "models": [{
            "slug": row["slug"],
            "providers": [{
                "provider": "fake-lowest-price-provider",
                "input_per_m_usd": row["input_per_m_usd"],
                "output_per_m_usd": row["output_per_m_usd"],
            }],
        } for row in frozen["openrouter"]["models"]],
        "raw_api_responses": [{"data": "preserved verbatim JSON value"}],
    }


def _register_catalog(run, benchmark_root, manifest, run_dir):
    return run.register_catalog_snapshot(
        benchmark_root, manifest, run_dir, _catalog_raw(manifest))


def test_manifest_must_match_current_frozen_bytes(benchmark_root, tmp_path):
    run = _runmod()
    source = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "20260714-open6-sol1"

    validated = run.prepare_run(benchmark_root, source, run_dir)

    assert validated["surface"]["item_count"] == 344
    assert (run_dir / "manifest.json").read_bytes() == source.read_bytes()
    changed = json.loads(source.read_text())
    changed["openrouter"]["hard_nte_usd"] = "25.01"
    source.write_text(json.dumps(changed))
    with pytest.raises(run.ContractStop, match="manifest"):
        run.prepare_run(benchmark_root, source, tmp_path / "other")


def test_append_only_store_hash_validates_and_rejects_duplicate_keys(tmp_path):
    run = _runmod()
    path = tmp_path / "custody.jsonl"
    store = run.AppendOnlyStore(path, "test-custody")

    store.append({"logical_key": "a", "body": {"secret": "response-not-key"}})
    assert store.by_key()["a"]["body"]["secret"] == "response-not-key"
    with pytest.raises(run.ContractStop, match="duplicate"):
        store.append({"logical_key": "a", "body": {}})

    rows = path.read_text().splitlines()
    tampered = json.loads(rows[-1])
    tampered["body"] = {"changed": True}
    rows[-1] = json.dumps(tampered, sort_keys=True, separators=(",", ":"))
    path.write_text("\n".join(rows) + "\n")
    with pytest.raises(run.ContractStop, match="hash-chain"):
        store.records()

    failures = run.AppendOnlyStore(
        tmp_path / "failures.jsonl", "failures", key_field=None)
    failures.append({"logical_key": "same-item", "error": "first"})
    failures.append({"logical_key": "same-item", "error": "concurrent-second"})
    assert len(failures.records()) == 2


def test_catalog_snapshot_registration_is_immutable_and_requires_eligible_exact_models(
        benchmark_root, tmp_path):
    run = _runmod()
    manifest = _manifest(benchmark_root, tmp_path)
    with pytest.raises(run.ContractStop, match="catalog snapshot"):
        run.run_canary(
            benchmark_root, manifest, tmp_path / "missing-catalog",
            delegate_factory=lambda _spec: pytest.fail("called before catalog"),
            sol_client=FakeSolClient(), offline_fake=True,
        )
    raw = _catalog_raw(manifest)
    run_dir = tmp_path / "run"

    artifact = run.register_catalog_snapshot(
        benchmark_root, manifest, run_dir, raw)
    assert artifact["validated_model_count"] == 6
    assert len(artifact["eligible_providers"]) == 6
    assert run.validate_catalog_snapshot(
        benchmark_root, manifest, run_dir)["raw_canonical_sha256"] == (
            artifact["raw_canonical_sha256"])

    raw["models"][0]["providers"][0]["output_per_m_usd"] = "999"
    with pytest.raises(run.ContractStop, match="eligible"):
        run.register_catalog_snapshot(
            benchmark_root, manifest, tmp_path / "other", raw)


def test_call_level_cache_resume_never_reruns_valid_substantive_output(
        benchmark_root, tmp_path):
    run = _runmod()
    item = run.select_public_items(benchmark_root)[0]
    delegate = FakePilotClient("minimax/minimax-m3")
    calls = run.AppendOnlyStore(tmp_path / "calls.jsonl", "sut-call-cache")
    client = run.CachedSutClient(delegate.slug, delegate, calls)
    messages = [Message("user", item.administrations[0].turns[0].text)]

    with client.item_context(item, "content"):
        first = client.complete(messages, system=item.administrations[0].system)
    with client.item_context(item, "content"):
        resumed = client.complete(messages, system=item.administrations[0].system)

    assert first.text == resumed.text
    assert len(delegate.calls) == 1
    assert len(calls.records()) == 1
    assert calls.records()[0]["logical_key"].endswith(":content:001")


def test_crash_recovery_rebuilds_sut_and_sol_caches_from_full_attempt_custody(
        benchmark_root, tmp_path):
    run = _runmod()
    item = run.select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    message = Message("user", item.administrations[0].turns[0].text)

    class Base:
        def build_payload(self, messages, system):
            return {"model": model, "messages": [
                {"role": m.role, "content": m.content} for m in messages],
                    "max_tokens": 2048}

    class Delegate:
        base_client = Base()

        def complete(self, *_args, **_kwargs):
            pytest.fail("valid paid SUT output was rerun")

    class Ledger:
        def attempt_snapshot(self, attempt):
            assert attempt == 7
            payload = self.payload
            return {"start": {
                "logical_key": f"or:{model}:{item.id}:content:001",
                "requested_model": model,
                "payload_sha256": run.transport_payload_hash(payload),
            }, "finish": {
                "failure": None, "status": 200, "returned_model": model,
                "response_sha256": run.value_sha256(self.body),
                "booked_usd": "0.001", "cost_basis": "reported",
                "prompt_tokens": 10, "completion_tokens": 3,
            }}

    ledger = Ledger()
    ledger.payload = Delegate.base_client.build_payload([message], None)
    ledger.body = {
        "model": model,
        "choices": [{"message": {"content": "custodied valid response"}}],
        "usage": {"cost": 0.001, "prompt_tokens": 10,
                  "completion_tokens": 3},
    }
    attempts = run.AppendOnlyStore(
        tmp_path / "or-attempts.jsonl", "or-attempts", key_field="attempt_id")
    attempts.append({
        "logical_key": f"or:{model}:{item.id}:content:001", "attempt_id": 7,
        "status": 200, "body": ledger.body,
        "body_sha256": run.value_sha256(ledger.body),
    })
    sut = run.CachedSutClient(
        model, Delegate(),
        run.AppendOnlyStore(tmp_path / "calls.jsonl", "sut-call-cache"),
        attempt_custody=attempts, ledger=ledger,
    )
    with sut.item_context(item, "content"):
        assert sut.complete([message]).text == "custodied valid response"

    route_key = f"sol:classifier:{model}:{item.id}:001"
    states = ["refused", "complied"]
    prompt, schema = run.classifier_contract_payload(
        item.design, f"{item.id}:route:001", states, "assistant")
    sol_attempts = run.AppendOnlyStore(
        tmp_path / "sol-attempts.jsonl", "sol-attempts", key_field="attempt_id")
    sol_attempts.append({
        "logical_key": route_key, "attempt_id": 4, "prompt": prompt,
        "schema": schema, "final_text": '{"state":"refused"}',
        "trace_jsonl": '{"type":"turn.completed","usage":{}}\n',
        "stderr": "", "returncode": 0, "error_class": None,
        "payload_sha256": run.text_sha256(prompt),
        "schema_sha256": run.value_sha256(schema),
        "trace_sha256": run.text_sha256(
            '{"type":"turn.completed","usage":{}}\n'),
        "response_sha256": run.text_sha256('{"state":"refused"}'),
        "error_sha256": None, "cli_version": "fake", "usage": {},
    })

    class SolLedger:
        def attempt_snapshot(self, attempt):
            assert attempt == 4
            return {"start": {
                "logical_key": route_key,
                "payload_sha256": run.text_sha256(prompt),
                "schema_sha256": run.value_sha256(schema),
            }, "finish": {
                "valid": True, "error_class": None,
                "trace_sha256": run.text_sha256(
                    '{"type":"turn.completed","usage":{}}\n'),
                "response_sha256": run.text_sha256('{"state":"refused"}'),
                "cli_version": "fake", "usage": {},
            }}

    class NoSol:
        ledger = SolLedger()

        def classify_state(self, *_args, **_kwargs):
            pytest.fail("valid Sol route was rerun")

    routes = run.AppendOnlyStore(tmp_path / "routes.jsonl", "sol-routing-cache")
    classifier = run.CachedSolClassifier(
        model, NoSol(), routes, attempt_custody=sol_attempts,
        ledger=SolLedger())
    with classifier.item_context(item):
        assert classifier("assistant", states, item.design) == "refused"
    assert routes.get(route_key)["recovered_from_attempt_id"] == 4


def test_design05_malformed_allocation_gets_only_exact_same_key_validator_replay(
        benchmark_root, tmp_path):
    run = _runmod()
    item = next(i for i in run.select_public_items(benchmark_root)
                if i.design == "05-ordoamoris")

    class ReplayDelegate(FakePilotClient):
        def __init__(self, slug):
            super().__init__(slug)
            self.invocations = []

        def complete(self, logical_key, messages, system=None,
                     response_validator=None):
            self.invocations.append((logical_key, [(m.role, m.content) for m in messages],
                                     system, response_validator))
            invalid = ModelResponse("not an allocation", self.slug,
                                    self.slug.split("/", 1)[0])
            valid = self.mock.complete(messages, system=system)
            body = {"model": self.slug, "usage": {"cost": 0.1},
                    "choices": [{"message": {"content": valid.text}}]}
            # The registered runtime owns replay; this fake confirms the validator is
            # supplied and simulates its byte-identical second request.
            assert response_validator(invalid, {**body, "choices": [
                {"message": {"content": invalid.text}}]}) is False
            assert response_validator(valid, body) is True
            self.invocations.append((logical_key, [(m.role, m.content) for m in messages],
                                     system, response_validator))
            return _PilotResult(valid, body, {"messages": self.invocations[0][1]}, (1, 2))

    delegate = ReplayDelegate("minimax/minimax-m3")
    client = run.CachedSutClient(
        delegate.slug, delegate,
        run.AppendOnlyStore(tmp_path / "calls.jsonl", "sut-call-cache"),
    )
    allocation = run.run_design05_allocation(item, client)

    assert allocation["ok"] is True
    assert allocation["attempt_ids"] == [1, 2]
    assert delegate.invocations[0][:3] == delegate.invocations[1][:3]
    assert delegate.invocations[0][0].endswith(":allocation:001")


def test_classifier_is_strictly_sol_routed_and_cached(benchmark_root, tmp_path):
    run = _runmod()
    item = next(i for i in run.select_public_items(benchmark_root)
                if i.design == "02-twomasters")
    sol = FakeSolClient()
    routes = run.AppendOnlyStore(tmp_path / "routes.jsonl", "sol-routing-cache")
    classifier = run.CachedSolClassifier("minimax/minimax-m3", sol, routes)

    with classifier.item_context(item):
        first = classifier("assistant text", ["refused", "complied"], item.design)
    with classifier.item_context(item):
        second = classifier("assistant text", ["refused", "complied"], item.design)

    assert first == second == "refused"
    assert len(sol.calls) == 1
    assert len(routes.records()) == 1
    assert routes.records()[0]["state"] == "refused"


def test_full_fake_surface_has_exact_geometry_resume_and_concurrency(
        benchmark_root, tmp_path, monkeypatch):
    run = _runmod()
    # Persistence behavior is covered separately; avoid thousands of physical syncs
    # while still exercising all 5,886 logical calls and 2,064 outputs here.
    monkeypatch.setattr(run.os, "fsync", lambda _fd: None)
    manifest = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "20260714-open6-sol1"
    _register_catalog(run, benchmark_root, manifest, run_dir)
    tracker = ConcurrencyTracker()
    delegates = {}
    item_map = {item.id: item for item in run.select_public_items(benchmark_root)}

    def delegate_factory(spec):
        client = FakePilotClient(spec.slug, tracker=tracker, item_map=item_map)
        delegates[spec.slug] = client
        return client

    sol = FakeSolClient()
    summary = run.run_surface(
        benchmark_root, manifest, run_dir,
        delegate_factory=delegate_factory, sol_client=sol, max_workers=2,
        offline_fake=True,
    )

    assert summary["complete_records"] == 2064
    assert summary["expected_records"] == 2064
    assert summary["complete"] is True
    assert sum(len(client.calls) for client in delegates.values()) == 5886
    assert len(sol.calls) == 1722
    assert tracker.max_active == 2
    assert all(value == 1 for value in tracker.max_by_model.values())
    records = run.load_execution_records(run_dir / "executions.jsonl",
                                         benchmark_root, manifest)
    assert len(records) == 2064
    assert len({(r["item_id"], r["model"]) for r in records}) == 2064

    resumed = run.run_surface(
        benchmark_root, manifest, run_dir,
        delegate_factory=lambda spec: pytest.fail(f"reran {spec.slug}"),
        sol_client=sol, max_workers=2, offline_fake=True,
    )
    assert resumed["new_records"] == 0
    assert len(sol.calls) == 1722


def test_promoted_first_item_canary_is_reused_by_full_run(
        benchmark_root, tmp_path, monkeypatch):
    run = _runmod()
    monkeypatch.setattr(run.os, "fsync", lambda _fd: None)
    manifest = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "20260714-open6-sol1"
    _register_catalog(run, benchmark_root, manifest, run_dir)
    delegates = {}
    item_map = {item.id: item for item in run.select_public_items(benchmark_root)}

    def factory(spec):
        return delegates.setdefault(
            spec.slug, FakePilotClient(spec.slug, item_map=item_map))

    canary = run.run_canary(
        benchmark_root, manifest, run_dir, delegate_factory=factory,
        sol_client=FakeSolClient(), max_workers=2, offline_fake=True,
    )
    before = sum(len(client.calls) for client in delegates.values())
    assert canary["complete_records"] == 6

    full = run.run_surface(
        benchmark_root, manifest, run_dir, delegate_factory=factory,
        sol_client=FakeSolClient(), max_workers=2, offline_fake=True,
    )
    assert full["complete_records"] == 2064
    assert sum(len(client.calls) for client in delegates.values()) == 5886
    assert before == 6


def test_status_and_checkpoint_cli_are_offline_and_hash_validated(
        benchmark_root, tmp_path):
    run = _runmod()
    manifest = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "20260714-open6-sol1"
    run.prepare_run(benchmark_root, manifest, run_dir)

    command = [
        sys.executable, "-m", "walkworthy.open6_sol1_run", "checkpoint",
        "--benchmark-root", str(benchmark_root), "--manifest", str(manifest),
        "--run-dir", str(run_dir),
    ]
    proc = subprocess.run(command, cwd=Path(run.__file__).resolve().parents[1],
                          text=True, capture_output=True, check=False)

    assert proc.returncode == 0, proc.stderr
    status = json.loads(proc.stdout)
    assert status["complete_records"] == 0
    assert status["openrouter_attempts"] == 0
    checkpoints = run.AppendOnlyStore(run_dir / "checkpoints.jsonl", "checkpoints")
    assert len(checkpoints.records()) == 1
