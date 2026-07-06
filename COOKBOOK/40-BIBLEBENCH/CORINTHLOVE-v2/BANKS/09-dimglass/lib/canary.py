"""Deterministic canary GUID generation for DIMGLASS.

Format: 10CB2-09-<uuid4>  (per 98-guide §2 and the build spec).

Canaries are deterministic given the bank seed so a regeneration reproduces the
same registry, but they are still UUID-v4-shaped (version nibble = 4, variant
bits = 10xx). They live ONLY in item metadata / the registry, never in any
candidate-visible field (leakage-checked in tests/test_leakage_canary.py).
"""
from __future__ import annotations

import random

DESIGN = "09"
PREFIX = f"10CB2-{DESIGN}-"


def _uuid4_from_rng(rng: random.Random) -> str:
    """Produce a syntactically valid RFC-4122 v4 UUID string from an RNG."""
    b = bytearray(rng.getrandbits(8) for _ in range(16))
    b[6] = (b[6] & 0x0F) | 0x40  # version 4
    b[8] = (b[8] & 0x3F) | 0x80  # variant 10
    h = b.hex()
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def make_canary(rng: random.Random) -> str:
    return PREFIX + _uuid4_from_rng(rng)


def is_wellformed(canary: str) -> bool:
    if not canary.startswith(PREFIX):
        return False
    tail = canary[len(PREFIX):]
    parts = tail.split("-")
    if len(parts) != 5:
        return False
    lens = [len(p) for p in parts]
    if lens != [8, 4, 4, 4, 12]:
        return False
    if parts[2][0] != "4":  # version nibble
        return False
    if parts[3][0].lower() not in "89ab":  # variant
        return False
    try:
        int(tail.replace("-", ""), 16)
    except ValueError:
        return False
    return True
