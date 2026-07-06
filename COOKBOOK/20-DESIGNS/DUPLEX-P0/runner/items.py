"""Item-bank loader: normalize the authored P0 bank into the runner's minimal record shape.

The authored bank (items/20260706-p0-item-bank.json) is produced by a separate agent and uses
its own richer schema (`id`, `base_prompt`, `resource_condition_variants`,
`is_discriminant_control`, monitored/unmonitored variants, canaries, ...). This module maps it
to the {item_id, text, axis, condition_prompts, ...} shape the orchestrator consumes, WITHOUT
the runner or its tests depending on the file existing (the tests use an in-memory fixture bank).

OPEN MAPPING ITEM (documented in README): the design's G1 "content-axis matched baseline"
(axis == "content") is NOT the same as the §5 non-moral discriminant-control battery. This bank
labels the latter via `is_discriminant_control`; it does not designate a separate content-
instrument axis. The analyst must designate which records constitute G1's content baseline
(a matched content-benchmark run on the same models, or a relabelled subset) before running G1.
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional

DEFAULT_BANK_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "items",
    "20260706-p0-item-bank.json",
)


def normalize_item(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Map one authored item dict to the runner's minimal record shape (original kept under 'raw')."""
    text = raw.get("text") or raw.get("base_prompt")
    if not text:
        scenario = raw.get("scenario", "") or ""
        question = raw.get("question", "") or ""
        text = (scenario + "\n\n" + question).strip()

    axis = raw.get("axis")
    if axis is None:
        # best-effort; see OPEN MAPPING ITEM in the module docstring re: G1 content baseline.
        axis = "discriminant_control" if raw.get("is_discriminant_control") else "process"

    return {
        "item_id": raw.get("item_id") or raw.get("id"),
        "text": text,
        "axis": axis,
        "condition_prompts": raw.get("resource_condition_variants") or {},
        "person": raw.get("person"),
        "content_tags": raw.get("content_tags"),
        "greene_subset": raw.get("greene_subset"),
        "greene_probe_type": raw.get("greene_probe_type"),
        "is_contamination_probe": raw.get("is_contamination_probe"),
        "is_discriminant_control": raw.get("is_discriminant_control"),
        "monitored_variant": raw.get("monitored_variant"),
        "unmonitored_variant": raw.get("unmonitored_variant"),
        "canary": raw.get("canary"),
        "raw": raw,
    }


def load_item_bank(path: Optional[str] = None) -> List[Dict[str, Any]]:
    """Load + normalize the authored bank. `data` may be {"items": [...]} or a bare list."""
    path = path or DEFAULT_BANK_PATH
    with open(path, "r") as fh:
        data = json.load(fh)
    items = data["items"] if isinstance(data, dict) and "items" in data else data
    return [normalize_item(it) for it in items]
