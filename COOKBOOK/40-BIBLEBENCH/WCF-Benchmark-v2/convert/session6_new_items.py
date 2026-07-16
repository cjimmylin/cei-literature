#!/usr/bin/env python
"""Session-6 v2.3 new-item source (2026-07-16).

Loads the 52 session-6-authored items from ``data/session6_new_items.json``
(assembled + G1-gated by ``analysis/session6_g1_check.py`` from the
post-adjudication final drafts; authoring pipeline: 6 opus drafters -> 10 blind
adversarial reviewers -> Fable adjudication (9 kills + 9 episode rebuilds) ->
repair agents -> fresh 4-reviewer round on rebuilt/replacement content ->
round-2 fixes; see reports/20260716-session6-review-adjudication.md).

These items are NOT derived from the v1 YAML — this module is their converter
source of record. ``yaml_to_jsonl.py`` appends them to the emitted datasets at
the v2.3 freeze. Session-4/5/6 patch layers do NOT apply to them (form rules
were enforced from birth); the loader only validates and routes.

Item counts: 15 contested + 28 frontier-open + 9 four-turn escalation episodes
(episodes carry ``pressure_turns`` — a list of 3 escalating user turns consumed
by ``episode_solver.scripted_dialogue``; the final turn ends with the frozen
session-2 CLOSING demand).
"""

from __future__ import annotations

import json
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
NEW_ITEMS_PATH = V2_ROOT / "data" / "session6_new_items.json"

EXPECTED_TOTAL = 52
EXPECTED_KINDS = {"contested": 15, "open": 28, "episode": 9}

# G4 gate (design memo §4: an item enters the leaderboard bank only if scoreable
# AND not instantly DEAD — some tier-1 answer < 100 in the Phase-2 live pilot).
# Applied strictly at the v2.3 freeze from
# analysis/20260716-session6-gate-results.json (qwen3.7-plus == 100 AND
# claude-haiku-4.5 == 100): all 9 four-turn escalation episodes (0/9 dented
# tier-1 despite plausible-duty reframes — but they produced a 58-pt tier gap,
# the strongest tier-break instrument authored to date; re-inclusion under an
# explicit tier-break rationale is an OWNER decision for a future session),
# all 8 crosswind items (the two-duty-collision mold is RLHF-soluble at
# tier-1), plus 2 complicit + 4 steadfast. Excluded items remain in
# session6_new_items.json (provenance) but are not emitted into the bank.
G4_EXCLUDED: set[str] = {
    "COMP-N-009", "COMP-N-010",
    "CROSS-N-001", "CROSS-N-002", "CROSS-N-003", "CROSS-N-004",
    "CROSS-N-005", "CROSS-N-007", "CROSS-N-008", "CROSS-N-009",
    "NARROW-N-001", "NARROW-N-002", "NARROW-N-003", "NARROW-N-004",
    "NARROW-N-005", "NARROW-N-006", "NARROW-N-007", "NARROW-N-008",
    "NARROW-N-009",
    "STED-N-001", "STED-N-002", "STED-N-008", "STED-N-009",
}


def load_new_items(path: Path = NEW_ITEMS_PATH) -> list[dict]:
    """Load, validate, and return the session-6 items (routed, id-sorted)."""
    items = json.loads(Path(path).read_text())
    if len(items) != EXPECTED_TOTAL:
        raise ValueError(f"expected {EXPECTED_TOTAL} session-6 items, got {len(items)}")
    kinds: dict[str, int] = {}
    for it in items:
        if it.get("authored") != "session-6" or "-N-" not in it["id"]:
            raise ValueError(f"{it.get('id')}: bad session-6 provenance")
        kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
        if it["kind"] == "episode" and len(it.get("pressure_turns") or []) != 3:
            raise ValueError(f"{it['id']}: episode without 3 pressure_turns")
    if kinds != EXPECTED_KINDS:
        raise ValueError(f"kind counts {kinds} != {EXPECTED_KINDS}")
    return sorted(items, key=lambda r: r["id"])


def main_and_episodes() -> tuple[list[dict], list[dict]]:
    items = load_new_items()
    return (
        [it for it in items if not it["episode"]],
        [it for it in items if it["episode"]],
    )


def bank_items() -> list[dict]:
    """Items entering the v2.3 leaderboard bank (G4 exclusions applied)."""
    return [it for it in load_new_items() if it["id"] not in G4_EXCLUDED]


if __name__ == "__main__":
    main, eps = main_and_episodes()
    print(f"session-6 items OK: {len(main)} main + {len(eps)} episodes")
