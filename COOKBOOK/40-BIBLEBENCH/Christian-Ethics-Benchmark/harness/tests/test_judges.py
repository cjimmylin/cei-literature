"""RED: judge layer — rubric prompt assembly, 2 cross-family judges, disagreement
logged (never averaged), per-turn / per-seat units, reference anchoring."""
import pytest

from walkworthy.clients import MockModelClient
from walkworthy.executors import execute_item
from walkworthy.judges import (
    MockJudge,
    Verdict,
    analyze_disagreement,
    assemble_rubric_prompt,
    judge_item,
)
from walkworthy.loader import load_design
from walkworthy.manifest import FIXED_PERMUTATION_SEEDS
from walkworthy.rubrics import DESIGN_RUBRICS, spec_for


def _first(design, benchmark_root, pred=None):
    items = load_design(design, benchmark_root, include_exemplars=False)
    if pred:
        items = [it for it in items if pred(it)]
    return items[0]


def test_rubric_registry_shapes():
    assert set(DESIGN_RUBRICS) >= {f"{i:02d}" for i in range(1, 11)} or len(DESIGN_RUBRICS) == 10
    assert len(spec_for("06-crookedpath").categories) == 7
    names = {c.name for c in spec_for("10-strangergate").categories}
    assert {"treatment", "prudence", "contempt", "duality"} <= names
    assert spec_for("05-ordoamoris").judge_free_primary


def test_rubric_prompt_embeds_key_categories_and_length_correction(benchmark_root):
    it = _first("01-goodsamaritan", benchmark_root)
    prompt = assemble_rubric_prompt(it, spec_for(it.design), response_text="some response")
    assert "action_class" in prompt and "rationale_quality" in prompt
    # the item's own keyed rubric is embedded so the judge scores against the anchor
    assert it.key["keyed_behavior"][:30] in prompt
    assert "length" in prompt.lower()          # length-correction instruction present


def test_rubric_prompt_reference_anchored_for_06(benchmark_root):
    it = _first("06-crookedpath", benchmark_root,
                pred=lambda i: i.extras.get("reference_answers"))
    prompt = assemble_rubric_prompt(it, spec_for(it.design), response_text="resp",
                                    references=it.extras.get("reference_answers"))
    assert "reference" in prompt.lower()


def test_mock_judge_emits_valid_verdict(benchmark_root):
    it = _first("01-goodsamaritan", benchmark_root)
    ex = execute_item(it, MockModelClient("mock-a", seed=1), FIXED_PERMUTATION_SEEDS)
    v = MockJudge("judge-x", family="anthropic").score(it, ex, spec_for(it.design))
    assert isinstance(v, Verdict)
    assert v.scores["action_class"] in \
        {"full_obedience", "partial", "deferral", "objective_first"}
    assert v.scores["rationale_quality"] in {0, 1, 2}


def test_judge_item_two_cross_family_and_no_averaging(benchmark_root):
    it = _first("01-goodsamaritan", benchmark_root)
    ex = execute_item(it, MockModelClient("mock-a", seed=1), FIXED_PERMUTATION_SEEDS)
    judges = [MockJudge("j-anthropic", family="anthropic", seed=1),
              MockJudge("j-openai", family="openai", seed=2)]
    report = judge_item(it, ex, judges)
    assert len(report.verdicts) == 2
    # agreement fraction reported; disagreements logged with BOTH values, no mean
    assert 0.0 <= report.agreement_rate <= 1.0
    for d in report.disagreements:
        assert "values" in d and len(d["values"]) == 2
        assert "mean" not in d and "averaged" not in d


def test_judge_item_rejects_same_family(benchmark_root):
    it = _first("01-goodsamaritan", benchmark_root)
    ex = execute_item(it, MockModelClient("mock-a", seed=1), FIXED_PERMUTATION_SEEDS)
    same = [MockJudge("j1", family="anthropic"), MockJudge("j2", family="anthropic")]
    with pytest.raises(ValueError):
        judge_item(it, ex, same)


def test_per_turn_verdict_has_one_entry_per_turn(benchmark_root):
    it = _first("02-twomasters", benchmark_root)
    ex = execute_item(it, MockModelClient("mock-a", seed=1), FIXED_PERMUTATION_SEEDS)
    v = MockJudge("j", family="openai").score(it, ex, spec_for(it.design))
    main = next(a for a in ex.administrations if a.label == "main")
    assert len(v.per_unit) == len(main.turns)
    assert all("turn_state" in u["scores"] for u in v.per_unit)


def test_per_seat_verdict_for_09(benchmark_root):
    items = load_design("09-doubleedge", benchmark_root, include_exemplars=False)
    it = items[0]
    ex = execute_item(it, MockModelClient("mock-a", seed=1), FIXED_PERMUTATION_SEEDS)
    v = MockJudge("j", family="openai").score(it, ex, spec_for(it.design))
    seat_labels = [a.label for a in ex.administrations if a.label.startswith("seat")]
    assert len(v.per_unit) == len(seat_labels)


def test_analyze_disagreement_no_average():
    spec = spec_for("01-goodsamaritan")
    v1 = Verdict("j1", "anthropic", "item",
                 scores={"action_class": "full_obedience", "rationale_quality": 2}, per_unit=[])
    v2 = Verdict("j2", "openai", "item",
                 scores={"action_class": "objective_first", "rationale_quality": 0}, per_unit=[])
    res = analyze_disagreement(v1, v2, spec)
    assert res["agreement_rate"] == 0.0
    assert len(res["disagreements"]) == 2
    # agreement case
    v3 = Verdict("j3", "google", "item",
                 scores={"action_class": "full_obedience", "rationale_quality": 2}, per_unit=[])
    res2 = analyze_disagreement(v1, v3, spec)
    assert res2["agreement_rate"] == 1.0
    assert res2["disagreements"] == []
