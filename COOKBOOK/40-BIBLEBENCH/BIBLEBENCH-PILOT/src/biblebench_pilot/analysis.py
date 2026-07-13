"""Deterministic synthetic-only analysis scaffolding for BibleBench.

This module validates analysis plumbing.  It cannot ingest real or unknown
provenance and does not compute composites, rankings, inferential statistics,
or empirical claims.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import csv
from dataclasses import dataclass
import io
import json
import math
from pathlib import Path
import re
from types import NoneType
from typing import Any, Literal, Mapping, TypeAlias

from .contracts import Json, canonical_sha256
from .custody import verify_cue_custody_manifest
from .schedule import Schedule


SYNTHETIC_PROVENANCE = "SYNTHETIC_VALIDATION_ONLY"

Module = Literal[
    "fruitbench", "corinthlove", "tencommandments", "sermonmount"
]
Role = Literal["target", "null", "restraint"]
Stratum = Literal["common_life", "christian_facing"]
Cue = Literal["C0", "C1", "C2"]
CompletionStatus = Literal["complete", "incomplete"]
EvidenceStatus = Literal["available", "missing"]
ConsistencyStatus = Literal["consistent", "inconsistent", "not_assessable"]
NativeValue: TypeAlias = NoneType | bool | int | float | str

_MODULES = ("fruitbench", "corinthlove", "tencommandments", "sermonmount")
_ROLES = frozenset({"target", "null", "restraint"})
_STRATA = ("common_life", "christian_facing")
_CUES = ("C0", "C1", "C2")
_COMPLETION = frozenset({"complete", "incomplete"})
_EVIDENCE = frozenset({"available", "missing"})
_CONSISTENCY = frozenset({"consistent", "inconsistent", "not_assessable"})
_MODULE_DIMENSIONS = {
    "fruitbench": ("bounded_kindness", "task_fidelity"),
    "corinthlove": ("authority_restraint", "truth_care"),
    "tencommandments": ("neighbor_protection", "truthful_witness"),
    "sermonmount": ("passage_fidelity", "prudent_action"),
}
_ID = re.compile(r"synthetic-[a-z0-9][a-z0-9-]{0,126}\Z")
_MODEL_ALIAS = re.compile(r"synthetic-model-[a-z0-9][a-z0-9-]{0,111}\Z")
_DIMENSION = re.compile(r"[a-z][a-z0-9_]{0,63}\Z")
_INCIDENT = re.compile(r"[a-z][a-z0-9_]{0,63}\Z")
_HASH = re.compile(r"[0-9a-f]{64}\Z")
_LOGICAL_ID = re.compile(r"[0-9a-f]{16}\Z")
_DOCUMENT_FIELDS = frozenset({"provenance", "schema_version", "observations"})
_ROW_FIELDS = frozenset(
    {
        "provenance",
        "observation_id",
        "model_alias",
        "module",
        "episode_id",
        "role",
        "stratum",
        "cue",
        "cue_set_id",
        "custody_primary_logical_call_id",
        "evidence_bundle_sha256",
        "completion_status",
        "evidence_status",
        "native_dimension_values",
        "red_line_incidents",
        "action_probe_consistency",
        "repeat_decisions",
    }
)
_REPEAT_FIELDS = frozenset({"first", "repeat"})
_PROHIBITED_INPUT_KEY = re.compile(
    r"(?:^|_)(?:overall(?:_score)?|composite(?:_score)?|aggregate(?:_score)?|"
    r"leaderboard|best_model|rank|ranking|p_value|pvalue|denominator|"
    r"percentage|empirical_claim)(?:$|_)",
)
_PROHIBITED_OUTPUT_KEY = re.compile(
    r"(?:^|_)(?:overall(?:_score)?|composite(?:_score)?|aggregate(?:_score)?|"
    r"leaderboard|best_model|rank|ranking|p_value|pvalue|empirical_claim)(?:$|_)",
)
_CUE_PAIRS = (("C0", "C1"), ("C0", "C2"), ("C1", "C2"))


@dataclass(frozen=True)
class SyntheticObservation:
    """One validated synthetic episode/cue observation."""

    provenance: Literal["SYNTHETIC_VALIDATION_ONLY"]
    observation_id: str
    model_alias: str
    module: Module
    episode_id: str
    role: Role
    stratum: Stratum
    cue: Cue
    cue_set_id: str
    custody_primary_logical_call_id: str
    evidence_bundle_sha256: str
    completion_status: CompletionStatus
    evidence_status: EvidenceStatus
    native_dimension_values: dict[str, NativeValue]
    red_line_incidents: tuple[str, ...]
    action_probe_consistency: ConsistencyStatus
    repeat_decisions: tuple[str, str] | None


def _require_exact_dict(value: Any, *, label: str) -> dict[str, Any]:
    if type(value) is not dict or any(type(key) is not str for key in value):
        raise ValueError(f"{label} must be a strict JSON object")
    return value


def _reject_prohibited_input_keys(value: Any, *, path: str = "input") -> None:
    if type(value) is dict:
        for key, child in value.items():
            if type(key) is not str:
                raise ValueError(f"{path} contains a non-string key")
            normalized = key.lower().replace("-", "_")
            if _PROHIBITED_INPUT_KEY.search(normalized):
                raise ValueError(f"prohibited analysis input field: {path}.{key}")
            _reject_prohibited_input_keys(child, path=f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            _reject_prohibited_input_keys(child, path=f"{path}[{index}]")


def _reject_prohibited_output_keys(value: Any, *, path: str = "output") -> None:
    if type(value) is dict:
        for key, child in value.items():
            if type(key) is not str:
                raise ValueError(f"{path} contains a non-string key")
            normalized = key.lower().replace("-", "_")
            if _PROHIBITED_OUTPUT_KEY.search(normalized):
                raise ValueError(f"prohibited analysis output field: {path}.{key}")
            _reject_prohibited_output_keys(child, path=f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            _reject_prohibited_output_keys(child, path=f"{path}[{index}]")


def _require_fields(
    value: Mapping[str, Any], expected: frozenset[str], *, label: str
) -> None:
    fields = frozenset(value)
    if fields != expected:
        missing = sorted(expected - fields)
        extra = sorted(fields - expected)
        raise ValueError(f"{label} fields are not closed; missing={missing}, extra={extra}")


def _require_string(value: Any, *, label: str) -> str:
    if type(value) is not str or not value:
        raise ValueError(f"{label} must be a non-empty string")
    return value


def _require_choice(value: Any, choices: frozenset[str] | tuple[str, ...], *, label: str) -> str:
    value = _require_string(value, label=label)
    if value not in choices:
        raise ValueError(f"{label} is invalid")
    return value


def _native_value(value: Any, *, label: str) -> NativeValue:
    if value is None or type(value) in {bool, int}:
        return value
    if type(value) is float:
        if math.isfinite(value):
            return value
        raise ValueError(f"{label} must be finite")
    if type(value) is str and value.strip() and len(value) <= 128:
        return value
    raise ValueError(f"{label} must be a bounded scalar or explicit null")


def _parse_row(raw: Any) -> SyntheticObservation:
    row = _require_exact_dict(raw, label="observation")
    _require_fields(row, _ROW_FIELDS, label="observation")
    if row["provenance"] != SYNTHETIC_PROVENANCE:
        raise ValueError("observation provenance must be SYNTHETIC_VALIDATION_ONLY")

    observation_id = _require_string(row["observation_id"], label="observation_id")
    if not _ID.fullmatch(observation_id):
        raise ValueError("observation_id must be an explicitly synthetic identifier")
    model_alias = _require_string(row["model_alias"], label="model_alias")
    if not _MODEL_ALIAS.fullmatch(model_alias):
        raise ValueError("model_alias must be an explicitly synthetic alias")
    cue_set_id = _require_string(row["cue_set_id"], label="cue_set_id")
    if not _ID.fullmatch(cue_set_id):
        raise ValueError("cue_set_id must be an explicitly synthetic identifier")
    episode_id = _require_string(row["episode_id"], label="episode_id")
    if len(episode_id.encode("utf-8")) > 128:
        raise ValueError("episode_id is too long")
    primary_logical_call_id = _require_string(
        row["custody_primary_logical_call_id"],
        label="custody_primary_logical_call_id",
    )
    if not _LOGICAL_ID.fullmatch(primary_logical_call_id):
        raise ValueError("custody_primary_logical_call_id is invalid")
    evidence_bundle_sha256 = _require_string(
        row["evidence_bundle_sha256"], label="evidence_bundle_sha256"
    )
    if not _HASH.fullmatch(evidence_bundle_sha256):
        raise ValueError("evidence_bundle_sha256 is invalid")
    module = _require_choice(row["module"], _MODULES, label="module")

    raw_dimensions = _require_exact_dict(
        row["native_dimension_values"], label="native_dimension_values"
    )
    registered_dimensions = _MODULE_DIMENSIONS[module]
    dimensions: dict[str, NativeValue] = {
        name: None for name in registered_dimensions
    }
    for name, raw_value in raw_dimensions.items():
        if not _DIMENSION.fullmatch(name):
            raise ValueError(f"invalid native dimension name: {name}")
        if name not in registered_dimensions:
            raise ValueError(f"dimension is not registered for {module}: {name}")
        dimensions[name] = _native_value(raw_value, label=f"dimension {name}")

    completion = _require_choice(
        row["completion_status"], _COMPLETION, label="completion_status"
    )
    evidence = _require_choice(
        row["evidence_status"], _EVIDENCE, label="evidence_status"
    )
    if completion == "complete" and evidence == "available" and any(
        value is None for value in dimensions.values()
    ):
        raise ValueError("complete available observations cannot have missing dimensions")
    if evidence == "missing" and any(value is not None for value in dimensions.values()):
        raise ValueError("missing evidence cannot support observed dimension values")

    raw_incidents = row["red_line_incidents"]
    if type(raw_incidents) is not list:
        raise ValueError("red_line_incidents must be a list")
    incidents: list[str] = []
    for incident in raw_incidents:
        incident = _require_string(incident, label="red_line_incident")
        if not _INCIDENT.fullmatch(incident):
            raise ValueError("red_line_incident is invalid")
        incidents.append(incident)
    if len(incidents) != len(set(incidents)):
        raise ValueError("red_line_incidents must be unique")
    if evidence == "missing" and incidents:
        raise ValueError("red-line incidents require available evidence")

    consistency = _require_choice(
        row["action_probe_consistency"],
        _CONSISTENCY,
        label="action_probe_consistency",
    )
    if (completion != "complete" or evidence != "available") and consistency != "not_assessable":
        raise ValueError("incomplete or missing evidence must be not_assessable")

    raw_repeat = row["repeat_decisions"]
    repeat: tuple[str, str] | None
    if raw_repeat is None:
        repeat = None
    else:
        repeat_object = _require_exact_dict(raw_repeat, label="repeat_decisions")
        _require_fields(repeat_object, _REPEAT_FIELDS, label="repeat_decisions")
        if completion != "complete" or evidence != "available":
            raise ValueError("repeat denominator requires complete available evidence")
        first = _require_string(repeat_object["first"], label="repeat_decisions.first")
        second = _require_string(repeat_object["repeat"], label="repeat_decisions.repeat")
        repeat = (first, second)

    return SyntheticObservation(
        provenance=SYNTHETIC_PROVENANCE,
        observation_id=observation_id,
        model_alias=model_alias,
        module=module,  # type: ignore[arg-type]
        episode_id=episode_id,
        role=_require_choice(row["role"], _ROLES, label="role"),  # type: ignore[arg-type]
        stratum=_require_choice(row["stratum"], _STRATA, label="stratum"),  # type: ignore[arg-type]
        cue=_require_choice(row["cue"], _CUES, label="cue"),  # type: ignore[arg-type]
        cue_set_id=cue_set_id,
        custody_primary_logical_call_id=primary_logical_call_id,
        evidence_bundle_sha256=evidence_bundle_sha256,
        completion_status=completion,  # type: ignore[arg-type]
        evidence_status=evidence,  # type: ignore[arg-type]
        native_dimension_values=dimensions,
        red_line_incidents=tuple(incidents),
        action_probe_consistency=consistency,  # type: ignore[arg-type]
        repeat_decisions=repeat,
    )


def validate_document(document: Any) -> tuple[SyntheticObservation, ...]:
    """Validate a closed synthetic observation document."""

    _reject_prohibited_input_keys(document)
    payload = _require_exact_dict(document, label="document")
    _require_fields(payload, _DOCUMENT_FIELDS, label="document")
    if payload["provenance"] != SYNTHETIC_PROVENANCE:
        raise ValueError("document provenance must be SYNTHETIC_VALIDATION_ONLY")
    if payload["schema_version"] != "synthetic-observations-v1":
        raise ValueError("unsupported synthetic observation schema")
    if type(payload["observations"]) is not list or not payload["observations"]:
        raise ValueError("observations must be a non-empty list")

    observations = tuple(_parse_row(row) for row in payload["observations"])
    identifiers = [row.observation_id for row in observations]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("duplicate observation_id")
    custody_ids = [row.custody_primary_logical_call_id for row in observations]
    if len(custody_ids) != len(set(custody_ids)):
        raise ValueError("duplicate custody primary logical call")
    return observations


def _verify_and_bind_cue_custody(
    document: Any,
    observations: tuple[SyntheticObservation, ...],
    *,
    schedule: Schedule | None,
    evidence_inventory: tuple[dict[str, str], ...] | None,
    manifest: dict[str, Json] | None,
    evidence_root: Path | None,
) -> dict[str, Any]:
    """Recompute primary custody and bind it to this observation document."""

    if any(
        value is None
        for value in (schedule, evidence_inventory, manifest, evidence_root)
    ):
        raise ValueError("cue contrasts require primary cue custody inputs")
    custody_verification = verify_cue_custody_manifest(
        schedule,
        evidence_inventory,
        manifest,
        evidence_root=evidence_root,
    )
    if type(manifest) is not dict:
        raise ValueError("observation custody binding is invalid")
    manifest_rows = manifest.get("rows")
    if type(manifest_rows) is not list:
        raise ValueError("observation custody binding is invalid")
    manifest_core = {
        key: value
        for key, value in manifest.items()
        if key not in {"manifest_sha256", "custody_receipt"}
    }
    receipt = manifest.get("custody_receipt")
    if type(receipt) is not dict:
        raise ValueError("observation custody binding is invalid")
    receipt_core = {
        key: value for key, value in receipt.items() if key != "receipt_sha256"
    }
    if (
        manifest.get("manifest_sha256")
        != custody_verification.manifest_sha256
        or canonical_sha256(manifest_core)
        != custody_verification.manifest_sha256
        or receipt.get("receipt_sha256")
        != custody_verification.receipt_sha256
        or canonical_sha256(receipt_core)
        != custody_verification.receipt_sha256
        or manifest.get("canonical_schedule_sha256")
        != custody_verification.canonical_schedule_sha256
        or manifest.get("row_count") != custody_verification.row_count
        or len(manifest_rows) != custody_verification.row_count
        or canonical_sha256(manifest_rows)
        != custody_verification.custody_rows_sha256
        or canonical_sha256(
            {
                "domain": "biblebench.cue_custody.inventory.v1",
                "rows": manifest_rows,
            }
        )
        != custody_verification.evidence_inventory_sha256
    ):
        raise ValueError("observation custody binding is invalid")
    by_primary = {
        row.get("primary_logical_call_id"): row
        for row in manifest_rows
        if type(row) is dict
    }
    if len(by_primary) != len(manifest_rows):
        raise ValueError("observation custody binding is invalid")
    cue_sets_by_identity: dict[tuple[str, str, str, str], tuple[str, str]] = {}
    for observation in observations:
        custody_row = by_primary.get(observation.custody_primary_logical_call_id)
        if custody_row is None or any(
            custody_row.get(field) != expected
            for field, expected in (
                ("actor_id", observation.model_alias),
                ("module", observation.module),
                ("episode_id", observation.episode_id),
                ("role", observation.role),
                ("cue", observation.cue),
                ("evidence_bundle_sha256", observation.evidence_bundle_sha256),
            )
        ):
            raise ValueError("observation custody binding is invalid")
        cue_identity = (
            observation.model_alias,
            observation.module,
            observation.episode_id,
            observation.role,
        )
        prior_binding = cue_sets_by_identity.setdefault(
            cue_identity,
            (observation.cue_set_id, observation.stratum),
        )
        if prior_binding[0] != observation.cue_set_id:
            raise ValueError("observation cue-set binding is invalid")
        if prior_binding[1] != observation.stratum:
            raise ValueError("cue-set stratum invariant is invalid")
    return {
        "provenance": SYNTHETIC_PROVENANCE,
        "status": "VERIFIED_PRIVATE_CUSTODY",
        "manifest_sha256": custody_verification.manifest_sha256,
        "receipt_sha256": custody_verification.receipt_sha256,
        "custody_rows_sha256": custody_verification.custody_rows_sha256,
        "observation_set_sha256": canonical_sha256(document),
        "bound_observation_count": len(observations),
    }


def load_synthetic_document(path: str | Path) -> dict[str, Any]:
    """Load and validate a synthetic observation JSON file."""

    try:
        document = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("unable to load strict synthetic observation JSON") from error
    validate_document(document)
    return document


def _percentage(count: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return round(100.0 * count / denominator, 6)


def _summary_count(value: Any) -> int:
    if type(value) is not int or value < 0:
        raise ValueError("invalid summary denominator")
    return value


def _validate_summary_denominators(summary: Mapping[str, Any]) -> None:
    """Reject mutated count surfaces that would misstate a denominator."""

    try:
        mechanical = summary["mechanical_validity"]
        observation_count = _summary_count(mechanical["observation_count"])
        dimension_slots = _summary_count(mechanical["dimension_value_slot_count"])
        if observation_count == 0 or dimension_slots == 0:
            raise ValueError("invalid summary denominator")
        if (
            _summary_count(mechanical["complete_count"])
            + _summary_count(mechanical["incomplete_count"])
            != observation_count
        ):
            raise ValueError("invalid summary denominator")
        if (
            _summary_count(mechanical["evidence_available_count"])
            + _summary_count(mechanical["evidence_missing_count"])
            != observation_count
        ):
            raise ValueError("invalid summary denominator")
        if _summary_count(mechanical["missing_dimension_value_count"]) > dimension_slots:
            raise ValueError("invalid summary denominator")

        for dimensions in summary["module_native_dimension_vectors"].values():
            for vector in dimensions.values():
                denominator = _summary_count(vector["denominator"])
                observed = _summary_count(vector["observed_count"])
                missing = _summary_count(vector["missing_count"])
                if denominator == 0 or observed + missing != denominator:
                    raise ValueError("invalid summary denominator")
                value_total = sum(
                    _summary_count(item["count"]) for item in vector["value_counts"]
                )
                if value_total != observed:
                    raise ValueError("invalid summary denominator")

        for stratum in _STRATA:
            stratum_data = summary["strata"][stratum]
            stratum_count = _summary_count(stratum_data["observation_count"])
            if sum(
                _summary_count(stratum_data["module_counts"][module])
                for module in _MODULES
            ) != stratum_count:
                raise ValueError("invalid summary denominator")
            if _summary_count(stratum_data["complete_count"]) > stratum_count:
                raise ValueError("invalid summary denominator")
            if _summary_count(stratum_data["evidence_missing_count"]) > stratum_count:
                raise ValueError("invalid summary denominator")
        if sum(
            _summary_count(summary["strata"][stratum]["observation_count"])
            for stratum in _STRATA
        ) != observation_count:
            raise ValueError("invalid summary denominator")

        red_lines = summary["red_line_incidents"]
        if _summary_count(red_lines["observation_denominator"]) != observation_count:
            raise ValueError("invalid summary denominator")
        if _summary_count(red_lines["observations_with_incident"]) > observation_count:
            raise ValueError("invalid summary denominator")
        if sum(_summary_count(count) for count in red_lines["by_class"].values()) != _summary_count(
            red_lines["incident_count"]
        ):
            raise ValueError("invalid summary denominator")

        consistency = summary["action_probe_consistency"]
        consistency_counts = consistency["counts"]
        eligible = _summary_count(consistency["eligible_denominator"])
        if eligible != (
            _summary_count(consistency_counts["consistent"])
            + _summary_count(consistency_counts["inconsistent"])
        ):
            raise ValueError("invalid summary denominator")
        if sum(_summary_count(count) for count in consistency_counts.values()) != observation_count:
            raise ValueError("invalid summary denominator")
        if consistency["consistent_percentage"] != _percentage(
            consistency_counts["consistent"], eligible
        ):
            raise ValueError("invalid summary denominator")

        repeat = summary["repeat_agreement"]
        repeat_denominator = _summary_count(repeat["repeat_pair_denominator"])
        agreement = _summary_count(repeat["exact_agreement_count"])
        disagreement = _summary_count(repeat["exact_disagreement_count"])
        if agreement + disagreement != repeat_denominator:
            raise ValueError("invalid summary denominator")
        if repeat["exact_agreement_percentage"] != _percentage(
            agreement, repeat_denominator
        ):
            raise ValueError("invalid summary denominator")

        if "cue_controlled_contrasts" in summary:
            cue_output = summary["cue_controlled_contrasts"]
            custody_output = cue_output["custody"]
            if (
                custody_output.get("provenance") != SYNTHETIC_PROVENANCE
                or custody_output.get("status") != "VERIFIED_PRIVATE_CUSTODY"
                or any(
                    type(custody_output.get(name)) is not str
                    or not _HASH.fullmatch(custody_output[name])
                    for name in (
                        "manifest_sha256",
                        "receipt_sha256",
                        "custody_rows_sha256",
                        "observation_set_sha256",
                    )
                )
                or custody_output.get("bound_observation_count")
                != observation_count
            ):
                raise ValueError("invalid synthetic cue custody output")
            paired = cue_output["paired_outcomes"]
            if [item["cue_pair"] for item in paired] != [
                "C0_vs_C1",
                "C0_vs_C2",
                "C1_vs_C2",
            ]:
                raise ValueError("invalid summary denominator")
            for item in paired:
                candidate = _summary_count(item["candidate_set_denominator"])
                eligible = _summary_count(item["eligible_set_count"])
                missing = _summary_count(item["missing_or_ineligible_set_count"])
                if eligible + missing != candidate:
                    raise ValueError("invalid summary denominator")
                for table in item["dimension_transition_tables"]:
                    table_candidate = _summary_count(
                        table["candidate_pair_denominator"]
                    )
                    table_eligible = _summary_count(
                        table["eligible_pair_denominator"]
                    )
                    table_missing = _summary_count(table["missing_pair_count"])
                    if table_eligible + table_missing != table_candidate:
                        raise ValueError("invalid summary denominator")
                    if sum(
                        _summary_count(transition["count"])
                        for transition in table["transitions"]
                    ) != table_eligible:
                        raise ValueError("invalid summary denominator")
    except (KeyError, TypeError, AttributeError) as error:
        raise ValueError("invalid summary denominator") from error


def _value_key(value: NativeValue) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _dimension_vectors(observations: tuple[SyntheticObservation, ...]) -> dict[str, Any]:
    vectors: dict[str, Any] = {}
    for module in _MODULES:
        module_rows = [row for row in observations if row.module == module]
        if not module_rows:
            continue
        module_vector: dict[str, Any] = {}
        for dimension in _MODULE_DIMENSIONS[module]:
            slots = [
                row.native_dimension_values[dimension]
                for row in module_rows
            ]
            observed = [value for value in slots if value is not None]
            counts = Counter(_value_key(value) for value in observed)
            values_by_key = {_value_key(value): value for value in observed}
            module_vector[dimension] = {
                "denominator": len(slots),
                "observed_count": len(observed),
                "missing_count": len(slots) - len(observed),
                "value_counts": [
                    {"value": values_by_key[key], "count": counts[key]}
                    for key in sorted(counts)
                ],
            }
        vectors[module] = module_vector
    return vectors


def _strata(observations: tuple[SyntheticObservation, ...]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for stratum in _STRATA:
        rows = [row for row in observations if row.stratum == stratum]
        output[stratum] = {
            "observation_count": len(rows),
            "complete_count": sum(row.completion_status == "complete" for row in rows),
            "evidence_missing_count": sum(row.evidence_status == "missing" for row in rows),
            "module_counts": {
                module: sum(row.module == module for row in rows) for module in _MODULES
            },
        }
    return output


def _cue_contrast_counts(
    observations: tuple[SyntheticObservation, ...],
    custody: dict[str, Any],
) -> dict[str, Any]:
    grouped: dict[
        tuple[str, str, str, str],
        dict[str, SyntheticObservation],
    ] = defaultdict(dict)
    for row in observations:
        key = (
            row.model_alias,
            row.module,
            row.episode_id,
            row.role,
        )
        if row.cue in grouped[key]:
            raise ValueError("duplicate cue within a controlled cue set")
        grouped[key][row.cue] = row

    paired_outcomes: list[dict[str, Any]] = []
    for left, right in _CUE_PAIRS:
        candidate_groups = [
            (key, cue_rows)
            for key, cue_rows in grouped.items()
            if left in cue_rows or right in cue_rows
        ]
        eligible_groups = [
            (key, cue_rows)
            for key, cue_rows in candidate_groups
            if left in cue_rows
            and right in cue_rows
            and all(
                row.completion_status == "complete"
                and row.evidence_status == "available"
                and all(
                    value is not None
                    for value in row.native_dimension_values.values()
                )
                for row in (cue_rows[left], cue_rows[right])
            )
        ]
        transition_tables: list[dict[str, Any]] = []
        for module in _MODULES:
            module_candidates = [
                item for item in candidate_groups if item[0][1] == module
            ]
            if not module_candidates:
                continue
            module_eligible = [
                item for item in eligible_groups if item[0][1] == module
            ]
            for dimension in _MODULE_DIMENSIONS[module]:
                transition_counter: Counter[tuple[str, str]] = Counter()
                transition_values: dict[
                    tuple[str, str], tuple[NativeValue, NativeValue]
                ] = {}
                for _, cue_rows in module_eligible:
                    left_value = cue_rows[left].native_dimension_values[dimension]
                    right_value = cue_rows[right].native_dimension_values[dimension]
                    transition_key = (
                        _value_key(left_value),
                        _value_key(right_value),
                    )
                    transition_counter[transition_key] += 1
                    transition_values[transition_key] = (
                        left_value,
                        right_value,
                    )
                transition_tables.append(
                    {
                        "module": module,
                        "dimension": dimension,
                        "candidate_pair_denominator": len(module_candidates),
                        "eligible_pair_denominator": len(module_eligible),
                        "missing_pair_count": (
                            len(module_candidates) - len(module_eligible)
                        ),
                        "transitions": [
                            {
                                "left_value": transition_values[key][0],
                                "right_value": transition_values[key][1],
                                "count": transition_counter[key],
                            }
                            for key in sorted(transition_counter)
                        ],
                    }
                )
        paired_outcomes.append(
            {
                "cue_pair": f"{left}_vs_{right}",
                "candidate_set_denominator": len(candidate_groups),
                "eligible_set_count": len(eligible_groups),
                "missing_or_ineligible_set_count": (
                    len(candidate_groups) - len(eligible_groups)
                ),
                "dimension_transition_tables": transition_tables,
            }
        )
    return {
        "custody": custody,
        "paired_outcomes": paired_outcomes,
    }


def summarize_document(
    document: Any,
    *,
    include_cue_contrasts: bool = False,
    schedule: Schedule | None = None,
    evidence_inventory: tuple[dict[str, str], ...] | None = None,
    custody_manifest: dict[str, Json] | None = None,
    evidence_root: Path | None = None,
) -> dict[str, Any]:
    """Build a deterministic vector-first synthetic summary."""

    if type(include_cue_contrasts) is not bool:
        raise ValueError("include_cue_contrasts must be boolean")
    observations = validate_document(document)
    dimension_slots = sum(len(row.native_dimension_values) for row in observations)
    missing_dimensions = sum(
        value is None
        for row in observations
        for value in row.native_dimension_values.values()
    )
    consistency = Counter(row.action_probe_consistency for row in observations)
    eligible_consistency = consistency["consistent"] + consistency["inconsistent"]
    repeat_rows = [row.repeat_decisions for row in observations if row.repeat_decisions]
    agreement = sum(first == second for first, second in repeat_rows)
    incidents = Counter(
        incident for row in observations for incident in row.red_line_incidents
    )
    incident_rows = sum(bool(row.red_line_incidents) for row in observations)

    summary: dict[str, Any] = {
        "provenance": SYNTHETIC_PROVENANCE,
        "schema_version": "synthetic-summary-v1",
        "limitations": [
            "Synthetic validation fixture; not model evidence.",
            "Only module-native dimension vectors and mechanical counts are present.",
            "Cue-controlled transitions require verifier-produced custody bound to the exact observation set.",
        ],
        "mechanical_validity": {
            "observation_count": len(observations),
            "complete_count": sum(
                row.completion_status == "complete" for row in observations
            ),
            "incomplete_count": sum(
                row.completion_status == "incomplete" for row in observations
            ),
            "evidence_available_count": sum(
                row.evidence_status == "available" for row in observations
            ),
            "evidence_missing_count": sum(
                row.evidence_status == "missing" for row in observations
            ),
            "dimension_value_slot_count": dimension_slots,
            "missing_dimension_value_count": missing_dimensions,
        },
        "module_native_dimension_vectors": _dimension_vectors(observations),
        "strata": _strata(observations),
        "red_line_incidents": {
            "observation_denominator": len(observations),
            "incident_count": sum(incidents.values()),
            "observations_with_incident": incident_rows,
            "by_class": dict(sorted(incidents.items())),
        },
        "action_probe_consistency": {
            "eligible_denominator": eligible_consistency,
            "counts": {
                status: consistency[status]
                for status in ("consistent", "inconsistent", "not_assessable")
            },
            "consistent_percentage": _percentage(
                consistency["consistent"], eligible_consistency
            ),
        },
        "repeat_agreement": {
            "repeat_pair_denominator": len(repeat_rows),
            "exact_agreement_count": agreement,
            "exact_disagreement_count": len(repeat_rows) - agreement,
            "exact_agreement_percentage": _percentage(agreement, len(repeat_rows)),
        },
    }
    if include_cue_contrasts:
        custody = _verify_and_bind_cue_custody(
            document,
            observations,
            schedule=schedule,
            evidence_inventory=evidence_inventory,
            manifest=custody_manifest,
            evidence_root=evidence_root,
        )
        summary["cue_controlled_contrasts"] = _cue_contrast_counts(
            observations, custody
        )
    return summary


def render_summary_json(summary: Mapping[str, Any]) -> bytes:
    """Render a stable, human-readable synthetic summary JSON document."""

    if type(summary) is not dict or summary.get("provenance") != SYNTHETIC_PROVENANCE:
        raise ValueError("summary input must declare SYNTHETIC_VALIDATION_ONLY")
    if summary.get("schema_version") != "synthetic-summary-v1":
        raise ValueError("unsupported synthetic summary schema")
    _reject_prohibited_output_keys(summary)
    _validate_summary_denominators(summary)
    return (
        json.dumps(
            summary,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _csv_rows(summary: Mapping[str, Any]) -> list[list[Any]]:
    note = "synthetic validation only; no empirical claim"
    rows: list[list[Any]] = []
    mechanical = summary["mechanical_validity"]
    for metric in sorted(mechanical):
        denominator = (
            mechanical["dimension_value_slot_count"]
            if "dimension" in metric
            else mechanical["observation_count"]
        )
        rows.append(
            [SYNTHETIC_PROVENANCE, "mechanical_validity", "all", "", metric, "", mechanical[metric], denominator, "", note]
        )

    for module, dimensions in summary["module_native_dimension_vectors"].items():
        for dimension, vector in dimensions.items():
            for value_count in vector["value_counts"]:
                rows.append(
                    [
                        SYNTHETIC_PROVENANCE,
                        "module_native_dimension_vector",
                        "all",
                        module,
                        dimension,
                        _value_key(value_count["value"]),
                        value_count["count"],
                        vector["denominator"],
                        _percentage(value_count["count"], vector["denominator"]),
                        note,
                    ]
                )
            rows.append(
                [SYNTHETIC_PROVENANCE, "module_native_dimension_vector", "all", module, dimension, "missing", vector["missing_count"], vector["denominator"], _percentage(vector["missing_count"], vector["denominator"]), note]
            )

    for stratum in _STRATA:
        stratum_data = summary["strata"][stratum]
        for module in _MODULES:
            rows.append(
                [SYNTHETIC_PROVENANCE, "stratum", stratum, module, "observation_count", "", stratum_data["module_counts"][module], stratum_data["observation_count"], "", note]
            )

    red_lines = summary["red_line_incidents"]
    for incident, count in red_lines["by_class"].items():
        rows.append(
            [SYNTHETIC_PROVENANCE, "red_line_incident", "all", "", "incident_class", incident, count, red_lines["observation_denominator"], _percentage(count, red_lines["observation_denominator"]), note]
        )

    consistency = summary["action_probe_consistency"]
    for status, count in consistency["counts"].items():
        denominator = (
            consistency["eligible_denominator"]
            if status != "not_assessable"
            else mechanical["observation_count"]
        )
        rows.append(
            [SYNTHETIC_PROVENANCE, "action_probe_consistency", "all", "", "status", status, count, denominator, _percentage(count, denominator), note]
        )

    repeat = summary["repeat_agreement"]
    for category, count in (
        ("exact_agreement", repeat["exact_agreement_count"]),
        ("exact_disagreement", repeat["exact_disagreement_count"]),
    ):
        rows.append(
            [SYNTHETIC_PROVENANCE, "repeat_agreement", "all", "", "repeat_decision", category, count, repeat["repeat_pair_denominator"], _percentage(count, repeat["repeat_pair_denominator"]), note]
        )

    if "cue_controlled_contrasts" in summary:
        for pair in summary["cue_controlled_contrasts"]["paired_outcomes"]:
            rows.append(
                [SYNTHETIC_PROVENANCE, "cue_pair_coverage", pair["cue_pair"], "", "pair_eligibility", "eligible", pair["eligible_set_count"], pair["candidate_set_denominator"], _percentage(pair["eligible_set_count"], pair["candidate_set_denominator"]), "paired counts only; verified bound custody"]
            )
            rows.append(
                [SYNTHETIC_PROVENANCE, "cue_pair_coverage", pair["cue_pair"], "", "pair_eligibility", "missing_or_ineligible", pair["missing_or_ineligible_set_count"], pair["candidate_set_denominator"], _percentage(pair["missing_or_ineligible_set_count"], pair["candidate_set_denominator"]), "paired counts only; verified bound custody"]
            )
            for table in pair["dimension_transition_tables"]:
                for transition in table["transitions"]:
                    category = (
                        f"{_value_key(transition['left_value'])}"
                        f"->{_value_key(transition['right_value'])}"
                    )
                    rows.append(
                        [SYNTHETIC_PROVENANCE, "cue_outcome_transition", pair["cue_pair"], table["module"], table["dimension"], category, transition["count"], table["eligible_pair_denominator"], _percentage(transition["count"], table["eligible_pair_denominator"]), "paired transition counts only; no effect claim"]
                    )
                rows.append(
                    [SYNTHETIC_PROVENANCE, "cue_outcome_transition_missingness", pair["cue_pair"], table["module"], table["dimension"], "missing_or_ineligible", table["missing_pair_count"], table["candidate_pair_denominator"], _percentage(table["missing_pair_count"], table["candidate_pair_denominator"]), "transparent pair eligibility denominator"]
                )
    return rows


def render_table_shells_csv(summary: Mapping[str, Any]) -> bytes:
    """Render stable synthetic-only CSV table shells and figure data."""

    if type(summary) is not dict or summary.get("provenance") != SYNTHETIC_PROVENANCE:
        raise ValueError("summary input must declare SYNTHETIC_VALIDATION_ONLY")
    if summary.get("schema_version") != "synthetic-summary-v1":
        raise ValueError("unsupported synthetic summary schema")
    _reject_prohibited_output_keys(summary)
    _validate_summary_denominators(summary)
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(
        [
            "provenance",
            "table",
            "scope",
            "module",
            "dimension",
            "category",
            "count",
            "denominator",
            "percentage",
            "note",
        ]
    )
    writer.writerows(_csv_rows(summary))
    return stream.getvalue().encode("utf-8")


def regenerate_artifacts(
    input_path: str | Path,
    summary_path: str | Path,
    csv_path: str | Path,
    *,
    include_cue_contrasts: bool = False,
    schedule: Schedule | None = None,
    evidence_inventory: tuple[dict[str, str], ...] | None = None,
    custody_manifest: dict[str, Json] | None = None,
    evidence_root: Path | None = None,
) -> dict[str, Any]:
    """Regenerate stable summary JSON and CSV bytes from synthetic input."""

    document = load_synthetic_document(input_path)
    summary = summarize_document(
        document,
        include_cue_contrasts=include_cue_contrasts,
        schedule=schedule,
        evidence_inventory=evidence_inventory,
        custody_manifest=custody_manifest,
        evidence_root=evidence_root,
    )
    Path(summary_path).write_bytes(render_summary_json(summary))
    Path(csv_path).write_bytes(render_table_shells_csv(summary))
    return summary


__all__ = (
    "SYNTHETIC_PROVENANCE",
    "NativeValue",
    "SyntheticObservation",
    "load_synthetic_document",
    "regenerate_artifacts",
    "render_summary_json",
    "render_table_shells_csv",
    "summarize_document",
    "validate_document",
)
