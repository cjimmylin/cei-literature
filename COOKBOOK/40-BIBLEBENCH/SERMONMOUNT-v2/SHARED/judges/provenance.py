"""Immutable role-family provenance used by private judge assignment."""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping, Optional, Tuple

from canonical import CanonicalSnapshot
from families import FamilyRegistry, normalize_family_identifier


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class ProvenanceError(ValueError):
    """A provenance record violates the shared private-record contract."""


class ResolutionStatus(str, Enum):
    RESOLVED = "resolved"
    UNRESOLVED = "unresolved"
    HUMAN_ONLY = "human_only"


class RoleType(str, Enum):
    MATERIAL_GENERATION = "material_generation"
    TESTED_RESPONSE = "tested_response"


def _required_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProvenanceError(f"{field}: expected non-empty text")
    return value


def _hash(value: Any, field: str) -> str:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ProvenanceError(f"{field}: expected lowercase SHA-256")
    return value


@dataclass(frozen=True)
class RoleFamilyProvenance:
    """One material-generation or tested-response role and its raw attestation."""

    role_id: str
    role_type: RoleType
    raw_model_alias: Optional[str]
    raw_authoring_attestation: str
    family_id: Optional[str]
    resolution_status: ResolutionStatus
    source_hash: str
    content_hash: str
    _snapshot: CanonicalSnapshot

    @classmethod
    def from_dict(
        cls, value: Mapping[str, Any], registry: FamilyRegistry
    ) -> "RoleFamilyProvenance":
        if not isinstance(value, Mapping):
            raise ProvenanceError("role provenance must be an object")
        snapshot = CanonicalSnapshot.capture(dict(value))
        raw = snapshot.to_object()
        expected = {
            "role_id",
            "role_type",
            "raw_model_alias",
            "raw_authoring_attestation",
            "family_id",
            "resolution_status",
            "source_hash",
            "content_hash",
            "provenance",
        }
        if not isinstance(raw, dict) or set(raw) != expected:
            raise ProvenanceError("role provenance fields are not exact")
        role_id = _required_text(raw["role_id"], "role_id")
        try:
            role_type = RoleType(raw["role_type"])
        except (TypeError, ValueError) as exc:
            raise ProvenanceError("role_type: invalid") from exc
        try:
            status = ResolutionStatus(raw["resolution_status"])
        except (TypeError, ValueError) as exc:
            raise ProvenanceError("resolution_status: invalid") from exc
        attestation = _required_text(
            raw["raw_authoring_attestation"], "raw_authoring_attestation"
        )
        source = _hash(raw["source_hash"], "source_hash")
        content = _hash(raw["content_hash"], "content_hash")
        if not isinstance(raw["provenance"], dict):
            raise ProvenanceError("provenance: expected object")

        alias = raw["raw_model_alias"]
        family_id = raw["family_id"]
        if status is ResolutionStatus.RESOLVED:
            if not isinstance(alias, str) or not alias:
                raise ProvenanceError("resolved role requires raw_model_alias")
            if not isinstance(family_id, str) or not family_id:
                raise ProvenanceError("resolved role requires family_id")
            try:
                family_id = normalize_family_identifier(family_id, "family_id")
            except ValueError as exc:
                raise ProvenanceError(str(exc)) from exc
            resolved = registry.resolve(alias)
            if resolved != family_id:
                raise ProvenanceError(
                    f"family_mismatch:{family_id}:registry_resolves:{resolved}"
                )
        elif status is ResolutionStatus.UNRESOLVED:
            if alias is not None and (not isinstance(alias, str) or not alias):
                raise ProvenanceError("unresolved raw_model_alias must be null or non-empty")
            if family_id is not None:
                raise ProvenanceError("unresolved role cannot assert family_id")
        else:  # explicit non-model provenance
            if alias is not None or family_id is not None:
                raise ProvenanceError("human_only role cannot borrow model alias/family")

        raw["family_id"] = family_id
        snapshot = CanonicalSnapshot.capture(raw)
        return cls(
            role_id=role_id,
            role_type=role_type,
            raw_model_alias=alias,
            raw_authoring_attestation=attestation,
            family_id=family_id,
            resolution_status=status,
            source_hash=source,
            content_hash=content,
            _snapshot=snapshot,
        )

    def to_dict(self) -> dict:
        value = self._snapshot.to_object()
        if not isinstance(value, dict):  # pragma: no cover
            raise AssertionError("role snapshot invariant")
        return value


@dataclass(frozen=True)
class AssignmentProvenance:
    """Private exclusion inputs with a separate anonymized public projection."""

    schema_version: str
    registry_version: str
    registry_hash: str
    required_material_roles: Tuple[str, ...]
    material_generation_families: Tuple[RoleFamilyProvenance, ...]
    tested_response: RoleFamilyProvenance

    @classmethod
    def from_dict(
        cls, value: Mapping[str, Any], registry: FamilyRegistry
    ) -> "AssignmentProvenance":
        if not isinstance(value, Mapping):
            raise ProvenanceError("assignment provenance must be an object")
        raw = CanonicalSnapshot.capture(dict(value)).to_object()
        expected = {
            "schema_version",
            "registry_version",
            "required_material_roles",
            "material_generation_families",
            "tested_response",
        }
        if not isinstance(raw, dict) or set(raw) != expected:
            raise ProvenanceError("assignment provenance fields are not exact")
        if raw["schema_version"] != "assignment-provenance-v1":
            raise ProvenanceError("schema_version: unsupported")
        if raw["registry_version"] != registry.version:
            raise ProvenanceError("registry_version mismatch")
        required = raw["required_material_roles"]
        if not isinstance(required, list):
            raise ProvenanceError("required_material_roles: expected array")
        required_roles = tuple(
            _required_text(role_id, "required_material_roles[]") for role_id in required
        )
        if len(required_roles) != len(set(required_roles)):
            raise ProvenanceError("role_overlap: duplicate required material role")

        material_raw = raw["material_generation_families"]
        if not isinstance(material_raw, list):
            raise ProvenanceError("material_generation_families: expected array")
        material = tuple(
            RoleFamilyProvenance.from_dict(row, registry) for row in material_raw
        )
        for record in material:
            if record.role_type is not RoleType.MATERIAL_GENERATION:
                raise ProvenanceError("material role has wrong role_type")
        material_ids = tuple(record.role_id for record in material)
        if len(material_ids) != len(set(material_ids)):
            raise ProvenanceError("role_overlap: duplicate material role")

        tested = RoleFamilyProvenance.from_dict(raw["tested_response"], registry)
        if tested.role_type is not RoleType.TESTED_RESPONSE:
            raise ProvenanceError("tested_response has wrong role_type")
        if tested.role_id in set(material_ids):
            raise ProvenanceError("role_overlap: tested response and material role")
        return cls(
            schema_version="assignment-provenance-v1",
            registry_version=registry.version,
            registry_hash=registry.registry_hash,
            required_material_roles=required_roles,
            material_generation_families=material,
            tested_response=tested,
        )

    def to_dict(self) -> dict:
        return {
            "schema_version": self.schema_version,
            "registry_version": self.registry_version,
            "required_material_roles": list(self.required_material_roles),
            "material_generation_families": [
                record.to_dict() for record in self.material_generation_families
            ],
            "tested_response": self.tested_response.to_dict(),
        }

    def to_public_dict(self, family_labels: Mapping[str, str]) -> dict:
        """Anonymize family identities and omit raw private attestations/provenance."""

        used_family_ids = {
            record.family_id
            for record in (*self.material_generation_families, self.tested_response)
            if record.resolution_status is ResolutionStatus.RESOLVED
        }
        private_names = {
            unicodedata.normalize("NFKC", value).casefold()
            for record in (*self.material_generation_families, self.tested_response)
            for value in (record.family_id, record.raw_model_alias)
            if isinstance(value, str)
        }
        labels = {}
        for family_id in used_family_ids:
            label = family_labels.get(family_id)
            normalized_label = (
                unicodedata.normalize("NFKC", label).casefold()
                if isinstance(label, str)
                else None
            )
            if (
                not isinstance(label, str)
                or not label.strip()
                or any(private in normalized_label for private in private_names)
            ):
                raise ProvenanceError(
                    f"anonymized family label missing/invalid for {family_id}"
                )
            labels[family_id] = label
        normalized_labels = {
            unicodedata.normalize("NFKC", label).casefold()
            for label in labels.values()
        }
        if len(normalized_labels) != len(labels):
            raise ProvenanceError("anonymized family labels must remain distinct")

        def public_role(record: RoleFamilyProvenance) -> dict:
            if record.resolution_status is ResolutionStatus.RESOLVED:
                family_label = labels[record.family_id]
            elif record.resolution_status is ResolutionStatus.HUMAN_ONLY:
                family_label = "human-only"
            else:
                family_label = None
            return {
                "role_id": record.role_id,
                "role_type": record.role_type.value,
                "family_label": family_label,
                "resolution_status": record.resolution_status.value,
                "source_hash": record.source_hash,
                "content_hash": record.content_hash,
            }

        public = {
            "schema_version": "public-assignment-provenance-v1",
            "registry_commitment": self.registry_hash,
            "required_material_roles": list(self.required_material_roles),
            "material_generation_families": [
                public_role(record) for record in self.material_generation_families
            ],
            "tested_response": public_role(self.tested_response),
        }

        def scan(value: Any, path: str = "$") -> None:
            if isinstance(value, Mapping):
                for key, child in value.items():
                    normalized_key = unicodedata.normalize("NFKC", key).casefold()
                    if any(secret in normalized_key for secret in private_names):
                        raise ProvenanceError(
                            f"public projection leaks private identifier at {path}.{key}"
                        )
                    scan(child, f"{path}.{key}")
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    scan(child, f"{path}[{index}]")
            elif isinstance(value, str):
                normalized_value = unicodedata.normalize("NFKC", value).casefold()
                if any(secret in normalized_value for secret in private_names):
                    raise ProvenanceError(
                        f"public projection leaks private identifier at {path}"
                    )

        scan(public)
        return public
