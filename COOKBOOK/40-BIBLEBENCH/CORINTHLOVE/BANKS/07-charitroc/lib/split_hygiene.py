"""Reportable three-way normalized-core shingle hygiene audit."""
from __future__ import annotations

from collections import defaultdict
import re

from lib import surfaces


SPLITS = ("public", "calibration", "private")
SPLIT_PAIRS = (
    ("public", "calibration"),
    ("public", "private"),
    ("calibration", "private"),
)
STAGES = ("stage_1", "stage_2", "stage_3", "stage_4")


def _wrapper_literals() -> tuple:
    templates = (
        surfaces.PUBLIC_TEMPLATES + surfaces.CALIBRATION_TEMPLATES
        + surfaces.PRIVATE_TEMPLATES
    )
    values = {surfaces.RESPONSE_FORMAT}
    for template in templates:
        for stage in STAGES:
            values.update(
                fragment
                for fragment in re.split(
                    r"\{[a-z0-9_]+\}", template[stage]
                )
                if fragment.strip()
            )
    return tuple(sorted(values, key=len, reverse=True))


WRAPPER_LITERALS = _wrapper_literals()


def normalized_core(text: str) -> str:
    core = text
    for literal in WRAPPER_LITERALS:
        core = core.replace(literal, " ")
    return surfaces.normalized_skeleton(core)


def four_token_shingles(text: str) -> set:
    tokens = re.findall(r"[a-z<>]+", text.lower())
    return {
        tuple(tokens[index:index + 4])
        for index in range(max(0, len(tokens) - 3))
    }


def containment(left: str, right: str) -> float:
    left_shingles = four_token_shingles(left)
    right_shingles = four_token_shingles(right)
    if not left_shingles or not right_shingles:
        return 0.0
    return len(left_shingles & right_shingles) / min(
        len(left_shingles), len(right_shingles)
    )


def _set_containment(left: set, right: set) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / min(len(left), len(right))


def audit_cross_split_shingles(episodes: list,
                               threshold: float = 0.25) -> dict:
    if not 0.0 < threshold <= 1.0:
        raise ValueError("threshold must lie in (0, 1]")
    grouped = defaultdict(list)
    for episode in episodes:
        grouped[(episode["template_family"], episode["split"])].append(
            episode
        )
    max_overlap = {
        f"{left}|{right}": 0.0 for left, right in SPLIT_PAIRS
    }
    violations = []
    comparisons = 0
    families = sorted({episode["template_family"] for episode in episodes})
    cached = {}
    for episode in episodes:
        for stage in STAGES:
            core = normalized_core(episode["multiturn_script"][stage])
            cached[(episode["id"], stage)] = (
                core, four_token_shingles(core)
            )
    for family in families:
        for split in SPLITS:
            assert grouped[(family, split)], (
                f"missing {family}/{split} rows in shingle audit"
            )
        for left_split, right_split in SPLIT_PAIRS:
            pair_name = f"{left_split}|{right_split}"
            for left in grouped[(family, left_split)]:
                for right in grouped[(family, right_split)]:
                    for stage in STAGES:
                        left_core, left_shingles = cached[(left["id"], stage)]
                        right_core, right_shingles = cached[(right["id"], stage)]
                        overlap = _set_containment(
                            left_shingles, right_shingles
                        )
                        comparisons += 1
                        max_overlap[pair_name] = max(
                            max_overlap[pair_name], overlap
                        )
                        if overlap >= threshold:
                            violations.append({
                                "split_pair": pair_name,
                                "family": family,
                                "stage": stage,
                                "left_id": left["id"],
                                "right_id": right["id"],
                                "overlap": overlap,
                                "left_core": left_core,
                                "right_core": right_core,
                            })
    return {
        "threshold": threshold,
        "width": 4,
        "comparisons": comparisons,
        "max_overlap": max_overlap,
        "violations": violations,
    }
