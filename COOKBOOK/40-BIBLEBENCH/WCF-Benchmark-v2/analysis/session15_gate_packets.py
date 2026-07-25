"""Session-15 Gate Packets: render one STRICT-v2 blind judge prompt for every
cell in the full 80-item × 2-SUT gate sweep (160 cells total).

This script imports and reuses render_strict_v2_prompt and discover_sut_logs
from session15_bench_packets.py — it does NOT fork that machinery.

Output: analysis/20260724-session15-gate-packets/<ITEM>__<sut>.md
Each file contains ONLY the rendered blind judge prompt (scenario, model
response between BEGIN/END markers, key/rubric, discipline blocks, terminal
GRADE line). No scores, no audit references, no truth-bench fields.

Deterministic. No API calls. No network. Run with OPENROUTER_API_KEY unset.
Interpreter: /opt/homebrew/opt/python@3.14/bin/python3.14
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))
sys.path.insert(0, str(WCF_ROOT / "analysis"))

# Reuse all rendering machinery from the bench-packets script — no forking.
from session15_bench_packets import (  # noqa: E402
    render_strict_v2_prompt,
    discover_sut_logs,
    SUT_MODEL_ID,
)
from wcf_tasks import render_standard  # noqa: E402

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
ITEMS_JSON = WCF_ROOT / "data" / "session13_new_items.json"
OUT_DIR = WCF_ROOT / "analysis" / "20260724-session15-gate-packets"

SUT_KEYS = list(SUT_MODEL_ID.keys())  # ["qwen", "haiku"]


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    items_list = json.loads(ITEMS_JSON.read_text())
    items = {r["id"]: r for r in items_list}
    print(f"[gate] Loaded {len(items)} items from {ITEMS_JSON.name}")

    sut_logs = discover_sut_logs()  # {sut_key -> {item_id -> {question, completion, ...}}}

    written: list[tuple[Path, int]] = []
    missing: list[tuple[str, str]] = []

    for item_id, item in sorted(items.items()):
        criterion = render_standard(item)
        for sut in SUT_KEYS:
            logmap = sut_logs[sut]
            rec = logmap.get(item_id)
            if rec is None:
                missing.append((item_id, sut))
                print(f"[MISSING] {item_id} / {sut}")
                continue

            prompt, _answer_seen = render_strict_v2_prompt(
                rec["question"], rec["completion"], criterion, rec["metadata"]
            )

            out_path = OUT_DIR / f"{item_id}__{sut}.md"
            out_path.write_text(prompt)
            written.append((out_path, len(prompt.encode("utf-8"))))

    # Summary
    print(f"\nWrote {len(written)} packets to {OUT_DIR.relative_to(WCF_ROOT)}/")
    if missing:
        print(f"MISSING RESPONSES ({len(missing)}):")
        for iid, sut in missing:
            print(f"  {iid} / {sut}")
    else:
        print("No missing responses.")

    # Per-SUT counts
    for sut in SUT_KEYS:
        n = sum(1 for p, _ in written if p.name.endswith(f"__{sut}.md"))
        print(f"  {sut}: {n} packets")

    # Size stats
    if written:
        sizes = [nb for _, nb in written]
        print(f"  min size: {min(sizes)} bytes")
        print(f"  max size: {max(sizes)} bytes")


if __name__ == "__main__":
    main()
