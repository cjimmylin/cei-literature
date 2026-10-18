"""v4-T known-groups tier probe: do d01/d05 differentiate Claude Haiku/Sonnet/Opus?

WALKWORTHY-CANARY-7f3e2026

Authorized by RULINGS-APPLIED-20260802a (boot prompt 20260802b §4). SUT
administration runs through the Claude Code CLI in headless print mode under the
machine's subscription OAuth ($0 external spend) — the pattern is ported from
`COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/wcfbench/cli_client.py`
(CLIModelClient), including its honesty caveats: subscription OAuth is for
modest-scale runs only (this census is capped at 486 SUT calls + §4.4 d05 format
retries), the CLI exposes no temperature/seed control, and every call carries
~10k tokens of harness overhead. The overhead is IDENTICAL across the three
tiers, so tier CONTRASTS are interpretable; absolute levels are NOT comparable
to the inspect_ai reference runs and must never be pooled with them.

Subcommands
-----------
  census   [--calibrate]   SUT administration (d01 49 + d05 32 lines x 3 models
                           x 2 epochs = 486 calls; --calibrate = 1 d01 + 1 d05
                           item x 3 models x 1 epoch = 6 calls). Resume-safe
                           append-only JSONL; d05 rows apply the instrument's
                           one-retry format rule inline (solver F9 convention:
                           retry fires only when the first response fails even
                           after offline recovery).
  score-d05                Judge-free CSR scoring ($0): reparse_allocation_response
                           + item_csr, imported read-only from walkworthy_inspect.
  judge-d01 [--calibrate]  Cross-family judging via OpenRouter (gpt-4.1-nano +
                           llama-3.3-70b-instruct, temperature 0) under a $1.00
                           HARD ceiling. --calibrate = one item's 6 responses x
                           2 judges = 12 calls, then projection; the full pass
                           refuses to start if the projection exceeds the ceiling.
  analyze                  Pre-committed read-outs (boot §4.7) -> analysis JSON.

judge-d01 re-judge options (2026-10-18; RULINGS-APPLIED-20261018b Stage 2; absent = unchanged)
  --judge LABEL=SLUG         add a judge label or replace a label's OpenRouter slug
  --only-judges L1[,L2]      judge only with these labels (e.g. only the candidate)
  --price-bound SLUG=IN,OUT  $/M-token bound when no usage.cost is returned (REQUIRED for a
                             slug without a built-in bound)
  --responses PATH           stored responses to re-judge (read-only; default: this probe's
                             responses.jsonl). No SUT is ever called by judge-d01.
  --log-root PATH            NEW directory for d01_judgments.jsonl + judge_tally.txt
                             (REQUIRED whenever any option here is used)
  --ceiling USD              hard ceiling for this judging pass (default $1.00)

Instrument identity: tools/audit/ is NOT pinned by INSTRUMENT.json; everything
under walkworthy_inspect/ and datasets/ is imported/read strictly read-only.
Judge prompts reuse the single shipped assembly surface
`scorers.assemble_rubric_prompt` (no fork). Judge calls send the assembled
prompt as the sole USER message with no system prompt — matching the
instrument's live judge pass, which generates from the bare rubric prompt.

All numbers this tool produces are PROBE DIAGNOSTICS, never WALKWORTHY numbers.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import random
import re
import statistics
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from walkworthy_inspect.ordo_constraints import item_csr  # noqa: E402
from walkworthy_inspect.parsers import (  # noqa: E402
    _FORMAT_REMINDER,
    reparse_allocation_response,
)
from walkworthy_inspect.rubrics import judge_categories, spec_for  # noqa: E402
from walkworthy_inspect.scorers import (  # noqa: E402
    _JSON_OBJ_RE,
    _coerce,
    assemble_rubric_prompt,
)

# --------------------------------------------------------------------------- #
# constants
# --------------------------------------------------------------------------- #
CANARY = "WALKWORTHY-CANARY-7f3e2026"

#: Pinned FULL model ids (boot §3 fact 2 — aliases float and silently change
#: what is measured). The 5-family ids carry no date suffix by design.
SUTS = ("claude-haiku-4-5-20251001", "claude-sonnet-5", "claude-opus-5")
EPOCHS = (1, 2)

BANKS = {
    "01": _V2_ROOT / "datasets" / "public" / "design01.jsonl",
    "05": _V2_ROOT / "datasets" / "public" / "design05.jsonl",
}

LOG_ROOT = _V2_ROOT / "logs" / "tier-probe-20260802"
RESPONSES_PATH = LOG_ROOT / "responses.jsonl"
SUT_TALLY_PATH = LOG_ROOT / "sut_tally.txt"
D05_SCORES_PATH = LOG_ROOT / "d05_scores.jsonl"
D01_JUDGE_PATH = LOG_ROOT / "d01_judgments.jsonl"
JUDGE_TALLY_PATH = LOG_ROOT / "judge_tally.txt"
ANALYSIS_PATH = LOG_ROOT / "analysis.json"

CLI_TIMEOUT_S = 300.0
SUT_CONCURRENCY = 4          # boot §4.2: modest parallelism, <= 4 subprocesses

# OpenRouter judging (ported from tools/audit/d02_davidson_bt_pilot.py)
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
JUDGES = {
    "judge-A": "openai/gpt-4.1-nano",
    "judge-B": "meta-llama/llama-3.3-70b-instruct",
}
PRICE_BOUND = {                       # $/Mtok (input, output) upper bounds
    "openai/gpt-4.1-nano": (0.10, 0.40),
    "meta-llama/llama-3.3-70b-instruct": (0.10, 0.30),
}
JUDGE_MAX_TOKENS = 4096               # scorers.JUDGE_MAX_TOKENS
JUDGE_CEILING_USD = 1.00              # RULINGS-APPLIED-20260802a hard ceiling
JUDGE_CONCURRENCY = 4

BOOT_SEED = 20260802
BOOTSTRAP_B = 10_000


# --------------------------------------------------------------------------- #
# safety tripwires
# --------------------------------------------------------------------------- #
def tripwires() -> None:
    if os.environ.get("WALKWORTHY_ALLOW_HOLDOUT"):
        sys.exit("ABORT: WALKWORTHY_ALLOW_HOLDOUT is set — the tier probe must "
                 "never run in a holdout-enabled environment.")
    for path in BANKS.values():
        sp = str(path)
        if "datasets/public" not in sp.replace("\\", "/") or "holdout" in sp.lower():
            sys.exit(f"ABORT: bank path fails the public-only tripwire: {sp}")
    if "rescore" in str(LOG_ROOT).lower():
        sys.exit("ABORT: log root must never contain the substring 'rescore'.")


def load_bank(design: str) -> List[dict]:
    rows = []
    with BANKS[design].open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            s = json.loads(line)
            canary = (s.get("metadata") or {}).get("canary")
            if canary != CANARY:
                sys.exit(f"ABORT: canary mismatch on sample {s.get('id')!r}: {canary!r}")
            rows.append(s)
    expected = {"01": 49, "05": 32}[design]
    if len(rows) != expected:
        sys.exit(f"ABORT: design{design} bank has {len(rows)} lines, expected {expected}")
    return rows


def sample_frames(s: dict) -> Tuple[Optional[str], str]:
    """-> (system_text or None, user_text). Banks are single-turn (multiturn None)."""
    msgs = s["input"]
    system = next((m["content"] for m in msgs if m["role"] == "system"), None)
    user = next(m["content"] for m in msgs if m["role"] == "user")
    return system, user


# --------------------------------------------------------------------------- #
# SUT channel: claude CLI headless print mode (subscription OAuth)
# --------------------------------------------------------------------------- #
class CLIError(RuntimeError):
    pass


class UnknownFlagError(CLIError):
    pass


def _cli_env() -> Dict[str, str]:
    env = dict(os.environ)
    # These would switch billing to API pay-as-you-go; drop them so the
    # subscription OAuth login is used (probe-confirmed apiKeySource: none).
    env.pop("ANTHROPIC_API_KEY", None)
    env.pop("ANTHROPIC_AUTH_TOKEN", None)
    return env


def _clean_cwd() -> str:
    """A CLAUDE.md-free cwd so vault memory cannot steer the model under test."""
    clean = os.path.join(tempfile.gettempdir(), "walkworthy-tierprobe-clean")
    os.makedirs(clean, exist_ok=True)
    marker = os.path.join(clean, "CLAUDE.md")
    if os.path.exists(marker):
        sys.exit(f"ABORT: clean cwd unexpectedly contains a CLAUDE.md: {marker}")
    return clean


def _hygiene_flags(max_turns_supported: bool) -> List[str]:
    # Verified against claude 2.1.220: --tools/--strict-mcp-config/
    # --permission-mode/--setting-sources/--system-prompt all present in
    # `claude -p --help`; --max-turns is absent from the help text, so its
    # support is probed on the first call and the mode FROZEN for the run.
    flags = ["--tools", "", "--strict-mcp-config",
             "--permission-mode", "dontAsk", "--setting-sources", ""]
    if max_turns_supported:
        flags += ["--max-turns", "1"]
    return flags


def cli_call(model: str, user_text: str, system_text: Optional[str],
             max_turns_supported: bool) -> Dict[str, Any]:
    """One headless single-turn completion. -> {text, cost_usd, duration_s, error}."""
    cmd = ["claude", "-p", user_text, "--model", model,
           "--output-format", "json", *_hygiene_flags(max_turns_supported)]
    if system_text:
        cmd += ["--system-prompt", system_text]
    t0 = time.time()
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              timeout=CLI_TIMEOUT_S, cwd=_clean_cwd(), env=_cli_env())
    except subprocess.TimeoutExpired:
        return {"text": "", "cost_usd": 0.0, "duration_s": time.time() - t0,
                "error": f"timeout after {CLI_TIMEOUT_S}s"}
    duration = time.time() - t0
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip()[:400]
        if "unknown option" in err and "--max-turns" in err:
            raise UnknownFlagError(err)
        return {"text": "", "cost_usd": 0.0, "duration_s": duration,
                "error": f"exit {proc.returncode}: {err}"}
    try:
        data = json.loads((proc.stdout or "").strip())
    except json.JSONDecodeError as exc:
        return {"text": "", "cost_usd": 0.0, "duration_s": duration,
                "error": f"stdout not JSON: {exc}"}
    events = data if isinstance(data, list) else [data]
    for ev in reversed(events):
        if isinstance(ev, dict) and ev.get("type") == "result":
            if ev.get("is_error"):
                return {"text": "", "cost_usd": float(ev.get("total_cost_usd") or 0.0),
                        "duration_s": duration,
                        "error": f"result error: {ev.get('subtype')}"}
            return {"text": str(ev.get("result", "")),
                    "cost_usd": float(ev.get("total_cost_usd") or 0.0),
                    "duration_s": duration, "error": None}
    if isinstance(data, dict) and "result" in data:
        return {"text": str(data["result"]),
                "cost_usd": float(data.get("total_cost_usd") or 0.0),
                "duration_s": duration, "error": None}
    return {"text": "", "cost_usd": 0.0, "duration_s": duration,
            "error": "no type:result element in CLI json output"}


def probe_max_turns_flag() -> bool:
    """Probe --max-turns support with one tiny haiku call; freeze the answer.

    An unknown option makes the CLI error out instantly at argv-parse time
    (no model call); a supported flag runs one trivial completion (subscription
    OAuth, counted in the tally as the probe row).
    """
    try:
        res = cli_call(SUTS[0], "Reply with exactly: OK", None, max_turns_supported=True)
    except UnknownFlagError:
        return False
    if res["error"] and "unknown option" in res["error"]:
        return False
    if res["error"]:
        sys.exit(f"ABORT: flag probe failed for another reason: {res['error']}")
    return True


# --------------------------------------------------------------------------- #
# append-only ledgers (pattern: d02_davidson_bt_pilot.Ledger)
# --------------------------------------------------------------------------- #
def load_jsonl(path: Path) -> List[dict]:
    rows = []
    if path.exists():
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    continue
    return rows


class Ledger:
    """Append-only JSONL + running tally, thread-safe. ceiling_usd None = no ceiling
    (the SUT channel is subscription OAuth; cost_usd is informational there)."""

    def __init__(self, path: Path, tally_path: Path, prior: List[dict],
                 ceiling_usd: Optional[float]):
        self.path = path
        self.tally_path = tally_path
        self.ceiling = ceiling_usd
        self.lock = threading.Lock()
        self.spend = sum(float(r.get("cost_usd") or 0.0) for r in prior)
        self.n = len(prior)
        self.stopped = False

    def record(self, row: dict) -> None:
        with self.lock:
            self.spend += float(row.get("cost_usd") or 0.0)
            self.n += 1
            with self.path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
                fh.flush()
            if self.ceiling is not None and self.spend >= self.ceiling:
                self.stopped = True
            ceiling = "none (subscription OAuth)" if self.ceiling is None \
                else f"{self.ceiling:.2f}"
            self.tally_path.write_text(
                f"rows_recorded: {self.n}\nspend_usd: {self.spend:.6f}\n"
                f"ceiling_usd: {ceiling}\nhard_stopped: {self.stopped}\n",
                encoding="utf-8")
            if self.n % 20 == 0 or self.stopped:
                print(f"    ... {self.n} rows, running spend ${self.spend:.4f}")


# --------------------------------------------------------------------------- #
# census (SUT administration)
# --------------------------------------------------------------------------- #
def d05_alloc_spec(s: dict) -> Tuple[List[str], float, str]:
    keyed = (s["metadata"].get("keyed") or {})
    alloc = (keyed.get("allocation")
             or (keyed.get("extras", {}) or {}).get("allocation") or {})
    tokens = alloc.get("tokens", []) or []
    budget = float(alloc.get("budget", 0) or 0)
    constraints = keyed.get("keyed_constraints", "") or alloc.get("constraints", "")
    return tokens, budget, constraints


def response_key(row: dict) -> Tuple:
    return (row["design"], row["id"], row["model"], row["epoch"], row["attempt"])


def run_census(calibrate: bool) -> None:
    tripwires()
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    banks = {d: load_bank(d) for d in ("01", "05")}
    cli_version = subprocess.run(["claude", "--version"], capture_output=True,
                                 text=True, timeout=15).stdout.strip()

    prior = load_jsonl(RESPONSES_PATH)
    done = {response_key(r) for r in prior if not r.get("error")}
    max_turns_supported = None
    for r in prior:
        if "max_turns_flag" in r:
            max_turns_supported = bool(r["max_turns_flag"])
            break
    if max_turns_supported is None:
        max_turns_supported = probe_max_turns_flag()
        print(f"  --max-turns flag supported by installed CLI: {max_turns_supported}")
    ledger = Ledger(RESPONSES_PATH, SUT_TALLY_PATH, prior, ceiling_usd=None)

    if calibrate:
        plan_samples = [( "01", banks["01"][0]), ("05", banks["05"][0])]
        epochs: Tuple[int, ...] = (1,)
    else:
        plan_samples = [("01", s) for s in banks["01"]] + [("05", s) for s in banks["05"]]
        epochs = EPOCHS

    jobs = [(design, s, model, ep)
            for design, s in plan_samples for model in SUTS for ep in epochs
            if (design, s["id"], model, ep, 1) not in done]
    total_planned = len(plan_samples) * len(SUTS) * len(epochs)
    print(f"  plan={total_planned} already_done={total_planned - len(jobs)} to_run={len(jobs)}")

    def one(job: Tuple[str, dict, str, int]) -> None:
        design, s, model, ep = job
        system_text, user_text = sample_frames(s)
        base = {
            "design": design, "id": s["id"],
            "item_id": s["metadata"]["item_id"], "admin": s["metadata"]["admin"],
            "model": model, "epoch": ep,
            "system_mode": "flag" if system_text else "none",
            "max_turns_flag": max_turns_supported, "cli_version": cli_version,
        }
        res = cli_call(model, user_text, system_text, max_turns_supported)
        ledger.record({**base, "attempt": 1, "response": res["text"],
                       "cost_usd": res["cost_usd"], "duration_s": round(res["duration_s"], 2),
                       "error": res["error"]})
        # d05 one-retry format rule (solver F9 convention): retry ONLY when the
        # first response fails even after the bounded offline recovery pass.
        if design == "05" and not res["error"]:
            tokens, budget, _ = d05_alloc_spec(s)
            if not reparse_allocation_response(res["text"], tokens, budget).ok:
                retry_user = user_text + "\n\n" + _FORMAT_REMINDER
                res2 = cli_call(model, retry_user, system_text, max_turns_supported)
                ledger.record({**base, "attempt": 2, "response": res2["text"],
                               "cost_usd": res2["cost_usd"],
                               "duration_s": round(res2["duration_s"], 2),
                               "error": res2["error"]})

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=SUT_CONCURRENCY) as pool:
        futures = [pool.submit(one, j) for j in jobs]
        for f in as_completed(futures):
            f.result()
    wall = time.time() - t0
    print(f"  census pass complete: {len(jobs)} first-pass calls in {wall/60:.1f} min "
          f"({wall/max(len(jobs),1):.1f} s/call incl. concurrency)")
    if calibrate and jobs:
        per_call = wall / len(jobs)
        print(f"  projection for 486 first-pass calls at concurrency {SUT_CONCURRENCY}: "
              f"~{486 * per_call / 60:.0f} min")


# --------------------------------------------------------------------------- #
# d05 scoring ($0, judge-free)
# --------------------------------------------------------------------------- #
def pick_scoring_rows(rows: List[dict]) -> Dict[Tuple, dict]:
    """(design,id,model,epoch) -> the row to score. Last non-error attempt-1 row;
    a d05 attempt-2 retry row is used ONLY when attempt 1 never parsed (F9)."""
    first: Dict[Tuple, dict] = {}
    retry: Dict[Tuple, dict] = {}
    for r in rows:
        if r.get("error"):
            continue
        k = (r["design"], r["id"], r["model"], r["epoch"])
        (first if r["attempt"] == 1 else retry)[k] = r
    return {"first": first, "retry": retry}  # type: ignore[return-value]


def run_score_d05() -> None:
    tripwires()
    bank = {s["id"]: s for s in load_bank("05")}
    rows = load_jsonl(RESPONSES_PATH)
    picked = pick_scoring_rows([r for r in rows if r["design"] == "05"])
    first, retry = picked["first"], picked["retry"]

    out: List[dict] = []
    for k, row in sorted(first.items()):
        s = bank[row["id"]]
        tokens, budget, constraints = d05_alloc_spec(s)
        parse1 = reparse_allocation_response(row["response"], tokens, budget)
        attempts = 1
        used = row
        parse = parse1
        if not parse1.ok and k in retry:
            attempts = 2
            used = retry[k]
            parse = reparse_allocation_response(used["response"], tokens, budget)
        csr = item_csr(parse.values, constraints, tokens) if parse.ok else None
        out.append({
            "design": "05", "id": row["id"], "item_id": row["item_id"],
            "model": row["model"], "epoch": row["epoch"], "attempts": attempts,
            "parse_ok": parse.ok, "unscorable": (not parse.ok) or csr is None,
            "csr": csr, "empty_response": not (used["response"] or "").strip(),
        })
    with D05_SCORES_PATH.open("w", encoding="utf-8") as fh:
        for r in out:
            fh.write(json.dumps(r) + "\n")
    n_ok = sum(1 for r in out if not r["unscorable"])
    print(f"  d05 scored: {len(out)} administrations, scorable {n_ok}, "
          f"unscorable {len(out) - n_ok}, retries used "
          f"{sum(1 for r in out if r['attempts'] == 2)}")


# --------------------------------------------------------------------------- #
# d01 judging (OpenRouter, $1.00 hard ceiling)
# --------------------------------------------------------------------------- #
def openrouter_call(model: str, prompt: str, api_key: str) -> Dict[str, Any]:
    """One chat completion; the assembled rubric prompt is the sole USER message
    (no system prompt — matches the instrument's live judge pass). Transport
    errors retried with backoff; parse retry is the caller's."""
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": JUDGE_MAX_TOKENS,
        "usage": {"include": True},
    }).encode("utf-8")
    last_err = None
    for attempt in range(4):
        req = urllib.request.Request(
            OPENROUTER_URL, data=body,
            headers={"Authorization": f"Bearer {api_key}",
                     "Content-Type": "application/json",
                     "X-Title": "walkworthy-v4t-tierprobe"})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                payload = json.loads(r.read().decode("utf-8"))
            choices = payload.get("choices") or []
            text = (choices[0].get("message") or {}).get("content") or "" if choices else ""
            usage = payload.get("usage") or {}
            cost = usage.get("cost")
            return {"text": text, "usage": usage,
                    "cost_actual": float(cost) if isinstance(cost, (int, float)) else None,
                    "error": None}
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
                ValueError, OSError) as exc:
            last_err = f"{type(exc).__name__}: {exc}"
            time.sleep(1.5 * (2 ** attempt))
    return {"text": "", "usage": {}, "cost_actual": None, "error": last_err}


def call_cost(model: str, usage: Dict[str, Any],
              cost_actual: Optional[float]) -> Tuple[float, str]:
    if cost_actual is not None:
        return cost_actual, "actual"
    pin, pout = PRICE_BOUND[model]
    tin = int(usage.get("prompt_tokens") or 0)
    tout = int(usage.get("completion_tokens") or 0)
    return (tin * pin + tout * pout) / 1_000_000.0, "bound"


def parse_judge_json(text: str, spec) -> Optional[Dict[str, Any]]:
    m = _JSON_OBJ_RE.search(text or "")
    if not m:
        return None
    try:
        obj = json.loads(m.group(0))
    except ValueError:
        return None
    if not isinstance(obj, dict):
        return None
    out = {}
    for cat in judge_categories(spec):
        out[cat.name] = _coerce(obj.get(cat.name), cat)
    return out


def judge_key(row: dict) -> Tuple:
    return (row["id"], row["model"], row["epoch"], row["judge"])


def run_judge_d01(calibrate: bool) -> None:
    tripwires()
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        sys.exit("ABORT: OPENROUTER_API_KEY not in environment. "
                 "source ~/.codex/secrets/openrouter.env first.")
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    spec = spec_for("01-goodsamaritan")
    bank = {s["id"]: s for s in load_bank("01")}

    resp_rows = [r for r in load_jsonl(RESPONSES_PATH)
                 if r["design"] == "01" and r["attempt"] == 1 and not r.get("error")]
    responses = {(r["id"], r["model"], r["epoch"]): r for r in resp_rows}

    prior = load_jsonl(D01_JUDGE_PATH)
    done = {judge_key(r) for r in prior if r.get("parsed") is not None or r.get("unscorable")}
    ledger = Ledger(D01_JUDGE_PATH, JUDGE_TALLY_PATH, prior, JUDGE_CEILING_USD)

    keys = sorted(responses.keys())
    if calibrate:
        first_item = keys[0][0]
        keys = [k for k in keys if k[0] == first_item]

    plan = [(k, judge) for k in keys for judge in JUDGES
            if (k[0], k[1], k[2], judge) not in done]
    print(f"  judge plan={len(keys) * len(JUDGES)} already_done="
          f"{len(keys) * len(JUDGES) - len(plan)} to_run={len(plan)} "
          f"(prior spend ${ledger.spend:.4f} of ${JUDGE_CEILING_USD:.2f})")

    # ceiling projection gate for the full pass: prior mean cost/call x remaining
    if not calibrate and prior:
        costs = [float(r.get("cost_usd") or 0.0) for r in prior]
        mean_cost = sum(costs) / len(costs)
        projection = ledger.spend + mean_cost * len(plan)
        print(f"  projection: mean ${mean_cost:.5f}/call x {len(plan)} remaining "
              f"-> total ${projection:.3f}")
        if projection > JUDGE_CEILING_USD:
            sys.exit(f"STOP: projected total ${projection:.3f} exceeds the "
                     f"${JUDGE_CEILING_USD:.2f} hard ceiling. Report to owner.")

    def one(job) -> None:
        if ledger.stopped:
            return
        (item_id, model, epoch), judge = job
        row = responses[(item_id, model, epoch)]
        s = bank[item_id]
        if not (row["response"] or "").strip():
            ledger.record({"id": item_id, "model": model, "epoch": epoch,
                           "judge": judge, "judge_model": JUDGES[judge],
                           "parsed": None, "unscorable": True,
                           "reason": "empty SUT response", "cost_usd": 0.0,
                           "attempts": 0})
            return
        prompt = assemble_rubric_prompt(s["metadata"], spec, row["response"],
                                        judge_categories(spec))
        attempts, cost_tot, basis, err = 0, 0.0, "bound", None
        parsed = None
        raw = ""
        for _ in range(2):                       # initial + ONE parse retry
            if ledger.stopped:
                break
            attempts += 1
            res = openrouter_call(JUDGES[judge], prompt, api_key)
            c, bs = call_cost(JUDGES[judge], res["usage"], res["cost_actual"])
            cost_tot += c
            basis = "actual" if bs == "actual" else basis
            err = res["error"]
            raw = res["text"]
            parsed = parse_judge_json(res["text"], spec)
            if parsed is not None and parsed.get("action_class") is not None:
                break
        ledger.record({"id": item_id, "model": model, "epoch": epoch,
                       "judge": judge, "judge_model": JUDGES[judge],
                       "parsed": parsed,
                       "unscorable": parsed is None or parsed.get("action_class") is None,
                       "reason": err, "raw": raw[:500],
                       "cost_usd": round(cost_tot, 6), "cost_basis": basis,
                       "attempts": attempts})

    with ThreadPoolExecutor(max_workers=JUDGE_CONCURRENCY) as pool:
        futures = [pool.submit(one, j) for j in plan]
        for f in as_completed(futures):
            f.result()
    print(f"  judging pass done: spend ${ledger.spend:.4f} of "
          f"${JUDGE_CEILING_USD:.2f} (hard_stopped={ledger.stopped})")
    if calibrate:
        rows = load_jsonl(D01_JUDGE_PATH)
        costs = [float(r.get("cost_usd") or 0.0) for r in rows]
        n_full = 588 if not _OVERRIDES["active"] else len(responses) * len(JUDGES)
        if costs:
            mean_cost = sum(costs) / len(costs)
            projection = mean_cost * n_full
            print(f"  calibration: mean ${mean_cost:.5f}/call -> projected full census "
                  f"({n_full} calls) ${projection:.3f} "
                  f"[{'OK under' if projection <= JUDGE_CEILING_USD else 'EXCEEDS'} "
                  f"${JUDGE_CEILING_USD:.2f} ceiling]")


# --------------------------------------------------------------------------- #
# analysis (boot §4.7 pre-committed read-outs)
# --------------------------------------------------------------------------- #
def mean(xs: List[float]) -> Optional[float]:
    return sum(xs) / len(xs) if xs else None


def item_clustered_bootstrap_ci(per_item: Dict[str, Tuple[List[float], List[float]]],
                                b: int = BOOTSTRAP_B,
                                seed: int = BOOT_SEED) -> Dict[str, Any]:
    """CI for mean(model_hi) - mean(model_lo) resampling ITEMS with replacement.

    per_item: item_id -> (hi_scores, lo_scores) score lists (epochs, judges pooled
    at the caller's chosen level). Items where either side is empty are dropped.
    """
    items = sorted(i for i, (hi, lo) in per_item.items() if hi and lo)
    if not items:
        return {"n_items": 0, "diff": None, "ci95": None, "excludes_zero": None}
    hi_all = [x for i in items for x in per_item[i][0]]
    lo_all = [x for i in items for x in per_item[i][1]]
    diff = mean(hi_all) - mean(lo_all)                     # type: ignore[operator]
    rng = random.Random(seed)
    draws = []
    for _ in range(b):
        picks = [items[rng.randrange(len(items))] for _ in items]
        hi = [x for i in picks for x in per_item[i][0]]
        lo = [x for i in picks for x in per_item[i][1]]
        draws.append(mean(hi) - mean(lo))                  # type: ignore[operator]
    draws.sort()
    lo_ci = draws[int(0.025 * b)]
    hi_ci = draws[min(int(0.975 * b), b - 1)]
    return {"n_items": len(items), "diff": round(diff, 4),
            "ci95": [round(lo_ci, 4), round(hi_ci, 4)],
            "excludes_zero": (lo_ci > 0) or (hi_ci < 0)}


def rank_corr(xs: List[float], ys: List[float]) -> Optional[float]:
    """Spearman rho (average-rank ties), pure python."""
    if len(xs) < 3:
        return None

    def ranks(v: List[float]) -> List[float]:
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    return pearson(ranks(xs), ranks(ys))


def pearson(xs: List[float], ys: List[float]) -> Optional[float]:
    n = len(xs)
    if n < 3:
        return None
    mx, my = mean(xs), mean(ys)
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))          # type: ignore[operator]
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))          # type: ignore[operator]
    if sx == 0 or sy == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (sx * sy)  # type: ignore[operator]


TIER_ORDER = {SUTS[0]: 0, SUTS[1]: 1, SUTS[2]: 2}          # haiku < sonnet < opus
CONTRASTS = [("claude-opus-5", "claude-haiku-4-5-20251001", "opus_minus_haiku"),
             ("claude-opus-5", "claude-sonnet-5", "opus_minus_sonnet"),
             ("claude-sonnet-5", "claude-haiku-4-5-20251001", "sonnet_minus_haiku")]


def run_analyze() -> None:
    tripwires()
    resp = load_jsonl(RESPONSES_PATH)
    d05 = load_jsonl(D05_SCORES_PATH)
    d01j = load_jsonl(D01_JUDGE_PATH)
    out: Dict[str, Any] = {"probe": "v4-T tier probe (diagnostics only)",
                           "canary": CANARY, "bootstrap_b": BOOTSTRAP_B,
                           "seed": BOOT_SEED}

    # ---- administration / refusal / error rates by tier --------------------
    admin: Dict[str, Any] = {}
    for m in SUTS:
        rows1 = [r for r in resp if r["model"] == m and r["attempt"] == 1]
        admin[m] = {
            "first_pass_calls": len(rows1),
            "cli_errors": sum(1 for r in rows1 if r.get("error")),
            "empty_responses": sum(1 for r in rows1
                                   if not r.get("error") and not (r["response"] or "").strip()),
            "d05_retries": sum(1 for r in resp
                               if r["model"] == m and r["attempt"] == 2),
            "cost_usd_reported": round(sum(float(r.get("cost_usd") or 0.0)
                                           for r in resp if r["model"] == m), 4),
        }
    out["administration"] = admin

    # ---- d05 (objective CSR) ----------------------------------------------
    d05_by_model = {m: [r["csr"] for r in d05
                        if r["model"] == m and not r["unscorable"]] for m in SUTS}
    d05_block: Dict[str, Any] = {
        "mean_csr_by_tier": {m: (round(mean(v), 4) if v else None)
                             for m, v in d05_by_model.items()},
        "scorable_by_tier": {m: len(v) for m, v in d05_by_model.items()},
        "parse_failure_rate_by_tier": {
            m: round(sum(1 for r in d05 if r["model"] == m and r["unscorable"])
                     / max(sum(1 for r in d05 if r["model"] == m), 1), 4)
            for m in SUTS},
    }
    for hi, lo, name in CONTRASTS:
        per_item: Dict[str, Tuple[List[float], List[float]]] = {}
        for item in {r["item_id"] for r in d05}:
            hi_v = [r["csr"] for r in d05 if r["item_id"] == item
                    and r["model"] == hi and not r["unscorable"]]
            lo_v = [r["csr"] for r in d05 if r["item_id"] == item
                    and r["model"] == lo and not r["unscorable"]]
            per_item[item] = (hi_v, lo_v)
        d05_block[name] = item_clustered_bootstrap_ci(per_item)
    # per-item discrimination
    item_means: Dict[str, Dict[str, Optional[float]]] = {}
    for item in sorted({r["item_id"] for r in d05}):
        item_means[item] = {m: mean([r["csr"] for r in d05 if r["item_id"] == item
                                     and r["model"] == m and not r["unscorable"]])
                            for m in SUTS}
    full = {i: v for i, v in item_means.items() if all(x is not None for x in v.values())}
    d05_block["items_with_all_tiers_scorable"] = len(full)
    d05_block["share_opus_gt_haiku"] = round(
        sum(1 for v in full.values() if v[SUTS[2]] > v[SUTS[0]]) / len(full), 4) if full else None
    d05_block["share_strictly_monotone"] = round(
        sum(1 for v in full.values()
            if v[SUTS[2]] > v[SUTS[1]] > v[SUTS[0]]) / len(full), 4) if full else None
    d05_block["monotone_coarseness_note"] = (
        "3-tier orderings have 6 permutations; a strict-monotone share near 1/6 "
        "is chance-level, and CSR ties (common at ceiling) further deflate it")
    out["d05_objective"] = d05_block

    # ---- d01 (judged) ------------------------------------------------------
    scored = [r for r in d01j if not r.get("unscorable")]
    d01_block: Dict[str, Any] = {"judged_rows": len(d01j), "scorable_rows": len(scored),
                                 "unscorable_rows": len(d01j) - len(scored)}
    per_judge: Dict[str, Any] = {}
    for judge in JUDGES:
        jr = [r for r in scored if r["judge"] == judge]
        block: Dict[str, Any] = {
            "keyed_class_rate_by_tier": {}, "rationale_quality_mean_by_tier": {}}
        for m in SUTS:
            mr = [r for r in jr if r["model"] == m]
            prim = [1.0 if r["parsed"]["action_class"] == "full_obedience" else 0.0
                    for r in mr]
            rq = [float(r["parsed"]["rationale_quality"]) for r in mr
                  if r["parsed"].get("rationale_quality") is not None]
            block["keyed_class_rate_by_tier"][m] = round(mean(prim), 4) if prim else None
            block["rationale_quality_mean_by_tier"][m] = round(mean(rq), 4) if rq else None
        for hi, lo, name in CONTRASTS:
            per_item = {}
            for item in {r["id"] for r in jr}:
                hi_v = [1.0 if r["parsed"]["action_class"] == "full_obedience" else 0.0
                        for r in jr if r["id"] == item and r["model"] == hi]
                lo_v = [1.0 if r["parsed"]["action_class"] == "full_obedience" else 0.0
                        for r in jr if r["id"] == item and r["model"] == lo]
                per_item[item] = (hi_v, lo_v)
            block[name] = item_clustered_bootstrap_ci(per_item)
        # per-item discrimination for this judge
        imeans = {}
        for item in sorted({r["id"] for r in jr}):
            imeans[item] = {m: mean([1.0 if r["parsed"]["action_class"] == "full_obedience"
                                     else 0.0 for r in jr
                                     if r["id"] == item and r["model"] == m])
                            for m in SUTS}
        ifull = {i: v for i, v in imeans.items() if all(x is not None for x in v.values())}
        block["share_opus_gt_haiku"] = round(
            sum(1 for v in ifull.values() if v[SUTS[2]] > v[SUTS[0]]) / len(ifull), 4) \
            if ifull else None
        block["share_strictly_monotone"] = round(
            sum(1 for v in ifull.values()
                if v[SUTS[2]] > v[SUTS[1]] > v[SUTS[0]]) / len(ifull), 4) \
            if ifull else None
        block["_item_means"] = ifull
        per_judge[judge] = block
    d01_block["per_judge"] = per_judge

    # cross-judge agreement on tier contrasts (the d02-crux out-of-sample check)
    xj: Dict[str, Any] = {}
    for _, _, name in CONTRASTS:
        a = per_judge["judge-A"].get(name, {})
        b = per_judge["judge-B"].get(name, {})
        if a.get("diff") is not None and b.get("diff") is not None:
            xj[f"{name}_sign_agreement"] = (
                (a["diff"] > 0) == (b["diff"] > 0) if a["diff"] * b["diff"] != 0
                else "a zero-diff side")
    ia = per_judge["judge-A"].pop("_item_means")
    ib = per_judge["judge-B"].pop("_item_means")
    common = sorted(set(ia) & set(ib))
    for label, fn in (("pearson", pearson), ("spearman", rank_corr)):
        xj[f"item_mean_score_corr_{label}"] = (
            round(v, 4) if (v := fn([mean(list(ia[i].values())) for i in common],
                                    [mean(list(ib[i].values())) for i in common])) is not None
            else None)
    # per-item Opus-Haiku gap correlation across judges (contrast-level agreement)
    ga = [ia[i][SUTS[2]] - ia[i][SUTS[0]] for i in common]
    gb = [ib[i][SUTS[2]] - ib[i][SUTS[0]] for i in common]
    for label, fn in (("pearson", pearson), ("spearman", rank_corr)):
        v = fn(ga, gb)
        xj[f"item_opus_haiku_gap_corr_{label}"] = round(v, 4) if v is not None else None
    # raw response-level agreement on action_class
    byk: Dict[Tuple, Dict[str, str]] = {}
    for r in scored:
        byk.setdefault((r["id"], r["model"], r["epoch"]), {})[r["judge"]] = \
            r["parsed"]["action_class"]
    both = [v for v in byk.values() if len(v) == 2]
    xj["response_level_action_class_agreement"] = (
        round(sum(1 for v in both if v["judge-A"] == v["judge-B"]) / len(both), 4)
        if both else None)
    xj["response_pairs_with_both_judges"] = len(both)
    d01_block["cross_judge"] = xj
    out["d01_judged"] = d01_block

    ANALYSIS_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    print(f"\n  analysis written to {ANALYSIS_PATH}")


# --------------------------------------------------------------------------- #
# judge-d01 re-judge overrides (2026-10-18; RULINGS-APPLIED-20261018b Stage 2)
# --------------------------------------------------------------------------- #
_DEFAULT_LOG_ROOT = LOG_ROOT
_OVERRIDES = {"active": False}
_LABEL_RE = re.compile(r"^[A-Za-z0-9_.-]+$")
_SLUG_RE = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._:-]+$")


def apply_judge_d01_overrides(args: argparse.Namespace) -> None:
    """Rebind the judging globals for a re-judge of STORED responses. No option -> no-op."""
    global LOG_ROOT, RESPONSES_PATH, D01_JUDGE_PATH, JUDGE_TALLY_PATH, JUDGE_CEILING_USD
    active = bool(args.judge or args.only_judges or args.price_bound or args.log_root
                  or args.responses or args.ceiling is not None)
    if not active:
        return
    for spec in args.price_bound:
        slug, sep, nums = spec.partition("=")
        parts = nums.split(",")
        if not sep or not _SLUG_RE.match(slug) or len(parts) != 2:
            sys.exit(f"ABORT: bad --price-bound {spec!r}; expected SLUG=IN,OUT ($/M tokens)")
        try:
            PRICE_BOUND[slug] = (float(parts[0]), float(parts[1]))
        except ValueError:
            sys.exit(f"ABORT: bad --price-bound numbers in {spec!r}")
    for spec in args.judge:
        label, sep, slug = spec.partition("=")
        if not sep or not _LABEL_RE.match(label) or not _SLUG_RE.match(slug):
            sys.exit(f"ABORT: bad --judge {spec!r}; expected LABEL=vendor/model")
        JUDGES[label] = slug
    if args.only_judges:
        keep = [x.strip() for x in args.only_judges.split(",") if x.strip()]
        unknown = [x for x in keep if x not in JUDGES]
        if not keep or unknown:
            sys.exit(f"ABORT: --only-judges names unknown label(s) {unknown}; "
                     f"known: {sorted(JUDGES)}")
        for label in list(JUDGES):
            if label not in keep:
                del JUDGES[label]
    missing = sorted({s for s in JUDGES.values() if s not in PRICE_BOUND})
    if missing:
        sys.exit(f"ABORT: no price bound for {missing}; pass --price-bound SLUG=IN,OUT")
    if args.responses:
        RESPONSES_PATH = Path(args.responses)
        if "holdout" in str(RESPONSES_PATH).lower():
            sys.exit("ABORT: --responses path fails the public-only tripwire.")
        if not RESPONSES_PATH.exists():
            sys.exit(f"ABORT: --responses {RESPONSES_PATH} does not exist.")
    if not args.log_root:
        sys.exit("ABORT: re-judge options require a NEW --log-root (the v4-T ledger "
                 f"{_DEFAULT_LOG_ROOT} is closed).")
    LOG_ROOT = Path(args.log_root)
    if LOG_ROOT.resolve() == _DEFAULT_LOG_ROOT.resolve():
        sys.exit(f"ABORT: {LOG_ROOT} is the closed v4-T ledger; use a NEW --log-root.")
    D01_JUDGE_PATH = LOG_ROOT / "d01_judgments.jsonl"
    JUDGE_TALLY_PATH = LOG_ROOT / "judge_tally.txt"
    if args.ceiling is not None:
        JUDGE_CEILING_USD = float(args.ceiling)
    _OVERRIDES["active"] = True
    print(f"  re-judge options active: judges={JUDGES}  responses={RESPONSES_PATH}  "
          f"log_root={LOG_ROOT}  ceiling=${JUDGE_CEILING_USD:.2f}  "
          f"price bounds={ {s: PRICE_BOUND[s] for s in JUDGES.values()} }")


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_census = sub.add_parser("census")
    p_census.add_argument("--calibrate", action="store_true")
    sub.add_parser("score-d05")
    p_judge = sub.add_parser("judge-d01")
    p_judge.add_argument("--calibrate", action="store_true")
    p_judge.add_argument("--judge", action="append", default=[], metavar="LABEL=SLUG")
    p_judge.add_argument("--only-judges", default=None, metavar="L1[,L2]")
    p_judge.add_argument("--price-bound", action="append", default=[], metavar="SLUG=IN,OUT")
    p_judge.add_argument("--responses", default=None, metavar="PATH")
    p_judge.add_argument("--log-root", default=None, metavar="PATH")
    p_judge.add_argument("--ceiling", type=float, default=None, metavar="USD")
    sub.add_parser("analyze")
    args = ap.parse_args()
    if args.cmd == "census":
        run_census(args.calibrate)
    elif args.cmd == "score-d05":
        run_score_d05()
    elif args.cmd == "judge-d01":
        apply_judge_d01_overrides(args)
        run_judge_d01(args.calibrate)
    elif args.cmd == "analyze":
        run_analyze()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# WALKWORTHY-CANARY-7f3e2026
