#!/usr/bin/env python3
"""Session-16 A3: Sol arm of the judge-stability study ($0, codex exec OAuth).

Runs the 20-cell x 3-repeat stability sample through the FROZEN Sol judge
(gpt-5.6-sol, high reasoning effort, strict-v2 packets rendered by s15 machinery).
Each verdict is a fresh `codex exec` process (fresh context per verdict by
construction). Hardened invocation mirrors analysis/session8_grade.py: ephemeral,
ignore-user-config (model re-pinned explicitly), read-only sandbox, empty workdir,
stdin </dev/null, web search + multi-agent off.

Usage: session16_stability_sol_driver.py --stream N   (N in 0..3; run 4 in parallel)

Resume-safe: tasks whose output file already exists and parses are skipped.
Outputs: /tmp/wcf-s16-a3/sol/cell-NN-rM.md (raw last message)
Parse contract (s8): strict last-match r'GRADE:\s*(\d+)'; one re-prompt with a
minimal format reminder on failure, then logged as parse-failure.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

A3_DIR = Path("/tmp/wcf-s16-a3")
OUT_DIR = A3_DIR / "sol"
REPEATS = 3
TIMEOUT = 600
GRADE_RE = re.compile(r"GRADE:\s*(\d+)")
REMINDER = ("\n\nIMPORTANT: End your reply with a final line of the exact form "
            "'GRADE: <integer 0-100>'.")


def call_sol(prompt: str) -> str:
    with tempfile.TemporaryDirectory(prefix="wcf_s16_codex_") as td:
        out_path = Path(td) / "last_message.txt"
        workdir = Path(td) / "empty"
        workdir.mkdir()
        argv = [
            "codex", "exec",
            "--ephemeral", "--ignore-user-config", "--ignore-rules",
            "--sandbox", "read-only", "--skip-git-repo-check",
            "-c", 'model="gpt-5.6-sol"',
            "-c", 'model_reasoning_effort="high"',
            "-c", 'web_search="disabled"',
            "-c", "features.multi_agent=false",
            "--json", "-o", str(out_path), "-C", str(workdir),
            prompt,
        ]
        with open("/dev/null") as devnull:  # stdin </dev/null MANDATORY
            proc = subprocess.run(argv, stdin=devnull, capture_output=True,
                                  text=True, timeout=TIMEOUT)
        if proc.returncode != 0:
            raise RuntimeError(f"codex exec exited {proc.returncode}: "
                               f"{(proc.stderr or '')[:300]}")
        if out_path.exists():
            return out_path.read_text()
        raise RuntimeError("no last message written")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stream", type=int, required=True)
    ap.add_argument("--nstreams", type=int, default=4)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((A3_DIR / "MANIFEST.json").read_text())
    tasks = [(m["cell"], r) for m in manifest for r in range(1, REPEATS + 1)]
    mine = [t for idx, t in enumerate(tasks) if idx % args.nstreams == args.stream]
    print(f"[stream {args.stream}] {len(mine)} tasks", flush=True)

    for cell, rep in mine:
        out = OUT_DIR / f"{cell}-r{rep}.md"
        if out.exists() and GRADE_RE.search(out.read_text()):
            print(f"[stream {args.stream}] skip {out.name} (done)", flush=True)
            continue
        prompt = (A3_DIR / f"{cell}.md").read_text()
        t0 = time.time()
        try:
            text = call_sol(prompt)
            if not GRADE_RE.search(text):
                text = call_sol(prompt + REMINDER)
                if not GRADE_RE.search(text):
                    text += "\n\n[PARSE-FAILURE after one re-prompt]"
            out.write_text(text)
            m = GRADE_RE.findall(text)
            print(f"[stream {args.stream}] {out.name} grade={m[-1] if m else 'FAIL'} "
                  f"({time.time()-t0:.0f}s)", flush=True)
        except Exception as e:  # log and continue; resume pass sweeps stragglers
            print(f"[stream {args.stream}] ERROR {out.name}: {e}", flush=True)

    print(f"[stream {args.stream}] DONE", flush=True)


if __name__ == "__main__":
    main()
