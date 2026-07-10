#!/usr/bin/env python3
"""Pluggable model-adapter interface for the THORNS harness.

ONE interface, three back-ends:
  - SyntheticModel  (synthetic_reference.py) — documented offline reference model; NO credentials.
  - AnthropicModel  — real, credential-gated (ANTHROPIC_API_KEY). Ready for the live pilot.
  - OpenAIModel     — portable stub; raises with install/credential instructions.

Roles (brief §A9.2 + fresh-eyes objections #2, #9):
  calibration        — 3 open models + the frozen attacker persona (never evaluated models)
  evaluation         — the models under test (the 3-model pilot)
  held_out_frontier  — D-21 transfer models; MUST be a different family than calibration AND evaluation
`family` and `vendor` labels are load-bearing provenance. load_roster() FAILS LOUD if a family
appears in more than one role, and live mode also rejects cross-role vendor overlap (D-37 S-10).
"""
from __future__ import annotations
import os, json, re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ModelSpec:
    name: str
    family: str
    vendor: str                         # load-bearing real provider lineage (D-37 S-10)
    adapter: str                       # "synthetic" | "anthropic" | "openai"
    role: str                          # calibration | evaluation | held_out_frontier
    model_id: str | None = None        # live back-ends
    profile: str | None = None         # synthetic back-end behavior profile
    attacker: bool = False             # exactly one calibration attacker in live THORNS
    persona_path: str | None = None    # frozen persona markdown; attacker only
    params: dict = field(default_factory=dict)


class ModelAdapter(ABC):
    def __init__(self, spec: ModelSpec):
        self.spec = spec
        self.name, self.family, self.vendor, self.role = (
            spec.name, spec.family, spec.vendor, spec.role
        )
        self.system_prompt: str | None = None

    @abstractmethod
    def generate(
        self, item: dict, gold: dict, *, system: str | None = None, rollout: int = 0
    ) -> dict:
        """Return {'text': str, 'intended_path': str|None}. intended_path is set only by the
        synthetic model (for the scorer self-check); live adapters return None for it."""
        ...


class AnthropicModel(ModelAdapter):
    """Real adapter. Credential-gated: needs ANTHROPIC_API_KEY. Wired but not exercised in this
    credential-blocked environment — flip config mode to 'live' once a key is present."""
    def generate(self, item, gold, *, system=None, rollout=0):
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
    def generate(self, item, gold, *, system=None, rollout=0):
        raise NotImplementedError(
            "OpenAIModel is a stub. Install the openai package with the active environment's "
            "`python -m pip install openai`, set OPENAI_API_KEY, then implement generate() with "
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


def load_persona_prompt(path: str | Path) -> str:
    """Load exactly one fenced prompt from a frozen persona markdown file."""
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"attacker persona file is missing or unreadable: {p}")
    blocks = re.findall(r"```(?:text)?\s*\n(.*?)\n```", p.read_text(encoding="utf-8"), re.S)
    if len(blocks) != 1 or not blocks[0].strip():
        raise SystemExit(f"attacker persona must contain exactly one non-empty fenced prompt: {p}")
    return blocks[0].strip()


def load_roster(config: dict) -> dict[str, list[ModelAdapter]]:
    """Build adapters and enforce load-bearing family/vendor/persona invariants."""
    from synthetic_reference import SyntheticModel, load_reference  # local import to avoid cycle
    adapters: dict[str, list[ModelAdapter]] = {}
    family_role: dict[str, set[str]] = {}
    vendor_role: dict[str, set[str]] = {}
    attackers: list[ModelAdapter] = []
    reference_path = (config.get("paths") or {}).get("synthetic_reference")
    has_synthetic = any(
        spec.get("adapter") == "synthetic"
        for specs in config.get("roles", {}).values()
        for spec in specs
    )
    if has_synthetic:
        if not reference_path:
            raise SystemExit("synthetic roster requires paths.synthetic_reference")
        load_reference(reference_path, expected_design=config.get("design"))
    for role, specs in config["roles"].items():
        adapters[role] = []
        for raw in specs:
            s = dict(raw)
            if not str(s.get("family", "")).strip():
                raise SystemExit(f"FAMILY label missing for role={role} model={s.get('name')}")
            if not str(s.get("vendor", "")).strip():
                raise SystemExit(f"VENDOR label missing for role={role} model={s.get('name')}")
            params = dict(s.get("params") or {})
            if s.get("adapter") == "synthetic" and reference_path:
                params.setdefault("reference_path", reference_path)
            s["params"] = params
            spec = ModelSpec(role=role, **s)
            family_role.setdefault(spec.family.strip().casefold(), set()).add(role)
            vendor_role.setdefault(spec.vendor.strip().casefold(), set()).add(role)
            if spec.persona_path and not spec.attacker:
                raise SystemExit(
                    f"attacker persona may be attached only to the calibration attacker: {spec.name}"
                )
            if spec.attacker and role != "calibration":
                raise SystemExit(f"attacker persona role must be calibration, got {role}: {spec.name}")
            if spec.adapter == "synthetic":
                adapter = SyntheticModel(spec)
            elif spec.adapter == "anthropic":
                adapter = AnthropicModel(spec)
            elif spec.adapter == "openai":
                adapter = OpenAIModel(spec)
            else:
                raise ValueError(f"unknown adapter {spec.adapter}")
            if spec.attacker:
                if not spec.persona_path:
                    if config.get("mode") == "live":
                        raise SystemExit("live calibration attacker lacks an attacker persona path")
                else:
                    adapter.system_prompt = load_persona_prompt(spec.persona_path)
                attackers.append(adapter)
            adapters[role].append(adapter)
    # Disjointness: calibration / evaluation / held_out_frontier must not share a family.
    bad = {fam: sorted(roles) for fam, roles in family_role.items() if len(roles) > 1}
    if bad:
        raise SystemExit(f"ROLE-FAMILY OVERLAP (objection #9 guard): {bad}. "
                         f"Calibration, evaluation, and held_out_frontier must be disjoint families.")
    attacker_required = (
        config.get("mode") == "live"
        or config.get("g1_aggregation") == "attacker_primary"
    )
    if attacker_required:
        if len(attackers) != 1:
            raise SystemExit(
                "THORNS attacker-primary calibration requires exactly one explicit "
                f"calibration attacker; found {len(attackers)}"
            )
    if config.get("mode") == "live":
        bad_vendor = {
            vendor: sorted(roles) for vendor, roles in vendor_role.items() if len(roles) > 1
        }
        if bad_vendor:
            raise SystemExit(
                f"ROLE-VENDOR OVERLAP (D-37 S-10 guard): {bad_vendor}. "
                "Calibration, evaluation, and held_out_frontier must be vendor-disjoint in live mode."
            )
    return adapters


if __name__ == "__main__":
    cfg = json.loads((Path(__file__).with_name("pilot_config.json")).read_text())
    r = load_roster(cfg)
    for role, ms in r.items():
        print(f"{role}: " + ", ".join(f"{m.name}({m.family}; {m.vendor})" for m in ms))
