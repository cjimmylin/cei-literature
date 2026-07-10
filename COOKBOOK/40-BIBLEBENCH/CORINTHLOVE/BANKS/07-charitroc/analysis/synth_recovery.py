"""Planted synthetic recovery fixtures.

Every result from this module is **harness validation, NOT a measurement**.
"""
from __future__ import annotations

import numpy as np


MALICIOUS_PROBS = np.asarray([0.40, 0.30, 0.15, 0.10, 0.05])
BENIGN_PROBS = np.asarray([0.05, 0.10, 0.15, 0.30, 0.40])


def _theoretical_ordinal_auc() -> float:
    total = 0.0
    malicious_below = 0.0
    for score in range(5):
        total += BENIGN_PROBS[score] * (
            malicious_below + 0.5 * MALICIOUS_PROBS[score]
        )
        malicious_below += MALICIOUS_PROBS[score]
    return float(total)


def simulate_ordinal(seed: int = 20260709, n_per_type: int = 4000):
    """Sample paired ordinal scores from distributions with an exact planted AUC."""
    if n_per_type < 10:
        raise ValueError("n_per_type must be at least 10")
    rng = np.random.default_rng(seed)
    malicious = rng.choice(5, size=n_per_type, p=MALICIOUS_PROBS)
    benign = rng.choice(5, size=n_per_type, p=BENIGN_PROBS)
    rows = []
    for index, score in enumerate(malicious):
        rows.append({"label": 0, "score": int(score),
                     "pair_id": f"synthetic-{index:05d}"})
    for index, score in enumerate(benign):
        rows.append({"label": 1, "score": int(score),
                     "pair_id": f"synthetic-{index:05d}"})
    return rows, {
        "auc": _theoretical_ordinal_auc(),
        "provenance": "harness validation, NOT a measurement",
    }


def simulate_stage3(seed: int = 23, n: int = 2000, accuracy: float = 0.76):
    """Plant a separate Bernoulli stage-3 accuracy channel."""
    if not 0.0 <= accuracy <= 1.0:
        raise ValueError("accuracy must be in [0, 1]")
    rng = np.random.default_rng(seed)
    outcomes = rng.random(n) < accuracy
    cues = ("strong", "weak", "absent", "adversarial")
    records = [
        {"update_correct": bool(outcome), "cue_variant": cues[index % len(cues)]}
        for index, outcome in enumerate(outcomes)
    ]
    return records, {
        "stage3_accuracy": accuracy,
        "provenance": "harness validation, NOT a measurement",
    }
