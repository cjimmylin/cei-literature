"""Bounded 2,400-request cheap OpenRouter diagnostic contracts."""

from copy import deepcopy
import importlib
import json
from pathlib import Path
import subprocess
import sys
import time

import pytest


ROOT = Path(__file__).resolve().parents[1]
BENCH_ROOT = ROOT.parents[2]
CONFIG = ROOT / "configs" / "openrouter-cheap-full-engineering-diagnostic.json"
SMOKE_DIR = ROOT / "pilots" / "20260711-cheap-openrouter-smoke-r2"
FULL_R1_DIR = ROOT / "pilots" / "20260711-cheap-openrouter-full-r1"
for search_root in (ROOT, BENCH_ROOT):
    if str(search_root) not in sys.path:
        sys.path.insert(0, str(search_root))


def _module():
    try:
        return importlib.import_module("harness.run_openrouter_diagnostic")
    except ModuleNotFoundError as exc:
        if exc.name == "harness.run_openrouter_diagnostic":
            pytest.fail("harness.run_openrouter_diagnostic has not been implemented")
        raise


class _NoCallClient:
    def __init__(self, row):
        self.model_id = row["model_id"]
        self.family = row["family"]
        self.vendor = row["vendor"]
        self.provider = row["provider"]
        self.max_tokens = 256
        self.cost_cap_usd = 1.0
        self.calls = []

    def generate(self, request, *, seed):
        self.calls.append((deepcopy(request), seed))
        raise AssertionError("preflight must not call generate")


class _AutoplayClient(_NoCallClient):
    def generate(self, request, *, seed):
        self.calls.append((deepcopy(request), seed))
        visible = json.loads(request["messages"][1]["content"])
        option_id = visible["options"][0]["option_id"]
        arguments = {"option_id": option_id}
        if visible["tool_schema"]["required"] != ["option_id"]:
            arguments["decision_record"] = {
                "material_basis": "Cheap diagnostic fixture transport.",
                "mandate_fit": "Recorded against the public mandate.",
            }
        self.last_call_metadata = {
            "response_id": "%s-%d" % (self.model_id, len(self.calls)),
            "requested_model": self.model_id,
            "returned_model": self.model_id,
            "provider": self.provider,
            "provider_attribution": "RESPONSE_ECHOED",
            "finish_reason": "stop",
            "usage": {
                "prompt_tokens": 100,
                "completion_tokens": 20,
                "total_tokens": 120,
                "cost": 0.000001,
            },
            "cost_usd": 0.000001,
            "attempt_count": 1,
            "response_status": "ACCEPTED",
        }
        return json.dumps(
            {
                "kind": "act",
                "tool": visible["tool_schema"]["name"],
                "arguments": arguments,
            },
            sort_keys=True,
            separators=(",", ":"),
        )


class _RetryAutoplayClient(_AutoplayClient):
    max_attempts = 3
    retry_base_seconds = 1.0


def _clients(config):
    return tuple(_NoCallClient(row) for row in config["model_roster"])


def _autoplay_clients(config):
    return tuple(_AutoplayClient(row) for row in config["model_roster"])


def _retry_autoplay_clients(config):
    return tuple(_RetryAutoplayClient(row) for row in config["model_roster"])


def test_frozen_transport_repair_attestation_binds_actual_r1_prefix():
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()
    plan = module.preflight_diagnostic(
        clients=_retry_autoplay_clients(config),
        smoke_dir=SMOKE_DIR,
    )

    digest = module._validate_transport_repair_attestation(FULL_R1_DIR, plan)

    assert digest == module.TRANSPORT_REPAIR_ATTESTATION_SHA256
    assert len(digest) == 64


def test_retry_enabled_resume_requires_attestation_before_new_calls(tmp_path):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()
    original_clients = _autoplay_clients(config)
    original_plan = module.preflight_diagnostic(
        clients=original_clients,
        smoke_dir=SMOKE_DIR,
    )
    output_dir = tmp_path / "pre-repair-prefix"
    schedule = original_plan.schedule[:1]
    module._execute_diagnostic_schedule(
        original_plan,
        schedule,
        output_dir=output_dir,
        resume=False,
        max_workers=1,
    )
    retry_clients = _retry_autoplay_clients(config)
    retry_plan = module.preflight_diagnostic(
        clients=retry_clients,
        smoke_dir=SMOKE_DIR,
    )

    with pytest.raises(ValueError, match="transport repair attestation"):
        module._execute_diagnostic_schedule(
            retry_plan,
            schedule,
            output_dir=output_dir,
            resume=True,
            max_workers=1,
        )

    assert all(client.calls == [] for client in retry_clients)


def test_full_diagnostic_config_is_exact_frozen_and_explicitly_ineligible():
    module = _module()

    config, digest = module.load_frozen_diagnostic_config()

    assert digest == "8f9876a03ea760defe9bef13a8b04cdcd99425677b5853e6b92d269061acfd84"
    assert config["run_id"] == "SKIM-P1-CHEAP-OPENROUTER-FULL-20260711-R1"
    assert config["mode"] == "LIVE_ONE_SEED_CHEAP_MODEL_ENGINEERING_DIAGNOSTIC"
    assert config["status"] == "NOT_RUN"
    assert config["eligible_for_empirical_decision"] is False
    assert config["seed"] == 20260711
    assert config["scheduled_requests"] == 2400
    assert config["max_paid_calls"] == 4800
    assert config["cost_cap_usd"] == 1.0
    assert len(config["model_roster"]) == 3
    assert len({row["vendor"] for row in config["model_roster"]}) == 3
    assert config["smoke_authorization"]["smoke_result_sha256"] == (
        "802b91ca8b01d346bd47fac55e4219ccc6f3b4cc26edb45243946c1dca746188"
    )


def test_full_preflight_binds_smoke_artifacts_schedule_and_cost_without_calls(
    tmp_path,
):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()
    clients = _clients(config)
    output_dir = tmp_path / "must-not-exist"

    plan = module.preflight_diagnostic(
        clients=clients,
        smoke_dir=SMOKE_DIR,
    )

    assert plan.status == "LIVE_ONE_SEED_CHEAP_MODEL_ENGINEERING_DIAGNOSTIC"
    assert plan.eligible_for_empirical_decision is False
    assert plan.seed == 20260711
    assert len(plan.schedule) == 2400
    assert all(
        sum(row["model_id"] == client.model_id for row in plan.schedule) == 800
        for client in clients
    )
    assert 0 < plan.preflight_cost_upper_bound_usd < 1.0
    assert plan.cost_cap_usd == 1.0
    assert plan.smoke_result_sha256 == config["smoke_authorization"][
        "smoke_result_sha256"
    ]
    assert all(client.calls == [] for client in clients)
    assert not output_dir.exists()


def test_full_preflight_rejects_tampered_smoke_before_calls_or_output(
    tmp_path,
):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()
    clients = _clients(config)
    copied = tmp_path / "tampered-smoke"
    copied.mkdir()
    payload = json.loads((SMOKE_DIR / "smoke-result.json").read_text())
    payload["eligible_for_empirical_decision"] = True
    (copied / "smoke-result.json").write_text(json.dumps(payload) + "\n")

    with pytest.raises((TypeError, ValueError, RuntimeError), match="smoke|hash"):
        module.preflight_diagnostic(clients=clients, smoke_dir=copied)

    assert all(client.calls == [] for client in clients)
    assert set(copied.iterdir()) == {copied / "smoke-result.json"}


def test_full_preflight_rejects_wrong_client_roster_before_calls():
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()
    clients = list(_clients(config))
    clients[0].model_id = "unfrozen/model"

    with pytest.raises((TypeError, ValueError, RuntimeError), match="client|roster|model"):
        module.preflight_diagnostic(clients=clients, smoke_dir=SMOKE_DIR)

    assert all(client.calls == [] for client in clients)


def test_full_diagnostic_cli_requires_explicit_paid_opt_in_before_key_or_network(
    tmp_path,
):
    script = ROOT / "harness" / "run_openrouter_diagnostic.py"
    completed = subprocess.run(
        [
            sys.executable,
            str(script),
            "--smoke-dir",
            str(SMOKE_DIR),
            "--output-dir",
            str(tmp_path / "never-created"),
        ],
        check=False,
        capture_output=True,
        text=True,
        env={},
    )

    assert completed.returncode != 0
    assert "--execute-paid-live" in completed.stderr
    assert not (tmp_path / "never-created").exists()


def test_diagnostic_checkpoint_resume_skips_completed_calls_and_extends_prefix(
    tmp_path,
):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()
    clients = _autoplay_clients(config)
    plan = module.preflight_diagnostic(clients=clients, smoke_dir=SMOKE_DIR)
    output_dir = tmp_path / "diagnostic-resume"
    first_schedule = plan.schedule[:2]

    first = module._execute_diagnostic_schedule(
        plan,
        first_schedule,
        output_dir=output_dir,
        resume=False,
        max_workers=3,
    )
    calls_after_first = tuple(len(client.calls) for client in clients)
    resumed = module._execute_diagnostic_schedule(
        plan,
        first_schedule,
        output_dir=output_dir,
        resume=True,
        max_workers=3,
    )
    extended = module._execute_diagnostic_schedule(
        plan,
        plan.schedule[:3],
        output_dir=output_dir,
        resume=True,
        max_workers=3,
    )

    assert len(first) == len(resumed) == 2
    assert first == resumed
    assert tuple(len(client.calls) for client in clients) == (
        calls_after_first[0] + 1,
        calls_after_first[1],
        calls_after_first[2],
    )
    assert len(extended) == 3
    assert all(episode["status"] == "VALID_TERMINAL" for episode in extended)
    assert all(episode["mechanical_score"]["status"] == "SCORED" for episode in extended)
    assert len(list((output_dir / "events").glob("*.jsonl"))) == 3
    checkpoint = output_dir / "checkpoints" / "model-0.jsonl"
    assert checkpoint.is_file()
    assert len(checkpoint.read_text().splitlines()) == 3


def test_diagnostic_resume_rejects_checkpoint_tamper_before_new_calls(tmp_path):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()
    clients = _autoplay_clients(config)
    plan = module.preflight_diagnostic(clients=clients, smoke_dir=SMOKE_DIR)
    output_dir = tmp_path / "tampered-resume"
    module._execute_diagnostic_schedule(
        plan,
        plan.schedule[:1],
        output_dir=output_dir,
        resume=False,
        max_workers=3,
    )
    checkpoint = output_dir / "checkpoints" / "model-0.jsonl"
    checkpoint.write_bytes(checkpoint.read_bytes() + b'{"forged":true}\n')
    calls_before = tuple(len(client.calls) for client in clients)

    with pytest.raises((TypeError, ValueError, RuntimeError), match="checkpoint|chain|canonical"):
        module._execute_diagnostic_schedule(
            plan,
            plan.schedule[:2],
            output_dir=output_dir,
            resume=True,
            max_workers=3,
        )

    assert tuple(len(client.calls) for client in clients) == calls_before


def test_charged_rejected_call_is_checkpointed_and_never_duplicated_on_resume(
    tmp_path,
):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()

    class ChargedReject(_AutoplayClient):
        def generate(self, request, *, seed):
            self.calls.append((deepcopy(request), seed))
            self.last_call_metadata = {
                "response_id": "charged-reject-1",
                "requested_model": self.model_id,
                "returned_model": self.model_id,
                "provider": self.provider,
                "provider_attribution": "RESPONSE_ECHOED",
                "finish_reason": "length",
                "usage": {"cost": 0.20},
                "cost_usd": 0.20,
                "attempt_count": 1,
                "response_status": "REJECTED_RESPONSE",
            }
            raise RuntimeError("charged response rejected")

    clients = list(_autoplay_clients(config))
    clients[0] = ChargedReject(config["model_roster"][0])
    plan = module.preflight_diagnostic(clients=clients, smoke_dir=SMOKE_DIR)
    output_dir = tmp_path / "charged-reject"
    schedule = plan.schedule[:1]

    with pytest.raises(RuntimeError, match="cost cap|charged|rejected"):
        module._execute_diagnostic_schedule(
            plan,
            schedule,
            output_dir=output_dir,
            resume=False,
            max_workers=3,
        )

    checkpoint = output_dir / "checkpoints" / "model-0.jsonl"
    assert checkpoint.is_file()
    row = json.loads(checkpoint.read_text().strip())
    assert row["episode"]["status"] == "PARKED_MODEL_CALL_ABORT"
    assert row["episode"]["paid_calls"] == 2
    assert row["episode"]["cost_usd"] == pytest.approx(0.20)
    assert len(clients[0].calls) == 1
    failure = json.loads((output_dir / "diagnostic-failure.json").read_text())
    assert failure["status"] == "CHEAP_DIAGNOSTIC_ABORTED"
    assert failure["paid_calls_accounted"] >= 1
    assert failure["total_cost_usd_accounted"] >= 0.20
    serialized_failure = json.dumps(failure).lower()
    assert "private_gold" not in serialized_failure
    assert "raw_response" not in serialized_failure
    assert "test-key" not in serialized_failure

    with pytest.raises((ValueError, RuntimeError), match="spend|bound|cost"):
        module._execute_diagnostic_schedule(
            plan,
            schedule,
            output_dir=output_dir,
            resume=True,
            max_workers=3,
        )
    assert len(clients[0].calls) == 1


def test_unknown_cost_repair_failure_reserves_full_episode_and_never_retries(
    tmp_path,
):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()

    class SyntaxThenUnknownCost(_AutoplayClient):
        def generate(self, request, *, seed):
            self.calls.append((deepcopy(request), seed))
            if len(self.calls) == 1:
                self.last_call_metadata = {
                    "response_id": "syntax-first",
                    "requested_model": self.model_id,
                    "returned_model": self.model_id,
                    "provider": self.provider,
                    "provider_attribution": "RESPONSE_ECHOED",
                    "finish_reason": "stop",
                    "usage": {"cost": 0.000001},
                    "cost_usd": 0.000001,
                    "attempt_count": 1,
                    "response_status": "ACCEPTED",
                }
                return "not-json"
            self.last_call_metadata = None
            raise RuntimeError("repair failed without cost metadata")

    clients = list(_autoplay_clients(config))
    clients[0] = SyntaxThenUnknownCost(config["model_roster"][0])
    plan = module.preflight_diagnostic(clients=clients, smoke_dir=SMOKE_DIR)
    output_dir = tmp_path / "unknown-repair-cost"
    schedule = plan.schedule[:1]

    with pytest.raises(RuntimeError, match="repair failed"):
        module._execute_diagnostic_schedule(
            plan,
            schedule,
            output_dir=output_dir,
            resume=False,
            max_workers=3,
        )

    row = json.loads(
        (output_dir / "checkpoints" / "model-0.jsonl").read_text().strip()
    )
    episode = row["episode"]
    assert len(clients[0].calls) == 2
    assert episode["paid_calls"] == 2
    assert episode["cost_usd"] > 0.000001
    assert episode["cost_accounting_status"] == (
        "CONSERVATIVE_MAX_REPORTED_OR_FULL_EPISODE_UPPER_BOUND"
    )

    resumed = module._execute_diagnostic_schedule(
        plan,
        schedule,
        output_dir=output_dir,
        resume=True,
        max_workers=3,
    )
    assert len(clients[0].calls) == 2
    assert resumed[0]["status"] == "PARKED_MODEL_CALL_ABORT"


def test_first_failed_worker_stops_other_model_groups_promptly(tmp_path):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()

    class SlowAutoplay(_AutoplayClient):
        def generate(self, request, *, seed):
            time.sleep(0.01)
            return super().generate(request, seed=seed)

    class ImmediateReject(_AutoplayClient):
        def generate(self, request, *, seed):
            self.calls.append((deepcopy(request), seed))
            self.last_call_metadata = {
                "response_id": "immediate-reject",
                "requested_model": self.model_id,
                "returned_model": self.model_id,
                "provider": self.provider,
                "provider_attribution": "RESPONSE_ECHOED",
                "finish_reason": "length",
                "usage": {"cost": 0.000001},
                "cost_usd": 0.000001,
                "attempt_count": 1,
                "response_status": "REJECTED_RESPONSE",
            }
            raise RuntimeError("immediate worker abort")

    clients = [SlowAutoplay(row) for row in config["model_roster"]]
    clients[2] = ImmediateReject(config["model_roster"][2])
    plan = module.preflight_diagnostic(clients=clients, smoke_dir=SMOKE_DIR)
    selected = tuple(
        row
        for model_id in [entry["model_id"] for entry in config["model_roster"]]
        for row in [
            candidate
            for candidate in plan.schedule
            if candidate["model_id"] == model_id
        ][:20]
    )

    with pytest.raises(RuntimeError, match="immediate worker abort"):
        module._execute_diagnostic_schedule(
            plan,
            selected,
            output_dir=tmp_path / "prompt-stop",
            resume=False,
            max_workers=3,
        )

    assert len(clients[2].calls) == 1
    assert len(clients[0].calls) < 20
    assert len(clients[1].calls) < 20


def test_public_diagnostic_refuses_incomplete_execution_result(monkeypatch, tmp_path):
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()
    clients = _autoplay_clients(config)
    plan = module.preflight_diagnostic(clients=clients, smoke_dir=SMOKE_DIR)

    def incomplete(*args, **kwargs):
        Path(kwargs["output_dir"]).mkdir(parents=True)
        return tuple()

    monkeypatch.setattr(module, "_execute_diagnostic_schedule", incomplete)
    with pytest.raises(RuntimeError, match="complete|scheduled|episode"):
        module.run_diagnostic(
            plan,
            output_dir=tmp_path / "incomplete-full",
            resume=False,
            max_workers=3,
        )
    assert not (tmp_path / "incomplete-full" / "diagnostic-result.json").exists()


def test_live_catalog_requires_exact_healthy_endpoint_prices_and_parameters():
    module = _module()
    config, _digest = module.load_frozen_diagnostic_config()

    class Response:
        status = 200

        def __init__(self, payload):
            self.payload = payload

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self):
            return json.dumps(self.payload).encode()

    payloads = {}
    for row in config["model_roster"]:
        payloads[row["model_id"]] = {
            "data": {
                "id": row["model_id"],
                "endpoints": [
                    {
                        "name": row["endpoint_name"],
                        "provider_name": row["provider"],
                        "status": 0,
                        "pricing": {
                            "prompt": row["prompt_price_per_token_usd"],
                            "completion": row["completion_price_per_token_usd"],
                        },
                        "supported_parameters": [
                            "max_tokens",
                            "temperature",
                            "seed",
                            "response_format",
                        ],
                    }
                ],
            }
        }

    def opener(request, timeout):
        model_id = request.full_url.split("/models/", 1)[1].rsplit(
            "/endpoints", 1
        )[0]
        assert request.get_header("Authorization") == "Bearer test-key"
        assert timeout == 30
        return Response(payloads[model_id])

    result = module.verify_live_catalog(
        config,
        api_key="test-key",
        opener=opener,
    )
    assert result == {
        "verified": True,
        "model_ids": [row["model_id"] for row in config["model_roster"]],
        "providers": [row["provider"] for row in config["model_roster"]],
    }
    assert "test-key" not in json.dumps(result)

    payloads[config["model_roster"][2]["model_id"]]["data"]["endpoints"][0][
        "status"
    ] = -2
    with pytest.raises((TypeError, ValueError, RuntimeError), match="catalog|endpoint|status"):
        module.verify_live_catalog(config, api_key="test-key", opener=opener)


def test_paid_cli_verifies_catalog_before_clients_and_runs_exact_plan(tmp_path):
    module = _module()
    events = []

    def catalog_verifier(config, *, api_key):
        events.append(("catalog", api_key))
        return {
            "verified": True,
            "model_ids": [row["model_id"] for row in config["model_roster"]],
            "providers": [row["provider"] for row in config["model_roster"]],
        }

    def client_factory(model_id, **kwargs):
        events.append(("client", model_id))
        row = {
            "model_id": model_id,
            "family": kwargs["family"],
            "vendor": kwargs["vendor"],
            "provider": kwargs["provider"],
        }
        return _AutoplayClient(row)

    def diagnostic_runner(plan, *, output_dir, resume, max_workers):
        events.append(("run", len(plan.schedule), resume, max_workers))
        assert output_dir == tmp_path / "paid"
        return {
            "status": module.RUN_STATUS + "_COMPLETE",
            "scheduled_requests": 2400,
            "paid_calls": 2400,
            "total_cost_usd": 0.03,
            "eligible_for_empirical_decision": False,
        }

    code = module.cli(
        [
            "--execute-paid-live",
            "--smoke-dir",
            str(SMOKE_DIR),
            "--output-dir",
            str(tmp_path / "paid"),
        ],
        environ={"OPENROUTER_API_KEY": "test-key"},
        client_factory=client_factory,
        catalog_verifier=catalog_verifier,
        diagnostic_runner=diagnostic_runner,
    )

    assert code == 0
    assert events[0] == ("catalog", "test-key")
    assert [event[0] for event in events[1:4]] == ["client", "client", "client"]
    assert events[4] == ("run", 2400, False, 3)
