#!/usr/bin/env python3
"""Run the bounded ZEROSUM forced-anchor OpenRouter diagnostic.

This is deliberately separate from ``run_p1.py``.  It is a one-seed,
single-vendor, pre-calibration mechanical diagnostic and can never satisfy the
official human-classifier or multi-vendor model gates.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Tuple


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from harness.model_adapters import build_requests_for_record  # noqa: E402
from harness.openrouter_client import (  # noqa: E402
    FROZEN_CANONICAL_MODEL_IDS,
    REQUESTED_MODEL_ROSTER,
    OpenRouterError,
    openrouter_client_from_roster,
    verify_requested_model_catalog,
)
from harness.openrouter_protocols import (  # noqa: E402
    PROTOCOLS_BY_CONFIG_SHA256,
    PROTOCOLS_BY_RUN_ID,
    V1_CONFIG_SHA256,
    V1_RUN_ID,
)
from scoring.forced_choice import build_choice_key  # noqa: E402
from zerosum_common import read_jsonl  # noqa: E402


FULL_STATUS = "LIVE_SINGLE_VENDOR_PRECALIBRATION_DIAGNOSTIC"
SMOKE_STATUS = "SMOKE_ONLY"
STUDY_ID = "10CB-ZEROSUM-P1"
RUN_ID = V1_RUN_ID
DATA_BASIS = "live_diagnostic"
SEED = 2026071001
FROZEN_CONFIG_SHA256 = V1_CONFIG_SHA256
REPAIR_INSTRUCTION = (
    "Return exactly one option letter from: {letters}. "
    "Do not include punctuation or explanation."
)
ZERO_HASH = "0" * 64
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_OPTION = re.compile(r"^\s*([A-Za-z])\s*$")
_EXPECTED_ROSTER = tuple(dict(row) for row in REQUESTED_MODEL_ROSTER)
_EXPECTED_THRESHOLDS = {
    "valid_response_rate_min_percent": 95,
    "ceiling_accuracy_min_percent": 90,
    "accuracy_discrimination_spread_min_points": 10,
    "zs_discrimination_spread_min_points": 20,
}
_ROOT_CONFIG_KEYS = {
    "schema_version",
    "study_id",
    "run_id",
    "status",
    "data_basis",
    "eligible_for_empirical_decision",
    "record_type",
    "seed",
    "expected_items_per_model",
    "expected_full_calls",
    "model_roster",
    "transport",
    "thresholds",
    "official_blockers",
    "provenance",
}
_IDENTITY_FIELDS = {
    "schema_version",
    "study_id",
    "run_id",
    "status",
    "data_basis",
    "eligible_for_empirical_decision",
    "model_id",
    "model_family",
    "vendor",
    "seed",
    "item_id",
    "core_id",
    "rho",
    "domain",
    "record_type",
    "attempt_index",
    "response_status",
    "raw_response",
    "selected_option_id",
    "call_metadata",
    "error_type",
    "error_message",
    "request_id",
    "config_sha256",
    "bank_sha256",
    "gold_sha256",
    "previous_attempt_sha256",
    "attempt_sha256",
}
_SUCCESS_METADATA_FIELDS = {
    "response_id",
    "model",
    "finish_reason",
    "usage",
    "requested_seed",
    "attempt_count",
}
_USAGE_NUMBER_FIELDS = {
    "prompt_tokens",
    "completion_tokens",
    "reasoning_tokens",
    "total_tokens",
    "accepted_prediction_tokens",
    "rejected_prediction_tokens",
    "cached_tokens",
    "audio_tokens",
    "image_tokens",
    "prompt_audio_tokens",
    "cost",
    "upstream_inference_cost",
}
_USAGE_DETAIL_FIELDS = {
    "completion_tokens_details",
    "prompt_tokens_details",
    "cost_details",
}
_ADAPTER_ERROR_TYPES = {
    "OpenRouterError",
    "OpenRouterConfigurationError",
    "OpenRouterRequestError",
    "OpenRouterTransportError",
    "OpenRouterResponseError",
    "OpenRouterCatalogError",
    "AdapterMetadataError",
}


class DiagnosticPreflightError(RuntimeError):
    """Raised before generation when frozen diagnostic inputs disagree."""


class DiagnosticResumeError(RuntimeError):
    """Raised before generation when an attempt checkpoint is not trustworthy."""


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_json_bytes(payload: Any) -> bytes:
    return json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _object_hash(payload: Any) -> str:
    return _sha256(_canonical_json_bytes(payload))


def _decode_config(payload: bytes) -> Mapping[str, Any]:
    try:
        decoded = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise DiagnosticPreflightError("config bytes are not valid UTF-8 JSON") from None
    if not isinstance(decoded, Mapping):
        raise DiagnosticPreflightError("config JSON root must be an object")
    return decoded


def _decode_jsonl(payload: bytes, label: str) -> List[Dict[str, Any]]:
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError:
        raise DiagnosticPreflightError("%s bytes are not valid UTF-8" % label) from None
    rows = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except ValueError:
            raise DiagnosticPreflightError(
                "%s line %d is not valid JSON" % (label, line_number)
            ) from None
        if not isinstance(row, dict):
            raise DiagnosticPreflightError(
                "%s line %d is not an object" % (label, line_number)
            )
        rows.append(row)
    return rows


def _canonical_roster(value: Any) -> List[Dict[str, str]]:
    if not isinstance(value, list):
        raise DiagnosticPreflightError("model_roster must be a list")
    canonical = []
    for row in value:
        if not isinstance(row, Mapping) or set(row) != {"model_id", "family", "vendor"}:
            raise DiagnosticPreflightError("model roster entries must contain exact identity fields")
        candidate = {}
        for field in ("model_id", "family", "vendor"):
            entry = row.get(field)
            if not isinstance(entry, str) or not entry or entry != " ".join(entry.split()):
                raise DiagnosticPreflightError("model roster identifiers must be canonical text")
            candidate[field] = entry
        canonical.append(candidate)
    return canonical


def _protocol_for_config(config: Mapping[str, Any]) -> Any:
    run_id = config.get("run_id") if isinstance(config, Mapping) else None
    protocol = PROTOCOLS_BY_RUN_ID.get(run_id)
    if protocol is None:
        raise DiagnosticPreflightError("run_id is not in the frozen protocol registry")
    return protocol


def _validate_config(config: Mapping[str, Any]) -> Any:
    if not isinstance(config, Mapping) or set(config) != _ROOT_CONFIG_KEYS:
        raise DiagnosticPreflightError("diagnostic config fields do not match frozen schema")
    protocol = _protocol_for_config(config)
    exact = {
        "schema_version": 1,
        "study_id": STUDY_ID,
        "run_id": protocol.run_id,
        "status": FULL_STATUS,
        "data_basis": DATA_BASIS,
        "eligible_for_empirical_decision": False,
        "record_type": "forced_anchor",
        "seed": SEED,
        "expected_items_per_model": 80,
        "expected_full_calls": 240,
        "official_blockers": ["NOT_RUN_HUMAN", "SINGLE_MODEL_VENDOR"],
    }
    for field, expected in exact.items():
        if config.get(field) != expected or type(config.get(field)) is not type(expected):
            raise DiagnosticPreflightError("frozen config mismatch: %s" % field)
    if _canonical_roster(config.get("model_roster")) != list(_EXPECTED_ROSTER):
        raise DiagnosticPreflightError("model roster does not match requested OpenRouter panel")
    thresholds = config.get("thresholds")
    if (
        not isinstance(thresholds, Mapping)
        or set(thresholds) != set(_EXPECTED_THRESHOLDS)
        or any(
            thresholds.get(field) != expected
            or type(thresholds.get(field)) is not type(expected)
            for field, expected in _EXPECTED_THRESHOLDS.items()
        )
    ):
        raise DiagnosticPreflightError("diagnostic thresholds do not match frozen values")
    if any(type(value) is not int or not 0 <= value <= 100 for value in thresholds.values()):
        raise DiagnosticPreflightError("diagnostic thresholds must be finite percentages")
    transport = config.get("transport")
    if (
        not isinstance(transport, Mapping)
        or set(transport) != set(protocol.transport)
        or any(
            transport.get(field) != expected
            or type(transport.get(field)) is not type(expected)
            for field, expected in protocol.transport.items()
        )
    ):
        raise DiagnosticPreflightError("transport config does not match frozen values")
    provenance = config.get("provenance")
    if (
        not isinstance(provenance, Mapping)
        or set(provenance) != set(protocol.provenance_keys)
    ):
        raise DiagnosticPreflightError("config provenance fields are invalid")
    if any(not isinstance(value, str) or _SHA256.fullmatch(value) is None for value in provenance.values()):
        raise DiagnosticPreflightError("config provenance hashes are invalid")
    if protocol.supersedes_config_sha256 is not None and provenance.get(
        "supersedes_config_sha256"
    ) != protocol.supersedes_config_sha256:
        raise DiagnosticPreflightError("config supersedes hash is invalid")
    return protocol


def _validate_artifacts(
    config: Mapping[str, Any],
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    *,
    config_bytes: bytes,
    bank_bytes: bytes,
    gold_bytes: bytes,
) -> Tuple[List[Mapping[str, Any]], Dict[str, str]]:
    protocol = _validate_config(config)
    if _decode_config(config_bytes) != config:
        raise DiagnosticPreflightError("config bytes do not decode to the supplied config")
    if _decode_jsonl(bank_bytes, "bank") != list(bank):
        raise DiagnosticPreflightError("bank bytes do not decode to the supplied rows")
    if _decode_jsonl(gold_bytes, "gold") != list(gold):
        raise DiagnosticPreflightError("gold bytes do not decode to the supplied rows")
    hashes = {
        "config_sha256": _sha256(config_bytes),
        "bank_sha256": _sha256(bank_bytes),
        "gold_sha256": _sha256(gold_bytes),
    }
    if (
        hashes["config_sha256"] != protocol.config_sha256
        or PROTOCOLS_BY_CONFIG_SHA256.get(hashes["config_sha256"]) != protocol
    ):
        raise DiagnosticPreflightError("config SHA256 does not match frozen diagnostic")
    if config["provenance"]["bank_sha256"] != hashes["bank_sha256"]:
        raise DiagnosticPreflightError("bank SHA256 does not match frozen config")
    if config["provenance"]["gold_sha256"] != hashes["gold_sha256"]:
        raise DiagnosticPreflightError("gold SHA256 does not match frozen config")
    if len(bank) != 632 or len(gold) != 632:
        raise DiagnosticPreflightError("bank and gold must each contain exactly 632 rows")
    bank_ids = [row.get("id") if isinstance(row, Mapping) else None for row in bank]
    gold_ids = [row.get("id") if isinstance(row, Mapping) else None for row in gold]
    if bank_ids != gold_ids or len(set(bank_ids)) != len(bank_ids) or None in bank_ids:
        raise DiagnosticPreflightError("bank/gold IDs must be unique and exactly aligned")
    forced = [row for row in bank if row.get("record_type") == "forced_anchor"]
    forced_gold = [row for row in gold if row.get("record_type") == "forced_anchor"]
    if len(forced) != 80 or len(forced_gold) != 80:
        raise DiagnosticPreflightError("bank/gold must contain exactly 80 forced anchors")
    if [row["id"] for row in forced] != [row["id"] for row in forced_gold]:
        raise DiagnosticPreflightError("forced public/private rows are not aligned")
    for record in forced:
        options = record.get("options")
        if not isinstance(options, list) or len(options) < 2:
            raise DiagnosticPreflightError("forced anchor options are incomplete")
        identifiers = [option.get("id") if isinstance(option, Mapping) else None for option in options]
        if (
            None in identifiers
            or len(set(identifiers)) != len(identifiers)
            or any(not isinstance(value, str) or len(value) != 1 or value.upper() != value for value in identifiers)
        ):
            raise DiagnosticPreflightError("forced option identifiers must be unique uppercase letters")
        requests = build_requests_for_record(record)
        if len(requests) != 1:
            raise DiagnosticPreflightError("forced anchors must produce exactly one request")
    try:
        build_choice_key(bank, gold)
    except (KeyError, TypeError, ValueError) as error:
        raise DiagnosticPreflightError("private forced choice key is invalid") from error
    return forced, hashes


def _validate_clients(config: Mapping[str, Any], clients: Sequence[Any]) -> Dict[str, Any]:
    if isinstance(clients, (str, bytes)) or not isinstance(clients, Sequence):
        raise DiagnosticPreflightError("clients must be an ordered sequence")
    observed = []
    client_by_model = {}
    for client in clients:
        try:
            identity = (client.model_id, client.family, client.vendor)
        except AttributeError:
            raise DiagnosticPreflightError("client identity metadata is incomplete") from None
        if not callable(getattr(client, "generate", None)):
            raise DiagnosticPreflightError("client generate method is not callable")
        observed.append(identity)
        if identity[0] in client_by_model:
            raise DiagnosticPreflightError("duplicate client model_id")
        client_by_model[identity[0]] = client
    expected = [
        (row["model_id"], row["family"], row["vendor"])
        for row in config["model_roster"]
    ]
    if observed != expected:
        raise DiagnosticPreflightError("client order/identity does not exactly match roster")
    if len({row[2] for row in observed}) != 1:
        raise DiagnosticPreflightError("diagnostic client roster must have exactly one vendor")
    return client_by_model


def _validate_catalog(config: Mapping[str, Any], catalog_result: Mapping[str, Any]) -> None:
    expected_ids = [row["model_id"] for row in config["model_roster"]]
    if (
        not isinstance(catalog_result, Mapping)
        or set(catalog_result) != {"verified", "model_ids"}
        or catalog_result.get("verified") is not True
        or type(catalog_result.get("verified")) is not bool
        or catalog_result.get("model_ids") != expected_ids
        or not isinstance(catalog_result.get("model_ids"), list)
    ):
        raise DiagnosticPreflightError("exact requested model catalog verification is required")


def preflight_diagnostic(
    config: Mapping[str, Any],
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    *,
    clients: Sequence[Any],
    catalog_result: Mapping[str, Any],
    config_bytes: bytes,
    bank_bytes: bytes,
    gold_bytes: bytes,
    smoke: bool,
) -> Dict[str, Any]:
    """Purely validate the complete frozen schedule before any generation."""

    if type(smoke) is not bool:
        raise DiagnosticPreflightError("smoke must be boolean")
    _validate_config(config)
    forced, hashes = _validate_artifacts(
        config,
        bank,
        gold,
        config_bytes=config_bytes,
        bank_bytes=bank_bytes,
        gold_bytes=gold_bytes,
    )
    _validate_clients(config, clients)
    _validate_catalog(config, catalog_result)
    scheduled = len(config["model_roster"]) * (1 if smoke else len(forced))
    expected = 3 if smoke else config["expected_full_calls"]
    if scheduled != expected:
        raise DiagnosticPreflightError("computed schedule does not match frozen call count")
    return {
        **hashes,
        "forced_anchor_count": len(forced),
        "scheduled_item_count": scheduled,
        "model_count": len(config["model_roster"]),
        "vendor_count": 1,
        "seed": config["seed"],
        "catalog_verified": True,
        "catalog_model_ids": list(catalog_result["model_ids"]),
        "smoke": smoke,
    }


def parse_option_letter(raw_response: Any, registered_options: Sequence[str]) -> Optional[str]:
    """Return a registered option only for an entire single-letter response."""

    if not isinstance(raw_response, str):
        return None
    match = _OPTION.fullmatch(raw_response)
    if match is None:
        return None
    selected = match.group(1).upper()
    registered = {
        value.upper()
        for value in registered_options
        if isinstance(value, str) and len(value) == 1
    }
    return selected if selected in registered else None


def _safe_usage(value: Any) -> Dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    safe = {}
    for key, child in value.items():
        if key in _USAGE_DETAIL_FIELDS and isinstance(child, Mapping):
            safe[key] = _safe_usage(child)
        elif key in _USAGE_NUMBER_FIELDS:
            if (
                isinstance(child, bool)
                or not isinstance(child, (int, float))
                or not math.isfinite(float(child))
                or child < 0
            ):
                continue
            if key.endswith("tokens") and type(child) is not int:
                continue
            safe[key] = child
        elif key == "is_byok" and type(child) is bool:
            safe[key] = child
    return safe


def _safe_call_metadata(client: Any, *, model_id: str, seed: int) -> Dict[str, Any]:
    metadata = getattr(client, "last_call_metadata", None)
    if not isinstance(metadata, Mapping):
        return {}
    safe = {}
    response_id = metadata.get("response_id")
    if isinstance(response_id, str) and response_id.strip() == response_id and response_id:
        safe["response_id"] = response_id
    actual_model = metadata.get("model")
    if actual_model in {model_id, FROZEN_CANONICAL_MODEL_IDS[model_id]}:
        safe["model"] = actual_model
    finish_reason = metadata.get("finish_reason")
    if isinstance(finish_reason, str) and finish_reason.strip() == finish_reason and finish_reason:
        safe["finish_reason"] = finish_reason
    if metadata.get("requested_seed") == seed and type(metadata.get("requested_seed")) is int:
        safe["requested_seed"] = seed
    attempt_count = metadata.get("attempt_count")
    if type(attempt_count) is int and 1 <= attempt_count <= 3:
        safe["attempt_count"] = attempt_count
    usage = _safe_usage(metadata.get("usage"))
    if usage:
        safe["usage"] = usage
    return safe


def _metadata_attributed(metadata: Mapping[str, Any], *, model_id: str, seed: int) -> bool:
    """Require the approved transport's server-attribution fields."""

    return (
        isinstance(metadata.get("response_id"), str)
        and bool(metadata["response_id"])
        and metadata.get("model") in {
            model_id, FROZEN_CANONICAL_MODEL_IDS[model_id]
        }
        and metadata.get("finish_reason") == "stop"
        and metadata.get("requested_seed") == seed
        and type(metadata.get("requested_seed")) is int
        and type(metadata.get("attempt_count")) is int
        and 1 <= metadata["attempt_count"] <= 3
    )


def _request_id(base: str, model_id: str, seed: int, attempt_index: int) -> str:
    safe_model = model_id.replace("/", "_")
    return "%s--model-%s--seed-%d--attempt-%d" % (
        base,
        safe_model,
        seed,
        attempt_index,
    )


def _schedule(
    config: Mapping[str, Any], forced: Sequence[Mapping[str, Any]], smoke: bool
) -> List[Tuple[Mapping[str, Any], Mapping[str, str]]]:
    records = list(forced[:1] if smoke else forced)
    return [
        (record, roster)
        for roster in config["model_roster"]
        for record in records
    ]


def _registered_options(record: Mapping[str, Any]) -> List[str]:
    return [option["id"] for option in record["options"]]


def _base_attempt(
    config: Mapping[str, Any],
    preflight: Mapping[str, Any],
    record: Mapping[str, Any],
    roster: Mapping[str, str],
    attempt_index: int,
    *,
    smoke: bool,
) -> Dict[str, Any]:
    base_request = build_requests_for_record(record)[0]
    return {
        "schema_version": 1,
        "study_id": STUDY_ID,
        "run_id": config["run_id"],
        "status": SMOKE_STATUS if smoke else FULL_STATUS,
        "data_basis": DATA_BASIS,
        "eligible_for_empirical_decision": False,
        "model_id": roster["model_id"],
        "model_family": roster["family"],
        "vendor": roster["vendor"],
        "seed": config["seed"],
        "item_id": record["id"],
        "core_id": record["core_id"],
        "rho": record["rho"],
        "domain": record["domain"],
        "record_type": "forced_anchor",
        "attempt_index": attempt_index,
        "request_id": _request_id(
            base_request["request_id"], roster["model_id"], config["seed"], attempt_index
        ),
        "config_sha256": preflight["config_sha256"],
        "bank_sha256": preflight["bank_sha256"],
        "gold_sha256": preflight["gold_sha256"],
    }


def _finalize_attempt_hash(row: Dict[str, Any], previous_hash: str) -> Dict[str, Any]:
    row["previous_attempt_sha256"] = previous_hash
    row["attempt_sha256"] = _object_hash(row)
    return row


def _classify_attempt(
    raw: Optional[str], registered: Sequence[str], *, error: Optional[OpenRouterError]
) -> Tuple[str, Optional[str], Optional[str], Optional[str]]:
    if error is not None:
        return (
            "adapter_error",
            None,
            type(error).__name__,
            "OpenRouter adapter failure",
        )
    if not isinstance(raw, str):
        return "adapter_error", None, "AdapterContractError", "Adapter returned non-text"
    selected = parse_option_letter(raw, registered)
    if selected is not None:
        return "valid_choice", selected, None, None
    if not raw.strip():
        return "blank_response", None, None, None
    return "invalid_choice", None, None, None


def _attempt_request(record: Mapping[str, Any], roster: Mapping[str, str], seed: int, attempt: int) -> Dict[str, Any]:
    request = deepcopy(build_requests_for_record(record)[0])
    request["request_id"] = _request_id(
        request["request_id"], roster["model_id"], seed, attempt
    )
    if attempt == 2:
        letters = ", ".join(_registered_options(record))
        request["messages"] = list(request["messages"]) + [
            {
                "role": "user",
                "content": REPAIR_INSTRUCTION.format(letters=letters),
            }
        ]
    return request


def _call_once(
    client: Any,
    config: Mapping[str, Any],
    preflight: Mapping[str, Any],
    record: Mapping[str, Any],
    roster: Mapping[str, str],
    attempt_index: int,
    previous_hash: str,
    seen_response_ids: set,
    *,
    smoke: bool,
) -> Dict[str, Any]:
    request = _attempt_request(record, roster, config["seed"], attempt_index)
    raw = None
    caught = None
    try:
        raw = client.generate(deepcopy(request), seed=config["seed"])
    except OpenRouterError as error:
        caught = error
    metadata = (
        _safe_call_metadata(client, model_id=roster["model_id"], seed=config["seed"])
        if caught is None
        else {}
    )
    if caught is None and not _metadata_attributed(
        metadata, model_id=roster["model_id"], seed=config["seed"]
    ):
        status = "adapter_error"
        selected = None
        error_type = "AdapterMetadataError"
        error_message = "Adapter response metadata failed attribution"
        stored_raw = None
        metadata = {}
    elif caught is None and metadata["response_id"] in seen_response_ids:
        status = "adapter_error"
        selected = None
        error_type = "AdapterMetadataError"
        error_message = "Adapter response metadata failed attribution"
        stored_raw = None
        metadata = {}
    else:
        status, selected, error_type, error_message = _classify_attempt(
            raw, _registered_options(record), error=caught
        )
        stored_raw = raw if isinstance(raw, str) else None
        if status == "adapter_error":
            metadata = {}
        elif metadata:
            seen_response_ids.add(metadata["response_id"])
    row = _base_attempt(
        config, preflight, record, roster, attempt_index, smoke=smoke
    )
    row.update(
        {
            "response_status": status,
            "raw_response": stored_raw,
            "selected_option_id": selected,
            "call_metadata": metadata,
            "error_type": error_type,
            "error_message": error_message,
        }
    )
    return _finalize_attempt_hash(row, previous_hash)


def _validate_prior_row(
    row: Any,
    config: Mapping[str, Any],
    preflight: Mapping[str, Any],
    record: Mapping[str, Any],
    roster: Mapping[str, str],
    attempt_index: int,
    previous_hash: str,
    *,
    smoke: bool,
) -> Dict[str, Any]:
    if not isinstance(row, Mapping) or set(row) != _IDENTITY_FIELDS:
        raise DiagnosticResumeError("attempt row fields do not match frozen audit schema")
    expected = _base_attempt(
        config, preflight, record, roster, attempt_index, smoke=smoke
    )
    for field, value in expected.items():
        if row.get(field) != value or type(row.get(field)) is not type(value):
            raise DiagnosticResumeError("attempt identity/provenance mismatch: %s" % field)
    if row.get("previous_attempt_sha256") != previous_hash:
        raise DiagnosticResumeError("attempt hash chain is out of order")
    without_hash = dict(row)
    supplied_hash = without_hash.pop("attempt_sha256", None)
    if not isinstance(supplied_hash, str) or _SHA256.fullmatch(supplied_hash) is None:
        raise DiagnosticResumeError("attempt SHA256 is invalid")
    if _object_hash(without_hash) != supplied_hash:
        raise DiagnosticResumeError("attempt row hash mismatch")
    raw = row.get("raw_response")
    selected = parse_option_letter(raw, _registered_options(record))
    status = row.get("response_status")
    if status == "valid_choice":
        valid = isinstance(raw, str) and selected is not None and row.get("selected_option_id") == selected
        valid = valid and row.get("error_type") is None and row.get("error_message") is None
    elif status == "blank_response":
        valid = isinstance(raw, str) and not raw.strip() and row.get("selected_option_id") is None
        valid = valid and row.get("error_type") is None and row.get("error_message") is None
    elif status == "invalid_choice":
        valid = isinstance(raw, str) and bool(raw.strip()) and selected is None
        valid = valid and row.get("selected_option_id") is None
        valid = valid and row.get("error_type") is None and row.get("error_message") is None
    elif status == "adapter_error":
        error_type = row.get("error_type")
        valid = raw is None and row.get("selected_option_id") is None
        valid = valid and error_type in (_ADAPTER_ERROR_TYPES | {"AdapterContractError"})
        valid = valid and row.get("error_message") in {
            "OpenRouter adapter failure",
            "Adapter returned non-text",
            "Adapter response metadata failed attribution",
        }
    else:
        valid = False
    if not valid:
        raise DiagnosticResumeError("attempt response fields conflict")
    metadata = row.get("call_metadata")
    if not isinstance(metadata, Mapping) or any(key not in _SUCCESS_METADATA_FIELDS for key in metadata):
        raise DiagnosticResumeError("attempt call metadata is unsafe")
    if status == "adapter_error":
        if metadata:
            raise DiagnosticResumeError("adapter error attempt must not retain call metadata")
    else:
        fake = type("Metadata", (), {"last_call_metadata": metadata})()
        if _safe_call_metadata(fake, model_id=roster["model_id"], seed=config["seed"]) != dict(metadata):
            raise DiagnosticResumeError("attempt call metadata failed safe-schema validation")
        if not _metadata_attributed(
            metadata, model_id=roster["model_id"], seed=config["seed"]
        ):
            raise DiagnosticResumeError("attempt call metadata lacks exact response attribution")
    return dict(row)


def _validate_prior_attempts(
    prior_attempts: Sequence[Mapping[str, Any]],
    schedule: Sequence[Tuple[Mapping[str, Any], Mapping[str, str]]],
    config: Mapping[str, Any],
    preflight: Mapping[str, Any],
    *,
    smoke: bool,
) -> Tuple[Dict[Tuple[str, str], List[Dict[str, Any]]], set]:
    if isinstance(prior_attempts, (str, bytes)) or not isinstance(prior_attempts, Sequence):
        raise DiagnosticResumeError("prior attempts must be an ordered sequence")
    grouped = {}
    cursor = 0
    previous_hash = ZERO_HASH
    response_ids = set()

    def register_response_id(row: Mapping[str, Any]) -> None:
        metadata = row.get("call_metadata")
        response_id = metadata.get("response_id") if isinstance(metadata, Mapping) else None
        if response_id is not None:
            if response_id in response_ids:
                raise DiagnosticResumeError("prior attempts replay a response attribution ID")
            response_ids.add(response_id)

    for record, roster in schedule:
        key = (roster["model_id"], record["id"])
        rows = []
        if cursor < len(prior_attempts):
            row = _validate_prior_row(
                prior_attempts[cursor], config, preflight, record, roster, 1,
                previous_hash, smoke=smoke,
            )
            rows.append(row)
            register_response_id(row)
            cursor += 1
            previous_hash = row["attempt_sha256"]
            if row["response_status"] != "valid_choice" and cursor < len(prior_attempts):
                row = _validate_prior_row(
                    prior_attempts[cursor], config, preflight, record, roster, 2,
                    previous_hash, smoke=smoke,
                )
                rows.append(row)
                register_response_id(row)
                cursor += 1
                previous_hash = row["attempt_sha256"]
        grouped[key] = rows
        if cursor == len(prior_attempts):
            # Remaining schedule entries have no prior rows.  Continuing the
            # loop only initializes their empty groups.
            continue
    if cursor != len(prior_attempts):
        raise DiagnosticResumeError("prior attempts contain duplicate or out-of-schedule rows")
    return grouped, response_ids


def _terminal_item(
    config: Mapping[str, Any],
    preflight: Mapping[str, Any],
    record: Mapping[str, Any],
    roster: Mapping[str, str],
    attempts: Sequence[Mapping[str, Any]],
    *,
    smoke: bool,
) -> Dict[str, Any]:
    terminal = attempts[-1]
    answered = terminal["response_status"] == "valid_choice"
    if answered:
        park_reason = None
    elif terminal["response_status"] == "adapter_error":
        park_reason = "adapter_error_after_repair"
    elif terminal["response_status"] == "blank_response":
        park_reason = "blank_response_after_repair"
    else:
        park_reason = "invalid_choice_after_repair"
    return {
        "schema_version": 1,
        "study_id": STUDY_ID,
        "run_id": config["run_id"],
        "status": SMOKE_STATUS if smoke else FULL_STATUS,
        "data_basis": DATA_BASIS,
        "eligible_for_empirical_decision": False,
        "model_id": roster["model_id"],
        "model_family": roster["family"],
        "vendor": roster["vendor"],
        "seed": config["seed"],
        "item_id": record["id"],
        "core_id": record["core_id"],
        "rho": record["rho"],
        "domain": record["domain"],
        "record_type": "forced_anchor",
        "response_status": "answered" if answered else "parked",
        "raw_response": terminal["raw_response"],
        "selected_option_id": terminal["selected_option_id"] if answered else None,
        "park_reason": park_reason,
        "attempt_count": len(attempts),
        "terminal_attempt_index": terminal["attempt_index"],
        "request_id": terminal["request_id"],
        "config_sha256": preflight["config_sha256"],
        "bank_sha256": preflight["bank_sha256"],
        "gold_sha256": preflight["gold_sha256"],
        "terminal_attempt_sha256": terminal["attempt_sha256"],
    }


def run_diagnostic(
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    *,
    clients: Sequence[Any],
    config: Mapping[str, Any],
    catalog_result: Mapping[str, Any],
    config_bytes: bytes,
    bank_bytes: bytes,
    gold_bytes: bytes,
    prior_attempts: Sequence[Mapping[str, Any]] = (),
    checkpoint: Optional[Callable[[Mapping[str, Any]], Any]] = None,
    smoke: bool = False,
) -> Dict[str, Any]:
    """Collect one terminal forced choice per model/item with exact repair."""

    if checkpoint is not None and not callable(checkpoint):
        raise DiagnosticPreflightError("checkpoint must be callable")
    preflight = preflight_diagnostic(
        config,
        bank,
        gold,
        clients=clients,
        catalog_result=catalog_result,
        config_bytes=config_bytes,
        bank_bytes=bank_bytes,
        gold_bytes=gold_bytes,
        smoke=smoke,
    )
    forced = [row for row in bank if row["record_type"] == "forced_anchor"]
    schedule = _schedule(config, forced, smoke)
    client_by_model = _validate_clients(config, clients)
    grouped_prior, seen_response_ids = _validate_prior_attempts(
        prior_attempts, schedule, config, preflight, smoke=smoke
    )
    attempts = [deepcopy(dict(row)) for row in prior_attempts]
    previous_hash = attempts[-1]["attempt_sha256"] if attempts else ZERO_HASH
    item_attempts = {}

    for record, roster in schedule:
        key = (roster["model_id"], record["id"])
        rows = list(grouped_prior[key])
        if not rows:
            new_row = _call_once(
                client_by_model[roster["model_id"]], config, preflight, record, roster,
                1, previous_hash, seen_response_ids, smoke=smoke,
            )
            attempts.append(new_row)
            rows.append(new_row)
            previous_hash = new_row["attempt_sha256"]
            if checkpoint is not None:
                checkpoint(deepcopy(new_row))
        if rows[-1]["response_status"] != "valid_choice" and len(rows) == 1:
            new_row = _call_once(
                client_by_model[roster["model_id"]], config, preflight, record, roster,
                2, previous_hash, seen_response_ids, smoke=smoke,
            )
            attempts.append(new_row)
            rows.append(new_row)
            previous_hash = new_row["attempt_sha256"]
            if checkpoint is not None:
                checkpoint(deepcopy(new_row))
        item_attempts[key] = rows

    items = [
        _terminal_item(
            config,
            preflight,
            record,
            roster,
            item_attempts[(roster["model_id"], record["id"])],
            smoke=smoke,
        )
        for record, roster in schedule
    ]
    if len(items) != preflight["scheduled_item_count"]:
        raise RuntimeError("diagnostic terminal schedule was not completed")
    return {
        "schema_version": 1,
        "study_id": STUDY_ID,
        "run_id": config["run_id"],
        "status": SMOKE_STATUS if smoke else FULL_STATUS,
        "data_basis": DATA_BASIS,
        "eligible_for_empirical_decision": False,
        "official_blockers": ["NOT_RUN_HUMAN", "SINGLE_MODEL_VENDOR"],
        "seed": config["seed"],
        "seed_count": 1,
        "record_type": "forced_anchor",
        "smoke": smoke,
        "expected_scheduled_items": preflight["scheduled_item_count"],
        "preflight": preflight,
        "attempts": attempts,
        "items": items,
        "provenance": {
            "config_sha256": preflight["config_sha256"],
            "bank_sha256": preflight["bank_sha256"],
            "gold_sha256": preflight["gold_sha256"],
            "audit_sha256": _object_hash(attempts),
            "response_sha256": _object_hash(items),
        },
    }


def _atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=str(path.parent), prefix=".%s." % path.name,
            suffix=".tmp", delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(str(temporary), str(path))
    except BaseException:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
        raise


def _append_checkpoint(path: Path) -> Callable[[Mapping[str, Any]], None]:
    def append(row: Mapping[str, Any]) -> None:
        serialized = _canonical_json_bytes(row) + b"\n"
        with path.open("ab") as handle:
            handle.write(serialized)
            handle.flush()
            os.fsync(handle.fileno())

    return append


def _default_client_factory(row: Mapping[str, Any], transport: Mapping[str, Any]) -> Any:
    return openrouter_client_from_roster(
        row,
        max_tokens=transport["max_tokens"],
        timeout=transport["timeout_seconds"],
        max_attempts=transport["max_attempts"],
        retry_base_seconds=transport["retry_base_seconds"],
        reasoning_effort=transport.get("reasoning_effort"),
    )


def _read_json_object(path: Path, label: str) -> Dict[str, Any]:
    if not path.is_file():
        raise DiagnosticPreflightError("smoke %s is missing" % label)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise DiagnosticPreflightError("smoke %s is not valid UTF-8 JSON" % label) from None
    if not isinstance(payload, dict):
        raise DiagnosticPreflightError("smoke %s root must be an object" % label)
    return payload


def _verify_smoke_authorization(
    smoke_dir: Path,
    *,
    config: Mapping[str, Any],
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    local_hashes: Mapping[str, str],
) -> Dict[str, str]:
    """Revalidate a successful smoke artifact set without external calls."""

    protocol = _protocol_for_config(config)

    from analysis.openrouter_diagnostic import (  # noqa: E402
        COLLECTION_FIELDS,
        DiagnosticCoverageError,
        analyze_diagnostic,
        render_diagnostic_markdown,
    )

    smoke_dir = Path(smoke_dir)
    if not smoke_dir.is_dir():
        raise DiagnosticPreflightError("--smoke-dir must be an existing directory")
    result_path = smoke_dir / "result.json"
    manifest_path = smoke_dir / "manifest.json"
    attempts_path = smoke_dir / "attempts.jsonl"
    report_path = smoke_dir / "report.md"
    result = _read_json_object(result_path, "result")
    manifest = _read_json_object(manifest_path, "manifest")
    result_provenance = result.get("provenance")
    manifest_provenance = manifest.get("provenance")
    if (
        result.get("run_id") != protocol.run_id
        or manifest.get("run_id") != protocol.run_id
        or not isinstance(result_provenance, Mapping)
        or not isinstance(manifest_provenance, Mapping)
        or result_provenance.get("config_sha256") != protocol.config_sha256
        or manifest_provenance.get("config_sha256") != protocol.config_sha256
        or local_hashes.get("config_sha256") != protocol.config_sha256
    ):
        raise DiagnosticPreflightError(
            "smoke proof protocol does not match the requested config"
        )
    expected_manifest_fields = {
        "schema_version", "study_id", "run_id", "status",
        "eligible_for_empirical_decision", "smoke_validation_passed",
        "artifacts", "provenance",
    }
    if protocol.revision == "R2":
        expected_manifest_fields.update(
            {"protocol_revision", "effective_reasoning_effort"}
        )
    if set(manifest) != expected_manifest_fields:
        raise DiagnosticPreflightError("smoke manifest fields do not match exact schema")
    exact_manifest = {
        "schema_version": 1,
        "study_id": STUDY_ID,
        "run_id": config["run_id"],
        "status": SMOKE_STATUS,
        "eligible_for_empirical_decision": False,
        "smoke_validation_passed": True,
    }
    if protocol.revision == "R2":
        exact_manifest.update(
            {
                "protocol_revision": protocol.revision,
                "effective_reasoning_effort": protocol.effective_reasoning_effort,
            }
        )
    if any(
        manifest.get(field) != expected
        or type(manifest.get(field)) is not type(expected)
        for field, expected in exact_manifest.items()
    ):
        raise DiagnosticPreflightError("smoke manifest does not record a successful smoke")
    artifacts = manifest.get("artifacts")
    expected_artifact_paths = {
        "attempts": "attempts.jsonl",
        "report": "report.md",
        "result": "result.json",
    }
    if not isinstance(artifacts, Mapping) or set(artifacts) != set(expected_artifact_paths):
        raise DiagnosticPreflightError("smoke manifest artifact set is invalid")
    artifact_files = {
        "attempts": attempts_path,
        "report": report_path,
        "result": result_path,
    }
    for name, expected_name in expected_artifact_paths.items():
        descriptor = artifacts.get(name)
        if (
            not isinstance(descriptor, Mapping)
            or set(descriptor) != {"path", "sha256"}
            or descriptor.get("path") != expected_name
            or type(descriptor.get("path")) is not str
            or not isinstance(descriptor.get("sha256"), str)
            or _SHA256.fullmatch(descriptor["sha256"]) is None
            or not artifact_files[name].is_file()
            or _sha256(artifact_files[name].read_bytes()) != descriptor["sha256"]
        ):
            raise DiagnosticPreflightError("smoke %s artifact hash/path mismatch" % name)
    if result_path.read_bytes() != _canonical_json_bytes(result) + b"\n":
        raise DiagnosticPreflightError("smoke result is not canonical JSON")
    if manifest_path.read_bytes() != _canonical_json_bytes(manifest) + b"\n":
        raise DiagnosticPreflightError("smoke manifest is not canonical JSON")
    if not set(COLLECTION_FIELDS).issubset(result):
        raise DiagnosticPreflightError("smoke result does not embed the complete collection")
    embedded_collection = {
        field: deepcopy(result[field]) for field in COLLECTION_FIELDS
    }
    try:
        recomputed = analyze_diagnostic(
            embedded_collection, bank, gold, config=config
        )
    except DiagnosticCoverageError as error:
        raise DiagnosticPreflightError("smoke embedded collection failed reanalysis") from error
    if recomputed != result:
        raise DiagnosticPreflightError("smoke result disagrees with deterministic reanalysis")
    if recomputed.get("smoke_validation_passed") is not True:
        raise DiagnosticPreflightError("smoke terminal choices did not all validate")
    if manifest.get("provenance") != recomputed.get("provenance"):
        raise DiagnosticPreflightError("smoke manifest/result provenance mismatch")
    for field in ("config_sha256", "bank_sha256", "gold_sha256"):
        if recomputed["provenance"].get(field) != local_hashes.get(field):
            raise DiagnosticPreflightError("smoke proof uses stale %s" % field)
    attempt_rows = read_jsonl(attempts_path)
    if attempt_rows != recomputed.get("attempts"):
        raise DiagnosticPreflightError("smoke attempts artifact disagrees with result")
    expected_attempt_bytes = b"".join(
        _canonical_json_bytes(row) + b"\n" for row in attempt_rows
    )
    if attempts_path.read_bytes() != expected_attempt_bytes:
        raise DiagnosticPreflightError("smoke attempts artifact is not canonical JSONL")
    expected_report = render_diagnostic_markdown(recomputed).encode("utf-8")
    if report_path.read_bytes() != expected_report:
        raise DiagnosticPreflightError("smoke report disagrees with deterministic rendering")
    return {
        "smoke_result_sha256": artifacts["result"]["sha256"],
        "smoke_manifest_sha256": _sha256(manifest_path.read_bytes()),
    }


def cli(
    argv: Optional[Sequence[str]] = None,
    *,
    catalog_verifier: Callable[[], Mapping[str, Any]] = verify_requested_model_catalog,
    client_factory: Callable[[Mapping[str, Any], Mapping[str, Any]], Any] = _default_client_factory,
) -> int:
    """CLI entry point with injectable offline seams for contract tests."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute-paid-live", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--smoke-dir", type=Path)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--config", type=Path, default=ROOT / "configs/openrouter-gpt55-54-54mini-forced-diagnostic.json")
    parser.add_argument("--bank", type=Path, default=ROOT / "itembank/bank/p1-private.jsonl")
    parser.add_argument("--gold", type=Path, default=ROOT / "itembank/gold/p1-private.gold.jsonl")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    if not args.execute_paid_live:
        parser.error("--execute-paid-live is required before any catalog or model call")
    if not callable(catalog_verifier) or not callable(client_factory):
        parser.error("catalog verifier and client factory must be callable")
    if args.smoke and args.smoke_dir is not None:
        parser.error("--smoke and --smoke-dir are mutually exclusive")
    if not args.smoke and args.smoke_dir is None:
        parser.error("full and resumed full runs require --smoke-dir")

    config_bytes = args.config.read_bytes()
    bank_bytes = args.bank.read_bytes()
    gold_bytes = args.gold.read_bytes()
    config = json.loads(config_bytes.decode("utf-8"))
    bank = _decode_jsonl(bank_bytes, "bank")
    gold = _decode_jsonl(gold_bytes, "gold")

    # Reject local/config/output errors before the catalog network request or
    # construction of credential-bearing clients.
    protocol = _validate_config(config)
    forced, local_hashes = _validate_artifacts(
        config,
        bank,
        gold,
        config_bytes=config_bytes,
        bank_bytes=bank_bytes,
        gold_bytes=gold_bytes,
    )
    output_dir = args.output_dir
    if args.smoke_dir is not None and args.smoke_dir.resolve() == output_dir.resolve():
        parser.error("--smoke-dir and --output-dir must be distinct")
    attempts_path = output_dir / "attempts.jsonl"
    if args.resume:
        if not attempts_path.is_file() or attempts_path.stat().st_size == 0:
            parser.error("--resume requires an existing nonempty attempts.jsonl checkpoint")
    elif output_dir.exists() and any(output_dir.iterdir()):
        parser.error("fresh output directory must be absent or empty")
    prior = read_jsonl(attempts_path) if attempts_path.exists() else []
    local_schedule = _schedule(config, forced, args.smoke)
    local_preflight = {
        **local_hashes,
        "forced_anchor_count": len(forced),
        "scheduled_item_count": len(local_schedule),
        "model_count": len(config["model_roster"]),
        "vendor_count": 1,
        "seed": config["seed"],
        "catalog_verified": True,
        "catalog_model_ids": [row["model_id"] for row in config["model_roster"]],
        "smoke": args.smoke,
    }
    _validate_prior_attempts(
        prior,
        local_schedule,
        config,
        local_preflight,
        smoke=args.smoke,
    )
    smoke_authorization = None
    if not args.smoke:
        smoke_authorization = _verify_smoke_authorization(
            args.smoke_dir,
            config=config,
            bank=bank,
            gold=gold,
            local_hashes=local_hashes,
        )

    catalog_result = catalog_verifier()
    clients = [client_factory(dict(row), dict(config["transport"])) for row in config["model_roster"]]
    preflight_diagnostic(
        config,
        bank,
        gold,
        clients=clients,
        catalog_result=catalog_result,
        config_bytes=config_bytes,
        bank_bytes=bank_bytes,
        gold_bytes=gold_bytes,
        smoke=args.smoke,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    collection = run_diagnostic(
        bank,
        gold,
        clients=clients,
        config=config,
        catalog_result=catalog_result,
        config_bytes=config_bytes,
        bank_bytes=bank_bytes,
        gold_bytes=gold_bytes,
        prior_attempts=prior,
        checkpoint=_append_checkpoint(attempts_path),
        smoke=args.smoke,
    )

    from analysis.openrouter_diagnostic import (  # noqa: E402
        analyze_diagnostic,
        render_diagnostic_markdown,
    )

    result = analyze_diagnostic(collection, bank, gold, config=config)
    if smoke_authorization is not None:
        result["provenance"].update(smoke_authorization)
    report = render_diagnostic_markdown(result)
    result_path = output_dir / "result.json"
    report_path = output_dir / "report.md"
    manifest_path = output_dir / "manifest.json"
    _atomic_write(result_path, _canonical_json_bytes(result) + b"\n")
    _atomic_write(report_path, report.encode("utf-8"))
    artifacts = {
        "attempts": {"path": attempts_path.name, "sha256": _sha256(attempts_path.read_bytes())},
        "report": {"path": report_path.name, "sha256": _sha256(report_path.read_bytes())},
        "result": {"path": result_path.name, "sha256": _sha256(result_path.read_bytes())},
    }
    manifest = {
        "schema_version": 1,
        "study_id": STUDY_ID,
        "run_id": config["run_id"],
        "status": result["status"],
        "eligible_for_empirical_decision": False,
        "smoke_validation_passed": result["smoke_validation_passed"],
        "artifacts": artifacts,
        "provenance": result["provenance"],
    }
    if protocol.revision == "R2":
        manifest.update(
            {
                "protocol_revision": protocol.revision,
                "effective_reasoning_effort": protocol.effective_reasoning_effort,
            }
        )
    _atomic_write(manifest_path, _canonical_json_bytes(manifest) + b"\n")
    print("status: %s" % result["status"])
    print("terminal items: %d" % len(result["items"]))
    if args.smoke:
        print("smoke_validation_passed: %s" % str(result["smoke_validation_passed"]).lower())
    print("eligible_for_empirical_decision: false")
    if args.smoke and result["smoke_validation_passed"] is not True:
        return 2
    return 0


def main() -> None:
    raise SystemExit(cli())


if __name__ == "__main__":
    main()


__all__ = [
    "DiagnosticPreflightError",
    "DiagnosticResumeError",
    "cli",
    "parse_option_letter",
    "preflight_diagnostic",
    "run_diagnostic",
]
