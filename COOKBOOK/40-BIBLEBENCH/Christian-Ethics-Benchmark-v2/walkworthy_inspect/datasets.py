"""Load per-design SCHEMA.md JSONL banks into Inspect datasets.

Each JSONL line is one *administration* (SCHEMA.md): `id`, `input` (a list of
role/content messages), `target` (keyed behavior string for the judge), and `metadata`
carrying `keyed`, `multiturn`, `pair_id`, `runnable`, the canary, etc.

- `load_design(...)` builds a `MemoryDataset` via `record_to_sample`, filtering
  `runnable == false` items by default.
- Holdout access is guarded: `load_holdout(...)` raises `WalkworthyHoldoutError` unless
  `WALKWORTHY_ALLOW_HOLDOUT=1` (AGENTS.md rule 6 / v1 HoldoutAccessError convention).
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, List, Optional

from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.model import ChatMessageAssistant, ChatMessageSystem, ChatMessageUser

# Package lives in <v2>/walkworthy_inspect/ ; datasets live at <v2>/datasets/.
_PKG_DIR = Path(__file__).resolve().parent
_V2_ROOT = _PKG_DIR.parent
PUBLIC_DIR = _V2_ROOT / "datasets" / "public"
HOLDOUT_DIR = _V2_ROOT / "datasets" / "holdout"

CANARY = "WALKWORTHY-CANARY-7f3e2026"

# design slug -> file stem
DESIGN_SLUGS = {
    "01": "01-goodsamaritan", "02": "02-twomasters", "03": "03-quiettongue",
    "04": "04-innerweight", "05": "05-ordoamoris", "06": "06-crookedpath",
    "07": "07-seventyseven", "08": "08-vocationfork", "09": "09-doubleedge",
    "10": "10-strangergate",
}


class WalkworthyHoldoutError(RuntimeError):
    """Raised on any holdout access without WALKWORTHY_ALLOW_HOLDOUT=1."""


def _design_num(design: str) -> str:
    """Normalize '01', '1', '01-goodsamaritan' -> zero-padded '01'."""
    stem = str(design).split("-", 1)[0]
    return f"{int(stem):02d}"


def _role_message(role: str, content: str):
    if role == "system":
        return ChatMessageSystem(content=content)
    if role == "assistant":
        return ChatMessageAssistant(content=content)
    return ChatMessageUser(content=content)


def record_to_sample(record: dict) -> Sample:
    """Convert one SCHEMA.md JSONL line into an Inspect `Sample`.

    `input` is a list of {role, content}; we rebuild it as typed ChatMessages so the
    system prompt lands as a real system message. `metadata` is passed through intact
    (keyed, multiturn, pair_id, canary, ...) — the solver and scorer read from it.
    """
    raw_input = record.get("input", "")
    if isinstance(raw_input, list):
        messages: List[Any] = [
            _role_message(m.get("role", "user"), m.get("content", ""))
            for m in raw_input
        ]
        model_input: Any = messages
    else:
        model_input = str(raw_input)
    return Sample(
        id=record.get("id"),
        input=model_input,
        target=record.get("target", ""),
        metadata=record.get("metadata", {}) or {},
    )


def _resolve_dir(dataset_dir: Optional[str], default: Path) -> Path:
    """Resolve a dataset dir. Relative dirs are tried against CWD then the v2 root.

    Inspect runs task files from the task file's directory, so a `-T dataset_dir=...`
    passed relative to the v2 root would otherwise miss. We try CWD first, then v2 root.
    """
    if not dataset_dir:
        return default
    p = Path(dataset_dir)
    if p.is_absolute():
        return p
    if p.exists():
        return p.resolve()
    alt = _V2_ROOT / dataset_dir
    if alt.exists():
        return alt
    return p  # let the caller raise a clear FileNotFoundError


def _read_jsonl(path: Path) -> List[dict]:
    if not path.exists():
        raise FileNotFoundError(f"dataset file not found: {path}")
    rows: List[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def _build_dataset(rows: List[dict], design: str, include_nonrunnable: bool) -> MemoryDataset:
    samples: List[Sample] = []
    for rec in rows:
        meta = rec.get("metadata", {}) or {}
        if not include_nonrunnable and meta.get("runnable", True) is False:
            continue
        samples.append(record_to_sample(rec))
    return MemoryDataset(samples=samples, name=f"walkworthy-{design}")


def load_design(design: str, dataset_dir: Optional[str] = None,
                include_nonrunnable: bool = False) -> MemoryDataset:
    """Load the public bank for one design.

    Args:
      design: '01'..'10' or a full slug like '01-goodsamaritan'.
      dataset_dir: directory holding `designNN.jsonl` (default: <v2>/datasets/public).
      include_nonrunnable: keep `runnable:false` items (default: filter them out).
    """
    num = _design_num(design)
    base = _resolve_dir(dataset_dir, PUBLIC_DIR)
    path = base / f"design{num}.jsonl"
    rows = _read_jsonl(path)
    return _build_dataset(rows, num, include_nonrunnable)


def load_holdout(design: str, dataset_dir: Optional[str] = None,
                 include_nonrunnable: bool = False) -> MemoryDataset:
    """Load the HOLDOUT bank for one design. Guarded by WALKWORTHY_ALLOW_HOLDOUT=1."""
    if os.environ.get("WALKWORTHY_ALLOW_HOLDOUT") != "1":
        raise WalkworthyHoldoutError(
            "holdout access denied — set WALKWORTHY_ALLOW_HOLDOUT=1 to load holdout "
            "banks (AGENTS.md rule 6). Never include holdout items in committed "
            "reports or prompts."
        )
    num = _design_num(design)
    base = _resolve_dir(dataset_dir, HOLDOUT_DIR)
    path = base / f"design{num}.jsonl"
    rows = _read_jsonl(path)
    return _build_dataset(rows, num, include_nonrunnable)
