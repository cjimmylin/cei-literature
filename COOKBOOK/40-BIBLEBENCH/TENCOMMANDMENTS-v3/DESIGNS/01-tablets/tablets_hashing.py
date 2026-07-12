"""Canonical serialization and SHA-256 helpers for TABLETS artifacts."""

import hashlib
import json
from pathlib import Path


def canonical_json(value):
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def canonical_sha256(value, raw_bytes=False):
    if raw_bytes:
        if not isinstance(value, bytes):
            raise TypeError("raw_bytes hashing requires bytes")
        payload = value
    else:
        payload = canonical_json(value).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path):
    path = Path(path)
    return hashlib.sha256(path.read_bytes()).hexdigest()


__all__ = ["canonical_json", "canonical_sha256", "sha256_file"]
