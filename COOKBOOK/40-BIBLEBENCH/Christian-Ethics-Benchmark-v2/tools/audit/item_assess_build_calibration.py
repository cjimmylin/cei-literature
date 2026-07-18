#!/usr/bin/env python
"""Build the 20-item calibration packet for the IVR-1 rater pilot.

Selection rule (deterministic, documented): per design, sort public item_ids;
pick index 2 and index len-3. Design 07 second pick is forced to WW-07-L02
(known defect item) so calibration exercises blocker detection.
Canary: WALKWORTHY-CANARY-7f3e2026
"""
import json
import re
from pathlib import Path

V2 = Path(__file__).resolve().parents[2]
LOGDIR = V2 / "logs" / "item-assessment-20260718"
PACKETS = LOGDIR / "packets"
OUTDIR = PACKETS / "calibration"
CANARY = "WALKWORTHY-CANARY-7f3e2026"

index = json.loads((PACKETS / "index.json").read_text())
batches = index["batches"] if isinstance(index, dict) and "batches" in index else index

# design -> [(item_id, batch_file)]
by_design = {}
for b in batches:
    if b["surface"] != "public":
        continue
    for iid in b["item_ids"]:
        by_design.setdefault(b["design"], []).append((iid, b["file"]))

picks = []
for design in sorted(by_design):
    items = sorted(by_design[design])
    sel = [items[2], items[len(items) - 3]]
    if design.startswith("d07") or "07" in design[:3]:
        forced = [t for t in items if t[0] == "WW-07-L02"]
        if forced and forced[0] not in sel:
            sel[1] = forced[0]
    picks.extend(sel)

assert len(picks) == 20, f"expected 20 picks, got {len(picks)}"

def extract_section(batch_path: Path, item_id: str) -> str:
    text = batch_path.read_text()
    m = re.search(rf"^### {re.escape(item_id)}$", text, flags=re.MULTILINE)
    assert m, f"{item_id} not found in {batch_path}"
    start = m.start()
    nxt = re.search(r"^### WW-", text[m.end():], flags=re.MULTILINE)
    end = m.end() + nxt.start() if nxt else len(text)
    return text[start:end].rstrip() + "\n"

OUTDIR.mkdir(parents=True, exist_ok=True)
groups = {"cal-1.md": picks[:10], "cal-2.md": picks[10:]}
manifest = {"canary": CANARY, "rule": "sorted idx 2 and len-3 per design; d07 second pick forced to WW-07-L02", "files": {}}
for fname, group in groups.items():
    parts = [f"# WALKWORTHY v2 -- IVR-1 CALIBRATION packet ({fname})\nCanary: {CANARY}\nSurface: public\n"]
    for iid, bfile in group:
        bpath = Path(bfile)
        if not bpath.is_absolute():
            bpath = V2 / bfile
        parts.append(extract_section(bpath, iid))
    (OUTDIR / fname).write_text("\n---\n\n".join(parts))
    manifest["files"][fname] = [iid for iid, _ in group]
(OUTDIR / "calibration-manifest.json").write_text(json.dumps(manifest, indent=2))
print(json.dumps(manifest["files"], indent=2))
print("chars:", {f: len((OUTDIR / f).read_text()) for f in groups})
