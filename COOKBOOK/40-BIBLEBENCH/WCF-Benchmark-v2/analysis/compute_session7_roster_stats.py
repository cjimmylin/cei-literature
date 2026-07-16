#!/usr/bin/env python
"""Session-7 track-2/3 roster stats: the four new-SUT rows on bank v2.4.

SUTs: gemini-3.5-flash (quotable ONLY after the kin DiD verdict —
analysis/session7_gemini_kin_did.py), mistral-large-2512 (kin: disclose the
s5-measured +0.97 family bound), z-ai/glm-5 (substituted for the retired
glm-4.7 slug — disclosed), minimax/minimax-m3.

Per SUT, three deliverables (s6 reporting form):
  (a) full-bank mean  = all scored items in wcf_main + wcf_episodes(item)
  (b) frontier-core   = the 66 *-N-* v2.4 items (single draw here; the frontier
                        trio's epochs-averaged core index lives in
                        compute_session7_epochs_stats.py)
  (c) escalation panel (wcf_new_episodes, STANDALONE — never merged into (a))

Also: quorum-drop ledger + token usage per SUT. The panel-items-never-in-core
assertion from compute_session6_roster_stats.py is preserved.

Writes analysis/20260716-session7-roster-stats.json.
"""
from __future__ import annotations

import glob
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

from inspect_ai.log import read_eval_log

V2 = Path(__file__).resolve().parent.parent
LOGS = V2 / "logs"
SUTS = {
    "openrouter/google/gemini-3.5-flash": {
        "tag": "gemini35flash",
        "bank_dirs": ["20260716-session7-gemini-main",
                      "20260716-session7-gemini-episodes"],
        "panel_dirs": ["20260716-session7-gemini-panel"],
        "kin_note": "QUOTABLE ONLY per 20260716-session7-gemini-kin-did.json",
    },
    "openrouter/mistralai/mistral-large-2512": {
        "tag": "mistral_large",
        "bank_dirs": ["20260716-session7-roster-mistral-main",
                      "20260716-session7-roster-mistral-episodes"],
        "panel_dirs": ["20260716-session7-roster-mistral-panel"],
        "kin_note": "family kin to g3 mistral-small: +0.97 bound (s5)",
    },
    "openrouter/z-ai/glm-5": {
        "tag": "glm5",
        "bank_dirs": ["20260716-session7-roster-glm-main",
                      "20260716-session7-roster-glm-episodes"],
        "panel_dirs": ["20260716-session7-roster-glm-panel"],
        "kin_note": "substituted for retired glm-4.7 slug (2026-07-16 catalog)",
    },
    "openrouter/minimax/minimax-m3": {
        "tag": "minimax_m3",
        "bank_dirs": ["20260716-session7-roster-minimax-main",
                      "20260716-session7-roster-minimax-episodes"],
        "panel_dirs": ["20260716-session7-roster-minimax-panel"],
        "kin_note": None,
    },
}


def read_dir_scores(dirs: list[str], model: str):
    """scores[item_id] = float (last-file-wins), plus unscored/quorum/usage."""
    scores: dict[str, float] = {}
    unscored, quorum_drops, statuses = [], [], []
    usage = defaultdict(lambda: [0, 0])
    for d in dirs:
        for f in sorted(glob.glob(str(LOGS / d / "*.eval"))):
            log = read_eval_log(f)
            if log.eval.model != model:
                continue
            statuses.append((Path(f).name[:44], log.status, len(log.samples or [])))
            for m, u in (log.stats.model_usage or {}).items():
                usage[m][0] += u.input_tokens
                usage[m][1] += u.output_tokens
            for s in (log.samples or []):
                for sc in (s.scores or {}).values():
                    panel = (sc.metadata or {}).get("panel") or {}
                    if panel.get("n_valid", 3) < 3:
                        quorum_drops.append(str(s.id))
                    try:
                        v = float(sc.value)
                    except (TypeError, ValueError):
                        v = float("nan")
                    if v != v:
                        unscored.append(str(s.id))
                    else:
                        scores[str(s.id)] = v
    return scores, unscored, quorum_drops, statuses, dict(usage)


def main() -> int:
    out = {"bank_version": "v2.4",
           "panel": "gemini-2.5-flash + deepseek-chat + mistral-small-2603 "
                    "(median, last-match parser, excellence gate ON main)",
           "note": "EXPLORATORY / NON-QUOTABLE; rubric conformity 0-100, "
                   "not accuracy. Frontier-trio epochs-averaged core index in "
                   "20260716-session7-epochs-stats.json.",
           "suts": {}}
    for model, cfg in SUTS.items():
        bank, uns_b, qd_b, st_b, use_b = read_dir_scores(cfg["bank_dirs"], model)
        panel, uns_p, qd_p, st_p, use_p = read_dir_scores(cfg["panel_dirs"], model)
        assert not any(i.startswith("NARROW-N") for i in bank), \
            "panel items leaked into bank scores"
        core = {i: v for i, v in bank.items() if "-N-" in i}
        row = {
            "kin_note": cfg["kin_note"],
            "n_bank_scored": len(bank),
            "full_bank_mean": round(mean(bank.values()), 2) if bank else None,
            "full_bank_stderr": round(stdev(bank.values()) / math.sqrt(len(bank)), 2)
            if len(bank) > 1 else None,
            "n_core": len(core),
            "frontier_core_mean": round(mean(core.values()), 2) if core else None,
            "frontier_core_stderr": round(stdev(core.values()) / math.sqrt(len(core)), 2)
            if len(core) > 1 else None,
            "escalation_panel_mean": round(mean(panel.values()), 2) if panel else None,
            "n_panel_scored": len(panel),
            "unscored_bank": uns_b, "unscored_panel": uns_p,
            "quorum_drops_bank": len(qd_b), "quorum_drops_panel": len(qd_p),
            "log_statuses": st_b + st_p,
            "usage_tokens": {m: {"in": io[0], "out": io[1]}
                             for m, io in {**use_b, **use_p}.items()},
        }
        out["suts"][cfg["tag"]] = row
    dest = V2 / "analysis" / "20260716-session7-roster-stats.json"
    dest.write_text(json.dumps(out, indent=1))
    for tag, r in out["suts"].items():
        print(f"{tag:14s} bank {r['full_bank_mean']} (n={r['n_bank_scored']}) | "
              f"core {r['frontier_core_mean']} (n={r['n_core']}) | "
              f"panel {r['escalation_panel_mean']} | unscored "
              f"{len(r['unscored_bank'])}/{len(r['unscored_panel'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
