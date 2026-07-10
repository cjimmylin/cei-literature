"""Item-record YAML loader — validates against the spine §10 schema.

Loads item records from a single YAML file or a directory of them, validates
every required field, and returns typed dataclasses. Fails LOUD (raises
``LoaderError`` with a field-level message) on any malformed item — a
schema-lint failure is a Phase-2 gate, so silent coercion is forbidden.

Spine §10 item-record schema (authoritative):

    id: <DESIGN>-<commandment>-<serial>
    design: dutybound | complicit | ... | narrowgate
    track: A | B
    tier: T1 | T2 | T3 | T4          (T2a / T2b sub-tiers accepted)
    commandments: [primary, secondary...]
    anchors:
      - 'WLC Q145 — "undue silence in a just cause" (proof: Lev 5:1)'
    stem: |
    key: |
    rubric:
      - {points: 1, criterion: "...", anchor: "WLC Q145"}
    difficulty_reservoir: <named reservoir + rationale>
    perturbations: [P1a, P1b, P3, ...]
    failure_notes: |
    status: exemplar | expanded | reviewed | released
    author: fable | opus
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

import yaml


class LoaderError(ValueError):
    """Raised when an item record violates the spine §10 schema."""


# --- allowed enumerations (spine §10 + §2/§3) -------------------------------
VALID_TRACKS = {"A", "B"}
# Base tiers plus the T2a/T2b applied sub-tiers used in the real item banks.
VALID_TIERS = {"T1", "T2", "T2a", "T2b", "T3", "T4"}
VALID_STATUS = {"exemplar", "expanded", "reviewed", "released"}
VALID_AUTHOR = {"fable", "opus"}
# R24: the three triaxial axes a rubric keypoint may be tagged to. A tagged OPEN
# rubric drives the per-keypoint award scorer (each axis fraction is computed
# mechanically from the keypoints tagged to it); untagged keypoints (axis=None)
# fall back to the hardened numeric axis prompt. Only these three are valid.
VALID_AXES = {"matter", "manner", "end"}

# Required top-level fields per the build brief.
REQUIRED_FIELDS = (
    "id",
    "design",
    "track",
    "tier",
    "commandments",
    "anchors",
    "stem",
    "key",
    "rubric",
    "status",
    "author",
)


@dataclass
class RubricKeypoint:
    """One decomposed, anchor-tied rubric keypoint (spine §4.1).

    ``axis`` (R24) tags an OPEN keypoint to one triaxial axis (matter|manner|end)
    so the per-keypoint award scorer can compute each axis fraction mechanically;
    ``None`` = untagged (the hardened numeric-axis fallback handles it).
    """

    points: float
    criterion: str
    anchor: Optional[str] = None
    axis: Optional[str] = None


@dataclass
class ItemRecord:
    """A validated item record (spine §10)."""

    id: str
    design: str
    track: str
    tier: str
    commandments: List[str]
    anchors: List[str]
    stem: str
    key: str
    rubric: List[RubricKeypoint]
    status: str
    author: str
    # Optional / descriptive fields.
    difficulty_reservoir: Optional[str] = None
    perturbations: List[str] = field(default_factory=list)
    failure_notes: Optional[str] = None
    # Anything extra the spec carries (e.g. gold ordinal keys) is preserved.
    extra: Dict[str, Any] = field(default_factory=dict)

    @property
    def total_points(self) -> float:
        """Sum of all rubric keypoint points (the item's max score)."""
        return sum(kp.points for kp in self.rubric)


def _require(cond: bool, msg: str) -> None:
    if not cond:
        raise LoaderError(msg)


def _validate_rubric(raw_rubric: Any, item_id: str) -> List[RubricKeypoint]:
    _require(
        isinstance(raw_rubric, list) and len(raw_rubric) > 0,
        f"[{item_id}] 'rubric' must be a non-empty list, got {type(raw_rubric).__name__}",
    )
    keypoints: List[RubricKeypoint] = []
    for i, kp in enumerate(raw_rubric):
        _require(
            isinstance(kp, dict),
            f"[{item_id}] rubric[{i}] must be a mapping, got {type(kp).__name__}",
        )
        _require(
            "points" in kp,
            f"[{item_id}] rubric[{i}] is missing required key 'points'",
        )
        pts = kp["points"]
        _require(
            isinstance(pts, (int, float)) and not isinstance(pts, bool),
            f"[{item_id}] rubric[{i}] 'points' must be numeric, got {pts!r}",
        )
        _require(
            pts >= 0,
            f"[{item_id}] rubric[{i}] 'points' must be non-negative, got {pts!r}",
        )
        criterion = kp.get("criterion", "")
        _require(
            isinstance(criterion, str) and criterion.strip() != "",
            f"[{item_id}] rubric[{i}] must carry a non-empty 'criterion'",
        )
        anchor = kp.get("anchor")
        _require(
            anchor is None or isinstance(anchor, str),
            f"[{item_id}] rubric[{i}] 'anchor' must be a string if present",
        )
        axis = kp.get("axis")
        _require(
            axis is None or (isinstance(axis, str) and axis in VALID_AXES),
            f"[{item_id}] rubric[{i}] 'axis' must be one of {sorted(VALID_AXES)} if present, got {axis!r}",
        )
        keypoints.append(
            RubricKeypoint(points=float(pts), criterion=criterion, anchor=anchor, axis=axis)
        )
    return keypoints


def _validate_record(raw: Any, source: str) -> ItemRecord:
    _require(
        isinstance(raw, dict),
        f"[{source}] item record must be a YAML mapping, got {type(raw).__name__}",
    )

    # id first, so every later message can name the item.
    item_id = raw.get("id")
    _require(
        isinstance(item_id, str) and item_id.strip() != "",
        f"[{source}] item is missing a non-empty 'id'",
    )

    missing = [f for f in REQUIRED_FIELDS if f not in raw]
    _require(
        not missing,
        f"[{item_id}] missing required field(s): {', '.join(missing)}",
    )

    design = raw["design"]
    _require(
        isinstance(design, str) and design.strip() != "",
        f"[{item_id}] 'design' must be a non-empty string",
    )

    track = raw["track"]
    _require(
        track in VALID_TRACKS,
        f"[{item_id}] 'track' must be one of {sorted(VALID_TRACKS)}, got {track!r}",
    )

    tier = raw["tier"]
    _require(
        tier in VALID_TIERS,
        f"[{item_id}] 'tier' must be one of {sorted(VALID_TIERS)}, got {tier!r}",
    )

    commandments = raw["commandments"]
    _require(
        isinstance(commandments, list) and len(commandments) > 0,
        f"[{item_id}] 'commandments' must be a non-empty list (primary first)",
    )

    anchors = raw["anchors"]
    _require(
        isinstance(anchors, list) and len(anchors) > 0,
        f"[{item_id}] 'anchors' must be a non-empty list (spine §10: ≥1 registry anchor)",
    )
    _require(
        all(isinstance(a, str) and a.strip() != "" for a in anchors),
        f"[{item_id}] every anchor must be a non-empty string",
    )

    stem = raw["stem"]
    _require(
        isinstance(stem, str) and stem.strip() != "",
        f"[{item_id}] 'stem' must be a non-empty string",
    )

    key = raw["key"]
    _require(
        isinstance(key, str) and key.strip() != "",
        f"[{item_id}] 'key' must be a non-empty string",
    )

    status = raw["status"]
    _require(
        status in VALID_STATUS,
        f"[{item_id}] 'status' must be one of {sorted(VALID_STATUS)}, got {status!r}",
    )

    author = raw["author"]
    _require(
        author in VALID_AUTHOR,
        f"[{item_id}] 'author' must be one of {sorted(VALID_AUTHOR)}, got {author!r}",
    )

    rubric = _validate_rubric(raw["rubric"], item_id)

    perturbations = raw.get("perturbations", []) or []
    _require(
        isinstance(perturbations, list),
        f"[{item_id}] 'perturbations' must be a list if present",
    )

    known = set(REQUIRED_FIELDS) | {
        "difficulty_reservoir",
        "perturbations",
        "failure_notes",
    }
    extra = {k: v for k, v in raw.items() if k not in known}

    return ItemRecord(
        id=item_id,
        design=design,
        track=track,
        tier=tier,
        commandments=[str(c) for c in commandments],
        anchors=list(anchors),
        stem=stem,
        key=key,
        rubric=rubric,
        status=status,
        author=author,
        difficulty_reservoir=raw.get("difficulty_reservoir"),
        perturbations=[str(p) for p in perturbations],
        failure_notes=raw.get("failure_notes"),
        extra=extra,
    )


def _load_yaml_docs(path: str) -> List[Any]:
    """Load one YAML file; supports either a single mapping or a list of them,
    and multi-document (``---``-separated) files."""
    with open(path, "r", encoding="utf-8") as fh:
        docs = list(yaml.safe_load_all(fh))
    records: List[Any] = []
    for doc in docs:
        if doc is None:
            continue
        if isinstance(doc, list):
            records.extend(doc)
        else:
            records.append(doc)
    return records


def load_item(path: str) -> ItemRecord:
    """Load and validate a single-record YAML file. Raises ``LoaderError``."""
    docs = _load_yaml_docs(path)
    _require(len(docs) == 1, f"[{path}] expected exactly one item record, found {len(docs)}")
    return _validate_record(docs[0], os.path.basename(path))


def load_items(path: str) -> List[ItemRecord]:
    """Load and validate item records from a file or a directory of ``*.yaml``.

    A file may hold one record or a list of records. A directory is scanned
    (sorted) for ``*.yaml`` / ``*.yml`` files. Raises ``LoaderError`` on the
    FIRST malformed record — schema-lint is fail-loud (Phase-2 gate).
    """
    records: List[ItemRecord] = []
    if os.path.isdir(path):
        names = sorted(
            n for n in os.listdir(path) if n.endswith((".yaml", ".yml"))
        )
        _require(names, f"[{path}] directory contains no .yaml/.yml files")
        for name in names:
            fpath = os.path.join(path, name)
            for raw in _load_yaml_docs(fpath):
                records.append(_validate_record(raw, name))
    else:
        for raw in _load_yaml_docs(path):
            records.append(_validate_record(raw, os.path.basename(path)))
    return records
