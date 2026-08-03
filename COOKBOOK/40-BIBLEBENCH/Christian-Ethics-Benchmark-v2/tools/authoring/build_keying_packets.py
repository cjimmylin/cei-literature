"""v4-A authoring — build STRIPPED blind-keying packets (spec 20260802f §7).

Reads drafted d05 bank files and emits keying packets containing ONLY what the
blind second keyer may see: item id, tokens, budget, ask, constraint text, and
the constraint-id legend (C1..Cn in parse order with each clause's raw text).
The drafter's author1 key and everything else is stripped — the double-keying
disagreement rate is an instrument property and leakage would bias it upward
by construction.

Usage:
  .venv/bin/python tools/authoring/build_keying_packets.py \
      --banks fileA.jsonl fileB.jsonl --out packets.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from walkworthy_inspect.ordo_constraints import parse_keyed_constraints  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--banks", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    packets = []
    for bank in args.banks:
        for line in Path(bank).open(encoding="utf-8"):
            if not line.strip():
                continue
            obj = json.loads(line)
            meta = obj["metadata"]
            keyed = meta["keyed"]
            alloc = keyed["extras"]["allocation"]
            parsed = parse_keyed_constraints(keyed["keyed_constraints"],
                                             alloc["tokens"])
            packets.append({
                "item_id": meta["item_id"],
                "tokens": alloc["tokens"],
                "budget": alloc["budget"],
                "ask": alloc["ask"],
                "constraints": keyed["keyed_constraints"],
                "constraint_legend": {
                    f"C{i + 1}": c.raw for i, c in enumerate(parsed.constraints)
                },
                "n_constraints": parsed.n_parsed,
            })

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for p in packets:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"wrote {len(packets)} stripped keying packets -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
