"""
shortcut_audit.py — 'solvable-without-the-moral-content' audit for M-REC (KB Step 2).

If the gold REC option can be picked by a superficial feature — being the longest, or
sharing the most words with the situation — then a model could score well without any moral
discrimination (18% of ETHICS-deontology items are physics-solvable [2024-Hancox-Li]). We
run two lexical baselines over the REC options and check they score near chance (25% for
4 options). A baseline that beats chance flags cores whose gold is lexically marked; those
should be rewritten (rotate option lengths / wording).

Run:  ../.venv/bin/python DESIGNS/09-witness/audits/shortcut_audit.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from witness_common import load_cores, ITEMBANK_DIR, AUDITS_DIR, write_jsonl  # noqa: E402

_WORD = re.compile(r"[a-z']+")


def _toks(s: str) -> set[str]:
    return set(_WORD.findall(s.lower()))


def main() -> int:
    cores = load_cores(ITEMBANK_DIR / "cores.jsonl")
    n = len(cores)
    longest_gold = 0          # times the longest option is the gold
    overlap_gold = 0          # times the max situation-overlap option is the gold
    rows = []
    for c in cores:
        opts = {"gold": c.rec_gold, "deficient": c.rec_deficient,
                "counterfeit": c.rec_counterfeit, "neutral": c.rec_neutral}
        # length baseline
        longest = max(opts, key=lambda p: len(opts[p]))
        # situation word-overlap baseline
        sit = _toks(c.situation)
        overlap = max(opts, key=lambda p: len(_toks(opts[p]) & sit))
        lg = (longest == "gold")
        og = (overlap == "gold")
        longest_gold += lg
        overlap_gold += og
        rows.append({"core_id": c.core_id, "longest_is_gold": lg,
                     "overlap_is_gold": og,
                     "gold_len": len(c.rec_gold),
                     "lens": {p: len(t) for p, t in opts.items()}})
    write_jsonl(rows, AUDITS_DIR / "shortcut_audit.jsonl")
    len_acc = longest_gold / n
    ovl_acc = overlap_gold / n
    # chance = 0.25; flag if a baseline is materially above chance (> 0.40)
    ok = (len_acc <= 0.40) and (ovl_acc <= 0.40)
    print(f"shortcut audit over {n} REC cores (chance = 0.25):")
    print(f"  longest-option baseline accuracy : {len_acc:.2f}")
    print(f"  situation-overlap baseline acc.  : {ovl_acc:.2f}")
    print(f"  GATE (both <= 0.40): {'PASS' if ok else 'FAIL — gold is lexically marked; rotate option wording'}")
    print(f"  wrote {AUDITS_DIR / 'shortcut_audit.jsonl'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
