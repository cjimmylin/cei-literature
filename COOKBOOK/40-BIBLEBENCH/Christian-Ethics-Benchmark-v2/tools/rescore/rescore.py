"""Two-judge re-score path — judge B, WITHOUT re-running the SUT.

Precondition #2 validation (2026-07-15d). The `inspect score` CLI re-score path does
NOT work for these custom scorers (documented finding, see the report):
  1. The CLI loads the target scorer file as a *top-level* module, so the package's
     relative imports (`from .ordo_constraints import ...`) raise ModuleNotFoundError.
  2. The 9 designs built by `scorers._register(...)` all share the registry name
     `_factory` (the `@scorer` decorator captured `_factory.__name__` before the
     post-hoc rename), so `--scorer ...@designNN_scorer` can't disambiguate them —
     only design05_scorer has a distinct registry name.

So this script IS the sanctioned path: it reads the Part-1 `.eval` logs (inspect_ai.log
API), re-assembles the SAME judge prompt via the walkworthy_inspect scorer code
(imported as a package, so prompt assembly / parsing / CSR are byte-identical to the
live judge-A pass), calls judge B, and writes judge-B verdicts JSONL. The SUT output is
read from the stored log (`sample.output.completion`); the SUT is never re-run.

Design 05 note: its PRIMARY (constraint_satisfaction_rate) is judge-free and
deterministic — it does not change between judges. We recompute it here for completeness
(identical to judge A) and additionally re-judge its model-graded secondary
`rationale_honesty` with judge B, matching the v1 2-judge protocol (both judges see the
same judge-graded categories).

AGENTS.md rule 1: every judge call passes an explicit max_tokens cap (JUDGE_MAX_TOKENS,
imported from the scorer module) — no 402 reservation trap.

Usage:
    source ~/.codex/secrets/openrouter.env
    .venv/bin/python tools/rescore/rescore.py \
        --log-dir logs/comparability-e2e \
        --judge-b openrouter/meta-llama/llama-3.3-70b-instruct \
        --out logs/comparability-e2e/judgeB-verdicts.jsonl
"""
from __future__ import annotations

import argparse
import asyncio
import glob
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# import walkworthy_inspect as a PACKAGE (v2 root on sys.path) so the scorer's
# relative imports resolve and prompt assembly is identical to the live pass.
_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402
from inspect_ai.model import GenerateConfig, get_model  # noqa: E402

from walkworthy_inspect.ordo_constraints import item_csr as _ordo_item_csr  # noqa: E402
from walkworthy_inspect.parsers import reparse_allocation_response  # noqa: E402
from walkworthy_inspect.rubrics import judge_categories, spec_for  # noqa: E402
from walkworthy_inspect.scorers import (  # noqa: E402
    JUDGE_MAX_TOKENS,
    UNSCORABLE,
    assemble_rubric_prompt,
    parse_judge_json,
)


def _design_num(meta: dict) -> str:
    d = str(meta.get("design", ""))
    return d.split("-", 1)[0].zfill(2) if d else "??"


async def _judge_one(model, prompt: str, categories) -> Dict[str, Any]:
    """Call judge B on one prompt, parse into {category: value|unscorable}."""
    try:
        out = await model.generate(prompt, config=GenerateConfig(max_tokens=JUDGE_MAX_TOKENS))
        judge_text = out.completion or ""
    except Exception as exc:  # judge failure is DATA, not a crash (v1/scorer semantics)
        return {"_judge_error": str(exc)[:200], "_raw": ""}
    parsed = parse_judge_json(judge_text, categories)
    if parsed is None:
        return {"_unparseable": True, "_raw": judge_text[:400]}
    return {k: (v if v is not None else UNSCORABLE) for k, v in parsed.items()}


async def rescore_log(path: str, judge_model_slug: str) -> List[dict]:
    log = read_eval_log(path)
    model = get_model(judge_model_slug)
    rows: List[dict] = []
    for s in log.samples or []:
        meta = s.metadata or {}
        design_num = _design_num(meta)
        spec = spec_for(design_num)
        completion = s.output.completion if s.output else ""

        # judge-A verdict from the stored Part-1 score (registry name is _factory
        # for 9 designs, design05_scorer for 05 — take the single score present).
        judge_a: Optional[dict] = None
        if s.scores:
            sc = list(s.scores.values())[0]
            judge_a = sc.value if isinstance(sc.value, dict) else {"value": sc.value}

        record: Dict[str, Any] = {
            "log": Path(path).name,
            "design": spec.design,
            "sample_id": s.id,
            "item_id": meta.get("item_id"),
            "admin": meta.get("admin"),
            "judge_a": judge_a,
        }

        if design_num in ("02", "07"):
            # Per-turn re-judge (2026-07-16): mirrors scorers._make_per_turn_scorer —
            # each recorded turn's RESPONSE ONLY is judged with unit_label="turn N",
            # so judge-B per-turn states are directly comparable to judge-A's
            # turn_states dict. Turns come from the persisted store["ww_turns"]
            # (present on all per-turn-era logs; older logs fall back to the
            # terminal-completion path below via the empty-turns guard).
            turns = (s.store or {}).get("ww_turns") or []
            if turns:
                cats = judge_categories(spec)   # == [turn_state]
                states_b: List[Any] = []
                for i, t in enumerate(turns):
                    prompt = assemble_rubric_prompt(
                        meta, spec, t.get("response", "") or "(empty)", cats,
                        unit_label=f"turn {i}")
                    jb = await _judge_one(model, prompt, cats)
                    st = jb.get("turn_state")
                    states_b.append(st if st not in (None, UNSCORABLE) and
                                    not jb.get("_unparseable") and
                                    not jb.get("_judge_error") else UNSCORABLE)
                record["judge_b"] = {
                    "turn_states": json.dumps(states_b),
                    "turn_state": states_b[-1] if states_b else UNSCORABLE,
                }
                record["branch_sources"] = [t.get("branch_source") for t in turns]
                rows.append(record)
                continue

        if design_num == "05":
            # judge-free PRIMARY (deterministic; identical across judges) — recompute
            keyed = meta.get("keyed", {}) or {}
            # 20260716 pilot bug fix (mirrors scorers.py): allocation spec lives at
            # keyed.extras.allocation in converted datasets, not top-level.
            alloc_spec = (keyed.get("allocation")
                          or (keyed.get("extras", {}) or {}).get("allocation")
                          or {})
            tokens = alloc_spec.get("tokens", []) or []
            budget = float(alloc_spec.get("budget", 0) or 0)
            constraints = keyed.get("keyed_constraints", "") or alloc_spec.get("constraints", "")
            parse = reparse_allocation_response(completion, tokens, budget)
            csr = _ordo_item_csr(parse.values or {}, constraints or "", tokens or [])
            # judged SECONDARY: rationale_honesty via judge B
            cats = judge_categories(spec)  # == [rationale_honesty]
            prompt = assemble_rubric_prompt(meta, spec, completion, cats)
            jb = await _judge_one(model, prompt, cats)
            record["judge_b"] = {
                "constraint_satisfaction_rate": csr if csr is not None else UNSCORABLE,
                "non_compliant": bool(parse.non_compliant),
                "allocation_ok": bool(parse.ok),
                **{k: v for k, v in jb.items() if not k.startswith("_")},
                **({"_judge_meta": {k: v for k, v in jb.items() if k.startswith("_")}}
                   if any(k.startswith("_") for k in jb) else {}),
            }
        else:
            cats = judge_categories(spec)
            prompt = assemble_rubric_prompt(meta, spec, completion, cats)
            jb = await _judge_one(model, prompt, cats)
            clean = {k: v for k, v in jb.items() if not k.startswith("_")}
            if any(k.startswith("_") for k in jb):
                clean["_judge_meta"] = {k: v for k, v in jb.items() if k.startswith("_")}
            record["judge_b"] = clean

        rows.append(record)
    return rows


async def main_async(args) -> None:
    logs = sorted(
        p for p in glob.glob(os.path.join(args.log_dir, "*.eval"))
        if "rescore" not in p and "_mockcheck" not in p
    )
    if not logs:
        print(f"no .eval logs in {args.log_dir}", file=sys.stderr)
        sys.exit(1)
    all_rows: List[dict] = []
    for p in logs:
        rows = await rescore_log(p, args.judge_b)
        all_rows.extend(rows)
        print(f"  rescored {Path(p).name}: {len(rows)} samples")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for r in all_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {len(all_rows)} judge-B verdicts -> {out}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Judge-B re-score of Part-1 .eval logs (no SUT re-run)")
    ap.add_argument("--log-dir", default="logs/comparability-e2e")
    ap.add_argument("--judge-b", default="openrouter/meta-llama/llama-3.3-70b-instruct")
    ap.add_argument("--out", default="logs/comparability-e2e/judgeB-verdicts.jsonl")
    args = ap.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
