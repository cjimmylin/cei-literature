#!/usr/bin/env python3
"""Session-16 B2: Sol arm of the pilot judging ($0, codex exec OAuth).

Judges all packets in /tmp/wcf-s16-pilot/packets/ with the FROZEN Sol judge in
canonical single-packet mode (fresh codex exec process per verdict; hardened
invocation identical to session16_stability_sol_driver.py). Timing per verdict
is logged — this run doubles as the pilot throughput measurement.

Usage: session16_pilot_sol_driver.py --stream N --nstreams 4
Resume-safe: verdicts whose output parses are skipped.
Outputs: /tmp/wcf-s16-pilot/sol/<packet-stem>.md
"""

from __future__ import annotations

import argparse
import re
import time
from pathlib import Path

from session16_stability_sol_driver import call_sol, GRADE_RE, REMINDER  # noqa: E402

PKT_DIR = Path("/tmp/wcf-s16-pilot/packets")
OUT_DIR = Path("/tmp/wcf-s16-pilot/sol")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stream", type=int, required=True)
    ap.add_argument("--nstreams", type=int, default=4)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    packets = sorted(PKT_DIR.glob("*.md"))
    mine = [p for i, p in enumerate(packets) if i % args.nstreams == args.stream]
    print(f"[stream {args.stream}] {len(mine)} tasks", flush=True)

    for pkt in mine:
        out = OUT_DIR / pkt.name
        if out.exists() and GRADE_RE.search(out.read_text()):
            continue
        t0 = time.time()
        try:
            text = call_sol(pkt.read_text())
            if not GRADE_RE.search(text):
                text = call_sol(pkt.read_text() + REMINDER)
                if not GRADE_RE.search(text):
                    text += "\n\n[PARSE-FAILURE after one re-prompt]"
            out.write_text(text)
            m = GRADE_RE.findall(text)
            print(f"[stream {args.stream}] {out.name} grade={m[-1] if m else 'FAIL'} "
                  f"({time.time()-t0:.0f}s)", flush=True)
        except Exception as e:
            print(f"[stream {args.stream}] ERROR {out.name}: {e}", flush=True)

    print(f"[stream {args.stream}] DONE", flush=True)


if __name__ == "__main__":
    main()
