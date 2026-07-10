"""Immutable canonical JSON snapshots and orthogonal SHA-256 hash domains.

The encoding is deliberately small and explicit: UTF-8 JSON, sorted object keys, no
insignificant whitespace, and no non-finite numbers.  Hash-domain functions reject their
own output field rather than silently deleting it.
"""
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from typing import Any, Mapping, Sequence, Union


JsonValue = Union[None, bool, int, float, str, list, dict]
PACKET_FIELDS = {
    "schema_version",
    "assignment_id",
    "assignment_hash",
    "evidence_hash",
    "rubric_hash",
    "criteria_hash",
    "rubric",
    "view",
    "packet_hash",
}
RUBRIC_FIELDS = {"rubric_id", "rubric_version", "criteria"}
VIEW_FIELDS = {"parent_evidence_hash", "transform", "task", "response"}


class CanonicalizationError(ValueError):
    """The value cannot be represented by this canonical contract."""


def _validate_json(value: Any, path: str = "$") -> None:
    if value is None or isinstance(value, (bool, str)):
        return
    if isinstance(value, int):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise CanonicalizationError(f"{path}: non-finite numbers are forbidden")
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            _validate_json(child, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, child in value.items():
            if not isinstance(key, str):
                raise CanonicalizationError(f"{path}: JSON object keys must be strings")
            _validate_json(child, f"{path}.{key}")
        return
    raise CanonicalizationError(f"{path}: unsupported JSON type {type(value).__name__}")


def canonical_bytes(value: Any) -> bytes:
    """Return the stack's deterministic UTF-8 JSON representation."""

    _validate_json(value)
    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:  # defensive parity with the pre-check
        raise CanonicalizationError(str(exc)) from exc


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


@dataclass(frozen=True)
class CanonicalSnapshot:
    """Mutation-proof canonical bytes and their digest."""

    raw: bytes
    sha256: str

    @classmethod
    def capture(cls, value: Any) -> "CanonicalSnapshot":
        raw = canonical_bytes(value)
        return cls(raw=raw, sha256=_sha256(raw))

    def to_object(self) -> JsonValue:
        # json.loads creates a fresh object on every call, so callers cannot mutate us.
        return json.loads(self.raw.decode("utf-8"))


def source_hash(value: Union[str, bytes]) -> str:
    """Hash exact source bytes without JSON normalization."""

    if isinstance(value, str):
        raw = value.encode("utf-8")
    elif isinstance(value, bytes):
        raw = value
    else:
        raise CanonicalizationError("source must be str or bytes")
    return _sha256(raw)


def _domain_hash(value: Any, own_field: str) -> str:
    if isinstance(value, Mapping) and own_field in value:
        raise CanonicalizationError(
            f"{own_field}: self-referential hash fields are forbidden"
        )
    return _sha256(canonical_bytes(value))


def content_hash(value: Any) -> str:
    return _domain_hash(value, "content_hash")


def evidence_hash(value: Any) -> str:
    return _domain_hash(value, "evidence_hash")


def assignment_hash(value: Any) -> str:
    return _domain_hash(value, "assignment_hash")


def rubric_hash(value: Any) -> str:
    return _domain_hash(value, "rubric_hash")


def _packet_digest(packet_without_hash: Mapping[str, Any]) -> str:
    if "packet_hash" in packet_without_hash:
        raise CanonicalizationError(
            "packet_hash: self-referential hash fields are forbidden"
        )
    return _sha256(canonical_bytes(dict(packet_without_hash)))


def _validate_rubric_envelope(rubric: Mapping[str, Any]) -> None:
    if not isinstance(rubric, Mapping) or set(rubric) != RUBRIC_FIELDS:
        raise CanonicalizationError("rubric envelope fields are not exact")
    for field in ("rubric_id", "rubric_version"):
        if not isinstance(rubric[field], str) or not rubric[field].strip():
            raise CanonicalizationError(f"rubric.{field} must be nonblank")
    if not isinstance(rubric["criteria"], Mapping):
        raise CanonicalizationError("rubric criteria must be an object")


def build_packet(
    view: Mapping[str, Any],
    private_assignment: Mapping[str, Any],
    rubric: Mapping[str, Any],
    *,
    parent_view: Mapping[str, Any] = None,
    forbidden_values: Sequence[str] = (),
    identity_tokens: Mapping[str, Sequence[str]] = None,
) -> dict:
    """Build a judge packet whose four hash domains remain independently auditable."""

    view_copy = CanonicalSnapshot.capture(dict(view)).to_object()
    assignment_copy = CanonicalSnapshot.capture(dict(private_assignment)).to_object()
    rubric_copy = CanonicalSnapshot.capture(dict(rubric)).to_object()
    if not isinstance(view_copy, dict) or set(view_copy) != VIEW_FIELDS:
        raise CanonicalizationError("view envelope fields are not exact")
    _validate_rubric_envelope(rubric_copy)
    _validate_view_lineage(view_copy, parent_view, identity_tokens)
    assignment_id = assignment_copy.get("assignment_id")
    if not isinstance(assignment_id, str) or not assignment_id:
        raise CanonicalizationError("private assignment requires a non-empty assignment_id")
    criteria = rubric_copy.get("criteria")
    if not isinstance(criteria, dict):
        raise CanonicalizationError("rubric requires a criteria object")

    packet = {
        "schema_version": "judge-transcript-v1",
        "assignment_id": assignment_id,
        "assignment_hash": assignment_hash(assignment_copy),
        "evidence_hash": evidence_hash(view_copy),
        "rubric_hash": rubric_hash(rubric_copy),
        "criteria_hash": content_hash(criteria),
        "rubric": rubric_copy,
        "view": view_copy,
    }
    packet["packet_hash"] = _packet_digest(packet)
    from privacy import require_packet_privacy

    require_packet_privacy(packet, forbidden_values=forbidden_values)
    return packet


def _validate_view_lineage(
    view: Mapping[str, Any],
    parent_view: Mapping[str, Any] = None,
    identity_tokens: Mapping[str, Sequence[str]] = None,
) -> None:
    if set(view) != VIEW_FIELDS:
        raise CanonicalizationError("view envelope fields are not exact")
    if not isinstance(view.get("task"), Mapping) or not isinstance(
        view.get("response"), Mapping
    ):
        raise CanonicalizationError("view task/response must be objects")
    transform = view.get("transform")
    parent_hash = view.get("parent_evidence_hash")
    if transform is None:
        if parent_hash is not None:
            raise CanonicalizationError("raw view must have null parent_evidence_hash")
        if parent_view is not None:
            raise CanonicalizationError("raw view does not accept parent_view")
        return
    if parent_view is None:
        raise CanonicalizationError("transformed view requires parent_view")
    from transforms import IdentityMaskError, validate_transformed_view

    try:
        validate_transformed_view(
            view, parent_view, identity_tokens=identity_tokens
        )
    except IdentityMaskError as exc:
        raise CanonicalizationError(f"transform authorization failed: {exc}") from exc


def verify_packet(
    packet: Mapping[str, Any],
    private_assignment: Mapping[str, Any],
    *,
    parent_view: Mapping[str, Any] = None,
    forbidden_values: Sequence[str] = (),
    identity_tokens: Mapping[str, Sequence[str]] = None,
) -> bool:
    """Recompute every packet linkage and fail closed on the first mismatch."""

    packet_copy = CanonicalSnapshot.capture(dict(packet)).to_object()
    if not isinstance(packet_copy, dict):  # pragma: no cover - Mapping already implies this
        raise CanonicalizationError("packet must be an object")
    if set(packet_copy) != PACKET_FIELDS:
        raise CanonicalizationError("packet envelope fields are not exact")
    if packet_copy.get("schema_version") != "judge-transcript-v1":
        raise CanonicalizationError("unsupported schema_version")
    from privacy import require_packet_privacy

    require_packet_privacy(packet_copy, forbidden_values=forbidden_values)
    private_copy = CanonicalSnapshot.capture(dict(private_assignment)).to_object()
    if not isinstance(packet_copy.get("assignment_id"), str) or not packet_copy[
        "assignment_id"
    ].strip():
        raise CanonicalizationError("assignment_id must be nonblank")
    if packet_copy.get("assignment_id") != private_copy.get("assignment_id"):
        raise CanonicalizationError("assignment_id does not match private assignment")

    expected_evidence = evidence_hash(packet_copy.get("view"))
    if packet_copy.get("evidence_hash") != expected_evidence:
        raise CanonicalizationError("evidence_hash mismatch")
    expected_assignment = assignment_hash(private_copy)
    if packet_copy.get("assignment_hash") != expected_assignment:
        raise CanonicalizationError("assignment_hash mismatch")
    rubric = packet_copy.get("rubric")
    _validate_rubric_envelope(rubric)
    _validate_view_lineage(packet_copy["view"], parent_view, identity_tokens)
    expected_rubric = rubric_hash(rubric)
    if packet_copy.get("rubric_hash") != expected_rubric:
        raise CanonicalizationError("rubric_hash mismatch")
    if not isinstance(rubric.get("criteria"), dict):
        raise CanonicalizationError("rubric criteria missing")
    expected_criteria = content_hash(rubric["criteria"])
    if packet_copy.get("criteria_hash") != expected_criteria:
        raise CanonicalizationError("criteria_hash mismatch")

    supplied_packet_hash = packet_copy.pop("packet_hash", None)
    if not isinstance(supplied_packet_hash, str):
        raise CanonicalizationError("packet_hash missing")
    if supplied_packet_hash != _packet_digest(packet_copy):
        raise CanonicalizationError("packet_hash mismatch")
    return True
