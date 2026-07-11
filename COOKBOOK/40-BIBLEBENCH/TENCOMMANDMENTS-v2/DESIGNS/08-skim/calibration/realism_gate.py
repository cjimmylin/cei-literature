#!/usr/bin/env python3
"""Fail-closed professional-realism gate for the frozen SKIM P1 packet."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from collections.abc import Mapping, Sequence
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any, Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from calibration.export_realism_packet import (  # noqa: E402
    build_realism_packet,
    canonical_jsonl_sha256,
)
from skim_constants import (  # noqa: E402
    DOMAINS,
    FAMILIES,
    FAMILY_CODES,
    MAGNITUDE_WINDOWS,
    PROFESSIONAL_REALISM_REQUIREMENTS,
    REVISION_HISTORY_FIELDS,
)
from skim_evidence import evaluate_professional_realism  # noqa: E402
from skim_hashing import canonical_json, canonical_sha256  # noqa: E402


INSTRUMENT = "SKIM-P1-PROFESSIONAL-REALISM"
NOT_RUN_STATUS = "NOT_RUN_PROFESSIONAL_REALISM"
HUMAN_BASELINE_NOT_RUN = "NOT_RUN_HUMAN_BASELINE"
DEFAULT_PUBLIC_BANK = ROOT / "itembank" / "bank" / "p1-public.jsonl"
DEFAULT_MANIFEST = ROOT / "itembank" / "manifest.json"
FROZEN_PUBLIC_BANK_SHA256 = (
    "b086718e70be89f7d7566bba058f8ebe52add4e6768ac5bed5a539a02608d385"
)
FROZEN_ITEMBANK_MANIFEST_SHA256 = (
    "edb8d11954d60c55a5d5d9d379ff692c3ac84fb2b2c9dd93b85e6eb2491d2ed2"
)

BINARY_FIELDS = (
    "scenario_realism",
    "magnitude_window_plausibility",
)
ORDINAL_FIELDS = (
    "scenario_realism_rating_1_to_5",
    "magnitude_window_plausibility_rating_1_to_5",
)
RATING_FIELDS = BINARY_FIELDS + ORDINAL_FIELDS

_PACKET_FIELDS = frozenset(
    {
        "review_id",
        "stratum_id",
        "domain",
        "scenario",
        "principal_mandate",
        "magnitude_window_usd",
        "rating_form",
    }
)
_LINKAGE_FIELDS = frozenset(
    {
        "review_id",
        "stratum_id",
        "core_id",
        "family",
        "family_code",
        "primary_logical_record_ids",
        "public_record_sha256_by_tier",
        "source_bank_sha256",
    }
)
_EVIDENCE_FIELDS = frozenset(
    {
        "schema_version",
        "instrument",
        "data_basis",
        "packet_sha256",
        "linkage_sha256",
        "panel",
        "ratings",
        "adjudications",
        "revision_history",
    }
)
_PANEL_FIELDS = frozenset(
    {
        "rater_id",
        "qualification",
        "qualification_evidence",
        "covers_procurement",
        "covers_finance",
        "synthetic",
    }
)
_RATING_RECORD_FIELDS = frozenset(
    {"review_id", "rater_id", "independent_submission", *RATING_FIELDS}
)
_ADJUDICATION_FIELDS = frozenset(
    {
        "review_id",
        "adjudicator_id",
        "disagreement_fields",
        "resolution",
        "reason",
    }
)
_PROFESSIONAL_QUALIFICATIONS = {
    "procurement_professional": (True, False),
    "finance_professional": (False, True),
    "procurement_finance_professional": (True, True),
}
_SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
_REVIEW_ID_RE = re.compile(r"skim-realism-review-[0-9a-f]{24}\Z")
_STRATUM_ID_RE = re.compile(r"skim-realism-stratum-[0-9a-f]{24}\Z")
_PROHIBITED_EVIDENCE_MARKERS = (
    "synthetic",
    "fixture",
    "literature",
    "modelgenerated",
)
_TIER_KEYS = frozenset(("1", "2", "3", "4"))


class _GateValidationError(ValueError):
    """Stable internal validation failure with a machine-facing reason."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def _fail(code: str) -> None:
    raise _GateValidationError(code)


def _canonical_identifier(value: Any) -> bool:
    return (
        type(value) is str
        and bool(value)
        and value == value.strip()
        and value == " ".join(value.split())
    )


def _valid_sha256(value: Any) -> bool:
    return (
        type(value) is str
        and _SHA256_RE.fullmatch(value) is not None
        and value != "0" * 64
    )


def _valid_ordinal(value: Any) -> bool:
    return type(value) is int and 1 <= value <= 5


def _safe_jsonl_sha256(rows: Any) -> Optional[str]:
    try:
        return canonical_jsonl_sha256(rows)
    except MemoryError:
        raise
    except Exception:
        return None


def _safe_canonical_sha256(value: Any) -> Optional[str]:
    try:
        return canonical_sha256(value)
    except MemoryError:
        raise
    except Exception:
        return None


def _has_prohibited_evidence_marker(value: str) -> bool:
    normalized = re.sub(r"[^a-z0-9]+", "", value.casefold())
    return any(marker in normalized for marker in _PROHIBITED_EVIDENCE_MARKERS)


def _scan_evidence_provenance(value: Any, active: Optional[set] = None) -> None:
    """Reject prohibited provenance markers in values, never in field names."""

    if type(value) is str:
        if _has_prohibited_evidence_marker(value):
            _fail("PROHIBITED_EVIDENCE_PROVENANCE")
        return
    if active is None:
        active = set()
    if isinstance(value, Mapping):
        marker = id(value)
        if marker in active:
            _fail("INVALID_EVIDENCE_PROVENANCE")
        active.add(marker)
        try:
            for child in value.values():
                _scan_evidence_provenance(child, active)
        finally:
            active.remove(marker)
    elif isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        marker = id(value)
        if marker in active:
            _fail("INVALID_EVIDENCE_PROVENANCE")
        active.add(marker)
        try:
            for child in value:
                _scan_evidence_provenance(child, active)
        finally:
            active.remove(marker)


@lru_cache(maxsize=1)
def _frozen_bank_contract() -> Tuple[str, Dict[str, Dict[str, Any]]]:
    """Load and derive the one trusted canonical public-bank projection."""

    bank_bytes = DEFAULT_PUBLIC_BANK.read_bytes()
    manifest_bytes = DEFAULT_MANIFEST.read_bytes()
    rows = _parse_canonical_jsonl_bytes(bank_bytes, str(DEFAULT_PUBLIC_BANK))
    manifest = _parse_canonical_json_bytes(
        manifest_bytes, str(DEFAULT_MANIFEST)
    )
    source_bank_sha256 = hashlib.sha256(bank_bytes).hexdigest()
    manifest_sha256 = hashlib.sha256(manifest_bytes).hexdigest()
    if (
        source_bank_sha256 != FROZEN_PUBLIC_BANK_SHA256
        or manifest_sha256 != FROZEN_ITEMBANK_MANIFEST_SHA256
        or canonical_jsonl_sha256(rows) != source_bank_sha256
    ):
        raise ValueError("frozen public bank bytes are not exact canonical JSONL")
    artifact_hashes = manifest.get("artifact_hashes")
    artifacts = manifest.get("artifacts")
    public_descriptor = (
        artifacts.get("public_bank") if type(artifacts) is dict else None
    )
    if (
        type(artifact_hashes) is not dict
        or artifact_hashes.get("logical_bank_sha256") != source_bank_sha256
        or type(public_descriptor) is not dict
        or public_descriptor.get("sha256") != source_bank_sha256
        or public_descriptor.get("bytes") != len(bank_bytes)
        or public_descriptor.get("rows") != len(rows)
    ):
        raise ValueError("frozen manifest does not bind the public bank bytes")

    expected_packet, expected_linkage, _result_payload = build_realism_packet(
        rows, seed=0
    )
    expected_by_core: Dict[str, Dict[str, Any]] = {}
    for packet_row, linkage_row in zip(expected_packet, expected_linkage):
        if linkage_row["source_bank_sha256"] != source_bank_sha256:
            raise ValueError("export projection is not bound to frozen bank bytes")
        core_id = linkage_row["core_id"]
        expected_by_core[core_id] = {
            "family": linkage_row["family"],
            "family_code": linkage_row["family_code"],
            "primary_logical_record_ids": tuple(
                linkage_row["primary_logical_record_ids"]
            ),
            "public_record_sha256_by_tier": dict(
                linkage_row["public_record_sha256_by_tier"]
            ),
            "domain": packet_row["domain"],
            "scenario": packet_row["scenario"],
            "principal_mandate": packet_row["principal_mandate"],
            "magnitude_window_usd": tuple(packet_row["magnitude_window_usd"]),
        }
    if len(expected_by_core) != 40:
        raise ValueError("frozen professional projection must contain 40 cores")
    return source_bank_sha256, expected_by_core


def _safe_frozen_source_sha256() -> Optional[str]:
    try:
        return _frozen_bank_contract()[0]
    except MemoryError:
        raise
    except Exception:
        return None


def _reported_data_basis(evidence: Any) -> Optional[str]:
    if type(evidence) is not dict:
        return None
    value = evidence.get("data_basis")
    return value if type(value) is str else None


def _finalize_result_hash(payload: Dict[str, Any]) -> Dict[str, Any]:
    payload["artifact_sha256"]["result"] = None
    payload["artifact_sha256"]["result"] = canonical_sha256(payload)
    return payload


def _result(
    *,
    status: str,
    packet_sha256: Optional[str],
    linkage_sha256: Optional[str],
    evidence_sha256: Optional[str],
    source_bank_sha256: Optional[str] = None,
    data_basis: Optional[str] = None,
    counts: Optional[Mapping[str, int]] = None,
    family_passing_cores: Optional[Mapping[str, int]] = None,
    fleiss_kappa: Optional[Mapping[str, Optional[float]]] = None,
    reasons: Sequence[str] = (),
) -> Dict[str, Any]:
    if status not in {NOT_RUN_STATUS, "PASS", "FAIL"}:
        raise ValueError("invalid professional-realism outer status")
    payload: Dict[str, Any] = {
        "schema_version": 1,
        "instrument": INSTRUMENT,
        "status": status,
        "data_basis": data_basis,
        "eligible_for_model_pilot": status == "PASS",
        "eligible_for_empirical_decision": False,
        "counts": dict(
            counts
            or {
                "cores": 40,
                "families": 5,
                "professionals": 0,
                "ratings": 0,
                "adjudications": 0,
            }
        ),
        "family_passing_cores": dict(family_passing_cores or {}),
        "fleiss_kappa": dict(
            fleiss_kappa
            or {
                "scenario_realism": None,
                "magnitude_window_plausibility": None,
            }
        ),
        "thresholds": dict(PROFESSIONAL_REALISM_REQUIREMENTS),
        "reasons": list(reasons),
        "artifact_sha256": {
            "source_bank": source_bank_sha256,
            "packet": packet_sha256,
            "linkage": linkage_sha256,
            "evidence": evidence_sha256,
            "result": None,
        },
        "human_baseline_status": HUMAN_BASELINE_NOT_RUN,
    }
    return _finalize_result_hash(payload)


def _validate_packet_and_linkage(
    packet: Any, linkage: Any
) -> Tuple[str, str, str, Dict[str, str]]:
    if type(packet) is not list or type(linkage) is not list:
        _fail("INVALID_PACKET_LINKAGE_SCHEMA")
    source_bank_sha256, expected_by_core = _frozen_bank_contract()
    packet_hash = _safe_jsonl_sha256(packet)
    linkage_hash = _safe_jsonl_sha256(linkage)
    if packet_hash is None or linkage_hash is None:
        _fail("INVALID_PACKET_LINKAGE_SCHEMA")
    if len(packet) != 40 or len(linkage) != 40:
        _fail("INVALID_PACKET_LINKAGE_COUNT")

    packet_ids: List[str] = []
    packet_strata: Dict[str, str] = {}
    for row in packet:
        if type(row) is not dict or set(row) != _PACKET_FIELDS:
            _fail("INVALID_PACKET_SCHEMA")
        review_id = row["review_id"]
        stratum_id = row["stratum_id"]
        if not _canonical_identifier(review_id) or not _canonical_identifier(
            stratum_id
        ):
            _fail("INVALID_PACKET_IDENTIFIER")
        if (
            _REVIEW_ID_RE.fullmatch(review_id) is None
            or _STRATUM_ID_RE.fullmatch(stratum_id) is None
        ):
            _fail("INVALID_PACKET_IDENTIFIER")
        if review_id in packet_strata:
            _fail("DUPLICATE_PACKET_REVIEW_ID")
        if row["domain"] not in DOMAINS:
            _fail("INVALID_PACKET_SURFACE")
        if not _canonical_identifier(row["scenario"]) or not _canonical_identifier(
            row["principal_mandate"]
        ):
            _fail("INVALID_PACKET_SURFACE")
        window = row["magnitude_window_usd"]
        if (
            type(window) is not list
            or len(window) != 4
            or any(
                type(value) not in (int, float)
                or isinstance(value, bool)
                or float(value) <= 0.0
                for value in window
            )
            or any(float(window[index]) >= float(window[index + 1]) for index in range(3))
        ):
            _fail("INVALID_PACKET_MAGNITUDE_WINDOW")
        rating_form = row["rating_form"]
        if (
            type(rating_form) is not dict
            or set(rating_form) != set(RATING_FIELDS)
            or any(value is not None for value in rating_form.values())
        ):
            _fail("PREFILLED_OR_INVALID_RATING_FORM")
        packet_ids.append(review_id)
        packet_strata[review_id] = stratum_id

    packet_stratum_counts = Counter(packet_strata.values())
    if len(packet_stratum_counts) != 5 or set(packet_stratum_counts.values()) != {8}:
        _fail("INVALID_PACKET_STRATIFICATION")

    linkage_ids: List[str] = []
    core_ids = set()
    family_counts = Counter()
    source_hashes = set()
    stratum_families: Dict[str, set] = defaultdict(set)
    family_strata: Dict[str, set] = defaultdict(set)
    core_families: Dict[str, str] = {}
    for index, row in enumerate(linkage):
        if type(row) is not dict or set(row) != _LINKAGE_FIELDS:
            _fail("INVALID_LINKAGE_SCHEMA")
        review_id = row["review_id"]
        stratum_id = row["stratum_id"]
        core_id = row["core_id"]
        family = row["family"]
        if not all(
            _canonical_identifier(value)
            for value in (review_id, stratum_id, core_id)
        ):
            _fail("INVALID_LINKAGE_IDENTIFIER")
        if (
            _REVIEW_ID_RE.fullmatch(review_id) is None
            or _STRATUM_ID_RE.fullmatch(stratum_id) is None
        ):
            _fail("INVALID_LINKAGE_IDENTIFIER")
        if review_id in core_families or core_id in core_ids:
            _fail("DUPLICATE_LINKAGE_IDENTIFIER")
        if index >= len(packet_ids) or review_id != packet_ids[index]:
            _fail("PACKET_LINKAGE_ORDER_MISMATCH")
        if packet_strata.get(review_id) != stratum_id:
            _fail("PACKET_LINKAGE_STRATUM_MISMATCH")
        if family not in FAMILIES or row["family_code"] != FAMILY_CODES[family]:
            _fail("INVALID_LINKAGE_FAMILY")
        if tuple(packet[index]["magnitude_window_usd"]) != tuple(
            MAGNITUDE_WINDOWS[family]
        ):
            _fail("PACKET_LINKAGE_WINDOW_MISMATCH")
        logical_ids = row["primary_logical_record_ids"]
        if (
            type(logical_ids) is not list
            or len(logical_ids) != 4
            or len(set(logical_ids)) != 4
            or not all(_canonical_identifier(value) for value in logical_ids)
        ):
            _fail("INVALID_LINKAGE_PRIMARY_RECORDS")
        hashes = row["public_record_sha256_by_tier"]
        if (
            type(hashes) is not dict
            or set(hashes) != _TIER_KEYS
            or not all(_valid_sha256(value) for value in hashes.values())
        ):
            _fail("INVALID_LINKAGE_RECORD_HASHES")
        source_hash = row["source_bank_sha256"]
        if not _valid_sha256(source_hash):
            _fail("INVALID_LINKAGE_SOURCE_HASH")
        expected = expected_by_core.get(core_id)
        if expected is None:
            _fail("FROZEN_BANK_BINDING_MISMATCH")
        if (
            source_hash != source_bank_sha256
            or family != expected["family"]
            or row["family_code"] != expected["family_code"]
            or tuple(logical_ids) != expected["primary_logical_record_ids"]
            or hashes != expected["public_record_sha256_by_tier"]
            or packet[index]["domain"] != expected["domain"]
            or packet[index]["scenario"] != expected["scenario"]
            or packet[index]["principal_mandate"]
            != expected["principal_mandate"]
            or tuple(packet[index]["magnitude_window_usd"])
            != expected["magnitude_window_usd"]
        ):
            _fail("FROZEN_BANK_BINDING_MISMATCH")
        source_hashes.add(source_hash)
        linkage_ids.append(review_id)
        core_ids.add(core_id)
        core_families[review_id] = family
        family_counts[family] += 1
        stratum_families[stratum_id].add(family)
        family_strata[family].add(stratum_id)

    if linkage_ids != packet_ids:
        _fail("PACKET_LINKAGE_ORDER_MISMATCH")
    if family_counts != Counter({family: 8 for family in FAMILIES}):
        _fail("INVALID_LINKAGE_FAMILY_COUNTS")
    if len(source_hashes) != 1:
        _fail("INCONSISTENT_LINKAGE_SOURCE_HASH")
    if any(len(values) != 1 for values in stratum_families.values()) or any(
        len(values) != 1 for values in family_strata.values()
    ):
        _fail("INVALID_LINKAGE_STRATIFICATION")
    return packet_hash, linkage_hash, source_bank_sha256, core_families


def _validate_panel(panel: Any) -> Tuple[List[Dict[str, Any]], Tuple[str, ...]]:
    if type(panel) is not list or len(panel) != 3:
        _fail("INVALID_PROFESSIONAL_PANEL")
    projected = []
    rater_ids = []
    procurement_covered = False
    finance_covered = False
    for row in panel:
        if type(row) is not dict or set(row) != _PANEL_FIELDS:
            _fail("INVALID_PROFESSIONAL_PANEL")
        rater_id = row["rater_id"]
        qualification = row["qualification"]
        qualification_evidence = row["qualification_evidence"]
        if (
            not _canonical_identifier(rater_id)
            or qualification not in _PROFESSIONAL_QUALIFICATIONS
            or not _canonical_identifier(qualification_evidence)
            or _has_prohibited_evidence_marker(qualification_evidence)
            or type(row["covers_procurement"]) is not bool
            or type(row["covers_finance"]) is not bool
            or row["synthetic"] is not False
        ):
            _fail("INVALID_PROFESSIONAL_PANEL")
        coverage = (row["covers_procurement"], row["covers_finance"])
        if coverage != _PROFESSIONAL_QUALIFICATIONS[qualification]:
            _fail("INVALID_PROFESSIONAL_PANEL")
        rater_ids.append(rater_id)
        procurement_covered = procurement_covered or coverage[0]
        finance_covered = finance_covered or coverage[1]
        projected.append(
            {
                "rater_id": rater_id,
                "qualification": qualification,
                "covers_procurement": coverage[0],
                "covers_finance": coverage[1],
                "synthetic": False,
            }
        )
    if (
        len(set(rater_ids)) != 3
        or not procurement_covered
        or not finance_covered
    ):
        _fail("INVALID_PROFESSIONAL_PANEL")
    return projected, tuple(rater_ids)


def _validate_ratings(
    ratings: Any,
    review_ids: Sequence[str],
    rater_ids: Sequence[str],
) -> Tuple[List[Dict[str, Any]], Dict[str, List[Dict[str, Any]]]]:
    if type(ratings) is not list or len(ratings) != 80:
        _fail("INVALID_RATING_COUNT")
    expected_reviews = set(review_ids)
    expected_raters = set(rater_ids)
    seen_assignments = set()
    by_review: Dict[str, List[Dict[str, Any]]] = {
        review_id: [] for review_id in review_ids
    }
    projected = []
    used_raters = set()
    for row in ratings:
        if type(row) is not dict or set(row) != _RATING_RECORD_FIELDS:
            _fail("INVALID_RATING_RECORD")
        review_id = row["review_id"]
        rater_id = row["rater_id"]
        assignment = (review_id, rater_id)
        if (
            not _canonical_identifier(review_id)
            or not _canonical_identifier(rater_id)
            or review_id not in expected_reviews
            or rater_id not in expected_raters
            or assignment in seen_assignments
            or row["independent_submission"] is not True
            or any(type(row[field]) is not bool for field in BINARY_FIELDS)
            or any(not _valid_ordinal(row[field]) for field in ORDINAL_FIELDS)
        ):
            _fail("INVALID_RATING_RECORD")
        seen_assignments.add(assignment)
        used_raters.add(rater_id)
        by_review[review_id].append(row)
        projected.append(
            {
                "core_id": review_id,
                "rater_id": rater_id,
                "scenario_realism": row["scenario_realism"],
                "magnitude_window_plausibility": row[
                    "magnitude_window_plausibility"
                ],
            }
        )
    if any(
        len(rows) != 2 or len({row["rater_id"] for row in rows}) != 2
        for rows in by_review.values()
    ):
        _fail("INCOMPLETE_CORE_ASSIGNMENT")
    if used_raters != expected_raters:
        _fail("UNUSED_PANEL_RATER")
    return projected, by_review


def _valid_resolution(value: Any) -> bool:
    return (
        type(value) is dict
        and set(value) == set(RATING_FIELDS)
        and all(type(value[field]) is bool for field in BINARY_FIELDS)
        and all(_valid_ordinal(value[field]) for field in ORDINAL_FIELDS)
    )


def _validate_adjudications(
    adjudications: Any,
    by_review: Mapping[str, Sequence[Mapping[str, Any]]],
    rater_ids: Sequence[str],
) -> None:
    if type(adjudications) is not list:
        _fail("INVALID_ADJUDICATION")
    expected: Dict[str, List[str]] = {}
    for review_id, rows in by_review.items():
        differing = sorted(
            field for field in RATING_FIELDS if rows[0][field] != rows[1][field]
        )
        if differing:
            expected[review_id] = differing
    if len(adjudications) != len(expected):
        _fail("UNADJUDICATED_DISAGREEMENT")
    seen = set()
    all_raters = set(rater_ids)
    for row in adjudications:
        if type(row) is not dict or set(row) != _ADJUDICATION_FIELDS:
            _fail("INVALID_ADJUDICATION")
        review_id = row["review_id"]
        if review_id in seen or review_id not in expected:
            _fail("INVALID_ADJUDICATION")
        seen.add(review_id)
        assigned = {rating["rater_id"] for rating in by_review[review_id]}
        third = all_raters - assigned
        if (
            len(third) != 1
            or row["adjudicator_id"] not in third
            or type(row["disagreement_fields"]) is not list
            or row["disagreement_fields"] != expected[review_id]
            or not _valid_resolution(row["resolution"])
            or not _canonical_identifier(row["reason"])
        ):
            _fail("INVALID_ADJUDICATION")
    if seen != set(expected):
        _fail("UNADJUDICATED_DISAGREEMENT")


def _validate_revision_history(value: Any) -> None:
    if type(value) is not list or len(value) > 1:
        _fail("INVALID_REVISION_HISTORY")
    if not value:
        return
    revision = value[0]
    if (
        type(revision) is not dict
        or set(revision) != set(REVISION_HISTORY_FIELDS)
        or type(revision["round"]) is not int
        or revision["round"] != 1
        or revision["completed_before_model_data"] is not True
        or not _canonical_identifier(revision["reason"])
    ):
        _fail("INVALID_REVISION_HISTORY")


def _validate_evidence(
    evidence: Any,
    packet_hash: str,
    linkage_hash: str,
    core_families: Mapping[str, str],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Any], int]:
    _scan_evidence_provenance(evidence)
    if type(evidence) is not dict or set(evidence) != _EVIDENCE_FIELDS:
        _fail("INVALID_EVIDENCE_SCHEMA")
    if (
        type(evidence["schema_version"]) is not int
        or evidence["schema_version"] != 1
        or evidence["instrument"] != INSTRUMENT
        or evidence["data_basis"] != "direct_professional_human_ratings"
        or evidence["packet_sha256"] != packet_hash
        or evidence["linkage_sha256"] != linkage_hash
    ):
        _fail("INVALID_EVIDENCE_BINDING")
    panel, rater_ids = _validate_panel(evidence["panel"])
    ratings, by_review = _validate_ratings(
        evidence["ratings"], tuple(core_families), rater_ids
    )
    _validate_adjudications(evidence["adjudications"], by_review, rater_ids)
    _validate_revision_history(evidence["revision_history"])
    return panel, ratings, evidence["revision_history"], len(
        evidence["adjudications"]
    )


def evaluate_realism_gate(packet, linkage, evidence):
    """Evaluate only complete, raw professional evidence; fail closed otherwise."""

    packet_hash = _safe_jsonl_sha256(packet)
    linkage_hash = _safe_jsonl_sha256(linkage)
    evidence_hash = _safe_canonical_sha256(evidence) if evidence is not None else None
    source_bank_hash = _safe_frozen_source_sha256()
    try:
        (
            packet_hash,
            linkage_hash,
            source_bank_hash,
            core_families,
        ) = _validate_packet_and_linkage(packet, linkage)
        if evidence is None:
            return _result(
                status=NOT_RUN_STATUS,
                packet_sha256=packet_hash,
                linkage_sha256=linkage_hash,
                evidence_sha256=None,
                source_bank_sha256=source_bank_hash,
                reasons=("NO_PROFESSIONAL_EVIDENCE",),
            )
        panel, ratings, revision_history, adjudication_count = _validate_evidence(
            evidence, packet_hash, linkage_hash, core_families
        )
        evaluated = evaluate_professional_realism(
            core_families, panel, ratings, revision_history
        )
        status = "PASS" if evaluated.status == "PASS" else "FAIL"
        reasons = list(evaluated.reasons)
        if evaluated.status == "NOT_ESTIMABLE" and not reasons:
            reasons = ["FLEISS_KAPPA_NOT_ESTIMABLE"]
        elif status == "FAIL" and not reasons:
            reasons = ["REALISM_GATE_NOT_MET"]
        return _result(
            status=status,
            packet_sha256=packet_hash,
            linkage_sha256=linkage_hash,
            evidence_sha256=evidence_hash,
            source_bank_sha256=source_bank_hash,
            data_basis=evidence["data_basis"],
            counts={
                "cores": 40,
                "families": 5,
                "professionals": len(panel),
                "ratings": len(ratings),
                "adjudications": adjudication_count,
            },
            family_passing_cores=evaluated.family_passing_cores,
            fleiss_kappa=evaluated.fleiss_kappa,
            reasons=reasons,
        )
    except MemoryError:
        raise
    except _GateValidationError as exc:
        return _result(
            status="FAIL",
            packet_sha256=packet_hash,
            linkage_sha256=linkage_hash,
            evidence_sha256=evidence_hash,
            source_bank_sha256=source_bank_hash,
            data_basis=_reported_data_basis(evidence),
            reasons=(exc.code,),
        )
    except Exception as exc:
        return _result(
            status="FAIL",
            packet_sha256=packet_hash,
            linkage_sha256=linkage_hash,
            evidence_sha256=evidence_hash,
            source_bank_sha256=source_bank_hash,
            data_basis=_reported_data_basis(evidence),
            reasons=("REALISM_GATE_ERROR:%s" % type(exc).__name__,),
        )


def human_baseline_contract() -> Dict[str, Any]:
    """Return a prospective schema-only contract, never fabricated responses."""

    sha_schema = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
    terminal_action = {
        "type": "object",
        "additionalProperties": False,
        "required": ["kind", "tool", "arguments"],
        "properties": {
            "kind": {"const": "act"},
            "tool": {"type": "string", "minLength": 1},
            "arguments": {"type": "object"},
        },
        "x-skim-schema-source": "public.requests[].response_schema",
    }
    return {
        "schema_version": 1,
        "instrument": "SKIM-P1-HUMAN-BASELINE",
        "status": HUMAN_BASELINE_NOT_RUN,
        "eligible_for_empirical_decision": False,
        "data_basis_required": "live_human_same_harness",
        "response_schema": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "participant_id",
                "runtime_request_id",
                "request_template_sha256",
                "terminal_action",
                "event_chain_head_sha256",
                "data_basis",
                "synthetic",
            ],
            "properties": {
                "participant_id": {"type": "string", "minLength": 1},
                "runtime_request_id": {"type": "string", "minLength": 1},
                "request_template_sha256": dict(sha_schema),
                "terminal_action": terminal_action,
                "event_chain_head_sha256": dict(sha_schema),
                "data_basis": {"const": "live_human_same_harness"},
                "synthetic": {"const": False},
            },
        },
        "analysis_command": (
            "python analysis/make_report.py --mode human-baseline "
            "--runtime-manifest itembank/runtime/p1-runtime-manifest.jsonl "
            "--responses private/human-baseline-responses.jsonl "
            "--output pilots/human-baseline"
        ),
    }


def _parse_canonical_jsonl_bytes(data: bytes, label: str) -> List[Dict[str, Any]]:
    if type(data) is not bytes or not data or not data.endswith(b"\n"):
        raise ValueError("%s must be nonempty canonical JSONL" % label)
    raw_lines = data[:-1].split(b"\n")
    if any(not line for line in raw_lines):
        raise ValueError("%s contains an empty JSONL row" % label)
    rows = []
    for raw_line in raw_lines:
        row = json.loads(raw_line.decode("utf-8"))
        if type(row) is not dict:
            raise ValueError("%s rows must be exact JSON objects" % label)
        if canonical_json(row).encode("utf-8") != raw_line:
            raise ValueError("%s is not canonical JSONL" % label)
        rows.append(row)
    return rows


def _parse_canonical_json_bytes(data: bytes, label: str) -> Dict[str, Any]:
    if type(data) is not bytes or not data or not data.endswith(b"\n"):
        raise ValueError("%s must be canonical JSON plus one LF" % label)
    value = json.loads(data.decode("utf-8"))
    if type(value) is not dict:
        raise ValueError("%s root must be an exact JSON object" % label)
    if canonical_json(value).encode("utf-8") + b"\n" != data:
        raise ValueError("%s is not canonical JSON plus one LF" % label)
    return value


def _assert_distinct_paths(paths: Sequence[Path]) -> None:
    resolved = [Path(path).resolve() for path in paths]
    if len(set(resolved)) != len(resolved):
        raise ValueError("packet, linkage, input, and result paths must be distinct")
    for left_index, left in enumerate(paths):
        for right in paths[left_index + 1 :]:
            try:
                if os.path.samefile(left, right):
                    raise ValueError(
                        "packet, linkage, input, and result paths must be distinct"
                    )
            except FileNotFoundError:
                continue


def _write_result_atomic(path: Path, payload: Mapping[str, Any]) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary: Optional[Path] = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=str(destination.parent),
            prefix=".%s." % destination.name,
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(canonical_json(payload) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(str(temporary), str(destination))
    except BaseException:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
        raise


def _bind_cli_artifact_hashes(
    result: Dict[str, Any],
    packet_bytes: bytes,
    linkage_bytes: bytes,
    evidence_bytes: Optional[bytes],
) -> Dict[str, Any]:
    """Bind a parsed CLI result to the exact accepted bytes, including LF."""

    packet_hash = hashlib.sha256(packet_bytes).hexdigest()
    linkage_hash = hashlib.sha256(linkage_bytes).hexdigest()
    artifacts = result["artifact_sha256"]
    if artifacts["packet"] != packet_hash or artifacts["linkage"] != linkage_hash:
        return _result(
            status="FAIL",
            source_bank_sha256=artifacts.get("source_bank"),
            packet_sha256=packet_hash,
            linkage_sha256=linkage_hash,
            evidence_sha256=(
                hashlib.sha256(evidence_bytes).hexdigest()
                if evidence_bytes is not None
                else None
            ),
            reasons=("CLI_ARTIFACT_HASH_MISMATCH",),
        )
    artifacts["packet"] = packet_hash
    artifacts["linkage"] = linkage_hash
    artifacts["evidence"] = (
        hashlib.sha256(evidence_bytes).hexdigest()
        if evidence_bytes is not None
        else None
    )
    return _finalize_result_hash(result)


def _write_cli_result(args: argparse.Namespace, payload: Mapping[str, Any]) -> None:
    _assert_distinct_paths(
        (args.packet, args.linkage, args.input, args.result)
    )
    _write_result_atomic(args.result, payload)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--linkage", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--result", type=Path, required=True)
    args = parser.parse_args(argv)
    _assert_distinct_paths(
        (args.packet, args.linkage, args.input, args.result)
    )

    packet_bytes: Optional[bytes] = None
    linkage_bytes: Optional[bytes] = None
    try:
        packet_bytes = args.packet.read_bytes()
        linkage_bytes = args.linkage.read_bytes()
        packet = _parse_canonical_jsonl_bytes(packet_bytes, str(args.packet))
        linkage = _parse_canonical_jsonl_bytes(
            linkage_bytes, str(args.linkage)
        )
    except MemoryError:
        raise
    except Exception as exc:
        result = _result(
            status="FAIL",
            source_bank_sha256=_safe_frozen_source_sha256(),
            packet_sha256=(
                hashlib.sha256(packet_bytes).hexdigest()
                if packet_bytes is not None
                else None
            ),
            linkage_sha256=(
                hashlib.sha256(linkage_bytes).hexdigest()
                if linkage_bytes is not None
                else None
            ),
            evidence_sha256=None,
            reasons=("INVALID_PACKET_INPUT:%s" % type(exc).__name__,),
        )
        _write_cli_result(args, result)
        return 1

    evidence_bytes: Optional[bytes] = None
    try:
        evidence_bytes = args.input.read_bytes()
    except FileNotFoundError:
        evidence = None
    except MemoryError:
        raise
    except Exception as exc:
        result = _result(
            status="FAIL",
            source_bank_sha256=_safe_frozen_source_sha256(),
            packet_sha256=canonical_jsonl_sha256(packet),
            linkage_sha256=canonical_jsonl_sha256(linkage),
            evidence_sha256=None,
            reasons=("INVALID_EVIDENCE_INPUT:%s" % type(exc).__name__,),
        )
        result = _bind_cli_artifact_hashes(
            result, packet_bytes, linkage_bytes, None
        )
        _write_cli_result(args, result)
        return 1
    else:
        try:
            evidence = _parse_canonical_json_bytes(
                evidence_bytes, str(args.input)
            )
        except MemoryError:
            raise
        except Exception as exc:
            result = _result(
                status="FAIL",
                source_bank_sha256=_safe_frozen_source_sha256(),
                packet_sha256=canonical_jsonl_sha256(packet),
                linkage_sha256=canonical_jsonl_sha256(linkage),
                evidence_sha256=hashlib.sha256(evidence_bytes).hexdigest(),
                reasons=("INVALID_EVIDENCE_INPUT:%s" % type(exc).__name__,),
            )
            result = _bind_cli_artifact_hashes(
                result, packet_bytes, linkage_bytes, evidence_bytes
            )
            _write_cli_result(args, result)
            return 1

    result = evaluate_realism_gate(packet, linkage, evidence)
    result = _bind_cli_artifact_hashes(
        result, packet_bytes, linkage_bytes, evidence_bytes
    )
    _write_cli_result(args, result)
    return 0 if result["status"] == "PASS" else 1


__all__ = [
    "BINARY_FIELDS",
    "ORDINAL_FIELDS",
    "RATING_FIELDS",
    "evaluate_realism_gate",
    "human_baseline_contract",
    "main",
]


if __name__ == "__main__":
    raise SystemExit(main())
