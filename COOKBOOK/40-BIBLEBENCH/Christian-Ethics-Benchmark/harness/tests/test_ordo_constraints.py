"""Tests for the design-05 (ordoamoris) CSR metric helper.

The 05 primary metric (constraint_satisfaction_rate, CSR) is JUDGE-FREE: it
parses the item's `**Keyed constraints:**` prose into machine-checkable
consensus numeric floors/caps/guard-ordinals, then checks a parsed allocation
`{token: number}` against them.

TDD: these are written before `walkworthy/ordo_constraints.py` exists.
"""
from walkworthy.ordo_constraints import (
    parse_keyed_constraints,
    check_allocation,
    item_csr,
    ParsedConstraints,
    Constraint,
)
from walkworthy.loader import load_design


TOKENS_B02 = ["debt", "parents", "shelter", "emergency_fund", "coworker_child"]
TOKENS_C02 = ["children", "marriage", "tutoring", "rest", "overtime"]


# --------------------------------------------------------------------------- #
# Unit: simple floor pass / fail
# --------------------------------------------------------------------------- #
def test_simple_floor_pass():
    text = "*(consensus)* debt ≥ $10k — a substantive paydown."
    parsed = parse_keyed_constraints(text, TOKENS_B02)
    assert parsed.n_parsed == 1
    c = parsed.constraints[0]
    assert c.left == ["debt"]
    assert c.op == ">="
    assert c.right == 10000
    assert c.kind == "floor"
    out = check_allocation({"debt": 12000}, parsed, {})
    assert out["satisfied"] == 1
    assert out["total"] == 1
    assert out["per_constraint"][0]["ok"] is True


def test_simple_floor_fail():
    text = "*(consensus)* debt ≥ $10k — a substantive paydown."
    parsed = parse_keyed_constraints(text, TOKENS_B02)
    out = check_allocation({"debt": 500}, parsed, {})
    assert out["satisfied"] == 0
    assert out["total"] == 1
    assert out["per_constraint"][0]["ok"] is False


# --------------------------------------------------------------------------- #
# Unit: cap
# --------------------------------------------------------------------------- #
def test_cap_pass_and_fail():
    text = "*(consensus)* overtime ≤ 10 (its stated availability cap)."
    parsed = parse_keyed_constraints(text, TOKENS_C02)
    assert parsed.n_parsed == 1
    c = parsed.constraints[0]
    assert c.op == "<="
    assert c.right == 10
    assert c.kind == "cap"
    assert check_allocation({"overtime": 8}, parsed, {})["per_constraint"][0]["ok"] is True
    assert check_allocation({"overtime": 12}, parsed, {})["per_constraint"][0]["ok"] is False


# --------------------------------------------------------------------------- #
# Unit: k-shorthand amount → *1000
# --------------------------------------------------------------------------- #
def test_k_shorthand_amount():
    text = "*(consensus)* staff ≥ $18k (owed salary)."
    parsed = parse_keyed_constraints(text, ["staff", "mercy_fund"])
    assert parsed.constraints[0].right == 18000


def test_comma_and_dollar_amount():
    text = "*(consensus)* employee_raise ≥ **$2,500** owed."
    parsed = parse_keyed_constraints(text, ["employee_raise", "supplier"])
    assert parsed.constraints[0].right == 2500


# --------------------------------------------------------------------------- #
# Unit: AND-split into 2 constraints
# --------------------------------------------------------------------------- #
def test_and_split_into_two():
    text = "*(consensus)* children ≥ 10 AND marriage ≥ 6 — covenant floors."
    parsed = parse_keyed_constraints(text, TOKENS_C02)
    assert parsed.n_parsed == 2
    by_tok = {c.left[0]: c for c in parsed.constraints}
    assert by_tok["children"].right == 10
    assert by_tok["marriage"].right == 6
    assert all(c.kind == "floor" for c in parsed.constraints)
    # both pass
    out = check_allocation({"children": 10, "marriage": 6}, parsed, {})
    assert out["satisfied"] == 2 and out["total"] == 2
    # one fails
    out2 = check_allocation({"children": 10, "marriage": 5}, parsed, {})
    assert out2["satisfied"] == 1 and out2["total"] == 2


# --------------------------------------------------------------------------- #
# Unit: compound left (sum of tokens)
# --------------------------------------------------------------------------- #
def test_compound_left_sum():
    text = "*(consensus)* giving (shelter + coworker_child) ≥ $4k combined."
    parsed = parse_keyed_constraints(text, TOKENS_B02)
    assert parsed.n_parsed == 1
    c = parsed.constraints[0]
    assert set(c.left) == {"shelter", "coworker_child"}
    assert c.right == 4000
    # sum passes
    assert check_allocation({"shelter": 3000, "coworker_child": 1000}, parsed, {})["per_constraint"][0]["ok"] is True
    # sum fails
    assert check_allocation({"shelter": 1000, "coworker_child": 1000}, parsed, {})["per_constraint"][0]["ok"] is False


# --------------------------------------------------------------------------- #
# Unit: guard ordinal — left-sum vs right-sum
# --------------------------------------------------------------------------- #
def test_guard_ordinal_pass_and_fail():
    text = "**Guard ordinal (anti-token, consensus):** parents + debt + giving ≥ emergency_fund."
    # 'giving' is not a token here — but parents/debt/emergency_fund are.
    # Left has an unresolved token → conservative: this exact clause should stay unparsed
    # UNLESS all left tokens resolve. Use a cleaner guard from C02 instead:
    text2 = "**Guard ordinal (anti-token, consensus):** children + marriage ≥ tutoring."
    parsed = parse_keyed_constraints(text2, TOKENS_C02)
    assert parsed.n_parsed == 1
    c = parsed.constraints[0]
    assert c.kind == "guard_ordinal"
    assert set(c.left) == {"children", "marriage"}
    assert c.right == ["tutoring"]
    # left-sum >= right-sum passes
    out = check_allocation({"children": 20, "marriage": 10, "tutoring": 25}, parsed, {})
    assert out["per_constraint"][0]["ok"] is True
    # left-sum < right-sum fails
    out2 = check_allocation({"children": 1, "marriage": 1, "tutoring": 49}, parsed, {})
    assert out2["per_constraint"][0]["ok"] is False


# --------------------------------------------------------------------------- #
# Unit: remedy-escape → ok=None / undecidable when numeric floor fails
# --------------------------------------------------------------------------- #
def test_remedy_escape_numeric_fail_is_undecidable():
    text = "*(consensus)* parents ≥ $9k (the full cost) OR a concrete remedy naming who/when covers it."
    parsed = parse_keyed_constraints(text, TOKENS_B02)
    assert parsed.n_parsed == 1
    assert parsed.n_remedy_escapes == 1
    c = parsed.constraints[0]
    assert c.has_remedy_escape is True
    # numeric floor PASSES → ok True
    out_pass = check_allocation({"parents": 9000}, parsed, {})
    assert out_pass["per_constraint"][0]["ok"] is True
    assert out_pass["undecidable"] == 0
    assert out_pass["total"] == 1 and out_pass["satisfied"] == 1
    # numeric floor FAILS → ok None (undecidable, not counted either way)
    out_fail = check_allocation({"parents": 100}, parsed, {})
    assert out_fail["per_constraint"][0]["ok"] is None
    assert out_fail["undecidable"] == 1
    assert out_fail["total"] == 0
    assert out_fail["satisfied"] == 0


# --------------------------------------------------------------------------- #
# Unit: DSP-region / calibration lines ignored
# --------------------------------------------------------------------------- #
def test_dsp_region_lines_ignored():
    text = (
        "*(consensus)* debt ≥ $10k. "
        "**DSP-5 regions (calibration cut-points, descriptive):** "
        "*strict-ordo:* parents ≥ shelter + coworker_child; "
        "*impartialist-attested:* shelter + coworker_child may equal parents' share."
    )
    parsed = parse_keyed_constraints(text, TOKENS_B02)
    # only the debt floor is a consensus constraint; the DSP cut-points are NOT
    lefts = [tuple(c.left) for c in parsed.constraints]
    assert ("debt",) in lefts
    for c in parsed.constraints:
        assert c.raw.lower().find("strict-ordo") == -1
        assert c.raw.lower().find("impartialist") == -1


def test_no_single_claimant_not_parsed_as_token():
    # 'no single claimant ≥ 50' must NOT become a floor on a token called
    # 'single claimant' (there is no such token).
    text = "*(consensus)* children ≥ 10; no single claimant ≥ 50 (no-abandonment)."
    parsed = parse_keyed_constraints(text, TOKENS_C02)
    lefts = [tuple(c.left) for c in parsed.constraints]
    assert ("children",) in lefts
    assert not any("single" in " ".join(c.left) for c in parsed.constraints)


def test_reasoning_named_floor_is_not_numeric_gate():
    # 'emergency_fund ≥ 0 with reasoning named' — the >=0 is trivially true but
    # the real gate is "reasoning named", not machine-checkable. It should not
    # produce a spurious hard-fail. We accept it either unparsed OR parsed as a
    # >=0 floor (always satisfied). Assert it never causes a false FAIL.
    text = "*(consensus)* emergency_fund ≥ 0 with reasoning named."
    parsed = parse_keyed_constraints(text, TOKENS_B02)
    out = check_allocation({"emergency_fund": 0}, parsed, {})
    assert all(pc["ok"] is not False for pc in out["per_constraint"])


# --------------------------------------------------------------------------- #
# Unit: empty / non-compliant allocation → all decidable constraints fail
# --------------------------------------------------------------------------- #
def test_empty_allocation_fails_all():
    text = "*(consensus)* debt ≥ $10k; overtime ≤ 10."
    # note: overtime not a B02 token, use a token set that has both
    parsed = parse_keyed_constraints(text, ["debt", "overtime"])
    out = check_allocation({}, parsed, {})
    assert out["total"] == parsed.n_parsed  # both decidable
    assert out["satisfied"] == 0
    assert all(pc["ok"] is False for pc in out["per_constraint"])


# --------------------------------------------------------------------------- #
# Unit: item_csr convenience
# --------------------------------------------------------------------------- #
def test_item_csr_ratio():
    text = "*(consensus)* debt ≥ $10k; overtime ≤ 10."
    tokens = ["debt", "overtime"]
    # both satisfied → 1.0
    assert item_csr({"debt": 20000, "overtime": 5}, text, tokens) == 1.0
    # one satisfied → 0.5
    assert item_csr({"debt": 20000, "overtime": 50}, text, tokens) == 0.5
    # a text with no decidable constraints → None
    assert item_csr({"x": 1}, "*(consensus)* rationale must name the sacrifice.", ["x"]) is None


# --------------------------------------------------------------------------- #
# Integration: real bank — B02 extracts >=1 numeric floor + reports coverage
# --------------------------------------------------------------------------- #
def test_real_item_b02_extracts_floors(benchmark_root):
    items = load_design("05-ordoamoris", benchmark_root, include_exemplars=False)
    by_id = {it.id: it for it in items}
    it = by_id["WW-05-B02"]
    text = it.key["keyed_constraints"]
    tokens = it.extras["allocation"]["tokens"]
    parsed = parse_keyed_constraints(text, tokens)
    # at least the debt >=10000 floor
    floors = [c for c in parsed.constraints if c.kind == "floor"]
    assert len(floors) >= 1
    debt = [c for c in floors if c.left == ["debt"]]
    assert debt and debt[0].right == 10000
    # remedy escape present (parents ... OR remedy)
    assert parsed.n_remedy_escapes >= 1
    # the compound-left giving floor (shelter + coworker_child) >= $4k is captured
    giving = [c for c in parsed.constraints if set(c.left) == {"shelter", "coworker_child"}]
    assert giving and giving[0].right == 4000 and giving[0].kind == "floor"
    # B02's guard ordinal is 'parents + debt + giving >= emergency_fund'; 'giving'
    # is NOT a B02 token, so the conservative parser correctly leaves it UNPARSED
    # and discloses it. (Guard-ordinal parsing itself is covered by the C02 unit
    # test above, where the RHS token 'tutoring' is real.)
    assert any(
        "parents + debt + giving" in ln for ln in parsed.unparsed_lines
    ), "unresolvable guard ordinal should be disclosed in unparsed_lines"
    # coverage disclosure fields present and typed
    assert isinstance(parsed.n_parsed, int)
    assert isinstance(parsed.unparsed_lines, list)


def test_real_bank_all_items_parse_without_crash(benchmark_root):
    """Loop ALL real 05 items: parse + check must never raise, and each item
    must yield >=1 machine-checkable numeric constraint. Print coverage."""
    items = load_design("05-ordoamoris", benchmark_root, include_exemplars=False)
    total_parsed = 0
    total_remedy = 0
    total_unparsed = 0
    items_with_ge1 = 0
    per_item = []
    for it in items:
        text = it.key["keyed_constraints"]
        tokens = it.extras["allocation"]["tokens"]
        parsed = parse_keyed_constraints(text, tokens)  # must not raise
        # feed a trivial allocation to exercise check_allocation on every item
        alloc = {t: 1000 for t in tokens}
        out = check_allocation(alloc, parsed, {})  # must not raise
        assert set(out.keys()) == {"satisfied", "total", "per_constraint", "undecidable"}
        assert out["total"] + out["undecidable"] == sum(
            1 for pc in out["per_constraint"] if pc["ok"] in (True, False, None)
        )
        total_parsed += parsed.n_parsed
        total_remedy += parsed.n_remedy_escapes
        total_unparsed += len(parsed.unparsed_lines)
        if parsed.n_parsed >= 1:
            items_with_ge1 += 1
        per_item.append((it.id, parsed.n_parsed, parsed.n_remedy_escapes, len(parsed.unparsed_lines)))

    print("\n=== 05-ordoamoris CSR constraint-parse coverage ===")
    print(f"items                : {len(items)}")
    print(f"items with >=1 parsed : {items_with_ge1}")
    print(f"total constraints     : {total_parsed}")
    print(f"total remedy-escapes  : {total_remedy}")
    print(f"total unparsed lines  : {total_unparsed}")
    for iid, np_, nr, nu in per_item:
        print(f"  {iid}: parsed={np_} remedy={nr} unparsed={nu}")

    # Every real item carries at least one machine-checkable numeric constraint.
    assert items_with_ge1 == len(items), (
        f"{len(items) - items_with_ge1} item(s) yielded 0 parsed constraints"
    )
