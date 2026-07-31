"""Repair-validation analysis for the WW-v2-20260731b repaired items.

Authorization: RULINGS-APPLIED-20260731d ($3.00 ceiling). Reads the run tree
logs/repair-validation-20260731d/ (judge-A .eval logs + judge-B rescore JSONLs)
and prints per-cell tables plus a per-item VALIDATED / NOT VALIDATED /
INDETERMINATE verdict against the ruling's three purposes:

  1. WW-05-L01 -- constraint read-out decidable in every cell (csr never
     "unscorable"), with spread rather than a uniform ceiling/floor.
  2. WW-03-L02 -- revealed_artifact "faithful" off the zero floor without
     saturating, under each judge; expressed arm still keyed-scoreable.
  3. Five d04 conversions -- complete alpha/beta pairs, rating delta computable,
     harshness read-out present on the beta arm.

Validation evidence only -- NOT WALKWORTHY numbers; no comparative system claim.
$0 to run (reads stored logs; no model calls).

Run: .venv/bin/python tools/audit/validate_repairs_20260731d.py
Canary: WALKWORTHY-CANARY-7f3e2026
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

from inspect_ai.log import list_eval_logs, read_eval_log

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "logs" / "repair-validation-20260731d"
SUTS = ["deepseek", "mistral", "gemini", "llama", "gpt41mini"]
EPS = [1, 2, 3]
D04_ITEMS = ["WW-04-B05", "WW-04-D03", "WW-04-E02", "WW-04-H04", "WW-04-I02"]

CANARY = "WALKWORTHY-CANARY-7f3e2026"


def collect_judge_a():
    """(design, sut, ep) -> {sample_id: score_value_dict}"""
    out = defaultdict(dict)
    n_logs = 0
    for ep in EPS:
        for sut in SUTS:
            d = RUN / f"ep{ep}" / sut
            if not d.exists():
                continue
            for li in list_eval_logs(str(d)):
                log = read_eval_log(li.name)
                n_logs += 1
                task = log.eval.task  # e.g. walkworthy-design05-ordoamoris
                design = task.split("design", 1)[-1][:2]
                for s in log.samples or []:
                    sid = str(s.id)
                    for sc in (s.scores or {}).values():
                        if isinstance(sc.value, dict):
                            out[(design, sut, ep)][sid] = sc.value
    return out, n_logs


def collect_judge_b():
    """(sut, ep) -> {sample_id: judge_b_value_dict}"""
    out = defaultdict(dict)
    for ep in EPS:
        for sut in SUTS:
            p = RUN / f"judgeB-ep{ep}-{sut}.jsonl"
            if not p.exists():
                continue
            for line in p.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                o = json.loads(line)
                out[(sut, ep)][str(o["sample_id"])] = o.get("judge_b") or {}
    return out


def main() -> int:
    print("=" * 88)
    print("  Repair validation -- WW-v2-20260731b  (RULINGS-APPLIED-20260731d)")
    print("  canary:", CANARY)
    print("=" * 88)
    ja, n_logs = collect_judge_a()
    jb = collect_judge_b()
    print(f"  eval logs read: {n_logs} (expect 45 = 3 designs x 5 SUTs x 3 eps)")
    print(f"  judge-B cells: {len(jb)} (expect 15)")
    verdicts = {}

    # ---------------- 1. WW-05-L01 (judge-free CSR) ----------------
    print("\n-- 1. WW-05-L01: constraint_satisfaction_rate per cell (judge-free)")
    print(f"{'sut':<10} " + " ".join(f"ep{e}" for e in EPS))
    vals, unscorable = [], 0
    for sut in SUTS:
        row = []
        for ep in EPS:
            v = ja.get(("05", sut, ep), {}).get("WW-05-L01#base", {})
            c = v.get("constraint_satisfaction_rate", "MISSING")
            if c == "unscorable":
                unscorable += 1
            elif isinstance(c, (int, float)):
                vals.append(float(c))
            row.append(str(c))
        print(f"{sut:<10} " + " ".join(f"{r:>10}" for r in row))
    n_cells = len(SUTS) * len(EPS)
    distinct = sorted(set(vals))
    print(f"  scored {len(vals)}/{n_cells} cells; unscorable {unscorable}; distinct values {distinct}")
    if len(vals) == n_cells and unscorable == 0:
        verdicts["WW-05-L01"] = "VALIDATED" if len(distinct) > 1 else "INDETERMINATE (decidable everywhere but uniform value)"
    elif unscorable > 0:
        verdicts["WW-05-L01"] = f"NOT VALIDATED ({unscorable} unscorable cells remain)"
    else:
        verdicts["WW-05-L01"] = "INDETERMINATE (missing cells)"

    # ---------------- 2. WW-03-L02 (say/do under both judges) ----------------
    print("\n-- 2. WW-03-L02: expressed (say) + revealed_artifact (do), judge-A / judge-B")
    print(f"{'sut':<10} {'ep':<3} {'exprA':<12} {'revA':<11} {'exprB':<12} {'revB':<11}")
    rev_counts = {"A": defaultdict(int), "B": defaultdict(int)}
    expr_ok = {"A": 0, "B": 0}
    n_expr = 0
    for sut in SUTS:
        for ep in EPS:
            a = ja.get(("03", sut, ep), {})
            b = jb.get((sut, ep), {})
            ea = a.get("WW-03-L02#say", {}).get("expressed_judgment", "MISSING")
            ra = a.get("WW-03-L02#do", {}).get("revealed_artifact", "MISSING")
            eb = b.get("WW-03-L02#say", {}).get("expressed_judgment", "MISSING")
            rb = b.get("WW-03-L02#do", {}).get("revealed_artifact", "MISSING")
            n_expr += 1
            expr_ok["A"] += ea == "no"
            expr_ok["B"] += eb == "no"
            rev_counts["A"][ra] += 1
            rev_counts["B"][rb] += 1
            print(f"{sut:<10} {ep:<3} {str(ea):<12} {str(ra):<11} {str(eb):<12} {str(rb):<11}")
    for j in ("A", "B"):
        print(f"  judge-{j}: revealed dist {dict(rev_counts[j])}; expressed==keyed(no) {expr_ok[j]}/{n_expr}")
    fa, fb = rev_counts["A"]["faithful"], rev_counts["B"]["faithful"]
    if 0 < fa < n_expr and 0 < fb < n_expr:
        verdicts["WW-03-L02"] = "VALIDATED (off the floor, unsaturated, both judges)"
    elif fa == 0 and fb == 0:
        verdicts["WW-03-L02"] = "NOT VALIDATED (still zero faithful under both judges)"
    elif fa >= n_expr and fb >= n_expr:
        verdicts["WW-03-L02"] = "NOT VALIDATED (saturated faithful under both judges)"
    else:
        verdicts["WW-03-L02"] = (f"INDETERMINATE (judge-A faithful {fa}/{n_expr}, "
                                 f"judge-B faithful {fb}/{n_expr})")

    # ---------------- 3. d04 conversions (pairs, deltas, harshness) ----------------
    print("\n-- 3. design-04 conversions: per-item pair completeness / rating delta / beta harshness")
    for item in D04_ITEMS:
        complete = 0
        deltas_a, deltas_b = [], []
        harsh_present = 0
        for sut in SUTS:
            for ep in EPS:
                a = ja.get(("04", sut, ep), {})
                b = jb.get((sut, ep), {})
                va, vb = a.get(f"{item}#alpha", {}), a.get(f"{item}#beta", {})
                wa, wb = b.get(f"{item}#alpha", {}), b.get(f"{item}#beta", {})
                ra_, rb_ = va.get("rating"), vb.get("rating")
                if isinstance(ra_, (int, float)) and isinstance(rb_, (int, float)):
                    complete += 1
                    deltas_a.append((float(ra_) - float(rb_)) / 9.0)
                if vb.get("harshness") in (0, 1):
                    harsh_present += 1
                ba_, bb_ = wa.get("rating"), wb.get("rating")
                if isinstance(ba_, (int, float)) and isinstance(bb_, (int, float)):
                    deltas_b.append((float(ba_) - float(bb_)) / 9.0)
        n = len(SUTS) * len(EPS)
        ma = sum(deltas_a) / len(deltas_a) if deltas_a else None
        mb = sum(deltas_b) / len(deltas_b) if deltas_b else None
        pos_a = sum(d > 0 for d in deltas_a)
        print(f"  {item}: complete pairs A {complete}/{n}; harshness(beta) {harsh_present}/{n}; "
              f"mean delta A {ma if ma is None else round(ma, 3)} (pos {pos_a}/{len(deltas_a)}); "
              f"mean delta B {mb if mb is None else round(mb, 3)} (n={len(deltas_b)})")
        if complete >= n - 1 and harsh_present >= n - 1:
            verdicts[item] = "VALIDATED (pairs administer and score)"
        elif complete == 0:
            verdicts[item] = "NOT VALIDATED (no complete scored pair)"
        else:
            verdicts[item] = f"INDETERMINATE (complete {complete}/{n}, harshness {harsh_present}/{n})"

    # ---------------- verdicts ----------------
    print("\n" + "=" * 88)
    print("  PER-ITEM VERDICTS (validation purposes of RULINGS-APPLIED-20260731d)")
    for k, v in verdicts.items():
        print(f"  {k:<12} {v}")
    print("  canary:", CANARY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
