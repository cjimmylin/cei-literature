"""Session-6 tests: s6 patch layer, authored new items, v2.3 bank composition,
escalation-episode machinery."""

import json
import sys
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V2_ROOT / "convert"))

from pressure_turns import CLOSING  # noqa: E402
from session6_new_items import (  # noqa: E402
    EXPECTED_KINDS,
    G4_EXCLUDED,
    bank_items,
    load_new_items,
)
from session6_patches import apply_patches as apply_s6  # noqa: E402


def _read_jsonl(name):
    return [json.loads(l) for l in open(V2_ROOT / "data" / name)]


# --- session6_patches (COMP-C4-005 repair) -----------------------------------

def test_s6_patch_touches_only_comp_c4_005():
    from session6_patches import touched_ids
    assert touched_ids() == {"COMP-C4-005"}


def test_s6_patch_applied_in_emitted_bank():
    rows = {r["id"]: r for r in _read_jsonl("wcf_main.jsonl")}
    r = rows["COMP-C4-005"]
    assert "constraints attached" not in r["stem"]
    assert "at least one vet and two techs on every shift" in r["stem"]
    assert "SCORING GATE (session-6 repair):" in r["key"]


def test_s6_patch_idempotent_and_noop_elsewhere():
    rows = _read_jsonl("wcf_main.jsonl")
    for r in rows[:20]:
        again = apply_s6(r)
        assert again == apply_s6(again)
        if r["id"] != "COMP-C4-005":
            assert again == r


# --- session-6 authored items -------------------------------------------------

def test_new_items_load_and_counts():
    items = load_new_items()
    assert len(items) == 52
    kinds = {}
    for it in items:
        kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
    assert kinds == EXPECTED_KINDS


def test_new_items_namespace_and_provenance():
    for it in load_new_items():
        assert "-N-" in it["id"], it["id"]
        assert it["authored"] == "session-6", it["id"]
        assert it["author_batch"], it["id"]


def test_new_items_form_rules():
    for it in load_new_items():
        total = sum(c["points"] for c in it["rubric"])
        assert 5.0 <= total <= 6.5, it["id"]
        cap = 8 if it["kind"] == "contested" else 6
        assert len(it["rubric"]) <= cap, it["id"]
        assert any(c.get("axis") == "manner" for c in it["rubric"]), it["id"]
        assert "GATE" in it["key"], it["id"]
        if it["kind"] == "contested":
            joined = " ".join(str(c["criterion"]) for c in it["rubric"])
            assert "accepted head-pair" in joined, it["id"]


def test_new_episode_escalation_machinery():
    for it in load_new_items():
        if it["kind"] != "episode":
            assert not it.get("pressure_turns"), it["id"]
            continue
        turns = it["pressure_turns"]
        assert len(turns) == 3, it["id"]
        assert turns[2].endswith(CLOSING), it["id"]
        assert CLOSING not in turns[0] and CLOSING not in turns[1], it["id"]


# --- G4 gate + v2.3 bank composition -------------------------------------------

def test_g4_exclusions_match_manifest_and_bank():
    m = json.loads((V2_ROOT / "data" / "BANK-VERSION.json").read_text())
    # v2.4: the manifest list is the union across authored sessions (s6 + s7).
    assert set(G4_EXCLUDED) <= set(m["g4_excluded_new_items"])
    bank_ids = {r["id"] for r in _read_jsonl("wcf_main.jsonl")}
    bank_ids |= {r["id"] for r in _read_jsonl("wcf_episodes.jsonl")}
    assert not (G4_EXCLUDED & bank_ids), "G4-excluded item leaked into the bank"
    entered = {it["id"] for it in bank_items()}
    assert entered <= bank_ids
    assert len(entered) == 29


def test_no_new_episode_in_bank():
    # All 9 session-6 episodes were G4-excluded (0/9 dented tier-1).
    for r in _read_jsonl("wcf_episodes.jsonl"):
        assert "-N-" not in r["id"], r["id"]


def test_gate_dataset_files_cover_all_52():
    ids = {r["id"] for r in _read_jsonl("wcf_new_main.jsonl")}
    ids |= {r["id"] for r in _read_jsonl("wcf_new_episodes.jsonl")}
    assert ids == {it["id"] for it in load_new_items()}


# --- escalation solver ----------------------------------------------------------

def test_solver_ramp_precedence():
    """Items with pressure_turns always run the ramp; others keep v2.1 behavior."""
    src = (V2_ROOT / "src" / "episode_solver.py").read_text()
    assert 'state.metadata.get("pressure_turns")' in src
    tasks_src = (V2_ROOT / "src" / "wcf_tasks.py").read_text()
    assert '"pressure_turns": record.get("pressure_turns")' in tasks_src
