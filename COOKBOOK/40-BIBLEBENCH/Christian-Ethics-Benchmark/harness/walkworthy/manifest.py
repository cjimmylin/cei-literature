"""Manifest schema + builder.

A run is fully described by `runs/<panel>/manifest.json`: item IDs only (never
item text — text is loaded from the versioned seed files at call time), the model
list, the judge pair, and FIXED permutation seeds (constants, never generated at
runtime — reproducibility, charter §6.6 perturbation reproducibility). This keeps
runs byte-reproducible and the manifest a compact audit record.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from .capability_battery import CAPABILITY_BATTERY
from .loader import load_public_split

# Fixed permutation seeds (frozen constants). Named per permutation axis the
# paired designs use; identical across runs so order effects are reproducible.
FIXED_PERMUTATION_SEEDS: Dict[str, int] = {
    "seat_order": 20260706,          # 09 seat A/B(/C) presentation order
    "twin_order": 20260706,          # 03 expressed/revealed, 08 covert/overt ordering
    "variant_order": 20260706,       # 10 N/U, 04 alpha/beta ordering
    "claimant_order": 20260706,      # 05 claimant presentation order within the ask
    "arbiter_placement": 20260706,   # 09 arbiter-probe placement
}


@dataclass
class Manifest:
    panel: str
    date_str: str
    designs: List[str]
    item_ids: List[str]
    models: List[dict]
    judges: List[dict]
    permutation_seeds: Dict[str, int]
    capability_battery: List[dict] = field(default_factory=list)
    notes: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    def write(self, path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")

    @classmethod
    def read(cls, path) -> "Manifest":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(**data)


def build_manifest(panel: str, date_str: str, benchmark_root,
                   models: List[dict], judges: List[dict],
                   designs: Optional[List[str]] = None,
                   include_exemplars: bool = True,
                   notes: str = "", items: Optional[List] = None) -> Manifest:
    """Build a manifest over the runnable PUBLIC split (IDs only).

    Cross-family judge guard: the two judges must be different families than each
    other and than the item-generator family (Fable/Opus). Enforced here.

    `items` (optional): an explicit, already-selected Item list (e.g. a panel
    pilot's 5-items/design subset). When given, the manifest records exactly those
    IDs + their designs — the loader is NOT re-read. `designs` still filters.
    """
    if items is None:
        items = load_public_split(benchmark_root, include_exemplars=include_exemplars,
                                  runnable_only=True)
    if designs:
        items = [it for it in items if it.design in set(designs)]
    item_ids = [it.id for it in items]
    used_designs = sorted({it.design for it in items})

    fams = [j.get("family") for j in judges]
    if len(judges) >= 2 and len(set(fams)) < 2:
        raise ValueError(f"judge pair must be cross-family; got families {fams}")

    return Manifest(
        panel=panel,
        date_str=date_str,
        designs=designs or used_designs,
        item_ids=item_ids,
        models=models,
        judges=judges,
        permutation_seeds=dict(FIXED_PERMUTATION_SEEDS),
        capability_battery=CAPABILITY_BATTERY,
        notes=notes,
    )
