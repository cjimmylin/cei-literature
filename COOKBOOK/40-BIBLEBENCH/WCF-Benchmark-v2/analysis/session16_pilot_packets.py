"""Session-16 pilot judge-packet rendering.

For every (item, SUT) response produced by session16_pilot_runner.py, render the
FROZEN strict-v2 judge prompt EXACTLY via the existing machinery
(session15_bench_packets.render_strict_v2_prompt) — never re-implemented:

    question  = the SAME sample.input the SUT saw
    completion = the SUT response completion (from the s16 responses JSONL)
    criterion = render_standard(item_record)     (wcf_tasks)
    metadata  = sample.metadata

CRITICAL ANTI-LEAKAGE RULE: each packet contains ONLY the rendered judge prompt.
No scores, no manifest data, no reference to this session's design.

Interpreter: /opt/homebrew/opt/python@3.14/bin/python3.14
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))
sys.path.insert(0, str(WCF_ROOT / "analysis"))

from wcf_tasks import record_to_sample, render_standard  # noqa: E402
from session15_bench_packets import render_strict_v2_prompt  # noqa: E402

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
DATA_FILE = WCF_ROOT / "data" / "wcf_main.jsonl"
RESP_DIR = WCF_ROOT / "logs" / "20260724-session16-pilot"
OUT_DIR = Path("/tmp/wcf-s16-pilot/packets")

SUT_TAGS = ["minimax-m3", "gpt-5-mini", "gpt-4o-mini"]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    records = [json.loads(l) for l in DATA_FILE.read_text().splitlines() if l.strip()]
    n_items = {r["id"]: r for r in records if "-N-" in r["id"]}
    assert len(n_items) == 146, f"expected 146 N items, got {len(n_items)}"

    # Precompute per-item question / criterion / metadata once.
    per_item = {}
    for item_id, rec in n_items.items():
        sample = record_to_sample(rec)
        per_item[item_id] = {
            "question": sample.input,
            "criterion": render_standard(rec),
            "metadata": sample.metadata,
        }

    written = 0
    empty_completions = []
    missing = []
    for tag in SUT_TAGS:
        path = RESP_DIR / f"responses-{tag}.jsonl"
        if not path.exists():
            missing.append(tag)
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            item_id = row["id"]
            completion = row.get("completion") or ""
            if not completion.strip():
                empty_completions.append(f"{item_id}__{tag}")
            info = per_item[item_id]
            prompt, _answer = render_strict_v2_prompt(
                question=info["question"],
                completion=completion,
                criterion=info["criterion"],
                metadata=info["metadata"],
            )
            out_path = OUT_DIR / f"{item_id}__{tag}.md"
            out_path.write_text(prompt, encoding="utf-8")
            written += 1

    print(f"[s16-packets] wrote {written} packets to {OUT_DIR}")
    if missing:
        print(f"[s16-packets] SUT response files MISSING (no run yet): {missing}")
    if empty_completions:
        print(f"[s16-packets] {len(empty_completions)} EMPTY completions "
              f"(packet still rendered with empty answer): {empty_completions}")


if __name__ == "__main__":
    main()
