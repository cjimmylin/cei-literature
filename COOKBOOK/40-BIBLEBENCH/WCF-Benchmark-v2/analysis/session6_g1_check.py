#!/usr/bin/env python
"""Session-6 G1 gate: assemble accepted items + mechanical form-rule checks.

Assembles the 6 post-adjudication final files into data/session6_new_items.json
(sorted by id) and runs every mechanically checkable form rule from the
authoring brief + adjudication memo. Exit nonzero on any failure.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

V2 = Path(__file__).resolve().parent.parent
DRAFTS = V2 / "data" / "session6-drafts"
sys.path.insert(0, str(V2 / "convert"))
from pressure_turns import CLOSING  # noqa: E402

FINAL_FILES = [
    "final-contested.json", "final-contested-new.json", "final-complicit.json",
    "final-steadfast.json", "final-crosswind.json", "final-episodes.json",
]
EXPECTED = {"contested": 15, "open": 28, "episode": 9}
LEAK_STRINGS = ["rubric", "this is a test", "you are being tested", "grader"]
HEDGES = ["sort cleanly", "not settle", "not resolve", "incommensurab"]

def main() -> int:
    items, errs = [], []
    for f in FINAL_FILES:
        items.extend(json.load(open(DRAFTS / f)))

    ids = [it["id"] for it in items]
    if len(set(ids)) != len(ids):
        errs.append("duplicate ids in accepted set")

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
        # schema
        for f in ("id", "design", "track", "tier", "commandments", "stem", "key",
                  "rubric", "kind", "contested", "episode"):
            if it.get(f) in (None, "", []):
                errs.append(f"{iid}: missing {f}")
        if it.get("authored") != "session-6" or "-N-" not in iid:
            errs.append(f"{iid}: provenance metadata/namespace")
        # routing consistency
        want = "episode" if it["episode"] else ("contested" if it["contested"] else "open")
        if it["kind"] != want:
            errs.append(f"{iid}: kind {it['kind']} != routed {want}")
        kinds[want] += 1
        # rubric form
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
        # self-containment sentinel + leak strings
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
        # process-pointer leak into grader-visible text
        for field in ("key",):
            low = it[field].lower()
            for p in ("batch ruling", "review-", "adjudicat", "session-6 "):
                if p in low:
                    errs.append(f"{iid}: process pointer '{p}' in {field}")
        # episodes
        if want == "episode":
            pts = it.get("pressure_turns") or []
            if len(pts) != 3:
                errs.append(f"{iid}: pressure_turns != 3")
            else:
                if not pts[2].endswith(CLOSING):
                    errs.append(f"{iid}: final turn lacks frozen CLOSING")
                if CLOSING in pts[0] or CLOSING in pts[1]:
                    errs.append(f"{iid}: CLOSING leaked early")
                for i, t in enumerate(pts):
                    for s in LEAK_STRINGS + ["test"]:
                        if f" {s}" in t.lower():
                            errs.append(f"{iid}: leak '{s}' in turn {i+2}")
        elif it.get("pressure_turns"):
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
    out = V2 / "data" / "session6_new_items.json"
    with open(out, "w") as fh:
        json.dump(items, fh, indent=1, ensure_ascii=False)
    print(f"G1 PASS: {len(items)} items -> {out.name} "
          f"(contested {kinds['contested']}, open {kinds['open']}, episodes {kinds['episode']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
