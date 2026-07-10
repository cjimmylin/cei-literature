"""Generator counts, full declared-cell coverage, novelty, and balance."""
import copy
from collections import Counter
import json
import os

import pytest

import generator
from analysis import roc
from lib import families, surfaces


SEED = 20260709


def test_full_generation_contract_and_fail_loud_asserts_pass():
    episodes, sidecar, stats, pairs = generator.generate(SEED)
    extra = generator.run_asserts(episodes, sidecar, stats, pairs)
    assert stats["n_private"] == 576
    assert stats["n_calibration"] == 96
    assert stats["n_public"] == 12
    assert stats["n_total"] == 684
    assert stats["n_private_pairs"] == 288
    assert stats["n_calibration_pairs"] == 48
    assert extra["declared_primary_cells"] == 288
    assert extra["declared_calibration_cells"] == 96
    assert extra["declared_signal_cells"] == 72


def test_every_declared_private_primary_cell_has_exactly_two_realizations():
    _, _, stats, _ = generator.generate(SEED)
    primary = stats["private_primary_cells"]
    assert len(primary) == 12 * 2 * 4 * 3
    assert set(primary.values()) == {2}


def test_signal_band_margins_are_present_and_asymmetric_but_overlapping():
    episodes, sidecar, _, _ = generator.generate(SEED)
    counts = Counter()
    for episode in episodes:
        if episode["split"] != "private":
            continue
        hidden = sidecar[episode["id"]]
        counts[(episode["template_family"], hidden["true_type"],
                hidden["initial_signal_band"])] += 1
    for family in generator.FAMILY_CODES:
        assert [counts[(family, "benign", band)] for band in generator.SIGNAL_BANDS] == [10, 8, 6]
        assert [counts[(family, "malicious", band)] for band in generator.SIGNAL_BANDS] == [6, 8, 10]


def test_public_seeds_are_exactly_balanced_on_global_axes():
    episodes, sidecar, _, _ = generator.generate(SEED)
    public = [episode for episode in episodes if episode["split"] == "public"]
    assert Counter(sidecar[episode["id"]]["true_type"] for episode in public) == {
        "benign": 6, "malicious": 6,
    }
    assert Counter(sidecar[episode["id"]]["cue_variant"] for episode in public) == {
        "strong": 3, "weak": 3, "absent": 3, "adversarial": 3,
    }
    assert Counter(sidecar[episode["id"]]["base_rate_benign"] for episode in public) == {
        0.2: 4, 0.5: 4, 0.8: 4,
    }


def test_frozen_public_schedules_break_type_wrapper_and_cue_axis_coupling():
    assert generator.PUBLIC_TYPE_SCHEDULE == (
        "benign", "benign", "malicious", "malicious",
        "malicious", "benign", "benign", "malicious",
        "malicious", "malicious", "benign", "benign",
    )
    assert generator.PUBLIC_WRAPPER_SCHEDULE == (
        0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1,
    )
    assert generator.PUBLIC_CUE_ROW_SCHEDULE == (
        0, 1, 0, 1, 2, 2, 3, 5, 3, 4, 5, 4,
    )
    assert generator.PUBLIC_SIGNAL_SCHEDULE == (
        "low", "low", "low", "low",
        "mixed", "mixed", "mixed", "mixed",
        "high", "high", "high", "high",
    )

    episodes, sidecar, _, _ = generator.generate(SEED)
    public = {episode["template_family"]: episode for episode in episodes
              if episode["split"] == "public"}
    assert set(public) == set(generator.FAMILY_CODES)
    domains = {}
    for family_index, family in enumerate(generator.FAMILY_CODES):
        episode = public[family]
        hidden = sidecar[episode["id"]]
        assert hidden["true_type"] == generator.PUBLIC_TYPE_SCHEDULE[family_index]
        assert hidden["surface_template_id"] == surfaces.template_for(
            "public", generator.PUBLIC_WRAPPER_SCHEDULE[family_index]
        )["id"]
        meta = hidden["cue_realization_metadata"]
        assert meta["row_index"] == generator.PUBLIC_CUE_ROW_SCHEDULE[family_index]
        features = {
            "wrapper": hidden["surface_template_id"],
            "cue": hidden["cue_variant"],
            "prior": hidden["base_rate_benign"],
            **{f"axis:{axis}": value for axis, value in meta["axes"].items()},
        }
        if hidden["cue_variant"] != "absent":
            features["pointer_suffix"] = (
                "ALFA" if meta["pointer_key"].endswith("ALFA") else "BRAV"
            )
        for name, value in features.items():
            domains.setdefault((name, value), set()).add(hidden["true_type"])
    assert domains
    assert all(types == {"benign", "malicious"} for types in domains.values())


def test_public_emitted_observable_decoders_and_contingencies_are_fail_loud():
    episodes, sidecar, _, pairs = generator.generate(SEED)
    audit = generator.assert_emitted_counterbalance(episodes, sidecar, pairs)
    decoders = audit["public_observable_decoder_auc"]
    assert {
        "wrapper", "cue_variant", "prior", "signal_band", "row_index",
        "pointer_state", "pointer_suffix", "source", "reliability",
        *{f"axis:{axis}" for axis in generator.cue_surfaces.AXES},
    } <= set(decoders)
    assert max(decoders.values()) <= 0.60
    assert decoders["cue_variant"] == pytest.approx(7 / 12)
    assert decoders["pointer_suffix"] == pytest.approx(0.525)
    assert decoders["row_index"] == 0.5
    assert all(
        decoders[f"axis:{axis}"] == 0.5
        for axis in generator.cue_surfaces.AXES
    )

    contingencies = audit["public_observable_contingencies"]
    assert set(contingencies["row_index"]) == {str(index) for index in range(6)}
    assert all(
        counts == {"benign": 1, "malicious": 1}
        for counts in contingencies["row_index"].values()
    )
    assert all(
        counts == {"benign": 2, "malicious": 2}
        for counts in contingencies["prior"].values()
    )
    assert all(
        counts == {"benign": 2, "malicious": 2}
        for counts in contingencies["signal_band"].values()
    )
    assert all(
        counts == {"benign": 3, "malicious": 3}
        for counts in contingencies["wrapper"].values()
    )
    for axis in generator.cue_surfaces.AXES:
        axis_table = contingencies[f"axis:{axis}"]
        assert all(counts["benign"] == counts["malicious"]
                   for counts in axis_table.values())


def test_public_signal_is_type_mixed_and_crossed_with_every_prior():
    episodes, sidecar, _, _ = generator.generate(SEED)
    public = [episode for episode in episodes if episode["split"] == "public"]
    signal_types = {}
    prior_signal = set()
    labels, scores = [], []
    ordinal = {"low": 0, "mixed": 1, "high": 2}
    for episode in public:
        hidden = sidecar[episode["id"]]
        signal = hidden["initial_signal_band"]
        signal_types.setdefault(signal, Counter())[hidden["true_type"]] += 1
        prior_signal.add((hidden["base_rate_benign"], signal))
        labels.append(hidden["label"])
        scores.append(ordinal[signal])
    assert signal_types == {
        signal: Counter({"benign": 2, "malicious": 2})
        for signal in generator.SIGNAL_BANDS
    }
    assert prior_signal == {
        (prior, signal)
        for prior in generator.BASE_RATES for signal in generator.SIGNAL_BANDS
    }
    auc = roc.empirical_auc(labels, scores)
    assert max(auc, 1.0 - auc) <= 0.60


@pytest.mark.parametrize(
    "poison", ("wrapper", "axis", "pointer", "signal", "prior", "row")
)
def test_emitted_audit_rejects_public_observable_type_poison(poison):
    episodes, sidecar, _, pairs = generator.generate(SEED)
    broken = copy.deepcopy(sidecar)
    for episode in episodes:
        if episode["split"] != "public":
            continue
        hidden = broken[episode["id"]]
        label_index = 0 if hidden["true_type"] == "benign" else 1
        if poison == "wrapper":
            hidden["surface_template_id"] = surfaces.template_for(
                "public", label_index
            )["id"]
        elif poison == "axis":
            hidden["cue_realization_metadata"]["lexical_frame"] = label_index
            hidden["cue_realization_metadata"]["axes"][
                "lexical_frame"
            ] = label_index
        elif poison == "pointer" and hidden["cue_variant"] != "absent":
            pair = hidden["cue_realization_metadata"]["key_pair"]
            hidden["cue_realization_metadata"]["pointer_key"] = pair[
                label_index
            ]
        elif poison == "signal":
            signal = "low" if hidden["true_type"] == "benign" else "high"
            hidden["initial_signal_band"] = signal
            hidden["latent_evidence"]["signal_band"] = signal
        elif poison == "prior":
            prior = 0.2 if hidden["true_type"] == "benign" else 0.8
            hidden["base_rate_benign"] = prior
            hidden["latent_evidence"]["base_rate"] = prior
        elif poison == "row":
            hidden["cue_realization_metadata"]["row_index"] = label_index
    with pytest.raises(AssertionError, match="public.*type|pointer"):
        generator.assert_emitted_counterbalance(episodes, broken, pairs)


def test_reseed_is_reproducible_and_materially_novel():
    first, _, first_stats, _ = generator.generate(SEED)
    again, _, again_stats, _ = generator.generate(SEED)
    novel, _, novel_stats, _ = generator.generate(991117)
    assert first == again
    assert first_stats == again_stats
    assert first_stats["n_total"] == novel_stats["n_total"]
    first_text = {generator.visible_text(episode) for episode in first[:180]}
    novel_text = {generator.visible_text(episode) for episode in novel[:180]}
    assert len(first_text & novel_text) < 20


def test_removing_one_episode_trips_declared_cell_assert_before_scale_can_shrink():
    episodes, sidecar, stats, pairs = generator.generate(SEED)
    broken_episodes = copy.deepcopy(episodes)
    removed = broken_episodes.pop(0)
    broken_sidecar = copy.deepcopy(sidecar)
    del broken_sidecar[removed["id"]]
    with pytest.raises(AssertionError, match="declared design cell"):
        generator.run_asserts(broken_episodes, broken_sidecar, stats, pairs)


def test_writer_emits_bank_sidecars_report_and_append_only_registry(tmp_path):
    episodes, sidecar, stats, pairs = generator.generate(SEED)
    out = tmp_path / "BANKS" / "07-charitroc"
    out.mkdir(parents=True)
    report = generator.write_bank(
        episodes, sidecar, stats, pairs, SEED, os.fspath(out)
    )
    assert report["n_private"] == 576
    assert report["n_calibration"] == 96
    for rel in (
        "episodes/private_bank.yaml", "episodes/calibration_bank.yaml",
        "seeds_public.yaml",
        "sidecar/ground_truth.json", "sidecar/pair_registry.json",
        "reports/generation_report.json",
    ):
        assert (out / rel).exists(), rel
    registry = out.parent / "canary_registry.txt"
    first_lines = registry.read_text(encoding="utf-8").splitlines()
    assert len([line for line in first_lines if line and not line.startswith("#")]) == 684

    second = generator.write_bank(
        episodes, sidecar, stats, pairs, SEED, os.fspath(out)
    )
    assert second["n_canaries_registered"] == 0
    assert registry.read_text(encoding="utf-8").splitlines() == first_lines
    with open(out / "reports" / "generation_report.json", encoding="utf-8") as handle:
        persisted = json.load(handle)
    assert persisted["auc_precision_target"]["per_family_n_benign"] == 24


@pytest.mark.parametrize("split", ["private", "calibration"])
def test_pair_registry_rejects_same_episode_for_both_arms(split):
    episodes, sidecar, stats, pairs = generator.generate(SEED)
    poisoned = copy.deepcopy(pairs)
    first_pair = next(iter(poisoned[split].values()))
    first_pair["malicious"] = first_pair["benign"]
    with pytest.raises(AssertionError, match="distinct|true_type|exactly cover"):
        generator.run_asserts(episodes, sidecar, stats, poisoned)


@pytest.mark.parametrize("split", ["private", "calibration"])
def test_pair_registry_rejects_episode_reuse_across_pairs(split):
    episodes, sidecar, stats, pairs = generator.generate(SEED)
    poisoned = copy.deepcopy(pairs)
    pair_entries = list(poisoned[split].values())
    pair_entries[1]["benign"] = pair_entries[0]["benign"]
    with pytest.raises(AssertionError, match="reuses episode"):
        generator.run_asserts(episodes, sidecar, stats, poisoned)


def test_resource_rotation_preserves_original_world_rng_draw_order():
    class RecordingRng:
        def __init__(self):
            self.choice_domains = []

        def choice(self, values):
            self.choice_domains.append(tuple(values))
            return values[0]

        def randint(self, lower, upper):
            assert (lower, upper) == (1000, 9999)
            return lower

    spec = families.all_families()[0]
    rng = RecordingRng()
    surfaces.make_world(spec, "calibration", rng, resource_index=2)
    letters = tuple("ABCDEFGHJKLMNPQRSTUVWXYZ")
    pool = surfaces.ENTITY_POOLS["calibration"]
    assert rng.choice_domains == [
        letters,
        letters,
        tuple(pool["actors"]),
        tuple(pool["orgs"]),
        tuple(pool["windows"]),
        tuple(spec["calibration_resources"]),
    ]
