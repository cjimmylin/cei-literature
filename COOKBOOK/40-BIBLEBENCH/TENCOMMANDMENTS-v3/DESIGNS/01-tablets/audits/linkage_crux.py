"""Parent/treatment linkage and CRUX-boundary audit for TABLETS P1."""

from collections import Counter
import hashlib
import json
from pathlib import Path

from audits.schema_balance import TABLETS_ROOT, parse_jsonl_bytes, read_artifact_bytes
from itembank.generator import build_rows
from tablets_schemas import validate_public_row


_CRUX_MEMO_NAME = "20260706-tablets-crux-coregistration.md"
_CRUX_MEMO_PATH = (
    TABLETS_ROOT.parents[2] / "TENCOMMANDMENTS-REVIEWS" / _CRUX_MEMO_NAME
)
_EXPECTED_MEMO_SHA256 = (
    "ac591d17dbd18935e32f3c80ef011d0a1418e875ceb5f35c80cee194e3ff66d7"
)
_EXPECTED_LINKAGE = {
    "cross_instrument_triads_forbidden": True,
    "gold_source_tiebreaker": "casuistic-precedence gold",
    "instrument": "TABLETS",
    "objects_in_conflict": "two named Decalogue norms on one actor",
    "overlap_analysis_status": "NOT_RUN",
    "seed_sharing_forbidden": True,
    "source_memo": _CRUX_MEMO_NAME,
    "source_memo_sha256": _EXPECTED_MEMO_SHA256,
    "status": "BINDING",
}


def _load_inputs(tablets_root, public_rows, linkage, source_memo_bytes):
    injected = any(
        value is not None for value in (public_rows, linkage, source_memo_bytes)
    )
    root = TABLETS_ROOT if tablets_root is None else Path(tablets_root)
    if public_rows is None:
        artifacts, _ = read_artifact_bytes(tablets_root=root)
        public_rows = parse_jsonl_bytes(artifacts["public"], "public")
    if linkage is None:
        try:
            linkage = json.loads(
                (root / "crux-coregistration-linkage.json").read_text(
                    encoding="utf-8"
                )
            )
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError("CRUX linkage JSON is invalid") from error
    if source_memo_bytes is None:
        memo_path = (
            _CRUX_MEMO_PATH
            if tablets_root is None
            else root.parents[2] / "TENCOMMANDMENTS-REVIEWS" / _CRUX_MEMO_NAME
        )
        source_memo_bytes = memo_path.read_bytes()
    if type(public_rows) is not list or not all(
        type(row) is dict for row in public_rows
    ):
        raise ValueError("public row projection must be a list of objects")
    if type(linkage) is not dict or type(source_memo_bytes) is not bytes:
        raise ValueError("CRUX linkage inputs have invalid types")
    return public_rows, linkage, source_memo_bytes, (
        "INJECTED_ROWS" if injected else "DISK"
    )


def audit_linkage_crux(
    tablets_root=None,
    public_rows=None,
    linkage=None,
    source_memo_bytes=None,
):
    """Audit reciprocal parents, exact treatments, and the binding CRUX memo."""
    public, linkage, memo_bytes, source = _load_inputs(
        tablets_root, public_rows, linkage, source_memo_bytes
    )
    for row in public:
        validate_public_row(row)
    if len(public) != 636 or len({row["id"] for row in public}) != 636:
        raise ValueError("TABLETS linkage projection identity drift")
    by_id = {row["id"]: row for row in public}
    parents = [row for row in public if row["record_type"] == "adjudication"]
    children = [row for row in public if row["record_type"] != "adjudication"]
    reciprocal_links = 0
    for parent in parents:
        if parent["parent_id"] is not None:
            raise ValueError("adjudication parent graph drift")
        for child_id in parent["paired_record_ids"]:
            child = by_id.get(child_id)
            if child is None or child["parent_id"] != parent["id"]:
                raise ValueError("parent graph is not reciprocal")
    for child in children:
        parent = by_id.get(child["parent_id"])
        if (
            parent is None
            or parent["record_type"] != "adjudication"
            or parent["framing_arm"] != "neutral"
            or parent["monitoring_condition"] != "unmonitored"
        ):
            raise ValueError("child parent must be a neutral adjudication")
        if child["paired_record_ids"] != [parent["id"]]:
            raise ValueError("child parent link is not exact")
        if child["id"] not in parent["paired_record_ids"]:
            raise ValueError("parent graph is not reciprocal")
        reciprocal_links += 1
    if len(parents) != 342 or len(children) != 294 or reciprocal_links != 294:
        raise ValueError("TABLETS parent graph count drift")

    expected_public, _, _ = build_rows()
    expected_by_id = {row["id"]: row for row in expected_public}
    treatment_parent_ids = {
        child["parent_id"]
        for child in children
        if child["record_type"] in {"threat_twin", "monitoring_twin"}
    }
    for parent_id in sorted(treatment_parent_ids):
        if by_id[parent_id] != expected_by_id.get(parent_id):
            raise ValueError("treatment parent differs from frozen generator")
    treatment_counts = Counter()
    for child in children:
        record_type = child["record_type"]
        expected = expected_by_id.get(child["id"])
        if expected is None or child != expected:
            raise ValueError("%s treatment replay differs from frozen contract" % record_type)
        treatment_counts[record_type] += 1
    expected_treatments = {
        "threat_twin": 135,
        "monitoring_twin": 69,
        "comprehension": 45,
        "recognition": 45,
    }
    if dict(treatment_counts) != expected_treatments:
        raise ValueError("TABLETS treatment replay count drift")
    gs_parents = {
        row["parent_id"] for row in children if row["record_type"] == "threat_twin"
    }
    x3_parents = {
        row["parent_id"]
        for row in children
        if row["record_type"] == "monitoring_twin"
    }
    if not gs_parents.isdisjoint(x3_parents):
        raise ValueError("GS and X3 parent sets must be disjoint")

    if linkage != _EXPECTED_LINKAGE:
        raise ValueError("CRUX linkage frozen boundary or memo hash drift")
    memo_hash = hashlib.sha256(memo_bytes).hexdigest()
    if memo_hash != _EXPECTED_MEMO_SHA256:
        raise ValueError("CRUX source memo hash mismatch")
    return {
        "audit": "TABLETS_LINKAGE_CRUX",
        "schema_version": "tablets-structural-audit.v1",
        "status": "PASS",
        "source": source,
        "sections": {
            "parent_graph": {
                "status": "PASS",
                "parent_rows": 342,
                "child_rows": 294,
                "reciprocal_links": 294,
            },
            "treatment_replay": {
                "status": "PASS",
                "threat_twin": 135,
                "monitoring_twin": 69,
                "comprehension": 45,
                "recognition": 45,
                "gs_x3_parent_sets_disjoint": True,
            },
            "crux_boundary": {
                "status": "PASS",
                "instrument": linkage["instrument"],
                "objects_in_conflict": linkage["objects_in_conflict"],
                "gold_source_tiebreaker": linkage["gold_source_tiebreaker"],
                "seed_sharing_forbidden": True,
                "cross_instrument_triads_forbidden": True,
                "source_memo": _CRUX_MEMO_NAME,
                "source_memo_sha256": memo_hash,
                "cross_bank_seed_triad_audit_status": (
                    "NOT_RUN_CRUX_BANK_UNAVAILABLE"
                ),
            },
        },
    }


__all__ = ["audit_linkage_crux"]
