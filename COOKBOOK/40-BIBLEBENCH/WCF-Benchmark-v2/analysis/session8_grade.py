#!/usr/bin/env python
"""Session-8 OAuth judge runner (J4 = claude -p opus, J5 = codex exec).

Replays persisted GRADE-FREE grading prompts (analysis/
20260717-session8-replay-rows.jsonl) through an out-of-benchmark OAuth judge
and appends results to analysis/20260717-session8-{j4,j5}-raw.jsonl.

Resume-safe: already-graded sample_keys are skipped on restart (append-only).

Parse contract (identical for both judges): strict last-match GRADE: N
(0-100), the harness regex. Unparseable -> exactly ONE re-prompt with a
minimal format reminder, then logged as parse-failure (grade=null).

Usage:
  session8_grade.py --judge j4 [--strata S1-epochs-core,...] [--limit N]
  session8_grade.py --judge j5 --rung 1 [--model gpt-5.5]
  session8_grade.py --judge j4 --smoke   # 3 seeded epochs-core calls
"""
from __future__ import annotations

import argparse
import json
import random
import re
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V2 = Path(__file__).resolve().parent.parent
ROWS = V2 / "analysis" / "20260717-session8-replay-rows.jsonl"
SMOKE_DIR = V2 / "analysis" / "20260717-session8-smoke"
GRADE_PATTERN = r"GRADE:\s*(\d{1,3})"
FORMAT_REMINDER = ("\n\nIMPORTANT: End your reply with a final line of the "
                   "form 'GRADE: <integer 0-100>'.")
RATE_LIMIT_MARKERS = ("rate limit", "429", "too many requests", "quota")
J4_MODEL = "opus"
J5_MODEL_DEFAULT = "gpt-5.5"
J4_TIMEOUT = 600
J5_TIMEOUT = 900
J4_WORKERS = 4

_write_lock = threading.Lock()


def parse_grade(text: str) -> int | None:
    m = re.findall(GRADE_PATTERN, text or "")
    if not m:
        return None
    v = int(m[-1])
    return v if 0 <= v <= 100 else None


# --------------------------------------------------------------------------- #
# Channels
# --------------------------------------------------------------------------- #
def call_j4(prompt: str, model: str) -> tuple[str, str]:
    """claude -p — returns (text, resolved_model_id). OAuth subscription."""
    proc = subprocess.run(
        ["claude", "-p", prompt, "--model", model, "--output-format", "json"],
        capture_output=True, text=True, timeout=J4_TIMEOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude -p exited {proc.returncode}: "
                           f"stderr={(proc.stderr or '')[:200]} "
                           f"stdout={(proc.stdout or '')[:300]}")
    out = (proc.stdout or "").strip()
    try:
        payload = json.loads(out)
        if isinstance(payload, list):  # CLI >=2.1: array of events
            payload = next((e for e in payload
                            if isinstance(e, dict)
                            and e.get("type") == "result"), {})
        text = payload.get("result", "")
        usage = payload.get("modelUsage") or {}
        resolved = next(iter(usage.keys()), model)
    except json.JSONDecodeError:
        text, resolved = out, model  # fall back to raw text
    if not text:
        raise RuntimeError("claude -p returned empty result")
    return text, resolved


def call_j5(prompt: str, model: str) -> tuple[str, str]:
    """codex exec hardened invocation — returns (text, model_pin)."""
    with tempfile.TemporaryDirectory(prefix="wcf_s8_codex_") as td:
        out_path = Path(td) / "last_message.txt"
        workdir = Path(td) / "empty"
        workdir.mkdir()
        argv = [
            "codex", "exec",
            "--ephemeral", "--ignore-user-config", "--ignore-rules",
            "--sandbox", "read-only", "--skip-git-repo-check",
            "-c", f"model={model}",
            "-c", 'model_reasoning_effort="medium"',
            "-c", 'web_search="disabled"',
            "-c", "features.multi_agent=false",
            "--json", "-o", str(out_path), "-C", str(workdir),
            prompt,
        ]
        with open("/dev/null") as devnull:  # stdin </dev/null MANDATORY
            proc = subprocess.run(argv, stdin=devnull, capture_output=True,
                                  text=True, timeout=J5_TIMEOUT)
        blob = (proc.stdout or "") + (proc.stderr or "")
        low = blob.lower()
        if any(m in low for m in RATE_LIMIT_MARKERS):
            raise RateLimited(blob[:300])
        if proc.returncode != 0:
            raise RuntimeError(f"codex exec exited {proc.returncode}: "
                               f"{(proc.stderr or '')[:300]}")
        completed = False
        for line in (proc.stdout or "").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            et = str(ev.get("type", ""))
            if et in ("error", "turn.failed"):
                raise RuntimeError(f"codex event failure: {line[:300]}")
            if et == "turn.completed":
                completed = True
            if "command" in et or "tool" in et or "mcp" in et:
                raise RuntimeError(f"codex unexpected tool event: {line[:200]}")
        if not completed:
            raise RuntimeError("codex: no turn.completed event")
        text = out_path.read_text().strip() if out_path.exists() else ""
        if not text:
            raise RuntimeError("codex produced no final message")
        return text, model


class RateLimited(RuntimeError):
    pass


# --------------------------------------------------------------------------- #
# Runner
# --------------------------------------------------------------------------- #
def grade_one(row: dict, judge: str, model: str, raw_path: Path,
              smoke: bool = False) -> dict:
    call = call_j4 if judge == "j4" else call_j5
    rec = {"sample_key": row["sample_key"], "stratum": row["stratum"],
           "grade": None, "attempt": 0, "wall_ms": 0, "model_id": model,
           "parse_fail": False}
    prompt = row["prompt"]
    for attempt in (1, 2):  # attempt 2 = the single format-reminder re-prompt
        p = prompt if attempt == 1 else prompt + FORMAT_REMINDER
        t0 = time.time()
        backoff = 30
        transient = 0
        while True:
            try:
                text, resolved = call(p, model)
                break
            except RateLimited as e:
                print(f"    rate-limited; sleeping {backoff}s ({e})",
                      flush=True)
                time.sleep(backoff)
                backoff = min(backoff * 2, 600)
            except subprocess.TimeoutExpired:
                text, resolved = "", model
                break
            except RuntimeError as e:
                transient += 1
                if transient > 3:
                    # channel failure: record it (excluded from resume 'done')
                    rec["channel_error"] = str(e)[:200]
                    rec["wall_ms"] = int((time.time() - t0) * 1000)
                    with _write_lock:
                        with raw_path.open("a") as fh:
                            fh.write(json.dumps(rec) + "\n")
                    return rec
                print(f"    transient channel error (try {transient}): "
                      f"{str(e)[:120]}; sleeping {20 * transient}s",
                      flush=True)
                time.sleep(20 * transient)
        rec["wall_ms"] = int((time.time() - t0) * 1000)
        rec["attempt"] = attempt
        rec["model_id"] = resolved
        g = parse_grade(text)
        if smoke:
            SMOKE_DIR.mkdir(exist_ok=True)
            (SMOKE_DIR / f"{judge}-{row['sample_key'].replace('|','_')}"
             f"-a{attempt}.txt").write_text(text or "(empty)")
        if g is not None:
            rec["grade"] = g
            rec["raw_tail"] = (text or "")[-400:]
            break
        if attempt == 2:
            rec["parse_fail"] = True
            rec["raw_tail"] = (text or "")[-400:]
    with _write_lock:
        with raw_path.open("a") as fh:
            fh.write(json.dumps(rec) + "\n")
    return rec


def load_rows(args) -> list[dict]:
    rows = [json.loads(l) for l in ROWS.read_text().splitlines()]
    if args.strata:
        keep = set(args.strata.split(","))
        rows = [r for r in rows if r["stratum"] in keep]
    if args.rung is not None:
        rows = [r for r in rows if r.get("j5_rung") == args.rung]
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", required=True, choices=["j4", "j5"])
    ap.add_argument("--model", default=None)
    ap.add_argument("--strata", default=None)
    ap.add_argument("--rung", type=int, default=None)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--raw-suffix", default="")
    ap.add_argument("--rows-file", default=None)
    args = ap.parse_args()
    global ROWS
    if args.rows_file:
        ROWS = Path(args.rows_file)

    judge = args.judge
    model = args.model or (J4_MODEL if judge == "j4" else J5_MODEL_DEFAULT)
    raw_path = (V2 / "analysis" /
                f"20260717-session8-{judge}{args.raw_suffix}-raw.jsonl")

    rows = load_rows(args)
    if args.smoke:
        rng = random.Random(2026)
        rows = rng.sample([r for r in rows if r["stratum"] == "S1-epochs-core"],
                          3)
    done = set()
    if raw_path.exists():
        for l in raw_path.read_text().splitlines():
            try:
                rec = json.loads(l)
                if not rec.get("channel_error"):  # channel fails retry on resume
                    done.add(rec["sample_key"])
            except Exception:
                pass
    todo = [r for r in rows if r["sample_key"] not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{judge} model={model}: {len(rows)} selected, {len(done)} done, "
          f"{len(todo)} to grade -> {raw_path.name}", flush=True)

    t0 = time.time()
    n_ok = n_pf = 0

    def report(rec, i):
        nonlocal n_ok, n_pf
        if rec["parse_fail"]:
            n_pf += 1
        else:
            n_ok += 1
        if (i + 1) % 10 == 0 or args.smoke:
            el = time.time() - t0
            print(f"  [{i+1}/{len(todo)}] ok={n_ok} pf={n_pf} "
                  f"{el/max(1,i+1):.1f}s/call elapsed={el/60:.1f}m "
                  f"last={rec['sample_key']} g={rec['grade']}", flush=True)

    if judge == "j4" and not args.smoke:
        with ThreadPoolExecutor(max_workers=J4_WORKERS) as ex:
            futs = [ex.submit(grade_one, r, judge, model, raw_path)
                    for r in todo]
            done_n = 0
            for fut in futs:
                try:
                    rec = fut.result()
                except Exception as e:  # lost record retries on resume
                    print(f"  worker error (will resume): {str(e)[:150]}",
                          flush=True)
                    done_n += 1
                    continue
                report(rec, done_n)
                done_n += 1
    else:  # serial: J5 always; smokes always
        for i, r in enumerate(todo):
            rec = grade_one(r, judge, model, raw_path, smoke=args.smoke)
            report(rec, i)

    print(f"DONE {judge}: ok={n_ok} parse_fail={n_pf} "
          f"wall={(time.time()-t0)/60:.1f}m", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
