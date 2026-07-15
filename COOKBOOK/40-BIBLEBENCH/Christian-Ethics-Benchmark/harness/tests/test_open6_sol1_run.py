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


def test_catalog_revalidation_is_append_only_with_same_roster_and_ceilings(
        benchmark_root, tmp_path):
    run = _runmod()
    manifest = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "run"
    raw = _catalog_raw(manifest)
    run.register_catalog_snapshot(benchmark_root, manifest, run_dir, raw)
    frozen_bytes = (run_dir / run.CATALOG_SNAPSHOT_NAME).read_bytes()

    recovered = _catalog_raw(manifest)
    recovered["fetched_at"] = "2026-07-14T13:00:00Z"
    first = run.register_catalog_revalidation(
        benchmark_root, manifest, run_dir, recovered,
        recovery_trigger="provider_recovery")
    recovered["fetched_at"] = "2026-07-14T14:00:00Z"
    second = run.register_catalog_revalidation(
        benchmark_root, manifest, run_dir, recovered,
        recovery_trigger="oauth_recovery")

    assert first["logical_key"] == "catalog-revalidation:000001"
    assert second["logical_key"] == "catalog-revalidation:000002"
    assert (run_dir / run.CATALOG_SNAPSHOT_NAME).read_bytes() == frozen_bytes
    assert len(run.validate_catalog_revalidations(
        benchmark_root, manifest, run_dir)) == 2

    invalid = _catalog_raw(manifest)
    target = invalid["models"][0]
    target["providers"][0]["input_per_m_usd"] = "999"
    target["providers"][0]["output_per_m_usd"] = "999"
    with pytest.raises(run.ContractStop, match="eligible"):
        run.register_catalog_revalidation(
            benchmark_root, manifest, run_dir, invalid,
            recovery_trigger="provider_recovery")
    assert len(run.validate_catalog_revalidations(
        benchmark_root, manifest, run_dir)) == 2


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


def test_inflight_attempts_finish_from_valid_custody_without_rerun(
        benchmark_root, tmp_path):
    run = _runmod()
    item = run.select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    message = Message("user", item.administrations[0].turns[0].text)
    logical_key = f"or:{model}:{item.id}:content:001"

    class Base:
        def build_payload(self, messages, system):
            return {"model": model, "messages": [
                {"role": row.role, "content": row.content} for row in messages],
                    "max_tokens": 2048}

    body = {
        "model": model,
        "choices": [{"message": {"content": "custodied valid response"}}],
        "usage": {"cost": 0.001, "prompt_tokens": 10,
                  "completion_tokens": 3},
    }
    payload = Base().build_payload([message], None)

    class InflightOpenRouterLedger:
        def __init__(self):
            self.starts = {7: {
                "logical_key": logical_key, "requested_model": model,
                "payload_sha256": run.transport_payload_hash(payload),
            }}
            self.finishes = {}
            self.finished = []

        def snapshot(self):
            return {"attempts": 7}

        def attempt_snapshot(self, attempt):
            return {"start": self.starts[attempt],
                    "finish": self.finishes.get(attempt)}

        def finish(self, attempt, status, response_body, **kwargs):
            self.finished.append((attempt, status, response_body, kwargs))
            assert attempt == 7
            assert status == 200
            assert response_body == body
            self.finishes[attempt] = {
                "failure": None, "status": 200, "returned_model": model,
                "response_sha256": run.value_sha256(body),
                "booked_usd": "0.001", "cost_basis": "reported",
                "prompt_tokens": 10, "completion_tokens": 3,
            }

    class NoOpenRouterRerun:
        base_client = Base()

        def complete(self, *_args, **_kwargs):
            pytest.fail("valid custodied OpenRouter response was rerun")

    or_custody = run.AppendOnlyStore(
        tmp_path / "or-custody.jsonl", "or-custody", key_field="attempt_id")
    or_custody.append({
        "logical_key": logical_key, "attempt_id": 7, "status": 200,
        "body": body, "body_sha256": run.value_sha256(body),
    })
    or_ledger = InflightOpenRouterLedger()
    calls = run.AppendOnlyStore(tmp_path / "calls.jsonl", "sut-call-cache")
    sut = run.CachedSutClient(
        model, NoOpenRouterRerun(), calls,
        attempt_custody=or_custody, ledger=or_ledger,
    )
    with sut.item_context(item, "content"):
        assert sut.complete([message]).text == "custodied valid response"
    assert [row[0] for row in or_ledger.finished] == [7]
    assert calls.get(logical_key)["recovered_from_attempt_id"] == 7

    states = ["refused", "complied"]
    route_key = f"sol:classifier:{model}:{item.id}:001"
    prompt, schema = run.classifier_contract_payload(
        item.design, f"{item.id}:route:001", states, "assistant")
    final_text = '{"state":"refused"}'
    trace_text = '{"type":"turn.completed","usage":{}}\n'

    class InflightSolLedger:
        def __init__(self):
            self.starts = {4: {
                "logical_key": route_key,
                "payload_sha256": run.text_sha256(prompt),
                "schema_sha256": run.value_sha256(schema),
            }}
            self.finishes = {}
            self.finished = []

        def snapshot(self):
            return {"attempts": 4}

        def attempt_snapshot(self, attempt):
            return {"start": self.starts[attempt],
                    "finish": self.finishes.get(attempt)}

        def finish(self, attempt, **kwargs):
            self.finished.append((attempt, kwargs))
            assert attempt == 4
            assert kwargs["valid"] is True
            self.finishes[attempt] = {
                "valid": True, "error_class": None,
                "trace_sha256": kwargs["trace_sha256"],
                "response_sha256": kwargs["response_sha256"],
                "cli_version": kwargs["cli_version"],
                "usage": kwargs["usage"],
            }

    sol_custody = run.AppendOnlyStore(
        tmp_path / "sol-custody.jsonl", "sol-custody", key_field="attempt_id")
    sol_custody.append({
        "logical_key": route_key, "attempt_id": 4, "prompt": prompt,
        "schema": schema, "final_text": final_text, "trace_jsonl": trace_text,
        "stderr": "", "returncode": 0, "error_class": None,
        "payload_sha256": run.text_sha256(prompt),
        "schema_sha256": run.value_sha256(schema),
        "trace_sha256": run.text_sha256(trace_text),
        "response_sha256": run.text_sha256(final_text),
        "error_sha256": None, "cli_version": "fake", "usage": {},
    })
    sol_ledger = InflightSolLedger()

    class NoSolRerun:
        def classify_state(self, *_args, **_kwargs):
            pytest.fail("valid custodied Sol response was rerun")

    routes = run.AppendOnlyStore(tmp_path / "routes.jsonl", "sol-routing-cache")
    classifier = run.CachedSolClassifier(
        model, NoSolRerun(), routes,
        attempt_custody=sol_custody, ledger=sol_ledger,
    )
    with classifier.item_context(item):
        assert classifier("assistant", states, item.design) == "refused"
    assert [row[0] for row in sol_ledger.finished] == [4]
    assert routes.get(route_key)["recovered_from_attempt_id"] == 4


def test_missing_inflight_custody_is_closed_before_one_exact_replay(
        benchmark_root, tmp_path):
    run = _runmod()
    item = run.select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    message = Message("user", item.administrations[0].turns[0].text)
    logical_key = f"or:{model}:{item.id}:content:001"

    class Base:
        def build_payload(self, messages, system):
            return {"model": model, "messages": [
                {"role": row.role, "content": row.content} for row in messages],
                    "max_tokens": 2048}

    payload = Base().build_payload([message], None)

    class InflightOpenRouterLedger:
        def __init__(self):
            self.finish_calls = []
            self.finish_record = None

        def snapshot(self):
            return {"attempts": 1}

        def attempt_snapshot(self, attempt):
            if attempt != 1:
                raise run.ContractStop("unknown attempt")
            return {"start": {
                "logical_key": logical_key, "requested_model": model,
                "payload_sha256": run.transport_payload_hash(payload),
            }, "finish": self.finish_record}

        def finish(self, attempt, status, body, **kwargs):
            self.finish_calls.append((attempt, status, body, kwargs))
            self.finish_record = {"failure": "custody_failure"}

    class ExactOpenRouterReplay:
        base_client = Base()

        def __init__(self):
            self.calls = 0

        def complete(self, key, messages, system=None, response_validator=None):
            self.calls += 1
            assert key == logical_key
            assert self.base_client.build_payload(messages, system) == payload
            response = ModelResponse("exact replay", model, model.split("/", 1)[0])
            body = {
                "model": model,
                "choices": [{"message": {"content": response.text}}],
                "usage": {"cost": 0.001, "prompt_tokens": 10,
                          "completion_tokens": 3},
            }
            return _PilotResult(response, body, payload, (2,))

    or_ledger = InflightOpenRouterLedger()
    delegate = ExactOpenRouterReplay()
    calls = run.AppendOnlyStore(tmp_path / "calls.jsonl", "sut-call-cache")
    sut = run.CachedSutClient(
        model, delegate, calls,
        attempt_custody=run.AppendOnlyStore(
            tmp_path / "empty-or-custody.jsonl", "or-custody",
            key_field="attempt_id"),
        ledger=or_ledger,
    )
    with sut.item_context(item, "content"):
        assert sut.complete([message]).text == "exact replay"
    assert delegate.calls == 1
    assert or_ledger.finish_calls == [(1, None, {}, {
        "failure_override": "custody_failure",
        "error_detail": {"type": "missing_attempt_custody"},
    })]
    assert calls.get(logical_key)["attempt_ids"] == [2]

    states = ["refused", "complied"]
    route_key = f"sol:classifier:{model}:{item.id}:001"
    prompt, schema = run.classifier_contract_payload(
        item.design, f"{item.id}:route:001", states, "assistant")

    class InflightSolLedger:
        def __init__(self):
            self.finish_calls = []
            self.finish_record = None

        def snapshot(self):
            return {"attempts": 1}

        def attempt_snapshot(self, attempt):
            if attempt != 1:
                raise run.ContractStop("unknown attempt")
            return {"start": {
                "logical_key": route_key,
                "payload_sha256": run.text_sha256(prompt),
                "schema_sha256": run.value_sha256(schema),
            }, "finish": self.finish_record}

        def finish(self, attempt, **kwargs):
            self.finish_calls.append((attempt, kwargs))
            self.finish_record = {
                "valid": False, "error_class": kwargs["error_class"]}

    class ExactSolReplay(FakeSolClient):
        def classify_state(self, key, design, opaque_key,
                           allowed_states, assistant_response):
            result = super().classify_state(
                key, design, opaque_key, allowed_states, assistant_response)
            result.prompt = prompt
            result.schema = schema
            result.attempt_ids = (2,)
            return result

    sol_ledger = InflightSolLedger()
    sol = ExactSolReplay()
    routes = run.AppendOnlyStore(tmp_path / "routes.jsonl", "sol-routing-cache")
    classifier = run.CachedSolClassifier(
        model, sol, routes,
        attempt_custody=run.AppendOnlyStore(
            tmp_path / "empty-sol-custody.jsonl", "sol-custody",
            key_field="attempt_id"),
        ledger=sol_ledger,
    )
    with classifier.item_context(item):
        assert classifier("assistant", states, item.design) == "refused"
    assert len(sol.calls) == 1
    assert sol_ledger.finish_calls == [(1, {
        "valid": False, "error_class": "interrupted",
        "trace_sha256": None, "response_sha256": None,
        "error_sha256": run.text_sha256("interrupted"),
        "cli_version": "crash-recovery", "usage": {},
    })]
    assert routes.get(route_key)["attempt_ids"] == [2]


def test_inflight_custodied_validator_defect_is_finished_then_replayed(
        benchmark_root, tmp_path):
    run = _runmod()
    item = run.select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    message = Message("user", item.administrations[0].turns[0].text)
    logical_key = f"or:{model}:{item.id}:content:001"

    class Base:
        def build_payload(self, messages, system):
            return {"model": model, "messages": [
                {"role": row.role, "content": row.content} for row in messages],
                    "max_tokens": 2048}

    payload = Base().build_payload([message], None)
    body = {
        "model": model,
        "choices": [{"message": {"content": "custodied response"}}],
        "usage": {"cost": 0.001, "prompt_tokens": 10,
                  "completion_tokens": 3},
    }

    class Ledger:
        def __init__(self):
            self.finish_record = None
            self.finish_calls = []

        def snapshot(self):
            return {"attempts": 1}

        def attempt_snapshot(self, attempt):
            return {"start": {
                "logical_key": logical_key, "requested_model": model,
                "payload_sha256": run.transport_payload_hash(payload),
            }, "finish": self.finish_record}

        def finish(self, attempt, status, response_body, **kwargs):
            self.finish_calls.append((attempt, status, response_body, kwargs))
            self.finish_record = {
                "failure": "malformed", "status": status,
                "returned_model": model,
                "response_sha256": run.value_sha256(response_body),
            }

    class Replay:
        base_client = Base()

        def __init__(self):
            self.calls = 0

        def complete(self, *_args, **_kwargs):
            self.calls += 1
            response = ModelResponse("exact replay", model, model.split("/", 1)[0])
            return _PilotResult(response, {
                **body,
                "choices": [{"message": {"content": response.text}}],
            }, payload, (2,))

    custody = run.AppendOnlyStore(
        tmp_path / "or-invalid-custody.jsonl", "or-custody",
        key_field="attempt_id")
    custody.append({
        "logical_key": logical_key, "attempt_id": 1, "status": 200,
        "body": body, "body_sha256": run.value_sha256(body),
    })
    ledger = Ledger()
    delegate = Replay()
    calls = run.AppendOnlyStore(tmp_path / "calls-invalid.jsonl", "sut-call-cache")
    sut = run.CachedSutClient(
        model, delegate, calls, attempt_custody=custody, ledger=ledger)

    def validator(_response, _body):
        raise ValueError("registered validator rejected output")

    with sut.item_context(item, "content"):
        assert sut.complete([message], response_validator=validator).text == "exact replay"
    assert delegate.calls == 1
    assert ledger.finish_calls[0][3] == {
        "failure_override": "malformed",
        "error_detail": {
            "type": "ValueError",
            "message": "registered validator rejected output",
        },
    }
    assert calls.get(logical_key)["attempt_ids"] == [1, 2]


def test_crash_after_two_finished_openrouter_failures_terminalizes_without_third_call(
        benchmark_root, tmp_path):
    run = _runmod()
    items = [item for item in run.select_public_items(benchmark_root)
             if item.design == "01-goodsamaritan"][:2]
    first, second = items
    spec = run.SUT_SPECS[0]
    source_key = f"or:{spec.slug}:{first.id}:content:001"

    class RecoveryDelegate(FakePilotClient):
        @property
        def base_client(self):
            return self

        def build_payload(self, messages, system):
            return {
                "model": self.slug,
                "messages": [{"role": row.role, "content": row.content}
                             for row in messages],
                "max_tokens": 2048,
            }

        def complete(self, logical_key, *args, **kwargs):
            if logical_key == source_key:
                pytest.fail("a forbidden third OpenRouter call was attempted")
            return super().complete(logical_key, *args, **kwargs)

    delegate = RecoveryDelegate(spec.slug)
    admin = first.administrations[0]
    payload = delegate.build_payload(
        [Message("user", admin.turns[0].text)], admin.system)
    bodies = [{"error": "temporary-1"}, {"error": "temporary-2"}]

    class FinishedLedger:
        def snapshot(self):
            return {"attempts": 2}

        def attempt_snapshot(self, attempt):
            body = bodies[attempt - 1]
            return {
                "start": {
                    "logical_key": source_key,
                    "requested_model": spec.slug,
                    "payload_sha256": run.transport_payload_hash(payload),
                },
                "finish": {
                    "status": 500,
                    "failure": "http_failure",
                    "returned_model": None,
                    "response_sha256": run.value_sha256(body),
                },
            }

    custody = run.AppendOnlyStore(
        tmp_path / "or-finished-custody.jsonl", "or-custody",
        key_field="attempt_id")
    for attempt, body in enumerate(bodies, 1):
        custody.append({
            "logical_key": source_key, "attempt_id": attempt,
            "status": 500, "body": body,
            "body_sha256": run.value_sha256(body),
        })
    stores = run._stores(tmp_path / "or-finished-run")

    assert run._run_model(
        spec, items, lambda _spec: delegate, FakeSolClient(), stores,
        {spec.slug}, sut_attempt_custody=custody,
        openrouter_ledger=FinishedLedger()) == 1
    assert stores["executions"].records()[0]["item_id"] == second.id
    terminal = stores["terminal_unresolved"].records()[0]
    assert terminal["source_role"] == "sut"
    assert terminal["source_logical_key"] == source_key
    assert terminal["attempt_ids"] == [1, 2]
    assert all(call["logical_key"] != source_key for call in delegate.calls)


def test_crash_after_two_finished_classifier_failures_terminalizes_without_third_call(
        benchmark_root, tmp_path):
    run = _runmod()
    items = [item for item in run.select_public_items(benchmark_root)
             if item.design == "02-twomasters"][:2]
    first, second = items
    spec = run.SUT_SPECS[0]
    source_key = f"sol:classifier:{spec.slug}:{first.id}:001"
    delegate = FakePilotClient(spec.slug)
    probe = FakePilotClient(spec.slug)
    admin = first.administrations[0]
    first_response = probe.complete(
        "probe", [Message("user", admin.turns[0].text)],
        system=admin.system).response.text
    states = list(admin.turns[1].branches)
    prompt, schema = run.classifier_contract_payload(
        first.design, f"{first.id}:route:001", states, first_response)

    class FinishedLedger:
        def snapshot(self):
            return {"attempts": 2}

        def attempt_snapshot(self, attempt):
            return {
                "start": {
                    "logical_key": source_key,
                    "payload_sha256": run.text_sha256(prompt),
                    "schema_sha256": run.value_sha256(schema),
                },
                "finish": {
                    "valid": False,
                    "error_class": "schema_invalid",
                    "trace_sha256": run.text_sha256(""),
                    "response_sha256": None,
                    "cli_version": "fake",
                    "usage": {},
                },
            }

    class RecoverySol(FakeSolClient):
        def __init__(self):
            super().__init__()
            self.ledger = FinishedLedger()

        def classify_state(self, logical_key, *args, **kwargs):
            if logical_key == source_key:
                pytest.fail("a forbidden third Sol classifier call was attempted")
            return super().classify_state(logical_key, *args, **kwargs)

    custody = run.AppendOnlyStore(
        tmp_path / "sol-finished-custody.jsonl", "sol-custody",
        key_field="attempt_id")
    for attempt in (1, 2):
        custody.append({
            "logical_key": source_key, "attempt_id": attempt,
            "prompt": prompt, "schema": schema, "final_text": "",
            "trace_jsonl": "", "stderr": "", "returncode": 0,
            "error_class": "schema_invalid",
            "payload_sha256": run.text_sha256(prompt),
            "schema_sha256": run.value_sha256(schema),
            "trace_sha256": run.text_sha256(""),
            "response_sha256": None,
            "error_sha256": run.value_sha256({"type": "schema_invalid"}),
            "cli_version": "fake", "usage": {},
        })
    stores = run._stores(tmp_path / "sol-finished-run")
    sol = RecoverySol()

    assert run._run_model(
        spec, items, lambda _spec: delegate, sol, stores, {spec.slug},
        sol_attempt_custody=custody) == 1
    assert stores["executions"].records()[0]["item_id"] == second.id
    terminal = stores["terminal_unresolved"].records()[0]
    assert terminal["source_role"] == "classifier"
    assert terminal["source_logical_key"] == source_key
    assert terminal["attempt_ids"] == [1, 2]
    assert all(call[0] != source_key for call in sol.calls)


def test_classifier_attempt_custody_and_routes_are_bijective():
    run = _runmod()
    custody = [
        {"attempt_id": 1, "logical_key": "sol:classifier:m:item-a:001"},
        {"attempt_id": 2, "logical_key": "sol:classifier:m:item-a:001"},
        {"attempt_id": 3, "logical_key": "sol:classifier:m:item-b:001"},
    ]
    routes = [
        {"logical_key": "sol:classifier:m:item-a:001", "attempt_ids": [1, 2]},
        {"logical_key": "sol:classifier:m:item-b:001", "attempt_ids": [3]},
    ]

    assert run._audit_classifier_attempt_bijection(routes, custody) is True
    with pytest.raises(run.ContractStop, match="bijection"):
        run._audit_classifier_attempt_bijection(routes, custody + [{
            "attempt_id": 4, "logical_key": "sol:classifier:m:item-c:001",
        }])
    with pytest.raises(run.ContractStop, match="bijection"):
        run._audit_classifier_attempt_bijection(
            routes + [{"logical_key": "sol:classifier:m:item-c:001",
                       "attempt_ids": [3]}], custody)

    mixed_custody = custody + [{
        "attempt_id": 4, "logical_key": "sol:judge:batch-000001",
    }]
    assert run._audit_classifier_attempt_bijection(routes, mixed_custody) is True
    with pytest.raises(run.ContractStop, match="unregistered Sol attempt prefix"):
        run._audit_classifier_attempt_bijection(routes, custody + [{
            "attempt_id": 4, "logical_key": "sol:other:batch-000001",
        }])


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


def test_terminal_sut_second_failure_is_recorded_and_other_items_continue(
        benchmark_root, tmp_path):
    run = _runmod()
    items = run.select_public_items(benchmark_root)[:2]
    first, second = items
    spec = run.SUT_SPECS[0]
    terminal_sut_key = f"or:{spec.slug}:{first.id}:content:001"

    class TerminalLedger:
        def __init__(self):
            self.starts = {}
            self.finishes = {}

        def snapshot(self):
            return {"attempts": len(self.starts)}

        def attempt_snapshot(self, attempt):
            return {"start": self.starts[attempt],
                    "finish": self.finishes.get(attempt)}

        def record_terminal(self):
            for attempt in (1, 2):
                self.starts[attempt] = {
                    "logical_key": terminal_sut_key,
                    "requested_model": spec.slug,
                    "payload_sha256": "a" * 64,
                }
                self.finishes[attempt] = {"failure": "http_failure"}

    ledger = TerminalLedger()

    class TerminalThenHealthy(FakePilotClient):
        def __init__(self):
            super().__init__(spec.slug)
            self.ledger = ledger

        def complete(self, logical_key, messages, system=None,
                     response_validator=None):
            if logical_key == terminal_sut_key:
                self.ledger.record_terminal()
                raise run.ThreadStop(
                    f"OpenRouter second failure for {logical_key}: http_failure")
            return super().complete(
                logical_key, messages, system=system,
                response_validator=response_validator)

    delegate = TerminalThenHealthy()
    stores = run._stores(tmp_path / "run")
    new = run._run_model(
        spec, items, lambda _spec: delegate, FakeSolClient(), stores,
        {spec.slug},
    )

    assert new == 1
    assert [row["item_id"] for row in stores["executions"].records()] == [second.id]
    terminal = stores["terminal_unresolved"].records()
    assert len(terminal) == 1
    assert {key: terminal[0][key] for key in (
        "schema_version", "logical_key", "status", "item_id", "design",
        "model", "source_role", "source_logical_key", "phase", "call_index",
        "failure_class", "attempt_ids",
    )} == {
        "schema_version":
            "walkworthy.open6-sol1.terminal-unresolved-item-model.v2",
        "logical_key": f"item:{spec.slug}:{first.id}",
        "status": "terminal_unresolved", "item_id": first.id,
        "design": first.design, "model": spec.slug,
        "source_role": "sut", "source_logical_key": terminal_sut_key,
        "phase": "content",
        "call_index": 1, "failure_class": "http_failure",
        "attempt_ids": [1, 2],
    }
    assert stores["failures"].records() == []
    assert run._run_model(
        spec, items, lambda _spec: pytest.fail("terminal/completed work reran"),
        FakeSolClient(), stores, {spec.slug}) == 0


def test_deepseek_exception_third_failure_is_a_permanent_systemic_stop(
        benchmark_root, tmp_path):
    run = _runmod()
    item = run.select_public_items(benchmark_root)[0]
    spec = next(row for row in run.SUT_SPECS
                if row.slug == "deepseek/deepseek-v4-pro")
    logical_key = (
        f"or:{spec.slug}:{item.id}:content:001")

    class ExceptionLedger:
        deepseek_exception = {"logical_key": logical_key}

        def attempt_snapshot(self, attempt):
            return {
                "start": {
                    "logical_key": logical_key,
                    "requested_model": spec.slug,
                    "payload_sha256": "a" * 64,
                },
                "finish": {
                    "failure": "http_failure",
                    "status": 404,
                },
            }

        def snapshot(self):
            return {"attempts": 3}

    custody = run.AppendOnlyStore(
        tmp_path / "custody.jsonl", "openrouter-attempt-custody",
        key_field="attempt_id")
    for attempt_id in (1, 2, 3):
        custody.append({
            "attempt_id": attempt_id,
            "logical_key": logical_key,
            "status": 404,
            "body": {"error": {"message": "model not found"}},
        })

    with pytest.raises(run.UnattendedStop, match="unavailability|HTTP 404"):
        run._terminal_record_from_stop(
            item, spec,
            run.ThreadStop(
                f"OpenRouter exceptional failure for {logical_key}: "
                "http_failure"),
            ExceptionLedger(), None, custody, None)


def test_terminal_sol_classifier_second_failure_marks_item_missing_and_continues(
        benchmark_root, tmp_path):
    run = _runmod()
    items = [item for item in run.select_public_items(benchmark_root)
             if item.design == "02-twomasters"][:2]
    first, second = items
    spec = run.SUT_SPECS[0]
    terminal_key = f"sol:classifier:{spec.slug}:{first.id}:001"

    class SolLedger:
        def __init__(self):
            self.starts = {}
            self.finishes = {}

        def snapshot(self):
            return {"attempts": len(self.starts)}

        def attempt_snapshot(self, attempt):
            return {"start": self.starts[attempt],
                    "finish": self.finishes[attempt]}

        def record_terminal(self):
            for attempt in (1, 2):
                self.starts[attempt] = {
                    "logical_key": terminal_key,
                    "payload_sha256": "a" * 64,
                    "schema_sha256": "b" * 64,
                }
                self.finishes[attempt] = {
                    "valid": False, "error_class": "schema_invalid"}

    ledger = SolLedger()

    class TerminalThenHealthySol(FakeSolClient):
        def __init__(self):
            super().__init__()
            self.ledger = ledger
            self.attempt_sink = None

        def classify_state(self, logical_key, design, opaque_key,
                           allowed_states, assistant_response):
            if logical_key == terminal_key:
                self.ledger.record_terminal()
                for attempt in (1, 2):
                    self.attempt_sink({
                        "logical_key": terminal_key, "attempt_id": attempt,
                        "error_class": "schema_invalid", "stderr": "",
                    })
                raise run.ThreadStop(
                    f"Sol second failure for {logical_key}: schema_invalid")
            return super().classify_state(
                logical_key, design, opaque_key, allowed_states,
                assistant_response)

    stores = run._stores(tmp_path / "run-sol-terminal")
    sol_custody = run.AppendOnlyStore(
        tmp_path / "run-sol-terminal" / run.SOL_ATTEMPT_CUSTODY_NAME,
        "sol-attempt-custody", key_field="attempt_id")
    sol = TerminalThenHealthySol()
    sol.attempt_sink = sol_custody.append_sink
    new = run._run_model(
        spec, items, lambda _spec: FakePilotClient(spec.slug),
        sol, stores, {spec.slug},
        sol_attempt_custody=sol_custody,
    )

    assert new == 1
    assert stores["executions"].records()[0]["item_id"] == second.id
    terminal = stores["terminal_unresolved"].records()[0]
    assert terminal["source_role"] == "classifier"
    assert terminal["source_logical_key"] == terminal_key
    assert terminal["phase"] == "classifier"
    assert terminal["attempt_ids"] == [1, 2]


def test_systemic_second_failure_detection_is_narrow_and_fail_closed():
    run = _runmod()
    with pytest.raises(run.UnattendedStop, match="OpenRouter authorization"):
        run._raise_if_systemic_terminal(
            "sut", [{"status": 402, "body": {"error": "credits"}}])
    with pytest.raises(run.UnattendedStop, match="Sol OAuth quota"):
        run._raise_if_systemic_terminal(
            "classifier", [{"error_class": "cli_failure",
                             "stderr": "Usage limit exceeded"}])
    with pytest.raises(run.UnattendedStop, match="unregistered Sol CLI"):
        run._raise_if_systemic_terminal(
            "classifier", [{"error_class": "cli_failure", "stderr": ""}])
    assert run._raise_if_systemic_terminal(
        "sut", [{"status": 500, "body": {"error": "temporary"}}]) is None
    assert run._raise_if_systemic_terminal(
        "classifier", [{"error_class": "schema_invalid", "stderr": ""}]) is None


def test_sol_attempt_role_accepts_classifier_and_judge_but_rejects_unknown():
    run = _runmod()
    assert run._registered_sol_attempt_role("sol:classifier:m:item:001") == "classifier"
    assert run._registered_sol_attempt_role("sol:judge:batch:001") == "judge"
    with pytest.raises(run.ContractStop, match="unregistered Sol attempt prefix"):
        run._registered_sol_attempt_role("sol:other:key")


def test_terminal_attempt_audit_requires_exact_ledger_finish_and_custody_ids():
    run = _runmod()
    model = "minimax/minimax-m3"
    or_key = f"or:{model}:WW-A:content:001"
    sol_key = f"sol:classifier:{model}:WW-B:001"
    prompt = "registered prompt"
    schema = {"type": "object"}
    trace = '{"type":"turn.completed"}\n'
    final_text = ""

    class Ledger:
        def __init__(self, starts, finishes):
            self.starts = starts
            self.finishes = finishes

        def snapshot(self):
            return {"attempts": len(self.starts)}

        def attempt_snapshot(self, attempt):
            return {"start": self.starts[attempt],
                    "finish": self.finishes.get(attempt)}

    or_ledger = Ledger({
        1: {"logical_key": or_key, "requested_model": model},
        2: {"logical_key": or_key, "requested_model": model},
    }, {
        1: {"failure": "http_failure"},
        2: {"failure": "http_failure"},
    })
    sol_ledger = Ledger({
        1: {"logical_key": sol_key,
            "payload_sha256": run.text_sha256(prompt),
            "schema_sha256": run.value_sha256(schema)},
        2: {"logical_key": sol_key,
            "payload_sha256": run.text_sha256(prompt),
            "schema_sha256": run.value_sha256(schema)},
    }, {
        1: {"valid": False, "error_class": "schema_invalid",
            "trace_sha256": run.text_sha256(trace),
            "response_sha256": None, "cli_version": "fake", "usage": {}},
        2: {"valid": False, "error_class": "schema_invalid",
            "trace_sha256": run.text_sha256(trace),
            "response_sha256": None, "cli_version": "fake", "usage": {}},
    })
    terminal = [{
        "source_role": "sut", "source_logical_key": or_key,
        "model": model, "failure_class": "http_failure",
        "attempt_ids": [1, 2],
    }, {
        "source_role": "classifier", "source_logical_key": sol_key,
        "model": model, "failure_class": "schema_invalid",
        "attempt_ids": [1, 2],
    }]
    or_custody = [
        {"attempt_id": attempt, "logical_key": or_key}
        for attempt in (1, 2)]
    sol_custody = [{
        "attempt_id": attempt, "logical_key": sol_key,
        "prompt": prompt, "schema": schema,
        "payload_sha256": run.text_sha256(prompt),
        "schema_sha256": run.value_sha256(schema),
        "final_text": final_text, "trace_jsonl": trace,
        "response_sha256": None, "trace_sha256": run.text_sha256(trace),
        "error_class": "schema_invalid",
        "cli_version": "fake", "usage": {},
    } for attempt in (1, 2)]

    assert run._audit_terminal_attempt_bijection(
        terminal, or_ledger, sol_ledger, or_custody, sol_custody) is True

    skipped = [dict(terminal[0], attempt_ids=[1, 3]), terminal[1]]
    with pytest.raises(run.ContractStop, match="terminal attempt"):
        run._audit_terminal_attempt_bijection(
            skipped, or_ledger, sol_ledger, or_custody, sol_custody)

    with pytest.raises(run.ContractStop, match="terminal attempt"):
        run._audit_terminal_attempt_bijection(
            terminal, or_ledger, sol_ledger, or_custody,
            sol_custody[:1])

    mismatched = [sol_custody[0], {
        "attempt_id": 2, "logical_key": "sol:classifier:other:WW-B:001",
    }]
    with pytest.raises(run.ContractStop, match="terminal attempt"):
        run._audit_terminal_attempt_bijection(
            terminal, or_ledger, sol_ledger, or_custody, mismatched)

    tampered = [dict(row) for row in sol_custody]
    tampered[1]["trace_sha256"] = "0" * 64
    with pytest.raises(run.ContractStop, match="terminal attempt"):
        run._audit_terminal_attempt_bijection(
            terminal, or_ledger, sol_ledger, or_custody, tampered)

    for omitted_field in ("prompt", "schema"):
        omitted = [dict(row) for row in sol_custody]
        omitted[1].pop(omitted_field)
        with pytest.raises(run.ContractStop, match="terminal attempt"):
            run._audit_terminal_attempt_bijection(
                terminal, or_ledger, sol_ledger, or_custody, omitted)

    tampered_prompt = [dict(row) for row in sol_custody]
    tampered_prompt[1]["prompt"] = prompt + " changed"
    with pytest.raises(run.ContractStop, match="terminal attempt"):
        run._audit_terminal_attempt_bijection(
            terminal, or_ledger, sol_ledger, or_custody, tampered_prompt)

    tampered_schema = [dict(row) for row in sol_custody]
    tampered_schema[1]["schema"] = {"type": "array"}
    with pytest.raises(run.ContractStop, match="terminal attempt"):
        run._audit_terminal_attempt_bijection(
            terminal, or_ledger, sol_ledger, or_custody, tampered_schema)

    mismatched_error = [dict(row) for row in sol_custody]
    mismatched_error[1]["error_class"] = "malformed"
    with pytest.raises(run.ContractStop, match="terminal attempt"):
        run._audit_terminal_attempt_bijection(
            terminal, or_ledger, sol_ledger, or_custody, mismatched_error)


def test_completion_state_distinguishes_terminal_surface_from_full_completion():
    run = _runmod()
    expected = {"item:model:a", "item:model:b"}
    partial = run._completion_state(
        expected, {"item:model:a"}, {"item:model:b"},
        exact_runtime_complete=False, failure_count=0, ledger_integrity=True)
    full = run._completion_state(
        expected, expected, set(), exact_runtime_complete=True,
        failure_count=0, ledger_integrity=True)

    assert partial == {
        "terminal_surface_complete": True,
        "fully_complete": False,
        "complete": False,
    }
    assert full == {
        "terminal_surface_complete": True,
        "fully_complete": True,
        "complete": True,
    }


def test_soft_budget_guard_projects_remaining_exact_models_and_stops_pre_request(
        tmp_path):
    run = _runmod()
    spec = next(row for row in run.SUT_SPECS if row.slug == "z-ai/glm-5.2")
    logical_key = f"or:{spec.slug}:WW-X:content:001"

    class Ledger:
        replay_cap = 295

        def snapshot(self):
            return {
                "booked_usd": run.Decimal("15.00"),
                "replays": 0,
                "inflight_usd": run.Decimal("0"),
                "attempts": 0,
            }

    calls = run.AppendOnlyStore(tmp_path / "calls.jsonl", "sut-call-cache")
    terminal = run.AppendOnlyStore(
        tmp_path / "terminal.jsonl", "terminal-unresolved-sut")
    checkpoints = run.AppendOnlyStore(
        tmp_path / "checkpoints.jsonl", "checkpoints")
    guard = run.SoftBudgetGuard(
        {logical_key}, calls, terminal, Ledger(), checkpoints)

    with pytest.raises(run.BudgetStop, match="soft projected-total"):
        guard.before_request()
    projection = guard.projection()
    ceiling = spec.max_call_usd_for_input(spec.input_envelope)
    assert projection["remaining_nominal_calls_by_model"] == {spec.slug: 1}
    assert projection["remaining_nominal_projection_usd"] == str(ceiling)
    assert projection["unused_replay_slots"] == 295
    assert projection["replay_projection_usd"] == str(ceiling * 295)
    assert projection["projected_total_usd"] == str(
        run.Decimal("15.00") + ceiling * 296)
    assert projection["continue_authorized"] is False
    saved = checkpoints.records()
    assert len(saved) == 1
    assert saved[0]["checkpoint_type"] == "soft_budget_pre_request"
    assert saved[0]["projected_total_usd"] == projection["projected_total_usd"]

    class BlockingGuard:
        def before_request(self):
            raise run.BudgetStop("blocked before transport")

    delegate = FakePilotClient(spec.slug)
    client = run.CachedSutClient(
        spec.slug, delegate,
        run.AppendOnlyStore(tmp_path / "blocked-calls.jsonl", "sut-call-cache"),
        budget_guard=BlockingGuard())
    item = type("Item", (), {"id": "WW-X", "design": "01-truthcost"})()
    with client.item_context(item, "content"):
        with pytest.raises(run.BudgetStop, match="before transport"):
            client.complete([Message("user", "prompt")])
    assert delegate.calls == []


def test_budget_abort_persists_one_resumable_stop_checkpoint_without_failure(
        benchmark_root, tmp_path):
    run = _runmod()
    manifest = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "budget-stop"
    _register_catalog(run, benchmark_root, manifest, run_dir)

    class BudgetBlocked(FakePilotClient):
        def complete(self, *_args, **_kwargs):
            raise run.BudgetStop("registered soft checkpoint stop")

    with pytest.raises(run.BudgetStop, match="soft checkpoint"):
        run.run_surface(
            benchmark_root, manifest, run_dir,
            delegate_factory=lambda spec: BudgetBlocked(spec.slug),
            sol_client=FakeSolClient(), max_workers=2, offline_fake=True,
        )

    checkpoints = run.AppendOnlyStore(
        run_dir / run.CHECKPOINT_NAME, "checkpoints").records()
    stops = [row for row in checkpoints
             if row.get("checkpoint_type") == "resumable_stop"]
    assert len(stops) == 1
    stop = stops[0]
    assert stop["reason_type"] == "BudgetStop"
    assert stop["complete_item_model_keys"] == []
    assert stop["terminal_item_model_keys"] == []
    assert len(stop["missing_item_model_keys"]) == 2064
    assert stop["openrouter"] == {
        "attempts": 0, "replays": 0, "booked_usd": "0",
        "reserved_usd": "0", "inflight_usd": "0",
    }
    assert stop["sol"] == {"attempts": 0, "replays": 0, "inflight": 0}
    assert stop["safest_next_command"][1:4] == [
        "-m", "walkworthy.open6_sol1_run", "checkpoint"]
    assert run._stores(run_dir)["failures"].records() == []


def test_first_worker_abort_signals_peer_workers_before_checkpoint(
        benchmark_root, tmp_path, monkeypatch):
    run = _runmod()
    manifest_path = _manifest(benchmark_root, tmp_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    run_dir = tmp_path / "coordinated-stop"
    _register_catalog(run, benchmark_root, manifest_path, run_dir)
    first_slug = manifest["openrouter"]["models"][0]["slug"]
    peer_started = run.threading.Event()
    peer_observed_stop = run.threading.Event()

    def controlled_worker(spec, *_args, abort_event=None, **_kwargs):
        if spec.slug == first_slug:
            assert peer_started.wait(2)
            raise run.BudgetStop("first worker stopped")
        peer_started.set()
        if abort_event is not None and abort_event.wait(2):
            peer_observed_stop.set()
        return 0

    monkeypatch.setattr(run, "_run_model", controlled_worker)
    with pytest.raises(run.BudgetStop, match="first worker stopped"):
        run.run_surface(
            benchmark_root, manifest_path, run_dir,
            delegate_factory=lambda spec: FakePilotClient(spec.slug),
            sol_client=FakeSolClient(), max_workers=2, offline_fake=True,
        )

    assert peer_observed_stop.is_set()
    checkpoints = run.AppendOnlyStore(
        run_dir / run.CHECKPOINT_NAME, "checkpoints").records()
    assert sum(row.get("checkpoint_type") == "resumable_stop"
               for row in checkpoints) == 1


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
