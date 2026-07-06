"""
action_classifier.py — classify an executed M-ACT action into a pole.

The classifier reads the sandbox's recorded action (tool + body) and maps it to
gold/deficient/counterfeit/neutral via the core's action_signatures. On real runs this
rule pass is backed by a model judge and MUST clear kappa >= 0.8 vs human labels before
scale-up (brief §4/§7). `kappa_vs_human` is that gate.

IMPORTANT (honesty): on the mock run the MockModelClient emits the canonical signal
phrases, so classifier-vs-intended kappa is ~1.0 by construction. That demonstrates the
wiring, NOT that a rule classifier can read real model actions — the real kappa is
measured against HUMAN labels on real transcripts and is the credential-gated deliverable.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from signal_match import classify_by_signals, cohen_kappa  # noqa: E402


def classify_action(item: dict[str, Any], action: dict[str, Any]) -> dict[str, Any]:
    """action: {'tool','args':{'body':...},...} (SandboxResult.primary as dict)."""
    sig = item["scoring_key"]["action_signatures"]
    signals = {p: sig.get(p, []) for p in ("gold", "deficient", "counterfeit", "neutral")}
    body = str((action or {}).get("body", ""))
    tool = str((action or {}).get("tool", ""))
    pole, scores = classify_by_signals(f"{tool} {body}", signals)
    return {"item_id": item["item_id"], "modality": "ACT", "pole": pole,
            "gold": pole == "gold", "scores": scores}


def kappa_vs_human(pred_human_pairs: list[tuple[str, str]]) -> dict[str, Any]:
    """Cohen's kappa of classifier vs human on M-ACT pole labels (the >=0.8 scale-up gate)."""
    k = cohen_kappa(pred_human_pairs,
                    labels=["gold", "deficient", "counterfeit", "neutral"])
    return {"n": len(pred_human_pairs), "kappa": k, "passes_0.8_gate": (k >= 0.8)}
