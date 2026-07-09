"""Unit tests for fairgold.stats numeric primitives (synthetic inputs only)."""
from __future__ import annotations

import math

import numpy as np
import pytest

from fairgold.stats import (
    jensen_shannon,
    kendall_tau,
    maximal_lottery,
    normalize,
    normalized_entropy,
    shannon_entropy,
    total_variation,
)


def test_normalize_sums_to_one():
    d = normalize({"a": 2, "b": 2})
    assert d == {"a": 0.5, "b": 0.5}


def test_normalize_rejects_negative():
    with pytest.raises(ValueError):
        normalize({"a": -1, "b": 2})


def test_normalize_rejects_zero_total():
    with pytest.raises(ValueError):
        normalize({"a": 0, "b": 0})


def test_shannon_entropy_uniform_binary_is_one_bit():
    assert shannon_entropy({"a": 1, "b": 1}) == pytest.approx(1.0)


def test_normalized_entropy_degenerate_is_zero():
    assert normalized_entropy({"a": 1, "b": 0}) == 0.0


def test_normalized_entropy_uniform_is_one():
    assert normalized_entropy({"a": 1, "b": 1, "c": 1}) == pytest.approx(1.0)


def test_total_variation_bounds():
    assert total_variation({"a": 1, "b": 0}, {"a": 1, "b": 0}) == pytest.approx(0.0)
    assert total_variation({"a": 1, "b": 0}, {"a": 0, "b": 1}) == pytest.approx(1.0)


def test_total_variation_half():
    tv = total_variation({"a": 1.0, "b": 0.0}, {"a": 0.5, "b": 0.5})
    assert tv == pytest.approx(0.5)


def test_jensen_shannon_identical_is_zero():
    assert jensen_shannon({"a": 0.3, "b": 0.7}, {"a": 0.3, "b": 0.7}) == pytest.approx(0.0)


def test_jensen_shannon_disjoint_is_one():
    # JS distance between disjoint-support distributions is 1 (base-2).
    assert jensen_shannon({"a": 1.0, "b": 0.0}, {"a": 0.0, "b": 1.0}) == pytest.approx(1.0)


def test_kendall_tau_identical():
    assert kendall_tau([3, 2, 1], [3, 2, 1]) == pytest.approx(1.0)


def test_kendall_tau_reversed():
    assert kendall_tau([1, 2, 3], [3, 2, 1]) == pytest.approx(-1.0)


def test_kendall_tau_constant_vector_is_stable():
    # One rule gives everyone the same score -> no discordant info -> 1.0.
    assert kendall_tau([1, 1, 1], [3, 2, 1]) == pytest.approx(1.0)


def test_kendall_tau_single_model():
    assert kendall_tau([5], [2]) == pytest.approx(1.0)


def test_maximal_lottery_condorcet_cycle_is_uniform():
    # Skew-symmetric 3-cycle margin matrix (rock-paper-scissors).
    M = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]], dtype=float)
    p = maximal_lottery(["A", "B", "C"], M)
    for opt in ("A", "B", "C"):
        assert p[opt] == pytest.approx(1.0 / 3.0, abs=1e-6)


def test_maximal_lottery_dominant_option():
    # A beats B and C; the lottery must put all mass on A.
    M = np.array([[0, 3, 3], [-3, 0, 1], [-3, -1, 0]], dtype=float)
    p = maximal_lottery(["A", "B", "C"], M)
    assert p["A"] == pytest.approx(1.0, abs=1e-6)
    assert p["B"] == pytest.approx(0.0, abs=1e-6)
    assert p["C"] == pytest.approx(0.0, abs=1e-6)


def test_maximal_lottery_probabilities_sum_to_one():
    M = np.array([[0, 2, -1], [-2, 0, 3], [1, -3, 0]], dtype=float)
    p = maximal_lottery(["A", "B", "C"], M)
    assert sum(p.values()) == pytest.approx(1.0)
    assert all(v >= -1e-9 for v in p.values())


def test_maximal_lottery_single_option():
    assert maximal_lottery(["only"], np.zeros((1, 1))) == {"only": 1.0}
