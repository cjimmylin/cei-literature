#!/usr/bin/env python3
"""Credential-free schema and public/private separation audit for ZEROSUM P1."""

from __future__ import annotations

import argparse
from collections import Counter
from collections.abc import Mapping, Sequence
from copy import deepcopy
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any, Dict, Iterable, List, Optional


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from itembank.build_bank import validate_bank  # noqa: E402


ITEMBANK = ROOT / "itembank"
DEFAULT_BANK = ITEMBANK / "bank" / "p1-private.jsonl"
DEFAULT_GOLD = ITEMBANK / "gold" / "p1-private.gold.jsonl"
DEFAULT_MANIFEST = ITEMBANK / "manifest.json"

SEVERITIES = frozenset(("hard", "soft"))


def make_finding(
    *,
    audit: str,
    code: str,
    severity: str,
    message: str,
    record_id: Optional[str] = None,
    details: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    """Create the stable JSON-safe finding shape shared by all static audits."""
    if severity not in SEVERITIES:
        raise ValueError("severity must be 'hard' or 'soft'")
    if not all(isinstance(value, str) and value.strip()
               for value in (audit, code, message)):
        raise ValueError("audit, code, and message must be nonempty strings")
    finding: Dict[str, Any] = {
        "audit": audit,
        "code": code,
        "severity": severity,
        "message": message,
    }
    if record_id is not None:
        finding["record_id"] = str(record_id)
    if details:
        finding["details"] = dict(details)
    return finding


def report_exit_code(findings: Iterable[Mapping[str, Any]]) -> int:
    """Return one only for hard findings; soft findings never block execution."""
    return int(any(finding.get("severity") == "hard" for finding in findings))


def _finding_sort_key(finding: Mapping[str, Any]) -> tuple:
    return (
        0 if finding.get("severity") == "hard" else 1,
        str(finding.get("code", "")),
        str(finding.get("record_id", "")),
        str(finding.get("message", "")),
    )


def write_reports(
    findings: Sequence[Mapping[str, Any]],
    *,
    audit_slug: str,
    audit_title: str,
    checked_records: int,
    output_dir: Path,
    report_date: Optional[str] = None,
) -> Dict[str, Path]:
    """Write deterministic JSONL findings and a human-readable dated summary."""
    report_date = report_date or date.today().isoformat()
    try:
        parsed_date = date.fromisoformat(report_date)
    except (TypeError, ValueError) as exc:
        raise ValueError("report_date must be YYYY-MM-DD") from exc
    if not isinstance(checked_records, int) or isinstance(checked_records, bool) or checked_records < 0:
        raise ValueError("checked_records must be a nonnegative integer")
    if not all(isinstance(value, str) and value.strip()
               for value in (audit_slug, audit_title)):
        raise ValueError("audit_slug and audit_title must be nonempty strings")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = parsed_date.strftime("%Y%m%d") + "-" + audit_slug
    paths = {
        "findings": output_dir / (prefix + "-findings.jsonl"),
        "summary": output_dir / (prefix + "-summary.md"),
    }
    ordered = sorted((dict(finding) for finding in findings), key=_finding_sort_key)
    findings_text = "".join(
        json.dumps(
            finding,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ) + "\n"
        for finding in ordered
    )
    paths["findings"].write_text(findings_text, encoding="utf-8")

    hard = sum(finding.get("severity") == "hard" for finding in ordered)
    soft = sum(finding.get("severity") == "soft" for finding in ordered)
    lines = [
        "# %s" % audit_title,
        "",
        "- Report date: %s" % report_date,
        "- Records checked: %d" % checked_records,
        "- Status: %s" % ("BLOCKED" if hard else "PASS"),
        "- Hard findings: %d" % hard,
        "- Soft findings: %d" % soft,
        "",
        "## Findings",
        "",
    ]
    if not ordered:
        lines.append("No findings.")
    else:
        for finding in ordered:
            location = (
                " (`%s`)" % finding["record_id"]
                if finding.get("record_id") else ""
            )
            lines.append(
                "- **%s — `%s`**%s: %s"
                % (
                    str(finding["severity"]).upper(),
                    finding["code"],
                    location,
                    finding["message"],
                )
            )
    paths["summary"].write_text("\n".join(lines) + "\n", encoding="utf-8")
    return paths


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    """Load a JSONL artifact strictly, including line-numbered parse failures."""
    records: List[Dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError("invalid JSON on line %d of %s" % (line_number, path)) from exc
            if not isinstance(value, dict):
                raise ValueError("line %d of %s is not a JSON object" % (line_number, path))
            records.append(value)
    return records


def _nested_key_paths(value: Any, prefix: tuple = ()) -> List[tuple]:
    paths: List[tuple] = []
    if isinstance(value, Mapping):
        for key, child in value.items():
            path = prefix + (str(key),)
            paths.append(path)
            paths.extend(_nested_key_paths(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            paths.extend(_nested_key_paths(child, prefix + (str(index),)))
    return paths


def _canonical_jsonl_bytes(records: Iterable[Mapping[str, Any]]) -> bytes:
    lines = [
        json.dumps(
            record,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        for record in records
    ]
    return (("\n".join(lines) + "\n") if lines else "").encode("utf-8")


def _valid_rho(value: Any, rho_grid: Sequence[Any]) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        and any(value == registered for registered in rho_grid)
    )


def _add(
    findings: List[Dict[str, Any]],
    code: str,
    message: str,
    *,
    record_id: Optional[str] = None,
    details: Optional[Mapping[str, Any]] = None,
) -> None:
    findings.append(make_finding(
        audit="schema",
        code=code,
        severity="hard",
        message=message,
        record_id=record_id,
        details=details,
    ))


def audit_schema(
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
) -> List[Dict[str, Any]]:
    """Pure fail-closed validation of schemas, linkage, rho, canaries, and gold poles."""
    findings: List[Dict[str, Any]] = []
    if not isinstance(bank, Sequence) or isinstance(bank, (str, bytes)):
        _add(findings, "schema.bank_not_sequence", "Public bank must be a sequence of objects.")
        return findings
    if not isinstance(gold, Sequence) or isinstance(gold, (str, bytes)):
        _add(findings, "schema.gold_not_sequence", "Private gold must be a sequence of objects.")
        return findings
    if not isinstance(manifest, Mapping):
        _add(findings, "schema.manifest_not_object", "Manifest must be an object.")
        return findings

    # JSON object key order is not semantic, but the Task-4 option shuffler uses
    # the authored class order. Restore that order from the certificate's option
    # list before invoking the independent full-bank validator on loaded JSONL.
    semantic_gold = deepcopy(list(gold))
    for record in semantic_gold:
        if not isinstance(record, dict) or record.get("record_type") != "advice_primary":
            continue
        option_text = record.get("option_text_by_class")
        certificate = record.get("certificate")
        certificate_options = (
            certificate.get("options") if isinstance(certificate, Mapping) else None
        )
        if isinstance(option_text, Mapping) and isinstance(certificate_options, list):
            classes = [
                option.get("class") for option in certificate_options
                if isinstance(option, Mapping)
            ]
            if len(classes) == len(option_text) and set(classes) == set(option_text):
                record["option_text_by_class"] = {
                    advice_class: option_text[advice_class]
                    for advice_class in classes
                }
    try:
        validate_bank(bank, semantic_gold)
    except Exception as exc:
        _add(
            findings,
            "schema.full_bank_semantics",
            "Full-bank semantic validation failed: %s" % exc,
            details={"exception_type": type(exc).__name__},
        )

    public_allowlists = manifest.get("public_key_allowlists")
    private_allowlists = manifest.get("private_key_allowlists")
    rho_grid = manifest.get("rho_grid")
    forbidden = manifest.get("public_forbidden_fields")
    for name, value in (
        ("public_key_allowlists", public_allowlists),
        ("private_key_allowlists", private_allowlists),
    ):
        if not isinstance(value, Mapping):
            _add(findings, "schema.manifest_contract", "Manifest %s must be an object." % name)
    if not isinstance(rho_grid, list) or not rho_grid:
        _add(findings, "schema.manifest_contract", "Manifest rho_grid must be a nonempty list.")
        rho_grid = []
    if not isinstance(forbidden, list) or not all(isinstance(item, str) for item in forbidden):
        _add(findings, "schema.manifest_contract", "Manifest public_forbidden_fields must be a string list.")
        forbidden = []

    expected_counts = manifest.get("counts", {})
    expected_total = expected_counts.get("total") if isinstance(expected_counts, Mapping) else None
    expected_by_type = (
        expected_counts.get("by_record_type")
        if isinstance(expected_counts, Mapping) else None
    )
    actual_by_type = Counter(
        record.get("record_type") if isinstance(record, Mapping) else None
        for record in bank
    )
    if expected_total != len(bank) or not isinstance(expected_by_type, Mapping) or dict(actual_by_type) != dict(expected_by_type):
        _add(
            findings,
            "schema.count_mismatch",
            "Public bank counts do not match the frozen manifest.",
            details={"actual_total": len(bank), "expected_total": expected_total},
        )
    if len(gold) != len(bank):
        _add(findings, "schema.gold_count_mismatch", "Public and private record counts differ.")

    gold_by_id: Dict[Any, Mapping[str, Any]] = {}
    gold_ids: List[Any] = []
    for index, record in enumerate(gold):
        if not isinstance(record, Mapping):
            _add(findings, "schema.private_not_object", "Private record is not an object.", record_id="index:%d" % index)
            continue
        record_id = record.get("id")
        gold_ids.append(record_id)
        if not isinstance(record_id, str) or not record_id:
            _add(findings, "schema.private_missing_id", "Private record lacks a nonempty id.", record_id="index:%d" % index)
        elif record_id in gold_by_id:
            _add(findings, "schema.duplicate_private_id", "Private record id is duplicated.", record_id=record_id)
        else:
            gold_by_id[record_id] = record

    public_ids: List[Any] = []
    seen_public_ids = set()
    valid_canaries: List[str] = []
    for index, record in enumerate(bank):
        if not isinstance(record, Mapping):
            _add(findings, "schema.public_not_object", "Public record is not an object.", record_id="index:%d" % index)
            continue
        record_id = record.get("id")
        public_ids.append(record_id)
        finding_id = record_id if isinstance(record_id, str) and record_id else "index:%d" % index
        if not isinstance(record_id, str) or not record_id:
            _add(findings, "schema.public_missing_id", "Public record lacks a nonempty id.", record_id=finding_id)
        elif record_id in seen_public_ids:
            _add(findings, "schema.duplicate_public_id", "Public record id is duplicated.", record_id=record_id)
        else:
            seen_public_ids.add(record_id)

        kind = record.get("record_type")
        allowed_public = (
            public_allowlists.get(kind)
            if isinstance(public_allowlists, Mapping) else None
        )
        if not isinstance(allowed_public, list) or set(record) != set(allowed_public):
            _add(
                findings,
                "schema.public_schema_mismatch",
                "Public keys do not exactly match the record-type allowlist.",
                record_id=finding_id,
                details={"record_type": kind},
            )
        leaked_paths = [
            ".".join(path)
            for path in _nested_key_paths(record)
            if path and path[-1] in forbidden
        ]
        if leaked_paths:
            _add(
                findings,
                "schema.public_forbidden_field",
                "Private scoring keys appear in a model-facing record.",
                record_id=finding_id,
                details={"paths": sorted(leaked_paths)},
            )

        rho = record.get("rho")
        if not _valid_rho(rho, rho_grid):
            _add(findings, "schema.rho_outside_grid", "rho is outside the registered grid.", record_id=finding_id)
        if record.get("payoff_correlation") != rho:
            _add(findings, "schema.rho_alias_mismatch", "payoff_correlation must equal rho.", record_id=finding_id)

        canary = record.get("canary")
        if not isinstance(canary, str) or not canary.strip():
            _add(findings, "schema.missing_canary", "Record lacks a nonempty canonical canary.", record_id=finding_id)
        else:
            valid_canaries.append(canary)
        if record.get("record_canary") != canary:
            _add(findings, "schema.record_canary_mismatch", "record_canary must equal canary.", record_id=finding_id)
        surface_canary = record.get("surface_canary")
        model_prompt = record.get("model_prompt")
        if not isinstance(surface_canary, str) or not surface_canary.strip():
            _add(findings, "schema.missing_surface_canary", "Record lacks a nonempty surface canary.", record_id=finding_id)
        elif not isinstance(model_prompt, str) or surface_canary not in model_prompt:
            _add(findings, "schema.surface_canary_not_rendered", "Surface canary is absent from model_prompt.", record_id=finding_id)

        gold_record = gold_by_id.get(record_id)
        if gold_record is None:
            _add(findings, "schema.missing_private_record", "No aligned private record exists.", record_id=finding_id)
            continue
        allowed_private = (
            private_allowlists.get(kind)
            if isinstance(private_allowlists, Mapping) else None
        )
        if not isinstance(allowed_private, list) or set(gold_record) != set(allowed_private):
            _add(
                findings,
                "schema.private_schema_mismatch",
                "Private keys do not exactly match the record-type allowlist.",
                record_id=finding_id,
                details={"record_type": kind},
            )
        for field in ("id", "record_type", "core_id", "certificate_id", "rho", "sf_cell"):
            if gold_record.get(field) != record.get(field):
                _add(
                    findings,
                    "schema.public_private_mismatch",
                    "Public/private linkage field %s differs." % field,
                    record_id=finding_id,
                    details={"field": field},
                )
        if kind == "advice_primary":
            modes = gold_record.get("failure_modes")
            normalized = [mode.lower() for mode in modes] if (
                isinstance(modes, list) and all(isinstance(mode, str) for mode in modes)
            ) else []
            has_positional = any(
                "positional" in mode and "sycophantic" in mode
                for mode in normalized
            )
            has_harmony = any(
                "naive-positivity" in mode and "harmony-theater" in mode
                for mode in normalized
            )
            if not (has_positional and has_harmony):
                _add(
                    findings,
                    "schema.two_sided_failure_poles",
                    "Primary gold must include positional/sycophantic and naive-positivity/harmony-theater poles.",
                    record_id=finding_id,
                )

    if public_ids != gold_ids:
        _add(findings, "schema.id_order_mismatch", "Public and private ids are not aligned in order.")
    if len(valid_canaries) != len(set(valid_canaries)):
        _add(findings, "schema.duplicate_canary", "Canonical record canaries are not unique.")

    artifacts = manifest.get("artifacts")
    for name, records in (("bank", bank), ("gold", gold)):
        expected_hash = None
        if isinstance(artifacts, Mapping) and isinstance(artifacts.get(name), Mapping):
            expected_hash = artifacts[name].get("sha256")
        try:
            actual_hash = hashlib.sha256(_canonical_jsonl_bytes(records)).hexdigest()
        except (TypeError, ValueError):
            actual_hash = None
        if not isinstance(expected_hash, str) or actual_hash != expected_hash:
            _add(
                findings,
                "schema.artifact_hash_mismatch",
                "%s content does not match the frozen manifest hash." % name.capitalize(),
                details={"artifact": name},
            )
    return sorted(findings, key=_finding_sort_key)


def _input_error(exc: Exception) -> List[Dict[str, Any]]:
    return [make_finding(
        audit="schema",
        code="schema.input_error",
        severity="hard",
        message=str(exc),
    )]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bank", type=Path, default=DEFAULT_BANK)
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "reports")
    parser.add_argument("--report-date", default=None)
    args = parser.parse_args(argv)
    checked_records = 0
    try:
        bank = load_jsonl(args.bank)
        checked_records = len(bank)
        gold = load_jsonl(args.gold)
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        findings = audit_schema(bank, gold, manifest)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        findings = _input_error(exc)
    write_reports(
        findings,
        audit_slug="schema-audit",
        audit_title="ZEROSUM P1 schema audit",
        checked_records=checked_records,
        output_dir=args.output_dir,
        report_date=args.report_date,
    )
    return report_exit_code(findings)


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "audit_schema", "load_jsonl", "main", "make_finding",
    "report_exit_code", "write_reports",
]
