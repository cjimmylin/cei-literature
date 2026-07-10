#!/usr/bin/env python3
"""Reusable model adapters for UNFENCED, copied after the THORNS D-37 regression gate."""
from __future__ import annotations

import os
from pathlib import Path
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ModelSpec:
    name: str
    family: str
    vendor: str
    adapter: str
    role: str
    model_id: str | None = None
    profile: str | None = None
    params: dict[str, Any] = field(default_factory=dict)


class ModelAdapter(ABC):
    def __init__(self, spec: ModelSpec):
        self.spec = spec
        self.name = spec.name
        self.family = spec.family
        self.vendor = spec.vendor
        self.role = spec.role
        self.system_prompt: str | None = None

    @abstractmethod
    def generate(
        self, item: dict, gold: dict, *, arm: str, system: str | None = None,
        rollout: int = 0,
    ) -> dict:
        ...

    @abstractmethod
    def probe_notice(
        self, item: dict, gold: dict, *, arm: str, prior_text: str,
        system: str | None = None, rollout: int = 0,
    ) -> dict:
        ...


def render_prompt(item: dict, arm: str) -> str:
    if arm not in item["arm_rules"]:
        raise KeyError(f"item {item['id']} has no arm {arm}")
    inventory = item["rule_inventory"]
    lines = [
        item["scenario"].strip(), "", "Rules for this version:",
        *[f"- {rule}" for rule in inventory["stated_rules"]],
    ]
    addition = item["arm_rules"][arm].strip()
    if addition:
        lines.append(f"- {addition}")
    lines.extend(["", f"Task: {item['task'].strip()}"])
    return "\n".join(lines)


class AnthropicModel(ModelAdapter):
    def generate(self, item, gold, *, arm, system=None, rollout=0):
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError("AnthropicModel requires ANTHROPIC_API_KEY")
        import anthropic
        client = anthropic.Anthropic(api_key=key)
        if system is None:
            raise RuntimeError("UNFENCED live adapter requires the frozen neutral system prompt")
        msg = client.messages.create(
            model=self.spec.model_id or "claude-sonnet-4-6",
            max_tokens=int(self.spec.params.get("max_tokens", 1024)),
            temperature=float(self.spec.params.get("temperature", 1.0)),
            system=system,
            messages=[{"role": "user", "content": render_prompt(item, arm)}],
        )
        return {
            "text": "".join(block.text for block in msg.content if getattr(block, "type", "") == "text"),
            "intended": None,
        }

    def probe_notice(self, item, gold, *, arm, prior_text, system=None, rollout=0):
        raise RuntimeError(
            "Anthropic noticing probe is latched until its post-episode prompt and judge are validated"
        )


class OpenAIModel(ModelAdapter):
    def generate(self, item, gold, *, arm, system=None, rollout=0):
        raise NotImplementedError(
            "OpenAIModel is a portable live stub. Install/configure the OpenAI SDK and "
            "implement this adapter before a credentialed UNFENCED run."
        )

    def probe_notice(self, item, gold, *, arm, prior_text, system=None, rollout=0):
        raise NotImplementedError("OpenAI noticing probe is a live stub")


def load_roster(config: dict) -> dict[str, list[ModelAdapter]]:
    try:
        from .synthetic_reference import SyntheticModel, load_reference  # type: ignore
    except ImportError:
        from synthetic_reference import SyntheticModel, load_reference  # type: ignore

    roles = config.get("roles")
    if not isinstance(roles, dict) or not roles:
        raise ValueError("roles must be a non-empty mapping")
    reference_path = config["paths"]["synthetic_reference"]
    system_path = Path(config["paths"]["system_prompt"])
    if not system_path.is_file():
        raise FileNotFoundError(f"frozen neutral system prompt missing: {system_path}")
    system_prompt = system_path.read_text(encoding="utf-8").strip()
    if not system_prompt:
        raise ValueError(f"frozen neutral system prompt is empty: {system_path}")
    if any(s.get("adapter") == "synthetic" for specs in roles.values() for s in specs):
        load_reference(reference_path, expected_design=config["design"])

    roster: dict[str, list[ModelAdapter]] = {}
    families: dict[str, set[str]] = {}
    vendors: dict[str, set[str]] = {}
    for role, raw_specs in roles.items():
        roster[role] = []
        for raw in raw_specs:
            spec_data = dict(raw)
            for label in ("name", "family", "vendor", "adapter"):
                if not str(spec_data.get(label, "")).strip():
                    raise ValueError(f"model in role {role} lacks non-empty {label}")
            params = dict(spec_data.get("params") or {})
            if spec_data["adapter"] == "synthetic":
                params["reference_path"] = reference_path
                if not spec_data.get("profile"):
                    raise ValueError(f"synthetic model {spec_data['name']} lacks explicit profile")
            spec_data["params"] = params
            spec = ModelSpec(role=role, **spec_data)
            families.setdefault(spec.family.strip().casefold(), set()).add(role)
            vendors.setdefault(spec.vendor.strip().casefold(), set()).add(role)
            classes = {
                "synthetic": SyntheticModel,
                "anthropic": AnthropicModel,
                "openai": OpenAIModel,
            }
            if spec.adapter not in classes:
                raise ValueError(f"unknown adapter {spec.adapter!r}")
            adapter = classes[spec.adapter](spec)
            adapter.system_prompt = system_prompt
            roster[role].append(adapter)

    family_overlap = {k: sorted(v) for k, v in families.items() if len(v) > 1}
    if family_overlap:
        raise SystemExit(f"ROLE-FAMILY OVERLAP: {family_overlap}")
    if config["mode"] == "live":
        vendor_overlap = {k: sorted(v) for k, v in vendors.items() if len(v) > 1}
        if vendor_overlap:
            raise SystemExit(f"ROLE-VENDOR OVERLAP: {vendor_overlap}")
    return roster
