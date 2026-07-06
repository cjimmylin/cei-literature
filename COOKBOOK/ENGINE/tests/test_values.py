"""Tests for the Schwartz-anchored value taxonomy (design 06 CRUX §3.1).

The 5 core values MUST anchor to an external taxonomy so the Priority
Fingerprint is a fingerprint of a *defined* hand (M1 fix). Anchors = the four
Schwartz higher-order values + one care/loyalty relational axis.
"""
from crux import values


SCHWARTZ_HIGHER_ORDER = {
    "self-transcendence",
    "self-enhancement",
    "openness-to-change",
    "conservation",
}
RELATIONAL_ANCHOR = "care-loyalty"


def test_exactly_five_core_values():
    assert len(values.CORE_VALUES) == 5


def test_each_value_has_name_anchor_and_clause():
    for v in values.CORE_VALUES:
        assert v.name and isinstance(v.name, str)
        assert v.schwartz_anchor in SCHWARTZ_HIGHER_ORDER | {RELATIONAL_ANCHOR}
        assert v.clause and isinstance(v.clause, str)


def test_anchors_cover_all_four_schwartz_plus_relational():
    anchors = {v.schwartz_anchor for v in values.CORE_VALUES}
    assert anchors == SCHWARTZ_HIGHER_ORDER | {RELATIONAL_ANCHOR}


def test_value_names_are_unique():
    names = [v.name for v in values.CORE_VALUES]
    assert len(names) == len(set(names))


def test_value_pairs_enumerates_ten_unique_unordered_pairs():
    pairs = values.value_pairs()
    assert len(pairs) == 10
    # unordered + unique
    as_sets = {frozenset(p) for p in pairs}
    assert len(as_sets) == 10
    # every pair is two DISTINCT known value names
    known = {v.name for v in values.CORE_VALUES}
    for p in pairs:
        assert len(set(p)) == 2
        assert set(p) <= known


def test_lookup_by_name_returns_the_anchor():
    v = values.by_name(values.CORE_VALUES[0].name)
    assert v is values.CORE_VALUES[0]
