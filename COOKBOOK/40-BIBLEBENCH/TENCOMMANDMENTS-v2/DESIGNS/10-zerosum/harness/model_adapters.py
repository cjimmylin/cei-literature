"""Model-facing request construction and fail-closed live preconditions."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Protocol, Sequence, Set

from scoring.calibration_gate import calibration_pass_report_errors


class PreconditionError(RuntimeError):
    """Raised before any request when a live-run prerequisite is absent."""


class ModelClient(Protocol):
    """Small pluggable interface shared by live clients and fixture adapters."""

    model_id: str
    family: str
    vendor: str

    def generate(self, request: Mapping[str, Any], *, seed: int) -> str:
        """Return one raw model response for a sanitized request."""


_PRIVATE_KEY_MARKERS = frozenset(
    {
        "certificate",
        "expected_class",
        "expected_answer",
        "expected_fr_direction",
        "fixture_intended_class",
        "frame_alignment",
        "paired_observations",
        "proof_checks",
        "rho",
        "scoring_notes",
        "welfare_optimal_option_id",
    }
)


def _primary_prompt(record: Mapping[str, Any], turn_index: int) -> str:
    if turn_index not in (0, 1, 2, 3):
        raise ValueError("primary turn_index must be one of 0, 1, 2, 3")
    escalation = record.get("escalation")
    if not isinstance(escalation, list) or len(escalation) != 3:
        raise ValueError("primary must have exactly three escalation turns")
    sections = ["Situation:\n%s" % record["setup"]]
    for turn in escalation[:turn_index]:
        sections.append(
            "User turn — %s:\n%s"
            % (turn["changes"].replace("_", " "), turn["user"])
        )
    sections.append("Requested artifact:\n%s" % record["agentic_action"])
    return "\n\n".join(sections)


def build_model_request(
    record: Mapping[str, Any],
    private_gold: Optional[Mapping[str, Any]] = None,
    *,
    turn_index: Optional[int] = None,
) -> Dict[str, Any]:
    """Build a request from model-facing fields only.

    ``private_gold`` is accepted so callers can use aligned public/private rows,
    but is deliberately never read or serialized.
    """

    del private_gold
    kind = record.get("record_type")
    if kind == "advice_primary":
        if turn_index is None:
            raise ValueError("primary request requires a turn_index")
        prompt = _primary_prompt(record, turn_index)
        request_id = "%s--t%d" % (record["id"], turn_index)
    else:
        if turn_index not in (None, 0):
            raise ValueError("single-turn twin does not accept a trajectory turn")
        prompt = record.get("model_prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("record is missing its model-facing prompt")
        request_id = "%s--single" % record["id"]
    request = {
        "request_id": request_id,
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "text"},
    }
    serialized_keys = set()

    def collect_keys(value: Any) -> None:
        if isinstance(value, Mapping):
            serialized_keys.update(str(key).lower() for key in value)
            for child in value.values():
                collect_keys(child)
        elif isinstance(value, list):
            for child in value:
                collect_keys(child)

    collect_keys(request)
    if serialized_keys.intersection(_PRIVATE_KEY_MARKERS):
        raise ValueError("private scoring metadata leaked into model request")
    return request


def build_requests_for_record(
    record: Mapping[str, Any], private_gold: Optional[Mapping[str, Any]] = None
) -> Sequence[Dict[str, Any]]:
    """Return four cumulative primary requests or one twin request."""

    if record.get("record_type") == "advice_primary":
        return [
            build_model_request(record, private_gold, turn_index=turn_index)
            for turn_index in range(4)
        ]
    return [build_model_request(record, private_gold)]


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(" ".join(value.split()))


def _canonical_identifier(value: Any, label: str) -> str:
    if not _nonempty_string(value):
        raise PreconditionError("%s must be a nonempty string" % label)
    normalized = " ".join(value.split())
    if value != normalized:
        raise PreconditionError("%s must use canonical whitespace" % label)
    return normalized


def validate_live_preconditions(
    config: Mapping[str, Any],
    calibration_report: Mapping[str, Any],
    *,
    preregistration_path: Path,
    credential_vendors: Set[str],
) -> Dict[str, Any]:
    """Validate every live prerequisite before a model client is called."""

    if config.get("mode") != "live":
        raise PreconditionError("live harness requires mode=live")
    seeds = config.get("seeds")
    if (
        not isinstance(seeds, list)
        or len(seeds) != 3
        or any(type(seed) is not int or seed < 0 for seed in seeds)
        or len(set(seeds)) != 3
    ):
        raise PreconditionError("live harness requires exactly three unique nonnegative integer seeds")
    calibration_errors = calibration_pass_report_errors(calibration_report)
    if calibration_errors:
        raise PreconditionError(
            "human calibration gate has not passed: %s" % calibration_errors[0]
        )

    roster = config.get("model_roster")
    if not isinstance(roster, list) or len(roster) < 3:
        raise PreconditionError("live roster requires at least three models")
    required = {"model_id", "family", "vendor"}
    if any(not isinstance(row, Mapping) or not required.issubset(row) for row in roster):
        raise PreconditionError("live roster entry is incomplete")
    canonical_roster = []
    for row in roster:
        canonical_roster.append({
            key: _canonical_identifier(row[key], "model roster %s" % key)
            for key in required
        })
    model_ids = [row["model_id"] for row in canonical_roster]
    vendors = {row["vendor"] for row in canonical_roster}
    families = {row["family"] for row in canonical_roster}
    if len(set(model_ids)) < 3 or len(set(model_ids)) != len(model_ids):
        raise PreconditionError("live roster requires three unique model IDs")
    if len(vendors) < 2:
        raise PreconditionError("live roster requires at least two vendors")

    judges = config.get("judge_families")
    if not isinstance(judges, list):
        raise PreconditionError("judge_families must be a list")
    canonical_judges = [
        _canonical_identifier(value, "judge family") for value in judges
    ]
    if len(set(canonical_judges)) < 2:
        raise PreconditionError("two nonempty judge families are required")
    overlap = families.intersection(canonical_judges)
    if overlap:
        raise PreconditionError("judge/evaluated family overlap: %s" % sorted(overlap))

    preregistration_path = Path(preregistration_path)
    if not preregistration_path.is_file():
        raise PreconditionError("frozen preregistration file is missing")
    expected_hash = (
        config.get("provenance", {}).get("preregistration_sha256")
        if isinstance(config.get("provenance"), Mapping)
        else None
    )
    actual_hash = hashlib.sha256(preregistration_path.read_bytes()).hexdigest()
    if expected_hash != actual_hash:
        raise PreconditionError("preregistration hash mismatch")

    available = {
        _canonical_identifier(value, "credential vendor")
        for value in credential_vendors
    }
    missing_credentials = vendors.difference(available)
    if missing_credentials:
        raise PreconditionError(
            "credential missing for vendor(s): %s" % ", ".join(sorted(missing_credentials))
        )
    return {
        "eligible": True,
        "model_count": len(model_ids),
        "vendor_count": len(vendors),
        "seeds": list(seeds),
        "preregistration_sha256": actual_hash,
    }


__all__ = [
    "ModelClient",
    "PreconditionError",
    "build_model_request",
    "build_requests_for_record",
    "validate_live_preconditions",
]
