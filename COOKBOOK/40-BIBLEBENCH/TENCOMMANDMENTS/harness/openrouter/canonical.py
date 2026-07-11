"""Bounded canonical JSON and SHA-256 helpers for OpenRouter artifacts."""

from hashlib import sha256
from typing import Any, Dict

from TENCOMMANDMENTS.harness.custody_stack.schema import (
    SchemaValidationError,
    canonical_json as _canonical_json,
    strict_json_loads,
    valid_sha256,
)


class CanonicalJSONError(ValueError):
    """Raised when a value is not bounded exact canonical JSON."""


def canonical_json(value: Any) -> str:
    """Return sorted, compact, UTF-8-safe JSON for one exact JSON value."""

    try:
        return _canonical_json(value)
    except SchemaValidationError as exc:
        raise CanonicalJSONError(str(exc)) from exc


def canonical_json_bytes(value: Any) -> bytes:
    """Return canonical JSON encoded as strict UTF-8 bytes."""

    return canonical_json(value).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    """Hash exact bytes with SHA-256."""

    if type(value) is not bytes:
        raise TypeError("SHA-256 input must be exact bytes")
    return sha256(value).hexdigest()


def canonical_sha256(value: Any) -> str:
    """Hash the canonical JSON encoding of one exact JSON value."""

    return sha256_bytes(canonical_json_bytes(value))


def is_sha256(value: Any) -> bool:
    """Return whether *value* is lowercase SHA-256 hexadecimal text."""

    return valid_sha256(value)


def load_canonical_json(raw: bytes) -> Dict[str, Any]:
    """Decode one canonical JSON object, rejecting alternate encodings."""

    if type(raw) is not bytes:
        raise CanonicalJSONError("canonical JSON input must be exact bytes")
    try:
        text = raw.decode("utf-8", errors="strict")
        value = strict_json_loads(text)
        encoded = canonical_json_bytes(value)
    except (UnicodeError, SchemaValidationError, CanonicalJSONError) as exc:
        raise CanonicalJSONError("invalid canonical JSON: %s" % exc) from exc
    if type(value) is not dict:
        raise CanonicalJSONError("canonical JSON root must be an object")
    if encoded != raw:
        raise CanonicalJSONError("JSON object is not canonical")
    return value


__all__ = [
    "CanonicalJSONError",
    "canonical_json",
    "canonical_json_bytes",
    "canonical_sha256",
    "is_sha256",
    "load_canonical_json",
    "sha256_bytes",
]
