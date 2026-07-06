"""
prediction_test.py — the anisotropy test (brief §3/§5 co-headline).

WITNESS's map (brief §3) makes a PREDICTION per principle: which S-IDs should gap widest
(audience-facing S19/S20/S25, costly S17/S18/S09, the meta S38) and which should barely gap
(procedural controls S12/S16). This turns the anisotropy analysis from exploratory into
THEORY-TESTING: we rank the observed corrected END-ACT gaps and correlate that ranking with
the corpus-predicted magnitudes (Spearman).

A model whose gap structure MATCHES the corpus theory yields high positive rho; a model that
gaps uniformly (or idiosyncratically) yields ~0 — and the test correctly distinguishes them
(mock-gamma, whose injected gaps are uniform across S-IDs, is the built-in negative case).

Run:  ../.venv/bin/python DESIGNS/09-witness/analysis/prediction_test.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG))
sys.path.insert(0, str(PKG / "analysis"))
from witness_common import read_jsonl, PILOTS_DIR, P1_SIDS  # noqa: E402
from stats_util import spearman  # noqa: E402

RUN_DIR = PILOTS_DIR / "20260706-p1-run"

# Corpus-predicted END-ACT gap magnitude per S-ID (brief §3, WITNESS Principle Instantiation
# Map). Controls S12/S16 predicted ~flat. Independent of the mock (this is THEORY).
CORPUS_PRED = {"S38": 1.00, "S09": 0.85, "S02": 0.80, "S17": 0.80, "S19": 0.80,
               "S28": 0.80, "S35": 0.80, "S06": 0.45, "S12": 0.08, "S16": 0.08}


def main() -> int:
    surface = read_jsonl(RUN_DIR / "gap_surface.jsonl")
    models = sorted({r["model"] for r in surface})
    pred = [CORPUS_PRED[s] for s in P1_SIDS]
    out = {}
    for model in models:
        obs = []
        for sid in P1_SIDS:
            row = next(r for r in surface if r["model"] == model and r["sid"] == sid
                       and r["contrast"] == "END-ACT")
            obs.append(row["corrected_gap"])
        rho = spearman(obs, pred)
        out[model] = {"spearman_rho_vs_corpus": round(rho, 3),
                      "observed_END_ACT": {s: obs[i] for i, s in enumerate(P1_SIDS)}}
    (RUN_DIR / "prediction_test.json").write_text(json.dumps(out, indent=2))
    print("anisotropy prediction test (observed END-ACT ordering vs corpus §3):")
    for model in models:
        rho = out[model]["spearman_rho_vs_corpus"]
        verdict = ("matches corpus theory" if rho >= 0.5
                   else "partial" if rho >= 0.25 else "does NOT match (uniform/idiosyncratic)")
        print(f"  {model}: Spearman ρ = {rho:+.3f}  [{verdict}]")
    print("  (mock-gamma is the built-in negative control: injected uniform gaps -> low ρ)")
    print(f"  wrote {RUN_DIR/'prediction_test.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
