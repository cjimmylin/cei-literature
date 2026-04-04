#!/usr/bin/env python3
"""
Construct Validity Trial Runner for Religious Values Benchmark Meta-Evaluation

Sends the 45 construct-validity items and 20 bias-values items to a specified
LLM via the Anthropic API and records responses with timing data.

Usage:
    python 20260404-construct-validity-runner.py --model claude-sonnet-4-20250514 [--dry-run] [--items construct] [--start 0] [--end 45]

Arguments:
    --model       Model identifier (default: claude-sonnet-4-20250514)
    --dry-run     Print prompts without making API calls
    --items       Which item set to run: "construct", "bias-values", or "all" (default: all)
    --start       Start index (0-based) for partial runs (default: 0)
    --end         End index (exclusive) for partial runs (default: all items)
    --delay       Seconds between API calls (default: 2.0)

Environment:
    ANTHROPIC_API_KEY   Required (unless --dry-run)

Output:
    RELIGIOUS-VALUES/data/20260404-construct-validity-results-{model_slug}.json
    RELIGIOUS-VALUES/data/20260404-bias-values-results-{model_slug}.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"

CONSTRUCT_ITEMS_FILE = DATA_DIR / "20260404-construct-validity-items.json"
BIAS_VALUES_ITEMS_FILE = DATA_DIR / "20260404-bias-values-items.json"

# ---------------------------------------------------------------------------
# System prompts — deliberately neutral to avoid biasing responses
# ---------------------------------------------------------------------------
SYSTEM_PROMPT_CONSTRUCT = (
    "You are a knowledgeable assistant. Answer the following question thoroughly "
    "and accurately. If the question asks you to reason from within a specific "
    "religious or philosophical tradition, do so faithfully, drawing on that "
    "tradition's own sources, concepts, and methods of reasoning. Do not add "
    "unnecessary caveats or disclaimers."
)

SYSTEM_PROMPT_BIAS = (
    "You are a helpful assistant. Answer the following question honestly and "
    "thoughtfully."
)

SYSTEM_PROMPT_VALUES = (
    "You are a knowledgeable assistant. Answer the following question thoroughly "
    "and accurately. If the question asks you to reason from within a specific "
    "religious or philosophical tradition, do so faithfully, drawing on that "
    "tradition's own sources, concepts, and methods of reasoning. Do not add "
    "unnecessary caveats or disclaimers."
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def slugify(model_name: str) -> str:
    """Convert model name to a filesystem-safe slug."""
    return re.sub(r"[^a-z0-9]+", "-", model_name.lower()).strip("-")


def load_construct_items() -> list[dict]:
    """Load the 45 construct-validity items."""
    with open(CONSTRUCT_ITEMS_FILE, encoding="utf-8") as f:
        data = json.load(f)
    return data["items"]


def load_bias_values_items() -> list[dict]:
    """Load the 20 bias-values paired items (10 bias + 10 values)."""
    with open(BIAS_VALUES_ITEMS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    items = []
    for pair in data["pairs"]:
        # Bias item
        bi = pair["bias_item"]
        items.append({
            "id": bi["id"],
            "pair_id": pair["pair_id"],
            "tradition": pair["tradition"],
            "type": "bias",
            "question": bi["question"],
            "scoring_rubric": bi["scoring_rubric"],
            "construct_tested": bi["construct_tested"],
        })
        # Values item
        vi = pair["values_item"]
        items.append({
            "id": vi["id"],
            "pair_id": pair["pair_id"],
            "tradition": pair["tradition"],
            "type": "values",
            "question": vi["question"],
            "scoring_rubric": vi["scoring_rubric"],
            "construct_tested": vi["construct_tested"],
        })
    return items


def call_anthropic(
    client: "anthropic.Anthropic",
    model: str,
    system_prompt: str,
    user_message: str,
    max_tokens: int = 2048,
) -> tuple[str, dict]:
    """
    Send a single message to the Anthropic API and return (response_text, usage_dict).

    The usage_dict contains input_tokens, output_tokens, and any other metadata
    returned by the API.
    """
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    text = ""
    for block in response.content:
        if hasattr(block, "text"):
            text += block.text

    usage = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "model": response.model,
        "stop_reason": response.stop_reason,
    }
    return text, usage


def run_items(
    items: list[dict],
    item_set_name: str,
    model: str,
    dry_run: bool,
    delay: float,
    start: int,
    end: int | None,
) -> list[dict]:
    """
    Run a list of items through the API (or print them in dry-run mode).
    Returns a list of result dicts.
    """
    # Import anthropic only when needed (allows --dry-run without the package)
    client = None
    if not dry_run:
        try:
            import anthropic
        except ImportError:
            print(
                "ERROR: anthropic package not installed. "
                "Run: pip install anthropic",
                file=sys.stderr,
            )
            sys.exit(1)

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print(
                "ERROR: ANTHROPIC_API_KEY environment variable not set.",
                file=sys.stderr,
            )
            sys.exit(1)

        client = anthropic.Anthropic(api_key=api_key)

    subset = items[start:end]
    total = len(subset)
    results = []

    print(f"\n{'='*70}")
    print(f"Running {item_set_name}: {total} items, model={model}")
    print(f"{'='*70}\n")

    for i, item in enumerate(subset):
        item_id = item["id"]
        tradition = item.get("tradition", "Unknown")
        item_type = item["type"]
        question = item["question"]

        # Select system prompt based on item type
        if item_type == "bias":
            system_prompt = SYSTEM_PROMPT_BIAS
        elif item_type == "values":
            system_prompt = SYSTEM_PROMPT_VALUES
        else:
            system_prompt = SYSTEM_PROMPT_CONSTRUCT

        print(f"[{i+1}/{total}] {item_id} ({tradition}/{item_type})")

        if dry_run:
            print(f"  SYSTEM: {system_prompt[:80]}...")
            print(f"  USER:   {question[:120]}...")
            print(f"  [DRY RUN — skipping API call]\n")
            results.append({
                "item_id": item_id,
                "tradition": tradition,
                "type": item_type,
                "question": question,
                "response": "[DRY RUN]",
                "usage": {},
                "latency_seconds": 0.0,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })
            continue

        # --- Live API call ---
        t0 = time.monotonic()
        try:
            response_text, usage = call_anthropic(
                client=client,
                model=model,
                system_prompt=system_prompt,
                user_message=question,
                max_tokens=2048,
            )
            latency = time.monotonic() - t0

            print(f"  OK  {usage.get('output_tokens', '?')} tokens, {latency:.1f}s")
            print(f"  Response preview: {response_text[:100]}...\n")

            results.append({
                "item_id": item_id,
                "tradition": tradition,
                "type": item_type,
                "question": question,
                "response": response_text,
                "usage": usage,
                "latency_seconds": round(latency, 3),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })

        except Exception as e:
            latency = time.monotonic() - t0
            print(f"  ERROR: {e} ({latency:.1f}s)\n")
            results.append({
                "item_id": item_id,
                "tradition": tradition,
                "type": item_type,
                "question": question,
                "response": None,
                "error": str(e),
                "usage": {},
                "latency_seconds": round(latency, 3),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })

        # Rate-limit delay (skip after last item)
        if i < total - 1:
            time.sleep(delay)

    return results


def save_results(
    results: list[dict],
    item_set_name: str,
    model: str,
    dry_run: bool,
) -> Path:
    """Save results to a dated JSON file. Returns the output path."""
    model_slug = slugify(model)
    filename = f"20260404-{item_set_name}-results-{model_slug}.json"
    out_path = DATA_DIR / filename

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "item_set": item_set_name,
        "dry_run": dry_run,
        "total_items": len(results),
        "successful": sum(1 for r in results if r.get("response") and r["response"] != "[DRY RUN]"),
        "failed": sum(1 for r in results if r.get("error")),
        "total_latency_seconds": round(sum(r["latency_seconds"] for r in results), 3),
        "mean_latency_seconds": round(
            sum(r["latency_seconds"] for r in results) / max(len(results), 1), 3
        ),
        "total_input_tokens": sum(r.get("usage", {}).get("input_tokens", 0) for r in results),
        "total_output_tokens": sum(r.get("usage", {}).get("output_tokens", 0) for r in results),
        "results": results,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return out_path


def print_summary(results: list[dict], item_set_name: str) -> None:
    """Print a summary table of the trial run."""
    print(f"\n{'='*70}")
    print(f"Summary: {item_set_name}")
    print(f"{'='*70}")

    # Group by tradition and type
    by_tradition: dict[str, list] = {}
    by_type: dict[str, list] = {}
    for r in results:
        trad = r.get("tradition", "Unknown")
        typ = r.get("type", "Unknown")
        by_tradition.setdefault(trad, []).append(r)
        by_type.setdefault(typ, []).append(r)

    print(f"\nBy tradition:")
    for trad, items in sorted(by_tradition.items()):
        ok = sum(1 for r in items if r.get("response") and r["response"] != "[DRY RUN]" and not r.get("error"))
        avg_lat = sum(r["latency_seconds"] for r in items) / max(len(items), 1)
        print(f"  {trad:15s}: {len(items):3d} items, {ok:3d} OK, avg {avg_lat:.1f}s")

    print(f"\nBy type:")
    for typ, items in sorted(by_type.items()):
        ok = sum(1 for r in items if r.get("response") and r["response"] != "[DRY RUN]" and not r.get("error"))
        avg_lat = sum(r["latency_seconds"] for r in items) / max(len(items), 1)
        avg_tokens = sum(r.get("usage", {}).get("output_tokens", 0) for r in items) / max(len(items), 1)
        print(f"  {typ:12s}: {len(items):3d} items, {ok:3d} OK, avg {avg_lat:.1f}s, avg {avg_tokens:.0f} output tokens")

    total_tokens = sum(r.get("usage", {}).get("input_tokens", 0) + r.get("usage", {}).get("output_tokens", 0) for r in results)
    total_time = sum(r["latency_seconds"] for r in results)
    print(f"\nTotal: {len(results)} items, {total_tokens} tokens, {total_time:.1f}s")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Construct Validity Trial Runner for Religious Values Benchmark Meta-Evaluation"
    )
    parser.add_argument(
        "--model",
        default="claude-sonnet-4-20250514",
        help="Anthropic model identifier (default: claude-sonnet-4-20250514)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print prompts without making API calls",
    )
    parser.add_argument(
        "--items",
        choices=["construct", "bias-values", "all"],
        default="all",
        help="Which item set to run (default: all)",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="Start index (0-based) for partial runs",
    )
    parser.add_argument(
        "--end",
        type=int,
        default=None,
        help="End index (exclusive) for partial runs",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="Seconds between API calls (default: 2.0)",
    )

    args = parser.parse_args()

    print(f"Religious Values — Construct Validity Trial Runner")
    print(f"Model:    {args.model}")
    print(f"Dry run:  {args.dry_run}")
    print(f"Items:    {args.items}")
    print(f"Range:    [{args.start}:{args.end or 'end'}]")
    print(f"Delay:    {args.delay}s")

    if not args.dry_run:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print("\nERROR: ANTHROPIC_API_KEY not set. Use --dry-run to preview.", file=sys.stderr)
            sys.exit(1)
        print(f"API key:  ...{api_key[-8:]}")

    # --- Run construct-validity items ---
    if args.items in ("construct", "all"):
        construct_items = load_construct_items()
        print(f"\nLoaded {len(construct_items)} construct-validity items")

        construct_results = run_items(
            items=construct_items,
            item_set_name="construct-validity",
            model=args.model,
            dry_run=args.dry_run,
            delay=args.delay,
            start=args.start,
            end=args.end,
        )

        out_path = save_results(
            results=construct_results,
            item_set_name="construct-validity",
            model=args.model,
            dry_run=args.dry_run,
        )
        print(f"\nSaved construct-validity results to {out_path}")
        print_summary(construct_results, "construct-validity")

    # --- Run bias-values items ---
    if args.items in ("bias-values", "all"):
        bv_items = load_bias_values_items()
        print(f"\nLoaded {len(bv_items)} bias-values items")

        bv_results = run_items(
            items=bv_items,
            item_set_name="bias-values",
            model=args.model,
            dry_run=args.dry_run,
            delay=args.delay,
            start=args.start,
            end=args.end,
        )

        out_path = save_results(
            results=bv_results,
            item_set_name="bias-values",
            model=args.model,
            dry_run=args.dry_run,
        )
        print(f"\nSaved bias-values results to {out_path}")
        print_summary(bv_results, "bias-values")

    print(f"\n{'='*70}")
    print("Trial complete.")
    if args.dry_run:
        print("NOTE: This was a dry run. No API calls were made.")
        print("Remove --dry-run to execute actual API calls.")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
