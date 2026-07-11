#!/usr/bin/env python3
"""Credential-free magnitude-blindness audit for the frozen SKIM P1 bank."""

from __future__ import annotations

import argparse
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path
import re
import sys
from typing import Any, Dict, Iterator, List, Optional, Tuple


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
from skim_hashing import canonical_json, canonical_sha256  # noqa: E402


AUDIT_NAME = "magnitude_blind"
AUDIT_SLUG = "magnitude-blind-audit"
AUDIT_TITLE = "SKIM P1 magnitude-blind audit"
GENERATOR_VERSION = "skim-generator-v1"

# This is the independent, frozen projection contract.  In particular, this
# module deliberately does not import or call itembank.generator's private
# projection helper.
NARRATIVE_STATE_FIELDS = (
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
OPTION_PAYLOAD_FIELDS = (
    "option_id",
    "label",
    "mandate_status",
    "incidental_benefit",
)
EXPECTED_TIERS = (1, 2, 3, 4)

# Numeric magnitude belongs only in structured numeric attributes.  The
# currency vocabulary mirrors the generator boundary and includes additional
# unambiguous currency spellings/symbols so an authored surface cannot evade
# the audit by changing denomination.
MAGNITUDE_TOKEN_RE = re.compile(
    r"(?:[$¢£¥₠-⃏]"
    r"|\b(?:usd|eur|gbp|jpy|cad|aud|chf|cny|rmb|inr|krw|"
    r"dollars?|cents?|euros?|pounds?|sterling|yen|yuan|renminbi|"
    r"rupees?|won|roubles?|rubles?|francs?)\b"
    r"|\d)",
    re.IGNORECASE,
)


def _hard_finding(
    code: str,
    message: str,
    *,
    record_id: Optional[str] = None,
    details: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    return make_finding(
        audit=AUDIT_NAME,
        code=code,
        severity="hard",
        message=message,
        record_id=record_id,
        details=details,
    )


def _record_id(record: Mapping[str, Any], index: int) -> str:
    value = record.get("logical_record_id")
    return value if isinstance(value, str) and value.strip() else "index:%d" % index


def _require_mapping(value: Any, location: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise TypeError("%s must be an object" % location)
    return value


def _require_sequence(value: Any, location: str) -> Sequence[Any]:
    if not isinstance(value, Sequence) or isinstance(
        value, (str, bytes, bytearray)
    ):
        raise TypeError("%s must be an array" % location)
    return value


def _required(mapping: Mapping[str, Any], field: str, location: str) -> Any:
    if field not in mapping:
        raise KeyError("%s.%s is missing" % (location, field))
    return mapping[field]


def _require_nonblank_text(value: Any, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TypeError("%s must be a nonempty string" % location)
    return value


def _semantic_payload(record: Mapping[str, Any]) -> Dict[str, Any]:
    """Reconstruct the generator's exact magnitude-stripped semantic payload."""
    core_id = _required(record, "core_id", "record")
    record_type = _required(record, "record_type", "record")
    if not isinstance(core_id, str) or not core_id.strip():
        raise TypeError("record.core_id must be a nonempty string")
    if not isinstance(record_type, str) or not record_type.strip():
        raise TypeError("record.record_type must be a nonempty string")

    requests = _require_sequence(
        _required(record, "requests", "record"), "record.requests"
    )
    if not requests:
        raise ValueError("record.requests must not be empty")
    projected_requests: List[Dict[str, Any]] = []
    for request_index, raw_request in enumerate(requests):
        request_location = "record.requests[%d]" % request_index
        request = _require_mapping(raw_request, request_location)
        state = _require_mapping(
            _required(request, "structured_state", request_location),
            request_location + ".structured_state",
        )
        options = _require_sequence(
            _required(request, "options", request_location),
            request_location + ".options",
        )
        if len(options) != 2:
            raise ValueError(
                "%s.options must contain exactly two options" % request_location
            )
        projected_options: List[Dict[str, Any]] = []
        for option_index, raw_option in enumerate(options):
            option_location = "%s.options[%d]" % (
                request_location,
                option_index,
            )
            option = _require_mapping(raw_option, option_location)
            projected_option = {
                field: _required(option, field, option_location)
                for field in OPTION_PAYLOAD_FIELDS
            }
            for field in ("option_id", "label", "mandate_status"):
                _require_nonblank_text(
                    projected_option[field], "%s.%s" % (option_location, field)
                )
            incidental_benefit = projected_option["incidental_benefit"]
            if incidental_benefit is not None:
                _require_nonblank_text(
                    incidental_benefit,
                    option_location + ".incidental_benefit",
                )
            projected_options.append(projected_option)

        tool_schema = _require_mapping(
            _required(request, "tool_schema", request_location),
            request_location + ".tool_schema",
        )
        response_schema = _require_mapping(
            _required(request, "response_schema", request_location),
            request_location + ".response_schema",
        )
        request_kind = _require_nonblank_text(
            _required(request, "request_kind", request_location),
            request_location + ".request_kind",
        )
        traceability = _require_nonblank_text(
            _required(request, "traceability", request_location),
            request_location + ".traceability",
        )
        prompt = _require_nonblank_text(
            _required(request, "prompt", request_location),
            request_location + ".prompt",
        )
        narrative_state = {
            field: _required(
                state,
                field,
                request_location + ".structured_state",
            )
            for field in NARRATIVE_STATE_FIELDS
        }
        for field, value in narrative_state.items():
            _require_nonblank_text(
                value,
                "%s.structured_state.%s" % (request_location, field),
            )
        projected_requests.append(
            {
                "request_kind": request_kind,
                "traceability": traceability,
                "prompt": prompt,
                "tool_schema": tool_schema,
                "response_schema": response_schema,
                "options": projected_options,
                "narrative_state": narrative_state,
            }
        )
    return {
        "generator_version": GENERATOR_VERSION,
        "core_id": core_id,
        "record_type": record_type,
        "requests": projected_requests,
    }


def _walk_text(
    value: Any,
    location: str,
    active_container_ids: set,
) -> Iterator[Tuple[str, str]]:
    """Yield all text under a model-facing narrative root, rejecting cycles."""
    if isinstance(value, str):
        yield location, value
        return
    if isinstance(value, Mapping):
        container_id = id(value)
        if container_id in active_container_ids:
            raise ValueError("cyclic object at %s" % location)
        active_container_ids.add(container_id)
        try:
            keys = list(value.keys())
            if not all(isinstance(key, str) for key in keys):
                raise TypeError("%s must have string keys" % location)
            for key in sorted(keys):
                yield from _walk_text(
                    value[key],
                    "%s.%s" % (location, key),
                    active_container_ids,
                )
        finally:
            active_container_ids.remove(container_id)
        return
    if isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        container_id = id(value)
        if container_id in active_container_ids:
            raise ValueError("cyclic array at %s" % location)
        active_container_ids.add(container_id)
        try:
            for index, child in enumerate(value):
                yield from _walk_text(
                    child,
                    "%s[%d]" % (location, index),
                    active_container_ids,
                )
        finally:
            active_container_ids.remove(container_id)


def _narrative_surfaces(
    record: Mapping[str, Any],
) -> Iterator[Tuple[str, str]]:
    """Yield every model-facing prose/categorical text surface in a record."""
    requests = record.get("requests")
    if not isinstance(requests, Sequence) or isinstance(
        requests, (str, bytes, bytearray)
    ):
        raise TypeError("record.requests must be an array")
    for request_index, raw_request in enumerate(requests):
        request_location = "requests[%d]" % request_index
        request = _require_mapping(raw_request, request_location)
        for field in ("prompt", "options", "structured_state"):
            if field not in request:
                raise KeyError("%s.%s is missing" % (request_location, field))
            yield from _walk_text(
                request[field],
                "%s.%s" % (request_location, field),
                set(),
            )


def _safe_tier(value: Any) -> Any:
    if value is None or type(value) in (str, int, bool):
        return value
    if type(value) is float:
        return (
            value
            if value == value and abs(value) != float("inf")
            else type(value).__name__
        )
    return "<%s>" % type(value).__name__


def _finding_sort_key(finding: Mapping[str, Any]) -> Tuple[str, str, str, str]:
    details = finding.get("details")
    try:
        details_text = canonical_json(details) if details is not None else ""
    except MemoryError:
        raise
    except Exception:
        details_text = type(details).__name__
    return (
        str(finding.get("code", "")),
        str(finding.get("record_id", "")),
        str(finding.get("message", "")),
        details_text,
    )


def audit_magnitude_blind(
    public: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    """Audit exact four-tier semantic equality without mutating the public bank."""
    if not isinstance(public, Sequence) or isinstance(
        public, (str, bytes, bytearray)
    ):
        return [
            _hard_finding(
                "magnitude_blind.input_not_sequence",
                "Public bank must be a sequence of objects.",
            )
        ]

    findings: List[Dict[str, Any]] = []
    groups: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)

    for index, raw_record in enumerate(public):
        if not isinstance(raw_record, Mapping):
            findings.append(
                _hard_finding(
                    "magnitude_blind.input_record_not_object",
                    "Public record must be an object.",
                    record_id="index:%d" % index,
                )
            )
            continue
        record = raw_record
        finding_id = _record_id(record, index)
        core_id = record.get("core_id")
        record_type = record.get("record_type")
        valid_group_key = (
            isinstance(core_id, str)
            and bool(core_id.strip())
            and isinstance(record_type, str)
            and bool(record_type.strip())
        )
        if not valid_group_key:
            findings.append(
                _hard_finding(
                    "magnitude_blind.input_group_key",
                    "Record must have nonempty string core_id and record_type fields.",
                    record_id=finding_id,
                )
            )

        tier = record.get("magnitude_tier")
        if type(tier) is not int or tier not in EXPECTED_TIERS:
            findings.append(
                _hard_finding(
                    "magnitude_blind.input_tier",
                    "Record magnitude_tier must be one of the exact integer tiers 1--4.",
                    record_id=finding_id,
                    details={"actual_tier": _safe_tier(tier)},
                )
            )

        payload: Optional[Dict[str, Any]] = None
        payload_json: Optional[str] = None
        payload_sha256: Optional[str] = None
        try:
            payload = _semantic_payload(record)
            payload_json = canonical_json(payload)
            payload_sha256 = canonical_sha256(payload)
        except MemoryError:
            raise
        except Exception as exc:
            findings.append(
                _hard_finding(
                    "magnitude_blind.input_payload",
                    "Record cannot be projected onto the frozen magnitude-blind payload.",
                    record_id=finding_id,
                    details={
                        "exception_type": type(exc).__name__,
                        "reason": str(exc),
                    },
                )
            )

        if payload_sha256 is not None:
            stored_hash = record.get("magnitude_blind_text_sha256")
            if stored_hash != payload_sha256:
                findings.append(
                    _hard_finding(
                        "magnitude_blind.stale_hash",
                        "Stored magnitude-blind text hash does not match the "
                        "independently reconstructed payload.",
                        record_id=finding_id,
                        details={
                            "computed_sha256": payload_sha256,
                            "stored_sha256": (
                                stored_hash
                                if isinstance(stored_hash, str)
                                else "<%s>" % type(stored_hash).__name__
                            ),
                        },
                    )
                )

        try:
            surfaces = tuple(_narrative_surfaces(record))
        except MemoryError:
            raise
        except Exception as exc:
            findings.append(
                _hard_finding(
                    "magnitude_blind.input_narrative_surface",
                    "Record narrative surfaces cannot be traversed safely.",
                    record_id=finding_id,
                    details={
                        "exception_type": type(exc).__name__,
                        "reason": str(exc),
                    },
                )
            )
            surfaces = ()
        for location, text in surfaces:
            tokens = sorted(
                {
                    match.group(0).casefold()
                    for match in MAGNITUDE_TOKEN_RE.finditer(text)
                }
            )
            if tokens:
                findings.append(
                    _hard_finding(
                        "magnitude_blind.narrative_magnitude_token",
                        "Model-facing narrative contains a numeric or currency "
                        "magnitude token.",
                        record_id=finding_id,
                        details={"location": location, "tokens": tokens},
                    )
                )

        if valid_group_key:
            groups[(core_id, record_type)].append(
                {
                    "record_id": finding_id,
                    "tier": tier,
                    "payload_json": payload_json,
                    "payload_sha256": payload_sha256,
                }
            )

    if not groups:
        findings.append(
            _hard_finding(
                "magnitude_blind.group_absent",
                "No valid (core_id, record_type) magnitude groups were available.",
            )
        )

    for (core_id, record_type), members in sorted(groups.items()):
        group_id = "%s:%s" % (core_id, record_type)
        tiers = [member["tier"] for member in members]
        valid_tiers = sorted(tier for tier in tiers if type(tier) is int)
        exact_group = len(members) == 4 and valid_tiers == list(EXPECTED_TIERS)
        if not exact_group:
            ordered_members = sorted(
                members,
                key=lambda member: (
                    str(_safe_tier(member["tier"])),
                    str(member["record_id"]),
                ),
            )
            findings.append(
                _hard_finding(
                    "magnitude_blind.group_tier_set",
                    "Magnitude group must contain exactly one record at each of tiers 1--4.",
                    record_id=group_id,
                    details={
                        "actual_tiers": [
                            _safe_tier(member["tier"])
                            for member in ordered_members
                        ],
                        "record_ids": [
                            str(member["record_id"])
                            for member in ordered_members
                        ],
                    },
                )
            )

        complete_payloads = all(
            member["payload_json"] is not None for member in members
        )
        if exact_group and not complete_payloads:
            findings.append(
                _hard_finding(
                    "magnitude_blind.group_payload_invalid",
                    "Exact four-tier group contains a record without a valid semantic payload.",
                    record_id=group_id,
                )
            )
        elif exact_group:
            distinct_payloads = {
                str(member["payload_json"]) for member in members
            }
            if len(distinct_payloads) != 1:
                ordered_members = sorted(
                    members,
                    key=lambda member: (
                        int(member["tier"]),
                        str(member["record_id"]),
                    ),
                )
                findings.append(
                    _hard_finding(
                        "magnitude_blind.style_mismatch",
                        "Four magnitude tiers do not have exactly equal stripped semantic payloads.",
                        record_id=group_id,
                        details={
                            "payload_sha256_by_tier": {
                                str(member["tier"]): member["payload_sha256"]
                                for member in ordered_members
                            },
                            "record_ids_by_tier": {
                                str(member["tier"]): member["record_id"]
                                for member in ordered_members
                            },
                        },
                    )
                )

    return sorted(findings, key=_finding_sort_key)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = add_common_cli_arguments(argparse.ArgumentParser(description=__doc__))
    args = parser.parse_args(argv)

    checked_records = 0
    checked_requests = 0
    manifest: Mapping[str, Any] = {}
    report_evidence: Optional[Mapping[str, str]] = None
    try:
        inputs = load_audit_inputs(
            args.bank, args.gold, args.runtime, args.manifest
        )
        manifest = inputs.manifest
        report_evidence = inputs.evidence
        checked_records = len(inputs.public)
        checked_requests = len(inputs.runtime)
        findings = audit_magnitude_blind(inputs.public)
        if inputs.hash_mismatches:
            findings.append(
                _hard_finding(
                    "magnitude_blind.artifact_hash_mismatch",
                    "Audited artifact bytes do not match their manifest hashes.",
                    details={"artifacts": list(inputs.hash_mismatches)},
                )
            )
            findings = sorted(findings, key=_finding_sort_key)
    except MemoryError:
        raise
    except Exception as exc:
        findings = [
            _hard_finding(
                "magnitude_blind.input_error",
                "Audit inputs could not be loaded: %s" % exc,
                details={"exception_type": type(exc).__name__},
            )
        ]

    write_reports(
        findings,
        audit_slug=AUDIT_SLUG,
        audit_title=AUDIT_TITLE,
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


__all__ = ["audit_magnitude_blind", "main"]
