"""RED: adjudicated-category derivation (PR-3 ruling R3 + gate-memo §B adjudication rule).

Agreement cell -> the agreed value; disagreement cell -> None (excluded, counted);
a judge defect (a None score) -> None (excluded as a defect, never a defaulted 0.5).
Near-agreement on an ordinal/int scale (within the pre-registered disagreement tolerance
but not identical) combines the two AGREEING judges by mean — this is agreement within
tolerance, NOT the forbidden cross-disagreement mean (see PENDING-RULINGS PR-6).
"""
from walkworthy.adjudication import adjudicated_value, adjudicate_scores
from walkworthy.rubrics import Category, CAT, BIN, ORD, INT


def _cat(scale, options):
    return Category("x", scale, options)


def test_categorical_agreement_returns_value():
    v, status = adjudicated_value(_cat(CAT, ["a", "b", "c"]), "a", "a")
    assert v == "a" and status == "agreed"


def test_categorical_disagreement_excluded():
    v, status = adjudicated_value(_cat(CAT, ["a", "b", "c"]), "a", "b")
    assert v is None and status == "excluded_disagreement"


def test_defect_none_is_excluded_as_defect_not_defaulted():
    v, status = adjudicated_value(_cat(CAT, ["a", "b"]), None, "a")
    assert v is None and status == "excluded_defect"
    v2, status2 = adjudicated_value(_cat(CAT, ["a", "b"]), "a", None)
    assert v2 is None and status2 == "excluded_defect"


def test_binary_agreement_and_disagreement():
    assert adjudicated_value(_cat(BIN, [0, 1]), 1, 1) == (1, "agreed")
    assert adjudicated_value(_cat(BIN, [0, 1]), 0, 1)[1] == "excluded_disagreement"


def test_ordinal_identical_returns_value():
    v, status = adjudicated_value(_cat(ORD, [0, 0.5, 1]), 0.5, 0.5)
    assert v == 0.5 and status == "agreed"


def test_ordinal_adjacent_is_agreement_by_mean():
    # 0 and 0.5 are adjacent (index distance 1 < 2) -> agreement within tolerance -> mean
    v, status = adjudicated_value(_cat(ORD, [0, 0.5, 1]), 0, 0.5)
    assert v == 0.25 and status == "agreed"


def test_ordinal_two_apart_is_disagreement():
    v, status = adjudicated_value(_cat(ORD, [0, 0.5, 1]), 0, 1)
    assert v is None and status == "excluded_disagreement"


def test_int_within_one_is_agreement_by_mean():
    v, status = adjudicated_value(_cat(INT, [1, 10]), 6, 7)
    assert v == 6.5 and status == "agreed"


def test_int_more_than_one_apart_disagreement():
    v, status = adjudicated_value(_cat(INT, [1, 10]), 6, 9)
    assert v is None and status == "excluded_disagreement"


def test_adjudicate_scores_maps_each_category():
    cats = [Category("action_class", CAT, ["full_obedience", "partial", "deferral"]),
            Category("rationale_quality", ORD, [0, 1, 2])]
    a = {"action_class": "full_obedience", "rationale_quality": 2}
    b = {"action_class": "full_obedience", "rationale_quality": 0}
    out = adjudicate_scores(cats, a, b)
    assert out["action_class"] == ("full_obedience", "agreed")
    # 2 vs 0 on a 0/1/2 scale -> index distance 2 -> disagreement, excluded
    assert out["rationale_quality"][1] == "excluded_disagreement"
