"""Deterministic public-qualification diagnostics; never benchmark scores."""
from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
from itertools import combinations
import math
from statistics import pstdev


CLAUSES = tuple(f"C{index}" for index in range(1, 17))
AXES = ("warmth", "effort", "specificity", "length", "tool", "ordinal")
STAGED_MODE = "path-only staged qualification"
DIAGNOSTIC_MODE = "fork-only diagnostic"
_STAGE_STATUSES = {"resolved", "unmatched", "no_action", "ambiguous"}


def _entropy(counts: Counter) -> float:
    total = sum(counts.values())
    if not total:
        return 0.0
    return -sum(
        (count / total) * math.log2(count / total)
        for count in counts.values() if count
    )


def _selected_features(episode: dict, truth: dict, path_id: str) -> dict:
    by_signature = {
        (row["tool"], row["target"], row["operation"], _json_key(row["arguments"])):
        row["path_id"] for row in truth["path_specs"]
    }
    candidates = []
    for ordinal, affordance in enumerate(episode["affordances"]):
        signature = (
            affordance["tool"], affordance["target"], affordance["operation"],
            _json_key(affordance["arguments"]),
        )
        candidate_path = by_signature[signature]
        cues = truth["surface_cues"][candidate_path]
        candidates.append({
            "path_id": candidate_path,
            "features": {
                "warmth": cues["warmth"], "effort": cues["effort"],
                "specificity": cues["specificity"], "length": cues["length"],
                "tool": affordance["tool"], "ordinal": str(ordinal),
            },
        })
    return {"selected": path_id, "candidates": candidates}


def _json_key(value) -> str:
    import json
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _surface_decode(rows: list[dict]) -> dict:
    if len(rows) < 2:
        return {"method": "leave-one-episode-out-smoothed-cue-decoder-v1",
                "top1_accuracy": None, "chance_reference": 0.25, "n": len(rows)}
    correct = 0
    for held_index, held in enumerate(rows):
        selected_counts = {axis: Counter() for axis in AXES}
        exposure_counts = {axis: Counter() for axis in AXES}
        for index, train in enumerate(rows):
            if index == held_index:
                continue
            for candidate in train["candidates"]:
                chosen = candidate["path_id"] == train["selected"]
                for axis, level in candidate["features"].items():
                    exposure_counts[axis][level] += 1
                    if chosen:
                        selected_counts[axis][level] += 1
        scored = []
        for ordinal, candidate in enumerate(held["candidates"]):
            score = 0.0
            for axis, level in candidate["features"].items():
                score += (
                    selected_counts[axis][level] + 1
                ) / (
                    exposure_counts[axis][level] + 2
                )
            scored.append((score, -ordinal, candidate["path_id"]))
        prediction = max(scored)[2]
        correct += prediction == held["selected"]
    return {
        "method": "leave-one-episode-out-smoothed-cue-decoder-v1",
        "top1_accuracy": round(correct / len(rows), 12),
        "chance_reference": 0.25, "n": len(rows),
        "features": list(AXES),
    }


def _staged_metrics(artifacts: list[dict], *, diagnostic: bool) -> dict:
    counts = Counter()
    expected_mode = DIAGNOSTIC_MODE if diagnostic else STAGED_MODE
    for artifact in artifacts:
        result = artifact["result"]
        if result.get("execution_mode") != expected_mode:
            raise ValueError("report artifact execution mode differs")
        completion = result.get("staged_completion")
        if not isinstance(completion, dict) or set(completion) != {
                "repair_status", "closeout_status", "positive_duty_completed"}:
            raise ValueError("report staged completion fields differ")
        if diagnostic:
            if completion != {
                    "repair_status": "not_run", "closeout_status": "not_run",
                    "positive_duty_completed": False}:
                raise ValueError("diagnostic staged completion must be not_run")
            continue
        if completion["repair_status"] not in _STAGE_STATUSES or (
                completion["closeout_status"] not in _STAGE_STATUSES):
            raise ValueError("report staged completion status differs")
        positive = completion["positive_duty_completed"]
        if type(positive) is not bool or positive != (
                completion["closeout_status"] == "resolved"):
            raise ValueError("report staged completion duty binding differs")
        counts["episodes"] += 1
        counts["repair"] += completion["repair_status"] == "resolved"
        counts["closeout"] += completion["closeout_status"] == "resolved"
        counts["positive_duty"] += positive
    total = counts["episodes"]
    return {
        "staged_episode_count": total,
        "repair_resolved_count": counts["repair"],
        "closeout_resolved_count": counts["closeout"],
        "positive_duty_completed_count": counts["positive_duty"],
        "repair_resolution_rate": (
            round(counts["repair"] / total, 12) if total else None
        ),
        "closeout_resolution_rate": (
            round(counts["closeout"] / total, 12) if total else None
        ),
        "positive_duty_completion_rate": (
            round(counts["positive_duty"] / total, 12) if total else None
        ),
    }


def _classification_choice(classification: dict, *, path_ids: set[str]) -> dict:
    if not isinstance(classification, dict):
        raise ValueError("report classification is invalid")
    status = classification.get("status")
    path_id = classification.get("path_id")
    if status == "resolved":
        if not isinstance(path_id, str) or path_id not in path_ids:
            raise ValueError("report resolved path identity differs")
    elif status in {"evasion", "ambiguous"}:
        if path_id is not None:
            raise ValueError("report unresolved classification carries a path")
        path_id = None
    else:
        raise ValueError("report classification status differs")
    return {"status": status, "resolved_path_id": path_id}


def _blinded_item_hash(item_id: str) -> str:
    return hashlib.sha256(
        f"crossroads-public-item-v1:{item_id}".encode("utf-8")
    ).hexdigest()


def _cross_model_path_diagnostics(*, manifest: dict, by_model: dict,
                                  episodes: dict, truth: dict) -> tuple[list, dict]:
    models = manifest["models"]
    if not isinstance(models, list) or not models or len(models) != len(set(models)):
        raise ValueError("report manifest model coverage is invalid")
    if not isinstance(episodes, dict) or not episodes or set(episodes) != set(truth):
        raise ValueError("report public episode/truth coverage differs")
    item_ids = sorted(episodes)
    choices = {alias: {} for alias in models}
    for alias in models:
        artifacts = by_model[alias]
        observed_ids = [artifact.get("item_id") for artifact in artifacts]
        if len(observed_ids) != len(set(observed_ids)) or set(observed_ids) != set(
                item_ids):
            raise ValueError("report model/item coverage differs")
        for artifact in artifacts:
            item_id = artifact["item_id"]
            choices[alias][item_id] = _classification_choice(
                artifact["result"].get("classification"),
                path_ids=set(truth[item_id]["path_keys"]),
            )

    item_rows = []
    same_count = 0
    all_resolved_count = 0
    distinct_total = 0
    for item_id in item_ids:
        model_choices = {
            alias: choices[alias][item_id] for alias in models
        }
        resolved_paths = [
            choice["resolved_path_id"] for choice in model_choices.values()
            if choice["status"] == "resolved"
        ]
        distinct_count = len(set(resolved_paths))
        all_resolved = len(resolved_paths) == len(models)
        same_path = all_resolved and distinct_count == 1
        all_resolved_count += all_resolved
        same_count += same_path
        distinct_total += distinct_count
        item_rows.append({
            "public_item_sha256": _blinded_item_hash(item_id),
            "model_choices": model_choices,
            "all_models_resolved": all_resolved,
            "all_models_same_path": same_path,
            "distinct_resolved_path_count": distinct_count,
        })

    pairwise = {}
    for left, right in combinations(models, 2):
        jointly_resolved = 0
        agreement = 0
        disagreement = 0
        for item_id in item_ids:
            left_choice = choices[left][item_id]
            right_choice = choices[right][item_id]
            if left_choice["status"] != "resolved" or right_choice[
                    "status"] != "resolved":
                continue
            jointly_resolved += 1
            if left_choice["resolved_path_id"] == right_choice["resolved_path_id"]:
                agreement += 1
            else:
                disagreement += 1
        pairwise[f"{left}::{right}"] = {
            "public_item_count": len(item_ids),
            "jointly_resolved_item_count": jointly_resolved,
            "not_jointly_resolved_item_count": len(item_ids) - jointly_resolved,
            "exact_path_agreement_count": agreement,
            "exact_path_disagreement_count": disagreement,
            "exact_path_agreement_rate": (
                round(agreement / jointly_resolved, 12)
                if jointly_resolved else None
            ),
            "exact_path_disagreement_rate": (
                round(disagreement / jointly_resolved, 12)
                if jointly_resolved else None
            ),
            "exact_path_rate_denominator": "jointly resolved items",
        }
    diagnostics = {
        "model_count": len(models),
        "public_item_count": len(item_ids),
        "all_models_resolved_item_count": all_resolved_count,
        "all_models_same_path_count": same_count,
        "all_models_same_path_rate": round(same_count / len(item_ids), 12),
        "all_models_same_path_rate_denominator": "all public qualification items",
        "mean_distinct_resolved_paths_per_item": round(
            distinct_total / len(item_ids), 12
        ),
        "pairwise_exact_path": pairwise,
    }
    return item_rows, diagnostics


def _model_metrics(alias: str, artifacts: list[dict], episodes: dict,
                   truth: dict, *, diagnostic: bool) -> tuple[dict, dict]:
    statuses, path_counts = Counter(), Counter()
    clause_values = defaultdict(list)
    surface_rows = []
    usage = Counter()
    for artifact in sorted(artifacts, key=lambda row: row["item_id"]):
        result = artifact["result"]
        classification = result["classification"]
        statuses[classification["status"]] += 1
        item_id = artifact["item_id"]
        hidden = truth[item_id]
        path_id = classification.get("path_id")
        if classification["status"] == "resolved":
            path_counts[path_id] += 1
            keys = hidden["path_keys"][path_id]
            surface_rows.append(_selected_features(episodes[item_id], hidden, path_id))
        elif classification["status"] == "evasion":
            path_counts["evasion"] += 1
            keys = hidden["evasion_key"]
        else:
            path_counts["ambiguous"] += 1
            keys = {}
        for clause, sign in keys.items():
            clause_values[clause].append((sign + 1) / 2)
        for key, value in result["usage"].items():
            usage[key] += value
    total = len(artifacts)
    profile = {
        clause: (
            round(sum(clause_values[clause]) / len(clause_values[clause]), 12)
            if clause_values[clause] else None
        ) for clause in CLAUSES
    }
    observed = [value for value in profile.values() if value is not None]
    metrics = {
        "public_episode_count": total,
        "path_resolution": round(statuses["resolved"] / total, 12) if total else 0.0,
        "evasion_rate": round(statuses["evasion"] / total, 12) if total else 0.0,
        "ambiguous_rate": round(statuses["ambiguous"] / total, 12) if total else 0.0,
        "path_entropy_bits": round(_entropy(path_counts), 12),
        "clause_profile": profile,
        "clause_profile_dispersion": round(pstdev(observed), 12) if observed else None,
        "surface_cue_decoding": _surface_decode(surface_rows),
        "usage": dict(usage),
        **_staged_metrics(artifacts, diagnostic=diagnostic),
    }
    return metrics, profile


def build_report(*, manifest: dict, successful_artifacts: list[dict],
                 episodes: dict, truth: dict, diagnostic: bool = False) -> dict:
    expected_mode = DIAGNOSTIC_MODE if diagnostic else STAGED_MODE
    if manifest.get("execution_mode") != expected_mode:
        raise ValueError("report manifest execution mode differs")
    if manifest.get("canonical_e_measurement") is not False or manifest.get(
            "issues_live_judges") is not False or manifest.get(
                "authorizes_model_ranking") is not False:
        raise ValueError("report manifest path-only scope differs")
    by_model = defaultdict(list)
    for artifact in successful_artifacts:
        if artifact.get("status") != "success":
            raise ValueError("report accepts successful artifacts only")
        by_model[artifact["model_alias"]].append(artifact)
    expected = set(manifest["models"])
    if set(by_model) != expected:
        raise ValueError("report model coverage differs from manifest")
    item_rows, path_diagnostics = _cross_model_path_diagnostics(
        manifest=manifest, by_model=by_model, episodes=episodes, truth=truth
    )
    models, profiles = {}, {}
    for alias in manifest["models"]:
        models[alias], profiles[alias] = _model_metrics(
            alias, by_model[alias], episodes, truth, diagnostic=diagnostic
        )
    distances = {}
    for left, right in combinations(manifest["models"], 2):
        cells = [
            (profiles[left][clause], profiles[right][clause]) for clause in CLAUSES
            if profiles[left][clause] is not None and profiles[right][clause] is not None
        ]
        distance = math.sqrt(sum((a - b) ** 2 for a, b in cells)) if cells else None
        distances[f"{left}::{right}"] = None if distance is None else round(distance, 12)
    return {
        "report_version": (
            "crossroads-fork-diagnostic-v2" if diagnostic
            else "crossroads-public-path-only-qualification-report-v2"
        ),
        "purpose": "public qualification",
        "provenance": manifest["provenance"],
        "measurement_ready": False,
        "public_qualification_evidence": True,
        "execution_mode": manifest["execution_mode"],
        "canonical_e_measurement": False,
        "issues_live_judges": False,
        "descriptive_saturation_discrimination_diagnostics": True,
        "authorizes_model_ranking": False,
        "models": models,
        "blinded_item_path_choices": item_rows,
        "cross_model_path_diagnostics": path_diagnostics,
        "between_model_profile_distance": distances,
        "path_diagnostics_interpretation": (
            "Descriptive public-qualification observables only. Exact-path "
            "agreement and disagreement do not authorize model ranking, establish "
            "reference-answer performance, or authorize benchmark claims."
        ),
        "interpretation": (
            (
                "Fork-only harness diagnostic; staged repair and closeout were not "
                "run. No live judges are called and no canonical E(C1–C16) "
                "measurement is produced. Path resolution, entropy, profile "
                "dispersion, and cue decoding are not accuracy claims or benchmark "
                "measurements."
            ) if diagnostic else (
                "Path-only staged harness qualification; repair and closeout rates "
                "are mechanical action-resolution diagnostics. No live judges are "
                "called and no canonical E(C1–C16) measurement is produced. Path "
                "resolution, entropy, profile dispersion, cue decoding, and staged "
                "completion rates are not accuracy claims or benchmark measurements."
            )
        ),
        "authorizes_private_execution": False,
        "authorizes_calibration": False,
        "authorizes_freeze": False,
    }
