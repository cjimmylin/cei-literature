"""PR-5 reliability probe — shake out flaky providers BEFORE committing the O4 roster.

The F-2 lesson: `qwen-2.5-72b` returned empty content on 45/50 pilot cells via its default
OpenRouter provider and was silently dropping data. This module probes each candidate SUT
(and tie-breaker judge candidate, incl. `x-ai/grok-4`) on 1 cell/design and reports ok /
empty / error, so a below-floor model is dropped from the roster instead of quietly
poisoning the panel. The tally logic is unit-tested; the actual probe RUN is live (panel
session), invoked via `python -m walkworthy.probe --models a,b,c`.
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .cli_backends import ModelCallError
from .clients import Message
from .loader import load_public_split

RELIABILITY_FLOOR = 0.9      # a candidate below this ok-rate is dropped (F-2 guard)


def draw_probe_prompts(all_items, per_design: int = 1) -> List[Tuple[str, str]]:
    """(design, first-user-message) for the first `per_design` items of each design."""
    by_design: dict = {}
    for it in all_items:
        by_design.setdefault(it.design, []).append(it)
    out: List[Tuple[str, str]] = []
    for design in sorted(by_design):
        pool = sorted(by_design[design], key=lambda it: it.id)
        for it in pool[:per_design]:
            text = ""
            for a in it.administrations:
                if a.turns and (a.turns[0].text or "").strip():
                    text = a.turns[0].text
                    break
                if a.terminal_ask:
                    text = a.terminal_ask
                    break
            out.append((design, text or f"(no prompt for {it.id})"))
    return out


def probe_client(name: str, client, prompts: List[Tuple[str, str]],
                 floor: float = RELIABILITY_FLOOR) -> dict:
    ok = 0
    errors: List[dict] = []
    for design, prompt in prompts:
        try:
            resp = client.complete([Message("user", prompt)])
            if (getattr(resp, "text", "") or "").strip():
                ok += 1
            else:
                errors.append({"design": design, "error": "empty content"})
        except ModelCallError as e:
            errors.append({"design": design, "error": str(e)[:160]})
        except Exception as e:                      # noqa: BLE001 — probe must survive any
            errors.append({"design": design, "error": f"{type(e).__name__}: {str(e)[:140]}"})
    n = len(prompts)
    ok_rate = ok / n if n else 0.0
    return {"name": name, "n": n, "ok": ok, "failed": n - ok,
            "ok_rate": round(ok_rate, 4), "reliable": ok_rate >= floor, "errors": errors}


def reliability_probe(named_clients: Dict[str, object], prompts: List[Tuple[str, str]],
                      floor: float = RELIABILITY_FLOOR) -> Dict[str, dict]:
    return {name: probe_client(name, client, prompts, floor)
            for name, client in named_clients.items()}


def render_probe_report(results: Dict[str, dict], date_str: Optional[str] = None) -> str:
    date_str = date_str or "(dated at run time)"
    L = ["# WALKWORTHY — O4 roster reliability probe (PR-5 / F-2)", "",
         "<!-- WALKWORTHY-CANARY-7f3e2026 -->",
         f"**Run:** {date_str}  ·  1 cell/design per candidate.  "
         f"**Reliability floor:** ok-rate ≥ {RELIABILITY_FLOOR}.", "",
         "| candidate | n | ok | ok-rate | verdict |",
         "|-----------|--:|---:|--------:|---------|"]
    for name, r in sorted(results.items()):
        verdict = "RELIABLE" if r["reliable"] else "**DROP (flaky)**"
        L.append(f"| `{name}` | {r['n']} | {r['ok']} | {r['ok_rate']:.2f} | {verdict} |")
    L += ["", "> A DROP verdict removes the candidate from the O4 roster (the qwen F-2 "
          "failure mode). Per-candidate error samples:"]
    for name, r in sorted(results.items()):
        if r["errors"]:
            L.append(f"- `{name}`: " + "; ".join(
                f"{e['design']}:{e['error'][:60]}" for e in r["errors"][:5]))
    return "\n".join(L)


def main(argv=None):
    from . import openrouter_backend as orb
    from .smoke import _cost_tracking_transport
    ap = argparse.ArgumentParser(description="WALKWORTHY PR-5 reliability probe (OpenRouter)")
    ap.add_argument("--benchmark-root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--models", required=True,
                    help="comma-separated candidate slugs (SUTs and/or tie-breaker judges)")
    ap.add_argument("--per-design", type=int, default=1)
    ap.add_argument("--out", default=None)
    ap.add_argument("--date", default=None)
    args = ap.parse_args(argv)
    root = Path(args.benchmark_root)
    date_str = args.date or date.today().strftime("%Y%m%d")
    key = orb.load_openrouter_key()
    if not key:
        raise SystemExit("probe: no OpenRouter key (set OPENROUTER_API_KEY or secrets file)")
    tr = _cost_tracking_transport()
    slugs = [s.strip() for s in args.models.split(",") if s.strip()]
    clients = {s: orb.OpenRouterClient(s, model=s, api_key=key, transport=tr) for s in slugs}
    items = load_public_split(str(root), include_exemplars=True, runnable_only=True)
    prompts = draw_probe_prompts(items, per_design=args.per_design)
    results = reliability_probe(clients, prompts)
    out = Path(args.out) if args.out else \
        root / "runs" / f"{date_str}-roster-probe" / "probe_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_probe_report(results, date_str), encoding="utf-8")
    for name, r in sorted(results.items()):
        print(f"[probe] {name}: ok {r['ok']}/{r['n']} ({r['ok_rate']:.2f}) "
              f"-> {'RELIABLE' if r['reliable'] else 'DROP'}")
    print(f"[probe] -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
