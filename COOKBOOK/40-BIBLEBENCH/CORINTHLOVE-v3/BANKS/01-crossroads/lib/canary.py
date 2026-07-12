"""Deterministic UUIDv4-format canaries and private authoring seeds."""
from __future__ import annotations

from collections.abc import Mapping
import hashlib
from pathlib import Path
import re
import uuid


_UUID4_BODY = (
    r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}"
)
CANARY_RE = re.compile(rf"10CB3-01-{_UUID4_BODY}")
JSEED_RE = re.compile(rf"JSEED-{_UUID4_BODY}")


def deterministic_uuid4(label: str, namespace: str) -> str:
    """Derive stable bytes while forcing RFC-4122 variant and v4 bits."""
    if not isinstance(label, str) or not label:
        raise ValueError("UUID label must be non-empty text")
    if not isinstance(namespace, str) or not namespace:
        raise ValueError("UUID namespace must be non-empty text")
    raw = bytearray(hashlib.sha256(
        f"{namespace}\x00{label}".encode("utf-8")
    ).digest()[:16])
    raw[6] = (raw[6] & 0x0F) | 0x40
    raw[8] = (raw[8] & 0x3F) | 0x80
    value = uuid.UUID(bytes=bytes(raw))
    if value.version != 4 or value.variant != uuid.RFC_4122:
        raise AssertionError("deterministic UUID did not retain v4/variant bits")
    return str(value)


def canary_for(item_id: str) -> str:
    value = f"10CB3-01-{deterministic_uuid4(item_id, 'crossroads-canary-v1')}"
    if CANARY_RE.fullmatch(value) is None:
        raise AssertionError("generated canary failed format validation")
    return value


def judge_seed_for(item_id: str) -> str:
    """Return an item-bound issuance seed that is never a judge case ID."""
    value = f"JSEED-{deterministic_uuid4(item_id, 'crossroads-judge-seed-v1')}"
    if JSEED_RE.fullmatch(value) is None:
        raise AssertionError("generated judge seed failed format validation")
    return value


def update_registry(path: Path, mappings: Mapping) -> None:
    """Append only missing mappings; reject remaps and global collisions."""
    path = Path(path)
    if not isinstance(mappings, Mapping) or not mappings:
        raise ValueError("canary mappings must be a non-empty mapping")
    requested = {}
    item_to_canary = {}
    for canary, item_id in mappings.items():
        if not isinstance(canary, str) or CANARY_RE.fullmatch(canary) is None:
            raise ValueError(f"invalid CROSSROADS canary: {canary!r}")
        if not isinstance(item_id, str) or not item_id:
            raise ValueError("registry item IDs must be non-empty text")
        if canary in requested or item_id in item_to_canary:
            raise ValueError("requested registry mappings must be one-to-one")
        requested[canary] = item_id
        item_to_canary[item_id] = canary

    original = path.read_text(encoding="utf-8") if path.exists() else ""
    existing = {}
    existing_items = {}
    for line_number, raw in enumerate(original.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        pieces = raw.split("\t")
        if len(pieces) != 2 or not all(pieces):
            raise ValueError(f"malformed canary registry line {line_number}")
        canary, item_id = pieces
        if canary in existing and existing[canary] != item_id:
            raise ValueError(f"canary remap at registry line {line_number}")
        if item_id in existing_items and existing_items[item_id] != canary:
            raise ValueError(f"item remap at registry line {line_number}")
        existing[canary] = item_id
        existing_items[item_id] = canary

    for canary, item_id in requested.items():
        if canary in existing and existing[canary] != item_id:
            raise ValueError("canary is already bound to another item")
        if item_id in existing_items and existing_items[item_id] != canary:
            raise ValueError("item is already bound to another canary")
    missing = [(canary, item_id) for canary, item_id in requested.items()
               if canary not in existing]
    if not missing:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    prefix = original
    if prefix and not prefix.endswith("\n"):
        prefix += "\n"
    addition = "".join(
        f"{canary}\t{item_id}\n"
        for canary, item_id in sorted(missing, key=lambda pair: pair[1])
    )
    path.write_text(prefix + addition, encoding="utf-8")
