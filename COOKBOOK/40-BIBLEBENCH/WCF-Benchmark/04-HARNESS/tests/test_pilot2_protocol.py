from __future__ import annotations

import json
import os
import sys

import pytest


HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

import pilot2_live as live  # noqa: E402
import pilot2_judge as pilot2_judge  # noqa: E402
import pilot2_oauth_canary as oauth_canary  # noqa: E402
import pilot2_preflight as preflight  # noqa: E402
import pilot2_report as report  # noqa: E402
import pilot2_run as run  # noqa: E402
from wcfbench import load_items  # noqa: E402


def _catalog_and_endpoints():
    catalog = {}
    endpoints = {}
    for spec in preflight.SUT_SPECS:
        reasoning = {
            "mandatory": False,
            "supported_efforts": ["high", "xhigh"],
        }
        catalog[spec.slug] = {
            "id": spec.slug,
            "canonical_slug": spec.slug + "-canonical",
            "context_length": 131072,
            "top_provider": {
                "context_length": 131072,
                "max_completion_tokens": 16384,
            },
            "architecture": {
                "input_modalities": ["text"], "output_modalities": ["text"]},
            "supported_parameters": [
                "temperature", "max_tokens", "reasoning"],
            "reasoning": reasoning,
        }
        endpoints[spec.slug] = [{
            "provider_name": spec.provider,
            "data_collection": "deny",
            "supported_parameters": [
                "temperature", "max_tokens", "reasoning"],
            "pricing": {
                "prompt": str(spec.prompt_price_per_token),
                "completion": str(spec.completion_price_per_token),
            },
            "context_length": 131072,
            "max_completion_tokens": 16384,
        }]
    return catalog, endpoints


def _manifest():
    catalog, endpoints = _catalog_and_endpoints()
    return preflight.build_manifest(
        catalog, endpoints, catalog_retrieved_at="2026-07-15T00:00:00Z")


def _ok_response(spec, *, content="final answer", reasoning_tokens=5, cost=0.001):
    return {
        "provider": spec.provider,
        "choices": [{
            "finish_reason": "stop",
            "message": {"content": content, "reasoning": "private chain"},
        }],
        "usage": {
            "prompt_tokens": 100,
            "completion_tokens": 20,
            "cost": cost,
            "completion_tokens_details": {
                "reasoning_tokens": reasoning_tokens,
            },
        },
    }


def test_exact_five_model_reasoning_contract_and_geometry():
    assert preflight.VALIDITY_LABEL == (
        "EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED "
        "OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED "
        "CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE")
    assert tuple(spec.slug for spec in preflight.SUT_SPECS) == (
        "minimax/minimax-m3", "z-ai/glm-5.2",
        "deepseek/deepseek-v4-pro", "qwen/qwen3.7-max",
        "google/gemma-4-31b-it")
    assert tuple(spec.provider for spec in preflight.SUT_SPECS) == (
        "MiniMax", "StreamLake", "DeepSeek", "Alibaba", "WandB")
    assert all(spec.reasoning in (
        {"enabled": True}, {"effort": "high"})
        for spec in preflight.SUT_SPECS)
    geometry = preflight.build_geometry(
        load_items(str(preflight.BANK_DIR)))
    assert geometry["sut_cells"] == 1150
    assert geometry["scorable_sut_cells"] == 1130
    assert geometry["diagnostic_sut_cells"] == 20
    assert geometry["scalar_eligible_total"] == 1110
    assert geometry["contested_total"] == 20
    assert geometry["logical_judge_decisions_total"] == 1740
    assert geometry["expected_judge_tasks"] == 220
    assert geometry["conservative_large_response_tasks"] == 590
    assert geometry["scalar_sufficiency"] == {"minimum": 200, "denominator": 222}


def test_manifest_pins_exact_provider_reasoning_price_and_8192_reservation():
    manifest = _manifest()
    assert manifest["status"] == "ZERO-PAID-PREFLIGHT-INPUT"
    assert manifest["auth_balance"]["status"] == "NOT_CHECKED"
    assert manifest["authorization_gate"]["paid_inference"] is False
    assert manifest["geometry"]["sut_attempts_max_per_model"] == 252
    assert manifest["geometry"]["sut_retries_reserved_per_model"] == 22
    assert manifest["judge"]["max_batch_size"] == 8
    assert manifest["judge"]["max_serialized_batch_bytes"] == 800000
    assert manifest["judge"]["max_serialized_record_bytes"] == 262144
    for row, spec in zip(manifest["models"], preflight.SUT_SPECS):
        assert row["slug"] == spec.slug
        assert row["request_parameters"] == {
            "temperature": 0, "max_tokens": 8192,
            "reasoning": spec.reasoning,
        }
        assert row["provider_policy"] == {
            "order": [spec.provider],
            "allow_fallbacks": False,
            "require_parameters": True,
            "data_collection": "deny",
            "max_price": {
                "prompt": spec.prompt_price_per_token * 1_000_000,
                "completion": spec.completion_price_per_token * 1_000_000,
            },
        }
        assert row["maximum_attempt_cost_usd"] == pytest.approx(
            2221 * spec.prompt_price_per_token
            + 8192 * spec.completion_price_per_token)
    assert manifest["planning_cost"]["proposed_cap_usd"] == 27.03


def test_manifest_rejects_wrong_provider_or_reasoning_capability():
    catalog, endpoints = _catalog_and_endpoints()
    endpoints[preflight.SUT_SPECS[0].slug][0]["provider_name"] = "Novita"
    with pytest.raises(preflight.PreflightError, match="pinned provider"):
        preflight.build_manifest(
            catalog, endpoints, catalog_retrieved_at="2026-07-15T00:00:00Z")
    catalog, endpoints = _catalog_and_endpoints()
    catalog[preflight.SUT_SPECS[1].slug]["reasoning"]["supported_efforts"] = ["xhigh"]
    with pytest.raises(preflight.PreflightError, match="high effort"):
        preflight.build_manifest(
            catalog, endpoints, catalog_retrieved_at="2026-07-15T00:00:00Z")


def test_request_is_pinned_and_contains_no_expansive_features():
    manifest = _manifest()
    for spec in preflight.SUT_SPECS:
        payload = run.build_sut_request(
            manifest, spec.slug, [{"role": "user", "content": "blind"}])
        assert payload == {
            "model": spec.slug,
            "messages": [{"role": "user", "content": "blind"}],
            "temperature": 0,
            "max_tokens": 8192,
            "reasoning": spec.reasoning,
            "provider": next(row["provider_policy"] for row in manifest["models"]
                             if row["slug"] == spec.slug),
        }


def test_provider_canary_retries_transport_once_but_never_semantic():
    spec = preflight.SUT_SPECS[0]
    calls = []

    def transport(_payload):
        calls.append(None)
        if len(calls) == 1:
            raise run.TransportFailure("timeout")
        return _ok_response(spec)

    outcome = run.run_provider_canary(spec, transport)
    assert outcome["status"] == "PASS" and len(calls) == 2
    calls.clear()
    with pytest.raises(run.TerminalStop, match="positive reasoning"):
        run.run_provider_canary(
            spec, lambda _payload: calls.append(None) or
            _ok_response(spec, reasoning_tokens=0))
    assert len(calls) == 1


@pytest.mark.parametrize("mutation, message", [
    (lambda response: response.update(provider="Novita"), "provider mismatch"),
    (lambda response: response["choices"][0]["message"].update(content=""),
     "nonempty final"),
    (lambda response: response["choices"][0].update(finish_reason="length"),
     "finish_reason"),
    (lambda response: response["usage"].pop("cost"), "cost"),
    (lambda response: response.update(ignored_parameters=["reasoning"]), "ignored"),
])
def test_provider_response_semantic_gates(mutation, message):
    spec = preflight.SUT_SPECS[0]
    response = _ok_response(spec)
    mutation(response)
    with pytest.raises(run.TerminalStop, match=message):
        run.validate_provider_response(spec, response)


def test_first_real_cells_are_sequential_before_three_remaining_shards():
    events = []
    result = run.execute_registered_sequence(
        item_ids=["A", "B", "C"],
        run_cell=lambda sut, item: events.append((sut, item)) or {"status": "response"},
        suts=tuple(spec.slug for spec in preflight.SUT_SPECS),
    )
    assert events[:5] == [(spec.slug, "A") for spec in preflight.SUT_SPECS]
    assert result["first_cells_validated"] == 5
    assert len(result["shards"]) == 3
    assert sorted(sut for shard in result["shards"] for sut in shard) == sorted(
        spec.slug for spec in preflight.SUT_SPECS)
    for spec in preflight.SUT_SPECS:
        assert events.count((spec.slug, "A")) == 1


def _judge_row(record_id, response, *, sut="sut-a", route="open"):
    return {
        "record_id": record_id, "sut": sut, "route": route,
        "payload": {"criterion_id": "KP1", "response": response},
        "private_reasoning": "must not pass to judge",
    }


def test_dynamic_batches_obey_identity_count_and_byte_envelopes():
    rows = [_judge_row(f"r{i}", "x" * 90000) for i in range(10)]
    batches, missing = run.build_dynamic_judge_batches(rows)
    assert not missing
    assert [len(batch) for batch in batches] == [8, 2]
    assert all(len(run.serialize_judge_batch(batch).encode()) <= 800000
               for batch in batches)
    assert all(len({row["record_id"] for row in batch}) == len(batch)
               for batch in batches)
    with pytest.raises(run.TerminalStop, match="mix"):
        run.build_dynamic_judge_batches([
            _judge_row("a", "ok"), _judge_row("b", "ok", route="episode")])


def test_oversized_record_is_preserved_and_missing_never_truncated_or_zero():
    oversized = _judge_row("large", "z" * 262145)
    batches, missing = run.build_dynamic_judge_batches([oversized])
    assert batches == []
    assert missing == [{
        "record_id": "large", "status": "missing",
        "score": None, "reason": "judge_record_byte_ceiling_exceeded",
        "response": "z" * 262145,
    }]


def test_judge_projection_passes_final_answer_only():
    record = run.project_final_answer_to_judge(
        sut="sut-a", route="open", item_id="ITEM", criterion_id="KP1",
        persisted_response={"final_answer": "visible", "reasoning": "private"})
    serialized = json.dumps(record)
    assert record["payload"]["response"] == "visible"
    assert "private" not in serialized and "reasoning" not in serialized


def test_pilot2_judge_reuses_isolated_sol_medium_adapter_with_larger_byte_limits():
    judge = pilot2_judge.Pilot2CodexOAuthJudge(persist=lambda _row: None)
    record = _judge_row("large-ok", "x" * 200000)
    judge._validate_input([record])
    command = judge._command(
        cwd="/empty", schema_path="/control/schema.json",
        output_path="/control/output.json", records=[record])
    assert command[command.index("--model") + 1] == "gpt-5.6-sol"
    assert 'model_reasoning_effort="medium"' in command
    assert command[command.index("--sandbox") + 1] == "read-only"
    assert 'web_search="disabled"' in command
    assert "features.multi_agent=false" in command
    too_large = _judge_row("too-large", "x" * 262145)
    with pytest.raises(pilot2_judge.JudgeAdapterError, match="byte envelope"):
        judge._validate_input([too_large])


def test_oauth_canary_fixture_is_exact_16_and_has_near_ceiling_record():
    records = oauth_canary.build_fixture_records()
    assert len(records) == 16
    assert {route: sum(row["route"] == route for row in records)
            for route in ("open", "contested", "episode")} == {
                "open": 8, "contested": 4, "episode": 4}
    assert len({row["record_id"] for row in records}) == 16
    assert max(len(run.serialize_judge_record(row)) for row in records) >= 250000
    assert all("response" in row["payload"] for row in records)


def test_immutable_custody_budget_and_missing_checkpoint(tmp_path):
    manifest = _manifest()
    manifest["authorization_gate"]["paid_inference"] = True
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest))
    state = live.prepare_run(manifest_path, tmp_path / "run", cap_usd=0.01)
    state.reserve("cell", 0.008)
    with pytest.raises(live.CustodyStop, match="cap"):
        state.reserve("other", 0.003)
    state.settle("cell", 0.004)
    state.checkpoint_missing("sut::item", "transport_exhausted", attempts=3)
    row = json.loads((state.run_dir / live.CHECKPOINT_FILE).read_text().splitlines()[-1])
    assert row["score"] is None and row["missing"] is True
    with pytest.raises(live.CustodyStop, match="already exists"):
        live.prepare_run(manifest_path, state.run_dir, cap_usd=0.01)


def test_report_payload_is_roster_ordered_non_ranked_and_refuses_empty_data():
    with pytest.raises(report.ReportError, match="empirical"):
        report.build_supplement_payload(_manifest(), [])
    rows = [{
        "sut": spec.slug, "numeric_scores": 200, "scalar_mean": index / 10,
        "matter": None, "manner": None, "end": None, "errors": 22,
    } for index, spec in enumerate(reversed(preflight.SUT_SPECS))]
    payload = report.build_supplement_payload(_manifest(), rows)
    assert [row["sut"] for row in payload["per_sut"]] == [
        spec.slug for spec in preflight.SUT_SPECS]
    assert payload["claims"] == {
        "ranking": False, "reasoning_effect": False, "release": False,
        "universal_score": False, "paper_replacement": False,
    }
    assert all(row["coverage_status"] == "SUFFICIENT_DESCRIPTIVE"
               for row in payload["per_sut"])


def test_fixture_only_end_to_end_protocol_structure():
    manifest = _manifest()
    spec = preflight.SUT_SPECS[0]
    request = run.build_sut_request(
        manifest, spec.slug, [{"role": "user", "content": "blind"}])
    final = run.validate_provider_response(spec, _ok_response(spec))
    judge_record = run.project_final_answer_to_judge(
        sut=spec.slug, route="open", item_id="FIXTURE",
        criterion_id="KP1", persisted_response=final)
    batches, missing = run.build_dynamic_judge_batches([judge_record])
    assert request["provider"]["order"] == ["MiniMax"]
    assert batches == [[judge_record]] and missing == []
    assert "reasoning" not in json.dumps(judge_record)
