"""Exhaustive mechanical outcome replay and fail-closed mutation probes."""

from collections import Counter
from copy import deepcopy

from audits.schema_balance import parse_jsonl_bytes, read_artifact_bytes
from scoring.mechanical import score_record
from tablets_constants import COMMANDMENT_SPECS


def _load_rows(tablets_root, public_rows, private_rows):
    injected = public_rows is not None or private_rows is not None
    if public_rows is None or private_rows is None:
        artifacts, _ = read_artifact_bytes(tablets_root=tablets_root)
        if public_rows is None:
            public_rows = parse_jsonl_bytes(artifacts["public"], "public")
        if private_rows is None:
            private_rows = parse_jsonl_bytes(artifacts["private"], "private")
    if (
        type(public_rows) is not list
        or type(private_rows) is not list
        or not all(type(row) is dict for row in public_rows + private_rows)
    ):
        raise ValueError("mechanical replay projections must be lists of objects")
    if len(public_rows) != 636 or len(private_rows) != 636:
        raise ValueError("mechanical replay projection count drift")
    if [row["id"] for row in public_rows] != [row["id"] for row in private_rows]:
        raise ValueError("mechanical replay public/private identity binding drift")
    return public_rows, private_rows, ("INJECTED_ROWS" if injected else "DISK")


def _valid_wrong_codes(expected):
    catalog = [COMMANDMENT_SPECS[index]["code"] for index in range(1, 11)]
    for first_index, first in enumerate(catalog):
        for second in catalog[first_index + 1 :]:
            candidate = [first, second]
            if set(candidate) != set(expected):
                return candidate
    raise AssertionError("recognition catalog lacks a valid wrong response")


def _must_reject(label, operation):
    try:
        operation()
    except ValueError:
        return True
    raise AssertionError("mechanical mutation was accepted: %s" % label)


def audit_mechanical_replay(
    tablets_root=None,
    public_rows=None,
    private_rows=None,
):
    """Replay every frozen choice plus control and mutation probes."""
    public, private, source = _load_rows(
        tablets_root, public_rows, private_rows
    )
    outcome_counts = Counter()
    comprehension_correct = 0
    comprehension_incorrect = 0
    recognition_correct = 0
    recognition_incorrect = 0
    panel_not_run_ids = set()
    c10_excluded_ids = set()

    for pub, gold in zip(public, private):
        representative = None
        if pub["record_type"] == "recognition":
            correct = score_record(
                pub,
                gold,
                {"selected_duty_codes": list(reversed(gold["expected_duty_codes"]))},
            )
            if correct["recognition_correct"] is not True:
                raise AssertionError("recognition correct replay failed")
            recognition_correct += 1
            wrong = score_record(
                pub,
                gold,
                {"selected_duty_codes": _valid_wrong_codes(gold["expected_duty_codes"])},
            )
            if wrong["recognition_correct"] is not False:
                raise AssertionError("recognition valid-wrong replay failed")
            recognition_incorrect += 1
            representative = correct
        else:
            for action_id, expected in gold["choice_map"].items():
                result = score_record(
                    pub, gold, {"selected_action_id": action_id}
                )
                if (
                    result["outcome_class"] != expected["outcome_class"]
                    or result["served_commandment"]
                    != expected["served_commandment"]
                ):
                    raise AssertionError("mechanical action replay disagrees with choice map")
                outcome_counts[result["outcome_class"]] += 1
                if representative is None:
                    representative = result
            if pub["record_type"] == "comprehension":
                correct = score_record(
                    pub,
                    gold,
                    {"selected_action_id": gold["expected_selected_action_id"]},
                )
                if correct["capability_correct"] is not True:
                    raise AssertionError("comprehension correct replay failed")
                comprehension_correct += 1
                wrong_action = next(
                    action_id
                    for action_id in gold["choice_map"]
                    if action_id != gold["expected_selected_action_id"]
                )
                wrong = score_record(
                    pub, gold, {"selected_action_id": wrong_action}
                )
                if wrong["capability_correct"] is not False:
                    raise AssertionError("comprehension valid-wrong replay failed")
                comprehension_incorrect += 1

        if gold["panel_status"] != "NOT_RUN" or representative["panel_status"] != "NOT_RUN":
            raise AssertionError("mechanical replay promoted unrun panel evidence")
        panel_not_run_ids.add(pub["id"])
        if 10 in pub["commandment"]:
            if (
                representative["bt_eligible"] is not False
                or representative["triad_eligible"] is not False
                or representative["exclusion_reason"] != "C10_ADVICE_CONFLICT"
            ):
                raise AssertionError("C10 exclusion replay failed")
            c10_excluded_ids.add(pub["id"])

    expected_outcomes = {
        "duty_a": 591,
        "duty_b": 591,
        "paralysis": 591,
        "third_way": 16,
    }
    if dict(outcome_counts) != expected_outcomes:
        raise AssertionError("mechanical outcome replay count drift")
    if (
        comprehension_correct != 45
        or comprehension_incorrect != 45
        or recognition_correct != 45
        or recognition_incorrect != 45
        or len(panel_not_run_ids) != 636
        or len(c10_excluded_ids) != 116
    ):
        raise AssertionError("mechanical control/evidence replay count drift")

    action_index = next(
        index
        for index, row in enumerate(public)
        if row["record_type"] == "adjudication"
    )
    action_public = public[action_index]
    action_private = private[action_index]
    valid_action = next(iter(action_private["choice_map"]))
    recognition_index = next(
        index
        for index, row in enumerate(public)
        if row["record_type"] == "recognition"
    )
    recognition_public = public[recognition_index]
    recognition_private = private[recognition_index]
    forged_private = deepcopy(action_private)
    forged_private["bt_eligible"] = not forged_private["bt_eligible"]
    mutations = {
        "extra_response_field": _must_reject(
            "extra_response_field",
            lambda: score_record(
                action_public,
                action_private,
                {"selected_action_id": valid_action, "extra": True},
            ),
        ),
        "unknown_action": _must_reject(
            "unknown_action",
            lambda: score_record(
                action_public,
                action_private,
                {"selected_action_id": "UNKNOWN_ACTION"},
            ),
        ),
        "forged_private_semantics": _must_reject(
            "forged_private_semantics",
            lambda: score_record(
                action_public,
                forged_private,
                {"selected_action_id": valid_action},
            ),
        ),
        "unknown_duty_code": _must_reject(
            "unknown_duty_code",
            lambda: score_record(
                recognition_public,
                recognition_private,
                {
                    "selected_duty_codes": [
                        recognition_private["expected_duty_codes"][0],
                        "UNKNOWN_DUTY_CODE",
                    ]
                },
            ),
        ),
    }
    return {
        "audit": "TABLETS_MECHANICAL_REPLAY",
        "schema_version": "tablets-structural-audit.v1",
        "status": "PASS",
        "source": source,
        "sections": {
            "valid_replay": {
                "status": "PASS",
                **expected_outcomes,
                "comprehension_correct": comprehension_correct,
                "comprehension_valid_incorrect": comprehension_incorrect,
                "recognition_correct": recognition_correct,
                "recognition_valid_incorrect": recognition_incorrect,
            },
            "evidence_guards": {
                "status": "PASS",
                "panel_not_run_rows": len(panel_not_run_ids),
                "c10_excluded_rows": len(c10_excluded_ids),
            },
            "mutation_rejections": {
                "status": "PASS",
                "rejection_count": len(mutations),
                **mutations,
            },
        },
    }


__all__ = ["audit_mechanical_replay"]
