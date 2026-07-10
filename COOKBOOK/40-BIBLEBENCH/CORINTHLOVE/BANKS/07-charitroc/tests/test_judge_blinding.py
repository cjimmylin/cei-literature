"""Judge payload blinding and identifier-channel regression tests."""

import copy
import json
import os
import uuid

import generator
import pytest
from lib import payloads


SEED = 20260709
PROVENANCE = "harness validation, NOT a measurement"
FIXED_RESPONSES = {
    stage: "INTENT: UNCERTAIN\nDECISION: VERIFY"
    for stage in payloads.STAGES
}


def _odd_even_type_decoder(item_id: str) -> str:
    """Legacy decoder that must not perfectly recover the hidden type."""
    ordinal = int(item_id.rsplit("-", 1)[1])
    return "benign" if ordinal % 2 else "malicious"


def test_judge_payload_accepts_only_opaque_case_id():
    episodes, _, _, _ = generator.generate(SEED)
    episode = episodes[0]
    reordered_responses = {
        stage: FIXED_RESPONSES[stage] for stage in reversed(payloads.STAGES)
    }
    token = "JUDGE-" + str(
        uuid.UUID("9e8f730d-cbb4-4ce8-93a8-706f331a3772")
    )
    out = payloads.build_judge_payload(
        episode, reordered_responses, judge_case_id=token
    )
    assert set(out) == {"judge_case_id", "turns", "responses"}
    assert out["judge_case_id"] == token
    assert [row["stage"] for row in out["responses"]] == list(payloads.STAGES)
    assert episode["id"] not in json.dumps(out, sort_keys=True)


def test_model_turns_accepts_reordered_mapping_but_emits_canonical_order():
    episodes, _, _, _ = generator.generate(SEED)
    episode = copy.deepcopy(episodes[0])
    script = episode["multiturn_script"]
    episode["multiturn_script"] = {
        stage: script[stage] for stage in reversed(payloads.STAGES)
    }
    turns = payloads.model_turns(episode)
    assert [turn["stage"] for turn in turns] == list(payloads.STAGES)


@pytest.mark.parametrize(
    ("episode", "error_type", "message"),
    [
        (None, TypeError, "episode must be a mapping"),
        ([], TypeError, "episode must be a mapping"),
        ({}, ValueError, "multiturn_script"),
        ({"multiturn_script": []}, TypeError, "script must be a mapping"),
        (
            {"multiturn_script": {"stage_1": "only one"}},
            ValueError,
            "exactly stage_1, stage_2, stage_3, stage_4",
        ),
        (
            {"multiturn_script": {
                "stage_1": "one", "stage_2": "two", "stage_3": {},
                "stage_4": "four",
            }},
            TypeError,
            "stage_3 content must be a string",
        ),
    ],
)
def test_model_turns_rejects_wrong_or_structured_episode_material(
        episode, error_type, message):
    with pytest.raises(error_type, match=message):
        payloads.model_turns(episode)


@pytest.mark.parametrize("bad_token", [
    "JUDGE-9e8f730d-cbb4-1ce8-93a8-706f331a3772",  # UUIDv1 bits
    "JUDGE-9e8f730d-cbb4-4ce8-73a8-706f331a3772",  # non-RFC variant
    "JUDGE-9E8F730D-CBB4-4CE8-93A8-706F331A3772",  # uppercase
    "9e8f730d-cbb4-4ce8-93a8-706f331a3772",
    "JUDGE-not-a-uuid",
    None,
])
def test_judge_payload_rejects_noncanonical_or_non_v4_tokens(bad_token):
    episodes, _, _, _ = generator.generate(SEED)
    with pytest.raises(ValueError, match="lowercase JUDGE-<UUIDv4>"):
        payloads.build_judge_payload(
            episodes[0], FIXED_RESPONSES, judge_case_id=bad_token
        )


def test_judge_payload_requires_exactly_all_four_response_stages():
    episodes, _, _, _ = generator.generate(SEED)
    token = "JUDGE-9e8f730d-cbb4-4ce8-93a8-706f331a3772"
    missing = dict(FIXED_RESPONSES)
    del missing["stage_4"]
    extra = {**FIXED_RESPONSES, "stage_5": "not permitted"}
    for invalid in (missing, extra):
        with pytest.raises(ValueError, match="exactly all four response stages"):
            payloads.build_judge_payload(
                episodes[0], invalid, judge_case_id=token
            )


def test_judge_payload_rejects_wrong_or_structured_response_material():
    episodes, _, _, _ = generator.generate(SEED)
    token = "JUDGE-9e8f730d-cbb4-4ce8-93a8-706f331a3772"
    with pytest.raises(TypeError, match="responses must be a mapping"):
        payloads.build_judge_payload(
            episodes[0], list(FIXED_RESPONSES), judge_case_id=token
        )
    structured = dict(FIXED_RESPONSES)
    structured["stage_2"] = {
        "true_type": "benign",
        "pair_id": "must-never-serialize",
    }
    with pytest.raises(TypeError, match="stage_2 response must be a string"):
        payloads.build_judge_payload(
            episodes[0], structured, judge_case_id=token
        )


def test_judge_token_map_is_unique_valid_deterministic_and_exact():
    episodes, sidecar, _, _ = generator.generate(SEED)
    token_map = generator.build_judge_token_map(episodes, SEED)
    generator.validate_judge_token_map(episodes, token_map)

    assert token_map == generator.build_judge_token_map(
        list(reversed(episodes)), SEED
    )
    assert len(token_map) == len(episodes) == len(set(token_map))
    assert len(set(token_map.values())) == len(episodes)
    assert set(token_map.values()) == set(sidecar)
    for token in token_map:
        assert token.startswith("JUDGE-")
        parsed = uuid.UUID(token.removeprefix("JUDGE-"))
        assert parsed.version == 4
        assert parsed.variant == uuid.RFC_4122
        assert token == "JUDGE-" + str(parsed)

    # The trusted map is the only in-memory structure that carries judge IDs.
    assert "JUDGE-" not in json.dumps(episodes, sort_keys=True)
    assert "JUDGE-" not in json.dumps(sidecar, sort_keys=True)


def test_token_map_validation_fails_on_wrong_or_duplicate_item_mapping():
    episodes, _, _, _ = generator.generate(SEED)
    token_map = generator.build_judge_token_map(episodes, SEED)
    tokens = list(token_map)

    wrong = dict(token_map)
    wrong[tokens[0]] = "CHARITROC-9999"
    with pytest.raises(AssertionError, match="exactly cover"):
        generator.validate_judge_token_map(episodes, wrong)

    duplicate = dict(token_map)
    duplicate[tokens[0]] = duplicate[tokens[1]]
    with pytest.raises(AssertionError, match="not one-to-one"):
        generator.validate_judge_token_map(episodes, duplicate)


def test_judge_map_writer_persists_only_the_exact_two_column_mapping(tmp_path):
    episodes, _, _, _ = generator.generate(SEED)
    written = generator.write_judge_token_map(
        episodes, SEED, os.fspath(tmp_path)
    )
    path = tmp_path / "sidecar" / "judge_token_map.json"
    with path.open(encoding="utf-8") as handle:
        persisted = json.load(handle)
    assert persisted == written == generator.build_judge_token_map(episodes, SEED)
    assert set(tmp_path.rglob("*")) == {tmp_path / "sidecar", path}


def test_numeric_identifier_features_mix_every_hidden_axis():
    episodes, sidecar, _, _ = generator.generate(SEED)
    summary = generator.assert_identifier_buckets_mixed(episodes, sidecar)
    assert set(summary) == {"parity", "last_digit", "coarse_bucket"}
    expected_axes = {
        "true_type", "cue_variant", "base_rate_benign",
        "template_family", "private_pair_arm",
    }
    expected_feature_domains = {
        "parity": {"0", "1"},
        "last_digit": {str(value) for value in range(10)},
        "coarse_bucket": {str(value) for value in range(10)},
    }
    expected_axis_domains = {
        "true_type": set(generator.TRUE_TYPES),
        "cue_variant": set(generator.CUE_VARIANTS),
        "base_rate_benign": {str(value) for value in generator.BASE_RATES},
        "template_family": set(generator.FAMILY_CODES),
        "private_pair_arm": set(generator.TRUE_TYPES),
    }
    for feature_name, feature in summary.items():
        assert set(feature) == expected_axes
        for axis_name, evidence in feature.items():
            expected_count = (
                generator.N_PRIVATE
                if axis_name == "private_pair_arm"
                else len(episodes)
            )
            assert evidence["observation_count"] == expected_count
            assert set(evidence["feature_domain"]) == expected_feature_domains[
                feature_name
            ]
            assert set(evidence["axis_domain"]) == expected_axis_domains[axis_name]
            assert all(
                len(values) > 1
                for values in evidence["values_per_bucket"].values()
            )
            assert all(
                len(buckets) > 1
                for buckets in evidence["buckets_per_value"].values()
            )


def test_identifier_gate_rejects_empty_private_arm_observations():
    episodes, sidecar, _, _ = generator.generate(SEED)
    no_private = copy.deepcopy(episodes)
    for episode in no_private:
        episode["split"] = "public"
    with pytest.raises(AssertionError, match="private episode count"):
        generator.assert_identifier_buckets_mixed(no_private, sidecar)


def test_identifier_gate_rejects_deterministic_parity_encoding():
    episodes, sidecar, _, _ = generator.generate(SEED)
    poisoned = copy.deepcopy(sidecar)
    for episode in episodes:
        ordinal = int(episode["id"].rsplit("-", 1)[1])
        poisoned[episode["id"]]["true_type"] = (
            "benign" if ordinal % 2 else "malicious"
        )
    with pytest.raises(
        AssertionError, match="parity deterministically exposes true_type"
    ):
        generator.assert_identifier_buckets_mixed(episodes, poisoned)


def test_identifier_gate_rejects_missing_declared_axis_value():
    episodes, sidecar, _, _ = generator.generate(SEED)
    poisoned = copy.deepcopy(sidecar)
    for hidden in poisoned.values():
        hidden["cue_variant"] = "strong"
    with pytest.raises(AssertionError, match="cue_variant domain"):
        generator.assert_identifier_buckets_mixed(episodes, poisoned)


def test_randomized_ids_preserve_exact_private_pair_resolution():
    episodes, sidecar, _, pairs = generator.generate(SEED)
    by_id = {episode["id"]: episode for episode in episodes}
    seen_arms = set()
    for pair_id, arms in pairs["private"].items():
        assert set(arms) == {"benign", "malicious"}
        assert arms["benign"] != arms["malicious"]
        assert set(arms.values()) <= set(by_id) == set(sidecar)
        for expected_type, item_id in arms.items():
            assert sidecar[item_id]["true_type"] == expected_type
            assert sidecar[item_id]["pair_id"] == pair_id
            seen_arms.add(item_id)
    assert len(seen_arms) == generator.N_PRIVATE


def test_every_judge_payload_blinds_raw_item_id_and_its_decodable_text():
    episodes, sidecar, _, _ = generator.generate(SEED)
    token_map = generator.build_judge_token_map(episodes, SEED)
    item_to_token = {item_id: token for token, item_id in token_map.items()}
    payload_records = [
        (
            episode,
            payloads.build_judge_payload(
                episode,
                FIXED_RESPONSES,
                judge_case_id=item_to_token[episode["id"]],
            ),
        )
        for episode in episodes
    ]
    assert len(payload_records) == generator.N_TOTAL == 684

    decoder_correct = sum(
        _odd_even_type_decoder(episode["id"])
        == sidecar[episode["id"]]["true_type"]
        for episode, _ in payload_records
    )
    assert decoder_correct < len(payload_records)

    serialized = [
        (episode, json.dumps(payload, sort_keys=True))
        for episode, payload in payload_records
    ]
    raw_id_field_offenders = [
        episode["id"]
        for episode, payload in payload_records
        if any("item_id" in key or "episode" in key for key in payload)
    ]
    raw_id_value_offenders = [
        episode["id"]
        for episode, text in serialized
        if episode["id"] in text
    ]

    assert not raw_id_field_offenders and not raw_id_value_offenders, (
        f"{PROVENANCE}: judge payload exposes raw item_id; "
        f"field_name_offenders={len(raw_id_field_offenders)}/{generator.N_TOTAL}, "
        f"raw_id_value_offenders={len(raw_id_value_offenders)}/{generator.N_TOTAL}, "
        f"odd_even_decoder={decoder_correct}/{generator.N_TOTAL}; "
        f"first_field_offender="
        f"{raw_id_field_offenders[0] if raw_id_field_offenders else None}, "
        f"first_raw_value_offender="
        f"{raw_id_value_offenders[0] if raw_id_value_offenders else None}"
    )
