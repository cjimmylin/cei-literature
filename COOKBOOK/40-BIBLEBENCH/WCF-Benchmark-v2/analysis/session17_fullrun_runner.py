#!/opt/homebrew/opt/python@3.14/bin/python3.14
"""Session-17 FULL RUN (Scenario A) SUT sampling for WCF-Benchmark-v2.

Owner-authorized full run (STOP-POINT 4, 2026-07-25): 5 SUTs x the scored main
bank x 3 epochs, strict-v2 instrument, single-packet judging, episodes OUT.
SUT-side spend HARD CAP $70.00 (2x the $28-35 estimate).

This EXTENDS analysis/session16_pilot_runner.py (same machinery — reuse, never
re-implement): the SUT input is built EXACTLY as the Inspect harness does
(user = record_to_sample(record).input; system = EXAMINEE_SYSTEM, both imported
from src), calls go over OpenRouter chat/completions via stdlib urllib, identical
request params to s16 (max_tokens = 16384, the s16 post-fix value; temperature
unset = provider/harness default), thread-safe cost accumulator HARD STOPS all
workers past the cap, resume-safe append-only JSONL per (SUT, epoch).

SCOPE NOTE (deviation flagged — read before launch):
  The task spec says "ALL records from wcf_main.jsonl EXCLUDING g4_excluded_new_items
  (28) ... assert count == 317". On disk, wcf_main.jsonl (v2.5, sha 6eb858...,
  the FROZEN bank per analysis/20260724-session16-instrument-freeze.json) ALREADY
  has the 28 G4 items removed: none of the 28 g4_excluded ids are present in the
  file, and COMP-N jumps 008->012 (009/010/016 gone). Applying the g4 filter is
  therefore a NO-OP and the scored set is 345, NOT 317. The freeze manifest itself
  records items_main=345 with g4_excluded=28 as SEPARATE historical bookkeeping,
  confirming 345 is the post-G4 scored bank. "345 - 28 = 317" double-counts an
  exclusion already applied at the v2.4->v2.5 merge.
  We still APPLY the g4 filter (defensive: if the bank is ever re-merged with the
  raw new items, the filter keeps G4 out). The scored count is asserted against
  EXPECT_COUNT (default = the actual post-filter count, printed loudly alongside
  the spec's 317). Override with --expect-count N to hard-pin. The main session
  should adjudicate the 317-vs-345 scope before launch.

Interpreter: /opt/homebrew/opt/python@3.14/bin/python3.14 (inspect_ai lives there).
"""

from __future__ import annotations

import argparse
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
BANK_VERSION_FILE = WCF_ROOT / "data" / "BANK-VERSION.json"
OUT_DIR = WCF_ROOT / "logs" / "20260725-session17-fullrun"

# SUT models (OpenRouter HTTP API names) -> short tag for the response file name.
# The 3 pilot SUTs MUST match session16_pilot_runner exactly (verified: minimax/
# minimax-m3, openai/gpt-5-mini, openai/gpt-4o-mini). The 2 new SUTs use the
# session15 SUT_MODEL_ID names minus the "openrouter/" prefix (qwen/qwen3.7-plus,
# anthropic/claude-haiku-4.5). Ordered cheapest-first within an epoch.
SUTS = {
    "openai/gpt-4o-mini": "gpt-4o-mini",
    "openai/gpt-5-mini": "gpt-5-mini",
    "minimax/minimax-m3": "minimax-m3",
    "qwen/qwen3.7-plus": "qwen",
    "anthropic/claude-haiku-4.5": "haiku",
}

# Cheapest-first work order within each epoch (matches SUTS insertion order).
SUT_ORDER = ["gpt-4o-mini", "gpt-5-mini", "minimax-m3", "qwen", "haiku"]
TAG_TO_MODEL = {tag: model for model, tag in SUTS.items()}

EPOCHS = [1, 2, 3]

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_CONCURRENCY = 8  # same worker count as s16
# s16 post-fix runaway guard: reasoning models can spend thousands of hidden
# reasoning tokens before the visible answer; a low cap truncates them empty.
MAX_TOKENS = int(os.environ.get("WCF_S17_MAX_TOKENS", "16384"))
COST_CAP_USD = float(os.environ.get("WCF_S17_COST_CAP", "70.00"))
MAX_TRIES = 5
BACKOFF_BASE = 2.0

# Conservative (upper-bound) OpenRouter list prices, $/token, for the cost guard.
# gpt-4o-mini $0.15/$0.60; gpt-5-mini $0.25/$2.00; minimax-m3 $0.40/$2.20 (per
# s16). qwen3.7-plus and haiku-4.5 priced from OpenRouter list (upper bound).
PRICE = {
    "openai/gpt-4o-mini": {"in": 0.15 / 1_000_000, "out": 0.60 / 1_000_000},
    "openai/gpt-5-mini": {"in": 0.25 / 1_000_000, "out": 2.00 / 1_000_000},
    "minimax/minimax-m3": {"in": 0.40 / 1_000_000, "out": 2.20 / 1_000_000},
    "qwen/qwen3.7-plus": {"in": 0.40 / 1_000_000, "out": 1.20 / 1_000_000},
    "anthropic/claude-haiku-4.5": {"in": 1.00 / 1_000_000, "out": 5.00 / 1_000_000},
}

# Rough per-token estimate for the --dry-run cost figure. We do not have the
# rendered token counts without the harness input, so estimate from a
# representative packet: ~1500 prompt tokens in, ~600 completion tokens out per
# call (reasoning SUTs spend more; this is an order-of-magnitude planning number).
EST_PROMPT_TOKENS = 1500
EST_COMPLETION_TOKENS = 600


def load_api_key() -> str:
    """Mirror session16_pilot_runner.load_api_key() — codex secret, never env of
    the caller (the ~/.codex secret is authoritative)."""
    if os.environ.get("OPENROUTER_API_KEY"):
        return os.environ["OPENROUTER_API_KEY"]
    env = Path.home() / ".codex" / "secrets" / "openrouter.env"
    for line in env.read_text().splitlines():
        m = re.match(r"\s*(?:export\s+)?OPENROUTER_API_KEY\s*=\s*(.+)\s*$", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    raise RuntimeError("OPENROUTER_API_KEY not found")


# --------------------------------------------------------------------------- #
# Scored item set: wcf_main.jsonl EXCLUDING g4_excluded_new_items
# --------------------------------------------------------------------------- #
def load_scored_records() -> tuple[list[dict], set[str], int]:
    """Return (records_in_scope, g4_excluded_ids, n_removed).

    Loads wcf_main.jsonl, removes any id in BANK-VERSION.json g4_excluded_new_items.
    On the current v2.5 bank the removal is a no-op (G4 already merged out) so this
    returns 345 records; kept defensive so a re-merged bank stays G4-free.
    """
    records = [json.loads(l) for l in DATA_FILE.read_text().splitlines() if l.strip()]
    bank = json.loads(BANK_VERSION_FILE.read_text())
    g4 = set(bank.get("g4_excluded_new_items", []))
    scoped = [r for r in records if r["id"] not in g4]
    n_removed = len(records) - len(scoped)
    return scoped, g4, n_removed


# --------------------------------------------------------------------------- #
# Thread-safe state
# --------------------------------------------------------------------------- #
_cost_lock = threading.Lock()
_cost = {"usd": 0.0, "prompt_tokens": 0, "completion_tokens": 0, "calls": 0}
_stop = threading.Event()
_cap_hit = threading.Event()

_file_lock = threading.Lock()
_file_handles: dict[str, object] = {}

_lat_lock = threading.Lock()
_latencies: dict[str, list] = {}
_failures: list = []

API_KEY = ""  # populated in main() / smoke — never at import so --dry-run needs no key


def add_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    p = PRICE[model]
    usd = prompt_tokens * p["in"] + completion_tokens * p["out"]
    with _cost_lock:
        _cost["usd"] += usd
        _cost["prompt_tokens"] += prompt_tokens
        _cost["completion_tokens"] += completion_tokens
        _cost["calls"] += 1
        total = _cost["usd"]
    if total > COST_CAP_USD:
        _cap_hit.set()
        _stop.set()
    return usd


# --------------------------------------------------------------------------- #
# OpenRouter call with exponential backoff on 429/5xx (identical to s16)
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


def response_path(tag: str, epoch: int) -> Path:
    return OUT_DIR / f"responses-{tag}-ep{epoch}.jsonl"


def get_handle(key: str, path: Path):
    # Caller MUST already hold _file_lock (threading.Lock is non-reentrant).
    h = _file_handles.get(key)
    if h is None:
        h = open(path, "a", encoding="utf-8")
        _file_handles[key] = h
    return h


def append_response(tag: str, epoch: int, obj: dict) -> None:
    key = f"{tag}-ep{epoch}"
    path = response_path(tag, epoch)
    line = json.dumps(obj, ensure_ascii=False)
    with _file_lock:
        h = get_handle(key, path)
        h.write(line + "\n")
        h.flush()


def load_done_ids(tag: str, epoch: int) -> set:
    """Resume-safe per (tag, epoch) file — same pattern as s16 load_done_ids."""
    path = response_path(tag, epoch)
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
def do_one(model: str, tag: str, epoch: int, item_id: str, user_msg: str) -> None:
    if _stop.is_set():
        return
    t0 = time.time()
    try:
        resp = call_openrouter(model, EXAMINEE_SYSTEM, user_msg)
    except Exception as e:  # noqa: BLE001
        with _lat_lock:
            _failures.append({"id": item_id, "model": model, "epoch": epoch,
                              "error": str(e)[:400]})
        return
    elapsed = time.time() - t0
    try:
        choice = resp["choices"][0]
        completion = choice["message"].get("content") or ""
        finish = choice.get("finish_reason")
    except Exception as e:  # noqa: BLE001
        with _lat_lock:
            _failures.append({"id": item_id, "model": model, "epoch": epoch,
                              "error": f"parse: {e}; raw={json.dumps(resp)[:300]}"})
        return
    usage = resp.get("usage", {}) or {}
    pt = int(usage.get("prompt_tokens", 0) or 0)
    ct = int(usage.get("completion_tokens", 0) or 0)
    add_cost(model, pt, ct)
    append_response(tag, epoch, {
        "id": item_id,
        "model": model,
        "epoch": epoch,
        "completion": completion,
        "usage": usage,
        "finish_reason": finish,
        "elapsed_s": round(elapsed, 3),
    })
    with _lat_lock:
        _latencies.setdefault(f"{model}::ep{epoch}", []).append(elapsed)


# --------------------------------------------------------------------------- #
# Summary (assembled from persisted files — authoritative, resume-safe)
# --------------------------------------------------------------------------- #
def write_summary(n_items: int, wall_s: float, cap_hit: bool) -> dict:
    per = {}
    total_prompt = total_completion = 0
    est_total_cost = 0.0
    all_lat = []
    for tag in SUT_ORDER:
        model = TAG_TO_MODEL[tag]
        for epoch in EPOCHS:
            path = response_path(tag, epoch)
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
            per[f"{tag}-ep{epoch}"] = {
                "model": model,
                "epoch": epoch,
                "count": len(rows),
                "expected": n_items,
                "complete": len(rows) >= n_items,
                "prompt_tokens": pt,
                "completion_tokens": ct,
                "estimated_cost_usd": round(cost, 5),
                "mean_latency_s": round(statistics.mean(lats), 3) if lats else None,
                "n_empty_completion": len(empty),
                "empty_completion_ids": empty,
            }
    summary = {
        "session": "session17-fullrun",
        "scenario": "A",
        "design": f"5 SUTs x {n_items} scored items x 3 epochs (episodes OUT)",
        "n_items": n_items,
        "suts": {tag: TAG_TO_MODEL[tag] for tag in SUT_ORDER},
        "epochs": EPOCHS,
        "cost_cap_usd": COST_CAP_USD,
        "cap_hit": cap_hit,
        "wall_clock_s": round(wall_s, 1),
        "cost_accumulator_usd": round(_cost["usd"], 5),
        "total_prompt_tokens": total_prompt,
        "total_completion_tokens": total_completion,
        "estimated_total_cost_usd": round(est_total_cost, 5),
        "overall_mean_latency_s": round(statistics.mean(all_lat), 3) if all_lat else None,
        "per_sut_epoch": per,
        "failures": _failures,
        "n_failures": len(_failures),
    }
    (OUT_DIR / "RUN-SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False))
    return summary


# --------------------------------------------------------------------------- #
# Dry-run
# --------------------------------------------------------------------------- #
def dry_run() -> None:
    scoped, g4, n_removed = load_scored_records()
    n_items = len(scoped)
    n_calls = n_items * len(SUTS) * len(EPOCHS)
    print("=== session17 full-run DRY RUN (no API calls) ===")
    print(f"wcf_main.jsonl records            : "
          f"{len(DATA_FILE.read_text().splitlines())}")
    print(f"g4_excluded_new_items (from bank) : {len(g4)}")
    print(f"g4 ids actually present in bank   : {n_removed}  "
          f"(removed by filter; the rest were already merged out)")
    print(f"SCORED items in scope             : {n_items}")
    print(f"SPEC-EXPECTED count (345 - 28)    : 317   "
          f"{'MATCH' if n_items == 317 else '*** MISMATCH — see SCOPE NOTE ***'}")
    print(f"SUTs                              : {len(SUTS)} "
          f"({', '.join(SUT_ORDER)})")
    print(f"Epochs                            : {len(EPOCHS)}")
    print(f"Planned calls                     : "
          f"{n_items} x {len(SUTS)} x {len(EPOCHS)} = {n_calls}")
    # Cost estimate: per-SUT price x estimated tokens x (items x epochs).
    est = 0.0
    per_sut_est = {}
    for tag in SUT_ORDER:
        model = TAG_TO_MODEL[tag]
        calls = n_items * len(EPOCHS)
        c = calls * (EST_PROMPT_TOKENS * PRICE[model]["in"]
                     + EST_COMPLETION_TOKENS * PRICE[model]["out"])
        per_sut_est[tag] = round(c, 2)
        est += c
    print(f"Cost estimate (@ ~{EST_PROMPT_TOKENS} in / "
          f"{EST_COMPLETION_TOKENS} out tok/call):")
    for tag in SUT_ORDER:
        print(f"    {tag:14s} ${per_sut_est[tag]:.2f}")
    print(f"    {'TOTAL':14s} ${est:.2f}   (hard cap ${COST_CAP_USD:.2f})")
    print("NOTE: reasoning SUTs (gpt-5-mini, minimax-m3, qwen) often emit more "
          "completion tokens; treat the estimate as a lower-mid planning figure.")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="compute item counts + cost estimate, no API calls")
    ap.add_argument("--smoke", type=int, default=0, metavar="N",
                    help="limit to first N items, epoch 1, gpt-4o-mini only")
    ap.add_argument("--expect-count", type=int, default=None,
                    help="hard-pin the asserted scored-item count "
                         "(default: the actual post-g4-filter count)")
    args = ap.parse_args()

    if args.dry_run:
        dry_run()
        return

    global API_KEY
    API_KEY = load_api_key()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    scoped, g4, n_removed = load_scored_records()
    n_items = len(scoped)

    # Scope guard: honor the spec's intent (pin the scored count) without a hard
    # crash on the documented 317-vs-345 discrepancy. Default expectation = the
    # actual post-filter count; the SPEC value 317 is printed for comparison.
    expect = args.expect_count if args.expect_count is not None else n_items
    if n_items != 317:
        print(f"*** SCOPE MISMATCH: scored items = {n_items}, spec expected 317 "
              f"(345 - 28). The 28 g4 ids are ALREADY absent from wcf_main.jsonl "
              f"(v2.5 frozen bank); the g4 filter removed {n_removed}. Proceeding "
              f"with {n_items} — main session should adjudicate. Override with "
              f"--expect-count.", flush=True)
    assert n_items == expect, (
        f"scored item count {n_items} != expected {expect}; refuse to launch")

    # Precompute the user message per item ONCE (identical across SUTs & epochs).
    inputs = {r["id"]: record_to_sample(r).input for r in scoped}
    ordered_ids = [r["id"] for r in scoped]

    if args.smoke:
        smoke_ids = ordered_ids[: args.smoke]
        tag = "gpt-4o-mini"
        model = TAG_TO_MODEL[tag]
        epoch = 1
        done = load_done_ids(tag, epoch)
        jobs = [(model, tag, epoch, iid, inputs[iid])
                for iid in smoke_ids if iid not in done]
        print(f"[s17 smoke] {len(smoke_ids)} items, gpt-4o-mini ep1, "
              f"{len(jobs)} to call (after resume-skip)", flush=True)
        wall0 = time.time()
        with cf.ThreadPoolExecutor(max_workers=min(MAX_CONCURRENCY, max(1, len(jobs)))) as ex:
            futs = [ex.submit(do_one, *j) for j in jobs]
            for f in cf.as_completed(futs):
                f.result()
        for h in _file_handles.values():
            try:
                h.close()
            except Exception:
                pass
        print(f"[s17 smoke] done in {time.time()-wall0:.1f}s  "
              f"cost ${_cost['usd']:.5f}  failures {len(_failures)}", flush=True)
        if _failures:
            print(json.dumps(_failures, indent=2))
        return

    # -------- FULL RUN: epoch-major, cheapest-SUT-first within each epoch -------- #
    wall0 = time.time()
    print(f"[s17] scored items {n_items}  SUTs {len(SUTS)}  epochs {len(EPOCHS)}  "
          f"planned {n_items*len(SUTS)*len(EPOCHS)}  cap ${COST_CAP_USD:.2f}",
          flush=True)

    for epoch in EPOCHS:
        for tag in SUT_ORDER:
            if _stop.is_set():
                break
            model = TAG_TO_MODEL[tag]
            done = load_done_ids(tag, epoch)
            jobs = [(model, tag, epoch, iid, inputs[iid])
                    for iid in ordered_ids if iid not in done]
            print(f"[s17] epoch {epoch} SUT {tag}: {len(jobs)} to run "
                  f"(after resume-skip)  cost-so-far ${_cost['usd']:.4f}", flush=True)
            with cf.ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as ex:
                futs = [ex.submit(do_one, *j) for j in jobs]
                for f in cf.as_completed(futs):
                    f.result()
            # Incremental summary update so progress is monitorable.
            write_summary(n_items, time.time() - wall0, _cap_hit.is_set())
            print(f"[s17] epoch {epoch} SUT {tag} DONE  "
                  f"cost-so-far ${_cost['usd']:.4f}", flush=True)
        if _stop.is_set():
            break

    for h in _file_handles.values():
        try:
            h.close()
        except Exception:
            pass

    summary = write_summary(n_items, time.time() - wall0, _cap_hit.is_set())

    # Completion flag only if every cell reached the full item count and no cap.
    all_complete = all(c["complete"] for c in summary["per_sut_epoch"].values())
    if all_complete and not _cap_hit.is_set():
        (OUT_DIR / "RUNNER-DONE").write_text(
            json.dumps({"done": True, "n_items": n_items,
                        "cost_usd": round(_cost["usd"], 5)}, indent=2))
        print("[s17] RUNNER-DONE written.", flush=True)
    else:
        print(f"[s17] NOT complete (all_complete={all_complete}, "
              f"cap_hit={_cap_hit.is_set()}) — RUNNER-DONE not written.", flush=True)
    print(json.dumps({k: summary[k] for k in
                      ("n_items", "cap_hit", "estimated_total_cost_usd",
                       "cost_accumulator_usd", "n_failures")}, indent=2), flush=True)
    if _cap_hit.is_set():
        print("\n*** COST CAP HIT — run stopped early ***", flush=True)


if __name__ == "__main__":
    main()
