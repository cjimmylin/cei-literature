"""Deterministic blinded batching for the OPEN6-SOL1 single descriptive judge.

This module only assembles and validates registered judge work.  It deliberately
does not call Codex, aggregate a cross-design score, adjudicate, or emit a gate
verdict.  Transport custody and the one-replay rule live in
``open6_sol1_runtime.SolExecClient``.
"""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence, Tuple

from .judges import assemble_rubric_prompt
from .open6_sol1 import SOL_BATCH_MAX_UNITS, canonical_json_bytes, sol_runtime_contract
from .references import bank_reference_provider
from .rubrics import BIN, CAT, INT, ORD, spec_for

SOL_JUDGE_NAME = "gpt-5.6-sol"
SOL_JUDGE_FAMILY = "openai"


class JudgeContractError(RuntimeError):
    """Raised when execution data cannot satisfy the frozen judge contract."""


def _hash(value) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def scoring_spec_payload(design: str) -> dict:
    spec = spec_for(design)
    return {
        "design": spec.design,
        "unit": spec.unit,
        "primary_metric": spec.primary_metric,
        "judge_free_primary": spec.judge_free_primary,
        "length_correction": spec.length_correction,
        "reference_anchored": spec.reference_anchored,
        "categories": [
            {
                "name": category.name,
                "scale": category.scale,
                "options": category.options,
                "description": category.desc,
            }
            for category in spec.categories
        ],
    }


def _category_schema(category) -> dict:
    if category.scale == CAT:
        return {"type": "string", "enum": list(category.options)}
    if category.scale in (ORD, BIN):
        kind = "integer" if all(type(value) is int for value in category.options) else "number"
        return {"type": kind, "enum": list(category.options)}
    if category.scale == INT:
        low, high = category.options
        return {"type": "integer", "minimum": low, "maximum": high}
    raise JudgeContractError(f"unsupported registered scale: {category.scale!r}")


def design_score_schema(design: str) -> dict:
    spec = spec_for(design)
    names = [category.name for category in spec.categories]
    return {
        "type": "object",
        "additionalProperties": False,
        "required": names,
        "properties": {
            category.name: _category_schema(category)
            for category in spec.categories
        },
    }


def first_allowed_score(design: str, category_name: str):
    for category in spec_for(design).categories:
        if category.name == category_name:
            return category.options[0]
    raise KeyError(category_name)


@dataclass(frozen=True)
class ScoringUnit:
    unit_key: str
    record_key: str
    design: str
    item_id: str
    unit_kind: str
    locator: Tuple[Tuple[str, object], ...]
    category_names: Tuple[str, ...]
    score_schema_sha256: str
    rubric_and_response: str

    @property
    def locator_dict(self) -> dict:
        return dict(self.locator)


@dataclass(frozen=True)
class JudgeBatch:
    batch_id: str
    design: str
    score_schema_sha256: str
    units: Tuple[ScoringUnit, ...]


@dataclass(frozen=True)
class JudgeRequest:
    logical_key: str
    batch_id: str
    design: str
    prompt: str
    schema: dict
    expected_unit_keys: Tuple[str, ...]
    score_schema: dict


def _opaque_key(run_namespace: str, model_slug: str, item_id: str, locator: dict) -> str:
    material = {
        "run_namespace": run_namespace,
        "model": model_slug,
        "item_id": item_id,
        "locator": locator,
    }
    return "u_" + _hash(material)[:40]


def _record_key(run_namespace: str, model_slug: str, item_id: str) -> str:
    return "r_" + _hash({
        "run_namespace": run_namespace,
        "model": model_slug,
        "item_id": item_id,
    })[:40]


def _unit(unit_key, record_key, item, kind, locator, response_text, label) -> ScoringUnit:
    spec = spec_for(item.design)
    references = bank_reference_provider(item) if spec.reference_anchored else None
    prompt = assemble_rubric_prompt(
        item,
        spec,
        response_text,
        references=references,
        unit_label=label,
    )
    score_schema = design_score_schema(item.design)
    return ScoringUnit(
        unit_key=unit_key,
        record_key=record_key,
        design=item.design,
        item_id=item.id,
        unit_kind=kind,
        locator=tuple(locator.items()),
        category_names=tuple(category.name for category in spec.categories),
        score_schema_sha256=_hash(score_schema),
        rubric_and_response=prompt,
    )


def build_scoring_units(item, execution, model_slug: str,
                        run_namespace: str) -> list[ScoringUnit]:
    """Materialize the exact logical judge units for one item-model execution."""
    if (execution.item_id != item.id or execution.design != item.design
            or execution.model != model_slug):
        raise JudgeContractError("item, execution, and model identity mismatch")
    spec = spec_for(item.design)
    units = []
    record_key = _record_key(run_namespace, model_slug, item.id)

    def add(kind, locator, response, label):
        if not isinstance(response, str) or not response.strip():
            raise JudgeContractError(
                f"missing response for {item.id} {dict(locator)!r}"
            )
        key = _opaque_key(run_namespace, model_slug, item.id, dict(locator))
        units.append(_unit(
            key, record_key, item, kind, dict(locator), response, label,
        ))

    if spec.unit == "item":
        if not execution.administrations:
            raise JudgeContractError(f"no administration for {item.id}")
        administration = execution.administrations[0]
        response = (
            administration.turns[0].response
            if administration.turns and administration.turns[0].response
            else administration.terminal_response
        )
        add("item", (("item", "item"),), response, None)
    elif spec.unit == "per_turn":
        main = next(
            (row for row in execution.administrations if row.label == "main"),
            execution.administrations[0] if execution.administrations else None,
        )
        if main is None:
            raise JudgeContractError(f"no main administration for {item.id}")
        for turn in main.turns:
            add("turn", (("index", turn.index),), turn.response, f"turn {turn.index}")
        if main.terminal_response is not None:
            add(
                "turn",
                (("index", len(main.turns) + 1), ("terminal", True)),
                main.terminal_response,
                "terminal artifact",
            )
    elif spec.unit == "per_admin":
        for administration in execution.administrations:
            response = (
                administration.turns[0].response
                if administration.turns and administration.turns[0].response
                else administration.terminal_response
            )
            add(
                "administration",
                (("label", administration.label),),
                response,
                administration.label,
            )
    elif spec.unit == "per_seat":
        for administration in execution.administrations:
            if not administration.label.startswith("seat"):
                continue
            response = (
                administration.turns[0].response
                if administration.turns and administration.turns[0].response
                else administration.terminal_response
            )
            add("seat", (("label", administration.label),), response, administration.label)
    else:
        raise JudgeContractError(f"unsupported scoring unit: {spec.unit!r}")

    expected = (
        1 if spec.unit == "item" else
        len([row for row in execution.administrations if row.label.startswith("seat")])
        if spec.unit == "per_seat" else
        len(execution.administrations) if spec.unit == "per_admin" else
        len(next(row for row in execution.administrations if row.label == "main").turns)
        + (1 if next(row for row in execution.administrations
                    if row.label == "main").terminal_response is not None else 0)
    )
    if len(units) != expected or len({unit.unit_key for unit in units}) != expected:
        raise JudgeContractError(f"scoring-unit geometry mismatch for {item.id}")
    return units


def batch_scoring_units(units: Iterable[ScoringUnit],
                        max_units: int = SOL_BATCH_MAX_UNITS) -> list[JudgeBatch]:
    if type(max_units) is not int or not (1 <= max_units <= SOL_BATCH_MAX_UNITS):
        raise JudgeContractError("judge batch size exceeds registered maximum")
    groups = {}
    for unit in units:
        groups.setdefault((unit.design, unit.score_schema_sha256), []).append(unit)
    batches = []
    for (design, schema_hash), group in sorted(groups.items()):
        ordered = sorted(group, key=lambda unit: unit.unit_key)
        for offset in range(0, len(ordered), max_units):
            chunk = tuple(ordered[offset:offset + max_units])
            batch_id = "b_" + _hash({
                "design": design,
                "schema": schema_hash,
                "keys": [unit.unit_key for unit in chunk],
            })[:40]
            batches.append(JudgeBatch(batch_id, design, schema_hash, chunk))
    return batches


def _request_schema(contract: dict, keys: Sequence[str], score_schema: dict) -> dict:
    """Bind dynamic values into the exact frozen schema template."""
    schema = deepcopy(contract["schema"]["template"])
    verdicts = schema["properties"]["verdicts"]
    verdicts["minItems"] = len(keys)
    verdicts["maxItems"] = len(keys)
    properties = verdicts["items"]["properties"]
    properties["unit_key"]["enum"] = list(keys)
    properties["scores"] = deepcopy(score_schema)
    return schema


def build_judge_request(batch: JudgeBatch) -> JudgeRequest:
    if not batch.units or len(batch.units) > SOL_BATCH_MAX_UNITS:
        raise JudgeContractError("invalid judge batch size")
    if ({unit.design for unit in batch.units} != {batch.design}
            or {unit.score_schema_sha256 for unit in batch.units}
            != {batch.score_schema_sha256}):
        raise JudgeContractError("judge batch crosses design or score schema")
    contract = sol_runtime_contract()["judge"]
    score_payload = scoring_spec_payload(batch.design)
    score_schema = design_score_schema(batch.design)
    if _hash(score_schema) != batch.score_schema_sha256:
        raise JudgeContractError("score-schema hash mismatch")
    blinded = [
        {
            "unit_key": unit.unit_key,
            "rubric_and_response": unit.rubric_and_response,
        }
        for unit in batch.units
    ]
    template = contract["prompt"]["user_template"]
    user = (
        template
        .replace("{{DESIGN}}", batch.design)
        .replace("{{SCORING_SPEC_JSON}}", json.dumps(
            score_payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        .replace("{{BLINDED_UNITS_JSON}}", json.dumps(
            blinded, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    )
    prompt = contract["prompt"]["system_text"] + "\n\n" + user
    keys = tuple(unit.unit_key for unit in batch.units)
    return JudgeRequest(
        logical_key="sol:judge:" + batch.batch_id,
        batch_id=batch.batch_id,
        design=batch.design,
        prompt=prompt,
        schema=_request_schema(contract, keys, score_schema),
        expected_unit_keys=keys,
        score_schema=score_schema,
    )


def validate_judge_result(request: JudgeRequest, value) -> bool:
    from .open6_sol1_runtime import validate_batch_result

    return validate_batch_result(
        value,
        request.expected_unit_keys,
        request.score_schema,
    )


def scores_by_unit(request: JudgeRequest, value) -> dict:
    if not validate_judge_result(request, value):
        raise ValueError("invalid judge result")
    return {row["unit_key"]: row["scores"] for row in value["verdicts"]}


def execute_judge_batch(sol_client, request: JudgeRequest):
    """Execute a batch with semantic key validation inside the replay boundary."""
    return sol_client.run_json(
        request.logical_key,
        request.prompt,
        request.schema,
        value_validator=lambda value: validate_judge_result(request, value),
    )


def reassemble_single_judge_verdict(item, units: Sequence[ScoringUnit],
                                    scores: Mapping[str, dict]) -> dict:
    """Reassemble one descriptive Sol verdict in the harness's familiar shape."""
    spec = spec_for(item.design)
    if (not units
            or any(unit.item_id != item.id or unit.design != item.design for unit in units)
            or len({unit.record_key for unit in units}) != 1):
        raise JudgeContractError("verdict units do not belong to one item-model record")
    if (len({unit.unit_key for unit in units}) != len(units)
            or len({unit.locator for unit in units}) != len(units)):
        raise JudgeContractError("duplicate verdict unit")
    if set(scores) != {unit.unit_key for unit in units}:
        raise JudgeContractError("verdict scores do not cover exact item units")
    verdict = {
        "judge": SOL_JUDGE_NAME,
        "family": SOL_JUDGE_FAMILY,
        "unit": spec.unit,
        "scores": {},
        "per_unit": [],
        "refused": False,
    }
    for unit in units:
        unit_scores = scores[unit.unit_key]
        request = JudgeRequest(
            logical_key="validation-only",
            batch_id="validation-only",
            design=item.design,
            prompt="",
            schema={},
            expected_unit_keys=(unit.unit_key,),
            score_schema=design_score_schema(item.design),
        )
        if not validate_judge_result(
            request, {"verdicts": [{"unit_key": unit.unit_key, "scores": unit_scores}]}
        ):
            raise JudgeContractError(f"invalid scores for {unit.unit_key}")
        if spec.unit == "item":
            verdict["scores"] = dict(unit_scores)
        else:
            row = unit.locator_dict
            row["scores"] = dict(unit_scores)
            verdict["per_unit"].append(row)
    return verdict
