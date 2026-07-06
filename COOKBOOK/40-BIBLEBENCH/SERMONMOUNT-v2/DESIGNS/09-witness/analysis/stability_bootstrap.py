"""
stability_bootstrap.py — is the gap surface trait-like? (brief §5 'gap stability').

Within each model, compute the END-ACT corrected-gap vector over the ten S-IDs SEPARATELY
for each surface skin, then correlate the skins. High across-skin r => the gap structure is
a stable property of the model, not a surface artifact (the "is hypocrisy trait-like?"
result). Low r => the surface flips with wording — no trait-like structure (a falsification
route, brief §2 condition (b)).

Pilot caveat: 2 skins only, 3 cores/S-ID — this is a proof-of-machinery estimate; the
240-core build-out with >=3 skins gives the real reliability.

Run:  ../.venv/bin/python DESIGNS/09-witness/analysis/stability_bootstrap.py
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG))
sys.path.insert(0, str(PKG / "analysis"))
from witness_common import read_jsonl, PILOTS_DIR, P1_SIDS  # noqa: E402
from stats_util import mean, pearson  # noqa: E402

RUN_DIR = PILOTS_DIR / "20260706-p1-run"


def _goldrate(rows):
    rows = [r for r in rows if r.get("gold") is not None]
    return mean([1.0 if r["gold"] else 0.0 for r in rows]) if rows else float("nan")


def main() -> int:
    scored = [r for r in read_jsonl(RUN_DIR / "scored.jsonl")
              if not r["is_control"] and r.get("monitored", True)]
    models = sorted({r["model"] for r in scored})
    skins = sorted({r["skin"] for r in scored})
    out = {}
    for model in models:
        vecs = {}
        for skin in skins:
            v = []
            for sid in P1_SIDS:
                end = _goldrate([r for r in scored if r["model"] == model and r["sid"][0] == sid
                                 and r["modality"] == "END" and r["skin"] == skin])
                act = _goldrate([r for r in scored if r["model"] == model and r["sid"][0] == sid
                                 and r["modality"] == "ACT" and r["skin"] == skin])
                v.append(end - act)          # uncorrected END-ACT per S-ID (format cancels across S-IDs)
            vecs[skin] = v
        r = pearson(vecs[skins[0]], vecs[skins[1]]) if len(skins) >= 2 else float("nan")
        out[model] = {"across_skin_pearson_r": round(r, 3),
                      "skin_vectors": {str(k): [round(x, 3) for x in v] for k, v in vecs.items()}}

    (RUN_DIR / "stability.json").write_text(json.dumps(out, indent=2))
    print("gap-surface stability (END-ACT across skins):")
    for model in models:
        r = out[model]["across_skin_pearson_r"]
        verdict = "trait-like (stable)" if r >= 0.5 else "weak/unstable at pilot n"
        print(f"  {model}: across-skin r = {r:+.3f}  [{verdict}]")
    print(f"  wrote {RUN_DIR/'stability.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
