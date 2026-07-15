#!/usr/bin/env python3
"""Offline structured-verdict replay through unchanged WCF-Bench scorers."""

from __future__ import annotations

import hashlib
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Sequence

import pilot2_preflight as preflight
from wcfbench.contested import (
    build_disclosure_prompt, score_contested_position, settled_core_keypoints)
from wcfbench.judge import build_award_prompt, build_judge_prompt
from wcfbench.judge_panel import (
    build_episode_keypoint_prompt, _parse_episode_keypoint_verdicts)
from wcfbench.refusal import classify_refusal
from wcfbench.response_parser import parse_ranking
from wcfbench.routing import infer_should_refuse, ordinal_max, scorer_kind
from wcfbench.scorers import score_aggravate_ordinal, score_prooftext_anchors
from wcfbench.triaxial import AXES, score_triaxial


def _not_implemented(*_args, **_kwargs):
    raise NotImplementedError("Pilot 2 scorer replay is not implemented")


def synthetic_structured_result(
    call_kind: str, payload: Mapping[str, Any],
) -> Dict[str, Any]:
    """Deterministic positive fixture output for mechanical schema/custody tests."""
    criteria = payload.get("criteria") or [{"criterion_id": "FIXTURE", "points": 1.0}]
    ids = [row.get("criterion_id") if isinstance(row, Mapping) else str(row)
           for row in criteria]
    if call_kind == "open_award":
        return {"awards": [{
            "criterion_id": value, "satisfied": True, "reason": "fixture award"}
            for value in ids]}
    if call_kind.startswith("open_axis_"):
        return {"axis": call_kind.rsplit("_", 1)[1], "score": 1.0,
                "reason": "fixture axis"}
    if call_kind == "contested_disclosure":
        return {"avoided_settled": True, "located_divide": True,
                "evidence_quote": str(payload.get("response") or "")[:20],
                "reason": "fixture disclosure"}
    if call_kind == "contested_position":
        return {"position_label": "defensible fixture position",
                "position_defensible": True, "reason": "fixture position"}
    if call_kind == "contested_coherence":
        return {"score": 1.0, "reason": "fixture coherence"}
    if call_kind == "contested_settled_core":
        return {"verdicts": [{
            "criterion_id": value, "satisfied": True, "reason": "fixture core"}
            for value in ids]}
    if call_kind == "episode_keypoints":
        return {"verdicts": [{
            "criterion_id": value, "satisfied": True, "reason": "fixture episode"}
            for value in ids]}
    raise ValueError(f"unsupported Pilot 2 call kind: {call_kind}")


class AnalysisError(RuntimeError):
    """Immutable responses/verdicts cannot support valid Pilot 2 analysis."""


class _CaptureJudge:
    def __init__(self, item: Any, response: str) -> None:
        self.item = item
        self.response = response
        self.prompts = []
        self.last_finish_reason = "stop"

    def complete(self, prompt: str, item_id: Optional[str] = None) -> str:
        self.prompts.append(prompt)
        if prompt.startswith("DISCLOSURE check"):
            quote = self.response[:20]
            return ("KP1: award — capture reason\n"
                    f'KP2: award — capture reason, "{quote}"')
        if prompt.startswith("POSITION-ATTRIBUTION check"):
            return "POSITION: capture position\nDEFENSIBLE: yes"
        if prompt.startswith("COHERENCE check"):
            return "SCORE: 1.0\nReason: capture"
        if prompt.startswith("SETTLED-CORE check"):
            return "\n".join(
                f"{index}: correct — capture reason"
                for index, _kp in enumerate(settled_core_keypoints(self.item), 1))
        if prompt.startswith("You are grading a Westminster-Standards benchmark"):
            tagged = [kp for kp in self.item.rubric if getattr(kp, "axis", None) in AXES]
            return "\n".join(
                f"KP{index}: award — capture reason"
                for index, _kp in enumerate(tagged, 1))
        if "Manner" in prompt or "MANNER" in prompt:
            return "SCORE: 1.0\nReason: capture"
        if "End" in prompt or "END" in prompt:
            return "SCORE: 1.0\nReason: capture"
        return "SCORE: 1.0\nReason: capture"


def _criteria(keypoints: Sequence[Any]) -> list:
    return [{"criterion_id": kp.criterion, "points": float(kp.points)}
            for kp in keypoints]


def _call(
    *, sut: str, item: Any, route: str, index: int, call_kind: str,
    prompt: str, response: str, criteria: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    return {
        "record_id": f"{sut}::{item.id}::call{index:02d}::{call_kind}",
        "sut": sut, "route": route, "item_id": item.id,
        "call_kind": call_kind,
        "payload": {
            "judge_prompt": prompt,
            "response": response,
            "criteria": [dict(row) for row in criteria],
        },
    }


def build_judge_calls(item: Any, response: str, *, sut: str) -> list:
    """Render the exact existing scorer prompts as one record per logical call."""
    route = scorer_kind(item)
    if route in {"ordinal", "anchor"}:
        return []
    if route == "episode":
        return [_call(
            sut=sut, item=item, route=route, index=1,
            call_kind="episode_keypoints",
            prompt=build_episode_keypoint_prompt(item, response), response=response,
            criteria=_criteria(item.rubric))]
    capture = _CaptureJudge(item, response)
    kinds = []
    criteria_by_call = []
    if route == "open":
        tagged = [kp for kp in item.rubric if getattr(kp, "axis", None) in AXES]
        axes = {kp.axis for kp in tagged}
        if tagged:
            kinds.append("open_award")
            criteria_by_call.append(_criteria(tagged))
        for axis in AXES:
            if axis not in axes:
                kinds.append(f"open_axis_{axis}")
                criteria_by_call.append([{
                    "criterion_id": f"__axis__:{axis}", "points": 1.0}])
        score_triaxial(
            stem=item.stem, rubric=item.rubric, response=response,
            judge=capture, item_id=item.id)
    elif route == "contested":
        score_contested_position(
            item=item, response=response, judge=capture,
            ranking=parse_ranking(response), item_id=item.id)
        kinds = ["contested_disclosure", "contested_position",
                 "contested_coherence"]
        criteria_by_call = [
            [{"criterion_id": "disclosure:avoided_settled", "points": .5},
             {"criterion_id": "disclosure:located_divide", "points": .5}],
            [{"criterion_id": "position:defensibility", "points": 1.0}],
            [{"criterion_id": "coherence", "points": 1.0}],
        ]
        core = settled_core_keypoints(item)
        if core:
            kinds.append("contested_settled_core")
            criteria_by_call.append(_criteria(core))
    else:
        raise AnalysisError(f"unsupported scorer route: {route}")
    if len(capture.prompts) != len(kinds):
        raise AnalysisError(
            f"existing scorer call geometry drifted for {item.id}: "
            f"{len(capture.prompts)} != {len(kinds)}")
    return [_call(
        sut=sut, item=item, route=route, index=index, call_kind=kind,
        prompt=prompt, response=response, criteria=criteria)
        for index, (kind, prompt, criteria) in enumerate(
            zip(kinds, capture.prompts, criteria_by_call), 1)]


class _ReplayJudge:
    def __init__(
        self, calls: Sequence[Mapping[str, Any]],
        verdicts: Sequence[Mapping[str, Any]], response: str,
    ) -> None:
        by_id = {row.get("record_id"): row for row in verdicts}
        if len(by_id) != len(verdicts) or set(by_id) != {
                row["record_id"] for row in calls}:
            raise AnalysisError("judge verdict IDs do not exactly match scorer calls")
        self.queue = [(row, by_id[row["record_id"]]["result"]) for row in calls]
        self.response = response
        self.last_finish_reason = "stop"

    def complete(self, prompt: str, item_id: Optional[str] = None) -> str:
        if not self.queue:
            raise AnalysisError("existing scorer requested an unregistered judge call")
        call, result = self.queue.pop(0)
        if call["payload"]["judge_prompt"] != prompt:
            raise AnalysisError("scorer prompt does not match immutable judge call")
        kind = call["call_kind"]
        if kind == "open_award":
            return "\n".join(
                f"KP{index}: {'award' if row['satisfied'] else 'deny'} — {row['reason']}"
                for index, row in enumerate(result["awards"], 1))
        if kind.startswith("open_axis_") or kind == "contested_coherence":
            return f"SCORE: {result['score']}\nReason: {result['reason']}"
        if kind == "contested_disclosure":
            kp1 = "award" if result["avoided_settled"] else "deny"
            kp2 = "award" if result["located_divide"] else "deny"
            return (f"KP1: {kp1} — {result['reason']}\n"
                    f"KP2: {kp2} — {result['reason']}, "
                    f'"{result["evidence_quote"]}"')
        if kind == "contested_position":
            defensible = "yes" if result["position_defensible"] else "no"
            return (f"POSITION: {result['position_label']}\n"
                    f"DEFENSIBLE: {defensible}")
        if kind in {"contested_settled_core", "episode_keypoints"}:
            return "\n".join(
                f"{index}: {'correct' if row['satisfied'] else 'wrong'} — {row['reason']}"
                for index, row in enumerate(result["verdicts"], 1))
        raise AnalysisError(f"unsupported replay call kind: {kind}")


def score_response(
    item: Any, response: str, verdicts: Sequence[Mapping[str, Any]], *, sut: str,
) -> Dict[str, Any]:
    """Replay structured outputs through the unchanged scorer/parsers."""
    route = scorer_kind(item)
    refusal = classify_refusal(
        response, should_refuse=infer_should_refuse(item))
    base = {
        "sut": sut, "item_id": item.id, "design": item.design,
        "route": route, "headline_score": None,
        "matter": None, "manner": None, "end": None,
        "refusal_class": refusal.refusal_class,
        "refusal_is_failure": refusal.is_failure,
        "error": None,
    }
    if route == "ordinal":
        ranking = parse_ranking(response)
        if ranking is None:
            base["error"] = "unparseable ordinal ranking"
            return base
        scored = score_aggravate_ordinal(
            item.extra.get("gold_order"), ranking,
            ordering_max=ordinal_max(item))
        base["headline_score"] = (
            scored.ordering_points / scored.ordering_max
            if scored.ordering_max else 0.0)
        return base
    if route == "anchor":
        scored = score_prooftext_anchors(item.rubric, response)
        base["headline_score"] = scored.fraction if scored.max_points > 0 else None
        if scored.max_points <= 0:
            base["error"] = "anchor denominator is zero"
        return base
    calls = build_judge_calls(item, response, sut=sut)
    replay = _ReplayJudge(calls, verdicts, response)
    if route == "open":
        scored = score_triaxial(
            stem=item.stem, rubric=item.rubric, response=response,
            judge=replay, item_id=item.id)
        base.update({
            "headline_score": scored.matter,
            "matter": scored.matter, "manner": scored.manner, "end": scored.end,
        })
    elif route == "contested":
        scored = score_contested_position(
            item=item, response=response, judge=replay,
            ranking=parse_ranking(response), item_id=item.id)
        base["contested"] = {
            "disclosure": scored.disclosure,
            "position_label": scored.position_label,
            "position_defensible": scored.position_defensible,
            "coherence": scored.coherence,
            "settled_core_fraction": scored.settled_core_fraction,
        }
    elif route == "episode":
        text = replay.complete(calls[0]["payload"]["judge_prompt"], item_id=item.id)
        values, _reasonless = _parse_episode_keypoint_verdicts(text, item)
        graded = [kp for kp in item.rubric if kp.criterion in values]
        denominator = sum(float(kp.points) for kp in graded)
        base["headline_score"] = (
            sum(float(kp.points) for kp in graded if values[kp.criterion]) / denominator
            if denominator else None)
        if denominator == 0:
            base["error"] = "episode has no parseable keypoint votes"
    if replay.queue:
        raise AnalysisError("one or more immutable judge calls were not consumed")
    return base


def _bootstrap(values: Sequence[float], seed: str) -> tuple:
    if not values:
        return None, None
    if len(values) == 1:
        return values[0], values[0]
    rng = random.Random(int(hashlib.sha256(seed.encode()).hexdigest()[:16], 16))
    means = []
    for _ in range(1000):
        sample = [values[rng.randrange(len(values))] for _ in values]
        means.append(sum(sample) / len(sample))
    means.sort()
    return means[24], means[974]


def _group_summary(rows: Sequence[Mapping[str, Any]], key: str, value: str) -> Dict[str, Any]:
    numeric = [float(row["headline_score"]) for row in rows
               if isinstance(row.get("headline_score"), (int, float))
               and not isinstance(row.get("headline_score"), bool)
               and math.isfinite(float(row["headline_score"]))]
    low, high = _bootstrap(numeric, f"pilot2:{key}:{value}")
    return {
        key: value, "expected": len(rows), "numeric": len(numeric),
        "errors_missing": len(rows) - len(numeric),
        "mean": sum(numeric) / len(numeric) if numeric else None,
        "ci_low": low, "ci_high": high,
    }


def summarize_scored_cells(
    rows: Sequence[Mapping[str, Any]], *, suts: Sequence[str],
) -> Dict[str, Any]:
    cells = [dict(row) for row in rows]
    per_sut = []
    for sut in suts:
        selected = [row for row in cells if row.get("sut") == sut
                    and row.get("route") != "contested"]
        summary = _group_summary(selected, "sut", sut)
        summary.update({
            "scalar_denominator": 222,
            "coverage_status": ("SUFFICIENT_DESCRIPTIVE"
                                if summary["numeric"] >= 200 else "INCOMPLETE"),
            "traceable_cells": sum(bool(row.get("source_response_sha256"))
                                   for row in cells if row.get("sut") == sut),
        })
        if summary["numeric"] < 200:
            summary["mean"] = summary["ci_low"] = summary["ci_high"] = None
        per_sut.append(summary)
    per_design = [_group_summary(group, "design", name)
                  for name, group in _groups(cells, "design")]
    per_route = [_group_summary(group, "route", name)
                 for name, group in _groups(cells, "route")]
    axis_summary = {}
    for axis in AXES:
        values = [float(row[axis]) for row in cells
                  if isinstance(row.get(axis), (int, float))]
        axis_summary[axis] = {
            "numeric": len(values),
            "mean": sum(values) / len(values) if values else None,
        }
    return {
        "validity_label": preflight.VALIDITY_LABEL,
        "cells": cells, "per_sut": per_sut,
        "per_design": per_design, "per_route": per_route,
        "axis_summary": axis_summary,
        "refusal_summary": dict(Counter(
            row.get("refusal_class") for row in cells if row.get("refusal_class"))),
        "contested_summary": [row for row in cells if row.get("route") == "contested"],
        "errors_missing": [row for row in cells if row.get("error")
                           or row.get("headline_score") is None],
        "traceability": [{
            "sut": row.get("sut"), "item_id": row.get("item_id"),
            "response_sha256": row.get("source_response_sha256"),
            "judge_record_ids": row.get("judge_record_ids", []),
        } for row in cells],
    }


def _groups(rows: Sequence[Mapping[str, Any]], key: str) -> list:
    grouped: Dict[str, list] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key))].append(row)
    return sorted(grouped.items())


def analyze_records(
    responses: Sequence[Mapping[str, Any]], verdicts: Sequence[Mapping[str, Any]],
    *, items: Sequence[Any], suts: Sequence[str],
) -> Dict[str, Any]:
    by_item = {item.id: item for item in items}
    if len(by_item) != 230:
        raise AnalysisError("analysis requires all 230 frozen items")
    verdict_by_id = {}
    for row in verdicts:
        record_id = row.get("record_id")
        if not isinstance(record_id, str) or record_id in verdict_by_id:
            raise AnalysisError("judge verdict IDs are missing or duplicated")
        verdict_by_id[record_id] = row
    cells, diagnostics = [], []
    for response_row in responses:
        sut, item_id = response_row.get("sut"), response_row.get("item_id")
        if sut not in suts or item_id not in by_item:
            raise AnalysisError("response is outside registered roster/bank")
        item = by_item[item_id]
        if item.extra.get("dev_set_only"):
            diagnostics.append({
                **dict(response_row), "diagnostic_only": True, "judge_calls": 0})
            continue
        if response_row.get("status") != "response":
            cells.append({
                "sut": sut, "item_id": item_id, "design": item.design,
                "route": scorer_kind(item), "headline_score": None,
                "error": response_row.get("error") or "missing response",
                "source_response_sha256": response_row.get("response_sha256"),
                "judge_record_ids": [],
            })
            continue
        response = response_row.get("final_answer")
        if not isinstance(response, str):
            raise AnalysisError("successful response lacks final answer")
        calls = build_judge_calls(item, response, sut=sut)
        cell_verdicts = [verdict_by_id[call["record_id"]] for call in calls
                         if call["record_id"] in verdict_by_id]
        if len(cell_verdicts) != len(calls):
            scored = {
                "sut": sut, "item_id": item_id, "design": item.design,
                "route": scorer_kind(item), "headline_score": None,
                "error": "missing judge verdict", "matter": None,
                "manner": None, "end": None, "refusal_class": None,
            }
        else:
            scored = score_response(item, response, cell_verdicts, sut=sut)
        scored["source_response_sha256"] = response_row.get("response_sha256")
        scored["judge_record_ids"] = [call["record_id"] for call in calls]
        cells.append(scored)
    dataset = summarize_scored_cells(cells, suts=suts)
    dataset["diagnostic_dev_cells"] = diagnostics
    return dataset


def analyze_immutable_run(run_dir: Path) -> Dict[str, Any]:
    """Read completed response checkpoints and structured verdicts without mutation."""
    run_dir = Path(run_dir)
    try:
        responses = [json.loads(line) for line in
                     (run_dir / "checkpoint.jsonl").read_text().splitlines() if line.strip()]
        verdicts = [json.loads(line) for line in
                    (run_dir / "judge-verdicts.jsonl").read_text().splitlines() if line.strip()]
    except (OSError, json.JSONDecodeError) as exc:
        raise AnalysisError("immutable run evidence is unreadable") from exc
    return analyze_records(
        responses, verdicts,
        items=preflight.load_items(str(preflight.BANK_DIR)), suts=preflight.SUTS)
