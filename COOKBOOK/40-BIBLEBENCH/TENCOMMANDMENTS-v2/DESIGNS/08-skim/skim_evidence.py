"""Capability, evidence-basis, realism, and release-budget validation."""

from collections.abc import Mapping as MappingABC
from collections.abc import Sequence as SequenceABC
from dataclasses import dataclass
import math
from types import MappingProxyType
from typing import Any, Mapping, Optional, Sequence

from skim_constants import (
    CAPABILITY_REFERENCE_FIELDS,
    FAMILIES,
    FAMILY_CORE_COUNTS,
    FROZEN_ARTIFACT_HASH_FIELDS,
    REVISION_HISTORY_FIELDS,
)
from skim_hashing import (
    _deep_freeze,
    _finite_real,
    _json_tree_is_finite,
    _nonblank_text,
    _text_sequence,
    _valid_sha256,
    canonical_sha256,
)


def derive_capability_projections(reference: Any) -> Optional[Mapping[str, float]]:
    """Derive frozen PC1 scores from exact complete-case rows and loadings."""

    if not isinstance(reference, MappingABC):
        return None
    try:
        columns_value = reference["benchmark_columns"]
        rows = reference["model_rows"]
        missing_data_rule = reference["missing_data_rule"]
        standardization = reference["standardization"]
        sign = reference["pc1_sign"]
        loadings = reference["pc1_loadings"]
    except (KeyError, TypeError):
        return None
    if (
        isinstance(columns_value, (str, bytes, bytearray))
        or not isinstance(columns_value, SequenceABC)
    ):
        return None
    columns = tuple(columns_value)
    if (
        len(columns) < 2
        or not all(type(column) is str and _nonblank_text(column) for column in columns)
        or len(set(columns)) != len(columns)
        or isinstance(rows, (str, bytes, bytearray))
        or not isinstance(rows, SequenceABC)
        or len(rows) < 3
        or missing_data_rule != "complete_case_no_imputation"
        or not isinstance(standardization, MappingABC)
        or set(standardization) != {"method", "ddof"}
        or standardization["method"] != "z_score"
        or type(standardization["ddof"]) is not int
        or standardization["ddof"] != 0
        or type(sign) is not str
        or not sign.startswith("positive_loading_on:")
        or not isinstance(loadings, MappingABC)
        or set(loadings) != set(columns)
        or not all(_finite_real(loadings[column]) for column in columns)
    ):
        return None
    anchor = sign[len("positive_loading_on:") :]
    if (
        sign != "positive_loading_on:" + anchor
        or anchor not in columns
        or float(loadings[anchor]) <= 0.0
    ):
        return None
    try:
        loading_norm = math.sqrt(
            math.fsum(float(loadings[column]) ** 2 for column in columns)
        )
    except (OverflowError, ValueError):
        return None
    if not math.isfinite(loading_norm) or abs(loading_norm - 1.0) > 1e-12:
        return None

    expected_row_fields = {"model_id", *columns}
    row_ids = []
    column_values = {column: [] for column in columns}
    for row in rows:
        if not isinstance(row, MappingABC) or set(row) != expected_row_fields:
            return None
        model_id = row["model_id"]
        if type(model_id) is not str or not _nonblank_text(model_id):
            return None
        row_ids.append(model_id)
        for column in columns:
            value = row[column]
            if not _finite_real(value):
                return None
            column_values[column].append(float(value))
    if len(set(row_ids)) != len(row_ids):
        return None

    standardized = {model_id: {} for model_id in row_ids}
    try:
        for column in columns:
            values = column_values[column]
            mean = math.fsum(values) / len(values)
            variance = math.fsum((value - mean) ** 2 for value in values) / len(
                values
            )
            if not math.isfinite(variance) or variance <= 0.0:
                return None
            standard_deviation = math.sqrt(variance)
            if not math.isfinite(standard_deviation) or standard_deviation <= 0.0:
                return None
            for model_id, value in zip(row_ids, values):
                z_score = (value - mean) / standard_deviation
                if not math.isfinite(z_score):
                    return None
                standardized[model_id][column] = z_score
        projections = {}
        for model_id in row_ids:
            projection = math.fsum(
                standardized[model_id][column] * float(loadings[column])
                for column in columns
            )
            if not math.isfinite(projection):
                return None
            projections[model_id] = projection
    except (OverflowError, ValueError, ZeroDivisionError):
        return None
    if len(set(projections.values())) < 2:
        return None
    return MappingProxyType(projections)


def hash_capability_reference(reference: Mapping[str, Any]) -> str:
    """Hash every capability-reference field except its self-referential hash."""

    if not isinstance(reference, MappingABC):
        raise TypeError("capability reference must be a mapping")
    payload = {key: value for key, value in reference.items() if key != "content_sha256"}
    return canonical_sha256(payload)


def _capability_reference_valid(
    reference: Any, required_model_ids: Sequence[str] = ()
) -> bool:
    if not isinstance(reference, MappingABC) or not _json_tree_is_finite(reference):
        return False
    if set(reference) != set(CAPABILITY_REFERENCE_FIELDS):
        return False
    if (
        type(reference["schema_version"]) is not int
        or reference["schema_version"] != 1
        or reference["status"] != "FROZEN"
    ):
        return False
    source = reference["source_snapshot"]
    if not isinstance(source, str) or not source.startswith(("https://", "http://")):
        return False
    if not _valid_sha256(reference["source_sha256"]):
        return False

    derived_scores = derive_capability_projections(reference)
    if derived_scores is None:
        return False
    row_ids = tuple(derived_scores)
    scores = reference["projected_scores"]
    if not isinstance(scores, MappingABC) or set(scores) != set(row_ids):
        return False
    if not all(_finite_real(value) for value in scores.values()):
        return False
    if any(
        not math.isclose(
            float(scores[model_id]),
            derived_scores[model_id],
            rel_tol=1e-12,
            abs_tol=1e-12,
        )
        for model_id in row_ids
    ):
        return False
    if len({float(value) for value in derived_scores.values()}) < 2:
        return False
    required = _text_sequence(required_model_ids)
    if required is None or len(set(required)) != len(required):
        return False
    if not set(required).issubset(scores):
        return False
    if required and len({float(derived_scores[model_id]) for model_id in required}) < 2:
        return False
    content_hash = reference["content_sha256"]
    if not _valid_sha256(content_hash):
        return False
    try:
        return content_hash.lower() == hash_capability_reference(reference)
    except Exception:
        return False


def capability_reference_status(
    reference: Any, required_model_ids: Sequence[str] = ()
) -> str:
    """Return COMPLETE or the fail-closed NOT_ESTIMABLE status."""

    return (
        "COMPLETE"
        if _capability_reference_valid(reference, required_model_ids)
        else "NOT_ESTIMABLE"
    )


def validate_capability_reference(
    reference: Any, required_model_ids: Sequence[str] = ()
) -> bool:
    """Return whether the external capability-PC1 record is complete and frozen."""

    return _capability_reference_valid(reference, required_model_ids)


@dataclass(frozen=True)
class EvidenceBasis:
    """Evidence needed for an official SKIM empirical decision.

    Every requirement is checked from exact evidence.  Synthetic and
    diagnostic records remain useful provenance, but can never become official.
    """

    mode: str
    data_basis: str
    professional_realism_status: str
    human_baseline_status: str
    model_ids: Sequence[str]
    vendors: Sequence[str]
    seeds: Sequence[int]
    synthetic: bool
    diagnostic_status: Optional[str]
    frozen_hashes: Mapping[str, str]
    capability_reference: Optional[Mapping[str, Any]]

    def __post_init__(self) -> None:
        if (
            isinstance(self.model_ids, SequenceABC)
            and not isinstance(self.model_ids, (str, bytes, bytearray))
        ):
            object.__setattr__(self, "model_ids", tuple(self.model_ids))
        if (
            isinstance(self.vendors, SequenceABC)
            and not isinstance(self.vendors, (str, bytes, bytearray))
        ):
            object.__setattr__(self, "vendors", tuple(self.vendors))
        if (
            isinstance(self.seeds, SequenceABC)
            and not isinstance(self.seeds, (str, bytes, bytearray))
        ):
            object.__setattr__(self, "seeds", tuple(self.seeds))
        if isinstance(self.frozen_hashes, MappingABC):
            object.__setattr__(self, "frozen_hashes", _deep_freeze(self.frozen_hashes))
        if isinstance(self.capability_reference, MappingABC):
            object.__setattr__(
                self, "capability_reference", _deep_freeze(self.capability_reference)
            )

    @property
    def official_eligible(self) -> bool:
        model_ids = _text_sequence(self.model_ids)
        vendors = _text_sequence(self.vendors)
        roster_valid = (
            model_ids is not None
            and vendors is not None
            and len(model_ids) == len(vendors) == 3
            and len(set(model_ids)) == 3
            and len(set(vendors)) >= 2
        )
        seeds_valid = (
            isinstance(self.seeds, SequenceABC)
            and not isinstance(self.seeds, (str, bytes, bytearray))
            and len(self.seeds) == 3
            and all(
                isinstance(seed, int) and not isinstance(seed, bool) and seed >= 0
                for seed in self.seeds
            )
            and len(set(self.seeds)) == 3
        )
        hashes_valid = (
            isinstance(self.frozen_hashes, MappingABC)
            and set(self.frozen_hashes) == set(FROZEN_ARTIFACT_HASH_FIELDS)
            and all(_valid_sha256(value) for value in self.frozen_hashes.values())
        )
        return (
            self.mode == "live"
            and self.data_basis == "external_model_responses"
            and self.synthetic is False
            and self.diagnostic_status is None
            and self.professional_realism_status == "PASS"
            and self.human_baseline_status == "COMPLETE"
            and roster_valid
            and seeds_valid
            and hashes_valid
            and validate_capability_reference(self.capability_reference, model_ids or ())
        )

    @property
    def eligible_for_empirical_decision(self) -> bool:
        return self.official_eligible


@dataclass(frozen=True)
class ProfessionalRealismResult:
    """Derived result for the raw professional-realism evidence packet."""

    status: str
    family_passing_cores: Mapping[str, int]
    fleiss_kappa: Mapping[str, Optional[float]]
    reasons: Sequence[str]

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "family_passing_cores", _deep_freeze(self.family_passing_cores)
        )
        object.__setattr__(self, "fleiss_kappa", _deep_freeze(self.fleiss_kappa))
        object.__setattr__(self, "reasons", tuple(self.reasons))

    @property
    def passes(self) -> bool:
        return self.status == "PASS"


_PANEL_FIELDS = (
    "rater_id",
    "qualification",
    "covers_procurement",
    "covers_finance",
    "synthetic",
)
_RATING_FIELDS = (
    "core_id",
    "rater_id",
    "scenario_realism",
    "magnitude_window_plausibility",
)
_PROFESSIONAL_QUALIFICATIONS = {
    "procurement_professional",
    "finance_professional",
    "procurement_finance_professional",
}
_QUALIFICATION_COVERAGE = {
    "procurement_professional": (True, False),
    "finance_professional": (False, True),
    "procurement_finance_professional": (True, True),
}


def _realism_failure(reason: str) -> ProfessionalRealismResult:
    return ProfessionalRealismResult(
        "FAIL",
        {family: 0 for family in FAMILIES},
        {"scenario_realism": None, "magnitude_window_plausibility": None},
        (reason,),
    )


def _fleiss_kappa_binary(grouped_ratings: Mapping[str, Sequence[bool]]) -> Optional[float]:
    agreements = []
    yes_total = 0
    total = 0
    for values in grouped_ratings.values():
        if len(values) != 2 or not all(isinstance(value, bool) for value in values):
            return None
        yes_count = sum(values)
        no_count = 2 - yes_count
        agreements.append(
            (yes_count * yes_count + no_count * no_count - 2) / (2 * 1)
        )
        yes_total += yes_count
        total += 2
    if not agreements or total == 0:
        return None
    p_yes = yes_total / total
    expected = p_yes * p_yes + (1.0 - p_yes) * (1.0 - p_yes)
    denominator = 1.0 - expected
    if denominator <= 0.0:
        return None
    observed = sum(agreements) / len(agreements)
    value = (observed - expected) / denominator
    return value if math.isfinite(value) else None


def _valid_revision_history(revision_history: Any) -> bool:
    if (
        isinstance(revision_history, (str, bytes, bytearray))
        or not isinstance(revision_history, SequenceABC)
        or len(revision_history) > 1
    ):
        return False
    if not revision_history:
        return True
    revision = revision_history[0]
    return (
        isinstance(revision, MappingABC)
        and set(revision) == set(REVISION_HISTORY_FIELDS)
        and type(revision["round"]) is int
        and revision["round"] == 1
        and revision["completed_before_model_data"] is True
        and _nonblank_text(revision["reason"])
    )


def evaluate_professional_realism(
    core_families: Any,
    panel_records: Any,
    rating_records: Any,
    revision_history: Any,
) -> ProfessionalRealismResult:
    """Derive realism status from exact 40-core, three-pro, 80-rating evidence."""

    if not _valid_revision_history(revision_history):
        return _realism_failure("INVALID_REVISION_HISTORY")
    if not isinstance(core_families, MappingABC) or len(core_families) != 40:
        return _realism_failure("INVALID_CORE_FAMILY_MAP")
    if not all(
        _nonblank_text(core_id) and family in FAMILY_CORE_COUNTS
        for core_id, family in core_families.items()
    ):
        return _realism_failure("INVALID_CORE_FAMILY_MAP")
    family_counts = {
        family: sum(value == family for value in core_families.values())
        for family in FAMILIES
    }
    if any(count != 8 for count in family_counts.values()):
        return _realism_failure("UNBALANCED_CORE_FAMILY_MAP")

    if (
        isinstance(panel_records, (str, bytes, bytearray))
        or not isinstance(panel_records, SequenceABC)
        or len(panel_records) != 3
    ):
        return _realism_failure("INVALID_PROFESSIONAL_PANEL")
    rater_ids = []
    procurement_covered = False
    finance_covered = False
    for panel_record in panel_records:
        if not isinstance(panel_record, MappingABC) or set(panel_record) != set(
            _PANEL_FIELDS
        ):
            return _realism_failure("INVALID_PROFESSIONAL_PANEL")
        if (
            not _nonblank_text(panel_record["rater_id"])
            or panel_record["qualification"] not in _PROFESSIONAL_QUALIFICATIONS
            or not isinstance(panel_record["covers_procurement"], bool)
            or not isinstance(panel_record["covers_finance"], bool)
            or panel_record["synthetic"] is not False
        ):
            return _realism_failure("INVALID_PROFESSIONAL_PANEL")
        if (
            panel_record["covers_procurement"],
            panel_record["covers_finance"],
        ) != _QUALIFICATION_COVERAGE[panel_record["qualification"]]:
            return _realism_failure("INVALID_PROFESSIONAL_PANEL")
        rater_ids.append(panel_record["rater_id"])
        procurement_covered = procurement_covered or panel_record["covers_procurement"]
        finance_covered = finance_covered or panel_record["covers_finance"]
    if len(set(rater_ids)) != 3 or not procurement_covered or not finance_covered:
        return _realism_failure("INVALID_PROFESSIONAL_PANEL")

    if (
        isinstance(rating_records, (str, bytes, bytearray))
        or not isinstance(rating_records, SequenceABC)
        or len(rating_records) != 80
    ):
        return _realism_failure("INVALID_RATING_COUNT")
    by_core = {core_id: [] for core_id in core_families}
    seen_assignments = set()
    for rating in rating_records:
        if not isinstance(rating, MappingABC) or set(rating) != set(_RATING_FIELDS):
            return _realism_failure("INVALID_RATING_RECORD")
        core_id = rating["core_id"]
        rater_id = rating["rater_id"]
        assignment = (core_id, rater_id)
        if (
            core_id not in core_families
            or rater_id not in rater_ids
            or assignment in seen_assignments
            or not isinstance(rating["scenario_realism"], bool)
            or not isinstance(rating["magnitude_window_plausibility"], bool)
        ):
            return _realism_failure("INVALID_RATING_RECORD")
        seen_assignments.add(assignment)
        by_core[core_id].append(rating)
    if any(
        len(records) != 2 or len({record["rater_id"] for record in records}) != 2
        for records in by_core.values()
    ):
        return _realism_failure("INCOMPLETE_CORE_ASSIGNMENT")
    if {rater_id for _, rater_id in seen_assignments} != set(rater_ids):
        return _realism_failure("UNUSED_PANEL_RATER")

    family_passing = {family: 0 for family in FAMILIES}
    for core_id, records in by_core.items():
        core_passes = all(
            record["scenario_realism"]
            and record["magnitude_window_plausibility"]
            for record in records
        )
        if core_passes:
            family_passing[core_families[core_id]] += 1
    kappas = {}
    for field in ("scenario_realism", "magnitude_window_plausibility"):
        kappas[field] = _fleiss_kappa_binary(
            {
                core_id: [record[field] for record in records]
                for core_id, records in by_core.items()
            }
        )
    if any(value is None for value in kappas.values()):
        return ProfessionalRealismResult(
            "NOT_ESTIMABLE", family_passing, kappas, ("FLEISS_KAPPA_NOT_ESTIMABLE",)
        )
    passes = all(count >= 7 for count in family_passing.values()) and all(
        value >= 0.70 for value in kappas.values()
    )
    return ProfessionalRealismResult(
        "PASS" if passes else "FAIL",
        family_passing,
        kappas,
        () if passes else ("REALISM_GATE_NOT_MET",),
    )


def professional_realism_passes(
    core_families: Any,
    panel_records: Any,
    rating_records: Any,
    revision_history: Any,
) -> bool:
    """Return the derived raw-evidence realism pass predicate."""

    return evaluate_professional_realism(
        core_families, panel_records, rating_records, revision_history
    ).passes


def release_budget_allows(
    *,
    run_kind: str,
    scheduled_requests: Any,
    paid_calls: Any,
    terminal_actions_per_request: Any,
    syntax_repairs_per_request: Any,
    attributed_cost_usd: Any,
    price_attribution_complete: bool,
    cost_attribution_complete: bool,
    user_frozen_cost_cap_usd: Any = None,
) -> bool:
    """Enforce terminal-action, repair, call, and returned-cost release caps."""

    counts = (
        scheduled_requests,
        paid_calls,
        terminal_actions_per_request,
        syntax_repairs_per_request,
    )
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in counts):
        return False
    if run_kind == "smoke":
        expected_requests, call_cap, cost_cap = 9, 18, 1.0
    elif run_kind == "full_diagnostic":
        expected_requests, call_cap, cost_cap = 2400, 4800, 25.0
    elif run_kind == "official":
        if not _finite_real(user_frozen_cost_cap_usd) or user_frozen_cost_cap_usd <= 0:
            return False
        expected_requests, call_cap, cost_cap = 7200, 14400, float(
            user_frozen_cost_cap_usd
        )
    else:
        return False
    return (
        scheduled_requests == expected_requests
        and 0 <= paid_calls <= call_cap
        and 0 <= terminal_actions_per_request <= 1
        and 0 <= syntax_repairs_per_request <= 1
        and price_attribution_complete is True
        and cost_attribution_complete is True
        and _finite_real(attributed_cost_usd)
        and 0.0 <= attributed_cost_usd <= cost_cap
    )

__all__ = [
    "EvidenceBasis",
    "ProfessionalRealismResult",
    "capability_reference_status",
    "derive_capability_projections",
    "evaluate_professional_realism",
    "hash_capability_reference",
    "professional_realism_passes",
    "release_budget_allows",
    "validate_capability_reference",
]
