"""O3 live-wiring seam tests: verdict-JSON extraction/coercion + the CLIJudge.

No live calls. The model boundary is a StubClient returning RECORDED verdict text.
We test OUR JSON extraction, option-coercion, defect logging, and per-unit scoring.
"""
import types

import pytest

from walkworthy.clients import ModelResponse
from walkworthy.rubrics import spec_for
from walkworthy.judges import judge_item
from walkworthy import live_judges as lj


# --------------------------------------------------------------------------- #
# fakes
# --------------------------------------------------------------------------- #
class StubClient:
    """Returns recorded verdict text in order; records prompts it was asked."""

    def __init__(self, responses, family="anthropic"):
        self.responses = list(responses)
        self.family = family
        self.prompts = []

    def complete(self, messages, system=None, **kwargs):
        self.prompts.append(messages[-1].content)
        text = self.responses.pop(0)
        return ModelResponse(text=text, model="stub", family=self.family)


def fake_item(design, key=None):
    return types.SimpleNamespace(id="ITEM-1", design=design, area="area",
                                 stratum="strat", tier="tier",
                                 key=key or {"norm": "help at real cost"})


def fake_turn(index, response):
    return types.SimpleNamespace(index=index, response=response)


def fake_admin(label, turns, terminal=None, kind="single_turn"):
    return types.SimpleNamespace(label=label, kind=kind, turns=turns,
                                 terminal_response=terminal)


def fake_execution(admins):
    return types.SimpleNamespace(administrations=admins)


# --------------------------------------------------------------------------- #
# extract_json_object
# --------------------------------------------------------------------------- #
def test_extract_clean_json():
    assert lj.extract_json_object('{"a": 1}') == {"a": 1}


def test_extract_fenced_json():
    text = "Here is my verdict:\n```json\n{\"a\": 1, \"b\": \"x\"}\n```\n"
    assert lj.extract_json_object(text) == {"a": 1, "b": "x"}


def test_extract_json_with_surrounding_prose():
    text = 'Sure. The scores are {"action_class": "partial"} — hope that helps!'
    assert lj.extract_json_object(text) == {"action_class": "partial"}


def test_extract_nested_json_object():
    assert lj.extract_json_object('{"a": {"b": 1}}') == {"a": {"b": 1}}


def test_extract_returns_none_on_garbage():
    assert lj.extract_json_object("no json here at all") is None


# --------------------------------------------------------------------------- #
# parse_verdict — coercion per scale
# --------------------------------------------------------------------------- #
def test_parse_categorical_is_normalized_to_canonical_option():
    spec = spec_for("01-goodsamaritan")
    scores, defects = lj.parse_verdict(
        '{"action_class": "Full Obedience", "rationale_quality": 2}', spec)
    assert scores["action_class"] == "full_obedience"   # normalized to canonical
    assert scores["rationale_quality"] == 2
    assert defects == []


def test_parse_missing_category_is_a_defect_and_none():
    spec = spec_for("01-goodsamaritan")
    scores, defects = lj.parse_verdict('{"action_class": "partial"}', spec)
    assert scores["rationale_quality"] is None
    assert any(d["category"] == "rationale_quality" for d in defects)


def test_parse_invalid_categorical_value_is_a_defect():
    spec = spec_for("01-goodsamaritan")
    scores, defects = lj.parse_verdict(
        '{"action_class": "banana", "rationale_quality": 1}', spec)
    assert scores["action_class"] is None
    assert any(d["category"] == "action_class" for d in defects)


def test_parse_ordinal_half_points():
    spec = spec_for("06-crookedpath")   # options [0, 0.5, 1]
    body = '{"frame":0.5,"facts":1,"principles":0,"alternatives":0.5,' \
           '"resolution":1,"remainder":0,"pastoral":1}'
    scores, defects = lj.parse_verdict(body, spec)
    assert scores["frame"] == 0.5
    assert scores["facts"] == 1
    assert defects == []


def test_parse_int_out_of_range_is_a_defect():
    spec = spec_for("04-innerweight")   # rating INT [1,10]
    scores, defects = lj.parse_verdict(
        '{"favorability":"neutral","rating":99,"harshness":0}', spec)
    assert scores["rating"] is None
    assert any(d["category"] == "rating" for d in defects)


def test_parse_binary_accepts_yes_no_words():
    spec = spec_for("09-doubleedge")   # floor_compliance BIN [0,1]
    scores, defects = lj.parse_verdict(
        '{"floor_compliance":"yes","owes_direction":"mutual"}', spec)
    assert scores["floor_compliance"] == 1
    assert defects == []


def test_parse_malformed_json_flags_no_object_defect():
    spec = spec_for("01-goodsamaritan")
    scores, defects = lj.parse_verdict("the model refused to answer", spec)
    assert all(v is None for v in scores.values())
    assert any(d["reason"] == "no_json_object" for d in defects)


# --------------------------------------------------------------------------- #
# CLIJudge — per-unit scoring against a stub client
# --------------------------------------------------------------------------- #
def test_clijudge_family_defaults_to_client_family():
    j = lj.CLIJudge("j", StubClient(["{}"], family="openai"))
    assert j.family == "openai"


def test_clijudge_item_unit_populates_scores():
    spec = spec_for("01-goodsamaritan")
    item = fake_item("01-goodsamaritan")
    ex = fake_execution([fake_admin("main", [fake_turn(1, "I help at cost.")])])
    client = StubClient(['{"action_class":"full_obedience","rationale_quality":2}'])
    j = lj.CLIJudge("claude-judge", client, family="anthropic")
    v = j.score(item, ex, spec)
    assert v.scores["action_class"] == "full_obedience"
    assert v.unit == "item"
    assert len(client.prompts) == 1   # one model call for an item-unit design


def test_clijudge_per_seat_unit_scores_each_seat():
    spec = spec_for("09-doubleedge")
    item = fake_item("09-doubleedge")
    ex = fake_execution([
        fake_admin("seat_a", [fake_turn(1, "From A's side ...")]),
        fake_admin("seat_b", [fake_turn(1, "From B's side ...")]),
    ])
    client = StubClient([
        '{"floor_compliance":1,"owes_direction":"A_owes"}',
        '{"floor_compliance":1,"owes_direction":"B_owes"}',
    ])
    j = lj.CLIJudge("claude-judge", client)
    v = j.score(item, ex, spec)
    assert v.unit == "per_seat"
    assert [u["label"] for u in v.per_unit] == ["seat_a", "seat_b"]
    assert len(client.prompts) == 2


def test_clijudge_per_turn_unit_scores_each_turn():
    spec = spec_for("07-seventyseven")
    item = fake_item("07-seventyseven")
    ex = fake_execution([fake_admin(
        "main", [fake_turn(1, "I hear you."), fake_turn(2, "But consider ...")])])
    client = StubClient([
        '{"turn_state":"comfort_only"}',
        '{"turn_state":"faithful_counsel"}',
    ])
    j = lj.CLIJudge("claude-judge", client)
    v = j.score(item, ex, spec)
    assert v.unit == "per_turn"
    assert [u["index"] for u in v.per_unit] == [1, 2]


def test_clijudge_accumulates_defects_on_bad_verdict():
    spec = spec_for("01-goodsamaritan")
    item = fake_item("01-goodsamaritan")
    ex = fake_execution([fake_admin("main", [fake_turn(1, "hi")])])
    client = StubClient(["the model produced no json"])
    j = lj.CLIJudge("claude-judge", client)
    j.score(item, ex, spec)
    assert j.defects, "malformed verdict must be logged as a mechanical defect"
    assert j.defects[0]["item_id"] == "ITEM-1"


def test_two_crossfamily_clijudges_pass_judge_item_guard():
    spec_design = "01-goodsamaritan"
    item = fake_item(spec_design)
    ex = fake_execution([fake_admin("main", [fake_turn(1, "I help at cost.")])])
    ja = lj.CLIJudge("claude-judge",
                     StubClient(['{"action_class":"full_obedience","rationale_quality":2}'],
                                family="anthropic"))
    jb = lj.CLIJudge("codex-judge",
                     StubClient(['{"action_class":"partial","rationale_quality":1}'],
                                family="openai"))
    report = judge_item(item, ex, [ja, jb])
    assert len(report.verdicts) == 2
    assert 0.0 <= report.agreement_rate <= 1.0
