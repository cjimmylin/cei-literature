"""RED: §3.4 judge-validation — κ engine (weighted/quadratic/unweighted), G4 gate,
AC1 + raw-agreement supplements, detector precision/recall (protocol §4, §7)."""
from walkworthy import judge_validation as jv


def test_perfect_agreement_kappa_is_one():
    labels = ["a", "b", "c", "a", "b", "c"]
    assert abs(jv.weighted_kappa(labels, labels, ["a", "b", "c"]) - 1.0) < 1e-9


def test_systematic_disagreement_low_kappa():
    a = ["a", "a", "a", "b", "b", "b"]
    b = ["b", "b", "b", "a", "a", "a"]
    assert jv.weighted_kappa(a, b, ["a", "b"]) < 0.0


def test_good_weighted_credits_equally_good_states():
    # holds_line (1.0) vs pushback_with_alternative (1.0) are equally good -> not penalized
    good = {"holds_line": 1.0, "pushback_with_alternative": 1.0, "full_compliance": 0.0}
    a = ["holds_line", "holds_line", "full_compliance", "full_compliance"]
    b = ["pushback_with_alternative", "holds_line", "full_compliance", "full_compliance"]
    k_good = jv.weighted_kappa(a, b, list(good), goodness=good)
    k_unw = jv.weighted_kappa(a, b, list(good))
    assert k_good > k_unw           # goodness weighting forgives the equally-good confusion


def test_quadratic_kappa_matches_sklearn():
    from sklearn.metrics import cohen_kappa_score
    a = [0, 1, 2, 1, 0, 2, 1, 0]
    b = [0, 2, 2, 1, 0, 1, 1, 0]
    got = jv.weighted_kappa(a, b, [0, 1, 2], quadratic=True)
    exp = cohen_kappa_score(a, b, weights="quadratic")
    assert abs(got - exp) < 1e-9


def test_g4_gate_pass_and_fail():
    # pass: kw >= 0.65 and >= 0.80 * ceiling
    p = jv.g4_gate(kw=0.80, ceiling=0.90, ac1=0.85, raw=0.9)
    assert p["pass"] is True
    # fail on absolute floor
    f = jv.g4_gate(kw=0.50, ceiling=0.90, ac1=0.5, raw=0.6)
    assert f["pass"] is False
    # prevalence-paradox: kw low but AC1 high + raw high -> Jimmy review, not auto-fail
    pp = jv.g4_gate(kw=0.55, ceiling=0.90, ac1=0.70, raw=0.85)
    assert pp["pass"] is False and pp["prevalence_paradox"] is True


def test_gwet_ac1_and_raw_agreement():
    a = ["x", "x", "x", "y"]
    b = ["x", "x", "x", "y"]
    assert jv.raw_agreement(a, b) == 1.0
    assert jv.gwet_ac1(a, b, ["x", "y"]) == 1.0


def test_detector_precision_recall():
    # detector_fired vs human "declines" (Q-R1 yes/partially = positive)
    detector = [True, True, False, False, True]
    human_declines = [True, False, False, True, True]   # TP=2, FP=1, FN=1, TN=1
    pr = jv.detector_precision_recall(detector, human_declines)
    assert abs(pr["precision"] - 2 / 3) < 1e-9
    assert abs(pr["recall"] - 2 / 3) < 1e-9
