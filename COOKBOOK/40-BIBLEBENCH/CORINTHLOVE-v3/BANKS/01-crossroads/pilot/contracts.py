"""Frozen identities, canonical hashing, and fail-closed API attestations."""
from __future__ import annotations

from copy import deepcopy
from decimal import Decimal, InvalidOperation
import hashlib
import json
import math
from pathlib import Path
import re


PILOT_ROOT = Path(__file__).resolve().parent
PROFILE_PATH = PILOT_ROOT / "cheap_profile.json"
CATALOG_EVIDENCE_VERSION = "openrouter-model-zdr-intersection-v1"
COMPLETION_EVIDENCE_VERSION = "openrouter-chat-router-metadata-v1"
MODEL_CATALOG_BASE_URL = "https://openrouter.ai/api/v1/models"
ZDR_CATALOG_URL = "https://openrouter.ai/api/v1/endpoints/zdr"
CATALOG_STATUS_POLICY = "exact-integer-zero"
FROZEN_PROFILE = {
    "profile_id": "crossroads-cheap-azure-v6",
    "purpose": "public qualification",
    "immutable": True,
    "catalog_snapshot_utc": "2026-07-12T02:13:01Z",
    "minimum_context_length": 400000,
    "reasoning_effort": "medium",
    "catalog_policy": {
        "evidence_version": CATALOG_EVIDENCE_VERSION,
        "admissible_status_code": 0,
        "minimum_eligible_endpoints": 1,
        "zdr_catalog_url": ZDR_CATALOG_URL,
    },
    "completion_policy": {
        "evidence_version": COMPLETION_EVIDENCE_VERSION,
        "require_generation_header": True,
        "require_response_provider": True,
        "require_router_metadata": True,
    },
    "routing": {
        "only": ["azure"],
        "order": ["azure"],
        "allow_fallbacks": False,
        "require_parameters": True,
        "data_collection": "deny",
        "zdr": True,
    },
    "models": {
        "openai/gpt-5-nano": {
            "expected_snapshot": "openai/gpt-5-nano-2025-08-07",
            "price_ceiling_per_token": {
                "input": 0.00000005, "output": 0.0000004,
            },
        },
        "openai/gpt-5.4-nano": {
            "expected_snapshot": "openai/gpt-5.4-nano-20260317",
            "price_ceiling_per_token": {
                "input": 0.0000002, "output": 0.00000125,
            },
        },
        "openai/gpt-5-mini": {
            "expected_snapshot": "openai/gpt-5-mini-2025-08-07",
            "price_ceiling_per_token": {
                "input": 0.00000025, "output": 0.000002,
            },
        },
        "openai/gpt-5.4-mini": {
            "expected_snapshot": "openai/gpt-5.4-mini-20260317",
            "price_ceiling_per_token": {
                "input": 0.00000075, "output": 0.0000045,
            },
        },
    },
}
REQUIRED_PARAMETERS = (
    "max_completion_tokens", "reasoning", "response_format",
    "structured_outputs", "tools", "tool_choice",
)
PROVENANCE_MOCK = "harness validation, NOT a measurement"
PROVENANCE_LIVE = "public qualification"
_CREDENTIAL_KEYS = {
    "authorization", "proxy_authorization", "api_key", "apikey",
    "openrouter_api_key", "secret", "token", "access_token",
    "refresh_token", "cookie", "set_cookie",
}
_CREDENTIAL_VALUE = re.compile(
    r"(?:sk-or-v1-[A-Za-z0-9_-]{8,}|OPENROUTER_API_KEY\s*=|Bearer\s+[A-Za-z0-9._~-]{6,})",
    re.IGNORECASE,
)
_HEX64 = re.compile(r"^[0-9a-f]{64}$")


def canonical_bytes(value) -> bytes:
    """Encode a JSON value deterministically and reject non-finite values."""
    try:
        return (json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
            allow_nan=False,
        ) + "\n").encode("utf-8")
    except (TypeError, ValueError):
        raise ValueError("value is not canonical JSON") from None


_FROZEN_PROFILE_CANONICAL = canonical_bytes(FROZEN_PROFILE)


def sha256_value(value) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def assert_sha256(value: object, label: str = "sha256") -> str:
    if not isinstance(value, str) or _HEX64.fullmatch(value) is None:
        raise ValueError(f"{label} must be a lowercase SHA-256")
    return value


def _normalized_key(key: str) -> str:
    return key.strip().lower().replace("-", "_").replace(" ", "_")


def assert_artifact_safe(value, path: str = "artifact") -> None:
    """Reject credentials recursively before an evidence byte is persisted."""
    if isinstance(value, dict):
        for key, child in value.items():
            if not isinstance(key, str):
                raise ValueError(f"credential safety requires string keys at {path}")
            normalized = _normalized_key(key)
            if normalized in _CREDENTIAL_KEYS or normalized.endswith("_api_key"):
                raise ValueError(f"credential field forbidden at {path}.{key}")
            assert_artifact_safe(child, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            assert_artifact_safe(child, f"{path}[{index}]")
    elif isinstance(value, str) and _CREDENTIAL_VALUE.search(value):
        raise ValueError(f"credential material forbidden at {path}")


def _strict_json_object(path: Path) -> dict:
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}")
            result[key] = value
        return result

    try:
        value = json.loads(
            Path(path).read_text(encoding="utf-8"),
            object_pairs_hook=unique_pairs,
            parse_constant=lambda _value: (_ for _ in ()).throw(ValueError()),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        raise ValueError("cheap profile must be strict JSON") from None
    if not isinstance(value, dict):
        raise ValueError("cheap profile must be strict JSON object")
    return value


def _validate_profile(profile: dict) -> dict:
    if not isinstance(profile, dict):
        raise ValueError("frozen cheap profile must be an object")
    try:
        observed = canonical_bytes(profile)
    except ValueError:
        raise ValueError("frozen cheap profile differs") from None
    if observed != _FROZEN_PROFILE_CANONICAL:
        raise ValueError("frozen cheap profile differs")
    assert_artifact_safe(profile)
    return deepcopy(profile)


def load_profile(path: Path = PROFILE_PATH) -> dict:
    return _validate_profile(_strict_json_object(path))


def resolve_model(alias: str, profile: dict | None = None) -> dict:
    profile = load_profile() if profile is None else _validate_profile(profile)
    models = profile.get("models", {})
    if alias not in models:
        raise ValueError(f"model {alias!r} is not in the frozen cheap allowlist")
    row = deepcopy(models[alias])
    row["alias"] = alias
    row["profile_id"] = profile["profile_id"]
    row["profile_sha256"] = sha256_value(profile)
    row["routing"] = deepcopy(profile["routing"])
    row["catalog_policy"] = deepcopy(profile["catalog_policy"])
    row["completion_policy"] = deepcopy(profile["completion_policy"])
    row["minimum_context_length"] = profile["minimum_context_length"]
    row["reasoning_effort"] = profile["reasoning_effort"]
    return row


def _decimal(value, label: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{label} must be a nonnegative finite price")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{label} must be a nonnegative finite price") from None
    if not result.is_finite() or result < 0:
        raise ValueError(f"{label} must be a nonnegative finite price")
    return result


def _endpoint_identity(endpoint: dict, *, label: str) -> tuple[str, str, str, str]:
    if not isinstance(endpoint, dict):
        raise ValueError(f"{label} endpoint must be an object")
    values = tuple(
        endpoint.get(field) for field in (
            "model_id", "provider_name", "tag", "name"
        )
    )
    if any(not isinstance(value, str) or not value for value in values):
        raise ValueError(f"{label} endpoint identity is incomplete")
    return values


def _endpoint_parameters(endpoint: dict, *, label: str) -> tuple[str, ...]:
    value = endpoint.get("supported_parameters")
    if not isinstance(value, list) or any(
            not isinstance(row, str) or not row for row in value):
        raise ValueError(f"{label} supported parameters are invalid")
    if len(value) != len(set(value)):
        raise ValueError(f"{label} supported parameters contain duplicates")
    return tuple(sorted(value))


def _endpoint_prices(endpoint: dict, *, label: str) -> dict:
    pricing = endpoint.get("pricing")
    if not isinstance(pricing, dict):
        raise ValueError(f"{label} pricing is absent")
    return {
        "input": _decimal(pricing.get("prompt"), f"{label} input price"),
        "output": _decimal(
            pricing.get("completion"), f"{label} output price"
        ),
    }


def _is_base_azure_endpoint(identity: tuple[str, str, str, str], alias: str) -> bool:
    model_id, provider_name, tag, _name = identity
    return (
        model_id == alias
        and provider_name == "Azure"
        and (tag == "azure" or tag.startswith("azure/"))
    )


def validate_catalog(catalog: dict, model: dict) -> dict:
    """Attest exact Azure endpoints by current model/ZDR catalog intersection."""
    required_fields = {
        "catalog_evidence_version", "model_id", "model_catalog_url",
        "zdr_catalog_url", "model_catalog_response", "zdr_catalog_response",
    }
    if not isinstance(catalog, dict) or set(catalog) != required_fields:
        raise ValueError("catalog evidence fields differ from frozen contract")
    if catalog.get("catalog_evidence_version") != CATALOG_EVIDENCE_VERSION:
        raise ValueError("catalog evidence version differs from frozen contract")
    alias = model.get("alias")
    expected_model_url = f"{MODEL_CATALOG_BASE_URL}/{alias}/endpoints"
    if catalog.get("model_id") != alias or catalog.get(
            "model_catalog_url") != expected_model_url:
        raise ValueError("catalog model identity differs from frozen alias")
    if catalog.get("zdr_catalog_url") != ZDR_CATALOG_URL:
        raise ValueError("catalog ZDR source differs from frozen contract")
    policy = model.get("catalog_policy")
    if policy != {
        "evidence_version": CATALOG_EVIDENCE_VERSION,
        "admissible_status_code": 0,
        "minimum_eligible_endpoints": 1,
        "zdr_catalog_url": ZDR_CATALOG_URL,
    }:
        raise ValueError("model catalog policy differs from frozen contract")
    if model.get("routing") != {
        "only": ["azure"], "order": ["azure"],
        "allow_fallbacks": False, "require_parameters": True,
        "data_collection": "deny", "zdr": True,
    }:
        raise ValueError("model routing differs from frozen Azure/ZDR contract")

    model_response = catalog.get("model_catalog_response")
    model_data = model_response.get("data") if isinstance(
        model_response, dict
    ) else None
    if not isinstance(model_data, dict) or model_data.get("id") != alias:
        raise ValueError("model endpoint catalog identity differs")
    # The current endpoint API does not expose a model-level context field.
    # When supplied it must be sound, but every routable endpoint remains the
    # authoritative unit and is checked independently below.
    if "context_length" in model_data and (
        type(model_data["context_length"]) is not int
        or model_data["context_length"] < model["minimum_context_length"]
    ):
        raise ValueError("catalog context capability below minimum")
    model_endpoints = model_data.get("endpoints")
    if not isinstance(model_endpoints, list):
        raise ValueError("model endpoint catalog rows are absent")

    zdr_response = catalog.get("zdr_catalog_response")
    zdr_endpoints = zdr_response.get("data") if isinstance(
        zdr_response, dict
    ) else None
    if not isinstance(zdr_endpoints, list):
        raise ValueError("ZDR endpoint catalog rows are absent")

    model_by_identity = {}
    for index, endpoint in enumerate(model_endpoints):
        identity = _endpoint_identity(endpoint, label="model catalog")
        if not _is_base_azure_endpoint(identity, alias):
            continue
        if identity in model_by_identity:
            raise ValueError("model catalog contains duplicate Azure identity")
        model_by_identity[identity] = (index, endpoint)

    zdr_by_identity = {}
    for index, endpoint in enumerate(zdr_endpoints):
        identity = _endpoint_identity(endpoint, label="ZDR catalog")
        if not _is_base_azure_endpoint(identity, alias):
            continue
        if identity in zdr_by_identity:
            raise ValueError("ZDR catalog contains duplicate Azure identity")
        zdr_by_identity[identity] = (index, endpoint)

    eligible = []
    for identity in sorted(set(model_by_identity) & set(zdr_by_identity)):
        model_index, model_endpoint = model_by_identity[identity]
        zdr_index, zdr_endpoint = zdr_by_identity[identity]
        for label, endpoint in (
            ("model catalog", model_endpoint), ("ZDR catalog", zdr_endpoint),
        ):
            if type(endpoint.get("status")) is not int or endpoint["status"] != 0:
                raise ValueError(
                    f"{label} endpoint violates exact-integer-zero status policy"
                )
        if identity[3] != f"Azure | {model['expected_snapshot']}":
            raise ValueError("Azure/ZDR endpoint snapshot differs from frozen model")
        model_context = model_endpoint.get("context_length")
        zdr_context = zdr_endpoint.get("context_length")
        if type(model_context) is not int or type(zdr_context) is not int:
            raise ValueError("Azure/ZDR endpoint context is invalid")
        if model_context != zdr_context:
            raise ValueError("model and ZDR catalogs disagree on endpoint context")
        if model_context < model["minimum_context_length"]:
            raise ValueError("Azure/ZDR endpoint context capability below minimum")
        model_parameters = _endpoint_parameters(
            model_endpoint, label="model catalog"
        )
        zdr_parameters = _endpoint_parameters(zdr_endpoint, label="ZDR catalog")
        if model_parameters != zdr_parameters:
            raise ValueError(
                "model and ZDR catalogs disagree on supported parameters"
            )
        if not set(REQUIRED_PARAMETERS) <= set(model_parameters):
            raise ValueError("Azure/ZDR endpoint missing required parameters")
        model_prices = _endpoint_prices(model_endpoint, label="model catalog")
        zdr_prices = _endpoint_prices(zdr_endpoint, label="ZDR catalog")
        if model_prices != zdr_prices:
            raise ValueError("model and ZDR catalogs disagree on endpoint pricing")
        for kind in ("input", "output"):
            ceiling = _decimal(
                model["price_ceiling_per_token"][kind], f"{kind} ceiling"
            )
            if model_prices[kind] > ceiling:
                raise ValueError(f"{kind} price ceiling exceeded")
        eligible.append({
            "model_catalog_index": model_index,
            "zdr_catalog_index": zdr_index,
            "model_id": identity[0], "provider_display_name": identity[1],
            "tag": identity[2], "snapshot_name": identity[3],
            "catalog_status_code": 0,
            "context_length": model_context,
            "supported_parameters": list(model_parameters),
            "pricing_per_token": {
                kind: str(model_prices[kind]) for kind in ("input", "output")
            },
        })
    if len(eligible) < policy["minimum_eligible_endpoints"]:
        raise ValueError("catalog has no eligible exact Azure/ZDR endpoint")
    equivalence_facts = {
        (
            row["model_id"], row["provider_display_name"],
            row["snapshot_name"], row["catalog_status_code"],
            row["context_length"], tuple(row["supported_parameters"]),
            row["pricing_per_token"]["input"],
            row["pricing_per_token"]["output"],
        )
        for row in eligible
    }
    if len(equivalence_facts) != 1:
        raise ValueError("eligible Azure/ZDR routes are not equivalent")
    attestation = {
        "attestation_version": CATALOG_EVIDENCE_VERSION,
        "model_alias": alias,
        "expected_snapshot": model["expected_snapshot"],
        "eligible_endpoint_count": len(eligible),
        "endpoint_tags": sorted(row["tag"] for row in eligible),
        "provider_display_name": "Azure",
        "provider_routing_slug": "azure",
        "catalog_status_policy": CATALOG_STATUS_POLICY,
        "request_zdr_required": True,
        "zdr_attestation": {
            "observed": True,
            "method": "exact-endpoint-membership",
            "source": ZDR_CATALOG_URL,
        },
        "eligible_endpoints": sorted(eligible, key=lambda row: row["tag"]),
    }
    assert_artifact_safe(catalog)
    assert_artifact_safe(attestation)
    return attestation


def require_nonnegative_number(value, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a nonnegative finite number")
    result = float(value)
    if not math.isfinite(result) or result < 0:
        raise ValueError(f"{label} must be a nonnegative finite number")
    return result
