"""Mocked contract tests for the ZEROSUM-local OpenRouter adapter.

No test in this module makes a network call or performs a real sleep.
"""

from copy import deepcopy
import io
import json
from pathlib import Path
import sys
import urllib.error

import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CANONICAL_MODEL_IDS = {
    "openai/gpt-5.5": "openai/gpt-5.5-20260423",
    "openai/gpt-5.4": "openai/gpt-5.4-20260305",
    "openai/gpt-5.4-mini": "openai/gpt-5.4-mini-20260317",
}
REQUIRED_SUPPORTED_PARAMETERS = [
    "reasoning_effort", "max_tokens", "response_format", "seed"
]


class _Response:
    def __init__(self, payload, *, raw=False):
        if raw:
            self._body = payload
        else:
            self._body = json.dumps(payload).encode("utf-8")

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


def _completion(
    content="model answer",
    *,
    response_id="generation-123",
    model="openai/gpt-5.5",
    finish_reason="stop",
    usage=None,
):
    return {
        "id": response_id,
        "model": model,
        "choices": [
            {
                "finish_reason": finish_reason,
                "message": {"role": "assistant", "content": content},
            }
        ],
        "usage": usage
        or {"prompt_tokens": 31, "completion_tokens": 7, "total_tokens": 38},
    }


def _http_error(code, *, headers=None):
    return urllib.error.HTTPError(
        url="https://openrouter.ai/api/v1/chat/completions",
        code=code,
        msg="test transport error",
        hdrs=headers,
        fp=io.BytesIO(b'{"error":"sanitized test failure"}'),
    )


def test_generate_sends_bounded_canonical_payload_without_mutating_request():
    from harness.openrouter_client import CHAT_COMPLETIONS_URL, OpenRouterClient

    captured = []

    def opener(http_request, timeout):
        captured.append((http_request, timeout))
        return _Response(_completion())

    canonical_request = {
        "request_id": "zs-001--t0--seed-17",
        "messages": [{"role": "user", "content": "Choose a prudent action."}],
        "response_format": {"type": "text"},
    }
    original = deepcopy(canonical_request)
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test-explicit",
        max_tokens=2048,
        timeout=19.0,
        opener=opener,
    )

    assert client.generate(canonical_request, seed=17) == "model answer"
    assert canonical_request == original
    assert len(captured) == 1
    http_request, timeout = captured[0]
    assert http_request.full_url == CHAT_COMPLETIONS_URL
    assert http_request.get_method() == "POST"
    assert timeout == 19.0
    assert http_request.get_header("Authorization") == "Bearer sk-test-explicit"
    assert http_request.get_header("Content-type") == "application/json"
    assert json.loads(http_request.data.decode("utf-8")) == {
        "model": "openai/gpt-5.5",
        "messages": [{"role": "user", "content": "Choose a prudent action."}],
        "seed": 17,
        "max_tokens": 2048,
        "response_format": {"type": "text"},
    }


def test_reasoning_effort_minimal_is_optional_and_added_only_when_configured():
    from harness.openrouter_client import OpenRouterClient

    bodies = []

    def opener(http_request, timeout):
        del timeout
        bodies.append(json.loads(http_request.data.decode("utf-8")))
        return _Response(_completion())

    OpenRouterClient(
        "openai/gpt-5.5", api_key="sk-test", opener=opener
    ).generate({"messages": [{"role": "user", "content": "v1"}]}, seed=1)
    OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        reasoning_effort="minimal",
        max_tokens=1024,
        opener=opener,
    ).generate({"messages": [{"role": "user", "content": "r2"}]}, seed=1)

    assert "reasoning_effort" not in bodies[0]
    assert bodies[1]["reasoning_effort"] == "minimal"
    assert bodies[1]["max_tokens"] == 1024


@pytest.mark.parametrize("reasoning_effort", ["", "low", " minimal ", True, 1])
def test_invalid_or_unsupported_reasoning_effort_fails_before_transport(
    reasoning_effort,
):
    from harness.openrouter_client import (
        OpenRouterClient,
        OpenRouterConfigurationError,
    )

    called = []
    with pytest.raises(OpenRouterConfigurationError, match="reasoning_effort"):
        OpenRouterClient(
            "openai/gpt-5.5",
            api_key="sk-test",
            reasoning_effort=reasoning_effort,
            opener=lambda request, timeout: called.append(request),
        )
    assert called == []


def test_generate_records_only_safe_response_metadata():
    from harness.openrouter_client import OpenRouterClient

    secret = "sk-never-disclose-this"
    prompt = "private prompt must not enter metadata"
    usage = {
        "prompt_tokens": 11,
        "completion_tokens": 5,
        "total_tokens": 16,
        "cost": 0.001,
        "is_byok": False,
        "prompt": prompt,
    }

    def opener(http_request, timeout):
        del http_request, timeout
        return _Response(_completion(usage=usage))

    client = OpenRouterClient("openai/gpt-5.5", api_key=secret, opener=opener)
    client.generate(
        {"messages": [{"role": "user", "content": prompt}]}, seed=91
    )
    metadata = client.last_call_metadata
    assert metadata == {
        "response_id": "generation-123",
        "model": "openai/gpt-5.5",
        "finish_reason": "stop",
        "usage": {
            "prompt_tokens": 11,
            "completion_tokens": 5,
            "total_tokens": 16,
            "cost": 0.001,
            "is_byok": False,
        },
        "requested_seed": 91,
        "attempt_count": 1,
    }
    serialized = json.dumps(metadata, sort_keys=True)
    assert secret not in serialized
    assert prompt not in serialized
    assert secret not in repr(client)


def test_explicit_key_takes_precedence_and_environment_key_is_supported(monkeypatch):
    from harness.openrouter_client import OpenRouterClient

    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-from-environment")
    headers = []

    def opener(http_request, timeout):
        del timeout
        headers.append(http_request.get_header("Authorization"))
        return _Response(_completion())

    OpenRouterClient(
        "openai/gpt-5.5", api_key="sk-explicit", opener=opener
    ).generate({"messages": [{"role": "user", "content": "one"}]}, seed=1)
    OpenRouterClient("openai/gpt-5.5", opener=opener).generate(
        {"messages": [{"role": "user", "content": "two"}]}, seed=2
    )
    assert headers == ["Bearer sk-explicit", "Bearer sk-from-environment"]


def test_missing_or_blank_api_key_fails_before_transport(monkeypatch):
    from harness.openrouter_client import OpenRouterConfigurationError, OpenRouterClient

    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    called = []

    def opener(http_request, timeout):
        called.append((http_request, timeout))
        return _Response(_completion())

    for explicit in (None, "", "   "):
        with pytest.raises(OpenRouterConfigurationError, match="OPENROUTER_API_KEY"):
            OpenRouterClient(
                "openai/gpt-5.5", api_key=explicit, opener=opener
            )
    assert called == []


@pytest.mark.parametrize(
    "credential",
    [" sk-leading", "sk-trailing ", "sk\nnewline", "sk\x00control"],
)
def test_api_key_rejects_header_unsafe_whitespace_and_controls(credential):
    from harness.openrouter_client import OpenRouterConfigurationError, OpenRouterClient

    with pytest.raises(OpenRouterConfigurationError, match="OPENROUTER_API_KEY"):
        OpenRouterClient("openai/gpt-5.5", api_key=credential)


@pytest.mark.parametrize("status", [429, 500, 503, 599])
def test_retryable_http_statuses_use_bounded_retry(status):
    from harness.openrouter_client import OpenRouterClient

    attempts = []
    sleeps = []

    def opener(http_request, timeout):
        del http_request, timeout
        attempts.append(status)
        if len(attempts) < 3:
            raise _http_error(status)
        return _Response(_completion())

    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        max_attempts=3,
        retry_base_seconds=0.25,
        opener=opener,
        sleeper=sleeps.append,
    )
    assert client.generate(
        {"messages": [{"role": "user", "content": "retry"}]}, seed=22
    ) == "model answer"
    assert len(attempts) == 3
    assert sleeps == [0.25, 0.5]
    assert client.last_call_metadata["attempt_count"] == 3


@pytest.mark.parametrize("status", [400, 401, 403, 404, 422])
def test_non_retryable_4xx_fails_once_without_disclosing_secret(status):
    from harness.openrouter_client import OpenRouterClient, OpenRouterTransportError

    secret = "sk-sensitive-transport-test"
    attempts = []
    sleeps = []

    def opener(http_request, timeout):
        del http_request, timeout
        attempts.append(status)
        raise _http_error(status)

    client = OpenRouterClient(
        "openai/gpt-5.4",
        api_key=secret,
        max_attempts=4,
        opener=opener,
        sleeper=sleeps.append,
    )
    with pytest.raises(OpenRouterTransportError, match=str(status)) as caught:
        client.generate(
            {"messages": [{"role": "user", "content": "do not leak"}]}, seed=5
        )
    assert len(attempts) == 1
    assert sleeps == []
    assert secret not in str(caught.value)
    assert client.last_call_metadata is None


def test_retry_budget_is_bounded_and_exhaustion_fails_closed():
    from harness.openrouter_client import (
        OpenRouterClient,
        OpenRouterConfigurationError,
        OpenRouterTransportError,
    )

    for bad_attempts in (0, 6, True):
        with pytest.raises(OpenRouterConfigurationError, match="max_attempts"):
            OpenRouterClient(
                "openai/gpt-5.5", api_key="sk-test", max_attempts=bad_attempts
            )

    attempts = []
    sleeps = []

    def opener(http_request, timeout):
        del http_request, timeout
        attempts.append(1)
        raise _http_error(429)

    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        max_attempts=3,
        opener=opener,
        sleeper=sleeps.append,
    )
    with pytest.raises(OpenRouterTransportError, match="after 3 attempt"):
        client.generate(
            {"messages": [{"role": "user", "content": "retry"}]}, seed=7
        )
    assert len(attempts) == 3
    assert len(sleeps) == 2


def test_retry_after_seconds_is_honored_but_bounded():
    from harness.openrouter_client import OpenRouterClient

    attempts = []
    sleeps = []

    def opener(http_request, timeout):
        del http_request, timeout
        attempts.append(1)
        if len(attempts) == 1:
            raise _http_error(429, headers={"Retry-After": "90"})
        return _Response(_completion())

    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=opener,
        sleeper=sleeps.append,
    )
    assert client.generate(
        {"messages": [{"role": "user", "content": "retry"}]}, seed=8
    ) == "model answer"
    assert len(attempts) == 2
    assert sleeps == [30.0]


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"choices": []},
        {"choices": [{}]},
        {"choices": [{"message": {}}]},
        {"choices": [{"message": {"content": None}}]},
        {"choices": [{"message": {"content": "   "}}]},
        {"choices": [{"message": {"content": "ok"}}], "usage": "not-an-object"},
    ],
)
def test_malformed_or_empty_completion_fails_closed(payload):
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: _Response(payload),
    )
    with pytest.raises(OpenRouterResponseError):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )
    assert client.last_call_metadata is None


def test_invalid_json_completion_fails_closed():
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: _Response(b"not json", raw=True),
    )
    with pytest.raises(OpenRouterResponseError, match="JSON"):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )


@pytest.mark.parametrize("finish_reason", ["error", "length", "content_filter", "tool_calls"])
def test_in_band_errors_and_nonterminal_finish_reasons_fail_closed(finish_reason):
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    payload = _completion(finish_reason=finish_reason)
    if finish_reason == "error":
        payload["error"] = {"code": 502, "message": "provider failed after partial text"}
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: _Response(payload),
    )
    with pytest.raises(OpenRouterResponseError):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )
    assert client.last_call_metadata is None


def test_top_level_error_fails_even_when_partial_choice_claims_stop():
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    payload = _completion(finish_reason="stop")
    payload["error"] = {"code": 500, "message": "partial provider failure"}
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: _Response(payload),
    )
    with pytest.raises(OpenRouterResponseError, match="in-band error"):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )


def test_choice_error_fails_even_when_partial_choice_claims_stop():
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    payload = _completion(finish_reason="stop")
    payload["choices"][0]["error"] = {
        "code": 500,
        "message": "partial provider failure",
    }
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: _Response(payload),
    )
    with pytest.raises(OpenRouterResponseError, match="choice contained an error"):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )


@pytest.mark.parametrize("response_model", [None, "openai/gpt-5.4", "gpt-5.5"])
def test_response_model_must_exactly_match_requested_slug(response_model):
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    payload = _completion(model=response_model)
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: _Response(payload),
    )
    with pytest.raises(OpenRouterResponseError, match="model"):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )


@pytest.mark.parametrize(
    ("requested_model", "canonical_model"),
    [
        ("openai/gpt-5.5", "openai/gpt-5.5-20260423"),
        ("openai/gpt-5.4", "openai/gpt-5.4-20260305"),
        ("openai/gpt-5.4-mini", "openai/gpt-5.4-mini-20260317"),
    ],
)
def test_response_accepts_only_exact_frozen_canonical_slug_and_preserves_it(
    requested_model, canonical_model
):
    import harness.openrouter_client as openrouter_client
    from harness.openrouter_client import OpenRouterClient

    assert getattr(openrouter_client, "FROZEN_CANONICAL_MODEL_IDS", None) == CANONICAL_MODEL_IDS
    client = OpenRouterClient(
        requested_model,
        api_key="sk-test",
        opener=lambda request, timeout: _Response(
            _completion(model=canonical_model)
        ),
    )
    assert client.generate(
        {"messages": [{"role": "user", "content": "test"}]}, seed=4
    ) == "model answer"
    assert client.last_call_metadata["model"] == canonical_model


def test_response_rejects_unregistered_dated_variant_of_requested_model():
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: _Response(
            _completion(model="openai/gpt-5.5-20260424")
        ),
    )
    with pytest.raises(OpenRouterResponseError, match="model"):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )


def test_frozen_canonical_model_mapping_cannot_be_mutated_at_runtime():
    from harness.openrouter_client import FROZEN_CANONICAL_MODEL_IDS

    model_id = "openai/gpt-5.5"
    original = FROZEN_CANONICAL_MODEL_IDS[model_id]
    try:
        with pytest.raises(TypeError):
            FROZEN_CANONICAL_MODEL_IDS[model_id] = "openai/gpt-5.5-20990101"
    finally:
        if FROZEN_CANONICAL_MODEL_IDS[model_id] != original:
            FROZEN_CANONICAL_MODEL_IDS[model_id] = original


def test_completion_content_cannot_serialize_the_api_key():
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    secret = "sk-content-disclosure-test"
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key=secret,
        opener=lambda request, timeout: _Response(_completion(content=secret)),
    )
    with pytest.raises(OpenRouterResponseError, match="credential"):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )


@pytest.mark.parametrize(
    "usage",
    [
        {"prompt_tokens": True, "completion_tokens": 1, "total_tokens": 2},
        {"prompt_tokens": -1, "completion_tokens": 1, "total_tokens": 0},
        {"prompt_tokens": 1, "completion_tokens": None, "total_tokens": 1},
        {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2, "cost": -0.1},
        {"prompt_tokens": 1, "prompt_tokens_details": {"cached_tokens": -1}},
    ],
)
def test_usage_fields_reject_invalid_types_and_negative_values(usage):
    from harness.openrouter_client import OpenRouterClient, OpenRouterResponseError

    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: _Response(_completion(usage=usage)),
    )
    with pytest.raises(OpenRouterResponseError, match="usage"):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=4
        )


@pytest.mark.parametrize("max_tokens", [0, -1, 16385, True, 1.5])
def test_token_budget_must_be_a_bounded_integer(max_tokens):
    from harness.openrouter_client import OpenRouterClient, OpenRouterConfigurationError

    with pytest.raises(OpenRouterConfigurationError, match="max_tokens"):
        OpenRouterClient(
            "openai/gpt-5.5", api_key="sk-test", max_tokens=max_tokens
        )


@pytest.mark.parametrize("seed", [-1, True, 1.5, "7"])
def test_seed_and_canonical_messages_are_validated_before_transport(seed):
    from harness.openrouter_client import OpenRouterClient, OpenRouterRequestError

    called = []
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: called.append(request),
    )
    with pytest.raises(OpenRouterRequestError):
        client.generate(
            {"messages": [{"role": "user", "content": "test"}]}, seed=seed
        )
    assert called == []


def test_response_format_is_forced_to_canonical_text_before_transport():
    from harness.openrouter_client import OpenRouterClient, OpenRouterRequestError

    called = []
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: called.append(request),
    )
    invalid_formats = [
        {"type": "json_object"},
        {"type": "text", "private": "gold"},
        "text",
    ]
    for response_format in invalid_formats:
        with pytest.raises(OpenRouterRequestError, match="response_format"):
            client.generate(
                {
                    "messages": [{"role": "user", "content": "test"}],
                    "response_format": response_format,
                },
                seed=1,
            )
    assert called == []


def test_malformed_canonical_messages_fail_before_transport():
    from harness.openrouter_client import OpenRouterClient, OpenRouterRequestError

    called = []
    client = OpenRouterClient(
        "openai/gpt-5.5",
        api_key="sk-test",
        opener=lambda request, timeout: called.append(request),
    )
    malformed_messages = [
        {},
        {"messages": []},
        {"messages": "not-a-list"},
        {"messages": [{"role": "", "content": "x"}]},
        {"messages": [{"role": "user", "content": ""}]},
        {"messages": [{"role": "user", "content": "x", "private": "gold"}]},
    ]
    for request in malformed_messages:
        with pytest.raises(OpenRouterRequestError):
            client.generate(request, seed=1)
    assert called == []


def test_roster_factory_accepts_only_the_exact_requested_openai_models():
    from harness.openrouter_client import (
        REQUESTED_MODEL_ROSTER,
        OpenRouterConfigurationError,
        openrouter_client_from_roster,
    )

    clients = [
        openrouter_client_from_roster(row, api_key="sk-test")
        for row in REQUESTED_MODEL_ROSTER
    ]
    assert [client.model_id for client in clients] == [
        "openai/gpt-5.5",
        "openai/gpt-5.4",
        "openai/gpt-5.4-mini",
    ]
    assert [client.family for client in clients] == [
        "gpt-5.5",
        "gpt-5.4",
        "gpt-5.4-mini",
    ]
    assert {client.vendor for client in clients} == {"openai"}

    invalid = [
        {"model_id": "openai/gpt-5.6", "family": "gpt-5.6", "vendor": "openai"},
        {"model_id": "openai/gpt-5.5", "family": "wrong", "vendor": "openai"},
        {"model_id": "openai/gpt-5.5", "family": "gpt-5.5", "vendor": "other"},
        {"model_id": "openai/gpt-5.5", "family": "gpt-5.5"},
        {
            "model_id": "openai/gpt-5.5",
            "family": "gpt-5.5",
            "vendor": "openai",
            "api_key": "must-not-enter-roster",
        },
    ]
    for row in invalid:
        with pytest.raises(OpenRouterConfigurationError):
            openrouter_client_from_roster(row, api_key="sk-test")


def test_catalog_verifier_confirms_exact_slugs_with_injected_transport():
    from harness.openrouter_client import (
        MODELS_URL,
        REQUESTED_MODEL_IDS,
        verify_requested_model_catalog,
    )

    captured = []

    def opener(http_request, timeout):
        captured.append((http_request, timeout))
        return _Response(
            {
                "data": [
                    {"id": "unrelated/model"},
                    *[
                        {
                            "id": model_id,
                            "canonical_slug": CANONICAL_MODEL_IDS[model_id],
                            "supported_parameters": REQUIRED_SUPPORTED_PARAMETERS,
                        }
                        for model_id in reversed(REQUESTED_MODEL_IDS)
                    ],
                ]
            }
        )

    result = verify_requested_model_catalog(
        api_key="sk-catalog-test", opener=opener, timeout=13.0
    )
    assert result == {
        "verified": True,
        "model_ids": list(REQUESTED_MODEL_IDS),
    }
    http_request, timeout = captured[0]
    assert http_request.full_url == MODELS_URL
    assert http_request.get_method() == "GET"
    assert http_request.get_header("Authorization") == "Bearer sk-catalog-test"
    assert timeout == 13.0


def test_catalog_verifier_fails_closed_when_slug_is_missing_or_payload_is_malformed():
    from harness.openrouter_client import (
        REQUESTED_MODEL_IDS,
        OpenRouterCatalogError,
        verify_requested_model_catalog,
    )

    missing = REQUESTED_MODEL_IDS[-1]
    available = [
        {
            "id": model_id,
            "canonical_slug": CANONICAL_MODEL_IDS[model_id],
            "supported_parameters": REQUIRED_SUPPORTED_PARAMETERS,
        }
        for model_id in REQUESTED_MODEL_IDS[:-1]
    ]
    with pytest.raises(OpenRouterCatalogError, match=missing):
        verify_requested_model_catalog(
            api_key="sk-test",
            opener=lambda request, timeout: _Response({"data": available}),
        )

    malformed = ({}, {"data": "not-a-list"}, {"data": [{}]})
    for payload in malformed:
        with pytest.raises(OpenRouterCatalogError):
            verify_requested_model_catalog(
                api_key="sk-test",
                opener=lambda request, timeout, payload=payload: _Response(payload),
            )


@pytest.mark.parametrize("bad_canonical", [None, "openai/gpt-5.4-mini-20990101"])
def test_catalog_verifier_rejects_missing_or_mismatched_canonical_slug(
    bad_canonical,
):
    from harness.openrouter_client import (
        REQUESTED_MODEL_IDS,
        OpenRouterCatalogError,
        verify_requested_model_catalog,
    )

    rows = [
        {
            "id": model_id,
            "canonical_slug": CANONICAL_MODEL_IDS[model_id],
            "supported_parameters": REQUIRED_SUPPORTED_PARAMETERS,
        }
        for model_id in REQUESTED_MODEL_IDS
    ]
    rows[-1]["canonical_slug"] = bad_canonical
    with pytest.raises(OpenRouterCatalogError, match="canonical_slug"):
        verify_requested_model_catalog(
            api_key="sk-test",
            opener=lambda request, timeout: _Response({"data": rows}),
        )


def test_catalog_verifier_rejects_requested_model_missing_reasoning_effort_support():
    from harness.openrouter_client import (
        REQUESTED_MODEL_IDS,
        OpenRouterCatalogError,
        verify_requested_model_catalog,
    )

    rows = [
        {
            "id": model_id,
            "canonical_slug": CANONICAL_MODEL_IDS[model_id],
            "supported_parameters": [
                parameter
                for parameter in REQUIRED_SUPPORTED_PARAMETERS
                if parameter != "reasoning_effort"
            ],
        }
        for model_id in REQUESTED_MODEL_IDS
    ]
    with pytest.raises(OpenRouterCatalogError, match="reasoning_effort"):
        verify_requested_model_catalog(
            api_key="sk-test",
            opener=lambda request, timeout: _Response({"data": rows}),
        )
