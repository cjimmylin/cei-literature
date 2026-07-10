"""Declared ambiguity controls and emitted counterbalance contracts."""
from collections import Counter, defaultdict

import pytest

import generator
import matching_audit
from lib import cue_surfaces


SEEDS = (20260709, 991117, 17, 888888)


def test_exact_opposite_label_twins_are_declared_and_capped():
    episodes, sidecar, _, _ = generator.generate(20260709)
    groups = matching_audit.exact_transcript_groups(episodes)
    opposite = matching_audit.opposite_label_transcript_groups(
        groups, sidecar
    )
    assert len(opposite) == 12
    assert {len(group) for group in opposite} == {2}
    assert {
        episode["template_family"]
        for group in opposite for episode in group
    } == set(generator.FAMILY_CODES)
    for group in opposite:
        hidden = [sidecar[episode["id"]] for episode in group]
        assert {episode["split"] for episode in group} == {"calibration"}
        assert {record["cue_variant"] for record in hidden} == {"absent"}
        assert {record["true_type"] for record in hidden} == {
            "benign", "malicious",
        }
        assert all(record["indistinguishable_control"] for record in hidden)
        assert all(
            record["latent_evidence"]["indistinguishable_control"]
            for record in hidden
        )


def test_normalized_core_opposite_label_twins_are_the_same_declared_controls():
    episodes, sidecar, _, _ = generator.generate(20260709)
    exact = matching_audit.opposite_label_transcript_groups(
        matching_audit.exact_transcript_groups(episodes), sidecar
    )
    core = matching_audit.opposite_label_transcript_groups(
        matching_audit.normalized_core_transcript_groups(episodes), sidecar
    )
    exact_ids = {frozenset(episode["id"] for episode in group) for group in exact}
    core_ids = {frozenset(episode["id"] for episode in group) for group in core}
    assert core_ids == exact_ids
    assert len(core_ids) == 12


def test_controls_are_only_calibration_absent_and_exactly_one_pair_per_family():
    episodes, sidecar, _, pairs = generator.generate(20260709)
    controls = [
        episode for episode in episodes
        if sidecar[episode["id"]]["indistinguishable_control"]
    ]
    assert len(controls) == 24
    assert Counter(episode["template_family"] for episode in controls) == {
        family: 2 for family in generator.FAMILY_CODES
    }
    assert {episode["split"] for episode in controls} == {"calibration"}
    assert {sidecar[e["id"]]["cue_variant"] for e in controls} == {"absent"}
    control_ids = {episode["id"] for episode in controls}
    controlled_pairs = [
        arms for arms in pairs["calibration"].values()
        if set(arms.values()) <= control_ids
    ]
    assert len(controlled_pairs) == 12


@pytest.mark.parametrize("seed", SEEDS)
def test_private_absent_pairs_never_collapse_to_exact_transcript_twins(seed):
    episodes, sidecar, _, pairs = generator.generate(seed)
    by_id = {episode["id"]: episode for episode in episodes}
    absent_pairs = [
        arms for arms in pairs["private"].values()
        if sidecar[arms["benign"]]["cue_variant"] == "absent"
    ]
    assert len(absent_pairs) == 72
    for arms in absent_pairs:
        hb, hm = sidecar[arms["benign"]], sidecar[arms["malicious"]]
        assert hb["initial_signal_band"] != hm["initial_signal_band"]
        assert (
            by_id[arms["benign"]]["multiturn_script"]
            != by_id[arms["malicious"]]["multiturn_script"]
        )


def test_private_emissions_span_axes_and_balance_pointer_orientation():
    episodes, sidecar, _, pairs = generator.generate(20260709)
    grouped = defaultdict(list)
    for arms in pairs["private"].values():
        hidden = sidecar[arms["benign"]]
        grouped[(hidden["latent_evidence"]["family"], hidden["cue_variant"])].append(
            hidden["cue_realization_metadata"]
        )
    assert len(grouped) == 12 * 4
    for key, rows in grouped.items():
        assert len(rows) == 6, key
        for axis in cue_surfaces.AXES:
            assert {row["axes"][axis] for row in rows} == {0, 1}, (key, axis)
        assert Counter(row["axes"]["polarity_position"] for row in rows) == {
            0: 3, 1: 3,
        }


def test_private_row_formula_and_all_emitted_axis_contingencies_are_exact():
    _, sidecar, _, pairs = generator.generate(20260709)
    by_prior = defaultdict(list)
    by_cue = defaultdict(list)
    by_family_prior = defaultdict(list)
    by_family_cue = defaultdict(list)
    for pair_id, arms in pairs["private"].items():
        family_number, combo_number = (
            int(value) - 1 for value in pair_id.rsplit("-", 2)[1:]
        )
        cue_index = combo_number // 6
        prior_index = (combo_number % 6) // 2
        realization = combo_number % 2
        hidden = sidecar[arms["benign"]]
        meta = hidden["cue_realization_metadata"]
        expected_row = (
            2 * family_number + 2 * cue_index + prior_index
            + realization + 1
        ) % 8
        assert meta["row_index"] == expected_row
        family = generator.FAMILY_CODES[family_number]
        cue = generator.CUE_VARIANTS[cue_index]
        by_prior[prior_index].append(meta)
        by_cue[cue].append(meta)
        by_family_prior[(family, prior_index)].append(meta)
        by_family_cue[(family, cue)].append(meta)

    for rows_by_cell, expected_count in (
        (by_prior, 48),
        (by_cue, 36),
        (by_family_prior, 4),
    ):
        for cell, rows in rows_by_cell.items():
            for axis in cue_surfaces.AXES:
                assert Counter(row["axes"][axis] for row in rows) == {
                    0: expected_count, 1: expected_count,
                }, (cell, axis)
    for cell, rows in by_family_cue.items():
        assert len(rows) == 6
        for axis in cue_surfaces.AXES:
            assert {row["axes"][axis] for row in rows} == {0, 1}, (
                cell, axis,
            )
        assert Counter(row["axes"]["polarity_position"] for row in rows) == {
            0: 3, 1: 3,
        }


def test_calibration_frozen_row_table_balances_every_axis_within_cue():
    assert generator.CALIBRATION_CUE_ROW_TABLE == (
        (1, 0, 1, 7, 3, 6, 6, 5, 2, 0, 4, 7),
        (0, 2, 6, 3, 1, 7, 5, 0, 7, 1, 4, 6),
        (3, 4, 5, 1, 6, 7, 1, 2, 6, 7, 0, 0),
        (0, 0, 1, 3, 2, 7, 6, 5, 4, 6, 7, 1),
    )
    _, sidecar, _, pairs = generator.generate(20260709)
    rows_by_cue = defaultdict(list)
    for pair_id, arms in pairs["calibration"].items():
        family_index, cue_index = (
            int(value) - 1 for value in pair_id.rsplit("-", 2)[1:]
        )
        hidden = sidecar[arms["benign"]]
        meta = hidden["cue_realization_metadata"]
        assert meta["row_index"] == generator.CALIBRATION_CUE_ROW_TABLE[
            cue_index
        ][family_index]
        rows_by_cue[generator.CUE_VARIANTS[cue_index]].append(meta)
    for cue, rows in rows_by_cue.items():
        assert len(rows) == 12
        for axis in cue_surfaces.AXES:
            assert Counter(row["axes"][axis] for row in rows) == {
                0: 6, 1: 6,
            }, (cue, axis)


def test_emitted_metadata_never_deterministically_maps_to_true_type():
    episodes, sidecar, _, _ = generator.generate(20260709)
    for split in ("calibration", "private"):
        domains = defaultdict(set)
        for episode in episodes:
            if episode["split"] != split:
                continue
            hidden = sidecar[episode["id"]]
            meta = hidden["cue_realization_metadata"]
            features = {
                **{f"axis:{axis}": value for axis, value in meta["axes"].items()},
                "key_pair": tuple(meta["key_pair"]),
                "source": meta["source"],
                "reliability": meta["reliability"],
            }
            for name, value in features.items():
                domains[(name, str(value))].add(hidden["true_type"])
        assert domains
        assert all(types == {"benign", "malicious"} for types in domains.values())


def test_each_calibration_family_mixes_both_pointer_keys_across_types():
    episodes, sidecar, _, _ = generator.generate(20260709)
    domains = defaultdict(set)
    for episode in episodes:
        hidden = sidecar[episode["id"]]
        if episode["split"] != "calibration":
            continue
        if hidden["cue_variant"] == "absent":
            continue
        pointer = hidden["cue_realization_metadata"]["pointer_key"]
        domains[(episode["template_family"], pointer)].add(
            hidden["true_type"]
        )
    assert len(domains) == 12 * 2
    assert all(types == {"benign", "malicious"} for types in domains.values())


def test_emitted_audit_rejects_calibration_pointer_key_type_poison():
    import copy

    episodes, sidecar, _, pairs = generator.generate(20260709)
    poisoned = copy.deepcopy(sidecar)
    for episode in episodes:
        hidden = poisoned[episode["id"]]
        if episode["split"] != "calibration" or hidden["cue_variant"] == "absent":
            continue
        pair = hidden["cue_realization_metadata"]["key_pair"]
        hidden["cue_realization_metadata"]["pointer_key"] = (
            pair[0] if hidden["true_type"] == "benign" else pair[1]
        )
    with pytest.raises(AssertionError, match="calibration.*type|pointer"):
        generator.assert_emitted_counterbalance(episodes, poisoned, pairs)


def test_matching_audit_reports_declared_controls_and_no_undeclared_twins():
    episodes, sidecar, _, pairs = generator.generate(20260709)
    result = matching_audit.audit_pairs(
        episodes, sidecar, pairs, assert_ok=True
    )
    assert result["n_pairs"] == 288
    assert result["n_declared_ambiguity_groups"] == 12
    assert result["n_undeclared_opposite_label_groups"] == 0
    assert result["n_declared_normalized_core_groups"] == 12
    assert result["n_undeclared_normalized_core_groups"] == 0
    assert result["private_char_budget_delta_max"] == 0
