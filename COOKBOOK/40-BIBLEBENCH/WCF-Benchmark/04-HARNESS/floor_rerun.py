#!/usr/bin/env python
"""Floor re-run of the 6-item slice with the MANIFEST-driven panel — memo R37.1 (session 12).

The session-11 settled-core PROMPT fix (the reason mandate the settled-core prompt never
asked for → floor collapsed to 0.0 in the pre-fix 20260710-r33-3judge run) must be
confirmed: the R31 sample-level floor (settled-core credited on the contested slice) holds
post-fix. This re-runs the same slice with a JudgePanel that CONSUMES a frozen qualification
manifest (R35.4) — NO probes re-run at construction, so per-surface eligibility cannot flip —
and reports whether disclosure / OPEN award gained a second valid family.

The judge roster is derived from the manifest (each judge with a non-empty eligible-surface
set becomes an OpenRouter client). Point --manifest at the combined third-family manifest if
the R36 screen wired a new family; else the provisional manifest of record.

SAFETY: default prints the PLAN, 0 calls. --go spends tokens (a few cents).
Requires $OPENROUTER_API_KEY. Writes a NEW dated dir (report immutability).

    python floor_rerun.py            # dry: plan + slug/manifest check
    python floor_rerun.py --go       # real calls
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
    load_manifest, manifest_is_fresh,
)
from wcfbench.judge import JudgeError  # noqa: E402

BANK_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "05-BANK-YAML"))
MODELS_URL = "https://openrouter.ai/api/v1/models"
PROVISIONAL_MANIFEST = os.path.normpath(os.path.join(
    HARNESS_ROOT, "..", "07-PILOTS", "20260710-probe-stability", "20260710-qualification-manifest.json"))
OUT_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "07-PILOTS", "20260710-floor-rerun"))

DEFAULT_SUTS = ["meta-llama/llama-3.1-8b-instruct", "deepseek/deepseek-chat"]
DEFAULT_OPEN_DESIGNS = ["complicit", "mending", "wholeheart"]
JUDGE_MAX_TOKENS = 2048


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


def _roster_from_manifest(manifest):
    """Judges the manifest qualified for >=1 surface (the discarded empties are skipped)."""
    return [(j["name"], j["family"], j["slug"]) for j in manifest["judges"] if j.get("eligible_surfaces")]


def _build_panel(roster, manifest):
    clients = [{"name": n, "family": f, "slug": s,
                "client": OpenRouterModelClient(model=s, max_tokens=JUDGE_MAX_TOKENS)}
               for n, f, s in roster]
    return JudgePanel(clients, k=len(clients), manifest=manifest)


def _print_plan(items, roster, suts, manifest, api_key):
    print("=" * 74)
    print("Floor re-run (manifest-driven panel) — PLAN (dry run; pass --go for real calls)")
    print("=" * 74)
    print(f"manifest: {manifest.get('run_dir')} | memo={manifest.get('memo')} | fresh={manifest_is_fresh(manifest)}")
    print(f"roster (>=1 surface): {roster}")
    for j in manifest["judges"]:
        print(f"    {j['slug']:44s} -> {j['eligible_surfaces'] or '[] discarded'}")
    print(f"items ({len(items)}):")
    for it in items:
        print(f"  - {it.id:16s} {scorer_kind(it):9s} :: {it.stem.strip()[:52]}…")
    print(f"SUTs: {suts}")
    if api_key:
        allslugs = [s for _, _, s in roster] + suts
        try:
            catalog = fetch_model_ids(api_key)
            invalid = [s for s in allslugs if s not in catalog]
            print(f"  invalid slugs: {invalid or 'none — all live'}")
        except Exception as e:
            print(f"  ! catalog fetch failed: {e}")
    print(f"output -> {OUT_DIR}/")


def _run_live(items, roster, suts, manifest):
    print("\n" + "=" * 74)
    print("Building the manifest-driven panel (NO probes re-run at construction — R35.4)…")
    print("=" * 74)
    try:
        panel = _build_panel(roster, manifest)
    except (OpenRouterError, JudgeError) as e:
        print(f"  PANEL UNUSABLE — {e}")
        return None
    print(f"  active judges: {[(n, f) for n, f, _ in panel.active]}")
    for name in [n for n, _, _ in panel.active]:
        elig = sorted(panel.eligible.get(name, set()))
        susp = sorted({OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE} - set(elig))
        print(f"    {name:14s} eligible={elig}  suspended={susp}")
    disc_fams = {f for n, f, _ in panel.active if DISCLOSURE in panel.eligible.get(n, set())}
    open_fams = {f for n, f, _ in panel.active if OPEN_AWARD in panel.eligible.get(n, set())}
    core_fams = {f for n, f, _ in panel.active if SETTLED_CORE in panel.eligible.get(n, set())}
    print(f"  DISCLOSURE-valid families: {sorted(disc_fams)} "
          f"({'>=2 → cross-judge pair' if len(disc_fams) >= 2 else '<2 → single-family (R34.4 label)'})")
    print(f"  OPEN-award-valid families: {sorted(open_fams)} "
          f"({'>=2 → cross-judge pair' if len(open_fams) >= 2 else '<2 → single-family (R34.4 label)'})")
    print(f"  SETTLED-CORE-valid families: {sorted(core_fams)}")

    print("\n" + "=" * 74)
    print("Scoring OPEN (triaxial) + CONTESTED (position/coherence/settled-core) across SUTs…")
    print("=" * 74)
    sut_clients = {s: OpenRouterModelClient(model=s, system=EXAMINEE_SYSTEM, max_tokens=2048) for s in suts}
    report = run(items, sut_clients, panel=panel)

    floor_rows = []
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
                tags.append(f"disc={cs.disclosure} coh={cs.coherence} core={cs.settled_core_fraction}")
                floor_rows.append((s, r.item_id, cs.settled_core_fraction))
            print(f"  [{r.item_id:14s}] {r.kind:9s} {' '.join(tags)}")
        print(f"  usage: {rep.usage}")

    # R31 floor check: every contested cell credits the settled core (fraction > 0) post-fix.
    n_cells = len(floor_rows)
    n_floor = sum(1 for _, _, frac in floor_rows if frac and frac > 0)
    print("\n" + "=" * 74)
    print(f"SETTLED-CORE FLOOR: {n_floor}/{n_cells} contested cells credit the settled core "
          f"(post settled-core prompt fix). {'FLOOR HOLDS' if n_floor == n_cells and n_cells else 'CHECK'}")
    print("=" * 74)
    cells = summarize_disagreement(report)
    return panel, report, cells, floor_rows, (n_floor, n_cells)


def _write_outputs(panel, report, cells, roster, suts, items, floor_rows, floor_stat, manifest):
    os.makedirs(OUT_DIR, exist_ok=True)
    eligibility = {n: sorted(panel.eligible.get(n, set())) for n, _, _ in panel.active}
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    raw = {
        "canary": "WCFBENCH-CANARY-c1647-x9k4q",
        "timestamp": ts,
        "manifest_run_dir": manifest.get("run_dir"),
        "manifest_memo": manifest.get("memo"),
        "judges_active": [(n, f) for n, f, _ in panel.active],
        "judges_eligibility": eligibility,
        "judges_discarded": panel.discarded,
        "suts": suts,
        "items": [i.id for i in items],
        "settled_core_floor": {"n_floor": floor_stat[0], "n_cells": floor_stat[1],
                               "rows": [{"sut": s, "item_id": i, "fraction": f} for s, i, f in floor_rows]},
        "cells": [
            {"item_id": c.item_id, "model": c.model, "kind": c.kind, "n_judges": c.n_judges,
             "max_spread": c.max_spread, "split_defensible": c.split_defensible,
             "axis_spreads": c.axis_spreads, "judge_values": c.judge_values, "detail": c.detail}
            for c in cells
        ],
        "per_item_raw": [
            {"model": m, "item_id": r.item_id, "kind": r.kind, "judge_raw": r.judge_raw, "error": r.error}
            for m, rep in report.reports.items() for r in rep.results if getattr(r, "judge_raw", None)
        ],
    }
    with open(os.path.join(OUT_DIR, "disagreement.json"), "w") as fh:
        json.dump(raw, fh, indent=2)
    th = template_hash()
    run_meta = {"canary": "WCFBENCH-CANARY-c1647-x9k4q", "judges_active": [(n, f) for n, f, _ in panel.active],
                "judges_eligibility": eligibility, "suts": suts}
    tpath = write_run_transcripts(report, OUT_DIR, template_hash=th, timestamp=ts, run_meta=run_meta)
    n_lines = sum(1 for _ in open(tpath))
    print(f"\n  wrote {OUT_DIR}/disagreement.json + {tpath} ({n_lines} cells; template_hash={th})")

    # NEW dated report (report immutability)
    disc_fams = sorted({f for n, f, _ in panel.active if DISCLOSURE in panel.eligible.get(n, set())})
    open_fams = sorted({f for n, f, _ in panel.active if OPEN_AWARD in panel.eligible.get(n, set())})
    md = os.path.join(OUT_DIR, "20260710-floor-rerun-report.md")
    lines = [
        "# WCF-Bench — Floor Re-run (manifest-driven panel, post settled-core fix)", "",
        f"Canary: `WCFBENCH-CANARY-c1647-x9k4q`  ·  Run: {ts}  ·  manifest: {manifest.get('run_dir')}",
        "", "DESCRIPTIVE / pre-gate. Confirms the R31 settled-core floor holds after the "
        "session-11 settled-core prompt fix, with a JudgePanel that consumes a frozen "
        "qualification manifest (R35.4 — no probe re-run at construction).", "",
        "## Settled-core floor",
        "",
        f"- **{floor_stat[0]}/{floor_stat[1]}** contested cells credit the settled core (fraction > 0).",
        f"- Verdict: {'FLOOR HOLDS (R31 confirmed post-fix)' if floor_stat[0] == floor_stat[1] and floor_stat[1] else 'CHECK — see rows'}",
        "",
        "| SUT | item | settled_core_fraction |", "|---|---|---|",
    ]
    for s, i, f in floor_rows:
        lines.append(f"| {s} | {i} | {f} |")
    lines += [
        "", "## Cross-family coverage per scored surface (R34.4)", "",
        f"- DISCLOSURE-valid families: {disc_fams} "
        f"({'>=2 → cross-judge pair' if len(disc_fams) >= 2 else '<2 → SINGLE-FAMILY (numbers not a measurement)'})",
        f"- OPEN-award-valid families: {open_fams} "
        f"({'>=2 → cross-judge pair' if len(open_fams) >= 2 else '<2 → SINGLE-FAMILY (numbers not a measurement)'})",
        "",
        "Active judges + eligibility: " + "; ".join(f"{n}={eligibility[n]}" for n, _, _ in panel.active),
        "",
    ]
    with open(md, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"  wrote {md}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true", help="make the real API calls (spends tokens)")
    ap.add_argument("--manifest", default=PROVISIONAL_MANIFEST,
                    help="qualification manifest to consume (default: provisional of record)")
    ap.add_argument("--suts", default=",".join(DEFAULT_SUTS))
    ap.add_argument("--open-designs", default=",".join(DEFAULT_OPEN_DESIGNS))
    args = ap.parse_args()

    suts = [s.strip() for s in args.suts.split(",") if s.strip()]
    open_designs = [d.strip() for d in args.open_designs.split(",") if d.strip()]
    api_key = os.environ.get("OPENROUTER_API_KEY")
    items = _select_items(open_designs)
    manifest = load_manifest(args.manifest)
    roster = _roster_from_manifest(manifest)

    if not args.go:
        _print_plan(items, roster, suts, manifest, api_key)
        return 0
    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY not set. `source ~/.codex/secrets/openrouter.env` first.",
              file=sys.stderr)
        return 2
    if not manifest_is_fresh(manifest):
        print("ERROR: manifest is STALE (template-hash drift) — re-qualify before the floor re-run.",
              file=sys.stderr)
        return 2

    out = _run_live(items, roster, suts, manifest)
    if out is None:
        return 1
    panel, report, cells, floor_rows, floor_stat = out
    _write_outputs(panel, report, cells, roster, suts, items, floor_rows, floor_stat, manifest)
    print("\nFloor re-run complete. DESCRIPTIVE / pre-gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
