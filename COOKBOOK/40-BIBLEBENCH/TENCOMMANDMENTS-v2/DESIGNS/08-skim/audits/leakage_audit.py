#!/usr/bin/env python3
"""Credential-free private-field and canary audit for SKIM P1."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audits.schema_audit import (  # noqa: E402
    add_common_cli_arguments,
    load_audit_inputs,
    make_finding,
    report_exit_code,
    write_reports,
)
from skim_constants import (  # noqa: E402
    PRIVATE_GOLD_FIELDS,
    PRIVATE_ONLY_FIELDS,
    PUBLIC_ITEM_FIELDS,
    REQUEST_FIELDS,
)


_PRIVATE_FIELDS = frozenset(PRIVATE_ONLY_FIELDS)
_PRIVATE_GOLD_FIELDS = frozenset(PRIVATE_GOLD_FIELDS)
_PUBLIC_ITEM_FIELDS = frozenset(PUBLIC_ITEM_FIELDS)
_REQUEST_FIELDS = frozenset(REQUEST_FIELDS)


def _rows(value):
    return type(value) in (list, tuple)


def _nonblank_string(value):
    return type(value) is str and bool(value.strip())


def _path_text(parts):
    text = ""
    for part in parts:
        if type(part) is int:
            text += "[%d]" % part
        elif text:
            text += "." + part
        else:
            text = part
    return text


def _private_paths(value, prefix=(), active=None):
    """Return deterministic paths whose exact key is private-only."""

    if active is None:
        active = set()
    if type(value) is dict:
        marker = id(value)
        if marker in active:
            raise ValueError("cyclic JSON object in audit input")
        active.add(marker)
        try:
            paths = []
            for key, child in value.items():
                if type(key) is not str:
                    raise ValueError("audit JSON object key is not an exact string")
                child_prefix = prefix + (key,)
                if key in _PRIVATE_FIELDS:
                    paths.append(_path_text(child_prefix))
                paths.extend(_private_paths(child, child_prefix, active))
            return paths
        finally:
            active.remove(marker)
    if type(value) in (list, tuple):
        marker = id(value)
        if marker in active:
            raise ValueError("cyclic JSON sequence in audit input")
        active.add(marker)
        try:
            paths = []
            for index, child in enumerate(value):
                paths.extend(_private_paths(child, prefix + (index,), active))
            return paths
        finally:
            active.remove(marker)
    return []


def _gold_marked_paths(value, prefix=(), active=None):
    """Return deterministic paths whose key contains ``gold`` case-insensitively."""

    if active is None:
        active = set()
    if type(value) is dict:
        marker = id(value)
        if marker in active:
            raise ValueError("cyclic JSON object in audit input")
        active.add(marker)
        try:
            paths = []
            for key, child in value.items():
                if type(key) is not str:
                    raise ValueError("audit JSON object key is not an exact string")
                child_prefix = prefix + (key,)
                if "gold" in key.casefold():
                    paths.append(_path_text(child_prefix))
                paths.extend(_gold_marked_paths(child, child_prefix, active))
            return paths
        finally:
            active.remove(marker)
    if type(value) in (list, tuple):
        marker = id(value)
        if marker in active:
            raise ValueError("cyclic JSON sequence in audit input")
        active.add(marker)
        try:
            paths = []
            for index, child in enumerate(value):
                paths.extend(
                    _gold_marked_paths(child, prefix + (index,), active)
                )
            return paths
        finally:
            active.remove(marker)
    return []


def _record_id(row, index, surface):
    if type(row) is dict:
        for key in (
            "logical_record_id",
            "runtime_request_id",
            "source_logical_record_id",
        ):
            value = row.get(key)
            if _nonblank_string(value):
                return value
    return "%s:index:%d" % (surface, index)


def _hard(findings, code, message, *, record_id=None, details=None):
    findings.append(
        make_finding(
            audit="leakage",
            code=code,
            severity="hard",
            message=message,
            record_id=record_id,
            details=details,
        )
    )


def _canary_finding(findings, message, *, record_id=None, details=None):
    _hard(
        findings,
        "leakage.missing_canary",
        message,
        record_id=record_id,
        details=details,
    )


def _sorted_findings(findings):
    return sorted(
        findings,
        key=lambda finding: (
            0 if finding.get("severity") == "hard" else 1,
            str(finding.get("code", "")),
            str(finding.get("record_id", "")),
            str(finding.get("message", "")),
            json.dumps(
                finding.get("details", {}),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            ),
        ),
    )


def _audit_leakage(public, gold, runtime):
    findings = []
    if not _rows(public):
        _hard(
            findings,
            "leakage.input_error",
            "Public bank must be an exact list or tuple of JSON objects.",
        )
        return _sorted_findings(findings)
    if not _rows(runtime):
        _hard(
            findings,
            "leakage.input_error",
            "Runtime manifest must be an exact list or tuple of JSON objects.",
        )
        return _sorted_findings(findings)
    if not _rows(gold):
        _hard(
            findings,
            "leakage.input_error",
            "Private gold must be an exact list or tuple of JSON objects.",
        )
        return _sorted_findings(findings)

    public_by_id = {}
    request_by_id = {}
    public_surface_canaries = []
    public_record_canaries = []
    public_request_canaries = []
    surface_by_core = defaultdict(set)
    core_by_surface = defaultdict(set)
    core_counts = Counter()
    expected_runtime_canaries = []
    expected_record_multiplicity = Counter()

    for index, row in enumerate(public):
        finding_id = _record_id(row, index, "public")
        if type(row) is not dict:
            _hard(
                findings,
                "leakage.input_error",
                "Public row is not an exact JSON object.",
                record_id=finding_id,
            )
            continue

        if set(row) != _PUBLIC_ITEM_FIELDS:
            _hard(
                findings,
                "leakage.public_allowlist",
                "Public row fields differ from the exact public allowlist.",
                record_id=finding_id,
                details={
                    "extra_fields": sorted(set(row) - _PUBLIC_ITEM_FIELDS),
                    "missing_fields": sorted(_PUBLIC_ITEM_FIELDS - set(row)),
                    "surface": "public",
                },
            )

        private_paths = sorted(set(_private_paths(row)))
        if private_paths:
            _hard(
                findings,
                "leakage.private_field_in_public",
                "Private-only field names appear in a model-facing public row.",
                record_id=finding_id,
                details={"surface": "public", "paths": private_paths},
            )

        logical_id = row.get("logical_record_id")
        core_id = row.get("core_id")
        surface_canary = row.get("surface_canary")
        record_canary = row.get("record_canary")
        alias_canary = row.get("canary")
        canaries_valid = all(
            _nonblank_string(value)
            for value in (surface_canary, record_canary, alias_canary)
        )
        if not canaries_valid:
            _canary_finding(
                findings,
                "Public row is missing a nonblank surface, record, or alias canary.",
                record_id=finding_id,
            )
        elif alias_canary != record_canary:
            _canary_finding(
                findings,
                "Public alias canary does not equal its record canary.",
                record_id=finding_id,
                details={
                    "alias_canary": alias_canary,
                    "record_canary": record_canary,
                },
            )

        if _nonblank_string(logical_id):
            if logical_id in public_by_id:
                _hard(
                    findings,
                    "leakage.input_error",
                    "Public logical-record ID is duplicated.",
                    record_id=logical_id,
                )
            else:
                public_by_id[logical_id] = row
        else:
            _hard(
                findings,
                "leakage.input_error",
                "Public row lacks a nonblank logical-record ID.",
                record_id=finding_id,
            )

        if _nonblank_string(core_id):
            core_counts[core_id] += 1
            if _nonblank_string(surface_canary):
                surface_by_core[core_id].add(surface_canary)
                core_by_surface[surface_canary].add(core_id)
        else:
            _hard(
                findings,
                "leakage.input_error",
                "Public row lacks a nonblank core ID.",
                record_id=finding_id,
            )
        if _nonblank_string(surface_canary):
            public_surface_canaries.append(surface_canary)
        if _nonblank_string(record_canary):
            public_record_canaries.append(record_canary)

        requests = row.get("requests")
        if type(requests) is not list:
            _canary_finding(
                findings,
                "Public row has no exact request list for canary inspection.",
                record_id=finding_id,
            )
            continue
        if _nonblank_string(record_canary):
            expected_record_multiplicity[record_canary] += len(requests)
        for request_index, request in enumerate(requests):
            request_finding_id = "%s:request:%d" % (finding_id, request_index)
            if type(request) is not dict:
                _hard(
                    findings,
                    "leakage.public_allowlist",
                    "Public request is not an exact JSON object.",
                    record_id=request_finding_id,
                    details={"surface": "request"},
                )
                _canary_finding(
                    findings,
                    "Public request is not an exact JSON object.",
                    record_id=request_finding_id,
                )
                continue
            if set(request) != _REQUEST_FIELDS:
                _hard(
                    findings,
                    "leakage.public_allowlist",
                    "Public request fields differ from the exact request allowlist.",
                    record_id=request_finding_id,
                    details={
                        "extra_fields": sorted(set(request) - _REQUEST_FIELDS),
                        "missing_fields": sorted(_REQUEST_FIELDS - set(request)),
                        "surface": "request",
                    },
                )
            request_id = request.get("request_id")
            request_canary = request.get("canary")
            if not _nonblank_string(request_canary):
                _canary_finding(
                    findings,
                    "Public request is missing a nonblank request canary.",
                    record_id=request_finding_id,
                )
            else:
                public_request_canaries.append(request_canary)
            if _nonblank_string(request_id):
                if request_id in request_by_id:
                    _hard(
                        findings,
                        "leakage.input_error",
                        "Public request ID is duplicated.",
                        record_id=request_id,
                    )
                else:
                    request_by_id[request_id] = request
            else:
                _hard(
                    findings,
                    "leakage.input_error",
                    "Public request lacks a nonblank request ID.",
                    record_id=request_finding_id,
                )

            state = request.get("structured_state")
            surface_reference = (
                state.get("surface_reference") if type(state) is dict else None
            )
            if (
                not _nonblank_string(surface_canary)
                or surface_reference != surface_canary
            ):
                _canary_finding(
                    findings,
                    "Request surface reference does not mirror the row surface canary.",
                    record_id=request_id or request_finding_id,
                )
            options = request.get("options")
            if type(options) is not list or not options:
                _canary_finding(
                    findings,
                    "Request has no option labels carrying its surface canary.",
                    record_id=request_id or request_finding_id,
                )
            elif _nonblank_string(surface_canary) and any(
                type(option) is not dict
                or not _nonblank_string(option.get("label"))
                or surface_canary not in option["label"]
                for option in options
            ):
                _canary_finding(
                    findings,
                    "Every option label must carry the model-visible surface canary.",
                    record_id=request_id or request_finding_id,
                )

            expected_runtime_canaries.append(
                (surface_canary, record_canary, request_canary)
            )

    if (
        len(public) != 640
        or len(core_counts) != 40
        or set(core_counts.values()) != {16}
        or len(surface_by_core) != 40
        or any(len(values) != 1 for values in surface_by_core.values())
        or len(core_by_surface) != 40
        or any(len(values) != 1 for values in core_by_surface.values())
        or len(public_surface_canaries) != 640
        or len(set(public_surface_canaries)) != 40
        or set(Counter(public_surface_canaries).values()) != {16}
    ):
        _canary_finding(
            findings,
            (
                "Surface canaries must form exactly forty one-to-one core "
                "strata with sixteen public rows each."
            ),
            details={
                "public_rows": len(public),
                "core_count": len(core_counts),
                "unique_surface_canaries": len(set(public_surface_canaries)),
            },
        )
    if len(public_record_canaries) != 640 or len(set(public_record_canaries)) != 640:
        _canary_finding(
            findings,
            "Record canaries must be nonblank and globally unique across all 640 public rows.",
            details={
                "record_canaries": len(public_record_canaries),
                "unique_record_canaries": len(set(public_record_canaries)),
            },
        )
    if len(public_request_canaries) != 800 or len(set(public_request_canaries)) != 800:
        _canary_finding(
            findings,
            "Request canaries must be nonblank and globally unique across all 800 public requests.",
            details={
                "request_canaries": len(public_request_canaries),
                "unique_request_canaries": len(set(public_request_canaries)),
            },
        )

    seen_private_ids = set()
    for index, row in enumerate(gold):
        finding_id = _record_id(row, index, "private")
        if type(row) is not dict:
            _hard(
                findings,
                "leakage.private_allowlist",
                "Private row is not an exact JSON object.",
                record_id=finding_id,
            )
            continue
        if set(row) != _PRIVATE_GOLD_FIELDS:
            _hard(
                findings,
                "leakage.private_allowlist",
                "Private row fields differ from the exact private allowlist.",
                record_id=finding_id,
                details={
                    "extra_fields": sorted(set(row) - _PRIVATE_GOLD_FIELDS),
                    "missing_fields": sorted(_PRIVATE_GOLD_FIELDS - set(row)),
                },
            )
        logical_id = row.get("logical_record_id")
        alignment_violations = []
        if not _nonblank_string(logical_id):
            alignment_violations.append("logical_record_id")
        elif logical_id in seen_private_ids:
            alignment_violations.append("duplicate_logical_record_id")
        else:
            seen_private_ids.add(logical_id)
        public_row = public[index] if index < len(public) else None
        if type(public_row) is not dict:
            alignment_violations.append("missing_public_row_at_index")
        else:
            for field in ("logical_record_id", "core_id", "record_type"):
                if row.get(field) != public_row.get(field):
                    alignment_violations.append(field)
        if alignment_violations:
            _hard(
                findings,
                "leakage.private_allowlist",
                "Private row is not uniquely aligned to its corresponding public row.",
                record_id=finding_id,
                details={"violations": sorted(set(alignment_violations))},
            )
    if len(gold) != len(public):
        _hard(
            findings,
            "leakage.private_allowlist",
            "Public and private allowlisted row collections are not one-to-one aligned.",
            details={"private_rows": len(gold), "public_rows": len(public)},
        )

    runtime_surface_canaries = []
    runtime_record_canaries = []
    runtime_request_canaries = []
    actual_runtime_canaries = []
    for index, row in enumerate(runtime):
        finding_id = _record_id(row, index, "runtime")
        if type(row) is not dict:
            _hard(
                findings,
                "leakage.input_error",
                "Runtime row is not an exact JSON object.",
                record_id=finding_id,
            )
            continue

        private_paths = sorted(set(_private_paths(row)))
        if private_paths:
            _hard(
                findings,
                "leakage.private_field_in_public",
                "Private-only field names appear in a model-facing runtime row.",
                record_id=finding_id,
                details={"surface": "runtime", "paths": private_paths},
            )
        gold_marked_paths = sorted(set(_gold_marked_paths(row)))
        if gold_marked_paths:
            _hard(
                findings,
                "leakage.private_field_in_public",
                "Gold-marked field names appear in a model-facing runtime row.",
                record_id=finding_id,
                details={"surface": "runtime", "paths": gold_marked_paths},
            )

        surface_canary = row.get("source_surface_canary")
        record_canary = row.get("source_record_canary")
        request_canary = row.get("source_request_canary")
        if not all(
            _nonblank_string(value)
            for value in (surface_canary, record_canary, request_canary)
        ):
            _canary_finding(
                findings,
                "Runtime row is missing a nonblank source canary.",
                record_id=finding_id,
            )
        if _nonblank_string(surface_canary):
            runtime_surface_canaries.append(surface_canary)
        if _nonblank_string(record_canary):
            runtime_record_canaries.append(record_canary)
        if _nonblank_string(request_canary):
            runtime_request_canaries.append(request_canary)
        actual_runtime_canaries.append(
            (surface_canary, record_canary, request_canary)
        )

        logical_id = row.get("source_logical_record_id")
        source_request_id = row.get("source_request_id")
        public_row = public_by_id.get(logical_id)
        public_request = request_by_id.get(source_request_id)
        template = row.get("request_template")
        template_canary = template.get("canary") if type(template) is dict else None
        template_state = (
            template.get("structured_state") if type(template) is dict else None
        )
        template_surface = (
            template_state.get("surface_reference")
            if type(template_state) is dict
            else None
        )
        template_options = template.get("options") if type(template) is dict else None
        template_labels_match = (
            type(template_options) is list
            and bool(template_options)
            and _nonblank_string(surface_canary)
            and all(
                type(option) is dict
                and _nonblank_string(option.get("label"))
                and surface_canary in option["label"]
                for option in template_options
            )
        )
        if (
            public_row is None
            or public_row.get("surface_canary") != surface_canary
            or public_row.get("record_canary") != record_canary
            or public_request is None
            or public_request.get("canary") != request_canary
            or template_canary != request_canary
            or template_surface != surface_canary
            or not template_labels_match
        ):
            _canary_finding(
                findings,
                (
                    "Runtime source and nested-template canaries do not "
                    "exactly mirror the public request."
                ),
                record_id=finding_id,
            )

    if len(runtime) != 800 or actual_runtime_canaries != expected_runtime_canaries:
        _canary_finding(
            findings,
            "Runtime canaries must exactly preserve flattened public request order and values.",
            details={
                "runtime_rows": len(runtime),
                "expected_rows": len(expected_runtime_canaries),
            },
        )
    runtime_surface_counts = Counter(runtime_surface_canaries)
    if (
        len(runtime_surface_canaries) != 800
        or len(runtime_surface_counts) != 40
        or set(runtime_surface_counts.values()) != {20}
    ):
        _canary_finding(
            findings,
            "Runtime surface canaries must contain forty strata with twenty requests each.",
            details={
                "runtime_surface_canaries": len(runtime_surface_canaries),
                "unique_surface_canaries": len(runtime_surface_counts),
            },
        )
    runtime_record_counts = Counter(runtime_record_canaries)
    if (
        len(runtime_record_canaries) != 800
        or runtime_record_counts != expected_record_multiplicity
        or Counter(runtime_record_counts.values()) != Counter({1: 480, 2: 160})
    ):
        _canary_finding(
            findings,
            (
                "Runtime record-canary multiplicity must be 480 direct rows "
                "and 160 two-child packet rows."
            ),
            details={
                "runtime_record_canaries": len(runtime_record_canaries),
                "unique_record_canaries": len(runtime_record_counts),
                "multiplicity": dict(
                    sorted(Counter(runtime_record_counts.values()).items())
                ),
            },
        )
    if len(runtime_request_canaries) != 800 or len(set(runtime_request_canaries)) != 800:
        _canary_finding(
            findings,
            "Runtime request canaries must be globally unique across all 800 requests.",
            details={
                "runtime_request_canaries": len(runtime_request_canaries),
                "unique_request_canaries": len(set(runtime_request_canaries)),
            },
        )

    return _sorted_findings(findings)


def audit_leakage(public, gold, runtime):
    """Return deterministic hard findings for leakage or canary drift."""

    try:
        return _audit_leakage(public, gold, runtime)
    except MemoryError:
        raise
    except Exception as exc:
        return [
            make_finding(
                audit="leakage",
                code="leakage.input_error",
                severity="hard",
                message="Leakage audit failed closed: %s" % exc,
                details={"exception_type": type(exc).__name__},
            )
        ]


def _validate_report_manifest(value):
    if type(value) is not dict:
        raise ValueError("manifest root is not an exact JSON object")
    hashes = value.get("artifact_hashes")
    generator = value.get("generator")
    if (
        type(hashes) is not dict
        or any(
            not _nonblank_string(hashes.get(field))
            for field in (
                "logical_bank_sha256",
                "private_gold_sha256",
                "runtime_manifest_sha256",
            )
        )
        or type(generator) is not dict
        or not _nonblank_string(generator.get("version"))
    ):
        raise ValueError("manifest lacks required audit-report evidence")
    return value


def _report_manifest(manifest):
    if type(manifest) is dict:
        return manifest
    return {
        "artifact_hashes": {
            "logical_bank_sha256": "NOT_AVAILABLE",
            "private_gold_sha256": "NOT_AVAILABLE",
            "runtime_manifest_sha256": "NOT_AVAILABLE",
        },
        "generator": {"version": "NOT_AVAILABLE"},
    }


def main(argv=None):
    parser = add_common_cli_arguments(argparse.ArgumentParser(description=__doc__))
    args = parser.parse_args(argv)

    checked_records = 0
    checked_requests = 0
    manifest = None
    report_evidence = None
    try:
        inputs = load_audit_inputs(
            args.bank, args.gold, args.runtime, args.manifest
        )
        manifest = _validate_report_manifest(inputs.manifest)
        report_evidence = inputs.evidence
        checked_records = len(inputs.public)
        checked_requests = len(inputs.runtime)
        findings = audit_leakage(inputs.public, inputs.gold, inputs.runtime)
        if inputs.hash_mismatches:
            _hard(
                findings,
                "leakage.artifact_hash_mismatch",
                "Audited artifact bytes do not match their manifest hashes.",
                details={"artifacts": list(inputs.hash_mismatches)},
            )
            findings = _sorted_findings(findings)
    except MemoryError:
        raise
    except Exception as exc:
        findings = [
            make_finding(
                audit="leakage",
                code="leakage.input_error",
                severity="hard",
                message="Leakage audit input failed closed: %s" % exc,
                details={"exception_type": type(exc).__name__},
            )
        ]

    write_reports(
        findings,
        audit_slug="leakage-audit",
        audit_title="SKIM P1 leakage audit",
        checked_records=checked_records,
        checked_requests=checked_requests,
        manifest=_report_manifest(manifest),
        output_dir=args.output_dir,
        report_date=args.report_date,
        artifact_evidence=report_evidence,
    )
    return report_exit_code(findings)


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["audit_leakage", "main"]
