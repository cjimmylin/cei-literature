"""Offline design-05 CSR recovery (20260716 pilot bug fix).

The live pilot ran design05_scorer with the alloc-spec field-path bug (top-level
keyed.allocation instead of keyed.extras.allocation), so every stored CSR is
structurally unscorable. CSR is judge-free and deterministic, so the TRUE values are
recoverable from the stored logs at zero cost: re-parse each stored SUT completion
with the CORRECT tokens/budget and recompute item_csr.

Usage:
    .venv/bin/python tools/audit/recompute_design05_csr.py --pilot-dir logs/pilot-20260716
"""
from __future__ import annotations

import argparse
import glob
import os
import sys
from pathlib import Path
from typing import List

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402

from walkworthy_inspect.ordo_constraints import item_csr  # noqa: E402
from walkworthy_inspect.parsers import reparse_allocation_response  # noqa: E402


def recover(log_path: str) -> dict:
    log = read_eval_log(log_path)
    vals: List[float] = []
    n_total = noncompliant = undecidable = 0
    for s in (log.samples or []):
        meta = s.metadata or {}
        if meta.get("is_exemplar") or str(meta.get("admin", "")).endswith("-exemplar"):
            continue
        n_total += 1
        keyed = meta.get("keyed", {}) or {}
        alloc = (keyed.get("allocation")
                 or (keyed.get("extras", {}) or {}).get("allocation") or {})
        tokens = alloc.get("tokens", []) or []
        budget = float(alloc.get("budget", 0) or 0)
        constraints = keyed.get("keyed_constraints", "") or alloc.get("constraints", "")
        completion = s.output.completion if s.output else ""
        parse = reparse_allocation_response(completion, tokens, budget)
        if parse.non_compliant or not parse.values:
            noncompliant += 1
            continue
        csr = item_csr(parse.values, constraints, tokens)
        if csr is None:
            undecidable += 1
            continue
        vals.append(float(csr))
    mean = sum(vals) / len(vals) if vals else float("nan")
    return {"csr_mean": round(mean, 4), "n": len(vals), "n_total": n_total,
            "non_compliant": noncompliant, "undecidable_constraints": undecidable}


def main() -> None:
    ap = argparse.ArgumentParser(description="Recover true design-05 CSR from stored logs.")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    args = ap.parse_args()
    print("=== design-05 CSR, recovered with the corrected alloc-spec path ===")
    for d in sorted(glob.glob(os.path.join(args.pilot_dir, "*/"))):
        logs = sorted(glob.glob(os.path.join(d, "*design05*.eval")))
        if not logs:
            continue
        sut = Path(d.rstrip("/")).name
        r = recover(logs[0])
        print(f"  {sut:20} {r}")


if __name__ == "__main__":
    main()
