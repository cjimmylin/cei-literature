"""Replay reciprocal inherited-twin links and monitoring parent projections."""

from itembank.generator import build_rows
from palter_constants import MONITORING_NOTICE


def run_linkage_replay(public_rows=None):
    if public_rows is None:
        public_rows, _, _ = build_rows()
    findings = []
    by_id = {}
    for row in public_rows:
        if row.get("id") in by_id:
            findings.append("duplicate public row ID: %s" % row.get("id"))
        by_id[row.get("id")] = row
    undirected_edges = set()
    for row in public_rows:
        row_id = row.get("id")
        links = row.get("paired_record_ids")
        if type(links) is not list:
            findings.append("%s has no exact paired_record_ids list" % row_id)
            continue
        for linked_id in links:
            linked = by_id.get(linked_id)
            if linked is None:
                findings.append("%s references missing pair %s" % (row_id, linked_id))
                continue
            if row_id not in linked.get("paired_record_ids", []):
                findings.append("%s -> %s is not reciprocal" % (row_id, linked_id))
            undirected_edges.add(tuple(sorted((row_id, linked_id))))

    monitoring_replays = 0
    for row in public_rows:
        if row.get("record_type") != "monitoring_twin":
            continue
        parent = by_id.get(row.get("parent_id"))
        if parent is None or parent.get("record_type") != "composition":
            findings.append("%s lacks an unmonitored primary parent" % row.get("id"))
            continue
        for field in (
            "core_id",
            "pack_family",
            "incentive_tier",
            "direction",
            "source_atoms",
            "probes",
            "response_schema",
        ):
            if row.get(field) != parent.get(field):
                findings.append("%s differs from parent on %s" % (row.get("id"), field))
        if row.get("prompt") != parent.get("prompt", "") + MONITORING_NOTICE:
            findings.append("%s monitoring prompt is not the exact counterpart" % row.get("id"))
        if row.get("paired_record_ids") != [parent.get("id")]:
            findings.append("%s does not link only its exact parent" % row.get("id"))
        monitoring_replays += 1
    if monitoring_replays != 32:
        findings.append("monitoring parent replay count is not 32")
    return {
        "status": "PASS" if not findings else "FAIL",
        "row_count": len(public_rows),
        "reciprocal_link_edges": len(undirected_edges),
        "monitoring_parent_replays": monitoring_replays,
        "findings": findings,
    }


__all__ = ["run_linkage_replay"]
