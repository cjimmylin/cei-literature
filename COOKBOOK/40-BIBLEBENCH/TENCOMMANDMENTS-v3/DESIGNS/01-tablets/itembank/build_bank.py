"""Build and verify the frozen TABLETS P1 projection artifacts."""

import argparse
from collections import Counter
import json
from pathlib import Path
import sys


TABLETS_ROOT = Path(__file__).resolve().parents[1]
if str(TABLETS_ROOT) not in sys.path:
    sys.path.insert(0, str(TABLETS_ROOT))

from itembank.generator import (
    build_private_row,
    build_rows,
    build_runtime_row,
    validate_frozen_public_row,
)
from tablets_constants import (
    GENERATOR_SEED,
    GENERATOR_VERSION,
    PANEL_STATUS,
    PAIRS,
    PRIORITY_PAIRS,
    PUBLIC_RECORD_COUNT,
    RECORD_TYPE_COUNTS,
    SCHEMA_VERSION,
)
from tablets_hashing import canonical_json, canonical_sha256
from tablets_schemas import validate_private_row, validate_public_row, validate_runtime_row


ROOT = TABLETS_ROOT
ARTIFACT_PATHS = {
    "public": ROOT / "itembank" / "bank" / "p1-public.jsonl",
    "private": ROOT / "itembank" / "gold" / "p1-private.gold.jsonl",
    "runtime": ROOT / "itembank" / "runtime" / "p1-runtime-manifest.jsonl",
    "manifest": ROOT / "itembank" / "manifest.json",
}


def _jsonl_bytes(rows):
    return ("\n".join(canonical_json(row) for row in rows) + "\n").encode("utf-8")


def _parse_jsonl(payload):
    text = payload.decode("utf-8")
    if not text.endswith("\n"):
        raise ValueError("JSONL artifact must end with a newline")
    return [json.loads(line) for line in text.splitlines()]


def _expected_manifest(artifacts):
    return {
        "benchmark": "TABLETS",
        "schema_version": SCHEMA_VERSION,
        "generator_version": GENERATOR_VERSION,
        "generator_seed": GENERATOR_SEED,
        "record_count": PUBLIC_RECORD_COUNT,
        "record_type_counts": RECORD_TYPE_COUNTS,
        "panel_status": PANEL_STATUS,
        "official_gold_eligible": False,
        "artifacts": {
            name: {
                "path": str(ARTIFACT_PATHS[name].relative_to(ROOT)),
                "sha256": canonical_sha256(payload, raw_bytes=True),
                "bytes": len(payload),
            }
            for name, payload in artifacts.items()
        },
    }


def _validate_schedule_coverage(public):
    by_type = {
        record_type: [row for row in public if row["record_type"] == record_type]
        for record_type in RECORD_TYPE_COUNTS
    }
    primary_pairs = Counter(row["pair"] for row in by_type["adjudication"])
    expected_primary = {
        pair: 12 if pair in PRIORITY_PAIRS else 6 for pair in PAIRS
    }
    if primary_pairs != expected_primary:
        raise ValueError("public schedule primary pair coverage mismatch")
    for record_type, per_pair in (
        ("threat_twin", 3),
        ("comprehension", 1),
        ("recognition", 1),
    ):
        if Counter(row["pair"] for row in by_type[record_type]) != {
            pair: per_pair for pair in PAIRS
        }:
            raise ValueError("public schedule %s pair coverage mismatch" % record_type)
    monitors = by_type["monitoring_twin"]
    if {row["pair"] for row in monitors} != set(PAIRS):
        raise ValueError("public schedule monitoring pair coverage mismatch")
    priority_monitor_pairs = {
        row["pair"] for row in monitors if row["severity_tier"] in {"T2", "T3"}
    }
    if priority_monitor_pairs != set(PRIORITY_PAIRS):
        raise ValueError("public schedule priority monitoring coverage mismatch")


def _validate_link_graph(public):
    by_id = {row["id"]: row for row in public}
    for row in public:
        parent_id = row["parent_id"]
        if parent_id is not None:
            if parent_id not in by_id:
                raise ValueError("parent link target does not exist")
            if parent_id not in row["paired_record_ids"]:
                raise ValueError("parent link is missing from paired record IDs")
            parent = by_id[parent_id]
            if (
                parent["record_type"] != "adjudication"
                or parent["framing_arm"] != "neutral"
                or parent["monitoring_condition"] != "unmonitored"
            ):
                raise ValueError("non-primary parent must be a neutral adjudication")
        for linked_id in row["paired_record_ids"]:
            if linked_id == row["id"]:
                raise ValueError("public link graph may not contain a self-link")
            if linked_id not in by_id:
                raise ValueError("paired link target does not exist")
            if row["id"] not in by_id[linked_id]["paired_record_ids"]:
                raise ValueError("paired links must be reciprocal")


def build_artifact_bytes():
    public, private, runtime = build_rows()
    artifacts = {
        "public": _jsonl_bytes(public),
        "private": _jsonl_bytes(private),
        "runtime": _jsonl_bytes(runtime),
    }
    manifest = _expected_manifest(artifacts)
    artifacts["manifest"] = (canonical_json(manifest) + "\n").encode("utf-8")
    return artifacts


def validate_artifact_bytes(artifacts):
    if set(artifacts) != {"public", "private", "runtime", "manifest"}:
        raise ValueError("artifact set is incomplete")
    manifest = json.loads(artifacts["manifest"])
    public = _parse_jsonl(artifacts["public"])
    private = _parse_jsonl(artifacts["private"])
    runtime = _parse_jsonl(artifacts["runtime"])
    if not (len(public) == len(private) == len(runtime) == PUBLIC_RECORD_COUNT):
        raise ValueError("projection record count mismatch")
    for row in public:
        validate_public_row(row)
    for row in private:
        validate_private_row(row)
    for row in runtime:
        validate_runtime_row(row)
    public_ids = [row["id"] for row in public]
    private_ids = [row["id"] for row in private]
    runtime_source_ids = [row["source_record_id"] for row in runtime]
    runtime_request_ids = [row["runtime_request_id"] for row in runtime]
    if len(set(public_ids)) != PUBLIC_RECORD_COUNT:
        raise ValueError("public IDs must be unique")
    if len(set(private_ids)) != PUBLIC_RECORD_COUNT:
        raise ValueError("private IDs must be unique")
    if len(set(runtime_source_ids)) != PUBLIC_RECORD_COUNT:
        raise ValueError("runtime source IDs must be unique")
    if len(set(runtime_request_ids)) != PUBLIC_RECORD_COUNT:
        raise ValueError("runtime request IDs must be unique")
    if Counter(row["record_type"] for row in public) != RECORD_TYPE_COUNTS:
        raise ValueError("public schedule record-type counts mismatch")
    _validate_schedule_coverage(public)
    _validate_link_graph(public)
    for row in public:
        validate_frozen_public_row(row)
    if public_ids != private_ids:
        raise ValueError("public/private ordering mismatch")
    if public_ids != runtime_source_ids:
        raise ValueError("public/runtime ordering mismatch")
    for pub, gold, request in zip(public, private, runtime):
        digest = canonical_sha256(pub)
        if gold["public_record_sha256"] != digest:
            raise ValueError("private projection binding mismatch")
        if gold != build_private_row(pub):
            raise ValueError("private row violates deterministic private semantics")
        if request["source_public_record_sha256"] != digest:
            raise ValueError("runtime projection binding mismatch")
        if request != build_runtime_row(pub):
            raise ValueError("runtime row violates deterministic runtime request")
    expected_manifest = _expected_manifest(
        {name: artifacts[name] for name in ("public", "private", "runtime")}
    )
    if manifest != expected_manifest:
        raise ValueError("manifest metadata/path/byte/hash mismatch")
    return True


def write_artifacts():
    artifacts = build_artifact_bytes()
    validate_artifact_bytes(artifacts)
    for name, path in ARTIFACT_PATHS.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(artifacts[name])
    return artifacts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify disk bytes only")
    args = parser.parse_args(argv)
    expected = build_artifact_bytes()
    validate_artifact_bytes(expected)
    if args.check:
        for name, path in ARTIFACT_PATHS.items():
            if not path.exists() or path.read_bytes() != expected[name]:
                raise SystemExit("artifact drift: %s" % path)
    else:
        write_artifacts()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
