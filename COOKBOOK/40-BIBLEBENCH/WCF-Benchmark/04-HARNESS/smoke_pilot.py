#!/usr/bin/env python3
"""Tiny REAL-token smoke pilot — proves the pipeline end-to-end on live model calls.

Loader -> CLIModelClient (claude CLI, subscription OAuth) -> judge-free scorers
(+ refusal taxonomy), on a couple of real fixtures. This is a PLUMBING check
(does the whole chain run on real responses?), NOT a measurement — the fixtures
are short paraphrases and the CLI path has no sampling control (see cli_client.py
caveats). Keep it small: individual-scale smoke use only.

SAFETY: makes NO calls unless you pass --go (real calls cost ~$0.02 each and use
your subscription quota). Without --go it prints the plan and exits.

    python smoke_pilot.py                 # dry: print plan, no calls
    python smoke_pilot.py --go            # make the real calls (haiku default)
    python smoke_pilot.py --go --model claude-sonnet-4-6
"""

from __future__ import annotations

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from wcfbench import (  # noqa: E402
    load_items, CLIModelClient, CLI_DEFAULT_MODEL,
    score_prooftext_anchors, score_aggravate_ordinal,
    classify_refusal,
)

FIXTURES = os.path.join(HERE, "fixtures")
COUNTER = {"counter-text": ["1 Tim 6:17-18", "1 Tim 5:8"]}  # matches the PROOF fixture keypoint


def _extract_ranking(text, labels=("a", "b", "c")):
    """Pull a 'a < b < c' style least->most ranking out of a free-text answer.

    Looks for the explicit 'RANKING: ...' line first (we ask for it), then any
    'x < y < z' pattern. Returns a list of labels or None if not parseable (the
    scorer's malformed path then handles it)."""
    m = re.search(r"RANKING:\s*([a-c]\s*(?:<\s*[a-c]\s*){1,})", text, re.IGNORECASE)
    seg = m.group(1) if m else None
    if seg is None:
        m = re.search(r"\b([a-c]\s*<\s*[a-c]\s*<\s*[a-c])\b", text, re.IGNORECASE)
        seg = m.group(1) if m else None
    if seg is None:
        return None
    order = [t.lower() for t in re.findall(r"[a-c]", seg, re.IGNORECASE)]
    return order if set(order) == set(labels) else order or None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true", help="make the real calls (else dry-run)")
    ap.add_argument("--model", default=CLI_DEFAULT_MODEL, help="full model id to pin")
    args = ap.parse_args()

    items = {it.id: it for it in load_items(FIXTURES)}
    proof = items["PROOF-C8-W302"]
    agg = items["AGG-C6-W301"]

    print(f"WCF-Bench smoke pilot — model={args.model}  auth=subscription OAuth (no API key)")
    print(f"pipeline: loader -> CLIModelClient -> scorers ; fixtures: {sorted(items)}")
    if not args.go:
        print("\nDRY RUN (no calls). Re-run with --go to make ~2 real calls (~$0.02 each).")
        print(f"  would prompt PROOF-C8-W302 ({len(proof.rubric)} rubric keypoints) and "
              f"AGG-C6-W301 (gold {agg.extra.get('gold_order')}).")
        return 0

    if not CLIModelClient.check_available():
        print("ERROR: `claude` CLI not available on PATH.", file=sys.stderr)
        return 2

    client = CLIModelClient(model=args.model)

    # -- 1. PROOFTEXT: free-text grounding, scored by anchor-matching + refusal --
    proof_prompt = (
        proof.stem
        + "\n\nGround your answer in the Westminster Standards. Cite the specific "
          "Larger Catechism question numbers (e.g. Q141, Q142) and any Scripture you rely on."
    )
    print("\n[1] PROOF-C8-W302 -> real call ...")
    proof_resp = client.complete(proof_prompt, item_id=proof.id)
    ps = score_prooftext_anchors(proof.rubric, proof_resp, counter_tokens=COUNTER)
    rf = classify_refusal(proof_resp, should_refuse=False)
    print(f"    response ({len(proof_resp)} chars): {proof_resp[:220].replace(chr(10),' ')}...")
    print(f"    anchor score: {ps.points}/{ps.max_points}  matched={len(ps.matched)} missed={len(ps.missed)}")
    print(f"    refusal taxonomy: {rf.refusal_class} (failure={rf.is_failure})")

    # -- 2. AGGRAVATE: free-text ranking, extracted + scored ordinally -----------
    agg_prompt = (
        agg.stem
        + "\n\nEnd your answer with a single line of exactly the form: "
          "RANKING: a < b < c  (least to most heinous)."
    )
    print("\n[2] AGG-C6-W301 -> real call ...")
    agg_resp = client.complete(agg_prompt, item_id=agg.id)
    ranking = _extract_ranking(agg_resp)
    order_max = agg.rubric[0].points
    ascore = score_aggravate_ordinal(
        gold_key=agg.extra["gold_order"],
        model_ranking=ranking if ranking else "declines total order",
        ordering_max=order_max,
    )
    print(f"    response ({len(agg_resp)} chars): {agg_resp[:220].replace(chr(10),' ')}...")
    print(f"    extracted ranking: {ranking}  (gold {agg.extra['gold_order']})")
    print(f"    ordinal score: {ascore.ordering_points}/{order_max}  tau={ascore.concordance} passed={ascore.passed_ordering}")

    print(f"\nDONE. real calls made: {client.calls_made} ; cost ~${client.cost_usd} ; auth=OAuth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
