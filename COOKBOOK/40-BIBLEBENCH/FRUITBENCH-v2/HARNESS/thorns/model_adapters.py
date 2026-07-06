#!/usr/bin/env python3
"""Pluggable model-adapter interface for the THORNS harness.

ONE interface, three back-ends:
  - SyntheticModel  (synthetic_reference.py) — documented offline reference model; NO credentials.
  - AnthropicModel  — real, credential-gated (ANTHROPIC_API_KEY). Ready for the live pilot.
  - OpenAIModel     — stub; raises with install/credential instructions.

Roles (brief §A9.2 + fresh-eyes objections #2, #9):
  calibration        — 3 open models + the frozen attacker persona (never evaluated models)
  evaluation         — the models under test (the 3-model pilot)
  held_out_frontier  — D-21 transfer models; MUST be a different family than calibration AND evaluation
load_roster() FAILS LOUD if any family appears in more than one role (objection #9: no silent reuse).
"""
from __future__ import annotations
import os, json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ModelSpec:
    name: str
    family: str
    adapter: str                       # "synthetic" | "anthropic" | "openai"
    role: str                          # calibration | evaluation | held_out_frontier
    model_id: str | None = None        # live back-ends
    profile: str | None = None         # synthetic back-end behavior profile
    params: dict = field(default_factory=dict)


class ModelAdapter(ABC):
    def __init__(self, spec: ModelSpec):
        self.spec = spec
        self.name, self.family, self.role = spec.name, spec.family, spec.role

    @abstractmethod
    def generate(self, item: dict, gold: dict, *, system: str | None = None) -> dict:
        """Return {'text': str, 'intended_path': str|None}. intended_path is set only by the
        synthetic model (for the scorer self-check); live adapters return None for it."""
        ...


class AnthropicModel(ModelAdapter):
    """Real adapter. Credential-gated: needs ANTHROPIC_API_KEY. Wired but not exercised in this
    credential-blocked environment — flip config mode to 'live' once a key is present."""
    def generate(self, item, gold, *, system=None):
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError(
                "AnthropicModel requires ANTHROPIC_API_KEY (absent in this environment). "
                "This is the credential block flagged in the fresh-eyes objections. "
                "Set the key and rerun with mode:'live' to execute the real pilot.")
        import anthropic  # noqa
        client = anthropic.Anthropic(api_key=key)
        prompt = _render_prompt(item)
        msg = client.messages.create(
            model=self.spec.model_id or "claude-sonnet-4-6",
            max_tokens=1024,
            system=system or "You are a helpful assistant.",
            messages=[{"role": "user", "content": prompt}],
        )
        return {"text": "".join(b.text for b in msg.content if getattr(b, "type", "") == "text"),
                "intended_path": None}


class OpenAIModel(ModelAdapter):
    def generate(self, item, gold, *, system=None):
        raise NotImplementedError(
            "OpenAIModel is a stub. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python "
            "-m pip install openai` and set OPENAI_API_KEY, then implement generate() with "
            "client.chat.completions.create(...). Cross-vendor coverage is required so the D-21 "
            "held-out frontier is a different family than the Anthropic evaluation models (objection #2).")


def _render_prompt(item: dict) -> str:
    """Flatten a bank item to a single user prompt (single-shot) or a scripted transcript (arc)."""
    if item.get("format") == "escalation_arc":
        lines = [item.get("prompt", "").strip(), ""]
        for t in item.get("turns", []):
            lines.append(f"[user, beat {t.get('beat')}]: {t.get('user','').strip()}")
        return "\n".join(lines)
    return item.get("prompt", "")


def load_roster(config: dict) -> dict[str, list[ModelAdapter]]:
    """Build adapters per role and enforce cross-role family disjointness (objection #9)."""
    from synthetic_reference import SyntheticModel  # local import to avoid cycle
    adapters: dict[str, list[ModelAdapter]] = {}
    family_role: dict[str, set[str]] = {}
    for role, specs in config["roles"].items():
        adapters[role] = []
        for s in specs:
            spec = ModelSpec(role=role, **s)
            family_role.setdefault(spec.family, set()).add(role)
            if spec.adapter == "synthetic":
                adapters[role].append(SyntheticModel(spec))
            elif spec.adapter == "anthropic":
                adapters[role].append(AnthropicModel(spec))
            elif spec.adapter == "openai":
                adapters[role].append(OpenAIModel(spec))
            else:
                raise ValueError(f"unknown adapter {spec.adapter}")
    # Disjointness: calibration / evaluation / held_out_frontier must not share a family.
    bad = {fam: sorted(roles) for fam, roles in family_role.items() if len(roles) > 1}
    if bad:
        raise SystemExit(f"ROLE-FAMILY OVERLAP (objection #9 guard): {bad}. "
                         f"Calibration, evaluation, and held_out_frontier must be disjoint families.")
    return adapters


if __name__ == "__main__":
    cfg = json.loads((Path(__file__).with_name("pilot_config.json")).read_text())
    r = load_roster(cfg)
    for role, ms in r.items():
        print(f"{role}: " + ", ".join(f"{m.name}({m.family})" for m in ms))
