"""Exact JSON-tree validation and canonical hashing for SKIM P1."""

from collections.abc import Mapping as MappingABC
from collections.abc import Sequence as SequenceABC
import hashlib
import json
import math
import re
from types import MappingProxyType
from typing import Any, Mapping, Optional, Tuple


_SHA256_RE = re.compile(r"[0-9a-fA-F]{64}\Z")
_JSON_SAFE_INTEGER_MAX = 2**53 - 1


def _finite_real(value: Any) -> bool:
    if type(value) is int:
        return abs(value) <= _JSON_SAFE_INTEGER_MAX
    return type(value) is float and math.isfinite(value)


def _probability(value: Any) -> bool:
    return _finite_real(value) and 0.0 <= value <= 1.0


def _point_score(value: Any) -> bool:
    return _finite_real(value) and 0.0 <= value <= 100.0


def _nonblank_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _valid_sha256(value: Any) -> bool:
    return (
        isinstance(value, str)
        and _SHA256_RE.fullmatch(value) is not None
        and value.lower() != "0" * 64
    )


def _text_sequence(value: Any) -> Optional[Tuple[str, ...]]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(
        value, SequenceABC
    ):
        return None
    result = []
    for entry in value:
        if not isinstance(entry, str) or not entry or entry != entry.strip():
            return None
        result.append(entry)
    return tuple(result)


def _deep_freeze(value: Any) -> Any:
    if isinstance(value, MappingABC):
        return MappingProxyType({key: _deep_freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_deep_freeze(item) for item in value)
    if isinstance(value, tuple):
        return tuple(_deep_freeze(item) for item in value)
    return value


def _json_ready(value: Any) -> Any:
    if isinstance(value, MappingABC):
        if not all(type(key) is str for key in value):
            raise TypeError("canonical JSON object keys must be strings")
        return {key: _json_ready(item) for key, item in value.items()}
    if type(value) in (list, tuple):
        return [_json_ready(item) for item in value]
    if value is None or type(value) in (str, bool):
        return value
    if type(value) is int:
        if abs(value) > _JSON_SAFE_INTEGER_MAX:
            raise ValueError("canonical JSON integers must be IEEE-754 safe")
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise ValueError("canonical JSON floats must be finite")
        return value
    raise TypeError("value is not an exact JSON-compatible type")


def canonical_json(value: Any) -> str:
    """Return the canonical UTF-8 JSON representation used for hashes."""

    return json.dumps(
        _json_ready(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def canonical_sha256(value: Any) -> str:
    """Hash a JSON-compatible value using the frozen canonical encoding."""

    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _config_hash_paths(value: Any, path: Tuple[str, ...] = ()) -> Tuple[Tuple[str, ...], ...]:
    paths = []
    if isinstance(value, MappingABC):
        for key, item in value.items():
            if key == "config_sha256":
                paths.append(path + (key,))
            paths.extend(_config_hash_paths(item, path + (str(key),)))
    elif isinstance(value, SequenceABC) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        for index, item in enumerate(value):
            paths.extend(_config_hash_paths(item, path + (str(index),)))
    return tuple(paths)


def config_content_sha256(config: Mapping[str, Any]) -> str:
    """Hash a config after nulling its one canonical self-hash location."""

    if not isinstance(config, MappingABC):
        raise TypeError("config must be a mapping")
    if _config_hash_paths(config) != (("artifact_hashes", "config_sha256"),):
        raise ValueError("config must have one artifact_hashes.config_sha256 location")
    payload = json.loads(canonical_json(config))
    payload["artifact_hashes"]["config_sha256"] = None
    return canonical_sha256(payload)


def validate_config_content_sha256(config: Any) -> bool:
    """Fail closed for absent, stale, zero, or duplicated config self-hashes."""

    if not isinstance(config, MappingABC):
        return False
    try:
        stored = config["artifact_hashes"]["config_sha256"]
        return _valid_sha256(stored) and stored.lower() == config_content_sha256(config)
    except Exception:
        return False


def _json_tree_is_finite(value: Any) -> bool:
    try:
        _json_ready(value)
    except Exception:
        return False
    return True

__all__ = [
    "canonical_json",
    "canonical_sha256",
    "config_content_sha256",
    "validate_config_content_sha256",
]
