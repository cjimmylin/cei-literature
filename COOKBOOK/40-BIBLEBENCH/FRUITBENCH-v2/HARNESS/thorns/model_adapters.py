#!/usr/bin/env python3
"""Pluggable model-adapter interface for the THORNS harness.

ONE message-first interface, four back-ends:
  - SyntheticModel  (synthetic_reference.py) — documented offline reference model; NO credentials.
  - AnthropicModel  — real, credential-gated (ANTHROPIC_API_KEY). Ready for the live pilot.
  - OpenRouterModel — real Responses transport through the shared fail-loud client.
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
from dataclasses import asdict, dataclass, field, is_dataclass
from pathlib import Path
from typing import Any


@dataclass
class ModelSpec:
    name: str
    family: str
    vendor: str                         # load-bearing real provider lineage (D-37 S-10)
    adapter: str                       # synthetic | anthropic | openrouter | openai
    role: str                          # calibration | evaluation | held_out_frontier
    model_id: str | None = None        # live back-ends
    actor_id: str | None = None        # opaque run identity (A01, A02, ...)
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
        self.actor_id = spec.actor_id
        slug = re.sub(r"[^a-z0-9]+", "-", spec.name.casefold()).strip("-")
        self.model_id = spec.model_id or f"{spec.adapter}/{slug}"
        self.system_prompt: str | None = None

    def generate(
        self, item: dict, gold: dict, *, system: str | None = None, rollout: int = 0
    ) -> dict:
        """Compatibility entry point for a first request; never flatten a future arc beat."""
        from trajectory import initial_messages

        return self.generate_messages(
            initial_messages(item),
            item=item,
            gold=gold,
            system=system,
            rollout=rollout,
            turn=1,
        )

    @abstractmethod
    def generate_messages(
        self,
        messages: list[dict[str, str]],
        *,
        item: dict,
        gold: dict,
        system: str | None = None,
        rollout: int = 0,
        turn: int = 1,
    ) -> dict:
        """Generate from only the actor-visible message history supplied by the executor."""
        ...


class AnthropicModel(ModelAdapter):
    """Real adapter. Credential-gated: needs ANTHROPIC_API_KEY. Wired but not exercised in this
    credential-blocked environment — flip config mode to 'live' once a key is present."""
    def generate_messages(
        self, messages, *, item, gold, system=None, rollout=0, turn=1
    ):
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError(
                "AnthropicModel requires ANTHROPIC_API_KEY (absent in this environment). "
                "This is the credential block flagged in the fresh-eyes objections. "
                "Set the key and rerun with mode:'live' to execute the real pilot.")
        import anthropic  # noqa
        client = anthropic.Anthropic(api_key=key)
        request = {
            "model": self.spec.model_id or "claude-sonnet-4-6",
            "max_tokens": int(self.spec.params.get("max_tokens", 1024)),
            "messages": messages,
        }
        if system:
            request["system"] = system
        msg = client.messages.create(**request)
        usage = getattr(msg, "usage", None)
        if hasattr(usage, "model_dump"):
            usage = usage.model_dump()
        elif usage is not None and not isinstance(usage, dict):
            usage = {
                key: getattr(usage, key)
                for key in ("input_tokens", "output_tokens")
                if hasattr(usage, key)
            }
        response_id = getattr(msg, "id", None)
        return {
            "text": "".join(
                b.text for b in msg.content if getattr(b, "type", "") == "text"
            ),
            "intended_path": None,
            "response_id": response_id,
            "request_id": getattr(msg, "_request_id", None),
            "generation_id": None,
            "returned_model": getattr(msg, "model", self.model_id),
            "usage": usage or {},
            "attempt_ledger": [
                {"attempt": 1, "status_code": 200, "response_id": response_id}
            ],
        }


class OpenAIModel(ModelAdapter):
    def generate_messages(
        self, messages, *, item, gold, system=None, rollout=0, turn=1
    ):
        raise NotImplementedError(
            "OpenAIModel is a stub. Install the openai package with the active environment's "
            "`python -m pip install openai`, set OPENAI_API_KEY, then implement generate() with "
            "client.chat.completions.create(...). Cross-vendor coverage is required so the D-21 "
            "held-out frontier is a different family than the Anthropic evaluation models (objection #2).")


class OpenRouterModel(ModelAdapter):
    """OpenRouter Responses adapter backed by HARNESS/shared/openrouter_client.py."""

    def __init__(self, spec: ModelSpec, *, client=None):
        super().__init__(spec)
        if client is None:
            import sys

            harness = Path(__file__).resolve().parent.parent
            if str(harness) not in sys.path:
                sys.path.insert(0, str(harness))
            from shared.openrouter_client import OpenRouterClient

            client = OpenRouterClient()
        self.client = client

    @staticmethod
    def _ledger(value):
        rows = []
        for entry in value or ():
            if is_dataclass(entry):
                rows.append(asdict(entry))
            elif isinstance(entry, dict):
                rows.append(dict(entry))
            else:
                rows.append(str(entry))
        return rows

    def generate_messages(
        self, messages, *, item, gold, system=None, rollout=0, turn=1
    ):
        params = self.spec.params
        expected_slug = params.get("expected_canonical_slug")
        provider_order = params.get("provider_order")
        if not isinstance(expected_slug, str) or not expected_slug.strip():
            raise ValueError("OpenRouterModel requires params.expected_canonical_slug")
        if not isinstance(provider_order, list) or len(provider_order) != 1:
            raise ValueError("OpenRouterModel requires one pinned params.provider_order")
        request_messages = [dict(message) for message in messages]
        if system:
            request_messages.insert(0, {"role": "system", "content": system})
        result = self.client.responses(
            model_id=self.model_id,
            messages=request_messages,
            max_output_tokens=int(params.get("max_output_tokens", 1024)),
            reasoning_effort=params.get("reasoning_effort", "medium"),
            provider_order=list(provider_order),
            expected_canonical_slug=expected_slug.strip(),
            service_tier=params.get("service_tier", "default"),
        )
        return {
            "text": result.text,
            "intended_path": None,
            "response_id": result.response_id,
            "request_id": result.request_id,
            "generation_id": result.generation_id,
            "returned_model": result.returned_model,
            "usage": dict(result.usage),
            "attempt_ledger": self._ledger(result.attempt_ledger),
            "router_metadata": dict(result.router_metadata),
            "routing_headers": dict(result.routing_headers),
            "attempts": result.attempts,
            "latency_ms": result.latency_ms,
            "service_tier": result.service_tier,
        }


def load_persona_prompt(path: str | Path) -> str:
    """Load exactly one fenced prompt from a frozen persona markdown file."""
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"attacker persona file is missing or unreadable: {p}")
    blocks = re.findall(r"```(?:text)?\s*\n(.*?)\n```", p.read_text(encoding="utf-8"), re.S)
    if len(blocks) != 1 or not blocks[0].strip():
        raise SystemExit(f"attacker persona must contain exactly one non-empty fenced prompt: {p}")
    return blocks[0].strip()


def load_roster(
    config: dict, *, openrouter_client: Any | None = None
) -> dict[str, list[ModelAdapter]]:
    """Build adapters and enforce load-bearing family/vendor/persona invariants."""
    from synthetic_reference import SyntheticModel, load_reference  # local import to avoid cycle
    adapters: dict[str, list[ModelAdapter]] = {}
    family_role: dict[str, set[str]] = {}
    vendor_role: dict[str, set[str]] = {}
    attackers: list[ModelAdapter] = []
    explicit_actor_ids: set[str] = set()
    for specs in config.get("roles", {}).values():
        for raw in specs:
            actor_id = raw.get("actor_id")
            if actor_id is None:
                continue
            if not isinstance(actor_id, str) or not re.fullmatch(r"A[0-9]{2,}", actor_id):
                raise SystemExit(f"invalid opaque actor_id: {actor_id!r}")
            if actor_id in explicit_actor_ids:
                raise SystemExit(f"duplicate opaque actor_id: {actor_id}")
            explicit_actor_ids.add(actor_id)
    assigned_actor_ids: set[str] = set()
    next_actor = 1
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
                if not s.get("model_id"):
                    slug = re.sub(
                        r"[^a-z0-9]+", "-", str(s.get("name", "model")).casefold()
                    ).strip("-")
                    s["model_id"] = f"synthetic/{slug}"
            if not s.get("actor_id"):
                while (
                    f"A{next_actor:02d}" in explicit_actor_ids
                    or f"A{next_actor:02d}" in assigned_actor_ids
                ):
                    next_actor += 1
                s["actor_id"] = f"A{next_actor:02d}"
                next_actor += 1
            assigned_actor_ids.add(s["actor_id"])
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
            elif spec.adapter == "openrouter":
                adapter = OpenRouterModel(spec, client=openrouter_client)
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
