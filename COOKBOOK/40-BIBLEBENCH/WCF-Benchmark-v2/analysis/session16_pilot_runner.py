"""Session-16 pilot SUT sampling for WCF-Benchmark-v2.

Owner-ratified design (do not deviate): 3 SUTs x the 146-item frontier core
(items whose id contains "-N-") x 1 epoch. SUT-side spend HARD CAP $5.00 total.

We build each SUT input EXACTLY as the Inspect harness does — the user message is
`record_to_sample(record).input` and the system message is `EXAMINEE_SYSTEM`
(both imported from the harness src, never re-implemented). SUTs are called
directly over the OpenRouter chat/completions HTTP API via stdlib urllib.request
(no third-party HTTP libs). Temperature is NOT set (provider default = harness
default). Resume-safe append-only JSONL per SUT; existing ids are skipped on
restart. A thread-safe cost accumulator HARD STOPS all workers if accumulated
cost exceeds the cap.

Interpreter: /opt/homebrew/opt/python@3.14/bin/python3.14 (inspect_ai lives there).
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import threading
import statistics
import concurrent.futures as cf
from pathlib import Path

import urllib.request
import urllib.error

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))
sys.path.insert(0, str(WCF_ROOT / "analysis"))

# Build the SUT input EXACTLY as the harness does — reuse, do NOT fork.
from wcf_tasks import record_to_sample  # noqa: E402
from prompt_frames import EXAMINEE_SYSTEM  # noqa: E402

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
DATA_FILE = WCF_ROOT / "data" / "wcf_main.jsonl"
OUT_DIR = WCF_ROOT / "logs" / "20260724-session16-pilot"

# SUT models (OpenRouter HTTP API names) -> short tag for the response file name.
SUTS = {
    "minimax/minimax-m3": "minimax-m3",
    "openai/gpt-5-mini": "gpt-5-mini",
    "openai/gpt-4o-mini": "gpt-4o-mini",
}

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_CONCURRENCY = 8
# The Inspect harness sets NO max_tokens on the examinee generate() solver, so the
# faithful "harness/provider default" is effectively uncapped. minimax-m3 and
# gpt-5-mini are REASONING models that can spend 4000-5000 tokens on hidden
# reasoning before emitting the visible answer; a 4096 cap truncates ~half of them
# to finish_reason="length" with EMPTY content. Set the runaway guard high enough
# that reasoning + a full answer both fit (override via WCF_S16_MAX_TOKENS).
MAX_TOKENS = int(os.environ.get("WCF_S16_MAX_TOKENS", "16384"))
COST_CAP_USD = float(os.environ.get("WCF_S16_COST_CAP", "5.00"))
MAX_TRIES = 5
BACKOFF_BASE = 2.0

# Conservative (upper-bound) OpenRouter list prices, $/token, for the cost guard.
# minimax-m3 $0.40/M in $2.20/M out; gpt-5-mini $0.25/M in $2.00/M out;
# gpt-4o-mini $0.15/M in $0.60/M out.
PRICE = {
    "minimax/minimax-m3": {"in": 0.40 / 1_000_000, "out": 2.20 / 1_000_000},
    "openai/gpt-5-mini": {"in": 0.25 / 1_000_000, "out": 2.00 / 1_000_000},
    "openai/gpt-4o-mini": {"in": 0.15 / 1_000_000, "out": 0.60 / 1_000_000},
}


def load_api_key() -> str:
    """Mirror session14_calibration.load_api_key() — env override then codex secret."""
    if os.environ.get("OPENROUTER_API_KEY"):
        return os.environ["OPENROUTER_API_KEY"]
    env = Path.home() / ".codex" / "secrets" / "openrouter.env"
    for line in env.read_text().splitlines():
        m = re.match(r"\s*(?:export\s+)?OPENROUTER_API_KEY\s*=\s*(.+)\s*$", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    raise RuntimeError("OPENROUTER_API_KEY not found")


API_KEY = load_api_key()

# --------------------------------------------------------------------------- #
# Thread-safe state
# --------------------------------------------------------------------------- #
_cost_lock = threading.Lock()
_cost = {"usd": 0.0, "prompt_tokens": 0, "completion_tokens": 0, "calls": 0}
_stop = threading.Event()
_cap_hit = threading.Event()

_file_lock = threading.Lock()
_file_handles: dict[str, object] = {}

# Per-model bookkeeping for the summary.
_lat_lock = threading.Lock()
_latencies: dict[str, list] = {}
_per_model_cost: dict[str, float] = {}
_per_model_tokens: dict[str, dict] = {}
_failures: list = []


def add_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    p = PRICE[model]
    usd = prompt_tokens * p["in"] + completion_tokens * p["out"]
    with _cost_lock:
        _cost["usd"] += usd
        _cost["prompt_tokens"] += prompt_tokens
        _cost["completion_tokens"] += completion_tokens
        _cost["calls"] += 1
        pm = _per_model_cost.setdefault(model, 0.0)
        _per_model_cost[model] = pm + usd
        t = _per_model_tokens.setdefault(model, {"prompt": 0, "completion": 0})
        t["prompt"] += prompt_tokens
        t["completion"] += completion_tokens
        total = _cost["usd"]
    if total > COST_CAP_USD:
        _cap_hit.set()
        _stop.set()
    return usd


# --------------------------------------------------------------------------- #
# OpenRouter call with exponential backoff on 429/5xx
# --------------------------------------------------------------------------- #
def call_openrouter(model: str, system: str, user: str) -> dict:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_tokens": MAX_TOKENS,
    }
    data = json.dumps(payload).encode("utf-8")
    last_err = None
    for attempt in range(MAX_TRIES):
        if _stop.is_set():
            raise RuntimeError("stopped (cost cap)")
        req = urllib.request.Request(
            OPENROUTER_URL,
            data=data,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            code = e.code
            last_err = f"HTTP {code}: {e.read().decode('utf-8', 'replace')[:300]}"
            if code in (429,) or 500 <= code < 600:
                time.sleep(BACKOFF_BASE * (2 ** attempt))
                continue
            raise RuntimeError(last_err)
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = f"URLError: {e}"
            time.sleep(BACKOFF_BASE * (2 ** attempt))
            continue
    raise RuntimeError(f"exhausted retries: {last_err}")


def get_handle(tag: str):
    # Caller MUST already hold _file_lock (threading.Lock is non-reentrant).
    h = _file_handles.get(tag)
    if h is None:
        path = OUT_DIR / f"responses-{tag}.jsonl"
        h = open(path, "a", encoding="utf-8")
        _file_handles[tag] = h
    return h


def append_response(tag: str, obj: dict) -> None:
    line = json.dumps(obj, ensure_ascii=False)
    with _file_lock:
        h = get_handle(tag)
        h.write(line + "\n")
        h.flush()


def load_done_ids(tag: str) -> set:
    path = OUT_DIR / f"responses-{tag}.jsonl"
    done = set()
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                done.add(json.loads(line)["id"])
            except Exception:
                pass
    return done


# --------------------------------------------------------------------------- #
# Worker
# --------------------------------------------------------------------------- #
def do_one(model: str, tag: str, item_id: str, user_msg: str) -> None:
    if _stop.is_set():
        return
    t0 = time.time()
    try:
        resp = call_openrouter(model, EXAMINEE_SYSTEM, user_msg)
    except Exception as e:  # noqa: BLE001
        with _lat_lock:
            _failures.append({"id": item_id, "model": model, "error": str(e)[:400]})
        return
    elapsed = time.time() - t0
    try:
        choice = resp["choices"][0]
        completion = choice["message"].get("content") or ""
        finish = choice.get("finish_reason")
    except Exception as e:  # noqa: BLE001
        with _lat_lock:
            _failures.append({"id": item_id, "model": model,
                              "error": f"parse: {e}; raw={json.dumps(resp)[:300]}"})
        return
    usage = resp.get("usage", {}) or {}
    pt = int(usage.get("prompt_tokens", 0) or 0)
    ct = int(usage.get("completion_tokens", 0) or 0)
    add_cost(model, pt, ct)
    append_response(tag, {
        "id": item_id,
        "model": model,
        "completion": completion,
        "usage": usage,
        "finish_reason": finish,
        "elapsed_s": round(elapsed, 3),
    })
    with _lat_lock:
        _latencies.setdefault(model, []).append(elapsed)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    records = [json.loads(l) for l in DATA_FILE.read_text().splitlines() if l.strip()]
    n_items = [r for r in records if "-N-" in r["id"]]
    assert len(n_items) == 146, f"expected 146 N items, got {len(n_items)}"

    # Precompute the user message per item once (identical across SUTs).
    inputs = {}
    for r in n_items:
        inputs[r["id"]] = record_to_sample(r).input

    wall0 = time.time()
    jobs = []
    for model, tag in SUTS.items():
        done = load_done_ids(tag)
        for r in n_items:
            if r["id"] in done:
                continue
            jobs.append((model, tag, r["id"], inputs[r["id"]]))

    print(f"[s16] N items: {len(n_items)}  SUTs: {len(SUTS)}  "
          f"jobs to run (after resume-skip): {len(jobs)}  cap ${COST_CAP_USD:.2f}")

    with cf.ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as ex:
        futs = [ex.submit(do_one, *j) for j in jobs]
        for f in cf.as_completed(futs):
            f.result()

    for h in _file_handles.values():
        try:
            h.close()
        except Exception:
            pass

    wall = time.time() - wall0

    # Assemble summary from the persisted files (authoritative, resume-safe).
    per_sut = {}
    all_lat = []
    total_prompt = total_completion = 0
    est_total_cost = 0.0
    for model, tag in SUTS.items():
        path = OUT_DIR / f"responses-{tag}.jsonl"
        rows = []
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
        pt = sum(int((r.get("usage") or {}).get("prompt_tokens", 0) or 0) for r in rows)
        ct = sum(int((r.get("usage") or {}).get("completion_tokens", 0) or 0) for r in rows)
        cost = pt * PRICE[model]["in"] + ct * PRICE[model]["out"]
        lats = [r["elapsed_s"] for r in rows if r.get("elapsed_s") is not None]
        all_lat.extend(lats)
        total_prompt += pt
        total_completion += ct
        est_total_cost += cost
        empty = [r["id"] for r in rows if not (r.get("completion") or "").strip()]
        per_sut[tag] = {
            "model": model,
            "count": len(rows),
            "prompt_tokens": pt,
            "completion_tokens": ct,
            "estimated_cost_usd": round(cost, 5),
            "mean_latency_s": round(statistics.mean(lats), 3) if lats else None,
            "median_latency_s": round(statistics.median(lats), 3) if lats else None,
            "empty_completion_ids": empty,
        }

    summary = {
        "session": "session16-pilot",
        "design": "3 SUTs x 146 N-items x 1 epoch",
        "n_items": len(n_items),
        "suts": list(SUTS.keys()),
        "cost_cap_usd": COST_CAP_USD,
        "cap_hit": _cap_hit.is_set(),
        "wall_clock_s": round(wall, 1),
        "total_prompt_tokens": total_prompt,
        "total_completion_tokens": total_completion,
        "estimated_total_cost_usd": round(est_total_cost, 5),
        "overall_mean_latency_s": round(statistics.mean(all_lat), 3) if all_lat else None,
        "overall_median_latency_s": round(statistics.median(all_lat), 3) if all_lat else None,
        "per_sut": per_sut,
        "failures": _failures,
        "n_failures": len(_failures),
    }
    (OUT_DIR / "RUN-SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False))
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    if _cap_hit.is_set():
        print("\n*** COST CAP HIT — run stopped early ***")


if __name__ == "__main__":
    main()
