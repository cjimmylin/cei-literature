from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from decimal import Decimal
from fractions import Fraction
import json
import math

import pytest

from conftest import (
    CustomReal,
    FAMILY_CODE,
    official_basis,
    realism_fixture,
    valid_capability_reference,
)
import skim_constants as constants
import skim_evidence as evidence
import skim_hashing as hashing


def test_capability_projections_are_derived_from_population_z_scores():
    reference = valid_capability_reference()

    projections = evidence.derive_capability_projections(reference)

    assert projections == {
        "m1": pytest.approx(-math.sqrt(3.0), rel=1e-12, abs=1e-12),
        "m2": pytest.approx(0.0, rel=1e-12, abs=1e-12),
        "m3": pytest.approx(math.sqrt(3.0), rel=1e-12, abs=1e-12),
    }
    assert json.loads(hashing.canonical_json(projections)) == pytest.approx(
        dict(projections), rel=1e-12, abs=1e-12
    )
    with pytest.raises(TypeError):
        projections["m1"] = 0.0

def test_capability_reference_rejects_self_asserted_or_misoriented_pc1():
    reference = valid_capability_reference()
    failures = []

    arbitrary_scores = deepcopy(reference)
    arbitrary_scores["projected_scores"] = {"m1": -100.0, "m2": 7.0, "m3": 99.0}
    arbitrary_scores["content_sha256"] = evidence.hash_capability_reference(
        arbitrary_scores
    )
    failures.append(arbitrary_scores)

    old_sign_syntax = deepcopy(reference)
    old_sign_syntax["pc1_sign"] = "positive_loading_on_bench_a"
    old_sign_syntax["content_sha256"] = evidence.hash_capability_reference(
        old_sign_syntax
    )
    failures.append(old_sign_syntax)

    unknown_anchor = deepcopy(reference)
    unknown_anchor["pc1_sign"] = "positive_loading_on:not_a_column"
    unknown_anchor["content_sha256"] = evidence.hash_capability_reference(
        unknown_anchor
    )
    failures.append(unknown_anchor)

    negative_anchor = deepcopy(reference)
    negative_anchor["pc1_loadings"] = {
        "bench_a": -math.sqrt(0.5),
        "bench_b": math.sqrt(0.5),
    }
    negative_anchor["content_sha256"] = evidence.hash_capability_reference(
        negative_anchor
    )
    failures.append(negative_anchor)

    nonunit_loading = deepcopy(reference)
    nonunit_loading["pc1_loadings"] = {"bench_a": 0.6, "bench_b": -0.6}
    nonunit_loading["content_sha256"] = evidence.hash_capability_reference(
        nonunit_loading
    )
    failures.append(nonunit_loading)

    assert all(
        not evidence.validate_capability_reference(
            candidate, ("m1", "m2", "m3")
        )
        for candidate in failures
    )

def test_capability_projection_rejects_zero_population_standard_deviation():
    reference = valid_capability_reference()
    for row in reference["model_rows"]:
        row["bench_a"] = 1.0
    reference["content_sha256"] = evidence.hash_capability_reference(reference)

    assert evidence.derive_capability_projections(reference) is None
    assert not evidence.validate_capability_reference(reference)

def test_capability_reference_requires_complete_external_finite_hashed_data():
    reference = valid_capability_reference()
    assert set(reference) == set(constants.CAPABILITY_REFERENCE_FIELDS)
    assert evidence.capability_reference_status(reference, ("m1", "m2", "m3")) == (
        "COMPLETE"
    )
    assert evidence.validate_capability_reference(reference, ("m1", "m2", "m3"))

    failures = []
    for field in constants.CAPABILITY_REFERENCE_FIELDS:
        candidate = deepcopy(reference)
        candidate.pop(field)
        failures.append(candidate)
    constant = deepcopy(reference)
    for row in constant["model_rows"]:
        row["bench_a"] = 1.0
    constant["content_sha256"] = evidence.hash_capability_reference(constant)
    failures.append(constant)
    nonfinite = deepcopy(reference)
    nonfinite["projected_scores"]["m2"] = float("nan")
    failures.append(nonfinite)
    stale_hash = deepcopy(reference)
    stale_hash["pc1_loadings"]["bench_a"] = 0.6
    failures.append(stale_hash)
    nonintegral_ddof = deepcopy(reference)
    nonintegral_ddof["standardization"]["ddof"] = 0.0
    nonintegral_ddof["content_sha256"] = evidence.hash_capability_reference(
        nonintegral_ddof
    )
    failures.append(nonintegral_ddof)
    extra = deepcopy(reference)
    extra["fabricated"] = True
    failures.append(extra)
    numeric_failures = []
    for value in (
        Fraction(1, 2),
        Decimal("0.5"),
        CustomReal(0.5),
        10**10000,
        float("nan"),
        float("inf"),
        object(),
    ):
        bad_row = deepcopy(reference)
        bad_row["model_rows"][0]["bench_a"] = value
        numeric_failures.append(bad_row)
        bad_loading = deepcopy(reference)
        bad_loading["pc1_loadings"]["bench_a"] = value
        numeric_failures.append(bad_loading)
    nonstring_row_key = deepcopy(reference)
    nonstring_row_key["model_rows"][0][1] = "unsupported"
    numeric_failures.append(nonstring_row_key)
    assert all(
        evidence.derive_capability_projections(candidate) is None
        for candidate in numeric_failures
    )
    failures.extend(numeric_failures)
    assert all(
        evidence.capability_reference_status(candidate, ("m1", "m2", "m3"))
        == "NOT_ESTIMABLE"
        for candidate in failures
    )

def test_capability_reference_rejects_constant_required_model_projection():
    reference = valid_capability_reference()
    reference["model_rows"] = [
        {"model_id": "m1", "bench_a": 1.0, "bench_b": 1.0},
        {"model_id": "m2", "bench_a": 1.0, "bench_b": 2.0},
        {"model_id": "m3", "bench_a": 1.0, "bench_b": 3.0},
        {"model_id": "m4", "bench_a": 4.0, "bench_b": 4.0},
    ]
    reference["pc1_loadings"] = {"bench_a": 1.0, "bench_b": 0.0}
    reference["projected_scores"] = {
        "m1": -1.0 / math.sqrt(3.0),
        "m2": -1.0 / math.sqrt(3.0),
        "m3": -1.0 / math.sqrt(3.0),
        "m4": math.sqrt(3.0),
    }
    reference["content_sha256"] = evidence.hash_capability_reference(reference)

    assert evidence.capability_reference_status(reference) == "COMPLETE"
    assert evidence.capability_reference_status(
        reference, ("m1", "m2", "m3")
    ) == "NOT_ESTIMABLE"

def test_evidence_basis_is_frozen_exact_and_fails_closed():
    basis = official_basis()
    assert basis.official_eligible is True
    assert basis.eligible_for_empirical_decision is True
    with pytest.raises(FrozenInstanceError):
        basis.mode = "synthetic"
    ineligible = (
        replace(basis, mode="synthetic", synthetic=True),
        replace(basis, diagnostic_status=constants.DIAGNOSTIC_STATUS),
        replace(basis, professional_realism_status="NOT_RUN"),
        replace(basis, human_baseline_status="NOT_RUN"),
        replace(basis, model_ids=("m1", "m2"), vendors=("a", "b")),
        replace(basis, vendors=("vendor-a",) * 3),
        replace(basis, seeds=(101,)),
        replace(basis, frozen_hashes={}),
        replace(
            basis,
            frozen_hashes={
                name: "0" * 64 for name in constants.FROZEN_ARTIFACT_HASH_FIELDS
            },
        ),
        replace(basis, capability_reference=None),
    )
    assert all(candidate.official_eligible is False for candidate in ineligible)

def test_release_budget_enforces_request_call_and_cost_pairs():
    shared = {
        "terminal_actions_per_request": 1,
        "syntax_repairs_per_request": 1,
        "price_attribution_complete": True,
        "cost_attribution_complete": True,
    }
    assert evidence.release_budget_allows(
        run_kind="smoke",
        scheduled_requests=9,
        paid_calls=18,
        attributed_cost_usd=1.0,
        **shared,
    )
    assert not evidence.release_budget_allows(
        run_kind="smoke",
        scheduled_requests=9,
        paid_calls=19,
        attributed_cost_usd=1.0,
        **shared,
    )
    assert not evidence.release_budget_allows(
        run_kind="smoke",
        scheduled_requests=8,
        paid_calls=16,
        attributed_cost_usd=0.5,
        **shared,
    )
    assert evidence.release_budget_allows(
        run_kind="full_diagnostic",
        scheduled_requests=2400,
        paid_calls=4800,
        attributed_cost_usd=25.0,
        **shared,
    )
    assert not evidence.release_budget_allows(
        run_kind="full_diagnostic",
        scheduled_requests=2399,
        paid_calls=4700,
        attributed_cost_usd=20.0,
        **shared,
    )
    assert not evidence.release_budget_allows(
        run_kind="smoke",
        scheduled_requests=9,
        paid_calls=9,
        attributed_cost_usd=0.1,
        price_attribution_complete=False,
        cost_attribution_complete=True,
        terminal_actions_per_request=1,
        syntax_repairs_per_request=0,
    )
    assert evidence.release_budget_allows(
        run_kind="official",
        scheduled_requests=7200,
        paid_calls=14400,
        attributed_cost_usd=50.0,
        user_frozen_cost_cap_usd=50.0,
        **shared,
    )
    assert not evidence.release_budget_allows(
        run_kind="official",
        scheduled_requests=7200,
        paid_calls=7200,
        attributed_cost_usd=1.0,
        user_frozen_cost_cap_usd=None,
        **shared,
    )

def test_professional_realism_is_derived_from_raw_complete_evidence():
    core_families, panel, ratings = realism_fixture()
    result = evidence.evaluate_professional_realism(
        core_families, panel, ratings, []
    )

    assert result.status == "PASS"
    assert result.passes is True
    assert result.family_passing_cores == {
        family: 7 for family in FAMILY_CODE
    }
    assert result.fleiss_kappa == {
        "scenario_realism": pytest.approx(1.0),
        "magnitude_window_plausibility": pytest.approx(1.0),
    }
    assert {rating["rater_id"] for rating in ratings} == {
        "pro-1",
        "pro-2",
        "pro-3",
    }
    assert evidence.professional_realism_passes(core_families, panel, ratings, [])

def test_professional_realism_revision_history_is_exact_and_pre_model():
    assert constants.REVISION_HISTORY_FIELDS == (
        "round",
        "completed_before_model_data",
        "reason",
    )
    core_families, panel, ratings = realism_fixture()
    valid_revision = [
        {
            "round": 1,
            "completed_before_model_data": True,
            "reason": "Clarified one magnitude-window surface.",
        }
    ]
    assert evidence.evaluate_professional_realism(
        core_families, panel, ratings, valid_revision
    ).passes

    invalid_histories = (
        [valid_revision[0], deepcopy(valid_revision[0])],
        [{**valid_revision[0], "completed_before_model_data": False}],
        [{**valid_revision[0], "round": 2}],
        [{**valid_revision[0], "reason": ""}],
        [{**valid_revision[0], "extra": True}],
        [{"round": 1, "completed_before_model_data": True}],
        "revision",
    )
    assert all(
        not evidence.evaluate_professional_realism(
            core_families, panel, ratings, history
        ).passes
        for history in invalid_histories
    )

def test_professional_realism_rejects_planted_raw_evidence_violations():
    core_families, panel, ratings = realism_fixture()
    failures = []

    missing = deepcopy(ratings)
    missing.pop()
    failures.append((core_families, panel, missing))

    duplicate = deepcopy(ratings)
    duplicate.append(deepcopy(duplicate[0]))
    failures.append((core_families, panel, duplicate))

    same_rater = deepcopy(ratings)
    same_rater[1]["rater_id"] = same_rater[0]["rater_id"]
    failures.append((core_families, panel, same_rater))

    absent_panelist = deepcopy(ratings)
    by_core = {}
    for rating in absent_panelist:
        by_core.setdefault(rating["core_id"], []).append(rating)
    for records in by_core.values():
        for record in records:
            if record["rater_id"] == "pro-3":
                other = next(item for item in records if item is not record)
                record["rater_id"] = (
                    "pro-2" if other["rater_id"] == "pro-1" else "pro-1"
                )
    failures.append((core_families, panel, absent_panelist))

    wrong_family = deepcopy(core_families)
    wrong_family[next(iter(wrong_family))] = "buried_talent"
    failures.append((wrong_family, panel, ratings))

    synthetic_panel = deepcopy(panel)
    synthetic_panel[0]["synthetic"] = True
    failures.append((core_families, synthetic_panel, ratings))

    unqualified = deepcopy(panel)
    unqualified[0]["qualification"] = ""
    failures.append((core_families, unqualified, ratings))

    false_coverage = deepcopy(panel)
    false_coverage[0]["covers_finance"] = True
    failures.append((core_families, false_coverage, ratings))

    bad_type = deepcopy(ratings)
    bad_type[0]["scenario_realism"] = 1
    failures.append((core_families, panel, bad_type))

    assert all(
        evidence.evaluate_professional_realism(*evidence_case, []).passes is False
        for evidence_case in failures
    )

    degenerate = deepcopy(ratings)
    for rating in degenerate:
        rating["scenario_realism"] = True
        rating["magnitude_window_plausibility"] = True
    result = evidence.evaluate_professional_realism(
        core_families, panel, degenerate, []
    )
    assert result.status == "NOT_ESTIMABLE"
    assert result.passes is False
