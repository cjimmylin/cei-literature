"""Contract tests for benchmark-neutral canonical JSON helpers."""

from decimal import Decimal
from hashlib import sha256

import pytest


def api():
    from TENCOMMANDMENTS.harness.openrouter import canonical

    return canonical


def test_canonical_json_bytes_are_sorted_compact_utf8_and_hashable():
    module = api()
    value = {"z": [True, None], "a": "café"}
    expected = '{"a":"café","z":[true,null]}'.encode("utf-8")

    assert module.canonical_json_bytes(value) == expected
    assert module.canonical_json(value) == expected.decode("utf-8")
    assert module.canonical_sha256(value) == sha256(expected).hexdigest()
    assert module.sha256_bytes(expected) == sha256(expected).hexdigest()
    assert module.is_sha256(module.canonical_sha256(value)) is True
    assert module.is_sha256(module.canonical_sha256(value).upper()) is False


def test_load_canonical_json_rejects_noncanonical_duplicate_and_unsafe_values():
    module = api()

    assert module.load_canonical_json(b'{"a":1,"b":2}') == {"a": 1, "b": 2}
    with pytest.raises(module.CanonicalJSONError, match="canonical"):
        module.load_canonical_json(b'{"b":2, "a":1}')
    with pytest.raises(module.CanonicalJSONError, match="duplicate|JSON"):
        module.load_canonical_json(b'{"a":1,"a":2}')
    with pytest.raises(module.CanonicalJSONError):
        module.canonical_json({"amount": Decimal("0.01")})
    with pytest.raises(module.CanonicalJSONError):
        module.canonical_json({"amount": float("nan")})
