"""v4-A authoring — assemble final v4 d05 banks with double-keyed sacrifice orders.

Merges drafted bank files with the blind second keys (author2) and the
adjudicated orders, writes the final public/holdout banks, and prints the
double-keying disagreement summary (spec §2.2: recorded and disclosed as an
instrument property). Runs entirely offline; holdout content never reaches the
console (only ids and rates are printed).

Inputs:
  --banks       drafted bank JSONLs (drafter output, author1 present)
  --author2     JSONL of {"item_id", "author2": [...]} from the blind keyer
  --adjudicated JSONL of {"item_id", "adjudicated": [...]} for items where the
                authors disagreed (agreed items adopt the shared order)
  --out         final bank path

Usage (run once per bank — public and holdout separately):
  .venv/bin/python tools/authoring/assemble_v4_d05.py \
      --banks drafterA.jsonl drafterB.jsonl drafterC.jsonl \
      --author2 author2_public.jsonl --adjudicated adjudicated_public.jsonl \
      --out datasets/v4/public/design05.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from walkworthy_v4.ranked_sacrifice import (  # noqa: E402
    bank_key_disagreement,
    key_disagreement,
)


def _load_map(path: str, field: str) -> Dict[str, List[str]]:
    out: Dict[str, List[str]] = {}
    if not path:
        return out
    for line in Path(path).open(encoding="utf-8"):
        if line.strip():
            obj = json.loads(line)
            out[obj["item_id"]] = obj[field]
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--banks", nargs="+", required=True)
    ap.add_argument("--author2", required=True)
    ap.add_argument("--adjudicated", default="")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    author2 = _load_map(args.author2, "author2")
    adjudicated = _load_map(args.adjudicated, "adjudicated")

    rows = []
    ranked_keys = []
    disagreements = []
    for bank in args.banks:
        for line in Path(bank).open(encoding="utf-8"):
            if not line.strip():
                continue
            obj = json.loads(line)
            meta = obj["metadata"]
            item_id = meta["item_id"]
            rk = meta["keyed"]["extras"]["ranked_sacrifice"]
            a1 = rk["keys"]["author1"]
            a2 = author2.get(item_id)
            if a2 is None:
                print(f"  MISSING author2 for {item_id}", file=sys.stderr)
                return 1
            rk["keys"]["author2"] = a2
            if a1 == a2:
                rk["adjudicated"] = list(a1)
            else:
                adj = adjudicated.get(item_id)
                if adj is None:
                    d = key_disagreement(a1, a2)
                    print(f"  DISAGREEMENT unadjudicated {item_id} "
                          f"(pairwise {d['pairwise_disagreement']:.2f})",
                          file=sys.stderr)
                    disagreements.append(item_id)
                    continue
                rk["adjudicated"] = list(adj)
            ranked_keys.append(rk)
            rows.append(obj)

    if disagreements:
        print(f"{len(disagreements)} unadjudicated disagreement(s) — supply "
              f"--adjudicated and re-run", file=sys.stderr)
        return 1

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    summary = bank_key_disagreement(ranked_keys)
    print(f"wrote {len(rows)} items -> {out}")
    print("double-keying disagreement (instrument property):")
    for k, v in summary.items():
        print(f"  {k}: {v if isinstance(v, int) else round(v, 4)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
