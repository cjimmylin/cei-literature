"""FR-16/17 W1 tie-breaker: full-cell routing, prompt identity, 2-of-3."""
from types import SimpleNamespace

from walkworthy.judges import assemble_rubric_prompt
from walkworthy.rubrics import CAT, ORD, Category, spec_for
from walkworthy.tiebreak import (TIEBREAKER_MODEL, apply_group_result,
                                 build_adjudicated_verdict, group_disagreements,
                                 is_own_family_sut, merge_reexecution,
                                 resolve_three, rubric_prompt_for_unit, scoring_unit,
                                 run_tiebreak, validate_transcript_contract)


def _item(design="01-goodsamaritan"):
    return SimpleNamespace(id="WW-X", design=design, area="A", stratum="a",
                           tier="core", key={"anchor": "keyed anchor"}, extras={})


def _rec(design="01-goodsamaritan", model="openai/gpt-4.1"):
    return {
        "item_id": "WW-X", "design": design, "model": model,
        "administrations": [{"label": "main", "response": "answer"}],
        "judge_report": {"disagreements": []},
    }


def test_tiebreaker_model_is_frozen_explicit_slug():
    assert TIEBREAKER_MODEL == "mistralai/mistral-large-2512"
    assert is_own_family_sut("mistralai/mistral-large-2512")
    assert not is_own_family_sut("openai/gpt-4.1")


def test_item_prompt_is_byte_identical_to_frozen_pair_prompt():
    item = _item()
    rec = _rec()

    actual = rubric_prompt_for_unit(item, rec, "action_class")
    expected = assemble_rubric_prompt(item, spec_for(item.design), "answer",
                                      references=None, unit_label=None)

    assert actual == expected


def test_per_turn_and_terminal_units_reuse_exact_original_labels():
    item = _item("07-seventyseven")
    rec = _rec("07-seventyseven")
    rec["administrations"] = [{
        "label": "main", "response": "first",
        "turns": [{"index": 1, "response": "turn one"},
                  {"index": 2, "response": "turn two"}],
        "terminal_response": "final note",
    }]

    assert scoring_unit(rec, spec_for(item.design), "2:turn_state") == (
        "2", "turn two", "turn 2")
    assert scoring_unit(rec, spec_for(item.design), "3:turn_state") == (
        "3", "final note", "terminal artifact")


def test_group_disagreements_calls_once_per_record_scoring_unit():
    rec = _rec("06-crookedpath")
    rec["judge_report"]["disagreements"] = [
        {"cell": "frame", "needs_adjudication": True},
        {"cell": "facts", "needs_adjudication": True},
        {"cell": "ignored", "needs_adjudication": False},
    ]

    groups = group_disagreements([rec])

    assert len(groups) == 1
    assert [c["cell"] for c in groups[0]["cells"]] == ["frame", "facts"]


def test_two_of_three_categorical_resolution_and_contested_result():
    cat = Category("x", CAT, ["a", "b", "c"])
    assert resolve_three(cat, "a", "b", "b") == ("b", "resolved")
    assert resolve_three(cat, "a", "b", "c") == (None, "contested")


def test_numeric_two_of_three_uses_only_the_unique_agreeing_pair():
    cat = Category("x", ORD, [0, 0.5, 1])
    assert resolve_three(cat, 0, 1, 0) == (0, "resolved")
    # 0~0.5 and 0.5~1 are both within tolerance, but imply different means. The
    # framework supplies no chooser, so this edge is surfaced rather than guessed.
    assert resolve_three(cat, 0, 1, 0.5) == (None, "ambiguous_tolerance")


def test_apply_result_preserves_pair_and_builds_separate_adjudicated_verdict():
    rec = _rec()
    rec["judge_report"] = {
        "verdicts": [
            {"judge": "j0", "family": "openai", "unit": "item", "scores": {
                "action_class": "full_obedience", "rationale_quality": 1}},
            {"judge": "j1", "family": "google", "unit": "item", "scores": {
                "action_class": "objective_first", "rationale_quality": 1}},
        ],
        "disagreements": [{"cell": "action_class",
                            "values": ["full_obedience", "objective_first"],
                            "scale": "categorical", "adjudicated": None,
                            "needs_adjudication": True}],
    }
    group = group_disagreements([rec])[0]

    out = apply_group_result(rec, group, {"action_class": "objective_first",
                                         "rationale_quality": 2})
    adjudicated = build_adjudicated_verdict(out)

    assert rec["judge_report"]["disagreements"][0]["needs_adjudication"] is True
    resolved = out["judge_report"]["disagreements"][0]
    assert resolved["adjudicated"] == "objective_first"
    assert resolved["needs_adjudication"] is False
    assert adjudicated["scores"] == {"action_class": "objective_first",
                                     "rationale_quality": 1}


def test_own_family_group_routes_cells_to_part_b_without_third_scores():
    rec = _rec(model=TIEBREAKER_MODEL)
    rec["judge_report"]["disagreements"] = [
        {"cell": "action_class", "values": ["full_obedience", "objective_first"],
         "scale": "categorical", "adjudicated": None, "needs_adjudication": True}
    ]
    group = group_disagreements([rec])[0]

    out = apply_group_result(rec, group, None)

    cell = out["judge_report"]["disagreements"][0]
    assert group["route"] == "part_b_own_family"
    assert cell["needs_adjudication"] is True
    assert cell["adjudication_status"] == "part_b_own_family"


def test_reexecution_merge_requires_exact_key_coverage_and_replaces_02_07_only():
    old02 = _rec("02-twomasters"); old02["item_id"] = "02-X"
    old01 = _rec("01-goodsamaritan"); old01["item_id"] = "01-X"
    new02 = _rec("02-twomasters"); new02["item_id"] = "02-X"
    new02["marker"] = "new"

    merged = merge_reexecution([old01, old02], [new02])

    assert merged[0] == old01
    assert merged[1]["marker"] == "new"
    try:
        merge_reexecution([old01, old02], [])
    except ValueError as exc:
        assert "coverage mismatch" in str(exc)
    else:
        raise AssertionError("missing re-execution key did not fail loud")


def test_transcript_contract_requires_every_turn_and_terminal_response():
    rec = _rec("07-seventyseven")
    rec["administrations"] = [{
        "label": "main", "n_turns": 2,
        "turns": [{"index": 1, "response": "r1"}, {"index": 2, "response": "r2"}],
        "terminal_user_text": "final ask", "terminal_response": "final response",
    }]
    assert validate_transcript_contract([rec]) == {"records": 1, "turns": 2,
                                                   "terminals": 1}
    rec["administrations"][0]["turns"][1]["response"] = ""
    try:
        validate_transcript_contract([rec])
    except ValueError as exc:
        assert "missing persisted response" in str(exc)
    else:
        raise AssertionError("missing response did not fail loud")


def test_runner_checkpoints_units_and_never_calls_model_for_own_family(tmp_path):
    def pending(model):
        rec = _rec(model=model)
        rec["judge_report"] = {
            "verdicts": [
                {"judge": "j0", "family": "openai", "unit": "item", "scores": {
                    "action_class": "full_obedience", "rationale_quality": 1}},
                {"judge": "j1", "family": "google", "unit": "item", "scores": {
                    "action_class": "objective_first", "rationale_quality": 1}},
            ],
            "disagreements": [{"cell": "action_class",
                                "values": ["full_obedience", "objective_first"],
                                "scale": "categorical", "adjudicated": None,
                                "needs_adjudication": True}],
        }
        return rec

    class Client:
        def __init__(self):
            self.calls = 0

        def complete(self, messages, system=None):
            self.calls += 1
            return SimpleNamespace(text=(
                '{"action_class":"objective_first","rationale_quality":1}'))

    client = Client()
    checkpoint = tmp_path / "events.jsonl"
    records, summary = run_tiebreak(
        [pending("openai/gpt-4.1"), pending(TIEBREAKER_MODEL)],
        {"WW-X": _item()}, client, checkpoint)

    assert client.calls == 1
    assert summary["tie_breaker_units"] == 1
    assert summary["own_family_units"] == 1
    assert records[0]["judge_report"]["adjudicated_verdict"]["scores"][
        "action_class"] == "objective_first"
    assert records[1]["judge_report"]["adjudicated_verdict"]["scores"][
        "action_class"] is None

    resumed = Client()
    _, summary2 = run_tiebreak(
        [pending("openai/gpt-4.1"), pending(TIEBREAKER_MODEL)],
        {"WW-X": _item()}, resumed, checkpoint)
    assert resumed.calls == 0
    assert summary2["checkpointed_units"] == 2
