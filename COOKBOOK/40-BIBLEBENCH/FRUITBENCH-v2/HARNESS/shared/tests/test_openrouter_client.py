from __future__ import annotations

import json
import sys
import threading
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Iterator

import pytest
from urllib.error import URLError


HARNESS = Path(__file__).resolve().parents[2]
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

from shared.openrouter_client import (  # noqa: E402
    ModelContract,
    OpenRouterClient,
    OpenRouterError,
    build_response_request,
    validate_catalog_contract,
)
import shared.openrouter_client as openrouter_client  # noqa: E402


SUBJECT_MODELS = (
    "openai/gpt-5.5",
    "openai/gpt-5.4",
    "openai/gpt-5.4-mini",
)

MESSAGES = [
    {"role": "system", "content": [{"type": "input_text", "text": "Be exact."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Fixture task."}]},
]

COMPLETED_RESPONSE = {
    "id": "resp_fixture",
    "model": "openai/gpt-5.5-20260423",
    "status": "completed",
    "output": [
        {
            "type": "message",
            "role": "assistant",
            "content": [{"type": "output_text", "text": "fixture answer"}],
        }
    ],
    "usage": {"input_tokens": 11, "output_tokens": 7, "total_tokens": 18},
}


class _FixtureHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler contract
        self._serve()

    def do_POST(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler contract
        self._serve()

    def _serve(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        self.server.requests.append(  # type: ignore[attr-defined]
            {
                "method": self.command,
                "path": self.path,
                "headers": dict(self.headers),
                "body": body,
            }
        )
        response = self.server.responses.pop(0)  # type: ignore[attr-defined]
        payload = response[1]
        if isinstance(payload, dict):
            encoded = json.dumps(payload).encode("utf-8")
        else:
            encoded = payload
        self.send_response(response[0])
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("X-Request-Id", "req_fixture")
        self.send_header("X-Generation-Id", "gen_fixture")
        self.send_header("X-OpenRouter-Provider", "openai")
        if len(response) == 3:
            for name, value in response[2].items():
                self.send_header(name, value)
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format: str, *args: object) -> None:
        return


@contextmanager
def _fixture_server(
    responses: list[
        tuple[int, dict[str, Any] | bytes]
        | tuple[int, dict[str, Any] | bytes, dict[str, str]]
    ],
) -> Iterator[tuple[str, ThreadingHTTPServer]]:
    server = ThreadingHTTPServer(("127.0.0.1", 0), _FixtureHandler)
    server.requests = []  # type: ignore[attr-defined]
    server.responses = list(responses)  # type: ignore[attr-defined]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        yield f"http://{host}:{port}/api/v1", server
    finally:
        server.shutdown()
        thread.join(timeout=2)
        server.server_close()


def _client(base_url: str, **overrides: Any) -> OpenRouterClient:
    return OpenRouterClient(
        api_key="fixture-secret",
        base_url=base_url,
        timeout=2.0,
        retry_backoff_seconds=0.0,
        **overrides,
    )


def _model(
    model_id: str,
    canonical_slug: str,
    *,
    supported_parameters: list[str] | None = None,
    supported_efforts: list[str] | None = None,
    expiration_date: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "id": model_id,
        "canonical_slug": canonical_slug,
        "supported_parameters": supported_parameters
        if supported_parameters is not None
        else ["reasoning", "max_tokens"],
        "expiration_date": expiration_date,
    }
    if supported_efforts is not None:
        record["reasoning"] = {"supported_efforts": supported_efforts}
    else:
        record["reasoning"] = {"supported_efforts": ["low", "medium", "high"]}
    return record


def test_subject_request_payloads_differ_only_by_model() -> None:
    payloads = [
        build_response_request(
            model_id=model,
            messages=MESSAGES,
            max_output_tokens=2048,
            reasoning_effort="medium",
            provider_order=["openai"],
        )
        for model in SUBJECT_MODELS
    ]

    assert [payload["model"] for payload in payloads] == list(SUBJECT_MODELS)
    for payload in payloads:
        assert payload["reasoning"] == {"effort": "medium"}
        assert payload["max_output_tokens"] == 2048
        assert payload["stream"] is False
        assert payload["store"] is False
        assert payload["service_tier"] == "default"
        assert payload["input"] == MESSAGES
        assert payload["provider"] == {
            "order": ["openai"],
            "allow_fallbacks": False,
            "require_parameters": True,
        }
        assert {**payload, "model": "same"} == {**payloads[0], "model": "same"}


def test_responses_posts_documented_shape_and_retains_provenance() -> None:
    with _fixture_server([(200, COMPLETED_RESPONSE)]) as (base_url, server):
        result = _client(base_url).responses(
            model_id=SUBJECT_MODELS[0],
            messages=MESSAGES,
            max_output_tokens=2048,
            reasoning_effort="medium",
            provider_order=["openai"],
            expected_canonical_slug="openai/gpt-5.5-20260423",
        )

    assert len(server.requests) == 1  # type: ignore[attr-defined]
    request = server.requests[0]  # type: ignore[attr-defined]
    assert request["method"] == "POST"
    assert request["path"] == "/api/v1/responses"
    assert request["headers"]["Authorization"] == "Bearer fixture-secret"
    assert request["headers"]["Content-Type"] == "application/json"
    request_headers = {key.casefold(): value for key, value in request["headers"].items()}
    assert request_headers["x-openrouter-metadata"] == "enabled"
    assert json.loads(request["body"]) == {
        "model": "openai/gpt-5.5",
        "input": MESSAGES,
        "max_output_tokens": 2048,
        "stream": False,
        "store": False,
        "service_tier": "default",
        "reasoning": {"effort": "medium"},
        "provider": {
            "order": ["openai"],
            "allow_fallbacks": False,
            "require_parameters": True,
        },
    }
    assert result.text == "fixture answer"
    assert result.response_id == "resp_fixture"
    assert result.requested_model == "openai/gpt-5.5"
    assert result.returned_model == "openai/gpt-5.5-20260423"
    assert result.request_id == "req_fixture"
    assert result.generation_id == "gen_fixture"
    assert result.router_metadata == {"x-openrouter-provider": "openai"}
    assert result.incomplete_details is None
    assert result.status == "completed"
    assert result.usage == {"input_tokens": 11, "output_tokens": 7, "total_tokens": 18}
    assert result.raw == COMPLETED_RESPONSE
    assert result.attempts == 1
    assert result.latency_ms >= 0


@pytest.mark.parametrize(
    ("payload", "error_type"),
    [
        ({**COMPLETED_RESPONSE, "status": "incomplete"}, "incomplete_response"),
        (
            {
                **COMPLETED_RESPONSE,
                "output": [
                    {
                        "type": "message",
                        "role": "assistant",
                        "content": [{"type": "refusal", "refusal": "no"}],
                    }
                ],
            },
            "schema_error",
        ),
        (
            {
                "error": {"code": 400, "message": "bad fixture request"},
                "error_type": "invalid_request",
            },
            "invalid_request",
        ),
    ],
)
def test_response_schema_and_error_envelopes_fail_without_retry(
    payload: dict[str, Any], error_type: str
) -> None:
    with _fixture_server([(200, payload)]) as (base_url, server):
        with pytest.raises(OpenRouterError) as caught:
            _client(base_url, max_retries=3).responses(
                model_id=SUBJECT_MODELS[0],
                messages=MESSAGES,
                max_output_tokens=2048,
                reasoning_effort="medium",
                provider_order=["openai"],
                expected_canonical_slug="openai/gpt-5.5-20260423",
            )

    assert caught.value.error_type == error_type
    assert caught.value.retryable is False
    assert caught.value.attempts == 1
    assert len(server.requests) == 1  # type: ignore[attr-defined]
    assert "fixture-secret" not in str(caught.value)


def test_malformed_json_fails_without_retry() -> None:
    with _fixture_server([(200, b"not-json")]) as (base_url, server):
        with pytest.raises(OpenRouterError) as caught:
            _client(base_url, max_retries=3).responses(
                model_id=SUBJECT_MODELS[0],
                messages=MESSAGES,
                max_output_tokens=2048,
                reasoning_effort="medium",
                provider_order=["openai"],
                expected_canonical_slug="openai/gpt-5.5-20260423",
            )

    assert caught.value.error_type == "malformed_json"
    assert caught.value.retryable is False
    assert caught.value.attempts == 1
    assert len(server.requests) == 1  # type: ignore[attr-defined]


def test_blank_key_is_a_typed_configuration_error() -> None:
    with pytest.raises(OpenRouterError) as caught:
        OpenRouterClient(api_key="   ")

    assert caught.value.error_type == "authentication_configuration_error"
    assert caught.value.attempts == 0
    assert caught.value.retryable is False


def test_authentication_error_fails_without_retry_and_never_exposes_key() -> None:
    error = {
        "error": {"code": 401, "message": "invalid credentials"},
        "error_type": "authentication_error",
    }
    with _fixture_server([(401, error)]) as (base_url, server):
        with pytest.raises(OpenRouterError) as caught:
            _client(base_url, max_retries=3).responses(
                model_id=SUBJECT_MODELS[0],
                messages=MESSAGES,
                max_output_tokens=2048,
                reasoning_effort="medium",
                provider_order=["openai"],
                expected_canonical_slug="openai/gpt-5.5-20260423",
            )

    assert caught.value.status_code == 401
    assert caught.value.error_type == "authentication_error"
    assert caught.value.retryable is False
    assert caught.value.attempts == 1
    assert len(server.requests) == 1  # type: ignore[attr-defined]
    assert "fixture-secret" not in repr(caught.value)


def test_429_and_503_retry_with_retry_after_and_a_bounded_attempt_count() -> None:
    retryable = {
        "error": {"code": 429, "message": "rate limited"},
        "error_type": "rate_limit_error",
    }
    overloaded = {
        "error": {"code": 503, "message": "provider unavailable"},
        "error_type": "provider_error",
    }
    delays: list[float] = []
    with _fixture_server(
        [
            (429, retryable, {"Retry-After": "0.25"}),
            (503, overloaded, {"Retry-After": "0.5"}),
            (200, COMPLETED_RESPONSE),
        ]
    ) as (base_url, server):
        result = _client(base_url, max_retries=2, sleeper=delays.append).responses(
            model_id=SUBJECT_MODELS[0],
            messages=MESSAGES,
            max_output_tokens=2048,
            reasoning_effort="medium",
            provider_order=["openai"],
            expected_canonical_slug="openai/gpt-5.5-20260423",
        )

    assert result.attempts == 3
    assert delays == [0.25, 0.5]
    assert len(server.requests) == 3  # type: ignore[attr-defined]


def test_top_level_authentication_error_never_retries_even_on_5xx() -> None:
    error = {
        "error": {"code": 500, "message": "do not retry this authentication failure"},
        "error_type": "authentication_error",
    }
    with _fixture_server([(500, error)]) as (base_url, server):
        with pytest.raises(OpenRouterError) as caught:
            _client(base_url, max_retries=3).responses(
                model_id=SUBJECT_MODELS[0],
                messages=MESSAGES,
                max_output_tokens=2048,
                reasoning_effort="medium",
                provider_order=["openai"],
                expected_canonical_slug="openai/gpt-5.5-20260423",
            )

    assert caught.value.error_type == "authentication_error"
    assert caught.value.retryable is False
    assert caught.value.attempts == 1
    assert len(server.requests) == 1  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    "error_type",
    ["rate_limit_exceeded", "provider_unavailable", "server", "unmapped"],
)
def test_canonical_retryable_error_retries_even_when_http_status_is_200(
    error_type: str,
) -> None:
    error = {
        "error": {"code": "server_error", "message": "rate limited"},
        "error_type": error_type,
    }
    delays: list[float] = []
    with _fixture_server([(200, error), (200, COMPLETED_RESPONSE)]) as (
        base_url,
        server,
    ):
        result = _client(
            base_url, max_retries=1, sleeper=delays.append
        ).responses(
            model_id=SUBJECT_MODELS[0],
            messages=MESSAGES,
            max_output_tokens=2048,
            reasoning_effort="medium",
            provider_order=["openai"],
            expected_canonical_slug="openai/gpt-5.5-20260423",
        )

    assert result.attempts == 2
    assert delays == [0.0]
    assert len(server.requests) == 2  # type: ignore[attr-defined]


def test_generic_network_error_is_not_retried(monkeypatch) -> None:
    attempts = 0
    delays: list[float] = []

    def fail_network(*_args, **_kwargs):
        nonlocal attempts
        attempts += 1
        raise URLError("fixture network failure")

    monkeypatch.setattr(openrouter_client, "urlopen", fail_network)
    with pytest.raises(OpenRouterError) as caught:
        OpenRouterClient(
            api_key="fixture-secret",
            max_retries=3,
            sleeper=delays.append,
        ).responses(
            model_id=SUBJECT_MODELS[0],
            messages=MESSAGES,
            max_output_tokens=2048,
            reasoning_effort="medium",
            provider_order=["openai"],
            expected_canonical_slug="openai/gpt-5.5-20260423",
        )

    assert caught.value.error_type == "network_error"
    assert caught.value.retryable is False
    assert caught.value.attempts == 1
    assert attempts == 1
    assert delays == []


def test_retry_budget_exhaustion_returns_typed_last_error() -> None:
    error = {
        "error": {"code": 500, "message": "fixture outage"},
        "error_type": "provider_error",
    }
    with _fixture_server([(500, error), (500, error), (500, error)]) as (
        base_url,
        server,
    ):
        with pytest.raises(OpenRouterError) as caught:
            _client(base_url, max_retries=2).responses(
                model_id=SUBJECT_MODELS[0],
                messages=MESSAGES,
                max_output_tokens=2048,
                reasoning_effort="medium",
                provider_order=["openai"],
                expected_canonical_slug="openai/gpt-5.5-20260423",
            )

    assert caught.value.status_code == 500
    assert caught.value.error_type == "provider_error"
    assert caught.value.retryable is True
    assert caught.value.attempts == 3
    assert len(server.requests) == 3  # type: ignore[attr-defined]


def test_fetch_catalog_uses_models_endpoint() -> None:
    catalog = {"data": [_model("openai/gpt-5.5", "openai/gpt-5.5-20260423")]}
    with _fixture_server([(200, catalog)]) as (base_url, server):
        result = _client(base_url).fetch_catalog()

    assert result == catalog
    assert server.requests[0]["method"] == "GET"  # type: ignore[attr-defined]
    assert server.requests[0]["path"] == "/api/v1/models"  # type: ignore[attr-defined]


def test_fetch_user_catalog_uses_authenticated_user_models_endpoint() -> None:
    catalog = {"data": [_model("openai/gpt-5.5", "openai/gpt-5.5-20260423")]}
    with _fixture_server([(200, catalog)]) as (base_url, server):
        result = _client(base_url).fetch_user_catalog()

    assert result == catalog
    assert server.requests[0]["method"] == "GET"  # type: ignore[attr-defined]
    assert server.requests[0]["path"] == "/api/v1/models/user"  # type: ignore[attr-defined]


def test_catalog_validation_returns_exact_canonical_slugs() -> None:
    catalog = {
        "data": [
            _model("openai/gpt-5.5", "openai/gpt-5.5-20260423"),
            _model("openai/gpt-5.4", "openai/gpt-5.4-20260305"),
            _model("openai/gpt-5.4-mini", "openai/gpt-5.4-mini-20260317"),
        ]
    }
    contracts = [
        ModelContract(
            model_id=model,
            required_parameters=("reasoning", "max_output_tokens"),
        )
        for model in SUBJECT_MODELS
    ]

    assert validate_catalog_contract(catalog, contracts) == {
        "openai/gpt-5.5": "openai/gpt-5.5-20260423",
        "openai/gpt-5.4": "openai/gpt-5.4-20260305",
        "openai/gpt-5.4-mini": "openai/gpt-5.4-mini-20260317",
    }


def test_returned_model_must_match_requested_alias_or_catalog_canonical_slug() -> None:
    wrong_model = {**COMPLETED_RESPONSE, "model": "openai/unrelated-model"}
    with _fixture_server([(200, wrong_model)]) as (base_url, server):
        with pytest.raises(OpenRouterError, match="returned model") as caught:
            _client(base_url).responses(
                model_id=SUBJECT_MODELS[0],
                messages=MESSAGES,
                max_output_tokens=2048,
                reasoning_effort="medium",
                provider_order=["openai"],
                expected_canonical_slug="openai/gpt-5.5-20260423",
            )

    assert caught.value.error_type == "model_mismatch"
    assert caught.value.retryable is False
    assert caught.value.attempts == 1
    assert len(server.requests) == 1  # type: ignore[attr-defined]


def test_returned_requested_alias_is_also_valid() -> None:
    alias_response = {**COMPLETED_RESPONSE, "model": SUBJECT_MODELS[0]}
    with _fixture_server([(200, alias_response)]) as (base_url, server):
        result = _client(base_url).responses(
            model_id=SUBJECT_MODELS[0],
            messages=MESSAGES,
            max_output_tokens=2048,
            reasoning_effort="medium",
            provider_order=["openai"],
            expected_canonical_slug="openai/gpt-5.5-20260423",
        )

    assert result.returned_model == SUBJECT_MODELS[0]
    assert len(server.requests) == 1  # type: ignore[attr-defined]


def test_responses_requires_a_catalog_bound_canonical_slug() -> None:
    with pytest.raises(TypeError, match="expected_canonical_slug"):
        _client("http://127.0.0.1:1/api/v1").responses(
            model_id=SUBJECT_MODELS[0],
            messages=MESSAGES,
            max_output_tokens=2048,
            reasoning_effort="medium",
            provider_order=["openai"],
        )


def test_model_contract_declares_responses_endpoint_for_online_preflight() -> None:
    contract = ModelContract(model_id=SUBJECT_MODELS[0])

    assert contract.api_endpoint == "responses"


def test_top_level_and_nested_output_text_must_agree() -> None:
    disagreement = {**COMPLETED_RESPONSE, "output_text": "different answer"}
    with _fixture_server([(200, disagreement)]) as (base_url, server):
        with pytest.raises(OpenRouterError) as caught:
            _client(base_url).responses(
                model_id=SUBJECT_MODELS[0],
                messages=MESSAGES,
                max_output_tokens=2048,
                reasoning_effort="medium",
                provider_order=["openai"],
                expected_canonical_slug="openai/gpt-5.5-20260423",
            )

    assert caught.value.error_type == "schema_error"
    assert caught.value.attempts == 1
    assert len(server.requests) == 1  # type: ignore[attr-defined]


def test_top_level_output_text_is_accepted_when_nested_text_is_absent() -> None:
    response = {
        **COMPLETED_RESPONSE,
        "output_text": "top-level answer",
        "output": [{"type": "reasoning", "summary": []}],
    }
    with _fixture_server([(200, response)]) as (base_url, _server):
        result = _client(base_url).responses(
            model_id=SUBJECT_MODELS[0],
            messages=MESSAGES,
            max_output_tokens=2048,
            reasoning_effort="medium",
            provider_order=["openai"],
            expected_canonical_slug="openai/gpt-5.5-20260423",
        )

    assert result.text == "top-level answer"


def test_null_supported_efforts_means_all_efforts_are_supported() -> None:
    model = _model("openai/gpt-5.5", "openai/gpt-5.5-20260423")
    model["reasoning"] = {"supported_efforts": None}

    assert validate_catalog_contract(
        {"data": [model]}, [ModelContract(model_id="openai/gpt-5.5")]
    ) == {"openai/gpt-5.5": "openai/gpt-5.5-20260423"}


@pytest.mark.parametrize(
    ("catalog", "contract", "message"),
    [
        (
            {"data": []},
            ModelContract(model_id="openai/gpt-5.5"),
            "missing",
        ),
        (
            {
                "data": [
                    _model(
                        "openai/gpt-5.5",
                        "openai/gpt-5.5-20260423",
                        expiration_date=(
                            datetime.now(timezone.utc) - timedelta(days=1)
                        ).isoformat(),
                    )
                ]
            },
            ModelContract(model_id="openai/gpt-5.5"),
            "expired",
        ),
        (
            {
                "data": [
                    _model(
                        "openai/gpt-5.5",
                        "openai/gpt-5.5-20260423",
                        supported_parameters=["max_tokens"],
                    )
                ]
            },
            ModelContract(model_id="openai/gpt-5.5"),
            "reasoning",
        ),
        (
            {
                "data": [
                    {
                        key: value
                        for key, value in _model(
                            "openai/gpt-5.5", "openai/gpt-5.5-20260423"
                        ).items()
                        if key != "reasoning"
                    }
                ]
            },
            ModelContract(model_id="openai/gpt-5.5"),
            "reasoning",
        ),
        (
            {
                "data": [
                    _model(
                        "openai/gpt-5.5",
                        "openai/gpt-5.5-20260423",
                        supported_efforts=["low", "high"],
                    )
                ]
            },
            ModelContract(model_id="openai/gpt-5.5"),
            "medium",
        ),
        (
            {
                "data": [
                    _model(
                        "openai/gpt-5.5",
                        "openai/gpt-5.5-20260423",
                        supported_parameters=["reasoning"],
                    )
                ]
            },
            ModelContract(
                model_id="openai/gpt-5.5",
                required_parameters=("reasoning", "temperature"),
            ),
            "temperature",
        ),
    ],
)
def test_catalog_validation_fails_closed(
    catalog: dict[str, Any], contract: ModelContract, message: str
) -> None:
    with pytest.raises(OpenRouterError, match=message) as caught:
        validate_catalog_contract(catalog, [contract])

    assert caught.value.error_type == "catalog_contract_error"
    assert caught.value.retryable is False
