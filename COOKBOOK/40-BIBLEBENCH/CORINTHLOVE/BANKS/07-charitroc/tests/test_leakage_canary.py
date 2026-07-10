"""Sidecar boundary, payload blindness, and 10CB-07 canaries."""
import copy
import json
import os
import uuid

import generator
import pytest
from lib import canary, payloads


def test_episode_schema_contains_no_ground_truth_fields():
    episodes, _, _, _ = generator.generate(20260709)
    allowed = {
        "id", "design", "verse_anchors", "template_family", "split",
        "multiturn_script", "canary",
    }
    assert all(set(episode) == allowed for episode in episodes)


def test_sidecar_keys_and_canaries_never_enter_model_visible_text():
    episodes, sidecar, _, _ = generator.generate(20260709)
    banned_field_names = (
        "true_type", "cue_variant", "pair_id", "defeat_class",
        "expected_stage3", "rubric_emphases", "failure_modes",
    )
    for episode in episodes:
        visible = payloads.model_visible_text(episode)
        assert episode["canary"] not in visible
        assert "10CB-07-" not in visible
        for field_name in banned_field_names:
            assert field_name not in visible
        assert sidecar[episode["id"]]["pair_id"] not in visible


def test_canaries_are_unique_wellformed_and_mirrored_in_sidecar():
    episodes, sidecar, _, _ = generator.generate(20260709)
    values = [episode["canary"] for episode in episodes]
    assert len(values) == len(set(values))
    assert all(canary.is_wellformed(value) for value in values)
    assert all(sidecar[episode["id"]]["canary"] == episode["canary"]
               for episode in episodes)


def test_judge_payload_has_only_observable_material():
    episodes, sidecar, _, _ = generator.generate(20260709)
    episode = episodes[0]
    responses = {
        stage: "INTENT: UNCERTAIN\nDECISION: VERIFY"
        for stage in episode["multiturn_script"]
    }
    token = "JUDGE-" + str(
        uuid.UUID("9e8f730d-cbb4-4ce8-93a8-706f331a3772")
    )
    payload = payloads.build_judge_payload(
        episode, responses, judge_case_id=token
    )
    serialized = json.dumps(payload)
    assert set(payload) == {"judge_case_id", "turns", "responses"}
    assert payload["judge_case_id"] == token
    assert episode["id"] not in serialized
    assert sidecar[episode["id"]]["pair_id"] not in serialized
    assert episode["canary"] not in serialized


def test_base_rate_is_intentionally_visible_but_field_name_is_not():
    episodes, sidecar, _, _ = generator.generate(20260709)
    for episode in episodes[:30]:
        stage_1 = episode["multiturn_script"]["stage_1"]
        prior = int(sidecar[episode["id"]]["base_rate_benign"] * 100)
        assert f"{prior}%" in stage_1
        assert "base_rate_benign" not in stage_1


def test_writer_fails_before_artifacts_on_stale_canary_registry_mapping(tmp_path):
    episodes, sidecar, stats, pairs = generator.generate(20260709)
    out = tmp_path / "BANKS" / "07-charitroc"
    out.mkdir(parents=True)
    registry = out.parent / "canary_registry.txt"
    first = episodes[0]
    registry.write_text(
        "# append-only registry\n"
        f"{first['canary']}  CHARITROC-9999  {generator.DESIGN}\n",
        encoding="utf-8",
    )

    with pytest.raises(AssertionError, match="stale canary registry mapping"):
        generator.write_bank(
            episodes, sidecar, stats, pairs, 20260709, os.fspath(out)
        )
    assert not (out / "episodes" / "private_bank.yaml").exists()
    assert not (out / "sidecar" / "judge_token_map.json").exists()


@pytest.mark.parametrize("poison", ["sidecar", "pairs", "stats"])
def test_writer_validates_all_inputs_before_any_filesystem_mutation(
        tmp_path, poison):
    episodes, sidecar, stats, pairs = generator.generate(20260709)
    sidecar = copy.deepcopy(sidecar)
    stats = copy.deepcopy(stats)
    pairs = copy.deepcopy(pairs)
    if poison == "sidecar":
        del sidecar[episodes[0]["id"]]
    elif poison == "pairs":
        pairs["private"].pop(next(iter(pairs["private"])))
    else:
        stats["n_total"] -= 1

    bank_parent = tmp_path / "BANKS"
    bank_parent.mkdir()
    out = bank_parent / "07-charitroc"
    registry = bank_parent / "canary_registry.txt"
    before = b"# existing append-only registry sentinel\n"
    registry.write_bytes(before)

    with pytest.raises((AssertionError, KeyError)):
        generator.write_bank(
            episodes, sidecar, stats, pairs, 20260709, os.fspath(out)
        )
    assert registry.read_bytes() == before
    assert not out.exists()
