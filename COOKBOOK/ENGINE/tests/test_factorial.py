"""Tests for the typed factorial spec + fractional design (CRUX §3.1, §4).

Spec facts encoded here:
- Full grid is >= 1,440 cells (§4).
- The pilot does NOT populate the full grid; it screens to a named <= ~60-cell
  fractional design (§4).
- Main-effect marginals (value_pair, stakes, uncertainty, ...) are FIXED
  (balanced); higher-order interactions are deliberately CONFOUNDED and the
  confounding structure is PUBLISHED.
"""
from crux import factorial, values


def test_factor_levels_match_spec():
    f = factorial.FACTORS
    assert len(f["value_pair"]) == 10
    assert f["stakes"] == ["minor", "serious", "severe"]
    assert f["uncertainty"] == ["complete_info", "one_unknown", "irreducible"]
    assert f["beneficiary"] == ["self", "other", "third_party", "group"]
    assert len(f["relationship"]) == 2
    assert len(f["reversibility"]) == 2


def test_full_grid_is_at_least_1440_cells():
    grid = factorial.full_grid()
    assert len(grid) >= 1440


def test_full_grid_cells_are_unique():
    grid = factorial.full_grid()
    keyed = {tuple(sorted(c.items())) for c in grid}
    assert len(keyed) == len(grid)


def test_fractional_design_is_at_most_60_cells():
    design = factorial.fractional_design()
    assert len(design.cells) <= 60


def test_fractional_design_main_effects_are_balanced():
    design = factorial.fractional_design(n_cells=60)
    n = len(design.cells)
    for factor, levels in factorial.FACTORS.items():
        if n % len(levels) != 0:
            continue  # non-divisible factors can't be perfectly balanced
        counts = {}
        for cell in design.cells:
            counts[cell[factor]] = counts.get(cell[factor], 0) + 1
        expected = n // len(levels)
        assert set(counts.values()) == {expected}, (
            f"{factor} not balanced: {counts}"
        )


def test_fractional_design_is_deterministic_for_a_seed():
    a = factorial.fractional_design(seed=7)
    b = factorial.fractional_design(seed=7)
    assert a.cells == b.cells


def test_fractional_design_varies_with_seed():
    a = factorial.fractional_design(seed=1)
    b = factorial.fractional_design(seed=2)
    assert a.cells != b.cells


def test_fractional_design_publishes_confounding_structure():
    design = factorial.fractional_design()
    # A named design with a serializable, non-empty confounding report.
    assert design.name
    report = design.confounding_report()
    assert isinstance(report, dict)
    assert report["design"]
    assert report["confounded_factors"]  # which factors are aliased/uncontrolled
    assert "max_pairwise_imbalance" in report


def test_every_cell_uses_a_real_value_pair():
    design = factorial.fractional_design()
    known = {frozenset(p) for p in values.value_pairs()}
    for cell in design.cells:
        assert frozenset(cell["value_pair"]) in known
