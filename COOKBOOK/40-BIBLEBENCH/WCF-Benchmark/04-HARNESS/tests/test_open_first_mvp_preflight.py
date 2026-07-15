from __future__ import annotations

import copy
import csv
import json
import os
import sys

import pytest


HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

import open_first_mvp_preflight as preflight  # noqa: E402
from wcfbench import load_items  # noqa: E402
import wcfbench.codex_oauth_judge as judge_module  # noqa: E402


PRICES = {
    "minimax/minimax-m3": (0.0000003, 0.0000012),
    "z-ai/glm-5.2": (0.000000903, 0.000002838),
    "deepseek/deepseek-v4-pro": (0.000000435, 0.00000087),
    "qwen/qwen3.7-max": (0.00000125, 0.00000375),
    "google/gemma-4-31b-it": (0.00000012, 0.00000035),
    "meta-llama/llama-4-maverick": (0.0000002, 0.0000008),
}


def _catalog():
    catalog = {
        slug: {
            "id": slug,
            "canonical_slug": f"{slug}-canonical",
            "architecture": {
                "input_modalities": ["text"],
                "output_modalities": ["text"],
            },
            "context_length": 131072,
            "top_provider": {"context_length": 131072, "max_completion_tokens": 8192},
            "links": {"details": f"/api/v1/models/{slug}/endpoints"},
            "pricing": {"prompt": str(prices[0]), "completion": str(prices[1])},
            "supported_parameters": ["temperature", "max_tokens", "reasoning"],
            "reasoning": {"mandatory": False, "supported_efforts": ["none", "high"]},
        }
        for slug, prices in PRICES.items()
    }
    catalog["meta-llama/llama-4-maverick"].pop("reasoning")
    catalog["meta-llama/llama-4-maverick"]["supported_parameters"].remove(
        "reasoning")
    return catalog


def _endpoints():
    return {
        slug: [{
            "provider_name": "fixture-provider",
            "data_collection": "deny",
            "supported_parameters": ["temperature", "max_tokens", "reasoning"],
            "pricing": {"prompt": str(prices[0]), "completion": str(prices[1])},
        }]
        for slug, prices in PRICES.items()
    }


def _prompt_ceilings():
    ceilings = {
        name: {
            "max_rendered_prompt_bytes": 3000 + index,
            "prompt_tokens": 3000 + index,
            "completion_tokens": 2048 if name == "sut" else 0,
            "source": "offline_rendered_prompt_ceiling",
        }
        for index, name in enumerate(preflight.PROMPT_CLASSES)
    }
    ceilings["sut"].update({
        "max_rendered_user_bytes": 1939,
        "max_rendered_transport_bytes": 2221,
        "max_rendered_prompt_bytes": 2221,
        "prompt_tokens": 2221,
    })
    return ceilings


def test_frozen_contract_and_geometry_match_the_bank():
    assert preflight.VALIDITY_LABEL == (
        "EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · "
        "SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE"
    )
    assert preflight.SUTS == tuple(PRICES)
    geometry = preflight.build_geometry(
        load_items(str(preflight.BANK_DIR)))
    assert geometry == {
        "bank_items": 230,
        "runnable_scorable_items": 226,
        "diagnostic_items": 4,
        "sut_cells": 1380,
        "scorable_sut_cells": 1356,
        "diagnostic_sut_cells": 24,
        "scalar_eligible_per_sut": 222,
        "scalar_eligible_total": 1332,
        "contested_per_sut": 4,
        "contested_total": 24,
        "logical_judge_decisions_per_sut": 348,
        "logical_judge_decisions_total": 2088,
        "judge_batch_size": 8,
        "judge_tasks_per_sut": 44,
        "judge_tasks_total": 264,
        "judge_route_decisions_per_sut": {
            "open": 310, "contested": 16, "episode": 22,
        },
        "sut_attempts_initial": 1380,
        "sut_retries_reserved_per_model": 22,
        "sut_attempts_max_per_model": 252,
        "sut_attempts_max_total": 1512,
    }


def test_manifest_freezes_catalog_prices_as_request_ceilings_and_no_auth_check():
    manifest = preflight.build_manifest(
        _catalog(), _endpoints(), _prompt_ceilings(),
        catalog_retrieved_at="2026-07-14T00:00:00Z",
    )
    assert manifest["validity_label"] == preflight.VALIDITY_LABEL
    assert manifest["auth_balance"] == {
        "status": "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED",
        "balance_usd": None,
        "top_up_usd": None,
    }
    assert manifest["sut_request_common"] == {
        "temperature": 0,
        "max_tokens": 2048,
        "tools": False,
        "web": False,
        "substitutions": False,
        "perturbations": False,
        "model_fallbacks": False,
    }
    for row in manifest["models"]:
        prompt, completion = PRICES[row["slug"]]
        assert row["provider_policy"] == {
            "sort": "price",
            "require_parameters": True,
            "data_collection": "deny",
            "max_price": {
                "prompt": prompt * 1_000_000,
                "completion": completion * 1_000_000,
            },
        }
        assert row["eligible_data_policy_endpoints"] == ["fixture-provider"]
        if row["slug"] == "meta-llama/llama-4-maverick":
            assert "reasoning" not in row["request_parameters"]
        else:
            assert row["request_parameters"]["reasoning"] == {"enabled": False}
    assert manifest["catalog_hash"] == preflight.build_manifest(
        _catalog(), _endpoints(), _prompt_ceilings(),
        catalog_retrieved_at="2026-07-14T00:00:00Z",
    )["catalog_hash"]
    assert manifest["planning_cost"] == {
        "sut_attempt_envelope_usd": pytest.approx(6.857361504),
        "utilization_fraction": 0.8,
        "proposed_cap_usd": 8.58,
    }


def test_more_expensive_endpoint_is_excluded_when_one_endpoint_meets_price_gate():
    endpoints = _endpoints()
    slug = preflight.SUTS[0]
    expensive = copy.deepcopy(endpoints[slug][0])
    expensive["provider_name"] = "expensive-provider"
    expensive["pricing"]["prompt"] = "99"
    expensive["pricing"]["completion"] = "99"
    endpoints[slug].insert(0, expensive)

    manifest = preflight.build_manifest(
        _catalog(), endpoints, _prompt_ceilings(),
        catalog_retrieved_at="2026-07-14T00:00:00Z",
    )

    row = next(model for model in manifest["models"] if model["slug"] == slug)
    assert row["eligible_data_policy_endpoints"] == ["fixture-provider"]
    assert row["provider_policy"] == {
        "sort": "price",
        "require_parameters": True,
        "data_collection": "deny",
        "max_price": {
            "prompt": PRICES[slug][0] * 1_000_000,
            "completion": PRICES[slug][1] * 1_000_000,
        },
    }


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda catalog, endpoints: catalog.pop(preflight.SUTS[0]), "missing exact"),
        (lambda catalog, endpoints: catalog[preflight.SUTS[0]].pop("context_length"),
         "context"),
        (lambda catalog, endpoints: catalog[preflight.SUTS[0]].pop("pricing"),
         "pricing"),
        (lambda catalog, endpoints: catalog[preflight.SUTS[0]].pop("architecture"),
         "capabilit"),
        (lambda catalog, endpoints: catalog[preflight.SUTS[0]]["reasoning"].update(
            {"mandatory": True}), "reasoning.*mandatory"),
        (lambda catalog, endpoints: endpoints.update({preflight.SUTS[0]: []}),
         "data-policy endpoint"),
        (lambda catalog, endpoints: endpoints[preflight.SUTS[0]][0]["pricing"].update(
            {"completion": "99"}), "price ceiling"),
    ],
)
def test_catalog_validation_fails_closed(mutation, message):
    catalog, endpoints = _catalog(), _endpoints()
    mutation(catalog, endpoints)
    with pytest.raises(preflight.PreflightError, match=message):
        preflight.build_manifest(
            catalog, endpoints, _prompt_ceilings(),
            catalog_retrieved_at="2026-07-14T00:00:00Z",
        )


def test_public_catalog_fetch_never_calls_auth_endpoint():
    calls = []
    catalog = _catalog()
    endpoints = _endpoints()

    def opener(url, api_key):
        calls.append((url, api_key))
        if url == preflight.MODELS_URL:
            return {"data": list(catalog.values())}
        slug = url.split("/models/", 1)[1].rsplit("/endpoints", 1)[0]
        return {"data": {"endpoints": endpoints[slug]}}

    got_catalog, got_endpoints = preflight.fetch_public_catalog(opener=opener)
    assert got_catalog == catalog
    assert got_endpoints == endpoints
    assert all(api_key is None for _url, api_key in calls)
    assert all("/auth/key" not in url for url, _api_key in calls)


def test_reasoning_mandatory_false_is_suppressed_without_effort_support():
    catalog = copy.deepcopy(_catalog())
    catalog[preflight.SUTS[0]]["reasoning"] = {
        "mandatory": False, "supported_efforts": ["high"]}
    manifest = preflight.build_manifest(
        catalog, _endpoints(), _prompt_ceilings(),
        catalog_retrieved_at="2026-07-14T00:00:00Z",
    )
    row = next(model for model in manifest["models"]
               if model["slug"] == preflight.SUTS[0])
    assert row["request_parameters"]["reasoning"] == {"enabled": False}


@pytest.mark.parametrize("mandatory", [True, None])
def test_reasoning_mandatory_true_or_unknown_fails_closed(mandatory):
    catalog = copy.deepcopy(_catalog())
    if mandatory is None:
        catalog[preflight.SUTS[0]]["reasoning"].pop("mandatory")
    else:
        catalog[preflight.SUTS[0]]["reasoning"]["mandatory"] = mandatory
    with pytest.raises(preflight.PreflightError, match="reasoning.*mandatory"):
        preflight.build_manifest(
            catalog, _endpoints(), _prompt_ceilings(),
            catalog_retrieved_at="2026-07-14T00:00:00Z",
        )


def test_reasoning_parameter_capability_without_metadata_fails_closed():
    catalog = copy.deepcopy(_catalog())
    catalog[preflight.SUTS[0]].pop("reasoning")
    with pytest.raises(preflight.PreflightError, match="reasoning capability is unknown"):
        preflight.build_manifest(
            catalog, _endpoints(), _prompt_ceilings(),
            catalog_retrieved_at="2026-07-14T00:00:00Z",
        )


def test_request_enforced_data_denial_accepts_omitted_endpoint_field():
    endpoints = _endpoints()
    for rows in endpoints.values():
        rows[0].pop("data_collection")
    manifest = preflight.build_manifest(
        _catalog(), endpoints, _prompt_ceilings(),
        catalog_retrieved_at="2026-07-14T00:00:00Z",
    )
    assert all(row["provider_policy"]["data_collection"] == "deny"
               and row["provider_policy"]["require_parameters"] is True
               for row in manifest["models"])


def test_sut_prompt_ceiling_is_derived_from_frozen_bank_rendering():
    ceiling = preflight.derive_sut_prompt_ceiling(
        load_items(str(preflight.BANK_DIR)))
    assert ceiling == {
        "status": "MEASURED_OFFLINE",
        "source": "frozen_bank_rendered_prompts",
        "max_rendered_user_bytes": 1939,
        "max_rendered_transport_bytes": 2221,
        "max_user_item_id": "MEND-C1-W301",
        "max_transport_item_id": "MEND-C1-W301",
        "prompt_tokens": 2221,
        "completion_tokens": 2048,
    }


def test_judge_prompt_ceilings_are_conservative_and_derived_offline():
    ceilings = preflight.derive_judge_prompt_ceilings(
        preflight.derive_sut_prompt_ceiling(
            load_items(str(preflight.BANK_DIR))))
    assert set(ceilings) == {"judge_open", "judge_contested", "judge_episode"}
    for route, row in ceilings.items():
        assert row["status"] == "DERIVED_OFFLINE_CONSERVATIVE"
        assert row["source"] == "offline_rendered_prompt_ceiling"
        assert row["route"] == route
        assert row["max_sut_response_tokens_per_record"] == 2048
        assert row["batch_size"] == 8
        assert row["max_rendered_prompt_bytes"] == row["prompt_tokens"]
        assert row["max_rendered_prompt_bytes"] == (
            judge_module.judge_prompt_byte_ceiling())
        assert row["max_judge_input_serialized_bytes"] == (
            judge_module.MAX_JUDGE_INPUT_SERIALIZED_BYTES)
        assert row["max_record_id_bytes"] == judge_module.MAX_RECORD_ID_BYTES
        assert row["max_criterion_id_bytes"] == judge_module.MAX_CRITERION_ID_BYTES
        assert row["max_sut_response_bytes"] == judge_module.MAX_SUT_RESPONSE_BYTES


def test_schedule_freezes_exact_item_id_partitions():
    schedule = preflight.build_schedule(load_items(str(preflight.BANK_DIR)))
    assert len(schedule["all_item_ids"]) == 230
    assert len(schedule["runnable_item_ids"]) == 226
    assert schedule["dev_set_only_item_ids"] == [
        "LIB-C2-W305", "LIB-C3-W202", "LIB-C7-008", "LIB-C8-W304"]
    assert len(schedule["scalar_eligible_item_ids"]) == 222
    assert schedule["contested_item_ids"] == [
        "AGG-C3-W302", "AGG-C5-W304", "AGG-C7-007", "AGG-C8-W305"]
    assert {route: len(ids) for route, ids in schedule[
        "judge_route_item_ids"].items()} == {
            "open": 161, "contested": 4, "episode": 22}
    assert not (set(schedule["runnable_item_ids"])
                & set(schedule["dev_set_only_item_ids"]))


def test_public_preflight_failure_writes_durable_nonexecutable_packet(tmp_path):
    output = tmp_path / "20260714-open-first-failed"
    endpoints = _endpoints()
    for rows in endpoints.values():
        rows[0]["data_collection"] = "allow"
    result = preflight.run_public_preflight(
        output,
        metadata_fetch=lambda: (_catalog(), endpoints),
        now=lambda: "2026-07-14T00:00:00Z",
    )
    assert result["status"] == "FAILED/NON-EXECUTABLE"
    assert not (output / "open-first-mvp-manifest.json").exists()
    expected = {
        "public-catalog-snapshot.json", "public-endpoint-snapshots.json",
        "prompt-ceilings.json", "cost-plan.json", "cost-plan.csv",
        "preflight-report.md", "failed-preflight.json",
    }
    assert {path.name for path in output.iterdir()} == expected
    failure = json.loads((output / "failed-preflight.json").read_text())
    assert failure["status"] == "FAILED/NON-EXECUTABLE"
    assert failure["auth_balance"]["status"] == (
        "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED")
    assert any("data-policy endpoint" in blocker for blocker in failure["blockers"])
    assert len(failure["catalog_hash"]) == 64
    assert failure["canonical_slugs"] == {
        slug: f"{slug}-canonical" for slug in preflight.SUTS}
    report = (output / "preflight-report.md").read_text()
    assert failure["catalog_hash"] in report
    assert "canonical slugs" in report.lower()
    prompts = json.loads((output / "prompt-ceilings.json").read_text())
    assert prompts["sut"]["max_rendered_transport_bytes"] == 2221
    for route in ("judge_open", "judge_contested", "judge_episode"):
        assert prompts[route]["status"] == "DERIVED_OFFLINE_CONSERVATIVE"
    costs = json.loads((output / "cost-plan.json").read_text())
    assert costs["totals"] == {
        "no_retry_230_calls_usd": pytest.approx(6.25870296),
        "attempt_envelope_252_calls_usd": pytest.approx(6.857361504),
        "proposed_cap_usd": 8.58,
    }
    with (output / "cost-plan.csv").open(newline="", encoding="utf-8") as handle:
        cost_rows = list(csv.DictReader(handle))
    assert len(cost_rows) == 7
    assert cost_rows[-1]["slug"] == "TOTAL"
    assert float(cost_rows[-1]["no_retry_230_calls_usd"]) == pytest.approx(
        6.25870296)
    assert float(cost_rows[-1]["attempt_envelope_252_calls_usd"]) == pytest.approx(
        6.857361504)


def test_public_preflight_derives_judge_route_ceilings_before_responses_exist(tmp_path):
    output = tmp_path / "20260714-open-first-success"
    result = preflight.run_public_preflight(
        output,
        metadata_fetch=lambda: (_catalog(), _endpoints()),
        now=lambda: "2026-07-14T00:00:00Z",
    )
    assert result["status"] == "EXECUTABLE-MANIFEST-INPUT"
    manifest = json.loads((output / "open-first-mvp-manifest.json").read_text())
    assert manifest["auth_balance"]["status"] == (
        "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED")
    assert manifest["rendered_prompt_ceilings"]["sut"][
        "max_rendered_transport_bytes"] == 2221
    assert all(manifest["rendered_prompt_ceilings"][route]["status"]
               == "DERIVED_OFFLINE_CONSERVATIVE"
               for route in ("judge_open", "judge_contested", "judge_episode"))
    assert not (output / "failed-preflight.json").exists()


def test_public_preflight_refuses_overwrite_before_fetch(tmp_path):
    output = tmp_path / "already-exists"
    output.mkdir()
    calls = []
    with pytest.raises(preflight.PreflightOutputError, match="already exists"):
        preflight.run_public_preflight(
            output, metadata_fetch=lambda: calls.append(True),
            now=lambda: "2026-07-14T00:00:00Z")
    assert calls == []


def test_cli_catches_validation_failure_after_writing_packet(tmp_path):
    output = tmp_path / "cli-failure"
    endpoints = _endpoints()
    for rows in endpoints.values():
        rows[0]["data_collection"] = "allow"
    rc = preflight.main(
        ["--public-preflight", "--output-dir", str(output)],
        metadata_fetch=lambda: (_catalog(), endpoints),
        now=lambda: "2026-07-14T00:00:00Z",
    )
    assert rc == 1
    assert (output / "failed-preflight.json").exists()


def test_default_clock_is_real_utc():
    timestamp = preflight._utc_now()
    assert timestamp.endswith("Z")
    assert "T" in timestamp
    assert timestamp != "timestamp-unavailable"
