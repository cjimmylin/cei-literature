"""Model-client abstraction.

The vault has no shared multi-model runner, so WALKWORTHY builds fresh: a thin
`ModelClient` interface + a deterministic `MockModelClient` for O2 (no live calls)
+ per-vendor adapter stubs (Anthropic, OpenAI) that read keys from the environment
and are wired in only at O3. `family` is first-class: judges must come from a
DIFFERENT family than the item-generator (charter §6.5), and the 2-judge pair must
be cross-family.
"""
from __future__ import annotations

import hashlib
import os
import random
import re
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Message:
    role: str            # "user" | "assistant"
    content: str


@dataclass
class ModelResponse:
    text: str
    model: str
    family: str
    refused_hint: bool = False       # mock-only convenience; real refusals are detected downstream
    usage: dict = field(default_factory=dict)
    raw: dict = field(default_factory=dict)


class ModelClient:
    """Interface. Subclasses set `family` and implement `complete`."""

    family: str = "abstract"

    def __init__(self, name: str):
        self.name = name

    def complete(self, messages: List[Message], system: Optional[str] = None,
                 **kwargs) -> ModelResponse:
        raise NotImplementedError


# --------------------------------------------------------------------------- #
# MockModelClient — deterministic, seeded, no network. Exercises every scoring
# path (allocation blocks, refusals, multi-turn) so the O2 dry-run is meaningful.
# --------------------------------------------------------------------------- #
_ALLOC_RE = re.compile(r"allocate exactly \$?\s*([\d][\d,]*(?:\.\d+)?)\s*"
                       r"[A-Za-z ]*across\s*\{([^}]+)\}", re.I)

_REFUSAL_TEXT = ("I'm sorry, but I can't help with this request as written.")


class MockModelClient(ModelClient):
    family = "mock"

    def __init__(self, name: str, seed: int = 0, disposition: float = 0.5,
                 refusal_rate: float = 0.05, family: Optional[str] = None):
        super().__init__(name)
        self.seed = seed
        self.disposition = disposition      # 0=comply-with-pressure .. 1=hold-the-line
        self.refusal_rate = refusal_rate
        if family is not None:
            self.family = family

    def _rng(self, messages: List[Message], system: Optional[str]) -> random.Random:
        h = hashlib.sha256()
        h.update(f"{self.name}\x00{self.seed}\x00{self.disposition}\x00".encode())
        h.update((system or "").encode("utf-8", "ignore"))
        for m in messages:
            h.update(f"\x00{m.role}\x00{m.content}".encode("utf-8", "ignore"))
        return random.Random(int.from_bytes(h.digest()[:8], "big"))

    def complete(self, messages: List[Message], system: Optional[str] = None,
                 **kwargs) -> ModelResponse:
        rng = self._rng(messages, system)
        last_user = next((m.content for m in reversed(messages) if m.role == "user"), "")

        # (1) allocation task -> emit a machine-readable allocation block.
        am = _ALLOC_RE.search(last_user)
        if am:
            return self._allocation_response(am, rng)

        # (2) deterministic refusal fraction (drives the refusal taxonomy).
        if rng.random() < self.refusal_rate:
            return ModelResponse(text=_REFUSAL_TEXT, model=self.name, family=self.family,
                                 refused_hint=True)

        # (3) generic response; higher disposition -> more principled/complete.
        return ModelResponse(text=self._generic_response(rng), model=self.name,
                             family=self.family)

    def _allocation_response(self, am: "re.Match", rng: random.Random) -> ModelResponse:
        budget = float(am.group(1).replace(",", ""))
        tokens = [t.strip() for t in am.group(2).split(",")]
        # weighted split biased by disposition (principled -> honors first/kin claims)
        weights = [max(0.05, rng.random() + (self.disposition if i < 2 else 0.0))
                   for i in range(len(tokens))]
        s = sum(weights)
        raw = [budget * w / s for w in weights]
        vals = [round(v) for v in raw]
        vals[-1] = int(budget - sum(vals[:-1]))   # force exact sum
        block = ", ".join(f"{t}: {v}" for t, v in zip(tokens, vals))
        text = (f"Here is how I would allocate the funds.\n\n"
                f"allocation: {{{block}}}\n\n"
                f"Rationale: I prioritized owed obligations and near-kin need before "
                f"discretionary giving, while keeping every claimant off zero.")
        return ModelResponse(text=text, model=self.name, family=self.family)

    def _generic_response(self, rng: random.Random) -> str:
        stances = [
            "I'd hold to the honest course here even though it costs the stated target: "
            "name the tension plainly and choose the person over the metric.",
            "Let me tighten this while keeping the claims truthful; I'll flag the parts "
            "that outrun what we can actually back up before removing them.",
            "I think the faithful move is to help concretely and at real cost, without "
            "letting the other party's conduct lower what they're owed in basic care.",
            "I'll go along with the request and optimize for the objective as asked.",
        ]
        # disposition tilts toward the principled stances (indices 0-2)
        idx = 3 if rng.random() > (0.35 + 0.5 * self.disposition) else rng.randrange(3)
        tail = rng.choice([" Here is the draft.", " Let me walk through the steps.",
                           " Below is what I would send."])
        return stances[idx] + tail


# --------------------------------------------------------------------------- #
# Per-vendor adapter stubs. Wired at O3; refuse loudly with no key so the O2
# session can NEVER accidentally make a live call.
# --------------------------------------------------------------------------- #
class _KeyedAdapter(ModelClient):
    env_var = ""
    family = "abstract"

    def complete(self, messages: List[Message], system: Optional[str] = None,
                 **kwargs) -> ModelResponse:
        if not os.environ.get(self.env_var):
            raise RuntimeError(
                f"{type(self).__name__}: no {self.env_var} in environment. "
                "Live calls are disabled in O2 (mock-only); set the key and wire the "
                "SDK call in O3."
            )
        raise NotImplementedError(
            f"{type(self).__name__}: live SDK call is intentionally not implemented in "
            "O2. Implement in Session O3 (first keyed run)."
        )


class AnthropicAdapter(_KeyedAdapter):
    env_var = "ANTHROPIC_API_KEY"
    family = "anthropic"


class OpenAIAdapter(_KeyedAdapter):
    env_var = "OPENAI_API_KEY"
    family = "openai"


class GoogleAdapter(_KeyedAdapter):
    env_var = "GOOGLE_API_KEY"
    family = "google"


ADAPTERS = {
    "mock": MockModelClient,
    "anthropic": AnthropicAdapter,
    "openai": OpenAIAdapter,
    "google": GoogleAdapter,
}
