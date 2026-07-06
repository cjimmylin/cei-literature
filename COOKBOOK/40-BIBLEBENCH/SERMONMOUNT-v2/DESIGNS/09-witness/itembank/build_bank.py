"""
build_bank.py — Merge seed + fan-out core batches into the frozen WITNESS core bank.

Pipeline:
  1. read seed_cores.jsonl + cores_batch_{A,B,C}.jsonl  (regenerate them first via each
     module's build(write=True) — done in the caller / CI step)
  2. re-validate EVERY core with validate_core (the LOCKED gate rules)
  3. enforce portfolio invariants:
       - 30 cores, P1's ten S-IDs, 3 cores each
       - 20% core-level holdout (== 6), sampled across S-ID strata (guide §3)
       - unique core_ids and unique content hashes
       - reverse-keyed ~30% of cores (acquiescence hygiene, brief §6)
  4. belt-and-suspenders leakage sweep over ALL string fields (not only model-facing)
  5. write cores.jsonl (the frozen bank) + SHARED/core-ledger.jsonl (guide §3)

Run:  ../.venv/bin/python DESIGNS/09-witness/itembank/build_bank.py
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from witness_common import (  # noqa: E402
    Core, validate_core, load_cores, dump_cores, leakage_hits,
    ITEMBANK_DIR, CORE_LEDGER, P1_SIDS, write_jsonl,
)

SOURCES = ["seed_cores.jsonl", "cores_batch_A.jsonl", "cores_batch_B.jsonl", "cores_batch_C.jsonl"]
ALL_STRING_FIELDS = (
    "situation", "stakes", "gold_action", "deficient_pole", "counterfeit_pole",
    "gap_prediction", "end_proposition", "rec_gold", "rec_deficient", "rec_counterfeit",
    "rec_neutral", "gen_prompt",
)


def main() -> int:
    cores: list[Core] = []
    for src in SOURCES:
        p = ITEMBANK_DIR / src
        if not p.exists():
            print(f"FATAL: missing source {p}")
            return 1
        batch = load_cores(p)
        print(f"  {src}: {len(batch)} cores")
        cores.extend(batch)

    problems: list[str] = []

    # 2. re-validate every core
    for c in cores:
        problems.extend(validate_core(c))

    # 3. invariants
    if len(cores) != 30:
        problems.append(f"expected 30 cores, got {len(cores)}")
    ids = [c.core_id for c in cores]
    dupe_ids = [i for i, n in Counter(ids).items() if n > 1]
    if dupe_ids:
        problems.append(f"duplicate core_ids: {dupe_ids}")
    hashes = [c.content_hash() for c in cores]
    dupe_h = [h for h, n in Counter(hashes).items() if n > 1]
    if dupe_h:
        problems.append(f"duplicate content hashes (near-duplicate cores): {dupe_h}")

    sid_counts = Counter(s for c in cores for s in c.sid)
    for sid in P1_SIDS:
        if sid_counts.get(sid, 0) != 3:
            problems.append(f"S-ID {sid}: expected 3 cores, got {sid_counts.get(sid, 0)}")
    extra = set(sid_counts) - set(P1_SIDS)
    if extra:
        problems.append(f"unexpected S-IDs present: {sorted(extra)}")

    n_hold = sum(c.holdout for c in cores)
    if n_hold != 6:
        problems.append(f"holdout should be 6 (20%), got {n_hold}")
    hold_sids = sorted({s for c in cores if c.holdout for s in c.sid})
    if len(hold_sids) < 5:
        problems.append(f"holdout not spread across strata (only {hold_sids})")

    n_rev = sum(c.end_reverse_keyed for c in cores)
    if not (7 <= n_rev <= 12):        # ~30% of 30
        problems.append(f"reverse-keyed count {n_rev} outside acceptable 7-12 band")

    # 4. leakage sweep over ALL string fields (extra safety beyond validate_core)
    for c in cores:
        for fld in ALL_STRING_FIELDS:
            hits = leakage_hits(getattr(c, fld))
            if hits:
                problems.append(f"{c.core_id}: leakage {sorted(set(hits))} in '{fld}'")
        for key in ("prompt", "system", "initial_state_desc"):
            hits = leakage_hits(str(c.act_spec.get(key, "")))
            if hits:
                problems.append(f"{c.core_id}: leakage {sorted(set(hits))} in act_spec['{key}']")

    if problems:
        print("\nBANK BUILD FAILED:")
        for p in problems:
            print("  -", p)
        return 1

    # 5. write frozen bank + ledger
    out = ITEMBANK_DIR / "cores.jsonl"
    dump_cores(cores, out)
    ledger = [c.ledger_record() for c in cores]
    write_jsonl(ledger, CORE_LEDGER)

    print("\nBANK OK")
    print(f"  cores           : {len(cores)}")
    print(f"  S-IDs           : {sorted(sid_counts)} (3 each)")
    print(f"  holdout         : {n_hold}/30 across strata {hold_sids}")
    print(f"  reverse-keyed   : {n_rev}/30 ({100*n_rev//30}%)")
    print(f"  families        : {len({c.family for c in cores})} distinct")
    print(f"  wrote           : {out}")
    print(f"  ledger          : {CORE_LEDGER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
