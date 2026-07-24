"""Session-14 Phase-2: offline STRICT-judge calibration against LOGGED s13 SUT
responses (NO SUT calls — completions come from the s13 .eval logs only).

For each of 26 calibration items x {qwen, haiku} SUT x 3 judges (the default
panel: gemini-2.5-flash / deepseek-chat / mistral-small-2603), we render the
STRICT grading prompt EXACTLY as the strict scorer path would and call the judge
via OpenRouter. We DO NOT re-implement the template rendering: the prompt is
assembled through the same steps the Inspect scorer uses —

  answer    = neutralize_structural_delimiters(defang_wcf_markers(completion))
  question  = neutralize_structural_delimiters(sample.input_text)
  criterion = neutralize_structural_delimiters(sample.target.text)
  prompt    = GRADE_TEMPLATE_STRICT.format(question=, answer=, criterion=,
                                           instructions=GRADE_INSTRUCTIONS, **md)

`defang_wcf_markers` is the WCF GP-02 sanitizer applied by bounded_grader's
_sanitize_state_for_grading BEFORE the inner scorer; `neutralize_structural_
delimiters` + `.format(**metadata)` are what model_scoring_prompt does inside
model_graded_qa. GRADE_TEMPLATE_STRICT / GRADE_INSTRUCTIONS are imported from
wcf_tasks (the strict_judge=True path), never re-typed.

Parsing: numeric score via the SAME last-match GRADE pattern (wcf_grading.
parse_grade). Fabrication: analysis/strict_quote_check.check_judge_grading
against the (defanged) SUT answer text the judge actually saw.

Config: temperature=0.0 (matches the panel scorer default grader_temperature=0.0
in wcf_tasks.wcf_s12_new_main). Concurrency <=8, exponential backoff, one retry
pass for empty/unparseable outputs, cost guard at $1.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import threading
import concurrent.futures as cf
from pathlib import Path

import urllib.request
import urllib.error

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))
sys.path.insert(0, str(WCF_ROOT / "analysis"))

from inspect_ai.log import read_eval_log  # noqa: E402
from inspect_ai.scorer._model import neutralize_structural_delimiters  # noqa: E402

# Import the STRICT rendering machinery — do NOT fork it.
from wcf_tasks import GRADE_TEMPLATE_STRICT, GRADE_INSTRUCTIONS  # noqa: E402
from wcf_grading import defang_wcf_markers, parse_grade  # noqa: E402
from strict_quote_check import check_judge_grading  # noqa: E402

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
LOG_DIR = WCF_ROOT / "logs" / "20260724-session13-gate-main"
QWEN_LOG = LOG_DIR / "2026-07-24T18-18-49-00-00_wcf-s12-new-main_V7zvwPiPZYQ37PcSuhuWZj.eval"
HAIKU_LOG = LOG_DIR / "2026-07-24T18-41-26-00-00_wcf-s12-new-main_fKuyHPKvbTs7hq2WH4TaTs.eval"

SAMPLE_JSON = WCF_ROOT / "analysis" / "20260724-session14-calibration-sample.json"
S13_RESULTS = WCF_ROOT / "analysis" / "20260724-session13-gate-results.json"

# Iteration-0 results (READ-ONLY) — for the delta column/notes vs iteration 0.
ITER0_RESULTS = WCF_ROOT / "analysis" / "20260724-session14-calibration-results.json"

# Iteration-1 (i2) dated outputs. Iteration-0 files are historical snapshots and
# are NOT overwritten (override via WCF_S14_OUT_TAG env if a later iteration runs).
_OUT_TAG = os.environ.get("WCF_S14_OUT_TAG", "20260724-session14-calibration-i2")
OUT_JSON = WCF_ROOT / "analysis" / f"{_OUT_TAG}-results.json"
OUT_MD = WCF_ROOT / "analysis" / f"{_OUT_TAG}-summary.md"
# Short iteration label for the MD prose (e.g. "i3" from a ...-i3 tag).
_m_tag = re.search(r"(i\d+)$", _OUT_TAG)
ITER_LABEL = _m_tag.group(1) if _m_tag else _OUT_TAG

# Default panel (same 3 models as wcf_tasks.DEFAULT_GRADER, minus the openrouter/ prefix
# for the direct OpenRouter chat/completions endpoint).
JUDGES = {
    "gemini-2.5-flash": "google/gemini-2.5-flash",
    "deepseek-chat": "deepseek/deepseek-chat",
    "mistral-small-2603": "mistralai/mistral-small-2603",
}

GRADER_TEMPERATURE = 0.0  # matches wcf_s12_new_main default grader_temperature
MAX_CONCURRENCY = 8
# Per-run cap for iteration 1 (i2): $0.55. Cumulative calibration must stay < $1
# and iteration 0 spent $0.41. Override via WCF_S14_COST_CAP if needed.
COST_CAP_USD = float(os.environ.get("WCF_S14_COST_CAP", "0.55"))
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Rough OpenRouter blended $/token estimates (prompt+completion averaged) for the
# cost guard only — conservative upper bounds so we stop early rather than overspend.
# (gemini-flash ~ $0.30/M, deepseek-chat ~ $0.90/M, mistral-small ~ $0.20/M output).
COST_PER_TOKEN = {
    "gemini-2.5-flash": 0.40 / 1_000_000,
    "deepseek-chat": 1.10 / 1_000_000,
    "mistral-small-2603": 0.30 / 1_000_000,
}


def load_api_key() -> str:
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
# Cost tracking (thread-safe)
# --------------------------------------------------------------------------- #
_lock = threading.Lock()
_cost = {"tokens": 0, "usd": 0.0, "calls": 0}
_stop = threading.Event()


def add_cost(judge: str, prompt_toks: int, completion_toks: int) -> None:
    with _lock:
        total = prompt_toks + completion_toks
        _cost["tokens"] += total
        _cost["usd"] += total * COST_PER_TOKEN[judge]
        _cost["calls"] += 1
        if _cost["usd"] > COST_CAP_USD:
            _stop.set()


# --------------------------------------------------------------------------- #
# Render the STRICT prompt exactly as the scorer path would
# --------------------------------------------------------------------------- #
def render_strict_prompt(question: str, completion: str, criterion: str, metadata: dict):
    """Return (prompt_text, defanged_answer_seen_by_judge).

    Reproduces model_scoring_prompt + the WCF GP-02 defang layer:
      1. defang WCF markers in the SUT completion (bounded_grader step)
      2. inspect neutralize_structural_delimiters on answer/question/criterion
      3. template.format(question, answer, criterion, instructions, **metadata)
    """
    defanged = defang_wcf_markers(completion)
    answer = neutralize_structural_delimiters(defanged)
    q = neutralize_structural_delimiters(question)
    crit = neutralize_structural_delimiters(criterion)
    # metadata sans the 4 reserved template keys (model_graded_qa omits them).
    md = {k: v for k, v in (metadata or {}).items()
          if k not in ("question", "answer", "criterion", "instructions")}
    prompt = GRADE_TEMPLATE_STRICT.format(
        question=q, answer=answer, criterion=crit,
        instructions=GRADE_INSTRUCTIONS, **md,
    )
    # `answer` is the exact text the judge sees; fabrication check runs against it.
    return prompt, answer


# --------------------------------------------------------------------------- #
# Parse the RUBRIC EVIDENCE / GATE CHECK blocks out of a judge output
# --------------------------------------------------------------------------- #
# Tolerate markdown emphasis / backticks / stray spaces the judge may wrap the
# exact header in (gemini in iter-0 emitted verifying quotes but its block header
# did not parse under the strict literal-bracket match — format drift, not a
# content failure). We fence on the BEGIN/END marker TEXT, ignoring surrounding
# ``*``/``_``/`` ` `` decoration and whitespace.
_DEC = r"[\*_`\s]*"
_DELIV_BLOCK = re.compile(
    _DEC + r"\[BEGIN DELIVERABLE CHECK\]" + _DEC + r"(.*?)" + _DEC
    + r"\[END DELIVERABLE CHECK\]",
    re.IGNORECASE | re.DOTALL)
_RUBRIC_BLOCK = re.compile(
    _DEC + r"\[BEGIN RUBRIC EVIDENCE\]" + _DEC + r"(.*?)" + _DEC
    + r"\[END RUBRIC EVIDENCE\]",
    re.IGNORECASE | re.DOTALL)
_CREDITED_BLOCK = re.compile(
    _DEC + r"\[BEGIN CREDITED\]" + _DEC + r"(.*?)" + _DEC + r"\[END CREDITED\]",
    re.IGNORECASE | re.DOTALL)
_GATE_BLOCK = re.compile(
    _DEC + r"\[BEGIN GATE CHECK\]" + _DEC + r"(.*?)" + _DEC + r"\[END GATE CHECK\]",
    re.IGNORECASE | re.DOTALL)
_CRIT_LINE = re.compile(
    r"Criterion\s+(\d+)\s*(?:\([^)]*\))?\s*:\s*(full|half|zero)\b", re.IGNORECASE)
_GATE_LINE = re.compile(
    r'GATE\s*(?:"([^"]*)"|:)\s*[^:]*?:?\s*\b(yes|no)\b', re.IGNORECASE)
# DELIVERABLE CHECK lines. ARTIFACT REQUESTED: <phrase>; DELIVERED: <yes|no> — ...
_ARTIFACT_LINE = re.compile(r"ARTIFACT\s+REQUESTED\s*:\s*(.+)$", re.IGNORECASE | re.MULTILINE)
_DELIVERED_LINE = re.compile(r"DELIVERED\s*:\s*\b(yes|no)\b", re.IGNORECASE)
# The (absent) sentinel used for absence-based deductions inside RUBRIC EVIDENCE.
_ABSENT_LINE = re.compile(r"QUOTE\s*:\s*\(\s*absent\b", re.IGNORECASE)
# CREDITED: w1 + w2 + ... = TOTAL of MAX pts  → capture TOTAL and MAX.
_CREDITED_LINE = re.compile(
    r"CREDITED\s*:\s*.*?=\s*([0-9]+(?:\.[0-9]+)?)\s*(?:of|/)\s*([0-9]+(?:\.[0-9]+)?)",
    re.IGNORECASE)


def parse_blocks(text: str) -> dict:
    text = text or ""
    deliv = _DELIV_BLOCK.search(text)
    rub = _RUBRIC_BLOCK.search(text)
    cred = _CREDITED_BLOCK.search(text)
    gate = _GATE_BLOCK.search(text)
    deliv_txt = deliv.group(1).strip() if deliv else ""
    rub_txt = rub.group(1).strip() if rub else ""
    cred_txt = cred.group(1).strip() if cred else ""
    gate_txt = gate.group(1).strip() if gate else ""
    rubric_lines = [
        {"criterion": int(m.group(1)), "credit": m.group(2).lower()}
        for m in _CRIT_LINE.finditer(rub_txt)
    ]
    gate_answers = [
        {"gate": (m.group(1) or "").strip(), "committed": m.group(2).lower()}
        for m in _GATE_LINE.finditer(gate_txt)
    ]
    # DELIVERABLE CHECK.
    art_m = _ARTIFACT_LINE.search(deliv_txt)
    del_m = _DELIVERED_LINE.search(deliv_txt)
    artifact_requested = art_m.group(1).strip() if art_m else None
    delivered = (del_m.group(1).lower() == "yes") if del_m else None
    # count (absent) deductions in the rubric block (absence-based zeros).
    n_absent = len(_ABSENT_LINE.findall(rub_txt))
    # CREDITED arithmetic.
    cred_m = _CREDITED_LINE.search(cred_txt) or _CREDITED_LINE.search(text)
    credited_total = float(cred_m.group(1)) if cred_m else None
    credited_max = float(cred_m.group(2)) if cred_m else None
    return {
        "deliverable_block_present": bool(deliv),
        "rubric_block_present": bool(rub),
        "credited_block_present": bool(cred),
        "gate_block_present": bool(gate),
        "artifact_requested": artifact_requested,
        "delivered": delivered,
        "n_absent_deductions": n_absent,
        "credited_total": credited_total,
        "credited_max": credited_max,
        "rubric_lines": rubric_lines,
        "gate_answers": gate_answers,
    }


# --------------------------------------------------------------------------- #
# One judge call (with backoff)
# --------------------------------------------------------------------------- #
def call_judge(judge_slug: str, prompt: str, max_retries: int = 5) -> dict:
    """Single OpenRouter chat/completions call. Returns dict with completion text
    + token usage, or {'error': ...}. Exponential backoff on 429/5xx/transport."""
    body = json.dumps({
        "model": judge_slug,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": GRADER_TEMPERATURE,
    }).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/cjimmylin/cei-literature",
        "X-Title": "WCF-v2-s14-calibration",
    }
    delay = 2.0
    last_err = None
    for attempt in range(max_retries):
        if _stop.is_set():
            return {"error": "cost_cap_stop"}
        try:
            req = urllib.request.Request(OPENROUTER_URL, data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            choices = data.get("choices") or []
            if not choices:
                last_err = f"no_choices: {str(data)[:200]}"
                time.sleep(delay); delay *= 2; continue
            text = choices[0].get("message", {}).get("content", "") or ""
            usage = data.get("usage", {}) or {}
            return {
                "completion": text,
                "prompt_tokens": usage.get("prompt_tokens", 0),
                "completion_tokens": usage.get("completion_tokens", 0),
            }
        except urllib.error.HTTPError as e:
            code = e.code
            last_err = f"http_{code}"
            if code in (429, 500, 502, 503, 504):
                time.sleep(delay); delay *= 2; continue
            try:
                last_err = f"http_{code}: {e.read().decode('utf-8')[:200]}"
            except Exception:
                pass
            if code in (400, 401, 403):
                return {"error": last_err}
            time.sleep(delay); delay *= 2
        except Exception as e:  # transport / timeout
            last_err = f"{type(e).__name__}: {e}"
            time.sleep(delay); delay *= 2
    return {"error": last_err or "max_retries"}


# --------------------------------------------------------------------------- #
# Load logged SUT responses + item fields
# --------------------------------------------------------------------------- #
def load_log_items(eval_path: Path) -> dict:
    """id -> {question, completion, criterion, metadata} from an s13 .eval log."""
    log = read_eval_log(str(eval_path))
    out = {}
    for s in log.samples:
        question = s.input if isinstance(s.input, str) else str(s.input)
        criterion = s.target if isinstance(s.target, str) else (
            "\n".join(s.target) if isinstance(s.target, list) else str(s.target))
        out[str(s.id)] = {
            "question": question,
            "completion": s.output.completion,
            "criterion": criterion,
            "metadata": dict(s.metadata or {}),
        }
    return out


def median(vals):
    vals = sorted(v for v in vals if v is not None)
    if not vals:
        return None
    n = len(vals)
    if n % 2:
        return float(vals[n // 2])
    return (vals[n // 2 - 1] + vals[n // 2]) / 2.0


def minval(vals):
    vals = [v for v in vals if v is not None]
    return float(min(vals)) if vals else None


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    sample_spec = json.loads(SAMPLE_JSON.read_text())
    items = sample_spec["items"]
    s13 = json.loads(S13_RESULTS.read_text())
    per_item_s13 = s13["per_item"]

    qwen_items = load_log_items(QWEN_LOG)
    haiku_items = load_log_items(HAIKU_LOG)
    sut_logs = {"qwen": qwen_items, "haiku": haiku_items}

    # Build the work list: (item_id, role, mold, sut, judge_name, judge_slug)
    work = []
    render_cache = {}  # (item_id, sut) -> (prompt, defanged_answer)
    for it in items:
        iid = it["id"]
        for sut, logmap in sut_logs.items():
            rec = logmap.get(iid)
            if rec is None:
                print(f"WARN: {iid} missing from {sut} log", file=sys.stderr)
                continue
            prompt, answer_seen = render_strict_prompt(
                rec["question"], rec["completion"], rec["criterion"], rec["metadata"])
            render_cache[(iid, sut)] = (prompt, answer_seen)
            for jname, jslug in JUDGES.items():
                work.append((iid, it["role"], it["mold"], sut, jname, jslug))

    print(f"Dispatching {len(work)} judge calls "
          f"({len(items)} items x {len(sut_logs)} SUTs x {len(JUDGES)} judges)...")

    # results[(iid,sut,jname)] = judge result record
    results = {}

    def do_call(job):
        iid, role, mold, sut, jname, jslug = job
        if _stop.is_set():
            return job, {"error": "cost_cap_stop"}
        prompt, answer_seen = render_cache[(iid, sut)]
        res = call_judge(jslug, prompt)
        if "error" not in res:
            add_cost(jname, res["prompt_tokens"], res["completion_tokens"])
        return job, res

    with cf.ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as ex:
        futs = [ex.submit(do_call, job) for job in work]
        for fut in cf.as_completed(futs):
            job, res = fut.result()
            iid, role, mold, sut, jname, jslug = job
            results[(iid, sut, jname)] = (job, res)

    # Retry pass: any empty/unparseable/errored judge output gets one more try.
    def is_bad(res):
        if "error" in res:
            return True
        text = res.get("completion", "")
        return (not text.strip()) or (parse_grade(text) is None)

    retry_jobs = [job for (job, res) in results.values() if is_bad(res)]
    if retry_jobs and not _stop.is_set():
        print(f"Retry pass on {len(retry_jobs)} bad/unparseable outputs...")
        with cf.ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as ex:
            futs = [ex.submit(do_call, job) for job in retry_jobs]
            for fut in cf.as_completed(futs):
                job, res = fut.result()
                iid, role, mold, sut, jname, jslug = job
                # keep the better of the two (a parseable score wins)
                prev = results[(iid, sut, jname)][1]
                if is_bad(prev) and not is_bad(res):
                    results[(iid, sut, jname)] = (job, res)
                elif is_bad(prev):
                    results[(iid, sut, jname)] = (job, res)  # still bad, record newest

    # --------------------------------------------------------------------- #
    # Assemble per item x SUT records
    # --------------------------------------------------------------------- #
    out_records = []
    unscored = []
    fab_flags = []  # (iid, sut, judge)
    lib006_fab = {}  # judge -> flagged

    for it in items:
        iid = it["id"]
        for sut in sut_logs:
            if (iid, sut) not in render_cache:
                continue
            _, answer_seen = render_cache[(iid, sut)]
            judges_out = {}
            scores = {}
            for jname in JUDGES:
                key = (iid, sut, jname)
                if key not in results:
                    continue
                _, res = results[key]
                if "error" in res:
                    judges_out[jname] = {"error": res["error"], "score": None}
                    unscored.append((iid, sut, jname, res["error"]))
                    continue
                text = res["completion"]
                grade = parse_grade(text)
                blocks = parse_blocks(text)
                qc = check_judge_grading(text, answer_seen)
                if grade is None:
                    unscored.append((iid, sut, jname, "grade_parse_failure"))
                else:
                    scores[jname] = float(grade)
                if qc.flagged:
                    fab_flags.append((iid, sut, jname))
                    if iid == "LIB-N-006" and sut == "qwen":
                        lib006_fab[jname] = True
                judges_out[jname] = {
                    "score": grade,
                    "artifact_requested": blocks["artifact_requested"],
                    "delivered": blocks["delivered"],
                    "n_absent_deductions": blocks["n_absent_deductions"],
                    "credited_total": blocks["credited_total"],
                    "credited_max": blocks["credited_max"],
                    "rubric_lines": blocks["rubric_lines"],
                    "gate_answers": blocks["gate_answers"],
                    "deliverable_block_present": blocks["deliverable_block_present"],
                    "rubric_block_present": blocks["rubric_block_present"],
                    "credited_block_present": blocks["credited_block_present"],
                    "gate_block_present": blocks["gate_block_present"],
                    "quote_check": qc.as_dict(),
                }
                if iid == "LIB-N-006" and sut == "qwen":
                    lib006_fab.setdefault(jname, qc.flagged)

            svals = list(scores.values())
            strict_med = median(svals)
            strict_min = minval(svals)
            s13_score = per_item_s13.get(iid, {}).get(sut)
            out_records.append({
                "id": iid,
                "role": it["role"],
                "mold": it["mold"],
                "sut": sut,
                "judges": judges_out,
                "strict_scores": scores,
                "strict_median": strict_med,
                "strict_min": strict_min,
                "s13_score": s13_score,
                "s13_gpt4omini": per_item_s13.get(iid, {}).get("gpt4omini"),
            })

    # --------------------------------------------------------------------- #
    # Write JSON
    # --------------------------------------------------------------------- #
    with _lock:
        cost_snapshot = dict(_cost)
    payload = {
        "generated": "2026-07-24",
        "session": "s14 Phase-2 strict-judge calibration (offline, logged s13 SUT responses)",
        "judges": list(JUDGES.keys()),
        "grader_temperature": GRADER_TEMPERATURE,
        "n_items": len(items),
        "n_suts": len(sut_logs),
        "n_judge_calls_planned": len(work),
        "cost_estimate": cost_snapshot,
        "cost_cap_usd": COST_CAP_USD,
        "cost_cap_hit": _stop.is_set(),
        "unscored_after_retry": [
            {"id": i, "sut": s, "judge": j, "reason": r} for (i, s, j, r) in unscored],
        "records": out_records,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    # --------------------------------------------------------------------- #
    # Write summary MD
    # --------------------------------------------------------------------- #
    # ------------------------------------------------------------------ #
    # Iteration-0 snapshot (READ-ONLY) for delta columns/notes.
    # ------------------------------------------------------------------ #
    i0_by_key = {}       # (id, sut) -> iter-0 record
    i0_fab_total = None
    i0_fab_by_judge = {}
    i0_unscored = None
    i0_spend = None
    i0_untied_med = None
    i0_untied_min = None
    try:
        i0 = json.loads(ITER0_RESULTS.read_text())
        for r in i0.get("records", []):
            i0_by_key[(r["id"], r["sut"])] = r
        i0_flags = []
        for r in i0.get("records", []):
            for jn, jd in r.get("judges", {}).items():
                if jd.get("quote_check", {}).get("flagged"):
                    i0_flags.append((r["id"], r["sut"], jn))
        i0_fab_total = len(i0_flags)
        for jn in JUDGES:
            i0_fab_by_judge[jn] = sum(1 for (_, _, j) in i0_flags if j == jn)
        i0_unscored = len(i0.get("unscored_after_retry", []))
        i0_spend = i0.get("cost_estimate", {}).get("usd")
        # recompute iter-0 tied untied counts
        tied0 = [it["id"] for it in items if it["role"] == "tied100_sample"]
        um = un = 0
        for iid in tied0:
            rq = i0_by_key.get((iid, "qwen")); rh = i0_by_key.get((iid, "haiku"))
            if rq and rh:
                if rq.get("strict_median") is not None and rh.get("strict_median") is not None \
                        and abs(rq["strict_median"] - rh["strict_median"]) > 0:
                    um += 1
                if rq.get("strict_min") is not None and rh.get("strict_min") is not None \
                        and abs(rq["strict_min"] - rh["strict_min"]) > 0:
                    un += 1
        i0_untied_med, i0_untied_min = um, un
    except Exception as e:  # iter-0 missing → deltas rendered as n/a
        print(f"WARN: could not load iteration-0 results for delta: {e}", file=sys.stderr)

    def rec(iid, sut):
        for r in out_records:
            if r["id"] == iid and r["sut"] == sut:
                return r
        return None

    def i0med(iid, sut):
        r = i0_by_key.get((iid, sut))
        return r.get("strict_median") if r else None

    def i0min(iid, sut):
        r = i0_by_key.get((iid, sut))
        return r.get("strict_min") if r else None

    def dfmt(new, old):
        if new is None or old is None:
            return "n/a"
        d = new - old
        return f"{d:+.0f}" if float(d).is_integer() else f"{d:+.1f}"

    def fmt(v):
        return "—" if v is None else (f"{v:.0f}" if float(v).is_integer() else f"{v:.1f}")

    def judge_scores_str(r):
        return " / ".join(
            fmt(r["judges"].get(j, {}).get("score")) for j in JUDGES)

    lines = []
    lines.append(f"# Session-14 Phase-2 STRICT-judge calibration — {ITER_LABEL} summary\n")
    lines.append("Revised strict template ("
                 + ("DELIVERABLE CHECK first + hardened CREDITED arithmetic + "
                    "(absent) sentinel + GATE-misfire guard" if ITER_LABEL == "i3"
                    else "mechanical verbatim verification + grade-from-credited-lines "
                         "+ worked mini-example")
                 + ") over the logged s13 SUT responses. "
                 "Delta columns/notes are vs iteration 0 "
                 "(`20260724-session14-calibration-results.json`).\n")
    lines.append(f"Generated 2026-07-24. Judges: {', '.join(JUDGES)}. "
                 f"temp={GRADER_TEMPERATURE}. Offline (logged s13 SUT responses; no SUT calls).\n")
    lines.append(f"Cost estimate: ${cost_snapshot['usd']:.4f} over {cost_snapshot['calls']} calls "
                 f"({cost_snapshot['tokens']:,} tokens). Cap ${COST_CAP_USD}. "
                 f"Cap hit: {_stop.is_set()}.\n")

    # (a) Control table
    lines.append("\n## (a) Control items (qwen SUT)\n")
    lines.append("| id | role | judge scores (gem/deep/mist) | strict median | strict min | s13 score | expected real | Δmed vs i0 | Δmin vs i0 |")
    lines.append("|----|------|------------------------------|---------------|-----------|-----------|---------------|-----------|-----------|")
    ctrl_expected = {
        "LIB-N-006": "~83", "PROOF-N-009": "~83-91",
        "MEND-N-002": "genuine-100", "MEND-N-009": "genuine-100",
        "PROOF-N-005": "genuine-100", "WHOLE-N-004": "genuine-100",
    }
    for iid in ["LIB-N-006", "PROOF-N-009", "MEND-N-002", "MEND-N-009", "PROOF-N-005", "WHOLE-N-004"]:
        r = rec(iid, "qwen")
        if not r:
            continue
        lines.append(f"| {iid} | {r['role']} | {judge_scores_str(r)} | "
                     f"{fmt(r['strict_median'])} | {fmt(r['strict_min'])} | "
                     f"{fmt(r['s13_score'])} | {ctrl_expected.get(iid,'')} | "
                     f"{dfmt(r['strict_median'], i0med(iid,'qwen'))} | "
                     f"{dfmt(r['strict_min'], i0min(iid,'qwen'))} |")

    # (b) tied100 table — both SUTs
    lines.append("\n## (b) tied100_sample items\n")
    lines.append("| id | qwen med | qwen min | haiku med | haiku min | "
                 "s13 qwen | s13 haiku | strict|q-h| med | strict|q-h| min | "
                 "Δ|q-h|med vs i0 | Δ|q-h|min vs i0 |")
    lines.append("|----|----------|----------|-----------|-----------|"
                 "----------|-----------|-----------------|-----------------|"
                 "-----------------|-----------------|")
    tied_ids = [it["id"] for it in items if it["role"] == "tied100_sample"]
    n_untied_med = 0
    n_untied_min = 0
    for iid in tied_ids:
        rq = rec(iid, "qwen")
        rh = rec(iid, "haiku")
        qmed = rq["strict_median"] if rq else None
        qmin = rq["strict_min"] if rq else None
        hmed = rh["strict_median"] if rh else None
        hmin = rh["strict_min"] if rh else None
        gap_med = abs(qmed - hmed) if (qmed is not None and hmed is not None) else None
        gap_min = abs(qmin - hmin) if (qmin is not None and hmin is not None) else None
        if gap_med is not None and gap_med > 0:
            n_untied_med += 1
        if gap_min is not None and gap_min > 0:
            n_untied_min += 1
        # iter-0 gaps for delta
        i0qmed, i0hmed = i0med(iid, "qwen"), i0med(iid, "haiku")
        i0qmin, i0hmin = i0min(iid, "qwen"), i0min(iid, "haiku")
        i0gap_med = abs(i0qmed - i0hmed) if (i0qmed is not None and i0hmed is not None) else None
        i0gap_min = abs(i0qmin - i0hmin) if (i0qmin is not None and i0hmin is not None) else None
        lines.append(
            f"| {iid} | {fmt(qmed)} | {fmt(qmin)} | {fmt(hmed)} | {fmt(hmin)} | "
            f"{fmt(rq['s13_score'] if rq else None)} | {fmt(rh['s13_score'] if rh else None)} | "
            f"{fmt(gap_med)} | {fmt(gap_min)} | "
            f"{dfmt(gap_med, i0gap_med)} | {dfmt(gap_min, i0gap_min)} |")
    d_um = dfmt(n_untied_med, i0_untied_med)
    d_un = dfmt(n_untied_min, i0_untied_min)
    lines.append(f"\n**Tied-100 items no longer tied (nonzero strict |qwen-haiku|):** "
                 f"under MEDIAN = {n_untied_med}/{len(tied_ids)} (i0 {i0_untied_med}; Δ {d_um}); "
                 f"under MIN = {n_untied_min}/{len(tied_ids)} (i0 {i0_untied_min}; Δ {d_un}).\n")

    # (c) fabrication flags
    lines.append("\n## (c) Fabrication flags\n")
    d_fab = dfmt(len(fab_flags), i0_fab_total)
    lines.append(f"Total flagged (item x SUT x judge with >=1 fabricated claimed quote): "
                 f"**{len(fab_flags)}** (i0 {i0_fab_total}; Δ {d_fab}). "
                 f"Rate this run: {len(fab_flags)}/{3*len(out_records)} judge-verdicts.\n")
    # Per-judge fabrication rate with delta vs iteration 0.
    lines.append("Per-judge fabrication flags (this run / i0 / Δ):")
    for j in JUDGES:
        cur = sum(1 for (_, _, jj) in fab_flags if jj == j)
        old = i0_fab_by_judge.get(j)
        lines.append(f"- {j}: {cur} / {old} / {dfmt(cur, old)}")
    lines.append("")
    lines.append("LIB-N-006 (qwen) per-judge fabrication flag:")
    for j in JUDGES:
        r = rec("LIB-N-006", "qwen")
        flagged = r["judges"].get(j, {}).get("quote_check", {}).get("flagged") if r else None
        lines.append(f"- {j}: flagged = {flagged}")
    # LIB-N-006 deepseek/mistral status explicitly (report requirement (c)).
    r006 = rec("LIB-N-006", "qwen")
    for j in ("deepseek-chat", "mistral-small-2603"):
        jd = r006["judges"].get(j, {}) if r006 else {}
        lines.append(f"- LIB-N-006/qwen/{j}: score={fmt(jd.get('score'))}, "
                     f"flagged={jd.get('quote_check',{}).get('flagged')}")
    if fab_flags:
        lines.append("\nAll flags (id / sut / judge):")
        for (i, s, j) in fab_flags:
            lines.append(f"- {i} / {s} / {j}")

    # (d) unscored
    lines.append("\n## (d) Unscored / parse failures after retry\n")
    lines.append(f"Count: **{len(unscored)}** (i0 {i0_unscored}; Δ {dfmt(len(unscored), i0_unscored)}).")
    for (i, s, j, r) in unscored:
        lines.append(f"- {i} / {s} / {j}: {r}")

    # (e) spend
    lines.append("\n## (e) Spend estimate\n")
    d_spend = (f"{cost_snapshot['usd'] - i0_spend:+.4f}" if i0_spend is not None else "n/a")
    lines.append(f"This run ({ITER_LABEL}): ${cost_snapshot['usd']:.4f} ({cost_snapshot['tokens']:,} tokens, "
                 f"{cost_snapshot['calls']} calls). Per-run cap ${COST_CAP_USD}. Cap hit: {_stop.is_set()}.")
    cum = (cost_snapshot['usd'] + i0_spend) if i0_spend is not None else None
    lines.append(f"\nIteration-0 spend: ${i0_spend:.4f}. Δ this run vs i0: ${d_spend}. "
                 f"Cumulative calibration spend: "
                 f"{('$%.4f' % cum) if cum is not None else 'n/a'} (budget < $1.00).")

    # (g) DELIVERABLE CHECK — per-judge delivered-verdict on the audited refusal /
    # non-delivery items (i3). These are the items the dissent audit flagged as
    # over-scored refusals; the DELIVERABLE CHECK should now fire "no" and drive
    # their score to the manner-line ceiling.
    lines.append("\n## (g) DELIVERABLE CHECK verdicts (audited refusal / non-delivery items)\n")
    lines.append("Per-judge `delivered` flag + score + #(absent) deductions. Audit expects "
                 "DELIVERED=no → score at the manner-line ceiling (~5-15).")
    lines.append("\n| id | sut | judge | delivered | #absent | score |")
    lines.append("|----|-----|-------|-----------|---------|-------|")
    deliv_watch = [
        ("LIB-N-011", "qwen"), ("LIB-N-011", "haiku"),
        ("WHOLE-N-007", "haiku"), ("MEND-N-001", "haiku"),
        ("WHOLE-N-002", "qwen"),
    ]
    for iid, sut in deliv_watch:
        r = rec(iid, sut)
        if not r:
            continue
        for j in JUDGES:
            jd = r["judges"].get(j, {})
            lines.append(f"| {iid} | {sut} | {j} | {jd.get('delivered')} | "
                         f"{jd.get('n_absent_deductions')} | {fmt(jd.get('score'))} |")

    lines.append("\n## (f) Files written\n")
    lines.append(f"- `{OUT_JSON.relative_to(WCF_ROOT)}`")
    lines.append(f"- `{OUT_MD.relative_to(WCF_ROOT)}`")

    OUT_MD.write_text("\n".join(lines) + "\n")

    # --------------------------------------------------------------------- #
    # stdout report
    # --------------------------------------------------------------------- #
    print("\n=== DONE ===")
    print(f"Cost: ${cost_snapshot['usd']:.4f} / {cost_snapshot['calls']} calls / "
          f"{cost_snapshot['tokens']:,} tokens. Cap hit: {_stop.is_set()}")
    print(f"Unscored after retry: {len(unscored)}")
    print(f"Fabrication flags total: {len(fab_flags)}")
    print(f"tied100 untied (median): {n_untied_med}/{len(tied_ids)}  "
          f"(min): {n_untied_min}/{len(tied_ids)}")
    print(f"Wrote: {OUT_JSON.name}, {OUT_MD.name}")


if __name__ == "__main__":
    main()
