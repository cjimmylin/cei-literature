#!/usr/bin/env python
"""OpenRouter 3-judge per-surface pilot — memo R33.4/R33.5/R33.6 (session 11).

The session-10 adjudication (R29/R30) suspended gpt-4o-mini for the disclosure surface
(dead constant channel) and gemini-2.5-flash for the OPEN award form (holistic
all-or-nothing) — leaving ONE valid disclosure judge and ONE valid OPEN-award judge on
the 2-judge panel (R30 makes H-DISC unpromotable there). R33.5 wires a THIRD fast-mid
family (mistral, ∉ {openai, google, anthropic, SUT families}) and re-runs the 6-item
slice descriptively so BOTH surfaces regain a cross-judge pair — confirming the
disclosure channel now discriminates.

The panel qualifies each judge PER SURFACE under the extended battery (R33.4: G4 +
award-consistency + discrimination + disclosure-inversion + negative-disclosure), so the
suspensions are re-derived live (and a re-qualified judge is re-admitted). k=3 → all
three judges grade every item; per-surface aggregation then selects the eligible ones.

SAFETY: default run prints the PLAN and makes NO calls. Pass --go to spend tokens.
Requires $OPENROUTER_API_KEY (`source ~/.codex/secrets/openrouter.env`).

    python openrouter_pilot_r33.py           # dry: plan + slug check, 0 calls
    python openrouter_pilot_r33.py --go       # real calls (a few cents)
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import urllib.error
import urllib.request

HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import (  # noqa: E402
    load_items, run, scorer_kind, OPEN, CONTESTED,
    OpenRouterModelClient, OpenRouterError, EXAMINEE_SYSTEM,
    JudgePanel, summarize_disagreement, template_hash, write_run_transcripts,
    OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE,
)
from wcfbench.judge import JudgeError  # noqa: E402

BANK_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "05-BANK-YAML"))
MODELS_URL = "https://openrouter.ai/api/v1/models"
# R33.5 re-run -> a NEW dated run directory (report immutability; the pre-fix and
# 20260710-open-contested-postfix dirs stay untouched).
OUT_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "07-PILOTS", "20260710-r33-3judge"))

# Three judges spanning three distinct families, none Anthropic (the bank is opus/
# anthropic-authored → generator-family exclusion drops Anthropic judges). Fast-mid tier
# (WALKWORTHY F-1). The third family is mistral (qwen dropped — WALKWORTHY F-2 dead slug).
DEFAULT_JUDGES = [
    ("gpt4omini", "openai", "openai/gpt-4o-mini"),
    ("gemini-flash", "google", "google/gemini-2.5-flash"),
    ("mistral-small", "mistral", "mistralai/mistral-small-3.2-24b-instruct"),
]
# SUTs: cross-family, distinct from every judge family (no self-family judging).
DEFAULT_SUTS = [
    "meta-llama/llama-3.1-8b-instruct",
    "deepseek/deepseek-chat",
]
DEFAULT_OPEN_DESIGNS = ["complicit", "mending", "wholeheart"]
JUDGE_MAX_TOKENS = 2048   # generous: the R33.1 reason+quote mandate lengthens verdicts.


def _select_items(open_designs):
    items = load_items(BANK_DIR)
    contested = [i for i in items if scorer_kind(i) == CONTESTED]
    chosen_open = []
    for design in open_designs:
        for i in items:
            if scorer_kind(i) == OPEN and i.design == design:
                chosen_open.append(i)
                break
    return chosen_open + contested


def fetch_model_ids(api_key):
    req = urllib.request.Request(MODELS_URL,
                                 headers={"Authorization": f"Bearer {api_key}"} if api_key else {},
                                 method="GET")
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return {m["id"] for m in data.get("data", []) if isinstance(m, dict) and "id" in m}


def _resolve(models, api_key):
    try:
        catalog = fetch_model_ids(api_key or "")
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError) as e:
        print(f"  ! could not fetch model catalog ({e}); proceeding without slug validation")
        return models, []
    return [m for m in models if m in catalog], [m for m in models if m not in catalog]


def _print_plan(items, judges, suts, api_key):
    print("=" * 74)
    print("OpenRouter 3-judge per-surface pilot — PLAN (dry run; pass --go for real calls)")
    print("=" * 74)
    print(f"bank: {BANK_DIR}")
    print(f"items ({len(items)}):")
    for it in items:
        print(f"  - {it.id:16s} {scorer_kind(it):9s} track={it.track} :: {it.stem.strip()[:52]}…")
    print(f"judges (3 families, per-surface qualified): {[(n, f, s) for n, f, s in judges]}")
    print(f"SUTs (examinees): {suts}")
    if api_key:
        allslugs = [s for _, _, s in judges] + suts
        valid, invalid = _resolve(allslugs, api_key)
        if invalid:
            print(f"  INVALID slugs (query {MODELS_URL}): {invalid}")
        else:
            print("  all slugs valid against the live catalog")
    else:
        print("  (set $OPENROUTER_API_KEY to validate slugs)")
    print(f"cost: a few cents (extended battery ×3 judges + {len(items)}×{len(suts)} cells × 3 judges).")
    print(f"output → {OUT_DIR}/")


def _build_panel(judges):
    clients = []
    for name, family, slug in judges:
        clients.append({"name": name, "family": family,
                        "client": OpenRouterModelClient(model=slug, max_tokens=JUDGE_MAX_TOKENS)})
    return JudgePanel(clients, k=3, calibrate=True)


def _run_live(items, judges, suts):
    print("\n" + "=" * 74)
    print("Building + qualifying the 3-judge panel (extended per-surface battery)…")
    print("=" * 74)
    try:
        panel = _build_panel(judges)
    except (OpenRouterError, JudgeError) as e:
        print(f"  PANEL UNUSABLE — {e}")
        return None
    print(f"  active judges: {[(n, f) for n, f, _ in panel.active]}")
    print("  per-surface eligibility (R33.4/R33.6):")
    for name in [n for n, _, _ in panel.active]:
        elig = sorted(panel.eligible.get(name, set()))
        susp = sorted({OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE} - set(elig))
        print(f"    {name:14s} eligible={elig}  suspended={susp}")
    if panel.discarded:
        print("  discard/suspension notes:")
        for n, reason in panel.discarded:
            print(f"    {n}: {reason}")

    # confirm the disclosure surface now has >= 2 valid families (R30 condition 6).
    disc_fams = {f for n, f, _ in panel.active if DISCLOSURE in panel.eligible.get(n, set())}
    open_fams = {f for n, f, _ in panel.active if OPEN_AWARD in panel.eligible.get(n, set())}
    print(f"  DISCLOSURE-valid families: {sorted(disc_fams)} "
          f"({'≥2 → cross-judge gap reportable' if len(disc_fams) >= 2 else '<2 → still starved'})")
    print(f"  OPEN-award-valid families: {sorted(open_fams)} "
          f"({'≥2 → cross-judge pair' if len(open_fams) >= 2 else '<2 → still starved'})")

    print("\n" + "=" * 74)
    print("Scoring OPEN (triaxial) + CONTESTED (position/coherence) across SUTs…")
    print("=" * 74)
    sut_clients = {s: OpenRouterModelClient(model=s, system=EXAMINEE_SYSTEM, max_tokens=2048) for s in suts}
    report = run(items, sut_clients, panel=panel)

    for s in suts:
        rep = report.reports[s]
        print(f"\n--- SUT {s} ---")
        for r in rep.results:
            tags = []
            if r.error:
                tags.append(f"ERROR={r.error[:48]}")
            if r.triaxial is not None:
                tags.append(f"M/Mn/E={r.triaxial.matter}/{r.triaxial.manner}/{r.triaxial.end}")
            if r.contested_score is not None:
                cs = r.contested_score
                tags.append(f"disc={cs.disclosure} coh={cs.coherence} core={cs.settled_core_fraction} "
                            f"rank_malformed={cs.ranking_malformed}")
            print(f"  [{r.item_id:14s}] {r.kind:9s} {' '.join(tags)}")
        trunc = getattr(sut_clients[s], "truncated_item_ids", [])
        if trunc:
            print(f"  ! SUT-truncated items: {trunc}")
        print(f"  usage: {rep.usage}")

    cells = summarize_disagreement(report)
    return panel, report, cells


def _write_outputs(panel, report, cells, judges, suts, items):
    os.makedirs(OUT_DIR, exist_ok=True)
    eligibility = {n: sorted(panel.eligible.get(n, set())) for n, _, _ in panel.active}
    raw = {
        "canary": "WCFBENCH-CANARY-c1647-x9k4q",
        "judges_active": [(n, f) for n, f, _ in panel.active],
        "judges_eligibility": eligibility,
        "judges_discarded": panel.discarded,
        "suts": suts,
        "items": [i.id for i in items],
        "cells": [
            {"item_id": c.item_id, "model": c.model, "kind": c.kind, "n_judges": c.n_judges,
             "max_spread": c.max_spread, "split_defensible": c.split_defensible,
             "axis_spreads": c.axis_spreads, "judge_values": c.judge_values, "detail": c.detail}
            for c in cells
        ],
        "per_item_raw": [
            {"model": m, "item_id": r.item_id, "kind": r.kind, "judge_raw": r.judge_raw,
             "error": r.error}
            for m, rep in report.reports.items() for r in rep.results
            if getattr(r, "judge_raw", None)
        ],
    }
    with open(os.path.join(OUT_DIR, "disagreement.json"), "w") as fh:
        json.dump(raw, fh, indent=2)
    print(f"\n  wrote {OUT_DIR}/disagreement.json ({len(cells)} cells)")

    th = template_hash()
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    run_meta = {"canary": "WCFBENCH-CANARY-c1647-x9k4q",
                "judges_active": [(n, f) for n, f, _ in panel.active],
                "judges_eligibility": eligibility, "suts": suts}
    tpath = write_run_transcripts(report, OUT_DIR, template_hash=th, timestamp=ts, run_meta=run_meta)
    n_lines = sum(1 for _ in open(tpath))
    print(f"  wrote {tpath} ({n_lines} transcript cells; template_hash={th})")

    print("\n  Top disagreement clusters (worst-first):")
    for c in cells[:8]:
        print(f"    {c.item_id:14s} {c.model:28s} {c.detail}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true", help="make the real API calls (spends tokens)")
    ap.add_argument("--suts", default=",".join(DEFAULT_SUTS))
    ap.add_argument("--open-designs", default=",".join(DEFAULT_OPEN_DESIGNS))
    args = ap.parse_args()

    suts = [s.strip() for s in args.suts.split(",") if s.strip()]
    open_designs = [d.strip() for d in args.open_designs.split(",") if d.strip()]
    judges = DEFAULT_JUDGES
    api_key = os.environ.get("OPENROUTER_API_KEY")
    items = _select_items(open_designs)

    if not args.go:
        _print_plan(items, judges, suts, api_key)
        return 0

    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY not set. `source ~/.codex/secrets/openrouter.env` first.",
              file=sys.stderr)
        return 2

    allslugs = [s for _, _, s in judges] + suts
    valid, invalid = _resolve(allslugs, api_key)
    if invalid:
        print(f"ERROR: invalid slug(s) not in catalog: {invalid}. Query {MODELS_URL}.", file=sys.stderr)
        return 2

    out = _run_live(items, judges, suts)
    if out is None:
        return 1
    panel, report, cells = out
    _write_outputs(panel, report, cells, judges, suts, items)
    print("\n" + "-" * 74)
    print("Pilot complete. DESCRIPTIVE / pre-gate — NOT the gated measurement. The per-surface "
          "eligibility + the disclosure cross-judge gap are the R33.5 deliverable; a Fable "
          "session adjudicates the third family's qualification if it disagrees with the memo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
