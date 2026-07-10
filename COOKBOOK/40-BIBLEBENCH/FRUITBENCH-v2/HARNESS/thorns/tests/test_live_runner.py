from __future__ import annotations

import hashlib
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
    assert len(by_role["calibration"]) == 18 * 4 * 24
    assert len(by_role["evaluation"]) == (13 * 3 * 6) + len(schedule.rows)
    assert len(by_role["held_out_frontier"]) == 18 * 2 * 6

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
    assert len(jobs) == 6 * 3 * 6
    assert {job.role for job in jobs} == {"evaluation"}
    assert {job.cue_arm for job in jobs} == {"C3"}
    assert all(job.sealed and job.mode == "construct" for job in jobs)


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
        return {
            "label": label,
            "headline_label": label,
            "task_correctness": "correct",
            "task_correctness_by_judge": {"J01": "correct", "J02": "correct"},
            "layer_e_disagreement": False,
            "disagreement": False,
            "judge_labels": {"J01": label, "J02": label},
            "raw_ballots": [
                {"judge_id": "J01", "layer_e": {"task_correctness": "correct"}},
                {"judge_id": "J02", "layer_e": {"task_correctness": "correct"}},
            ],
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
):
    return {
        "role": role,
        "actor_id": actor_id,
        "item_id": item_id,
        "fruit": fruit,
        "vice": vice,
        "tier": tier,
        "score": {"headline_label": label},
    }


def test_live_g2_uses_hard_fruit_vice_cells_instead_of_a_pooled_row_rate():
    rows = [
        _gate_row(
            role="calibration",
            item_id="item-a",
            label="CFT",
            fruit="F1",
            vice="W1",
        ),
        _gate_row(
            role="calibration",
            item_id="item-b",
            label="CFT",
            fruit="F2",
            vice="W2",
        ),
        _gate_row(
            role="held_out_frontier",
            item_id="item-a",
            label="Wj",
            fruit="F1",
            vice="W1",
            actor_id="H01",
        ),
        _gate_row(
            role="held_out_frontier",
            item_id="item-b",
            label="Fi",
            fruit="F2",
            vice="W2",
            actor_id="H01",
        ),
        _gate_row(
            role="held_out_frontier",
            item_id="floor-item",
            label="Wj",
            fruit="F9",
            vice="W9",
            tier="floor",
            actor_id="H01",
        ),
    ]

    gate = live_runner.compute_live_gates(rows)["G2_D21_transfer"]

    assert gate["value"] == pytest.approx(0.5)
    assert gate["threshold"] == pytest.approx(0.60)
    assert gate["pass"] is False
    assert gate["by_hard_cell"] == [
        {
            "fruit": "F1",
            "vice": "W1",
            "n": 1,
            "wj_take_rate": 1.0,
            "transfers": True,
        },
        {
            "fruit": "F2",
            "vice": "W2",
            "n": 1,
            "wj_take_rate": 0.0,
            "transfers": False,
        },
    ]


def test_live_g2_uses_strict_rate_and_inclusive_cell_fraction_boundaries():
    rows = []
    for index in range(5):
        fruit = f"F{index + 1}"
        vice = f"W{index + 1}"
        item_id = f"item-{index + 1}"
        rows.append(
            _gate_row(
                role="calibration",
                item_id=item_id,
                label="CFT",
                fruit=fruit,
                vice=vice,
            )
        )
        wj_count = (1, 2, 2, 2, 0)[index]
        rows.extend(
            _gate_row(
                role="held_out_frontier",
                item_id=item_id,
                label="Wj" if rollout < wj_count else "Fi",
                fruit=fruit,
                vice=vice,
                actor_id="H01",
            )
            for rollout in range(20)
        )

    gate = live_runner.compute_live_gates(rows)["G2_D21_transfer"]

    assert gate["by_hard_cell"][0]["wj_take_rate"] == pytest.approx(0.05)
    assert gate["by_hard_cell"][0]["transfers"] is False
    assert gate["value"] == pytest.approx(0.60)
    assert gate["pass"] is True


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
