#!/usr/bin/env python
"""OpenRouter OPEN + CONTESTED pilot — the live judge panel on real tokens.

Unlike ``openrouter_pilot.py`` (mechanical scorers + the NARROWGATE gate), this
drives the **§4.3 judge path**: it builds a cross-family :class:`JudgePanel`,
runs the **G4 calibration battery** on the real judges (discarding any that score
the polish-confound B >= A), then scores a diverse slice of OPEN items (triaxial
Matter/Manner/End) and the CONTESTED items (position/coherence adherence) across
2-3 SUT families — and writes the **cross-judge DISAGREEMENT clusters** a downstream
Fable session adjudicates (the boot prompt's deliverable).

OpenRouter is the sanctioned measurement path (Jimmy, 2026-07-09). This run stays
SMALL — it is a first live validation of the judge chain + the disagreement payload,
not the gated G1-G7 measurement.

SAFETY: default run prints the PLAN and makes NO calls. Pass --go to spend tokens.
Requires $OPENROUTER_API_KEY (`source ~/.codex/secrets/openrouter.env`). Slugs drift
— the dry run resolves requested models against /api/v1/models.

    python openrouter_pilot_open.py                 # dry: plan + slug check, 0 calls
    python openrouter_pilot_open.py --go            # real calls (a few cents)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import (  # noqa: E402
    load_items,
    run,
    scorer_kind,
    OPEN,
    CONTESTED,
    OpenRouterModelClient,
    OpenRouterError,
    EXAMINEE_SYSTEM,
    JudgePanel,
    summarize_disagreement,
)
from wcfbench.judge import JudgeError  # noqa: E402

BANK_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "05-BANK-YAML"))
MODELS_URL = "https://openrouter.ai/api/v1/models"
OUT_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "07-PILOTS", "20260710-open-contested"))

# Judges must be cross-family AND not the Anthropic family (the items are opus/
# anthropic-authored, so the generator-family exclusion drops Anthropic judges).
# Fast mid judges (WALKWORTHY F-1: frontier judges too slow).
DEFAULT_JUDGES = [
    ("gpt4omini", "openai", "openai/gpt-4o-mini"),
    ("gemini-flash", "google", "google/gemini-2.5-flash"),
]
# SUTs: cross-family, distinct from the judge families (no self-family judging).
DEFAULT_SUTS = [
    "meta-llama/llama-3.1-8b-instruct",
    "deepseek/deepseek-chat",
]
# A diverse OPEN slice (one per distinct design) + all CONTESTED items.
DEFAULT_OPEN_DESIGNS = ["complicit", "mending", "wholeheart"]


def _family_of(slug: str) -> str:
    head = slug.split("/", 1)[0].lower()
    return {"meta-llama": "meta", "mistralai": "mistral"}.get(head, head)


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
    print("OpenRouter OPEN+CONTESTED pilot — PLAN (dry run; pass --go for real calls)")
    print("=" * 74)
    print(f"bank: {BANK_DIR}")
    print(f"items ({len(items)}):")
    for it in items:
        print(f"  - {it.id:16s} {scorer_kind(it):9s} track={it.track} :: {it.stem.strip()[:56]}…")
    print(f"judges (cross-family, generator-excluded, G4-calibrated): "
          f"{[(n, f, s) for n, f, s in judges]}")
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
    print(f"cost: a few cents (G4 calibration + {len(items)}×{len(suts)} cells × 2 judges × 3-4 axis calls).")
    print(f"output → {OUT_DIR}/ (disagreement clusters for the Fable session)")


def _build_panel(judges):
    clients = []
    for name, family, slug in judges:
        clients.append({"name": name, "family": family,
                        "client": OpenRouterModelClient(model=slug, max_tokens=1024)})
    return JudgePanel(clients, k=2, calibrate=True)


def _run_live(items, judges, suts):
    print("\n" + "=" * 74)
    print("Building + calibrating the judge panel (G4 polish-confound battery)…")
    print("=" * 74)
    try:
        panel = _build_panel(judges)
    except (OpenRouterError, JudgeError) as e:
        print(f"  PANEL UNUSABLE — {e}")
        return None
    print(f"  active judges: {[(n, f) for n, f, _ in panel.active]}")
    if panel.discarded:
        print(f"  DISCARDED (miscalibrated / errored): {panel.discarded}")
    else:
        print("  no judge discarded — all passed G4 calibration")

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
                tags.append(f"triaxial M/Mn/E={r.triaxial.matter}/{r.triaxial.manner}/{r.triaxial.end}")
            if r.contested_score is not None:
                cs = r.contested_score
                tags.append(f"disc={cs.disclosure} defensible={cs.position_defensible} "
                            f"coh={cs.coherence} core={cs.settled_core_fraction}")
            print(f"  [{r.item_id:14s}] {r.kind:9s} {' '.join(tags)}")
        trunc = getattr(sut_clients[s], "truncated_item_ids", [])
        if trunc:
            print(f"  ! TRUNCATED items (finish_reason=length): {trunc}")
        print(f"  usage: {rep.usage}")

    cells = summarize_disagreement(report)
    return panel, report, cells


def _write_outputs(panel, report, cells, judges, suts, items):
    os.makedirs(OUT_DIR, exist_ok=True)
    # raw disagreement JSON
    raw = {
        "canary": "WCFBENCH-CANARY-c1647-x9k4q",
        "judges_active": [(n, f) for n, f, _ in panel.active],
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
        print(f"ERROR: invalid slug(s) not in catalog: {invalid}. Query {MODELS_URL} and pass --suts.",
              file=sys.stderr)
        return 2

    out = _run_live(items, judges, suts)
    if out is None:
        return 1
    panel, report, cells = out
    _write_outputs(panel, report, cells, judges, suts, items)
    print("\n" + "-" * 74)
    print("Pilot complete. This is a PILOT (small slice), NOT the gated measurement. The "
          "disagreement clusters + calibration outcome are the input a Fable session adjudicates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
