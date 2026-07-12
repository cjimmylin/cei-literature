"""Known-theta recovery gate for the exploratory latent estimator."""
from __future__ import annotations

import numpy as np
from scipy.special import softmax

from analysis.latent_profile import CLAUSES, audit_block_information, fit_latent_profile
from lib.blocks import build_deep_structures


PROVENANCE = "harness validation, NOT a measurement"
THRESHOLDS = {
    "minimum_theta_correlation": 0.90,
    "maximum_theta_rmse": 0.30,
    "minimum_information_rank": 15,
}


def _simulate(seed, repeats_per_structure):
    if type(seed) is not int:
        raise ValueError("seed must be an integer")
    if type(repeats_per_structure) is not int or repeats_per_structure < 15:
        raise ValueError("repeats_per_structure must be an integer of at least 15")
    rng = np.random.default_rng(seed)
    planted = np.linspace(-1.0, 1.0, 16)
    planted -= np.mean(planted)
    rows = []
    blocks = build_deep_structures()
    for structure in blocks:
        path_keys = {
            path["path_id"]: dict(path["clause_keys"])
            for path in structure["base_paths"]
        }
        matrix = np.zeros((4, 16), dtype=float)
        for path_index, path in enumerate(structure["base_paths"]):
            for clause, value in path["clause_keys"].items():
                matrix[path_index, int(clause.removeprefix("C")) - 1] = value
        probabilities = softmax(matrix @ planted)
        for _ in range(repeats_per_structure):
            selected = int(rng.choice(4, p=probabilities))
            rows.append({
                "model_id": "synthetic-known-theta",
                "structure_id": structure["structure_id"],
                "outcome_type": "resolved",
                "path_keys": path_keys,
                "selected_path": f"path-{selected}",
            })
    # Construct separately to retain the frozen 40 structure IDs exactly once.
    audit_blocks = [{
        "structure_id": structure["structure_id"],
        "path_keys": {
            path["path_id"]: dict(path["clause_keys"])
            for path in structure["base_paths"]
        },
    } for structure in build_deep_structures()]
    return rows, audit_blocks, planted


def run_recovery(*, seed=20260711, repeats_per_structure=15):
    """Recover a planted profile and emit the build-blocking verdict."""
    rows, blocks, planted = _simulate(seed, repeats_per_structure)
    audit = audit_block_information(
        blocks, min_rank=15, min_pair_coverage=2, min_clause_blocks=10,
    )
    fitted = fit_latent_profile(rows, l2=1.0)
    estimated = np.asarray([fitted["theta"][clause] for clause in CLAUSES])
    correlation = float(np.corrcoef(planted, estimated)[0, 1])
    rmse = float(np.sqrt(np.mean((planted - estimated) ** 2)))
    passed = (
        fitted["converged"]
        and audit["rank"] >= THRESHOLDS["minimum_information_rank"]
        and correlation >= THRESHOLDS["minimum_theta_correlation"]
        and rmse <= THRESHOLDS["maximum_theta_rmse"]
    )
    return {
        "provenance": PROVENANCE,
        "n_rows": len(rows),
        "actual_structure_count": len(blocks),
        "repeats_per_structure": repeats_per_structure,
        "design_source": "lib.blocks.build_deep_structures",
        "seed": seed,
        "thresholds": dict(THRESHOLDS),
        "information_rank": audit["rank"],
        "theta_correlation": correlation,
        "theta_rmse": rmse,
        "optimizer_converged": fitted["converged"],
        "planted_theta": {
            clause: float(planted[index]) for index, clause in enumerate(CLAUSES)
        },
        "estimated_theta": dict(fitted["theta"]),
        "build_gate_pass": bool(passed),
    }
