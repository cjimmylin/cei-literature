#!/usr/bin/env python3
"""Deterministic UNFENCED synthetic reference — harness validation only."""
from __future__ import annotations

import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path

try:
    from .model_adapters import ModelAdapter  # type: ignore
except ImportError:
    from model_adapters import ModelAdapter  # type: ignore


DEFAULT_REFERENCE = Path(__file__).with_name("synthetic_reference.json")


@lru_cache(maxsize=None)
def load_reference(path: str | Path = DEFAULT_REFERENCE, *, expected_design: str | None = None) -> dict:
    p = Path(path).resolve()
    data = json.loads(p.read_text(encoding="utf-8"))
    if data.get("design") != expected_design and expected_design is not None:
        raise ValueError(
            f"synthetic reference design {data.get('design')!r} does not match {expected_design!r}"
        )
    for key in ("profiles", "environment_priors"):
        if not isinstance(data.get(key), dict) or not data[key]:
            raise ValueError(f"synthetic reference lacks non-empty {key}")
    for name, values in {**data["profiles"], **data["environment_priors"]}.items():
        if not isinstance(values, dict) or any(
            isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v)
            for v in values.values()
        ):
            raise ValueError(f"synthetic reference row {name!r} must contain finite numeric values")
    return data


def _urand(*parts) -> float:
    digest = hashlib.sha256("::".join(map(str, parts)).encode()).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def _clamp(value: float) -> float:
    return min(0.97, max(0.01, value))


def choose(item: dict, gold: dict, profile_name: str, *, arm: str, seed: int, rollout: int,
           reference_path: str | Path) -> dict:
    reference = load_reference(reference_path, expected_design="unfenced")
    short = item["id"].split("-")[1]
    if short not in reference["environment_priors"]:
        raise KeyError(f"unknown UNFENCED synthetic environment {short!r}")
    if profile_name not in reference["profiles"]:
        raise KeyError(f"unknown UNFENCED synthetic profile {profile_name!r}")
    profile = reference["profiles"][profile_name]
    prior = reference["environment_priors"][short]
    notice_p = profile["notice_base"] + prior["notice_delta"]
    if arm == "V3":
        notice_p += profile["v3_notice_delta"]
    notice_p = _clamp(notice_p)
    noticed = _urand(seed, item["id"], profile_name, arm, rollout, "notice") < notice_p
    if not noticed:
        return {
            "noticed": False, "surfaced": False, "acted": False, "outcome": "miss",
            "rule_citing": False, "self_crowning": False,
            "minor_fit_deficit": False, "serious_override": False,
        }

    flags = {
        "rule_citing": _urand(
            seed, item["id"], profile_name, arm, rollout, "rule_citing"
        ) < profile["rule_citing_rate"],
        "self_crowning": _urand(
            seed, item["id"], profile_name, arm, rollout, "self_crowning"
        ) < profile["self_crowning_rate"],
        "minor_fit_deficit": False,
        "serious_override": False,
    }

    fit_p = profile["fit_base"] + prior["fit_delta"]
    if arm == "V1":
        fit_p += profile["v1_fit_gain"]
    elif arm == "V2" and gold["affordance"]["v2_rule_covers"]:
        fit_p += profile["v2_fit_gain"]
    elif arm == "V3":
        fit_p = profile["v3_surface_fit"]
    fit_p = _clamp(fit_p)
    draw = _urand(seed, item["id"], profile_name, arm, rollout, "outcome")
    if draw < fit_p:
        flags["minor_fit_deficit"] = _urand(
            seed, item["id"], profile_name, arm, rollout, "minor_fit_deficit"
        ) < profile["minor_deficit_rate"]
        if arm == "V3" or gold["affordance"]["mode"] == "restraint":
            return {"noticed": True, "surfaced": True, "acted": False, "outcome": "boundary_respecting_decline", **flags}
        return {"noticed": True, "surfaced": True, "acted": True, "outcome": "fitting_act", **flags}
    if draw < fit_p + profile["overshoot_rate"]:
        flags["serious_override"] = _urand(
            seed, item["id"], profile_name, arm, rollout, "serious_override"
        ) < profile["serious_override_rate"]
        return {"noticed": True, "surfaced": True, "acted": True, "outcome": "overshoot", **flags}
    return {"noticed": True, "surfaced": False, "acted": False, "outcome": "miss", **flags}


class SyntheticModel(ModelAdapter):
    def __init__(self, spec):
        super().__init__(spec)
        self.profile = spec.profile
        self.seed = int(spec.params.get("seed", 20260709))
        self.reference_path = spec.params["reference_path"]

    def generate(self, item, gold, *, arm, system=None, rollout=0):
        intended = choose(
            item, gold, self.profile, arm=arm, seed=self.seed, rollout=rollout,
            reference_path=self.reference_path,
        )
        aff = gold["affordance"]["id"]
        text = (
            f"[AFF:{aff}] [NOTICE:{'yes' if intended['noticed'] else 'no'}] "
            f"[SURFACE:{'yes' if intended['surfaced'] else 'no'}] "
            f"[ACTED:{'yes' if intended['acted'] else 'no'}] "
            f"[OUTCOME:{intended['outcome']}] "
            f"[RULE_CITING:{'yes' if intended['rule_citing'] else 'no'}] "
            f"[SELF_CROWNING:{'yes' if intended['self_crowning'] else 'no'}] "
            f"[MINOR_DEFICIT:{'yes' if intended['minor_fit_deficit'] else 'no'}] "
            f"[SERIOUS_OVERRIDE:{'yes' if intended['serious_override'] else 'no'}]"
        )
        return {
            "text": text,
            "intended": {"affordance_id": aff, **intended},
        }

    def probe_notice(self, item, gold, *, arm, prior_text, system=None, rollout=0):
        reference = load_reference(self.reference_path, expected_design="unfenced")
        short = item["id"].split("-")[1]
        profile = reference["profiles"][self.profile]
        prior = reference["environment_priors"][short]
        probability = profile["notice_base"] + prior["notice_delta"] + 0.08
        if arm == "V3":
            probability += profile["v3_notice_delta"]
        noticed = _urand(
            self.seed, item["id"], self.profile, arm, rollout, "post_episode_probe"
        ) < _clamp(probability)
        aff = gold["affordance"]["id"]
        return {
            "text": f"[PROBE_AFF:{aff}] [PROBE_NOTICE:{'yes' if noticed else 'no'}]",
            "intended": {"affordance_id": aff, "probe_noticed": noticed},
        }
