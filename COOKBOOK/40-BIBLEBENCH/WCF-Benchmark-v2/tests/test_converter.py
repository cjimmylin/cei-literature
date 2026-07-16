"""Converter integrity checks: counts, leakage, routing, schema."""

import json
import sys
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V2_ROOT / "convert"))

from yaml_to_jsonl import BANK_DIR, load_bank, scorer_kind, to_record  # noqa: E402

DESIGNS = {
    "dutybound", "complicit", "aggravate", "steadfast", "crosswind",
    "liberty", "prooftext", "mending", "wholeheart", "narrowgate",
}
TIERS = {"T2", "T2a", "T2b", "T3", "T4"}


def _read_jsonl(name):
    path = V2_ROOT / "data" / name
    return [json.loads(line) for line in path.read_text().splitlines()]


def test_bank_counts():
    items = load_bank(BANK_DIR)
    assert len(items) == 226, f"expected 226 runnable items, got {len(items)}"
    kinds = [scorer_kind(i) for i in items]
    assert kinds.count("episode") == 22
    assert len(items) - kinds.count("episode") == 204


def test_jsonl_counts_and_split():
    main = _read_jsonl("wcf_main.jsonl")
    episodes = _read_jsonl("wcf_episodes.jsonl")
    assert len(main) == 204
    assert len(episodes) == 22
    assert all(r["kind"] != "episode" for r in main)
    assert all(r["kind"] == "episode" for r in episodes)


def test_no_dev_set_leakage():
    dev_ids = {"LIB-C3-W202", "LIB-C7-008", "LIB-C8-W304", "LIB-C2-W305"}
    all_ids = {r["id"] for r in _read_jsonl("wcf_main.jsonl") + _read_jsonl("wcf_episodes.jsonl")}
    assert not (dev_ids & all_ids), f"dev_set_only items leaked: {dev_ids & all_ids}"


def test_schema_and_vocab():
    rows = _read_jsonl("wcf_main.jsonl") + _read_jsonl("wcf_episodes.jsonl")
    ids = [r["id"] for r in rows]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for r in rows:
        assert r["design"] in DESIGNS, r["id"]
        assert r["tier"] in TIERS, f"{r['id']} unexpected tier {r['tier']}"
        assert r["track"] in ("A", "B"), r["id"]
        assert r["stem"].strip() and r["key"].strip(), r["id"]
        assert isinstance(r["rubric"], list) and r["rubric"], r["id"]
        for entry in r["rubric"]:
            assert "points" in entry and "criterion" in entry, r["id"]


def test_routing_invariants():
    rows = _read_jsonl("wcf_main.jsonl")
    for r in rows:
        if r["contested"]:
            assert r["kind"] == "contested", r["id"]
        if r["kind"] == "ordinal":
            assert r["design"] == "aggravate" and r["gold_order"], r["id"]
        if r["kind"] == "anchor":
            assert r["design"] == "prooftext", r["id"]
