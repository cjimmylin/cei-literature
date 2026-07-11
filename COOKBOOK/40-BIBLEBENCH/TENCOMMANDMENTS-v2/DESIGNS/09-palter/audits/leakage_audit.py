"""Scan public and runtime projections for private or self-scoring fields."""

from itembank.generator import build_rows
from palter_schemas import PRIVATE_ONLY_FIELDS


FORBIDDEN_KEYS = PRIVATE_ONLY_FIELDS | frozenset(
    {
        "claim_atoms",
        "reader_probe_answers",
        "unsupported_claim_ids",
    }
)


def _walk(value, projection, row_id, path, findings):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = "%s.%s" % (path, key) if path else key
            if key in FORBIDDEN_KEYS:
                findings.append(
                    {
                        "projection": projection,
                        "row_id": row_id,
                        "path": child_path,
                        "forbidden_key": key,
                    }
                )
            _walk(child, projection, row_id, child_path, findings)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _walk(child, projection, row_id, "%s[%s]" % (path, index), findings)


def run_leakage_audit(public_rows=None, runtime_rows=None):
    if public_rows is None or runtime_rows is None:
        generated_public, _, generated_runtime = build_rows()
        public_rows = generated_public if public_rows is None else public_rows
        runtime_rows = generated_runtime if runtime_rows is None else runtime_rows
    findings = []
    for projection, rows in (("public", public_rows), ("runtime", runtime_rows)):
        for index, row in enumerate(rows):
            row_id = row.get("id", row.get("source_record_id", "row-%s" % index))
            _walk(row, projection, row_id, "", findings)
            identifier = row.get("id", row.get("runtime_request_id", ""))
            for leaked_label in ("-faithful", "-paltered"):
                if leaked_label in identifier:
                    findings.append(
                        {
                            "projection": projection,
                            "row_id": row_id,
                            "path": "id",
                            "forbidden_key": "gold_label_in_identifier",
                        }
                    )
    return {
        "status": "PASS" if not findings else "FAIL",
        "rows_scanned": {"public": len(public_rows), "runtime": len(runtime_rows)},
        "forbidden_keys": sorted(FORBIDDEN_KEYS),
        "findings": findings,
    }


__all__ = ["run_leakage_audit"]
