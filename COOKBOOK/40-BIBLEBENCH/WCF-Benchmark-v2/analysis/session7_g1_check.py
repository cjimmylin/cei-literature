#!/usr/bin/env python
"""Session-7 G1 gate: assemble accepted items + mechanical form-rule checks.

Assembles the 5 post-adjudication draft files into data/session7_new_items.json
(sorted by id) and runs every mechanically checkable form rule from the s7
authoring brief + both adjudication memos. Exit nonzero on any failure.
Session-7 authored only two kinds (contested + open) — no episodes.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

V2 = Path(__file__).resolve().parent.parent
DRAFTS = V2 / "data" / "session7-drafts"

DRAFT_FILES = ["draft-D1a.json", "draft-D1b.json", "draft-D1c.json",
               "draft-D2.json", "draft-D3.json"]
EXPECTED = {"contested": 22, "open": 20, "episode": 0}
KILLED = {"CONT-N-033", "CONT-N-035", "CONT-N-038", "COMP-N-013",
          "COMP-N-014", "COMP-N-019", "STED-N-012", "STED-N-016"}
LEAK_STRINGS = ["rubric", "this is a test", "you are being tested", "grader"]
HEDGES = ["sort cleanly", "not settle", "not resolve", "incommensurab"]


def main() -> int:
    items, errs = [], []
    for f in DRAFT_FILES:
        items.extend(json.load(open(DRAFTS / f)))

    ids = [it["id"] for it in items]
    if len(set(ids)) != len(ids):
        errs.append("duplicate ids in accepted set")
    dead = set(ids) & KILLED
    if dead:
        errs.append(f"killed ids present: {dead}")

    existing = set()
    for bank in ("wcf_main.jsonl", "wcf_episodes.jsonl"):
        for line in open(V2 / "data" / bank):
            existing.add(json.loads(line)["id"])
    clash = set(ids) & existing
    if clash:
        errs.append(f"id clash with existing bank: {clash}")

    kinds = {"contested": 0, "open": 0, "episode": 0}
    for it in items:
        iid = it["id"]
        for f in ("id", "design", "track", "tier", "commandments", "stem", "key",
                  "rubric", "kind", "contested", "episode"):
            if it.get(f) in (None, "", []):
                errs.append(f"{iid}: missing {f}")
        if it.get("authored") != "session-7" or "-N-" not in iid:
            errs.append(f"{iid}: provenance metadata/namespace")
        want = "episode" if it["episode"] else ("contested" if it["contested"] else "open")
        if it["kind"] != want:
            errs.append(f"{iid}: kind {it['kind']} != routed {want}")
        kinds[want] += 1
        tot = sum(c["points"] for c in it["rubric"])
        if not (5.0 <= tot <= 6.5):
            errs.append(f"{iid}: total {tot}")
        cap = 8 if want == "contested" else 6
        if len(it["rubric"]) > cap:
            errs.append(f"{iid}: {len(it['rubric'])} lines > {cap}")
        if not any(c.get("axis") == "manner" for c in it["rubric"]):
            errs.append(f"{iid}: no manner line")
        if "GATE" not in it["key"]:
            errs.append(f"{iid}: no GATE block in key")
        low_stem = it["stem"].lower()
        if "attached" in low_stem:
            errs.append(f"{iid}: stem says 'attached'")
        for s in LEAK_STRINGS:
            if s in low_stem:
                errs.append(f"{iid}: leak string '{s}' in stem")
        if want == "contested":
            for h in HEDGES:
                if h in low_stem:
                    errs.append(f"{iid}: hedge '{h}' in stem")
            joined = " ".join(str(c["criterion"]) for c in it["rubric"])
            if "accepted head-pair" not in joined:
                errs.append(f"{iid}: no enumerated head-pair criterion")
        low = it["key"].lower()
        for p in ("batch ruling", "review-", "adjudicat", "session-7 ",
                  "lens a", "lens b", "proposed_fix"):
            if p in low:
                errs.append(f"{iid}: process pointer '{p}' in key")
        if it.get("pressure_turns"):
            errs.append(f"{iid}: non-episode carries pressure_turns")

    for k, want_n in EXPECTED.items():
        if kinds[k] != want_n:
            errs.append(f"kind {k}: {kinds[k]} != expected {want_n}")

    if errs:
        print("G1 FAIL:")
        for e in errs:
            print(" -", e)
        return 1

    items.sort(key=lambda r: r["id"])
    out = V2 / "data" / "session7_new_items.json"
    with open(out, "w") as fh:
        json.dump(items, fh, indent=1, ensure_ascii=False)
    print(f"G1 PASS: {len(items)} items -> {out.name} "
          f"(contested {kinds['contested']}, open {kinds['open']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
