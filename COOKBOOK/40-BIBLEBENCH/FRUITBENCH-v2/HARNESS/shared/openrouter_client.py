"""Fail-loud OpenRouter Responses transport and catalog contracts.

The client intentionally uses only the Python standard library.  It freezes the
request controls needed for comparative benchmark runs, exposes routing
provenance, and treats malformed or ambiguous responses as invalid evidence.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any, Callable, Mapping, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_SERVICE_TIER = "default"
_PARAMETER_ALIASES = {
    "max_output_tokens": ("max_tokens", "max_completion_tokens"),
}
_NON_RETRYABLE_ERROR_FRAGMENTS = (
    "auth",
    "permission",
    "billing",
    "payment",
    "invalid",
    "schema",
    "malformed",
    "moderation",
    "policy",
    "not_found",
)
_RETRYABLE_ERROR_FRAGMENTS = (
    "rate_limit",
    "provider",
    "overload",
    "server_error",
    "upstream",
    "timeout",
)


class OpenRouterError(RuntimeError):
    """Typed OpenRouter failure with no secret-bearing request representation."""

    def __init__(
        self,
        message: str,
        *,
        error_type: str,
        status_code: int | None = None,
        api_code: Any = None,
        response_id: str | None = None,
        generation_id: str | None = None,
        retryable: bool = False,
        retry_after_seconds: float | None = None,
        attempts: int = 0,
        raw: Any = None,
        incomplete_details: Any = None,
    ) -> None:
        super().__init__(message)
        self.error_type = error_type
        self.status_code = status_code
        self.http_status = status_code
        self.api_code = api_code
        self.response_id = response_id
        self.generation_id = generation_id
        self.retryable = retryable
        self.retry_after_seconds = retry_after_seconds
        self.attempts = attempts
        self.raw = raw
        self.incomplete_details = incomplete_details

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(error_type={self.error_type!r}, "
            f"status_code={self.status_code!r}, retryable={self.retryable!r}, "
            f"attempts={self.attempts!r})"
        )


@dataclass(frozen=True)
class ModelContract:
    """Capabilities a model must expose before it can enter a live roster."""

    model_id: str
    required_parameters: tuple[str, ...] = ("reasoning",)
    reasoning_effort: str | None = "medium"
    api_endpoint: str = "responses"
    expected_canonical_slug: str | None = None
    max_output_tokens: int | None = None


@dataclass(frozen=True)
class ResponseResult:
    """Completed response plus the provenance required for an evidence row."""

    text: str
    response_id: str
    requested_model: str
    returned_model: str
    status: str
    usage: dict[str, Any]
    raw: dict[str, Any]
    request_id: str | None
    generation_id: str | None
    router_metadata: dict[str, Any]
    incomplete_details: Any
    attempts: int
    latency_ms: float
    service_tier: str = DEFAULT_SERVICE_TIER


def _configuration_error(message: str) -> OpenRouterError:
    return OpenRouterError(
        message,
        error_type="authentication_configuration_error",
        retryable=False,
        attempts=0,
    )


def _validate_messages(messages: Sequence[Mapping[str, Any]]) -> None:
    if not isinstance(messages, (list, tuple)) or not messages:
        raise ValueError("messages must be a non-empty sequence")
    allowed_roles = {"system", "developer", "user", "assistant"}
    for index, message in enumerate(messages):
        if not isinstance(message, Mapping):
            raise ValueError(f"message {index} must be an object")
        if message.get("role") not in allowed_roles:
            raise ValueError(f"message {index} has an invalid role")
        content = message.get("content")
        if isinstance(content, str):
            if not content.strip():
                raise ValueError(f"message {index} has blank content")
            continue
        if not isinstance(content, list) or not content:
            raise ValueError(f"message {index} content must be text or a non-empty list")
        for part_index, part in enumerate(content):
            if not isinstance(part, Mapping) or not str(part.get("type", "")).strip():
                raise ValueError(
                    f"message {index} content part {part_index} must have a type"
                )


def build_response_request(
    *,
    model_id: str,
    messages: list[dict[str, Any]],
    max_output_tokens: int,
    reasoning_effort: str | None,
    provider_order: Sequence[str] | None = None,
    service_tier: str = DEFAULT_SERVICE_TIER,
) -> dict[str, Any]:
    """Build the frozen non-streaming Responses request used by benchmark actors."""

    if not isinstance(model_id, str) or not model_id.strip() or "/" not in model_id:
        raise ValueError("model_id must be an exact author/model identifier")
    _validate_messages(messages)
    if isinstance(max_output_tokens, bool) or not isinstance(max_output_tokens, int):
        raise ValueError("max_output_tokens must be a positive integer")
    if max_output_tokens <= 0:
        raise ValueError("max_output_tokens must be a positive integer")
    if reasoning_effort is not None and (
        not isinstance(reasoning_effort, str) or not reasoning_effort.strip()
    ):
        raise ValueError("reasoning_effort must be non-blank or None")
    if not isinstance(service_tier, str) or not service_tier.strip():
        raise ValueError("service_tier must be non-blank")

    order = list(provider_order or [model_id.split("/", 1)[0]])
    if not order or any(not isinstance(value, str) or not value.strip() for value in order):
        raise ValueError("provider_order must contain non-blank provider identifiers")

    payload: dict[str, Any] = {
        "model": model_id,
        "input": messages,
        "max_output_tokens": max_output_tokens,
        "stream": False,
        "store": False,
        "service_tier": service_tier,
    }
    if reasoning_effort is not None:
        payload["reasoning"] = {"effort": reasoning_effort}
    payload["provider"] = {
        "order": order,
        "allow_fallbacks": False,
        "require_parameters": True,
    }
    return payload


def _catalog_error(message: str) -> OpenRouterError:
    return OpenRouterError(
        message,
        error_type="catalog_contract_error",
        retryable=False,
        attempts=0,
    )


def _parse_expiration(value: Any, model_id: str) -> datetime | None:
    if value in (None, ""):
        return None
    if not isinstance(value, str):
        raise _catalog_error(f"{model_id} expiration_date is malformed")
    candidate = value.strip()
    try:
        if candidate.endswith("Z"):
            candidate = candidate[:-1] + "+00:00"
        parsed = datetime.fromisoformat(candidate)
    except ValueError as exc:
        raise _catalog_error(f"{model_id} expiration_date is malformed") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _parameter_supported(required: str, advertised: set[str]) -> bool:
    alternatives = _PARAMETER_ALIASES.get(required, (required,))
    return any(name in advertised for name in alternatives)


def validate_catalog_contract(
    catalog: dict[str, Any],
    contracts: Sequence[ModelContract],
    *,
    now: datetime | None = None,
) -> dict[str, str]:
    """Fail closed unless every exact model satisfies its declared contract."""

    if not isinstance(catalog, dict) or not isinstance(catalog.get("data"), list):
        raise _catalog_error("catalog is missing a data list")
    records: dict[str, list[dict[str, Any]]] = {}
    for raw in catalog["data"]:
        if isinstance(raw, dict) and isinstance(raw.get("id"), str):
            records.setdefault(raw["id"], []).append(raw)
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    current = current.astimezone(timezone.utc)

    resolved: dict[str, str] = {}
    for contract in contracts:
        if not isinstance(contract.model_id, str) or not contract.model_id.strip():
            raise _catalog_error("contract has a missing model_id")
        matches = records.get(contract.model_id, [])
        if not matches:
            raise _catalog_error(f"model {contract.model_id} is missing from catalog")
        if len(matches) != 1:
            raise _catalog_error(f"model {contract.model_id} has duplicate catalog records")
        model = matches[0]

        expires = _parse_expiration(model.get("expiration_date"), contract.model_id)
        if expires is not None and expires <= current:
            raise _catalog_error(f"model {contract.model_id} is expired")

        supported_raw = model.get("supported_parameters")
        if not isinstance(supported_raw, list) or any(
            not isinstance(value, str) for value in supported_raw
        ):
            raise _catalog_error(
                f"model {contract.model_id} has malformed supported_parameters"
            )
        supported = set(supported_raw)
        for required in contract.required_parameters:
            if not _parameter_supported(required, supported):
                raise _catalog_error(
                    f"model {contract.model_id} does not support {required}"
                )

        if contract.reasoning_effort is not None:
            reasoning = model.get("reasoning")
            if not isinstance(reasoning, dict) or "supported_efforts" not in reasoning:
                raise _catalog_error(
                    f"model {contract.model_id} does not expose reasoning efforts"
                )
            efforts = reasoning["supported_efforts"]
            if efforts is not None:
                if not isinstance(efforts, list) or any(
                    not isinstance(value, str) for value in efforts
                ):
                    raise _catalog_error(
                        f"model {contract.model_id} has malformed reasoning efforts"
                    )
                if contract.reasoning_effort not in efforts:
                    raise _catalog_error(
                        f"model {contract.model_id} does not support "
                        f"{contract.reasoning_effort} reasoning"
                    )

        canonical = model.get("canonical_slug")
        if not isinstance(canonical, str) or not canonical.strip():
            raise _catalog_error(
                f"model {contract.model_id} has a missing canonical_slug"
            )
        if (
            contract.expected_canonical_slug is not None
            and canonical != contract.expected_canonical_slug
        ):
            raise _catalog_error(
                f"model {contract.model_id} canonical slug changed: {canonical}"
            )
        resolved[contract.model_id] = canonical
    return resolved


def _header(headers: Mapping[str, Any], name: str) -> str | None:
    wanted = name.casefold()
    for key, value in headers.items():
        if str(key).casefold() == wanted:
            return str(value)
    return None


def _retry_after_seconds(headers: Mapping[str, Any]) -> float | None:
    raw = _header(headers, "Retry-After")
    if raw is None:
        return None
    try:
        return max(0.0, float(raw))
    except ValueError:
        try:
            retry_at = parsedate_to_datetime(raw)
        except (TypeError, ValueError):
            return None
        if retry_at.tzinfo is None:
            retry_at = retry_at.replace(tzinfo=timezone.utc)
        return max(
            0.0,
            (retry_at.astimezone(timezone.utc) - datetime.now(timezone.utc)).total_seconds(),
        )


def _decode_json(body: bytes, *, attempts: int, status_code: int | None) -> Any:
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise OpenRouterError(
            "OpenRouter returned malformed JSON",
            error_type="malformed_json",
            status_code=status_code,
            retryable=False,
            attempts=attempts,
        ) from exc


def _error_details(
    payload: Any,
    *,
    status_code: int | None,
    headers: Mapping[str, Any],
    attempts: int,
) -> OpenRouterError:
    raw = payload if isinstance(payload, dict) else None
    envelope = payload.get("error") if isinstance(payload, dict) else None
    if not isinstance(envelope, dict):
        envelope = {}
    error_type = (
        payload.get("error_type")
        if isinstance(payload, dict) and isinstance(payload.get("error_type"), str)
        else "http_error"
    )
    message = envelope.get("message")
    if not isinstance(message, str) or not message.strip():
        message = f"OpenRouter request failed ({error_type})"
    lowered = error_type.casefold()
    retryable = bool(
        status_code == 429
        or (status_code is not None and status_code >= 500)
        or any(fragment in lowered for fragment in _RETRYABLE_ERROR_FRAGMENTS)
    )
    if any(fragment in lowered for fragment in _NON_RETRYABLE_ERROR_FRAGMENTS):
        retryable = False
    if status_code in {400, 401, 402, 403, 404, 405, 409, 422}:
        retryable = False
    return OpenRouterError(
        message,
        error_type=error_type,
        status_code=status_code,
        api_code=envelope.get("code"),
        response_id=(
            payload.get("id")
            if isinstance(payload, dict) and isinstance(payload.get("id"), str)
            else None
        ),
        generation_id=_header(headers, "X-Generation-Id"),
        retryable=retryable,
        retry_after_seconds=_retry_after_seconds(headers),
        attempts=attempts,
        raw=raw,
        incomplete_details=(
            payload.get("incomplete_details") if isinstance(payload, dict) else None
        ),
    )


def _extract_text(payload: dict[str, Any], *, attempts: int) -> str:
    nested_parts: list[str] = []
    output = payload.get("output")
    if output is not None:
        if not isinstance(output, list):
            raise OpenRouterError(
                "response output must be a list",
                error_type="schema_error",
                retryable=False,
                attempts=attempts,
                raw=payload,
            )
        for item in output:
            if not isinstance(item, dict):
                raise OpenRouterError(
                    "response output contains a malformed item",
                    error_type="schema_error",
                    retryable=False,
                    attempts=attempts,
                    raw=payload,
                )
            if item.get("type") == "reasoning":
                continue
            content = item.get("content")
            if content is None:
                continue
            if not isinstance(content, list):
                raise OpenRouterError(
                    "response message content must be a list",
                    error_type="schema_error",
                    retryable=False,
                    attempts=attempts,
                    raw=payload,
                )
            for part in content:
                if (
                    isinstance(part, dict)
                    and part.get("type") == "output_text"
                    and isinstance(part.get("text"), str)
                ):
                    nested_parts.append(part["text"])
    nested = "".join(nested_parts) if nested_parts else None
    top = payload.get("output_text")
    if top is not None and not isinstance(top, str):
        raise OpenRouterError(
            "top-level output_text must be text",
            error_type="schema_error",
            retryable=False,
            attempts=attempts,
            raw=payload,
        )
    if isinstance(top, str) and nested is not None and top != nested:
        raise OpenRouterError(
            "top-level and nested output text disagree",
            error_type="schema_error",
            retryable=False,
            attempts=attempts,
            raw=payload,
        )
    text = top if isinstance(top, str) else nested
    if not isinstance(text, str) or not text.strip():
        raise OpenRouterError(
            "completed response contains no output text",
            error_type="schema_error",
            retryable=False,
            attempts=attempts,
            raw=payload,
        )
    return text


class OpenRouterClient:
    """Small synchronous client with explicit retries and provenance capture."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 60.0,
        max_retries: int = 2,
        retry_backoff_seconds: float = 1.0,
        sleeper: Callable[[float], Any] = time.sleep,
        app_title: str | None = None,
        app_referer: str | None = None,
    ) -> None:
        key = api_key if api_key is not None else os.environ.get("OPENROUTER_API_KEY")
        if not isinstance(key, str) or not key.strip():
            raise _configuration_error(
                "OPENROUTER_API_KEY is missing or blank; no request was made"
            )
        if not isinstance(base_url, str) or not base_url.strip():
            raise ValueError("base_url must be non-blank")
        if timeout <= 0:
            raise ValueError("timeout must be positive")
        if isinstance(max_retries, bool) or not isinstance(max_retries, int):
            raise ValueError("max_retries must be a non-negative integer")
        if max_retries < 0:
            raise ValueError("max_retries must be a non-negative integer")
        if retry_backoff_seconds < 0:
            raise ValueError("retry_backoff_seconds must be non-negative")

        self._api_key = key.strip()
        self.base_url = base_url.rstrip("/")
        self.timeout = float(timeout)
        self.max_retries = max_retries
        self.retry_backoff_seconds = float(retry_backoff_seconds)
        self._sleeper = sleeper
        self._app_title = app_title
        self._app_referer = app_referer

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(base_url={self.base_url!r}, "
            f"timeout={self.timeout!r}, max_retries={self.max_retries!r})"
        )

    def _headers(self, *, has_body: bool) -> dict[str, str]:
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Accept": "application/json",
            "X-OpenRouter-Metadata": "enabled",
        }
        if has_body:
            headers["Content-Type"] = "application/json"
        if self._app_title:
            headers["X-Title"] = self._app_title
        if self._app_referer:
            headers["HTTP-Referer"] = self._app_referer
        return headers

    def _request_json(
        self,
        method: str,
        path: str,
        *,
        payload: dict[str, Any] | None = None,
    ) -> tuple[dict[str, Any], dict[str, str], int, float]:
        encoded = (
            json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
            if payload is not None
            else None
        )
        started = time.monotonic()
        for attempt in range(1, self.max_retries + 2):
            request = Request(
                f"{self.base_url}{path}",
                data=encoded,
                method=method,
                headers=self._headers(has_body=payload is not None),
            )
            try:
                with urlopen(request, timeout=self.timeout) as response:
                    body = response.read()
                    headers = {key: value for key, value in response.headers.items()}
                    status_code = int(response.status)
            except HTTPError as exc:
                body = exc.read()
                headers = {key: value for key, value in exc.headers.items()}
                status_code = int(exc.code)
            except URLError as exc:
                error = OpenRouterError(
                    "OpenRouter network request failed",
                    error_type="network_error",
                    retryable=False,
                    attempts=attempt,
                )
                raise error from exc

            decoded = _decode_json(
                body, attempts=attempt, status_code=status_code
            )
            if not isinstance(decoded, dict):
                raise OpenRouterError(
                    "OpenRouter response must be a JSON object",
                    error_type="schema_error",
                    status_code=status_code,
                    retryable=False,
                    attempts=attempt,
                )
            has_error = isinstance(decoded.get("error"), dict)
            if status_code >= 400 or has_error:
                error = _error_details(
                    decoded,
                    status_code=status_code,
                    headers=headers,
                    attempts=attempt,
                )
                if error.retryable and attempt <= self.max_retries:
                    delay = (
                        error.retry_after_seconds
                        if error.retry_after_seconds is not None
                        else self.retry_backoff_seconds * attempt
                    )
                    self._sleeper(delay)
                    continue
                raise error
            elapsed_ms = (time.monotonic() - started) * 1000.0
            return decoded, headers, attempt, elapsed_ms

        raise AssertionError("unreachable retry loop")

    def responses(
        self,
        *,
        model_id: str,
        messages: list[dict[str, Any]],
        max_output_tokens: int,
        reasoning_effort: str | None,
        provider_order: Sequence[str] | None = None,
        expected_canonical_slug: str,
        service_tier: str = DEFAULT_SERVICE_TIER,
    ) -> ResponseResult:
        if (
            not isinstance(expected_canonical_slug, str)
            or not expected_canonical_slug.strip()
        ):
            raise ValueError(
                "expected_canonical_slug must be bound from a validated catalog"
            )
        request_payload = build_response_request(
            model_id=model_id,
            messages=messages,
            max_output_tokens=max_output_tokens,
            reasoning_effort=reasoning_effort,
            provider_order=provider_order,
            service_tier=service_tier,
        )
        payload, headers, attempts, latency_ms = self._request_json(
            "POST", "/responses", payload=request_payload
        )

        if isinstance(payload.get("error"), dict):
            raise _error_details(
                payload, status_code=200, headers=headers, attempts=attempts
            )
        status = payload.get("status")
        incomplete_details = payload.get("incomplete_details")
        if status != "completed":
            error_type = (
                "incomplete_response"
                if status == "incomplete"
                else (
                    payload.get("error_type")
                    if isinstance(payload.get("error_type"), str)
                    else "failed_response"
                )
            )
            raise OpenRouterError(
                f"OpenRouter response status is {status!r}",
                error_type=error_type,
                status_code=200,
                response_id=(
                    payload.get("id") if isinstance(payload.get("id"), str) else None
                ),
                generation_id=_header(headers, "X-Generation-Id"),
                retryable=False,
                attempts=attempts,
                raw=payload,
                incomplete_details=incomplete_details,
            )

        response_id = payload.get("id")
        returned_model = payload.get("model")
        usage = payload.get("usage")
        if not isinstance(response_id, str) or not response_id.strip():
            raise OpenRouterError(
                "completed response has a missing id",
                error_type="schema_error",
                retryable=False,
                attempts=attempts,
                raw=payload,
            )
        if not isinstance(returned_model, str) or not returned_model.strip():
            raise OpenRouterError(
                "completed response has a missing model",
                error_type="schema_error",
                retryable=False,
                attempts=attempts,
                raw=payload,
            )
        if not isinstance(usage, dict):
            raise OpenRouterError(
                "completed response has malformed usage",
                error_type="schema_error",
                retryable=False,
                attempts=attempts,
                raw=payload,
            )
        allowed_models = {model_id}
        allowed_models.add(expected_canonical_slug)
        if returned_model not in allowed_models:
            raise OpenRouterError(
                f"returned model {returned_model!r} does not match the frozen request",
                error_type="model_mismatch",
                retryable=False,
                attempts=attempts,
                response_id=response_id,
                generation_id=_header(headers, "X-Generation-Id"),
                raw=payload,
            )
        text = _extract_text(payload, attempts=attempts)

        metadata: dict[str, Any] = {}
        body_metadata = payload.get("openrouter_metadata")
        if isinstance(body_metadata, dict):
            metadata.update(body_metadata)
        for key, value in headers.items():
            lowered = key.casefold()
            if lowered.startswith("x-openrouter-"):
                metadata[lowered] = value

        return ResponseResult(
            text=text,
            response_id=response_id,
            requested_model=model_id,
            returned_model=returned_model,
            status=status,
            usage=dict(usage),
            raw=payload,
            request_id=_header(headers, "X-Request-Id"),
            generation_id=_header(headers, "X-Generation-Id"),
            router_metadata=metadata,
            incomplete_details=incomplete_details,
            attempts=attempts,
            latency_ms=latency_ms,
            service_tier=service_tier,
        )

    def fetch_catalog(self) -> dict[str, Any]:
        payload, _headers, _attempts, _latency = self._request_json("GET", "/models")
        return payload

    def fetch_user_catalog(self) -> dict[str, Any]:
        payload, _headers, _attempts, _latency = self._request_json(
            "GET", "/models/user"
        )
        return payload

    def fetch_endpoints(self, model_id: str) -> dict[str, Any]:
        if not isinstance(model_id, str) or "/" not in model_id:
            raise ValueError("model_id must be an exact author/model identifier")
        path = "/models/" + quote(model_id, safe="/") + "/endpoints"
        payload, _headers, _attempts, _latency = self._request_json("GET", path)
        return payload
