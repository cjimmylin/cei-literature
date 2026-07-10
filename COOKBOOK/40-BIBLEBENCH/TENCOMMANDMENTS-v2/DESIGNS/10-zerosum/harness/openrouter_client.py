"""Isolated, fail-closed OpenRouter transport for ZEROSUM P1.

The adapter deliberately implements only the small ``ModelClient`` seam used by
the local harness.  It does not change the benchmark's human-calibration or
multi-vendor live-run preconditions.
"""

from __future__ import annotations

from copy import deepcopy
import json
import math
import os
import time
from types import MappingProxyType
from typing import Any, Callable, Dict, Mapping, Optional, Sequence, Tuple
import urllib.error
import urllib.request


CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"
MODELS_URL = "https://openrouter.ai/api/v1/models"
ENV_KEY = "OPENROUTER_API_KEY"

REQUESTED_MODEL_ROSTER: Tuple[Mapping[str, str], ...] = (
    {
        "model_id": "openai/gpt-5.5",
        "family": "gpt-5.5",
        "vendor": "openai",
    },
    {
        "model_id": "openai/gpt-5.4",
        "family": "gpt-5.4",
        "vendor": "openai",
    },
    {
        "model_id": "openai/gpt-5.4-mini",
        "family": "gpt-5.4-mini",
        "vendor": "openai",
    },
)
REQUESTED_MODEL_IDS: Tuple[str, ...] = tuple(
    row["model_id"] for row in REQUESTED_MODEL_ROSTER
)
FROZEN_CANONICAL_MODEL_IDS: Mapping[str, str] = MappingProxyType({
    "openai/gpt-5.5": "openai/gpt-5.5-20260423",
    "openai/gpt-5.4": "openai/gpt-5.4-20260305",
    "openai/gpt-5.4-mini": "openai/gpt-5.4-mini-20260317",
})
_ROSTER_BY_ID = {row["model_id"]: dict(row) for row in REQUESTED_MODEL_ROSTER}

_MAX_TOKEN_LIMIT = 16_384
_MAX_ATTEMPTS_LIMIT = 5
_MAX_SEED = 2**31 - 1
_REQUIRED_CATALOG_PARAMETERS = frozenset(
    {"reasoning_effort", "max_tokens", "response_format", "seed"}
)
_ALLOWED_ROLES = frozenset({"assistant", "developer", "system", "user"})
_TOKEN_USAGE_KEYS = frozenset(
    {
        "accepted_prediction_tokens",
        "audio_tokens",
        "cached_tokens",
        "completion_tokens",
        "image_tokens",
        "prompt_audio_tokens",
        "prompt_tokens",
        "reasoning_tokens",
        "rejected_prediction_tokens",
        "total_tokens",
    }
)
_COST_USAGE_KEYS = frozenset({"cost", "upstream_inference_cost"})
_DETAIL_USAGE_KEYS = frozenset(
    {"completion_tokens_details", "cost_details", "prompt_tokens_details"}
)
_SAFE_USAGE_KEYS = (
    _TOKEN_USAGE_KEYS
    | _COST_USAGE_KEYS
    | _DETAIL_USAGE_KEYS
    | frozenset({"is_byok"})
)


class OpenRouterError(RuntimeError):
    """Base class for sanitized adapter failures."""


class OpenRouterConfigurationError(OpenRouterError):
    """Raised when local adapter configuration is invalid."""


class OpenRouterRequestError(OpenRouterError):
    """Raised before transport when a canonical request is invalid."""


class OpenRouterTransportError(OpenRouterError):
    """Raised for a sanitized HTTP or network failure."""


class OpenRouterResponseError(OpenRouterError):
    """Raised when a completion response cannot be safely parsed."""


class OpenRouterCatalogError(OpenRouterError):
    """Raised when the requested model roster cannot be catalog-verified."""


def _resolve_api_key(api_key: Optional[str]) -> str:
    candidate = os.environ.get(ENV_KEY) if api_key is None else api_key
    if (
        not isinstance(candidate, str)
        or not candidate
        or candidate.strip() != candidate
        or any(ord(character) < 33 or ord(character) > 126 for character in candidate)
    ):
        raise OpenRouterConfigurationError(
            "%s must be a nonblank header-safe ASCII credential" % ENV_KEY
        )
    return candidate


def _bounded_integer(
    value: Any, label: str, *, minimum: int, maximum: int
) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise OpenRouterConfigurationError(
            "%s must be an integer in [%d, %d]" % (label, minimum, maximum)
        )
    return value


def _validated_timeout(value: Any) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or not 0 < float(value) <= 300
    ):
        raise OpenRouterConfigurationError("timeout must be in (0, 300] seconds")
    return float(value)


def _validated_retry_base(value: Any) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or not 0 <= float(value) <= 30
    ):
        raise OpenRouterConfigurationError(
            "retry_base_seconds must be in [0, 30]"
        )
    return float(value)


def _decode_json_body(body: Any, error_type: type, label: str) -> Mapping[str, Any]:
    if isinstance(body, bytes):
        try:
            text = body.decode("utf-8")
        except UnicodeDecodeError:
            raise error_type("%s was not valid UTF-8" % label) from None
    elif isinstance(body, str):
        text = body
    else:
        raise error_type("%s body was not bytes or text" % label)
    try:
        payload = json.loads(text)
    except (TypeError, ValueError):
        raise error_type("%s was not valid JSON" % label) from None
    if not isinstance(payload, Mapping):
        raise error_type("%s JSON root must be an object" % label)
    return payload


def _read_response(response: Any) -> Any:
    with response as handle:
        return handle.read()


def _canonical_messages(request: Mapping[str, Any]) -> Sequence[Dict[str, str]]:
    if not isinstance(request, Mapping):
        raise OpenRouterRequestError("canonical request must be an object")
    messages = request.get("messages")
    if not isinstance(messages, list) or not messages:
        raise OpenRouterRequestError("canonical request requires nonempty messages")
    canonical = []
    for message in messages:
        if not isinstance(message, Mapping) or set(message) != {"role", "content"}:
            raise OpenRouterRequestError(
                "each canonical message must contain only role and content"
            )
        role = message.get("role")
        content = message.get("content")
        if role not in _ALLOWED_ROLES:
            raise OpenRouterRequestError("canonical message role is invalid")
        if not isinstance(content, str) or not content.strip():
            raise OpenRouterRequestError("canonical message content must be nonblank text")
        canonical.append({"role": role, "content": content})
    return canonical


def _canonical_response_format(request: Mapping[str, Any]) -> Dict[str, str]:
    response_format = request.get("response_format", {"type": "text"})
    if (
        not isinstance(response_format, Mapping)
        or set(response_format) != {"type"}
        or response_format.get("type") != "text"
    ):
        raise OpenRouterRequestError(
            "canonical response_format must be exactly type=text"
        )
    return {"type": "text"}


def _safe_usage_value(field: str, value: Any) -> Any:
    if field in _DETAIL_USAGE_KEYS:
        if not isinstance(value, Mapping):
            raise OpenRouterResponseError(
                "usage %s must be an object" % field
            )
        return {
            key: _safe_usage_value(key, child)
            for key, child in value.items()
            if isinstance(key, str) and key in _SAFE_USAGE_KEYS
        }
    if field == "is_byok":
        if type(value) is not bool:
            raise OpenRouterResponseError("usage is_byok must be boolean")
        return value
    if field in _TOKEN_USAGE_KEYS:
        if type(value) is not int or value < 0:
            raise OpenRouterResponseError(
                "usage %s must be a nonnegative integer" % field
            )
        return value
    if field in _COST_USAGE_KEYS:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(float(value))
            or value < 0
        ):
            raise OpenRouterResponseError(
                "usage %s must be a nonnegative finite number" % field
            )
        return value
    raise OpenRouterResponseError("usage metadata contained an unsafe field")


def _safe_usage(payload: Mapping[str, Any]) -> Dict[str, Any]:
    if "usage" not in payload or payload["usage"] is None:
        return {}
    usage = payload["usage"]
    if not isinstance(usage, Mapping):
        raise OpenRouterResponseError("completion usage must be an object")
    return {
        key: _safe_usage_value(key, value)
        for key, value in usage.items()
        if isinstance(key, str) and key in _SAFE_USAGE_KEYS
    }


def _required_response_string(
    value: Any,
    label: str,
    *,
    secret: str,
) -> str:
    if not isinstance(value, str) or not value.strip():
        raise OpenRouterResponseError("completion %s must be nonblank text" % label)
    if secret in value:
        raise OpenRouterResponseError(
            "completion %s contained credential material" % label
        )
    return value


class OpenRouterClient:
    """Stdlib HTTPS client implementing the local ``ModelClient`` protocol."""

    def __init__(
        self,
        model_id: str,
        *,
        family: Optional[str] = None,
        vendor: str = "openai",
        api_key: Optional[str] = None,
        max_tokens: int = 4096,
        reasoning_effort: Optional[str] = None,
        timeout: float = 60.0,
        max_attempts: int = 3,
        retry_base_seconds: float = 0.5,
        opener: Optional[Callable[..., Any]] = None,
        sleeper: Optional[Callable[[float], Any]] = None,
    ) -> None:
        expected = _ROSTER_BY_ID.get(model_id)
        if expected is None:
            raise OpenRouterConfigurationError(
                "model_id is not in the frozen requested OpenRouter roster"
            )
        resolved_family = expected["family"] if family is None else family
        if resolved_family != expected["family"]:
            raise OpenRouterConfigurationError("model family does not match model_id")
        if vendor != expected["vendor"]:
            raise OpenRouterConfigurationError("model vendor does not match model_id")
        self.model_id = model_id
        self.family = resolved_family
        self.vendor = vendor
        self.max_tokens = _bounded_integer(
            max_tokens, "max_tokens", minimum=1, maximum=_MAX_TOKEN_LIMIT
        )
        if reasoning_effort is not None and reasoning_effort != "minimal":
            raise OpenRouterConfigurationError(
                "reasoning_effort must be omitted or exactly minimal"
            )
        self.reasoning_effort = reasoning_effort
        self.timeout = _validated_timeout(timeout)
        self.max_attempts = _bounded_integer(
            max_attempts, "max_attempts", minimum=1, maximum=_MAX_ATTEMPTS_LIMIT
        )
        self.retry_base_seconds = _validated_retry_base(retry_base_seconds)
        self._api_key = _resolve_api_key(api_key)
        self._opener = urllib.request.urlopen if opener is None else opener
        self._sleeper = time.sleep if sleeper is None else sleeper
        if not callable(self._opener):
            raise OpenRouterConfigurationError("opener must be callable")
        if not callable(self._sleeper):
            raise OpenRouterConfigurationError("sleeper must be callable")
        self._last_call_metadata: Optional[Dict[str, Any]] = None

    def __repr__(self) -> str:
        return (
            "OpenRouterClient(model_id=%r, family=%r, vendor=%r, max_tokens=%d)"
            % (self.model_id, self.family, self.vendor, self.max_tokens)
        )

    @property
    def last_call_metadata(self) -> Optional[Dict[str, Any]]:
        """Return a defensive copy of safe response metadata, never prompts/keys."""

        return deepcopy(self._last_call_metadata)

    def _request_body(self, request: Mapping[str, Any], seed: int) -> bytes:
        if type(seed) is not int or not 0 <= seed <= _MAX_SEED:
            raise OpenRouterRequestError(
                "seed must be a nonnegative 32-bit integer"
            )
        payload = {
            "model": self.model_id,
            "messages": list(_canonical_messages(request)),
            "seed": seed,
            "max_tokens": self.max_tokens,
            "response_format": _canonical_response_format(request),
        }
        if self.reasoning_effort is not None:
            payload["reasoning_effort"] = self.reasoning_effort
        try:
            return json.dumps(
                payload,
                ensure_ascii=False,
                allow_nan=False,
                separators=(",", ":"),
            ).encode("utf-8")
        except (TypeError, ValueError):
            raise OpenRouterRequestError(
                "canonical request could not be serialized"
            ) from None

    def _http_request(self, body: bytes) -> urllib.request.Request:
        return urllib.request.Request(
            CHAT_COMPLETIONS_URL,
            data=body,
            method="POST",
            headers={
                "Authorization": "Bearer %s" % self._api_key,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )

    def _execute(self, http_request: urllib.request.Request) -> Tuple[Any, int]:
        for attempt in range(1, self.max_attempts + 1):
            try:
                response = self._opener(http_request, timeout=self.timeout)
                return _read_response(response), attempt
            except urllib.error.HTTPError as error:
                retryable = error.code == 429 or 500 <= error.code <= 599
                if retryable and attempt < self.max_attempts:
                    delay = self.retry_base_seconds * (2 ** (attempt - 1))
                    headers = getattr(error, "headers", None)
                    retry_after = headers.get("Retry-After") if headers is not None else None
                    if retry_after is not None:
                        try:
                            parsed_retry_after = float(retry_after)
                        except (TypeError, ValueError):
                            parsed_retry_after = delay
                        if math.isfinite(parsed_retry_after) and parsed_retry_after >= 0:
                            delay = parsed_retry_after
                    delay = min(delay, 30.0)
                    self._sleeper(delay)
                    continue
                suffix = (
                    " after %d attempts" % attempt if retryable else ""
                )
                raise OpenRouterTransportError(
                    "OpenRouter HTTP %d%s" % (error.code, suffix)
                ) from None
            except (urllib.error.URLError, TimeoutError, OSError):
                raise OpenRouterTransportError(
                    "OpenRouter network transport failed on attempt %d" % attempt
                ) from None
        raise OpenRouterTransportError("OpenRouter retry loop ended unexpectedly")

    def _parse_completion(
        self, payload: Mapping[str, Any], *, seed: int, attempt_count: int
    ) -> str:
        if "error" in payload and payload["error"] is not None:
            raise OpenRouterResponseError(
                "completion response contained an in-band error"
            )
        choices = payload.get("choices")
        if not isinstance(choices, list) or not choices:
            raise OpenRouterResponseError("completion choices must be nonempty")
        choice = choices[0]
        if not isinstance(choice, Mapping):
            raise OpenRouterResponseError("first completion choice must be an object")
        if "error" in choice and choice["error"] is not None:
            raise OpenRouterResponseError(
                "first completion choice contained an error"
            )
        message = choice.get("message")
        if not isinstance(message, Mapping):
            raise OpenRouterResponseError("first completion choice is missing message")
        content = message.get("content")
        if not isinstance(content, str) or not content.strip():
            raise OpenRouterResponseError(
                "first completion message content must be nonblank text"
            )
        if self._api_key in content:
            raise OpenRouterResponseError(
                "completion content contained credential material"
            )

        response_id = _required_response_string(
            payload.get("id"), "id", secret=self._api_key
        )
        response_model = _required_response_string(
            payload.get("model"),
            "model",
            secret=self._api_key,
        )
        allowed_response_models = {
            self.model_id,
            FROZEN_CANONICAL_MODEL_IDS[self.model_id],
        }
        if response_model not in allowed_response_models:
            raise OpenRouterResponseError(
                "completion model did not match the requested alias or exact frozen canonical slug"
            )
        finish_reason = _required_response_string(
            choice.get("finish_reason"), "finish_reason", secret=self._api_key
        )
        if finish_reason != "stop":
            raise OpenRouterResponseError(
                "completion finish_reason was not stop"
            )
        metadata = {
            "response_id": response_id,
            "model": response_model,
            "finish_reason": finish_reason,
            "usage": _safe_usage(payload),
            "requested_seed": seed,
            "attempt_count": attempt_count,
        }
        # This check is intentionally redundant with the field validators: it
        # prevents future metadata additions from accidentally serializing a key.
        serialized = json.dumps(metadata, sort_keys=True, allow_nan=False)
        if self._api_key in serialized:
            raise OpenRouterResponseError(
                "safe completion metadata contained credential material"
            )
        self._last_call_metadata = metadata
        return content

    def generate(self, request: Mapping[str, Any], *, seed: int) -> str:
        """Return a nonblank completion for one sanitized canonical request."""

        self._last_call_metadata = None
        body = self._request_body(request, seed)
        raw_body, attempt_count = self._execute(self._http_request(body))
        payload = _decode_json_body(
            raw_body, OpenRouterResponseError, "completion response"
        )
        return self._parse_completion(
            payload, seed=seed, attempt_count=attempt_count
        )


def openrouter_client_from_roster(
    roster_entry: Mapping[str, Any], **client_options: Any
) -> OpenRouterClient:
    """Build a client from one exact, non-secret frozen roster mapping."""

    if not isinstance(roster_entry, Mapping) or set(roster_entry) != {
        "model_id",
        "family",
        "vendor",
    }:
        raise OpenRouterConfigurationError(
            "roster entry must contain only model_id, family, and vendor"
        )
    model_id = roster_entry.get("model_id")
    expected = _ROSTER_BY_ID.get(model_id)
    if expected is None or any(
        roster_entry.get(field) != expected[field]
        for field in ("model_id", "family", "vendor")
    ):
        raise OpenRouterConfigurationError(
            "roster entry does not match the frozen requested OpenRouter roster"
        )
    return OpenRouterClient(
        expected["model_id"],
        family=expected["family"],
        vendor=expected["vendor"],
        **client_options,
    )


def verify_requested_model_catalog(
    *,
    api_key: Optional[str] = None,
    opener: Optional[Callable[..., Any]] = None,
    timeout: float = 30.0,
) -> Dict[str, Any]:
    """Verify all three exact requested slugs against ``/api/v1/models``."""

    resolved_key = _resolve_api_key(api_key)
    resolved_timeout = _validated_timeout(timeout)
    resolved_opener = urllib.request.urlopen if opener is None else opener
    if not callable(resolved_opener):
        raise OpenRouterConfigurationError("opener must be callable")
    request = urllib.request.Request(
        MODELS_URL,
        method="GET",
        headers={
            "Authorization": "Bearer %s" % resolved_key,
            "Accept": "application/json",
        },
    )
    try:
        response = resolved_opener(request, timeout=resolved_timeout)
        raw_body = _read_response(response)
    except urllib.error.HTTPError as error:
        raise OpenRouterCatalogError(
            "OpenRouter model catalog returned HTTP %d" % error.code
        ) from None
    except (urllib.error.URLError, TimeoutError, OSError):
        raise OpenRouterCatalogError(
            "OpenRouter model catalog transport failed"
        ) from None
    payload = _decode_json_body(
        raw_body, OpenRouterCatalogError, "model catalog response"
    )
    rows = payload.get("data")
    if not isinstance(rows, list):
        raise OpenRouterCatalogError("model catalog data must be a list")
    available = set()
    for row in rows:
        if (
            not isinstance(row, Mapping)
            or not isinstance(row.get("id"), str)
            or not row["id"].strip()
        ):
            raise OpenRouterCatalogError("model catalog contains an invalid row")
        model_id = row["id"]
        if model_id in REQUESTED_MODEL_IDS:
            if model_id in available:
                raise OpenRouterCatalogError(
                    "model catalog contains duplicate requested slug: %s" % model_id
                )
            expected_canonical = FROZEN_CANONICAL_MODEL_IDS[model_id]
            if row.get("canonical_slug") != expected_canonical:
                raise OpenRouterCatalogError(
                    "model catalog canonical_slug mismatch for %s" % model_id
                )
            supported = row.get("supported_parameters")
            if (
                not isinstance(supported, list)
                or any(not isinstance(value, str) for value in supported)
            ):
                raise OpenRouterCatalogError(
                    "model catalog supported_parameters invalid for %s" % model_id
                )
            missing_parameters = _REQUIRED_CATALOG_PARAMETERS.difference(supported)
            if missing_parameters:
                raise OpenRouterCatalogError(
                    "model catalog missing supported parameter(s) for %s: %s"
                    % (model_id, ", ".join(sorted(missing_parameters)))
                )
        available.add(model_id)
    missing = [model_id for model_id in REQUESTED_MODEL_IDS if model_id not in available]
    if missing:
        raise OpenRouterCatalogError(
            "requested OpenRouter model slug(s) missing: %s" % ", ".join(missing)
        )
    return {"verified": True, "model_ids": list(REQUESTED_MODEL_IDS)}


__all__ = [
    "CHAT_COMPLETIONS_URL",
    "FROZEN_CANONICAL_MODEL_IDS",
    "MODELS_URL",
    "REQUESTED_MODEL_IDS",
    "REQUESTED_MODEL_ROSTER",
    "OpenRouterCatalogError",
    "OpenRouterClient",
    "OpenRouterConfigurationError",
    "OpenRouterError",
    "OpenRouterRequestError",
    "OpenRouterResponseError",
    "OpenRouterTransportError",
    "openrouter_client_from_roster",
    "verify_requested_model_catalog",
]
