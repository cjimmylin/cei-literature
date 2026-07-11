"""Contract tests for the benchmark-neutral sanitized OpenRouter client."""

from copy import deepcopy
import io
import json
import threading
import urllib.error

import pytest


SECRET = "test-secret-never-persist"


def api():
    import TENCOMMANDMENTS.harness.openrouter as openrouter

    return openrouter


class Response:
    status = 200

    def __init__(self, payload):
        self.raw = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return self.raw


def route(module):
    return module.ModelRoute(
        model_id="vendor/cheap-model",
        provider="Cheap Provider",
        endpoint_name="Cheap Provider: cheap-model",
        prompt_price_per_token_usd="0.000001",
        completion_price_per_token_usd="0.000002",
        canonical_model_id="vendor/cheap-model-20260701",
    )


def request():
    return {
        "messages": [
            {"role": "developer", "content": "Return one JSON object."},
            {"role": "user", "content": '{"question":"choose"}'},
        ],
        "response_format": {"type": "json_object"},
    }


def completion(**updates):
    value = {
        "id": "generation-001",
        "model": "vendor/cheap-model-20260701",
        "provider": "Cheap Provider",
        "choices": [
            {
                "message": {"role": "assistant", "content": '{"choice":"A"}'},
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 4,
            "total_tokens": 14,
            "cost": 0.000018,
            "unsafe_future_field": SECRET,
        },
    }
    value.update(updates)
    return value


def ledger(module, *call_ids):
    plan = module.preflight_spend(
        [module.CallEstimate(call_id, "0.001") for call_id in call_ids],
        cost_cap_usd="0.01",
    )
    return module.SpendLedger(plan)


def test_chat_request_pins_exact_provider_and_custodies_safe_usage_and_cost():
    module = api()
    seen = []

    def opener(http_request, timeout):
        seen.append((http_request, timeout))
        return Response(completion())

    spend = ledger(module, "call-001")
    client = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        max_tokens=128,
        opener=opener,
        ledger=spend,
    )
    content = client.generate(request(), seed=17, call_id="call-001")

    assert content == '{"choice":"A"}'
    http_request, timeout = seen[0]
    assert timeout == 60.0
    body = json.loads(http_request.data.decode("utf-8"))
    assert body["provider"] == {
        "order": ["Cheap Provider"],
        "allow_fallbacks": False,
        "require_parameters": True,
    }
    assert body["model"] == "vendor/cheap-model"
    assert body["temperature"] == 0
    assert body["usage"] == {"include": True}
    assert http_request.data == module.canonical_json_bytes(body)
    assert SECRET not in http_request.data.decode("utf-8")
    assert http_request.get_header("Authorization") == "Bearer " + SECRET

    metadata = client.last_call_metadata
    assert metadata["response_status"] == "ACCEPTED"
    assert metadata["provider"] == "Cheap Provider"
    assert metadata["provider_attribution"] == "RESPONSE_ECHOED"
    assert metadata["returned_model"] == "vendor/cheap-model-20260701"
    assert metadata["cost_usd"] == "0.000018"
    assert metadata["attempt_count"] == 1
    assert metadata["usage"] == {
        "prompt_tokens": 10,
        "completion_tokens": 4,
        "total_tokens": 14,
        "cost": 0.000018,
    }
    assert spend.spent_cost_usd == "0.000018"
    assert SECRET not in json.dumps(metadata, sort_keys=True)
    metadata["usage"]["cost"] = 999
    assert client.last_call_metadata["usage"]["cost"] == 0.000018


def test_response_without_provider_is_attributed_to_fail_closed_request_pin():
    module = api()
    payload = completion()
    payload.pop("provider")
    client = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: Response(payload),
        ledger=ledger(module, "call-001"),
    )

    client.generate(request(), seed=1, call_id="call-001")
    assert client.last_call_metadata["provider_attribution"] == (
        "REQUEST_PINNED_ALLOW_FALLBACKS_FALSE"
    )


@pytest.mark.parametrize(
    "updates, message",
    [
        ({"provider": "Wrong Provider"}, "provider"),
        ({"model": "vendor/different"}, "model"),
        ({"choices": []}, "choices"),
        ({"choices": [{"message": {"content": "x"}, "finish_reason": "length"}]}, "finish"),
        ({"error": {"message": SECRET}}, "in-band"),
    ],
)
def test_paid_but_invalid_responses_are_accounted_then_rejected(updates, message):
    module = api()
    spend = ledger(module, "call-001")
    client = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: Response(completion(**updates)),
        ledger=spend,
    )

    with pytest.raises(module.OpenRouterResponseError, match=message):
        client.generate(request(), seed=1, call_id="call-001")
    assert spend.spent_cost_usd == "0.000018"
    assert client.last_call_metadata["response_status"] == "REJECTED_RESPONSE"
    assert SECRET not in str(client.last_call_metadata)


def test_request_and_ledger_are_validated_before_transport():
    module = api()
    calls = []
    client = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: calls.append(True),
        ledger=ledger(module, "scheduled"),
    )

    with pytest.raises(module.SpendLedgerError, match="schedule"):
        client.generate(request(), seed=1, call_id="unscheduled")
    bad = deepcopy(request())
    bad["private_gold"] = {"answer": "A"}
    with pytest.raises(module.OpenRouterRequestError, match="fields"):
        client.generate(bad, seed=1, call_id="scheduled")
    assert calls == []


def test_api_key_in_model_facing_content_is_rejected_before_transport():
    module = api()
    calls = []
    exposed = request()
    exposed["messages"][1]["content"] = "accidental credential: " + SECRET
    client = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: calls.append(True),
        ledger=ledger(module, "call-001"),
    )

    with pytest.raises(module.OpenRouterRequestError, match="credential"):
        client.generate(exposed, seed=1, call_id="call-001")
    assert calls == []


def http_error(code, retry_after=None):
    headers = {} if retry_after is None else {"Retry-After": retry_after}
    return urllib.error.HTTPError(
        "https://openrouter.invalid",
        code,
        "secret body must not surface",
        headers,
        io.BytesIO((SECRET + " response body").encode()),
    )


def test_only_429_retries_reuse_exact_request_and_honor_retry_after():
    module = api()
    attempts = []
    sleeps = []

    def opener(http_request, timeout):
        attempts.append(http_request)
        if len(attempts) == 1:
            raise http_error(429, "7")
        return Response(completion())

    client = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=opener,
        sleeper=sleeps.append,
        max_attempts=3,
        retry_base_seconds=1,
        ledger=ledger(module, "call-001"),
    )

    client.generate(request(), seed=9, call_id="call-001")
    assert attempts[0] is attempts[1]
    assert attempts[0].data == attempts[1].data
    assert sleeps == [7.0]
    assert client.last_call_metadata["attempt_count"] == 2


@pytest.mark.parametrize("failure", [http_error(500), urllib.error.URLError(SECRET)])
def test_non_429_and_ambiguous_transport_failures_never_retry(failure):
    module = api()
    calls = []

    def opener(*_args, **_kwargs):
        calls.append(True)
        raise failure

    client = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=opener,
        sleeper=lambda _delay: pytest.fail("must not retry"),
        max_attempts=3,
        ledger=ledger(module, "call-001"),
    )

    with pytest.raises(module.OpenRouterTransportError) as caught:
        client.generate(request(), seed=1, call_id="call-001")
    assert calls == [True]
    assert caught.value.attempt_count == 1
    assert SECRET not in str(caught.value)


def test_safe_429_exhaustion_releases_call_but_ambiguous_failure_reserves_it():
    module = api()
    spend = ledger(module, "safe-call", "ambiguous-call")

    safe = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: (_ for _ in ()).throw(http_error(429)),
        sleeper=lambda _delay: None,
        max_attempts=1,
        ledger=spend,
    )
    with pytest.raises(module.OpenRouterTransportError) as caught:
        safe.generate(request(), seed=1, call_id="safe-call")
    assert caught.value.status_code == 429
    assert "safe-call" not in spend.inflight_call_ids

    ambiguous = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: (_ for _ in ()).throw(http_error(500)),
        max_attempts=1,
        ledger=spend,
    )
    with pytest.raises(module.OpenRouterTransportError) as caught:
        ambiguous.generate(request(), seed=1, call_id="ambiguous-call")
    assert caught.value.status_code == 500
    assert spend.inflight_call_ids == ("ambiguous-call",)

    calls = []
    duplicate = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: calls.append(True),
        ledger=spend,
    )
    with pytest.raises(module.SpendLedgerError, match="reserved|authorized|in.flight"):
        duplicate.generate(request(), seed=1, call_id="ambiguous-call")
    assert calls == []


def test_shared_ledger_reservation_blocks_concurrent_duplicate_before_transport():
    module = api()
    spend = ledger(module, "one-logical-call")
    entered = threading.Event()
    release = threading.Event()
    first_errors = []
    second_calls = []

    def first_opener(*_args, **_kwargs):
        entered.set()
        assert release.wait(timeout=5)
        return Response(completion())

    first = module.OpenRouterChatClient(
        route(module), api_key=SECRET, opener=first_opener, ledger=spend
    )
    second = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: second_calls.append(True),
        ledger=spend,
    )

    def run_first():
        try:
            first.generate(request(), seed=1, call_id="one-logical-call")
        except Exception as exc:  # pragma: no cover - asserted below
            first_errors.append(exc)

    worker = threading.Thread(target=run_first)
    worker.start()
    assert entered.wait(timeout=5)
    with pytest.raises(module.SpendLedgerError, match="reserved|authorized|in.flight"):
        second.generate(request(), seed=1, call_id="one-logical-call")
    release.set()
    worker.join(timeout=5)

    assert not worker.is_alive()
    assert first_errors == []
    assert second_calls == []
    assert spend.completed_call_ids == ("one-logical-call",)


def test_replayed_response_id_is_paid_and_custodied_before_rejection():
    module = api()
    spend = ledger(module, "call-001", "call-002")
    client = module.OpenRouterChatClient(
        route(module),
        api_key=SECRET,
        opener=lambda *_args, **_kwargs: Response(completion()),
        ledger=spend,
    )

    client.generate(request(), seed=1, call_id="call-001")
    with pytest.raises(module.OpenRouterResponseError, match="already observed"):
        client.generate(request(), seed=2, call_id="call-002")
    assert spend.completed_call_ids == ("call-001", "call-002")
    assert spend.spent_cost_usd == "0.000036"
    assert client.last_call_metadata["response_status"] == "REJECTED_RESPONSE"


def catalog_payload(module):
    selected = route(module)
    return {
        "data": {
            "id": selected.model_id,
            "endpoints": [
                {
                    "name": selected.endpoint_name,
                    "provider_name": selected.provider,
                    "status": 0,
                    "pricing": {
                        "prompt": selected.prompt_price_per_token_usd,
                        "completion": selected.completion_price_per_token_usd,
                    },
                    "supported_parameters": [
                        "max_tokens",
                        "response_format",
                        "seed",
                        "temperature",
                    ],
                }
            ],
        }
    }


def test_catalog_verifies_one_exact_healthy_provider_endpoint_without_secrets():
    module = api()
    requests = []

    def opener(http_request, timeout):
        requests.append((http_request, timeout))
        return Response(catalog_payload(module))

    verification = module.verify_model_routes(
        [route(module)],
        api_key=SECRET,
        opener=opener,
    )

    assert verification.to_dict() == {
        "verified": True,
        "routes": [
            {
                "model_id": "vendor/cheap-model",
                "provider": "Cheap Provider",
                "endpoint_name": "Cheap Provider: cheap-model",
            }
        ],
    }
    assert requests[0][0].full_url.endswith(
        "/api/v1/models/vendor/cheap-model/endpoints"
    )
    assert requests[0][0].get_header("Authorization") == "Bearer " + SECRET
    assert SECRET not in json.dumps(verification.to_dict())


@pytest.mark.parametrize("mutation", ["price", "status", "parameters", "duplicate"])
def test_catalog_fails_closed_when_exact_endpoint_contract_changes(mutation):
    module = api()
    payload = catalog_payload(module)
    endpoint = payload["data"]["endpoints"][0]
    if mutation == "price":
        endpoint["pricing"]["prompt"] = "0.000009"
    elif mutation == "status":
        endpoint["status"] = -2
    elif mutation == "parameters":
        endpoint["supported_parameters"].remove("seed")
    else:
        payload["data"]["endpoints"].append(deepcopy(endpoint))

    with pytest.raises(module.OpenRouterCatalogError, match="endpoint"):
        module.verify_model_routes(
            [route(module)],
            api_key=SECRET,
            opener=lambda *_args, **_kwargs: Response(payload),
        )


def test_catalog_malformed_response_uses_sanitized_catalog_error_type():
    module = api()

    class MalformedResponse(Response):
        def __init__(self):
            self.raw = b"not-json"

    with pytest.raises(module.OpenRouterCatalogError, match="catalog|JSON") as caught:
        module.verify_model_routes(
            [route(module)],
            api_key=SECRET,
            opener=lambda *_args, **_kwargs: MalformedResponse(),
        )
    assert SECRET not in str(caught.value)


def test_catalog_invalid_http_envelope_uses_catalog_error_type():
    module = api()

    class InvalidStatusResponse(Response):
        status = "200"

        def __init__(self):
            self.raw = b"{}"

    with pytest.raises(module.OpenRouterCatalogError, match="catalog|invalid"):
        module.verify_model_routes(
            [route(module)],
            api_key=SECRET,
            opener=lambda *_args, **_kwargs: InvalidStatusResponse(),
        )
