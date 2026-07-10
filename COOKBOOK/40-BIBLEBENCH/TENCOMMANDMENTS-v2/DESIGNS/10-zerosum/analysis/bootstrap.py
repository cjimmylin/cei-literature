"""Deterministic scenario-core cluster bootstrap helpers."""

from __future__ import annotations

from copy import deepcopy
import random
from typing import Any, Dict, Mapping, Sequence


def resample_by_core(
    rows: Sequence[Mapping[str, Any]], *, seed: int
) -> Sequence[Dict[str, Any]]:
    """Sample core IDs with replacement while retaining every sibling row."""

    grouped: Dict[str, list] = {}
    for source in rows:
        core_id = source.get("core_id")
        if not isinstance(core_id, str) or not core_id:
            raise ValueError("every bootstrap row requires core_id")
        grouped.setdefault(core_id, []).append(source)
    if not grouped:
        raise ValueError("cannot bootstrap an empty row set")
    core_ids = sorted(grouped)
    rng = random.Random(seed)
    sampled = []
    for draw_index in range(len(core_ids)):
        source_id = core_ids[rng.randrange(len(core_ids))]
        bootstrap_id = "%04d:%s" % (draw_index, source_id)
        for source in grouped[source_id]:
            row = deepcopy(dict(source))
            row["bootstrap_core_id"] = bootstrap_id
            sampled.append(row)
    return sampled


__all__ = ["resample_by_core"]
