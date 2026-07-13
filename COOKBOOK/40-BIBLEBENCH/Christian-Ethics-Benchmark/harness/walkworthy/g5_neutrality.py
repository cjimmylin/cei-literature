"""Frozen W4 G5 blind reference-neutrality runner for designs 06 and 09."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

from .clients import Message
from .g5_reference_lint import lint_reference_files, parse_reference_pairs
from .live_judges import JUDGE_SYSTEM, parse_verdict
from .rubrics import g5_spec_for

G5_DESIGNS = ("06-crookedpath", "09-doubleedge")
G5_JUDGE_MODELS = ("openai/gpt-4.1-mini", "google/gemini-2.5-flash")
G5_SYSTEM = JUDGE_SYSTEM
G5_SYSTEM_SHA256 = hashlib.sha256(G5_SYSTEM.encode("utf-8")).hexdigest()


class G5Stop(RuntimeError):
    """Terminal frozen-protocol stop requiring owner escalation."""


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _json_sha256(value: dict) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_promoted_pairs(benchmark_root) -> dict:
    root = Path(benchmark_root)
    config_dir = root / "harness" / "config" / "g5"
    manifest_path = config_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if tuple(manifest.get("designs", {})) != G5_DESIGNS:
        raise ValueError("G5 manifest must contain exactly the registered 06/09 designs")
    pairs = {}
    reference_hashes = {}
    reference_paths = {}
    for design in G5_DESIGNS:
        entry = manifest["designs"][design]
        path = config_dir / entry["path"]
        actual = _sha256(path)
        if actual != entry.get("promoted_sha256"):
            raise ValueError(f"G5 promoted config hash mismatch: {design}")
        reference_hashes[design] = actual
        reference_paths[design] = path
        pairs[design] = parse_reference_pairs(path, design)
    lint = lint_reference_files(
        reference_paths["06-crookedpath"], reference_paths["09-doubleedge"],
        root / "DESIGNS" / "09-doubleedge-seeds.md")
    if lint["failures"]:
        raise ValueError("G5 reference lint failed")
    return {
        "version": manifest["version"],
        "manifest_sha256": _sha256(manifest_path),
        "reference_hashes": reference_hashes,
        "lint": lint,
        "pairs": pairs,
    }


def validate_judge_models(models) -> tuple:
    """Accept the frozen pair in either CLI order and return canonical order."""
    supplied = tuple(models)
    if len(supplied) != 2 or len(set(supplied)) != 2 \
            or set(supplied) != set(G5_JUDGE_MODELS):
        raise ValueError(
            f"G5 requires the frozen G5 judge pair {G5_JUDGE_MODELS!r}; "
            f"received {supplied!r}")
    return G5_JUDGE_MODELS


def _run_manifest(loaded: dict) -> dict:
    item_ids = {design: [pair["item_id"] for pair in loaded["pairs"][design]]
                for design in G5_DESIGNS}
    categories = {design: [category.name for category in g5_spec_for(design).categories]
                  for design in G5_DESIGNS}
    return {
        "kind": "o5-w4-g5-reference-neutrality",
        "protocol_version": loaded["version"],
        "source_manifest_sha256": loaded["manifest_sha256"],
        "reference_hashes": loaded["reference_hashes"],
        "judge_models": list(G5_JUDGE_MODELS),
        "judge_families": [model.split("/", 1)[0] for model in G5_JUDGE_MODELS],
        "system_sha256": G5_SYSTEM_SHA256,
        "designs": list(G5_DESIGNS),
        "item_ids": item_ids,
        "categories": categories,
        "selected_pairs": sum(len(ids) for ids in item_ids.values()),
        "initial_reference_scores": sum(len(ids) * 2 * len(G5_JUDGE_MODELS)
                                        for ids in item_ids.values()),
        "category_cell_comparisons": sum(
            len(item_ids[design]) * len(G5_JUDGE_MODELS) * len(categories[design])
            for design in G5_DESIGNS),
        "violation_threshold": {"operator": ">", "value": 0.5},
        "reelicitation": "exactly one fresh two-pole attempt per initial violation",
        "schedule": "design,pair,pole,judge; all initial calls before re-elicitation",
    }


def _write_or_validate_manifest(path: Path, manifest: dict) -> str:
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError("G5 run manifest is invalid JSON") from exc
        if existing != manifest:
            raise ValueError("G5 run manifest mismatch")
    else:
        path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return _json_sha256(manifest)


def build_blind_prompt(pair: dict, pole: int, spec) -> str:
    """Build a single-pole prompt with no opposite answer or pole label."""
    if pole not in (0, 1):
        raise ValueError(f"G5 pole must be 0 or 1, not {pole!r}")
    categories = "\n".join(
        f"- {category.name}: {category.desc} Allowed values: "
        f"{json.dumps(category.options)}"
        for category in spec.categories)
    return (
        "Blindly score the quality of the candidate answer against the case context.\n"
        "Evaluate the reasoning and execution only: do not reward or penalize the "
        "conclusion, and do not guess which side of a matched pair this is.\n\n"
        f"Item: {pair['item_id']}\n"
        f"Case context:\n{pair['context']}\n\n"
        f"Candidate answer:\n{pair['poles'][pole]}\n\n"
        "Score every category independently:\n"
        f"{categories}\n\n"
        "Return exactly one JSON object whose keys are the category names and whose "
        "values are allowed numeric scores."
    )


def violates_neutrality(left: dict, right: dict) -> bool:
    """The frozen boundary is strict: exactly 0.5 passes; greater than 0.5 fails."""
    if set(left) != set(right):
        raise ValueError("G5 score keys differ across poles")
    return any(abs(float(left[name]) - float(right[name])) > 0.5 for name in left)


def _event_key(event: dict) -> tuple:
    return (event.get("design"), event.get("item_id"), event.get("pole"),
            event.get("judge_model"), event.get("attempt"))


def _expected_key(design: str, pair: dict, pole: int, judge: str,
                  attempt: int) -> tuple:
    return design, pair["item_id"], pole, judge, attempt


def _parse_scores(text: str, spec) -> dict:
    scores, defects = parse_verdict(text, spec)
    if defects:
        raise ValueError("G5 parse defect: " + json.dumps(defects, sort_keys=True))
    return scores


def _usage(response) -> dict:
    usage = response.usage if isinstance(response.usage, dict) else {}
    return {
        "usd": float(usage.get("cost", usage.get("usd", 0)) or 0),
        "calls": 1,
        "prompt_tokens": int(usage.get("prompt_tokens", 0) or 0),
        "completion_tokens": int(usage.get("completion_tokens", 0) or 0),
    }


def _valid_cost(cost: object) -> bool:
    if not isinstance(cost, dict) or set(cost) != {
            "usd", "calls", "prompt_tokens", "completion_tokens"}:
        return False
    values = (cost.get("usd"), cost.get("prompt_tokens"), cost.get("completion_tokens"))
    return cost.get("calls") == 1 and all(
        isinstance(value, (int, float)) and not isinstance(value, bool)
        and math.isfinite(float(value)) and float(value) >= 0 for value in values)


def _read_events(path: Path) -> list:
    if not path.exists():
        return []
    events = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"G5 checkpoint provenance invalid at line {line_no}") from exc
        events.append(event)
    keys = [_event_key(event) for event in events]
    if len(keys) != len(set(keys)):
        raise ValueError("G5 checkpoint contains a duplicate event key")
    return events


def _read_error_events(path: Path) -> list:
    if not path.exists():
        return []
    events = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"G5 error checkpoint provenance invalid at line {line_no}") from exc
    keys = [_error_key(event) for event in events]
    if len(keys) != len(set(keys)):
        raise ValueError("G5 error checkpoint contains a duplicate event key")
    return events


def _expected_prompt(pair: dict, pole: int, design: str) -> tuple:
    spec = g5_spec_for(design)
    prompt = build_blind_prompt(pair, pole, spec)
    return prompt, hashlib.sha256(prompt.encode("utf-8")).hexdigest(), spec


_EVENT_FIELDS = {
    "design", "item_id", "pole", "judge_model", "requested_family", "attempt",
    "prompt_sha256", "system_sha256", "protocol_version", "manifest_sha256",
    "run_manifest_sha256", "reference_sha256", "response_model", "response_family",
    "response_sha256", "scores", "defects", "cost",
}


def _validate_event(event: dict, loaded: dict, pair_by_item: dict,
                    run_manifest_sha256: str) -> None:
    design = event.get("design")
    item_id = event.get("item_id")
    pole = event.get("pole")
    judge = event.get("judge_model")
    attempt = event.get("attempt")
    pair = pair_by_item.get((design, item_id))
    mismatches = []
    if set(event) != _EVENT_FIELDS:
        mismatches.append("event fields")
    if pair is None or pole not in (0, 1) or judge not in G5_JUDGE_MODELS \
            or attempt not in (1, 2):
        mismatches.append("unregistered event identity")
    else:
        _, prompt_hash, spec = _expected_prompt(pair, pole, design)
        if event.get("prompt_sha256") != prompt_hash:
            mismatches.append("prompt hash")
        if event.get("manifest_sha256") != loaded["manifest_sha256"]:
            mismatches.append("manifest hash")
        if event.get("run_manifest_sha256") != run_manifest_sha256:
            mismatches.append("run manifest hash")
        if event.get("reference_sha256") != loaded["reference_hashes"][design]:
            mismatches.append("reference hash")
        expected_family = judge.split("/", 1)[0]
        if event.get("requested_family") != expected_family:
            mismatches.append("requested family")
        if event.get("system_sha256") != G5_SYSTEM_SHA256:
            mismatches.append("system hash")
        if event.get("protocol_version") != loaded["version"]:
            mismatches.append("protocol version")
        response_model = event.get("response_model")
        if response_model != judge:
            mismatches.append("response model")
        if event.get("response_family") != expected_family:
            mismatches.append("response family")
        if not isinstance(event.get("response_sha256"), str) \
                or len(event.get("response_sha256")) != 64:
            mismatches.append("response hash")
        try:
            _parse_scores(json.dumps(event.get("scores")), spec)
        except ValueError:
            mismatches.append("scores")
    if event.get("defects") != []:
        mismatches.append("defects")
    if not _valid_cost(event.get("cost")):
        mismatches.append("cost")
    if mismatches:
        raise ValueError("G5 checkpoint provenance mismatch: " + ", ".join(mismatches))


def _error_key(event: dict) -> tuple:
    return _event_key(event), event.get("failure_index")


def _validate_error_event(event: dict, loaded: dict, pair_by_item: dict,
                          run_manifest_sha256: str) -> None:
    required = (_EVENT_FIELDS - {"scores"}) | {"failure_index", "raw_response_sha256"}
    mismatches = []
    if set(event) != required:
        mismatches.append("error fields")
    design, item_id, pole = event.get("design"), event.get("item_id"), event.get("pole")
    judge, attempt = event.get("judge_model"), event.get("attempt")
    pair = pair_by_item.get((design, item_id))
    if pair is None or pole not in (0, 1) or judge not in G5_JUDGE_MODELS \
            or attempt not in (1, 2):
        mismatches.append("identity provenance")
    else:
        _, prompt_hash, _ = _expected_prompt(pair, pole, design)
        expected_family = judge.split("/", 1)[0]
        checks = (
            (event.get("prompt_sha256") == prompt_hash, "prompt hash"),
            (event.get("system_sha256") == G5_SYSTEM_SHA256, "system hash"),
            (event.get("protocol_version") == loaded["version"], "protocol version"),
            (event.get("manifest_sha256") == loaded["manifest_sha256"], "manifest hash"),
            (event.get("run_manifest_sha256") == run_manifest_sha256,
             "run manifest hash"),
            (event.get("reference_sha256") == loaded["reference_hashes"][design],
             "reference hash"),
            (event.get("requested_family") == expected_family, "requested family"),
        )
        mismatches.extend(label for ok, label in checks if not ok)
        reasons = {defect.get("reason") for defect in (event.get("defects") or [])
                   if isinstance(defect, dict)}
        if event.get("response_model") != judge \
                and "returned_model_mismatch" not in reasons:
            mismatches.append("unrecorded response model mismatch")
        if event.get("response_family") != expected_family \
                and "returned_family_mismatch" not in reasons:
            mismatches.append("unrecorded response family mismatch")
    if not isinstance(event.get("failure_index"), int) or event.get("failure_index") < 1:
        mismatches.append("failure index")
    if not isinstance(event.get("raw_response_sha256"), str) \
            or len(event.get("raw_response_sha256")) != 64:
        mismatches.append("raw response hash")
    if not isinstance(event.get("defects"), list) or not event.get("defects"):
        mismatches.append("defects")
    if event.get("response_sha256") != event.get("raw_response_sha256"):
        mismatches.append("response hash")
    if not _valid_cost(event.get("cost")):
        mismatches.append("cost")
    if mismatches:
        raise ValueError("G5 error checkpoint provenance mismatch: " + ", ".join(mismatches))


def _index(events: list) -> dict:
    return {_event_key(event): event for event in events}


def _initial_plan(loaded: dict) -> list:
    return [_expected_key(design, pair, pole, judge, 1)
            for design in G5_DESIGNS
            for pair in loaded["pairs"][design]
            for pole in (0, 1)
            for judge in G5_JUDGE_MODELS]


def _retry_plan_for_loaded(loaded: dict, initial: list) -> list:
    initial_set = {(design, pair["item_id"], judge)
                   for design, pair, judge in initial}
    return [_expected_key(design, pair, pole, judge, 2)
            for design in G5_DESIGNS
            for pair in loaded["pairs"][design]
            for pole in (0, 1)
            for judge in G5_JUDGE_MODELS
            if (design, pair["item_id"], judge) in initial_set]


def _validate_ledger_order(events: list, error_events: list, loaded: dict) -> list:
    initial_plan = _initial_plan(loaded)
    keys = [_event_key(event) for event in events]
    initial_count = sum(key[-1] == 1 for key in keys)
    if initial_count < len(initial_plan):
        expected = initial_plan
        initial = []
    else:
        indexed = _index(events)
        initial = _initial_violations(loaded, indexed)
        expected = initial_plan + _retry_plan_for_loaded(loaded, initial)
    if keys != expected[:len(keys)]:
        raise ValueError("G5 checkpoint event order is not a deterministic plan prefix")

    failures_by_key = {}
    for event in error_events:
        failures_by_key.setdefault(_event_key(event), []).append(event["failure_index"])
    for indices in failures_by_key.values():
        if indices != list(range(1, len(indices) + 1)):
            raise ValueError("G5 error checkpoint failure index is not contiguous")
    plan_index = {key: index for index, key in enumerate(expected)}
    positions = []
    for event in error_events:
        key = _event_key(event)
        if key not in plan_index:
            raise ValueError("G5 error checkpoint event order references an unscheduled call")
        positions.append(plan_index[key])
    if positions != sorted(positions):
        raise ValueError("G5 error checkpoint event order is not monotonic")
    return initial


def _derived_completion(loaded: dict, events: list, initial: list) -> tuple:
    expected_count = len(_initial_plan(loaded))
    if len(events) < expected_count:
        return False, None
    expected_count += len(_retry_plan_for_loaded(loaded, initial))
    complete = len(events) == expected_count
    if not complete:
        return False, None
    persistent = _persistent_violations(initial, _index(events))
    both = _both_disqualified(_disqualified(persistent))
    stop_trigger = f"both_judges_disqualified:{both}" if both else None
    return True, stop_trigger


def _initial_violations(loaded: dict, indexed: dict) -> list:
    violations = []
    for design in G5_DESIGNS:
        for pair in loaded["pairs"][design]:
            for judge in G5_JUDGE_MODELS:
                left = indexed[_expected_key(design, pair, 0, judge, 1)]["scores"]
                right = indexed[_expected_key(design, pair, 1, judge, 1)]["scores"]
                if violates_neutrality(left, right):
                    violations.append((design, pair, judge))
    return violations


def _violation_rows(groups: list, indexed: dict, attempt: int) -> list:
    rows = []
    for design, pair, judge in groups:
        left = indexed.get(_expected_key(design, pair, 0, judge, attempt))
        right = indexed.get(_expected_key(design, pair, 1, judge, attempt))
        if left is None or right is None:
            continue
        categories = [name for name in left["scores"]
                      if abs(float(left["scores"][name])
                             - float(right["scores"][name])) > 0.5]
        if categories:
            rows.append({"design": design, "item_id": pair["item_id"],
                         "judge_model": judge, "categories": categories})
    return rows


def _persistent_violations(initial: list, indexed: dict) -> list:
    return _violation_rows(initial, indexed, 2)


def _disqualified(persistent: list) -> list:
    found = {(row["design"], row["judge_model"]) for row in persistent}
    return [{"design": design, "judge_model": judge}
            for design in G5_DESIGNS for judge in G5_JUDGE_MODELS
            if (design, judge) in found]


def _both_disqualified(disqualified: list) -> str | None:
    found = {(row["design"], row["judge_model"]) for row in disqualified}
    for design in G5_DESIGNS:
        if all((design, judge) in found for judge in G5_JUDGE_MODELS):
            return design
    return None


def _summary(loaded: dict, events: list, error_events: list, initial: list, complete: bool,
             stop_trigger: str | None = None) -> dict:
    indexed = _index(events)
    initial_rows = _violation_rows(initial, indexed, 1)
    persistent = _persistent_violations(initial, indexed)
    disqualified = _disqualified(persistent)
    disqualified_set = {(row["design"], row["judge_model"])
                        for row in disqualified}
    costs = [event["cost"] for event in events + error_events]
    manifest = _run_manifest(loaded)
    return {
        "protocol_version": loaded["version"],
        "manifest_sha256": loaded["manifest_sha256"],
        "reference_hashes": loaded["reference_hashes"],
        "judge_models": list(G5_JUDGE_MODELS),
        "selected_pairs": manifest["selected_pairs"],
        "initial_reference_scores": manifest["initial_reference_scores"],
        "category_cell_comparisons": manifest["category_cell_comparisons"],
        "initial_calls": sum(event["attempt"] == 1 for event in events),
        "initial_violations": len(initial),
        "initial_violation_rows": initial_rows,
        "reelicitation_calls": sum(event["attempt"] == 2 for event in events),
        "violations": persistent,
        "persistent_violation_rows": persistent,
        "disqualified": disqualified,
        "judge_statuses": [
            {"design": design, "judge_model": judge,
             "status": ("PENDING" if not complete else
                        ("DISQUALIFIED" if (design, judge) in disqualified_set else "PASS"))}
            for design in G5_DESIGNS for judge in G5_JUDGE_MODELS],
        "lint": {
            "status": "PASS",
            "pair_counts": {design: len(loaded["pairs"][design]) for design in G5_DESIGNS},
            "failure_count": len(loaded["lint"]["failures"]),
            "directed": loaded["lint"]["directed"],
        },
        "error_calls": len(error_events),
        "complete": complete,
        "stop_trigger": stop_trigger,
        "cost": {
            "usd": round(sum(float(cost["usd"]) for cost in costs), 8),
            "calls": sum(int(cost["calls"]) for cost in costs),
            "prompt_tokens": sum(int(cost["prompt_tokens"]) for cost in costs),
            "completion_tokens": sum(int(cost["completion_tokens"]) for cost in costs),
        },
    }


def _write_summary(path: Path, summary: dict) -> None:
    path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


def run_g5(benchmark_root, out, clients: dict, max_new_calls: int | None = None) -> dict:
    """Run/resume the frozen blind G5 protocol with append-only event custody."""
    validate_judge_models(tuple(clients))
    if max_new_calls is not None and max_new_calls < 0:
        raise ValueError("max_new_calls must be non-negative")
    out_dir = Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)
    events_path = out_dir / "g5_events.jsonl"
    error_events_path = out_dir / "g5_error_events.jsonl"
    run_manifest_path = out_dir / "g5_manifest.json"
    summary_path = out_dir / "g5_summary.json"
    prior_summary = None
    if summary_path.exists():
        try:
            prior_summary = json.loads(summary_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError("G5 summary is invalid JSON") from exc

    loaded = load_promoted_pairs(benchmark_root)
    run_manifest_sha256 = _write_or_validate_manifest(
        run_manifest_path, _run_manifest(loaded))
    pair_by_item = {(design, pair["item_id"]): pair
                    for design in G5_DESIGNS for pair in loaded["pairs"][design]}
    events = _read_events(events_path)
    error_events = _read_error_events(error_events_path)
    for event in events:
        _validate_event(event, loaded, pair_by_item, run_manifest_sha256)
    for event in error_events:
        _validate_error_event(event, loaded, pair_by_item, run_manifest_sha256)
    ordered_initial = _validate_ledger_order(events, error_events, loaded)
    if prior_summary is not None and prior_summary.get("complete") is True:
        derived_complete, derived_stop = _derived_completion(
            loaded, events, ordered_initial)
        recomputed = _summary(
            loaded, events, error_events, ordered_initial,
            derived_complete, derived_stop)
        if recomputed != prior_summary:
            raise ValueError("completed G5 summary provenance mismatch")
        raise ValueError("completed G5 run is immutable")
    indexed = _index(events)
    new_calls = 0

    def append_call(design: str, pair: dict, pole: int, judge: str,
                    attempt: int, handle, error_handle) -> None:
        nonlocal new_calls
        prompt, prompt_hash, spec = _expected_prompt(pair, pole, design)
        response = clients[judge].complete([Message("user", prompt)], system=G5_SYSTEM)
        new_calls += 1
        expected_family = judge.split("/", 1)[0]
        provenance_defects = []
        if response.model != judge:
            provenance_defects.append({
                "category": None, "reason": "returned_model_mismatch",
                "raw": str(response.model)[:200]})
        if response.family != expected_family:
            provenance_defects.append({
                "category": None, "reason": "returned_family_mismatch",
                "raw": str(response.family)[:200]})
        scores, parse_defects = parse_verdict(response.text, spec)
        defects = provenance_defects + parse_defects
        response_hash = hashlib.sha256((response.text or "").encode("utf-8")).hexdigest()
        common = {
            "design": design,
            "item_id": pair["item_id"],
            "pole": pole,
            "judge_model": judge,
            "requested_family": expected_family,
            "attempt": attempt,
            "prompt_sha256": prompt_hash,
            "system_sha256": G5_SYSTEM_SHA256,
            "protocol_version": loaded["version"],
            "manifest_sha256": loaded["manifest_sha256"],
            "run_manifest_sha256": run_manifest_sha256,
            "reference_sha256": loaded["reference_hashes"][design],
            "response_model": response.model,
            "response_family": response.family,
            "response_sha256": response_hash,
            "cost": _usage(response),
        }
        if defects:
            prior_failures = sum(_event_key(error) ==
                                 _expected_key(design, pair, pole, judge, attempt)
                                 for error in error_events)
            error_event = {
                **common,
                "failure_index": prior_failures + 1,
                "raw_response_sha256": response_hash,
                "defects": defects,
            }
            error_handle.write(json.dumps(error_event, ensure_ascii=False) + "\n")
            error_handle.flush()
            os.fsync(error_handle.fileno())
            error_events.append(error_event)
            label = "returned model provenance" if provenance_defects else "parse defect"
            raise ValueError("G5 " + label + ": " + json.dumps(defects, sort_keys=True))
        event = {**common, "scores": scores, "defects": []}
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())
        events.append(event)
        indexed[_event_key(event)] = event

    def capped() -> bool:
        return max_new_calls is not None and new_calls >= max_new_calls

    initial_plan = [(design, pair, pole, judge)
                    for design in G5_DESIGNS
                    for pair in loaded["pairs"][design]
                    for pole in (0, 1)
                    for judge in G5_JUDGE_MODELS]
    with events_path.open("a", encoding="utf-8") as handle, \
            error_events_path.open("a", encoding="utf-8") as error_handle:
        for design, pair, pole, judge in initial_plan:
            key = _expected_key(design, pair, pole, judge, 1)
            if key in indexed:
                continue
            if capped():
                summary = _summary(loaded, events, error_events, [], complete=False)
                _write_summary(summary_path, summary)
                return summary
            append_call(design, pair, pole, judge, 1, handle, error_handle)

        initial = _initial_violations(loaded, indexed)
        allowed_retry_keys = {
            _expected_key(design, pair, pole, judge, 2)
            for design, pair, judge in initial for pole in (0, 1)}
        unexpected_retries = [key for key in indexed
                              if key[-1] == 2 and key not in allowed_retry_keys]
        if unexpected_retries:
            raise ValueError("G5 checkpoint provenance includes retry without initial violation")

        retry_plan = [(design, pair, pole, judge)
                      for design in G5_DESIGNS
                      for pair in loaded["pairs"][design]
                      for pole in (0, 1)
                      for judge in G5_JUDGE_MODELS
                      if (design, pair, judge) in initial]
        for design, pair, pole, judge in retry_plan:
            key = _expected_key(design, pair, pole, judge, 2)
            if key in indexed:
                continue
            if capped():
                summary = _summary(
                    loaded, events, error_events, initial, complete=False)
                _write_summary(summary_path, summary)
                return summary
            append_call(design, pair, pole, judge, 2, handle, error_handle)

        persistent = _persistent_violations(initial, indexed)
        both = _both_disqualified(_disqualified(persistent))
        if both:
            trigger = f"both_judges_disqualified:{both}"
            summary = _summary(loaded, events, error_events, initial, True, trigger)
            _write_summary(summary_path, summary)
            raise G5Stop(f"G5 STOP: both judges disqualified on {both}")

    summary = _summary(loaded, events, error_events, initial, complete=True)
    _write_summary(summary_path, summary)
    return summary


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="WALKWORTHY frozen W4 G5 runner")
    parser.add_argument("--benchmark-root", default=str(Path(__file__).resolve().parents[2]))
    parser.add_argument("--out", required=True)
    parser.add_argument("--judge1", required=True)
    parser.add_argument("--judge2", required=True)
    parser.add_argument("--max-new-calls", type=int, default=None)
    args = parser.parse_args(argv)

    judges = validate_judge_models((args.judge1, args.judge2))
    from . import openrouter_backend as orb
    key = orb.load_openrouter_key()
    if not key:
        raise SystemExit("G5: no OpenRouter key")
    clients = {model: orb.OpenRouterClient(model, model=model, api_key=key)
               for model in judges}
    summary = run_g5(args.benchmark_root, args.out, clients,
                     max_new_calls=args.max_new_calls)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
