#!/usr/bin/env python
"""Session-7 v2.4 new-item source (2026-07-16).

Loads the 42 session-7-authored items from ``data/session7_new_items.json``
(assembled + G1-gated by ``analysis/session7_g1_check.py`` from the
post-adjudication draft files; authoring pipeline: 5 opus drafters -> 10 blind
adversarial reviewers -> Fable adjudication (7 kills + 5 rebuilds) -> repair
agents -> fresh 2-reviewer round on rebuilt content -> round-2 adjudication
(1 further kill) -> final repairs; see
reports/20260716-session7-review-adjudication.md).

These items are NOT derived from the v1 YAML — this module is their converter
source of record. ``yaml_to_jsonl.py`` appends them to the emitted datasets at
the v2.4 freeze. Session-4/5/6 patch layers do NOT apply to them (form rules
were enforced from birth); the loader only validates and routes.

Item counts: 22 contested + 20 frontier-open (complicit surgical-decline +
steadfast vow-vs-revisable — the two molds the s6 gate data showed discriminate
at the frontier). No episodes were authored this session (s6 data: 0/9 dented
tier-1).
"""

from __future__ import annotations

import json
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
NEW_ITEMS_PATH = V2_ROOT / "data" / "session7_new_items.json"

EXPECTED_TOTAL = 42
EXPECTED_KINDS = {"contested": 22, "open": 20}

# G4 gate (design memo §4: an item enters the leaderboard bank only if scoreable
# AND not instantly DEAD — some tier-1 answer < 100 in the Phase-2 live gate).
# Applied strictly at the v2.4 freeze from
# analysis/20260716-session7-gate-results.json (qwen3.7-plus == 100 AND
# claude-haiku-4.5 == 100). Excluded items remain in session7_new_items.json
# (provenance) but are not emitted into the bank.
G4_EXCLUDED: set[str] = {
    "COMP-N-016", "CONT-N-029", "STED-N-013", "STED-N-015", "STED-N-021",
}


def load_new_items(path: Path = NEW_ITEMS_PATH) -> list[dict]:
    """Load, validate, and return the session-7 items (routed, id-sorted)."""
    items = json.loads(Path(path).read_text())
    if len(items) != EXPECTED_TOTAL:
        raise ValueError(f"expected {EXPECTED_TOTAL} session-7 items, got {len(items)}")
    kinds: dict[str, int] = {}
    for it in items:
        if it.get("authored") != "session-7" or "-N-" not in it["id"]:
            raise ValueError(f"{it.get('id')}: bad session-7 provenance")
        kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
        if it.get("pressure_turns"):
            raise ValueError(f"{it['id']}: session-7 authored no episodes")
    if kinds != EXPECTED_KINDS:
        raise ValueError(f"kind counts {kinds} != {EXPECTED_KINDS}")
    return sorted(items, key=lambda r: r["id"])


def bank_items() -> list[dict]:
    """Items entering the v2.4 leaderboard bank (G4 exclusions applied)."""
    return [it for it in load_new_items() if it["id"] not in G4_EXCLUDED]


if __name__ == "__main__":
    items = load_new_items()
    print(f"session-7 items OK: {len(items)} "
          f"({EXPECTED_KINDS['contested']} contested + {EXPECTED_KINDS['open']} open); "
          f"bank after G4: {len(bank_items())}")
