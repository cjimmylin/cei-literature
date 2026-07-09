#!/usr/bin/env python3
"""WCF-Bench harness dry-run — mock-first, NO network.

Loads the YAML fixtures, runs each through a MockModelClient (canned responses),
applies the appropriate mechanical scorer (AGGRAVATE ordinal or PROOFTEXT
anchors), and prints a small per-item score report.

    /Users/.../.venv/bin/python run_dryrun.py

Every number printed is a MOCK result on canned responses — it is NOT a
measurement of any model (build-plan Phase 2 exit note). No API keys, no sockets.
"""

from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from wcfbench import (  # noqa: E402
    MockModelClient,
    load_items,
    score_aggravate_ordinal,
    score_prooftext_anchors,
)
from wcfbench.scorers import INCOMPARABLE  # noqa: E402

FIXTURES_DIR = os.path.join(HERE, "fixtures")


def _canned_responses():
    """Deterministic mock responses exercising each scorer path.

    One 'good' response per item that scores well, to show the happy path.
    (test_harness.py exercises the wrong/declined/non-citing paths.)
    """
    return {
        # AGG-C6-W301 — orderable, gold a<b<c. Good response gives the right order.
        "AGG-C6-W301": {
            "ranking": ["a", "b", "c"],
            "text": (
                "Least to most heinous: a < b < c. The rival (a) carries the "
                "highest material stakes yet ranks lowest — stakes are not a "
                "Q151 head. (b) > (a) on the especially-related clause (H2). "
                "(c) > (b) on office (H1, example followed) plus souls-under-charge (H2)."
            ),
        },
        # AGG-C5-W304 — incomparable. Good response DECLINES a total order.
        "AGG-C5-W304": {
            "ranking": INCOMPARABLE,
            "text": (
                "The Q151 calculus does not yield a confident ordering: one "
                "eyes-open willful refusal vs three years of continuance are "
                "incommensurable. I decline a total order and profile each."
            ),
        },
        # PROOF-C8-W302 — anchor matching. Good response cites Q141, Q142, WCF 1.9
        # and the required counter-texts.
        "PROOF-C8-W302": {
            "text": (
                "The verse actually says 'the LOVE of money is the root of all "
                "evil' (1 Tim 6:10) — an affection, not the thing. Compare "
                "1 Tim 6:17-18 and 1 Tim 5:8 (provide for your household). "
                "WLC Q141 makes a lawful calling, frugality, and providing for "
                "others duties (see WCF 1.9, Scripture interprets Scripture); "
                "WLC Q142 names covetousness as the real sin. You are free and "
                "dutiful to provide and steward."
            ),
        },
    }


# Counter-text requirement for the PROOFTEXT counter-texts keypoint (mirrors the
# rubric's ">=2 of ..." — we require at least these two tokens to appear).
PROOFTEXT_COUNTER_TOKENS = {
    "counter-texts supplied": ["1 Tim 6:17-18", "1 Tim 5:8"],
}


def main() -> int:
    print("=" * 72)
    print("WCF-Bench harness dry-run (MOCK — not a measurement)")
    print("=" * 72)

    items = load_items(FIXTURES_DIR)
    print(f"Loaded {len(items)} item record(s) from {os.path.relpath(FIXTURES_DIR, HERE)}/\n")

    client = MockModelClient()
    canned = _canned_responses()
    for item_id, resp in canned.items():
        client.register(item_id, resp["text"])

    total_awarded = 0.0
    total_max = 0.0

    for item in items:
        resp = canned.get(item.id, {})
        model_text = client.complete(prompt=item.stem, item_id=item.id)
        print(f"[{item.id}]  design={item.design}  track={item.track}  tier={item.tier}")

        if item.design == "aggravate":
            gold = item.extra.get("gold_order")
            ordering_max = item.rubric[0].points  # first keypoint = ordering
            score = score_aggravate_ordinal(
                gold_key=gold,
                model_ranking=resp.get("ranking"),
                ordering_max=ordering_max,
            )
            awarded, mx = score.ordering_points, score.ordering_max
            print(f"    ordinal scorer: {score.detail}")
            print(f"    ordering credit: {awarded:.2f} / {mx:.2f}")

        elif item.design == "prooftext":
            score = score_prooftext_anchors(
                rubric=item.rubric,
                model_response=model_text,
                counter_tokens=PROOFTEXT_COUNTER_TOKENS,
            )
            awarded, mx = score.points, score.max_points
            print(f"    anchor scorer: {score.detail}")
            print(f"    anchored credit: {awarded:.2f} / {mx:.2f}  (matched: {len(score.matched)})")

        else:
            print(f"    (no mechanical scorer for design={item.design!r} in this skeleton)")
            awarded = mx = 0.0

        total_awarded += awarded
        total_max += mx
        print()

    print("-" * 72)
    print(f"SUMMARY (mock): {total_awarded:.2f} / {total_max:.2f} mechanical points "
          f"across {len(items)} items")
    print(f"API calls made: 0 (MockModelClient; {len(client.call_log)} canned .complete() lookups)")
    print("-" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
