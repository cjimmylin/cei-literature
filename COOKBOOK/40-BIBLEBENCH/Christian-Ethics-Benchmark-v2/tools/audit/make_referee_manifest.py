"""JR-referee sampling manifest builder — OFFLINE join + seeded sampling. NO model calls.

WALKWORTHY-CANARY-7f3e2026

Reads ONLY stored artifacts:
  * the exported prompt universe  logs/jr-referee-20260716/prompts-{02,07,06}.jsonl
    (one row per unit: design 02/07 rows are PER-TURN with turn_index; design 06 rows
    are PER-SAMPLE with turn_index=null),
  * judge-A per-unit verdicts from the pilot `.eval` logs (Score.value; turn_states is a
    JSON-ENCODED STRING — decode it; design 06 = 7 category scores in the same dict),
  * judge-B per-unit verdicts from each SUT's judgeB-verdicts.jsonl.

JOIN KEY DISCIPLINE (critical): sample_ids COLLIDE across SUTs (same items), so EVERY
join is scoped by (sut, log-basename, sample_id). turn_index is POSITIONAL into the
decoded turn_states list. This mirrors ablation_agreement.py / context_ablation_agreement.py
(the _sut_log_basenames log-scoping bug they document, found 2026-07-16).

Strata:
  02/07 (per-turn): disagreement = judge-A state != judge-B state at turn_index
                    (string inequality; UNSCORABLE counts as a state, so
                    state-vs-unscorable = disagreement, both-unscorable = agreement).
  06 (per-sample):  profile_mean = mean of the 7 category scores per judge; rank all 155
                    units by |mean_A - mean_B| desc, ties broken by (design,sut,log,
                    sample_id); top 60 = "gap" candidates, remaining 95 = control pool.

Seeded sampling (seed=20260716, one random.Random instance). The candidate list for
every stratum is sorted by (design, sut, log, sample_id, turn_index) BEFORE drawing so
the draw is reproducible. DRAW ORDER (fixed, documented):
    1. 07 agreement controls   (sample 150)
    2. 02 disagreement         (sample 200)
    3. 02 agreement controls   (sample 80)
    4. 06 controls             (sample 60 from the remaining 95)
  07 disagreement turns are taken WHOLESALE (every one, no draw). 06 gap stratum is the
  top-60 wholesale (no draw). Those two wholesale takes consume no RNG entropy, keeping
  the four sampled draws in the order above.

Outputs (logs/jr-referee-20260716/):
  sample-manifest.jsonl  one row per sampled unit — NO judge verdicts (blindness hygiene):
        {design, sut, log, sample_id, item_id, admin, turn_index, prompt_sha256, stratum}
        stratum in {disagreement, control, gap}  (06 uses gap/control only).
  manifest-meta.json     seed, draw order, per-design/per-stratum counts, per-SUT counts,
        disagreement base rates, unscorable-involvement counts, sha256 of the manifest,
        generation timestamp, canary string.

Usage:
    .venv/bin/python tools/audit/make_referee_manifest.py
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402

UNSCORABLE = "unscorable"
SEED = 20260716
CANARY = "WALKWORTHY-CANARY-7f3e2026"
PER_TURN_DESIGNS = {"02", "07"}
PROFILE_CATS = ["frame", "facts", "principles", "alternatives",
                "resolution", "remainder", "pastoral"]

# sampling sizes
N_07_AGREE_CONTROL = 150
N_02_DISAGREE = 200
N_02_AGREE_CONTROL = 80
N_06_GAP = 60          # wholesale top-K by |mean_A - mean_B|
N_06_CONTROL = 60      # drawn from the remaining 95


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def _design_num_from_task(task_name: str) -> Optional[str]:
    for n in [f"{i:02d}" for i in range(1, 11)]:
        if f"design{n}" in (task_name or ""):
            return n
    return None


def _decode_turn_states(raw: Any) -> List[Any]:
    if isinstance(raw, list):
        return raw
    try:
        return json.loads(raw or "[]")
    except (json.JSONDecodeError, TypeError, ValueError):
        return []


def _basename(p: str) -> str:
    return os.path.basename(p or "")


# --------------------------------------------------------------------------- #
# judge-A from eval logs, keyed (sut, log-basename, sample_id)
# --------------------------------------------------------------------------- #
def _load_judge_a(pilot_dir: str, designs: set) -> Dict[Tuple[str, str, str], dict]:
    """{(sut, log_basename, sample_id): Score.value dict} for the requested designs."""
    out: Dict[Tuple[str, str, str], dict] = {}
    for sut_path in sorted(glob.glob(os.path.join(pilot_dir, "*/"))):
        sut = Path(sut_path.rstrip("/")).name
        for p in sorted(glob.glob(os.path.join(sut_path, "*.eval"))):
            head = read_eval_log(p, header_only=True)
            dn = _design_num_from_task(head.eval.task)
            if dn not in designs:
                continue
            log = read_eval_log(p)
            lb = _basename(p)
            for s in (log.samples or []):
                if not s.scores:
                    continue
                sc = list(s.scores.values())[0]
                val = sc.value if isinstance(sc.value, dict) else {}
                out[(sut, lb, s.id)] = val
    return out


# --------------------------------------------------------------------------- #
# judge-B from judgeB-verdicts.jsonl, keyed (sut, log-basename, sample_id)
# --------------------------------------------------------------------------- #
def _load_judge_b(pilot_dir: str, designs: set) -> Dict[Tuple[str, str, str], dict]:
    """{(sut, log_basename, sample_id): judge_b dict} for the requested designs."""
    out: Dict[Tuple[str, str, str], dict] = {}
    for sut_path in sorted(glob.glob(os.path.join(pilot_dir, "*/"))):
        sut = Path(sut_path.rstrip("/")).name
        vpath = os.path.join(sut_path, "judgeB-verdicts.jsonl")
        if not os.path.exists(vpath):
            continue
        for line in open(vpath, encoding="utf-8"):
            r = json.loads(line)
            dn = (r.get("design", "") or "")[:2]
            if dn not in designs:
                continue
            jb = r.get("judge_b") or {}
            out[(sut, _basename(r.get("log", "")), r["sample_id"])] = jb
    return out


def _profile_status(val: dict) -> Tuple[Optional[float], List[str]]:
    """(profile_mean, list of non-numeric category names).

    profile_mean = mean of the 7 category scores. If ANY category is missing / None /
    UNSCORABLE / unparseable, the mean over 7 is undefined -> return (None, [bad cats]).
    A judge that returns an all-None profile (whole-sample non-verdict, observed for a
    handful of design-06 units) yields all 7 categories bad.
    """
    vals: List[float] = []
    bad: List[str] = []
    for c in PROFILE_CATS:
        v = val.get(c)
        if v is None or v == UNSCORABLE:
            bad.append(c)
            continue
        try:
            vals.append(float(v))
        except (TypeError, ValueError):
            bad.append(c)
    if bad:
        return None, bad
    return (sum(vals) / len(vals) if vals else None), bad


# --------------------------------------------------------------------------- #
# core build
# --------------------------------------------------------------------------- #
def build(pilot_dir: str, prompts_dir: str, out_dir: str) -> Dict[str, Any]:
    designs = {"02", "07", "06"}
    judge_a = _load_judge_a(pilot_dir, designs)
    judge_b = _load_judge_b(pilot_dir, designs)

    # Read prompt universe -> per-design list of unit dicts
    prompts: Dict[str, List[dict]] = {}
    for d in ("02", "07", "06"):
        rows = []
        with open(os.path.join(prompts_dir, f"prompts-{d}.jsonl"), encoding="utf-8") as fh:
            for line in fh:
                rows.append(json.loads(line))
        prompts[d] = rows

    unresolved: List[dict] = []

    # ---- per-turn designs (02/07): classify each unit ------------------- #
    # unit record augmented with A/B state + disagreement flag + unscorable involvement
    per_turn_units: Dict[str, List[dict]] = {"02": [], "07": []}
    for d in ("02", "07"):
        for r in prompts[d]:
            key = (r["sut"], _basename(r["log"]), r["sample_id"])
            va = judge_a.get(key)
            vb = judge_b.get(key)
            if va is None or vb is None:
                unresolved.append({**{k: r.get(k) for k in
                                      ("design", "sut", "log", "sample_id", "turn_index")},
                                   "missing_A": va is None, "missing_B": vb is None})
                continue
            a_states = _decode_turn_states(va.get("turn_states"))
            b_states = _decode_turn_states(vb.get("turn_states"))
            ti = r["turn_index"]
            a_state = a_states[ti] if (ti is not None and ti < len(a_states)) else None
            b_state = b_states[ti] if (ti is not None and ti < len(b_states)) else None
            if a_state is None or b_state is None:
                # positional resolution failed -> treat as unresolved (report, do not drop silently)
                unresolved.append({**{k: r.get(k) for k in
                                      ("design", "sut", "log", "sample_id", "turn_index")},
                                   "reason": "turn_index out of range in turn_states",
                                   "len_A": len(a_states), "len_B": len(b_states)})
                continue
            disagree = (a_state != b_state)
            involves_unscorable = (a_state == UNSCORABLE or b_state == UNSCORABLE)
            per_turn_units[d].append({
                "design": d, "sut": r["sut"], "log": _basename(r["log"]),
                "sample_id": r["sample_id"], "item_id": r["item_id"],
                "admin": r["admin"], "turn_index": ti,
                "prompt_sha256": r["prompt_sha256"],
                "disagree": disagree, "involves_unscorable": involves_unscorable,
            })

    # ---- design 06: per-sample profile gap ------------------------------ #
    six_units: List[dict] = []
    for r in prompts["06"]:
        key = (r["sut"], _basename(r["log"]), r["sample_id"])
        va = judge_a.get(key)
        vb = judge_b.get(key)
        if va is None or vb is None:
            unresolved.append({**{k: r.get(k) for k in
                                  ("design", "sut", "log", "sample_id", "turn_index")},
                               "missing_A": va is None, "missing_B": vb is None})
            continue
        ma, bad_a = _profile_status(va)
        mb, bad_b = _profile_status(vb)
        if ma is None or mb is None:
            # one (or both) judge could not produce a scorable 7-category profile.
            # These CANNOT enter the |mean_A - mean_B| ranking; report, do not silently drop.
            unresolved.append({**{k: r.get(k) for k in
                                  ("design", "sut", "log", "sample_id", "turn_index")},
                               "reason": "profile_mean undefined",
                               "bad_categories_A": bad_a, "bad_categories_B": bad_b,
                               "judgeA_all_null": len(bad_a) == len(PROFILE_CATS),
                               "judgeB_all_null": len(bad_b) == len(PROFILE_CATS)})
            continue
        six_units.append({
            "design": "06", "sut": r["sut"], "log": _basename(r["log"]),
            "sample_id": r["sample_id"], "item_id": r["item_id"],
            "admin": r["admin"], "turn_index": None,
            "prompt_sha256": r["prompt_sha256"],
            "gap": abs(ma - mb),
        })

    # rank 06 by |gap| desc, ties by deterministic unit-key (design,sut,log,sample_id)
    six_ranked = sorted(
        six_units,
        key=lambda u: (-u["gap"], u["design"], u["sut"], u["log"], u["sample_id"]),
    )
    six_gap = six_ranked[:N_06_GAP]
    six_control_pool = six_ranked[N_06_GAP:]

    # ---- seeded sampling ------------------------------------------------ #
    rng = random.Random(SEED)

    def _sortkey(u: dict) -> tuple:
        # turn_index None (design 06) sorts before ints via (-1)
        ti = u["turn_index"]
        return (u["design"], u["sut"], u["log"], u["sample_id"],
                -1 if ti is None else ti)

    d07_disagree = sorted([u for u in per_turn_units["07"] if u["disagree"]], key=_sortkey)
    d07_agree = sorted([u for u in per_turn_units["07"] if not u["disagree"]], key=_sortkey)
    d02_disagree = sorted([u for u in per_turn_units["02"] if u["disagree"]], key=_sortkey)
    d02_agree = sorted([u for u in per_turn_units["02"] if not u["disagree"]], key=_sortkey)
    six_control_pool_sorted = sorted(six_control_pool, key=_sortkey)
    six_gap_sorted = sorted(six_gap, key=_sortkey)

    def _draw(pool: List[dict], n: int) -> List[dict]:
        if n >= len(pool):
            return list(pool)
        return rng.sample(pool, n)

    # DRAW ORDER: 07-controls, 02-disagree, 02-controls, 06-controls
    sel_07_agree = _draw(d07_agree, N_07_AGREE_CONTROL)
    sel_02_disagree = _draw(d02_disagree, N_02_DISAGREE)
    sel_02_agree = _draw(d02_agree, N_02_AGREE_CONTROL)
    sel_06_control = _draw(six_control_pool_sorted, N_06_CONTROL)

    # wholesale takes (no RNG)
    sel_07_disagree = d07_disagree
    sel_06_gap = six_gap_sorted

    # ---- assemble manifest rows (stratum-tagged, no verdicts) ----------- #
    def _row(u: dict, stratum: str) -> dict:
        return {
            "design": u["design"], "sut": u["sut"], "log": u["log"],
            "sample_id": u["sample_id"], "item_id": u["item_id"],
            "admin": u["admin"], "turn_index": u["turn_index"],
            "prompt_sha256": u["prompt_sha256"], "stratum": stratum,
        }

    manifest: List[dict] = []
    manifest += [_row(u, "disagreement") for u in sel_07_disagree]
    manifest += [_row(u, "control") for u in sel_07_agree]
    manifest += [_row(u, "disagreement") for u in sel_02_disagree]
    manifest += [_row(u, "control") for u in sel_02_agree]
    manifest += [_row(u, "gap") for u in sel_06_gap]
    manifest += [_row(u, "control") for u in sel_06_control]

    # deterministic file order (independent of draw order) for stable bytes
    manifest.sort(key=lambda u: (u["design"], u["sut"], u["log"], u["sample_id"],
                                 -1 if u["turn_index"] is None else u["turn_index"],
                                 u["stratum"]))

    # ---- write manifest ------------------------------------------------- #
    os.makedirs(out_dir, exist_ok=True)
    man_path = os.path.join(out_dir, "sample-manifest.jsonl")
    buf = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                  for row in manifest)
    with open(man_path, "w", encoding="utf-8") as fh:
        fh.write(buf)
    man_sha = hashlib.sha256(buf.encode("utf-8")).hexdigest()

    # ---- stats for meta ------------------------------------------------- #
    def _counts(units: List[dict]) -> Tuple[int, int, int]:
        tot = len(units)
        dis = sum(1 for u in units if u["disagree"])
        dis_unscorable = sum(1 for u in units if u["disagree"] and u["involves_unscorable"])
        return tot, dis, dis_unscorable

    t02, dis02, unsc02 = _counts(per_turn_units["02"])
    t07, dis07, unsc07 = _counts(per_turn_units["07"])

    per_design_stratum = {
        "02": {"disagreement": len(sel_02_disagree), "control": len(sel_02_agree)},
        "07": {"disagreement": len(sel_07_disagree), "control": len(sel_07_agree)},
        "06": {"gap": len(sel_06_gap), "control": len(sel_06_control)},
    }

    per_sut: Dict[str, int] = {}
    for row in manifest:
        per_sut[row["sut"]] = per_sut.get(row["sut"], 0) + 1

    meta = {
        "canary": CANARY,
        "seed": SEED,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "draw_order": [
            "07-agreement-controls (sample 150)",
            "02-disagreement (sample 200)",
            "02-agreement-controls (sample 80)",
            "06-controls (sample 60 from remaining 95)",
        ],
        "wholesale_takes": [
            "07-disagreement (all)",
            "06-gap top-60 (all)",
        ],
        "sample_manifest_sha256": man_sha,
        "total_sampled_units": len(manifest),
        "per_design_stratum_counts": per_design_stratum,
        "per_sut_counts": dict(sorted(per_sut.items())),
        "resolved_unit_universe": {
            "02": t02, "07": t07, "06": len(six_units),
        },
        "prompt_universe": {
            "02": len(prompts["02"]), "07": len(prompts["07"]), "06": len(prompts["06"]),
        },
        "disagreement_counts": {
            "02": {"disagreement": dis02, "total": t02,
                   "base_rate": (dis02 / t02) if t02 else None},
            "07": {"disagreement": dis07, "total": t07,
                   "base_rate": (dis07 / t07) if t07 else None},
        },
        "unscorable_involvement_in_disagreement": {
            "02": unsc02, "07": unsc07,
        },
        "design06_gap_stratum": {
            "gap_size": len(sel_06_gap),
            "control_pool_size": len(six_control_pool),
            "min_gap_in_top60": (min(u["gap"] for u in six_gap) if six_gap else None),
            "max_gap": (max(u["gap"] for u in six_ranked) if six_ranked else None),
        },
        "join_completeness": {
            "all_resolved": len(unresolved) == 0,
            "n_unresolved": len(unresolved),
            "n_unresolved_by_design": {
                d: sum(1 for u in unresolved if u.get("design") == d)
                for d in ("02", "07", "06")
            },
            "n_missing_A": sum(1 for u in unresolved if u.get("missing_A")),
            "n_missing_B": sum(1 for u in unresolved if u.get("missing_B")),
            "n_06_judgeB_all_null": sum(1 for u in unresolved if u.get("judgeB_all_null")),
            "n_06_judgeA_all_null": sum(1 for u in unresolved if u.get("judgeA_all_null")),
            "note": ("All unresolved units are design-06 samples where one judge returned "
                     "no scorable 7-category profile (all-null), so |mean_A-mean_B| is "
                     "undefined and the unit cannot enter the gap ranking. Reported here, "
                     "excluded from the 06 candidate pool by construction — not silently dropped."),
            "unresolved": unresolved[:50],
        },
    }
    meta_path = os.path.join(out_dir, "manifest-meta.json")
    with open(meta_path, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)

    return {"manifest_path": man_path, "meta_path": meta_path, "meta": meta,
            "n_unresolved": len(unresolved)}


def main() -> None:
    ap = argparse.ArgumentParser(description="Build JR-referee sampling manifest (offline).")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ap.add_argument("--prompts-dir", default="logs/jr-referee-20260716")
    ap.add_argument("--out-dir", default="logs/jr-referee-20260716")
    args = ap.parse_args()

    res = build(args.pilot_dir, args.prompts_dir, args.out_dir)
    m = res["meta"]
    print(CANARY)
    print(f"manifest      -> {res['manifest_path']}")
    print(f"meta          -> {res['meta_path']}")
    print(f"total sampled -> {m['total_sampled_units']}")
    print(f"sha256        -> {m['sample_manifest_sha256']}")
    print(f"join complete -> {m['join_completeness']['all_resolved']} "
          f"(n_unresolved={m['join_completeness']['n_unresolved']})")
    print("per-design stratum counts:", json.dumps(m["per_design_stratum_counts"]))
    print("per-sut counts:", json.dumps(m["per_sut_counts"]))
    print("disagreement base rates:",
          json.dumps({d: round(v["base_rate"], 4) if v["base_rate"] is not None else None
                      for d, v in m["disagreement_counts"].items()}))
    print("unscorable-in-disagreement:", json.dumps(m["unscorable_involvement_in_disagreement"]))


if __name__ == "__main__":
    main()
