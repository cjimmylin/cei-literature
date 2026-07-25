#!/usr/bin/env python
"""Session-13 v2.5 new-item source (2026-07-24).

Loads the 80 session-13 items from ``data/session13_new_items.json`` (the merged
hardening tranche: 63 double-hazard rebuilds + 17 frozen s12 discriminators;
assembled + G1-gated by ``analysis/session13_g1_check.py`` from the
post-adjudication rebuild batches; authoring pipeline: 8 opus rebuilders (2 per
mold) -> 16 blind adversarial reviewers -> Fable adjudication (0 kills + 4 major /
~20 minor repairs) -> fresh 2-reviewer round on rebuilt content -> final repairs;
see reports/20260724-session13-wave-report.md).

These items are NOT derived from the v1 YAML — this module is their converter
source of record. ``yaml_to_jsonl.py`` appends them to the emitted datasets at
the v2.5 freeze. Session-4/5/6 patch layers do NOT apply to them (form rules were
enforced from birth); the loader only validates and routes.

Admission instrument (session 15, owner-ratified 2026-07-24): the cheap 3-judge
median panel that scored the s13 live gate NO-GO (25/80) was RETIRED for admission
decisions; a $0 strong-judge panel (mean-of-2: Claude Opus via Agent channel +
GPT-5.6-Sol via codex exec, strict-v2 template) rejudged the logged s13 gate run
(n=80, both SUTs) and the tranche went GO under the verbatim criterion
(nonzero |qwen-haiku| = 70/80 >= 27 required; unscored == 0). Strict-mode scores
are a DIFFERENT instrument (bank-versioning rule extended to judge-mode); no
cross-version or cross-judge-mode score comparison. See data/BANK-VERSION.json
notes for the full admission-instrument record.

Item counts: 80 total (63 rebuilt session-13 + 17 frozen session-12); 20 per mold
(MEND / LIB / PROOF / WHOLE); 60 open + 20 anchor. No episodes were authored this
session (double-hazard drafting/anchor items only).
"""

from __future__ import annotations

import json
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
NEW_ITEMS_PATH = V2_ROOT / "data" / "session13_new_items.json"

EXPECTED_TOTAL = 80
EXPECTED_KINDS = {"open": 60, "anchor": 20}
# Provenance split within the merged tranche (frozen 17 keep session-12; the
# rebuilt 63 flip to session-13). Both provenances enter the bank together.
EXPECTED_AUTHORED = {"session-13": 63, "session-12": 17}

# G4 gate (design memo §4: an item enters the leaderboard bank only if scoreable
# AND not instantly DEAD under the admission instrument). The session-15
# strong-judge admission rejudge found ``unscored == 0`` for the full tranche —
# all 80 items are scoreable and none is dead-ceiling under the strong-judge
# instrument that ruled GO. Owner ratification (2026-07-24) admits all 80. There
# are therefore NO G4 exclusions this session; the set is empty by design (kept
# for parity with session6/7 loaders and the manifest schema).
G4_EXCLUDED: set[str] = set()


def load_new_items(path: Path = NEW_ITEMS_PATH) -> list[dict]:
    """Load, validate, and return the session-13 items (routed, id-sorted)."""
    items = json.loads(Path(path).read_text())
    if len(items) != EXPECTED_TOTAL:
        raise ValueError(f"expected {EXPECTED_TOTAL} session-13 items, got {len(items)}")
    kinds: dict[str, int] = {}
    authored: dict[str, int] = {}
    for it in items:
        if it.get("authored") not in EXPECTED_AUTHORED or "-N-" not in it["id"]:
            raise ValueError(f"{it.get('id')}: bad session-13 provenance")
        kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
        authored[it["authored"]] = authored.get(it["authored"], 0) + 1
        if it.get("pressure_turns"):
            raise ValueError(f"{it['id']}: session-13 authored no episodes")
    if kinds != EXPECTED_KINDS:
        raise ValueError(f"kind counts {kinds} != {EXPECTED_KINDS}")
    if authored != EXPECTED_AUTHORED:
        raise ValueError(f"authored counts {authored} != {EXPECTED_AUTHORED}")
    return sorted(items, key=lambda r: r["id"])


def bank_items() -> list[dict]:
    """Items entering the v2.5 leaderboard bank (G4 exclusions applied)."""
    return [it for it in load_new_items() if it["id"] not in G4_EXCLUDED]


if __name__ == "__main__":
    items = load_new_items()
    print(f"session-13 items OK: {len(items)} "
          f"({EXPECTED_KINDS['open']} open + {EXPECTED_KINDS['anchor']} anchor; "
          f"{EXPECTED_AUTHORED['session-13']} rebuilt + "
          f"{EXPECTED_AUTHORED['session-12']} frozen); "
          f"bank after G4: {len(bank_items())}")
