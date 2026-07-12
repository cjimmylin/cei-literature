"""Build and validate the frozen credential-free TABLETS audit bundle."""

import argparse
from copy import deepcopy
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import sys


TABLETS_ROOT = Path(__file__).resolve().parents[1]
if str(TABLETS_ROOT) not in sys.path:
    sys.path.insert(0, str(TABLETS_ROOT))

from audits.leakage import audit_leakage
from audits.lexical_length import audit_lexical_length
from audits.linkage_crux import audit_linkage_crux
from audits.mechanical_replay import audit_mechanical_replay
from audits.schema_balance import audit_schema_balance
from calibration.status import load_evidence_status


RUN_ID = "20260711-credential-free-r1"
FROZEN_OUTPUT_DIR = TABLETS_ROOT / "audits" / "reports" / RUN_ID
COST_CONFIG_PATH = TABLETS_ROOT / "audits" / "config" / "openrouter-cheap-roster.json"
_SOURCE_SPECS = {
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
_PROVENANCE_PATHS = {
    "audits/__init__.py": TABLETS_ROOT / "audits" / "__init__.py",
    "audits/schema_balance.py": TABLETS_ROOT / "audits" / "schema_balance.py",
    "audits/leakage.py": TABLETS_ROOT / "audits" / "leakage.py",
    "audits/linkage_crux.py": TABLETS_ROOT / "audits" / "linkage_crux.py",
    "audits/mechanical_replay.py": TABLETS_ROOT / "audits" / "mechanical_replay.py",
    "audits/lexical_length.py": TABLETS_ROOT / "audits" / "lexical_length.py",
    "audits/run_all.py": TABLETS_ROOT / "audits" / "run_all.py",
    "audits/config/openrouter-cheap-roster.json": COST_CONFIG_PATH,
    "calibration/status.py": TABLETS_ROOT / "calibration" / "status.py",
    "analysis/power.py": TABLETS_ROOT / "analysis" / "power.py",
    "scoring/mechanical.py": TABLETS_ROOT / "scoring" / "mechanical.py",
    "itembank/generator.py": TABLETS_ROOT / "itembank" / "generator.py",
    "itembank/build_bank.py": TABLETS_ROOT / "itembank" / "build_bank.py",
    "tablets_schemas.py": TABLETS_ROOT / "tablets_schemas.py",
    "tablets_constants.py": TABLETS_ROOT / "tablets_constants.py",
    "tablets_hashing.py": TABLETS_ROOT / "tablets_hashing.py",
    "preregistration.md": TABLETS_ROOT / "preregistration.md",
    "crux-coregistration-linkage.json": TABLETS_ROOT
    / "crux-coregistration-linkage.json",
    "TENCOMMANDMENTS-REVIEWS/20260706-tablets-crux-coregistration.md": (
        TABLETS_ROOT.parents[2]
        / "TENCOMMANDMENTS-REVIEWS"
        / "20260706-tablets-crux-coregistration.md"
    ),
}


def _expected_cost_config():
    return {
        "schema_version": "tablets-openrouter-cost.v1",
        "max_prompt_tokens": 8192,
        "max_tokens": 1536,
        "syntax_repairs_per_request": 1,
        "provider_policy": {
            "allow_fallbacks": False,
            "require_parameters": True,
        },
        "roster_basis": {
            "path": "TENCOMMANDMENTS-v2/DESIGNS/08-skim/configs/openrouter-cheap-engineering-smoke-r2.json",
            "sha256": "5cf79207e29a38b2465c524f272e4cf8b97600267b46b2479373ca363f215597",
        },
        "routes": [
            {
                "canonical_model_id": "inclusionai/ling-2.6-flash",
                "completion_price_per_token_usd": "0.00000003",
                "endpoint_name": "Novita | inclusionai/ling-2.6-flash-20260421",
                "prompt_price_per_token_usd": "0.00000001",
                "provider": "Novita",
            },
            {
                "canonical_model_id": "meta-llama/llama-3.1-8b-instruct",
                "completion_price_per_token_usd": "0.00000003",
                "endpoint_name": "DeepInfra | meta-llama/llama-3.1-8b-instruct",
                "prompt_price_per_token_usd": "0.00000002",
                "provider": "DeepInfra",
            },
            {
                "canonical_model_id": "mistralai/mistral-nemo",
                "completion_price_per_token_usd": "0.00000004",
                "endpoint_name": "DeepInfra | mistralai/mistral-nemo",
                "prompt_price_per_token_usd": "0.00000002",
                "provider": "DeepInfra",
            },
        ],
        "phases": {
            "smoke": {
                "initial_calls_per_route": 6,
                "cap_usd": "0.01",
                "authorization_status": "CHEAP_TEST_AUTHORIZED",
            },
            "cheap_full": {
                "initial_calls_per_route": 636,
                "cap_usd": "1.00",
                "authorization_status": "CHEAP_TEST_AUTHORIZED",
            },
            "official": {
                "initial_calls_per_route": 1908,
                "cap_usd": "3.00",
                "authorization_status": "PREVIEW_ONLY_UNAUTHORIZED",
            },
        },
    }


def validate_cost_config(config):
    """Reject any roster, price, call, repair, cap, or fallback drift."""
    if type(config) is not dict or config != _expected_cost_config():
        raise ValueError("OpenRouter cost config differs from the frozen roster contract")
    return True


def load_cost_config(path=COST_CONFIG_PATH):
    """Load the canonical cost config and require deterministic JSON bytes."""
    path = Path(path)
    payload = path.read_bytes()
    try:
        config = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("OpenRouter cost config is invalid JSON") from error
    validate_cost_config(config)
    if payload != _canonical_json_bytes(config):
        raise ValueError("OpenRouter cost config has deterministic byte drift")
    return config


def derive_cost_preflight(config):
    """Derive all request counts and upper bounds using exact Decimal math."""
    validate_cost_config(config)
    try:
        per_route_costs = [
            Decimal(config["max_prompt_tokens"])
            * Decimal(route["prompt_price_per_token_usd"])
            + Decimal(config["max_tokens"])
            * Decimal(route["completion_price_per_token_usd"])
            for route in config["routes"]
        ]
    except (InvalidOperation, TypeError, ValueError) as error:
        raise ValueError("OpenRouter cost config price is invalid") from error
    paid_multiplier = 1 + config["syntax_repairs_per_request"]
    quantization = Decimal("0.00000001")
    result = {}
    for name in ("smoke", "cheap_full", "official"):
        phase = config["phases"][name]
        per_route_calls = phase["initial_calls_per_route"]
        initial_requests = per_route_calls * len(config["routes"])
        paid_calls = initial_requests * paid_multiplier
        upper_bound = (
            Decimal(per_route_calls)
            * Decimal(paid_multiplier)
            * sum(per_route_costs, Decimal("0"))
        ).quantize(quantization)
        if upper_bound > Decimal(phase["cap_usd"]):
            raise ValueError("OpenRouter derived upper bound exceeds frozen cap")
        result[name] = {
            "initial_requests": initial_requests,
            "paid_calls": paid_calls,
            "upper_bound_usd": format(upper_bound, "f"),
            "cap_usd": phase["cap_usd"],
            "authorization_status": phase["authorization_status"],
        }
    return result


def _provenance_hashes():
    return {
        name: hashlib.sha256(path.read_bytes()).hexdigest()
        for name, path in sorted(_PROVENANCE_PATHS.items())
    }


def derive_aggregate_status(hard_statuses, lexical_status, has_empirical_blockers):
    """Apply the frozen FAIL > REWORK > blocker-aware completion ordering."""
    if type(hard_statuses) is not list or not hard_statuses:
        raise ValueError("aggregate hard statuses must be a nonempty list")
    if any(status != "PASS" for status in hard_statuses):
        return "FAIL"
    if lexical_status != "PASS":
        return "REWORK"
    if has_empirical_blockers:
        return "COMPLETE_WITH_EMPIRICAL_BLOCKERS"
    return "PASS"


def _source_hashes():
    hashes = {}
    for name, spec in _SOURCE_SPECS.items():
        payload = (TABLETS_ROOT / spec["path"]).read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        if digest != spec["sha256"]:
            raise ValueError("aggregate source hash drift: %s" % name)
        hashes[name] = digest
    return hashes


def _power_status():
    path = TABLETS_ROOT / _SOURCE_SPECS["power_report"]["path"]
    try:
        report = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("frozen power report is invalid") from error
    if (
        report.get("evidence_eligibility") != "PRE_RUN_ONLY"
        or report.get("empirical_status") != "NOT_EMPIRICAL"
        or report.get("simulations") != 10_000
        or report.get("seed") != 20_260_711
    ):
        raise ValueError("frozen power report status drift")
    claims = report.get("claims")
    if type(claims) is not list or len(claims) != 5:
        raise ValueError("frozen power report claim drift")
    return {row["claim"]: row["claim_status"] for row in claims}


def _evidence_summary():
    status = load_evidence_status()
    return {
        "overall_status": status["overall_status"],
        **{
            name: entry["status"]
            for name, entry in status["evidence"].items()
        },
    }


def _blockers(evidence, power, crux_status):
    blockers = [
        {"blocker": name, "status": status}
        for name, status in evidence.items()
        if name != "overall_status" and status != "PASS"
    ]
    blockers.extend(
        {"blocker": "power.%s" % name, "status": status}
        for name, status in power.items()
        if status != "POWER_ADEQUATE_PRE_RUN"
    )
    blockers.append(
        {
            "blocker": "crux_cross_bank_seed_triad_audit",
            "status": crux_status,
        }
    )
    return blockers


def _build_audit_result():
    source_hashes = _source_hashes()
    cost_preflight = derive_cost_preflight(load_cost_config())
    provenance_hashes = _provenance_hashes()
    audits = {
        "schema_balance": audit_schema_balance(),
        "leakage": audit_leakage(),
        "linkage_crux": audit_linkage_crux(),
        "mechanical_replay": audit_mechanical_replay(),
        "lexical_length": audit_lexical_length(),
    }
    evidence = _evidence_summary()
    power = _power_status()
    crux_status = audits["linkage_crux"]["sections"]["crux_boundary"][
        "cross_bank_seed_triad_audit_status"
    ]
    blockers = _blockers(evidence, power, crux_status)
    hard_statuses = [
        audits[name]["status"]
        for name in (
            "schema_balance",
            "leakage",
            "linkage_crux",
            "mechanical_replay",
        )
    ]
    status = derive_aggregate_status(
        hard_statuses,
        audits["lexical_length"]["status"],
        bool(blockers),
    )
    return {
        "audit": "TABLETS_CREDENTIAL_FREE_AGGREGATE",
        "schema_version": "tablets-audit-aggregate.v1",
        "run_id": RUN_ID,
        "status": status,
        "evidence_eligibility": "CREDENTIAL_FREE_ENGINEERING_ONLY",
        "eligibility": {
            "empirical": False,
            "official": False,
            "publication": False,
        },
        "judge_calls": 0,
        "audits": audits,
        "evidence_status": evidence,
        "power_status": power,
        "cross_bank_seed_triad_audit_status": crux_status,
        "empirical_blockers": blockers,
        "cost_preflight": cost_preflight,
        "source_hashes": source_hashes,
        "provenance_hashes": provenance_hashes,
    }


def _validate_result_structure(result):
    if type(result) is not dict:
        raise ValueError("aggregate result must be an object")
    if result.get("run_id") != RUN_ID:
        raise ValueError("aggregate run ID drift")
    if result.get("evidence_eligibility") != "CREDENTIAL_FREE_ENGINEERING_ONLY":
        raise ValueError("aggregate evidence eligibility promotion forbidden")
    if result.get("eligibility") != {
        "empirical": False,
        "official": False,
        "publication": False,
    }:
        raise ValueError("aggregate eligibility promotion forbidden")
    if result.get("judge_calls") != 0:
        raise ValueError("aggregate judge calls must remain zero")
    expected_cost = derive_cost_preflight(load_cost_config())
    if result.get("cost_preflight") != expected_cost:
        raise ValueError("aggregate cost preflight drift")
    expected_hashes = {
        name: spec["sha256"] for name, spec in _SOURCE_SPECS.items()
    }
    if result.get("source_hashes") != expected_hashes:
        raise ValueError("aggregate source hash drift")
    if result.get("provenance_hashes") != _provenance_hashes():
        raise ValueError("aggregate executable provenance or code hash drift")
    audits = result.get("audits")
    if type(audits) is not dict or set(audits) != {
        "schema_balance",
        "leakage",
        "linkage_crux",
        "mechanical_replay",
        "lexical_length",
    }:
        raise ValueError("aggregate audit section drift")
    evidence = result.get("evidence_status")
    power = result.get("power_status")
    if type(evidence) is not dict or type(power) is not dict:
        raise ValueError("aggregate blocker status drift")
    if evidence.get("overall_status") != "NOT_RUN":
        raise ValueError("aggregate empirical blocker promotion forbidden")
    for name in (
        "casuistry_panel",
        "edge_judge",
        "human_baseline",
        "professional_baseline",
        "contested_distribution",
        "real_10pct_finetune_probe",
        "official_multiseed_model_run",
    ):
        if evidence.get(name) != "NOT_RUN":
            raise ValueError("aggregate empirical blocker promotion forbidden")
    crux_status = result.get("cross_bank_seed_triad_audit_status")
    if crux_status != "NOT_RUN_CRUX_BANK_UNAVAILABLE":
        raise ValueError("aggregate CRUX cross-bank status promotion forbidden")
    if power.get("triad_coherence") != "NOT_ESTIMABLE_UNTIL_WIN_MARGINS":
        raise ValueError("aggregate conditional triad power promotion forbidden")
    hard_statuses = [
        audits[name].get("status")
        for name in (
            "schema_balance",
            "leakage",
            "linkage_crux",
            "mechanical_replay",
        )
    ]
    expected_status = derive_aggregate_status(
        hard_statuses,
        audits["lexical_length"].get("status"),
        bool(result.get("empirical_blockers")),
    )
    if result.get("status") != expected_status:
        raise ValueError("aggregate status contradicts hard/style/blocker status")
    if result["cost_preflight"]["official"]["authorization_status"] != (
        "PREVIEW_ONLY_UNAUTHORIZED"
    ):
        raise ValueError("official preflight authorization promotion forbidden")
    return True


def validate_audit_result(result):
    """Strictly recompute and reject any aggregate substitution."""
    _validate_result_structure(result)
    if result != _build_audit_result():
        raise ValueError("aggregate deterministic recomputation mismatch")
    return True


def _canonical_json_bytes(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode("utf-8")


def _markdown(result):
    lines = [
        "# TABLETS credential-free audit report",
        "",
        "- Run: `%s`" % result["run_id"],
        "- Status: `%s`" % result["status"],
        "- Evidence eligibility: `%s`" % result["evidence_eligibility"],
        "- Judge calls: `%d`" % result["judge_calls"],
        "",
        "## Engineering audits",
        "",
        "| Section | Status |",
        "|---|---|",
    ]
    for name in (
        "schema_balance",
        "leakage",
        "linkage_crux",
        "mechanical_replay",
        "lexical_length",
    ):
        lines.append("| %s | %s |" % (name, result["audits"][name]["status"]))
    lines.extend(
        [
            "",
            "## Cost preflight",
            "",
            "| Phase | Initial requests | Paid calls | Upper bound | Cap | Authorization |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for name in ("smoke", "cheap_full", "official"):
        row = result["cost_preflight"][name]
        lines.append(
            "| %s | %d | %d | $%s | $%s | %s |"
            % (
                name,
                row["initial_requests"],
                row["paid_calls"],
                row["upper_bound_usd"],
                row["cap_usd"],
                row["authorization_status"],
            )
        )
    lines.extend(["", "## Empirical blockers", ""])
    for blocker in result["empirical_blockers"]:
        lines.append(
            "- `%s`: `%s`" % (blocker["blocker"], blocker["status"])
        )
    lines.extend(
        [
            "",
            "This bundle is credential-free engineering evidence only. It is not "
            "eligible for empirical, official, or publication claims.",
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def _manifest(result_bytes, report_bytes):
    return {
        "schema_version": "tablets-audit-manifest.v1",
        "run_id": RUN_ID,
        "outputs": {
            "audit-result.json": {
                "bytes": len(result_bytes),
                "sha256": hashlib.sha256(result_bytes).hexdigest(),
            },
            "report.md": {
                "bytes": len(report_bytes),
                "sha256": hashlib.sha256(report_bytes).hexdigest(),
            },
        },
        "sources": deepcopy(_SOURCE_SPECS),
        "provenance": _provenance_hashes(),
    }


def build_audit_bundle():
    """Build the exact three-file aggregate bundle in memory."""
    result = _build_audit_result()
    _validate_result_structure(result)
    result_bytes = _canonical_json_bytes(result)
    report_bytes = _markdown(result)
    manifest_bytes = _canonical_json_bytes(_manifest(result_bytes, report_bytes))
    return {
        "audit-result.json": result_bytes,
        "report.md": report_bytes,
        "manifest.json": manifest_bytes,
    }


def validate_audit_bundle(bundle):
    """Recompute result/report/manifest and reject byte or hash forgery."""
    if type(bundle) is not dict or set(bundle) != {
        "audit-result.json",
        "report.md",
        "manifest.json",
    }:
        raise ValueError("aggregate bundle must contain exactly three files")
    if not all(type(payload) is bytes for payload in bundle.values()):
        raise ValueError("aggregate bundle values must be bytes")
    try:
        result = json.loads(bundle["audit-result.json"].decode("utf-8"))
        manifest = json.loads(bundle["manifest.json"].decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("aggregate bundle JSON is invalid") from error
    validate_audit_result(result)
    expected_result = _canonical_json_bytes(result)
    expected_report = _markdown(result)
    expected_manifest = _canonical_json_bytes(
        _manifest(expected_result, expected_report)
    )
    if bundle["audit-result.json"] != expected_result:
        raise ValueError("aggregate result bytes are not deterministic")
    if bundle["report.md"] != expected_report:
        raise ValueError("aggregate report bytes are not deterministic")
    if bundle["manifest.json"] != expected_manifest or manifest != json.loads(
        expected_manifest
    ):
        raise ValueError("aggregate manifest output hash mismatch")
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=FROZEN_OUTPUT_DIR)
    args = parser.parse_args(argv)
    bundle = build_audit_bundle()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    existing = {path.name for path in args.output_dir.iterdir()}
    unexpected = existing - set(bundle)
    if unexpected:
        raise SystemExit("aggregate output directory contains unexpected entries")
    for filename in ("audit-result.json", "report.md", "manifest.json"):
        (args.output_dir / filename).write_bytes(bundle[filename])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "COST_CONFIG_PATH",
    "FROZEN_OUTPUT_DIR",
    "RUN_ID",
    "build_audit_bundle",
    "derive_cost_preflight",
    "derive_aggregate_status",
    "load_cost_config",
    "validate_audit_bundle",
    "validate_audit_result",
    "validate_cost_config",
]
