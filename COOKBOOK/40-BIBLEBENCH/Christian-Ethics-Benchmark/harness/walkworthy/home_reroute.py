"""PR-16 FR-7 derived-run materialization for Google-judge 05/06 flags.

The W1 and W2 artifacts are immutable inputs.  Exactly the Google-SUT cells in designs
05 and 06 are recomputed from the surviving OpenAI judge plus the registered Mistral
tie-breaker.  Google never participates in the replacement value.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import date
from pathlib import Path

from .adjudication import (AGREED, EXCLUDED_DEFECT, EXCLUDED_DISAGREEMENT,
                           adjudicated_value)
from .clients import Message
from .live_judges import JUDGE_SYSTEM, parse_verdict
from .rubrics import spec_for
from .tiebreak import _cost_delta, rubric_prompt_for_unit

SURVIVING_JUDGE = "openai/gpt-4.1-mini"
DISQUALIFIED_JUDGE = "google/gemini-2.5-flash"
MISTRAL_MODEL = "mistralai/mistral-large-2512"
GOOGLE_SUT = "google/gemini-2.5-pro"
TARGET_CATEGORIES = {
    "05-ordoamoris": ("rationale_honesty",),
    "06-crookedpath": ("frame", "facts", "principles", "alternatives",
                       "resolution", "remainder", "pastoral"),
}
PRODUCTION_RECORDS = 2064
PRODUCTION_UNITS = 63
PRODUCTION_CELLS = 249
PRODUCTION_REUSED = 11
PRODUCTION_NEW = 52
AUTHORIZED_SOURCE_RUN = "20260712-o5-tiebreak"


def _normalise_judge(name: str) -> str:
    return str(name).removeprefix("or:")


def _key(item_id, model, unit_key="item") -> tuple[str, str, str]:
    return str(item_id), str(model), str(unit_key)


def _events_by_key(events) -> dict:
    result = {}
    for event in events:
        key = _key(event.get("item_id"), event.get("model"), event.get("unit_key"))
        if key in result:
            raise ValueError(f"duplicate FR-7 event key: {key}")
        result[key] = event
    return result


def _complete_reusable(event: dict | None, categories: tuple[str, ...]) -> bool:
    if (not event or event.get("tiebreaker_model") != MISTRAL_MODEL
            or event.get("route") != "tie_breaker"):
        return False
    if event.get("defects"):
        return False
    scores = event.get("scores")
    return isinstance(scores, dict) and all(scores.get(name) is not None
                                            for name in categories)


def plan_home_reroute(records: list, source_events: list) -> list:
    """Return the deterministic 05/06 Google-SUT item-unit plan."""
    reusable = _events_by_key(source_events)
    plan = []
    seen = set()
    for index, record in enumerate(records):
        design = record.get("design")
        if design not in TARGET_CATEGORIES or record.get("model") != GOOGLE_SUT:
            continue
        key = _key(record.get("item_id"), record.get("model"))
        if key in seen:
            raise ValueError(f"duplicate selected FR-7 record key: {key}")
        seen.add(key)
        categories = TARGET_CATEGORIES[design]
        source_event = reusable.get(key)
        prior_cells = ((record.get("judge_report") or {}).get("disagreements") or [])
        superseded = sum(
            str(cell.get("cell")) in categories
            and cell.get("adjudication_status") == "part_b_ambiguous_tolerance"
            for cell in prior_cells)
        plan.append({
            "record_index": index,
            "item_id": record["item_id"],
            "design": design,
            "model": record["model"],
            "unit_key": "item",
            "categories": categories,
            "superseded_pr15_cells": superseded,
            "source": ("reused_w1" if _complete_reusable(source_event, categories)
                       else "new_call"),
            "source_event": source_event if _complete_reusable(source_event, categories)
                            else None,
        })
    return plan


def _surviving_scores(record: dict) -> dict:
    verdicts = (record.get("judge_report") or {}).get("verdicts") or []
    matches = [v for v in verdicts if _normalise_judge(v.get("judge")) == SURVIVING_JUDGE]
    disqualified = [v for v in verdicts
                    if _normalise_judge(v.get("judge")) == DISQUALIFIED_JUDGE]
    if len(matches) != 1 or len(disqualified) != 1:
        raise ValueError(
            f"{record.get('item_id')}: expected one surviving OpenAI and one "
            "disqualified Google verdict")
    return matches[0].get("scores") or {}


def _upsert_disagreement(report: dict, category_name: str, a, b, value, status: str) -> dict:
    cells = report.setdefault("disagreements", [])
    cell = next((candidate for candidate in cells
                 if str(candidate.get("cell")) == category_name), None)
    if cell is None:
        cell = {"cell": category_name}
        cells.append(cell)
    cell.update({
        "values": [a, b],
        "adjudicated": value,
        "needs_adjudication": status != AGREED,
        "replacement_judges": [SURVIVING_JUDGE, MISTRAL_MODEL],
        "disqualified_judge": DISQUALIFIED_JUDGE,
        "tiebreaker_model": MISTRAL_MODEL,
        "tiebreaker_value": b,
        "adjudication_status": {
            AGREED: "home_reroute_resolved",
            EXCLUDED_DISAGREEMENT: "part_b_home_reroute_disagreement",
            EXCLUDED_DEFECT: "part_b_home_reroute_defect",
        }[status],
    })
    return cell


def apply_replacement_pair(record: dict, mistral_scores: dict | None,
                           event_source: str | None = None) -> dict:
    """Replace only the ratified target cells using OpenAI + Mistral."""
    design = record.get("design")
    if design not in TARGET_CATEGORIES or record.get("model") != GOOGLE_SUT:
        return deepcopy(record)
    out = deepcopy(record)
    report = out.setdefault("judge_report", {})
    derived = report.get("adjudicated_verdict")
    if not isinstance(derived, dict) or not isinstance(derived.get("scores"), dict):
        raise ValueError(f"{record.get('item_id')}: missing W1 adjudicated item verdict")
    openai_scores = _surviving_scores(out)
    mistral_scores = mistral_scores or {}
    cell_rows = []
    for name in TARGET_CATEGORIES[design]:
        category = next(c for c in spec_for(design).categories if c.name == name)
        a, b = openai_scores.get(name), mistral_scores.get(name)
        value, status = adjudicated_value(category, a, b)
        derived["scores"][name] = value if status == AGREED else None
        cell = _upsert_disagreement(report, name, a, b, value, status)
        cell_rows.append({"cell": name, "status": cell["adjudication_status"],
                          "value": cell["adjudicated"]})
    report["home_reroute"] = {
        "ruling": "PR-16-option-1",
        "disqualified_judge": DISQUALIFIED_JUDGE,
        "replacement_judges": [SURVIVING_JUDGE, MISTRAL_MODEL],
        "event_source": event_source,
        "cells": cell_rows,
    }
    derived["judge"] = "derived:pair-plus-tiebreak-plus-fr7-reroute"
    return out


def _read_checkpoint(path: Path) -> dict:
    if not path.exists():
        return {}
    events = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid FR-7 checkpoint JSON at line {line_no}") from exc
    return _events_by_key(events)


def _zero_cost() -> dict:
    return {"usd": 0.0, "calls": 0, "prompt_tokens": 0, "completion_tokens": 0}


def validate_nonselected_invariance(source: list, derived: list, plan: list) -> None:
    """Prove that only the selected records' selected rubric cells changed."""
    if len(source) != len(derived):
        raise ValueError("PR-16 nonselected invariance failed: record count changed")
    selected = {unit["record_index"]: set(unit["categories"]) for unit in plan}
    for index, (before, after) in enumerate(zip(source, derived)):
        if index not in selected:
            if before != after:
                raise ValueError(
                    f"PR-16 nonselected invariance failed at record {index}")
            continue
        categories = selected[index]
        b = deepcopy(before)
        a = deepcopy(after)
        b_report = b.get("judge_report") or {}
        a_report = a.get("judge_report") or {}
        b_disagreements = b_report.get("disagreements") or []
        a_disagreements = a_report.get("disagreements") or []
        b_other = [cell for cell in b_disagreements
                   if str(cell.get("cell")) not in categories]
        a_other = [cell for cell in a_disagreements
                   if str(cell.get("cell")) not in categories]
        if b_other != a_other:
            raise ValueError(
                f"PR-16 nonselected cell invariance failed at record {index}")
        a_report["disagreements"] = deepcopy(b_disagreements)
        a_report.pop("home_reroute", None)
        b_derived = b_report.get("adjudicated_verdict") or {}
        a_derived = a_report.get("adjudicated_verdict") or {}
        a_derived["judge"] = b_derived.get("judge")
        for category in categories:
            (a_derived.get("scores") or {})[category] = \
                (b_derived.get("scores") or {}).get(category)
        if a != b:
            raise ValueError(
                f"PR-16 nonselected field invariance failed at record {index}")


def _validate_checkpoint_event(event: dict, unit: dict) -> None:
    expected = {
        "item_id": unit["item_id"], "design": unit["design"],
        "model": unit["model"], "unit_key": unit["unit_key"],
        "route": "home_reroute", "source": unit["source"],
        "tiebreaker_model": MISTRAL_MODEL,
    }
    mismatches = [f"{field}={event.get(field)!r} expected {value!r}"
                  for field, value in expected.items() if event.get(field) != value]
    scores = event.get("scores")
    if not isinstance(scores, dict):
        mismatches.append("scores is not an object")
    elif not event.get("defects") and any(scores.get(name) is None
                                           for name in unit["categories"]):
        mismatches.append("defect-free event lacks a selected score")
    if unit["source"] == "reused_w1" and (event.get("cost") or {}) != _zero_cost():
        mismatches.append("reused event has nonzero incremental cost")
    if mismatches:
        raise ValueError("FR-7 checkpoint provenance mismatch: " + "; ".join(mismatches))


def run_home_reroute(records: list, items_by_id: dict, client, source_events: list,
                     checkpoint_path, cost_probe=None,
                     max_new_units: int | None = None,
                     source_run: str = AUTHORIZED_SOURCE_RUN) -> tuple[list, dict]:
    """Run/resume the append-only 63-unit replacement computation."""
    checkpoint = Path(checkpoint_path)
    checkpoint.parent.mkdir(parents=True, exist_ok=True)
    cached = _read_checkpoint(checkpoint)
    plan = plan_home_reroute(records, source_events)
    planned_keys = {_key(unit["item_id"], unit["model"], unit["unit_key"])
                    for unit in plan}
    extras = sorted(set(cached) - planned_keys)
    if extras:
        raise ValueError(f"PR-16 unexpected checkpoint keys: {extras[:3]}")
    out = deepcopy(records)
    processed = 0
    checkpointed = 0
    new_this_invocation = 0

    with checkpoint.open("a", encoding="utf-8") as handle:
        for unit in plan:
            key = _key(unit["item_id"], unit["model"], unit["unit_key"])
            event = cached.get(key)
            if event is not None:
                _validate_checkpoint_event(event, unit)
                checkpointed += 1
            elif unit["source"] == "reused_w1":
                source = unit["source_event"]
                event = {
                    "item_id": unit["item_id"], "design": unit["design"],
                    "model": unit["model"], "unit_key": unit["unit_key"],
                    "route": "home_reroute", "source": "reused_w1",
                    "source_run": source_run,
                    "tiebreaker_model": MISTRAL_MODEL,
                    "scores": deepcopy(source["scores"]), "defects": [],
                    "cost": _zero_cost(), "source_cost": deepcopy(source.get("cost") or {}),
                }
                handle.write(json.dumps(event, ensure_ascii=False) + "\n")
                handle.flush()
                cached[key] = event
                _validate_checkpoint_event(event, unit)
            else:
                if max_new_units is not None and new_this_invocation >= max_new_units:
                    break
                item = items_by_id.get(unit["item_id"])
                if item is None:
                    raise ValueError(f"missing public item for {unit['item_id']}")
                before = cost_probe() if cost_probe else None
                prompt = rubric_prompt_for_unit(
                    item, out[unit["record_index"]], unit["categories"][0])
                response = client.complete([Message("user", prompt)], system=JUDGE_SYSTEM)
                scores, defects = parse_verdict(response.text, spec_for(unit["design"]))
                after = cost_probe() if cost_probe else None
                event = {
                    "item_id": unit["item_id"], "design": unit["design"],
                    "model": unit["model"], "unit_key": unit["unit_key"],
                    "route": "home_reroute", "source": "new_call",
                    "tiebreaker_model": MISTRAL_MODEL, "scores": scores,
                    "defects": defects or [], "cost": _cost_delta(before, after),
                }
                handle.write(json.dumps(event, ensure_ascii=False) + "\n")
                handle.flush()
                cached[key] = event
                _validate_checkpoint_event(event, unit)
                new_this_invocation += 1
            index = unit["record_index"]
            out[index] = apply_replacement_pair(
                out[index], event.get("scores"), event_source=event.get("source"))
            processed += 1

    selected_keys = {_key(unit["item_id"], unit["model"], unit["unit_key"])
                     for unit in plan[:processed]}
    used_events = [cached[key] for key in selected_keys]
    status_counts = Counter()
    by_design = defaultdict(Counter)
    for unit in plan[:processed]:
        reroute = out[unit["record_index"]]["judge_report"]["home_reroute"]
        for cell in reroute["cells"]:
            status_counts[cell["status"]] += 1
            by_design[unit["design"]][cell["status"]] += 1
    cost = {
        "usd": round(sum(float((e.get("cost") or {}).get("usd", 0))
                         for e in used_events), 8),
        "calls": sum(int((e.get("cost") or {}).get("calls", 0)) for e in used_events),
        "prompt_tokens": sum(int((e.get("cost") or {}).get("prompt_tokens", 0))
                             for e in used_events),
        "completion_tokens": sum(int((e.get("cost") or {}).get("completion_tokens", 0))
                                 for e in used_events),
    }
    validate_nonselected_invariance(records, out, plan)
    summary = {
        "ruling": "PR-16-option-1",
        "selected_units": len(plan),
        "selected_cells": sum(len(unit["categories"]) for unit in plan),
        "reused_w1_units": sum(unit["source"] == "reused_w1" for unit in plan),
        "new_call_units": sum(unit["source"] == "new_call" for unit in plan),
        "superseded_pr15_cells": sum(unit["superseded_pr15_cells"] for unit in plan),
        "checkpointed_units": checkpointed,
        "new_units_this_invocation": new_this_invocation,
        "processed_units": processed,
        "resolved_cells": status_counts["home_reroute_resolved"],
        "part_b_disagreement_cells": status_counts[
            "part_b_home_reroute_disagreement"],
        "part_b_defect_cells": status_counts["part_b_home_reroute_defect"],
        "complete": processed == len(plan),
        "surviving_judge": SURVIVING_JUDGE,
        "disqualified_judge": DISQUALIFIED_JUDGE,
        "tiebreaker_model": MISTRAL_MODEL,
        "by_design": {design: dict(counts) for design, counts in sorted(by_design.items())},
        "cost": cost,
    }
    return out, summary


def _read_jsonl(path: Path) -> list:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def _write_jsonl(path: Path, records: list) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def _validate_production(records: list, plan: list) -> None:
    keys = [(record.get("item_id"), record.get("model")) for record in records]
    if len(records) != PRODUCTION_RECORDS or len(keys) != len(set(keys)):
        raise ValueError("PR-16 production input must contain 2,064 unique records")
    actual = (len(plan), sum(len(unit["categories"]) for unit in plan),
              sum(unit["source"] == "reused_w1" for unit in plan),
              sum(unit["source"] == "new_call" for unit in plan),
              sum(unit["superseded_pr15_cells"] for unit in plan))
    expected = (PRODUCTION_UNITS, PRODUCTION_CELLS, PRODUCTION_REUSED, PRODUCTION_NEW, 11)
    if actual != expected:
        raise ValueError(f"PR-16 production surface mismatch: {actual} != {expected}")


def _validate_source_summary(summary: dict) -> None:
    expected = {
        "groups": 2682, "cells": 3176, "tie_breaker_units": 2224,
        "own_family_units": 458, "processed_groups": 2682,
        "ambiguous_tolerance_cells": 0, "complete": True,
        "tiebreaker_model": MISTRAL_MODEL,
    }
    changed = [f"{field}={summary.get(field)!r} expected {value!r}"
               for field, value in expected.items() if summary.get(field) != value]
    if changed:
        raise ValueError("PR-16 source W1 provenance mismatch: " + "; ".join(changed))


def _public_run_dir(root: Path, run_name: str) -> Path:
    part = Path(run_name)
    if (part.is_absolute() or len(part.parts) != 1 or run_name in (".", "..")
            or "HOLDOUT" in run_name.upper()):
        raise SystemExit("PR-16 is restricted to named PUBLIC runs directories")
    runs = (root / "runs").resolve()
    candidate = (runs / run_name).resolve()
    if runs not in candidate.parents:
        raise SystemExit("PR-16 is restricted to named PUBLIC runs directories")
    return candidate


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="WALKWORTHY PR-16 FR-7 reroute")
    parser.add_argument("--benchmark-root", default=str(Path(__file__).resolve().parents[2]))
    parser.add_argument("--source-run", required=True)
    parser.add_argument("--out-run", required=True)
    parser.add_argument("--date", default=None)
    parser.add_argument("--surviving-judge", required=True)
    parser.add_argument("--disqualified-judge", required=True)
    parser.add_argument("--tiebreaker-model", required=True)
    parser.add_argument("--max-new-units", type=int, default=None)
    args = parser.parse_args(argv)
    explicit = (args.surviving_judge, args.disqualified_judge, args.tiebreaker_model)
    frozen = (SURVIVING_JUDGE, DISQUALIFIED_JUDGE, MISTRAL_MODEL)
    if explicit != frozen:
        raise SystemExit(f"PR-16 requires explicit frozen models: {frozen}")
    if args.source_run == args.out_run:
        raise SystemExit("PR-16 output must be a NEW derived run")
    if any("HOLDOUT" in value.upper() for value in
           (str(args.benchmark_root), args.source_run, args.out_run)):
        raise SystemExit("PR-16 is restricted to PUBLIC runs")

    root = Path(args.benchmark_root).resolve()
    source_dir = _public_run_dir(root, args.source_run)
    out_dir = _public_run_dir(root, args.out_run)
    if args.source_run != AUTHORIZED_SOURCE_RUN:
        raise SystemExit(f"PR-16 source is pinned to {AUTHORIZED_SOURCE_RUN}")

    from . import openrouter_backend as orb
    from .loader import load_public_split
    from .smoke import _cost_tracking_transport

    completed_summary = out_dir / "home_reroute_summary.json"
    if completed_summary.exists():
        try:
            prior = json.loads(completed_summary.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise SystemExit("PR-16 STOP: existing derived summary is invalid") from exc
        if prior.get("complete") is True:
            raise SystemExit("PR-16 derived run is immutable after completion")
    source_scored = source_dir / "scored_items.jsonl"
    source_events_path = source_dir / "tiebreak_events.jsonl"
    source_summary_path = source_dir / "tiebreak_summary.json"
    for required in (source_scored, source_events_path, source_summary_path):
        if not required.is_file():
            raise SystemExit(f"missing PR-16 source artifact: {required}")
    records = _read_jsonl(source_scored)
    source_events = _read_jsonl(source_events_path)
    source_summary = json.loads(source_summary_path.read_text(encoding="utf-8"))
    _validate_source_summary(source_summary)
    plan = plan_home_reroute(records, source_events)
    _validate_production(records, plan)
    items = {item.id: item for item in load_public_split(
        str(root), include_exemplars=True, runnable_only=True)}

    key = orb.load_openrouter_key()
    if not key:
        raise SystemExit("PR-16: no OpenRouter key")
    transport = _cost_tracking_transport()
    client = orb.OpenRouterClient(MISTRAL_MODEL, model=MISTRAL_MODEL, api_key=key,
                                  transport=transport)
    out_dir.mkdir(parents=True, exist_ok=True)
    derived, summary = run_home_reroute(
        records, items, client, source_events, out_dir / "home_reroute_events.jsonl",
        cost_probe=lambda: dict(transport.acc), max_new_units=args.max_new_units,
        source_run=args.source_run)
    summary.update({"date": args.date or f"{date.today():%Y%m%d}",
                    "source_run": args.source_run, "out_run": args.out_run,
                    "source_records": len(records), "derived_records": len(derived)})
    _write_jsonl(out_dir / "scored_items.jsonl", derived)
    target_w1 = out_dir / "tiebreak_summary.json"
    if target_w1.exists():
        if json.loads(target_w1.read_text(encoding="utf-8")) != source_summary:
            raise SystemExit("PR-16 STOP: derived run W1 provenance changed")
    else:
        target_w1.write_text(json.dumps(source_summary, indent=2) + "\n", encoding="utf-8")
    (out_dir / "home_reroute_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if not summary["complete"]:
        raise SystemExit("PR-16 incomplete; resume the same output run")
    if (summary["selected_units"], summary["selected_cells"],
            summary["reused_w1_units"], summary["new_call_units"]) != (
                PRODUCTION_UNITS, PRODUCTION_CELLS, PRODUCTION_REUSED, PRODUCTION_NEW):
        raise SystemExit("PR-16 STOP: final acceptance counts changed")
    if summary["superseded_pr15_cells"] != 11:
        raise SystemExit("PR-16 STOP: expected exactly 11 superseded PR-15 cells")
    if (summary["resolved_cells"] + summary["part_b_disagreement_cells"]
            + summary["part_b_defect_cells"] != PRODUCTION_CELLS):
        raise SystemExit("PR-16 STOP: not every selected cell has a final route")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
