"""Canonical serialization helpers used by every PALTER artifact."""

import hashlib
import json


def canonical_json(value):
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def canonical_sha256(value):
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def canonical_jsonl_bytes(rows):
    return b"".join(
        canonical_json(row).encode("utf-8") + b"\n" for row in rows
    )
