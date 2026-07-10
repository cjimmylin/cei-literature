"""Fail-closed validation of an explicitly proposed independent-family panel."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence, Tuple

from canonical import CanonicalSnapshot
from families import FamilyRegistry
from provenance import AssignmentProvenance, ResolutionStatus


class ScheduleError(ValueError):
    """The proposed assignment is not authorized to reach a provider."""

    def __init__(self, detail: str, context: Mapping[str, Any] = None) -> None:
        super().__init__(detail)
        self.reason_code = detail.split(":", 1)[0]
        # The caller persists this private record; failures never return a panel.
        self._audit_snapshot = CanonicalSnapshot.capture(
            {
                "approved": False,
                "reason_code": self.reason_code,
                "detail": detail,
                **(dict(context) if context is not None else {}),
            }
        )

    @property
    def audit_record(self) -> dict:
        value = self._audit_snapshot.to_object()
        if not isinstance(value, dict):  # pragma: no cover
            raise AssertionError("schedule failure snapshot invariant")
        return value


@dataclass(frozen=True)
class JudgeCandidate:
    judge_id: str
    raw_model_alias: str
    family_id: str
    registry_version: str

    @classmethod
    def from_alias(
        cls, judge_id: str, alias: str, registry: FamilyRegistry
    ) -> "JudgeCandidate":
        if not isinstance(judge_id, str) or not judge_id.strip():
            raise ScheduleError("judge_id must be non-empty")
        return cls(
            judge_id=judge_id,
            raw_model_alias=alias,
            family_id=registry.resolve(alias),
            registry_version=registry.version,
        )


@dataclass(frozen=True)
class ScheduleDecision:
    """Private audit record for a successful, caller-selected assignment."""

    registry_version: str
    registry_hash: str
    excluded_family_ids: Tuple[str, ...]
    eligible_family_ids: Tuple[str, ...]
    eligible_judge_ids: Tuple[str, ...]
    assigned_judge_ids: Tuple[str, ...]
    assigned_family_ids: Tuple[str, ...]
    _audit_snapshot: CanonicalSnapshot
    approved: bool = True

    def to_dict(self) -> dict:
        context = self._audit_snapshot.to_object()
        if not isinstance(context, dict):  # pragma: no cover
            raise AssertionError("schedule audit snapshot invariant")
        return {
            "registry_version": self.registry_version,
            "registry_hash": self.registry_hash,
            "excluded_family_ids": list(self.excluded_family_ids),
            "eligible_family_ids": list(self.eligible_family_ids),
            "eligible_judge_ids": list(self.eligible_judge_ids),
            "assigned_judge_ids": list(self.assigned_judge_ids),
            "assigned_family_ids": list(self.assigned_family_ids),
            **context,
            "approved": self.approved,
        }

    @property
    def material_generation_families(self) -> Tuple[dict, ...]:
        return tuple(self.to_dict()["material_generation_families"])

    @property
    def tested_response(self) -> dict:
        return self.to_dict()["tested_response"]

    @property
    def judge_roster(self) -> Tuple[dict, ...]:
        return tuple(self.to_dict()["judge_roster"])

    @property
    def assigned_judges(self) -> Tuple[dict, ...]:
        return tuple(self.to_dict()["assigned_judges"])


def _role_audit(record) -> dict:
    return {
        "role_id": record.role_id,
        "raw_model_alias": record.raw_model_alias,
        "family_id": record.family_id,
        "source_hash": record.source_hash,
        "content_hash": record.content_hash,
        "resolution_status": record.resolution_status.value,
    }


def _judge_audit(candidate: JudgeCandidate) -> dict:
    return {
        "judge_id": candidate.judge_id,
        "raw_model_alias": candidate.raw_model_alias,
        "family_id": candidate.family_id,
    }


def schedule_panel(
    registry: FamilyRegistry,
    provenance: AssignmentProvenance,
    roster: Sequence[JudgeCandidate],
    assigned_judge_ids: Sequence[str],
) -> ScheduleDecision:
    """Validate a proposed panel; this function never chooses models or workloads."""

    context = {
        "provenance_registry_hash": provenance.registry_hash,
        "active_registry_hash": registry.registry_hash,
        "material_generation_families": [
            _role_audit(record) for record in provenance.material_generation_families
        ],
        "tested_response": _role_audit(provenance.tested_response),
        "judge_roster": [_judge_audit(candidate) for candidate in roster],
    }

    def failure(detail: str) -> ScheduleError:
        return ScheduleError(detail, context)

    if provenance.registry_hash != registry.registry_hash:
        raise failure("registry_hash mismatch")
    if provenance.registry_version != registry.version:
        raise failure("registry_version mismatch")
    required = set(provenance.required_material_roles)
    present = {record.role_id for record in provenance.material_generation_families}
    if required != present:
        missing = sorted(required - present)
        extra = sorted(present - required)
        raise failure(
            f"material_role_manifest_mismatch:missing={missing}:extra={extra}"
        )

    excluded = set()
    for record in provenance.material_generation_families:
        if record.resolution_status is ResolutionStatus.UNRESOLVED:
            raise failure(f"unresolved_material_role:{record.role_id}")
        if record.resolution_status is ResolutionStatus.RESOLVED:
            if record.family_id is None or not registry.contains_family(record.family_id):
                raise failure(f"unknown_material_family:{record.role_id}")
            # Re-resolve at the execution boundary; no stale, analyst-resolved IDs.
            if registry.resolve(record.raw_model_alias) != record.family_id:
                raise failure(f"material_family_mismatch:{record.role_id}")
            excluded.add(record.family_id)

    tested = provenance.tested_response
    if tested.resolution_status is ResolutionStatus.UNRESOLVED:
        raise failure("unresolved_tested_response_family")
    if tested.resolution_status is ResolutionStatus.RESOLVED:
        if tested.family_id is None or not registry.contains_family(tested.family_id):
            raise failure("unknown_tested_response_family")
        if registry.resolve(tested.raw_model_alias) != tested.family_id:
            raise failure("tested_response_family_mismatch")
        excluded.add(tested.family_id)

    roster_by_id = {}
    for candidate in roster:
        if candidate.judge_id in roster_by_id:
            raise failure(f"duplicate_judge_id:{candidate.judge_id}")
        if candidate.registry_version != registry.version:
            raise failure(f"judge_registry_version:{candidate.judge_id}")
        if registry.resolve(candidate.raw_model_alias) != candidate.family_id:
            raise failure(f"judge_family_mismatch:{candidate.judge_id}")
        roster_by_id[candidate.judge_id] = candidate

    eligible = {
        judge_id: candidate
        for judge_id, candidate in roster_by_id.items()
        if candidate.family_id not in excluded
    }
    eligible_families = {candidate.family_id for candidate in eligible.values()}
    if len(eligible_families) < 2:
        raise failure(
            f"eligible_family_count:{len(eligible_families)}:requires_at_least_2"
        )

    assigned_ids = tuple(assigned_judge_ids)
    if len(assigned_ids) != len(set(assigned_ids)):
        raise failure("duplicate_assigned_judge")
    assigned = []
    for judge_id in assigned_ids:
        if judge_id not in roster_by_id:
            raise failure(f"assigned_judge_not_in_roster:{judge_id}")
        candidate = roster_by_id[judge_id]
        if judge_id not in eligible:
            raise failure(
                f"assigned_ineligible_family:{judge_id}:{candidate.family_id}"
            )
        assigned.append(candidate)
    assigned_families = {candidate.family_id for candidate in assigned}
    if len(assigned_families) < 2:
        raise failure(
            f"assigned_family_count:{len(assigned_families)}:requires_at_least_2"
        )

    return ScheduleDecision(
        registry_version=registry.version,
        registry_hash=registry.registry_hash,
        excluded_family_ids=tuple(sorted(excluded)),
        eligible_family_ids=tuple(sorted(eligible_families)),
        eligible_judge_ids=tuple(sorted(eligible)),
        assigned_judge_ids=assigned_ids,
        assigned_family_ids=tuple(sorted(assigned_families)),
        _audit_snapshot=CanonicalSnapshot.capture(
            {
                **context,
                "assigned_judges": [
                    _judge_audit(candidate) for candidate in assigned
                ],
            }
        ),
    )
