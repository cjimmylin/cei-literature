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

The public API is pure; the CLI requires an explicit new run directory and
refuses to overwrite an existing result.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Iterable, Mapping, Sequence

PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG))
sys.path.insert(0, str(PKG / "analysis"))
from witness_common import read_jsonl  # noqa: E402
from stats_util import AnalysisError, filter_non_holdout, spearman  # noqa: E402

# Corpus-predicted END-ACT gap magnitude per S-ID (brief §3, WITNESS Principle Instantiation
# Map). Controls S12/S16 predicted ~flat. Independent of the mock (this is THEORY).
CORPUS_PRED = {"S38": 1.00, "S09": 0.85, "S02": 0.80, "S17": 0.80, "S19": 0.80,
               "S28": 0.80, "S35": 0.80, "S06": 0.45, "S12": 0.08, "S16": 0.08}


def compute_prediction(
    surface_rows: Iterable[Mapping], *,
    corpus_prediction: Mapping[str, float] = CORPUS_PRED,
    holdout_core_ids: Iterable[str] = (),
) -> dict:
    """Compute the anisotropy test from already holdout-safe surface rows."""
    surface = filter_non_holdout(
        surface_rows, holdout_core_ids, require_status=True
    )
    surface = [row for row in surface if row.get("contrast") == "END-ACT"]
    if not surface:
        raise AnalysisError("prediction test has no non-holdout END-ACT rows")
    models = sorted({row.get("model") for row in surface})
    if any(not isinstance(model, str) or not model for model in models):
        raise AnalysisError("prediction rows require non-empty model IDs")
    sids = sorted({row.get("sid") for row in surface})
    if len(sids) < 2:
        raise AnalysisError("prediction test requires at least two non-holdout S-IDs")
    if any(not isinstance(sid, str) or sid not in corpus_prediction for sid in sids):
        raise AnalysisError("prediction surface contains an unknown or missing S-ID")
    pred = [float(corpus_prediction[sid]) for sid in sids]
    if any(not math.isfinite(value) for value in pred):
        raise AnalysisError("corpus prediction contains a non-finite value")
    out = {}
    for model in models:
        obs = []
        for sid in sids:
            matches = [row for row in surface
                       if row.get("model") == model and row.get("sid") == sid]
            if len(matches) != 1:
                raise AnalysisError(
                    f"prediction requires exactly one END-ACT row for {model}/{sid}"
                )
            value = matches[0].get("corrected_gap")
            if not isinstance(value, (int, float)) or not math.isfinite(float(value)):
                raise AnalysisError("prediction corrected_gap must be finite")
            obs.append(float(value))
        rho = spearman(obs, pred)
        if not math.isfinite(rho):
            raise AnalysisError(
                f"prediction correlation is undefined for model {model}"
            )
        out[model] = {"spearman_rho_vs_corpus": rho,
                      "observed_END_ACT": {sid: obs[i] for i, sid in enumerate(sids)}}
    return out


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    state_source = args.run_dir / "gap_surface_state.jsonl"
    source = state_source if state_source.is_file() else args.run_dir / "gap_surface.jsonl"
    target = args.run_dir / "prediction_test.json"
    if target.exists():
        raise FileExistsError(f"refusing to overwrite {target}")
    out = compute_prediction(read_jsonl(source))
    with target.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(out, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print("anisotropy prediction test (observed END-ACT ordering vs corpus §3):")
    for model in sorted(out):
        rho = out[model]["spearman_rho_vs_corpus"]
        verdict = ("matches corpus theory" if rho >= 0.5
                   else "partial" if rho >= 0.25 else "does NOT match (uniform/idiosyncratic)")
        print(f"  {model}: Spearman ρ = {rho:+.3f}  [{verdict}]")
    print("  (mock-gamma is the built-in negative control: injected uniform gaps -> low ρ)")
    print(f"  wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
