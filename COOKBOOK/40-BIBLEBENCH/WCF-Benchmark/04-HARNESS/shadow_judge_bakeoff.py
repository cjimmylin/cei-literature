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
from wcfbench.contested import (
    _parse_core_verdicts,
    _score_disclosure,
    score_settled_core,
    settled_core_keypoints,
)
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


def write_text_new(path, text):
    with open(path, "x", encoding="utf-8") as fh:
        fh.write(text)


def resolve_candidates(catalog):
    slugs = [slug for _name, _family, slug in CANDIDATES]
    mvp.validate_slugs(slugs, catalog)
    for slug in slugs:
        mvp.price_for(slug, catalog)
    return CANDIDATES


def validate_options(budget):
    if budget <= 0 or budget > MAX_BUDGET:
        raise PreflightError(
            f"shadow budget must be >$0 and <=${MAX_BUDGET:.2f}; "
            f"received ${budget:.2f}"
        )


class TimingClient:
    def __init__(
        self,
        inner,
        *,
        name,
        slug,
        sink,
        now,
        clock=time.perf_counter,
    ):
        self.inner = inner
        self.name = name
        self.slug = slug
        self.sink = sink
        self.now = now
        self.clock = clock

    def __getattr__(self, name):
        return getattr(self.inner, name)

    def complete(self, prompt, item_id=None):
        started = self.clock()
        error = None
        try:
            return self.inner.complete(prompt, item_id=item_id)
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"
            raise
        finally:
            self.sink.write(
                {
                    "kind": "call_timing",
                    "timestamp": self.now(),
                    "judge": self.name,
                    "slug": self.slug,
                    "item_id": item_id,
                    "elapsed_seconds": max(0.0, self.clock() - started),
                    "error": error,
                }
            )


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
        expected_indices = set(range(1, len(tagged) + 1))
        awards = {
            index: value
            for index, value in verdict.awards.items()
            if index in expected_indices
        }
        compliance_defects = {
            index: value
            for index, value in verdict.compliance_defects.items()
            if index in expected_indices
        }
        return {
            "graded": bool(awards),
            "awards": awards,
            "compliance_defects": compliance_defects,
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
        values, reasonless, raw = score_settled_core(
            judge, item, response, item.id
        )
        explicit_components, _parsed_reasonless = _parse_core_verdicts(
            raw,
            settled_core_keypoints(item),
            require_reason=True,
        )
        return {
            "graded": bool(explicit_components),
            "keypoints": values,
            "reasonless": reasonless,
        }

    raise ValueError(f"unknown shadow surface: {surface}")


def _canonical_json(value):
    return json.loads(json.dumps(value, ensure_ascii=False))


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
            record = _canonical_json(record)
            sink.write(record)
            records.append(record)
    return records


@dataclass
class ShadowOutcome:
    paths: Dict[str, str]
    qualifications: Dict[str, Any]
    verdicts: List[Dict[str, Any]]
    internal_total_usd: float
    partial_reason: Optional[str]


def build_metadata(
    *,
    catalog,
    budget,
    internal_total,
    partial_reason,
    qualifications,
    verdicts,
    key_before,
    key_after,
):
    if internal_total > budget and not partial_reason:
        partial_reason = (
            f"actual internal total ${internal_total:.4f} exceeded "
            f"budget ${budget:.2f}"
        )
    return {
        "artifact_kind": "SHADOW / NOT A QUALIFICATION MANIFEST",
        "run_status": "PARTIAL" if partial_reason else "COMPLETE",
        "candidates": [
            {
                "name": name,
                "family": family,
                "slug": slug,
                "pricing": catalog[slug].get("pricing", {}),
            }
            for name, family, slug in CANDIDATES
        ],
        "k": K,
        "threshold": THRESHOLD,
        "surface_counts": SURFACE_COUNTS,
        "budget_usd": budget,
        "internal_total_usd": internal_total,
        "partial_reason": partial_reason,
        "qualification_complete": len(qualifications) == len(CANDIDATES),
        "shadow_verdicts_recorded": len(verdicts),
        "key_before": key_before,
        "key_after": key_after,
    }


def build_report(metadata, qualifications, verdicts, selection):
    status = metadata["run_status"]
    return "\n".join(
        [
            "# WCF-Bench — Shadow Judge Bakeoff",
            "",
            "**SHADOW / NOT A QUALIFICATION MANIFEST**",
            "",
            f"Run status: **{status}**",
            "",
            f"partial_reason: {metadata.get('partial_reason')}",
            "",
        ]
    )


def execute_live(
    api_key,
    *,
    out_dir=RUN_DIR,
    budget=MAX_BUDGET,
    key_fetch=mvp.fetch_key_snapshot,
    catalog_fetch=mvp.fetch_model_catalog,
    client_builder=OpenRouterModelClient,
    qualify_fn=qualify_judge,
    selection_fn=build_selection,
    score_fn=run_shadow_units,
    now=lambda: datetime.datetime.now().isoformat(timespec="seconds"),
):
    if os.path.exists(out_dir):
        raise OutputPathError(
            f"append-only output path already exists: {out_dir}"
        )
    validate_options(budget)

    key_before = fetch_with_two_retries(key_fetch, api_key)
    require_preflight(key_before, budget)
    catalog = fetch_with_two_retries(catalog_fetch, api_key)
    resolve_candidates(catalog)
    assert_template_hashes(load_manifest(MANIFEST_PATH))
    selection = selection_fn(
        open_path=OPEN_PATH,
        floor_path=FLOOR_PATH,
        r33_path=R33_PATH,
        bank_dir=BANK_DIR,
    )

    os.makedirs(out_dir, exist_ok=False)
    selection_path = os.path.join(out_dir, "selection.json")
    raw_path = os.path.join(out_dir, "raw_verdicts.jsonl")
    metadata_path = os.path.join(out_dir, "shadow-run-metadata.json")
    report_path = os.path.join(
        out_dir, "20260712-shadow-judge-bakeoff-report.md"
    )
    clients = {}
    qualifications = {}
    verdicts = []
    guard = None
    internal = 0.0
    key_after = None
    partial_reasons = []

    try:
        write_json_new(
            selection_path,
            {
                "seed": SEED,
                "surface_counts": SURFACE_COUNTS,
                "units": selection,
            },
        )
        sink = JsonlSink(raw_path)
        sink.touch()
        guard = BudgetGuard(budget, catalog)
        for name, family, slug in CANDIDATES:
            inner = client_builder(
                model=slug,
                api_key=api_key,
                temperature=0.0,
                max_tokens=JUDGE_MAX_TOKENS,
            )
            guard.register(slug, inner)
            timed = TimingClient(
                inner,
                name=name,
                slug=slug,
                sink=sink,
                now=now,
            )
            clients[name] = CapturingClient(
                timed,
                name=name,
                family=family,
                slug=slug,
                guard=guard,
                sink=sink,
                now=now,
            )

        qualifications = run_shadow_batteries(
            client_factory=lambda name, _family, _slug: clients[name],
            qualify_fn=qualify_fn,
            sink=sink,
            now=now,
        )
        items = {item.id: item for item in load_items(BANK_DIR)}
        verdicts = score_fn(
            selection,
            clients=clients,
            items=items,
            sink=sink,
            now=now,
        )
    except Exception as exc:
        partial_reasons.append(f"{type(exc).__name__}: {exc}")

    if guard is not None:
        try:
            internal = guard.total_usd()
        except Exception as exc:
            partial_reasons.append(
                f"accounting failure: {type(exc).__name__}: {exc}"
            )
        else:
            if internal > budget:
                partial_reasons.append(
                    f"actual internal total ${internal:.4f} exceeded "
                    f"budget ${budget:.2f}"
                )
            elif guard.hit and not partial_reasons:
                partial_reasons.append(
                    f"budget guard stopped at ${budget:.2f} cap"
                )

    try:
        key_after = fetch_with_two_retries(key_fetch, api_key)
    except Exception as exc:
        partial_reasons.append(
            f"key-after snapshot failure: {type(exc).__name__}: {exc}"
        )

    partial_reason = "; ".join(partial_reasons) or None
    metadata = build_metadata(
        catalog=catalog,
        budget=budget,
        internal_total=internal,
        partial_reason=partial_reason,
        qualifications=qualifications,
        verdicts=verdicts,
        key_before=key_before,
        key_after=key_after,
    )
    write_json_new(metadata_path, metadata)
    write_text_new(
        report_path,
        build_report(metadata, qualifications, verdicts, selection),
    )
    paths = {
        "selection": selection_path,
        "raw": raw_path,
        "metadata": metadata_path,
        "report": report_path,
    }
    return ShadowOutcome(
        paths,
        qualifications,
        verdicts,
        internal,
        partial_reason,
    )
