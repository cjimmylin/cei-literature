"""Tests for disagreement.py — cross-judge disagreement clusters (the Fable input).

A downstream Fable session adjudicates the items where the cross-family judges
disagree most. This module walks a RunReport and, for every panel-graded cell
(OPEN triaxial or CONTESTED adherence), computes the per-axis spread across judges
and a split-defensibility flag, sorted worst-first. Pure/deterministic; no network.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.runner import RunReport, ModelRunReport, PerItemResult  # noqa: E402
from wcfbench.routing import OPEN, CONTESTED, ORDINAL  # noqa: E402
from wcfbench.disagreement import (  # noqa: E402
    summarize_disagreement,
    DisagreementCell,
)


def _open_result(item_id, model, per_judge):
    return PerItemResult(model=model, item_id=item_id, design="complicit", commandment="C8",
                         tier="T2", track="A", kind=OPEN, judge_raw=per_judge)


def _contested_result(item_id, model, per_judge):
    return PerItemResult(model=model, item_id=item_id, design="aggravate", commandment="C5",
                         tier="T2b", track="B", kind=CONTESTED, contested=True, judge_raw=per_judge)


def _report(results, model="sut-1"):
    return RunReport(reports={model: ModelRunReport(model=model, results=results)})


# ===========================================================================

def test_open_cell_axis_spread_computed():
    r = _report([_open_result("COMP-C8-W301", "sut-1", [
        {"name": "gpt", "family": "openai", "matter": 2.0, "manner": 1.0, "end": 1.0},
        {"name": "gemini", "family": "google", "matter": 0.0, "manner": 1.0, "end": 1.0},
    ])])
    cells = summarize_disagreement(r)
    assert len(cells) == 1
    cell = cells[0]
    assert isinstance(cell, DisagreementCell)
    assert cell.axis_spreads["matter"] == pytest.approx(2.0)
    assert cell.axis_spreads["manner"] == pytest.approx(0.0)
    assert cell.max_spread == pytest.approx(2.0)
    assert cell.n_judges == 2


def test_contested_split_defensibility_flagged():
    r = _report([_contested_result("AGG-C5-W304", "sut-1", [
        {"name": "gpt", "family": "openai", "disclosure": 0.9, "coherence": 0.8,
         "position_defensible": True, "settled_core_fraction": 1.0},
        {"name": "gemini", "family": "google", "disclosure": 0.4, "coherence": 0.5,
         "position_defensible": False, "settled_core_fraction": 1.0},
    ])])
    cells = summarize_disagreement(r)
    assert cells[0].split_defensible is True
    assert cells[0].axis_spreads["disclosure"] == pytest.approx(0.5)


def test_cells_sorted_worst_first():
    r = _report([
        _open_result("LOW", "sut-1", [
            {"name": "a", "family": "openai", "matter": 1.0, "manner": 1.0, "end": 1.0},
            {"name": "b", "family": "google", "matter": 1.1, "manner": 1.0, "end": 1.0}]),
        _open_result("HIGH", "sut-1", [
            {"name": "a", "family": "openai", "matter": 2.0, "manner": 0.0, "end": 1.0},
            {"name": "b", "family": "google", "matter": 0.0, "manner": 2.0, "end": 1.0}]),
    ])
    cells = summarize_disagreement(r)
    assert [c.item_id for c in cells] == ["HIGH", "LOW"]   # HIGH spread first


def test_fenced_raw_value_is_preserved_but_excluded_from_eligible_ranking():
    r = _report([
        _open_result("FENCED-ARTIFACT", "sut-1", [
            {"name": "a", "family": "openai", "matter": 0.0, "manner": 1.0, "end": 1.0,
             "eligible_surfaces": ["open_award"], "scale_defect": {}},
            {"name": "b", "family": "google", "matter": 0.1, "manner": 1.0, "end": 1.0,
             "eligible_surfaces": ["open_award"], "scale_defect": {}},
            {"name": "fenced", "family": "x-ai", "matter": 2.5, "manner": 1.0, "end": 1.0,
             "eligible_surfaces": ["open_award"], "scale_defect": {"matter": True}},
            {"name": "shadow", "family": "cohere", "matter": 2.0, "manner": 1.0, "end": 1.0,
             "eligible_surfaces": ["coherence"], "scale_defect": {}},
        ]),
        _open_result("REAL-DISAGREEMENT", "sut-1", [
            {"name": "a", "family": "openai", "matter": 0.0, "manner": 1.0, "end": 1.0,
             "eligible_surfaces": ["open_award"], "scale_defect": {}},
            {"name": "b", "family": "google", "matter": 0.8, "manner": 1.0, "end": 1.0,
             "eligible_surfaces": ["open_award"], "scale_defect": {}},
        ]),
    ])

    cells = summarize_disagreement(r)

    assert [c.item_id for c in cells] == ["REAL-DISAGREEMENT", "FENCED-ARTIFACT"]
    artifact = cells[1]
    assert artifact.max_spread == pytest.approx(2.5)
    assert artifact.eligible_spread == pytest.approx(0.1)
    assert artifact.eligible_axis_spreads["matter"] == pytest.approx(0.1)
    by_name = {v["name"]: v for v in artifact.judge_values["matter"]}
    assert by_name["fenced"] == {
        "name": "fenced", "family": "x-ai", "value": 2.5,
        "eligible": True, "scale_defect": True,
    }
    assert by_name["shadow"]["eligible"] is False
    assert by_name["shadow"]["scale_defect"] is False


def test_mechanical_items_without_judge_raw_are_skipped():
    mech = PerItemResult(model="sut-1", item_id="AGG-C6-W301", design="aggravate",
                         commandment="C6", tier="T2a", track="B", kind=ORDINAL,
                         fraction=1.0, scored=True)  # no judge_raw
    r = _report([mech, _open_result("COMP-C8-W301", "sut-1", [
        {"name": "a", "family": "openai", "matter": 1.0, "manner": 1.0, "end": 1.0},
        {"name": "b", "family": "google", "matter": 1.0, "manner": 1.0, "end": 1.0}])])
    cells = summarize_disagreement(r)
    assert [c.item_id for c in cells] == ["COMP-C8-W301"]


def test_single_judge_cell_has_zero_spread():
    r = _report([_open_result("X", "sut-1", [
        {"name": "a", "family": "openai", "matter": 2.0, "manner": 1.0, "end": 1.0}])])
    cells = summarize_disagreement(r)
    assert cells[0].max_spread == pytest.approx(0.0)
    assert cells[0].n_judges == 1


def test_multi_model_cells_carry_the_model():
    r = RunReport(reports={
        "sut-A": ModelRunReport(model="sut-A", results=[_open_result("I", "sut-A", [
            {"name": "a", "family": "openai", "matter": 2.0, "manner": 1, "end": 1},
            {"name": "b", "family": "google", "matter": 0.0, "manner": 1, "end": 1}])]),
        "sut-B": ModelRunReport(model="sut-B", results=[_open_result("I", "sut-B", [
            {"name": "a", "family": "openai", "matter": 1.0, "manner": 1, "end": 1},
            {"name": "b", "family": "google", "matter": 1.0, "manner": 1, "end": 1}])]),
    })
    cells = summarize_disagreement(r)
    by_model = {(c.item_id, c.model): c for c in cells}
    assert by_model[("I", "sut-A")].max_spread == pytest.approx(2.0)
    assert by_model[("I", "sut-B")].max_spread == pytest.approx(0.0)
