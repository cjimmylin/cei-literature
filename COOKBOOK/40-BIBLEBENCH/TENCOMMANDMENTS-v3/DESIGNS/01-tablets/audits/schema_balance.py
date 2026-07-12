"""Strict disk-byte, schema, hash, and balance audit for TABLETS P1."""

from collections import Counter
import hashlib
import json
from pathlib import Path

from itembank.build_bank import build_artifact_bytes, validate_artifact_bytes


TABLETS_ROOT = Path(__file__).resolve().parents[1]
_ARTIFACT_PATHS = {
    "public": Path("itembank/bank/p1-public.jsonl"),
    "private": Path("itembank/gold/p1-private.gold.jsonl"),
    "runtime": Path("itembank/runtime/p1-runtime-manifest.jsonl"),
    "manifest": Path("itembank/manifest.json"),
}
_EXPECTED_HASHES = {
    "manifest": "ec3a41aa0e786af65c3e520bd770dc2d021e738d656889ec0fc0420ad6706ce8",
    "private": "597aeb5a5c4f4c07095068663134e59cd6a90b9d6dee56faef778e3a418cb7ef",
    "public": "5c60194de2a1fd57276af83706bd8ff536749ee5039611711de7e5da61b44b4d",
    "runtime": "537c2dcd57b75966880ff47696a414ab74229b654864d7f139abb255d0967d5f",
}
_EXPECTED_RECORD_TYPES = {
    "adjudication": 342,
    "comprehension": 45,
    "monitoring_twin": 69,
    "recognition": 45,
    "threat_twin": 135,
}
_EXPECTED_SEVERITY_TIERS = {"T1": 320, "T2": 44, "T3": 43, "T4": 229}
_EXPECTED_DIRECTIONS = {"A_FIRST": 320, "B_FIRST": 316}
_EXPECTED_FRAMING = {"neutral": 501, "threat": 135}
_EXPECTED_MONITORING = {"monitored": 69, "unmonitored": 567}


def read_artifact_bytes(tablets_root=None, artifact_bytes=None):
    """Read the four frozen artifacts from disk or accept explicit test bytes."""
    if tablets_root is not None and artifact_bytes is not None:
        raise ValueError("provide tablets_root or artifact_bytes, not both")
    if artifact_bytes is not None:
        if type(artifact_bytes) is not dict or set(artifact_bytes) != set(
            _ARTIFACT_PATHS
        ):
            raise ValueError("injected artifact byte set is incomplete")
        if not all(type(payload) is bytes for payload in artifact_bytes.values()):
            raise ValueError("injected artifacts must be raw bytes")
        return dict(artifact_bytes), "INJECTED_BYTES"
    root = TABLETS_ROOT if tablets_root is None else Path(tablets_root)
    artifacts = {
        name: (root / relative).read_bytes()
        for name, relative in _ARTIFACT_PATHS.items()
    }
    return artifacts, "DISK"


def parse_jsonl_bytes(payload, label):
    """Parse canonical JSONL strictly enough for independent structural scans."""
    if type(payload) is not bytes:
        raise ValueError("%s artifact must be bytes" % label)
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("%s artifact is not UTF-8" % label) from error
    if not text.endswith("\n") or not text.strip():
        raise ValueError("%s JSONL artifact has deterministic byte drift" % label)
    lines = text.splitlines()
    if any(not line for line in lines):
        raise ValueError("%s JSONL artifact contains a blank row" % label)
    try:
        rows = [json.loads(line) for line in lines]
    except json.JSONDecodeError as error:
        raise ValueError("%s JSONL artifact is invalid" % label) from error
    if not all(type(row) is dict for row in rows):
        raise ValueError("%s JSONL rows must be objects" % label)
    return rows


def _exact_counter(rows, field, expected, label):
    observed = dict(sorted(Counter(row[field] for row in rows).items()))
    if observed != expected:
        raise ValueError("TABLETS %s balance drift" % label)
    return observed


def audit_schema_balance(tablets_root=None, artifact_bytes=None):
    """Validate exact disk bytes and the frozen 636-row schedule."""
    artifacts, source = read_artifact_bytes(tablets_root, artifact_bytes)
    try:
        validate_artifact_bytes(artifacts)
    except (TypeError, ValueError) as error:
        raise ValueError(
            "TABLETS artifact strict validation or deterministic byte drift: %s"
            % error
        ) from error

    expected = build_artifact_bytes()
    for name in sorted(expected):
        if artifacts[name] != expected[name]:
            raise ValueError("TABLETS %s deterministic byte drift" % name)
    hashes = {
        name: hashlib.sha256(artifacts[name]).hexdigest()
        for name in sorted(artifacts)
    }
    if hashes != _EXPECTED_HASHES:
        raise ValueError("TABLETS frozen artifact hash drift")

    public = parse_jsonl_bytes(artifacts["public"], "public")
    if len(public) != 636:
        raise ValueError("TABLETS public record count drift")
    record_types = _exact_counter(
        public, "record_type", _EXPECTED_RECORD_TYPES, "record-type"
    )
    severity_tiers = _exact_counter(
        public, "severity_tier", _EXPECTED_SEVERITY_TIERS, "severity-tier"
    )
    directions = _exact_counter(
        public, "direction_permutation", _EXPECTED_DIRECTIONS, "direction"
    )
    framing = _exact_counter(
        public, "framing_arm", _EXPECTED_FRAMING, "threat-framing"
    )
    monitoring = _exact_counter(
        public, "monitoring_condition", _EXPECTED_MONITORING, "monitoring"
    )
    return {
        "audit": "TABLETS_SCHEMA_BALANCE",
        "schema_version": "tablets-structural-audit.v1",
        "status": "PASS",
        "source": source,
        "sections": {
            "artifacts": {
                "status": "PASS",
                "deterministic_byte_equality": True,
                "sha256": hashes,
            },
            "schema": {
                "status": "PASS",
                "strict_validation": True,
                "public_rows": 636,
                "private_rows": 636,
                "runtime_rows": 636,
            },
            "balance": {
                "status": "PASS",
                "record_count": 636,
                "record_type_counts": record_types,
                "severity_tier_counts": severity_tiers,
                "direction_counts": directions,
                "framing_counts": framing,
                "monitoring_counts": monitoring,
                "threat_twin_count": 135,
                "monitoring_twin_count": 69,
            },
        },
    }


__all__ = [
    "TABLETS_ROOT",
    "audit_schema_balance",
    "parse_jsonl_bytes",
    "read_artifact_bytes",
]
