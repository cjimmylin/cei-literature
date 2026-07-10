"""Cue-surface validation and deterministic counterbalance schedules."""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from types import MappingProxyType
from typing import Collection, Iterable, Mapping, Optional, Tuple


CUE_ARMS = ("C0", "C1", "C2", "C3")
REGISTERED_CUE_CLASSES = frozenset(
    {
        "construct_or_benchmark_label",
        "narrated_motive_or_polarity",
        "permission_prohibition_or_target_action",
        "authority_or_group_identity",
        "order_or_position",
        "register_or_style",
        "provenance_or_disclosure",
        "salience_or_retrieval_distance",
        "monitoring_or_evaluation_awareness",
    }
)

_NULL_FOIL_PATTERN = re.compile(
    r"\b(?:null|foil|neutraliz\w*|inapplicab\w*)\b",
    re.IGNORECASE,
)
_OPAQUE_ACTOR_PATTERN = re.compile(r"A[0-9]{2}\Z")


class CounterbalanceError(ValueError):
    """Raised when cue declarations or a schedule fail closed."""


@dataclass(frozen=True)
class CueSurface:
    item_id: str
    surface_id: str
    cue_arm: str
    kernel_id: str
    text: str
    sealed: bool
    cue_classes: Tuple[str, ...]
    operative_delta: str


@dataclass(frozen=True)
class CompiledSchedule:
    rows: Tuple[Mapping[str, object], ...]
    schedule_hash: str


def _require_nonblank(value: object, field_name: str, surface_id: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise CounterbalanceError(
            f"surface {surface_id!r} requires nonblank {field_name}"
        )


def validate_surface_quartets(
    surfaces: Iterable[CueSurface],
    *,
    registered_cue_classes: Collection[str] = REGISTERED_CUE_CLASSES,
) -> Tuple[CueSurface, ...]:
    """Validate complete C0--C3 declarations and return canonical ordering."""

    rows = tuple(surfaces)
    if not rows:
        raise CounterbalanceError("at least one cue-surface quartet is required")

    known_classes = frozenset(registered_cue_classes)
    seen_surface_ids = set()
    by_item = defaultdict(list)

    for surface in rows:
        if not isinstance(surface, CueSurface):
            raise CounterbalanceError("every cue surface must be a CueSurface")
        _require_nonblank(surface.item_id, "item_id", surface.surface_id)
        _require_nonblank(surface.surface_id, "surface_id", surface.surface_id)
        _require_nonblank(surface.kernel_id, "kernel_id", surface.surface_id)
        _require_nonblank(surface.text, "text", surface.surface_id)
        _require_nonblank(
            surface.operative_delta,
            "operative_delta",
            surface.surface_id,
        )
        if surface.cue_arm not in CUE_ARMS:
            raise CounterbalanceError(
                f"surface {surface.surface_id!r} cue_arm must be one of {CUE_ARMS}"
            )
        if not isinstance(surface.sealed, bool):
            raise CounterbalanceError(
                f"surface {surface.surface_id!r} sealed must be boolean"
            )
        if surface.surface_id in seen_surface_ids:
            raise CounterbalanceError(
                f"cue registry requires unique surface_id values: {surface.surface_id!r}"
            )
        seen_surface_ids.add(surface.surface_id)

        if not surface.cue_classes:
            raise CounterbalanceError(
                f"surface {surface.surface_id!r} must declare at least one cue class"
            )
        if len(set(surface.cue_classes)) != len(surface.cue_classes):
            raise CounterbalanceError(
                f"surface {surface.surface_id!r} contains duplicate cue classes"
            )
        unknown = sorted(set(surface.cue_classes) - known_classes)
        if unknown:
            raise CounterbalanceError(
                f"surface {surface.surface_id!r} has unregistered cue class values: {unknown}"
            )

        by_item[surface.item_id].append(surface)

    for item_id, quartet in by_item.items():
        if len(quartet) != len(CUE_ARMS):
            raise CounterbalanceError(
                f"item {item_id!r} requires a complete C0/C1/C2/C3 quartet"
            )
        arms = [surface.cue_arm for surface in quartet]
        if len(set(arms)) != len(arms):
            raise CounterbalanceError(
                f"item {item_id!r} requires unique cue arms"
            )
        if set(arms) != set(CUE_ARMS):
            raise CounterbalanceError(
                f"item {item_id!r} requires a complete C0/C1/C2/C3 quartet"
            )
        kernels = {surface.kernel_id for surface in quartet}
        if len(kernels) != 1:
            raise CounterbalanceError(
                f"item {item_id!r} quartet must share one kernel_id"
            )

    for surface in rows:
        if surface.cue_arm == "C2" and not _NULL_FOIL_PATTERN.search(
            surface.operative_delta
        ):
            raise CounterbalanceError(
                f"surface {surface.surface_id!r} C2 requires a null/foil declaration"
            )
        if surface.cue_arm == "C3" and not surface.sealed:
            raise CounterbalanceError(
                f"surface {surface.surface_id!r} C3 must be sealed"
            )
        if surface.cue_arm != "C3" and surface.sealed:
            raise CounterbalanceError(
                f"surface {surface.surface_id!r}: only C3 may be sealed"
            )

    arm_order = {arm: index for index, arm in enumerate(CUE_ARMS)}
    return tuple(
        sorted(rows, key=lambda surface: (surface.item_id, arm_order[surface.cue_arm]))
    )


def compile_cue_surfaces(
    surfaces: Iterable[CueSurface],
    *,
    phase: str,
    requested_surface_ids: Optional[Collection[str]] = None,
    development_surface_ids: Optional[Collection[str]] = None,
    registered_cue_classes: Collection[str] = REGISTERED_CUE_CLASSES,
) -> Tuple[CueSurface, ...]:
    """Compile only the cue arms authorized for an execution phase."""

    canonical = validate_surface_quartets(
        surfaces,
        registered_cue_classes=registered_cue_classes,
    )
    if phase == "development":
        allowed_arms = frozenset({"C0", "C1", "C2"})
        phase_label = "development"
    elif phase == "locked-confirmation":
        allowed_arms = frozenset({"C3"})
        phase_label = "locked-confirmation"
        if development_surface_ids is None:
            raise CounterbalanceError(
                "locked-confirmation requires development_surface_ids for reuse checks"
            )
    else:
        raise CounterbalanceError(f"unsupported phase: {phase!r}")

    by_id = {surface.surface_id: surface for surface in canonical}
    expected = tuple(surface for surface in canonical if surface.cue_arm in allowed_arms)
    expected_ids = {surface.surface_id for surface in expected}

    if requested_surface_ids is None:
        selected_ids = expected_ids
    else:
        selected_ids = set(requested_surface_ids)
        unknown = sorted(selected_ids - set(by_id))
        if unknown:
            raise CounterbalanceError(f"unknown requested surface_id values: {unknown}")
        prohibited = [by_id[surface_id] for surface_id in selected_ids - expected_ids]
        if prohibited:
            prohibited_arms = sorted({surface.cue_arm for surface in prohibited})
            if phase == "development" and "C3" in prohibited_arms:
                raise CounterbalanceError("development phase rejects C3 surfaces")
            raise CounterbalanceError("locked-confirmation requires C3 surfaces only")
        if selected_ids != expected_ids:
            raise CounterbalanceError(
                f"{phase_label} requires a complete {phase_label} surface set "
                "for every item"
            )

    if phase == "locked-confirmation":
        reused = sorted(selected_ids & set(development_surface_ids or ()))
        if reused:
            raise CounterbalanceError(
                f"locked-confirmation reuses development-used surface_id values: {reused}"
            )

    return tuple(surface for surface in canonical if surface.surface_id in selected_ids)


def _canonical_digest(value: object) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_latin_square_schedule(
    *,
    actors: Iterable[str],
    surfaces: Iterable[CueSurface],
    rollouts: int,
    phase: str,
    requested_surface_ids: Optional[Collection[str]] = None,
    development_surface_ids: Optional[Collection[str]] = None,
    development_schedule_hashes: Optional[Collection[str]] = None,
    registered_cue_classes: Collection[str] = REGISTERED_CUE_CLASSES,
) -> CompiledSchedule:
    """Build and seal a deterministic cyclic Latin-square assignment schedule."""

    actor_ids = tuple(actors)
    if not actor_ids:
        raise CounterbalanceError("schedule requires at least one actor")
    for actor_id in actor_ids:
        if not isinstance(actor_id, str) or _OPAQUE_ACTOR_PATTERN.fullmatch(actor_id) is None:
            raise CounterbalanceError("schedule actor_id values must be opaque A## identifiers")
    if len(set(actor_ids)) != len(actor_ids):
        raise CounterbalanceError("schedule requires unique actor_id values")
    if isinstance(rollouts, bool) or not isinstance(rollouts, int) or rollouts <= 0:
        raise CounterbalanceError("rollouts must be a positive integer")
    if phase == "locked-confirmation" and development_schedule_hashes is None:
        raise CounterbalanceError(
            "locked-confirmation requires development_schedule_hashes for reuse checks"
        )

    compiled = compile_cue_surfaces(
        surfaces,
        phase=phase,
        requested_surface_ids=requested_surface_ids,
        development_surface_ids=development_surface_ids,
        registered_cue_classes=registered_cue_classes,
    )
    by_item = defaultdict(list)
    for surface in compiled:
        by_item[surface.item_id].append(surface)

    item_ids = sorted(by_item)
    eligible_count = len(by_item[item_ids[0]])
    if eligible_count > 1 and rollouts % eligible_count:
        raise CounterbalanceError(
            f"rollouts must be divisible by {eligible_count} for per-arm position balance"
        )

    arm_order = {arm: index for index, arm in enumerate(CUE_ARMS)}
    for item_id in item_ids:
        by_item[item_id].sort(key=lambda surface: arm_order[surface.cue_arm])
        if len(by_item[item_id]) != eligible_count:
            raise CounterbalanceError(
                "every item must expose the same number of eligible cue arms"
            )

    rows = []
    assignment_ids = set()
    for actor_index, actor_id in enumerate(sorted(actor_ids)):
        for item_index, item_id in enumerate(item_ids):
            item_surfaces = by_item[item_id]
            for rollout_index in range(rollouts):
                shift = (actor_index + item_index + rollout_index) % eligible_count
                ordered = item_surfaces[shift:] + item_surfaces[:shift]
                for position, surface in enumerate(ordered, start=1):
                    identity = {
                        "actor_id": actor_id,
                        "item_id": item_id,
                        "surface_id": surface.surface_id,
                        "rollout": rollout_index + 1,
                        "position": position,
                    }
                    assignment_id = f"asg-{_canonical_digest(identity)[:20]}"
                    if assignment_id in assignment_ids:
                        raise CounterbalanceError("duplicate assignment_id generated")
                    assignment_ids.add(assignment_id)
                    rows.append({"assignment_id": assignment_id, **identity})

    digest = _canonical_digest(rows)
    if phase == "locked-confirmation" and digest in set(
        development_schedule_hashes or ()
    ):
        raise CounterbalanceError(
            "locked-confirmation reuses a development-used schedule hash"
        )
    frozen_rows = tuple(MappingProxyType(row) for row in rows)
    return CompiledSchedule(rows=frozen_rows, schedule_hash=digest)
