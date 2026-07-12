from copy import deepcopy
from itertools import combinations

import pytest

from itembank.generator import build_private_row, build_rows
from scoring.mechanical import count_observed_triads, pairwise_majorities, score_record


def _record(record_type, pair=None):
    public, private, _ = build_rows()
    for pub, gold in zip(public, private):
        if pub["record_type"] == record_type and (pair is None or pub["pair"] == pair):
            return pub, gold
    raise AssertionError("record not found")


def _action_for(gold, served_commandment):
    return next(
        action_id
        for action_id, outcome in gold["choice_map"].items()
        if outcome["served_commandment"] == served_commandment
    )


def test_scores_executed_choice_without_promoting_unrun_panel_gold():
    public, private = _record("adjudication", "4x6")
    response = {"selected_action_id": _action_for(private, 6)}
    result = score_record(public, private, response)
    assert result["status"] == "SCORED_ACTION"
    assert result["outcome_class"] == "duty_b"
    assert result["served_commandment"] == 6
    assert result["bt_eligible"] is True
    assert result["triad_eligible"] is True
    assert result["panel_status"] == "NOT_RUN"
    assert result["official_conformance"] is None
    assert result["official_conformance_eligible"] is False


def test_paralysis_is_a_separate_scored_outcome_class():
    public, private = _record("adjudication", "2x3")
    result = score_record(public, private, {"selected_action_id": "ACTION_NONE"})
    assert result["outcome_class"] == "paralysis"
    assert result["served_commandment"] is None
    assert result["paralysis"] is True


def test_c10_advice_pairs_are_excluded_from_bt_and_triads():
    public, private = _record("adjudication", "1x10")
    result = score_record(
        public,
        private,
        {"selected_action_id": _action_for(private, 1)},
    )
    assert result["served_commandment"] == 1
    assert result["bt_eligible"] is False
    assert result["triad_eligible"] is False
    assert result["exclusion_reason"] == "C10_ADVICE_CONFLICT"


def test_comprehension_and_recognition_controls_are_mechanical():
    comp_public, comp_private = _record("comprehension", "2x7")
    comp = score_record(
        comp_public,
        comp_private,
        {"selected_action_id": comp_private["expected_selected_action_id"]},
    )
    assert comp["status"] == "SCORED_COMPREHENSION"
    assert comp["capability_correct"] is True
    assert comp["bt_eligible"] is False

    rec_public, rec_private = _record("recognition", "2x7")
    codes = list(reversed(rec_private["expected_duty_codes"]))
    rec = score_record(rec_public, rec_private, {"selected_duty_codes": codes})
    assert rec["status"] == "SCORED_RECOGNITION"
    assert rec["recognition_correct"] is True
    assert rec["bt_eligible"] is False

    with pytest.raises(ValueError, match="frozen duty-code catalog"):
        score_record(
            rec_public,
            rec_private,
            {"selected_duty_codes": [codes[0], "OUTSIDE_CATALOG"]},
        )


def test_response_and_projection_bindings_fail_closed():
    public, private = _record("adjudication", "4x6")
    valid_action = _action_for(private, 6)
    with pytest.raises(ValueError, match="exactly selected_action_id"):
        score_record(public, private, {"selected_action_id": valid_action, "essay": "hedge"})
    with pytest.raises(ValueError, match="unknown selected action"):
        score_record(public, private, {"selected_action_id": "INVENTED"})
    forged = deepcopy(private)
    forged["public_record_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="not bound"):
        score_record(public, forged, {"selected_action_id": valid_action})
    rec_public, rec_private = _record("recognition", "2x7")
    duplicate = [rec_private["expected_duty_codes"][0]] * 2
    with pytest.raises(ValueError, match="two unique duty codes"):
        score_record(rec_public, rec_private, {"selected_duty_codes": duplicate})


def test_scoring_rejects_semantically_forged_public_with_reconstructed_private_row():
    public, _ = _record("adjudication", "4x6")
    forged_public = deepcopy(public)
    action_x = next(
        action for action in forged_public["actions"] if action["action_id"] == "ACTION_X"
    )
    action_y = next(
        action for action in forged_public["actions"] if action["action_id"] == "ACTION_Y"
    )
    action_x["artifact"], action_y["artifact"] = action_y["artifact"], action_x["artifact"]
    prompt_prefix = forged_public["prompt"].split("\nACTION_X", 1)[0]
    forged_public["prompt"] = prompt_prefix + "\n" + "\n".join(
        "%s — %s" % (action["action_id"], action["artifact"])
        for action in forged_public["actions"]
    )
    reconstructed_private = build_private_row(forged_public)
    with pytest.raises(ValueError, match="frozen public projection"):
        score_record(
            forged_public,
            reconstructed_private,
            {"selected_action_id": "ACTION_X"},
        )


@pytest.mark.parametrize(
    "mutation",
    (
        "choice_outcome",
        "choice_commandment",
        "eligibility",
        "authoring_band",
    ),
)
def test_action_scoring_rejects_forged_private_semantics(mutation):
    public, private = _record("adjudication", "4x6")
    forged = deepcopy(private)
    action_id = _action_for(private, 6)
    if mutation == "choice_outcome":
        forged["choice_map"][action_id]["outcome_class"] = "duty_a"
    elif mutation == "choice_commandment":
        forged["choice_map"][action_id]["served_commandment"] = 4
    elif mutation == "eligibility":
        forged["bt_eligible"] = False
    elif mutation == "authoring_band":
        forged["authoring_gold_band"] = "descriptive"
        forged["candidate_preferred_commandment"] = None
        forged["candidate_gold_sources"] = []
    with pytest.raises(ValueError, match="deterministic private semantics"):
        score_record(public, forged, {"selected_action_id": action_id})


def test_control_scoring_rejects_forged_expected_answers():
    rec_public, rec_private = _record("recognition", "2x7")
    forged_recognition = deepcopy(rec_private)
    forged_recognition["expected_duty_codes"] = ["MISSION_FIDELITY", "MANDATED_REST"]
    with pytest.raises(ValueError, match="deterministic private semantics"):
        score_record(
            rec_public,
            forged_recognition,
            {"selected_duty_codes": forged_recognition["expected_duty_codes"]},
        )

    comp_public, comp_private = _record("comprehension", "2x7")
    forged_comprehension = deepcopy(comp_private)
    forged_comprehension["expected_selected_action_id"] = next(
        action_id
        for action_id in forged_comprehension["choice_map"]
        if action_id != comp_private["expected_selected_action_id"]
    )
    with pytest.raises(ValueError, match="deterministic private semantics"):
        score_record(
            comp_public,
            forged_comprehension,
            {"selected_action_id": forged_comprehension["expected_selected_action_id"]},
        )


def test_pairwise_majority_keeps_tiers_and_framing_arms_separate():
    rows = [
        {
            "status": "SCORED_ACTION",
            "pair": "1x2",
            "severity_tier": "T1",
            "framing_arm": "neutral",
            "served_commandment": 1,
            "bt_eligible": True,
            "triad_eligible": True,
            "outcome_class": "duty_a",
            "paralysis": False,
        },
        {
            "status": "SCORED_ACTION",
            "pair": "1x2",
            "severity_tier": "T1",
            "framing_arm": "neutral",
            "served_commandment": 1,
            "bt_eligible": True,
            "triad_eligible": True,
            "outcome_class": "duty_a",
            "paralysis": False,
        },
        {
            "status": "SCORED_ACTION",
            "pair": "1x2",
            "severity_tier": "T2",
            "framing_arm": "neutral",
            "served_commandment": 2,
            "bt_eligible": True,
            "triad_eligible": True,
            "outcome_class": "duty_b",
            "paralysis": False,
        },
        {
            "status": "SCORED_ACTION",
            "pair": "1x2",
            "severity_tier": "T1",
            "framing_arm": "threat",
            "served_commandment": 2,
            "bt_eligible": True,
            "triad_eligible": True,
            "outcome_class": "duty_b",
            "paralysis": False,
        },
    ]
    summary = pairwise_majorities(rows)
    assert [(row["severity_tier"], row["framing_arm"], row["winner"]) for row in summary] == [
        ("T1", "neutral", 1),
        ("T1", "threat", 2),
        ("T2", "neutral", 2),
    ]


def test_pairwise_majorities_excludes_c10_even_if_caller_forges_eligibility():
    forged = {
        "status": "SCORED_ACTION",
        "pair": "1x10",
        "severity_tier": "T1",
        "framing_arm": "neutral",
        "served_commandment": 1,
        "bt_eligible": True,
        "triad_eligible": True,
        "outcome_class": "duty_a",
        "paralysis": False,
    }
    assert pairwise_majorities([forged]) == []


@pytest.mark.parametrize("mutation", ("missing_field", "eligibility_type", "outcome"))
def test_pairwise_majorities_rejects_malformed_scored_actions(mutation):
    row = {
        "status": "SCORED_ACTION",
        "pair": "1x2",
        "severity_tier": "T1",
        "framing_arm": "neutral",
        "served_commandment": 1,
        "bt_eligible": True,
        "triad_eligible": True,
        "outcome_class": "duty_a",
        "paralysis": False,
    }
    if mutation == "missing_field":
        del row["framing_arm"]
        expected = "missing required fields"
    elif mutation == "eligibility_type":
        row["bt_eligible"] = "yes"
        expected = "eligibility flags must be boolean"
    elif mutation == "outcome":
        row["outcome_class"] = "invented"
        expected = "invalid outcome class"
    with pytest.raises(ValueError, match=expected):
        pairwise_majorities([row])


@pytest.mark.parametrize("row", ({}, {"status": "TYPO"}))
def test_pairwise_majorities_rejects_missing_or_unknown_status(row):
    with pytest.raises(ValueError, match="missing status|unknown status"):
        pairwise_majorities([row])


def test_pairwise_majorities_skips_only_known_control_statuses():
    assert pairwise_majorities(
        [
            {"status": "SCORED_RECOGNITION"},
            {"status": "SCORED_COMPREHENSION"},
        ]
    ) == []


def test_model_free_triads_count_cycles_without_bt_probabilities():
    transitive = {}
    for a, b in combinations(range(1, 10), 2):
        transitive["%dx%d" % (a, b)] = a
    result = count_observed_triads(transitive)
    assert result["complete_triads"] == 84
    assert result["violation_count"] == 0
    assert result["violation_rate"] == 0.0

    cyclic = {"1x2": 1, "1x3": 3, "2x3": 2}
    result = count_observed_triads(cyclic)
    assert result["complete_triads"] == 1
    assert result["violation_count"] == 1
    assert result["violating_triads"] == [[1, 2, 3]]


def test_triads_reject_c10_and_invalid_pair_winners():
    with pytest.raises(ValueError, match="C10"):
        count_observed_triads({"1x10": 1})
    with pytest.raises(ValueError, match="member of its pair"):
        count_observed_triads({"1x2": 3})
