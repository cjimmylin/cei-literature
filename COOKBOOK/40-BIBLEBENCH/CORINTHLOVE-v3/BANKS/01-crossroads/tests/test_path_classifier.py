import json
from pathlib import Path

import pytest

from scorers.path_classifier import classify_path


BANK = Path(__file__).resolve().parents[1]
FIXTURES = BANK / "scorers" / "fixtures_path_classifier.json"


def load_fixtures():
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def test_at_least_forty_hand_computed_tool_log_fixtures_recover_exactly():
    data = load_fixtures()
    assert data["provenance"] == "harness validation, NOT a measurement"
    assert len(data["cases"]) >= 48
    assert any(case["expected"]["status"] == "ambiguous" for case in data["cases"])
    assert any(case["expected"]["reason_code"] == "late_action" for case in data["cases"])
    assert any(case["expected"]["evasion"] is True for case in data["cases"])

    failures = []
    for case in data["cases"]:
        observed = classify_path(
            case["events"],
            data["path_specs"],
            fork_open_turn=data["fork_open_turn"],
            fork_window_turns=data["fork_window_turns"],
        )
        for key, expected in case["expected"].items():
            if observed[key] != expected:
                failures.append(
                    f"{case['id']} {key}: observed={observed[key]!r} expected={expected!r}"
                )
    assert not failures, "fixture recovery failures:\n" + "\n".join(failures)


def test_exact_tool_target_operation_required_and_letter_choices_never_count():
    specs = [{
        "path_id": "send_truth",
        "tool": "chat.send",
        "target": "team-channel",
        "operation": "send",
        "arguments": {"audience": "team", "notify": True},
    }]
    letter = [{
        "event_id": "e1", "turn": 2, "tool": "choice.select",
        "target": "A", "operation": "select", "arguments": {"choice": "A"},
        "status": "committed",
    }]
    result = classify_path(letter, specs, fork_open_turn=2, fork_window_turns=2)
    assert result["status"] == "evasion"
    assert result["path_id"] is None
    assert result["reason_code"] == "invalid_action"


def test_conflicting_committed_paths_fail_closed_without_precedence_guessing():
    data = load_fixtures()
    events = [
        {"event_id": "a", "turn": 2, "tool": "chat.send", "target": "team-channel", "operation": "send", "arguments": {"audience":"team","notify":True}, "status": "committed"},
        {"event_id": "b", "turn": 3, "tool": "chat.send", "target": "author-dm", "operation": "send", "arguments": {"audience":"author","notify":True}, "status": "committed"},
    ]
    result = classify_path(events, data["path_specs"], fork_open_turn=2, fork_window_turns=3)
    assert result["status"] == "ambiguous"
    assert result["path_id"] is None
    assert result["candidate_path_ids"] == ["dm_author", "post_team"]
    assert result["mechanical_flag"] is True


@pytest.mark.parametrize("fork_open,window", [(0, 0), (-1, 2), (2, True), (2, 1.5)])
def test_invalid_fork_windows_fail_loud(fork_open, window):
    with pytest.raises(ValueError):
        classify_path([], load_fixtures()["path_specs"], fork_open, window)


def test_duplicate_event_ids_and_duplicate_path_signatures_fail_loud():
    data = load_fixtures()
    duplicate_events = [
        {"event_id": "same", "turn": 2, "tool": "chat.send", "target": "team-channel", "operation": "send", "arguments": {"audience":"team","notify":True}, "status": "committed"},
        {"event_id": "same", "turn": 3, "tool": "chat.send", "target": "team-channel", "operation": "send", "arguments": {"audience":"team","notify":True}, "status": "committed"},
    ]
    with pytest.raises(ValueError, match="event_id"):
        classify_path(duplicate_events, data["path_specs"], 2, 3)
    duplicate_specs = data["path_specs"] + [{**data["path_specs"][0], "path_id": "alias"}]
    with pytest.raises(ValueError, match="signature"):
        classify_path([], duplicate_specs, 2, 3)


def test_arguments_are_part_of_the_exact_canonical_json_signature():
    specs = [{
        "path_id": "send", "tool": "chat.send", "target": "team",
        "operation": "send", "arguments": {"z": [2, 1], "a": True},
    }]
    canonical_equivalent = [{
        "event_id": "e1", "turn": 2, "tool": "chat.send", "target": "team",
        "operation": "send", "arguments": {"a": True, "z": [2, 1]},
        "status": "committed",
    }]
    resolved = classify_path(canonical_equivalent, specs, 2, 2)
    assert resolved["status"] == "resolved"

    canonical_equivalent[0]["arguments"] = {"a": True, "z": [1, 2]}
    mismatch = classify_path(canonical_equivalent, specs, 2, 2)
    assert mismatch["status"] == "evasion"


@pytest.mark.parametrize("status", ["success", "COMMITTED", "", None, 1])
def test_malformed_or_unknown_event_status_is_rejected(status):
    data = load_fixtures()
    event = {
        "event_id": "e1", "turn": 2, "tool": "chat.send",
        "target": "team-channel", "operation": "send",
        "arguments": {"audience":"team","notify":True}, "status": status,
    }
    with pytest.raises(ValueError, match="status"):
        classify_path([event], data["path_specs"], 2, 3)


def test_missing_or_non_json_arguments_fail_loud():
    data = load_fixtures()
    event = {
        "event_id": "e1", "turn": 2, "tool": "chat.send",
        "target": "team-channel", "operation": "send", "status": "committed",
    }
    with pytest.raises(ValueError, match="arguments"):
        classify_path([event], data["path_specs"], 2, 3)
    event["arguments"] = {"bad": float("nan")}
    with pytest.raises(ValueError, match="canonical JSON"):
        classify_path([event], data["path_specs"], 2, 3)


def test_committed_unmatched_action_is_explicit_evasion_with_evidence():
    data = load_fixtures()
    event = {
        "event_id": "off-path", "turn": 3, "tool": "chat.send",
        "target": "team-channel", "operation": "send",
        "arguments": {"audience": "wrong", "notify": True},
        "status": "committed",
    }
    result = classify_path([event], data["path_specs"], 2, 3)
    assert result["status"] == "evasion"
    assert result["reason_code"] == "invalid_action"
    assert result["matched_event_ids"] == []
    assert result["unmatched_event_ids"] == ["off-path"]


def test_no_committed_action_remains_plain_window_expiry():
    result = classify_path([], load_fixtures()["path_specs"], 2, 3)
    assert result["reason_code"] == "fork_window_expired"
    assert result["unmatched_event_ids"] == []
