from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Union

from jsonschema import Draft202012Validator
import yaml

MODULES = (
    "fruitbench",
    "corinthlove",
    "tencommandments",
    "sermonmount",
)


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _load_yaml_object(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected YAML object: {path}")
    return value


def _validate(instance: dict[str, Any], schema: dict[str, Any], *, path: Path) -> None:
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        detail = "; ".join(error.message for error in errors)
        raise ValueError(f"schema validation failed for {path}: {detail}")


def _load_frozen_authored_sources(
    root: Path,
) -> tuple[
    Path,
    dict[str, Any],
    list[dict[str, Any]],
    list[tuple[str, dict[str, Any]]],
    dict[tuple[str, str], dict[str, Any]],
]:
    authored_schema_path = root / "schemas" / "authored-episode-bank.schema.json"
    authored_schema = _load_json(authored_schema_path)
    source_banks: list[dict[str, Any]] = []
    loaded_banks: list[tuple[str, dict[str, Any]]] = []
    episodes_by_identity: dict[tuple[str, str], dict[str, Any]] = {}
    observed_episode_ids: set[str] = set()

    for module in MODULES:
        relative_path = Path("modules") / module / "episodes.yaml"
        path = root / relative_path
        bank = _load_yaml_object(path)
        _validate(bank, authored_schema, path=path)
        if bank["module"] != module:
            raise ValueError(f"bank module mismatch: {path}")
        source_banks.append(
            {
                "module": module,
                "path": relative_path.as_posix(),
                "file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "canonical_sha256": _canonical_sha256(bank),
            }
        )
        loaded_banks.append((module, bank))
        for episode in bank["episodes"]:
            episode_id = episode["episode_id"]
            if episode_id in observed_episode_ids:
                raise ValueError(f"duplicate episode_id: {episode_id}")
            observed_episode_ids.add(episode_id)
            episodes_by_identity[(module, episode_id)] = episode

    if len(episodes_by_identity) != 48:
        raise ValueError(
            f"expected 48 unique authored episodes, found {len(episodes_by_identity)}"
        )
    return (
        authored_schema_path,
        authored_schema,
        source_banks,
        loaded_banks,
        episodes_by_identity,
    )


def roll_up_owner_decisions(behavior: str, interpretive: str) -> str:
    allowed = {"APPROVE", "REVISE", "REJECT", "DEFER", "NOT_APPLICABLE"}
    decisions = (behavior, interpretive)
    if any(decision not in allowed for decision in decisions):
        raise ValueError("invalid owner track decision")
    applicable = [
        decision for decision in decisions if decision != "NOT_APPLICABLE"
    ]
    if not applicable:
        return "DEFER"
    for decision in ("DEFER", "REJECT", "REVISE", "APPROVE"):
        if decision in applicable:
            return decision
    raise AssertionError("unreachable owner decision roll-up")


def validate_review_packet(
    packet: dict[str, Any], package_root: Union[str, Path]
) -> None:
    root = Path(package_root).resolve()
    (
        authored_schema_path,
        _,
        expected_source_banks,
        _,
        episodes_by_identity,
    ) = _load_frozen_authored_sources(root)
    expected_schema_sha256 = hashlib.sha256(
        authored_schema_path.read_bytes()
    ).hexdigest()
    if packet.get("source_bank_schema_sha256") != expected_schema_sha256:
        raise ValueError(
            "source_bank_schema_sha256 does not match frozen authored schema"
        )
    if packet.get("source_banks") != expected_source_banks:
        raise ValueError("source_banks metadata does not match frozen authored banks")

    observed_record_identities: set[tuple[str, str]] = set()
    for record in packet.get("records", []):
        identity = (record.get("module"), record.get("episode_id"))
        payload = record.get("review_payload")
        if (
            identity not in episodes_by_identity
            or not isinstance(payload, dict)
            or payload.get("episode_id") != record.get("episode_id")
        ):
            raise ValueError(
                f"{record.get('episode_id')}: frozen authored episode identity mismatch"
            )
        if identity in observed_record_identities:
            raise ValueError(f"{record.get('episode_id')}: duplicate review record identity")
        observed_record_identities.add(identity)
        if payload != episodes_by_identity[identity]:
            raise ValueError(
                f"{record.get('episode_id')}: review_payload does not match "
                "frozen authored episode"
            )
        expected_record = _review_record(identity[0], episodes_by_identity[identity])
        for field, expected_value in expected_record.items():
            if field.startswith("owner_"):
                continue
            if record.get(field) != expected_value:
                raise ValueError(
                    f"{record.get('episode_id')}: non-owner field {field} does not "
                    "match frozen authored episode"
                )
        payload_sha256 = _canonical_sha256(record.get("review_payload"))
        if payload_sha256 != record.get("review_payload_sha256"):
            raise ValueError(
                f"{record.get('episode_id')}: review_payload_sha256 does not match payload"
            )
        if payload_sha256 != record.get("authored_episode_sha256"):
            raise ValueError(
                f"{record.get('episode_id')}: review_payload_sha256 does not match "
                "authored_episode_sha256"
            )
        status = record.get("owner_review_status")
        decision_fields = (
            "owner_behavior_decision",
            "owner_interpretive_decision",
            "owner_record_decision",
        )
        if status == "pending":
            if any(record.get(field) is not None for field in decision_fields):
                raise ValueError("pending owner decisions must be null")
        elif status == "reviewed":
            expected = roll_up_owner_decisions(
                record.get("owner_behavior_decision"),
                record.get("owner_interpretive_decision"),
            )
            if record.get("owner_record_decision") != expected:
                raise ValueError(
                    f"{record.get('episode_id')}: owner_record_decision must be "
                    f"{expected}"
                )
            record_decision = record.get("owner_record_decision")
            if record.get("owner_confidence") == "low" and record_decision not in {
                "REVISE",
                "DEFER",
            }:
                raise ValueError(
                    f"{record.get('episode_id')}: low confidence requires owner "
                    "record decision REVISE or DEFER"
                )
            if (
                record.get("owner_contestability") == "outside_competence"
                and record_decision != "DEFER"
            ):
                raise ValueError(
                    f"{record.get('episode_id')}: outside competence requires owner "
                    "record decision DEFER"
                )
            issues = record.get("owner_issues") or []
            issue_ids = [issue.get("issue_id") for issue in issues]
            if len(issue_ids) != len(set(issue_ids)):
                raise ValueError(f"{record.get('episode_id')}: duplicate owner issue ID")
            for issue in issues:
                priority = issue.get("priority")
                issue_track = issue.get("track")
                if issue_track in {"behavior", "interpretive"}:
                    affected_decision = record.get(
                        f"owner_{issue_track}_decision"
                    )
                else:
                    affected_decision = record.get("owner_record_decision")
                if priority == "P0" and affected_decision != "DEFER":
                    raise ValueError(
                        f"{record.get('episode_id')}: P0 {issue_track} issue "
                        "requires affected decision DEFER"
                    )
                if priority == "P1" and affected_decision not in {
                    "REVISE",
                    "DEFER",
                }:
                    raise ValueError(
                        f"{record.get('episode_id')}: P1 {issue_track} issue "
                        "requires affected decision REVISE or DEFER"
                    )
            priorities = {issue.get("priority") for issue in issues}
            if "P0" in priorities and record_decision != "DEFER":
                raise ValueError(
                    f"{record.get('episode_id')}: P0 requires owner record DEFER"
                )
            if "P1" in priorities and record_decision == "APPROVE":
                raise ValueError(
                    f"{record.get('episode_id')}: P1 cannot have owner record APPROVE"
                )

    if observed_record_identities != set(episodes_by_identity):
        raise ValueError("review records do not exactly cover frozen authored episodes")

    packet_status = packet.get("owner_review_status")
    if packet_status == "completed":
        records = packet.get("records", [])
        if any(record.get("owner_review_status") != "reviewed" for record in records):
            raise ValueError("completed packet requires all records reviewed")
        judge = packet.get("owner_judge") or {}
        judge_id = judge.get("judge_id")
        if any(record.get("owner_judge_id") != judge_id for record in records):
            raise ValueError("completed packet judge identity does not bind all records")

    review_schema_path = root / "schemas" / "provisional-gold-review.schema.json"
    _validate(packet, _load_json(review_schema_path), path=review_schema_path)


def _review_record(module: str, episode: dict[str, Any]) -> dict[str, Any]:
    episode_sha256 = _canonical_sha256(episode)
    return {
        "module": module,
        "episode_id": episode["episode_id"],
        "core_id": episode["core_id"],
        "role": episode["role"],
        "stratum": episode["stratum"],
        "authored_episode_sha256": episode_sha256,
        "review_payload": episode,
        "review_payload_sha256": episode_sha256,
        "provenance": {
            "passage_anchors": episode["passage_anchors"],
            "source_artifacts": episode["source_artifacts"],
        },
        "observable_criteria": {
            "affected_parties": episode["affected_parties"],
            "authority_boundary": episode["authority_boundary"],
            "acceptable_action_band": episode["acceptable_action_band"],
            "prohibited_actions": episode["prohibited_actions"],
            "deficient_pole": episode["deficient_pole"],
            "counterfeit_pole": episode["counterfeit_pole"],
            "red_line_classes": episode["red_line_classes"],
            "terminal_observables": episode["execution_contract"][
                "terminal_observables"
            ],
            "repair_expectations": episode["repair_expectations"],
        },
        "behavioral_attribution": episode["behavioral_attribution"],
        "judge_confidence": episode["judge_confidence"],
        "contestability": episode["contestability"],
        "track_applicability": {
            "behavior": (
                "applicable"
                if episode["behavioral_attribution"] == "applicable"
                else "not_applicable"
            ),
            "interpretive": (
                "applicable"
                if episode["stratum"] == "christian_facing"
                else "not_applicable"
            ),
        },
        "classification": "single_expert_provisional_gold",
        "owner_review_status": "pending",
        "owner_behavior_decision": None,
        "owner_interpretive_decision": None,
        "owner_record_decision": None,
        "owner_behavior_rationale": None,
        "owner_interpretive_rationale": None,
        "owner_confidence": None,
        "owner_contestability": None,
        "owner_issues": None,
        "owner_judge_id": None,
        "owner_notes": None,
        "owner_reviewed_at": None,
    }


def build_review_packet(package_root: Union[str, Path]) -> dict[str, Any]:
    root = Path(package_root).resolve()
    (
        authored_schema_path,
        _,
        source_banks,
        loaded_banks,
        _,
    ) = _load_frozen_authored_sources(root)
    records = []
    for module, bank in loaded_banks:
        for episode in bank["episodes"]:
            records.append(_review_record(module, episode))

    if len(records) != 48:
        raise ValueError(f"expected 48 unique review records, found {len(records)}")

    packet = {
        "packet_version": "provisional-gold-review-v1",
        "classification": "single_expert_provisional_gold",
        "owner_review_status": "pending",
        "owner_judge": None,
        "owner_completed_at": None,
        "source_bank_schema_sha256": hashlib.sha256(
            authored_schema_path.read_bytes()
        ).hexdigest(),
        "source_banks": source_banks,
        "records": records,
        "owner_record_rollup_rule": {
            "version": "dual-track-rollup-v1",
            "behavior_decision_field": "owner_behavior_decision",
            "interpretive_decision_field": "owner_interpretive_decision",
            "record_decision_field": "owner_record_decision",
            "applicable_track_decisions": ["APPROVE", "REVISE", "REJECT", "DEFER"],
            "not_applicable_value": "NOT_APPLICABLE",
            "not_applicable_handling": "ignored",
            "precedence": ["DEFER", "REJECT", "REVISE", "APPROVE"],
            "no_applicable_tracks_result": "DEFER",
        },
        "blinded_repeat_procedure": {
            "timing": "post_pass_one",
            "target_fraction": 0.2,
            "sample_size": 10,
            "stratification": ["module", "role"],
            "module_minimum": 2,
            "role_minimum": 3,
            "seed_domain": "repeat_sampling_v1",
            "digest_input": (
                "UTF-8(repeat_sampling_v1) + NUL + "
                "ASCII(adjudicated_packet_sha256) + NUL + UTF-8(episode_id)"
            ),
            "ranking_rule": (
                "Sort by digest ascending, then episode_id Unicode-code-point "
                "ascending."
            ),
            "selection_rule": (
                "Scan the ranking once and greedily accept the earliest candidate "
                "whose inclusion still permits a 10-record completion with every "
                "module and role minimum satisfied."
            ),
            "skip_rule": (
                "Skip a ranked candidate exactly when accepting it would leave no "
                "10-record completion satisfying every module and role minimum."
            ),
            "backfill_rule": (
                "Continue the same ranked feasibility scan until 10 records are "
                "selected; there is no discretionary backfill."
            ),
            "tie_break": (
                "Digest ties are resolved by episode_id Unicode-code-point "
                "ascending."
            ),
            "opaque_repeat_id_format": "RPT-{ordinal:03d}",
            "mapping_custody": (
                "Create and hold the episode-to-repeat-ID mapping outside "
                "the pass-one packet after selection."
            ),
            "unblinding": "after_repeat_submission",
        },
    }
    validate_review_packet(packet, root)
    return packet


def _file_entry(path: Path, *, relative_path: str) -> dict[str, Any]:
    content = path.read_bytes()
    return {
        "path": relative_path,
        "sha256": hashlib.sha256(content).hexdigest(),
        "bytes": len(content),
    }


def export_review_packet(
    package_root: Union[str, Path], output_dir: Union[str, Path]
) -> tuple[Path, Path]:
    root = Path(package_root).resolve()
    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination
    destination.mkdir(parents=True, exist_ok=True)

    packet = build_review_packet(root)
    packet_bytes = yaml.safe_dump(
        packet,
        allow_unicode=True,
        sort_keys=False,
        width=88,
    ).encode("utf-8")
    packet_path = destination / "provisional-gold-review.yaml"
    manifest_path = destination / "packet-manifest.json"

    authored_schema_path = root / "schemas" / "authored-episode-bank.schema.json"
    review_schema_path = root / "schemas" / "provisional-gold-review.schema.json"
    manifest = {
        "manifest_version": "packet-manifest-v1",
        "classification": "single_expert_provisional_gold",
        "record_count": len(packet["records"]),
        "inputs": {
            "authored_episode_bank_schema": _file_entry(
                authored_schema_path,
                relative_path="schemas/authored-episode-bank.schema.json",
            ),
            "provisional_gold_review_schema": _file_entry(
                review_schema_path,
                relative_path="schemas/provisional-gold-review.schema.json",
            ),
            "episode_banks": [
                {
                    "module": bank["module"],
                    "path": bank["path"],
                    "sha256": bank["file_sha256"],
                    "canonical_sha256": bank["canonical_sha256"],
                }
                for bank in packet["source_banks"]
            ],
        },
        "artifacts": [
            {
                "path": packet_path.name,
                "sha256": hashlib.sha256(packet_bytes).hexdigest(),
                "bytes": len(packet_bytes),
            }
        ],
    }
    manifest_bytes = (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    expected_outputs = (
        (packet_path, packet_bytes),
        (manifest_path, manifest_bytes),
    )
    for path, expected_bytes in expected_outputs:
        if path.exists() and path.read_bytes() != expected_bytes:
            raise FileExistsError(f"refusing to overwrite modified output: {path}")
    for path, expected_bytes in expected_outputs:
        if not path.exists():
            path.write_bytes(expected_bytes)
    return packet_path, manifest_path


def finalize_review_packet(
    package_root: Union[str, Path],
    reviewed_packet_path: Union[str, Path],
    output_dir: Union[str, Path],
    *,
    judge: dict[str, str],
    completed_at: str,
) -> tuple[Path, Path]:
    root = Path(package_root).resolve()
    input_path = Path(reviewed_packet_path).resolve()
    packet = _load_yaml_object(input_path)
    validate_review_packet(packet, root)
    if any(
        record.get("owner_review_status") != "reviewed"
        for record in packet.get("records", [])
    ):
        raise ValueError("all records must be reviewed before finalization")
    judge_id = judge.get("judge_id")
    if any(
        record.get("owner_judge_id") != judge_id
        for record in packet.get("records", [])
    ):
        raise ValueError("judge identity must match every reviewed record")

    completed_packet = json.loads(json.dumps(packet, ensure_ascii=False))
    completed_packet["owner_review_status"] = "completed"
    completed_packet["owner_judge"] = judge
    completed_packet["owner_completed_at"] = completed_at
    validate_review_packet(completed_packet, root)
    packet_bytes = yaml.safe_dump(
        completed_packet,
        allow_unicode=True,
        sort_keys=False,
        width=88,
    ).encode("utf-8")

    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination
    destination.mkdir(parents=True, exist_ok=True)
    packet_path = destination / "adjudicated-provisional-gold-review.yaml"
    manifest_path = destination / "adjudicated-packet-manifest.json"
    manifest = {
        "manifest_version": "adjudicated-packet-manifest-v1",
        "classification": "single_expert_provisional_gold",
        "owner_review_status": "completed",
        "judge": judge,
        "completed_at": completed_at,
        "record_count": len(completed_packet["records"]),
        "source_review_packet": _file_entry(
            input_path, relative_path=input_path.name
        ),
        "artifacts": [
            {
                "path": packet_path.name,
                "sha256": hashlib.sha256(packet_bytes).hexdigest(),
                "bytes": len(packet_bytes),
            }
        ],
    }
    manifest_bytes = (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    if packet_path.exists() or manifest_path.exists():
        raise FileExistsError(
            f"immutable adjudicated output already exists: {destination}"
        )
    with packet_path.open("xb") as stream:
        stream.write(packet_bytes)
    with manifest_path.open("xb") as stream:
        stream.write(manifest_bytes)
    return packet_path, manifest_path


def _repeat_digest(adjudicated_packet_sha256: str, episode_id: str) -> str:
    digest_input = (
        b"repeat_sampling_v1"
        + b"\x00"
        + adjudicated_packet_sha256.encode("ascii")
        + b"\x00"
        + episode_id.encode("utf-8")
    )
    return hashlib.sha256(digest_input).hexdigest()


def _repeat_completion_is_feasible(
    selected: list[dict[str, Any]], remaining: list[dict[str, Any]]
) -> bool:
    sample_size = 10
    module_minimum = 2
    role_minimum = 3
    roles = ("target", "null", "restraint")
    slots = sample_size - len(selected)
    if slots < 0 or len(remaining) < slots:
        return False

    module_counts = {
        module: sum(row["module"] == module for row in selected)
        for module in MODULES
    }
    role_counts = {
        role: sum(row["role"] == role for row in selected) for role in roles
    }
    initial_module_need = tuple(
        max(0, module_minimum - module_counts[module]) for module in MODULES
    )
    initial_role_need = tuple(
        max(0, role_minimum - role_counts[role]) for role in roles
    )

    @lru_cache(maxsize=None)
    def search(
        index: int,
        open_slots: int,
        module_need: tuple[int, ...],
        role_need: tuple[int, ...],
    ) -> bool:
        if open_slots == 0:
            return not any(module_need) and not any(role_need)
        if len(remaining) - index < open_slots:
            return False
        if sum(module_need) > open_slots or sum(role_need) > open_slots:
            return False
        if index >= len(remaining):
            return False

        candidate = remaining[index]
        module_index = MODULES.index(candidate["module"])
        role_index = roles.index(candidate["role"])
        next_module_need = list(module_need)
        next_role_need = list(role_need)
        next_module_need[module_index] = max(0, next_module_need[module_index] - 1)
        next_role_need[role_index] = max(0, next_role_need[role_index] - 1)
        if search(
            index + 1,
            open_slots - 1,
            tuple(next_module_need),
            tuple(next_role_need),
        ):
            return True
        return search(index + 1, open_slots, module_need, role_need)

    return search(0, slots, initial_module_need, initial_role_need)


def build_repeat_mapping(
    completed_packet: dict[str, Any], adjudicated_packet_sha256: str
) -> dict[str, Any]:
    if completed_packet.get("owner_review_status") != "completed":
        raise ValueError("repeat selection requires a completed adjudicated packet")
    if len(adjudicated_packet_sha256) != 64 or any(
        character not in "0123456789abcdef"
        for character in adjudicated_packet_sha256
    ):
        raise ValueError("adjudicated packet SHA-256 must be lowercase hexadecimal")
    records = completed_packet.get("records", [])
    if len(records) != 48:
        raise ValueError("repeat selection requires exactly 48 records")

    ranked = [
        {
            "module": record["module"],
            "role": record["role"],
            "episode_id": record["episode_id"],
            "selection_digest": _repeat_digest(
                adjudicated_packet_sha256, record["episode_id"]
            ),
        }
        for record in records
    ]
    ranked.sort(key=lambda row: (row["selection_digest"], row["episode_id"]))
    if not _repeat_completion_is_feasible([], ranked):
        raise ValueError("no repeat sample satisfies the registered stratification")

    selected: list[dict[str, Any]] = []
    for index, candidate in enumerate(ranked):
        if len(selected) == 10:
            break
        if _repeat_completion_is_feasible(selected + [candidate], ranked[index + 1 :]):
            selected.append(candidate)
    if len(selected) != 10:
        raise ValueError("deterministic repeat selector did not produce 10 records")

    return {
        "mapping_version": "blinded-repeat-mapping-v1",
        "source_adjudicated_packet_sha256": adjudicated_packet_sha256,
        "sample_size": 10,
        "stratification": {
            "module_minimum": 2,
            "role_minimum": 3,
        },
        "entries": [
            {
                "repeat_id": f"RPT-{index:03d}",
                **candidate,
            }
            for index, candidate in enumerate(selected, start=1)
        ],
    }


def write_repeat_mapping(
    package_root: Union[str, Path],
    adjudicated_packet_path: Union[str, Path],
    mapping_path: Union[str, Path],
) -> Path:
    root = Path(package_root).resolve()
    packet_path = Path(adjudicated_packet_path).resolve()
    packet_bytes = packet_path.read_bytes()
    packet = _load_yaml_object(packet_path)
    validate_review_packet(packet, root)
    mapping = build_repeat_mapping(
        packet, hashlib.sha256(packet_bytes).hexdigest()
    )
    destination = Path(mapping_path)
    if destination.exists():
        raise FileExistsError(f"repeat mapping already exists: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    mapping_bytes = yaml.safe_dump(
        mapping, allow_unicode=True, sort_keys=False, width=88
    ).encode("utf-8")
    with destination.open("xb") as stream:
        stream.write(mapping_bytes)
    destination.chmod(0o600)
    return destination


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Export the deterministic BibleBench provisional-gold review packet."
    )
    parser.add_argument("--package-root", required=True)
    parser.add_argument("--output-dir", required=True)
    return parser


def main(argv: Union[list[str], None] = None) -> int:
    arguments = _parser().parse_args(argv)
    try:
        packet_path, manifest_path = export_review_packet(
            arguments.package_root, arguments.output_dir
        )
    except FileExistsError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"wrote {packet_path}")
    print(f"wrote {manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
