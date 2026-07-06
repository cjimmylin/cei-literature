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
