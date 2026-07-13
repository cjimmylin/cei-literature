"""Validate and append isolated panel shards into one resumable checkpoint."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterable, Sequence, Set


def _key(record: dict) -> tuple:
    return record.get("item_id"), record.get("model")


def _read_jsonl(path: Path) -> list:
    if not path.exists():
        return []
    records = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON in {path}:{lineno}: {exc}") from exc
        if not record.get("item_id") or not record.get("model"):
            raise ValueError(f"missing item_id/model in {path}:{lineno}")
        records.append(record)
    return records


def _index(records: Iterable[dict], source: Path) -> dict:
    indexed = {}
    for record in records:
        key = _key(record)
        if key in indexed:
            raise ValueError(f"duplicate key within {source}: {key}")
        indexed[key] = record
    return indexed


def merge_reexecution_shards(canonical_path, shard_paths: Sequence,
                             expected_path, designs: Set[str],
                             append: bool = False) -> dict:
    """Require the exact expected key surface, then append only missing shard rows.

    Re-running after a partial/successful append is safe: byte-equivalent duplicate
    records are accepted, while any conflicting duplicate fails before a write.
    """
    canonical_path = Path(canonical_path)
    shard_paths = [Path(path) for path in shard_paths]
    expected_path = Path(expected_path)

    canonical = _index(_read_jsonl(canonical_path), canonical_path)
    expected_records = [record for record in _read_jsonl(expected_path)
                        if record.get("design") in designs]
    expected = _index(expected_records, expected_path)

    prospective = dict(canonical)
    for shard_path in shard_paths:
        shard = _index(_read_jsonl(shard_path), shard_path)
        for key, record in shard.items():
            if key in prospective and prospective[key] != record:
                raise ValueError(f"conflicting duplicate key across inputs: {key}")
            prospective[key] = record

    expected_keys = set(expected)
    actual_keys = set(prospective)
    missing = expected_keys - actual_keys
    extra = actual_keys - expected_keys
    if missing or extra:
        raise ValueError(
            f"coverage mismatch: missing={len(missing)} extra={len(extra)}")

    to_append = [prospective[_key(record)] for record in expected_records
                 if _key(record) not in canonical]
    appended = 0
    if append and to_append:
        canonical_path.parent.mkdir(parents=True, exist_ok=True)
        with canonical_path.open("a", encoding="utf-8") as fh:
            for record in to_append:
                fh.write(json.dumps(record, ensure_ascii=False) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        appended = len(to_append)

    return {
        "expected_keys": len(expected_keys),
        "canonical_keys": len(canonical),
        "prospective_keys": len(actual_keys),
        "appended": appended,
        "complete": actual_keys == expected_keys,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate and append isolated WALKWORTHY panel shards")
    parser.add_argument("--canonical", required=True)
    parser.add_argument("--shard", action="append", required=True)
    parser.add_argument("--expected", required=True)
    parser.add_argument("--designs", required=True,
                        help="comma-separated design ids included in the run")
    parser.add_argument("--append", action="store_true")
    args = parser.parse_args(argv)
    summary = merge_reexecution_shards(
        args.canonical, args.shard, args.expected,
        {design.strip() for design in args.designs.split(",") if design.strip()},
        append=args.append)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
