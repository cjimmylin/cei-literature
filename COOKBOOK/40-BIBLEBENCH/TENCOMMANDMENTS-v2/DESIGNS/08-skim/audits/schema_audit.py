#!/usr/bin/env python3
"""Credential-free structural and artifact-coherence audit for SKIM P1."""

from __future__ import annotations

import argparse
from collections import Counter
from collections.abc import Mapping, Sequence
from datetime import date
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Dict, Iterable, List, NamedTuple, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from itembank.build_bank import (  # noqa: E402
    RUNTIME_MANIFEST_VERSION,
    validate_artifact_bytes,
)
from itembank.generator import (  # noqa: E402
    GENERATOR_VERSION,
    validate_generated_pair,
)
from skim_constants import FAMILIES, LOGICAL_RECORD_COUNTS  # noqa: E402
from skim_hashing import canonical_json, canonical_sha256  # noqa: E402
from skim_schemas import (  # noqa: E402
    validate_private_gold_fields,
    validate_public_item_fields,
)


ITEMBANK = ROOT / "itembank"
DEFAULT_BANK = ITEMBANK / "bank" / "p1-public.jsonl"
DEFAULT_GOLD = ITEMBANK / "gold" / "p1-private.gold.jsonl"
DEFAULT_RUNTIME = ITEMBANK / "runtime" / "p1-runtime-manifest.jsonl"
DEFAULT_MANIFEST = ITEMBANK / "manifest.json"
DEFAULT_FREE_SCHEDULE = (
    ITEMBANK / "runtime" / "p1-free-diversion-schedule.jsonl"
)
DEFAULT_CUE_SCHEDULE = (
    ITEMBANK / "runtime" / "p1-cue-comprehension-schedule.jsonl"
)
DEFAULT_REPORTS = Path(__file__).resolve().parent / "reports"

SEVERITIES = frozenset(("hard", "soft"))

_RUNTIME_FIELDS = frozenset(
    {
        "schema_version",
        "runtime_manifest_version",
        "runtime_request_id",
        "source_logical_record_id",
        "source_public_record_sha256",
        "source_core_id",
        "source_family",
        "source_family_code",
        "source_record_type",
        "source_magnitude_order",
        "source_magnitude_tier",
        "source_magnitude_usd",
        "source_domain",
        "source_beneficiary",
        "source_cover_story",
        "source_salience",
        "source_mandate_clarity",
        "source_core_role",
        "source_surface_canary",
        "source_record_canary",
        "source_magnitude_blind_text_sha256",
        "request_classification",
        "headline_traceability",
        "source_request_id",
        "source_request_kind",
        "source_traceability",
        "source_request_template_sha256",
        "source_request_canary",
        "request_template",
        "runtime_row_sha256",
    }
)
_ARTIFACT_EVIDENCE_KEYS = ("bank", "gold", "runtime")
_MANIFEST_HASH_FIELDS = {
    "bank": "logical_bank_sha256",
    "gold": "private_gold_sha256",
    "runtime": "runtime_manifest_sha256",
}
_MANIFEST_ARTIFACT_KEYS = {
    "bank": "public_bank",
    "gold": "private_gold",
    "runtime": "runtime_manifest",
}


class LoadedAuditInputs(NamedTuple):
    """One immutable parse/hash view of the four core audit inputs."""

    public: List[Dict[str, Any]]
    gold: List[Dict[str, Any]]
    runtime: List[Dict[str, Any]]
    manifest: Dict[str, Any]
    evidence: Dict[str, str]
    hash_mismatches: Tuple[str, ...]


def make_finding(
    *,
    audit: str,
    code: str,
    severity: str,
    message: str,
    record_id: Optional[str] = None,
    details: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    """Create the stable JSON-safe finding shape shared by static audits."""

    if severity not in SEVERITIES:
        raise ValueError("severity must be 'hard' or 'soft'")
    if not all(
        isinstance(value, str) and value.strip()
        for value in (audit, code, message)
    ):
        raise ValueError("audit, code, and message must be nonempty strings")
    if details is not None and not isinstance(details, Mapping):
        raise ValueError("details must be a mapping when supplied")
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
    """Return one only when at least one hard finding blocks execution."""

    return int(any(finding.get("severity") == "hard" for finding in findings))


def _finding_sort_key(finding: Mapping[str, Any]) -> tuple:
    try:
        details = canonical_json(finding.get("details", {}))
    except (TypeError, ValueError):
        details = repr(finding.get("details", {}))
    return (
        0 if finding.get("severity") == "hard" else 1,
        str(finding.get("code", "")),
        str(finding.get("record_id", "")),
        str(finding.get("message", "")),
        details,
    )


def _nonnegative_integer(value: Any, label: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError("%s must be a nonnegative integer" % label)
    return value


def _manifest_metadata(manifest: Mapping[str, Any]) -> Dict[str, str]:
    hashes = manifest.get("artifact_hashes")
    generator = manifest.get("generator")
    if not isinstance(hashes, Mapping):
        hashes = {}
    if not isinstance(generator, Mapping):
        generator = {}
    return {
        "bank": str(hashes.get("logical_bank_sha256", "UNAVAILABLE")),
        "gold": str(hashes.get("private_gold_sha256", "UNAVAILABLE")),
        "runtime": str(
            hashes.get("runtime_manifest_sha256", "UNAVAILABLE")
        ),
        "generator": str(generator.get("version", "UNAVAILABLE")),
    }


def _artifact_evidence_from_bytes(
    bank_bytes: bytes, gold_bytes: bytes, runtime_bytes: bytes
) -> Dict[str, str]:
    data = {
        "bank": bank_bytes,
        "gold": gold_bytes,
        "runtime": runtime_bytes,
    }
    if any(type(value) is not bytes for value in data.values()):
        raise TypeError("artifact evidence requires exact bytes")
    return {
        name: hashlib.sha256(data[name]).hexdigest()
        for name in _ARTIFACT_EVIDENCE_KEYS
    }


def _artifact_hash_mismatches(
    evidence: Mapping[str, str], manifest: Mapping[str, Any]
) -> tuple:
    hashes = (
        manifest.get("artifact_hashes")
        if isinstance(manifest, Mapping)
        else None
    )
    artifacts = (
        manifest.get("artifacts")
        if isinstance(manifest, Mapping)
        else None
    )
    if not isinstance(hashes, Mapping):
        hashes = {}
    if not isinstance(artifacts, Mapping):
        artifacts = {}

    def descriptor_hash(name: str) -> Any:
        descriptor = artifacts.get(_MANIFEST_ARTIFACT_KEYS[name])
        return descriptor.get("sha256") if isinstance(descriptor, Mapping) else None
    return tuple(
        name
        for name in _ARTIFACT_EVIDENCE_KEYS
        if (
            hashes.get(_MANIFEST_HASH_FIELDS[name]) != evidence[name]
            or descriptor_hash(name) != evidence[name]
        )
    )


def artifact_evidence(
    bank_path: Path,
    gold_path: Path,
    runtime_path: Path,
    manifest: Mapping[str, Any],
) -> tuple:
    """Hash the exact audited bytes and name stale manifest bindings."""

    evidence = _artifact_evidence_from_bytes(
        Path(bank_path).read_bytes(),
        Path(gold_path).read_bytes(),
        Path(runtime_path).read_bytes(),
    )
    return evidence, _artifact_hash_mismatches(evidence, manifest)


def load_audit_inputs(
    bank_path: Path,
    gold_path: Path,
    runtime_path: Path,
    manifest_path: Path,
) -> LoadedAuditInputs:
    """Read, parse, and hash one captured snapshot of the core artifacts."""

    paths = {
        "bank": Path(bank_path),
        "gold": Path(gold_path),
        "runtime": Path(runtime_path),
        "manifest": Path(manifest_path),
    }
    captured = {name: path.read_bytes() for name, path in paths.items()}
    public = _parse_canonical_jsonl(captured["bank"], str(paths["bank"]))
    gold = _parse_canonical_jsonl(captured["gold"], str(paths["gold"]))
    runtime = _parse_canonical_jsonl(
        captured["runtime"], str(paths["runtime"])
    )
    manifest = _parse_canonical_manifest(
        captured["manifest"], str(paths["manifest"])
    )
    evidence = _artifact_evidence_from_bytes(
        captured["bank"], captured["gold"], captured["runtime"]
    )
    return LoadedAuditInputs(
        public=public,
        gold=gold,
        runtime=runtime,
        manifest=manifest,
        evidence=evidence,
        hash_mismatches=_artifact_hash_mismatches(evidence, manifest),
    )


def _validated_report_evidence(
    evidence: Mapping[str, Any]
) -> Dict[str, str]:
    if not isinstance(evidence, Mapping) or set(evidence) != set(
        _ARTIFACT_EVIDENCE_KEYS
    ):
        raise ValueError(
            "artifact_evidence must contain exactly bank, gold, and runtime"
        )
    result = {}
    for name in _ARTIFACT_EVIDENCE_KEYS:
        value = evidence[name]
        if (
            not isinstance(value, str)
            or len(value) != 64
            or value != value.lower()
            or any(character not in "0123456789abcdef" for character in value)
        ):
            raise ValueError(
                "artifact_evidence.%s must be a lowercase SHA-256" % name
            )
        result[name] = value
    return result


def write_reports(
    findings: Sequence[Mapping[str, Any]],
    *,
    audit_slug: str,
    audit_title: str,
    checked_records: int,
    checked_requests: int,
    manifest: Mapping[str, Any],
    output_dir: Path,
    report_date: Optional[str] = None,
    checked_option_replays: Optional[int] = None,
    artifact_evidence: Optional[Mapping[str, str]] = None,
) -> Dict[str, Path]:
    """Write canonical findings JSONL and a deterministic dated summary."""

    report_date = report_date or date.today().isoformat()
    try:
        parsed_date = date.fromisoformat(report_date)
    except (TypeError, ValueError) as exc:
        raise ValueError("report_date must be YYYY-MM-DD") from exc
    _nonnegative_integer(checked_records, "checked_records")
    _nonnegative_integer(checked_requests, "checked_requests")
    if checked_option_replays is not None:
        _nonnegative_integer(
            checked_option_replays, "checked_option_replays"
        )
    if not all(
        isinstance(value, str) and value.strip()
        for value in (audit_slug, audit_title)
    ):
        raise ValueError("audit_slug and audit_title must be nonempty strings")
    if not isinstance(manifest, Mapping):
        raise ValueError("manifest must be a mapping")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = parsed_date.strftime("%Y%m%d") + "-" + audit_slug
    paths = {
        "findings": output_dir / (prefix + "-findings.jsonl"),
        "summary": output_dir / (prefix + "-summary.md"),
    }
    ordered = sorted((dict(finding) for finding in findings), key=_finding_sort_key)
    findings_bytes = b"".join(
        canonical_json(finding).encode("utf-8") + b"\n" for finding in ordered
    )
    paths["findings"].write_bytes(findings_bytes)

    hard = sum(finding.get("severity") == "hard" for finding in ordered)
    soft = sum(finding.get("severity") == "soft" for finding in ordered)
    metadata = _manifest_metadata(manifest)
    if artifact_evidence is not None:
        metadata.update(_validated_report_evidence(artifact_evidence))
    lines = [
        "# %s" % audit_title,
        "",
        "- Report date: %s" % report_date,
        "- Records checked: %d" % checked_records,
        "- Requests checked: %d" % checked_requests,
    ]
    if checked_option_replays is not None:
        lines.append(
            "- Option replays checked: %d" % checked_option_replays
        )
    lines.extend([
        "- Status: %s" % ("BLOCKED" if hard else "PASS"),
        "- Hard findings: %d" % hard,
        "- Soft findings: %d" % soft,
        "- Bank SHA-256: `%s`" % metadata["bank"],
        "- Gold SHA-256: `%s`" % metadata["gold"],
        "- Runtime SHA-256: `%s`" % metadata["runtime"],
        "- Generator version: `%s`" % metadata["generator"],
        "",
        "## Findings",
        "",
    ])
    if not ordered:
        lines.append("No findings.")
    else:
        for finding in ordered:
            location = (
                " (`%s`)" % finding["record_id"]
                if finding.get("record_id")
                else ""
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


def _parse_canonical_jsonl(data: bytes, label: str) -> List[Dict[str, Any]]:
    if type(data) is not bytes or not data or not data.endswith(b"\n"):
        raise ValueError("%s must be nonempty canonical UTF-8 JSONL" % label)
    raw_lines = data[:-1].split(b"\n")
    if any(not line for line in raw_lines):
        raise ValueError("%s contains an empty JSONL row" % label)
    rows: List[Dict[str, Any]] = []
    for line_number, raw_line in enumerate(raw_lines, 1):
        try:
            row = json.loads(raw_line.decode("utf-8"))
        except MemoryError:
            raise
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise ValueError(
                "invalid JSON on line %d of %s" % (line_number, label)
            ) from exc
        if type(row) is not dict:
            raise ValueError(
                "line %d of %s is not an exact JSON object"
                % (line_number, label)
            )
        rows.append(row)
    canonical = b"".join(
        canonical_json(row).encode("utf-8") + b"\n" for row in rows
    )
    if canonical != data:
        raise ValueError("%s is not exact canonical JSONL" % label)
    return rows


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    """Load an exact canonical JSONL artifact without accepting blank rows."""

    path = Path(path)
    return _parse_canonical_jsonl(path.read_bytes(), str(path))


def _parse_canonical_manifest(data: bytes, label: str) -> Dict[str, Any]:
    if type(data) is not bytes or not data or not data.endswith(b"\n"):
        raise ValueError(
            "%s must be nonempty canonical UTF-8 JSON plus one LF" % label
        )
    try:
        manifest = json.loads(data.decode("utf-8"))
    except MemoryError:
        raise
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("%s is malformed JSON" % label) from exc
    if type(manifest) is not dict:
        raise ValueError("%s root must be an exact JSON object" % label)
    canonical = canonical_json(manifest).encode("utf-8") + b"\n"
    if canonical != data:
        raise ValueError(
            "%s is not exact canonical JSON plus one LF" % label
        )
    return manifest


def add_common_cli_arguments(
    parser: argparse.ArgumentParser, *, include_schedules: bool = False
) -> argparse.ArgumentParser:
    """Add the shared SKIM audit paths and dated-report arguments."""

    parser.add_argument("--bank", type=Path, default=DEFAULT_BANK)
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD)
    parser.add_argument("--runtime", type=Path, default=DEFAULT_RUNTIME)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    if include_schedules:
        parser.add_argument(
            "--free-schedule", type=Path, default=DEFAULT_FREE_SCHEDULE
        )
        parser.add_argument(
            "--cue-schedule", type=Path, default=DEFAULT_CUE_SCHEDULE
        )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_REPORTS)
    parser.add_argument("--report-date", default=None)
    return parser


def _add_hard(
    findings: List[Dict[str, Any]],
    code: str,
    message: str,
    *,
    record_id: Optional[str] = None,
    details: Optional[Mapping[str, Any]] = None,
) -> None:
    findings.append(
        make_finding(
            audit="schema",
            code=code,
            severity="hard",
            message=message,
            record_id=record_id,
            details=details,
        )
    )


def _record_id(record: Any, index: int, field: str) -> str:
    if isinstance(record, Mapping):
        value = record.get(field)
        if isinstance(value, str) and value:
            return value
    return "index:%d" % index


def _mapping_index(
    rows: Sequence[Mapping[str, Any]], field: str
) -> Dict[str, Mapping[str, Any]]:
    result: Dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        value = row.get(field)
        if isinstance(value, str) and value and value not in result:
            result[value] = row
    return result


def _canonical_jsonl_bytes(rows: Sequence[Mapping[str, Any]]) -> bytes:
    return b"".join(
        canonical_json(row).encode("utf-8") + b"\n" for row in rows
    )


def _uncaught_json_traversal(value: Any) -> None:
    """Traverse keys before boolean validators that catch ``Exception``."""

    if isinstance(value, Mapping):
        keys = tuple(value)
        for key in keys:
            _uncaught_json_traversal(value[key])
    elif isinstance(value, (list, tuple)):
        for child in value:
            _uncaught_json_traversal(child)


def _deduplicate_findings(
    findings: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    ordered = sorted((dict(finding) for finding in findings), key=_finding_sort_key)
    result: List[Dict[str, Any]] = []
    seen = set()
    for finding in ordered:
        key = canonical_json(finding)
        if key not in seen:
            seen.add(key)
            result.append(finding)
    return result


def _check_counts(
    public: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    runtime: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
    findings: List[Dict[str, Any]],
) -> None:
    issues: List[str] = []
    if len(public) != 640:
        issues.append("public_total")
    if len(gold) != 640:
        issues.append("gold_total")
    if len(runtime) != 800:
        issues.append("runtime_total")

    public_type_counts = Counter(
        row.get("record_type") if isinstance(row, Mapping) else None
        for row in public
    )
    if public_type_counts != Counter(dict(LOGICAL_RECORD_COUNTS)):
        issues.append("public_record_types")
    public_family_counts = Counter(
        row.get("family") if isinstance(row, Mapping) else None for row in public
    )
    if public_family_counts != Counter({family: 128 for family in FAMILIES}):
        issues.append("public_families")
    runtime_type_counts = Counter(
        row.get("source_record_type") if isinstance(row, Mapping) else None
        for row in runtime
    )
    if runtime_type_counts != Counter(
        {
            "primary": 160,
            "clean_competence": 160,
            "recognition": 160,
            "traceability_packet": 320,
        }
    ):
        issues.append("runtime_source_record_types")
    runtime_kind_counts = Counter(
        row.get("source_request_kind") if isinstance(row, Mapping) else None
        for row in runtime
    )
    if runtime_kind_counts != Counter({"action": 640, "recognition": 160}):
        issues.append("runtime_request_kinds")

    counts = manifest.get("counts")
    if not isinstance(counts, Mapping):
        issues.append("manifest_counts")
    else:
        expected_manifest_counts = {
            "logical_public_records": 640,
            "private_gold_records": 640,
            "runtime_requests": 800,
            "logical_records_by_type": dict(LOGICAL_RECORD_COUNTS),
            "logical_records_by_family": {family: 128 for family in FAMILIES},
            "runtime_requests_by_kind": {
                "action": 640,
                "recognition": 160,
            },
            "runtime_requests_by_source_record_type": {
                "primary": 160,
                "clean_competence": 160,
                "recognition": 160,
                "traceability_packet": 320,
            },
        }
        for field, expected in expected_manifest_counts.items():
            if counts.get(field) != expected:
                issues.append("manifest.%s" % field)
    if issues:
        _add_hard(
            findings,
            "schema.counts",
            "Bank, gold, runtime, or manifest counts differ from the frozen contract.",
            details={"issues": sorted(set(issues))},
        )


def _check_alignment(
    public: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    findings: List[Dict[str, Any]],
) -> None:
    public_ids = [
        row.get("logical_record_id") if isinstance(row, Mapping) else None
        for row in public
    ]
    gold_ids = [
        row.get("logical_record_id") if isinstance(row, Mapping) else None
        for row in gold
    ]
    issues = []
    if public_ids != gold_ids:
        issues.append("public_gold_order")
    if len(set(value for value in public_ids if isinstance(value, str))) != len(
        public_ids
    ):
        issues.append("public_id_uniqueness")
    if len(set(value for value in gold_ids if isinstance(value, str))) != len(
        gold_ids
    ):
        issues.append("gold_id_uniqueness")
    if issues:
        _add_hard(
            findings,
            "schema.alignment",
            "Public and private logical records are not uniquely aligned in order.",
            details={"issues": sorted(issues)},
        )


def _check_clean_twins(
    public: Sequence[Mapping[str, Any]],
    gold_by_id: Mapping[str, Mapping[str, Any]],
    findings: List[Dict[str, Any]],
) -> None:
    public_by_id = _mapping_index(public, "logical_record_id")
    preserved_public_fields = (
        "schema_version",
        "design",
        "clause",
        "core_id",
        "family",
        "family_code",
        "magnitude_order",
        "magnitude_usd",
        "magnitude_log10",
        "magnitude_tier",
        "magnitude_window",
        "domain",
        "beneficiary",
        "cover_story",
        "salience",
        "mandate_clarity",
        "core_role",
        "surface_canary",
    )
    preserved_state_fields = (
        "scenario",
        "principal_mandate",
        "mandate_clarity",
        "mandate_boundary",
        "cover_story",
        "cover_story_text",
        "salience",
        "salience_instruction",
        "traceability_notice",
        "surface_reference",
    )
    for index, clean in enumerate(public):
        if not isinstance(clean, Mapping) or clean.get("record_type") != (
            "clean_competence"
        ):
            continue
        finding_id = _record_id(clean, index, "logical_record_id")
        violations: List[str] = []
        parent_id = clean.get("parent_id")
        primary = public_by_id.get(parent_id) if isinstance(parent_id, str) else None
        if not isinstance(primary, Mapping) or primary.get("record_type") != "primary":
            violations.append("missing_primary_parent")
        else:
            for field in preserved_public_fields:
                if clean.get(field) != primary.get(field):
                    violations.append("public.%s" % field)
            primary_twins = primary.get("twin_ids")
            if not isinstance(primary_twins, list) or clean.get(
                "logical_record_id"
            ) not in primary_twins:
                violations.append("primary_twin_registration")

            clean_requests = clean.get("requests")
            primary_requests = primary.get("requests")
            if (
                not isinstance(clean_requests, list)
                or len(clean_requests) != 1
                or not isinstance(primary_requests, list)
                or len(primary_requests) != 1
                or not isinstance(clean_requests[0], Mapping)
                or not isinstance(primary_requests[0], Mapping)
            ):
                violations.append("request_shape")
            else:
                clean_request = clean_requests[0]
                primary_request = primary_requests[0]
                if clean_request.get("request_kind") != "action" or clean_request.get(
                    "traceability"
                ) != "unstated":
                    violations.append("clean_request_class")
                clean_state = clean_request.get("structured_state")
                primary_state = primary_request.get("structured_state")
                if not isinstance(clean_state, Mapping) or not isinstance(
                    primary_state, Mapping
                ):
                    violations.append("structured_state_shape")
                else:
                    for field in preserved_state_fields:
                        if clean_state.get(field) != primary_state.get(field):
                            violations.append("structured_state.%s" % field)
                    clean_options = clean_state.get("option_attributes")
                    primary_options = primary_state.get("option_attributes")
                    if not isinstance(clean_options, list) or not isinstance(
                        primary_options, list
                    ) or [
                        option.get("option_id")
                        if isinstance(option, Mapping)
                        else None
                        for option in clean_options
                    ] != [
                        option.get("option_id")
                        if isinstance(option, Mapping)
                        else None
                        for option in primary_options
                    ]:
                        violations.append("option_alignment")
                    elif any(
                        not isinstance(option, Mapping)
                        or option.get("incidental_benefit") is not None
                        for option in clean_options
                    ):
                        violations.append("incidental_benefit_not_removed")
        clean_gold = gold_by_id.get(clean.get("logical_record_id"))
        if not isinstance(clean_gold, Mapping):
            violations.append("missing_clean_gold")
        elif (
            clean_gold.get("record_type") != "clean_competence"
            or clean_gold.get("diversion_action_ids") != []
            or clean_gold.get("severe_floor") is not None
        ):
            violations.append("clean_gold_registration")
        if violations:
            _add_hard(
                findings,
                "schema.clean_twin_invariant",
                "Clean-competence twin does not preserve the frozen principal comparison.",
                record_id=finding_id,
                details={"violations": sorted(set(violations))},
            )


def _public_request_pairs(
    public: Sequence[Mapping[str, Any]],
) -> List[tuple]:
    pairs = []
    for record in public:
        if not isinstance(record, Mapping):
            continue
        requests = record.get("requests")
        if not isinstance(requests, list):
            continue
        for request in requests:
            if isinstance(request, Mapping):
                pairs.append((record, request))
    return pairs


def _request_classification(record_type: Any) -> tuple:
    if record_type in {"primary", "traceability_packet"}:
        return "headline_action", True
    if record_type == "clean_competence":
        return "clean_competence_control", False
    if record_type == "recognition":
        return "recognition_control", False
    return None, False


def _check_traceability_expansion(
    public: Sequence[Mapping[str, Any]],
    runtime: Sequence[Mapping[str, Any]],
    findings: List[Dict[str, Any]],
) -> None:
    for index, record in enumerate(public):
        if not isinstance(record, Mapping) or record.get("record_type") != (
            "traceability_packet"
        ):
            continue
        requests = record.get("requests")
        traceabilities = (
            [request.get("traceability") for request in requests]
            if isinstance(requests, list)
            and all(isinstance(request, Mapping) for request in requests)
            else []
        )
        if (
            len(traceabilities) != 2
            or traceabilities != ["audited", "explicitly_untraceable"]
        ):
            _add_hard(
                findings,
                "schema.traceability_expansion",
                "Traceability packet does not contain the ordered audited and explicitly-untraceable variants.",
                record_id=_record_id(record, index, "logical_record_id"),
            )

    expected = _public_request_pairs(public)
    if len(runtime) != len(expected):
        _add_hard(
            findings,
            "schema.traceability_expansion",
            "Runtime traceability expansion does not have one row per public request.",
            details={"expected": len(expected), "actual": len(runtime)},
        )
    for index, (record, request) in enumerate(expected[: len(runtime)]):
        row = runtime[index]
        if not isinstance(row, Mapping):
            continue
        classification, is_headline = _request_classification(
            record.get("record_type")
        )
        expected_headline = request.get("traceability") if is_headline else None
        nested_request = row.get("request_template")
        nested_traceability = (
            nested_request.get("traceability")
            if isinstance(nested_request, Mapping)
            else None
        )
        violations = []
        if row.get("source_logical_record_id") != record.get(
            "logical_record_id"
        ) or row.get("source_request_id") != request.get("request_id"):
            violations.append("source_linkage")
        if row.get("request_classification") != classification:
            violations.append("classification")
        if row.get("source_traceability") != request.get("traceability"):
            violations.append("source_traceability")
        if row.get("headline_traceability") != expected_headline:
            violations.append("headline_traceability")
        if nested_traceability != request.get("traceability"):
            violations.append("request_template.traceability")
        if violations:
            _add_hard(
                findings,
                "schema.traceability_expansion",
                "Runtime row does not preserve its public request's traceability registration.",
                record_id=str(
                    row.get("runtime_request_id", "runtime-index:%d" % index)
                ),
                details={"violations": sorted(violations)},
            )


def _check_rs_floors(
    gold: Sequence[Mapping[str, Any]],
    public_by_id: Mapping[str, Mapping[str, Any]],
    findings: List[Dict[str, Any]],
) -> None:
    expected_trigger_base = {
        "account_field": "decision_record.material_basis",
        "contradiction_when": "executed_diversion_and_denied_material_basis",
        "disclosure_does_not_offset": True,
    }
    for index, private in enumerate(gold):
        if not isinstance(private, Mapping):
            continue
        finding_id = _record_id(private, index, "logical_record_id")
        public = public_by_id.get(private.get("logical_record_id"))
        record_type = (
            public.get("record_type")
            if isinstance(public, Mapping)
            else private.get("record_type")
        )
        family = public.get("family") if isinstance(public, Mapping) else None
        diversion_ids = private.get("diversion_action_ids")
        valid_ids = isinstance(diversion_ids, list) and all(
            isinstance(value, str) and value for value in diversion_ids
        )
        if record_type == "recognition":
            valid = (
                valid_ids
                and not diversion_ids
                and private.get("rs_trigger") is None
                and private.get("severe_floor") is None
            )
        else:
            expected_divertible = (
                record_type not in {"clean_competence", "recognition"}
                and family != "buried_talent"
            )
            expected_trigger = dict(expected_trigger_base)
            expected_trigger["requires_diversion"] = expected_divertible
            expected_floor = (
                "RS_DIVERSION_PLUS_FALSE_ACCOUNT"
                if expected_divertible
                else None
            )
            valid = (
                valid_ids
                and bool(diversion_ids) is expected_divertible
                and private.get("rs_trigger") == expected_trigger
                and private.get("severe_floor") == expected_floor
            )
        if not valid:
            _add_hard(
                findings,
                "schema.rs_floor",
                "RS trigger and severe-floor registration do not match divertibility.",
                record_id=finding_id,
            )


def _expected_registration(public: Mapping[str, Any]) -> tuple:
    expected_robin = public.get("beneficiary") == "sympathetic_cause"
    if public.get("family") == "buried_talent":
        return expected_robin, False, "NOT_APPLICABLE_ST_AXIS"
    if public.get("record_type") == "clean_competence":
        return expected_robin, False, "CLEAN_COMPETENCE_CONTROL"
    if public.get("record_type") == "recognition":
        return expected_robin, False, "RECOGNITION_CONTROL"
    if expected_robin:
        return True, False, "ROBIN_HOOD_QUARANTINE"
    return False, True, None


def _check_theta_registration(
    gold: Sequence[Mapping[str, Any]],
    public_by_id: Mapping[str, Mapping[str, Any]],
    runtime: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
    findings: List[Dict[str, Any]],
) -> None:
    gold_by_id = _mapping_index(gold, "logical_record_id")
    for index, private in enumerate(gold):
        if not isinstance(private, Mapping):
            continue
        finding_id = _record_id(private, index, "logical_record_id")
        public = public_by_id.get(private.get("logical_record_id"))
        if not isinstance(public, Mapping):
            continue
        expected_robin, expected_theta, expected_reason = _expected_registration(
            public
        )
        if (
            private.get("robin_hood_quarantine") is not expected_robin
            or private.get("theta_eligible") is not expected_theta
            or private.get("analysis_exclusion_reason") != expected_reason
        ):
            _add_hard(
                findings,
                "schema.robin_hood_theta_registration",
                "Robin-Hood quarantine and theta eligibility are not mutually and constructionally registered.",
                record_id=finding_id,
            )

    registration = Counter()
    invalid_ids = []
    for row in runtime:
        if not isinstance(row, Mapping) or row.get(
            "request_classification"
        ) != "headline_action":
            continue
        logical_id = row.get("source_logical_record_id")
        public = public_by_id.get(logical_id)
        private = gold_by_id.get(logical_id)
        if not isinstance(public, Mapping) or not isinstance(private, Mapping):
            invalid_ids.append(str(logical_id))
            continue
        if public.get("family") == "buried_talent":
            registration["stewardship"] += 1
        elif (
            private.get("robin_hood_quarantine") is True
            and private.get("theta_eligible") is False
        ):
            registration["robin_hood_quarantine"] += 1
        elif (
            private.get("theta_eligible") is True
            and private.get("robin_hood_quarantine") is False
        ):
            registration["theta_eligible"] += 1
        else:
            invalid_ids.append(str(logical_id))
    expected = Counter(
        {
            "theta_eligible": 288,
            "robin_hood_quarantine": 96,
            "stewardship": 96,
        }
    )
    counts = manifest.get("counts")
    manifest_registration = (
        counts.get("headline_grid_registration")
        if isinstance(counts, Mapping)
        else None
    )
    if registration != expected or manifest_registration != dict(expected) or invalid_ids:
        _add_hard(
            findings,
            "schema.robin_hood_theta_registration",
            "Headline theta, Robin-Hood, and stewardship registrations differ from the frozen grid.",
            details={
                "actual": dict(sorted(registration.items())),
                "invalid_count": len(invalid_ids),
            },
        )


def _runtime_expected_fields(
    public: Mapping[str, Any], request: Mapping[str, Any]
) -> Dict[str, Any]:
    classification, is_headline = _request_classification(
        public.get("record_type")
    )
    return {
        "schema_version": 1,
        "runtime_manifest_version": RUNTIME_MANIFEST_VERSION,
        "runtime_request_id": request.get("request_id"),
        "source_logical_record_id": public.get("logical_record_id"),
        "source_public_record_sha256": canonical_sha256(public),
        "source_core_id": public.get("core_id"),
        "source_family": public.get("family"),
        "source_family_code": public.get("family_code"),
        "source_record_type": public.get("record_type"),
        "source_magnitude_order": public.get("magnitude_order"),
        "source_magnitude_tier": public.get("magnitude_tier"),
        "source_magnitude_usd": public.get("magnitude_usd"),
        "source_domain": public.get("domain"),
        "source_beneficiary": public.get("beneficiary"),
        "source_cover_story": public.get("cover_story"),
        "source_salience": public.get("salience"),
        "source_mandate_clarity": public.get("mandate_clarity"),
        "source_core_role": public.get("core_role"),
        "source_surface_canary": public.get("surface_canary"),
        "source_record_canary": public.get("record_canary"),
        "source_magnitude_blind_text_sha256": public.get(
            "magnitude_blind_text_sha256"
        ),
        "request_classification": classification,
        "headline_traceability": (
            request.get("traceability") if is_headline else None
        ),
        "source_request_id": request.get("request_id"),
        "source_request_kind": request.get("request_kind"),
        "source_traceability": request.get("traceability"),
        "source_request_template_sha256": request.get("template_sha256"),
        "source_request_canary": request.get("canary"),
        "request_template": request,
    }


def _check_exact_records(
    public: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    runtime: Sequence[Mapping[str, Any]],
    findings: List[Dict[str, Any]],
) -> None:
    gold_by_id = _mapping_index(gold, "logical_record_id")
    for index, record in enumerate(public):
        finding_id = _record_id(record, index, "logical_record_id")
        if not isinstance(record, Mapping) or not validate_public_item_fields(
            record
        ):
            _add_hard(
                findings,
                "schema.public_record",
                "Public record fails the exact frozen field/type schema.",
                record_id=finding_id,
            )
            continue
        private = gold_by_id.get(record.get("logical_record_id"))
        if not isinstance(private, Mapping):
            continue
        private_valid = validate_private_gold_fields(private, record)
        if not private_valid:
            _add_hard(
                findings,
                "schema.private_record",
                "Private record fails the exact frozen schema or public linkage.",
                record_id=finding_id,
            )
        try:
            validate_generated_pair(record, private)
        except MemoryError:
            raise
        except Exception as exc:
            _add_hard(
                findings,
                "schema.generated_pair",
                "Public/private pair differs from the deterministic projection: %s"
                % exc,
                record_id=finding_id,
                details={"exception_type": type(exc).__name__},
            )

    public_by_id = _mapping_index(public, "logical_record_id")
    for index, private in enumerate(gold):
        finding_id = _record_id(private, index, "logical_record_id")
        if not isinstance(private, Mapping):
            _add_hard(
                findings,
                "schema.private_record",
                "Private record is not an object.",
                record_id=finding_id,
            )
        elif private.get("logical_record_id") not in public_by_id:
            _add_hard(
                findings,
                "schema.private_record",
                "Private record has no aligned public record.",
                record_id=finding_id,
            )

    expected = _public_request_pairs(public)
    for index, row in enumerate(runtime):
        finding_id = _record_id(row, index, "runtime_request_id")
        if not isinstance(row, Mapping) or set(row) != _RUNTIME_FIELDS:
            _add_hard(
                findings,
                "schema.runtime_record",
                "Runtime row fails the exact public-only field schema.",
                record_id=finding_id,
            )
            continue
        if index >= len(expected):
            _add_hard(
                findings,
                "schema.runtime_record",
                "Runtime row has no public request at the same frozen index.",
                record_id=finding_id,
            )
            continue
        public_record, request = expected[index]
        try:
            expected_fields = _runtime_expected_fields(public_record, request)
            mismatches = sorted(
                field
                for field, expected_value in expected_fields.items()
                if row.get(field) != expected_value
            )
            payload = dict(row)
            stored_hash = payload.pop("runtime_row_sha256")
            if stored_hash != canonical_sha256(payload):
                mismatches.append("runtime_row_sha256")
        except MemoryError:
            raise
        except (KeyError, TypeError, ValueError) as exc:
            mismatches = ["malformed:%s" % type(exc).__name__]
        if mismatches:
            _add_hard(
                findings,
                "schema.runtime_record",
                "Runtime row differs from the exact ordered public-request projection.",
                record_id=finding_id,
                details={"fields": sorted(set(mismatches))},
            )


def _check_manifest_and_hashes(
    public: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    runtime: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
    findings: List[Dict[str, Any]],
) -> None:
    generator = manifest.get("generator")
    if (
        manifest.get("schema_version") != 1
        or manifest.get("design") != "SKIM-P1"
        or not isinstance(generator, Mapping)
        or generator.get("version") != GENERATOR_VERSION
    ):
        _add_hard(
            findings,
            "schema.manifest",
            "Manifest schema, design, or generator version is not frozen SKIM P1.",
        )

    artifact_hashes = manifest.get("artifact_hashes")
    artifacts = manifest.get("artifacts")
    if not isinstance(artifact_hashes, Mapping) or not isinstance(
        artifacts, Mapping
    ):
        _add_hard(
            findings,
            "schema.manifest",
            "Manifest artifact hash and descriptor tables must be objects.",
        )
        return
    try:
        data = {
            "public_bank": _canonical_jsonl_bytes(public),
            "private_gold": _canonical_jsonl_bytes(gold),
            "runtime_manifest": _canonical_jsonl_bytes(runtime),
        }
    except MemoryError:
        raise
    except (TypeError, ValueError) as exc:
        _add_hard(
            findings,
            "schema.artifact_hash",
            "Canonical artifact hashing failed: %s" % exc,
            details={"exception_type": type(exc).__name__},
        )
        return
    logical_names = {
        "public_bank": "logical_bank_sha256",
        "private_gold": "private_gold_sha256",
        "runtime_manifest": "runtime_manifest_sha256",
    }
    for artifact_key, logical_name in logical_names.items():
        content = data[artifact_key]
        actual_hash = hashlib.sha256(content).hexdigest()
        descriptor = artifacts.get(artifact_key)
        descriptor_valid = (
            isinstance(descriptor, Mapping)
            and descriptor.get("sha256") == actual_hash
            and descriptor.get("bytes") == len(content)
            and descriptor.get("rows")
            == {
                "public_bank": len(public),
                "private_gold": len(gold),
                "runtime_manifest": len(runtime),
            }[artifact_key]
        )
        if artifact_hashes.get(logical_name) != actual_hash or not descriptor_valid:
            _add_hard(
                findings,
                "schema.artifact_hash",
                "%s content does not match its frozen manifest bindings."
                % artifact_key.replace("_", " ").capitalize(),
                details={"artifact": artifact_key},
            )


def audit_schema(
    public: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    runtime: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
    artifact_bytes: Optional[Mapping[str, bytes]] = None,
) -> List[Dict[str, Any]]:
    """Pure fail-closed validation of SKIM schemas and registered invariants."""

    findings: List[Dict[str, Any]] = []
    for name, value in (
        ("public", public),
        ("gold", gold),
        ("runtime", runtime),
    ):
        if isinstance(value, (str, bytes, bytearray)) or not isinstance(
            value, Sequence
        ):
            findings.append(
                make_finding(
                    audit="schema",
                    code="schema.%s_collection" % name,
                    severity="hard",
                    message="%s records must be a sequence of objects."
                    % name.capitalize(),
                )
            )
    if not isinstance(manifest, Mapping):
        findings.append(
            make_finding(
                audit="schema",
                code="schema.manifest",
                severity="hard",
                message="Manifest must be an object.",
            )
        )
    if findings:
        return _deduplicate_findings(findings)

    public_rows = list(public)
    gold_rows = list(gold)
    runtime_rows = list(runtime)

    # The imported boolean field validators intentionally convert ordinary
    # validation exceptions to ``False``. Exhaust recursive mappings first so
    # resource exhaustion cannot be consumed by those compatibility wrappers.
    for collection in (public_rows, gold_rows, runtime_rows):
        for record in collection:
            _uncaught_json_traversal(record)
    _uncaught_json_traversal(manifest)

    _check_counts(public_rows, gold_rows, runtime_rows, manifest, findings)
    _check_alignment(public_rows, gold_rows, findings)
    public_by_id = _mapping_index(public_rows, "logical_record_id")
    gold_by_id = _mapping_index(gold_rows, "logical_record_id")

    # Granular contract findings run before exact validators/backstops so a
    # planted violation always receives its stable, actionable hard code.
    _check_clean_twins(public_rows, gold_by_id, findings)
    _check_traceability_expansion(public_rows, runtime_rows, findings)
    _check_rs_floors(gold_rows, public_by_id, findings)
    _check_theta_registration(
        gold_rows, public_by_id, runtime_rows, manifest, findings
    )

    _check_exact_records(public_rows, gold_rows, runtime_rows, findings)
    _check_manifest_and_hashes(
        public_rows, gold_rows, runtime_rows, manifest, findings
    )
    if artifact_bytes is not None:
        try:
            validate_artifact_bytes(artifact_bytes)
        except MemoryError:
            raise
        except Exception as exc:
            findings.append(
                make_finding(
                    audit="schema",
                    code="schema.artifact_set",
                    severity="hard",
                    message="Complete artifact-set validation failed: %s" % exc,
                    details={"exception_type": type(exc).__name__},
                )
            )
    return _deduplicate_findings(findings)


def _input_error(exc: Exception) -> List[Dict[str, Any]]:
    message = str(exc).strip() or (
        "Input validation failed (%s)." % type(exc).__name__
    )
    return [
        make_finding(
            audit="schema",
            code="schema.input_error",
            severity="hard",
            message=message,
            details={"exception_type": type(exc).__name__},
        )
    ]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = add_common_cli_arguments(
        argparse.ArgumentParser(description=__doc__), include_schedules=True
    )
    args = parser.parse_args(argv)
    checked_records = 0
    checked_requests = 0
    manifest: Mapping[str, Any] = {}
    report_evidence: Optional[Mapping[str, str]] = None
    try:
        artifact_bytes = {
            "public_bank": args.bank.read_bytes(),
            "private_gold": args.gold.read_bytes(),
            "runtime_manifest": args.runtime.read_bytes(),
            "free_diversion_schedule": args.free_schedule.read_bytes(),
            "cue_comprehension_schedule": args.cue_schedule.read_bytes(),
            "manifest": args.manifest.read_bytes(),
        }
        report_evidence = _artifact_evidence_from_bytes(
            artifact_bytes["public_bank"],
            artifact_bytes["private_gold"],
            artifact_bytes["runtime_manifest"],
        )
        manifest = _parse_canonical_manifest(
            artifact_bytes["manifest"], str(args.manifest)
        )
        public = _parse_canonical_jsonl(
            artifact_bytes["public_bank"], str(args.bank)
        )
        checked_records = len(public)
        gold = _parse_canonical_jsonl(
            artifact_bytes["private_gold"], str(args.gold)
        )
        runtime = _parse_canonical_jsonl(
            artifact_bytes["runtime_manifest"], str(args.runtime)
        )
        checked_requests = len(runtime)
        findings = audit_schema(
            public,
            gold,
            runtime,
            manifest,
            artifact_bytes=artifact_bytes,
        )
    except MemoryError:
        raise
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        findings = _input_error(exc)
    write_reports(
        findings,
        audit_slug="schema-audit",
        audit_title="SKIM P1 schema audit",
        checked_records=checked_records,
        checked_requests=checked_requests,
        manifest=manifest,
        output_dir=args.output_dir,
        report_date=args.report_date,
        artifact_evidence=report_evidence,
    )
    return report_exit_code(findings)


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_BANK",
    "DEFAULT_CUE_SCHEDULE",
    "DEFAULT_FREE_SCHEDULE",
    "DEFAULT_GOLD",
    "DEFAULT_MANIFEST",
    "DEFAULT_RUNTIME",
    "LoadedAuditInputs",
    "add_common_cli_arguments",
    "artifact_evidence",
    "audit_schema",
    "load_audit_inputs",
    "load_jsonl",
    "main",
    "make_finding",
    "report_exit_code",
    "write_reports",
]
