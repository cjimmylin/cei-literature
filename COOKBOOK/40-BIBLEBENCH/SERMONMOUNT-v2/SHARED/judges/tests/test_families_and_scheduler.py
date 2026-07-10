"""Fail-closed family registry, provenance, and scheduling fixtures."""
from __future__ import annotations

import copy

import pytest

from families import FamilyRegistry, FamilyRegistryError, FamilyResolutionError
from provenance import AssignmentProvenance, ProvenanceError
from scheduler import JudgeCandidate, ScheduleError, schedule_panel


SHA_A = "a" * 64
SHA_B = "b" * 64


def registry_config() -> dict:
    return {
        "registry_version": "registry-test-v1",
        "families": [
            {"family_id": "family-a"},
            {"family_id": "family-b"},
            {"family_id": "family-c"},
            {"family_id": "family-d"},
        ],
        "aliases": [
            {"alias": "author-model", "family_id": "family-a"},
            {"alias": "tested-model", "family_id": "family-b"},
            {"alias": "judge-c-1", "family_id": "family-c"},
            {"alias": "judge-c-2", "family_id": "family-c"},
            {"alias": "judge-d-1", "family_id": "family-d"},
        ],
    }


def role(role_id: str = "item_author", **changes: object) -> dict:
    value = {
        "role_id": role_id,
        "role_type": "material_generation",
        "raw_model_alias": "author-model",
        "raw_authoring_attestation": "Raw declaration retained verbatim.",
        "family_id": "family-a",
        "resolution_status": "resolved",
        "source_hash": SHA_A,
        "content_hash": SHA_B,
        "provenance": {"run_id": "authoring-run-1"},
    }
    value.update(changes)
    return value


def tested(**changes: object) -> dict:
    value = {
        "role_id": "tested_response",
        "role_type": "tested_response",
        "raw_model_alias": "tested-model",
        "raw_authoring_attestation": "Raw tested-response declaration.",
        "family_id": "family-b",
        "resolution_status": "resolved",
        "source_hash": SHA_A,
        "content_hash": SHA_B,
        "provenance": {"run_id": "response-run-1"},
    }
    value.update(changes)
    return value


def manifest_dict(*, roles: list[dict] | None = None, tested_record: dict | None = None) -> dict:
    return {
        "schema_version": "assignment-provenance-v1",
        "registry_version": "registry-test-v1",
        "required_material_roles": ["item_author"],
        "material_generation_families": roles if roles is not None else [role()],
        "tested_response": tested_record if tested_record is not None else tested(),
    }


def roster(registry: FamilyRegistry) -> list[JudgeCandidate]:
    return [
        JudgeCandidate.from_alias("judge-1", "author-model", registry),
        JudgeCandidate.from_alias("judge-2", "tested-model", registry),
        JudgeCandidate.from_alias("judge-3", "judge-c-1", registry),
        JudgeCandidate.from_alias("judge-4", "judge-c-2", registry),
        JudgeCandidate.from_alias("judge-5", "judge-d-1", registry),
    ]


def test_registry_resolves_only_nfkc_casefolded_frozen_aliases() -> None:
    config = registry_config()
    registry = FamilyRegistry.from_config(config)
    config["aliases"][0]["family_id"] = "family-d"

    assert registry.resolve("author-model") == "family-a"
    assert registry.resolve("AUTHOR-MODEL") == "family-a"
    assert registry.to_dict()["aliases"][0]["family_id"] == "family-a"
    for invalid in ("", "unknown", " author-model ", "family-a"):
        with pytest.raises(FamilyResolutionError):
            registry.resolve(invalid)


@pytest.mark.parametrize(
    "aliases",
    [
        [
            {"alias": "collision", "family_id": "family-a"},
            {"alias": "collision", "family_id": "family-b"},
        ],
        [
            {"alias": "collision", "family_id": "family-a"},
            {"alias": "collision", "family_id": "family-a"},
        ],
    ],
)
def test_alias_collisions_and_multiple_mappings_fail_at_registry_freeze(aliases: list[dict]) -> None:
    config = registry_config()
    config["aliases"] = aliases
    with pytest.raises(FamilyRegistryError, match="alias_collision"):
        FamilyRegistry.from_config(config)


def test_role_provenance_round_trip_preserves_raw_attestation_and_hashes() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    manifest = AssignmentProvenance.from_dict(manifest_dict(), registry)
    serialized = manifest.to_dict()

    assert serialized["material_generation_families"][0][
        "raw_authoring_attestation"
    ] == "Raw declaration retained verbatim."
    assert serialized["material_generation_families"][0]["source_hash"] == SHA_A
    assert serialized["material_generation_families"][0]["content_hash"] == SHA_B
    assert serialized["material_generation_families"][0]["resolution_status"] == "resolved"
    assert AssignmentProvenance.from_dict(serialized, registry).to_dict() == serialized


def test_unknown_or_mismatched_resolved_role_family_fails() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    with pytest.raises(FamilyResolutionError):
        AssignmentProvenance.from_dict(
            manifest_dict(roles=[role(raw_model_alias="not-frozen")]), registry
        )
    with pytest.raises(ProvenanceError, match="family_mismatch"):
        AssignmentProvenance.from_dict(
            manifest_dict(roles=[role(family_id="family-d")]), registry
        )


def test_duplicate_or_overlapping_roles_fail_closed() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    with pytest.raises(ProvenanceError, match="role_overlap"):
        AssignmentProvenance.from_dict(
            manifest_dict(roles=[role(), role()]), registry
        )
    with pytest.raises(ProvenanceError, match="role_overlap"):
        AssignmentProvenance.from_dict(
            manifest_dict(tested_record=tested(role_id="item_author")), registry
        )


def test_unresolved_role_is_preserved_but_scheduler_rejects_it() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    unresolved = role(
        raw_model_alias="unlisted-raw-alias",
        family_id=None,
        resolution_status="unresolved",
    )
    manifest = AssignmentProvenance.from_dict(manifest_dict(roles=[unresolved]), registry)
    assert manifest.to_dict()["material_generation_families"][0][
        "resolution_status"
    ] == "unresolved"
    with pytest.raises(ScheduleError, match="unresolved_material_role"):
        schedule_panel(registry, manifest, roster(registry), ["judge-3", "judge-5"])


def test_scheduler_excludes_material_and_tested_response_family_union() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    manifest = AssignmentProvenance.from_dict(manifest_dict(), registry)
    decision = schedule_panel(
        registry, manifest, roster(registry), ["judge-3", "judge-5"]
    )

    assert decision.excluded_family_ids == ("family-a", "family-b")
    assert decision.eligible_family_ids == ("family-c", "family-d")
    assert decision.assigned_family_ids == ("family-c", "family-d")
    assert decision.approved is True

    for excluded_judge in ("judge-1", "judge-2"):
        with pytest.raises(ScheduleError, match="assigned_ineligible_family"):
            schedule_panel(
                registry, manifest, roster(registry), [excluded_judge, "judge-5"]
            )


def test_two_models_from_one_family_do_not_form_independent_panel() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    manifest = AssignmentProvenance.from_dict(manifest_dict(), registry)
    with pytest.raises(ScheduleError, match="assigned_family_count") as caught:
        schedule_panel(registry, manifest, roster(registry), ["judge-3", "judge-4"])
    assert caught.value.audit_record["approved"] is False
    assert caught.value.audit_record["reason_code"] == "assigned_family_count"
    assert caught.value.audit_record["detail"] == (
        "assigned_family_count:1:requires_at_least_2"
    )
    assert caught.value.audit_record["material_generation_families"][0][
        "raw_model_alias"
    ] == "author-model"


def test_fewer_than_two_eligible_families_fails_before_assignment() -> None:
    config = registry_config()
    config["aliases"] = [
        row for row in config["aliases"] if row["alias"] != "judge-d-1"
    ]
    registry = FamilyRegistry.from_config(config)
    limited_roster = [
        JudgeCandidate.from_alias("judge-3", "judge-c-1", registry),
        JudgeCandidate.from_alias("judge-4", "judge-c-2", registry),
    ]
    manifest = AssignmentProvenance.from_dict(manifest_dict(), registry)
    with pytest.raises(ScheduleError, match="eligible_family_count"):
        schedule_panel(registry, manifest, limited_roster, ["judge-3", "judge-4"])


def test_manifest_and_registry_versions_must_match() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    data = manifest_dict()
    data["registry_version"] = "other-registry"
    with pytest.raises(ProvenanceError, match="registry_version"):
        AssignmentProvenance.from_dict(data, registry)


def test_missing_or_undeclared_material_role_fails_at_schedule_boundary() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    missing = manifest_dict(roles=[])
    manifest = AssignmentProvenance.from_dict(missing, registry)
    with pytest.raises(ScheduleError, match="material_role_manifest_mismatch"):
        schedule_panel(registry, manifest, roster(registry), ["judge-3", "judge-5"])

    extra = manifest_dict(roles=[role(), role("rubric_author")])
    manifest = AssignmentProvenance.from_dict(extra, registry)
    with pytest.raises(ScheduleError, match="material_role_manifest_mismatch"):
        schedule_panel(registry, manifest, roster(registry), ["judge-3", "judge-5"])


def test_unresolved_tested_response_family_fails_closed() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    unresolved = tested(
        raw_model_alias="unlisted-tested-alias",
        family_id=None,
        resolution_status="unresolved",
    )
    manifest = AssignmentProvenance.from_dict(
        manifest_dict(tested_record=unresolved), registry
    )
    with pytest.raises(ScheduleError, match="unresolved_tested_response_family"):
        schedule_panel(registry, manifest, roster(registry), ["judge-3", "judge-5"])
