#!/usr/bin/env python
"""RP-04 S1 pilot — machinery-validation statistics.

Computes, from the judge verdicts + the held-out truth in the manifest:
  * Per family: injected-label recovery rate (judge D1 gold_signal vs the record's
    known pole-derived gold_signal), overall and by modality / pole / tier.
    Refusal + parse-failure + error + timeout counts.
  * Inter-family: Cohen's kappa on D1 over records where BOTH families produced a
    verdict; raw agreement %.
  * Wilson 95% CI on every recovery rate.
  * Machinery sanity checks (deterministic-simulator "dead giveaway" tests).

NOTHING here is a judge-bias / model-behavior number. These validate the pipeline
recovers injected labels and that agreement stats compute correctly.
"""
from __future__ import annotations

import json
import math
import os
import collections

HERE = os.path.dirname(os.path.abspath(__file__))


def wilson_ci(k, n, z=1.96):
    """Wilson score interval for a binomial proportion. Returns (lo, hi, phat)."""
    if n == 0:
        return (0.0, 0.0, None)
    phat = k / n
    denom = 1 + z * z / n
    center = (phat + z * z / (2 * n)) / denom
    half = (z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / denom
    return (max(0.0, center - half), min(1.0, center + half), phat)


def cohen_kappa(pairs):
    """pairs: list of (a, b) with a,b in {True,False}. Cohen's kappa for 2 raters,
    binary labels. Returns (kappa, po, pe, n)."""
    n = len(pairs)
    if n == 0:
        return (None, None, None, 0)
    po = sum(1 for a, b in pairs if a == b) / n
    # marginal probabilities
    a_true = sum(1 for a, b in pairs if a) / n
    b_true = sum(1 for a, b in pairs if b) / n
    pe = a_true * b_true + (1 - a_true) * (1 - b_true)
    if pe == 1.0:
        # degenerate: both raters constant & identical -> perfect agreement,
        # kappa undefined (0/0). Report None with a note.
        return (None, po, pe, n)
    kappa = (po - pe) / (1 - pe)
    return (kappa, po, pe, n)


def recovery_table(rows):
    """rows: verdict rows with final_status=='ok'. Returns dict of recovery stats
    overall and by modality/pole/tier."""
    ok = [r for r in rows if r["final_status"] == "ok" and r["gold_signal"] is not None]
    def rate(subset):
        n = len(subset)
        k = sum(1 for r in subset if bool(r["gold_signal"]) == bool(r["_truth_gold_signal"]))
        lo, hi, phat = wilson_ci(k, n)
        return {"n": n, "correct": k,
                "rate": round(phat, 4) if phat is not None else None,
                "wilson95": [round(lo, 4), round(hi, 4)]}
    out = {"overall": rate(ok)}
    for dim in ("modality", "tier"):
        out[f"by_{dim}"] = {}
        for val in sorted(set(r[dim] for r in ok)):
            out[f"by_{dim}"][val] = rate([r for r in ok if r[dim] == val])
    out["by_truth_pole"] = {}
    for val in sorted(set(r["_truth_pole"] for r in ok)):
        out["by_truth_pole"][val] = rate([r for r in ok if r["_truth_pole"] == val])
    out["by_gold_signal_class"] = {}
    for val in (True, False):
        out["by_gold_signal_class"][str(val)] = rate(
            [r for r in ok if bool(r["_truth_gold_signal"]) == val])
    return out


def status_counts(rows):
    c = collections.Counter(r["final_status"] for r in rows)
    return {k: c.get(k, 0) for k in ("ok", "refusal", "error", "timeout", "parse_failure")}


def load_merged_verdicts():
    """Merge the valid anthropic arm (original run) with the codex RE-RUN arm.

    The original run's codex arm was invalidated by external config drift
    (model_reasoning_effort='ultra' / model='gpt-5.6-sol' set in the shared
    ~/.codex/config.toml by another session), so codex exited returncode=1
    before any model call. rerun_codex.py re-ran the codex arm with per-call
    `-c` overrides. We therefore take anthropic verdicts from the first run and
    codex verdicts from the rerun.
    """
    orig = json.load(open(os.path.join(HERE, "20260709-judge-verdicts.json")))
    verdicts = [r for r in orig["verdicts"] if r["family"] == "anthropic_cli"]
    call_totals = {"anthropic_cli": orig["call_totals"]["anthropic_cli"]}
    versions = dict(orig["versions"])
    transcripts = [orig["transcript_path"]]
    tcount = orig["transcript_count"]
    codex_meta = {}
    rerun_path = os.path.join(HERE, "20260709-codex-rerun-verdicts.json")
    if os.path.exists(rerun_path):
        rr = json.load(open(rerun_path))
        verdicts += rr["verdicts"]
        call_totals["openai_cli"] = rr["calls"]
        transcripts.append(rr["transcript_path"])
        tcount += rr["transcript_count"]
        codex_meta = rr.get("codex_overrides", {})
        # count the original (broken) codex calls too for full accounting
        codex_meta["original_broken_codex_calls"] = orig["call_totals"].get("openai_cli")
    else:
        # fall back to whatever the original codex arm was (broken)
        verdicts += [r for r in orig["verdicts"] if r["family"] == "openai_cli"]
        call_totals["openai_cli"] = orig["call_totals"].get("openai_cli")
    return {"versions": versions, "verdicts": verdicts,
            "call_totals": call_totals, "transcript_path": transcripts,
            "transcript_count": tcount, "codex_meta": codex_meta}


def main():
    data = load_merged_verdicts()
    verdicts = data["verdicts"]
    families = sorted(set(r["family"] for r in verdicts))

    per_family = {}
    for fam in families:
        rows = [r for r in verdicts if r["family"] == fam]
        per_family[fam] = {
            "n_records": len(rows),
            "calls_made": data["call_totals"].get(fam),
            "status_counts": status_counts(rows),
            "recovery": recovery_table(rows),
            "model_id_reported": rows[0]["model_id"] if rows else None,
            "confidence_mean": round(
                sum(r["confidence"] for r in rows
                    if r["final_status"] == "ok" and r["confidence"] is not None)
                / max(1, sum(1 for r in rows if r["final_status"] == "ok"
                             and r["confidence"] is not None)), 4),
        }

    # Inter-family agreement on D1, records where BOTH produced a verdict.
    by_id = collections.defaultdict(dict)
    for r in verdicts:
        if r["final_status"] == "ok" and r["gold_signal"] is not None:
            by_id[r["sample_id"]][r["family"]] = bool(r["gold_signal"])
    both = [sid for sid, d in by_id.items() if len(d) == len(families)]
    f1, f2 = families[0], families[1]
    pairs = [(by_id[sid][f1], by_id[sid][f2]) for sid in both]
    kappa, po, pe, n = cohen_kappa(pairs)
    inter = {
        "families": families,
        "n_both_verdict": n,
        "raw_agreement": round(po, 4) if po is not None else None,
        "cohen_kappa": round(kappa, 4) if kappa is not None else None,
        "p_expected": round(pe, 4) if pe is not None else None,
        "kappa_note": ("kappa undefined (pe==1: both raters constant & identical) "
                       if kappa is None and n > 0 else ""),
    }

    # ---- Machinery sanity checks (deterministic-simulator dead-giveaway tests) ----
    ok_all = [r for r in verdicts if r["final_status"] == "ok" and r["gold_signal"] is not None]
    # (a) Both families should recover a DETERMINISTIC label at high rate. A low
    #     rate flags a reconstruction/prompt bug, not "bias".
    # (b) Per (sample_id) the TRUTH is fixed; if the two families disagree that is
    #     judge-interpretation variance on a fixed stimulus, NOT bias — count it.
    disagreements = [sid for sid in both if by_id[sid][f1] != by_id[sid][f2]]
    # (c) "Structure that cannot exist": since subjects are deterministic, any
    #     recovery rate SIGNIFICANTLY below the trivial baseline (predict majority
    #     class) with tight CI would indicate the pipeline is mis-wired. Report the
    #     majority-class baseline for context.
    truth_vals = [bool(r["_truth_gold_signal"]) for r in ok_all]
    maj = max(sum(truth_vals), len(truth_vals) - sum(truth_vals)) / max(1, len(truth_vals))
    sanity = {
        "n_both_verdict": len(both),
        "n_interfamily_disagreements": len(disagreements),
        "disagreement_sample_ids": disagreements,
        "majority_class_baseline": round(maj, 4),
        "interpretation": (
            "Subjects are deterministic synthetic-mock records; a fixed injected "
            "label exists per record. High recovery = the reconstruction+judge+parse "
            "pipeline correctly presents the pair and reads the verdict. Inter-family "
            "disagreements reflect judge-interpretation variance on a FIXED stimulus "
            "(rubric ambiguity / reconstruction minimality), NOT model bias. No number "
            "here is a bias, agreement-with-truth-as-behavior, or judge-quality claim."),
    }

    report = {
        "provenance": {
            "subjects": "synthetic-mock (frozen WITNESS scored.jsonl)",
            "judges": "cli-oauth-provisional",
            "versions": data["versions"],
            "validates": "re-scoring machinery ONLY",
        },
        "per_family": per_family,
        "inter_family": inter,
        "machinery_sanity": sanity,
        "transcript_path": data["transcript_path"],
        "transcript_count": data["transcript_count"],
        "call_totals": data["call_totals"],
        "codex_meta": data.get("codex_meta", {}),
    }
    out_path = os.path.join(HERE, "20260709-stats.json")
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=2)
    print(json.dumps(report, indent=2))
    print("\nwrote", out_path)


if __name__ == "__main__":
    main()
