"""Multi-model PANEL RUNNER — the §1 P0 pilot + O4 panel driver (measurement path).

Generalizes the O3 smoke driver from a 1-item/design slice on ONE model to the full
`items x models` panel: it fans the ALREADY-TESTED, client-agnostic per-item pipeline
(`_run_05_allocation` / `execute_item` / `score_item` / `judge_item`) over N SUT models
and a selected item subset, with three additions and NO change to the measurement logic:

  1. **Deterministic item selection** (`select_panel_items`) — the first N items/design
     by id, so the P0 pilot's 5-items/design subset is reproducible from the manifest.
  2. **Per-(item, model) checkpoint + RESUME** — every scored record already carries
     `item_id` + `model`, so the output file `scored_items.jsonl` IS the checkpoint: on
     restart, completed cells are read and skipped, and a killed run continues without
     re-calling the model. An item's calls are one atomic unit (no mid-item recovery).
  3. **Cost tracking** — with an OpenRouter cost probe, each item's real `usage.cost`
     delta is stored on its record (`_panel_cost`); run + per-model totals are summed
     from the records, so the reported cost is resume-safe.

The two judges are cross-family and both != the item-generator family (charter §6.5);
disagreement is logged, never averaged. Judge/keyed-outcome semantics are UNCHANGED
from `run.score_item` (the `verdicts[0]` keyed-outcome coupling is a parked ruling,
PR-3 — surfaced in the report, not patched here).

This is the MEASUREMENT path (OpenRouter = a real paid API), but a P0 pilot's numbers
are DESCRIPTIVE / PRE-GATE: the §3.4 judge-validity gate (human labels) is not yet run,
so scores are a scale + mechanics shakeout, not a benchmark result.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Callable, List, Optional

from .executors import execute_item
from .loader import load_public_split
from .manifest import build_manifest
from .run import _run_05_allocation, score_item

PILOT_DISCLAIMER = (
    "P0 PILOT — real cross-model measurement PATH (OpenRouter), but the numbers are "
    "DESCRIPTIVE / PRE-GATE: a mechanics + scale shakeout on a 5-items/design subset. "
    "The §3.4 judge-validity gate (human labels) is NOT yet run, so no score here is a "
    "benchmark result. FIX-MECHANICS-ONLY: items are NOT edited from model performance."
)


# --------------------------------------------------------------------------- #
# item selection
# --------------------------------------------------------------------------- #
def select_panel_items(all_items, items_per_design: Optional[int] = None) -> list:
    """The first `items_per_design` runnable items per design, by id (deterministic).

    `items_per_design=None` -> every item (the full O4 panel). A design with fewer
    than N items contributes all of them. Selection is stable/reproducible so the
    manifest's IDs fully pin what ran.
    """
    if items_per_design is None:
        return list(all_items)
    by_design: dict = {}
    for it in all_items:
        by_design.setdefault(it.design, []).append(it)
    out = []
    for design in sorted(by_design):
        pool = sorted(by_design[design], key=lambda it: it.id)
        out.extend(pool[:items_per_design])
    return out


# --------------------------------------------------------------------------- #
# checkpoint helpers
# --------------------------------------------------------------------------- #
def _read_checkpoint(path: Path) -> List[dict]:
    """Read prior scored records (resume). Skips blank/corrupt lines defensively."""
    if not path.exists():
        return []
    out: List[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        if r.get("item_id") and r.get("model"):
            out.append(r)
    return out


def _cost_delta(before: Optional[dict], after: Optional[dict]) -> dict:
    zero = {"usd": 0.0, "calls": 0, "prompt_tokens": 0, "completion_tokens": 0}
    if before is None or after is None:
        return zero
    return {
        "usd": round(float(after.get("cost", 0.0)) - float(before.get("cost", 0.0)), 8),
        "calls": int(after.get("calls", 0)) - int(before.get("calls", 0)),
        "prompt_tokens": int(after.get("prompt_tokens", 0)) - int(before.get("prompt_tokens", 0)),
        "completion_tokens": (int(after.get("completion_tokens", 0))
                              - int(before.get("completion_tokens", 0))),
    }


# --------------------------------------------------------------------------- #
# aggregation
# --------------------------------------------------------------------------- #
def _aggregate(records: List[dict], judges) -> dict:
    cells: dict = {}
    refusal_overall: Counter = Counter()
    total_schema = 0
    cost_usd = cost_calls = ptok = ctok = 0.0
    cost_by_model: dict = defaultdict(float)
    jp_by_design: dict = {}

    for r in records:
        d, m = r["design"], r["model"]
        cd = cells.setdefault(d, {}).setdefault(
            m, {"scalars": [], "n": 0, "refusal": Counter(),
                "agree_cells": 0, "total_cells": 0, "n_disagreements": 0})
        cd["scalars"].append(float(r.get("scalar_goodness", 0.5)))
        cd["n"] += 1
        cd["refusal"][r.get("refusal_tag")] += 1
        refusal_overall[r.get("refusal_tag")] += 1
        total_schema += len(r.get("schema_errors", []))

        jr = r.get("judge_report", {}) or {}
        n_cells = int(jr.get("cells", 0))
        disagr = len(jr.get("disagreements", []))
        agree = n_cells - disagr
        cd["total_cells"] += n_cells
        cd["agree_cells"] += agree
        cd["n_disagreements"] += disagr
        jpd = jp_by_design.setdefault(d, {"agree": 0, "total": 0, "disagr": 0})
        jpd["agree"] += agree; jpd["total"] += n_cells; jpd["disagr"] += disagr

        pc = r.get("_panel_cost", {}) or {}
        cost_usd += float(pc.get("usd", 0.0)); cost_calls += int(pc.get("calls", 0))
        ptok += int(pc.get("prompt_tokens", 0)); ctok += int(pc.get("completion_tokens", 0))
        cost_by_model[m] += float(pc.get("usd", 0.0))

    cell_out: dict = {}
    for d, mm in cells.items():
        cell_out[d] = {}
        for m, cd in mm.items():
            mean = sum(cd["scalars"]) / len(cd["scalars"]) if cd["scalars"] else 0.0
            agree = (cd["agree_cells"] / cd["total_cells"]) if cd["total_cells"] else 1.0
            cell_out[d][m] = {
                "mean_scalar": round(mean, 4),
                "score_0_100": round(mean * 100, 1),
                "n": cd["n"],
                "refusal_tags": dict(cd["refusal"]),
                "judge_agreement": round(agree, 4),
                "n_disagreements": cd["n_disagreements"],
            }

    design_spread: dict = {}
    for d, mm in cell_out.items():
        by_model = {m: mm[m]["score_0_100"] for m in sorted(mm)}
        vals = list(by_model.values())
        design_spread[d] = {"by_model": by_model, "max": max(vals), "min": min(vals),
                            "spread_points": round(max(vals) - min(vals), 1)}

    total_cells = sum(v["total"] for v in jp_by_design.values())
    total_agree = sum(v["agree"] for v in jp_by_design.values())
    judge_pair = {
        "judges": [{"name": j.name, "family": j.family} for j in judges],
        "overall_agreement": round(total_agree / total_cells, 4) if total_cells else 1.0,
        "by_design": {d: (round(v["agree"] / v["total"], 4) if v["total"] else 1.0)
                      for d, v in sorted(jp_by_design.items())},
        "total_disagreement_cells": sum(v["disagr"] for v in jp_by_design.values()),
    }

    return {
        "cells": cell_out,
        "design_spread": design_spread,
        "judge_pair": judge_pair,
        "refusal_accounting": dict(refusal_overall),
        "total_schema_errors": total_schema,
        "cost": {
            "total_usd": round(cost_usd, 6),
            "calls": int(cost_calls),
            "prompt_tokens": int(ptok),
            "completion_tokens": int(ctok),
            "by_model": {m: round(c, 6) for m, c in sorted(cost_by_model.items())},
        },
    }


# --------------------------------------------------------------------------- #
# the runner
# --------------------------------------------------------------------------- #
def run_panel(benchmark_root, out_dir, sut_clients, judges, state_classifier,
              items_per_design: Optional[int] = None, designs: Optional[List[str]] = None,
              all_items=None, date_str: Optional[str] = None, panel: Optional[str] = None,
              resume: bool = True, cost_probe: Optional[Callable[[], dict]] = None,
              adapter: str = "openrouter", kind: str = "p0-pilot",
              disclaimer: str = PILOT_DISCLAIMER, notes: str = "",
              write_report: bool = True, progress: Optional[Callable] = None) -> dict:
    date_str = date_str or date.today().strftime("%Y%m%d")
    panel = panel or f"{date_str}-p0-pilot"
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    if all_items is None:
        # PUBLIC split only; loader HARD-REFUSES HOLDOUT (charter §6.6).
        all_items = load_public_split(benchmark_root, include_exemplars=True,
                                      runnable_only=True)
    if designs:
        want = set(designs)
        all_items = [it for it in all_items if it.design in want]
    slice_items = select_panel_items(all_items, items_per_design)

    models_meta = [{"name": s.name, "family": getattr(s, "family", "unknown"),
                    "adapter": adapter} for s in sut_clients]
    manifest = build_manifest(
        panel=panel, date_str=date_str, benchmark_root=benchmark_root,
        models=models_meta,
        judges=[{"name": j.name, "family": j.family} for j in judges],
        items=slice_items,
        notes=notes or f"{kind}: {len(slice_items)} items x {len(sut_clients)} models "
                       f"(measurement path; {disclaimer[:40]}...).",
    )
    manifest.write(out / "manifest.json")
    seeds = manifest.permutation_seeds

    ckpt = out / "scored_items.jsonl"
    errpath = out / "panel_errors.jsonl"
    existing = _read_checkpoint(ckpt) if resume else []
    done = {(r.get("item_id"), r.get("model")) for r in existing}

    new_records: List[dict] = []
    errors: List[dict] = []
    mode = "a" if (resume and ckpt.exists()) else "w"
    fh = ckpt.open(mode, encoding="utf-8")
    efh = errpath.open("a" if resume and errpath.exists() else "w", encoding="utf-8")
    try:
        for sut in sut_clients:
            for item in slice_items:
                key = (item.id, sut.name)
                if key in done:
                    continue
                before = cost_probe() if cost_probe else None
                # A single bad model response (e.g. empty content mid multi-turn) must
                # NOT kill the whole panel — log it as data and continue (master plan §2:
                # "non-compliance logged as data"). No scored record is written, so the
                # cell is retried on the next resume (transient errors self-heal).
                try:
                    allocation = None
                    if item.design.startswith("05"):
                        allocation, _ = _run_05_allocation(item, sut)
                    ex = execute_item(item, sut, seeds, state_classifier=state_classifier)
                    rec = score_item(item, ex, judges, allocation=allocation)
                except Exception as e:  # noqa: BLE001 — batch runner must survive any cell
                    after = cost_probe() if cost_probe else None
                    err = {"item_id": item.id, "design": item.design, "model": sut.name,
                           "error_type": type(e).__name__, "error": str(e)[:300],
                           "cost": _cost_delta(before, after)}
                    errors.append(err)
                    efh.write(json.dumps(err, ensure_ascii=False) + "\n")
                    efh.flush()
                    if progress:
                        progress(sut.name, f"{item.id} !ERROR {type(e).__name__}", len(new_records))
                    continue
                after = cost_probe() if cost_probe else None
                rec["_panel_cost"] = _cost_delta(before, after)
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                fh.flush()
                new_records.append(rec)
                done.add(key)
                if progress:
                    progress(sut.name, item.id, len(new_records))
    finally:
        fh.close()
        efh.close()

    all_records = existing + new_records
    judge_defects: list = []
    for j in judges:
        judge_defects.extend(getattr(j, "defects", []))
    classifier_defects = list(getattr(state_classifier, "defects", []))

    agg = _aggregate(all_records, judges)
    top = {
        "panel": panel,
        "date": date_str,
        "kind": kind,
        "disclaimer": disclaimer,
        "adapter": adapter,
        "designs": sorted({it.design for it in slice_items}),
        "items_per_design": items_per_design,
        "suts": [{"name": s.name, "family": s.family} for s in sut_clients],
        "n_items": len(slice_items),
        "n_models": len({r["model"] for r in all_records}),
        "n_records": len(all_records),
        "n_new_records": len(new_records),
        "n_errors": len(errors),
        "errors": errors,
        "defects": {"judge": judge_defects, "classifier": classifier_defects},
    }
    top.update(agg)

    (out / "panel_summary.json").write_text(json.dumps(top, indent=2, ensure_ascii=False),
                                            encoding="utf-8")
    if write_report:
        (out / "panel_report.md").write_text(_render_panel_report(top), encoding="utf-8")
    return top


# --------------------------------------------------------------------------- #
# report
# --------------------------------------------------------------------------- #
def _render_panel_report(top: dict) -> str:
    suts = [s["name"] for s in top["suts"]]
    L = [
        "# WALKWORTHY — P0 pilot panel (auto-render)",
        "",
        "<!-- WALKWORTHY-CANARY-7f3e2026 -->",
        f"> **{top['disclaimer']}**",
        "",
        f"**Panel:** `{top['panel']}`  ·  **kind:** {top['kind']}  ·  "
        f"**adapter:** {top['adapter']}",
        f"**SUT models ({top['n_models']}):** " + ", ".join(
            f"{s['name']} ({s['family']})" for s in top["suts"]),
        f"**Judges (cross-family):** " + ", ".join(
            f"{j['name']}/{j['family']}" for j in top["judge_pair"]["judges"]),
        "",
        f"Items/design: {top['items_per_design']}  ·  items: {top['n_items']}  ·  "
        f"records: {top['n_records']}  ·  new this run: {top['n_new_records']}  ·  "
        f"cell errors: {top.get('n_errors', 0)}  ·  "
        f"schema errors: {top['total_schema_errors']}  ·  "
        f"judge defects: {len(top['defects']['judge'])}  ·  "
        f"classifier defects: {len(top['defects']['classifier'])}",
        "",
    ]
    errs = top.get("errors") or []
    if errs:
        by_model_err: Counter = Counter(e.get("model") for e in errs)
        L += [f"> **{len(errs)} cell error(s)** (logged as data, not scored; retried on "
              f"resume): " + ", ".join(f"{m}={n}" for m, n in by_model_err.most_common())
              + ". See `panel_errors.jsonl`.", ""]
    cost = top.get("cost", {})
    if cost:
        L += [
            f"**Cost:** ${cost.get('total_usd', 0):.4f} total  ·  "
            f"{cost.get('calls', 0)} calls  ·  "
            f"{cost.get('prompt_tokens', 0)}+{cost.get('completion_tokens', 0)} tok"
            + (("  ·  by model: " + ", ".join(f"{m}=${c:.4f}"
               for m, c in cost.get("by_model", {}).items())) if cost.get("by_model") else ""),
            "",
        ]

    # per-design x model descriptive scores (0-100 scalar goodness)
    L += ["## Descriptive scores — mean scalar-goodness × 100 (PRE-GATE)",
          "",
          "| design | " + " | ".join(suts) + " | spread |",
          "|--------|" + "|".join(["------:"] * len(suts)) + "|-------:|"]
    for d in sorted(top["cells"]):
        row = [d]
        mm = top["cells"][d]
        for s in suts:
            row.append(f"{mm[s]['score_0_100']:.1f}" if s in mm else "—")
        row.append(f"{top['design_spread'][d]['spread_points']:.1f}")
        L.append("| " + " | ".join(row) + " |")
    L += ["",
          "> Spread = best−worst SUT (points). This is the **§3 spread-gate INPUT**, "
          "not a pass/fail — gate adjudication is the (Fable) O5 session's job.",
          ""]

    # judge-pair comparison — the headline O4-prep validity surface
    L += ["## Judge-pair agreement (cross-family; disagreements logged, never averaged)",
          "",
          f"**Overall agreement:** {top['judge_pair']['overall_agreement']:.2f}  ·  "
          f"**disagreement cells:** {top['judge_pair']['total_disagreement_cells']}",
          "",
          "| design | judge agreement |",
          "|--------|----------------:|"]
    for d, a in top["judge_pair"]["by_design"].items():
        L.append(f"| {d} | {a:.2f} |")
    L += ["",
          "> Low agreement on a design foreshadows the **§3.4 judge-validity gate**: "
          "judges are not interchangeable, so scores there are not trustworthy until "
          "validated against the human-label sample. Refusal-tag / keyed-outcome is "
          "still taken from `verdicts[0]` (PR-3, parked — not patched).",
          "",
          "## Refusal accounting (four-way taxonomy, whole run)",
          ""]
    for k, v in Counter(top["refusal_accounting"]).most_common():
        L.append(f"- **{k}**: {v}")
    L += ["",
          "## Artifacts",
          "- `manifest.json` — item IDs (subset) only, SUT list, cross-family judge pair, "
          "fixed permutation seeds, pinned capability battery.",
          "- `panel_summary.json` — machine-readable cells + spread + judge-pair + cost.",
          "- `scored_items.jsonl` — one record per (item × model); the resumable checkpoint "
          "(gitignored, regenerable).",
          ""]
    return "\n".join(L)


# --------------------------------------------------------------------------- #
# live wiring (OpenRouter measurement path) — CLI entrypoint only
# --------------------------------------------------------------------------- #
def _build_openrouter(sut_slugs, judge1, judge2, classifier_slug, key, transport):
    from .live_judges import CLIJudge, make_cli_state_classifier
    from .references import bank_reference_provider
    from . import openrouter_backend as orb
    mk = lambda m: orb.OpenRouterClient(m, model=m, api_key=key, transport=transport)
    suts = [mk(s) for s in sut_slugs]
    # judges carry the reference provider so 06/09 are scored against the bank anchors
    # (previously unanchored). families auto-derive from slug.
    judges = [CLIJudge(f"or:{judge1}", mk(judge1), reference_provider=bank_reference_provider),
              CLIJudge(f"or:{judge2}", mk(judge2), reference_provider=bank_reference_provider)]
    classifier = make_cli_state_classifier(mk(classifier_slug))
    return suts, judges, classifier


def main(argv=None):
    from .smoke import _cost_tracking_transport
    ap = argparse.ArgumentParser(description="WALKWORTHY multi-model PANEL runner (OpenRouter)")
    ap.add_argument("--benchmark-root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--out", default=None, help="output dir (default runs/<panel>/)")
    ap.add_argument("--date", default=None)
    ap.add_argument("--panel", default=None, help="panel name (default <date>-p0-pilot)")
    ap.add_argument("--kind", default="p0-pilot")
    ap.add_argument("--designs", default=None, help="comma-separated design ids (default: all 10)")
    ap.add_argument("--items-per-design", type=int, default=5,
                    help="N items/design (P0 pilot=5; 0/negative = full split)")
    ap.add_argument("--no-resume", action="store_true", help="ignore any existing checkpoint")
    # SUT panel: cross-vendor slugs. Judges default to NON-anthropic (item generator was
    # Claude) + cross-family with each other (charter §6.5).
    ap.add_argument("--sut-models", required=True,
                    help="comma-separated OpenRouter SUT slugs (e.g. small,mid,frontier)")
    ap.add_argument("--judge1-model", default="openai/gpt-5.6-terra")
    ap.add_argument("--judge2-model", default="google/gemini-3.5-flash")
    ap.add_argument("--classifier-model", default="openai/gpt-5.6-terra")
    args = ap.parse_args(argv)

    from . import openrouter_backend as orb
    root = Path(args.benchmark_root)
    date_str = args.date or date.today().strftime("%Y%m%d")
    panel = args.panel or f"{date_str}-p0-pilot"
    out = Path(args.out) if args.out else root / "runs" / panel
    designs = args.designs.split(",") if args.designs else None
    ipd = args.items_per_design if args.items_per_design and args.items_per_design > 0 else None
    sut_slugs = [s.strip() for s in args.sut_models.split(",") if s.strip()]

    key = orb.load_openrouter_key()
    if not key:
        raise SystemExit("panel: no OpenRouter key (set OPENROUTER_API_KEY or the secrets file)")
    tr = _cost_tracking_transport()
    suts, judges, classifier = _build_openrouter(
        sut_slugs, args.judge1_model, args.judge2_model, args.classifier_model, key, tr)

    def progress(model, item_id, n):
        print(f"  [{n}] {model}  {item_id}", flush=True)

    top = run_panel(str(root), out, suts, judges, classifier,
                    items_per_design=ipd, designs=designs, date_str=date_str,
                    panel=panel, kind=args.kind, resume=not args.no_resume,
                    cost_probe=lambda: dict(tr.acc), adapter="openrouter", progress=progress)

    print(f"[panel] {top['n_records']} records ({top['n_new_records']} new), "
          f"{top['total_schema_errors']} schema errors, "
          f"{len(top['defects']['judge'])} judge defects, "
          f"{len(top['defects']['classifier'])} classifier defects")
    print(f"[panel] judge agreement (overall): {top['judge_pair']['overall_agreement']:.2f}")
    print(f"[panel] cost: ${top['cost']['total_usd']:.4f} "
          f"({top['cost']['calls']} calls, "
          f"{top['cost']['prompt_tokens']}+{top['cost']['completion_tokens']} tok)")
    print(f"[panel] -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
