"""Exploratory conditional-logit approximation to a Thurstonian profile.

D-18 forbids this estimator from replacing the direct key profile.  It uses
known path keys, fixes comparative-error scale through the logit link, and
identifies the 16 coordinates with ``sum(theta)=0``.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations

import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp

from lib.blocks import build_deep_structures


CLAUSES = tuple(f"C{index}" for index in range(1, 17))
_CLAUSE_INDEX = {clause: index for index, clause in enumerate(CLAUSES)}
_BASIS = np.linalg.qr(np.vstack([np.eye(15), -np.ones((1, 15))]))[0]


def _path_matrix(path_keys, label="path_keys"):
    if type(path_keys) is not dict or len(path_keys) < 2:
        raise ValueError(f"{label} must contain at least two paths")
    path_ids = []
    matrix = []
    for path_id, keys in path_keys.items():
        if type(path_id) is not str or not path_id:
            raise ValueError(f"{label} path IDs must be non-empty strings")
        if type(keys) is not dict or not set(keys) <= set(CLAUSES):
            raise ValueError(f"{label} contains invalid clause keys")
        row = np.zeros(16, dtype=float)
        for clause, value in keys.items():
            if type(value) is not int or value not in {-1, 0, 1}:
                raise ValueError(f"{label} keys must be exact -1, 0, or 1")
            row[_CLAUSE_INDEX[clause]] = value
        path_ids.append(path_id)
        matrix.append(row)
    return path_ids, np.asarray(matrix, dtype=float)


def audit_block_information(blocks, *, min_rank=15, min_pair_coverage=2,
                            min_clause_blocks=10):
    """Audit centered known-key information and explicit pair coverage."""
    if type(blocks) is not list or not blocks:
        raise ValueError("blocks must be a non-empty list")
    for value, label in (
        (min_rank, "min_rank"), (min_pair_coverage, "min_pair_coverage"),
        (min_clause_blocks, "min_clause_blocks"),
    ):
        if type(value) is not int or value < 0:
            raise ValueError(f"{label} must be a nonnegative integer")
    information = np.zeros((16, 16), dtype=float)
    clause_blocks = Counter()
    pair_coverage = Counter()
    structure_ids = set()
    for index, block in enumerate(blocks):
        if type(block) is not dict or "path_keys" not in block:
            raise ValueError(f"block {index} fields differ")
        structure_id = block.get("structure_id", f"block-{index}")
        if type(structure_id) is not str or not structure_id:
            raise ValueError(f"block {index} structure_id differs")
        if structure_id in structure_ids:
            raise ValueError(f"duplicate structure_id: {structure_id}")
        structure_ids.add(structure_id)
        _, matrix = _path_matrix(block["path_keys"], f"block {index} path_keys")
        centered = matrix - np.mean(matrix, axis=0, keepdims=True)
        information += centered.T @ centered
        active = [CLAUSES[column] for column in range(16)
                  if np.any(matrix[:, column] != 0)]
        clause_blocks.update(active)
        pair_coverage.update(tuple(pair) for pair in combinations(active, 2))

    reduced_information = _BASIS.T @ information @ _BASIS
    eigenvalues = np.linalg.eigvalsh(reduced_information)
    positive = eigenvalues[eigenvalues > 1e-10]
    rank = int(np.linalg.matrix_rank(reduced_information, tol=1e-10))
    condition = float(positive[-1] / positive[0]) if len(positive) else None
    all_pairs = list(combinations(CLAUSES, 2))
    minimum_pair = min((pair_coverage[pair] for pair in all_pairs), default=0)
    minimum_clause = min((clause_blocks[clause] for clause in CLAUSES), default=0)
    covariance = _BASIS @ np.linalg.pinv(reduced_information) @ _BASIS.T
    standard_errors = np.sqrt(np.clip(np.diag(covariance), 0, None))
    return {
        "rank": rank,
        "maximum_identifiable_rank": 15,
        "identification_constraint": "sum(theta)=0",
        "condition_number_nonzero": condition,
        "minimum_pair_coverage": int(minimum_pair),
        "minimum_clause_blocks": int(minimum_clause),
        "pair_coverage": {
            f"{left}|{right}": int(pair_coverage[(left, right)])
            for left, right in all_pairs
        },
        "clause_blocks": {
            clause: int(clause_blocks[clause]) for clause in CLAUSES
        },
        "approximate_se": {
            clause: float(standard_errors[index])
            for index, clause in enumerate(CLAUSES)
        },
        "thresholds": {
            "min_rank": min_rank,
            "min_pair_coverage": min_pair_coverage,
            "min_clause_blocks": min_clause_blocks,
        },
        "gate_pass": (
            rank >= min_rank
            and minimum_pair >= min_pair_coverage
            and minimum_clause >= min_clause_blocks
        ),
    }


def within_clause_irt_status(*, n_respondents, n_items,
                             minimum_responses_per_item):
    """Apply the frozen floor before any within-clause IRT is attempted."""
    for value, label in (
        (n_respondents, "n_respondents"), (n_items, "n_items"),
        (minimum_responses_per_item, "minimum_responses_per_item"),
    ):
        if type(value) is not int or value < 0:
            raise ValueError(f"{label} must be a nonnegative integer")
    if n_respondents < 50:
        return {
            "status": "not_estimable",
            "reason": "requires at least 50 independent respondents",
            "exploratory_only": True,
        }
    if n_items < 20:
        return {
            "status": "not_estimable",
            "reason": "requires at least 20 informative items per clause",
            "exploratory_only": True,
        }
    if minimum_responses_per_item < 30:
        return {
            "status": "not_estimable",
            "reason": "requires at least 30 responses per item",
            "exploratory_only": True,
        }
    return {
        "status": "eligible_exploratory",
        "reason": "all preregistered count floors met",
        "exploratory_only": True,
    }


def fit_latent_profile(rows, *, l2=1.0):
    """Fit a sum-zero conditional-logit MAP profile from executed choices."""
    if type(rows) is not list or not rows:
        raise ValueError("latent rows must be a non-empty list")
    if len(rows) < 200:
        raise ValueError("latent fit requires at least 200 rows")
    if type(l2) not in {int, float} or isinstance(l2, bool) or l2 <= 0:
        raise ValueError("l2 must be positive")
    matrices = []
    choices = []
    expected_structures = {
        structure["structure_id"]: structure
        for structure in build_deep_structures()
    }
    structure_counts = Counter()
    representative_blocks = {}
    model_ids = set()
    for index, row in enumerate(rows):
        required = {
            "model_id", "structure_id", "outcome_type", "path_keys",
            "selected_path",
        }
        if type(row) is not dict or not required <= set(row):
            raise ValueError(f"latent row {index} fields differ")
        if type(row["model_id"]) is not str or not row["model_id"]:
            raise ValueError(f"latent row {index} model_id differs")
        model_ids.add(row["model_id"])
        if row["outcome_type"] != "resolved":
            raise ValueError("latent exploratory fit accepts resolved outcomes only")
        structure_id = row["structure_id"]
        if structure_id not in expected_structures:
            raise ValueError("latent fit requires the 40 actual structure IDs")
        expected_clauses = set(expected_structures[structure_id]["clauses"])
        path_keys = row["path_keys"]
        if type(path_keys) is not dict or len(path_keys) != 4:
            raise ValueError(f"latent row {index} requires exactly four paths")
        for keys in path_keys.values():
            if type(keys) is not dict or set(keys) != expected_clauses:
                raise ValueError(
                    f"latent row {index} keys differ from actual structure coverage"
                )
            if Counter(keys.values()) != Counter({1: 2, -1: 2}):
                raise ValueError(
                    f"latent row {index} path keys must balance two plus/two minus"
                )
        for clause in expected_clauses:
            if Counter(keys[clause] for keys in path_keys.values()) != Counter({1: 2, -1: 2}):
                raise ValueError(
                    f"latent row {index} clause keys must balance two plus/two minus"
                )
        path_ids, matrix = _path_matrix(row["path_keys"], f"latent row {index}")
        if row["selected_path"] not in path_ids:
            raise ValueError(f"latent row {index} selected_path differs")
        matrices.append(matrix)
        choices.append(path_ids.index(row["selected_path"]))
        structure_counts[structure_id] += 1
        representative_blocks.setdefault(structure_id, {
            "structure_id": structure_id, "path_keys": row["path_keys"],
        })

    if len(model_ids) != 1:
        raise ValueError("latent fit requires exactly one model_id; pooling is forbidden")
    if set(structure_counts) != set(expected_structures):
        raise ValueError("latent fit requires complete expected coverage of all 40 structures")
    if min(structure_counts.values()) < 5:
        raise ValueError("latent fit requires at least five rows per actual structure")
    information = audit_block_information(
        [representative_blocks[key] for key in sorted(representative_blocks)],
        min_rank=15, min_pair_coverage=2, min_clause_blocks=10,
    )
    if not information["gate_pass"]:
        raise ValueError("latent fit block-information gate failed")

    def objective(beta):
        theta = _BASIS @ beta
        loss = 0.5 * float(l2) * float(theta @ theta)
        gradient_theta = float(l2) * theta
        for matrix, chosen in zip(matrices, choices):
            utility = matrix @ theta
            loss += float(logsumexp(utility) - utility[chosen])
            probabilities = np.exp(utility - logsumexp(utility))
            probabilities[chosen] -= 1.0
            gradient_theta += matrix.T @ probabilities
        return loss, _BASIS.T @ gradient_theta

    result = minimize(
        objective,
        np.zeros(15, dtype=float),
        method="L-BFGS-B",
        jac=True,
        options={"maxiter": 1000, "ftol": 1e-12, "gtol": 1e-8},
    )
    theta = _BASIS @ result.x
    theta -= np.mean(theta)
    return {
        "theta": {clause: float(theta[index])
                  for index, clause in enumerate(CLAUSES)},
        "converged": bool(result.success),
        "optimizer_message": str(result.message),
        "objective": float(result.fun),
        "iterations": int(result.nit),
        "l2": float(l2),
        "information_rank": information["rank"],
        "model_id": next(iter(model_ids)),
        "n_rows": len(rows),
        "n_structures": len(structure_counts),
        "status": "estimable_exploratory",
        "identification_constraint": "sum(theta)=0",
        "estimator": "conditional-logit MAP approximation to Thurstonian choice",
        "exploratory_only": True,
    }
