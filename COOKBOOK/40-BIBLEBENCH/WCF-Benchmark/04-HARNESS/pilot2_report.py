#!/usr/bin/env python3
"""Empirical-data gate and neutral report payload for the Pilot 2 supplement."""

from __future__ import annotations

from typing import Any, Dict, Mapping, Sequence

import pilot2_preflight as preflight


class ReportError(RuntimeError):
    """A Pilot 2 supplement cannot be emitted from the supplied evidence."""


def build_supplement_payload(
    manifest: Mapping[str, Any], rows: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    if not rows:
        raise ReportError("empirical results are required; no empty supplement")
    if manifest.get("validity_label") != preflight.VALIDITY_LABEL:
        raise ReportError("manifest validity label is not Pilot 2")
    keyed = {row.get("sut"): dict(row) for row in rows}
    if set(keyed) != set(preflight.SUTS) or len(rows) != len(preflight.SUTS):
        raise ReportError("empirical results must cover each exact SUT once")
    ordered = []
    for slug in preflight.SUTS:
        row = keyed[slug]
        numeric = row.get("numeric_scores")
        if not isinstance(numeric, int) or isinstance(numeric, bool) \
                or not 0 <= numeric <= 222:
            raise ReportError(f"invalid scalar coverage: {slug}")
        row["coverage_status"] = (
            "SUFFICIENT_DESCRIPTIVE" if numeric >= 200 else "INCOMPLETE")
        if numeric < 200:
            row["scalar_mean"] = None
        ordered.append(row)
    return {
        "validity_label": preflight.VALIDITY_LABEL,
        "presentation_order": "FROZEN_ROSTER_NOT_SCORE_ORDER",
        "per_sut": ordered,
        "separate_surfaces": [
            "matter", "manner", "end", "refusal", "contested",
            "coverage", "errors", "diagnostic_dev_set"],
        "claims": {
            "ranking": False,
            "reasoning_effect": False,
            "release": False,
            "universal_score": False,
            "paper_replacement": False,
        },
    }


def main() -> int:
    print("Pilot 2 supplement generation is blocked until empirical evidence exists.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
