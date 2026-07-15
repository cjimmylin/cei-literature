"""Offline-only tests for the OPEN6-SOL1 authorized live driver."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from walkworthy.clients import Message


def _live():
    from walkworthy import open6_sol1_live

    return open6_sol1_live


def _manifest(benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import build_manifest, write_or_validate_manifest

    path = tmp_path / "manifest.json"
    write_or_validate_manifest(path, build_manifest(benchmark_root))
    return path


def _endpoint_response(slug, prompt, completion, provider="Provider One"):
    return {
        "data": {
            "id": slug,
            "endpoints": [{
                "name": provider,
                "pricing": {"prompt": prompt, "completion": completion},
            }],
        },
    }


def test_catalog_fetch_normalizes_only_exact_roster_and_per_token_prices(
        benchmark_root, tmp_path):
    live = _live()
    manifest_path = _manifest(benchmark_root, tmp_path)
    manifest = json.loads(manifest_path.read_text())
    by_slug = {row["slug"]: row for row in manifest["openrouter"]["models"]}
    seen = []

    def fetch_json(url):
        seen.append(url)
        slug = url.removeprefix(live.CATALOG_ENDPOINT_PREFIX).removesuffix(
            "/endpoints")
        row = by_slug[slug]
        return _endpoint_response(
            slug,
            str(float(row["input_per_m_usd"]) / 1_000_000),
            str(float(row["output_per_m_usd"]) / 1_000_000),
        )

    raw = live.fetch_catalog_snapshot(
        manifest, fetch_json=fetch_json,
        fetched_at="2026-07-14T20:00:00Z")

    assert [row["slug"] for row in raw["models"]] == list(by_slug)
    assert len(raw["raw_api_responses"]) == 6
    assert seen == raw["source_urls"]
    assert all(set(row) == {"slug", "providers"} for row in raw["models"])
    assert raw["models"][0]["providers"][0]["input_per_m_usd"] == (
        by_slug[raw["models"][0]["slug"]]["input_per_m_usd"])
    assert "api_key" not in json.dumps(raw).casefold()


def test_catalog_fetch_fails_closed_on_wrong_model_or_malformed_provider(
        benchmark_root, tmp_path):
    live = _live()
    manifest = json.loads(_manifest(benchmark_root, tmp_path).read_text())

    with pytest.raises(live.ContractStop, match="model identity"):
        live.fetch_catalog_snapshot(
            manifest,
            fetch_json=lambda _url: _endpoint_response(
                "substituted/model", "0.000001", "0.000001"),
            fetched_at="2026-07-14T20:00:00Z")

    def malformed(url):
        slug = url.removeprefix(live.CATALOG_ENDPOINT_PREFIX).removesuffix(
            "/endpoints")
        return {"data": {"id": slug, "endpoints": [{
            "name": "provider", "pricing": {"prompt": "free"},
        }]}}

    with pytest.raises(live.ContractStop, match="pricing"):
        live.fetch_catalog_snapshot(
            manifest, fetch_json=malformed,
            fetched_at="2026-07-14T20:00:00Z")


def test_live_authority_and_offline_gate_are_fail_closed(
        benchmark_root, tmp_path):
    live = _live()
    manifest = json.loads(_manifest(benchmark_root, tmp_path).read_text())

    assert live.validate_live_authority(manifest) is True
    assert live.validate_offline_gate(
        {"fully_complete": True, "run_mode": "offline_fake",
         "holdout_loaded": False},
        {"judge_complete": True, "single_judge_only": True,
         "holdout_loaded": False}) is True

    changed = json.loads(json.dumps(manifest))
    changed["authorization"]["live_execution"]["authorized"] = False
    with pytest.raises(live.ContractStop, match="authorization"):
        live.validate_live_authority(changed)
    with pytest.raises(live.ContractStop, match="offline dry run"):
        live.validate_offline_gate(
            {"fully_complete": False, "run_mode": "offline_fake",
             "holdout_loaded": False},
            {"judge_complete": True, "single_judge_only": True,
             "holdout_loaded": False})


def test_deepseek_exception_materializes_only_after_bound_revalidation(
        benchmark_root, tmp_path):
    live = _live()
    from walkworthy import open6_sol1_run as run
    from walkworthy import open6_sol1_runtime as runtime

    assert hasattr(live, "materialize_deepseek_exception")
    manifest_path = _manifest(benchmark_root, tmp_path)
    manifest = json.loads(manifest_path.read_text())
    run_dir = tmp_path / "live"
    raw = {
        "fetched_at": "2026-07-15T08:30:00Z",
        "source_urls": ["https://openrouter.ai/api/v1/models"],
        "models": [{
            "slug": row["slug"],
            "providers": [{
                "provider": "eligible",
                "input_per_m_usd": row["input_per_m_usd"],
                "output_per_m_usd": row["output_per_m_usd"],
            }],
        } for row in manifest["openrouter"]["models"]],
        "raw_api_responses": [{"test": True}],
    }
    run.register_catalog_snapshot(
        benchmark_root, manifest_path, run_dir, raw)

    spec = next(row for row in runtime.SUT_SPECS
                if row.slug == runtime.DEEPSEEK_EXCEPTION_MODEL)
    responses = [
        (404, {"error": {"message": "not found"}}),
        (404, {"error": {"message": "not found"}}),
    ]

    def transport(_url, _headers, _payload, timeout=None):
        return responses.pop(0)

    ledger = runtime.OpenRouterAttemptLedger(
        run_dir / live.OPENROUTER_LEDGER_NAME)
    with pytest.raises(runtime.ThreadStop):
        runtime.OpenRouterPilotClient(
            spec, "k", ledger, transport).complete(
                runtime.DEEPSEEK_EXCEPTION_LOGICAL_KEY,
                [Message("user", "registered canary")])
    live.revalidate_catalog(
        benchmark_root, manifest_path, run_dir,
        fetched_at="2026-07-15T08:31:00Z",
        recovery_trigger="provider_recovery",
        fetch_json=lambda url: _endpoint_response(
            url.removeprefix(live.CATALOG_ENDPOINT_PREFIX).removesuffix(
                "/endpoints"),
            "0.00000001", "0.00000001"))

    marker = live.materialize_deepseek_exception(
        benchmark_root, manifest_path, run_dir,
        authorization_path=(
            benchmark_root / "00-PORTFOLIO" /
            "20260715-jimmy-open6-sol1-deepseek-exception-authorization.md"))

    assert marker["logical_key"] == runtime.DEEPSEEK_EXCEPTION_LOGICAL_KEY
    assert marker["requested_model"] == runtime.DEEPSEEK_EXCEPTION_MODEL
    assert marker["prior_attempt_ids"] == [1, 2]
    assert marker["prior_statuses"] == [404, 404]
    assert marker["maximum_additional_attempts"] == 1
    assert marker["catalog_revalidation_logical_key"] == (
        "catalog-revalidation:000001")
    assert (run_dir / runtime.DEEPSEEK_EXCEPTION_MARKER_NAME).read_text() == (
        json.dumps(marker, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")) + "\n")


def test_cli_registers_bounded_deepseek_revalidation_phase():
    live = _live()

    args = live._parser().parse_args([
        "revalidate-deepseek-exception",
        "--benchmark-root", "..",
        "--manifest", "../runs/live/manifest.json",
        "--run-dir", "../runs/live",
        "--fetched-at", "2026-07-15T08:31:00Z",
        "--authorization", "../00-PORTFOLIO/authorization.md",
    ])

    assert args.phase == "revalidate-deepseek-exception"
    assert args.authorization.endswith("authorization.md")


@pytest.mark.parametrize("api_key,max_workers", [
    ("", 2),
    ("test-placeholder", 0),
    ("test-placeholder", 3),
    ("test-placeholder", True),
])
def test_execute_rejects_invalid_live_configuration_before_any_artifact_or_call(
        benchmark_root, tmp_path, api_key, max_workers):
    live = _live()
    manifest_path = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "must-not-exist"
    calls = []

    def forbidden(*_args, **_kwargs):
        calls.append("called")
        pytest.fail("invalid live configuration reached a call seam")

    with pytest.raises(live.ContractStop, match="configuration"):
        live.execute_authorized(
            benchmark_root, manifest_path, tmp_path / "offline", run_dir,
            api_key=api_key, transport=forbidden, codex_runner=forbidden,
            max_workers=max_workers)

    assert calls == []
    assert not run_dir.exists()


def test_dry_run_materializes_immutable_complete_summary(
        benchmark_root, tmp_path, monkeypatch):
    live = _live()
    from walkworthy import open6_sol1_run as run

    manifest_path = _manifest(benchmark_root, tmp_path)
    manifest = json.loads(manifest_path.read_text())
    catalog_source = tmp_path / "catalog-source"
    raw = {
        "fetched_at": "2026-07-14T20:00:00Z",
        "source_urls": ["https://openrouter.ai/api/v1/models"],
        "models": [{
            "slug": row["slug"],
            "providers": [{
                "provider": "fake-provider",
                "input_per_m_usd": row["input_per_m_usd"],
                "output_per_m_usd": row["output_per_m_usd"],
            }],
        } for row in manifest["openrouter"]["models"]],
        "raw_api_responses": [{"preserved": True}],
    }
    run.register_catalog_snapshot(
        benchmark_root, manifest_path, catalog_source, raw)
    dry_dir = tmp_path / "offline"
    sut = {"fully_complete": True, "run_mode": "offline_fake",
           "holdout_loaded": False}
    judge = {"judge_complete": True, "single_judge_only": True,
             "holdout_loaded": False}
    calls = []
    monkeypatch.setattr(live, "run_surface", lambda *a, **k: calls.append(
        "sut") or sut)
    monkeypatch.setattr(live, "sut_status", lambda *a, **k: sut)
    monkeypatch.setattr(live, "run_judging", lambda *a, **k: calls.append(
        "judge") or judge)
    monkeypatch.setattr(live, "judge_status", lambda *a, **k: judge)
    monkeypatch.setattr(live, "prepare_judge_plan", lambda *a, **k: {
        "units": 5370, "category_cells": 10008, "batches": 227,
    })

    first = live.materialize_offline_dry_run(
        benchmark_root, manifest_path, dry_dir,
        catalog_source_run_dir=catalog_source)
    second = live.materialize_offline_dry_run(
        benchmark_root, manifest_path, dry_dir,
        catalog_source_run_dir=catalog_source)

    assert first == second
    assert first["offline_gate_passed"] is True
    assert calls == ["sut", "judge", "sut", "judge"]
    assert (dry_dir / live.OFFLINE_DRY_RUN_SUMMARY_NAME).is_file()
    assert "api_key" not in json.dumps(first).casefold()


@pytest.mark.timeout(900)
def test_full_production_fake_dry_run_exact_geometry_and_immutable_resume(
        benchmark_root, tmp_path):
    live = _live()
    from walkworthy import open6_sol1_run as run

    manifest_path = _manifest(benchmark_root, tmp_path)
    manifest = json.loads(manifest_path.read_text())
    catalog_source = tmp_path / "catalog-source"
    raw = {
        "fetched_at": "2026-07-14T20:00:00Z",
        "source_urls": ["https://openrouter.ai/api/v1/models"],
        "models": [{
            "slug": row["slug"],
            "providers": [{
                "provider": "fake-provider",
                "input_per_m_usd": row["input_per_m_usd"],
                "output_per_m_usd": row["output_per_m_usd"],
            }],
        } for row in manifest["openrouter"]["models"]],
        "raw_api_responses": [{"preserved": True}],
    }
    run.register_catalog_snapshot(
        benchmark_root, manifest_path, catalog_source, raw)
    dry_dir = tmp_path / "full-offline"

    first = live.materialize_offline_dry_run(
        benchmark_root, manifest_path, dry_dir,
        catalog_source_run_dir=catalog_source, max_workers=2)
    before = {
        path.name: (path.stat().st_size, live._sha256_bytes(path.read_bytes()))
        for path in dry_dir.iterdir() if path.is_file()
    }
    second = live.materialize_offline_dry_run(
        benchmark_root, manifest_path, dry_dir,
        catalog_source_run_dir=catalog_source, max_workers=2)
    after = {
        path.name: (path.stat().st_size, live._sha256_bytes(path.read_bytes()))
        for path in dry_dir.iterdir() if path.is_file()
    }

    assert first == second
    assert before == after
    assert first["offline_gate_passed"] is True
    assert first["sut_status"]["complete_records"] == 2064
    assert first["sut_status"]["cached_sut_calls"] == 5886
    assert first["sut_status"]["cached_classifier_routes"] == 1722
    assert first["sut_status"]["fully_complete"] is True
    assert first["judge_plan"]["units"] == 5370
    assert first["judge_plan"]["category_cells"] == 10008
    assert first["judge_plan"]["batches"] == 227
    assert first["judge_status"]["valid_batches"] == 227
    assert first["judge_status"]["judge_complete"] is True
    assert first["paid_calls"] == 0
    assert first["credentials_accessed"] is False
    assert first["holdout_loaded"] is False


def test_frozen_sol_canaries_are_one_classifier_and_one_24_unit_judge():
    live = _live()
    tasks = live.sol_canary_tasks()

    assert [task.kind for task in tasks] == ["classifier", "judge"]
    assert tasks[0].logical_key == "canary:sol:classifier:v1"
    assert tasks[1].logical_key == "canary:sol:judge:v1"
    assert len(tasks[1].expected_unit_keys) == 24
    assert len(set(tasks[1].expected_unit_keys)) == 24
    assert all(len(task.prompt_sha256) == 64 for task in tasks)
    assert all(len(task.schema_sha256) == 64 for task in tasks)
    assert live.sol_canary_tasks() == tasks


def _first_value(schema):
    if "const" in schema:
        return schema["const"]
    if "enum" in schema:
        return schema["enum"][0]
    kind = schema["type"]
    if kind == "object":
        return {key: _first_value(schema["properties"][key])
                for key in schema.get("required", [])}
    if kind == "array":
        item_schema = schema["items"]
        unit_key_schema = (item_schema.get("properties", {})
                           .get("unit_key", {}))
        keys = unit_key_schema.get("enum")
        if (isinstance(keys, list)
                and len(keys) == schema.get("minItems", 0)):
            values = []
            for key in keys:
                value = _first_value(item_schema)
                value["unit_key"] = key
                values.append(value)
            return values
        return [_first_value(item_schema)
                for _ in range(schema.get("minItems", 0))]
    if kind == "string":
        return "ok"
    if kind in ("number", "integer"):
        return schema.get("minimum", 0)
    if kind == "boolean":
        return False
    return None


class _FakeSolResult:
    def __init__(self, value, prompt, schema, attempt_id):
        self.value = value
        self.prompt = prompt
        self.schema = schema
        self.final_text = json.dumps(value, sort_keys=True, separators=(",", ":"))
        self.trace_jsonl = '{"type":"turn.completed","usage":{}}\n'
        self.cli_version = "fake-sol"
        self.usage = {}
        self.attempt_ids = (attempt_id,)


class _FakeSol:
    def __init__(self):
        self.calls = []

    def run_json(self, logical_key, prompt, schema, value_validator=None):
        value = _first_value(schema)
        assert value_validator is None or value_validator(value) is True
        self.calls.append((logical_key, prompt, schema))
        return _FakeSolResult(value, prompt, schema, len(self.calls))


def test_sol_canary_results_are_immutable_and_valid_outputs_are_not_rerun(tmp_path):
    live = _live()
    fake = _FakeSol()

    first = live.run_sol_canaries(tmp_path, fake)
    second = live.run_sol_canaries(tmp_path, fake)

    assert first == second
    assert first["passed"] is True
    assert first["task_count"] == 2
    assert len(fake.calls) == 2
    assert len(live.load_sol_canary_results(tmp_path)) == 2
    assert "prompt" in first["tasks"][0]
    assert "schema" in first["tasks"][0]


def test_sol_canary_recovers_valid_attempt_custody_without_rerun(tmp_path):
    live = _live()
    from walkworthy.open6_sol1_run import AppendOnlyStore
    from walkworthy.open6_sol1_runtime import SolTaskLedger

    custody = AppendOnlyStore(
        tmp_path / live.CANARY_SOL_CUSTODY_NAME,
        "canary-sol-attempt-custody", key_field="attempt_id")
    ledger = SolTaskLedger(
        tmp_path / live.CANARY_SOL_LEDGER_NAME,
        planned_cap=2, max_attempts=4, replay_cap=2)
    trace = '{"type":"turn.completed","usage":{}}\n'
    for task in live.sol_canary_tasks():
        value = _first_value(task.schema)
        final = json.dumps(value, sort_keys=True, separators=(",", ":"))
        attempt = ledger.begin(
            task.logical_key, task.prompt_sha256, task.schema_sha256)
        custody.append({
            "logical_key": task.logical_key, "attempt_id": attempt,
            "prompt": task.prompt, "schema": task.schema,
            "final_text": final, "trace_jsonl": trace,
            "stderr": "", "returncode": 0, "error_class": None,
            "payload_sha256": task.prompt_sha256,
            "schema_sha256": task.schema_sha256,
            "trace_sha256": live._text_hash(trace),
            "response_sha256": live._text_hash(final),
            "error_sha256": None, "cli_version": "fake", "usage": {},
        })
        ledger.finish(
            attempt, valid=True, trace_sha256=live._text_hash(trace),
            response_sha256=live._text_hash(final), error_sha256=None,
            cli_version="fake", usage={})

    class NoRerun:
        def __init__(self):
            self.ledger = ledger
            self._canary_custody_store = custody

        def run_json(self, *_args, **_kwargs):
            pytest.fail("valid Sol canary was rerun")

    assert live.run_sol_canaries(tmp_path, NoRerun())["passed"] is True
    assert len(live.load_sol_canary_results(tmp_path)) == 2


def test_canary_artifact_keeps_gate_time_turn_count_on_resume(tmp_path):
    live = _live()
    payload = {
        "schema_version": "test", "passed": True,
        "combined_sol_attempts_at_gate": 2,
    }
    assert live._write_or_validate_canary_artifact(tmp_path, payload) == payload
    resumed = dict(payload, combined_sol_attempts_at_gate=99)
    assert live._write_or_validate_canary_artifact(
        tmp_path, resumed)["combined_sol_attempts_at_gate"] == 2


def test_guarded_sol_stops_after_registered_replay_on_oauth_quota(tmp_path):
    live = _live()
    from walkworthy.open6_sol1_run import AppendOnlyStore, UnattendedStop
    from walkworthy.open6_sol1_runtime import SolTaskLedger

    custody = AppendOnlyStore(
        tmp_path / "custody.jsonl", "canary-sol-attempt-custody",
        key_field="attempt_id")
    ledger = SolTaskLedger(
        tmp_path / "sol.jsonl", planned_cap=2, max_attempts=4,
        replay_cap=2)

    class Proc:
        stdout = ""
        stderr = "OAuth usage limit reached"
        returncode = 1

    client = live.GuardedSolExecClient(
        ledger, runner=lambda *_args, **_kwargs: Proc(),
        cli_version="fake", attempt_sink=custody.append_sink,
        attempt_records=custody.records)
    task = live.sol_canary_tasks()[0]

    with pytest.raises(UnattendedStop, match="OAuth"):
        client.run_json(task.logical_key, task.prompt, task.schema)
    assert ledger.snapshot()["attempts"] == 2


def test_guarded_sol_treats_empty_stderr_cli_failure_as_systemic(tmp_path):
    live = _live()
    from walkworthy.open6_sol1_run import AppendOnlyStore, UnattendedStop
    from walkworthy.open6_sol1_runtime import SolTaskLedger

    custody = AppendOnlyStore(
        tmp_path / "custody.jsonl", "canary-sol-attempt-custody",
        key_field="attempt_id")
    ledger = SolTaskLedger(
        tmp_path / "sol.jsonl", planned_cap=2, max_attempts=4,
        replay_cap=2)

    class Proc:
        stdout = ""
        stderr = ""
        returncode = 1

    client = live.GuardedSolExecClient(
        ledger, runner=lambda *_args, **_kwargs: Proc(),
        cli_version="fake", attempt_sink=custody.append_sink,
        attempt_records=custody.records)
    task = live.sol_canary_tasks()[0]

    with pytest.raises(UnattendedStop, match="unregistered Sol CLI"):
        client.run_json(task.logical_key, task.prompt, task.schema)
    assert ledger.snapshot()["attempts"] == 2


def test_combined_sol_ledger_blocks_before_combined_turn_cap():
    live = _live()

    class Base:
        def __init__(self):
            self.attempts = 2044
            self.started = []

        def snapshot(self):
            return {"attempts": self.attempts, "inflight": 0}

        def begin(self, *args):
            self.started.append(args)
            self.attempts += 1
            return self.attempts

    base = Base()
    combined = live.CombinedSolLedger(base, canary_attempt_count=lambda: 2)
    assert combined.begin("key", "a" * 64, "b" * 64) == 2045
    with pytest.raises(live.BudgetStop, match="combined Sol turn cap"):
        combined.begin("other", "a" * 64, "b" * 64)
    assert len(base.started) == 1


def test_promoted_sut_canary_evidence_requires_all_six_exact_models(
        benchmark_root, tmp_path):
    live = _live()
    manifest = json.loads(_manifest(benchmark_root, tmp_path).read_text())
    item_id = manifest["surface"]["ordered_item_ids"][0]
    calls = []
    executions = []
    for row in manifest["openrouter"]["models"]:
        slug = row["slug"]
        request = {"system": None, "messages": [{"role": "user", "content": "x"}]}
        payload = {"model": slug, "messages": request["messages"],
                   "max_tokens": 2048}
        response = {"text": "answer", "model": slug}
        calls.append({
            "logical_key": f"or:{slug}:{item_id}:content:001",
            "model": slug, "request": request, "payload": payload,
            "response": response,
        })
        executions.append({
            "logical_key": f"item:{slug}:{item_id}", "model": slug,
            "item_id": item_id,
        })

    evidence = live.validate_promoted_sut_canary_records(
        manifest, calls, executions, [])
    assert len(evidence) == 6
    assert all(row["outcome"] == "passed" for row in evidence)
    assert all(len(row["request_sha256"]) == 64 for row in evidence)
    with pytest.raises(live.ContractStop, match="six promoted"):
        live.validate_promoted_sut_canary_records(
            manifest, calls[:-1], executions[:-1], [])


def test_stop_checkpoint_is_idempotent_and_contains_safe_resume_command(tmp_path):
    live = _live()
    snapshot = {
        "complete_records": 4, "expected_records": 6,
        "completed_logical_keys": [f"item:m:{i}" for i in range(4)],
        "missing_logical_keys": ["item:m:4", "item:m:5"],
        "terminal_unresolved_logical_keys": ["item:m:5"],
        "openrouter_attempts": 9, "sol_attempts": 2,
        "openrouter_accounting": {"booked_usd": "0.12"},
        "sol_accounting": {"combined_attempts": 2},
        "soft_budget_projection": {"booked_usd": "0.12",
                                    "projected_total_usd": "12.30"},
        "judge_expected_batch_count": 0,
        "judge_completed_batch_count": 0,
        "judge_terminal_batch_count": 0,
        "judge_missing_batch_count": 0,
        "judge_expected_logical_keys": [],
        "judge_completed_logical_keys": [],
        "judge_terminal_logical_keys": [],
        "judge_missing_logical_keys": [],
        "judge_unresolved_logical_keys": [],
        "judge_upstream_empty_logical_keys": [],
    }
    command = "python -m walkworthy.open6_sol1_live execute --run-dir RUN"

    first = live.record_stop(tmp_path, "quota exhausted", command, snapshot)
    second = live.record_stop(tmp_path, "quota exhausted", command, snapshot)

    assert first == second
    assert first["stop_reason"] == "quota exhausted"
    assert first["safest_next_command"] == command
    assert first["missing_execution_records"] == 2
    assert first["terminal_unresolved_logical_keys"] == ["item:m:5"]
    assert len((tmp_path / live.STOP_CHECKPOINT_NAME).read_text().splitlines()) == 1


def test_stop_snapshot_captures_exact_judge_batch_partition(tmp_path):
    live = _live()
    from walkworthy.open6_sol1_run import AppendOnlyStore

    manifest = {
        "openrouter": {"models": [{"slug": "m"}]},
        "surface": {"ordered_item_ids": ["i"]},
    }
    plans = AppendOnlyStore(
        tmp_path / live.JUDGE_PLAN_NAME, "sol-judge-batch-plan")
    results = AppendOnlyStore(
        tmp_path / live.JUDGE_RESULT_NAME, "sol-judge-batch-results")
    unresolved = AppendOnlyStore(
        tmp_path / live.JUDGE_UNRESOLVED_NAME,
        "sol-judge-unresolved-batches")
    plans.append({"logical_key": "sol:judge:valid",
                  "available_unit_keys": ["u1"]})
    plans.append({"logical_key": "sol:judge:unresolved",
                  "available_unit_keys": ["u2"]})
    plans.append({"logical_key": "sol:judge:upstream-empty",
                  "available_unit_keys": []})
    plans.append({"logical_key": "sol:judge:pending",
                  "available_unit_keys": ["u3"]})
    results.append({"logical_key": "sol:judge:valid"})
    unresolved.append({"logical_key": "sol:judge:unresolved"})

    snapshot = live._stop_snapshot(manifest, tmp_path, runtime=None)

    assert snapshot["judge_expected_batch_count"] == 4
    assert snapshot["judge_completed_batch_count"] == 1
    assert snapshot["judge_terminal_batch_count"] == 2
    assert snapshot["judge_missing_batch_count"] == 1
    assert snapshot["judge_expected_logical_keys"] == [
        "sol:judge:pending", "sol:judge:unresolved",
        "sol:judge:upstream-empty", "sol:judge:valid"]
    assert snapshot["judge_completed_logical_keys"] == ["sol:judge:valid"]
    assert snapshot["judge_terminal_logical_keys"] == [
        "sol:judge:unresolved", "sol:judge:upstream-empty"]
    assert snapshot["judge_missing_logical_keys"] == ["sol:judge:pending"]


def test_sanitized_status_never_serializes_api_key(tmp_path):
    live = _live()
    status = live.sanitized_status(
        tmp_path,
        sut_status={"complete_records": 7},
        judge_status={"completed_batches": 3},
        secret="sk-do-not-print")
    encoded = json.dumps(status, sort_keys=True)

    assert "sk-do-not-print" not in encoded
    assert "secret" not in status
    assert status["sut"]["complete_records"] == 7
