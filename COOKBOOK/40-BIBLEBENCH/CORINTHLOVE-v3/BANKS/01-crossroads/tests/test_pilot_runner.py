from __future__ import annotations

from copy import deepcopy
import json
import shutil
import sys
from pathlib import Path

import pytest


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK))

from pilot import cli, contracts, executor  # noqa: E402
from pilot.runner import QualificationRunner  # noqa: E402
from pilot.verify import verify_run  # noqa: E402


SNAPSHOTS = {
    alias: row["expected_snapshot"]
    for alias, row in contracts.load_profile()["models"].items()
}


def _rewrite_artifact_and_rechain(root: Path, relative: Path, payload: dict) -> None:
    """Simulate an attacker who rewrites bytes and recomputes the whole journal."""
    path = root / relative
    path.write_bytes(contracts.canonical_bytes(payload))
    journal = root / "journal.jsonl"
    entries = [json.loads(line) for line in journal.read_text().splitlines()]
    relative_text = relative.as_posix()
    for entry in entries:
        if entry["artifact"] == relative_text:
            entry["artifact_sha256"] = contracts.sha256_value(payload)
    previous = "0" * 64
    for entry in entries:
        entry["previous_entry_sha256"] = previous
        previous = contracts.sha256_value(entry)
    journal.write_bytes(b"".join(contracts.canonical_bytes(row) for row in entries))


def _assert_whole_root_semantic_rejection(tmp_path: Path, source: Path,
                                          relative: Path, payload: dict,
                                          label: str) -> None:
    clone = tmp_path / f"tamper-{label}"
    shutil.copytree(source, clone)
    _rewrite_artifact_and_rechain(clone, relative, payload)
    with pytest.raises(ValueError):
        verify_run(clone, bank_root=BANK)


class FakeOpenRouter:
    def __init__(self, *, fail_completions=0):
        self.catalog_calls = []
        self.requests = []
        self.fail_completions = fail_completions
        self.counter = 0

    def catalog(self, alias):
        self.catalog_calls.append(alias)
        model = contracts.resolve_model(alias)
        ceilings = model["price_ceiling_per_token"]
        endpoint = {
            "model_id": alias, "provider_name": "Azure",
            "name": f"Azure | {model['expected_snapshot']}",
            "tag": "azure", "status": 0,
            "context_length": 400_000,
            "supported_parameters": list(contracts.REQUIRED_PARAMETERS),
            "pricing": {
                "prompt": str(ceilings["input"]),
                "completion": str(ceilings["output"]),
            },
        }
        return {
            "catalog_evidence_version": "openrouter-model-zdr-intersection-v1",
            "model_id": alias,
            "model_catalog_url": (
                f"https://openrouter.ai/api/v1/models/{alias}/endpoints"
            ),
            "zdr_catalog_url": "https://openrouter.ai/api/v1/endpoints/zdr",
            "model_catalog_response": {
                "data": {
                    "id": alias, "endpoints": [deepcopy(endpoint)],
                },
            },
            "zdr_catalog_response": {
                "data": [{**deepcopy(endpoint), "model_id": alias}],
            },
        }

    def complete(self, body):
        self.requests.append(deepcopy(body))
        if self.fail_completions:
            self.fail_completions -= 1
            raise RuntimeError("scripted transport failure")
        self.counter += 1
        call_id = f"fake-{self.counter:04d}"
        alias = body["model"]
        message = {"role": "assistant", "content": "{}", "tool_calls": []}
        finish = "stop"
        if body.get("tools"):
            schema = body["tools"][0]["function"]["parameters"]["oneOf"][0]
            action = {
                key: deepcopy(value["const"])
                for key, value in schema["properties"].items()
            }
            message = {
                "role": "assistant", "content": None,
                "tool_calls": [{
                    "id": f"tool-{call_id}", "type": "function",
                    "function": {"name": "execute_action",
                                 "arguments": json.dumps(action)},
                }],
            }
            finish = "tool_calls"
        raw = {
            "response": {
                "id": call_id, "model": SNAPSHOTS[alias],
                "provider": "Azure",
                "choices": [{"finish_reason": finish, "message": message}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 2,
                          "total_tokens": 12, "cost": 0.000001},
                "openrouter_metadata": {
                    "requested": alias, "strategy": "direct", "attempt": 1,
                    "endpoints": {"total": 1, "available": [{
                        "provider": "Azure", "model": SNAPSHOTS[alias],
                        "selected": True,
                    }]},
                },
            },
            "response_headers": {"x_generation_id": [call_id]},
        }
        return raw


class TruncatedForkOpenRouter(FakeOpenRouter):
    def __init__(self):
        super().__init__()
        self.truncated = False

    def complete(self, body):
        raw = super().complete(body)
        if body.get("tools") and not self.truncated:
            self.truncated = True
            choice = raw["response"]["choices"][0]
            choice["finish_reason"] = "length"
            choice["native_finish_reason"] = "max_output_tokens"
            choice["message"]["tool_calls"][0]["function"][
                "arguments"
            ] = '{"tool":"field.alert"'
            raw["response"]["usage"] = {
                "prompt_tokens": 10, "completion_tokens": 2048,
                "completion_tokens_details": {"reasoning_tokens": 1600},
                "total_tokens": 2058, "cost": 0.0008,
            }
        return raw


class TruncatedFollowOpenRouter(FakeOpenRouter):
    def __init__(self):
        super().__init__()
        self.tool_calls_seen = 0

    def complete(self, body):
        raw = super().complete(body)
        if body.get("tools"):
            self.tool_calls_seen += 1
            if self.tool_calls_seen == 2:
                choice = raw["response"]["choices"][0]
                choice["finish_reason"] = "length"
                choice["native_finish_reason"] = "max_output_tokens"
        return raw


class RejectedAccessOpenRouter(FakeOpenRouter):
    def complete(self, body):
        raw = super().complete(body)
        if not body.get("tools"):
            raw["response"]["provider"] = "Other"
        return raw


class OverflowAccessOpenRouter(FakeOpenRouter):
    def complete(self, body):
        raw = super().complete(body)
        if not body.get("tools"):
            raw["response"]["usage"]["cost"] = 10 ** 10000
        return raw


class TransportForkOpenRouter(FakeOpenRouter):
    def complete(self, body):
        if body.get("tools"):
            raise RuntimeError("scripted staged transport failure")
        return super().complete(body)


def test_full_mock_lifecycle_reuses_canaries_and_semantically_verifies(tmp_path):
    client = FakeOpenRouter()
    root = tmp_path / "run"
    runner = QualificationRunner.create(
        root, bank_root=BANK, client=client,
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    runner.access()
    assert client.requests[0]["max_completion_tokens"] == 512
    runner.canary()
    calls_after_canary = len(client.requests)
    assert calls_after_canary == 1 + 6 * 3
    runner.smoke()
    assert len(client.requests) == calls_after_canary + 24 * 3
    assert runner.smoke() == runner.load_report()
    report = runner.load_report()
    assert report["purpose"] == "public qualification"
    assert report["provenance"] == contracts.PROVENANCE_MOCK
    assert report["measurement_ready"] is False
    assert report["public_qualification_evidence"] is True
    assert report["execution_mode"] == "path-only staged qualification"
    assert report["canonical_e_measurement"] is False
    assert report["issues_live_judges"] is False
    assert report["authorizes_model_ranking"] is False
    assert report["authorizes_private_execution"] is False
    assert set(report["models"]["openai/gpt-5-nano"]) >= {
        "path_resolution", "evasion_rate", "path_entropy_bits",
        "clause_profile_dispersion", "surface_cue_decoding",
        "repair_resolution_rate", "closeout_resolution_rate",
        "positive_duty_completion_rate",
    }
    assert len(report["blinded_item_path_choices"]) == 30
    path_diagnostics = report["cross_model_path_diagnostics"]
    assert path_diagnostics["public_item_count"] == 30
    assert set(path_diagnostics) >= {
        "all_models_same_path_count", "all_models_same_path_rate",
        "mean_distinct_resolved_paths_per_item", "pairwise_exact_path",
    }
    rendered = json.dumps(report).lower()
    assert "auc" not in rendered and "correctness" not in rendered
    verification = verify_run(root, bank_root=BANK, require_phase="smoke")
    assert verification["valid"] is True
    assert verification["authorizes_model_ranking"] is False
    assert verification["successful_episode_artifacts"] == 30


def test_manifest_binds_transport_contract_and_runner_runtime(tmp_path):
    runner = QualificationRunner.create(
        tmp_path / "run", bank_root=BANK, client=FakeOpenRouter(),
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    assert runner.manifest["manifest_version"] == (
        "crossroads-public-qualification-v6"
    )
    expected = {
        "pilot_contracts": contracts.sha256_file(BANK / "pilot" / "contracts.py"),
        "openrouter_transport": contracts.sha256_file(
            BANK / "pilot" / "openrouter.py"
        ),
        "runner": contracts.sha256_file(BANK / "pilot" / "runner.py"),
    }
    for name, digest in expected.items():
        assert runner.manifest["hashes"][name] == digest


def test_retry_requires_explicit_new_invocation_and_is_max_three(tmp_path):
    client = FakeOpenRouter(fail_completions=1)
    runner = QualificationRunner.create(
        tmp_path / "run", bank_root=BANK, client=client,
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    with pytest.raises(RuntimeError, match="failed attempt 1"):
        runner.access()
    access_dir = tmp_path / "run" / "access" / "openai--gpt-5-nano"
    attempts = sorted(access_dir.glob("attempt-*.json"))
    first_failure = json.loads(attempts[0].read_text())
    assert first_failure["status"] == "failed"
    access_evidence = first_failure["failure_evidence"]
    assert access_evidence["failure_evidence_version"] == (
        "crossroads-access-failure-v1"
    )
    assert access_evidence["failure_phase"] == "transport"
    assert access_evidence["raw_call"] is None
    assert access_evidence["request_sha256"] == contracts.sha256_value(
        access_evidence["request"]
    )
    request_count = len(client.requests)
    with pytest.raises(ValueError, match="explicit retry"):
        runner.access()
    assert len(client.requests) == request_count
    runner.access(retry_failed=True)
    attempts = sorted(access_dir.glob("attempt-*.json"))
    assert [json.loads(path.read_text())["status"] for path in attempts] == [
        "failed", "success",
    ]

    failing = FakeOpenRouter(fail_completions=4)
    runner2 = QualificationRunner.create(
        tmp_path / "run2", bank_root=BANK, client=failing,
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    with pytest.raises(RuntimeError, match="failed attempt 1"):
        runner2.access()
    with pytest.raises(RuntimeError, match="failed attempt 2"):
        runner2.access(retry_failed=True)
    with pytest.raises(RuntimeError, match="failed attempt 3"):
        runner2.access(retry_failed=True)
    with pytest.raises(ValueError, match="three-attempt ceiling"):
        runner2.access(retry_failed=True)
    assert len(list((tmp_path / "run2" / "access" / "openai--gpt-5-nano").glob(
        "attempt-*.json"))) == 3


def test_rejected_paid_access_response_is_preserved_and_canonically_replayed(
        tmp_path):
    root = tmp_path / "access-rejection"
    runner = QualificationRunner.create(
        root, bank_root=BANK, client=RejectedAccessOpenRouter(),
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    with pytest.raises(RuntimeError, match="access failed attempt 1"):
        runner.access()
    relative = Path("access/openai--gpt-5-nano/attempt-1.json")
    failed = json.loads((root / relative).read_text())
    evidence = failed["failure_evidence"]
    assert evidence["failure_phase"] == "attestation"
    assert evidence["raw_call"]["response"]["provider"] == "Other"
    assert evidence["request"] == runner._access_request(
        contracts.resolve_model("openai/gpt-5-nano"), 1
    )
    assert runner._validate_access(failed) is True
    assert verify_run(root, bank_root=BANK)["valid"] is True

    request_poison = deepcopy(failed)
    request_poison["failure_evidence"]["request"]["transport_body"]["messages"][
        0
    ]["content"] += " altered"
    request_poison["failure_evidence"]["request_sha256"] = contracts.sha256_value(
        request_poison["failure_evidence"]["request"]
    )
    assert runner._validate_access(request_poison) is False
    _assert_whole_root_semantic_rejection(
        tmp_path, root, relative, request_poison, "access-rehashed-request"
    )

    raw_poison = deepcopy(failed)
    raw_poison["failure_evidence"]["raw_call"]["response"]["provider"] = "Azure"
    assert runner._validate_access(raw_poison) is False
    _assert_whole_root_semantic_rejection(
        tmp_path, root, relative, raw_poison, "access-raw-response"
    )


def test_non_value_error_access_attestation_failure_still_preserves_raw_call(
        tmp_path):
    root = tmp_path / "access-overflow"
    runner = QualificationRunner.create(
        root, bank_root=BANK, client=OverflowAccessOpenRouter(),
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    with pytest.raises(RuntimeError, match="access failed attempt 1"):
        runner.access()
    relative = Path("access/openai--gpt-5-nano/attempt-1.json")
    failed = json.loads((root / relative).read_text())
    assert failed["error_code"] == "OverflowError"
    assert failed["failure_evidence"]["failure_phase"] == "attestation"
    assert isinstance(failed["failure_evidence"]["raw_call"], dict)
    assert runner._validate_access(failed) is True
    assert verify_run(root, bank_root=BANK)["valid"] is True
    poisoned = deepcopy(failed)
    poisoned["failure_evidence"] = None
    assert runner._validate_access(poisoned) is False
    _assert_whole_root_semantic_rejection(
        tmp_path, root, relative, poisoned, "access-overflow-dropped-evidence"
    )


def test_truncated_fork_is_durable_failure_and_never_completes_canary_or_evasion(
        tmp_path):
    client = TruncatedForkOpenRouter()
    root = tmp_path / "run"
    runner = QualificationRunner.create(
        root, bank_root=BANK, client=client,
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    runner.access()
    with pytest.raises(RuntimeError, match="episode failed attempt 1"):
        runner.canary()
    item_id = runner.manifest["canary_item_ids"][0]
    failed_path = (
        root / "episodes" / "openai--gpt-5-nano" / item_id / "attempt-1.json"
    )
    failed_relative = failed_path.relative_to(root)
    failed = json.loads(failed_path.read_text())
    assert failed["status"] == "failed"
    assert failed["error_code"] == "ValueError"
    assert "finish reason" in failed["error_message"]
    assert "normalized='length'" in failed["error_message"]
    assert "native='max_output_tokens'" in failed["error_message"]
    assert "completion_tokens=2048" in failed["error_message"]
    assert "reasoning_tokens=1600" in failed["error_message"]
    evidence = failed["failure_evidence"]
    assert evidence["failure_evidence_version"] == "crossroads-rejected-call-v2"
    assert evidence["failure_kind"] == "validation"
    assert evidence["failed_stage"] == "fork"
    assert evidence["completed_stages"] == []
    assert evidence["request_sha256"] == contracts.sha256_value(evidence["request"])
    assert evidence["request"]["transport_body"]["max_completion_tokens"] == 4096
    raw_choice = evidence["raw_call"]["response"]["choices"][0]
    assert raw_choice["finish_reason"] == "length"
    assert raw_choice["native_finish_reason"] == "max_output_tokens"
    assert evidence["validation_error"] == {
        "code": "ValueError", "message": failed["error_message"],
    }
    assert "result" not in failed
    assert verify_run(root, bank_root=BANK)["valid"] is True

    for mutation in ("finish", "header", "request", "message", "drop_evidence"):
        poisoned = deepcopy(failed)
        if mutation == "finish":
            poisoned["failure_evidence"]["raw_call"]["response"]["choices"][0][
                "finish_reason"
            ] = "tool_calls"
        elif mutation == "header":
            poisoned["failure_evidence"]["raw_call"]["response_headers"][
                "x_generation_id"
            ] = ["different-id"]
        elif mutation == "request":
            poisoned["failure_evidence"]["request"]["transport_body"][
                "max_completion_tokens"
            ] = 1
            poisoned["failure_evidence"]["request_sha256"] = contracts.sha256_value(
                poisoned["failure_evidence"]["request"]
            )
        elif mutation == "message":
            poisoned["failure_evidence"]["validation_error"]["message"] = "changed"
        else:
            poisoned["failure_evidence"] = None
        assert runner._validate_episode(poisoned) is False
        _assert_whole_root_semantic_rejection(
            tmp_path, root, failed_relative, poisoned, f"fork-{mutation}"
        )

    for mutation in ("message", "tool_constant", "stage_schema_hash"):
        poisoned = deepcopy(failed)
        request = poisoned["failure_evidence"]["request"]
        if mutation == "message":
            request["transport_body"]["messages"][0]["content"] += " altered"
        elif mutation == "tool_constant":
            request["transport_body"]["tools"][0]["function"]["parameters"][
                "oneOf"
            ][0]["properties"]["target"]["const"] += "-altered"
        else:
            request["stage_tool_schema_sha256"] = "f" * 64
        poisoned["failure_evidence"]["request_sha256"] = contracts.sha256_value(
            request
        )
        assert runner._validate_episode(poisoned) is False
        _assert_whole_root_semantic_rejection(
            tmp_path, root, failed_relative, poisoned, f"fork-rehash-{mutation}"
        )
    events = [row["event"] for row in runner.store.read_journal()]
    assert "phase_complete:canary" not in events
    assert runner._successful("episode", runner.manifest["canary_item_ids"]) == []
    with pytest.raises(ValueError, match="explicit retry"):
        runner.canary()


def test_followthrough_failure_preserves_and_replays_completed_fork_prefix(tmp_path):
    root = tmp_path / "follow-failure"
    runner = QualificationRunner.create(
        root, bank_root=BANK, client=TruncatedFollowOpenRouter(),
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    runner.access()
    with pytest.raises(RuntimeError, match="episode failed attempt 1"):
        runner.canary()
    item_id = runner.manifest["canary_item_ids"][0]
    failed_path = (
        root / "episodes" / "openai--gpt-5-nano" / item_id / "attempt-1.json"
    )
    failed_relative = failed_path.relative_to(root)
    failed = json.loads(failed_path.read_text())
    evidence = failed["failure_evidence"]
    assert evidence["failed_stage"] == "followthrough"
    assert [
        row["record"]["stage"] for row in evidence["completed_stages"]
    ] == ["fork"]
    assert runner._validate_episode(failed) is True
    assert verify_run(root, bank_root=BANK)["valid"] is True

    poisoned = deepcopy(failed)
    poisoned["failure_evidence"]["completed_stages"][0]["record"][
        "raw_call"
    ]["response"]["provider"] = "Other"
    assert runner._validate_episode(poisoned) is False
    _assert_whole_root_semantic_rejection(
        tmp_path, root, failed_relative, poisoned, "follow-prefix-raw"
    )

    for mutation in ("prior_observable", "selected_branch", "prefix_request"):
        poisoned = deepcopy(failed)
        if mutation == "prefix_request":
            record = poisoned["failure_evidence"]["completed_stages"][0]["record"]
            record["request"]["transport_body"]["messages"][0][
                "content"
            ] += " altered"
            record["request_sha256"] = contracts.sha256_value(record["request"])
        else:
            request = poisoned["failure_evidence"]["request"]
            if mutation == "prior_observable":
                for message in request["transport_body"]["messages"]:
                    if message.get("role") == "assistant" and (
                            "committed_tool_effect" in message.get("content", "")):
                        message["content"] += " altered"
                        break
                request["prior_observable_sha256"] = contracts.sha256_value(
                    [{"altered": True}]
                )
            else:
                interface = json.loads(
                    request["transport_body"]["messages"][1]["content"]
                )
                interface["selected_branch_state"]["tampered"] = True
                request["transport_body"]["messages"][1]["content"] = json.dumps(
                    interface, sort_keys=True, separators=(",", ":")
                )
            poisoned["failure_evidence"]["request_sha256"] = contracts.sha256_value(
                request
            )
        assert runner._validate_episode(poisoned) is False
        _assert_whole_root_semantic_rejection(
            tmp_path, root, failed_relative, poisoned, f"follow-{mutation}"
        )


def test_staged_transport_failure_preserves_canonical_request_and_absent_raw(
        tmp_path):
    root = tmp_path / "stage-transport"
    runner = QualificationRunner.create(
        root, bank_root=BANK, client=TransportForkOpenRouter(),
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    runner.access()
    with pytest.raises(RuntimeError, match="episode failed attempt 1"):
        runner.canary()
    item_id = runner.manifest["canary_item_ids"][0]
    failed_path = (
        root / "episodes" / "openai--gpt-5-nano" / item_id / "attempt-1.json"
    )
    failed = json.loads(failed_path.read_text())
    evidence = failed["failure_evidence"]
    assert evidence["failure_kind"] == "transport"
    assert evidence["raw_call"] is None
    assert evidence["request_sha256"] == contracts.sha256_value(evidence["request"])
    assert runner._validate_episode(failed) is True
    assert verify_run(root, bank_root=BANK)["valid"] is True
    poisoned = deepcopy(failed)
    poisoned["failure_evidence"]["request"]["transport_body"]["messages"][0][
        "content"
    ] += " altered"
    poisoned["failure_evidence"]["request_sha256"] = contracts.sha256_value(
        poisoned["failure_evidence"]["request"]
    )
    assert runner._validate_episode(poisoned) is False
    _assert_whole_root_semantic_rejection(
        tmp_path, root, failed_path.relative_to(root), poisoned,
        "stage-transport-rehashed-request",
    )


def test_cli_paid_commands_require_explicit_retry_flag_to_advance_failures():
    parser = cli._parser()
    for command in ("access", "canary", "smoke", "diagnose"):
        args = parser.parse_args([
            command, "--root", "/tmp/crossroads-audit",
            "--retry-failed",
        ])
        assert args.retry_failed is True


def test_create_preflights_complete_staged_contract_before_root_or_transport(
        tmp_path, monkeypatch):
    client = FakeOpenRouter()

    def reject_incomplete(_episode, _truth):
        raise ValueError("scripted incomplete branch schema")

    monkeypatch.setattr(executor, "tool_schema_sha256", reject_incomplete)
    root = tmp_path / "must-not-exist"
    with pytest.raises(ValueError, match="public staged tool contract incomplete"):
        QualificationRunner.create(
            root, bank_root=BANK, client=client,
            model_aliases=["openai/gpt-5-nano"],
            provenance=contracts.PROVENANCE_MOCK,
        )
    assert not root.exists()
    assert client.catalog_calls == []
    assert client.requests == []


def test_failed_attempt_replay_requires_exact_identity_binding_and_flags(tmp_path):
    runner = QualificationRunner.create(
        tmp_path / "run", bank_root=BANK, client=FakeOpenRouter(),
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    alias = "openai/gpt-5-nano"
    model = contracts.resolve_model(alias)
    access_request = runner._access_request(model, 1)
    scripted_error = RuntimeError("scripted failure")
    access = {
        "artifact_version": "crossroads-qualification-attempt-v2",
        "kind": "access", "status": "failed",
        "purpose": "public qualification",
        "provenance": contracts.PROVENANCE_MOCK,
        "measurement_ready": False,
        "public_qualification_evidence": True,
        "model_alias": alias, "item_id": None, "attempt": 1,
        "binding": access_request["binding"],
        "error_code": "RuntimeError", "error_message": "scripted failure",
        "failure_evidence": runner._access_failure_evidence(
            phase="catalog", request=access_request, error=scripted_error,
        ),
        "authorizes_private_execution": False,
        "authorizes_calibration": False, "authorizes_freeze": False,
    }
    assert runner._validate_access(access) is True
    access_mutations = (
        ("model_alias", "openai/gpt-5.4"),
        ("item_id", "CROSSROADS-0001"),
        ("attempt", 999),
        ("purpose", "measurement"),
        ("provenance", contracts.PROVENANCE_LIVE),
        ("public_qualification_evidence", False),
        ("authorizes_private_execution", True),
        ("binding", {"bank_sha256": "f" * 64}),
    )
    for field, value in access_mutations:
        poisoned = deepcopy(access); poisoned[field] = value
        assert runner._validate_access(poisoned) is False

    item_id = runner.manifest["public_item_ids"][0]
    episode = deepcopy(access)
    episode.update({
        "kind": "episode", "item_id": item_id,
        "binding": runner._request_binding(item_id),
        "failure_evidence": None,
    })
    assert runner._validate_episode(episode) is False
    for field, value in (
        ("model_alias", "openai/gpt-5.4"),
        ("item_id", "CROSSROADS-0001"),
        ("attempt", 0),
        ("purpose", "measurement"),
        ("provenance", contracts.PROVENANCE_LIVE),
        ("authorizes_freeze", True),
        ("binding", {"bank_sha256": "0" * 64}),
    ):
        poisoned = deepcopy(episode); poisoned[field] = value
        assert runner._validate_episode(poisoned) is False


def test_fork_only_diagnostic_is_explicit_and_never_qualifies(tmp_path):
    client = FakeOpenRouter()
    runner = QualificationRunner.create(
        tmp_path / "diag", bank_root=BANK, client=client,
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
        execution_mode="fork-only diagnostic",
    )
    runner.access(); report = runner.diagnose()
    assert report["execution_mode"] == "fork-only diagnostic"
    assert report["measurement_ready"] is False
    assert report["authorizes_calibration"] is False
    assert len(client.requests) == 1 + 30
    with pytest.raises(ValueError, match="path-only staged"):
        runner.canary()
    verify_run(tmp_path / "diag", bank_root=BANK, require_phase="diagnostic")


def test_semantic_replay_rejects_rehashed_classification_or_request_tamper(tmp_path):
    client = FakeOpenRouter()
    runner = QualificationRunner.create(
        tmp_path / "run", bank_root=BANK, client=client,
        model_aliases=["openai/gpt-5-nano"],
        provenance=contracts.PROVENANCE_MOCK,
    )
    runner.access(); runner.canary()
    artifact_path = next((tmp_path / "run" / "episodes").rglob("attempt-1.json"))
    artifact = json.loads(artifact_path.read_text())
    item_id = artifact["item_id"]
    public = {row["id"]: row for row in json.loads((BANK / "seeds_public.yaml").read_text())}
    truth = json.loads((BANK / "sidecar" / "ground_truth.json").read_text())
    model = contracts.resolve_model("openai/gpt-5-nano")
    binding = artifact["result"]["stages"][0]["request"]["binding"]
    executor.verify_episode_result(
        public[item_id], truth[item_id], model=model,
        result=artifact["result"], binding=binding,
    )
    poisoned = deepcopy(artifact["result"])
    poisoned["classification"]["path_id"] = "fabricated"
    with pytest.raises(ValueError, match="classification replay"):
        executor.verify_episode_result(
            public[item_id], truth[item_id], model=model,
            result=poisoned, binding=binding,
        )
    poisoned = deepcopy(artifact["result"])
    poisoned["stages"][0]["request"]["transport_body"]["messages"][0]["content"] += " drift"
    with pytest.raises(ValueError, match="request replay"):
        executor.verify_episode_result(
            public[item_id], truth[item_id], model=model,
            result=poisoned, binding=binding,
        )


def test_runner_rejects_flagship_alias_private_ids_and_live_mock_confusion(tmp_path):
    with pytest.raises(ValueError, match="cheap allowlist"):
        QualificationRunner.create(
            tmp_path / "run", bank_root=BANK, client=FakeOpenRouter(),
            model_aliases=["openai/gpt-5.4"], provenance=contracts.PROVENANCE_MOCK,
        )
    with pytest.raises(ValueError, match="provenance"):
        QualificationRunner.create(
            tmp_path / "run2", bank_root=BANK, client=FakeOpenRouter(),
            model_aliases=["openai/gpt-5-nano"], provenance="measurement",
        )
