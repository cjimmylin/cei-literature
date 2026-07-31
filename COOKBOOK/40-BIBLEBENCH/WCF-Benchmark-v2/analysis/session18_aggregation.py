#!/usr/bin/env python3
"""Session-18 A1: aggregate the session-17 Scenario-A full-run panel verdicts.

Design: 5 SUTs x 345 scored items x 3 epochs = 5,175 cells, judged by the frozen
strict-v2 two-judge panel (opus + Sol, single-packet mode, mean-of-2).

Authority model
---------------
* The 15 ``responses-<sut>-ep<n>.jsonl`` files are AUTHORITATIVE for the expected
  cell set: expected = {(item_id, sut, epoch)} read row-by-row from every file.
  ``RUN-SUMMARY.json`` per-epoch ``complete`` flags are NOT consulted (known
  cosmetic lag).
* Every integrity gate is decided by SET MEMBERSHIP, never by arithmetic on
  counts (vault Data-Integrity rule; cf. the s16 "345-28=317" error).
* Empty/blank SUT completions are DATA (they floor the judged score), not
  exclusions. No cell is ever dropped for a blank completion.

Grade contract: strict LAST-match of ``GRADE:`` in the verdict body, matching the
session-16 convention (``session16_pilot_stats.py``: ``re.findall`` then
``[-1]``). An anchored ``^GRADE:\\s*(-?\\d+)\\s*$`` pass runs alongside it as a
cross-check; a disagreement between the two is reported as a format anomaly.

Outputs (written to analysis/ and copied into the run-log dir):
  <DATE>-session18-panel.json
  <DATE>-session18-perjudge.csv

Read-only with respect to every other file. Pure stdlib, $0.

Usage:
  python3.14 analysis/session18_aggregation.py --date 20260729 [--allow-partial]
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
RUN_DIR = WCF_ROOT / "logs" / "20260725-session17-fullrun"
ANALYSIS_DIR = WCF_ROOT / "analysis"

INSTRUMENT_SHA = "c32fee45652008e724c304a3e6df8c1d4ee43b055a7439d826f1ab0048d6e650"

SUTS = ("gpt-4o-mini", "gpt-5-mini", "haiku", "minimax-m3", "qwen")
EPOCHS = (1, 2, 3)
N_ITEMS_EXPECTED = 345
N_CELLS_EXPECTED = 5175
JUDGES = ("opus", "sol")
GAP_TRIAGE_THRESHOLD = 30

# session-16 convention: unanchored scan, take the LAST match.
GRADE_RE = re.compile(r"GRADE:\s*(-?\d+)")
# anchored cross-check of the same contract
GRADE_RE_ANCHORED = re.compile(r"^GRADE:\s*(-?\d+)\s*$", re.MULTILINE)

RESPONSES_RE = re.compile(r"^responses-(?P<sut>.+)-ep(?P<epoch>\d+)\.jsonl$")


# --------------------------------------------------------------------------- #
# parsing
# --------------------------------------------------------------------------- #

def parse_grade(path: Path) -> tuple[int | None, str | None]:
    """Return (grade, anomaly). grade is None when the file does not parse."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:  # pragma: no cover - unreadable verdict
        return None, f"unreadable: {exc}"

    loose = GRADE_RE.findall(text)
    if not loose:
        return None, "no GRADE: line"

    anchored = GRADE_RE_ANCHORED.findall(text)
    anomaly = None
    if not anchored:
        anomaly = "GRADE: present but not on its own line"
    elif anchored[-1] != loose[-1]:
        anomaly = (f"last-match disagreement: unanchored={loose[-1]} "
                   f"anchored={anchored[-1]}")
    elif len(loose) > 1:
        anomaly = f"{len(loose)} GRADE: matches (used last)"

    value = int(loose[-1])
    if not 0 <= value <= 100:
        return None, f"grade out of range 0-100: {value}"
    return value, anomaly


def cell_key(item: str, sut: str, epoch: int) -> tuple[str, str, int]:
    return (item, sut, epoch)


def verdict_name(item: str, sut: str, epoch: int) -> str:
    return f"{item}__{sut}__ep{epoch}.md"


def parse_verdict_name(name: str) -> tuple[str, str, int] | None:
    stem = name[:-3] if name.endswith(".md") else name
    parts = stem.split("__")
    if len(parts) != 3:
        return None
    item, sut, ep = parts
    if not ep.startswith("ep") or not ep[2:].isdigit():
        return None
    return cell_key(item, sut, int(ep[2:]))


# --------------------------------------------------------------------------- #
# inputs
# --------------------------------------------------------------------------- #

def load_expected_cells() -> tuple[dict, dict]:
    """Expected cell set from the responses JSONLs (authoritative).

    Returns (expected_cells, detail) where expected_cells maps cell -> row info
    (currently just whether the SUT completion was blank; blanks are DATA).
    """
    files = sorted(RUN_DIR.glob("responses-*.jsonl"))
    expected: dict[tuple[str, str, int], dict] = {}
    per_file: dict[tuple[str, int], dict] = {}
    problems: list[str] = []

    for path in files:
        m = RESPONSES_RE.match(path.name)
        if not m:
            problems.append(f"{path.name}: unparseable responses filename")
            continue
        sut = m.group("sut")
        epoch = int(m.group("epoch"))
        items: list[str] = []
        blanks = 0
        epoch_mismatch = 0
        with path.open(encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    problems.append(f"{path.name}:{lineno}: bad JSON ({exc})")
                    continue
                item = row.get("id")
                if not item:
                    problems.append(f"{path.name}:{lineno}: row has no 'id'")
                    continue
                items.append(item)
                if row.get("epoch") not in (None, epoch):
                    epoch_mismatch += 1
                blank = not str(row.get("completion") or "").strip()
                if blank:
                    blanks += 1
                key = cell_key(item, sut, epoch)
                if key in expected:
                    problems.append(f"{path.name}:{lineno}: duplicate cell {key}")
                expected[key] = {"blank_completion": blank}
        if epoch_mismatch:
            problems.append(
                f"{path.name}: {epoch_mismatch} rows whose 'epoch' field "
                f"disagrees with the filename")
        per_file[(sut, epoch)] = {
            "file": path.name,
            "rows": len(items),
            "unique_items": len(set(items)),
            "blank_completions": blanks,
            "items": set(items),
        }

    return expected, {"files": per_file, "problems": problems,
                      "n_files": len(files)}


def load_verdicts(judge: str) -> tuple[dict, dict]:
    """Return (cell -> grade|None, detail) for one judge arm."""
    directory = RUN_DIR / f"{judge}-verdicts"
    grades: dict[tuple[str, str, int], int | None] = {}
    unparsed: list[str] = []
    anomalies: list[str] = []
    unnamed: list[str] = []
    for path in sorted(directory.glob("*.md")):
        key = parse_verdict_name(path.name)
        if key is None:
            unnamed.append(path.name)
            continue
        grade, anomaly = parse_grade(path)
        grades[key] = grade
        if grade is None:
            unparsed.append(f"{judge}-verdicts/{path.name}: {anomaly}")
        elif anomaly:
            anomalies.append(f"{judge}-verdicts/{path.name}: {anomaly}")
    return grades, {"unparsed": unparsed, "anomalies": anomalies,
                    "unnamed_files": unnamed,
                    "dir_exists": directory.is_dir()}


# --------------------------------------------------------------------------- #
# gates
# --------------------------------------------------------------------------- #

def by_chunk(cells) -> dict[tuple[str, int], list[str]]:
    out: dict[tuple[str, int], list[str]] = {}
    for item, sut, epoch in cells:
        out.setdefault((sut, epoch), []).append(item)
    for v in out.values():
        v.sort()
    return out


def chunk_label(sut: str, epoch: int) -> str:
    return f"{sut}-ep{epoch}"


def run_gates(expected, exp_detail, sol, sol_detail, opus, opus_detail,
              allow_partial: bool) -> dict:
    gates: dict[str, dict] = {}

    # ---- Gate 1: expected cell set shape (set membership only) ------------- #
    files = exp_detail["files"]
    item_sets = {k: v["items"] for k, v in files.items()}
    all_items: set[str] = set().union(*item_sets.values()) if item_sets else set()
    reference = item_sets.get(("gpt-4o-mini", 1))
    if reference is None and item_sets:
        reference = next(iter(item_sets.values()))
    mismatched_files = sorted(
        chunk_label(*k) for k, s in item_sets.items() if s != reference)
    bad_chunk_counts = sorted(
        f"{chunk_label(*k)}: {len(v['items'])} unique items ({v['rows']} rows)"
        for k, v in files.items() if len(v["items"]) != N_ITEMS_EXPECTED)
    missing_chunks = sorted(
        chunk_label(s, e) for s in SUTS for e in EPOCHS if (s, e) not in files)

    g1_ok = (
        exp_detail["n_files"] == len(SUTS) * len(EPOCHS)
        and not missing_chunks
        and not exp_detail["problems"]
        and not bad_chunk_counts
        and not mismatched_files
        and len(all_items) == N_ITEMS_EXPECTED
        and len(expected) == N_CELLS_EXPECTED
    )
    gates["gate1_expected_cell_set"] = {
        "pass": g1_ok,
        "responses_files": exp_detail["n_files"],
        "n_expected_cells": len(expected),
        "n_expected_cells_target": N_CELLS_EXPECTED,
        "n_unique_items_overall": len(all_items),
        "n_unique_items_target": N_ITEMS_EXPECTED,
        "chunks_missing_a_responses_file": missing_chunks,
        "chunks_with_wrong_unique_item_count": bad_chunk_counts,
        "chunks_whose_item_set_differs_from_reference": mismatched_files,
        "row_level_problems": exp_detail["problems"],
        "blank_completions_by_chunk": {
            chunk_label(*k): v["blank_completions"]
            for k, v in sorted(files.items()) if v["blank_completions"]
        },
        "note": ("blank SUT completions are DATA (floored scores), never "
                 "exclusions; RUN-SUMMARY.json complete flags not consulted"),
    }

    # ---- Gate 2: sol set == expected set EXACTLY --------------------------- #
    sol_keys = set(sol)
    sol_extra = sorted(sol_keys - set(expected))
    sol_missing = sorted(set(expected) - sol_keys)
    gates["gate2_sol_set_identity"] = {
        "pass": not sol_extra and not sol_missing and sol_detail["dir_exists"]
                and not sol_detail["unnamed_files"],
        "n_sol_verdicts": len(sol_keys),
        "n_extra": len(sol_extra),
        "n_missing": len(sol_missing),
        "extra": [verdict_name(*k) for k in sol_extra[:50]],
        "missing": [verdict_name(*k) for k in sol_missing[:50]],
        "truncated": len(sol_extra) > 50 or len(sol_missing) > 50,
        "unparseable_filenames": sol_detail["unnamed_files"],
    }

    # ---- Gate 3: opus subset of expected; report missing ------------------- #
    opus_keys = set(opus)
    opus_extra = sorted(opus_keys - set(expected))
    opus_missing = sorted(set(expected) - opus_keys)
    missing_by_chunk = by_chunk(opus_missing)
    breakdown: dict[str, object] = {}
    for (sut, epoch), items in sorted(missing_by_chunk.items()):
        label = chunk_label(sut, epoch)
        breakdown[label] = (items if len(items) <= 20
                            else {"missing_count": len(items)})
    subset_ok = not opus_extra and not opus_detail["unnamed_files"]
    complete = subset_ok and not opus_missing
    gates["gate3_opus_subset_and_completeness"] = {
        "pass": complete or (subset_ok and allow_partial),
        "subset_of_expected": subset_ok,
        "complete": complete,
        "severity": "ok" if complete else ("warning" if allow_partial else "fail"),
        "n_opus_verdicts": len(opus_keys),
        "n_missing": len(opus_missing),
        "n_extra": len(opus_extra),
        "extra": [verdict_name(*k) for k in opus_extra[:50]],
        "missing_by_chunk": breakdown,
        "unparseable_filenames": opus_detail["unnamed_files"],
    }

    # ---- Gate 4: every verdict parses to an int grade in 0..100 ------------ #
    unparsed_sol = sol_detail["unparsed"]
    unparsed_opus = opus_detail["unparsed"]
    n_unparsed = len(unparsed_sol) + len(unparsed_opus)
    gates["gate4_grade_parse"] = {
        "pass": n_unparsed == 0 or allow_partial,
        "severity": "ok" if n_unparsed == 0
                    else ("warning" if allow_partial else "fail"),
        "n_unparsed": n_unparsed,
        "unparsed_sol": unparsed_sol,
        "unparsed_opus": unparsed_opus,
        "format_anomalies": sol_detail["anomalies"] + opus_detail["anomalies"],
        "contract": "strict LAST-match of GRADE: (session-16 convention), "
                    "cross-checked against ^GRADE:\\s*(-?\\d+)\\s*$",
    }

    # ---- Gate 5: no cell dropped for a blank completion ------------------- #
    blank_cells = sorted(k for k, v in expected.items() if v["blank_completion"])
    gates["gate5_blank_completions_are_data"] = {
        "pass": True,
        "n_blank_completions": len(blank_cells),
        "n_blank_cells_dropped": 0,
        "policy": "blank/empty SUT completions are scored as data (floored), "
                  "never excluded from the cell set",
        "examples": [verdict_name(*k) for k in blank_cells[:20]],
    }

    gates["_all_pass"] = all(g["pass"] for k, g in gates.items()
                             if not k.startswith("_"))
    return gates


# --------------------------------------------------------------------------- #
# aggregation + reporting
# --------------------------------------------------------------------------- #

def build_cells(expected, opus, sol) -> list[dict]:
    rows = []
    for item, sut, epoch in sorted(expected,
                                   key=lambda k: (k[1], k[2], k[0])):
        key = (item, sut, epoch)
        o = opus.get(key)
        s = sol.get(key)
        panel = (o + s) / 2 if (o is not None and s is not None) else None
        rows.append({"item": item, "sut": sut, "epoch": epoch,
                     "opus": o, "sol": s, "panel_mean": panel})
    return rows


def print_report(rows: list[dict], gates: dict, partial: bool) -> None:
    print("=" * 78)
    print("WCF-Bench-v2 session-18 panel aggregation "
          "(session-17 Scenario-A full run)")
    print("=" * 78)

    print("\nJudged counts per SUT x epoch (opus / sol / expected):")
    header = f"  {'sut':<14}" + "".join(f"{'ep'+str(e):>18}" for e in EPOCHS)
    print(header)
    for sut in SUTS:
        line = f"  {sut:<14}"
        for epoch in EPOCHS:
            cells = [r for r in rows if r["sut"] == sut and r["epoch"] == epoch]
            no = sum(1 for r in cells if r["opus"] is not None)
            ns = sum(1 for r in cells if r["sol"] is not None)
            line += f"{no:>6} /{ns:>5} /{len(cells):>4}"
        print(line)

    g4 = gates["gate4_grade_parse"]
    print(f"\nParse failures (both arms): {g4['n_unparsed']}")
    if g4["format_anomalies"]:
        print(f"Format anomalies: {len(g4['format_anomalies'])} "
              f"(see gates.gate4_grade_parse.format_anomalies)")
    g3 = gates["gate3_opus_subset_and_completeness"]
    print(f"Opus arm: {g3['n_opus_verdicts']} verdicts, "
          f"{g3['n_missing']} cells not yet judged "
          f"({g3['severity'].upper()})")

    both = [r for r in rows if r["panel_mean"] is not None]
    print(f"\nTriage preview over cells with BOTH judges (n={len(both)}):")
    print(f"  {'sut':<14}{'n':>6}{'panel_mean':>13}{'mean_gap':>11}"
          f"{'|gap|>=30':>11}")
    for sut in SUTS:
        cells = [r for r in both if r["sut"] == sut]
        if not cells:
            print(f"  {sut:<14}{0:>6}{'-':>13}{'-':>11}{'-':>11}")
            continue
        panels = [r["panel_mean"] for r in cells]
        gaps = [r["opus"] - r["sol"] for r in cells]
        big = sum(1 for g in gaps if abs(g) >= GAP_TRIAGE_THRESHOLD)
        print(f"  {sut:<14}{len(cells):>6}"
              f"{statistics.mean(panels):>13.2f}"
              f"{statistics.mean(gaps):>11.2f}{big:>11}")
    if both:
        panels = [r["panel_mean"] for r in both]
        gaps = [r["opus"] - r["sol"] for r in both]
        big = sum(1 for g in gaps if abs(g) >= GAP_TRIAGE_THRESHOLD)
        print(f"  {'ALL':<14}{len(both):>6}{statistics.mean(panels):>13.2f}"
              f"{statistics.mean(gaps):>11.2f}{big:>11}")

    print(f"\nGATES: {'PASS' if gates['_all_pass'] else 'FAIL'}"
          f"{'  (partial: opus arm incomplete)' if partial else ''}")
    for name, g in gates.items():
        if name.startswith("_"):
            continue
        mark = "PASS" if g["pass"] else "FAIL"
        sev = g.get("severity")
        if sev == "warning":
            mark = "WARN"
        print(f"  [{mark}] {name}")
        if not g["pass"] or sev == "warning":
            for k, v in g.items():
                if k in ("pass", "severity", "note", "policy", "contract",
                         "examples"):
                    continue
                if isinstance(v, (list, dict)) and not v:
                    continue
                print(f"        {k}: {json.dumps(v)[:600]}")


def write_outputs(date: str, rows: list[dict], gates: dict,
                  partial: bool) -> list[Path]:
    meta = {
        "name": "WCF-Bench-v2 session-18 panel aggregation "
                "(session-17 Scenario A full run)",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "date_prefix": date,
        "instrument_sha": INSTRUMENT_SHA,
        "design": "5 SUTs x 345 scored items x 3 epochs; frozen instrument "
                  "(strict-v2, opus+Sol mean-of-2, single-packet mode)",
        "source_run": str(RUN_DIR.relative_to(WCF_ROOT)),
        "n_cells": len(rows),
        "n_cells_both_judges": sum(1 for r in rows
                                   if r["panel_mean"] is not None),
        "partial": partial,
        "gates": gates,
    }
    payload = {"meta": meta, "cells": rows}

    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(["item", "sut", "epoch", "opus", "sol", "panel_mean", "gap"])
    for r in rows:
        o, s, p = r["opus"], r["sol"], r["panel_mean"]
        gap = "" if p is None else o - s
        writer.writerow([r["item"], r["sut"], r["epoch"],
                         "" if o is None else o,
                         "" if s is None else s,
                         "" if p is None else p,
                         gap])
    csv_text = buf.getvalue()
    json_text = json.dumps(payload, indent=1) + "\n"

    written = []
    for directory in (ANALYSIS_DIR, RUN_DIR):
        for suffix, text in ((f"{date}-session18-panel.json", json_text),
                             (f"{date}-session18-perjudge.csv", csv_text)):
            path = directory / suffix
            # Safety: only ever write a path whose basename carries THIS --date
            # prefix. Same-date re-runs may overwrite their own regenerable
            # artifacts; a different date can never clobber an earlier file.
            if not path.name.startswith(f"{date}-session18-"):
                raise SystemExit(f"refusing to write unexpected path: {path}")
            path.write_text(text, encoding="utf-8")
            written.append(path)
    return written


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", required=True,
                    help="YYYYMMDD prefix for the output filenames")
    ap.add_argument("--allow-partial", action="store_true",
                    help="treat opus-arm incompleteness / parse failures as "
                         "warnings; aggregate over cells with both judges and "
                         "stamp the output partial:true")
    args = ap.parse_args()
    if not re.fullmatch(r"\d{8}", args.date):
        ap.error("--date must be YYYYMMDD")

    expected, exp_detail = load_expected_cells()
    sol, sol_detail = load_verdicts("sol")
    opus, opus_detail = load_verdicts("opus")

    gates = run_gates(expected, exp_detail, sol, sol_detail, opus, opus_detail,
                      args.allow_partial)
    rows = build_cells(expected, opus, sol)

    g3 = gates["gate3_opus_subset_and_completeness"]
    g4 = gates["gate4_grade_parse"]
    partial = bool(args.allow_partial and (not g3["complete"]
                                           or g4["n_unparsed"] > 0))

    print_report(rows, gates, partial)

    if not gates["_all_pass"]:
        print("\nGATES: FAIL — no outputs written.")
        return 1

    written = write_outputs(args.date, rows, gates, partial)
    print("\nWrote:")
    for path in written:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
