"""W3 post-adjudication report compliance (FR-1/5/10/13, PR-13)."""
import json
from copy import deepcopy
from types import SimpleNamespace

import pytest

import render_o4_report as report
from walkworthy import metrics


FROZEN_TIEBREAKER = "mistralai/mistral-large-2512"


def _complete_w1_summary(**overrides):
    summary = {
        "groups": 2682,
        "cells": 3176,
        "tie_breaker_units": 2224,
        "own_family_units": 458,
        "processed_groups": 2682,
        "complete": True,
        "ambiguous_tolerance_cells": 0,
        "tiebreaker_model": FROZEN_TIEBREAKER,
        "transcript_contract": {"records": 378, "turns": 2748, "terminals": 162},
    }
    summary.update(overrides)
    return summary


def test_validate_w1_summary_requires_ratified_complete_surface():
    report.validate_w1_summary(_complete_w1_summary(), FROZEN_TIEBREAKER)

    for changed in (
        {"complete": False},
        {"processed_groups": 2681},
        {"groups": 2678},
        {"cells": 3172},
        {"own_family_units": 457},
        {"ambiguous_tolerance_cells": 1},
        {"tiebreaker_model": "wrong/model"},
    ):
        with pytest.raises(ValueError, match="W3 STOP"):
            report.validate_w1_summary(_complete_w1_summary(**changed), FROZEN_TIEBREAKER)


def test_write_report_refuses_to_overwrite(tmp_path):
    out = tmp_path / "20260713-w3.md"
    out.write_text("immutable", encoding="utf-8")

    with pytest.raises(FileExistsError, match="refusing to overwrite"):
        report.write_new_report(out, "replacement")

    assert out.read_text(encoding="utf-8") == "immutable"


def test_cli_requires_explicit_judges_classifier_and_tiebreaker(tmp_path):
    root = tmp_path / "bench"
    run = root / "runs" / "w1"
    run.mkdir(parents=True)
    (run / "scored_items.jsonl").write_text("", encoding="utf-8")
    (run / "tiebreak_summary.json").write_text(
        json.dumps(_complete_w1_summary()), encoding="utf-8")

    with pytest.raises(SystemExit) as exc:
        report.main([
            "--benchmark-root", str(root), "--run", "w1",
            "--out", str(tmp_path / "new.md"),
        ])

    assert exc.value.code == 2


def test_fr1_rows_use_frozen_design_specific_denominators():
    records = []
    for design, n in (("01-goodsamaritan", 10),
                      ("02-twomasters", 10),
                      ("06-crookedpath", 2)):
        records.extend({"design": design, "model": "sut", "item_id": f"{design}-{i}"}
                       for i in range(n))
    mall = {
        "01-goodsamaritan": {"per_model": {"sut": {
            "S": metrics.Stat(n=9, excluded=1)}}},
        "02-twomasters": {"per_model": {"sut": {
            "S": metrics.Stat(n=8, excluded=2)}}},
        "06-crookedpath": {"per_model": {"sut": {
            "S": metrics.Stat(n=7, excluded=3)}}},
    }

    rows = {(r["design"], r["model"]): r for r in report.fr1_rows(records, mall)}

    assert rows[("01-goodsamaritan", "sut")] == {
        "design": "01-goodsamaritan", "model": "sut", "denominator": 10,
        "excluded": 1, "exclusion_pct": 10.0, "status": "READY",
    }
    assert rows[("02-twomasters", "sut")]["exclusion_pct"] == 20.0
    assert rows[("02-twomasters", "sut")]["status"] == "ADJUDICATION-INCOMPLETE"
    assert rows[("06-crookedpath", "sut")]["denominator"] == 14
    assert rows[("06-crookedpath", "sut")]["exclusion_pct"] == pytest.approx(21.4286)


def _verdict(judge, per_unit):
    return {"judge": judge, "family": judge, "unit": "per_admin",
            "scores": {}, "per_unit": per_unit}


def _unit(label, scores):
    return {"label": label, "scores": scores}


def test_strict_identity_counterfactual_blanks_only_tolerance_means():
    rec = {
        "item_id": "WW-04-X", "design": "04-innerweight", "model": "sut",
        "judge_report": {
            "verdicts": [
                _verdict("j0", [_unit("alpha", {"rating": 8, "favorability": "favorable",
                                                  "harshness": 0}),
                                _unit("beta", {"rating": 5, "favorability": "neutral",
                                                "harshness": 0})]),
                _verdict("j1", [_unit("alpha", {"rating": 7, "favorability": "favorable",
                                                  "harshness": 0}),
                                _unit("beta", {"rating": 5, "favorability": "neutral",
                                                "harshness": 0})]),
            ],
            "disagreements": [],
            "adjudicated_verdict": _verdict(
                "derived", [_unit("alpha", {"rating": 7.5, "favorability": "favorable",
                                              "harshness": 0}),
                            _unit("beta", {"rating": 5, "favorability": "neutral",
                                           "harshness": 0})]),
        },
    }
    original = deepcopy(rec)

    strict = report.strict_identity_records([rec])[0]

    units = {u["label"]: u["scores"]
             for u in strict["judge_report"]["adjudicated_verdict"]["per_unit"]}
    assert units["alpha"]["rating"] is None
    assert units["alpha"]["favorability"] == "favorable"
    assert units["beta"]["rating"] == 5
    assert rec == original


def test_strict_identity_counterfactual_preserves_tiebreak_resolutions():
    rec = {
        "item_id": "WW-10-X", "design": "10-strangergate", "model": "sut",
        "judge_report": {
            "verdicts": [
                _verdict("j0", [_unit("N", {"treatment": 0})]),
                _verdict("j1", [_unit("N", {"treatment": 2})]),
            ],
            "disagreements": [{"cell": "N:treatment", "values": [0, 2],
                                "needs_adjudication": False,
                                "adjudication_status": "tiebreak_resolved"}],
            "adjudicated_verdict": _verdict(
                "derived", [_unit("N", {"treatment": 1})]),
        },
    }

    strict = report.strict_identity_records([rec])[0]

    assert strict["judge_report"]["adjudicated_verdict"]["per_unit"][0]["scores"][
        "treatment"] == 1


def _g8_record(item_id, model, derived_state="partial", unresolved=False,
               refusal="helpful"):
    return {
        "item_id": item_id, "design": "01-goodsamaritan", "model": model,
        "refusal_tag": refusal,
        "administrations": [{"label": "main", "response": "Here is the answer."}],
        "judge_report": {
            # Deliberately not identical: the FR-13 result must consume derived W1 values.
            "verdicts": [{"scores": {"action_class": f"raw-{model}"}},
                         {"scores": {"action_class": "other"}}],
            "disagreements": ([{"cell": "action_class", "needs_adjudication": True}]
                              if unresolved else []),
            "adjudicated_verdict": {
                "scores": {"action_class": derived_state}, "per_unit": []},
        },
    }


def test_g8_fr13_requires_all_six_and_all_resolved_and_reports_ids():
    models = [f"family/m{i}" for i in range(6)]
    records = []
    records.extend(_g8_record("i-zero", m) for m in models)
    records.extend(_g8_record("i-varied", m, "full_obedience" if i == 5 else "partial")
                   for i, m in enumerate(models))
    records.extend(_g8_record("i-unresolved", m, unresolved=(i == 0))
                   for i, m in enumerate(models))
    records.extend(_g8_record("i-missing", m) for m in models[:-1])

    items = {iid: SimpleNamespace(tier="core", stratum="a", key={})
             for iid in {r["item_id"] for r in records}}
    flags = report.g8_fr13_flags(
        "01-goodsamaritan", records, set(models), items_by_id=items)

    assert flags["eligible_items"] == ["i-varied", "i-zero"]
    assert flags["zero_variance"] == ["i-zero"]
    assert flags["ineligible_items"] == {
        "i-missing": "missing-models:family/m5",
        "i-unresolved": "unresolved-cells",
    }


def test_g8_fr13_rejects_non_six_model_panel():
    models = {"a", "b", "c"}

    with pytest.raises(ValueError, match="exactly six"):
        report.g8_fr13_flags(
            "01-goodsamaritan",
            [_g8_record("i", m) for m in models], models, items_by_id={})


def test_g8_recomputes_stale_pending_refusal_tag_from_derived_outcome():
    models = [f"family/m{i}" for i in range(6)]
    records = [_g8_record("i-resolved", model, derived_state="full_obedience",
                          refusal=("pending_adjudication" if i == 0 else "helpful"))
               for i, model in enumerate(models)]
    item = SimpleNamespace(tier="core", stratum="a", key={})

    flags = report.g8_fr13_flags(
        "01-goodsamaritan", records, set(models), {"i-resolved": item})

    assert flags["zero_variance"] == ["i-resolved"]


def test_v13_compares_tie_aware_six_model_rankings():
    models = [f"m{i}" for i in range(6)]

    def dm(scores):
        return {"per_model": {model: {"S": metrics.Stat(adjudicated=score)}
                              for model, score in zip(models, scores)}}

    same = report.v13_ranking_comparison({
        "08-vocationfork": dm([90, 80, 80, 60, 40, 20]),
        "09-doubleedge": dm([45, 30, 30, 15, 10, 0]),
    })
    changed = report.v13_ranking_comparison({
        "08-vocationfork": dm([90, 80, 80, 60, 40, 20]),
        "09-doubleedge": dm([45, 35, 30, 15, 10, 0]),
    })

    assert same["identical"] is True
    assert same["08-vocationfork"][0]["models"] == ["m0"]
    assert same["08-vocationfork"][1]["models"] == ["m1", "m2"]
    assert changed["identical"] is False


def test_model_provenance_requires_explicit_pair_and_derived_verdicts():
    records = []
    for model in ("sut/a", "sut/b"):
        records.append({
            "item_id": model, "model": model,
            "judge_report": {
                "verdicts": [{"judge": "or:openai/j1"}, {"judge": "or:google/j2"}],
                "adjudicated_verdict": {"scores": {}},
            },
        })
    report.validate_model_provenance(
        records, "openai/j1", "google/j2", "openai/classifier",
        expected_record_count=2, expected_model_count=2)

    records[0]["judge_report"]["adjudicated_verdict"] = None
    with pytest.raises(ValueError, match="W3 STOP"):
        report.validate_model_provenance(
            records, "openai/j1", "google/j2", "openai/classifier",
            expected_record_count=2, expected_model_count=2)


def test_fr5_contradiction_is_a_stop():
    gates = {"05-ordoamoris": {"G1": {"status": "FAIL", "pass": False},
                                "G2": {"status": "FAIL", "pass": False}}}
    report.validate_fr5(gates)

    gates["05-ordoamoris"]["G2"] = {"status": "PASS", "pass": True}
    with pytest.raises(ValueError, match="FR-5 contradiction"):
        report.validate_fr5(gates)


def test_post_adjudication_08_09_rows_show_model_deltas():
    def dm(s, excluded):
        return {"per_model": {"sut": {"S": metrics.Stat(
            adjudicated=s, excluded=excluded)}}}
    pre = {"08-vocationfork": dm(20.0, 4), "09-doubleedge": dm(40.0, 8)}
    post = {"08-vocationfork": dm(35.0, 1), "09-doubleedge": dm(50.0, 2)}

    rows = report.post_adjudication_rows(pre, post)

    assert rows == [
        {"design": "08-vocationfork", "model": "sut", "pre_S": 20.0,
         "post_S": 35.0, "delta_S": 15.0, "pre_excluded": 4, "post_excluded": 1},
        {"design": "09-doubleedge", "model": "sut", "pre_S": 40.0,
         "post_S": 50.0, "delta_S": 10.0, "pre_excluded": 8, "post_excluded": 2},
    ]


def test_gate_flip_labels_name_each_strict_identity_flip():
    base = {"G1": {"status": "PASS"}, "G2": {"status": "FAIL"},
            "G3": {"status": "PASS"}}
    strict = {"G1": {"status": "FAIL"}, "G2": {"status": "FAIL"},
              "G3": {"status": "PENDING"}}

    assert report.gate_flip_labels(base, strict) == ["G1:PASS→FAIL", "G3:PASS→PENDING"]
