"""Offline contract tests for the pinned OpenRouter execution adapter."""
from __future__ import annotations

import base64
from copy import deepcopy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from pilot import contracts, manifest, openrouter_driver


BANK = Path(__file__).resolve().parents[1]
API_KEY = "unit-test-key-not-a-live-credential"
UUIDS = iter((
    "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
    "54c94821-a36c-4ea7-ae2c-568a1a4410ef",
))
ACTION = json.dumps({
    "reason": "The evidence is incomplete, so verification is proportionate.",
    "INTENT": "UNCERTAIN",
    "DECISION": "VERIFY",
}, separators=(",", ":"))
CHEAP_RETURNED_SNAPSHOTS = {
    "gpt-5-nano": "openai/gpt-5-nano-2025-08-07",
    "gpt-5.4-nano": "openai/gpt-5.4-nano-20260317",
    "gpt-5-mini": "openai/gpt-5-mini-2025-08-07",
    "gpt-5.4-mini": "openai/gpt-5.4-mini-20260317",
}


@pytest.fixture(scope="module")
def episode():
    rows = yaml.safe_load((BANK / "seeds_public.yaml").read_text())
    return rows[0]


def _unique_uuid():
    return next(UUIDS)


def _event(content=None, *, finish=None, metadata=None, reasoning=None,
           model="openai/gpt-5.5", provider="OpenAI", usage=None,
           error=None, tool_calls=None, generation_id="gen-test",
           status=None, extra=None):
    delta = {}
    if content is not None:
        delta["content"] = content
    if reasoning is not None:
        delta["reasoning_details"] = reasoning
    if tool_calls is not None:
        delta["tool_calls"] = tool_calls
    event = {
        "id": generation_id,
        "object": "chat.completion.chunk",
        "created": 1783700000,
        "model": model,
        "provider": provider,
        "choices": ([] if usage is not None or metadata is not None else [{
            "index": 0,
            "delta": delta,
            "finish_reason": finish,
        }]),
    }
    if usage is not None:
        event["usage"] = usage
    if metadata is not None:
        event["openrouter_metadata"] = metadata
    if error is not None:
        event["error"] = error
    if status is not None:
        event["status"] = status
    if extra is not None:
        event.update(deepcopy(extra))
    return event


def _metadata(*, provider="OpenAI", model="openai/gpt-5.5", pipeline=None):
    row = {
        "requested": model,
        "strategy": "direct",
        "attempt": 1,
        "endpoints": {
            "total": 1,
            "available": [{
                "provider": provider,
                "model": model,
                "selected": True,
            }],
        },
        "attempts": [{"provider": provider, "model": model, "status": 200}],
    }
    if pipeline is not None:
        row["pipeline"] = pipeline
    return row


def _multiple_endpoint_metadata(
        *, provider="Azure", model="openai/gpt-5-nano", requested=None):
    return {
        "requested": requested or model,
        "strategy": "direct",
        "attempt": 1,
        "endpoints": {
            "total": 2,
            "available": [
                {"provider": provider, "model": model, "selected": True},
                {"provider": provider, "model": model, "selected": False},
            ],
        },
        "attempts": [
            {"provider": provider, "model": model, "status": 200},
        ],
        "pipeline": [],
    }


def _sse(*events, fragment=False):
    text = ": OPENROUTER PROCESSING\n\n"
    text += "".join(
        "data: " + json.dumps(event, separators=(",", ":")) + "\n\n"
        for event in events
    )
    text += "data: [DONE]\n\n"
    raw = text.encode("utf-8")
    if not fragment:
        return [raw]
    cuts = (1, 9, 31, 89, len(raw) - 3)
    chunks = []
    start = 0
    for end in cuts:
        chunks.append(raw[start:end])
        start = end
    chunks.append(raw[start:])
    return chunks


def _success_chunks(*, content=ACTION, metadata=None, reasoning=None,
                    model="openai/gpt-5.5", provider="OpenAI",
                    pipeline=None, tool_calls=None, fragment=True):
    metadata = metadata or _metadata(
        provider=provider, model=model, pipeline=pipeline
    )
    usage = {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
        "prompt_tokens_details": {"cached_tokens": 4},
        "completion_tokens_details": {"reasoning_tokens": 8},
    }
    midpoint = len(content) // 2
    events = [
        _event(content[:midpoint], model=model, provider=provider,
               reasoning=reasoning, tool_calls=tool_calls),
        _event(content[midpoint:], finish="stop", model=model,
               provider=provider),
        _event(model=model, provider=provider, usage=usage),
        _event(model=model, provider=provider, metadata=metadata),
    ]
    return _sse(*events, fragment=fragment)


def _azure_live_terminal_events(
        *, requested="openai/gpt-5-nano",
        returned=CHEAP_RETURNED_SNAPSHOTS["gpt-5-nano"]):
    """Reproduce OpenRouter's documented terminal metadata+usage chunk."""
    metadata = {
        "requested": requested,
        "strategy": "direct",
        "attempt": 1,
        "endpoints": {
            "total": 3,
            "available": [{
                "provider": "Azure",
                "model": returned,
                "selected": True,
            }],
        },
    }
    events = [
        _event(ACTION, model=returned, provider="Azure"),
        _event("", finish="stop", model=returned, provider="Azure",
               extra={"native_finish_reason": "completed"}),
        {
            "id": "gen-test",
            "object": "chat.completion.chunk",
            "created": 1783700000,
            "model": returned,
            "provider": "Azure",
            "service_tier": "default",
            "choices": [{
                "index": 0,
                "delta": {"content": "", "role": "assistant"},
                "finish_reason": "stop",
                "native_finish_reason": "completed",
            }],
            "usage": _usage_object(),
            "openrouter_metadata": metadata,
        },
    ]
    return events


def _unicode_json_string(value):
    return '"' + "".join(f"\\u{ord(character):04x}" for character in value) + '"'


def _sse_with_unicode_escaped_value(events, value):
    serialized = [json.dumps(event, separators=(",", ":")) for event in events]
    for index, payload in enumerate(serialized):
        if json.dumps(value) in payload:
            serialized[index] = payload.replace(
                json.dumps(value), _unicode_json_string(value), 1
            )
            break
    else:
        raise AssertionError("escaped fixture value was not present")
    text = ": OPENROUTER PROCESSING\n\n"
    text += "".join("data: " + payload + "\n\n" for payload in serialized)
    text += "data: [DONE]\n\n"
    return [text.encode("utf-8")]


class FakeTransport:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, *, url, headers, body, timeout):
        self.calls.append({
            "url": url,
            "headers": deepcopy(headers),
            "body": bytes(body),
            "timeout": timeout,
        })
        if not self.responses:
            raise AssertionError("unexpected transport call")
        return self.responses.pop(0)


class TransportSequence:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = []

    def __call__(self, *, url, headers, body, timeout):
        self.calls.append({
            "url": url,
            "headers": deepcopy(headers),
            "body": bytes(body),
            "timeout": timeout,
        })
        if not self.outcomes:
            raise AssertionError("unexpected transport call")
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome


def _response(chunks, *, status=200, headers=None):
    return openrouter_driver.TransportResponse(
        status=status,
        headers=headers or {"X-Generation-Id": "gen-test"},
        chunks=chunks,
    )


def _one_stage_request(episode, *, stage="stage_1", prior=None,
                       execution_id="9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
                       logical_model_id="gpt-5.5",
                       panel_profile=manifest.FLAGSHIP_PROFILE_ID):
    identity = manifest.resolve_openrouter_identity(
        logical_model_id, profile_id=panel_profile
    )
    return contracts.build_stage_request(
        episode,
        execution_id=execution_id,
        provider=identity["provider"],
        logical_model_id=identity["logical_model_id"],
        provider_model_id=identity["provider_model_id"],
        configuration_id=identity["configuration_id"],
        stage=stage,
        prior_responses=prior or {},
    )


def _run_fixture_stage(episode, chunks, *, headers=None, future_turns=None):
    transport = FakeTransport([_response(chunks, headers=headers)])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode),
        future_turns=future_turns or [],
        transport=transport,
        api_key=API_KEY,
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    return result, transport


def _usage_object():
    return {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
        "prompt_tokens_details": {"cached_tokens": 4},
        "completion_tokens_details": {"reasoning_tokens": 8},
    }


def _crafted_stage_result(request, *, raw_final=ACTION, reasoning=None):
    attempt = contracts.build_stage_attempt(
        attempt_index=1,
        started_at_utc="2026-07-10T12:00:00Z",
        completed_at_utc="2026-07-10T12:00:01Z",
        provider_request_id="gen-crafted",
        token_emission_started=True,
        exit_status=None,
        http_status=200,
        finish_reason="stop",
        usage={
            "input_tokens": 120,
            "cached_input_tokens": 4,
            "output_tokens": 24,
            "reasoning_tokens": 8,
            "total_tokens": 144,
        },
        raw_trace="preserved crafted trace",
        raw_final_message=raw_final,
        reasoning_effort="medium",
        reasoning_details=reasoning,
        error_code=None,
    )
    return contracts.build_stage_result(
        request,
        run_mode="mock",
        returned_provider_model_id=request["provider_model_id"],
        returned_provider_name="OpenAI",
        session_id=None,
        transport_request_sha256="0" * 64,
        attempts=[attempt],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )


def test_request_body_and_sanitized_descriptor_freeze_routing(episode):
    request = _one_stage_request(episode)
    wire = openrouter_driver.build_wire_request(request, api_key=API_KEY)

    assert wire.url == "https://openrouter.ai/api/v1/chat/completions"
    assert wire.headers == {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json",
        "Accept": "text/event-stream",
        "X-OpenRouter-Metadata": "enabled",
    }
    body = json.loads(wire.body)
    assert hashlib.sha256(wire.body).hexdigest() == (
        "b42e9d0102ace7a5a0652f193c6f02b09ed0ea906e22104b5b07eecab584a9a5"
    )
    assert body["model"] == "openai/gpt-5.5"
    assert body["stream"] is True
    assert body["reasoning"] == {"effort": "medium"}
    assert body["provider"] == {
        "only": ["OpenAI"],
        "order": ["OpenAI"],
        "allow_fallbacks": False,
        "require_parameters": True,
        "data_collection": "deny",
        "zdr": True,
    }
    assert "tools" not in body and "plugins" not in body
    assert body["response_format"]["type"] == "json_schema"
    assert body["response_format"]["json_schema"]["strict"] is True
    serialized = json.dumps(wire.sanitized_descriptor, sort_keys=True)
    assert API_KEY not in serialized
    assert "Authorization" not in serialized
    assert wire.transport_request_sha256 == contracts.canonical_sha256(
        wire.sanitized_descriptor
    )


def test_cheap_profile_drives_exact_azure_wire_policy(episode):
    request = _one_stage_request(
        episode,
        logical_model_id="gpt-5-nano",
        panel_profile=manifest.CHEAP_PROFILE_ID,
    )

    wire = openrouter_driver.build_wire_request(request, api_key=API_KEY)
    body = json.loads(wire.body)

    assert body["model"] == "openai/gpt-5-nano"
    assert body["reasoning"] == {"effort": "medium"}
    assert body["provider"] == {
        "only": ["Azure"],
        "order": ["Azure"],
        "allow_fallbacks": False,
        "require_parameters": True,
        "data_collection": "deny",
        "zdr": True,
    }
    assert wire.sanitized_descriptor["body"] == body


def test_resolved_wire_pin_must_match_exact_returned_provider(
        episode, monkeypatch):
    real_resolve = manifest.resolve_openrouter_identity

    def poisoned_resolve(logical_model_id, profile_id=manifest.FLAGSHIP_PROFILE_ID):
        resolved = real_resolve(logical_model_id, profile_id=profile_id)
        if profile_id == manifest.FLAGSHIP_PROFILE_ID:
            resolved["routing_policy"]["only"] = ["Azure"]
            resolved["routing_policy"]["order"] = ["Azure"]
        return resolved

    monkeypatch.setattr(
        manifest, "resolve_openrouter_identity", poisoned_resolve
    )

    with pytest.raises(ValueError, match="routing|provider"):
        openrouter_driver.build_wire_request(
            _one_stage_request(episode), api_key=API_KEY
        )


def test_cheap_profile_stage_attests_azure_and_multiple_endpoints(episode):
    model = "openai/gpt-5-nano"
    returned = CHEAP_RETURNED_SNAPSHOTS["gpt-5-nano"]
    transport = FakeTransport([_response(_success_chunks(
        model=returned,
        provider="Azure",
        metadata=_multiple_endpoint_metadata(model=returned, requested=model),
    ))])
    request = _one_stage_request(
        episode,
        logical_model_id="gpt-5-nano",
        panel_profile=manifest.CHEAP_PROFILE_ID,
    )

    result = openrouter_driver.run_stage(
        request,
        future_turns=[],
        transport=transport,
        api_key=API_KEY,
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )

    assert result["terminal_status"] == "complete"
    assert result["returned_provider_model_id"] == returned
    assert result["returned_provider_name"] == "Azure"
    assert result["integrity"]["provider_identity_ok"] is True
    assert result["integrity"]["measurement_ready"] is False


def test_fragmented_sse_comments_reasoning_and_metadata_are_preserved(episode):
    reasoning = [{
        "type": "reasoning.summary",
        "summary": "Compared evidence and request risk.",
        "id": "reasoning-1",
        "format": "openai-responses-v1",
        "index": 0,
    }]
    transport = FakeTransport([
        _response(_success_chunks(reasoning=reasoning, fragment=True)),
    ])
    request = _one_stage_request(episode)
    result = openrouter_driver.run_stage(
        request,
        future_turns=[],
        transport=transport,
        api_key=API_KEY,
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )

    assert result["terminal_status"] == "complete"
    assert result["attempts"][0]["raw_final_message"] == ACTION
    assert result["attempts"][0]["reasoning_details"] == reasoning
    assert result["attempts"][0]["usage"] == {
        "input_tokens": 120,
        "cached_input_tokens": 4,
        "output_tokens": 24,
        "reasoning_tokens": 8,
        "total_tokens": 144,
    }
    assert result["provenance"] == "harness validation, NOT a measurement"
    assert result["integrity"]["integrity_valid"] is True
    assert result["integrity"]["measurement_ready"] is False


def test_pre_token_429_retries_but_midstream_error_never_retries(episode):
    transport = FakeTransport([
        _response([b'{"error":{"code":429}}'], status=429,
                  headers={"Retry-After": "1"}),
        _response(_success_chunks()),
    ])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert len(transport.calls) == 2
    assert result["transport_retry_count"] == 1
    assert result["terminal_status"] == "complete"

    midstream = _sse(
        _event("{\"reason\":", model="openai/gpt-5.5"),
        _event("", finish="error", error={
            "code": "server_error", "message": "provider disconnected"
        }),
    )
    transport = FakeTransport([_response(midstream)])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert len(transport.calls) == 1
    assert result["terminal_status"] != "complete"
    assert result["integrity"]["measurement_ready"] is False


def test_only_429_or_503_are_retryable_and_retry_after_is_bounded(episode):
    sleeps = []
    transport = FakeTransport([
        _response([b'{"error":{"code":429}}'], status=429,
                  headers={"Retry-After": "999"}),
        _response([b'{"error":{"code":503}}'], status=503,
                  headers={"Retry-After": "not-a-delay"}),
        _response(_success_chunks()),
    ])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=sleeps.append,
    )
    assert sleeps == [120, 2]
    assert result["transport_retry_count"] == 2
    assert result["terminal_status"] == "complete"

    transport = FakeTransport([
        _response([b'{"error":{"code":502}}'], status=502),
        _response(_success_chunks()),
    ])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert len(transport.calls) == 1
    assert result["terminal_status"] == "failed"
    assert result["integrity"]["transport_successful"] is False


def test_retry_after_sixty_seconds_is_honored_exactly(episode):
    sleeps = []
    transport = FakeTransport([
        _response([b'{"error":{"code":429}}'], status=429,
                  headers={"Retry-After": "60"}),
        _response(_success_chunks()),
    ])

    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=sleeps.append,
    )

    assert sleeps == [60]
    assert result["transport_retry_count"] == 1
    assert result["terminal_status"] == "complete"


def test_invalid_canonical_response_is_unresolved_without_repair_or_retry(episode):
    transport = FakeTransport([
        _response(_success_chunks(content="INTENT: UNCERTAIN\nDECISION: VERIFY")),
    ])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert len(transport.calls) == 1
    assert result["terminal_status"] == "unresolved"
    assert result["attempts"][0]["parse_mode"] == "unresolved"
    assert result["attempts"][0]["raw_final_message"] == (
        "INTENT: UNCERTAIN\nDECISION: VERIFY"
    )


@pytest.mark.parametrize("mutation", ["wrong-model", "wrong-provider", "pipeline"])
def test_wrong_route_or_router_pipeline_invalidates(episode, mutation):
    model = "openai/gpt-5.4" if mutation == "wrong-model" else "openai/gpt-5.5"
    provider = "Azure" if mutation == "wrong-provider" else "OpenAI"
    pipeline = ([{"type": "context_compression", "name": "middle-out"}]
                if mutation == "pipeline" else None)
    transport = FakeTransport([
        _response(_success_chunks(
            model=model, provider=provider, pipeline=pipeline
        )),
    ])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False


def test_cheap_route_accepts_multiple_all_exact_endpoints_only():
    model = "openai/gpt-5-nano"
    provider = "Azure"
    generation_id = "gen-cheap"
    events = [{
        "id": generation_id,
        "model": model,
        "provider": provider,
    }]

    route_ok, returned_model, returned_provider = (
        openrouter_driver._route_evidence(
            _multiple_endpoint_metadata(),
            model,
            events,
            generation_id,
            [0],
            expected_provider=provider,
            eligible_endpoint_policy="all_exact_one_selected",
        )
    )

    assert route_ok is True
    assert returned_model == model
    assert returned_provider == provider


def test_live_azure_snapshot_and_terminal_metadata_usage_shape_is_accepted():
    returned = CHEAP_RETURNED_SNAPSHOTS["gpt-5-nano"]
    transport = FakeTransport([_response(_sse(
        *_azure_live_terminal_events(), fragment=True
    ))])

    run = openrouter_driver._run_live_access_probe(
        logical_model_id="gpt-5-nano",
        api_key=API_KEY,
        transport=transport,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        authorization=openrouter_driver._LIVE_ACCESS_PROBE_AUTHORIZATION,
    )

    assert len(transport.calls) == 1
    assert run["status"] == "complete"
    assert run["results"][0]["terminal_status"] == "complete"
    assert run["results"][0]["returned_provider_model_id"] == returned
    assert run["results"][0]["returned_provider_name"] == "Azure"
    assert run["results"][0]["attempts"][0]["error_code"] is None


def test_live_azure_terminal_metadata_accepts_explicit_empty_attempts():
    events = _azure_live_terminal_events()
    events[-1]["openrouter_metadata"]["attempts"] = []
    transport = FakeTransport([_response(_sse(*events))])

    run = openrouter_driver._run_live_access_probe(
        logical_model_id="gpt-5-nano",
        api_key=API_KEY,
        transport=transport,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        authorization=openrouter_driver._LIVE_ACCESS_PROBE_AUTHORIZATION,
    )

    assert run["status"] == "complete"
    assert run["results"][0]["integrity"]["provider_identity_ok"] is True


@pytest.mark.parametrize(
    "mutation",
    (
        "unfrozen-selected-snapshot",
        "mismatched-event-snapshot",
        "wrong-provider",
        "fallback-pipeline",
        "extra-finish",
    ),
)
def test_live_azure_terminal_shape_still_rejects_identity_or_finish_poison(
        mutation):
    events = _azure_live_terminal_events()
    metadata = events[-1]["openrouter_metadata"]
    if mutation == "unfrozen-selected-snapshot":
        unfrozen = "openai/gpt-5-nano-2099-01-01"
        metadata["endpoints"]["available"][0]["model"] = unfrozen
        for event in events:
            event["model"] = unfrozen
    elif mutation == "mismatched-event-snapshot":
        events[0]["model"] = "openai/gpt-5-nano"
    elif mutation == "wrong-provider":
        metadata["endpoints"]["available"][0]["provider"] = "OpenAI"
        for event in events:
            event["provider"] = "OpenAI"
    elif mutation == "fallback-pipeline":
        metadata["pipeline"] = [{"type": "fallback"}]
    else:
        events[0]["choices"][0]["finish_reason"] = "stop"
    transport = FakeTransport([_response(_sse(*events))])

    run = openrouter_driver._run_live_access_probe(
        logical_model_id="gpt-5-nano",
        api_key=API_KEY,
        transport=transport,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        authorization=openrouter_driver._LIVE_ACCESS_PROBE_AUTHORIZATION,
    )

    assert len(transport.calls) == 1
    assert run["status"] == "invalidated"
    assert run["results"][0]["integrity"]["measurement_ready"] is False


@pytest.mark.parametrize(
    "mutation",
    (
        "wrong-provider",
        "wrong-model",
        "two-selected",
        "zero-selected",
        "two-attempts",
        "failed-attempt",
        "pipeline",
    ),
)
def test_cheap_route_rejects_any_nonexact_endpoint_or_execution(mutation):
    model = "openai/gpt-5-nano"
    provider = "Azure"
    generation_id = "gen-cheap"
    metadata = _multiple_endpoint_metadata()
    if mutation == "wrong-provider":
        metadata["endpoints"]["available"][1]["provider"] = "OpenAI"
    elif mutation == "wrong-model":
        metadata["endpoints"]["available"][1]["model"] = "openai/gpt-5-mini"
    elif mutation == "two-selected":
        metadata["endpoints"]["available"][1]["selected"] = True
    elif mutation == "zero-selected":
        metadata["endpoints"]["available"][0]["selected"] = False
    elif mutation == "two-attempts":
        metadata["attempts"].append(deepcopy(metadata["attempts"][0]))
    elif mutation == "failed-attempt":
        metadata["attempts"][0]["status"] = 503
    elif mutation == "pipeline":
        metadata["pipeline"] = [{"type": "fallback"}]

    route_ok, _, _ = openrouter_driver._route_evidence(
        metadata,
        model,
        [{"id": generation_id, "model": model, "provider": provider}],
        generation_id,
        [0],
        expected_provider=provider,
        eligible_endpoint_policy="all_exact_one_selected",
    )

    assert route_ok is False


def test_flagship_route_still_rejects_multiple_exact_endpoints():
    model = "openai/gpt-5.5"
    provider = "OpenAI"
    generation_id = "gen-flagship"
    metadata = _multiple_endpoint_metadata(provider=provider, model=model)

    route_ok, _, _ = openrouter_driver._route_evidence(
        metadata,
        model,
        [{"id": generation_id, "model": model, "provider": provider}],
        generation_id,
        [0],
        expected_provider=provider,
        eligible_endpoint_policy="exactly_one",
    )

    assert route_ok is False


@pytest.mark.parametrize("failure", ["missing-metadata", "missing-generation-id"])
def test_missing_router_attestation_invalidates(episode, failure):
    if failure == "missing-metadata":
        usage = {
            "prompt_tokens": 120,
            "completion_tokens": 24,
            "total_tokens": 144,
        }
        chunks = _sse(
            _event(ACTION, finish="stop"),
            _event(usage=usage),
        )
        headers = {"X-Generation-Id": "gen-test"}
    else:
        chunks = _success_chunks()
        headers = {"Content-Type": "text/event-stream"}
    transport = FakeTransport([_response(chunks, headers=headers)])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False


def test_tool_event_and_future_prompt_or_hash_invalidate(episode):
    future = episode["multiturn_script"]["stage_2"]
    for leaked in (future, contracts.sha256_utf8(future)):
        transport = FakeTransport([
            _response(_success_chunks(content=ACTION + leaked)),
        ])
        result = openrouter_driver.run_stage(
            _one_stage_request(episode),
            future_turns=[{"stage": "stage_2", "content": future}],
            transport=transport, api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )
        assert result["terminal_status"] == "invalidated"
        assert "future_text" in result["integrity"]["violations"]

    transport = FakeTransport([
        _response(_success_chunks(tool_calls=[{
            "id": "call-1", "type": "function",
            "function": {"name": "lookup", "arguments": "{}"},
        }])),
    ])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert result["terminal_status"] == "invalidated"
    assert result["tool_events"]


@pytest.mark.parametrize("payload", [
    b'data: {"id":"a","id":"b"}\n\ndata: [DONE]\n\n',
    b'data: not-json\n\ndata: [DONE]\n\n',
    b'data: {"choices":[]}\n\n',
])
def test_malformed_or_incomplete_utf8_sse_invalidates_without_retry(
        episode, payload):
    transport = FakeTransport([_response([payload])])
    result = openrouter_driver.run_stage(
        _one_stage_request(episode), future_turns=[], transport=transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert len(transport.calls) == 1
    assert result["terminal_status"] == "invalidated"
    assert result["attempts"][0]["raw_trace"] == payload.decode("utf-8")
    assert API_KEY not in json.dumps(result, sort_keys=True)


def test_four_stage_episode_uses_exact_raw_history_and_builds_chain(episode):
    transport = FakeTransport([
        _response(_success_chunks()) for _ in range(4)
    ])
    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert run["status"] == "complete"
    assert len(run["requests"]) == len(run["results"]) == 4
    assert contracts.validate_stage_chain(
        run["chain"], run["requests"], run["results"], episode
    ) == run["chain"]
    for index, call in enumerate(transport.calls):
        messages = json.loads(call["body"])["messages"]
        assert len(messages) == 2 * index + 1
        assert messages[-1] == {
            "role": "user",
            "content": episode["multiturn_script"][f"stage_{index + 1}"],
        }
        for prior in range(index):
            assert messages[2 * prior + 1]["content"] == ACTION
    assert API_KEY not in json.dumps(run, sort_keys=True)


def test_four_stage_cheap_episode_uses_profile_identity_and_azure_route(
        episode):
    model = "openai/gpt-5-nano"
    returned = CHEAP_RETURNED_SNAPSHOTS["gpt-5-nano"]
    transport = FakeTransport([
        _response(_success_chunks(
            model=returned,
            provider="Azure",
            metadata=_multiple_endpoint_metadata(
                model=returned, requested=model
            ),
        ))
        for _ in range(4)
    ])

    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5-nano",
        panel_profile=manifest.CHEAP_PROFILE_ID,
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )

    assert run["status"] == "complete"
    assert len(run["requests"]) == len(run["results"]) == 4
    assert all(
        request["logical_model_id"] == "gpt-5-nano"
        and request["provider_model_id"] == model
        and request["configuration_id"] == (
            "openrouter-azure-gpt-5-nano-medium-no-fallback-zdr"
        )
        for request in run["requests"]
    )
    assert all(
        result["returned_provider_name"] == "Azure"
        and result["integrity"]["provider_identity_ok"] is True
        for result in run["results"]
    )
    assert all(
        json.loads(call["body"])["provider"]["only"] == ["Azure"]
        for call in transport.calls
    )
    assert contracts.validate_stage_chain(
        run["chain"], run["requests"], run["results"], episode
    ) == run["chain"]


def test_four_stage_gpt54_mini_episode_uses_exact_azure_snapshot(episode):
    model = "openai/gpt-5.4-mini"
    returned = CHEAP_RETURNED_SNAPSHOTS["gpt-5.4-mini"]
    transport = FakeTransport([
        _response(_success_chunks(
            model=returned,
            provider="Azure",
            metadata=_multiple_endpoint_metadata(
                model=returned, requested=model
            ),
        ))
        for _ in range(4)
    ])

    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.4-mini",
        panel_profile=manifest.GPT54_MINI_PROFILE_ID,
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )

    assert run["status"] == "complete"
    assert len(run["requests"]) == len(run["results"]) == 4
    assert all(
        request["provider_model_id"] == model
        and request["configuration_id"] == (
            "openrouter-azure-gpt-5.4-mini-medium-no-fallback-zdr"
        )
        for request in run["requests"]
    )
    assert all(
        result["returned_provider_model_id"] == returned
        and result["returned_provider_name"] == "Azure"
        and result["integrity"]["provider_identity_ok"] is True
        for result in run["results"]
    )
    assert all(
        json.loads(call["body"])["provider"] == {
            "only": ["Azure"],
            "order": ["Azure"],
            "allow_fallbacks": False,
            "require_parameters": True,
            "data_collection": "deny",
            "zdr": True,
        }
        for call in transport.calls
    )


def test_live_access_probe_is_exactly_one_nonmeasurement_stage(episode):
    model = "openai/gpt-5-nano"
    returned = CHEAP_RETURNED_SNAPSHOTS["gpt-5-nano"]
    transport = FakeTransport([_response(_success_chunks(
        model=returned,
        provider="Azure",
        metadata=_multiple_endpoint_metadata(model=returned, requested=model),
    ))])
    before = []
    sink = []

    run = openrouter_driver._run_live_access_probe(
        logical_model_id="gpt-5-nano",
        api_key=API_KEY,
        transport=transport,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        before_stage=lambda event: before.append(deepcopy(event)),
        stage_sink=lambda event: sink.append(deepcopy(event)),
        authorization=openrouter_driver._LIVE_ACCESS_PROBE_AUTHORIZATION,
    )

    assert len(transport.calls) == 1
    assert run["status"] == "complete"
    assert run["provenance"] == (
        "live OpenRouter access probe, NOT a measurement"
    )
    assert run["measurement_ready"] is False
    assert run["integrity_session_count"] == 1
    assert len(run["sessions"]) == 1
    assert len(run["requests"]) == len(run["results"]) == 1
    assert len(run["transport_descriptors"]) == 1
    assert run["chain"] is None
    assert run["requests"][0]["stage"] == "stage_1"
    assert run["requests"][0]["current_visible_turn"]["content"] == (
        manifest.build_cheap_access_probe("gpt-5-nano")[
            "multiturn_script"
        ]["stage_1"]
    )
    assert run["results"][0]["run_mode"] == "openrouter_probe"
    assert run["results"][0]["integrity"]["measurement_ready"] is False
    assert [event["stage"] for event in before] == ["stage_1"]
    assert [event["stage"] for event in sink] == ["stage_1"]
    assert "result" not in before[0] and sink[0]["result"] == run["results"][0]


def test_gpt54_mini_access_probe_is_one_exact_nonmeasurement_stage():
    model = "openai/gpt-5.4-mini"
    returned = CHEAP_RETURNED_SNAPSHOTS["gpt-5.4-mini"]
    transport = FakeTransport([_response(_success_chunks(
        model=returned,
        provider="Azure",
        metadata=_multiple_endpoint_metadata(model=returned, requested=model),
    ))])

    run = openrouter_driver._run_live_access_probe(
        logical_model_id="gpt-5.4-mini",
        profile_id=manifest.GPT54_MINI_PROFILE_ID,
        api_key=API_KEY,
        transport=transport,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        authorization=openrouter_driver._LIVE_ACCESS_PROBE_AUTHORIZATION,
    )

    assert len(transport.calls) == 1
    assert run["status"] == "complete"
    assert run["measurement_ready"] is False
    assert run["results"][0]["returned_provider_model_id"] == returned
    assert run["results"][0]["returned_provider_name"] == "Azure"
    assert run["results"][0]["run_mode"] == "openrouter_probe"


def test_stage_hooks_are_sanitized_deepcopied_and_follow_transport_validation(
        episode, monkeypatch):
    transport = FakeTransport([
        _response(_success_chunks()) for _ in range(4)
    ])
    timeline = []
    before_events = []
    sink_events = []
    original_validate = openrouter_driver.validate_transport_descriptor

    def validate(*args, **kwargs):
        outcome = original_validate(*args, **kwargs)
        timeline.append(("validated", kwargs["request"]["stage"]))
        return outcome

    monkeypatch.setattr(
        openrouter_driver, "validate_transport_descriptor", validate
    )

    def before_stage(event):
        stage_number = contracts.STAGES.index(event["stage"])
        assert len(transport.calls) == stage_number
        assert set(event) == {
            "provider", "integrity_session", "execution_id", "stage",
            "request", "transport_descriptor", "attestation",
        }
        assert event["provider"] == "openrouter"
        assert event["integrity_session"] == 1
        assert event["attestation"] is None
        assert API_KEY not in json.dumps(event, sort_keys=True)
        assert event["execution_id"] == event["request"]["execution_id"]
        timeline.append(("before", event["stage"]))
        before_events.append(deepcopy(event))
        event["request"]["stage"] = "poisoned"
        event["transport_descriptor"]["method"] = "POISONED"
        return {"ignored": True}

    def stage_sink(event):
        stage_number = contracts.STAGES.index(event["stage"]) + 1
        assert len(transport.calls) == stage_number
        assert set(event) == {
            "provider", "integrity_session", "execution_id", "stage",
            "request", "transport_descriptor", "attestation", "result",
        }
        assert timeline[-1] == ("validated", event["stage"])
        assert event["attestation"] is None
        assert event["result"] == contracts.validate_stage_result(
            event["result"], event["request"]
        )
        assert API_KEY not in json.dumps(event, sort_keys=True)
        timeline.append(("sink", event["stage"]))
        sink_events.append(deepcopy(event))
        event["result"]["terminal_status"] = "poisoned"
        return "ignored"

    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        before_stage=before_stage,
        stage_sink=stage_sink,
    )

    assert [row["stage"] for row in before_events] == list(contracts.STAGES)
    assert [row["stage"] for row in sink_events] == list(contracts.STAGES)
    assert all(row["stage"] in contracts.STAGES for row in run["requests"])
    assert all(row["terminal_status"] == "complete" for row in run["results"])
    for stage in contracts.STAGES:
        assert timeline.index(("before", stage)) < timeline.index(
            ("validated", stage)
        ) < timeline.index(("sink", stage))


@pytest.mark.parametrize("crash_hook", ["before_stage_2", "sink_stage_1"])
def test_stage_hook_exception_prevents_every_subsequent_openrouter_call(
        episode, crash_hook):
    transport = FakeTransport([
        _response(_success_chunks()) for _ in range(4)
    ])

    def before_stage(event):
        if crash_hook == "before_stage_2" and event["stage"] == "stage_2":
            raise RuntimeError("before-stage crash")

    def stage_sink(event):
        if crash_hook == "sink_stage_1" and event["stage"] == "stage_1":
            raise RuntimeError("stage-sink crash")

    with pytest.raises(RuntimeError, match="crash"):
        openrouter_driver.run_episode(
            episode,
            logical_model_id="gpt-5.5",
            transport=transport,
            api_key=API_KEY,
            uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
            before_stage=before_stage,
            stage_sink=stage_sink,
        )
    assert len(transport.calls) == 1


def test_stage_hooks_number_openrouter_integrity_rerun_sessions_exactly(episode):
    ids = iter((
        "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        "54c94821-a36c-4ea7-ae2c-568a1a4410ef",
    ))
    transport = FakeTransport([
        _response(_success_chunks(model="openai/gpt-5.4")),
        *[_response(_success_chunks()) for _ in range(4)],
    ])
    events = []

    def capture(kind):
        def callback(event):
            events.append((
                kind, event["integrity_session"], event["stage"],
                event["execution_id"],
            ))
        return callback

    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: next(ids),
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        before_stage=capture("before"),
        stage_sink=capture("sink"),
    )

    assert len(transport.calls) == 5
    assert [(kind, session, stage) for kind, session, stage, _run_id in events] == [
        ("before", 1, "stage_1"),
        ("sink", 1, "stage_1"),
        *[
            row
            for stage in contracts.STAGES
            for row in (("before", 2, stage), ("sink", 2, stage))
        ],
    ]
    assert {run_id for _kind, session, _stage, run_id in events if session == 1} == {
        run["sessions"][0]["execution_id"]
    }
    assert {run_id for _kind, session, _stage, run_id in events if session == 2} == {
        run["sessions"][1]["execution_id"]
    }


def test_openrouter_protocol_failure_emits_start_only_and_keeps_failure_record(
        episode):
    raw = b"data: \xff"
    transport = FakeTransport([_response([raw])])
    before_events = []
    sink_events = []

    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        before_stage=lambda event: before_events.append(deepcopy(event)),
        stage_sink=lambda event: sink_events.append(deepcopy(event)),
    )

    assert run["status"] == "failed"
    assert len(before_events) == 1
    assert before_events[0]["stage"] == "stage_1"
    assert before_events[0]["attestation"] is None
    assert sink_events == []
    assert API_KEY not in json.dumps(before_events[0], sort_keys=True)
    assert run["failure_record"]["raw_bytes_sha256"] == hashlib.sha256(
        raw
    ).hexdigest()


def test_run_live_episode_forwards_provider_neutral_stage_hooks(
        episode, monkeypatch):
    captured = {}
    before_stage = lambda _event: None
    stage_sink = lambda _event: None

    def fake_run_episode(*args, **kwargs):
        captured["args"] = args
        captured["kwargs"] = kwargs
        return {"forwarded": True}

    monkeypatch.setattr(openrouter_driver, "run_episode", fake_run_episode)
    result = openrouter_driver.run_live_episode(
        episode,
        logical_model_id="gpt-5.5",
        api_key=API_KEY,
        before_stage=before_stage,
        stage_sink=stage_sink,
    )

    assert result == {"forwarded": True}
    assert captured["args"] == (episode,)
    assert captured["kwargs"]["before_stage"] is before_stage
    assert captured["kwargs"]["stage_sink"] is stage_sink
    assert captured["kwargs"]["run_mode"] == "openrouter"
    assert captured["kwargs"]["logical_model_id"] == "gpt-5.5"
    assert captured["kwargs"]["panel_profile"] == manifest.FLAGSHIP_PROFILE_ID


def test_generic_live_entrypoints_reject_cheap_scope_before_internal_call(
        episode, monkeypatch):
    calls = []

    def forbidden(*_args, **_kwargs):
        calls.append("called")
        raise AssertionError("cheap live scope reached generic execution")

    monkeypatch.setattr(openrouter_driver, "run_episode", forbidden)
    with pytest.raises(ValueError, match="cheap|qualification|dedicated"):
        openrouter_driver.run_live_episode(
            episode,
            logical_model_id="gpt-5-nano",
            panel_profile=manifest.CHEAP_PROFILE_ID,
            api_key=API_KEY,
        )
    monkeypatch.setattr(openrouter_driver, "_run_stage_record", forbidden)
    with pytest.raises(ValueError, match="cheap|qualification|dedicated"):
        openrouter_driver.run_stage(
            _one_stage_request(
                episode,
                logical_model_id="gpt-5-nano",
                panel_profile=manifest.CHEAP_PROFILE_ID,
            ),
            future_turns=[],
            api_key=API_KEY,
            run_mode="openrouter",
        )
    assert calls == []


def test_dedicated_live_qualification_validates_scope_before_authorized_core(
        episode, monkeypatch):
    captured = []

    def fake_authorized(*args, **kwargs):
        captured.append((args, kwargs))
        return {"authorized": True}

    monkeypatch.setattr(
        openrouter_driver, "_run_episode_authorized", fake_authorized,
        raising=False,
    )
    result = openrouter_driver.run_live_cheap_qualification_episode(
        episode,
        logical_model_id="gpt-5-nano",
        purpose="canary",
        api_key=API_KEY,
    )
    assert result == {"authorized": True}
    assert captured[0][0] == (episode,)
    assert captured[0][1]["run_mode"] == "openrouter"
    assert captured[0][1]["panel_profile"] == manifest.CHEAP_PROFILE_ID
    assert captured[0][1]["authorization"] is (
        openrouter_driver._LIVE_CHEAP_QUALIFICATION_AUTHORIZATION
    )

    mutated = deepcopy(episode)
    mutated["multiturn_script"]["stage_1"] += " mutation"
    for candidate, purpose, model in (
        (mutated, "canary", "gpt-5-nano"),
        (episode, "calibration", "gpt-5-nano"),
        (episode, "smoke", "gpt-5.5"),
    ):
        with pytest.raises(
                ValueError, match="public|qualification|purpose|cheap|model"):
            openrouter_driver.run_live_cheap_qualification_episode(
                candidate,
                logical_model_id=model,
                purpose=purpose,
                api_key=API_KEY,
            )
    assert len(captured) == 1


def test_dedicated_live_qualification_accepts_only_frozen_mini_profile(
        episode, monkeypatch):
    captured = []

    def fake_authorized(*args, **kwargs):
        captured.append((args, kwargs))
        return {"authorized": True}

    monkeypatch.setattr(
        openrouter_driver, "_run_episode_authorized", fake_authorized,
        raising=False,
    )
    result = openrouter_driver.run_live_cheap_qualification_episode(
        episode,
        logical_model_id="gpt-5.4-mini",
        purpose="smoke",
        api_key=API_KEY,
        profile_id=manifest.GPT54_MINI_PROFILE_ID,
    )

    assert result == {"authorized": True}
    assert captured[0][1]["panel_profile"] == (
        manifest.GPT54_MINI_PROFILE_ID
    )
    assert captured[0][1]["authorization"] is (
        openrouter_driver._LIVE_CHEAP_QUALIFICATION_AUTHORIZATION
    )

    with pytest.raises(ValueError, match="profile|frozen|qualification"):
        openrouter_driver.run_live_cheap_qualification_episode(
            episode,
            logical_model_id="gpt-5.4-mini",
            purpose="smoke",
            api_key=API_KEY,
            profile_id="unfrozen-profile",
        )
    assert len(captured) == 1


@pytest.mark.parametrize("boundary", [
    "public-qualification",
    "authorized-qualification-core",
    "public-access-probe",
    "authorized-access-probe-core",
])
def test_every_dedicated_qualification_boundary_rejects_flagship_profile(
        episode, monkeypatch, boundary):
    calls = []

    def forbidden(*_args, **_kwargs):
        calls.append("called")
        raise AssertionError("flagship reached dedicated qualification core")

    with pytest.raises(ValueError, match="qualification|profile|frozen"):
        if boundary == "public-qualification":
            monkeypatch.setattr(
                openrouter_driver, "_run_episode_authorized", forbidden
            )
            openrouter_driver.run_live_cheap_qualification_episode(
                episode,
                logical_model_id="gpt-5.5",
                purpose="canary",
                api_key=API_KEY,
                profile_id=manifest.FLAGSHIP_PROFILE_ID,
            )
        elif boundary == "authorized-qualification-core":
            monkeypatch.setattr(
                openrouter_driver, "_run_episode_core", forbidden
            )
            openrouter_driver._run_episode_authorized(
                episode,
                logical_model_id="gpt-5.5",
                api_key=API_KEY,
                run_mode="openrouter",
                panel_profile=manifest.FLAGSHIP_PROFILE_ID,
                authorization=(
                    openrouter_driver._LIVE_CHEAP_QUALIFICATION_AUTHORIZATION
                ),
            )
        elif boundary == "public-access-probe":
            monkeypatch.setattr(
                openrouter_driver, "_run_live_access_probe", forbidden
            )
            openrouter_driver.run_live_access_probe(
                logical_model_id="gpt-5.5",
                api_key=API_KEY,
                profile_id=manifest.FLAGSHIP_PROFILE_ID,
            )
        else:
            transport = FakeTransport([])
            openrouter_driver._run_live_access_probe(
                logical_model_id="gpt-5.5",
                profile_id=manifest.FLAGSHIP_PROFILE_ID,
                api_key=API_KEY,
                transport=transport,
                uuid_factory=lambda: (
                    "9ef76c30-b620-4ea7-a719-91f3e46cc8b2"
                ),
                now=openrouter_driver.SequenceClock(),
                sleeper=lambda _seconds: None,
                authorization=(
                    openrouter_driver._LIVE_ACCESS_PROBE_AUTHORIZATION
                ),
            )
            assert transport.calls == []
    assert calls == []


def test_dedicated_live_entrypoints_do_not_accept_dependency_injection(episode):
    transport = FakeTransport([])
    with pytest.raises(TypeError):
        openrouter_driver.run_live_cheap_qualification_episode(
            episode,
            logical_model_id="gpt-5-nano",
            purpose="smoke",
            api_key=API_KEY,
            transport=transport,
        )
    with pytest.raises(TypeError):
        openrouter_driver.run_live_access_probe(
            logical_model_id="gpt-5-nano",
            api_key=API_KEY,
            transport=transport,
        )
    assert transport.calls == []


def test_prior_reasoning_details_are_forwarded_unmodified(episode):
    reasoning = [{
        "type": "reasoning.summary",
        "summary": "Compared the visible evidence.",
        "id": "reasoning-1",
        "format": "openai-responses-v1",
        "index": 0,
    }]
    first_transport = FakeTransport([
        _response(_success_chunks(reasoning=reasoning)),
    ])
    first_request = _one_stage_request(episode)
    first_result = openrouter_driver.run_stage(
        first_request, future_turns=[], transport=first_transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    second_request = _one_stage_request(
        episode,
        stage="stage_2",
        prior={"stage_1": first_result["attempts"][0]["raw_final_message"]},
    )
    second_transport = FakeTransport([_response(_success_chunks())])
    openrouter_driver.run_stage(
        second_request, future_turns=[], transport=second_transport,
        api_key=API_KEY, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        prior_results=[first_result],
    )
    messages = json.loads(second_transport.calls[0]["body"])["messages"]
    assert messages[1]["content"] == ACTION
    assert messages[1]["reasoning_details"] == reasoning


def test_integrity_invalidation_reruns_whole_episode_once_with_fresh_uuid(
        episode):
    ids = iter((
        "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        "54c94821-a36c-4ea7-ae2c-568a1a4410ef",
    ))
    transport = FakeTransport([
        _response(_success_chunks(model="openai/gpt-5.4")),
        *[_response(_success_chunks()) for _ in range(4)],
    ])
    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: next(ids),
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert run["status"] == "complete"
    assert run["integrity_session_count"] == 2
    assert [row["status"] for row in run["sessions"]] == [
        "invalidated", "complete",
    ]
    assert run["sessions"][0]["execution_id"] != run["sessions"][1][
        "execution_id"
    ]
    assert len(transport.calls) == 5


def test_api_key_is_never_persisted_and_descriptor_tamper_fails(episode):
    secret = "sk-live-NeverPersistThisCredential"
    transport = FakeTransport([_response(_success_chunks())])
    request = _one_stage_request(episode)
    result = openrouter_driver.run_stage(
        request, future_turns=[], transport=transport,
        api_key=secret, now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )
    assert transport.calls[0]["headers"]["Authorization"] == "Bearer " + secret
    assert secret not in json.dumps(result, sort_keys=True)
    wire = openrouter_driver.build_wire_request(request, api_key=secret)
    assert secret not in json.dumps(wire.sanitized_descriptor, sort_keys=True)
    tampered = deepcopy(wire.sanitized_descriptor)
    tampered["body"]["provider"]["allow_fallbacks"] = True
    with pytest.raises(ValueError, match="frozen"):
        openrouter_driver.validate_transport_descriptor(
            result,
            tampered,
            request=request,
            prior_results=[],
            future_turns=[],
        )


def test_transient_request_and_response_evidence_hide_api_key_from_repr(
        episode):
    wire = openrouter_driver.build_wire_request(
        _one_stage_request(episode), api_key=API_KEY
    )
    response = openrouter_driver.TransportResponse(
        status=200,
        headers={"X-Diagnostic": API_KEY},
        chunks=[API_KEY.encode("utf-8")],
    )

    assert API_KEY not in repr(wire)
    assert API_KEY not in repr(response)


def test_exact_api_key_echo_in_innocuous_response_body_is_force_redacted(
        episode):
    events = [
        _event(ACTION, finish="stop", extra={"diagnostic": API_KEY}),
        _event(usage=_usage_object()),
        _event(metadata=_metadata()),
    ]
    closed = []
    response = openrouter_driver.TransportResponse(
        status=200,
        headers={"X-Generation-Id": "gen-test"},
        chunks=_sse(*events),
        closer=lambda: closed.append(True),
    )
    transport = FakeTransport([response])

    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver.run_stage(
            _one_stage_request(episode),
            future_turns=[],
            transport=transport,
            api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )

    record = raised.value.failure_record
    serialized = json.dumps({
        "error": str(raised.value),
        "record": record,
    }, sort_keys=True)
    assert API_KEY not in serialized
    assert record["failure_kind"] == "credential_material"
    assert record["raw_bytes_base64"] is None
    assert record["raw_redacted"] is True
    assert record["measurement_ready"] is False
    assert closed == [True]


@pytest.mark.parametrize("escape_mode", ["full", "partial"])
def test_unicode_escaped_exact_api_key_echo_is_force_redacted(
        episode, escape_mode):
    events = [
        _event(ACTION, finish="stop", extra={"diagnostic": API_KEY}),
        _event(usage=_usage_object()),
        _event(metadata=_metadata()),
    ]
    if escape_mode == "full":
        chunks = _sse_with_unicode_escaped_value(events, API_KEY)
    else:
        serialized = [
            json.dumps(event, separators=(",", ":")) for event in events
        ]
        replacement = json.dumps(API_KEY).replace("-", r"\u002d", 1)
        serialized[0] = serialized[0].replace(
            json.dumps(API_KEY), replacement, 1
        )
        chunks = [(
            ": OPENROUTER PROCESSING\n\n"
            + "".join("data: " + payload + "\n\n" for payload in serialized)
            + "data: [DONE]\n\n"
        ).encode("utf-8")]
    transport = FakeTransport([_response(chunks)])

    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver.run_stage(
            _one_stage_request(episode),
            future_turns=[],
            transport=transport,
            api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )

    record = raised.value.failure_record
    assert API_KEY not in json.dumps(record, sort_keys=True)
    assert record["raw_bytes_base64"] is None
    assert record["raw_redacted"] is True
    assert record["measurement_ready"] is False


def test_exact_api_key_echo_in_decoded_event_tree_is_force_redacted(episode):
    decoded_unicode_escape = API_KEY.replace("-", r"\u002d", 1)
    assert API_KEY not in decoded_unicode_escape
    events = [
        _event(
            ACTION,
            finish="stop",
            extra={"diagnostic": decoded_unicode_escape},
        ),
        _event(usage=_usage_object()),
        _event(metadata=_metadata()),
    ]
    transport = FakeTransport([_response(_sse(*events))])

    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver.run_stage(
            _one_stage_request(episode),
            future_turns=[],
            transport=transport,
            api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )

    record = raised.value.failure_record
    serialized = json.dumps(record, sort_keys=True)
    assert API_KEY not in serialized
    assert decoded_unicode_escape not in serialized
    assert record["raw_bytes_base64"] is None
    assert record["raw_redacted"] is True
    assert record["measurement_ready"] is False


@pytest.mark.parametrize("header_location", ["key", "value"])
def test_exact_api_key_echo_in_any_response_header_is_force_redacted(
        header_location):
    model = "openai/gpt-5-nano"
    headers = {"X-Generation-Id": "gen-test"}
    if header_location == "key":
        echoed_header = "X-Diagnostic-" + API_KEY
        headers[echoed_header] = "present"
    else:
        echoed_header = "diagnostic-" + API_KEY + "-echo"
        headers["X-Diagnostic"] = echoed_header
    closed = []
    response = openrouter_driver.TransportResponse(
        status=200,
        headers=headers,
        chunks=_success_chunks(
            model=model,
            provider="Azure",
            metadata=_multiple_endpoint_metadata(model=model),
        ),
        closer=lambda: closed.append(True),
    )
    transport = FakeTransport([response])

    run = openrouter_driver._run_live_access_probe(
        logical_model_id="gpt-5-nano",
        api_key=API_KEY,
        transport=transport,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
        authorization=openrouter_driver._LIVE_ACCESS_PROBE_AUTHORIZATION,
    )

    serialized = json.dumps(run, sort_keys=True)
    record = run["failure_record"]
    assert API_KEY not in serialized
    assert echoed_header not in serialized
    assert run["status"] == "failed"
    assert run["measurement_ready"] is False
    assert record["failure_kind"] == "credential_material"
    assert record["raw_bytes_base64"] is None
    assert record["raw_redacted"] is True
    assert record["measurement_ready"] is False
    assert closed == [True]


@pytest.mark.parametrize(
    "model_visible_location",
    ["current_prompt", "prior_response", "prior_reasoning"],
)
def test_exact_api_key_in_model_visible_body_is_rejected_before_transport(
        episode, model_visible_location):
    prior_results = []
    if model_visible_location == "current_prompt":
        poisoned = deepcopy(episode)
        poisoned["multiturn_script"]["stage_1"] += " " + API_KEY
        request = _one_stage_request(poisoned)
    else:
        prior_response = (
            API_KEY if model_visible_location == "prior_response" else ACTION
        )
        request = _one_stage_request(
            episode,
            stage="stage_2",
            prior={"stage_1": prior_response},
        )
        prior_results = [_crafted_stage_result(
            _one_stage_request(episode),
            raw_final=prior_response,
            reasoning=(
                [{"summary": API_KEY}]
                if model_visible_location == "prior_reasoning" else None
            ),
        )]
    transport = FakeTransport([])

    with pytest.raises(ValueError) as raised:
        openrouter_driver.run_stage(
            request,
            future_turns=[],
            transport=transport,
            api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
            prior_results=prior_results,
        )

    serialized_error = json.dumps({
        "args": raised.value.args,
        "message": str(raised.value),
        "repr": repr(raised.value),
    }, sort_keys=True)
    assert API_KEY not in serialized_error
    assert transport.calls == []


def test_nonmatching_similar_value_remains_allowed_in_request_and_response(
        episode):
    similar = API_KEY[:-1] + "x"
    assert API_KEY not in similar
    candidate = deepcopy(episode)
    candidate["multiturn_script"]["stage_1"] += " " + similar
    events = [
        _event(ACTION, finish="stop", extra={"diagnostic": similar}),
        _event(usage=_usage_object()),
        _event(metadata=_metadata()),
    ]
    transport = FakeTransport([_response(_sse(*events))])

    result = openrouter_driver.run_stage(
        _one_stage_request(candidate),
        future_turns=[],
        transport=transport,
        api_key=API_KEY,
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )

    assert result["terminal_status"] == "complete"
    assert len(transport.calls) == 1
    assert similar in transport.calls[0]["body"].decode("utf-8")
    assert similar in result["attempts"][0]["raw_trace"]
    assert API_KEY not in json.dumps(result, sort_keys=True)


@pytest.mark.parametrize("mutation", [
    "mixed-generation-id",
    "header-generation-mismatch",
    "missing-event-model",
    "missing-event-provider",
])
def test_every_relevant_event_and_route_attempt_is_exactly_attested(
        episode, mutation):
    metadata = _metadata()
    usage = {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
        "prompt_tokens_details": {"cached_tokens": 4},
        "completion_tokens_details": {"reasoning_tokens": 8},
    }
    events = [
        _event(ACTION, finish="stop"),
        _event(usage=usage),
        _event(metadata=metadata),
    ]
    headers = {"X-Generation-Id": "gen-test"}
    if mutation == "mixed-generation-id":
        events[1]["id"] = "gen-other"
    elif mutation == "header-generation-mismatch":
        headers = {"X-Generation-Id": "gen-header"}
    elif mutation == "missing-event-model":
        del events[0]["model"]
    elif mutation == "missing-event-provider":
        del events[1]["provider"]

    result, transport = _run_fixture_stage(
        episode, _sse(*events), headers=headers
    )

    assert len(transport.calls) == 1
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False
    assert result["attempts"][0]["raw_trace"]


@pytest.mark.parametrize("finish_reason", [
    None,
    "error",
    "length",
    "content_filter",
    "tool_calls",
])
def test_nonexact_or_missing_terminal_finish_is_preserved_but_not_measured(
        episode, finish_reason):
    usage = {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
        "prompt_tokens_details": {"cached_tokens": 4},
        "completion_tokens_details": {"reasoning_tokens": 8},
    }
    events = [
        _event(ACTION, finish=finish_reason),
        _event(usage=usage),
        _event(metadata=_metadata()),
    ]
    result, transport = _run_fixture_stage(episode, _sse(*events))

    assert len(transport.calls) == 1
    assert result["terminal_status"] != "complete"
    assert result["integrity"]["measurement_ready"] is False
    assert result["attempts"][0]["raw_final_message"] == ACTION
    assert result["attempts"][0]["raw_trace"]
    assert result["attempts"][0]["error_code"] is not None


@pytest.mark.parametrize("status", ["failed", "incomplete", "error"])
def test_top_level_failure_status_is_terminal_and_never_retried(episode, status):
    events = [
        _event(ACTION, finish="stop", status=status),
        _event(usage={
            "prompt_tokens": 120,
            "completion_tokens": 24,
            "total_tokens": 144,
        }),
        _event(metadata=_metadata()),
    ]
    result, transport = _run_fixture_stage(episode, _sse(*events))

    assert len(transport.calls) == 1
    assert result["terminal_status"] != "complete"
    assert result["attempts"][0]["error_code"] is not None
    assert result["integrity"]["measurement_ready"] is False


@pytest.mark.parametrize("finish_events", [
    ("stop", "stop"),
    ("length", "stop"),
])
def test_multiple_or_conflicting_finish_events_invalidate(
        episode, finish_events):
    usage = {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
    }
    events = [
        _event(ACTION[:10], finish=finish_events[0]),
        _event(ACTION[10:], finish=finish_events[1]),
        _event(usage=usage),
        _event(metadata=_metadata()),
    ]
    result, _transport = _run_fixture_stage(episode, _sse(*events))

    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False


@pytest.mark.parametrize("capability_event", [
    {"choices": [{
        "index": 0,
        "delta": {"function_call": {"name": "lookup", "arguments": "{}"}},
        "finish_reason": None,
    }]},
    {"plugins": [{"id": "web-search"}]},
    {"response": {"healing": {"enabled": True}}},
    {"context_compression": {"type": "middle-out"}},
])
def test_recursive_capability_scan_preserves_and_invalidates(
        episode, capability_event):
    usage = {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
    }
    events = [
        _event(ACTION, finish="stop"),
        _event(usage=usage),
        _event(metadata=_metadata()),
    ]
    events.insert(0, {
        "id": "gen-test",
        "model": "openai/gpt-5.5",
        "provider": "OpenAI",
        **deepcopy(capability_event),
    })
    result, _transport = _run_fixture_stage(episode, _sse(*events))

    assert result["terminal_status"] == "invalidated"
    assert result["tool_events"]
    assert "tool_event" in result["integrity"]["violations"]


def test_unicode_escaped_future_hash_and_lowercase_identifier_invalidate(
        episode):
    usage = {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
    }
    future = episode["multiturn_script"]["stage_2"]
    future_hash = contracts.sha256_utf8(future)
    for leaked, expected_violation in (
        (future_hash, "future_text"),
        ("charitroc-0001", "forbidden_identifier_echo"),
    ):
        events = [
            _event(ACTION, finish="stop", extra={"audit": leaked}),
            _event(usage=usage),
            _event(metadata=_metadata()),
        ]
        chunks = _sse_with_unicode_escaped_value(events, leaked)
        result, _transport = _run_fixture_stage(
            episode,
            chunks,
            future_turns=[{"stage": "stage_2", "content": future}],
        )
        assert result["terminal_status"] == "invalidated"
        assert expected_violation in result["integrity"]["violations"]


def test_unicode_escaped_credential_fails_without_serializing_secret(episode):
    secret = "Bearer sk-review-secret-12345678"
    events = [
        _event(ACTION, finish="stop", extra={"authorization": secret}),
        _event(usage={
            "prompt_tokens": 120,
            "completion_tokens": 24,
            "total_tokens": 144,
        }),
        _event(metadata=_metadata()),
    ]
    chunks = _sse_with_unicode_escaped_value(events, secret)
    transport = FakeTransport([_response(chunks)])

    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver.run_stage(
            _one_stage_request(episode), future_turns=[], transport=transport,
            api_key=API_KEY, now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )

    serialized = json.dumps(raised.value.failure_record, sort_keys=True)
    assert secret not in serialized
    assert raised.value.failure_record["raw_redacted"] is True
    assert raised.value.failure_record["raw_bytes_base64"] is None
    assert raised.value.failure_record["measurement_ready"] is False


def test_descriptor_is_reconstructed_not_accepted_after_rehash(episode):
    request = _one_stage_request(episode)
    transport = FakeTransport([_response(_success_chunks())])
    result = openrouter_driver.run_stage(
        request, future_turns=[], transport=transport, api_key=API_KEY,
        now=openrouter_driver.SequenceClock(), sleeper=lambda _seconds: None,
    )
    wire = openrouter_driver.build_wire_request(request, api_key=API_KEY)
    tampered = deepcopy(wire.sanitized_descriptor)
    tampered["body"]["provider"]["allow_fallbacks"] = True
    forged = contracts.build_stage_result(
        request,
        run_mode="mock",
        returned_provider_model_id=result["returned_provider_model_id"],
        returned_provider_name=result["returned_provider_name"],
        session_id=None,
        transport_request_sha256=contracts.canonical_sha256(tampered),
        attempts=result["attempts"],
        tool_events=result["tool_events"],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )

    with pytest.raises(ValueError, match="frozen"):
        openrouter_driver.validate_transport_descriptor(
            forged,
            tampered,
            request=request,
            prior_results=[],
            future_turns=[],
        )


def test_live_provenance_rejects_all_injected_dependencies(episode):
    transport = FakeTransport([_response(_success_chunks())])
    with pytest.raises(ValueError, match="production defaults"):
        openrouter_driver.run_stage(
            _one_stage_request(episode),
            future_turns=[],
            transport=transport,
            api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
            run_mode="openrouter",
        )
    with pytest.raises(ValueError, match="production defaults"):
        openrouter_driver.run_episode(
            episode,
            logical_model_id="gpt-5.5",
            transport=transport,
            api_key=API_KEY,
            uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
            run_mode="openrouter",
        )
    assert transport.calls == []
    assert callable(openrouter_driver.run_live_episode)


def test_runtime_wire_configuration_uses_predeclared_literal_digest():
    assert openrouter_driver.FROZEN_RUNTIME_WIRE_CONFIGURATION_SHA256 == (
        "f76cd7e9a01f907ccac3bd88d37b0a865ab5698c0bb9859fb18290045077e071"
    )
    assert contracts.canonical_sha256(
        openrouter_driver._runtime_wire_configuration()
    ) == openrouter_driver.FROZEN_RUNTIME_WIRE_CONFIGURATION_SHA256


@pytest.mark.parametrize(("name", "poison"), [
    ("API_URL", "https://example.invalid/v1/chat/completions"),
    ("REQUEST_TIMEOUT_SECONDS", 1),
    ("MAX_COMPLETION_TOKENS", 1),
    ("MAX_TRANSPORT_ATTEMPTS", 1),
    ("MAX_RETRY_DELAY_SECONDS", 1),
    ("MAX_TRACE_BYTES", 128),
    ("SANITIZED_HEADERS", {"Content-Type": "text/plain"}),
    ("STREAMING_ENABLED", False),
    ("REASONING_POLICY", {"effort": "low"}),
    ("RESPONSE_FORMAT_POLICY", {
        "type": "json_object", "name": "changed", "strict": False,
    }),
    ("ROUTING_POLICY", {
        "only": ["Other"], "order": ["Other"], "allow_fallbacks": True,
        "require_parameters": False, "data_collection": "allow", "zdr": False,
    }),
])
def test_mutated_runtime_wire_configuration_fails_before_transport(
        episode, monkeypatch, name, poison):
    monkeypatch.setattr(openrouter_driver, name, poison)
    transport = FakeTransport([_response(_success_chunks())])

    with pytest.raises(ValueError, match="frozen.*configuration|configuration.*frozen"):
        openrouter_driver.run_stage(
            _one_stage_request(episode),
            future_turns=[],
            transport=transport,
            api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )
    assert transport.calls == []


def test_pre_response_transport_errors_retry_and_sink_one_terminal_failure(
        episode):
    transport = TransportSequence([
        openrouter_driver.OpenRouterTransportError("pre-response failure")
        for _ in range(3)
    ])
    sleeps = []
    before = []
    sinks = []

    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=sleeps.append,
        before_stage=lambda event: before.append(deepcopy(event)),
        stage_sink=lambda event: sinks.append(deepcopy(event)),
    )

    assert run["status"] == "failed"
    assert run["integrity_session_count"] == 1
    assert len(transport.calls) == 3
    assert sleeps == [1, 2]
    assert len(before) == len(sinks) == 1
    result = sinks[0]["result"]
    assert result == run["results"][0]
    assert result["terminal_status"] == "failed"
    assert result["transport_retry_count"] == 2
    assert result["integrity"]["violations"] == [
        "provider_identity", "transport_error",
    ]
    assert all(attempt["error_code"] == "transport_error"
               for attempt in result["attempts"])
    assert all(attempt["raw_trace"] == ""
               for attempt in result["attempts"])


def test_pre_response_transport_retry_can_succeed_without_hidden_selection(
        episode):
    transport = TransportSequence([
        openrouter_driver.OpenRouterTransportError("pre-response failure"),
        _response(_success_chunks()),
        *[_response(_success_chunks()) for _ in range(3)],
    ])
    sleeps = []

    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=sleeps.append,
    )

    assert run["status"] == "complete"
    assert sleeps == [1]
    assert len(transport.calls) == 5
    first = run["results"][0]
    assert first["transport_retry_count"] == 1
    assert first["attempts"][0]["raw_trace"] == ""
    assert first["attempts"][0]["error_code"] == "transport_error"
    assert first["integrity"]["integrity_valid"] is True
    assert first["integrity"]["measurement_ready"] is False


def test_strict_utf8_malformed_sse_becomes_exact_invalidated_evidence(episode):
    raw = b'data: {"id":"a","id":"b"}\n\ndata: [DONE]\n\n'
    result, transport = _run_fixture_stage(episode, [raw])

    assert len(transport.calls) == 1
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False
    assert result["transport_retry_count"] == 0
    assert result["attempts"][0]["raw_trace"] == raw.decode("utf-8")
    assert result["attempts"][0]["raw_trace_sha256"] == hashlib.sha256(
        raw
    ).hexdigest()


@pytest.mark.parametrize("failure_kind", ["invalid_utf8", "iterator_failure"])
def test_binary_or_interrupted_stream_failure_record_keeps_all_partial_bytes(
        episode, failure_kind):
    partial = b"data: {\"id\":\"gen-test\"}\n\n"
    if failure_kind == "invalid_utf8":
        chunks = [partial + b"\xff"]
        exact = partial + b"\xff"
    else:
        exact = partial

        def interrupted():
            yield partial
            raise OSError("fixture iterator interrupted")

        chunks = interrupted()
    transport = FakeTransport([_response(chunks)])

    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver.run_stage(
            _one_stage_request(episode), future_turns=[], transport=transport,
            api_key=API_KEY, now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )

    record = raised.value.failure_record
    assert record["failure_kind"] == failure_kind
    assert record["provenance"] == "harness validation, NOT a measurement"
    assert record["measurement_ready"] is False
    assert record["raw_redacted"] is False
    assert base64.b64decode(record["raw_bytes_base64"]) == exact
    assert record["raw_bytes_sha256"] == hashlib.sha256(exact).hexdigest()
    assert record["raw_byte_count"] == len(exact)
    assert len(transport.calls) == 1


def test_episode_stops_and_exposes_nonmeasurement_binary_failure(episode):
    raw = b"data: \xff"
    transport = FakeTransport([_response([raw])])
    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )

    assert run["status"] == "failed"
    assert run["provenance"] == "harness validation, NOT a measurement"
    assert run["measurement_ready"] is False
    assert run["failure_record"]["raw_bytes_sha256"] == hashlib.sha256(
        raw
    ).hexdigest()
    assert len(transport.calls) == 1


@pytest.mark.parametrize("usage_mutation", [
    "missing",
    "before-finish",
    "inconsistent-total",
    "reasoning-exceeds-output",
])
def test_terminal_usage_is_required_ordered_and_arithmetically_consistent(
        episode, usage_mutation):
    usage = {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
        "prompt_tokens_details": {"cached_tokens": 4},
        "completion_tokens_details": {"reasoning_tokens": 8},
    }
    if usage_mutation == "inconsistent-total":
        usage["total_tokens"] = 999
    elif usage_mutation == "reasoning-exceeds-output":
        usage["completion_tokens_details"]["reasoning_tokens"] = 25
    content = _event(ACTION, finish="stop")
    usage_event = _event(usage=usage)
    metadata_event = _event(metadata=_metadata())
    if usage_mutation == "missing":
        events = [content, metadata_event]
    elif usage_mutation == "before-finish":
        events = [usage_event, content, metadata_event]
    else:
        events = [content, usage_event, metadata_event]

    result, transport = _run_fixture_stage(episode, _sse(*events))

    assert len(transport.calls) == 1
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False
    assert result["attempts"][0]["error_code"] is not None


@pytest.mark.parametrize("generation_id", ["", " gen-test "])
def test_empty_or_noncanonical_generation_header_invalidates_without_error(
        episode, generation_id):
    result, _transport = _run_fixture_stage(
        episode,
        _success_chunks(),
        headers={"X-Generation-Id": generation_id},
    )

    assert result["terminal_status"] == "invalidated"
    assert result["attempts"][0]["provider_request_id"] is None


def test_boolean_route_counts_do_not_satisfy_exact_integer_attestation(episode):
    metadata = _metadata()
    metadata["endpoints"]["total"] = True
    result, _transport = _run_fixture_stage(
        episode, _success_chunks(metadata=metadata)
    )

    assert result["terminal_status"] == "invalidated"


@pytest.mark.parametrize("field", ["plugin_call", "web_search_call"])
def test_recursive_capability_scan_rejects_extended_capability_field_names(
        episode, field):
    events = [
        _event(ACTION, finish="stop", extra={
            "provider_extension": {field: {"name": "lookup"}},
        }),
        _event(usage={
            "prompt_tokens": 120,
            "completion_tokens": 24,
            "total_tokens": 144,
        }),
        _event(metadata=_metadata()),
    ]
    result, _transport = _run_fixture_stage(episode, _sse(*events))

    assert result["terminal_status"] == "invalidated"
    assert result["tool_events"]


def test_unicode_escaped_credential_key_alone_is_fail_safe(episode):
    key = "client_secret"
    events = [
        _event(ACTION, finish="stop", extra={key: "opaque-value"}),
        _event(usage={
            "prompt_tokens": 120,
            "completion_tokens": 24,
            "total_tokens": 144,
        }),
        _event(metadata=_metadata()),
    ]
    transport = FakeTransport([_response(
        _sse_with_unicode_escaped_value(events, key)
    )])

    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver.run_stage(
            _one_stage_request(episode), future_turns=[], transport=transport,
            api_key=API_KEY, now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )

    assert raised.value.failure_record["raw_redacted"] is True
    assert raised.value.failure_record["raw_bytes_base64"] is None


def test_iterator_protocol_exception_is_wrapped_with_partial_evidence(episode):
    partial = b'data: {"id":"gen-test"}\n\n'

    def interrupted():
        yield partial
        raise openrouter_driver.OpenRouterProtocolError("fixture failure")

    transport = FakeTransport([_response(interrupted())])
    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver.run_stage(
            _one_stage_request(episode), future_turns=[], transport=transport,
            api_key=API_KEY, now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )

    assert raised.value.failure_record["failure_kind"] == "iterator_failure"
    assert base64.b64decode(
        raised.value.failure_record["raw_bytes_base64"]
    ) == partial


@pytest.mark.parametrize("mutation", ["bad-details", "output-after-usage"])
def test_usage_event_must_be_structurally_terminal(episode, mutation):
    usage = {
        "prompt_tokens": 120,
        "completion_tokens": 24,
        "total_tokens": 144,
    }
    if mutation == "bad-details":
        usage["prompt_tokens_details"] = []
        events = [
            _event(ACTION, finish="stop"),
            _event(usage=usage),
            _event(metadata=_metadata()),
        ]
    else:
        midpoint = len(ACTION) // 2
        events = [
            _event(ACTION[:midpoint], finish="stop"),
            _event(usage=usage),
            _event(ACTION[midpoint:]),
            _event(metadata=_metadata()),
        ]
    result, _transport = _run_fixture_stage(episode, _sse(*events))

    assert result["terminal_status"] == "invalidated"
    assert result["attempts"][0]["error_code"] is not None


@pytest.mark.parametrize("field, value", [
    ("authorization", "Bearer sk-review-secret-12345678"),
    ("client_secret", "opaque-value"),
])
def test_malformed_unicode_escaped_credentials_are_never_persisted(
        episode, field, value):
    raw = (
        'data: {"id":"a","id":"b",'
        + _unicode_json_string(field)
        + ":"
        + _unicode_json_string(value)
        + "}\n\ndata: [DONE]\n\n"
    ).encode("utf-8")
    transport = FakeTransport([_response([raw])])

    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver.run_stage(
            _one_stage_request(episode), future_turns=[], transport=transport,
            api_key=API_KEY, now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
        )

    record = raised.value.failure_record
    assert record["raw_redacted"] is True
    assert record["raw_bytes_base64"] is None
    assert value not in json.dumps(record, sort_keys=True)


def test_conflicting_case_variant_generation_headers_invalidate(episode):
    result, _transport = _run_fixture_stage(
        episode,
        _success_chunks(),
        headers={
            "X-Generation-Id": "gen-test",
            "x-generation-id": "gen-other",
        },
    )

    assert result["terminal_status"] == "invalidated"
    assert result["attempts"][0]["provider_request_id"] is None


def test_free_prior_reasoning_map_cannot_enter_wire_descriptor(episode):
    request = _one_stage_request(
        episode, stage="stage_2", prior={"stage_1": ACTION}
    )
    with pytest.raises(TypeError) as raised:
        openrouter_driver.build_wire_request(
            request,
            api_key=API_KEY,
            prior_reasoning={
                "stage_1": [{"client_secret": "opaque-value"}],
            },
        )
    assert "opaque-value" not in str(raised.value)


def test_stage_runner_does_not_coerce_arbitrary_empty_prior_map(episode):
    transport = FakeTransport([_response(_success_chunks())])
    with pytest.raises(ValueError, match="prior results"):
        openrouter_driver.run_stage(
            _one_stage_request(episode),
            future_turns=[],
            transport=transport,
            api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
            prior_results={},
        )
    assert transport.calls == []


@pytest.mark.parametrize("failure_kind", [
    "terminal_finish",
    "in_band_error",
    "protocol_malformed",
])
def test_episode_does_not_integrity_rerun_transport_or_protocol_failures(
        episode, failure_kind):
    if failure_kind == "terminal_finish":
        bad = _sse(
            _event(ACTION, finish="length"),
            _event(usage=_usage_object()),
            _event(metadata=_metadata()),
        )
    elif failure_kind == "in_band_error":
        bad = _sse(
            _event(ACTION, finish="stop", error={
                "code": 500, "message": "provider failed",
            }),
            _event(usage=_usage_object()),
            _event(metadata=_metadata()),
        )
    else:
        bad = [b'data: {"id":"a","id":"b"}\n\ndata: [DONE]\n\n']
    transport = FakeTransport([
        _response(bad),
        *[_response(_success_chunks()) for _ in range(4)],
    ])
    ids = iter((
        "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        "54c94821-a36c-4ea7-ae2c-568a1a4410ef",
    ))

    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: next(ids),
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )

    assert run["status"] == "invalidated"
    assert run["integrity_session_count"] == 1
    assert len(run["sessions"]) == 1
    assert len(transport.calls) == 1
    assert run["results"][-1]["attempts"][-1]["error_code"] is not None


@pytest.mark.parametrize("later_output", ["content", "reasoning"])
def test_stop_finish_must_be_on_final_output_event(episode, later_output):
    first = _event(ACTION if later_output == "reasoning" else ACTION[:20],
                   finish="stop")
    if later_output == "content":
        later = _event(ACTION[20:])
    else:
        later = _event(reasoning=[{
            "type": "reasoning.summary",
            "summary": "continued after terminal finish",
        }])
    result, transport = _run_fixture_stage(
        episode,
        _sse(
            first,
            later,
            _event(usage=_usage_object()),
            _event(metadata=_metadata()),
        ),
    )

    assert len(transport.calls) == 1
    assert result["terminal_status"] == "invalidated"
    assert result["attempts"][0]["error_code"] is not None


def test_finish_only_terminal_choice_is_valid_final_output_event(episode):
    """OpenAI streams commonly put stop on an empty terminal choice chunk."""
    midpoint = len(ACTION) // 2
    result, transport = _run_fixture_stage(
        episode,
        _sse(
            _event(ACTION[:midpoint]),
            _event(ACTION[midpoint:]),
            _event("", finish="stop"),
            _event(usage=_usage_object()),
            _event(metadata=_metadata()),
        ),
    )

    assert len(transport.calls) == 1
    assert result["terminal_status"] == "complete"
    assert result["attempts"][0]["error_code"] is None


def test_any_choice_event_after_terminal_stop_invalidates(episode):
    result, _transport = _run_fixture_stage(
        episode,
        _sse(
            _event(ACTION),
            _event("", finish="stop"),
            _event(""),
            _event(usage=_usage_object()),
            _event(metadata=_metadata()),
        ),
    )

    assert result["terminal_status"] == "invalidated"
    assert result["attempts"][0]["error_code"] is not None


@pytest.mark.parametrize("marker", [
    {"response": {"status": "FAILED"}},
    {"response": {"kind": "Cancelled"}},
    {"response": {"type": "REJECTED"}},
    {"response": {"state": "Aborted"}},
    {"response": {"status": 503}},
    {"response": {"status": 503.0}},
    {"response": {"error": {"status": 429}}},
    {"response": {"status": "failure"}},
    {"response": {"status": "timed_out"}},
    {"response": {"status": "expired"}},
    {"response": {"error": {}}},
])
def test_recursive_failure_markers_preserve_and_invalidate(episode, marker):
    result, transport = _run_fixture_stage(
        episode,
        _sse(
            _event(ACTION, finish="stop", extra=marker),
            _event(usage=_usage_object()),
            _event(metadata=_metadata()),
        ),
    )

    assert len(transport.calls) == 1
    assert result["terminal_status"] == "invalidated"
    assert result["attempts"][0]["error_code"] is not None
    assert result["attempts"][0]["raw_trace"]


def test_semantic_failure_words_in_model_content_are_not_status_markers(episode):
    semantic = json.dumps({
        "reason": "The report uses ERROR, FAILED, and ABORTED as quoted words.",
        "INTENT": "UNCERTAIN",
        "DECISION": "VERIFY",
    }, separators=(",", ":"))
    result, _transport = _run_fixture_stage(
        episode, _success_chunks(content=semantic)
    )

    assert result["terminal_status"] == "complete"
    assert result["attempts"][0]["error_code"] is None


@pytest.mark.parametrize("capability", [
    {"delta_key": "function_call", "value": {}},
    {"top_key": "plugins", "value": []},
    {"top_key": "tool_calls", "value": None},
    {"marker_key": "type", "value": "function"},
    {"marker_key": "kind", "value": "WEB_SEARCH"},
])
def test_capability_presence_or_structural_marker_always_invalidates(
        episode, capability):
    first = _event(ACTION, finish="stop")
    if "delta_key" in capability:
        first["choices"][0]["delta"][capability["delta_key"]] = capability[
            "value"]
    elif "top_key" in capability:
        first[capability["top_key"]] = capability["value"]
    else:
        first["extension"] = {
            capability["marker_key"]: capability["value"],
        }
    result, _transport = _run_fixture_stage(
        episode,
        _sse(
            first,
            _event(usage=_usage_object()),
            _event(metadata=_metadata()),
        ),
    )

    assert result["terminal_status"] == "invalidated"
    assert result["tool_events"]
    assert "tool_event" in result["integrity"]["violations"]


def test_wire_reasoning_is_derived_from_bound_prior_results(episode):
    stage_1 = _one_stage_request(episode)
    reasoning = [{
        "type": "reasoning.summary",
        "summary": "Compared only the visible first-stage evidence.",
    }]
    prior_result = _crafted_stage_result(stage_1, reasoning=reasoning)
    stage_2 = _one_stage_request(
        episode, stage="stage_2", prior={"stage_1": ACTION}
    )
    future_turns = [
        {"stage": stage, "content": episode["multiturn_script"][stage]}
        for stage in ("stage_3", "stage_4")
    ]

    wire = openrouter_driver.build_wire_request(
        stage_2,
        api_key=API_KEY,
        prior_results=[prior_result],
        future_turns=future_turns,
    )

    messages = json.loads(wire.body)["messages"]
    assert messages[1]["reasoning_details"] == reasoning
    with pytest.raises(TypeError):
        openrouter_driver.build_wire_request(
            stage_2,
            api_key=API_KEY,
            prior_reasoning={"stage_1": reasoning},
        )


def test_bound_prior_result_must_match_exact_request_history(episode):
    stage_1 = _one_stage_request(episode)
    alternate = json.dumps({
        "reason": "A different raw prior response.",
        "INTENT": "UNCERTAIN",
        "DECISION": "VERIFY",
    }, separators=(",", ":"))
    prior_result = _crafted_stage_result(stage_1, raw_final=alternate)
    stage_2 = _one_stage_request(
        episode, stage="stage_2", prior={"stage_1": ACTION}
    )

    with pytest.raises(ValueError, match="history"):
        openrouter_driver.build_wire_request(
            stage_2,
            api_key=API_KEY,
            prior_results=[prior_result],
            future_turns=[],
        )


def test_derived_reasoning_cannot_expose_current_or_future_episode_turns(
        episode):
    stage_1 = _one_stage_request(episode)
    stage_2_text = episode["multiturn_script"]["stage_2"]
    prior_result = _crafted_stage_result(
        stage_1,
        reasoning=[{"summary": stage_2_text}],
    )
    stage_2 = _one_stage_request(
        episode, stage="stage_2", prior={"stage_1": ACTION}
    )

    with pytest.raises(ValueError, match="future"):
        openrouter_driver.build_wire_request(
            stage_2,
            api_key=API_KEY,
            prior_results=[prior_result],
            future_turns=[
                {"stage": stage, "content": episode["multiturn_script"][stage]}
                for stage in ("stage_3", "stage_4")
            ],
        )


def test_bound_raw_history_cannot_expose_later_episode_turns(episode):
    stage_4_hash = contracts.sha256_utf8(
        episode["multiturn_script"]["stage_4"]
    )
    leaked = json.dumps({
        "reason": "Unavailable later hash: " + stage_4_hash,
        "INTENT": "UNCERTAIN",
        "DECISION": "VERIFY",
    }, separators=(",", ":"))
    stage_1 = _one_stage_request(episode)
    prior_result = _crafted_stage_result(stage_1, raw_final=leaked)
    stage_2 = deepcopy(_one_stage_request(
        episode, stage="stage_2", prior={"stage_1": ACTION}
    ))
    stage_2["prior_visible_turns"][0]["response"] = leaked
    stage_2["request_sha256"] = contracts.canonical_sha256({
        key: value for key, value in stage_2.items()
        if key != "request_sha256"
    })
    stage_2 = contracts.validate_stage_request(stage_2)

    with pytest.raises(ValueError, match="future"):
        openrouter_driver.build_wire_request(
            stage_2,
            api_key=API_KEY,
            prior_results=[prior_result],
            future_turns=[
                {"stage": stage, "content": episode["multiturn_script"][stage]}
                for stage in ("stage_3", "stage_4")
            ],
        )


def test_episode_descriptor_validator_binds_full_prefix(episode):
    transport = FakeTransport([
        _response(_success_chunks()) for _ in range(4)
    ])
    run = openrouter_driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        transport=transport,
        api_key=API_KEY,
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        now=openrouter_driver.SequenceClock(),
        sleeper=lambda _seconds: None,
    )

    assert openrouter_driver.validate_episode_transport_descriptors(
        episode,
        run["requests"],
        run["results"],
        run["transport_descriptors"],
    ) == run["transport_descriptors"]


@pytest.mark.parametrize(("logical_model_id", "profile_id", "run_mode", "label"), [
    (
        "gpt-5.5", manifest.FLAGSHIP_PROFILE_ID, "openrouter",
        "live OpenRouter calibration attempt, NOT a measurement",
    ),
    (
        "gpt-5-nano", manifest.CHEAP_PROFILE_ID, "openrouter",
        "live OpenRouter qualification attempt, NOT a measurement",
    ),
    (
        "gpt-5-nano", manifest.CHEAP_PROFILE_ID, "openrouter_probe",
        "live OpenRouter access probe attempt, NOT a measurement",
    ),
    (
        "gpt-5.4-mini", manifest.GPT54_MINI_PROFILE_ID, "openrouter",
        "live OpenRouter qualification attempt, NOT a measurement",
    ),
    (
        "gpt-5.4-mini", manifest.GPT54_MINI_PROFILE_ID,
        "openrouter_probe",
        "live OpenRouter access probe attempt, NOT a measurement",
    ),
])
def test_live_failure_record_is_attempt_not_measurement_and_identity_bound(
        episode, logical_model_id, profile_id, run_mode, label):
    request_episode = (
        manifest.build_cheap_access_probe(
            logical_model_id, profile_id=profile_id
        )
        if run_mode == "openrouter_probe" else episode
    )
    request = _one_stage_request(
        request_episode,
        logical_model_id=logical_model_id,
        panel_profile=profile_id,
    )
    transport = FakeTransport([_response([b"data: \xff"])])
    expected_wire = openrouter_driver.build_wire_request(
        request,
        api_key=API_KEY,
        prior_results=[],
        future_turns=[],
    )

    with pytest.raises(openrouter_driver.OpenRouterProtocolError) as raised:
        openrouter_driver._run_stage_record(
            request,
            future_turns=[],
            transport=transport,
            api_key=API_KEY,
            now=openrouter_driver.SequenceClock(),
            sleeper=lambda _seconds: None,
            prior_results=[],
            run_mode=run_mode,
        )

    record = raised.value.failure_record
    assert record["provenance"] == label
    assert record["run_mode"] == run_mode
    assert record["measurement_ready"] is False
    assert record["provider"] == "openrouter"
    assert record["logical_model_id"] == logical_model_id
    assert record["provider_model_id"] == f"openai/{logical_model_id}"
    assert record["configuration_id"] == request["configuration_id"]
    assert record["request_sha256"] == request["request_sha256"]
    assert record["transport_request_sha256"] == (
        expected_wire.transport_request_sha256
    )
    assert API_KEY not in json.dumps(record, sort_keys=True)
