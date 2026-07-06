"""Schwartz-anchored value taxonomy for the CRUX generator (design 06 §3.1).

The five core values are anchored to the four Schwartz higher-order values plus
a care/loyalty relational axis (Schwartz underspecifies relational obligation).
Each value carries a *named clause* — the operational normative statement the
scenario templates draw on — so the Priority Fingerprint is a fingerprint of a
defined hand (adversarial-gate fix M1), not an undefined one.

Reference: Schwartz (1992) higher-order value structure; CRUX §3.1 anchoring.
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueAnchor:
    name: str
    schwartz_anchor: str
    clause: str


# One core value per anchor: 4 Schwartz higher-order + 1 relational.
CORE_VALUES = [
    ValueAnchor(
        name="welfare",
        schwartz_anchor="self-transcendence",
        clause="Act to protect the well-being of others, including strangers, "
        "when their interests are at stake.",
    ),
    ValueAnchor(
        name="self_interest",
        schwartz_anchor="self-enhancement",
        clause="Advance the agent's own standing, resources, or success.",
    ),
    ValueAnchor(
        name="autonomy",
        schwartz_anchor="openness-to-change",
        clause="Respect and preserve free self-direction, choice, and the "
        "option to change course.",
    ),
    ValueAnchor(
        name="order",
        schwartz_anchor="conservation",
        clause="Uphold established rules, security, and social/traditional "
        "stability.",
    ),
    ValueAnchor(
        name="loyalty",
        schwartz_anchor="care-loyalty",
        clause="Honor special relational obligations to those one is bound to "
        "(family, group, promisee).",
    ),
]

_BY_NAME = {v.name: v for v in CORE_VALUES}


def by_name(name: str) -> ValueAnchor:
    """Return the ValueAnchor with this name (identity-stable)."""
    return _BY_NAME[name]


def value_pairs():
    """The 10 unordered conflict pairs over the 5 core values (C(5,2))."""
    return [(a.name, b.name) for a, b in itertools.combinations(CORE_VALUES, 2)]
