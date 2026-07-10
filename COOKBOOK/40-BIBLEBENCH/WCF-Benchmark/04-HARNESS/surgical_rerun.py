#!/usr/bin/env python
"""R40.4 surgical re-run — the persisted-text-first floor divergence closure (memo R38-R41).

Binding memo `20260710-fable-grok-ratification-floor-divergence-memo.md`, R40.4. The
`AGG-C8-W305 x llama` aggregate 0.0 was adjudicated a judge-side + transport-side artifact:
grok's JSONDecodeError drop left an even 2-judge settled-core panel and the old tie->False
rule resolved a 1-1 tie to False. This script surgically re-grades ONLY the cells the memo
directs, PRESERVING the adjudicated sample (no new SUT call where a persisted response
exists):

  (a) re-grade grok-4.20 ONLY on the PERSISTED AGG-C8-W305 x llama response (NO SUT call) —
      supplies the missing 3rd settled-core vote, completing the tie-breaker the memo needs.
  (b) re-grade ALL 3 judges on the PERSISTED deepseek WHOLE-C9-W301 response (the SUT text
      exists; all 3 judge calls transport-failed in the floor re-run -> judges = []).
  (c) FRESH deepseek/deepseek-chat SUT calls ONLY for AGG-C3-W302 / AGG-C5-W304 / AGG-C8-W305
      (no persisted response — the deepseek contested arm 403'd on "Key limit exceeded"),
      graded by the manifest panel.
  (d) the llama arm is NOT re-run (scored + adjudicated).

Panel = the combined third-family manifest, UNCHANGED (no prompt template edited — R40.4
requires running under the CURRENT templates for comparability with the adjudication). The
R40.2 retry seam + R40.3 tie->UNGRADED fix are LIVE in judge_panel.py, so grok's parse loss
is now retried and a residual even split escalates instead of silently resolving to False.

SAFETY: default prints the PLAN, 0 calls. --go spends tokens (~30-60 fast/mid-model calls,
budget < $2). Requires $OPENROUTER_API_KEY. Writes a NEW dated dir (report immutability);
NEVER writes into 20260710-floor-rerun/. Canary re-used, never re-minted. FOREGROUND only.

    python surgical_rerun.py            # dry: plan + persisted-cell inventory
    python surgical_rerun.py --go       # real calls (persisted re-grades + 3 fresh deepseek)
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys

HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import (  # noqa: E402
    load_items, scorer_kind, CONTESTED, OPEN, run,
    OpenRouterModelClient, OpenRouterError, EXAMINEE_SYSTEM,
    JudgePanel, template_hash,
    OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE,
    load_manifest, manifest_is_fresh,
    parse_ranking,
)
from wcfbench.contested import (  # noqa: E402
    score_contested_position, settled_core_keypoints, _parse_core_verdicts,
)
from wcfbench.judge import JudgeError  # noqa: E402

CANARY = "WCFBENCH-CANARY-c1647-x9k4q"
BANK_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "05-BANK-YAML"))
FLOOR_RERUN_DIR = os.path.normpath(os.path.join(
    HARNESS_ROOT, "..", "07-PILOTS", "20260710-floor-rerun"))
PERSISTED_TRANSCRIPTS = os.path.join(FLOOR_RERUN_DIR, "transcripts.jsonl")
COMBINED_MANIFEST = os.path.normpath(os.path.join(
    HARNESS_ROOT, "..", "07-PILOTS", "20260710-third-family-screen",
    "20260710-third-family-manifest.json"))
OUT_DIR = os.path.normpath(os.path.join(
    HARNESS_ROOT, "..", "07-PILOTS", "20260710-surgical-rerun"))

LLAMA = "meta-llama/llama-3.1-8b-instruct"
DEEPSEEK = "deepseek/deepseek-chat"
JUDGE_MAX_TOKENS = 2048

# The memo-directed cells.
PERSISTED_GROK_ONLY = (LLAMA, "AGG-C8-W305")          # (a) grok only, persisted text
PERSISTED_ALL3 = (DEEPSEEK, "WHOLE-C9-W301")          # (b) all 3 judges, persisted text
FRESH_DEEPSEEK = ["AGG-C3-W302", "AGG-C5-W304", "AGG-C8-W305"]   # (c) fresh SUT calls


# ---------------------------------------------------------------------------
# Persisted-transcript reader.
# ---------------------------------------------------------------------------

def _load_persisted():
    """Return {(model, item_id): record} from the frozen floor-rerun transcripts."""
    recs = {}
    with open(PERSISTED_TRANSCRIPTS) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            recs[(r["model"], r["item_id"])] = r
    return recs


class _PersistedResponseClient:
    """A .complete seam that ignores the prompt and returns a FROZEN persisted SUT
    response — so a re-grade uses the SAME sample of record (no new SUT call, no drift)."""

    def __init__(self, text):
        self._text = text
        self.call_count = 0
        self.total_tokens = 0
        self.last_finish_reason = "stop"
        self.last_truncated = False

    def complete(self, prompt, item_id=None):
        return self._text


# ---------------------------------------------------------------------------
# Panel construction from the manifest.
# ---------------------------------------------------------------------------

def _roster(manifest):
    return [(j["name"], j["family"], j["slug"])
            for j in manifest["judges"] if j.get("eligible_surfaces")]


def _judge_clients(roster):
    return {n: {"name": n, "family": f, "slug": s,
                "client": OpenRouterModelClient(model=s, max_tokens=JUDGE_MAX_TOKENS)}
            for n, f, s in roster}


def _build_panel(roster, manifest):
    clients = list(_judge_clients(roster).values())
    return JudgePanel(clients, k=len(clients), manifest=manifest)


def _select_items():
    items = load_items(BANK_DIR)
    by_id = {i.id: i for i in items}
    return by_id


# ---------------------------------------------------------------------------
# (a) grok-only re-grade on persisted AGG-C8 x llama + tie-break completion.
# ---------------------------------------------------------------------------

def _parse_persisted_core(record, judge_name, item):
    """Recover the per-keypoint settled-core booleans for a persisted judge by re-parsing
    its stored settled-core verdict text (the last verdict_texts entry) through the SAME
    parser the live path uses. Returns {criterion: bool}."""
    core_kps = settled_core_keypoints(item)
    for j in record.get("judges", []):
        if j["name"] == judge_name:
            texts = j.get("verdict_texts", [])
            # settled-core is the last surface emitted (disclosure, position, coherence, core)
            ctext = texts[-1] if texts else ""
            verdicts, _ = _parse_core_verdicts(ctext, core_kps, require_reason=True)
            return {kp.criterion: bool(verdicts.get(kp.criterion, False)) for kp in core_kps}
    return {}


def _regrade_grok_only(persisted, item, grok_client):
    """(a) Score grok-4.20 on the PERSISTED AGG-C8 x llama response and combine with the
    persisted gpt/gemini settled-core booleans to complete the 3-judge tie-breaker."""
    rec = persisted[PERSISTED_GROK_ONLY]
    response = rec["sut_response"]
    ranking = parse_ranking(response)
    grok_score = score_contested_position(item=item, response=response, judge=grok_client,
                                          ranking=ranking, item_id=item.id)
    core_kps = settled_core_keypoints(item)
    grok_core = {kp.criterion: bool(grok_score.settled_core.get(kp.criterion, False))
                 for kp in core_kps}
    gpt_core = _parse_persisted_core(rec, "gpt4omini", item)
    gem_core = _parse_persisted_core(rec, "gemini-flash", item)

    # apply the R40.3 aggregation rule across the now-complete 3-judge SETTLED_CORE panel.
    per_kp = {}
    for kp in core_kps:
        votes = [d.get(kp.criterion) for d in (gpt_core, gem_core, grok_core)
                 if kp.criterion in d]
        trues = sum(1 for v in votes if v)
        if len(votes) % 2 == 0 and trues == len(votes) / 2:
            agg = None    # (won't happen at n=3, but honor the rule)
        else:
            agg = trues > len(votes) / 2
        per_kp[kp.criterion] = {"votes": {"gpt4omini": gpt_core.get(kp.criterion),
                                          "gemini-flash": gem_core.get(kp.criterion),
                                          "grok-4.20": grok_core.get(kp.criterion)},
                                "aggregate": agg}
    graded = [v["aggregate"] for v in per_kp.values() if v["aggregate"] is not None]
    fraction = (sum(1 for v in graded if v) / len(graded)) if graded else None
    return {
        "cell": "AGG-C8-W305 x llama (persisted; grok re-graded, 3-judge tie-break)",
        "grok_settled_core_fraction": grok_score.settled_core_fraction,
        "grok_disclosure": grok_score.disclosure,
        "grok_coherence": grok_score.coherence,
        "grok_position_label": grok_score.position_label,
        "grok_position_defensible": grok_score.position_defensible,
        "grok_verdict_texts": list(grok_score.raw_verdicts),
        "per_keypoint": per_kp,
        "settled_core_fraction_3judge": fraction,
        "retried": grok_score.retried,
        "finish_reason": grok_score.finish_reason,
    }


# ---------------------------------------------------------------------------
# (b) all-3-judge re-grade on persisted deepseek WHOLE-C9-W301 (OPEN).
# ---------------------------------------------------------------------------

def _regrade_all3_persisted(persisted, item, panel):
    rec = persisted[PERSISTED_ALL3]
    response = rec["sut_response"]
    verdict = panel.score_open(item, response)
    return {
        "cell": "WHOLE-C9-W301 x deepseek (persisted; all 3 judges re-graded)",
        "triaxial": {"matter": verdict.triaxial.matter, "manner": verdict.triaxial.manner,
                     "end": verdict.triaxial.end},
        "headline": verdict.headline,
        "per_judge": verdict.per_judge,
        "judges_used": [list(t) for t in verdict.judges_used],
    }


# ---------------------------------------------------------------------------
# (c) fresh deepseek SUT calls for the 3 contested cells, panel-graded.
# ---------------------------------------------------------------------------

def _fresh_deepseek_contested(items_by_id, panel):
    """(c) FRESH deepseek SUT calls for the 3 contested cells via the SAME run() seam the
    floor re-run uses (identical prompt build + ranking parse + panel scoring)."""
    items = [items_by_id[iid] for iid in FRESH_DEEPSEEK]
    sut = OpenRouterModelClient(model=DEEPSEEK, system=EXAMINEE_SYSTEM, max_tokens=2048)
    report = run(items, {DEEPSEEK: sut}, panel=panel)
    out = []
    for r in report.reports[DEEPSEEK].results:
        cs = r.contested_score
        out.append({
            "cell": f"{r.item_id} x deepseek (FRESH SUT call)",
            "item_id": r.item_id,
            "error": r.error,
            "sut_response": getattr(r, "response_full", None),
            "settled_core": ({k: v for k, v in cs.settled_core.items()} if cs else None),
            "settled_core_fraction": (cs.settled_core_fraction if cs else None),
            "disclosure": (cs.disclosure if cs else None),
            "coherence": (cs.coherence if cs else None),
            "position_label": (cs.position_label if cs else None),
            "position_defensible": (cs.position_defensible if cs else None),
            "escalation": (cs.detail.get("settled_core_escalation", "") if cs else ""),
            "per_judge": (r.judge_raw if getattr(r, "judge_raw", None) else []),
        })
    return out, sut


# ---------------------------------------------------------------------------
# Plan / dry run.
# ---------------------------------------------------------------------------

def _print_plan(items_by_id, roster, manifest, persisted, api_key):
    print("=" * 78)
    print("R40.4 SURGICAL RE-RUN — PLAN (dry run; pass --go for real calls)")
    print("=" * 78)
    print(f"manifest: {manifest.get('run_dir')} | memo={manifest.get('memo')} | "
          f"fresh={manifest_is_fresh(manifest)}")
    print(f"panel roster (>=1 surface): {[(n, f) for n, f, _ in roster]}")
    print()
    print("PERSISTED cells (NO new SUT call — adjudicated sample preserved):")
    for (m, iid), tag in [(PERSISTED_GROK_ONLY, "(a) grok-4.20 ONLY re-graded"),
                          (PERSISTED_ALL3, "(b) all 3 judges re-graded")]:
        rec = persisted.get((m, iid))
        have = "OK" if rec and rec.get("sut_response") else "MISSING"
        n_judges = len(rec.get("judges", [])) if rec else 0
        print(f"  - {iid:14s} x {m:34s} [{have}] persisted judges={n_judges}  {tag}")
    print()
    print("FRESH deepseek SUT calls (no persisted response — the 403'd contested arm):")
    for iid in FRESH_DEEPSEEK:
        it = items_by_id.get(iid)
        knd = scorer_kind(it) if it else "?"
        print(f"  - {iid:14s} x {DEEPSEEK:34s} [{knd}]  (c)")
    print()
    print("NOT re-run: the llama arm (scored + adjudicated) — (d).")
    print(f"template_hash (settled-core prompt UNCHANGED): {template_hash()}")
    print(f"output -> {OUT_DIR}/  (NEW dated dir; floor-rerun/ is frozen)")
    est = "~2 (grok on 1 persisted contested) + ~10 (3 judges x WHOLE) + ~15 (panel x 3 contested)"
    print(f"est calls: {est}  (~30-45 fast/mid-model calls, < $2)")
    if not api_key:
        print("  ! $OPENROUTER_API_KEY not set — `source ~/.codex/secrets/openrouter.env` before --go")


# ---------------------------------------------------------------------------
# Output.
# ---------------------------------------------------------------------------

def _write_outputs(result_a, result_b, result_c, panel, manifest, sut_deepseek):
    os.makedirs(OUT_DIR, exist_ok=True)
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    th = template_hash()

    # append-only full transcript + disagreement record
    payload = {
        "canary": CANARY,
        "timestamp": ts,
        "memo": "R40.4 surgical re-run (persisted-text-first)",
        "manifest_run_dir": manifest.get("run_dir"),
        "template_hash": th,
        "judges_active": [[n, f] for n, f, _ in panel.active],
        "judges_eligibility": {n: sorted(panel.eligible.get(n, set())) for n, _, _ in panel.active},
        "judges_discarded": panel.discarded,
        "a_grok_only_persisted_agg_c8": result_a,
        "b_all3_persisted_whole_c9": result_b,
        "c_fresh_deepseek_contested": result_c,
        "deepseek_sut_usage": {"call_count": getattr(sut_deepseek, "call_count", None),
                               "total_tokens": getattr(sut_deepseek, "total_tokens", None)},
    }
    tpath = os.path.join(OUT_DIR, "transcripts.jsonl")
    with open(tpath, "w") as fh:
        fh.write(json.dumps(payload) + "\n")
    dpath = os.path.join(OUT_DIR, "disagreement.json")
    with open(dpath, "w") as fh:
        json.dump(payload, fh, indent=2)
    print(f"\n  wrote {tpath}")
    print(f"  wrote {dpath}")
    return ts, th, payload


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true", help="make the real API calls (spends tokens)")
    ap.add_argument("--manifest", default=COMBINED_MANIFEST)
    args = ap.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    manifest = load_manifest(args.manifest)
    roster = _roster(manifest)
    items_by_id = _select_items()
    persisted = _load_persisted()

    if not args.go:
        _print_plan(items_by_id, roster, manifest, persisted, api_key)
        return 0
    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY not set. `source ~/.codex/secrets/openrouter.env` first.",
              file=sys.stderr)
        return 2
    if not manifest_is_fresh(manifest):
        print("ERROR: manifest STALE (template-hash drift). Re-qualify first.", file=sys.stderr)
        return 2

    print("Building the manifest-driven panel (R35.4 — no probes at construction)…")
    try:
        panel = _build_panel(roster, manifest)
    except (OpenRouterError, JudgeError) as e:
        print(f"  PANEL UNUSABLE — {e}", file=sys.stderr)
        return 1
    print(f"  active judges: {[(n, f) for n, f, _ in panel.active]}")
    for name in [n for n, _, _ in panel.active]:
        print(f"    {name:14s} eligible={sorted(panel.eligible.get(name, set()))}")

    agg_c8_item = items_by_id["AGG-C8-W305"]
    whole_c9_item = items_by_id["WHOLE-C9-W301"]

    # (a) grok-only on persisted AGG-C8 x llama -> the completed tie-breaker.
    print("\n(a) re-grading grok-4.20 ONLY on the PERSISTED AGG-C8-W305 x llama response…")
    grok_client = OpenRouterModelClient(model="x-ai/grok-4.20", max_tokens=JUDGE_MAX_TOKENS)
    result_a = _regrade_grok_only(persisted, agg_c8_item, grok_client)
    print(f"    grok settled_core_fraction={result_a['grok_settled_core_fraction']} "
          f"retried={result_a['retried']}")
    print(f"    3-judge settled_core_fraction={result_a['settled_core_fraction_3judge']}")

    # (b) all 3 judges on persisted deepseek WHOLE-C9-W301.
    print("\n(b) re-grading ALL 3 judges on the PERSISTED deepseek WHOLE-C9-W301 response…")
    result_b = _regrade_all3_persisted(persisted, whole_c9_item, panel)
    print(f"    triaxial={result_b['triaxial']} headline={result_b['headline']} "
          f"judges={result_b['judges_used']}")

    # (c) fresh deepseek SUT calls for the 3 contested cells.
    print("\n(c) FRESH deepseek SUT calls for AGG-C3-W302 / AGG-C5-W304 / AGG-C8-W305…")
    result_c, sut_deepseek = _fresh_deepseek_contested(items_by_id, panel)
    for r in result_c:
        print(f"    [{r['item_id']}] core={r['settled_core_fraction']} disc={r['disclosure']} "
              f"coh={r['coherence']} escalation={r['escalation'] or 'none'}")

    ts, th, payload = _write_outputs(result_a, result_b, result_c, panel, manifest, sut_deepseek)
    print(f"\n  panel.discarded (transport/retry event log): {panel.discarded or 'none'}")
    print("\nSurgical re-run complete. DESCRIPTIVE / pre-gate. See the dated report.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
