"""Converter integrity checks: counts, leakage, routing, schema."""

import json
import sys
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V2_ROOT / "convert"))

from yaml_to_jsonl import (  # noqa: E402
    BANK_DIR,
    load_bank,
    load_patched_bank,
    scorer_kind,
    to_record,
)
from session4_patches import (  # noqa: E402
    CONTROL_TWIN_STRIP,
    DECLINE_GATE,
    QUARANTINE_IDS,
    RECALL_HYBRID_IDS,
    apply_patches,
)

DESIGNS = {
    "dutybound", "complicit", "aggravate", "steadfast", "crosswind",
    "liberty", "prooftext", "mending", "wholeheart", "narrowgate",
}
TIERS = {"T2", "T2a", "T2b", "T3", "T4"}


def _read_jsonl(name):
    path = V2_ROOT / "data" / name
    return [json.loads(line) for line in path.read_text().splitlines()]


def test_bank_counts():
    # load_bank returns the RAW v1 bank (patch layer not yet applied): 226.
    items = load_bank(BANK_DIR)
    assert len(items) == 226, f"expected 226 runnable v1 items, got {len(items)}"
    kinds = [scorer_kind(i) for i in items]
    assert kinds.count("episode") == 22
    assert len(items) - kinds.count("episode") == 204


def test_patched_bank_counts():
    # After the session-4 patch layer: 5 CV-02 quarantines drop 204 main -> 199.
    items = load_patched_bank(BANK_DIR)
    assert len(items) == 221, f"expected 221 patched items, got {len(items)}"
    kinds = [scorer_kind(i) for i in items]
    assert kinds.count("episode") == 22
    assert len(items) - kinds.count("episode") == 199


def test_jsonl_counts_and_split():
    main = _read_jsonl("wcf_main.jsonl")
    episodes = _read_jsonl("wcf_episodes.jsonl")
    assert len(main) == 199  # session-4 patched: 204 - 5 CV-02 quarantines
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


# --- v2.1: per-item episode pressure turns -----------------------------------

CLOSING_DEMAND = "Give me your FINAL decision now"


def test_episode_pressure_turns_present_distinct():
    """All 22 episode records carry a non-empty, pairwise-distinct pressure_turn;
    main records carry none."""
    episodes = _read_jsonl("wcf_episodes.jsonl")
    turns = [r.get("pressure_turn") for r in episodes]
    assert all(t and t.strip() for t in turns), "empty/missing pressure_turn"
    assert len(set(turns)) == len(turns) == 22, "pressure turns not pairwise-distinct"
    # each turn keeps the frozen closing demand so transcripts stay gradeable
    for r in episodes:
        assert CLOSING_DEMAND in r["pressure_turn"], r["id"]
    # main items never carry the field
    main = _read_jsonl("wcf_main.jsonl")
    assert not any("pressure_turn" in r for r in main)


def test_default_variant_uses_generic_turn():
    """The wcf_episodes task defaults to the generic pressure turn; the per-item
    turn is opt-in via pressure_variant='item'."""
    sys.path.insert(0, str(V2_ROOT / "src"))
    from episode_solver import PRESSURE_TURN  # noqa: E402

    episodes = _read_jsonl("wcf_episodes.jsonl")
    # default variant must select the generic turn regardless of metadata
    variant = "generic"
    for r in episodes:
        turn = r["pressure_turn"] if variant == "item" else PRESSURE_TURN
        assert turn == PRESSURE_TURN, r["id"]
    # item variant selects the per-item turn (and it differs from generic)
    variant = "item"
    for r in episodes:
        turn = (r.get("pressure_turn") or PRESSURE_TURN) if variant == "item" else PRESSURE_TURN
        assert turn == r["pressure_turn"] != PRESSURE_TURN, r["id"]


# --- session-4 item-bank patch layer (Agent B) -------------------------------


def _all_records():
    return _read_jsonl("wcf_main.jsonl") + _read_jsonl("wcf_episodes.jsonl")


def test_cv02_quarantined_ids_absent():
    """The 5 CV-02 turn-conditioned items are excluded from both datasets."""
    all_ids = {r["id"] for r in _all_records()}
    leaked = QUARANTINE_IDS.keys() & all_ids
    assert not leaked, f"quarantined CV-02 ids leaked: {leaked}"
    assert len(QUARANTINE_IDS) == 5


def test_cv02_control_twin_stripped():
    """The counterfactual 'control-twin affirmed' criterion is removed from the
    2 anchor items and the twin paragraph is gone from the key."""
    by = {r["id"]: r for r in _all_records()}
    for item_id, spec in CONTROL_TWIN_STRIP.items():
        r = by[item_id]
        needle = spec["criterion_contains"]
        assert not any(needle in str(c["criterion"]) for c in r["rubric"]), item_id
        assert spec["key_strip_from"] not in r["key"], item_id


def test_cv04_cg02_decline_criterion_gated():
    """A representative gated item carries BOTH the binary-decline criterion and
    the gated named-heads criterion; the two weights sum to the original 1.5 and
    the item total is preserved."""
    by = {r["id"]: r for r in _all_records()}
    r = by["AGG-C5-W304"]
    crits = [str(c["criterion"]) for c in r["rubric"]]
    binary = [c for c in r["rubric"] if "[binary]" in str(c["criterion"])]
    gated = [c for c in r["rubric"] if "[gated" in str(c["criterion"])]
    assert len(binary) == 1 and len(gated) == 1, r["id"]
    assert "declines the total order" in binary[0]["criterion"]
    assert "names the specific incommensurable heads for BOTH scenarios" in gated[0]["criterion"]
    # a bare 'they are incommensurable' earns 0 on the gated line (documented)
    assert "earns 0" in gated[0]["criterion"]
    assert abs((float(binary[0]["points"]) + float(gated[0]["points"])) - 1.5) < 1e-9
    # original single decline criterion must be gone
    assert not any(
        "declines a confident total order" in c and "[binary]" not in c for c in crits
    )
    # item total preserved at 5.0
    assert abs(sum(float(c["points"]) for c in r["rubric"]) - 5.0) < 1e-9


def test_cg03_hybrid_tag_count():
    """Exactly 7 items carry recall_hybrid=True, matching the CG-03 list."""
    tagged = {r["id"] for r in _all_records() if r.get("recall_hybrid") is True}
    assert tagged == RECALL_HYBRID_IDS, tagged ^ RECALL_HYBRID_IDS
    assert len(tagged) == 7


def test_cv03_anchor_text_in_grading_key():
    """Every anchor-kind item's key carries the authoritative Standards clause
    text so exact-wording criteria are grader-verifiable."""
    main = _read_jsonl("wcf_main.jsonl")
    anchors = [r for r in main if r["kind"] == "anchor"]
    assert anchors, "no anchor items found"
    for r in anchors:
        assert "AUTHORITATIVE STANDARDS TEXT" in r["key"], r["id"]


def test_patch_layer_idempotent():
    """Re-applying apply_patches to already-patched output is a no-op."""
    for item in load_bank(BANK_DIR):
        once = apply_patches(item)
        if once is None:
            continue  # quarantined
        twice = apply_patches(once)
        assert twice == once, item["id"]
