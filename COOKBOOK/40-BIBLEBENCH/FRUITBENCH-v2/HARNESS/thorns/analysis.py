#!/usr/bin/env python3
"""Pure preregistered saturation/discrimination analysis for live THORNS rows.

The inferential unit is always an item.  Rollouts are first reduced within an
actor/item/surface/task-arm cell and never enter an effect-size denominator as
independent observations.  The frozen JSON config defines endpoints, the
smallest effect of interest (SOEI), cue/null limits, and judge/task-validity
latches.  This module performs no I/O except reading that config.

Construct surfaces C0/C1/C3 use only ``Fi/Wj/CFT/mixed/other``.  The C2 null
surface has a deliberately disjoint outcome domain:
``foil_correct/target_action_false_positive/indeterminate``.  A missing or
no-fusion headline label in either domain remains in the evidence table and
latches the analysis invalid; it is never silently dropped.

Each terminal row must carry ``actor_id``, ``item_id``, ``surface_id``,
``cue_arm``, ``task_arm``, ``rollout``, ``task_correctness``, ``final_label``,
``judge_ids``, ``judge_disagreement``, ``output_length``, and
``headline_eligible``.  A ``judge_labels`` mapping is optional; when present it
enables directional per-judge vote effects in addition to disagreement rates.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, Callable


HERE = Path(__file__).resolve().parent
DEFAULT_CONFIG = HERE / "analysis_config.openrouter.json"
FROZEN_ANALYSIS_CONFIG_SHA256 = (
    "3c4b1f6a9e5aad99c66df809111a383728b3fb487a17dd437b5e475cd269670e"
)

_CONFIG_KEYS = {
    "schema_version",
    "design",
    "preregistration_id",
    "unit_of_inference",
    "actors",
    "comparisons",
    "cue_arms",
    "mixed_panel",
    "task_success_labels",
    "final_label_scores",
    "top_endpoint_label",
    "bottom_endpoint_label",
    "control_labels",
    "null_false_positive_labels",
    "required_judge_ids",
    "cluster_bootstrap",
    "thresholds",
    "rounding_digits",
}
_MIXED_PANEL_KEYS = {
    "cue_registration_rule",
    "base_primary_arm",
    "registered_cue_primary_arm",
    "development_required_cue_arms",
    "confirmation_arm",
    "confirmation_trigger",
}
_THRESHOLD_KEYS = {
    "smallest_effect_of_interest",
    "endpoint_item_rate",
    "saturated_item_fraction",
    "minimum_headline_items_per_actor",
    "minimum_task_success_rate",
    "stable_direction_fraction",
    "maximum_null_false_positive_rate",
    "maximum_counterbalanced_rank_reversal_fraction",
    "maximum_cue_dominance_ratio",
    "cue_model_interaction_report_threshold",
    "maximum_judge_disagreement_rate",
    "length_confound_absolute_correlation",
}
_ROW_FIELDS = {
    "actor_id",
    "item_id",
    "surface_id",
    "cue_arm",
    "task_arm",
    "rollout",
    "task_correctness",
    "final_label",
    "judge_ids",
    "judge_disagreement",
    "output_length",
    "headline_eligible",
}
_TASK_CORRECTNESS = {"correct", "partial", "incorrect", "not_assessable"}


def _strict_json_object(raw: bytes, name: str) -> dict[str, Any]:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"{name} has duplicate key {key!r}")
            result[key] = value
        return result

    def reject_constant(value: str) -> None:
        raise ValueError(f"{name} contains non-finite number {value}")

    try:
        decoded = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{name} must be strict UTF-8 JSON") from exc
    if not isinstance(decoded, dict):
        raise ValueError(f"{name} must be a JSON object")
    return decoded


def _closed_keys(record: Mapping[str, Any], expected: set[str], name: str) -> None:
    missing = sorted(expected - set(record))
    extra = sorted(set(record) - expected)
    if missing or extra:
        raise ValueError(f"{name} key mismatch: missing={missing}, extra={extra}")


def _nonblank(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{field} must be an exact non-blank string")
    return value


def _finite_number(value: Any, field: str, *, minimum: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a finite number >= {minimum}")
    number = float(value)
    if not math.isfinite(number) or number < minimum:
        raise ValueError(f"{field} must be a finite number >= {minimum}")
    return number


def _unit_interval(value: Any, field: str) -> float:
    number = _finite_number(value, field)
    if number > 1:
        raise ValueError(f"{field} must be in [0,1]")
    return number


def load_analysis_config(
    path: str | Path = DEFAULT_CONFIG,
    *,
    expected_sha256: str | None = None,
) -> tuple[dict[str, Any], dict[str, str]]:
    """Load and validate a raw-byte hash-bound analysis preregistration."""

    config_path = Path(path).resolve()
    raw = config_path.read_bytes()
    actual_sha256 = hashlib.sha256(raw).hexdigest()
    if expected_sha256 is None:
        if config_path != DEFAULT_CONFIG.resolve():
            raise ValueError("a non-default analysis config requires expected_sha256")
        expected_sha256 = FROZEN_ANALYSIS_CONFIG_SHA256
    if expected_sha256 != actual_sha256:
        raise ValueError(
            "analysis config hash mismatch: "
            f"expected {expected_sha256}, got {actual_sha256}"
        )

    cfg = _strict_json_object(raw, "analysis config")
    _closed_keys(cfg, _CONFIG_KEYS, "analysis config")
    if cfg["schema_version"] != "1.0" or cfg["design"] != "thorns":
        raise ValueError("analysis config must be THORNS schema_version 1.0")
    _nonblank(cfg["preregistration_id"], "preregistration_id")
    if cfg["unit_of_inference"] != "item":
        raise ValueError("THORNS analysis unit_of_inference must be item")

    actors = cfg["actors"]
    if actors != ["A01", "A02", "A03"]:
        raise ValueError("analysis actors must be exactly A01/A02/A03")
    expected_comparisons = [["A01", "A02"], ["A01", "A03"], ["A02", "A03"]]
    if cfg["comparisons"] != expected_comparisons:
        raise ValueError("analysis comparisons must enumerate the frozen actor pairs")

    cue_arms = cfg["cue_arms"]
    expected_cue_keys = {
        "original",
        "de_cued_primary",
        "null_foil",
        "sealed_confirmation",
    }
    if not isinstance(cue_arms, dict) or set(cue_arms) != expected_cue_keys:
        raise ValueError("analysis cue_arms must define C0/C1/C2/C3 roles")
    if list(cue_arms.values()) != ["C0", "C1", "C2", "C3"]:
        raise ValueError("analysis cue roles must resolve exactly to C0/C1/C2/C3")

    mixed_panel = cfg["mixed_panel"]
    if not isinstance(mixed_panel, dict):
        raise ValueError("analysis mixed_panel must be an object")
    _closed_keys(mixed_panel, _MIXED_PANEL_KEYS, "analysis mixed_panel")
    expected_mixed_panel = {
        "cue_registration_rule": "ANY_HEADLINE_NON_C0_ARM",
        "base_primary_arm": cue_arms["original"],
        "registered_cue_primary_arm": cue_arms["de_cued_primary"],
        "development_required_cue_arms": [
            cue_arms["original"],
            cue_arms["de_cued_primary"],
            cue_arms["null_foil"],
        ],
        "confirmation_arm": cue_arms["sealed_confirmation"],
        "confirmation_trigger": "ANY_HEADLINE_C3_ROW",
    }
    if mixed_panel != expected_mixed_panel:
        raise ValueError(
            "analysis mixed_panel must freeze the registered mixed-stage policy"
        )

    scores = cfg["final_label_scores"]
    if not isinstance(scores, dict) or set(scores) != {"Fi", "Wj", "CFT", "mixed", "other"}:
        raise ValueError("analysis final_label_scores must cover the five THORNS labels")
    for label, value in scores.items():
        _unit_interval(value, f"final_label_scores.{label}")
    if cfg["top_endpoint_label"] != "Fi" or cfg["bottom_endpoint_label"] != "Wj":
        raise ValueError("THORNS endpoint labels must remain Fi and Wj")
    control_labels = cfg["control_labels"]
    if control_labels != [
        "foil_correct",
        "target_action_false_positive",
        "indeterminate",
    ]:
        raise ValueError(
            "control_labels must freeze the three explicit C2 outcomes"
        )
    null_labels = cfg["null_false_positive_labels"]
    if (
        not isinstance(null_labels, list)
        or not null_labels
        or len(null_labels) != len(set(null_labels))
        or set(null_labels) - set(control_labels)
    ):
        raise ValueError("null_false_positive_labels must be unique C2 control labels")
    if null_labels != ["target_action_false_positive"]:
        raise ValueError(
            "the C2 false-positive endpoint must be target_action_false_positive"
        )
    if cfg["task_success_labels"] != ["correct"]:
        raise ValueError("task-success conditioning is frozen to exact correctness")
    if cfg["required_judge_ids"] != ["J01", "J02"]:
        raise ValueError("analysis requires the frozen J01/J02 judge pair")
    bootstrap = cfg["cluster_bootstrap"]
    if not isinstance(bootstrap, dict) or set(bootstrap) != {
        "unit",
        "replicates",
        "confidence_level",
        "seed",
    }:
        raise ValueError("cluster_bootstrap must freeze unit/replicates/confidence/seed")
    if bootstrap["unit"] != "item":
        raise ValueError("cluster bootstrap unit must be item")
    if (
        isinstance(bootstrap["replicates"], bool)
        or not isinstance(bootstrap["replicates"], int)
        or bootstrap["replicates"] < 1000
    ):
        raise ValueError("cluster_bootstrap.replicates must be an integer >=1000")
    confidence_level = _unit_interval(
        bootstrap["confidence_level"], "cluster_bootstrap.confidence_level"
    )
    if not 0 < confidence_level < 1:
        raise ValueError("cluster_bootstrap.confidence_level must be strictly in (0,1)")
    if isinstance(bootstrap["seed"], bool) or not isinstance(bootstrap["seed"], int):
        raise ValueError("cluster_bootstrap.seed must be an integer")

    thresholds = cfg["thresholds"]
    if not isinstance(thresholds, dict):
        raise ValueError("analysis thresholds must be an object")
    _closed_keys(thresholds, _THRESHOLD_KEYS, "analysis thresholds")
    for key, value in thresholds.items():
        if key == "minimum_headline_items_per_actor":
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"thresholds.{key} must be a positive integer")
        else:
            _unit_interval(value, f"thresholds.{key}")
    if thresholds["maximum_cue_dominance_ratio"] != 1.0:
        raise ValueError("cue dominance ratio boundary is frozen to 1.0")
    digits = cfg["rounding_digits"]
    if isinstance(digits, bool) or not isinstance(digits, int) or not 0 <= digits <= 12:
        raise ValueError("rounding_digits must be an integer in [0,12]")

    return cfg, {"path": str(config_path), "sha256": actual_sha256}


def _mean(values: Sequence[float]) -> float | None:
    return statistics.mean(values) if values else None


def _median(values: Sequence[float]) -> float | None:
    return statistics.median(values) if values else None


def _sign(value: float | None) -> int:
    if value is None or value == 0:
        return 0
    return 1 if value > 0 else -1


def _direction_fraction(differences: Sequence[float], direction: int) -> float:
    nonzero = [value for value in differences if value != 0]
    if not nonzero:
        return 1.0
    return sum(_sign(value) == direction for value in nonzero) / len(nonzero)


def _cluster_bootstrap_interval(
    values: Sequence[float], *, cfg: Mapping[str, Any], seed_key: str
) -> list[float] | None:
    if not values:
        return None
    bootstrap = cfg["cluster_bootstrap"]
    seed_material = f"{bootstrap['seed']}:{seed_key}".encode("utf-8")
    seed = int.from_bytes(hashlib.sha256(seed_material).digest()[:8], "big")
    rng = random.Random(seed)
    n = len(values)
    draws = sorted(
        statistics.mean(values[rng.randrange(n)] for _ in range(n))
        for _ in range(bootstrap["replicates"])
    )
    alpha = 1.0 - bootstrap["confidence_level"]
    lower_index = math.floor((alpha / 2.0) * (len(draws) - 1))
    upper_index = math.ceil((1.0 - alpha / 2.0) * (len(draws) - 1))
    return [draws[lower_index], draws[upper_index]]


def _round_tree(value: Any, digits: int) -> Any:
    if isinstance(value, float):
        return round(value, digits)
    if isinstance(value, dict):
        return {key: _round_tree(child, digits) for key, child in value.items()}
    if isinstance(value, list):
        return [_round_tree(child, digits) for child in value]
    return value


def _normalize_rows(
    rows: Sequence[Mapping[str, Any]], cfg: Mapping[str, Any]
) -> tuple[list[dict[str, Any]], list[str]]:
    if isinstance(rows, (str, bytes, bytearray)) or not isinstance(rows, Sequence):
        raise ValueError("terminal rows must be a sequence of objects")
    if not rows:
        raise ValueError("terminal rows must not be empty")
    actors = set(cfg["actors"])
    cues = set(cfg["cue_arms"].values())
    construct_labels = set(cfg["final_label_scores"])
    control_labels = set(cfg["control_labels"])
    null_cue = cfg["cue_arms"]["null_foil"]
    normalized = []
    integrity_failures: list[str] = []
    headline_keys: set[tuple[Any, ...]] = set()
    surface_cues: dict[str, str] = {}
    item_cue_surfaces: dict[tuple[str, str], str] = {}
    required_judges = set(cfg["required_judge_ids"])

    for index, source in enumerate(rows):
        if not isinstance(source, Mapping):
            raise ValueError(f"terminal row {index} must be an object")
        missing = sorted(_ROW_FIELDS - set(source))
        if missing:
            raise ValueError(f"terminal row {index} missing field(s) {missing}")
        row = dict(source)
        actor_id = _nonblank(row["actor_id"], f"row {index}.actor_id")
        if actor_id not in actors:
            raise ValueError(f"row {index}.actor_id is not one of {sorted(actors)}")
        row["item_id"] = _nonblank(row["item_id"], f"row {index}.item_id")
        row["surface_id"] = _nonblank(row["surface_id"], f"row {index}.surface_id")
        cue_arm = _nonblank(row["cue_arm"], f"row {index}.cue_arm")
        if cue_arm not in cues:
            raise ValueError(f"row {index}.cue_arm is not one of {sorted(cues)}")
        row["task_arm"] = _nonblank(row["task_arm"], f"row {index}.task_arm")
        rollout = row["rollout"]
        if isinstance(rollout, bool) or not isinstance(rollout, int) or rollout < 0:
            raise ValueError(f"row {index}.rollout must be a non-negative integer")
        correctness = row["task_correctness"]
        if correctness not in _TASK_CORRECTNESS:
            raise ValueError(
                f"row {index}.task_correctness must be one of {sorted(_TASK_CORRECTNESS)}"
            )
        if not isinstance(row["headline_eligible"], bool):
            raise ValueError(f"row {index}.headline_eligible must be boolean")
        if not isinstance(row["judge_disagreement"], bool):
            raise ValueError(f"row {index}.judge_disagreement must be boolean")
        row["output_length"] = _finite_number(
            row["output_length"], f"row {index}.output_length"
        )

        final_label = row["final_label"]
        is_control = cue_arm == null_cue
        allowed_labels = control_labels if is_control else construct_labels
        row["_label_domain"] = "control" if is_control else "construct"
        row["_resolved"] = final_label in allowed_labels
        if final_label is not None and final_label not in allowed_labels:
            if not isinstance(final_label, str) or final_label.lower() not in {
                "unresolved",
                "no_fusion",
            }:
                domain = "C2 control" if is_control else "THORNS construct"
                raise ValueError(
                    f"row {index}.final_label is not a {domain} label"
                )

        judge_ids = row["judge_ids"]
        if (
            isinstance(judge_ids, (str, bytes, bytearray))
            or not isinstance(judge_ids, Sequence)
            or any(not isinstance(judge_id, str) for judge_id in judge_ids)
            or len(judge_ids) != len(set(judge_ids))
        ):
            raise ValueError(f"row {index}.judge_ids must be a unique string list")
        row["judge_ids"] = list(judge_ids)
        if row["headline_eligible"] and set(judge_ids) != required_judges:
            integrity_failures.append("JUDGE_ID_SET")

        judge_labels = row.get("judge_labels")
        if judge_labels is not None:
            if not isinstance(judge_labels, Mapping) or set(judge_labels) != set(judge_ids):
                raise ValueError(
                    f"row {index}.judge_labels must exactly map the listed judge_ids"
                )
            normalized_votes = {}
            for judge_id, label in judge_labels.items():
                if label not in allowed_labels:
                    domain = "C2 control" if is_control else "THORNS construct"
                    raise ValueError(
                        f"row {index}.judge_labels[{judge_id!r}] is not a {domain} label"
                    )
                normalized_votes[judge_id] = label
            row["judge_labels"] = normalized_votes
            observed_disagreement = len(set(normalized_votes.values())) > 1
            if (
                row["headline_eligible"]
                and row["judge_disagreement"] != observed_disagreement
            ):
                integrity_failures.append("JUDGE_DISAGREEMENT_MISMATCH")

        if row["headline_eligible"]:
            prior_cue = surface_cues.setdefault(row["surface_id"], cue_arm)
            if prior_cue != cue_arm:
                integrity_failures.append("SURFACE_CUE_COLLISION")
            item_cue_key = (row["item_id"], cue_arm)
            prior_surface = item_cue_surfaces.setdefault(
                item_cue_key, row["surface_id"]
            )
            if prior_surface != row["surface_id"]:
                integrity_failures.append("SURFACE_ASSIGNMENT_MISMATCH")
            key = (
                actor_id,
                row["item_id"],
                row["surface_id"],
                row["task_arm"],
                rollout,
            )
            if key in headline_keys:
                integrity_failures.append("DUPLICATE_TERMINAL_KEY")
            headline_keys.add(key)
        normalized.append(row)

    return normalized, integrity_failures


def _cell_summary(
    rows: Sequence[Mapping[str, Any]], cfg: Mapping[str, Any]
) -> dict[str, Any]:
    is_control = bool(rows and rows[0]["_label_domain"] == "control")
    labels = list(cfg["control_labels"] if is_control else cfg["final_label_scores"])
    scores = cfg["final_label_scores"]
    resolved = [row for row in rows if row["_resolved"]]
    successful = [
        row
        for row in resolved
        if row["task_correctness"] in cfg["task_success_labels"]
    ]

    def outcomes(selected: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
        n = len(selected)
        return {
            "n_rollouts": n,
            "label_rates": {
                label: (sum(row["final_label"] == label for row in selected) / n if n else None)
                for label in labels
            },
            "primary_mean": (
                statistics.mean(scores[row["final_label"]] for row in selected)
                if selected and not is_control
                else None
            ),
        }

    return {
        "n_rollouts": len(rows),
        "n_resolved": len(resolved),
        "task_success_rate": (
            sum(
                row["task_correctness"] in cfg["task_success_labels"]
                for row in rows
            )
            / len(rows)
        ),
        "unconditional": outcomes(resolved),
        "task_success_conditioned": outcomes(successful),
    }


def _surface_item_matrix(
    rows: Sequence[Mapping[str, Any]],
    *,
    cue_arm: str,
    cfg: Mapping[str, Any],
    value: Callable[[Mapping[str, Any]], float],
) -> dict[tuple[str, str], float]:
    by_task: dict[tuple[str, str, str], list[float]] = defaultdict(list)
    for row in rows:
        if (
            row["cue_arm"] == cue_arm
            and row["_resolved"]
            and row["task_correctness"] in cfg["task_success_labels"]
        ):
            by_task[(row["actor_id"], row["item_id"], row["task_arm"])].append(
                value(row)
            )
    by_item: dict[tuple[str, str], list[float]] = defaultdict(list)
    for (actor_id, item_id, _task_arm), values in by_task.items():
        by_item[(actor_id, item_id)].append(statistics.mean(values))
    return {key: statistics.mean(values) for key, values in by_item.items()}


def _task_success_matrix(
    rows: Sequence[Mapping[str, Any]], *, cue_arm: str, cfg: Mapping[str, Any]
) -> dict[tuple[str, str], float]:
    by_task: dict[tuple[str, str, str], list[float]] = defaultdict(list)
    for row in rows:
        if row["cue_arm"] == cue_arm:
            by_task[(row["actor_id"], row["item_id"], row["task_arm"])].append(
                float(row["task_correctness"] in cfg["task_success_labels"])
            )
    by_item: dict[tuple[str, str], list[float]] = defaultdict(list)
    for (actor_id, item_id, _task_arm), values in by_task.items():
        by_item[(actor_id, item_id)].append(statistics.mean(values))
    return {key: statistics.mean(values) for key, values in by_item.items()}


def _selected_item_matrix(
    rows: Sequence[Mapping[str, Any]],
    *,
    selected_arm_by_item: Mapping[str, str],
    cfg: Mapping[str, Any],
    value: Callable[[Mapping[str, Any]], float],
) -> dict[tuple[str, str], float]:
    """Reduce the mixed base/cue primary panel at the item level."""

    by_task: dict[tuple[str, str, str], list[float]] = defaultdict(list)
    for row in rows:
        if (
            selected_arm_by_item.get(row["item_id"]) == row["cue_arm"]
            and row["_resolved"]
            and row["task_correctness"] in cfg["task_success_labels"]
        ):
            by_task[(row["actor_id"], row["item_id"], row["task_arm"])].append(
                value(row)
            )
    by_item: dict[tuple[str, str], list[float]] = defaultdict(list)
    for (actor_id, item_id, _task_arm), values in by_task.items():
        by_item[(actor_id, item_id)].append(statistics.mean(values))
    return {key: statistics.mean(values) for key, values in by_item.items()}


def _selected_task_success_matrix(
    rows: Sequence[Mapping[str, Any]],
    *,
    selected_arm_by_item: Mapping[str, str],
    cfg: Mapping[str, Any],
) -> dict[tuple[str, str], float]:
    by_task: dict[tuple[str, str, str], list[float]] = defaultdict(list)
    for row in rows:
        if selected_arm_by_item.get(row["item_id"]) == row["cue_arm"]:
            by_task[(row["actor_id"], row["item_id"], row["task_arm"])].append(
                float(row["task_correctness"] in cfg["task_success_labels"])
            )
    by_item: dict[tuple[str, str], list[float]] = defaultdict(list)
    for (actor_id, item_id, _task_arm), values in by_task.items():
        by_item[(actor_id, item_id)].append(statistics.mean(values))
    return {key: statistics.mean(values) for key, values in by_item.items()}


def _paired_effect(
    matrix: Mapping[tuple[str, str], float],
    actor_a: str,
    actor_b: str,
    *,
    cfg: Mapping[str, Any],
    seed_key: str,
) -> dict[str, Any]:
    items_a = {item_id for actor, item_id in matrix if actor == actor_a}
    items_b = {item_id for actor, item_id in matrix if actor == actor_b}
    common = sorted(items_a & items_b)
    differences = [matrix[(actor_a, item)] - matrix[(actor_b, item)] for item in common]
    effect = _mean(differences)
    direction = _sign(effect)
    return {
        "effect": effect,
        "n_items": len(common),
        "nonzero_n_items": sum(value != 0 for value in differences),
        "direction": direction,
        "direction_fraction": _direction_fraction(differences, direction),
        "cluster_bootstrap_ci": _cluster_bootstrap_interval(
            differences, cfg=cfg, seed_key=seed_key
        ),
        "item_differences": differences,
        "item_ids": common,
    }


def _pearson(xs: Sequence[float], ys: Sequence[float]) -> float | None:
    if len(xs) != len(ys) or len(xs) < 2:
        return None
    x_mean = statistics.mean(xs)
    y_mean = statistics.mean(ys)
    x_dev = [value - x_mean for value in xs]
    y_dev = [value - y_mean for value in ys]
    x_ss = sum(value * value for value in x_dev)
    y_ss = sum(value * value for value in y_dev)
    if x_ss == 0 or y_ss == 0:
        return None
    return sum(x * y for x, y in zip(x_dev, y_dev)) / math.sqrt(x_ss * y_ss)


def _clustered_row_mean(
    rows: Sequence[Mapping[str, Any]], value: Callable[[Mapping[str, Any]], float | None]
) -> tuple[float | None, int]:
    by_cell: dict[tuple[str, str, str, str], list[float]] = defaultdict(list)
    for row in rows:
        observed = value(row)
        if observed is not None:
            by_cell[
                (row["actor_id"], row["item_id"], row["cue_arm"], row["task_arm"])
            ].append(observed)
    by_item: dict[str, list[float]] = defaultdict(list)
    for (_actor, item_id, _cue, _task), values in by_cell.items():
        by_item[item_id].append(statistics.mean(values))
    item_values = [statistics.mean(values) for values in by_item.values()]
    return _mean(item_values), len(by_item)


def _counterbalance_coverage_diagnostics(
    rows: Sequence[Mapping[str, Any]], cfg: Mapping[str, Any]
) -> dict[str, Any]:
    """Validate the preregistered mixed panel and staged C3 transition.

    An item becomes a registered cue item when any headline non-C0 arm is
    observed.  Registered cue items must have actor-balanced C0/C1/C2 task
    arms.  Items with C0 only are base items and require only actor-balanced
    C0.  C3 is optional throughout development, but the first headline C3 row
    atomically starts locked confirmation and requires C3 for every registered
    cue item and actor.
    """

    actors = list(cfg["actors"])
    policy = cfg["mixed_panel"]
    base_arm = policy["base_primary_arm"]
    development_arms = list(policy["development_required_cue_arms"])
    confirmation_arm = policy["confirmation_arm"]
    item_ids = sorted({row["item_id"] for row in rows})
    arms_by_item: dict[str, set[str]] = defaultdict(set)
    actual: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for row in rows:
        item_id = row["item_id"]
        arms_by_item[item_id].add(row["cue_arm"])
        actual[(row["actor_id"], item_id, row["cue_arm"])].add(
            row["task_arm"]
        )

    registered_cue_items = sorted(
        item_id
        for item_id in item_ids
        if any(arm != base_arm for arm in arms_by_item[item_id])
    )
    registered_set = set(registered_cue_items)
    base_items = sorted(set(item_ids) - registered_set)
    confirmation_started = any(
        confirmation_arm in arms_by_item[item_id]
        for item_id in registered_cue_items
    )

    missing_cells: list[dict[str, Any]] = []
    for item_id in item_ids:
        required_arms = (
            list(development_arms) if item_id in registered_set else [base_arm]
        )
        if confirmation_started and item_id in registered_set:
            required_arms.append(confirmation_arm)

        # C0 defines the task-arm contract.  If malformed evidence lacks C0,
        # the union of observed arms still gives deterministic diagnostics.
        expected_tasks = set().union(
            *(actual[(actor_id, item_id, base_arm)] for actor_id in actors)
        )
        if not expected_tasks:
            expected_tasks = set().union(
                *(
                    actual[(actor_id, item_id, arm)]
                    for actor_id in actors
                    for arm in required_arms
                )
            )
        for cue_arm in required_arms:
            for actor_id in actors:
                observed = actual[(actor_id, item_id, cue_arm)]
                if observed != expected_tasks:
                    missing_cells.append(
                        {
                            "actor_id": actor_id,
                            "item_id": item_id,
                            "cue_arm": cue_arm,
                            "missing_task_arms": sorted(expected_tasks - observed),
                            "unexpected_task_arms": sorted(observed - expected_tasks),
                        }
                    )

    missing_cells.sort(
        key=lambda cell: (cell["item_id"], cell["cue_arm"], cell["actor_id"])
    )
    confirmation_missing = [
        cell for cell in missing_cells if cell["cue_arm"] == confirmation_arm
    ]
    confirmation_complete = (
        confirmation_started and not confirmation_missing and not missing_cells
    )
    return {
        "unit": "actor/item/cue/task-arm cell",
        "stage": "locked_confirmation" if confirmation_started else "development",
        "base_item_ids": base_items,
        "base_item_count": len(base_items),
        "registered_cue_item_ids": registered_cue_items,
        "registered_cue_item_count": len(registered_cue_items),
        "cue_registration_rule": policy["cue_registration_rule"],
        "primary_arm_by_role": {
            "base": policy["base_primary_arm"],
            "registered_cue": policy["registered_cue_primary_arm"],
        },
        "development_required_cue_arms": development_arms,
        "confirmation_arm": confirmation_arm,
        "confirmation_status": (
            "pending"
            if not confirmation_started
            else "complete"
            if confirmation_complete
            else "incomplete"
        ),
        "confirmation_pending": not confirmation_started,
        "confirmation_complete": confirmation_complete,
        "missing_cell_count": len(missing_cells),
        "missing_cells": missing_cells,
    }


def _judge_diagnostics(
    rows: Sequence[Mapping[str, Any]], cfg: Mapping[str, Any]
) -> dict[str, Any]:
    construct_score = cfg["final_label_scores"]
    control_score = {"foil_correct": 0.0, "target_action_false_positive": 1.0}

    def score_for(row: Mapping[str, Any]) -> Mapping[str, float]:
        return control_score if row["_label_domain"] == "control" else construct_score

    overall_rate, overall_n = _clustered_row_mean(
        rows, lambda row: float(row["judge_disagreement"])
    )
    by_judge = {}
    for judge_id in cfg["required_judge_ids"]:
        judge_rows = [row for row in rows if judge_id in row["judge_ids"]]
        disagreement_rate, _ = _clustered_row_mean(
            judge_rows, lambda row: float(row["judge_disagreement"])
        )

        def vote_effect(row: Mapping[str, Any]) -> float | None:
            votes = row.get("judge_labels")
            if not isinstance(votes, Mapping) or not row["_resolved"]:
                return None
            scores = score_for(row)
            if votes[judge_id] not in scores:
                return None
            return scores[votes[judge_id]] - scores[row["final_label"]]

        effect, effect_n = _clustered_row_mean(judge_rows, vote_effect)
        by_judge[judge_id] = {
            "n_rows": len(judge_rows),
            "n_items": len({row["item_id"] for row in judge_rows}),
            "disagreement_exposure_rate": disagreement_rate,
            "vote_minus_resolved_effect": effect,
            "vote_effect_n_items": effect_n,
        }

    pairwise = []
    for judge_a, judge_b in [cfg["required_judge_ids"]]:
        def judge_difference(row: Mapping[str, Any]) -> float | None:
            votes = row.get("judge_labels")
            if not isinstance(votes, Mapping):
                return None
            scores = score_for(row)
            if votes[judge_a] not in scores or votes[judge_b] not in scores:
                return None
            return scores[votes[judge_a]] - scores[votes[judge_b]]

        effect, n_items = _clustered_row_mean(rows, judge_difference)
        pairwise.append(
            {
                "judge_a": judge_a,
                "judge_b": judge_b,
                "effect": effect,
                "n_items": n_items,
            }
        )
    return {
        "unit": "item",
        "overall_disagreement_rate": overall_rate,
        "n_items": overall_n,
        "by_judge": by_judge,
        "pairwise_judge_effects": pairwise,
    }


def analyze_terminal_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    config_path: str | Path = DEFAULT_CONFIG,
    expected_config_sha256: str | None = None,
) -> dict[str, Any]:
    """Analyze resolved THORNS terminal rows without mutation or external calls."""

    cfg, config_provenance = load_analysis_config(
        config_path, expected_sha256=expected_config_sha256
    )
    normalized, integrity_failures = _normalize_rows(rows, cfg)
    headline = [row for row in normalized if row["headline_eligible"]]
    if not headline:
        raise ValueError("terminal rows contain no headline-eligible evidence")
    thresholds = cfg["thresholds"]
    actors = cfg["actors"]
    comparisons = cfg["comparisons"]
    scores = cfg["final_label_scores"]
    cue = cfg["cue_arms"]
    primary_cue = cue["de_cued_primary"]
    coverage_diagnostics = _counterbalance_coverage_diagnostics(headline, cfg)
    registered_cue_items = set(
        coverage_diagnostics["registered_cue_item_ids"]
    )
    primary_arm_by_item = {
        item_id: (
            cfg["mixed_panel"]["registered_cue_primary_arm"]
            if item_id in registered_cue_items
            else cfg["mixed_panel"]["base_primary_arm"]
        )
        for item_id in {row["item_id"] for row in headline}
    }

    grouped: dict[tuple[str, str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in headline:
        grouped[
            (
                row["actor_id"],
                row["item_id"],
                row["surface_id"],
                row["cue_arm"],
                row["task_arm"],
            )
        ].append(row)
    per_actor_item_rates = []
    for (actor_id, item_id, surface_id, cue_arm, task_arm), cell_rows in sorted(
        grouped.items()
    ):
        per_actor_item_rates.append(
            {
                "actor_id": actor_id,
                "item_id": item_id,
                "surface_id": surface_id,
                "cue_arm": cue_arm,
                "task_arm": task_arm,
                **_cell_summary(cell_rows, cfg),
            }
        )

    construct_cues = (
        cue["original"],
        cue["de_cued_primary"],
        cue["sealed_confirmation"],
    )
    score_matrices = {
        cue_arm: _surface_item_matrix(
            headline,
            cue_arm=cue_arm,
            cfg=cfg,
            value=lambda row: scores[row["final_label"]],
        )
        for cue_arm in construct_cues
    }
    primary_score_matrix = _selected_item_matrix(
        headline,
        selected_arm_by_item=primary_arm_by_item,
        cfg=cfg,
        value=lambda row: scores[row["final_label"]],
    )
    top_matrix = _selected_item_matrix(
        headline,
        selected_arm_by_item=primary_arm_by_item,
        cfg=cfg,
        value=lambda row: float(row["final_label"] == cfg["top_endpoint_label"]),
    )
    bottom_matrix = _selected_item_matrix(
        headline,
        selected_arm_by_item=primary_arm_by_item,
        cfg=cfg,
        value=lambda row: float(row["final_label"] == cfg["bottom_endpoint_label"]),
    )
    length_matrix = _selected_item_matrix(
        headline,
        selected_arm_by_item=primary_arm_by_item,
        cfg=cfg,
        value=lambda row: row["output_length"],
    )
    task_matrix = _selected_task_success_matrix(
        headline, selected_arm_by_item=primary_arm_by_item, cfg=cfg
    )

    task_by_actor = {}
    for actor_id in actors:
        values = [value for (actor, _item), value in task_matrix.items() if actor == actor_id]
        rate = _mean(values)
        task_by_actor[actor_id] = {
            "n_items": len(values),
            "rate": rate,
            "passes": (
                len(values) >= thresholds["minimum_headline_items_per_actor"]
                and rate is not None
                and rate >= thresholds["minimum_task_success_rate"]
            ),
        }
    task_success = {
        "condition": cfg["task_success_labels"],
        "minimum_rate": thresholds["minimum_task_success_rate"],
        "by_actor": task_by_actor,
        "all_actors_pass": all(value["passes"] for value in task_by_actor.values()),
    }

    raw_pairwise = []
    soei = thresholds["smallest_effect_of_interest"]
    stable_direction = thresholds["stable_direction_fraction"]
    for actor_a, actor_b in comparisons:
        pair_key = f"{actor_a}-{actor_b}"
        primary = _paired_effect(
            primary_score_matrix,
            actor_a,
            actor_b,
            cfg=cfg,
            seed_key=f"{pair_key}:mixed-primary",
        )
        original = _paired_effect(
            score_matrices[cue["original"]],
            actor_a,
            actor_b,
            cfg=cfg,
            seed_key=f"{pair_key}:{cue['original']}",
        )
        confirmation_reference = _paired_effect(
            score_matrices[primary_cue],
            actor_a,
            actor_b,
            cfg=cfg,
            seed_key=f"{pair_key}:{primary_cue}:confirmation-reference",
        )
        confirmation_matrix = (
            score_matrices[cue["sealed_confirmation"]]
            if coverage_diagnostics["confirmation_complete"]
            else {}
        )
        confirmation = _paired_effect(
            confirmation_matrix,
            actor_a,
            actor_b,
            cfg=cfg,
            seed_key=f"{pair_key}:{cue['sealed_confirmation']}",
        )
        effect = primary["effect"]
        confirmation_same_direction = (
            confirmation_reference["effect"] is not None
            and confirmation["effect"] is not None
            and _sign(confirmation_reference["effect"]) != 0
            and _sign(confirmation_reference["effect"])
            == _sign(confirmation["effect"])
        )
        exceeds_soei = effect is not None and abs(effect) > soei
        primary_ci = primary["cluster_bootstrap_ci"]
        confirmation_ci = confirmation["cluster_bootstrap_ci"]
        primary_ci_excludes_zero = (
            primary_ci is not None and (primary_ci[0] > 0 or primary_ci[1] < 0)
        )
        confirmation_ci_excludes_zero = (
            confirmation_ci is not None
            and (confirmation_ci[0] > 0 or confirmation_ci[1] < 0)
        )
        development_stable = (
            exceeds_soei
            and primary_ci_excludes_zero
            and primary["direction_fraction"] >= stable_direction
        )
        preliminarily_stable = (
            development_stable
            and coverage_diagnostics["confirmation_complete"]
            and confirmation_same_direction
            and confirmation_ci_excludes_zero
            and confirmation["direction_fraction"] >= stable_direction
        )
        raw_pairwise.append(
            {
                "actor_a": actor_a,
                "actor_b": actor_b,
                "effect": effect,
                "n_items": primary["n_items"],
                "nonzero_n_items": primary["nonzero_n_items"],
                "direction": primary["direction"],
                "direction_fraction": primary["direction_fraction"],
                "bootstrap_unit": cfg["cluster_bootstrap"]["unit"],
                "bootstrap_replicates": cfg["cluster_bootstrap"]["replicates"],
                "bootstrap_confidence_level": cfg["cluster_bootstrap"][
                    "confidence_level"
                ],
                "cluster_bootstrap_ci": primary_ci,
                "cluster_bootstrap_ci_excludes_zero": primary_ci_excludes_zero,
                "soei": soei,
                "inside_indifference_region": (
                    effect is not None and abs(effect) <= soei
                ),
                "exceeds_soei": exceeds_soei,
                "development_stable": development_stable,
                "original_effect": original["effect"],
                "original_n_items": original["n_items"],
                "confirmation_reference_effect": confirmation_reference["effect"],
                "confirmation_reference_n_items": confirmation_reference["n_items"],
                "confirmation_effect": confirmation["effect"],
                "confirmation_n_items": confirmation["n_items"],
                "confirmation_cluster_bootstrap_ci": confirmation_ci,
                "confirmation_ci_excludes_zero": confirmation_ci_excludes_zero,
                "confirmation_same_direction": confirmation_same_direction,
                "confirmation_direction_fraction": confirmation["direction_fraction"],
                "preliminarily_stable": preliminarily_stable,
                "_item_ids": primary["item_ids"],
                "_score_differences": primary["item_differences"],
            }
        )

    length_by_actor = {}
    for actor_id in actors:
        values = [value for (actor, _item), value in length_matrix.items() if actor == actor_id]
        length_by_actor[actor_id] = {
            "n_items": len(values),
            "mean_length": _mean(values),
        }
    length_pairwise = []
    length_confounded_pairs: set[tuple[str, str]] = set()
    for effect in raw_pairwise:
        actor_a, actor_b = effect["actor_a"], effect["actor_b"]
        common_items = [
            item_id
            for item_id in effect["_item_ids"]
            if (actor_a, item_id) in length_matrix and (actor_b, item_id) in length_matrix
        ]
        score_differences = [
            primary_score_matrix[(actor_a, item_id)]
            - primary_score_matrix[(actor_b, item_id)]
            for item_id in common_items
        ]
        length_differences = [
            length_matrix[(actor_a, item_id)] - length_matrix[(actor_b, item_id)]
            for item_id in common_items
        ]
        correlation = _pearson(score_differences, length_differences)
        potential_confound = (
            effect["development_stable"]
            and correlation is not None
            and abs(correlation)
            >= thresholds["length_confound_absolute_correlation"]
        )
        if potential_confound:
            length_confounded_pairs.add((actor_a, actor_b))
        length_pairwise.append(
            {
                "actor_a": actor_a,
                "actor_b": actor_b,
                "n_items": len(common_items),
                "mean_length_difference": _mean(length_differences),
                "score_length_difference_correlation": correlation,
                "potential_confound": potential_confound,
            }
        )
        effect["length_potential_confound"] = potential_confound
        effect["development_stable"] = (
            effect["development_stable"] and not potential_confound
        )
        effect["stable"] = effect["preliminarily_stable"] and not potential_confound
        del effect["_item_ids"]
        del effect["_score_differences"]

    endpoint_by_actor = {}
    endpoint_rate = thresholds["endpoint_item_rate"]
    saturated_fraction = thresholds["saturated_item_fraction"]
    for actor_id in actors:
        top_values = [value for (actor, _item), value in top_matrix.items() if actor == actor_id]
        bottom_values = [
            value for (actor, _item), value in bottom_matrix.items() if actor == actor_id
        ]
        top_fraction = (
            sum(value >= endpoint_rate for value in top_values) / len(top_values)
            if top_values
            else None
        )
        bottom_fraction = (
            sum(value >= endpoint_rate for value in bottom_values) / len(bottom_values)
            if bottom_values
            else None
        )
        at_ceiling = top_fraction is not None and top_fraction >= saturated_fraction
        at_floor = bottom_fraction is not None and bottom_fraction >= saturated_fraction
        endpoint_by_actor[actor_id] = {
            "n_items": len(top_values),
            "top_endpoint_item_fraction": top_fraction,
            "bottom_endpoint_item_fraction": bottom_fraction,
            "endpoint_classification": (
                "CEILING" if at_ceiling else "FLOOR" if at_floor else "INTERIOR"
            ),
        }
    all_pairwise_below_soei = all(
        effect["effect"] is not None and abs(effect["effect"]) < soei
        for effect in raw_pairwise
    )
    saturated_high = (
        task_success["all_actors_pass"]
        and all(
            value["endpoint_classification"] == "CEILING"
            for value in endpoint_by_actor.values()
        )
        and all_pairwise_below_soei
    )
    saturated_low = (
        task_success["all_actors_pass"]
        and all(
            value["endpoint_classification"] == "FLOOR"
            for value in endpoint_by_actor.values()
        )
        and all_pairwise_below_soei
    )
    saturation = {
        "unit": "item",
        "top_endpoint_label": cfg["top_endpoint_label"],
        "bottom_endpoint_label": cfg["bottom_endpoint_label"],
        "endpoint_item_rate": endpoint_rate,
        "saturated_item_fraction": saturated_fraction,
        "by_actor": endpoint_by_actor,
        "all_pairwise_below_soei": all_pairwise_below_soei,
        "classification": (
            "SATURATED-HIGH"
            if saturated_high
            else "SATURATED-LOW"
            if saturated_low
            else "NOT-SATURATED"
        ),
    }

    original_matrix = score_matrices[cue["original"]]
    primary_matrix = score_matrices[primary_cue]
    cue_effects_by_actor = {}
    all_absolute_cue_effects = []
    actor_cue_means = {}
    for actor_id in actors:
        original_items = {item for actor, item in original_matrix if actor == actor_id}
        primary_items = {item for actor, item in primary_matrix if actor == actor_id}
        common = sorted(original_items & primary_items)
        differences = [
            original_matrix[(actor_id, item)] - primary_matrix[(actor_id, item)]
            for item in common
        ]
        all_absolute_cue_effects.extend(abs(value) for value in differences)
        actor_cue_means[actor_id] = _mean(differences)
        cue_effects_by_actor[actor_id] = {
            "effect_c0_minus_c1": _mean(differences),
            "median_absolute_item_effect": _median(
                [abs(value) for value in differences]
            ),
            "n_items": len(common),
        }
    cue_interactions = []
    for actor_a, actor_b in comparisons:
        effect_a = actor_cue_means[actor_a]
        effect_b = actor_cue_means[actor_b]
        cue_interactions.append(
            {
                "actor_a": actor_a,
                "actor_b": actor_b,
                "difference_in_cue_effects": (
                    effect_a - effect_b
                    if effect_a is not None and effect_b is not None
                    else None
                ),
            }
        )
    present_cue_means = [value for value in actor_cue_means.values() if value is not None]
    interaction_range = (
        max(present_cue_means) - min(present_cue_means)
        if present_cue_means
        else None
    )

    complete_rank_items = []
    reversed_items = []
    all_item_ids = sorted({row["item_id"] for row in headline})
    for item_id in all_item_ids:
        if not all(
            (actor_id, item_id) in score_matrices[arm]
            for actor_id in actors
            for arm in (cue["original"], primary_cue, cue["sealed_confirmation"])
        ):
            continue
        complete_rank_items.append(item_id)
        reversed_here = False
        for actor_a, actor_b in comparisons:
            surface_directions = []
            for arm in (cue["original"], primary_cue, cue["sealed_confirmation"]):
                difference = (
                    score_matrices[arm][(actor_a, item_id)]
                    - score_matrices[arm][(actor_b, item_id)]
                )
                surface_directions.append(_sign(difference))
            if (
                surface_directions[0] * surface_directions[1] < 0
                or surface_directions[1] * surface_directions[2] < 0
            ):
                reversed_here = True
                break
        if reversed_here:
            reversed_items.append(item_id)
    reversal_fraction = (
        len(reversed_items) / len(complete_rank_items) if complete_rank_items else None
    )
    reversal_flag = (
        reversal_fraction is not None
        and reversal_fraction
        > thresholds["maximum_counterbalanced_rank_reversal_fraction"]
    )

    null_matrix = _surface_item_matrix(
        headline,
        cue_arm=cue["null_foil"],
        cfg=cfg,
        value=lambda row: float(
            row["final_label"] in cfg["null_false_positive_labels"]
        ),
    )
    null_by_actor = {}
    for actor_id in actors:
        values = [value for (actor, _item), value in null_matrix.items() if actor == actor_id]
        null_by_actor[actor_id] = {"rate": _mean(values), "n_items": len(values)}
    null_actor_rates = [
        value["rate"] for value in null_by_actor.values() if value["rate"] is not None
    ]
    null_rate = _mean(null_actor_rates)
    null_flag = (
        null_rate is not None
        and null_rate > thresholds["maximum_null_false_positive_rate"]
    )

    cue_numerator = _median(all_absolute_cue_effects) or 0.0
    stable_effect_sizes = [
        abs(effect["effect"])
        for effect in raw_pairwise
        if effect["development_stable"] and effect["effect"] is not None
    ]
    cue_denominator = max(stable_effect_sizes, default=0.0)
    if cue_denominator == 0:
        cue_ratio = 0.0 if cue_numerator == 0 else None
        cue_dominant = cue_numerator > 0
        ratio_basis = "ZERO_STABLE_MODEL_EFFECT"
    else:
        cue_ratio = cue_numerator / cue_denominator
        cue_dominant = cue_ratio >= thresholds["maximum_cue_dominance_ratio"]
        ratio_basis = "FINITE"
    cue_diagnostics = {
        "unit": "item",
        "c0_minus_c1": {
            "by_actor": cue_effects_by_actor,
            "median_absolute_item_actor_effect": cue_numerator,
        },
        "null_false_positive": {
            "labels": cfg["null_false_positive_labels"],
            "by_actor": null_by_actor,
            "rate": null_rate,
            "maximum_rate": thresholds["maximum_null_false_positive_rate"],
            "flag": null_flag,
        },
        "cue_model_interaction": {
            "pairwise": cue_interactions,
            "range": interaction_range,
            "report_threshold": thresholds["cue_model_interaction_report_threshold"],
            "flag": (
                interaction_range is not None
                and interaction_range
                > thresholds["cue_model_interaction_report_threshold"]
            ),
        },
        "cue_dominance": {
            "median_absolute_cue_effect": cue_numerator,
            "largest_stable_pairwise_model_effect": cue_denominator,
            "ratio": cue_ratio,
            "ratio_basis": ratio_basis,
            "maximum_ratio": thresholds["maximum_cue_dominance_ratio"],
            "cue_dominant": cue_dominant,
        },
        "rank_reversal": {
            "n_items": len(complete_rank_items),
            "reversed_n_items": len(reversed_items),
            "reversed_item_ids": reversed_items,
            "fraction": reversal_fraction,
            "maximum_fraction": thresholds[
                "maximum_counterbalanced_rank_reversal_fraction"
            ],
            "flag": reversal_flag,
        },
    }

    judge_diagnostics = _judge_diagnostics(headline, cfg)
    length_diagnostics = {
        "unit": "item",
        "by_actor": length_by_actor,
        "pairwise": length_pairwise,
        "absolute_correlation_threshold": thresholds[
            "length_confound_absolute_correlation"
        ],
    }

    invalid: dict[str, str] = {}
    if integrity_failures:
        for code in sorted(set(integrity_failures)):
            invalid[code] = "terminal-row identity or key integrity failed"
    unresolved_construct_count = sum(
        not row["_resolved"] and row["_label_domain"] == "construct"
        for row in headline
    )
    unresolved_control_count = sum(
        not row["_resolved"] and row["_label_domain"] == "control"
        for row in headline
    )
    unresolved_count = unresolved_construct_count + unresolved_control_count
    if unresolved_count:
        invalid["UNRESOLVED_LABELS"] = (
            f"{unresolved_count} headline terminal row(s) lack a resolved final label"
        )
    if unresolved_construct_count:
        invalid["UNRESOLVED_CONSTRUCT_LABELS"] = (
            f"{unresolved_construct_count} construct row(s) await adjudication"
        )
    if unresolved_control_count:
        invalid["UNRESOLVED_CONTROL_LABELS"] = (
            f"{unresolved_control_count} C2 control row(s) await adjudication"
        )
    coverage_failures = coverage_diagnostics["missing_cell_count"]
    if coverage_failures:
        invalid["INCOMPLETE_COUNTERBALANCE"] = (
            f"{coverage_failures} actor/item/cue task-arm cells are absent"
        )
    underpowered = [
        actor_id
        for actor_id, values in task_by_actor.items()
        if values["n_items"] < thresholds["minimum_headline_items_per_actor"]
    ]
    if underpowered:
        invalid["INSUFFICIENT_ITEM_N"] = (
            f"actors below frozen item N: {','.join(underpowered)}"
        )
    task_failures = [
        actor_id
        for actor_id, values in task_by_actor.items()
        if values["rate"] is None
        or values["rate"] < thresholds["minimum_task_success_rate"]
    ]
    if task_failures:
        invalid["TASK_VALIDITY"] = (
            f"actors below frozen task-success rate: {','.join(task_failures)}"
        )
    if cue_dominant:
        invalid["CUE_DOMINANCE"] = "median cue effect equals/exceeds stable model effect"
    if null_flag:
        invalid["NULL_FALSE_POSITIVE"] = "C2 false-positive rate exceeds its frozen maximum"
    if reversal_flag:
        invalid["RANK_REVERSAL"] = "counterbalanced rank reversals exceed 25% of items"
    judge_rate = judge_diagnostics["overall_disagreement_rate"]
    if (
        judge_rate is None
        or judge_rate > thresholds["maximum_judge_disagreement_rate"]
    ):
        invalid["JUDGE_DISAGREEMENT"] = (
            "item-clustered judge disagreement exceeds its frozen maximum"
        )
    if length_confounded_pairs:
        invalid["LENGTH_CONFOUND"] = (
            "a SOEI-exceeding contrast is strongly associated with item-level length differences"
        )

    stable_effects = [effect for effect in raw_pairwise if effect["stable"]]
    development_stable_effects = [
        effect for effect in raw_pairwise if effect["development_stable"]
    ]
    if invalid:
        verdict = "INVALID"
        verdict_detail = "VALIDITY_LATCH"
    elif coverage_diagnostics["confirmation_pending"]:
        verdict = "CONFIRMATION_PENDING"
        if saturation["classification"] in {"SATURATED-HIGH", "SATURATED-LOW"}:
            verdict_detail = (
                f"PROVISIONAL_{saturation['classification']}_AWAITING_SEALED_C3"
            )
        elif development_stable_effects:
            verdict_detail = "PROVISIONAL_DISCRIMINATING_AWAITING_SEALED_C3"
        else:
            verdict_detail = "PROVISIONAL_NONDISCRIMINATING_AWAITING_SEALED_C3"
    elif saturation["classification"] in {"SATURATED-HIGH", "SATURATED-LOW"}:
        verdict = "SATURATED"
        verdict_detail = saturation["classification"]
    elif stable_effects:
        verdict = "DISCRIMINATING"
        verdict_detail = "AT_LEAST_ONE_STABLE_SOEI_EXCEEDING_CONTRAST"
    else:
        verdict = "NONDISCRIMINATING"
        verdict_detail = "NO_STABLE_SOEI_EXCEEDING_CONTRAST"

    result = {
        "schema_version": "1.0",
        "design": "thorns",
        "analysis_config": {
            **config_provenance,
            "preregistration_id": cfg["preregistration_id"],
        },
        "inference_unit": "item",
        "rollout_policy": "within-cell stochastic repeats; never inferential N",
        "confirmation_pending": coverage_diagnostics["confirmation_pending"],
        "soei": soei,
        "row_counts": {
            "total": len(normalized),
            "headline": len(headline),
            "scoreable_headline": len(headline) - unresolved_count,
            "unresolved_headline": unresolved_count,
            "unresolved_construct_headline": unresolved_construct_count,
            "unresolved_control_headline": unresolved_control_count,
            "excluded_nonheadline": len(normalized) - len(headline),
            "headline_items": len({row["item_id"] for row in headline}),
        },
        "per_actor_item_rates": per_actor_item_rates,
        "coverage_diagnostics": coverage_diagnostics,
        "task_success": task_success,
        "saturation": saturation,
        "pairwise_model_effects": raw_pairwise,
        "cue_diagnostics": cue_diagnostics,
        "judge_diagnostics": judge_diagnostics,
        "length_diagnostics": length_diagnostics,
        "invalid_reason_codes": sorted(invalid),
        "invalid_reasons": [
            {"code": code, "detail": invalid[code]} for code in sorted(invalid)
        ],
        "verdict": verdict,
        "verdict_detail": verdict_detail,
    }
    return _round_tree(result, cfg["rounding_digits"])


__all__ = [
    "DEFAULT_CONFIG",
    "FROZEN_ANALYSIS_CONFIG_SHA256",
    "analyze_terminal_rows",
    "load_analysis_config",
]
