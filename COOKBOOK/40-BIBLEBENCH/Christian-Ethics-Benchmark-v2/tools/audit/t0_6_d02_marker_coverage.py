"""T0-6: design-02 keyed T-marker coverage audit.

Reads the public design-02 item bank (datasets/public/design02.jsonl) and
tabulates every occurrence of the authored `T<N>` prose marker (e.g. "Material
concession begins at T4") that appears in the keyed rationale text. These
markers encode WHERE in the escalation ladder a keyed event begins/ends; the
question this script exists to answer is purely descriptive: how much of the
bank carries them, and in which JSON field(s) do they live. Whether any code
in the scoring pipeline actually parses them is answered separately by a
manual code sweep (see the companion report) -- this script does not touch
tools/, scorers.py, or metrics.py.

Zero model/API calls. Reads ONLY datasets/public/design02.jsonl (no holdout
access, no WALKWORTHY_ALLOW_HOLDOUT).

Usage:
    $V2/.venv/bin/python $V2/tools/audit/t0_6_d02_marker_coverage.py
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parents[2]
BANK_PATH = V2_ROOT / "datasets" / "public" / "design02.jsonl"

# Word-bounded on both sides so we never match a digit-bearing token embedded in a
# larger word (verified empirically: loose vs strict regex produced identical hits
# on this bank, but keep the strict form for safety on future edits to the bank).
MARKER_RE = re.compile(r"\bT(\d+)\b")

# Fields we walk looking for T<N> occurrences. `target` and `metadata.keyed.keyed`
# are the two paths this bank ever puts prose in; walk the whole record generically
# anyway so a future bank edit that moves the text somewhere else still gets caught.
def iter_string_fields(obj, path="root"):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from iter_string_fields(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from iter_string_fields(v, f"{path}[{i}]")


def short_context(text: str, start: int, end: int, max_words: int = 10) -> str:
    """Return a short (<= max_words) phrase around a regex match span."""
    before = text[:start].split()
    after = text[end:].split()
    n_before = max_words // 2
    n_after = max_words - n_before
    quote = " ".join(before[-n_before:] + [text[start:end]] + after[:n_after])
    return quote.strip()


def load_bank(path: Path):
    records = []
    with path.open() as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            records.append((line_no, json.loads(line)))
    return records


def main() -> None:
    if not BANK_PATH.exists():
        raise SystemExit(f"bank not found: {BANK_PATH}")

    records = load_bank(BANK_PATH)
    total_lines = len(records)

    item_ids_all = [rec["metadata"]["item_id"] for _, rec in records]
    unique_item_ids = sorted(set(item_ids_all))
    admin_counts = Counter(rec["metadata"]["admin"] for _, rec in records)

    # Verify base/cold_open admin variants carry identical target text per item_id,
    # so per-item marker analysis on the "base" variant is not undercounting anything
    # that only shows up in "cold_open".
    by_item = {}
    for _, rec in records:
        by_item.setdefault(rec["metadata"]["item_id"], {})[rec["metadata"]["admin"]] = rec

    admin_variants_identical = 0
    admin_variants_diff = []
    for iid, admins in by_item.items():
        if "base" in admins and "cold_open" in admins:
            if admins["base"]["target"] == admins["cold_open"]["target"]:
                admin_variants_identical += 1
            else:
                admin_variants_diff.append(iid)

    print("=" * 78)
    print("T0-6: design-02 keyed T-marker coverage")
    print("=" * 78)
    print(f"Bank file: {BANK_PATH}")
    print(f"Total JSONL lines (all admin variants): {total_lines}")
    print(f"Admin variant counts: {dict(admin_counts)}")
    print(f"Unique item_ids: {len(unique_item_ids)}")
    print(f"Admin variants with identical target text per item_id: "
          f"{admin_variants_identical} / {len(by_item)}")
    if admin_variants_diff:
        print(f"  ITEMS WITH DIFFERING base/cold_open target text: {admin_variants_diff}")
    print()

    # ------------------------------------------------------------------ #
    # Field sweep: which JSON field paths carry T<N> markers at all, across
    # every line in the bank (not just "base"), so duplication is visible.
    # ------------------------------------------------------------------ #
    field_hit_counts = Counter()
    for _, rec in records:
        for path, text in iter_string_fields(rec):
            n_hits = len(MARKER_RE.findall(text))
            if n_hits:
                field_hit_counts[path] += n_hits

    print("-" * 78)
    print("Field paths carrying >=1 T<N> marker occurrence (summed over all "
          f"{total_lines} lines, both admin variants):")
    print("-" * 78)
    for path, n in sorted(field_hit_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {n:>4}  {path}")
    print()

    # ------------------------------------------------------------------ #
    # Per-item analysis on the "base" admin variant (target/keyed text is
    # identical across admin variants per the check above, so this is not an
    # undercount).
    # ------------------------------------------------------------------ #
    base_recs = [rec for _, rec in records if rec["metadata"]["admin"] == "base"]
    base_recs.sort(key=lambda r: r["metadata"]["item_id"])

    items_with_markers = []
    items_without_markers = []
    all_n_values = []
    per_item_detail = []

    for rec in base_recs:
        iid = rec["metadata"]["item_id"]
        target_text = rec.get("target", "") or ""
        matches = list(MARKER_RE.finditer(target_text))
        n_values = [int(m.group(1)) for m in matches]
        if matches:
            items_with_markers.append(iid)
        else:
            items_without_markers.append(iid)
        all_n_values.extend(n_values)

        occurrences = []
        for m in matches:
            occurrences.append({
                "marker": m.group(0),
                "n": int(m.group(1)),
                "field": "target (== metadata.keyed.keyed, duplicate text)",
                "quote": short_context(target_text, m.start(), m.end()),
            })
        per_item_detail.append({
            "item_id": iid,
            "ladder_length": rec["metadata"]["variables"]["ladder_length"],
            "n_markers": len(matches),
            "n_values": n_values,
            "occurrences": occurrences,
        })

    print("-" * 78)
    print("Per-item marker detail (base admin variant; target == metadata.keyed.keyed)")
    print("-" * 78)
    for d in per_item_detail:
        print(f"\n{d['item_id']}  (ladder_length={d['ladder_length']}, "
              f"n_markers={d['n_markers']}, N values={d['n_values']})")
        for occ in d["occurrences"]:
            print(f"    {occ['marker']:<4} field={occ['field']:<45} "
                  f"quote: \"{occ['quote']}\"")

    n_dist = Counter(all_n_values)

    print()
    print("=" * 78)
    print("COVERAGE SUMMARY")
    print("=" * 78)
    print(f"Unique items (design02): {len(base_recs)}")
    print(f"Items with >=1 T<N> marker: {len(items_with_markers)} / {len(base_recs)}")
    print(f"Items WITHOUT any T<N> marker: {len(items_without_markers)}")
    print(f"  item_ids: {items_without_markers if items_without_markers else '(none)'}")
    print(f"Total marker occurrences across the bank: {len(all_n_values)}")
    print(f"N-value range: min={min(all_n_values) if all_n_values else None}, "
          f"max={max(all_n_values) if all_n_values else None}")
    print("N-value distribution (N -> occurrence count):")
    for n in sorted(n_dist):
        print(f"  T{n:<3} : {n_dist[n]}")
    print()
    print("Fields carrying markers: target, metadata.keyed.keyed "
          "(same string duplicated onto both paths by the converter -- ONE "
          "conceptual field, not two independent surfaces).")
    print()
    print("=" * 78)
    print("END OF REPORT")
    print("=" * 78)


if __name__ == "__main__":
    main()
