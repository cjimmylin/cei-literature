#!/usr/bin/env python
"""Session-8 Phase 0: extract replay rows for the OAuth meta-judging study.

Dumps every sample needed by the J4/J5 grading runs to
analysis/20260717-session8-replay-rows.jsonl, one row per sample:
  sample_key   item_id|sut_short|epoch|dir_short  (stable resume key)
  stratum      S1-epochs-core | S2-ceiling | S3-episodes
  substratum   epochs-core | roster-main | episodes | panel | qwen-ramp
  sut          full openrouter model id;  sut_short  last path segment
  epoch, item_id, mold (contested/complicit/steadfast/v1-kind)
  prompt       persisted GRADE-FREE grading prompt (verbatim replay instrument)
  panel        {n_valid, values [gemini, deepseek, mistral_small]}
  prompt_chars, prompt_tokens_est (chars/4)
  j5_rung      1..4 or null (priority-ladder membership, seeded where sampled)

Strata (s8 boot prompt):
  S1 epochs-core: all 594 (66 core items x 3 SUTs x 3 epochs)
  S2 ceiling: per 20260716A methodology — items where ALL 4 roster-main SUTs
     score panel-median >= 95, restricted to v1-derived (no '-N-'); seeded
     sample of 25 items x 4 SUTs = 100 rows
  S3 episodes: seeded subsample ~85 of roster episodes (4x22) + panels (4x9)
     + qwen-ramp (27), multi-turn-history prompts included deliberately

J5 ladder (owner-locked): rung1 = S1a epoch-1 all 3 SUTs (198); rung2 = S1b
epochs 2-3 haiku+gpt-5-mini (+264); rung3 = S2' ceiling subsample (60);
rung4 = S3' episode subsample (40).

Also prints an episode-prompt length pre-measurement (truncation-risk flags).
"""
from __future__ import annotations

import glob
import json
import random
import statistics as st
from collections import defaultdict
from pathlib import Path

from inspect_ai.log import read_eval_log

V2 = Path(__file__).resolve().parent.parent
OUT = V2 / "analysis" / "20260717-session8-replay-rows.jsonl"
SEED = 1337
CEILING_N_ITEMS = 25
EP_SAMPLE = {"episodes": 48, "panel": 20, "qwen-ramp": 17}   # -> 85
J5_CEILING_N = 60   # 15 items x 4 SUTs
J5_EPISODE_N = 40
TRUNC_FLAG_CHARS = 100_000  # conservative CLI-context risk flag

EPOCHS_CORE = "20260716-session7-epochs-core"
ROSTER_MAIN = {
    "gemini": "20260716-session7-gemini-main",
    "glm": "20260716-session7-roster-glm-main",
    "minimax": "20260716-session7-roster-minimax-main",
    "mistral": "20260716-session7-roster-mistral-main",
}
EPISODE_DIRS = {
    "episodes": ["20260716-session7-gemini-episodes",
                 "20260716-session7-roster-glm-episodes",
                 "20260716-session7-roster-minimax-episodes",
                 "20260716-session7-roster-mistral-episodes"],
    "panel": ["20260716-session7-gemini-panel",
              "20260716-session7-roster-glm-panel",
              "20260716-session7-roster-minimax-panel",
              "20260716-session7-roster-mistral-panel"],
    "qwen-ramp": ["20260716-session7-qwen-ramp"],
}
HEADLINE_SUTS = {"claude-haiku-4.5", "gpt-5-mini"}


def load_molds() -> dict:
    molds = {}
    for fn in ["wcf_main.jsonl", "wcf_new_main.jsonl", "wcf_s7_new_main.jsonl",
               "wcf_episodes.jsonl", "wcf_new_episodes.jsonl"]:
        p = V2 / "data" / fn
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            if not line.strip():
                continue
            d = json.loads(line)
            if d.get("contested"):
                m = "contested"
            elif d.get("design") == "complicit":
                m = "complicit"
            elif d.get("design") == "steadfast":
                m = "steadfast"
            else:
                m = "v1-kind"
            molds[d["id"]] = m
    return molds


def rows_from_dir(dir_name: str, substratum: str, molds: dict) -> list[dict]:
    rows = []
    for f in sorted(glob.glob(str(V2 / "logs" / dir_name / "*.eval"))):
        log = read_eval_log(f)
        sut = log.eval.model
        sut_short = sut.split("/")[-1]
        for s in (log.samples or []):
            sc = (s.scores or {}).get("multi_scorer")
            if sc is None:
                continue
            md = sc.metadata or {}
            grading = md.get("grading") or []
            panel = md.get("panel") or {}
            if not grading or not panel.get("values"):
                continue
            prompt = grading[0]["content"]
            epoch = getattr(s, "epoch", 1) or 1
            item_id = str(s.id)
            dir_short = dir_name.replace("20260716-session7-", "")
            rows.append({
                "sample_key": f"{item_id}|{sut_short}|{epoch}|{dir_short}",
                "substratum": substratum,
                "sut": sut, "sut_short": sut_short,
                "epoch": epoch, "item_id": item_id,
                "mold": molds.get(item_id, "v1-kind"),
                "prompt": prompt,
                "panel": panel,
                "prompt_chars": len(prompt),
                "prompt_tokens_est": len(prompt) // 4,
            })
    return rows


def main() -> int:
    rng = random.Random(SEED)
    molds = load_molds()

    # --- S1: epochs-core (all) -------------------------------------------
    s1 = rows_from_dir(EPOCHS_CORE, "epochs-core", molds)
    assert len(s1) == 594, f"epochs-core expected 594, got {len(s1)}"
    for r in s1:
        r["stratum"] = "S1-epochs-core"

    # --- S2: ceiling stratum from the 4 roster-main runs -----------------
    roster_rows = []
    for short, d in ROSTER_MAIN.items():
        roster_rows.extend(rows_from_dir(d, "roster-main", molds))
    by_item = defaultdict(dict)   # item -> sut_short -> median
    row_index = defaultdict(dict)  # item -> sut_short -> row
    for r in roster_rows:
        vals = [v for v in r["panel"]["values"] if isinstance(v, (int, float))]
        if not vals:
            continue
        by_item[r["item_id"]][r["sut_short"]] = st.median(vals)
        row_index[r["item_id"]][r["sut_short"]] = r
    ceiling_items = sorted(
        it for it, per_sut in by_item.items()
        if "-N-" not in it and len(per_sut) == 4
        and all(v >= 95 for v in per_sut.values())
    )
    chosen = sorted(rng.sample(ceiling_items,
                               min(CEILING_N_ITEMS, len(ceiling_items))))
    s2 = []
    for it in chosen:
        for sut_short, r in sorted(row_index[it].items()):
            r["stratum"] = "S2-ceiling"
            s2.append(r)

    # --- S3: episode strata subsample ------------------------------------
    s3 = []
    for sub, dirs in EPISODE_DIRS.items():
        pool = []
        for d in dirs:
            pool.extend(rows_from_dir(d, sub, molds))
        take = min(EP_SAMPLE[sub], len(pool))
        pick = rng.sample(pool, take)
        for r in pick:
            r["stratum"] = "S3-episodes"
        s3.extend(pick)

    # --- J5 rung tags ------------------------------------------------------
    for r in s1:
        if r["epoch"] == 1:
            r["j5_rung"] = 1
        elif r["sut_short"] in HEADLINE_SUTS:
            r["j5_rung"] = 2
        else:
            r["j5_rung"] = None
    j5_ceiling_items = set(rng.sample(chosen, min(15, len(chosen))))
    for r in s2:
        r["j5_rung"] = 3 if r["item_id"] in j5_ceiling_items else None
    j5_ep = set(id(x) for x in rng.sample(s3, min(J5_EPISODE_N, len(s3))))
    for r in s3:
        r["j5_rung"] = 4 if id(r) in j5_ep else None

    rows = s1 + s2 + s3
    keys = [r["sample_key"] for r in rows]
    assert len(keys) == len(set(keys)), "duplicate sample_key"

    with OUT.open("w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")

    # --- pre-measurement report ------------------------------------------
    def stat(rs):
        ls = [r["prompt_chars"] for r in rs]
        return (f"n={len(rs)} chars min={min(ls)} med={int(st.median(ls))} "
                f"max={max(ls)}")
    print(f"S1 epochs-core: {stat(s1)}")
    print(f"S2 ceiling:     {stat(s2)}  ({len(chosen)} items of "
          f"{len(ceiling_items)} eligible)")
    for sub in EP_SAMPLE:
        sel = [r for r in s3 if r['substratum'] == sub]
        print(f"S3 {sub:9s}: {stat(sel)}")
    flagged = [r for r in rows if r["prompt_chars"] > TRUNC_FLAG_CHARS]
    print(f"TRUNCATION-RISK (> {TRUNC_FLAG_CHARS} chars): {len(flagged)}")
    for r in flagged:
        print(f"  {r['sample_key']} {r['prompt_chars']}")
    n_dropout = sum(1 for r in rows if r["panel"].get("n_valid", 3) < 3)
    print(f"incumbent quorum dropouts (n_valid<3): {n_dropout}")
    lad = defaultdict(int)
    for r in rows:
        lad[r.get("j5_rung")] += 1
    print("J5 ladder:", dict(sorted((str(k), v) for k, v in lad.items())))
    print(f"TOTAL rows: {len(rows)} -> {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
