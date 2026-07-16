#!/usr/bin/env python3
"""
analyze_agreement.py — compute v2-vs-v1jA agreement + v1jA-vs-v1jB baseline.

Reads:
  * replay verdicts (v2-vs-v1jA) from logs/replay-20260715/replay_verdicts_mistral.jsonl
  * v1 verdicts.jsonl for the v1 judge-A vs judge-B natural baseline (FREE, no calls).

Metrics per design, per FIELD:
  * categorical: exact-agreement %, Cohen's kappa (when >=2 categories on both sides
    and >=? units; else raw-only + note)
  * ordinal/int: exact %, within-tolerance (|delta|<=1) %
Baseline: same fields, v1 judge-A vs v1 judge-B, on the SAME (design,item,admin,SUT) units.
"""
from __future__ import annotations
import json
from collections import defaultdict, Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
V2 = HERE.parent.parent
V1 = V2.parent / "Christian-Ethics-Benchmark"
REPLAY = V2 / "logs/replay-20260715/replay_verdicts_mistral.jsonl"
SUT = "mistralai/mistral-small-3.2-24b-instruct"

# field types: which are categorical vs ordinal/int
CAT_FIELDS = {"action_class", "expressed_judgment", "revealed_artifact",
              "favorability", "turn_state", "guardrail_state", "owes_direction"}
ORD_FIELDS = {"rationale_quality", "keypoints_met", "rationale_honesty",
              "frame", "facts", "principles", "alternatives", "resolution",
              "remainder", "pastoral", "treatment", "prudence", "rating"}
BIN_FIELDS = {"harshness", "contempt", "duality", "floor_compliance"}

DESIGN_ADMINMAP = {  # v1 admin -> v2 admin (for the baseline join key, use v1 admin)
    "01": {"main": "base"}, "03": {"expressed": "say", "revealed": "do"},
    "04": {"alpha": "alpha", "beta": "beta"}, "05": {"main": "base"},
    "06": {"main": "base"}, "08": {"covert": "covert", "overt": "overt"},
    "09": {"seat_A": "seat_A", "seat_B": "seat_B"}, "10": {"U": "U", "N": "N"},
}


def cohen_kappa(pairs):
    """pairs: list of (a,b) categorical labels. Returns kappa or None."""
    n = len(pairs)
    if n == 0:
        return None
    cats = sorted(set([a for a, _ in pairs] + [b for _, b in pairs]))
    if len(cats) < 2:
        return None  # degenerate: only one category observed -> kappa undefined
    po = sum(1 for a, b in pairs if a == b) / n
    ca = Counter(a for a, _ in pairs)
    cb = Counter(b for _, b in pairs)
    pe = sum((ca[c] / n) * (cb[c] / n) for c in cats)
    if pe == 1.0:
        return None
    return (po - pe) / (1 - pe)


def load_replay():
    """(design,item,v1_admin) -> {field: (v1_val, v2_val)}"""
    out = {}
    for line in REPLAY.read_text().splitlines():
        r = json.loads(line)
        dnum = r["design"].split("-", 1)[0]
        key = (dnum, r["item_id"], r["v1_admin"])
        v1s, v2s = r["v1_scores"], r["v2_scores"]
        fields = {}
        if isinstance(v2s, dict) and "__unscorable__" not in v2s and "__error__" not in v2s:
            for f, v1v in v1s.items():
                fields[f] = (v1v, v2s.get(f, "__missing__"))
        else:
            for f, v1v in v1s.items():
                fields[f] = (v1v, "__unscorable__")
        out[key] = fields
    return out


def load_v1_baseline(unit_keys):
    """For the SAME units, extract v1 judge-A vs judge-B scores.
    unit_keys: set of (dnum, item, v1_admin). Returns (dnum,item,v1_admin)->{field:(A,B)}."""
    # gather per (judge, dnum, item) -> {admin: scores}
    store = defaultdict(dict)  # (judge,dnum,item) -> {admin_or_main: scores}
    for line in (V1 / "runs/20260713-mvp-a1/verdicts.jsonl").read_text().splitlines():
        r = json.loads(line)
        if r["model"] != SUT:
            continue
        judge = "A" if r["judge"] == "openai/gpt-4.1-nano" else "B"
        dnum = r["design"].split("-", 1)[0]
        v = r["verdict"]
        d = store[(judge, dnum, r["item_id"])]
        if v["unit"] == "item":
            d["main"] = dict(v["scores"])
        else:
            for u in v.get("per_unit", []):
                if u.get("label") is not None:
                    d[u["label"]] = dict(u["scores"])
    out = {}
    for (dnum, item, admin) in unit_keys:
        a = store.get(("A", dnum, item), {}).get(admin)
        b = store.get(("B", dnum, item), {}).get(admin)
        if a is None or b is None:
            continue
        fields = {}
        for f, av in a.items():
            if f in b:
                fields[f] = (av, b[f])
        out[(dnum, item, admin)] = fields
    return out


def norm(v):
    return v  # values already comparable; None stays None


def summarize(pairs_by_field, label):
    """pairs_by_field: {field:[(x,y),...]}. Returns per-field dict of metrics."""
    res = {}
    for f, pairs in pairs_by_field.items():
        # drop pairs where either side is unscorable/missing/None -> count separately
        clean = [(a, b) for a, b in pairs
                 if a not in ("__missing__", "__unscorable__", None)
                 and b not in ("__missing__", "__unscorable__", None)]
        n_total = len(pairs)
        n = len(clean)
        n_drop = n_total - n
        if n == 0:
            res[f] = {"n": 0, "n_total": n_total, "n_drop": n_drop}
            continue
        exact = sum(1 for a, b in clean if a == b) / n
        entry = {"n": n, "n_total": n_total, "n_drop": n_drop, "exact": exact}
        if f in ORD_FIELDS or f in BIN_FIELDS:
            tol = sum(1 for a, b in clean if abs(float(a) - float(b)) <= 1) / n
            entry["within1"] = tol
        if f in CAT_FIELDS or f in BIN_FIELDS:
            k = cohen_kappa([(str(a), str(b)) for a, b in clean])
            entry["kappa"] = k
        res[f] = entry
    return res


def main():
    replay = load_replay()
    unit_keys = set(replay.keys())
    baseline = load_v1_baseline(unit_keys)

    # group by design
    designs = sorted(set(k[0] for k in unit_keys))
    report = {}
    for dnum in designs:
        # v2 vs v1jA
        v2_pbf = defaultdict(list)
        units_d = [k for k in unit_keys if k[0] == dnum]
        for k in units_d:
            for f, (v1v, v2v) in replay[k].items():
                v2_pbf[f].append((v1v, v2v))
        # v1jA vs v1jB on same units
        base_pbf = defaultdict(list)
        for k in units_d:
            for f, (av, bv) in baseline.get(k, {}).items():
                base_pbf[f].append((av, bv))
        report[dnum] = {
            "n_units": len(units_d),
            "v2_vs_v1jA": summarize(v2_pbf, "v2vjA"),
            "v1jA_vs_v1jB": summarize(base_pbf, "jAvjB"),
        }

    # overall unit-level exact agreement (all fields must match) — a strict headline
    def unit_exact(pbf_source):
        pass

    # pretty print
    print("=" * 100)
    print(f"HARNESS-COMPARABILITY: v2-scorer vs v1-judge-A (gpt-4.1-nano), SUT={SUT}")
    print("=" * 100)
    for dnum in designs:
        R = report[dnum]
        print(f"\n### design{dnum}  (n_units={R['n_units']})")
        allf = sorted(set(R["v2_vs_v1jA"]) | set(R["v1jA_vs_v1jB"]))
        for f in allf:
            a = R["v2_vs_v1jA"].get(f, {})
            b = R["v1jA_vs_v1jB"].get(f, {})
            def fmt(d):
                if not d or d.get("n", 0) == 0:
                    return f"n={d.get('n',0)}(drop{d.get('n_drop',0)})"
                s = f"n={d['n']} exact={d['exact']*100:.0f}%"
                if "within1" in d:
                    s += f" w1={d['within1']*100:.0f}%"
                if "kappa" in d:
                    s += f" k={d['kappa']:.2f}" if d["kappa"] is not None else " k=n/a"
                if d.get("n_drop"):
                    s += f" drop={d['n_drop']}"
                return s
            print(f"   {f:20s} | v2vjA: {fmt(a):48s} | jAvjB: {fmt(b)}")

    # write machine-readable
    outp = V2 / "logs/replay-20260715/agreement_summary.json"
    outp.write_text(json.dumps(report, indent=2, default=str))
    print(f"\nWrote {outp}")


if __name__ == "__main__":
    main()
