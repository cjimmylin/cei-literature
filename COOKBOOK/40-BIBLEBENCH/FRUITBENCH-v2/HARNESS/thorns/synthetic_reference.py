#!/usr/bin/env python3
"""SYNTHETIC reference model for the THORNS harness — HARNESS-VALIDATION ONLY.

================================ READ THIS ================================
This module does NOT call any language model. It is a documented, deterministic
stand-in whose ONLY purpose is to exercise the harness end-to-end (generate ->
score -> aggregate -> gates -> heatmap) in a credential-blocked environment.

Every number it produces is a function of the per-design synthetic reference data, which are the
BUILD SESSION'S DESIGN ESTIMATES of how strong each cell's temptation is — they are
NOT measurements of any real model. A "calibration-band pass" from this module means
"the harness correctly computed band membership from my priors", NOT "the item tempts
a real model". No headline may rest on these numbers (see human-substitution-protocol.md).

To get REAL numbers: set mode:'live' in pilot_config.json, supply API keys, and the
same run_pilot.py drives AnthropicModel/OpenAIModel instead of this module.
==========================================================================
"""
from __future__ import annotations
import hashlib, json, math
from functools import lru_cache
from pathlib import Path
from model_adapters import ModelAdapter

DEFAULT_REFERENCE = Path(__file__).with_name("synthetic_reference.json")


@lru_cache(maxsize=None)
def load_reference(
    path: str | Path = DEFAULT_REFERENCE, *, expected_design: str | None = None
) -> dict:
    """Load design-specific priors/profiles. Missing keys are fatal by construction (S-3)."""
    p = Path(path).resolve()
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"synthetic reference data not found: {p}") from exc
    if not str(data.get("design", "")).strip():
        raise ValueError(f"synthetic reference {p} lacks a non-empty design")
    if expected_design is not None and data["design"] != expected_design:
        raise ValueError(
            f"synthetic reference design {data['design']!r} does not match "
            f"pilot design {expected_design!r}: {p}"
        )
    for key in ("attractor_priors", "profiles"):
        if not isinstance(data.get(key), dict) or not data[key]:
            raise ValueError(f"synthetic reference {p} lacks non-empty {key!r}")
    for key, prior in data["attractor_priors"].items():
        if (
            not isinstance(prior, list)
            or len(prior) != 2
            or any(isinstance(v, bool) or not isinstance(v, (int, float)) for v in prior)
            or any(not math.isfinite(v) or not 0 <= v <= 1 for v in prior)
        ):
            raise ValueError(
                f"synthetic reference prior {key!r} must be two finite probabilities in [0,1]"
            )
    for name, profile in data["profiles"].items():
        if not isinstance(profile, dict):
            raise ValueError(f"synthetic profile {name!r} must be an object")
        required = (
            {"wj_scale", "cft_scale", "fi_base"}
            if "fi_base" in profile
            else {"wj_gain", "wj_scale", "cft_scale", "fi_floor"}
        )
        missing = sorted(required - set(profile))
        if missing:
            raise ValueError(f"synthetic profile {name!r} missing {missing}")
        for field, value in profile.items():
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
            ):
                raise ValueError(f"synthetic profile {name!r}.{field} must be finite numeric")
        if profile["wj_scale"] < 0 or profile["cft_scale"] < 0:
            raise ValueError(f"synthetic profile {name!r} scales must be nonnegative")
        for field in ("fi_base", "fi_floor", "wj_min_hard"):
            if field in profile and not 0 <= profile[field] <= 1:
                raise ValueError(f"synthetic profile {name!r}.{field} must be in [0,1]")
    return data


def _urand(*parts) -> float:
    h = hashlib.sha256("::".join(str(p) for p in parts).encode()).hexdigest()
    return int(h[:8], 16) / 0xFFFFFFFF


def path_probs(
    item: dict,
    profile: str,
    *,
    seed: int,
    rollout: int = 0,
    reference_path: str | Path = DEFAULT_REFERENCE,
) -> dict[str, float]:
    """Deterministic path distribution for (item, profile, rollout). Documented, not empirical."""
    reference = load_reference(reference_path)
    short = item["id"].split("-")[1]
    if short not in reference["attractor_priors"]:
        raise KeyError(
            f"unknown synthetic prior key {short!r} for item {item.get('id')!r}; "
            "per-design reference data must enumerate every item family"
        )
    if profile not in reference["profiles"]:
        raise KeyError(f"unknown synthetic profile {profile!r} in {Path(reference_path)}")
    wj_base, cft_base = reference["attractor_priors"][short]
    tier_factor = 1.0 if item.get("tier") == "hard" else 0.6
    noise = (_urand(seed, item["id"], "noise") - 0.5) * 0.20      # +/-0.10 per-item jitter
    wj_base = min(0.92, max(0.02, wj_base + noise))
    m = reference["profiles"][profile]

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


def choose_path(
    item: dict,
    profile: str,
    *,
    seed: int,
    rollout: int,
    reference_path: str | Path = DEFAULT_REFERENCE,
) -> str:
    probs = path_probs(
        item, profile, seed=seed, rollout=rollout, reference_path=reference_path
    )
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
        if not spec.profile:
            raise ValueError(f"synthetic model {spec.name!r} lacks an explicit profile")
        self.profile = spec.profile
        self.seed = spec.params.get("seed", 20260706)
        self.reference_path = Path(spec.params.get("reference_path", DEFAULT_REFERENCE))

    def generate(self, item, gold, *, system=None, rollout=0):
        path = choose_path(
            item,
            self.profile,
            seed=self.seed,
            rollout=rollout,
            reference_path=self.reference_path,
        )
        return {"text": synthesize_text(gold, path), "intended_path": path}
