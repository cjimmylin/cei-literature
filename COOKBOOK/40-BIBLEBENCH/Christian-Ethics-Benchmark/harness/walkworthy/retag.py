"""PR-3 R4 — retroactive refusal re-tag over existing run records (mechanical, no live calls).

The pilot + O3 smokes were tagged by the pre-ruling logic (verdicts[0]-only, no keyed
coupling), so their `unnecessary_refusal` / `policy_violating_compliance` split is
unreadable (pilot report caveat). This re-derives the four-way split under R1/R2 from BOTH
judges and writes it as a NEW dated analysis file — original run records are immutable
(report-immutability rule); this is a derived artifact.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, Tuple

from . import outcomes
from .loader import load_public_split
from .refusal import tag_response


def _item_for(rec: dict, items_by_id: Optional[dict]):
    if items_by_id and rec["item_id"] in items_by_id:
        return items_by_id[rec["item_id"]]
    return SimpleNamespace(id=rec.get("item_id"), design=rec.get("design"),
                           tier=rec.get("tier", "core"), stratum=rec.get("stratum", "a"),
                           key={})


def retag_record(rec: dict, items_by_id: Optional[dict]) -> dict:
    item = _item_for(rec, items_by_id)
    vdicts = (rec.get("judge_report") or {}).get("verdicts", [])
    admins = rec.get("administrations") or [{"label": "main",
                                             "response": rec.get("response")}]
    new_tags, reasons, overrides = {}, {}, {}
    for ar in admins:
        label = ar.get("label", "main")
        txt = ar.get("response") or ar.get("terminal") or ""
        _, engaged, keyed = outcomes.load_bearing_outcome(
            rec["design"], item, vdicts, label, rec.get("allocation"))
        rt = tag_response(txt, item, engaged=engaged, keyed_outcome=keyed)
        new_tags[label] = rt.tag
        reasons[label] = rt.refusal_reason
        overrides[label] = rt.lexical_override
    primary = admins[0].get("label", "main") if admins else "main"
    return {"item_id": rec["item_id"], "design": rec["design"], "model": rec["model"],
            "old_refusal_tag": rec.get("refusal_tag"),
            "new_refusal_tag": new_tags.get(primary),
            "new_refusal_tags": new_tags, "refusal_reason": reasons,
            "lexical_override": overrides}


def retag_run(records: list, items_by_id: Optional[dict]) -> Tuple[list, dict]:
    retagged = [retag_record(r, items_by_id) for r in records]
    old = Counter(r["old_refusal_tag"] for r in retagged)
    new = Counter(r["new_refusal_tag"] for r in retagged)
    reasons = Counter(rr for r in retagged for rr in r["refusal_reason"].values() if rr)
    overrides = sum(1 for r in retagged for ov in r["lexical_override"].values() if ov)
    transitions = Counter((r["old_refusal_tag"], r["new_refusal_tag"]) for r in retagged)
    summary = {"n": len(retagged), "old": dict(old), "new": dict(new),
               "reasons": dict(reasons), "lexical_overrides": overrides,
               "transitions": {f"{a} -> {b}": n for (a, b), n in transitions.most_common()}}
    return retagged, summary


def _load_records(run_dir: Path) -> list:
    fp = run_dir / "scored_items.jsonl"
    if not fp.exists():
        return []
    out = []
    for line in fp.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def _render(all_summaries: dict, date_str: str) -> str:
    L = ["# WALKWORTHY — PR-3 Retroactive Refusal Re-Tag (R4)", "",
         "<!-- WALKWORTHY-CANARY-7f3e2026 -->",
         f"**Generated:** {date_str} (O4-build, mechanical — no live calls).  "
         "**Authority:** `20260710-fable-PR3-ruling.md` R4.",
         "",
         "> Derived analysis over existing (immutable) run records. Legacy records were "
         "scored at item level (pre-per_admin); the load-bearing outcome falls back to "
         "the item-level verdict for the per-admin twin designs, so twin gaps are NOT "
         "re-derived here — only the four-way refusal split is (R4's stated purpose). "
         "`pending_adjudication` = the adjudicated keyed_outcome was unavailable (judge "
         "disagreement / legacy structure), NOT a fifth taxonomy cell.", ""]
    for run, s in all_summaries.items():
        L += [f"## `{run}` — {s['n']} records", "",
              "**Old split (pre-ruling):** " + ", ".join(f"{k}={v}" for k, v in s["old"].items()),
              "", "**New split (R1/R2):** " + ", ".join(f"{k}={v}" for k, v in s["new"].items()),
              "", f"**Refusal reasons:** " + (", ".join(f"{k}={v}" for k, v in s["reasons"].items()) or "—")
              + f"  ·  **lexical overrides (R1):** {s['lexical_overrides']}", "",
              "**Transitions (old → new):**", ""]
        for t, n in s["transitions"].items():
            L.append(f"- {t}: {n}")
        L.append("")
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description="PR-3 R4 retroactive refusal re-tag")
    ap.add_argument("--benchmark-root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--runs", nargs="+", required=True, help="run dir names under runs/")
    ap.add_argument("--out", default=None, help="output report path")
    ap.add_argument("--date", default=None)
    args = ap.parse_args(argv)
    root = Path(args.benchmark_root)
    date_str = args.date or date.today().strftime("%Y%m%d")
    items = {it.id: it for it in load_public_split(str(root), include_exemplars=True,
                                                   runnable_only=False)}
    all_summaries = {}
    for run in args.runs:
        recs = _load_records(root / "runs" / run)
        if not recs:
            all_summaries[run] = {"n": 0, "old": {}, "new": {}, "reasons": {},
                                  "lexical_overrides": 0, "transitions": {}}
            continue
        _, summary = retag_run(recs, items)
        all_summaries[run] = summary
    out = Path(args.out) if args.out else \
        root / "00-PORTFOLIO" / f"{date_str}-pr3-retag-analysis.md"
    out.write_text(_render(all_summaries, date_str), encoding="utf-8")
    print(f"[retag] {sum(s['n'] for s in all_summaries.values())} records over "
          f"{len(all_summaries)} runs -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
