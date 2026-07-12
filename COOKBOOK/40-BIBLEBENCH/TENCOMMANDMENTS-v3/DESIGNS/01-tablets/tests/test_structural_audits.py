from copy import deepcopy
import json
from pathlib import Path

import pytest

import tablets_constants as constants
from audits.leakage import audit_leakage
from audits.linkage_crux import audit_linkage_crux
from audits.mechanical_replay import audit_mechanical_replay
from audits.schema_balance import audit_schema_balance
from itembank.generator import build_rows
from tablets_hashing import canonical_json


ROOT = Path(__file__).resolve().parents[1]
_ARTIFACT_PATHS = {
    "public": Path("itembank/bank/p1-public.jsonl"),
    "private": Path("itembank/gold/p1-private.gold.jsonl"),
    "runtime": Path("itembank/runtime/p1-runtime-manifest.jsonl"),
    "manifest": Path("itembank/manifest.json"),
}


def _disk_artifacts(root=ROOT):
    return {
        name: (root / relative).read_bytes()
        for name, relative in _ARTIFACT_PATHS.items()
    }


def _replace_jsonl_row(artifacts, name, row_index, mutate):
    changed = dict(artifacts)
    rows = [json.loads(line) for line in changed[name].decode("utf-8").splitlines()]
    mutate(rows[row_index])
    changed[name] = (
        "\n".join(canonical_json(row) for row in rows) + "\n"
    ).encode("utf-8")
    return changed


def _copy_artifacts(root):
    for name, relative in _ARTIFACT_PATHS.items():
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((ROOT / relative).read_bytes())


def test_schema_balance_reads_disk_and_freezes_exact_counts_and_hashes():
    first = audit_schema_balance()
    second = audit_schema_balance()

    assert first == second
    assert first["status"] == "PASS"
    assert first["source"] == "DISK"
    assert first["sections"]["schema"]["strict_validation"] is True
    assert first["sections"]["artifacts"]["deterministic_byte_equality"] is True
    assert first["sections"]["artifacts"]["sha256"] == {
        "manifest": "ec3a41aa0e786af65c3e520bd770dc2d021e738d656889ec0fc0420ad6706ce8",
        "private": "597aeb5a5c4f4c07095068663134e59cd6a90b9d6dee56faef778e3a418cb7ef",
        "public": "5c60194de2a1fd57276af83706bd8ff536749ee5039611711de7e5da61b44b4d",
        "runtime": "537c2dcd57b75966880ff47696a414ab74229b654864d7f139abb255d0967d5f",
    }
    balance = first["sections"]["balance"]
    assert balance["record_count"] == 636
    assert balance["record_type_counts"] == {
        "adjudication": 342,
        "comprehension": 45,
        "monitoring_twin": 69,
        "recognition": 45,
        "threat_twin": 135,
    }
    assert balance["severity_tier_counts"] == {
        "T1": 320,
        "T2": 44,
        "T3": 43,
        "T4": 229,
    }
    assert balance["direction_counts"] == {"A_FIRST": 320, "B_FIRST": 316}
    assert balance["framing_counts"] == {"neutral": 501, "threat": 135}
    assert balance["monitoring_counts"] == {"monitored": 69, "unmonitored": 567}


def test_schema_balance_rejects_tampered_disk_bytes(tmp_path):
    root = tmp_path / "tablets"
    _copy_artifacts(root)
    public_path = root / _ARTIFACT_PATHS["public"]
    public_path.write_bytes(public_path.read_bytes() + b" ")

    with pytest.raises(ValueError, match="deterministic byte drift|hash"):
        audit_schema_balance(tablets_root=root)


def test_schema_balance_rejects_injected_runtime_source_hash_forgery():
    forged = _replace_jsonl_row(
        _disk_artifacts(),
        "runtime",
        0,
        lambda row: row.__setitem__("source_public_record_sha256", "0" * 64),
    )
    with pytest.raises(ValueError, match="deterministic byte drift|source|binding"):
        audit_schema_balance(artifact_bytes=forged)


def test_leakage_audit_recursively_scans_disk_public_and_runtime():
    first = audit_leakage()
    second = audit_leakage()

    assert first == second
    assert first["status"] == "PASS"
    assert first["source"] == "DISK"
    assert first["sections"] == {
        "public": {
            "status": "PASS",
            "records_scanned": 636,
            "forbidden_field_hits": [],
        },
        "runtime": {
            "status": "PASS",
            "records_scanned": 636,
            "forbidden_field_hits": [],
        },
    }


@pytest.mark.parametrize(
    "forbidden_field",
    (
        "choice_map",
        "authoring_gold_band",
        "gold_label",
        "panel_evidence",
        "expected_answer",
        "action_map",
    ),
)
def test_leakage_audit_rejects_nested_private_or_answer_fields(forbidden_field):
    forged = _replace_jsonl_row(
        _disk_artifacts(),
        "runtime",
        0,
        lambda row: row["response_schema"].setdefault("audit_metadata", {}).update(
            {forbidden_field: {"fixture": True}}
        ),
    )
    with pytest.raises(ValueError, match="private-field leakage|forbidden.*field"):
        audit_leakage(artifact_bytes=forged)


@pytest.mark.parametrize(
    "forbidden_field",
    (
        "Choice_Map",
        "EXPECTED_DUTY_CODES",
        "AuThOrInG_GoLd_BaNd",
        "PaNeL_EvIdEnCe",
        "AcTiOn_MaP",
    ),
)
def test_leakage_audit_rejects_case_variant_nested_private_fields(forbidden_field):
    forged = _replace_jsonl_row(
        _disk_artifacts(),
        "runtime",
        0,
        lambda row: row["response_schema"].setdefault("audit_metadata", {}).update(
            {forbidden_field: {"fixture": True}}
        ),
    )
    with pytest.raises(ValueError, match="private-field leakage|forbidden.*field"):
        audit_leakage(artifact_bytes=forged)


def test_leakage_audit_allows_nested_public_pair_and_commandment_metadata():
    allowed = _replace_jsonl_row(
        _disk_artifacts(),
        "runtime",
        0,
        lambda row: row["response_schema"].setdefault("audit_metadata", {}).update(
            {"pair": "1x2", "commandment": [1, 2]}
        ),
    )
    report = audit_leakage(artifact_bytes=allowed)
    assert report["status"] == "PASS"
    assert report["source"] == "INJECTED_BYTES"


def test_linkage_audit_replays_all_treatments_and_keeps_crux_unavailable_fail_closed():
    first = audit_linkage_crux()
    second = audit_linkage_crux()

    assert first == second
    assert first["status"] == "PASS"
    assert first["source"] == "DISK"
    assert first["sections"]["parent_graph"] == {
        "status": "PASS",
        "parent_rows": 342,
        "child_rows": 294,
        "reciprocal_links": 294,
    }
    assert first["sections"]["treatment_replay"] == {
        "status": "PASS",
        "threat_twin": 135,
        "monitoring_twin": 69,
        "comprehension": 45,
        "recognition": 45,
        "gs_x3_parent_sets_disjoint": True,
    }
    crux = first["sections"]["crux_boundary"]
    assert crux["status"] == "PASS"
    assert crux["source_memo_sha256"] == (
        "ac591d17dbd18935e32f3c80ef011d0a1418e875ceb5f35c80cee194e3ff66d7"
    )
    assert crux["cross_bank_seed_triad_audit_status"] == (
        "NOT_RUN_CRUX_BANK_UNAVAILABLE"
    )
    assert crux["cross_bank_seed_triad_audit_status"] != "PASS"


def test_linkage_audit_rejects_reciprocal_but_semantically_wrong_rewire():
    public, _, _ = build_rows()
    forged = deepcopy(public)
    by_id = {row["id"]: row for row in forged}
    twin = next(row for row in forged if row["record_type"] == "threat_twin")
    old_parent = by_id[twin["parent_id"]]
    wrong_parent = next(
        row
        for row in forged
        if row["record_type"] == "adjudication" and row["id"] != old_parent["id"]
    )
    old_parent["paired_record_ids"].remove(twin["id"])
    wrong_parent["paired_record_ids"].append(twin["id"])
    twin["parent_id"] = wrong_parent["id"]
    twin["paired_record_ids"] = [wrong_parent["id"]]

    with pytest.raises(ValueError, match="treatment|rewire|frozen"):
        audit_linkage_crux(public_rows=forged)


def test_linkage_audit_rejects_coupled_parent_and_threat_mutation():
    public, _, _ = build_rows()
    forged = deepcopy(public)
    by_id = {row["id"]: row for row in forged}
    twin = next(row for row in forged if row["record_type"] == "threat_twin")
    parent = by_id[twin["parent_id"]]
    parent["prompt"] += "\nCOUPLED FORGED STYLE MARKER"
    twin["prompt"] = parent["prompt"] + constants.THREAT_NOTICE

    with pytest.raises(ValueError, match="parent|treatment|frozen"):
        audit_linkage_crux(public_rows=forged)


@pytest.mark.parametrize(
    "record_type",
    ("threat_twin", "monitoring_twin", "comprehension", "recognition"),
)
def test_linkage_audit_rejects_treatment_drift_for_every_child_kind(record_type):
    public, _, _ = build_rows()
    forged = deepcopy(public)
    child = next(row for row in forged if row["record_type"] == record_type)
    child["prompt"] += "\nFORGED TREATMENT DRIFT"

    with pytest.raises(ValueError, match="treatment|frozen|suffix"):
        audit_linkage_crux(public_rows=forged)


def test_linkage_audit_rejects_crux_memo_hash_or_boundary_substitution():
    linkage = json.loads((ROOT / "crux-coregistration-linkage.json").read_text())
    forged_hash = deepcopy(linkage)
    forged_hash["source_memo_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="CRUX|memo|hash"):
        audit_linkage_crux(linkage=forged_hash)

    forged_boundary = deepcopy(linkage)
    forged_boundary["objects_in_conflict"] = "generic stakeholder values"
    with pytest.raises(ValueError, match="CRUX|boundary|frozen"):
        audit_linkage_crux(linkage=forged_boundary)


def test_mechanical_audit_replays_every_outcome_control_and_fail_closed_probe():
    first = audit_mechanical_replay()
    second = audit_mechanical_replay()

    assert first == second
    assert first["status"] == "PASS"
    assert first["source"] == "DISK"
    assert first["sections"]["valid_replay"] == {
        "status": "PASS",
        "duty_a": 591,
        "duty_b": 591,
        "paralysis": 591,
        "third_way": 16,
        "comprehension_correct": 45,
        "comprehension_valid_incorrect": 45,
        "recognition_correct": 45,
        "recognition_valid_incorrect": 45,
    }
    assert first["sections"]["evidence_guards"] == {
        "status": "PASS",
        "panel_not_run_rows": 636,
        "c10_excluded_rows": 116,
    }
    mutations = first["sections"]["mutation_rejections"]
    assert mutations["status"] == "PASS"
    assert mutations["rejection_count"] == 4
    assert all(
        mutations[name]
        for name in (
            "extra_response_field",
            "unknown_action",
            "forged_private_semantics",
            "unknown_duty_code",
        )
    )


def test_mechanical_audit_rejects_injected_private_semantic_forgery():
    public, private, _ = build_rows()
    forged = deepcopy(private)
    row = next(item for item in forged if item["choice_map"])
    action_id = next(iter(row["choice_map"]))
    row["choice_map"][action_id]["outcome_class"] = "paralysis"
    row["choice_map"][action_id]["served_commandment"] = None

    with pytest.raises(ValueError, match="private|semantic|replay|binding"):
        audit_mechanical_replay(public_rows=public, private_rows=forged)
