"""Adversarial regressions from the independent bounded-core review."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource

from canonical import (
    CanonicalizationError,
    build_packet,
    canonical_bytes,
    content_hash,
    evidence_hash,
    rubric_hash,
    verify_packet,
)
from families import FamilyRegistry, FamilyRegistryError
from metrics import weighted_kappa
from privacy import PacketPrivacyError, require_packet_privacy
from provenance import AssignmentProvenance, ProvenanceError
from results import ResultValidationError, validate_judgment, validate_tested_response_disposition
from scheduler import schedule_panel
from transforms import IdentityMaskError, mask_identity_spans, validate_transformed_view

from test_canonical import ASSIGNMENT, RUBRIC
from test_families_and_scheduler import manifest_dict, registry_config, roster
from test_results import envelope


ROOT = Path(__file__).resolve().parents[1]


def raw_view(text: str = "I am Model-X; here are the material facts.") -> dict:
    return {
        "parent_evidence_hash": None,
        "transform": None,
        "task": {"prompt": "Reply."},
        "response": {"text": text, "events": []},
    }


def test_registry_normalizes_canonical_ids_and_aliases_at_freeze() -> None:
    config = {
        "registry_version": "registry-v1",
        "families": [{"family_id": "ＦＡＭＩＬＹ－Ａ"}],
        "aliases": [{"alias": "ＡＵＴＨＯＲ－ＭＯＤＥＬ", "family_id": "ＦＡＭＩＬＹ－Ａ"}],
    }
    registry = FamilyRegistry.from_config(config)
    assert registry.version == "registry-v1"
    assert registry.family_ids == ("family-a",)
    assert registry.resolve("Author-Model") == "family-a"
    assert registry.resolve("ＡＵＴＨＯＲ－ＭＯＤＥＬ") == "family-a"
    assert registry.to_dict() == {
        "registry_version": "registry-v1",
        "families": [{"family_id": "family-a"}],
        "aliases": [{"alias": "author-model", "family_id": "family-a"}],
    }


@pytest.mark.parametrize(
    "families,aliases",
    [
        (
            [{"family_id": "Family-A"}, {"family_id": "ＦＡＭＩＬＹ－Ａ"}],
            [],
        ),
        (
            [{"family_id": "family-a"}, {"family_id": "family-b"}],
            [
                {"alias": "Judge-A", "family_id": "family-a"},
                {"alias": "ＪＵＤＧＥ－Ａ", "family_id": "family-b"},
            ],
        ),
        (
            [{"family_id": "family-a"}, {"family_id": "family-b"}],
            [{"alias": "ＦＡＭＩＬＹ－Ａ", "family_id": "family-b"}],
        ),
    ],
)
def test_registry_rejects_normalized_family_alias_and_canonical_alias_collisions(
    families: list[dict], aliases: list[dict]
) -> None:
    with pytest.raises(FamilyRegistryError, match="collision|duplicate"):
        FamilyRegistry.from_config(
            {"registry_version": "v1", "families": families, "aliases": aliases}
        )


@pytest.mark.parametrize(
    "private_key",
    [
        "model_id",
        "provider",
        "family_id",
        "arm_label",
        "vendor",
        "model_family",
        "condition_label",
        "cross_modality_outcomes",
        "endpoint_version",
    ],
)
def test_privacy_recursively_rejects_full_readme_identity_and_condition_keys(
    private_key: str,
) -> None:
    packet = build_packet(raw_view(), ASSIGNMENT, RUBRIC)
    packet["view"]["response"]["nested"] = {private_key.upper(): "secret"}
    with pytest.raises(PacketPrivacyError, match="forbidden private field"):
        require_packet_privacy(packet)


def test_privacy_normalizes_nfkc_casefold_for_keys_and_embedded_values() -> None:
    packet = build_packet(raw_view(), ASSIGNMENT, RUBRIC)
    packet["view"]["task"]["ＭＯＤＥＬ＿ＩＤ"] = "hidden"
    with pytest.raises(PacketPrivacyError, match="forbidden private field"):
        require_packet_privacy(packet)

    packet = build_packet(raw_view("Identity: ＡＵＴＨＯＲ－ＭＯＤＥＬ."), ASSIGNMENT, RUBRIC)
    with pytest.raises(PacketPrivacyError, match="forbidden value"):
        require_packet_privacy(packet, forbidden_values=("author-model",))


def test_identity_mask_is_deterministic_linked_and_neighbor_preserving() -> None:
    raw = raw_view()
    original = copy.deepcopy(raw)
    derived = mask_identity_spans(
        raw,
        [
            {
                "path": "response.text",
                "source_start": 5,
                "source_end": 12,
                "replacement": "<MODEL_ID>",
            }
        ],
        transform_version="identity-mask-v1",
        identity_tokens={"<MODEL_ID>": ["Model-X"]},
    )
    assert raw == original
    assert derived["response"]["text"] == "I am <MODEL_ID>; here are the material facts."
    assert derived["parent_evidence_hash"] == evidence_hash(raw)
    span = derived["transform"]["span_map"][0]
    assert span == {
        "path": "response.text",
        "source_start": 5,
        "source_end": 12,
        "derived_start": 5,
        "derived_end": 15,
        "replacement": "<MODEL_ID>",
    }
    transform_payload = {
        key: value for key, value in derived["transform"].items() if key != "transform_hash"
    }
    assert derived["transform"]["transform_hash"] == content_hash(
        {"parent_evidence_hash": evidence_hash(raw), **transform_payload}
    )
    assert validate_transformed_view(
        derived, raw, identity_tokens={"<MODEL_ID>": ["Model-X"]}
    ) is True

    packet = build_packet(
        derived,
        ASSIGNMENT,
        RUBRIC,
        parent_view=raw,
        identity_tokens={"<MODEL_ID>": ["Model-X"]},
    )
    assert verify_packet(
        packet,
        ASSIGNMENT,
        parent_view=raw,
        identity_tokens={"<MODEL_ID>": ["Model-X"]},
    ) is True
    with pytest.raises(CanonicalizationError, match="parent_view"):
        verify_packet(packet, ASSIGNMENT)


def test_identity_mask_rejects_bounds_overlap_and_unmapped_mutation() -> None:
    raw = raw_view()
    with pytest.raises(IdentityMaskError, match="bounds"):
        mask_identity_spans(
            raw,
            [{"path": "response.text", "source_start": 5, "source_end": 500, "replacement": "X"}],
            transform_version="identity-mask-v1",
            identity_tokens={"<MODEL_ID>": ["Model-X"]},
        )
    with pytest.raises(IdentityMaskError, match="overlap"):
        mask_identity_spans(
            raw,
            [
                {"path": "response.text", "source_start": 5, "source_end": 12, "replacement": "<MODEL_ID>"},
                {"path": "response.text", "source_start": 10, "source_end": 13, "replacement": "<MODEL_ID>"},
            ],
            transform_version="identity-mask-v1",
            identity_tokens={"<MODEL_ID>": ["Model-X"]},
        )
    derived = mask_identity_spans(
        raw,
        [{"path": "response.text", "source_start": 5, "source_end": 12, "replacement": "<MODEL_ID>"}],
        transform_version="identity-mask-v1",
        identity_tokens={"<MODEL_ID>": ["Model-X"]},
    )
    derived["response"]["text"] = derived["response"]["text"].replace("facts", "claims")
    with pytest.raises(IdentityMaskError, match="coverage|reproduce"):
        validate_transformed_view(
            derived, raw, identity_tokens={"<MODEL_ID>": ["Model-X"]}
        )


def test_identity_mask_rejects_substantive_selection_and_untyped_placeholder() -> None:
    raw = raw_view()
    with pytest.raises(IdentityMaskError, match="identity-bearing"):
        mask_identity_spans(
            raw,
            [
                {
                    "path": "response.text",
                    "source_start": 29,
                    "source_end": 37,
                    "replacement": "<MODEL_ID>",
                }
            ],
            transform_version="identity-mask-v1",
            identity_tokens={"<MODEL_ID>": ["Model-X"]},
        )
    with pytest.raises(IdentityMaskError, match="placeholder"):
        mask_identity_spans(
            raw,
            [
                {
                    "path": "response.text",
                    "source_start": 5,
                    "source_end": 12,
                    "replacement": "REDACTED",
                }
            ],
            transform_version="identity-mask-v1",
            identity_tokens={"<MODEL_ID>": ["Model-X"]},
        )


def test_verify_packet_rejects_unsupported_schema_extras_and_private_fields() -> None:
    packet = build_packet(raw_view(), ASSIGNMENT, RUBRIC)
    packet["unexpected"] = "extra"
    with pytest.raises(CanonicalizationError, match="envelope"):
        verify_packet(packet, ASSIGNMENT)

    packet = build_packet(raw_view(), ASSIGNMENT, RUBRIC)
    packet["schema_version"] = "judge-transcript-v999"
    with pytest.raises(CanonicalizationError, match="schema_version"):
        verify_packet(packet, ASSIGNMENT)

    packet = build_packet(raw_view(), ASSIGNMENT, RUBRIC)
    packet["view"]["task"]["provider"] = "private"
    with pytest.raises(PacketPrivacyError):
        verify_packet(packet, ASSIGNMENT)

    malformed_view = raw_view()
    malformed_view["task"] = "not-an-object"
    with pytest.raises(CanonicalizationError, match="task/response"):
        build_packet(malformed_view, ASSIGNMENT, RUBRIC)


def test_packet_build_and_verify_apply_configured_forbidden_identity_values() -> None:
    view = raw_view("I am ＭＯＤＥＬ－Ｘ.")
    with pytest.raises(PacketPrivacyError, match="forbidden value"):
        build_packet(view, ASSIGNMENT, RUBRIC, forbidden_values=("model-x",))

    packet = build_packet(view, ASSIGNMENT, RUBRIC)
    with pytest.raises(PacketPrivacyError, match="forbidden value"):
        verify_packet(packet, ASSIGNMENT, forbidden_values=("model-x",))


def test_verify_packet_applies_builder_semantics_to_forged_envelope() -> None:
    packet = build_packet(raw_view(), ASSIGNMENT, RUBRIC)
    packet["rubric"]["rubric_id"] = "   "
    packet["rubric_hash"] = rubric_hash(packet["rubric"])
    without_packet_hash = {
        key: value for key, value in packet.items() if key != "packet_hash"
    }
    packet["packet_hash"] = hashlib.sha256(
        canonical_bytes(without_packet_hash)
    ).hexdigest()
    with pytest.raises(CanonicalizationError, match="rubric_id"):
        verify_packet(packet, ASSIGNMENT)


def test_judgment_binds_rubric_id_to_result_schema_and_rejects_unknown_rubric() -> None:
    mismatched = envelope(
        result={"result_schema": "witness-pole-v1", "label": "gold"}
    )
    mismatched["rubric_id"] = "canticle-graded"
    with pytest.raises(ResultValidationError, match="rubric.*result_schema"):
        validate_judgment(mismatched)

    unknown = envelope(status="abstain", result=None, reason="missing_evidence")
    unknown["rubric_id"] = "unregistered-rubric"
    with pytest.raises(ResultValidationError, match="rubric_id"):
        validate_judgment(unknown)


@pytest.mark.parametrize(
    "field,value",
    [("status", {}), ("disposition", []), ("disposition", {})],
)
def test_invalid_states_always_raise_documented_validation_error(field: str, value: object) -> None:
    if field == "status":
        record = envelope(result={"result_schema": "witness-pole-v1", "label": "gold"})
        record[field] = value
        with pytest.raises(ResultValidationError):
            validate_judgment(record)
    else:
        with pytest.raises(ResultValidationError):
            validate_tested_response_disposition(
                {"schema_version": "tested-response-disposition-v1", "evidence_hash": "a" * 64, field: value}
            )


@pytest.mark.parametrize("bad_value", [float("nan"), float("inf"), -1.01, 1.01])
def test_weighted_kappa_rejects_nonfinite_or_out_of_range_strategy_values(
    bad_value: float,
) -> None:
    class BadStrategy:
        strategy_id = "bad-fixture"

        def compute(self, left: list[int], right: list[int]) -> float:
            return bad_value

    with pytest.raises(ValueError, match="finite|range"):
        weighted_kappa([0], [0], strategy=BadStrategy())


def test_private_scheduler_audits_include_raw_aliases_and_role_linkage_hashes() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    provenance = AssignmentProvenance.from_dict(manifest_dict(), registry)
    candidates = roster(registry)
    decision = schedule_panel(registry, provenance, candidates, ["judge-3", "judge-5"])
    audit = decision.to_dict()
    assert audit["material_generation_families"] == [
        {
            "role_id": "item_author",
            "raw_model_alias": "author-model",
            "family_id": "family-a",
            "source_hash": "a" * 64,
            "content_hash": "b" * 64,
            "resolution_status": "resolved",
        }
    ]
    assert audit["tested_response"]["raw_model_alias"] == "tested-model"
    assert {row["raw_model_alias"] for row in audit["assigned_judges"]} == {
        "judge-c-1",
        "judge-d-1",
    }

    with pytest.raises(Exception) as caught:
        schedule_panel(registry, provenance, candidates, ["judge-3", "judge-4"])
    assert caught.value.audit_record["material_generation_families"] == audit[
        "material_generation_families"
    ]

    decision.material_generation_families[0]["family_id"] = "tampered"
    assert decision.to_dict()["material_generation_families"][0]["family_id"] == "family-a"

    rejected = caught.value.audit_record
    rejected["material_generation_families"][0]["family_id"] = "tampered"
    assert caught.value.audit_record["material_generation_families"][0][
        "family_id"
    ] == "family-a"


def test_scheduler_rejects_same_version_registry_commitment_swap() -> None:
    original = FamilyRegistry.from_config(registry_config())
    provenance = AssignmentProvenance.from_dict(manifest_dict(), original)
    swapped_config = registry_config()
    swapped_config["aliases"].append(
        {"alias": "unused-alias", "family_id": "family-c"}
    )
    swapped = FamilyRegistry.from_config(swapped_config)
    assert swapped.version == original.version
    assert swapped.registry_hash != original.registry_hash
    with pytest.raises(Exception, match="registry_hash"):
        schedule_panel(
            swapped,
            provenance,
            roster(swapped),
            ["judge-3", "judge-5"],
        )


def test_public_projection_has_public_identity_commitment_and_no_embedded_private_ids() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    provenance = AssignmentProvenance.from_dict(manifest_dict(), registry)
    public = provenance.to_public_dict(
        {"family-a": "authoring-panel-1", "family-b": "tested-panel-1"}
    )
    assert public["schema_version"] == "public-assignment-provenance-v1"
    assert public["registry_commitment"] == registry.registry_hash
    assert "registry_version" not in public

    for embedded in ("public-family-a-label", "PUBLIC-AUTHOR-MODEL-LABEL"):
        with pytest.raises(ProvenanceError, match="anonymized family label"):
            provenance.to_public_dict(
                {"family-a": embedded, "family-b": "tested-panel-1"}
            )


def test_public_projection_scans_all_fields_and_normalized_label_collisions() -> None:
    registry = FamilyRegistry.from_config(registry_config())
    leaking_manifest = manifest_dict()
    leaking_manifest["required_material_roles"] = ["family-a-author-role"]
    leaking_manifest["material_generation_families"][0][
        "role_id"
    ] = "family-a-author-role"
    leaking = AssignmentProvenance.from_dict(leaking_manifest, registry)
    with pytest.raises(ProvenanceError, match="public projection"):
        leaking.to_public_dict(
            {"family-a": "authoring-panel-1", "family-b": "tested-panel-1"}
        )

    provenance = AssignmentProvenance.from_dict(manifest_dict(), registry)
    with pytest.raises(ProvenanceError, match="distinct"):
        provenance.to_public_dict(
            {"family-a": "Panel-One", "family-b": "ＰＡＮＥＬ－ＯＮＥ"}
        )


@pytest.mark.parametrize(
    "bypass_key",
    ["modelId", "model-id", "tested_provider", "material_generation_family_id"],
)
def test_privacy_canonicalizes_camel_and_separator_key_bypasses(
    bypass_key: str,
) -> None:
    packet = build_packet(raw_view(), ASSIGNMENT, RUBRIC)
    packet["view"]["task"][bypass_key] = "private"
    with pytest.raises(PacketPrivacyError, match="forbidden private field"):
        require_packet_privacy(packet)


def test_canticle_integral_float_matches_json_schema_and_canonicalizes_to_int() -> None:
    schemas, schema_registry = _schema_registry()
    fixture = {
        "result_schema": "canticle-graded-v1",
        "score": 1.0,
        "low_score_attribution": "deficient",
    }
    Draft202012Validator(
        schemas["canticle-graded-v1.schema.json"], registry=schema_registry
    ).validate(fixture)
    from results import validate_labeled_result

    normalized = validate_labeled_result(fixture)
    assert normalized["score"] == 1
    assert type(normalized["score"]) is int


def _schema_registry() -> tuple[dict[str, dict], Registry]:
    paths = sorted([*ROOT.glob("schemas/*.schema.json"), *ROOT.glob("rubrics/*.schema.json")])
    schemas = {path.name: json.loads(path.read_text(encoding="utf-8")) for path in paths}
    registry = Registry().with_resources(
        (schema["$id"], Resource.from_contents(schema)) for schema in schemas.values()
    )
    return schemas, registry


def test_json_schemas_reject_whitespace_duplicates_role_mismatch_and_bool_integer() -> None:
    schemas, schema_registry = _schema_registry()
    family_validator = Draft202012Validator(
        schemas["family-registry-v1.schema.json"], registry=schema_registry
    )
    whitespace = registry_config()
    whitespace["registry_version"] = "   "
    with pytest.raises(ValidationError):
        family_validator.validate(whitespace)
    duplicate = registry_config()
    duplicate["families"].append(copy.deepcopy(duplicate["families"][0]))
    with pytest.raises(ValidationError):
        family_validator.validate(duplicate)

    assignment_validator = Draft202012Validator(
        schemas["assignment-provenance-v1.schema.json"], registry=schema_registry
    )
    wrong_role = manifest_dict()
    wrong_role["material_generation_families"][0]["role_type"] = "tested_response"
    with pytest.raises(ValidationError):
        assignment_validator.validate(wrong_role)

    canticle_validator = Draft202012Validator(
        schemas["canticle-graded-v1.schema.json"], registry=schema_registry
    )
    with pytest.raises(ValidationError):
        canticle_validator.validate(
            {"result_schema": "canticle-graded-v1", "score": True, "low_score_attribution": "deficient"}
        )


def test_schema_plus_semantics_catches_normalized_and_cross_record_uniqueness() -> None:
    schemas, schema_registry = _schema_registry()
    family_validator = Draft202012Validator(
        schemas["family-registry-v1.schema.json"], registry=schema_registry
    )
    normalized_duplicate = {
        "registry_version": "v1",
        "families": [{"family_id": "Family-A"}, {"family_id": "ＦＡＭＩＬＹ－Ａ"}],
        "aliases": [],
    }
    family_validator.validate(normalized_duplicate)
    with pytest.raises(FamilyRegistryError):
        FamilyRegistry.from_config(normalized_duplicate)

    registry = FamilyRegistry.from_config(registry_config())
    duplicate_roles = manifest_dict()
    second = copy.deepcopy(duplicate_roles["material_generation_families"][0])
    second["raw_authoring_attestation"] = "A second record with the same role ID."
    duplicate_roles["material_generation_families"].append(second)
    with pytest.raises(ProvenanceError, match="role_overlap"):
        AssignmentProvenance.from_dict(duplicate_roles, registry)


def test_explicit_schema_plus_semantic_validation_entrypoints_fail_closed() -> None:
    from schema_semantics import (
        SchemaSemanticValidationError,
        validate_assignment_provenance_document,
        validate_family_registry_document,
    )

    registry = validate_family_registry_document(registry_config())
    assert registry.resolve("AUTHOR-MODEL") == "family-a"
    assert validate_assignment_provenance_document(
        manifest_dict(), registry
    ).tested_response.family_id == "family-b"

    collision = {
        "registry_version": "v1",
        "families": [{"family_id": "Family-A"}, {"family_id": "ＦＡＭＩＬＹ－Ａ"}],
        "aliases": [],
    }
    with pytest.raises(SchemaSemanticValidationError, match="duplicate_family_id"):
        validate_family_registry_document(collision)

    missing_role = manifest_dict(roles=[])
    with pytest.raises(SchemaSemanticValidationError, match="material_role_manifest"):
        validate_assignment_provenance_document(missing_role, registry)


def test_public_schema_enforces_resolution_specific_family_label() -> None:
    schemas, schema_registry = _schema_registry()
    validator = Draft202012Validator(
        schemas["public-assignment-provenance-v1.schema.json"], registry=schema_registry
    )
    registry = FamilyRegistry.from_config(registry_config())
    public = AssignmentProvenance.from_dict(manifest_dict(), registry).to_public_dict(
        {"family-a": "authoring-panel-1", "family-b": "tested-panel-1"}
    )
    validator.validate(public)
    public["tested_response"]["family_label"] = None
    with pytest.raises(ValidationError):
        validator.validate(public)


def test_judgment_schema_binds_rubric_to_result_schema() -> None:
    schemas, schema_registry = _schema_registry()
    validator = Draft202012Validator(
        schemas["judge-output-v1.schema.json"], registry=schema_registry
    )
    mismatched = envelope(
        result={"result_schema": "witness-pole-v1", "label": "gold"}
    )
    mismatched["rubric_id"] = "canticle-graded"
    with pytest.raises(ValidationError):
        validator.validate(mismatched)
