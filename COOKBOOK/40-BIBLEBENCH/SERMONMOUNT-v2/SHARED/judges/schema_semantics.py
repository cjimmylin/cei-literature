"""Combined JSON-Schema and cross-record semantic validation entrypoints."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource

from families import FamilyRegistry, FamilyRegistryError
from provenance import AssignmentProvenance, ProvenanceError


class SchemaSemanticValidationError(ValueError):
    """A document failed structural schema or nonlocal semantic constraints."""


ROOT = Path(__file__).resolve().parent


def _schemas() -> tuple[dict, Registry]:
    paths = sorted([*ROOT.glob("schemas/*.schema.json"), *ROOT.glob("rubrics/*.schema.json")])
    schemas = {
        path.name: json.loads(path.read_text(encoding="utf-8")) for path in paths
    }
    registry = Registry().with_resources(
        (schema["$id"], Resource.from_contents(schema)) for schema in schemas.values()
    )
    return schemas, registry


def _validate_schema(name: str, value: Mapping[str, Any]) -> None:
    schemas, registry = _schemas()
    try:
        Draft202012Validator(schemas[name], registry=registry).validate(value)
    except ValidationError as exc:
        raise SchemaSemanticValidationError(f"schema_validation:{exc.message}") from exc


def validate_family_registry_document(value: Mapping[str, Any]) -> FamilyRegistry:
    """Validate local shape, then NFKC collisions and family/alias references."""

    _validate_schema("family-registry-v1.schema.json", value)
    try:
        return FamilyRegistry.from_config(value)
    except FamilyRegistryError as exc:
        raise SchemaSemanticValidationError(str(exc)) from exc


def validate_assignment_provenance_document(
    value: Mapping[str, Any], registry: FamilyRegistry
) -> AssignmentProvenance:
    """Validate local shape, then role uniqueness/type/family cross-record links."""

    _validate_schema("assignment-provenance-v1.schema.json", value)
    try:
        provenance = AssignmentProvenance.from_dict(value, registry)
    except (ProvenanceError, FamilyRegistryError) as exc:
        raise SchemaSemanticValidationError(str(exc)) from exc
    required = set(provenance.required_material_roles)
    present = {record.role_id for record in provenance.material_generation_families}
    if required != present:
        raise SchemaSemanticValidationError(
            "material_role_manifest_mismatch:"
            f"missing={sorted(required - present)}:extra={sorted(present - required)}"
        )
    return provenance
