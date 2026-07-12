"""Frozen affine-plane block construction for CROSSROADS."""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import hashlib
from itertools import combinations

from .registry import CLAUSES, CLAUSE_REGISTRY
from .scenarios import SCENARIO_CATALOG, claim_records


DEFAULT_SCENARIO_SEED = "crossroads-causal-v2"


GF4_BLOCKS = (
    (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15),
    (4, 8, 12, 16), (1, 6, 11, 16), (2, 5, 12, 15),
    (3, 8, 9, 14), (4, 7, 10, 13), (1, 7, 12, 14),
    (2, 8, 11, 13), (3, 5, 10, 16), (4, 6, 9, 15),
    (1, 8, 10, 15), (2, 7, 9, 16), (3, 6, 12, 13),
    (4, 5, 11, 14), (1, 2, 3, 4), (5, 6, 7, 8),
    (9, 10, 11, 12), (13, 14, 15, 16),
)

_BALANCED_PATTERN_FAMILIES = (
    (
        (1, 1, -1, -1),
        (1, -1, 1, -1),
        (-1, 1, -1, 1),
        (-1, -1, 1, 1),
    ),
    (
        (1, 1, -1, -1),
        (1, -1, -1, 1),
        (-1, 1, 1, -1),
        (-1, -1, 1, 1),
    ),
)


def validate_base_blocks(source=GF4_BLOCKS) -> dict:
    """Fail loudly unless *source* is the exact 2-(16,4,1) affine design."""
    if tuple(source) != GF4_BLOCKS:
        raise ValueError("GF(4) block list differs from the frozen construction")
    if len(source) != 20 or any(len(block) != 4 for block in source):
        raise ValueError("GF(4) design must contain twenty four-point blocks")
    if any(len(set(block)) != 4 or not set(block) <= set(range(1, 17))
           for block in source):
        raise ValueError("GF(4) block points must be distinct integers 1..16")
    clause_frequency = Counter(point for block in source for point in block)
    pair_frequency = Counter(
        pair for block in source for pair in combinations(sorted(block), 2)
    )
    if clause_frequency != Counter({point: 5 for point in range(1, 17)}):
        raise ValueError("each point must occur in exactly five affine lines")
    if len(pair_frequency) != 120 or set(pair_frequency.values()) != {1}:
        raise ValueError("each unordered point pair must occur exactly once")
    return {
        "blocks": 20,
        "block_size": 4,
        "clause_frequency": {f"C{point}": 5 for point in range(1, 17)},
        "pair_frequency": 1,
        "pair_count": 120,
    }


def _oriented_clauses(block, orientation: int):
    clauses = tuple(f"C{point}" for point in block)
    if orientation == 0:
        return clauses
    if orientation == 1:
        return (clauses[2], clauses[3], clauses[0], clauses[1])
    raise ValueError("orientation must be zero or one")


def _base_paths(clauses, orientation: int, scenario: dict):
    patterns = _BALANCED_PATTERN_FAMILIES[orientation]
    base_requirement = dict(zip(clauses, patterns[0]))
    rows = []
    plans = {row["path_id"]: row for row in scenario["action_plans"]}
    for index, pattern in enumerate(patterns):
        path_id = f"path-{index}"
        rows.append({
            "path_id": path_id,
            "clause_keys": dict(zip(clauses, pattern)),
            "action_states": {
                clause: state * base_requirement[clause]
                for clause, state in zip(clauses, pattern)
            },
            "stable_plan": deepcopy(plans[path_id]),
            "action_cost": plans[path_id]["causal_commitment"],
        })
    return rows


def fifth_requirement_phase(block_index: int) -> int:
    """Derive the fifth private mask from the affine-line band.

    Four consecutive affine lines share a phase.  Across both orientations this
    makes every clause's extra required state exactly balanced, while every
    fixed causal action role has at most two extra signed cells per clause.
    """
    if block_index not in range(1, 21):
        raise ValueError("affine block index must be 1..20")
    return ((block_index - 1) // 4) % 4


def _scenario_order(seed: str) -> list[dict]:
    if not isinstance(seed, str) or not seed.strip():
        raise ValueError("scenario seed must be non-empty text")
    return sorted(
        (deepcopy(row) for row in SCENARIO_CATALOG),
        key=lambda row: hashlib.sha256(
            f"{seed}\x00{row['scenario_id']}".encode("utf-8")
        ).digest(),
    )


def build_deep_structures(seed: str = DEFAULT_SCENARIO_SEED) -> list:
    """Return the duplicated, independently oriented 2-(16,4,2) design."""
    validate_base_blocks()
    scenarios = _scenario_order(seed)
    structures = []
    for orientation in range(2):
        for block_index, block in enumerate(GF4_BLOCKS, 1):
            clauses = _oriented_clauses(block, orientation)
            structure_number = orientation * 20 + block_index
            scenario = scenarios[structure_number - 1]
            fifth_phase = fifth_requirement_phase(block_index)
            active_claims = claim_records(scenario, list(clauses))
            rows = {
                "structure_id": f"XR-DS-{structure_number:03d}",
                "affine_line": block_index,
                "orientation": orientation,
                "scenario_id": scenario["scenario_id"],
                "template_family": scenario["template_family"],
                "scenario": scenario,
                "clauses": list(clauses),
                "competing_claims": [
                    {
                        **claim,
                        "expert_construct": CLAUSE_REGISTRY[claim["clause"]][
                            "fork_family"
                        ],
                    }
                    for claim in active_claims
                ],
                "base_paths": _base_paths(clauses, orientation, scenario),
                "requirement_states": [
                    dict(zip(clauses, pattern))
                    for pattern in _BALANCED_PATTERN_FAMILIES[orientation]
                ] + [
                    dict(zip(
                        clauses,
                        _BALANCED_PATTERN_FAMILIES[orientation][fifth_phase],
                    )),
                    {
                        clause: -state
                        for clause, state in zip(
                            clauses, _BALANCED_PATTERN_FAMILIES[orientation][2]
                        )
                    },
                ],
                "fifth_requirement_phase": fifth_phase,
                "inaction_cost": scenario["loss"],
            }
            structures.append(rows)
    _validate_duplicated_design(structures)
    return structures


def _validate_duplicated_design(structures) -> None:
    if len(structures) != 40:
        raise AssertionError("deep-structure count must be exactly 40")
    clause_frequency = Counter()
    pair_frequency = Counter()
    scenario_signatures = set()
    for structure in structures:
        clauses = structure["clauses"]
        clause_frequency.update(clauses)
        pair_frequency.update(combinations(sorted(clauses), 2))
        paths = structure["base_paths"]
        if len(paths) != 4:
            raise AssertionError("every structure must expose four paths")
        for path in paths:
            if path["stable_plan"]["path_id"] != path["path_id"]:
                raise AssertionError("stable plan and affine path IDs differ")
            if Counter(path["clause_keys"].values()) != Counter({1: 2, -1: 2}):
                raise AssertionError("every path must have exactly two plus and two minus keys")
            if set(path["action_states"]) != set(clauses) or set(
                    path["action_states"].values()) - {-1, 1}:
                raise AssertionError("action-state matrix must be binary and complete")
        for clause in clauses:
            signs = Counter(path["clause_keys"][clause] for path in paths)
            if signs != Counter({1: 2, -1: 2}):
                raise AssertionError("each clause must be plus/minus balanced within a structure")
        scenario = structure["scenario"]
        requirements = structure["requirement_states"]
        if len(requirements) != 6 or any(
                set(row) != set(clauses) or Counter(row.values()) != Counter({1: 2, -1: 2})
                for row in requirements):
            raise AssertionError("every parameter needs a balanced required-state vector")
        for requirement in requirements:
            derived = {
                path["path_id"]: {
                    clause: 1 if path["action_states"][clause] == requirement[clause] else -1
                    for clause in clauses
                }
                for path in paths
            }
            if any(Counter(vector.values()) != Counter({1: 2, -1: 2})
                   for vector in derived.values()):
                raise AssertionError("relational keys must be 2+/2- for every path")
            if any(Counter(vector[clause] for vector in derived.values()) != Counter({1: 2, -1: 2})
                   for clause in clauses):
                raise AssertionError("relational keys must be 2+/2- for every claim")
        if structure["scenario_id"] != scenario["scenario_id"] or (
                structure["template_family"] != scenario["template_family"]):
            raise AssertionError("structure scenario crosswalk changed")
        if [row["clause"] for row in structure["competing_claims"]] != clauses:
            raise AssertionError("active claims must preserve oriented clause order")
        signature = (
            scenario["template_family"], scenario["domain"],
            tuple(sorted(scenario["roles"].items())), scenario["artifact"],
            scenario["incident"], scenario["evidence_state"],
            scenario["deadline"], scenario["baseline_duty"],
            tuple(row["visible_claim"] for row in structure["competing_claims"]),
            tuple((row["path_id"], row["plan"], row["causal_commitment"])
                  for row in scenario["action_plans"]),
        )
        if signature in scenario_signatures:
            raise AssertionError("deep structures must have distinct causal skeletons")
        scenario_signatures.add(signature)
    if clause_frequency != Counter({clause: 10 for clause in CLAUSES}):
        raise AssertionError("each clause must occur in exactly ten structures")
    if len(pair_frequency) != 120 or set(pair_frequency.values()) != {2}:
        raise AssertionError("each unordered clause pair must occur exactly twice")
    if len(scenario_signatures) != 40:
        raise AssertionError("all forty deep structures need distinct causal signatures")
