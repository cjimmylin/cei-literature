#!/usr/bin/env python
"""Session-8 Phase 3: the seven meta-judging analyses.

Inputs ($0 — logs already extracted + OAuth raw grade files):
  analysis/20260717-session8-replay-rows.jsonl   (panel values, molds, strata)
  analysis/20260717-session8-j4-raw.jsonl        (J4 = claude-opus-4-8 OAuth)
  analysis/20260717-session8-j5-raw.jsonl        (J5 = gpt-5.5 codex OAuth)
  analysis/20260717-session8-contamination-raw.jsonl  (optional, analysis 7)

Output: analysis/20260717-session8-meta-judging-stats.json

Analyses (s8 boot prompt):
  1 house-style deltas vs incumbent panel median (by mold / SUT)
  2 five-judge reliability (pairwise Spearman / ICC(2,k) / MAD, by mold)
  3 headline sensitivity — gpt-5-mini vs haiku paired gap + MDD80 (=2.80*SE,
    s7 convention, epochs-averaged) under each judge config.  FRAMING RULE
    (pre-stated): single-judge rows are GAP-STABILITY evidence only; the
    5-judge median is the one potentially tighter re-derivation.
  4 cross-kin DiD: d = J4-J5; tau = (dbar_haiku - dbar_qwen) -
    (dbar_gpt5mini - dbar_qwen); item-clustered bootstrap CI (5000 reps)
  5 top-10 s7 discriminators: per-SUT spread under panel vs J4 vs J5
  6 GATE-cap consistency (<=40 signal agreement)
  7 contamination bound (style-normalized re-grade delta), if file present
"""
from __future__ import annotations

import json
import math
import random
import statistics as st
from collections import defaultdict
from itertools import combinations
from pathlib import Path

V2 = Path(__file__).resolve().parent.parent
A = V2 / "analysis"
ROWS = A / "20260717-session8-replay-rows.jsonl"
OUT = A / "20260717-session8-meta-judging-stats.json"
SEED = 1337
N_BOOT = 5000
JUDGES = ["gemini", "deepseek", "mistral_small", "J4", "J5"]
HEAD_SUTS = {"gpt-5-mini": "gpt5mini", "claude-haiku-4.5": "haiku",
             "qwen3.7-plus": "qwen"}
TOP10 = ["COMP-N-015", "COMP-N-020", "CONT-N-022", "COMP-N-008", "COMP-N-022",
         "COMP-N-004", "COMP-N-007", "COMP-N-023", "COMP-N-024", "COMP-N-021"]


def jload(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def latest_grades(path: Path) -> dict[str, int]:
    """sample_key -> grade (latest record wins; parse-fails excluded)."""
    out = {}
    for rec in jload(path):
        if rec.get("grade") is not None:
            out[rec["sample_key"]] = rec["grade"]
    return out


def mean(xs):
    return st.mean(xs) if xs else None


def rnd(x, nd=2):
    return round(x, nd) if x is not None else None


# ---------------------------------------------------------------- reliability
def ranks(xs: list[float]) -> list[float]:
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    rk = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            rk[order[k]] = avg
        i = j + 1
    return rk


def pearson(a, b):
    n = len(a)
    ma, mb = st.mean(a), st.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    da = math.sqrt(sum((x - ma) ** 2 for x in a))
    db = math.sqrt(sum((y - mb) ** 2 for y in b))
    return num / (da * db) if da and db else None


def spearman(a, b):
    return pearson(ranks(a), ranks(b))


def icc2k(matrix: list[list[float]]):
    """ICC(2,k): two-way random, absolute agreement, average of k raters."""
    n = len(matrix)
    k = len(matrix[0])
    if n < 2:
        return None
    grand = st.mean([v for row in matrix for v in row])
    row_m = [st.mean(r) for r in matrix]
    col_m = [st.mean([matrix[i][j] for i in range(n)]) for j in range(k)]
    ss_rows = k * sum((m - grand) ** 2 for m in row_m)
    ss_cols = n * sum((m - grand) ** 2 for m in col_m)
    ss_tot = sum((v - grand) ** 2 for row in matrix for v in row)
    ss_err = ss_tot - ss_rows - ss_cols
    msr = ss_rows / (n - 1)
    msc = ss_cols / (k - 1)
    mse = ss_err / ((n - 1) * (k - 1))
    denom = msr + (msc - mse) / n
    return (msr - mse) / denom if denom else None


# ------------------------------------------------------------------- pairwise
def paired_gap(item_means_a: dict, item_means_b: dict):
    """s7 convention: per-item diff -> gap, SE, MDD80=2.80*SE."""
    common = sorted(set(item_means_a) & set(item_means_b))
    if len(common) < 2:
        return None
    diffs = [item_means_a[x] - item_means_b[x] for x in common]
    se = st.stdev(diffs) / math.sqrt(len(diffs))
    g = st.mean(diffs)
    return {"n": len(common), "gap": rnd(g), "se_diff": rnd(se),
            "mdd80": rnd(2.80 * se),
            "significant_at_mdd80": bool(abs(g) >= 2.80 * se)}


def main() -> int:
    rows = {r["sample_key"]: r for r in jload(ROWS)}
    j4 = latest_grades(A / "20260717-session8-j4-raw.jsonl")
    j5 = latest_grades(A / "20260717-session8-j5-raw.jsonl")

    # judge grade accessor: incumbents ride in panel values
    def g(key: str, judge: str):
        r = rows[key]
        if judge == "J4":
            return j4.get(key)
        if judge == "J5":
            return j5.get(key)
        idx = {"gemini": 0, "deepseek": 1, "mistral_small": 2}[judge]
        v = r["panel"]["values"][idx]
        return v if isinstance(v, (int, float)) else None

    def pmed(key: str):
        vals = [v for v in rows[key]["panel"]["values"]
                if isinstance(v, (int, float))]
        return st.median(vals) if vals else None

    twin = sorted(k for k in rows if k in j4 and k in j5)
    j4_all = sorted(k for k in rows if k in j4)
    out = {
        "bank_version": "v2.4",
        "panel": "median(gemini-2.5-flash, deepseek-chat, mistral-small-2603)",
        "parser": "last-match GRADE: N (harness regex)",
        "n_rows": len(rows), "n_j4": len(j4), "n_j5": len(j5),
        "n_twin": len(twin),
        "framing": "EXPLORATORY / NON-QUOTABLE; single-judge headline rows are "
                   "gap-stability evidence only (no significance claims); "
                   "5-judge median is the sensitivity anchor",
    }

    # --- parse-fail rates -------------------------------------------------
    pf = {}
    for tag in ("j4", "j5"):
        recs = jload(A / f"20260717-session8-{tag}-raw.jsonl")
        n_pf = sum(1 for r in recs if r.get("parse_fail"))
        n_retry = sum(1 for r in recs if r.get("attempt") == 2
                      and not r.get("parse_fail"))
        pf[tag.upper()] = {"n_records": len(recs), "parse_fail": n_pf,
                           "recovered_on_reminder_retry": n_retry}
    out["parse_stats"] = pf

    # --- 1 house-style ----------------------------------------------------
    def house(keys, judges):
        res = {}
        for j in judges:
            ds = [(g(k, j) - pmed(k), rows[k]) for k in keys
                  if g(k, j) is not None and pmed(k) is not None]
            by_mold, by_sut = defaultdict(list), defaultdict(list)
            for d, r in ds:
                by_mold[r["mold"]].append(d)
                by_sut[r["sut_short"]].append(d)
            res[j] = {
                "n": len(ds), "overall": rnd(mean([d for d, _ in ds])),
                "by_mold": {m: rnd(mean(v)) for m, v in sorted(by_mold.items())},
                "by_sut": {s: rnd(mean(v)) for s, v in sorted(by_sut.items())},
            }
        return res
    out["house_style_twin"] = house(twin, JUDGES)
    out["house_style_j4_superset"] = house(j4_all, ["J4"])
    out["s5_baseline_reference"] = {
        "gemini": {"overall": -6.48, "contested": -11.2, "anchor": -15.7},
        "deepseek": {"overall": 1.18}, "mistral_small": {"overall": 1.95},
        "source": "analysis/20260716-session5-panel-health.json (cited, "
                  "not recomputed; different sample base)"}

    # --- 2 five-judge reliability ----------------------------------------
    def reliability(keys):
        keys = [k for k in keys
                if all(g(k, j) is not None for j in JUDGES)]
        if len(keys) < 3:
            return {"n": len(keys)}
        mat = [[g(k, j) for j in JUDGES] for k in keys]
        pair = {}
        for a, b in combinations(range(len(JUDGES)), 2):
            va = [m[a] for m in mat]
            vb = [m[b] for m in mat]
            pair[f"{JUDGES[a]}~{JUDGES[b]}"] = {
                "spearman": rnd(spearman(va, vb), 3),
                "mad": rnd(mean([abs(x - y) for x, y in zip(va, vb)])),
            }
        return {"n": len(keys), "icc2k": rnd(icc2k(mat), 3), "pairwise": pair}
    rel = {"overall": reliability(twin)}
    for m in ("contested", "complicit", "steadfast", "v1-kind"):
        rel[m] = reliability([k for k in twin if rows[k]["mold"] == m])
    out["reliability"] = rel

    # --- 3 headline sensitivity ------------------------------------------
    core = [k for k in rows if rows[k]["stratum"] == "S1-epochs-core"]

    def config_item_means(score_fn, keys):
        per = defaultdict(lambda: defaultdict(list))  # sut_tag -> item -> vals
        for k in keys:
            r = rows[k]
            tag = HEAD_SUTS.get(r["sut_short"])
            if tag is None:
                continue
            v = score_fn(k)
            if v is not None:
                per[tag][r["item_id"]].append(v)
        return {t: {i: st.mean(v) for i, v in items.items()}
                for t, items in per.items()}

    def headline(score_fn, keys, label):
        im = config_item_means(score_fn, keys)
        res = {"epochs_note": {
            t: rnd(mean([len_ for len_ in
                         [len([k for k in keys
                               if rows[k]["item_id"] == i
                               and HEAD_SUTS.get(rows[k]["sut_short"]) == t
                               and score_fn(k) is not None])
                          for i in im.get(t, {})]]), 2)
            for t in im}}
        for a, b in (("gpt5mini", "haiku"), ("gpt5mini", "qwen"),
                     ("haiku", "qwen")):
            if a in im and b in im:
                res[f"{a}-vs-{b}"] = paired_gap(im[a], im[b])
        means = {t: rnd(mean(list(v.values()))) for t, v in im.items()}
        res["sut_means"] = means
        return res

    sens = {}
    sens["panel3_reference"] = headline(pmed, core, "panel3")
    for j in ("gemini", "deepseek", "mistral_small"):
        sens[f"{j}_alone"] = headline(lambda k, j=j: g(k, j), core, j)
    sens["J4_alone"] = headline(lambda k: g(k, "J4"), core, "J4")
    sens["J5_alone"] = headline(lambda k: g(k, "J5"), core, "J5")

    def med5(k):
        vals = [g(k, j) for j in JUDGES]
        vals = [v for v in vals if v is not None]
        return st.median(vals) if len(vals) == 5 else None
    sens["median5"] = headline(med5, core, "median5")
    out["headline_sensitivity"] = sens

    # --- 4 cross-kin DiD --------------------------------------------------
    def build_dd(epoch1_only: bool):
        dd_ = defaultdict(lambda: defaultdict(list))  # tag -> item -> [d]
        for k in twin:
            r = rows[k]
            tag = HEAD_SUTS.get(r["sut_short"])
            if tag is None or r["stratum"] != "S1-epochs-core":
                continue
            if epoch1_only and r["epoch"] != 1:
                continue
            dd_[tag][r["item_id"]].append(j4[k] - j5[k])
        return dd_

    def tau_from(dd_):
        db = {t: mean([d for it in dd_.get(t, {}).values() for d in it])
              for t in ("haiku", "gpt5mini", "qwen")}
        if any(v is None for v in db.values()):
            return None, db
        # NOTE: the qwen anchor cancels algebraically -> tau == dbar_haiku -
        # dbar_gpt5mini. qwen is a displayed sanity baseline, not a numerical
        # identifier in tau. The DiD form is kept for interpretive framing.
        return ((db["haiku"] - db["qwen"]) - (db["gpt5mini"] - db["qwen"]),
                db)

    def did_block(epoch1_only: bool):
        dd_ = build_dd(epoch1_only)
        tau_o, db = tau_from(dd_)
        items = sorted(set().union(*[set(v) for v in dd_.values()])) \
            if dd_ else []
        rng_ = random.Random(SEED)
        bt = []
        for _ in range(N_BOOT):
            pick = [rng_.choice(items) for _ in items] if items else []
            bdd = {t: defaultdict(list) for t in dd_}
            for bi, it in enumerate(pick):
                for t in dd_:
                    if it in dd_[t]:
                        bdd[t][f"{it}#{bi}"] = dd_[t][it]
            tb, _ = tau_from(bdd)
            if tb is not None:
                bt.append(tb)
        bt.sort()
        ci_ = ([rnd(bt[int(0.025 * len(bt))], 3),
                rnd(bt[int(0.975 * len(bt))], 3)] if bt else None)
        n_by_sut = {t: sum(len(v) for v in dd_.get(t, {}).values())
                    for t in ("haiku", "gpt5mini", "qwen")}
        return {
            "n_items_clustered": len(items),
            "n_twin_core_samples": sum(n_by_sut.values()),
            "n_by_sut": n_by_sut,
            "dbar_by_sut": {t: rnd(v, 3) for t, v in db.items()},
            "component_anthropic_kin": rnd(db["haiku"] - db["qwen"], 3)
                if None not in (db.get("haiku"), db.get("qwen")) else None,
            "component_openai_kin": rnd(db["gpt5mini"] - db["qwen"], 3)
                if None not in (db.get("gpt5mini"), db.get("qwen")) else None,
            "tau_obs": rnd(tau_o, 3) if tau_o is not None else None,
            "tau_ci95_item_clustered": ci_, "n_boot": len(bt),
        }

    default_did = did_block(epoch1_only=False)
    e1_did = did_block(epoch1_only=True)
    out["cross_kin_did"] = {
        "design": "d = J4-J5 per twin epochs-core sample; tau = "
                  "(dbar_haiku - dbar_qwen) - (dbar_gpt5mini - dbar_qwen); "
                  "positive tau = symmetric mutual in-group favoritism",
        "identification_caveat": "tau reduces algebraically to dbar_haiku - "
            "dbar_gpt5mini (the qwen anchor cancels); qwen is a displayed "
            "baseline only. tau conflates kin favoritism with any J4-vs-J5 x "
            "SUT-pair interaction and rests on ONE (twin-difference) "
            "instrument, so 'CI excludes zero' is itself an inferential claim "
            "carrying the single-instrument caveat.",
        **default_did,
        "epochs_imbalance_note": "DEFAULT variant: qwen J5 coverage is epoch-1 "
            "only (n=" + str(default_did["n_by_sut"]["qwen"]) + ") vs haiku/"
            "gpt-5-mini epochs 1-3 (n=" + str(default_did["n_by_sut"]["haiku"])
            + " each). The displayed qwen dbar + kin components are therefore "
            "epoch-imbalanced; they do NOT enter tau (anchor cancellation). "
            "tau's two real terms (haiku, gpt5mini) are epoch-balanced.",
        "robustness_epoch1_only": e1_did,
    }

    # --- 5 top-10 discriminator artifact check ---------------------------
    disc = {}
    for it in TOP10:
        keys = [k for k in core if rows[k]["item_id"] == it]
        entry = {}
        for label, fn in (("panel3", pmed),
                          ("J4", lambda k: g(k, "J4")),
                          ("J5", lambda k: g(k, "J5"))):
            per_sut = defaultdict(list)
            for k in keys:
                v = fn(k)
                if v is not None:
                    per_sut[HEAD_SUTS.get(rows[k]["sut_short"], "?")].append(v)
            m = {t: rnd(mean(v)) for t, v in sorted(per_sut.items())}
            entry[label] = {"per_sut": m,
                            "spread": rnd(max(m.values()) - min(m.values()))
                            if len(m) == 3 else None}
        disc[it] = entry
    out["top10_discriminators"] = disc

    # --- 6 GATE-cap consistency ------------------------------------------
    cap_keys = [k for k in twin
                if any(isinstance(v, (int, float)) and v <= 40
                       for v in rows[k]["panel"]["values"])]
    cap = {"n_cap_eligible_twin": len(cap_keys),
           "definition": "any incumbent grade <=40 on the sample"}
    sig = {}
    for j in JUDGES:
        vals = [g(k, j) for k in cap_keys]
        ok = [v for v in vals if v is not None]
        sig[j] = [1 if v <= 40 else 0 for v in ok]
        cap[f"rate_{j}"] = rnd(mean(sig[j]), 3) if ok else None
    agree = {}
    for a, b in combinations(JUDGES, 2):
        if sig.get(a) and sig.get(b) and len(sig[a]) == len(sig[b]):
            agree[f"{a}~{b}"] = rnd(
                mean([1 if x == y else 0
                      for x, y in zip(sig[a], sig[b])]), 3)
    cap["cap_signal_agreement"] = agree
    out["gate_cap"] = cap

    # --- 7 contamination bound (optional input) --------------------------
    contam_path = A / "20260717-session8-j4-contamination-raw.jsonl"
    if contam_path.exists():
        cg = latest_grades(contam_path)
        ds = [cg[k] - j4[k] for k in cg if k in j4]
        out["contamination_bound"] = {
            "method": "style-normalized [BEGIN MODEL RESPONSE] span "
                      "(markdown stripped), re-graded with J4; delta = "
                      "normalized - original",
            "n": len(ds), "mean_delta": rnd(mean(ds)),
            "mean_abs_delta": rnd(mean([abs(d) for d in ds])),
            "max_abs_delta": max((abs(d) for d in ds), default=None),
            "explicit_tell_scan": "0/779 prompts contain model/vendor "
                                  "self-identification strings",
        }
    else:
        out["contamination_bound"] = {"status": "pending",
                                      "explicit_tell_scan": "0/779"}

    OUT.write_text(json.dumps(out, indent=1))
    print(json.dumps({k: out[k] for k in
                      ("n_rows", "n_j4", "n_j5", "n_twin", "parse_stats")},
                     indent=1))
    hs = out["headline_sensitivity"]
    for cfg in ("panel3_reference", "gemini_alone", "deepseek_alone",
                "mistral_small_alone", "J4_alone", "J5_alone", "median5"):
        p = hs.get(cfg, {}).get("gpt5mini-vs-haiku")
        if p:
            print(f"{cfg:22s} gap {p['gap']:6.2f}  MDD80 {p['mdd80']:5.2f}  "
                  f"{'SIG' if p['significant_at_mdd80'] else 'ns'}  n={p['n']}")
    ck = out["cross_kin_did"]
    print(f"tau {ck['tau_obs']}  CI {ck['tau_ci95_item_clustered']}  "
          f"dbar {ck['dbar_by_sut']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
