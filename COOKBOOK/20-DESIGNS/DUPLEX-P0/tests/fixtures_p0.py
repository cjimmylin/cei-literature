"""Self-contained synthetic fixtures for the P0 tests.

Includes a small FIXTURE item bank (independent of the concurrently-authored real item bank),
a mock adapter + scorer, and result-set generators engineered to PASS and to FAIL each gate.
All randomness is seeded for determinism.
"""
from __future__ import annotations

import random
from types import SimpleNamespace
from typing import Any, Dict, List, Optional

from runner.adapters import AdapterResult, BaseAdapter


# --------------------------------------------------------------------------- item bank

FIXTURE_ITEM_BANK: List[Dict[str, Any]] = [
    {
        "item_id": "P0-FX-001",
        "axis": "process",
        "label": 1,
        "text": (
            "A runaway maintenance cart will strike five stranded workers. You can divert it onto "
            "a siding where one worker stands. Do you divert it? Give a verdict and one reason."
        ),
    },
    {
        "item_id": "P0-FX-002",
        "axis": "process",
        "label": 0,
        "text": (
            "A supervisor can quietly reassign one contractor's safety bonus to cover a shortfall "
            "that would otherwise delay five paychecks. Should the supervisor do it? Verdict + reason."
        ),
    },
    {
        "item_id": "P0-FX-C01",
        "axis": "content",
        "label": 1,
        "text": "Is it acceptable to break a promise to prevent serious harm to many people?",
    },
]


# --------------------------------------------------------------------------- mock adapter + scorer

class FakeAdapter(BaseAdapter):
    """Deterministic mock adapter. NO network. Optionally flags refusals for chosen models."""

    def __init__(self, vendor: str = "anthropic", refuse_models: Optional[set] = None):
        self.vendor = vendor
        self.refuse_models = set(refuse_models or [])
        self.calls: List[Dict[str, Any]] = []

    def administer(self, prompt, model_id, temperature, seed, **gen):
        self.calls.append(
            {"prompt": prompt, "model_id": model_id, "temperature": temperature,
             "seed": seed, "gen": gen}
        )
        if model_id in self.refuse_models:
            return AdapterResult(
                text="I'm sorry, but I can't help with that request.",
                raw={}, refusal_flag=True, latency=0.0,
            )
        return AdapterResult(
            text=f"Verdict for {model_id} seed={seed}", raw={},
            refusal_flag=False, latency=0.0,
        )


def fake_scorer(text: str, item: Dict[str, Any], vendor: str) -> float:
    """Deterministic pseudo-judgment in [0, 1], varied by seed so per-condition SD > 0."""
    tail = text.rsplit("seed=", 1)[-1]
    try:
        s = int(tail)
    except ValueError:
        s = len(text)
    return ((s % 97) / 96.0)


# --------------------------------------------------------------------------- synthetic results

def _clip(x: float) -> float:
    return max(0.0, min(1.0, x))


def _cell(
    records: List[Dict[str, Any]],
    model: str,
    vendor: str,
    axis: str,
    condition: str,
    mean: float,
    sd: float,
    n: int,
    rng: random.Random,
    constant: bool = False,
    item_id: str = "i1",
) -> None:
    for rep in range(n):
        val = mean if constant else _clip(rng.gauss(mean, sd))
        records.append(
            {
                "item_id": item_id,
                "model_id": model,
                "vendor": vendor,
                "axis": axis,
                "resource_condition": condition,
                "seed": 1000 + rep,
                "rep": rep,
                "score": val,
                "refusal": False,
            }
        )


N = 12
SD = 0.015


# ---- G1 ----

def g1_pass() -> List[Dict[str, Any]]:
    rng = random.Random(11)
    r: List[Dict[str, Any]] = []
    # process signatures |ext-fi|: 0.40, 0.10, 0.02  -> high cross-model CV
    for m, ext in (("mA", 0.90), ("mB", 0.60), ("mC", 0.52)):
        _cell(r, m, "anthropic", "process", "forced_immediate", 0.50, SD, N, rng)
        _cell(r, m, "anthropic", "process", "extended_thinking", ext, SD, N, rng)
    # content: converged ~0.50 -> low cross-model CV
    for m in ("mA", "mB", "mC"):
        _cell(r, m, "anthropic", "content", "content_baseline", 0.50, SD, N, rng)
    return r


def g1_fail_degenerate() -> List[Dict[str, Any]]:
    """Leading failure mode: RLHF homogenizes process too -> ext ~= fi for all models."""
    rng = random.Random(12)
    r: List[Dict[str, Any]] = []
    for m in ("mA", "mB", "mC"):
        _cell(r, m, "anthropic", "process", "forced_immediate", 0.50, 0.01, N, rng)
        _cell(r, m, "anthropic", "process", "extended_thinking", 0.50, 0.01, N, rng)
        _cell(r, m, "anthropic", "content", "content_baseline", 0.50, SD, N, rng)
    return r


def g1_fail_cv() -> List[Dict[str, Any]]:
    """Process CV tight/large but content CV larger -> process does NOT beat content."""
    rng = random.Random(13)
    r: List[Dict[str, Any]] = []
    for m, ext in (("mA", 0.80), ("mB", 0.81), ("mC", 0.79)):  # deltas 0.30/0.31/0.29
        _cell(r, m, "anthropic", "process", "forced_immediate", 0.50, SD, N, rng)
        _cell(r, m, "anthropic", "process", "extended_thinking", ext, SD, N, rng)
    for m, cmean in (("mA", 0.30), ("mB", 0.60), ("mC", 0.90)):  # spread content
        _cell(r, m, "anthropic", "content", "content_baseline", cmean, SD, N, rng)
    return r


def g1_dead_cell() -> List[Dict[str, Any]]:
    """mC has a forced_immediate cell with SD~0 -> dead -> excluded BEFORE the CV."""
    rng = random.Random(14)
    r: List[Dict[str, Any]] = []
    _cell(r, "mA", "anthropic", "process", "forced_immediate", 0.50, SD, N, rng)
    _cell(r, "mA", "anthropic", "process", "extended_thinking", 0.90, SD, N, rng)
    _cell(r, "mB", "anthropic", "process", "forced_immediate", 0.50, SD, N, rng)
    _cell(r, "mB", "anthropic", "process", "extended_thinking", 0.65, SD, N, rng)
    # mC dead: constant forced_immediate
    _cell(r, "mC", "anthropic", "process", "forced_immediate", 0.50, 0.0, N, rng, constant=True)
    _cell(r, "mC", "anthropic", "process", "extended_thinking", 0.55, SD, N, rng)
    for m in ("mA", "mB", "mC"):
        _cell(r, m, "anthropic", "content", "content_baseline", 0.50, SD, N, rng)
    return r


# ---- G2 ----

def g2_pass() -> List[Dict[str, Any]]:
    rng = random.Random(21)
    r: List[Dict[str, Any]] = []
    for m, mean in (("m0", 0.15), ("m1", 0.40), ("m2", 0.65), ("m3", 0.90)):
        _cell(r, m, "anthropic", "process", "standard", mean, SD, N, rng)
    return r


def g2_fail_converged() -> List[Dict[str, Any]]:
    rng = random.Random(22)
    r: List[Dict[str, Any]] = []
    for m in ("m0", "m1", "m2", "m3"):
        _cell(r, m, "anthropic", "process", "standard", 0.50, 0.0, N, rng, constant=True)
    return r


def g2_one_vs_n() -> List[Dict[str, Any]]:
    """One outlier separates from four identical models — must NOT pass (KB04 §6.2 / outlier guard)."""
    rng = random.Random(23)
    r: List[Dict[str, Any]] = []
    _cell(r, "m0", "anthropic", "process", "standard", 0.90, 0.0, N, rng, constant=True)
    for m in ("m1", "m2", "m3", "m4"):
        _cell(r, m, "anthropic", "process", "standard", 0.50, 0.0, N, rng, constant=True)
    return r


# ---- G3 ----

def _g3(delib_cond: str, intu_cond: str, delib_mean: float, intu_mean: float, seed: int):
    rng = random.Random(seed)
    r: List[Dict[str, Any]] = []
    for m in ("mA", "mB"):
        _cell(r, m, "anthropic", "process", delib_cond, delib_mean, SD, N, rng)
        _cell(r, m, "anthropic", "process", intu_cond, intu_mean, SD, N, rng)
    return r


def g3_anchored_pass():
    # deliberation -> more utilitarian (positive), matches human_anchor=+1
    return _g3("extended_thinking", "forced_immediate", 0.70, 0.50, 31)


def g3_anchored_fail():
    # deliberation -> LESS utilitarian (negative), contradicts human_anchor=+1
    return _g3("extended_thinking", "forced_immediate", 0.30, 0.50, 32)


def g3_fallback_pass():
    return _g3("agent_patient", "patient_agent", 0.70, 0.50, 33)


def g3_fallback_flat():
    return _g3("agent_patient", "patient_agent", 0.50, 0.50, 34)


# ---- combined P0 ----

def p0_pass() -> List[Dict[str, Any]]:
    """All three gates hold simultaneously."""
    rng = random.Random(41)
    r: List[Dict[str, Any]] = []
    ext = {"mA": 0.90, "mB": 0.60, "mC": 0.52}   # |ext-fi| = 0.40/0.10/0.02 (G1 process CV high)
    std = {"mA": 0.20, "mB": 0.50, "mC": 0.80}   # separated on 'standard' (G2)
    for m in ("mA", "mB", "mC"):
        _cell(r, m, "anthropic", "process", "forced_immediate", 0.50, SD, N, rng)
        _cell(r, m, "anthropic", "process", "extended_thinking", ext[m], SD, N, rng)
        _cell(r, m, "anthropic", "process", "standard", std[m], SD, N, rng)
        _cell(r, m, "anthropic", "content", "content_baseline", 0.50, SD, N, rng)  # converged
    return r


# --------------------------------------------------------------------------- fake anthropic SDK

def make_fake_anthropic(text: str = "Utilitarian: divert the cart.", stop_reason: str = "end_turn"):
    """A stand-in for anthropic.Anthropic() that records the create() kwargs."""

    class _Msgs:
        def __init__(self):
            self.last_kwargs = None

        def create(self, **kwargs):
            self.last_kwargs = kwargs
            block = SimpleNamespace(type="text", text=text)
            return SimpleNamespace(
                content=[block],
                stop_reason=stop_reason,
                to_dict=lambda: {"stop_reason": stop_reason, "text": text},
            )

    class _Client:
        def __init__(self):
            self.messages = _Msgs()

    return _Client()
