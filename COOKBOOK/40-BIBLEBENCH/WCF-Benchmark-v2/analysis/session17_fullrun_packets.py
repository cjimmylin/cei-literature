#!/opt/homebrew/opt/python@3.14/bin/python3.14
"""Session-17 full-run INCREMENTAL strict-v2 judge-packet renderer.

For every existing session17_fullrun_runner response record
(logs/20260725-session17-fullrun/responses-<tag>-ep<N>.jsonl), render the FROZEN
strict-v2 judge prompt via the EXISTING machinery
(session15_bench_packets.render_strict_v2_prompt) — never re-implemented:

    question   = the SAME sample.input the SUT saw (record_to_sample(rec).input)
    completion = the SUT response completion (from the s17 responses JSONL)
    criterion  = render_standard(item_record)            (wcf_tasks)
    metadata   = sample.metadata

Incremental + concurrency-safe: render_all() writes each packet
    /tmp/wcf-s17-fullrun/packets/<ITEM>__<tag>__ep<N>.md
ATOMICALLY (tmp file in the same dir + os.replace) only if missing, so several
sol-driver streams can call render_all() without producing torn packets, and a
mid-run call renders only the newly-arrived responses.

CRITICAL ANTI-LEAKAGE RULE: each packet contains ONLY the rendered judge prompt.
No scores, no manifest data, no reference to this session's design. Empty
completions still render (judges floor them).

SAFETY GATE (import-time): the strict-v2 template sha256 must equal the frozen
value c32fee45652008e724c304a3e6df8c1d4ee43b055a7439d826f1ab0048d6e650, else the
module refuses to import.

Interpreter: /opt/homebrew/opt/python@3.14/bin/python3.14
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
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
BANK_VERSION_FILE = WCF_ROOT / "data" / "BANK-VERSION.json"
RESP_DIR = WCF_ROOT / "logs" / "20260725-session17-fullrun"
OUT_DIR = Path("/tmp/wcf-s17-fullrun/packets")

TEMPLATE_V2 = WCF_ROOT / "src" / "templates" / "wcf_grade_template_strict_v2.txt"
STRICT_V2_SHA256 = "c32fee45652008e724c304a3e6df8c1d4ee43b055a7439d826f1ab0048d6e650"

# Tags produced by session17_fullrun_runner (response file suffixes).
SUT_TAGS = ["gpt-4o-mini", "gpt-5-mini", "minimax-m3", "qwen", "haiku"]
EPOCHS = [1, 2, 3]

# --------------------------------------------------------------------------- #
# Import-time SAFETY GATE: strict-v2 template integrity
# --------------------------------------------------------------------------- #
_actual_sha = hashlib.sha256(TEMPLATE_V2.read_bytes()).hexdigest()
assert _actual_sha == STRICT_V2_SHA256, (
    f"strict-v2 template sha256 mismatch: expected {STRICT_V2_SHA256}, "
    f"got {_actual_sha} — refusing to render (instrument is FROZEN)")


# --------------------------------------------------------------------------- #
# Per-item question / criterion / metadata precomputed once (all scored items)
# --------------------------------------------------------------------------- #
def _load_per_item() -> dict:
    records = [json.loads(l) for l in DATA_FILE.read_text().splitlines() if l.strip()]
    g4 = set(json.loads(BANK_VERSION_FILE.read_text()).get("g4_excluded_new_items", []))
    scoped = [r for r in records if r["id"] not in g4]
    per_item = {}
    for rec in scoped:
        sample = record_to_sample(rec)
        per_item[rec["id"]] = {
            "question": sample.input,
            "criterion": render_standard(rec),
            "metadata": sample.metadata,
        }
    return per_item


_PER_ITEM_CACHE: dict | None = None


def _per_item() -> dict:
    global _PER_ITEM_CACHE
    if _PER_ITEM_CACHE is None:
        _PER_ITEM_CACHE = _load_per_item()
    return _PER_ITEM_CACHE


def _atomic_write(path: Path, text: str) -> None:
    """Write via a tmp file in the same dir + os.replace (atomic on POSIX)."""
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)  # cleanup of our OWN just-created tmp on failure only
        except OSError:
            pass
        raise


# --------------------------------------------------------------------------- #
# render_all — incremental, importable, concurrency-safe
# --------------------------------------------------------------------------- #
def render_all() -> dict:
    """Render every not-yet-rendered (item, tag, epoch) packet. Returns counts."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    per_item = _per_item()

    rendered = skipped = total = 0
    for tag in SUT_TAGS:
        for epoch in EPOCHS:
            path = RESP_DIR / f"responses-{tag}-ep{epoch}.jsonl"
            if not path.exists():
                continue
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue  # torn append tail; picked up next cycle
                item_id = row.get("id")
                if item_id is None or item_id not in per_item:
                    continue
                total += 1
                out_path = OUT_DIR / f"{item_id}__{tag}__ep{epoch}.md"
                if out_path.exists():
                    skipped += 1
                    continue
                completion = row.get("completion") or ""  # empty still renders
                info = per_item[item_id]
                prompt, _answer = render_strict_v2_prompt(
                    question=info["question"],
                    completion=completion,
                    criterion=info["criterion"],
                    metadata=info["metadata"],
                )
                _atomic_write(out_path, prompt)
                rendered += 1
    return {"rendered": rendered, "skipped": skipped, "total": total}


def main() -> None:
    counts = render_all()
    print(f"[s17-packets] rendered={counts['rendered']} "
          f"skipped={counts['skipped']} total={counts['total']} -> {OUT_DIR}")


if __name__ == "__main__":
    main()
