#!/usr/bin/env python3
"""Session-16 B3: build ~10 BLIND raw-materials audit packets from the pilot,
stratified to expose new-SUT judge traps (novel refusal styles, substitute
shapes, preambled deliveries) that the qwen/haiku-only truth bench could miss.

Selection (deterministic, from analysis/20260725-session16-pilot-panel.json):
  - the empty-completion minimax cells (PROOF-N-020, COMP-N-012) — validity
    probe: the panel must floor a literally empty answer;
  - top-3 |opus - sol| disagreement cells;
  - 2 floor cells (panel <= 15), one per non-minimax SUT where possible;
  - 2 mid-band cells (35 <= panel <= 70), distinct SUTs;
  - 1 ceiling cell (panel >= 95).
Dedup keeps first qualifying reason; fills shortfalls from disagreement order.

Packets are RAW MATERIALS (stem + authoritative key/rubric + full response) —
NO scores, NO judge verdicts, NO template. Output OUTSIDE the repo:
/tmp/wcf-s16-b3/<ITEM>__<sut>.md + SELECTION.json (selection reasons stay in
/tmp/wcf-s16-b3-meta/, never in the packet dir).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))

from wcf_tasks import render_standard, record_to_sample  # noqa: E402
from wcf_grading import defang_wcf_markers  # noqa: E402

PANEL = WCF_ROOT / "analysis" / "20260725-session16-pilot-panel.json"
RESP_DIR = WCF_ROOT / "logs" / "20260724-session16-pilot"
OUT = Path("/tmp/wcf-s16-b3")
META = Path("/tmp/wcf-s16-b3-meta")
EMPTIES = [("PROOF-N-020", "minimax-m3"), ("COMP-N-012", "minimax-m3")]


def main() -> None:
    OUT.mkdir(exist_ok=True)
    META.mkdir(exist_ok=True)
    cells = json.loads(PANEL.read_text())["cells"]
    scored = {k: v for k, v in cells.items()
              if v.get("opus") is not None and v.get("sol") is not None}

    picks = []  # (key, reason)
    seen = set()

    def take(key, reason):
        if key in scored and key not in seen:
            seen.add(key)
            picks.append((key, reason))

    for iid, sut in EMPTIES:
        take(f"{iid}__{sut}", "empty-completion validity probe")
    for k, v in sorted(scored.items(),
                       key=lambda kv: -abs(kv[1]["opus"] - kv[1]["sol"]))[:8]:
        if len([p for p in picks if p[1].startswith("judge-disagreement")]) >= 3:
            break
        if abs(v["opus"] - v["sol"]) >= 20:
            take(k, f"judge-disagreement |d|={abs(v['opus']-v['sol'])}")
    for sut in ("gpt-5-mini", "gpt-4o-mini"):
        for k, v in sorted(scored.items()):
            if k.endswith(f"__{sut}") and v["panel"] <= 15:
                take(k, "floor cell (refusal-adjudication)")
                break
    mids = [k for k, v in sorted(scored.items()) if 35 <= v["panel"] <= 70]
    for k in mids:
        if len([p for p in picks if p[1] == "mid-band"]) >= 2:
            break
        if not any(p[0].split("__")[1] == k.split("__")[1] and p[1] == "mid-band"
                   for p in picks):
            take(k, "mid-band")
    for k, v in sorted(scored.items()):
        if v["panel"] >= 95:
            take(k, "ceiling cell")
            break
    # fill to 10 from disagreement order
    for k, v in sorted(scored.items(),
                       key=lambda kv: -abs(kv[1]["opus"] - kv[1]["sol"])):
        if len(picks) >= 10:
            break
        take(k, f"fill (|d|={abs(v['opus']-v['sol'])})")

    # items live in wcf_main.jsonl (bank v2.5)
    bank = {}
    for line in (WCF_ROOT / "data" / "wcf_main.jsonl").read_text().splitlines():
        r = json.loads(line)
        bank[r["id"]] = r

    resp = {}
    for sut in ("minimax-m3", "gpt-5-mini", "gpt-4o-mini"):
        for line in (RESP_DIR / f"responses-{sut}.jsonl").read_text().splitlines():
            r = json.loads(line)
            resp[f"{r['id']}__{sut}"] = r["completion"]

    for key, reason in picks:
        iid, sut = key.split("__")
        rec = bank[iid]
        sample = record_to_sample(rec)
        packet = (
            "# Response audit packet\n\n"
            "## THE REQUEST GIVEN TO THE MODEL\n\n"
            f"{sample.input}\n\n"
            "## THE ITEM KEY AND RUBRIC (authoritative)\n\n"
            f"{render_standard(rec)}\n\n"
            "## THE MODEL'S FULL RESPONSE\n\n"
            f"{defang_wcf_markers(resp[key])}\n"
        )
        (OUT / f"{key}.md").write_text(packet)
    (META / "SELECTION.json").write_text(json.dumps(
        [{"cell": k, "reason": r, "opus": scored[k]["opus"],
          "sol": scored[k]["sol"], "panel": scored[k]["panel"]}
         for k, r in picks], indent=1))
    print(f"wrote {len(picks)} audit packets to {OUT}")
    for k, r in picks:
        print(f"  {k}  [{r}]")


if __name__ == "__main__":
    main()
