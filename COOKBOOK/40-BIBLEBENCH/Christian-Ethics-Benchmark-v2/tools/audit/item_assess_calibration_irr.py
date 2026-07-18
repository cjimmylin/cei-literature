"""
item_assess_calibration_irr.py
Inter-rater reliability for item-assessment calibration set.

Default (no CLI args) behaviour — original A/B run:
  Inputs:
    $V2/logs/item-assessment-20260718/ratings/calibration/cal-raterA.jsonl
    $V2/logs/item-assessment-20260718/ratings/calibration/cal-raterB.jsonl
  Outputs:
    $V2/logs/item-assessment-20260718/calibration-irr.json
    $V2/logs/item-assessment-20260718/calibration-irr.md

CLI usage:
  python item_assess_calibration_irr.py <raterX.jsonl> <raterY.jsonl> <output-suffix>

  e.g.  python item_assess_calibration_irr.py \\
            ratings/calibration/cal-raterC.jsonl \\
            ratings/calibration/cal-raterD.jsonl \\
            CD
  → outputs calibration-irr-CD.json / calibration-irr-CD.md in $OUT_DIR.

Run from any directory:
  /path/to/.venv/bin/python tools/audit/item_assess_calibration_irr.py [args]
"""

import json
import pathlib
import sys
from collections import Counter

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
V2 = pathlib.Path(__file__).resolve().parents[2]  # .../Christian-Ethics-Benchmark-v2
_DEFAULT_RATINGS_DIR = V2 / "logs" / "item-assessment-20260718" / "ratings" / "calibration"
OUT_DIR = V2 / "logs" / "item-assessment-20260718"

CANARY = "WALKWORTHY-CANARY-7f3e2026"

# ---------------------------------------------------------------------------
# Ordinal category orders (low → high)
# ---------------------------------------------------------------------------
ORDINAL_ORDERS = {
    "kv":              ["sound", "contestable", "unsound"],
    "af":              ["supports", "partial", "no_support", "defective"],
    "cl":              ["clear", "minor", "material"],
    "gr":              ["generic", "mixed", "corpus_required"],
    "derived_severity": ["clean", "minor", "major", "blocker"],
    # Legacy key kept for backward-compat (original A/B files may use "severity")
    "severity":        ["clean", "minor", "major", "blocker"],
}

# All rated dimensions for the NEW rubric (IVR-1.1, no severity field).
# "derived_severity" is computed; "pi" and "bi" are nominal.
DIMS_NEW = ["kv", "af", "cl", "gr", "pi", "bi", "derived_severity"]

# Dimensions present in old rubric files (includes literal "severity").
DIMS_LEGACY = ["kv", "af", "cl", "gr", "severity"]

# ---------------------------------------------------------------------------
# Derived severity mapping (IVR-1.1)
#
#   blocker  if kv == "unsound"
#   major    if kv == "contestable"
#              OR af in {"no_support", "defective"}
#              OR cl == "material"
#              OR pi == "confound"
#   minor    if af == "partial"
#              OR cl == "minor"
#              OR bi == "flag"
#   clean    otherwise
# ---------------------------------------------------------------------------

def derive_severity(record: dict) -> str:
    kv = record.get("kv", "")
    af = record.get("af", "")
    cl = record.get("cl", "")
    pi = record.get("pi", "")
    bi = record.get("bi", "")

    if kv == "unsound":
        return "blocker"
    if (kv == "contestable"
            or af in {"no_support", "defective"}
            or cl == "material"
            or pi == "confound"):
        return "major"
    if af == "partial" or cl == "minor" or bi == "flag":
        return "minor"
    return "clean"


# ---------------------------------------------------------------------------
# Load JSONL (skip header line 0); gracefully handle missing dims
# ---------------------------------------------------------------------------

def load_jsonl(path: pathlib.Path) -> tuple[dict, list[str]]:
    """Return (records_dict, detected_dims).

    detected_dims is the union of all non-metadata keys found in the data rows
    (excluding *_note / fix / item_id fields).
    """
    records: dict = {}
    all_keys: set = set()
    with open(path) as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    # First line is a header object
    header = json.loads(lines[0])
    assert "canary" in header, f"Missing canary in {path}"
    assert header["canary"] == CANARY, f"Canary mismatch in {path}: {header['canary']}"
    for ln in lines[1:]:
        obj = json.loads(ln)
        iid = obj["item_id"]
        records[iid] = obj
        all_keys |= set(obj.keys())
    # Filter to rating dimensions only (drop metadata keys)
    _exclude = {"item_id", "fix"}
    dim_keys = {k for k in all_keys
                if not k.endswith("_note") and not k.endswith("_alt") and k not in _exclude}
    return records, dim_keys  # returns a set


# ---------------------------------------------------------------------------
# Kappa utilities
# ---------------------------------------------------------------------------

def raw_agreement(a_vals, b_vals):
    assert len(a_vals) == len(b_vals)
    n = len(a_vals)
    if n == 0:
        return None
    return sum(x == y for x, y in zip(a_vals, b_vals)) / n


def cohen_kappa_unweighted(a_vals, b_vals, categories):
    """Cohen's kappa (unweighted). Returns (kappa, note)."""
    n = len(a_vals)
    if n == 0:
        return None, "no data"
    a_unique = set(a_vals)
    b_unique = set(b_vals)
    if len(a_unique) == 1 or len(b_unique) == 1:
        agree = raw_agreement(a_vals, b_vals)
        return None, (f"degenerate (A uses {sorted(a_unique)}, "
                      f"B uses {sorted(b_unique)}); raw_agreement={agree:.3f}")

    cats = categories if categories else sorted(set(a_vals) | set(b_vals))
    cat_idx = {c: i for i, c in enumerate(cats)}
    k = len(cats)
    cm = [[0] * k for _ in range(k)]
    for av, bv in zip(a_vals, b_vals):
        if av in cat_idx and bv in cat_idx:
            cm[cat_idx[av]][cat_idx[bv]] += 1
    total = sum(sum(row) for row in cm)
    if total == 0:
        return None, "all values outside category set"
    po = sum(cm[i][i] for i in range(k)) / total
    row_sums = [sum(cm[i][j] for j in range(k)) for i in range(k)]
    col_sums = [sum(cm[i][j] for i in range(k)) for j in range(k)]
    pe = sum(row_sums[i] * col_sums[i] for i in range(k)) / (total ** 2)
    if abs(1 - pe) < 1e-12:
        return None, f"pe≈1 (degenerate); raw_agreement={po:.3f}"
    kappa = (po - pe) / (1 - pe)
    return kappa, ""


def cohen_kappa_linear_weighted(a_vals, b_vals, ordered_cats):
    """Linear-weighted Cohen's kappa for ordinal data. Returns (kappa, note)."""
    n = len(a_vals)
    if n == 0:
        return None, "no data"
    cats = ordered_cats
    cat_idx = {c: i for i, c in enumerate(cats)}
    k = len(cats)
    valid = [(av, bv) for av, bv in zip(a_vals, b_vals) if av in cat_idx and bv in cat_idx]
    if not valid:
        return None, "all values outside ordered category set"
    n_valid = len(valid)
    a_used = set(av for av, _ in valid)
    b_used = set(bv for _, bv in valid)
    if len(a_used) == 1 or len(b_used) == 1:
        agree = sum(1 for av, bv in valid if av == bv) / n_valid
        return None, (f"degenerate (A uses {sorted(a_used)}, "
                      f"B uses {sorted(b_used)}); raw_agreement={agree:.3f}")

    cm = [[0] * k for _ in range(k)]
    for av, bv in valid:
        cm[cat_idx[av]][cat_idx[bv]] += 1
    total = sum(sum(row) for row in cm)

    def w(i, j):
        return 1.0 - abs(i - j) / (k - 1)

    row_sums = [sum(cm[i][j] for j in range(k)) for i in range(k)]
    col_sums = [sum(cm[i][j] for i in range(k)) for j in range(k)]

    po_w = sum(w(i, j) * cm[i][j] for i in range(k) for j in range(k)) / total
    pe_w = sum(w(i, j) * row_sums[i] * col_sums[j]
               for i in range(k) for j in range(k)) / (total ** 2)
    if abs(1 - pe_w) < 1e-12:
        return None, f"pe_w≈1 (degenerate); raw_agreement={po_w:.3f}"
    kappa = (po_w - pe_w) / (1 - pe_w)
    return kappa, ""


# ---------------------------------------------------------------------------
# Confusion table
# ---------------------------------------------------------------------------

def confusion_table(a_vals, b_vals, categories):
    """Returns dict with cats list and matrix (A-rows x B-cols)."""
    cats = categories if categories else sorted(set(a_vals) | set(b_vals))
    cat_idx = {c: i for i, c in enumerate(cats)}
    k = len(cats)
    cm = [[0] * k for _ in range(k)]
    for av, bv in zip(a_vals, b_vals):
        ai = cat_idx.get(av)
        bi = cat_idx.get(bv)
        if ai is not None and bi is not None:
            cm[ai][bi] += 1
    return {"categories": cats, "matrix": cm}


# ---------------------------------------------------------------------------
# Core IRR computation (works for any pair of rating dicts)
# ---------------------------------------------------------------------------

def compute_irr(rater_a: dict, rater_b: dict, dims: list[str],
                rater_label_a: str = "A", rater_label_b: str = "B") -> dict:
    """Return full IRR result dict given two rating dicts and dimension list."""
    ids_a = set(rater_a.keys())
    ids_b = set(rater_b.keys())
    matched_ids = sorted(ids_a & ids_b)
    n = len(matched_ids)
    print(f"[OK] {n} items matched across raters ({rater_label_a}, {rater_label_b}).")
    if ids_a - ids_b:
        print(f"     {rater_label_a}-only items: {sorted(ids_a - ids_b)}")
    if ids_b - ids_a:
        print(f"     {rater_label_b}-only items: {sorted(ids_b - ids_a)}")

    def get_val(record, dim):
        """Return the value for dim; returns empty string if dim absent."""
        return record.get(dim, "")

    def get_categories(dim, a_vals, b_vals):
        if dim in ORDINAL_ORDERS:
            return ORDINAL_ORDERS[dim]
        return sorted(set(a_vals) | set(b_vals))

    results = {}
    for dim in dims:
        a_vals = [get_val(rater_a[i], dim) for i in matched_ids]
        b_vals = [get_val(rater_b[i], dim) for i in matched_ids]

        # Filter out items where either rater has no value for this dim
        pairs = [(av, bv) for av, bv in zip(a_vals, b_vals)
                 if av != "" and bv != ""]
        if len(pairs) < len(a_vals):
            n_missing = len(a_vals) - len(pairs)
            print(f"     [{dim}] {n_missing} item(s) missing in one or both raters — excluded from this dim.")
        if not pairs:
            results[dim] = {
                "raw_agreement": None,
                "kappa": None,
                "kappa_note": "no paired data",
                "weighted_kappa": None,
                "weighted_kappa_note": "",
                "is_ordinal": dim in ORDINAL_ORDERS,
                "categories": [],
                "confusion": {"categories": [], "matrix": []},
            }
            continue

        pa_vals, pb_vals = zip(*pairs)
        pa_vals, pb_vals = list(pa_vals), list(pb_vals)
        cats = get_categories(dim, pa_vals, pb_vals)

        agree = raw_agreement(pa_vals, pb_vals)
        kappa, kappa_note = cohen_kappa_unweighted(pa_vals, pb_vals, cats)

        wkappa = None
        wkappa_note = ""
        if dim in ORDINAL_ORDERS:
            wkappa, wkappa_note = cohen_kappa_linear_weighted(
                pa_vals, pb_vals, ORDINAL_ORDERS[dim])

        ctable = confusion_table(pa_vals, pb_vals, cats)

        results[dim] = {
            "raw_agreement": round(agree, 4) if agree is not None else None,
            "kappa": round(kappa, 4) if kappa is not None else None,
            "kappa_note": kappa_note,
            "weighted_kappa": round(wkappa, 4) if wkappa is not None else None,
            "weighted_kappa_note": wkappa_note,
            "is_ordinal": dim in ORDINAL_ORDERS,
            "n_pairs": len(pairs),
            "categories": cats,
            "confusion": ctable,
        }

    # Per-item disagreement listing
    disagreements = []
    for iid in matched_ids:
        ra = rater_a[iid]
        rb = rater_b[iid]
        diff_dims = []
        for dim in dims:
            av = get_val(ra, dim)
            bv = get_val(rb, dim)
            if av == "" and bv == "":
                continue  # both absent — skip
            if av != bv:
                note_key = dim + "_note"
                diff_dims.append({
                    "dim": dim,
                    rater_label_a: av,
                    rater_label_b: bv,
                    f"{rater_label_a}_note": ra.get(note_key, ""),
                    f"{rater_label_b}_note": rb.get(note_key, ""),
                })
        if diff_dims:
            disagreements.append({"item_id": iid, "diffs": diff_dims})

    return {
        "canary": CANARY,
        "n_items": n,
        "item_ids": matched_ids,
        "rater_labels": [rater_label_a, rater_label_b],
        "dimensions": results,
        "disagreements": disagreements,
    }


# ---------------------------------------------------------------------------
# Markdown renderer
# ---------------------------------------------------------------------------

def render_md(irr: dict, dims: list[str]) -> str:
    results = irr["dimensions"]
    disagreements = irr["disagreements"]
    rl = irr["rater_labels"]
    rA, rB = rl[0], rl[1]

    lines = []
    lines.append("# Item Assessment Calibration — IRR Report")
    lines.append("")
    lines.append(f"**Canary:** `{irr['canary']}`")
    lines.append(f"**N items:** {irr['n_items']}")
    lines.append(f"**Raters:** {rA}, {rB}")
    lines.append(f"**Item IDs:** {', '.join(irr['item_ids'])}")
    lines.append("")

    lines.append("## Kappa Summary Table")
    lines.append("")
    lines.append("| Dimension | N pairs | Raw Agree | Kappa (unweighted) | Weighted Kappa | Notes |")
    lines.append("|-----------|---------|----------|--------------------|----------------|-------|")
    for dim in dims:
        r = results[dim]
        np_str = str(r.get("n_pairs", ""))
        agree_str = f"{r['raw_agreement']:.3f}" if r['raw_agreement'] is not None else "N/A"
        kappa_str = f"{r['kappa']:.3f}" if r['kappa'] is not None else "N/A"
        wk_str = (f"{r['weighted_kappa']:.3f}" if r['weighted_kappa'] is not None
                  else ("—" if not r['is_ordinal'] else "N/A"))
        note = r['kappa_note'] or r['weighted_kappa_note'] or ""
        lines.append(f"| {dim} | {np_str} | {agree_str} | {kappa_str} | {wk_str} | {note} |")
    lines.append("")

    lines.append(f"## Confusion Tables ({rA} rows x {rB} cols)")
    lines.append("")
    for dim in dims:
        r = results[dim]
        cats = r["confusion"]["categories"]
        matrix = r["confusion"]["matrix"]
        if not cats:
            lines.append(f"### {dim}")
            lines.append("")
            lines.append("_No paired data._")
            lines.append("")
            continue
        lines.append(f"### {dim}")
        lines.append("")
        header_row = f"| {rA} \\ {rB} | " + " | ".join(cats) + " |"
        sep_row = "|-------|" + "|".join(["---"] * len(cats)) + "|"
        lines.append(header_row)
        lines.append(sep_row)
        for i, cat in enumerate(cats):
            row_vals = " | ".join(str(matrix[i][j]) for j in range(len(cats)))
            lines.append(f"| **{cat}** | {row_vals} |")
        lines.append("")

    lines.append("## Per-Item Disagreements (with Rater Notes)")
    lines.append("")
    if not disagreements:
        lines.append("_No disagreements — perfect agreement on all items._")
    else:
        lines.append(f"_{len(disagreements)} item(s) with at least one dimension disagreement._")
        lines.append("")
        for entry in disagreements:
            lines.append(f"### {entry['item_id']}")
            lines.append("")
            for d in entry['diffs']:
                lines.append(f"**{d['dim']}**: {rA}=`{d[rA]}` vs {rB}=`{d[rB]}`")
                note_a = d.get(f"{rA}_note", "")
                note_b = d.get(f"{rB}_note", "")
                if note_a:
                    lines.append(f"- _Rater {rA} note:_ {note_a}")
                if note_b:
                    lines.append(f"- _Rater {rB} note:_ {note_b}")
                lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Stdout summary
# ---------------------------------------------------------------------------

def print_kappa_table(irr: dict, dims: list[str]):
    results = irr["dimensions"]
    disagreements = irr["disagreements"]
    print("\n--- KAPPA TABLE ---")
    print(f"{'Dim':<18} {'N':>4} {'RawAgree':>9} {'Kappa':>8} {'WtdKappa':>10}  Notes")
    print("-" * 80)
    for dim in dims:
        r = results[dim]
        np_str = str(r.get("n_pairs", "?"))
        agree_str = f"{r['raw_agreement']:.3f}" if r['raw_agreement'] is not None else "N/A"
        kappa_str = f"{r['kappa']:.3f}" if r['kappa'] is not None else "N/A"
        wk_str = (f"{r['weighted_kappa']:.3f}" if r['weighted_kappa'] is not None
                  else ("—" if not r['is_ordinal'] else "N/A"))
        note = r['kappa_note'] or r['weighted_kappa_note'] or ""
        note_trunc = note[:55] + "..." if len(note) > 55 else note
        print(f"{dim:<18} {np_str:>4} {agree_str:>9} {kappa_str:>8} {wk_str:>10}  {note_trunc}")

    print(f"\n{len(disagreements)} item(s) with disagreements: "
          + (", ".join(e['item_id'] for e in disagreements) if disagreements else "none"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Parse optional CLI args
    args = sys.argv[1:]
    if len(args) == 0:
        # Default: original A/B behaviour
        path_a = _DEFAULT_RATINGS_DIR / "cal-raterA.jsonl"
        path_b = _DEFAULT_RATINGS_DIR / "cal-raterB.jsonl"
        suffix = ""
    elif len(args) == 3:
        path_a = pathlib.Path(args[0])
        path_b = pathlib.Path(args[1])
        suffix = args[2]
        # Resolve relative paths from the V2 root
        if not path_a.is_absolute():
            path_a = V2 / path_a
        if not path_b.is_absolute():
            path_b = V2 / path_b
    else:
        print("Usage: item_assess_calibration_irr.py [<raterX.jsonl> <raterY.jsonl> <suffix>]")
        sys.exit(1)

    # Derive rater labels from file stems (cal-raterX.jsonl -> X)
    def _label(p: pathlib.Path) -> str:
        stem = p.stem  # e.g. "cal-raterC"
        if stem.startswith("cal-rater"):
            return stem[len("cal-rater"):]
        return stem

    label_a = _label(path_a)
    label_b = _label(path_b)

    print(f"[INFO] Rater {label_a}: {path_a}")
    print(f"[INFO] Rater {label_b}: {path_b}")

    # Load
    rater_a, dims_a = load_jsonl(path_a)
    rater_b, dims_b = load_jsonl(path_b)

    # Decide which dimension set to use.
    # If neither file has a literal "severity" key, use the new rubric dim set.
    # If files have "severity", fall back to legacy dims (backward compat).
    has_severity = ("severity" in dims_a) or ("severity" in dims_b)
    if has_severity:
        dims = DIMS_LEGACY + [d for d in sorted(dims_a | dims_b)
                              if d not in DIMS_LEGACY and d not in {"severity"}]
        # Keep severity as is; no derived_severity for legacy files
        use_derived = False
        print("[INFO] Legacy rubric detected (severity field present); using DIMS_LEGACY.")
    else:
        use_derived = True
        dims = DIMS_NEW
        print("[INFO] IVR-1.1 rubric detected (no severity field); computing derived_severity.")

    # Inject derived_severity into each record
    if use_derived:
        for rec in rater_a.values():
            rec["derived_severity"] = derive_severity(rec)
        for rec in rater_b.values():
            rec["derived_severity"] = derive_severity(rec)

    # Compute IRR
    irr = compute_irr(rater_a, rater_b, dims,
                      rater_label_a=label_a, rater_label_b=label_b)

    # Output filenames
    if suffix:
        json_name = f"calibration-irr-{suffix}.json"
        md_name = f"calibration-irr-{suffix}.md"
    else:
        json_name = "calibration-irr.json"
        md_name = "calibration-irr.md"

    json_path = OUT_DIR / json_name
    md_path = OUT_DIR / md_name

    # Write JSON
    with open(json_path, "w") as fh:
        json.dump(irr, fh, indent=2)
    print(f"[OK] JSON written: {json_path}")

    # Write Markdown
    with open(md_path, "w") as fh:
        fh.write(render_md(irr, dims))
    print(f"[OK] Markdown written: {md_path}")

    # Stdout kappa table
    print_kappa_table(irr, dims)

    return 0


if __name__ == "__main__":
    sys.exit(main())
