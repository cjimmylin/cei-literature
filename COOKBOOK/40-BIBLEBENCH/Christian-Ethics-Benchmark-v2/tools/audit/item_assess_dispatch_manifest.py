#!/usr/bin/env python
"""Group packet batches into rater-dispatch units (<=3 files, <=210k chars).
Canary: WALKWORTHY-CANARY-7f3e2026"""
import json
from pathlib import Path

V2 = Path(__file__).resolve().parents[2]
LOGDIR = V2 / "logs" / "item-assessment-20260718"
index = json.loads((LOGDIR / "packets" / "index.json").read_text())
batches = index["batches"] if isinstance(index, dict) and "batches" in index else index

units = []
for surface in ("public", "holdout"):
    surf = [b for b in batches if b["surface"] == surface]
    cur, cur_chars = [], 0
    for b in surf:
        c = b.get("char_count") or b.get("chars") or 0
        if cur and (len(cur) == 3 or cur_chars + c > 210_000):
            units.append({"surface": surface, "files": cur, "chars": cur_chars})
            cur, cur_chars = [], 0
        cur.append(b)
        cur_chars += c
    if cur:
        units.append({"surface": surface, "files": cur, "chars": cur_chars})

manifest = {"canary": "WALKWORTHY-CANARY-7f3e2026", "units": []}
for i, u in enumerate(units, 1):
    manifest["units"].append({
        "unit": f"U{i:02d}",
        "surface": u["surface"],
        "chars": u["chars"],
        "n_items": sum(len(b["item_ids"]) for b in u["files"]),
        "files": [b["file"] for b in u["files"]],
        "outputs": [Path(b["file"]).stem for b in u["files"]],
        "item_ids": sum((b["item_ids"] for b in u["files"]), []),
    })
(LOGDIR / "dispatch-manifest.json").write_text(json.dumps(manifest, indent=2))
pub = [u for u in manifest["units"] if u["surface"] == "public"]
hold = [u for u in manifest["units"] if u["surface"] == "holdout"]
print(f"units: {len(manifest['units'])} (public {len(pub)}, holdout {len(hold)})")
print(f"items: public {sum(u['n_items'] for u in pub)}, holdout {sum(u['n_items'] for u in hold)}")
for u in manifest["units"]:
    print(u["unit"], u["surface"], f"{u['chars']:>7}", u["n_items"], [Path(f).name for f in u["files"]])
