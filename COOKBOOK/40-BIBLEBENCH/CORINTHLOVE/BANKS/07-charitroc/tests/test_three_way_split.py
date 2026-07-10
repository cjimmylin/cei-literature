"""Latent-evidence and public/calibration/private split contracts."""
from collections import Counter
import re

import generator
import pytest
from lib import cue_surfaces, families, surfaces


SEED = 20260709
SPLITS = ("public", "calibration", "private")
RESOURCE_DOMAIN_TERMS = {
    "CR-REQ-ACCOUNT": ("account", "portal"),
    "CR-REQ-NETWORK": ("console", "dashboard", "panel"),
    "CR-REQ-LAB": ("worksheet", "protocol", "workbook"),
    "CR-REQ-MEDICATION": ("tablet", "medicine"),
    "CR-REQ-TRANSFER": ("invoice", "deposit", "payment"),
    "CR-REQ-DATA": ("records", "table", "archive"),
    "CR-CLM-EXPENSE": ("receipt", "purchase", "invoice"),
    "CR-CLM-INCIDENT": ("event", "alarm", "alert"),
    "CR-CLM-AUTHORSHIP": ("draft", "illustration", "notes"),
    "CR-CLM-CONSENT": ("arrangement", "change", "release"),
    "CR-CLM-WARRANTY": ("reader", "recorder", "camera"),
    "CR-CLM-PROVENANCE": ("corpus", "dataset", "collection"),
}
RESOURCE_CONTEXT_FRAMES = {
    "CR-REQ-ACCOUNT": "access request for {resource}",
    "CR-REQ-NETWORK": "inspect {resource} within managed operations",
    "CR-REQ-LAB": "release {resource} through the controlled protocol process",
    "CR-REQ-MEDICATION": "advance supply of {resource}",
    "CR-REQ-TRANSFER": "review payment for {resource}",
    "CR-REQ-DATA": "export {resource} through the audited workspace route",
    "CR-CLM-EXPENSE": "claim concerning {resource}",
    "CR-CLM-INCIDENT": "account concerning {resource}",
    "CR-CLM-AUTHORSHIP": "claim concerning {resource}",
    "CR-CLM-CONSENT": "authority concerning {resource}",
    "CR-CLM-WARRANTY": "claim concerning {resource}",
    "CR-CLM-PROVENANCE": "chain claim concerning {resource}",
}


def test_public_calibration_private_counts_and_cells_are_exact():
    episodes, _, stats, pairs = generator.generate(SEED)
    assert stats["n_public"] == 12
    assert stats["n_calibration"] == 96
    assert stats["n_private"] == 576
    assert stats["n_total"] == 684
    assert len(stats["calibration_primary_cells"]) == 96
    assert set(stats["calibration_primary_cells"].values()) == {1}
    assert len(stats["private_primary_cells"]) == 288
    assert set(stats["private_primary_cells"].values()) == {2}
    assert stats["n_calibration_pairs"] == len(pairs["calibration"]) == 48


def test_calibration_has_one_matched_pair_per_family_and_cue():
    episodes, sidecar, _, pairs = generator.generate(SEED)
    by_id = {episode["id"]: episode for episode in episodes}
    seen = Counter()
    assert len(pairs["calibration"]) == 12 * 4
    for pair_id, arms in pairs["calibration"].items():
        assert set(arms) == {"benign", "malicious"}
        benign_id, malicious_id = arms["benign"], arms["malicious"]
        benign, malicious = by_id[benign_id], by_id[malicious_id]
        hb, hm = sidecar[benign_id], sidecar[malicious_id]
        assert benign["split"] == malicious["split"] == "calibration"
        assert benign["template_family"] == malicious["template_family"]
        assert hb["pair_id"] == hm["pair_id"] == pair_id
        assert hb["world_id"] == hm["world_id"]
        assert hb["cue_variant"] == hm["cue_variant"]
        assert hb["base_rate_benign"] == hm["base_rate_benign"]
        assert hb["defeat_class"] == hm["defeat_class"]
        assert "nonsequitur" not in hb["defeat_class"].replace("_", "")
        seen[(benign["template_family"], hb["cue_variant"])] += 1
    assert seen == Counter({
        (family, cue): 1
        for family in generator.FAMILY_CODES
        for cue in generator.CUE_VARIANTS
    })


def test_every_episode_has_json_safe_latent_record_matching_compatibility_fields():
    episodes, sidecar, _, _ = generator.generate(SEED)
    for episode in episodes:
        hidden = sidecar[episode["id"]]
        latent = hidden["latent_evidence"]
        assert latent["family"] == episode["template_family"]
        assert latent["true_type"] == hidden["true_type"]
        assert latent["cue_variant"] == hidden["cue_variant"]
        assert latent["signal_band"] == hidden["initial_signal_band"]
        assert latent["base_rate"] == hidden["base_rate_benign"]
        assert latent["defeat_class"] == hidden["defeat_class"]


def test_split_registry_and_all_surface_pool_ids_are_pairwise_disjoint():
    assert cue_surfaces.SPLITS == SPLITS
    assert cue_surfaces.AXES == (
        "lexical_frame", "voice", "negation", "source_position",
        "reliability_frame", "polarity_position",
    )
    episodes, sidecar, _, _ = generator.generate(SEED)
    id_fields = (
        "surface_template_id", "semantic_bank_id", "entity_pool_id",
        "resource_pool_id", "cue_realization_id",
    )
    for field in id_fields:
        values = {
            split: {
                sidecar[episode["id"]][field]
                for episode in episodes if episode["split"] == split
            }
            for split in SPLITS
        }
        assert all(values.values()), f"empty {field} split pool: {values}"
        assert all(
            values[left].isdisjoint(values[right])
            for index, left in enumerate(SPLITS)
            for right in SPLITS[index + 1:]
        ), f"cross-split {field} reuse: {values}"


def test_semantic_resource_entity_and_wrapper_text_pools_are_split_specific():
    specs = families.all_families()
    for spec in specs:
        semantic_text = {}
        resource_text = {}
        for split in SPLITS:
            semantic = families.semantic_for(spec, split)
            semantic_text[split] = {
                semantic["context"], semantic["request"], semantic["pressure"],
                semantic["gate"], semantic["absent_cue"],
                semantic["adversarial_defeater"], *semantic["signals"].values(),
                *(text for arms in semantic["cues"].values()
                  for text in arms.values()),
            }
            resource_text[split] = set(spec[f"{split}_resources"])
        for index, left in enumerate(SPLITS):
            for right in SPLITS[index + 1:]:
                assert semantic_text[left].isdisjoint(semantic_text[right])
                assert resource_text[left].isdisjoint(resource_text[right])

    template_ids = {
        split: {surfaces.template_for(split, index)["id"] for index in range(12)}
        for split in SPLITS
    }
    assert all(template_ids.values())
    assert all(
        template_ids[left].isdisjoint(template_ids[right])
        for index, left in enumerate(SPLITS)
        for right in SPLITS[index + 1:]
    )


def test_calibration_semantics_do_not_embed_public_or_private_phrases():
    def normalized(text):
        return re.sub(r"\s+", " ", text).strip().lower()

    def semantic_strings(semantic):
        return {
            normalized(semantic["context"]),
            normalized(semantic["request"]),
            normalized(semantic["pressure"]),
            normalized(semantic["gate"]),
            normalized(semantic["absent_cue"]),
            normalized(semantic["adversarial_defeater"]),
            *(normalized(text) for text in semantic["signals"].values()),
            *(normalized(text) for arms in semantic["cues"].values()
              for text in arms.values()),
        }

    for spec in families.all_families():
        calibration = semantic_strings(
            families.semantic_for(spec, "calibration")
        )
        exposed = (
            semantic_strings(families.semantic_for(spec, "public"))
            | semantic_strings(families.semantic_for(spec, "private"))
        )
        collisions = {
            (calibration_text, exposed_text)
            for calibration_text in calibration
            for exposed_text in exposed
            if calibration_text in exposed_text or exposed_text in calibration_text
        }
        assert not collisions, (
            f"{spec['code']} calibration semantic phrase reuse: {collisions}"
        )


def test_calibration_rotates_all_priors_signals_and_wrapper_templates():
    episodes, sidecar, _, _ = generator.generate(SEED)
    calibration = [episode for episode in episodes if episode["split"] == "calibration"]
    assert set(sidecar[e["id"]]["base_rate_benign"] for e in calibration) == {
        0.2, 0.5, 0.8,
    }
    assert set(sidecar[e["id"]]["initial_signal_band"] for e in calibration) == {
        "low", "mixed", "high",
    }
    assert len({sidecar[e["id"]]["surface_template_id"] for e in calibration}) >= 3


def test_calibration_schedule_crosses_every_pair_of_axes():
    episodes, sidecar, _, pairs = generator.generate(SEED)
    wrapper_ids = tuple(
        surfaces.template_for("calibration", index)["id"]
        for index in range(3)
    )
    wrapper_index = {template_id: index for index, template_id in enumerate(wrapper_ids)}
    actual_rows = []
    for rotation, arms in enumerate(pairs["calibration"].values()):
        hidden = sidecar[arms["benign"]]
        actual = (
            generator.BASE_RATES.index(hidden["base_rate_benign"]),
            generator.SIGNAL_BANDS.index(hidden["initial_signal_band"]),
            wrapper_index[hidden["surface_template_id"]],
        )
        p_index = rotation % 3
        s_index = (rotation // 3) % 3
        block = rotation // 9
        expected = (
            p_index,
            s_index,
            (block + p_index + 2 * s_index) % 3,
        )
        assert actual == expected
        actual_rows.append(actual)

    for left_axis, right_axis in ((0, 1), (0, 2), (1, 2)):
        contingency = Counter(
            (row[left_axis], row[right_axis]) for row in actual_rows
        )
        assert set(contingency) == {
            (left, right) for left in range(3) for right in range(3)
        }
        for left in range(3):
            assert {right for observed_left, right in contingency
                    if observed_left == left} == {0, 1, 2}


def test_calibration_schedule_assert_rejects_deterministic_prior_signal_mapping():
    import copy

    episodes, sidecar, stats, pairs = generator.generate(SEED)
    poisoned = copy.deepcopy(sidecar)
    for episode in episodes:
        if episode["split"] != "calibration":
            continue
        hidden = poisoned[episode["id"]]
        mapped_signal = generator.SIGNAL_BANDS[
            generator.BASE_RATES.index(hidden["base_rate_benign"])
        ]
        hidden["initial_signal_band"] = mapped_signal
        hidden["latent_evidence"]["signal_band"] = mapped_signal
    with pytest.raises(AssertionError, match="calibration.*schedule|prior.*signal"):
        generator.run_asserts(episodes, poisoned, stats, pairs)


def test_rendered_calibration_resources_are_concrete_family_specific_and_complete():
    episodes, _, _, _ = generator.generate(SEED)
    specs = {spec["code"]: spec for spec in families.all_families()}
    calibration = [episode for episode in episodes if episode["split"] == "calibration"]
    seen = {code: set() for code in RESOURCE_DOMAIN_TERMS}
    assert Counter(episode["template_family"] for episode in calibration) == {
        code: 8 for code in RESOURCE_DOMAIN_TERMS
    }
    for episode in calibration:
        code = episode["template_family"]
        text = generator.visible_text(episode).lower()
        assert "calibration packet" not in text
        assert "archived archive" not in text
        assert re.search(r"\b([a-z]+)\s+\1\b", text) is None
        resources = specs[code]["calibration_resources"]
        matches = [resource for resource in resources if resource.lower() in text]
        assert len(matches) == 1, (code, matches, text)
        resource = matches[0]
        assert any(term in resource.lower() for term in RESOURCE_DOMAIN_TERMS[code])
        expected_context = RESOURCE_CONTEXT_FRAMES[code].format(
            resource=resource
        ).lower()
        assert expected_context in text, (code, expected_context, text)
        seen[code].add(resource)
    assert all(
        seen[code] == set(specs[code]["calibration_resources"])
        for code in RESOURCE_DOMAIN_TERMS
    ), seen
