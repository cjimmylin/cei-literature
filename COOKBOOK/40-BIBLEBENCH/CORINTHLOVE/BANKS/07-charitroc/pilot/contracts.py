"""Provider-neutral, fail-closed contracts for staged model requests.

Only model-visible prompts and prior model responses cross this boundary.  Bank
identifiers, canaries, sidecar fields, judge identifiers, and credentials are
deliberately neither serialized nor accepted.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import math
import re
import uuid

from lib.payloads import model_turns
from pilot import manifest
from scorers import action_scale


CONTRACT_VERSION = "charitroc-stage-request-v1"
STAGES = ("stage_1", "stage_2", "stage_3", "stage_4")
STAGE_REQUEST_KEYS = {
    "contract_version",
    "execution_id",
    "provider",
    "logical_model_id",
    "provider_model_id",
    "configuration_id",
    "stage",
    "prior_visible_turns",
    "current_visible_turn",
    "response_schema",
    "response_schema_sha256",
    "request_sha256",
}
PRIOR_TURN_KEYS = {"stage", "prompt", "response"}
CURRENT_TURN_KEYS = {"stage", "content"}

RESULT_CONTRACT_VERSION = "charitroc-stage-result-v1"
RUN_PROVENANCE = {
    "mock": "harness validation, NOT a measurement",
    "codex": "live Codex calibration measurement",
    "openrouter": "live OpenRouter calibration measurement",
    "openrouter_probe": "live OpenRouter access probe, NOT a measurement",
}
CHEAP_OPENROUTER_PROVENANCE = "live OpenRouter qualification measurement"
STAGE_RESULT_KEYS = {
    "contract_version", "provenance", "run_mode", "execution_id",
    "provider", "logical_model_id", "requested_provider_model_id",
    "returned_provider_model_id", "returned_provider_name",
    "configuration_id", "stage", "request_sha256",
    "transport_request_sha256", "response_schema_sha256", "session_id",
    "transport_retry_count", "attempts", "tool_events", "terminal_status",
    "integrity", "result_sha256",
}
STAGE_ATTEMPT_KEYS = {
    "attempt_index", "started_at_utc", "completed_at_utc",
    "provider_request_id", "token_emission_started", "exit_status",
    "http_status", "finish_reason", "usage", "raw_trace",
    "raw_trace_sha256", "raw_final_message", "raw_final_message_sha256",
    "parsed_response", "parsed_response_sha256", "parse_mode",
    "reasoning_effort", "reasoning_details", "reasoning_details_sha256",
    "error_code",
}
USAGE_KEYS = {
    "input_tokens", "cached_input_tokens", "output_tokens",
    "reasoning_tokens", "total_tokens",
}
INTEGRITY_KEYS = {
    "provider_identity_ok", "session_chain_ok", "isolation_ok",
    "future_text_absent", "tools_absent", "trace_complete",
    "identifier_echo_absent", "transport_successful",
    "mechanically_resolved", "violations", "integrity_valid",
    "measurement_ready",
}
TERMINAL_STATUSES = {"complete", "unresolved", "invalidated", "failed"}
INTEGRITY_RERUN_ALLOWED_VIOLATIONS = {
    "provider_identity", "session_chain", "isolation", "future_text",
    "tool_event", "trace_incomplete", "forbidden_identifier_echo",
}
CHAIN_CONTRACT_VERSION = "charitroc-stage-chain-v1"
STAGE_CHAIN_KEYS = {
    "contract_version", "provenance", "run_mode", "execution_id",
    "provider", "logical_model_id", "provider_model_id",
    "configuration_id", "response_schema_sha256", "stage_count",
    "request_sha256s", "result_sha256s", "session_id",
    "measurement_ready", "chain_sha256",
}

_UUID4_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_RFC3339_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
_ITEM_ID_RE = re.compile(r"CHARITROC-[0-9]{4}", re.IGNORECASE)
_JUDGE_ID_RE = re.compile(
    r"JUDGE-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}",
    re.IGNORECASE,
)
_SECRET_VALUE_RE = re.compile(
    r"(?i)(?:\b(?:sk|rk)-[A-Za-z0-9_-]{8,}|"
    r"\bBearer\s+[A-Za-z0-9._~+/=-]+|"
    r"\bOPENROUTER_API_KEY\s*=)"
)

_HIDDEN_KEYS = {
    "id",
    "item_id",
    "episode_id",
    "occurrence_id",
    "design",
    "verse_anchors",
    "template_family",
    "family",
    "split",
    "canary",
    "sidecar",
    "ground_truth",
    "metadata",
    "hidden_metadata",
    "true_type",
    "truth",
    "label",
    "surface",
    "cue",
    "cue_class",
    "cue_variant",
    "signal_band",
    "prior",
    "base_rate",
    "base_rate_benign",
    "initial_signal_band",
    "pair_id",
    "pair_arm",
    "defeat_class",
    "cue_truth_status",
    "expected_stage3",
    "latent_evidence",
    "surface_template_id",
    "semantic_bank_id",
    "entity_pool_id",
    "resource_pool_id",
    "cue_realization_id",
    "cue_surface_pool_id",
    "cue_realization_metadata",
    "world_id",
    "indistinguishable_control",
    "oracle",
    "scoring_key",
    "failure_modes",
    "rubric_emphases",
    "judge_case_id",
    "judge_id",
    "judge_ids",
    "judge_token_map",
}
_SECRET_KEY_FRAGMENTS = (
    "api_key",
    "apikey",
    "password",
    "passwd",
    "secret",
    "credential",
    "authorization",
    "auth_token",
    "access_token",
    "refresh_token",
    "bearer_token",
    "token",
    "private_key",
    "session_cookie",
    "cookie",
    "headers",
    "environment",
    "env",
    "signed_url",
)


def _assert_json_domain(value):
    """Reject Python-only values before JSON encoding.

    Exact Python container/scalar types keep the wire representation
    deterministic and avoid bool/int or tuple/list ambiguities.
    """
    value_type = type(value)
    if value is None or value_type in {str, bool, int}:
        return
    if value_type is float:
        if not math.isfinite(value):
            raise ValueError("value is not strict canonical JSON")
        return
    if value_type is list:
        for item in value:
            _assert_json_domain(item)
        return
    if value_type is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise ValueError("value is not strict canonical JSON")
            _assert_json_domain(item)
        return
    raise ValueError("value is not strict canonical JSON")


def canonical_json_bytes(value):
    """Return UTF-8 RFC-8259 JSON with deterministic key ordering."""
    _assert_json_domain(value)
    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeError):
        # Do not include the rejected value (which may be a credential).
        raise ValueError("value is not strict canonical JSON") from None


def canonical_sha256(value):
    """Hash the strict canonical JSON representation of *value*."""
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _reject_json_constant(_value):
    raise ValueError("serialized request is not strict JSON")


def _unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            # Key/value text is intentionally omitted to avoid credential leaks.
            raise ValueError("serialized request contains a duplicate JSON key")
        result[key] = value
    return result


def _loads_unique(payload):
    if type(payload) is bytes:
        try:
            payload = payload.decode("utf-8", errors="strict")
        except UnicodeError:
            raise ValueError("serialized request must be UTF-8 JSON") from None
    if type(payload) is not str:
        raise ValueError("serialized request must be text or UTF-8 bytes")
    try:
        parsed = json.loads(
            payload,
            object_pairs_hook=_unique_json_object,
            parse_constant=_reject_json_constant,
        )
    except (json.JSONDecodeError, TypeError, ValueError):
        # Never echo source JSON: it can contain an accidentally supplied key.
        raise ValueError("serialized request is not unique-key strict JSON") from None
    return parsed


def _normalized_key(key):
    return key.strip().lower().replace("-", "_").replace(" ", "_")


def _assert_no_forbidden_content(value):
    """Recursively reject hidden identifiers/metadata and credential material."""
    if type(value) is dict:
        for key, item in value.items():
            normalized = _normalized_key(key)
            if normalized in _HIDDEN_KEYS:
                raise ValueError("request contains a forbidden hidden-metadata key")
            if any(fragment in normalized for fragment in _SECRET_KEY_FRAGMENTS):
                raise ValueError("request contains a forbidden credential key")
            _assert_no_forbidden_content(item)
        return
    if type(value) is list:
        for item in value:
            _assert_no_forbidden_content(item)
        return
    if type(value) is str:
        if (
            "10cb-07-" in value.lower()
            or _ITEM_ID_RE.search(value) is not None
            or _JUDGE_ID_RE.search(value) is not None
        ):
            raise ValueError("request visible text contains a forbidden identifier")
        if _SECRET_VALUE_RE.search(value) is not None:
            raise ValueError("request visible text contains credential material")


def _assert_no_credential_material(value):
    """Reject transport credential material without echoing any source value."""
    if type(value) is dict:
        for key, item in value.items():
            normalized = _normalized_key(key)
            if any(fragment in normalized for fragment in _SECRET_KEY_FRAGMENTS):
                raise ValueError("result contains credential material")
            _assert_no_credential_material(item)
        return
    if type(value) is list:
        for item in value:
            _assert_no_credential_material(item)
        return
    if type(value) is str and _SECRET_VALUE_RE.search(value) is not None:
        raise ValueError("result contains credential material")


def _contains_forbidden_identifier(value):
    """Detect bank-private identifiers in preserved provider evidence."""
    if type(value) is str:
        return (
            "10cb-07-" in value.lower()
            or _ITEM_ID_RE.search(value) is not None
            or _JUDGE_ID_RE.search(value) is not None
        )
    if type(value) is list:
        return any(_contains_forbidden_identifier(item) for item in value)
    if type(value) is dict:
        return any(
            _contains_forbidden_identifier(key)
            or _contains_forbidden_identifier(item)
            for key, item in value.items()
        )
    return False


def _valid_execution_id(value):
    if type(value) is not str or _UUID4_RE.fullmatch(value) is None:
        return False
    try:
        parsed = uuid.UUID(value)
    except (ValueError, AttributeError):
        return False
    return parsed.version == 4 and parsed.variant == uuid.RFC_4122


def _validate_identity(request):
    identity_fields = (
        request["provider"],
        request["logical_model_id"],
        request["provider_model_id"],
        request["configuration_id"],
    )
    if any(type(value) is not str or not value for value in identity_fields):
        raise ValueError("provider identity fields must be non-empty strings")
    try:
        manifest.frozen_identity_profile(identity_fields)
    except ValueError:
        raise ValueError("provider identity tuple is not in the frozen panel")


def _without_request_hash(request):
    return {
        key: value
        for key, value in request.items()
        if key != "request_sha256"
    }


def validate_stage_request(request):
    """Validate and return a detached StageRequest object.

    Recomputing a hash cannot make a poisoned structural, identity, history, or
    schema field valid: every semantic invariant is checked independently.
    """
    canonical_json_bytes(request)
    _assert_no_forbidden_content(request)

    if type(request) is not dict or set(request) != STAGE_REQUEST_KEYS:
        raise ValueError("stage request must use exact top-level keys")
    if request["contract_version"] != CONTRACT_VERSION:
        raise ValueError("stage request contract version mismatch")
    if not _valid_execution_id(request["execution_id"]):
        raise ValueError("execution_id must be a lowercase RFC-4122 UUIDv4")

    _validate_identity(request)

    stage = request["stage"]
    if type(stage) is not str or stage not in STAGES:
        raise ValueError("stage must be one of stage_1 through stage_4")
    stage_index = STAGES.index(stage)

    prior = request["prior_visible_turns"]
    if type(prior) is not list or len(prior) != stage_index:
        raise ValueError("prior visible history has the wrong stage count")
    for index, turn in enumerate(prior):
        if type(turn) is not dict or set(turn) != PRIOR_TURN_KEYS:
            raise ValueError("prior visible history turn keys are not exact")
        if turn["stage"] != STAGES[index]:
            raise ValueError("prior visible history is not contiguous and ordered")
        if type(turn["prompt"]) is not str or type(turn["response"]) is not str:
            raise ValueError("prior visible history text must be strings")

    current = request["current_visible_turn"]
    if type(current) is not dict or set(current) != CURRENT_TURN_KEYS:
        raise ValueError("current visible turn keys are not exact")
    if current["stage"] != stage:
        raise ValueError("current visible turn stage mismatch")
    if type(current["content"]) is not str:
        raise ValueError("current visible content must be a string")

    schema = request["response_schema"]
    loaded_schema = manifest.load_response_schema()
    frozen_schema = manifest.EXPECTED_RESPONSE_SCHEMA
    if (
        type(schema) is not dict
        or canonical_json_bytes(loaded_schema) != canonical_json_bytes(frozen_schema)
        or canonical_json_bytes(schema) != canonical_json_bytes(frozen_schema)
    ):
        raise ValueError("response schema does not match the frozen schema")
    schema_hash = request["response_schema_sha256"]
    if (
        type(schema_hash) is not str
        or _SHA256_RE.fullmatch(schema_hash) is None
        or schema_hash != canonical_sha256(schema)
    ):
        raise ValueError("response schema hash mismatch")

    request_hash = request["request_sha256"]
    if (
        type(request_hash) is not str
        or _SHA256_RE.fullmatch(request_hash) is None
        or request_hash != canonical_sha256(_without_request_hash(request))
    ):
        raise ValueError("request hash mismatch")
    return deepcopy(request)


def build_stage_request(
        episode,
        *,
        execution_id,
        provider,
        logical_model_id,
        provider_model_id,
        configuration_id,
        stage,
        prior_responses):
    """Build a StageRequest by projecting only visible turns from an episode."""
    if type(stage) is not str or stage not in STAGES:
        raise ValueError("stage must be one of stage_1 through stage_4")
    try:
        turns = model_turns(episode)
    except (TypeError, ValueError):
        raise ValueError(
            "episode must expose exactly four model-visible text turns"
        ) from None
    by_stage = {turn["stage"]: turn["content"] for turn in turns}
    stage_index = STAGES.index(stage)
    expected_prior = STAGES[:stage_index]
    if type(prior_responses) is not dict or (
            len(prior_responses) != len(expected_prior)
            or set(prior_responses) != set(expected_prior)):
        raise ValueError("prior responses must exactly cover preceding stages")
    if any(type(prior_responses[key]) is not str for key in expected_prior):
        raise ValueError("prior responses must be strings")
    for prior_stage in expected_prior:
        response = prior_responses[prior_stage]
        prior_index = STAGES.index(prior_stage)
        for future_stage in STAGES[prior_index + 1:]:
            future_text = by_stage[future_stage]
            if future_text in response or sha256_utf8(future_text) in response:
                raise ValueError(
                    "prior response contains future-stage text or hash"
                )

    schema = deepcopy(manifest.load_response_schema())
    request = {
        "contract_version": CONTRACT_VERSION,
        "execution_id": execution_id,
        "provider": provider,
        "logical_model_id": logical_model_id,
        "provider_model_id": provider_model_id,
        "configuration_id": configuration_id,
        "stage": stage,
        "prior_visible_turns": [
            {
                "stage": prior_stage,
                "prompt": by_stage[prior_stage],
                "response": prior_responses[prior_stage],
            }
            for prior_stage in expected_prior
        ],
        "current_visible_turn": {
            "stage": stage,
            "content": by_stage[stage],
        },
        "response_schema": schema,
        "response_schema_sha256": canonical_sha256(schema),
    }
    request["request_sha256"] = canonical_sha256(request)
    return validate_stage_request(request)


def dumps_stage_request(request):
    """Validate and serialize a StageRequest as canonical JSON text."""
    return canonical_json_bytes(validate_stage_request(request)).decode("utf-8")


def loads_stage_request(payload):
    """Parse unique-key strict JSON and validate it as a StageRequest."""
    return validate_stage_request(_loads_unique(payload))


def sha256_utf8(value):
    """Hash exact UTF-8 text without whitespace or newline normalization."""
    if type(value) is not str:
        raise ValueError("raw value must be text for exact UTF-8 hashing")
    try:
        encoded = value.encode("utf-8", errors="strict")
    except UnicodeError:
        raise ValueError("raw value must be valid UTF-8 text") from None
    return hashlib.sha256(encoded).hexdigest()


def _nullable_nonempty_text(value, path):
    if value is not None and (type(value) is not str or not value):
        raise ValueError(f"{path} must be null or a non-empty string")
    return value


def _nullable_integer(value, path, *, lower=None, upper=None):
    if value is None:
        return value
    if type(value) is not int:
        raise ValueError(f"{path} must be null or an integer")
    if lower is not None and value < lower:
        raise ValueError(f"{path} is below its declared bound")
    if upper is not None and value > upper:
        raise ValueError(f"{path} is above its declared bound")
    return value


def _timestamp(value, path):
    if type(value) is not str or _RFC3339_RE.fullmatch(value) is None:
        raise ValueError(f"{path} must be RFC3339 UTC at whole-second precision")
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError:
        raise ValueError(f"{path} must be valid RFC3339 UTC") from None


def _validate_usage(usage):
    if type(usage) is not dict or set(usage) != USAGE_KEYS:
        raise ValueError("attempt usage must use exact token-count keys")
    for key, value in usage.items():
        _nullable_integer(value, f"usage.{key}", lower=0)
    return usage


def _expected_attempt_projection(attempt):
    raw = attempt["raw_final_message"]
    if raw is None:
        parsed = None
    else:
        parsed = action_scale.parse_canonical_response(raw)
    return {
        "raw_trace_sha256": sha256_utf8(attempt["raw_trace"]),
        "raw_final_message_sha256": (
            sha256_utf8(raw) if raw is not None else None
        ),
        "parsed_response": parsed,
        "parsed_response_sha256": (
            canonical_sha256(parsed) if parsed is not None else None
        ),
        "parse_mode": (
            action_scale.CANONICAL_JSON_V1 if parsed is not None
            else "unresolved"
        ),
        "reasoning_details_sha256": (
            canonical_sha256(attempt["reasoning_details"])
            if attempt["reasoning_details"] is not None else None
        ),
    }


def _is_zero_byte_pre_response_transport_attempt(attempt):
    """Recognize exact evidence that no provider response bytes were received."""
    return (
        attempt["raw_trace"] == ""
        and attempt["error_code"] == "transport_error"
        and attempt["provider_request_id"] is None
        and attempt["token_emission_started"] is False
        and attempt["exit_status"] is None
        and attempt["http_status"] is None
        and attempt["finish_reason"] is None
        and all(value is None for value in attempt["usage"].values())
        and attempt["raw_final_message"] is None
        and attempt["reasoning_details"] is None
    )


def validate_stage_attempt(attempt):
    """Validate one immutable raw transport attempt and all derived hashes."""
    canonical_json_bytes(attempt)
    if type(attempt) is not dict or set(attempt) != STAGE_ATTEMPT_KEYS:
        raise ValueError("stage attempt must use exact keys")
    _assert_no_credential_material(attempt["raw_trace"])
    _assert_no_credential_material(attempt["raw_final_message"])
    _assert_no_credential_material(attempt["reasoning_details"])
    if type(attempt["attempt_index"]) is not int or not 1 <= attempt[
            "attempt_index"] <= 3:
        raise ValueError("attempt_index must be an integer from 1 through 3")
    started = _timestamp(attempt["started_at_utc"], "started_at_utc")
    completed = _timestamp(attempt["completed_at_utc"], "completed_at_utc")
    if completed < started:
        raise ValueError("attempt completion precedes its start")
    _nullable_nonempty_text(attempt["provider_request_id"], "provider_request_id")
    if type(attempt["token_emission_started"]) is not bool:
        raise ValueError("token_emission_started must be a boolean")
    _nullable_integer(attempt["exit_status"], "exit_status")
    _nullable_integer(attempt["http_status"], "http_status", lower=100, upper=599)
    _nullable_nonempty_text(attempt["finish_reason"], "finish_reason")
    _validate_usage(attempt["usage"])
    if type(attempt["raw_trace"]) is not str:
        raise ValueError("raw_trace must be exact text")
    if attempt["raw_final_message"] is not None and type(
            attempt["raw_final_message"]) is not str:
        raise ValueError("raw_final_message must be null or exact text")
    if attempt["raw_final_message"] is not None and not attempt[
            "token_emission_started"]:
        raise ValueError("a raw response requires token emission")
    if attempt["reasoning_effort"] != "medium":
        raise ValueError("reasoning_effort must be exactly medium")
    if attempt["reasoning_details"] is not None:
        _assert_json_domain(attempt["reasoning_details"])
    _nullable_nonempty_text(attempt["error_code"], "error_code")
    if not attempt["raw_trace"] and not (
            _is_zero_byte_pre_response_transport_attempt(attempt)):
        raise ValueError(
            "empty raw_trace is reserved for exact pre-response transport "
            "failure evidence"
        )

    expected = _expected_attempt_projection(attempt)
    for field, value in expected.items():
        if attempt[field] != value:
            raise ValueError(
                f"attempt {field} hash/parsed value disagrees with raw evidence"
            )
    return deepcopy(attempt)


def build_stage_attempt(
        *, attempt_index, started_at_utc, completed_at_utc,
        provider_request_id, token_emission_started, exit_status, http_status,
        finish_reason, usage, raw_trace, raw_final_message, reasoning_effort,
        reasoning_details, error_code):
    """Build one detached attempt, deriving parse state and every raw hash."""
    attempt = {
        "attempt_index": attempt_index,
        "started_at_utc": started_at_utc,
        "completed_at_utc": completed_at_utc,
        "provider_request_id": provider_request_id,
        "token_emission_started": token_emission_started,
        "exit_status": exit_status,
        "http_status": http_status,
        "finish_reason": finish_reason,
        "usage": deepcopy(usage),
        "raw_trace": raw_trace,
        "raw_trace_sha256": sha256_utf8(raw_trace),
        "raw_final_message": raw_final_message,
        "raw_final_message_sha256": (
            sha256_utf8(raw_final_message)
            if raw_final_message is not None else None
        ),
        "parsed_response": (
            action_scale.parse_canonical_response(raw_final_message)
            if raw_final_message is not None else None
        ),
        "parsed_response_sha256": None,
        "parse_mode": "unresolved",
        "reasoning_effort": reasoning_effort,
        "reasoning_details": deepcopy(reasoning_details),
        "reasoning_details_sha256": (
            canonical_sha256(reasoning_details)
            if reasoning_details is not None else None
        ),
        "error_code": error_code,
    }
    if attempt["parsed_response"] is not None:
        attempt["parsed_response_sha256"] = canonical_sha256(
            attempt["parsed_response"]
        )
        attempt["parse_mode"] = action_scale.CANONICAL_JSON_V1
    return validate_stage_attempt(attempt)


def _validate_attempt_sequence(attempts):
    if type(attempts) is not list or not 1 <= len(attempts) <= 3:
        raise ValueError("result requires one through three transport attempts")
    validated = [validate_stage_attempt(row) for row in attempts]
    previous_completed = None
    for index, attempt in enumerate(validated, 1):
        if attempt["attempt_index"] != index:
            raise ValueError("attempt indexes must be contiguous from one")
        started = _timestamp(attempt["started_at_utc"], "started_at_utc")
        completed = _timestamp(attempt["completed_at_utc"], "completed_at_utc")
        if previous_completed is not None and started < previous_completed:
            raise ValueError("transport attempts overlap or reverse time")
        previous_completed = completed
        if index < len(validated):
            if (
                attempt["token_emission_started"]
                or attempt["raw_final_message"] is not None
                or attempt["parsed_response"] is not None
            ):
                raise ValueError(
                    "transport retry is forbidden after any token or response"
                )
            if attempt["error_code"] is None:
                raise ValueError("transport retry requires an explicit error")
    return validated


def _run_mode_provenance(run_mode, identity):
    if run_mode not in RUN_PROVENANCE:
        raise ValueError(
            "run_mode must be mock, codex, openrouter, or openrouter_probe"
        )
    profile_id = manifest.frozen_identity_profile(identity)
    provider = identity[0]
    if run_mode == "mock":
        return RUN_PROVENANCE[run_mode]
    if run_mode == "codex":
        if provider != "codex" or profile_id != manifest.FLAGSHIP_PROFILE_ID:
            raise ValueError("live Codex run_mode requires a flagship Codex identity")
        return RUN_PROVENANCE[run_mode]
    if run_mode == "openrouter":
        if provider != "openrouter":
            raise ValueError("live OpenRouter run_mode requires an OpenRouter identity")
        if profile_id == manifest.FLAGSHIP_PROFILE_ID:
            return RUN_PROVENANCE[run_mode]
        if profile_id in manifest.QUALIFICATION_PROFILE_IDS:
            return CHEAP_OPENROUTER_PROVENANCE
    if (
        run_mode == "openrouter_probe"
        and provider == "openrouter"
        and profile_id in manifest.QUALIFICATION_PROFILE_IDS
    ):
        return RUN_PROVENANCE[run_mode]
    raise ValueError(
        "openrouter_probe requires an exact cheap OpenRouter identity profile"
    )


def _session_shape_ok(provider, session_id):
    if provider == "codex":
        return type(session_id) is str and bool(session_id)
    return session_id is None


def _expected_integrity(
        result, *, session_chain_evidence, isolation_evidence,
        future_text_evidence):
    attempts = result["attempts"]
    final = attempts[-1]
    identity = (
        result["provider"], result["logical_model_id"],
        result["requested_provider_model_id"], result["configuration_id"],
    )
    provider_identity_ok = (
        result["returned_provider_model_id"]
        in manifest.expected_returned_provider_model_ids(identity)
        and result["returned_provider_name"]
        == manifest.expected_returned_provider(identity)
    )
    session_chain_ok = (
        session_chain_evidence
        and _session_shape_ok(result["provider"], result["session_id"])
    )
    isolation_ok = isolation_evidence
    future_text_absent = future_text_evidence
    tools_absent = not result["tool_events"]
    trace_complete = all(
        type(attempt["raw_trace"]) is str
        and (
            bool(attempt["raw_trace"])
            or _is_zero_byte_pre_response_transport_attempt(attempt)
        )
        for attempt in attempts
    )
    identifier_echo_absent = not any(
        _contains_forbidden_identifier(attempt[field])
        for attempt in attempts
        for field in (
            "raw_trace", "raw_final_message", "reasoning_details"
        )
    ) and not _contains_forbidden_identifier(result["tool_events"])
    transport_successful = (
        final["error_code"] is None
        and final["exit_status"] in (None, 0)
        and final["http_status"] in (None, 200)
    )
    mechanically_resolved = final["parsed_response"] is not None
    checks = (
        (provider_identity_ok, "provider_identity"),
        (session_chain_ok, "session_chain"),
        (isolation_ok, "isolation"),
        (future_text_absent, "future_text"),
        (tools_absent, "tool_event"),
        (trace_complete, "trace_incomplete"),
        (identifier_echo_absent, "forbidden_identifier_echo"),
        (transport_successful, "transport_error"),
    )
    violations = [name for passed, name in checks if not passed]
    integrity_valid = not violations
    measurement_ready = (
        result["run_mode"] not in {"mock", "openrouter_probe"}
        and integrity_valid
        and mechanically_resolved
    )
    return {
        "provider_identity_ok": provider_identity_ok,
        "session_chain_ok": session_chain_ok,
        "isolation_ok": isolation_ok,
        "future_text_absent": future_text_absent,
        "tools_absent": tools_absent,
        "trace_complete": trace_complete,
        "identifier_echo_absent": identifier_echo_absent,
        "transport_successful": transport_successful,
        "mechanically_resolved": mechanically_resolved,
        "violations": violations,
        "integrity_valid": integrity_valid,
        "measurement_ready": measurement_ready,
    }


def _expected_terminal(result, integrity):
    final = result["attempts"][-1]
    if (
        final["raw_final_message"] is None
        and (
            set(integrity["violations"]) == {"transport_error"}
            or
            final["error_code"] == "transport_error"
            or (
                type(final["error_code"]) is str
                and final["error_code"].startswith("http_")
            )
        )
    ):
        return "failed"
    if not integrity["integrity_valid"]:
        return "invalidated"
    if final["parsed_response"] is not None:
        return "complete"
    if final["raw_final_message"] is not None:
        return "unresolved"
    return "failed"


def _without_result_hash(result):
    return {
        key: value for key, value in result.items()
        if key != "result_sha256"
    }


def validate_stage_result(result, request):
    """Validate one provider-neutral result against its exact StageRequest."""
    canonical_json_bytes(result)
    request = validate_stage_request(request)
    if type(result) is not dict or set(result) != STAGE_RESULT_KEYS:
        raise ValueError("stage result must use exact top-level keys")
    if result["contract_version"] != RESULT_CONTRACT_VERSION:
        raise ValueError("stage result contract version mismatch")
    result_identity = (
        result["provider"], result["logical_model_id"],
        result["requested_provider_model_id"], result["configuration_id"],
    )
    provenance = _run_mode_provenance(result["run_mode"], result_identity)
    if result["provenance"] != provenance:
        raise ValueError("result provenance does not match run_mode")
    bound = {
        "execution_id": request["execution_id"],
        "provider": request["provider"],
        "logical_model_id": request["logical_model_id"],
        "requested_provider_model_id": request["provider_model_id"],
        "configuration_id": request["configuration_id"],
        "stage": request["stage"],
        "request_sha256": request["request_sha256"],
        "response_schema_sha256": request["response_schema_sha256"],
    }
    for field, expected in bound.items():
        if result[field] != expected:
            raise ValueError(f"result {field} does not match its request")
    for field in ("returned_provider_model_id", "returned_provider_name"):
        if type(result[field]) is not str or not result[field]:
            raise ValueError(f"result {field} must be a non-empty string")
    if result["session_id"] is not None and (
            type(result["session_id"]) is not str or not result["session_id"]):
        raise ValueError("session_id must be null or a non-empty string")
    if type(result["transport_request_sha256"]) is not str or _SHA256_RE.fullmatch(
            result["transport_request_sha256"]) is None:
        raise ValueError("transport request hash must be a SHA-256 digest")
    attempts = _validate_attempt_sequence(result["attempts"])
    if type(result["transport_retry_count"]) is not int or result[
            "transport_retry_count"] != len(attempts) - 1:
        raise ValueError("transport retry count disagrees with attempts")
    if type(result["tool_events"]) is not list:
        raise ValueError("tool_events must be a list")
    _assert_json_domain(result["tool_events"])
    _assert_no_credential_material(result["tool_events"])
    if type(result["integrity"]) is not dict or set(result[
            "integrity"]) != INTEGRITY_KEYS:
        raise ValueError("result integrity must use exact keys")
    integrity = result["integrity"]
    for field in (
            "provider_identity_ok", "session_chain_ok", "isolation_ok",
            "future_text_absent", "tools_absent", "trace_complete",
            "identifier_echo_absent", "transport_successful",
            "mechanically_resolved",
            "integrity_valid", "measurement_ready"):
        if type(integrity[field]) is not bool:
            raise ValueError(f"integrity.{field} must be a boolean")
    if type(integrity["violations"]) is not list or any(
            type(value) is not str for value in integrity["violations"]):
        raise ValueError("integrity violations must be a string list")

    detached = deepcopy(result)
    detached["attempts"] = attempts
    expected_integrity = _expected_integrity(
        detached,
        session_chain_evidence=integrity["session_chain_ok"],
        isolation_evidence=integrity["isolation_ok"],
        future_text_evidence=integrity["future_text_absent"],
    )
    if integrity != expected_integrity:
        raise ValueError("result integrity claims disagree with evidence")
    expected_terminal = _expected_terminal(detached, expected_integrity)
    if result["terminal_status"] not in TERMINAL_STATUSES or result[
            "terminal_status"] != expected_terminal:
        raise ValueError("result terminal status disagrees with evidence")
    if type(result["result_sha256"]) is not str or result[
            "result_sha256"] != canonical_sha256(_without_result_hash(result)):
        raise ValueError("result hash mismatch")
    return detached


def build_stage_result(
        request, *, run_mode, returned_provider_model_id,
        returned_provider_name, session_id, transport_request_sha256,
        attempts, tool_events, session_chain_ok, isolation_ok,
        future_text_absent):
    """Build a detached result and derive integrity/terminal fields."""
    request = validate_stage_request(request)
    if any(type(value) is not bool for value in (
            session_chain_ok, isolation_ok, future_text_absent)):
        raise ValueError("integrity evidence must use exact booleans")
    validated_attempts = _validate_attempt_sequence(deepcopy(attempts))
    request_identity = tuple(request[key] for key in (
        "provider", "logical_model_id", "provider_model_id",
        "configuration_id",
    ))
    provenance = _run_mode_provenance(run_mode, request_identity)
    result = {
        "contract_version": RESULT_CONTRACT_VERSION,
        "provenance": provenance,
        "run_mode": run_mode,
        "execution_id": request["execution_id"],
        "provider": request["provider"],
        "logical_model_id": request["logical_model_id"],
        "requested_provider_model_id": request["provider_model_id"],
        "returned_provider_model_id": returned_provider_model_id,
        "returned_provider_name": returned_provider_name,
        "configuration_id": request["configuration_id"],
        "stage": request["stage"],
        "request_sha256": request["request_sha256"],
        "transport_request_sha256": transport_request_sha256,
        "response_schema_sha256": request["response_schema_sha256"],
        "session_id": session_id,
        "transport_retry_count": len(validated_attempts) - 1,
        "attempts": validated_attempts,
        "tool_events": deepcopy(tool_events),
        "terminal_status": None,
        "integrity": None,
    }
    if type(tool_events) is not list:
        raise ValueError("tool_events must be a list")
    _assert_json_domain(tool_events)
    integrity = _expected_integrity(
        result,
        session_chain_evidence=session_chain_ok,
        isolation_evidence=isolation_ok,
        future_text_evidence=future_text_absent,
    )
    result["integrity"] = integrity
    result["terminal_status"] = _expected_terminal(result, integrity)
    result["result_sha256"] = canonical_sha256(result)
    return validate_stage_result(result, request)


def dumps_stage_result(result, request):
    """Validate and serialize one StageResult as canonical JSON text."""
    return canonical_json_bytes(validate_stage_result(
        result, request
    )).decode("utf-8")


def loads_stage_result(payload, request):
    """Parse unique-key strict JSON and validate one StageResult."""
    return validate_stage_result(_loads_unique(payload), request)


def _contains_future_stage_material(value, future_turns):
    if value is None:
        return False
    texts = []
    if type(value) is str:
        texts.append(value)
    elif type(value) is list:
        for item in value:
            if _contains_future_stage_material(item, future_turns):
                return True
    elif type(value) is dict:
        for item in value.values():
            if _contains_future_stage_material(item, future_turns):
                return True
    for source in texts:
        for turn in future_turns:
            content = turn["content"]
            if content in source or sha256_utf8(content) in source:
                return True
    return False


def _build_stage_chain_payload(requests, results, episode):
    if type(requests) is not list or type(results) is not list or (
            len(requests) != 4 or len(results) != 4):
        raise ValueError("complete stage chain requires exactly four requests/results")
    try:
        visible_turns = model_turns(episode)
    except (TypeError, ValueError):
        raise ValueError("chain episode must expose four visible turns") from None

    validated_requests = []
    validated_results = []
    base_identity = None
    previous_completed = None
    for index, stage in enumerate(STAGES):
        request = validate_stage_request(requests[index])
        if request["stage"] != stage or request["current_visible_turn"] != {
                "stage": stage, "content": visible_turns[index]["content"]}:
            raise ValueError("chain request stage/current prompt differs from episode")
        identity = (
            request["execution_id"], request["provider"],
            request["logical_model_id"], request["provider_model_id"],
            request["configuration_id"], request["response_schema_sha256"],
        )
        if base_identity is None:
            base_identity = identity
        elif identity != base_identity:
            raise ValueError("chain execution/request identity changed across stages")

        # Recompute future exposure from raw evidence before trusting the
        # driver's recorded boolean or advancing to the next request.
        candidate = results[index]
        if type(candidate) is dict and type(candidate.get("attempts")) is list:
            future = visible_turns[index + 1:]
            for attempt in candidate["attempts"]:
                if type(attempt) is dict and (
                    _contains_future_stage_material(
                        attempt.get("raw_trace"), future
                    )
                    or _contains_future_stage_material(
                        attempt.get("raw_final_message"), future
                    )
                    or _contains_future_stage_material(
                        attempt.get("reasoning_details"), future
                    )
                ):
                    raise ValueError("chain raw evidence contains future-stage material")

        expected_prior = []
        for prior_index in range(index):
            prior_final = validated_results[prior_index]["attempts"][-1][
                "raw_final_message"
            ]
            if prior_final is None:
                raise ValueError("chain history cannot advance without a response")
            expected_prior.append({
                "stage": STAGES[prior_index],
                "prompt": validated_requests[prior_index][
                    "current_visible_turn"
                ]["content"],
                "response": prior_final,
            })
        if request["prior_visible_turns"] != expected_prior:
            raise ValueError("chain visible history prompt/response mismatch")

        result = validate_stage_result(candidate, request)
        if not result["integrity"]["integrity_valid"] or result[
                "terminal_status"] == "invalidated":
            raise ValueError("complete chain contains an integrity-invalidated stage")
        if result["terminal_status"] == "failed":
            raise ValueError("complete chain contains a failed stage without response")

        first_started = _timestamp(
            result["attempts"][0]["started_at_utc"], "started_at_utc"
        )
        last_completed = _timestamp(
            result["attempts"][-1]["completed_at_utc"], "completed_at_utc"
        )
        if previous_completed is not None and first_started < previous_completed:
            raise ValueError("chain stages overlap or reverse chronological order")
        previous_completed = last_completed
        validated_requests.append(request)
        validated_results.append(result)

    provider = base_identity[1]
    run_modes = {result["run_mode"] for result in validated_results}
    provenances = {result["provenance"] for result in validated_results}
    if len(run_modes) != 1 or len(provenances) != 1:
        raise ValueError("chain run_mode/provenance changed across stages")
    run_mode = next(iter(run_modes))
    sessions = [result["session_id"] for result in validated_results]
    if provider == "codex":
        if any(type(value) is not str or not value for value in sessions) or len(
                set(sessions)) != 1:
            raise ValueError("Codex chain requires one identical thread/session")
        session_id = sessions[0]
    else:
        if any(value is not None for value in sessions):
            raise ValueError("OpenRouter chain must not invent a session")
        session_id = None
    payload = {
        "contract_version": CHAIN_CONTRACT_VERSION,
        "provenance": next(iter(provenances)),
        "run_mode": run_mode,
        "execution_id": base_identity[0],
        "provider": provider,
        "logical_model_id": base_identity[2],
        "provider_model_id": base_identity[3],
        "configuration_id": base_identity[4],
        "response_schema_sha256": base_identity[5],
        "stage_count": 4,
        "request_sha256s": [
            request["request_sha256"] for request in validated_requests
        ],
        "result_sha256s": [
            result["result_sha256"] for result in validated_results
        ],
        "session_id": session_id,
        "measurement_ready": all(
            result["integrity"]["measurement_ready"]
            for result in validated_results
        ),
    }
    return payload


def build_stage_chain(requests, results, episode):
    """Build a hash-bound complete four-stage conversation record."""
    chain = _build_stage_chain_payload(requests, results, episode)
    chain["chain_sha256"] = canonical_sha256(chain)
    return validate_stage_chain(chain, requests, results, episode)


def validate_stage_chain(chain, requests, results, episode):
    """Recompute a complete conversation from requests and raw results."""
    canonical_json_bytes(chain)
    if type(chain) is not dict or set(chain) != STAGE_CHAIN_KEYS:
        raise ValueError("stage chain must use exact keys")
    expected = _build_stage_chain_payload(requests, results, episode)
    if any(chain.get(key) != value for key, value in expected.items()):
        raise ValueError("stage chain fields disagree with request/result history")
    if type(chain["chain_sha256"]) is not str or chain[
            "chain_sha256"] != canonical_sha256(expected):
        raise ValueError("stage chain hash mismatch")
    return deepcopy(chain)


def validate_integrity_rerun(
        previous_requests, previous_results, new_requests):
    """Authorize one new execution only after a recorded integrity failure.

    Parse/schema failure is an unresolved measurement outcome, not an integrity
    failure, so it can never satisfy this authorization contract.
    """
    if (
        type(previous_requests) is not list
        or type(previous_results) is not list
        or not previous_requests
        or len(previous_requests) != len(previous_results)
        or type(new_requests) is not list
        or len(new_requests) != 1
    ):
        raise ValueError("integrity rerun requires paired previous and new requests")
    prior_pairs = [
        (
            validate_stage_request(request),
            validate_stage_result(result, request),
        )
        for request, result in zip(previous_requests, previous_results)
    ]
    previous_ids = {request["execution_id"] for request, _ in prior_pairs}
    if len(previous_ids) != 1:
        raise ValueError("previous integrity attempt has mixed execution IDs")
    if len(prior_pairs) > len(STAGES):
        raise ValueError("previous integrity attempt exceeds the stage contract")
    prior_identity = None
    expected_history = []
    for index, (request, result) in enumerate(prior_pairs):
        if request["stage"] != STAGES[index]:
            raise ValueError(
                "previous integrity attempt must be a contiguous stage prefix"
            )
        identity = tuple(request[key] for key in (
            "provider", "logical_model_id", "provider_model_id",
            "configuration_id",
        ))
        if prior_identity is None:
            prior_identity = identity
        elif identity != prior_identity:
            raise ValueError(
                "previous integrity attempt changed frozen model identity"
            )
        if request["prior_visible_turns"] != expected_history:
            raise ValueError(
                "previous integrity attempt has non-contiguous visible history"
            )
        if index < len(prior_pairs) - 1:
            if (
                not result["integrity"]["integrity_valid"]
                or result["terminal_status"] in {"invalidated", "failed"}
            ):
                raise ValueError(
                    "previous integrity attempt advanced after a terminal stage"
                )
            raw_response = result["attempts"][-1]["raw_final_message"]
            if raw_response is None:
                raise ValueError(
                    "previous integrity attempt advanced without a response"
                )
            expected_history.append({
                "stage": request["stage"],
                "prompt": request["current_visible_turn"]["content"],
                "response": raw_response,
            })
    final_result = prior_pairs[-1][1]
    if not (
            final_result["terminal_status"] == "invalidated"
            and not final_result["integrity"]["integrity_valid"]):
        raise ValueError(
            "unresolved parse/schema failure does not authorize integrity rerun"
        )
    violations = set(final_result["integrity"]["violations"])
    final_attempt = final_result["attempts"][-1]
    if (
        not violations
        or not violations <= INTEGRITY_RERUN_ALLOWED_VIOLATIONS
        or "transport_error" in violations
        or final_attempt["error_code"] is not None
        or final_attempt["exit_status"] not in (None, 0)
        or final_attempt["http_status"] not in (None, 200)
    ):
        raise ValueError(
            "transport/protocol failure does not authorize integrity rerun"
        )

    validated_new = [validate_stage_request(request) for request in new_requests]
    if validated_new[0]["stage"] != "stage_1":
        raise ValueError("integrity rerun must restart at stage_1")
    new_ids = {request["execution_id"] for request in validated_new}
    if len(new_ids) != 1:
        raise ValueError("integrity rerun requests have mixed execution IDs")
    previous_id = next(iter(previous_ids))
    new_id = next(iter(new_ids))
    if new_id == previous_id:
        raise ValueError("integrity rerun requires a fresh execution UUID")
    old_identity = prior_identity
    for request in validated_new:
        identity = tuple(request[key] for key in (
            "provider", "logical_model_id", "provider_model_id",
            "configuration_id",
        ))
        if identity != old_identity:
            raise ValueError("integrity rerun changed the frozen model identity")
    original_stage_one = prior_pairs[0][0]
    restarted_stage_one = validated_new[0]
    for field in (
            "contract_version", "stage", "prior_visible_turns",
            "current_visible_turn", "response_schema",
            "response_schema_sha256"):
        if restarted_stage_one[field] != original_stage_one[field]:
            raise ValueError(
                "integrity rerun changed the original episode-visible prompt"
            )
    return {
        "authorized": True,
        "previous_execution_id": previous_id,
        "new_execution_id": new_id,
    }
