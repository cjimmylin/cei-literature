#!/usr/bin/env python
"""Session-7 track-2: gemini-free-panel kin DiD for the google SUT row.

Mandatory before any google number is quotable (s5 kin ruling; s7 boot prompt).

Method (mirrors analysis/session5_kin_regrade.py replay + the s5 DiD form):
  - SUT rows: gemini-3.5-flash (kin to grader g1=gemini-2.5-flash) from
    logs/20260716-session7-gemini-main; CONTROL qwen3.7-plus (non-kin, epoch 1)
    from logs/20260716-session7-epochs-core.
  - N=60 sampled main-task responses per SUT (seeded RNG 1337).
  - Replay: grading prompt = scores['multi_scorer'].metadata.grading[0].content
    (grade-free by construction) -> openrouter/amazon/nova-pro-v1 (validated
    kin-free substitute; command-r banned from audit panels).
  - Persisted panel values [g1 gemini, g2 deepseek, g3 mistral-small] give the
    default-panel median for free; kin-free panel median = median(g2, g3, nova).
  - delta(SUT) = mean(default) - mean(kinfree); DiD = delta(gemini SUT) -
    delta(qwen SUT); bootstrap 2000 for the 95% CI.

PRE-STATED quotability rule (stated before results seen): the gemini row is
quotable WITH a disclosed +/-bound if the DiD 95% CI upper bound < 5.0 points;
otherwise only the kin-free-adjusted number is quotable. The measured bound is
disclosed either way.

Writes analysis/20260716-session7-gemini-kin-did.json.
"""
from __future__ import annotations

import asyncio
import glob
import json
import random
import re
import statistics as st
from pathlib import Path

from inspect_ai.log import read_eval_log
from inspect_ai.model import ChatMessageUser, get_model

V2 = Path(__file__).resolve().parent.parent
GEMINI_DIR = V2 / "logs" / "20260716-session7-gemini-main"
CONTROL_DIR = V2 / "logs" / "20260716-session7-epochs-core"
GEMINI_SUT = "openrouter/google/gemini-3.5-flash"
CONTROL_SUT = "openrouter/qwen/qwen3.7-plus"
NOVA = "openrouter/amazon/nova-pro-v1"
N_SAMPLE = 60
SEED = 1337
N_BOOT = 2000
GRADE_PATTERN = r"GRADE:\s*(\d{1,3})"
CONCURRENCY = 10
MAX_RETRIES = 4


def parse_grade(text: str) -> int | None:
    m = re.findall(GRADE_PATTERN, text or "")
    if not m:
        return None
    v = int(m[-1])
    return v if 0 <= v <= 100 else None


def rows_from(log_dir: Path, sut: str, epoch1_only: bool) -> list[dict]:
    rows = []
    for f in sorted(glob.glob(str(log_dir / "*.eval"))):
        log = read_eval_log(f)
        if log.eval.model != sut:
            continue
        for s in (log.samples or []):
            if epoch1_only and getattr(s, "epoch", 1) != 1:
                continue
            sc = (s.scores or {}).get("multi_scorer")
            if sc is None:
                continue
            md = sc.metadata or {}
            grading = md.get("grading") or []
            panel = (md.get("panel") or {}).get("values")
            if not grading or not panel or len(panel) != 3:
                continue
            rows.append({
                "sample_id": str(s.id),
                "prompt": grading[0]["content"],
                "panel": panel,  # [gemini, deepseek, mistral_small]
            })
    return rows


def med(vals: list) -> float | None:
    ok = [v for v in vals if isinstance(v, (int, float))]
    return st.median(ok) if ok else None


async def grade_all(rows: list[dict]) -> None:
    model = get_model(NOVA)
    sem = asyncio.Semaphore(CONCURRENCY)

    async def one(r):
        async with sem:
            for _ in range(MAX_RETRIES):
                try:
                    out = await model.generate([ChatMessageUser(content=r["prompt"])])
                    g = parse_grade(out.completion)
                    if g is not None:
                        r["nova"] = g
                        return
                except Exception:
                    await asyncio.sleep(2)
            r["nova"] = None

    await asyncio.gather(*(one(r) for r in rows))


def deltas(rows: list[dict]) -> list[float]:
    """Per-row default-median minus kinfree-median (rows with valid nova)."""
    out = []
    for r in rows:
        if r.get("nova") is None:
            continue
        dflt = med(r["panel"])
        kinfree = med([r["panel"][1], r["panel"][2], r["nova"]])
        if dflt is None or kinfree is None:
            continue
        out.append(dflt - kinfree)
    return out


def main() -> int:
    rng = random.Random(SEED)
    gem = rows_from(GEMINI_DIR, GEMINI_SUT, epoch1_only=False)
    ctl = rows_from(CONTROL_DIR, CONTROL_SUT, epoch1_only=True)
    if not gem or not ctl:
        raise SystemExit(f"missing logs: gemini {len(gem)} rows, control {len(ctl)}")
    gem_s = rng.sample(gem, min(N_SAMPLE, len(gem)))
    ctl_s = rng.sample(ctl, min(N_SAMPLE, len(ctl)))
    asyncio.run(grade_all(gem_s + ctl_s))

    d_gem = deltas(gem_s)
    d_ctl = deltas(ctl_s)
    obs = st.mean(d_gem) - st.mean(d_ctl)
    boots = []
    for _ in range(N_BOOT):
        bg = [rng.choice(d_gem) for _ in d_gem]
        bc = [rng.choice(d_ctl) for _ in d_ctl]
        boots.append(st.mean(bg) - st.mean(bc))
    boots.sort()
    lo, hi = boots[int(0.025 * N_BOOT)], boots[int(0.975 * N_BOOT)]
    quotable = hi < 5.0
    out = {
        "method": "gemini-free-panel DiD (s5 form); nova-pro replay of persisted "
                  "grade-free grading prompts; kinfree panel = median(deepseek, "
                  "mistral-small, nova)",
        "pre_stated_rule": "gemini row quotable with disclosed bound iff DiD CI95 "
                           "upper < 5.0 points; else kin-free-adjusted only",
        "n_gemini_rows": len(d_gem), "n_control_rows": len(d_ctl),
        "nova_unparseable": sum(1 for r in gem_s + ctl_s if r.get("nova") is None),
        "delta_gemini_sut": round(st.mean(d_gem), 3),
        "delta_control_qwen_sut": round(st.mean(d_ctl), 3),
        "did_obs": round(obs, 3),
        "did_ci95": [round(lo, 3), round(hi, 3)],
        "verdict_quotable_with_bound": quotable,
    }
    dest = V2 / "analysis" / "20260716-session7-gemini-kin-did.json"
    dest.write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
