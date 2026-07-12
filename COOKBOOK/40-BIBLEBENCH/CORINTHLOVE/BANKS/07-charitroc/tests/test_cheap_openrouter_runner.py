"""Offline qualification-runner tests for CHARITROC's cheap OpenRouter panel."""
from __future__ import annotations

import base64
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
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
EXPECTED_RETURNED_MODEL_IDS = {
    "gpt-5-nano": "openai/gpt-5-nano-2025-08-07",
    "gpt-5.4-nano": "openai/gpt-5.4-nano-20260317",
    "gpt-5-mini": "openai/gpt-5-mini-2025-08-07",
    "gpt-5.4-mini": "openai/gpt-5.4-mini-20260317",
}
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
        logical_model_id = provider_model_id.removeprefix("openai/")
        endpoint = {
            "name": (
                "Azure | "
                f"{EXPECTED_RETURNED_MODEL_IDS[logical_model_id]}"
            ),
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


def test_runner_credential_scan_allows_embedded_ciphertext_token_fragment():
    cheap._assert_no_credentials({
        "encrypted_reasoning": "prefixsk-abcdefghijklmnop",
    })


@pytest.mark.parametrize("secret", [
    "sk-or-v1-abcdefghijklmnop",
    "rk-live-abcdefghijklmnop",
    "Bearer opaque-credential-value",
])
def test_runner_credential_scan_rejects_standalone_common_secrets(secret):
    with pytest.raises(ValueError, match="credential"):
        cheap._assert_no_credentials({"provider_payload": secret})


class FakeCheapDriver:
    """Explicit mock dependency emitting real validated stage contracts."""

    def __init__(
            self, sidecar, *, crash_calls=(), crash_after_stages=(),
            fail_calls=(), returned_model_ids=None):
        self.sidecar = deepcopy(sidecar)
        self.crash_calls = set(crash_calls)
        self.crash_after_stages = set(crash_after_stages)
        self.fail_calls = set(fail_calls)
        self.returned_model_ids = dict(returned_model_ids or {})
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
                returned_provider_model_id=self.returned_model_ids.get(
                    logical_model_id,
                    EXPECTED_RETURNED_MODEL_IDS[logical_model_id],
                ),
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
        tmp_path, sidecar, *, driver=None, catalog=None, bank_root=BANK,
        profile_id=manifest.CHEAP_PROFILE_ID):
    return cheap.CheapOpenRouterQualificationRunner(
        bank_root=bank_root,
        out_dir=tmp_path / "qualification",
        run_mode="mock",
        driver=driver or FakeCheapDriver(sidecar),
        catalog_loader=catalog or FakeCatalog(),
        clock=TickClock(),
        profile_id=profile_id,
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


def test_gpt54_mini_profile_completes_public_smoke_report_and_all_verify(
        tmp_path, sidecar):
    runner = _runner(
        tmp_path,
        sidecar,
        profile_id=manifest.GPT54_MINI_PROFILE_ID,
    )
    metadata = json.loads((runner.out_dir / "run_metadata.json").read_text())

    assert metadata["profile_id"] == manifest.GPT54_MINI_PROFILE_ID
    assert metadata["profile_sha256"] == (
        manifest.qualification_panel_sha256(
            manifest.GPT54_MINI_PROFILE_ID
        )
    )
    assert metadata["logical_model_ids"] == ["gpt-5.4-mini"]
    assert metadata["provider_model_ids"] == ["openai/gpt-5.4-mini"]

    access = runner.access()
    canary = runner.canary()
    smoke = runner.smoke()
    report = runner.report()
    verified = runner.verify("all")

    assert access["models"] == ["gpt-5.4-mini"]
    assert len(access["probes"]) == 1
    assert access["probes"][0]["logical_model_id"] == "gpt-5.4-mini"
    assert canary["model_episode_count"] == 4
    assert smoke["model_episode_count"] == 12
    assert smoke["reused_canary_model_episode_count"] == 4
    assert report["profile_id"] == manifest.GPT54_MINI_PROFILE_ID
    assert set(report["model_reports"]) == {"gpt-5.4-mini"}
    assert report["public_episode_count_per_model"] == 12
    assert report["between_model_ranges"]["empirical_auc"]["range"] == 0.0
    assert verified["valid"] is True
    assert verified["profile_id"] == manifest.GPT54_MINI_PROFILE_ID


def test_runner_rejects_arbitrary_qualification_profile_before_artifacts(
        tmp_path, sidecar):
    out = tmp_path / "unfrozen"
    with pytest.raises(ValueError, match="qualification|profile|frozen"):
        cheap.CheapOpenRouterQualificationRunner(
            bank_root=BANK,
            out_dir=out,
            run_mode="mock",
            driver=FakeCheapDriver(sidecar),
            catalog_loader=FakeCatalog(),
            clock=TickClock(),
            profile_id="unfrozen-profile",
        )
    assert not out.exists()


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


def test_live_dispatches_access_and_public_qualification_to_dedicated_apis(
        tmp_path, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "runner-test-key")
    runner = cheap.CheapOpenRouterQualificationRunner(
        bank_root=BANK,
        out_dir=tmp_path / "live",
        run_mode="live",
    )
    calls = []
    before_stage = lambda _event: None
    stage_sink = lambda _event: None

    def access_api(
            *, logical_model_id, api_key, before_stage, stage_sink,
            profile_id):
        calls.append((
            "access", logical_model_id, api_key, before_stage, stage_sink,
            profile_id,
        ))
        return {"dedicated": "access"}

    def qualification_api(
            episode, *, logical_model_id, purpose, api_key,
            before_stage, stage_sink, profile_id):
        calls.append((
            purpose, episode["id"], logical_model_id, api_key,
            before_stage, stage_sink, profile_id,
        ))
        return {"dedicated": purpose}

    monkeypatch.setattr(
        cheap.openrouter_driver, "run_live_access_probe", access_api
    )
    monkeypatch.setattr(
        cheap.openrouter_driver,
        "run_live_cheap_qualification_episode",
        qualification_api,
    )
    model = CHEAP_MODELS[0]
    probe = manifest.build_cheap_access_probe(model)
    public = runner.public_episodes[0]

    assert runner._call_driver(
        probe, model, purpose="access",
        before_stage=before_stage, stage_sink=stage_sink,
    ) == {"dedicated": "access"}
    assert runner._call_driver(
        public, model, purpose="canary",
        before_stage=before_stage, stage_sink=stage_sink,
    ) == {"dedicated": "canary"}
    assert runner._call_driver(
        public, model, purpose="smoke",
        before_stage=before_stage, stage_sink=stage_sink,
    ) == {"dedicated": "smoke"}
    assert calls == [
        (
            "access", model, "runner-test-key", before_stage, stage_sink,
            manifest.CHEAP_PROFILE_ID,
        ),
        (
            "canary", public["id"], model, "runner-test-key",
            before_stage, stage_sink, manifest.CHEAP_PROFILE_ID,
        ),
        (
            "smoke", public["id"], model, "runner-test-key",
            before_stage, stage_sink, manifest.CHEAP_PROFILE_ID,
        ),
    ]


def test_mock_dispatch_keeps_explicit_fake_run_episode(
        tmp_path, sidecar, monkeypatch):
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver)
    monkeypatch.setattr(
        cheap.openrouter_driver,
        "run_live_cheap_qualification_episode",
        lambda *_args, **_kwargs: pytest.fail("mock reached live API"),
    )

    run = runner._call_driver(
        runner.public_episodes[0], CHEAP_MODELS[0], purpose="canary",
        before_stage=None, stage_sink=None,
    )

    assert run["status"] == "complete"
    assert driver.calls == [(
        runner.public_episodes[0]["id"],
        CHEAP_MODELS[0],
        manifest.CHEAP_PROFILE_ID,
    )]


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
    for row in report["models"]:
        assert row["eligible_azure_endpoints"] == [{
            "catalog_endpoint_index": 0,
            "provider_name": "Azure",
            "returned_provider_model_id": EXPECTED_RETURNED_MODEL_IDS[
                row["logical_model_id"]
            ],
            "context_length": 400000,
            "required_parameters_present": sorted(REQUIRED_PARAMETERS),
            "input_usd_per_million_tokens": "0.01",
            "output_usd_per_million_tokens": "0.1",
        }]


def test_catalog_preflight_allows_multiple_individually_eligible_azure_endpoints(
        tmp_path, sidecar):
    def duplicate(payload, _model):
        second = deepcopy(payload["data"]["endpoints"][0])
        payload["data"]["endpoints"].append(second)

    runner = _runner(tmp_path, sidecar, catalog=FakeCatalog(mutate=duplicate))
    report = runner.preflight_catalog()

    assert [row["eligible_azure_endpoint_count"]
            for row in report["models"]] == [2, 2, 2]


@pytest.mark.parametrize("name", [
    "Azure exact endpoint",
    "Azure | openai/gpt-5-nano",
    "Azure | openai/gpt-5-nano-2025-08-07-substitute",
])
def test_catalog_preflight_rejects_nonexact_snapshot_endpoint_names(
        tmp_path, sidecar, name):
    def substitute(payload, provider_model_id):
        if provider_model_id == "openai/gpt-5-nano":
            payload["data"]["endpoints"][0]["name"] = name

    runner = _runner(
        tmp_path, sidecar, catalog=FakeCatalog(mutate=substitute)
    )

    with pytest.raises(ValueError, match="eligible|snapshot|endpoint"):
        runner.preflight_catalog()


def test_persisted_catalog_rejects_rehashed_snapshot_substitution(
        tmp_path, sidecar):
    runner = _runner(tmp_path, sidecar)
    runner.preflight_catalog()
    path = runner.out_dir / "catalog/preflight.json"
    report = json.loads(path.read_text())
    report["models"][0]["eligible_azure_endpoints"][0][
        "returned_provider_model_id"
    ] = "openai/gpt-5-nano-substitute"
    report["catalog_preflight_sha256"] = contracts.canonical_sha256({
        key: value for key, value in report.items()
        if key != "catalog_preflight_sha256"
    })
    path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(ValueError, match="catalog|endpoint|snapshot"):
        runner._validate_catalog_artifact()


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


def test_live_access_readiness_requires_exact_probe_provenance_and_false_measurement(
        tmp_path):
    runner = cheap.CheapOpenRouterQualificationRunner(
        bank_root=BANK,
        out_dir=tmp_path / "live-access",
        run_mode="live",
    )
    model = CHEAP_MODELS[0]
    identity = runner.identities[model]
    probe = manifest.build_cheap_access_probe(model)
    request = contracts.build_stage_request(
        probe,
        execution_id="9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        provider="openrouter",
        logical_model_id=model,
        provider_model_id=identity["provider_model_id"],
        configuration_id=identity["configuration_id"],
        stage="stage_1",
        prior_responses={},
    )
    descriptor = {
        "fixture": "live-access-probe",
        "request_sha256": request["request_sha256"],
    }
    raw = _response("UNCERTAIN", "VERIFY", "Access probe.")
    attempt = contracts.build_stage_attempt(
        attempt_index=1,
        started_at_utc="2026-07-11T01:00:00Z",
        completed_at_utc="2026-07-11T01:00:01Z",
        provider_request_id="probe-fixture",
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
    result = contracts.build_stage_result(
        request,
        run_mode="openrouter_probe",
        returned_provider_model_id=EXPECTED_RETURNED_MODEL_IDS[model],
        returned_provider_name="Azure",
        session_id=None,
        transport_request_sha256=contracts.canonical_sha256(descriptor),
        attempts=[attempt],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )
    event = {
        "provider": "openrouter",
        "integrity_session": 1,
        "execution_id": request["execution_id"],
        "stage": "stage_1",
        "request": request,
        "transport_descriptor": descriptor,
        "attestation": None,
        "result": result,
    }

    assert result["provenance"] == (
        "live OpenRouter access probe, NOT a measurement"
    )
    assert result["integrity"]["measurement_ready"] is False
    assert runner._access_ready(request, result) is True
    artifact = runner._build_access_artifact(model, 1, event)
    assert artifact["provenance"] == (
        "model access probe, NOT a measurement"
    )
    assert artifact["measurement_ready"] is False
    assert artifact["ready"] is True
    assert artifact["result"]["provenance"] == result["provenance"]

    wrong = deepcopy(result)
    wrong["provenance"] = "live OpenRouter qualification measurement"
    assert runner._access_ready(request, wrong) is False

    requested_alias = deepcopy(result)
    requested_alias["returned_provider_model_id"] = identity[
        "provider_model_id"
    ]
    assert runner._access_ready(request, requested_alias) is False

    mismatched_snapshot = deepcopy(result)
    mismatched_snapshot["returned_provider_model_id"] = (
        "openai/gpt-5-nano-2025-08-07-substitute"
    )
    assert runner._access_ready(request, mismatched_snapshot) is False

    forged_probe = deepcopy(probe)
    forged_probe["multiturn_script"]["stage_1"] += " Arbitrary prompt."
    forged_request = contracts.build_stage_request(
        forged_probe,
        execution_id=request["execution_id"],
        provider="openrouter",
        logical_model_id=model,
        provider_model_id=identity["provider_model_id"],
        configuration_id=identity["configuration_id"],
        stage="stage_1",
        prior_responses={},
    )
    forged_descriptor = {
        "fixture": "forged-live-access-probe",
        "request_sha256": forged_request["request_sha256"],
    }
    forged_result = contracts.build_stage_result(
        forged_request,
        run_mode="openrouter_probe",
        returned_provider_model_id=EXPECTED_RETURNED_MODEL_IDS[model],
        returned_provider_name="Azure",
        session_id=None,
        transport_request_sha256=contracts.canonical_sha256(
            forged_descriptor
        ),
        attempts=[attempt],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )
    forged_artifact = deepcopy(artifact)
    forged_artifact.update({
        "request": forged_request,
        "result": forged_result,
        "transport_descriptor": forged_descriptor,
        "ready": True,
        "failure_kind": None,
    })
    forged_artifact["access_artifact_sha256"] = contracts.canonical_sha256({
        key: value for key, value in forged_artifact.items()
        if key != "access_artifact_sha256"
    })

    assert runner._access_ready(forged_request, forged_result) is False
    with pytest.raises(ValueError, match="access|probe|request|evidence"):
        runner._validate_access_artifact(forged_artifact, model, 1)


def test_episode_readiness_requires_frozen_returned_snapshot(
        tmp_path, sidecar):
    model = CHEAP_MODELS[0]
    snapshot_driver = FakeCheapDriver(
        sidecar,
        returned_model_ids={model: EXPECTED_RETURNED_MODEL_IDS[model]},
    )
    runner = _runner(tmp_path, sidecar, driver=snapshot_driver)
    item_id = sorted(runner._by_id)[0]
    episode = runner._by_id[item_id]

    snapshot_run = snapshot_driver.run_episode(
        episode,
        logical_model_id=model,
        panel_profile=manifest.CHEAP_PROFILE_ID,
    )
    alias_run = FakeCheapDriver(
        sidecar,
        returned_model_ids={model: runner.identities[model][
            "provider_model_id"]},
    ).run_episode(
        episode,
        logical_model_id=model,
        panel_profile=manifest.CHEAP_PROFILE_ID,
    )
    mismatch_run = FakeCheapDriver(
        sidecar,
        returned_model_ids={model: "openai/gpt-5-nano-substitute"},
    ).run_episode(
        episode,
        logical_model_id=model,
        panel_profile=manifest.CHEAP_PROFILE_ID,
    )

    assert runner._episode_ready(snapshot_run, model) is True
    assert runner._episode_ready(alias_run, model) is False
    assert runner._episode_ready(mismatch_run, model) is False


def test_live_access_protocol_failure_is_durable_and_requires_explicit_retry(
        tmp_path, monkeypatch):
    runner = cheap.CheapOpenRouterQualificationRunner(
        bank_root=BANK,
        out_dir=tmp_path / "live-protocol-failure",
        run_mode="live",
    )
    model = CHEAP_MODELS[0]
    identity = runner.identities[model]
    probe = manifest.build_cheap_access_probe(model)
    request = contracts.build_stage_request(
        probe,
        execution_id="9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        provider="openrouter",
        logical_model_id=model,
        provider_model_id=identity["provider_model_id"],
        configuration_id=identity["configuration_id"],
        stage="stage_1",
        prior_responses={},
    )
    descriptor = {
        "fixture": "live-protocol-failure",
        "request_sha256": request["request_sha256"],
    }
    raw = b"\xff"
    failure_record = {
        "failure_record_version": "charitroc-openrouter-failure-v1",
        "provenance": (
            "live OpenRouter access probe attempt, NOT a measurement"
        ),
        "run_mode": "openrouter_probe",
        "measurement_ready": False,
        "failure_kind": "invalid_utf8",
        "raw_bytes_base64": base64.b64encode(raw).decode("ascii"),
        "raw_bytes_sha256": hashlib.sha256(raw).hexdigest(),
        "raw_byte_count": 1,
        "raw_redacted": False,
        "provider": "openrouter",
        "logical_model_id": model,
        "model": identity["provider_model_id"],
        "provider_model_id": identity["provider_model_id"],
        "configuration_id": identity["configuration_id"],
        "request_sha256": request["request_sha256"],
        "transport_request_sha256": contracts.canonical_sha256(descriptor),
    }
    calls = []

    def failed_probe(
            episode, observed_model, *, purpose, before_stage, stage_sink):
        calls.append((episode, observed_model, purpose))
        before_stage({
            "provider": "openrouter",
            "integrity_session": 1,
            "execution_id": request["execution_id"],
            "stage": "stage_1",
            "request": deepcopy(request),
            "transport_descriptor": deepcopy(descriptor),
            "attestation": None,
        })
        return {
            "status": "failed",
            "provenance": failure_record["provenance"],
            "measurement_ready": False,
            "integrity_session_count": 1,
            "sessions": [],
            "requests": [deepcopy(request)],
            "results": [],
            "transport_descriptors": [],
            "chain": None,
            "failure_record": deepcopy(failure_record),
        }

    monkeypatch.setattr(runner, "_call_driver", failed_probe)

    with pytest.raises(ValueError, match="explicit.*retry"):
        runner._run_access_model(model, 1)

    events = runner._access_events()
    assert [event["state"] for event in events] == ["started", "failed"]
    artifact = runner._validate_access_artifact(
        json.loads(runner._access_failure_path(model, 1).read_text()),
        model,
        1,
    )
    assert artifact["ready"] is False
    assert artifact["failure_kind"] == "provider_terminal_failure"
    assert artifact["failure_record"] == failure_record
    with pytest.raises(ValueError, match="explicit.*retry"):
        runner._prepare_access_attempt(model, retry_failed=False)
    assert len(calls) == 1


@pytest.mark.parametrize("artifact_kind", ["success", "protocol-failure"])
@pytest.mark.parametrize("validation_path", ["reconcile", "history"])
def test_access_artifact_from_different_execution_cannot_bind_to_start(
        tmp_path, sidecar, artifact_kind, validation_path):
    model = CHEAP_MODELS[0]
    run_mode = "mock" if artifact_kind == "success" else "live"
    if run_mode == "mock":
        source = _runner(tmp_path / "source", sidecar)
        target = _runner(tmp_path / "target", sidecar)
        source._run_access_model(model, 1)
        source_path = source._access_success_path(model)
        target_path = target._access_success_path(model)
        terminal_state = "succeeded"
        terminal_kind = "validated_probe"
    else:
        source = cheap.CheapOpenRouterQualificationRunner(
            bank_root=BANK,
            out_dir=tmp_path / "source-live",
            run_mode="live",
        )
        target = cheap.CheapOpenRouterQualificationRunner(
            bank_root=BANK,
            out_dir=tmp_path / "target-live",
            run_mode="live",
        )
        identity = source.identities[model]
        source_probe = manifest.build_cheap_access_probe(model)
        source_request = contracts.build_stage_request(
            source_probe,
            execution_id="9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
            provider="openrouter",
            logical_model_id=model,
            provider_model_id=identity["provider_model_id"],
            configuration_id=identity["configuration_id"],
            stage="stage_1",
            prior_responses={},
        )
        source_descriptor = {
            "fixture": "foreign-protocol-failure",
            "request_sha256": source_request["request_sha256"],
        }
        raw = b"\xff"
        failure_record = {
            "failure_record_version": "charitroc-openrouter-failure-v1",
            "provenance": (
                "live OpenRouter access probe attempt, NOT a measurement"
            ),
            "run_mode": "openrouter_probe",
            "measurement_ready": False,
            "failure_kind": "invalid_utf8",
            "raw_bytes_base64": base64.b64encode(raw).decode("ascii"),
            "raw_bytes_sha256": hashlib.sha256(raw).hexdigest(),
            "raw_byte_count": len(raw),
            "raw_redacted": False,
            "provider": "openrouter",
            "logical_model_id": model,
            "model": identity["provider_model_id"],
            "provider_model_id": identity["provider_model_id"],
            "configuration_id": identity["configuration_id"],
            "request_sha256": source_request["request_sha256"],
            "transport_request_sha256": contracts.canonical_sha256(
                source_descriptor
            ),
        }
        failure_run = {
            "status": "failed",
            "provenance": failure_record["provenance"],
            "measurement_ready": False,
            "integrity_session_count": 1,
            "sessions": [],
            "requests": [source_request],
            "results": [],
            "transport_descriptors": [],
            "chain": None,
            "failure_record": failure_record,
        }
        source_event = {
            "provider": "openrouter",
            "integrity_session": 1,
            "execution_id": source_request["execution_id"],
            "stage": "stage_1",
            "request": source_request,
            "transport_descriptor": source_descriptor,
            "attestation": None,
        }
        source_artifact = source._build_access_protocol_failure_artifact(
            model, 1, failure_run, source_event
        )
        source_path = source._access_failure_path(model, 1)
        cheap._write_new_json(source_path, source_artifact)
        target_path = target._access_failure_path(model, 1)
        terminal_state = "failed"
        terminal_kind = "provider_terminal_failure"

    target_identity = target.identities[model]
    target_request = contracts.build_stage_request(
        manifest.build_cheap_access_probe(model),
        execution_id="54c94821-a36c-4ea7-ae2c-568a1a4410ef",
        provider="openrouter",
        logical_model_id=model,
        provider_model_id=target_identity["provider_model_id"],
        configuration_id=target_identity["configuration_id"],
        stage="stage_1",
        prior_responses={},
    )
    target_descriptor = {
        "fixture": "active-target-start",
        "request_sha256": target_request["request_sha256"],
    }
    start = target._append_access_event(
        model=model,
        attempt=1,
        state="started",
        request_sha=target_request["request_sha256"],
        descriptor_sha=contracts.canonical_sha256(target_descriptor),
    )
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)

    if validation_path == "history":
        target._append_access_event(
            model=model,
            attempt=1,
            state=terminal_state,
            request_sha=start["request_sha256"],
            descriptor_sha=start["transport_descriptor_sha256"],
            start=start,
            artifact=target_path,
            terminal_kind=terminal_kind,
        )
        operation = lambda: target._validate_access_history(
            target._access_events()
        )
    else:
        operation = lambda: target._reconcile_access_orphan(
            model, target._access_events()
        )

    event_count = len(target._access_events())
    with pytest.raises(
            ValueError, match="access|artifact|request|descriptor|start|binding"):
        operation()
    assert len(target._access_events()) == event_count


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


def test_access_retry_reuses_validated_frozen_catalog_without_refetch(
        tmp_path, sidecar):
    driver = FakeCheapDriver(sidecar, fail_calls={1})
    catalog = FakeCatalog()
    runner = _runner(
        tmp_path, sidecar, driver=driver, catalog=catalog
    )
    with pytest.raises(ValueError, match="explicit.*retry"):
        runner.access()
    frozen_path = runner.out_dir / "catalog/preflight.json"
    frozen_bytes = frozen_path.read_bytes()
    assert len(catalog.calls) == len(CHEAP_MODELS)

    class ForbiddenCatalog:
        def __init__(self):
            self.calls = []

        def __call__(self, provider_model_id):
            self.calls.append(provider_model_id)
            raise AssertionError("frozen catalog must not be refetched")

    forbidden = ForbiddenCatalog()
    runner._catalog_loader = forbidden

    report = runner.access(retry_failed=True)

    assert report["measurement_ready"] is False
    assert forbidden.calls == []
    assert frozen_path.read_bytes() == frozen_bytes


def test_access_retry_rejects_tampered_frozen_catalog_before_driver_call(
        tmp_path, sidecar):
    driver = FakeCheapDriver(sidecar, fail_calls={1})
    runner = _runner(tmp_path, sidecar, driver=driver)
    with pytest.raises(ValueError, match="explicit.*retry"):
        runner.access()
    path = runner.out_dir / "catalog/preflight.json"
    report = json.loads(path.read_text())
    report["models"][0]["eligible_azure_endpoints"][0][
        "returned_provider_model_id"
    ] = "openai/gpt-5-nano-substitute"
    report["catalog_preflight_sha256"] = contracts.canonical_sha256({
        key: value for key, value in report.items()
        if key != "catalog_preflight_sha256"
    })
    path.write_text(json.dumps(report), encoding="utf-8")
    driver_call_count = len(driver.calls)

    class ForbiddenCatalog:
        calls = []

        def __call__(self, provider_model_id):
            self.calls.append(provider_model_id)
            raise AssertionError("tampered frozen catalog must not refetch")

    forbidden = ForbiddenCatalog()
    runner._catalog_loader = forbidden

    with pytest.raises(ValueError, match="catalog|endpoint|snapshot"):
        runner.access(retry_failed=True)

    assert forbidden.calls == []
    assert len(driver.calls) == driver_call_count


def test_canary_is_exactly_one_public_item_per_cue_and_smoke_reuses_it(
        tmp_path, sidecar):
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()

    class ForbiddenCatalog:
        def __init__(self):
            self.calls = []

        def __call__(self, provider_model_id):
            self.calls.append(provider_model_id)
            raise AssertionError("frozen catalog must not be refetched")

    forbidden = ForbiddenCatalog()
    runner._catalog_loader = forbidden

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
    assert forbidden.calls == []
    assert runner.verify("smoke")["valid"] is True

    extra = runner.out_dir / "episodes" / canary_ids[0] / "extra-model.json"
    extra.write_text("{}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="artifact|coverage|extra"):
        runner.verify("smoke")


def test_canary_rejects_tampered_frozen_catalog_before_driver_call(
        tmp_path, sidecar):
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()
    path = runner.out_dir / "catalog/preflight.json"
    report = json.loads(path.read_text())
    report["models"][0]["eligible_azure_endpoints"][0][
        "returned_provider_model_id"
    ] = "openai/gpt-5-nano-substitute"
    report["catalog_preflight_sha256"] = contracts.canonical_sha256({
        key: value for key, value in report.items()
        if key != "catalog_preflight_sha256"
    })
    path.write_text(json.dumps(report), encoding="utf-8")
    driver_call_count = len(driver.calls)

    class ForbiddenCatalog:
        calls = []

        def __call__(self, provider_model_id):
            self.calls.append(provider_model_id)
            raise AssertionError("tampered frozen catalog must not refetch")

    forbidden = ForbiddenCatalog()
    runner._catalog_loader = forbidden

    with pytest.raises(ValueError, match="catalog|endpoint|snapshot"):
        runner.canary()

    assert forbidden.calls == []
    assert len(driver.calls) == driver_call_count


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


@pytest.mark.parametrize("crash_on", [1, 2])
def test_stage_artifact_crash_window_reconciles_before_abandon_and_retry(
        tmp_path, sidecar, monkeypatch, crash_on):
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()
    item_id = runner.canary_item_ids[0]
    model = CHEAP_MODELS[0]
    original_append = runner._append_stage_evidence_event
    append_count = 0

    def crash_first_stage_journal_append(**kwargs):
        nonlocal append_count
        append_count += 1
        if append_count == crash_on:
            raise RuntimeError("simulated post-stage-file journal crash")
        return original_append(**kwargs)

    monkeypatch.setattr(
        runner,
        "_append_stage_evidence_event",
        crash_first_stage_journal_append,
    )
    with pytest.raises(RuntimeError, match="stage-file journal crash"):
        runner.canary()

    orphan = (
        runner.out_dir / "evidence" / item_id / model
        / f"attempt-01/{contracts.STAGES[crash_on - 1]}.json"
    )
    assert orphan.is_file()
    journal_path = runner.out_dir / "evidence/stage-journal.jsonl"
    journal_before = (
        journal_path.read_text().splitlines() if journal_path.exists() else []
    )
    assert len(journal_before) == crash_on - 1

    resumed = _runner(tmp_path, sidecar, driver=driver)
    canary = resumed.canary()
    episode_events = resumed._episode_events()
    stage_events = resumed._stage_evidence_events(episode_events)
    adopted = [
        event for event in stage_events
        if event["item_id"] == item_id
        and event["logical_model_id"] == model
        and event["attempt_number"] == 1
    ]
    rows = resumed._arm_events(episode_events, item_id, model)

    assert [event["stage"] for event in adopted] == list(
        contracts.STAGES[:crash_on]
    )
    reconciled = adopted[-1]
    assert reconciled["previous_event_sha256"] == (
        adopted[-2]["event_sha256"] if crash_on == 2 else None
    )
    assert stage_events[crash_on]["previous_event_sha256"] == reconciled[
        "event_sha256"
    ]
    assert reconciled["artifact_sha256"] == cheap._file_sha(orphan)
    assert [event["state"] for event in rows[:4]] == [
        "started", "abandoned", "started", "succeeded",
    ]
    assert cheap._parse_timestamp(reconciled["timestamp_utc"]) < (
        cheap._parse_timestamp(rows[1]["timestamp_utc"])
    )
    bank_calls = [
        call for call in driver.calls
        if not call[0].startswith("CHEAP-ACCESS-")
    ]
    assert len(bank_calls) == 13
    assert canary["model_episode_count"] == 12
    assert resumed.verify("canary")["valid"] is True


@pytest.mark.parametrize("case", [
    "invalid", "noncontiguous", "multiple", "foreign-execution",
    "foreign-execution-journaled",
])
def test_stage_artifact_reconciliation_fails_closed_on_ambiguous_orphan(
        tmp_path, sidecar, monkeypatch, case):
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()
    item_id = runner.canary_item_ids[0]
    model = CHEAP_MODELS[0]
    original_append = runner._append_stage_evidence_event
    append_count = 0
    crash_on = 1 if case == "invalid" else 2

    def crash_selected_stage_journal_append(**kwargs):
        nonlocal append_count
        append_count += 1
        if append_count == crash_on:
            raise RuntimeError("simulated post-stage-file journal crash")
        return original_append(**kwargs)

    monkeypatch.setattr(
        runner,
        "_append_stage_evidence_event",
        crash_selected_stage_journal_append,
    )
    with pytest.raises(RuntimeError, match="stage-file journal crash"):
        runner.canary()

    attempt_dir = (
        runner.out_dir / "evidence" / item_id / model / "attempt-01"
    )
    if case == "invalid":
        path = attempt_dir / "stage_1.json"
        payload = json.loads(path.read_text())
        payload["profile_id"] = "tampered-profile"
        payload["stage_artifact_sha256"] = contracts.canonical_sha256({
            key: value for key, value in payload.items()
            if key != "stage_artifact_sha256"
        })
        path.write_text(json.dumps(payload), encoding="utf-8")
    elif case == "noncontiguous":
        (attempt_dir / "stage_1.json").unlink()
        (runner.out_dir / "evidence/stage-journal.jsonl").unlink()
        assert (attempt_dir / "stage_2.json").is_file()
    elif case == "multiple":
        shutil.copy2(
            attempt_dir / "stage_2.json",
            attempt_dir / "stage_3.json",
        )
    else:
        path = attempt_dir / "stage_2.json"
        payload = json.loads(path.read_text())
        request = payload["request"]
        result = payload["result"]
        request["execution_id"] = str(uuid.UUID(int=999, version=4))
        request["request_sha256"] = contracts.canonical_sha256({
            key: value for key, value in request.items()
            if key != "request_sha256"
        })
        result["execution_id"] = request["execution_id"]
        result["request_sha256"] = request["request_sha256"]
        result["result_sha256"] = contracts.canonical_sha256({
            key: value for key, value in result.items()
            if key != "result_sha256"
        })
        payload["stage_artifact_sha256"] = contracts.canonical_sha256({
            key: value for key, value in payload.items()
            if key != "stage_artifact_sha256"
        })
        path.write_text(json.dumps(payload), encoding="utf-8")
        if case == "foreign-execution-journaled":
            start = runner._episode_events()[0]
            original_append(
                item_id=item_id,
                model=model,
                source="canary",
                attempt=1,
                stage="stage_2",
                start=start,
                artifact_path=path,
                artifact=payload,
            )

    calls_before_resume = len(driver.calls)
    if case == "foreign-execution-journaled":
        with pytest.raises(
                ValueError, match="stage|evidence|request|execution|history"):
            _runner(tmp_path, sidecar, driver=driver)
        assert len(driver.calls) == calls_before_resume
        return
    resumed = _runner(tmp_path, sidecar, driver=driver)
    with pytest.raises(
            ValueError,
            match="stage|evidence|artifact|coverage|orphan|contiguous|ambiguous"):
        resumed.canary()
    assert len(driver.calls) == calls_before_resume


@pytest.mark.parametrize("arm_state", ["completed", "untouched"])
def test_unstarted_stage_artifact_fails_before_any_driver_call(
        tmp_path, sidecar, arm_state):
    driver = FakeCheapDriver(sidecar)
    runner = _runner(tmp_path, sidecar, driver=driver)
    runner.access()
    item_id = runner.canary_item_ids[0]
    model = CHEAP_MODELS[0]

    if arm_state == "completed":
        attempt = runner._prepare_episode_attempt(
            item_id, model, "canary", retry_failed=False
        )
        runner._run_episode_arm(item_id, model, "canary", attempt)
        source_path = runner._stage_path(item_id, model, 1, "stage_1")
        orphan_path = runner._stage_path(item_id, model, 2, "stage_1")
        payload = json.loads(source_path.read_text())
        payload["attempt_number"] = 2
        payload["stage_artifact_sha256"] = contracts.canonical_sha256({
            key: value for key, value in payload.items()
            if key != "stage_artifact_sha256"
        })
    else:
        source_driver = FakeCheapDriver(sidecar)
        source_runner = _runner(
            tmp_path / "source", sidecar, driver=source_driver
        )
        source_runner.access()
        attempt = source_runner._prepare_episode_attempt(
            item_id, model, "canary", retry_failed=False
        )
        source_runner._run_episode_arm(
            item_id, model, "canary", attempt
        )
        source_path = source_runner._stage_path(
            item_id, model, 1, "stage_1"
        )
        orphan_path = runner._stage_path(item_id, model, 1, "stage_1")
        payload = json.loads(source_path.read_text())

    orphan_path.parent.mkdir(parents=True, exist_ok=True)
    orphan_path.write_text(json.dumps(payload), encoding="utf-8")
    calls_before_resume = len(driver.calls)

    with pytest.raises(
            ValueError, match="stage|evidence|artifact|orphan|coverage"):
        runner.canary()
    assert len(driver.calls) == calls_before_resume


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


def test_gpt54_mini_cli_is_explicit_and_exposes_no_profile_switch():
    completed = subprocess.run(
        [sys.executable, "pilot/run_gpt54_mini_openrouter.py", "--help"],
        cwd=BANK,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    assert "GPT-5.4-mini" in completed.stdout
    assert "{access,canary,smoke,verify,report}" in completed.stdout
    assert "--profile" not in completed.stdout
    for forbidden in ("calibration", "reliability", "freeze", "private"):
        rejected = subprocess.run(
            [
                sys.executable, "pilot/run_gpt54_mini_openrouter.py",
                forbidden, "--out", "/tmp/forbidden-charitroc-mini-command",
                "--run-mode", "live",
            ],
            cwd=BANK,
            capture_output=True,
            text=True,
            check=False,
        )
        assert rejected.returncode != 0
        assert "invalid choice" in rejected.stderr
