from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK))

from pilot import contracts  # noqa: E402
from pilot.openrouter import OpenRouterClient, OpenRouterTransportError  # noqa: E402


class Headers:
    def __init__(self, values=None):
        self.values = {} if values is None else dict(values)

    def get_all(self, name):
        value = self.values.get(name)
        if value is None:
            return None
        return list(value) if isinstance(value, list) else [value]

    def get(self, name, default=None):
        values = self.get_all(name)
        return values[0] if values else default


class Response:
    def __init__(self, payload, status=200, headers=None):
        self.status = status
        self.payload = contracts.canonical_bytes(payload)
        self.headers = Headers(headers)
        self.closed = False

    def getcode(self):
        return self.status

    def read(self, _limit):
        return self.payload

    def close(self):
        self.closed = True


class SequenceURLopener:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def __call__(self, request, timeout):
        self.requests.append((request, timeout))
        return self.responses.pop(0)


def _catalog(alias, tags=("azure",)):
    model = contracts.resolve_model(alias)
    return {
        "data": {
            "id": alias,
            "endpoints": [{
                "model_id": alias, "provider_name": "Azure",
                "name": f"Azure | {model['expected_snapshot']}",
                "tag": tag, "status": 0,
                "context_length": 400_000,
                "supported_parameters": list(contracts.REQUIRED_PARAMETERS),
                "pricing": {
                    "prompt": str(model["price_ceiling_per_token"]["input"]),
                    "completion": str(model["price_ceiling_per_token"]["output"]),
                },
            } for tag in tags],
        }
    }


def _zdr_catalog(alias, tags=("azure",)):
    return {
        "data": [
            {**endpoint, "model_id": alias}
            for endpoint in _catalog(alias, tags)["data"]["endpoints"]
        ],
    }


def test_production_client_catalog_and_direct_completion_evidence_are_mocked_offline():
    alias = "openai/gpt-5-nano"
    snapshot = contracts.resolve_model(alias)["expected_snapshot"]
    completion = {
        "id": "gen-1", "model": snapshot, "provider": "Azure",
        "choices": [{"finish_reason": "stop", "message": {
            "role": "assistant", "content": "{}", "tool_calls": []
        }}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 2,
                  "total_tokens": 12, "cost": 0.000001},
        "openrouter_metadata": {
            "requested": alias, "strategy": "direct", "attempt": 1,
            "endpoints": {"total": 1, "available": [{
                "provider": "Azure", "model": snapshot, "selected": True,
            }]},
        },
    }
    opener = SequenceURLopener([
        Response(_catalog(alias)), Response(_zdr_catalog(alias)),
        Response(completion, headers={"X-Generation-Id": "gen-1"}),
    ])
    client = OpenRouterClient(
        environ={"OPENROUTER_API_KEY": "sk-or-v1-test-only-secret"},
        urlopen=opener,
    )
    catalog = client.catalog(alias)
    assert contracts.validate_catalog(
        catalog, contracts.resolve_model(alias)
    )["provider_display_name"] == "Azure"
    body = {
        "model": alias, "messages": [{"role": "user", "content": "test"}],
        "usage": {"include": True},
        "provider": contracts.resolve_model(alias)["routing"],
    }
    result = client.complete(body)
    assert result == {
        "response": completion,
        "response_headers": {"x_generation_id": ["gen-1"]},
    }
    assert "test-only-secret" not in json.dumps(result)
    assert opener.requests[0][0].get_header("Authorization") is None
    assert opener.requests[1][0].get_header("Authorization") is None
    assert opener.requests[2][0].get_header("Authorization").startswith("Bearer ")
    assert opener.requests[2][0].get_header("X-openrouter-metadata") == "enabled"
    assert json.loads(opener.requests[2][0].data) == body


def test_client_requires_environment_key_and_rejects_echoed_secret():
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        OpenRouterClient(environ={})
    secret = "sk-or-v1-test-only-secret"
    opener = SequenceURLopener([Response({"echo": secret})])
    client = OpenRouterClient(
        environ={"OPENROUTER_API_KEY": secret}, urlopen=opener,
    )
    with pytest.raises(OpenRouterTransportError, match="credential"):
        client.catalog("openai/gpt-5-nano")


def test_catalog_requires_exact_membership_in_zdr_endpoint_catalog():
    alias = "openai/gpt-5-nano"
    client = OpenRouterClient(
        environ={"OPENROUTER_API_KEY": "sk-or-v1-test-only-secret"},
        urlopen=SequenceURLopener([
            Response(_catalog(alias)), Response({"data": []}),
        ]),
    )
    with pytest.raises(ValueError, match="eligible exact Azure/ZDR endpoint"):
        client.catalog(alias)


def test_catalog_accepts_equivalent_exact_azure_region_rows_without_zdr_field():
    alias = "openai/gpt-5-nano"
    tags = ("azure/swedencentral", "azure")
    opener = SequenceURLopener([
        Response(_catalog(alias, tags)), Response(_zdr_catalog(alias, tags)),
    ])
    client = OpenRouterClient(
        environ={"OPENROUTER_API_KEY": "sk-or-v1-test-only-secret"},
        urlopen=opener,
    )
    evidence = client.catalog(alias)
    attestation = contracts.validate_catalog(
        evidence, contracts.resolve_model(alias)
    )
    assert attestation["eligible_endpoint_count"] == 2
    assert all(
        "zdr" not in row
        for row in evidence["model_catalog_response"]["data"]["endpoints"]
    )


def test_completion_rejects_undeclared_model_parameter_before_transport():
    opener = SequenceURLopener([])
    alias = "openai/gpt-5-nano"
    client = OpenRouterClient(
        environ={"OPENROUTER_API_KEY": "sk-or-v1-test-only-secret"},
        urlopen=opener,
    )
    with pytest.raises(ValueError, match="catalog-declared"):
        client.complete({
            "model": alias, "messages": [], "usage": {"include": True},
            "provider": contracts.resolve_model(alias)["routing"],
            "parallel_tool_calls": False,
        })
    assert opener.requests == []


def test_completion_preserves_missing_generation_header_without_polling():
    alias = "openai/gpt-5-nano"
    snapshot = contracts.resolve_model(alias)["expected_snapshot"]
    completion = {
        "id": "gen-null", "model": snapshot, "provider": "Azure",
        "choices": [{"finish_reason": "stop", "message": {
            "role": "assistant", "content": "{}", "tool_calls": []
        }}],
        "usage": {"prompt_tokens": 1, "completion_tokens": 1,
                  "total_tokens": 2, "cost": 0.0},
        "openrouter_metadata": {
            "requested": alias, "strategy": "direct", "attempt": 1,
            "endpoints": {"total": 1, "available": [{
                "provider": "Azure", "model": snapshot, "selected": True,
            }]},
        },
    }
    opener = SequenceURLopener([Response(completion)])
    client = OpenRouterClient(
        environ={"OPENROUTER_API_KEY": "sk-or-v1-test-only-secret"},
        urlopen=opener,
    )
    result = client.complete({
        "model": alias, "messages": [], "usage": {"include": True},
        "provider": contracts.resolve_model(alias)["routing"],
    })
    assert result["response_headers"] == {"x_generation_id": []}
    assert len(opener.requests) == 1
