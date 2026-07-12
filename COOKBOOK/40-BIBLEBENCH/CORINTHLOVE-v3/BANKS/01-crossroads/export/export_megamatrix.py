#!/usr/bin/env python3
"""Manifest-complete native C1-C16 episode-choice export."""
from __future__ import annotations

from copy import deepcopy
from itertools import product
import csv
import hashlib
import json
from pathlib import Path
import random

import yaml


BANK = Path(__file__).resolve().parents[1]
METHOD_ID = "01-crossroads"
CLAUSES = tuple(f"C{i}" for i in range(1, 17))
SCHEMA = [
    "model_id", "method_id", "item_family", "item_id", "clause",
    "score", "rung", "judge_ids", "mechanical_flag", "canary_id",
]
MOCK_LABEL = "harness validation, NOT a measurement"
MANIFEST_VERSION = "CROSSROADS-export-manifest-v1"
PUBLIC_EXCLUSION = "public qualification episode: not a sealed private measurement episode"
JUDGE_SENTINEL = "mechanical"


def _canonical(value) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False,
    ).encode()


def _sha(value) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _coverage_sha() -> str:
    return hashlib.sha256((BANK / "export/coverage_map.json").read_bytes()).hexdigest()


def _clause_mask(hidden: dict) -> tuple[str, ...]:
    path_keys = hidden.get("path_keys")
    if not isinstance(path_keys, dict) or not path_keys:
        raise ValueError("sidecar path_keys are required for export")
    clauses = set()
    for vector in path_keys.values():
        if not isinstance(vector, dict) or not vector:
            raise ValueError("every path needs a key vector")
        for clause, sign in vector.items():
            if clause not in CLAUSES or sign not in {-1, 0, 1}:
                raise ValueError("path key contains an invalid clause/sign")
            if sign:
                clauses.add(clause)
    if not clauses:
        raise ValueError("episode has no scored clauses")
    return tuple(sorted(clauses, key=lambda value: int(value[1:])))


def build_expected_manifest(episodes: dict, sidecar: dict,
                            expected_models) -> dict:
    models = list(expected_models)
    if (not models or len(models) != len(set(models))
            or any(not isinstance(model, str) or not model.strip() for model in models)):
        raise ValueError("expected_models must be explicit unique strings")
    if not isinstance(episodes, dict) or set(episodes) != set(sidecar):
        raise ValueError("episode/sidecar inventory mismatch")
    private_ids, exclusions, masks = [], [], {}
    for item_id, episode in episodes.items():
        if episode.get("id") != item_id:
            raise ValueError("episode dictionary key differs from item id")
        split = episode.get("split")
        if split == "private":
            private_ids.append(item_id)
            masks[item_id] = list(_clause_mask(sidecar[item_id]))
        elif split == "public":
            exclusions.append({"item_id": item_id, "reason": PUBLIC_EXCLUSION})
        else:
            raise ValueError("export bank contains an unknown split")
    private_ids.sort()
    exclusions.sort(key=lambda row: row["item_id"])
    if set(clause for values in masks.values() for clause in values) != set(CLAUSES):
        raise ValueError("private export does not cover all frozen C1-C16 clauses")
    expected = [
        {"model_id": model, "item_id": item_id, "clause": clause}
        for model in models for item_id in private_ids for clause in masks[item_id]
    ]
    body = {
        "manifest_version": MANIFEST_VERSION,
        "method_id": METHOD_ID,
        "coverage_map_sha256": _coverage_sha(),
        "expected_models": models,
        "bank_episode_ids": sorted(episodes),
        "expected_episode_ids": private_ids,
        "expected_episode_count": len(private_ids),
        "excluded_episode_count": len(exclusions),
        "exclusions": exclusions,
        "item_clause_masks": {key: masks[key] for key in sorted(masks)},
        "expected_rows": expected,
        "expected_row_count": len(expected),
    }
    body["manifest_sha256"] = _sha(body)
    return body


def _expected_keys(manifest: dict) -> list[tuple[str, str, str]]:
    if (manifest.get("manifest_version") != MANIFEST_VERSION
            or manifest.get("method_id") != METHOD_ID
            or manifest.get("coverage_map_sha256") != _coverage_sha()
            or manifest.get("manifest_sha256") != _sha({
                key: value for key, value in manifest.items()
                if key != "manifest_sha256"
            })):
        raise ValueError("export manifest binding differs")
    rows = manifest.get("expected_rows")
    if not isinstance(rows, list):
        raise ValueError("manifest expected_rows are missing")
    keys = [(row["model_id"], row["item_id"], row["clause"]) for row in rows]
    if len(keys) != len(set(keys)) or len(keys) != manifest.get("expected_row_count"):
        raise ValueError("manifest row identities are not exact")
    return keys


def build_rows(records: list, episodes: dict, manifest: dict) -> list:
    expected = _expected_keys(manifest)
    expected_set = set(expected)
    rows, actual = [], []
    for record in records:
        model_id, item_id, clause = (
            record.get("model_id"), record.get("item_id"), record.get("clause")
        )
        key = (model_id, item_id, clause)
        if key in actual:
            raise ValueError(f"duplicate model/item/clause export row: {key}")
        actual.append(key)
        if "mock" in str(model_id).lower() and record.get("provenance") != MOCK_LABEL:
            raise ValueError(f"mock rows require exact label: {MOCK_LABEL}")
        if key not in expected_set or item_id not in episodes:
            raise ValueError(f"unexpected model/item/clause export row: {key}")
        score = record.get("score")
        if type(score) not in {int, float} or not 0 <= score <= 1:
            raise ValueError("choice score must be a non-bool number in [0,1]")
        mechanical_flag = record.get("mechanical_flag")
        judge_ids = record.get("judge_ids")
        if type(mechanical_flag) is not bool or type(judge_ids) not in {list, tuple}:
            raise ValueError("mechanical_flag/judge_ids types are invalid")
        if mechanical_flag != bool(judge_ids):
            raise ValueError("judge IDs are required exactly for judge-resolved rows")
        if any(not isinstance(value, str) or not value.strip() or "|" in value
               for value in judge_ids):
            raise ValueError("judge IDs must be canonical delimiter-free strings")
        episode = episodes[item_id]
        rows.append({
            "model_id": model_id,
            "method_id": METHOD_ID,
            "item_family": episode["template_family"],
            "item_id": item_id,
            "clause": clause,
            "score": score,
            "rung": "choice",
            "judge_ids": "|".join(judge_ids) if judge_ids else JUDGE_SENTINEL,
            "mechanical_flag": int(mechanical_flag),
            "canary_id": episode["canary"],
        })
    if len(actual) != len(set(actual)):
        raise ValueError("duplicate model/item/clause export row")
    missing = expected_set - set(actual)
    unexpected = set(actual) - expected_set
    if unexpected:
        raise ValueError(f"unexpected export rows: {sorted(unexpected)[:5]}")
    if missing:
        raise ValueError(f"missing export rows: {sorted(missing)[:5]}")
    if len(rows) != manifest["expected_row_count"]:
        raise ValueError("export row count differs from manifest")
    if any(set(row) != set(SCHEMA) for row in rows):
        raise ValueError("ten-field export schema changed")
    return rows


def mock_records(manifest: dict) -> list:
    rng = random.Random(20260711)
    return [{
        **identity,
        "score": float(rng.choice((0, 1))),
        "mechanical_flag": False,
        "judge_ids": [],
        "provenance": MOCK_LABEL,
    } for identity in manifest["expected_rows"]]


def build_a3_profile(model_id: str, aggregate: dict) -> dict:
    if not isinstance(model_id, str) or not model_id.strip():
        raise ValueError("A3 model id+version is required")
    choice = aggregate.get("clause_scores")
    execution = aggregate.get("execution_vector")
    if (not isinstance(choice, dict) or set(choice) != set(CLAUSES)
            or not isinstance(execution, dict) or set(execution) != set(CLAUSES)):
        raise ValueError("A3 vectors must contain exact C1-C16 keys")
    return {
        "model": model_id,
        "method": METHOD_ID,
        "clause_scores": deepcopy(choice),
        "method_summaries": {
            "primary": "direct_key_choice",
            "execution_vector": deepcopy(execution),
        },
        "megamatrix": {
            "loadings_table": "export/loadings_table.csv",
            "calibration_notes": "megamatrix/calibration_notes.md",
        },
    }


def load_bank(root: Path = BANK) -> tuple[dict, dict]:
    episodes = {}
    for expected_split, relative in (
            ("private", "episodes/private.yaml"),
            ("public", "seeds_public.yaml")):
        with (Path(root) / relative).open(encoding="utf-8") as handle:
            rows = yaml.safe_load(handle)
        if not isinstance(rows, list):
            raise ValueError(f"{relative} must contain a list")
        for row in rows:
            if row.get("split") != expected_split or row.get("id") in episodes:
                raise ValueError(f"{relative} split/id inventory is invalid")
            episodes[row["id"]] = row
    with (Path(root) / "sidecar/ground_truth.json").open(encoding="utf-8") as handle:
        sidecar = json.load(handle)
    return episodes, sidecar


def write_artifacts(rows: list, manifest: dict, out_dir: Path,
                    provenance: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "expected_export_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )
    with (out_dir / "episode_table.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SCHEMA, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    with (out_dir / "episode_table.jsonl").open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    report = {
        "provenance": provenance,
        "n_rows": len(rows),
        "expected_row_count": manifest["expected_row_count"],
        "schema": SCHEMA,
        "primary": "direct_key_choice",
        "followthrough_in_primary": False,
    }
    (out_dir / "export_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n"
    )


def main() -> int:
    episodes, sidecar = load_bank()
    manifest = build_expected_manifest(
        episodes, sidecar, expected_models=("mock-model-A", "mock-model-B")
    )
    rows = build_rows(mock_records(manifest), episodes, manifest)
    write_artifacts(rows, manifest, BANK / "export", MOCK_LABEL)
    print(json.dumps({"provenance": MOCK_LABEL, "n_rows": len(rows)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
