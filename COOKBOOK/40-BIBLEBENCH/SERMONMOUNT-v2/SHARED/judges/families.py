"""Frozen, config-supplied canonical model-family registry."""
from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Dict, Mapping, Tuple
import unicodedata

from canonical import CanonicalSnapshot, content_hash


class FamilyRegistryError(ValueError):
    """The frozen registry is structurally invalid."""


class FamilyResolutionError(FamilyRegistryError):
    """A raw alias cannot be resolved exactly through the frozen table."""


def _nonempty_string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise FamilyRegistryError(f"{field}: expected a non-empty, unpadded string")
    return value


def normalize_family_identifier(value: Any, field: str = "family identifier") -> str:
    """Canonicalize a family ID/alias without guessing from substrings."""

    raw = _nonempty_string(value, field)
    normalized = unicodedata.normalize("NFKC", raw).casefold()
    if not normalized or normalized != normalized.strip():
        raise FamilyRegistryError(f"{field}: invalid after NFKC/casefold")
    return normalized


@dataclass(frozen=True)
class FamilyRegistry:
    """An immutable registry snapshot; it never guesses from provider/model text."""

    version: str
    registry_hash: str
    _snapshot: CanonicalSnapshot
    _family_ids: Tuple[str, ...]
    _aliases: Mapping[str, str]

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "FamilyRegistry":
        if not isinstance(config, Mapping):
            raise FamilyRegistryError("registry config must be an object")
        frozen = CanonicalSnapshot.capture(dict(config)).to_object()
        if not isinstance(frozen, dict):  # pragma: no cover - guarded by Mapping
            raise FamilyRegistryError("registry config must be an object")
        if set(frozen) != {"registry_version", "families", "aliases"}:
            raise FamilyRegistryError("registry config fields are not exact")
        version = _nonempty_string(frozen["registry_version"], "registry_version")

        family_rows = frozen["families"]
        if not isinstance(family_rows, list) or not family_rows:
            raise FamilyRegistryError("families: expected a non-empty array")
        family_ids = []
        seen_families = set()
        for index, row in enumerate(family_rows):
            if not isinstance(row, dict) or set(row) != {"family_id"}:
                raise FamilyRegistryError(f"families[{index}]: expected only family_id")
            family_id = normalize_family_identifier(
                row["family_id"], f"families[{index}].family_id"
            )
            if family_id in seen_families:
                raise FamilyRegistryError(f"duplicate_family_id:{family_id}")
            seen_families.add(family_id)
            family_ids.append(family_id)

        alias_rows = frozen["aliases"]
        if not isinstance(alias_rows, list):
            raise FamilyRegistryError("aliases: expected an array")
        aliases: Dict[str, str] = {}
        for index, row in enumerate(alias_rows):
            if not isinstance(row, dict) or set(row) != {"alias", "family_id"}:
                raise FamilyRegistryError(
                    f"aliases[{index}]: expected alias and family_id only"
                )
            alias = normalize_family_identifier(row["alias"], f"aliases[{index}].alias")
            family_id = normalize_family_identifier(
                row["family_id"], f"aliases[{index}].family_id"
            )
            if family_id not in seen_families:
                raise FamilyRegistryError(f"unknown_family_id:{family_id}")
            # Duplicate rows are multiply mapped even when they repeat one target.
            if alias in aliases:
                raise FamilyRegistryError(f"alias_collision:{alias}")
            if alias in seen_families and alias != family_id:
                raise FamilyRegistryError(
                    f"canonical_alias_collision:{alias}:maps_to:{family_id}"
                )
            aliases[alias] = family_id

        normalized_config = {
            "registry_version": version,
            "families": [{"family_id": family_id} for family_id in family_ids],
            "aliases": [
                {"alias": alias, "family_id": family_id}
                for alias, family_id in aliases.items()
            ],
        }
        snapshot = CanonicalSnapshot.capture(normalized_config)

        return cls(
            version=version,
            registry_hash=snapshot.sha256,
            _snapshot=snapshot,
            _family_ids=tuple(family_ids),
            _aliases=MappingProxyType(aliases),
        )

    def resolve(self, raw_alias: str) -> str:
        try:
            alias = normalize_family_identifier(raw_alias, "alias")
        except FamilyRegistryError as exc:
            raise FamilyResolutionError(str(exc)) from exc
        try:
            return self._aliases[alias]
        except KeyError as exc:
            raise FamilyResolutionError(f"unknown_alias:{raw_alias}") from exc

    def contains_family(self, family_id: str) -> bool:
        return family_id in self._family_ids

    @property
    def family_ids(self) -> Tuple[str, ...]:
        return self._family_ids

    def to_dict(self) -> dict:
        value = self._snapshot.to_object()
        if not isinstance(value, dict):  # pragma: no cover
            raise AssertionError("registry snapshot invariant")
        return value
