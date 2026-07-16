#!/usr/bin/env python
"""Build blind referee batch files for the JR meta-audit.

WALKWORTHY-CANARY-7f3e2026

Reads the frozen sample manifest + exported prompt JSONLs and writes
single-design batch files of ~25 units each to /tmp/jr-batches/ containing
ONLY {prompt_sha256, prompt} — no SUT identity, no vault paths, no judge
verdicts (blindness by construction: referee agents read /tmp only).

Ladder spreading: units sharing a ladder key (sut, log, sample_id) are
assigned to distinct batches (least-filled-first greedy), so no batch holds
two turns of the same ladder unless a ladder has more turns than batches.

Deterministic given the frozen inputs. Also writes a dispatch ledger
(batch -> prompt_sha256 list) under logs/jr-referee-20260716/ for resume
tracking; the ledger stays vault-side, batches are the only referee-visible
artifact.
"""
import json
import math
import os
from collections import defaultdict

V2 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JR = os.path.join(V2, "logs", "jr-referee-20260716")
BATCH_DIR = "/tmp/jr-batches"
BATCH_SIZE = 25


def main():
    prompts = {}
    for d in ("02", "07", "06"):
        with open(os.path.join(JR, f"prompts-{d}.jsonl")) as f:
            for line in f:
                row = json.loads(line)
                prompts[(row["design"], row["prompt_sha256"])] = row["prompt"]

    by_design = defaultdict(list)
    with open(os.path.join(JR, "sample-manifest.jsonl")) as f:
        for line in f:
            row = json.loads(line)
            by_design[row["design"]].append(row)

    os.makedirs(BATCH_DIR, exist_ok=True)
    ledger = {}
    for design in sorted(by_design):
        units = by_design[design]
        n_batches = math.ceil(len(units) / BATCH_SIZE)
        ladders = defaultdict(list)
        for u in units:
            ladders[(u["sut"], u["log"], u["sample_id"])].append(u)
        batches = [[] for _ in range(n_batches)]
        for lkey in sorted(ladders):
            turns = sorted(ladders[lkey], key=lambda u: (u["turn_index"] is not None, u["turn_index"]))
            # assign this ladder's turns to distinct least-filled batches
            order = sorted(range(n_batches), key=lambda i: (len(batches[i]), i))
            for u, bi in zip(turns, order):
                batches[bi].append(u)
            # a ladder longer than n_batches wraps (documented caveat)
            for k, u in enumerate(turns[n_batches:]):
                batches[order[k % n_batches]].append(u)
        for bi, batch in enumerate(batches):
            batch.sort(key=lambda u: u["prompt_sha256"])
            name = f"batch-{design}-{bi:02d}"
            payload = {
                "batch": name,
                "design": design,
                "units": [
                    {"prompt_sha256": u["prompt_sha256"],
                     "prompt": prompts[(design, u["prompt_sha256"])]}
                    for u in batch
                ],
            }
            with open(os.path.join(BATCH_DIR, name + ".json"), "w") as f:
                json.dump(payload, f, ensure_ascii=False, indent=1)
            ledger[name] = [u["prompt_sha256"] for u in batch]

    with open(os.path.join(JR, "dispatch-ledger.json"), "w") as f:
        json.dump({"canary": "WALKWORTHY-CANARY-7f3e2026",
                   "batch_size": BATCH_SIZE,
                   "batches": ledger}, f, indent=1, sort_keys=True)

    sizes = {name: len(v) for name, v in ledger.items()}
    per_design = defaultdict(int)
    for name in ledger:
        per_design[name.split("-")[1]] += 1
    print(json.dumps({"n_batches": len(ledger),
                      "per_design_batches": dict(per_design),
                      "total_units": sum(sizes.values()),
                      "min_batch": min(sizes.values()),
                      "max_batch": max(sizes.values())}, indent=1))


if __name__ == "__main__":
    main()
