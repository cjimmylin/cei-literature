"""Session-16 A1: build the BLIND re-audit packet for the CONTESTED LIB-N-010/haiku
truth-bench row. NO API calls.

Unlike the s15 judge packets, this packet is RAW MATERIALS, not a rendered judge
prompt: the auditor sees the request (stem), the authoritative item key/rubric
(render_standard), and the full logged SUT response — nothing else. It must NOT
contain: the strict-v2 template, any expected score/band, the s14 audit verdict,
the two s15 strong-judge verdicts, or any reference to the truth bench. The
auditor is settling exactly the dispute those documents disagree on, so any
exposure would anchor it.

Output goes OUTSIDE the repo (anti-leakage discipline): /tmp/wcf-s16-a1/.
"""

from __future__ import annotations

import sys
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))
sys.path.insert(0, str(WCF_ROOT / "analysis"))

import json  # noqa: E402

from wcf_tasks import render_standard  # noqa: E402
from wcf_grading import defang_wcf_markers  # noqa: E402
from session15_bench_packets import discover_sut_logs  # noqa: E402

ITEM_ID = "LIB-N-010"
SUT = "haiku"
OUT_DIR = Path("/tmp/wcf-s16-a1")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    items = {r["id"]: r for r in
             json.loads((WCF_ROOT / "data" / "session13_new_items.json").read_text())}
    item = items[ITEM_ID]
    rec = discover_sut_logs()[SUT][ITEM_ID]

    criterion = render_standard(item)
    response = defang_wcf_markers(rec["completion"])

    packet = (
        "# Response audit packet\n\n"
        "## THE REQUEST GIVEN TO THE MODEL\n\n"
        f"{rec['question']}\n\n"
        "## THE ITEM KEY AND RUBRIC (authoritative)\n\n"
        f"{criterion}\n\n"
        "## THE MODEL'S FULL RESPONSE\n\n"
        f"{response}\n"
    )
    out = OUT_DIR / f"{ITEM_ID}__{SUT}__audit-packet.md"
    out.write_text(packet)
    print(f"wrote {out} ({len(packet.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
