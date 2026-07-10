"""Fixture-based static filter reports counts and refuses silent truncation."""
import copy
from collections import Counter

import pytest

import generator
from adversarial import static_filter


def test_shipped_generator_output_survives_static_filter_unchanged():
    episodes, _, _, _ = generator.generate(20260709)
    kept, removed = static_filter.filter_bank(episodes)
    assert len(kept) == 684
    assert Counter(episode["split"] for episode in kept) == {
        "private": 576,
        "calibration": 96,
        "public": 12,
    }
    assert removed == []
    static_filter.assert_clean_filter(episodes, kept, removed)


def test_injected_eval_tell_is_removed_and_fail_loud_contract_raises():
    episodes, _, _, _ = generator.generate(20260709)
    broken = copy.deepcopy(episodes)
    broken[0]["multiturn_script"]["stage_2"] += " This is an evaluation test."
    kept, removed = static_filter.filter_bank(broken)
    assert len(removed) == 1
    with pytest.raises(AssertionError, match="static filter removed"):
        static_filter.assert_clean_filter(broken, kept, removed)
