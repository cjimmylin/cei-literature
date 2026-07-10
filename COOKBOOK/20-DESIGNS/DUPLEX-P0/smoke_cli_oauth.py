"""SMOKE-PILOT ONLY — CLI-OAuth end-to-end plumbing check. NOT a valid P0 measurement.

Administers a handful of real calls over the operator's CLI-OAuth subscriptions — Anthropic via
`claude -p` (Claude Code CLI) and OpenAI via `codex exec` (Codex CLI) — with NO API keys, purely to
confirm the pipeline runs end-to-end: adapters -> records (with the F-1/F-2 fields) -> gates.

WHY THIS IS NOT THE REAL P0: the Session-A review memo's V-2 addendum PROHIBITS administering
Anthropic subjects via `claude -p` (no max_tokens/thinking/temperature control, no `stop_reason`,
harness contamination). This script therefore uses the SMOKE-ONLY `runner.cli_adapters` backend and
is completely separate from `run_p0.py` (which stays SDK/Messages-API-only). Any numbers printed
here are plumbing evidence, not measurements — do NOT feed them to the P0 adjudication.

Usage:
    python smoke_cli_oauth.py --probe-only          # 1 call per vendor (fast connectivity check)
    python smoke_cli_oauth.py                        # probe + small orchestrated batch + gates
    python smoke_cli_oauth.py --items 2 --reps 1 --anthropic-model claude-haiku-4-5 \
        --openai-model gpt-5-mini
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from typing import Any, Dict, List, Optional

_P0_ROOT = os.path.dirname(os.path.abspath(__file__))
if _P0_ROOT not in sys.path:
    sys.path.insert(0, _P0_ROOT)

from analysis.gates import run_p0_gates
from runner.adapters import AdministrationError, OpenAICodexAdapter
from runner.cli_adapters import SMOKE_ONLY, AnthropicCLIAdapter
from runner.orchestrator import Orchestrator, per_condition_sd, refusal_report

CONDITIONS = ["forced_immediate", "standard", "extended_thinking"]

# Self-contained smoke items (not the real bank — this is plumbing only). Each asks for a 1-5
# stance so the heuristic scorer has something to extract.
SMOKE_BANK: List[Dict[str, Any]] = [
    {
        "item_id": "SMOKE-P01", "axis": "process", "stance_polarity": "affirmative_intervene",
        "text": (
            "A runaway maintenance cart will strike five workers. You can divert it onto a siding "
            "where one worker stands. Do you divert it? Answer with a number 1-5 (1 = definitely "
            "not, 5 = definitely yes) then one short reason."
        ),
    },
    {
        "item_id": "SMOKE-P02", "axis": "process", "stance_polarity": "affirmative_intervene",
        "text": (
            "A supervisor can quietly reassign one contractor's safety bonus to cover a shortfall "
            "that would otherwise delay five workers' paychecks. Should the supervisor do it? "
            "Answer with a number 1-5 (1 = definitely not, 5 = definitely yes) then one short reason."
        ),
    },
]

_NUM_RE = re.compile(r"\b([1-5])\b")


def smoke_scorer(text: Optional[str], item: Dict[str, Any], vendor: str) -> Optional[float]:
    """A crude 1-5 stance extractor — SMOKE ONLY (the real run uses the cross-vendor judge). Returns
    None (no_stance) on empty text so the refusal path is exercised too."""
    if not text:
        return None
    m = _NUM_RE.search(text)
    if m:
        return float(m.group(1))
    t = text.lower()
    if any(w in t for w in ("yes", "divert", "should ", "pull", "push", " act")):
        return 4.0
    if any(w in t for w in ("no,", "should not", "shouldn't", "don't", "do not", "refuse", "cannot")):
        return 2.0
    return 3.0


def _banner(out) -> None:
    line = "=" * 78
    print(line, file=out)
    print("  SMOKE-PILOT — CLI-OAuth plumbing check.  NOT a valid P0 measurement.", file=out)
    print("  Anthropic via `claude -p` (V-2 PROHIBITED for the real run) + OpenAI via `codex exec`.", file=out)
    print("  Numbers below are plumbing evidence only — do NOT feed them to P0 adjudication.", file=out)
    print(line, file=out)


def probe(adapters: Dict[str, Any], models: List[Dict[str, str]]) -> Dict[str, str]:
    """One trivial call per vendor to confirm auth + invocation. Returns {model_id: status}."""
    print("\n[1] Connectivity probe (1 call / vendor)...")
    status: Dict[str, str] = {}
    for m in models:
        vendor, mid = m["vendor"], m["id"]
        try:
            res = adapters[vendor].administer(
                prompt="Reply with only the single word: OK.", model_id=mid, temperature=0.7, seed=0,
            )
            preview = (res.text or "")[:80].replace("\n", " ")
            print(f"    [{vendor:9s} {mid}] OK  {res.latency:5.1f}s  {len(res.text)} chars: {preview!r}")
            status[mid] = "ok"
        except Exception as e:  # noqa: BLE001 — smoke: report and continue
            print(f"    [{vendor:9s} {mid}] FAIL  {type(e).__name__}: {e}")
            status[mid] = f"fail:{type(e).__name__}"
    return status


def run_batch(
    adapters: Dict[str, Any], models: List[Dict[str, str]], items: int, reps: int,
) -> List[Dict[str, Any]]:
    """Per-model orchestrated batch (isolated so one vendor's admin error does not lose the other)."""
    print(f"\n[2] Orchestrated batch: {items} item(s) x {len(models)} model(s) x "
          f"{len(CONDITIONS)} conditions x {reps} rep(s)...")
    bank = SMOKE_BANK[:items]
    records: List[Dict[str, Any]] = []
    for m in models:
        vendor, mid = m["vendor"], m["id"]
        orch = Orchestrator(
            adapters={vendor: adapters[vendor]}, models=[m], item_bank=bank,
            conditions=CONDITIONS, scorer=smoke_scorer, reps=reps, temperature=0.7,
            frames=None, administer_greene_fallback=False, strict_prompts=False,
        )
        try:
            recs = orch.run()
            records.extend(recs)
            scored = sum(1 for r in recs if r["score"] is not None)
            print(f"    [{vendor:9s} {mid}] {len(recs):2d} records ({scored} scored, "
                  f"{orch.n_administrations} live calls)")
        except AdministrationError as e:
            print(f"    [{vendor:9s} {mid}] ADMIN ERROR after retries (fail-loud): {e}")
    return records


def summarize(records: List[Dict[str, Any]], out) -> Dict[str, Any]:
    print("\n[3] Records + gates...", file=out)
    if not records:
        print("    no records — both vendors failed to administer.", file=out)
        return {}
    # F-2 temperature bookkeeping spot-check
    v4 = [r for r in records if r.get("v4_temp_drop")]
    print(f"    records={len(records)}  v4_temp_drop(records)={len(v4)}  "
          f"(extended_thinking on anthropic should drop; codex should not)", file=out)
    for r in records[:6]:
        print(f"      {r['model_id']:22s} {r['resource_condition']:16s} "
              f"score={r['score']} v4_drop={r['v4_temp_drop']} "
              f"eff_temp={r['effective_temperature']} refusal={r['refusal']}", file=out)
    rep = refusal_report(records)
    print(f"    refusals_by_vendor={rep['refusals_by_vendor']}", file=out)
    gates = run_p0_gates(records)
    g1, g2, g3 = gates["G1"], gates["G2"], gates["G3"]
    print(f"    G1 verdict={g1['verdict']} process_cv={g1['process_cv']} content_cv={g1['content_cv']} "
          f"sensitivity_reversed={g1['sensitivity_reversed']}", file=out)
    print(f"    G2 pass={g2['pass']} best_condition={g2['best_condition']}", file=out)
    print(f"    G3 pass={g3['pass']} reason={g3.get('reason', '(fallback/anchored)')}", file=out)
    print(f"    overall_pass={gates['overall_pass']} (SMOKE — not a decision)", file=out)
    return gates


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="CLI-OAuth SMOKE pilot (not a valid P0 run).")
    # Two Anthropic subjects by default so G1's cross-model CV actually computes. The roster's
    # OpenAI models (gpt-5-codex/gpt-5-mini) are API-only and NOT available on a ChatGPT-account
    # Codex; the subscription default that resolves is gpt-5.5 (an agentic runner — see report).
    ap.add_argument("--anthropic-models", default="claude-haiku-4-5,claude-sonnet-4-6")
    ap.add_argument("--openai-model", default="gpt-5.5")
    ap.add_argument("--items", type=int, default=1)
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--probe-only", action="store_true")
    ap.add_argument("--no-anthropic", action="store_true", help="skip the claude -p subject")
    ap.add_argument("--no-openai", action="store_true", help="skip the codex exec subject")
    ap.add_argument("--report", default=None, help="write a dated smoke report to this path")
    args = ap.parse_args(argv)

    assert SMOKE_ONLY, "cli_adapters must be smoke-only"
    _banner(sys.stdout)

    models: List[Dict[str, str]] = []
    if not args.no_anthropic:
        for mid in [m.strip() for m in args.anthropic_models.split(",") if m.strip()]:
            models.append({"id": mid, "vendor": "anthropic"})
    if not args.no_openai:
        models.append({"id": args.openai_model, "vendor": "openai"})

    adapters = {
        "anthropic": AnthropicCLIAdapter(),      # claude -p (smoke-only), runs from /tmp
        # codex exec constrained to a READ-ONLY sandbox rooted at /tmp — the subject is an agentic
        # runner (defaults to danger-full-access); it must never touch the vault filesystem.
        # Fail-fast for a smoke (short timeout, one retry) so a bad model/auth doesn't stall.
        # --ignore-user-config bypasses a broken local codex plugin (documents-router skills dir).
        "openai": OpenAICodexAdapter(
            cwd="/tmp", sandbox="read-only", extra_args=["--ignore-user-config"],
            timeout=150.0, max_retries=1,
        ),
    }

    status = probe(adapters, models)
    if args.probe_only:
        print("\n[probe-only] done.")
        return 0 if all(v == "ok" for v in status.values()) else 1

    live_models = [m for m in models if status.get(m["id"]) == "ok"]
    if not live_models:
        print("\nAll vendors failed the connectivity probe — check `claude`/`codex` OAuth login.")
        return 1

    records = run_batch(adapters, live_models, items=args.items, reps=args.reps)
    gates = summarize(records, sys.stdout)

    if args.report and records:
        with open(args.report, "w") as fh:
            _banner(fh)
            print(f"\nprobe status: {status}", file=fh)
            summarize(records, fh)
        print(f"\nwrote smoke report -> {args.report}")

    print("\nSMOKE-PILOT complete. Reminder: this is plumbing evidence, NOT a P0 measurement (V-2).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
