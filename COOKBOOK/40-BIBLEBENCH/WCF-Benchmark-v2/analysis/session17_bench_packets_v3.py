"""Session-17: render the 20-cell successor truth bench under the STRICT-v3
candidate instrument, for BLIND single-packet grading by judge agents.

NO API of any kind. Mirrors session15_bench_packets.render_strict_v2_prompt
EXACTLY (same defang_wcf_markers -> neutralize_structural_delimiters pipeline,
same GRADE_INSTRUCTIONS, same .format contract) but swaps in the strict-v3
template text. Does NOT modify any existing script.

Cell enumeration: analysis/20260725-session16-truth-bench-v2.json -> cells.
ANTI-LEAKAGE: only the `item` and `sut` fields of each cell reach a packet;
`expected`/`band`/`class`/`note`/`status` are NEVER written out.

Two response sources:
  - qwen/haiku cells (17): discover_sut_logs() over logs/20260724-session13-
    gate-main/*.eval, criterion = render_standard(item) from session13_new_items
    (exactly session15_bench_packets.main()'s data flow).
  - gpt-4o-mini/minimax-m3 cells (3): responses-<sut>.jsonl from
    logs/20260724-session16-pilot/, criterion/question via the
    session16_pilot_packets.py pattern (wcf_main.jsonl, record_to_sample,
    render_standard).

Interpreter: /opt/homebrew/opt/python@3.14/bin/python3.14
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))
sys.path.insert(0, str(WCF_ROOT / "analysis"))

from inspect_ai.scorer._model import neutralize_structural_delimiters  # noqa: E402
from wcf_tasks import record_to_sample, render_standard, GRADE_INSTRUCTIONS  # noqa: E402
from wcf_grading import defang_wcf_markers  # noqa: E402

# Reuse s15's SUT-log discovery verbatim (qwen/haiku, keyed by eval model id).
from session15_bench_packets import discover_sut_logs  # noqa: E402

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
TRUTH_BENCH = WCF_ROOT / "analysis" / "20260725-session16-truth-bench-v2.json"
TEMPLATE_V3 = WCF_ROOT / "src" / "templates" / "wcf_grade_template_strict_v3.txt"
TEMPLATE_V2 = WCF_ROOT / "src" / "templates" / "wcf_grade_template_strict_v2.txt"
ITEMS_JSON = WCF_ROOT / "data" / "session13_new_items.json"
MAIN_JSONL = WCF_ROOT / "data" / "wcf_main.jsonl"
PILOT_DIR = WCF_ROOT / "logs" / "20260724-session16-pilot"

ARCHIVE_DIR = WCF_ROOT / "logs" / "20260725-session17-bench-v3" / "packets"
WORK_DIR = Path("/tmp/wcf-s17-bench/packets")
MANIFEST = WCF_ROOT / "logs" / "20260725-session17-bench-v3" / "RENDER-MANIFEST.json"

INTERPRETER = "/opt/homebrew/opt/python@3.14/bin/python3.14"

EVAL_SUTS = {"qwen", "haiku"}
PILOT_SUTS = {"gpt-4o-mini", "minimax-m3"}

V3_EXPECTED_SHA = "ce5c9fa507ed850df3ab7aeb1018c70e27262e9c01b167ac64e3dd363c79bf9e"
V2_EXPECTED_PREFIX = "c32fee45"

# --------------------------------------------------------------------------- #
# SAFETY GATE
# --------------------------------------------------------------------------- #
def _sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


V3_SHA = _sha256_file(TEMPLATE_V3)
V2_SHA = _sha256_file(TEMPLATE_V2)
print(f"[gate] strict-v3 sha256 = {V3_SHA}")
print(f"[gate] strict-v2 sha256 = {V2_SHA}")
if V3_SHA != V3_EXPECTED_SHA:
    raise SystemExit(
        f"[gate] FATAL: strict-v3 template sha mismatch\n"
        f"        expected {V3_EXPECTED_SHA}\n        got      {V3_SHA}")
if not V2_SHA.startswith(V2_EXPECTED_PREFIX):
    print(f"[gate] WARNING: strict-v2 sha does NOT start with {V2_EXPECTED_PREFIX!r} "
          f"(got prefix {V2_SHA[:8]!r}) -- proceeding, but investigate.")
else:
    print(f"[gate] strict-v2 prefix OK ({V2_EXPECTED_PREFIX})")

# Load the v3 template ONCE.
GRADE_TEMPLATE_STRICT_V3 = TEMPLATE_V3.read_text()


# --------------------------------------------------------------------------- #
# Render the STRICT-v3 prompt exactly as render_strict_v2_prompt, v3 template
# --------------------------------------------------------------------------- #
def render_strict_v3_prompt(question: str, completion: str, criterion: str,
                            metadata: dict | None = None):
    """Return (prompt_text, defanged_answer_seen_by_judge).

    Mirrors session15_bench_packets.render_strict_v2_prompt EXACTLY, except the
    template object is the strict-v3 instrument:
      1. defang WCF markers in the SUT completion
      2. inspect neutralize_structural_delimiters on answer/question/criterion
      3. template.format(question, answer, criterion, instructions, **metadata)
    """
    defanged = defang_wcf_markers(completion)
    answer = neutralize_structural_delimiters(defanged)
    q = neutralize_structural_delimiters(question)
    crit = neutralize_structural_delimiters(criterion)
    md = {k: v for k, v in (metadata or {}).items()
          if k not in ("question", "answer", "criterion", "instructions")}
    prompt = GRADE_TEMPLATE_STRICT_V3.format(
        question=q, answer=answer, criterion=crit,
        instructions=GRADE_INSTRUCTIONS, **md,
    )
    return prompt, answer


# --------------------------------------------------------------------------- #
# Baseline: pure template + instructions with EMPTY slots. Any scan token that
# appears here is template-legitimate and must NOT be flagged in packets.
# --------------------------------------------------------------------------- #
SCAN_TOKENS = [
    "expected", "truth-bench", "truth bench", "audit",
    "strict-v2 scored", "session16", "selection",
]


def _baseline_text() -> str:
    prompt, _ = render_strict_v3_prompt(question="", completion="", criterion="")
    return prompt.lower()


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    bench = json.loads(TRUTH_BENCH.read_text())
    cells = bench["cells"]  # enumerate (item, sut) ONLY -- never expected/band/etc

    # ------ eval-source (qwen/haiku) prep: exactly session15 main() flow ------
    items = {r["id"]: r for r in json.loads(ITEMS_JSON.read_text())}
    sut_logs = discover_sut_logs()

    # ------ pilot-source (gpt-4o-mini/minimax-m3) prep: session16 pattern ------
    records = [json.loads(l) for l in MAIN_JSONL.read_text().splitlines() if l.strip()]
    rec_by_id = {r["id"]: r for r in records}
    per_item_pilot = {}  # item_id -> {question, criterion, metadata}
    pilot_resp = {}      # sut -> {item_id -> completion}
    for sut in sorted(PILOT_SUTS):
        path = PILOT_DIR / f"responses-{sut}.jsonl"
        m = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            m[row["id"]] = row.get("completion") or ""
        pilot_resp[sut] = m
        print(f"[pilot] {sut}: {len(m)} responses from {path.name}")

    baseline = _baseline_text()
    baseline_tokens = {t for t in SCAN_TOKENS if t in baseline}
    print(f"[scan] tokens present in v3 template+instructions baseline "
          f"(NOT flagged): {sorted(baseline_tokens)}")
    flaggable = [t for t in SCAN_TOKENS if t not in baseline_tokens]

    written = []           # (item, sut, source, path, sha, nbytes, prompt)
    empty_completions = []
    for cell in cells:
        iid = cell["item"]
        sut = cell["sut"]

        if sut in EVAL_SUTS:
            source = "s13-eval"
            item = items.get(iid)
            if item is None:
                raise RuntimeError(f"item {iid} not in {ITEMS_JSON.name}")
            logmap = sut_logs.get(sut)
            if logmap is None:
                raise RuntimeError(f"no SUT log for {sut}")
            rec = logmap.get(iid)
            if rec is None:
                raise RuntimeError(f"{iid} missing from {sut} eval log")
            question = rec["question"]
            completion = rec["completion"]
            criterion = render_standard(item)          # authoritative item key
            metadata = rec["metadata"]
        elif sut in PILOT_SUTS:
            source = "pilot-jsonl"
            rec = rec_by_id.get(iid)
            if rec is None:
                raise RuntimeError(f"item {iid} not in {MAIN_JSONL.name}")
            sample = record_to_sample(rec)
            question = sample.input
            criterion = render_standard(rec)
            metadata = sample.metadata
            completion = pilot_resp[sut].get(iid)
            if completion is None:
                raise RuntimeError(f"{iid} missing from {sut} pilot responses")
        else:
            raise RuntimeError(f"unknown sut {sut!r} for item {iid}")

        if not (completion or "").strip():
            empty_completions.append(f"{iid}__{sut}")

        prompt, _answer = render_strict_v3_prompt(
            question, completion, criterion, metadata)

        pkt = prompt.encode("utf-8")
        sha = hashlib.sha256(pkt).hexdigest()
        name = f"{iid}__{sut}.md"
        (ARCHIVE_DIR / name).write_bytes(pkt)
        (WORK_DIR / name).write_bytes(pkt)
        written.append({
            "item": iid, "sut": sut, "source": source,
            "name": name, "sha256": sha, "bytes": len(pkt), "prompt": prompt,
        })

    # ---------------------- leakage scan ---------------------- #
    print(f"\n[scan] flaggable tokens (absent from baseline): {flaggable}")
    scan_hits = {t: [] for t in flaggable}
    for w in written:
        low = w["prompt"].lower()
        for t in flaggable:
            if t in low:
                scan_hits[t].append(w["name"])
    scan_clean = True
    for t in flaggable:
        hits = scan_hits[t]
        verdict = "CLEAN" if not hits else f"LEAK in {hits}"
        if hits:
            scan_clean = False
        print(f"[scan] {t!r:20s}: {verdict}")
    for t in sorted(baseline_tokens):
        print(f"[scan] {t!r:20s}: template-legitimate (skipped)")

    # ---------------------- manifest ---------------------- #
    manifest = {
        "date": "2026-07-25",
        "session": "session17-bench-v3",
        "template": {
            "path": str(TEMPLATE_V3.relative_to(WCF_ROOT)),
            "sha256": V3_SHA,
        },
        "interpreter": INTERPRETER,
        "n_cells": len(written),
        "cells": [
            {"item": w["item"], "sut": w["sut"], "source": w["source"],
             "packet": w["name"], "packet_sha256": w["sha256"],
             "packet_bytes": w["bytes"]}
            for w in written
        ],  # provenance only -- NO bands/expected/class
        "archive_dir": str(ARCHIVE_DIR.relative_to(WCF_ROOT)),
        "work_dir": str(WORK_DIR),
    }
    MANIFEST.write_text(json.dumps(manifest, indent=1))

    # ---------------------- report ---------------------- #
    print(f"\n[write] {len(written)} packets -> {ARCHIVE_DIR.relative_to(WCF_ROOT)}/")
    print(f"[write] {len(written)} packets -> {WORK_DIR}/")
    for w in written:
        print(f"  {w['name']:32s} {w['source']:12s} {w['bytes']:6d} B  {w['sha256'][:12]}")
    print(f"[write] manifest -> {MANIFEST.relative_to(WCF_ROOT)}")
    print(f"\n[verify] leakage scan {'CLEAN' if scan_clean else 'FAILED'}")
    print(f"[verify] empty completions: {empty_completions or 'none'}")

    # ---------------------- sanity diff vs s15 v2 packet ---------------------- #
    s15_pkt = (WCF_ROOT / "analysis" / "20260724-session15-bench-packets"
               / "LIB-N-006__qwen.md")
    v3_pkt = next((w for w in written if w["name"] == "LIB-N-006__qwen.md"), None)
    if s15_pkt.exists() and v3_pkt is not None:
        v2_text = s15_pkt.read_text()
        v3_text = v3_pkt["prompt"]
        # The defanged SUT completion is the load-bearing shared substring: it is
        # produced by the identical pipeline, so it must appear byte-identically
        # in both v2 and v3 packets. Extract via the s13 eval record.
        rec = sut_logs["qwen"]["LIB-N-006"]
        _, answer_seen = render_strict_v3_prompt(
            rec["question"], rec["completion"],
            render_standard(items["LIB-N-006"]), rec["metadata"])
        probe = answer_seen.strip()[:400]
        in_v2 = probe in v2_text
        in_v3 = probe in v3_text
        print(f"\n[sanity] LIB-N-006__qwen: SUT-completion substring "
              f"(first 400 chars) in v2 packet={in_v2}, in v3 packet={in_v3}, "
              f"identical_and_present={in_v2 and in_v3}")
        print(f"[sanity] v2 bytes={len(v2_text.encode('utf-8'))}, "
              f"v3 bytes={v3_pkt['bytes']} (differ by template = "
              f"{v3_pkt['bytes'] - len(v2_text.encode('utf-8')):+d} B)")
    else:
        print(f"\n[sanity] SKIPPED (s15 packet exists={s15_pkt.exists()}, "
              f"v3 packet found={v3_pkt is not None})")


if __name__ == "__main__":
    main()
