"""Credential-free exact schema, artifact, count, and balance audit."""

from collections import Counter
import hashlib
import json

from itembank.build_bank import (
    ARTIFACT_PATHS,
    ITEMBANK_ROOT,
    build_artifact_bytes,
    validate_artifact_bytes,
)


def _disk_artifacts():
    return {
        key: (ITEMBANK_ROOT / relative_path).read_bytes()
        for key, relative_path in ARTIFACT_PATHS.items()
    }


def _jsonl(data):
    return [json.loads(line) for line in data.decode("utf-8").splitlines()]


def run_schema_balance_audit(artifact_bytes=None):
    findings = []
    try:
        artifacts = _disk_artifacts() if artifact_bytes is None else artifact_bytes
        validation = validate_artifact_bytes(artifacts)
        if artifact_bytes is None:
            expected = build_artifact_bytes()
            for key in ARTIFACT_PATHS:
                if artifacts[key] != expected[key]:
                    findings.append("on-disk %s differs from deterministic rebuild" % key)
        public = _jsonl(artifacts["public_bank"])
        counts = Counter(row["record_type"] for row in public)
        monitored = [row for row in public if row["record_type"] == "monitoring_twin"]
        monitoring_balance = {
            "fraction_of_primary": len(monitored) / float(counts["composition"]),
            "per_tier": dict(sorted(Counter(row["incentive_tier"] for row in monitored).items())),
            "per_direction": dict(sorted(Counter(row["direction"] for row in monitored).items())),
        }
        exact_counts = {
            "composition": counts["composition"],
            "no_incentive_twin": counts["no_incentive_twin"],
            "monitoring_twin": counts["monitoring_twin"],
            "recognition": counts["recognition"],
            "detection": counts["detection"],
            "total": len(public),
        }
        if exact_counts != {
            "composition": 160,
            "no_incentive_twin": 40,
            "monitoring_twin": 32,
            "recognition": 40,
            "detection": 40,
            "total": 312,
        }:
            findings.append("record counts differ from the frozen 312-row schedule")
        if monitoring_balance != {
            "fraction_of_primary": 0.2,
            "per_tier": {"T1": 8, "T2": 8, "T3": 8, "T4": 8},
            "per_direction": {"deflate": 16, "inflate": 16},
        }:
            findings.append("monitoring rows are not balanced by tier and direction")
        return {
            "status": "PASS" if not findings else "FAIL",
            "counts": exact_counts,
            "monitoring_balance": {
                "fraction_of_primary": monitoring_balance["fraction_of_primary"],
                "per_tier": monitoring_balance["per_tier"],
                "per_direction": {
                    "inflate": monitoring_balance["per_direction"].get("inflate", 0),
                    "deflate": monitoring_balance["per_direction"].get("deflate", 0),
                },
            },
            "artifact_sha256": {
                key: hashlib.sha256(value).hexdigest()
                for key, value in sorted(artifacts.items())
            },
            "validated_manifest_sha256": validation["manifest_sha256"],
            "findings": findings,
        }
    except Exception as exc:
        return {
            "status": "FAIL",
            "counts": {},
            "monitoring_balance": {},
            "artifact_sha256": {},
            "validated_manifest_sha256": None,
            "findings": ["%s: %s" % (type(exc).__name__, exc)],
        }


__all__ = ["run_schema_balance_audit"]
