#!/usr/bin/env python
"""Convert the WCF-Benchmark v1 YAML item bank to Inspect AI JSONL datasets.

Reads all multi-document YAML files in WCF-Benchmark/05-BANK-YAML/ (read-only),
drops dev_set_only items, routes each item to a scorer kind (mirroring v1
wcfbench/routing.py precedence exactly), and writes two JSONL files:

    data/wcf_main.jsonl      — single-completion items (expected: 204)
    data/wcf_episodes.jsonl  — NARROWGATE agentic episodes (expected: 22)

Regenerable at any time; the bank YAML is the source of truth and is never
modified. Run from anywhere: paths resolve relative to this file.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

import yaml

from pressure_turns import PRESSURE_TURNS
from session4_patches import apply_patches
from session5_patches import apply_patches as apply_patches_s5

V2_ROOT = Path(__file__).resolve().parent.parent
BANK_DIR = V2_ROOT.parent / "WCF-Benchmark" / "05-BANK-YAML"
DATA_DIR = V2_ROOT / "data"
TEMPLATE_DIR = V2_ROOT / "src" / "templates"

# v2.2 bank-version manifest constants (design memo §3). GRADE_PATTERN and the
# panel default mirror src/wcf_grading.py + src/wcf_tasks.py; kept here as literals
# so the manifest is self-describing without importing the inspect_ai stack.
BANK_VERSION = "v2.2"
PATCH_LAYERS = ["session4_patches", "session5_patches"]
# Mirrors src/wcf_grading.py:GRADE_PATTERN (last-match, word-bounded, no 4-digit
# truncation). Kept as a literal so the manifest is self-describing without pulling
# the inspect_ai stack into the converter; a guard test asserts it stays in sync
# with the source of truth in src/wcf_grading.py.
GRADE_PATTERN = r"(?is).*(?<!\w)GRADE(?!\w)\s*:\s*(\d{1,3})(?!\d)"
PANEL_DEFAULT = (
    "openrouter/google/gemini-2.5-flash"
    ",openrouter/deepseek/deepseek-chat"
    ",openrouter/mistralai/mistral-small-2603"
)
MANIFEST_DATE = "2026-07-16"

REQUIRED_FIELDS = ("id", "design", "track", "tier", "commandments", "stem", "key", "rubric")

# v2 (session-4 patched bank): 5 CV-02 turn-conditioned items quarantined from
# the 204 v1 main items -> 199. Episodes unchanged.
EXPECTED_MAIN = 199
EXPECTED_EPISODES = 22


def scorer_kind(item: dict) -> str:
    """Routing kind — precedence ported from v1 wcfbench/routing.py:

    1. NARROWGATE (or any ``episode: true``) is episode.
    2. ``contested: true`` beats the ordinal branch (binding ruling: contested
       items are never scored as if their gold order were settled).
    3. AGGRAVATE with a ``gold_order`` is ordinal.
    4. PROOFTEXT is anchor.
    5. Everything else is open (the safe fallback: no format ask).
    """
    design = (item.get("design") or "").strip().lower()
    if design == "narrowgate" or item.get("episode") is True:
        return "episode"
    if item.get("contested") is True:
        return "contested"
    if design == "aggravate" and item.get("gold_order") is not None:
        return "ordinal"
    if design == "prooftext":
        return "anchor"
    return "open"


def load_bank(bank_dir: Path = BANK_DIR) -> list[dict]:
    """Load every runnable item from the bank (dev_set_only excluded)."""
    items: list[dict] = []
    seen_ids: set[str] = set()
    for path in sorted(bank_dir.glob("*.yaml")):
        for doc in yaml.safe_load_all(path.read_text()):
            if doc is None:  # trailing '---' yields an empty document
                continue
            missing = [f for f in REQUIRED_FIELDS if f not in doc]
            if missing:
                raise ValueError(f"{path.name}: item {doc.get('id', '?')} missing {missing}")
            if doc["id"] in seen_ids:
                raise ValueError(f"{path.name}: duplicate id {doc['id']}")
            seen_ids.add(doc["id"])
            if doc.get("dev_set_only") is True:
                continue
            items.append(doc)
    return items


def to_record(item: dict) -> dict:
    """Reduce a bank item to the fields the Inspect tasks consume.

    Episode records additionally carry a per-item ``pressure_turn`` (v2.1): the
    second-turn user message voicing the item's highest cost dial, authored in
    ``convert/pressure_turns.py``. Non-episode records omit the field. The field
    is consumed OPT-IN by the ``wcf_episodes`` task (``pressure_variant=item``);
    default behavior ignores it.
    """
    record = {
        "id": item["id"],
        "design": item["design"],
        "track": item["track"],
        "tier": str(item["tier"]),
        "commandments": item["commandments"],
        "contested": item.get("contested") is True,
        "episode": item.get("episode") is True,
        "kind": scorer_kind(item),
        "stem": item["stem"],
        "key": item["key"],
        "rubric": item["rubric"],
        "gold_order": item.get("gold_order"),
    }
    # CG-03 (session-4 patch): recall-hybrid tag, carried into the JSONL so the
    # "conduct-only" framing is never overstated. Only present on tagged items.
    if item.get("recall_hybrid") is True:
        record["recall_hybrid"] = True
    if record["kind"] == "episode":
        turn = PRESSURE_TURNS.get(item["id"])
        if turn is None:
            raise ValueError(f"episode {item['id']} has no authored pressure_turn")
        record["pressure_turn"] = turn
    return record


def load_patched_bank(bank_dir: Path = BANK_DIR) -> list[dict]:
    """Load the v1 bank, then apply the session-4 patch layer, then session-5.

    Chain: v1 YAML (read-only) -> session4_patches.apply_patches (CV-02 quarantine
    + control-twin strip + CV-04/CG-02 decline gate + CV-03 anchor-text + CG-03
    recall tag) -> session5_patches.apply_patches (Lever B R1-R5 rubric repairs on
    12 AMBIG items + Lever C item-specific incommensurable-head-pair enumeration on
    the 3 contested items that carry a decline criterion). Quarantined items (CV-02)
    are dropped by session4 (return None) before session5 runs. The v1 source YAML
    is never modified.
    """
    patched: list[dict] = []
    for item in load_bank(bank_dir):
        out = apply_patches(item)
        if out is None:
            continue  # CV-02 quarantine (session4)
        out = apply_patches_s5(out)
        patched.append(out)
    return patched


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_manifest(data_dir: Path = DATA_DIR, template_dir: Path = TEMPLATE_DIR) -> dict:
    """Write ``data/BANK-VERSION.json`` (design memo §3 bank-versioning rule).

    Records the bank version, patch layers, sha256 of both emitted JSONL files,
    sha256 of both grading templates (original + excellence, Lever A), the grade
    pattern, the panel default, and the date. Must be called AFTER the JSONL files
    are emitted so the hashes match on disk.
    """
    manifest = {
        "bank_version": BANK_VERSION,
        "patch_layers": PATCH_LAYERS,
        "sha256_wcf_main": _sha256(data_dir / "wcf_main.jsonl"),
        "sha256_wcf_episodes": _sha256(data_dir / "wcf_episodes.jsonl"),
        "sha256_grading_template_original": _sha256(
            template_dir / "wcf_grade_template.txt"
        ),
        "sha256_grading_template_excellence": _sha256(
            template_dir / "wcf_grade_template_excellence.txt"
        ),
        "grade_pattern": GRADE_PATTERN,
        "panel": PANEL_DEFAULT,
        "date": MANIFEST_DATE,
    }
    (data_dir / "BANK-VERSION.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    )
    return manifest


def convert(bank_dir: Path = BANK_DIR, data_dir: Path = DATA_DIR) -> tuple[int, int]:
    records = [to_record(item) for item in load_patched_bank(bank_dir)]
    main = [r for r in records if r["kind"] != "episode"]
    episodes = [r for r in records if r["kind"] == "episode"]

    data_dir.mkdir(parents=True, exist_ok=True)
    for name, rows in (("wcf_main.jsonl", main), ("wcf_episodes.jsonl", episodes)):
        with open(data_dir / name, "w") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    write_manifest(data_dir)
    return len(main), len(episodes)


if __name__ == "__main__":
    n_main, n_episodes = convert()
    print(f"wcf_main.jsonl: {n_main} items (expected {EXPECTED_MAIN})")
    print(f"wcf_episodes.jsonl: {n_episodes} items (expected {EXPECTED_EPISODES})")
    if (n_main, n_episodes) != (EXPECTED_MAIN, EXPECTED_EPISODES):
        raise SystemExit("COUNT MISMATCH — do not run evals until resolved")
    print("data/BANK-VERSION.json written")
    print("OK")
