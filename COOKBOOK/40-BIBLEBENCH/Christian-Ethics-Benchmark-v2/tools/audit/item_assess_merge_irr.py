"""
item_assess_merge_irr.py
========================
Merge rater-A and rater-B item-assessment JSONL files, compute IRR
statistics, build adjudication and confirmed-major queues, and write
summary outputs.

Usage:
    python tools/audit/item_assess_merge_irr.py

All outputs land in:
    logs/item-assessment-20260718/
"""

from __future__ import annotations

import json
import math
import pathlib
import re
import sys
import collections

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
V2 = pathlib.Path(__file__).resolve().parents[2]
LOG = V2 / "logs" / "item-assessment-20260718"
RATINGS = LOG / "ratings"

CANARY = "WALKWORTHY-CANARY-7f3e2026"

SURFACES = ["public", "holdout"]
EXPECTED = {"public": 355, "holdout": 158}

# ---------------------------------------------------------------------------
# Category normalisation helpers
# ---------------------------------------------------------------------------

def norm(v: str) -> str:
    return v.strip().lower() if v else ""


# ---------------------------------------------------------------------------
# Ordinal scales (lower index = lower severity)
# ---------------------------------------------------------------------------
KV_ORD = ["sound", "contestable", "unsound"]
AF_ORD = ["supports", "partial", "no_support", "defective"]
CL_ORD = ["clear", "minor", "material"]
GR_ORD = ["generic", "mixed", "corpus_required"]
SEV_ORD = ["clean", "minor", "major", "blocker"]

# ---------------------------------------------------------------------------
# File loading
# ---------------------------------------------------------------------------

def load_surface(surface: str):
    """
    Returns:
        items_by_rater: dict[rater] -> dict[item_id] -> record
        errors: list of str
    """
    base = RATINGS / surface
    items_by_rater: dict[str, dict[str, dict]] = {"A": {}, "B": {}}
    errors: list[str] = []

    for rater in ("A", "B"):
        for fpath in sorted(base.glob(f"*-rater{rater}.jsonl")):
            with open(fpath, encoding="utf-8") as fh:
                raw_lines = fh.read().splitlines()

            if not raw_lines:
                errors.append(f"EMPTY FILE: {fpath.name}")
                continue

            # First line: header
            try:
                hdr = json.loads(raw_lines[0])
            except json.JSONDecodeError as e:
                errors.append(f"BAD HEADER ({fpath.name}): {e}")
                continue

            # Check canary in header
            if hdr.get("canary") != CANARY:
                errors.append(
                    f"CANARY MISMATCH ({fpath.name}): {hdr.get('canary')!r}"
                )

            for lineno, raw in enumerate(raw_lines[1:], start=2):
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    rec = json.loads(raw)
                except json.JSONDecodeError as e:
                    errors.append(
                        f"MALFORMED LINE {lineno} in {fpath.name}: {e}"
                    )
                    continue

                item_id = rec.get("item_id", "")
                if not item_id:
                    errors.append(
                        f"MISSING item_id line {lineno} in {fpath.name}"
                    )
                    continue

                if item_id in items_by_rater[rater]:
                    errors.append(
                        f"DUPLICATE item_id {item_id!r} in rater{rater} "
                        f"({fpath.name} line {lineno})"
                    )
                    # keep first occurrence
                    continue

                # Normalise category fields in-place
                for field in ("kv", "af", "cl", "gr", "pi", "bi"):
                    rec[field] = norm(rec.get(field, ""))

                items_by_rater[rater][item_id] = rec

    return items_by_rater, errors


# ---------------------------------------------------------------------------
# Derive design code from item_id  (e.g. WW-07-B03 -> d07)
# ---------------------------------------------------------------------------

def design_from_id(item_id: str) -> str:
    m = re.match(r"WW-(\d+)-", item_id)
    if m:
        return f"d{m.group(1).zfill(2)}"
    return "unknown"


# ---------------------------------------------------------------------------
# Severity derivation rule
# ---------------------------------------------------------------------------

def derive_severity(kv: str, af: str, cl: str, pi: str, bi: str) -> str:
    """
    blocker  : kv == unsound
    major    : kv == contestable  OR  af in {no_support, defective}
               OR  cl == material  OR  pi == confound
    minor    : af == partial  OR  cl == minor  OR  bi == flag
    clean    : otherwise
    pi values na / holds both treated as non-triggers.
    """
    if kv == "unsound":
        return "blocker"
    if (kv == "contestable"
            or af in ("no_support", "defective")
            or cl == "material"
            or pi == "confound"):
        return "major"
    if af == "partial" or cl == "minor" or bi == "flag":
        return "minor"
    return "clean"


# ---------------------------------------------------------------------------
# Cohen's kappa (unweighted and linearly weighted)
# ---------------------------------------------------------------------------

def cohen_kappa(labels_a: list, labels_b: list, categories: list,
                weights: str = "unweighted") -> float | None:
    """
    Returns Cohen's kappa (unweighted or linear-weighted).
    Returns None when degenerate (all-same column or zero items).
    categories: ordered list of valid labels.
    weights: 'unweighted' | 'linear'
    """
    n = len(labels_a)
    if n == 0:
        return None

    cat_idx = {c: i for i, c in enumerate(categories)}
    k = len(categories)

    # Build confusion matrix
    mat = [[0] * k for _ in range(k)]
    valid = 0
    for a, b in zip(labels_a, labels_b):
        if a not in cat_idx or b not in cat_idx:
            continue
        mat[cat_idx[a]][cat_idx[b]] += 1
        valid += 1

    if valid == 0:
        return None

    # Weight matrix
    w = [[0.0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if weights == "linear":
                w[i][j] = 1.0 - abs(i - j) / (k - 1) if k > 1 else 1.0
            else:
                w[i][j] = 1.0 if i == j else 0.0

    row_sum = [sum(mat[i]) for i in range(k)]
    col_sum = [sum(mat[i][j] for i in range(k)) for j in range(k)]

    po = sum(w[i][j] * mat[i][j] for i in range(k) for j in range(k)) / valid
    pe = sum(
        w[i][j] * row_sum[i] * col_sum[j]
        for i in range(k) for j in range(k)
    ) / (valid * valid)

    if abs(1.0 - pe) < 1e-9:
        return None  # degenerate: all raters agree on one category

    return round((po - pe) / (1.0 - pe), 4)


def raw_agreement(labels_a: list, labels_b: list) -> float | None:
    pairs = [(a, b) for a, b in zip(labels_a, labels_b)
             if a is not None and b is not None]
    if not pairs:
        return None
    return round(sum(a == b for a, b in pairs) / len(pairs), 4)


# ---------------------------------------------------------------------------
# IRR for a dimension over a list of (a_val, b_val) pairs
# ---------------------------------------------------------------------------

def compute_irr(pairs: list[tuple[str, str]],
                categories: list[str],
                weighted: bool = False) -> dict:
    la = [p[0] for p in pairs]
    lb = [p[1] for p in pairs]
    ra = raw_agreement(la, lb)
    kappa = cohen_kappa(la, lb, categories, weights="unweighted")
    wkappa = (
        cohen_kappa(la, lb, categories, weights="linear") if weighted else None
    )
    result = {
        "n": len(pairs),
        "raw_agreement": ra,
        "kappa": kappa,
    }
    if weighted:
        result["weighted_kappa"] = wkappa
    return result


# ---------------------------------------------------------------------------
# Collapse pi: na/holds -> "holds_or_na"; confound stays
# ---------------------------------------------------------------------------

def collapse_pi(v: str) -> str:
    if v in ("na", "holds", ""):
        return "holds_or_na"
    return v  # "confound"


# ---------------------------------------------------------------------------
# Main merge + analysis
# ---------------------------------------------------------------------------

def process_surface(surface: str) -> dict:
    """
    Returns a rich dict with merged records, IRR stats, queues, etc.
    """
    items_by_rater, load_errors = load_surface(surface)
    rA = items_by_rater["A"]
    rB = items_by_rater["B"]

    ids_A = set(rA.keys())
    ids_B = set(rB.keys())

    matched_ids = ids_A & ids_B
    only_A = ids_A - ids_B
    only_B = ids_B - ids_A

    completeness = {
        "expected": EXPECTED[surface],
        "rater_A_total": len(ids_A),
        "rater_B_total": len(ids_B),
        "matched": len(matched_ids),
        "only_in_A": sorted(only_A),
        "only_in_B": sorted(only_B),
        "load_errors": load_errors,
    }

    # ---- Build merged records ----
    merged = []
    for item_id in sorted(matched_ids):
        a = rA[item_id]
        b = rB[item_id]
        design = design_from_id(item_id)

        sev_A = derive_severity(a["kv"], a["af"], a["cl"], a["pi"], a["bi"])
        sev_B = derive_severity(b["kv"], b["af"], b["cl"], b["pi"], b["bi"])

        if sev_A == sev_B:
            consensus_sev = sev_A
            disputed = False
        else:
            consensus_sev = "disputed"
            disputed = True

        rec = {
            "item_id": item_id,
            "design": design,
            "A": {
                "kv": a["kv"], "kv_note": a.get("kv_note", ""),
                "af": a["af"], "af_note": a.get("af_note", ""),
                "cl": a["cl"], "cl_alt": a.get("cl_alt", ""),
                "gr": a["gr"], "gr_note": a.get("gr_note", ""),
                "pi": a["pi"], "pi_note": a.get("pi_note", ""),
                "bi": a["bi"], "bi_note": a.get("bi_note", ""),
                "fix": a.get("fix", ""),
                "derived_severity": sev_A,
            },
            "B": {
                "kv": b["kv"], "kv_note": b.get("kv_note", ""),
                "af": b["af"], "af_note": b.get("af_note", ""),
                "cl": b["cl"], "cl_alt": b.get("cl_alt", ""),
                "gr": b["gr"], "gr_note": b.get("gr_note", ""),
                "pi": b["pi"], "pi_note": b.get("pi_note", ""),
                "bi": b["bi"], "bi_note": b.get("bi_note", ""),
                "fix": b.get("fix", ""),
                "derived_severity": sev_B,
            },
            "consensus_severity": consensus_sev,
            "disputed": disputed,
        }
        merged.append(rec)

    # ---- IRR computations ----
    # Group by design for per-design breakdown
    by_design: dict[str, list[dict]] = collections.defaultdict(list)
    for rec in merged:
        by_design[rec["design"]].append(rec)

    def irr_for_group(recs: list[dict]) -> dict:
        kv_pairs = [(r["A"]["kv"], r["B"]["kv"]) for r in recs]
        af_pairs = [(r["A"]["af"], r["B"]["af"]) for r in recs]
        cl_pairs = [(r["A"]["cl"], r["B"]["cl"]) for r in recs]
        gr_pairs = [(r["A"]["gr"], r["B"]["gr"]) for r in recs]
        pi_pairs_raw = [(r["A"]["pi"], r["B"]["pi"]) for r in recs]
        pi_pairs = [(collapse_pi(a), collapse_pi(b)) for a, b in pi_pairs_raw]
        bi_pairs = [(r["A"]["bi"], r["B"]["bi"]) for r in recs]
        sev_pairs = [
            (r["A"]["derived_severity"], r["B"]["derived_severity"])
            for r in recs
        ]
        # gr-binary: generic vs not-generic
        gr_bin_pairs = [
            ("generic" if a == "generic" else "non_generic",
             "generic" if b == "generic" else "non_generic")
            for a, b in gr_pairs
        ]

        return {
            "kv": compute_irr(kv_pairs, KV_ORD, weighted=True),
            "af": compute_irr(af_pairs, AF_ORD, weighted=True),
            "cl": compute_irr(cl_pairs, CL_ORD, weighted=True),
            "gr": compute_irr(gr_pairs, GR_ORD, weighted=True),
            "gr_binary": compute_irr(gr_bin_pairs, ["generic", "non_generic"],
                                     weighted=False),
            "pi": compute_irr(pi_pairs, ["holds_or_na", "confound"],
                              weighted=False),
            "bi": compute_irr(bi_pairs, ["none", "flag"], weighted=False),
            "derived_severity": compute_irr(sev_pairs, SEV_ORD, weighted=True),
        }

    irr_pooled = irr_for_group(merged)
    irr_by_design = {d: irr_for_group(recs) for d, recs in sorted(by_design.items())}

    # ---- Queues ----
    MAJOR_OR_BLOCKER = {"major", "blocker"}

    adj_queue = []  # disputed AND at least one is major/blocker
    confirmed_major = []  # both are major/blocker

    for rec in merged:
        sA = rec["A"]["derived_severity"]
        sB = rec["B"]["derived_severity"]
        if rec["disputed"] and (sA in MAJOR_OR_BLOCKER or sB in MAJOR_OR_BLOCKER):
            adj_queue.append(rec)
        if sA in MAJOR_OR_BLOCKER and sB in MAJOR_OR_BLOCKER:
            confirmed_major.append(rec)

    # ---- Agreed severity counts per design per surface ----
    sev_counts: dict[str, dict[str, int]] = {}
    for d, recs in sorted(by_design.items()):
        counts = collections.Counter()
        for rec in recs:
            counts[rec["consensus_severity"]] += 1
        sev_counts[d] = dict(counts)
    sev_counts["_pooled"] = dict(
        collections.Counter(r["consensus_severity"] for r in merged)
    )

    return {
        "surface": surface,
        "completeness": completeness,
        "merged": merged,
        "irr_pooled": irr_pooled,
        "irr_by_design": irr_by_design,
        "adj_queue": adj_queue,
        "confirmed_major": confirmed_major,
        "sev_counts": sev_counts,
    }


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_jsonl(path: pathlib.Path, rows: list[dict], header_extra: dict = None):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        hdr = {"canary": CANARY}
        if header_extra:
            hdr.update(header_extra)
        fh.write(json.dumps(hdr) + "\n")
        for row in rows:
            fh.write(json.dumps(row) + "\n")


def write_json(path: pathlib.Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2)
    return path


def fmt_kappa(v) -> str:
    if v is None:
        return "—"
    return f"{v:.4f}"


def irr_table_md(irr_pooled: dict, irr_by_design: dict) -> str:
    lines = []
    lines.append(f"<!-- canary: {CANARY} -->")
    lines.append("")
    lines.append("## IRR — Pooled")
    lines.append("")
    lines.append(
        "| Dimension | n | Raw Agree | κ (unweighted) | κ_w (linear) | Note |"
    )
    lines.append(
        "|-----------|---|-----------|----------------|--------------|------|"
    )

    DIM_META = [
        ("kv",              "ordinal: sound<contestable<unsound"),
        ("af",              "ordinal: supports<partial<no_support<defective"),
        ("cl",              "ordinal: clear<minor<material"),
        ("gr",              "ordinal: generic<mixed<corpus_required"),
        ("gr_binary",       "binary: generic vs non-generic"),
        ("pi",              "binary (na=holds collapsed): holds_or_na vs confound"),
        ("bi",              "binary: none vs flag"),
        ("derived_severity","ordinal: clean<minor<major<blocker"),
    ]

    for dim, note in DIM_META:
        s = irr_pooled[dim]
        wk = s.get("weighted_kappa")
        lines.append(
            f"| {dim} | {s['n']} | {fmt_kappa(s['raw_agreement'])} "
            f"| {fmt_kappa(s['kappa'])} | {fmt_kappa(wk)} | {note} |"
        )

    lines.append("")
    lines.append("## IRR — Per Design")
    lines.append("")

    for design, irr in sorted(irr_by_design.items()):
        lines.append(f"### {design}")
        lines.append("")
        lines.append(
            "| Dimension | n | Raw Agree | κ | κ_w |"
        )
        lines.append("|-----------|---|-----------|---|-----|")
        for dim, _ in DIM_META:
            s = irr[dim]
            wk = s.get("weighted_kappa")
            lines.append(
                f"| {dim} | {s['n']} | {fmt_kappa(s['raw_agreement'])} "
                f"| {fmt_kappa(s['kappa'])} | {fmt_kappa(wk)} |"
            )
        lines.append("")

    return "\n".join(lines)


def queue_md(queue: list[dict], title: str, surface: str) -> str:
    lines = []
    lines.append(f"<!-- canary: {CANARY} -->")
    lines.append("")
    lines.append(f"# {title} — {surface} (n={len(queue)})")
    lines.append("")
    if not queue:
        lines.append("_No items in this queue._")
        return "\n".join(lines)

    for rec in queue:
        iid = rec["item_id"]
        design = rec["design"]
        lines.append(f"## {iid}  [{design}]")
        lines.append("")
        lines.append(
            f"**Consensus:** {rec['consensus_severity']}  "
            f"(**A:** {rec['A']['derived_severity']} | "
            f"**B:** {rec['B']['derived_severity']})"
        )
        lines.append("")

        # Rater A codes + notes
        a = rec["A"]
        b = rec["B"]
        for rater_label, r in [("Rater A", a), ("Rater B", b)]:
            lines.append(f"### {rater_label}")
            lines.append("")
            lines.append(f"- **kv:** `{r['kv']}`  {r['kv_note']}")
            lines.append(f"- **af:** `{r['af']}`  {r['af_note']}")
            lines.append(
                f"- **cl:** `{r['cl']}`"
                + (f" / alt: `{r['cl_alt']}`" if r['cl_alt'] else "")
            )
            lines.append(f"- **gr:** `{r['gr']}`  {r['gr_note']}")
            lines.append(f"- **pi:** `{r['pi']}`  {r['pi_note']}")
            lines.append(f"- **bi:** `{r['bi']}`  {r['bi_note']}")
            if r["fix"]:
                lines.append(f"- **fix:** {r['fix']}")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def severity_summary_md(
    public_counts: dict, holdout_counts: dict
) -> str:
    lines = []
    lines.append(f"<!-- canary: {CANARY} -->")
    lines.append("")
    lines.append("# Severity Summary")
    lines.append("")

    for surface, counts in [("public", public_counts), ("holdout", holdout_counts)]:
        lines.append(f"## {surface}")
        lines.append("")
        lines.append(
            "| Design | clean | minor | major | blocker | disputed | total |"
        )
        lines.append(
            "|--------|-------|-------|-------|---------|----------|-------|"
        )
        for design in sorted(k for k in counts if k != "_pooled"):
            c = counts[design]
            total = sum(c.values())
            lines.append(
                f"| {design} "
                f"| {c.get('clean', 0)} "
                f"| {c.get('minor', 0)} "
                f"| {c.get('major', 0)} "
                f"| {c.get('blocker', 0)} "
                f"| {c.get('disputed', 0)} "
                f"| {total} |"
            )
        p = counts.get("_pooled", {})
        ptotal = sum(p.values())
        lines.append(
            f"| **POOLED** "
            f"| **{p.get('clean', 0)}** "
            f"| **{p.get('minor', 0)}** "
            f"| **{p.get('major', 0)}** "
            f"| **{p.get('blocker', 0)}** "
            f"| **{p.get('disputed', 0)}** "
            f"| **{ptotal}** |"
        )
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    results = {}
    for surface in SURFACES:
        print(f"Processing {surface}...", flush=True)
        results[surface] = process_surface(surface)

    pub = results["public"]
    hld = results["holdout"]

    # ---- Write merged ledgers ----
    for surface, res in results.items():
        path = LOG / f"merged-ledger-{surface}.jsonl"
        write_jsonl(
            path,
            res["merged"],
            {"surface": surface, "n_items": len(res["merged"])},
        )
        print(f"  Wrote {path}")

    # ---- Write IRR JSON + MD ----
    irr_full_json = {
        "canary": CANARY,
        "public": {
            "pooled": pub["irr_pooled"],
            "by_design": pub["irr_by_design"],
        },
        "holdout": {
            "pooled": hld["irr_pooled"],
            "by_design": hld["irr_by_design"],
        },
    }
    irr_json_path = LOG / "irr-full.json"
    write_json(irr_json_path, irr_full_json)
    print(f"  Wrote {irr_json_path}")

    irr_md_content = f"<!-- canary: {CANARY} -->\n\n# IRR Full Report\n\n"
    for surface, res in results.items():
        irr_md_content += f"# Surface: {surface}\n\n"
        irr_md_content += irr_table_md(res["irr_pooled"], res["irr_by_design"])
        irr_md_content += "\n\n"

    irr_md_path = LOG / "irr-full.md"
    with open(irr_md_path, "w", encoding="utf-8") as fh:
        fh.write(irr_md_content)
    print(f"  Wrote {irr_md_path}")

    # ---- Write adjudication queues ----
    for surface, res in results.items():
        path = LOG / f"adjudication-queue-{surface}.md"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(queue_md(res["adj_queue"], "Adjudication Queue", surface))
        print(f"  Wrote {path} (n={len(res['adj_queue'])})")

    # ---- Write confirmed-major queues ----
    for surface, res in results.items():
        path = LOG / f"confirmed-major-{surface}.md"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(queue_md(res["confirmed_major"], "Confirmed Major/Blocker", surface))
        print(f"  Wrote {path} (n={len(res['confirmed_major'])})")

    # ---- Write severity summary ----
    sev_md = severity_summary_md(pub["sev_counts"], hld["sev_counts"])
    sev_path = LOG / "severity-summary.md"
    with open(sev_path, "w", encoding="utf-8") as fh:
        fh.write(sev_md)
    print(f"  Wrote {sev_path}")

    # ---- Print completeness report ----
    print("\n" + "=" * 60)
    print("COMPLETENESS REPORT")
    print("=" * 60)
    for surface, res in results.items():
        c = res["completeness"]
        print(f"\n  Surface: {surface}")
        print(f"    Expected:       {c['expected']}")
        print(f"    Rater A total:  {c['rater_A_total']}")
        print(f"    Rater B total:  {c['rater_B_total']}")
        print(f"    Matched:        {c['matched']}")
        if c["only_in_A"]:
            print(f"    Only in A:      {c['only_in_A']}")
        if c["only_in_B"]:
            print(f"    Only in B:      {c['only_in_B']}")
        if c["load_errors"]:
            print(f"    Load errors:")
            for e in c["load_errors"]:
                print(f"      {e}")
        else:
            print(f"    Load errors:    none")

    # ---- Print pooled kappa tables ----
    print("\n" + "=" * 60)
    print("POOLED IRR TABLES")
    print("=" * 60)

    DIM_META = [
        ("kv",               "ordinal wt"),
        ("af",               "ordinal wt"),
        ("cl",               "ordinal wt"),
        ("gr",               "ordinal wt"),
        ("gr_binary",        "binary"),
        ("pi",               "binary"),
        ("bi",               "binary"),
        ("derived_severity", "ordinal wt"),
    ]

    for surface, res in results.items():
        print(f"\n  Surface: {surface}")
        print(f"  {'Dim':<18} {'n':>5}  {'RawAgr':>7}  {'kappa':>7}  {'kappa_w':>8}")
        print(f"  {'-'*18} {'-'*5}  {'-'*7}  {'-'*7}  {'-'*8}")
        for dim, note in DIM_META:
            s = res["irr_pooled"][dim]
            wk = s.get("weighted_kappa")
            print(
                f"  {dim:<18} {s['n']:>5}  "
                f"{fmt_kappa(s['raw_agreement']):>7}  "
                f"{fmt_kappa(s['kappa']):>7}  "
                f"{fmt_kappa(wk):>8}  ({note})"
            )

    # ---- Print severity counts ----
    print("\n" + "=" * 60)
    print("AGREED SEVERITY COUNTS (pooled per surface)")
    print("=" * 60)
    for surface, res in results.items():
        p = res["sev_counts"].get("_pooled", {})
        total = sum(p.values())
        print(
            f"  {surface}: clean={p.get('clean',0)}  minor={p.get('minor',0)}  "
            f"major={p.get('major',0)}  blocker={p.get('blocker',0)}  "
            f"disputed={p.get('disputed',0)}  total={total}"
        )

    # ---- Print queue sizes ----
    print("\n" + "=" * 60)
    print("QUEUE SIZES")
    print("=" * 60)
    for surface, res in results.items():
        print(
            f"  {surface}: adjudication-queue={len(res['adj_queue'])}  "
            f"confirmed-major={len(res['confirmed_major'])}"
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
