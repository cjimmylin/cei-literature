"""Recursive private-field leakage audit for public and runtime projections."""

from tablets_schemas import PRIVATE_ONLY_FIELDS

from audits.schema_balance import parse_jsonl_bytes, read_artifact_bytes


_EXPLICIT_FORBIDDEN_FIELDS = set(PRIVATE_ONLY_FIELDS) | {
    "action_map",
    "action_to_outcome",
    "answer_key",
    "correct_answer",
    "expected_answer",
    "gold_answer",
    "gold_band",
    "gold_label",
    "outcome_map",
    "preferred_answer",
}
_NORMALIZED_EXPLICIT_FORBIDDEN_FIELDS = {
    field.lower() for field in _EXPLICIT_FORBIDDEN_FIELDS
}


def _forbidden_rule(field):
    normalized = field.lower()
    if normalized in _NORMALIZED_EXPLICIT_FORBIDDEN_FIELDS:
        return "private_or_answer_field"
    if normalized.startswith("authoring_"):
        return "authoring_field"
    if "gold" in normalized:
        return "gold_field"
    if normalized == "evidence" or normalized.endswith("_evidence"):
        return "evidence_field"
    if normalized.startswith("expected_") or normalized.endswith("_answer"):
        return "expected_answer_field"
    if "action" in normalized and normalized.endswith("_map"):
        return "action_map_field"
    return None


def _recursive_hits(value, path):
    hits = []
    if type(value) is dict:
        for field in sorted(value):
            child_path = "%s.%s" % (path, field)
            rule = _forbidden_rule(field)
            if rule is not None:
                hits.append({"field": field, "path": child_path, "rule": rule})
            hits.extend(_recursive_hits(value[field], child_path))
    elif type(value) is list:
        for index, child in enumerate(value):
            hits.extend(_recursive_hits(child, "%s[%d]" % (path, index)))
    return hits


def audit_leakage(tablets_root=None, artifact_bytes=None):
    """Fail on private, authoring, gold, evidence, or answer keys at any depth."""
    artifacts, source = read_artifact_bytes(tablets_root, artifact_bytes)
    rows_by_projection = {
        "public": parse_jsonl_bytes(artifacts["public"], "public"),
        "runtime": parse_jsonl_bytes(artifacts["runtime"], "runtime"),
    }
    sections = {}
    for projection in ("public", "runtime"):
        rows = rows_by_projection[projection]
        hits = []
        for index, row in enumerate(rows):
            hits.extend(_recursive_hits(row, "$[%d]" % index))
        hits = sorted(hits, key=lambda item: (item["path"], item["field"]))
        if hits:
            first = hits[0]
            raise ValueError(
                "TABLETS private-field leakage: forbidden field %r at %s"
                % (first["field"], first["path"])
            )
        sections[projection] = {
            "status": "PASS",
            "records_scanned": len(rows),
            "forbidden_field_hits": [],
        }
    return {
        "audit": "TABLETS_PRIVATE_FIELD_LEAKAGE",
        "schema_version": "tablets-structural-audit.v1",
        "status": "PASS",
        "source": source,
        "sections": sections,
    }


__all__ = ["audit_leakage"]
