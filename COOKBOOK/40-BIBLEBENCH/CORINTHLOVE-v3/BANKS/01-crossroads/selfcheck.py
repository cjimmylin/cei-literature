#!/usr/bin/env python3
"""Fail-loud consolidated offline readiness audit for CROSSROADS."""
from __future__ import annotations

import csv
import json
from pathlib import Path
import re
import sys

import yaml


BANK = Path(__file__).resolve().parent
PRIVATE_COUNT = 600
PUBLIC_COUNT = 30
ACCEPTED_COUNT = 630
REJECTED_COUNT = 40
MOCK_LABEL = "harness validation, NOT a measurement"
CLAUSES = tuple(f"C{i}" for i in range(1, 17))
CANARY_RE = re.compile(
    r"^10CB3-01-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)
JSEED_RE = re.compile(
    r"^JSEED-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)
PUBLIC_FORBIDDEN_KEYS = {
    "path_key", "path_keys", "key", "key_plus", "key_minus",
    "clause_sign", "reaction_table", "reaction_tables", "branch_table",
    "branch_tables", "parameter_state", "hidden_state", "ground_truth",
    "rubric_emphases", "expected_behavior", "failure_modes",
}
CLAUSE_SIGN_RE = re.compile(
    r"\bC(?:[1-9]|1[0-6])\s*(?:\+|-|plus\b|minus\b)", re.I
)
REQUIRED = (
    "README.md", "DECISIONS.md", "clause_mapping.md",
    "key_validation_protocol.md", "stated_pair_study.md",
    "pilot_protocol.md", "judge_anchors.md", "deep_structures.yaml",
    "episodes/private.yaml", "seeds_public.yaml",
    "sidecar/ground_truth.json", "sidecar/judge_token_map.json",
    "sidecar/judge_roster.schema.json", "sidecar/judge_roster.mock.json",
    "sidecar/hardness_gate_log.jsonl", "sidecar/stated_pairs.json",
    "export/coverage_map.json",
    "export/profile.schema.json", "export/loadings_table.csv",
    "export/expected_export_manifest.json", "export/episode_table.jsonl",
    "export/episode_table.csv", "export/export_report.json",
    "megamatrix/calibration_notes.md",
)


def check_counts(private: list, public: list) -> str:
    assert len(private) == PRIVATE_COUNT, "private episode count must be 600"
    assert len(public) == PUBLIC_COUNT, "public episode count must be 30"
    assert all(row.get("split") == "private" for row in private), "private split labels differ"
    assert all(row.get("split") == "public" for row in public), "public split labels differ"
    ids = [row.get("id") for row in private + public]
    assert len(ids) == len(set(ids)) == ACCEPTED_COUNT, "episode IDs must be 630 unique values"
    return "630 episodes (600 private + 30 public)"


def check_canaries(episodes: list, registry_path: Path) -> str:
    canaries = [row.get("canary") for row in episodes]
    assert len(canaries) == len(set(canaries)) == ACCEPTED_COUNT, "canaries must be 630 unique values"
    assert all(isinstance(value, str) and CANARY_RE.fullmatch(value)
               for value in canaries), "canary format differs"
    assert Path(registry_path).is_file(), "global canary registry is missing"
    mappings, all_markers = {}, []
    for number, line in enumerate(Path(registry_path).read_text().splitlines(), 1):
        if not line.strip():
            continue
        parts = line.split("\t")
        assert len(parts) == 2, f"canary registry line {number} is malformed"
        marker, item_id = parts
        assert marker not in mappings, "canary registry markers must be globally unique"
        mappings[marker] = item_id
        all_markers.append(marker)
    assert len(all_markers) == len(set(all_markers)), "canary registry must be append-only unique"
    expected = {row["canary"]: row["id"] for row in episodes}
    assert all(mappings.get(marker) == item_id for marker, item_id in expected.items()), (
        "every current canary must retain its item-bound registry mapping"
    )
    return "630 unique registered canaries"


def check_judge_seed_map(episodes: list, judge_map: dict) -> str:
    ids = {row["id"] for row in episodes}
    assert isinstance(judge_map, dict) and len(judge_map) == ACCEPTED_COUNT, (
        "judge authoring-seed map must contain exactly 630 rows"
    )
    assert all(isinstance(token, str) and JSEED_RE.fullmatch(token)
               for token in judge_map), "authoring seeds must be private JSEED UUIDv4 tokens"
    assert len(set(judge_map.values())) == ACCEPTED_COUNT, "judge-seed mappings must be one-to-one"
    assert set(judge_map.values()) == ids, "judge-seed map must cover every episode exactly"
    return "630 private authoring JSEED mappings (zero pre-issued JCASE tokens)"


def check_judge_roster_assets(root: Path) -> str:
    """Validate the non-measurement fixture without inventing an actual roster."""
    import jsonschema
    from scorers.judge_roster import (
        FrozenJudgeRoster, canonical_roster_sha256,
    )

    root = Path(root)
    schema = json.loads(
        (root / "sidecar/judge_roster.schema.json").read_text(encoding="utf-8")
    )
    document = json.loads(
        (root / "sidecar/judge_roster.mock.json").read_text(encoding="utf-8")
    )
    jsonschema.Draft202012Validator(schema).validate(document)
    assert document.get("provenance") == MOCK_LABEL, (
        "mock judge roster must be labelled exactly as harness validation"
    )
    assert document.get("human_validation_status") == (
        "not performed; actual roster is an external dependency"
    ), "mock roster must not claim actual human or model judging"
    assert not (root / "sidecar/judge_roster.actual.json").exists(), (
        "actual judge roster must remain an external run-time dependency"
    )
    roster = FrozenJudgeRoster.from_document(
        document, expected_sha256=canonical_roster_sha256(document)
    )
    raw = [row for row in document["judges"] if row["role"] == "raw"]
    adjudicators = [
        row for row in document["judges"] if row["role"] == "adjudicator"
    ]
    assert len(raw) >= 2 and len({row["family"] for row in raw}) >= 2, (
        "mock harness needs two distinct raw judge families"
    )
    assert adjudicators, "mock harness needs a separately roled adjudicator"
    for row in raw + adjudicators:
        roster.lookup(row["judge_id"], required_role=row["role"])
    return "hash-frozen mock JUDGE roster validates; actual roster remains external"


def check_hardness(episodes: list, decisions: list) -> str:
    assert isinstance(decisions, list), "hardness log must be a JSONL list"
    accepted = [row for row in decisions if row.get("decision") == "accepted"]
    rejected = [row for row in decisions if row.get("decision") == "rejected"]
    assert len(accepted) == ACCEPTED_COUNT, "accepted hardness count must be 630"
    assert len(rejected) == REJECTED_COUNT, "rejected hardness count must be 40"
    assert {row.get("candidate_id") for row in accepted} == {
        row["id"] for row in episodes
    }, "hardness accepted IDs must equal the emitted bank"
    rejected_ids = [row.get("candidate_id") for row in rejected]
    assert len(rejected_ids) == len(set(rejected_ids)), "rejected hardness IDs must be unique"
    assert all(isinstance(row.get("reasons"), list) and row["reasons"]
               and all(isinstance(reason, str) and reason.strip()
                       for reason in row["reasons"])
               for row in rejected), "every rejected hardness row needs reasons"
    assert len(decisions) == ACCEPTED_COUNT + REJECTED_COUNT, "hardness log has extra decisions"
    return "670 hardness decisions (630 accepted + 40 rejected)"


def _redaction_violations(value, path="public") -> list[str]:
    violations = []
    if isinstance(value, dict):
        for key, item in value.items():
            normalized = str(key).lower().replace("-", "_")
            if normalized in PUBLIC_FORBIDDEN_KEYS:
                violations.append(f"{path}.{key}")
            violations.extend(_redaction_violations(item, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            violations.extend(_redaction_violations(item, f"{path}[{index}]"))
    elif isinstance(value, str) and CLAUSE_SIGN_RE.search(value):
        violations.append(path)
    return violations


def check_public_redaction(public: list) -> str:
    violations = _redaction_violations(public)
    assert not violations, f"public YAML redaction failed: {violations[:8]}"
    return "public YAML is key-redacted"


def check_stated_pairs(episodes: list, pairs: list) -> str:
    assert isinstance(pairs, list) and len(pairs) == 60, (
        "stated-pair inventory must contain exactly 60 rows"
    )
    pair_ids = [row.get("pair_id") for row in pairs]
    enacted_ids = [row.get("enacted_item_id") for row in pairs]
    assert (all(isinstance(value, str) and value for value in pair_ids)
            and len(pair_ids) == len(set(pair_ids))), "stated pair IDs must be unique"
    assert len(enacted_ids) == len(set(enacted_ids)), (
        "stated pairs require 60 unique enacted matches"
    )
    assert set(enacted_ids).issubset({row["id"] for row in episodes}), (
        "stated pairs reference unknown enacted items"
    )
    counts = {
        order: sum(row.get("order") == order for row in pairs)
        for order in ("stated_first", "enacted_first")
    }
    assert counts == {"stated_first": 30, "enacted_first": 30}, (
        "stated-pair order schedule must be balanced 30/30"
    )
    assert all(isinstance(row.get("stated_item"), dict) and row["stated_item"]
               for row in pairs), "every pair needs a nonempty matched stated item"
    return "60 unique stated/enacted pairs (30 per order)"


def _signature(value: dict) -> tuple:
    return (
        value["tool"], value["target"], value["operation"],
        json.dumps(
            value["arguments"], sort_keys=True, separators=(",", ":"),
            ensure_ascii=False, allow_nan=False,
        ),
    )


def check_ground_truth_semantics(episodes: list, sidecar: dict) -> str:
    from collections import Counter
    from scorers.path_classifier import classify_path

    assert set(sidecar) == {row["id"] for row in episodes}, (
        "semantic check requires exact ground-truth coverage"
    )
    for episode in episodes:
        hidden = sidecar[episode["id"]]
        clauses = hidden.get("clauses")
        specs = hidden.get("path_specs")
        keys = hidden.get("path_keys")
        assert isinstance(clauses, list) and len(clauses) == 4, (
            "every episode must have four active clauses"
        )
        assert isinstance(specs, list) and len(specs) == 4, (
            "every generated fork must have four path specs"
        )
        path_ids = {spec.get("path_id") for spec in specs}
        assert len(path_ids) == 4 and set(keys) == path_ids, (
            "path specs and key vectors must be a bijection"
        )
        assert {_signature(row) for row in episode["affordances"]} == {
            _signature(row) for row in specs
        }, "visible and hidden executable signatures differ"
        per_clause = {clause: [] for clause in clauses}
        for path_id, vector in keys.items():
            assert set(vector) == set(clauses), "path vector active clauses differ"
            assert Counter(vector.values()) == Counter({1: 2, -1: 2}), (
                "each path must preserve the 2+/2- twin-pole balance"
            )
            for clause, sign in vector.items():
                per_clause[clause].append(sign)
        assert all(Counter(values) == Counter({1: 2, -1: 2})
                   for values in per_clause.values()), (
            "every clause must be honored and violated by two paths"
        )
        assert hidden.get("evasion_key") == {
            clause: -1 for clause in clauses
        }, "evasion_key must score every active clause -1"
        assert hidden.get("evasion_paths") == [], (
            "expiry evasion must not be conflated with an explicit path"
        )
        reaction = hidden.get("reaction_table")
        assert isinstance(reaction, dict) and set(reaction) == path_ids | {"evasion"}, (
            "reaction branch coverage must equal four paths plus evasion"
        )
        assert all(isinstance(branch, dict)
                   and isinstance(branch.get("turns"), list)
                   and 3 <= len(branch["turns"]) <= 8
                   for branch in reaction.values()), (
            "every reaction branch must contain 3..8 turns"
        )
        fork_open = hidden.get("fork_open_turn")
        window = hidden.get("fork_window_turns")
        for index, spec in enumerate(specs):
            event = {
                "event_id": f"selfcheck-{index}",
                "turn": fork_open,
                "tool": spec["tool"],
                "target": spec["target"],
                "operation": spec["operation"],
                "arguments": spec["arguments"],
                "status": "committed",
            }
            observed = classify_path([event], specs, fork_open, window)
            assert (observed["status"] == "resolved"
                    and observed["path_id"] == spec["path_id"]
                    and observed["mechanical_flag"] is False), (
                "semantic path classifier failed a generated signature"
            )
        evasion = classify_path([], specs, fork_open, window)
        assert (evasion["status"] == "evasion" and evasion["evasion"] is True
                and evasion["mechanical_flag"] is False), (
            "empty fork must resolve to mechanical evasion"
        )
    return "semantic path/reaction/evasion/twin-pole contracts pass"


def check_design_rank(structures: list) -> dict:
    from collections import Counter
    from analysis.latent_profile import audit_block_information

    assert isinstance(structures, list) and len(structures) == 40, (
        "design rank check requires exactly 40 structures"
    )
    rows = []
    for structure in structures:
        clauses = structure["clauses"]
        paths = structure["base_paths"]
        assert len(clauses) == len(paths) == 4, "structure size changed"
        per_clause = {clause: [] for clause in clauses}
        for path in paths:
            vector = path["clause_keys"]
            assert set(vector) == set(clauses), "structure key clauses differ"
            assert Counter(vector.values()) == Counter({1: 2, -1: 2}), (
                "structure path twin-pole balance failed"
            )
            for clause, sign in vector.items():
                per_clause[clause].append(sign)
        assert all(Counter(values) == Counter({1: 2, -1: 2})
                   for values in per_clause.values()), (
            "structure clause twin-pole balance failed"
        )
        rows.append({
            "structure_id": structure["structure_id"],
            "path_keys": {
                path["path_id"]: path["clause_keys"] for path in paths
            },
        })
    report = audit_block_information(
        rows, min_rank=15, min_pair_coverage=2, min_clause_blocks=10
    )
    assert report["rank"] == 15 and report["gate_pass"] is True, (
        "actual design must attain the sum-zero rank-15 gate"
    )
    return report


def check_scope_and_citations(root: Path) -> str:
    root = Path(root)
    sibling_tokens = (
        "CHARI" + "TROC", "DIM" + "GLASS",
        "CORINTH" + "LOVE/BANKS/07-", "CORINTH" + "LOVE-v2/",
    )
    banned_citation = "icmi" + "-proceedings"
    violations = []
    for path in root.rglob("*"):
        if (not path.is_file() or path.suffix.lower() not in {
                ".py", ".md", ".json", ".jsonl", ".yaml", ".yml", ".csv", ".txt"}):
            continue
        text = path.read_text(errors="replace")
        if any(token.lower() in text.lower() for token in sibling_tokens):
            violations.append(str(path))
        if banned_citation.lower() in text.lower():
            violations.append(str(path))
    assert not violations, f"scope/citation scan failed: {sorted(set(violations))[:8]}"
    return "scope and citation scan clean"


def check_required_files(root: Path) -> str:
    missing = [relative for relative in REQUIRED if not (Path(root) / relative).is_file()]
    assert not missing, f"required artifacts missing: {missing}"
    return f"{len(REQUIRED)} required artifacts present"


def _read_yaml(path: Path) -> list:
    with path.open(encoding="utf-8") as handle:
        rows = yaml.safe_load(handle)
    assert isinstance(rows, list), f"{path.name} must contain a list"
    return rows


def _read_jsonl(path: Path) -> list:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            assert line.endswith("\n"), f"{path.name} line {number} is truncated"
            rows.append(json.loads(line))
    return rows


def check_export_artifacts(root: Path) -> str:
    export = Path(root) / "export"
    manifest = json.loads((export / "expected_export_manifest.json").read_text())
    rows = _read_jsonl(export / "episode_table.jsonl")
    expected = manifest.get("expected_row_count")
    assert len(rows) == expected and expected > 0, "export JSONL row count differs"
    from export import export_megamatrix as exporter
    assert all(set(row) == set(exporter.SCHEMA) for row in rows), "export schema differs"
    identities = [(row["model_id"], row["item_id"], row["clause"]) for row in rows]
    assert len(identities) == len(set(identities)), "export rows are duplicated"
    expected_ids = {
        (row["model_id"], row["item_id"], row["clause"])
        for row in manifest["expected_rows"]
    }
    assert set(identities) == expected_ids, "export matrix is truncated or unexpected"
    with (export / "episode_table.csv").open(newline="", encoding="utf-8") as handle:
        csv_rows = list(csv.DictReader(handle))
    assert len(csv_rows) == len(rows), "CSV/JSONL export counts differ"
    report = json.loads((export / "export_report.json").read_text())
    if any("mock" in model.lower() for model in manifest["expected_models"]):
        assert report.get("provenance") == MOCK_LABEL, "mock export label differs"
    coverage = json.loads((export / "coverage_map.json").read_text())
    assert coverage["fixed_before_pilot"] is True, "coverage map must be frozen"
    assert coverage["declared_coverage"]["clauses"] == list(CLAUSES), (
        "coverage map must preserve native C1-C16 order"
    )
    return f"{len(rows)} manifest-complete ten-field export rows"


def run(root: Path = BANK, write_report: bool = True) -> dict:
    root = Path(root)
    check_required_files(root)
    private = _read_yaml(root / "episodes/private.yaml")
    public = _read_yaml(root / "seeds_public.yaml")
    episodes = private + public
    results = {
        "counts": check_counts(private, public),
        "public_redaction": check_public_redaction(public),
    }
    sidecar = json.loads((root / "sidecar/ground_truth.json").read_text())
    assert set(sidecar) == {row["id"] for row in episodes}, "ground truth coverage differs"
    results["canaries"] = check_canaries(
        episodes, root.parent / "canary_registry.txt"
    )
    results["judge_authoring_seeds"] = check_judge_seed_map(
        episodes, json.loads((root / "sidecar/judge_token_map.json").read_text())
    )
    results["judge_roster"] = check_judge_roster_assets(root)
    results["hardness"] = check_hardness(
        episodes, _read_jsonl(root / "sidecar/hardness_gate_log.jsonl")
    )
    results["stated_pairs"] = check_stated_pairs(
        episodes, json.loads((root / "sidecar/stated_pairs.json").read_text())
    )
    results["ground_truth_semantics"] = check_ground_truth_semantics(
        episodes, sidecar
    )
    structures = _read_yaml(root / "deep_structures.yaml")
    results["design_information"] = check_design_rank(structures)
    lib_path = str(root / "lib")
    if lib_path not in sys.path:
        sys.path.insert(0, lib_path)
    import payloads
    import split_hygiene
    for episode in episodes:
        payloads.build_model_payload(episode)
    split_report = split_hygiene.audit(public, private, sidecar)
    split_hygiene.assert_clean(split_report)
    results["split_hygiene"] = split_report
    from adversarial import run_adversarial
    adversarial_report = run_adversarial.evaluate(episodes, sidecar)
    run_adversarial.assert_all_caught(adversarial_report)
    results["adversarial"] = adversarial_report
    results["export"] = check_export_artifacts(root)
    results["scope"] = check_scope_and_citations(root)
    report = {"provenance": MOCK_LABEL, "passed": True, "checks": results}
    if write_report:
        (root / "reports").mkdir(exist_ok=True)
        (root / "reports/selfcheck_report.json").write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n"
        )
    return report


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
