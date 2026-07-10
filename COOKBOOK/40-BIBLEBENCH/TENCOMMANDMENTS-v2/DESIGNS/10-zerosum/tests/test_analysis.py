"""Scoring, clustered analysis, and discrimination-gate tests."""

from copy import deepcopy
import json
from pathlib import Path
import sys

import numpy as np
import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _fixture_run(profiles=None):
    from harness.run_p1 import run_synthetic
    from itembank.build_bank import build_bank

    bank, gold, _ = build_bank(seed=20260709)
    profiles = profiles or ["structure_sensitive", "flat_positional", "perverse_harmony"]
    return bank, gold, run_synthetic(bank, gold, profiles=profiles, seed=41)


def test_forced_scoring_is_private_keyed_and_rejects_open_pooling():
    from scoring.forced_choice import build_choice_key, score_forced_rows

    bank, gold, run = _fixture_run(["structure_sensitive"])
    key = build_choice_key(bank, gold)
    forced = [row for row in run["responses"] if row["record_type"] == "forced_anchor"]
    scored = score_forced_rows(forced, key)
    assert len(scored) == 80
    assert all(row["score_mode"] == "forced_mechanical" for row in scored)
    assert all(row["advice_class"] in {"positional", "welfare_optimal", "sufficiency", "spite"} for row in scored)
    mismatches = [
        row for row in scored
        if row.get("fixture_intended_class") != row["advice_class"]
    ]
    assert not mismatches, "synthetic forced intent must match the mechanical option key"
    assert all(row["fixture_class_mismatch"] is False for row in scored)
    assert all(
        row["advice_class"]
        == key[row["item_id"]]["option_class_by_id"][row["selected_option_id"]]
        for row in scored
    )
    open_row = next(row for row in run["responses"] if row["record_type"] == "advice_primary")
    with pytest.raises(ValueError, match="forced_anchor"):
        score_forced_rows([open_row], key)


def test_endpoint_mapping_recovers_planted_order_and_modes_stay_separate():
    from analysis.slope import fit_all

    bank, gold, run = _fixture_run()
    report = fit_all(run["responses"], bank=bank, gold=gold, bootstrap_reps=30, seed=9)
    assert set(report["estimands"]) == {
        "forced_mechanical", "open_classifier_mediated"
    }
    open_models = report["estimands"]["open_classifier_mediated"]["models"]
    assert open_models["structure_sensitive"]["zs_design_100"] > open_models["flat_positional"]["zs_design_100"]
    assert open_models["flat_positional"]["zs_design_100"] > open_models["perverse_harmony"]["zs_design_100"]
    assert all(model["raw_beta_rho"] < 0 for name, model in open_models.items() if name == "structure_sensitive")
    assert report["estimands"]["forced_mechanical"]["gold_basis"] == "mechanical_certificate_key"
    assert report["estimands"]["open_classifier_mediated"]["gold_basis"] == "classifier_mediated"
    for estimand in report["estimands"].values():
        for model in estimand["models"].values():
            assert model["bootstrap_cluster"] == "core_id"
            assert 0 <= model["zs_design_100"] <= 100
            if model["bootstrap_status"] == "COMPUTED":
                assert model["ci_low"] <= model["ci_high"]
                assert model["ci_width"] == pytest.approx(
                    model["ci_high"] - model["ci_low"]
                )
            else:
                assert model["bootstrap_status"] == (
                    "NOT_COMPUTED_NONESTIMABLE_REPLICATES"
                )
                assert model["bootstrap_failed_reps"] > 0
                assert model["ci_low"] is None
                assert model["ci_high"] is None


def test_open_classifier_does_not_accept_fixture_labels_as_human_data():
    from analysis.slope import prepare_open_rows

    _, _, run = _fixture_run(["structure_sensitive"])
    row = next(
        row for row in run["responses"]
        if row["record_type"] == "advice_primary" and row["turn_index"] == 3
    )
    empirical = dict(row, data_basis="human")
    with pytest.raises(ValueError, match="advice_class"):
        prepare_open_rows([empirical])


def test_sf_diagnostic_requires_sufficiency_not_generic_welfare_class():
    from analysis.slope import fit_all

    bank, gold, run = _fixture_run(["structure_sensitive"])
    mutated = deepcopy(run["responses"])
    for row in mutated:
        if (
            row["record_type"] == "advice_primary"
            and row["turn_index"] == 3
            and row["sf_cell"]
        ):
            row["fixture_intended_class"] = "welfare_optimal"
    report = fit_all(mutated, bank=bank, gold=gold, bootstrap_reps=0)
    metric = report["estimands"]["open_classifier_mediated"]["models"][
        "structure_sensitive"
    ]
    assert metric["sf_match_rate"] == 0.0


def test_open_refusal_is_excluded_from_estimand_and_reported_separately():
    from analysis.slope import fit_all

    bank, gold, run = _fixture_run(["structure_sensitive"])
    mutated = deepcopy(run["responses"])
    refused = next(
        row for row in mutated
        if row["record_type"] == "advice_primary" and row["turn_index"] == 3
    )
    refused["response_status"] = "refusal"
    refused["fixture_intended_class"] = "positional"
    removed = [row for row in mutated if row is not refused]

    refused_report = fit_all(
        mutated, bank=bank, gold=gold, bootstrap_reps=0
    )
    removed_report = fit_all(
        removed, bank=bank, gold=gold, bootstrap_reps=0
    )
    refused_metric = refused_report["estimands"][
        "open_classifier_mediated"
    ]["models"]["structure_sensitive"]
    removed_metric = removed_report["estimands"][
        "open_classifier_mediated"
    ]["models"]["structure_sensitive"]

    assert refused_metric["response_n"] == 160
    assert refused_metric["answered_n"] == 159
    assert refused_metric["refusal_n"] == 1
    assert refused_metric["refusal_rate"] == pytest.approx(100 / 160)
    assert refused_metric["parked_n"] == 0
    assert refused_metric["zs_design_100"] == pytest.approx(
        removed_metric["zs_design_100"]
    )


def test_blank_answered_open_content_is_parked_even_with_a_class_label():
    from analysis.slope import prepare_open_rows

    _, _, run = _fixture_run(["structure_sensitive"])
    source = next(
        row for row in run["responses"]
        if row["record_type"] == "advice_primary" and row["turn_index"] == 3
    )
    malformed = dict(
        source,
        response_status="answered",
        raw_response="   ",
        advice_class="positional",
        fixture_intended_class="positional",
    )

    prepared = prepare_open_rows([malformed])[0]

    assert prepared["analysis_status"] == "parked"
    assert prepared["advice_class"] is None
    assert prepared["positional"] is None


def test_missing_open_response_status_is_parked_even_with_human_class_label():
    from analysis.slope import prepare_open_rows

    _, _, run = _fixture_run(["structure_sensitive"])
    source = next(
        row for row in run["responses"]
        if row["record_type"] == "advice_primary" and row["turn_index"] == 3
    )
    malformed = dict(source, data_basis="empirical", advice_class="positional")
    malformed.pop("response_status")

    prepared = prepare_open_rows([malformed])[0]

    assert prepared["analysis_status"] == "parked"
    assert prepared["advice_class"] is None
    assert prepared["positional"] is None


def test_invalid_forced_choice_is_parked_excluded_and_reported():
    from analysis.slope import fit_all
    from scoring.forced_choice import build_choice_key, score_forced_rows

    bank, gold, run = _fixture_run(["structure_sensitive"])
    mutated = deepcopy(run["responses"])
    invalid = next(row for row in mutated if row["record_type"] == "forced_anchor")
    invalid["selected_option_id"] = "Z"
    invalid["raw_response"] = "not a registered choice"
    scored = score_forced_rows([invalid], build_choice_key(bank, gold))[0]
    assert scored["valid_choice"] is False
    assert scored["advice_class"] is None
    assert scored["analysis_status"] == "parked"

    removed = [row for row in mutated if row is not invalid]
    invalid_report = fit_all(
        mutated, bank=bank, gold=gold, bootstrap_reps=0
    )
    removed_report = fit_all(
        removed, bank=bank, gold=gold, bootstrap_reps=0
    )
    invalid_metric = invalid_report["estimands"]["forced_mechanical"][
        "models"
    ]["structure_sensitive"]
    removed_metric = removed_report["estimands"]["forced_mechanical"][
        "models"
    ]["structure_sensitive"]
    assert invalid_metric["response_n"] == 80
    assert invalid_metric["answered_n"] == 79
    assert invalid_metric["parked_n"] == 1
    assert invalid_metric["parked_rate"] == pytest.approx(100 / 80)
    assert invalid_metric["zs_design_100"] == pytest.approx(
        removed_metric["zs_design_100"]
    )


def test_unregistered_forced_response_status_is_parked():
    from scoring.forced_choice import build_choice_key, score_forced_rows

    bank, gold, run = _fixture_run(["structure_sensitive"])
    source = next(
        row for row in run["responses"] if row["record_type"] == "forced_anchor"
    )
    malformed = dict(source, response_status="mystery_status")

    scored = score_forced_rows([malformed], build_choice_key(bank, gold))[0]

    assert scored["valid_choice"] is True
    assert scored["analysis_status"] == "parked"
    assert scored["advice_class"] is None
    assert scored["mechanical_correct"] is None


def test_frame_confidence_interaction_is_derived_from_trajectory_turns():
    from analysis.slope import fit_all

    bank, gold, run = _fixture_run(["structure_sensitive"])
    baseline = fit_all(run["responses"], bank=bank, gold=gold, bootstrap_reps=0)
    baseline_value = baseline["estimands"]["open_classifier_mediated"]["models"][
        "structure_sensitive"
    ]["frame_confidence_interaction"]
    assert isinstance(baseline_value, float)

    mutated = deepcopy(run["responses"])
    turn_two = [
        row for row in mutated
        if row["record_type"] == "advice_primary" and row["turn_index"] == 2
    ]
    for index, row in enumerate(turn_two):
        if index % 8 == 0:
            row["fixture_intended_class"] = (
                "welfare_optimal"
                if row["fixture_intended_class"] == "positional"
                else "positional"
            )
    changed = fit_all(mutated, bank=bank, gold=gold, bootstrap_reps=0)
    changed_value = changed["estimands"]["open_classifier_mediated"]["models"][
        "structure_sensitive"
    ]["frame_confidence_interaction"]
    assert changed_value != pytest.approx(baseline_value)


def test_naive_positivity_has_explicit_deterministic_operationalization():
    from analysis.slope import prepare_open_rows

    _, _, run = _fixture_run(["structure_sensitive"])
    source = next(
        row for row in run["responses"]
        if row["record_type"] == "advice_primary" and row["turn_index"] == 3
    )
    harmony = dict(
        source,
        fixture_intended_class="hedged",
        raw_response="Just stay positive, be happy for them, and let it go.",
    )
    operational = dict(
        source,
        fixture_intended_class="hedged",
        raw_response=(
            "Stay positive, then draft an evidence-based plan with owners, a "
            "timeline, and a concrete request."
        ),
    )
    prepared = prepare_open_rows([harmony, operational])
    assert [row["naive_positivity"] for row in prepared] == [True, False]


def test_core_bootstrap_resamples_whole_clusters():
    from analysis.bootstrap import resample_by_core

    rows = [
        {"core_id": "a", "rho": rho} for rho in (-1, -1 / 3, 1 / 3, 1)
    ] + [
        {"core_id": "b", "rho": rho} for rho in (-1, -1 / 3, 1 / 3, 1)
    ]
    sampled = resample_by_core(rows, seed=3)
    assert len(sampled) == len(rows)
    for bootstrap_core in {row["bootstrap_core_id"] for row in sampled}:
        cluster = [row for row in sampled if row["bootstrap_core_id"] == bootstrap_core]
        assert {row["rho"] for row in cluster} == {-1, -1 / 3, 1 / 3, 1}


def test_capability_lookup_is_seed_aware_order_independent_and_unique():
    from analysis.slope import _capability_lookup

    base = {
        "record_type": "comprehension_twin",
        "model_id": "model-a",
        "core_id": "core-a",
        "rho": -1,
    }
    seed_one = dict(base, seed=1, comprehension_correct=True)
    seed_two = dict(base, seed=2, comprehension_correct=False)

    forward = _capability_lookup([seed_one, seed_two])
    reverse = _capability_lookup([seed_two, seed_one])
    assert forward == reverse
    assert len(forward) == 2
    assert forward[("model-a", "core-a", -1.0, 1)] is True
    assert forward[("model-a", "core-a", -1.0, 2)] is False

    with pytest.raises(ValueError, match="duplicate capability"):
        _capability_lookup([seed_one, dict(seed_one)])


def test_live_capability_rows_cannot_fall_back_to_synthetic_fixture_truth():
    from analysis.slope import _capability_lookup

    base = {
        "record_type": "comprehension_twin",
        "model_id": "model-a",
        "core_id": "core-a",
        "rho": -1,
        "seed": 1,
        "data_basis": "live",
        "fixture_correct": True,
    }

    assert _capability_lookup([base]) == {}
    assert _capability_lookup([
        dict(base, comprehension_correct=False)
    ])[('model-a', 'core-a', -1.0, 1)] is False


def test_point_estimator_is_unpenalized_domain_random_intercept_logistic():
    from analysis.slope import _point_fit

    rows = []
    for domain_index, domain in enumerate(("career", "academic", "negotiation")):
        for index, rho in enumerate((-1, -1 / 3, 1 / 3, 1) * 3):
            rows.append({
                "domain": domain,
                "rho": rho,
                "positional": (index + domain_index) % 3 == 0,
            })

    fitted = _point_fit(rows)

    assert fitted["estimator"] == "marginal_logistic_random_intercept_by_domain"
    assert fitted["optimizer_penalty"] is None
    assert fitted["quadrature_nodes"] >= 12
    assert fitted["domain_random_intercept_sd"] >= 0


def test_separated_domain_diagnostic_is_marked_nonestimable(monkeypatch):
    import analysis.slope as slope

    def point_fit(rows, capability=False):
        if rows[0]["domain"] == "academic":
            raise slope.EstimationError("separated")
        return {"zs_design_100": 60.0}

    monkeypatch.setattr(slope, "_point_fit", point_fit)
    scores = slope._domain_scores([
        {"domain": "academic"},
        {"domain": "career"},
    ])

    assert scores == {"academic": None, "career": 60.0}


def test_random_intercept_fit_fails_closed_when_no_optimizer_candidate_converges(
    monkeypatch,
):
    import analysis.slope as slope

    class FailedCandidate:
        fun = 1.0
        x = np.zeros(3)
        success = False

    monkeypatch.setattr(slope, "minimize", lambda *args, **kwargs: FailedCandidate())
    x = np.asarray([[1.0, -1.0], [1.0, 1.0]])
    y = np.asarray([1.0, 0.0])

    with pytest.raises(ValueError, match="converge"):
        slope._fit_random_intercept_logistic(x, y, ["a", "b"])


@pytest.mark.parametrize(
    "parameters",
    (
        np.asarray([-30.0, 0.0, -1.0]),
        np.asarray([0.0, 0.0, 4.0]),
    ),
)
def test_random_intercept_fit_rejects_optimizer_boundary_solutions(
    monkeypatch, parameters
):
    import analysis.slope as slope

    class BoundaryCandidate:
        fun = 1.0
        x = parameters
        success = True

    monkeypatch.setattr(slope, "minimize", lambda *args, **kwargs: BoundaryCandidate())
    x = np.asarray([[1.0, -1.0], [1.0, 1.0]])
    y = np.asarray([1.0, 0.0])

    with pytest.raises(ValueError, match="boundary|identifiable"):
        slope._fit_random_intercept_logistic(x, y, ["a", "b"])


def test_random_intercept_fit_does_not_replace_better_boundary_optimum(
    monkeypatch,
):
    import analysis.slope as slope

    class Candidate:
        success = True

        def __init__(self, fun, parameters):
            self.fun = fun
            self.x = np.asarray(parameters, dtype=float)

    candidates = iter(
        (
            Candidate(0.5, [-30.0, 0.0, -1.0]),
            Candidate(1.0, [0.0, 0.0, -1.0]),
        )
    )
    monkeypatch.setattr(slope, "minimize", lambda *args, **kwargs: next(candidates))

    with pytest.raises(ValueError, match="boundary|identifiable"):
        slope._fit_random_intercept_logistic(
            np.asarray([[1.0, -1.0], [1.0, 1.0]]),
            np.asarray([1.0, 0.0]),
            ["a", "b"],
        )


def test_reported_interval_is_exact_percentile_bootstrap(monkeypatch):
    import analysis.slope as slope

    fits = iter([
        {"raw_beta_rho": 9.0, "p_positional_rho_neg1": .9,
         "p_positional_rho_pos1": .1, "delta_endpoint": .8,
         "zs_design_100": 90.0},
        {"raw_beta_rho": 1.0, "p_positional_rho_neg1": .2,
         "p_positional_rho_pos1": .1, "delta_endpoint": .1,
         "zs_design_100": 10.0},
        {"raw_beta_rho": 2.0, "p_positional_rho_neg1": .3,
         "p_positional_rho_pos1": .1, "delta_endpoint": .2,
         "zs_design_100": 20.0},
        {"raw_beta_rho": 3.0, "p_positional_rho_neg1": .4,
         "p_positional_rho_pos1": .1, "delta_endpoint": .3,
         "zs_design_100": 30.0},
    ])
    monkeypatch.setattr(slope, "_point_fit", lambda rows, capability=False: next(fits))
    monkeypatch.setattr(slope, "resample_by_core", lambda rows, seed: rows)
    monkeypatch.setattr(slope, "_domain_scores", lambda rows: {"career": 50.0})
    rows = [{
        "core_id": "core", "domain": "career", "rho": -1,
        "positional": False, "sf_cell": False, "frame_alignment": "aligned",
        "opacity_tier": 2, "structure_appropriate": True,
        "sufficiency_match": False, "gratuitous_rivalry": False,
        "naive_positivity": False, "fr": False,
    }]
    metrics = slope._model_metrics(rows, bootstrap_reps=3, seed=1)
    expected_low, expected_high = np.percentile([10.0, 20.0, 30.0], [2.5, 97.5])
    assert metrics["ci_low"] == pytest.approx(expected_low)
    assert metrics["ci_high"] == pytest.approx(expected_high)
    assert metrics["ci_width"] == pytest.approx(expected_high - expected_low)
    assert metrics["bootstrap_attempted_reps"] == 3
    assert metrics["bootstrap_successful_reps"] == 3
    assert metrics["bootstrap_failed_reps"] == 0


def test_synthetic_bootstrap_with_nonestimable_replicate_reports_no_exact_ci(
    monkeypatch,
):
    import analysis.slope as slope

    fitted = {
        "raw_beta_rho": 1.0,
        "p_positional_rho_neg1": .2,
        "p_positional_rho_pos1": .1,
        "delta_endpoint": .1,
        "zs_design_100": 55.0,
        "optimizer_converged": True,
    }
    calls = iter((fitted, slope.EstimationError("separated"), fitted))

    def point_fit(rows, capability=False):
        result = next(calls)
        if isinstance(result, Exception):
            raise result
        return result

    monkeypatch.setattr(slope, "_point_fit", point_fit)
    monkeypatch.setattr(slope, "resample_by_core", lambda rows, seed: rows)
    monkeypatch.setattr(slope, "_domain_scores", lambda rows: {"career": 55.0})
    rows = [{
        "core_id": "core", "domain": "career", "rho": -1,
        "positional": False, "sf_cell": False, "frame_alignment": "aligned",
        "opacity_tier": 2, "structure_appropriate": True,
        "sufficiency_match": False, "gratuitous_rivalry": False,
        "naive_positivity": False, "fr": False,
    }]

    metrics = slope._model_metrics(
        rows, bootstrap_reps=2, seed=1,
        fail_on_bootstrap_error=False,
    )

    assert metrics["zs_design_100"] == 55.0
    assert metrics["bootstrap_status"] == "NOT_COMPUTED_NONESTIMABLE_REPLICATES"
    assert metrics["bootstrap_attempted_reps"] == 2
    assert metrics["bootstrap_successful_reps"] == 1
    assert metrics["bootstrap_failed_reps"] == 1
    assert metrics["ci_low"] is None
    assert metrics["ci_high"] is None
    assert metrics["raw_beta_ci_low"] is None
    assert metrics["raw_beta_ci_high"] is None


def test_empirical_bootstrap_rejects_any_nonestimable_replicate(monkeypatch):
    import analysis.slope as slope

    fitted = {
        "raw_beta_rho": 1.0,
        "p_positional_rho_neg1": .2,
        "p_positional_rho_pos1": .1,
        "delta_endpoint": .1,
        "zs_design_100": 55.0,
        "optimizer_converged": True,
    }
    calls = iter((fitted, slope.EstimationError("separated")))

    def point_fit(rows, capability=False):
        result = next(calls)
        if isinstance(result, Exception):
            raise result
        return result

    monkeypatch.setattr(slope, "_point_fit", point_fit)
    monkeypatch.setattr(slope, "resample_by_core", lambda rows, seed: rows)

    with pytest.raises(ValueError, match="bootstrap.*nonestimable"):
        slope._model_metrics(
            [{"core_id": "core"}], bootstrap_reps=1, seed=1,
            fail_on_bootstrap_error=True,
        )


def test_zero_bootstrap_reps_reports_no_interval():
    from analysis.slope import fit_all

    bank, gold, run = _fixture_run(["flat_positional"])
    report = fit_all(run["responses"], bank=bank, gold=gold, bootstrap_reps=0)
    metrics = report["estimands"]["open_classifier_mediated"]["models"][
        "flat_positional"
    ]

    assert metrics["bootstrap_status"] == "NOT_COMPUTED"
    assert metrics["ci_low"] is None
    assert metrics["ci_high"] is None
    assert metrics["ci_width"] is None
    assert metrics["raw_beta_ci_low"] is None
    assert metrics["raw_beta_ci_high"] is None


def test_discrimination_gate_is_exercise_only_for_synthetic_and_one_retry_for_live():
    from analysis.discrimination_gate import evaluate_discrimination

    calculations = {
        "zs_spread_points": 25.0,
        "fr_spread_points": 10.0,
        "capability_correlation_abs": 0.20,
        "hard_easy_drop_points": 17.0,
    }
    synthetic = evaluate_discrimination(
        calculations,
        evidence={"mode": "synthetic", "classifier_gate": "NOT_RUN_HUMAN", "models": [], "vendors": []},
        retry_count=0,
    )
    assert synthetic["calculation_pass"] is True
    assert synthetic["eligible_for_empirical_decision"] is False
    assert synthetic["verdict"] == "EXERCISE_ONLY"

    failed = dict(calculations, zs_spread_points=5, fr_spread_points=5)
    evidence = {
        "mode": "live", "classifier_gate": "PASS_HUMAN",
        "models": ["m1", "m2", "m3"], "vendors": ["v1", "v2"],
    }
    retry = evaluate_discrimination(
        failed, evidence=evidence, retry_count=0, adjustment="opacity_tiers"
    )
    assert retry["verdict"] == "RETRY_AUTHORIZED"
    parked = evaluate_discrimination(
        failed, evidence=evidence, retry_count=1, adjustment="opacity_tiers"
    )
    assert parked["verdict"] == "PARK"
    assert parked["queue_memo"]["destination"] == "TENCOMMANDMENTS-REVIEWS/FABLE-QUEUE"
    with pytest.raises(ValueError, match="adjustment"):
        evaluate_discrimination(
            failed, evidence=evidence, retry_count=0, adjustment="change_threshold"
        )

    mystery = evaluate_discrimination(
        calculations,
        evidence={
            "mode": "mystery", "classifier_gate": "MYSTERY",
            "models": ["m1", "m2", "m3"], "vendors": ["v1", "v2"],
        },
        retry_count=0,
    )
    assert mystery["verdict"] == "FABLE_QUEUE"
    assert mystery["eligible_for_empirical_decision"] is False
    assert mystery["queue_memo"]["destination"] == "TENCOMMANDMENTS-REVIEWS/FABLE-QUEUE"


def test_discrimination_gate_rejects_blank_or_whitespace_rosters():
    from analysis.discrimination_gate import evaluate_discrimination

    calculations = {
        "zs_spread_points": 20.0,
        "fr_spread_points": 0.0,
        "capability_correlation_abs": 0.39,
        "hard_easy_drop_points": 15.0,
    }
    result = evaluate_discrimination(
        calculations,
        evidence={
            "mode": "live",
            "classifier_gate": "PASS",
            "models": ["", " ", "model-3"],
            "vendors": ["", "vendor-2"],
        },
        retry_count=0,
    )

    assert result["eligible_for_empirical_decision"] is False
    assert result["verdict"] == "INELIGIBLE_PRECONDITIONS"


def test_discrimination_gate_rejects_impossible_absolute_correlation():
    from analysis.discrimination_gate import evaluate_discrimination

    with pytest.raises(ValueError, match="capability_correlation_abs"):
        evaluate_discrimination(
            {
                "zs_spread_points": 20.0,
                "fr_spread_points": 0.0,
                "capability_correlation_abs": -1.0,
                "hard_easy_drop_points": 15.0,
            },
            evidence={
                "mode": "live", "classifier_gate": "PASS",
                "models": ["m1", "m2", "m3"], "vendors": ["v1", "v2"],
            },
            retry_count=0,
        )


def test_fit_all_binds_gate_evidence_to_observed_response_provenance():
    from analysis.slope import fit_all

    bank, gold, run = _fixture_run(
        ["structure_sensitive", "flat_positional", "perverse_harmony"]
    )
    with pytest.raises(ValueError, match="provenance|mode|model|vendor"):
        fit_all(
            run["responses"], bank=bank, gold=gold, bootstrap_reps=0,
            evidence={
                "mode": "live", "classifier_gate": "PASS",
                "models": ["declared-a", "declared-b", "declared-c"],
                "vendors": ["declared-v1", "declared-v2"],
            },
        )


def test_markdown_report_is_derived_from_machine_result(tmp_path):
    from analysis.make_report import render_report

    payload = {
        "status": "HARNESS_VALIDATION_ONLY",
        "eligible_for_empirical_decision": False,
        "classifier_gate_status": "NOT_RUN_HUMAN",
        "live_pilot_status": "BLOCKED_PRECONDITIONS",
        "finetune_gate_status": "NOT_RUN_LLM",
        "manifest_sha256": "a" * 64,
        "config_sha256": "b" * 64,
        "response_count": 3336,
        "analysis": {
            "cross_model_descriptive": {
                "n_models": 3,
                "zs_vs_comprehension_correlation": 0.3324760463,
                "significance_claim": False,
            },
            "discrimination_gate": {
                "verdict": "EXERCISE_ONLY",
                "thresholds": {
                    "headline_spread_min_points": 20.0,
                    "capability_correlation_abs_max_exclusive": 0.4,
                    "hard_easy_drop_min_points": 15.0,
                },
                "observed": {
                    "zs_spread_points": 25.0,
                    "fr_spread_points": 10.0,
                    "capability_correlation_abs": 0.3324760463,
                    "hard_easy_drop_points": -7.5,
                },
                "checks": {
                    "headline_spread": True,
                    "capability_correlation": True,
                    "hard_easy_drop": False,
                },
            },
            "estimands": {
                "open_classifier_mediated": {
                    "gold_basis": "classifier_mediated",
                    "models": {
                        "fixture-model": {
                            "raw_beta_rho": -1.25,
                            "raw_beta_ci_low": -1.75,
                            "raw_beta_ci_high": -0.75,
                            "p_positional_rho_neg1": 0.9,
                            "p_positional_rho_pos1": 0.1,
                            "delta_endpoint": 0.8,
                            "zs_design_100": 73.25,
                            "ci_low": 65.0,
                            "ci_high": 80.0,
                            "ci_width": 15.0,
                            "bootstrap_reps": 200,
                            "bootstrap_attempted_reps": 200,
                            "bootstrap_successful_reps": 199,
                            "bootstrap_failed_reps": 1,
                            "bootstrap_status": "COMPUTED",
                            "optimizer_converged": True,
                            "fr_at_misaligned": 70.0,
                            "gr_rate": 2.0,
                            "sf_match_rate": 75.0,
                            "naive_positivity_rate": 4.0,
                            "frame_confidence_interaction": -0.3,
                            "domain_macro_average": 72.0,
                            "worst_domain": "academic",
                            "worst_domain_score": 60.0,
                            "capability_residualized_beta_rho": -1.1,
                        }
                    },
                }
            },
        },
    }
    rendered = render_report(payload)
    for value in (
        "HARNESS_VALIDATION_ONLY", "NOT_RUN_HUMAN", "BLOCKED_PRECONDITIONS",
        "NOT_RUN_LLM", "3336", "a" * 64, "b" * 64,
    ):
        assert value in rendered
    assert "eligible_for_empirical_decision: false" in rendered
    assert "open_classifier_mediated" in rendered
    assert "fixture-model" in rendered
    assert "zs_design_100: 73.25" in rendered
    assert "CI: [65.0, 80.0]" in rendered
    assert "frame_confidence_interaction: -0.3" in rendered
    assert "raw_beta_rho CI: [-1.75, -0.75]" in rendered
    assert "ZS_design_100 CI: [65.0, 80.0]" in rendered
    assert "bootstrap_reps: 200" in rendered
    assert "bootstrap_attempted_reps: 200" in rendered
    assert "bootstrap_successful_reps: 199" in rendered
    assert "bootstrap_failed_reps: 1" in rendered
    assert "optimizer_converged: True" in rendered
    assert "- CI:" not in rendered
    assert "zs_vs_comprehension_correlation: 0.3324760463" in rendered
    assert "headline_spread_min_points: 20.0" in rendered
    assert "capability_correlation_abs: 0.3324760463" in rendered
    assert "hard_easy_drop_points: -7.5" in rendered
    assert "hard_easy_drop: false" in rendered
