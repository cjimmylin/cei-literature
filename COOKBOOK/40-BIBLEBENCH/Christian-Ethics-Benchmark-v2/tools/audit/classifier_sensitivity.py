"""F3: 02/07 branch-classifier sensitivity over stored pilot logs (20260716 adjudication).

The branch classifier picks which user turn each SUT receives on the 02/07 ladders
(solvers.py::_classify_branch): a classifier MODEL verdict when it maps cleanly to a
branch state ("classifier"), else the v1 lexical heuristic ("heuristic"). In the pilot
the classifier model was judge-A (gpt-4.1-nano, tasks/design02+07: classifier =
judge_model) — the anchor-dependent judge (20260716-f2-ablations-report) is ALSO the
stimulus generator. Cross-harness c2 quantified the blast radius: only 17-19/36
design-07 turn positions received byte-identical stimuli across harnesses
(20260716-crossharness-results §"Quantified confounds").

OFFLINE (free, this tool's default): mine stored `ww_turns` records (M3) from the
pilot logs —
  (a) branch_source distribution per design x SUT,
  (b) lexical-heuristic fallback rate,
  (c) OTHER-ROUTE REPLAY: for every classifier-routed turn, re-classify the stored
      prior response with the v1 lexical heuristic (`_heuristic_branch`, pure code)
      and report the would-have-diverged rate — per turn, and per ladder ("any turn
      diverged" = the whole downstream stimulus chain changes). This is the
      stimulus-instability number the c2 finding predicts.

GATED (spend memo; NOT run by default): --alt-classifier re-classifies the same stored
prior responses with an alternative classifier MODEL via the exact _classify_branch
prompt (classifier-tokens only, ZERO SUT re-runs; pattern = tools/rescore/rescore.py).
--dry-run prints the call/cost estimate for that arm without any model call.

Join discipline: all tallies are scoped per SUT directory / log file — sample_ids
collide across SUTs (the 2026-07-16 ablation_agreement lesson); no cross-SUT joins.

Usage (offline analysis, free):
    .venv/bin/python tools/audit/classifier_sensitivity.py --pilot-dir logs/pilot-20260716

Usage (gated alt-classifier arm, dry-run cost estimate — ZERO model calls):
    .venv/bin/python tools/audit/classifier_sensitivity.py --dry-run \
        --alt-classifier openrouter/mistralai/mistral-small-3.2-24b-instruct \
        --price 0.06,0.18

Usage (gated alt-classifier arm, live — requires explicit owner GO):
    source ~/.codex/secrets/openrouter.env
    .venv/bin/python tools/audit/classifier_sensitivity.py \
        --alt-classifier <slug> --out logs/f3-classifier-20260716/altclass.jsonl
"""
from __future__ import annotations

import argparse
import asyncio
import glob
import json
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402
from inspect_ai.model import GenerateConfig, get_model  # noqa: E402

from walkworthy_inspect.solvers import (  # noqa: E402
    DEFAULT_MAX_TOKENS,
    _heuristic_branch,
    _map_branch,
)

F3_DESIGNS = ("02", "07")


def _design_num(meta: dict) -> str:
    d = str(meta.get("design", ""))
    return d.split("-", 1)[0].zfill(2) if d else "??"


# --------------------------------------------------------------------------- #
# ladder reconstruction: align each branched ww_turns record with its
# metadata.multiturn turn (positional, verified by user_text membership in the
# turn's branches; alignment failures are REPORTED, never silently dropped).
# --------------------------------------------------------------------------- #
def branched_turns(meta: dict, turns_record: List[dict]) -> List[dict]:
    """Yield one row per branched administered turn:
    {rec_index, states, branches, branch_state, branch_source, prior_response,
     user_text, aligned}."""
    mt = meta.get("multiturn") or {}
    turns: List[dict] = (mt.get("turns") or []) if isinstance(mt, dict) else []
    rows = []
    for k, rec in enumerate(turns_record):
        if rec.get("branch_source") is None:
            continue  # opening turn, unbranched turn, or terminal ask
        # positional mapping: record k was produced while walking turns[k]
        # (solvers.py walks turns[1:] and the opening is record 0).
        cand = turns[k] if k < len(turns) and isinstance(turns[k], dict) else {}
        branches = cand.get("branches") or {}
        aligned = bool(branches) and rec.get("user_text") in set(branches.values())
        if not aligned:
            # fallback: first metadata turn whose branches contain this user_text
            for t in turns:
                if isinstance(t, dict) and t.get("branches") and \
                        rec.get("user_text") in set(t["branches"].values()):
                    branches, aligned = t["branches"], True
                    break
        rows.append({
            "rec_index": k,
            "states": list(branches.keys()),
            "branches": branches,
            "branch_state": rec.get("branch_state"),
            "branch_source": rec.get("branch_source"),
            "prior_response": (turns_record[k - 1].get("response", "")
                               if k >= 1 else ""),
            "user_text": rec.get("user_text", ""),
            "aligned": aligned,
        })
    return rows


def _iter_ladder_samples(pilot_dir: str):
    """Yield (sut_name, log_name, sample) for every 02/07 sample, scoped per log."""
    for sut in sorted(glob.glob(os.path.join(pilot_dir, "*/"))):
        sut_name = Path(sut.rstrip("/")).name
        for p in sorted(glob.glob(os.path.join(sut, "*.eval"))):
            stem = Path(p).name
            if not any(f"design{d}" in stem for d in F3_DESIGNS):
                continue
            log = read_eval_log(p)
            for s in (log.samples or []):
                yield sut_name, stem, s


# --------------------------------------------------------------------------- #
# offline analysis (free)
# --------------------------------------------------------------------------- #
def analyze(pilot_dir: str) -> dict:
    cells: Dict[tuple, Dict[str, Any]] = defaultdict(lambda: {
        "n_samples": 0, "n_branched_turns": 0, "n_classifier": 0, "n_heuristic": 0,
        "n_other_source": 0, "n_misaligned": 0,
        "n_replayed": 0, "n_diverged": 0,
        "ladders_with_classifier_turn": 0, "ladders_any_diverged": 0,
        "diverged_transitions": defaultdict(int),
    })
    for sut_name, _log_name, s in _iter_ladder_samples(pilot_dir):
        meta = s.metadata or {}
        dnum = _design_num(meta)
        store = getattr(s, "store", None) or {}
        turns_record = store.get("ww_turns") or []
        if not turns_record:
            continue
        cell = cells[(dnum, sut_name)]
        cell["n_samples"] += 1
        rows = branched_turns(meta, turns_record)
        ladder_has_classifier = False
        ladder_diverged = False
        for row in rows:
            cell["n_branched_turns"] += 1
            src = row["branch_source"]
            if src == "classifier":
                cell["n_classifier"] += 1
            elif src == "heuristic":
                cell["n_heuristic"] += 1
            else:
                cell["n_other_source"] += 1
            if not row["aligned"]:
                cell["n_misaligned"] += 1
                continue
            if src != "classifier":
                continue  # other-route replay of heuristic turns needs a model (gated)
            ladder_has_classifier = True
            other = _heuristic_branch(row["prior_response"], row["states"], dnum)
            cell["n_replayed"] += 1
            if other != row["branch_state"]:
                cell["n_diverged"] += 1
                ladder_diverged = True
                cell["diverged_transitions"][f"{row['branch_state']}->{other}"] += 1
        if ladder_has_classifier:
            cell["ladders_with_classifier_turn"] += 1
            if ladder_diverged:
                cell["ladders_any_diverged"] += 1
    # freeze defaultdicts for JSON
    out = {}
    for (dnum, sut), cell in sorted(cells.items()):
        cell["diverged_transitions"] = dict(cell["diverged_transitions"])
        out[f"{dnum}/{sut}"] = cell
    return out


def print_report(cells: dict) -> None:
    print("=== F3 offline: branch_source distribution + heuristic-replay divergence ===")
    print(f"{'cell':28} {'turns':>5} {'clsf':>5} {'heur':>5} "
          f"{'misal':>5} {'replay':>6} {'diverg':>6} {'rate':>6}  ladders(any-div/clsf)")
    for key, c in cells.items():
        rate = (c["n_diverged"] / c["n_replayed"]) if c["n_replayed"] else float("nan")
        print(f"{key:28} {c['n_branched_turns']:5} {c['n_classifier']:5} "
              f"{c['n_heuristic']:5} {c['n_misaligned']:5} {c['n_replayed']:6} "
              f"{c['n_diverged']:6} {rate:6.3f}  "
              f"{c['ladders_any_diverged']}/{c['ladders_with_classifier_turn']}")
    for key, c in cells.items():
        if c["diverged_transitions"]:
            print(f"  {key} transitions: {c['diverged_transitions']}")


# --------------------------------------------------------------------------- #
# gated alt-classifier arm (spend memo): same stored prior responses, the exact
# _classify_branch prompt, an alternative classifier model. ZERO SUT re-runs.
# --------------------------------------------------------------------------- #
def _classify_prompt(rubric: str, states: List[str], prior_response: str) -> str:
    # byte-identical to solvers.py::_classify_branch prompt assembly
    return (
        f"{rubric}\n\n"
        f"Classify the following response into exactly one of these states: "
        f"{', '.join(states)}.\n"
        f"Reply with only the single state word.\n\n"
        f"RESPONSE:\n{prior_response or '(empty)'}"
    )


def _alt_plan(pilot_dir: str) -> List[dict]:
    """All branched turns (both sources) with their prompts — the alt-classifier scope."""
    plan = []
    for sut_name, log_name, s in _iter_ladder_samples(pilot_dir):
        meta = s.metadata or {}
        dnum = _design_num(meta)
        mt = meta.get("multiturn") or {}
        rubric = (mt.get("classifier_rubric", "") or "") if isinstance(mt, dict) else ""
        branch_table = mt.get("branch_table") if isinstance(mt, dict) else None
        store = getattr(s, "store", None) or {}
        for row in branched_turns(meta, store.get("ww_turns") or []):
            if not row["aligned"]:
                continue
            plan.append({
                "sut": sut_name, "log": log_name, "design": dnum,
                "sample_id": s.id, "item_id": meta.get("item_id"),
                "rec_index": row["rec_index"],
                "states": row["states"],
                "branch_table": branch_table,
                "pilot_state": row["branch_state"],
                "pilot_source": row["branch_source"],
                "prompt": _classify_prompt(rubric, row["states"],
                                           row["prior_response"]),
                "prior_response": row["prior_response"],
            })
    return plan


def dry_run_alt(pilot_dir: str, alt_models: List[str],
                price: Optional[tuple]) -> None:
    plan = _alt_plan(pilot_dir)
    total_chars = sum(len(r["prompt"]) for r in plan)
    est_in = total_chars // 4
    by_cell = defaultdict(int)
    for r in plan:
        by_cell[(r["design"], r["sut"])] += 1
    print("=== DRY RUN alt-classifier arm (ZERO model calls) ===")
    for (d, sut), n in sorted(by_cell.items()):
        print(f"  {d}/{sut:20} calls={n}")
    print(f"  TOTAL calls/model={len(plan)}  est_input_tokens={est_in} (chars/4)")
    for m in alt_models:
        line = f"  {m}: calls={len(plan)}"
        if price:
            pin, pout = price
            est_out = len(plan) * 8  # single state word + slack
            cost = (est_in / 1e6) * pin + (est_out / 1e6) * pout
            line += f"  est_output_tokens={est_out}  EST_COST=${cost:.4f}"
        print(line)


async def run_alt(pilot_dir: str, alt_model: str, out_path: Path,
                  concurrency: int) -> None:
    plan = _alt_plan(pilot_dir)
    model = get_model(alt_model)
    sem = asyncio.Semaphore(concurrency)

    async def _one(row: dict) -> dict:
        async with sem:
            try:
                out = await model.generate(
                    row["prompt"], config=GenerateConfig(max_tokens=DEFAULT_MAX_TOKENS))
                raw = (out.completion or "").strip()
                err = None
            except Exception as exc:  # classifier failure is DATA
                raw, err = "", str(exc)[:200]
        mapped = _map_branch(raw, row["states"], row["branch_table"])
        fell_back = mapped is None
        alt_state = mapped if mapped is not None else _heuristic_branch(
            row["prior_response"], row["states"], row["design"])
        return {k: row[k] for k in ("sut", "log", "design", "sample_id", "item_id",
                                    "rec_index", "pilot_state", "pilot_source")} | {
            "alt_model": alt_model,
            "alt_raw": raw[:120],
            "alt_state": alt_state,
            "alt_fell_back_to_heuristic": fell_back,
            "diverged": alt_state != row["pilot_state"],
            "error": err,
        }

    rows = await asyncio.gather(*[_one(r) for r in plan])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    n_div = sum(r["diverged"] for r in rows)
    print(f"wrote {len(rows)} alt-classifications -> {out_path} "
          f"(diverged={n_div}, {n_div / len(rows):.3f})" if rows else "no rows")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="F3 branch-classifier sensitivity over stored 02/07 pilot logs.")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ap.add_argument("--json-out", default=None,
                    help="offline mode: also write the cells dict as JSON")
    ap.add_argument("--alt-classifier", default=None,
                    help="GATED arm: alternative classifier model slug(s), comma-separated")
    ap.add_argument("--out", default=None,
                    help="GATED arm: output JSONL (one per alt model; suffixed if several)")
    ap.add_argument("--dry-run", action="store_true",
                    help="alt arm: ZERO model calls, print call/cost estimate")
    ap.add_argument("--price", default=None, metavar="IN,OUT",
                    help="dry-run: USD per 1M input,output tokens")
    ap.add_argument("--concurrency", type=int, default=4)
    args = ap.parse_args()

    if args.alt_classifier:
        alts = [m.strip() for m in args.alt_classifier.split(",") if m.strip()]
        price = None
        if args.price:
            pin, _, pout = args.price.partition(",")
            price = (float(pin), float(pout))
        if args.dry_run:
            dry_run_alt(args.pilot_dir, alts, price)
            return
        if not args.out:
            ap.error("--out required for a live alt-classifier run (GATED: owner GO)")
        for i, alt in enumerate(alts):
            out = Path(args.out)
            if len(alts) > 1:
                out = out.with_name(f"{out.stem}-{i}{out.suffix}")
            asyncio.run(run_alt(args.pilot_dir, alt, out, args.concurrency))
        return

    cells = analyze(args.pilot_dir)
    print_report(cells)
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(cells, indent=2) + "\n",
                                       encoding="utf-8")


if __name__ == "__main__":
    main()
