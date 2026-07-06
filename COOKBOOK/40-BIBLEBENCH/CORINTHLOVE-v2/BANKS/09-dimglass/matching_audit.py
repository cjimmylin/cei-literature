#!/usr/bin/env python3
"""Matched-arm symmetry audit for DIMGLASS d2-d3 twins (brief §11 item 2, D-16).

C3 (rubric): where the design uses matched conditions, the two arms must differ
ONLY in the manipulated variable (evidence validity). This audit renders every
d2/d3 valid/invalid twin, tabulates surface features per arm (word count, char
count, digit count, citation markers, hedge words, sentence count), and asserts:

  * mean SIGNED word-count diff (valid - invalid) ~ 0  (no systematic direction),
  * max ABS word-count diff within tolerance,
  * per-pair char/digit/citation/hedge diffs within tolerance,

failing loud on any systematic asymmetry. Emits reports/arm_symmetry_table.md.

The audit works directly on generated twins so it reflects the SHIPPED text.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

_CIT_RE = re.compile(r"§|\bdoc\b|\brow\b|\bsource\b|\brecord\b|\blog\b|\bnote\b|\btable\b|\bfootnote\b|\bannex\b|\breference\b",
                     re.IGNORECASE)
_HEDGE_RE = re.compile(r"\bmaybe\b|\bmildly\b|\bslightly\b|\bweakly\b|\bnudge|\btilt|\bhint|\blean|\bsmall\b",
                       re.IGNORECASE)

TOL = {
    "word_mean_signed": 0.75,   # |systematic| direction must be ~0
    "word_max_abs": 3,
    "char_mean_signed": 6.0,
    "char_max_abs": 24,
    "digit_max_abs": 2,
    "cit_max_abs": 1,
    "hedge_max_abs": 1,
}


def features(text: str):
    words = text.split()
    n_sent = len(re.findall(r"[.!?]", text)) or 1
    return {
        "words": len(words),
        "chars": len(text),
        "digits": sum(c.isdigit() for c in text),
        "cit": len(_CIT_RE.findall(text)),
        "hedge": len(_HEDGE_RE.findall(text)),
        "sent": n_sent,
    }


def run(bank_dir=None, assert_ok=True):
    import yaml
    bank_dir = bank_dir or os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(bank_dir, "episodes", "private_bank.yaml")) as f:
        priv = yaml.safe_load(f)
    with open(os.path.join(bank_dir, "seeds_public.yaml")) as f:
        pub = yaml.safe_load(f)
    episodes = {e["id"]: e for e in (priv + pub)}
    with open(os.path.join(bank_dir, "sidecar", "pair_registry.json")) as f:
        pair_registry = json.load(f)

    # per (domain,dose) accumulate diffs
    per_group = defaultdict(lambda: defaultdict(list))
    pair_rows = []
    for split, pairs in pair_registry.items():
        for pid, pr in pairs.items():
            ev = episodes[pr["valid"]]
            ei = episodes[pr["invalid"]]
            dose = ev["parameters"]["round_1"]["dose"]
            domain = ev["parameters"]["domain"]
            fv = features(ev["multiturn_script"]["stage_2"])
            fi = features(ei["multiturn_script"]["stage_2"])
            for k in fv:
                per_group[(domain, dose)][k].append(fv[k] - fi[k])
            pair_rows.append((domain, dose, split, fv, fi))

    # aggregate + assert
    lines = ["# DIMGLASS d2-d3 matched-arm symmetry audit",
             "",
             "Arms differ ONLY in evidence validity (claim clause + counter token).",
             "Diffs are (valid arm) minus (invalid arm), per matched pair.",
             "",
             "| domain | dose | n_pairs | word Δ mean(signed) | word Δ max|abs| | "
             "char Δ mean | char Δ max|abs| | digit max|abs| | cit max|abs| | hedge max|abs| |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    failures = []
    for (domain, dose), feats in sorted(per_group.items()):
        n = len(feats["words"])
        wmean = sum(feats["words"]) / n
        wmax = max(abs(x) for x in feats["words"])
        cmean = sum(feats["chars"]) / n
        cmax = max(abs(x) for x in feats["chars"])
        dmax = max(abs(x) for x in feats["digits"])
        citmax = max(abs(x) for x in feats["cit"])
        hmax = max(abs(x) for x in feats["hedge"])
        lines.append(f"| {domain} | {dose} | {n} | {wmean:+.3f} | {wmax} | "
                     f"{cmean:+.2f} | {cmax} | {dmax} | {citmax} | {hmax} |")
        if abs(wmean) > TOL["word_mean_signed"]:
            failures.append(f"{domain}/{dose}: word mean-signed {wmean:+.3f} exceeds {TOL['word_mean_signed']}")
        if wmax > TOL["word_max_abs"]:
            failures.append(f"{domain}/{dose}: word max-abs {wmax} exceeds {TOL['word_max_abs']}")
        if abs(cmean) > TOL["char_mean_signed"]:
            failures.append(f"{domain}/{dose}: char mean-signed {cmean:+.2f} exceeds {TOL['char_mean_signed']}")
        if cmax > TOL["char_max_abs"]:
            failures.append(f"{domain}/{dose}: char max-abs {cmax} exceeds {TOL['char_max_abs']}")
        if dmax > TOL["digit_max_abs"]:
            failures.append(f"{domain}/{dose}: digit max-abs {dmax} exceeds {TOL['digit_max_abs']}")
        if citmax > TOL["cit_max_abs"]:
            failures.append(f"{domain}/{dose}: cit max-abs {citmax} exceeds {TOL['cit_max_abs']}")
        if hmax > TOL["hedge_max_abs"]:
            failures.append(f"{domain}/{dose}: hedge max-abs {hmax} exceeds {TOL['hedge_max_abs']}")

    lines += ["", f"Total matched pairs audited: {len(pair_rows)}",
              f"Tolerances: {json.dumps(TOL)}", ""]
    if failures:
        lines.append("## FAILURES")
        lines += [f"- {x}" for x in failures]
    else:
        lines.append("## RESULT: PASS — no systematic surface asymmetry between arms.")

    report = "\n".join(lines) + "\n"
    with open(os.path.join(bank_dir, "reports", "arm_symmetry_table.md"), "w") as f:
        f.write(report)

    if assert_ok:
        assert not failures, "MATCHING AUDIT FAILED:\n" + "\n".join(failures)
    return {"n_pairs": len(pair_rows), "failures": failures}


if __name__ == "__main__":
    res = run(assert_ok=True)
    print(json.dumps(res, indent=2))
