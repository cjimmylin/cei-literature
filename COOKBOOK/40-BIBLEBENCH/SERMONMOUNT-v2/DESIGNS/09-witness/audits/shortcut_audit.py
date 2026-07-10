"""Tie-neutral lexical shortcut and REC length-parity audit for WITNESS.

The two shortcut probes select the longest option and the option with the largest
set-overlap with situation words. Ties are reported in two order-independent ways:

* fractional credit is the expected gold accuracy under uniform tie-breaking;
* conservative credit is one whenever gold belongs to the maximizing tie.

Both versions of both probes must be at most 0.40. Every core must also satisfy
``abs(len(gold) - mean(len(distractors))) / mean(len(distractors)) <= 0.10``.

MF-4 operationalizes "no pole systematically shortest" as an authoring
counterbalance: for ``n`` cores, every pole's fractional shortest credit must lie in
``[floor(n / 4), ceil(n / 4)]``. This is an explicit mechanical operationalization,
not language quoted from the governing review.

Run:  ../.venv/bin/python DESIGNS/09-witness/audits/shortcut_audit.py
"""
from __future__ import annotations

import math
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import Mapping

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from witness_common import load_cores, ITEMBANK_DIR, AUDITS_DIR, write_jsonl  # noqa: E402


POLES = ("gold", "deficient", "counterfeit", "neutral")
SOURCE_BATCH_FILES = (
    "seed_cores.jsonl",
    "cores_batch_A.jsonl",
    "cores_batch_B.jsonl",
    "cores_batch_C.jsonl",
)
SHORTCUT_LIMIT = Fraction(2, 5)
LENGTH_PARITY_LIMIT = Fraction(1, 10)
_WORD = re.compile(r"[a-z']+")


def _toks(text: str) -> set[str]:
    return set(_WORD.findall(text.lower()))


def _ordered_poles(poles) -> tuple[str, ...]:
    present = set(poles)
    ordered = [pole for pole in POLES if pole in present]
    ordered.extend(sorted(present - set(POLES)))
    return tuple(ordered)


def extreme_poles(scores: Mapping[str, int], *, maximize: bool = True) -> tuple[str, ...]:
    """Return every maximizing/minimizing pole in canonical, mapping-independent order."""
    if not scores:
        raise ValueError("scores must not be empty")
    extreme = (max if maximize else min)(scores.values())
    return _ordered_poles(pole for pole, score in scores.items() if score == extreme)


def fractional_target_credit(
        scores: Mapping[str, int], target: str = "gold", *, maximize: bool = True) -> Fraction:
    """Expected target accuracy under uniform tie-breaking at the selected extreme."""
    winners = extreme_poles(scores, maximize=maximize)
    return Fraction(1, len(winners)) if target in winners else Fraction(0, 1)


def conservative_target_credit(
        scores: Mapping[str, int], target: str = "gold", *, maximize: bool = True) -> int:
    """Adversarial tie upper bound: one whenever target belongs to the selected tie."""
    return int(target in extreme_poles(scores, maximize=maximize))


def length_parity_fraction(options: Mapping[str, str]) -> Fraction:
    """Return the exact MF-4 gold-vs-mean-distractors character-length ratio."""
    lengths = {pole: len(options[pole]) for pole in POLES}
    distractor_sum = sum(lengths[pole] for pole in POLES if pole != "gold")
    if distractor_sum == 0:
        raise ValueError("distractor mean length must be positive")
    # |g - sum(d)/3| / (sum(d)/3) == |3g - sum(d)| / sum(d)
    return Fraction(abs(3 * lengths["gold"] - distractor_sum), distractor_sum)


def length_parity_passes(options: Mapping[str, str]) -> bool:
    return length_parity_fraction(options) <= LENGTH_PARITY_LIMIT


def shortest_balance(credits: Mapping[str, Fraction], n_cores: int) -> dict:
    """Apply the nearest-equal four-pole counterbalancing operationalization."""
    lower = math.floor(n_cores / len(POLES))
    upper = math.ceil(n_cores / len(POLES))
    ok = all(lower <= Fraction(credits.get(pole, 0)) <= upper for pole in POLES)
    return {"ok": ok, "lower": lower, "upper": upper}


def _options(core) -> dict:
    return {
        "gold": getattr(core, "rec_gold", None),
        "deficient": getattr(core, "rec_deficient", None),
        "counterfeit": getattr(core, "rec_counterfeit", None),
        "neutral": getattr(core, "rec_neutral", None),
    }


def _option_findings(core_id: str, options: Mapping[str, object]) -> list[str]:
    findings: list[str] = []
    for pole in POLES:
        value = options.get(pole)
        if not isinstance(value, str):
            findings.append(
                f"{core_id}: REC {pole} option must be a string, got {type(value).__name__}"
            )
        elif not value.strip():
            findings.append(f"{core_id}: REC {pole} option must not be empty")
    valid_values = [value.strip().casefold() for value in options.values()
                    if isinstance(value, str) and value.strip()]
    if len(valid_values) == len(POLES) and len(set(valid_values)) != len(POLES):
        findings.append(f"{core_id}: REC options must be pairwise distinct")
    return findings


def audit_core(core) -> dict:
    """Audit one core without raising on malformed options; return every finding."""
    core_id = str(getattr(core, "core_id", "<missing-core-id>"))
    options = _options(core)
    findings = _option_findings(core_id, options)
    row = {
        "core_id": core_id,
        "auditable": not findings,
        "findings": findings,
        "lens": {},
        "gold_len": None,
        "length_parity_ratio": None,
        "longest_poles": [],
        "shortest_poles": [],
        "overlap_scores": {},
        "overlap_poles": [],
        "longest_gold_fractional": None,
        "longest_gold_conservative": None,
        "overlap_gold_fractional": None,
        "overlap_gold_conservative": None,
        # Backward-compatible booleans now mean conservative tie membership.
        "longest_is_gold": None,
        "overlap_is_gold": None,
    }
    if findings:
        return row

    lengths = {pole: len(options[pole]) for pole in POLES}
    parity = length_parity_fraction(options)
    if parity > LENGTH_PARITY_LIMIT:
        row["findings"].append(
            f"{core_id}: REC length parity {float(parity):.6f} exceeds 0.100000"
        )

    situation = getattr(core, "situation", "")
    if not isinstance(situation, str):
        row["findings"].append(
            f"{core_id}: situation must be a string, got {type(situation).__name__}"
        )
        situation = ""
    situation_tokens = _toks(situation)
    overlaps = {
        pole: len(_toks(options[pole]) & situation_tokens)
        for pole in POLES
    }
    longest = extreme_poles(lengths)
    shortest = extreme_poles(lengths, maximize=False)
    overlap = extreme_poles(overlaps)
    longest_fractional = fractional_target_credit(lengths)
    longest_conservative = conservative_target_credit(lengths)
    overlap_fractional = fractional_target_credit(overlaps)
    overlap_conservative = conservative_target_credit(overlaps)

    row.update({
        "auditable": True,
        "lens": lengths,
        "gold_len": lengths["gold"],
        "length_parity_ratio": float(parity),
        "longest_poles": list(longest),
        "shortest_poles": list(shortest),
        "overlap_scores": overlaps,
        "overlap_poles": list(overlap),
        "longest_gold_fractional": float(longest_fractional),
        "longest_gold_conservative": longest_conservative,
        "overlap_gold_fractional": float(overlap_fractional),
        "overlap_gold_conservative": overlap_conservative,
        "longest_is_gold": bool(longest_conservative),
        "overlap_is_gold": bool(overlap_conservative),
    })
    return row


def _gold_credit(poles: list[str], *, conservative: bool = False) -> Fraction:
    if "gold" not in poles:
        return Fraction(0, 1)
    return Fraction(1, 1) if conservative else Fraction(1, len(poles))


def audit_bank(cores) -> dict:
    """Audit a core collection, returning all rows/findings and every MF-4 gate."""
    ordered = sorted(list(cores), key=lambda core: str(getattr(core, "core_id", "")))
    rows = [audit_core(core) for core in ordered]
    findings = [finding for row in rows for finding in row["findings"]]
    auditable = [row for row in rows if row["auditable"]]
    n = len(auditable)

    if not rows:
        findings.append("bank: expected at least one REC core")
    if not auditable:
        metrics = {
            "longest_fractional": 0.0,
            "longest_conservative": 0.0,
            "overlap_fractional": 0.0,
            "overlap_conservative": 0.0,
        }
        shortest_credits = {pole: 0.0 for pole in POLES}
        balance = shortest_balance({pole: Fraction(0, 1) for pole in POLES}, 0)
    else:
        longest_fractional = sum(
            (_gold_credit(row["longest_poles"]) for row in auditable), Fraction(0, 1)
        ) / n
        longest_conservative = sum(
            (_gold_credit(row["longest_poles"], conservative=True)
             for row in auditable), Fraction(0, 1)
        ) / n
        overlap_fractional = sum(
            (_gold_credit(row["overlap_poles"]) for row in auditable), Fraction(0, 1)
        ) / n
        overlap_conservative = sum(
            (_gold_credit(row["overlap_poles"], conservative=True)
             for row in auditable), Fraction(0, 1)
        ) / n
        exact_shortest = {
            pole: sum(
                (Fraction(1, len(row["shortest_poles"]))
                 if pole in row["shortest_poles"] else Fraction(0, 1)
                 for row in auditable),
                Fraction(0, 1),
            )
            for pole in POLES
        }
        metrics = {
            "longest_fractional": float(longest_fractional),
            "longest_conservative": float(longest_conservative),
            "overlap_fractional": float(overlap_fractional),
            "overlap_conservative": float(overlap_conservative),
        }
        shortest_credits = {pole: float(value) for pole, value in exact_shortest.items()}
        balance = shortest_balance(exact_shortest, n)

        exact_metrics = {
            "longest fractional": longest_fractional,
            "longest conservative": longest_conservative,
            "overlap fractional": overlap_fractional,
            "overlap conservative": overlap_conservative,
        }
        for label, value in exact_metrics.items():
            if value > SHORTCUT_LIMIT:
                findings.append(
                    f"bank: {label} shortcut accuracy {float(value):.6f} exceeds 0.400000"
                )
        if not balance["ok"]:
            rendered = ", ".join(
                f"{pole}={shortest_credits[pole]:g}" for pole in POLES
            )
            findings.append(
                "bank: shortest-pole balance outside "
                f"[{balance['lower']}, {balance['upper']}]: {rendered}"
            )

    return {
        "ok": not findings,
        "n_cores": len(rows),
        "n_audited": n,
        "rows": rows,
        "metrics": metrics,
        "shortest_credits": shortest_credits,
        "shortest_bounds": [balance["lower"], balance["upper"]],
        "findings": findings,
    }


def audit_source_batches(itembank_dir: Path = ITEMBANK_DIR) -> dict[str, dict]:
    """Run the complete hard gate separately on every authoring batch."""
    return {
        name: audit_bank(load_cores(itembank_dir / name))
        for name in SOURCE_BATCH_FILES
    }


def _metric_line(result: dict) -> str:
    metrics = result["metrics"]
    return (
        f"longest={metrics['longest_fractional']:.3f}/"
        f"{metrics['longest_conservative']:.3f}; "
        f"overlap={metrics['overlap_fractional']:.3f}/"
        f"{metrics['overlap_conservative']:.3f}"
    )


def main() -> int:
    result = audit_bank(load_cores(ITEMBANK_DIR / "cores.jsonl"))
    batch_results = audit_source_batches()
    write_jsonl(result["rows"], AUDITS_DIR / "shortcut_audit.jsonl")
    metrics = result["metrics"]
    print(f"shortcut audit over {result['n_cores']} REC cores (chance = 0.25):")
    print(
        "  longest-option baseline       : "
        f"fractional={metrics['longest_fractional']:.3f}; "
        f"conservative={metrics['longest_conservative']:.3f}"
    )
    print(
        "  situation-overlap baseline    : "
        f"fractional={metrics['overlap_fractional']:.3f}; "
        f"conservative={metrics['overlap_conservative']:.3f}"
    )
    credits = result["shortest_credits"]
    print(
        "  fractional shortest credits  : "
        + ", ".join(f"{pole}={credits[pole]:g}" for pole in POLES)
        + f"; bounds={result['shortest_bounds']}"
    )
    print("  per-authoring-batch gates:")
    for name, batch in batch_results.items():
        batch_credits = ",".join(
            f"{pole[0]}={batch['shortest_credits'][pole]:g}" for pole in POLES
        )
        print(
            f"    {name}: {'PASS' if batch['ok'] else 'FAIL'}; "
            f"{_metric_line(batch)}; shortest={batch_credits}; "
            f"bounds={batch['shortest_bounds']}"
        )
    if result["findings"]:
        print("  MERGED FINDINGS:")
        for finding in result["findings"]:
            print("   -", finding)
    for name, batch in batch_results.items():
        if batch["findings"]:
            print(f"  {name} FINDINGS:")
            for finding in batch["findings"]:
                print("   -", finding)
    overall_ok = result["ok"] and all(batch["ok"] for batch in batch_results.values())
    print(
        "  GATE (all four shortcut metrics <= 0.40; per-core parity <= 0.10; "
        "shortest balanced; merged + every authoring batch): "
        f"{'PASS' if overall_ok else 'FAIL'}"
    )
    print(f"  wrote {AUDITS_DIR / 'shortcut_audit.jsonl'}")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
