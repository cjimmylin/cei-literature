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


def test_export_part_b_selects_unresolved_cells():
    recs = _bank("01-goodsamaritan", 5, ["m1"])
    # mark 2 as needing adjudication
    recs[0]["scalar_adjudicated"] = None
    recs[1]["refusal_tag"] = "pending_adjudication"
    for r in recs[2:]:
        r["scalar_adjudicated"] = 0.5
        r["judge_report"] = {"verdicts": [{}, {}], "disagreements": []}
    units = ls.export_part_b("01-goodsamaritan", recs)
    assert len(units) == 2
    assert all(u["unit_id"].startswith("01-goodsamaritan-B") for u in units)
    # blind: no model/judge fields leak into the exported unit
    assert all("model" in u and "scalar" not in json_dumps(u).lower() for u in units)


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
