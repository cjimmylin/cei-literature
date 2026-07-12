"""Fail-closed tests for the provider-neutral staged request boundary."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import uuid

import pytest
import yaml

from pilot import contracts


BANK = Path(__file__).resolve().parents[1]
EXECUTION_ID = "9ef76c30-b620-4ea7-a719-91f3e46cc8b2"
RESPONSE = json.dumps({
    "reason": "The evidence remains incomplete.",
    "INTENT": "UNCERTAIN",
    "DECISION": "VERIFY",
}, sort_keys=True)
REQUEST_KEYS = {
    "contract_version",
    "execution_id",
    "provider",
    "logical_model_id",
    "provider_model_id",
    "configuration_id",
    "stage",
    "prior_visible_turns",
    "current_visible_turn",
    "response_schema",
    "response_schema_sha256",
    "request_sha256",
}


@pytest.fixture(scope="module")
def episode():
    rows = yaml.safe_load((BANK / "seeds_public.yaml").read_text())
    assert rows
    return rows[0]


def _identity(provider="codex", logical="gpt-5.5"):
    if provider == "codex":
        return {
            "provider": provider,
            "logical_model_id": logical,
            "provider_model_id": logical,
            "configuration_id": f"codex-cli-{logical}-medium-isolated",
        }
    return {
        "provider": provider,
        "logical_model_id": logical,
        "provider_model_id": f"openai/{logical}",
        "configuration_id": (
            f"openrouter-openai-{logical}-medium-no-fallback"
        ),
    }


def _cheap_identity(logical="gpt-5-nano"):
    return {
        key: value for key, value in contracts.manifest.resolve_openrouter_identity(
            logical, profile_id="cheap-azure-v1"
        ).items()
        if key in {
            "provider", "logical_model_id", "provider_model_id",
            "configuration_id",
        }
    }


def _gpt54_mini_identity():
    return {
        key: value for key, value in contracts.manifest.resolve_openrouter_identity(
            "gpt-5.4-mini", profile_id="gpt54-mini-azure-v1"
        ).items()
        if key in {
            "provider", "logical_model_id", "provider_model_id",
            "configuration_id",
        }
    }


def _build(episode, *, stage="stage_2", provider="codex",
           logical="gpt-5.5", prior_responses=None, execution_id=EXECUTION_ID):
    if prior_responses is None:
        prior_responses = {"stage_1": RESPONSE} if stage == "stage_2" else {}
    return contracts.build_stage_request(
        episode,
        execution_id=execution_id,
        stage=stage,
        prior_responses=prior_responses,
        **_identity(provider, logical),
    )


def _rehash(request):
    request["request_sha256"] = contracts.canonical_sha256({
        key: value for key, value in request.items()
        if key != "request_sha256"
    })
    return request


def test_builder_emits_only_exact_stage_request_keys_and_validates(episode):
    request = _build(episode)

    assert set(request) == REQUEST_KEYS
    assert request["contract_version"] == "charitroc-stage-request-v1"
    assert request["execution_id"] == EXECUTION_ID
    assert request["stage"] == "stage_2"
    assert request["prior_visible_turns"] == [{
        "stage": "stage_1",
        "prompt": episode["multiturn_script"]["stage_1"],
        "response": RESPONSE,
    }]
    assert request["current_visible_turn"] == {
        "stage": "stage_2",
        "content": episode["multiturn_script"]["stage_2"],
    }
    assert request["response_schema_sha256"] == (
        contracts.canonical_sha256(request["response_schema"])
    )
    assert request["request_sha256"] == contracts.canonical_sha256({
        key: value for key, value in request.items()
        if key != "request_sha256"
    })
    assert contracts.validate_stage_request(request) == request


@pytest.mark.parametrize("provider,logical", [
    ("codex", "gpt-5.5"),
    ("codex", "gpt-5.4"),
    ("codex", "gpt-5.4-mini"),
    ("openrouter", "gpt-5.5"),
    ("openrouter", "gpt-5.4"),
    ("openrouter", "gpt-5.4-mini"),
])
def test_all_and_only_frozen_panel_identity_tuples_build(
        episode, provider, logical):
    request = _build(episode, provider=provider, logical=logical)
    assert contracts.validate_stage_request(request) == request


@pytest.mark.parametrize("logical", [
    "gpt-5-nano", "gpt-5.4-nano", "gpt-5-mini",
])
def test_exact_cheap_profile_identity_tuples_build(episode, logical):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_cheap_identity(logical),
    )
    assert contracts.validate_stage_request(request) == request


def test_exact_gpt54_mini_qualification_identity_tuple_builds(episode):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_gpt54_mini_identity(),
    )
    assert contracts.validate_stage_request(request) == request


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("logical_model_id", "gpt-5.5"),
        ("provider_model_id", "openai/gpt-5-mini"),
        (
            "configuration_id",
            "openrouter-openai-gpt-5-nano-medium-no-fallback",
        ),
        ("provider", "codex"),
    ],
)
def test_cross_profile_identity_mixing_fails_even_when_rehashed(
        episode, field, bad_value):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_cheap_identity(),
    )
    request[field] = bad_value
    _rehash(request)

    with pytest.raises(ValueError, match="frozen panel"):
        contracts.validate_stage_request(request)


@pytest.mark.parametrize("field,bad_value", [
    ("provider", "sol"),
    ("logical_model_id", "gpt-5.6-sol"),
    ("provider_model_id", "gpt-5.4"),
    ("configuration_id", "codex-cli-gpt-5.5-medium-isolated"),
])
def test_wrong_or_mixed_provider_tuple_fails_even_when_rehashed(
        episode, field, bad_value):
    request = _build(episode, provider="openrouter", logical="gpt-5.4")
    request[field] = bad_value
    _rehash(request)

    with pytest.raises(ValueError, match="frozen panel"):
        contracts.validate_stage_request(request)


@pytest.mark.parametrize("mutation", ["missing", "extra", "rehashed-version"])
def test_missing_extra_and_rehashed_structural_poison_fails(episode, mutation):
    request = _build(episode)
    if mutation == "missing":
        del request["configuration_id"]
    elif mutation == "extra":
        request["item_id"] = "opaque-but-forbidden"
    else:
        request["contract_version"] = "charitroc-stage-request-v2"
    _rehash(request)

    with pytest.raises(ValueError):
        contracts.validate_stage_request(request)


def test_response_schema_and_schema_hash_are_both_frozen(episode):
    request = _build(episode)
    request["response_schema"]["properties"]["reason"]["maxLength"] = 401
    request["response_schema_sha256"] = contracts.canonical_sha256(
        request["response_schema"]
    )
    _rehash(request)
    with pytest.raises(ValueError, match="response schema"):
        contracts.validate_stage_request(request)

    request = _build(episode)
    request["response_schema_sha256"] = "0" * 64
    _rehash(request)
    with pytest.raises(ValueError, match="response schema hash"):
        contracts.validate_stage_request(request)


@pytest.mark.parametrize("execution_id", [
    "9EF76C30-B620-4EA7-A719-91F3E46CC8B2",
    "9ef76c30-b620-1ea7-a719-91f3e46cc8b2",
    "9ef76c30-b620-4ea7-7719-91f3e46cc8b2",
    str(uuid.uuid5(uuid.NAMESPACE_DNS, "not-v4")),
    "not-a-uuid",
])
def test_execution_id_is_strict_lowercase_rfc4122_uuidv4(
        episode, execution_id):
    with pytest.raises(ValueError, match="execution_id"):
        _build(episode, execution_id=execution_id)


@pytest.mark.parametrize("stage,prior_responses", [
    ("stage_1", {"stage_1": RESPONSE}),
    ("stage_2", {}),
    ("stage_2", {"stage_1": RESPONSE, "stage_2": RESPONSE}),
    ("stage_3", {"stage_1": RESPONSE}),
    ("stage_3", {"stage_1": RESPONSE, "stage_3": RESPONSE}),
    ("stage_5", {}),
])
def test_builder_rejects_missing_future_or_noncontiguous_history(
        episode, stage, prior_responses):
    with pytest.raises(ValueError):
        _build(episode, stage=stage, prior_responses=prior_responses)


@pytest.mark.parametrize("exposure", ["text", "hash"])
def test_builder_rejects_future_stage_text_or_hash_in_prior_response(
        episode, exposure):
    future = episode["multiturn_script"]["stage_3"]
    leaked = future if exposure == "text" else contracts.sha256_utf8(future)
    with pytest.raises(ValueError, match="future-stage"):
        _build(
            episode,
            stage="stage_2",
            prior_responses={"stage_1": "Leaked value: " + leaked},
        )


def test_validator_rejects_reordered_or_wrong_stage_history_even_when_rehashed(
        episode):
    request = _build(
        episode,
        stage="stage_4",
        prior_responses={
            "stage_1": RESPONSE,
            "stage_2": RESPONSE,
            "stage_3": RESPONSE,
        },
    )
    request["prior_visible_turns"][0], request["prior_visible_turns"][1] = (
        request["prior_visible_turns"][1],
        request["prior_visible_turns"][0],
    )
    _rehash(request)

    with pytest.raises(ValueError, match="history"):
        contracts.validate_stage_request(request)


def test_builder_extracts_visible_turns_from_full_episode_without_leaking_ids(
        episode):
    request = _build(episode)
    serialized = contracts.dumps_stage_request(request)

    assert episode["id"] not in serialized
    assert episode["canary"] not in serialized
    assert episode["template_family"] not in serialized
    assert episode["split"] not in serialized
    assert "CHARITROC-" not in serialized
    assert "10CB-07-" not in serialized


def test_full_episode_or_sidecar_objects_cannot_cross_validator_boundary(episode):
    with pytest.raises(ValueError):
        contracts.validate_stage_request(episode)
    with pytest.raises(ValueError):
        contracts.build_stage_request(
            {"true_type": "benign", "label": 1},
            execution_id=EXECUTION_ID,
            stage="stage_1",
            prior_responses={},
            **_identity(),
        )

    request = _build(episode)
    request["current_visible_turn"]["sidecar"] = {
        "true_type": "benign",
        "label": 1,
    }
    _rehash(request)
    with pytest.raises(ValueError):
        contracts.validate_stage_request(request)


@pytest.mark.parametrize("sentinel", [
    "10CB-07-452ec262-8025-449d-bfb0-788e122135bd",
    "CHARITROC-0577",
    "JUDGE-a19ca5c6-ce54-42cb-84be-83025d5f52cf",
])
def test_visible_strings_reject_bank_and_judge_identifiers_without_echo(
        episode, sentinel):
    request = _build(episode)
    request["current_visible_turn"]["content"] += " " + sentinel
    _rehash(request)
    with pytest.raises(ValueError) as raised:
        contracts.validate_stage_request(request)
    assert sentinel not in str(raised.value)


def test_secret_keys_and_values_are_rejected_recursively_without_echo(episode):
    sentinel = "sk-live-NeverEchoThisSecretValue"
    request = _build(episode)
    request["current_visible_turn"]["api_key"] = sentinel
    _rehash(request)
    with pytest.raises(ValueError) as raised:
        contracts.validate_stage_request(request)
    assert sentinel not in str(raised.value)

    with pytest.raises(ValueError) as raised:
        _build(episode, prior_responses={"stage_1": sentinel})
    assert sentinel not in str(raised.value)


def test_canonical_hash_is_key_order_invariant_and_content_sensitive():
    left = {"b": [2, {"d": "four", "c": 3}], "a": 1}
    right = {"a": 1, "b": [2, {"c": 3, "d": "four"}]}
    changed = {"a": 1, "b": [2, {"c": 3, "d": "FOUR"}]}

    assert contracts.canonical_sha256(left) == contracts.canonical_sha256(right)
    assert contracts.canonical_sha256(left) != contracts.canonical_sha256(changed)
    assert contracts.canonical_json_bytes(left) == (
        b'{"a":1,"b":[2,{"c":3,"d":"four"}]}'
    )


def test_request_hash_is_content_sensitive(episode):
    request = _build(episode)
    request["current_visible_turn"]["content"] += " changed"
    with pytest.raises(ValueError, match="request hash"):
        contracts.validate_stage_request(request)


@pytest.mark.parametrize("mutation", [
    lambda request: request.update(stage=2),
    lambda request: request.update(prior_visible_turns=tuple(
        request["prior_visible_turns"]
    )),
    lambda request: request["current_visible_turn"].update(content=7),
    lambda request: request.update(response_schema_sha256=b"0" * 64),
])
def test_exact_json_types_are_enforced(episode, mutation):
    request = _build(episode)
    mutation(request)
    with pytest.raises(ValueError):
        contracts.validate_stage_request(request)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), -float("inf")])
def test_canonical_json_and_contract_reject_nonfinite_numbers(episode, value):
    with pytest.raises(ValueError, match="canonical JSON"):
        contracts.canonical_json_bytes({"value": value})

    request = _build(episode)
    request["response_schema"]["poison"] = value
    with pytest.raises(ValueError):
        contracts.validate_stage_request(request)


def test_duplicate_json_keys_are_rejected_without_echoing_key_or_value():
    sentinel = "sk-live-NeverEchoThisSecretValue"
    payload = '{"api_key":"safe","api_key":"' + sentinel + '"}'
    with pytest.raises(ValueError) as raised:
        contracts.loads_stage_request(payload)
    assert "api_key" not in str(raised.value)
    assert sentinel not in str(raised.value)


def test_dumps_is_canonical_and_loads_round_trip_validates(episode):
    request = _build(episode)
    encoded = contracts.dumps_stage_request(request)

    assert encoded.encode("utf-8") == contracts.canonical_json_bytes(request)
    assert contracts.loads_stage_request(encoded) == request


def test_validator_rejects_request_hash_mismatch(episode):
    request = _build(episode)
    request["request_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="request hash"):
        contracts.validate_stage_request(request)


def test_validator_does_not_mutate_caller_input(episode):
    request = _build(episode)
    original = deepcopy(request)
    validated = contracts.validate_stage_request(request)
    assert request == original
    assert validated == original
    assert validated is not request


# StageResult/Attempt RED contract -------------------------------------------------

USAGE = {
    "input_tokens": 100,
    "cached_input_tokens": 20,
    "output_tokens": 30,
    "reasoning_tokens": 10,
    "total_tokens": 130,
}


def _stage_one_request(episode, provider="codex", logical="gpt-5.5"):
    return _build(
        episode,
        stage="stage_1",
        provider=provider,
        logical=logical,
        prior_responses={},
    )


def _attempt(*, response=RESPONSE, index=1, token_started=True,
             error_code=None, raw_trace='{"type":"turn.completed"}',
             started="2026-07-10T12:00:00Z",
             completed="2026-07-10T12:00:01Z", usage=USAGE,
             reasoning_details=None):
    return contracts.build_stage_attempt(
        attempt_index=index,
        started_at_utc=started,
        completed_at_utc=completed,
        provider_request_id=f"provider-request-{index}",
        token_emission_started=token_started,
        exit_status=0 if error_code is None else 1,
        http_status=200 if error_code is None else 503,
        finish_reason="stop" if error_code is None else None,
        usage=usage,
        raw_trace=raw_trace,
        raw_final_message=response,
        reasoning_effort="medium",
        reasoning_details=reasoning_details,
        error_code=error_code,
    )


def _result(episode, *, provider="codex", run_mode=None, attempts=None,
            returned_model=None, returned_provider="OpenAI", session_id=None,
            tool_events=None, session_chain_ok=True, isolation_ok=True,
            future_text_absent=True):
    request = _stage_one_request(episode, provider=provider)
    if run_mode is None:
        run_mode = provider
    if attempts is None:
        attempts = [_attempt()]
    if returned_model is None:
        returned_model = request["provider_model_id"]
    if session_id is None and provider == "codex":
        session_id = "019f49e3-b7de-7272-9d25-545c82c2674c"
    result = contracts.build_stage_result(
        request,
        run_mode=run_mode,
        returned_provider_model_id=returned_model,
        returned_provider_name=returned_provider,
        session_id=session_id,
        transport_request_sha256="a" * 64,
        attempts=attempts,
        tool_events=[] if tool_events is None else tool_events,
        session_chain_ok=session_chain_ok,
        isolation_ok=isolation_ok,
        future_text_absent=future_text_absent,
    )
    return request, result


def test_complete_codex_result_is_exact_hashed_and_measurement_ready(episode):
    request, result = _result(episode)

    assert set(result) == contracts.STAGE_RESULT_KEYS
    assert result["provenance"] == "live Codex calibration measurement"
    assert result["terminal_status"] == "complete"
    assert result["integrity"]["integrity_valid"] is True
    assert result["integrity"]["mechanically_resolved"] is True
    assert result["integrity"]["measurement_ready"] is True
    assert result["attempts"][0]["parsed_response"] == json.loads(RESPONSE)
    assert result["result_sha256"] == contracts.canonical_sha256({
        key: value for key, value in result.items() if key != "result_sha256"
    })
    assert contracts.validate_stage_result(result, request) == result


def test_openrouter_result_requires_null_session_and_exact_provenance(episode):
    request, result = _result(episode, provider="openrouter", session_id=None)
    assert result["session_id"] is None
    assert result["provenance"] == "live OpenRouter calibration measurement"
    assert result["integrity"]["measurement_ready"] is True
    assert contracts.validate_stage_result(result, request) == result


def test_cheap_openrouter_result_requires_azure_provider_identity(episode):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_cheap_identity(),
    )
    result = contracts.build_stage_result(
        request,
        run_mode="openrouter",
        returned_provider_model_id="openai/gpt-5-nano-2025-08-07",
        returned_provider_name="Azure",
        session_id=None,
        transport_request_sha256="a" * 64,
        attempts=[_attempt()],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )

    assert result["provenance"] == (
        "live OpenRouter qualification measurement"
    )
    assert result["integrity"]["provider_identity_ok"] is True
    assert result["integrity"]["measurement_ready"] is True
    assert contracts.validate_stage_result(result, request) == result


def test_cheap_openrouter_probe_builds_valid_nonmeasurement_result(episode):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_cheap_identity(),
    )
    result = contracts.build_stage_result(
        request,
        run_mode="openrouter_probe",
        returned_provider_model_id="openai/gpt-5-nano-2025-08-07",
        returned_provider_name="Azure",
        session_id=None,
        transport_request_sha256="a" * 64,
        attempts=[_attempt()],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )

    assert result["provenance"] == (
        "live OpenRouter access probe, NOT a measurement"
    )
    assert result["terminal_status"] == "complete"
    assert result["integrity"]["integrity_valid"] is True
    assert result["integrity"]["measurement_ready"] is False
    assert contracts.validate_stage_result(result, request) == result


@pytest.mark.parametrize("run_mode", ["openrouter", "openrouter_probe"])
def test_gpt54_mini_qualification_result_uses_exact_azure_provenance(
        episode, run_mode):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_gpt54_mini_identity(),
    )
    result = contracts.build_stage_result(
        request,
        run_mode=run_mode,
        returned_provider_model_id="openai/gpt-5.4-mini-20260317",
        returned_provider_name="Azure",
        session_id=None,
        transport_request_sha256="a" * 64,
        attempts=[_attempt()],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )

    assert result["provenance"] == (
        "live OpenRouter qualification measurement"
        if run_mode == "openrouter"
        else "live OpenRouter access probe, NOT a measurement"
    )
    assert result["integrity"]["provider_identity_ok"] is True
    assert result["integrity"]["measurement_ready"] is (
        run_mode == "openrouter"
    )
    assert contracts.validate_stage_result(result, request) == result


@pytest.mark.parametrize("provider", ["codex", "openrouter"])
def test_openrouter_probe_rejects_flagship_and_codex_identities(
        episode, provider):
    request = _stage_one_request(episode, provider=provider)
    with pytest.raises(ValueError, match="probe|run_mode|profile"):
        contracts.build_stage_result(
            request,
            run_mode="openrouter_probe",
            returned_provider_model_id=request["provider_model_id"],
            returned_provider_name="OpenAI",
            session_id=(
                "019f49e3-b7de-7272-9d25-545c82c2674c"
                if provider == "codex" else None
            ),
            transport_request_sha256="a" * 64,
            attempts=[_attempt()],
            tool_events=[],
            session_chain_ok=True,
            isolation_ok=True,
            future_text_absent=True,
        )


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("provenance", "live OpenRouter calibration measurement"),
        ("run_mode", "openrouter_probe"),
    ],
)
def test_cheap_result_rejects_rehashed_provenance_or_run_mode_tamper(
        episode, field, bad_value):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_cheap_identity(),
    )
    result = contracts.build_stage_result(
        request,
        run_mode="openrouter",
        returned_provider_model_id=request["provider_model_id"],
        returned_provider_name="Azure",
        session_id=None,
        transport_request_sha256="a" * 64,
        attempts=[_attempt()],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )
    result[field] = bad_value
    result["result_sha256"] = contracts.canonical_sha256({
        key: value for key, value in result.items()
        if key != "result_sha256"
    })

    with pytest.raises(ValueError, match="provenance|integrity|run_mode"):
        contracts.validate_stage_result(result, request)


def test_cheap_openrouter_result_rejects_flagship_returned_provider(episode):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_cheap_identity(),
    )
    result = contracts.build_stage_result(
        request,
        run_mode="openrouter",
        returned_provider_model_id="openai/gpt-5-nano-2025-08-07",
        returned_provider_name="OpenAI",
        session_id=None,
        transport_request_sha256="a" * 64,
        attempts=[_attempt()],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )

    assert result["integrity"]["provider_identity_ok"] is False
    assert result["terminal_status"] == "invalidated"
    assert "provider_identity" in result["integrity"]["violations"]
    assert result["integrity"]["measurement_ready"] is False
    assert contracts.validate_stage_result(result, request) == result


@pytest.mark.parametrize("returned_model", [
    "openai/gpt-5-nano",
    "openai/gpt-5-nano-2099-01-01",
    "openai/gpt-5-mini-2025-08-07",
])
def test_cheap_openrouter_result_rejects_unfrozen_returned_model(
        episode, returned_model):
    request = contracts.build_stage_request(
        episode,
        execution_id=EXECUTION_ID,
        stage="stage_1",
        prior_responses={},
        **_cheap_identity(),
    )
    result = contracts.build_stage_result(
        request,
        run_mode="openrouter",
        returned_provider_model_id=returned_model,
        returned_provider_name="Azure",
        session_id=None,
        transport_request_sha256="a" * 64,
        attempts=[_attempt()],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )

    assert result["integrity"]["provider_identity_ok"] is False
    assert result["integrity"]["measurement_ready"] is False
    assert result["terminal_status"] == "invalidated"


def test_mock_result_is_explicitly_not_a_measurement(episode):
    request, result = _result(episode, run_mode="mock")
    assert result["provenance"] == "harness validation, NOT a measurement"
    assert result["terminal_status"] == "complete"
    assert result["integrity"]["integrity_valid"] is True
    assert result["integrity"]["measurement_ready"] is False
    assert contracts.validate_stage_result(result, request) == result


def test_invalid_json_is_preserved_unresolved_without_retry_or_repair(episode):
    raw = "INTENT: UNCERTAIN\nDECISION: VERIFY"
    request, result = _result(episode, attempts=[_attempt(response=raw)])
    attempt = result["attempts"][0]
    assert attempt["raw_final_message"] == raw
    assert attempt["parsed_response"] is None
    assert attempt["parsed_response_sha256"] is None
    assert attempt["parse_mode"] == "unresolved"
    assert result["transport_retry_count"] == 0
    assert result["terminal_status"] == "unresolved"
    assert result["integrity"]["integrity_valid"] is True
    assert result["integrity"]["measurement_ready"] is False
    assert not any("repair" in key for key in contracts.STAGE_ATTEMPT_KEYS)


def test_pre_token_transport_failure_can_retry_and_preserves_attempts(episode):
    failed = _attempt(
        response=None,
        token_started=False,
        error_code="provider_unavailable",
        raw_trace='{"error":"provider_unavailable"}',
    )
    success = _attempt(
        index=2,
        started="2026-07-10T12:00:02Z",
        completed="2026-07-10T12:00:03Z",
    )
    _, result = _result(episode, attempts=[failed, success])
    assert result["transport_retry_count"] == 1
    assert [row["attempt_index"] for row in result["attempts"]] == [1, 2]
    assert result["attempts"][0]["error_code"] == "provider_unavailable"
    assert result["terminal_status"] == "complete"


@pytest.mark.parametrize("first", [
    lambda: _attempt(response="not-json", token_started=True),
    lambda: _attempt(response=RESPONSE, token_started=True),
    lambda: _attempt(response=None, token_started=True, error_code="stream_error"),
])
def test_no_retry_after_any_semantic_token_or_response(episode, first):
    second = _attempt(
        index=2,
        started="2026-07-10T12:00:02Z",
        completed="2026-07-10T12:00:03Z",
    )
    with pytest.raises(ValueError, match="retry|token|response"):
        _result(episode, attempts=[first(), second])


def test_at_most_two_transport_retries(episode):
    with pytest.raises(ValueError, match="three|retry|attempt"):
        attempts = []
        for index in range(1, 5):
            attempts.append(_attempt(
                index=index,
                response=None if index < 4 else RESPONSE,
                token_started=index == 4,
                error_code="transient" if index < 4 else None,
                started=f"2026-07-10T12:00:0{2 * index - 2}Z",
                completed=f"2026-07-10T12:00:0{2 * index - 1}Z",
            ))
        _result(episode, attempts=attempts)


@pytest.mark.parametrize("field", [
    "raw_trace_sha256",
    "raw_final_message_sha256",
    "parsed_response_sha256",
    "reasoning_details_sha256",
])
def test_attempt_hash_tamper_is_rejected(episode, field):
    attempt = _attempt(reasoning_details={"kind": "summary"})
    attempt[field] = "0" * 64
    with pytest.raises(ValueError, match="hash"):
        _result(episode, attempts=[attempt])


def test_caller_cannot_claim_parsed_values_that_disagree_with_raw(episode):
    attempt = _attempt()
    attempt["parsed_response"]["DECISION"] = "GRANT"
    attempt["parsed_response_sha256"] = contracts.canonical_sha256(
        attempt["parsed_response"]
    )
    with pytest.raises(ValueError, match="parsed|raw"):
        _result(episode, attempts=[attempt])


@pytest.mark.parametrize("mutation", [
    lambda attempt: attempt["usage"].update(input_tokens=True),
    lambda attempt: attempt["usage"].update(output_tokens=-1),
    lambda attempt: attempt.update(reasoning_effort="high"),
    lambda attempt: attempt.update(started_at_utc="2026-07-10 12:00:00"),
    lambda attempt: attempt.update(extra="not-exact"),
])
def test_attempt_types_bounds_and_exact_keys_fail_loudly(episode, mutation):
    attempt = _attempt()
    mutation(attempt)
    with pytest.raises(ValueError):
        _result(episode, attempts=[attempt])


@pytest.mark.parametrize("kwargs,violation", [
    ({"returned_model": "wrong-model"}, "provider_identity"),
    ({"returned_provider": "WrongProvider"}, "provider_identity"),
    ({"tool_events": [{"type": "tool.call"}]}, "tool_event"),
    ({"session_chain_ok": False}, "session_chain"),
    ({"isolation_ok": False}, "isolation"),
    ({"future_text_absent": False}, "future_text"),
])
def test_integrity_evidence_invalidates_instead_of_being_scored(
        episode, kwargs, violation):
    request, result = _result(episode, **kwargs)
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["integrity_valid"] is False
    assert result["integrity"]["measurement_ready"] is False
    assert violation in result["integrity"]["violations"]
    assert contracts.validate_stage_result(result, request) == result


@pytest.mark.parametrize("sentinel", [
    "10CB-07-452ec262-8025-449d-bfb0-788e122135bd",
    "CHARITROC-0577",
    "JUDGE-a19ca5c6-ce54-42cb-84be-83025d5f52cf",
])
def test_result_preserves_but_invalidates_forbidden_identifier_echo(
        episode, sentinel):
    raw = json.dumps({
        "reason": "Unexpected echo: " + sentinel,
        "INTENT": "UNCERTAIN",
        "DECISION": "VERIFY",
    }, separators=(",", ":"))
    request, result = _result(episode, attempts=[_attempt(response=raw)])
    assert result["attempts"][0]["raw_final_message"] == raw
    assert result["integrity"]["identifier_echo_absent"] is False
    assert "forbidden_identifier_echo" in result["integrity"]["violations"]
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False
    assert contracts.validate_stage_result(result, request) == result


@pytest.mark.parametrize("sentinel", [
    "10cb-07-452ec262-8025-449d-bfb0-788e122135bd",
    "charitroc-0577",
    "judge-a19ca5c6-ce54-42cb-84be-83025d5f52cf",
])
def test_identifier_echo_detection_is_case_insensitive(episode, sentinel):
    raw = json.dumps({
        "reason": "Unexpected echo: " + sentinel,
        "INTENT": "UNCERTAIN",
        "DECISION": "VERIFY",
    }, separators=(",", ":"))
    _, result = _result(episode, attempts=[_attempt(response=raw)])
    assert result["integrity"]["identifier_echo_absent"] is False
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False


@pytest.mark.parametrize("location", [
    "raw_trace", "reasoning_details", "tool_events",
])
def test_lowercase_identifier_echo_is_scanned_across_all_result_evidence(
        episode, location):
    sentinel = "charitroc-0577"
    attempt_kwargs = {}
    result_kwargs = {}
    if location == "raw_trace":
        attempt_kwargs["raw_trace"] = json.dumps({"echo": sentinel})
    elif location == "reasoning_details":
        attempt_kwargs["reasoning_details"] = {"summary": sentinel}
    else:
        result_kwargs["tool_events"] = [{"description": sentinel}]
    _, result = _result(
        episode,
        attempts=[_attempt(**attempt_kwargs)],
        **result_kwargs,
    )
    assert result["integrity"]["identifier_echo_absent"] is False
    assert result["terminal_status"] == "invalidated"


def test_lowercase_identifier_is_rejected_from_outbound_request(episode):
    request = _build(episode)
    request["current_visible_turn"]["content"] += " charitroc-0577"
    _rehash(request)
    with pytest.raises(ValueError, match="forbidden identifier"):
        contracts.validate_stage_request(request)


def test_parseable_response_with_transport_error_is_never_measurement_ready(
        episode):
    request, result = _result(episode, attempts=[_attempt(
        response=RESPONSE,
        token_started=True,
        error_code="stream_error",
        raw_trace='{"type":"error","code":"stream_error"}',
    )])
    assert result["attempts"][0]["parsed_response"] == json.loads(RESPONSE)
    assert result["integrity"]["transport_successful"] is False
    assert "transport_error" in result["integrity"]["violations"]
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False
    assert contracts.validate_stage_result(result, request) == result


def test_zero_byte_pre_response_transport_attempt_is_complete_failed_evidence(
        episode):
    attempt = contracts.build_stage_attempt(
        attempt_index=1,
        started_at_utc="2026-07-10T12:00:00Z",
        completed_at_utc="2026-07-10T12:00:01Z",
        provider_request_id=None,
        token_emission_started=False,
        exit_status=None,
        http_status=None,
        finish_reason=None,
        usage={key: None for key in contracts.USAGE_KEYS},
        raw_trace="",
        raw_final_message=None,
        reasoning_effort="medium",
        reasoning_details=None,
        error_code="transport_error",
    )
    request, result = _result(
        episode,
        provider="openrouter",
        attempts=[attempt],
        session_id=None,
    )

    assert result["terminal_status"] == "failed"
    assert result["integrity"]["trace_complete"] is True
    assert result["integrity"]["violations"] == ["transport_error"]
    assert result["integrity"]["measurement_ready"] is False
    assert contracts.validate_stage_result(result, request) == result


def test_rehashed_transport_integrity_claim_cannot_override_raw_error(episode):
    request, result = _result(episode, attempts=[_attempt(
        response=RESPONSE,
        token_started=True,
        error_code="stream_error",
        raw_trace='{"type":"error","code":"stream_error"}',
    )])
    result["integrity"]["transport_successful"] = True
    result["integrity"]["violations"] = []
    result["integrity"]["integrity_valid"] = True
    result["integrity"]["measurement_ready"] = True
    result["terminal_status"] = "complete"
    result["result_sha256"] = contracts.canonical_sha256({
        key: value for key, value in result.items()
        if key != "result_sha256"
    })
    with pytest.raises(ValueError, match="integrity|evidence"):
        contracts.validate_stage_result(result, request)


def test_terminal_transport_failure_without_response_is_failed(episode):
    failed = _attempt(
        response=None,
        token_started=False,
        error_code="provider_unavailable",
        raw_trace='{"error":"provider_unavailable"}',
    )
    request, result = _result(episode, attempts=[failed])
    assert result["terminal_status"] == "failed"
    assert result["integrity"]["measurement_ready"] is False
    assert contracts.validate_stage_result(result, request) == result


def test_result_rehashed_extra_field_and_terminal_claim_are_rejected(episode):
    request, result = _result(episode)
    result["extra"] = "poison"
    result["result_sha256"] = contracts.canonical_sha256({
        key: value for key, value in result.items() if key != "result_sha256"
    })
    with pytest.raises(ValueError, match="exact"):
        contracts.validate_stage_result(result, request)

    request, result = _result(episode)
    result["terminal_status"] = "unresolved"
    result["result_sha256"] = contracts.canonical_sha256({
        key: value for key, value in result.items() if key != "result_sha256"
    })
    with pytest.raises(ValueError, match="terminal"):
        contracts.validate_stage_result(result, request)


def test_result_hash_request_hash_and_schema_hash_are_bound(episode):
    request, result = _result(episode)
    for field in ("request_sha256", "response_schema_sha256", "result_sha256"):
        changed = deepcopy(result)
        changed[field] = "0" * 64
        if field != "result_sha256":
            changed["result_sha256"] = contracts.canonical_sha256({
                key: value for key, value in changed.items()
                if key != "result_sha256"
            })
        with pytest.raises(ValueError, match="hash|request|schema"):
            contracts.validate_stage_result(changed, request)


def test_duplicate_result_json_keys_are_rejected(episode):
    request, result = _result(episode)
    encoded = contracts.dumps_stage_result(result, request)
    duplicate = '{"run_mode":"mock",' + encoded[1:]
    with pytest.raises(ValueError, match="unique-key|duplicate"):
        contracts.loads_stage_result(duplicate, request)


def test_result_validator_returns_detached_copy(episode):
    request, result = _result(episode)
    original = deepcopy(result)
    validated = contracts.validate_stage_result(result, request)
    assert validated == original
    assert validated is not result
    assert validated["attempts"] is not result["attempts"]


# Four-stage continuity and integrity-rerun authorization ------------------------

def _four_stage_run(episode, *, provider="codex", responses=None,
                    execution_id=EXECUTION_ID, session_id=None,
                    tool_stage=None, request_identity=None, run_mode=None,
                    returned_provider="OpenAI", returned_model=None):
    responses = responses or {stage: RESPONSE for stage in contracts.STAGES}
    if provider == "codex" and session_id is None:
        session_id = "019f49e3-b7de-7272-9d25-545c82c2674c"
    requests = []
    results = []
    prior = {}
    identity = request_identity or _identity(provider, "gpt-5.5")
    run_mode = run_mode or provider
    for index, stage in enumerate(contracts.STAGES):
        request = contracts.build_stage_request(
            episode,
            execution_id=execution_id,
            stage=stage,
            prior_responses=prior,
            **identity,
        )
        attempt = contracts.build_stage_attempt(
            attempt_index=1,
            started_at_utc=f"2026-07-10T12:00:0{2 * index}Z",
            completed_at_utc=f"2026-07-10T12:00:0{2 * index + 1}Z",
            provider_request_id=f"provider-stage-{index + 1}",
            token_emission_started=True,
            exit_status=0,
            http_status=200,
            finish_reason="stop",
            usage=USAGE,
            raw_trace=json.dumps({"stage": stage, "type": "turn.completed"}),
            raw_final_message=responses[stage],
            reasoning_effort="medium",
            reasoning_details=None,
            error_code=None,
        )
        result = contracts.build_stage_result(
            request,
            run_mode=run_mode,
            returned_provider_model_id=(
                returned_model or request["provider_model_id"]
            ),
            returned_provider_name=returned_provider,
            session_id=session_id,
            transport_request_sha256=chr(ord("b") + index) * 64,
            attempts=[attempt],
            tool_events=(
                [{"type": "tool.call"}] if tool_stage == stage else []
            ),
            session_chain_ok=True,
            isolation_ok=True,
            future_text_absent=True,
        )
        requests.append(request)
        results.append(result)
        prior[stage] = responses[stage]
    return requests, results


def test_complete_four_stage_codex_chain_is_hashed_and_measurement_ready(episode):
    requests, results = _four_stage_run(episode)
    chain = contracts.build_stage_chain(requests, results, episode)
    assert set(chain) == contracts.STAGE_CHAIN_KEYS
    assert chain["stage_count"] == 4
    assert chain["session_id"] == results[0]["session_id"]
    assert chain["request_sha256s"] == [row["request_sha256"] for row in requests]
    assert chain["result_sha256s"] == [row["result_sha256"] for row in results]
    assert chain["measurement_ready"] is True
    assert contracts.validate_stage_chain(
        chain, requests, results, episode
    ) == chain


def test_complete_openrouter_chain_has_no_invented_session(episode):
    requests, results = _four_stage_run(
        episode, provider="openrouter", session_id=None
    )
    chain = contracts.build_stage_chain(requests, results, episode)
    assert chain["session_id"] is None
    assert chain["measurement_ready"] is True


def test_complete_cheap_openrouter_probe_chain_is_never_measurement_ready(
        episode):
    requests, results = _four_stage_run(
        episode,
        provider="openrouter",
        session_id=None,
        request_identity=_cheap_identity(),
        run_mode="openrouter_probe",
        returned_provider="Azure",
        returned_model="openai/gpt-5-nano-2025-08-07",
    )
    chain = contracts.build_stage_chain(requests, results, episode)

    assert chain["provenance"] == (
        "live OpenRouter access probe, NOT a measurement"
    )
    assert chain["run_mode"] == "openrouter_probe"
    assert chain["measurement_ready"] is False
    assert all(
        result["integrity"]["measurement_ready"] is False
        for result in results
    )
    assert contracts.validate_stage_chain(
        chain, requests, results, episode
    ) == chain


def test_unresolved_final_stage_is_structurally_valid_but_not_measurement_ready(
        episode):
    responses = {stage: RESPONSE for stage in contracts.STAGES}
    responses["stage_4"] = "not canonical JSON"
    requests, results = _four_stage_run(episode, responses=responses)
    chain = contracts.build_stage_chain(requests, results, episode)
    assert results[-1]["terminal_status"] == "unresolved"
    assert chain["measurement_ready"] is False


def test_chain_rejects_broken_codex_session_even_when_each_result_is_valid(
        episode):
    requests, results = _four_stage_run(episode)
    request = requests[1]
    old = results[1]
    results[1] = contracts.build_stage_result(
        request,
        run_mode="codex",
        returned_provider_model_id=request["provider_model_id"],
        returned_provider_name="OpenAI",
        session_id="different-thread-id",
        transport_request_sha256=old["transport_request_sha256"],
        attempts=old["attempts"],
        tool_events=[],
        session_chain_ok=True,
        isolation_ok=True,
        future_text_absent=True,
    )
    with pytest.raises(ValueError, match="session|thread"):
        contracts.build_stage_chain(requests, results, episode)


def test_chain_rejects_prior_prompt_or_response_disagreement(episode):
    requests, results = _four_stage_run(episode)
    requests[2]["prior_visible_turns"][0]["response"] = "different response"
    _rehash(requests[2])
    with pytest.raises(ValueError, match="history|response"):
        contracts.build_stage_chain(requests, results, episode)


def test_chain_recomputes_future_stage_exposure_from_raw_text_and_hash(episode):
    for exposure in ("text", "hash"):
        requests, results = _four_stage_run(episode)
        future = episode["multiturn_script"]["stage_3"]
        leaked = future if exposure == "text" else contracts.sha256_utf8(future)
        stage_one = results[0]
        poisoned_attempt = contracts.build_stage_attempt(
            attempt_index=1,
            started_at_utc="2026-07-10T12:00:00Z",
            completed_at_utc="2026-07-10T12:00:01Z",
            provider_request_id="provider-stage-1",
            token_emission_started=True,
            exit_status=0,
            http_status=200,
            finish_reason="stop",
            usage=USAGE,
            raw_trace='{"type":"turn.completed"}',
            raw_final_message="Leaked future: " + leaked,
            reasoning_effort="medium",
            reasoning_details=None,
            error_code=None,
        )
        results[0] = contracts.build_stage_result(
            requests[0],
            run_mode="codex",
            returned_provider_model_id=requests[0]["provider_model_id"],
            returned_provider_name="OpenAI",
            session_id=stage_one["session_id"],
            transport_request_sha256=stage_one["transport_request_sha256"],
            attempts=[poisoned_attempt],
            tool_events=[],
            session_chain_ok=True,
            isolation_ok=True,
            future_text_absent=True,
        )
        requests[1]["prior_visible_turns"][0]["response"] = (
            poisoned_attempt["raw_final_message"]
        )
        _rehash(requests[1])
        with pytest.raises(ValueError, match="future-stage"):
            contracts.build_stage_chain(requests, results, episode)


def test_full_chain_rejects_integrity_invalidated_stage(episode):
    requests, results = _four_stage_run(episode, tool_stage="stage_2")
    assert results[1]["terminal_status"] == "invalidated"
    with pytest.raises(ValueError, match="integrity|invalidated"):
        contracts.build_stage_chain(requests, results, episode)


def test_chain_rejects_execution_identity_or_stage_order_drift(episode):
    requests, results = _four_stage_run(episode)
    requests[2]["execution_id"] = "54c94821-a36c-4ea7-ae2c-568a1a4410ef"
    _rehash(requests[2])
    with pytest.raises(ValueError, match="execution|request"):
        contracts.build_stage_chain(requests, results, episode)


def test_integrity_rerun_requires_fresh_uuid_and_actual_invalidation(episode):
    previous_requests, previous_results = _four_stage_run(
        episode, tool_stage="stage_1"
    )
    previous_requests = previous_requests[:1]
    previous_results = previous_results[:1]
    new_id = "54c94821-a36c-4ea7-ae2c-568a1a4410ef"
    new_request = _build(
        episode,
        stage="stage_1",
        prior_responses={},
        execution_id=new_id,
    )
    authorized = contracts.validate_integrity_rerun(
        previous_requests,
        previous_results,
        [new_request],
    )
    assert authorized == {
        "authorized": True,
        "previous_execution_id": EXECUTION_ID,
        "new_execution_id": new_id,
    }

    same_id_request = _build(
        episode,
        stage="stage_1",
        prior_responses={},
        execution_id=EXECUTION_ID,
    )
    with pytest.raises(ValueError, match="fresh|execution"):
        contracts.validate_integrity_rerun(
            previous_requests, previous_results, [same_id_request]
        )


def test_integrity_rerun_cannot_switch_to_a_different_episode(episode):
    previous_requests, previous_results = _four_stage_run(
        episode, tool_stage="stage_1"
    )
    other_episode = yaml.safe_load((BANK / "seeds_public.yaml").read_text())[1]
    assert (
        other_episode["multiturn_script"]["stage_1"]
        != episode["multiturn_script"]["stage_1"]
    )
    switched_request = _build(
        other_episode,
        stage="stage_1",
        prior_responses={},
        execution_id="54c94821-a36c-4ea7-ae2c-568a1a4410ef",
    )
    with pytest.raises(ValueError, match="episode|prompt|visible"):
        contracts.validate_integrity_rerun(
            previous_requests[:1], previous_results[:1], [switched_request]
        )


def test_failed_transport_or_noncontiguous_prefix_cannot_authorize_rerun(
        episode):
    failed_request, failed_result = _result(episode, attempts=[_attempt(
        response=None,
        token_started=False,
        error_code="provider_unavailable",
        raw_trace='{"error":"provider_unavailable"}',
    )])
    restart = _build(
        episode,
        stage="stage_1",
        prior_responses={},
        execution_id="54c94821-a36c-4ea7-ae2c-568a1a4410ef",
    )
    with pytest.raises(ValueError, match="integrity|unresolved|failure"):
        contracts.validate_integrity_rerun(
            [failed_request], [failed_result], [restart]
        )

    requests, results = _four_stage_run(episode, tool_stage="stage_2")
    with pytest.raises(ValueError, match="contiguous|prefix"):
        contracts.validate_integrity_rerun(
            requests[1:2], results[1:2], [restart]
        )


def test_post_token_transport_error_cannot_authorize_integrity_rerun(episode):
    failed_request, failed_result = _result(episode, attempts=[_attempt(
        response=RESPONSE,
        token_started=True,
        error_code="stream_error",
        raw_trace='{"type":"error","code":"stream_error"}',
    )])
    assert failed_result["terminal_status"] == "invalidated"
    assert "transport_error" in failed_result["integrity"]["violations"]
    restart = _build(
        episode,
        stage="stage_1",
        prior_responses={},
        execution_id="54c94821-a36c-4ea7-ae2c-568a1a4410ef",
    )
    with pytest.raises(ValueError, match="transport|integrity|rerun"):
        contracts.validate_integrity_rerun(
            [failed_request], [failed_result], [restart]
        )


def test_parse_failure_never_authorizes_whole_episode_rerun(episode):
    responses = {stage: RESPONSE for stage in contracts.STAGES}
    responses["stage_1"] = "not canonical JSON"
    previous_requests, previous_results = _four_stage_run(
        episode, responses=responses
    )
    previous_requests = previous_requests[:1]
    previous_results = previous_results[:1]
    new_request = _build(
        episode,
        stage="stage_1",
        prior_responses={},
        execution_id="54c94821-a36c-4ea7-ae2c-568a1a4410ef",
    )
    with pytest.raises(ValueError, match="integrity|parse|unresolved"):
        contracts.validate_integrity_rerun(
            previous_requests, previous_results, [new_request]
        )


def test_raw_transport_trace_cannot_serialize_credential_material(episode):
    sentinel = "sk-live-NeverEchoThisSecretValue"
    with pytest.raises(ValueError) as raised:
        _attempt(raw_trace="Authorization: Bearer " + sentinel)
    assert sentinel not in str(raised.value)
