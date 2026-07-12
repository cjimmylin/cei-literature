"""Minimal production OpenRouter transport for cheap public qualification.

The API key is accepted only from ``OPENROUTER_API_KEY`` in the process
environment.  It is used to construct the Authorization header at call time
and is never returned in an artifact-facing value.
"""
from __future__ import annotations

from copy import deepcopy
import json
import os
import urllib.error
import urllib.parse
import urllib.request

from . import contracts


CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
CATALOG_BASE_URL = "https://openrouter.ai/api/v1/models"
ZDR_CATALOG_URL = contracts.ZDR_CATALOG_URL
MAX_RESPONSE_BYTES = 16 * 1024 * 1024
HTTP_TIMEOUT_SECONDS = 300


class OpenRouterTransportError(RuntimeError):
    """A sanitized transport or provider-protocol failure."""


def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _strict_json(raw: bytes, label: str) -> dict:
    try:
        value = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=_unique_pairs,
            parse_constant=lambda _value: (_ for _ in ()).throw(ValueError()),
        )
    except (UnicodeError, json.JSONDecodeError, ValueError):
        raise OpenRouterTransportError(f"{label} was not strict JSON") from None
    if not isinstance(value, dict):
        raise OpenRouterTransportError(f"{label} was not a JSON object")
    contracts.assert_artifact_safe(value)
    return value


def _catalog_url(alias: str) -> str:
    if not isinstance(alias, str) or alias.count("/") != 1:
        raise ValueError("OpenRouter model alias must be author/model")
    author, model = alias.split("/", 1)
    if not author or not model:
        raise ValueError("OpenRouter model alias must be author/model")
    return (
        f"{CATALOG_BASE_URL}/{urllib.parse.quote(author, safe='')}/"
        f"{urllib.parse.quote(model, safe='')}/endpoints"
    )


def _catalog_evidence(model_payload: dict, zdr_payload: dict, model: dict) -> dict:
    """Bind raw model and ZDR catalogs for independently replayable validation."""
    evidence = {
        "catalog_evidence_version": contracts.CATALOG_EVIDENCE_VERSION,
        "model_id": model["alias"],
        "model_catalog_url": _catalog_url(model["alias"]),
        "zdr_catalog_url": ZDR_CATALOG_URL,
        "model_catalog_response": deepcopy(model_payload),
        "zdr_catalog_response": deepcopy(zdr_payload),
    }
    # This is the paid-call gate.  Endpoint-level ZDR is proven by exact
    # membership in OpenRouter's dedicated ZDR catalog, never inferred from an
    # absent field in the per-model response.
    contracts.validate_catalog(evidence, model)
    contracts.assert_artifact_safe(evidence)
    return evidence


class OpenRouterClient:
    """Non-retrying client preserving direct response and header evidence."""

    live_transport = True

    def __init__(self, *, environ=None, urlopen=None):
        environment = os.environ if environ is None else environ
        key = environment.get("OPENROUTER_API_KEY")
        if not isinstance(key, str) or not key.strip() or key != key.strip() or (
                "\n" in key or "\r" in key):
            raise ValueError("OPENROUTER_API_KEY is absent or invalid")
        self._api_key = key
        self._urlopen = urllib.request.urlopen if urlopen is None else urlopen

    def __repr__(self) -> str:
        return "OpenRouterClient(environment_credential=<redacted>)"

    def _headers(self, *, authorized: bool) -> dict:
        headers = {
            "Accept": "application/json",
            "User-Agent": "CROSSROADS-cheap-public-qualification/1",
        }
        if authorized:
            headers["Authorization"] = f"Bearer {self._api_key}"
            headers["Content-Type"] = "application/json"
            headers["X-OpenRouter-Metadata"] = "enabled"
        return headers

    @staticmethod
    def _response_header_values(headers, name: str) -> list[str]:
        if headers is None:
            return []
        if hasattr(headers, "get_all"):
            values = headers.get_all(name)
        else:
            value = headers.get(name) if hasattr(headers, "get") else None
            values = None if value is None else [value]
        if values is None:
            return []
        if not isinstance(values, list) or any(
            not isinstance(value, str) or not value or "\r" in value or "\n" in value
            for value in values
        ):
            raise OpenRouterTransportError("completion response header is invalid")
        return list(values)

    def _request(self, request: urllib.request.Request, *, label: str,
                 retry_statuses=()) -> tuple[int, dict | None, dict]:
        try:
            response = self._urlopen(request, timeout=HTTP_TIMEOUT_SECONDS)
            try:
                status = getattr(response, "status", None)
                if status is None:
                    status = response.getcode()
                response_headers = {
                    "x_generation_id": self._response_header_values(
                        getattr(response, "headers", None), "X-Generation-Id"
                    ),
                }
                raw = response.read(MAX_RESPONSE_BYTES + 1)
            finally:
                response.close()
        except urllib.error.HTTPError as error:
            status = error.code
            error.close()
            if status in retry_statuses:
                return status, None, {"x_generation_id": []}
            raise OpenRouterTransportError(f"{label} returned HTTP {status}") from None
        except (urllib.error.URLError, TimeoutError, OSError):
            raise OpenRouterTransportError(f"{label} transport failed") from None
        if len(raw) > MAX_RESPONSE_BYTES:
            raise OpenRouterTransportError(f"{label} exceeded response byte ceiling")
        if self._api_key.encode("utf-8") in raw:
            raise OpenRouterTransportError(f"{label} echoed credential material")
        if status in retry_statuses:
            return status, None, response_headers
        if status != 200:
            raise OpenRouterTransportError(f"{label} returned HTTP {status}")
        return status, _strict_json(raw, label), response_headers

    def catalog(self, alias: str) -> dict:
        model = contracts.resolve_model(alias)
        request = urllib.request.Request(
            _catalog_url(alias), headers=self._headers(authorized=False), method="GET"
        )
        _, model_payload, _ = self._request(
            request, label="OpenRouter model endpoint catalog"
        )
        zdr_request = urllib.request.Request(
            ZDR_CATALOG_URL, headers=self._headers(authorized=False), method="GET"
        )
        _, zdr_payload, _ = self._request(
            zdr_request, label="OpenRouter ZDR endpoint catalog"
        )
        return _catalog_evidence(model_payload, zdr_payload, model)

    def complete(self, body: dict) -> dict:
        if not isinstance(body, dict):
            raise ValueError("OpenRouter completion body must be an object")
        model = contracts.resolve_model(body.get("model"))
        if body.get("provider") != model["routing"]:
            raise ValueError("OpenRouter completion routing differs from frozen profile")
        if body.get("usage") != {"include": True}:
            raise ValueError("OpenRouter completion must request usage/cost evidence")
        parameter_keys = set(body) - {"model", "messages", "provider", "usage"}
        if not parameter_keys <= set(contracts.REQUIRED_PARAMETERS):
            raise ValueError(
                "OpenRouter completion parameters must be catalog-declared"
            )
        contracts.assert_artifact_safe(body)
        wire = contracts.canonical_bytes(body)
        request = urllib.request.Request(
            CHAT_URL, data=wire, headers=self._headers(authorized=True), method="POST"
        )
        _, response, response_headers = self._request(
            request, label="OpenRouter completion"
        )
        request_id = response.get("id")
        if not isinstance(request_id, str) or not request_id:
            raise OpenRouterTransportError("completion response lacks request identity")
        result = {
            "response": response,
            "response_headers": response_headers,
        }
        contracts.assert_artifact_safe(result)
        return result
