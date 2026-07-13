"""Hermetic contracts for the PPP-1 zero-paid metadata preflight."""

from __future__ import annotations

import json
import os
import sys

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

import ppp1_preflight as ppp1  # noqa: E402
from wcfbench import load_items  # noqa: E402


def _bomb(*_args, **_kwargs):
    raise AssertionError("dry mode touched metadata or artifacts")


def _catalog_entry(slug, prompt, completion, **extra):
    entry = {
        "id": slug,
        "name": slug,
        "context_length": 131072,
        "architecture": {
            "input_modalities": ["text"],
            "output_modalities": ["text"],
        },
        "pricing": {"prompt": str(prompt), "completion": str(completion)},
        "supported_parameters": ["max_tokens", "response_format"],
    }
    entry.update(extra)
    return entry


def _catalog():
    return {
        "meta-llama/llama-3.1-8b-instruct": _catalog_entry(
            "meta-llama/llama-3.1-8b-instruct", "0.00000002", "0.00000003"),
        "deepseek/deepseek-chat": _catalog_entry(
            "deepseek/deepseek-chat", "0.0000002002", "0.0000008001"),
        "qwen/qwen3.7-plus": _catalog_entry(
            "qwen/qwen3.7-plus", "0.00000032", "0.00000128"),
        "google/gemini-2.5-flash": _catalog_entry(
            "google/gemini-2.5-flash", "0.0000003", "0.0000025"),
    }


def _profiles():
    return {
        "base_sut": {
            "prompt_tokens": 1939,
            "completion_tokens": 2048,
            "source": "rendered_prompt_fixed_completion_ceiling",
            "derivation": {"request_class": "base_sut"},
        },
        "base_judge": {
            "prompt_tokens": 16000,
            "completion_tokens": 2048,
            "source": "rendered_prompt_fixed_completion_ceiling",
            "derivation": {"request_class": "base_judge"},
        },
    }


def _metadata():
    return {
        "key_snapshot": {
            "usage": 1436.0,
            "limit": 1500.0,
            "limit_remaining": 64.0,
        },
        "catalog": _catalog(),
        "catalog_retrieved_at": "2026-07-13T18:30:00Z",
    }


def test_dry_mode_has_no_network_or_writes(capsys):
    assert ppp1.main([], metadata_fetch=_bomb, artifact_writer=_bomb) == 0
    output = capsys.readouterr().out
    assert "DRY RUN" in output
    assert "no inference" in output.lower()


def test_call_plan_is_exact_226_by_three_single_judge_geometry():
    items = load_items(os.path.join(os.path.dirname(HARNESS), "05-BANK-YAML"))

    plan = ppp1.build_call_plan(items)

    assert plan["runnable_items"] == 226
    assert plan["judge_calls_per_sut"] == 348
    assert plan["totals"] == {"sut": 678, "judge": 1044, "total": 1722}
    assert len(plan["classes"]) == 6
    for sut in ppp1.PPP1_SUTS:
        assert any(row["model"] == sut and row["count"] == 226
                   for row in plan["classes"] if row["role"] == "sut")
        assert any(row["sut_context"] == sut and row["count"] == 348
                   for row in plan["classes"] if row["role"] == "judge")


def test_payloads_freeze_exact_roster_cost_runtime_and_cap_conflict():
    payloads = ppp1.build_preflight_payloads(_profiles(), _metadata())
    manifest = payloads["ppp1-run-manifest.json"]

    assert set(payloads) == ppp1.EXPECTED_ARTIFACTS
    assert manifest["sut_roster"] == list(ppp1.PPP1_SUTS)
    assert manifest["judge"] == ppp1.PPP1_JUDGE
    assert manifest["logical_calls"] == 1722
    assert manifest["forecast_cost_usd"] > 5.0
    assert manifest["minimum_ratifiable_cap_usd"] > manifest["forecast_cost_usd"]
    assert manifest["strategy_cap_usd"] == 5.0
    assert manifest["strategy_cap_feasible"] is False
    assert manifest["required_top_up_usd"] == 0.0
    assert manifest["runtime"]["baseline_minutes"] > 0
    assert manifest["paid_inference_authorized"] is False
    assert "EXPLORATORY MANUSCRIPT PREVIEW" in manifest["validity_label"]
    assert "chat/completions" not in json.dumps(payloads)


def test_budget_branches_are_monotonic_and_zero_floor_is_not_executable():
    call_plan = ppp1.build_call_plan(
        load_items(os.path.join(os.path.dirname(HARNESS), "05-BANK-YAML")))

    branches = ppp1.build_budget_branches(
        call_plan["classes"], _catalog(), _profiles())

    assert [row["judge_completion_tokens"] for row in branches] == [
        2048, 1024, 512, 256, 0]
    assert all(left["forecast_cost_usd"] > right["forecast_cost_usd"]
               for left, right in zip(branches, branches[1:]))
    assert all(row["executable"] is True for row in branches[:-1])
    assert branches[-1]["executable"] is False
    assert branches[-1]["forecast_cost_usd"] > ppp1.STRATEGY_CAP_USD


def test_missing_slug_price_or_required_capability_fails_loudly():
    catalog = _catalog()
    catalog.pop(ppp1.PPP1_JUDGE)
    metadata = dict(_metadata(), catalog=catalog)
    with pytest.raises(ValueError, match="missing exact PPP-1 catalog slug"):
        ppp1.build_preflight_payloads(_profiles(), metadata)

    catalog = _catalog()
    catalog[ppp1.PPP1_JUDGE]["supported_parameters"].remove("response_format")
    metadata = dict(_metadata(), catalog=catalog)
    with pytest.raises(ValueError, match="required parameter"):
        ppp1.build_preflight_payloads(_profiles(), metadata)


def test_cli_uses_injected_metadata_and_writer_without_exposing_secret(
        tmp_path, monkeypatch):
    inputs = tmp_path / "inputs.json"
    inputs.write_text(json.dumps({"token_profiles": _profiles()}), encoding="utf-8")
    captured = {}

    def writer(output_dir, payloads, *, forbidden_values):
        captured.update({"output_dir": str(output_dir), "payloads": payloads,
                         "forbidden_values": forbidden_values})
        return []

    monkeypatch.setenv("OPENROUTER_API_KEY", "runtime-secret")
    code = ppp1.main(
        ["--metadata-preflight", "--output-dir", str(tmp_path / "packet"),
         "--inputs-json", str(inputs)],
        metadata_fetch=lambda _key: _metadata(), artifact_writer=writer)

    assert code == 0
    assert set(captured["payloads"]) == ppp1.EXPECTED_ARTIFACTS
    assert captured["forbidden_values"] == ["runtime-secret"]
    assert "runtime-secret" not in json.dumps(captured["payloads"])


def test_writer_is_exclusive_and_rejects_secret_material(tmp_path):
    payloads = ppp1.build_preflight_payloads(_profiles(), _metadata())
    output = tmp_path / "packet"

    paths = ppp1.write_new_artifacts(
        output, payloads, forbidden_values=["runtime-secret"])
    assert len(paths) == 5
    with pytest.raises(FileExistsError):
        ppp1.write_new_artifacts(output, payloads)

    unsafe = dict(payloads)
    unsafe["auth-snapshot.json"] = {"note": "runtime-secret"}
    with pytest.raises(ppp1.SecretDisclosureError):
        ppp1.write_new_artifacts(
            tmp_path / "unsafe", unsafe, forbidden_values=["runtime-secret"])


def test_retry_geometry_matches_actual_normal_episode_and_judge_seams():
    items = load_items(os.path.join(os.path.dirname(HARNESS), "05-BANK-YAML"))

    geometry = ppp1.build_retry_geometry(items)

    assert geometry["initial_api_attempts"] == {
        "normal_sut": 612,
        "episode_sut": 66,
        "open_judge": 930,
        "contested_judge": 48,
        "episode_judge": 66,
        "total": 1722,
    }
    assert geometry["maximum_api_attempts"] == {
        "normal_sut": 612,
        "episode_sut": 132,
        "open_judge": 2628,
        "contested_judge": 120,
        "episode_judge": 132,
        "total": 3624,
    }
    assert geometry["maximum_retry_increment"] == 1902
    assert geometry["open_item_geometry"] == {
        "tagged_all_axes": {"items": 49, "initial_per_item": 1, "maximum_per_item": 4},
        "tagged_two_axes": {"items": 75, "initial_per_item": 2, "maximum_per_item": 6},
        "tagged_one_axis": {"items": 4, "initial_per_item": 3, "maximum_per_item": 8},
        "numeric_three_axes": {"items": 33, "initial_per_item": 3, "maximum_per_item": 6},
    }


def test_offline_correction_supersedes_retry_and_cap_fields_without_network(
        tmp_path, monkeypatch):
    original = tmp_path / "original"
    original.mkdir()
    (original / "ppp1-run-manifest.json").write_text(json.dumps(
        ppp1.build_preflight_payloads(_profiles(), _metadata())[
            "ppp1-run-manifest.json"]), encoding="utf-8")
    (original / "auth-snapshot.json").write_text(json.dumps({
        "validity_label": ppp1.VALIDITY_LABEL,
        "retrieved_at": "2026-07-13T18:30:00Z",
        **_metadata()["key_snapshot"],
    }), encoding="utf-8")
    (original / "openrouter-catalog-snapshot.json").write_text(json.dumps({
        "validity_label": ppp1.VALIDITY_LABEL,
        "retrieved_at": "2026-07-13T18:30:00Z",
        "models": list(_catalog().values()),
    }), encoding="utf-8")
    captured = {}

    def writer(output_dir, payloads, *, forbidden_values):
        captured.update(output_dir=str(output_dir), payloads=payloads,
                        forbidden_values=forbidden_values)
        return []

    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    code = ppp1.main(
        ["--offline-retry-correction", "--source-dir", str(original),
         "--output-dir", str(tmp_path / "correction")],
        metadata_fetch=_bomb, artifact_writer=writer)

    assert code == 0
    assert set(captured["payloads"]) == ppp1.CORRECTION_ARTIFACTS
    assert captured["forbidden_values"] == []
    correction = captured["payloads"]["ppp1-retry-correction.json"]
    assert correction["network_calls"] == 0
    assert correction["supersedes"]["retry_reserved_api_attempts"] == {
        "original": 3444, "corrected": 3624}
    assert correction["logical_forecast_cost_usd"] == pytest.approx(11.5698587676)
    assert correction["maximum_retry_reserved_forecast_cost_usd"] > 11.5698587676
    assert correction["maximum_retry_reserved_minimum_cap_usd"] > 14.47
    assert correction["strategy_cap_feasible"] is False
    assert all(ppp1.VALIDITY_LABEL in ppp1.render_artifact(name, payload)
               for name, payload in captured["payloads"].items())


def test_branch_addendum_labels_logical_branches_and_prices_each_retry_envelope(
        tmp_path, monkeypatch):
    original = tmp_path / "original"
    correction_dir = tmp_path / "correction"
    original.mkdir()
    correction_dir.mkdir()
    original_payloads = ppp1.build_preflight_payloads(_profiles(), _metadata())
    for name in ("ppp1-run-manifest.json", "auth-snapshot.json",
                 "openrouter-catalog-snapshot.json"):
        (original / name).write_text(
            json.dumps(original_payloads[name]), encoding="utf-8")
    correction_payloads = ppp1.build_retry_correction_payloads(original)
    (correction_dir / "ppp1-retry-correction.json").write_text(json.dumps(
        correction_payloads["ppp1-retry-correction.json"]), encoding="utf-8")
    captured = {}

    def writer(output_dir, payloads, *, forbidden_values):
        captured.update(output_dir=str(output_dir), payloads=payloads,
                        forbidden_values=forbidden_values)
        return []

    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    code = ppp1.main(
        ["--offline-branch-addendum", "--source-dir", str(original),
         "--correction-dir", str(correction_dir),
         "--output-dir", str(tmp_path / "addendum")],
        metadata_fetch=_bomb, artifact_writer=writer)

    assert code == 0
    assert set(captured["payloads"]) == ppp1.BRANCH_ADDENDUM_ARTIFACTS
    assert captured["forbidden_values"] == []
    addendum = captured["payloads"]["ppp1-branch-addendum.json"]
    assert addendum["network_calls"] == 0
    assert addendum["supersedes_or_qualifies"] == [
        "original completion-cap branch forecast/cap interpretation"]
    rows = addendum["branches"]
    assert [row["judge_completion_tokens"] for row in rows] == [2048, 1024, 512, 256, 0]
    assert all(row["logical_forecast_classification"] == "LOGICAL-CALL-ONLY"
               for row in rows)
    assert all(row["logical_forecast_retry_inclusive"] is False for row in rows)
    assert all(row["logical_forecast_is_live_nte"] is False for row in rows)
    assert all("unless retries are disabled" in row["live_nte_condition"] for row in rows)
    assert all(row["maximum_retry_envelope_forecast_usd"] >
               row["logical_forecast_usd"] for row in rows)
    assert all(row["maximum_retry_envelope_minimum_cap_usd"] >
               row["logical_minimum_cap_usd"] for row in rows)
    assert [row["executable"] for row in rows] == [True, True, True, True, False]
    assert all(row["maximum_retry_envelope_top_up_usd"] == 0.0 for row in rows)
    assert all(ppp1.VALIDITY_LABEL in ppp1.render_artifact(name, payload)
               for name, payload in captured["payloads"].items())
