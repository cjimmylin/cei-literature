#!/usr/bin/env python3
"""
replay_score.py — Harness-comparability replay for Christian-Ethics-Benchmark-v2.

Isolates the PURE HARNESS DELTA: do v2's scorers reproduce v1's judge verdicts
when SUT responses and judge model are held FIXED?

Design (documented in the report):
  * SUBSTRATE: v2 PRE-REVIEW datasets (identical item content to what v1 ran;
    post-review datasets carry 105 ratified fixes that would confound). Copied into
    tools/replay/data/public/ from RECYCLE-BIN/datasets-prereview-20260715/.
  * RESPONSE INJECTION: the v2 model-graded scorer reads the SUT response from
    `state.output.completion` and nothing else (scorers.py:299). So the most faithful
    replay is to build a minimal TaskState with metadata = the pre-review dataset row's
    metadata and output.completion = v1's stored response for the matching (item, admin),
    then call the SAME scorer factory v2 uses in production
    (_make_model_graded_scorer(design, judge_model)). No SUT call is made.
  * JOIN UNIT: (design, item_id, admin_label). v1 admin labels are mapped to v2 dataset
    admin labels via ADMIN_MAP below. Each v1 per-admin/per-seat unit carries its own
    response and its own full score-dict — a clean 1:1 with a v2 per_admin/per_seat row.
  * JUDGE: openrouter/openai/gpt-4.1-nano (v1 judge-A slug), max_tokens capped.
  * EXCLUSIONS: designs 02 & 07 are per_turn in v1 (turn_state per turn) but v2's scorer
    reads only the FINAL completion and emits a single item-level score — no clean
    per-turn alignment. Excluded from the judge-path replay (documented).
"""
from __future__ import annotations
import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V2 = HERE.parent.parent  # .../Christian-Ethics-Benchmark-v2
V1 = V2.parent / "Christian-Ethics-Benchmark"
DATA = HERE / "data" / "public"

sys.path.insert(0, str(V2))

# Cap the hardcoded judge max_tokens BEFORE importing scorers (402 trap + cost control).
import walkworthy_inspect.scorers as scorers_mod  # noqa: E402
scorers_mod.JUDGE_MAX_TOKENS = 256  # v1 judge used max_tokens=256 (manifest.json)

from walkworthy_inspect.scorers import _make_model_graded_scorer  # noqa: E402
from inspect_ai.solver import TaskState  # noqa: E402
from inspect_ai.scorer import Target  # noqa: E402
from inspect_ai.model import ModelOutput, get_model  # noqa: E402

JUDGE_A = "openrouter/openai/gpt-4.1-nano"

DESIGN_SLUG = {
    "01": "01-goodsamaritan", "02": "02-twomasters", "03": "03-quiettongue",
    "04": "04-innerweight", "05": "05-ordoamoris", "06": "06-crookedpath",
    "07": "07-seventyseven", "08": "08-vocationfork", "09": "09-doubleedge",
    "10": "10-strangergate",
}

# v1 admin label -> v2 dataset admin label. None = same label.
# Item-unit designs (01/05/06): v1 admin 'main' -> v2 dataset '#base' row.
ADMIN_MAP = {
    "01": {"main": "base"},
    "03": {"expressed": "say", "revealed": "do"},
    "04": {"alpha": "alpha", "beta": "beta"},
    "05": {"main": "base"},
    "06": {"main": "base"},
    "08": {"covert": "covert", "overt": "overt"},
    "09": {"seat_A": "seat_A", "seat_B": "seat_B"},  # 'arbiter' has no v2 per-seat row
    "10": {"U": "U", "N": "N"},
}

# Designs excluded from judge-path replay (per_turn v1 vs single-completion v2 scorer).
EXCLUDED_DESIGNS = {"02", "07"}

# 05 has a judge-free primary (CSR) but ALSO a model-graded rationale_honesty category;
# the generic _make_model_graded_scorer path scores that category, matching v1's
# rationale_honesty verdict field. (05's design05_scorer wraps additional judge-free
# logic, but for the JUDGE-PATH comparison the rationale_honesty judge field is what
# aligns with v1's verdict scores.)


def load_dataset_index():
    """design_num -> { (item_id, v2_admin): metadata_dict } from PRE-REVIEW datasets."""
    idx = {}
    for dnum, slug in DESIGN_SLUG.items():
        fn = DATA / f"design{dnum}.jsonl"
        d = {}
        for line in fn.read_text().splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            md = rec["metadata"]
            # skip exemplar rows (admin like 'base-exemplar'); v1 ran only real admins
            admin = md.get("admin")
            if admin and admin.endswith("-exemplar"):
                continue
            d[(md["item_id"], admin)] = md
        idx[dnum] = d
    return idx


def build_units(sut_model: str):
    """Yield replay units: dicts with design_num, item_id, v1_admin, v2_admin,
    response_text, metadata, and v1 gold scores (judge-A) for that unit."""
    man = json.loads((V1 / "runs/20260713-mvp-a1/manifest.json").read_text())
    mvp_ids = set(man["item_ids"])

    # v1 executions for the chosen SUT: item_id -> {admin_label: response_text}
    execs = {}
    for line in (V1 / "runs/20260713-mvp-a1/executions.jsonl").read_text().splitlines():
        r = json.loads(line)
        if r["model"] != sut_model:
            continue
        admins = {}
        for a in r["execution"]["administrations"]:
            admins[a.get("label")] = a.get("response")
        execs[r["item_id"]] = {"design": r["design"], "admins": admins}

    # v1 judge-A verdicts: (item_id) -> per-admin/item score dicts
    v1_gold = {}  # (design_num, item_id, v1_admin) -> scores dict
    for line in (V1 / "runs/20260713-mvp-a1/verdicts.jsonl").read_text().splitlines():
        r = json.loads(line)
        if r["model"] != sut_model or r["judge"] != "openai/gpt-4.1-nano":
            continue
        dnum = r["design"].split("-", 1)[0]
        v = r["verdict"]
        if v["unit"] == "item":
            v1_gold[(dnum, r["item_id"], "main")] = dict(v["scores"])
        else:
            for u in v.get("per_unit", []):
                lbl = u.get("label")
                if lbl is None:  # per_turn (index-keyed) — excluded designs
                    continue
                v1_gold[(dnum, r["item_id"], lbl)] = dict(u["scores"])

    idx = load_dataset_index()

    units = []
    for item_id in sorted(mvp_ids):
        if item_id not in execs:
            continue
        dnum = execs[item_id]["design"].split("-", 1)[0]
        if dnum in EXCLUDED_DESIGNS:
            continue
        amap = ADMIN_MAP[dnum]
        for v1_admin, resp in execs[item_id]["admins"].items():
            if v1_admin not in amap:
                continue  # e.g. design09 'arbiter' — no v2 per-seat row
            v2_admin = amap[v1_admin]
            md = idx[dnum].get((item_id, v2_admin))
            if md is None:
                # some designs store item-unit rows with admin='base'
                md = idx[dnum].get((item_id, "base"))
            if md is None:
                continue
            gold = v1_gold.get((dnum, item_id, v1_admin))
            if gold is None:
                continue
            units.append({
                "design_num": dnum,
                "design": execs[item_id]["design"],
                "item_id": item_id,
                "v1_admin": v1_admin,
                "v2_admin": v2_admin,
                "response_text": resp or "",
                "metadata": md,
                "v1_gold": gold,
            })
    return units


async def score_unit(unit, sut_model):
    scorer = _make_model_graded_scorer(unit["design"], JUDGE_A)
    state = TaskState(
        model="replay/" + sut_model,
        sample_id=f"{unit['item_id']}#{unit['v2_admin']}",
        epoch=1,
        input="",
        messages=[],
        metadata=unit["metadata"],
        output=ModelOutput.from_content(model=sut_model, content=unit["response_text"]),
    )
    score = await scorer(state, Target(""))
    return score


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sut", default="mistralai/mistral-small-3.2-24b-instruct")
    ap.add_argument("--out", default=str(V2 / "logs/replay-20260715/replay_verdicts.jsonl"))
    ap.add_argument("--limit", type=int, default=0, help="cap units for a dry run (0=all)")
    ap.add_argument("--concurrency", type=int, default=6)
    args = ap.parse_args()

    if not os.environ.get("OPENROUTER_API_KEY"):
        print("ERROR: OPENROUTER_API_KEY not set. `source ~/.codex/secrets/openrouter.env`",
              file=sys.stderr)
        sys.exit(2)

    units = build_units(args.sut)
    if args.limit:
        units = units[:args.limit]
    print(f"SUT={args.sut}  units={len(units)}  judge={JUDGE_A}  max_tokens={scorers_mod.JUDGE_MAX_TOKENS}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    sem = asyncio.Semaphore(args.concurrency)
    results = []

    async def run_one(u):
        async with sem:
            try:
                score = await score_unit(u, args.sut)
                v2_scores = score.value if isinstance(score.value, dict) else {"__unscorable__": score.value}
            except Exception as exc:
                v2_scores = {"__error__": str(exc)}
            rec = {
                "design": u["design"], "item_id": u["item_id"],
                "v1_admin": u["v1_admin"], "v2_admin": u["v2_admin"],
                "sut": args.sut, "judge": JUDGE_A,
                "v1_scores": u["v1_gold"], "v2_scores": v2_scores,
            }
            results.append(rec)
            print(f"  {u['item_id']}#{u['v2_admin']:>8} v1={u['v1_gold']} v2={v2_scores}")

    await asyncio.gather(*(run_one(u) for u in units))

    # deterministic order
    results.sort(key=lambda r: (r["design"], r["item_id"], r["v2_admin"]))
    with out_path.open("w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    print(f"\nWrote {len(results)} replay verdicts -> {out_path}")


if __name__ == "__main__":
    asyncio.run(main())
