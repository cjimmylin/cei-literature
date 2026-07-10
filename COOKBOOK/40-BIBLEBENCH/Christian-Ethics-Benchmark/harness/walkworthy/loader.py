"""Load the WALKWORTHY PUBLIC split into normalized Items.

HARD RULE (charter §6.6): this loader loads the PUBLIC split ONLY —
DESIGNS/*-seeds.md (+ optional spec exemplars). It REFUSES any HOLDOUT/ path.
HOLDOUT is gitignored, contamination/perturbation use only, and must never
enter a public run.
"""
from __future__ import annotations

from pathlib import Path
from typing import List

from .builders import BUILDERS
from .models import Item
from .parsing import parse_raw_items

CANARY = "WALKWORTHY-CANARY-7f3e2026"

DESIGN_CODES = [
    "01-goodsamaritan", "02-twomasters", "03-quiettongue", "04-innerweight",
    "05-ordoamoris", "06-crookedpath", "07-seventyseven", "08-vocationfork",
    "09-doubleedge", "10-strangergate",
]


class HoldoutAccessError(RuntimeError):
    """Raised if anything tries to load a HOLDOUT path in a public run."""


def _guard_public(path: Path) -> None:
    parts = {p.upper() for p in path.parts}
    if "HOLDOUT" in parts:
        raise HoldoutAccessError(
            f"Refusing to load HOLDOUT path in a public run: {path} (charter §6.6)"
        )


def load_design(design: str, benchmark_root, include_exemplars: bool = True) -> List[Item]:
    """Load one design's PUBLIC items (seed bank + optional spec exemplars)."""
    if design not in DESIGN_CODES:
        raise ValueError(f"unknown design {design!r}")
    root = Path(benchmark_root)
    seed_path = root / "DESIGNS" / f"{design}-seeds.md"
    _guard_public(seed_path)
    if not seed_path.exists():
        raise FileNotFoundError(seed_path)

    builder = BUILDERS.get(design)
    if builder is None:
        raise NotImplementedError(f"no builder yet for {design}")

    raws = parse_raw_items(seed_path.read_text(encoding="utf-8"), str(seed_path))
    items = [builder(r, design) for r in raws]

    if include_exemplars:
        spec_path = root / "DESIGNS" / f"{design}.md"
        _guard_public(spec_path)
        if spec_path.exists():
            ex_raws = parse_raw_items(spec_path.read_text(encoding="utf-8"), str(spec_path))
            for r in ex_raws:
                ex = builder(r, design)
                ex.is_exemplar = True
                items.append(ex)
    for it in items:
        it.runnable = it.is_runnable()
    return items


def load_public_split(benchmark_root, include_exemplars: bool = True,
                      runnable_only: bool = False) -> List["Item"]:
    """Load the entire PUBLIC split across all 10 designs (never HOLDOUT)."""
    out: List[Item] = []
    for design in DESIGN_CODES:
        for it in load_design(design, benchmark_root, include_exemplars=include_exemplars):
            if runnable_only and not it.runnable:
                continue
            out.append(it)
    return out
