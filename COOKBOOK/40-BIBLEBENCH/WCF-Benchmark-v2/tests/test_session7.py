"""Session-7 tests: authored new items, v2.4 bank composition, grader-retry
wrapper, frontier-core task wiring. Session-7 authored no patch layer and no
episodes (mirrors test_session6.py where applicable)."""

import json
import sys
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V2_ROOT / "convert"))

from session7_new_items import (  # noqa: E402
    EXPECTED_KINDS,
    G4_EXCLUDED,
    bank_items,
    load_new_items,
)


def _read_jsonl(name):
    return [json.loads(l) for l in open(V2_ROOT / "data" / name)]


# --- session-7 authored items -------------------------------------------------

def test_new_items_load_and_counts():
    items = load_new_items()
    assert len(items) == 42
    kinds = {}
    for it in items:
        kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
    assert kinds == EXPECTED_KINDS


def test_new_items_namespace_and_provenance():
    for it in load_new_items():
        assert "-N-" in it["id"], it["id"]
        assert it["authored"] == "session-7", it["id"]
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


def test_no_episodes_authored():
    for it in load_new_items():
        assert it["kind"] in ("contested", "open"), it["id"]
        assert not it.get("pressure_turns"), it["id"]


# --- G4 gate + v2.4 bank composition -------------------------------------------

def test_g4_exclusions_match_manifest_and_bank():
    m = json.loads((V2_ROOT / "data" / "BANK-VERSION.json").read_text())
    assert set(G4_EXCLUDED) <= set(m["g4_excluded_new_items"])
    bank_ids = {r["id"] for r in _read_jsonl("wcf_main.jsonl")}
    bank_ids |= {r["id"] for r in _read_jsonl("wcf_episodes.jsonl")}
    assert not (G4_EXCLUDED & bank_ids), "G4-excluded item leaked into the bank"
    entered = {it["id"] for it in bank_items()}
    assert entered <= bank_ids
    assert len(entered) == 37


def test_v24_bank_composition():
    main = _read_jsonl("wcf_main.jsonl")
    s7 = [r for r in main if r.get("authored") == "session-7"]
    assert len(s7) == 37
    kinds = {}
    for r in s7:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    assert kinds == {"contested": 21, "open": 16}


def test_gate_dataset_file_covers_all_42():
    ids = {r["id"] for r in _read_jsonl("wcf_s7_new_main.jsonl")}
    assert ids == {it["id"] for it in load_new_items()}


# --- frontier-core task + grader retry wrapper ---------------------------------

def test_frontier_core_task_size():
    sys.path.insert(0, str(V2_ROOT / "src"))
    from wcf_tasks import wcf_frontier_core
    t = wcf_frontier_core()
    ids = [str(s.id) for s in t.dataset]
    assert len(ids) == 29 + 37
    assert all("-N-" in i for i in ids)
    assert not any(i.startswith("NARROW-N") for i in ids)


def test_grader_retry_wrapper_constant():
    from wcf_grading import GRADER_ATTEMPTS
    assert GRADER_ATTEMPTS == 3
    src = (V2_ROOT / "src" / "wcf_grading.py").read_text()
    assert "for attempt in range(GRADER_ATTEMPTS)" in src
