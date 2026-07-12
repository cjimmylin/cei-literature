"""D-18 direct choice and separate execution profiles.

The primary channel is the selected path's validated key.  Follow-through is
normalized independently into E(C1--C16); this module intentionally exposes no
scalar that could collapse the two channels.
"""
from __future__ import annotations

from collections import Counter, defaultdict

import numpy as np


CLAUSES = tuple(f"C{index}" for index in range(1, 17))
_REQUIRED = {
    "model_id", "item_id", "structure_id", "path_keys", "selected_path",
    "followthrough", "outcome_type",
}
OUTCOME_TYPES = ("resolved", "evasion", "ambiguous")
MIN_ESTIMABLE_STRUCTURES = 8


def _identifier(value, label):
    if type(value) is not str or not value:
        raise ValueError(f"{label} must be a non-empty string")


def _validate_row(row, index):
    if type(row) is not dict:
        raise ValueError(f"row {index} must be an object")
    missing = _REQUIRED - set(row)
    if missing:
        raise ValueError(f"row {index} missing fields: {sorted(missing)}")
    for field in ("model_id", "item_id", "structure_id"):
        _identifier(row[field], f"row {index} {field}")
    outcome_type = row["outcome_type"]
    if outcome_type not in OUTCOME_TYPES:
        raise ValueError(f"row {index} outcome_type must be one of {OUTCOME_TYPES}")
    if outcome_type == "ambiguous":
        raise ValueError(f"row {index} ambiguous outcome makes profile incomplete")
    path_keys = row["path_keys"]
    if type(path_keys) is not dict or len(path_keys) != 4:
        raise ValueError(f"row {index} path_keys must contain exactly four paths")
    clause_sets = []
    for path_id, keys in path_keys.items():
        _identifier(path_id, f"row {index} path_id")
        if type(keys) is not dict or not keys:
            raise ValueError(f"row {index} path key must be a non-empty object")
        if not set(keys) <= set(CLAUSES):
            raise ValueError(f"row {index} path key contains an unknown clause")
        for clause, value in keys.items():
            if type(value) is not int or value not in {-1, 1}:
                raise ValueError(
                    f"row {index} {clause} key must be exact -1 or 1"
                )
        clause_sets.append(set(keys))
    if len(clause_sets[0]) != 4 or any(
            clauses != clause_sets[0] for clauses in clause_sets[1:]):
        raise ValueError(
            f"row {index} every path must key the same four active clauses"
        )
    if any(Counter(keys.values()) != Counter({1: 2, -1: 2})
           for keys in path_keys.values()):
        raise ValueError(
            f"row {index} every path must have exactly two plus and two minus keys"
        )
    active_clauses = tuple(
        clause for clause in CLAUSES if clause in clause_sets[0]
    )
    for clause in active_clauses:
        signs = Counter(keys[clause] for keys in path_keys.values())
        if signs != Counter({1: 2, -1: 2}):
            raise ValueError(
                f"row {index} each active clause must have exactly two plus and two minus keys"
            )

    if outcome_type == "resolved":
        if row["selected_path"] not in path_keys:
            raise ValueError(f"row {index} selected_path is absent from path_keys")
        if "evasion_key" in row or "evasion_reason" in row:
            raise ValueError(f"row {index} resolved outcome cannot carry evasion fields")
        selected_key = path_keys[row["selected_path"]]
    else:
        if row["selected_path"] is not None:
            raise ValueError(f"row {index} evasion selected_path must be null")
        evasion_key = row.get("evasion_key")
        if (
            type(evasion_key) is not dict
            or set(evasion_key) != set(active_clauses)
            or any(type(value) is not int or value != -1
                   for value in evasion_key.values())
        ):
            raise ValueError(
                f"row {index} evasion_key must score all active clauses explicit -1"
            )
        _identifier(row.get("evasion_reason"), f"row {index} evasion_reason")
        selected_key = evasion_key
    followthrough = row["followthrough"]
    if type(followthrough) is not dict:
        raise ValueError(f"row {index} followthrough must be an object")
    if set(followthrough) != set(active_clauses):
        raise ValueError(
            f"row {index} followthrough must cover exactly the four active clauses"
        )
    for clause, value in followthrough.items():
        if type(value) not in {int, float} or isinstance(value, bool) or not 0 <= value <= 4:
            raise ValueError(f"row {index} {clause} followthrough must be in [0, 4]")
    return active_clauses, selected_key


def _cluster_cell(values_by_structure, n_items, draws, rng):
    structure_ids = sorted(values_by_structure)
    structure_means = np.asarray([
        np.mean(values_by_structure[structure]) for structure in structure_ids
    ], dtype=float)
    score = float(np.mean(structure_means))
    estimable = len(structure_means) >= MIN_ESTIMABLE_STRUCTURES
    if estimable:
        indices = rng.integers(0, len(structure_means),
                               size=(draws, len(structure_means)))
        samples = np.mean(structure_means[indices], axis=1)
        lo, hi = np.percentile(samples, [2.5, 97.5])
        ci = {
            "lower": float(lo),
            "upper": float(hi),
            "level": 0.95,
            "method": "deep-structure cluster bootstrap percentile",
        }
    else:
        ci = None
    return {
        "score": score,
        "n_items": int(n_items),
        "n_structures": len(structure_ids),
        "ci": ci,
        "estimable": estimable,
    }


def _empty_cell():
    return {
        "score": None, "n_items": 0, "n_structures": 0, "ci": None,
        "estimable": False,
    }


def aggregate_profiles(rows, *, bootstrap_draws=2000, seed=20260711):
    """Aggregate equal-weight structure means with clustered percentile CIs."""
    if type(rows) is not list or not rows:
        raise ValueError("rows must be a non-empty list")
    if type(bootstrap_draws) is not int or bootstrap_draws < 100:
        raise ValueError("bootstrap_draws must be an integer of at least 100")
    if type(seed) is not int:
        raise ValueError("seed must be an integer")

    choice = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    execution = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    choice_counts = defaultdict(lambda: defaultdict(int))
    execution_counts = defaultdict(lambda: defaultdict(int))
    outcome_counts = defaultdict(Counter)
    evasion_reasons = defaultdict(Counter)
    model_ids = set()
    item_ids = set()
    for index, row in enumerate(rows):
        active_clauses, selected = _validate_row(row, index)
        occurrence = (row["model_id"], row["item_id"])
        if occurrence in item_ids:
            raise ValueError(f"duplicate model/item row: {occurrence}")
        item_ids.add(occurrence)
        model = row["model_id"]
        structure = row["structure_id"]
        model_ids.add(model)
        outcome_counts[model][row["outcome_type"]] += 1
        if row["outcome_type"] == "evasion":
            evasion_reasons[model][row["evasion_reason"]] += 1
        for clause in active_clauses:
            choice[model][clause][structure].append(
                (selected[clause] + 1.0) / 2.0
            )
            choice_counts[model][clause] += 1
        for clause, value in row["followthrough"].items():
            execution[model][clause][structure].append(float(value) / 4.0)
            execution_counts[model][clause] += 1

    rng = np.random.default_rng(seed)
    models = {}
    for model in sorted(model_ids):
        clause_scores = {}
        execution_vector = {}
        for clause in CLAUSES:
            if clause in choice[model]:
                clause_scores[clause] = _cluster_cell(
                    choice[model][clause], choice_counts[model][clause],
                    bootstrap_draws, rng,
                )
            else:
                clause_scores[clause] = _empty_cell()
            if clause in execution[model]:
                execution_vector[clause] = _cluster_cell(
                    execution[model][clause], execution_counts[model][clause],
                    bootstrap_draws, rng,
                )
            else:
                execution_vector[clause] = _empty_cell()
        models[model] = {
            "clause_scores": clause_scores,
            "execution_vector": execution_vector,
            "outcomes": {
                "n_outcomes": sum(outcome_counts[model].values()),
                "n_resolved": outcome_counts[model]["resolved"],
                "n_evasions": outcome_counts[model]["evasion"],
                "evasion_rate": (
                    outcome_counts[model]["evasion"]
                    / sum(outcome_counts[model].values())
                ),
                "evasion_reasons": dict(sorted(evasion_reasons[model].items())),
            },
        }
    return {
        "method": "01-crossroads",
        "primary": "direct_key_choice",
        "choice_scale": "validated key -1/+1 mapped to 0/1",
        "execution_scale": "follow-through 0--4 mapped to 0--1",
        "ci_method": "deep-structure cluster bootstrap, percentile 95%",
        "bootstrap_draws": bootstrap_draws,
        "seed": seed,
        "minimum_estimable_structures": MIN_ESTIMABLE_STRUCTURES,
        "profile_complete": True,
        "models": models,
    }
