import json
from dataclasses import replace
from types import MappingProxyType

import pytest


class FakeClient:
    def __init__(self, plan, route, ledger, behavior, calls):
        self.plan = plan
        self.route = route
        self.ledger = ledger
        self.behavior = behavior
        self.calls = calls
        self.last_call_metadata = None
        self.by_paid_id = {}
        for row in plan.schedule:
            self.by_paid_id[row.initial_call_id] = row
            self.by_paid_id[row.repair_call_id] = row

    def _success(self, row, request, repair):
        public = self.plan.bundle.public_by_id[row.source_record_id]
        private = self.plan.bundle.private_by_id[row.source_record_id]
        if repair:
            if row.role == "evaluated":
                if public["record_type"] in {
                    "composition",
                    "no_incentive_twin",
                    "monitoring_twin",
                }:
                    return {"composition": public["source_atoms"][0]["text"]}
                if public["record_type"] == "recognition":
                    return {"label": private["gold_label"]}
                return {
                    "label": private["gold_label"],
                    "localized_moves": (
                        []
                        if private["gold_label"] == "faithful"
                        else private["spin_moves"]
                    ),
                }
            payload = json.loads(request["messages"][1]["content"])
            schema = payload["response_schema"]
            if "probe_answers" in schema["properties"]:
                return {
                    "probe_answers": {
                        probe["probe_id"]: 0.0 for probe in public["probes"]
                    }
                }
            composition = payload["rejected_output"]
            claim = public["source_atoms"][0]
            return {
                "extraction_complete": True,
                "claims": [
                    {
                        "claim_id": "claim-1",
                        "claim_text": claim["text"],
                        "support_status": "supported",
                        "support_atom_ids": [claim["atom_id"]],
                    }
                ],
            }
        if row.role == "evaluated":
            if public["record_type"] in {
                "composition",
                "no_incentive_twin",
                "monitoring_twin",
            }:
                return {"composition": public["source_atoms"][0]["text"]}
            if public["record_type"] == "recognition":
                return {"label": private["gold_label"]}
            return {
                "label": private["gold_label"],
                "localized_moves": (
                    []
                    if private["gold_label"] == "faithful"
                    else private["spin_moves"]
                ),
            }
        payload = json.loads(request["messages"][1]["content"])
        if row.role == "reader":
            return {
                "probe_answers": {
                    probe["probe_id"]: 0.0 for probe in payload["probes"]
                }
            }
        composition = payload["composition"]
        matching = [
            atom for atom in payload["source_atoms"] if atom["text"] in composition
        ]
        claim = matching[0]
        return {
            "extraction_complete": True,
            "claims": [
                {
                    "claim_id": "claim-1",
                    "claim_text": claim["text"],
                    "support_status": "supported",
                    "support_atom_ids": [claim["atom_id"]],
                }
            ],
        }

    def generate(self, request, *, seed, call_id):
        from TENCOMMANDMENTS.harness.openrouter import (
            OpenRouterResponseError,
            OpenRouterTransportError,
        )

        row = self.by_paid_id[call_id]
        repair = call_id == row.repair_call_id
        self.calls.append(call_id)
        self.ledger.authorize_call(call_id)
        action = self.behavior.get(call_id, "success")
        if action == "429":
            self.ledger.release_call(call_id)
            raise OpenRouterTransportError(
                "rate limited", status_code=429, attempt_count=3
            )
        if action == "ambiguous":
            raise OpenRouterTransportError(
                "ambiguous", status_code=None, attempt_count=1
            )
        if action == "malformed_paid_envelope":
            raise OpenRouterResponseError("paid response envelope was malformed")
        spend = self.ledger.record_paid_call(call_id, "0.000001")
        self.last_call_metadata = {
            "call_id": call_id,
            "requested_model": self.route.model_id,
            "provider": self.route.provider,
            "requested_seed": seed,
            "attempt_count": 1,
            "usage": {"cost": 0.000001},
            "cost_usd": "0.000001",
            "cumulative_cost_usd": spend.cumulative_cost_usd,
            "response_status": "ACCEPTED",
        }
        if action == "paid_rejected":
            self.last_call_metadata["response_status"] = "REJECTED_RESPONSE"
            raise OpenRouterResponseError("paid response rejected")
        if action == "invalid_json":
            return "not-json"
        return json.dumps(self._success(row, request, repair))


def factory(plan, behavior, calls):
    def build(route, _route_row, ledger, _config):
        return FakeClient(plan, route, ledger, behavior, calls)

    return build


def catalog_verifier(routes, **_kwargs):
    from TENCOMMANDMENTS.harness.openrouter import CatalogVerification

    return CatalogVerification(tuple(routes))


def test_smoke_executes_all_51_calls_with_one_repair_and_writes_sanitized_custody(
    tmp_path,
):
    from harness import palter_openrouter as transport
    from harness import run_openrouter_smoke as smoke
    from TENCOMMANDMENTS.harness.openrouter import load_checkpoint_stream

    plan = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
    behavior = {plan.schedule[0].initial_call_id: "invalid_json"}
    calls = []
    output = tmp_path / "smoke"
    result = smoke.run_smoke(
        output,
        api_key="fake-secret",
        catalog_verifier=catalog_verifier,
        client_factory=factory(plan, behavior, calls),
    )

    assert result["status"] == "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE"
    assert result["scheduled_semantic_calls"] == 51
    assert result["accounted_semantic_calls"] == 51
    assert result["paid_calls"] == 52
    assert result["parked_semantic_calls"] == 0
    assert result["bt_status"] == "NOT_RUN"
    assert result["eligible_for_empirical_decision"] is False
    assert len(calls) == 52
    snapshot = load_checkpoint_stream(
        output / "calls.jsonl", plan.config["run_id"]
    )
    assert len(snapshot.records) == 52
    serialized = json.dumps(result, sort_keys=True)
    assert "raw_response" not in serialized
    assert "probe_gold" not in serialized
    assert "spin_moves" not in serialized
    assert (output / "smoke-result.json").is_file()
    with pytest.raises(ValueError, match="fresh|exists"):
        smoke.run_smoke(
            output,
            api_key="fake-secret",
            catalog_verifier=catalog_verifier,
            client_factory=factory(plan, {}, []),
        )


def test_call_checkpoint_resume_never_replays_ambiguous_paid_rejected_or_429_calls(
    tmp_path,
):
    from harness import palter_openrouter as transport
    from TENCOMMANDMENTS.harness.openrouter import load_checkpoint_stream

    plan = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
    behavior = {
        plan.schedule[0].initial_call_id: "ambiguous",
        plan.schedule[1].initial_call_id: "429",
        plan.schedule[2].initial_call_id: "paid_rejected",
    }
    calls = []
    output = tmp_path / "resume"
    first = transport.execute_plan(
        plan,
        output,
        api_key="fake-secret",
        catalog_verification={"verified": True, "routes": []},
        client_factory=factory(plan, behavior, calls),
        resume=False,
    )
    assert first["accounted_semantic_calls"] == 51
    statuses = {
        row["status"]
        for row in load_checkpoint_stream(
            output / "calls.jsonl", plan.config["run_id"]
        ).payloads
    }
    assert "PARKED_AMBIGUOUS_CONSERVATIVE" in statuses
    assert "PARKED_UNCHARGED_429" in statuses
    assert "PARKED_PAID_REJECTED" in statuses
    assert "PARKED_DEPENDENCY" in statuses

    resumed_calls = []
    second = transport.execute_plan(
        plan,
        output,
        api_key="fake-secret",
        catalog_verification={"verified": True, "routes": []},
        client_factory=factory(plan, {}, resumed_calls),
        resume=True,
    )
    assert second["accounted_semantic_calls"] == 51
    assert resumed_calls == []
    assert second["cost_usd"] == first["cost_usd"]


def test_forged_terminal_checkpoint_without_paid_or_parsed_custody_fails_closed(
    tmp_path,
):
    from harness import palter_openrouter as transport
    from TENCOMMANDMENTS.harness.openrouter import append_checkpoint

    plan = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
    output = tmp_path / "forged"
    output.mkdir()
    call = plan.schedule[0]
    forged = transport._checkpoint_payload(
        plan,
        call,
        call_id=call.initial_call_id,
        attempt_kind="initial",
        status="ACCEPTED",
        parsed_response=None,
        rejected_content=None,
        call_metadata=None,
        spend_record=None,
    )
    append_checkpoint(output / "calls.jsonl", plan.config["run_id"], forged)

    with pytest.raises(ValueError, match="checkpoint.*custody|checkpoint.*lifecycle"):
        transport.execute_plan(
            plan,
            output,
            api_key="fake-secret",
            catalog_verification={"verified": True, "routes": []},
            client_factory=factory(plan, {}, []),
            resume=True,
        )


def test_full_preflight_succeeds_offline_but_live_execution_fails_on_bt_not_run(
    tmp_path,
    capsys,
):
    from harness import run_openrouter

    summary = run_openrouter.preflight("full")
    assert summary["semantic_calls"] == 3720
    assert summary["paid_call_ceiling"] == 7440
    assert summary["cost_cap_usd"] == "2"
    assert summary["bt_status"] == "NOT_RUN"
    assert summary["network_calls"] == 0

    assert run_openrouter.main(["--mode", "full", "--preflight-only"]) == 0
    printed = json.loads(capsys.readouterr().out)
    assert printed == summary

    with pytest.raises(ValueError, match="BT.*NOT_RUN"):
        run_openrouter.run(
            "full",
            tmp_path / "must-not-run",
            api_key="fake-secret",
        )
    assert not (tmp_path / "must-not-run").exists()


def test_malformed_paid_envelope_is_conservatively_accounted_as_ambiguous(tmp_path):
    from harness import palter_openrouter as transport
    from TENCOMMANDMENTS.harness.openrouter import load_checkpoint_stream

    plan = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
    first = plan.schedule[0]
    output = tmp_path / "malformed"
    result = transport.execute_plan(
        plan,
        output,
        api_key="fake-secret",
        catalog_verification={"verified": True, "routes": []},
        client_factory=factory(
            plan,
            {first.initial_call_id: "malformed_paid_envelope"},
            [],
        ),
        resume=False,
    )
    payload = load_checkpoint_stream(
        output / "calls.jsonl", plan.config["run_id"]
    ).payloads[0]
    maximum = next(
        row.max_cost_usd
        for row in plan.preflight.calls
        if row.call_id == first.initial_call_id
    )
    assert payload["status"] == "PARKED_AMBIGUOUS_CONSERVATIVE"
    assert transport.Decimal(payload["spend_record"]["cost_usd"]) == maximum
    assert result["parked_semantic_calls"] >= 1


def test_resume_after_durable_pending_repair_runs_repair_not_initial(
    tmp_path,
    monkeypatch,
):
    from harness import palter_openrouter as transport
    from TENCOMMANDMENTS.harness.openrouter import load_checkpoint_stream

    plan = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
    first = plan.schedule[0]
    output = tmp_path / "repair-resume"
    original_append = transport._append_payload
    crashed = {"done": False}

    def append_then_crash(*args, **kwargs):
        payload = args[2]
        head = original_append(*args, **kwargs)
        if (
            payload["status"] == transport._PENDING_REPAIR_STATUS
            and not crashed["done"]
        ):
            crashed["done"] = True
            raise RuntimeError("simulated process crash after durable checkpoint")
        return head

    monkeypatch.setattr(transport, "_append_payload", append_then_crash)
    with pytest.raises(RuntimeError, match="simulated process crash"):
        transport.execute_plan(
            plan,
            output,
            api_key="fake-secret",
            catalog_verification={"verified": True, "routes": []},
            client_factory=factory(
                plan,
                {first.initial_call_id: "invalid_json"},
                [],
            ),
            resume=False,
        )
    snapshot = load_checkpoint_stream(
        output / "calls.jsonl", plan.config["run_id"]
    )
    assert len(snapshot.records) == 1
    assert snapshot.payloads[0]["status"] == transport._PENDING_REPAIR_STATUS

    monkeypatch.setattr(transport, "_append_payload", original_append)
    resumed_calls = []
    result = transport.execute_plan(
        plan,
        output,
        api_key="fake-secret",
        catalog_verification={"verified": True, "routes": []},
        client_factory=factory(plan, {}, resumed_calls),
        resume=True,
    )
    assert resumed_calls[0] == first.repair_call_id
    assert first.initial_call_id not in resumed_calls
    assert result["accounted_semantic_calls"] == 51


def test_future_bt_authorized_full_entry_uses_the_full_plan(tmp_path, monkeypatch):
    from harness import palter_openrouter as transport
    from harness import run_openrouter

    full = transport.preflight_config(transport.FULL_CONFIG_PATH)
    authorized_config = dict(full.config)
    authorized_config["bt_status"] = "PASS"
    authorized = replace(full, config=MappingProxyType(authorized_config))
    monkeypatch.setattr(
        run_openrouter.transport,
        "preflight_config",
        lambda _path: authorized,
    )
    captured = {}

    def fake_run_plan(plan, output_dir, **kwargs):
        captured["plan"] = plan
        captured["output_dir"] = output_dir
        captured["kwargs"] = kwargs
        return {"status": "FULL_FAKE"}

    monkeypatch.setattr(
        run_openrouter.run_openrouter_smoke,
        "run_plan",
        fake_run_plan,
        raising=False,
    )
    monkeypatch.setattr(
        run_openrouter.run_openrouter_smoke,
        "run_smoke",
        lambda *args, **kwargs: {"status": "WRONG_SMOKE_ENTRY"},
    )
    result = run_openrouter.run(
        "full",
        tmp_path / "full",
        api_key="fake-secret",
    )
    assert result == {"status": "FULL_FAKE"}
    assert captured["plan"].config["mode"] == "CHEAP_OPENROUTER_FULL_DIAGNOSTIC"
    assert captured["kwargs"]["result_filename"] == "full-result.json"
