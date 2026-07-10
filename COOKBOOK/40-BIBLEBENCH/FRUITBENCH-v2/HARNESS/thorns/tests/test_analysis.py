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
MIXED_CUE_ITEMS = 6


def _rows(label_for, *, headline_eligible: bool = True) -> list[dict]:
    rows = []
    for item_index in range(N_ITEMS):
        item_id = f"thorns-analysis-{item_index:03d}"
        for actor_id in ACTORS:
            for cue_arm in CUES:
                label = label_for(actor_id, item_index, cue_arm)
                rows.append(
                    {
                        "actor_id": actor_id,
                        "item_id": item_id,
                        "surface_id": f"{item_id}-{cue_arm}",
                        "cue_arm": cue_arm,
                        "task_arm": "main",
                        "rollout": 0,
                        "task_correctness": "correct",
                        "final_label": label,
                        "judge_ids": ["J01", "J02"],
                        "judge_labels": {"J01": label, "J02": label},
                        "judge_disagreement": False,
                        "output_length": 120,
                        "headline_eligible": headline_eligible,
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
    """Build the registered 13-base/6-cue live headline geometry.

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
    ) -> None:
        label = (
            "foil_correct"
            if cue_arm == "C2"
            else construct_label(actor_id, item_index)
        )
        rows.append(
            {
                "actor_id": actor_id,
                "item_id": item_id,
                "surface_id": f"{item_id}-{cue_arm}",
                "cue_arm": cue_arm,
                "task_arm": "main",
                "rollout": 0,
                "task_correctness": "correct",
                "final_label": label,
                "judge_ids": ["J01", "J02"],
                "judge_labels": {"J01": label, "J02": label},
                "judge_disagreement": False,
                "output_length": 120,
                "headline_eligible": headline_eligible,
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


def _pair(result: dict, actor_a: str, actor_b: str) -> dict:
    return next(
        effect
        for effect in result["pairwise_model_effects"]
        if effect["actor_a"] == actor_a and effect["actor_b"] == actor_b
    )


def test_development_mixed_panel_is_complete_without_sealed_c3():
    result = analysis.analyze_terminal_rows(_mixed_panel_rows())

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
    assert _pair(result, "A01", "A02")["confirmation_effect"] is None
    assert _pair(result, "A01", "A02")["confirmation_n_items"] == 0


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
        "confirmation_trigger": "ANY_HEADLINE_C3_ROW",
    }


def test_complete_c3_for_every_registered_cue_item_runs_sealed_confirmation():
    result = analysis.analyze_terminal_rows(
        _mixed_panel_rows(confirmation="complete")
    )

    coverage = result["coverage_diagnostics"]
    assert coverage["stage"] == "locked_confirmation"
    assert coverage["confirmation_status"] == "complete"
    assert coverage["confirmation_pending"] is False
    assert coverage["confirmation_complete"] is True
    assert coverage["missing_cell_count"] == 0
    assert "INCOMPLETE_COUNTERBALANCE" not in result["invalid_reason_codes"]
    effect = _pair(result, "A01", "A02")
    assert effect["n_items"] == MIXED_BASE_ITEMS + MIXED_CUE_ITEMS
    assert effect["confirmation_n_items"] == MIXED_CUE_ITEMS
    assert effect["confirmation_effect"] is not None
    assert effect["stable"] is True
    assert result["verdict"] == "DISCRIMINATING"


def test_partial_c3_latches_invalid_and_withholds_sealed_effects():
    result = analysis.analyze_terminal_rows(
        _mixed_panel_rows(confirmation="partial")
    )

    coverage = result["coverage_diagnostics"]
    assert coverage["stage"] == "locked_confirmation"
    assert coverage["confirmation_status"] == "incomplete"
    assert coverage["confirmation_pending"] is False
    assert coverage["confirmation_complete"] is False
    assert coverage["missing_cell_count"] == 1
    assert coverage["missing_cells"] == [
        {
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
    assert effect["confirmation_effect"] is None
    assert effect["confirmation_n_items"] == 0


def test_all_actor_top_endpoints_are_saturated_high():
    result = analysis.analyze_terminal_rows(
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
    result = analysis.analyze_terminal_rows(
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

    result = analysis.analyze_terminal_rows(_rows(label))

    assert result["verdict"] == "INVALID"
    assert result["cue_diagnostics"]["cue_dominance"]["cue_dominant"] is True
    assert result["cue_diagnostics"]["cue_dominance"]["ratio"] is None
    assert "CUE_DOMINANCE" in result["invalid_reason_codes"]


def test_interior_equal_actor_rates_are_nondiscriminating():
    result = analysis.analyze_terminal_rows(
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


def test_stable_heldout_pairwise_effect_is_genuinely_discriminating():
    result = analysis.analyze_terminal_rows(_discriminating_rows())

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

    result = analysis.analyze_terminal_rows(rows)

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
        analysis.analyze_terminal_rows(rows)


def test_unresolved_headline_label_latches_invalid_instead_of_being_dropped():
    rows = _discriminating_rows()
    unresolved = next(
        row
        for row in rows
        if row["actor_id"] == "A02" and row["cue_arm"] == "C1"
    )
    unresolved["final_label"] = None

    result = analysis.analyze_terminal_rows(rows)

    assert result["verdict"] == "INVALID"
    assert result["row_counts"]["unresolved_headline"] == 1
    assert "UNRESOLVED_LABELS" in result["invalid_reason_codes"]


def test_unresolved_construct_judge_disagreement_has_a_construct_validity_latch():
    rows = _discriminating_rows()
    unresolved = next(
        row
        for row in rows
        if row["actor_id"] == "A02" and row["cue_arm"] == "C1"
    )
    unresolved["final_label"] = "no_fusion"
    unresolved["judge_labels"] = {"J01": "Fi", "J02": "Wj"}
    unresolved["judge_disagreement"] = True

    result = analysis.analyze_terminal_rows(rows)

    assert result["verdict"] == "INVALID"
    assert result["row_counts"]["unresolved_construct_headline"] == 1
    assert "UNRESOLVED_CONSTRUCT_LABELS" in result["invalid_reason_codes"]


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

    result = analysis.analyze_terminal_rows(rows)

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

    result = analysis.analyze_terminal_rows(rows)

    assert result["verdict"] == "DISCRIMINATING"
    assert result["row_counts"]["unresolved_control_headline"] == 0
    assert "UNRESOLVED_CONTROL_LABELS" not in result["invalid_reason_codes"]


def test_soei_exceeding_effect_from_two_items_is_not_mistaken_for_stable_separation():
    def sparse_effect(actor_id: str, item_index: int) -> str:
        if actor_id == "A01" and item_index < 2:
            return "Fi"
        return "Wj"

    result = analysis.analyze_terminal_rows(_rows(_non_null(sparse_effect)))
    effect = _pair(result, "A01", "A02")

    assert effect["effect"] > result["soei"]
    assert effect["cluster_bootstrap_ci"][0] == 0.0
    assert effect["stable"] is False
    assert result["verdict"] == "NONDISCRIMINATING"


def test_exploratory_rows_are_reported_but_excluded_from_every_headline_result():
    baseline = analysis.analyze_terminal_rows(_discriminating_rows())
    exploratory = _rows(
        _non_null(lambda actor, _item: "Wj" if actor == "A01" else "Fi"),
        headline_eligible=False,
    )
    for row in exploratory:
        row["surface_id"] += "-exploratory"
    with_exploratory = analysis.analyze_terminal_rows(
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

    result = analysis.analyze_terminal_rows(rows)

    assert result["verdict"] == "INVALID"
    assert "SURFACE_ASSIGNMENT_MISMATCH" in result["invalid_reason_codes"]


def test_rollout_duplication_does_not_manufacture_item_n_or_change_verdict():
    rows = _discriminating_rows()
    baseline = analysis.analyze_terminal_rows(rows)
    duplicates = []
    for row in rows:
        duplicate = copy.deepcopy(row)
        duplicate["rollout"] = 100
        duplicates.append(duplicate)

    duplicated = analysis.analyze_terminal_rows(rows + duplicates)

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

    result = analysis.analyze_terminal_rows(rows + [failed])
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

    result = analysis.analyze_terminal_rows(
        _discriminating_rows(), expected_config_sha256=expected
    )

    assert result["analysis_config"]["sha256"] == expected
    assert result["analysis_config"]["preregistration_id"].startswith(
        "THORNS-OPENROUTER-ANALYSIS"
    )
    assert json.loads(json.dumps(result, allow_nan=False))["verdict"] == (
        "DISCRIMINATING"
    )
