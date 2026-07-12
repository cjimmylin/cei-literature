"""RED: Part A label-sample drawing (human-label protocol §2, §9).

Deterministic (seed 20260710), stratified, fail-loud on an unfillable hard minimum,
blind to judge outputs. Emits provenance jsonl + a blinded CSV (no model/judge fields).
"""
import pytest

from walkworthy import label_sample as ls


def _rec(design, item_id, model, difficulty="hard", stratum="a", area="A",
         lexical_fired=False):
    return {"item_id": item_id, "design": design, "model": model,
            "difficulty": difficulty, "stratum": stratum, "area": area,
            "administrations": [{"label": "main", "response": f"response text for {item_id}"}],
            "refusal_lexical": {"main": {"is_refusal": lexical_fired}},
            "judge_report": {"verdicts": [{"scores": {}}, {"scores": {}}]}}


def _bank(design, n_items, models, **kw):
    recs = []
    for i in range(n_items):
        for m in models:
            recs.append(_rec(design, f"{design}-I{i:02d}", m, **kw))
    return recs


def test_draw_is_deterministic():
    recs = _bank("01-goodsamaritan", 40, ["m1", "m2", "m3"])
    a = ls.draw_part_a("01-goodsamaritan", recs, {}, target=30)
    b = ls.draw_part_a("01-goodsamaritan", recs, {}, target=30)
    ids_a = [(r["item_id"], r["model"]) for r in a["selected"]]
    ids_b = [(r["item_id"], r["model"]) for r in b["selected"]]
    assert ids_a == ids_b and len(ids_a) == 30


def test_distinct_items_and_sut_balance():
    recs = _bank("01-goodsamaritan", 40, ["m1", "m2", "m3"])
    out = ls.draw_part_a("01-goodsamaritan", recs, {}, target=30)
    items = {r["item_id"] for r in out["selected"]}
    assert len(items) >= 20                     # protocol: >= 20 distinct items
    per_model = {}
    for r in out["selected"]:
        per_model[r["model"]] = per_model.get(r["model"], 0) + 1
    assert max(per_model.values()) - min(per_model.values()) <= 2    # balanced across SUTs


def test_hard_minimums_lexical_and_stratum_c():
    recs = _bank("01-goodsamaritan", 30, ["m1", "m2"])
    # inject 5 lexical-fired + 3 stratum-c distinct-item cells
    for i in range(5):
        recs.append(_rec("01-goodsamaritan", f"01-goodsamaritan-LEX{i}", "m1", lexical_fired=True))
    for i in range(3):
        recs.append(_rec("01-goodsamaritan", f"01-goodsamaritan-C{i}", "m2", stratum="c"))
    out = ls.draw_part_a("01-goodsamaritan", recs, {}, target=30)
    lex = sum(1 for r in out["selected"]
              if any(v.get("is_refusal") for v in r["refusal_lexical"].values()))
    cc = sum(1 for r in out["selected"] if r["stratum"] == "c")
    assert lex >= 5 and cc >= 3


def test_fail_loud_when_target_unfillable():
    recs = _bank("01-goodsamaritan", 5, ["m1"])       # only 5 cells, target 30
    with pytest.raises(ls.LabelSampleError):
        ls.draw_part_a("01-goodsamaritan", recs, {}, target=30)


def _disagreement(cell, scale="categorical", needs=True):
    return {"cell": cell, "values": ["a", "b"], "scale": scale,
            "adjudicated": None, "needs_adjudication": needs}


def test_export_part_b_emits_one_unit_per_unresolved_cell():
    recs = _bank("01-goodsamaritan", 3, ["m1"])
    recs[0]["judge_report"]["disagreements"] = [
        _disagreement("action_class"), _disagreement("rationale_quality", "ordinal")]
    recs[1]["judge_report"]["disagreements"] = [
        _disagreement("action_class"), _disagreement("ignored", needs=False)]
    recs[2]["scalar_adjudicated"] = None  # retired record-level selector: not a cell

    units = ls.export_part_b("01-goodsamaritan", recs)

    assert [u["cell"] for u in units] == [
        "action_class", "rationale_quality", "action_class"]
    assert len({u["unit_id"] for u in units}) == 3
    assert all("values" not in u and "judge" not in json_dumps(u).lower() for u in units)


def test_export_part_b_attaches_turn_specific_parent_context():
    rec = _rec("02-twomasters", "WW-02-X", "m1")
    rec["administrations"] = [{
        "label": "main", "response": "legacy first response",
        "turns": [
            {"index": 1, "user_text": "u1", "response": "r1"},
            {"index": 2, "user_text": "u2", "response": "r2"},
        ],
    }]
    rec["judge_report"]["disagreements"] = [_disagreement("2:turn_state")]

    unit = ls.export_part_b("02-twomasters", [rec])[0]

    assert unit["cell"] == "2:turn_state"
    assert "u2" in unit["context_and_response"]
    assert "r2" in unit["context_and_response"]
    assert "r1" not in unit["context_and_response"]


def test_export_part_b_attaches_terminal_artifact_context():
    rec = _rec("07-seventyseven", "WW-07-X", "m1")
    rec["administrations"] = [{
        "label": "main", "response": "legacy first response",
        "turns": [
            {"index": 1, "user_text": "u1", "response": "r1"},
            {"index": 2, "user_text": "u2", "response": "r2"},
        ],
        "terminal_user_text": "write the final note",
        "terminal_response": "the final note",
    }]
    rec["judge_report"]["disagreements"] = [_disagreement("3:arc_conformance")]

    unit = ls.export_part_b("07-seventyseven", [rec])[0]

    assert "write the final note" in unit["context_and_response"]
    assert "the final note" in unit["context_and_response"]
    assert "r2" not in unit["context_and_response"]


def test_export_part_b_all_uses_fr17_wave_order_then_item_id():
    recs = []
    for design, item in [("01-goodsamaritan", "I2"), ("02-twomasters", "I9"),
                         ("02-twomasters", "I1"), ("08-vocationfork", "I0")]:
        rec = _rec(design, item, "m1")
        rec["judge_report"]["disagreements"] = [_disagreement("outcome")]
        recs.append(rec)

    units = ls.export_part_b_all(recs)

    assert [(u["design"], u["item_id"]) for u in units] == [
        ("02-twomasters", "I1"), ("02-twomasters", "I9"),
        ("01-goodsamaritan", "I2"), ("08-vocationfork", "I0")]


def test_export_part_b_routes_09_arbiter_and_failed_05_reparse_without_third_judge():
    rec09 = _rec("09-doubleedge", "WW-09-X", "m1")
    rec09["refusal_tags"] = {"arbiter": "pending_adjudication"}
    rec05 = _rec("05-ordoamoris", "WW-05-X", "m1")
    rec05["allocation_reparse_failed"] = True

    units = ls.export_part_b_all([rec09, rec05])

    assert [(u["design"], u["cell"], u["route"]) for u in units] == [
        ("05-ordoamoris", "allocation_parse", "05-reparse-failed"),
        ("09-doubleedge", "arbiter_first", "09-arbiter-direct")]


def test_emit_part_b_separates_blind_rows_from_provenance(tmp_path):
    rec = _rec("01-goodsamaritan", "WW-01-X", "secret-model")
    rec["judge_report"]["disagreements"] = [_disagreement("action_class")]

    n = ls.emit_part_b("01-goodsamaritan", [rec], tmp_path)

    blind = (tmp_path / "01-goodsamaritan-partB.jsonl").read_text()
    provenance = (tmp_path / "01-goodsamaritan-partB-provenance.jsonl").read_text()
    assert n == 1
    assert "secret-model" not in blind
    assert "context_and_response" in blind and "action_class" in blind
    assert "secret-model" in provenance
    assert "context_and_response" not in provenance


def json_dumps(o):
    import json as _j
    return _j.dumps(o)


def test_blind_csv_has_no_model_or_judge_fields():
    recs = _bank("01-goodsamaritan", 40, ["m1", "m2", "m3"])
    out = ls.draw_part_a("01-goodsamaritan", recs, {}, target=30)
    csv_text = ls.render_blind_csv("01-goodsamaritan", out["selected"])
    assert "m1" not in csv_text and "m2" not in csv_text
    assert "judge" not in csv_text.lower() and "scalar" not in csv_text.lower()
    # PR-3 detector-validation columns are present (Q-R1 / Q-R2)
    assert "Q-R1" in csv_text and "Q-R2" in csv_text
