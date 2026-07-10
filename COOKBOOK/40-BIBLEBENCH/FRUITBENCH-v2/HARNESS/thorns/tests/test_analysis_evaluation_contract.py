from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest


THORNS = Path(__file__).resolve().parents[1]
HARNESS = THORNS.parent
for path in (THORNS, HARNESS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import analysis  # noqa: E402
import live_runner  # noqa: E402
from preflight import (  # noqa: E402
    compile_phase_schedule,
    load_openrouter_config,
    load_registered_cue_surfaces,
)


CONFIG = THORNS / "pilot_config.openrouter.json"
ACTORS = ("A01", "A02", "A03")
CONTRACT_FIELDS = (
    "phase",
    "actor_id",
    "item_id",
    "surface_id",
    "cue_arm",
    "task_arm",
    "rollout",
    "schedule_position",
    "headline_eligible",
    "targeted_cue_factors",
)


def _contract_rows(rows: list[dict]) -> list[dict]:
    return [{field: copy.deepcopy(row[field]) for field in CONTRACT_FIELDS} for row in rows]


def _terminal_row(
    *,
    phase: str,
    actor_id: str,
    item_id: str,
    cue_arm: str,
    rollout: int,
    position: int,
    factor: str,
    final_label: str,
    headline_eligible: bool = True,
) -> dict:
    is_control = cue_arm == "C2"
    task_arm = "null_control" if is_control else "construct"
    score = {"Fi": 4.0, "Wj": 0.0}.get(final_label)
    return {
        "phase": phase,
        "actor_id": actor_id,
        "item_id": item_id,
        "surface_id": f"{item_id}-{cue_arm}",
        "cue_arm": cue_arm,
        "task_arm": task_arm,
        "rollout": rollout,
        "schedule_position": position,
        "headline_eligible": headline_eligible,
        "targeted_cue_factors": [factor],
        "task_correctness": "correct",
        "final_label": final_label,
        "judge_ids": ["J01", "J02"],
        "judge_labels": {"J01": final_label, "J02": final_label},
        "judge_disagreement": False,
        "output_length": 120,
        "path_quality": None if is_control else score,
        "rubric_score": None if is_control else score,
        "judge_path_quality": None if is_control else {"J01": score, "J02": score},
        "judge_rubric_scores": None if is_control else {"J01": score, "J02": score},
    }


def _realistic_complete_rows() -> list[dict]:
    rows: list[dict] = []
    for item_index in range(8):
        item_id = f"contract-cue-{item_index:02d}"
        factor = "factor-red" if item_index < 4 else "factor-blue"
        for actor_index, actor_id in enumerate(ACTORS):
            for rollout in range(6):
                for arm_index, cue_arm in enumerate(("C0", "C1", "C2")):
                    position = ((arm_index - actor_index - item_index - rollout) % 3) + 1
                    if cue_arm == "C2":
                        label = "foil_correct"
                    elif cue_arm == "C0" and factor == "factor-red":
                        label = "Fi"
                    elif cue_arm == "C1" and factor == "factor-red" and position == 1:
                        label = "Fi"
                    else:
                        label = "Wj"
                    rows.append(
                        _terminal_row(
                            phase="development",
                            actor_id=actor_id,
                            item_id=item_id,
                            cue_arm=cue_arm,
                            rollout=rollout,
                            position=position,
                            factor=factor,
                            final_label=label,
                        )
                    )
                rows.append(
                    _terminal_row(
                        phase="locked-confirmation",
                        actor_id=actor_id,
                        item_id=item_id,
                        cue_arm="C3",
                        rollout=rollout,
                        position=1,
                        factor=factor,
                        final_label="Fi" if actor_id == "A01" else "Wj",
                    )
                )
    return rows


def _contract(rows: list[dict]) -> dict:
    return analysis.freeze_expected_evaluation_contract(_contract_rows(rows))


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "extra"])
def test_empirical_verdict_requires_exact_compiled_rollout_identities(mutation: str):
    expected_rows = _realistic_complete_rows()
    actual_rows = copy.deepcopy(expected_rows)
    if mutation == "missing":
        actual_rows.pop()
    elif mutation == "duplicate":
        actual_rows.append(copy.deepcopy(actual_rows[-1]))
    else:
        extra = copy.deepcopy(actual_rows[-1])
        extra["rollout"] = 6
        actual_rows.append(extra)

    result = analysis.analyze_terminal_rows(
        actual_rows,
        expected_evaluation_contract=_contract(expected_rows),
    )

    diagnostics = result["evaluation_contract_diagnostics"]
    assert diagnostics["complete"] is False
    assert diagnostics[f"{mutation}_row_count"] == 1
    assert "EVALUATION_CONTRACT_MISMATCH" in result["invalid_reason_codes"]
    assert result["verdict"] == "INVALID"
    assert all(effect["effect"] is None for effect in result["pairwise_model_effects"])


def test_frozen_expected_contract_rejects_incomplete_duplicate_and_wrong_mode_plans():
    rows = _realistic_complete_rows()
    incomplete = _contract_rows(rows[:-1])
    duplicate = _contract_rows(rows) + [_contract_rows(rows)[-1]]
    wrong_mode = _contract_rows(rows)
    c2 = next(row for row in wrong_mode if row["cue_arm"] == "C2")
    c2["task_arm"] = "construct"

    with pytest.raises(ValueError, match="rollout IDs"):
        analysis.freeze_expected_evaluation_contract(incomplete)
    with pytest.raises(ValueError, match="duplicate expected evaluation identity"):
        analysis.freeze_expected_evaluation_contract(duplicate)
    with pytest.raises(ValueError, match="task mode"):
        analysis.freeze_expected_evaluation_contract(wrong_mode)


def test_real_compiler_geometry_is_arm_mode_aware_and_complete():
    cfg = load_openrouter_config(CONFIG)
    surfaces = load_registered_cue_surfaces(cfg)
    schedule = compile_phase_schedule(cfg, "development", surfaces=surfaces)
    jobs = [
        job
        for job in live_runner.compile_live_jobs(
            cfg, phase="development", schedule_rows=schedule.rows
        )
        if job.role == "evaluation"
    ]
    contract_rows = [
        {
            "phase": job.phase,
            "actor_id": job.actor_id,
            "item_id": job.item_id,
            "surface_id": job.surface_id,
            "cue_arm": job.cue_arm,
            "task_arm": job.task_arm,
            "rollout": job.rollout,
            "schedule_position": job.position,
            "headline_eligible": job.headline_eligible,
            "targeted_cue_factors": list(job.targeted_cue_factors),
        }
        for job in jobs
    ]
    rows = []
    for job, identity in zip(jobs, contract_rows):
        label = (
            "foil_correct"
            if job.cue_arm == "C2"
            else "Fi"
            if job.actor_id == "A01"
            else "Wj"
        )
        score = {"Fi": 4.0, "Wj": 0.0}.get(label)
        rows.append(
            {
                **identity,
                "task_correctness": "correct",
                "final_label": label,
                "judge_ids": ["J01", "J02"],
                "judge_labels": {"J01": label, "J02": label},
                "judge_disagreement": False,
                "output_length": 120,
                "path_quality": score,
                "rubric_score": score,
                "judge_path_quality": (
                    None if score is None else {"J01": score, "J02": score}
                ),
                "judge_rubric_scores": (
                    None if score is None else {"J01": score, "J02": score}
                ),
            }
        )

    result = analysis.analyze_terminal_rows(
        rows,
        expected_evaluation_contract=analysis.freeze_expected_evaluation_contract(
            contract_rows
        ),
    )

    assert len(jobs) == 558
    assert result["evaluation_contract_diagnostics"]["complete"] is True
    assert result["coverage_diagnostics"]["missing_cell_count"] == 0
    assert result["coverage_diagnostics"]["expected_task_arm_by_cue_arm"] == {
        "C0": "construct",
        "C1": "construct",
        "C2": "null_control",
    }
    assert "INCOMPLETE_COUNTERBALANCE" not in result["invalid_reason_codes"]


def test_position_diagnostics_are_within_item_and_locked_position_is_unavailable():
    rows = _realistic_complete_rows()
    result = analysis.analyze_terminal_rows(
        rows,
        expected_evaluation_contract=_contract(rows),
    )

    position = result["position_diagnostics"]
    development = position["development_construct"]
    assert development["available"] is True
    assert development["observed_schedule_positions"] == [1, 2, 3]
    assert development["unit"] == "actor/item/cue-arm after within-position rollout reduction"
    assert {
        (contrast["position_a"], contrast["position_b"])
        for contrast in development["within_item_position_contrasts"]
    } == {(1, 2), (1, 3), (2, 3)}
    assert position["locked_confirmation"] == {
        "analysis_phase": "locked-confirmation",
        "available": False,
        "unavailable_reason": "INVARIANT_SCHEDULE_POSITION",
        "observed_schedule_positions": [1],
    }

    factor = result["cue_diagnostics"]["c0_minus_c1"]["by_registered_factor"]
    assert factor["factor-red"]["n_items"] == 4
    assert factor["factor-red"]["by_actor"]["A01"]["effect_c0_minus_c1"] == pytest.approx(2 / 3)
    assert factor["factor-blue"]["by_actor"]["A01"]["effect_c0_minus_c1"] == 0.0
    assert result["cue_diagnostics"]["c0_minus_c1"]["factor_membership_policy"].startswith(
        "each item contributes"
    )
