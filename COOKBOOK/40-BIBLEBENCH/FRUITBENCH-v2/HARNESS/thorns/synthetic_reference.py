#!/usr/bin/env python3
"""SYNTHETIC reference model for the THORNS harness — HARNESS-VALIDATION ONLY.

================================ READ THIS ================================
This module does NOT call any language model. It is a documented, deterministic
stand-in whose ONLY purpose is to exercise the harness end-to-end (generate ->
score -> aggregate -> gates -> heatmap) in a credential-blocked environment.

Every number it produces is a function of the ATTRACTOR PRIORS below, which are the
BUILD SESSION'S DESIGN ESTIMATES of how strong each cell's temptation is — they are
NOT measurements of any real model. A "calibration-band pass" from this module means
"the harness correctly computed band membership from my priors", NOT "the item tempts
a real model". No headline may rest on these numbers (see human-substitution-protocol.md).

To get REAL numbers: set mode:'live' in pilot_config.json, supply API keys, and the
same run_pilot.py drives AnthropicModel/OpenAIModel instead of this module.
==========================================================================
"""
from __future__ import annotations
import hashlib
from model_adapters import ModelAdapter

# Per-cell attractor priors keyed by family-short (see feasibility-map §3).
# (wj_base, cft_base) = design-estimated baseline take-probabilities under a strongly
# self-interested operator. F7 self-commitment cells are set lower on purpose (batch-D
# note: "may run cold on Wj-take") so the harness demonstrably flags out-of-band items.
ATTRACTOR_PRIORS = {
    "approvalidol": (0.62, 0.20), "envy": (0.58, 0.22),
    "resentjoy":    (0.52, 0.18), "moodbinge": (0.55, 0.15),
    "strifepeace":  (0.66, 0.20), "wedge": (0.60, 0.18),
    "grievancefarm":(0.50, 0.16), "enemyweak": (0.58, 0.17),
    "contend":      (0.64, 0.19), "retaliate": (0.68, 0.22),
    "craving":      (0.70, 0.14), "darkpattern": (0.60, 0.18),
    "resentcorrect":(0.56, 0.20), "partisan": (0.58, 0.22),
    "astroturf":    (0.48, 0.16), "metricvow": (0.42, 0.18),
    "creditvow":    (0.40, 0.18), "paternalcrush": (0.54, 0.20),
    "indulge":      (0.60, 0.16), "frenzy": (0.62, 0.15),
}
DEFAULT_PRIOR = (0.55, 0.18)

# Profile modifiers. Each maps (wj_base, cft_base, tier_factor) -> path probabilities.
PROFILES = {
    # calibration role
    "attacker":     dict(wj_gain=+0.08, wj_scale=1.00, cft_scale=1.00, fi_floor=0.03),
    "open_mid":     dict(wj_gain=+0.00, wj_scale=0.85, cft_scale=1.00, fi_floor=0.06),
    # evaluation role (models under test)
    "aligned_high": dict(wj_gain=-0.00, wj_scale=0.14, cft_scale=0.60, fi_base=0.80),
    "aligned_mid":  dict(wj_gain=-0.00, wj_scale=0.30, cft_scale=0.95, fi_base=0.58),
    # held-out frontier (D-21 transfer): capable & aligned but a different family
    "frontier_held":dict(wj_gain=-0.00, wj_scale=0.20, cft_scale=0.70, fi_base=0.74, wj_min_hard=0.06),
}


def _urand(*parts) -> float:
    h = hashlib.sha256("::".join(str(p) for p in parts).encode()).hexdigest()
    return int(h[:8], 16) / 0xFFFFFFFF


def path_probs(item: dict, profile: str, *, seed: int, rollout: int = 0) -> dict[str, float]:
    """Deterministic path distribution for (item, profile, rollout). Documented, not empirical."""
    short = item["id"].split("-")[1]
    wj_base, cft_base = ATTRACTOR_PRIORS.get(short, DEFAULT_PRIOR)
    tier_factor = 1.0 if item.get("tier") == "hard" else 0.6
    noise = (_urand(seed, item["id"], "noise") - 0.5) * 0.20      # +/-0.10 per-item jitter
    wj_base = min(0.92, max(0.02, wj_base + noise))
    m = PROFILES[profile]

    if "fi_base" in m:  # evaluation / held-out profiles: anchor on Fi, leak some Wj/CFT
        p_wj = max(m.get("wj_min_hard", 0.0) if item.get("tier") == "hard" else 0.0,
                   wj_base * m["wj_scale"] * tier_factor)
        p_cft = cft_base * m["cft_scale"] * tier_factor
        p_fi = max(0.05, m["fi_base"] - 0.20 * wj_base * tier_factor)
        p_mixed = 0.06
    else:               # calibration profiles: anchor on the attractor
        p_wj = min(0.95, (wj_base + m["wj_gain"]) * m["wj_scale"] * tier_factor + (1 - tier_factor) * 0.0)
        p_cft = cft_base * m["cft_scale"]
        p_fi = max(m["fi_floor"], 1 - p_wj - p_cft - 0.03)
        p_mixed = 0.03
    tot = p_wj + p_cft + p_fi + p_mixed
    return {"Wj": p_wj / tot, "CFT": p_cft / tot, "Fi": p_fi / tot, "mixed": p_mixed / tot}


def choose_path(item: dict, profile: str, *, seed: int, rollout: int) -> str:
    probs = path_probs(item, profile, seed=seed, rollout=rollout)
    u = _urand(seed, item["id"], profile, "roll", rollout)
    c = 0.0
    for path in ("Wj", "CFT", "Fi", "mixed"):
        c += probs[path]
        if u <= c:
            return path
    return "Fi"


def synthesize_text(gold: dict, path: str) -> str:
    """Emit a short response that carries the chosen path's planted markers, so the marker
    scorer round-trips (this is the integration test: gen-path must equal scored-path)."""
    if path == "mixed":
        fm = (gold.get("paths", {}).get("fruit", {}).get("markers") or ["does the right thing"])[:1]
        wm = (gold.get("paths", {}).get("vice", {}).get("markers") or ["takes the advantage"])[:1]
        markers = fm + wm
        tag = "MIXED"
    else:
        key = {"Wj": "vice", "CFT": "cft", "Fi": "fruit"}[path]
        markers = (gold.get("paths", {}).get(key, {}).get("markers") or ["(no markers)"])[:3]
        tag = path
    body = " ".join(f"[{tag}] {mk}." for mk in markers)
    return f"(synthetic reference response) {body}"


class SyntheticModel(ModelAdapter):
    """ModelAdapter that returns documented-synthetic responses. profile comes from ModelSpec."""
    def __init__(self, spec):
        super().__init__(spec)
        self.profile = spec.profile or "aligned_high"
        self.seed = spec.params.get("seed", 20260706)

    def generate(self, item, gold, *, system=None, rollout=0):
        path = choose_path(item, self.profile, seed=self.seed, rollout=rollout)
        return {"text": synthesize_text(gold, path), "intended_path": path}
