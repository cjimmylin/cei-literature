"""FR-16(c) bounded offline re-parse for design-05 structural pendings.

Only 05 records that are pending, allocation-invalid, and have no real two-judge
disagreement enter this path. The input records are never mutated. One exact-label
recovery pass either produces a complete budget-valid allocation or marks the atomic
`allocation_parse` cell for human Part B; it never invokes a model or infers a value.
"""
from __future__ import annotations

from copy import deepcopy

from .parsers import reparse_allocation_response
from .refusal import tag_response


def _selected(rec: dict) -> bool:
    return (
        rec.get("design") == "05-ordoamoris"
        and rec.get("refusal_tag") == "pending_adjudication"
        and not (rec.get("allocation") or {}).get("ok")
        and not ((rec.get("judge_report") or {}).get("disagreements") or [])
    )


def _response(rec: dict) -> tuple:
    administrations = rec.get("administrations") or []
    admin = administrations[0] if administrations else {}
    return admin.get("label") or "main", (
        admin.get("response") or admin.get("terminal_response")
        or admin.get("terminal") or ""
    )


def reparse_records(records: list, items_by_id: dict) -> tuple:
    """Return `(deep-copied records, counts)` after the single permitted pass."""
    out = deepcopy(records)
    counts = {"selected": 0, "recovered": 0, "failed": 0}
    for rec in out:
        if not _selected(rec):
            continue
        counts["selected"] += 1
        item = items_by_id[rec["item_id"]]
        spec = (item.extras or {}).get("allocation") or {}
        label, response = _response(rec)
        parsed = reparse_allocation_response(
            response, list(spec.get("tokens") or []), float(spec.get("budget") or 0.0))
        rec["allocation_reparse"] = {
            "method": "bounded-offline-exact-label-v1",
            "passes": 1,
            "live_calls": 0,
            "status": "recovered" if parsed.ok else "failed",
        }
        rec["allocation_reparse_failed"] = not parsed.ok
        if not parsed.ok:
            counts["failed"] += 1
            continue

        counts["recovered"] += 1
        old_attempts = (rec.get("allocation") or {}).get("attempts")
        rec["allocation"] = {
            "ok": True,
            "values": parsed.values,
            "total": parsed.total,
            "sum_ok": parsed.sum_ok,
            "tokens_missing": parsed.tokens_missing,
            "non_compliant": False,
            "attempts": old_attempts,
        }
        # Reproduce score_item's judge-free design-05 bookkeeping mechanically.
        rec["keyed_outcome"] = "faithful"
        rec["scalar_adjudicated"] = 1.0
        rec["scalar_goodness"] = 1.0
        rt = tag_response(response, item, engaged=True, keyed_outcome="faithful")
        rec["refusal_tag"] = rt.tag
        rec.setdefault("refusal_tags", {})[label] = rt.tag
        rec.setdefault("refusal_reason", {})[label] = rt.refusal_reason
        rec.setdefault("refusal_lexical", {})[label] = rt.lexical
        rec.setdefault("lexical_refusal_override", {})[label] = rt.lexical_override
    return out, counts
