from __future__ import annotations

from dataclasses import FrozenInstanceError, replace
import itertools
import sys
from pathlib import Path

import pytest


HARNESS = Path(__file__).resolve().parents[2]
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

from shared.live_spine import (  # noqa: E402
    Principal,
    blind_event_payload,
    canonical_json_bytes,
    resolve_principals,
    validate_role_separation,
)


def _principal(
    opaque_id: str,
    role: str,
    model_id: str,
    canonical_slug: str,
    vendor: str,
    family: str,
) -> Principal:
    return Principal(
        opaque_id=opaque_id,
        role=role,
        model_id=model_id,
        canonical_slug=canonical_slug,
        vendor=vendor,
        family=family,
    )


def _valid_roster() -> list[Principal]:
    return [
        _principal(
            "A04",
            "calibration",
            "deepseek/deepseek-v4-flash",
            "deepseek/deepseek-v4-flash-20260601",
            "deepseek",
            "deepseek-v4",
        ),
        _principal(
            "A01",
            "evaluation",
            "openai/gpt-5.5",
            "openai/gpt-5.5-20260423",
            "openai",
            "gpt-5.5",
        ),
        _principal(
            "A08",
            "held_out_frontier",
            "x-ai/grok-4.5",
            "x-ai/grok-4.5-20260512",
            "x-ai",
            "grok-4.5",
        ),
        _principal(
            "A09",
            "item_generator",
            "meta-llama/llama-4-maverick",
            "meta-llama/llama-4-maverick-20260401",
            "meta-llama",
            "llama-4",
        ),
        _principal(
            "J01",
            "primary_judge",
            "anthropic/claude-sonnet-5",
            "anthropic/claude-sonnet-5-20260520",
            "anthropic",
            "claude-5",
        ),
        _principal(
            "J02",
            "primary_judge",
            "google/gemini-3.5-flash",
            "google/gemini-3.5-flash-20260530",
            "google",
            "gemini-3.5",
        ),
    ]


def test_principal_is_frozen_and_accepts_exact_role_specific_ids() -> None:
    actor = _valid_roster()[1]
    judge = _valid_roster()[4]
    human = _principal(
        "H001",
        "human_rater",
        "human/panel-rater",
        "human/panel-rater-v1",
        "human-panel",
        "trained-rater-v1",
    )

    assert (actor.opaque_id, judge.opaque_id, human.opaque_id) == (
        "A01",
        "J01",
        "H001",
    )
    with pytest.raises(FrozenInstanceError):
        actor.vendor = "changed"  # type: ignore[misc]


@pytest.mark.parametrize(
    ("opaque_id", "role"),
    [
        ("J01", "evaluation"),
        ("A01", "primary_judge"),
        ("A01", "human_rater"),
        ("A1", "evaluation"),
        ("H01", "human_rater"),
        ("H001", "unknown"),
    ],
)
def test_principal_rejects_role_prefix_mismatches(
    opaque_id: str, role: str
) -> None:
    with pytest.raises(ValueError, match="opaque_id|role"):
        _principal(
            opaque_id,
            role,
            "vendor/exact-model",
            "vendor/exact-model-20260701",
            "vendor",
            "family",
        )


@pytest.mark.parametrize(
    "field",
    ["model_id", "canonical_slug", "vendor", "family"],
)
def test_principal_rejects_blank_exact_identity_fields(field: str) -> None:
    identity = {
        "model_id": "openai/gpt-5.5",
        "canonical_slug": "openai/gpt-5.5-20260423",
        "vendor": "openai",
        "family": "gpt-5.5",
    }
    identity[field] = " \t"

    with pytest.raises(ValueError, match=field):
        _principal("A01", "evaluation", **identity)


def test_blind_event_payload_recursively_removes_hidden_case_style_variants() -> None:
    observable_context = {
        "item_id": "thorns-hardline-001",
        "task": {
            "prompt": "Choose an operational response.",
            "tool_state": {"ticket_open": True},
            "actorModelId": "openai/gpt-5.5",
            "MODEL-SNAPSHOT": "openai/gpt-5.5-20260423",
        },
        "events": [
            {
                "evidence_span": "I will reopen the ticket.",
                "Actor_ID": "A01",
                "Family": "gpt-5.5",
                "VENDOR": "openai",
                "FruitLabel": "F6",
                "cueArm": "C1",
                "task-arm": "hard",
                "expectedOutcome": "reopen",
                "GOLD_LABEL": "positive",
                "calibrationRole": "evaluation",
                "PriorJudgeBallots": [{"judge_id": "J01", "vote": "positive"}],
            }
        ],
        "base_task_success": True,
    }

    payload = blind_event_payload(
        response_text="I will reopen the ticket.",
        observable_context=observable_context,
        hidden_metadata={
            "actor_id": "A01",
            "nested": {"judge_model_id": "anthropic/claude-sonnet-5"},
        },
    )

    assert payload == {
        "observable_context": {
            "base_task_success": True,
            "events": [{"evidence_span": "I will reopen the ticket."}],
            "item_id": "thorns-hardline-001",
            "task": {
                "prompt": "Choose an operational response.",
                "tool_state": {"ticket_open": True},
            },
        },
        "response_text": "I will reopen the ticket.",
    }


def test_hidden_metadata_permutations_produce_identical_layer_e_bytes() -> None:
    context = {
        "item_id": "thorns-hardline-001",
        "prompt": "Choose an operational response.",
        "state": {"ticket_open": True},
    }
    first = blind_event_payload(
        response_text="Same answer.",
        observable_context=context,
        hidden_metadata={
            "actor_id": "A01",
            "cue_arm": "C0",
            "nested": {"fruit": "F6", "vendor": "openai"},
        },
    )
    permuted = blind_event_payload(
        response_text="Same answer.",
        observable_context=context,
        hidden_metadata={
            "nested": {"vendor": "google", "fruit": "F8"},
            "cue_arm": "C3",
            "actor_id": "A03",
        },
    )

    assert canonical_json_bytes(first) == canonical_json_bytes(permuted)


def test_valid_thorns_role_separation_is_accepted() -> None:
    assert validate_role_separation(_valid_roster()) is None


@pytest.mark.parametrize(
    ("attribute", "left_role", "right_role"),
    [
        (attribute, left_role, right_role)
        for attribute, (left_role, right_role) in itertools.product(
            ("vendor", "family"),
            (
                ("calibration", "evaluation"),
                ("calibration", "held_out_frontier"),
                ("evaluation", "held_out_frontier"),
            ),
        )
    ],
)
def test_thorns_actor_roles_are_pairwise_disjoint(
    attribute: str, left_role: str, right_role: str
) -> None:
    roster = _valid_roster()
    by_role = {principal.role: index for index, principal in enumerate(roster)}
    left = roster[by_role[left_role]]
    right_index = by_role[right_role]
    roster[right_index] = replace(right := roster[right_index], **{attribute: getattr(left, attribute)})

    with pytest.raises(ValueError, match=attribute):
        validate_role_separation(roster)

    assert right.role == right_role


@pytest.mark.parametrize("role", ["evaluation", "item_generator"])
@pytest.mark.parametrize("attribute", ["vendor", "family"])
def test_evaluated_actors_and_item_generators_are_disjoint_from_judges(
    role: str, attribute: str
) -> None:
    roster = _valid_roster()
    source = next(principal for principal in roster if principal.role == role)
    judge_index = next(
        index for index, principal in enumerate(roster) if principal.opaque_id == "J01"
    )
    roster[judge_index] = replace(
        roster[judge_index], **{attribute: getattr(source, attribute)}
    )

    with pytest.raises(ValueError, match=attribute):
        validate_role_separation(roster)


def test_live_scoring_requires_two_primary_judges() -> None:
    roster = [principal for principal in _valid_roster() if principal.opaque_id != "J02"]

    with pytest.raises(ValueError, match="two primary judges"):
        validate_role_separation(roster)


def test_primary_judges_must_be_non_openai() -> None:
    roster = _valid_roster()
    judge_index = next(
        index for index, principal in enumerate(roster) if principal.opaque_id == "J02"
    )
    roster[judge_index] = replace(
        roster[judge_index],
        model_id="openai/gpt-5.4",
        canonical_slug="openai/gpt-5.4-20260423",
        vendor="openai",
        family="gpt-5.4",
    )

    with pytest.raises(ValueError, match="non-OpenAI"):
        validate_role_separation(roster)


@pytest.mark.parametrize("attribute", ["vendor", "family"])
def test_primary_judges_are_mutually_disjoint(attribute: str) -> None:
    roster = _valid_roster()
    first = next(principal for principal in roster if principal.opaque_id == "J01")
    second_index = next(
        index for index, principal in enumerate(roster) if principal.opaque_id == "J02"
    )
    roster[second_index] = replace(
        roster[second_index], **{attribute: getattr(first, attribute)}
    )

    with pytest.raises(ValueError, match=attribute):
        validate_role_separation(roster)


def _catalog() -> dict[str, object]:
    return {
        "data": [
            {
                "id": "openai/gpt-5.5",
                "canonical_slug": "openai/gpt-5.5-20260423",
                "vendor": "openai",
                "family": "gpt-5.5",
            }
        ]
    }


def _principal_config(**overrides: str) -> dict[str, object]:
    row = {
        "opaque_id": "A01",
        "role": "evaluation",
        "model_id": "openai/gpt-5.5",
        "canonical_slug": "OPENAI/GPT-5.5-20260423",
        "vendor": "OpenAI",
        "family": "GPT-5.5",
        **overrides,
    }
    return {"principals": [row]}


def test_principals_are_resolved_from_catalog_identity_data() -> None:
    resolved = resolve_principals(_principal_config(), _catalog())

    assert resolved == (
        _principal(
            "A01",
            "evaluation",
            "openai/gpt-5.5",
            "openai/gpt-5.5-20260423",
            "openai",
            "gpt-5.5",
        ),
    )


@pytest.mark.parametrize(
    ("field", "inconsistent"),
    [
        ("canonical_slug", "openai/gpt-5.5-wrong-snapshot"),
        ("vendor", "friendly-lab-label"),
        ("family", "friendly-family-label"),
    ],
)
def test_config_identity_labels_cannot_contradict_catalog(
    field: str, inconsistent: str
) -> None:
    with pytest.raises(ValueError, match=field):
        resolve_principals(_principal_config(**{field: inconsistent}), _catalog())


@pytest.mark.parametrize("field", ["canonical_slug", "vendor", "family"])
def test_catalog_identity_fields_must_be_exact_and_nonblank(field: str) -> None:
    catalog = _catalog()
    catalog["data"][0][field] = " "  # type: ignore[index]

    with pytest.raises(ValueError, match=field):
        resolve_principals(_principal_config(), catalog)
