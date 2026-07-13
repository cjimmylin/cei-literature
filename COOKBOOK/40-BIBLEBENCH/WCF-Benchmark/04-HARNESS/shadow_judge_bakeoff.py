#!/usr/bin/env python
"""Approved shadow-judge bakeoff runner."""

from __future__ import annotations

import argparse
from collections import Counter
import datetime
import hashlib
import json
import math
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


def _finite_nonnegative(value):
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
        and value >= 0
    )


def _finite_nonnegative_integer(value):
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and value >= 0
    )


def validate_key_snapshot(snapshot, label):
    if not isinstance(snapshot, dict):
        raise PreflightError(f"{label} key snapshot must be an object")
    for field in ("usage", "limit", "limit_remaining"):
        value = snapshot.get(field)
        if value is not None and not _finite_nonnegative(value):
            raise PreflightError(
                f"{label} {field} must be finite and nonnegative"
            )
    return snapshot


def resolve_candidates(catalog):
    slugs = [slug for _name, _family, slug in CANDIDATES]
    mvp.validate_slugs(slugs, catalog)
    for slug in slugs:
        prompt_price, completion_price = mvp.price_for(slug, catalog)
        if not all(
            _finite_nonnegative(value)
            for value in (prompt_price, completion_price)
        ):
            raise PreflightError(
                f"catalog prices for {slug!r} must be finite and nonnegative"
            )
    return CANDIDATES


def validate_options(budget):
    if (
        not isinstance(budget, (int, float))
        or isinstance(budget, bool)
        or not math.isfinite(float(budget))
        or budget <= 0
        or budget > MAX_BUDGET
    ):
        raise PreflightError(
            f"shadow budget must be >$0 and <=${MAX_BUDGET:.2f}; "
            f"received ${budget:.2f}"
        )


class TimingLinkedSink(JsonlSink):
    def __init__(self, path):
        super().__init__(path)
        self._next_timing_sequence = 0
        self._pending_by_judge = {}

    def write(self, record):
        linked = dict(record)
        kind = linked.get("kind")
        judge = linked.get("judge")
        if kind == "call_timing":
            self._next_timing_sequence += 1
            sequence = self._next_timing_sequence
            linked["timing_sequence"] = sequence
            self._pending_by_judge.setdefault(judge, []).append(sequence)
        elif kind == "raw_call":
            pending = self._pending_by_judge.get(judge, [])
            if not pending:
                raise RuntimeError(
                    f"raw_call for {judge!r} has no pending call_timing record"
                )
            linked["timing_sequence"] = pending.pop(0)
        super().write(linked)


class StrictCapturingClient(CapturingClient):
    @staticmethod
    def _usable_usage(entries):
        if not entries:
            return False
        for entry in entries:
            usage = (entry or {}).get("usage")
            if not isinstance(usage, dict):
                return False
            for field in (
                "prompt_tokens",
                "completion_tokens",
                "total_tokens",
            ):
                if field in usage and not _finite_nonnegative_integer(
                    usage[field]
                ):
                    return False
            cost = usage.get("cost")
            has_cost = cost not in (None, "")
            if has_cost and not _finite_nonnegative(cost):
                return False
            has_tokens = (
                "prompt_tokens" in usage
                and "completion_tokens" in usage
            )
            if not has_cost and not has_tokens:
                return False
        return True


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


def build_reconciliation(*, internal_total, key_before, key_after, budget):
    result = {
        "status": "UNRECONCILED",
        "internal_total_usd": internal_total,
        "key_usage_delta_usd": None,
        "within_20_percent": None,
        "unavailable_reason": None,
    }
    if not _finite_nonnegative(internal_total):
        result["unavailable_reason"] = (
            "internal total must be finite and nonnegative"
        )
        return result
    if key_after is None:
        result["unavailable_reason"] = "key-after usage unavailable"
        return result
    before_usage = key_before.get("usage") if isinstance(key_before, dict) else None
    after_usage = key_after.get("usage") if isinstance(key_after, dict) else None
    if before_usage is None or after_usage is None:
        result["unavailable_reason"] = "key usage unavailable"
        return result
    if not _finite_nonnegative(before_usage) or not _finite_nonnegative(
        after_usage
    ):
        result["unavailable_reason"] = (
            "key usage must be finite and nonnegative"
        )
        return result

    delta = after_usage - before_usage
    if not math.isfinite(delta):
        result["unavailable_reason"] = "key usage delta must be finite"
        return result
    if delta < 0:
        result["unavailable_reason"] = "key usage delta is negative"
        return result
    result["key_usage_delta_usd"] = delta
    if internal_total > budget or delta > budget:
        result["within_20_percent"] = False
        result["unavailable_reason"] = "accounting total exceeded budget"
        return result

    if delta == 0:
        within = abs(internal_total) <= 1e-9
    else:
        within = abs(internal_total - delta) <= 0.2 * delta
    result["within_20_percent"] = within
    if not within:
        result["unavailable_reason"] = (
            "internal and key totals differ by more than 20%"
        )
        return result
    result["status"] = "RECONCILED"
    return result


def _qualification_coverage_complete(qualifications):
    expected = {name: (family, slug) for name, family, slug in CANDIDATES}
    if set(qualifications) != set(expected):
        return False
    for name, (family, slug) in expected.items():
        qualification = qualifications[name]
        if not isinstance(qualification, JudgeQualification):
            return False
        if (
            qualification.name != name
            or qualification.family != family
            or qualification.slug != slug
            or qualification.k != K
            or set(qualification.probe_reps) != set(PROBES)
        ):
            return False
        for probe in PROBES:
            reps = qualification.probe_reps[probe]
            if (
                reps.k != K
                or len(reps.reps) != K
                or {record.get("rep") for record in reps.reps}
                != set(range(K))
            ):
                return False
    return True


def assess_evidence(selection, qualifications, raw_records):
    surface_counts = {
        surface: sum(unit.get("surface") == surface for unit in selection)
        for surface in SURFACE_COUNTS
    }
    selection_complete = (
        len(selection) == sum(SURFACE_COUNTS.values())
        and surface_counts == SURFACE_COUNTS
    )
    qualification_complete = _qualification_coverage_complete(qualifications)

    probe_records = [
        record for record in raw_records if record.get("kind") == "probe_rep"
    ]
    expected_probes = Counter(
        (name, probe, rep)
        for name, _family, _slug in CANDIDATES
        for probe in PROBES
        for rep in range(K)
    )
    actual_probes = Counter(
        (record.get("judge"), record.get("probe"), record.get("rep"))
        for record in probe_records
    )
    probe_coverage_complete = actual_probes == expected_probes

    verdict_records = [
        record
        for record in raw_records
        if record.get("kind") == "shadow_verdict"
    ]
    expected_verdicts = Counter(
        (
            name,
            unit.get("surface"),
            unit.get("item_id"),
            unit.get("sut_slug"),
            unit.get("response_sha256"),
        )
        for name, _family, _slug in CANDIDATES
        for unit in selection
    )
    actual_verdicts = Counter(
        (
            record.get("judge"),
            record.get("surface"),
            record.get("item_id"),
            record.get("sut_slug"),
            record.get("response_sha256"),
        )
        for record in verdict_records
    )
    verdict_coverage_complete = (
        len(verdict_records) == 56 and actual_verdicts == expected_verdicts
    )

    timings = [
        record for record in raw_records if record.get("kind") == "call_timing"
    ]
    raw_calls = [
        record for record in raw_records if record.get("kind") == "raw_call"
    ]
    timing_keys = Counter(
        (record.get("judge"), record.get("timing_sequence"))
        for record in timings
    )
    raw_keys = Counter(
        (record.get("judge"), record.get("timing_sequence"))
        for record in raw_calls
    )
    timing_pairs_complete = (
        timing_keys == raw_keys
        and all(key[1] is not None for key in timing_keys)
        and all(count == 1 for count in timing_keys.values())
        and all(count == 1 for count in raw_keys.values())
        and all(
            isinstance(record.get("invocation"), int)
            and isinstance(record.get("attempt"), int)
            for record in raw_calls
        )
    )

    issues = []
    if not selection_complete:
        issues.append("selection is not exact 8/8/6/6 (28 units)")
    if not qualification_complete:
        issues.append("qualification objects lack exact two-candidate K=8 coverage")
    if not probe_coverage_complete:
        issues.append("persisted probe_rep coverage is not exact 96 records")
    if not verdict_coverage_complete:
        issues.append("persisted shadow_verdict coverage is not exact 56 records")
    if not timing_pairs_complete:
        issues.append("call_timing/raw_call attempts are not paired one-to-one")
    return {
        "complete": not issues,
        "selection_complete": selection_complete,
        "qualification_complete": qualification_complete,
        "probe_coverage_complete": probe_coverage_complete,
        "probe_reps_recorded": len(probe_records),
        "verdict_coverage_complete": verdict_coverage_complete,
        "shadow_verdicts_recorded": len(verdict_records),
        "timing_pairs_complete": timing_pairs_complete,
        "issues": issues,
    }


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
    selection=None,
    raw_records=None,
    reconciliation=None,
):
    selection = selection or []
    raw_records = raw_records or []
    evidence = assess_evidence(selection, qualifications, raw_records)
    reconciliation = reconciliation or build_reconciliation(
        internal_total=internal_total,
        key_before=key_before,
        key_after=key_after,
        budget=budget,
    )
    reasons = [partial_reason] if partial_reason else []
    if internal_total > budget and not partial_reason:
        reasons.append(
            f"actual internal total ${internal_total:.4f} exceeded "
            f"budget ${budget:.2f}"
        )
    if not evidence["complete"]:
        reasons.append("evidence incomplete: " + "; ".join(evidence["issues"]))
    if reconciliation["status"] != "RECONCILED":
        reasons.append(
            "reconciliation UNRECONCILED: "
            + str(reconciliation["unavailable_reason"])
        )
    partial_reason = "; ".join(dict.fromkeys(reasons)) or None
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
        "qualification_complete": evidence["qualification_complete"]
        and evidence["probe_coverage_complete"],
        "probe_reps_recorded": evidence["probe_reps_recorded"],
        "shadow_verdicts_recorded": evidence["shadow_verdicts_recorded"],
        "evidence": evidence,
        "reconciliation": reconciliation,
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
    validate_key_snapshot(key_before, "key-before")
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

    def add_partial_reason(reason):
        if reason and reason not in partial_reasons:
            partial_reasons.append(reason)

    try:
        write_json_new(
            selection_path,
            {
                "seed": SEED,
                "surface_counts": SURFACE_COUNTS,
                "units": selection,
            },
        )
        sink = TimingLinkedSink(raw_path)
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
            clients[name] = StrictCapturingClient(
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
        add_partial_reason(f"{type(exc).__name__}: {exc}")

    if guard is not None:
        if guard.accounting_error:
            add_partial_reason(
                f"accounting error: {guard.accounting_error}"
            )
        if guard.fatal_error:
            add_partial_reason(f"fatal evidence error: {guard.fatal_error}")
        try:
            measured_total = guard.total_usd()
        except Exception as exc:
            add_partial_reason(
                f"accounting failure: {type(exc).__name__}: {exc}"
            )
        else:
            if not _finite_nonnegative(measured_total):
                add_partial_reason(
                    "internal total must be finite and nonnegative"
                )
                internal = 0.0
            else:
                internal = float(measured_total)
            if internal > budget:
                add_partial_reason(
                    f"actual internal total ${internal:.4f} exceeded "
                    f"budget ${budget:.2f}"
                )
            elif guard.hit and not partial_reasons:
                add_partial_reason(
                    f"budget guard stopped at ${budget:.2f} cap"
                )

    try:
        key_after = fetch_with_two_retries(key_fetch, api_key)
        validate_key_snapshot(key_after, "key-after")
    except Exception as exc:
        key_after = None
        add_partial_reason(
            f"key-after snapshot failure: {type(exc).__name__}: {exc}"
        )

    raw_records = []
    if os.path.exists(raw_path):
        try:
            raw_records = read_jsonl(raw_path)
        except Exception as exc:
            add_partial_reason(
                f"raw evidence read failure: {type(exc).__name__}: {exc}"
            )
    verdicts = [
        record
        for record in raw_records
        if record.get("kind") == "shadow_verdict"
    ]
    reconciliation = build_reconciliation(
        internal_total=internal,
        key_before=key_before,
        key_after=key_after,
        budget=budget,
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
        selection=selection,
        raw_records=raw_records,
        reconciliation=reconciliation,
    )
    partial_reason = metadata["partial_reason"]
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
