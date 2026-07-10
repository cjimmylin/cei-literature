#!/usr/bin/env python3
"""Credential-free rho-sibling matched-surface audit for ZEROSUM P1."""

from __future__ import annotations

import argparse
from collections import defaultdict
from collections.abc import Mapping, Sequence
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any, Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audits.schema_audit import (  # noqa: E402
    DEFAULT_BANK,
    DEFAULT_MANIFEST,
    load_jsonl,
    make_finding,
    report_exit_code,
    write_reports,
)
from harness.model_adapters import build_requests_for_record  # noqa: E402


NUMBER_RE = re.compile(
    r"(?<![A-Za-z0-9_])[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?![A-Za-z0-9_])"
)
INVARIANT_FIELDS = (
    "core_id",
    "design",
    "clause",
    "dose_tier",
    "domain",
    "beneficiary",
    "salience",
    "secular_anchor",
    "panel_kappa",
    "difficulty_est",
    "frame",
    "opacity_tier",
    "stakes",
    "sf_cell",
    "surface_canary",
    "monitoring_condition",
    "agentic_action",
    "escalation",
)


def normalize_surface(text: str) -> str:
    """Mask signed integers/decimals and normalize whitespace per preregistration."""
    if not isinstance(text, str):
        raise TypeError("model_prompt must be a string")
    return " ".join(NUMBER_RE.sub("<NUM>", text).split())


def audit_matched_surface(
    bank: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
) -> List[Dict[str, Any]]:
    """Pure validation of the four-rho matched wording and sibling invariants."""
    if not isinstance(bank, Sequence) or isinstance(bank, (str, bytes)):
        return [make_finding(
            audit="matched_surface",
            code="matched_surface.bank_not_sequence",
            severity="hard",
            message="Public bank must be a sequence of objects.",
        )]
    if not isinstance(manifest, Mapping):
        return [make_finding(
            audit="matched_surface",
            code="matched_surface.manifest_not_object",
            severity="hard",
            message="Manifest must be an object.",
        )]
    rho_grid = manifest.get("rho_grid")
    if not isinstance(rho_grid, list) or not rho_grid:
        return [make_finding(
            audit="matched_surface",
            code="matched_surface.manifest_rho_grid",
            severity="hard",
            message="Manifest rho_grid must be a nonempty list.",
        )]

    findings: List[Dict[str, Any]] = []
    by_core: Dict[Any, List[Mapping[str, Any]]] = defaultdict(list)
    for index, record in enumerate(bank):
        if not isinstance(record, Mapping):
            findings.append(make_finding(
                audit="matched_surface",
                code="matched_surface.public_not_object",
                severity="hard",
                message="Public record is not an object.",
                record_id="index:%d" % index,
            ))
            continue
        if record.get("record_type") == "advice_primary":
            by_core[record.get("core_id")].append(record)

    if not by_core:
        findings.append(make_finding(
            audit="matched_surface",
            code="matched_surface.no_primaries",
            severity="hard",
            message="No advice_primary records were available for comparison.",
        ))
        return findings

    for core_id, siblings in sorted(by_core.items(), key=lambda pair: str(pair[0])):
        finding_id = str(core_id) if core_id is not None else "missing-core-id"
        actual_rhos = [record.get("rho") for record in siblings]
        if len(siblings) != len(rho_grid) or any(
            sum(value == registered for value in actual_rhos) != 1
            for registered in rho_grid
        ):
            findings.append(make_finding(
                audit="matched_surface",
                code="matched_surface.rho_sibling_set",
                severity="hard",
                message="Core does not contain exactly one primary at each registered rho.",
                record_id=finding_id,
                details={"actual_rhos": actual_rhos, "expected_rhos": list(rho_grid)},
            ))

        normalized_by_id: Dict[str, str] = {}
        trajectory_by_id: Dict[str, tuple] = {}
        for index, record in enumerate(siblings):
            record_id = record.get("id")
            key = record_id if isinstance(record_id, str) else "%s:index:%d" % (finding_id, index)
            prompt = record.get("model_prompt")
            if not isinstance(prompt, str) or not prompt.strip():
                findings.append(make_finding(
                    audit="matched_surface",
                    code="matched_surface.missing_model_prompt",
                    severity="hard",
                    message="Primary lacks a nonempty model_prompt.",
                    record_id=key,
                ))
                continue
            normalized_by_id[key] = normalize_surface(prompt)
            try:
                requests = build_requests_for_record(record)
                trajectory = tuple(
                    request["messages"][-1]["content"] for request in requests
                )
            except (KeyError, TypeError, ValueError) as exc:
                findings.append(make_finding(
                    audit="matched_surface",
                    code="matched_surface.invalid_trajectory",
                    severity="hard",
                    message="Primary trajectory could not be reconstructed: %s" % exc,
                    record_id=key,
                ))
                continue
            if len(trajectory) != 4:
                findings.append(make_finding(
                    audit="matched_surface",
                    code="matched_surface.invalid_trajectory",
                    severity="hard",
                    message="Primary trajectory must contain exactly four requests.",
                    record_id=key,
                ))
                continue
            trajectory_by_id[key] = tuple(
                normalize_surface(surface) for surface in trajectory
            )
            if prompt != trajectory[-1]:
                findings.append(make_finding(
                    audit="matched_surface",
                    code="matched_surface.stored_prompt_mismatch",
                    severity="hard",
                    message="Stored model_prompt differs from the final rendered trajectory request.",
                    record_id=key,
                ))
        if normalized_by_id and len(set(normalized_by_id.values())) != 1:
            findings.append(make_finding(
                audit="matched_surface",
                code="matched_surface.nonnumeric_mismatch",
                severity="hard",
                message="rho siblings differ after all registered numeric values are masked.",
                record_id=finding_id,
                details={
                    "normalized_sha256_by_id": {
                        record_id: hashlib.sha256(surface.encode("utf-8")).hexdigest()
                        for record_id, surface in sorted(normalized_by_id.items())
                    }
                },
            ))
        if trajectory_by_id and len(set(trajectory_by_id.values())) != 1:
            findings.append(make_finding(
                audit="matched_surface",
                code="matched_surface.trajectory_nonnumeric_mismatch",
                severity="hard",
                message="rho siblings' rendered trajectory requests differ after numeric masking.",
                record_id=finding_id,
                details={
                    "trajectory_sha256_by_id": {
                        record_id: hashlib.sha256(
                            json.dumps(
                                trajectory,
                                ensure_ascii=False,
                                separators=(",", ":"),
                            ).encode("utf-8")
                        ).hexdigest()
                        for record_id, trajectory in sorted(trajectory_by_id.items())
                    }
                },
            ))

        anchor = siblings[0]
        changed_fields = sorted(
            field
            for field in INVARIANT_FIELDS
            if any(record.get(field) != anchor.get(field) for record in siblings[1:])
        )
        if changed_fields:
            findings.append(make_finding(
                audit="matched_surface",
                code="matched_surface.invariant_metadata",
                severity="hard",
                message="rho siblings differ on preregistered non-rho metadata.",
                record_id=finding_id,
                details={"fields": changed_fields},
            ))
    return sorted(
        findings,
        key=lambda finding: (
            finding["code"], finding.get("record_id", ""), finding["message"]
        ),
    )


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bank", type=Path, default=DEFAULT_BANK)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "reports")
    parser.add_argument("--report-date", default=None)
    args = parser.parse_args(argv)
    checked_records = 0
    try:
        bank = load_jsonl(args.bank)
        checked_records = len(bank)
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        findings = audit_matched_surface(bank, manifest)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        findings = [make_finding(
            audit="matched_surface",
            code="matched_surface.input_error",
            severity="hard",
            message=str(exc),
        )]
    write_reports(
        findings,
        audit_slug="matched-surface-audit",
        audit_title="ZEROSUM P1 matched-surface audit",
        checked_records=checked_records,
        output_dir=args.output_dir,
        report_date=args.report_date,
    )
    return report_exit_code(findings)


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["audit_matched_surface", "main", "normalize_surface"]
