#!/usr/bin/env python
"""R39(d) settled-core re-qualification + R36.4 frontier OPEN-award screen (live, OpenRouter).

Two live tasks, one script, one new dated run dir:

  1. SETTLED-CORE RE-QUALIFICATION (R39(d)). The floor-gloss changed the settled-core prompt,
     which is now in `current_template_hashes()` (closing the R35.6 gap) — so the third-family
     manifest is STALE and every judge must re-qualify the SETTLED_CORE surface. We run ONLY the
     NEW settled-core probe live (K=8, >=5/8) for the three incumbent judges (gpt-4o-mini,
     gemini-2.5-flash, grok-4.20) and CARRY FORWARD all other surfaces' frozen pass counts from
     the third-family screen manifest. HONEST OUTCOME: a judge that fails the new probe (<5/8)
     LOSES settled-core eligibility in the new manifest. If fewer than 2 of the 3 pass, STOP.

  2. FRONTIER OPEN-AWARD SCREEN (R36.4 escalation). Run the full K=8 5-probe battery on two
     frontier-tier new-family candidates in order — a cohere command-a-class slug, then an amazon
     nova-pro-class slug (resolved live against /api/v1/models). A candidate qualifies for the
     OPEN award iff g4 AND award-consistency AND discrimination all reach >=5/8. If one qualifies,
     it joins the combined manifest (OPEN award gains a 2nd family). If both fail, record + move on.

SAFETY: default run prints the PLAN and makes NO calls. Pass --go to spend tokens.
Requires $OPENROUTER_API_KEY (`source ~/.codex/secrets/openrouter.env`).

    python settled_requal.py            # dry: plan + slug check + key balance, 0 calls
    python settled_requal.py --go       # real calls (budget < $8; settled ~cents, screen the bulk)

APPEND-ONLY: writes a NEW dir 07-PILOTS/20260710-settled-requal/ and modifies no existing
harness module, test, bank, or pilot dir. The old third-family manifest stays FROZEN.
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
from wcfbench.qualification import (  # noqa: E402
    run_probe_reps, qualify_judge, build_manifest, write_manifest, load_manifest,
    manifest_from_pass_table, current_template_hashes,
    JudgeQualification, ProbeReps,
    SURFACE_PROBES, PROBES,
    OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE,
    DEFAULT_K, DEFAULT_THRESHOLD,
)

MODELS_URL = "https://openrouter.ai/api/v1/models"
KEY_URL = "https://openrouter.ai/api/v1/auth/key"
OUT_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "07-PILOTS", "20260710-settled-requal"))
FROZEN_MANIFEST = os.path.normpath(os.path.join(
    HARNESS_ROOT, "..", "07-PILOTS", "20260710-third-family-screen",
    "20260710-third-family-manifest.json"))
K = 8
THRESHOLD = 5
JUDGE_MAX_TOKENS = 2048
RETRIES = 2
MIN_BALANCE = 10.0     # R39(d) pre-flight: proceed only if limit_remaining > $10

# The three incumbent judges whose SETTLED_CORE surface must re-qualify (R39(d)). G4 + all
# other surfaces are carried forward from the frozen manifest; only settled_core is run live.
INCUMBENT_JUDGES = [
    ("gpt4omini", "openai", "openai/gpt-4o-mini"),
    ("gemini-flash", "google", "google/gemini-2.5-flash"),
    ("grok-4.20", "x-ai", "x-ai/grok-4.20"),
]

# R36.4 frontier OPEN-award candidates, IN ORDER (cohere command-a class, then amazon nova-pro
# class). Slugs resolved live against the catalog; first live slug per family wins; skip cleanly
# if none resolves. Family NOT in {openai, google, anthropic}.
FRONTIER_CANDIDATES = [
    ("cohere", ["cohere/command-a", "cohere/command-a-03-2025", "cohere/command-r-plus-08-2024",
                "cohere/command-r-plus"]),
    ("amazon", ["amazon/nova-pro-v1", "amazon/nova-pro", "amazon/nova-premier-v1"]),
]


class CapturingClient:
    """Wraps an OpenRouterModelClient: transport-level retry on 5xx, mirrors finish_reason so the
    R35.1 retry seam fires through the wrapper, records raw calls for the run artifact."""

    def __init__(self, inner):
        self.inner = inner
        self.calls = []
        self.last_finish_reason = None
        self.last_truncated = False

    def reset(self):
        self.calls = []

    def complete(self, prompt, item_id=None):
        last_err = None
        for attempt in range(RETRIES + 1):
            try:
                text = self.inner.complete(prompt, item_id=item_id)
                self.last_finish_reason = self.inner.last_finish_reason
                self.last_truncated = self.inner.last_truncated
                self.calls.append({"item_id": item_id, "text": text,
                                   "finish_reason": self.inner.last_finish_reason,
                                   "truncated": self.inner.last_truncated, "error": None})
                return text
            except OpenRouterError as e:
                last_err = e
                if attempt < RETRIES:
                    time.sleep(2.0 * (attempt + 1))
                    continue
        self.calls.append({"item_id": item_id, "text": None, "finish_reason": None,
                           "truncated": False, "error": str(last_err)})
        raise last_err


def _get_json(url, api_key):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"}, method="GET")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_model_ids(api_key):
    data = _get_json(MODELS_URL, api_key)
    return {m["id"] for m in data.get("data", []) if isinstance(m, dict) and "id" in m}


def key_balance(api_key):
    d = _get_json(KEY_URL, api_key).get("data", {})
    return d.get("limit_remaining"), d.get("limit"), d.get("usage")


def resolve_frontier(catalog):
    """First live slug per frontier family, in order; None if the family has no live slug."""
    out = []
    for family, slugs in FRONTIER_CANDIDATES:
        live = next((s for s in slugs if s in catalog), None)
        out.append((family, live, slugs))
    return out


def _print_plan(api_key):
    print("=" * 78)
    print("R39(d) settled-core re-qualification + R36.4 frontier OPEN-award screen — PLAN (dry)")
    print("=" * 78)
    print(f"K={K}, gate >= {THRESHOLD}/{K}, temperature=0, JUDGE_MAX_TOKENS={JUDGE_MAX_TOKENS}")
    print("\nTASK 1 — settled-core re-qualification (LIVE, settled_core probe ONLY):")
    for n, f, s in INCUMBENT_JUDGES:
        print(f"  - {n:14s} {f:8s} {s}   (carry forward all other surfaces from frozen manifest)")
    print(f"  live calls: 3 judges x {K} reps x 3 fixtures x ~1 call = ~72 fast-mid calls (cents)")
    print("\nTASK 2 — frontier OPEN-award screen (LIVE, full 5+1-probe battery):")
    print(f"  candidates in order: {[f for f, _ in FRONTIER_CANDIDATES]}")
    if api_key:
        try:
            rem, lim, use = key_balance(api_key)
            print(f"\n  key balance: limit_remaining=${rem} (limit=${lim}, usage=${use})")
            print(f"  pre-flight: {'OK — > $%.0f' % MIN_BALANCE if (rem or 0) > MIN_BALANCE else 'STOP — below threshold, Jimmy top-up'}")
            catalog = fetch_model_ids(api_key)
            inc_bad = [s for _, _, s in INCUMBENT_JUDGES if s not in catalog]
            print(f"  incumbent slugs invalid: {inc_bad or 'none — all live'}")
            for family, live, slugs in resolve_frontier(catalog):
                print(f"  frontier {family:8s} -> {live or 'NONE live in catalog (will skip)'}")
        except Exception as e:
            print(f"  ! catalog/key fetch failed: {e}")
    else:
        print("  (set $OPENROUTER_API_KEY to validate slugs + check balance)")
    print(f"\noutput -> {OUT_DIR}/")


def _run_settled_probe_live(judges, raw_fh, ts):
    """Run the settled_core probe K=8 for each incumbent; return name -> ProbeReps + raw records."""
    reps_by_judge = {}
    for jname, jfamily, jslug in judges:
        print(f"\n=== settled-core requal: {jname} ({jslug}) ===")
        inner = OpenRouterModelClient(model=jslug, temperature=0.0, max_tokens=JUDGE_MAX_TOKENS)
        cap = CapturingClient(inner)
        # run each rep, capturing the raw calls so causes are auditable
        reps = []
        n_pass = 0
        for rep in range(K):
            cap.reset()
            from wcfbench.qualification import _run_probe_once
            try:
                passed, cause, detail, observed = _run_probe_once(cap, "settled_core")
            except Exception as e:
                passed, cause, detail, observed = False, "fail_transport_after_retry", f"{type(e).__name__}: {e}", None
            if passed:
                n_pass += 1
            rec = {"canary": "WCFBENCH-CANARY-c1647-x9k4q", "timestamp": ts,
                   "judge": jname, "judge_family": jfamily, "judge_slug": jslug,
                   "probe": "settled_core", "rep": rep, "passed": passed, "cause": cause,
                   "detail": detail, "observed": observed,
                   "raw_texts": [{"item_id": c["item_id"], "text": c["text"],
                                  "finish_reason": c["finish_reason"], "error": c["error"]}
                                 for c in cap.calls]}
            raw_fh.write(json.dumps(rec) + "\n")
            raw_fh.flush()
            print(f"  rep{rep} {'PASS' if passed else 'FAIL':4s} cause={cause}  {detail[:70]}")
            reps.append({"rep": rep, "passed": passed, "cause": cause, "detail": detail})
        pr = ProbeReps(probe="settled_core", k=K, n_pass=n_pass, reps=reps)
        reps_by_judge[jname] = pr
        print(f"  --> settled_core: {n_pass}/{K}  {pr.cause_tally()}")
    return reps_by_judge


def _run_frontier_screen(candidates, raw_fh, ts):
    """Run the full K=8 battery on each frontier candidate in order; return list of result rows."""
    results = []
    for family, slug in candidates:
        name = slug.split("/")[-1]
        print(f"\n=== frontier screen: {name} ({slug}) ===")
        inner = OpenRouterModelClient(model=slug, temperature=0.0, max_tokens=JUDGE_MAX_TOKENS)
        cap = CapturingClient(inner)
        qual = qualify_judge(cap, name=name, family=family, slug=slug, k=K, threshold=THRESHOLD)
        row = {"name": name, "family": family, "slug": slug,
               "probe_pass": {p: {"n_pass": r.n_pass, "k": r.k} for p, r in qual.probe_reps.items()},
               "cause_tally": {p: r.cause_tally() for p, r in qual.probe_reps.items()},
               "eligible_surfaces": sorted(qual.surfaces)}
        # OPEN-award qualification = g4 AND award-consistency AND discrimination all >=5/8
        open_ok = all(qual.probe_reps[p].n_pass >= THRESHOLD
                      for p in ("g4", "award_consistency", "discrimination"))
        row["open_award_qualified"] = open_ok
        results.append(row)
        for p in PROBES:
            print(f"  {p:22s} {qual.probe_reps[p].n_pass}/{K}  {qual.probe_reps[p].cause_tally()}")
        print(f"  OPEN-award qualified: {open_ok}   eligible: {sorted(qual.surfaces) or '[] none'}")
        rec = {"canary": "WCFBENCH-CANARY-c1647-x9k4q", "timestamp": ts, "kind": "frontier_screen",
               "name": name, "family": family, "slug": slug,
               "probe_pass": row["probe_pass"], "cause_tally": row["cause_tally"],
               "eligible_surfaces": row["eligible_surfaces"], "open_award_qualified": open_ok}
        raw_fh.write(json.dumps(rec) + "\n")
        raw_fh.flush()
        if open_ok:
            print(f"  >>> QUALIFIES for OPEN award — a 2nd OPEN-award family ({family}). Stopping frontier screen.")
            break
        print("  --- does not qualify for OPEN award; next frontier candidate.")
    return results


def run(api_key, go):
    if not go:
        _print_plan(api_key)
        return 0

    # R39(d)/R40.1 pre-flight: key balance.
    rem, lim, use = key_balance(api_key)
    print(f"key balance: limit_remaining=${rem} (limit=${lim}, usage=${use})")
    if (rem or 0) <= MIN_BALANCE:
        print(f"STOP: limit_remaining ${rem} <= ${MIN_BALANCE} — Jimmy top-up needed (R40.1).", file=sys.stderr)
        return 2

    catalog = fetch_model_ids(api_key)
    inc_bad = [s for _, _, s in INCUMBENT_JUDGES if s not in catalog]
    if inc_bad:
        print(f"ERROR: incumbent slug(s) not live: {inc_bad}", file=sys.stderr)
        return 2

    os.makedirs(OUT_DIR, exist_ok=True)
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    raw_path = os.path.join(OUT_DIR, "raw_verdicts.jsonl")

    with open(raw_path, "w") as raw_fh:
        # --- TASK 1: settled-core re-qualification ---
        settled_reps = _run_settled_probe_live(INCUMBENT_JUDGES, raw_fh, ts)

        # honest outcome: count how many incumbents pass the new probe
        passers = [n for n, pr in settled_reps.items() if pr.n_pass >= THRESHOLD]
        print(f"\nsettled-core probe passers (>= {THRESHOLD}/{K}): {passers} ({len(passers)}/3)")
        if len(passers) < 2:
            print("STOP: fewer than 2 judge families pass the settled-core probe. Settled-core would "
                  "have < 2 valid families — do not improvise. Reporting and stopping (R39(d)).",
                  file=sys.stderr)
            # still write what we have + a loud report, then stop before the frontier screen.
            _finalize(settled_reps, frontier_results=[], frontier_qualified=None, ts=ts,
                      stopped="settled_core < 2 families")
            return 3

        # --- TASK 2: frontier OPEN-award screen ---
        resolved = resolve_frontier(catalog)
        for family, live, slugs in resolved:
            print(f"frontier {family:8s} -> {live or 'NONE live — skip'}")
        candidates = [(family, slug) for family, slug, _ in resolved if slug]
        frontier_results = _run_frontier_screen(candidates, raw_fh, ts) if candidates else []
        frontier_qualified = next((r for r in frontier_results if r["open_award_qualified"]), None)

    _finalize(settled_reps, frontier_results, frontier_qualified, ts, stopped=None)
    return 0


def _finalize(settled_reps, frontier_results, frontier_qualified, ts, stopped):
    """Build the fresh combined manifest (carry forward + settled requal + optional frontier) +
    write the dated report. The old third-family manifest stays untouched."""
    frozen = load_manifest(FROZEN_MANIFEST)
    frozen_by_slug = {j["slug"]: j for j in frozen["judges"]}
    incumbent_slugs = {s for _, _, s in INCUMBENT_JUDGES}

    rows = []
    # carry forward every judge in the frozen manifest; OVERRIDE settled_core for incumbents
    # with the live re-qual counts. Mistral rows (discarded) carry forward as-is (settled_core=0).
    name_by_slug = {s: n for n, _, s in INCUMBENT_JUDGES}
    for j in frozen["judges"]:
        counts = {p: v["n_pass"] for p, v in j["probe_pass"].items()}
        slug = j["slug"]
        if slug in incumbent_slugs:
            pr = settled_reps[name_by_slug[slug]]
            counts["settled_core"] = pr.n_pass          # live re-qual result (honest)
        else:
            counts.setdefault("settled_core", 0)         # never ran the probe -> no settled-core
        rows.append({"name": j["name"], "family": j["family"], "slug": slug, "pass_counts": counts})

    # optional: the frontier OPEN-award qualifier joins the manifest
    if frontier_qualified:
        fq = frontier_qualified
        rows.append({"name": fq["name"], "family": fq["family"], "slug": fq["slug"],
                     "pass_counts": {p: v["n_pass"] for p, v in fq["probe_pass"].items()}})

    combined = manifest_from_pass_table(
        rows, run_dir="07-PILOTS/20260710-settled-requal", timestamp=ts,
        memo="R39(d) settled-core requal + R36.4 frontier OPEN-award screen (fresh template hashes)",
        k=K, threshold=THRESHOLD)
    # fresh template hashes (now INCLUDING settled_core) come from current_template_hashes() by
    # default in build_manifest; assert it carries the settled_core key loudly.
    assert "settled_core" in combined["template_hashes"], "fresh manifest must hash the settled-core prompt"
    mpath = os.path.join(OUT_DIR, "20260710-settled-requal-manifest.json")
    write_manifest(mpath, combined)
    print(f"\nwrote combined manifest {mpath}")

    _write_report(settled_reps, frontier_results, frontier_qualified, combined, ts, stopped)


def _write_report(settled_reps, frontier_results, frontier_qualified, combined, ts, stopped):
    md = os.path.join(OUT_DIR, "20260710-settled-requal-report.md")
    by_slug = {j["slug"]: j for j in combined["judges"]}
    L = []
    L.append("# WCF-Bench — R39(d) Settled-Core Re-qualification + R36.4 Frontier OPEN-Award Screen")
    L.append("")
    L.append(f"Canary: `WCFBENCH-CANARY-c1647-x9k4q`  ·  Run: {ts}  ·  K={K}, gate >= {THRESHOLD}/{K}, temperature=0")
    L.append("")
    L.append("DESCRIPTIVE / pre-gate. The floor-gloss changed the settled-core prompt (now in "
             "`current_template_hashes()`), staling the third-family manifest; every judge re-qualifies "
             "the SETTLED_CORE surface via the NEW settled-core probe. All other surfaces are carried "
             "forward from the frozen third-family manifest.")
    L.append("")
    if stopped:
        L.append(f"> **STOPPED: {stopped}** — see the honest-outcome section; combined manifest reflects the stop.")
        L.append("")

    L.append("## 1. Settled-core probe re-qualification (LIVE)")
    L.append("")
    L.append("| judge | settled_core n_pass/K | cause tally | SETTLED_CORE eligible now? |")
    L.append("|---|---|---|---|")
    for jname, _, jslug in INCUMBENT_JUDGES:
        pr = settled_reps.get(jname)
        if pr is None:
            continue
        elig = SETTLED_CORE in set(by_slug.get(jslug, {}).get("eligible_surfaces", []))
        L.append(f"| {jname} | {pr.n_pass}/{pr.k} | {pr.cause_tally()} | {'YES' if elig else 'NO — SUSPENDED'} |")
    L.append("")

    L.append("## 2. Combined manifest eligibility (carried-forward + settled requal + frontier)")
    L.append("")
    L.append("| judge | family | eligible surfaces |")
    L.append("|---|---|---|")
    for j in combined["judges"]:
        L.append(f"| {j['name']} | {j['family']} | {j['eligible_surfaces'] or '[] — discarded'} |")
    L.append("")
    # settled-core family count (the load-bearing ≥2 check)
    sc_fams = sorted({j["family"] for j in combined["judges"] if SETTLED_CORE in j["eligible_surfaces"]})
    oa_fams = sorted({j["family"] for j in combined["judges"] if OPEN_AWARD in j["eligible_surfaces"]})
    disc_fams = sorted({j["family"] for j in combined["judges"] if DISCLOSURE in j["eligible_surfaces"]})
    L.append(f"- **SETTLED_CORE valid families:** {sc_fams} ({len(sc_fams)})")
    L.append(f"- **OPEN_AWARD valid families:** {oa_fams} ({len(oa_fams)})")
    L.append(f"- **DISCLOSURE valid families:** {disc_fams} ({len(disc_fams)})")
    L.append("")

    L.append("## 3. Frontier OPEN-award screen (R36.4, LIVE)")
    L.append("")
    if not frontier_results:
        L.append("No frontier candidate slug was live in the catalog (or the screen was skipped after a "
                 "settled-core STOP). Frontier screen not run.")
    else:
        L.append("| candidate | family | g4 | award-consist | discrimination | OPEN-award qualified? |")
        L.append("|---|---|---|---|---|---|")
        for r in frontier_results:
            pp = r["probe_pass"]
            L.append(f"| {r['name']} | {r['family']} | {pp['g4']['n_pass']}/{K} | "
                     f"{pp['award_consistency']['n_pass']}/{K} | {pp['discrimination']['n_pass']}/{K} | "
                     f"{'YES' if r['open_award_qualified'] else 'no'} |")
        L.append("")
        if frontier_qualified:
            L.append(f"**OPEN award GAINED a 2nd family: `{frontier_qualified['slug']}` "
                     f"(family={frontier_qualified['family']}).** Joined the combined manifest.")
        else:
            L.append("No frontier candidate qualified for the OPEN award. MVP ships single-family-labeled "
                     "on OPEN award (R34.4 unchanged).")
    L.append("")

    L.append("## 4. Fresh template hashes (settled-core now hashed — R35.6 gap closed)")
    L.append("")
    for k, v in sorted(combined["template_hashes"].items()):
        L.append(f"- `{k}`: `{v}`")
    L.append("")
    L.append("## 5. Guardrails")
    L.append("")
    L.append("Report immutability: NEW dated dir; the third-family-screen manifest is FROZEN/untouched. "
             "Canary not re-minted. Secrets runtime-only. Scope-locked to WCF-Benchmark.")
    L.append("")
    with open(md, "w") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"wrote {md}")


def main():
    global K
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true", help="make the real API calls (spends tokens)")
    ap.add_argument("-k", type=int, default=K, help="reps per probe")
    args = ap.parse_args()
    K = args.k
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if args.go and not api_key:
        print("ERROR: $OPENROUTER_API_KEY not set. `source ~/.codex/secrets/openrouter.env` first.",
              file=sys.stderr)
        return 2
    return run(api_key, args.go)


if __name__ == "__main__":
    raise SystemExit(main())
