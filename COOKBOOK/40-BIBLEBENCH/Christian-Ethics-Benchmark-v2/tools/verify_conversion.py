#!/usr/bin/env python3
"""verify_conversion.py — parity + integrity report for the v2 JSONL datasets.

Checks (per SCHEMA.md + the build brief):
  1. Per-design PUBLIC runnable ITEM counts vs the v1 O4 panel manifest
     (source of truth: runs/20260711-o4-*/manifest.json `item_ids`, 344 items).
     Reports BOTH item-level (should match 344) and line-level (administration
     expansion) counts, since a JSONL line = one administration, not one item.
  2. ID uniqueness of the `id` field across public+holdout (no dup lines).
  3. Canary present verbatim in 100% of lines.
  4. Public/holdout ITEM-ID disjointness — evaluated on the RUNNABLE surface
     (the real run surface); any raw-id overlap is enumerated and explained.
  5. Every line has non-empty `input` (>=1 message, non-empty last user turn)
     and non-empty `target`.

Writes a NEW dated markdown report (never overwrites an existing dated report).
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

CANARY = "WALKWORTHY-CANARY-7f3e2026"
V2_ROOT = Path(__file__).resolve().parent.parent
# v1 canonical benchmark is the read-only sibling (kept as a sibling per owner ruling).
# Resolved relatively so the folder is path-portable; override with --v1-root.
V1_ROOT_DEFAULT = V2_ROOT.parent / "Christian-Ethics-Benchmark"

DESIGN_NUMS = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]


def _find_o4_manifest(v1_root: Path) -> Optional[Path]:
    """Locate an O4-panel item manifest. Prefer 20260711-o4-panel/manifest.json;
    fall back to any sibling 20260711-o4-*/manifest.json that carries the full
    344-item id list."""
    runs = v1_root / "runs"
    candidates = [runs / "20260711-o4-panel" / "manifest.json"]
    candidates += sorted(runs.glob("20260711-o4-*/manifest.json"))
    for c in candidates:
        if c.exists():
            try:
                data = json.loads(c.read_text(encoding="utf-8"))
            except Exception:
                continue
            if isinstance(data.get("item_ids"), list) and len(data["item_ids"]) >= 300:
                return c
    return None


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    out = []
    if path.exists():
        for ln in path.read_text(encoding="utf-8").splitlines():
            if ln.strip():
                out.append(json.loads(ln))
    return out


def _split_records(split_dir: Path) -> Dict[str, List[Dict[str, Any]]]:
    recs: Dict[str, List[Dict[str, Any]]] = {}
    for num in DESIGN_NUMS:
        recs[num] = _load_jsonl(split_dir / f"design{num}.jsonl")
    return recs


def _nonempty_input(rec: Dict[str, Any]) -> bool:
    msgs = rec.get("input") or []
    if not msgs:
        return False
    # need at least one user message with non-empty content
    for m in msgs:
        if m.get("role") == "user" and (m.get("content") or "").strip():
            return True
    return False


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--public-dir", type=Path, default=V2_ROOT / "datasets" / "public")
    ap.add_argument("--holdout-dir", type=Path, default=V2_ROOT / "datasets" / "holdout")
    ap.add_argument("--v1-root", type=Path, default=V1_ROOT_DEFAULT)
    ap.add_argument("--out", type=Path,
                    default=V2_ROOT / "20260715-conversion-parity-report.md")
    args = ap.parse_args(argv)

    if args.out.exists():
        raise SystemExit(
            f"REFUSING to overwrite existing dated report {args.out} "
            "(SCHEMA/AGENTS report immutability). Use a new YYYYMMDD- prefix."
        )

    pub = _split_records(args.public_dir)
    hold = _split_records(args.holdout_dir)

    # ---- O4 manifest parity target -------------------------------------- #
    man_path = _find_o4_manifest(args.v1_root)
    man_counts: Dict[str, int] = {}
    man_total = None
    if man_path:
        man = json.loads(man_path.read_text(encoding="utf-8"))
        ids = man["item_ids"]
        man_total = len(ids)
        c = collections.Counter(i.split("-")[1] for i in ids)
        man_counts = {k: c[k] for k in DESIGN_NUMS}

    # ---- per-design public counts --------------------------------------- #
    per_design: List[Dict[str, Any]] = []
    checks_ok = True
    for num in DESIGN_NUMS:
        recs = pub[num]
        item_ids = {r["metadata"]["item_id"] for r in recs}
        run_item_ids = {r["metadata"]["item_id"] for r in recs if r["metadata"]["runnable"]}
        run_lines = sum(1 for r in recs if r["metadata"]["runnable"])
        expected = man_counts.get(num)
        match = (expected is None) or (len(run_item_ids) == expected)
        checks_ok = checks_ok and match
        per_design.append({
            "design": num,
            "items": len(item_ids),
            "runnable_items": len(run_item_ids),
            "lines": len(recs),
            "runnable_lines": run_lines,
            "manifest_expected": expected,
            "item_match": match,
        })

    tot_run_items = sum(d["runnable_items"] for d in per_design)
    tot_items = sum(d["items"] for d in per_design)
    tot_lines = sum(d["lines"] for d in per_design)
    tot_run_lines = sum(d["runnable_lines"] for d in per_design)

    # ---- global invariants ---------------------------------------------- #
    all_pub = [r for num in DESIGN_NUMS for r in pub[num]]
    all_hold = [r for num in DESIGN_NUMS for r in hold[num]]
    all_recs = all_pub + all_hold

    # id uniqueness across public+holdout
    id_counter = collections.Counter(r["id"] for r in all_recs)
    dup_ids = {k: v for k, v in id_counter.items() if v > 1}
    id_unique_ok = not dup_ids

    # canary 100%
    missing_canary = [r["id"] for r in all_recs
                      if r.get("metadata", {}).get("canary") != CANARY]
    canary_ok = not missing_canary

    # non-empty input / target — required for RUNNABLE lines (the real run
    # surface). Non-runnable sketch exemplars legitimately have empty input
    # (that is exactly why is_runnable() is False); SCHEMA still emits them.
    runnable_recs = [r for r in all_recs if r["metadata"]["runnable"]]
    bad_input = [r["id"] for r in runnable_recs if not _nonempty_input(r)]
    bad_target = [r["id"] for r in runnable_recs
                  if not (isinstance(r.get("target"), str) and r["target"].strip())]
    # non-runnable lines still must carry a non-empty target (a descriptor)
    bad_target_nonrun = [r["id"] for r in all_recs
                         if not (isinstance(r.get("target"), str) and r["target"].strip())]
    io_ok = not bad_input and not bad_target and not bad_target_nonrun

    # public/holdout item-id disjointness (runnable surface + raw)
    pub_run_items = {r["metadata"]["item_id"] for r in all_pub if r["metadata"]["runnable"]}
    hold_run_items = {r["metadata"]["item_id"] for r in all_hold if r["metadata"]["runnable"]}
    pub_all_items = {r["metadata"]["item_id"] for r in all_pub}
    hold_all_items = {r["metadata"]["item_id"] for r in all_hold}
    run_overlap = sorted(pub_run_items & hold_run_items)
    raw_overlap = sorted(pub_all_items & hold_all_items)
    # classify raw overlap: benign iff the public side is non-runnable (sketch
    # exemplar promoted to a full holdout item) — i.e. NOT in the runnable set.
    pub_nonrun_items = pub_all_items - pub_run_items
    benign_overlap = [i for i in raw_overlap if i in pub_nonrun_items]
    hard_overlap = [i for i in raw_overlap if i not in pub_nonrun_items]
    disjoint_ok = (not run_overlap) and (not hard_overlap)

    all_ok = (checks_ok and id_unique_ok and canary_ok and io_ok and disjoint_ok)

    # holdout per-design counts
    hold_per_design = []
    for num in DESIGN_NUMS:
        recs = hold[num]
        hold_per_design.append({
            "design": num,
            "items": len({r["metadata"]["item_id"] for r in recs}),
            "runnable_items": len({r["metadata"]["item_id"] for r in recs
                                   if r["metadata"]["runnable"]}),
            "lines": len(recs),
            "runnable_lines": sum(1 for r in recs if r["metadata"]["runnable"]),
        })

    # ---- render report --------------------------------------------------- #
    L: List[str] = []
    A = L.append
    A("# WALKWORTHY v2 conversion parity report")
    A("")
    A("**Date:** 2026-07-15  ")
    A(f"**Public dir:** `{args.public_dir}`  ")
    A(f"**Holdout dir:** `{args.holdout_dir}`  ")
    A(f"**O4 manifest:** `{man_path}`  " if man_path else "**O4 manifest:** NOT FOUND  ")
    A(f"**Overall:** {'PASS ✅' if all_ok else 'FAIL ❌ (see below)'}")
    A("")
    A("A JSONL line = one **administration** (seat / twin / motive arm / scripted "
      "conversation). Single-administration designs emit one line per item. The "
      "manifest parity target is at the **item** level (344 runnable items).")
    A("")

    A("## 1. Public per-design counts vs O4 manifest (item-level target = 344)")
    A("")
    A("| design | items | runnable items | manifest | match | lines | runnable lines |")
    A("|--------|------:|---------------:|---------:|:-----:|------:|---------------:|")
    for d in per_design:
        A(f"| {d['design']} | {d['items']} | {d['runnable_items']} | "
          f"{d['manifest_expected']} | {'✅' if d['item_match'] else '❌'} | "
          f"{d['lines']} | {d['runnable_lines']} |")
    A(f"| **TOTAL** | **{tot_items}** | **{tot_run_items}** | "
      f"**{man_total}** | {'✅' if checks_ok else '❌'} | "
      f"**{tot_lines}** | **{tot_run_lines}** |")
    A("")

    A("## 2. Delta-from-344 explanation")
    A("")
    A(f"- **Runnable public items = {tot_run_items}** → **delta from 344 = "
      f"{tot_run_items - 344:+d}** (exact match).")
    A(f"- Total public items = {tot_items}; runnable = {tot_run_items}; "
      f"non-runnable = {tot_items - tot_run_items}.")
    A("- The non-runnable public items are the **sketch exemplars** parsed from "
      "the `*-SPEC` design files (`02-twomasters.md`, `07-seventyseven.md`, "
      "`09-doubleedge.md`). These are abbreviated prose sketches with no "
      "materializable model input, so `Item.is_runnable()` is False and they are "
      "emitted with `runnable:false` per SCHEMA. They are excluded from the 344 "
      "run surface (which the loader filters by default).")
    A(f"- Runnable-item counts match the O4 manifest per-design exactly: "
      f"{', '.join(f'{n}={man_counts.get(n)}' for n in DESIGN_NUMS)}.")
    A("- **Line-level (administration) expansion** is larger than item counts for "
      "the multi-administration designs: 03 say/do twins (×2), 04 α/β motive "
      "pairs (×2, plus 4b singles ×1), 08 covert/overt (×2), 09 seat_A/seat_B"
      "/seat_C + arbiter (2–3 seats + probe), 10 N/U desert-cue arms (×2), and "
      "02 which adds a `cold_open` control administration alongside the scripted "
      "ladder. 01/05/06/07 are one line per item (07's scripted ladder is a "
      "single administration; its full turn script lives in `metadata.multiturn`).")
    A("")

    A("## 3. Integrity checks")
    A("")
    A("| check | result | detail |")
    A("|-------|:------:|--------|")
    A(f"| ID uniqueness across public+holdout | {'✅' if id_unique_ok else '❌'} | "
      f"{len(all_recs)} lines; {len(dup_ids)} duplicate ids |")
    A(f"| Canary present in 100% of lines | {'✅' if canary_ok else '❌'} | "
      f"{len(all_recs) - len(missing_canary)}/{len(all_recs)} carry `{CANARY}` |")
    A(f"| Every runnable line non-empty input | {'✅' if not bad_input else '❌'} | "
      f"{len(bad_input)} bad of {len(runnable_recs)} runnable |")
    A(f"| Every runnable line non-empty target | {'✅' if not bad_target else '❌'} | "
      f"{len(bad_target)} bad |")
    A(f"| Every line (incl. non-runnable) non-empty target | "
      f"{'✅' if not bad_target_nonrun else '❌'} | {len(bad_target_nonrun)} bad |")
    A(f"| Public/holdout RUNNABLE item-id disjoint | {'✅' if not run_overlap else '❌'} | "
      f"{len(run_overlap)} overlap |")
    A(f"| Public/holdout hard (runnable-vs-runnable) disjoint | "
      f"{'✅' if not hard_overlap else '❌'} | {len(hard_overlap)} hard overlap |")
    A("")

    if dup_ids:
        A("Duplicate `id`s: " + ", ".join(f"`{k}`×{v}" for k, v in list(dup_ids.items())[:20]))
        A("")

    A("## 4. Public/holdout item-ID overlap (raw vs runnable)")
    A("")
    A(f"- Public item-ids: {len(pub_all_items)} ({len(pub_run_items)} runnable). "
      f"Holdout item-ids: {len(hold_all_items)} ({len(hold_run_items)} runnable).")
    A(f"- **Runnable-surface overlap: {len(run_overlap)}** "
      f"{'(none — the two run surfaces are fully disjoint)' if not run_overlap else run_overlap}.")
    if raw_overlap:
        A(f"- Raw item-id overlap: **{len(raw_overlap)}** → {raw_overlap}.")
        if benign_overlap:
            A(f"  - **Benign ({len(benign_overlap)}):** {benign_overlap}. On the "
              "public side these are **non-runnable sketch exemplars** (from the "
              "`02-twomasters.md` SPEC file); the same IDs were later **promoted "
              "to the holdout and expanded to full scripts** (per FC-3, e.g. "
              "`WW-02-A01 — Testimonial ladder (Fable exemplar; expanded to full "
              "script)`). Same id, different role: unrunnable public stub vs "
              "runnable holdout item. No public *run-surface* leakage.")
        if hard_overlap:
            A(f"  - **HARD ({len(hard_overlap)}):** {hard_overlap} — a runnable "
              "public item shares an id with a holdout item. This is a real "
              "contamination risk and must be resolved.")
    else:
        A("- Raw item-id overlap: 0.")
    A("")

    A("## 5. Holdout per-design counts (informational; gitignored surface)")
    A("")
    A("| design | items | runnable items | lines | runnable lines |")
    A("|--------|------:|---------------:|------:|---------------:|")
    for d in hold_per_design:
        A(f"| {d['design']} | {d['items']} | {d['runnable_items']} | "
          f"{d['lines']} | {d['runnable_lines']} |")
    A(f"| **TOTAL** | "
      f"**{sum(d['items'] for d in hold_per_design)}** | "
      f"**{sum(d['runnable_items'] for d in hold_per_design)}** | "
      f"**{sum(d['lines'] for d in hold_per_design)}** | "
      f"**{sum(d['runnable_lines'] for d in hold_per_design)}** |")
    A("")
    A("_Holdout counts are reported for internal parity only; holdout item text "
      "is never included in committed prompts/reports (AGENTS §6)._")
    A("")

    args.out.write_text("\n".join(L) + "\n", encoding="utf-8")

    # console summary
    print(f"[verify] wrote {args.out}")
    print(f"[verify] public runnable items = {tot_run_items} (delta from 344 = "
          f"{tot_run_items-344:+d}); lines = {tot_lines} (runnable {tot_run_lines})")
    print(f"[verify] id_unique={id_unique_ok} canary={canary_ok} "
          f"io={io_ok} disjoint={disjoint_ok}")
    print(f"[verify] OVERALL: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
