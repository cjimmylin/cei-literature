#!/usr/bin/env python
"""WCF-Benchmark-v2 Stream B — grader-effect bound (EXPLORATORY / NON-QUOTABLE).

Re-grade the session-2 full-pass responses with two additional cross-family
graders (deepseek-chat, mistral-small-2603) to measure how much the single
gemini-2.5-flash grader moves scores. ZERO SUT spend.

ANTI-LEAKAGE (binding): each new grader is fed the EXACT prompt the incumbent
gemini grader received, replayed byte-for-byte from
`sample.scores['model_graded_qa'].metadata['grading'][0]['content']`. That
persisted prompt contains only (template + question + answer + criterion +
numeric instructions) — no prior grade, no other grader's output, no score.
We never read sibling-stream logs; input set is logs/20260715-full-pass only.

Grade parsing uses the SAME grade_pattern as the harness (last GRADE: N wins).

Usage:
    set -a && source ~/.codex/secrets/openrouter.env && set +a
    ./.venv-v2/bin/python analysis/regrade_graders.py
"""
from __future__ import annotations

import asyncio
import glob
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from inspect_ai.log import read_eval_log
from inspect_ai.model import GenerateConfig, ChatMessageUser, get_model

V2_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = V2_ROOT / "logs" / "20260715-full-pass"
OUT_DIR = V2_ROOT / "analysis"

# Same pattern the harness uses (last match wins via re.findall tail).
GRADE_PATTERN = r"GRADE:\s*(\d{1,3})"

GRADERS = {
    "deepseek": "openrouter/deepseek/deepseek-chat",
    "mistral": "openrouter/mistralai/mistral-small-2603",
}
INCUMBENT = "gemini"  # openrouter/google/gemini-2.5-flash (already in logs)
CONCURRENCY = 12
MAX_RETRIES = 5


def parse_grade(text: str) -> int | None:
    """Return the LAST GRADE: N in the grader output, or None. Mirrors harness
    semantics (instructions tell grader to END with the grade)."""
    matches = re.findall(GRADE_PATTERN, text or "")
    if not matches:
        return None
    val = int(matches[-1])
    return val if 0 <= val <= 100 else None


def load_samples() -> list[dict]:
    """Read all full-pass logs; return one row per (sample, SUT) with the
    incumbent grade and the exact replay prompt."""
    rows = []
    for f in sorted(glob.glob(str(LOG_DIR / "*.eval"))):
        log = read_eval_log(f)
        sut = log.eval.model
        task = log.eval.task  # wcf_main | wcf_episodes
        for s in log.samples:
            sc = s.scores["model_graded_qa"]
            grading = (sc.metadata or {}).get("grading")
            if not grading:
                continue
            prompt = grading[0]["content"]
            try:
                gem = int(sc.value)
            except (TypeError, ValueError):
                gem = None
            rows.append({
                "sample_id": str(s.id),
                "sut": sut,
                "task": task,
                "design": (s.metadata or {}).get("design"),
                "kind": (s.metadata or {}).get("kind"),
                "tier": (s.metadata or {}).get("tier"),
                "contested": (s.metadata or {}).get("contested"),
                "episode": (s.metadata or {}).get("episode"),
                "prompt": prompt,
                "gemini": gem,
            })
    return rows


async def grade_one(model, prompt: str) -> tuple[int | None, str]:
    for attempt in range(MAX_RETRIES):
        try:
            out = await model.generate([ChatMessageUser(content=prompt)])
            comp = out.completion
            return parse_grade(comp), comp
        except Exception as e:  # rate-limit / transient
            wait = min(2 ** attempt, 30)
            print(f"    retry {attempt+1}/{MAX_RETRIES} after {wait}s: {e}")
            await asyncio.sleep(wait)
    return None, "ERROR: max retries exceeded"


async def run_grader(name: str, slug: str, rows: list[dict]) -> None:
    model = get_model(slug, config=GenerateConfig(temperature=0.0))
    sem = asyncio.Semaphore(CONCURRENCY)
    done = 0
    t0 = time.time()

    async def worker(i: int, row: dict):
        nonlocal done
        async with sem:
            grade, comp = await grade_one(model, row["prompt"])
        row[name] = grade
        row[f"{name}_raw"] = comp[-400:] if comp else ""
        done += 1
        if done % 50 == 0 or done == len(rows):
            print(f"  [{name}] {done}/{len(rows)}  ({time.time()-t0:.0f}s)")

    await asyncio.gather(*(worker(i, r) for i, r in enumerate(rows)))
    none_ct = sum(1 for r in rows if r.get(name) is None)
    print(f"  [{name}] DONE {len(rows)} graded, {none_ct} unparseable, {time.time()-t0:.0f}s")


async def main() -> None:
    if not os.environ.get("OPENROUTER_API_KEY"):
        raise SystemExit("OPENROUTER_API_KEY not set — source the env first.")
    rows = load_samples()
    print(f"Loaded {len(rows)} (sample, SUT) rows from {LOG_DIR.name}")
    for name, slug in GRADERS.items():
        print(f"Grading with {name} = {slug}")
        await run_grader(name, slug, rows)

    # strip bulky prompt/raw fields from the matrix receipt; keep a compact grade matrix
    matrix = []
    for r in rows:
        matrix.append({
            "sample_id": r["sample_id"],
            "sut": r["sut"],
            "task": r["task"],
            "design": r["design"],
            "kind": r["kind"],
            "tier": r["tier"],
            "contested": r["contested"],
            "episode": r["episode"],
            "gemini": r["gemini"],
            "deepseek": r.get("deepseek"),
            "mistral": r.get("mistral"),
        })
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    out = OUT_DIR / f"{stamp}-streamB-grade-matrix.json"
    with open(out, "w") as fh:
        json.dump({
            "_meta": {
                "generated": datetime.now(timezone.utc).isoformat(),
                "banner": "EXPLORATORY / NON-QUOTABLE",
                "source_logs": LOG_DIR.name,
                "incumbent_grader": "openrouter/google/gemini-2.5-flash",
                "added_graders": GRADERS,
                "grader_temperature": 0.0,
                "n_rows": len(matrix),
                "replay_source": "sample.scores['model_graded_qa'].metadata['grading'][0]['content'] (byte-identical to incumbent prompt)",
                "grade_pattern": GRADE_PATTERN,
            },
            "matrix": matrix,
        }, fh, indent=2)
    print(f"Wrote {out}")

    # also dump raw grader completions for audit (separate, bulky)
    raw_out = OUT_DIR / f"{stamp}-streamB-grader-raw.json"
    with open(raw_out, "w") as fh:
        json.dump([{
            "sample_id": r["sample_id"], "sut": r["sut"],
            "deepseek_raw": r.get("deepseek_raw", ""),
            "mistral_raw": r.get("mistral_raw", ""),
        } for r in rows], fh, indent=2)
    print(f"Wrote {raw_out}")


if __name__ == "__main__":
    asyncio.run(main())
