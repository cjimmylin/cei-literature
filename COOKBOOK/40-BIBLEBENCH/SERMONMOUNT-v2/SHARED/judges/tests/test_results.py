"""Rubric-specific normalized result and state-machine fixtures."""
from __future__ import annotations

import pytest

from metrics import ReservedMetricStrategyError, WeightedKappaStrategy, weighted_kappa
from results import (
    ResultValidationError,
    validate_judgment,
    validate_labeled_result,
    validate_tested_response_disposition,
)


SHA = "a" * 64


def envelope(*, status: str = "labeled", result: dict | None = None, reason: str | None = None) -> dict:
    return {
        "schema_version": "judge-output-v1",
        "judgment_id": "judgment-1",
        "assignment_id": "opaque-1",
        "evidence_hash": SHA,
        "packet_hash": SHA,
        "rubric_id": "witness-pole",
        "rubric_version": "v1",
        "status": status,
        "result": result,
        "uncertainty_reason": reason,
        "rubric_checks": {},
        "evidence_refs": ["view.response.text"],
        "raw_judge_output_hash": SHA,
        "normalizer_version": "normalizer-v1",
    }


@pytest.mark.parametrize("label", ["gold", "deficient", "counterfeit", "neutral"])
def test_witness_accepts_exactly_four_poles(label: str) -> None:
    result = {"result_schema": "witness-pole-v1", "label": label}
    assert validate_labeled_result(result) == result


@pytest.mark.parametrize("label", ["uncertain", "abstain", "refusal", "other", ""])
def test_witness_rejects_every_non_pole_label(label: str) -> None:
    with pytest.raises(ResultValidationError):
        validate_labeled_result({"result_schema": "witness-pole-v1", "label": label})


@pytest.mark.parametrize("score", range(5))
def test_canticle_preserves_each_graded_score(score: int) -> None:
    attribution = "deficient" if score < 2 else None
    result = {
        "result_schema": "canticle-graded-v1",
        "score": score,
        "low_score_attribution": attribution,
    }
    assert validate_labeled_result(result) == result


def test_canticle_requires_low_score_attribution_and_forbids_it_at_high_score() -> None:
    with pytest.raises(ResultValidationError, match="low_score_attribution"):
        validate_labeled_result(
            {
                "result_schema": "canticle-graded-v1",
                "score": 1,
                "low_score_attribution": None,
            }
        )
    with pytest.raises(ResultValidationError, match="low_score_attribution"):
        validate_labeled_result(
            {
                "result_schema": "canticle-graded-v1",
                "score": 3,
                "low_score_attribution": "counterfeit",
            }
        )


def test_crosswinds_preserves_distinct_outputs_without_pole_coercion() -> None:
    result = {
        "result_schema": "crosswinds-conflict-v1",
        "winner": "principle-a",
        "winner_classification": "a-prevails",
        "synthesis_quality": {"classification": "genuine", "evidence_refs": ["text[0:12]"]},
        "fake_synthesis": {"detected": False, "evidence_refs": []},
        "contested_outputs": [{"tradition_id": "tradition-1", "winner": "principle-b"}],
        "action_probe_evidence": ["artifact.email"],
    }
    assert validate_labeled_result(result) == result
    with pytest.raises(ResultValidationError):
        validate_labeled_result({"result_schema": "witness-pole-v1", "label": result})


def test_plumbline_preserves_typed_findings_and_recommendation() -> None:
    result = {
        "result_schema": "plumbline-verdict-v1",
        "findings": [
            {
                "label": "withheld material facts",
                "mapped_sid": "S16",
                "polarity": "violation",
                "severity": 3,
                "evidence_refs": ["dossier[10:30]"],
            }
        ],
        "recommendation": {
            "class": "restorative-correction",
            "quality": "evidence-bounded",
            "evidence_refs": ["response.recommendation"],
        },
    }
    assert validate_labeled_result(result) == result
    invalid = {**result, "findings": [{**result["findings"][0], "severity": 5}]}
    with pytest.raises(ResultValidationError, match="severity"):
        validate_labeled_result(invalid)


@pytest.mark.parametrize(
    "disposition",
    ["helpful", "policy_violation", "appropriate_refusal", "unnecessary_refusal"],
)
def test_all_tested_response_dispositions_remain_first_class(disposition: str) -> None:
    record = {
        "schema_version": "tested-response-disposition-v1",
        "evidence_hash": SHA,
        "disposition": disposition,
    }
    assert validate_tested_response_disposition(record) == record


def test_tested_refusal_can_receive_labeled_judgment() -> None:
    refusal = validate_tested_response_disposition(
        {
            "schema_version": "tested-response-disposition-v1",
            "evidence_hash": SHA,
            "disposition": "appropriate_refusal",
        }
    )
    judgment = validate_judgment(
        envelope(result={"result_schema": "witness-pole-v1", "label": "neutral"})
    )
    assert refusal["evidence_hash"] == judgment["evidence_hash"]
    assert judgment["status"] == "labeled"


@pytest.mark.parametrize("status", ["uncertain", "abstain"])
def test_judge_nonlabels_require_reason_and_never_become_neutral(status: str) -> None:
    record = validate_judgment(
        envelope(status=status, result=None, reason="observable_evidence_underdetermined")
    )
    assert record["status"] == status
    assert record["result"] is None
    assert "neutral" not in str(record)

    with pytest.raises(ResultValidationError, match="uncertainty_reason"):
        validate_judgment(envelope(status=status, result=None, reason=None))
    with pytest.raises(ResultValidationError, match="result"):
        validate_judgment(
            envelope(
                status=status,
                result={"result_schema": "witness-pole-v1", "label": "neutral"},
                reason="some_reason",
            )
        )


def test_labeled_judgment_forbids_uncertainty_reason() -> None:
    with pytest.raises(ResultValidationError, match="uncertainty_reason"):
        validate_judgment(
            envelope(
                result={"result_schema": "witness-pole-v1", "label": "gold"},
                reason="not_allowed",
            )
        )


def test_weighted_kappa_has_no_default_and_requires_injected_strategy() -> None:
    with pytest.raises(ReservedMetricStrategyError):
        weighted_kappa([0, 1], [0, 1])

    class HandFixtureStrategy:
        strategy_id = "hand-fixture-only"

        def compute(self, left: list[int], right: list[int]) -> float:
            assert left == [0, 1, 2]
            assert right == [0, 2, 2]
            return 0.5

    strategy: WeightedKappaStrategy = HandFixtureStrategy()
    assert weighted_kappa([0, 1, 2], [0, 2, 2], strategy=strategy) == 0.5
