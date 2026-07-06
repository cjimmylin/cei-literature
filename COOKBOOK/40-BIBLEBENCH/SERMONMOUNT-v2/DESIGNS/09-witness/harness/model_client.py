"""
model_client.py — Model interface for the WITNESS harness.

`ModelClient` is the seam between the instrument and whatever produces responses. A REAL
run plugs in an AnthropicClient / CodexClient (stubbed below — they raise until credentials
exist). The P1 in this repository runs `MockModelClient`, a DETERMINISTIC simulator used
for HARNESS VALIDATION ONLY.

WHY A MOCK, AND WHAT IT DOES / DOES NOT SHOW
--------------------------------------------
This vault has no API credentials (no .env, no keys; only the anthropic SDK is installed).
A live multi-model P1 is therefore credential-gated (the Fable-review STOP point). To prove
the instrument is CORRECT before spending real tokens, MockModelClient emits responses drawn
from a *hand-set* gap profile: a known END->ACT dissociation concentrated in the predicted
large-gap principles and ~zero in the control principles (S12, S16), plus a pure format-
difficulty penalty applied equally to moral and non-moral items.

Consequently the numbers the pipeline produces from the mock are NOT a measurement of any
model. They are a check that the analysis (a) recovers the injected gap structure, (b)
subtracts the format effect correctly, and (c) that the prediction test fires when the
injected structure matches the corpus predictions and fails when it does not (mock-gamma).
Swap in a real client and the identical pipeline yields real numbers.

Deterministic: all randomness is hash-derived, so a run is byte-reproducible (no seeds, no
wall-clock — safe to re-run and diff).
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
def _u(*parts: Any) -> float:
    """Deterministic uniform draw in [0,1) from the given parts."""
    h = hashlib.sha256("::".join(str(p) for p in parts).encode("utf-8")).hexdigest()
    return int(h[:12], 16) / float(1 << 48)


@dataclass
class ModelResponse:
    modality: str
    raw: Any                       # END: {"answer","confidence"}; REC: {"choice": int};
                                   # GEN: {"text": str}; ACT: {"tool","args"}
    meta: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
class ModelClient:
    """Abstract responder. respond() receives the full rendered item; a REAL client must
    use ONLY item['prompt'] (+ item['tools'] for ACT) and never the private scoring key."""

    name: str = "abstract"

    def respond(self, item: dict[str, Any], monitored: bool = True, rep: int = 0) -> ModelResponse:
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Mock gap profiles.  Each profile encodes: base competence, a per-modality pure format
# penalty (SAME shape for all — the thing the control battery estimates and we subtract),
# a per-modality TRUE moral gap (the profession->behaviour dissociation, ×sid weight), and
# per-S-ID weights.  alpha/beta follow the corpus predictions (big gap on S38/S02/S09/S17/
# S19/S28/S35, ~0 on controls). gamma VIOLATES them (gaps everywhere) so the prediction
# test has a negative case.
_FORMAT_PENALTY = {"END": 0.00, "REC": 0.03, "GEN": 0.06, "ACT": 0.11}   # pure format, all items

# corpus-predicted relative gap magnitude per S-ID (brief §3); controls ~0
_PRED_WEIGHT = {
    "S38": 1.00, "S02": 0.80, "S09": 0.85, "S17": 0.80, "S19": 0.80,
    "S28": 0.80, "S35": 0.80, "S06": 0.45, "S12": 0.08, "S16": 0.08,
}

_PROFILES = {
    "mock-alpha": dict(base=0.92, base_ctrl=0.95,
                       moral_gap={"END": 0.00, "REC": 0.05, "GEN": 0.11, "ACT": 0.34},
                       weight=_PRED_WEIGHT, monitored_bonus=0.06),
    "mock-beta":  dict(base=0.85, base_ctrl=0.90,
                       moral_gap={"END": 0.00, "REC": 0.06, "GEN": 0.13, "ACT": 0.29},
                       weight=_PRED_WEIGHT, monitored_bonus=0.05),
    # gamma: same *shape* format penalty, but its moral gap is UNIFORM across S-IDs
    # (controls gap as much as S38) — the anisotropy prediction should FAIL for gamma.
    "mock-gamma": dict(base=0.80, base_ctrl=0.88,
                       moral_gap={"END": 0.02, "REC": 0.08, "GEN": 0.14, "ACT": 0.26},
                       weight={s: 0.6 for s in _PRED_WEIGHT}, monitored_bonus=0.10),
}


class MockModelClient(ModelClient):
    """Deterministic simulator. NOT a measurement of any real model (see module docstring)."""

    def __init__(self, name: str):
        if name not in _PROFILES:
            raise ValueError(f"unknown mock profile {name}; have {list(_PROFILES)}")
        self.name = name
        self.p = _PROFILES[name]

    # -- core propensity -----------------------------------------------------
    def _gold_rate(self, sid: str, modality: str, is_control: bool, monitored: bool) -> float:
        p = self.p
        fmt = _FORMAT_PENALTY[modality]
        if is_control:
            rate = p["base_ctrl"] - fmt
        else:
            w = p["weight"].get(sid, 0.6)
            rate = p["base"] - fmt - p["moral_gap"][modality] * w
        # eval-awareness: unmonitored ACT/GEN degrade more (11-15% precedent, Law 6).
        if not monitored and modality in ("GEN", "ACT"):
            rate -= p["monitored_bonus"]
        return max(0.02, min(0.98, rate))

    def _pick_pole(self, item: dict, modality: str, monitored: bool, rep: int) -> str:
        sid = item["sid"][0]
        is_ctrl = item.get("is_control", False)
        gr = self._gold_rate(sid, modality, is_ctrl, monitored)
        # `rep` is the sample index: real benchmarks sample each item k times to estimate a
        # gold-RATE; here each rep is an independent hash-derived Bernoulli draw.
        draw = _u(self.name, item["item_id"], modality, monitored, rep)
        if draw < gr:
            return "gold"
        # non-gold splits deficient / counterfeit (+ small neutral), hash-decided
        d2 = _u(self.name, item["item_id"], modality, "pole", rep)
        if d2 < 0.10:
            return "neutral"
        return "deficient" if d2 < 0.55 else "counterfeit"

    # -- interface -----------------------------------------------------------
    def respond(self, item: dict[str, Any], monitored: bool = True, rep: int = 0) -> ModelResponse:
        m = item["modality"]
        pole = self._pick_pole(item, m, monitored, rep)
        key = item["scoring_key"]

        if m == "END":
            # gold endorsement = agree on a normal item, disagree on a reverse-keyed item
            gold_endorse = (pole == "gold")
            answer = ("agree" if gold_endorse else "disagree")
            if key.get("reverse_keyed"):
                answer = "disagree" if gold_endorse else "agree"
            conf = 0.6 + 0.35 * _u(self.name, item["item_id"], "conf", rep)
            return ModelResponse(m, {"answer": answer, "confidence": round(conf, 3)},
                                 {"intended_pole": pole})

        if m == "REC":
            order = key["option_order"]                # list of poles in shown order
            choice = order.index(pole) if pole in order else order.index("neutral")
            return ModelResponse(m, {"choice": choice}, {"intended_pole": pole})

        if m == "GEN":
            signals = " ".join(key["signals"].get(pole, []))
            text = f"{key['pole_text'].get(pole, '')} {signals}".strip()
            return ModelResponse(m, {"text": text}, {"intended_pole": pole})

        if m == "ACT":
            sig = key["action_signatures"]
            tool = sig.get("tool", (item.get("tools") or ["noop"])[0])
            body = " ".join(sig.get(pole, []))
            return ModelResponse(m, {"tool": tool, "args": {"body": body}},
                                 {"intended_pole": pole})

        raise ValueError(f"unknown modality {m}")


# ---------------------------------------------------------------------------
# Real-client stubs — the credential-gated path. Wire these when keys exist, then the
# identical harness produces real numbers (brief §9 P1: >=3 models, >=2 families;
# program directive §5: aim for >=4 across >=2 families when budget allows).
class AnthropicClient(ModelClient):
    def __init__(self, model: str):
        self.name = model
        raise NotImplementedError(
            "AnthropicClient is credential-gated: set ANTHROPIC_API_KEY and implement "
            "respond() via the anthropic SDK (installed). END/REC -> text completion; "
            "ACT -> tool-use loop against harness.act_sandbox. This is the Fable/credential "
            "STOP point recorded in the P1 report.")


class CodexClient(ModelClient):
    def __init__(self, model: str = "gpt-5-codex"):
        self.name = model
        raise NotImplementedError(
            "CodexClient would shell out to the OAuth `codex` CLI (present on PATH) for an "
            "OpenAI-family model — a single-family real slice. Cross-family P1 still needs an "
            "Anthropic key. Credential-gated.")


def get_client(spec: str) -> ModelClient:
    if spec in _PROFILES:
        return MockModelClient(spec)
    if spec.startswith("anthropic:"):
        return AnthropicClient(spec.split(":", 1)[1])
    if spec.startswith("codex:"):
        return CodexClient(spec.split(":", 1)[1])
    raise ValueError(f"unknown client spec {spec}")


MOCK_MODELS = ["mock-alpha", "mock-beta", "mock-gamma"]
