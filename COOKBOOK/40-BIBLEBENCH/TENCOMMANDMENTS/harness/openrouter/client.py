"""Sanitized, exact-provider OpenRouter chat transport and catalog preflight."""

from copy import deepcopy
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import json
import math
import os
import threading
import time
from typing import Any, Callable, Dict, Mapping, Optional, Sequence, Tuple
import urllib.error
import urllib.request

from TENCOMMANDMENTS.harness.custody_stack.schema import (
    SchemaValidationError,
    strict_json_loads,
)

from .budget import SpendLedger
from .canonical import CanonicalJSONError, canonical_json_bytes


CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_ENDPOINTS_URL = "https://openrouter.ai/api/v1/models/%s/endpoints"
OPENROUTER_API_KEY_ENV = "OPENROUTER_API_KEY"
MAX_RESPONSE_BYTES = 1024 * 1024
_MAX_ATTEMPTS = 5
_MAX_RETRY_DELAY_SECONDS = 30.0
_MAX_TOKENS = 16_384
_MAX_SEED = (2**31) - 1
_DEFAULT_REQUIRED_PARAMETERS = (
    "max_tokens",
    "response_format",
    "seed",
    "temperature",
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
    """Base class for sanitized OpenRouter failures."""


class OpenRouterConfigurationError(OpenRouterError):
    """Raised when a route or local client option is unsafe."""


class OpenRouterRequestError(OpenRouterError):
    """Raised before transport when a chat request is not canonical."""


class OpenRouterTransportError(OpenRouterError):
    """Raised when an HTTP exchange has no safely accepted response."""

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
    """Raised after transport when a paid response fails validation."""


class OpenRouterCatalogError(OpenRouterError):
    """Raised when an exact model/provider endpoint cannot be verified."""


def _exact_text(value: Any, label: str, error_type: type) -> str:
    if type(value) is not str or not value.strip() or value.strip() != value:
        raise error_type("%s must be nonblank exact text" % label)
    try:
        value.encode("utf-8", errors="strict")
    except UnicodeError:
        raise error_type("%s must be valid UTF-8 text" % label) from None
    return value


def _price_text(value: Any, label: str) -> str:
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise OpenRouterConfigurationError("%s must be a finite nonnegative price" % label)
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise OpenRouterConfigurationError(
            "%s must be a finite nonnegative price" % label
        ) from None
    if not amount.is_finite() or amount < 0:
        raise OpenRouterConfigurationError("%s must be a finite nonnegative price" % label)
    text = format(amount, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return "0" if text in {"", "-0"} else text


@dataclass(frozen=True)
class ModelRoute:
    """One frozen OpenRouter model and exact provider endpoint contract."""

    model_id: str
    provider: str
    endpoint_name: str
    prompt_price_per_token_usd: Any
    completion_price_per_token_usd: Any
    canonical_model_id: Optional[str] = None
    required_parameters: Tuple[str, ...] = _DEFAULT_REQUIRED_PARAMETERS

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "model_id",
            _exact_text(self.model_id, "model_id", OpenRouterConfigurationError),
        )
        object.__setattr__(
            self,
            "provider",
            _exact_text(self.provider, "provider", OpenRouterConfigurationError),
        )
        object.__setattr__(
            self,
            "endpoint_name",
            _exact_text(
                self.endpoint_name,
                "endpoint_name",
                OpenRouterConfigurationError,
            ),
        )
        object.__setattr__(
            self,
            "prompt_price_per_token_usd",
            _price_text(
                self.prompt_price_per_token_usd,
                "prompt_price_per_token_usd",
            ),
        )
        object.__setattr__(
            self,
            "completion_price_per_token_usd",
            _price_text(
                self.completion_price_per_token_usd,
                "completion_price_per_token_usd",
            ),
        )
        if self.canonical_model_id is not None:
            object.__setattr__(
                self,
                "canonical_model_id",
                _exact_text(
                    self.canonical_model_id,
                    "canonical_model_id",
                    OpenRouterConfigurationError,
                ),
            )
        if not isinstance(self.required_parameters, (list, tuple)):
            raise OpenRouterConfigurationError(
                "required_parameters must be an exact sequence"
            )
        parameters = tuple(
            _exact_text(value, "required parameter", OpenRouterConfigurationError)
            for value in self.required_parameters
        )
        if len(set(parameters)) != len(parameters):
            raise OpenRouterConfigurationError("required_parameters contains duplicates")
        if not set(_DEFAULT_REQUIRED_PARAMETERS).issubset(parameters):
            raise OpenRouterConfigurationError(
                "required_parameters must include the chat transport parameters"
            )
        object.__setattr__(self, "required_parameters", parameters)


@dataclass(frozen=True)
class CatalogVerification:
    """Sanitized proof that every frozen route matched one healthy endpoint."""

    routes: Tuple[ModelRoute, ...]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "verified": True,
            "routes": [
                {
                    "model_id": row.model_id,
                    "provider": row.provider,
                    "endpoint_name": row.endpoint_name,
                }
                for row in self.routes
            ],
        }


def _resolve_api_key(value: Optional[str]) -> str:
    candidate = os.environ.get(OPENROUTER_API_KEY_ENV) if value is None else value
    if (
        type(candidate) is not str
        or not candidate
        or candidate.strip() != candidate
        or any(ord(character) < 33 or ord(character) > 126 for character in candidate)
    ):
        raise OpenRouterConfigurationError(
            "%s must be header-safe ASCII text" % OPENROUTER_API_KEY_ENV
        )
    return candidate


def _bounded_int(value: Any, label: str, minimum: int, maximum: int) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise OpenRouterConfigurationError(
            "%s must be an integer in [%d, %d]" % (label, minimum, maximum)
        )
    return value


def _bounded_number(
    value: Any, label: str, minimum_exclusive: float, maximum: float
) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or not minimum_exclusive < float(value) <= maximum
    ):
        raise OpenRouterConfigurationError(
            "%s must be in (%s, %s]" % (label, minimum_exclusive, maximum)
        )
    return float(value)


def _retry_base(value: Any) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or not 0 <= float(value) <= _MAX_RETRY_DELAY_SECONDS
    ):
        raise OpenRouterConfigurationError(
            "retry_base_seconds must be finite and in [0, 30]"
        )
    return float(value)


def _read_http_response(response: Any) -> Tuple[int, bytes]:
    with response as handle:
        status = getattr(handle, "status", 200)
        raw = handle.read()
    if type(status) is not int:
        raise OpenRouterTransportError(
            "OpenRouter response status was invalid",
            status_code=None,
            attempt_count=1,
        )
    if type(raw) is not bytes or len(raw) > MAX_RESPONSE_BYTES:
        raise OpenRouterResponseError("OpenRouter response body was invalid or too large")
    return status, raw


def _retry_delay(error: Any, fallback: float) -> float:
    headers = getattr(error, "headers", None)
    retry_after = headers.get("Retry-After") if headers is not None else None
    if retry_after is not None:
        try:
            parsed = float(retry_after)
        except (TypeError, ValueError):
            parsed = fallback
        if math.isfinite(parsed) and parsed >= 0:
            fallback = parsed
    return min(fallback, _MAX_RETRY_DELAY_SECONDS)


def _decode_object(raw: bytes, label: str, error_type: type) -> Dict[str, Any]:
    try:
        text = raw.decode("utf-8", errors="strict")
        payload = strict_json_loads(text)
    except (UnicodeError, SchemaValidationError) as exc:
        raise error_type("%s was not bounded valid JSON" % label) from exc
    if type(payload) is not dict:
        raise error_type("%s root must be an object" % label)
    return payload


def _safe_usage_value(field: str, value: Any) -> Any:
    if field in _DETAIL_USAGE_KEYS:
        if not isinstance(value, Mapping):
            raise OpenRouterResponseError("usage %s must be an object" % field)
        return {
            key: _safe_usage_value(key, child)
            for key, child in value.items()
            if type(key) is str and key in _SAFE_USAGE_KEYS
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
    usage = payload.get("usage")
    if not isinstance(usage, Mapping):
        raise OpenRouterResponseError("response usage must be an object")
    safe = {
        key: _safe_usage_value(key, value)
        for key, value in usage.items()
        if type(key) is str and key in _SAFE_USAGE_KEYS
    }
    if "cost" not in safe:
        raise OpenRouterResponseError("response usage must include numeric cost")
    return safe


def _cost_text(value: Any) -> str:
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise OpenRouterResponseError("response cost was invalid") from None
    if not amount.is_finite() or amount < 0:
        raise OpenRouterResponseError("response cost was invalid")
    text = format(amount, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return "0" if text in {"", "-0"} else text


def _safe_request(request: Any) -> Tuple[Sequence[Dict[str, str]], Dict[str, str]]:
    if type(request) is not dict or set(request) != {"messages", "response_format"}:
        raise OpenRouterRequestError(
            "chat request fields must be exactly messages and response_format"
        )
    messages = request["messages"]
    if type(messages) is not list or not messages:
        raise OpenRouterRequestError("chat request messages must be a nonempty list")
    safe_messages = []
    for message in messages:
        if type(message) is not dict or set(message) != {"role", "content"}:
            raise OpenRouterRequestError(
                "each message must contain only role and content"
            )
        role = message.get("role")
        content = message.get("content")
        if role not in _ALLOWED_ROLES:
            raise OpenRouterRequestError("message role is invalid")
        if type(content) is not str or not content.strip():
            raise OpenRouterRequestError("message content must be nonblank text")
        safe_messages.append({"role": role, "content": content})
    response_format = request["response_format"]
    if (
        type(response_format) is not dict
        or set(response_format) != {"type"}
        or response_format.get("type") not in {"json_object", "text"}
    ):
        raise OpenRouterRequestError(
            "response_format must be exactly type=text or type=json_object"
        )
    return safe_messages, {"type": response_format["type"]}


class OpenRouterChatClient:
    """Stdlib chat client with exact provider routing and paid-cost custody."""

    def __init__(
        self,
        route: ModelRoute,
        *,
        api_key: Optional[str] = None,
        max_tokens: int = 256,
        timeout: float = 60.0,
        max_attempts: int = 3,
        retry_base_seconds: float = 1.0,
        opener: Optional[Callable[..., Any]] = None,
        sleeper: Optional[Callable[[float], Any]] = None,
        ledger: Optional[SpendLedger] = None,
    ) -> None:
        if type(route) is not ModelRoute:
            raise OpenRouterConfigurationError("route must be an exact ModelRoute")
        if ledger is not None and type(ledger) is not SpendLedger:
            raise OpenRouterConfigurationError("ledger must be an exact SpendLedger")
        self.route = route
        self.max_tokens = _bounded_int(max_tokens, "max_tokens", 1, _MAX_TOKENS)
        self.timeout = _bounded_number(timeout, "timeout", 0, 300)
        self.max_attempts = _bounded_int(
            max_attempts, "max_attempts", 1, _MAX_ATTEMPTS
        )
        self.retry_base_seconds = _retry_base(retry_base_seconds)
        self._api_key = _resolve_api_key(api_key)
        self._opener = urllib.request.urlopen if opener is None else opener
        self._sleeper = time.sleep if sleeper is None else sleeper
        if not callable(self._opener) or not callable(self._sleeper):
            raise OpenRouterConfigurationError("opener and sleeper must be callable")
        self._ledger = ledger
        self._spent = Decimal("0")
        self._completed_call_ids = set()
        self._reserved_call_ids = set()
        self._seen_response_ids = set()
        self._last_call_metadata = None  # type: Optional[Dict[str, Any]]
        self._lock = threading.Lock()

    def __repr__(self) -> str:
        return "OpenRouterChatClient(model_id=%r, provider=%r)" % (
            self.route.model_id,
            self.route.provider,
        )

    @property
    def last_call_metadata(self) -> Optional[Dict[str, Any]]:
        return deepcopy(self._last_call_metadata)

    def _body(self, request: Any, seed: int) -> bytes:
        if type(seed) is not int or not 0 <= seed <= _MAX_SEED:
            raise OpenRouterRequestError(
                "seed must be a nonnegative 32-bit integer"
            )
        messages, response_format = _safe_request(request)
        body = {
            "model": self.route.model_id,
            "messages": list(messages),
            "seed": seed,
            "max_tokens": self.max_tokens,
            "temperature": 0,
            "response_format": response_format,
            "provider": {
                "order": [self.route.provider],
                "allow_fallbacks": False,
                "require_parameters": True,
            },
            "usage": {"include": True},
        }
        try:
            encoded = canonical_json_bytes(body)
        except CanonicalJSONError as exc:
            raise OpenRouterRequestError("chat request is not canonical JSON") from exc
        if self._api_key.encode("ascii") in encoded:
            raise OpenRouterRequestError(
                "chat request contained credential material"
            )
        return encoded

    def _http_request(self, body: bytes) -> urllib.request.Request:
        return urllib.request.Request(
            CHAT_COMPLETIONS_URL,
            data=body,
            method="POST",
            headers={
                "Authorization": "Bearer " + self._api_key,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )

    def _execute(self, request: urllib.request.Request) -> Tuple[bytes, int]:
        for attempt in range(1, self.max_attempts + 1):
            try:
                response = self._opener(request, timeout=self.timeout)
                status, raw = _read_http_response(response)
                if status != 200:
                    if status == 429 and attempt < self.max_attempts:
                        self._sleeper(
                            min(
                                self.retry_base_seconds * (2 ** (attempt - 1)),
                                _MAX_RETRY_DELAY_SECONDS,
                            )
                        )
                        continue
                    raise OpenRouterTransportError(
                        "OpenRouter HTTP %d" % status,
                        status_code=status,
                        attempt_count=attempt,
                    )
                return raw, attempt
            except urllib.error.HTTPError as error:
                if error.code == 429 and attempt < self.max_attempts:
                    fallback = self.retry_base_seconds * (2 ** (attempt - 1))
                    self._sleeper(_retry_delay(error, fallback))
                    continue
                suffix = " after %d attempts" % attempt if error.code == 429 else ""
                raise OpenRouterTransportError(
                    "OpenRouter HTTP %d%s" % (error.code, suffix),
                    status_code=error.code,
                    attempt_count=attempt,
                ) from None
            except OpenRouterTransportError:
                raise
            except (urllib.error.URLError, TimeoutError, OSError):
                raise OpenRouterTransportError(
                    "OpenRouter transport failed on attempt %d" % attempt,
                    status_code=None,
                    attempt_count=attempt,
                ) from None
        raise OpenRouterTransportError(
            "OpenRouter 429 retry loop ended unexpectedly",
            status_code=429,
            attempt_count=self.max_attempts,
        )

    def _account_paid_response(
        self,
        payload: Mapping[str, Any],
        *,
        call_id: str,
        seed: int,
        attempt_count: int,
    ) -> Dict[str, Any]:
        usage = _safe_usage(payload)
        cost_text = _cost_text(usage["cost"])
        metadata = {
            "call_id": call_id,
            "requested_model": self.route.model_id,
            "provider": self.route.provider,
            "requested_seed": seed,
            "attempt_count": attempt_count,
            "usage": usage,
            "cost_usd": cost_text,
            "response_status": "RECEIVED_UNVALIDATED",
        }
        self._last_call_metadata = metadata
        self._completed_call_ids.add(call_id)
        self._reserved_call_ids.discard(call_id)
        if self._ledger is not None:
            try:
                self._ledger.record_paid_call(call_id, cost_text)
            except Exception:
                metadata["cumulative_cost_usd"] = self._ledger.spent_cost_usd
                metadata["response_status"] = "REJECTED_SPEND_BOUND"
                raise
            metadata["cumulative_cost_usd"] = self._ledger.spent_cost_usd
        else:
            self._spent += Decimal(cost_text)
            metadata["cumulative_cost_usd"] = _cost_text(self._spent)
        return metadata

    def _validate_response(
        self,
        payload: Mapping[str, Any],
        metadata: Dict[str, Any],
    ) -> str:
        try:
            if payload.get("error") is not None:
                raise OpenRouterResponseError(
                    "completion response contained an in-band error"
                )
            response_id = _exact_text(
                payload.get("id"), "response id", OpenRouterResponseError
            )
            returned_model = _exact_text(
                payload.get("model"), "response model", OpenRouterResponseError
            )
            allowed_models = {self.route.model_id}
            if self.route.canonical_model_id is not None:
                allowed_models.add(self.route.canonical_model_id)
            if returned_model not in allowed_models:
                raise OpenRouterResponseError(
                    "response model did not match the frozen route"
                )
            returned_provider = payload.get("provider")
            if returned_provider is not None:
                returned_provider = _exact_text(
                    returned_provider,
                    "response provider",
                    OpenRouterResponseError,
                )
                if returned_provider != self.route.provider:
                    raise OpenRouterResponseError(
                        "response provider did not match the exact provider pin"
                    )
            choices = payload.get("choices")
            if type(choices) is not list or not choices or type(choices[0]) is not dict:
                raise OpenRouterResponseError("response choices were malformed")
            choice = choices[0]
            message = choice.get("message")
            if type(message) is not dict:
                raise OpenRouterResponseError("response message was malformed")
            content = message.get("content")
            if type(content) is not str or not content.strip():
                raise OpenRouterResponseError("response content must be nonblank text")
            finish_reason = choice.get("finish_reason")
            if finish_reason != "stop":
                raise OpenRouterResponseError("response finish_reason was not stop")
            for value, label in (
                (response_id, "response id"),
                (returned_model, "response model"),
                (content, "response content"),
            ):
                if self._api_key in value:
                    raise OpenRouterResponseError(
                        "%s contained credential material" % label
                    )
            if response_id in self._seen_response_ids:
                raise OpenRouterResponseError("response id was already observed")
            metadata.update(
                {
                    "response_id": response_id,
                    "returned_model": returned_model,
                    "finish_reason": finish_reason,
                    "provider_attribution": (
                        "RESPONSE_ECHOED"
                        if returned_provider is not None
                        else "REQUEST_PINNED_ALLOW_FALLBACKS_FALSE"
                    ),
                }
            )
            serialized = json.dumps(metadata, sort_keys=True, allow_nan=False)
            if self._api_key in serialized:
                raise OpenRouterResponseError(
                    "safe response metadata contained credential material"
                )
            self._seen_response_ids.add(response_id)
            metadata["response_status"] = "ACCEPTED"
            return content
        except OpenRouterResponseError:
            metadata["response_status"] = "REJECTED_RESPONSE"
            raise

    def generate(self, request: Any, *, seed: int, call_id: str) -> str:
        """Execute one logical paid call and return validated response text."""

        resolved_call_id = _exact_text(
            call_id, "call_id", OpenRouterRequestError
        )
        with self._lock:
            self._last_call_metadata = None
            body = self._body(request, seed)
            http_request = self._http_request(body)
            if (
                resolved_call_id in self._completed_call_ids
                or resolved_call_id in self._reserved_call_ids
            ):
                raise OpenRouterRequestError("call_id was already paid or reserved")
            self._reserved_call_ids.add(resolved_call_id)
            if self._ledger is not None:
                try:
                    self._ledger.authorize_call(resolved_call_id)
                except Exception:
                    self._reserved_call_ids.discard(resolved_call_id)
                    raise
            try:
                raw, attempt_count = self._execute(http_request)
            except OpenRouterTransportError as exc:
                if exc.status_code == 429:
                    self._reserved_call_ids.discard(resolved_call_id)
                    if self._ledger is not None:
                        self._ledger.release_call(resolved_call_id)
                raise
            payload = _decode_object(
                raw, "OpenRouter completion response", OpenRouterResponseError
            )
            metadata = self._account_paid_response(
                payload,
                call_id=resolved_call_id,
                seed=seed,
                attempt_count=attempt_count,
            )
            return self._validate_response(payload, metadata)


def _catalog_response(
    request: urllib.request.Request,
    *,
    opener: Callable[..., Any],
    sleeper: Callable[[float], Any],
    timeout: float,
    max_attempts: int,
    retry_base_seconds: float,
) -> bytes:
    for attempt in range(1, max_attempts + 1):
        try:
            response = opener(request, timeout=timeout)
            status, raw = _read_http_response(response)
            if status == 200:
                return raw
            if status == 429 and attempt < max_attempts:
                sleeper(
                    min(
                        retry_base_seconds * (2 ** (attempt - 1)),
                        _MAX_RETRY_DELAY_SECONDS,
                    )
                )
                continue
            raise OpenRouterCatalogError(
                "OpenRouter endpoint catalog returned HTTP %d" % status
            )
        except urllib.error.HTTPError as error:
            if error.code == 429 and attempt < max_attempts:
                sleeper(
                    _retry_delay(
                        error,
                        retry_base_seconds * (2 ** (attempt - 1)),
                    )
                )
                continue
            raise OpenRouterCatalogError(
                "OpenRouter endpoint catalog returned HTTP %d" % error.code
            ) from None
        except (OpenRouterResponseError, OpenRouterTransportError):
            raise OpenRouterCatalogError(
                "OpenRouter endpoint catalog response envelope was invalid"
            ) from None
        except OpenRouterCatalogError:
            raise
        except (urllib.error.URLError, TimeoutError, OSError):
            raise OpenRouterCatalogError(
                "OpenRouter endpoint catalog transport failed"
            ) from None
    raise OpenRouterCatalogError("OpenRouter endpoint catalog retry loop failed")


def verify_model_routes(
    routes: Sequence[ModelRoute],
    *,
    api_key: Optional[str] = None,
    opener: Optional[Callable[..., Any]] = None,
    sleeper: Optional[Callable[[float], Any]] = None,
    timeout: float = 30.0,
    max_attempts: int = 3,
    retry_base_seconds: float = 1.0,
) -> CatalogVerification:
    """Verify one exact healthy endpoint for every frozen model route."""

    if not isinstance(routes, (list, tuple)) or not routes:
        raise OpenRouterCatalogError("model routes must be a nonempty sequence")
    frozen = tuple(routes)
    if any(type(row) is not ModelRoute for row in frozen):
        raise OpenRouterCatalogError("model routes must contain exact ModelRoute values")
    route_keys = tuple((row.model_id, row.provider, row.endpoint_name) for row in frozen)
    if len(set(route_keys)) != len(route_keys):
        raise OpenRouterCatalogError("model routes contain a duplicate exact endpoint")
    key = _resolve_api_key(api_key)
    transport = urllib.request.urlopen if opener is None else opener
    pause = time.sleep if sleeper is None else sleeper
    if not callable(transport) or not callable(pause):
        raise OpenRouterConfigurationError("catalog opener and sleeper must be callable")
    resolved_timeout = _bounded_number(timeout, "timeout", 0, 300)
    attempts = _bounded_int(max_attempts, "max_attempts", 1, _MAX_ATTEMPTS)
    retry_base = _retry_base(retry_base_seconds)

    for route in frozen:
        request = urllib.request.Request(
            MODEL_ENDPOINTS_URL % route.model_id,
            method="GET",
            headers={
                "Authorization": "Bearer " + key,
                "Accept": "application/json",
            },
        )
        raw = _catalog_response(
            request,
            opener=transport,
            sleeper=pause,
            timeout=resolved_timeout,
            max_attempts=attempts,
            retry_base_seconds=retry_base,
        )
        payload = _decode_object(
            raw,
            "OpenRouter endpoint catalog",
            OpenRouterCatalogError,
        )
        data = payload.get("data")
        endpoints = data.get("endpoints") if type(data) is dict else None
        if (
            type(data) is not dict
            or data.get("id") != route.model_id
            or type(endpoints) is not list
        ):
            raise OpenRouterCatalogError(
                "catalog endpoint model identity or list was invalid"
            )
        matches = []
        for endpoint in endpoints:
            if type(endpoint) is not dict:
                continue
            pricing = endpoint.get("pricing")
            parameters = endpoint.get("supported_parameters")
            if (
                endpoint.get("name") == route.endpoint_name
                and endpoint.get("provider_name") == route.provider
                and type(endpoint.get("status")) is int
                and endpoint["status"] == 0
                and type(pricing) is dict
                and pricing.get("prompt") == route.prompt_price_per_token_usd
                and pricing.get("completion")
                == route.completion_price_per_token_usd
                and type(parameters) is list
                and all(type(parameter) is str for parameter in parameters)
                and set(route.required_parameters).issubset(parameters)
            ):
                matches.append(endpoint)
        if len(matches) != 1:
            raise OpenRouterCatalogError(
                "catalog endpoint price, parameters, status, or identity changed"
            )
    return CatalogVerification(frozen)


__all__ = [
    "CHAT_COMPLETIONS_URL",
    "MAX_RESPONSE_BYTES",
    "MODEL_ENDPOINTS_URL",
    "OPENROUTER_API_KEY_ENV",
    "CatalogVerification",
    "ModelRoute",
    "OpenRouterCatalogError",
    "OpenRouterChatClient",
    "OpenRouterConfigurationError",
    "OpenRouterError",
    "OpenRouterRequestError",
    "OpenRouterResponseError",
    "OpenRouterTransportError",
    "verify_model_routes",
]
