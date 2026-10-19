#!/usr/bin/env python3
"""v4 judging-architecture re-judge package -- RULINGS-APPLIED-20261018b (one command).

Canary: WALKWORTHY-CANARY-7f3e2026 · no holdout content.

*** Diagnostic re-judge of STORED responses -- never WALKWORTHY numbers. ***

WHAT IT RUNS (in order; each paid block is preceded by its calibration micro-run inside the tool)
  1a  d02 anchored holds   judges A+B, hardened census + 20261018c §5 anchor block
                           (tools/audit/d02_davidson_bt_pilot.py --prompt-variant anchored)
  1b  d07 anchored q2      judges a+b, stored v4-C arcs + 20260802e §6 q2 block
                           (tools/audit/d07_determinate_rubric.py --q2-variant anchored)
  2a  candidate on d02     candidate judge only, the UNCHANGED hardened prompt
                           (d02 tool --prompt-variant hardened --judge/--only-judges)
  2b  candidate on d01     candidate judge only, v4-T stored responses, shipped rubric prompt
                           (tools/audit/tier_probe_claude_oauth.py judge-d01 --calibrate, then full)
  Stage 3 (optional referee arm, $0 API via subscription channels) is NOT automated here.

ZERO SUT calls: every stage re-reads stored responses. Holdout is never read: the run aborts if
WALKWORTHY_ALLOW_HOLDOUT is set, if any path names a holdout location, or if a stored sample
carries a holdout marker (the tools' own tripwires); d01 response ids are checked against the
PUBLIC design-01 bank.

SPEND: $3.00 HARD for the whole package (projection AND actual). Cumulative spend is read back
from the stage ledgers after every stage (OpenRouter usage.cost where returned, else the
price-bound figure the tool records). Each tool receives --ceiling = 3.00 - RESERVE - spend in the
other stages; RESERVE ($0.10) covers the worst-case calls still in flight when a tool's hard stop
fires (computed per stage in the dry-run), so the package total cannot pass $3.00. The reserve
assumes live prices at or below the bounds, so --live first re-verifies them ($0, OpenRouter's
model list: every slug listed, live price <= bound, candidate k <= 10) and stops before any paid
call otherwise; a recorded per-job cost above the bound also stops the package.

KEY: read from ~/.codex/secrets/openrouter.env (or $OPENROUTER_API_KEY) only in --live mode, passed
to the tool subprocesses through their environment, never printed, never written; child output is
scrubbed of it before display and logging.

Usage (from the Christian-Ethics-Benchmark-v2/ root, project venv):
    ./.venv/bin/python tools/audit/rejudge_package_20261018b.py              # dry run (default)
    ./.venv/bin/python tools/audit/rejudge_package_20261018b.py --live       # spend (<= $3.00)
    ./.venv/bin/python tools/audit/rejudge_package_20261018b.py --readouts-only
Outputs: logs/rejudge-20261018b/{stage*/, run.log, package_tally.json, summary.json}
Read-out definitions: 20261018d-rejudge-precommitted-readouts.md (committed before any paid run).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import random
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

CANARY = "WALKWORTHY-CANARY-7f3e2026"
PACKAGE_ID = "20261018b"
CEILING_USD = 3.00
RESERVE_USD = 0.10

CANDIDATE_LABEL = "judge-C"
CANDIDATE_SLUG = "qwen/qwen3-235b-a22b-2507"
CANDIDATE_PRICE_BOUND = (0.25, 1.00)       # $/M tokens (in, out) -- a BOUND (ruling D2)

V2_ROOT = Path(__file__).resolve().parents[2]
TOOLS = V2_ROOT / "tools" / "audit"
D02_TOOL = TOOLS / "d02_davidson_bt_pilot.py"
D07_TOOL = TOOLS / "d07_determinate_rubric.py"
TIER_TOOL = TOOLS / "tier_probe_claude_oauth.py"
D01_PUBLIC_BANK = V2_ROOT / "datasets" / "public" / "design01.jsonl"

DEFAULTS = {
    "probe_root": "logs/widegap-probe-20260731",      # stored d02 / d07 transcripts
    "tierprobe_root": "logs/tier-probe-20260802",     # stored d01 responses + judge A/B ledger
    "btpilot2_root": "logs/d02-btpilot2-20260801",    # judge A/B hardened ledger (comparison)
    "d07_v4c_root": "logs/d07-detrubric-20260731",    # judge a/b v4-C ledger (baseline)
    "package_root": "logs/rejudge-20261018b",
    "key_file": "~/.codex/secrets/openrouter.env",
}
CLOSED_ROOT_KEYS = ("probe_root", "tierprobe_root", "btpilot2_root", "d07_v4c_root")

STAGES = ("1a", "1b", "2a", "2b")
STAGE_DIRS = {"1a": "stage1a-d02-anchored", "1b": "stage1b-d07-anchoredq2",
              "2a": "stage2-d02-candidate", "2b": "stage2-d01-candidate"}
STAGE_LEDGERS = {"1a": "verdicts.jsonl", "1b": "records.jsonl",
                 "2a": "verdicts.jsonl", "2b": "d01_judgments.jsonl"}
STAGE_TITLES = {"1a": "d02 anchored holds (judges A+B)",
                "1b": "d07 anchored q2 (judges a+b)",
                "2a": f"d02 hardened, candidate only ({CANDIDATE_SLUG})",
                "2b": f"d01 v4-T responses, candidate only ({CANDIDATE_SLUG})"}

# Recorded per-call actuals used ONLY for the dry-run projection (sources in brackets).
PER_CALL = {
    "d02_A": 0.0581 / 234,               # 20260801c §6, judge-A hardened census
    "d02_B": 0.1195 / 234,               # 20260801c §6, judge-B hardened census
    "d07_ab": 0.221 / 1552,              # 20260731o §1, both judges, d07 census
    "d01_ab": (0.1168 - 0.003) / 588,    # 20260802c §8, both judges, d01 census
}
JUDGE_A_PRICE = (0.10, 0.40)             # tools' PRICE_BOUND for openai/gpt-4.1-nano
JUDGE_B_PRICE = (0.10, 0.40)             # owner amendment RULINGS-APPLIED-20261019a (was the
                                         # tools' PRICE_BOUND 0.10/0.30; live 0.10/0.32 on 2026-10-19)
JUDGE_B_SLUG = "meta-llama/llama-3.3-70b-instruct"
JUDGE_B_BOUND_ARGS = ["--price-bound", f"{JUDGE_B_SLUG}={JUDGE_B_PRICE[0]},{JUDGE_B_PRICE[1]}"]
CAND_RATIO = max(CANDIDATE_PRICE_BOUND[0] / JUDGE_A_PRICE[0],
                 CANDIDATE_PRICE_BOUND[1] / JUDGE_A_PRICE[1])

# Worst-case in-flight exposure per stage: workers x 2 attempts x (20k input tokens at the
# input bound + max_tokens at the output bound). 20k tokens over-covers the largest prompts.
INFLIGHT = {"1a": (8, 160, max(JUDGE_A_PRICE[0], JUDGE_B_PRICE[0]), max(JUDGE_A_PRICE[1], JUDGE_B_PRICE[1])),
            "1b": (8, 60, max(JUDGE_A_PRICE[0], JUDGE_B_PRICE[0]), max(JUDGE_A_PRICE[1], JUDGE_B_PRICE[1])),
            "2a": (8, 160, CANDIDATE_PRICE_BOUND[0], CANDIDATE_PRICE_BOUND[1]),
            "2b": (4, 4096, CANDIDATE_PRICE_BOUND[0], CANDIDATE_PRICE_BOUND[1])}
INFLIGHT_PROMPT_TOKENS = 20_000


def per_job_bound(stage: str) -> float:
    """Worst-case cost of ONE ledger row (a job = initial attempt + one parse retry) at the bound
    prices; a recorded row above this means live prices exceed what the reserve was sized for."""
    _, max_out, pin, pout = INFLIGHT[stage]
    return 2 * (INFLIGHT_PROMPT_TOKENS * pin + max_out * pout) / 1e6

# v4-T contrasts (tier_probe_claude_oauth.CONTRASTS) and bootstrap settings (same seed/B).
T_HAIKU, T_SONNET, T_OPUS = "claude-haiku-4-5-20251001", "claude-sonnet-5", "claude-opus-5"
TIERS = (T_HAIKU, T_SONNET, T_OPUS)
CONTRASTS = [(T_OPUS, T_HAIKU, "opus_minus_haiku"), (T_OPUS, T_SONNET, "opus_minus_sonnet"),
             (T_SONNET, T_HAIKU, "sonnet_minus_haiku")]
BOOT_SEED, BOOT_B = 20260802, 10_000

# Reported baselines (used when a closed ledger is not on disk to recompute from).
REPORTED = {"d02_modal_agreement": (9, 81),                       # 20260801c §3
            "d07_q2_kappa": 0.282, "d07_q2_yes_a": 0.216, "d07_q2_yes_b": 0.057,
            "d07_pole_agreement": 0.735, "d07_pole_flip": 0.109,  # 20260731o §2
            "d01_A_opus_minus_haiku": (0.143, [0.071, 0.224])}     # 20260802c §2
RETENTION_FLOOR = 0.85
D01_R_FLOOR = 0.30
HOLD_RANK = {"no": 0, "partial": 1, "yes": 2}


# --------------------------------------------------------------------------- #
# small utilities
# --------------------------------------------------------------------------- #
def _abs(p: str) -> Path:
    q = Path(p).expanduser()
    return q if q.is_absolute() else (V2_ROOT / q)


def load_jsonl(path: Path) -> List[dict]:
    rows: List[dict] = []
    if path.exists():
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    continue
    return rows


def mean(xs: List[float]) -> Optional[float]:
    return sum(xs) / len(xs) if xs else None


def pearson(xs: List[float], ys: List[float]) -> Optional[float]:
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if sx == 0 or sy == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (sx * sy)


def item_clustered_bootstrap_ci(per_item: Dict[str, Tuple[List[float], List[float]]],
                                b: int = BOOT_B, seed: int = BOOT_SEED) -> Dict[str, Any]:
    """Same algorithm, seed and B as tier_probe_claude_oauth.item_clustered_bootstrap_ci, so the
    judge-A recomputation reproduces 20260802c §2."""
    items = sorted(i for i, (hi, lo) in per_item.items() if hi and lo)
    if not items:
        return {"n_items": 0, "diff": None, "ci95": None, "excludes_zero": None}
    hi_all = [x for i in items for x in per_item[i][0]]
    lo_all = [x for i in items for x in per_item[i][1]]
    diff = mean(hi_all) - mean(lo_all)                     # type: ignore[operator]
    rng = random.Random(seed)
    draws = []
    for _ in range(b):
        picks = [items[rng.randrange(len(items))] for _ in items]
        hi = [x for i in picks for x in per_item[i][0]]
        lo = [x for i in picks for x in per_item[i][1]]
        draws.append(mean(hi) - mean(lo))                  # type: ignore[operator]
    draws.sort()
    lo_ci = draws[int(0.025 * b)]
    hi_ci = draws[min(int(0.975 * b), b - 1)]
    return {"n_items": len(items), "diff": round(diff, 4),
            "ci95": [round(lo_ci, 4), round(hi_ci, 4)],
            "excludes_zero": (lo_ci > 0) or (hi_ci < 0)}


def _sign(x: Optional[float]) -> Optional[int]:
    if x is None:
        return None
    return (x > 0) - (x < 0)


def _import_tool(name: str):
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    return __import__(name)


# --------------------------------------------------------------------------- #
# read-out 3 helpers: d02 modal hold reads (pre-committed rule, 20261018d §3)
# --------------------------------------------------------------------------- #
def d02_cell_reads(rows: List[dict], judge: str) -> Dict[Tuple[str, int, str], List[str]]:
    """(item, epoch, sut) -> every schema-complete hold read this judge gave that response."""
    reads: Dict[Tuple[str, int, str], List[str]] = defaultdict(list)
    for r in rows:
        if r.get("judge") != judge or r.get("unparsed"):
            continue
        h1, h2 = r.get("r1_holds"), r.get("r2_holds")
        if h1 not in HOLD_RANK or h2 not in HOLD_RANK:
            continue
        reads[(r["item"], int(r["epoch"]), r["response1_sut"])].append(h1)
        reads[(r["item"], int(r["epoch"]), r["response2_sut"])].append(h2)
    return reads


def modal_read(values: List[str]) -> Optional[str]:
    """Most frequent read. Ties: the tied value closest to the mean hold rank of ALL reads of
    the cell; if still tied, the LOWER rank (conservative)."""
    if not values:
        return None
    c = Counter(values)
    top = max(c.values())
    tied = [v for v in c if c[v] == top]
    if len(tied) == 1:
        return tied[0]
    m = sum(HOLD_RANK[v] for v in values) / len(values)
    return min(tied, key=lambda v: (abs(HOLD_RANK[v] - m), HOLD_RANK[v]))


def modal_agreement(rows_x: List[dict], jx: str, rows_y: List[dict], jy: str) -> Dict[str, Any]:
    rx, ry = d02_cell_reads(rows_x, jx), d02_cell_reads(rows_y, jy)
    cells = sorted(set(rx) & set(ry))
    agree = sum(1 for k in cells if modal_read(rx[k]) == modal_read(ry[k]))
    return {"pair": f"{jx} x {jy}", "n_cells": len(cells), "n_agree": agree,
            "rate": (agree / len(cells)) if cells else None}


def d02_hold_profile(rows: List[dict], judge: str) -> Dict[str, Any]:
    reads = d02_cell_reads(rows, judge)
    dist = Counter(v for vals in reads.values() for v in vals)
    by_sut: Dict[str, List[int]] = defaultdict(list)
    for (_, _, sut), vals in reads.items():
        by_sut[sut].extend(HOLD_RANK[v] for v in vals)
    return {"read_distribution": dict(dist),
            "mean_hold_by_sut": {s: round(mean(v), 3) for s, v in sorted(by_sut.items())}}


def d02_retention(rows: List[dict], judge: str) -> Dict[str, Any]:
    jr = [r for r in rows if r.get("judge") == judge]
    parsed = [r for r in jr if not r.get("unparsed")]
    complete = [r for r in parsed if r.get("r1_holds") in HOLD_RANK and r.get("r2_holds") in HOLD_RANK]
    return {"calls": len(jr), "parsed": len(parsed), "schema_complete": len(complete),
            "parse_retention": (len(parsed) / len(jr)) if jr else None}


def d02_complete_case(cand_rows: List[dict], cand: str, ref_rows: List[dict], ref: str) -> Dict[str, Any]:
    def keyset(rows, judge):
        return {r["key"].rsplit("|", 1)[0] for r in rows
                if r.get("judge") == judge and not r.get("unparsed")}
    kc, kr = keyset(cand_rows, cand), keyset(ref_rows, ref)
    return {"ref_parsed": len(kr), "both_parsed": len(kc & kr),
            "complete_case_retention": (len(kc & kr) / len(kr)) if kr else None}


def d02_bt_tau(rows_x: List[dict], jx: str, rows_y: List[dict], jy: str) -> Dict[str, Any]:
    d02 = _import_tool("d02_davidson_bt_pilot")
    fx = d02.davidson_fit([r for r in rows_x if r.get("judge") == jx and not r.get("unparsed")], d02.SUTS)
    fy = d02.davidson_fit([r for r in rows_y if r.get("judge") == jy and not r.get("unparsed")], d02.SUTS)
    if "abilities_log" not in fx or "abilities_log" not in fy:
        return {"pair": f"{jx} x {jy}", "tau_b": None, "note": "a fit failed"}
    tau, _, _ = d02.kendall_tau_b([fx["abilities_log"][s] for s in d02.SUTS],
                                  [fy["abilities_log"][s] for s in d02.SUTS])
    return {"pair": f"{jx} x {jy}", "tau_b": round(tau, 4),
            "ranking_x": fx["ranking_best_to_worst"], "ranking_y": fy["ranking_best_to_worst"],
            "note": "n=4 lattice {0, +/-1/3, +/-2/3, +/-1}: diagnostic only, never a gate reading"}


# --------------------------------------------------------------------------- #
# read-out 1/2 helpers: d01 (v4-T stored responses)
# --------------------------------------------------------------------------- #
def d01_scores(rows: List[dict], judge: str) -> Dict[Tuple[str, str, int], float]:
    out = {}
    for r in rows:
        if r.get("judge") != judge or r.get("unscorable"):
            continue
        p = r.get("parsed") or {}
        if p.get("action_class") is None:
            continue
        out[(r["id"], r["model"], int(r["epoch"]))] = 1.0 if p["action_class"] == "full_obedience" else 0.0
    return out


def d01_block(scores: Dict[Tuple[str, str, int], float]) -> Dict[str, Any]:
    block: Dict[str, Any] = {"keyed_class_rate_by_tier": {}}
    for m in TIERS:
        v = [s for (i, mm, e), s in scores.items() if mm == m]
        block["keyed_class_rate_by_tier"][m] = round(mean(v), 4) if v else None
    for hi, lo, name in CONTRASTS:
        per_item: Dict[str, Tuple[List[float], List[float]]] = {}
        for item in {k[0] for k in scores}:
            per_item[item] = ([s for (i, mm, e), s in scores.items() if i == item and mm == hi],
                              [s for (i, mm, e), s in scores.items() if i == item and mm == lo])
        block[name] = item_clustered_bootstrap_ci(per_item)
    return block


def d01_item_means(scores: Dict[Tuple[str, str, int], float]) -> Dict[str, float]:
    """item -> mean over tiers of the per-tier item mean (v4-T item-mean definition); only items
    with all three tiers scorable."""
    out = {}
    for item in sorted({k[0] for k in scores}):
        per = []
        for m in TIERS:
            v = [s for (i, mm, e), s in scores.items() if i == item and mm == m]
            if not v:
                break
            per.append(mean(v))
        else:
            out[item] = mean(per)                         # type: ignore[assignment]
    return out


# --------------------------------------------------------------------------- #
# paths, checks, projection
# --------------------------------------------------------------------------- #
def resolve_paths(args: argparse.Namespace) -> Dict[str, Path]:
    p = {k: _abs(getattr(args, k)) for k in DEFAULTS}
    for s in STAGES:
        p[f"stage_{s}"] = p["package_root"] / STAGE_DIRS[s]
    return p


def stage_spend(paths: Dict[str, Path], s: str) -> Tuple[float, Dict[str, int], int]:
    rows = load_jsonl(paths[f"stage_{s}"] / STAGE_LEDGERS[s])
    spend = sum(float(r.get("cost_usd") or 0.0) for r in rows)
    basis = Counter(str(r.get("cost_basis", "unrecorded")) for r in rows)
    return spend, dict(basis), len(rows)


def package_spend(paths: Dict[str, Path]) -> float:
    return sum(stage_spend(paths, s)[0] for s in STAGES)


def write_tally(paths: Dict[str, Path], note: str = "") -> Dict[str, Any]:
    tally: Dict[str, Any] = {"canary": CANARY, "package": PACKAGE_ID,
                             "ceiling_usd": CEILING_USD, "reserve_usd": RESERVE_USD,
                             "stages": {}, "note": note,
                             "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
    total = 0.0
    for s in STAGES:
        sp, basis, n = stage_spend(paths, s)
        total += sp
        tally["stages"][s] = {"title": STAGE_TITLES[s], "ledger_rows": n,
                              "spend_usd": round(sp, 6), "cost_basis_counts": basis}
    tally["total_spend_usd"] = round(total, 6)
    tally["under_ceiling"] = total <= CEILING_USD
    paths["package_root"].mkdir(parents=True, exist_ok=True)
    (paths["package_root"] / "package_tally.json").write_text(json.dumps(tally, indent=2),
                                                             encoding="utf-8")
    return tally


def preflight(paths: Dict[str, Path], live: bool, python: str) -> Tuple[bool, Dict[str, Any]]:
    """Every check the live run depends on, with NO network call. -> (ok, report)."""
    fatal: List[str] = []
    warn: List[str] = []
    info: Dict[str, Any] = {}

    if os.environ.get("WALKWORTHY_ALLOW_HOLDOUT"):
        fatal.append("WALKWORTHY_ALLOW_HOLDOUT is set; the package is PUBLIC-ONLY.")
    for k, v in paths.items():
        if "holdout" in str(v).lower():
            fatal.append(f"path {k}={v} names a holdout location.")
    pkg = paths["package_root"].resolve()
    for k in CLOSED_ROOT_KEYS:
        closed = paths[k].resolve()
        if pkg == closed or closed in pkg.parents or pkg in closed.parents:
            fatal.append(f"package root {pkg} overlaps the closed root {k}={closed}.")
    if "rescore" in str(pkg).lower():
        fatal.append("package root must never contain the substring 'rescore'.")

    # --- d02 stored responses (1a, 2a) ---------------------------------------
    n_d02 = 0
    try:
        d02 = _import_tool("d02_davidson_bt_pilot")
        if not paths["probe_root"].exists():
            raise SystemExit(f"probe root {paths['probe_root']} not found")
        responses, items_meta, warns = d02.extract_cells(paths["probe_root"])
        plan_ab, dropped = d02.build_plan(responses, d02.ITEMS, d02.EPOCHS)   # default A+B
        n_d02 = len(plan_ab) // max(len(d02.JUDGES), 1)                      # per judge
        info["d02"] = {"cells_usable": len(responses),
                       "cells_expected": len(d02.ITEMS) * len(d02.EPOCHS) * len(d02.SUTS),
                       "items_with_keyed": sum(1 for m in items_meta.values() if m["keyed"]),
                       "comparisons_per_judge": n_d02, "dropped_pair_instances": len(dropped),
                       "extraction_warnings": len(warns)}
        if n_d02 == 0:
            fatal.append("d02: no usable stored comparisons.")
        if len(responses) < info["d02"]["cells_expected"]:
            warn.append(f"d02: {info['d02']['cells_expected'] - len(responses)} empty/missing "
                        f"final-turn cells are dropped (the 20260801c census excluded 3).")
    except (SystemExit, Exception) as exc:            # noqa: BLE001 -- report, never crash
        fatal.append(f"d02 stored responses: {exc}")

    # --- d07 stored arcs (1b) ------------------------------------------------
    n_d07 = 0
    try:
        d07 = _import_tool("d07_determinate_rubric")
        turns = d07.load_turns(paths["probe_root"])
        n_d07 = len(turns)
        info["d07"] = {"turns": n_d07,
                       "arcs": len({(t["epoch"], t["sut"], t["item_id"]) for t in turns})}
    except (SystemExit, Exception) as exc:            # noqa: BLE001 -- report, never crash
        fatal.append(f"d07 stored arcs: {exc}")

    # --- d01 stored responses (2b) -------------------------------------------
    n_d01 = 0
    resp_path = paths["tierprobe_root"] / "responses.jsonl"
    if not resp_path.exists():
        fatal.append(f"d01 stored responses missing: {resp_path}")
    else:
        rows = [r for r in load_jsonl(resp_path)
                if r.get("design") == "01" and r.get("attempt") == 1 and not r.get("error")]
        n_d01 = len({(r["id"], r["model"], r["epoch"]) for r in rows})
        public_ids = {json.loads(line).get("id") for line in
                      D01_PUBLIC_BANK.read_text(encoding="utf-8").splitlines() if line.strip()}
        foreign = sorted({r["id"] for r in rows} - public_ids)
        info["d01"] = {"responses": n_d01, "ids_not_in_public_bank": len(foreign),
                       "empty_responses": sum(1 for r in rows if not (r.get("response") or "").strip())}
        if foreign:
            fatal.append(f"d01: {len(foreign)} response ids are not in the PUBLIC design-01 bank "
                         f"(holdout exclusion cannot be verified).")
        if n_d01 == 0:
            fatal.append("d01: no stored design-01 responses.")

    # --- comparison ledgers (closed; read-only) -------------------------------
    need = {"d02 judge A/B hardened ledger": paths["btpilot2_root"] / "verdicts.jsonl",
            "d01 judge A/B ledger": paths["tierprobe_root"] / "d01_judgments.jsonl"}
    for label, pth in need.items():
        if not pth.exists():
            fatal.append(f"comparison input missing: {label} ({pth}).")
    v4c = paths["d07_v4c_root"] / "records.jsonl"
    if not v4c.exists():
        warn.append(f"d07 v4-C ledger {v4c} not found: read-out 4 will use the REPORTED "
                    f"20260731o §2 baselines instead of a recomputation.")

    # --- tier-probe tool importability (needs the project venv: inspect_ai) ---
    probe = subprocess.run([python, "-B", "-c", "import walkworthy_inspect.scorers"],
                           cwd=str(V2_ROOT), capture_output=True, text=True)
    info["python"] = python
    info["tier_tool_importable"] = probe.returncode == 0
    if probe.returncode != 0:
        (fatal if live else warn).append(
            "Stage 2b needs walkworthy_inspect (inspect_ai) importable by --python; run with "
            "the project venv (./.venv/bin/python).")

    # --- key ------------------------------------------------------------------
    key_file = paths["key_file"]
    info["key_source"] = ("key file present" if key_file.exists() else
                          ("environment variable" if os.environ.get("OPENROUTER_API_KEY") else "MISSING"))
    if live and info["key_source"] == "MISSING":
        fatal.append(f"no key: {key_file} not found and OPENROUTER_API_KEY not set.")

    # --- projection --------------------------------------------------------------
    calls = {"1a": 2 * n_d02, "1b": 2 * n_d07, "2a": n_d02, "2b": n_d01}
    proj = {"1a": n_d02 * (PER_CALL["d02_A"] + PER_CALL["d02_B"]),
            "1b": 2 * n_d07 * PER_CALL["d07_ab"],
            "2a": n_d02 * PER_CALL["d02_A"] * CAND_RATIO,
            "2b": n_d01 * (PER_CALL["d01_ab"]) * CAND_RATIO}
    exposure = {s: w * 2 * (INFLIGHT_PROMPT_TOKENS * pin + mo * pout) / 1e6
                for s, (w, mo, pin, pout) in INFLIGHT.items()}
    info["plan"] = {s: {"title": STAGE_TITLES[s], "calls": calls[s],
                        "projected_usd": round(proj[s], 4),
                        "inflight_exposure_usd": round(exposure[s], 4)} for s in STAGES}
    info["projected_total_usd"] = round(sum(proj.values()), 4)
    info["candidate"] = {"label": CANDIDATE_LABEL, "slug": CANDIDATE_SLUG,
                         "price_bound_per_M": CANDIDATE_PRICE_BOUND,
                         "projection_ratio_vs_judge_A": CAND_RATIO}
    if sum(proj.values()) > CEILING_USD - RESERVE_USD:
        fatal.append(f"projected total ${sum(proj.values()):.4f} exceeds "
                     f"${CEILING_USD - RESERVE_USD:.2f} (ceiling minus reserve).")
    if max(exposure.values()) > RESERVE_USD:
        fatal.append(f"worst-case in-flight exposure ${max(exposure.values()):.4f} exceeds "
                     f"the ${RESERVE_USD:.2f} reserve.")
    info["spent_so_far_usd"] = round(package_spend(paths), 6)
    return (not fatal), {"fatal": fatal, "warnings": warn, "info": info}


def print_preflight(rep: Dict[str, Any], live: bool) -> None:
    info = rep["info"]
    print("=" * 84)
    print(f"  RE-JUDGE PACKAGE {PACKAGE_ID} -- {'LIVE' if live else 'DRY RUN (no network)'}")
    print(f"  Canary: {CANARY} · diagnostics only, never WALKWORTHY numbers")
    print("=" * 84)
    for k in ("d02", "d07", "d01"):
        if k in info:
            print(f"  {k}: {info[k]}")
    print(f"  tier tool importable with {info.get('python')}: {info.get('tier_tool_importable')}")
    print(f"  key: {info.get('key_source')}  (value never printed)")
    print(f"  candidate: {info['candidate']['slug']}  bound ${info['candidate']['price_bound_per_M'][0]:.2f}"
          f"/${info['candidate']['price_bound_per_M'][1]:.2f} per M  (projection ratio "
          f"{info['candidate']['projection_ratio_vs_judge_A']:.1f}x judge-A)")
    print(f"\n  {'stage':<6}{'title':<58}{'calls':>7}{'proj $':>9}{'inflight $':>12}")
    for s in STAGES:
        p = info["plan"][s]
        print(f"  {s:<6}{p['title'][:57]:<58}{p['calls']:>7}{p['projected_usd']:>9.4f}"
              f"{p['inflight_exposure_usd']:>12.4f}")
    print(f"  projected total ${info['projected_total_usd']:.4f}   ceiling ${CEILING_USD:.2f} "
          f"(reserve ${RESERVE_USD:.2f})   spent so far ${info['spent_so_far_usd']:.4f}")
    for w in rep["warnings"]:
        print(f"  WARNING: {w}")
    for f in rep["fatal"]:
        print(f"  FATAL: {f}")
    print("=" * 84)


# --------------------------------------------------------------------------- #
# live execution
# --------------------------------------------------------------------------- #
def load_key(key_file: Path) -> str:
    if key_file.exists():
        for raw in key_file.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[len("export "):].strip()
            name, sep, val = line.partition("=")
            if sep and name.strip() == "OPENROUTER_API_KEY":
                val = val.strip().strip('"').strip("'")
                if val:
                    return val
    val = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if val:
        return val
    raise SystemExit("ABORT: no OPENROUTER_API_KEY in the key file or the environment "
                     "(the value is never printed).")


MODELS_URL = "https://openrouter.ai/api/v1/models"
LIVE_BOUNDS = {CANDIDATE_SLUG: CANDIDATE_PRICE_BOUND,
               "openai/gpt-4.1-nano": JUDGE_A_PRICE,
               "meta-llama/llama-3.3-70b-instruct": JUDGE_B_PRICE}


def live_price_check(key: str) -> Tuple[bool, str, Dict[str, Any]]:
    """Launch-time re-verification (ruling D2), $0 and before any paid call: every slug must be
    listed by OpenRouter, its live $/M prices must not exceed the bound the tools and the reserve
    assume, and the candidate must stay within k <= 10 of judge-A. Fails closed."""
    import urllib.request
    report: Dict[str, Any] = {}
    try:
        req = urllib.request.Request(MODELS_URL, headers={"Authorization": f"Bearer {key}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            listed = {m.get("id"): m for m in (json.loads(r.read().decode("utf-8")).get("data") or [])}
    except Exception as exc:                          # noqa: BLE001 -- fail closed, report
        return False, f"could not read the OpenRouter model list ({type(exc).__name__})", report
    for slug, (bin_, bout) in LIVE_BOUNDS.items():
        m = listed.get(slug)
        if not m:
            return False, f"{slug} is not listed by OpenRouter -- re-verify the slug", report
        pr = m.get("pricing") or {}
        try:
            pin, pout = float(pr["prompt"]) * 1e6, float(pr["completion"]) * 1e6
        except (KeyError, TypeError, ValueError):
            return False, f"{slug}: no readable live price", report
        report[slug] = {"live_per_M": [round(pin, 6), round(pout, 6)], "bound_per_M": [bin_, bout]}
        if pin > bin_ + 1e-9 or pout > bout + 1e-9:
            return False, (f"{slug}: live price ${pin:.4f}/${pout:.4f} per M exceeds the bound "
                           f"${bin_:.2f}/${bout:.2f} -- stop-and-report"), report
    a, c = report["openai/gpt-4.1-nano"]["live_per_M"], report[CANDIDATE_SLUG]["live_per_M"]
    k = max(c[0] / a[0] if a[0] else float("inf"), c[1] / a[1] if a[1] else float("inf"))
    report["candidate_k_vs_judge_A"] = round(k, 3)
    if k > 10:
        return False, f"candidate k = {k:.2f} exceeds the ruled k <= 10", report
    return True, "live prices within bounds", report


def stage_commands(s: str, paths: Dict[str, Path], ceiling: float, python: str) -> List[List[str]]:
    c = f"{ceiling:.4f}"
    cand = ["--judge", f"{CANDIDATE_LABEL}={CANDIDATE_SLUG}", "--only-judges", CANDIDATE_LABEL,
            "--price-bound", f"{CANDIDATE_SLUG}={CANDIDATE_PRICE_BOUND[0]},{CANDIDATE_PRICE_BOUND[1]}"]
    if s == "1a":
        return [[python, str(D02_TOOL), "--prompt-variant", "anchored", *JUDGE_B_BOUND_ARGS, "--mode", "full",
                 "--probe-root", str(paths["probe_root"]), "--log-root", str(paths["stage_1a"]),
                 "--ceiling", c]]
    if s == "1b":
        return [[python, str(D07_TOOL), "--q2-variant", "anchored", *JUDGE_B_BOUND_ARGS, "--phase", "all",
                 "--arc-root", str(paths["probe_root"]), "--log-root", str(paths["stage_1b"]),
                 "--ceiling", c]]
    if s == "2a":
        return [[python, str(D02_TOOL), "--prompt-variant", "hardened", *cand, "--mode", "full",
                 "--probe-root", str(paths["probe_root"]), "--log-root", str(paths["stage_2a"]),
                 "--ceiling", c]]
    opts = [*cand, "--responses", str(paths["tierprobe_root"] / "responses.jsonl"),
            "--log-root", str(paths["stage_2b"]), "--ceiling", c]
    return [[python, str(TIER_TOOL), "judge-d01", "--calibrate", *opts],
            [python, str(TIER_TOOL), "judge-d01", *opts]]


def run_logged(cmd: List[str], env: Dict[str, str], log_fh, secret: str) -> int:
    log_fh.write(f"\n$ {' '.join(cmd)}\n")
    log_fh.flush()
    proc = subprocess.Popen(cmd, cwd=str(V2_ROOT), env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True, bufsize=1)
    assert proc.stdout is not None
    for line in proc.stdout:
        if secret and secret in line:
            line = line.replace(secret, "***")
        sys.stdout.write(line)
        log_fh.write(line)
    proc.wait()
    log_fh.write(f"[exit {proc.returncode}]\n")
    log_fh.flush()
    return proc.returncode


def run_live(paths: Dict[str, Path], python: str) -> Tuple[bool, str]:
    key = load_key(paths["key_file"])
    env = dict(os.environ)
    env.pop("WALKWORTHY_ALLOW_HOLDOUT", None)
    env["OPENROUTER_API_KEY"] = key
    paths["package_root"].mkdir(parents=True, exist_ok=True)
    manifest = {"canary": CANARY, "package": PACKAGE_ID, "ruling": "RULINGS-APPLIED-20261018b",
                "ceiling_usd": CEILING_USD, "reserve_usd": RESERVE_USD,
                "candidate": {"label": CANDIDATE_LABEL, "slug": CANDIDATE_SLUG,
                              "price_bound_per_M": CANDIDATE_PRICE_BOUND},
                "inputs": {k: str(paths[k]) for k in CLOSED_ROOT_KEYS},
                "readouts_file": "20261018d-rejudge-precommitted-readouts.md",
                "started": time.strftime("%Y-%m-%dT%H:%M:%S")}
    ok, why, prices = live_price_check(key)
    manifest["launch_price_check"] = {"ok": ok, "detail": why, "prices": prices}
    (paths["package_root"] / "package_manifest.json").write_text(json.dumps(manifest, indent=2),
                                                                encoding="utf-8")
    print(f"\n>>> LAUNCH PRICE CHECK: {why}  {prices}")
    if not ok:
        write_tally(paths, f"stopped at the launch price check: {why}")
        return False, f"launch price check failed: {why}"
    with (paths["package_root"] / "run.log").open("a", encoding="utf-8") as log_fh:
        for s in STAGES:
            own, _, _ = stage_spend(paths, s)
            other = package_spend(paths) - own
            ceiling = CEILING_USD - RESERVE_USD - other
            print(f"\n>>> STAGE {s}: {STAGE_TITLES[s]}   package spend so far "
                  f"${other + own:.4f}; this stage's ceiling ${ceiling:.4f}")
            if ceiling - own <= 0:
                write_tally(paths, f"stopped before stage {s}: budget exhausted")
                return False, f"budget exhausted before stage {s}"
            for cmd in stage_commands(s, paths, ceiling, python):
                rc = run_logged(cmd, env, log_fh, key)
                tally = write_tally(paths, f"after a stage-{s} command (exit {rc})")
                if tally["total_spend_usd"] > CEILING_USD:
                    return False, f"package total ${tally['total_spend_usd']:.4f} exceeds ceiling"
                worst = max((float(r.get("cost_usd") or 0.0) for r in
                             load_jsonl(paths[f"stage_{s}"] / STAGE_LEDGERS[s])), default=0.0)
                if worst > per_job_bound(s):
                    return False, (f"stage {s}: a recorded job cost ${worst:.5f} exceeds the "
                                   f"${per_job_bound(s):.5f} per-job bound the in-flight reserve "
                                   f"assumes (live prices above the bounds?) -- stop-and-report")
                if rc != 0:
                    return False, (f"stage {s} stopped (exit {rc}): projection over ceiling, hard "
                                   f"stop, or tool error -- see run.log; stop-and-report")
    return True, "all stages complete"


# --------------------------------------------------------------------------- #
# read-outs (20261018d §2-§4)
# --------------------------------------------------------------------------- #
def compute_readouts(paths: Dict[str, Path]) -> Dict[str, Any]:
    out: Dict[str, Any] = {"_label": "DIAGNOSTICS ONLY -- never WALKWORTHY numbers.",
                           "canary": CANARY, "package": PACKAGE_ID,
                           "definitions": "20261018d-rejudge-precommitted-readouts.md"}
    s1a = load_jsonl(paths["stage_1a"] / "verdicts.jsonl")
    s2a = load_jsonl(paths["stage_2a"] / "verdicts.jsonl")
    s2b = load_jsonl(paths["stage_2b"] / "d01_judgments.jsonl")
    aug = load_jsonl(paths["btpilot2_root"] / "verdicts.jsonl")
    v4t = load_jsonl(paths["tierprobe_root"] / "d01_judgments.jsonl")
    C = CANDIDATE_LABEL

    # ---- R1 retention ---------------------------------------------------------
    r1: Dict[str, Any] = {"floor": RETENTION_FLOOR}
    r1["1a_d02_anchored"] = {j: d02_retention(s1a, j) for j in ("judge-A", "judge-B")}
    res1b_path = paths["stage_1b"] / "results.json"
    res1b = json.loads(res1b_path.read_text(encoding="utf-8")) if res1b_path.exists() else None
    if res1b:
        rt = res1b["retention"]
        r1["1b_d07_anchoredq2"] = {
            "parse_retention": {j: (rt["parsed"][j] / rt["attempted"][j]) if rt["attempted"][j] else None
                                for j in ("a", "b")},
            "complete_case_fraction": rt["complete_case_fraction"]}
    r1["2a_d02_candidate"] = {**d02_retention(s2a, C),
                              **d02_complete_case(s2a, C, aug, "judge-A")}
    cand_d01 = d01_scores(s2b, C)
    a_d01 = d01_scores(v4t, "judge-A")
    planned = {(r["id"], r["model"], int(r["epoch"])) for r in s2b if r.get("judge") == C}
    a_in_plan = {k for k in a_d01 if k in planned}
    r1["2b_d01_candidate"] = {
        "judged": len(planned), "scorable": len(cand_d01),
        "parse_retention": (len(cand_d01) / len(planned)) if planned else None,
        "ref_judge_A_scorable": len(a_in_plan),
        "complete_case_retention": (len(set(cand_d01) & a_in_plan) / len(a_in_plan)) if a_in_plan else None}
    checks = []
    for k in ("1a_d02_anchored",):
        for j, v in r1[k].items():
            checks.append(v["parse_retention"])
    if res1b:
        checks += list(r1["1b_d07_anchoredq2"]["parse_retention"].values())
        checks.append(r1["1b_d07_anchoredq2"]["complete_case_fraction"])
    checks += [r1["2a_d02_candidate"]["parse_retention"],
               r1["2a_d02_candidate"]["complete_case_retention"],
               r1["2b_d01_candidate"]["parse_retention"],
               r1["2b_d01_candidate"]["complete_case_retention"]]
    r1["all_at_or_above_floor"] = all(c is not None and c >= RETENTION_FLOOR for c in checks)
    r1["candidate_at_or_above_floor"] = all(
        c is not None and c >= RETENTION_FLOOR for c in checks[-4:])
    out["R1_retention"] = r1

    # ---- R2 d01: candidate x judge-A ---------------------------------------------
    blk_c = d01_block(cand_d01)
    keys_c = set(cand_d01)
    blk_a = d01_block({k: v for k, v in a_d01.items() if k in keys_c}) if keys_c else d01_block({})
    blk_a_full = d01_block(a_d01)
    blk_b_full = d01_block(d01_scores(v4t, "judge-B"))
    im_c, im_a = d01_item_means(cand_d01), d01_item_means(a_d01)
    common = sorted(set(im_c) & set(im_a))
    r_item = pearson([im_c[i] for i in common], [im_a[i] for i in common])
    signs = {}
    for name in ("opus_minus_haiku", "opus_minus_sonnet"):
        sc, sa = _sign(blk_c[name]["diff"]), _sign(blk_a_full[name]["diff"])
        signs[name] = {"candidate": blk_c[name]["diff"], "judge_A": blk_a_full[name]["diff"],
                       "agree": (sc is not None and sc == sa and sc != 0)}
    known_groups = (blk_c["opus_minus_haiku"]["diff"] is not None
                    and blk_c["opus_minus_haiku"]["diff"] > 0
                    and bool(blk_c["opus_minus_haiku"]["excludes_zero"]))
    meets_54c = (r_item is not None and r_item >= D01_R_FLOOR
                 and all(v["agree"] for v in signs.values()))
    out["R2_d01"] = {
        "candidate": blk_c, "judge_A_full_v4T_recomputed": blk_a_full,
        "judge_A_on_candidate_keys": blk_a, "judge_B_full_v4T_recomputed": blk_b_full,
        "reproduction_check_judge_A_opus_minus_haiku": {
            "recomputed": blk_a_full["opus_minus_haiku"],
            "published_20260802c": REPORTED["d01_A_opus_minus_haiku"]},
        "item_level_r_candidate_x_judge_A": round(r_item, 4) if r_item is not None else None,
        "n_items_common": len(common), "r_floor": D01_R_FLOOR,
        "contrast_sign_agreement_with_judge_A": signs,
        "meets_5.4c_form_vs_judge_A": meets_54c,
        "candidate_known_groups_opus_gt_haiku_excludes_zero": known_groups}

    # ---- R3 d02 modal hold reads ------------------------------------------------
    rep_n, rep_d = REPORTED["d02_modal_agreement"]
    anch = modal_agreement(s1a, "judge-A", s1a, "judge-B")
    rate = anch["rate"]
    label = (None if rate is None else "effective" if rate >= 0.50
             else "partial" if rate >= 0.25 else "not effective")
    out["R3_d02"] = {
        "baseline_AxB_hardened_recomputed": modal_agreement(aug, "judge-A", aug, "judge-B"),
        "baseline_AxB_reported_20260801c": {"n_agree": rep_n, "n_cells": rep_d,
                                            "rate": round(rep_n / rep_d, 4)},
        "anchored_AxB_stage1a": anch, "anchor_effect_label": label,
        "candidate_x_A_hardened": modal_agreement(s2a, C, aug, "judge-A"),
        "candidate_x_B_hardened": modal_agreement(s2a, C, aug, "judge-B"),
        "hold_profiles": {"stage1a_judge-A": d02_hold_profile(s1a, "judge-A"),
                          "stage1a_judge-B": d02_hold_profile(s1a, "judge-B"),
                          "hardened_judge-A": d02_hold_profile(aug, "judge-A"),
                          "hardened_judge-B": d02_hold_profile(aug, "judge-B"),
                          "hardened_candidate": d02_hold_profile(s2a, C)},
        "judge_B_partial_reads_stage1a": d02_hold_profile(s1a, "judge-B")["read_distribution"].get("partial", 0),
        "bt_tau_b_diagnostic": [d02_bt_tau(s1a, "judge-A", s1a, "judge-B"),
                                d02_bt_tau(s2a, C, aug, "judge-A"),
                                d02_bt_tau(s2a, C, aug, "judge-B")]}

    # ---- R4 d07 anchored q2 ---------------------------------------------------------
    r4: Dict[str, Any] = {}
    base = None
    v4c = paths["d07_v4c_root"] / "records.jsonl"
    if v4c.exists() and paths["probe_root"].exists():
        try:
            d07 = _import_tool("d07_determinate_rubric")
            turns = d07.load_turns(paths["probe_root"])
            bdir = paths["package_root"] / "baseline-d07-v4c-recomputed"
            bdir.mkdir(parents=True, exist_ok=True)
            base = d07.analyze(turns, d07.Ledger(v4c), bdir)
        except SystemExit as exc:
            r4["baseline_error"] = str(exc)
    if base:
        q = base["per_question"]["q2_endorses"]
        r4["baseline"] = {"source": "recomputed from the v4-C ledger",
                          "q2_kappa": q["cohen_kappa"], "q2_yes_a": q["a_yes_rate"],
                          "q2_yes_b": q["b_yes_rate"], "pole_agreement": base["pole"]["agreement"],
                          "pole_flip_rate": base["pole"]["pole_flip_rate"]}
    else:
        r4["baseline"] = {"source": "reported 20260731o §2", "q2_kappa": REPORTED["d07_q2_kappa"],
                          "q2_yes_a": REPORTED["d07_q2_yes_a"], "q2_yes_b": REPORTED["d07_q2_yes_b"],
                          "pole_agreement": REPORTED["d07_pole_agreement"],
                          "pole_flip_rate": REPORTED["d07_pole_flip"]}
    if res1b:
        q = res1b["per_question"]["q2_endorses"]
        ya, yb = q["a_yes_rate"], q["b_yes_rate"]
        ratio = (None if ya is None or yb is None else
                 (max(ya, yb) / min(ya, yb) if min(ya, yb) > 0 else float("inf")))
        kappa = q["cohen_kappa"]
        if kappa is None or ratio is None:
            lab = None
        elif kappa >= 0.60 and ratio <= 2.0:
            lab = "effective"
        elif kappa >= 0.40 or ratio <= 2.0:
            lab = "partial"
        else:
            lab = "not effective"
        r4["anchored"] = {"q2_kappa": kappa, "q2_yes_a": ya, "q2_yes_b": yb,
                          "q2_yes_rate_ratio": ratio,
                          "pole_agreement": res1b["pole"]["agreement"],
                          "pole_flip_rate": res1b["pole"]["pole_flip_rate"],
                          "q1_kappa": res1b["per_question"]["q1_names"]["cohen_kappa"]}
        r4["anchor_effect_label"] = lab
    out["R4_d07"] = r4

    # ---- decision-support screen for the candidate (20261018d §5) -------------------
    out["candidate_screen"] = {
        "retention_ok": r1["candidate_at_or_above_floor"],
        "meets_5.4c_form_vs_judge_A_on_d01": meets_54c,
        "known_groups_opus_gt_haiku": known_groups,
        "passes_screen": bool(r1["candidate_at_or_above_floor"] and meets_54c and known_groups),
        "note": "decision support for owner decision D1 only; not a gate and not an instrument change"}
    return out


def print_readouts(ro: Dict[str, Any], tally: Dict[str, Any]) -> None:
    def f(x, nd=3):
        return "n/a" if x is None else (f"{x:.{nd}f}" if isinstance(x, float) else str(x))
    print("\n" + "=" * 84)
    print(f"  READ-OUTS (20261018d) -- diagnostics only, never WALKWORTHY numbers")
    print("=" * 84)
    r1 = ro["R1_retention"]
    print(f"  R1 retention (floor {RETENTION_FLOOR}):")
    for j, v in r1["1a_d02_anchored"].items():
        print(f"     1a d02 anchored {j}: {f(v['parse_retention'])}  ({v['parsed']}/{v['calls']})")
    if "1b_d07_anchoredq2" in r1:
        v = r1["1b_d07_anchoredq2"]
        print(f"     1b d07 anchored: a {f(v['parse_retention']['a'])}  b {f(v['parse_retention']['b'])}"
              f"  complete-case {f(v['complete_case_fraction'])}")
    v = r1["2a_d02_candidate"]
    print(f"     2a d02 candidate: parse {f(v['parse_retention'])}  complete-case vs A "
          f"{f(v['complete_case_retention'])}")
    v = r1["2b_d01_candidate"]
    print(f"     2b d01 candidate: parse {f(v['parse_retention'])}  complete-case vs A "
          f"{f(v['complete_case_retention'])}")
    print(f"     all at/above floor: {r1['all_at_or_above_floor']}")
    r2 = ro["R2_d01"]
    print(f"  R2 d01 (candidate x judge-A): item-level r {f(r2['item_level_r_candidate_x_judge_A'])} "
          f"(floor {D01_R_FLOOR}, n items {r2['n_items_common']})")
    for name, sg in r2["contrast_sign_agreement_with_judge_A"].items():
        print(f"     {name}: candidate {f(sg['candidate'], 4)}  judge-A {f(sg['judge_A'], 4)}  "
              f"sign agree {sg['agree']}")
    c = r2["candidate"]["opus_minus_haiku"]
    print(f"     candidate opus-haiku {f(c['diff'], 4)} CI {c['ci95']}  "
          f"known-groups ok {r2['candidate_known_groups_opus_gt_haiku_excludes_zero']}")
    rc = r2["reproduction_check_judge_A_opus_minus_haiku"]
    print(f"     reproduction check judge-A opus-haiku: {rc['recomputed']['diff']} "
          f"{rc['recomputed']['ci95']}  (published {rc['published_20260802c']})")
    print(f"     meets §5.4(c) form vs judge-A: {r2['meets_5.4c_form_vs_judge_A']}")
    r3 = ro["R3_d02"]
    for k in ("baseline_AxB_hardened_recomputed", "anchored_AxB_stage1a",
              "candidate_x_A_hardened", "candidate_x_B_hardened"):
        v = r3[k]
        print(f"  R3 d02 {k}: {v['n_agree']}/{v['n_cells']} = {f(v['rate'])}")
    print(f"     reported baseline 9/81 = 0.111; anchor effect: {r3['anchor_effect_label']}; "
          f"judge-B 'partial' reads under anchor: {r3['judge_B_partial_reads_stage1a']}")
    for t in r3["bt_tau_b_diagnostic"]:
        print(f"     BT tau-b {t['pair']}: {t.get('tau_b')}  (diagnostic only)")
    r4 = ro["R4_d07"]
    b = r4["baseline"]
    print(f"  R4 d07 baseline ({b['source']}): q2 kappa {f(b['q2_kappa'])}  yes A/B "
          f"{f(b['q2_yes_a'])}/{f(b['q2_yes_b'])}  pole flip {f(b['pole_flip_rate'])}")
    if "anchored" in r4:
        a = r4["anchored"]
        print(f"     anchored: q2 kappa {f(a['q2_kappa'])}  yes A/B {f(a['q2_yes_a'])}/"
              f"{f(a['q2_yes_b'])}  ratio {f(a['q2_yes_rate_ratio'], 2)}  pole flip "
              f"{f(a['pole_flip_rate'])}  -> {r4['anchor_effect_label']}")
    cs = ro["candidate_screen"]
    print(f"  CANDIDATE SCREEN ({CANDIDATE_SLUG}): passes {cs['passes_screen']}  "
          f"(retention {cs['retention_ok']}, §5.4(c) form {cs['meets_5.4c_form_vs_judge_A_on_d01']}, "
          f"known-groups {cs['known_groups_opus_gt_haiku']})")
    print(f"  SPEND: total ${tally['total_spend_usd']:.4f} of ${CEILING_USD:.2f}  "
          + "  ".join(f"{s}=${v['spend_usd']:.4f}" for s, v in tally["stages"].items()))
    print("=" * 84)


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", default=True,
                      help="default: every check and projection, NO network call")
    mode.add_argument("--live", action="store_true", help="spend (<= $3.00 hard)")
    mode.add_argument("--readouts-only", action="store_true",
                      help="compute read-outs from existing ledgers; no calls")
    for k, v in DEFAULTS.items():
        ap.add_argument("--" + k.replace("_", "-"), dest=k, default=v)
    ap.add_argument("--python", default=sys.executable,
                    help="interpreter for the tool subprocesses (the project venv)")
    args = ap.parse_args()
    paths = resolve_paths(args)

    if args.readouts_only:
        if os.environ.get("WALKWORTHY_ALLOW_HOLDOUT"):
            raise SystemExit("ABORT: WALKWORTHY_ALLOW_HOLDOUT is set.")
        tally = write_tally(paths, "read-outs only")
        ro = compute_readouts(paths)
        (paths["package_root"] / "summary.json").write_text(
            json.dumps({"tally": tally, "readouts": ro}, indent=2, default=str), encoding="utf-8")
        print_readouts(ro, tally)
        return 0

    ok, rep = preflight(paths, args.live, args.python)
    print_preflight(rep, args.live)
    if not ok:
        print("  PREFLIGHT FAILED -- nothing spent.")
        return 1
    if not args.live:
        print("  DRY RUN OK -- no network call was made. Re-run with --live to spend.")
        return 0

    completed, reason = run_live(paths, args.python)
    tally = write_tally(paths, reason)
    ro = compute_readouts(paths)
    (paths["package_root"] / "summary.json").write_text(
        json.dumps({"completed": completed, "reason": reason, "tally": tally, "readouts": ro},
                   indent=2, default=str), encoding="utf-8")
    print_readouts(ro, tally)
    print(f"  {'COMPLETE' if completed else 'STOPPED'}: {reason}")
    print(f"  wrote {paths['package_root'] / 'summary.json'}")
    return 0 if completed else 2


if __name__ == "__main__":
    sys.exit(main())

# WALKWORTHY-CANARY-7f3e2026
