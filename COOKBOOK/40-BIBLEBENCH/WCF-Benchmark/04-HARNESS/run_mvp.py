#!/usr/bin/env python
"""WCF-Bench MVP full-bank runner — resumable, per-cell descriptive pilot (session-13).

A single entrypoint that runs the WHOLE runnable bank (open + ordinal + anchor + contested;
EPISODE + dev_set_only excluded) across a configurable SUT roster, under a manifest-driven
JudgePanel, with the one capability the existing one-shot pipeline lacks: **per-(item, SUT)
checkpoint/resume**. Interrupt it (SIGINT, crash, budget cap) and re-run against the same
``--run-dir``; completed cells are skipped, the run continues where it stopped.

DESCRIPTIVE / PRE-GATE. This is NOT a gated G1–G7 measurement. OPEN-award numbers are labeled
SINGLE-FAMILY when <2 open_award-eligible families are in the manifest (R34.4). Settled-core
0.0 / False keypoints are a SCREEN, listed for sample-level review (R39(e)), never asserted as
a model failure. Every cell persists the SUT prompt+response + judge verdict texts (R27).

MODES (safety-first: default = dry-run, 0 network calls):
    python run_mvp.py                 # DRY-RUN: item counts, roster, cell plan, cost projection
    python run_mvp.py --limit 3       # SMOKE: first 3 items live (needs --go)
    python run_mvp.py --go            # LIVE full bank
    python run_mvp.py --go --run-dir 07-PILOTS/20260710-mvp-run   # RESUME an existing run dir

Requires $OPENROUTER_API_KEY for any live call. Writes a NEW dated run dir (report immutability).
"""

from __future__ import annotations

import argparse
import datetime
import os
import sys

HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import load_manifest, manifest_is_fresh  # noqa: E402
from wcfbench import mvp  # noqa: E402

BANK_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "05-BANK-YAML"))
DEFAULT_MANIFEST = os.path.normpath(os.path.join(
    HARNESS_ROOT, "..", "07-PILOTS", "20260710-third-family-screen",
    "20260710-third-family-manifest.json"))
PILOTS_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "07-PILOTS"))


def _default_run_dir() -> str:
    return os.path.join(PILOTS_DIR, f"{datetime.date.today():%Y%m%d}-mvp-run")


def _now() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")


def _print_dry_run(plan, suts, manifest, run_dir, budget, api_key):
    from wcfbench import OPEN_AWARD, DISCLOSURE, SETTLED_CORE
    print("=" * 76)
    print("WCF-Bench MVP runner — DRY-RUN plan (no network; pass --go for live calls)")
    print("=" * 76)
    print(f"canary: {mvp.CANARY}")
    print(f"manifest: {manifest.get('run_dir')} | memo={manifest.get('memo')} | "
          f"fresh={manifest_is_fresh(manifest)}")
    print(f"bank: {plan.total_loaded} loaded → {len(plan.runnable)} runnable "
          f"(excluded dev_set_only={plan.excluded_dev}; EPISODE={len(plan.excluded_episode)})")
    print(f"roster (judges >=1 surface): {[(n, f) for n, f, _ in mvp.manifest_roster(manifest)]}")
    print(f"  OPEN-award families:  {mvp.eligible_families(manifest, OPEN_AWARD)} "
          f"({'>=2 cross-family' if len(mvp.eligible_families(manifest, OPEN_AWARD)) >= 2 else '<2 SINGLE-FAMILY (R34.4)'})")
    print(f"  DISCLOSURE families:  {mvp.eligible_families(manifest, DISCLOSURE)}")
    print(f"  SETTLED-CORE families:{mvp.eligible_families(manifest, SETTLED_CORE)}")
    print(f"SUTs ({len(suts)}): {suts}")
    n_cells = len(plan.runnable) * len(suts)
    print(f"cell plan: {len(plan.runnable)} items × {len(suts)} SUTs = {n_cells} cells")
    print(f"budget cap: ${budget:.2f} | run dir: {run_dir}")

    # cost projection from live pricing if a key is present, else a placeholder rate.
    if api_key:
        try:
            catalog = mvp.fetch_model_catalog(api_key)
            all_slugs = suts + [s for _, _, s in mvp.manifest_roster(manifest)]
            missing = [s for s in all_slugs if s not in catalog]
            print(f"  slug check: {'ALL LIVE' if not missing else 'MISSING ' + str(missing)}")
            for s in suts:
                pp, pc = mvp.price_for(s, catalog)
                print(f"    {s:44s} $/1K prompt≈{pp*1000:.5f}  $/1K completion≈{pc*1000:.5f}")
            # rough projection at ~700 prompt + ~500 completion tok / SUT cell.
            proj = sum(mvp.cell_cost(700, 500, mvp.price_for(s, catalog)) for s in suts) \
                * len(plan.runnable)
            print(f"  projected SUT cost @ ~700p/500c per cell: ${proj:.4f} "
                  f"(judge cost additional; see report after --go)")
        except Exception as e:  # pragma: no cover - network path
            print(f"  ! catalog/pricing fetch failed: {e} (dry projection unavailable)")
    else:
        print("  no $OPENROUTER_API_KEY — projection uses placeholder rate "
              "($0.001/1K prompt, $0.002/1K completion):")
        placeholder = (0.001 / 1000, 0.002 / 1000)
        proj = mvp.cell_cost(700, 500, placeholder) * len(plan.runnable) * len(suts)
        print(f"  projected SUT cost: ${proj:.4f} (illustrative only)")
    print("=" * 76)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="WCF-Bench MVP full-bank resumable runner")
    ap.add_argument("--go", action="store_true",
                    help="make the real API calls (spends tokens). Default = dry-run.")
    ap.add_argument("--limit", type=int, default=None,
                    help="run only the first N runnable items (smoke mode).")
    ap.add_argument("--suts", default=",".join(mvp.DEFAULT_SUTS),
                    help="comma-separated OpenRouter SUT slugs (non-judge families).")
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST,
                    help="qualification manifest to consume (a newer re-qualification is fine).")
    ap.add_argument("--run-dir", default=None,
                    help="output dir; resume if it already has a checkpoint.jsonl. "
                         "Default: 07-PILOTS/<YYYYMMDD>-mvp-run/")
    ap.add_argument("--budget", type=float, default=mvp.DEFAULT_BUDGET_USD,
                    help=f"abort cleanly (checkpointed) at this $ estimate (default {mvp.DEFAULT_BUDGET_USD}).")
    ap.add_argument("--print-every", type=int, default=10,
                    help="print running cost/token/error line every N new cells.")
    ap.add_argument("--concurrency", type=int, default=1,
                    help="number of cells to score in parallel (default 1 = sequential; "
                         "N>1 uses a ThreadPoolExecutor). Cells for the same SUT are "
                         "serialized on that client; distinct SUTs run in parallel. "
                         "Checkpoint/budget/resume semantics are unchanged.")
    ap.add_argument("--bank-dir", default=BANK_DIR, help="bank YAML dir (default 05-BANK-YAML).")
    ap.add_argument("--regen-report", action="store_true",
                    help="OFFLINE: rebuild the report + disagreement.json for --run-dir from its "
                         "existing checkpoint.jsonl + transcripts.jsonl, covering ALL scored "
                         "cells (resume-safe). Opens NO network. Reuses transcripts in place.")
    ap.add_argument("--report-name", default=None,
                    help="report filename to write (default <YYYYMMDD>-mvp-run-report.md).")
    args = ap.parse_args(argv)

    suts = [s.strip() for s in args.suts.split(",") if s.strip()]
    run_dir = args.run_dir or _default_run_dir()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    manifest = load_manifest(args.manifest)
    plan = mvp.select_bank(args.bank_dir)
    if args.limit is not None:
        plan.runnable = plan.runnable[: args.limit]

    report_name = args.report_name or f"{datetime.date.today():%Y%m%d}-mvp-run-report.md"

    # ---- OFFLINE REGEN (no network): rebuild report + disagreement over the FULL checkpoint ----
    if args.regen_report:
        if not os.path.exists(os.path.join(run_dir, "checkpoint.jsonl")):
            print(f"ERROR: no checkpoint.jsonl in {run_dir} — nothing to regenerate.",
                  file=sys.stderr)
            return 2
        ts = _now()
        # PURE-OFFLINE: no catalog fetch. Cost is recomputed from the checkpoint usage blocks
        # using an empty catalog → the per-token prices default to 0 for any model not carried
        # in the checkpoint's own usage (the estimate stays a documented lower bound).
        paths = mvp.regen_report(
            run_dir, plan, suts, manifest,
            timestamp=ts, budget_usd=args.budget, report_name=report_name, catalog={})
        print("=" * 76)
        print(f"REGENERATED (offline) report + disagreement for {run_dir}")
        for k, v in paths.items():
            print(f"  {k:12s} {v}")
        print("Covers ALL scored cells from checkpoint.jsonl (resume-safe). No network opened.")
        print("=" * 76)
        return 0

    # ---- DRY-RUN (default; no network) ----
    if not args.go:
        _print_dry_run(plan, suts, manifest, run_dir, args.budget, api_key)
        return 0

    # ---- LIVE ----
    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY not set. `source ~/.codex/secrets/openrouter.env` first.",
              file=sys.stderr)
        return 2
    if not manifest_is_fresh(manifest):
        print("ERROR: manifest is STALE (template-hash drift) — re-qualify before a live run.",
              file=sys.stderr)
        return 2

    # Key-side reconciliation snapshot + depleted-credit pre-flight.
    key_before = mvp.fetch_key_snapshot(api_key)
    remaining = key_before.get("limit_remaining")
    if remaining is None and key_before.get("limit") is not None and key_before.get("usage") is not None:
        remaining = key_before["limit"] - key_before["usage"]
    if remaining is not None and remaining < args.budget:
        print(f"ERROR: OpenRouter remaining credit ${remaining:.2f} is below the "
              f"${args.budget:.2f} run budget; stop for top-up before live calls.",
              file=sys.stderr)
        return 2

    # slug validation — FAIL LOUD with nearest-match suggestions (model IDs drift).
    print("Validating SUT + judge slugs against GET /api/v1/models …")
    catalog = mvp.fetch_model_catalog(api_key)
    all_slugs = suts + [s for _, _, s in mvp.manifest_roster(manifest)]
    try:
        mvp.validate_slugs(all_slugs, catalog)
    except mvp.SlugValidationError as e:
        print(str(e), file=sys.stderr)
        return 2
    print(f"  all {len(all_slugs)} slugs live.")

    # build clients + manifest-driven panel (no probes re-run at construction — R35.4).
    print("Building SUT clients + manifest-driven JudgePanel …")
    sut_clients = mvp.build_sut_clients(suts)
    panel = mvp.build_panel(manifest)
    print(f"  active judges: {[(n, f) for n, f, _ in panel.active]}")

    ts = _now()
    print(f"Running {len(plan.runnable)} items × {len(suts)} SUTs "
          f"({'SMOKE limit=' + str(args.limit) if args.limit is not None else 'FULL'}) "
          f"→ {run_dir}  (concurrency={args.concurrency})")
    outcome = mvp.run_bank(
        plan, suts, sut_clients, panel, run_dir,
        catalog=catalog, budget_usd=args.budget, print_every=args.print_every,
        concurrency=args.concurrency, logger=print, now=_now,
    )

    try:
        key_after = mvp.fetch_key_snapshot(api_key)
        if key_before.get("usage") is not None and key_after.get("usage") is not None:
            outcome.key_usage_delta_usd = key_after["usage"] - key_before["usage"]
    except Exception:  # paid results must persist even if reconciliation lookup fails
        print("WARNING: post-run key usage unavailable; report will mark reconciliation unavailable.",
              file=sys.stderr)

    paths = mvp.write_outputs(outcome, plan, suts, manifest, panel,
                              timestamp=ts, budget_usd=args.budget, report_name=report_name,
                              catalog=catalog)

    print("\n" + "=" * 76)
    print(f"MVP run {'ABORTED (budget)' if outcome.budget_hit else 'COMPLETE'} — "
          f"{outcome.completed} scored, {outcome.errored} errored, {outcome.skipped} skipped")
    print(f"internal cost ${max(outcome.est_cost_usd, outcome.actuals_to_date_usd):.4f} "
          f"/ budget ${args.budget:.2f} · "
          f"{outcome.total_tokens} tokens")
    for k, v in paths.items():
        print(f"  {k:12s} {v}")
    print("DESCRIPTIVE / PRE-GATE — not a gated G1–G7 measurement.")
    print("=" * 76)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
