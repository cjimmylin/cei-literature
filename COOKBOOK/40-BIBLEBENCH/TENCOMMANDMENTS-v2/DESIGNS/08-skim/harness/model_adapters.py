"""Public request projection and a small, fail-closed OpenRouter adapter."""

from __future__ import annotations

from copy import deepcopy
import json
import math
import os
import time
from typing import Any, Callable, Dict, Mapping, Optional
import urllib.error
import urllib.request


CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"
_MAX_ATTEMPTS_LIMIT = 5
_MAX_RETRY_DELAY_SECONDS = 30.0

_PUBLIC_REQUEST_KEYS = (
    "options",
    "prompt",
    "response_schema",
    "structured_state",
    "tool_schema",
    "traceability",
)
_PRIVATE_KEYS = frozenset(
    {
        "mechanical_action_map",
        "principal_optimal_action_id",
        "diversion_action_ids",
        "recognition_answer_id",
        "private_gold",
        "rs_trigger",
        "theta_eligible",
    }
)
_SAFE_USAGE_KEYS = frozenset(
    {
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "reasoning_tokens",
        "cached_tokens",
        "cost",
        "upstream_inference_cost",
        "is_byok",
    }
)
_DEVELOPER_MESSAGE = (
    "Return exactly one JSON object matching response_schema and invoking the "
    "declared tool. Do not include Markdown fences, commentary, or extra text."
)


class OpenRouterError(RuntimeError):
    """Base class for sanitized OpenRouter adapter failures."""


class OpenRouterConfigurationError(OpenRouterError):
    """Raised when client configuration is unsafe or invalid."""


class OpenRouterRequestError(OpenRouterError):
    """Raised before transport when a model request is invalid."""


class OpenRouterTransportError(OpenRouterError):
    """Raised when the HTTP exchange fails."""

    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int],
        attempt_count: int,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.attempt_count = attempt_count


class OpenRouterResponseError(OpenRouterError):
    """Raised when a response cannot be safely accepted."""


def _contains_private_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        if any(key in _PRIVATE_KEYS for key in value):
            return True
        return any(_contains_private_key(child) for child in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_private_key(child) for child in value)
    return False


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def build_model_request(runtime_row: Mapping[str, Any]) -> Dict[str, Any]:
    """Project one frozen runtime row into its public model-facing request."""

    if not isinstance(runtime_row, Mapping):
        raise TypeError("runtime row must be an object")
    request_id = runtime_row.get("runtime_request_id")
    template = runtime_row.get("request_template")
    if not isinstance(request_id, str) or not request_id.strip():
        raise ValueError("runtime row is missing runtime_request_id")
    if not isinstance(template, Mapping):
        raise ValueError("runtime row is missing request_template")
    if template.get("request_id") != request_id:
        raise ValueError("runtime request/template identifier mismatch")
    missing = [key for key in _PUBLIC_REQUEST_KEYS if key not in template]
    if missing:
        raise ValueError("request template is missing public projection fields")

    public_projection = {key: template[key] for key in _PUBLIC_REQUEST_KEYS}
    if _contains_private_key(public_projection):
        raise ValueError("private scoring metadata leaked into public projection")
    content = _canonical_json(public_projection)
    return {
        "request_id": request_id,
        "messages": [
            {"role": "developer", "content": _DEVELOPER_MESSAGE},
            {"role": "user", "content": content},
        ],
        "response_format": {"type": "text"},
    }


def _nonblank_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise OpenRouterConfigurationError("%s must be nonblank text" % label)
    return value


def _resolve_api_key(value: Optional[str]) -> str:
    candidate = os.environ.get("OPENROUTER_API_KEY") if value is None else value
    if (
        not isinstance(candidate, str)
        or not candidate
        or candidate.strip() != candidate
        or any(ord(character) < 33 or ord(character) > 126 for character in candidate)
    ):
        raise OpenRouterConfigurationError(
            "OPENROUTER_API_KEY must be header-safe ASCII text"
        )
    return candidate


def _safe_messages(request: Mapping[str, Any]) -> list:
    if not isinstance(request, Mapping):
        raise OpenRouterRequestError("model request must be an object")
    messages = request.get("messages")
    if not isinstance(messages, list) or not messages:
        raise OpenRouterRequestError("model request requires messages")
    safe = []
    for message in messages:
        if not isinstance(message, Mapping) or set(message) != {"role", "content"}:
            raise OpenRouterRequestError(
                "each message must contain only role and content"
            )
        role = message.get("role")
        content = message.get("content")
        if role not in {"developer", "system", "user", "assistant"}:
            raise OpenRouterRequestError("message role is invalid")
        if not isinstance(content, str) or not content.strip():
            raise OpenRouterRequestError("message content must be nonblank text")
        safe.append({"role": role, "content": content})
    if request.get("response_format") != {"type": "text"}:
        raise OpenRouterRequestError("response_format must be exactly type=text")
    return safe


def _safe_usage(value: Any) -> Dict[str, Any]:
    if not isinstance(value, Mapping):
        raise OpenRouterResponseError("response usage must be an object")
    safe = {key: child for key, child in value.items() if key in _SAFE_USAGE_KEYS}
    for key, child in safe.items():
        if key == "is_byok":
            if type(child) is not bool:
                raise OpenRouterResponseError("usage is_byok must be boolean")
        elif key.endswith("tokens"):
            if type(child) is not int or child < 0:
                raise OpenRouterResponseError("usage token counts must be nonnegative integers")
        elif isinstance(child, bool) or not isinstance(child, (int, float)):
            raise OpenRouterResponseError("usage cost fields must be numeric")
        elif not math.isfinite(float(child)) or child < 0:
            raise OpenRouterResponseError("usage cost fields must be finite and nonnegative")
    return safe


class OpenRouterClient:
    """Generic OpenRouter client with pinned provider routing and a cost cap."""

    def __init__(
        self,
        model_id: str,
        family: str,
        vendor: str,
        provider: str,
        api_key: Optional[str] = None,
        max_tokens: int = 256,
        cost_cap_usd: float = 1.0,
        max_attempts: int = 3,
        retry_base_seconds: float = 1.0,
        opener: Optional[Callable[..., Any]] = None,
        sleeper: Optional[Callable[[float], Any]] = None,
    ) -> None:
        self.model_id = _nonblank_string(model_id, "model_id")
        self.family = _nonblank_string(family, "family")
        self.vendor = _nonblank_string(vendor, "vendor")
        self.provider = _nonblank_string(provider, "provider")
        if type(max_tokens) is not int or not 1 <= max_tokens <= 16_384:
            raise OpenRouterConfigurationError(
                "max_tokens must be an integer in [1, 16384]"
            )
        if (
            isinstance(cost_cap_usd, bool)
            or not isinstance(cost_cap_usd, (int, float))
            or not math.isfinite(float(cost_cap_usd))
            or cost_cap_usd <= 0
        ):
            raise OpenRouterConfigurationError("cost_cap_usd must be finite and positive")
        self.max_tokens = max_tokens
        self.cost_cap_usd = float(cost_cap_usd)
        if type(max_attempts) is not int or not 1 <= max_attempts <= _MAX_ATTEMPTS_LIMIT:
            raise OpenRouterConfigurationError(
                "max_attempts must be an integer in [1, %d]" % _MAX_ATTEMPTS_LIMIT
            )
        if (
            isinstance(retry_base_seconds, bool)
            or not isinstance(retry_base_seconds, (int, float))
            or not math.isfinite(float(retry_base_seconds))
            or not 0 <= float(retry_base_seconds) <= _MAX_RETRY_DELAY_SECONDS
        ):
            raise OpenRouterConfigurationError(
                "retry_base_seconds must be finite and in [0, 30]"
            )
        self.max_attempts = max_attempts
        self.retry_base_seconds = float(retry_base_seconds)
        self.spent_cost_usd = 0.0
        self._api_key = _resolve_api_key(api_key)
        self._opener = urllib.request.urlopen if opener is None else opener
        self._sleeper = time.sleep if sleeper is None else sleeper
        if not callable(self._opener) or not callable(self._sleeper):
            raise OpenRouterConfigurationError("opener and sleeper must be callable")
        self._last_call_metadata: Optional[Dict[str, Any]] = None

    def __repr__(self) -> str:
        return (
            "OpenRouterClient(model_id=%r, family=%r, vendor=%r, provider=%r)"
            % (self.model_id, self.family, self.vendor, self.provider)
        )

    @property
    def last_call_metadata(self) -> Optional[Dict[str, Any]]:
        return deepcopy(self._last_call_metadata)

    def _body(self, request: Mapping[str, Any], seed: int) -> bytes:
        if type(seed) is not int or not 0 <= seed <= 2**31 - 1:
            raise OpenRouterRequestError("seed must be a nonnegative 32-bit integer")
        body = {
            "model": self.model_id,
            "messages": _safe_messages(request),
            "seed": seed,
            "max_tokens": self.max_tokens,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "provider": {
                "order": [self.provider],
                "allow_fallbacks": False,
                "require_parameters": True,
            },
            "usage": {"include": True},
        }
        try:
            return _canonical_json(body).encode("utf-8")
        except (TypeError, ValueError):
            raise OpenRouterRequestError("model request is not canonical JSON") from None

    def _account_paid_response(
        self,
        payload: Mapping[str, Any],
        usage: Mapping[str, Any],
        attempt_count: int,
    ) -> float:
        cost = usage.get("cost")
        if isinstance(cost, bool) or not isinstance(cost, (int, float)):
            raise OpenRouterResponseError(
                "response usage did not include numeric cost"
            )
        cost_usd = float(cost)
        metadata: Dict[str, Any] = {
            "requested_model": self.model_id,
            "usage": dict(usage),
            "cost_usd": cost_usd,
            "attempt_count": attempt_count,
            "response_status": "RECEIVED_UNVALIDATED",
        }
        choices = payload.get("choices")
        choice = choices[0] if isinstance(choices, list) and choices else None
        candidates = {
            "response_id": payload.get("id"),
            "returned_model": payload.get("model"),
            "provider": payload.get("provider"),
            "finish_reason": (
                choice.get("finish_reason")
                if isinstance(choice, Mapping)
                else None
            ),
        }
        for field, value in candidates.items():
            if (
                isinstance(value, str)
                and value.strip()
                and self._api_key not in value
            ):
                metadata[field] = value
        self.spent_cost_usd = math.fsum((self.spent_cost_usd, cost_usd))
        self._last_call_metadata = metadata
        return cost_usd

    def _parse(self, raw: Any, *, attempt_count: int) -> str:
        if isinstance(raw, bytes):
            try:
                raw = raw.decode("utf-8")
            except UnicodeDecodeError:
                raise OpenRouterResponseError("response was not UTF-8") from None
        if not isinstance(raw, str):
            raise OpenRouterResponseError("response body must be bytes or text")
        try:
            payload = json.loads(raw)
        except (TypeError, ValueError):
            raise OpenRouterResponseError("response was not valid JSON") from None
        if not isinstance(payload, Mapping):
            raise OpenRouterResponseError("response payload was malformed")
        usage = _safe_usage(payload.get("usage"))
        self._account_paid_response(payload, usage, attempt_count)
        try:
            if payload.get("error") is not None:
                raise OpenRouterResponseError("response payload was malformed")
            choices = payload.get("choices")
            if (
                not isinstance(choices, list)
                or not choices
                or not isinstance(choices[0], Mapping)
            ):
                raise OpenRouterResponseError("response choices were malformed")
            choice = choices[0]
            message = choice.get("message")
            if not isinstance(message, Mapping):
                raise OpenRouterResponseError("response message was malformed")
            content = message.get("content")
            if not isinstance(content, str) or not content.strip():
                raise OpenRouterResponseError(
                    "response content must be nonblank text"
                )

            response_id = payload.get("id")
            returned_model = payload.get("model")
            returned_provider = payload.get("provider")
            finish_reason = choice.get("finish_reason")
            for value, label in (
                (response_id, "id"),
                (returned_model, "model"),
                (finish_reason, "finish_reason"),
            ):
                if not isinstance(value, str) or not value.strip():
                    raise OpenRouterResponseError(
                        "response %s was malformed" % label
                    )
                if self._api_key in value:
                    raise OpenRouterResponseError(
                        "response metadata contained credential material"
                    )
            if returned_provider is not None and (
                not isinstance(returned_provider, str)
                or not returned_provider.strip()
                or self._api_key in returned_provider
            ):
                raise OpenRouterResponseError(
                    "response provider was malformed"
                )
            if (
                returned_provider is not None
                and returned_provider != self.provider
            ):
                raise OpenRouterResponseError(
                    "response provider did not match pinned provider"
                )
            if finish_reason != "stop":
                raise OpenRouterResponseError(
                    "response did not finish normally"
                )
            if self._api_key in content:
                raise OpenRouterResponseError(
                    "response content contained credential material"
                )
            if self.spent_cost_usd > self.cost_cap_usd:
                raise OpenRouterResponseError(
                    "response cost exceeded configured cap"
                )
            if self._api_key in _canonical_json(self._last_call_metadata):
                raise OpenRouterResponseError(
                    "safe metadata contained credential material"
                )
        except OpenRouterResponseError:
            self._last_call_metadata["response_status"] = "REJECTED_RESPONSE"
            raise
        self._last_call_metadata["provider"] = self.provider
        self._last_call_metadata["provider_attribution"] = (
            "RESPONSE_ECHOED"
            if returned_provider is not None
            else "REQUEST_PINNED_ALLOW_FALLBACKS_FALSE"
        )
        self._last_call_metadata["response_status"] = "ACCEPTED"
        return content

    def generate(self, request: Mapping[str, Any], *, seed: int) -> str:
        """POST one bounded request and return one validated text response."""

        self._last_call_metadata = None
        http_request = urllib.request.Request(
            CHAT_COMPLETIONS_URL,
            data=self._body(request, seed),
            method="POST",
            headers={
                "Authorization": "Bearer %s" % self._api_key,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        for attempt in range(1, self.max_attempts + 1):
            try:
                response = self._opener(http_request, timeout=60.0)
                with response as handle:
                    raw = handle.read()
                return self._parse(raw, attempt_count=attempt)
            except urllib.error.HTTPError as error:
                retryable = error.code == 429
                if retryable and attempt < self.max_attempts:
                    delay = self.retry_base_seconds * (2 ** (attempt - 1))
                    headers = getattr(error, "headers", None)
                    retry_after = (
                        headers.get("Retry-After") if headers is not None else None
                    )
                    if retry_after is not None:
                        try:
                            parsed_retry_after = float(retry_after)
                        except (TypeError, ValueError):
                            parsed_retry_after = delay
                        if (
                            math.isfinite(parsed_retry_after)
                            and parsed_retry_after >= 0
                        ):
                            delay = parsed_retry_after
                    self._sleeper(min(delay, _MAX_RETRY_DELAY_SECONDS))
                    continue
                suffix = " after %d attempts" % attempt if retryable else ""
                raise OpenRouterTransportError(
                    "OpenRouter HTTP %d%s" % (error.code, suffix),
                    status_code=error.code,
                    attempt_count=attempt,
                ) from None
            except (urllib.error.URLError, TimeoutError, OSError):
                raise OpenRouterTransportError(
                    "OpenRouter transport failed on attempt %d" % attempt,
                    status_code=None,
                    attempt_count=attempt,
                ) from None
        raise OpenRouterTransportError(
            "OpenRouter retry loop ended unexpectedly",
            status_code=None,
            attempt_count=self.max_attempts,
        )


__all__ = [
    "OpenRouterClient",
    "OpenRouterConfigurationError",
    "OpenRouterError",
    "OpenRouterRequestError",
    "OpenRouterResponseError",
    "OpenRouterTransportError",
    "build_model_request",
]
