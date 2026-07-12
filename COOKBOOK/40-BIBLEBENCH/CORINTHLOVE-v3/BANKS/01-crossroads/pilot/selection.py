"""Deterministic six-item constrained set cover for public qualification."""
from __future__ import annotations

from itertools import combinations
import os
from pathlib import Path

from .contracts import assert_artifact_safe, assert_sha256, canonical_bytes


CLAUSES = tuple(f"C{index}" for index in range(1, 17))
FALLBACK_FAMILIES = {
    "capability-vs-love": {"C1"},
    "patience-kindness": {"C2", "C3"},
    "status": {"C4", "C5", "C7"},
    "truth-dignity": {"C6", "C10", "C11"},
    "protective-trust": {"C12", "C13", "C14"},
    "endurance-humility": {"C15", "C16"},
}


def _coverage(episode: dict, truth: dict) -> tuple[set, set, set]:
    clauses = set(truth.get("clauses", []))
    if not clauses <= set(CLAUSES) or not clauses:
        raise ValueError("public sidecar clauses are invalid")
    families = {
        family for family, members in FALLBACK_FAMILIES.items()
        if clauses & members
    }
    tools = episode.get("tools")
    if not isinstance(tools, list) or not tools:
        raise ValueError("public substrate tools are absent")
    substrates = set()
    for tool in tools:
        if not isinstance(tool, dict) or not isinstance(tool.get("name"), str):
            raise ValueError("public substrate tool is invalid")
        substrates.add(tool["name"])
    return clauses, families, substrates


def select_canary_ids(episodes: list, ground_truth: dict) -> list[str]:
    """Return the lexicographically first complete six-item public set cover."""
    if not isinstance(episodes, list) or len(episodes) < 6:
        raise ValueError("at least six public episodes are required")
    rows = {}
    for episode in episodes:
        if not isinstance(episode, dict) or episode.get("split") != "public":
            raise ValueError("canary selection accepts public episodes only")
        item_id = episode.get("id")
        truth = ground_truth.get(item_id)
        if not isinstance(item_id, str) or not isinstance(truth, dict) or truth.get(
                "split") != "public":
            raise ValueError("canary selection requires public sidecar rows")
        if item_id in rows:
            raise ValueError("public episode IDs must be unique")
        rows[item_id] = _coverage(episode, truth)
    required_substrates = set().union(*(row[2] for row in rows.values()))
    for candidate in combinations(sorted(rows), 6):
        clauses = set().union(*(rows[item][0] for item in candidate))
        families = set().union(*(rows[item][1] for item in candidate))
        substrates = set().union(*(rows[item][2] for item in candidate))
        if (
            clauses == set(CLAUSES)
            and families == set(FALLBACK_FAMILIES)
            and substrates == required_substrates
        ):
            return list(candidate)
    raise ValueError("no complete six-item set cover exists")


def _write_create_only(path: Path, payload: dict) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    assert_artifact_safe(payload)
    data = canonical_bytes(payload)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def build_canary_selection(episodes: list, ground_truth: dict,
                           *, bank_sha256: str) -> dict:
    selected = select_canary_ids(episodes, ground_truth)
    by_id = {row["id"]: row for row in episodes}
    clauses, families, substrates = set(), set(), set()
    for item_id in selected:
        covered = _coverage(by_id[item_id], ground_truth[item_id])
        clauses.update(covered[0]); families.update(covered[1]); substrates.update(covered[2])
    return {
        "selection_version": "crossroads-public-canary-v1",
        "purpose": "public qualification",
        "item_ids": selected,
        "tie_break": "lexicographic item ID",
        "bank_sha256": assert_sha256(bank_sha256, "bank_sha256"),
        "coverage": {
            "clauses": list(CLAUSES),
            "fallback_families": sorted(families),
            "substrates": sorted(substrates),
        },
        "authorizes_private_execution": False,
        "authorizes_calibration": False,
        "authorizes_freeze": False,
    }


def freeze_canary_selection(path: Path, episodes: list, ground_truth: dict,
                            *, bank_sha256: str) -> dict:
    payload = build_canary_selection(
        episodes, ground_truth, bank_sha256=bank_sha256
    )
    _write_create_only(Path(path), payload)
    return payload
