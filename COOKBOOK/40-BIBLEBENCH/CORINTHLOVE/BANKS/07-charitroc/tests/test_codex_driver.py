"""Offline, fail-closed tests for the Codex CLI pilot driver."""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess

import pytest
import yaml

from lib.payloads import model_turns as model_turns_for_test
from pilot import codex_driver, contracts


BANK = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "codex_events"
THREAD = "019e1111-1111-7111-8111-111111111111"
EXECUTION_IDS = iter((
    "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
    "a10e9f10-50a2-4baa-a53d-44d47d3e5d8c",
    "bf4f267d-078e-43cf-8122-9cf012820819",
))


def fixture(name):
    return (FIXTURES / name).read_bytes()


def _parse_test_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _valid_response_text():
    for line in fixture("valid.jsonl").splitlines():
        row = json.loads(line)
        if (
            row.get("type") == "item.completed"
            and row.get("item", {}).get("type") == "agent_message"
        ):
            return row["item"]["text"]
    raise AssertionError("valid fixture lacks final response")


@pytest.fixture
def episode():
    rows = yaml.safe_load((BANK / "seeds_public.yaml").read_text())
    assert rows
    return rows[0]


class FakeClock:
    def __init__(self):
        self.value = datetime(2026, 7, 10, tzinfo=timezone.utc)

    def __call__(self):
        value = self.value
        self.value += timedelta(seconds=1)
        return value


class FakeExecutor:
    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.calls = []

    def __call__(self, argv, *, stdin, cwd):
        self.calls.append({
            "argv": tuple(argv),
            "stdin": stdin,
            "cwd": Path(cwd),
            "entries": tuple(Path(cwd).iterdir()),
        })
        if not self.outputs:
            raise AssertionError("unexpected Codex invocation")
        value = self.outputs.pop(0)
        if isinstance(value, BaseException):
            raise value
        if isinstance(value, codex_driver.ExecutionOutcome):
            return value
        chunks = value if isinstance(value, (list, tuple)) else (value,)
        return codex_driver.ExecutionOutcome(
            stdout_chunks=tuple(chunks), stderr=b"", exit_status=0,
        )


class FakeSleeper:
    def __init__(self):
        self.delays = []

    def __call__(self, delay):
        self.delays.append(delay)


class FakeAttestor:
    def __init__(self, mutations=None):
        self.mutations = list(mutations or [])
        self.calls = []

    def __call__(self, session_id, *, stage, requested_model,
                 isolation_dir, started_at_utc, observed_at_utc,
                 future_turns, required_disabled_features,
                 current_prompt, expected_response):
        self.calls.append((session_id, stage, requested_model, isolation_dir))
        row = {
            "source": "mock",
            "thread_id": session_id,
            "returned_provider_model_id": requested_model,
            "returned_provider_name": "OpenAI",
            "cli_version": "0.134.0",
            "cwd": str(Path(isolation_dir).resolve()),
            "sandbox": "read-only",
            "reasoning_effort": "medium",
            "turn_count": contracts.STAGES.index(stage) + 1,
            "disabled_features": list(required_disabled_features),
            "rollout_path": None,
            "rollout_prefix_size": 0,
            "rollout_prefix_sha256": hashlib.sha256(b"").hexdigest(),
            "rollout_mtime_ns": 0,
            "latest_context_timestamp_utc": observed_at_utc,
            "scanned_payload_sha256": contracts.canonical_sha256([]),
            "future_text_absent": True,
            "identifier_absent": True,
            "stage": stage,
            "current_prompt_sha256": contracts.sha256_utf8(current_prompt),
            "current_prompt_linked": True,
            "final_response_sha256": (
                contracts.sha256_utf8(expected_response)
                if expected_response is not None else None
            ),
            "final_response_linked": expected_response is not None,
            "stage_evidence_sha256": contracts.canonical_sha256([]),
            "rollout_tools_absent": True,
            "rollout_tool_evidence_sha256": contracts.canonical_sha256([]),
        }
        if self.mutations:
            row.update(self.mutations.pop(0))
        return row


def make_driver(tmp_path, outputs, *, attestor=None, ids=None):
    executor = FakeExecutor(outputs)
    counter = iter(ids or (
        "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        "a10e9f10-50a2-4baa-a53d-44d47d3e5d8c",
    ))
    directories = iter(
        tmp_path / f"cx-{index:032x}" for index in range(1, 5)
    )
    sleeper = FakeSleeper()
    driver = codex_driver.CodexDriver(
        run_mode="mock",
        executor=executor,
        attestor=attestor or FakeAttestor(),
        clock=FakeClock(),
        uuid_factory=lambda: next(counter),
        tempdir_factory=lambda: next(directories),
        sleeper=sleeper,
        codex_binary="codex",
    )
    driver.test_sleeper = sleeper
    return driver, executor


def stage_request(episode, stage="stage_1", prior=None):
    return contracts.build_stage_request(
        episode,
        execution_id="9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        provider="codex",
        logical_model_id="gpt-5.5",
        provider_model_id="gpt-5.5",
        configuration_id="codex-cli-gpt-5.5-medium-isolated",
        stage=stage,
        prior_responses=prior or {},
    )


def test_mock_is_default_but_requires_explicit_executor_and_attestor():
    with pytest.raises(codex_driver.CodexDriverError, match="mock"):
        codex_driver.CodexDriver()


@pytest.mark.parametrize("injected", [
    {"executor": object()},
    {"attestor": object()},
    {"clock": object()},
    {"uuid_factory": object()},
    {"tempdir_factory": object()},
    {"sleeper": object()},
    {"response_schema_path": BANK / "pilot" / "response_schema.json"},
    {"codex_binary": "codex"},
])
def test_live_mode_rejects_every_injected_dependency(injected):
    with pytest.raises(codex_driver.CodexDriverError, match="production"):
        codex_driver.CodexDriver(run_mode="codex", **injected)


def test_fake_dependencies_can_never_forge_live_provenance(tmp_path):
    with pytest.raises(codex_driver.CodexDriverError, match="production"):
        codex_driver.CodexDriver(
            run_mode="codex",
            executor=FakeExecutor([fixture("valid.jsonl")]),
            attestor=FakeAttestor(),
        )


def test_live_dependency_mutation_is_rejected_before_execution(episode):
    driver = codex_driver.CodexDriver(run_mode="codex")
    fake = FakeExecutor([fixture("valid.jsonl")])
    driver.executor = fake
    with pytest.raises(codex_driver.CodexDriverError, match="production"):
        driver.run_episode(episode, logical_model_id="gpt-5.5")
    assert fake.calls == []


def test_evidence_verifier_rejects_offline_relabel_as_live(
        episode, tmp_path):
    driver, _ = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    run = driver.run_episode(episode, logical_model_id="gpt-5.5")
    poisoned = deepcopy(run.final)
    request = poisoned.requests[0]
    old = poisoned.results[0]
    poisoned.results[0] = contracts.build_stage_result(
        request, run_mode="codex",
        returned_provider_model_id=old["returned_provider_model_id"],
        returned_provider_name=old["returned_provider_name"],
        session_id=old["session_id"],
        transport_request_sha256=old["transport_request_sha256"],
        attempts=old["attempts"], tool_events=old["tool_events"],
        session_chain_ok=old["integrity"]["session_chain_ok"],
        isolation_ok=old["integrity"]["isolation_ok"],
        future_text_absent=old["integrity"]["future_text_absent"],
    )
    object.__setattr__(poisoned, "chain", None)
    with pytest.raises(codex_driver.CodexDriverError, match="run_mode"):
        driver.validate_episode_attempt(poisoned, episode)


def test_evidence_verifier_rechecks_production_dependency_identity(
        episode, tmp_path):
    mock_driver, _ = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    run = mock_driver.run_episode(episode, logical_model_id="gpt-5.5")
    live_driver = codex_driver.CodexDriver(run_mode="codex")
    live_driver.executor = FakeExecutor([])
    with pytest.raises(codex_driver.CodexDriverError, match="production"):
        live_driver.validate_episode_attempt(run.final, episode)


def test_production_runtime_identity_is_absolute_and_frozen(monkeypatch, tmp_path):
    driver = codex_driver.CodexDriver(run_mode="codex")
    assert Path(driver.codex_binary).is_absolute()
    assert driver.codex_cli_version == "0.134.0"
    assert len(driver.codex_binary_sha256) == 64
    assert driver.codex_home == driver.attestor.codex_home

    monkeypatch.setenv("PATH", str(tmp_path / "no-codex"))
    with pytest.raises(codex_driver.CodexDriverError, match="production"):
        driver._assert_production_dependencies()


@pytest.mark.parametrize("mutation", ["binary_hash", "codex_home", "features"])
def test_production_runtime_mutations_are_rejected(
        monkeypatch, tmp_path, mutation):
    driver = codex_driver.CodexDriver(run_mode="codex")
    if mutation == "binary_hash":
        driver.codex_binary_sha256 = "0" * 64
    elif mutation == "codex_home":
        driver.attestor.codex_home = (tmp_path / "other-home").resolve()
    else:
        monkeypatch.setattr(
            codex_driver, "DISABLED_TOOL_FEATURES", ("shell_tool",)
        )
    with pytest.raises(codex_driver.CodexDriverError, match="production"):
        driver._assert_production_dependencies()


def test_persisted_context_audit_restore_refreshes_fingerprint_fail_closed(
        tmp_path):
    driver = codex_driver.CodexDriver(run_mode="codex")
    isolation = (tmp_path / "cx-replayed-audit").resolve()
    audit = driver._finalize_context_audit({
        "audit_version": codex_driver.CONTEXT_AUDIT_VERSION,
        "source": "codex-debug-prompt-input",
        "provider_model_id": "gpt-5.5",
        "isolation_dir": str(isolation),
        "context_profile_sha256": codex_driver.CONTEXT_PROFILE_SHA256,
        "sentinel_sha256": contracts.sha256_utf8(
            codex_driver.CONTEXT_AUDIT_SENTINEL
        ),
        "argv_sha256": contracts.canonical_sha256(list(
            driver._context_preflight_argv("gpt-5.5")
        )),
        "raw_stdout_sha256": hashlib.sha256(b"safe replay").hexdigest(),
        "rendered_input_sha256": contracts.canonical_sha256(
            codex_driver.EXPECTED_CONTEXT_AUDIT_INPUT
        ),
        "passed": True,
    })

    restored = driver.restore_persisted_context_audit(isolation, audit)

    assert restored == audit
    assert driver._context_audit_for(isolation) == audit
    driver._assert_production_dependencies()
    assert driver.restore_persisted_context_audit(isolation, audit) == audit

    poisoned = deepcopy(audit)
    poisoned["raw_stdout_sha256"] = hashlib.sha256(b"other").hexdigest()
    poisoned["audit_sha256"] = contracts.canonical_sha256({
        key: value for key, value in poisoned.items()
        if key != "audit_sha256"
    })
    with pytest.raises(codex_driver.CodexDriverError, match="context audit"):
        driver.restore_persisted_context_audit(isolation, poisoned)
    driver._assert_production_dependencies()


def test_valid_four_stage_run_builds_contract_valid_chain(episode, tmp_path):
    driver, executor = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)

    run = driver.run_episode(episode, logical_model_id="gpt-5.5")

    assert len(run.attempts) == 1
    assert len(run.requests) == len(run.results) == 4
    assert run.chain["measurement_ready"] is False
    assert len(run.transport_descriptors) == len(run.attestations) == 4
    assert contracts.validate_stage_chain(
        run.chain, run.requests, run.results, episode
    ) == run.chain
    for request, result in zip(run.requests, run.results):
        assert contracts.validate_stage_request(request) == request
        assert contracts.validate_stage_result(result, request) == result
        assert result["provenance"] == "harness validation, NOT a measurement"
        assert result["run_mode"] == "mock"
        assert result["integrity"]["measurement_ready"] is False
        assert result["attempts"][-1]["reasoning_effort"] == "medium"
        assert result["attempts"][-1]["exit_status"] == 0
        assert result["attempts"][-1]["http_status"] is None
        assert result["integrity"]["transport_successful"] is True
    assert all(
        descriptor["run_mode"] == "mock"
        and set(descriptor["runtime_identity"])
        == codex_driver.RUNTIME_IDENTITY_KEYS
        for descriptor in run.transport_descriptors
    )
    assert not executor.outputs


def test_stage_hooks_are_deepcopied_ordered_and_follow_stage_validation(
        episode, tmp_path):
    driver, executor = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    timeline = []
    before_events = []
    sink_events = []
    original_validate = driver.validate_stage_evidence

    def validate(*args, **kwargs):
        outcome = original_validate(*args, **kwargs)
        timeline.append(("validated", args[0]["stage"]))
        return outcome

    driver.validate_stage_evidence = validate

    def before_stage(event):
        stage_number = contracts.STAGES.index(event["stage"])
        assert len(executor.calls) == stage_number
        assert set(event) == {
            "provider", "integrity_session", "execution_id", "stage",
            "request", "transport_descriptor", "attestation",
        }
        assert event["provider"] == "codex"
        assert event["integrity_session"] == 1
        assert event["attestation"] is None
        assert event["transport_descriptor"]["context_audit"]
        assert event["execution_id"] == event["request"]["execution_id"]
        timeline.append(("before", event["stage"]))
        before_events.append(deepcopy(event))
        event["request"]["stage"] = "poisoned"
        event["transport_descriptor"]["stage"] = "poisoned"
        return {"ignored": True}

    def stage_sink(event):
        stage_number = contracts.STAGES.index(event["stage"]) + 1
        assert len(executor.calls) == stage_number
        assert set(event) == {
            "provider", "integrity_session", "execution_id", "stage",
            "request", "transport_descriptor", "attestation", "result",
        }
        assert timeline[-1] == ("validated", event["stage"])
        assert event["attestation"]["attestation_version"] == (
            codex_driver.ATTESTATION_VERSION
        )
        assert event["result"] == contracts.validate_stage_result(
            event["result"], event["request"]
        )
        timeline.append(("sink", event["stage"]))
        sink_events.append(deepcopy(event))
        event["result"]["terminal_status"] = "poisoned"
        event["attestation"]["source"] = "poisoned"
        return "ignored"

    run = driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        before_stage=before_stage,
        stage_sink=stage_sink,
    )

    assert [row["stage"] for row in before_events] == list(contracts.STAGES)
    assert [row["stage"] for row in sink_events] == list(contracts.STAGES)
    assert all(row["stage"] in contracts.STAGES for row in run.requests)
    assert all(row["terminal_status"] == "complete" for row in run.results)
    for stage in contracts.STAGES:
        assert timeline.index(("before", stage)) < timeline.index(
            ("validated", stage)
        ) < timeline.index(("sink", stage))


@pytest.mark.parametrize("crash_hook", ["before_stage_2", "sink_stage_1"])
def test_stage_hook_exception_prevents_every_subsequent_codex_call(
        episode, tmp_path, crash_hook):
    driver, executor = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)

    def before_stage(event):
        if crash_hook == "before_stage_2" and event["stage"] == "stage_2":
            raise RuntimeError("before-stage crash")

    def stage_sink(event):
        if crash_hook == "sink_stage_1" and event["stage"] == "stage_1":
            raise RuntimeError("stage-sink crash")

    with pytest.raises(RuntimeError, match="crash"):
        driver.run_episode(
            episode,
            logical_model_id="gpt-5.5",
            before_stage=before_stage,
            stage_sink=stage_sink,
        )
    assert len(executor.calls) == 1


def test_stage_hooks_number_codex_integrity_rerun_sessions_exactly(
        episode, tmp_path):
    driver, executor = make_driver(
        tmp_path,
        [fixture("tool.jsonl")] + [fixture("valid.jsonl")] * 4,
    )
    events = []

    def capture(kind):
        def callback(event):
            events.append((
                kind, event["integrity_session"], event["stage"],
                event["execution_id"],
            ))
        return callback

    run = driver.run_episode(
        episode,
        logical_model_id="gpt-5.5",
        allow_integrity_rerun=True,
        before_stage=capture("before"),
        stage_sink=capture("sink"),
    )

    assert len(executor.calls) == 5
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
        run.attempts[0].execution_id
    }
    assert {run_id for _kind, session, _stage, run_id in events if session == 2} == {
        run.attempts[1].execution_id
    }


@pytest.mark.parametrize("logical", ["gpt-5.5", "gpt-5.4", "gpt-5.4-mini"])
def test_exact_panel_identity_and_initial_resume_commands(
        episode, tmp_path, logical):
    driver, executor = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)

    run = driver.run_episode(episode, logical_model_id=logical)
    isolation = str(run.isolation_dir.resolve())
    schema = str((BANK / "pilot" / "response_schema.json").resolve())
    disables = tuple(
        part
        for feature in codex_driver.DISABLED_TOOL_FEATURES
        for part in ("--disable", feature)
    )
    context_configs = tuple(
        part
        for override in codex_driver.CONTEXT_CONFIG_OVERRIDES
        for part in ("-c", override)
    )
    assert executor.calls[0]["argv"] == (
        "codex", "exec", "--strict-config", "--ignore-user-config",
        "--ignore-rules",
        *disables, "--skip-git-repo-check", "--sandbox", "read-only", "--json",
        "--model", logical, "-c", 'model_reasoning_effort="medium"',
        *context_configs,
        "--cd", isolation, "--output-schema", schema, "-",
    )
    expected_resume = (
        "codex", "exec", "resume", "--strict-config",
        "--ignore-user-config",
        "--ignore-rules", *disables, "--skip-git-repo-check", "--json",
        "--model", logical, "-c", 'model_reasoning_effort="medium"',
        *context_configs,
        "--output-schema", schema, THREAD, "-",
    )
    assert all(call["argv"] == expected_resume for call in executor.calls[1:])
    assert all("--last" not in call["argv"] for call in executor.calls)
    assert all(call["cwd"].resolve() == run.isolation_dir.resolve()
               for call in executor.calls)


def test_every_codex_command_freezes_the_strict_context_profile(
        episode, tmp_path):
    driver, executor = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    driver.run_episode(episode, logical_model_id="gpt-5.5")

    required_configs = {
        "skills.include_instructions=false",
        "skills.bundled.enabled=false",
        "skills.config=[]",
        "include_permissions_instructions=false",
        "include_apps_instructions=false",
        "include_collaboration_mode_instructions=false",
        "include_environment_context=false",
    }
    for call in executor.calls:
        argv = call["argv"]
        assert "--strict-config" in argv
        assert required_configs <= {
            argv[index + 1]
            for index, value in enumerate(argv[:-1]) if value == "-c"
        }
        for feature in (
                "shell_snapshot", "memories", "enable_request_compression"):
            assert ("--disable", feature) in tuple(zip(argv, argv[1:]))


def _fake_production_subprocess(monkeypatch, *, extra_item=False):
    calls = []

    def fake_run(argv, **kwargs):
        argv = tuple(str(value) for value in argv)
        calls.append({"argv": argv, "kwargs": kwargs})
        if argv[-1:] == ("--version",):
            return subprocess.CompletedProcess(
                argv, 0, stdout=b"codex-cli 0.134.0\n", stderr=b""
            )
        if argv[1:3] == ("debug", "prompt-input"):
            sentinel = argv[-1]
            rendered = [{
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": sentinel}],
            }]
            if extra_item:
                rendered.insert(0, {
                    "type": "message", "role": "developer",
                    "content": [{"type": "input_text", "text": "leak"}],
                })
            return subprocess.CompletedProcess(
                argv, 0,
                stdout=json.dumps(rendered).encode("utf-8"), stderr=b"",
            )
        raise AssertionError("unexpected subprocess invocation")

    monkeypatch.setattr(codex_driver.subprocess, "run", fake_run)
    return calls


def test_production_preflight_attests_exact_user_only_context_before_model_call(
        monkeypatch, tmp_path):
    calls = _fake_production_subprocess(monkeypatch)
    isolation = tmp_path / "cx-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    monkeypatch.setattr(
        codex_driver.tempfile, "mkdtemp", lambda prefix: str(isolation)
    )
    driver = codex_driver.CodexDriver(run_mode="codex")

    created = driver.create_isolation_dir(provider_model_id="gpt-5.5")

    assert created == isolation.resolve()
    debug_calls = [
        call for call in calls
        if call["argv"][1:3] == ("debug", "prompt-input")
    ]
    assert len(debug_calls) == 1
    assert debug_calls[0]["kwargs"]["cwd"] == str(isolation.resolve())
    audit = driver.context_audits[created]
    assert audit["source"] == "codex-debug-prompt-input"
    assert audit["passed"] is True
    assert len(audit["audit_sha256"]) == 64
    assert tuple(created.iterdir()) == ()


def test_production_preflight_rejects_any_extra_model_visible_item(
        monkeypatch, tmp_path):
    _fake_production_subprocess(monkeypatch, extra_item=True)
    isolation = tmp_path / "cx-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    monkeypatch.setattr(
        codex_driver.tempfile, "mkdtemp", lambda prefix: str(isolation)
    )
    driver = codex_driver.CodexDriver(run_mode="codex")

    with pytest.raises(codex_driver.CodexDriverError, match="context preflight"):
        driver.create_isolation_dir(provider_model_id="gpt-5.5")


@pytest.mark.parametrize("mutation", [
    "expected_input",
    "sentinel",
    "context_profile",
    "audit_version",
    "record_keys",
])
def test_production_runtime_fingerprint_binds_live_context_contract_sources(
        monkeypatch, mutation):
    _fake_production_subprocess(monkeypatch)
    driver = codex_driver.CodexDriver(run_mode="codex")
    if mutation == "expected_input":
        poisoned = deepcopy(codex_driver.EXPECTED_CONTEXT_AUDIT_INPUT)
        poisoned.append({
            "type": "message", "role": "developer",
            "content": [{"type": "input_text", "text": "forged"}],
        })
        monkeypatch.setattr(
            codex_driver, "EXPECTED_CONTEXT_AUDIT_INPUT", poisoned
        )
    elif mutation == "sentinel":
        monkeypatch.setattr(
            codex_driver, "CONTEXT_AUDIT_SENTINEL", "mutated-sentinel"
        )
    elif mutation == "context_profile":
        poisoned = deepcopy(codex_driver.CONTEXT_PROFILE)
        poisoned["strict_config"] = False
        monkeypatch.setattr(codex_driver, "CONTEXT_PROFILE", poisoned)
    elif mutation == "audit_version":
        monkeypatch.setattr(
            codex_driver, "CONTEXT_AUDIT_VERSION", "mutated-version"
        )
    else:
        poisoned = set(codex_driver.CONTEXT_AUDIT_RECORD_KEYS)
        poisoned.remove("raw_stdout_sha256")
        monkeypatch.setattr(
            codex_driver, "CONTEXT_AUDIT_RECORD_KEYS", poisoned
        )

    with pytest.raises(codex_driver.CodexDriverError, match="production"):
        driver._assert_production_dependencies()


def test_mock_context_audit_is_explicit_and_cannot_claim_live_attestation(
        episode, tmp_path):
    driver, _ = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    run = driver.run_episode(episode, logical_model_id="gpt-5.5")

    audit = run.transport_descriptors[0]["context_audit"]
    assert audit["source"] == "mock"
    assert audit["passed"] is False
    assert run.attestations[0]["context_audit_sha256"] == audit[
        "audit_sha256"
    ]
    assert run.attestations[0]["context_profile_sha256"] == (
        run.transport_descriptors[0]["context_profile_sha256"]
    )
    assert run.results[0]["integrity"]["measurement_ready"] is False


def test_each_invocation_receives_only_current_prompt_in_empty_isolation(
        episode, tmp_path):
    driver, executor = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    run = driver.run_episode(episode, logical_model_id="gpt-5.5")

    for index, call in enumerate(executor.calls, 1):
        assert call["stdin"] == episode["multiturn_script"][f"stage_{index}"]
        assert call["entries"] == ()
    assert "CHARITROC-" not in run.isolation_dir.name
    assert episode["canary"] not in run.isolation_dir.name


@pytest.mark.parametrize("name", ["malformed.jsonl", "duplicate-key.jsonl"])
def test_malformed_or_duplicate_jsonl_fails_closed_without_retry(
        episode, tmp_path, name):
    driver, executor = make_driver(tmp_path, [fixture(name)])
    request = stage_request(episode)
    isolation = driver.create_isolation_dir()

    result = driver.run_stage(
        request, episode=episode, isolation_dir=isolation, session_id=None
    )

    assert len(executor.calls) == 1
    assert result["terminal_status"] == "invalidated"
    assert result["attempts"][0]["raw_trace"] == fixture(name).decode("utf-8")
    assert result["attempts"][0]["parsed_response"] is None
    assert result["integrity"]["measurement_ready"] is False


@pytest.mark.parametrize("mutation", [
    {"returned_provider_model_id": "gpt-5.4"},
    {"returned_provider_model_id": "unverified"},
    {"returned_provider_name": "unverified"},
])
def test_wrong_or_missing_returned_identity_invalidates(
        episode, tmp_path, mutation):
    attestor = FakeAttestor([mutation])
    driver, _ = make_driver(
        tmp_path, [fixture("valid.jsonl")], attestor=attestor
    )
    request = stage_request(episode)
    result = driver.run_stage(
        request, episode=episode, isolation_dir=driver.create_isolation_dir(),
        session_id=None,
    )
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["provider_identity_ok"] is False


def test_broken_resume_thread_invalidates_and_stops_episode(episode, tmp_path):
    broken = fixture("valid.jsonl").replace(
        THREAD.encode(), b"019e2222-2222-7222-8222-222222222222"
    )
    driver, executor = make_driver(
        tmp_path, [fixture("valid.jsonl"), broken]
    )
    run = driver.run_episode(episode, logical_model_id="gpt-5.5")
    assert len(run.requests) == 2
    assert run.results[-1]["terminal_status"] == "invalidated"
    assert run.chain is None
    assert len(executor.calls) == 2


def test_non_uuid_or_uppercase_thread_id_fails_closed(episode, tmp_path):
    for bad in (b"thread-not-a-uuid", THREAD.upper().encode("ascii")):
        raw = fixture("valid.jsonl").replace(THREAD.encode("ascii"), bad)
        driver, executor = make_driver(tmp_path, [raw])
        result = driver.run_stage(
            stage_request(episode), episode=episode,
            isolation_dir=driver.create_isolation_dir(), session_id=None,
        )
        assert len(executor.calls) == 1
        assert result["terminal_status"] == "invalidated"
        assert result["integrity"]["session_chain_ok"] is False


def test_reused_item_id_fails_closed(episode, tmp_path):
    raw = fixture("valid.jsonl").replace(
        b'"id":"item_1"', b'"id":"item_0"'
    )
    driver, _ = make_driver(tmp_path, [raw])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["session_chain_ok"] is False


def test_turn_completed_rejects_dangling_started_item(episode, tmp_path):
    dangling = (
        b'{"type":"item.started","item":{"id":"dangling",'
        b'"type":"reasoning","text":"unfinished"}}\n'
    )
    raw = fixture("valid.jsonl").replace(
        b'{"type":"turn.started"}\n',
        b'{"type":"turn.started"}\n' + dangling,
    )
    driver, _ = make_driver(tmp_path, [raw])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["session_chain_ok"] is False


def test_final_agent_message_must_be_final_completed_response_item(
        episode, tmp_path):
    lines = fixture("valid.jsonl").splitlines(keepends=True)
    # Swap the completed reasoning and final response items.
    lines[2], lines[3] = lines[3], lines[2]
    driver, _ = make_driver(tmp_path, [b"".join(lines)])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["session_chain_ok"] is False


def test_zero_output_or_inconsistent_usage_fails_closed(episode, tmp_path):
    variants = (
        fixture("valid.jsonl").replace(
            b'"output_tokens":35,"reasoning_output_tokens":12',
            b'"output_tokens":0,"reasoning_output_tokens":0',
        ),
        fixture("valid.jsonl").replace(
            b'"input_tokens":120,"cached_input_tokens":20',
            b'"input_tokens":10,"cached_input_tokens":20',
        ),
        fixture("valid.jsonl").replace(
            b'"output_tokens":35,"reasoning_output_tokens":12',
            b'"output_tokens":4,"reasoning_output_tokens":12',
        ),
    )
    for raw in variants:
        driver, _ = make_driver(tmp_path, [raw])
        result = driver.run_stage(
            stage_request(episode), episode=episode,
            isolation_dir=driver.create_isolation_dir(), session_id=None,
        )
        assert result["terminal_status"] == "invalidated"
        assert result["integrity"]["session_chain_ok"] is False
        assert result["integrity"]["transport_successful"] is True


def test_tool_event_is_preserved_and_invalidates(episode, tmp_path):
    driver, _ = make_driver(tmp_path, [fixture("tool.jsonl")])
    request = stage_request(episode)
    result = driver.run_stage(
        request, episode=episode, isolation_dir=driver.create_isolation_dir(),
        session_id=None,
    )
    assert result["tool_events"][0]["item"]["type"] == "command_execution"
    assert result["integrity"]["tools_absent"] is False
    assert result["terminal_status"] == "invalidated"


@pytest.mark.parametrize("payload", [
    {"type": "function_call", "name": "read_config", "arguments": "{}"},
    {"type": "custom_tool_call", "name": "schema_probe", "input": "{}"},
    {"type": "tool_call", "name": "definition_lookup", "arguments": "{}"},
])
def test_rollout_active_tool_structure_dominates_inert_name_markers(payload):
    records = [{"type": "response_item", "payload": payload}]
    evidence = codex_driver._rollout_tool_evidence(records)

    assert len(evidence) == 1
    assert evidence[0]["record_index"] == 0
    assert len(evidence[0]["record_sha256"]) == 64


@pytest.mark.parametrize("payload", [
    {
        "type": "message", "role": "assistant", "function_call": None,
    },
    {
        "type": "message", "role": "assistant", "tool_call": {},
    },
    {
        "type": "message", "role": "assistant",
        "tool_name": None, "arguments": None,
    },
    {
        "type": "message", "role": "assistant", "content": [{
            "type": "output_text", "function_call": {},
        }],
    },
])
def test_rollout_message_structural_tool_keys_fail_closed_even_empty(payload):
    records = [{"type": "response_item", "payload": payload}]
    evidence = codex_driver._rollout_tool_evidence(records)

    assert len(evidence) == 1
    assert evidence[0]["record_index"] == 0


@pytest.mark.parametrize("exposure", ["text", "hash"])
def test_future_text_or_hash_in_early_raw_evidence_invalidates(
        episode, tmp_path, exposure):
    leaked = episode["multiturn_script"]["stage_3"]
    if exposure == "hash":
        leaked = contracts.sha256_utf8(leaked)
    raw = fixture("valid.jsonl").replace(
        b"I should apply the stated evidence.", leaked.encode("utf-8")
    )
    driver, _ = make_driver(tmp_path, [raw])
    request = stage_request(episode)
    result = driver.run_stage(
        request, episode=episode, isolation_dir=driver.create_isolation_dir(),
        session_id=None,
    )
    assert result["integrity"]["future_text_absent"] is False
    assert result["terminal_status"] == "invalidated"


def test_explicit_pre_token_transport_error_retries_then_succeeds(
        episode, tmp_path):
    driver, executor = make_driver(tmp_path, [
        fixture("pre-token-transport.jsonl"), fixture("valid.jsonl")
    ])
    request = stage_request(episode)
    result = driver.run_stage(
        request, episode=episode, isolation_dir=driver.create_isolation_dir(),
        session_id=None,
    )
    assert len(executor.calls) == 2
    assert result["transport_retry_count"] == 1
    assert len(result["attempts"]) == 2
    assert result["attempts"][0]["token_emission_started"] is False
    assert result["attempts"][0]["error_code"] == "pre_token_transport_error"
    assert result["terminal_status"] == "complete"
    assert driver.test_sleeper.delays == [1]


def test_actual_pre_token_usage_limit_pair_is_durable_and_retryable(
        episode, tmp_path):
    raw = fixture("pre-token-usage-limit.jsonl")
    outcomes = [
        codex_driver.ExecutionOutcome(
            stdout_chunks=(raw,), stderr=b"", exit_status=1,
        )
        for _ in range(3)
    ]
    driver, executor = make_driver(tmp_path, outcomes)

    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )

    assert len(executor.calls) == 3
    assert driver.test_sleeper.delays == [1, 2]
    assert result["transport_retry_count"] == 2
    assert result["terminal_status"] == "invalidated"
    assert [row["error_code"] for row in result["attempts"]] == [
        "pre_token_transport_error",
        "pre_token_transport_error",
        "pre_token_transport_error",
    ]
    assert all(row["raw_trace"] == raw.decode("utf-8")
               for row in result["attempts"])


def test_mismatched_usage_limit_terminal_pair_never_authorizes_retry(
        episode, tmp_path):
    raw = fixture("pre-token-usage-limit.jsonl").replace(
        b'purchase more credits or try again later."}}',
        b'purchase more credits or contact support."}}',
    )
    driver, executor = make_driver(
        tmp_path, [raw, fixture("valid.jsonl")]
    )

    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )

    assert len(executor.calls) == 1
    assert driver.test_sleeper.delays == []
    assert result["terminal_status"] == "invalidated"


def test_executor_exception_is_not_a_retryable_provider_error(
        episode, tmp_path):
    driver, executor = make_driver(
        tmp_path,
        [codex_driver.CodexPreTokenTransportError("not persisted")],
    )
    with pytest.raises(codex_driver.CodexDriverError, match="executor"):
        driver.run_stage(
            stage_request(episode), episode=episode,
            isolation_dir=driver.create_isolation_dir(), session_id=None,
        )
    assert len(executor.calls) == 1
    assert driver.test_sleeper.delays == []


def test_malformed_trace_cannot_borrow_later_transport_error_for_retry(
        episode, tmp_path):
    raw = (
        b'{"type":"thread.started","thread_id":"' + THREAD.encode() + b'"}\n'
        b'{"type":"turn.started"}\n'
        b'{malformed}\n'
        b'{"type":"error","message":"transport error: connection reset"}\n'
    )
    driver, executor = make_driver(tmp_path, [raw])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert len(executor.calls) == 1
    assert driver.test_sleeper.delays == []
    assert result["terminal_status"] == "invalidated"


def test_transport_retries_are_capped_at_two(episode, tmp_path):
    driver, executor = make_driver(
        tmp_path, [fixture("pre-token-transport.jsonl")] * 3
    )
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert len(executor.calls) == 3
    assert driver.test_sleeper.delays == [1, 2]
    assert result["transport_retry_count"] == 2
    assert result["terminal_status"] == "invalidated"


def test_exhausted_or_midstream_transport_never_authorizes_episode_rerun(
        episode, tmp_path):
    for outputs in (
        [fixture("pre-token-transport.jsonl")] * 3,
        [fixture("midstream-error.jsonl")],
    ):
        driver, executor = make_driver(tmp_path, outputs)
        run = driver.run_episode(
            episode, logical_model_id="gpt-5.5",
            allow_integrity_rerun=True,
        )
        assert len(run.attempts) == 1
        assert run.authorization is None
        assert "transport_error" in run.results[-1]["integrity"]["violations"]
        assert not executor.outputs


def test_midstream_error_never_retries(episode, tmp_path):
    driver, executor = make_driver(
        tmp_path, [fixture("midstream-error.jsonl")]
    )
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert len(executor.calls) == 1
    assert result["attempts"][0]["token_emission_started"] is True
    assert result["terminal_status"] == "invalidated"


def test_nonzero_process_exit_is_preserved_and_invalidates_without_retry(
        episode, tmp_path):
    outcome = codex_driver.ExecutionOutcome(
        stdout_chunks=(fixture("valid.jsonl"),), stderr=b"safe diagnostic",
        exit_status=7,
    )
    driver, executor = make_driver(tmp_path, [outcome])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert len(executor.calls) == 1
    assert result["attempts"][0]["exit_status"] == 7
    assert result["attempts"][0]["error_code"] == "nonzero_exit"
    assert result["integrity"]["transport_successful"] is False
    assert result["terminal_status"] == "invalidated"


def test_nonzero_exit_never_authorizes_episode_rerun(episode, tmp_path):
    outcome = codex_driver.ExecutionOutcome(
        stdout_chunks=(fixture("valid.jsonl"),), stderr=b"safe",
        exit_status=9,
    )
    driver, _ = make_driver(tmp_path, [outcome])
    run = driver.run_episode(
        episode, logical_model_id="gpt-5.5", allow_integrity_rerun=True
    )
    assert len(run.attempts) == 1
    assert run.authorization is None
    assert "transport_error" in run.results[-1]["integrity"]["violations"]


def test_invalid_canonical_response_is_unresolved_without_repair_or_retry(
        episode, tmp_path):
    driver, executor = make_driver(
        tmp_path, [fixture("invalid-response.jsonl")]
    )
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert len(executor.calls) == 1
    assert result["attempts"][0]["raw_final_message"].startswith("INTENT:")
    assert result["attempts"][0]["parsed_response"] is None
    assert result["terminal_status"] == "unresolved"
    assert result["integrity"]["integrity_valid"] is True


def test_incomplete_trace_invalidates_without_retry(episode, tmp_path):
    driver, executor = make_driver(tmp_path, [fixture("incomplete.jsonl")])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert len(executor.calls) == 1
    assert result["attempts"][0]["raw_trace"] == (
        fixture("incomplete.jsonl").decode("utf-8")
    )
    assert result["terminal_status"] == "invalidated"


def test_chunked_jsonl_is_parsed_incrementally_and_preserved_exactly(
        episode, tmp_path):
    raw = fixture("valid.jsonl")
    chunks = [raw[:17], raw[17:113], raw[113:219], raw[219:]]
    driver, _ = make_driver(tmp_path, [chunks])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    assert result["attempts"][0]["raw_trace"] == raw.decode("utf-8")
    assert result["terminal_status"] == "complete"


def test_crlf_binary_trace_is_preserved_before_strict_utf8_decode(
        episode, tmp_path):
    raw = fixture("valid.jsonl").replace(b"\n", b"\r\n")
    chunks = (raw[:23], raw[23:207], raw[207:])
    driver, _ = make_driver(tmp_path, [chunks])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    attempt = result["attempts"][0]
    assert attempt["raw_trace"].encode("utf-8") == raw
    assert attempt["raw_trace_sha256"] == hashlib.sha256(raw).hexdigest()
    assert result["terminal_status"] == "complete"


def test_credentials_are_never_written_into_result_or_exception(
        episode, tmp_path):
    raw = fixture("valid.jsonl").replace(
        b"I should apply the stated evidence.", b"Bearer abcdefghijklmnop"
    )
    driver, _ = make_driver(tmp_path, [raw])
    with pytest.raises(codex_driver.CodexDriverError) as caught:
        driver.run_stage(
            stage_request(episode), episode=episode,
            isolation_dir=driver.create_isolation_dir(), session_id=None,
        )
    assert "abcdefghijklmnop" not in str(caught.value)
    assert "credential" in str(caught.value).lower()


def test_integrity_failure_authorizes_one_fresh_whole_episode_rerun(
        episode, tmp_path):
    driver, executor = make_driver(
        tmp_path,
        [fixture("tool.jsonl")] + [fixture("valid.jsonl")] * 4,
    )
    run = driver.run_episode(
        episode, logical_model_id="gpt-5.5", allow_integrity_rerun=True
    )
    assert len(run.attempts) == 2
    assert run.authorization["authorized"] is True
    assert run.attempts[0].results[-1]["terminal_status"] == "invalidated"
    assert run.chain is not None and run.chain["measurement_ready"] is False
    assert run.attempts[0].execution_id != run.attempts[1].execution_id
    assert run.attempts[0].isolation_dir != run.attempts[1].isolation_dir
    assert len(executor.calls) == 5


def test_successful_process_incomplete_trace_may_authorize_integrity_rerun(
        episode, tmp_path):
    driver, _ = make_driver(
        tmp_path,
        [fixture("incomplete.jsonl")] + [fixture("valid.jsonl")] * 4,
    )
    run = driver.run_episode(
        episode, logical_model_id="gpt-5.5", allow_integrity_rerun=True
    )
    assert len(run.attempts) == 2
    assert run.authorization["authorized"] is True
    first = run.attempts[0].results[-1]
    assert first["integrity"]["transport_successful"] is True
    assert first["terminal_status"] == "invalidated"


def test_parse_failure_cannot_authorize_integrity_rerun(episode, tmp_path):
    driver, executor = make_driver(
        tmp_path,
        [fixture("invalid-response.jsonl")] + [fixture("valid.jsonl")] * 3,
    )
    run = driver.run_episode(
        episode, logical_model_id="gpt-5.5", allow_integrity_rerun=True
    )
    assert len(run.attempts) == 1
    assert run.authorization is None
    assert run.results[0]["terminal_status"] == "unresolved"
    assert len(executor.calls) == 4


def test_attested_isolation_and_turn_count_are_fail_closed(
        episode, tmp_path):
    for mutation in (
        {"sandbox": "workspace-write"},
        {"turn_count": 7},
        {"cli_version": "0.135.0"},
    ):
        driver, _ = make_driver(
            tmp_path, [fixture("valid.jsonl")],
            attestor=FakeAttestor([mutation]),
        )
        result = driver.run_stage(
            stage_request(episode), episode=episode,
            isolation_dir=driver.create_isolation_dir(), session_id=None,
        )
        assert result["integrity"]["isolation_ok"] is False
        assert result["terminal_status"] == "invalidated"


def test_subprocess_stderr_and_transport_descriptor_do_not_enter_records(
        episode, tmp_path):
    outcome = codex_driver.ExecutionOutcome(
        stdout_chunks=(fixture("valid.jsonl"),),
        stderr=b"OPENROUTER_API_KEY=not-recorded-secret",
        exit_status=0,
    )
    driver, _ = make_driver(tmp_path, [outcome])
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    serialized = json.dumps(result, sort_keys=True)
    assert "not-recorded-secret" not in serialized
    assert result["transport_request_sha256"] == (
        driver.last_transport_request_sha256
    )


def _rehash_result(result):
    result["result_sha256"] = contracts.canonical_sha256({
        key: value for key, value in result.items()
        if key != "result_sha256"
    })


def _rehash_attestation(attestation):
    attestation["attestation_sha256"] = contracts.canonical_sha256({
        key: value for key, value in attestation.items()
        if key != "attestation_sha256"
    })


def test_persisted_transport_and_attestation_records_revalidate_exactly(
        episode, tmp_path):
    driver, _ = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    run = driver.run_episode(episode, logical_model_id="gpt-5.5")

    assert driver.validate_episode_attempt(run.final, episode) == run.final
    for descriptor, attestation, result in zip(
            run.transport_descriptors, run.attestations, run.results):
        assert set(descriptor) == codex_driver.TRANSPORT_DESCRIPTOR_KEYS
        assert set(attestation) == codex_driver.ATTESTATION_RECORD_KEYS
        assert contracts.canonical_sha256(descriptor) == result[
            "transport_request_sha256"
        ]


def test_zeroed_and_rehashed_transport_descriptor_is_rejected(
        episode, tmp_path):
    driver, _ = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    run = driver.run_episode(episode, logical_model_id="gpt-5.5")
    poisoned = deepcopy(run.final)
    descriptor = poisoned.transport_descriptors[0]
    descriptor["stdin_sha256"] = "0" * 64
    poisoned.results[0]["transport_request_sha256"] = (
        contracts.canonical_sha256(descriptor)
    )
    _rehash_result(poisoned.results[0])
    assert contracts.validate_stage_result(
        poisoned.results[0], poisoned.requests[0]
    ) == poisoned.results[0]

    with pytest.raises(codex_driver.CodexDriverError, match="descriptor"):
        driver.validate_episode_attempt(poisoned, episode)


def test_rehashed_flipped_attestation_evidence_is_rejected(
        episode, tmp_path):
    driver, _ = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    run = driver.run_episode(episode, logical_model_id="gpt-5.5")
    poisoned = deepcopy(run.final)
    poisoned.attestations[0]["future_text_absent"] = False
    _rehash_attestation(poisoned.attestations[0])

    with pytest.raises(codex_driver.CodexDriverError, match="attestation"):
        driver.validate_episode_attempt(poisoned, episode)


def test_rehashed_result_session_cannot_detach_from_attested_thread(
        episode, tmp_path):
    driver, _ = make_driver(tmp_path, [fixture("valid.jsonl")] * 4)
    run = driver.run_episode(episode, logical_model_id="gpt-5.5")
    poisoned = deepcopy(run.final)
    poisoned.results[0]["session_id"] = (
        "019e2222-2222-7222-8222-222222222222"
    )
    _rehash_result(poisoned.results[0])
    assert contracts.validate_stage_result(
        poisoned.results[0], poisoned.requests[0]
    ) == poisoned.results[0]
    with pytest.raises(codex_driver.CodexDriverError, match="attestation"):
        driver.validate_episode_attempt(poisoned, episode)


@pytest.mark.parametrize("evidence_time", [
    "2026-07-09T00:00:00Z",
    "2030-01-01T00:00:00Z",
])
def test_out_of_interval_rollout_with_future_prompt_and_identifier_is_rejected(
        episode, tmp_path, evidence_time):
    isolation = tmp_path / "cx-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    codex_home = tmp_path / "codex-home"
    rollout = (
        codex_home / "sessions" / "2026" / "07" / "10"
        / f"rollout-test-{THREAD}.jsonl"
    )
    rollout.parent.mkdir(parents=True)
    records = [
        {
            "timestamp": evidence_time,
            "type": "session_meta",
            "payload": {
                "id": THREAD, "cli_version": "0.134.0",
                "model_provider": "openai", "cwd": str(isolation),
                "base_instructions": "Return only the requested object.",
            },
        },
        {
            "timestamp": evidence_time,
            "type": "turn_context",
            "payload": {
                "model": "gpt-5.5", "cwd": str(isolation),
                "sandbox_policy": {"type": "read-only"},
                "effort": "medium",
            },
        },
        {
            "timestamp": evidence_time,
            "type": "response_item",
            "payload": {
                "role": "user",
                "content": (
                    episode["multiturn_script"]["stage_3"]
                    + " 10CB-07-aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"
                ),
            },
        },
    ]
    rollout.write_bytes(b"".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")).encode("utf-8")
        + b"\n" for row in records
    ))
    evidence_epoch = _parse_test_time(evidence_time).timestamp()
    os.utime(rollout, (evidence_epoch, evidence_epoch))

    executor = FakeExecutor([fixture("valid.jsonl")])
    driver = codex_driver.CodexDriver(
        run_mode="mock", executor=executor,
        attestor=codex_driver.CodexRolloutAttestor(codex_home),
        clock=FakeClock(),
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        tempdir_factory=lambda: isolation,
        sleeper=FakeSleeper(), codex_binary="codex",
    )
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    evidence = driver.last_rollout_attestation
    assert evidence["source"] == "rollout"
    assert evidence["future_text_absent"] is False
    assert evidence["identifier_absent"] is False
    assert result["terminal_status"] == "invalidated"
    assert result["integrity"]["measurement_ready"] is False


def test_rollout_only_function_call_invalidates_and_external_copy_rejected(
        episode, tmp_path):
    isolation = tmp_path / "cx-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    codex_home = tmp_path / "codex-home"
    rollout = (
        codex_home / "sessions" / "2026" / "07" / "10"
        / f"rollout-tool-{THREAD}.jsonl"
    )
    rollout.parent.mkdir(parents=True)
    stamp = "2026-07-10T00:00:00Z"
    response = _valid_response_text()
    records = [
        {
            "timestamp": stamp, "type": "session_meta",
            "payload": {
                "id": THREAD, "cli_version": "0.134.0",
                "model_provider": "openai", "cwd": str(isolation),
            },
        },
        {
            "timestamp": stamp, "type": "turn_context",
            "payload": {
                "model": "gpt-5.5", "cwd": str(isolation),
                "sandbox_policy": {"type": "read-only"},
                "effort": "medium",
            },
        },
        {
            "timestamp": stamp, "type": "response_item",
            "payload": {"type": "message", "role": "user",
                        "content": episode["multiturn_script"]["stage_1"]},
        },
        {
            "timestamp": stamp, "type": "response_item",
            "payload": {
                "type": "function_call", "name": "exec_command",
                "arguments": "{}",
            },
        },
        {
            "timestamp": stamp, "type": "response_item",
            "payload": {"type": "message", "role": "assistant",
                        "content": response},
        },
    ]
    raw = b"".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")).encode()
        + b"\n" for row in records
    )
    rollout.write_bytes(raw)
    mtime = datetime(2026, 7, 10, 0, 0, 1, tzinfo=timezone.utc).timestamp()
    os.utime(rollout, (mtime, mtime))
    attestor = codex_driver.CodexRolloutAttestor(codex_home)
    driver = codex_driver.CodexDriver(
        run_mode="mock", executor=FakeExecutor([fixture("valid.jsonl")]),
        attestor=attestor, clock=FakeClock(),
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        tempdir_factory=lambda: isolation, sleeper=FakeSleeper(),
        codex_binary="codex",
    )
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    evidence = driver.last_rollout_attestation
    assert evidence["current_prompt_linked"] is True
    assert evidence["final_response_linked"] is True
    assert evidence["rollout_tools_absent"] is False
    assert result["integrity"]["tools_absent"] is False
    assert result["tool_events"][-1]["type"] == "rollout_tool_activity"
    assert result["terminal_status"] == "invalidated"

    external = tmp_path / "external-rollout.jsonl"
    external.write_bytes(raw)
    os.utime(external, (mtime, mtime))
    poisoned = deepcopy(evidence)
    poisoned["rollout_path"] = str(external)
    _rehash_attestation(poisoned)
    with pytest.raises(codex_driver.CodexDriverError, match="production root"):
        attestor.rederive_attestation(
            poisoned,
            future_turns=model_turns_for_test(episode)[1:],
            current_prompt=episode["multiturn_script"]["stage_1"],
            expected_response=response,
        )


@pytest.mark.parametrize("broken_link", ["prompt", "response"])
def test_rollout_stage_requires_exact_current_prompt_and_response_link(
        episode, tmp_path, broken_link):
    isolation = tmp_path / "cx-cccccccccccccccccccccccccccccccc"
    codex_home = tmp_path / "codex-home"
    rollout = (
        codex_home / "sessions" / "2026" / "07" / "10"
        / f"rollout-link-{THREAD}.jsonl"
    )
    rollout.parent.mkdir(parents=True)
    stamp = "2026-07-10T00:00:00Z"
    response = _valid_response_text()
    records = [{
        "timestamp": stamp, "type": "session_meta",
        "payload": {
            "id": THREAD, "cli_version": "0.134.0",
            "model_provider": "openai", "cwd": str(isolation),
        },
    }]
    records.append({
        "timestamp": stamp, "type": "turn_context",
        "payload": {
            "model": "gpt-5.5", "cwd": str(isolation),
            "sandbox_policy": {"type": "read-only"},
            "effort": "medium",
        },
    })
    if broken_link != "prompt":
        records.append({
            "timestamp": stamp, "type": "response_item",
            "payload": {"type": "message", "role": "user",
                        "content": episode["multiturn_script"]["stage_1"]},
        })
    records.append({
        "timestamp": stamp, "type": "response_item",
        "payload": {"type": "message", "role": "assistant",
                    "content": (
                        "wrong response" if broken_link == "response"
                        else response
                    )},
    })
    rollout.write_bytes(b"".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")).encode()
        + b"\n" for row in records
    ))
    mtime = datetime(2026, 7, 10, 0, 0, 1, tzinfo=timezone.utc).timestamp()
    os.utime(rollout, (mtime, mtime))
    driver = codex_driver.CodexDriver(
        run_mode="mock", executor=FakeExecutor([fixture("valid.jsonl")]),
        attestor=codex_driver.CodexRolloutAttestor(codex_home),
        clock=FakeClock(),
        uuid_factory=lambda: "9ef76c30-b620-4ea7-a719-91f3e46cc8b2",
        tempdir_factory=lambda: isolation, sleeper=FakeSleeper(),
        codex_binary="codex",
    )
    result = driver.run_stage(
        stage_request(episode), episode=episode,
        isolation_dir=driver.create_isolation_dir(), session_id=None,
    )
    evidence = driver.last_rollout_attestation
    assert evidence["current_prompt_linked"] is (broken_link != "prompt")
    assert evidence["final_response_linked"] is (broken_link != "response")
    assert evidence["rollout_tools_absent"] is True
    assert result["integrity"]["session_chain_ok"] is False
    assert result["terminal_status"] == "invalidated"


@pytest.mark.parametrize("poison", [
    "borrow_prior_response",
    "duplicate_current_prompt",
    "nonterminal_current_response",
])
def test_rollout_stage_links_require_ordered_unique_prompt_and_terminal_response(
        tmp_path, poison):
    isolation = tmp_path / "cx-dddddddddddddddddddddddddddddddd"
    codex_home = tmp_path / "codex-home"
    rollout = (
        codex_home / "sessions" / "2026" / "07" / "10"
        / f"rollout-window-{THREAD}.jsonl"
    )
    rollout.parent.mkdir(parents=True)
    stamp = "2026-07-10T00:00:00Z"
    prompt = "current stage prompt"
    response = (
        '{"reason":"same","INTENT":"UNCERTAIN","DECISION":"VERIFY"}'
    )
    records = [
        {
            "timestamp": stamp, "type": "session_meta",
            "payload": {
                "id": THREAD, "cli_version": "0.134.0",
                "model_provider": "openai",
            },
        },
        {
            "timestamp": stamp, "type": "turn_context",
            "payload": {
                "model": "gpt-5.5", "cwd": str(isolation),
                "sandbox_policy": {"type": "read-only"},
                "effort": "medium",
            },
        },
    ]
    if poison == "borrow_prior_response":
        records.append({
            "timestamp": stamp, "type": "response_item",
            "payload": {
                "type": "message", "role": "assistant",
                "content": response,
            },
        })
    records.append({
        "timestamp": stamp, "type": "turn_context",
        "payload": {
            "model": "gpt-5.5", "cwd": str(isolation),
            "sandbox_policy": {"type": "read-only"}, "effort": "medium",
        },
    })
    records.append({
        "timestamp": stamp, "type": "response_item",
        "payload": {"type": "message", "role": "user", "content": prompt},
    })
    if poison == "duplicate_current_prompt":
        records.append({
            "timestamp": stamp, "type": "response_item",
            "payload": {
                "type": "message", "role": "user", "content": prompt,
            },
        })
    if poison != "borrow_prior_response":
        records.append({
            "timestamp": stamp, "type": "response_item",
            "payload": {
                "type": "message", "role": "assistant",
                "content": response,
            },
        })
    if poison == "nonterminal_current_response":
        records.append({
            "timestamp": stamp, "type": "response_item",
            "payload": {
                "type": "message", "role": "assistant",
                "content": "later assistant response",
            },
        })
    rollout.write_bytes(b"".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")).encode()
        + b"\n" for row in records
    ))

    projection = codex_driver.CodexRolloutAttestor(codex_home)._project(
        rollout,
        future_turns=[], current_prompt=prompt, expected_response=response,
    )

    if poison == "duplicate_current_prompt":
        assert projection["current_prompt_linked"] is False
        assert projection["final_response_linked"] is True
    else:
        assert projection["current_prompt_linked"] is True
        assert projection["final_response_linked"] is False


@pytest.mark.parametrize("poison", [
    "later_user",
    "later_reasoning",
    "intervening_user",
])
def test_rollout_current_assistant_must_be_terminal_response_item(
        tmp_path, poison):
    isolation = tmp_path / "cx-eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    codex_home = tmp_path / "codex-home"
    rollout = (
        codex_home / "sessions" / "2026" / "07" / "10"
        / f"rollout-terminal-{THREAD}.jsonl"
    )
    rollout.parent.mkdir(parents=True)
    stamp = "2026-07-10T00:00:00Z"
    prompt = "current stage prompt"
    response = (
        '{"reason":"same","INTENT":"UNCERTAIN","DECISION":"VERIFY"}'
    )
    records = [
        {
            "timestamp": stamp, "type": "session_meta",
            "payload": {
                "id": THREAD, "cli_version": "0.134.0",
                "model_provider": "openai",
            },
        },
        {
            "timestamp": stamp, "type": "turn_context",
            "payload": {
                "model": "gpt-5.5", "cwd": str(isolation),
                "sandbox_policy": {"type": "read-only"},
                "effort": "medium",
            },
        },
        {
            "timestamp": stamp, "type": "response_item",
            "payload": {
                "type": "message", "role": "user", "content": prompt,
            },
        },
    ]
    if poison == "intervening_user":
        records.append({
            "timestamp": stamp, "type": "response_item",
            "payload": {
                "type": "message", "role": "user",
                "content": "later prompt",
            },
        })
    records.append({
        "timestamp": stamp, "type": "response_item",
        "payload": {
            "type": "message", "role": "assistant", "content": response,
        },
    })
    if poison == "later_user":
        records.append({
            "timestamp": stamp, "type": "response_item",
            "payload": {
                "type": "message", "role": "user",
                "content": "later prompt",
            },
        })
    elif poison == "later_reasoning":
        records.append({
            "timestamp": stamp, "type": "response_item",
            "payload": {"type": "reasoning", "summary": []},
        })
    rollout.write_bytes(b"".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")).encode()
        + b"\n" for row in records
    ))

    projection = codex_driver.CodexRolloutAttestor(codex_home)._project(
        rollout,
        future_turns=[], current_prompt=prompt, expected_response=response,
    )

    assert projection["current_prompt_linked"] is (
        poison == "later_reasoning"
    )
    assert projection["final_response_linked"] is (
        poison == "intervening_user"
    )


def test_fixture_provenance_readme_lists_exact_synthetic_hashes():
    readme = (FIXTURES / "README.md").read_text(encoding="utf-8")
    assert "0.134.0" in readme
    assert "synthetic" in readme.lower()
    assert "not captured" in readme.lower()
    for path in sorted(FIXTURES.glob("*.jsonl")):
        assert path.name in readme
        assert hashlib.sha256(path.read_bytes()).hexdigest() in readme


def test_rollout_symlink_ancestor_is_rejected(tmp_path):
    codex_home = tmp_path / "codex-home"
    external = tmp_path / "external-sessions"
    target = external / "2026" / "07" / "10" / f"rollout-{THREAD}.jsonl"
    target.parent.mkdir(parents=True)
    target.write_bytes(b"{}\n")
    codex_home.mkdir()
    (codex_home / "sessions").symlink_to(external, target_is_directory=True)
    attestor = codex_driver.CodexRolloutAttestor(codex_home)
    lexical = codex_home / "sessions" / "2026" / "07" / "10" / target.name
    with pytest.raises(codex_driver.CodexDriverError, match="symlink"):
        attestor._safe_rollout_path(lexical)
