"""X2 shortcut / gaming audit (design §5, §7 P0; KB04 §6 item 5).

Two probes, one combined verdict:

  1. lexical_length_baseline  — a lexical/length-only scorer that MUST sit ~ chance. If a
     single length/word-count threshold can beat chance, the item bank leaks surface structure.
  2. FineTuneProbe            — INTERFACE ONLY (needs training infra): fine-tune on 10% of the
     bank and check it stays BELOW SOTA parity. Stubbed with a clear TODO.

Pass rule (both must hold): lexical ~ chance AND the 10%-fine-tune probe is below parity.
"""
from __future__ import annotations

from collections import Counter
from typing import List, Optional, Sequence


def _accuracy_at_threshold(feats: Sequence[float], labels: Sequence[int], thr: float, flip: bool) -> float:
    correct = 0
    for x, y in zip(feats, labels):
        pred = 1 if x >= thr else 0
        if flip:
            pred = 1 - pred
        if pred == y:
            correct += 1
    return correct / len(labels)


def _best_single_feature_accuracy(feats: Sequence[float], labels: Sequence[int]) -> float:
    """Best accuracy achievable by ANY single threshold on this feature (both polarities).

    This is deliberately adversarial: we hand the shortcut the best possible cut so that
    "~ chance" is a strong statement — even the strongest lexical cut can't beat chance.
    """
    if not feats:
        return 0.0
    candidates = sorted(set(feats))
    thresholds = [candidates[0] - 1.0] + [
        (candidates[i] + candidates[i + 1]) / 2.0 for i in range(len(candidates) - 1)
    ] + [candidates[-1] + 1.0]
    best = 0.0
    for thr in thresholds:
        for flip in (False, True):
            best = max(best, _accuracy_at_threshold(feats, labels, thr, flip))
    return best


def lexical_length_baseline(
    items: Sequence[dict], tol: float = 0.1
) -> dict:
    """Lexical/length-only baseline. `items` = [{"text": str, "label": 0|1}, ...] (binary).

    Reports the best single-threshold accuracy over two cheap features (char length, word
    count) vs the majority-class chance rate. `near_chance` (== the pass condition for this
    probe) is True iff the best lexical accuracy is within `tol` of chance.
    """
    labels = [int(it["label"]) for it in items]
    n = len(labels)
    if n == 0:
        return {"lexical_accuracy": 0.0, "chance": 0.0, "delta": 0.0, "near_chance": True,
                "n": 0}
    counts = Counter(labels)
    chance = max(counts.values()) / n  # majority-class baseline (doc 04 §4)

    char_len = [float(len(it["text"])) for it in items]
    word_cnt = [float(len(it["text"].split())) for it in items]
    lexical_acc = max(
        _best_single_feature_accuracy(char_len, labels),
        _best_single_feature_accuracy(word_cnt, labels),
    )
    delta = lexical_acc - chance
    return {
        "lexical_accuracy": lexical_acc,
        "chance": chance,
        "delta": delta,
        "near_chance": abs(delta) <= tol,
        "n": n,
    }


class FineTuneProbe:
    """INTERFACE / harness for the 10%-fine-tune probe (KB04 §6 item 5) — NOT runnable here.

    The real probe fine-tunes a model on a `fraction` slice of the bank and checks whether it
    reaches parity with SOTA on the held-out remainder. That needs training infrastructure
    (GPU, a fine-tunable checkpoint, a train/eval split harness) which is out of scope for the
    P0 analysis layer. `run()` therefore raises NotImplementedError with the TODO. Consumers
    feed the probe's eventual `below_parity` boolean into `combined_shortcut_verdict`.

    Pass rule (documented, enforced by combined_shortcut_verdict):
        the fine-tuned probe must stay BELOW SOTA parity (accuracy_probe < accuracy_sota - margin).
    """

    def __init__(self, fraction: float = 0.10, parity_margin: float = 0.02) -> None:
        self.fraction = fraction
        self.parity_margin = parity_margin

    def run(self, items: Sequence[dict], sota_accuracy: Optional[float] = None) -> dict:
        raise NotImplementedError(
            "FineTuneProbe.run requires training infrastructure (fine-tune on "
            f"{self.fraction:.0%} of the bank, then compare to SOTA parity). "
            "TODO(live): wire to a fine-tune harness; return "
            "{'probe_accuracy': float, 'sota_accuracy': float, "
            "'below_parity': probe_accuracy < sota_accuracy - parity_margin}."
        )

    def verdict_from_accuracies(self, probe_accuracy: float, sota_accuracy: float) -> dict:
        """Apply the documented pass rule once real accuracies exist (no training needed)."""
        below = probe_accuracy < (sota_accuracy - self.parity_margin)
        return {
            "probe_accuracy": probe_accuracy,
            "sota_accuracy": sota_accuracy,
            "parity_margin": self.parity_margin,
            "below_parity": below,
        }


def combined_shortcut_verdict(
    lexical_near_chance: bool, probe_below_parity: Optional[bool]
) -> dict:
    """X2 combined rule: lexical ~ chance AND 10%-fine-tune probe below parity.

    `probe_below_parity` is None when the fine-tune probe has not been run yet — in that case
    the audit is INCOMPLETE (pass is None), never silently True.
    """
    if probe_below_parity is None:
        return {
            "lexical_near_chance": lexical_near_chance,
            "probe_below_parity": None,
            "pass": None,
            "status": "incomplete: fine-tune probe not run",
        }
    passed = bool(lexical_near_chance and probe_below_parity)
    return {
        "lexical_near_chance": lexical_near_chance,
        "probe_below_parity": probe_below_parity,
        "pass": passed,
        "status": "complete",
    }
