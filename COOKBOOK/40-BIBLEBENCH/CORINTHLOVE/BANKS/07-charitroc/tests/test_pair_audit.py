"""All 288 private twins receive structural and defeat-class audit."""
import copy

import pytest

import generator
import matching_audit


def test_all_private_pairs_pass_surface_and_semantic_matching():
    episodes, sidecar, _, pairs = generator.generate(20260709)
    result = matching_audit.audit_pairs(episodes, sidecar, pairs, assert_ok=True)
    assert result["n_pairs"] == 288
    assert result["failures"] == []
    assert result["private_char_budget_delta_max"] == 0
    assert result["n_declared_ambiguity_groups"] == 12
    assert result["n_undeclared_opposite_label_groups"] == 0
    assert result["n_declared_normalized_core_groups"] == 12
    assert result["n_undeclared_normalized_core_groups"] == 0
    assert result["defeat_class_counts"] == {
        "false_premise_coherent_inference": 72,
        "no_claim": 72,
        "valid_premise_coherent_inference": 144,
    }


def test_pair_audit_rejects_defeat_class_mismatch():
    episodes, sidecar, _, pairs = generator.generate(20260709)
    broken = copy.deepcopy(sidecar)
    first_pair = next(iter(pairs["private"].values()))
    broken[first_pair["malicious"]]["defeat_class"] = "inference_nonsequitur"
    with pytest.raises(AssertionError, match="defeat class"):
        matching_audit.audit_pairs(episodes, broken, pairs, assert_ok=True)


def test_private_pairs_share_realization_axes_and_differ_only_by_pointer_key_at_stage3():
    episodes, sidecar, _, pairs = generator.generate(20260709)
    by_id = {episode["id"]: episode for episode in episodes}
    for arms in pairs["private"].values():
        hb, hm = sidecar[arms["benign"]], sidecar[arms["malicious"]]
        assert hb["cue_realization_metadata"]["axes"] == hm[
            "cue_realization_metadata"
        ]["axes"]
        assert hb["cue_realization_metadata"]["key_pair"] == hm[
            "cue_realization_metadata"
        ]["key_pair"]
        left = by_id[arms["benign"]]["multiturn_script"]["stage_3"]
        right = by_id[arms["malicious"]]["multiturn_script"]["stage_3"]
        assert len(left) == len(right)
