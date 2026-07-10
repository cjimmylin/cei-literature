#!/usr/bin/env python
"""Judge acceptance-probe STABILITY SWEEP (live, via OpenRouter) — session 12.

Runs the five R33.4 judge-acceptance probes K=8 times each, at temperature 0, for
each of four fast-mid judge slugs, and records per-run pass/fail + the diagnostic
detail (discrimination award patterns, negative-disclosure score, truncations/parse
defects). This is a STABILITY diagnostic — it quantifies the non-determinism the
session-11 memo flagged (gemini discrimination flips; mistral-small qualification
instability) so a Fable session can rule on which judges are admissible per surface.

The five probes (all from the existing harness, invoked with their real signatures):
  - G4 battery                    -> wcfbench.judge.run_judge_calibration
  - award-consistency probe       -> wcfbench.judge.run_award_consistency_probe
  - discrimination probe          -> wcfbench.judge.run_discrimination_probe
  - disclosure-inversion probe    -> wcfbench.contested.run_disclosure_inversion_probe
  - negative-disclosure probe     -> wcfbench.contested.run_negative_disclosure_probe

SAFETY: default run prints the PLAN and makes NO calls. Pass --go to spend tokens.
Requires $OPENROUTER_API_KEY (`source ~/.codex/secrets/openrouter.env`).

    python probe_stability.py           # dry: plan + slug check, 0 calls
    python probe_stability.py --go      # real calls (well under $1)

This script is APPEND-ONLY: it writes a NEW dir 07-PILOTS/20260710-probe-stability/
and modifies no existing harness module, test, bank, or pilot dir.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request

HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import OpenRouterModelClient, OpenRouterError  # noqa: E402
from wcfbench.judge import (  # noqa: E402
    run_judge_calibration,
    run_award_consistency_probe,
    run_discrimination_probe,
)
from wcfbench.contested import (  # noqa: E402
    run_disclosure_inversion_probe,
    run_negative_disclosure_probe,
)
from wcfbench.probe_fixtures import DISCRIMINATION_DISCRIMINATING_KPS  # noqa: E402

MODELS_URL = "https://openrouter.ai/api/v1/models"
OUT_DIR = os.path.normpath(
    os.path.join(HARNESS_ROOT, "..", "07-PILOTS", "20260710-probe-stability")
)
K = 8
JUDGE_MAX_TOKENS = 2048
RETRIES = 2  # on network/5xx errors, retry up to 2x then record an error rep

# Three fixed judges + one fresh mid-tier candidate (validated live in main()).
FIXED_JUDGES = [
    ("gpt4omini", "openai", "openai/gpt-4o-mini"),
    ("gemini-flash", "google", "google/gemini-2.5-flash"),
    ("mistral-small", "mistral", "mistralai/mistral-small-3.2-24b-instruct"),
]
# 4th candidate: try mistral-medium-3.1 first; fall back to nearest available
# mistral-medium / cohere command-r class slug (family NOT openai/google/anthropic/
# meta/deepseek). Ordered preference list; first live slug wins.
FOURTH_CANDIDATES = [
    ("mistral-medium", "mistral", "mistralai/mistral-medium-3.1"),
    ("mistral-medium", "mistral", "mistralai/mistral-medium-3"),
    ("mistral-medium", "mistral", "mistralai/mistral-medium"),
    ("command-r-plus", "cohere", "cohere/command-r-plus"),
    ("command-r", "cohere", "cohere/command-r"),
    ("command-a", "cohere", "cohere/command-a"),
]

PROBES = ["g4", "award_consistency", "discrimination",
          "disclosure_inversion", "negative_disclosure"]


class CapturingClient:
    """Wraps an OpenRouterModelClient, recording every .complete(prompt, item_id)
    call — the raw text and the underlying client's finish_reason — so a probe's
    internal calls can be inspected after it returns. Retries transient errors."""

    def __init__(self, inner):
        self.inner = inner
        self.calls = []  # list of {item_id, text, finish_reason, truncated, error}

    def reset(self):
        self.calls = []

    def complete(self, prompt, item_id=None):
        last_err = None
        for attempt in range(RETRIES + 1):
            try:
                text = self.inner.complete(prompt, item_id=item_id)
                self.calls.append({
                    "item_id": item_id,
                    "text": text,
                    "finish_reason": self.inner.last_finish_reason,
                    "truncated": self.inner.last_truncated,
                    "error": None,
                })
                return text
            except OpenRouterError as e:
                last_err = e
                if attempt < RETRIES:
                    time.sleep(2.0 * (attempt + 1))
                    continue
        # exhausted retries — record and re-raise so the probe rep is an error rep
        self.calls.append({
            "item_id": item_id, "text": None, "finish_reason": None,
            "truncated": False, "error": str(last_err),
        })
        raise last_err


def fetch_model_ids(api_key):
    req = urllib.request.Request(
        MODELS_URL,
        headers={"Authorization": f"Bearer {api_key}"} if api_key else {},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return {m["id"] for m in data.get("data", []) if isinstance(m, dict) and "id" in m}


def pick_fourth(catalog):
    for name, family, slug in FOURTH_CANDIDATES:
        if slug in catalog:
            return (name, family, slug)
    return None


def _award_pattern(calls, item_substr):
    """Extract the parsed award pattern on the discriminating KPs from a captured
    discrimination-probe call whose item_id contains item_substr (STRONG/WEAK)."""
    from wcfbench.judge import parse_award_verdict
    for c in calls:
        if c["item_id"] and item_substr in c["item_id"] and c["text"]:
            v = parse_award_verdict(c["text"])
            return {kp: v.awards.get(kp) for kp in DISCRIMINATION_DISCRIMINATING_KPS}
    return None


def run_probe(name, cap):
    """Run one probe once against the capturing client; return a result dict.
    Records raw verdict texts, parsed outcome, pass/fail, finish_reasons."""
    cap.reset()
    rec = {"probe": name, "passed": None, "detail": "", "observed": None,
           "error": None, "raw_texts": [], "finish_reasons": [], "truncated_any": False}
    try:
        if name == "g4":
            r = run_judge_calibration(cap)
            rec["passed"] = not r.flagged
            rec["detail"] = f"flagged={r.flagged}; failing_cases=" + str(
                [cid for cid, v in r.by_case.items() if not v["passed"]])
            rec["observed"] = {cid: {"higher": v.get("higher"), "lower": v.get("lower"),
                                     "passed": v["passed"]} for cid, v in r.by_case.items()}
        elif name == "award_consistency":
            r = run_award_consistency_probe(cap)
            rec["passed"] = r.passed
            rec["detail"] = r.detail
            rec["observed"] = r.observed
        elif name == "discrimination":
            r = run_discrimination_probe(cap)
            rec["passed"] = r.passed
            rec["detail"] = r.detail
            rec["observed"] = r.observed
            rec["strong_pattern"] = _award_pattern(cap.calls, "STRONG")
            rec["weak_pattern"] = _award_pattern(cap.calls, "WEAK")
        elif name == "disclosure_inversion":
            r = run_disclosure_inversion_probe(cap)
            rec["passed"] = r.passed
            rec["detail"] = r.detail
            rec["observed"] = r.observed
        elif name == "negative_disclosure":
            r = run_negative_disclosure_probe(cap)
            rec["passed"] = r.passed
            rec["detail"] = r.detail
            rec["observed"] = r.observed
            rec["disclosure_score"] = r.observed
        else:
            raise ValueError(f"unknown probe {name}")
    except Exception as e:  # probe raised (incl. exhausted-retry network error)
        rec["error"] = f"{type(e).__name__}: {e}"
        rec["passed"] = False
    # attach the captured raw payload
    rec["raw_texts"] = [{"item_id": c["item_id"], "text": c["text"],
                         "finish_reason": c["finish_reason"], "truncated": c["truncated"],
                         "error": c["error"]} for c in cap.calls]
    rec["finish_reasons"] = [c["finish_reason"] for c in cap.calls]
    rec["truncated_any"] = any(c["truncated"] for c in cap.calls)
    return rec


def _print_plan(judges, api_key):
    print("=" * 74)
    print("Probe-stability sweep — PLAN (dry run; pass --go for real calls)")
    print("=" * 74)
    print(f"K reps per (judge, probe): {K}")
    print(f"probes: {PROBES}")
    print("judges:")
    for n, f, s in judges:
        print(f"  - {n:16s} {f:8s} {s}")
    if judges and judges[-1][2] == "PENDING":
        print("  (4th slug resolved live against the catalog under --go)")
    total = len(judges) * len(PROBES) * K
    print(f"total probe executions: ~{total} (each = 1-6 small judge calls)")
    if api_key:
        try:
            catalog = fetch_model_ids(api_key)
            fixed_slugs = [s for _, _, s in FIXED_JUDGES]
            invalid = [s for s in fixed_slugs if s not in catalog]
            print(f"  fixed slugs invalid: {invalid or 'none — all live'}")
            fourth = pick_fourth(catalog)
            print(f"  4th candidate resolved: {fourth}")
            avail = [s for _, _, s in FOURTH_CANDIDATES if s in catalog]
            print(f"  (mistral-medium/cohere candidates live in catalog: {avail})")
        except Exception as e:
            print(f"  ! catalog fetch failed: {e}")
    else:
        print("  (set $OPENROUTER_API_KEY to validate slugs)")
    print(f"output -> {OUT_DIR}/")


def main():
    global K
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true", help="make the real API calls (spends tokens)")
    ap.add_argument("-k", type=int, default=K, help="reps per (judge, probe)")
    args = ap.parse_args()

    K = args.k
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not args.go:
        judges = FIXED_JUDGES + [("mistral-medium", "mistral", "PENDING")]
        _print_plan(judges, api_key)
        return 0

    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY not set. `source ~/.codex/secrets/openrouter.env` first.",
              file=sys.stderr)
        return 2

    try:
        catalog = fetch_model_ids(api_key)
    except Exception as e:
        print(f"ERROR: could not fetch model catalog: {e}", file=sys.stderr)
        return 2

    fixed_invalid = [s for _, _, s in FIXED_JUDGES if s not in catalog]
    if fixed_invalid:
        print(f"ERROR: fixed judge slug(s) not in catalog: {fixed_invalid}", file=sys.stderr)
        return 2

    fourth = pick_fourth(catalog)
    if fourth is None:
        print("ERROR: no 4th mid-tier candidate slug found live in catalog. "
              f"Tried: {[s for _, _, s in FOURTH_CANDIDATES]}", file=sys.stderr)
        return 2
    judges = FIXED_JUDGES + [fourth]
    print(f"4th judge slug (live-validated): {fourth[2]} (family={fourth[1]})")
    print(f"all four judges: {[s for _, _, s in judges]}")

    os.makedirs(OUT_DIR, exist_ok=True)
    raw_path = os.path.join(OUT_DIR, "raw_verdicts.jsonl")
    ts = datetime.datetime.now().isoformat(timespec="seconds")

    pass_counts = {}   # (judge_name, probe) -> n_pass
    fourth_meta = {"slug": fourth[2], "family": fourth[1], "name": fourth[0]}

    with open(raw_path, "w") as rawfh:
        for jname, jfamily, jslug in judges:
            print(f"\n=== judge {jname} ({jslug}) ===")
            inner = OpenRouterModelClient(model=jslug, temperature=0.0,
                                          max_tokens=JUDGE_MAX_TOKENS)
            cap = CapturingClient(inner)
            for probe in PROBES:
                n_pass = 0
                for rep in range(K):
                    rec = run_probe(probe, cap)
                    if rec["passed"]:
                        n_pass += 1
                    out = {
                        "canary": "WCFBENCH-CANARY-c1647-x9k4q",
                        "timestamp": ts,
                        "judge": jname, "judge_family": jfamily, "judge_slug": jslug,
                        "probe": probe, "rep": rep,
                        "passed": rec["passed"], "detail": rec["detail"],
                        "observed": rec["observed"], "error": rec["error"],
                        "finish_reasons": rec["finish_reasons"],
                        "truncated_any": rec["truncated_any"],
                        "raw_texts": rec["raw_texts"],
                    }
                    if probe == "discrimination":
                        out["strong_pattern"] = rec.get("strong_pattern")
                        out["weak_pattern"] = rec.get("weak_pattern")
                    if probe == "negative_disclosure":
                        out["disclosure_score"] = rec.get("disclosure_score")
                    rawfh.write(json.dumps(out) + "\n")
                    rawfh.flush()
                    flag = "PASS" if rec["passed"] else "FAIL"
                    extra = ""
                    if probe == "discrimination":
                        extra = f" strong={rec.get('strong_pattern')} weak={rec.get('weak_pattern')}"
                    if probe == "negative_disclosure":
                        extra = f" disclosure={rec.get('disclosure_score')}"
                    if rec["error"]:
                        extra += f" ERR={rec['error'][:60]}"
                    print(f"  {probe:22s} rep{rep} {flag}{extra}")
                pass_counts[(jname, probe)] = n_pass
                print(f"  --> {probe}: {n_pass}/{K} pass")

    # pass_rates.json
    pass_rates = {}
    for (jname, probe), n in pass_counts.items():
        pass_rates.setdefault(jname, {})[probe] = {"n_pass": n, "k": K}
    pr_path = os.path.join(OUT_DIR, "pass_rates.json")
    with open(pr_path, "w") as fh:
        json.dump({"canary": "WCFBENCH-CANARY-c1647-x9k4q", "timestamp": ts,
                   "k": K, "fourth_judge": fourth_meta,
                   "judges": [{"name": n, "family": f, "slug": s} for n, f, s in judges],
                   "pass_rates": pass_rates}, fh, indent=2)
    print(f"\nwrote {pr_path}")
    print(f"wrote {raw_path}")

    _write_report(judges, pass_counts, raw_path, fourth_meta, ts)
    return 0


def _write_report(judges, pass_counts, raw_path, fourth_meta, ts):
    """Assemble the markdown report from the raw jsonl (re-read for per-run detail)."""
    records = [json.loads(l) for l in open(raw_path)]
    md = os.path.join(OUT_DIR, "20260710-probe-stability-report.md")
    jnames = [n for n, _, _ in judges]

    lines = []
    lines.append("# WCF-Bench — Judge Acceptance-Probe Stability Sweep")
    lines.append("")
    lines.append(f"Canary: `WCFBENCH-CANARY-c1647-x9k4q`  ·  Run: {ts}  ·  K={K} reps, temperature=0")
    lines.append("")
    lines.append("DESCRIPTIVE / pre-gate diagnostic. Quantifies the non-determinism the "
                 "session-11 memo flagged in the judge-acceptance battery; NOT a gated measurement.")
    lines.append("")
    lines.append("## Judges")
    lines.append("")
    for n, f, s in judges:
        tag = " (4th, live-validated)" if s == fourth_meta["slug"] else ""
        lines.append(f"- **{n}** — `{s}` (family={f}){tag}")
    lines.append("")

    # 1) pass-rate table
    lines.append("## 1. Pass-rate table (n_pass / 8)")
    lines.append("")
    header = "| judge | " + " | ".join(PROBES) + " |"
    sep = "|" + "---|" * (len(PROBES) + 1)
    lines.append(header)
    lines.append(sep)
    for jn in jnames:
        row = [jn]
        for p in PROBES:
            row.append(str(pass_counts.get((jn, p), "—")) + "/" + str(K))
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    # 2) discrimination per-run detail
    lines.append("## 2. Discrimination probe — per-run detail")
    lines.append("")
    lines.append("Reference divergence (indisputable KPs 1/2/3): strong=award/award/award, "
                 "weak=deny/deny/deny. A PASS reproduces the divergence; a "
                 "holistic-failure run emits identical strong/weak patterns.")
    lines.append("")
    for jn in jnames:
        recs = [r for r in records if r["judge"] == jn and r["probe"] == "discrimination"]
        recs.sort(key=lambda r: r["rep"])
        n_identical = n_divergent_pass = n_parse_issue = 0
        examples = []
        for r in recs:
            sp = r.get("strong_pattern")
            wp = r.get("weak_pattern")
            none_present = (sp is None or wp is None
                            or any(v is None for v in (sp or {}).values())
                            or any(v is None for v in (wp or {}).values())
                            or r.get("error"))
            if none_present:
                n_parse_issue += 1
                cat = "parse/None"
            elif sp == wp:
                n_identical += 1
                cat = "IDENTICAL (holistic fail)"
            elif r["passed"]:
                n_divergent_pass += 1
                cat = "divergent PASS"
            else:
                cat = "divergent but off-reference"

            def fmt(pat):
                if pat is None:
                    return "None"
                return "".join("A" if pat.get(k) is True else
                               ("D" if pat.get(k) is False else "?")
                               for k in DISCRIMINATION_DISCRIMINATING_KPS)
            examples.append((r["rep"], fmt(sp), fmt(wp), cat, r["passed"]))
        lines.append(f"### {jn}")
        lines.append("")
        lines.append(f"- identical strong/weak [holistic failure]: **{n_identical}/{K}**")
        lines.append(f"- reference-matching divergence [pass]: **{n_divergent_pass}/{K}**")
        lines.append(f"- parse-None / missing-KP lines: **{n_parse_issue}/{K}**")
        lines.append("")
        lines.append("| rep | strong(KP1-3) | weak(KP1-3) | category | passed |")
        lines.append("|---|---|---|---|---|")
        for rep, sp, wp, cat, passed in examples:
            lines.append(f"| {rep} | {sp} | {wp} | {cat} | {passed} |")
        lines.append("")

    # 3) negative-disclosure per-run detail
    lines.append("## 3. Negative-disclosure probe — per-run detail")
    lines.append("")
    lines.append("Reference disclosure = 0.0 (confident-order response asserts settled). "
                 "A run passes iff disclosure ≤ 0.0.")
    lines.append("")
    for jn in jnames:
        recs = [r for r in records if r["judge"] == jn and r["probe"] == "negative_disclosure"]
        recs.sort(key=lambda r: r["rep"])
        scores = [r.get("disclosure_score") for r in recs]
        lines.append(f"### {jn}")
        lines.append("")
        lines.append(f"- disclosure scores across {K} runs: `{scores}`")
        dist = {}
        for s in scores:
            dist[str(s)] = dist.get(str(s), 0) + 1
        lines.append(f"- distribution: {dist}")
        errs = [r["rep"] for r in recs if r.get("error")]
        if errs:
            lines.append(f"- error reps: {errs}")
        lines.append("")

    # 4) defect counts
    lines.append("## 4. Parse failures / truncations / format defects")
    lines.append("")
    n_trunc = sum(1 for r in records if r.get("truncated_any"))
    n_err = sum(1 for r in records if r.get("error"))
    n_empty = 0
    for r in records:
        for rt in r.get("raw_texts", []):
            if rt.get("text") is not None and rt["text"].strip() == "":
                n_empty += 1
    lines.append(f"- reps with any truncated call (finish_reason=length): **{n_trunc}** / {len(records)}")
    lines.append(f"- reps that errored (network/5xx after {RETRIES} retries): **{n_err}** / {len(records)}")
    lines.append(f"- empty response strings observed: **{n_empty}**")
    # per-judge finish_reason tally
    lines.append("")
    lines.append("Finish-reason tally per judge (across all calls):")
    lines.append("")
    for jn in jnames:
        fr = {}
        for r in records:
            if r["judge"] != jn:
                continue
            for reason in r.get("finish_reasons", []):
                fr[str(reason)] = fr.get(str(reason), 0) + 1
        lines.append(f"- **{jn}**: {fr}")
    lines.append("")

    with open(md, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {md}")


if __name__ == "__main__":
    raise SystemExit(main())
