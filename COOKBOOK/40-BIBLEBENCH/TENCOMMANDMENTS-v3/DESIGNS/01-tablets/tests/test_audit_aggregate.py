from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

from audits.run_all import (
    COST_CONFIG_PATH,
    FROZEN_OUTPUT_DIR,
    build_audit_bundle,
    derive_cost_preflight,
    derive_aggregate_status,
    load_cost_config,
    validate_audit_bundle,
    validate_audit_result,
    validate_cost_config,
)


@pytest.fixture(scope="module")
def bundle():
    return build_audit_bundle()


def test_status_reducer_is_fail_closed_and_blocker_aware():
    assert derive_aggregate_status(["PASS", "FAIL"], "PASS", True) == "FAIL"
    assert derive_aggregate_status(["PASS"] * 4, "REWORK", True) == "REWORK"
    assert derive_aggregate_status(["PASS"] * 4, "PASS", True) == (
        "COMPLETE_WITH_EMPIRICAL_BLOCKERS"
    )
    assert derive_aggregate_status(["PASS"] * 4, "PASS", False) == "PASS"


def test_canonical_cost_config_freezes_roster_prices_calls_and_provider_policy():
    config = load_cost_config()
    assert COST_CONFIG_PATH.is_file()
    assert config["max_prompt_tokens"] == 8192
    assert config["max_tokens"] == 1536
    assert config["syntax_repairs_per_request"] == 1
    assert config["provider_policy"] == {
        "allow_fallbacks": False,
        "require_parameters": True,
    }
    assert [
        (route["provider"], route["canonical_model_id"])
        for route in config["routes"]
    ] == [
        ("Novita", "inclusionai/ling-2.6-flash"),
        ("DeepInfra", "meta-llama/llama-3.1-8b-instruct"),
        ("DeepInfra", "mistralai/mistral-nemo"),
    ]
    assert [
        (route["prompt_price_per_token_usd"], route["completion_price_per_token_usd"])
        for route in config["routes"]
    ] == [
        ("0.00000001", "0.00000003"),
        ("0.00000002", "0.00000003"),
        ("0.00000002", "0.00000004"),
    ]
    assert {
        name: phase["initial_calls_per_route"]
        for name, phase in config["phases"].items()
    } == {"smoke": 6, "cheap_full": 636, "official": 1908}
    assert validate_cost_config(config) is True


@pytest.mark.parametrize("mutation", ("price", "calls", "fallback"))
def test_cost_config_validator_rejects_price_call_or_fallback_mutation(mutation):
    forged = deepcopy(load_cost_config())
    if mutation == "price":
        forged["routes"][0]["prompt_price_per_token_usd"] = "0.00000000"
    elif mutation == "calls":
        forged["phases"]["smoke"]["initial_calls_per_route"] = 5
    else:
        forged["provider_policy"]["allow_fallbacks"] = True
    with pytest.raises(ValueError, match="cost config|price|calls|fallback|frozen"):
        validate_cost_config(forged)


def test_cost_preflight_is_derived_with_decimal_from_frozen_config():
    assert derive_cost_preflight(load_cost_config()) == {
        "smoke": {
            "initial_requests": 18,
            "paid_calls": 36,
            "upper_bound_usd": "0.00675840",
            "cap_usd": "0.01",
            "authorization_status": "CHEAP_TEST_AUTHORIZED",
        },
        "cheap_full": {
            "initial_requests": 1908,
            "paid_calls": 3816,
            "upper_bound_usd": "0.71639040",
            "cap_usd": "1.00",
            "authorization_status": "CHEAP_TEST_AUTHORIZED",
        },
        "official": {
            "initial_requests": 5724,
            "paid_calls": 11448,
            "upper_bound_usd": "2.14917120",
            "cap_usd": "3.00",
            "authorization_status": "PREVIEW_ONLY_UNAUTHORIZED",
        },
    }


def test_aggregate_result_freezes_sections_blockers_and_cost_preflight(bundle):
    result = json.loads(bundle["audit-result.json"])

    assert result["status"] == "COMPLETE_WITH_EMPIRICAL_BLOCKERS"
    assert result["evidence_eligibility"] == "CREDENTIAL_FREE_ENGINEERING_ONLY"
    assert result["eligibility"] == {
        "empirical": False,
        "official": False,
        "publication": False,
    }
    assert result["judge_calls"] == 0
    assert {name: section["status"] for name, section in result["audits"].items()} == {
        "schema_balance": "PASS",
        "leakage": "PASS",
        "linkage_crux": "PASS",
        "mechanical_replay": "PASS",
        "lexical_length": "PASS",
    }
    assert result["evidence_status"]["overall_status"] == "NOT_RUN"
    assert result["evidence_status"]["casuistry_panel"] == "NOT_RUN"
    assert result["evidence_status"]["professional_baseline"] == "NOT_RUN"
    assert result["evidence_status"]["real_10pct_finetune_probe"] == "NOT_RUN"
    assert result["power_status"]["triad_coherence"] == (
        "NOT_ESTIMABLE_UNTIL_WIN_MARGINS"
    )
    assert result["cross_bank_seed_triad_audit_status"] == (
        "NOT_RUN_CRUX_BANK_UNAVAILABLE"
    )
    assert result["cost_preflight"] == {
        "smoke": {
            "initial_requests": 18,
            "paid_calls": 36,
            "upper_bound_usd": "0.00675840",
            "cap_usd": "0.01",
            "authorization_status": "CHEAP_TEST_AUTHORIZED",
        },
        "cheap_full": {
            "initial_requests": 1908,
            "paid_calls": 3816,
            "upper_bound_usd": "0.71639040",
            "cap_usd": "1.00",
            "authorization_status": "CHEAP_TEST_AUTHORIZED",
        },
        "official": {
            "initial_requests": 5724,
            "paid_calls": 11448,
            "upper_bound_usd": "2.14917120",
            "cap_usd": "3.00",
            "authorization_status": "PREVIEW_ONLY_UNAUTHORIZED",
        },
    }
    assert validate_audit_result(result) is True


def test_manifest_binds_exact_output_and_source_hashes(bundle):
    manifest = json.loads(bundle["manifest.json"])
    assert validate_audit_bundle(bundle) is True
    assert set(bundle) == {"audit-result.json", "report.md", "manifest.json"}
    for filename in ("audit-result.json", "report.md"):
        assert manifest["outputs"][filename] == {
            "bytes": len(bundle[filename]),
            "sha256": hashlib.sha256(bundle[filename]).hexdigest(),
        }
    assert manifest["sources"] == {
        "bank_manifest": {
            "path": "itembank/manifest.json",
            "sha256": "ec3a41aa0e786af65c3e520bd770dc2d021e738d656889ec0fc0420ad6706ce8",
        },
        "calibration_status": {
            "path": "calibration/evidence-status.json",
            "sha256": "64551752a65b2d557774e411118428d2d76e4671e312d002f50de3b9a3858890",
        },
        "power_report": {
            "path": "reports/power-report.json",
            "sha256": "de0641bdda96296d8f3a7a160c8b4e2f20d6c5b880106026f18077a23d2db8fb",
        },
        "private_bank": {
            "path": "itembank/gold/p1-private.gold.jsonl",
            "sha256": "597aeb5a5c4f4c07095068663134e59cd6a90b9d6dee56faef778e3a418cb7ef",
        },
        "public_bank": {
            "path": "itembank/bank/p1-public.jsonl",
            "sha256": "5c60194de2a1fd57276af83706bd8ff536749ee5039611711de7e5da61b44b4d",
        },
        "runtime_manifest": {
            "path": "itembank/runtime/p1-runtime-manifest.jsonl",
            "sha256": "537c2dcd57b75966880ff47696a414ab74229b654864d7f139abb255d0967d5f",
        },
    }


def test_result_and_manifest_bind_complete_executable_provenance(bundle):
    result = json.loads(bundle["audit-result.json"])
    manifest = json.loads(bundle["manifest.json"])
    required_paths = {
        "audits/__init__.py",
        "audits/schema_balance.py",
        "audits/leakage.py",
        "audits/linkage_crux.py",
        "audits/mechanical_replay.py",
        "audits/lexical_length.py",
        "audits/run_all.py",
        "audits/config/openrouter-cheap-roster.json",
        "calibration/status.py",
        "analysis/power.py",
        "scoring/mechanical.py",
        "itembank/generator.py",
        "itembank/build_bank.py",
        "tablets_schemas.py",
        "tablets_constants.py",
        "tablets_hashing.py",
        "preregistration.md",
        "crux-coregistration-linkage.json",
        "TENCOMMANDMENTS-REVIEWS/20260706-tablets-crux-coregistration.md",
    }
    assert set(result["provenance_hashes"]) == required_paths
    assert manifest["provenance"] == result["provenance_hashes"]
    for relative, digest in result["provenance_hashes"].items():
        path = (
            Path(__file__).resolve().parents[4] / relative
            if relative.startswith("TENCOMMANDMENTS-REVIEWS/")
            else Path(__file__).resolve().parents[1] / relative
        )
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest


@pytest.mark.parametrize(
    "mutation", ("cost", "cost_literal", "status", "promotion", "source_hash", "code_hash")
)
def test_result_validator_rejects_cost_status_hash_or_promotion_forgery(bundle, mutation):
    forged = json.loads(bundle["audit-result.json"])
    if mutation == "cost":
        forged["cost_preflight"]["smoke"]["cap_usd"] = "99.00"
        expected = "cost"
    elif mutation == "cost_literal":
        forged["cost_preflight"]["cheap_full"]["upper_bound_usd"] = "0.70000000"
        expected = "cost"
    elif mutation == "status":
        forged["status"] = "PASS"
        expected = "status|blocker"
    elif mutation == "promotion":
        forged["eligibility"]["empirical"] = True
        expected = "eligib|promotion"
    elif mutation == "source_hash":
        forged["source_hashes"]["public_bank"] = "0" * 64
        expected = "source.*hash"
    else:
        forged["provenance_hashes"]["audits/run_all.py"] = "0" * 64
        expected = "provenance|code.*hash"
    with pytest.raises(ValueError, match=expected):
        validate_audit_result(forged)


def test_bundle_validator_rejects_output_hash_forgery(bundle):
    forged = dict(bundle)
    manifest = json.loads(forged["manifest.json"])
    manifest["outputs"]["report.md"]["sha256"] = "0" * 64
    forged["manifest.json"] = (
        json.dumps(manifest, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")
    with pytest.raises(ValueError, match="output.*hash|manifest"):
        validate_audit_bundle(forged)


def test_bundle_validator_rejects_config_provenance_hash_forgery(bundle):
    forged = dict(bundle)
    manifest = json.loads(forged["manifest.json"])
    manifest["provenance"]["audits/config/openrouter-cheap-roster.json"] = "0" * 64
    forged["manifest.json"] = (
        json.dumps(manifest, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")
    with pytest.raises(ValueError, match="provenance|config.*hash|manifest"):
        validate_audit_bundle(forged)


def test_frozen_bundle_and_two_cli_runs_are_byte_identical(bundle, tmp_path):
    assert {path.name for path in FROZEN_OUTPUT_DIR.iterdir()} == set(bundle)
    assert {
        path.name: path.read_bytes() for path in FROZEN_OUTPUT_DIR.iterdir()
    } == bundle

    script = Path(__file__).resolve().parents[1] / "audits" / "run_all.py"
    output_dir = tmp_path / "aggregate"
    command = [sys.executable, str(script), "--output-dir", str(output_dir)]
    first = subprocess.run(command, capture_output=True, text=True, check=False)
    assert first.returncode == 0, first.stderr
    first_bytes = {path.name: path.read_bytes() for path in output_dir.iterdir()}
    second = subprocess.run(command, capture_output=True, text=True, check=False)
    assert second.returncode == 0, second.stderr
    second_bytes = {path.name: path.read_bytes() for path in output_dir.iterdir()}
    assert set(first_bytes) == {"audit-result.json", "report.md", "manifest.json"}
    assert first_bytes == second_bytes == bundle
