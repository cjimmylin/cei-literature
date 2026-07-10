from decimal import Decimal
from fractions import Fraction
import json

import pytest

from conftest import CustomReal
import skim_constants as constants
import skim_hashing as hashing


def test_canonical_json_rejects_unsafe_or_unsupported_values_recursively():
    invalid_values = (
        2**53,
        -(2**53),
        10**10000,
        Fraction(1, 2),
        Decimal("0.5"),
        CustomReal(0.5),
        float("nan"),
        float("inf"),
        object(),
        {"nested": object()},
        {1: "non-string-key"},
    )
    for value in invalid_values:
        with pytest.raises((TypeError, ValueError, OverflowError)):
            hashing.canonical_json(value)
        with pytest.raises((TypeError, ValueError, OverflowError)):
            hashing.canonical_sha256(value)

    supported = {
        "safe_max": 2**53 - 1,
        "safe_min": -(2**53 - 1),
        "tuple": (1, 2.5),
        "frozen": constants.ITEM_RETENTION_RULES,
    }
    assert json.loads(hashing.canonical_json(supported))["safe_max"] == 2**53 - 1
    assert len(hashing.canonical_sha256(supported)) == 64
