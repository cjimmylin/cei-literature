#!/usr/bin/env python
"""Approved shadow-judge bakeoff runner."""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from format_bridge_requal import (
    BudgetGuard,
    CapturingClient,
    JsonlSink,
    OutputPathError,
    PreflightError,
    fetch_with_two_retries,
    require_preflight,
)
from wcfbench import load_items, mvp
from wcfbench.contested import _score_disclosure, score_settled_core
from wcfbench.judge import (
    award_emission_count,
    build_award_prompt,
    complete_with_retry,
    parse_award_verdict,
    willingness_to_grade,
)
from wcfbench.openrouter_client import OpenRouterModelClient
from wcfbench.qualification import (
    DEFAULT_K,
    DEFAULT_THRESHOLD,
    PROBES,
    JudgeQualification,
    current_template_hashes,
    load_manifest,
    qualify_judge,
)
from wcfbench.triaxial import AXES, TriaxialScore, _score_numeric_axis


HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.normpath(os.path.join(HERE, ".."))
RUN_DIR = os.path.join(PROJECT, "07-PILOTS", "20260712-shadow-judge-bakeoff")
MANIFEST_PATH = os.path.join(
    PROJECT,
    "07-PILOTS",
    "20260712-artifact-corrected-requal",
    "20260712-artifact-corrected-requal-manifest.json",
)
OPEN_PATH = os.path.join(
    PROJECT,
    "07-PILOTS",
    "20260712-mvp-open-reparse",
    "corrected-open-transcripts.jsonl",
)
FLOOR_PATH = os.path.join(
    PROJECT, "07-PILOTS", "20260710-floor-rerun", "transcripts.jsonl"
)
R33_PATH = os.path.join(
    PROJECT, "07-PILOTS", "20260710-r33-3judge", "transcripts.jsonl"
)
BANK_DIR = os.path.join(PROJECT, "05-BANK-YAML")

CANDIDATES = (
    ("glm-5.2", "z-ai", "z-ai/glm-5.2"),
    ("deepseek-v4-pro", "deepseek", "deepseek/deepseek-v4-pro"),
)
SURFACE_COUNTS = {
    "open_award": 8,
    "coherence": 8,
    "disclosure": 6,
    "settled_core": 6,
}
K = DEFAULT_K
THRESHOLD = DEFAULT_THRESHOLD
MAX_BUDGET = 1.0
JUDGE_MAX_TOKENS = 2048
SEED = 1647


def read_jsonl(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _usable(record: Dict[str, Any]) -> bool:
    return bool(record.get("sut_response")) and bool(record.get("judges"))


def select_contested_records(floor, r33, *, expected=6):
    chosen = {}
    for source_name, records in (("floor-rerun", floor), ("r33-3judge", r33)):
        for record in records:
            if record.get("kind") != "contested" or not _usable(record):
                continue
            key = (str(record["item_id"]), str(record["model"]))
            if key not in chosen:
                copied = dict(record)
                copied["source_run"] = source_name
                chosen[key] = copied
    if len(chosen) != expected:
        raise PreflightError(
            f"expected {expected} unique contested units, found {len(chosen)}"
        )
    return [chosen[key] for key in sorted(chosen)]


def take_seeded(surface, rows, count):
    ordered = sorted(
        rows,
        key=lambda row: hashlib.sha256(
            f"{SEED}|{surface}|{row['item_id']}|{row['model']}".encode()
        ).hexdigest(),
    )
    if len(ordered) < count:
        raise PreflightError(f"{surface}: need {count} units, found {len(ordered)}")
    return ordered[:count]


def _judges_by_name(record):
    return {str(j["name"]): j for j in record.get("judges", [])}


def _unit(surface, record, axis=None):
    response = str(record["sut_response"])
    return {
        "surface": surface,
        "item_id": str(record["item_id"]),
        "sut_slug": str(record["model"]),
        "sut_response": response,
        "response_sha256": hashlib.sha256(response.encode()).hexdigest(),
        "source_run": record.get("source_run", "corrected-mvp-open-reparse"),
        "axis": axis,
        "comparators": _judges_by_name(record),
    }


def build_selection(*, open_path, floor_path, r33_path, bank_dir):
    items = {item.id: item for item in load_items(bank_dir)}
    open_rows = [
        row for row in read_jsonl(open_path) if row.get("kind") == "open"
    ]
    award_rows = []
    coherence_rows = []
    for row in open_rows:
        judges = _judges_by_name(row)
        comparator_names = ("gemini-flash", "grok-4.20")
        if not set(comparator_names).issubset(judges):
            continue
        if all(
            judges[name].get("scores", {}).get("awards")
            for name in comparator_names
        ):
            award_rows.append(row)
        item = items[row["item_id"]]
        untagged = [
            axis
            for axis in AXES
            if not any(
                getattr(keypoint, "axis", None) == axis
                for keypoint in item.rubric
            )
        ]
        if len(untagged) == 1 and all(
            judges[name].get("scores", {}).get(untagged[0]) is not None
            for name in comparator_names
        ):
            copied = dict(row)
            copied["numeric_axis"] = untagged[0]
            coherence_rows.append(copied)

    selected = [
        _unit("open_award", row)
        for row in take_seeded("open_award", award_rows, 8)
    ]
    selected += [
        _unit("coherence", row, axis=row["numeric_axis"])
        for row in take_seeded("coherence", coherence_rows, 8)
    ]
    contested = select_contested_records(
        read_jsonl(floor_path), read_jsonl(r33_path)
    )
    selected += [_unit("disclosure", row) for row in contested]
    selected += [_unit("settled_core", row) for row in contested]
    return selected


def write_json_new(path, value):
    with open(path, "x", encoding="utf-8") as fh:
        json.dump(value, fh, indent=2, sort_keys=True)


def persist_probe_reps(sink, qualification, now):
    for probe in PROBES:
        for rep in qualification.probe_reps[probe].reps:
            sink.write(
                {
                    "kind": "probe_rep",
                    "timestamp": now(),
                    "judge": qualification.name,
                    "family": qualification.family,
                    "slug": qualification.slug,
                    "probe": probe,
                    "rep": rep["rep"],
                    "passed": rep["passed"],
                    "cause": rep["cause"],
                    "detail": rep["detail"],
                }
            )


def run_shadow_batteries(
    *,
    client_factory,
    qualify_fn=qualify_judge,
    sink=None,
    now=lambda: datetime.datetime.now().isoformat(timespec="seconds"),
):
    results = {}
    for name, family, slug in CANDIDATES:
        client = client_factory(name, family, slug)
        result = qualify_fn(
            client,
            name=name,
            family=family,
            slug=slug,
            k=K,
            threshold=THRESHOLD,
        )
        results[name] = result
        if sink is not None and isinstance(result, JudgeQualification):
            persist_probe_reps(sink, result, now)
    return results


def assert_template_hashes(manifest):
    if manifest.get("template_hashes") != current_template_hashes():
        raise PreflightError(
            "qualification template hash mismatch; stop before spending"
        )


def score_shadow_unit(unit, item, judge):
    surface = unit["surface"]
    response = unit["sut_response"]

    if surface == "open_award":
        tagged = [
            keypoint
            for keypoint in item.rubric
            if getattr(keypoint, "axis", None) in AXES
        ]
        prompt = build_award_prompt(
            stem=item.stem,
            rubric=item.rubric,
            response=response,
        )
        call = complete_with_retry(
            judge,
            prompt,
            item_id=item.id,
            is_complete=lambda text: award_emission_count(text) >= len(tagged),
        )
        if call.discarded or not willingness_to_grade(call.text):
            return {
                "graded": False,
                "awards": {},
                "compliance_defects": {},
                "discarded": call.discarded,
            }
        verdict = parse_award_verdict(call.text, require_reason=True)
        return {
            "graded": bool(verdict.awards),
            "awards": verdict.awards,
            "compliance_defects": verdict.compliance_defects,
            "discarded": False,
        }

    if surface == "coherence":
        axis = unit["axis"]
        score = TriaxialScore()
        _score_numeric_axis(
            score,
            axis,
            stem=item.stem,
            rubric=item.rubric,
            response=response,
            judge=judge,
            item_id=item.id,
        )
        return {
            "graded": bool(score.graded.get(axis, False)),
            "value": getattr(score, axis),
            "axis": axis,
            "scale_defect": bool(score.scale_defect.get(axis, False)),
        }

    if surface == "disclosure":
        score = _score_disclosure(judge, item, response, item.id)
        return {
            "graded": score.graded,
            "value": score.value,
            "awards": score.awards,
            "defects": score.defects,
            "discarded": score.discarded,
        }

    if surface == "settled_core":
        values, reasonless, _raw = score_settled_core(
            judge, item, response, item.id
        )
        return {
            "graded": bool(values),
            "keypoints": values,
            "reasonless": reasonless,
        }

    raise ValueError(f"unknown shadow surface: {surface}")


def run_shadow_units(
    selection,
    *,
    clients,
    items,
    sink,
    now,
    clock=time.perf_counter,
):
    records = []
    for name, _family, _slug in CANDIDATES:
        judge = clients[name]
        for unit in selection:
            started = clock()
            try:
                result = score_shadow_unit(
                    unit,
                    items[unit["item_id"]],
                    judge,
                )
                error = None
            except Exception as exc:
                result = None
                error = f"{type(exc).__name__}: {exc}"
            record = {
                "kind": "shadow_verdict",
                "timestamp": now(),
                "judge": name,
                "surface": unit["surface"],
                "item_id": unit["item_id"],
                "sut_slug": unit["sut_slug"],
                "response_sha256": unit["response_sha256"],
                "elapsed_seconds": max(0, clock() - started),
                "result": result,
                "error": error,
            }
            sink.write(record)
            records.append(record)
    return records
