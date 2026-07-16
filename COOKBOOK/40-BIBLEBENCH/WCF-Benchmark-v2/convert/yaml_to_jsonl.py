#!/usr/bin/env python
"""Convert the WCF-Benchmark v1 YAML item bank to Inspect AI JSONL datasets.

Reads all multi-document YAML files in WCF-Benchmark/05-BANK-YAML/ (read-only),
drops dev_set_only items, routes each item to a scorer kind (mirroring v1
wcfbench/routing.py precedence exactly), and writes two JSONL files:

    data/wcf_main.jsonl      — single-completion items (expected: 204)
    data/wcf_episodes.jsonl  — NARROWGATE agentic episodes (expected: 22)

Regenerable at any time; the bank YAML is the source of truth and is never
modified. Run from anywhere: paths resolve relative to this file.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from pressure_turns import PRESSURE_TURNS

V2_ROOT = Path(__file__).resolve().parent.parent
BANK_DIR = V2_ROOT.parent / "WCF-Benchmark" / "05-BANK-YAML"
DATA_DIR = V2_ROOT / "data"

REQUIRED_FIELDS = ("id", "design", "track", "tier", "commandments", "stem", "key", "rubric")

EXPECTED_MAIN = 204
EXPECTED_EPISODES = 22


def scorer_kind(item: dict) -> str:
    """Routing kind — precedence ported from v1 wcfbench/routing.py:

    1. NARROWGATE (or any ``episode: true``) is episode.
    2. ``contested: true`` beats the ordinal branch (binding ruling: contested
       items are never scored as if their gold order were settled).
    3. AGGRAVATE with a ``gold_order`` is ordinal.
    4. PROOFTEXT is anchor.
    5. Everything else is open (the safe fallback: no format ask).
    """
    design = (item.get("design") or "").strip().lower()
    if design == "narrowgate" or item.get("episode") is True:
        return "episode"
    if item.get("contested") is True:
        return "contested"
    if design == "aggravate" and item.get("gold_order") is not None:
        return "ordinal"
    if design == "prooftext":
        return "anchor"
    return "open"


def load_bank(bank_dir: Path = BANK_DIR) -> list[dict]:
    """Load every runnable item from the bank (dev_set_only excluded)."""
    items: list[dict] = []
    seen_ids: set[str] = set()
    for path in sorted(bank_dir.glob("*.yaml")):
        for doc in yaml.safe_load_all(path.read_text()):
            if doc is None:  # trailing '---' yields an empty document
                continue
            missing = [f for f in REQUIRED_FIELDS if f not in doc]
            if missing:
                raise ValueError(f"{path.name}: item {doc.get('id', '?')} missing {missing}")
            if doc["id"] in seen_ids:
                raise ValueError(f"{path.name}: duplicate id {doc['id']}")
            seen_ids.add(doc["id"])
            if doc.get("dev_set_only") is True:
                continue
            items.append(doc)
    return items


def to_record(item: dict) -> dict:
    """Reduce a bank item to the fields the Inspect tasks consume.

    Episode records additionally carry a per-item ``pressure_turn`` (v2.1): the
    second-turn user message voicing the item's highest cost dial, authored in
    ``convert/pressure_turns.py``. Non-episode records omit the field. The field
    is consumed OPT-IN by the ``wcf_episodes`` task (``pressure_variant=item``);
    default behavior ignores it.
    """
    record = {
        "id": item["id"],
        "design": item["design"],
        "track": item["track"],
        "tier": str(item["tier"]),
        "commandments": item["commandments"],
        "contested": item.get("contested") is True,
        "episode": item.get("episode") is True,
        "kind": scorer_kind(item),
        "stem": item["stem"],
        "key": item["key"],
        "rubric": item["rubric"],
        "gold_order": item.get("gold_order"),
    }
    if record["kind"] == "episode":
        turn = PRESSURE_TURNS.get(item["id"])
        if turn is None:
            raise ValueError(f"episode {item['id']} has no authored pressure_turn")
        record["pressure_turn"] = turn
    return record


def convert(bank_dir: Path = BANK_DIR, data_dir: Path = DATA_DIR) -> tuple[int, int]:
    records = [to_record(item) for item in load_bank(bank_dir)]
    main = [r for r in records if r["kind"] != "episode"]
    episodes = [r for r in records if r["kind"] == "episode"]

    data_dir.mkdir(parents=True, exist_ok=True)
    for name, rows in (("wcf_main.jsonl", main), ("wcf_episodes.jsonl", episodes)):
        with open(data_dir / name, "w") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return len(main), len(episodes)


if __name__ == "__main__":
    n_main, n_episodes = convert()
    print(f"wcf_main.jsonl: {n_main} items (expected {EXPECTED_MAIN})")
    print(f"wcf_episodes.jsonl: {n_episodes} items (expected {EXPECTED_EPISODES})")
    if (n_main, n_episodes) != (EXPECTED_MAIN, EXPECTED_EPISODES):
        raise SystemExit("COUNT MISMATCH — do not run evals until resolved")
    print("OK")
