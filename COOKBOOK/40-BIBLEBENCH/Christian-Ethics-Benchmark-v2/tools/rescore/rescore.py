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
from walkworthy_v4.completion_guard import (  # noqa: E402
    COMPLETION_EXCLUDED,
    check_completion,
    excluded_meta,
)


def _design_num(meta: dict) -> str:
    d = str(meta.get("design", ""))
    return d.split("-", 1)[0].zfill(2) if d else "??"


# v4-A 2(a) judge parse hardening (RULINGS-APPLIED-20260801a RULING 1.2; defect
# record 20260731o §6.1). The reminder is the F9 convention ported to the judge
# path: it fires ONLY on attempts after the plain prompt has already failed to
# parse, so a parseable first reply is byte-identical to the pre-hardening path.
_JUDGE_FORMAT_REMINDER = (
    "REMINDER: your previous reply could not be parsed. Respond with a SINGLE "
    "JSON object containing exactly the requested keys and nothing else - no "
    "markdown, no headings, no commentary, no repetition. Output the JSON "
    "object now."
)
DEFAULT_JUDGE_ATTEMPTS = 3
RETENTION_TARGET = 0.85  # ratified complete-case gate (20260731o §6.1)
_ERROR_BACKOFF_BASE_S = 0.5  # transport-error backoff; tests set this to 0


async def _judge_one(model, prompt: str, categories,
                     max_attempts: int = DEFAULT_JUDGE_ATTEMPTS) -> Dict[str, Any]:
    """Call judge B on one prompt, parse into {category: value|unscorable}.

    Retries on parse failure (degenerate/empty/non-JSON output) and on transport
    error, up to max_attempts total calls; attempts after the first append
    _JUDGE_FORMAT_REMINDER (same-prompt retry alone is insufficient: the v4-T
    probe's 5 degenerate llama-3.3-70b outputs each failed an identical retry).
    `_attempts` is recorded on every return value for audit.
    """
    last_error: Optional[str] = None
    last_raw = ""
    attempts = 0
    for attempt in range(max(1, max_attempts)):
        attempts = attempt + 1
        attempt_prompt = (prompt if attempt == 0
                          else prompt + "\n\n" + _JUDGE_FORMAT_REMINDER)
        try:
            out = await model.generate(
                attempt_prompt, config=GenerateConfig(max_tokens=JUDGE_MAX_TOKENS))
            judge_text = out.completion or ""
        except Exception as exc:  # judge failure is DATA, not a crash (v1/scorer semantics)
            last_error = str(exc)[:200]
            if attempt < max_attempts - 1 and _ERROR_BACKOFF_BASE_S:
                await asyncio.sleep(_ERROR_BACKOFF_BASE_S * (2 ** attempt))
            continue
        last_error = None
        last_raw = judge_text[:400]
        parsed = parse_judge_json(judge_text, categories)
        if parsed is not None:
            result = {k: (v if v is not None else UNSCORABLE) for k, v in parsed.items()}
            result["_attempts"] = attempts
            return result
    if last_error is not None:
        return {"_judge_error": last_error, "_raw": last_raw, "_attempts": attempts}
    return {"_unparseable": True, "_raw": last_raw, "_attempts": attempts}


def retention_by_design(rows: List[dict]) -> Dict[str, dict]:
    """Per-design complete-case retention over judge-B verdict rows.

    A row is complete-case when no judge-B call behind it ended unparseable or
    errored (per-turn designs: every turn parsed). Genuine UNSCORABLE verdicts
    from a PARSED reply are judge data, not attrition, and do not count against
    retention. Completion-excluded rows (v4-A 2(b): empty/truncated SUT output,
    never judged) are SUT-side attrition — counted in `excluded`, outside both
    the numerator and the denominator, and disclosed separately.
    """
    stats: Dict[str, dict] = {}
    for r in rows:
        jb = r.get("judge_b") or {}
        meta = jb.get("_judge_meta") or {}
        design = str(r.get("design", "??"))
        d = stats.setdefault(design, {"rows": 0, "complete": 0, "excluded": 0})
        if meta.get(COMPLETION_EXCLUDED):
            d["excluded"] += 1
            continue
        d["rows"] += 1
        if "turn_failures" in meta:
            failed = any(meta["turn_failures"])
        else:
            failed = bool(meta.get("_unparseable") or meta.get("_judge_error"))
        if not failed:
            d["complete"] += 1
    for d in stats.values():
        d["retention"] = (d["complete"] / d["rows"]) if d["rows"] else None
    return stats


def print_retention_report(rows: List[dict]) -> None:
    stats = retention_by_design(rows)
    print(f"complete-case retention by design (target >= {RETENTION_TARGET:.2f}):")
    for design in sorted(stats):
        d = stats[design]
        if d["retention"] is None:
            line = f"  {design}: 0 judged rows"
        else:
            line = f"  {design}: {d['complete']}/{d['rows']} = {d['retention']:.3f}"
            if d["retention"] < RETENTION_TARGET:
                line += f"  WARN below {RETENTION_TARGET:.2f} gate"
        if d.get("excluded"):
            line += f"  ({d['excluded']} completion-excluded, SUT-side)"
        print(line)


async def rescore_log(path: str, judge_model_slug: str,
                      judge_attempts: int = DEFAULT_JUDGE_ATTEMPTS) -> List[dict]:
    log = read_eval_log(path)
    model = get_model(judge_model_slug)
    rows: List[dict] = []
    for s in log.samples or []:
        meta = s.metadata or {}
        design_num = _design_num(meta)
        spec = spec_for(design_num)
        completion = s.output.completion if s.output else ""
        stop_reason = getattr(s.output, "stop_reason", None) if s.output else None
        # v4-A 2(b) half (a): empty/truncated completions never reach a judge
        # (20260731o §6.2 — judges scored empty text, incl. 14 d08 passing
        # guardrail verdicts). SUT-side attrition, excluded with reason.
        completion_check = check_completion(completion, stop_reason)

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
                turn_attempts: List[int] = []
                turn_failures: List[bool] = []
                turn_excluded: List[bool] = []
                for i, t in enumerate(turns):
                    response = t.get("response", "") or ""
                    turn_check = check_completion(response)
                    if not turn_check.scorable:
                        # 2(b): an empty SUT turn is excluded pre-judge — the v3
                        # path judged the literal placeholder "(empty)".
                        states_b.append(UNSCORABLE)
                        turn_attempts.append(0)
                        turn_failures.append(False)
                        turn_excluded.append(True)
                        continue
                    prompt = assemble_rubric_prompt(
                        meta, spec, response, cats, unit_label=f"turn {i}")
                    jb = await _judge_one(model, prompt, cats,
                                          max_attempts=judge_attempts)
                    st = jb.get("turn_state")
                    states_b.append(st if st not in (None, UNSCORABLE) and
                                    not jb.get("_unparseable") and
                                    not jb.get("_judge_error") else UNSCORABLE)
                    turn_attempts.append(int(jb.get("_attempts", 1)))
                    turn_failures.append(bool(jb.get("_unparseable") or
                                              jb.get("_judge_error")))
                    turn_excluded.append(False)
                record["judge_b"] = {
                    "turn_states": json.dumps(states_b),
                    "turn_state": states_b[-1] if states_b else UNSCORABLE,
                    "_judge_meta": {"turn_attempts": turn_attempts,
                                    "turn_failures": turn_failures,
                                    "turn_excluded": turn_excluded},
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
            # judged SECONDARY: rationale_honesty via judge B (the judge-free
            # PRIMARY above is still computed: an empty completion is
            # non_compliant DATA under F8 parser semantics, not attrition).
            cats = judge_categories(spec)  # == [rationale_honesty]
            if not completion_check.scorable:
                jb = {c.name: UNSCORABLE for c in cats}
                jb.update(excluded_meta(completion_check))
            else:
                prompt = assemble_rubric_prompt(meta, spec, completion, cats)
                jb = await _judge_one(model, prompt, cats,
                                      max_attempts=judge_attempts)
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
            if not completion_check.scorable:
                jb = {c.name: UNSCORABLE for c in cats}
                jb.update(excluded_meta(completion_check))
            else:
                prompt = assemble_rubric_prompt(meta, spec, completion, cats)
                jb = await _judge_one(model, prompt, cats,
                                      max_attempts=judge_attempts)
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
        rows = await rescore_log(p, args.judge_b, judge_attempts=args.judge_attempts)
        all_rows.extend(rows)
        print(f"  rescored {Path(p).name}: {len(rows)} samples")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for r in all_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {len(all_rows)} judge-B verdicts -> {out}")
    print_retention_report(all_rows)


def main() -> None:
    ap = argparse.ArgumentParser(description="Judge-B re-score of Part-1 .eval logs (no SUT re-run)")
    ap.add_argument("--log-dir", default="logs/comparability-e2e")
    ap.add_argument("--judge-b", default="openrouter/meta-llama/llama-3.3-70b-instruct")
    ap.add_argument("--out", default="logs/comparability-e2e/judgeB-verdicts.jsonl")
    ap.add_argument("--judge-attempts", type=int, default=DEFAULT_JUDGE_ATTEMPTS,
                    help="max judge calls per unit: 1 plain + N-1 format-reminder "
                         "retries on parse failure (v4-A 2(a), 20260731o §6.1)")
    args = ap.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
