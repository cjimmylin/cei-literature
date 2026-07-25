#!/opt/homebrew/opt/python@3.14/bin/python3.14
"""Session 17 — Sol arm of the strict-v3 20-cell bench re-pass.

One verdict per bench packet (single-packet mode, fresh codex process per
verdict via session16_stability_sol_driver.call_sol — hardened argv, model
gpt-5.6-sol, effort high, stdin /dev/null). No repeats: 20 cells x 1.

Packets:  /tmp/wcf-s17-bench/packets/<ITEM>__<sut>.md  (strict-v3 rendered,
          leakage-scanned by session17_bench_packets_v3.py)
Verdicts: /tmp/wcf-s17-bench/sol/<ITEM>__<sut>.md

Usage: session17_bench_sol_driver.py --stream N [--nstreams 4]
Resume-safe: skips cells whose verdict file exists and parses.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "analysis"))

from session16_stability_sol_driver import GRADE_RE, REMINDER, call_sol  # noqa: E402

BENCH_DIR = Path("/tmp/wcf-s17-bench")
PACKET_DIR = BENCH_DIR / "packets"
OUT_DIR = BENCH_DIR / "sol"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stream", type=int, required=True)
    ap.add_argument("--nstreams", type=int, default=4)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    packets = sorted(PACKET_DIR.glob("*.md"))
    if len(packets) != 20:
        raise RuntimeError(f"expected 20 packets, found {len(packets)}")

    mine = [p for i, p in enumerate(packets) if i % args.nstreams == args.stream]
    print(f"[stream {args.stream}] {len(mine)} cells: {[p.stem for p in mine]}", flush=True)

    for pkt in mine:
        out = OUT_DIR / pkt.name
        if out.exists() and GRADE_RE.search(out.read_text()):
            print(f"[stream {args.stream}] SKIP {pkt.stem} (done)", flush=True)
            continue
        t0 = time.time()
        prompt = pkt.read_text()
        text = call_sol(prompt)
        if not GRADE_RE.search(text):
            text = call_sol(prompt + REMINDER)
            if not GRADE_RE.search(text):
                text += "\n[PARSE-FAILURE after one re-prompt]"
        out.write_text(text)
        m = GRADE_RE.findall(text)
        grade = m[-1] if m else "PARSE-FAIL"
        print(f"[stream {args.stream}] {pkt.stem}: GRADE={grade} ({time.time()-t0:.0f}s)", flush=True)

    print(f"[stream {args.stream}] DONE", flush=True)


if __name__ == "__main__":
    main()
