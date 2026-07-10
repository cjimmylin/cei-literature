from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest


HARNESS = Path(__file__).resolve().parents[1]
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

import analysis  # noqa: E402


ACTORS = ("A01", "A02", "A03")
CUES = ("C0", "C1", "C2", "C3")
N_ITEMS = 10
MIXED_BASE_ITEMS = 13
MIXED_CUE_ITEMS = 5
PATH_QUALITY = {"Fi": 4.0, "Wj": 0.0, "CFT": 0.5, "mixed": 2.0, "other": 1.0}
CONTRACT_ROW_FIELDS = (
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


def _expected_rows(rows: list[dict]) -> list[dict]:
    return [{field: copy.deepcopy(row[field]) for field in CONTRACT_ROW_FIELDS} for row in rows]


def _analyze(
    rows: list[dict],
    *,
    expected_rows: list[dict] | None = None,
    **kwargs,
) -> dict:
    contract = analysis.freeze_expected_evaluation_contract(
        _expected_rows(rows if expected_rows is None else expected_rows),
        config_path=kwargs.get("config_path", analysis.DEFAULT_CONFIG),
        expected_config_sha256=kwargs.get("expected_config_sha256"),
    )
    return analysis.analyze_terminal_rows(
        rows,
        expected_evaluation_contract=contract,
        **kwargs,
    )


def _construct_fields(label: str) -> dict:
    if label in PATH_QUALITY:
        quality = PATH_QUALITY[label]
        return {
            "path_quality": quality,
            "rubric_score": quality,
            "judge_path_quality": {"J01": quality, "J02": quality},
            "judge_rubric_scores": {"J01": quality, "J02": quality},
        }
    return {
        "path_quality": None,
        "rubric_score": None,
        "judge_path_quality": None,
        "judge_rubric_scores": None,
    }


def _set_construct_outcome(row: dict, label: str, *, rubric_score: float | None = None) -> None:
    quality = PATH_QUALITY[label]
    rubric = quality if rubric_score is None else rubric_score
    row.update(
        {
            "final_label": label,
            "judge_labels": {"J01": label, "J02": label},
            "judge_disagreement": False,
            "path_quality": quality,
            "rubric_score": rubric,
            "judge_path_quality": {"J01": quality, "J02": quality},
            "judge_rubric_scores": {"J01": rubric, "J02": rubric},
        }
    )


def _set_null_fused_construct(row: dict) -> None:
    row.update(
        {
            "final_label": "no_fusion",
            "judge_labels": {"J01": "Fi", "J02": "Wj"},
            "judge_disagreement": True,
            "path_quality": None,
            "rubric_score": None,
            "judge_path_quality": {"J01": 4.0, "J02": 0.0},
            "judge_rubric_scores": {"J01": 4.0, "J02": 0.0},
        }
    )


def _assert_null_fused_secondary_unavailable(result: dict) -> None:
    for endpoint in ("path_quality", "rubric_score"):
        endpoint_result = result["secondary_endpoint_pairwise_effects"][endpoint]
        for summary in (
            endpoint_result["unconditional"][0],
            endpoint_result["task_correct_conditioned"][0],
        ):
            assert summary["available"] is False
            assert summary["effect"] is None
            assert summary["unavailable_reason"] == "NULL_FUSED_ENDPOINT"
            assert summary["expected_n_items"] == N_ITEMS


def _rows(label_for, *, headline_eligible: bool = True) -> list[dict]:
    rows = []
    for item_index in range(N_ITEMS):
        item_id = f"thorns-analysis-{item_index:03d}"
        for actor_index, actor_id in enumerate(ACTORS):
            for cue_arm in CUES:
                label = label_for(actor_id, item_index, cue_arm)
                for rollout in range(6):
                    arm_index = {"C0": 0, "C1": 1, "C2": 2}.get(cue_arm)
                    position = (
                        1
                        if cue_arm == "C3"
                        else ((arm_index - actor_index - item_index - rollout) % 3) + 1
                    )
                    rows.append(
                        {
                            "actor_id": actor_id,
                            "item_id": item_id,
                            "surface_id": f"{item_id}-{cue_arm}",
                            "cue_arm": cue_arm,
                            "task_arm": "null_control" if cue_arm == "C2" else "construct",
                            "rollout": rollout,
                            "task_correctness": "correct",
                            "final_label": label,
                            "judge_ids": ["J01", "J02"],
                            "judge_labels": {"J01": label, "J02": label},
                            "judge_disagreement": False,
                            "output_length": 120,
                            "headline_eligible": headline_eligible,
                            "phase": (
                                "locked-confirmation" if cue_arm == "C3" else "development"
                            ),
                            "schedule_position": position,
                            "targeted_cue_factors": ["registered-factor"],
                            **_construct_fields(label),
                        }
                    )
    return rows


def _non_null(label_for):
    def wrapped(actor_id: str, item_index: int, cue_arm: str) -> str:
        if cue_arm == "C2":
            return "foil_correct"
        return label_for(actor_id, item_index)

    return wrapped


def _discriminating_rows() -> list[dict]:
    def label(actor_id: str, item_index: int) -> str:
        if actor_id == "A01":
            return "Fi"
        if actor_id == "A02":
            return "Fi" if item_index < N_ITEMS // 2 else "Wj"
        return "Wj"

    return _rows(_non_null(label))


def _mixed_panel_rows(*, confirmation: str = "absent") -> list[dict]:
    """Build the registered 13-base/5-cue plus one exploratory live geometry.

    ``confirmation`` is one of ``absent``, ``complete``, or ``partial``.  The
    partial fixture omits exactly A03's C3 task arm for the final cue item.
    """

    if confirmation not in {"absent", "complete", "partial"}:
        raise ValueError("unsupported confirmation fixture")

    def construct_label(actor_id: str, item_index: int) -> str:
        if actor_id == "A01":
            return "Fi"
        if actor_id == "A02":
            return "Fi" if item_index % 2 == 0 else "Wj"
        return "Wj"

    def append_row(
        rows: list[dict],
        *,
        actor_id: str,
        item_id: str,
        item_index: int,
        cue_arm: str,
        headline_eligible: bool = True,
        phase: str | None = None,
    ) -> None:
        label = (
            "foil_correct"
            if cue_arm == "C2"
            else construct_label(actor_id, item_index)
        )
        resolved_phase = phase or (
            "locked-confirmation" if cue_arm == "C3" else "development"
        )
        actor_index = ACTORS.index(actor_id)
        is_scheduled_development = (
            resolved_phase == "development" and item_id.startswith("thorns-cue-")
        ) or not headline_eligible
        for rollout in range(6):
            arm_index = {"C0": 0, "C1": 1, "C2": 2}.get(cue_arm)
            position = (
                ((arm_index - actor_index - item_index - rollout) % 3) + 1
                if is_scheduled_development
                else 1
            )
            rows.append(
                {
                    "actor_id": actor_id,
                    "item_id": item_id,
                    "surface_id": f"{item_id}-{cue_arm}",
                    "cue_arm": cue_arm,
                    "task_arm": "null_control" if cue_arm == "C2" else "construct",
                    "rollout": rollout,
                    "task_correctness": "correct",
                    "final_label": label,
                    "judge_ids": ["J01", "J02"],
                    "judge_labels": {"J01": label, "J02": label},
                    "judge_disagreement": False,
                    "output_length": 120,
                    "headline_eligible": headline_eligible,
                    "phase": resolved_phase,
                    "schedule_position": position,
                    "targeted_cue_factors": (
                        ["registered-factor"] if is_scheduled_development or cue_arm == "C3" else []
                    ),
                    **_construct_fields(label),
                }
            )

    rows: list[dict] = []
    for item_index in range(MIXED_BASE_ITEMS):
        item_id = f"thorns-base-{item_index:03d}"
        for actor_id in ACTORS:
            append_row(
                rows,
                actor_id=actor_id,
                item_id=item_id,
                item_index=item_index,
                cue_arm="C0",
            )
            if confirmation in {"complete", "partial"}:
                append_row(
                    rows,
                    actor_id=actor_id,
                    item_id=item_id,
                    item_index=item_index,
                    cue_arm="C0",
                    phase="locked-confirmation",
                )

    for item_index in range(MIXED_CUE_ITEMS):
        item_id = f"thorns-cue-{item_index:03d}"
        for actor_id in ACTORS:
            arms = ["C0", "C1", "C2"]
            if confirmation in {"complete", "partial"}:
                arms.append("C3")
            for cue_arm in arms:
                if (
                    confirmation == "partial"
                    and item_index == MIXED_CUE_ITEMS - 1
                    and actor_id == "A03"
                    and cue_arm == "C3"
                ):
                    continue
                append_row(
                    rows,
                    actor_id=actor_id,
                    item_id=item_id,
                    item_index=item_index,
                    cue_arm=cue_arm,
                )

    # A complete paternalcrush cue geometry is diagnostic-only and must not
    # register as a headline cue item.
    for actor_id in ACTORS:
        for cue_arm in ("C0", "C1", "C2"):
            append_row(
                rows,
                actor_id=actor_id,
                item_id="thorns-paternalcrush-exploratory",
                item_index=0,
                cue_arm=cue_arm,
                headline_eligible=False,
            )
    return rows


def _complete_phase_panel() -> list[dict]:
    """Development C0/C1/C2 plus fresh locked C0-base/C3-cue evidence."""
    return _mixed_panel_rows(confirmation="complete")


def _pair(result: dict, actor_a: str, actor_b: str) -> dict:
    return next(
        effect
        for effect in result["pairwise_model_effects"]
        if effect["actor_a"] == actor_a and effect["actor_b"] == actor_b
    )


def test_locked_headline_contrast_uses_only_fresh_locked_rows():
    rows = _complete_phase_panel()
    for row in rows:
        if row["cue_arm"] == "C2":
            continue
        if row["phase"] == "development":
            _set_construct_outcome(row, "Wj")
        else:
            _set_construct_outcome(row, "Fi" if row["actor_id"] == "A01" else "Wj")

    result = _analyze(rows)
    effect = _pair(result, "A01", "A02")

    assert result["primary_analysis_phase"] == "locked-confirmation"
    assert result["coverage_diagnostics"]["confirmation_complete"] is True
    assert effect["analysis_phase"] == "locked-confirmation"
    assert effect["n_items"] == MIXED_BASE_ITEMS + MIXED_CUE_ITEMS
    assert effect["effect"] == 1.0
    assert result["development_pairwise_diagnostics"][0]["effect"] == 0.0
    assert result["verdict"] == "DISCRIMINATING"


def test_primary_and_secondary_pairwise_effects_are_unconditional_with_task_correct_sensitivities():
    rows = _rows(_non_null(lambda actor, _item: "Fi" if actor == "A01" else "Wj"))
    for row in rows:
        if row["cue_arm"] != "C2":
            _set_construct_outcome(
                row,
                "Fi" if row["actor_id"] == "A01" else "Wj",
                rubric_score=2.0 if row["actor_id"] == "A01" else 1.0,
            )
    failed = copy.deepcopy(
        next(
            row
            for row in rows
            if row["phase"] == "locked-confirmation"
            and row["actor_id"] == "A01"
            and row["item_id"] == "thorns-analysis-000"
        )
    )
    failed["rollout"] = 1
    failed["task_correctness"] = "incorrect"
    _set_construct_outcome(failed, "Wj", rubric_score=4.0)

    result = _analyze(rows + [failed])
    primary = _pair(result, "A01", "A02")
    path = result["secondary_endpoint_pairwise_effects"]["path_quality"]
    rubric = result["secondary_endpoint_pairwise_effects"]["rubric_score"]

    assert primary["effect"] == 0.95
    assert primary["task_correct_conditioned_sensitivity"]["effect"] == 1.0
    assert path["soei"] is None
    assert path["unconditional"][0]["effect"] == 3.8
    assert path["task_correct_conditioned"][0]["effect"] == 4.0
    assert rubric["soei"] == 0.3
    assert rubric["unconditional"][0]["effect"] == 1.1
    assert rubric["task_correct_conditioned"][0]["effect"] == 1.0
    assert result["inference_unit"] == "item"


def test_endpoint_saturation_uses_all_locked_scoreable_rows():
    rows = _rows(_non_null(lambda _actor, _item: "Fi"))
    for row in rows:
        if (
            row["phase"] == "locked-confirmation"
            and row["item_id"] in {"thorns-analysis-000", "thorns-analysis-001"}
        ):
            row["task_correctness"] = "incorrect"
            _set_construct_outcome(row, "Wj")

    result = _analyze(rows)

    assert result["task_success"]["all_actors_pass"] is True
    assert result["saturation"]["denominator_policy"] == (
        "all scoreable rows in the primary analysis phase; task correctness is not a filter"
    )
    assert result["saturation"]["by_actor"]["A01"][
        "top_endpoint_item_fraction"
    ] == 0.8
    assert result["saturation"]["classification"] == "NOT-SATURATED"


def test_all_indeterminate_c2_fails_with_explicit_false_positive_denominator():
    rows = _discriminating_rows()
    for row in rows:
        if row["cue_arm"] == "C2":
            row["final_label"] = "indeterminate"
            row["judge_labels"] = {"J01": "indeterminate", "J02": "indeterminate"}

    result = _analyze(rows)
    c2 = result["cue_diagnostics"]["c2_outcomes"]

    assert c2["overall_outcome_rates"] == {
        "foil_correct": 0.0,
        "target_action_false_positive": 0.0,
        "indeterminate": 1.0,
        "unresolved_or_refusal": 0.0,
    }
    assert c2["false_positive"]["rate"] is None
    assert c2["false_positive"]["denominator_outcomes"] == [
        "foil_correct",
        "target_action_false_positive",
    ]
    assert c2["false_positive"]["denominator_n_actor_items"] == 0
    assert c2["indeterminate"]["maximum_rate"] == 0.1
    assert c2["indeterminate"]["flag"] is True
    assert "NULL_INDETERMINATE" in result["invalid_reason_codes"]
    assert result["verdict"] == "INVALID"


def test_schedule_position_and_targeted_factors_are_retained_and_diagnosed():
    rows = _rows(
        _non_null(
            lambda actor, item: (
                "Fi" if actor == "A01" and item >= N_ITEMS // 2 else "Wj"
            )
        )
    )

    result = _analyze(rows)
    position = result["position_diagnostics"]

    assert position["estimand"] == "primary_label_score_by_schedule_position"
    assert position["analysis_phase"] == "locked-confirmation"
    assert position["observed_schedule_positions"] == list(range(1, N_ITEMS + 1))
    assert position["targeted_cue_factors"] == ["registered-factor"]
    assert position["by_actor"]["A01"]["primary_score_position_correlation"] > 0.8
    locked_cell = next(
        cell
        for cell in result["per_actor_item_rates"]
        if cell["phase"] == "locked-confirmation" and cell["actor_id"] == "A01"
    )
    assert locked_cell["schedule_positions"]
    assert locked_cell["targeted_cue_factors"] == ["registered-factor"]


def test_j01_and_j02_publish_complete_unfused_construct_contrasts():
    rows = _rows(_non_null(lambda _actor, _item: "Wj"))
    for row in rows:
        if row["phase"] != "locked-confirmation":
            continue
        j01 = "Fi" if row["actor_id"] == "A01" else "Wj"
        j02 = "Fi" if row["actor_id"] == "A02" else "Wj"
        row["judge_labels"] = {"J01": j01, "J02": j02}
        row["judge_path_quality"] = {
            "J01": PATH_QUALITY[j01],
            "J02": PATH_QUALITY[j02],
        }
        row["judge_rubric_scores"] = {
            "J01": PATH_QUALITY[j01],
            "J02": PATH_QUALITY[j02],
        }
        row["judge_disagreement"] = j01 != j02

    result = _analyze(rows)
    contrasts = result["judge_diagnostics"]["no_fusion_pairwise_model_contrasts"]

    assert contrasts["fusion_policy"].startswith("none")
    assert contrasts["complete_actor_pair_count"] == len(analysis.load_analysis_config()[0]["comparisons"])
    j01 = contrasts["by_judge"]["J01"]
    j02 = contrasts["by_judge"]["J02"]
    assert len(j01["label_score"]) == 3
    assert len(j02["label_score"]) == 3
    assert j01["label_score"][0]["effect"] == 1.0
    assert j02["label_score"][0]["effect"] == -1.0
    assert j01["path_quality"][0]["effect"] == 4.0
    assert j02["path_quality"][0]["effect"] == -4.0


def test_development_mixed_panel_is_complete_without_sealed_c3():
    result = _analyze(_mixed_panel_rows())

    coverage = result["coverage_diagnostics"]
    assert coverage["stage"] == "development"
    assert coverage["confirmation_status"] == "pending"
    assert coverage["confirmation_pending"] is True
    assert coverage["confirmation_complete"] is False
    assert coverage["base_item_count"] == MIXED_BASE_ITEMS
    assert coverage["registered_cue_item_count"] == MIXED_CUE_ITEMS
    assert coverage["missing_cell_count"] == 0
    assert coverage["primary_arm_by_role"] == {
        "base": "C0",
        "registered_cue": "C1",
    }
    assert "INCOMPLETE_COUNTERBALANCE" not in result["invalid_reason_codes"]
    assert result["verdict"] == "CONFIRMATION_PENDING"
    assert result["row_counts"]["headline_items"] == (
        MIXED_BASE_ITEMS + MIXED_CUE_ITEMS
    )
    assert result["row_counts"]["excluded_nonheadline"] == len(ACTORS) * 3
    assert result["task_success"]["by_actor"]["A01"]["n_items"] == (
        MIXED_BASE_ITEMS + MIXED_CUE_ITEMS
    )
    assert _pair(result, "A01", "A02")["n_items"] == (
        MIXED_BASE_ITEMS + MIXED_CUE_ITEMS
    )
    assert _pair(result, "A01", "A02")["analysis_phase"] == "development"
    assert _pair(result, "A01", "A02")["task_correct_conditioned_sensitivity"][
        "n_items"
    ] == MIXED_BASE_ITEMS + MIXED_CUE_ITEMS


def test_mixed_panel_coverage_policy_is_frozen_in_the_raw_config():
    config_path = HARNESS / "analysis_config.openrouter.json"
    expected = hashlib.sha256(config_path.read_bytes()).hexdigest()

    config, provenance = analysis.load_analysis_config(
        config_path, expected_sha256=expected
    )

    assert provenance["sha256"] == expected
    assert config["mixed_panel"] == {
        "cue_registration_rule": "ANY_HEADLINE_NON_C0_ARM",
        "base_primary_arm": "C0",
        "registered_cue_primary_arm": "C1",
        "development_required_cue_arms": ["C0", "C1", "C2"],
        "confirmation_arm": "C3",
        "confirmation_trigger": "ANY_LOCKED_PHASE_ROW",
    }


@pytest.mark.parametrize(
    ("threshold", "wrong_value"),
    [
        ("smallest_effect_of_interest", 0.2),
        ("rubric_score_smallest_effect_of_interest", 0.2),
        ("maximum_null_indeterminate_rate", 0.2),
    ],
)
def test_registered_analysis_threshold_values_are_validation_locked(
    tmp_path: Path, threshold: str, wrong_value: float
):
    config = json.loads((HARNESS / "analysis_config.openrouter.json").read_text())
    config["thresholds"][threshold] = wrong_value
    candidate = tmp_path / "analysis.json"
    candidate.write_text(json.dumps(config))
    expected = hashlib.sha256(candidate.read_bytes()).hexdigest()

    with pytest.raises(ValueError, match="frozen"):
        analysis.load_analysis_config(candidate, expected_sha256=expected)


def test_complete_c3_for_every_registered_cue_item_runs_sealed_confirmation():
    result = _analyze(
        _mixed_panel_rows(confirmation="complete")
    )

    coverage = result["coverage_diagnostics"]
    assert coverage["stage"] == "locked-confirmation"
    assert coverage["confirmation_status"] == "complete"
    assert coverage["confirmation_pending"] is False
    assert coverage["confirmation_complete"] is True
    assert coverage["missing_cell_count"] == 0
    assert "INCOMPLETE_COUNTERBALANCE" not in result["invalid_reason_codes"]
    effect = _pair(result, "A01", "A02")
    assert effect["n_items"] == MIXED_BASE_ITEMS + MIXED_CUE_ITEMS
    assert effect["analysis_phase"] == "locked-confirmation"
    assert effect["effect"] is not None
    assert effect["stable"] is True
    assert result["verdict"] == "DISCRIMINATING"


def test_partial_c3_latches_invalid_and_withholds_sealed_effects():
    result = _analyze(
        _mixed_panel_rows(confirmation="partial")
    )

    coverage = result["coverage_diagnostics"]
    assert coverage["stage"] == "locked-confirmation"
    assert coverage["confirmation_status"] == "incomplete"
    assert coverage["confirmation_pending"] is False
    assert coverage["confirmation_complete"] is False
    assert coverage["missing_cell_count"] == 1
    assert coverage["missing_cells"] == [
        {
            "phase": "locked-confirmation",
            "actor_id": "A03",
            "item_id": "thorns-cue-005",
            "cue_arm": "C3",
            "missing_task_arms": ["main"],
            "unexpected_task_arms": [],
        }
    ]
    assert result["verdict"] == "INVALID"
    assert "INCOMPLETE_COUNTERBALANCE" in result["invalid_reason_codes"]
    effect = _pair(result, "A01", "A02")
    assert effect["effect"] is None
    assert effect["n_items"] == 0


def test_missing_fresh_locked_base_cell_rejects_partial_confirmation():
    rows = _complete_phase_panel()
    rows.remove(
        next(
            row
            for row in rows
            if row["phase"] == "locked-confirmation"
            and row["cue_arm"] == "C0"
            and row["actor_id"] == "A03"
            and row["item_id"] == "thorns-base-012"
        )
    )

    result = _analyze(rows)

    assert result["coverage_diagnostics"]["confirmation_status"] == "incomplete"
    assert result["coverage_diagnostics"]["missing_confirmation_cell_count"] == 1
    assert "INCOMPLETE_COUNTERBALANCE" in result["invalid_reason_codes"]
    assert result["verdict"] == "INVALID"
    assert all(effect["effect"] is None for effect in result["pairwise_model_effects"])


def test_any_locked_phase_row_triggers_locked_headline_coverage():
    rows = _mixed_panel_rows()
    nonheadline_locked = copy.deepcopy(
        next(row for row in rows if not row["headline_eligible"])
    )
    nonheadline_locked["phase"] = "locked-confirmation"
    nonheadline_locked["rollout"] = 99

    result = _analyze(rows + [nonheadline_locked])

    assert result["primary_analysis_phase"] == "locked-confirmation"
    assert result["coverage_diagnostics"]["confirmation_status"] == "incomplete"
    assert result["verdict"] == "INVALID"
    assert all(effect["effect"] is None for effect in result["pairwise_model_effects"])


def test_all_actor_top_endpoints_are_saturated_high():
    result = _analyze(
        _rows(_non_null(lambda _actor, _item: "Fi"))
    )

    assert result["verdict"] == "SATURATED"
    assert result["saturation"]["classification"] == "SATURATED-HIGH"
    assert all(
        actor["endpoint_classification"] == "CEILING"
        for actor in result["saturation"]["by_actor"].values()
    )
    assert result["inference_unit"] == "item"
    assert _pair(result, "A01", "A02")["n_items"] == N_ITEMS


def test_all_actor_bottom_endpoints_are_saturated_low_after_task_success():
    result = _analyze(
        _rows(_non_null(lambda _actor, _item: "Wj"))
    )

    assert result["verdict"] == "SATURATED"
    assert result["saturation"]["classification"] == "SATURATED-LOW"
    assert result["task_success"]["all_actors_pass"] is True
    assert all(
        actor["endpoint_classification"] == "FLOOR"
        for actor in result["saturation"]["by_actor"].values()
    )


def test_common_surface_shift_with_no_stable_model_effect_is_cue_dominated_invalid():
    def label(_actor_id: str, item_index: int, cue_arm: str) -> str:
        if cue_arm == "C2":
            return "foil_correct"
        if cue_arm == "C0":
            return "Fi"
        return "Fi" if item_index < N_ITEMS // 2 else "Wj"

    result = _analyze(_rows(label))

    assert result["verdict"] == "INVALID"
    assert result["cue_diagnostics"]["cue_dominance"]["cue_dominant"] is True
    assert result["cue_diagnostics"]["cue_dominance"]["ratio"] is None
    assert "CUE_DOMINANCE" in result["invalid_reason_codes"]


def test_interior_equal_actor_rates_are_nondiscriminating():
    result = _analyze(
        _rows(
            _non_null(
                lambda _actor, item: "Fi" if item < N_ITEMS // 2 else "Wj"
            )
        )
    )

    assert result["verdict"] == "NONDISCRIMINATING"
    assert result["verdict_detail"] == "NO_STABLE_SOEI_EXCEEDING_CONTRAST"
    assert result["saturation"]["classification"] == "NOT-SATURATED"
    assert not any(effect["stable"] for effect in result["pairwise_model_effects"])


def test_synthetic_stable_pairwise_effect_meets_discrimination_rule():
    result = _analyze(_discriminating_rows())

    assert result["verdict"] == "DISCRIMINATING"
    assert result["verdict_detail"] == "AT_LEAST_ONE_STABLE_SOEI_EXCEEDING_CONTRAST"
    assert result["saturation"]["classification"] == "NOT-SATURATED"
    assert _pair(result, "A01", "A02")["effect"] > result["soei"]
    assert _pair(result, "A01", "A02")["cluster_bootstrap_ci"][0] > 0
    assert _pair(result, "A01", "A02")["bootstrap_unit"] == "item"
    assert _pair(result, "A01", "A02")["stable"] is True
    assert result["cue_diagnostics"]["rank_reversal"]["flag"] is False
    assert result["cue_diagnostics"]["null_false_positive"]["rate"] == 0.0
    assert result["judge_diagnostics"]["overall_disagreement_rate"] == 0.0
    assert result["judge_diagnostics"]["by_judge"]["J01"]["n_items"] == N_ITEMS
    assert result["length_diagnostics"]["by_actor"]["A01"]["mean_length"] == 120.0


def test_c2_null_controls_use_only_the_explicit_control_label_domain():
    rows = _discriminating_rows()
    for row in rows:
        if row["cue_arm"] == "C2":
            row["final_label"] = "foil_correct"
            row["judge_labels"] = {
                "J01": "foil_correct",
                "J02": "foil_correct",
            }

    result = _analyze(rows)

    assert result["verdict"] == "DISCRIMINATING"
    assert result["cue_diagnostics"]["null_false_positive"]["labels"] == [
        "target_action_false_positive"
    ]
    assert result["cue_diagnostics"]["null_false_positive"]["rate"] == 0.0
    c2_cell = next(
        cell for cell in result["per_actor_item_rates"] if cell["cue_arm"] == "C2"
    )
    assert set(c2_cell["unconditional"]["label_rates"]) == {
        "foil_correct",
        "target_action_false_positive",
        "indeterminate",
    }


@pytest.mark.parametrize(
    ("cue_arm", "wrong_label"),
    [("C2", "Fi"), ("C1", "foil_correct")],
)
def test_construct_and_control_label_domains_are_never_interchangeable(
    cue_arm: str, wrong_label: str
):
    rows = _discriminating_rows()
    target = next(row for row in rows if row["cue_arm"] == cue_arm)
    target["final_label"] = wrong_label
    target["judge_labels"] = {"J01": wrong_label, "J02": wrong_label}

    with pytest.raises(ValueError, match="label"):
        _analyze(rows)


def test_unresolved_headline_label_latches_invalid_instead_of_being_dropped():
    rows = _discriminating_rows()
    unresolved = next(
        row
        for row in rows
        if row["actor_id"] == "A02" and row["cue_arm"] == "C1"
    )
    unresolved["final_label"] = None

    result = _analyze(rows)

    assert result["verdict"] == "INVALID"
    assert result["row_counts"]["unresolved_headline"] == 1
    assert "UNRESOLVED_LABELS" in result["invalid_reason_codes"]


def test_unresolved_construct_judge_disagreement_has_a_construct_validity_latch():
    rows = _discriminating_rows()
    unresolved = next(
        row
        for row in rows
        if row["actor_id"] == "A02"
        and row["item_id"] == "thorns-analysis-000"
        and row["phase"] == "locked-confirmation"
    )
    unresolved["final_label"] = "no_fusion"
    unresolved["judge_labels"] = {"J01": "Fi", "J02": "Wj"}
    unresolved["path_quality"] = None
    unresolved["rubric_score"] = None
    unresolved["judge_path_quality"] = {"J01": 4.0, "J02": 0.0}
    unresolved["judge_rubric_scores"] = {"J01": 4.0, "J02": 0.0}
    unresolved["judge_disagreement"] = True

    result = _analyze(rows)

    assert result["verdict"] == "INVALID"
    assert result["row_counts"]["unresolved_construct_headline"] == 1
    assert "UNRESOLVED_CONSTRUCT_LABELS" in result["invalid_reason_codes"]
    for endpoint in ("path_quality", "rubric_score"):
        summary = result["secondary_endpoint_pairwise_effects"][endpoint][
            "unconditional"
        ][0]
        assert summary["available"] is False
        assert summary["effect"] is None
        assert summary["unavailable_reason"] == "NULL_FUSED_ENDPOINT"
    unfused = result["judge_diagnostics"]["no_fusion_pairwise_model_contrasts"]
    assert unfused["by_judge"]["J01"]["label_score"][0]["n_items"] == N_ITEMS
    assert unfused["by_judge"]["J02"]["label_score"][0]["n_items"] == N_ITEMS


def test_null_fused_duplicate_rollout_withholds_secondary_endpoint():
    rows = _discriminating_rows()
    duplicate = copy.deepcopy(
        next(
            row
            for row in rows
            if row["actor_id"] == "A02"
            and row["item_id"] == "thorns-analysis-000"
            and row["phase"] == "locked-confirmation"
        )
    )
    duplicate["rollout"] = 1
    _set_null_fused_construct(duplicate)

    result = _analyze(rows + [duplicate])

    _assert_null_fused_secondary_unavailable(result)
    assert "UNRESOLVED_CONSTRUCT_LABELS" in result["invalid_reason_codes"]


def test_null_fused_alternate_task_arm_withholds_secondary_endpoint():
    rows = _discriminating_rows()
    alternate_rows = []
    for row in rows:
        alternate = copy.deepcopy(row)
        alternate["task_arm"] = "alternate"
        if (
            alternate["actor_id"] == "A02"
            and alternate["item_id"] == "thorns-analysis-000"
            and alternate["phase"] == "locked-confirmation"
        ):
            _set_null_fused_construct(alternate)
        alternate_rows.append(alternate)

    result = _analyze(rows + alternate_rows)

    _assert_null_fused_secondary_unavailable(result)
    assert "UNRESOLVED_CONSTRUCT_LABELS" in result["invalid_reason_codes"]


def test_c2_rates_equal_weight_task_arms_after_within_cell_rollout_reduction():
    rows = _discriminating_rows()
    additions = []
    for row in rows:
        alternate = copy.deepcopy(row)
        alternate["task_arm"] = "alternate"
        if row["cue_arm"] == "C2":
            alternate["final_label"] = "target_action_false_positive"
            alternate["judge_labels"] = {
                "J01": "target_action_false_positive",
                "J02": "target_action_false_positive",
            }
            for rollout in range(1, 9):
                repeated_foil = copy.deepcopy(row)
                repeated_foil["rollout"] = rollout
                additions.append(repeated_foil)
        additions.append(alternate)

    result = _analyze(rows + additions)
    c2 = result["cue_diagnostics"]["c2_outcomes"]

    assert c2["overall_outcome_rates"]["foil_correct"] == 0.5
    assert c2["overall_outcome_rates"]["target_action_false_positive"] == 0.5
    assert c2["false_positive"]["rate"] == 0.5
    assert c2["false_positive"]["denominator_unit"] == (
        "actor/item after equal task-arm reduction"
    )
    assert c2["false_positive"]["denominator_n_actor_items"] == len(ACTORS) * N_ITEMS


def test_unresolved_c2_judge_disagreement_has_a_control_validity_latch():
    rows = _discriminating_rows()
    unresolved = next(
        row
        for row in rows
        if row["actor_id"] == "A02" and row["cue_arm"] == "C2"
    )
    unresolved["final_label"] = None
    unresolved["judge_labels"] = {
        "J01": "foil_correct",
        "J02": "target_action_false_positive",
    }
    unresolved["judge_disagreement"] = True

    result = _analyze(rows)

    assert result["verdict"] == "INVALID"
    assert result["row_counts"]["unresolved_control_headline"] == 1
    assert "UNRESOLVED_CONTROL_LABELS" in result["invalid_reason_codes"]


def test_agreed_indeterminate_is_an_explicit_resolved_c2_outcome():
    rows = _discriminating_rows()
    indeterminate = next(
        row
        for row in rows
        if row["actor_id"] == "A02" and row["cue_arm"] == "C2"
    )
    indeterminate["final_label"] = "indeterminate"
    indeterminate["judge_labels"] = {
        "J01": "indeterminate",
        "J02": "indeterminate",
    }

    result = _analyze(rows)

    assert result["verdict"] == "DISCRIMINATING"
    assert result["row_counts"]["unresolved_control_headline"] == 0
    assert "UNRESOLVED_CONTROL_LABELS" not in result["invalid_reason_codes"]


def test_soei_exceeding_effect_from_two_items_is_not_mistaken_for_stable_separation():
    def sparse_effect(actor_id: str, item_index: int) -> str:
        if actor_id == "A01" and item_index < 2:
            return "Fi"
        return "Wj"

    result = _analyze(_rows(_non_null(sparse_effect)))
    effect = _pair(result, "A01", "A02")

    assert effect["effect"] > result["soei"]
    assert effect["cluster_bootstrap_ci"][0] == 0.0
    assert effect["stable"] is False
    assert result["verdict"] == "NONDISCRIMINATING"


def test_exploratory_rows_are_reported_but_excluded_from_every_headline_result():
    baseline = _analyze(_discriminating_rows())
    exploratory = _rows(
        _non_null(lambda actor, _item: "Wj" if actor == "A01" else "Fi"),
        headline_eligible=False,
    )
    for row in exploratory:
        row["surface_id"] += "-exploratory"
    with_exploratory = _analyze(
        exploratory + _discriminating_rows()
    )

    assert with_exploratory["verdict"] == baseline["verdict"]
    assert with_exploratory["saturation"] == baseline["saturation"]
    assert with_exploratory["pairwise_model_effects"] == baseline[
        "pairwise_model_effects"
    ]
    assert with_exploratory["row_counts"]["excluded_nonheadline"] == len(
        exploratory
    )


def test_actor_specific_surface_substitution_latches_counterbalance_invalid():
    rows = _discriminating_rows()
    substituted = next(
        row
        for row in rows
        if row["actor_id"] == "A03"
        and row["item_id"] == "thorns-analysis-000"
        and row["cue_arm"] == "C1"
    )
    substituted["surface_id"] += "-actor-specific"

    result = _analyze(rows)

    assert result["verdict"] == "INVALID"
    assert "SURFACE_ASSIGNMENT_MISMATCH" in result["invalid_reason_codes"]


def test_rollout_duplication_does_not_manufacture_item_n_or_change_verdict():
    rows = _discriminating_rows()
    baseline = _analyze(rows)
    duplicates = []
    for row in rows:
        duplicate = copy.deepcopy(row)
        duplicate["rollout"] = 100
        duplicates.append(duplicate)

    duplicated = _analyze(rows + duplicates)

    assert duplicated["verdict"] == baseline["verdict"]
    assert _pair(duplicated, "A01", "A02")["n_items"] == N_ITEMS
    assert _pair(duplicated, "A01", "A02")["effect"] == _pair(
        baseline, "A01", "A02"
    )["effect"]
    assert duplicated["row_counts"]["headline"] == 2 * baseline["row_counts"][
        "headline"
    ]


def test_rates_are_unconditional_and_task_success_conditioned_per_actor_item():
    rows = _discriminating_rows()
    target = next(
        row
        for row in rows
        if row["actor_id"] == "A01"
        and row["item_id"] == "thorns-analysis-000"
        and row["cue_arm"] == "C1"
    )
    failed = copy.deepcopy(target)
    failed["rollout"] = 1
    failed["task_correctness"] = "incorrect"
    failed["final_label"] = "Wj"
    failed["judge_labels"] = {"J01": "Wj", "J02": "Wj"}

    result = _analyze(rows + [failed])
    rate = next(
        row
        for row in result["per_actor_item_rates"]
        if row["actor_id"] == "A01"
        and row["item_id"] == "thorns-analysis-000"
        and row["cue_arm"] == "C1"
    )

    assert rate["n_rollouts"] == 2
    assert rate["unconditional"]["label_rates"]["Fi"] == 0.5
    assert rate["task_success_conditioned"]["n_rollouts"] == 1
    assert rate["task_success_conditioned"]["label_rates"]["Fi"] == 1.0


def test_frozen_config_is_raw_byte_hash_bound_and_output_is_strict_json():
    config_path = HARNESS / "analysis_config.openrouter.json"
    expected = hashlib.sha256(config_path.read_bytes()).hexdigest()

    assert expected == analysis.FROZEN_ANALYSIS_CONFIG_SHA256
    frozen, frozen_provenance = analysis.load_analysis_config()
    assert frozen_provenance["sha256"] == analysis.FROZEN_ANALYSIS_CONFIG_SHA256
    assert frozen["thresholds"]["smallest_effect_of_interest"] == 0.1
    assert frozen["thresholds"]["rubric_score_smallest_effect_of_interest"] == 0.3
    assert frozen["thresholds"]["maximum_null_indeterminate_rate"] == 0.1

    result = _analyze(
        _discriminating_rows(), expected_config_sha256=expected
    )

    assert result["analysis_config"]["sha256"] == expected
    assert result["analysis_config"]["preregistration_id"].startswith(
        "THORNS-OPENROUTER-ANALYSIS"
    )
    assert json.loads(json.dumps(result, allow_nan=False))["verdict"] == (
        "DISCRIMINATING"
    )
