"""Mechanical-only analysis for the bounded OpenRouter forced diagnostic."""

from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import math
import re
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from harness.model_adapters import build_requests_for_record
from harness.openrouter_client import FROZEN_CANONICAL_MODEL_IDS
from harness.openrouter_protocols import (
    DiagnosticProtocol,
    PROTOCOLS_BY_CONFIG_SHA256,
    PROTOCOLS_BY_RUN_ID,
)
from scoring.forced_choice import build_choice_key, score_forced_rows
from zerosum_common import RHO_GRID, zs_design_100


FULL_STATUS = "LIVE_SINGLE_VENDOR_PRECALIBRATION_DIAGNOSTIC"
SMOKE_STATUS = "SMOKE_ONLY"
BLOCKERS = ["NOT_RUN_HUMAN", "SINGLE_MODEL_VENDOR"]
EXPECTED_THRESHOLDS = {
    "valid_response_rate_min_percent": 95,
    "ceiling_accuracy_min_percent": 90,
    "accuracy_discrimination_spread_min_points": 10,
    "zs_discrimination_spread_min_points": 20,
}
EXPECTED_ROSTER = [
    {"model_id": "openai/gpt-5.5", "family": "gpt-5.5", "vendor": "openai"},
    {"model_id": "openai/gpt-5.4", "family": "gpt-5.4", "vendor": "openai"},
    {"model_id": "openai/gpt-5.4-mini", "family": "gpt-5.4-mini", "vendor": "openai"},
]
COLLECTION_FIELDS = {
    "schema_version", "study_id", "run_id", "status", "data_basis",
    "eligible_for_empirical_decision", "official_blockers", "seed",
    "seed_count", "record_type", "smoke", "expected_scheduled_items",
    "preflight", "attempts", "items", "provenance",
}
PREFLIGHT_FIELDS = {
    "config_sha256", "bank_sha256", "gold_sha256", "forced_anchor_count",
    "scheduled_item_count", "model_count", "vendor_count", "seed",
    "catalog_verified", "catalog_model_ids", "smoke",
}
PROVENANCE_FIELDS = {
    "config_sha256", "bank_sha256", "gold_sha256", "audit_sha256",
    "response_sha256",
}
ATTEMPT_FIELDS = {
    "schema_version", "study_id", "run_id", "status", "data_basis",
    "eligible_for_empirical_decision", "model_id", "model_family",
    "vendor", "seed", "item_id", "core_id", "rho", "domain",
    "record_type", "attempt_index", "response_status", "raw_response",
    "selected_option_id", "call_metadata", "error_type", "error_message",
    "request_id", "config_sha256", "bank_sha256", "gold_sha256",
    "previous_attempt_sha256", "attempt_sha256",
}
ITEM_FIELDS = {
    "schema_version", "study_id", "run_id", "status", "data_basis",
    "eligible_for_empirical_decision", "model_id", "model_family",
    "vendor", "seed", "item_id", "core_id", "rho", "domain",
    "record_type", "response_status", "raw_response", "selected_option_id",
    "park_reason", "attempt_count", "terminal_attempt_index", "request_id",
    "config_sha256", "bank_sha256", "gold_sha256",
    "terminal_attempt_sha256",
}
CONFIG_FIELDS = {
    "schema_version", "study_id", "run_id", "status", "data_basis",
    "eligible_for_empirical_decision", "record_type", "seed",
    "expected_items_per_model", "expected_full_calls", "model_roster",
    "transport", "thresholds", "official_blockers", "provenance",
}
CALL_METADATA_FIELDS = {
    "response_id", "model", "finish_reason", "usage", "requested_seed",
    "attempt_count",
}
USAGE_NUMBER_FIELDS = {
    "prompt_tokens", "completion_tokens", "reasoning_tokens", "total_tokens",
    "accepted_prediction_tokens", "rejected_prediction_tokens",
    "cached_tokens", "audio_tokens", "image_tokens", "prompt_audio_tokens",
    "cost", "upstream_inference_cost",
}
USAGE_DETAIL_FIELDS = {
    "completion_tokens_details", "prompt_tokens_details", "cost_details",
}
ADAPTER_ERROR_TYPES = {
    "OpenRouterError", "OpenRouterConfigurationError", "OpenRouterRequestError",
    "OpenRouterTransportError", "OpenRouterResponseError", "OpenRouterCatalogError",
    "AdapterContractError", "AdapterMetadataError",
}
ADAPTER_ERROR_MESSAGES = {
    "OpenRouter adapter failure",
    "Adapter returned non-text",
    "Adapter response metadata failed attribution",
}
ZERO_HASH = "0" * 64
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
OPTION_RE = re.compile(r"^\s*([A-Za-z])\s*$")


class DiagnosticCoverageError(ValueError):
    """Raised when terminal mechanical coverage or provenance is incomplete."""


def _canonical_hash(payload: Any) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _canonical_jsonl_hash(rows: Sequence[Mapping[str, Any]]) -> str:
    try:
        payload = b"".join(
            json.dumps(
                row,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            ).encode("utf-8") + b"\n"
            for row in rows
        )
    except (TypeError, ValueError):
        raise DiagnosticCoverageError("actual scoring rows are not canonical JSON objects") from None
    return hashlib.sha256(payload).hexdigest()


def _strict_option(raw: Any, registered: Sequence[str]) -> Optional[str]:
    if not isinstance(raw, str):
        return None
    match = OPTION_RE.fullmatch(raw)
    if match is None:
        return None
    selected = match.group(1).upper()
    return selected if selected in set(registered) else None


def _exact_frozen_mapping(value: Any, expected: Mapping[str, Any]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(expected)
        and all(
            value.get(field) == frozen
            and type(value.get(field)) is type(frozen)
            for field, frozen in expected.items()
        )
    )


def _expected_request_id(
    record: Mapping[str, Any], model_id: str, seed: int, attempt_index: int
) -> str:
    requests = build_requests_for_record(record)
    if len(requests) != 1:
        raise DiagnosticCoverageError("forced item did not reconstruct one request")
    safe_model = model_id.replace("/", "_")
    return "%s--model-%s--seed-%d--attempt-%d" % (
        requests[0]["request_id"], safe_model, seed, attempt_index
    )


def _safe_usage_object(value: Any) -> bool:
    if not isinstance(value, Mapping):
        return False
    for field, child in value.items():
        if field in USAGE_DETAIL_FIELDS:
            if not _safe_usage_object(child):
                return False
        elif field in USAGE_NUMBER_FIELDS:
            if (
                isinstance(child, bool)
                or not isinstance(child, (int, float))
                or not math.isfinite(float(child))
                or child < 0
                or (field.endswith("tokens") and type(child) is not int)
            ):
                return False
        elif field == "is_byok":
            if type(child) is not bool:
                return False
        else:
            return False
    return True


def _validate_attempt_semantics(
    attempt: Mapping[str, Any],
    registered: Sequence[str],
    *,
    expected_previous_hash: str,
    provenance: Mapping[str, Any],
    protocol: DiagnosticProtocol,
) -> str:
    if set(attempt) != ATTEMPT_FIELDS:
        raise DiagnosticCoverageError("attempt fields do not match exact audit schema")
    if attempt.get("previous_attempt_sha256") != expected_previous_hash:
        raise DiagnosticCoverageError("attempt previous-hash chain is broken")
    supplied_hash = attempt.get("attempt_sha256")
    if not isinstance(supplied_hash, str) or SHA256_RE.fullmatch(supplied_hash) is None:
        raise DiagnosticCoverageError("attempt self-hash is invalid")
    without_hash = dict(attempt)
    without_hash.pop("attempt_sha256")
    if _canonical_hash(without_hash) != supplied_hash:
        raise DiagnosticCoverageError("attempt self-hash does not match its fields")
    for field in ("config_sha256", "bank_sha256", "gold_sha256"):
        if attempt.get(field) != provenance.get(field):
            raise DiagnosticCoverageError("attempt artifact provenance mismatch")
    if (
        attempt.get("schema_version") != 1
        or type(attempt.get("schema_version")) is not int
        or attempt.get("study_id") != "10CB-ZEROSUM-P1"
        or attempt.get("run_id") != protocol.run_id
        or attempt.get("data_basis") != "live_diagnostic"
        or attempt.get("eligible_for_empirical_decision") is not False
        or attempt.get("record_type") != "forced_anchor"
        or attempt.get("seed") != 2026071001
        or type(attempt.get("seed")) is not int
        or type(attempt.get("attempt_index")) is not int
        or attempt.get("attempt_index") not in (1, 2)
        or isinstance(attempt.get("rho"), bool)
        or type(attempt.get("rho")) not in (int, float)
        or attempt.get("rho") not in RHO_GRID
    ):
        raise DiagnosticCoverageError("attempt frozen identity fields are invalid")
    selected = _strict_option(attempt.get("raw_response"), registered)
    status = attempt.get("response_status")
    error_type = attempt.get("error_type")
    error_message = attempt.get("error_message")
    metadata = attempt.get("call_metadata")
    if not isinstance(metadata, Mapping) or any(
        field not in CALL_METADATA_FIELDS for field in metadata
    ):
        raise DiagnosticCoverageError("attempt call metadata contains unsafe fields")
    if "usage" in metadata and not _safe_usage_object(metadata["usage"]):
        raise DiagnosticCoverageError("attempt usage metadata contains unsafe fields")
    if status == "valid_choice":
        valid = (
            selected is not None
            and attempt.get("selected_option_id") == selected
            and error_type is None
            and error_message is None
        )
    elif status == "blank_response":
        raw = attempt.get("raw_response")
        valid = (
            isinstance(raw, str)
            and not raw.strip()
            and attempt.get("selected_option_id") is None
            and error_type is None
            and error_message is None
        )
    elif status == "invalid_choice":
        raw = attempt.get("raw_response")
        valid = (
            isinstance(raw, str)
            and bool(raw.strip())
            and selected is None
            and attempt.get("selected_option_id") is None
            and error_type is None
            and error_message is None
        )
    elif status == "adapter_error":
        valid = (
            attempt.get("raw_response") is None
            and attempt.get("selected_option_id") is None
            and isinstance(error_type, str)
            and error_type in ADAPTER_ERROR_TYPES
            and isinstance(error_message, str)
            and error_message in ADAPTER_ERROR_MESSAGES
            and not metadata
        )
    else:
        valid = False
    if not valid:
        raise DiagnosticCoverageError("attempt response fields conflict")
    if status != "adapter_error":
        if (
            metadata.get("model") not in {
                attempt.get("model_id"),
                FROZEN_CANONICAL_MODEL_IDS.get(attempt.get("model_id")),
            }
            or metadata.get("finish_reason") != "stop"
            or metadata.get("requested_seed") != attempt.get("seed")
            or type(metadata.get("requested_seed")) is not int
            or not isinstance(metadata.get("response_id"), str)
            or not metadata["response_id"]
            or type(metadata.get("attempt_count")) is not int
            or not 1 <= metadata["attempt_count"] <= 3
        ):
            raise DiagnosticCoverageError("attempt metadata lacks exact response attribution")
    return supplied_hash


def _percent(numerator: int, denominator: int) -> Optional[float]:
    if denominator == 0:
        return None
    return 100.0 * numerator / denominator


def _mean_boolean(rows: Sequence[Mapping[str, Any]], field: str) -> Optional[float]:
    values = [row[field] for row in rows if type(row.get(field)) is bool]
    if not values:
        return None
    return sum(values) / len(values)


def _spread(values: Sequence[Optional[float]]) -> Optional[float]:
    if not values or any(value is None for value in values):
        return None
    numeric = [float(value) for value in values if value is not None]
    if any(not math.isfinite(value) for value in numeric):
        return None
    return max(numeric) - min(numeric)


def _usage_totals(attempts: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    totals = {
        "attempts": len(attempts),
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "reasoning_tokens": 0,
        "total_tokens": 0,
        "cost": 0.0,
        "attempts_with_cost": 0,
        "attempts_missing_cost": 0,
    }
    for attempt in attempts:
        metadata = attempt.get("call_metadata")
        usage = metadata.get("usage") if isinstance(metadata, Mapping) else None
        usage = usage if isinstance(usage, Mapping) else {}
        for field in ("prompt_tokens", "completion_tokens", "total_tokens"):
            value = usage.get(field)
            if type(value) is int and value >= 0:
                totals[field] += value
        reasoning = usage.get("reasoning_tokens")
        if type(reasoning) is not int:
            details = usage.get("completion_tokens_details")
            reasoning = details.get("reasoning_tokens") if isinstance(details, Mapping) else None
        if type(reasoning) is int and reasoning >= 0:
            totals["reasoning_tokens"] += reasoning
        cost = usage.get("cost")
        if cost is None:
            cost = usage.get("upstream_inference_cost")
        if (
            not isinstance(cost, bool)
            and isinstance(cost, (int, float))
            and math.isfinite(float(cost))
            and cost >= 0
        ):
            totals["cost"] += float(cost)
            totals["attempts_with_cost"] += 1
        else:
            totals["attempts_missing_cost"] += 1
    totals["cost"] = round(totals["cost"], 12)
    totals["cost_coverage_percent"] = _percent(
        totals["attempts_with_cost"], totals["attempts"]
    )
    return totals


def _validate_collection(
    collection: Mapping[str, Any],
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    config: Mapping[str, Any],
) -> Tuple[bool, DiagnosticProtocol]:
    if not isinstance(collection, Mapping):
        raise DiagnosticCoverageError("diagnostic collection must be an object")
    if set(collection) != COLLECTION_FIELDS:
        raise DiagnosticCoverageError("collection fields do not match exact diagnostic schema")
    if not isinstance(config, Mapping) or set(config) != CONFIG_FIELDS:
        raise DiagnosticCoverageError("config fields do not match exact frozen schema")
    protocol = PROTOCOLS_BY_RUN_ID.get(config.get("run_id"))
    if protocol is None:
        raise DiagnosticCoverageError("analysis config is not in the frozen protocol registry")
    if (
        isinstance(bank, (str, bytes))
        or isinstance(gold, (str, bytes))
        or not isinstance(bank, Sequence)
        or not isinstance(gold, Sequence)
        or any(not isinstance(row, Mapping) for row in bank)
        or any(not isinstance(row, Mapping) for row in gold)
    ):
        raise DiagnosticCoverageError("bank/gold scoring rows must be object sequences")
    smoke = collection.get("status") == SMOKE_STATUS
    expected_status = SMOKE_STATUS if smoke else FULL_STATUS
    exact_top = {
        "schema_version": 1,
        "study_id": "10CB-ZEROSUM-P1",
        "run_id": protocol.run_id,
        "status": expected_status,
        "data_basis": "live_diagnostic",
        "eligible_for_empirical_decision": False,
        "official_blockers": BLOCKERS,
        "seed": 2026071001,
        "seed_count": 1,
        "record_type": "forced_anchor",
        "smoke": smoke,
    }
    for field, expected in exact_top.items():
        if collection.get(field) != expected or type(collection.get(field)) is not type(expected):
            raise DiagnosticCoverageError("collection metadata mismatch: %s" % field)
    frozen_config = {
        "schema_version": 1,
        "study_id": "10CB-ZEROSUM-P1",
        "run_id": protocol.run_id,
        "status": FULL_STATUS,
        "data_basis": "live_diagnostic",
        "eligible_for_empirical_decision": False,
        "record_type": "forced_anchor",
        "seed": 2026071001,
        "expected_items_per_model": 80,
        "expected_full_calls": 240,
        "official_blockers": BLOCKERS,
    }
    for field, expected in frozen_config.items():
        if config.get(field) != expected or type(config.get(field)) is not type(expected):
            raise DiagnosticCoverageError("frozen analysis config mismatch: %s" % field)
    if not _exact_frozen_mapping(config.get("thresholds"), EXPECTED_THRESHOLDS):
        raise DiagnosticCoverageError("analysis thresholds differ from frozen config")
    roster = config.get("model_roster")
    if roster != EXPECTED_ROSTER:
        raise DiagnosticCoverageError("analysis roster differs from frozen OpenAI panel")
    if not _exact_frozen_mapping(config.get("transport"), protocol.transport):
        raise DiagnosticCoverageError("analysis transport differs from frozen config")
    if (
        not isinstance(config.get("provenance"), Mapping)
        or set(config["provenance"]) != set(protocol.provenance_keys)
    ):
        raise DiagnosticCoverageError("analysis config provenance fields are invalid")
    if any(
        not isinstance(value, str) or SHA256_RE.fullmatch(value) is None
        for value in config["provenance"].values()
    ):
        raise DiagnosticCoverageError("analysis config provenance hashes are invalid")
    if (
        protocol.supersedes_config_sha256 is not None
        and config["provenance"].get("supersedes_config_sha256")
        != protocol.supersedes_config_sha256
    ):
        raise DiagnosticCoverageError("analysis config supersedes hash is invalid")
    forced = [row for row in bank if row.get("record_type") == "forced_anchor"]
    if len(forced) != 80:
        raise DiagnosticCoverageError("bank does not contain exactly 80 forced anchors")
    try:
        build_choice_key(bank, gold)
    except (KeyError, TypeError, ValueError) as error:
        raise DiagnosticCoverageError("private mechanical key is invalid") from error
    selected_forced = forced[:1] if smoke else forced
    expected = [
        (model["model_id"], model["family"], model["vendor"], item)
        for model in roster
        for item in selected_forced
    ]
    items = collection.get("items")
    attempts = collection.get("attempts")
    if not isinstance(items, list) or not isinstance(attempts, list):
        raise DiagnosticCoverageError("collection attempts/items must be lists")
    if (
        len(items) != len(expected)
        or collection.get("expected_scheduled_items") != len(expected)
        or type(collection.get("expected_scheduled_items")) is not int
    ):
        raise DiagnosticCoverageError("terminal item coverage is incomplete")
    provenance = collection.get("provenance")
    if not isinstance(provenance, Mapping) or set(provenance) != PROVENANCE_FIELDS:
        raise DiagnosticCoverageError("collection provenance fields are invalid")
    if (
        provenance.get("config_sha256") != protocol.config_sha256
        or PROTOCOLS_BY_CONFIG_SHA256.get(provenance.get("config_sha256"))
        is not protocol
    ):
        raise DiagnosticCoverageError("config SHA256 does not match frozen diagnostic")
    if _canonical_jsonl_hash(bank) != provenance.get("bank_sha256"):
        raise DiagnosticCoverageError("actual bank hash differs from collection provenance")
    if _canonical_jsonl_hash(gold) != provenance.get("gold_sha256"):
        raise DiagnosticCoverageError("actual gold hash differs from collection provenance")
    preflight = collection.get("preflight")
    if not isinstance(preflight, Mapping) or set(preflight) != PREFLIGHT_FIELDS:
        raise DiagnosticCoverageError("preflight fields do not match exact schema")
    exact_preflight_values = {
        "forced_anchor_count": 80,
        "scheduled_item_count": len(expected),
        "model_count": 3,
        "vendor_count": 1,
        "seed": 2026071001,
        "catalog_verified": True,
        "catalog_model_ids": [row["model_id"] for row in EXPECTED_ROSTER],
        "smoke": smoke,
    }
    if (
        preflight.get("config_sha256") != provenance.get("config_sha256")
        or preflight.get("bank_sha256") != provenance.get("bank_sha256")
        or preflight.get("gold_sha256") != provenance.get("gold_sha256")
        or any(
            preflight.get(field) != frozen
            or type(preflight.get(field)) is not type(frozen)
            for field, frozen in exact_preflight_values.items()
        )
    ):
        raise DiagnosticCoverageError("preflight evidence conflicts with collection")
    record_by_id = {row["id"]: row for row in selected_forced}
    if len(record_by_id) != len(selected_forced):
        raise DiagnosticCoverageError("forced scoring item IDs are not unique")
    for item_row, (model_id, family, vendor, record) in zip(items, expected):
        if not isinstance(item_row, Mapping):
            raise DiagnosticCoverageError("terminal item row must be an object")
        if set(item_row) != ITEM_FIELDS:
            raise DiagnosticCoverageError("terminal item fields do not match exact schema")
        identity = (
            item_row.get("model_id"), item_row.get("model_family"),
            item_row.get("vendor"), item_row.get("item_id"),
            item_row.get("core_id"), item_row.get("rho"), item_row.get("domain"),
        )
        expected_identity = (
            model_id, family, vendor, record["id"], record["core_id"],
            record["rho"], record["domain"],
        )
        if identity != expected_identity:
            raise DiagnosticCoverageError("terminal item schedule/order mismatch")
        if (
            item_row.get("schema_version") != 1
            or type(item_row.get("schema_version")) is not int
            or item_row.get("study_id") != "10CB-ZEROSUM-P1"
            or item_row.get("run_id") != protocol.run_id
            or item_row.get("status") != expected_status
            or item_row.get("data_basis") != "live_diagnostic"
            or item_row.get("eligible_for_empirical_decision") is not False
            or item_row.get("seed") != 2026071001
            or type(item_row.get("seed")) is not int
            or type(item_row.get("terminal_attempt_index")) is not int
            or item_row.get("terminal_attempt_index") not in (1, 2)
            or type(item_row.get("rho")) is not type(record.get("rho"))
            or item_row.get("record_type") != "forced_anchor"
        ):
            raise DiagnosticCoverageError("terminal item frozen identity fields are invalid")
        if item_row.get("response_status") not in {"answered", "parked"}:
            raise DiagnosticCoverageError("terminal response status is invalid")
        if item_row.get("response_status") == "answered":
            options = {option["id"] for option in record["options"]}
            raw_selected = _strict_option(item_row.get("raw_response"), sorted(options))
            if (
                item_row.get("selected_option_id") not in options
                or item_row.get("selected_option_id") != raw_selected
                or item_row.get("park_reason") is not None
            ):
                raise DiagnosticCoverageError("answered terminal choice is invalid")
        elif item_row.get("selected_option_id") is not None or not isinstance(item_row.get("park_reason"), str):
            raise DiagnosticCoverageError("parked terminal row is invalid")
    if provenance.get("audit_sha256") != _canonical_hash(attempts):
        raise DiagnosticCoverageError("attempt audit hash mismatch")
    if provenance.get("response_sha256") != _canonical_hash(items):
        raise DiagnosticCoverageError("terminal response hash mismatch")
    for field in ("config_sha256", "bank_sha256", "gold_sha256"):
        value = provenance.get(field)
        if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
            raise DiagnosticCoverageError("artifact provenance hash is invalid")
        if any(row.get(field) != value for row in items):
            raise DiagnosticCoverageError("terminal item artifact provenance mismatch")
        if any(row.get(field) != value for row in attempts):
            raise DiagnosticCoverageError("attempt artifact provenance mismatch")
    if provenance.get("bank_sha256") != config.get("provenance", {}).get("bank_sha256"):
        raise DiagnosticCoverageError("bank hash does not match frozen config")
    if provenance.get("gold_sha256") != config.get("provenance", {}).get("gold_sha256"):
        raise DiagnosticCoverageError("gold hash does not match frozen config")

    cursor = 0
    previous_attempt_hash = ZERO_HASH
    response_ids = set()
    for item in items:
        count = item.get("attempt_count")
        if type(count) is not int or count not in (1, 2):
            raise DiagnosticCoverageError("terminal attempt count is invalid")
        group = attempts[cursor:cursor + count]
        if len(group) != count:
            raise DiagnosticCoverageError("attempt audit is shorter than terminal coverage")
        if any(
            row.get("model_id") != item["model_id"] or row.get("item_id") != item["item_id"]
            for row in group
        ):
            raise DiagnosticCoverageError("attempt audit order does not match terminal items")
        if [row.get("attempt_index") for row in group] != list(range(1, count + 1)):
            raise DiagnosticCoverageError("attempt indices are incomplete")
        record = record_by_id[item["item_id"]]
        registered = [option["id"] for option in record["options"]]
        for attempt in group:
            previous_attempt_hash = _validate_attempt_semantics(
                attempt,
                registered,
                expected_previous_hash=previous_attempt_hash,
                provenance=provenance,
                protocol=protocol,
            )
            reconstructed_request_id = _expected_request_id(
                record,
                item["model_id"],
                item["seed"],
                attempt["attempt_index"],
            )
            if (
                attempt.get("status") != expected_status
                or attempt.get("model_family") != item.get("model_family")
                or attempt.get("vendor") != item.get("vendor")
                or attempt.get("core_id") != item.get("core_id")
                or attempt.get("rho") != item.get("rho")
                or attempt.get("domain") != item.get("domain")
                or attempt.get("request_id") != reconstructed_request_id
            ):
                raise DiagnosticCoverageError(
                    "attempt identity or request_id conflicts with frozen schedule"
                )
            metadata = attempt.get("call_metadata")
            response_id = metadata.get("response_id") if isinstance(metadata, Mapping) else None
            if response_id is not None:
                if response_id in response_ids:
                    raise DiagnosticCoverageError("response attribution ID was replayed")
                response_ids.add(response_id)
        if group[-1].get("attempt_sha256") != item.get("terminal_attempt_sha256"):
            raise DiagnosticCoverageError("terminal item does not bind to final attempt")
        if count == 2 and group[0].get("response_status") == "valid_choice":
            raise DiagnosticCoverageError("valid first choice received a discretionary replacement")
        if item["response_status"] == "parked" and count != 2:
            raise DiagnosticCoverageError("parked item did not receive exactly one repair")
        if item["response_status"] == "answered" and group[-1].get("response_status") != "valid_choice":
            raise DiagnosticCoverageError("answered item does not end in a valid choice")
        if item["response_status"] == "parked" and group[-1].get("response_status") == "valid_choice":
            raise DiagnosticCoverageError("parked item ends in a valid choice")
        terminal_status = group[-1].get("response_status")
        expected_park_reason = {
            "adapter_error": "adapter_error_after_repair",
            "blank_response": "blank_response_after_repair",
            "invalid_choice": "invalid_choice_after_repair",
        }.get(terminal_status)
        if item["response_status"] == "answered":
            if item.get("park_reason") is not None:
                raise DiagnosticCoverageError("answered item park_reason must be null")
        elif item.get("park_reason") != expected_park_reason:
            raise DiagnosticCoverageError(
                "parked item park_reason does not match terminal attempt"
            )
        if (
            group[-1].get("raw_response") != item.get("raw_response")
            or group[-1].get("selected_option_id") != item.get("selected_option_id")
            or group[-1].get("request_id") != item.get("request_id")
            or group[-1].get("attempt_index") != item.get("terminal_attempt_index")
        ):
            raise DiagnosticCoverageError("terminal item fields disagree with final attempt")
        cursor += count
    if cursor != len(attempts):
        raise DiagnosticCoverageError("attempt audit contains duplicate or unbound rows")
    return smoke, protocol


def _model_metrics(
    roster: Mapping[str, str],
    scored: Sequence[Mapping[str, Any]],
    attempts: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    rows = [row for row in scored if row["model_id"] == roster["model_id"]]
    valid = [row for row in rows if row["analysis_status"] == "answered"]
    parked = [row for row in rows if row["analysis_status"] == "parked"]
    rho_rows = []
    endpoint_rates = {}
    for rho in RHO_GRID:
        subset = [row for row in rows if row["rho"] == rho]
        rho_valid = [row for row in subset if row["analysis_status"] == "answered"]
        rho_parked = [row for row in subset if row["analysis_status"] == "parked"]
        positional = _mean_boolean(rho_valid, "positional")
        if rho in (-1, 1):
            endpoint_rates[rho] = positional
        rho_rows.append(
            {
                "rho": rho,
                "response_n": len(subset),
                "valid_n": len(rho_valid),
                "parked_n": len(rho_parked),
                "valid_response_rate_percent": _percent(len(rho_valid), len(subset)),
                "mechanical_accuracy_percent": (
                    None
                    if not rho_valid
                    else 100.0 * sum(row["mechanical_correct"] for row in rho_valid) / len(rho_valid)
                ),
                "positional_rate_percent": None if positional is None else 100.0 * positional,
            }
        )
    neg = endpoint_rates.get(-1)
    pos = endpoint_rates.get(1)
    delta = None if neg is None or pos is None else neg - pos
    model_attempts = [row for row in attempts if row["model_id"] == roster["model_id"]]
    return {
        "model_id": roster["model_id"],
        "model_family": roster["family"],
        "vendor": roster["vendor"],
        "response_count": len(rows),
        "valid_count": len(valid),
        "parked_count": len(parked),
        "valid_response_rate_percent": _percent(len(valid), len(rows)),
        "parked_rate_percent": _percent(len(parked), len(rows)),
        "mechanical_accuracy_percent": (
            None
            if not valid
            else 100.0 * sum(row["mechanical_correct"] for row in valid) / len(valid)
        ),
        "per_rho": rho_rows,
        "endpoint_positional_rate_rho_minus1_percent": None if neg is None else 100.0 * neg,
        "endpoint_positional_rate_rho_plus1_percent": None if pos is None else 100.0 * pos,
        "endpoint_delta": delta,
        "zs_design_100": None if delta is None else zs_design_100(delta),
        "usage": _usage_totals(model_attempts),
    }


def analyze_diagnostic(
    collection: Mapping[str, Any],
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    *,
    config: Mapping[str, Any],
) -> Dict[str, Any]:
    """Score exact terminal choices and apply only precommitted diagnostics."""

    smoke, protocol = _validate_collection(collection, bank, gold, config)
    choice_key = build_choice_key(bank, gold)
    scored = score_forced_rows(collection["items"], choice_key)
    roster = config["model_roster"]
    smoke_validation_passed = None
    if smoke:
        expected_smoke_models = [row["model_id"] for row in roster]
        smoke_validation_passed = (
            len(scored) == 3
            and [row.get("model_id") for row in scored] == expected_smoke_models
            and all(
                row.get("analysis_status") == "answered"
                and row.get("valid_choice") is True
                for row in scored
            )
        )
    models = [
        _model_metrics(row, scored, collection["attempts"])
        for row in roster
    ]
    accuracy_spread = None if smoke else _spread(
        [row["mechanical_accuracy_percent"] for row in models]
    )
    zs_spread = None if smoke else _spread([row["zs_design_100"] for row in models])
    thresholds = deepcopy(dict(config["thresholds"]))
    if smoke:
        checks = {
            "valid_response_rate_gate": None,
            "ceiling_saturation": None,
            "accuracy_discrimination": None,
            "structural_discrimination": None,
        }
        classification = "SMOKE_ONLY_NO_SATURATION_CONCLUSION"
    else:
        valid_gate = all(
            row["valid_response_rate_percent"] is not None
            and row["valid_response_rate_percent"] >= thresholds["valid_response_rate_min_percent"]
            for row in models
        )
        ceiling = valid_gate and all(
            row["mechanical_accuracy_percent"] is not None
            and row["mechanical_accuracy_percent"] >= thresholds["ceiling_accuracy_min_percent"]
            for row in models
        )
        accuracy_discrimination = (
            valid_gate
            and accuracy_spread is not None
            and accuracy_spread >= thresholds["accuracy_discrimination_spread_min_points"]
        )
        structural_discrimination = (
            valid_gate
            and zs_spread is not None
            and zs_spread >= thresholds["zs_discrimination_spread_min_points"]
        )
        checks = {
            "valid_response_rate_gate": valid_gate,
            "ceiling_saturation": ceiling,
            "accuracy_discrimination": accuracy_discrimination,
            "structural_discrimination": structural_discrimination,
        }
        if not valid_gate:
            classification = "INSUFFICIENT_VALID_RESPONSE_COVERAGE"
        elif accuracy_discrimination or structural_discrimination:
            classification = "WITHIN_OPENAI_DESCRIPTIVE_DISCRIMINATION"
        elif ceiling:
            classification = "WITHIN_OPENAI_CEILING_SATURATION"
        else:
            classification = "WITHIN_OPENAI_NO_FROZEN_PATTERN"
    result = deepcopy(dict(collection))
    result.update(
        {
            "eligible_for_empirical_decision": False,
            "official_blockers": list(BLOCKERS),
            "diagnostic_scope": "descriptive_within_openai_only",
            "thresholds": thresholds,
            "models": models,
            "cross_model": {
                "accuracy_spread_points": accuracy_spread,
                "zs_spread_points": zs_spread,
            },
            "checks": checks,
            "classification": classification,
            "smoke_validation_passed": smoke_validation_passed,
            "usage": _usage_totals(collection["attempts"]),
            "provenance": {
                **deepcopy(dict(collection["provenance"])),
                "audit_sha256": _canonical_hash(collection["attempts"]),
                "response_sha256": _canonical_hash(collection["items"]),
            },
        }
    )
    if protocol.revision == "R2":
        result["protocol_revision"] = protocol.revision
        result["effective_reasoning_effort"] = protocol.effective_reasoning_effort
    return result


def _display(value: Any, *, digits: int = 2) -> str:
    if value is None:
        return "NOT COMPUTED"
    if type(value) is bool:
        return "PASS" if value else "NO"
    if isinstance(value, float):
        return ("%%.%df" % digits) % value
    return str(value)


def _threshold_display(value: Any) -> str:
    if not isinstance(value, bool) and isinstance(value, (int, float)):
        return _display(float(value))
    return _display(value)


def render_diagnostic_markdown(result: Mapping[str, Any]) -> str:
    """Render a deterministic report using only machine-result values."""

    status = result.get("status")
    smoke = status == SMOKE_STATUS
    lines = [
        "# %s" % status,
        "",
        "> **Diagnostic only.** `eligible_for_empirical_decision: false`. This one-seed, descriptive within-OpenAI comparison does not pass any official gate.",
        "",
        "- Study: `%s`" % result.get("study_id"),
        "- Run: `%s`" % result.get("run_id"),
    ]
    if "protocol_revision" in result or "effective_reasoning_effort" in result:
        lines.extend(
            [
                "- Transport revision: `%s`" % result.get("protocol_revision"),
                "- Effective reasoning effort: `%s`"
                % result.get("effective_reasoning_effort"),
            ]
        )
    lines.extend(
        [
        "- Status: `%s`" % status,
        "- Data basis: `%s`" % result.get("data_basis"),
        "- Seed: `%s` (one seed)" % result.get("seed"),
        "- Eligible for empirical decision: `false`",
        "- Official blockers: `%s`" % "`, `".join(result.get("official_blockers", [])),
        "",
        ]
    )
    if smoke:
        lines.extend(
            [
                "## Smoke result",
                "",
                "- Smoke validation passed: %s"
                % _display(result.get("smoke_validation_passed")),
                "",
                "This is `SMOKE_ONLY`; it has no saturation conclusion and no discrimination conclusion.",
                "",
            ]
        )
    lines.extend(
        [
            "## Mechanical forced-choice results",
            "",
            "| Model | Valid / responses | Valid rate | Parked rate | Accuracy among valid | Endpoint delta | ZS_design_100 |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in result.get("models", []):
        lines.append(
            "| `%s` | %s / %s | %s%% | %s%% | %s%% | %s | %s |"
            % (
                row.get("model_id"),
                row.get("valid_count"),
                row.get("response_count"),
                _display(row.get("valid_response_rate_percent")),
                _display(row.get("parked_rate_percent")),
                _display(row.get("mechanical_accuracy_percent")),
                _display(row.get("endpoint_delta"), digits=4),
                _display(row.get("zs_design_100")),
            )
        )
    thresholds = result.get("thresholds", {})
    lines.extend(
        [
            "",
            "## Frozen thresholds",
            "",
            "- Valid response rate minimum: %s%%"
            % _threshold_display(thresholds.get("valid_response_rate_min_percent")),
            "- Ceiling accuracy minimum: %s%%"
            % _threshold_display(thresholds.get("ceiling_accuracy_min_percent")),
            "- Accuracy discrimination spread minimum: %s points"
            % _threshold_display(thresholds.get("accuracy_discrimination_spread_min_points")),
            "- ZS discrimination spread minimum: %s points"
            % _threshold_display(thresholds.get("zs_discrimination_spread_min_points")),
            "",
            "## Per-rho mechanical results",
            "",
            "| Model | rho | Responses | Valid | Parked | Valid rate | Accuracy among valid | Positional rate |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for model in result.get("models", []):
        for rho_row in model.get("per_rho", []):
            lines.append(
                "| `%s` | %s | %s | %s | %s | %s%% | %s%% | %s%% |"
                % (
                    model.get("model_id"),
                    _display(rho_row.get("rho"), digits=4),
                    rho_row.get("response_n"),
                    rho_row.get("valid_n"),
                    rho_row.get("parked_n"),
                    _display(rho_row.get("valid_response_rate_percent")),
                    _display(rho_row.get("mechanical_accuracy_percent")),
                    _display(rho_row.get("positional_rate_percent")),
                )
            )
    cross = result.get("cross_model", {})
    checks = result.get("checks", {})
    lines.extend(
        [
            "",
            "## Frozen descriptive checks",
            "",
            "- Classification: `%s`" % result.get("classification"),
            "- Accuracy spread: %s points" % _display(cross.get("accuracy_spread_points")),
            "- ZS spread: %s points" % _display(cross.get("zs_spread_points")),
            "- Valid-response prerequisite: %s" % _display(checks.get("valid_response_rate_gate")),
            "- Ceiling saturation check: %s" % _display(checks.get("ceiling_saturation")),
            "- Accuracy-discrimination check: %s" % _display(checks.get("accuracy_discrimination")),
            "- Structural-discrimination check: %s" % _display(checks.get("structural_discrimination")),
            "",
            "These checks are descriptive within-OpenAI only. They do not discharge `NOT_RUN_HUMAN` or `SINGLE_MODEL_VENDOR`.",
            "",
            "## Usage and provenance",
            "",
        ]
    )
    usage = result.get("usage", {})
    lines.extend(
        [
            "- Attempts: %s" % usage.get("attempts"),
            "- Prompt tokens: %s" % usage.get("prompt_tokens"),
            "- Completion tokens: %s" % usage.get("completion_tokens"),
            "- Reasoning tokens: %s" % usage.get("reasoning_tokens"),
            "- Total tokens: %s" % usage.get("total_tokens"),
            "- Cost: %s" % _display(usage.get("cost"), digits=6),
            "- Cost metadata coverage: %s / %s attempts (%s%%); %s attempts missing cost"
            % (
                usage.get("attempts_with_cost"),
                usage.get("attempts"),
                _display(usage.get("cost_coverage_percent")),
                usage.get("attempts_missing_cost"),
            ),
        ]
    )
    for field in (
        "config_sha256", "bank_sha256", "gold_sha256", "audit_sha256",
        "response_sha256", "smoke_result_sha256", "smoke_manifest_sha256",
    ):
        if field in result.get("provenance", {}):
            lines.append("- %s: `%s`" % (field, result["provenance"][field]))
    lines.append("")
    return "\n".join(lines)


__all__ = [
    "DiagnosticCoverageError",
    "analyze_diagnostic",
    "render_diagnostic_markdown",
]
