#!/usr/bin/env python3
"""Pinned megamatrix episode export for CHARITROC.

One row represents an episode's primary stage-4 ordinal gate score. D-07's
stage-3 revision score is intentionally absent and exported separately by the
pilot harness. Default execution uses synthetic mock rows and labels them
``harness validation, NOT a measurement``.

``mechanical_flag=0`` means the mechanical parser resolved the score and the
serialized ``judge_ids`` value is the exact ``mechanical`` sentinel.
``mechanical_flag=1`` means mechanical resolution failed and one or more actual
judge IDs must be serialized as delimiter-separated components.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import random
from itertools import product


BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METHOD_ID = "charitroc"
CLAUSE = "CHARITROC:CALIBRATED_CHARITY"
MOCK_LABEL = "harness validation, NOT a measurement"
SCHEMA = [
    "model_id", "method_id", "item_family", "item_id", "clause",
    "score", "rung", "judge_ids", "mechanical_flag", "canary_id",
]
MANIFEST_FILENAME = "expected_export_manifest.json"
MANIFEST_VERSION = "CHARITROC-export-manifest-v2"
MOCK_MODELS = ("mock-model-A", "mock-model-B")
EXPECTED_FAMILIES = (
    "CR-REQ-ACCOUNT", "CR-REQ-NETWORK", "CR-REQ-LAB",
    "CR-REQ-MEDICATION", "CR-REQ-TRANSFER", "CR-REQ-DATA",
    "CR-CLM-EXPENSE", "CR-CLM-INCIDENT", "CR-CLM-AUTHORSHIP",
    "CR-CLM-CONSENT", "CR-CLM-WARRANTY", "CR-CLM-PROVENANCE",
)
EXPECTED_TRUE_TYPES = ("benign", "malicious")
EXPECTED_CUES = ("strong", "weak", "absent", "adversarial")
EXPECTED_PRIORS = (0.2, 0.5, 0.8)
JUDGE_SENTINEL = "mechanical"
JUDGE_DELIMITER = "|"
EXPECTED_SPLIT_COUNTS = {
    "private": 576,
    "calibration": 96,
    "public": 12,
}
NON_PRIVATE_EXCLUSION_REASONS = {
    "calibration": (
        "calibration episode: pilot-only, not a sealed private "
        "measurement episode"
    ),
    "public": (
        "public seed: demonstration-only, not a private evaluation episode"
    ),
}


def _cell_key(episode: dict, hidden: dict) -> str:
    return "|".join([
        episode["template_family"], hidden["true_type"],
        hidden["cue_variant"], str(hidden["base_rate_benign"]),
    ])


def _declared_cell_keys() -> set:
    return {
        "|".join([family, true_type, cue, str(prior)])
        for family, true_type, cue, prior in product(
            EXPECTED_FAMILIES, EXPECTED_TRUE_TYPES,
            EXPECTED_CUES, EXPECTED_PRIORS,
        )
    }


def _split_counts(episodes: dict) -> dict:
    counts = {split: 0 for split in EXPECTED_SPLIT_COUNTS}
    unexpected = {}
    for item_id, episode in episodes.items():
        split = episode.get("split")
        if split not in counts:
            unexpected[item_id] = split
        else:
            counts[split] += 1
    if unexpected:
        raise ValueError(f"split inventory has unexpected values: {unexpected}")
    return counts


def validate_bank_inventory(episodes: dict, sidecar: dict) -> dict:
    """Require the complete public/calibration/private construction bank."""
    if not isinstance(episodes, dict) or not isinstance(sidecar, dict):
        raise ValueError("episodes and sidecar must be dictionaries")
    if set(episodes) != set(sidecar):
        raise ValueError("episode/sidecar key mismatch in split inventory")
    bad_ids = [
        item_id for item_id, episode in episodes.items()
        if not isinstance(episode, dict) or episode.get("id") != item_id
    ]
    if bad_ids:
        raise ValueError(
            f"episode dictionary keys must match episode ids: {bad_ids[:8]}"
        )
    counts = _split_counts(episodes)
    if counts != EXPECTED_SPLIT_COUNTS:
        raise ValueError(
            "split inventory mismatch: "
            f"expected={EXPECTED_SPLIT_COUNTS} observed={counts}"
        )
    return counts


def non_private_exclusions(episodes: dict) -> dict:
    """Return every calibration/public exclusion with a frozen reason."""
    _split_counts(episodes)
    return {
        item_id: NON_PRIVATE_EXCLUSION_REASONS[episode["split"]]
        for item_id, episode in episodes.items()
        if episode["split"] in NON_PRIVATE_EXCLUSION_REASONS
    }


def public_seed_exclusions(episodes: dict) -> dict:
    """Compatibility name for the complete non-private exclusion map.

    Calibration episodes were added after the initial export implementation.
    Keeping this callable avoids silently restoring the old public-only
    behavior in downstream scripts while the clearer name is adopted.
    """
    return non_private_exclusions(episodes)


def build_expected_manifest(episodes: dict, sidecar: dict,
                            expected_models, exclusions: dict) -> dict:
    """Freeze expected models, episodes, cells, and explicit exclusions.

    The expectation is built from the complete bank, never from received scored
    rows. Consequently a truncated scored-run file cannot redefine success.
    """
    models = list(expected_models)
    if (not models or len(models) != len(set(models))
            or any(not isinstance(model, str) or not model.strip() for model in models)):
        raise ValueError("expected_models must be an explicit non-empty unique string list")
    if not isinstance(exclusions, dict):
        raise ValueError("exclusions must explicitly map item_id to a non-empty reason")

    bank_ids = set(episodes)
    if bank_ids != set(sidecar):
        raise ValueError("episode/sidecar key mismatch while building export manifest")
    if any(episode.get("id") != item_id for item_id, episode in episodes.items()):
        raise ValueError("episode dictionary keys must match episode ids")

    exclusion_ids = set(exclusions)
    unknown_exclusions = exclusion_ids - bank_ids
    if unknown_exclusions:
        raise ValueError(f"exclusion accounting has unknown ids: {sorted(unknown_exclusions)}")
    bad_reasons = sorted(
        item_id for item_id, reason in exclusions.items()
        if not isinstance(reason, str) or not reason.strip()
    )
    if bad_reasons:
        raise ValueError(f"exclusion accounting has blank reasons: {bad_reasons}")

    non_private_ids = {
        item_id for item_id, episode in episodes.items()
        if episode.get("split") != "private"
    }
    if exclusion_ids != non_private_ids:
        raise ValueError(
            "every non-private episode and no private episode must be an "
            "explicit exclusion: "
            f"missing={sorted(non_private_ids - exclusion_ids)[:8]} "
            f"unexpected={sorted(exclusion_ids - non_private_ids)[:8]}"
        )
    wrong_reasons = {
        item_id: reason for item_id, reason in exclusions.items()
        if reason != NON_PRIVATE_EXCLUSION_REASONS[
            episodes[item_id]["split"]
        ]
    }
    if wrong_reasons:
        raise ValueError(
            f"non-private exclusion reasons changed: {wrong_reasons}"
        )

    expected_ids = sorted(bank_ids - exclusion_ids)

    cells = {}
    for item_id in expected_ids:
        key = _cell_key(episodes[item_id], sidecar[item_id])
        cells.setdefault(key, []).append(item_id)
    cells = {key: sorted(item_ids) for key, item_ids in sorted(cells.items())}

    manifest = {
        "manifest_version": MANIFEST_VERSION,
        "method_id": METHOD_ID,
        "clause": CLAUSE,
        "expected_models": models,
        "bank_episode_ids": sorted(bank_ids),
        "bank_episode_count": len(bank_ids),
        "split_counts": _split_counts(episodes),
        "expected_episode_ids": expected_ids,
        "expected_episode_count": len(expected_ids),
        "exclusions": [
            {"item_id": item_id, "reason": exclusions[item_id]}
            for item_id in sorted(exclusions)
        ],
        "excluded_episode_count": len(exclusions),
        "exclusion_counts_by_split": {
            split: sum(
                episodes[item_id]["split"] == split
                for item_id in exclusions
            )
            for split in ("calibration", "public")
        },
        "cell_dimensions": {
            "item_families": list(EXPECTED_FAMILIES),
            "true_types": list(EXPECTED_TRUE_TYPES),
            "cue_variants": list(EXPECTED_CUES),
            "base_rate_benign": list(EXPECTED_PRIORS),
        },
        "expected_cells": cells,
        "expected_cell_count": len(cells),
        "expected_row_count": len(models) * len(expected_ids),
    }
    validate_expected_manifest(manifest, episodes, sidecar)
    return manifest


def validate_expected_manifest(manifest: dict, episodes: dict,
                               sidecar: dict) -> dict:
    """Fail loudly unless a persisted expectation exactly matches the bank."""
    if manifest.get("manifest_version") != MANIFEST_VERSION:
        raise ValueError("unexpected export manifest version")
    if manifest.get("method_id") != METHOD_ID or manifest.get("clause") != CLAUSE:
        raise ValueError("export manifest method/clause mismatch")

    models = manifest.get("expected_models")
    if (not isinstance(models, list) or not models
            or len(models) != len(set(models))
            or any(not isinstance(model, str) or not model.strip() for model in models)):
        raise ValueError("expected_models must be an explicit non-empty unique string list")

    bank_ids = set(episodes)
    if bank_ids != set(sidecar):
        raise ValueError("episode/sidecar key mismatch while validating export manifest")
    if manifest.get("bank_episode_ids") != sorted(bank_ids):
        raise ValueError("bank episode manifest mismatch")
    if manifest.get("bank_episode_count") != len(bank_ids):
        raise ValueError("bank episode count mismatch")

    exclusions = manifest.get("exclusions")
    if not isinstance(exclusions, list):
        raise ValueError("exclusion accounting requires an explicit list")
    exclusion_ids = []
    for exclusion in exclusions:
        if (not isinstance(exclusion, dict)
                or set(exclusion) != {"item_id", "reason"}
                or exclusion["item_id"] not in bank_ids
                or not isinstance(exclusion["reason"], str)
                or not exclusion["reason"].strip()):
            raise ValueError(f"invalid exclusion accounting entry: {exclusion!r}")
        exclusion_ids.append(exclusion["item_id"])
    if len(exclusion_ids) != len(set(exclusion_ids)):
        raise ValueError("exclusion accounting contains duplicate ids")
    if manifest.get("excluded_episode_count") != len(exclusion_ids):
        raise ValueError("exclusion accounting count mismatch")

    non_private_ids = {
        item_id for item_id, episode in episodes.items()
        if episode.get("split") != "private"
    }
    if set(exclusion_ids) != non_private_ids:
        raise ValueError(
            "non-private exclusion accounting mismatch: "
            f"missing={sorted(non_private_ids - set(exclusion_ids))[:8]} "
            f"unexpected={sorted(set(exclusion_ids) - non_private_ids)[:8]}"
        )
    expected_exclusion_counts = {
        split: sum(
            episodes[item_id]["split"] == split
            for item_id in exclusion_ids
        )
        for split in ("calibration", "public")
    }
    if manifest.get("exclusion_counts_by_split") != expected_exclusion_counts:
        raise ValueError("non-private exclusion split counts mismatch")
    for exclusion in exclusions:
        expected_reason = NON_PRIVATE_EXCLUSION_REASONS[
            episodes[exclusion["item_id"]]["split"]
        ]
        if exclusion["reason"] != expected_reason:
            raise ValueError(
                f"{exclusion['item_id']}: non-private exclusion reason mismatch"
            )

    expected_ids = manifest.get("expected_episode_ids")
    if not isinstance(expected_ids, list) or len(expected_ids) != len(set(expected_ids)):
        raise ValueError("expected episode manifest must be a unique list")
    expected_set = set(expected_ids)
    excluded_set = set(exclusion_ids)
    if expected_set & excluded_set or expected_set | excluded_set != bank_ids:
        raise ValueError("exclusion accounting does not partition the bank exactly")
    if manifest.get("expected_episode_count") != len(expected_ids):
        raise ValueError("expected episode count mismatch")
    if any(episodes[item_id].get("split") != "private" for item_id in expected_ids):
        raise ValueError("non-private episodes remain in expected episode manifest")

    expected_dimensions = {
        "item_families": list(EXPECTED_FAMILIES),
        "true_types": list(EXPECTED_TRUE_TYPES),
        "cue_variants": list(EXPECTED_CUES),
        "base_rate_benign": list(EXPECTED_PRIORS),
    }
    if manifest.get("cell_dimensions") != expected_dimensions:
        raise ValueError("declared cell coverage dimensions changed")

    actual_cells = {}
    for item_id in expected_ids:
        key = _cell_key(episodes[item_id], sidecar[item_id])
        actual_cells.setdefault(key, []).append(item_id)
    actual_cells = {
        key: sorted(item_ids) for key, item_ids in sorted(actual_cells.items())
    }
    declared_keys = _declared_cell_keys()
    if set(actual_cells) != declared_keys:
        missing = sorted(declared_keys - set(actual_cells))
        unexpected = sorted(set(actual_cells) - declared_keys)
        raise ValueError(
            "declared cell coverage mismatch: "
            f"missing={missing} unexpected={unexpected}"
        )
    if manifest.get("expected_cells") != actual_cells:
        raise ValueError("expected cell manifest does not match expected episodes")
    if manifest.get("expected_cell_count") != len(declared_keys):
        raise ValueError("declared cell coverage count mismatch")
    wrong_cell_sizes = {
        key: len(item_ids) for key, item_ids in actual_cells.items()
        if len(item_ids) != 2
    }
    if wrong_cell_sizes:
        raise ValueError(
            "declared cell coverage requires exactly 2 episodes per cell: "
            f"{wrong_cell_sizes}"
        )

    split_counts = validate_bank_inventory(episodes, sidecar)
    if manifest.get("split_counts") != split_counts:
        raise ValueError("split inventory in export manifest mismatch")

    expected_row_count = len(models) * len(expected_ids)
    if manifest.get("expected_row_count") != expected_row_count:
        raise ValueError("expected model-by-episode row count mismatch")
    return {
        "n_models": len(models),
        "n_episodes": len(expected_ids),
        "n_exclusions": len(exclusion_ids),
        "n_cells": len(actual_cells),
        "n_rows": expected_row_count,
    }


def validate_export_rows(rows: list, episodes: dict, sidecar: dict,
                         manifest: dict, row_format: str = "json") -> dict:
    """Assert exactly one schema-valid row for every model x episode pair."""
    if row_format not in {"json", "csv"}:
        raise ValueError("row_format must be 'json' or 'csv'")
    summary = validate_expected_manifest(manifest, episodes, sidecar)
    if not rows:
        raise ValueError("no export rows")
    for row in rows:
        if set(row) != set(SCHEMA):
            raise ValueError("export schema mismatch")

    expected_models = set(manifest["expected_models"])
    actual_models = {row["model_id"] for row in rows}
    if actual_models != expected_models:
        raise ValueError(
            "model set mismatch: "
            f"missing={sorted(expected_models - actual_models)} "
            f"unexpected={sorted(actual_models - expected_models)}"
        )

    expected_pairs = set(product(
        manifest["expected_models"], manifest["expected_episode_ids"]
    ))
    actual_pairs = []
    for row in rows:
        item_id = row["item_id"]
        if item_id not in episodes:
            raise ValueError(f"unknown item_id in export row: {item_id}")
        episode = episodes[item_id]
        if row["method_id"] != METHOD_ID or row["clause"] != CLAUSE:
            raise ValueError(f"{item_id}: method/clause export mismatch")
        if row["item_family"] != episode["template_family"]:
            raise ValueError(f"{item_id}: family export mismatch")
        if row["rung"] != "stage_4":
            raise ValueError(f"{item_id}: primary rung must be stage_4")
        if row["canary_id"] != episode["canary"]:
            raise ValueError(f"{item_id}: canary export mismatch")
        if row_format == "json":
            if type(row["score"]) is not int or row["score"] not in range(5):
                raise ValueError(
                    f"{item_id}: JSON score must be a non-bool integer 0..4"
                )
            if (type(row["mechanical_flag"]) is not int
                    or row["mechanical_flag"] not in {0, 1}):
                raise ValueError(
                    f"{item_id}: JSON mechanical_flag must be a non-bool "
                    "integer 0 or 1"
                )
            mechanical_flag = row["mechanical_flag"]
        elif (type(row["score"]) is not str
              or row["score"] not in {"0", "1", "2", "3", "4"}):
            raise ValueError(
                f"{item_id}: CSV score must be an exact digit 0..4"
            )
        else:
            if (type(row["mechanical_flag"]) is not str
                    or row["mechanical_flag"] not in {"0", "1"}):
                raise ValueError(
                    f"{item_id}: CSV mechanical_flag must be exact '0' or '1'"
                )
            mechanical_flag = int(row["mechanical_flag"])

        serialized_judges = row["judge_ids"]
        if (type(serialized_judges) is not str
                or not serialized_judges.strip()):
            raise ValueError(
                f"{item_id}: judge_ids must be a non-empty string "
                "consistent with mechanical_flag"
            )
        if mechanical_flag == 0:
            if serialized_judges != JUDGE_SENTINEL:
                raise ValueError(
                    f"{item_id}: mechanical_flag=0 requires judge_ids "
                    f"sentinel {JUDGE_SENTINEL!r}"
                )
        else:
            components = serialized_judges.split(JUDGE_DELIMITER)
            if (serialized_judges == JUDGE_SENTINEL
                    or any(
                        not component
                        or component != component.strip()
                        or component == JUDGE_SENTINEL
                        for component in components
                    )):
                raise ValueError(
                    f"{item_id}: judge_ids must be pipe-separated non-empty "
                    "delimiter-free components when mechanical_flag=1"
                )
        actual_pairs.append((row["model_id"], item_id))

    if len(actual_pairs) != len(set(actual_pairs)):
        raise ValueError("duplicate model/item export row")
    actual_pair_set = set(actual_pairs)
    unexpected = actual_pair_set - expected_pairs
    if unexpected:
        raise ValueError(f"unexpected model/item rows: {sorted(unexpected)[:8]}")
    missing = expected_pairs - actual_pair_set
    if missing:
        raise ValueError(f"missing model/item rows: {sorted(missing)[:8]}")
    if len(rows) != manifest["expected_row_count"]:
        raise ValueError("export row count does not match complete manifest")

    # Make the cell assertion explicit per model; do not rely only on totals.
    for model_id in manifest["expected_models"]:
        model_items = {
            row["item_id"] for row in rows if row["model_id"] == model_id
        }
        for cell, item_ids in manifest["expected_cells"].items():
            if model_items.intersection(item_ids) != set(item_ids):
                raise ValueError(f"{model_id}: incomplete declared cell {cell}")
    return summary


def build_rows(records: list, episodes: dict, sidecar: dict,
               manifest: dict) -> list:
    rows = []
    seen = set()
    for record in records:
        model_id = record["model_id"]
        if "mock" in model_id.lower() and record.get("provenance") != MOCK_LABEL:
            raise ValueError(f"mock rows require label: {MOCK_LABEL}")
        item_id = record["item_id"]
        key = (model_id, item_id)
        if key in seen:
            raise ValueError(f"duplicate model/item export row: {key}")
        seen.add(key)
        if item_id not in episodes or item_id not in sidecar:
            raise ValueError(f"unknown item_id in scored records: {item_id}")
        episode = episodes[item_id]
        hidden = sidecar[item_id]
        score = record["stage4_score"]
        if type(score) is not int or score not in range(5):
            raise ValueError(
                f"stage4_score must be a non-bool integer 0..4, got "
                f"{score!r}"
            )
        if hidden["scoring_key"]["primary_stage"] != "stage_4":
            raise ValueError(f"{item_id}: sidecar primary stage changed")
        mechanical_flag = record.get("mechanical_flag")
        if type(mechanical_flag) is not bool:
            raise ValueError("mechanical_flag must be an exact bool")
        judge_ids = record.get("judge_ids")
        if type(judge_ids) not in {list, tuple}:
            raise ValueError("judge_ids must be an exact list or tuple")
        if any(
                type(judge_id) is not str
                or not judge_id
                or judge_id != judge_id.strip()
                or JUDGE_DELIMITER in judge_id
                or judge_id == JUDGE_SENTINEL
                for judge_id in judge_ids):
            raise ValueError(
                "judge_ids must contain canonical non-empty delimiter-free "
                "strings"
            )
        if mechanical_flag != bool(judge_ids):
            raise ValueError(
                "mechanical_flag and judge_ids mismatch: flagged rows require "
                "judge IDs; mechanically resolved rows require none"
            )
        serialized_judges = (
            JUDGE_DELIMITER.join(judge_ids)
            if mechanical_flag else JUDGE_SENTINEL
        )
        rows.append({
            "model_id": model_id,
            "method_id": METHOD_ID,
            "item_family": episode["template_family"],
            "item_id": item_id,
            "clause": CLAUSE,
            "score": score,
            "rung": "stage_4",
            "judge_ids": serialized_judges,
            "mechanical_flag": int(mechanical_flag),
            "canary_id": episode["canary"],
        })
    validate_export_rows(
        rows, episodes, sidecar, manifest, row_format="json"
    )
    return rows


def write_rows(rows: list, out_dir: str):
    assert rows, "no export rows"
    assert all(set(row) == set(SCHEMA) for row in rows), "export schema mismatch"
    with open(os.path.join(out_dir, "episode_table.csv"), "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=SCHEMA, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)
    with open(os.path.join(out_dir, "episode_table.jsonl"), "w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def write_expected_manifest(out_dir: str, manifest: dict):
    with open(os.path.join(out_dir, MANIFEST_FILENAME), "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)


def write_export_report(out_dir: str, provenance: str, rows: list,
                        manifest: dict):
    report = {
        "provenance": provenance,
        "artifact_role": "complete synthetic export" if provenance == MOCK_LABEL else "complete export",
        "n_rows": len(rows),
        "expected_row_count": manifest["expected_row_count"],
        "expected_model_count": len(manifest["expected_models"]),
        "expected_episode_count": manifest["expected_episode_count"],
        "expected_cell_count": manifest["expected_cell_count"],
        "excluded_episode_count": manifest["excluded_episode_count"],
        "expected_manifest": MANIFEST_FILENAME,
        "schema": SCHEMA,
        "primary_stage": "stage_4",
        "stage3_in_primary_score": False,
    }
    with open(os.path.join(out_dir, "export_report.json"), "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)


def load_bank(bank_dir: str = BANK):
    import yaml
    episodes = {}
    for expected_split, rel in (
        ("private", "episodes/private_bank.yaml"),
        ("calibration", "episodes/calibration_bank.yaml"),
        ("public", "seeds_public.yaml"),
    ):
        path = os.path.join(bank_dir, rel)
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"missing {expected_split} split artifact: {rel}"
            )
        with open(path, encoding="utf-8") as handle:
            rows = yaml.safe_load(handle)
        if not isinstance(rows, list) or not rows:
            raise ValueError(f"{expected_split} split artifact must be a non-empty list")
        for episode in rows:
            if not isinstance(episode, dict) or not isinstance(episode.get("id"), str):
                raise ValueError(f"malformed episode in {expected_split} split")
            if episode.get("split") != expected_split:
                raise ValueError(
                    f"{episode['id']}: split file says {expected_split} but "
                    f"episode says {episode.get('split')}"
                )
            if episode["id"] in episodes:
                raise ValueError(f"duplicate episode id across splits: {episode['id']}")
            episodes[episode["id"]] = episode
    with open(os.path.join(bank_dir, "sidecar", "ground_truth.json"), encoding="utf-8") as handle:
        sidecar = json.load(handle)
    validate_bank_inventory(episodes, sidecar)
    return episodes, sidecar


def mock_records(manifest: dict) -> list:
    rng = random.Random(20260709)
    records = []
    for model_id in manifest["expected_models"]:
        for item_id in manifest["expected_episode_ids"]:
            stage4_score = rng.randint(0, 4)
            stage3_update_score = rng.randint(0, 1)
            mechanical_flag = rng.random() < 0.15
            records.append({
                "model_id": model_id,
                "item_id": item_id,
                "stage4_score": stage4_score,
                "stage3_update_score": stage3_update_score,
                "mechanical_flag": mechanical_flag,
                "judge_ids": (
                    ["mock-judge-X", "mock-judge-Y"]
                    if mechanical_flag else []
                ),
                "provenance": MOCK_LABEL,
            })
    return records


def main():
    parser = argparse.ArgumentParser(
        description="Write a manifest-complete CHARITROC megamatrix export."
    )
    parser.add_argument("records", nargs="?", help="JSONL scored records")
    parser.add_argument(
        "--expected-model", action="append", dest="expected_models",
        help="Expected model id; repeat once per model (required with records).",
    )
    args = parser.parse_args()

    episodes, sidecar = load_bank()
    out_dir = os.path.join(BANK, "export")
    if args.records:
        if not args.expected_models:
            parser.error("--expected-model is required with provided scored records")
        expected_models = args.expected_models
    else:
        expected_models = args.expected_models or list(MOCK_MODELS)
    manifest = build_expected_manifest(
        episodes,
        sidecar,
        expected_models=expected_models,
        exclusions=non_private_exclusions(episodes),
    )

    if args.records:
        with open(args.records, encoding="utf-8") as handle:
            records = [json.loads(line) for line in handle if line.strip()]
        label = "provided scored records"
    else:
        records = mock_records(manifest)
        mock_path = os.path.join(out_dir, "scored_runs.MOCK.jsonl")
        with open(mock_path, "w", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record) + "\n")
        label = MOCK_LABEL
    rows = build_rows(records, episodes, sidecar, manifest)
    write_expected_manifest(out_dir, manifest)
    write_rows(rows, out_dir)
    write_export_report(out_dir, label, rows, manifest)
    print(json.dumps({
        "provenance": label,
        "n_rows": len(rows),
        "expected_models": manifest["expected_models"],
        "expected_episodes": manifest["expected_episode_count"],
        "expected_cells": manifest["expected_cell_count"],
        "excluded_episodes": manifest["excluded_episode_count"],
        "schema": SCHEMA,
        "sample": rows[0],
    }, indent=2))


if __name__ == "__main__":
    main()
