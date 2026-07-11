"""Build, validate, and install deterministic PALTER P1 artifacts."""

from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

PALTER_ROOT = Path(__file__).resolve().parent.parent
if str(PALTER_ROOT) not in sys.path:
    sys.path.insert(0, str(PALTER_ROOT))

from itembank.generator import build_rows
from palter_constants import (
    BT_PASS_SPEARMAN,
    BT_SAMPLE_COMPOSITIONS,
    FAMILIES,
    GENERATOR_SEED,
    GENERATOR_VERSION,
    PRIVATE_RECORD_COUNT,
    PUBLIC_RECORD_COUNT,
    RECORD_TYPE_COUNTS,
    RUNTIME_RECORD_COUNT,
    SCHEMA_VERSION,
)
from palter_hashing import canonical_json, canonical_jsonl_bytes, canonical_sha256
from palter_schemas import (
    validate_private_row,
    validate_public_row,
    validate_runtime_row,
)


ITEMBANK_ROOT = Path(__file__).resolve().parent
ARTIFACT_PATHS = {
    "public_bank": "bank/p1-public.jsonl",
    "private_gold": "gold/p1-private.gold.jsonl",
    "runtime_manifest": "runtime/p1-runtime-manifest.jsonl",
    "manifest": "manifest.json",
}


def _sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def _manifest(public_bytes, private_bytes, runtime_bytes):
    return {
        "schema_version": SCHEMA_VERSION,
        "generator_version": GENERATOR_VERSION,
        "seed": GENERATOR_SEED,
        "counts": {
            "public_bank": PUBLIC_RECORD_COUNT,
            "private_gold": PRIVATE_RECORD_COUNT,
            "runtime_manifest": RUNTIME_RECORD_COUNT,
            "by_record_type": RECORD_TYPE_COUNTS,
            "bt_sample_compositions": BT_SAMPLE_COMPOSITIONS,
            "families": len(FAMILIES),
        },
        "frozen_rules": {
            "bt_pass_spearman_per_family": BT_PASS_SPEARMAN,
            "atom_audit_route": "unsupported_claims_to_LY",
            "pr_baseline": "excess_over_no_incentive_twin",
            "probe_bands": "two_sided",
            "material_harm_floor_tiers": ["T1", "T2"],
            "human_bt_status": "NOT_RUN",
            "probe_band_panel_status": "NOT_RUN",
            "predicted_shift_status": "CONSTRUCTIONAL_SYNTHETIC_PROFILE_ONLY",
            "evaluated_response_fields": ["composition"],
            "reader_judge_families_minimum": 2,
            "atom_audit_judge_families_minimum": 2,
            "pr_claims_authorized": False,
        },
        "artifacts": {
            "public_bank": {
                "path": ARTIFACT_PATHS["public_bank"],
                "sha256": _sha256_bytes(public_bytes),
            },
            "private_gold": {
                "path": ARTIFACT_PATHS["private_gold"],
                "sha256": _sha256_bytes(private_bytes),
            },
            "runtime_manifest": {
                "path": ARTIFACT_PATHS["runtime_manifest"],
                "sha256": _sha256_bytes(runtime_bytes),
            },
        },
    }


def build_artifact_bytes():
    public, private, runtime = build_rows()
    public_bytes = canonical_jsonl_bytes(public)
    private_bytes = canonical_jsonl_bytes(private)
    runtime_bytes = canonical_jsonl_bytes(runtime)
    manifest = _manifest(public_bytes, private_bytes, runtime_bytes)
    artifacts = {
        "public_bank": public_bytes,
        "private_gold": private_bytes,
        "runtime_manifest": runtime_bytes,
        "manifest": canonical_json(manifest).encode("utf-8") + b"\n",
    }
    validate_artifact_bytes(artifacts)
    return artifacts


def _parse_jsonl(data, label):
    if type(data) is not bytes or not data or not data.endswith(b"\n"):
        raise ValueError("%s must be nonempty canonical JSONL" % label)
    try:
        rows = tuple(json.loads(line.decode("utf-8")) for line in data[:-1].split(b"\n"))
    except Exception as exc:
        raise ValueError("%s is malformed JSONL" % label) from exc
    if canonical_jsonl_bytes(rows) != data:
        raise ValueError("%s is not canonical JSONL" % label)
    return rows


def validate_artifact_bytes(artifacts):
    if type(artifacts) is not dict or set(artifacts) != set(ARTIFACT_PATHS):
        raise ValueError("artifact set does not match the frozen contract")
    public = _parse_jsonl(artifacts["public_bank"], "public bank")
    private = _parse_jsonl(artifacts["private_gold"], "private gold")
    runtime = _parse_jsonl(artifacts["runtime_manifest"], "runtime manifest")
    try:
        manifest = json.loads(artifacts["manifest"].decode("utf-8"))
    except Exception as exc:
        raise ValueError("manifest is malformed") from exc
    if canonical_json(manifest).encode("utf-8") + b"\n" != artifacts["manifest"]:
        raise ValueError("manifest is not canonical JSON plus one newline")
    if (len(public), len(private), len(runtime)) != (
        PUBLIC_RECORD_COUNT,
        PRIVATE_RECORD_COUNT,
        RUNTIME_RECORD_COUNT,
    ):
        raise ValueError("artifact row count changed")
    if Counter(row.get("record_type") for row in public) != Counter(RECORD_TYPE_COUNTS):
        raise ValueError("public record-type counts changed")
    if [row.get("id") for row in public] != [row.get("id") for row in private]:
        raise ValueError("public/private order or linkage changed")
    if [row.get("id") for row in public] != [row.get("source_record_id") for row in runtime]:
        raise ValueError("public/runtime order or linkage changed")
    if len({row.get("id") for row in public}) != PUBLIC_RECORD_COUNT:
        raise ValueError("public IDs are not unique")

    for public_row, private_row, runtime_row in zip(public, private, runtime):
        validate_public_row(public_row)
        validate_private_row(private_row)
        validate_runtime_row(runtime_row)
        digest = canonical_sha256(public_row)
        if private_row["public_record_sha256"] != digest:
            raise ValueError("private gold has a stale public hash")
        if runtime_row["source_public_record_sha256"] != digest:
            raise ValueError("runtime manifest has a stale public hash")

    expected_hashes = {
        key: _sha256_bytes(artifacts[key])
        for key in ("public_bank", "private_gold", "runtime_manifest")
    }
    for key, digest in expected_hashes.items():
        if manifest.get("artifacts", {}).get(key, {}).get("sha256") != digest:
            raise ValueError("%s hash does not match manifest" % key)
    if manifest.get("counts", {}).get("bt_sample_compositions") != sum(
        bool(row["bt_sample"]) for row in private
    ):
        raise ValueError("BT sample count does not match manifest")
    return {
        "counts": {
            "public_bank": len(public),
            "private_gold": len(private),
            "runtime_manifest": len(runtime),
        },
        "manifest_sha256": _sha256_bytes(artifacts["manifest"]),
    }


def _atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=".%s." % path.name, dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def write_bank(root=ITEMBANK_ROOT):
    artifacts = build_artifact_bytes()
    root = Path(root)
    for key, relative_path in ARTIFACT_PATHS.items():
        _atomic_write(root / relative_path, artifacts[key])
    return validate_artifact_bytes(artifacts)


if __name__ == "__main__":
    print(canonical_json(write_bank()))
