#!/usr/bin/env python3
"""Fixture-only Pilot 2 Codex-OAuth canary contract; never invokes OAuth on import."""

from __future__ import annotations

from typing import Any, Callable, Dict, Mapping, Sequence

import pilot2_run as controller


ROUTE_COUNTS = (("open", 8), ("contested", 4), ("episode", 4))


class CanaryError(RuntimeError):
    """The registered 16-record zero-dollar judge canary failed."""


def build_fixture_records() -> list:
    """Create synthetic, non-bank judge records with exact route geometry."""
    records = []
    index = 0
    for route, count in ROUTE_COUNTS:
        for _ in range(count):
            index += 1
            response = "Synthetic non-bank answer for mechanical schema validation."
            if index == 1:
                response = "N" * 250_000
            records.append({
                "record_id": f"pilot2-canary-{index:02d}",
                "sut": "pilot2-synthetic-canary",
                "route": route,
                "payload": {
                    "criterion_id": f"FIXTURE-{route.upper()}-{index:02d}",
                    "response": response,
                },
            })
    return records


def run_fixture_canary(
    judge_batch: Callable[[Sequence[Mapping[str, Any]]], Mapping[str, Any]],
) -> Dict[str, Any]:
    """Run injected OAuth judging sequentially; the caller owns live authorization."""
    records = build_fixture_records()
    all_batches = []
    missing = []
    for route, _count in ROUTE_COUNTS:
        route_records = [row for row in records if row["route"] == route]
        batches, oversized = controller.build_dynamic_judge_batches(route_records)
        if oversized:
            raise CanaryError("registered near-ceiling record exceeded byte contract")
        all_batches.extend(batches)
    returned = []
    for batch in all_batches:  # concurrency one by construction
        result = judge_batch(batch)
        rows = result.get("records") if isinstance(result, Mapping) else None
        unresolved = result.get("missing_record_ids") if isinstance(result, Mapping) else None
        if not isinstance(rows, list) or unresolved:
            raise CanaryError("OAuth canary lost or malformed records")
        returned.extend(rows)
    expected = {row["record_id"] for row in records}
    observed = [row.get("record_id") for row in returned if isinstance(row, Mapping)]
    if len(observed) != 16 or set(observed) != expected or len(set(observed)) != 16:
        raise CanaryError("OAuth canary did not return 16 unique registered IDs")
    return {"status": "PASS", "records": 16, "batches": len(all_batches)}


def main() -> int:
    print("Pilot 2 OAuth canary requires separate authorization and an injected judge.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
