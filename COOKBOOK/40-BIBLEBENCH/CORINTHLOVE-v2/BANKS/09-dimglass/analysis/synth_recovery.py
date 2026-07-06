"""Synthetic-data generator with PLANTED dose-response parameters.

Used by tests/test_synth_recovery.py to assert the analysis recovers the planted
beta0 (sycophancy), beta1 (elasticity), ceiling (d4/d5 saturation, D-16), and the
d2-d3 matched-pair discernment differential within tolerance BEFORE any real
pilot. This is the analysis-side analogue of the scorer fixtures.

NOTE: purely synthetic. Any number produced here is 'harness validation, NOT a
measurement.'
"""
from __future__ import annotations

import numpy as np

DOSE_ORD = {"d0": 0, "d1": 1, "d2": 2, "d3": 3, "d4": 4, "d5": 5}


def simulate(seed=20260706, n_items=120, reps=6,
             beta0=0.30, beta1=0.45, ceiling=-0.40, discernment=0.80,
             noise_sd=0.30):
    """Return (valid_arm_rows, matched_pairs, planted).

    valid_arm_rows: list of dict(dose, update, item, domain) for VALID evidence.
    matched_pairs : list of (valid_update, invalid_update) at d2-d3.

    Model for a VALID observation at dose level t:
        update = beta0 + beta1*t + ceiling*[t>=4] + item_effect + noise
    At d2-d3, the INVALID twin has the SAME surface (same t) but lacks genuine
    evidence, so its update = beta0 + beta1_social*t' + item_effect + noise,
    where beta1_social is a small pure-surface slope; the planted differential
    (valid - invalid) at d2-d3 equals `discernment`.
    """
    rng = np.random.default_rng(seed)
    item_effects = rng.normal(0, 0.20, size=n_items)
    valid_rows = []
    matched = []
    for it in range(n_items):
        ie = item_effects[it]
        # valid arm across all doses
        for dose, t in DOSE_ORD.items():
            for _ in range(reps):
                u = beta0 + beta1 * t + (ceiling if t >= 4 else 0.0) + ie \
                    + rng.normal(0, noise_sd)
                u = float(np.clip(u, 0, 3))
                valid_rows.append({"dose": dose, "update": u, "item": f"it{it}",
                                   "domain": f"dom{it % 5}"})
        # matched d2-d3 pairs: valid and invalid twins share the item base but
        # carry INDEPENDENT response noise (as real responses would), so the
        # paired difference has mean == discernment with a non-degenerate CI.
        for dose in ("d2", "d3"):
            t = DOSE_ORD[dose]
            for _ in range(reps):
                base = beta0 + beta1 * t + ie
                v = float(np.clip(base + discernment / 2 + rng.normal(0, noise_sd), 0, 3))
                inv = float(np.clip(base - discernment / 2 + rng.normal(0, noise_sd), 0, 3))
                matched.append((v, inv))
    planted = {"beta0": beta0, "beta1": beta1, "ceiling": ceiling,
               "discernment": discernment}
    return valid_rows, matched, planted
