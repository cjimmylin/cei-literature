"""Frozen panel, sampling, plan-state, and private-launch contracts."""
from collections import Counter, defaultdict
import copy
import json
import os
from pathlib import Path
import shutil

import pytest
import yaml

import generator
from pilot import manifest


BANK = Path(__file__).resolve().parents[1]
SEED = 20260709
MODELS = ("gpt-5.5", "gpt-5.4", "gpt-5.4-mini")
STAGES = ("smoke", "calibration", "reliability", "private")
HIDDEN_ENTRY_KEYS = {
    "true_type", "label", "cue_variant", "base_rate_benign", "pair_id",
    "family", "template_family", "split", "sidecar", "scoring_key",
    "expected_stage3", "defeat_class", "canary",
}
CODEX_ISOLATION_PROFILE = {
    "ignore_user_config": True,
    "ignore_rules": True,
    "skip_git_repo_check": True,
    "sandbox": "read-only",
    "working_directory": "new-empty-opaque-per-episode",
    "tools_enabled": False,
}
OPENROUTER_ROUTING_POLICY = {
    "require_parameters": True,
    "allow_fallbacks": False,
    "tools_enabled": False,
    "plugins_enabled": False,
    "web_search_enabled": False,
    "message_healing_enabled": False,
    "context_compression_enabled": False,
    "data_collection": "deny",
    "zero_data_retention_required": True,
    "provider_pin": {
        "organization": "OpenAI",
        "required": True,
        "verify_at_launch": True,
    },
    "reasoning_effort": "medium",
}


@pytest.fixture(scope="module")
def bank_data():
    episodes, sidecar, _, _ = generator.generate(SEED)
    return episodes, sidecar


@pytest.fixture(scope="module")
def samples(bank_data):
    episodes, sidecar = bank_data
    return {
        stage: manifest.build_sample(stage, episodes, sidecar, SEED)
        for stage in STAGES
    }


def entries(sample, extension=False):
    return sample["extension_entries" if extension else "entries"]


def rehash_plan(plan):
    plan["plan_hash"] = manifest.canonical_sha256({
        key: value for key, value in plan.items() if key != "plan_hash"
    })
    return plan


def run_event(plan, *, event_id, state="started", attempt=1,
              timestamp="2026-07-10T12:00:00Z", session_attempt=1,
              occurrence_index=0, model=None):
    occurrence = plan["entries"][occurrence_index]
    if model is None:
        model = occurrence["model_execution_order"][0]
    return {
        "event_id": event_id,
        "plan_hash": plan["plan_hash"],
        "plan_occurrence_id": occurrence["occurrence_id"],
        "item_id": occurrence["item_id"],
        "logical_model_id": model,
        "session_attempt": session_attempt,
        "state": state,
        "attempt": attempt,
        "timestamp_utc": timestamp,
    }


def coordinated_unsampled_poison(episodes, sidecar, sampled_ids):
    poisoned_episodes = copy.deepcopy(episodes)
    poisoned_sidecar = copy.deepcopy(sidecar)
    pair_members = defaultdict(set)
    for item_id, hidden in sidecar.items():
        if hidden["pair_id"].startswith("CRPAIR-"):
            pair_members[hidden["pair_id"]].add(item_id)
    target_pair, target_ids = next(
        (pair_id, item_ids)
        for pair_id, item_ids in pair_members.items()
        if item_ids.isdisjoint(sampled_ids)
    )
    by_id = {row["id"]: row for row in poisoned_episodes}
    for item_id in target_ids:
        hidden = poisoned_sidecar[item_id]
        hidden["defeat_class"] = "non_sequitur_invalid"
        hidden["latent_evidence"]["defeat_class"] = "non_sequitur_invalid"
        hidden["latent_evidence"]["signal_band"] = "POISON"
        hidden["expected_stage3"]["posterior_direction"] = 999
        hidden["scoring_key"]["auc_label"] = 1 - hidden["scoring_key"][
            "auc_label"
        ]
        by_id[item_id]["multiturn_script"]["stage_1"] += (
            f" Hidden truth leak: true_type={hidden['true_type']}."
        )
        by_id[item_id]["multiturn_script"]["stage_2"] += (
            " Arbitrary coordinated visible transcript poison."
        )
    assert len(target_ids) == 2 and target_pair
    return poisoned_episodes, poisoned_sidecar


def pair_chunks(sample, sidecar, extension=False):
    rows = entries(sample, extension=extension)
    assert len(rows) % 2 == 0
    grouped = {}
    for row in rows:
        pair_id = sidecar[row["item_id"]]["pair_id"]
        grouped.setdefault(pair_id, []).append(row)
    chunks = list(grouped.values())
    for chunk in chunks:
        assert len(chunk) == 2
        assert len({sidecar[row["item_id"]]["pair_id"] for row in chunk}) == 1
        assert {sidecar[row["item_id"]]["true_type"] for row in chunk} == {
            "benign", "malicious",
        }
    return chunks


def test_panel_is_exact_ordered_medium_and_explicitly_excludes_sol():
    panel = manifest.load_panel()

    assert panel["sol_excluded"] is True
    assert [row["logical_model_id"] for row in panel["models"]] == list(MODELS)
    assert {row["reasoning_effort"] for row in panel["models"]} == {"medium"}
    assert panel["fallback_policy"] == {
        "allow_fallback": False,
        "allow_substitution": False,
        "on_unavailable": "stop_model_arm",
    }
    assert all("sol" not in row["logical_model_id"].lower()
               for row in panel["models"])


def test_panel_separates_logical_codex_and_openrouter_identities():
    panel = manifest.load_panel()

    for row in panel["models"]:
        logical = row["logical_model_id"]
        codex = row["providers"]["codex"]
        openrouter = row["providers"]["openrouter"]
        assert codex["provider_model_id"] == logical
        assert codex["configuration_id"].startswith("codex-cli-")
        assert openrouter["provider_model_id"].startswith("openai/")
        assert openrouter["provider_model_id"].split("/", 1)[1] == logical
        assert openrouter["configuration_id"].startswith("openrouter-")
        assert openrouter["verify_at_launch"] is True
        assert codex["configuration_id"] != openrouter["configuration_id"]


def test_panel_freezes_substantive_codex_and_openrouter_policies():
    panel = manifest.load_panel()

    for row in panel["models"]:
        assert row["providers"]["codex"]["isolation_profile"] == (
            CODEX_ISOLATION_PROFILE
        )
        assert row["providers"]["openrouter"]["routing_policy"] == (
            OPENROUTER_ROUTING_POLICY
        )


@pytest.mark.parametrize(
    ("provider", "path", "bad_value"),
    [
        ("codex", ("isolation_profile", "ignore_user_config"), False),
        ("codex", ("isolation_profile", "ignore_rules"), False),
        ("codex", ("isolation_profile", "skip_git_repo_check"), False),
        ("codex", ("isolation_profile", "sandbox"), "workspace-write"),
        ("codex", ("isolation_profile", "working_directory"), "repository"),
        ("codex", ("isolation_profile", "tools_enabled"), True),
        ("openrouter", ("routing_policy", "require_parameters"), False),
        ("openrouter", ("routing_policy", "allow_fallbacks"), True),
        ("openrouter", ("routing_policy", "tools_enabled"), True),
        ("openrouter", ("routing_policy", "plugins_enabled"), True),
        ("openrouter", ("routing_policy", "web_search_enabled"), True),
        ("openrouter", ("routing_policy", "message_healing_enabled"), True),
        ("openrouter", ("routing_policy", "context_compression_enabled"), True),
        ("openrouter", ("routing_policy", "data_collection"), "allow"),
        ("openrouter", ("routing_policy", "zero_data_retention_required"), False),
        (
            "openrouter",
            ("routing_policy", "provider_pin", "required"),
            False,
        ),
        (
            "openrouter",
            ("routing_policy", "provider_pin", "verify_at_launch"),
            False,
        ),
        ("openrouter", ("routing_policy", "reasoning_effort"), "low"),
    ],
)
def test_panel_policy_poison_fails_loudly(
        tmp_path, provider, path, bad_value):
    panel = copy.deepcopy(manifest.load_panel())
    cursor = panel["models"][0]["providers"][provider]
    for component in path[:-1]:
        cursor = cursor.setdefault(component, {})
    cursor[path[-1]] = bad_value
    poisoned = tmp_path / "panel.json"
    poisoned.write_text(json.dumps(panel), encoding="utf-8")

    with pytest.raises(ValueError, match="policy|profile"):
        manifest.load_panel(poisoned)


def test_response_schema_is_strict_and_canonical():
    schema = manifest.load_response_schema()

    assert schema["type"] == "object"
    assert schema["additionalProperties"] is False
    assert schema["required"] == ["reason", "INTENT", "DECISION"]
    assert set(schema["properties"]) == {"reason", "INTENT", "DECISION"}
    assert schema["properties"]["reason"]["type"] == "string"
    assert schema["properties"]["INTENT"]["enum"] == [
        "BENIGN", "UNCERTAIN", "MALICIOUS",
    ]
    assert schema["properties"]["DECISION"]["enum"] == [
        "REFUSE", "RESTRICT", "VERIFY", "CONDITIONAL", "GRANT",
    ]


@pytest.mark.parametrize(
    ("poison", "message"),
    [
        ("version", "manifest version"),
        ("extra_top", "exact keys"),
        ("extra_model", "model keys"),
        ("extra_provider", "provider keys"),
        ("wrong_openrouter_slug", "OpenRouter provider ID"),
    ],
)
def test_panel_rejects_semantic_manifest_poison(tmp_path, poison, message):
    panel = copy.deepcopy(manifest.load_panel())
    if poison == "version":
        panel["manifest_version"] = "unfrozen-version"
    elif poison == "extra_top":
        panel["notes"] = "unfrozen"
    elif poison == "extra_model":
        panel["models"][0]["alias"] = "unfrozen"
    elif poison == "extra_provider":
        panel["models"][0]["providers"]["codex"]["temperature"] = 0
    else:
        panel["models"][0]["providers"]["openrouter"][
            "provider_model_id"
        ] = "another-org/gpt-5.5"
    path = tmp_path / "panel.json"
    path.write_text(json.dumps(panel), encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        manifest.load_panel(path)


@pytest.mark.parametrize(
    ("poison", "message"),
    [
        ("schema_version", "response schema"),
        ("title", "response schema"),
        ("reason_min", "response schema"),
        ("reason_max", "response schema"),
        ("extra_top", "response schema"),
        ("extra_reason", "response schema"),
    ],
)
def test_response_schema_rejects_bounds_versions_and_extra_keywords(
        tmp_path, poison, message):
    schema = copy.deepcopy(manifest.load_response_schema())
    if poison == "schema_version":
        schema["$schema"] = "https://json-schema.org/draft-07/schema"
    elif poison == "title":
        schema["title"] = "unfrozen"
    elif poison == "reason_min":
        schema["properties"]["reason"]["minLength"] = 0
    elif poison == "reason_max":
        schema["properties"]["reason"]["maxLength"] = 401
    elif poison == "extra_top":
        schema["description"] = "unfrozen"
    else:
        schema["properties"]["reason"]["pattern"] = ".*"
    path = tmp_path / "schema.json"
    path.write_text(json.dumps(schema), encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        manifest.load_response_schema(path)


@pytest.mark.parametrize(
    ("stage", "expected", "extension"),
    [
        ("smoke", 24, 0),
        ("calibration", 96, 0),
        ("reliability", 24, 0),
        ("private", 96, 96),
    ],
)
def test_samples_have_exact_counts_and_no_visible_hidden_truth(
        samples, stage, expected, extension):
    sample = samples[stage]
    assert sample["manifest_kind"] == "immutable_plan"
    assert sample["stage"] == stage
    assert sample["entry_count"] == len(sample["entries"]) == expected
    assert sample["extension_entry_count"] == len(
        sample["extension_entries"]
    ) == extension
    for row in sample["entries"] + sample["extension_entries"]:
        assert set(row) == {
            "occurrence_id", "item_id", "model_execution_order",
        }
        assert not (set(row) & HIDDEN_ENTRY_KEYS)
        assert row["model_execution_order"] in [
            list(MODELS[index:] + MODELS[:index]) for index in range(3)
        ]
    serialized = json.dumps(sample["entries"] + sample["extension_entries"])
    assert not any(f'"{key}"' in serialized for key in HIDDEN_ENTRY_KEYS)


def test_samples_are_deterministic_and_seed_changes_only_predeclared_order(bank_data):
    episodes, sidecar = bank_data
    first = manifest.build_sample("private", episodes, sidecar, SEED)
    again = manifest.build_sample("private", episodes, sidecar, SEED)
    other = manifest.build_sample("private", episodes, sidecar, SEED + 1)

    assert first == again
    assert first["plan_hash"] == manifest.canonical_sha256({
        key: value for key, value in first.items() if key != "plan_hash"
    })
    assert first != other
    assert {row["item_id"] for row in first["entries"]} | {
        row["item_id"] for row in first["extension_entries"]
    } == {
        row["item_id"] for row in other["entries"]
    } | {
        row["item_id"] for row in other["extension_entries"]
    }


@pytest.mark.parametrize(
    "poison",
    [
        "panel", "sol", "seed", "count", "entry_extra", "duplicate_item",
        "occurrence", "model_rotation", "private_overlap",
    ],
)
def test_semantic_plan_validator_rejects_rehashed_poison(
        poison, samples, bank_data):
    episodes, sidecar = bank_data
    plan = copy.deepcopy(samples["private"])
    if poison == "panel":
        plan["panel_logical_model_ids"] = list(reversed(MODELS))
    elif poison == "sol":
        plan["panel_logical_model_ids"][-1] = "gpt-5.6-sol"
    elif poison == "seed":
        plan["seed"] += 1
    elif poison == "count":
        plan["entry_count"] -= 1
    elif poison == "entry_extra":
        plan["entries"][0]["true_type"] = "benign"
    elif poison == "duplicate_item":
        plan["entries"][1]["item_id"] = plan["entries"][0]["item_id"]
    elif poison == "occurrence":
        plan["entries"][0]["occurrence_id"] = "calibration-001"
    elif poison == "model_rotation":
        plan["entries"][0]["model_execution_order"] = list(MODELS)
    else:
        plan["extension_entries"][0]["item_id"] = plan["entries"][0][
            "item_id"
        ]
    rehash_plan(plan)

    with pytest.raises(ValueError, match="sample plan semantic"):
        manifest.validate_sample_plan(plan, episodes, sidecar)


def test_sample_manifests_require_one_coherent_seed(samples, bank_data):
    episodes, sidecar = bank_data
    changed = copy.deepcopy(samples)
    changed["smoke"] = manifest.build_sample(
        "smoke", episodes, sidecar, SEED + 1
    )
    with pytest.raises(ValueError, match="coherent seed"):
        manifest.validate_sample_manifests(changed, episodes, sidecar)


def test_sampling_rejects_incomplete_684_bank_and_missing_private_pair(bank_data):
    episodes, sidecar = bank_data
    public_id = next(row["id"] for row in episodes if row["split"] == "public")
    without_public = [row for row in episodes if row["id"] != public_id]
    public_sidecar = {key: value for key, value in sidecar.items()
                      if key != public_id}
    with pytest.raises(ValueError, match="684"):
        manifest.build_sample("smoke", without_public, public_sidecar, SEED)

    target_pair = next(
        hidden["pair_id"] for hidden in sidecar.values()
        if hidden["pair_id"].startswith("CRPAIR-")
        and hidden["base_rate_benign"] == 0.8
        and hidden["cue_variant"] == "strong"
    )
    removed_ids = {
        item_id for item_id, hidden in sidecar.items()
        if hidden["pair_id"] == target_pair
    }
    without_pair = [row for row in episodes if row["id"] not in removed_ids]
    pair_sidecar = {key: value for key, value in sidecar.items()
                    if key not in removed_ids}
    with pytest.raises(ValueError, match="288 private pairs|684"):
        manifest.build_sample("private", without_pair, pair_sidecar, SEED)


def test_sampling_rejects_defeat_class_and_latent_sidecar_poison(bank_data):
    episodes, sidecar = bank_data
    target = next(row for row in episodes if row["split"] == "private")

    defeat_poison = copy.deepcopy(sidecar)
    defeat_poison[target["id"]]["defeat_class"] = "non_sequitur_invalid"
    with pytest.raises(ValueError, match="defeat class"):
        manifest.build_sample("private", episodes, defeat_poison, SEED)

    latent_poison = copy.deepcopy(sidecar)
    latent_poison[target["id"]]["latent_evidence"]["family"] = next(
        family for family in generator.FAMILY_CODES
        if family != target["template_family"]
    )
    with pytest.raises(ValueError, match="latent evidence"):
        manifest.build_sample("private", episodes, latent_poison, SEED)


@pytest.mark.parametrize("poison", ["empty_public_sidecar", "public_family"])
def test_complete_bank_deeply_validates_public_rows(bank_data, poison):
    episodes, sidecar = bank_data
    changed_episodes = copy.deepcopy(episodes)
    changed_sidecar = copy.deepcopy(sidecar)
    public = next(row for row in changed_episodes if row["split"] == "public")
    if poison == "empty_public_sidecar":
        changed_sidecar[public["id"]] = {}
    else:
        public["template_family"] = "POISON"

    with pytest.raises(ValueError, match="canonical|public|sidecar"):
        manifest.build_sample(
            "private", changed_episodes, changed_sidecar, SEED
        )


def test_complete_bank_rejects_coordinated_unsampled_semantic_and_text_poison(
        bank_data, samples):
    episodes, sidecar = bank_data
    sampled_ids = {
        row["item_id"]
        for row in samples["private"]["entries"]
        + samples["private"]["extension_entries"]
    }
    changed_episodes, changed_sidecar = coordinated_unsampled_poison(
        episodes, sidecar, sampled_ids
    )

    with pytest.raises(
            ValueError,
            match="canonical|defeat class|transcript|latent|expected_stage3"):
        manifest.build_sample(
            "private", changed_episodes, changed_sidecar, SEED
        )


@pytest.mark.parametrize(
    "poison",
    [
        "stage2_text", "stage1_truth_leak", "scoring_label",
        "expected_stage3", "signal_band", "coordinated_defeat",
    ],
)
def test_complete_bank_rejects_each_isolated_unsampled_poison(
        poison, bank_data, samples):
    episodes, sidecar = bank_data
    sampled_ids = {
        row["item_id"]
        for row in samples["private"]["entries"]
        + samples["private"]["extension_entries"]
    }
    pair_members = defaultdict(set)
    for item_id, hidden in sidecar.items():
        if hidden["pair_id"].startswith("CRPAIR-"):
            pair_members[hidden["pair_id"]].add(item_id)
    target_ids = next(
        item_ids for item_ids in pair_members.values()
        if item_ids.isdisjoint(sampled_ids)
    )
    changed_episodes = copy.deepcopy(episodes)
    changed_sidecar = copy.deepcopy(sidecar)
    by_id = {row["id"]: row for row in changed_episodes}
    target_id = sorted(target_ids)[0]
    hidden = changed_sidecar[target_id]
    if poison == "stage2_text":
        by_id[target_id]["multiturn_script"]["stage_2"] += " arbitrary poison"
    elif poison == "stage1_truth_leak":
        by_id[target_id]["multiturn_script"]["stage_1"] += (
            f" true_type={hidden['true_type']}"
        )
    elif poison == "scoring_label":
        hidden["scoring_key"]["auc_label"] = 1 - hidden["scoring_key"][
            "auc_label"
        ]
    elif poison == "expected_stage3":
        hidden["expected_stage3"]["posterior_direction"] = 999
    elif poison == "signal_band":
        hidden["latent_evidence"]["signal_band"] = "POISON"
    else:
        for item_id in target_ids:
            changed_sidecar[item_id]["defeat_class"] = "non_sequitur_invalid"
            changed_sidecar[item_id]["latent_evidence"][
                "defeat_class"
            ] = "non_sequitur_invalid"

    with pytest.raises(ValueError, match="canonical|defeat class|construction"):
        manifest.build_sample(
            "private", changed_episodes, changed_sidecar, SEED
        )


def test_smoke_is_one_pair_per_family_at_family_mod_four_cue(samples, bank_data):
    _, sidecar = bank_data
    smoke = samples["smoke"]
    chunks = pair_chunks(smoke, sidecar)
    assert len(chunks) == 12

    observed = {}
    prior_pairs = Counter()
    for chunk in chunks:
        hidden = sidecar[chunk[0]["item_id"]]
        family = hidden["latent_evidence"]["family"]
        observed[family] = hidden["cue_variant"]
        prior_pairs[hidden["base_rate_benign"]] += 1
    assert observed == {
        family: generator.CUE_VARIANTS[index % 4]
        for index, family in enumerate(generator.FAMILY_CODES)
    }
    assert prior_pairs == Counter({0.2: 4, 0.5: 4, 0.8: 4})


def test_calibration_is_all_48_complete_pairs(samples, bank_data):
    episodes, sidecar = bank_data
    calibration_ids = {
        episode["id"] for episode in episodes if episode["split"] == "calibration"
    }
    sample = samples["calibration"]

    assert {row["item_id"] for row in sample["entries"]} == calibration_ids
    assert len(pair_chunks(sample, sidecar)) == 48


def test_reliability_repeats_smoke_items_as_fresh_occurrences(samples):
    smoke = samples["smoke"]
    reliability = samples["reliability"]

    assert {row["item_id"] for row in reliability["entries"]} == {
        row["item_id"] for row in smoke["entries"]
    }
    assert {row["occurrence_id"] for row in reliability["entries"]}.isdisjoint(
        {row["occurrence_id"] for row in smoke["entries"]}
    )
    assert all(row["occurrence_id"].startswith("reliability-")
               for row in reliability["entries"])


def test_private_primary_and_extension_are_pair_complete_balanced_and_disjoint(
        samples, bank_data):
    _, sidecar = bank_data
    private = samples["private"]
    primary_chunks = pair_chunks(private, sidecar)
    extension_chunks = pair_chunks(private, sidecar, extension=True)
    assert len(primary_chunks) == len(extension_chunks) == 48

    primary_ids = {row["item_id"] for row in private["entries"]}
    extension_ids = {row["item_id"] for row in private["extension_entries"]}
    assert primary_ids.isdisjoint(extension_ids)

    for chunks in (primary_chunks, extension_chunks):
        cells = Counter()
        priors = Counter()
        for chunk in chunks:
            hidden = sidecar[chunk[0]["item_id"]]
            cell = (
                hidden["latent_evidence"]["family"], hidden["cue_variant"]
            )
            cells[cell] += 1
            priors[hidden["base_rate_benign"]] += 1
        assert cells == Counter({
            (family, cue): 1
            for family in generator.FAMILY_CODES
            for cue in generator.CUE_VARIANTS
        })
        assert priors == Counter({0.2: 16, 0.5: 16, 0.8: 16})


def test_pair_arm_and_model_execution_orders_rotate_deterministically(
        samples, bank_data):
    _, sidecar = bank_data
    for stage in STAGES:
        for extension in (False, True):
            rows = entries(samples[stage], extension=extension)
            if not rows:
                continue
            chunks = pair_chunks(samples[stage], sidecar, extension=extension)
            orientations = [
                tuple(sidecar[row["item_id"]]["true_type"] for row in chunk)
                for chunk in chunks
            ]
            assert set(orientations) == {
                ("benign", "malicious"), ("malicious", "benign"),
            }
            order_counts = Counter(tuple(row["model_execution_order"])
                                   for row in rows)
            assert set(order_counts) == {
                MODELS[index:] + MODELS[:index] for index in range(3)
            }
            assert max(order_counts.values()) - min(order_counts.values()) <= 1


def test_pair_arms_are_separated_in_the_deterministic_execution_order(
        samples, bank_data):
    _, sidecar = bank_data
    for stage in STAGES:
        for extension in (False, True):
            rows = entries(samples[stage], extension=extension)
            if not rows:
                continue
            positions = defaultdict(list)
            for index, row in enumerate(rows):
                positions[sidecar[row["item_id"]]["pair_id"]].append(index)
            assert all(len(pair_positions) == 2
                       for pair_positions in positions.values())
            assert min(
                abs(pair_positions[1] - pair_positions[0])
                for pair_positions in positions.values()
            ) > 1


def test_plan_write_is_immutable_and_run_state_is_separate_append_only(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    plan_path = tmp_path / "calibration-plan.json"
    state_path = tmp_path / "calibration-state.jsonl"
    manifest.write_plan_manifest(
        plan_path, samples["calibration"], episodes, sidecar, root=tmp_path
    )
    first_bytes = plan_path.read_bytes()
    with pytest.raises(ValueError, match="immutable plan"):
        manifest.write_plan_manifest(
            plan_path, samples["calibration"], episodes, sidecar,
            root=tmp_path,
        )

    first_event = run_event(samples["calibration"], event_id="event-001")
    second_event = {**first_event, "event_id": "event-002", "state": "complete"}
    manifest.append_run_state_event(
        state_path, first_event, samples["calibration"], root=tmp_path
    )
    first_line = state_path.read_bytes()
    manifest.append_run_state_event(
        state_path, second_event, samples["calibration"], root=tmp_path
    )

    assert plan_path.read_bytes() == first_bytes
    assert state_path.read_bytes().startswith(first_line)
    state_rows = [json.loads(line) for line in state_path.read_text().splitlines()]
    assert state_rows == [first_event, second_event]
    assert set(first_event) == set(manifest.RUN_STATE_EVENT_KEYS)
    assert not (set(first_event) & set(manifest.PLAN_ENTRY_KEYS))


@pytest.mark.parametrize(
    ("poison", "message"),
    [
        ("unknown_occurrence", "occurrence"),
        ("timestamp", "RFC3339"),
        ("attempt", "attempt"),
        ("invalid_first_transition", "transition"),
    ],
)
def test_run_state_is_plan_bound_and_transition_checked(
        tmp_path, samples, poison, message):
    plan = samples["calibration"]
    event = run_event(plan, event_id="event-poison")
    if poison == "unknown_occurrence":
        event["plan_occurrence_id"] = "private-999"
    elif poison == "timestamp":
        event["timestamp_utc"] = "2026-07-10 12:00:00"
    elif poison == "attempt":
        event["attempt"] = 4
    else:
        event["state"] = "complete"
    with pytest.raises(ValueError, match=message):
        manifest.append_run_state_event(
            tmp_path / "state.jsonl", event, plan, root=tmp_path
        )


def test_run_state_rejects_duplicate_ids_terminal_reentry_and_time_reversal(
        tmp_path, samples):
    plan = samples["calibration"]
    path = tmp_path / "state.jsonl"
    base = run_event(plan, event_id="event-1")
    manifest.append_run_state_event(path, base, plan, root=tmp_path)
    duplicate = {**base, "state": "complete"}
    with pytest.raises(ValueError, match="duplicate"):
        manifest.append_run_state_event(path, duplicate, plan, root=tmp_path)
    reversed_time = {
        **base,
        "event_id": "event-2",
        "state": "complete",
        "timestamp_utc": "2026-07-10T11:59:59Z",
    }
    with pytest.raises(ValueError, match="timestamp"):
        manifest.append_run_state_event(path, reversed_time, plan, root=tmp_path)
    complete = {**reversed_time, "timestamp_utc": "2026-07-10T12:01:00Z"}
    manifest.append_run_state_event(path, complete, plan, root=tmp_path)
    reentry = {
        **complete,
        "event_id": "event-3",
        "state": "started",
        "attempt": 2,
        "timestamp_utc": "2026-07-10T12:02:00Z",
    }
    with pytest.raises(ValueError, match="terminal|transition"):
        manifest.append_run_state_event(path, reentry, plan, root=tmp_path)


def test_run_state_event_contract_binds_plan_item_and_integrity_session():
    assert {"plan_hash", "item_id", "session_attempt"} <= set(
        manifest.RUN_STATE_EVENT_KEYS
    )


def test_run_state_history_cannot_switch_to_a_different_plan(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    plan_a = samples["calibration"]
    plan_b = manifest.build_sample(
        "calibration", episodes, sidecar, SEED + 1
    )
    assert plan_a["plan_hash"] != plan_b["plan_hash"]
    path = tmp_path / "plan-bound.jsonl"
    manifest.append_run_state_event(
        path, run_event(plan_a, event_id="plan-a-start"), plan_a,
        root=tmp_path,
    )
    plan_b_complete = run_event(
        plan_b, event_id="plan-b-complete", state="complete",
        timestamp="2026-07-10T12:01:00Z",
    )
    with pytest.raises(ValueError, match="plan hash"):
        manifest.append_run_state_event(
            path, plan_b_complete, plan_b, root=tmp_path
        )


def test_run_state_rejects_occurrence_item_remapping(tmp_path, samples):
    plan = samples["calibration"]
    event = run_event(plan, event_id="wrong-item")
    event["item_id"] = plan["entries"][1]["item_id"]
    with pytest.raises(ValueError, match="item"):
        manifest.append_run_state_event(
            tmp_path / "wrong-item.jsonl", event, plan, root=tmp_path
        )


def test_run_state_models_one_whole_episode_rerun_with_transport_reset(
        tmp_path, samples):
    plan = samples["calibration"]
    path = tmp_path / "integrity-rerun.jsonl"
    events = [
        run_event(plan, event_id="run1-start"),
        run_event(
            plan, event_id="run1-retry1", state="retry",
            timestamp="2026-07-10T12:01:00Z",
        ),
        run_event(
            plan, event_id="run1-start2", attempt=2,
            timestamp="2026-07-10T12:02:00Z",
        ),
        run_event(
            plan, event_id="run1-retry2", state="retry", attempt=2,
            timestamp="2026-07-10T12:03:00Z",
        ),
        run_event(
            plan, event_id="run1-start3", attempt=3,
            timestamp="2026-07-10T12:04:00Z",
        ),
        run_event(
            plan, event_id="run1-invalid", state="invalidated", attempt=3,
            timestamp="2026-07-10T12:05:00Z",
        ),
        run_event(
            plan, event_id="run2-start", session_attempt=2, attempt=1,
            timestamp="2026-07-10T12:06:00Z",
        ),
        run_event(
            plan, event_id="run2-complete", session_attempt=2,
            state="complete", attempt=1,
            timestamp="2026-07-10T12:07:00Z",
        ),
    ]
    for event in events:
        manifest.append_run_state_event(path, event, plan, root=tmp_path)

    third_session = run_event(
        plan, event_id="run3-start", session_attempt=3,
        timestamp="2026-07-10T12:08:00Z",
    )
    with pytest.raises(ValueError, match="session|rerun"):
        manifest.append_run_state_event(
            path, third_session, plan, root=tmp_path
        )
    orphan_second_session = run_event(
        plan, event_id="orphan-run2", session_attempt=2
    )
    with pytest.raises(ValueError, match="session|rerun|invalidated"):
        manifest.append_run_state_event(
            tmp_path / "orphan-rerun.jsonl", orphan_second_session, plan,
            root=tmp_path,
        )


def test_run_state_enforces_declared_model_execution_order(tmp_path, samples):
    plan = samples["calibration"]
    order = plan["entries"][0]["model_execution_order"]
    wrong_first = run_event(
        plan, event_id="wrong-model-first", model=order[-1]
    )
    with pytest.raises(ValueError, match="model execution order"):
        manifest.append_run_state_event(
            tmp_path / "wrong-model-order.jsonl", wrong_first, plan,
            root=tmp_path,
        )

    path = tmp_path / "valid-model-order.jsonl"
    first_start = run_event(plan, event_id="model1-start", model=order[0])
    first_complete = run_event(
        plan, event_id="model1-complete", model=order[0], state="complete",
        timestamp="2026-07-10T12:01:00Z",
    )
    second_start = run_event(
        plan, event_id="model2-start", model=order[1],
        timestamp="2026-07-10T12:02:00Z",
    )
    for event in (first_start, first_complete, second_start):
        manifest.append_run_state_event(path, event, plan, root=tmp_path)


def test_run_state_enforces_occurrence_before_model_traversal(
        tmp_path, samples):
    plan = samples["calibration"]
    early_second_occurrence = run_event(
        plan, event_id="early-occurrence-2", occurrence_index=1
    )
    with pytest.raises(ValueError, match="occurrence execution order"):
        manifest.append_run_state_event(
            tmp_path / "early-occurrence.jsonl", early_second_occurrence,
            plan, root=tmp_path,
        )


def test_run_state_rejects_transport_retry_after_attempt_three():
    with pytest.raises(ValueError, match="retry|attempt"):
        manifest._validate_run_transition(
            {"state": "started", "attempt": 3},
            {"state": "retry", "attempt": 3},
        )


def test_plan_state_and_freeze_writers_reject_out_of_root_and_symlinks(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    root = tmp_path / "safe"
    root.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    with pytest.raises(ValueError, match="outside root"):
        manifest.write_plan_manifest(
            outside / "plan.json", samples["smoke"], episodes, sidecar,
            root=root,
        )

    target = outside / "state.jsonl"
    target.write_text("", encoding="utf-8")
    symlink = root / "state.jsonl"
    symlink.symlink_to(target)
    event = run_event(samples["smoke"], event_id="event-link")
    with pytest.raises(ValueError, match="symlink"):
        manifest.append_run_state_event(
            symlink, event, samples["smoke"], root=root
        )


def make_freeze_root(tmp_path, bank_data):
    episodes, sidecar = bank_data
    root = tmp_path / "bank"
    for paths in manifest.FREEZE_FILE_GROUPS.values():
        for relative in paths:
            source = BANK / relative
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.exists():
                shutil.copy2(source, target)
            else:
                # Generated artifacts are deliberately stale in the real bank;
                # freeze tests use explicit stand-ins without regenerating it.
                target.write_text(f"fixture for {relative}\n", encoding="utf-8")

    split_paths = {
        "private": root / "episodes" / "private_bank.yaml",
        "calibration": root / "episodes" / "calibration_bank.yaml",
        "public": root / "seeds_public.yaml",
    }
    for split, path in split_paths.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(
            [row for row in episodes if row["split"] == split],
            sort_keys=False, allow_unicode=True, width=100,
        ), encoding="utf-8")
    (root / "sidecar" / "ground_truth.json").write_text(
        json.dumps(sidecar, indent=1), encoding="utf-8"
    )
    pairs = {"private": {}, "calibration": {}}
    for episode in episodes:
        split = episode["split"]
        if split not in pairs:
            continue
        hidden = sidecar[episode["id"]]
        pairs[split].setdefault(hidden["pair_id"], {})[
            hidden["true_type"]
        ] = episode["id"]
    (root / "sidecar" / "pair_registry.json").write_text(
        json.dumps(pairs, indent=1), encoding="utf-8"
    )
    judge_map = generator.build_judge_token_map(episodes, SEED)
    (root / "sidecar" / "judge_token_map.json").write_text(
        json.dumps(judge_map, indent=1), encoding="utf-8"
    )
    report = {"seed": SEED, **generator._stats(episodes, sidecar, pairs)}
    (root / "reports" / "generation_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    fake_codex = tmp_path / "codex-test"
    fake_codex.write_bytes(b"#!/bin/sh\necho codex-cli-test\n")
    fake_codex.chmod(0o755)
    return root, fake_codex


def test_freeze_groups_cover_load_bearing_production_surfaces():
    assert {
        "lib/canary.py", "matching_audit.py",
    } <= set(manifest.FREEZE_FILE_GROUPS["construction"])
    assert {
        "adversarial/lexical_baselines.py",
        "adversarial/static_filter.py",
        "adversarial/run_adversarial.py",
    } <= set(manifest.FREEZE_FILE_GROUPS["adversarial"])
    assert "analysis/synth_recovery.py" in manifest.FREEZE_FILE_GROUPS[
        "analysis"
    ]
    assert "export/export_megamatrix.py" in manifest.FREEZE_FILE_GROUPS[
        "export"
    ]
    assert "scorers/__init__.py" in manifest.FREEZE_FILE_GROUPS["scoring"]
    assert {"selfcheck.py", "pilot_protocol.md"} <= set(
        manifest.FREEZE_FILE_GROUPS["construction"]
    )
    assert {
        "reports/lexical_baseline_report.json",
        "export/export_report.json",
    } <= set(manifest.FREEZE_FILE_GROUPS["generated"])


def test_freeze_is_canonical_complete_and_refuses_launch_before_freeze(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    root, fake_codex = make_freeze_root(tmp_path, bank_data)
    kwargs = {
        "sample_manifests": samples,
        "episodes": episodes,
        "sidecar": sidecar,
        "codex_cli_path": fake_codex,
        "codex_cli_version": "codex-cli-test",
    }

    with pytest.raises(ValueError, match="freeze required before private"):
        manifest.validate_private_launch(None, root, **kwargs)
    first = manifest.build_freeze(root, **kwargs)
    again = manifest.build_freeze(root, **kwargs)

    assert first == again
    assert first["freeze_hash"] == manifest.canonical_sha256({
        key: value for key, value in first.items() if key != "freeze_hash"
    })
    assert set(first["file_groups"]) == {
        "construction", "scoring", "analysis", "pilot", "generated",
        "coverage", "adversarial", "export",
    }
    assert set(first["sample_manifest_hashes"]) == set(STAGES)
    assert first["panel_manifest_hash"] == first["file_hashes"][
        "pilot/panel_manifest.json"
    ]
    assert first["response_schema_hash"] == first["file_hashes"][
        "pilot/response_schema.json"
    ]
    assert first["coverage_manifest_hash"] == first["file_hashes"][
        "export/coverage_map.json"
    ]
    assert first["runtime"]["codex_cli"] == {
        "path": os.fspath(fake_codex.resolve()),
        "version": "codex-cli-test",
        "binary_sha256": manifest.sha256_file(fake_codex),
    }
    assert first["runtime"]["python"]["version"]
    assert {"numpy", "scikit-learn", "PyYAML", "pytest"} <= set(
        first["runtime"]["dependencies"]
    )
    assert manifest.validate_private_launch(first, root, **kwargs)["valid"] is True


def test_private_launch_detects_file_sample_and_binary_tamper(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    root, fake_codex = make_freeze_root(tmp_path, bank_data)
    kwargs = {
        "sample_manifests": samples,
        "episodes": episodes,
        "sidecar": sidecar,
        "codex_cli_path": fake_codex,
        "codex_cli_version": "codex-cli-test",
    }
    freeze = manifest.build_freeze(root, **kwargs)

    target = root / "lib" / "cue_surfaces.py"
    target.write_text(target.read_text(encoding="utf-8") + "# tamper\n",
                      encoding="utf-8")
    with pytest.raises(ValueError, match="freeze hash mismatch"):
        manifest.validate_private_launch(freeze, root, **kwargs)

    root, fake_codex = make_freeze_root(tmp_path / "sample", bank_data)
    sample_freeze = manifest.build_freeze(
        root,
        sample_manifests=samples,
        episodes=episodes,
        sidecar=sidecar,
        codex_cli_path=fake_codex,
        codex_cli_version="codex-cli-test",
    )
    changed_samples = dict(samples)
    changed_samples["private"] = dict(samples["private"])
    changed_samples["private"]["seed"] += 1
    with pytest.raises(ValueError, match="freeze hash mismatch"):
        manifest.validate_private_launch(
            sample_freeze, root,
            sample_manifests=changed_samples,
            episodes=episodes,
            sidecar=sidecar,
            codex_cli_path=fake_codex,
            codex_cli_version="codex-cli-test",
        )

    root, fake_codex = make_freeze_root(tmp_path / "binary", bank_data)
    binary_freeze = manifest.build_freeze(
        root,
        sample_manifests=samples,
        episodes=episodes,
        sidecar=sidecar,
        codex_cli_path=fake_codex,
        codex_cli_version="codex-cli-test",
    )
    fake_codex.write_bytes(fake_codex.read_bytes() + b"# tamper\n")
    with pytest.raises(ValueError, match="freeze hash mismatch"):
        manifest.validate_private_launch(
            binary_freeze, root,
            sample_manifests=samples,
            episodes=episodes,
            sidecar=sidecar,
            codex_cli_path=fake_codex,
            codex_cli_version="codex-cli-test",
        )

    root, fake_codex = make_freeze_root(tmp_path / "scorer-init", bank_data)
    scorer_freeze = manifest.build_freeze(
        root, sample_manifests=samples, episodes=episodes, sidecar=sidecar,
        codex_cli_path=fake_codex, codex_cli_version="codex-cli-test",
    )
    scorer_init = root / "scorers" / "__init__.py"
    scorer_init.write_text(
        scorer_init.read_text(encoding="utf-8")
        + "\nraise RuntimeError('post-freeze poison')\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="freeze hash mismatch"):
        manifest.validate_private_launch(
            scorer_freeze, root, sample_manifests=samples,
            episodes=episodes, sidecar=sidecar,
            codex_cli_path=fake_codex,
            codex_cli_version="codex-cli-test",
        )


def test_build_freeze_rejects_semantically_invalid_panel_and_schema(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    for target_name in ("panel", "schema"):
        root, fake_codex = make_freeze_root(
            tmp_path / target_name, bank_data
        )
        if target_name == "panel":
            path = root / "pilot" / "panel_manifest.json"
            value = json.loads(path.read_text(encoding="utf-8"))
            value["manifest_version"] = "poison"
        else:
            path = root / "pilot" / "response_schema.json"
            value = json.loads(path.read_text(encoding="utf-8"))
            value["properties"]["reason"]["minLength"] = 0
        path.write_text(json.dumps(value), encoding="utf-8")
        with pytest.raises(ValueError, match="manifest version|response schema"):
            manifest.build_freeze(
                root,
                sample_manifests=samples,
                episodes=episodes,
                sidecar=sidecar,
                codex_cli_path=fake_codex,
                codex_cli_version="codex-cli-test",
            )


def test_freeze_rejects_symlinked_root_or_member(tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    root, fake_codex = make_freeze_root(tmp_path / "member", bank_data)
    target = root / "lib" / "cue_surfaces.py"
    external = tmp_path / "external.py"
    external.write_bytes(target.read_bytes())
    target.unlink()
    target.symlink_to(external)
    with pytest.raises(ValueError, match="symlink"):
        manifest.build_freeze(
            root, sample_manifests=samples, episodes=episodes, sidecar=sidecar,
            codex_cli_path=fake_codex, codex_cli_version="codex-cli-test",
        )

    real_root, fake_codex = make_freeze_root(tmp_path / "root", bank_data)
    linked_root = tmp_path / "linked-bank"
    linked_root.symlink_to(real_root, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        manifest.build_freeze(
            linked_root, sample_manifests=samples, episodes=episodes,
            sidecar=sidecar, codex_cli_path=fake_codex,
            codex_cli_version="codex-cli-test",
        )

    real_parent = tmp_path / "real-parent"
    ancestor_root, fake_codex = make_freeze_root(real_parent, bank_data)
    linked_parent = tmp_path / "linked-parent"
    linked_parent.symlink_to(real_parent, target_is_directory=True)
    root_through_linked_ancestor = linked_parent / ancestor_root.name
    assert not root_through_linked_ancestor.is_symlink()
    with pytest.raises(ValueError, match="symlink"):
        manifest.build_freeze(
            root_through_linked_ancestor, sample_manifests=samples,
            episodes=episodes, sidecar=sidecar,
            codex_cli_path=fake_codex,
            codex_cli_version="codex-cli-test",
        )


def test_codex_version_claim_is_verified_by_executing_binary(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    root, fake_codex = make_freeze_root(tmp_path, bank_data)
    with pytest.raises(ValueError, match="Codex CLI version mismatch"):
        manifest.build_freeze(
            root, sample_manifests=samples, episodes=episodes, sidecar=sidecar,
            codex_cli_path=fake_codex, codex_cli_version="caller-claim",
        )


def test_freeze_rejects_poisoned_memory_and_persisted_bank_artifacts(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    sampled_ids = {
        row["item_id"]
        for row in samples["private"]["entries"]
        + samples["private"]["extension_entries"]
    }
    changed_episodes, changed_sidecar = coordinated_unsampled_poison(
        episodes, sidecar, sampled_ids
    )
    root, fake_codex = make_freeze_root(tmp_path / "memory", bank_data)
    with pytest.raises(ValueError, match="canonical|construction|bank"):
        manifest.build_freeze(
            root, sample_manifests=samples, episodes=changed_episodes,
            sidecar=changed_sidecar, codex_cli_path=fake_codex,
            codex_cli_version="codex-cli-test",
        )

    for poison in (
            "ground_truth", "private_yaml", "pair_registry", "judge_map",
            "generation_report"):
        root, fake_codex = make_freeze_root(tmp_path / poison, bank_data)
        if poison == "ground_truth":
            (root / "sidecar" / "ground_truth.json").write_text(
                json.dumps({"POISON": {"true_type": "malicious"}}),
                encoding="utf-8",
            )
        else:
            target_and_value = {
                "private_yaml": (
                    root / "episodes" / "private_bank.yaml",
                    yaml.safe_dump([{"id": "POISON", "split": "private"}]),
                ),
                "pair_registry": (
                    root / "sidecar" / "pair_registry.json",
                    json.dumps({"private": {}}),
                ),
                "judge_map": (
                    root / "sidecar" / "judge_token_map.json",
                    json.dumps({}),
                ),
                "generation_report": (
                    root / "reports" / "generation_report.json",
                    json.dumps({"seed": SEED, "n_total": 1}),
                ),
            }
            target, value = target_and_value[poison]
            target.write_text(value, encoding="utf-8")
        with pytest.raises(
                ValueError,
                match=(
                    "disk|persisted|canonical|split artifact|sidecar|684|"
                    "registry|judge|report"
                )):
            manifest.build_freeze(
                root, sample_manifests=samples, episodes=episodes,
                sidecar=sidecar, codex_cli_path=fake_codex,
                codex_cli_version="codex-cli-test",
            )


def test_freeze_binds_bank_inputs_and_freeze_writer_is_semantic_and_confined(
        tmp_path, samples, bank_data):
    episodes, sidecar = bank_data
    root, fake_codex = make_freeze_root(
        tmp_path / "bank-input", bank_data
    )
    kwargs = {
        "sample_manifests": samples,
        "episodes": episodes,
        "sidecar": sidecar,
        "codex_cli_path": fake_codex,
        "codex_cli_version": "codex-cli-test",
    }
    freeze = manifest.build_freeze(root, **kwargs)
    assert freeze["bank_input_hashes"] == {
        "episodes": manifest.canonical_sha256(episodes),
        "sidecar": manifest.canonical_sha256(sidecar),
    }

    changed_episodes = copy.deepcopy(episodes)
    public = next(row for row in changed_episodes if row["split"] == "public")
    public["multiturn_script"]["stage_1"] += " caller-side poison"
    with pytest.raises(ValueError, match="freeze hash mismatch"):
        manifest.validate_private_launch(
            freeze, root, **{**kwargs, "episodes": changed_episodes}
        )

    semantic_poison = copy.deepcopy(freeze)
    semantic_poison["freeze_version"] = "unfrozen-version"
    semantic_poison["freeze_hash"] = manifest.canonical_sha256({
        key: value for key, value in semantic_poison.items()
        if key != "freeze_hash"
    })
    with pytest.raises(ValueError, match="invalid freeze manifest"):
        manifest.write_freeze_manifest(
            root / "pilot" / "poison-freeze.json", semantic_poison,
            root=root,
        )

    with pytest.raises(ValueError, match="outside root"):
        manifest.write_freeze_manifest(
            tmp_path / "outside-freeze.json", freeze, root=root
        )
    external = tmp_path / "external-freeze.json"
    external.write_text("", encoding="utf-8")
    linked = root / "pilot" / "linked-freeze.json"
    linked.symlink_to(external)
    with pytest.raises(ValueError, match="symlink"):
        manifest.write_freeze_manifest(linked, freeze, root=root)


def test_pilot_protocol_distinguishes_scoped_and_shared_panels_and_two_retries():
    text = (BANK / "pilot_protocol.md").read_text(encoding="utf-8")
    assert all(model in text for model in MODELS)
    assert "GPT-5.6 Sol is excluded" in text
    assert "three-model calibration panel" in text
    assert ">=8-model shared" in text
    assert "maximum two transport retries" in text
