"""F7 (JV-8) — design-07 PRIOR-TURN-CONTEXT judging experiment (offline assembly + live).

R11 flags design-07 per-turn judging as ORDER-BLIND for order-dependent states: each
turn is judged in isolation (the shipped `_make_per_turn_scorer` assembles one prompt per
turn from that turn's response ONLY). This tool re-judges the SAME stored design-07 turns
with the rubric prompt AUGMENTED by prior-turn context — the administered user turns and
SUT responses up to turn i-1, read from the Inspect store key `ww_turns` — versus the
shipped context-free verdicts as baseline. JUDGE calls only; the SUT is NEVER re-run.

MONKEYPATCH-AND-RESTORE (mirrors tools/audit/judge_ablation.py philosophy):
    The whole point is that everything EXCEPT the injected prior-turn context is
    byte-identical to the live per-turn judge pass. `assemble_rubric_prompt` resolves
    `scorers._references(meta)` through the module namespace to build the reference block
    (design-07 ships `reference_anchored=True`, so that block is always emitted). We patch
    `_scorers._references` to return the ORIGINAL design-07 anchors with ONE extra anchor
    PREPENDED: a "Prior turns in this conversation (turns 0..i-1)" block for the current
    turn. The per-turn context is passed through a module-local holder set immediately
    before each `assemble_rubric_prompt` call and cleared after. We patch, assemble, then
    restore the original `_references` in `finally`. The assembler is REUSED verbatim, not
    forked — so the context-free arm and the context arm differ by exactly one block.

WHY THE REFERENCE-BLOCK SURFACE (not response_text): the shipped assembler injects
`response_text` as the turn under evaluation and gates every extra block behind
`spec.reference_anchored`. Design-07 is reference-anchored, so prepending the context to
`_references(meta)` places it inside the already-emitted "# Matched-quality reference
answers" section, ahead of the state anchors — the judge sees the conversation so far,
then the state-classification anchors, then the turn to score. No assembler fork; the
turn's own `response_text` is still the unit under evaluation.

Modes:
  (a) --dry-run (DEFAULT): assemble ALL context-augmented prompts, write per-prompt
      char/token stats, ZERO network calls.
  (b) --live: gated behind BOTH the flag AND env WW_F7_LIVE=1 (left unset), AND requires
      an explicit --max-tokens cap (OpenRouter 402 reservation trap: every call needs an
      explicit max_tokens). Verdicts are written INCREMENTALLY (JSONL append per verdict,
      NOT buffered-to-completion — the classifier_sensitivity.py buffer-everything pattern
      made progress invisible).

Data gotchas (all have bitten before):
  * Inspect Score.value rejects nested dicts, so turn_states is JSON-encoded elsewhere;
    here we read the raw `ww_turns` store list (already decoded by inspect_ai.log).
  * sample_ids COLLIDE across SUTs (same items) — every output row is scoped by
    (sut, log basename, sample_id) so downstream joins never silently overwrite.

AGENTS.md rule 1: every judge call passes an explicit max_tokens cap.

Usage (dry-run — ZERO model calls; default):
    .venv/bin/python tools/audit/judge_context_ablation.py \
        --judge openrouter/openai/gpt-4.1-nano \
        --stats-out logs/f7-context/dryrun-judgeA.json --dry-run

Usage (live — NOT authorized this session; needs WW_F7_LIVE=1 + --max-tokens):
    WW_F7_LIVE=1 source ~/.codex/secrets/openrouter.env
    .venv/bin/python tools/audit/judge_context_ablation.py \
        --judge openrouter/openai/gpt-4.1-nano --live --max-tokens 4096 \
        --out logs/f7-context/context-judgeA.jsonl
"""
from __future__ import annotations

import argparse
import asyncio
import contextlib
import glob
import json
import os
import statistics
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# import walkworthy_inspect as a PACKAGE (v2 root on sys.path) so the scorer's relative
# imports resolve and prompt assembly is identical to the live per-turn pass.
_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.model import GenerateConfig, get_model  # noqa: E402
from inspect_ai.log import read_eval_log  # noqa: E402

from walkworthy_inspect import scorers as _scorers  # noqa: E402
from walkworthy_inspect.rubrics import judge_categories, spec_for  # noqa: E402
from walkworthy_inspect.scorers import (  # noqa: E402
    JUDGE_MAX_TOKENS,
    UNSCORABLE,
    assemble_rubric_prompt,
    parse_judge_json,
)

DESIGN = "07"
# per-turn user/response context truncation (mirrors the 400-char cap the assembler
# already applies to each reference-anchor text, so the injected block stays in-band).
_CTX_TURN_CHARS = 600


def _design_num(meta: dict) -> str:
    d = str(meta.get("design", ""))
    return d.split("-", 1)[0].zfill(2) if d else "??"


# --------------------------------------------------------------------------- #
# module-local holder for the current turn's prior context. The patched _references
# reads it; the driver sets it immediately before each assemble_rubric_prompt call and
# clears it after. This is how per-turn context reaches an otherwise meta-only function
# without forking the assembler.
# --------------------------------------------------------------------------- #
_CURRENT_PRIOR_CONTEXT: Dict[str, Any] = {"anchor": None}


def _build_prior_context_anchor(turns: List[dict], i: int) -> Optional[dict]:
    """One reference-anchor dict summarizing turns 0..i-1 (the conversation so far).

    Returns None for turn 0 (no prior context) so the context arm's turn-0 prompt is
    byte-identical to the context-free arm's turn-0 prompt — turn 0 has no order info to
    add, and forcing an empty block would spuriously differentiate it.
    """
    if i <= 0:
        return None
    prior = turns[:i]
    lines: List[str] = []
    for t in prior:
        idx = (t or {}).get("index", "?")
        user = (str((t or {}).get("user_text", "") or "")).strip()[:_CTX_TURN_CHARS]
        resp = (str((t or {}).get("response", "") or "")).strip()[:_CTX_TURN_CHARS]
        lines.append(f"[turn {idx}] SEEKER: {user}")
        lines.append(f"[turn {idx}] COUNSELOR: {resp}")
    text = "\n".join(lines)
    return {
        "label": ("Prior turns in THIS conversation (turns 0.."
                  f"{i - 1}) — the counsel state is ORDER-DEPENDENT: judge the turn "
                  "below in light of what was already said/asked, not in isolation"),
        "text": text,
    }


@contextlib.contextmanager
def context_patch():
    """Patch _scorers._references to PREPEND the current-turn prior-context anchor to the
    ORIGINAL design-07 anchors; restore the original in finally."""
    orig_refs = _scorers._references

    def _refs(meta: dict) -> List[dict]:
        base = orig_refs(meta)
        if str(meta.get("design", "")).startswith(DESIGN):
            ctx = _CURRENT_PRIOR_CONTEXT.get("anchor")
            if ctx is not None:
                return [ctx] + list(base)
        return base

    _scorers._references = _refs
    try:
        yield
    finally:
        _scorers._references = orig_refs
        _CURRENT_PRIOR_CONTEXT["anchor"] = None


def _assemble_turn_prompt(meta: dict, spec, cats, turns: List[dict], i: int) -> str:
    """Assemble the context-augmented judge prompt for turn i. REUSES the shipped
    assembler; the prior-context anchor is injected via the module-local holder + patch."""
    _CURRENT_PRIOR_CONTEXT["anchor"] = _build_prior_context_anchor(turns, i)
    try:
        resp = (turns[i] or {}).get("response", "") or "(empty)"
        return assemble_rubric_prompt(meta, spec, resp, cats, unit_label=f"turn {i}")
    finally:
        _CURRENT_PRIOR_CONTEXT["anchor"] = None


# --------------------------------------------------------------------------- #
# iterate stored design-07 samples across SUTs, assembling one plan per sample.
# --------------------------------------------------------------------------- #
def _sut_dirs(pilot_dir: str, suts_csv: Optional[str]) -> List[str]:
    all_suts = sorted(d for d in glob.glob(os.path.join(pilot_dir, "*/"))
                      if glob.glob(os.path.join(d, "*.eval")))
    if not suts_csv:
        return all_suts
    want = {s.strip() for s in suts_csv.split(",") if s.strip()}
    return [d for d in all_suts if Path(d.rstrip("/")).name in want]


def _iter_design07_samples(sut_dir: str):
    """Yield (log_basename, sample) for every design-07 sample in a SUT dir."""
    for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
        if "design07" not in Path(p).name:
            continue
        log = read_eval_log(p)
        for s in (log.samples or []):
            if _design_num(s.metadata or {}) != DESIGN:
                continue
            yield Path(p).name, s


def _sample_plan(sut_name: str, log_name: str, s) -> Optional[dict]:
    """Build the per-turn context-augmented prompt list for one sample."""
    meta = s.metadata or {}
    spec = spec_for(DESIGN)
    cats = judge_categories(spec)
    turns = (s.store or {}).get("ww_turns") or []
    if not turns:
        return None
    prompts = [_assemble_turn_prompt(meta, spec, cats, turns, i)
               for i in range(len(turns))]
    return {
        "sut": sut_name,
        "log": log_name,
        "sample_id": s.id,
        "item_id": meta.get("item_id"),
        "admin": meta.get("admin"),
        "design": spec.design,
        "n_turns": len(turns),
        "branch_sources": [(t or {}).get("branch_source") for t in turns],
        "prompts": prompts,
        "categories": cats,
    }


# --------------------------------------------------------------------------- #
# DRY RUN: assemble ALL prompts, ZERO model calls; per-prompt char/token stats.
# --------------------------------------------------------------------------- #
def dry_run(pilot_dir: str, suts_csv: Optional[str], judge: str,
            stats_out: Optional[str]) -> None:
    per_sut: Dict[str, Dict[str, int]] = {}
    all_lens: List[int] = []
    turn0_lens: List[int] = []
    total_calls = 0
    total_chars = 0
    sut_dirs = _sut_dirs(pilot_dir, suts_csv)

    with context_patch():
        for sut in sut_dirs:
            sut_name = Path(sut.rstrip("/")).name
            per_sut.setdefault(sut_name, {"samples": 0, "turns": 0, "chars": 0})
            for log_name, s in _iter_design07_samples(sut):
                plan = _sample_plan(sut_name, log_name, s)
                if plan is None:
                    continue
                per_sut[sut_name]["samples"] += 1
                for i, pr in enumerate(plan["prompts"]):
                    L = len(pr)
                    all_lens.append(L)
                    if i == 0:
                        turn0_lens.append(L)
                    per_sut[sut_name]["turns"] += 1
                    per_sut[sut_name]["chars"] += L
                    total_calls += 1
                    total_chars += L

    est_in_tokens = total_chars // 4
    print(f"=== F7 DRY RUN  design-{DESIGN} prior-turn-context  judge={judge} ===")
    print(f"    SUTs={len(sut_dirs)}  (context arm; per-turn re-judge, no SUT calls)\n")
    for sut_name, dd in per_sut.items():
        print(f"  {sut_name:20} samples={dd['samples']:3}  "
              f"prompts(turns)={dd['turns']:4}  chars={dd['chars']:>9}")
    print(f"\n  TOTAL prompts (per judge) = {total_calls}")
    print(f"  TOTAL prompt_chars        = {total_chars}")
    print(f"  est_input_tokens (chars/4)= {est_in_tokens}")

    dist = _len_dist(all_lens)
    print("\n  --- context-augmented prompt length (chars) ---")
    for k, v in dist.items():
        print(f"    {k:8} = {v}")
    if turn0_lens:
        print(f"    turn0_n  = {len(turn0_lens)}  (no prior context; baseline-length)")
        print(f"    turn0_mean_chars = {statistics.mean(turn0_lens):.1f}")

    if stats_out:
        payload = {
            "mode": "dry-run", "design": DESIGN, "judge": judge,
            "suts": [Path(d.rstrip('/')).name for d in sut_dirs],
            "total_prompts_per_judge": total_calls,
            "total_prompt_chars": total_chars,
            "est_input_tokens_chars_div4": est_in_tokens,
            "prompt_len_chars": dist,
            "turn0_prompts": len(turn0_lens),
            "per_sut": per_sut,
        }
        Path(stats_out).parent.mkdir(parents=True, exist_ok=True)
        with open(stats_out, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)
        print(f"\n  wrote per-prompt stats -> {stats_out}")


def _len_dist(lens: List[int]) -> Dict[str, Any]:
    if not lens:
        return {"n": 0}
    srt = sorted(lens)
    def _pct(p: float) -> int:
        return srt[min(len(srt) - 1, int(round(p * (len(srt) - 1))))]
    return {
        "n": len(lens),
        "min": srt[0],
        "mean": round(statistics.mean(lens), 1),
        "median": srt[len(srt) // 2],
        "p90": _pct(0.90),
        "max": srt[-1],
        "total_chars": sum(lens),
        "est_input_tokens_total": sum(lens) // 4,
    }


# --------------------------------------------------------------------------- #
# LIVE re-judge (gated). Writes verdicts INCREMENTALLY (append per verdict).
# --------------------------------------------------------------------------- #
async def _judge_one(model, prompt: str, cats, max_tokens: int) -> Dict[str, Any]:
    try:
        out = await model.generate(prompt, config=GenerateConfig(max_tokens=max_tokens))
        judge_text = out.completion or ""
    except Exception as exc:  # judge failure is DATA, not a crash
        return {"_judge_error": str(exc)[:200]}
    parsed = parse_judge_json(judge_text, cats)
    if parsed is None:
        return {"_unparseable": True, "_raw": judge_text[:300]}
    ts = parsed.get("turn_state")
    return {"turn_state": ts if ts is not None else UNSCORABLE}


async def live_run(pilot_dir: str, suts_csv: Optional[str], judge: str,
                   out_path: str, max_tokens: int, concurrency: int) -> None:
    sut_dirs = _sut_dirs(pilot_dir, suts_csv)
    model = get_model(judge)
    sem = asyncio.Semaphore(concurrency)
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    n_rows = 0

    async def _guarded(prompt, cats):
        async with sem:
            return await _judge_one(model, prompt, cats, max_tokens)

    # append-per-verdict: open in append mode, flush each line so progress is visible.
    with context_patch(), out.open("a", encoding="utf-8") as fh:
        for sut in sut_dirs:
            sut_name = Path(sut.rstrip("/")).name
            for log_name, s in _iter_design07_samples(sut):
                plan = _sample_plan(sut_name, log_name, s)
                if plan is None:
                    continue
                cats = plan["categories"]
                results = await asyncio.gather(
                    *[_guarded(p, cats) for p in plan["prompts"]])
                states: List[Any] = []
                for jr in results:
                    st = jr.get("turn_state")
                    ok = (st not in (None, UNSCORABLE)
                          and not jr.get("_unparseable") and not jr.get("_judge_error"))
                    states.append(st if ok else UNSCORABLE)
                row = {
                    "sut": plan["sut"], "log": plan["log"],
                    "sample_id": plan["sample_id"], "item_id": plan["item_id"],
                    "admin": plan["admin"], "design": plan["design"],
                    "arm": "prior-turn-context", "judge_model": judge,
                    "verdict": {
                        "turn_states": json.dumps(states),
                        "turn_state": states[-1] if states else UNSCORABLE,
                        "branch_sources": plan["branch_sources"],
                    },
                }
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
                fh.flush()  # incremental — progress visible, not buffered-to-completion
                n_rows += 1
                print(f"  {sut_name}/{plan['sample_id']}: {len(states)} turns")
    print(f"wrote {n_rows} context-augmented verdict rows (append) -> {out}")


# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(
        description="F7 design-07 prior-turn-context re-judge (offline assembly + gated live).")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ap.add_argument("--judge", required=True, help="judge model slug")
    ap.add_argument("--suts", default=None, help="comma-separated SUT dir names (default all)")
    ap.add_argument("--dry-run", action="store_true", default=True,
                    help="assemble ALL prompts, ZERO model calls (DEFAULT)")
    ap.add_argument("--live", action="store_true",
                    help="fire judge calls (requires WW_F7_LIVE=1 env AND --max-tokens)")
    ap.add_argument("--stats-out", default=None, help="dry-run: JSON per-prompt stats path")
    ap.add_argument("--out", default=None, help="live: output JSONL path (appended)")
    ap.add_argument("--max-tokens", type=int, default=None,
                    help=f"live: explicit output cap (prior runs use {JUDGE_MAX_TOKENS})")
    ap.add_argument("--concurrency", type=int, default=4)
    args = ap.parse_args()

    if args.live:
        # DOUBLE GATE: flag + env var. Env var is intentionally left UNSET this session.
        if os.environ.get("WW_F7_LIVE") != "1":
            print("REFUSED: --live requires env WW_F7_LIVE=1 (unset). No calls made.",
                  file=sys.stderr)
            sys.exit(2)
        if args.max_tokens is None:
            print("REFUSED: --live requires an explicit --max-tokens (OpenRouter 402 "
                  "reservation trap). No calls made.", file=sys.stderr)
            sys.exit(2)
        if not args.out:
            print("REFUSED: --live requires --out. No calls made.", file=sys.stderr)
            sys.exit(2)
        asyncio.run(live_run(args.pilot_dir, args.suts, args.judge, args.out,
                             args.max_tokens, args.concurrency))
    else:
        dry_run(args.pilot_dir, args.suts, args.judge, args.stats_out)


if __name__ == "__main__":
    main()
