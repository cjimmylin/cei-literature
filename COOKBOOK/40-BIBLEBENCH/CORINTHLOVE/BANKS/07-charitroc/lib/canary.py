"""Deterministic RFC-4122-v4-shaped CHARITROC canaries."""
from __future__ import annotations

import random


PREFIX = "10CB-07-"


def _uuid4_from_rng(rng: random.Random) -> str:
    octets = bytearray(rng.getrandbits(8) for _ in range(16))
    octets[6] = (octets[6] & 0x0F) | 0x40
    octets[8] = (octets[8] & 0x3F) | 0x80
    value = octets.hex()
    return (
        f"{value[0:8]}-{value[8:12]}-{value[12:16]}-"
        f"{value[16:20]}-{value[20:32]}"
    )


def make_canary(rng: random.Random) -> str:
    return PREFIX + _uuid4_from_rng(rng)


def is_wellformed(value: str) -> bool:
    if not isinstance(value, str) or not value.startswith(PREFIX):
        return False
    tail = value[len(PREFIX):]
    parts = tail.split("-")
    if [len(part) for part in parts] != [8, 4, 4, 4, 12]:
        return False
    if parts[2][0].lower() != "4" or parts[3][0].lower() not in "89ab":
        return False
    try:
        int("".join(parts), 16)
    except ValueError:
        return False
    return True
