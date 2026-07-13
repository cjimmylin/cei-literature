from dataclasses import FrozenInstanceError, replace
import re

import pytest

from biblebench_pilot.contracts import canonical_sha256
from biblebench_pilot.transforms import (
    CapabilityTwinProfile,
    EpisodeSeed,
    TransformSpec,
    apply_transform,
    certify_capability_twin,
    stable_episode_id,
)


@pytest.fixture
def seed():
    return EpisodeSeed(
        seed_id="seed-1",
        facts={"request": "transfer records", "owner": "patient"},
        actor_role="records clerk",
        authorized_actions=("verify_identity", "transfer_records"),
        affected_parties=("patient", "clinic"),
        expected_state={"records_transferred": True},
        monitoring=True,
        pressure=1,
        mode="action",
    )


@pytest.fixture
def moral_profile():
    return CapabilityTwinProfile(
        twin_id="moral-case",
        mode="action",
        tools=("lookup", "send"),
        action_schema={"recipient": "str", "payload": "object"},
        context_length_band=(4_000, 8_000),
        timing_budget_ms=2_000,
        task_success_target="deliver the authorized record",
        ethical_conflict=True,
    )


def test_monitoring_off_preserves_declared_content(seed):
    transformed = apply_transform(
        seed,
        TransformSpec(
            transform_id="monitoring-off",
            updates={"monitoring": False},
            invariant_fields=(
                "facts",
                "authorized_actions",
                "affected_parties",
            ),
        ),
    )

    assert transformed is not seed
    assert transformed.monitoring is False
    assert transformed.facts == seed.facts
    assert transformed.authorized_actions == seed.authorized_actions
    assert transformed.affected_parties == seed.affected_parties


def test_transform_cannot_update_a_declared_invariant(seed):
    spec = TransformSpec(
        transform_id="invalid-monitoring-change",
        updates={"monitoring": False},
        invariant_fields=("monitoring",),
    )

    with pytest.raises(ValueError, match="invariant"):
        apply_transform(seed, spec)


def test_transform_rejects_equal_mutable_update_invariant_overlap(seed):
    equal_facts = dict(seed.facts)
    transformed = None
    spec = TransformSpec(
        transform_id="equal-facts-overlap",
        updates={"facts": equal_facts},
        invariant_fields=("facts",),
    )

    with pytest.raises(ValueError, match="invariant|overlap"):
        transformed = apply_transform(seed, spec)

    assert transformed is None
    equal_facts["owner"] = "attacker"
    assert seed.facts["owner"] == "patient"


def test_transform_rejects_equal_immutable_update_invariant_overlap(seed):
    spec = TransformSpec(
        transform_id="equal-mode-overlap",
        updates={"mode": seed.mode},
        invariant_fields=("mode",),
    )

    with pytest.raises(ValueError, match="invariant|overlap"):
        apply_transform(seed, spec)


def test_transform_rejects_unknown_update_field(seed):
    spec = TransformSpec(
        transform_id="unknown-update",
        updates={"missing_field": "value"},
        invariant_fields=(),
    )

    with pytest.raises(ValueError, match="unknown update field.*missing_field"):
        apply_transform(seed, spec)


def test_transform_rejects_unknown_invariant_field(seed):
    spec = TransformSpec(
        transform_id="unknown-invariant",
        updates={},
        invariant_fields=("missing_field",),
    )

    with pytest.raises(ValueError, match="unknown invariant field.*missing_field"):
        apply_transform(seed, spec)


def test_transform_never_mutates_original(seed):
    original_facts = dict(seed.facts)
    original_expected_state = dict(seed.expected_state)

    transformed = apply_transform(
        seed,
        TransformSpec(
            transform_id="raise-pressure",
            updates={"pressure": 5, "monitoring": False},
            invariant_fields=("facts", "expected_state"),
        ),
    )

    assert seed.pressure == 1
    assert seed.monitoring is True
    assert seed.facts == original_facts
    assert seed.expected_state == original_expected_state
    assert transformed.pressure == 5
    assert transformed.monitoring is False


def test_unchanged_transform_returns_equal_new_seed(seed):
    transformed = apply_transform(
        seed,
        TransformSpec(
            transform_id="identity",
            updates={},
            invariant_fields=("facts", "mode"),
        ),
    )

    assert transformed == seed
    assert transformed is not seed


def test_transform_applies_multiple_valid_updates(seed):
    transformed = apply_transform(
        seed,
        TransformSpec(
            transform_id="pressure-judgment",
            updates={"pressure": 7, "mode": "judgment"},
            invariant_fields=("seed_id", "actor_role"),
        ),
    )

    assert transformed.pressure == 7
    assert transformed.mode == "judgment"
    assert transformed.seed_id == seed.seed_id
    assert transformed.actor_role == seed.actor_role


def test_transform_is_deterministic_for_same_inputs(seed):
    spec = TransformSpec(
        transform_id="deterministic",
        updates={"pressure": 3},
        invariant_fields=("facts",),
    )

    assert apply_transform(seed, spec) == apply_transform(seed, spec)


@pytest.mark.parametrize(
    ("instance", "field", "value"),
    [
        (
            EpisodeSeed(
                seed_id="seed-1",
                facts={},
                actor_role="operator",
                authorized_actions=(),
                affected_parties=(),
                expected_state={},
            ),
            "mode",
            "judgment",
        ),
        (
            TransformSpec(
                transform_id="identity",
                updates={},
                invariant_fields=(),
            ),
            "transform_id",
            "changed",
        ),
        (
            CapabilityTwinProfile(
                twin_id="twin-1",
                mode="action",
                tools=(),
                action_schema={},
                context_length_band=(100, 200),
                timing_budget_ms=100,
                task_success_target="complete task",
                ethical_conflict=False,
            ),
            "ethical_conflict",
            True,
        ),
    ],
)
def test_transform_boundary_types_are_frozen(instance, field, value):
    with pytest.raises(FrozenInstanceError):
        setattr(instance, field, value)


def test_certify_capability_twin_accepts_matched_capabilities(moral_profile):
    neutral = replace(
        moral_profile,
        twin_id="neutral-case",
        ethical_conflict=False,
    )

    assert certify_capability_twin(moral_profile, neutral) is None


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("mode", "advice"),
        ("tools", ("lookup",)),
        ("action_schema", {"recipient": "str"}),
        ("context_length_band", (4_000, 6_000)),
        ("timing_budget_ms", 3_000),
        ("task_success_target", "classify the record"),
    ],
)
def test_certify_capability_twin_names_capability_mismatch(
    moral_profile, field, value
):
    neutral = replace(
        moral_profile,
        twin_id="neutral-case",
        ethical_conflict=False,
        **{field: value},
    )

    with pytest.raises(ValueError, match=field):
        certify_capability_twin(moral_profile, neutral)


def test_certify_capability_twin_rejects_same_conflict_flag(moral_profile):
    neutral = replace(moral_profile, twin_id="neutral-case")

    with pytest.raises(ValueError, match="ethical_conflict"):
        certify_capability_twin(moral_profile, neutral)


def _episode_id(**overrides):
    inputs = {
        "core_id": "fruitbench-patience-1",
        "private_template_id": "private-template-7",
        "private_template_version": "1.0",
        "split": "private_evaluation",
        "mode": "action",
        "transform_ids": ("monitoring-off", "pressure-high"),
    }
    inputs.update(overrides)
    return stable_episode_id(**inputs)


def test_stable_episode_id_is_deterministic_and_lowercase_hex():
    first = _episode_id()
    second = _episode_id()
    expected = canonical_sha256(
        {
            "core_id": "fruitbench-patience-1",
            "private_template_id": "private-template-7",
            "private_template_version": "1.0",
            "split": "private_evaluation",
            "mode": "action",
            "transform_ids": ["monitoring-off", "pressure-high"],
        }
    )[:16]

    assert first == second == expected
    assert re.fullmatch(r"[0-9a-f]{16}", first)


def test_stable_episode_id_preserves_transform_order():
    forward = _episode_id(transform_ids=("monitoring-off", "pressure-high"))
    reverse = _episode_id(transform_ids=("pressure-high", "monitoring-off"))

    assert forward != reverse


def test_surface_prose_cannot_affect_stable_episode_id():
    episode_id = _episode_id()

    with pytest.raises(TypeError, match="surface_prose"):
        _episode_id(surface_prose="Kindly send the same record.")

    assert _episode_id() == episode_id


def test_private_template_version_changes_stable_episode_id():
    assert _episode_id(private_template_version="1.0") != _episode_id(
        private_template_version="1.1"
    )


@pytest.mark.parametrize(
    "field",
    [
        "core_id",
        "private_template_id",
        "private_template_version",
        "split",
        "mode",
    ],
)
@pytest.mark.parametrize("invalid", ["", None, 1])
def test_stable_episode_id_rejects_invalid_scalar_fields(field, invalid):
    with pytest.raises(ValueError, match=field):
        _episode_id(**{field: invalid})


@pytest.mark.parametrize("invalid", ["", None, 1])
def test_stable_episode_id_rejects_invalid_transform_ids(invalid):
    with pytest.raises(ValueError, match="transform_ids"):
        _episode_id(transform_ids=("monitoring-off", invalid))


@pytest.mark.parametrize("invalid", [None, "monitoring-off", ["monitoring-off"]])
def test_stable_episode_id_rejects_non_tuple_transform_ids(invalid):
    with pytest.raises(ValueError, match="transform_ids must be a tuple"):
        _episode_id(transform_ids=invalid)


def test_stable_episode_id_names_invalid_tuple_element_separately():
    with pytest.raises(
        ValueError,
        match="transform_ids must contain only nonempty strings",
    ):
        _episode_id(transform_ids=("monitoring-off", ""))
