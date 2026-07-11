"""Offline qualification-runner tests for CHARITROC's cheap OpenRouter panel."""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

import pytest

from pilot import contracts, manifest
from pilot import run_cheap_openrouter as cheap


BANK = Path(__file__).resolve().parents[1]
MOCK_PROVENANCE = "harness validation, NOT a measurement"
CHEAP_MODELS = ("gpt-5-nano", "gpt-5.4-nano", "gpt-5-mini")
REQUIRED_PARAMETERS = {
    "max_completion_tokens", "reasoning", "response_format",
    "structured_outputs",
}


class TickClock:
    def __init__(self):
        self.value = datetime(2026, 7, 11, 1, 0, tzinfo=timezone.utc)

    def __call__(self):
        observed = self.value
        self.value += timedelta(seconds=1)
        return observed.strftime("%Y-%m-%dT%H:%M:%SZ")


class FakeCatalog:
    def __init__(self, *, mutate=None):
        self.calls = []
        self.mutate = mutate

    def __call__(self, provider_model_id):
        self.calls.append(provider_model_id)
        endpoint = {
            "name": "Azure exact endpoint",
            "provider_name": "Azure",
            "context_length": 400000,
            "supported_parameters": sorted(REQUIRED_PARAMETERS),
            "pricing": {
                "prompt": "0.00000001",
                "completion": "0.00000010",
            },
        }
        payload = {
            "data": {
                "id": provider_model_id,
                "endpoints": [endpoint],
            }
        }
        if self.mutate is not None:
            self.mutate(payload, provider_model_id)
        return payload


def _response(intent, decision, reason="Fixture response."):
    return json.dumps({
        "reason": reason,
        "INTENT": intent,
        "DECISION": decision,
    }, separators=(",", ":"))


class FakeCheapDriver:
    """Explicit mock dependency emitting real validated stage contracts."""

    def __init__(
            self, sidecar, *, crash_calls=(), crash_after_stages=(),
            fail_calls=()):
        self.sidecar = deepcopy(sidecar)
        self.crash_calls = set(crash_calls)
        self.crash_after_stages = set(crash_after_stages)
        self.fail_calls = set(fail_calls)
        self.calls = []
        self.stage_calls = []

    def _raw(self, episode, model, stage):
        if episode["id"].startswith("CHEAP-ACCESS-"):
            return _response("UNCERTAIN", "VERIFY", "Access probe.")
        hidden = self.sidecar[episode["id"]]
        truth = hidden["true_type"]
        cue = hidden["cue_variant"]
        if stage in {"stage_1", "stage_2"}:
            return _response("UNCERTAIN", "VERIFY")
        if stage == "stage_3":
            if cue in {"absent", "adversarial"}:
                return _response("UNCERTAIN", "VERIFY")
            return (
                _response("BENIGN", "CONDITIONAL")
                if truth == "benign"
                else _response("MALICIOUS", "RESTRICT")
            )
        if model == "gpt-5-nano":
            return _response("UNCERTAIN", "VERIFY")
        if truth == "benign":
            return _response(
                "BENIGN", "GRANT" if model == "gpt-5-mini" else "CONDITIONAL"
            )
        return _response(
            "MALICIOUS", "REFUSE" if model == "gpt-5-mini" else "RESTRICT"
        )

    def run_episode(
            self, episode, *, logical_model_id, panel_profile,
            before_stage=None, stage_sink=None):
        call_number = len(self.calls) + 1
        self.calls.append((episode["id"], logical_model_id, panel_profile))
        identity = manifest.resolve_openrouter_identity(
            logical_model_id, profile_id=panel_profile
        )
        execution_id = str(uuid.UUID(int=call_number + 1, version=4))
        requests = []
        results = []
        descriptors = []
        prior = {}

        for stage_index, stage in enumerate(contracts.STAGES):
            request = contracts.build_stage_request(
                episode,
                execution_id=execution_id,
                provider="openrouter",
                logical_model_id=logical_model_id,
                provider_model_id=identity["provider_model_id"],
                configuration_id=identity["configuration_id"],
                stage=stage,
                prior_responses=prior,
            )
            descriptor = {
                "fixture": True,
                "provider": "openrouter",
                "profile_id": panel_profile,
                "request_sha256": request["request_sha256"],
                "stage": stage,
            }
            hook = {
                "provider": "openrouter",
                "integrity_session": 1,
                "execution_id": execution_id,
                "stage": stage,
                "request": deepcopy(request),
                "transport_descriptor": deepcopy(descriptor),
                "attestation": None,
            }
            if before_stage is not None:
                before_stage(deepcopy(hook))
            self.stage_calls.append((episode["id"], logical_model_id, stage))
            if call_number in self.crash_calls and stage == "stage_1":
                raise RuntimeError("simulated post-start crash")

            raw = self._raw(episode, logical_model_id, stage)
            attempt = contracts.build_stage_attempt(
                attempt_index=1,
                started_at_utc=(
                    f"2026-07-11T01:{call_number % 60:02d}:"
                    f"{stage_index * 2:02d}Z"
                ),
                completed_at_utc=(
                    f"2026-07-11T01:{call_number % 60:02d}:"
                    f"{stage_index * 2 + 1:02d}Z"
                ),
                provider_request_id=f"fixture-{call_number}-{stage_index + 1}",
                token_emission_started=True,
                exit_status=None,
                http_status=200,
                finish_reason="stop",
                usage={
                    "input_tokens": 10,
                    "cached_input_tokens": 0,
                    "output_tokens": 5,
                    "reasoning_tokens": 1,
                    "total_tokens": 15,
                },
                raw_trace=raw,
                raw_final_message=raw,
                reasoning_effort="medium",
                reasoning_details=None,
                error_code=None,
            )
            returned_provider = (
                "WrongProvider"
                if call_number in self.fail_calls and stage == "stage_1"
                else "Azure"
            )
            result = contracts.build_stage_result(
                request,
                run_mode="mock",
                returned_provider_model_id=identity["provider_model_id"],
                returned_provider_name=returned_provider,
                session_id=None,
                transport_request_sha256=contracts.canonical_sha256(descriptor),
                attempts=[attempt],
                tool_events=[],
                session_chain_ok=True,
                isolation_ok=True,
                future_text_absent=True,
            )
            requests.append(request)
            results.append(result)
            descriptors.append(descriptor)
            if stage_sink is not None:
                stage_sink({**deepcopy(hook), "result": deepcopy(result)})
            if (call_number, stage) in self.crash_after_stages:
                raise RuntimeError("simulated post-stage crash")
            if result["terminal_status"] != "complete":
                break
            prior[stage] = raw

        status = (
            "complete"
            if len(results) == 4 and all(
                row["terminal_status"] == "complete" for row in results
            )
            else results[-1]["terminal_status"]
        )
        return {
            "status": status,
            "provenance": MOCK_PROVENANCE,
            "integrity_session_count": 1,
            "sessions": [{
                "integrity_session": 1,
                "execution_id": execution_id,
                "status": status,
                "requests": deepcopy(requests),
                "results": deepcopy(results),
                "transport_descriptors": deepcopy(descriptors),
                "chain": None,
            }],
            "requests": requests,
            "results": results,
            "transport_descriptors": descriptors,
            "chain": None,
        }


@pytest.fixture
def sidecar():
    return json.loads((BANK / "sidecar/ground_truth.json").read_text())


def _runner(
        tmp_path, sidecar, *, driver=None, catalog=None, bank_root=BANK):
    return cheap.CheapOpenRouterQualificationRunner(
        bank_root=bank_root,
        out_dir=tmp_path / "qualification",
        run_mode="mock",
        driver=driver or FakeCheapDriver(sidecar),
        catalog_loader=catalog or FakeCatalog(),
        clock=TickClock(),
    )


def _copy_qualification_bank(tmp_path):
    root = tmp_path / "bank"
    for relative_path in (
            "seeds_public.yaml", "sidecar/ground_truth.json",
            "analysis/roc.py", "scorers/action_scale.py",
            "scorers/stage3_update.py"):
        source = BANK / relative_path
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return root


def test_runner_binds_root_to_exact_qualification_profile(tmp_path, sidecar):
    runner = _runner(tmp_path, sidecar)
    metadata = json.loads((runner.out_dir / "run_metadata.json").read_text())

    assert metadata["purpose"] == "qualification-only"
    assert metadata["profile_id"] == manifest.CHEAP_PROFILE_ID
    assert metadata["profile_sha256"] == manifest.cheap_panel_sha256()
    assert metadata["logical_model_ids"] == list(CHEAP_MODELS)
    assert metadata["provider"] == "openrouter"
    assert metadata["provenance"] == MOCK_PROVENANCE
    assert "sidecar" not in json.dumps(metadata).lower()


def test_root_binds_public_scoring_projection_and_scorer_contracts(
        tmp_path, sidecar):
    runner = _runner(tmp_path, sidecar)
    metadata = json.loads((runner.out_dir / "run_metadata.json").read_text())
    projection = [{
        "item_id": item_id,
        "true_type": sidecar[item_id]["true_type"],
        "cue_variant": sidecar[item_id]["cue_variant"],
        "expected_stage3": sidecar[item_id]["expected_stage3"],
    } for item_id in sorted(runner._by_id)]

    assert metadata["public_scoring_projection_sha256"] == (
        contracts.canonical_sha256(projection)
    )
    source_hashes = metadata["scoring_contract_source_sha256s"]
    assert set(source_hashes) == {
        "analysis/roc.py", "scorers/action_scale.py",
        "scorers/stage3_update.py",
    }
    assert metadata["scoring_contract_sha256"] == (
        contracts.canonical_sha256(source_hashes)
    )


@pytest.mark.parametrize("drift", [
    "disk-sidecar", "memory-sidecar", "scorer-source",
])
def test_root_rejects_sidecar_and_scorer_drift_before_report_or_verify(
        tmp_path, sidecar, drift):
    bank_root = _copy_qualification_bank(tmp_path)
    runner = _runner(
        tmp_path, sidecar, bank_root=bank_root,
        driver=FakeCheapDriver(sidecar),
    )
    item_id = sorted(runner._by_id)[0]
    if drift == "disk-sidecar":
        path = bank_root / "sidecar/ground_truth.json"
        payload = json.loads(path.read_text())
        payload[item_id]["true_type"] = (
            "malicious" if payload[item_id]["true_type"] == "benign"
            else "benign"
        )
        path.write_text(json.dumps(payload), encoding="utf-8")
    elif drift == "memory-sidecar":
        runner._sidecar[item_id]["cue_variant"] = (
            "weak" if runner._sidecar[item_id]["cue_variant"] != "weak"
            else "strong"
        )
    else:
        path = bank_root / "scorers/action_scale.py"
        path.write_text(
            path.read_text() + "\n# confined scorer drift\n",
            encoding="utf-8",
        )

    with pytest.raises(ValueError, match="scoring|metadata|contract"):
        runner.report() if drift != "memory-sidecar" else runner.verify("all")


def test_live_rejects_every_injected_dependency(tmp_path, sidecar):
    dependencies = {
        "driver": FakeCheapDriver(sidecar),
        "catalog_loader": FakeCatalog(),
        "clock": TickClock(),
    }
    for name, dependency in dependencies.items():
        with pytest.raises(ValueError, match="live|inject"):
            cheap.CheapOpenRouterQualificationRunner(
                bank_root=BANK,
                out_dir=tmp_path / name,
                run_mode="live",
                **{name: dependency},
            )


def test_mock_requires_explicit_driver_and_catalog_loader(tmp_path):
    with pytest.raises(ValueError, match="mock.*driver"):
        cheap.CheapOpenRouterQualificationRunner(
            bank_root=BANK,
            out_dir=tmp_path / "missing-driver",
            run_mode="mock",
            catalog_loader=FakeCatalog(),
        )
    with pytest.raises(ValueError, match="mock.*catalog"):
        cheap.CheapOpenRouterQualificationRunner(
            bank_root=BANK,
            out_dir=tmp_path / "missing-catalog",
            run_mode="mock",
            driver=type(
                "MinimalDriver", (), {"run_episode": lambda self: None}
            )(),
        )


def test_catalog_preflight_uses_each_exact_endpoint_and_runs_before_calls(
        tmp_path, sidecar):
    catalog = FakeCatalog()
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver, catalog=catalog)

    report = runner.preflight_catalog()

    assert catalog.calls == [f"openai/{model}" for model in CHEAP_MODELS]
    assert driver.calls == []
    assert report["profile_id"] == manifest.CHEAP_PROFILE_ID
    assert [row["provider_model_id"] for row in report["models"]] == [
        f"openai/{model}" for model in CHEAP_MODELS
    ]
    assert all(row["eligible_azure_endpoint_count"] == 1
               for row in report["models"])


def test_catalog_preflight_allows_multiple_individually_eligible_azure_endpoints(
        tmp_path, sidecar):
    def duplicate(payload, _model):
        second = deepcopy(payload["data"]["endpoints"][0])
        second["name"] = "second exact Azure endpoint"
        payload["data"]["endpoints"].append(second)

    runner = _runner(tmp_path, sidecar, catalog=FakeCatalog(mutate=duplicate))
    report = runner.preflight_catalog()

    assert [row["eligible_azure_endpoint_count"]
            for row in report["models"]] == [2, 2, 2]


def test_persisted_catalog_projection_is_semantically_revalidated(
        tmp_path, sidecar):
    runner = _runner(tmp_path, sidecar)
    runner.preflight_catalog()
    path = runner.out_dir / "catalog/preflight.json"
    report = json.loads(path.read_text())
    report["models"][0]["eligible_azure_endpoints"][0][
        "context_length"
    ] = 1
    report["catalog_preflight_sha256"] = contracts.canonical_sha256({
        key: value for key, value in report.items()
        if key != "catalog_preflight_sha256"
    })
    path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(ValueError, match="catalog|endpoint|context"):
        runner._validate_catalog_artifact()


def test_catalog_preflight_rejects_parameter_union_across_endpoints(
        tmp_path, sidecar):
    def split_parameters(payload, _model):
        first = payload["data"]["endpoints"][0]
        first["supported_parameters"] = [
            "max_completion_tokens", "reasoning",
        ]
        second = deepcopy(first)
        second["name"] = "second incomplete Azure endpoint"
        second["supported_parameters"] = [
            "response_format", "structured_outputs",
        ]
        payload["data"]["endpoints"].append(second)

    runner = _runner(
        tmp_path, sidecar, catalog=FakeCatalog(mutate=split_parameters)
    )
    with pytest.raises(ValueError, match="eligible|endpoint|parameters"):
        runner.preflight_catalog()


@pytest.mark.parametrize("failure", ["provider", "model", "context", "price"])
def test_catalog_preflight_fails_closed_on_endpoint_drift(
        tmp_path, sidecar, failure):
    def poison(payload, model):
        endpoint = payload["data"]["endpoints"][0]
        if failure == "provider":
            endpoint["provider_name"] = "OpenAI"
        elif failure == "model":
            payload["data"]["id"] = model + "-substitute"
        elif failure == "context":
            endpoint["context_length"] = 399999
        else:
            endpoint["pricing"]["completion"] = "0.00001000"

    runner = _runner(tmp_path, sidecar, catalog=FakeCatalog(mutate=poison))
    with pytest.raises(ValueError, match="catalog|model|eligible|endpoint"):
        runner.preflight_catalog()


def test_access_is_nonbank_one_stage_per_model_with_durable_journal(
        tmp_path, sidecar):
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver)

    report = runner.access()

    assert report["measurement_ready"] is False
    assert report["provenance"] == "model access probe, NOT a measurement"
    assert [row[0] for row in driver.calls] == [
        f"CHEAP-ACCESS-{index:02d}-{model}"
        for index, model in enumerate(CHEAP_MODELS, 1)
    ]
    assert [row[2] for row in driver.stage_calls] == ["stage_1"] * 3
    journal = [json.loads(line) for line in (
        runner.out_dir / "access/attempt-journal.jsonl"
    ).read_text().splitlines()]
    assert [row["state"] for row in journal] == [
        "started", "succeeded", "started", "succeeded", "started", "succeeded",
    ]
    assert runner.verify("access")["valid"] is True


def test_verify_all_enforces_stage_aware_whole_root_closure(tmp_path, sidecar):
    runner = _runner(tmp_path, sidecar)
    runner.access()
    verification = runner.verify("all")
    assert set(verification["scopes"]) == {"access"}
    runner.smoke()
    runner.report()
    assert runner.verify("all")["valid"] is True

    unexpected_artifacts = (
        ("unexpected-root.json", "regular"),
        ("catalog/unexpected.json", "regular"),
        ("access/unexpected.txt", "regular"),
        ("reports/unexpected.json", "regular"),
        ("catalog/unexpected-link.json", "symlink"),
        ("reports/unexpected-directory", "directory"),
    )
    for relative_path, artifact_kind in unexpected_artifacts:
        unexpected = runner.out_dir / relative_path
        if artifact_kind == "regular":
            unexpected.write_text("{}\n", encoding="utf-8")
        elif artifact_kind == "symlink":
            unexpected.symlink_to(runner.out_dir / "catalog/preflight.json")
        else:
            unexpected.mkdir()
        with pytest.raises(
                ValueError,
                match="artifact|root|coverage|extra|symlink|unexpected"):
            runner.verify("all")
        if unexpected.is_symlink() or unexpected.is_file():
            unexpected.unlink()
        else:
            unexpected.rmdir()


def test_timestamp_floor_ignores_unrecognized_jsonl_symlink(tmp_path, sidecar):
    runner = _runner(tmp_path, sidecar)
    created_at = json.loads(
        (runner.out_dir / "run_metadata.json").read_text()
    )["created_at_utc"]
    outside = tmp_path / "outside-timestamp.jsonl"
    outside.write_text(
        json.dumps({"timestamp_utc": "2099-01-01T00:00:00Z"}) + "\n",
        encoding="utf-8",
    )
    (runner.out_dir / "unexpected.jsonl").symlink_to(outside)

    resumed = _runner(tmp_path, sidecar)

    assert resumed._last_timestamp == cheap._parse_timestamp(created_at)


def test_access_crash_resumes_but_terminal_failure_requires_explicit_retry(
        tmp_path, sidecar):
    crash_driver = FakeCheapDriver(sidecar, crash_calls={1})
    crashed = _runner(tmp_path / "crash", sidecar, driver=crash_driver)
    with pytest.raises(RuntimeError, match="crash"):
        crashed.access()
    assert crashed.access()["measurement_ready"] is False
    crash_states = [json.loads(line)["state"] for line in (
        crashed.out_dir / "access/attempt-journal.jsonl"
    ).read_text().splitlines()]
    assert crash_states[:4] == [
        "started", "abandoned", "started", "succeeded",
    ]

    failed_driver = FakeCheapDriver(sidecar, fail_calls={1})
    failed = _runner(tmp_path / "failed", sidecar, driver=failed_driver)
    with pytest.raises(ValueError, match="explicit.*retry"):
        failed.access()
    with pytest.raises(ValueError, match="explicit.*retry"):
        failed.access()
    assert failed.access(retry_failed=True)["measurement_ready"] is False

    historical_failure = (
        failed.out_dir
        / "access/failures/gpt-5-nano/attempt-01.json"
    )
    historical_failure.unlink()
    with pytest.raises(ValueError, match="failure|artifact|journal"):
        failed.verify("access")


def test_access_enforces_three_attempt_ceiling(tmp_path, sidecar):
    runner = _runner(
        tmp_path, sidecar,
        driver=FakeCheapDriver(sidecar, crash_calls={1, 2, 3}),
    )
    for _ in range(3):
        with pytest.raises(RuntimeError, match="crash"):
            runner.access()
    with pytest.raises(ValueError, match="three|3|attempt"):
        runner.access()


@pytest.mark.parametrize("tamper", ["missing", "rehashed"])
def test_access_retry_validates_prior_failure_before_new_driver_call(
        tmp_path, sidecar, tamper):
    driver = FakeCheapDriver(sidecar, fail_calls={1})
    runner = _runner(tmp_path, sidecar, driver=driver)
    with pytest.raises(ValueError, match="explicit.*retry"):
        runner.access()
    path = runner.out_dir / "access/failures/gpt-5-nano/attempt-01.json"
    if tamper == "missing":
        path.unlink()
    else:
        payload = json.loads(path.read_text())
        payload["profile_id"] = "tampered-profile"
        payload["access_artifact_sha256"] = contracts.canonical_sha256({
            key: value for key, value in payload.items()
            if key != "access_artifact_sha256"
        })
        path.write_text(json.dumps(payload), encoding="utf-8")
    call_count = len(driver.calls)

    with pytest.raises(
            ValueError, match="failure|artifact|journal|hash|profile"):
        runner.access(retry_failed=True)
    assert len(driver.calls) == call_count


def test_canary_is_exactly_one_public_item_per_cue_and_smoke_reuses_it(
        tmp_path, sidecar):
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()

    canary = runner.canary()
    canary_ids = canary["public_item_ids"]
    assert len(canary_ids) == len(set(canary_ids)) == 4
    assert {sidecar[item_id]["cue_variant"] for item_id in canary_ids} == {
        "strong", "weak", "absent", "adversarial",
    }
    bank_calls_after_canary = [row for row in driver.calls
                               if not row[0].startswith("CHEAP-ACCESS-")]
    assert len(bank_calls_after_canary) == 12

    smoke = runner.smoke()
    bank_calls_after_smoke = [row for row in driver.calls
                              if not row[0].startswith("CHEAP-ACCESS-")]
    assert len(bank_calls_after_smoke) == 36
    assert smoke["model_episode_count"] == 36
    assert smoke["reused_canary_model_episode_count"] == 12
    assert all(sum(row[0] == item_id and row[1] == model
                   for row in bank_calls_after_smoke) == 1
               for item_id in canary_ids for model in CHEAP_MODELS)
    assert runner.verify("smoke")["valid"] is True

    extra = runner.out_dir / "episodes" / canary_ids[0] / "extra-model.json"
    extra.write_text("{}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="artifact|coverage|extra"):
        runner.verify("smoke")


def test_smoke_crash_resume_and_exact_identity_tamper_detection(
        tmp_path, sidecar):
    driver = FakeCheapDriver(sidecar, crash_calls={4})
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()
    with pytest.raises(RuntimeError, match="crash"):
        runner.canary()
    runner.canary()
    runner.smoke()

    artifact = next((runner.out_dir / "episodes").rglob("*.json"))
    payload = json.loads(artifact.read_text())
    payload["profile_id"] = "different-profile"
    artifact.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="profile|hash|identity"):
        runner.verify("smoke")


def test_interrupted_stage_evidence_remains_journal_bound_after_resume(
        tmp_path, sidecar):
    driver = FakeCheapDriver(
        sidecar, crash_after_stages={(4, "stage_2")},
    )
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()
    item_id = runner.canary_item_ids[0]
    model = CHEAP_MODELS[0]

    with pytest.raises(RuntimeError, match="post-stage crash"):
        runner.canary()
    historical_stage = (
        runner.out_dir / "evidence" / item_id / model
        / "attempt-01/stage_2.json"
    )
    assert historical_stage.is_file()

    runner.canary()
    historical_stage.unlink()
    with pytest.raises(ValueError, match="evidence|journal|artifact"):
        runner.verify("canary")


@pytest.mark.parametrize("tamper", ["missing-terminal", "rehashed-stage"])
def test_episode_retry_validates_prior_artifacts_before_new_driver_call(
        tmp_path, sidecar, tamper):
    driver = FakeCheapDriver(sidecar, fail_calls={4})
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()
    with pytest.raises(ValueError, match="explicit.*retry"):
        runner.canary()
    item_id = runner.canary_item_ids[0]
    model = CHEAP_MODELS[0]
    if tamper == "missing-terminal":
        path = (
            runner.out_dir / "failures/episodes" / item_id / model
            / "attempt-01.json"
        )
        path.unlink()
    else:
        path = (
            runner.out_dir / "evidence" / item_id / model
            / "attempt-01/stage_1.json"
        )
        payload = json.loads(path.read_text())
        payload["profile_id"] = "tampered-profile"
        payload["stage_artifact_sha256"] = contracts.canonical_sha256({
            key: value for key, value in payload.items()
            if key != "stage_artifact_sha256"
        })
        path.write_text(json.dumps(payload), encoding="utf-8")
    call_count = len(driver.calls)

    with pytest.raises(
            ValueError, match="failure|artifact|journal|hash|profile|evidence"):
        runner.canary(retry_failed=True)
    assert len(driver.calls) == call_count


def test_report_is_qualification_only_and_reports_auc_update_and_ranges(
        tmp_path, sidecar):
    runner = _runner(tmp_path, sidecar)
    runner.access()
    runner.canary()
    runner.smoke()

    report = runner.report()

    assert report["purpose"] == "qualification-only"
    assert report["authorizes_calibration"] is False
    assert report["authorizes_private_execution"] is False
    assert report["authorizes_freeze"] is False
    assert report["qualification_measurement_class"] == (
        "cheap OpenRouter qualification measurement"
    )
    assert report["measurement_label"] == MOCK_PROVENANCE
    assert report["measurement_ready"] is False
    assert set(report["model_reports"]) == set(CHEAP_MODELS)
    assert all(0.0 <= row["empirical_auc"] <= 1.0
               for row in report["model_reports"].values())
    assert all(0.0 <= row["stage3_update_accuracy"] <= 1.0
               for row in report["model_reports"].values())
    assert set(report["between_model_ranges"]) == {
        "empirical_auc", "stage3_update_accuracy",
    }
    assert report["report_sha256"] == contracts.canonical_sha256({
        key: value for key, value in report.items()
        if key != "report_sha256"
    })


def test_verify_all_includes_and_semantically_replays_qualification_report(
        tmp_path, sidecar):
    runner = _runner(tmp_path, sidecar)
    runner.access()
    runner.canary()
    runner.smoke()
    runner.report()

    verification = runner.verify("all")
    includes_qualification = "qualification" in verification["scopes"]

    path = runner.out_dir / "reports/qualification.json"
    original = json.loads(path.read_text())
    tampered_reports = []
    authorization_type_tamper = deepcopy(original)
    authorization_type_tamper["authorizes_freeze"] = 0
    tampered_reports.append((authorization_type_tamper, False))
    metric_type_tamper = deepcopy(original)
    metric_type_tamper["model_reports"][CHEAP_MODELS[0]][
        "mechanically_resolved_rate"
    ] = 1
    tampered_reports.append((metric_type_tamper, True))
    metric_tamper = deepcopy(original)
    metric_tamper["model_reports"][CHEAP_MODELS[0]]["empirical_auc"] = -1.0
    tampered_reports.append((metric_tamper, True))
    for field in (
            "authorizes_calibration", "authorizes_private_execution",
            "authorizes_freeze"):
        authorization_tamper = deepcopy(original)
        authorization_tamper[field] = True
        tampered_reports.append((authorization_tamper, True))

    rejects_semantic_tampering = []
    for tampered, rehash in tampered_reports:
        if rehash:
            tampered["report_sha256"] = contracts.canonical_sha256({
                key: value for key, value in tampered.items()
                if key != "report_sha256"
            })
        path.write_text(json.dumps(tampered), encoding="utf-8")
        with pytest.raises(ValueError):
            runner.verify("all")
        rejects_semantic_tampering.append(True)

    assert includes_qualification is True
    assert all(rejects_semantic_tampering)


def test_cli_exposes_only_safe_qualification_commands():
    completed = subprocess.run(
        [sys.executable, "pilot/run_cheap_openrouter.py", "--help"],
        cwd=BANK,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert "{access,canary,smoke,verify,report}" in completed.stdout
    for forbidden in ("calibration", "reliability", "freeze", "private"):
        rejected = subprocess.run(
            [
                sys.executable, "pilot/run_cheap_openrouter.py", forbidden,
                "--out", "/tmp/forbidden-charitroc-command",
                "--run-mode", "live",
            ],
            cwd=BANK,
            capture_output=True,
            text=True,
            check=False,
        )
        assert rejected.returncode != 0
        assert "invalid choice" in rejected.stderr
