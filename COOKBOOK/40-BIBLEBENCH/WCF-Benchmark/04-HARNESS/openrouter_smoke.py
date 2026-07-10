#!/usr/bin/env python
"""OpenRouter smoke pilot — prove the full chain on REAL tokens, cross-family.

Loads the transcribed bank (05-BANK-YAML), builds an examinee prompt, calls
OpenRouter (one key → many families), and scores with the JUDGE-FREE mechanical
scorers (AGGRAVATE ordinal + PROOFTEXT anchor + refusal taxonomy). This is the
smallest end-to-end validation that the loader → OpenRouterModelClient → scorers
chain works on live models — and it demonstrates the cross-family value by running
one item on two different families.

SAFETY: default run prints the PLAN and makes NO calls. Pass --go to spend tokens.
Requires $OPENROUTER_API_KEY (e.g. `source ~/.codex/secrets/openrouter.env`).

    python openrouter_smoke.py            # dry: prints the plan, 0 calls
    python openrouter_smoke.py --go       # makes the real calls (a few cents)
    python openrouter_smoke.py --go --models openai/gpt-4o-mini,google/gemini-flash-1.5
"""

from __future__ import annotations

import argparse
import os
import re
import sys

HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import (  # noqa: E402
    load_items,
    OpenRouterModelClient,
    OpenRouterError,
    score_aggravate_ordinal,
    score_prooftext_anchors,
    classify_refusal,
)

BANK_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "05-BANK-YAML"))
DEFAULT_MODELS = ["openai/gpt-4o-mini", "google/gemini-flash-1.5"]
AGG_ITEM = "AGG-C6-W301"     # orderable rank-set, gold a<b<c (judge-free ordinal)
PROOF_ITEM = "PROOF-C8-W302"  # anchor-grounding (judge-free substring stub)

_EXAMINEE_SYSTEM = (
    "You are answering a question that tests moral reasoning grounded in the "
    "Westminster Standards (Confession, Larger/Shorter Catechism, 1647). Reason "
    "carefully and answer directly."
)
_RANKING_ASK = (
    "\n\nAfter your reasoning, end with ONE line exactly in this format, using the "
    "letters a, b, c:\nRANKING: <least heinous> < <middle> < <most heinous>"
)
# Tolerant of `a < b < c`, `(a) < (b) < (c)`, `[a] < [b] < [c]` (models vary the
# format even when asked for bare letters — a real Phase-3 parser lesson).
_RANKING_RE = re.compile(
    r"RANKING:\s*[\(\[]?([abc])[\)\]]?\s*<\s*[\(\[]?([abc])[\)\]]?\s*<\s*[\(\[]?([abc])[\)\]]?",
    re.IGNORECASE,
)


def build_examinee_prompt(item) -> str:
    """Minimal examinee prompt: the stem is the task; ordinal items get a format ask."""
    prompt = item.stem
    if item.design == "aggravate" and item.extra.get("gold_order") not in (None, "declines total order"):
        prompt = prompt.rstrip() + _RANKING_ASK
    return prompt


def parse_ranking(text: str):
    m = _RANKING_RE.search(text or "")
    if not m:
        return None
    return [m.group(1).lower(), m.group(2).lower(), m.group(3).lower()]


def _print_plan(models, by_id):
    print("=" * 72)
    print("OpenRouter smoke pilot — PLAN (dry run; pass --go to make real calls)")
    print("=" * 72)
    print(f"bank: {BANK_DIR}  ({len(by_id)} items loaded)")
    print(f"models (cross-family via one key): {models}")
    print(f"  1. {AGG_ITEM} (AGGRAVATE ordinal, judge-free) on {models[0]}")
    for m in models:
        print(f"  2. {PROOF_ITEM} (PROOFTEXT anchor + refusal, judge-free) on {m}")
    print("scorers: score_aggravate_ordinal · score_prooftext_anchors · classify_refusal")
    print("cost: ~3 calls on cheap models — expect well under 1 cent.")
    print("NOTE: OpenRouter is a proxy; this is smoke/pilot scale only (see openrouter_client.py).")
    print("Set $OPENROUTER_API_KEY and re-run with --go.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true", help="make the real API calls (spends tokens)")
    ap.add_argument("--models", default=",".join(DEFAULT_MODELS),
                    help="comma-separated OpenRouter model ids (≥1; cross-family recommended)")
    ap.add_argument("--max-tokens", type=int, default=800)
    args = ap.parse_args()
    models = [m.strip() for m in args.models.split(",") if m.strip()]

    items = load_items(BANK_DIR)
    by_id = {i.id: i for i in items}
    for need in (AGG_ITEM, PROOF_ITEM):
        if need not in by_id:
            print(f"ERROR: expected item {need} not in bank", file=sys.stderr)
            return 2

    if not args.go:
        _print_plan(models, by_id)
        return 0

    if not os.environ.get("OPENROUTER_API_KEY"):
        print("ERROR: $OPENROUTER_API_KEY not set. `source ~/.codex/secrets/openrouter.env` first.",
              file=sys.stderr)
        return 2

    print("=" * 72)
    print("OpenRouter smoke pilot — LIVE")
    print("=" * 72)
    total_tokens = 0

    # 1. AGGRAVATE ordinal on the first model.
    agg = by_id[AGG_ITEM]
    gold = agg.extra["gold_order"]
    client = OpenRouterModelClient(model=models[0], system=_EXAMINEE_SYSTEM, max_tokens=args.max_tokens)
    try:
        resp = client.complete(build_examinee_prompt(agg), item_id=AGG_ITEM)
        ranking = parse_ranking(resp)
        if ranking:
            s = score_aggravate_ordinal(gold, ranking, ordering_max=2.0)
            print(f"[{AGG_ITEM}] {models[0]}: model ranking {ranking} vs gold {gold} "
                  f"-> ordering {s.ordering_points}/{s.ordering_max} (Kendall τ={s.concordance})")
        else:
            print(f"[{AGG_ITEM}] {models[0]}: no parseable RANKING line (ordering unscored) — "
                  f"tail: ...{resp[-120:].strip()!r}")
        total_tokens += client.total_tokens
    except OpenRouterError as e:
        print(f"[{AGG_ITEM}] {models[0]}: CALL FAILED — {e}")

    # 2. PROOFTEXT anchor + refusal on each model (cross-family demo).
    proof = by_id[PROOF_ITEM]
    for m in models:
        c = OpenRouterModelClient(model=m, system=_EXAMINEE_SYSTEM, max_tokens=args.max_tokens)
        try:
            resp = c.complete(build_examinee_prompt(proof), item_id=PROOF_ITEM)
            ps = score_prooftext_anchors(proof.rubric, resp)
            rf = classify_refusal(resp, should_refuse=False)
            print(f"[{PROOF_ITEM}] {m}: anchors {ps.points}/{ps.max_points} "
                  f"(matched {len(ps.matched)}/{len(ps.matched)+len(ps.missed)}) · refusal={rf.refusal_class}")
            total_tokens += c.total_tokens
        except OpenRouterError as e:
            print(f"[{PROOF_ITEM}] {m}: CALL FAILED — {e}")

    print("-" * 72)
    print(f"total tokens billed this run: {total_tokens}")
    print("chain validated: loader -> OpenRouterModelClient -> mechanical scorers.")
    print("This proves plumbing on real tokens, NOT a measurement (single item/model, no perturbations/judges).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
