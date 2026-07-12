from __future__ import annotations

from dataclasses import dataclass, fields, replace
from typing import Any

from biblebench_pilot.contracts import canonical_sha256


@dataclass(frozen=True)
class EpisodeSeed:
    seed_id: str
    facts: dict[str, Any]
    actor_role: str
    authorized_actions: tuple[str, ...]
    affected_parties: tuple[str, ...]
    expected_state: dict[str, Any]
    monitoring: bool = True
    pressure: int = 0
    mode: str = "action"


@dataclass(frozen=True)
class TransformSpec:
    transform_id: str
    updates: dict[str, Any]
    invariant_fields: tuple[str, ...]


@dataclass(frozen=True)
class CapabilityTwinProfile:
    twin_id: str
    mode: str
    tools: tuple[str, ...]
    action_schema: dict[str, Any]
    context_length_band: tuple[int, int]
    timing_budget_ms: int
    task_success_target: str
    ethical_conflict: bool


def apply_transform(seed: EpisodeSeed, spec: TransformSpec) -> EpisodeSeed:
    seed_fields = {field.name for field in fields(EpisodeSeed)}

    for field_name in spec.invariant_fields:
        if field_name not in seed_fields:
            raise ValueError(f"unknown invariant field: {field_name}")
    for field_name in spec.updates:
        if field_name not in seed_fields:
            raise ValueError(f"unknown update field: {field_name}")

    invariant_values = {
        field_name: getattr(seed, field_name)
        for field_name in spec.invariant_fields
    }
    transformed = replace(seed, **spec.updates)

    for field_name, original_value in invariant_values.items():
        if getattr(transformed, field_name) != original_value:
            raise ValueError(f"transform changed invariant field: {field_name}")

    return transformed


_CAPABILITY_FIELDS = (
    "mode",
    "tools",
    "action_schema",
    "context_length_band",
    "timing_budget_ms",
    "task_success_target",
)


def certify_capability_twin(
    moral: CapabilityTwinProfile,
    neutral: CapabilityTwinProfile,
) -> None:
    for field_name in _CAPABILITY_FIELDS:
        if getattr(moral, field_name) != getattr(neutral, field_name):
            raise ValueError(f"capability twin mismatch: {field_name}")

    if moral.ethical_conflict == neutral.ethical_conflict:
        raise ValueError("capability twin mismatch: ethical_conflict")


def stable_episode_id(
    *,
    core_id: str,
    private_template_id: str,
    private_template_version: str,
    split: str,
    mode: str,
    transform_ids: tuple[str, ...],
) -> str:
    scalar_fields = {
        "core_id": core_id,
        "private_template_id": private_template_id,
        "private_template_version": private_template_version,
        "split": split,
        "mode": mode,
    }
    for field_name, value in scalar_fields.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a nonempty string")

    if not isinstance(transform_ids, tuple) or any(
        not isinstance(transform_id, str) or not transform_id.strip()
        for transform_id in transform_ids
    ):
        raise ValueError("transform_ids must contain only nonempty strings")

    payload = {
        "core_id": core_id,
        "private_template_id": private_template_id,
        "private_template_version": private_template_version,
        "split": split,
        "mode": mode,
        "transform_ids": list(transform_ids),
    }
    return canonical_sha256(payload)[:16]
