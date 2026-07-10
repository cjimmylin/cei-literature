"""Tests for the WCF-Bench mock-first harness skeleton.

Run:
    /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
        COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q

No network is touched anywhere (MockModelClient only).
"""

from __future__ import annotations

import os
import sys

import pytest

# Make the harness package importable without installation.
HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import (  # noqa: E402
    LoaderError,
    MockModelClient,
    load_items,
    score_aggravate_ordinal,
    score_prooftext_anchors,
)
from wcfbench.loader import _validate_record  # noqa: E402  (internal, tested directly)
from wcfbench.scorers import INCOMPARABLE  # noqa: E402

FIXTURES_DIR = os.path.join(HARNESS_ROOT, "fixtures")


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------

def test_loads_all_fixtures():
    items = load_items(FIXTURES_DIR)
    assert len(items) == 3
    ids = {it.id for it in items}
    assert ids == {"AGG-C6-W301", "AGG-C5-W304", "PROOF-C8-W302"}
    # every rubric keypoint has numeric points; total_points is positive
    for it in items:
        assert it.total_points > 0
        for kp in it.rubric:
            assert isinstance(kp.points, float)


def test_fixtures_have_expected_shapes():
    items = {it.id: it for it in load_items(FIXTURES_DIR)}
    agg = items["AGG-C6-W301"]
    assert agg.design == "aggravate"
    assert agg.extra["gold_order"] == ["a", "b", "c"]  # orderable
    inc = items["AGG-C5-W304"]
    assert inc.extra["gold_order"].strip().lower() == INCOMPARABLE  # incomparable
    proof = items["PROOF-C8-W302"]
    assert proof.design == "prooftext"
    # at least one anchored keypoint the mechanical scorer can act on
    assert any(kp.anchor for kp in proof.rubric)


def test_malformed_record_raises():
    # missing required 'rubric' field
    bad = {
        "id": "BAD-C1-001",
        "design": "aggravate",
        "track": "B",
        "tier": "T2",
        "commandments": ["C1"],
        "anchors": ["WLC Q150 — test"],
        "stem": "stem",
        "key": "key",
        "status": "expanded",
        "author": "opus",
        # 'rubric' deliberately omitted
    }
    with pytest.raises(LoaderError) as ei:
        _validate_record(bad, "inline-bad")
    assert "rubric" in str(ei.value)


def test_malformed_rubric_points_raise():
    bad = {
        "id": "BAD-C1-002",
        "design": "aggravate",
        "track": "B",
        "tier": "T2",
        "commandments": ["C1"],
        "anchors": ["WLC Q150 — test"],
        "stem": "stem",
        "key": "key",
        "status": "expanded",
        "author": "opus",
        "rubric": [{"points": "not-a-number", "criterion": "x"}],
    }
    with pytest.raises(LoaderError) as ei:
        _validate_record(bad, "inline-bad")
    assert "points" in str(ei.value)


def test_rubric_axis_field_loads():
    # R24: OPEN rubric keypoints carry an axis tag (matter|manner|end) so the
    # per-keypoint award scorer can compute each axis fraction mechanically.
    rec = _validate_record({
        "id": "OK-C1-004", "design": "mending", "track": "B", "tier": "T3",
        "commandments": ["C1"], "anchors": ["WLC Q145 — test"], "stem": "s", "key": "k",
        "status": "reviewed", "author": "opus",
        "rubric": [
            {"points": 2, "criterion": "substance", "anchor": "WLC Q145", "axis": "matter"},
            {"points": 1, "criterion": "courtesy", "anchor": "WLC Q135", "axis": "manner"},
            {"points": 1, "criterion": "chief end", "anchor": "WSC Q1", "axis": "end"},
        ],
    }, "inline-ok")
    assert [kp.axis for kp in rec.rubric] == ["matter", "manner", "end"]


def test_rubric_axis_defaults_none():
    # An untagged keypoint (earlier-wave items, or non-axis scorers) has axis=None
    # — the numeric fallback path handles those, so tagging is not mandatory.
    rec = _validate_record({
        "id": "OK-C1-005", "design": "aggravate", "track": "B", "tier": "T2",
        "commandments": ["C1"], "anchors": ["WLC Q150 — test"], "stem": "s", "key": "k",
        "status": "expanded", "author": "opus",
        "rubric": [{"points": 1, "criterion": "x", "anchor": "WLC Q150"}],
    }, "inline-ok")
    assert rec.rubric[0].axis is None


def test_bad_axis_raises():
    bad = {
        "id": "BAD-C1-006", "design": "mending", "track": "B", "tier": "T3",
        "commandments": ["C1"], "anchors": ["WLC Q145 — test"], "stem": "s", "key": "k",
        "status": "reviewed", "author": "opus",
        "rubric": [{"points": 1, "criterion": "x", "axis": "substance"}],  # not matter|manner|end
    }
    with pytest.raises(LoaderError) as ei:
        _validate_record(bad, "inline-bad")
    assert "axis" in str(ei.value)


def test_bad_enum_raises():
    bad = {
        "id": "BAD-C1-003",
        "design": "aggravate",
        "track": "Z",  # invalid track
        "tier": "T2",
        "commandments": ["C1"],
        "anchors": ["WLC Q150 — test"],
        "stem": "stem",
        "key": "key",
        "status": "expanded",
        "author": "opus",
        "rubric": [{"points": 1, "criterion": "x"}],
    }
    with pytest.raises(LoaderError) as ei:
        _validate_record(bad, "inline-bad")
    assert "track" in str(ei.value)


# ---------------------------------------------------------------------------
# AGGRAVATE ordinal scorer — orderable rank-set
# ---------------------------------------------------------------------------

def test_correct_ranking_full_credit():
    s = score_aggravate_ordinal(gold_key=["a", "b", "c"], model_ranking=["a", "b", "c"], ordering_max=2.0)
    assert s.concordance == 1.0
    assert s.ordering_points == 2.0
    assert s.passed_ordering is True
    assert s.transitive is True


def test_wrong_ranking_reduced_or_zero():
    # fully inverted order -> tau = -1 -> zero credit
    inverted = score_aggravate_ordinal(gold_key=["a", "b", "c"], model_ranking=["c", "b", "a"], ordering_max=2.0)
    assert inverted.concordance == -1.0
    assert inverted.ordering_points == 0.0
    assert inverted.passed_ordering is False

    # one pair swapped -> partial credit strictly between 0 and full
    partial = score_aggravate_ordinal(gold_key=["a", "b", "c"], model_ranking=["b", "a", "c"], ordering_max=2.0)
    assert 0.0 < partial.ordering_points < 2.0
    assert partial.passed_ordering is False


def test_declining_an_orderable_item_scores_zero():
    s = score_aggravate_ordinal(gold_key=["a", "b", "c"], model_ranking=INCOMPARABLE, ordering_max=2.0)
    assert s.ordering_points == 0.0
    assert s.declined is True


def test_malformed_model_order_scores_zero():
    # repeated label -> not a valid strict ranking
    s = score_aggravate_ordinal(gold_key=["a", "b", "c"], model_ranking=["a", "a", "b"], ordering_max=2.0)
    assert s.ordering_points == 0.0
    assert s.transitive is False


# ---------------------------------------------------------------------------
# AGGRAVATE ordinal scorer — incomparable item
# ---------------------------------------------------------------------------

def test_incomparable_confident_order_scores_zero():
    s = score_aggravate_ordinal(gold_key=INCOMPARABLE, model_ranking=["a", "b"], ordering_max=1.5)
    assert s.incomparable_item is True
    assert s.declined is False
    assert s.ordering_points == 0.0
    assert s.passed_ordering is False


def test_incomparable_decline_scores_full():
    s = score_aggravate_ordinal(gold_key=INCOMPARABLE, model_ranking=INCOMPARABLE, ordering_max=1.5)
    assert s.incomparable_item is True
    assert s.declined is True
    assert s.ordering_points == 1.5
    assert s.passed_ordering is True


# ---------------------------------------------------------------------------
# PROOFTEXT anchor scorer
# ---------------------------------------------------------------------------

def _proof_item():
    return {it.id: it for it in load_items(FIXTURES_DIR)}["PROOF-C8-W302"]


def test_prooftext_citing_scores_higher_than_not():
    item = _proof_item()
    counter = {"counter-texts supplied": ["1 Tim 6:17-18", "1 Tim 5:8"]}

    good = (
        "The LOVE of money is the root of all evil. See 1 Tim 6:17-18 and "
        "1 Tim 5:8. WLC Q141 makes provision a duty; WCF 1.9 (Scripture "
        "interprets Scripture); WLC Q142 names covetousness."
    )
    bad = "Money is bad, you should give it all away. Be humble."

    good_score = score_prooftext_anchors(item.rubric, good, counter_tokens=counter)
    bad_score = score_prooftext_anchors(item.rubric, bad, counter_tokens=counter)

    assert good_score.points > bad_score.points
    assert bad_score.points == 0.0
    # the citing response should match multiple anchored keypoints
    assert len(good_score.matched) >= 3
    # and the anchored max is the sum of anchored keypoints' points
    assert good_score.max_points > 0


def test_prooftext_counter_text_requirement_bites():
    item = _proof_item()
    counter = {"counter-texts supplied": ["1 Tim 6:17-18", "1 Tim 5:8"]}
    # cites the anchors (WCF 1.9, Q141, Q142) but omits the required counter-texts
    cites_no_counter = "WCF 1.9 and WLC Q141 and WLC Q142 are relevant here."
    s = score_prooftext_anchors(item.rubric, cites_no_counter, counter_tokens=counter)
    # the counter-text keypoint (also anchored WCF 1.9) must be withheld
    assert any("counter-texts" in m.lower() for m in s.missed)


# ---------------------------------------------------------------------------
# MockModelClient — no network, scriptable, logged
# ---------------------------------------------------------------------------

def test_mock_client_is_scriptable_and_offline():
    client = MockModelClient(default_response="<none>")
    client.register("AGG-C6-W301", "a < b < c")
    assert client.complete("rank these", item_id="AGG-C6-W301") == "a < b < c"
    # unregistered id -> default response (exercises the empty-answer path)
    assert client.complete("rank these", item_id="UNKNOWN") == "<none>"
    # call log records both calls in order
    assert client.call_log == [("rank these", "AGG-C6-W301"), ("rank these", "UNKNOWN")]


# ---------------------------------------------------------------------------
# End-to-end: loader -> mock client -> scorers on the real fixtures
# ---------------------------------------------------------------------------

def test_end_to_end_dryrun_paths():
    items = {it.id: it for it in load_items(FIXTURES_DIR)}
    client = MockModelClient()
    client.register("PROOF-C8-W302", (
        "The LOVE of money (1 Tim 6:10). See 1 Tim 6:17-18 and 1 Tim 5:8. "
        "WLC Q141, WCF 1.9, WLC Q142."
    ))

    # AGGRAVATE orderable
    agg = items["AGG-C6-W301"]
    agg_score = score_aggravate_ordinal(
        gold_key=agg.extra["gold_order"], model_ranking=["a", "b", "c"],
        ordering_max=agg.rubric[0].points,
    )
    assert agg_score.passed_ordering

    # AGGRAVATE incomparable
    inc = items["AGG-C5-W304"]
    inc_score = score_aggravate_ordinal(
        gold_key=inc.extra["gold_order"], model_ranking=INCOMPARABLE,
        ordering_max=inc.rubric[0].points,
    )
    assert inc_score.passed_ordering

    # PROOFTEXT
    proof = items["PROOF-C8-W302"]
    text = client.complete(prompt=proof.stem, item_id=proof.id)
    proof_score = score_prooftext_anchors(
        proof.rubric, text,
        counter_tokens={"counter-texts supplied": ["1 Tim 6:17-18", "1 Tim 5:8"]},
    )
    assert proof_score.points > 0
