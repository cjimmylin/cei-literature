import json
from pathlib import Path
import re
import uuid

import pytest

from lib.registry import CLAUSE_REGISTRY
from lib.judge_cases import OccurrenceCaseRegistry, canonical_response_sha256
from scorers.followthrough import (
    CLAUSES,
    irr_audit,
    score_followthrough,
    validate_anchor_manifest,
)
from scorers.judge_roster import FrozenJudgeRoster, canonical_roster_sha256


BANK = Path(__file__).resolve().parents[1]
FIXTURES = BANK / "scorers" / "fixtures_followthrough.json"
ROSTER_FIXTURE = BANK / "sidecar" / "judge_roster.mock.json"
CASE_ID = "JCASE-123e4567-e89b-42d3-a456-426614174000"
CASE_ID_2 = "JCASE-223e4567-e89b-42d3-a456-426614174000"
SEED = "JSEED-323e4567-e89b-42d3-a456-426614174000"
ITEM = "CROSSROADS-0001"
JUDGE_A = "JUDGE-550e8400-e29b-41d4-a716-446655440000"
JUDGE_B = "JUDGE-6ba7b810-9dad-41d1-80b4-00c04fd430c8"
JUDGE_C = "JUDGE-6ba7b811-9dad-41d1-80b4-00c04fd430c8"
RESPONSE_SHA256 = canonical_response_sha256(
    [{"role": "assistant", "content": "Observable enacted response."}],
    [{"path": "final-report", "content": "Corrected."}],
)


def load_manifest():
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def rating(judge_id, score, pole="none", **updates):
    row = {
        "judge_id": judge_id,
        "score": score,
        "failure_pole": pole,
        "pious_language_without_action": False,
        "positive_duty_completed": score >= 3,
        "evidence_ids": [f"tool:{judge_id[-4:]}", "artifact:final"],
    }
    row.update(updates)
    return row


def case(ratings=None, adjudication=None, **updates):
    row = {
        "judge_case_id": CASE_ID,
        "response_sha256": RESPONSE_SHA256,
        "clause": "C6",
        "ratings": ratings or [
            rating(JUDGE_A, 3),
            rating(JUDGE_B, 4),
        ],
        "adjudication": adjudication,
    }
    row.update(updates)
    return row


@pytest.fixture
def judging(tmp_path):
    uuids = iter([
        uuid.UUID(CASE_ID.removeprefix("JCASE-")),
        uuid.UUID(CASE_ID_2.removeprefix("JCASE-")),
    ])
    registry = OccurrenceCaseRegistry(
        tmp_path / "private" / "judge_case_registry.jsonl",
        {SEED: ITEM},
        uuid_factory=lambda: next(uuids),
    )

    def issue(*, occurrence=1, candidate_family="candidate-openai"):
        return registry.issue_case(
            authoring_seed=SEED,
            run_id="run-a",
            execution_id=f"execution-{occurrence}",
            candidate_model_snapshot="provider/model-20260711",
            candidate_family=candidate_family,
            response_sha256=RESPONSE_SHA256,
            scoring_occurrence=occurrence,
        )

    assert issue() == CASE_ID
    document = json.loads(ROSTER_FIXTURE.read_text(encoding="utf-8"))
    roster = FrozenJudgeRoster.from_document(
        document, expected_sha256=canonical_roster_sha256(document)
    )
    return {"registry": registry, "roster": roster, "issue": issue}


def score(record, judging):
    return score_followthrough(
        record, roster=judging["roster"],
        case_registry=judging["registry"],
    )


def test_anchor_manifest_is_exact_16_by_5_by_3_and_registry_verbatim():
    manifest = load_manifest()
    assert manifest["provenance"] == "harness validation, NOT a measurement"
    assert manifest["human_validation_status"] == "not performed; external dependency"
    assert validate_anchor_manifest(manifest) is True
    assert set(manifest["clauses"]) == set(CLAUSES)
    exemplar_ids = []
    for clause, rubric in manifest["clauses"].items():
        assert rubric["operational_definition"] == CLAUSE_REGISTRY[clause]["construct"]
        assert rubric["specialization"] != rubric["operational_definition"]
        assert set(rubric["anchors"]) == {str(score) for score in range(5)}
        assert all(len(rubric["anchors"][str(score)]) == 3 for score in range(5))
        exemplars = [item for level in rubric["anchors"].values() for item in level]
        exemplar_ids.extend(item["exemplar_id"] for item in exemplars)
        assert any(item["pious_language_without_action"] for item in exemplars)
        assert any(item["failure_pole"] == "harsh" for item in exemplars)
    assert len(exemplar_ids) == 16 * 5 * 3
    assert len(set(exemplar_ids)) == len(exemplar_ids)


def test_anchor_texts_are_concrete_clause_specific_enactments_not_templates():
    manifest = load_manifest()
    forbidden = re.compile(
        r"\bexemplar\s*[123]\b|\bgeneric\b|\bplaceholder\b|"
        r"\btemplate\b|\blevel\s*[0-4]\b",
        re.IGNORECASE,
    )
    for clause, rubric in manifest["clauses"].items():
        assert rubric["sentimental_pole"] == CLAUSE_REGISTRY[clause]["sentimental_pole"]
        assert rubric["harsh_pole"] == CLAUSE_REGISTRY[clause]["harsh_pole"]
        for score in range(5):
            rows = rubric["anchors"][str(score)]
            assert len({row["context_id"] for row in rows}) == 3
            assert len({(row["action_evidence"], row["artifact_evidence"])
                        for row in rows}) == 3
            for row in rows:
                text = row["text"]
                assert forbidden.search(text) is None, (clause, score, text)
                assert row["action_evidence"].lower() in text.lower()
                assert row["artifact_evidence"].lower() in text.lower()
                assert len(text.split()) >= 18


def test_consensus_preserves_two_raw_judges_and_blind_case_identity(judging):
    scored = score(case(), judging)
    assert scored["judge_case_id"] == CASE_ID
    assert scored["judge_ids"] == [JUDGE_A, JUDGE_B]
    assert scored["judge_families"] == ["judge-anthropic", "judge-google"]
    assert scored["roster_sha256"] == judging["roster"].sha256
    assert scored["response_sha256"] == RESPONSE_SHA256
    assert scored["raw_ratings"] == case()["ratings"]
    assert scored["consensus"]["score"] == 3.5
    assert scored["consensus"]["source"] == "raw-judge mean"
    assert scored["adjudication"] is None
    assert scored["complete"] is True
    assert scored["mechanical_flag"] is True
    assert "overall_score" not in scored


def test_material_disagreement_remains_incomplete_until_separate_adjudication(judging):
    ratings = [
        rating(JUDGE_A, 1, "harsh"),
        rating(JUDGE_B, 4, "none"),
    ]
    incomplete = score(case(ratings=ratings), judging)
    assert incomplete["complete"] is False
    assert incomplete["consensus"] is None
    assert incomplete["disagreement"] == {
        "score_range": 3,
        "pole_disagreement": True,
        "adjudication_required": True,
        "adjudicated": False,
    }

    adjudication = {
        **rating(JUDGE_C, 2, "mixed",
                 positive_duty_completed=False),
        "reason": "Reviewed both cited artifacts against the frozen C6 anchors.",
    }
    complete = score(case(ratings=ratings, adjudication=adjudication), judging)
    assert complete["raw_ratings"] == ratings
    assert complete["adjudication"] == adjudication
    assert complete["consensus"]["score"] == 2
    assert complete["consensus"]["source"] == "adjudicator"
    assert complete["complete"] is True


def test_adjudicator_family_must_differ_from_both_raw_judge_families(judging):
    document = json.loads(ROSTER_FIXTURE.read_text(encoding="utf-8"))
    adjudicator = next(
        row for row in document["judges"] if row["role"] == "adjudicator"
    )
    adjudicator["family"] = "judge-anthropic"
    correlated_roster = FrozenJudgeRoster.from_document(
        document, expected_sha256=canonical_roster_sha256(document)
    )
    ratings = [rating(JUDGE_A, 1, "harsh"), rating(JUDGE_B, 4, "none")]
    adjudication = {
        **rating(JUDGE_C, 2, "mixed", positive_duty_completed=False),
        "reason": "Applied the frozen C6 anchors to both raw evidence sets.",
    }
    with pytest.raises(ValueError, match="adjudicator family must differ"):
        score_followthrough(
            case(ratings=ratings, adjudication=adjudication),
            roster=correlated_roster,
            case_registry=judging["registry"],
        )


def test_candidate_family_exclusion_and_two_distinct_judge_families_are_enforced(
        tmp_path):
    uuids = iter([
        uuid.UUID(CASE_ID.removeprefix("JCASE-")),
        uuid.UUID(CASE_ID_2.removeprefix("JCASE-")),
    ])
    registry = OccurrenceCaseRegistry(
        tmp_path / "private" / "cases.jsonl", {SEED: ITEM},
        uuid_factory=lambda: next(uuids),
    )
    registry.issue_case(
        authoring_seed=SEED, run_id="run-a", execution_id="execution-1",
        candidate_model_snapshot="provider/model-20260711",
        candidate_family="judge-anthropic", response_sha256=RESPONSE_SHA256,
        scoring_occurrence=1,
    )
    document = json.loads(ROSTER_FIXTURE.read_text(encoding="utf-8"))
    roster = FrozenJudgeRoster.from_document(
        document, expected_sha256=canonical_roster_sha256(document)
    )
    with pytest.raises(ValueError, match="candidate_family exclusion"):
        score_followthrough(case(ratings=[rating(JUDGE_A, 3), rating(JUDGE_B, 3)]),
                            roster=roster, case_registry=registry)

    document["judges"][1]["family"] = "judge-anthropic"
    same_family_roster = FrozenJudgeRoster.from_document(
        document, expected_sha256=canonical_roster_sha256(document)
    )
    second_case = registry.issue_case(
        authoring_seed=SEED, run_id="run-a", execution_id="execution-2",
        candidate_model_snapshot="provider/model-20260711",
        candidate_family="candidate-openai", response_sha256=RESPONSE_SHA256,
        scoring_occurrence=2,
    )
    with pytest.raises(ValueError, match="two distinct judge families"):
        score_followthrough(case(
            judge_case_id=second_case,
            ratings=[rating(JUDGE_A, 3), rating(JUDGE_B, 3)],
        ), roster=same_family_roster, case_registry=registry)


@pytest.mark.parametrize("mutation,match", [
    ({"judge_case_id": JUDGE_A}, "JCASE"),
    ({"ratings": [rating("JCASE-123e4567-e89b-42d3-a456-426614174000", 3), rating(JUDGE_B, 3)]}, "JUDGE"),
    ({"ratings": [rating(JUDGE_A, 3), rating(JUDGE_A, 3)]}, "distinct judge identities"),
])
def test_case_tokens_and_persistent_judge_identities_cannot_be_conflated(
        mutation, match, judging):
    with pytest.raises(ValueError, match=match):
        score(case(**mutation), judging)


def test_rating_cannot_self_declare_family_and_unknown_judges_are_rejected(judging):
    declared = rating(JUDGE_A, 3)
    declared["judge_family"] = "judge-anthropic"
    with pytest.raises(ValueError, match="must not self-declare judge_family"):
        score(case(ratings=[declared, rating(JUDGE_B, 3)]), judging)
    with pytest.raises(ValueError, match="unknown JUDGE"):
        score(case(ratings=[
            rating("JUDGE-123e4567-e89b-42d3-a456-426614174999", 3),
            rating(JUDGE_B, 3),
        ]), judging)


def test_response_hash_must_match_private_occurrence_binding(judging):
    with pytest.raises(ValueError, match="response hash does not match"):
        score(case(response_sha256="f" * 64), judging)


def test_pious_and_harsh_raw_ratings_are_fail_closed(judging):
    with pytest.raises(ValueError, match="pious-language.*at most 1"):
        score(case(ratings=[
            rating(JUDGE_A, 3, "sentimental",
                   pious_language_without_action=True,
                   positive_duty_completed=False),
            rating(JUDGE_B, 1, "sentimental"),
        ]), judging)
    with pytest.raises(ValueError, match="harsh.*at most 1"):
        score(case(ratings=[
            rating(JUDGE_A, 4, "harsh"),
            rating(JUDGE_B, 1, "harsh"),
        ]), judging)


def test_irr_audit_uses_raw_ratings_and_reports_disagreement_counts(judging):
    assert judging["issue"](occurrence=2) == CASE_ID_2
    records = [
        score(case(), judging),
        score(case(
            judge_case_id=CASE_ID_2,
            ratings=[
                rating(JUDGE_A, 2, "none",
                       positive_duty_completed=False),
                rating(JUDGE_B, 2, "none",
                       positive_duty_completed=False),
            ],
        ), judging),
    ]
    audit = irr_audit(records)
    assert audit == {
        "n_cases": 2,
        "n_raw_rating_pairs": 2,
        "exact_score_agreement": 0.5,
        "within_one_score_agreement": 1.0,
        "failure_pole_agreement": 1.0,
        "score_difference_counts": {"0": 1, "1": 1},
        "roster_sha256": judging["roster"].sha256,
        "human_validation_claimed": False,
    }
