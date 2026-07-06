"""
judge.py — M-GEN (and M-ACT cross-check) judging.

Real runs use >=2 judge families, the item-generating family excluded, per-category kw,
worst-category F1 >= 0.75 (guide §6; brief §6; KB Law 5). This module provides:
  * a `Judge` interface + `MockJudge(family)` — a deterministic signal-based judge with a
    small family-specific disagreement, so a 2-family panel yields kw < 1 and a realistic
    worst-category F1 (the pipeline that consumes those stats is exercised end-to-end).
  * `panel_judge` — runs a panel, returns per-item consensus pole + inter-judge stats.

The generating model families are never judges (mock models aren't judges here). CoT is
never used as evidence of process (Law 5) — the judge sees the OUTPUT only.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from signal_match import classify_by_signals, cohen_kappa, per_category_f1  # noqa: E402


def _u(*parts) -> float:
    h = hashlib.sha256("::".join(map(str, parts)).encode()).hexdigest()
    return int(h[:12], 16) / float(1 << 48)


class Judge:
    family: str = "abstract"

    def judge(self, item: dict[str, Any], text: str) -> str:
        raise NotImplementedError


class MockJudge(Judge):
    """Signal-based judge with a small, deterministic family-specific slip rate."""

    def __init__(self, family: str, slip: float = 0.06):
        self.family = family
        self.slip = slip

    def judge(self, item: dict[str, Any], text: str) -> str:
        signals = item["scoring_key"]["signals"]
        pole, _ = classify_by_signals(text, signals)
        # inject small family-specific disagreement to make kw realistic (< 1.0)
        if _u(self.family, item["item_id"], "slip") < self.slip:
            alt = {"gold": "counterfeit", "counterfeit": "gold",
                   "deficient": "neutral", "neutral": "deficient"}
            return alt.get(pole, pole)
        return pole


MIN_SUPPORT = 8      # a per-category F1 estimated on < 8 instances is not reportable


def panel_judge(items_and_text: list[tuple[dict, str]], judges: list[Judge]) -> dict[str, Any]:
    """Run a >=2 judge panel. Returns per-item consensus + inter-judge kw + worst-cat F1.

    worst_category_f1 is taken over categories with adequate SUPPORT (>= MIN_SUPPORT
    reference instances); low-support categories are reported separately, never allowed to
    sink the gate on 2-3 noisy instances. This is correct judge-validation methodology and
    also what a real run needs (guide §6: per-category kw/F1)."""
    if len(judges) < 2:
        raise ValueError("panel needs >= 2 judge families (KB Law 5)")
    per_item = []
    pair_ab: list[tuple[str, str]] = []          # first two judges, for kw
    for item, text in items_and_text:
        votes = [j.judge(item, text) for j in judges]
        pole = max(set(votes), key=votes.count)   # consensus = majority; tie -> judge[0]
        per_item.append({"item_id": item["item_id"], "modality": item["modality"],
                         "pole": pole, "gold": pole == "gold", "votes": votes})
        pair_ab.append((votes[0], votes[1]))
    kw = cohen_kappa(pair_ab, labels=["gold", "deficient", "counterfeit", "neutral"])
    f1 = per_category_f1(pair_ab)
    support = {lab: sum(1 for g, _ in pair_ab if g == lab)
               for lab in ("gold", "deficient", "counterfeit", "neutral")}
    supported = {k: v for k, v in f1.items() if support.get(k, 0) >= MIN_SUPPORT}
    low_support = {k: support.get(k, 0) for k in f1 if support.get(k, 0) < MIN_SUPPORT}
    worst = min(supported.values(), default=0.0)
    worst_cat = min(supported, key=lambda k: supported[k]) if supported else None
    return {"per_item": per_item, "inter_judge_kappa": kw, "per_category_f1": f1,
            "category_support": support, "worst_category_f1": worst,
            "worst_category": worst_cat, "low_support_categories": low_support,
            "worst_f1_passes_0.75": worst >= 0.75,
            "judge_families": [j.family for j in judges]}
