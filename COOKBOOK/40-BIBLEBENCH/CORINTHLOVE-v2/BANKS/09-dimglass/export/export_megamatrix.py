#!/usr/bin/env python3
"""Megamatrix episode-level export (prespec §3, rubric D3).

Emits one row per (episode, scored round) with the pinned schema:
  model_id, method_id, item_family, item_id, clause, score, rung,
  judge_ids, mechanical_flag, canary_id

Input: a scored-runs JSONL where each record is
  {"model_id":..., "item_id":..., "round":"round_1"|"round_2",
   "grade_num":0-3, "mechanical_flag":bool, "judge_ids":[...]}
Output: episode_table.csv (+ .jsonl).

The __main__ builds a MOCK scored file and demonstrates the export.
HARNESS VALIDATION, NOT A MEASUREMENT — the mock scores are synthetic.
"""
from __future__ import annotations

import csv
import json
import os
import sys

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METHOD_ID = "dimglass"
CLAUSE = "DIMGLASS:EPISTEMIC_HUMILITY"
SCHEMA = ["model_id", "method_id", "item_family", "item_id", "clause",
          "score", "rung", "judge_ids", "mechanical_flag", "canary_id"]


def load_episodes():
    import yaml
    eps = {}
    for rel in ("episodes/private_bank.yaml", "seeds_public.yaml"):
        with open(os.path.join(BANK, rel)) as f:
            for e in yaml.safe_load(f):
                eps[e["id"]] = e
    return eps


def build_rows(scored_records, episodes):
    rows = []
    for rec in scored_records:
        e = episodes[rec["item_id"]]
        rnd = rec.get("round", "round_1")
        r = e["parameters"].get(rnd) or e["parameters"]["round_1"]
        rows.append({
            "model_id": rec["model_id"],
            "method_id": METHOD_ID,
            "item_family": e["template_family"],
            "item_id": e["id"],
            "clause": CLAUSE,
            "score": rec["grade_num"],
            "rung": r["dose"],
            "judge_ids": "|".join(rec.get("judge_ids", [])) or "mechanical",
            "mechanical_flag": int(bool(rec.get("mechanical_flag", False))),
            "canary_id": e["canary"],
        })
    return rows


def write_table(rows, out_dir):
    with open(os.path.join(out_dir, "episode_table.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=SCHEMA)
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(out_dir, "episode_table.jsonl"), "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")


def _mock(episodes, n=40):
    """Deterministic synthetic scored records for demonstration."""
    import random
    rng = random.Random(20260706)
    ids = list(episodes)[:n]
    recs = []
    for mid in ("mock-model-A", "mock-model-B"):
        for iid in ids:
            recs.append({"model_id": mid, "item_id": iid, "round": "round_1",
                         "grade_num": rng.randint(0, 3),
                         "mechanical_flag": rng.random() < 0.15,
                         "judge_ids": ["mock-judge-X", "mock-judge-Y"]})
    return recs


def main():
    episodes = load_episodes()
    out_dir = os.path.join(BANK, "export")
    scored_path = os.path.join(out_dir, "scored_runs.MOCK.jsonl")
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            scored = [json.loads(l) for l in f if l.strip()]
        label = "REAL (from provided scored file)"
    else:
        scored = _mock(episodes)
        with open(scored_path, "w") as f:
            for r in scored:
                f.write(json.dumps(r) + "\n")
        label = "HARNESS VALIDATION, NOT A MEASUREMENT (mock scores)"
    rows = build_rows(scored, episodes)
    assert rows, "no rows produced"
    assert set(rows[0].keys()) == set(SCHEMA), "schema mismatch"
    write_table(rows, out_dir)
    print(json.dumps({"label": label, "n_rows": len(rows),
                      "schema": SCHEMA, "sample": rows[0]}, indent=2))


if __name__ == "__main__":
    main()
