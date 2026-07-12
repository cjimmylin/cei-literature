"""Hash-frozen persistent judge identity roster validation."""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import hashlib
import json
import re
from types import MappingProxyType


_UUID4_BODY = (
    r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}"
)
JUDGE_RE = re.compile(rf"^JUDGE-{_UUID4_BODY}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
FAMILY_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
ROLES = ("raw", "adjudicator")
SCHEMA_VERSION = "crossroads-judge-roster-v1"
_DOCUMENT_FIELDS = {
    "schema_version", "provenance", "human_validation_status", "judges",
}
_JUDGE_FIELDS = {
    "judge_id", "family", "provider", "identity_kind",
    "exact_model_version", "human_identity_class", "prompt_sha256",
    "configuration_sha256", "role",
}


def _canonical_bytes(value: object) -> bytes:
    try:
        return json.dumps(
            value, sort_keys=True, separators=(",", ":"),
            ensure_ascii=False, allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError):
        raise ValueError("judge roster must be canonical JSON data") from None


def canonical_roster_sha256(document: Mapping) -> str:
    if not isinstance(document, Mapping):
        raise TypeError("judge roster document must be a mapping")
    return hashlib.sha256(_canonical_bytes(document)).hexdigest()


def _nonempty(value: object, label: str) -> str:
    if type(value) is not str or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value


class FrozenJudgeRoster:
    """An immutable, digest-bound lookup for persistent judge identities."""

    __slots__ = (
        "_identities", "sha256", "provenance", "human_validation_status",
        "_frozen",
    )

    def __setattr__(self, name, value):
        if getattr(self, "_frozen", False):
            raise AttributeError("FrozenJudgeRoster is immutable")
        object.__setattr__(self, name, value)

    def __init__(self, document: Mapping, *, expected_sha256: str) -> None:
        if type(expected_sha256) is not str or SHA256_RE.fullmatch(
                expected_sha256) is None:
            raise ValueError("expected roster hash must be lowercase SHA-256")
        if not isinstance(document, Mapping):
            raise TypeError("judge roster document must be a mapping")
        snapshot = deepcopy(dict(document))
        digest = canonical_roster_sha256(snapshot)
        if digest != expected_sha256:
            raise ValueError("judge roster hash mismatch; roster mutation rejected")
        if type(snapshot) is not dict or set(snapshot) != _DOCUMENT_FIELDS:
            raise ValueError("judge roster document fields differ")
        if snapshot["schema_version"] != SCHEMA_VERSION:
            raise ValueError("judge roster schema version differs")
        provenance = _nonempty(snapshot["provenance"], "roster provenance")
        human_status = _nonempty(
            snapshot["human_validation_status"], "human validation status",
        )
        judges = snapshot["judges"]
        if type(judges) is not list or not judges:
            raise ValueError("judge roster must contain at least one identity")
        identities: dict[str, MappingProxyType] = {}
        for row in judges:
            if type(row) is not dict or set(row) != _JUDGE_FIELDS:
                raise ValueError("judge roster identity fields differ")
            judge_id = row["judge_id"]
            if type(judge_id) is not str or JUDGE_RE.fullmatch(judge_id) is None:
                raise ValueError("judge_id must be persistent JUDGE-<UUIDv4>")
            if judge_id in identities:
                raise ValueError("rebound or duplicate JUDGE identity in roster")
            family = row["family"]
            provider = row["provider"]
            if type(family) is not str or FAMILY_RE.fullmatch(family) is None:
                raise ValueError("judge family must be a normalized identifier")
            if type(provider) is not str or FAMILY_RE.fullmatch(provider) is None:
                raise ValueError("judge provider must be a normalized identifier")
            if row["role"] not in ROLES:
                raise ValueError("judge role must be raw or adjudicator")
            for field in ("prompt_sha256", "configuration_sha256"):
                if type(row[field]) is not str or SHA256_RE.fullmatch(
                        row[field]) is None:
                    raise ValueError(f"judge {field} must be lowercase SHA-256")
            model = row["exact_model_version"]
            human = row["human_identity_class"]
            if row["identity_kind"] == "model":
                valid_identity = (
                    type(model) is str and bool(model.strip()) and human is None
                )
            elif row["identity_kind"] == "human":
                valid_identity = (
                    model is None and type(human) is str and bool(human.strip())
                )
            else:
                valid_identity = False
            if not valid_identity:
                raise ValueError(
                    "judge requires exactly one identity binding matching identity_kind"
                )
            identities[judge_id] = MappingProxyType(deepcopy(row))
        self._identities = MappingProxyType(identities)
        self.sha256 = digest
        self.provenance = provenance
        self.human_validation_status = human_status
        self._frozen = True

    @classmethod
    def from_document(
        cls, document: Mapping, *, expected_sha256: str,
    ) -> "FrozenJudgeRoster":
        return cls(document, expected_sha256=expected_sha256)

    def lookup(self, judge_id: str, *, required_role: str) -> Mapping:
        if required_role not in ROLES:
            raise ValueError("required judge role differs")
        if type(judge_id) is not str or JUDGE_RE.fullmatch(judge_id) is None:
            raise ValueError("judge lookup requires JUDGE-<UUIDv4>")
        try:
            binding = self._identities[judge_id]
        except KeyError:
            raise ValueError("unknown JUDGE identity in frozen roster") from None
        if binding["role"] != required_role:
            raise ValueError("JUDGE role mismatch in frozen roster")
        return binding
