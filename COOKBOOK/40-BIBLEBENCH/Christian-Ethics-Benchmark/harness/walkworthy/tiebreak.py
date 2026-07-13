"""W1 third-judge mechanics (FR-2, FR-16, FR-17).

The frozen pair's unresolved atomic cells are grouped by original scoring unit so the
tie-breaker receives the same complete rubric prompt once per unit. Mistral-family SUT
cells never enter this model path. Resolution is strictly two-of-three within the
existing scale tolerance; ambiguous non-transitive numeric tolerance is surfaced for
PENDING-RULINGS rather than assigned a value.
"""
from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from copy import deepcopy
from datetime import date
from pathlib import Path

from .adjudication import AGREED, adjudicated_value
from .clients import Message
from .judges import _disagree, assemble_rubric_prompt
from .live_judges import JUDGE_SYSTEM, parse_verdict
from .openrouter_backend import family_from_slug
from .references import bank_reference_provider
from .rubrics import spec_for

TIEBREAKER_MODEL = "mistralai/mistral-large-2512"
TIEBREAKER_FAMILY = "mistralai"
REEXECUTED_DESIGNS = {"02-twomasters", "07-seventyseven"}


def is_own_family_sut(model: str) -> bool:
    return family_from_slug(model or "") == TIEBREAKER_FAMILY


def _record_key(rec: dict) -> tuple:
    return rec.get("item_id"), rec.get("model")


def merge_reexecution(base_records: list, reexecuted_records: list) -> list:
    """Replace 02/07 by exact `(item, model)` key; partial or extra runs fail loud."""
    expected = {_record_key(r) for r in base_records if r.get("design") in REEXECUTED_DESIGNS}
    actual_keys = [_record_key(r) for r in reexecuted_records
                   if r.get("design") in REEXECUTED_DESIGNS]
    actual = set(actual_keys)
    if len(actual_keys) != len(actual):
        raise ValueError("02/07 re-execution contains duplicate item/model keys")
    if expected != actual:
        missing = len(expected - actual)
        extra = len(actual - expected)
        raise ValueError(f"02/07 re-execution coverage mismatch: missing={missing} extra={extra}")
    replacements = {_record_key(r): r for r in reexecuted_records}
    return [deepcopy(replacements[_record_key(r)]) if r.get("design") in REEXECUTED_DESIGNS
            else deepcopy(r) for r in base_records]


def validate_transcript_contract(records: list) -> dict:
    """Fail if any recorded turn/terminal ask lacks its persisted response."""
    turns = terminals = 0
    for rec in records:
        for admin in rec.get("administrations") or []:
            stored = admin.get("turns") or []
            expected = int(admin.get("n_turns", len(stored)))
            if len(stored) != expected:
                raise ValueError(
                    f"{rec.get('item_id')}/{rec.get('model')}/{admin.get('label')}: "
                    f"turn-count mismatch {len(stored)} != {expected}")
            for turn in stored:
                if not str(turn.get("response") or "").strip():
                    raise ValueError(
                        f"{rec.get('item_id')}/{rec.get('model')}/{admin.get('label')}/"
                        f"turn-{turn.get('index')}: missing persisted response")
                turns += 1
            if admin.get("terminal_user_text") is not None:
                if not str(admin.get("terminal_response") or "").strip():
                    raise ValueError(
                        f"{rec.get('item_id')}/{rec.get('model')}/{admin.get('label')}: "
                        "missing persisted terminal response")
                terminals += 1
    return {"records": len(records), "turns": turns, "terminals": terminals}


def _cell_parts(cell_name: str) -> tuple:
    if ":" not in cell_name:
        return None, cell_name
    return tuple(cell_name.split(":", 1))


def scoring_unit(rec: dict, spec, cell_name: str) -> tuple:
    """Return `(unit key, response text, original unit label)` for one cell."""
    prefix, _ = _cell_parts(cell_name)
    administrations = rec.get("administrations") or []
    if spec.unit == "item":
        admin = administrations[0] if administrations else {}
        text = (admin.get("response") or admin.get("terminal_response")
                or admin.get("terminal") or "")
        return "item", text, None

    if spec.unit == "per_turn":
        if prefix is None or not prefix.isdigit():
            raise ValueError(f"per-turn cell lacks numeric unit prefix: {cell_name}")
        index = int(prefix)
        main = next((a for a in administrations if a.get("label") == "main"),
                    administrations[0] if administrations else {})
        turns = main.get("turns") or []
        for turn in turns:
            if int(turn.get("index", -1)) == index:
                return prefix, turn.get("response") or "", f"turn {index}"
        if index == len(turns) + 1 and main.get("terminal_response") is not None:
            return prefix, main.get("terminal_response") or "", "terminal artifact"
        raise ValueError(f"no persisted response for {rec.get('item_id')} cell {cell_name}")

    if prefix is None:
        raise ValueError(f"{spec.unit} cell lacks unit prefix: {cell_name}")
    admin = next((a for a in administrations if a.get("label") == prefix), None)
    if admin is None:
        raise ValueError(f"no administration {prefix} for {rec.get('item_id')}")
    text = (admin.get("response") or admin.get("terminal_response")
            or admin.get("terminal") or "")
    return prefix, text, prefix


def rubric_prompt_for_unit(item, rec: dict, cell_name: str) -> str:
    """Rebuild exactly the prompt text produced for the frozen pair's scoring unit."""
    spec = spec_for(item.design)
    _, response, label = scoring_unit(rec, spec, cell_name)
    refs = bank_reference_provider(item) if spec.reference_anchored else None
    return assemble_rubric_prompt(item, spec, response, references=refs,
                                  unit_label=label)


def group_disagreements(records: list) -> list:
    """Group all real unresolved cells by record and original scoring unit."""
    groups = OrderedDict()
    for record_index, rec in enumerate(records):
        spec = spec_for(rec["design"])
        for cell in ((rec.get("judge_report") or {}).get("disagreements") or []):
            if cell.get("needs_adjudication") is not True:
                continue
            prefix, _ = _cell_parts(str(cell.get("cell", "")))
            unit_key = "item" if spec.unit == "item" else prefix
            key = (record_index, unit_key)
            group = groups.setdefault(key, {
                "record_index": record_index,
                "item_id": rec["item_id"],
                "design": rec["design"],
                "model": rec["model"],
                "unit_key": unit_key,
                "route": ("part_b_own_family" if is_own_family_sut(rec["model"])
                          else "tie_breaker"),
                "cells": [],
            })
            group["cells"].append(cell)
    return list(groups.values())


def resolve_three(category, a, b, third) -> tuple:
    """Return `(value, status)` under unambiguous two-of-three scale agreement."""
    values = (a, b, third)
    if any(v is None for v in values):
        return None, "defect"
    agreeing_values = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        if _disagree(category, values[i], values[j]):
            continue
        value, status = adjudicated_value(category, values[i], values[j])
        if status == AGREED:
            agreeing_values.append(value)
    if not agreeing_values:
        return None, "contested"
    unique = set(agreeing_values)
    if len(unique) == 1:
        return agreeing_values[0], "resolved"
    return None, "ambiguous_tolerance"


def _category(spec, name: str):
    return next((c for c in spec.categories if c.name == name), None)


def apply_group_result(rec: dict, group: dict, third_scores,
                       ambiguous_tolerance_policy: str = "stop") -> dict:
    """Apply one checkpointed unit result to a copy; frozen-pair verdicts stay intact."""
    out = deepcopy(rec)
    spec = spec_for(out["design"])
    wanted = {str(c["cell"]) for c in group["cells"]}
    cells = (out.get("judge_report") or {}).get("disagreements") or []
    for cell in cells:
        if str(cell.get("cell")) not in wanted or cell.get("needs_adjudication") is not True:
            continue
        if group["route"] == "part_b_own_family":
            cell["adjudication_status"] = "part_b_own_family"
            cell["tiebreaker_model"] = TIEBREAKER_MODEL
            continue
        _, category_name = _cell_parts(str(cell["cell"]))
        category = _category(spec, category_name)
        third = (third_scores or {}).get(category_name)
        value, status = resolve_three(category, *(cell.get("values") or [None, None])[:2],
                                      third)
        cell["tiebreaker_model"] = TIEBREAKER_MODEL
        cell["tiebreaker_value"] = third
        if status == "resolved":
            cell["adjudicated"] = value
            cell["needs_adjudication"] = False
            cell["adjudication_status"] = "tiebreak_resolved"
        elif status == "ambiguous_tolerance":
            cell["adjudication_status"] = (
                "part_b_ambiguous_tolerance"
                if ambiguous_tolerance_policy == "part_b"
                else "pending_ruling_ambiguous_tolerance")
        else:
            cell["adjudication_status"] = f"part_b_{status}"
    (out.get("judge_report") or {}).setdefault("tiebreaker_units", []).append({
        "model": TIEBREAKER_MODEL,
        "unit_key": group["unit_key"],
        "route": group["route"],
        "scores": deepcopy(third_scores) if third_scores is not None else None,
    })
    return out


def _unit_key(unit: dict):
    return unit.get("label", unit.get("index"))


def build_adjudicated_verdict(rec: dict) -> dict:
    """Materialize one derived verdict while retaining both frozen pair verdicts."""
    report = rec.get("judge_report") or {}
    verdicts = report.get("verdicts") or []
    if len(verdicts) < 2:
        raise ValueError(f"{rec.get('item_id')}: need the two frozen-pair verdicts")
    spec = spec_for(rec["design"])
    v0, v1 = verdicts[:2]
    disagreements = {str(c.get("cell")): c for c in report.get("disagreements") or []}

    def merged(scores0: dict, scores1: dict, prefix=None):
        scores = {}
        for category in spec.categories:
            cell_name = f"{prefix}:{category.name}" if prefix is not None else category.name
            disagreement = disagreements.get(cell_name)
            if disagreement and disagreement.get("adjudication_status") == "tiebreak_resolved":
                scores[category.name] = disagreement.get("adjudicated")
                continue
            value, status = adjudicated_value(
                category, (scores0 or {}).get(category.name), (scores1 or {}).get(category.name))
            scores[category.name] = value if status == AGREED else None
        return scores

    derived = {"judge": "derived:pair-plus-tiebreak", "family": "derived",
               "unit": spec.unit, "scores": {}, "per_unit": [], "refused": False}
    if spec.unit == "item":
        derived["scores"] = merged(v0.get("scores") or {}, v1.get("scores") or {})
        return derived

    by_key1 = {_unit_key(u): u for u in v1.get("per_unit") or []}
    for unit0 in v0.get("per_unit") or []:
        key = _unit_key(unit0)
        unit1 = by_key1.get(key, {})
        unit = {k: deepcopy(v) for k, v in unit0.items() if k != "scores"}
        unit["scores"] = merged(unit0.get("scores") or {}, unit1.get("scores") or {}, key)
        derived["per_unit"].append(unit)
    return derived


def _event_key(item_id, model, unit_key) -> tuple:
    return str(item_id), str(model), str(unit_key)


def _read_events(path: Path) -> dict:
    events = {}
    if not path.exists():
        return events
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except (json.JSONDecodeError, TypeError):
            continue
        key = _event_key(event.get("item_id"), event.get("model"), event.get("unit_key"))
        events[key] = event
    return events


def _cost_delta(before, after) -> dict:
    before = before or {}
    after = after or {}
    return {
        "usd": round(float(after.get("cost", 0)) - float(before.get("cost", 0)), 8),
        "calls": int(after.get("calls", 0)) - int(before.get("calls", 0)),
        "prompt_tokens": (int(after.get("prompt_tokens", 0))
                          - int(before.get("prompt_tokens", 0))),
        "completion_tokens": (int(after.get("completion_tokens", 0))
                              - int(before.get("completion_tokens", 0))),
    }


def run_tiebreak(records: list, items_by_id: dict, client, checkpoint_path,
                 cost_probe=None, max_new_tiebreak_units=None,
                 ambiguous_tolerance_policy: str = "stop") -> tuple:
    """Run/resume W1 unit calls and return derived records plus mechanical counts."""
    checkpoint = Path(checkpoint_path)
    checkpoint.parent.mkdir(parents=True, exist_ok=True)
    events = _read_events(checkpoint)
    groups = group_disagreements(records)
    out = deepcopy(records)
    counts = {"groups": len(groups), "cells": sum(len(g["cells"]) for g in groups),
              "tie_breaker_units": 0, "own_family_units": 0,
              "checkpointed_units": 0, "new_units": 0, "defects": 0,
              "contested_cells": 0, "ambiguous_tolerance_cells": 0,
              "processed_groups": 0, "complete": False}

    with checkpoint.open("a", encoding="utf-8") as fh:
        for group in groups:
            key = _event_key(group["item_id"], group["model"], group["unit_key"])
            event = events.get(key)
            if group["route"] == "part_b_own_family":
                counts["own_family_units"] += 1
            else:
                counts["tie_breaker_units"] += 1
            if event is not None:
                counts["checkpointed_units"] += 1
            else:
                if (group["route"] == "tie_breaker"
                        and max_new_tiebreak_units is not None
                        and counts["new_units"] >= max_new_tiebreak_units):
                    break
                scores = defects = None
                before = cost_probe() if cost_probe else None
                if group["route"] == "tie_breaker":
                    item = items_by_id[group["item_id"]]
                    prompt = rubric_prompt_for_unit(
                        item, out[group["record_index"]], group["cells"][0]["cell"])
                    response = client.complete([Message("user", prompt)], system=JUDGE_SYSTEM)
                    scores, defects = parse_verdict(response.text, spec_for(group["design"]))
                    counts["defects"] += len(defects)
                after = cost_probe() if cost_probe else None
                event = {"item_id": group["item_id"], "design": group["design"],
                         "model": group["model"], "unit_key": group["unit_key"],
                         "route": group["route"], "tiebreaker_model": TIEBREAKER_MODEL,
                         "scores": scores, "defects": defects or [],
                         "cost": _cost_delta(before, after)}
                fh.write(json.dumps(event, ensure_ascii=False) + "\n")
                fh.flush()
                events[key] = event
                counts["new_units"] += 1
            idx = group["record_index"]
            out[idx] = apply_group_result(
                out[idx], group, event.get("scores"),
                ambiguous_tolerance_policy=ambiguous_tolerance_policy)
            counts["processed_groups"] += 1

    for rec in out:
        rec.setdefault("judge_report", {})["adjudicated_verdict"] = \
            build_adjudicated_verdict(rec)
        for cell in (rec["judge_report"].get("disagreements") or []):
            status = cell.get("adjudication_status", "")
            if status.startswith("part_b_"):
                counts["contested_cells"] += 1
            elif status == "pending_ruling_ambiguous_tolerance":
                counts["ambiguous_tolerance_cells"] += 1
    counts["complete"] = counts["processed_groups"] == len(groups)
    used_keys = {_event_key(g["item_id"], g["model"], g["unit_key"])
                 for g in groups[:counts["processed_groups"]]}
    used_events = [events[k] for k in used_keys if k in events]
    counts["cost"] = {
        "usd": round(sum(float((e.get("cost") or {}).get("usd", 0)) for e in used_events), 8),
        "calls": sum(int((e.get("cost") or {}).get("calls", 0)) for e in used_events),
        "prompt_tokens": sum(int((e.get("cost") or {}).get("prompt_tokens", 0))
                             for e in used_events),
        "completion_tokens": sum(int((e.get("cost") or {}).get("completion_tokens", 0))
                                 for e in used_events),
    }
    return out, counts


def _read_jsonl(path: Path) -> list:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def main(argv=None):
    ap = argparse.ArgumentParser(description="WALKWORTHY W1 full-surface tie-breaker")
    ap.add_argument("--benchmark-root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--base-run", required=True)
    ap.add_argument("--reexecution-run", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--date", default=None)
    ap.add_argument("--tiebreaker-model", required=True)
    ap.add_argument("--max-new-tiebreak-units", type=int, default=None,
                    help="bounded reliability probe; omit for the full resumable W1 run")
    ap.add_argument("--ambiguous-tolerance-policy", choices=("stop", "part_b"),
                    default="stop",
                    help="PR-15 disposition; part_b requires Jimmy's ratified option 1")
    args = ap.parse_args(argv)
    if args.tiebreaker_model != TIEBREAKER_MODEL:
        raise SystemExit(f"W1 model must be explicit frozen slug: {TIEBREAKER_MODEL}")

    from . import openrouter_backend as orb
    from .loader import load_public_split
    from .reparse05 import reparse_records
    from .smoke import _cost_tracking_transport

    root = Path(args.benchmark_root)
    base = _read_jsonl(root / "runs" / args.base_run / "scored_items.jsonl")
    reexecuted = _read_jsonl(root / "runs" / args.reexecution_run / "scored_items.jsonl")
    transcript = validate_transcript_contract(reexecuted)
    merged = merge_reexecution(base, reexecuted)
    items = {item.id: item for item in load_public_split(
        str(root), include_exemplars=True, runnable_only=True)}
    merged, reparse_summary = reparse_records(merged, items)

    key = orb.load_openrouter_key()
    if not key:
        raise SystemExit("W1: no OpenRouter key")
    transport = _cost_tracking_transport()
    client = orb.OpenRouterClient(TIEBREAKER_MODEL, model=TIEBREAKER_MODEL,
                                  api_key=key, transport=transport)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    derived, summary = run_tiebreak(
        merged, items, client, out_dir / "tiebreak_events.jsonl",
        cost_probe=lambda: dict(transport.acc),
        max_new_tiebreak_units=args.max_new_tiebreak_units,
        ambiguous_tolerance_policy=args.ambiguous_tolerance_policy)
    summary.update({"date": args.date or f"{date.today():%Y%m%d}",
                    "base_run": args.base_run,
                    "reexecution_run": args.reexecution_run,
                    "tiebreaker_model": TIEBREAKER_MODEL,
                    "ambiguous_tolerance_policy": args.ambiguous_tolerance_policy,
                    "transcript_contract": transcript,
                    "reparse05": reparse_summary})
    with (out_dir / "scored_items.jsonl").open("w", encoding="utf-8") as fh:
        for rec in derived:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    (out_dir / "tiebreak_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if summary["ambiguous_tolerance_cells"]:
        raise SystemExit("W1 STOP: append numeric-tolerance ambiguity to PENDING-RULINGS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
