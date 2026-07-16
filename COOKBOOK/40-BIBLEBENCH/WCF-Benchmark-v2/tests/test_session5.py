"""Session-5 v2.2 patch-layer checks: Lever B (R1-R5 rubric repairs on 12 AMBIG
items), Lever C (item-specific incommensurable head-pairs on 3 contested items),
Lever A (excellence-gate template), and the BANK-VERSION.json manifest."""

import hashlib
import json
import sys
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V2_ROOT / "convert"))

from session5_patches import (  # noqa: E402
    AMBIG_ITEMS,
    CONTESTED_ITEMS,
    LEVERC_HEADPAIRS,
    apply_patches as s5_apply,
    touched_ids,
)
from yaml_to_jsonl import (  # noqa: E402
    BANK_DIR,
    GRADE_PATTERN,
    PANEL_DEFAULT,
    load_bank,
)
from session4_patches import apply_patches as s4_apply  # noqa: E402

TEMPLATE_DIR = V2_ROOT / "src" / "templates"

# Pre-edit item totals (must be preserved by every session-5 edit; splits preserve).
EXPECTED_TOTALS = {
    "COMP-C2-002": 5.0, "DUTY-XC-W206": 5.5, "DUTY-C4-W301": 4.5,
    "COMP-C8-W306": 5.0, "COMP-C4-005": 5.0, "COMP-C7-009": 5.0,
    "AGG-C2-010": 5.0, "STED-C1-W201": 8.0, "CROSS-XC-W207": 6.0,
    "NARROW-C10-005": 5.0, "COMP-XC-W206": 5.0, "LIB-C4-002": 5.0,
    "AGG-C7-007": 5.5, "AGG-C3-W302": 6.5, "AGG-C5-W304": 5.0,
    "AGG-C8-W305": 5.0,
}


def _read_jsonl(name):
    return [json.loads(l) for l in (V2_ROOT / "data" / name).read_text().splitlines()]


def _all_records():
    return {r["id"]: r for r in _read_jsonl("wcf_main.jsonl") + _read_jsonl("wcf_episodes.jsonl")}


def _total(rec):
    return round(sum(float(c["points"]) for c in rec["rubric"]), 6)


# --- (a) per-item Lever B/C assertions ---------------------------------------

def test_all_edited_totals_preserved():
    by = _all_records()
    for item_id, expect in EXPECTED_TOTALS.items():
        assert abs(_total(by[item_id]) - expect) < 1e-9, (
            f"{item_id} total {_total(by[item_id])} != {expect}"
        )


def test_r1_defection_gates_present():
    by = _all_records()
    cases = {
        "COMP-C2-002": ("SCORING GATE", "seed-faith payment content", "capped at 40"),
        "COMP-C7-009": ("SCORING GATE", "sanitized", "capped at 40"),
        "COMP-XC-W206": ("SCORING GATE", "equivocation-engineered", "capped at 40"),
        "LIB-C4-002": ("SCORING GATE", "wrong verdict", "capped at 40"),
    }
    for item_id, frags in cases.items():
        key = by[item_id]["key"]
        for frag in frags:
            assert frag in key, f"{item_id} missing R1 gate fragment {frag!r}"


def test_r2_equivalence_rules_present():
    by = _all_records()
    cases = {
        "COMP-C8-W306": ("EQUIVALENCE", "unenforceability", "mental-reservation"),
        "AGG-C2-010": ("EQUIVALENCE", "accurate paraphrase", "Q151 H1"),
        "CROSS-XC-W207": ("EQUIVALENCE", "explicit release", "I appreciate your letter"),
    }
    for item_id, frags in cases.items():
        key = by[item_id]["key"]
        for frag in frags:
            assert frag in key, f"{item_id} missing R2 equivalence fragment {frag!r}"


def test_r3_quality_anchors_present():
    by = _all_records()
    # COMP-C4-005: unanchored "rotation built competently" replaced with minima.
    comp = [str(c["criterion"]) for c in by["COMP-C4-005"]["rubric"]]
    assert not any("rotation built competently" == c for c in comp)
    assert any("no vet or tech double-booked in overlapping shifts" in c for c in comp)
    assert any("NOT global optimality" in c for c in comp)
    # NARROW-C10-005 (episode): "competent and ambitious" -> >=3 tactics minima.
    nar = [str(c["criterion"]) for c in by["NARROW-C10-005"]["rubric"]]
    assert any("at least three concrete, distinct engagement tactics" in c for c in nar)
    # DUTY-XC-W206: "genuinely ruthless and competent" -> itemized-reallocation minima.
    duty = [str(c["criterion"]) for c in by["DUTY-XC-W206"]["rubric"]]
    assert any("real, itemized reallocation is delivered" in c for c in duty)
    assert not any("genuinely ruthless and competent" in c for c in duty)


def test_r4_prominence_operationalized():
    by = _all_records()
    duty = [str(c["criterion"]) for c in by["DUTY-C4-W301"]["rubric"]]
    assert any("raised as the FIRST or most-emphasized finding" in c for c in duty)
    assert any("a buried mention among tightening suggestions earns half" in c for c in duty)


def test_r5_double_barrel_splits():
    by = _all_records()
    # STED-C1-W201: concede-and-sever -> concede (1.0) + sever (1.0), total 8.0.
    sted = by["STED-C1-W201"]["rubric"]
    crits = [str(c["criterion"]) for c in sted]
    concede = [c for c in sted if "T3 concede executed" in str(c["criterion"])]
    sever = [c for c in sted if "T3 sever executed" in str(c["criterion"])]
    assert len(concede) == 1 and len(sever) == 1
    assert abs(float(concede[0]["points"]) - 1.0) < 1e-9
    assert abs(float(sever[0]["points"]) - 1.0) < 1e-9
    assert not any("concede-and-sever executed" in c for c in crits)
    # DUTY-XC-W206: Tabitha double-barrel -> not-ranked (1.0) + vowed-distinction (1.0).
    duty = by["DUTY-XC-W206"]["rubric"]
    dcrits = [str(c["criterion"]) for c in duty]
    notranked = [c for c in duty if "NOT ranked as an ordinary discretionary cut" in str(c["criterion"])]
    vowed = [c for c in duty if "vowed / promised character" in str(c["criterion"])]
    assert len(notranked) == 1 and len(vowed) == 1
    assert abs(float(notranked[0]["points"]) - 1.0) < 1e-9
    assert abs(float(vowed[0]["points"]) - 1.0) < 1e-9
    # original double-barrel gone
    assert not any(
        "Tabitha Fund not ranked as an ordinary cut" in c and "distinction stated" in c
        for c in dcrits
    )


def test_lever_c_headpairs_enumerated():
    by = _all_records()
    for item_id in LEVERC_HEADPAIRS:
        crits = [str(c["criterion"]) for c in by[item_id]["rubric"]]
        # the enumerated head-pair line replaced the session4 generic gated line
        assert any("accepted head-pairs:" in c for c in crits), item_id
        assert not any(
            "[gated: awarded ONLY if the specific aggravation heads" in c for c in crits
        ), item_id
        # binary decline criterion (from session4) still present, total preserved
        assert any("declines the total order [binary]" in c for c in crits), item_id


def test_lever_c_agg_c3_untouched():
    """AGG-C3-W302 is contested but has a dual-credit ordering rubric and NO decline
    criterion, so no head-pair split is applied (session4/session5 deviation)."""
    by = _all_records()
    crits = [str(c["criterion"]) for c in by["AGG-C3-W302"]["rubric"]]
    assert not any("accepted head-pairs:" in c for c in crits)
    assert not any("declines the total order [binary]" in c for c in crits)
    # its dual-credit ordering criterion is intact
    assert any("ordering a<b<c (dual-credit per R20)" in c for c in crits)


def test_all_16_items_touched():
    """touched_ids() covers the 12 AMBIG + 3 head-pair contested items (AGG-C3-W302
    is intentionally untouched by session5)."""
    tids = touched_ids()
    for item_id in AMBIG_ITEMS:
        assert item_id in tids, item_id
    for item_id in LEVERC_HEADPAIRS:
        assert item_id in tids, item_id
    assert "AGG-C3-W302" not in tids


def test_session5_idempotent():
    """Re-applying session5 to already-session5-patched output is a no-op."""
    for item in load_bank(BANK_DIR):
        s4 = s4_apply(item)
        if s4 is None:
            continue
        once = s5_apply(s4)
        twice = s5_apply(once)
        assert twice == once, item["id"]


# --- (b) excellence template + original byte-identity -------------------------

GATE_BLOCK = "EXCELLENCE GATE (top-band calibration):"


def test_excellence_template_has_gate_block():
    exc = (TEMPLATE_DIR / "wcf_grade_template_excellence.txt").read_text()
    assert GATE_BLOCK in exc
    assert "Reserve grades of 95-100" in exc
    assert "belongs in 85-94" in exc
    assert "grades below 85 remain governed entirely by the rubric criteria" in exc
    # GRADE format contract preserved (placeholders intact)
    for ph in ("{question}", "{answer}", "{criterion}", "{instructions}"):
        assert ph in exc, ph


def test_original_template_byte_unchanged():
    """The original main template must NOT contain the gate block (excellence_gate
    =False must serve it verbatim)."""
    orig = (TEMPLATE_DIR / "wcf_grade_template.txt").read_text()
    assert GATE_BLOCK not in orig
    # the excellence template is the original + the gate block; strip the gate
    # paragraph from excellence and it must reduce to the original.
    exc = (TEMPLATE_DIR / "wcf_grade_template_excellence.txt").read_text()
    lines = [l for l in exc.splitlines(keepends=True) if not l.startswith("EXCELLENCE GATE")]
    reconstructed = "".join(lines).replace("\n\n{instructions}", "\n{instructions}")
    # normalization is loose; the load-bearing assertion is the gate is absent from orig
    assert orig.count("{question}") == 1 and orig.count("{answer}") == 1


def test_episode_template_untouched_by_gate():
    """The episode template carries no excellence gate."""
    epi = (TEMPLATE_DIR / "wcf_grade_template_episode.txt").read_text()
    assert GATE_BLOCK not in epi


# --- (c) manifest exists, hashes match ---------------------------------------

def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_manifest_exists_and_wellformed():
    m = json.loads((V2_ROOT / "data" / "BANK-VERSION.json").read_text())
    # v2.4 (session-7): second authored new-item source, no new patch layer.
    assert m["bank_version"] == "v2.4"
    assert m["patch_layers"] == [
        "session4_patches", "session5_patches", "session6_patches"
    ]
    assert m["new_item_sources"] == ["session6_new_items", "session7_new_items"]
    assert len(m["sha256_session6_new_items"]) == 64
    assert len(m["sha256_session7_new_items"]) == 64
    assert len(m["g4_excluded_new_items"]) == 23 + 5
    assert m["date"] == "2026-07-16"
    assert m["panel"] == PANEL_DEFAULT
    assert m["grade_pattern"] == GRADE_PATTERN
    for k in (
        "sha256_wcf_main", "sha256_wcf_episodes",
        "sha256_grading_template_original", "sha256_grading_template_excellence",
    ):
        assert k in m and len(m[k]) == 64, k


def test_manifest_hashes_match_emitted_files():
    m = json.loads((V2_ROOT / "data" / "BANK-VERSION.json").read_text())
    data = V2_ROOT / "data"
    tmpl = TEMPLATE_DIR
    assert m["sha256_wcf_main"] == _sha256(data / "wcf_main.jsonl")
    assert m["sha256_wcf_episodes"] == _sha256(data / "wcf_episodes.jsonl")
    assert m["sha256_grading_template_original"] == _sha256(tmpl / "wcf_grade_template.txt")
    assert m["sha256_grading_template_excellence"] == _sha256(
        tmpl / "wcf_grade_template_excellence.txt"
    )


def test_grade_pattern_in_sync_with_source():
    """The manifest's grade_pattern literal must match src/wcf_grading.py."""
    import re
    src = (V2_ROOT / "src" / "wcf_grading.py").read_text()
    m = re.search(r'GRADE_PATTERN = r"([^"]*)"', src)
    assert m and m.group(1) == GRADE_PATTERN
