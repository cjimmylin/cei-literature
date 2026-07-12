from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys

import pytest

import tablets_constants as constants
from tablets_hashing import canonical_json, canonical_sha256, sha256_file
from tablets_schemas import (
    PRIVATE_ONLY_FIELDS,
    validate_private_row,
    validate_public_row,
    validate_runtime_row,
)
from itembank.build_bank import build_artifact_bytes, validate_artifact_bytes
from itembank.generator import build_private_row, build_rows, build_runtime_row


ROOT = Path(__file__).resolve().parents[1]


def _recursive_keys(value):
    if isinstance(value, dict):
        keys = set(value)
        for child in value.values():
            keys.update(_recursive_keys(child))
        return keys
    if isinstance(value, list):
        keys = set()
        for child in value:
            keys.update(_recursive_keys(child))
        return keys
    return set()


def _mutate_jsonl_artifact(artifacts, name, row_index, mutate, rebind_manifest=False):
    changed = dict(artifacts)
    rows = [json.loads(line) for line in artifacts[name].decode("utf-8").splitlines()]
    mutate(rows[row_index])
    changed[name] = ("\n".join(canonical_json(row) for row in rows) + "\n").encode("utf-8")
    if rebind_manifest:
        manifest = json.loads(changed["manifest"])
        manifest["artifacts"][name]["sha256"] = canonical_sha256(
            changed[name], raw_bytes=True
        )
        manifest["artifacts"][name]["bytes"] = len(changed[name])
        changed["manifest"] = (canonical_json(manifest) + "\n").encode("utf-8")
    return changed


def _rebuild_artifacts_from_public(artifacts, public_rows):
    changed = dict(artifacts)
    projections = {
        "public": public_rows,
        "private": [build_private_row(row) for row in public_rows],
        "runtime": [build_runtime_row(row) for row in public_rows],
    }
    manifest = json.loads(artifacts["manifest"])
    for name, rows in projections.items():
        changed[name] = (
            "\n".join(canonical_json(row) for row in rows) + "\n"
        ).encode("utf-8")
        manifest["artifacts"][name]["sha256"] = canonical_sha256(
            changed[name], raw_bytes=True
        )
        manifest["artifacts"][name]["bytes"] = len(changed[name])
    changed["manifest"] = (canonical_json(manifest) + "\n").encode("utf-8")
    return changed


def test_frozen_contract_has_corrected_exact_schedule():
    assert len(constants.COMMANDMENTS) == 10
    assert len(constants.PAIRS) == 45
    assert len(constants.PRIORITY_PAIRS) == 12
    assert constants.BASE_SEVERITY_TIERS == ("T1", "T4")
    assert constants.PRIORITY_SEVERITY_TIERS == ("T2", "T3")
    assert constants.BASE_GRID_COUNT == 270
    assert constants.PRIORITY_LADDER_COUNT == 72
    assert constants.NEUTRAL_PRIMARY_COUNT == 342
    assert constants.THREAT_TWIN_COUNT == 135
    assert constants.COMPREHENSION_COUNT == 45
    assert constants.CONSTRUCTION_COUNT == 522
    assert constants.RECOGNITION_COUNT == 45
    assert constants.MONITORING_TWIN_COUNT == 69
    assert constants.PUBLIC_RECORD_COUNT == 636
    assert constants.PRIVATE_RECORD_COUNT == 636
    assert constants.RUNTIME_RECORD_COUNT == 636
    assert constants.RECORD_TYPE_COUNTS == {
        "adjudication": 342,
        "threat_twin": 135,
        "comprehension": 45,
        "recognition": 45,
        "monitoring_twin": 69,
    }
    assert constants.MONITORING_TWIN_COUNT / constants.NEUTRAL_PRIMARY_COUNT >= 0.20
    assert (constants.MONITORING_TWIN_COUNT - 1) / constants.NEUTRAL_PRIMARY_COUNT < 0.20


def test_bank_builder_is_a_directly_executable_entry_point():
    completed = subprocess.run(
        [sys.executable, str(ROOT / "itembank" / "build_bank.py"), "--help"],
        cwd=str(ROOT.parents[2]),
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert "Build and verify" in completed.stdout


def test_preregistration_discloses_corrected_denominator_and_evidence_gates():
    prereg = (ROOT / "preregistration.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for required in (
        "636",
        "342 neutral primary",
        "69 additive matched monitored",
        "135 threat",
        "within severity tier",
        "tier-by-pair",
        "marginal-preserving permutation",
        "C10",
        "NOT_RUN",
        "panel-certified",
        "CRUX",
    ):
        assert required in prereg
    for required in ("636", "69", "NOT_RUN", "must not", "CRUX"):
        assert required in readme
    assert "OpenRouter" not in readme


def test_crux_linkage_freezes_boundary_and_binds_source_memo():
    linkage = json.loads((ROOT / "crux-coregistration-linkage.json").read_text())
    source = ROOT.parents[2] / "TENCOMMANDMENTS-REVIEWS" / linkage["source_memo"]
    assert linkage["status"] == "BINDING"
    assert linkage["instrument"] == "TABLETS"
    assert linkage["objects_in_conflict"] == "two named Decalogue norms on one actor"
    assert linkage["gold_source_tiebreaker"] == "casuistic-precedence gold"
    assert linkage["seed_sharing_forbidden"] is True
    assert linkage["cross_instrument_triads_forbidden"] is True
    assert linkage["source_memo_sha256"] == sha256_file(source)


def test_generator_builds_exact_deterministic_balanced_projections():
    first = build_rows()
    second = build_rows()
    assert canonical_json(first) == canonical_json(second)
    public, private, runtime = first
    assert (len(public), len(private), len(runtime)) == (636, 636, 636)
    assert Counter(row["record_type"] for row in public) == constants.RECORD_TYPE_COUNTS

    primary = [row for row in public if row["record_type"] == "adjudication"]
    assert Counter(row["severity_tier"] for row in primary) == {
        "T1": 135,
        "T4": 135,
        "T2": 36,
        "T3": 36,
    }
    assert Counter(row["pair"] for row in primary) == {
        pair: 12 if pair in constants.PRIORITY_PAIRS else 6
        for pair in constants.PAIRS
    }
    assert Counter(row["direction_permutation"] for row in primary) == {
        "A_FIRST": 171,
        "B_FIRST": 171,
    }
    threat = [row for row in public if row["record_type"] == "threat_twin"]
    assert Counter(row["pair"] for row in threat) == {pair: 3 for pair in constants.PAIRS}
    threat_tiers = Counter(row["severity_tier"] for row in threat)
    assert set(threat_tiers) == {"T1", "T4"}
    assert abs(threat_tiers["T1"] - threat_tiers["T4"]) <= 1

    public_ids = [row["id"] for row in public]
    assert len(set(public_ids)) == 636
    assert public_ids == [row["id"] for row in private]
    assert public_ids == [row["source_record_id"] for row in runtime]
    for pub, gold, request in zip(public, private, runtime):
        assert validate_public_row(pub) is True
        assert validate_private_row(gold) is True
        assert validate_runtime_row(request) is True
        assert gold["public_record_sha256"] == canonical_sha256(pub)
        assert request["source_public_record_sha256"] == canonical_sha256(pub)
        assert _recursive_keys(pub).isdisjoint(PRIVATE_ONLY_FIELDS)
        assert _recursive_keys(request).isdisjoint(PRIVATE_ONLY_FIELDS)


@pytest.mark.parametrize(
    "mutation",
    ("version", "request_id", "source_id", "prompt", "schema", "max_tokens"),
)
def test_artifact_validation_rejects_runtime_substitution(mutation):
    artifacts = build_artifact_bytes()

    def mutate(row):
        if mutation == "version":
            row["runtime_manifest_version"] = "forged-runtime-version"
        elif mutation == "request_id":
            row["runtime_request_id"] = "REQ-FORGED"
        elif mutation == "source_id":
            row["source_record_id"] = "TAB-FORGED"
        elif mutation == "prompt":
            row["messages"][0]["content"] = "substituted prompt"
        elif mutation == "schema":
            row["response_schema"] = {"type": "object"}
        elif mutation == "max_tokens":
            row["max_output_tokens"] += 1

    forged = _mutate_jsonl_artifact(
        artifacts, "runtime", 0, mutate, rebind_manifest=True
    )
    with pytest.raises(ValueError, match="runtime"):
        validate_artifact_bytes(forged)


def test_twins_are_additive_exact_reciprocal_and_match_sources():
    public, _, _ = build_rows()
    by_id = {row["id"]: row for row in public}
    for row in public:
        assert all(link in by_id for link in row["paired_record_ids"])
        assert all(row["id"] in by_id[link]["paired_record_ids"] for link in row["paired_record_ids"])

    monitors = [row for row in public if row["record_type"] == "monitoring_twin"]
    assert len(monitors) == 69
    per_pair = Counter(row["pair"] for row in monitors)
    assert set(per_pair) == set(constants.PAIRS)
    assert min(per_pair.values()) == 1
    assert max(per_pair.values()) == 3
    assert Counter(per_pair.values()) == {1: 24, 2: 18, 3: 3}
    assert Counter(row["severity_tier"] for row in monitors) == {
        "T1": 27,
        "T4": 27,
        "T2": 8,
        "T3": 7,
    }
    directions = Counter(row["direction_permutation"] for row in monitors)
    assert abs(directions["A_FIRST"] - directions["B_FIRST"]) <= 1
    base_monitors = [row for row in monitors if row["severity_tier"] in {"T1", "T4"}]
    priority_monitors = [row for row in monitors if row["severity_tier"] in {"T2", "T3"}]
    assert len(base_monitors) == 54
    assert len(priority_monitors) == 15
    assert {row["pair"] for row in base_monitors} == set(constants.PAIRS)
    assert {row["pair"] for row in priority_monitors} == set(constants.PRIORITY_PAIRS)
    threat_parent_ids = {
        row["parent_id"]
        for row in public
        if row["record_type"] == "threat_twin"
    }
    assert threat_parent_ids.isdisjoint({row["parent_id"] for row in monitors})
    for row in monitors:
        parent = by_id[row["parent_id"]]
        assert parent["record_type"] == "adjudication"
        assert parent["framing_arm"] == "neutral"
        for field in (
            "pair",
            "commandment",
            "severity_tier",
            "realization_index",
            "direction_permutation",
            "domain",
            "actions",
            "response_schema",
        ):
            assert row[field] == parent[field]
        assert row["prompt"] == parent["prompt"] + constants.MONITORING_NOTICE

    threats = [row for row in public if row["record_type"] == "threat_twin"]
    for row in threats:
        parent = by_id[row["parent_id"]]
        assert parent["record_type"] == "adjudication"
        assert parent["severity_tier"] in {"T1", "T4"}
        assert row["prompt"] == parent["prompt"] + constants.THREAT_NOTICE
        assert row["framing_arm"] == "threat"

    assert Counter(row["record_type"] for row in public if row["parent_id"] is not None) == {
        "threat_twin": 135,
        "comprehension": 45,
        "recognition": 45,
        "monitoring_twin": 69,
    }


def test_track_a_prompts_hide_religious_vocabulary_and_numbers():
    public, _, _ = build_rows()
    forbidden = ("commandment", "decalogue", "exodus", "deuteronomy", "sabbath", "god")
    for row in public:
        prompt = row["prompt"].lower()
        assert not any(token in prompt for token in forbidden)
        assert not any("commandment %d" % number in prompt for number in range(1, 11))


def test_all_recognition_controls_include_the_matched_parent_case_context():
    public, _, _ = build_rows()
    by_id = {row["id"]: row for row in public}
    recognition = [row for row in public if row["record_type"] == "recognition"]
    assert len(recognition) == 45
    for row in recognition:
        parent = by_id[row["parent_id"]]
        context = parent["prompt"].split(
            " Execute exactly one available action", 1
        )[0]
        assert context in row["prompt"]


def test_private_gold_remains_provisional_until_real_panel_runs():
    _, private, _ = build_rows()
    assert {row["panel_status"] for row in private} == {"NOT_RUN"}
    assert {row["panel_kappa"] for row in private} == {None}
    assert {row["official_gold_eligible"] for row in private} == {False}
    assert all(row["human_evidence"] is None for row in private)
    assert all(row["professional_evidence"] is None for row in private)


def test_frozen_artifacts_match_builder_bytes_and_manifest_hashes():
    artifacts = build_artifact_bytes()
    validate_artifact_bytes(artifacts)
    expected_paths = {
        "public": ROOT / "itembank" / "bank" / "p1-public.jsonl",
        "private": ROOT / "itembank" / "gold" / "p1-private.gold.jsonl",
        "runtime": ROOT / "itembank" / "runtime" / "p1-runtime-manifest.jsonl",
        "manifest": ROOT / "itembank" / "manifest.json",
    }
    for name, path in expected_paths.items():
        assert path.read_bytes() == artifacts[name]
    manifest = json.loads(artifacts["manifest"])
    assert manifest["record_count"] == 636
    assert manifest["panel_status"] == "NOT_RUN"
    for key in ("public", "private", "runtime"):
        assert manifest["artifacts"][key]["sha256"] == canonical_sha256(
            artifacts[key], raw_bytes=True
        )


def test_artifact_validation_rejects_duplicate_public_identity_before_bindings():
    artifacts = build_artifact_bytes()
    first_id = json.loads(artifacts["public"].decode("utf-8").splitlines()[0])["id"]
    forged = _mutate_jsonl_artifact(
        artifacts,
        "public",
        1,
        lambda row: row.__setitem__("id", first_id),
        rebind_manifest=True,
    )
    with pytest.raises(ValueError, match="public IDs must be unique"):
        validate_artifact_bytes(forged)


def test_artifact_validation_rejects_nonreciprocal_parent_link():
    artifacts = build_artifact_bytes()
    public_rows = [
        json.loads(line) for line in artifacts["public"].decode("utf-8").splitlines()
    ]
    twin_index = next(
        index
        for index, row in enumerate(public_rows)
        if row["record_type"] == "threat_twin"
    )
    wrong_parent = next(
        row["id"]
        for row in public_rows
        if row["record_type"] == "adjudication"
        and row["id"] != public_rows[twin_index]["parent_id"]
    )
    forged = _mutate_jsonl_artifact(
        artifacts,
        "public",
        twin_index,
        lambda row: row.__setitem__("paired_record_ids", [wrong_parent]),
        rebind_manifest=True,
    )
    with pytest.raises(ValueError, match="reciprocal|parent link"):
        validate_artifact_bytes(forged)


def test_artifact_validation_rejects_self_linked_primary():
    artifacts = build_artifact_bytes()
    public = [
        json.loads(line) for line in artifacts["public"].decode("utf-8").splitlines()
    ]
    primary = next(row for row in public if row["record_type"] == "adjudication")
    primary["paired_record_ids"].append(primary["id"])
    forged = _rebuild_artifacts_from_public(artifacts, public)
    with pytest.raises(ValueError, match="self-link"):
        validate_artifact_bytes(forged)


def test_artifact_validation_rejects_reciprocal_twin_rewire_to_wrong_parent():
    artifacts = build_artifact_bytes()
    public = [
        json.loads(line) for line in artifacts["public"].decode("utf-8").splitlines()
    ]
    by_id = {row["id"]: row for row in public}
    twin = next(row for row in public if row["record_type"] == "threat_twin")
    old_parent = by_id[twin["parent_id"]]
    wrong_parent = next(
        row
        for row in public
        if row["record_type"] == "adjudication" and row["id"] != old_parent["id"]
    )
    old_parent["paired_record_ids"].remove(twin["id"])
    wrong_parent["paired_record_ids"].append(twin["id"])
    twin["parent_id"] = wrong_parent["id"]
    twin["paired_record_ids"] = [wrong_parent["id"]]
    forged = _rebuild_artifacts_from_public(artifacts, public)
    with pytest.raises(ValueError, match="frozen public projection"):
        validate_artifact_bytes(forged)


def test_artifact_validation_rejects_swapped_action_meanings_with_rebound_projections():
    artifacts = build_artifact_bytes()
    public = [
        json.loads(line) for line in artifacts["public"].decode("utf-8").splitlines()
    ]
    row = next(item for item in public if item["record_type"] == "adjudication")
    action_x = next(action for action in row["actions"] if action["action_id"] == "ACTION_X")
    action_y = next(action for action in row["actions"] if action["action_id"] == "ACTION_Y")
    action_x["artifact"], action_y["artifact"] = action_y["artifact"], action_x["artifact"]
    prompt_prefix = row["prompt"].split("\nACTION_X", 1)[0]
    row["prompt"] = prompt_prefix + "\n" + "\n".join(
        "%s — %s" % (action["action_id"], action["artifact"])
        for action in row["actions"]
    )
    forged = _rebuild_artifacts_from_public(artifacts, public)
    with pytest.raises(ValueError, match="frozen public projection"):
        validate_artifact_bytes(forged)


@pytest.mark.parametrize("mutation", ("seed", "path", "bytes"))
def test_artifact_validation_rejects_manifest_metadata_substitution(mutation):
    artifacts = build_artifact_bytes()
    forged = dict(artifacts)
    manifest = json.loads(forged["manifest"])
    if mutation == "seed":
        manifest["generator_seed"] = "forged-seed"
    elif mutation == "path":
        manifest["artifacts"]["public"]["path"] = "elsewhere.jsonl"
    elif mutation == "bytes":
        manifest["artifacts"]["public"]["bytes"] += 1
    forged["manifest"] = (canonical_json(manifest) + "\n").encode("utf-8")
    with pytest.raises(ValueError, match="manifest"):
        validate_artifact_bytes(forged)


@pytest.mark.parametrize("record_type", ("adjudication", "recognition"))
def test_public_response_schema_enum_must_exactly_match_frozen_choices(record_type):
    public, _, _ = build_rows()
    row = deepcopy(next(row for row in public if row["record_type"] == record_type))
    if record_type == "recognition":
        row["response_schema"]["properties"]["selected_duty_codes"]["items"]["enum"] = [
            "MISSION_FIDELITY",
            "MANDATED_REST",
        ]
    else:
        row["response_schema"]["properties"]["selected_action_id"]["enum"] = [
            "ACTION_X",
            "ACTION_Y",
        ]
    with pytest.raises(ValueError, match="enum must exactly match"):
        validate_public_row(row)
