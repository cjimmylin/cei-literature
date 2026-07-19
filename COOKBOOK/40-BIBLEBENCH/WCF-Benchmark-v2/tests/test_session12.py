"""Session-12 Phase-0 regression tests (P1 gold_order guard + P4 schema fields).

P1: render_standard emitted a GOLD ORDER line for ANY truthy gold_order; the 5
v1 AGG items carrying the string sentinel "declines total order" had it
char-split ("d < e < c < …") into their judge prompts (s11 report §7).
P4: mold + provenance are now explicit schema fields on every emitted record.

Run:  .venv-v2/bin/python -m pytest tests/test_session12.py -q
"""

import json
import sys
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V2_ROOT / "src"))
sys.path.insert(0, str(V2_ROOT / "convert"))

from wcf_tasks import render_standard  # noqa: E402
from yaml_to_jsonl import MOLD_BY_PREFIX, mold_for  # noqa: E402

SENTINEL_IDS = {
    "AGG-C3-003", "AGG-C4-W202", "AGG-C7-007", "AGG-C5-W304", "AGG-C8-W305",
}


def _read_jsonl(name):
    return [json.loads(line) for line in (V2_ROOT / "data" / name).read_text().splitlines()]


def _record(gold_order):
    r = {
        "id": "TEST-C1-001",
        "key": "Gold key text.",
        "rubric": [{"points": 1.0, "criterion": "names the duty"}],
    }
    if gold_order is not None:
        r["gold_order"] = gold_order
    return r


# --- P1: gold_order rendering ------------------------------------------------


def test_list_gold_order_renders_joined():
    std = render_standard(_record(["lesser sin", "greater sin"]))
    assert "GOLD ORDER (least to most heinous): lesser sin < greater sin" in std


def test_string_sentinel_gold_order_omitted():
    std = render_standard(_record("declines total order"))
    assert "GOLD ORDER" not in std
    assert " < " not in std  # no char-split artifact


def test_absent_and_null_gold_order_omitted():
    assert "GOLD ORDER" not in render_standard(_record(None))  # field absent
    null_rec = _record(None)
    null_rec["gold_order"] = None  # field present but null (the JSONL shape)
    assert "GOLD ORDER" not in render_standard(null_rec)


def test_bank_sentinel_items_render_clean():
    """The 5 real sentinel items keep their string in the data (legacy; §3(d)
    bans NEW string sentinels) but render with no GOLD ORDER line."""
    by = {r["id"]: r for r in _read_jsonl("wcf_main.jsonl")}
    assert SENTINEL_IDS <= by.keys()
    for iid in SENTINEL_IDS:
        r = by[iid]
        assert r["gold_order"] == "declines total order", iid
        std = render_standard(r)
        assert "GOLD ORDER" not in std, iid


def test_true_ordinal_items_still_render_gold_order():
    mains = _read_jsonl("wcf_main.jsonl")
    listed = [r for r in mains if isinstance(r.get("gold_order"), list)]
    assert listed, "no list-typed gold_order items found"
    for r in listed:
        assert "GOLD ORDER (least to most heinous): " in render_standard(r), r["id"]


# --- P4: mold + provenance schema fields -------------------------------------


def test_every_record_carries_mold_and_provenance():
    rows = _read_jsonl("wcf_main.jsonl") + _read_jsonl("wcf_episodes.jsonl")
    for r in rows:
        assert r["mold"] == mold_for(r["id"]), r["id"]
        assert r["provenance"] in {"v1", "session-6", "session-7", "session-12"}, r["id"]


def test_mold_counts_match_s11_stock():
    """The four s12 target molds at their s11-assessed stock (pre-expansion)."""
    rows = _read_jsonl("wcf_main.jsonl") + _read_jsonl("wcf_episodes.jsonl")
    counts = {}
    for r in rows:
        counts[r["mold"]] = counts.get(r["mold"], 0) + 1
    assert counts["mending"] == 21
    assert counts["liberty"] == 19
    assert counts["prooftext"] == 23
    assert counts["wholeheart"] == 22
    assert sum(counts.values()) == 287


def test_mold_map_rejects_unknown_prefix():
    import pytest
    with pytest.raises(ValueError):
        mold_for("BOGUS-C1-001")
    assert set(MOLD_BY_PREFIX) == {
        "AGG", "CONT", "COMP", "STED", "CROSS", "PROOF",
        "WHOLE", "DUTY", "MEND", "LIB", "NARROW",
    }
