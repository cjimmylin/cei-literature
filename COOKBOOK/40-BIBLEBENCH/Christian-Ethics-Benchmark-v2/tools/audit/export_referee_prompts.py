"""Export the EXACT judge prompts shipped for designs 02, 07 (per-turn) and 06 (single-turn).

WALKWORTHY-CANARY-7f3e2026

Offline reassembly ONLY — ZERO network calls, no SUT re-run, no judge re-run. This tool
reads the stored Part-1 `.eval` pilot logs (inspect_ai.log API) and re-assembles the
SHIPPED judge prompt for every judgeable unit, then emits one JSONL row per unit carrying
the full prompt string and its sha256. The point is byte-fidelity: the prompt text must be
IDENTICAL to what the shipped judges saw, so we REUSE the single assembly surface
`walkworthy_inspect.scorers.assemble_rubric_prompt(meta, spec, response_text, categories,
unit_label=...)` — the same function the live judge pass, rescore.py, judge_ablation.py and
judge_context_ablation.py all call. No prompt assembly is forked here.

SHIPPED-variant settings (what the deployed judges actually saw):
  * Design 02 (per-turn, two-masters): UN-anchored ships (spec_for("02").reference_anchored
    is False). We call the assembler with NO arm patch — mirrors judge_ablation.py's dry-run
    loop with the arm ablation removed (the SHIPPED baseline). One prompt per store
    "ww_turns" entry, unit_label="turn {i}".
  * Design 07 (per-turn, seventy-seven): reference-anchored ships (state anchors emitted).
    We call the assembler WITHOUT judge_context_ablation.py's context_patch — i.e.
    context-FREE, the shipped per-turn baseline. One prompt per "ww_turns" entry,
    unit_label="turn {i}".
  * Design 06 (single-turn, crooked-path): one prompt per stored completion, assembled
    exactly as rescore.py's inner loop:
    assemble_rubric_prompt(meta, spec_for("06"), s.output.completion, judge_categories(spec)).

The sha256 custody pattern is copied from judge_certify.py::_prompt_sha256
(sha256 of prompt.encode("utf-8")).

Data gotchas (all documented in the sibling audit tools):
  * sample_ids COLLIDE across SUTs (same items) — every row is scoped by
    (sut, log basename, sample_id); turn_index is positional in "ww_turns".
  * Design 02/07 turn_states inside Score.value is a JSON-encoded string, but we do NOT
    need it: we read the raw decoded store list "ww_turns" (inspect_ai.log already decodes
    the store), exactly like the per-turn re-judge loops.
  * Design 06 completions come from s.output.completion.

Output row shape (one JSON line per judgeable unit):
  {"sut","log","sample_id","item_id","admin","design","turn_index","prompt_sha256","prompt"}
  - turn_index is an int for 02/07 (positional in ww_turns), null for 06.
  - "design" is the numeric prefix ("02"|"07"|"06"), per spec.

Usage (produce all three JSONLs):
    .venv/bin/python tools/audit/export_referee_prompts.py

    # second determinism run into a temp subdir:
    .venv/bin/python tools/audit/export_referee_prompts.py \
        --out-dir logs/jr-referee-20260716/determinism-check
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# import walkworthy_inspect as a PACKAGE (v2 root on sys.path) so the scorer's relative
# imports resolve and prompt assembly is IDENTICAL to the shipped judge pass.
_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402

from walkworthy_inspect.rubrics import judge_categories, spec_for  # noqa: E402
from walkworthy_inspect.scorers import assemble_rubric_prompt  # noqa: E402

# designs this exporter covers -> per-turn (True) or single-turn (False).
# 02 ships un-anchored, 07 ships reference-anchored; BOTH are shipped context-FREE per-turn
# (no arm patch, no context_patch), so the plain assembler call IS the shipped prompt.
_DESIGNS = {"02": True, "07": True, "06": False}


def _design_num(meta: dict) -> str:
    """Numeric design prefix (mirrors the sibling audit tools' _design_num)."""
    d = str(meta.get("design", ""))
    return d.split("-", 1)[0].zfill(2) if d else "??"


def _prompt_sha256(prompt: str) -> str:
    """sha256 of the prompt text (copied from judge_certify.py::_prompt_sha256)."""
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def _sut_dirs(pilot_dir: str) -> List[str]:
    """SUT subdirs that actually contain .eval logs (mirrors the sibling tools)."""
    return sorted(d for d in glob.glob(os.path.join(pilot_dir, "*/"))
                  if glob.glob(os.path.join(d, "*.eval")))


def _assemble_units(sut_name: str, log_name: str, s) -> List[Dict[str, Any]]:
    """Assemble every judgeable unit for one stored sample, SHIPPED-variant.

    Returns a list of export rows (empty if the sample is out of scope / has no turns).
    Prompt assembly REUSES assemble_rubric_prompt verbatim — no fork, no arm patch.
    """
    meta = s.metadata or {}
    dnum = _design_num(meta)
    if dnum not in _DESIGNS:
        return []
    spec = spec_for(dnum)
    cats = judge_categories(spec)
    rows: List[Dict[str, Any]] = []

    def _mk(prompt: str, turn_index: Optional[int]) -> Dict[str, Any]:
        return {
            "sut": sut_name,
            "log": log_name,
            "sample_id": s.id,
            "item_id": meta.get("item_id"),
            "admin": meta.get("admin"),
            "design": dnum,
            "turn_index": turn_index,
            "prompt_sha256": _prompt_sha256(prompt),
            "prompt": prompt,
        }

    if _DESIGNS[dnum]:  # per-turn (02, 07)
        # mirrors rescore.py / judge_ablation.py per-turn loop: one prompt per ww_turns
        # entry, response ONLY, unit_label="turn {i}". SHIPPED = no anchor/context patch.
        turns = (s.store or {}).get("ww_turns") or []
        for i, t in enumerate(turns):
            resp = (t or {}).get("response", "") or "(empty)"
            prompt = assemble_rubric_prompt(meta, spec, resp, cats, unit_label=f"turn {i}")
            rows.append(_mk(prompt, i))
    else:  # single-turn (06)
        # mirrors rescore.py: assemble_rubric_prompt(meta, spec_for("06"),
        # s.output.completion, judge_categories(spec)) — turn_index is null.
        completion = s.output.completion if s.output else ""
        prompt = assemble_rubric_prompt(meta, spec, completion, cats)
        rows.append(_mk(prompt, None))
    return rows


def export(pilot_dir: str, out_dir: str) -> Dict[str, Any]:
    """Export prompts-02/07/06.jsonl into out_dir. Returns a summary dict for reporting."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    rows_by_design: Dict[str, List[Dict[str, Any]]] = {d: [] for d in _DESIGNS}
    # counts[design][sut] = n_rows ; also track samples with no turns (skips)
    counts: Dict[str, Dict[str, int]] = {d: {} for d in _DESIGNS}
    skipped: List[Dict[str, Any]] = []
    samples_by_design: Dict[str, Dict[str, int]] = {d: {} for d in _DESIGNS}

    for sut_dir in _sut_dirs(pilot_dir):
        sut_name = Path(sut_dir.rstrip("/")).name
        for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
            log_name = Path(p).name
            # cheap design pre-filter on the filename (only read logs we cover)
            if not any(f"design{d}" in log_name for d in _DESIGNS):
                continue
            log = read_eval_log(p)
            for s in (log.samples or []):
                meta = s.metadata or {}
                dnum = _design_num(meta)
                if dnum not in _DESIGNS:
                    continue
                samples_by_design[dnum][sut_name] = \
                    samples_by_design[dnum].get(sut_name, 0) + 1
                units = _assemble_units(sut_name, log_name, s)
                if not units:
                    # per-turn sample with empty/absent ww_turns -> nothing judgeable
                    skipped.append({
                        "sut": sut_name, "log": log_name, "sample_id": s.id,
                        "design": dnum, "reason": "no ww_turns (empty/absent per-turn store)",
                    })
                    continue
                rows_by_design[dnum].extend(units)
                counts[dnum][sut_name] = counts[dnum].get(sut_name, 0) + len(units)

    written: Dict[str, str] = {}
    for dnum, rows in rows_by_design.items():
        path = out / f"prompts-{dnum}.jsonl"
        with path.open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        written[dnum] = str(path)

    return {
        "out_dir": str(out),
        "written": written,
        "counts": counts,                # design -> sut -> n rows
        "samples_by_design": samples_by_design,  # design -> sut -> n samples
        "totals": {d: len(rows_by_design[d]) for d in _DESIGNS},
        "skipped": skipped,
    }


def _print_summary(summary: Dict[str, Any]) -> None:
    print(f"=== export_referee_prompts  out_dir={summary['out_dir']} ===")
    for dnum in _DESIGNS:
        per_sut = summary["counts"][dnum]
        total = summary["totals"][dnum]
        detail = ", ".join(f"{k}={v}" for k, v in sorted(per_sut.items()))
        print(f"  design {dnum}: {total:5} rows  [{detail}]  -> "
              f"{Path(summary['written'][dnum]).name}")
    if summary["skipped"]:
        print(f"  SKIPPED {len(summary['skipped'])} samples "
              f"(no judgeable units):")
        for sk in summary["skipped"][:20]:
            print(f"    {sk['sut']}/{sk['log']} sample={sk['sample_id']} "
                  f"design={sk['design']}: {sk['reason']}")
    else:
        print("  SKIPPED 0 samples")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Export SHIPPED judge prompts for designs 02/07 (per-turn) & 06 "
                    "(single-turn) from stored pilot logs. ZERO network calls.")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ap.add_argument("--out-dir", default="logs/jr-referee-20260716",
                    help="output dir for prompts-{02,07,06}.jsonl")
    args = ap.parse_args()
    summary = export(args.pilot_dir, args.out_dir)
    _print_summary(summary)


if __name__ == "__main__":
    main()
