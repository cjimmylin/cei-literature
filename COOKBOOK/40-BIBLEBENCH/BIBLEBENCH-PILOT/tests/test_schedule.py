from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import FrozenInstanceError, fields, replace
import json
import re

import pytest

import biblebench_pilot.schedule as schedule_module
from biblebench_pilot.artifacts import assert_actor_payload_safe
from biblebench_pilot.contracts import canonical_sha256
from biblebench_pilot.schedule import (
    CueVariant,
    DevelopmentEpisode,
    DevelopmentPack,
    EvidenceBundlePlan,
    LogicalCall,
    Schedule,
    compile_schedule,
)


ACTORS = ("A", "B", "C", "D")
CUES = ("C0", "C1", "C2")
HASHES = ("a" * 64, "b" * 64, "c" * 64, "d" * 64)


def _variant(cue: str, **changes) -> CueVariant:
    values = {
        "cue": cue,
        "cue_surface": {"C0": "plain", "C1": "scriptural", "C2": "secular"}[cue],
        "shared_body": "Choose the most responsible next action.",
        "task_semantics_sha256": HASHES[0],
        "answer_semantics_sha256": HASHES[1],
        "tool_schema_sha256": HASHES[2],
        "response_schema_sha256": HASHES[3],
        "decoding": {"temperature": 0, "max_tokens": 64},
        "semantic_response_tokens": ("answer", "reason"),
    }
    values.update(changes)
    return CueVariant(**values)


def _episode(index: int, **changes) -> DevelopmentEpisode:
    values = {
        "episode_id": f"ep-{index:02d}",
        "role": ("target", "null", "restraint")[index % 3],
        "forecast_payload": {"question": f"forecast-{index}", "choices": [0, 1]},
        "probe_payload": {"question": f"probe-{index}"},
        "variants": tuple(_variant(cue) for cue in CUES),
    }
    values.update(changes)
    return DevelopmentEpisode(**values)


def _pack(**changes) -> DevelopmentPack:
    values = {
        "module": "fruitbench",
        "episodes": tuple(_episode(index) for index in range(12)),
    }
    values.update(changes)
    return DevelopmentPack(**values)


def _with_episode(pack: DevelopmentPack, index: int, episode: DevelopmentEpisode):
    episodes = list(pack.episodes)
    episodes[index] = episode
    return replace(pack, episodes=tuple(episodes))


def _with_variant(
    pack: DevelopmentPack,
    episode_index: int,
    variant_index: int,
    variant: CueVariant,
) -> DevelopmentPack:
    episode = pack.episodes[episode_index]
    variants = list(episode.variants)
    variants[variant_index] = variant
    return _with_episode(pack, episode_index, replace(episode, variants=tuple(variants)))


def _schedule(seed: int = 711) -> Schedule:
    return compile_schedule(_pack(), actor_ids=ACTORS, seed=seed)


def _schedule_with_calls(
    schedule: Schedule, calls: list[LogicalCall]
) -> Schedule:
    return Schedule(
        seed=schedule.seed,
        bundles=schedule.bundles,
        logical_calls=tuple(calls),
    )


def test_compiles_required_balanced_schedule_without_reserved_condition() -> None:
    pack = _pack()

    schedule = compile_schedule(pack, actor_ids=ACTORS, seed=711)

    assert {row.cue for row in schedule.primary_rows} == {"C0", "C1", "C2"}
    assert "C3" not in schedule.to_canonical_json()
    assert len({row.bundle_id for row in schedule.forecast_rows}) == pack.episode_count * 4
    assert len(schedule.bundles) == 48
    assert len(schedule.logical_calls) == 48 * 7
    assert len(schedule.forecast_rows) == 48
    assert len(schedule.primary_rows) == 144
    assert len(schedule.probe_rows) == 144
    assert pack.role_counts() == {"target": 4, "null": 4, "restraint": 4}
    schedule.assert_counterbalanced()


@pytest.mark.parametrize("reserved", ["C3", "c3", "prefix-c3-suffix"])
def test_compile_rejects_reserved_condition_in_authored_pack_any_case(
    reserved: str,
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], forecast_payload={"ordinary_note": reserved}
    )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "surface", ["c0", "C0", "treatment c1", "(C2)", "condition c3"]
)
def test_compile_rejects_internal_condition_labels_in_cue_surfaces_any_case(
    surface: str,
) -> None:
    pack = _pack()
    exposed = replace(pack.episodes[0].variants[1], cue_surface=surface)

    with pytest.raises(ValueError):
        compile_schedule(
            _with_variant(pack, 0, 1, exposed), actor_ids=ACTORS, seed=711
        )


def test_canonical_schedule_rejects_lowercase_reserved_condition() -> None:
    encoded = _schedule().to_canonical_json()
    assert "C3" not in encoded
    assert re.search(
        r"(?<![A-Za-z0-9])C3(?![A-Za-z0-9])", encoded, re.IGNORECASE
    ) is None

    with pytest.raises(ValueError):
        compile_schedule(
            _pack(), actor_ids=("A", "B", "C", "actor-c3"), seed=711
        )


@pytest.mark.parametrize(
    "later_key",
    [
        "lens",
        "lens_id",
        "Lens-ID",
        "intervention",
        "interventionId",
        "physical_id",
        "physical_attempt_id",
        "attempt_id",
        "lens_call_id",
        "lens_identifier",
        "lens_result",
        "lens_description",
        "intervention_call_id",
        "intervention_config",
        "physical_call_id",
        "physical_attempt",
        "provider_attempt_id",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_compile_rejects_later_scope_actor_visible_fields_recursively(
    later_key: str, field_name: str
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], **{field_name: {"nested": [{later_key: "opaque"}]}}
    )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_later_scope_prose_and_nonexact_keys_remain_allowed() -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        forecast_payload={
            "ordinary_notes": "A lens may help describe the ordinary prose.",
            "description": "An intervention may be discussed.",
            "attempt_notes": "A physical attempt can be described.",
        },
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload == episode.forecast_payload


def test_compile_checks_every_detached_actor_visible_payload(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    checked: list[dict] = []

    def recording_policy(payload) -> None:
        checked.append(payload)
        assert_actor_payload_safe(payload)

    monkeypatch.setattr(
        schedule_module, "assert_actor_payload_safe", recording_policy
    )

    schedule = compile_schedule(_pack(), actor_ids=ACTORS, seed=711)

    assert len(schedule.logical_calls) == 336
    assert len(checked) == len(schedule.logical_calls) * 2
    assert {id(payload) for payload in checked} == {
        id(row.request_payload) for row in schedule.logical_calls
    }
    assert Counter(id(payload) for payload in checked) == Counter(
        {id(row.request_payload): 2 for row in schedule.logical_calls}
    )


@pytest.mark.parametrize(
    ("surface", "body", "tokens"),
    [
        ("actor_model", "Choose the next action.", ("answer", "reason")),
        ("ordinary surface", "model_identity", ("answer", "reason")),
        ("ordinary surface", "Choose the next action.", ("private",)),
    ],
)
def test_compile_rejects_artifact_policy_leaks_from_variant_fields(
    surface: str, body: str, tokens: tuple[str, ...]
) -> None:
    pack = _pack()
    variants = tuple(
        replace(
            variant,
            cue_surface=surface if variant.cue == "C1" else variant.cue_surface,
            shared_body=body,
            semantic_response_tokens=tokens,
        )
        for variant in pack.episodes[0].variants
    )
    episode = replace(pack.episodes[0], variants=variants)

    with pytest.raises(ValueError, match="unsafe model-visible payload"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    ("field_name", "payload"),
    [
        ("forecast_payload", {"role": "do-not-echo-this"}),
        ("forecast_payload", {"private": "do-not-echo-this"}),
        ("probe_payload", {"actor_model": "do-not-echo-this"}),
        ("probe_payload", {"model_identity": "do-not-echo-this"}),
        ("probe_payload", {"expected_label": "do-not-echo-this"}),
        ("probe_payload", {"gold": "do-not-echo-this"}),
    ],
)
def test_compile_rejects_actor_payload_policy_keys_without_echo(
    field_name: str, payload: dict
) -> None:
    pack = _pack()
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError) as caught:
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )

    assert "do-not-echo-this" not in str(caught.value)


def test_public_types_are_frozen_and_have_only_frozen_contract_fields() -> None:
    expected = {
        CueVariant: (
            "cue",
            "cue_surface",
            "shared_body",
            "task_semantics_sha256",
            "answer_semantics_sha256",
            "tool_schema_sha256",
            "response_schema_sha256",
            "decoding",
            "semantic_response_tokens",
        ),
        DevelopmentEpisode: (
            "episode_id",
            "role",
            "forecast_payload",
            "probe_payload",
            "variants",
        ),
        DevelopmentPack: ("module", "episodes"),
        EvidenceBundlePlan: (
            "bundle_id",
            "actor_id",
            "module",
            "episode_id",
            "role",
            "logical_call_ids",
        ),
        LogicalCall: (
            "logical_call_id",
            "bundle_id",
            "actor_id",
            "module",
            "episode_id",
            "role",
            "call_kind",
            "cue",
            "presentation_position",
            "request_payload",
        ),
        Schedule: ("seed", "bundles", "logical_calls"),
    }
    for kind, names in expected.items():
        assert tuple(field.name for field in fields(kind)) == names

    with pytest.raises(FrozenInstanceError):
        _schedule().seed = 1

    assert not any("physical" in field.name for field in fields(LogicalCall))


def test_global_order_and_bundle_sequences_follow_documented_rotations() -> None:
    schedule = _schedule()
    actors = tuple(sorted(ACTORS))
    episodes = tuple(sorted(episode.episode_id for episode in _pack().episodes))
    expected_bundle_pairs = []
    for episode_index, episode_id in enumerate(episodes):
        offset = (schedule.seed + episode_index) % len(actors)
        actor_order = actors[offset:] + actors[:offset]
        expected_bundle_pairs.extend((actor, episode_id) for actor in actor_order)

    assert [
        (bundle.actor_id, bundle.episode_id) for bundle in schedule.bundles
    ] == expected_bundle_pairs

    actor_index = {actor: index for index, actor in enumerate(actors)}
    episode_index = {episode: index for index, episode in enumerate(episodes)}
    first_cues = {}
    for bundle in schedule.bundles:
        calls = [
            row for row in schedule.logical_calls if row.bundle_id == bundle.bundle_id
        ]
        rotation = (
            schedule.seed
            + actor_index[bundle.actor_id]
            + episode_index[bundle.episode_id]
        ) % 3
        expected_cues = CUES[rotation:] + CUES[:rotation]
        assert calls[0].call_kind == "forecast"
        assert calls[0].cue is None
        assert calls[0].presentation_position == -1
        assert [row.call_kind for row in calls] == [
            "forecast",
            "primary",
            "probe",
            "primary",
            "probe",
            "primary",
            "probe",
        ]
        assert [row.cue for row in calls[1::2]] == list(expected_cues)
        assert [row.cue for row in calls[2::2]] == list(expected_cues)
        assert [row.presentation_position for row in calls[1:]] == [0, 0, 1, 1, 2, 2]
        first_cues[(bundle.actor_id, bundle.episode_id)] = expected_cues[0]

    counts = defaultdict(Counter)
    for row in schedule.primary_rows:
        counts[(row.actor_id, row.presentation_position)][row.cue] += 1
    assert set(counts) == {(actor, position) for actor in ACTORS for position in range(3)}
    assert all(counter == Counter({"C0": 4, "C1": 4, "C2": 4}) for counter in counts.values())
    assert len({first_cues[(actor, episodes[0])] for actor in ACTORS}) == 3


def test_identifiers_use_canonical_domain_separated_material() -> None:
    schedule = _schedule()
    bundle = schedule.bundles[0]
    call = schedule.logical_calls[0]
    bundle_material = {
        "domain": "biblebench.bundle.v1",
        "seed": schedule.seed,
        "actor_id": bundle.actor_id,
        "module": bundle.module,
        "episode_id": bundle.episode_id,
        "role": bundle.role,
    }
    call_material = {
        "domain": "biblebench.logical_call.v1",
        "seed": schedule.seed,
        "bundle_id": call.bundle_id,
        "actor_id": call.actor_id,
        "module": call.module,
        "episode_id": call.episode_id,
        "role": call.role,
        "call_kind": call.call_kind,
        "cue": call.cue,
        "presentation_position": call.presentation_position,
    }

    assert bundle.bundle_id == canonical_sha256(bundle_material)[:16]
    assert call.logical_call_id == canonical_sha256(call_material)[:16]
    all_ids = [bundle.bundle_id for bundle in schedule.bundles]
    all_ids.extend(row.logical_call_id for row in schedule.logical_calls)
    assert len(all_ids) == len(set(all_ids))
    assert all(re.fullmatch(r"[0-9a-f]{16}", identifier) for identifier in all_ids)


def test_determinism_seed_effect_and_membership() -> None:
    first = _schedule(711)
    repeated = _schedule(711)
    changed = _schedule(712)

    assert first == repeated
    assert first.to_canonical_json().encode("utf-8") == repeated.to_canonical_json().encode("utf-8")
    assert first.to_canonical_json() != changed.to_canonical_json()
    assert [row.cue for row in first.primary_rows] != [row.cue for row in changed.primary_rows]
    membership = lambda schedule: {
        (bundle.actor_id, bundle.module, bundle.episode_id, bundle.role)
        for bundle in schedule.bundles
    }
    assert membership(first) == membership(changed)
    assert Counter(row.call_kind for row in first.logical_calls) == Counter(
        row.call_kind for row in changed.logical_calls
    )


def test_request_payloads_are_minimal_private_safe_and_detached() -> None:
    pack = _pack()
    schedule = compile_schedule(pack, actor_ids=ACTORS, seed=711)
    forecast = schedule.forecast_rows[0]
    primary = schedule.primary_rows[0]
    probe = schedule.probe_rows[0]

    assert forecast.request_payload == pack.episodes[0].forecast_payload
    assert primary.request_payload == {
        "shared_body": "Choose the most responsible next action.",
        "cue_surface": primary.request_payload["cue_surface"],
        "semantic_response_tokens": ["answer", "reason"],
    }
    assert set(probe.request_payload) == {"question", "primary_logical_call_id"}
    assert probe.request_payload["primary_logical_call_id"] == primary.logical_call_id
    serialized_payloads = json.dumps(
        [row.request_payload for row in schedule.logical_calls], sort_keys=True
    ).lower()
    for forbidden in ("actor_id", "model", "role", "private", "expected", "gold"):
        assert f'"{forbidden}"' not in serialized_payloads
    assert "cue\"" not in serialized_payloads

    pack.episodes[0].forecast_payload["question"] = "changed-source"
    pack.episodes[0].probe_payload["question"] = "changed-source"
    pack.episodes[0].variants[0].decoding["temperature"] = 1
    assert forecast.request_payload["question"] == "forecast-0"
    assert probe.request_payload["question"] == "probe-0"

    another_primary = next(
        row
        for row in schedule.primary_rows
        if row.logical_call_id != primary.logical_call_id
    )
    primary.request_payload["semantic_response_tokens"].append("mutated")
    assert another_primary.request_payload["semantic_response_tokens"] == ["answer", "reason"]


@pytest.mark.parametrize(
    ("pack", "actors", "seed"),
    [
        (object(), ACTORS, 711),
        (_pack(), ["A", "B", "C", "D"], 711),
        (_pack(), ("A", "B", "C"), 711),
        (_pack(), ("A", "B", "C", "C"), 711),
        (_pack(), ("A", "B", "C", " "), 711),
        (_pack(), ("A", "B", "C", 4), 711),
        (_pack(), ACTORS, True),
        (_pack(), ACTORS, 1.0),
        (replace(_pack(), module="unknown"), ACTORS, 711),
        (replace(_pack(), episodes=list(_pack().episodes)), ACTORS, 711),
        (replace(_pack(), episodes=_pack().episodes[:11]), ACTORS, 711),
    ],
)
def test_compile_rejects_invalid_top_level_inputs(pack, actors, seed) -> None:
    with pytest.raises((TypeError, ValueError)):
        compile_schedule(pack, actor_ids=actors, seed=seed)


def test_compile_requires_unique_episode_ids_and_exact_role_counts() -> None:
    pack = _pack()
    duplicate = _with_episode(
        pack, 1, replace(pack.episodes[1], episode_id=pack.episodes[0].episode_id)
    )
    wrong_roles = _with_episode(pack, 0, replace(pack.episodes[0], role="null"))
    blank_id = _with_episode(pack, 0, replace(pack.episodes[0], episode_id=" "))

    for invalid in (duplicate, wrong_roles, blank_id):
        with pytest.raises(ValueError):
            compile_schedule(invalid, actor_ids=ACTORS, seed=711)


@pytest.mark.parametrize(
    "variants",
    [
        (_variant("C0"), _variant("C1")),
        (_variant("C0"), _variant("C1"), _variant("C1")),
        (_variant("C0"), _variant("C1"), _variant("C2"), _variant("C2")),
        [_variant("C0"), _variant("C1"), _variant("C2")],
    ],
)
def test_compile_requires_exact_variant_tuple(variants) -> None:
    pack = _pack()
    invalid = _with_episode(pack, 0, replace(pack.episodes[0], variants=variants))
    with pytest.raises((TypeError, ValueError)):
        compile_schedule(invalid, actor_ids=ACTORS, seed=711)


@pytest.mark.parametrize(
    "changed",
    [
        {"shared_body": "different"},
        {"task_semantics_sha256": "e" * 64},
        {"answer_semantics_sha256": "A" * 64},
        {"tool_schema_sha256": "f" * 63},
        {"response_schema_sha256": "not-a-hash"},
        {"decoding": {"temperature": 1, "max_tokens": 64}},
        {"semantic_response_tokens": ("reason", "answer")},
        {"semantic_response_tokens": ()},
        {"semantic_response_tokens": ("answer", "")},
        {"cue_surface": ""},
        {"cue_surface": "plain"},
    ],
)
def test_compile_enforces_cue_invariants(changed) -> None:
    pack = _pack()
    invalid = _with_variant(pack, 0, 1, replace(pack.episodes[0].variants[1], **changed))
    with pytest.raises(ValueError):
        compile_schedule(invalid, actor_ids=ACTORS, seed=711)


def test_compile_keeps_internal_cue_labels_out_of_cue_surfaces() -> None:
    pack = _pack()
    exposed = replace(pack.episodes[0].variants[1], cue_surface="treatment C1")

    with pytest.raises(ValueError):
        compile_schedule(
            _with_variant(pack, 0, 1, exposed), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "field_name,value",
    [
        ("forecast_payload", {"nested": ["literal-C3-value"]}),
        ("forecast_payload", {"C3": "reserved key"}),
        ("probe_payload", {"nested": {"field_c3": True}}),
        ("probe_payload", {"expected_label": "yes"}),
        ("probe_payload", {"gold": "yes"}),
        ("forecast_payload", {"private_gold": "yes"}),
        ("probe_payload", {"actor_id": "opaque-no"}),
        ("probe_payload", {"model_name": "opaque-no"}),
        ("probe_payload", {"tested_model": "opaque-no"}),
    ],
)
def test_compile_rejects_reserved_or_private_payload_fields(field_name, value) -> None:
    pack = _pack()
    episode = replace(pack.episodes[0], **{field_name: value})
    with pytest.raises(ValueError):
        compile_schedule(_with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711)


def test_compile_rejects_an_added_c3_field_anywhere_in_pack() -> None:
    pack = _pack()
    object.__setattr__(pack.episodes[0], "c3", {"otherwise": "innocent"})

    with pytest.raises(ValueError):
        compile_schedule(pack, actor_ids=ACTORS, seed=711)


@pytest.mark.parametrize(
    "payload",
    [
        {1: "non-string key"},
        {"bad": float("nan")},
        {"bad": ("tuple",)},
        {"bad": object()},
        {"bad": "\ud800"},
    ],
)
def test_compile_rejects_noncanonical_payloads(payload) -> None:
    pack = _pack()
    episode = replace(pack.episodes[0], forecast_payload=payload)
    with pytest.raises(ValueError):
        compile_schedule(_with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711)


def test_compile_rejects_cyclic_json_payloads() -> None:
    cyclic = []
    cyclic.append(cyclic)
    pack = _pack()
    episode = replace(pack.episodes[0], probe_payload={"cycle": cyclic})
    with pytest.raises(ValueError):
        compile_schedule(_with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711)


@pytest.mark.parametrize(
    "mutation",
    [
        "forecast_private",
        "primary_sensitive_value",
        "probe_private",
        "forecast_later_scope",
    ],
)
def test_scheduled_actor_payloads_are_revalidated_even_when_all_actors_match(
    mutation: str,
) -> None:
    schedule = _schedule()
    episode_id = schedule.bundles[0].episode_id
    calls = list(schedule.logical_calls)
    for index, row in enumerate(calls):
        if row.episode_id != episode_id:
            continue
        payload = json.loads(json.dumps(row.request_payload))
        if mutation == "forecast_private" and row.call_kind == "forecast":
            payload["nested"] = {"private": "leak"}
        elif mutation == "primary_sensitive_value" and row.call_kind == "primary":
            payload["shared_body"] = "model_identity"
        elif mutation == "probe_private" and row.call_kind == "probe":
            payload["nested"] = {"private": "leak"}
        elif mutation == "forecast_later_scope" and row.call_kind == "forecast":
            payload["nested"] = {"lens_call_id": "opaque"}
        else:
            continue
        calls[index] = replace(row, request_payload=payload)

    invalid = _schedule_with_calls(schedule, calls)
    with pytest.raises(ValueError):
        invalid.assert_counterbalanced()
    with pytest.raises(ValueError):
        invalid.to_canonical_json()


@pytest.mark.parametrize(
    "mutation",
    [
        "all_primary_bodies",
        "cue_surface_mapping",
        "all_primary_tokens",
        "forecast_semantics",
        "probe_semantics",
    ],
)
def test_assert_counterbalanced_rejects_cross_actor_semantic_changes(
    mutation: str,
) -> None:
    schedule = _schedule()
    calls = list(schedule.logical_calls)
    bundle = schedule.bundles[0]
    bundle_indices = [
        index for index, row in enumerate(calls) if row.bundle_id == bundle.bundle_id
    ]
    if mutation == "all_primary_bodies":
        for index in bundle_indices[1::2]:
            payload = json.loads(json.dumps(calls[index].request_payload))
            payload["shared_body"] = "Choose an actor-specific alternative action."
            calls[index] = replace(calls[index], request_payload=payload)
    elif mutation == "cue_surface_mapping":
        first, second = bundle_indices[1], bundle_indices[3]
        first_payload = json.loads(json.dumps(calls[first].request_payload))
        second_payload = json.loads(json.dumps(calls[second].request_payload))
        first_payload["cue_surface"], second_payload["cue_surface"] = (
            second_payload["cue_surface"],
            first_payload["cue_surface"],
        )
        calls[first] = replace(calls[first], request_payload=first_payload)
        calls[second] = replace(calls[second], request_payload=second_payload)
    elif mutation == "all_primary_tokens":
        for index in bundle_indices[1::2]:
            payload = json.loads(json.dumps(calls[index].request_payload))
            payload["semantic_response_tokens"] = ["answer", "basis"]
            calls[index] = replace(calls[index], request_payload=payload)
    elif mutation == "forecast_semantics":
        index = bundle_indices[0]
        payload = json.loads(json.dumps(calls[index].request_payload))
        payload["question"] = "alternate forecast question"
        calls[index] = replace(calls[index], request_payload=payload)
    elif mutation == "probe_semantics":
        index = bundle_indices[2]
        payload = json.loads(json.dumps(calls[index].request_payload))
        payload["question"] = "alternate probe question"
        calls[index] = replace(calls[index], request_payload=payload)

    with pytest.raises(ValueError):
        _schedule_with_calls(schedule, calls).assert_counterbalanced()


@pytest.mark.parametrize(
    "mutation",
    [
        "drop_bundle",
        "reorder_bundles",
        "drop_call",
        "reorder_calls",
        "bad_bundle_id",
        "bad_call_id",
        "bad_kind",
        "bad_cue",
        "bad_position",
        "bad_payload",
        "bad_probe_reference",
        "c3_payload",
        "payload_alias",
        "bad_bundle_call_order",
    ],
)
def test_assert_counterbalanced_rejects_mutated_schedules(mutation: str) -> None:
    schedule = _schedule()
    bundles = list(schedule.bundles)
    calls = list(schedule.logical_calls)
    if mutation == "drop_bundle":
        bundles.pop()
    elif mutation == "reorder_bundles":
        bundles[0], bundles[1] = bundles[1], bundles[0]
    elif mutation == "drop_call":
        calls.pop()
    elif mutation == "reorder_calls":
        calls[1], calls[2] = calls[2], calls[1]
    elif mutation == "bad_bundle_id":
        bundles[0] = replace(bundles[0], bundle_id="0" * 16)
    elif mutation == "bad_call_id":
        calls[0] = replace(calls[0], logical_call_id="0" * 16)
    elif mutation == "bad_kind":
        calls[0] = replace(calls[0], call_kind="primary")
    elif mutation == "bad_cue":
        calls[1] = replace(calls[1], cue="C2" if calls[1].cue != "C2" else "C1")
    elif mutation == "bad_position":
        calls[1] = replace(calls[1], presentation_position=2)
    elif mutation == "bad_payload":
        calls[1] = replace(calls[1], request_payload={"shared_body": "leak"})
    elif mutation == "bad_probe_reference":
        changed = dict(calls[2].request_payload)
        changed["primary_logical_call_id"] = "0" * 16
        calls[2] = replace(calls[2], request_payload=changed)
    elif mutation == "c3_payload":
        calls[0] = replace(calls[0], request_payload={"reserved": "C3"})
    elif mutation == "payload_alias":
        calls[7] = replace(calls[7], request_payload=calls[0].request_payload)
    elif mutation == "bad_bundle_call_order":
        identifiers = list(bundles[0].logical_call_ids)
        identifiers[1], identifiers[2] = identifiers[2], identifiers[1]
        bundles[0] = replace(
            bundles[0], logical_call_ids=tuple(identifiers)
        )

    invalid = Schedule(
        seed=schedule.seed,
        bundles=tuple(bundles),
        logical_calls=tuple(calls),
    )
    with pytest.raises(ValueError):
        invalid.assert_counterbalanced()


def test_canonical_json_has_only_public_schedule_structure() -> None:
    schedule = _schedule()
    encoded = schedule.to_canonical_json()
    parsed = json.loads(encoded)

    assert encoded.encode("utf-8").decode("utf-8") == encoded
    assert list(parsed) == ["bundles", "logical_calls", "seed"]
    assert parsed["seed"] == 711
    assert len(parsed["bundles"]) == 48
    assert len(parsed["logical_calls"]) == 336
    assert "physical" not in encoded.lower()
    assert "attempt" not in encoded.lower()
    assert "C3" not in encoded
