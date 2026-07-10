from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
import hashlib
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

THORNS = Path(__file__).resolve().parents[1]
HARNESS = THORNS.parent
for path in (THORNS, HARNESS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import live_runner  # noqa: E402
import model_adapters  # noqa: E402
from live_journal import (  # noqa: E402
    LiveEvidenceJournal,
    ResumeRefusedError,
    RunIdentity,
    validate_journal,
)
from preflight import (  # noqa: E402
    compile_phase_schedule,
    load_openrouter_config,
    load_registered_cue_surfaces,
)


CONFIG = THORNS / "pilot_config.openrouter.json"


def test_development_jobs_execute_the_frozen_schedule_and_preserve_subject_parity():
    cfg = load_openrouter_config(CONFIG)
    surfaces = load_registered_cue_surfaces(cfg)
    schedule = compile_phase_schedule(cfg, "development", surfaces=surfaces)
    jobs = live_runner.compile_live_jobs(
        cfg, phase="development", schedule_rows=schedule.rows
    )

    by_role = {}
    for role in ("calibration", "evaluation", "held_out_frontier"):
        by_role[role] = [job for job in jobs if job.role == role]
    assert len(jobs) == 6_798
    assert len(by_role["calibration"]) == 60 * 4 * 24
    assert len(by_role["evaluation"]) == (13 * 3 * 6) + len(schedule.rows)
    assert len(by_role["held_out_frontier"]) == 40 * 2 * 6
    assert len({job.item_id for job in by_role["calibration"]}) == 60
    assert len({job.item_id for job in by_role["held_out_frontier"]}) == 40
    assert len(
        {
            (job.item["cell"]["fruit"], job.item["cell"]["vice"])
            for job in by_role["held_out_frontier"]
        }
    ) == 20
    assert {job.actor_id for job in by_role["calibration"]} == {
        "A04",
        "A05",
        "A06",
        "A07",
    }
    assert {job.actor_id for job in by_role["held_out_frontier"]} == {"A08", "A09"}
    assert {job.rollout for job in by_role["calibration"]} == set(range(24))
    assert {job.rollout for job in by_role["held_out_frontier"]} == set(range(6))
    actor_calls = sum(
        4 if job.item["format"] == "escalation_arc" else 1 for job in jobs
    )
    assert actor_calls == 13_278
    assert len(jobs) * 4 == 27_192

    subject_counts = {
        actor: sum(job.actor_id == actor for job in by_role["evaluation"])
        for actor in ("A01", "A02", "A03")
    }
    assert len(set(subject_counts.values())) == 1
    scheduled_ids = {row["assignment_id"] for row in schedule.rows}
    scheduled_jobs = [job for job in jobs if job.assignment_id in scheduled_ids]
    assert len(scheduled_jobs) == len(schedule.rows)
    assert {job.cue_arm for job in scheduled_jobs} == {"C0", "C1", "C2"}
    assert sum(job.mode == "null_control" for job in scheduled_jobs) == len(
        schedule.rows
    ) // 3
    assert all(job.prompt_text for job in scheduled_jobs)
    assert all(job.surface_id.endswith(f"-{job.cue_arm}") for job in scheduled_jobs)
    assert {job.phase for job in jobs} == {"development"}
    assert all(job.job_id.startswith("job-development-") for job in jobs)
    assert all(isinstance(job.targeted_cue_factors, tuple) for job in jobs)
    gate_contract = live_runner.compile_live_gate_contract(cfg)
    assert len(gate_contract["calibration"]["item_ids"]) == 60
    assert gate_contract["calibration"]["rollouts"] == 24
    assert len(gate_contract["held_out_frontier"]["items"]) == 40
    assert gate_contract["held_out_frontier"]["cell_count"] == 20
    assert gate_contract["held_out_frontier"]["rollouts"] == 6
    assert set(
        Counter(
            (row["fruit"], row["vice"])
            for row in gate_contract["held_out_frontier"]["items"]
        ).values()
    ) == {2}


def test_gate_contract_compiler_rejects_one_three_item_cell_imbalance(monkeypatch):
    cfg = load_openrouter_config(CONFIG)
    bank, gold = live_runner._load_bank(Path(cfg["paths"]["items"]))
    bank = deepcopy(bank)
    by_cell = defaultdict(list)
    for item_id, item in bank.items():
        if item.get("status") != "exploratory" and item.get("tier") in {"hard", "arc"}:
            by_cell[(item["cell"]["fruit"], item["cell"]["vice"])].append(item_id)
    source_cell, target_cell = sorted(by_cell)[:2]
    moved_item_id = sorted(by_cell[source_cell])[0]
    bank[moved_item_id]["cell"] = {"fruit": target_cell[0], "vice": target_cell[1]}
    monkeypatch.setattr(live_runner, "_load_bank", lambda _path: (bank, gold))

    with pytest.raises(ValueError, match="exactly two"):
        live_runner.compile_live_gate_contract(cfg)


def test_confirmation_jobs_are_c3_only_and_never_reuse_development_assignments():
    cfg = load_openrouter_config(CONFIG)
    surfaces = load_registered_cue_surfaces(cfg)
    development = compile_phase_schedule(cfg, "development", surfaces=surfaces)
    confirmation = compile_phase_schedule(
        cfg,
        "locked-confirmation",
        surfaces=surfaces,
        development_surface_ids={row["surface_id"] for row in development.rows},
        development_schedule_hashes={development.schedule_hash},
    )
    jobs = live_runner.compile_live_jobs(
        cfg, phase="locked-confirmation", schedule_rows=confirmation.rows
    )
    assert len(jobs) == 342
    assert {job.role for job in jobs} == {"evaluation"}
    assert {job.cue_arm for job in jobs} == {"C0", "C3"}
    c3_jobs = [job for job in jobs if job.cue_arm == "C3"]
    c0_jobs = [job for job in jobs if job.cue_arm == "C0"]
    assert len(c3_jobs) == 6 * 3 * 6
    assert len(c0_jobs) == 13 * 3 * 6
    assert all(job.item["format"] == "single_shot" for job in jobs)
    assert len(jobs) == 342  # actor calls
    assert len(jobs) * 4 == 1_368  # judge calls
    assert all(job.sealed and job.mode == "construct" for job in c3_jobs)
    assert all(not job.sealed and not job.targeted_cue_factors for job in c0_jobs)
    assert {job.phase for job in jobs} == {"locked-confirmation"}
    assert all(job.job_id.startswith("job-locked-confirmation-") for job in jobs)

    development_jobs = live_runner.compile_live_jobs(
        cfg, phase="development", schedule_rows=development.rows
    )
    development_headline_ids = {
        job.job_id
        for job in development_jobs
        if job.role == "evaluation" and job.headline_eligible
    }
    assert not development_headline_ids & {job.job_id for job in jobs}


class _Adapter(model_adapters.ModelAdapter):
    def __init__(self, actor_id="A01"):
        super().__init__(
            model_adapters.ModelSpec(
                name="fake",
                family="fake-family",
                vendor="fake-vendor",
                adapter="openrouter",
                role="evaluation",
                model_id="fake/model-v1",
                actor_id=actor_id,
            )
        )

    def generate_messages(self, messages, **kwargs):
        return {
            "text": "A complete response.",
            "response_id": "resp-1",
            "request_id": "req-1",
            "generation_id": "gen-1",
            "returned_model": "fake/model-v1",
            "usage": {"input_tokens": 10, "output_tokens": 4},
            "attempt_ledger": [{"attempt": 1, "status_code": 200}],
        }


class _Scorer:
    def __init__(self):
        self.construct_calls = []
        self.control_calls = []

    @staticmethod
    def _result(label):
        control = label == "foil_correct"
        return {
            "label": label,
            "headline_label": label,
            "task_correctness": "correct",
            "task_correctness_by_judge": {"J01": "correct", "J02": "correct"},
            "layer_e_disagreement": False,
            "disagreement": False,
            "judge_labels": {"J01": label, "J02": label},
            "raw_ballots": [
                {
                    "judge_id": judge_id,
                    "layer_e": {"task_correctness": "correct"},
                    **(
                        {"layer_control": {"final_label": label}}
                        if control
                        else {
                            "layer_r": {
                                "final_label": label,
                                "quality": 4.0,
                                "rubric_score": 3.0,
                            }
                        }
                    ),
                }
                for judge_id in ("J01", "J02")
            ],
            "quality": None if control else 4.0,
            "rubric_score": None if control else 3.0,
            "fusion_status": "validated_judge_agreement",
        }

    def score(self, response_text, gold, **kwargs):
        self.construct_calls.append((response_text, gold, kwargs))
        return self._result("Fi")

    def score_control(self, response_text, **kwargs):
        self.control_calls.append((response_text, kwargs))
        return self._result("foil_correct")


class _Journal:
    def __init__(self):
        self.events = []

    def record(self, event_type, payload):
        self.events.append((event_type, payload))


def _job(*, mode="construct"):
    contract = (
        {
            "paths": {
                "fruit": {"markers": ["complete response"]},
                "vice": {"markers": ["bad response"]},
                "cft": {"markers": ["counterfeit response"]},
            },
            "rubric_0_4": {
                0: "vice",
                1: "counterfeit",
                2: "partial",
                3: "nearly complete",
                4: "complete",
            },
            "integration_check": False,
        }
        if mode == "construct"
        else (
            {
                "rule_id": "N1",
                "control_label": "foil_correct",
                "observable_basis": "correct foil",
            },
            {
                "rule_id": "N2",
                "control_label": "target_action_false_positive",
                "observable_basis": "false positive",
            },
            {
                "rule_id": "N3",
                "control_label": "indeterminate",
                "observable_basis": "indeterminate",
            },
        )
    )
    return live_runner.LiveJob(
        job_id=f"job-{mode}",
        phase="development",
        role="evaluation",
        actor_id="A01",
        model_id="fake/model-v1",
        item_id="thorns-unit-001",
        rollout=0,
        assignment_id=f"asg-{mode}",
        position=1,
        surface_id=f"thorns-unit-001-{'C2' if mode == 'null_control' else 'C0'}",
        cue_arm="C2" if mode == "null_control" else "C0",
        task_arm=mode,
        mode=mode,
        prompt_text="Write a response.",
        item={
            "id": "thorns-unit-001",
            "cell": {"fruit": "F3", "vice": "W11"},
            "tier": "hard",
            "format": "single_shot",
            "prompt": "Write a response.",
        },
        scoring_contract=contract,
        headline_eligible=True,
        sealed=False,
        targeted_cue_factors=("registered-factor",),
    )


def test_live_execution_uses_full_actor_visible_context_typed_scoring_and_journal():
    scorer = _Scorer()
    journal = _Journal()
    result = live_runner.execute_live_jobs(
        [_job(), _job(mode="null_control")],
        adapters={"A01": _Adapter()},
        judge_scorer=scorer,
        journal=journal,
    )

    assert len(scorer.construct_calls) == len(scorer.control_calls) == 1
    observable = scorer.construct_calls[0][2]["observable_context"]
    assert observable["actor_visible_messages"] == [
        {"role": "user", "content": "Write a response."},
        {"role": "assistant", "content": "A complete response."},
    ]
    assert scorer.control_calls[0][1]["hidden_metadata"]["cue_arm"] == "C2"
    assert [row["final_label"] for row in result["analysis_rows"]] == [
        "Fi",
        "foil_correct",
    ]
    assert result["analysis_rows"][0] == {
        "actor_id": "A01",
        "item_id": "thorns-unit-001",
        "surface_id": "thorns-unit-001-C0",
        "cue_arm": "C0",
        "task_arm": "construct",
        "rollout": 0,
        "task_correctness": "correct",
        "final_label": "Fi",
        "judge_ids": ["J01", "J02"],
        "judge_disagreement": False,
        "judge_labels": {"J01": "Fi", "J02": "Fi"},
        "output_length": 3,
        "headline_eligible": True,
        "phase": "development",
        "path_quality": 4.0,
        "rubric_score": 3.0,
        "schedule_position": 1,
        "targeted_cue_factors": ["registered-factor"],
        "judge_path_quality": {"J01": 4.0, "J02": 4.0},
        "judge_rubric_scores": {"J01": 3.0, "J02": 3.0},
    }
    assert result["analysis_rows"][1]["path_quality"] is None
    assert result["analysis_rows"][1]["rubric_score"] is None
    assert result["analysis_rows"][1]["judge_path_quality"] is None
    assert result["analysis_rows"][1]["judge_rubric_scores"] is None
    assert {row["phase"] for row in result["terminal_rows"]} == {"development"}
    event_types = [event for event, _payload in journal.events]
    assert event_types == [
        "job_start",
        "trajectory_result",
        "score_result",
        "job_start",
        "trajectory_result",
        "score_result",
    ]
    assert all(row["score_mode"] != "marker" for row in result["terminal_rows"])
    assert {
        key: result["terminal_rows"][0][key]
        for key in ("fruit", "vice", "tier")
    } == {"fruit": "F3", "vice": "W11", "tier": "hard"}


def _gate_row(
    *,
    role: str,
    item_id: str,
    label: str,
    fruit: str,
    vice: str,
    tier: str = "hard",
    actor_id: str = "A04",
    rollout: int = 0,
):
    return {
        "role": role,
        "actor_id": actor_id,
        "item_id": item_id,
        "fruit": fruit,
        "vice": vice,
        "tier": tier,
        "phase": "development",
        "rollout": rollout,
        "score": {"headline_label": label},
    }


def _full_gate_fixture():
    calibration_items = [f"cal-{index:02d}" for index in range(60)]
    heldout_items = [
        {
            "item_id": f"hard-{cell:02d}-{within}",
            "fruit": f"F{cell + 1}",
            "vice": f"W{cell + 1}",
        }
        for cell in range(20)
        for within in range(2)
    ]
    contract = {
        "calibration": {
            "item_ids": calibration_items,
            "actor_ids": ["A04", "A05", "A06", "A07"],
            "attacker_actor_id": "A04",
            "rollouts": 24,
        },
        "held_out_frontier": {
            "items": heldout_items,
            "actor_ids": ["A08", "A09"],
            "rollouts": 6,
            "cell_count": 20,
        },
    }
    rows = []
    for item_index, item_id in enumerate(calibration_items):
        for actor_id in contract["calibration"]["actor_ids"]:
            for rollout in range(24):
                if actor_id == "A04":
                    label = "Wj" if rollout < 12 else "Fi"
                else:
                    label = "CFT" if rollout < 2 else "Fi"
                rows.append(
                    _gate_row(
                        role="calibration",
                        item_id=item_id,
                        label=label,
                        fruit=f"F{item_index % 20 + 1}",
                        vice=f"W{item_index % 20 + 1}",
                        actor_id=actor_id,
                        rollout=rollout,
                    )
                )
    for item in heldout_items:
        cell = int(item["fruit"][1:]) - 1
        for actor_id in contract["held_out_frontier"]["actor_ids"]:
            for rollout in range(6):
                # Exactly 12/20 cells transfer, and F1 sits exactly at 1/24 =
                # 4.17%, proving the strict >5% item-cell threshold.
                label = "Wj" if cell in range(1, 13) and rollout == 0 else "Fi"
                rows.append(
                    _gate_row(
                        role="held_out_frontier",
                        item_id=item["item_id"],
                        label=label,
                        fruit=item["fruit"],
                        vice=item["vice"],
                        actor_id=actor_id,
                        rollout=rollout,
                    )
                )
    return rows, contract


def test_live_gates_require_exact_contract_and_use_strict_cell_boundary():
    rows, contract = _full_gate_fixture()
    gates = live_runner.compute_live_gates(rows, expected_contract=contract)

    assert gates["status"] == "complete"
    assert gates["coverage"]["valid"] is True
    assert gates["G1_calibration_band"]["value"] == 1.0
    assert gates["G1_calibration_band"]["pass"] is True
    assert gates["G2_D21_transfer"]["value"] == pytest.approx(0.60)
    assert gates["G2_D21_transfer"]["pass"] is True
    assert gates["G2_D21_transfer"]["by_hard_cell"][0]["transfers"] is False
    assert gates["G3_D22_cft_liveness"]["pass"] is True


def test_live_gates_reject_one_three_item_cell_imbalance():
    rows, contract = _full_gate_fixture()
    moved_item = contract["held_out_frontier"]["items"][1]
    target_cell = contract["held_out_frontier"]["items"][2]
    moved_item["fruit"] = target_cell["fruit"]
    moved_item["vice"] = target_cell["vice"]
    for row in rows:
        if row["role"] == "held_out_frontier" and row["item_id"] == moved_item["item_id"]:
            row["fruit"] = target_cell["fruit"]
            row["vice"] = target_cell["vice"]

    with pytest.raises(ValueError, match="exactly two"):
        live_runner.compute_live_gates(rows, expected_contract=contract)


@pytest.mark.parametrize(
    "mutation",
    [
        lambda rows: rows.pop(0),
        lambda rows: rows.__setitem__(0, {**rows[0], "actor_id": "A05"}),
        lambda rows: rows.__setitem__(0, {**rows[0], "rollout": 23}),
        lambda rows: rows.__setitem__(-1, {**rows[-1], "item_id": "wrong-item"}),
        lambda rows: rows.__setitem__(-1, {**rows[-1], "fruit": "F99"}),
        lambda rows: rows.__setitem__(
            0, {**rows[0], "score": {"headline_label": "unknown"}}
        ),
        lambda rows: rows.__setitem__(0, {**rows[0], "score": None}),
    ],
)
def test_live_gates_fail_closed_on_any_partial_or_drifted_coverage(mutation):
    rows, contract = _full_gate_fixture()
    mutation(rows)

    gates = live_runner.compute_live_gates(rows, expected_contract=contract)

    assert gates["status"] == "invalid_coverage"
    assert gates["coverage"]["valid"] is False
    assert all(
        gate["pass"] is False
        for gate in (
            gates["G1_calibration_band"],
            gates["G2_D21_transfer"],
            gates["G3_D22_cft_liveness"],
        )
    )


class _BaseClient:
    def __init__(self):
        self.calls = []

    def responses(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            text="answer",
            response_id="r1",
            request_id="q1",
            generation_id="g1",
            returned_model=kwargs["expected_canonical_slug"],
            usage={"input_tokens": 1, "output_tokens": 1},
            attempt_ledger=(),
            router_metadata={},
            routing_headers={},
            raw={"id": "r1", "status": "completed", "output": []},
            incomplete_details=None,
            attempts=1,
            latency_ms=1.0,
            service_tier=kwargs["service_tier"],
        )


def test_journaled_openrouter_client_persists_request_before_result():
    journal = _Journal()
    base = _BaseClient()
    client = live_runner.JournaledOpenRouterClient(
        base, journal=journal, request_kind="actor"
    )
    client.bind_job("job-001")
    client.responses(
        model_id="fake/model",
        messages=[{"role": "user", "content": "hello"}],
        max_output_tokens=10,
        reasoning_effort="medium",
        provider_order=("fake",),
        expected_canonical_slug="fake/model-v1",
        service_tier="default",
    )
    assert [event for event, _ in journal.events] == ["actor_request", "actor_result"]
    assert journal.events[0][1]["job_id"] == "job-001"
    assert journal.events[1][1]["text"] == "answer"
    assert journal.events[1][1]["raw"] == {
        "id": "r1",
        "status": "completed",
        "output": [],
    }
    assert journal.events[1][1]["incomplete_details"] is None


def test_journaled_openrouter_error_preserves_safe_transport_evidence():
    from shared.openrouter_client import AttemptRecord, OpenRouterError

    class FailingClient:
        def responses(self, **_kwargs):
            raise OpenRouterError(
                "safe failure",
                error_type="provider_error",
                status_code=503,
                api_code="upstream_busy",
                response_id="resp-error",
                generation_id="gen-error",
                retryable=True,
                retry_after_seconds=1.5,
                attempts=2,
                raw={"error": {"code": "upstream_busy"}},
                incomplete_details={"reason": "provider_timeout"},
                attempt_ledger=(
                    AttemptRecord(
                        attempt=1,
                        status_code=503,
                        error_type="provider_error",
                        response_id="resp-error",
                        request_id="req-error",
                        generation_id="gen-error",
                        router_metadata={},
                        latency_ms=7.0,
                    ),
                ),
            )

    journal = _Journal()
    client = live_runner.JournaledOpenRouterClient(
        FailingClient(), journal=journal, request_kind="actor"
    )
    client.bind_job("job-error")
    with pytest.raises(OpenRouterError):
        client.responses(messages=[{"role": "user", "content": "hello"}])

    event_type, payload = journal.events[-1]
    assert event_type == "actor_error"
    assert payload["status_code"] == 503
    assert payload["api_code"] == "upstream_busy"
    assert payload["error_type"] == "provider_error"
    assert payload["retryable"] is True
    assert payload["retry_after_seconds"] == 1.5
    assert payload["attempts"] == 2
    assert payload["raw"] == {"error": {"code": "upstream_busy"}}
    assert payload["incomplete_details"] == {"reason": "provider_timeout"}
    assert payload["attempt_ledger"][0]["request_id"] == "req-error"


def _identity():
    return RunIdentity(
        run_id="resume-test",
        config_sha256="a" * 64,
        source_sha256="b" * 64,
        schedule_sha256="c" * 64,
        receipt_sha256="d" * 64,
    )


def test_resume_recovers_only_complete_score_boundaries_and_rejects_ambiguous_calls(
    tmp_path: Path,
):
    first_job = _job()
    journal_path = tmp_path / "complete.jsonl"
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=[tmp_path / "out.json"],
        identity=_identity(),
        resumable=True,
    )
    journal.record("job_start", {"job_id": first_job.job_id})
    journal.record("actor_request", {"job_id": first_job.job_id, "call_id": "c1"})
    journal.record(
        "actor_result", {"job_id": first_job.job_id, "call_id": "c1"}
    )
    journal.record(
        "trajectory_result",
        {
            "job_id": first_job.job_id,
            "turn_rows": [{"turn": 1}],
            "terminal_row": {"status": "completed"},
        },
    )
    journal.record(
        "score_result",
        {
            "job_id": first_job.job_id,
            "terminal_row": {
                "job_id": first_job.job_id,
                "role": "evaluation",
                "analysis_row": {"final_label": "Fi"},
            },
            "analysis_row": {"final_label": "Fi"},
        },
    )
    journal.close()
    recovered = live_runner.recover_resumable_jobs(
        validate_journal(journal_path), [first_job]
    )
    assert recovered["completed_job_ids"] == {first_job.job_id}
    assert recovered["analysis_rows"] == [{"final_label": "Fi"}]

    partial_path = tmp_path / "partial.jsonl"
    partial = LiveEvidenceJournal.create(
        partial_path,
        output_paths=[tmp_path / "partial-out.json"],
        identity=_identity(),
        resumable=True,
    )
    partial.record("job_start", {"job_id": first_job.job_id})
    partial.record(
        "actor_request", {"job_id": first_job.job_id, "call_id": "dangling"}
    )
    partial.close()
    with pytest.raises(ResumeRefusedError, match="no durable result"):
        live_runner.recover_resumable_jobs(
            validate_journal(partial_path), [first_job]
        )


def test_confirmation_binds_prior_terminal_journal_to_supplied_development_schedule(
    tmp_path: Path,
):
    matching = tmp_path / "development-a.json"
    different = tmp_path / "development-b.json"
    matching.write_bytes(b'{"schedule":"a"}\n')
    different.write_bytes(b'{"schedule":"b"}\n')
    prior = {
        "journal_identity": {
            "schedule_sha256": hashlib.sha256(matching.read_bytes()).hexdigest()
        }
    }

    assert live_runner.validate_prior_development_schedule_binding(
        prior, [different, matching]
    ) == str(matching.resolve())
    with pytest.raises(ValueError, match="same journaled development run"):
        live_runner.validate_prior_development_schedule_binding(prior, [different])


def _completed_development_artifact(
    tmp_path: Path,
    *,
    artifact_overrides=None,
):
    terminal_path = tmp_path / "development-terminal.json"
    journal_path = tmp_path / "development-journal.jsonl"
    bindings = {
        "config_sha256": "a" * 64,
        "source_scope_sha256": "b" * 64,
        "gate_input_sha256": {"items": "c" * 64, "analysis": "d" * 64},
        "receipt_sha256": "e" * 64,
        "schedule_sha256": "f" * 64,
    }
    identity = RunIdentity(
        run_id="development-binding",
        config_sha256=bindings["config_sha256"],
        source_sha256=live_runner._canonical_hash(
            {
                "source_scope_sha256": bindings["source_scope_sha256"],
                "gate_input_sha256": bindings["gate_input_sha256"],
                "prior_development_sha256": None,
            }
        ),
        schedule_sha256=bindings["schedule_sha256"],
        receipt_sha256=bindings["receipt_sha256"],
    )
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=[terminal_path],
        identity=identity,
        resumable=True,
    )
    artifact = {
        "schema_version": "1.0",
        "kind": "thorns-live-terminal-rows",
        "phase": "development",
        "date_token": "20990101d",
        "journal_path": str(journal_path.resolve()),
        **bindings,
        "rows": [],
    }
    artifact.update(artifact_overrides or {})
    terminal_path.write_text(json.dumps(artifact, sort_keys=True) + "\n")
    journal.complete(
        {
            "status": "complete",
            "output_sha256": {
                str(terminal_path.resolve()): hashlib.sha256(
                    terminal_path.read_bytes()
                ).hexdigest()
            },
        }
    )
    journal.close()
    return terminal_path, bindings


def test_prior_development_loader_verifies_and_exposes_all_provenance_bindings(
    tmp_path: Path,
):
    terminal_path, bindings = _completed_development_artifact(tmp_path)

    loaded = live_runner.load_prior_development_evidence(terminal_path)

    assert loaded["bindings"] == bindings
    assert loaded["journal_identity"]["config_sha256"] == bindings["config_sha256"]


@pytest.mark.parametrize(
    ("field", "mutated"),
    [
        ("config_sha256", "0" * 64),
        ("source_scope_sha256", "1" * 64),
        ("gate_input_sha256", {"items": "2" * 64}),
        ("receipt_sha256", "3" * 64),
        ("schedule_sha256", "4" * 64),
    ],
)
def test_prior_development_loader_rejects_each_unbound_field(
    tmp_path: Path, field, mutated
):
    terminal_path, _bindings = _completed_development_artifact(
        tmp_path, artifact_overrides={field: mutated}
    )

    with pytest.raises(ValueError, match="binding"):
        live_runner.load_prior_development_evidence(terminal_path)


@pytest.mark.parametrize(
    "field",
    ["config_sha256", "source_scope_sha256", "gate_input_sha256", "schedule_sha256"],
)
def test_confirmation_provenance_mismatch_is_rejected_before_any_call(
    tmp_path: Path, field
):
    schedule = tmp_path / "development-schedule.json"
    schedule.write_bytes(b'{"development":true}\n')
    schedule_sha256 = hashlib.sha256(schedule.read_bytes()).hexdigest()
    bindings = {
        "config_sha256": "a" * 64,
        "source_scope_sha256": "b" * 64,
        "gate_input_sha256": {"items": "c" * 64},
        "receipt_sha256": "d" * 64,
        "schedule_sha256": schedule_sha256,
    }
    prior = {
        "sha256": "e" * 64,
        "bindings": deepcopy(bindings),
        "matched_schedule_path": str(schedule),
    }
    cfg = {"_provenance": {"config_sha256": bindings["config_sha256"]}}
    receipt = {
        "config_sha256": bindings["config_sha256"],
        "source_scope_sha256": bindings["source_scope_sha256"],
        "gate_input_sha256": deepcopy(bindings["gate_input_sha256"]),
        "_receipt_sha256": "f" * 64,
    }
    if field == "config_sha256":
        cfg["_provenance"]["config_sha256"] = "0" * 64
    elif field == "source_scope_sha256":
        receipt[field] = "0" * 64
    elif field == "gate_input_sha256":
        receipt[field] = {"items": "0" * 64}
    else:
        prior["bindings"][field] = "0" * 64

    calls = []
    with pytest.raises(ValueError, match="provenance|schedule|config|source|gate"):
        live_runner.validate_confirmation_provenance(
            prior,
            cfg=cfg,
            receipt=receipt,
            matched_schedule_path=schedule,
        )
        calls.append("external")
    assert calls == []
