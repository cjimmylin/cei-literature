#!/usr/bin/env python
"""Approved shadow-judge bakeoff runner."""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from format_bridge_requal import (
    BudgetGuard,
    CapturingClient,
    JsonlSink,
    OutputPathError,
    PreflightError,
    fetch_with_two_retries,
    require_preflight,
)
from wcfbench import load_items, mvp
from wcfbench.contested import _score_disclosure, score_settled_core
from wcfbench.judge import (
    award_emission_count,
    build_award_prompt,
    complete_with_retry,
    parse_award_verdict,
    willingness_to_grade,
)
from wcfbench.openrouter_client import OpenRouterModelClient
from wcfbench.qualification import (
    DEFAULT_K,
    DEFAULT_THRESHOLD,
    PROBES,
    JudgeQualification,
    current_template_hashes,
    load_manifest,
    qualify_judge,
)
from wcfbench.triaxial import AXES, TriaxialScore, _score_numeric_axis


HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.normpath(os.path.join(HERE, ".."))
RUN_DIR = os.path.join(PROJECT, "07-PILOTS", "20260712-shadow-judge-bakeoff")
MANIFEST_PATH = os.path.join(
    PROJECT,
    "07-PILOTS",
    "20260712-artifact-corrected-requal",
    "20260712-artifact-corrected-requal-manifest.json",
)
OPEN_PATH = os.path.join(
    PROJECT,
    "07-PILOTS",
    "20260712-mvp-open-reparse",
    "corrected-open-transcripts.jsonl",
)
FLOOR_PATH = os.path.join(
    PROJECT, "07-PILOTS", "20260710-floor-rerun", "transcripts.jsonl"
)
R33_PATH = os.path.join(
    PROJECT, "07-PILOTS", "20260710-r33-3judge", "transcripts.jsonl"
)
BANK_DIR = os.path.join(PROJECT, "05-BANK-YAML")

CANDIDATES = (
    ("glm-5.2", "z-ai", "z-ai/glm-5.2"),
    ("deepseek-v4-pro", "deepseek", "deepseek/deepseek-v4-pro"),
)
SURFACE_COUNTS = {
    "open_award": 8,
    "coherence": 8,
    "disclosure": 6,
    "settled_core": 6,
}
K = DEFAULT_K
THRESHOLD = DEFAULT_THRESHOLD
MAX_BUDGET = 1.0
JUDGE_MAX_TOKENS = 2048
SEED = 1647


def read_jsonl(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _usable(record: Dict[str, Any]) -> bool:
    return bool(record.get("sut_response")) and bool(record.get("judges"))


def select_contested_records(floor, r33, *, expected=6):
    chosen = {}
    for source_name, records in (("floor-rerun", floor), ("r33-3judge", r33)):
        for record in records:
            if record.get("kind") != "contested" or not _usable(record):
                continue
            key = (str(record["item_id"]), str(record["model"]))
            if key not in chosen:
                copied = dict(record)
                copied["source_run"] = source_name
                chosen[key] = copied
    if len(chosen) != expected:
        raise PreflightError(
            f"expected {expected} unique contested units, found {len(chosen)}"
        )
    return [chosen[key] for key in sorted(chosen)]


def take_seeded(surface, rows, count):
    ordered = sorted(
        rows,
        key=lambda row: hashlib.sha256(
            f"{SEED}|{surface}|{row['item_id']}|{row['model']}".encode()
        ).hexdigest(),
    )
    if len(ordered) < count:
        raise PreflightError(f"{surface}: need {count} units, found {len(ordered)}")
    return ordered[:count]
