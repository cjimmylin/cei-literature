"""Offline contract tests for OPEN6-SOL1 single-judge batching."""

from __future__ import annotations

from collections import Counter

import pytest

from walkworthy.executors import (
    AdministrationResult,
    ItemExecution,
    TurnResult,
)
from walkworthy.open6_sol1 import select_public_items

MODEL_SLUGS = (
    "minimax/minimax-m3",
    "z-ai/glm-5.2",
    "deepseek/deepseek-v4-pro",
    "qwen/qwen3.5-397b-a17b",
    "google/gemma-4-31b-it",
    "meta-llama/llama-4-maverick",
)


def _module():
    from walkworthy import open6_sol1_judge

    return open6_sol1_judge


def _execution(item, model):
    administrations = []
    for admin in item.administrations:
        turns = [
            TurnResult(
                index=turn.index,
                user_text=turn.text or next(iter((turn.branches or {"": ""}).values())),
                response=f"response for {item.id} {admin.label} turn {turn.index}",
                branch_state=(next(iter(turn.branches)) if turn.branches else None),
            )
            for turn in admin.turns
        ]
        administrations.append(
            AdministrationResult(
                label=admin.label,
                kind=admin.kind,
                system=admin.system,
                turns=turns,
                terminal_response=(
                    f"terminal response for {item.id} {admin.label}"
                    if admin.terminal_ask
                    else None
                ),
                terminal_user_text=admin.terminal_ask,
            )
        )
    return ItemExecution(
        item_id=item.id,
        design=item.design,
        model=model,
        order=[admin.label for admin in administrations],
        administrations=administrations,
        isolation_used=item.isolation_required,
    )


def test_full_surface_units_cells_and_same_design_batches(benchmark_root):
    judge = _module()
    items = select_public_items(benchmark_root)
    units = []
    for model in MODEL_SLUGS:
        for item in items:
            units.extend(judge.build_scoring_units(
                item, _execution(item, model), model, "manifest-sha",
            ))

    assert len(units) == 5370
    assert sum(len(unit.category_names) for unit in units) == 10008
    assert len({unit.unit_key for unit in units}) == 5370
    assert Counter(unit.design for unit in units) == {
        "01-goodsamaritan": 294,
        "02-twomasters": 1716,
        "03-quiettongue": 396,
        "04-innerweight": 360,
        "05-ordoamoris": 192,
        "06-crookedpath": 186,
        "07-seventyseven": 978,
        "08-vocationfork": 396,
        "09-doubleedge": 420,
        "10-strangergate": 432,
    }

    batches = judge.batch_scoring_units(units)
    assert len(batches) == 227
    assert all(1 <= len(batch.units) <= 24 for batch in batches)
    assert all(len({unit.design for unit in batch.units}) == 1 for batch in batches)
    assert all(len({unit.score_schema_sha256 for unit in batch.units}) == 1
               for batch in batches)


def test_unit_text_selection_and_model_blinding(benchmark_root):
    judge = _module()
    items = {item.design: item for item in select_public_items(benchmark_root)}

    for design, expected_kind in (
        ("01-goodsamaritan", "item"),
        ("02-twomasters", "turn"),
        ("03-quiettongue", "administration"),
        ("09-doubleedge", "seat"),
    ):
        item = items[design]
        model = MODEL_SLUGS[0]
        units = judge.build_scoring_units(
            item, _execution(item, model), model, "manifest-sha",
        )
        assert units
        assert all(unit.unit_kind == expected_kind for unit in units)
        request = judge.build_judge_request(judge.batch_scoring_units(units)[0])
        assert model not in request.prompt
        assert all(other not in request.prompt for other in MODEL_SLUGS)
        assert item.id in request.prompt
        assert "response for" in request.prompt or "terminal response" in request.prompt


def test_judge_request_uses_exact_closed_schema_and_is_byte_stable(benchmark_root):
    judge = _module()
    item = next(item for item in select_public_items(benchmark_root)
                if item.design == "04-innerweight")
    units = judge.build_scoring_units(
        item, _execution(item, MODEL_SLUGS[1]), MODEL_SLUGS[1], "manifest-sha",
    )
    batch = judge.batch_scoring_units(units)[0]
    first = judge.build_judge_request(batch)
    second = judge.build_judge_request(batch)

    assert first == second
    assert first.expected_unit_keys == tuple(unit.unit_key for unit in batch.units)
    assert first.schema["additionalProperties"] is False
    verdict = first.schema["properties"]["verdicts"]["items"]
    assert verdict["additionalProperties"] is False
    scores = verdict["properties"]["scores"]
    assert scores["additionalProperties"] is False
    assert scores["required"] == ["favorability", "rating", "harshness"]
    assert scores["properties"]["rating"] == {
        "type": "integer", "minimum": 1, "maximum": 10,
    }
    assert scores["properties"]["harshness"] == {
        "type": "integer", "enum": [0, 1],
    }


def test_batch_result_requires_exact_unique_keys_and_registered_values(benchmark_root):
    judge = _module()
    item = next(item for item in select_public_items(benchmark_root)
                if item.design == "01-goodsamaritan")
    unit = judge.build_scoring_units(
        item, _execution(item, MODEL_SLUGS[0]), MODEL_SLUGS[0], "manifest-sha",
    )[0]
    batch = judge.batch_scoring_units([unit])[0]
    request = judge.build_judge_request(batch)
    good = {
        "verdicts": [{
            "unit_key": unit.unit_key,
            "scores": {"action_class": "partial", "rationale_quality": 1},
        }],
    }
    assert judge.validate_judge_result(request, good)
    assert judge.scores_by_unit(request, good) == {
        unit.unit_key: {"action_class": "partial", "rationale_quality": 1},
    }

    duplicate = {"verdicts": good["verdicts"] * 2}
    wrong = {"verdicts": [{**good["verdicts"][0], "unit_key": "not-registered"}]}
    bad_value = {"verdicts": [{
        "unit_key": unit.unit_key,
        "scores": {"action_class": "partial", "rationale_quality": 9},
    }]}
    assert not judge.validate_judge_result(request, duplicate)
    assert not judge.validate_judge_result(request, wrong)
    assert not judge.validate_judge_result(request, bad_value)
    with pytest.raises(ValueError, match="invalid judge result"):
        judge.scores_by_unit(request, bad_value)


def test_single_judge_verdict_reassembly_preserves_registered_unit_shape(benchmark_root):
    judge = _module()
    items = {item.design: item for item in select_public_items(benchmark_root)}

    for design in ("01-goodsamaritan", "02-twomasters", "03-quiettongue",
                   "09-doubleedge"):
        item = items[design]
        execution = _execution(item, MODEL_SLUGS[0])
        units = judge.build_scoring_units(item, execution, MODEL_SLUGS[0], "manifest-sha")
        scores = {
            unit.unit_key: {
                name: judge.first_allowed_score(design, name)
                for name in unit.category_names
            }
            for unit in units
        }
        verdict = judge.reassemble_single_judge_verdict(item, units, scores)
        assert verdict["judge"] == "gpt-5.6-sol"
        assert verdict["family"] == "openai"
        assert verdict["unit"] == judge.scoring_spec_payload(design)["unit"]
        if verdict["unit"] == "item":
            assert verdict["scores"]
            assert verdict["per_unit"] == []
        else:
            assert verdict["scores"] == {}
            assert len(verdict["per_unit"]) == len(units)


def test_verdict_reassembly_rejects_mixed_model_records_and_duplicate_units(
        benchmark_root):
    judge = _module()
    item = next(item for item in select_public_items(benchmark_root)
                if item.design == "01-goodsamaritan")
    first = judge.build_scoring_units(
        item, _execution(item, MODEL_SLUGS[0]), MODEL_SLUGS[0], "manifest-sha",
    )[0]
    second = judge.build_scoring_units(
        item, _execution(item, MODEL_SLUGS[1]), MODEL_SLUGS[1], "manifest-sha",
    )[0]
    score = {"action_class": "partial", "rationale_quality": 1}
    with pytest.raises(judge.JudgeContractError, match="one item-model record"):
        judge.reassemble_single_judge_verdict(
            item, [first, second], {first.unit_key: score, second.unit_key: score},
        )
    with pytest.raises(judge.JudgeContractError, match="duplicate"):
        judge.reassemble_single_judge_verdict(
            item, [first, first], {first.unit_key: score},
        )


def test_execute_batch_wires_semantic_validator_into_sol_retry(benchmark_root):
    judge = _module()
    item = next(item for item in select_public_items(benchmark_root)
                if item.design == "01-goodsamaritan")
    unit = judge.build_scoring_units(
        item, _execution(item, MODEL_SLUGS[0]), MODEL_SLUGS[0], "manifest-sha",
    )[0]
    request = judge.build_judge_request(judge.batch_scoring_units([unit])[0])
    good = {"verdicts": [{
        "unit_key": unit.unit_key,
        "scores": {"action_class": "partial", "rationale_quality": 1},
    }]}

    class FakeResult:
        value = good

    class FakeSol:
        call = None

        def run_json(self, logical_key, prompt, schema, *, value_validator):
            self.call = (logical_key, prompt, schema, value_validator)
            assert value_validator(good)
            duplicate = {"verdicts": good["verdicts"] * 2}
            assert not value_validator(duplicate)
            return FakeResult()

    sol = FakeSol()
    result = judge.execute_judge_batch(sol, request)
    assert isinstance(result, FakeResult)
    assert sol.call[:3] == (request.logical_key, request.prompt, request.schema)
