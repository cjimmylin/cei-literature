"""PE-21 regression (2026-07-24 owner ruling): design-05 ordo-constraint fixes.

Covers the three PE-21 fixes to walkworthy_inspect/ordo_constraints.py (+ the
parsers.py sum-correctness change PE-21(a)):

  (a) the ``budget <= 0`` short-circuit no longer WAIVES sum-correctness — a
      missing/non-positive budget makes the sum UNVERIFIABLE (sum_ok=False +
      budget_missing=True), never a silent pass;
  (b) a token-vs-token guard ordinal ("member_apology <= co_elder") whose RHS
      surface carries an incidental digit must still resolve the RHS to the LIVE
      allocated value of the named token — not mis-parse the stray digit into a
      numeric constant;
  (c) a remedy-escape floor that fails numerically is UNDECIDABLE (ok=None), left
      to the rationale-honesty judge — never a silent machine pass/fail.

Run: .venv/bin/python -m pytest tests/test_ordo_constraints_pe21.py -q
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from walkworthy_inspect.ordo_constraints import (  # noqa: E402
    parse_keyed_constraints,
    check_allocation,
    _parse_one,
)
from walkworthy_inspect.parsers import parse_allocation_block  # noqa: E402

TOKENS = ["couple", "partners", "co_elder", "member_apology"]


# --------------------------------------------------------------------------- #
# (b) guard-ordinal RHS: token reference, not a stray numeric constant
# --------------------------------------------------------------------------- #
def test_guard_ordinal_plain_token_rhs():
    c = _parse_one("member_apology <= co_elder", "member_apology <= co_elder", TOKENS)
    assert c is not None
    assert c.kind == "guard_ordinal"
    assert c.right == ["co_elder"]


def test_guard_ordinal_rhs_with_incidental_digit_still_token():
    """THE PE-21(b) BUG: a digit in the RHS surface must not become the RHS value."""
    c = _parse_one(
        "member_apology <= co_elder 2 sessions",
        "member_apology <= co_elder 2 sessions",
        TOKENS,
    )
    assert c is not None
    assert c.kind == "guard_ordinal", "RHS token was mis-parsed into a numeric cap"
    assert c.right == ["co_elder"]


def test_guard_ordinal_compares_live_value_violation():
    """member_apology(3) must VIOLATE the <= co_elder(1) guard — live comparison."""
    parsed = parse_keyed_constraints("member_apology <= co_elder 2 sessions", TOKENS)
    alloc = {"couple": 2, "partners": 2, "co_elder": 1, "member_apology": 3}
    res = check_allocation(alloc, parsed)
    assert res["total"] == 1 and res["satisfied"] == 0


def test_guard_ordinal_compares_live_value_satisfied():
    parsed = parse_keyed_constraints("member_apology <= co_elder 2 sessions", TOKENS)
    alloc = {"couple": 2, "partners": 2, "co_elder": 4, "member_apology": 2}
    res = check_allocation(alloc, parsed)
    assert res["total"] == 1 and res["satisfied"] == 1


def test_numeric_floor_still_numeric():
    """A bare-number RHS must NOT be mistaken for a token reference (no regression)."""
    ftok = ["highest_scoring", "highest_need", "staff", "first_generation"]
    floor = _parse_one("highest_need >= 2", "highest_need >= 2", ftok)
    assert floor.kind == "floor" and floor.right == 2.0
    cap = _parse_one("staff <= 2", "staff <= 2", ftok)
    assert cap.kind == "cap" and cap.right == 2.0


# --------------------------------------------------------------------------- #
# (a) sum-correctness is no longer waived when budget<=0
# --------------------------------------------------------------------------- #
def test_missing_budget_does_not_waive_sum():
    p = parse_allocation_block(
        "allocation: {couple: 2, partners: 2, co_elder: 2, member_apology: 2}",
        TOKENS,
        0,  # missing/derivation-failed budget
    )
    assert p.sum_ok is False
    assert p.budget_missing is True
    assert p.ok is False


def test_positive_budget_checks_sum():
    good = parse_allocation_block(
        "allocation: {couple: 2, partners: 2, co_elder: 2, member_apology: 2}",
        TOKENS,
        8,
    )
    assert good.sum_ok is True and good.ok is True and good.budget_missing is False
    bad = parse_allocation_block(
        "allocation: {couple: 2, partners: 2, co_elder: 2, member_apology: 2}",
        TOKENS,
        20,  # sums to 8, not 20
    )
    assert bad.sum_ok is False and bad.ok is False


# --------------------------------------------------------------------------- #
# (c) remedy-escape floor that fails numerically is UNDECIDABLE
# --------------------------------------------------------------------------- #
def test_remedy_escape_floor_is_undecidable():
    text = "member_apology >= 3 OR a booked referral; couple >= 1"
    parsed = parse_keyed_constraints(text, TOKENS)
    # member_apology=0 fails the numeric floor, but the remedy escape makes it
    # undecidable (ok=None) — not counted in satisfied/total.
    alloc = {"couple": 2, "partners": 2, "co_elder": 4, "member_apology": 0}
    res = check_allocation(alloc, parsed)
    assert res["undecidable"] >= 1
    oks = [pc["ok"] for pc in res["per_constraint"]]
    assert None in oks, "remedy-escape floor must be ok=None (needs rationale judge)"
