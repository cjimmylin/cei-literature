"""Output-schema validation for scored-item records and per-design reports.

Keeps the run output well-formed so O4/O5 analysis can rely on structure. Each
scored-item record must carry: identity, the administration responses, a four-way
refusal tag, and a two-judge report; design-specific requirements add on top
(05 -> allocation parse; per_turn/per_seat designs -> unit-level scores).
"""
from __future__ import annotations

from typing import List

from .rubrics import ScoringSpec

_BASE_REQUIRED = ["item_id", "design", "model", "administrations", "refusal_tag",
                  "judge_report"]

# PR-3 R3 fields — every scored record decouples the scalar from verdicts[0] and retains
# the raw refusal signal. `scalar_adjudicated` may be None (disagreement); it must be
# PRESENT. `scalar_by_judge` carries one diagnostic scalar per judge.
_PR3_REQUIRED = ["scalar_by_judge", "refusal_lexical"]


def validate_scored_item(record: dict, spec: ScoringSpec) -> List[str]:
    errors: List[str] = []
    for f in _BASE_REQUIRED:
        if f not in record:
            errors.append(f"missing required field: {f}")
    for f in _PR3_REQUIRED:
        if f not in record:
            errors.append(f"missing PR-3 field: {f}")
    sbj = record.get("scalar_by_judge")
    if sbj is not None and (not isinstance(sbj, list) or len(sbj) < 2):
        errors.append("scalar_by_judge must be a per-judge list of >= 2 scalars")

    jr = record.get("judge_report")
    if isinstance(jr, dict):
        if len(jr.get("verdicts", [])) < 2:
            errors.append("judge_report must carry >= 2 verdicts (cross-family)")
        if "disagreements" not in jr:
            errors.append("judge_report missing disagreements log")
    elif "judge_report" in record:
        errors.append("judge_report must be an object")

    # design-specific
    if spec.design.startswith("05") and "allocation" not in record:
        errors.append("05 record missing allocation parse")
    if spec.unit == "per_turn" and "per_turn_scores" not in record and \
            not _verdicts_have_per_unit(record):
        errors.append("per_turn design record missing per-turn scores")
    if spec.unit == "per_seat" and "per_seat_scores" not in record and \
            not _verdicts_have_per_unit(record):
        errors.append("per_seat design record missing per-seat scores")
    if spec.unit == "per_admin" and not _verdicts_have_per_unit(record):
        errors.append("per_admin (paired twin) design record missing per-administration scores")
    return errors


def _verdicts_have_per_unit(record: dict) -> bool:
    jr = record.get("judge_report") or {}
    return any(v.get("per_unit") for v in jr.get("verdicts", []) if isinstance(v, dict))


_REPORT_REQUIRED = ["design", "n_items", "primary_metric", "per_area",
                    "refusal_accounting", "judge_disagreement_rate"]


def validate_design_report(report: dict) -> List[str]:
    errors = [f"missing report field: {f}" for f in _REPORT_REQUIRED if f not in report]
    return errors
