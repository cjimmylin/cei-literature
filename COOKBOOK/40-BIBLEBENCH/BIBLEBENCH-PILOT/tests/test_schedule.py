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
_FULLWIDTH_HEX = str.maketrans(
    "0123456789abcdef", "０１２３４５６７８９ａｂｃｄｅｆ"
)


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


def _binary_alias_dag(levels: int):
    shared = {"value": "ordinary"}
    for _ in range(levels):
        shared = [shared, shared]
    return shared


def _assert_no_mutable_aliases(value) -> None:
    seen = set()
    stack = [value]
    while stack:
        current = stack.pop()
        if type(current) not in {dict, list}:
            continue
        identifier = id(current)
        if identifier in seen:
            raise AssertionError("canonical JSON received a mutable alias")
        seen.add(identifier)
        children = current.values() if type(current) is dict else current
        stack.extend(children)


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


@pytest.mark.parametrize(
    ("location", "reserved"),
    [
        ("forecast_key", "Ｃ３"),
        ("forecast_value", "conditionＣ３Surface"),
        ("probe_key", "ordinary_𝐂𝟙_payload"),
        ("probe_value", "visible 𝕮𝟤 label"),
        ("primary_surface", "internal Ｃ０"),
        ("primary_body", "condition𝑪𝟙Surface"),
    ],
)
def test_compatibility_condition_labels_are_rejected_across_visible_calls(
    location: str, reserved: str
) -> None:
    pack = _pack()
    episode = pack.episodes[0]
    if location == "forecast_key":
        episode = replace(episode, forecast_payload={reserved: "ordinary"})
    elif location == "forecast_value":
        episode = replace(
            episode, forecast_payload={"ordinary_note": reserved}
        )
    elif location == "probe_key":
        episode = replace(
            episode, probe_payload={"nested": [{reserved: "ordinary"}]}
        )
    elif location == "probe_value":
        episode = replace(
            episode, probe_payload={"nested": [{"ordinary": reserved}]}
        )
    elif location == "primary_surface":
        variants = tuple(
            replace(variant, cue_surface=reserved)
            if variant.cue == "C1"
            else variant
            for variant in episode.variants
        )
        episode = replace(episode, variants=variants)
    else:
        episode = replace(
            episode,
            variants=tuple(
                replace(variant, shared_body=reserved)
                for variant in episode.variants
            ),
        )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_compatibility_equivalent_cue_surfaces_are_not_distinct() -> None:
    pack = _pack()
    variant = replace(pack.episodes[0].variants[1], cue_surface="ｐｌａｉｎ")

    with pytest.raises(ValueError, match="distinct"):
        compile_schedule(
            _with_variant(pack, 0, 1, variant), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    ("field_name", "protected_key"),
    [
        ("forecast_payload", "𝐚ctor𝑀odel"),
        ("forecast_payload", "ｍｏｄｅｌ_id"),
        ("forecast_payload", "ｐｒｏｖｉｄｅｒ_id"),
        ("probe_payload", "𝓁ens-id"),
        ("probe_payload", "roℓeLabel"),
        ("probe_payload", "expecᵗed.label"),
        ("probe_payload", "𝓅rivate_ﬁeld"),
        ("probe_payload", "𝓈cheduleId"),
    ],
)
def test_compatibility_policy_keys_are_rejected_recursively(
    field_name: str, protected_key: str
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        **{field_name: {"outer": [{protected_key: "opaque"}]}},
    )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_compatibility_schedule_reference_keys_remain_reserved(
    field_name: str,
) -> None:
    pack = _pack()
    reserved_key = "ｐｒｉｍａｒｙ＿ｌｏｇｉｃａｌ＿ｃａｌｌ＿ｉｄ"
    episode = replace(
        pack.episodes[0],
        **{field_name: {reserved_key: "opaque"}},
    )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
@pytest.mark.parametrize(
    "reserved_key",
    [
        "logical_call_id",
        "logicalCallId",
        "logical-call-id",
        "primaryLogicalCallId",
        "sourcePrimaryLogicalCallIdCopy",
        "logical_calls_id",
        "logicalCallsId",
        "logical-calls-id",
        "logical calls id",
        "primary_logical_calls_id",
        "primaryLogicalCallsIdentifier",
        "nestedPrimaryLogicalCallsIdsCopy",
        "ｐｒｉｍａｒｙ＿ｌｏｇｉｃａｌ＿ｃａｌｌｓ＿ｉｄｅｎｔｉｆｉｅｒ",
        "primary logical call id",
        "ｐｒｉｍａｒｙ＿ｌｏｇｉｃａｌ＿ｃａｌｌ＿ｉｄ",
    ],
)
def test_authored_logical_call_reference_keys_are_rejected_recursively(
    field_name: str, reserved_key: str
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        **{field_name: {"outer": [{reserved_key: "opaque"}]}},
    )

    with pytest.raises(ValueError, match="logical call reference"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "benign_key",
    ["logical_reasoning", "callback_id", "calligraphy_notes"],
)
def test_benign_call_words_remain_allowed_in_authored_payloads(
    benign_key: str,
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        forecast_payload={"outer": [{benign_key: "ordinary"}]},
        probe_payload={"outer": [{benign_key: "ordinary"}]},
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload["outer"] == [
        {benign_key: "ordinary"}
    ]
    assert schedule.probe_rows[0].request_payload["outer"] == [
        {benign_key: "ordinary"}
    ]


@pytest.mark.parametrize(
    "reference_label",
    [
        "primary_logical_call_id",
        "logicalCallId",
        "logical-calls-identifier",
        "primary logical calls ids",
        "ｐｒｉｍａｒｙ＿ｌｏｇｉｃａｌ＿ｃａｌｌ＿ｉｄ",
    ],
)
@pytest.mark.parametrize(
    "location", ["forecast", "probe", "primary_body", "primary_token"]
)
def test_explicit_logical_call_reference_values_are_rejected_recursively(
    reference_label: str, location: str
) -> None:
    pack = _pack()
    episode = pack.episodes[0]
    if location == "forecast":
        episode = replace(
            episode,
            forecast_payload={"outer": [{"note": reference_label}]},
        )
    elif location == "probe":
        episode = replace(
            episode,
            probe_payload={"outer": [{"note": reference_label}]},
        )
    elif location == "primary_body":
        episode = replace(
            episode,
            variants=tuple(
                replace(variant, shared_body=reference_label)
                for variant in episode.variants
            ),
        )
    else:
        episode = replace(
            episode,
            variants=tuple(
                replace(
                    variant,
                    semantic_response_tokens=(reference_label,),
                )
                for variant in episode.variants
            ),
        )

    with pytest.raises(ValueError, match="logical call reference"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "benign_text", ["the argument is logical", "call support"]
)
def test_benign_logical_and_call_prose_remains_allowed(
    benign_text: str,
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        forecast_payload={"note": benign_text},
        probe_payload={"note": benign_text},
        variants=tuple(
            replace(variant, shared_body=benign_text)
            for variant in pack.episodes[0].variants
        ),
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload["note"] == benign_text
    assert schedule.probe_rows[0].request_payload["note"] == benign_text
    assert schedule.primary_rows[0].request_payload["shared_body"] == benign_text


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
@pytest.mark.parametrize("mixed_key", ["mοdel", "actοr_id"])
def test_mixed_script_identifier_keys_are_rejected_generically(
    field_name: str, mixed_key: str
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        **{field_name: {"outer": [{mixed_key: "ordinary"}]}},
    )

    with pytest.raises(ValueError, match="mixed-script identifier key"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_script_aware_key_tokens_preserve_latin_and_separated_scripts() -> None:
    pack = _pack()
    payload = {
        "café": "ordinary",
        "résumé2": "ordinary",
        "第1章": "ordinary",
        "質問_v2": "ordinary",
    }
    episode = replace(
        pack.episodes[0],
        forecast_payload=payload,
        probe_payload=payload,
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload == payload
    assert schedule.probe_rows[0].request_payload == payload


@pytest.mark.parametrize("confusable_label", ["С3", "Ϲ2", "с0", "ϲ1"])
@pytest.mark.parametrize("location", ["forecast", "probe", "primary"])
def test_high_risk_cue_label_homoglyphs_are_rejected(
    confusable_label: str, location: str
) -> None:
    pack = _pack()
    episode = pack.episodes[0]
    if location == "forecast":
        episode = replace(
            episode, forecast_payload={"note": confusable_label}
        )
    elif location == "probe":
        episode = replace(
            episode, probe_payload={"note": confusable_label}
        )
    else:
        episode = replace(
            episode,
            variants=tuple(
                replace(variant, shared_body=confusable_label)
                for variant in episode.variants
            ),
        )

    with pytest.raises(ValueError, match="reserved condition label"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "homoglyph",
    [
        "ᴄ",
        "Ꮯ",
        "ꮯ",
        "Ƈ",
        "ƈ",
        "ꓚ",
        "Ⲥ",
        "ⲥ",
        "Ꞓ",
        "ꞓ",
        "Ȼ",
        "ȼ",
    ],
)
@pytest.mark.parametrize(
    "location",
    [
        "forecast_value",
        "forecast_key",
        "probe_nested_value",
        "probe_nested_key",
        "primary_body",
        "primary_token",
    ],
)
def test_extended_cue_homoglyph_labels_are_rejected_across_visible_contexts(
    homoglyph: str, location: str
) -> None:
    pack = _pack()
    episode = pack.episodes[0]
    exposed = f"{homoglyph}2"
    if location == "forecast_value":
        episode = replace(episode, forecast_payload={"note": exposed})
    elif location == "forecast_key":
        episode = replace(episode, forecast_payload={exposed: "ordinary"})
    elif location == "probe_nested_value":
        episode = replace(
            episode,
            probe_payload={"outer": [{"note": exposed}]},
        )
    elif location == "probe_nested_key":
        episode = replace(
            episode,
            probe_payload={"outer": [{exposed: "ordinary"}]},
        )
    elif location == "primary_body":
        episode = replace(
            episode,
            variants=tuple(
                replace(variant, shared_body=exposed)
                for variant in episode.variants
            ),
        )
    else:
        episode = replace(
            episode,
            variants=tuple(
                replace(
                    variant,
                    semantic_response_tokens=(exposed,),
                )
                for variant in episode.variants
            ),
        )

    with pytest.raises(ValueError, match="reserved condition label"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "homoglyph",
    [
        "ᴄ",
        "Ꮯ",
        "ꮯ",
        "Ƈ",
        "ƈ",
        "ꓚ",
        "Ⲥ",
        "ⲥ",
        "Ꞓ",
        "ꞓ",
        "Ȼ",
        "ȼ",
    ],
)
def test_extended_cue_homoglyphs_remain_ordinary_without_adjacent_cue_digit(
    homoglyph: str,
) -> None:
    pack = _pack()
    forecast_payload = {homoglyph: f"marker {homoglyph}4"}
    probe_payload = {"note": f"marker {homoglyph} before chapter 3"}
    body = f"Explain the international marker {homoglyph} in chapter 3."
    episode = replace(
        pack.episodes[0],
        forecast_payload=forecast_payload,
        probe_payload=probe_payload,
        variants=tuple(
            replace(variant, shared_body=body)
            for variant in pack.episodes[0].variants
        ),
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload == forecast_payload
    assert schedule.probe_rows[0].request_payload == probe_payload
    assert schedule.primary_rows[0].request_payload["shared_body"] == body


@pytest.mark.parametrize(
    "disguised_label",
    [
        "Ç3",
        "ç3",
        "Ć3",
        "ć3",
        "C\u03273",
        "C\u200d3",
        "C\u200c3",
        "C\ufe0f3",
        "C\u00ad3",
        "C-3",
        "C 3",
        "C_3",
        "C/3",
        "C.3",
        "C\t3",
        "C\n3",
        "C—3",
        "C--3",
        "C  3",
        "C+3",
        "C=3",
        "C→3",
        "C✅3",
        "C£3",
        "C^3",
        "CЗ",
        "cз",
        "СЗ",
        "сз",
        "CƷ",
        "cʒ",
        "CƐ",
        "cɛ",
        "CȜ",
        "Cȝ",
        "C٣",
        "C३",
        "C³",
    ],
)
@pytest.mark.parametrize(
    "location",
    [
        "forecast_value",
        "forecast_key",
        "probe_nested_value",
        "probe_nested_key",
        "primary_body",
    ],
)
def test_combining_ignorable_and_separator_cue_labels_are_rejected(
    disguised_label: str, location: str
) -> None:
    pack = _pack()
    episode = pack.episodes[0]
    if location == "forecast_value":
        episode = replace(
            episode, forecast_payload={"note": disguised_label}
        )
    elif location == "forecast_key":
        episode = replace(
            episode, forecast_payload={disguised_label: "ordinary"}
        )
    elif location == "probe_nested_value":
        episode = replace(
            episode,
            probe_payload={"outer": [{"note": disguised_label}]},
        )
    elif location == "probe_nested_key":
        episode = replace(
            episode,
            probe_payload={"outer": [{disguised_label: "ordinary"}]},
        )
    else:
        episode = replace(
            episode,
            variants=tuple(
                replace(variant, shared_body=disguised_label)
                for variant in episode.variants
            ),
        )

    with pytest.raises(ValueError, match="reserved condition label"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "benign_text",
    [
        "façade 3",
        "Ćiril 3",
        "Café 3",
        "C-4",
        "C 4",
        "第3章",
        "word\u200d 3",
        "Budget £5 + tax remains visible ✅",
        "x → y; the modifier ˄ is documented.",
        "Use model+craft and provider+care as ordinary compounds.",
    ],
)
def test_diacritic_and_international_nonlabels_preserve_exact_bytes(
    benign_text: str,
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        forecast_payload={"note": benign_text},
        probe_payload={"note": benign_text},
        variants=tuple(
            replace(variant, shared_body=benign_text)
            for variant in pack.episodes[0].variants
        ),
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload["note"] == benign_text
    assert schedule.probe_rows[0].request_payload["note"] == benign_text
    assert schedule.primary_rows[0].request_payload["shared_body"] == benign_text


@pytest.mark.parametrize(
    ("ascii_value", "unicode_value", "expected"),
    [
        ("C_3", "Ｃ—٣", "C3"),
        ("C\t3", "С\u200dЗ", "C3"),
        ("C+3", "Ｃ→٣", "C3"),
        ("C$3", "Ｃ£٣", "C3"),
        ("C^3", "Ｃ˄٣", "C3"),
        ("C*3", "Ｃ✅٣", "C3"),
    ],
)
def test_label_policy_ascii_fast_path_matches_unicode_skeleton(
    ascii_value: str, unicode_value: str, expected: str
) -> None:
    assert schedule_module._label_policy_text(ascii_value) == expected
    assert schedule_module._label_policy_text(unicode_value) == expected


@pytest.mark.parametrize(
    ("ascii_value", "unicode_value", "expected"),
    [
        ("ab-c d\t\x00e", "ａｂ—ｃ　ｄ\u200dｅ", "abcde"),
        ("6e779c794025e210", "6ε779ϲ794025ε210", "6e779c794025e210"),
        ("ab+cd=ef", "ａｂ→ｃｄ✅ｅｆ", "abcdef"),
        ("ab$cd^ef", "ａｂ£ｃｄ˄ｅｆ", "abcdef"),
    ],
)
def test_generated_id_comparison_fast_path_matches_unicode_skeleton(
    ascii_value: str, unicode_value: str, expected: str
) -> None:
    assert schedule_module._comparison_skeleton(ascii_value) == expected
    assert schedule_module._comparison_skeleton(unicode_value) == expected


def test_international_prose_with_numbers_remains_allowed() -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        forecast_payload={"説明": "第3章の説明"},
        probe_payload={"追跡質問": "Слово 3 и μοντέλο 2"},
        variants=tuple(
            replace(variant, shared_body="第3章を説明してください")
            for variant in pack.episodes[0].variants
        ),
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload == {
        "説明": "第3章の説明"
    }
    assert schedule.probe_rows[0].request_payload == {
        "追跡質問": "Слово 3 и μοντέλο 2"
    }


@pytest.mark.parametrize(
    "sensitive_assignment",
    [
        "The expected label is target",
        "The tested model: GPT-X",
        "testedModel=GPT-X",
        "The actor id is A",
        "model_identity is hidden-model",
    ],
)
@pytest.mark.parametrize("location", ["forecast", "probe", "primary"])
def test_explicit_sensitive_assignments_are_rejected_in_visible_strings(
    sensitive_assignment: str, location: str
) -> None:
    pack = _pack()
    episode = pack.episodes[0]
    if location == "forecast":
        episode = replace(
            episode, forecast_payload={"note": sensitive_assignment}
        )
    elif location == "probe":
        episode = replace(
            episode, probe_payload={"note": sensitive_assignment}
        )
    else:
        episode = replace(
            episode,
            variants=tuple(
                replace(variant, shared_body=sensitive_assignment)
                for variant in episode.variants
            ),
        )

    with pytest.raises(ValueError, match="sensitive assignment"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "sensitive_assignment",
    [
        "The provider is OpenRouter",
        "gold label: target",
        "groundTruth=target",
        "The condition is treatment",
        "cue: scriptural",
        "actor role=target",
        "schedule id is hidden-schedule",
        "bundleId is hidden-bundle",
        "episode id: hidden-episode",
        "private id=hidden-private",
        "The prοvider is OpenRouter",
        "gοld label: target",
        "cοndition is treatment",
        "actοr role=target",
        "The prоvider is OpenRouter",
        "gоld label: target",
        "cоndition is treatment",
        "actоr role=target",
        "ϲondition is treatment",
        "Ϲue: scriptural",
        "expected\u200d label: target",
        "model\u200d identity: hidden-model",
        "gοld—label: target",
        "prοvider\u200d: OpenRouter",
        "provider\u2060assigned OpenRouter",
        "provider\u200dis OpenAI",
        "provider\u0301is openrouter",
        "selected provider is openrouter",
        "current provider: OpenAI",
        "requested provider assigned OpenRouter",
        "chosen provider=OpenAI",
        "the chosen provider is openrouter",
        "A provider is openai",
        "The healthcare provider is OpenAI",
        "The provider is undisclosed",
        "provider+is+OpenRouter",
        "model+identity+is+GPT-X",
        "condition+is+treatment",
        "gold+label+is+target",
        "The provider is useful+OpenRouter",
        "provider£is£OpenRouter",
        "model^identity^is^GPT-X",
        "condition→is→treatment",
        "gold✅label✅is✅target",
    ],
)
@pytest.mark.parametrize("location", ["forecast", "probe", "primary"])
def test_registered_metadata_assignments_are_rejected_in_all_call_payloads(
    sensitive_assignment: str, location: str
) -> None:
    pack = _pack()
    episode = pack.episodes[0]
    if location == "forecast":
        episode = replace(
            episode, forecast_payload={"note": sensitive_assignment}
        )
    elif location == "probe":
        episode = replace(
            episode, probe_payload={"note": sensitive_assignment}
        )
    else:
        episode = replace(
            episode,
            variants=tuple(
                replace(variant, shared_body=sensitive_assignment)
                for variant in episode.variants
            ),
        )

    with pytest.raises(ValueError, match="sensitive assignment"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "benign_text",
    [
        "The expected outcome is uncertain",
        "This model is useful",
        "The actor is responsible",
        "gold is a color",
        "the condition is stable",
        "A provider is useful",
        "A healthcare provider is available today",
        "A pastoral care provider is compassionate",
        "The healthcare provider is available today",
        "The provider is useful",
        "The provider is compassionate",
        "The provider is available today",
        "The chosen provider is available today",
    ],
)
def test_benign_assignment_like_prose_remains_allowed(benign_text: str) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        forecast_payload={"note": benign_text},
        probe_payload={"note": benign_text},
        variants=tuple(
            replace(variant, shared_body=benign_text)
            for variant in pack.episodes[0].variants
        ),
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload["note"] == benign_text
    assert schedule.probe_rows[0].request_payload["note"] == benign_text
    assert schedule.primary_rows[0].request_payload["shared_body"] == benign_text


@pytest.mark.parametrize(
    "confusable_c",
    [
        "С",
        "с",
        "Ϲ",
        "ϲ",
        "ᴄ",
        "Ꮯ",
        "ꮯ",
        "Ƈ",
        "ƈ",
        "ꓚ",
        "Ⲥ",
        "ⲥ",
        "Ꞓ",
        "ꞓ",
        "Ȼ",
        "ȼ",
    ],
)
def test_sensitive_policy_maps_all_registered_c_confusables(
    confusable_c: str,
) -> None:
    authored = f"{confusable_c}ondition is treatment"

    assert (
        schedule_module._protected_word_policy_text(authored)
        == "condition is treatment"
    )


@pytest.mark.parametrize(
    "mixed_language_text",
    ["The οcean is calm", "Смешанный οтвет полезен"],
)
def test_non_sensitive_mixed_language_prose_preserves_authored_bytes(
    mixed_language_text: str,
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        forecast_payload={"note": mixed_language_text},
        probe_payload={"note": mixed_language_text},
        variants=tuple(
            replace(variant, shared_body=mixed_language_text)
            for variant in pack.episodes[0].variants
        ),
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload["note"] == mixed_language_text
    assert schedule.probe_rows[0].request_payload["note"] == mixed_language_text
    assert (
        schedule.primary_rows[0].request_payload["shared_body"]
        == mixed_language_text
    )


@pytest.mark.parametrize(
    ("ascii_assignment", "unicode_assignment"),
    [
        (
            "provider assigned OpenRouter",
            "provider\u2060assigned OpenRouter",
        ),
        ("provider is OpenAI", "provider\u200dis OpenAI"),
        ("provider is openrouter", "provider\u0301is openrouter"),
    ],
)
def test_provider_identity_fast_path_matches_invisible_boundaries(
    ascii_assignment: str, unicode_assignment: str
) -> None:
    pack = _pack()
    for assignment in (ascii_assignment, unicode_assignment):
        episode = replace(
            pack.episodes[0], forecast_payload={"note": assignment}
        )

        with pytest.raises(ValueError, match="sensitive assignment") as error:
            compile_schedule(
                _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
            )
        assert "OpenRouter" not in str(error.value)
        assert "OpenAI" not in str(error.value)
        assert "openrouter" not in str(error.value)


@pytest.mark.parametrize(
    ("ascii_value", "unicode_value", "expected"),
    [
        (
            "model+identity+is+GPT-X",
            "ｍｏｄｅｌ→ｉｄｅｎｔｉｔｙ✅ｉｓ£ＧＰＴ－Ｘ",
            "model identity is gpt x",
        ),
        (
            "condition^is^treatment",
            "ｃｏｎｄｉｔｉｏｎ˄ｉｓ˄ｔｒｅａｔｍｅｎｔ",
            "condition is treatment",
        ),
        (
            "provider=OpenRouter",
            "ｐｒｏｖｉｄｅｒ＝ＯｐｅｎＲｏｕｔｅｒ",
            "provider assigned open router",
        ),
    ],
)
def test_protected_phrase_fast_path_matches_symbol_reference_skeleton(
    ascii_value: str, unicode_value: str, expected: str
) -> None:
    assert schedule_module._protected_word_policy_text(ascii_value) == expected
    assert schedule_module._protected_word_policy_text(unicode_value) == expected


@pytest.mark.parametrize(
    ("location", "protected_value"),
    [
        ("forecast", "ｍｏｄｅｌ_identity"),
        ("probe", "ｐｒｉｖａｔｅ"),
        ("primary_body", "ｅｘｐｅｃｔｅｄ_label"),
        ("primary_token", "𝐚ctor_𝒎odel"),
    ],
)
def test_compatibility_policy_values_are_rejected_recursively(
    location: str, protected_value: str
) -> None:
    pack = _pack()
    episode = pack.episodes[0]
    if location == "forecast":
        episode = replace(
            episode,
            forecast_payload={"outer": [{"ordinary": protected_value}]},
        )
    elif location == "probe":
        episode = replace(
            episode,
            probe_payload={"outer": [{"ordinary": protected_value}]},
        )
    elif location == "primary_body":
        episode = replace(
            episode,
            variants=tuple(
                replace(variant, shared_body=protected_value)
                for variant in episode.variants
            ),
        )
    else:
        episode = replace(
            episode,
            variants=tuple(
                replace(
                    variant,
                    semantic_response_tokens=(protected_value,),
                )
                for variant in episode.variants
            ),
        )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    ("field_name", "compatibility_hex"),
    [
        ("request_id", "ｃ３" + "ａ" * 14),
        ("content_sha256", "ｃ２" + "ｂ" * 62),
    ],
)
def test_compatibility_hex_does_not_gain_an_opaque_label_exemption(
    field_name: str, compatibility_hex: str
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0],
        forecast_payload={field_name: compatibility_hex},
    )

    with pytest.raises(ValueError, match="reserved condition label"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_compatibility_hash_glyphs_are_not_accepted_as_ascii_sha256() -> None:
    pack = _pack()
    variants = tuple(
        replace(variant, task_semantics_sha256="ｃ３" + "ａ" * 62)
        for variant in pack.episodes[0].variants
    )
    episode = replace(pack.episodes[0], variants=variants)

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_benign_international_unicode_is_preserved_without_policy_rewrite() -> None:
    pack = _pack()
    forecast_payload = {
        "ｑｕｅｓｔｉｏｎ": {
            "説明": "ｈｅｌｌｏ oﬃce — 国際化された説明"
        }
    }
    probe_payload = {
        "追跡質問": ["普通の応答", "μοντέλο", "prívate"]
    }
    body = "最も責任ある次の行動を選んでください。"
    surfaces = {"C0": "일반", "C1": "성서적", "C2": "세속적"}
    tokens = ("回答", "理由")
    episode = replace(
        pack.episodes[0],
        forecast_payload=forecast_payload,
        probe_payload=probe_payload,
        variants=tuple(
            replace(
                variant,
                cue_surface=surfaces[variant.cue],
                shared_body=body,
                semantic_response_tokens=tokens,
            )
            for variant in pack.episodes[0].variants
        ),
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    forecast = next(
        row for row in schedule.forecast_rows if row.episode_id == episode.episode_id
    )
    probe = next(
        row for row in schedule.probe_rows if row.episode_id == episode.episode_id
    )
    primary = next(
        row for row in schedule.primary_rows if row.episode_id == episode.episode_id
    )
    assert forecast.request_payload == forecast_payload
    assert {
        key: value
        for key, value in probe.request_payload.items()
        if key != "primary_logical_call_id"
    } == probe_payload
    assert primary.request_payload["shared_body"] == body
    assert primary.request_payload["cue_surface"] == surfaces[primary.cue]
    assert primary.request_payload["semantic_response_tokens"] == list(tokens)


@pytest.mark.parametrize(
    ("field_name", "payload"),
    [
        ("forecast_payload", {"ordinary": 1, "ｏｒｄｉｎａｒｙ": 2}),
        (
            "probe_payload",
            {"nested": {"safe": "left", "ｓａｆｅ": "right"}},
        ),
    ],
)
def test_compatibility_colliding_policy_keys_are_rejected_recursively(
    field_name: str, payload: dict
) -> None:
    pack = _pack()
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError, match="compatibility-colliding"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_compatibility_policy_view_restores_authored_tree_after_rejection(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured = {
        "ｑｕｅｓｔｉｏｎ": {"ordinary": "ｐｒｉｖａｔｅ"}
    }
    authored = json.loads(json.dumps(captured))

    def rejecting_policy(payload) -> None:
        assert payload == {"question": {"ordinary": "private"}}
        raise ValueError("unsafe model-visible payload")

    monkeypatch.setattr(
        schedule_module, "assert_actor_payload_safe", rejecting_policy
    )

    with pytest.raises(ValueError, match="unsafe model-visible payload"):
        schedule_module._assert_actor_policy_safe(captured)

    assert captured == authored
    assert list(captured) == list(authored)


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
        "registered_lens_id",
        "module_lens_identifier",
        "registered_intervention_id",
        "module_physical_attempt_id",
        "lens_token",
        "lens_version",
        "intervention_token",
        "provider_id",
        "provider_route",
        "requested_provider",
        "route",
        "route_id",
        "route_name",
        "route_config",
        "route_token",
        "route_version",
        "route_description",
        "selected_route",
        "requested_route",
        "returned_route",
        "fallback_route",
        "current_route",
        "active_route",
        "chosen_route",
        "resolved_route",
        "execution_route",
        "backend_route",
        "novelprefix_route",
        "routes",
        "fallback_routes",
        "available_routes",
        "delivery_routes",
        "lenses",
        "evaluation_lenses",
        "interventions",
        "registered_interventions",
        "providers",
        "available_providers",
        "physical_ids",
        "physical_attempts",
        "physical_attempts_ids",
        "attempt_ids",
        "attempt_identifiers",
        "physical_calls",
        "physicalids",
        "physicalattempts",
        "physicalattemptids",
        "attemptids",
        "attemptidentifiers",
        "lensids",
        "interventionids",
        "providerids",
        "routeids",
        "lensesidentifiers",
        "interventionsidentifier",
        "providersids",
        "routesidentifiers",
        "physicalcalls",
        "physicalattemptsidentifiers",
        "attemptsids",
        "lenscall",
        "lensconfig",
        "lensresult",
        "lenstoken",
        "lensversion",
        "lenscallsuffix",
        "interventionconfigsuffix",
        "providerroute",
        "providerrouteextra",
        "providerconfig",
        "providertoken",
        "providerversion",
        "routeconfig",
        "routedescription",
        "fallbackroute",
        "fallbackroutesuffix",
        "physicalcallids",
        "physicalcallsids",
        "physicalattemptcalls",
        "attemptidextra",
        "attemptidentifierresult",
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
            "lensing_notes": "Lensing is an ordinary unrelated word here.",
            "physicality_notes": "Physicality is ordinary prose here.",
            "interventional_notes": "Interventional is an unrelated adjective.",
            "delivery_route": "An ordinary task delivery path.",
            "evacuation_route": "An ordinary task evacuation path.",
            "routing_notes": "Ordinary routing prose.",
            "reroute_notes": "Ordinary reroute prose.",
            "providership_notes": "Providership is unrelated ordinary prose.",
            "attempting_notes": "Attempting is an ordinary word.",
            "identifying_notes": "Identifying is an ordinary word.",
            "caller_notes": "Caller is an ordinary word.",
            "lensingsummary": "Lensing morphology is benign.",
            "interventionalsummary": "Interventional morphology is benign.",
            "providershipsummary": "Providership morphology is benign.",
            "reroutesummary": "Reroute morphology is benign.",
            "goldenrule": "A benign golden rule field.",
            "riskfactor": "A benign risk factor field.",
            "modelingnotes": "Benign modeling notes.",
            "rescuenotes": "Benign rescue notes.",
            "contractorname": "A legitimate contractor name.",
            "tractorid": "A legitimate tractor identifier.",
            "extractornotes": "Legitimate extractor notes.",
            "parolestatus": "A legitimate status field.",
            "marigoldcolor": "A legitimate color field.",
            "goldfishcount": "A legitimate count field.",
            "enroutestatus": "A legitimate status field.",
            "glenscount": "A legitimate count field.",
            "remodelplan": "A legitimate plan field.",
            "rescheduleoptions": "Legitimate scheduling options.",
            "barbecueplan": "A legitimate meal plan.",
            "golden_rule": "An ordinary principle, not a result field.",
            "risk_factor": "An ordinary descriptive factor.",
            "physical_state": "An ordinary state description.",
        },
        probe_payload={
            "golden_rule": "An ordinary principle.",
            "risk_factor": "An ordinary descriptive factor.",
            "physical_state": "An ordinary state description.",
            "interventional_notes": "Interventional is an unrelated adjective.",
            "delivery_route": "An ordinary task delivery path.",
            "evacuation_route": "An ordinary task evacuation path.",
            "routing_notes": "Ordinary routing prose.",
            "reroute_notes": "Ordinary reroute prose.",
            "providership_notes": "Providership is unrelated ordinary prose.",
            "attempting_notes": "Attempting is an ordinary word.",
            "identifying_notes": "Identifying is an ordinary word.",
            "caller_notes": "Caller is an ordinary word.",
            "lensingsummary": "Lensing morphology is benign.",
            "interventionalsummary": "Interventional morphology is benign.",
            "providershipsummary": "Providership morphology is benign.",
            "reroutesummary": "Reroute morphology is benign.",
            "goldenrule": "A benign golden rule field.",
            "golden_rule": "A benign golden rule field.",
            "riskfactor": "A benign risk factor field.",
            "risk_factor": "A benign risk factor field.",
            "modelingnotes": "Benign modeling notes.",
            "rescuenotes": "Benign rescue notes.",
            "contractorname": "A legitimate contractor name.",
            "tractorid": "A legitimate tractor identifier.",
            "extractornotes": "Legitimate extractor notes.",
            "parolestatus": "A legitimate status field.",
            "marigoldcolor": "A legitimate color field.",
            "goldfishcount": "A legitimate count field.",
            "enroutestatus": "A legitimate status field.",
            "glenscount": "A legitimate count field.",
            "remodelplan": "A legitimate plan field.",
        },
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload == episode.forecast_payload


@pytest.mark.parametrize(
    "protected_key",
    [
        "lenssecret",
        "secretlens",
        "providersocket",
        "routeendpoint",
        "physicalidsecret",
        "attemptidsecret",
        "actorsecret",
        "secretactorid",
        "modelsecret",
        "secretmodelid",
        "riskfactorsecret",
        "expectedoutcome",
        "goldscore",
        "rolecode",
        "privateblob",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_rejects_protected_metadata_with_unregistered_affixes(
    protected_key: str, field_name: str
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {protected_key: "opaque"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "protected_key",
    [
        "glensesid",
        "glensessecret",
        "prefixglensesidsuffix",
        "reroutesid",
        "reroutestoken",
        "prefixreroutesidsuffix",
        "enroutesid",
        "enroutestoken",
        "prefixenroutesidsuffix",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_rejects_protected_token_extending_past_benign_context(
    protected_key: str, field_name: str
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {protected_key: "opaque"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "protected_key",
    [
        "cuecode",
        "conditionarm",
        "schedulehash",
        "bundlehash",
        "episodehash",
    ],
)
def test_forecast_rejects_blinded_metadata_with_unregistered_affixes(
    protected_key: str,
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {protected_key: "opaque"}}]}
    episode = replace(pack.episodes[0], forecast_payload=payload)

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "benign_key",
    [
        "lensingnotes",
        "interventionalnotes",
        "providershipnotes",
        "routingnotes",
        "reroutenotes",
        "riskfactor",
        "risk_factor",
        "risk_factors",
        "contractorname",
        "tractorid",
        "extractornotes",
        "role_play",
        "modelingnotes",
        "modelling_notes",
        "remodelplan",
        "rescuenotes",
        "barbecueplan",
        "goldenrule",
        "marigoldcolor",
        "goldfishcount",
        "parolestatus",
        "enroutestatus",
        "glenscount",
        "rescheduleoptions",
        "physicalitynotes",
        "physicalstate",
        "physical_state",
        "attemptingnotes",
        "identifyingnotes",
        "callernotes",
        "deliveryroute",
        "evacuationroute",
        "subcontractorname",
        "farmtractorid",
        "dataextractornotes",
        "kitchenremodelplan",
        "postparolestatus",
        "wildmarigoldcolor",
        "pondgoldfishcount",
        "mountainglenscount",
        "statusenroutestatus",
        "noninterventionalsummary",
        "newprovidershipsummary",
        "cameralensingnotes",
        "againreroutesummary",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_allows_registered_benign_key_families_across_calls(
    benign_key: str, field_name: str
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {benign_key: "ordinary"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    rows = (
        schedule.forecast_rows
        if field_name == "forecast_payload"
        else schedule.probe_rows
    )
    assert rows[0].request_payload["outer"] == payload["outer"]


@pytest.mark.parametrize(
    "benign_key",
    [
        "auditfactor",
        "auditfactors",
        "storybookroleplay",
        "ukmodellingnotes",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_allows_complete_benign_grammars_at_arbitrary_positions(
    benign_key: str, field_name: str
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {benign_key: "ordinary"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    rows = (
        schedule.forecast_rows
        if field_name == "forecast_payload"
        else schedule.probe_rows
    )
    assert rows[0].request_payload["outer"] == payload["outer"]


@pytest.mark.parametrize(
    "protected_key",
    [
        "res_cue_notes",
        "resCueNotes",
        "barbe_cue_plan",
        "re_schedule_options",
        "reScheduleOptions",
        "f_actor",
        "contr_actor_name",
        "re_model_plan",
        "gold_en_rule",
        "mari_gold_color",
        "pa_role_status",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_rejects_reserved_key_components_before_benign_grammar(
    protected_key: str, field_name: str
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {protected_key: "opaque"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("protected_key", ["bundle_id", "episode_id"])
def test_probe_rejects_all_actor_visible_metadata_components(
    protected_key: str,
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], probe_payload={protected_key: "opaque"}
    )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("protected_key", ["user_role_play", "statusRolePlay"])
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_role_component_exception_is_exactly_role_play(
    protected_key: str, field_name: str
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], **{field_name: {protected_key: "opaque"}}
    )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "benign_key",
    [
        "rescue_notes",
        "barbecue_plan",
        "reschedule_options",
        "remodel_plan",
        "golden_rule",
        "marigold_color",
        "parole_status",
        "role_play",
        "rolePlay",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_preserves_registered_noncomponent_grammars(
    benign_key: str, field_name: str
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {benign_key: "ordinary"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    rows = (
        schedule.forecast_rows
        if field_name == "forecast_payload"
        else schedule.probe_rows
    )
    assert rows[0].request_payload["outer"] == payload["outer"]


@pytest.mark.parametrize(
    "protected_key",
    [
        "resCUENotes",
        "reSCHEDULEOptions",
        "contrACTORName",
        "reMODELPlan",
        "mariGOLDColor",
        "paROLEStatus",
        "userROLEPlay",
        "statusROLEPlay",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_rejects_acronym_title_reserved_components(
    protected_key: str, field_name: str
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], **{field_name: {protected_key: "opaque"}}
    )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_preserves_ordinary_acronym_and_hash_keys(
    field_name: str,
) -> None:
    pack = _pack()
    payload = {
        "HTTPStatus": "ordinary",
        "taskSHA256": "c3" + "a" * 62,
    }
    episode = replace(pack.episodes[0], **{field_name: payload})

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    rows = (
        schedule.forecast_rows
        if field_name == "forecast_payload"
        else schedule.probe_rows
    )
    assert rows[0].request_payload["HTTPStatus"] == "ordinary"
    assert rows[0].request_payload["taskSHA256"] == payload["taskSHA256"]


@pytest.mark.parametrize(
    "protected_key",
    [
        "providership_id",
        "reschedule_id",
        "golden_label",
        "lensing_id",
        "contractor_token",
        "tractor_label",
        "extractor_score",
        "roleplay_config",
        "parole_hash",
        "modeling_token",
        "remodel_id",
        "marigold_label",
        "goldfish_score",
        "enroute_token",
        "reroute_config",
        "glens_id",
        "interventional_hash",
        "rescue_id",
        "barbecue_label",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_rejects_benign_stems_with_unregistered_terminal_suffixes(
    protected_key: str, field_name: str
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {protected_key: "opaque"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "benign_key",
    [
        "emergencyrescuenotes",
        "familybarbecueplan",
        "projectrescheduleoptions",
    ],
)
def test_forecast_allows_prefixed_benign_blinding_contexts(
    benign_key: str,
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {benign_key: "ordinary"}}]}
    episode = replace(pack.episodes[0], forecast_payload=payload)

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload == payload


@pytest.mark.parametrize(
    "compound_key",
    [
        "contractoractorid",
        "goldenexpectedlabel",
        "reroutelensid",
        "prefixcontractoractoridsuffix",
        "prefixgoldenexpectedlabelsuffix",
        "prefixreroutelensidsuffix",
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_benign_occurrence_does_not_shield_another_protected_occurrence(
    compound_key: str, field_name: str
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {compound_key: "opaque"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "compound_key",
    [
        "prefixrescuecuecodesuffix",
        "prefixbarbecuecuecodesuffix",
        "prefixrescheduleschedulehashsuffix",
    ],
)
def test_forecast_benign_context_does_not_shield_second_blinded_occurrence(
    compound_key: str,
) -> None:
    pack = _pack()
    payload = {"outer": [{"inner": {compound_key: "opaque"}}]}
    episode = replace(pack.episodes[0], forecast_payload=payload)

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_scans_very_long_keys_iteratively(field_name: str) -> None:
    pack = _pack()
    protected_key = f"{'x' * 200_000}actorsecret"
    payload = {"outer": [{"inner": {protected_key: "opaque"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError, match="request payload exceeds limits"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_rejects_very_long_repeated_benign_contexts(
    field_name: str,
) -> None:
    pack = _pack()
    benign_key = "contractor" * 20_000
    payload = {"outer": [{"inner": {benign_key: "ordinary"}}]}
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError, match="request payload exceeds limits"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "payload",
    [
        {"first": "x" * (32 * 1024), "second": "y" * (32 * 1024)},
        {"é" * 257: "ordinary"},
        {"ordinary": "é" * 16_385},
        {"items": [None] * 4_096},
    ],
)
@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_rejects_request_limit_overruns(
    payload: dict, field_name: str
) -> None:
    pack = _pack()
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(
        ValueError,
        match=r"exceeds (?:reserved-label traversal )?limits",
    ):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_payload_accepts_utf8_key_and_string_at_limits(field_name: str) -> None:
    pack = _pack()
    payload = {"é" * 256: "é" * 16_384}
    episode = replace(pack.episodes[0], **{field_name: payload})

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    rows = (
        schedule.forecast_rows
        if field_name == "forecast_payload"
        else schedule.probe_rows
    )
    assert next(
        value
        for value in rows[0].request_payload.values()
        if type(value) is str and len(value) > 1_000
    ) == next(iter(payload.values()))


def test_request_limits_apply_before_payload_expansion(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], forecast_payload={"ordinary": "x" * 32_769}
    )
    detached_calls = 0
    original = schedule_module._detached

    def recording_detached(value):
        nonlocal detached_calls
        detached_calls += 1
        return original(value)

    monkeypatch.setattr(schedule_module, "_detached", recording_detached)

    with pytest.raises(ValueError, match="request payload exceeds limits"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )
    assert detached_calls == 0


def test_validate_payload_captures_before_canonical_mutation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    payload = {
        "question": "before",
        "nested": {"note": "before"},
    }
    original = schedule_module.canonical_json_bytes
    mutated = False

    def mutate_source_during_canonical(value):
        nonlocal mutated
        if not mutated:
            payload["nested"]["note"] = "after"
            mutated = True
        return original(value)

    monkeypatch.setattr(
        schedule_module,
        "canonical_json_bytes",
        mutate_source_during_canonical,
    )

    captured = schedule_module._validate_payload(payload, "payload")

    assert mutated
    assert payload["nested"]["note"] == "after"
    assert captured["nested"]["note"] == "before"
    assert captured is not payload


def test_validate_pack_returns_a_fully_captured_tree() -> None:
    pack = _pack()

    captured = schedule_module._validate_pack(pack)

    assert captured is not pack
    assert captured.episodes[0] is not pack.episodes[0]
    assert (
        captured.episodes[0].forecast_payload
        is not pack.episodes[0].forecast_payload
    )
    assert (
        captured.episodes[0].forecast_payload["choices"]
        is not pack.episodes[0].forecast_payload["choices"]
    )
    assert (
        captured.episodes[0].variants[0].decoding
        is not pack.episodes[0].variants[0].decoding
    )

    pack.episodes[0].forecast_payload["choices"].append(9)
    pack.episodes[0].probe_payload["question"] = "changed"
    pack.episodes[0].variants[0].decoding["temperature"] = 1

    assert captured.episodes[0].forecast_payload["choices"] == [0, 1]
    assert captured.episodes[0].probe_payload["question"] == "probe-0"
    assert captured.episodes[0].variants[0].decoding["temperature"] == 0


def test_pack_request_label_budgets_are_scoped_per_payload() -> None:
    pack = _pack()
    episodes = tuple(
        replace(
            episode,
            forecast_payload={"items": [None] * 150},
            probe_payload={"items": [None] * 150},
        )
        for episode in pack.episodes
    )

    schedule = compile_schedule(
        replace(pack, episodes=episodes), actor_ids=ACTORS, seed=711
    )

    assert len(schedule.logical_calls) == 336


def test_pack_accepts_one_request_at_node_budget_boundary() -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], forecast_payload={"items": [None] * 4_093}
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert len(schedule.forecast_rows[0].request_payload["items"]) == 4_093


def test_pack_rejects_one_request_over_node_budget() -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], forecast_payload={"items": [None] * 4_094}
    )

    with pytest.raises(ValueError, match="limits"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_pack_rejects_one_variant_over_label_walk_budget() -> None:
    pack = _pack()
    variant = replace(
        pack.episodes[0].variants[0],
        decoding={"items": [None] * 4_094},
    )

    with pytest.raises(ValueError, match="limits"):
        compile_schedule(
            _with_variant(pack, 0, 0, variant), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("levels", [12, 14, 18])
def test_variant_alias_dag_rejects_before_canonicalization(
    levels: int, monkeypatch: pytest.MonkeyPatch
) -> None:
    original = schedule_module.canonical_json_bytes
    canonical_calls = 0

    def guarded_canonical(value):
        nonlocal canonical_calls
        _assert_no_mutable_aliases(value)
        canonical_calls += 1
        return original(value)

    monkeypatch.setattr(
        schedule_module, "canonical_json_bytes", guarded_canonical
    )
    variant = replace(
        _variant("C0"), decoding={"dag": _binary_alias_dag(levels)}
    )

    with pytest.raises(ValueError, match="limits"):
        schedule_module._validate_variant(variant)
    assert canonical_calls == 0


def test_variant_small_alias_is_captured_without_shared_containers() -> None:
    shared = {"value": "ordinary"}
    variant = replace(
        _variant("C0"), decoding={"first": shared, "second": shared}
    )

    captured = schedule_module._validate_variant(variant)

    assert captured.decoding == variant.decoding
    assert captured.decoding is not variant.decoding
    assert captured.decoding["first"] is not captured.decoding["second"]


@pytest.mark.parametrize(
    "location", ["episode_id", "shared_body", "cue_surface"]
)
def test_scoped_pack_label_walk_still_rejects_authored_c3(
    location: str,
) -> None:
    pack = _pack()
    if location == "episode_id":
        episode = replace(pack.episodes[0], episode_id="ep-C3")
        invalid = _with_episode(pack, 0, episode)
    elif location == "shared_body":
        variants = tuple(
            replace(variant, shared_body="visible C3")
            for variant in pack.episodes[0].variants
        )
        episode = replace(pack.episodes[0], variants=variants)
        invalid = _with_episode(pack, 0, episode)
    else:
        variant = replace(
            pack.episodes[0].variants[0], cue_surface="visible C3"
        )
        invalid = _with_variant(pack, 0, 0, variant)

    with pytest.raises(ValueError, match="reserved condition label"):
        compile_schedule(invalid, actor_ids=ACTORS, seed=711)


@pytest.mark.parametrize(
    "blind_key",
    [
        "cue",
        "condition",
        "actor",
        "actor_id",
        "actor_model",
        "model",
        "model_id",
        "model_name",
        "tested_model",
        "provider",
        "route",
        "schedule_id",
        "bundle_id",
        "episode_id",
        "role",
        "expected",
        "gold",
        "private",
        "actorid",
        "actormodel",
        "modelid",
        "modelname",
        "testedmodel",
        "conditionid",
        "cueid",
        "scheduleid",
        "bundleid",
        "episodeid",
        "rolelabel",
        "expectedlabel",
        "goldlabel",
        "privateid",
        "episoderole",
    ],
)
def test_forecast_payload_rejects_blinding_metadata_recursively(
    blind_key: str,
) -> None:
    pack = _pack()
    episode = replace(
        pack.episodes[0], forecast_payload={"nested": [{blind_key: "opaque"}]}
    )

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_forecast_allows_unstructured_blinding_words_in_ordinary_prose() -> None:
    pack = _pack()
    text = (
        "Discuss actor and model behavior without exposing a structured provider, "
        "route, condition, or cue field."
    )
    episode = replace(pack.episodes[0], forecast_payload={"question": text})

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.forecast_rows[0].request_payload == {"question": text}


@pytest.mark.parametrize(
    ("location", "reserved"),
    [
        ("key", "conditionC3Payload"),
        ("key", "actorc3metadata"),
        ("value", "conditionC1Surface"),
        ("value", "cueC0Value"),
        ("surface", "actorc2metadata"),
    ],
)
def test_authored_visible_strings_reject_embedded_condition_labels(
    location: str, reserved: str
) -> None:
    pack = _pack()
    if location == "key":
        episode = replace(pack.episodes[0], forecast_payload={reserved: "ordinary"})
        invalid = _with_episode(pack, 0, episode)
    elif location == "value":
        episode = replace(
            pack.episodes[0], forecast_payload={"ordinary_note": reserved}
        )
        invalid = _with_episode(pack, 0, episode)
    else:
        variant = replace(pack.episodes[0].variants[1], cue_surface=reserved)
        invalid = _with_variant(pack, 0, 1, variant)

    with pytest.raises(ValueError):
        compile_schedule(invalid, actor_ids=ACTORS, seed=711)


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
@pytest.mark.parametrize(
    "payload",
    [
        {"cue": "C0"},
        {"condition": "ordinary"},
        {"ordinary": {"nested": ["visible C2 label"]}},
    ],
)
def test_authored_actor_visible_payloads_reject_condition_metadata_and_labels(
    field_name: str, payload: dict
) -> None:
    pack = _pack()
    episode = replace(pack.episodes[0], **{field_name: payload})

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("call_kind", ["forecast", "primary", "probe"])
def test_scheduled_actor_visible_payloads_have_no_structural_cue_exemption(
    call_kind: str,
) -> None:
    schedule = _schedule()
    calls = list(schedule.logical_calls)
    index = next(
        index
        for index, row in enumerate(calls)
        if row.call_kind == call_kind
    )
    payload = json.loads(json.dumps(calls[index].request_payload))
    payload["cue"] = "C0"
    calls[index] = replace(calls[index], request_payload=payload)

    with pytest.raises(ValueError, match="reserved condition label"):
        _schedule_with_calls(schedule, calls).assert_counterbalanced()


def test_digest_and_opaque_id_fields_allow_incidental_hex_label_fragments() -> None:
    pack = _pack()
    variants = tuple(
        replace(
            variant,
            task_semantics_sha256="c3" + "a" * 62,
            answer_semantics_sha256="c0" + "b" * 62,
        )
        for variant in pack.episodes[0].variants
    )
    episode = replace(pack.episodes[0], variants=variants)
    actors = (
        "c3" + "a" * 14,
        "c2" + "b" * 14,
        "c1" + "c" * 14,
        "c0" + "d" * 14,
    )

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=actors, seed=711
    )

    schedule.assert_counterbalanced()


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
    checked_ids = {id(payload) for payload in checked}
    schedule_payload_ids = {
        id(row.request_payload) for row in schedule.logical_calls
    }
    assert len(checked_ids) == len(checked)
    assert schedule_payload_ids < checked_ids


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
            "primary_logical_call_id",
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
    pack_episodes = tuple(sorted(_pack().episodes, key=lambda item: item.episode_id))
    episodes = tuple(episode.episode_id for episode in pack_episodes)
    role_by_episode = {episode.episode_id: episode.role for episode in pack_episodes}
    role_index = {role: index for index, role in enumerate(("target", "null", "restraint"))}
    role_seen = Counter()
    role_ordinal = {}
    for episode in pack_episodes:
        role_ordinal[episode.episode_id] = role_seen[episode.role]
        role_seen[episode.role] += 1
    expected_bundle_pairs = []
    for episode_index, episode_id in enumerate(episodes):
        offset = (schedule.seed + episode_index) % len(actors)
        actor_order = actors[offset:] + actors[:offset]
        expected_bundle_pairs.extend((actor, episode_id) for actor in actor_order)

    assert [
        (bundle.actor_id, bundle.episode_id) for bundle in schedule.bundles
    ] == expected_bundle_pairs

    actor_index = {actor: index for index, actor in enumerate(actors)}
    first_cues = {}
    for bundle in schedule.bundles:
        calls = [
            row for row in schedule.logical_calls if row.bundle_id == bundle.bundle_id
        ]
        rotation = (
            schedule.seed
            + actor_index[bundle.actor_id]
            + role_index[bundle.role]
            + role_ordinal[bundle.episode_id]
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
    role_counts = defaultdict(Counter)
    for row in schedule.primary_rows:
        counts[(row.actor_id, row.presentation_position)][row.cue] += 1
        role_counts[(row.actor_id, row.role, row.presentation_position)][row.cue] += 1
    assert set(counts) == {(actor, position) for actor in ACTORS for position in range(3)}
    assert all(counter == Counter({"C0": 4, "C1": 4, "C2": 4}) for counter in counts.values())
    assert set(role_counts) == {
        (actor, role, position)
        for actor in ACTORS
        for role in ("target", "null", "restraint")
        for position in range(3)
    }
    for counter in role_counts.values():
        values = [counter[cue] for cue in CUES]
        assert max(values) - min(values) <= 1
        assert max(values) < 4
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
        "logical_call_ids": list(bundle.logical_call_ids),
    }
    call_material = {
        "domain": "biblebench.logical_call.v1",
        "seed": schedule.seed,
        "actor_id": call.actor_id,
        "module": call.module,
        "episode_id": call.episode_id,
        "role": call.role,
        "call_kind": call.call_kind,
        "cue": call.cue,
        "presentation_position": call.presentation_position,
        "primary_logical_call_id": call.primary_logical_call_id,
        "request_payload_sha256": canonical_sha256(call.request_payload),
    }

    assert bundle.bundle_id == canonical_sha256(bundle_material)[:16]
    assert call.logical_call_id == canonical_sha256(call_material)[:16]
    all_ids = [bundle.bundle_id for bundle in schedule.bundles]
    all_ids.extend(row.logical_call_id for row in schedule.logical_calls)
    assert len(all_ids) == len(set(all_ids))
    assert all(re.fullmatch(r"[0-9a-f]{16}", identifier) for identifier in all_ids)


def test_payload_changes_rebind_affected_call_and_bundle_identifiers() -> None:
    base_pack = _pack()
    base = compile_schedule(base_pack, actor_ids=ACTORS, seed=711)
    episode = base_pack.episodes[0]

    forecast_episode = replace(
        episode,
        forecast_payload={"question": "alternate forecast", "choices": [0, 1]},
    )
    forecast_changed = compile_schedule(
        _with_episode(base_pack, 0, forecast_episode),
        actor_ids=ACTORS,
        seed=711,
    )

    surface_variant = replace(
        episode.variants[1], cue_surface="alternate scriptural surface"
    )
    primary_changed = compile_schedule(
        _with_variant(base_pack, 0, 1, surface_variant),
        actor_ids=ACTORS,
        seed=711,
    )

    probe_episode = replace(
        episode, probe_payload={"question": "alternate probe"}
    )
    probe_changed = compile_schedule(
        _with_episode(base_pack, 0, probe_episode),
        actor_ids=ACTORS,
        seed=711,
    )

    def calls(schedule: Schedule) -> dict[tuple, str]:
        return {
            (
                row.actor_id,
                row.episode_id,
                row.call_kind,
                row.cue,
                row.presentation_position,
            ): row.logical_call_id
            for row in schedule.logical_calls
        }

    base_calls = calls(base)
    forecast_calls = calls(forecast_changed)
    primary_calls = calls(primary_changed)
    probe_calls = calls(probe_changed)
    for identity, base_id in base_calls.items():
        _, episode_id, kind, cue, _ = identity
        if episode_id != "ep-00":
            assert forecast_calls[identity] == base_id
            assert primary_calls[identity] == base_id
            assert probe_calls[identity] == base_id
            continue
        assert (forecast_calls[identity] != base_id) == (kind == "forecast")
        assert (primary_calls[identity] != base_id) == (
            cue == "C1" and kind in {"primary", "probe"}
        )
        assert (probe_calls[identity] != base_id) == (kind == "probe")

    base_bundles = {
        (bundle.actor_id, bundle.episode_id): bundle.bundle_id
        for bundle in base.bundles
    }
    for changed in (forecast_changed, primary_changed, probe_changed):
        for bundle in changed.bundles:
            identity = (bundle.actor_id, bundle.episode_id)
            assert (bundle.bundle_id != base_bundles[identity]) == (
                bundle.episode_id == "ep-00"
            )


@pytest.mark.parametrize("kind", ["forecast", "primary", "probe"])
def test_payload_mutation_under_original_identifiers_is_rejected(kind: str) -> None:
    schedule = _schedule()
    episode_id = schedule.bundles[0].episode_id
    calls = list(schedule.logical_calls)
    for index, row in enumerate(calls):
        if row.episode_id != episode_id or row.call_kind != kind:
            continue
        payload = json.loads(json.dumps(row.request_payload))
        if kind == "forecast":
            payload["question"] = "safe changed forecast"
        elif kind == "primary":
            payload["shared_body"] = "Choose a different responsible action."
        else:
            payload["question"] = "safe changed probe"
        calls[index] = replace(row, request_payload=payload)

    invalid = _schedule_with_calls(schedule, calls)
    with pytest.raises(ValueError, match="logical call ID"):
        invalid.assert_counterbalanced()
    with pytest.raises(ValueError):
        invalid.to_canonical_json()


@pytest.mark.parametrize("levels", [12, 18])
def test_canonical_serialization_rejects_alias_dag_before_canonicalization(
    levels: int, monkeypatch: pytest.MonkeyPatch
) -> None:
    schedule = _schedule()
    calls = list(schedule.logical_calls)
    calls[0] = replace(
        calls[0], request_payload={"dag": _binary_alias_dag(levels)}
    )
    schedule = _schedule_with_calls(schedule, calls)
    original = schedule_module.canonical_json_bytes
    canonical_calls = 0

    def guarded_canonical(value):
        nonlocal canonical_calls
        _assert_no_mutable_aliases(value)
        canonical_calls += 1
        return original(value)

    monkeypatch.setattr(
        schedule_module, "canonical_json_bytes", guarded_canonical
    )

    with pytest.raises(ValueError, match="limits"):
        schedule.to_canonical_json()
    assert canonical_calls == 0


def test_canonical_serialization_never_canonicalizes_mutable_aliases(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    schedule = _schedule()
    original = schedule_module.canonical_json_bytes
    canonical_calls = 0

    def guarded_canonical(value):
        nonlocal canonical_calls
        _assert_no_mutable_aliases(value)
        canonical_calls += 1
        return original(value)

    monkeypatch.setattr(
        schedule_module, "canonical_json_bytes", guarded_canonical
    )

    schedule.to_canonical_json()

    assert canonical_calls > len(schedule.logical_calls)


def test_canonical_serialization_uses_an_immutable_payload_snapshot(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    schedule = _schedule()
    original_question = schedule.logical_calls[0].request_payload["question"]
    original = schedule_module.canonical_json_bytes
    mutated = False

    def mutate_during_full_schedule_encoding(value):
        nonlocal mutated
        if type(value) is dict and "logical_calls" in value and not mutated:
            schedule.logical_calls[0].request_payload["question"] = (
                "mutated during serialization"
            )
            mutated = True
        return original(value)

    monkeypatch.setattr(
        schedule_module,
        "canonical_json_bytes",
        mutate_during_full_schedule_encoding,
    )

    encoded = schedule.to_canonical_json()

    assert mutated
    parsed = json.loads(encoded)
    assert (
        parsed["logical_calls"][0]["request_payload"]["question"]
        == original_question
    )
    assert (
        schedule.logical_calls[0].request_payload["question"]
        == "mutated during serialization"
    )


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
    assert probe.request_payload == {"question": "probe-0"}
    assert forecast.primary_logical_call_id is None
    assert primary.primary_logical_call_id is None
    assert probe.primary_logical_call_id == primary.logical_call_id
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


def test_probe_payloads_are_cue_invariant_while_private_links_are_distinct() -> None:
    schedule = _schedule()
    bundle = schedule.bundles[0]
    calls = [
        row for row in schedule.logical_calls if row.bundle_id == bundle.bundle_id
    ]
    primaries = calls[1::2]
    probes = calls[2::2]

    assert len({canonical_sha256(row.request_payload) for row in probes}) == 1
    assert all(
        "logical_call_id" not in json.dumps(row.request_payload).casefold()
        for row in probes
    )
    assert [row.primary_logical_call_id for row in probes] == [
        row.logical_call_id for row in primaries
    ]
    assert len({row.primary_logical_call_id for row in probes}) == 3


def test_canonical_schedule_serializes_private_probe_links_only_as_row_metadata() -> None:
    schedule = _schedule()
    parsed = json.loads(schedule.to_canonical_json())

    for source, serialized in zip(
        schedule.logical_calls, parsed["logical_calls"], strict=True
    ):
        assert serialized["primary_logical_call_id"] == (
            source.primary_logical_call_id
        )
        assert "primary_logical_call_id" not in serialized["request_payload"]


@pytest.mark.parametrize(
    "leak_form", ["exact", "prose", "uppercase", "fullwidth", "key"]
)
def test_compile_rejects_a_generated_primary_id_in_its_probe_payload(
    leak_form: str,
) -> None:
    pack = _pack()
    source_primary = next(
        row
        for row in compile_schedule(
            pack, actor_ids=ACTORS, seed=711
        ).primary_rows
        if row.episode_id == "ep-00"
        and re.search(r"c[0-3]", row.logical_call_id, re.IGNORECASE) is None
    )
    primary_id = source_primary.logical_call_id
    if leak_form == "exact":
        probe_payload = {"request_id": primary_id}
    elif leak_form == "prose":
        probe_payload = {"note": f"linked primary ({primary_id})."}
    elif leak_form == "uppercase":
        probe_payload = {"note": primary_id.upper()}
    elif leak_form == "fullwidth":
        probe_payload = {"note": primary_id.translate(_FULLWIDTH_HEX)}
    else:
        probe_payload = {f"reference-{primary_id}": "ordinary"}
    episode = replace(pack.episodes[0], probe_payload=probe_payload)

    with pytest.raises(ValueError, match="generated schedule identifier"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "leak_form",
    [
        "hash_prefix",
        "hash_middle",
        "zwj_split",
        "hyphen_split",
        "space_split",
        "combining_split",
        "tab_split",
        "newline_split",
        "nul_split",
    ],
)
def test_generated_id_firewall_rejects_disguised_and_embedded_ids(
    leak_form: str,
) -> None:
    pack = _pack()
    primary_id = next(
        row.logical_call_id
        for row in compile_schedule(
            pack, actor_ids=ACTORS, seed=711
        ).primary_rows
        if row.episode_id == "ep-00"
        and re.search(r"c[0-3]", row.logical_call_id, re.IGNORECASE) is None
    )
    if leak_form == "hash_prefix":
        probe_payload = {"content_sha256": primary_id + "a" * 48}
    elif leak_form == "hash_middle":
        probe_payload = {
            "content_sha256": "a" * 24 + primary_id + "b" * 24
        }
    elif leak_form == "zwj_split":
        probe_payload = {"note": "\u200d".join(primary_id)}
    elif leak_form == "hyphen_split":
        probe_payload = {"note": "-".join(primary_id)}
    elif leak_form == "space_split":
        probe_payload = {"note": " ".join(primary_id)}
    elif leak_form == "combining_split":
        probe_payload = {"note": primary_id[:8] + "\u0327" + primary_id[8:]}
    elif leak_form == "tab_split":
        probe_payload = {"note": "\t".join(primary_id)}
    elif leak_form == "newline_split":
        probe_payload = {"note": "\n".join(primary_id)}
    else:
        probe_payload = {"note": "\x00".join(primary_id)}
    episode = replace(pack.episodes[0], probe_payload=probe_payload)

    with pytest.raises(ValueError, match="generated schedule identifier"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    ("source_characters", "translation"),
    [
        ("0123456789", str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")),
        ("ace", str.maketrans({"a": "а", "c": "с", "e": "е"})),
    ],
)
def test_generated_id_firewall_rejects_unicode_digit_and_hex_lookalikes(
    source_characters: str, translation: dict[int, str]
) -> None:
    pack = _pack()
    primary_id = next(
        row.logical_call_id
        for row in compile_schedule(
            pack, actor_ids=ACTORS, seed=711
        ).primary_rows
        if row.episode_id == "ep-00"
        and re.search(r"c[0-3]", row.logical_call_id, re.IGNORECASE) is None
        and any(
            character in row.logical_call_id
            for character in source_characters
        )
    )
    disguised_id = primary_id.translate(translation)
    episode = replace(
        pack.episodes[0], probe_payload={"note": disguised_id}
    )

    assert disguised_id != primary_id
    with pytest.raises(ValueError, match="generated schedule identifier"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_generated_id_firewall_rejects_exact_lunate_sigma_escape() -> None:
    pack = _pack()
    private_id = "6e779c794025e210"
    disguised_id = "6ε779ϲ794025ε210"
    generated_ids = {
        row.logical_call_id
        for row in compile_schedule(pack, actor_ids=ACTORS, seed=711).logical_calls
    }
    assert private_id in generated_ids
    episode = replace(
        pack.episodes[0], probe_payload={"note": disguised_id}
    )

    with pytest.raises(ValueError, match="generated schedule identifier"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize("symbol", ["+", "=", "→", "✅", "£", "^"])
def test_generated_id_firewall_rejects_symbol_split_private_id(
    symbol: str,
) -> None:
    pack = _pack()
    private_id = "6e779c794025e210"
    disguised_id = symbol.join(private_id)
    generated_ids = {
        row.logical_call_id
        for row in compile_schedule(pack, actor_ids=ACTORS, seed=711).logical_calls
    }
    assert private_id in generated_ids
    episode = replace(
        pack.episodes[0], probe_payload={"note": disguised_id}
    )

    with pytest.raises(ValueError, match="generated schedule identifier"):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


def test_generated_id_firewall_preserves_unrelated_greek_prose_and_id() -> None:
    pack = _pack()
    probe_payload = {
        "note": "Η ελληνική λέξη σίγμα παραμένει ακριβής.",
        "request_id": "6ε779ϲ794025ε211",
    }
    episode = replace(pack.episodes[0], probe_payload=probe_payload)

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.probe_rows[0].request_payload == probe_payload


def test_generated_id_firewall_preserves_unrelated_ids_and_hashes() -> None:
    pack = _pack()
    probe_payload = {
        "request_id": "0123456789abcdef",
        "content_sha256": "0" * 64,
        "alternate_hash": "f" * 64,
        "note": "dead-beef-dead-beef",
    }
    episode = replace(pack.episodes[0], probe_payload=probe_payload)

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    assert schedule.probe_rows[0].request_payload == probe_payload


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


def test_actor_ids_reject_nfkc_casefold_collisions_and_oversized_values() -> None:
    with pytest.raises(ValueError, match="actor IDs.*collision"):
        compile_schedule(
            _pack(), actor_ids=("A", "Ａ", "B", "C"), seed=711
        )
    with pytest.raises(ValueError, match="actor_id.*128 bytes"):
        compile_schedule(
            _pack(), actor_ids=("A", "B", "C", "é" * 65), seed=711
        )


def test_episode_ids_reject_nfkc_casefold_collisions_and_oversized_values() -> None:
    pack = _pack()
    collision = _with_episode(
        pack,
        0,
        replace(pack.episodes[0], episode_id="ｅｐ－０１"),
    )
    oversized = _with_episode(
        pack,
        0,
        replace(pack.episodes[0], episode_id="界" * 43),
    )

    with pytest.raises(ValueError, match="episode IDs.*collision"):
        compile_schedule(collision, actor_ids=ACTORS, seed=711)
    with pytest.raises(ValueError, match="episode_id.*128 bytes"):
        compile_schedule(oversized, actor_ids=ACTORS, seed=711)


def test_distinct_unicode_actor_and_episode_ids_remain_supported() -> None:
    pack = _pack()
    episodes = tuple(
        replace(episode, episode_id=f"章-{index:02d}")
        for index, episode in enumerate(pack.episodes)
    )

    schedule = compile_schedule(
        replace(pack, episodes=episodes),
        actor_ids=("α", "β", "家", "Д"),
        seed=711,
    )

    assert {bundle.actor_id for bundle in schedule.bundles} == {
        "α",
        "β",
        "家",
        "Д",
    }
    assert len({bundle.episode_id for bundle in schedule.bundles}) == 12


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


@pytest.mark.parametrize(
    ("field_name", "changed_value"),
    [
        ("task_semantics_sha256", "e" * 64),
        ("answer_semantics_sha256", "f" * 64),
        ("tool_schema_sha256", "0" * 64),
        ("response_schema_sha256", "1" * 64),
        ("semantic_response_tokens", ("answer", "basis")),
    ],
)
def test_cue_invariant_mismatch_error_names_constant_field(
    field_name: str, changed_value: object
) -> None:
    pack = _pack()
    changed_variant = replace(
        pack.episodes[0].variants[1], **{field_name: changed_value}
    )
    invalid = _with_variant(pack, 0, 1, changed_variant)

    with pytest.raises(
        ValueError, match=rf"cue variants change {field_name}$"
    ):
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
        ("probe_payload", {"actorid": "opaque-no"}),
        ("probe_payload", {"actormodel": "opaque-no"}),
        ("probe_payload", {"modelid": "opaque-no"}),
        ("probe_payload", {"modelname": "opaque-no"}),
        ("probe_payload", {"testedmodel": "opaque-no"}),
        ("probe_payload", {"rolelabel": "opaque-no"}),
        ("probe_payload", {"expectedlabel": "opaque-no"}),
        ("probe_payload", {"goldlabel": "opaque-no"}),
        ("probe_payload", {"privateid": "opaque-no"}),
        ("probe_payload", {"episoderole": "opaque-no"}),
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


def test_scoped_pack_scalar_walk_remains_bounded() -> None:
    pack = _pack()
    for index in range(4_096):
        object.__setattr__(pack, f"extra_{index}", None)

    with pytest.raises(ValueError, match="traversal limits"):
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


@pytest.mark.parametrize("levels", [20, 30])
def test_reserved_label_walk_inspects_shared_alias_dag_once(
    levels: int, monkeypatch: pytest.MonkeyPatch
) -> None:
    original = schedule_module._EMBEDDED_CUE_LABEL

    class BoundedSearch:
        calls = 0

        def search(self, value):
            self.calls += 1
            if self.calls > 200:
                raise AssertionError("reserved-label walk repeated a shared alias")
            return original.search(value)

    bounded = BoundedSearch()
    monkeypatch.setattr(schedule_module, "_EMBEDDED_CUE_LABEL", bounded)
    shared = {"ordinary_note": "ordinary"}
    for _ in range(levels):
        shared = {"left": shared, "right": shared}

    schedule_module._assert_no_c3(shared)

    assert bounded.calls <= 2 * levels + 2


@pytest.mark.parametrize(
    "field_order",
    [("opaque_id", "ordinary"), ("ordinary", "opaque_id")],
)
def test_reserved_label_walk_rescans_alias_under_each_policy_context(
    field_order: tuple[str, str],
) -> None:
    shared = ["c3" + "a" * 14]
    payload = {name: shared for name in field_order}

    with pytest.raises(ValueError, match="reserved condition label"):
        schedule_module._assert_no_c3(payload)


def test_reserved_label_walk_allows_safe_aliases_with_one_policy_context() -> None:
    opaque = ["c3" + "a" * 14]
    ordinary = ["ordinary"]

    schedule_module._assert_no_c3(
        {"first_id": opaque, "second_id": opaque}
    )
    schedule_module._assert_no_c3(
        {"first": ordinary, "second": ordinary}
    )


@pytest.mark.parametrize(
    "field_order",
    [("opaque_id", "ordinary"), ("ordinary", "opaque_id")],
)
def test_reserved_label_walk_allows_safe_aliases_across_policy_contexts(
    field_order: tuple[str, str],
) -> None:
    shared = ["ordinary"]

    schedule_module._assert_no_c3(
        {name: shared for name in field_order}
    )


def test_reserved_label_walk_context_states_remain_bounded(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original = schedule_module._EMBEDDED_CUE_LABEL

    class BoundedSearch:
        calls = 0

        def search(self, value):
            self.calls += 1
            if self.calls > 256:
                raise AssertionError("reserved-label contexts were unbounded")
            return original.search(value)

    bounded = BoundedSearch()
    monkeypatch.setattr(schedule_module, "_EMBEDDED_CUE_LABEL", bounded)
    shared = ["ordinary"]
    payload = {
        **{f"opaque_{index}_id": shared for index in range(100)},
        **{f"ordinary_{index}": shared for index in range(100)},
    }

    schedule_module._assert_no_c3(payload)

    assert bounded.calls <= 202


def test_reserved_label_walk_rejects_wide_container_before_children() -> None:
    wide = ["C3", *([None] * 4_096)]

    with pytest.raises(ValueError, match="traversal limits"):
        schedule_module._assert_no_c3(wide)


def test_reserved_label_walk_still_rejects_cycles_with_seen_aliases() -> None:
    cyclic = []
    cyclic.append(cyclic)

    with pytest.raises(ValueError, match="traversal limits"):
        schedule_module._assert_no_c3(cyclic)


def test_reserved_label_walk_still_rejects_depth_boundary() -> None:
    nested = []
    for _ in range(128):
        nested = [nested]

    with pytest.raises(ValueError, match="traversal limits"):
        schedule_module._assert_no_c3(nested)


@pytest.mark.parametrize("field_name", ["forecast_payload", "probe_payload"])
def test_compile_accepts_small_shared_payload_aliases(
    field_name: str,
) -> None:
    pack = _pack()
    shared = {"ordinary_note": "ordinary"}
    payload = {"left": shared, "right": shared}
    episode = replace(pack.episodes[0], **{field_name: payload})

    schedule = compile_schedule(
        _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
    )

    rows = (
        schedule.forecast_rows
        if field_name == "forecast_payload"
        else schedule.probe_rows
    )
    assert rows[0].request_payload["left"] == shared
    assert rows[0].request_payload["right"] == shared
    assert (
        rows[0].request_payload["left"]
        is not rows[0].request_payload["right"]
    )


def test_reserved_label_walk_rejects_excessive_depth_without_recursion_error() -> None:
    nested = []
    cursor = nested
    for _ in range(2_000):
        child = []
        cursor.append(child)
        cursor = child
    pack = _pack()
    episode = replace(pack.episodes[0], forecast_payload={"nested": nested})

    with pytest.raises(ValueError):
        compile_schedule(
            _with_episode(pack, 0, episode), actor_ids=ACTORS, seed=711
        )


@pytest.mark.parametrize(
    "mutation",
    [
        "forecast_private",
        "primary_sensitive_value",
        "probe_private",
        "forecast_later_scope",
        "forecast_blinding",
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
        elif mutation == "forecast_blinding" and row.call_kind == "forecast":
            payload["nested"] = {"provider": "opaque"}
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


@pytest.mark.parametrize(
    "mutation",
    [
        "missing_probe_link",
        "wrong_primary_link",
        "cross_bundle_link",
        "cross_actor_link",
        "self_link",
        "forecast_link",
        "primary_link",
    ],
)
def test_private_probe_linkage_fails_closed_under_tampering(
    mutation: str,
) -> None:
    schedule = _schedule()
    calls = list(schedule.logical_calls)
    probe_index = 2
    probe = calls[probe_index]
    if mutation == "missing_probe_link":
        calls[probe_index] = replace(probe, primary_logical_call_id=None)
    elif mutation == "wrong_primary_link":
        calls[probe_index] = replace(
            probe, primary_logical_call_id=calls[3].logical_call_id
        )
    elif mutation == "cross_bundle_link":
        calls[probe_index] = replace(
            probe, primary_logical_call_id=calls[8].logical_call_id
        )
    elif mutation == "cross_actor_link":
        other_actor_primary = next(
            row
            for row in calls
            if row.call_kind == "primary"
            and row.episode_id == probe.episode_id
            and row.actor_id != probe.actor_id
        )
        calls[probe_index] = replace(
            probe,
            primary_logical_call_id=other_actor_primary.logical_call_id,
        )
    elif mutation == "self_link":
        calls[probe_index] = replace(
            probe, primary_logical_call_id=probe.logical_call_id
        )
    elif mutation == "forecast_link":
        calls[0] = replace(
            calls[0], primary_logical_call_id=calls[0].logical_call_id
        )
    else:
        calls[1] = replace(
            calls[1], primary_logical_call_id=calls[1].logical_call_id
        )

    invalid = _schedule_with_calls(schedule, calls)
    with pytest.raises(ValueError):
        invalid.assert_counterbalanced()
    with pytest.raises(ValueError):
        invalid.to_canonical_json()


def test_counterbalance_revalidation_rejects_generated_id_payload_leakage() -> None:
    schedule = _schedule()
    calls = list(schedule.logical_calls)
    primary = calls[1]
    probe = calls[2]
    payload = json.loads(json.dumps(probe.request_payload))
    payload["request_id"] = primary.logical_call_id
    calls[2] = replace(probe, request_payload=payload)
    invalid = _schedule_with_calls(schedule, calls)

    with pytest.raises(ValueError, match="generated schedule identifier"):
        invalid.assert_counterbalanced()
    with pytest.raises(ValueError, match="generated schedule identifier"):
        invalid.to_canonical_json()


def test_assert_counterbalanced_accepts_a_bounded_payload_alias_snapshot() -> None:
    schedule = _schedule()
    calls = list(schedule.logical_calls)
    calls[7] = replace(
        calls[7], request_payload=calls[0].request_payload
    )
    aliased = _schedule_with_calls(schedule, calls)

    aliased.assert_counterbalanced()
    encoded = aliased.to_canonical_json()

    assert json.loads(encoded)["logical_calls"][0]["request_payload"] == (
        json.loads(encoded)["logical_calls"][7]["request_payload"]
    )


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
