"""Config-driven roster loading (config/p0-roster.yaml).

Loads YAML (pyyaml is in the vault venv) or JSON, and exposes the enabled subject list. The
roster is the single source of truth for which vendors/models are on and which are
present-but-disabled (Gemini).
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional


def load_roster(path: str) -> Dict[str, Any]:
    """Load a roster from .yaml/.yml (pyyaml) or .json."""
    ext = os.path.splitext(path)[1].lower()
    with open(path, "r") as fh:
        if ext in (".yaml", ".yml"):
            import yaml  # deferred; pyyaml is installed in the venv

            return yaml.safe_load(fh)
        if ext == ".json":
            return json.load(fh)
    # unknown extension: try YAML then JSON
    text = open(path, "r").read()
    try:
        import yaml

        return yaml.safe_load(text)
    except Exception:
        return json.loads(text)


def enabled_models(roster: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Flat list of enabled subject models: {id, label, vendor, judge_eligible, ...}.

    A model is enabled only if BOTH its vendor block and its own `enabled` flag are true.
    """
    out: List[Dict[str, Any]] = []
    for vendor, block in (roster.get("vendors") or {}).items():
        if not block.get("enabled"):
            continue
        for m in block.get("models", []):
            if not m.get("enabled"):
                continue
            entry = dict(m)
            entry["vendor"] = vendor
            out.append(entry)
    return out


def all_models(roster: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Every model in the roster (enabled or not), each tagged with its vendor + vendor_enabled."""
    out: List[Dict[str, Any]] = []
    for vendor, block in (roster.get("vendors") or {}).items():
        for m in block.get("models", []):
            entry = dict(m)
            entry["vendor"] = vendor
            entry["vendor_enabled"] = bool(block.get("enabled"))
            out.append(entry)
    return out


def vendor_of(roster: Dict[str, Any], model_id: str) -> Optional[str]:
    for m in all_models(roster):
        if m["id"] == model_id:
            return m["vendor"]
    return None


def adapter_kwargs_for(roster: Dict[str, Any], vendor: str) -> Dict[str, Any]:
    """Per-vendor adapter construction kwargs derived from the roster config, passed straight to
    ``runner.adapters.build_adapter(vendor, **kwargs)``.

    The roster is the single source of truth for the OpenAI backend (§3.5 cross-family): its openai
    vendor block carries a ``backend`` selector (api | openrouter | codex) plus an optional
    ``auth.base_url`` / ``auth.env`` that override the backend preset. Only the OpenAI vendor takes
    such kwargs today — anthropic/google return ``{}`` (their build_adapter branches accept no
    backend/base_url), so this stays a no-op for them and does not disturb the frozen Anthropic path.
    """
    if vendor.lower() != "openai":
        return {}
    block = (roster.get("vendors") or {}).get(vendor, {}) or {}
    out: Dict[str, Any] = {}
    backend = block.get("backend")
    if backend:
        out["backend"] = backend
    auth = block.get("auth") or {}
    if auth.get("base_url"):
        out["base_url"] = auth["base_url"]
    if auth.get("env"):
        out["api_key_env"] = auth["env"]
    return out
