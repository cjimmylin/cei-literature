#!/opt/homebrew/opt/python@3.14/bin/python3.14
"""Session-17 full-run Sol judge — poll-loop daemon (single-packet mode, $0).

One verdict per strict-v2 packet, fresh codex process per verdict via
session16_stability_sol_driver.call_sol (model gpt-5.6-sol, effort high, stdin
</dev/null). Same one-re-prompt parse contract as session17_bench_sol_driver.py
(strict last-match 'GRADE: <int>'; one re-prompt on failure).

This runs CONCURRENTLY with session17_fullrun_runner: it renders packets from
whatever responses exist so far and judges its shard, sleeping between cycles,
until the runner is done AND everything is rendered AND its shard is fully judged.

Streams: --stream N --nstreams M (default 8). Sharding is a stable
zlib.crc32(filename) % nstreams == stream, so a packet always lands on the same
stream regardless of enumeration order or arrival time.

Renderer coordination: ONLY stream 0 calls session17_fullrun_packets.render_all()
each cycle (avoids N streams racing the renderer); render_all() is itself atomic
+ idempotent, so this is a courtesy not a correctness requirement.

Packets:  /tmp/wcf-s17-fullrun/packets/<ITEM>__<tag>__ep<N>.md
Verdicts: logs/20260725-session17-fullrun/sol-verdicts/<name>.md   (REPO dir, not /tmp)
Failures: logs/.../sol-verdicts/<name>.md.FAILED  (marker; nothing deleted)

Resume-safe: skips verdicts that already exist and contain a parseable GRADE.
Interpreter: /opt/homebrew/opt/python@3.14/bin/python3.14
"""

from __future__ import annotations

import argparse
import sys
import time
import zlib
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "analysis"))

from session16_stability_sol_driver import GRADE_RE, REMINDER, call_sol  # noqa: E402
import session17_fullrun_packets as packets  # noqa: E402

PACKET_DIR = Path("/tmp/wcf-s17-fullrun/packets")
LOG_DIR = WCF_ROOT / "logs" / "20260725-session17-fullrun"
VERDICT_DIR = LOG_DIR / "sol-verdicts"
RUNNER_DONE = LOG_DIR / "RUNNER-DONE"

SLEEP_S = 60


def shard_of(name: str, nstreams: int) -> int:
    return zlib.crc32(name.encode("utf-8")) % nstreams


def is_judged(verdict_path: Path) -> bool:
    if not verdict_path.exists():
        return False
    try:
        return bool(GRADE_RE.search(verdict_path.read_text()))
    except OSError:
        return False


def judge_one(pkt: Path, out: Path, stream: int) -> str:
    """Judge a single packet with one re-prompt on parse failure. Returns grade
    string (or 'FAILED'). Records a .FAILED marker on RuntimeError (retry once),
    never deletes/overwrites an existing parseable verdict."""
    prompt = pkt.read_text()
    for attempt in (1, 2):  # call_sol RuntimeError -> retry ONCE, then mark failed
        try:
            text = call_sol(prompt)
            if not GRADE_RE.search(text):
                text = call_sol(prompt + REMINDER)
                if not GRADE_RE.search(text):
                    text += "\n[PARSE-FAILURE after one re-prompt]"
            out.write_text(text)
            m = GRADE_RE.findall(text)
            return m[-1] if m else "PARSE-FAIL"
        except RuntimeError as e:
            if attempt == 2:
                marker = out.with_suffix(out.suffix + ".FAILED")
                marker.write_text(f"call_sol RuntimeError x2: {str(e)[:400]}\n")
                print(f"[stream {stream}] FAILED {pkt.stem}: {str(e)[:160]}",
                      flush=True)
                return "FAILED"
            time.sleep(2.0)
    return "FAILED"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stream", type=int, required=True)
    ap.add_argument("--nstreams", type=int, default=8)
    args = ap.parse_args()

    VERDICT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[stream {args.stream}/{args.nstreams}] poll-loop start", flush=True)

    while True:
        cycle_t0 = time.time()

        # (a) Only stream 0 drives the incremental renderer.
        n_rendered = 0
        if args.stream == 0:
            try:
                counts = packets.render_all()
                n_rendered = counts["rendered"]
                if n_rendered:
                    print(f"[stream 0] rendered {n_rendered} new packets "
                          f"(skipped {counts['skipped']}, total {counts['total']})",
                          flush=True)
            except Exception as e:  # noqa: BLE001 — never crash the loop on render
                print(f"[stream 0] render_all error: {str(e)[:200]}", flush=True)

        # (b) Enumerate this stream's shard; judge every unjudged packet.
        all_pkts = sorted(PACKET_DIR.glob("*.md")) if PACKET_DIR.exists() else []
        mine = [p for p in all_pkts if shard_of(p.name, args.nstreams) == args.stream]
        unjudged = [p for p in mine if not is_judged(VERDICT_DIR / p.name)]

        judged_this_cycle = 0
        for pkt in unjudged:
            out = VERDICT_DIR / pkt.name
            if is_judged(out):  # re-check (another pass may have finished it)
                continue
            t0 = time.time()
            grade = judge_one(pkt, out, args.stream)
            judged_this_cycle += 1
            print(f"[stream {args.stream}] {pkt.stem}: GRADE={grade} "
                  f"({time.time()-t0:.0f}s)", flush=True)

        # (c) Exit when runner done AND nothing left to render AND shard clean.
        remaining = [p for p in mine if not is_judged(VERDICT_DIR / p.name)
                     and not (VERDICT_DIR / (p.name + ".FAILED")).exists()]
        runner_done = RUNNER_DONE.exists()
        if runner_done and n_rendered == 0 and not remaining:
            print(f"[stream {args.stream}] DONE — runner finished, 0 to render, "
                  f"shard fully judged ({len(mine)} packets).", flush=True)
            return

        print(f"[stream {args.stream}] cycle: shard={len(mine)} judged_now="
              f"{judged_this_cycle} remaining={len(remaining)} "
              f"runner_done={runner_done} ({time.time()-cycle_t0:.0f}s)",
              flush=True)
        time.sleep(SLEEP_S)


if __name__ == "__main__":
    main()
