"""O3 mechanics-SMOKE driver.

Runs a SMALL live slice (one item across each structurally-distinct design) to prove
— on REAL model output — that the whole pipeline works end to end: prompt rendering,
four-way refusal tagging, the strict 05 allocation parser + one-retry, judge JSON
verdict parsing, judge-backed 02/07 branch selection, and per-seat scoring.

It is NOT the §1 P0 pilot (3 models × 5 items/design) and NOT the O4 panel — those
need the sanctioned Developer-Platform API on both vendors. Every number here is
"smoke, not a measurement." The driver REUSES the already-tested, client-agnostic
pipeline functions (execute_item / score_item / _run_05_allocation / build_manifest);
only the clients + judges + classifier are swapped to live CLI backends.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import List, Optional

from .cli_backends import ClaudeCLIClient, CodexCLIClient, _default_runner
from .executors import execute_item
from .live_judges import CLIJudge, make_cli_state_classifier
from .loader import load_public_split
from .manifest import build_manifest
from .rubrics import spec_for
from .run import _run_05_allocation, score_item

# one per structural family: single-turn/item, allocation, scripted per-turn, paired per-seat
DEFAULT_DESIGN_PICKS = ["01-goodsamaritan", "05-ordoamoris",
                        "07-seventyseven", "09-doubleedge"]


def _admin_cost(item) -> int:
    return sum(len(a.turns) + (1 if a.terminal_ask else 0) for a in item.administrations)


def build_smoke_slice(all_items, design_picks: List[str]) -> list:
    """Pick the cheapest (fewest-call) runnable item for each present design pick."""
    by_design: dict = {}
    for it in all_items:
        by_design.setdefault(it.design, []).append(it)
    out = []
    for d in design_picks:
        pool = by_design.get(d, [])
        if pool:
            out.append(sorted(pool, key=_admin_cost)[0])
    return out


def _item_mechanics(item, execution, record, allocation) -> dict:
    spec = spec_for(item.design)
    branch_states = []
    for ar in execution.administrations:
        for t in ar.turns:
            if getattr(t, "branch_state", None) is not None:
                branch_states.append({"admin": ar.label, "turn": t.index,
                                      "state": t.branch_state})
    m = {
        "item_id": item.id,
        "design": item.design,
        "unit": spec.unit,
        "n_admins": len(execution.administrations),
        "order": execution.order,
        "isolation_used": execution.isolation_used,
        "refusal_tag": record.get("refusal_tag"),
        "refusal_tags": record.get("refusal_tags"),
        "schema_errors": record.get("schema_errors", []),
        "judge_agreement_rate": record["judge_report"]["agreement_rate"],
        "judge_disagreements": len(record["judge_report"]["disagreements"]),
        "judge_families": [v["family"] for v in record["judge_report"]["verdicts"]],
    }
    if branch_states:
        m["branch_states"] = branch_states
    if allocation is not None:
        m["allocation"] = allocation
    return m


def run_smoke(benchmark_root, out_dir, sut_client, judges, state_classifier,
              design_picks: Optional[List[str]] = None, all_items=None,
              date_str: Optional[str] = None, panel: Optional[str] = None,
              write_records: bool = True, extra: Optional[dict] = None) -> dict:
    date_str = date_str or date.today().strftime("%Y%m%d")
    panel = panel or f"{date_str}-o3-smoke"
    design_picks = design_picks or DEFAULT_DESIGN_PICKS
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    if all_items is None:
        # PUBLIC split only; loader HARD-REFUSES HOLDOUT (charter §6.6).
        all_items = load_public_split(benchmark_root, include_exemplars=True,
                                      runnable_only=True)
    slice_items = build_smoke_slice(all_items, design_picks)

    manifest = build_manifest(
        panel=panel, date_str=date_str, benchmark_root=benchmark_root,
        models=[{"name": sut_client.name, "family": sut_client.family, "adapter": "cli"}],
        judges=[{"name": j.name, "family": j.family} for j in judges],
        notes="O3 mechanics smoke (subscription-CLI live calls; NOT a measurement).",
    )
    manifest.write(out / "manifest.json")
    seeds = manifest.permutation_seeds

    records: list = []
    mechanics: list = []
    for item in slice_items:
        allocation = None
        if item.design.startswith("05"):
            allocation, _ = _run_05_allocation(item, sut_client)
        ex = execute_item(item, sut_client, seeds, state_classifier=state_classifier)
        rec = score_item(item, ex, judges, allocation=allocation)
        records.append(rec)
        mechanics.append(_item_mechanics(item, ex, rec, allocation))

    judge_defects: list = []
    for j in judges:
        judge_defects.extend(getattr(j, "defects", []))
    classifier_defects = list(getattr(state_classifier, "defects", []))

    top = {
        "panel": panel,
        "date": date_str,
        "kind": "o3-mechanics-smoke",
        "disclaimer": "SMOKE, not a measurement. Subscription-CLI live calls; "
                      "the full P0 pilot + O4 panel need the sanctioned API on both vendors.",
        "design_picks": design_picks,
        "sut": {"name": sut_client.name, "family": sut_client.family},
        "judges": [{"name": j.name, "family": j.family} for j in judges],
        "n_items": len(slice_items),
        "n_records": len(records),
        "total_schema_errors": sum(len(r.get("schema_errors", [])) for r in records),
        "mechanics": mechanics,
        "defects": {"judge": judge_defects, "classifier": classifier_defects},
    }
    if extra:
        top.update(extra)

    (out / "smoke_summary.json").write_text(json.dumps(top, indent=2), encoding="utf-8")
    if write_records:
        with (out / "scored_items.jsonl").open("w", encoding="utf-8") as fh:
            for r in records:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    (out / "smoke_report.md").write_text(_render_smoke_report(top), encoding="utf-8")
    return top


def _render_smoke_report(top: dict) -> str:
    L = ["# WALKWORTHY O3 — mechanics smoke (auto-render)",
         "",
         "<!-- WALKWORTHY-CANARY-7f3e2026 -->",
         f"> **{top['disclaimer']}**",
         "",
         f"**Panel:** `{top['panel']}`  ·  **SUT:** {top['sut']['name']} "
         f"({top['sut']['family']})  ·  **Judges:** "
         + ", ".join(f"{j['name']}/{j['family']}" for j in top["judges"]),
         "",
         f"Items: {top['n_items']}  ·  records: {top['n_records']}  ·  "
         f"schema errors: {top['total_schema_errors']}  ·  "
         f"judge defects: {len(top['defects']['judge'])}  ·  "
         f"classifier defects: {len(top['defects']['classifier'])}",
         "",
         "## Per-item mechanics",
         "",
         "| item | design | unit | refusal_tag | judge agree | disagr | branch states | alloc ok |",
         "|------|--------|------|-------------|------------:|-------:|---------------|----------|"]
    for m in top["mechanics"]:
        bs = ("; ".join(f"{b['admin']}#{b['turn']}={b['state']}" for b in m["branch_states"])
              if m.get("branch_states") else "—")
        alloc = m.get("allocation")
        alloc_s = ("—" if alloc is None
                   else f"ok={alloc.get('ok')} nc={alloc.get('non_compliant')} "
                        f"att={alloc.get('attempts')}")
        L.append(f"| {m['item_id']} | {m['design']} | {m['unit']} | {m['refusal_tag']} | "
                 f"{m['judge_agreement_rate']:.2f} | {m['judge_disagreements']} | {bs} | {alloc_s} |")
    return "\n".join(L)


# --------------------------------------------------------------------------- #
# live wiring (subscription CLIs) — only used from the CLI entrypoint
# --------------------------------------------------------------------------- #
def _counting_runner():
    state = {"n": 0}

    def runner(argv, timeout=None):
        state["n"] += 1
        return _default_runner(argv, timeout=timeout)

    runner.state = state
    return runner


def main(argv=None):
    ap = argparse.ArgumentParser(description="WALKWORTHY O3 mechanics smoke (LIVE CLI calls)")
    ap.add_argument("--benchmark-root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--out", default=None)
    ap.add_argument("--sut-model", default="sonnet", help="claude -p model for the SUT")
    ap.add_argument("--judge-model", default="sonnet", help="claude -p model for the Claude judge")
    ap.add_argument("--codex-model", default=None, help="codex -m model (default = account default)")
    ap.add_argument("--date", default=None)
    ap.add_argument("--panel", default=None, help="panel name (default <date>-o3-smoke)")
    ap.add_argument("--designs", default=None, help="comma-separated design ids (default: 4-family slice)")
    args = ap.parse_args(argv)

    root = Path(args.benchmark_root)
    date_str = args.date or date.today().strftime("%Y%m%d")
    panel = args.panel or f"{date_str}-o3-smoke"
    out = Path(args.out) if args.out else root / "runs" / panel
    picks = args.designs.split(",") if args.designs else DEFAULT_DESIGN_PICKS

    sut_r, jc_r, cx_r, cls_r = (_counting_runner() for _ in range(4))
    sut = ClaudeCLIClient(f"claude:{args.sut_model}@cli", model=args.sut_model, runner=sut_r)
    judges = [
        CLIJudge(f"claude:{args.judge_model}@cli-judge",
                 ClaudeCLIClient("claude-judge", model=args.judge_model, runner=jc_r),
                 family="anthropic"),
        CLIJudge("codex@cli-judge",
                 CodexCLIClient("codex-judge", model=args.codex_model, runner=cx_r),
                 family="openai"),
    ]
    classifier = make_cli_state_classifier(
        ClaudeCLIClient("claude-classifier", model=args.judge_model, runner=cls_r))

    top = run_smoke(str(root), out, sut, judges, classifier, design_picks=picks,
                    date_str=date_str, panel=panel)

    counts = {"sut": sut_r.state["n"], "claude_judge": jc_r.state["n"],
              "codex_judge": cx_r.state["n"], "classifier": cls_r.state["n"]}
    counts["total"] = sum(counts.values())
    top["call_counts"] = counts
    (out / "smoke_summary.json").write_text(json.dumps(top, indent=2), encoding="utf-8")

    print(f"[o3-smoke] {top['n_records']} records, "
          f"{top['total_schema_errors']} schema errors, "
          f"{len(top['defects']['judge'])} judge defects, "
          f"{len(top['defects']['classifier'])} classifier defects")
    print(f"[o3-smoke] live calls: {counts}")
    print(f"[o3-smoke] -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
