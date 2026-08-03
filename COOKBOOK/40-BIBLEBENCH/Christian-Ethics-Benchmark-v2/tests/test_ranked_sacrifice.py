"""v4-A 2(c) — ranked-sacrifice scorer (spec 20260731j §2.2) with double-keying.

Covers: keyed-object validation (total order, both independent author keys),
per-item and bank-level double-keying disagreement disclosure, tie-aware Kendall
τ-b, and the two read-outs — PRIMARY binary first-sacrifice match (defined at
≥ 1 violation; full compliance on an infeasible-by-design item flags the ITEM),
SECONDARY τ-b at ≥ 3 violations with degenerate cases excluded as counts.
Remedy-escape shortfalls stay undecidable (pinned-checker semantics — the
rationale judge owns the escape). No model calls ($0).

Run: .venv/bin/python -m pytest tests/test_ranked_sacrifice.py -q
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from walkworthy_v4.ranked_sacrifice import (  # noqa: E402
    bank_key_disagreement,
    kendall_tau_b,
    key_disagreement,
    score_ranked_sacrifice,
    validate_key,
)

TOKENS = ["family", "church", "savings", "medical"]
# C1 family / C2 church / C3 savings / C4 medical — all hard floors.
CONSTRAINTS = "family >= $500; church >= $300; savings >= $400; medical >= $600"


def _key(adjudicated, author1=None, author2=None):
    return {
        "keys": {"author1": author1 or list(adjudicated),
                 "author2": author2 or list(adjudicated)},
        "adjudicated": list(adjudicated),
    }


# --------------------------------------------------------------------------- #
# keyed-object validation (total order, double-keyed)
# --------------------------------------------------------------------------- #
def test_valid_key_passes():
    assert validate_key(_key(["C4", "C2", "C3", "C1"]), 4) == []


def test_missing_author_key_fails():
    k = _key(["C1", "C2", "C3", "C4"])
    del k["keys"]["author2"]
    assert any("author2" in e for e in validate_key(k, 4))


def test_partial_order_rejected():
    k = _key(["C1", "C2", "C3", "C4"], author1=["C1", "C2"])
    assert any("author1" in e for e in validate_key(k, 4))


def test_missing_adjudicated_rejected():
    k = _key(["C1", "C2", "C3", "C4"])
    del k["adjudicated"]
    assert any("adjudicated" in e for e in validate_key(k, 4))


# --------------------------------------------------------------------------- #
# double-keying disagreement disclosure (instrument property)
# --------------------------------------------------------------------------- #
def test_identical_keys_no_disagreement():
    d = key_disagreement(["C1", "C2", "C3"], ["C1", "C2", "C3"])
    assert d["identical"] and d["first_sacrifice_agree"]
    assert d["pairwise_disagreement"] == 0.0


def test_reversed_keys_full_disagreement():
    d = key_disagreement(["C1", "C2", "C3"], ["C3", "C2", "C1"])
    assert not d["identical"] and not d["first_sacrifice_agree"]
    assert d["pairwise_disagreement"] == 1.0


def test_adjacent_swap_partial_disagreement():
    d = key_disagreement(["C1", "C2", "C3"], ["C1", "C3", "C2"])
    assert d["first_sacrifice_agree"]
    assert abs(d["pairwise_disagreement"] - 1 / 3) < 1e-9


def test_bank_disagreement_summary():
    keys = [
        _key(["C1", "C2", "C3"]),
        _key(["C1", "C2", "C3"], author2=["C2", "C1", "C3"]),
    ]
    s = bank_key_disagreement(keys)
    assert s["n_items"] == 2
    assert s["identical_rate"] == 0.5
    assert s["first_sacrifice_agreement_rate"] == 0.5


# --------------------------------------------------------------------------- #
# Kendall tau-b
# --------------------------------------------------------------------------- #
def test_tau_b_perfect_agreement_and_reversal():
    assert kendall_tau_b([1, 2, 3], [10, 20, 30]) == 1.0
    assert kendall_tau_b([1, 2, 3], [30, 20, 10]) == -1.0


def test_tau_b_tie_aware():
    # y ties on the first pair: nc=2, nd=0, n0=3, ty=1 -> 2/sqrt(3*2)
    t = kendall_tau_b([1, 2, 3], [5, 5, 9])
    assert abs(t - 2 / (3 * 2) ** 0.5) < 1e-12


def test_tau_b_undefined_cases():
    assert kendall_tau_b([1], [1]) is None
    assert kendall_tau_b([1, 2, 3], [7, 7, 7]) is None


# --------------------------------------------------------------------------- #
# PRIMARY: first-sacrifice match
# --------------------------------------------------------------------------- #
def test_primary_match_single_violation():
    # only medical (C4) violated; keyed first sacrifice = C4 -> match
    values = {"family": 500, "church": 300, "savings": 400, "medical": 0}
    r = score_ranked_sacrifice(values, CONSTRAINTS, TOKENS,
                               _key(["C4", "C2", "C3", "C1"]))
    assert r.first_sacrifice_match is True
    assert r.n_violated == 1
    assert r.tau_b is None and r.tau_excluded_reason == "fewer_than_3_violations"


def test_primary_mismatch():
    # only church (C2) violated but the key says sacrifice C4 first -> mismatch
    values = {"family": 500, "church": 0, "savings": 400, "medical": 600}
    r = score_ranked_sacrifice(values, CONSTRAINTS, TOKENS,
                               _key(["C4", "C2", "C3", "C1"]))
    assert r.first_sacrifice_match is False


def test_primary_deepest_cut_wins():
    # church cut 2/3, savings cut 1/2, medical cut fully -> C4 sacrificed first
    values = {"family": 500, "church": 100, "savings": 200, "medical": 0}
    r = score_ranked_sacrifice(values, CONSTRAINTS, TOKENS,
                               _key(["C4", "C2", "C3", "C1"]))
    assert r.first_sacrifice_match is True
    assert r.observed_order == ["C4", "C2", "C3"]


def test_primary_tie_at_top_accepts_keyed_first():
    # church and medical both cut 100 pct -> tied top set {C2, C4}
    values = {"family": 500, "church": 0, "savings": 400, "medical": 0}
    r = score_ranked_sacrifice(values, CONSTRAINTS, TOKENS,
                               _key(["C2", "C4", "C3", "C1"]))
    assert r.first_sacrifice_match is True


def test_full_compliance_flags_item_not_model():
    # satisfiable here only because the TEST budget is unconstrained — a real
    # hardened item is infeasible-by-design, so this outcome is an item defect.
    values = {"family": 500, "church": 300, "savings": 400, "medical": 600}
    r = score_ranked_sacrifice(values, CONSTRAINTS, TOKENS,
                               _key(["C4", "C2", "C3", "C1"]))
    assert r.first_sacrifice_match is None
    assert r.item_flag == "fully_compliant_on_infeasible_item"


def test_non_compliant_allocation_excluded_as_count():
    r = score_ranked_sacrifice({}, CONSTRAINTS, TOKENS,
                               _key(["C4", "C2", "C3", "C1"]))
    assert r.first_sacrifice_match is None
    assert r.primary_excluded_reason == "non_compliant_allocation"
    assert r.tau_excluded_reason == "non_compliant_allocation"


def test_invalid_key_is_item_defect():
    r = score_ranked_sacrifice({"family": 1}, CONSTRAINTS, TOKENS,
                               _key(["C4", "C2"]))
    assert r.item_flag == "invalid_key"


# --------------------------------------------------------------------------- #
# SECONDARY: tau-b over the violated subset
# --------------------------------------------------------------------------- #
def test_tau_perfect_concordance():
    # severities: C4 1.0 > C2 2/3 > C3 1/2; keyed sacrifice order C4,C2,C3
    values = {"family": 500, "church": 100, "savings": 200, "medical": 0}
    r = score_ranked_sacrifice(values, CONSTRAINTS, TOKENS,
                               _key(["C4", "C2", "C3", "C1"]))
    assert r.n_violated == 3
    assert r.tau_b == 1.0


def test_tau_perfect_reversal():
    values = {"family": 500, "church": 100, "savings": 200, "medical": 0}
    r = score_ranked_sacrifice(values, CONSTRAINTS, TOKENS,
                               _key(["C3", "C2", "C4", "C1"]))
    # keyed says C3 first, C2, then C4 — observed depth-of-cut is C4, C2, C3
    assert r.tau_b == -1.0


def test_tau_excluded_below_three_violations():
    values = {"family": 500, "church": 0, "savings": 400, "medical": 0}
    r = score_ranked_sacrifice(values, CONSTRAINTS, TOKENS,
                               _key(["C2", "C4", "C3", "C1"]))
    assert r.n_violated == 2
    assert r.tau_b is None and r.tau_excluded_reason == "fewer_than_3_violations"


# --------------------------------------------------------------------------- #
# remedy escapes stay undecidable (judge owns them)
# --------------------------------------------------------------------------- #
ESCAPE_CONSTRAINTS = ("family >= $500; church >= $300; savings >= $400; "
                      "medical >= $600 OR a concrete dated remedy plan")


def test_failing_escape_clause_is_undecidable_not_violated():
    values = {"family": 500, "church": 100, "savings": 200, "medical": 0}
    r = score_ranked_sacrifice(values, ESCAPE_CONSTRAINTS, TOKENS,
                               _key(["C2", "C3", "C1", "C4"]))
    assert r.n_undecidable == 1
    assert "C4" not in r.violated_ids
    assert r.n_violated == 2  # church, savings
    assert r.first_sacrifice_match is True  # C2 is the deepest decidable cut
