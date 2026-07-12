"""Pinned, provider-audited OpenRouter execution for CHARITROC.

The adapter has no bank-side metadata surface.  It consumes validated
``StageRequest`` objects, preserves exact SSE bytes, and emits only validated
``StageResult``/``StageChain`` records.  The default run mode is deliberately
``mock`` so fixture tests can never be mislabeled as measurements.
"""
from __future__ import annotations

import base64
from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
import hashlib
import json
import re
import time
import urllib.error
import urllib.request
import uuid

from lib.payloads import model_turns
from pilot import contracts, manifest


API_URL = "https://openrouter.ai/api/v1/chat/completions"
REQUEST_TIMEOUT_SECONDS = 300
MAX_COMPLETION_TOKENS = 4096
MAX_TRANSPORT_ATTEMPTS = 3
MAX_RETRY_DELAY_SECONDS = 120
MAX_TRACE_BYTES = 16 * 1024 * 1024
SANITIZED_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "text/event-stream",
    "X-OpenRouter-Metadata": "enabled",
}
STREAMING_ENABLED = True
REASONING_POLICY = {"effort": "medium"}
RESPONSE_FORMAT_POLICY = {
    "type": "json_schema",
    "name": "charitroc_stage_response",
    "strict": True,
}
ROUTING_POLICY = {
    "only": ["OpenAI"],
    "order": ["OpenAI"],
    "allow_fallbacks": False,
    "require_parameters": True,
    "data_collection": "deny",
    "zdr": True,
}
NULL_USAGE = {
    "input_tokens": None,
    "cached_input_tokens": None,
    "output_tokens": None,
    "reasoning_tokens": None,
    "total_tokens": None,
}
FAILURE_RECORD_VERSION = "charitroc-openrouter-failure-v1"
LIVE_ATTEMPT_PROVENANCE = (
    "live OpenRouter calibration attempt, NOT a measurement"
)
LIVE_QUALIFICATION_ATTEMPT_PROVENANCE = (
    "live OpenRouter qualification attempt, NOT a measurement"
)
LIVE_ACCESS_PROBE_ATTEMPT_PROVENANCE = (
    "live OpenRouter access probe attempt, NOT a measurement"
)
_LIVE_CHEAP_QUALIFICATION_AUTHORIZATION = object()
_LIVE_ACCESS_PROBE_AUTHORIZATION = object()
_SECRET_VALUE_RE = re.compile(
    r"(?i)(?:\b(?:sk|rk)-[A-Za-z0-9_-]{8,}|"
    r"\bBearer\s+[A-Za-z0-9._~+/=-]+|"
    r"\bOPENROUTER_API_KEY\s*=)"
)
_CREDENTIAL_KEYS = {
    "api_key", "apikey", "authorization", "auth_token", "access_token",
    "refresh_token", "bearer_token", "token", "password", "passwd",
    "secret", "credential", "credentials", "private_key", "cookie",
    "session_cookie", "signed_url", "openrouter_api_key",
}
_CREDENTIAL_KEY_FRAGMENTS = (
    "api_key", "apikey", "authorization", "auth_token", "access_token",
    "refresh_token", "bearer", "password", "passwd", "secret",
    "credential", "private_key", "cookie", "signed_url",
)
_CAPABILITY_KEYS = {
    "tool", "tools", "tool_call", "tool_calls", "function", "functions",
    "function_call", "plugin", "plugins", "web", "web_search", "search",
    "healing", "response_healing", "compression", "context_compression",
}
_CAPABILITY_KEY_FRAGMENTS = (
    "tool", "function", "plugin", "web", "search", "healing",
    "compression",
)
_CAPABILITY_MARKER_KEYS = {"type", "kind"}
_CAPABILITY_MARKER_VALUES = {
    "tool", "tools", "tool_call", "tool_calls", "function",
    "function_call", "functions", "plugin", "plugins", "web",
    "web_search", "search", "healing", "response_healing",
    "compression", "context_compression",
}
_FAILURE_MARKER_KEYS = {"status", "state", "type", "kind", "code"}
_FAILURE_NUMERIC_KEYS = {
    "status", "status_code", "http_status", "http_code", "code",
    "error_code",
}
_FAILURE_MARKER_VALUES = {
    "failed", "error", "incomplete", "canceled", "cancelled",
    "rejected", "aborted", "failure", "timed_out", "timed out",
    "timeout", "expired",
}
_UNICODE_ESCAPE_RE = re.compile(r"\\u([0-9a-fA-F]{4})")
_ITEM_ID_RE = re.compile(r"CHARITROC-[0-9]{4}", re.IGNORECASE)
_JUDGE_ID_RE = re.compile(
    r"JUDGE-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}",
    re.IGNORECASE,
)


def _runtime_wire_configuration():
    return {
        "api_url": API_URL,
        "request_timeout_seconds": REQUEST_TIMEOUT_SECONDS,
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "max_transport_attempts": MAX_TRANSPORT_ATTEMPTS,
        "max_retry_delay_seconds": MAX_RETRY_DELAY_SECONDS,
        "max_trace_bytes": MAX_TRACE_BYTES,
        "sanitized_headers": deepcopy(SANITIZED_HEADERS),
        "streaming_enabled": STREAMING_ENABLED,
        "reasoning_policy": deepcopy(REASONING_POLICY),
        "response_format_policy": deepcopy(RESPONSE_FORMAT_POLICY),
        "routing_policy": deepcopy(ROUTING_POLICY),
    }


FROZEN_RUNTIME_WIRE_CONFIGURATION_SHA256 = (
    "f76cd7e9a01f907ccac3bd88d37b0a865ab5698c0bb9859fb18290045077e071"
)


def _assert_frozen_runtime_wire_configuration():
    if contracts.canonical_sha256(_runtime_wire_configuration()) != (
            FROZEN_RUNTIME_WIRE_CONFIGURATION_SHA256):
        raise ValueError(
            "OpenRouter frozen runtime wire configuration has changed"
        )


class OpenRouterProtocolError(ValueError):
    """The preserved provider stream cannot satisfy the frozen wire contract."""

    def __init__(self, message, *, failure_record=None):
        super().__init__(message)
        self.failure_record = deepcopy(failure_record)


class OpenRouterTransportError(RuntimeError):
    """The HTTP transport failed before a response envelope was available."""


def _validate_stage_hooks(before_stage, stage_sink):
    for name, callback in (
            ("before_stage", before_stage), ("stage_sink", stage_sink)):
        if callback is not None and not callable(callback):
            raise ValueError(f"{name} must be callable or None")


def _emit_stage_hook(
        callback, *, integrity_session, request, transport_descriptor,
        result=None, include_result=False):
    if callback is None:
        return
    event = {
        "provider": "openrouter",
        "integrity_session": integrity_session,
        "execution_id": request["execution_id"],
        "stage": request["stage"],
        "request": deepcopy(request),
        "transport_descriptor": deepcopy(transport_descriptor),
        "attestation": None,
    }
    if include_result:
        event["result"] = deepcopy(result)
    callback(event)


@dataclass(frozen=True)
class WireRequest:
    url: str
    headers: dict = field(repr=False)
    body: bytes = field(repr=False)
    sanitized_descriptor: dict
    transport_request_sha256: str


@dataclass
class TransportResponse:
    status: int
    headers: dict = field(repr=False)
    chunks: object = field(repr=False)
    closer: object = field(default=None, repr=False)

    def close(self):
        if self.closer is not None:
            self.closer()


class SequenceClock:
    """Deterministic whole-second UTC clock for fixtures."""

    def __init__(self, start=None):
        self._next = start or datetime(
            2026, 7, 10, 12, 0, 0, tzinfo=timezone.utc
        )

    def __call__(self):
        current = self._next
        self._next = current + timedelta(seconds=1)
        return current.strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _unique_json(payload):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result

    try:
        value = json.loads(
            payload,
            object_pairs_hook=unique_pairs,
            parse_constant=lambda _value: (_ for _ in ()).throw(
                ValueError("non-finite JSON value")
            ),
        )
    except (json.JSONDecodeError, UnicodeError, ValueError, TypeError):
        raise OpenRouterProtocolError(
            "OpenRouter stream contains invalid or duplicate-key JSON"
        ) from None
    if type(value) is not dict:
        raise OpenRouterProtocolError("OpenRouter event must be a JSON object")
    return value


def _normalized_key(value):
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def _is_credential_key(value):
    normalized = _normalized_key(value)
    return (
        normalized in _CREDENTIAL_KEYS
        or any(fragment in normalized
               for fragment in _CREDENTIAL_KEY_FRAGMENTS)
    )


def _contains_credential_material(value):
    """Scan decoded provider trees without treating usage counts as secrets."""
    if type(value) is dict:
        for key, item in value.items():
            if _is_credential_key(key):
                return True
            if _contains_credential_material(item):
                return True
        return False
    if type(value) is list:
        return any(_contains_credential_material(item) for item in value)
    return type(value) is str and _SECRET_VALUE_RE.search(value) is not None


def _contains_raw_credential_material(raw):
    try:
        text = raw.decode("utf-8", errors="ignore")
    except (AttributeError, UnicodeError):
        return False
    expanded = _UNICODE_ESCAPE_RE.sub(
        lambda match: chr(int(match.group(1), 16)), text
    )
    if _SECRET_VALUE_RE.search(expanded) is not None:
        return True
    return any(
        _is_credential_key(key)
        for key in re.findall(r'"([^"\r\n]*)"\s*:', expanded)
    )


def _contains_exact_secret(value, exact_secret):
    if type(value) is bytes:
        if exact_secret.encode("utf-8") in value:
            return True
        value = value.decode("utf-8", errors="ignore")
    if type(value) is str:
        if exact_secret in value:
            return True
        expanded = _UNICODE_ESCAPE_RE.sub(
            lambda match: chr(int(match.group(1), 16)), value
        )
        return exact_secret in expanded
    if type(value) is dict:
        return any(
            _contains_exact_secret(key, exact_secret)
            or _contains_exact_secret(item, exact_secret)
            for key, item in value.items()
        )
    if type(value) in {list, tuple}:
        return any(
            _contains_exact_secret(item, exact_secret) for item in value
        )
    return False


def _failure_record(
        raw, failure_kind, *, failure_context, force_redact=False):
    raw = bytes(raw)
    redacted = force_redact or _contains_raw_credential_material(raw)
    record = {
        "failure_record_version": FAILURE_RECORD_VERSION,
        "provenance": (
            contracts.RUN_PROVENANCE["mock"]
            if failure_context["run_mode"] == "mock"
            else failure_context["attempt_provenance"]
        ),
        "run_mode": failure_context["run_mode"],
        "measurement_ready": False,
        "failure_kind": failure_kind,
        "raw_bytes_base64": (
            None if redacted else base64.b64encode(raw).decode("ascii")
        ),
        "raw_bytes_sha256": hashlib.sha256(raw).hexdigest(),
        "raw_byte_count": len(raw),
        "raw_redacted": redacted,
    }
    record.update(deepcopy(failure_context["identity"]))
    return record


def _binary_protocol_error(
        failure_kind, raw, *, failure_context, force_redact=False):
    return OpenRouterProtocolError(
        "OpenRouter stream failed before safe text evidence was available",
        failure_record=_failure_record(
            raw,
            failure_kind,
            failure_context=failure_context,
            force_redact=force_redact,
        ),
    )


def _capture_stream(
        chunks, failure_context, *, exact_secret, response_headers=None):
    """Capture every yielded byte before parsing or decoding provider data."""
    raw = bytearray()
    header_echo = _contains_exact_secret(response_headers, exact_secret)

    def capture_error(failure_kind, extra=None):
        force_redact = (
            header_echo
            or _contains_exact_secret(bytes(raw), exact_secret)
            or _contains_exact_secret(extra, exact_secret)
        )
        return _binary_protocol_error(
            failure_kind,
            raw,
            failure_context=failure_context,
            force_redact=force_redact,
        )

    try:
        for chunk in chunks:
            if type(chunk) is not bytes:
                raise capture_error("invalid_chunk", chunk)
            raw.extend(chunk)
            if len(raw) > MAX_TRACE_BYTES:
                raise capture_error("trace_limit")
    except OpenRouterProtocolError as error:
        if error.failure_record is not None:
            raise
        raise capture_error("iterator_failure") from None
    except Exception:
        raise capture_error("iterator_failure") from None
    captured = bytes(raw)
    if (
        header_echo
        or
        _contains_exact_secret(captured, exact_secret)
        or _contains_raw_credential_material(captured)
    ):
        raise _binary_protocol_error(
            "credential_material",
            captured,
            failure_context=failure_context,
            force_redact=True,
        )
    try:
        text = captured.decode("utf-8", errors="strict")
    except UnicodeError:
        raise _binary_protocol_error(
            "invalid_utf8", captured, failure_context=failure_context
        ) from None
    return captured, text


def _capability_evidence(value, path=()):
    evidence = []
    if type(value) is dict:
        for key, item in value.items():
            normalized = _normalized_key(key)
            current = path + (key,)
            if (
                normalized in _CAPABILITY_KEYS
                or any(fragment in normalized
                       for fragment in _CAPABILITY_KEY_FRAGMENTS)
            ):
                evidence.append({
                    "path": ".".join(current),
                    "value": deepcopy(item),
                })
            marker_value = (
                _normalized_key(item).replace(".", "_")
                if type(item) is str else None
            )
            if (
                normalized in _CAPABILITY_MARKER_KEYS
                and marker_value in _CAPABILITY_MARKER_VALUES
            ):
                evidence.append({
                    "path": ".".join(current),
                    "value": deepcopy(item),
                })
            evidence.extend(_capability_evidence(item, current))
    elif type(value) is list:
        for index, item in enumerate(value):
            evidence.extend(_capability_evidence(
                item, path + (str(index),)
            ))
    return evidence


def _failure_status_evidence(value, path=(), *, inside_error=False):
    evidence = []
    if type(value) is dict:
        for key, item in value.items():
            normalized = _normalized_key(key)
            current = path + (key,)
            marker = False
            # Any structured ``error`` field is provider failure evidence,
            # even when an upstream adapter leaves its value empty.  Treating
            # an empty object as success would let a malformed failure
            # envelope become a measurement.
            if normalized == "error":
                marker = True
            if (
                type(item) in {int, float}
                and item >= 400
                and (
                    normalized in _FAILURE_NUMERIC_KEYS
                    or inside_error
                    or "status" in normalized
                )
            ):
                marker = True
            if (
                type(item) is str
                and item.strip().lower() in _FAILURE_MARKER_VALUES
                and (
                    normalized in _FAILURE_MARKER_KEYS
                    or normalized == "error_code"
                    or inside_error
                )
            ):
                marker = True
            if marker:
                evidence.append(".".join(current))
            evidence.extend(_failure_status_evidence(
                item,
                current,
                inside_error=inside_error or normalized == "error",
            ))
    elif type(value) is list:
        for index, item in enumerate(value):
            evidence.extend(_failure_status_evidence(
                item,
                path + (str(index),),
                inside_error=inside_error,
            ))
    return evidence


def _forbidden_identifiers(value):
    matches = []
    if type(value) is str:
        lowered = value.lower()
        if "10cb-07-" in lowered:
            matches.append(value)
        if _ITEM_ID_RE.search(value) is not None:
            matches.append(value)
        if _JUDGE_ID_RE.search(value) is not None:
            matches.append(value)
    elif type(value) is list:
        for item in value:
            matches.extend(_forbidden_identifiers(item))
    elif type(value) is dict:
        for key, item in value.items():
            matches.extend(_forbidden_identifiers(key))
            matches.extend(_forbidden_identifiers(item))
    return matches


_REQUEST_IDENTITY_KEYS = (
    "provider", "logical_model_id", "provider_model_id", "configuration_id",
)


def _request_identity_tuple(request):
    return tuple(request[key] for key in _REQUEST_IDENTITY_KEYS)


def _validate_resolved_identity(resolved, identity):
    if type(resolved) is not dict or tuple(
            resolved.get(key) for key in _REQUEST_IDENTITY_KEYS) != identity:
        raise ValueError("resolved OpenRouter identity does not match request")
    expected_provider = manifest.expected_returned_provider(identity)
    if resolved.get("expected_returned_provider") != expected_provider:
        raise ValueError("resolved OpenRouter returned provider is inconsistent")
    expected_models = manifest.expected_returned_provider_model_ids(identity)
    if resolved.get("expected_returned_provider_model_ids") != expected_models:
        raise ValueError("resolved OpenRouter returned model IDs are inconsistent")
    if resolved.get("eligible_endpoint_policy") not in {
            "exactly_one", "all_exact_one_selected"}:
        raise ValueError("resolved OpenRouter endpoint policy is not frozen")
    if resolved.get("reasoning_effort") != "medium":
        raise ValueError("resolved OpenRouter reasoning policy is not frozen")
    routing_policy = resolved.get("routing_policy")
    expected_routing_policy = {
        "only": [expected_provider],
        "order": [expected_provider],
        "allow_fallbacks": False,
        "require_parameters": True,
        "data_collection": "deny",
        "zdr": True,
    }
    if routing_policy != expected_routing_policy:
        raise ValueError(
            "resolved OpenRouter wire routing policy and provider disagree"
        )
    if (
        expected_provider,
        resolved.get("eligible_endpoint_policy"),
    ) not in {
        ("OpenAI", "exactly_one"),
        ("Azure", "all_exact_one_selected"),
    }:
        raise ValueError(
            "resolved OpenRouter provider and endpoint policy disagree"
        )
    return resolved


def _resolve_request_identity(request):
    identity = _request_identity_tuple(request)
    matches = []
    for profile_id in (
            manifest.FLAGSHIP_PROFILE_ID,
            *manifest.QUALIFICATION_PROFILE_IDS):
        try:
            resolved = manifest.resolve_openrouter_identity(
                request["logical_model_id"], profile_id=profile_id
            )
        except ValueError:
            continue
        if tuple(resolved.get(key) for key in _REQUEST_IDENTITY_KEYS) == identity:
            matches.append(resolved)
    if len(matches) != 1:
        raise ValueError(
            "request does not resolve to exactly one frozen OpenRouter profile"
        )
    return _validate_resolved_identity(matches[0], identity)


def _panel_identity(
        logical_model_id, panel_profile=manifest.FLAGSHIP_PROFILE_ID):
    resolved = manifest.resolve_openrouter_identity(
        logical_model_id, profile_id=panel_profile
    )
    identity = tuple(resolved.get(key) for key in _REQUEST_IDENTITY_KEYS)
    _validate_resolved_identity(resolved, identity)
    return {key: resolved[key] for key in _REQUEST_IDENTITY_KEYS}


def _assistant_reasoning_fields(value):
    if value is None:
        return {}
    if type(value) is list:
        return {"reasoning_details": deepcopy(value)}
    if type(value) is dict and set(value).issubset({
            "reasoning", "reasoning_details"}):
        return deepcopy(value)
    raise ValueError("prior reasoning evidence has an unsupported shape")


def _prior_request_from_history(request, index):
    turn = request["prior_visible_turns"][index]
    prior_request = {
        "contract_version": request["contract_version"],
        "execution_id": request["execution_id"],
        "provider": request["provider"],
        "logical_model_id": request["logical_model_id"],
        "provider_model_id": request["provider_model_id"],
        "configuration_id": request["configuration_id"],
        "stage": turn["stage"],
        "prior_visible_turns": deepcopy(
            request["prior_visible_turns"][:index]
        ),
        "current_visible_turn": {
            "stage": turn["stage"],
            "content": turn["prompt"],
        },
        "response_schema": deepcopy(request["response_schema"]),
        "response_schema_sha256": request["response_schema_sha256"],
    }
    prior_request["request_sha256"] = contracts.canonical_sha256(
        prior_request
    )
    return contracts.validate_stage_request(prior_request)


def _derive_prior_reasoning(request, prior_results):
    if prior_results is None:
        prior_results = []
    if type(prior_results) is not list or len(prior_results) != len(
            request["prior_visible_turns"]):
        raise ValueError(
            "prior results must exactly cover visible request history"
        )
    reasoning = {}
    validated = []
    for index, supplied_result in enumerate(prior_results):
        prior_request = _prior_request_from_history(request, index)
        result = contracts.validate_stage_result(
            supplied_result, prior_request
        )
        if result["terminal_status"] in {"invalidated", "failed"}:
            raise ValueError("prior result is not safe visible history")
        final_attempt = result["attempts"][-1]
        if final_attempt["raw_final_message"] != request[
                "prior_visible_turns"][index]["response"]:
            raise ValueError("prior result does not match exact request history")
        reasoning[result["stage"]] = deepcopy(
            final_attempt["reasoning_details"]
        )
        validated.append(result)
    return reasoning, validated


def _validate_future_turns(future_turns):
    if future_turns is None:
        return []
    if type(future_turns) is not list or any(
            type(turn) is not dict
            or set(turn) != {"stage", "content"}
            or turn["stage"] not in contracts.STAGES
            or type(turn["content"]) is not str
            for turn in future_turns):
        raise ValueError("future turns must use exact visible-turn records")
    if len({turn["stage"] for turn in future_turns}) != len(future_turns):
        raise ValueError("future turns must not repeat stages")
    return deepcopy(future_turns)


def _assert_reasoning_is_prior_visible(request, reasoning, future_turns):
    if _contains_credential_material(reasoning):
        raise ValueError("prior reasoning contains credential material")
    if _forbidden_identifiers(reasoning):
        raise ValueError("prior reasoning contains forbidden identifiers")
    unavailable = [{
        "stage": request["stage"],
        "content": request["current_visible_turn"]["content"],
    }] + future_turns
    if not _future_absent([reasoning], unavailable):
        raise ValueError("prior reasoning contains current or future text")
    for turn in request["prior_visible_turns"]:
        if not _future_absent([turn["response"]], unavailable):
            raise ValueError("prior raw history contains current or future text")


def build_wire_request(
        request, *, api_key, prior_results=None, future_turns=None):
    """Build exact live headers plus a separately hashable public descriptor."""
    _assert_frozen_runtime_wire_configuration()
    request = contracts.validate_stage_request(request)
    if request["provider"] != "openrouter":
        raise ValueError("OpenRouter driver requires an OpenRouter StageRequest")
    resolved_identity = _resolve_request_identity(request)
    if type(api_key) is not str or not api_key:
        raise ValueError("OpenRouter API key must be supplied out of band")
    future_turns = _validate_future_turns(future_turns)
    prior_reasoning, _validated_prior = _derive_prior_reasoning(
        request, prior_results
    )
    _assert_reasoning_is_prior_visible(
        request, prior_reasoning, future_turns
    )

    messages = []
    for turn in request["prior_visible_turns"]:
        messages.append({"role": "user", "content": turn["prompt"]})
        assistant = {"role": "assistant", "content": turn["response"]}
        assistant.update(_assistant_reasoning_fields(
            prior_reasoning.get(turn["stage"])
        ))
        messages.append(assistant)
    messages.append({
        "role": "user",
        "content": request["current_visible_turn"]["content"],
    })

    body_object = {
        "model": request["provider_model_id"],
        "messages": messages,
        "stream": STREAMING_ENABLED,
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "reasoning": {
            "effort": resolved_identity["reasoning_effort"],
        },
        "response_format": {
            "type": RESPONSE_FORMAT_POLICY["type"],
            "json_schema": {
                "name": RESPONSE_FORMAT_POLICY["name"],
                "strict": RESPONSE_FORMAT_POLICY["strict"],
                "schema": deepcopy(request["response_schema"]),
            },
        },
        "provider": deepcopy(resolved_identity["routing_policy"]),
    }
    descriptor = {
        "method": "POST",
        "url": API_URL,
        "headers": deepcopy(SANITIZED_HEADERS),
        "body": deepcopy(body_object),
    }
    if any(
            _contains_exact_secret(value, api_key)
            for value in (prior_reasoning, messages, body_object, descriptor)):
        raise ValueError("OpenRouter API key must remain out of band")
    body = contracts.canonical_json_bytes(body_object)
    headers = {
        "Authorization": "Bearer " + api_key,
        **SANITIZED_HEADERS,
    }
    return WireRequest(
        url=API_URL,
        headers=headers,
        body=body,
        sanitized_descriptor=descriptor,
        transport_request_sha256=contracts.canonical_sha256(descriptor),
    )


def _build_failure_context(request, wire, run_mode):
    if run_mode not in {"mock", "openrouter", "openrouter_probe"}:
        raise ValueError("failure context run_mode is not OpenRouter-safe")
    identity_tuple = _request_identity_tuple(request)
    profile_id = manifest.frozen_identity_profile(identity_tuple)
    if run_mode == "mock":
        attempt_provenance = contracts.RUN_PROVENANCE["mock"]
    elif run_mode == "openrouter" and profile_id == manifest.FLAGSHIP_PROFILE_ID:
        attempt_provenance = LIVE_ATTEMPT_PROVENANCE
    elif (
        run_mode == "openrouter"
        and profile_id in manifest.QUALIFICATION_PROFILE_IDS
    ):
        attempt_provenance = LIVE_QUALIFICATION_ATTEMPT_PROVENANCE
    elif (
        run_mode == "openrouter_probe"
        and profile_id in manifest.QUALIFICATION_PROFILE_IDS
    ):
        attempt_provenance = LIVE_ACCESS_PROBE_ATTEMPT_PROVENANCE
    else:
        raise ValueError("failure context identity/run_mode scope is not authorized")
    return {
        "run_mode": run_mode,
        "attempt_provenance": attempt_provenance,
        "identity": {
            "provider": request["provider"],
            "logical_model_id": request["logical_model_id"],
            "model": request["provider_model_id"],
            "provider_model_id": request["provider_model_id"],
            "configuration_id": request["configuration_id"],
            "request_sha256": request["request_sha256"],
            "transport_request_sha256": wire.transport_request_sha256,
        },
    }


def validate_transport_descriptor(
        result, descriptor, *, request, prior_results, future_turns):
    """Reconstruct and bind the exact frozen descriptor and StageRequest."""
    result = contracts.validate_stage_result(result, request)
    if type(descriptor) is not dict or set(descriptor) != {
            "method", "url", "headers", "body"}:
        raise ValueError("transport descriptor keys are not exact")
    serialized = contracts.canonical_json_bytes(descriptor)
    if re.search(
            br"(?i)(?:\b(?:sk|rk)-[A-Za-z0-9_-]{8,}|"
            br"\bBearer\s+[A-Za-z0-9._~+/=-]+|"
            br"\bOPENROUTER_API_KEY\s*=)",
            serialized):
        raise ValueError("transport descriptor contains credential material")
    expected = build_wire_request(
        request,
        api_key="out-of-band-descriptor-validation-key",
        prior_results=prior_results,
        future_turns=future_turns,
    ).sanitized_descriptor
    if descriptor != expected:
        raise ValueError("transport descriptor differs from frozen request")
    if result["transport_request_sha256"] != contracts.canonical_sha256(
            descriptor):
        raise ValueError("transport descriptor hash mismatch")
    return deepcopy(descriptor)


def validate_episode_transport_descriptors(
        episode, requests, results, descriptors):
    """Bind every descriptor in a contiguous run prefix to episode evidence."""
    if (
        type(requests) is not list
        or type(results) is not list
        or type(descriptors) is not list
        or not requests
        or len(requests) != len(results)
        or len(requests) != len(descriptors)
        or len(requests) > len(contracts.STAGES)
    ):
        raise ValueError(
            "episode descriptor validation requires an exact nonempty prefix"
        )
    turns = model_turns(episode)
    validated_requests = []
    validated_results = []
    validated_descriptors = []
    expected_history = []
    identity = None
    for index, (request, result, descriptor) in enumerate(zip(
            requests, results, descriptors)):
        request = contracts.validate_stage_request(request)
        if request["stage"] != contracts.STAGES[index] or request[
                "current_visible_turn"] != turns[index]:
            raise ValueError("request prefix does not match exact episode turns")
        current_identity = tuple(request[key] for key in (
            "execution_id", "provider", "logical_model_id",
            "provider_model_id", "configuration_id",
        ))
        if identity is None:
            identity = current_identity
        elif current_identity != identity:
            raise ValueError("request prefix changed frozen execution identity")
        if request["prior_visible_turns"] != expected_history:
            raise ValueError("request prefix has non-contiguous episode history")
        result = contracts.validate_stage_result(result, request)
        if index < len(requests) - 1 and result[
                "terminal_status"] in {"invalidated", "failed"}:
            raise ValueError("request prefix advanced after a terminal result")
        descriptor = validate_transport_descriptor(
            result,
            descriptor,
            request=request,
            prior_results=validated_results,
            future_turns=turns[index + 1:],
        )
        validated_requests.append(request)
        validated_results.append(result)
        validated_descriptors.append(descriptor)
        raw_response = result["attempts"][-1]["raw_final_message"]
        if index < len(requests) - 1:
            if raw_response is None:
                raise ValueError("request prefix advanced without raw response")
            expected_history.append({
                "stage": request["stage"],
                "prompt": request["current_visible_turn"]["content"],
                "response": raw_response,
            })
    return validated_descriptors


def default_transport(*, url, headers, body, timeout):
    """Production stdlib transport; response bytes remain streaming/lossless."""
    request = urllib.request.Request(
        url=url,
        data=body,
        headers=headers,
        method="POST",
    )
    try:
        response = urllib.request.urlopen(request, timeout=timeout)
    except urllib.error.HTTPError as error:
        raw = error.read()
        return TransportResponse(
            status=error.code,
            headers=dict(error.headers.items()) if error.headers else {},
            chunks=[raw],
            closer=error.close,
        )
    except (urllib.error.URLError, TimeoutError, OSError):
        raise OpenRouterTransportError(
            "OpenRouter transport failed before an HTTP response"
        ) from None

    def chunks():
        while True:
            chunk = response.read(65536)
            if not chunk:
                break
            yield chunk

    return TransportResponse(
        status=response.status,
        headers=dict(response.headers.items()),
        chunks=chunks(),
        closer=response.close,
    )


def _read_exact_chunks(
        chunks, failure_context, *, exact_secret, response_headers=None):
    _raw, text = _capture_stream(
        chunks,
        failure_context,
        exact_secret=exact_secret,
        response_headers=response_headers,
    )
    return text


def _parse_sse(raw_trace):
    """Frame already-captured strict UTF-8 SSE without touching evidence."""
    if type(raw_trace) is not str:
        raise OpenRouterProtocolError("OpenRouter trace must be strict text")
    buffer = raw_trace
    data_lines = []
    events = []
    saw_done = False

    def finish_event():
        nonlocal data_lines, saw_done
        if not data_lines:
            return
        payload = "\n".join(data_lines)
        data_lines = []
        if payload == "[DONE]":
            if saw_done:
                raise OpenRouterProtocolError("duplicate OpenRouter DONE marker")
            saw_done = True
            return
        if saw_done:
            raise OpenRouterProtocolError("OpenRouter data followed DONE")
        events.append(_unique_json(payload))

    def consume_line(line):
        if line.endswith("\r"):
            line = line[:-1]
        if not line:
            finish_event()
            return
        if line.startswith(":"):
            return
        if not line.startswith("data:"):
            raise OpenRouterProtocolError("unexpected OpenRouter SSE field")
        value = line[5:]
        if value.startswith(" "):
            value = value[1:]
        data_lines.append(value)

    while "\n" in buffer:
        line, buffer = buffer.split("\n", 1)
        consume_line(line)
    if buffer:
        consume_line(buffer)
    finish_event()
    if not saw_done:
        raise OpenRouterProtocolError("OpenRouter stream lacks DONE marker")
    if not events:
        raise OpenRouterProtocolError("OpenRouter stream contains no events")
    return events


def _header(headers, name):
    if type(headers) is not dict:
        return None
    lowered = name.lower()
    for key, value in headers.items():
        if type(key) is str and key.lower() == lowered:
            return value
    return None


def _generation_id(headers, raw_bytes, failure_context):
    values = []
    if type(headers) is dict:
        values = [
            value for key, value in headers.items()
            if type(key) is str and key.lower() == "x-generation-id"
        ]
    if any(
            type(value) is str and _contains_credential_material(value)
            for value in values):
        raise _binary_protocol_error(
            "credential_material",
            raw_bytes,
            failure_context=failure_context,
            force_redact=True,
        )
    if len(values) != 1:
        return None
    value = values[0]
    if type(value) is not str or not value or value.strip() != value:
        return None
    return value


def _count(value, path):
    if value is None:
        return None
    if type(value) is not int or value < 0:
        raise OpenRouterProtocolError(f"invalid OpenRouter usage field {path}")
    return value


def _usage(value):
    if value is None:
        return deepcopy(NULL_USAGE)
    if type(value) is not dict:
        raise OpenRouterProtocolError("OpenRouter usage must be an object")
    prompt_details = value.get("prompt_tokens_details", {})
    completion_details = value.get("completion_tokens_details", {})
    if type(prompt_details) is not dict or type(completion_details) is not dict:
        raise OpenRouterProtocolError("OpenRouter usage details must be objects")
    return {
        "input_tokens": _count(value.get("prompt_tokens"), "prompt_tokens"),
        "cached_input_tokens": _count(
            prompt_details.get("cached_tokens"), "cached_tokens"
        ),
        "output_tokens": _count(
            value.get("completion_tokens"), "completion_tokens"
        ),
        "reasoning_tokens": _count(
            completion_details.get("reasoning_tokens"), "reasoning_tokens"
        ),
        "total_tokens": _count(value.get("total_tokens"), "total_tokens"),
    }


def _usage_consistent(usage):
    input_tokens = usage["input_tokens"]
    output_tokens = usage["output_tokens"]
    total_tokens = usage["total_tokens"]
    if any(value is None for value in (
            input_tokens, output_tokens, total_tokens)):
        return False
    if total_tokens != input_tokens + output_tokens:
        return False
    cached = usage["cached_input_tokens"]
    reasoning = usage["reasoning_tokens"]
    if cached is not None and cached > input_tokens:
        return False
    if reasoning is not None and reasoning > output_tokens:
        return False
    return True


def _route_evidence(
        metadata, requested_model, events, generation_id,
        metadata_indices, *, expected_provider="OpenAI",
        eligible_endpoint_policy="exactly_one",
        expected_returned_model_ids=None):
    if eligible_endpoint_policy not in {
            "exactly_one", "all_exact_one_selected"}:
        raise ValueError("unknown eligible-endpoint attestation policy")
    if expected_returned_model_ids is None:
        expected_returned_model_ids = [requested_model]
    if (
        type(expected_returned_model_ids) is not list
        or not expected_returned_model_ids
        or any(type(value) is not str or not value
               for value in expected_returned_model_ids)
        or len(expected_returned_model_ids) != len(set(
            expected_returned_model_ids
        ))
    ):
        raise ValueError("expected returned model IDs are not frozen")
    selected_provider = None
    selected_model = None
    ok = type(metadata) is dict
    if not ok:
        return False, "UNVERIFIED", "UNVERIFIED"
    ok = ok and metadata.get("requested") == requested_model
    ok = ok and metadata.get("strategy") == "direct"
    ok = ok and type(metadata.get("attempt")) is int and metadata.get(
        "attempt") == 1
    endpoints = metadata.get("endpoints")
    available = endpoints.get("available") if type(endpoints) is dict else None
    if (
        type(endpoints) is not dict
        or type(endpoints.get("total")) is not int
        or type(available) is not list
        or not available
        or endpoints.get("total") < len(available)
        or (
            eligible_endpoint_policy == "exactly_one"
            and (
                len(available) != 1
                or endpoints.get("total") != 1
            )
        )
    ):
        ok = False
        available = []
    selected = [
        row for row in available
        if type(row) is dict and row.get("selected") is True
    ]
    if len(selected) == 1:
        selected_provider = selected[0].get("provider")
        selected_model = selected[0].get("model")
    else:
        ok = False
    ok = ok and all(
        type(row) is dict
        and row.get("provider") == expected_provider
        and row.get("model") in expected_returned_model_ids
        and type(row.get("selected")) is bool
        for row in available)
    attempts = metadata.get("attempts")
    if attempts is not None and attempts != []:
        ok = ok and type(attempts) is list and len(attempts) == 1
    if type(attempts) is list and len(attempts) == 1:
        ok = ok and all(
            type(row) is dict
            and row.get("provider") == expected_provider
            and row.get("model") == selected_model
            and type(row.get("status")) is int
            and row.get("status") == 200
            for row in attempts)
    ok = ok and metadata.get("pipeline", []) == []
    ok = ok and metadata.get("fallback", False) is False
    ok = ok and metadata.get("fallbacks", []) == []
    ok = ok and type(generation_id) is str and bool(generation_id)
    ok = ok and generation_id.strip() == generation_id
    ok = ok and bool(events) and all(
        event.get("id") == generation_id
        and event.get("model") == selected_model
        and event.get("provider") == expected_provider
        for event in events)
    ok = ok and metadata_indices == [len(events) - 1]
    return (
        bool(ok),
        selected_model if type(selected_model) is str else "UNVERIFIED",
        selected_provider if type(selected_provider) is str else "UNVERIFIED",
    )


def _parse_success(
        raw_bytes, raw_trace, response_headers, requested_model,
        failure_context, *, exact_secret, expected_provider="OpenAI",
        eligible_endpoint_policy="exactly_one",
        expected_returned_model_ids=None):
    events = _parse_sse(raw_trace)
    if (
        _contains_exact_secret(events, exact_secret)
        or _contains_credential_material(events)
    ):
        raise _binary_protocol_error(
            "credential_material",
            raw_bytes,
            failure_context=failure_context,
            force_redact=True,
        )
    content = []
    reasoning_details = []
    reasoning_text = []
    tool_events = _capability_evidence(events)
    for identifier in _forbidden_identifiers(events):
        tool_events.append({
            "kind": "forbidden_identifier_echo",
            "value": identifier,
        })
    metadata_rows = []
    metadata_indices = []
    usage_rows = []
    finish_reasons = []
    finish_indices = []
    output_event_indices = []
    emitted_output_indices = []
    error_codes = (
        ["provider_failure_marker"]
        if _failure_status_evidence(events) else []
    )
    token_started = False

    for event_index, event in enumerate(events):
        if "openrouter_metadata" in event:
            metadata_rows.append(deepcopy(event["openrouter_metadata"]))
            metadata_indices.append(event_index)
        if "usage" in event:
            usage_rows.append((event_index, deepcopy(event["usage"])))
        if "error" in event:
            error = event["error"]
            if type(error) is dict and "code" in error:
                error_codes.append("stream_" + str(error["code"]))
            else:
                error_codes.append("stream_error_malformed")
        if event.get("status") in {"failed", "incomplete", "error"}:
            error_codes.append("status_" + event["status"])

        choices = event.get("choices", [])
        if type(choices) is not list:
            raise OpenRouterProtocolError("OpenRouter choices must be an array")
        if len(choices) > 1:
            raise OpenRouterProtocolError("OpenRouter returned multiple choices")
        if not choices:
            continue
        choice = choices[0]
        if type(choice) is not dict or choice.get("index") != 0:
            raise OpenRouterProtocolError("OpenRouter choice index is not exact")
        delta = choice.get("delta", {})
        if type(delta) is not dict:
            raise OpenRouterProtocolError("OpenRouter delta must be an object")
        output_event_indices.append(event_index)
        if "content" in delta:
            fragment = delta["content"]
            if fragment is not None and type(fragment) is not str:
                raise OpenRouterProtocolError(
                    "OpenRouter content delta must be text or null"
                )
            if fragment:
                token_started = True
                content.append(fragment)
                emitted_output_indices.append(event_index)
        if "reasoning_details" in delta:
            details = delta["reasoning_details"]
            if type(details) is not list:
                raise OpenRouterProtocolError(
                    "OpenRouter reasoning_details must be an array"
                )
            if details:
                token_started = True
                reasoning_details.extend(deepcopy(details))
                emitted_output_indices.append(event_index)
        if "reasoning" in delta:
            reasoning = delta["reasoning"]
            if reasoning is not None and type(reasoning) is not str:
                raise OpenRouterProtocolError(
                    "OpenRouter reasoning delta must be text or null"
                )
            if reasoning:
                token_started = True
                reasoning_text.append(reasoning)
                emitted_output_indices.append(event_index)
        if choice.get("finish_reason") is not None:
            if type(choice["finish_reason"]) is not str:
                raise OpenRouterProtocolError(
                    "OpenRouter finish reason must be text"
                )
            finish_reasons.append(choice["finish_reason"])
            finish_indices.append(event_index)

    metadata = metadata_rows[0] if len(metadata_rows) == 1 else None
    generation_id = _generation_id(
        response_headers, raw_bytes, failure_context
    )
    for identifier in _forbidden_identifiers(generation_id):
        tool_events.append({
            "kind": "forbidden_identifier_echo",
            "value": identifier,
        })
    route_ok, returned_model, returned_provider = _route_evidence(
        metadata,
        requested_model,
        events,
        generation_id,
        metadata_indices,
        expected_provider=expected_provider,
        eligible_endpoint_policy=eligible_endpoint_policy,
        expected_returned_model_ids=expected_returned_model_ids,
    )

    terminal_finish_repeat = False
    if finish_reasons == ["stop", "stop"] and len(usage_rows) == 1:
        terminal_index = finish_indices[-1]
        terminal_event = events[terminal_index]
        terminal_choices = terminal_event.get("choices")
        terminal_delta = (
            terminal_choices[0].get("delta")
            if type(terminal_choices) is list
            and len(terminal_choices) == 1
            and type(terminal_choices[0]) is dict
            else None
        )
        prior_output_indices = [
            index for index in output_event_indices if index < terminal_index
        ]
        terminal_finish_repeat = bool(
            terminal_index == len(events) - 1
            and metadata_indices == [terminal_index]
            and usage_rows[0][0] == terminal_index
            and output_event_indices
            and max(output_event_indices) == terminal_index
            and prior_output_indices
            and finish_indices[0] == max(prior_output_indices)
            and not any(
                index > finish_indices[0]
                for index in emitted_output_indices
            )
            and type(terminal_delta) is dict
            and terminal_delta.get("content") in {None, ""}
            and terminal_delta.get("reasoning") in {None, ""}
            and terminal_delta.get("reasoning_details") in (None, [], ())
        )

    usage = deepcopy(NULL_USAGE)
    if len(usage_rows) != 1:
        error_codes.append("terminal_usage_count")
    else:
        usage_index, usage_value = usage_rows[0]
        try:
            usage = _usage(usage_value)
        except OpenRouterProtocolError:
            error_codes.append("terminal_usage_shape")
            usage = deepcopy(NULL_USAGE)
        else:
            if not _usage_consistent(usage):
                error_codes.append("terminal_usage_inconsistent")
        if (
            not finish_indices
            or (
                terminal_finish_repeat
                and usage_index != finish_indices[-1]
            )
            or (
                not terminal_finish_repeat
                and usage_index <= max(finish_indices)
            )
            or (
                output_event_indices
                and not terminal_finish_repeat
                and usage_index <= max(output_event_indices)
            )
        ):
            error_codes.append("terminal_usage_order")

    if finish_reasons == ["stop", "stop"] and terminal_finish_repeat:
        pass
    elif finish_reasons != ["stop"]:
        if not finish_reasons:
            error_codes.append("missing_finish_reason")
        elif len(finish_reasons) != 1:
            error_codes.append("multiple_finish_reasons")
        else:
            error_codes.append("finish_reason_" + finish_reasons[0])
    elif (
        not emitted_output_indices
        or not output_event_indices
        or finish_indices != [max(output_event_indices)]
    ):
        error_codes.append("finish_not_final_output")

    if reasoning_details and reasoning_text:
        reasoning = {
            "reasoning_details": reasoning_details,
            "reasoning": "".join(reasoning_text),
        }
    elif reasoning_details:
        reasoning = reasoning_details
    elif reasoning_text:
        reasoning = {"reasoning": "".join(reasoning_text)}
    else:
        reasoning = None
    raw_final = "".join(content) if content else None
    error_code = (
        "|".join(sorted(set(error_codes))) if error_codes else None
    )
    return {
        "raw_trace": raw_trace,
        "raw_final_message": raw_final,
        "reasoning_details": reasoning,
        "tool_events": tool_events,
        "usage": usage,
        "finish_reason": (
            finish_reasons[-1] if finish_reasons else None
        ),
        "error_code": error_code,
        "token_emission_started": token_started,
        "provider_request_id": (
            generation_id
        ),
        "returned_provider_model_id": returned_model,
        "returned_provider_name": returned_provider,
        "route_ok": route_ok,
        "decoded_events": events,
    }


def _future_absent(values, future_turns):
    def strings(value):
        if type(value) is str:
            yield value
        elif type(value) is list:
            for item in value:
                yield from strings(item)
        elif type(value) is dict:
            for key, item in value.items():
                yield key
                yield from strings(item)

    for value in values:
        for source in strings(value):
            for turn in future_turns:
                content = turn["content"]
                if content in source or contracts.sha256_utf8(content) in source:
                    return False
    return True


def _retry_delay(headers, attempt_index):
    value = _header(headers, "Retry-After")
    if type(value) is str and value.isdigit():
        return min(int(value), MAX_RETRY_DELAY_SECONDS)
    return min(2 ** (attempt_index - 1), MAX_RETRY_DELAY_SECONDS)


def _run_stage_record(
        request, *, future_turns, transport, api_key, now, sleeper,
        prior_results, run_mode, before_stage=None, integrity_session=1):
    request = contracts.validate_stage_request(request)
    resolved_identity = _resolve_request_identity(request)
    reasoning_effort = resolved_identity["reasoning_effort"]
    if type(future_turns) is not list or any(
            type(turn) is not dict or set(turn) != {"stage", "content"}
            for turn in future_turns):
        raise ValueError("future turns must use exact visible-turn records")
    wire = build_wire_request(
        request,
        api_key=api_key,
        prior_results=prior_results,
        future_turns=future_turns,
    )
    _emit_stage_hook(
        before_stage,
        integrity_session=integrity_session,
        request=request,
        transport_descriptor=wire.sanitized_descriptor,
    )
    failure_context = _build_failure_context(request, wire, run_mode)
    attempts = []
    returned_model = "UNVERIFIED"
    returned_provider = "UNVERIFIED"
    tool_events = []
    isolation_ok = True
    future_text_absent = True

    for attempt_index in range(1, MAX_TRANSPORT_ATTEMPTS + 1):
        started = now()
        try:
            response = transport(
                url=wire.url,
                headers=wire.headers,
                body=wire.body,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
        except OpenRouterTransportError:
            completed = now()
            attempts.append(contracts.build_stage_attempt(
                attempt_index=attempt_index,
                started_at_utc=started,
                completed_at_utc=completed,
                provider_request_id=None,
                token_emission_started=False,
                exit_status=None,
                http_status=None,
                finish_reason=None,
                usage=deepcopy(NULL_USAGE),
                raw_trace="",
                raw_final_message=None,
                reasoning_effort=reasoning_effort,
                reasoning_details=None,
                error_code="transport_error",
            ))
            if attempt_index < MAX_TRANSPORT_ATTEMPTS:
                sleeper(_retry_delay({}, attempt_index))
                continue
            break
        if not isinstance(response, TransportResponse):
            raise OpenRouterProtocolError(
                "transport returned an unsupported response object"
            )
        if type(response.status) is not int or not 100 <= response.status <= 599:
            raise OpenRouterProtocolError("transport returned an invalid status")
        try:
            raw_bytes, raw_trace = _capture_stream(
                response.chunks,
                failure_context,
                exact_secret=api_key,
                response_headers=response.headers,
            )
            if response.status != 200:
                error_code = "http_" + str(response.status)
                completed = now()
                attempts.append(contracts.build_stage_attempt(
                    attempt_index=attempt_index,
                    started_at_utc=started,
                    completed_at_utc=completed,
                    provider_request_id=_generation_id(
                        response.headers, raw_bytes, failure_context
                    ),
                    token_emission_started=False,
                    exit_status=None,
                    http_status=response.status,
                    finish_reason=None,
                    usage=deepcopy(NULL_USAGE),
                    raw_trace=raw_trace,
                    raw_final_message=None,
                    reasoning_effort=reasoning_effort,
                    reasoning_details=None,
                    error_code=error_code,
                ))
                if (
                    response.status in {429, 503}
                    and attempt_index < MAX_TRANSPORT_ATTEMPTS
                ):
                    sleeper(_retry_delay(response.headers, attempt_index))
                    continue
                break

            try:
                parsed = _parse_success(
                    raw_bytes,
                    raw_trace,
                    response.headers,
                    request["provider_model_id"],
                    failure_context,
                    exact_secret=api_key,
                    expected_provider=resolved_identity[
                        "expected_returned_provider"
                    ],
                    eligible_endpoint_policy=resolved_identity[
                        "eligible_endpoint_policy"
                    ],
                    expected_returned_model_ids=resolved_identity[
                        "expected_returned_provider_model_ids"
                    ],
                )
            except OpenRouterProtocolError as error:
                if error.failure_record is not None:
                    raise
                isolation_ok = False
                completed = now()
                attempts.append(contracts.build_stage_attempt(
                    attempt_index=attempt_index,
                    started_at_utc=started,
                    completed_at_utc=completed,
                    provider_request_id=_generation_id(
                        response.headers, raw_bytes, failure_context
                    ),
                    token_emission_started=False,
                    exit_status=None,
                    http_status=200,
                    finish_reason=None,
                    usage=deepcopy(NULL_USAGE),
                    raw_trace=raw_trace,
                    raw_final_message=None,
                    reasoning_effort=reasoning_effort,
                    reasoning_details=None,
                    error_code="protocol_malformed_sse",
                ))
                break
            returned_model = parsed["returned_provider_model_id"]
            returned_provider = parsed["returned_provider_name"]
            tool_events = parsed["tool_events"]
            isolation_ok = parsed["route_ok"]
            future_text_absent = _future_absent((
                parsed["raw_trace"], parsed["raw_final_message"],
                parsed["reasoning_details"], tool_events,
                parsed["decoded_events"],
            ), future_turns)
            completed = now()
            attempts.append(contracts.build_stage_attempt(
                attempt_index=attempt_index,
                started_at_utc=started,
                completed_at_utc=completed,
                provider_request_id=parsed["provider_request_id"],
                token_emission_started=parsed["token_emission_started"],
                exit_status=None,
                http_status=200,
                finish_reason=parsed["finish_reason"],
                usage=parsed["usage"],
                raw_trace=parsed["raw_trace"],
                raw_final_message=parsed["raw_final_message"],
                reasoning_effort=reasoning_effort,
                reasoning_details=parsed["reasoning_details"],
                error_code=parsed["error_code"],
            ))
            break
        finally:
            response.close()

    result = contracts.build_stage_result(
        request,
        run_mode=run_mode,
        returned_provider_model_id=returned_model,
        returned_provider_name=returned_provider,
        session_id=None,
        transport_request_sha256=wire.transport_request_sha256,
        attempts=attempts,
        tool_events=tool_events,
        session_chain_ok=True,
        isolation_ok=isolation_ok,
        future_text_absent=future_text_absent,
    )
    validate_transport_descriptor(
        result,
        wire.sanitized_descriptor,
        request=request,
        prior_results=prior_results,
        future_turns=future_turns,
    )
    return {
        "result": result,
        "transport_descriptor": deepcopy(wire.sanitized_descriptor),
    }


def _assert_run_dependencies(
        run_mode, *, transport, now, sleeper, uuid_factory=None):
    _assert_frozen_runtime_wire_configuration()
    if run_mode not in {"mock", "openrouter", "openrouter_probe"}:
        raise ValueError(
            "OpenRouter run_mode must be mock, openrouter, or openrouter_probe"
        )
    if run_mode == "mock":
        return
    production_only = (
        transport is default_transport
        and now is utc_now
        and sleeper is time.sleep
        and (uuid_factory is None or uuid_factory is uuid.uuid4)
    )
    if not production_only:
        raise ValueError(
            "live OpenRouter provenance requires production defaults"
        )


def _assert_public_stage_scope(request, run_mode):
    """Reject cheap live work from the generic one-stage entry point."""
    if run_mode not in {"openrouter", "openrouter_probe"}:
        return
    profile_id = manifest.frozen_identity_profile(
        _request_identity_tuple(contracts.validate_stage_request(request))
    )
    if profile_id in manifest.QUALIFICATION_PROFILE_IDS:
        raise ValueError(
            "cheap live stages require a dedicated qualification or access API"
        )
    if run_mode == "openrouter_probe":
        raise ValueError("access probes require the dedicated cheap access API")


def _assert_qualification_profile(profile_id):
    """Reject non-qualification profiles at every dedicated API boundary."""
    if (
        type(profile_id) is not str
        or profile_id not in manifest.QUALIFICATION_PROFILE_IDS
    ):
        raise ValueError("dedicated qualification profile_id is not frozen")


def _assert_episode_scope(run_mode, panel_profile, authorization):
    if run_mode == "mock":
        return
    if run_mode == "openrouter_probe":
        raise ValueError("four-stage execution cannot use access-probe run_mode")
    if run_mode != "openrouter":
        return
    if panel_profile == manifest.FLAGSHIP_PROFILE_ID:
        return
    if (
        panel_profile in manifest.QUALIFICATION_PROFILE_IDS
        and authorization is _LIVE_CHEAP_QUALIFICATION_AUTHORIZATION
    ):
        return
    raise ValueError(
        "cheap live episodes require the dedicated qualification API"
    )


def _integrity_rerun_allowed(result):
    if result["terminal_status"] != "invalidated":
        return False
    violations = set(result["integrity"]["violations"])
    final_attempt = result["attempts"][-1]
    return bool(violations) and (
        violations <= contracts.INTEGRITY_RERUN_ALLOWED_VIOLATIONS
        and "transport_error" not in violations
        and final_attempt["error_code"] is None
        and final_attempt["exit_status"] in (None, 0)
        and final_attempt["http_status"] in (None, 200)
    )


def run_stage(
        request, *, future_turns, transport=default_transport, api_key,
        now=utc_now, sleeper=time.sleep, prior_results=None,
        run_mode="mock"):
    """Execute one stage; fixture callers remain non-measurements by default."""
    _assert_public_stage_scope(request, run_mode)
    _assert_run_dependencies(
        run_mode, transport=transport, now=now, sleeper=sleeper
    )
    return _run_stage_record(
        request,
        future_turns=future_turns,
        transport=transport,
        api_key=api_key,
        now=now,
        sleeper=sleeper,
        prior_results=([] if prior_results is None else prior_results),
        run_mode=run_mode,
    )["result"]


def _run_episode_core(
        episode, *, logical_model_id, transport=default_transport, api_key,
        uuid_factory=uuid.uuid4, now=utc_now, sleeper=time.sleep,
        run_mode="mock", before_stage=None, stage_sink=None,
        panel_profile=manifest.FLAGSHIP_PROFILE_ID, authorization=None):
    """Run four progressive turns, with one whole-episode integrity rerun."""
    _validate_stage_hooks(before_stage, stage_sink)
    _assert_episode_scope(run_mode, panel_profile, authorization)
    _assert_run_dependencies(
        run_mode,
        transport=transport,
        now=now,
        sleeper=sleeper,
        uuid_factory=uuid_factory,
    )
    identity = _panel_identity(
        logical_model_id, panel_profile=panel_profile
    )
    turns = model_turns(episode)
    sessions = []
    prior_invalidated = None

    for integrity_session in (1, 2):
        execution_id = str(uuid_factory())
        requests = []
        results = []
        descriptors = []
        prior_responses = {}

        for index, stage in enumerate(contracts.STAGES):
            request = contracts.build_stage_request(
                episode,
                execution_id=execution_id,
                stage=stage,
                prior_responses=prior_responses,
                **identity,
            )
            if index == 0 and prior_invalidated is not None:
                contracts.validate_integrity_rerun(
                    prior_invalidated["requests"],
                    prior_invalidated["results"],
                    [request],
                )
            try:
                record = _run_stage_record(
                    request,
                    future_turns=turns[index + 1:],
                    transport=transport,
                    api_key=api_key,
                    now=now,
                    sleeper=sleeper,
                    prior_results=results,
                    run_mode=run_mode,
                    before_stage=before_stage,
                    integrity_session=integrity_session,
                )
            except OpenRouterProtocolError as error:
                if error.failure_record is None:
                    raise
                failure_record = deepcopy(error.failure_record)
                session = {
                    "integrity_session": integrity_session,
                    "execution_id": execution_id,
                    "status": "failed",
                    "requests": requests + [request],
                    "results": results,
                    "transport_descriptors": descriptors,
                    "chain": None,
                    "failure_record": failure_record,
                }
                sessions.append(session)
                return {
                    "status": "failed",
                    "provenance": failure_record["provenance"],
                    "measurement_ready": False,
                    "integrity_session_count": integrity_session,
                    "sessions": sessions,
                    "requests": requests + [request],
                    "results": results,
                    "transport_descriptors": descriptors,
                    "chain": None,
                    "failure_record": failure_record,
                }
            result = record["result"]
            requests.append(request)
            results.append(result)
            descriptors.append(record["transport_descriptor"])
            validate_episode_transport_descriptors(
                episode, requests, results, descriptors
            )
            _emit_stage_hook(
                stage_sink,
                integrity_session=integrity_session,
                request=request,
                transport_descriptor=record["transport_descriptor"],
                result=result,
                include_result=True,
            )

            if result["terminal_status"] in {"invalidated", "failed"}:
                break
            raw_final = result["attempts"][-1]["raw_final_message"]
            if raw_final is None:
                break
            prior_responses[stage] = raw_final

        if results[-1]["terminal_status"] == "invalidated":
            session = {
                "integrity_session": integrity_session,
                "execution_id": execution_id,
                "status": "invalidated",
                "requests": requests,
                "results": results,
                "transport_descriptors": descriptors,
            }
            sessions.append(session)
            if (
                integrity_session == 1
                and _integrity_rerun_allowed(results[-1])
            ):
                prior_invalidated = session
                continue
            return {
                "status": "invalidated",
                "provenance": results[-1]["provenance"],
                "integrity_session_count": integrity_session,
                "sessions": sessions,
                "requests": requests,
                "results": results,
                "transport_descriptors": descriptors,
                "chain": None,
            }
        if results[-1]["terminal_status"] == "failed":
            sessions.append({
                "integrity_session": integrity_session,
                "execution_id": execution_id,
                "status": "failed",
                "requests": requests,
                "results": results,
                "transport_descriptors": descriptors,
            })
            return {
                "status": "failed",
                "provenance": results[-1]["provenance"],
                "integrity_session_count": integrity_session,
                "sessions": sessions,
                "requests": requests,
                "results": results,
                "transport_descriptors": descriptors,
                "chain": None,
            }

        chain = contracts.build_stage_chain(requests, results, episode)
        status = (
            "complete"
            if all(row["terminal_status"] == "complete" for row in results)
            else "unresolved"
        )
        sessions.append({
            "integrity_session": integrity_session,
            "execution_id": execution_id,
            "status": status,
            "requests": requests,
            "results": results,
            "transport_descriptors": descriptors,
            "chain": chain,
        })
        return {
            "status": status,
            "provenance": results[-1]["provenance"],
            "integrity_session_count": integrity_session,
            "sessions": sessions,
            "requests": requests,
            "results": results,
            "transport_descriptors": descriptors,
            "chain": chain,
        }
    raise AssertionError("unreachable integrity-session state")


def run_episode(
        episode, *, logical_model_id, transport=default_transport, api_key,
        uuid_factory=uuid.uuid4, now=utc_now, sleeper=time.sleep,
        run_mode="mock", before_stage=None, stage_sink=None,
        panel_profile=manifest.FLAGSHIP_PROFILE_ID):
    """Generic fixture/flagship runner; cheap mock fixtures remain supported."""
    return _run_episode_core(
        episode,
        logical_model_id=logical_model_id,
        transport=transport,
        api_key=api_key,
        uuid_factory=uuid_factory,
        now=now,
        sleeper=sleeper,
        run_mode=run_mode,
        before_stage=before_stage,
        stage_sink=stage_sink,
        panel_profile=panel_profile,
    )


def _run_episode_authorized(
        episode, *, logical_model_id, api_key, run_mode, panel_profile,
        authorization, before_stage=None, stage_sink=None):
    _assert_qualification_profile(panel_profile)
    if authorization is not _LIVE_CHEAP_QUALIFICATION_AUTHORIZATION:
        raise ValueError("cheap live qualification authorization is invalid")
    return _run_episode_core(
        episode,
        logical_model_id=logical_model_id,
        api_key=api_key,
        run_mode=run_mode,
        before_stage=before_stage,
        stage_sink=stage_sink,
        panel_profile=panel_profile,
        authorization=authorization,
    )


def _run_live_access_probe(
        *, logical_model_id, api_key, transport, uuid_factory, now, sleeper,
        before_stage=None, stage_sink=None, authorization=None,
        profile_id=manifest.CHEAP_PROFILE_ID):
    """Private, testable one-stage core for the canonical access probe."""
    _assert_qualification_profile(profile_id)
    if authorization is not _LIVE_ACCESS_PROBE_AUTHORIZATION:
        raise ValueError("live access probe authorization is invalid")
    _validate_stage_hooks(before_stage, stage_sink)
    probe = manifest.validate_cheap_access_probe(
        manifest.build_cheap_access_probe(
            logical_model_id, profile_id=profile_id
        ),
        logical_model_id=logical_model_id,
        profile_id=profile_id,
    )
    identity = _panel_identity(
        logical_model_id, panel_profile=profile_id
    )
    turns = model_turns(probe)
    execution_id = str(uuid_factory())
    request = contracts.build_stage_request(
        probe,
        execution_id=execution_id,
        stage="stage_1",
        prior_responses={},
        **identity,
    )
    try:
        record = _run_stage_record(
            request,
            future_turns=turns[1:],
            transport=transport,
            api_key=api_key,
            now=now,
            sleeper=sleeper,
            prior_results=[],
            run_mode="openrouter_probe",
            before_stage=before_stage,
            integrity_session=1,
        )
    except OpenRouterProtocolError as error:
        if error.failure_record is None:
            raise
        failure_record = deepcopy(error.failure_record)
        session = {
            "integrity_session": 1,
            "execution_id": execution_id,
            "status": "failed",
            "requests": [request],
            "results": [],
            "transport_descriptors": [],
            "chain": None,
            "failure_record": failure_record,
        }
        return {
            "status": "failed",
            "provenance": failure_record["provenance"],
            "measurement_ready": False,
            "integrity_session_count": 1,
            "sessions": [session],
            "requests": [request],
            "results": [],
            "transport_descriptors": [],
            "chain": None,
            "failure_record": failure_record,
        }

    result = record["result"]
    descriptor = record["transport_descriptor"]
    validate_episode_transport_descriptors(
        probe, [request], [result], [descriptor]
    )
    _emit_stage_hook(
        stage_sink,
        integrity_session=1,
        request=request,
        transport_descriptor=descriptor,
        result=result,
        include_result=True,
    )
    status = result["terminal_status"]
    session = {
        "integrity_session": 1,
        "execution_id": execution_id,
        "status": status,
        "requests": [request],
        "results": [result],
        "transport_descriptors": [descriptor],
        "chain": None,
    }
    return {
        "status": status,
        "provenance": result["provenance"],
        "measurement_ready": False,
        "integrity_session_count": 1,
        "sessions": [session],
        "requests": [request],
        "results": [result],
        "transport_descriptors": [descriptor],
        "chain": None,
    }


def run_live_episode(
        episode, *, logical_model_id, api_key, before_stage=None,
        stage_sink=None, panel_profile=manifest.FLAGSHIP_PROFILE_ID):
    """Production-only entry point for live OpenRouter measurement runs."""
    if panel_profile != manifest.FLAGSHIP_PROFILE_ID:
        raise ValueError(
            "cheap live episodes require the dedicated qualification API"
        )
    return run_episode(
        episode,
        logical_model_id=logical_model_id,
        api_key=api_key,
        run_mode="openrouter",
        before_stage=before_stage,
        stage_sink=stage_sink,
        panel_profile=panel_profile,
    )


def run_live_cheap_qualification_episode(
        episode, *, logical_model_id, purpose, api_key, before_stage=None,
        stage_sink=None, profile_id=manifest.CHEAP_PROFILE_ID):
    """Run one exact public cheap canary/smoke episode in production."""
    _assert_qualification_profile(profile_id)
    validated = manifest.validate_public_qualification_episode(
        episode, purpose=purpose
    )
    _panel_identity(
        logical_model_id, panel_profile=profile_id
    )
    return _run_episode_authorized(
        validated,
        logical_model_id=logical_model_id,
        api_key=api_key,
        run_mode="openrouter",
        before_stage=before_stage,
        stage_sink=stage_sink,
        panel_profile=profile_id,
        authorization=_LIVE_CHEAP_QUALIFICATION_AUTHORIZATION,
    )


def run_live_access_probe(
        *, logical_model_id, api_key, before_stage=None, stage_sink=None,
        profile_id=manifest.CHEAP_PROFILE_ID):
    """Run exactly stage one of the canonical non-bank cheap access probe."""
    _assert_qualification_profile(profile_id)
    _assert_run_dependencies(
        "openrouter_probe",
        transport=default_transport,
        now=utc_now,
        sleeper=time.sleep,
        uuid_factory=uuid.uuid4,
    )
    return _run_live_access_probe(
        logical_model_id=logical_model_id,
        api_key=api_key,
        transport=default_transport,
        uuid_factory=uuid.uuid4,
        now=utc_now,
        sleeper=time.sleep,
        before_stage=before_stage,
        stage_sink=stage_sink,
        profile_id=profile_id,
        authorization=_LIVE_ACCESS_PROBE_AUTHORIZATION,
    )
