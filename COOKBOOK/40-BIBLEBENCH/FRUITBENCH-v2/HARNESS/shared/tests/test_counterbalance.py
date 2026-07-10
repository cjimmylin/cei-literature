from __future__ import annotations

import importlib
import sys
from collections import Counter
from dataclasses import FrozenInstanceError, replace
from pathlib import Path
from typing import Any

import pytest


HARNESS = Path(__file__).resolve().parents[2]
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))


def _api() -> Any:
    return importlib.import_module("shared.counterbalance")


def _quartet(
    *,
    item_id: str = "item-01",
    kernel_id: str = "kernel-01",
    prefix: str | None = None,
) -> list[Any]:
    api = _api()
    prefix = prefix or item_id
    cue_classes = ("narrated_motive_or_polarity", "order_or_position")
    specifications = (
        ("C0", "Original matched task surface.", False, "original: registered surface"),
        ("C1", "Matched task surface without motive narration.", False, "de-cued: motive narration removed"),
        ("C2", "Matched task surface with no target affordance.", False, "null: target affordance neutralized"),
        ("C3", "Independent sealed realization of the same kernel.", True, "holdout: independently authored realization"),
    )
    return [
        api.CueSurface(
            item_id=item_id,
            surface_id=f"{prefix}-{arm.lower()}",
            cue_arm=arm,
            kernel_id=kernel_id,
            text=text,
            sealed=sealed,
            cue_classes=cue_classes,
            operative_delta=delta,
        )
        for arm, text, sealed, delta in specifications
    ]


def test_cue_surface_is_frozen_and_complete_quartets_are_canonicalized() -> None:
    api = _api()
    surfaces = _quartet()

    canonical = api.validate_surface_quartets(reversed(surfaces))

    assert tuple(surface.cue_arm for surface in canonical) == ("C0", "C1", "C2", "C3")
    assert canonical[2].operative_delta.startswith("null:")
    with pytest.raises(FrozenInstanceError):
        canonical[0].text = "mutated"


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (lambda rows: rows[:-1], "complete C0/C1/C2/C3 quartet"),
        (
            lambda rows: [*rows[:3], replace(rows[3], cue_arm="C2")],
            "unique cue arms",
        ),
        (
            lambda rows: [*rows[:3], replace(rows[3], kernel_id="other-kernel")],
            "one kernel_id",
        ),
        (
            lambda rows: [*rows[:2], replace(rows[2], operative_delta="affordance changed"), *rows[3:]],
            "null/foil",
        ),
        (
            lambda rows: [replace(rows[0], sealed=True), *rows[1:]],
            "only C3",
        ),
        (
            lambda rows: [*rows[:3], replace(rows[3], sealed=False)],
            "C3 must be sealed",
        ),
        (
            lambda rows: [*rows[:3], replace(rows[3], sealed="yes")],
            "sealed must be boolean",
        ),
        (
            lambda rows: [replace(rows[0], text="   "), *rows[1:]],
            "nonblank text",
        ),
        (
            lambda rows: [replace(rows[0], operative_delta=""), *rows[1:]],
            "nonblank operative_delta",
        ),
        (
            lambda rows: [replace(rows[0], cue_classes=("invented-cue",)), *rows[1:]],
            "unregistered cue class",
        ),
        (
            lambda rows: [replace(rows[0], cue_classes=()), *rows[1:]],
            "at least one cue class",
        ),
    ],
)
def test_quartet_validation_rejects_invalid_declarations(mutate: Any, message: str) -> None:
    api = _api()

    with pytest.raises(api.CounterbalanceError, match=message):
        api.validate_surface_quartets(mutate(_quartet()))


def test_quartet_validation_rejects_duplicate_surface_ids_globally() -> None:
    api = _api()
    first = _quartet(item_id="item-01", kernel_id="kernel-01")
    second = _quartet(item_id="item-02", kernel_id="kernel-02")
    second[0] = replace(second[0], surface_id=first[0].surface_id)

    with pytest.raises(api.CounterbalanceError, match="unique surface_id"):
        api.validate_surface_quartets([*first, *second])


def test_quartet_validation_rejects_blank_identifiers_and_unknown_arms() -> None:
    api = _api()
    rows = _quartet()

    with pytest.raises(api.CounterbalanceError, match="nonblank item_id"):
        api.validate_surface_quartets([replace(rows[0], item_id=" "), *rows[1:]])
    with pytest.raises(api.CounterbalanceError, match="cue_arm must be one of"):
        api.validate_surface_quartets([replace(rows[0], cue_arm="CX"), *rows[1:]])


def test_development_compiler_exposes_c0_c1_c2_and_rejects_c3_requests() -> None:
    api = _api()
    registry = _quartet()

    compiled = api.compile_cue_surfaces(registry, phase="development")

    assert tuple(surface.cue_arm for surface in compiled) == ("C0", "C1", "C2")
    assert all(not surface.sealed for surface in compiled)
    with pytest.raises(api.CounterbalanceError, match="development phase rejects C3"):
        api.compile_cue_surfaces(
            registry,
            phase="development",
            requested_surface_ids=(registry[3].surface_id,),
        )


def test_locked_confirmation_requires_only_unused_c3_surfaces() -> None:
    api = _api()
    registry = _quartet()
    development_ids = {surface.surface_id for surface in registry[:3]}

    with pytest.raises(api.CounterbalanceError, match="development_surface_ids"):
        api.compile_cue_surfaces(registry, phase="locked-confirmation")

    compiled = api.compile_cue_surfaces(
        registry,
        phase="locked-confirmation",
        development_surface_ids=development_ids,
    )

    assert tuple(surface.cue_arm for surface in compiled) == ("C3",)
    with pytest.raises(api.CounterbalanceError, match="development-used surface_id"):
        api.compile_cue_surfaces(
            registry,
            phase="locked-confirmation",
            development_surface_ids={registry[3].surface_id},
        )
    with pytest.raises(api.CounterbalanceError, match="locked-confirmation requires C3"):
        api.compile_cue_surfaces(
            registry,
            phase="locked-confirmation",
            development_surface_ids=development_ids,
            requested_surface_ids=(registry[0].surface_id,),
        )


def test_compiler_requires_a_complete_phase_surface_set_for_every_item() -> None:
    api = _api()
    first = _quartet(item_id="item-01", kernel_id="kernel-01")
    second = _quartet(item_id="item-02", kernel_id="kernel-02")
    registry = [*first, *second]

    with pytest.raises(api.CounterbalanceError, match="complete development surface set"):
        api.compile_cue_surfaces(
            registry,
            phase="development",
            requested_surface_ids=tuple(surface.surface_id for surface in first[:3]),
        )
    with pytest.raises(api.CounterbalanceError, match="unsupported phase"):
        api.compile_cue_surfaces(registry, phase="preview")


def test_latin_square_schedule_is_stable_and_input_order_independent() -> None:
    api = _api()
    registry = [
        *_quartet(item_id="item-02", kernel_id="kernel-02"),
        *_quartet(item_id="item-01", kernel_id="kernel-01"),
    ]

    first = api.build_latin_square_schedule(
        actors=("A02", "A01"),
        surfaces=registry,
        rollouts=6,
        phase="development",
    )
    second = api.build_latin_square_schedule(
        actors=("A01", "A02"),
        surfaces=reversed(registry),
        rollouts=6,
        phase="development",
    )

    assert first.rows == second.rows
    assert first.schedule_hash == second.schedule_hash
    assert len(first.schedule_hash) == 64
    assert len(first.rows) == 2 * 2 * 3 * 6
    expected_fields = {
        "assignment_id",
        "actor_id",
        "item_id",
        "surface_id",
        "rollout",
        "position",
    }
    assert all(set(row) == expected_fields for row in first.rows)
    assert len({row["assignment_id"] for row in first.rows}) == len(first.rows)
    with pytest.raises(FrozenInstanceError):
        first.schedule_hash = "changed"
    with pytest.raises(TypeError):
        first.rows[0]["actor_id"] = "A99"


def test_every_actor_item_arm_is_count_and_position_balanced() -> None:
    api = _api()
    registry = [
        *_quartet(item_id="item-01", kernel_id="kernel-01"),
        *_quartet(item_id="item-02", kernel_id="kernel-02"),
    ]
    arm_by_surface = {surface.surface_id: surface.cue_arm for surface in registry}

    schedule = api.build_latin_square_schedule(
        actors=("A01", "A02"),
        surfaces=registry,
        rollouts=6,
        phase="development",
    )

    arm_counts = Counter(
        (row["actor_id"], row["item_id"], arm_by_surface[row["surface_id"]])
        for row in schedule.rows
    )
    position_counts = Counter(
        (
            row["actor_id"],
            row["item_id"],
            arm_by_surface[row["surface_id"]],
            row["position"],
        )
        for row in schedule.rows
    )
    rollout_counts = Counter(
        (row["actor_id"], row["item_id"], row["rollout"])
        for row in schedule.rows
    )

    assert set(arm_counts.values()) == {6}
    assert set(position_counts.values()) == {2}
    assert {key[3] for key in position_counts} == {1, 2, 3}
    assert set(rollout_counts.values()) == {3}
    assert {key[2] for key in rollout_counts} == set(range(1, 7))


@pytest.mark.parametrize(
    ("actors", "rollouts", "message"),
    [
        ((), 6, "at least one actor"),
        (("A01", "A01"), 6, "unique actor_id"),
        (("A01",), 0, "positive integer"),
        (("A01",), True, "positive integer"),
        (("A01",), 5, "divisible by 3"),
    ],
)
def test_schedule_rejects_impossible_balance(
    actors: tuple[str, ...], rollouts: Any, message: str
) -> None:
    api = _api()

    with pytest.raises(api.CounterbalanceError, match=message):
        api.build_latin_square_schedule(
            actors=actors,
            surfaces=_quartet(),
            rollouts=rollouts,
            phase="development",
        )


def test_locked_schedule_uses_only_c3_and_rejects_reused_schedule_hash() -> None:
    api = _api()
    registry = _quartet()
    development_surface_ids = {surface.surface_id for surface in registry[:3]}

    with pytest.raises(api.CounterbalanceError, match="development_schedule_hashes"):
        api.build_latin_square_schedule(
            actors=("A01",),
            surfaces=registry,
            rollouts=2,
            phase="locked-confirmation",
            development_surface_ids=development_surface_ids,
        )

    locked = api.build_latin_square_schedule(
        actors=("A01",),
        surfaces=registry,
        rollouts=2,
        phase="locked-confirmation",
        development_surface_ids=development_surface_ids,
        development_schedule_hashes=set(),
    )

    assert {row["surface_id"] for row in locked.rows} == {registry[3].surface_id}
    assert {row["position"] for row in locked.rows} == {1}
    with pytest.raises(api.CounterbalanceError, match="development-used schedule hash"):
        api.build_latin_square_schedule(
            actors=("A01",),
            surfaces=registry,
            rollouts=2,
            phase="locked-confirmation",
            development_surface_ids=development_surface_ids,
            development_schedule_hashes={locked.schedule_hash},
        )
