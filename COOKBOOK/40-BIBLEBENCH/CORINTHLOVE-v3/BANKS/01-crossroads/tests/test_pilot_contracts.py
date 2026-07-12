from __future__ import annotations

from copy import deepcopy
import json
import sys
from pathlib import Path

import pytest


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK))

from pilot import contracts  # noqa: E402
from pilot.selection import freeze_canary_selection, select_canary_ids  # noqa: E402


def _public_rows():
    clauses = [f"C{i}" for i in range(1, 17)]
    groups = [
        clauses[0:4], clauses[4:8], clauses[8:12], clauses[12:16],
        ["C1", "C5", "C9", "C13"], ["C2", "C6", "C10", "C14"],
    ]
    episodes, truth = [], {}
    for index, covered in enumerate(groups, 1):
        item_id = f"CROSSROADS-{600 + index:04d}"
        episodes.append({
            "id": item_id,
            "split": "public",
            "tools": [{"name": "workspace.edit"}, {"name": "chat.send"}],
        })
        truth[item_id] = {"split": "public", "clauses": covered}
    return episodes, truth


def _catalog_evidence(alias="openai/gpt-5-nano", tags=("azure",)):
    model = contracts.resolve_model(alias)
    name = f"Azure | {model['expected_snapshot']}"
    endpoints = [{
        "model_id": alias, "provider_name": "Azure", "name": name,
        "tag": tag, "status": 0,
        "context_length": 400_000,
        "supported_parameters": list(contracts.REQUIRED_PARAMETERS),
        "pricing": {
            "prompt": str(model["price_ceiling_per_token"]["input"]),
            "completion": str(model["price_ceiling_per_token"]["output"]),
        },
    } for tag in tags]
    zdr_endpoints = [
        {**deepcopy(endpoint), "model_id": alias} for endpoint in endpoints
    ]
    return {
        "catalog_evidence_version": "openrouter-model-zdr-intersection-v1",
        "model_id": alias,
        "model_catalog_url": (
            f"https://openrouter.ai/api/v1/models/{alias}/endpoints"
        ),
        "zdr_catalog_url": "https://openrouter.ai/api/v1/endpoints/zdr",
        "model_catalog_response": {
            "data": {
                "id": alias, "endpoints": endpoints,
            },
        },
        "zdr_catalog_response": {"data": zdr_endpoints},
    }


def test_frozen_profile_contains_only_four_authorized_cheap_models():
    profile = contracts.load_profile()
    assert profile["profile_id"] == "crossroads-cheap-azure-v6"
    assert set(profile["models"]) == {
        "openai/gpt-5-nano",
        "openai/gpt-5.4-nano",
        "openai/gpt-5-mini",
        "openai/gpt-5.4-mini",
    }
    assert {
        alias: row["expected_snapshot"]
        for alias, row in profile["models"].items()
    } == {
        "openai/gpt-5-nano": "openai/gpt-5-nano-2025-08-07",
        "openai/gpt-5.4-nano": "openai/gpt-5.4-nano-20260317",
        "openai/gpt-5-mini": "openai/gpt-5-mini-2025-08-07",
        "openai/gpt-5.4-mini": "openai/gpt-5.4-mini-20260317",
    }
    assert profile["routing"] == {
        "only": ["azure"], "order": ["azure"],
        "allow_fallbacks": False, "require_parameters": True,
        "data_collection": "deny", "zdr": True,
    }
    assert profile["completion_policy"] == {
        "evidence_version": "openrouter-chat-router-metadata-v1",
        "require_generation_header": True,
        "require_response_provider": True,
        "require_router_metadata": True,
    }
    with pytest.raises(ValueError, match="not in the frozen cheap allowlist"):
        contracts.resolve_model("openai/gpt-5.4")


def test_every_profile_identity_snapshot_routing_and_ceiling_is_runtime_frozen():
    profile = contracts.load_profile()
    mutations = []
    for path, value in (
        (("profile_id",), "changed-profile"),
        (("purpose",), "measurement"),
        (("immutable",), False),
        (("catalog_snapshot_utc",), "2099-01-01T00:00:00Z"),
        (("minimum_context_length",), 1),
        (("reasoning_effort",), "high"),
        (("completion_policy", "require_router_metadata"), False),
        (("routing", "only"), ["OpenAI"]),
        (("models", "openai/gpt-5-nano", "expected_snapshot"),
         "openai/gpt-5.4"),
        (("models", "openai/gpt-5-nano", "price_ceiling_per_token", "output"),
         99),
    ):
        poisoned = deepcopy(profile)
        target = poisoned
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(poisoned)
    poisoned = deepcopy(profile)
    poisoned["unfrozen_extra"] = True
    mutations.append(poisoned)

    for poisoned in mutations:
        with pytest.raises(ValueError, match="frozen cheap profile"):
            contracts.resolve_model("openai/gpt-5-nano", poisoned)


def test_profile_loader_rejects_duplicate_json_keys(tmp_path):
    path = tmp_path / "profile.json"
    path.write_text('{"profile_id":"a","profile_id":"b"}\n')
    with pytest.raises(ValueError, match="strict JSON"):
        contracts.load_profile(path)


def test_runtime_profile_baseline_cannot_be_redefined_by_mutating_exported_data():
    baseline = contracts.load_profile()
    poisoned = deepcopy(baseline)
    poisoned["profile_id"] = "attacker-redefined-profile"
    original = contracts.FROZEN_PROFILE["profile_id"]
    try:
        contracts.FROZEN_PROFILE["profile_id"] = poisoned["profile_id"]
        with pytest.raises(ValueError, match="frozen cheap profile"):
            contracts.resolve_model("openai/gpt-5-nano", poisoned)
    finally:
        contracts.FROZEN_PROFILE["profile_id"] = original


def test_catalog_gate_accepts_one_or_more_exact_azure_endpoints_in_zdr_catalog():
    model = contracts.resolve_model("openai/gpt-5-nano")
    catalog = _catalog_evidence(tags=("azure/swedencentral", "azure"))
    attestation = contracts.validate_catalog(catalog, model)
    assert attestation["eligible_endpoint_count"] == 2
    assert attestation["endpoint_tags"] == ["azure", "azure/swedencentral"]
    assert "zdr" not in attestation
    assert attestation["zdr_attestation"] == {
        "observed": True,
        "method": "exact-endpoint-membership",
        "source": "https://openrouter.ai/api/v1/endpoints/zdr",
    }


def test_catalog_gate_rejects_absent_zdr_membership_status_and_price_drift():
    model = contracts.resolve_model("openai/gpt-5-nano")
    catalog = _catalog_evidence()
    poisoned = json.loads(json.dumps(catalog))
    poisoned["zdr_catalog_response"]["data"] = []
    with pytest.raises(ValueError, match="eligible exact Azure/ZDR endpoint"):
        contracts.validate_catalog(poisoned, model)

    poisoned = json.loads(json.dumps(catalog))
    poisoned["model_catalog_response"]["data"]["endpoints"][0][
        "status"
    ] = "available"
    poisoned["zdr_catalog_response"]["data"][0]["status"] = "available"
    with pytest.raises(ValueError, match="status policy"):
        contracts.validate_catalog(poisoned, model)

    poisoned = json.loads(json.dumps(catalog))
    poisoned["model_catalog_response"]["data"]["endpoints"][0]["status"] = 1
    poisoned["zdr_catalog_response"]["data"][0]["status"] = 1
    with pytest.raises(ValueError, match="status policy"):
        contracts.validate_catalog(poisoned, model)

    poisoned = json.loads(json.dumps(catalog))
    poisoned["model_catalog_response"]["data"]["endpoints"][0]["pricing"][
        "completion"
    ] = "0.1"
    poisoned["zdr_catalog_response"]["data"][0]["pricing"][
        "completion"
    ] = "0.1"
    with pytest.raises(ValueError, match="price ceiling"):
        contracts.validate_catalog(poisoned, model)


def test_catalog_gate_rejects_cross_catalog_endpoint_fact_disagreement():
    model = contracts.resolve_model("openai/gpt-5-nano")
    catalog = _catalog_evidence()
    catalog["zdr_catalog_response"]["data"][0]["context_length"] = 399_999
    with pytest.raises(ValueError, match="catalogs disagree"):
        contracts.validate_catalog(catalog, model)


def test_catalog_gate_does_not_union_capabilities_across_endpoints():
    model = contracts.resolve_model("openai/gpt-5-nano")
    catalog = _catalog_evidence(tags=("azure/one", "azure/two"))
    missing = list(contracts.REQUIRED_PARAMETERS)
    catalog["model_catalog_response"]["data"]["endpoints"][0][
        "supported_parameters"
    ] = missing[:-1]
    catalog["zdr_catalog_response"]["data"][0][
        "supported_parameters"
    ] = missing[:-1]
    catalog["model_catalog_response"]["data"]["endpoints"][1][
        "supported_parameters"
    ] = missing[1:]
    catalog["zdr_catalog_response"]["data"][1][
        "supported_parameters"
    ] = missing[1:]
    with pytest.raises(ValueError, match="missing required parameters"):
        contracts.validate_catalog(catalog, model)


def test_catalog_gate_requires_duplicate_regions_to_have_equivalent_facts():
    model = contracts.resolve_model("openai/gpt-5-nano")
    catalog = _catalog_evidence(tags=("azure/one", "azure/two"))
    catalog["model_catalog_response"]["data"]["endpoints"][1][
        "context_length"
    ] = 400_001
    catalog["zdr_catalog_response"]["data"][1]["context_length"] = 400_001
    with pytest.raises(ValueError, match="routes are not equivalent"):
        contracts.validate_catalog(catalog, model)


def test_set_cover_freezes_six_public_ids_with_clause_family_and_substrate_coverage(tmp_path):
    episodes, truth = _public_rows()
    selected = select_canary_ids(episodes, truth)
    assert selected == [row["id"] for row in episodes]
    path = tmp_path / "canary_selection.json"
    frozen = freeze_canary_selection(path, episodes, truth, bank_sha256="a" * 64)
    assert frozen["item_ids"] == selected
    assert frozen["coverage"]["clauses"] == [f"C{i}" for i in range(1, 17)]
    assert len(frozen["coverage"]["fallback_families"]) == 6
    assert frozen["coverage"]["substrates"] == ["chat.send", "workspace.edit"]
    with pytest.raises(FileExistsError):
        freeze_canary_selection(path, episodes, truth, bank_sha256="a" * 64)


def test_set_cover_rejects_private_rows_and_incomplete_coverage():
    episodes, truth = _public_rows()
    episodes[0]["split"] = "private"
    with pytest.raises(ValueError, match="public"):
        select_canary_ids(episodes, truth)
    episodes, truth = _public_rows()
    truth[episodes[3]["id"]]["clauses"] = ["C1"]
    with pytest.raises(ValueError, match="six-item set cover"):
        select_canary_ids(episodes, truth)


@pytest.mark.parametrize(
    "poison",
    [
        {"Authorization": "Bearer secret"},
        {"api_key": "secret"},
        {"nested": ["sk-or-v1-abcdefghijklmnopqrstuvwxyz"]},
        {"nested": "OPENROUTER_API_KEY=secret"},
    ],
)
def test_artifact_secret_scan_rejects_keys_and_values(poison):
    with pytest.raises(ValueError, match="credential"):
        contracts.assert_artifact_safe(poison)
