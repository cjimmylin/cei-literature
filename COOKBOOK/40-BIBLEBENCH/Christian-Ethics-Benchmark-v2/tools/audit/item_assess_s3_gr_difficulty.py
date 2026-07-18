"""S3 construct cross-check: GR (genre-routing) class vs. item difficulty.

Joins:
  - logs/item-assessment-20260718/merged-ledger-public.jsonl  (per-item rater A/B gr values)
  - logs/item-assessment-20260718/m3-item-difficulty-public.json  (per-item 5-SUT keyed-success)

GR consensus rule:
  "generic"         if BOTH raters generic
  "corpus_required" if BOTH corpus_required
  "mixed"           otherwise (one or both are "mixed", or raters disagree)

Outputs (in logs/item-assessment-20260718/):
  s3-gr-difficulty.json   (full tables + per-design data)
  s3-gr-difficulty.md     (human-readable summary)

Canary: WALKWORTHY-CANARY-7f3e2026
"""
from __future__ import annotations

import json
import statistics
from collections import defaultdict
from pathlib import Path

BASE = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2")
LOG_DIR = BASE / "logs" / "item-assessment-20260718"
LEDGER_PATH = LOG_DIR / "merged-ledger-public.jsonl"
M3_PATH = LOG_DIR / "m3-item-difficulty-public.json"

OUT_JSON = LOG_DIR / "s3-gr-difficulty.json"
OUT_MD   = LOG_DIR / "s3-gr-difficulty.md"

CANARY = "WALKWORTHY-CANARY-7f3e2026"

# CV-1 annotation: only designs 04/05/10 are corpus-distinctive
CV1_CORPUS_DISTINCTIVE = {"04", "05", "10"}


def gr_consensus(a_gr: str, b_gr: str) -> str:
    if a_gr == "generic" and b_gr == "generic":
        return "generic"
    if a_gr == "corpus_required" and b_gr == "corpus_required":
        return "corpus_required"
    return "mixed"


def load_ledger(path: Path) -> dict:
    """Return {item_id: {"A_gr": ..., "B_gr": ..., "design": ...}}."""
    items = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if "item_id" not in row:
                continue  # header / meta row
            item_id = row["item_id"]
            a_gr = (row.get("A") or {}).get("gr", "")
            b_gr = (row.get("B") or {}).get("gr", "")
            design = (row.get("design") or "").lstrip("d")
            items[item_id] = {"A_gr": a_gr, "B_gr": b_gr, "design": design}
    return items


def load_m3(path: Path) -> dict:
    """Return {item_key: {"pass_rate": float, "floor": bool, "ceiling": bool, "separation": bool, "design": str}}."""
    with open(path) as f:
        m3 = json.load(f)
    out = {}
    for item in m3.get("items", []):
        key = item["item_key"]
        out[key] = {
            "pass_rate": item["keyed_success_rate"],
            "floor": item["floor_flag"],
            "ceiling": item["ceiling_flag"],
            "separation": item["separation"],
            "design": item["design"],
        }
    return out


def pct(n: int, d: int) -> float:
    return round(100.0 * n / d, 1) if d else float("nan")


def main():
    ledger = load_ledger(LEDGER_PATH)
    m3 = load_m3(M3_PATH)

    # --- join on item_id / item_key ---
    joined = []
    unmatched_ledger = []
    unmatched_m3 = set(m3.keys())

    for item_id, ldata in ledger.items():
        if item_id not in m3:
            unmatched_ledger.append(item_id)
            continue
        mdata = m3[item_id]
        unmatched_m3.discard(item_id)
        consensus = gr_consensus(ldata["A_gr"], ldata["B_gr"])
        joined.append({
            "item_id": item_id,
            "design": ldata["design"],
            "A_gr": ldata["A_gr"],
            "B_gr": ldata["B_gr"],
            "gr_consensus": consensus,
            "pass_rate": mdata["pass_rate"],
            "floor": mdata["floor"],
            "ceiling": mdata["ceiling"],
            "separation": mdata["separation"],
        })

    n_joined = len(joined)

    # --- pooled GR class stats ---
    def class_stats(rows):
        n = len(rows)
        if n == 0:
            return {"n": 0, "mean_pass_rate": float("nan"),
                    "floor_pct": float("nan"), "ceiling_pct": float("nan"),
                    "separation_pct": float("nan")}
        pass_rates = [r["pass_rate"] for r in rows if r["pass_rate"] is not None]
        n_scorable = len(pass_rates)
        floors = sum(1 for r in rows if r["floor"])
        ceilings = sum(1 for r in rows if r["ceiling"])
        seps = sum(1 for r in rows if r["separation"])
        return {
            "n": n,
            "n_pass_rate_scorable": n_scorable,
            "mean_pass_rate": round(statistics.mean(pass_rates), 4) if n_scorable else float("nan"),
            "floor_pct": pct(floors, n),
            "ceiling_pct": pct(ceilings, n),
            "separation_pct": pct(seps, n),
        }

    gr_classes = ["generic", "corpus_required", "mixed"]
    pooled_stats = {}
    for cls in gr_classes:
        rows = [r for r in joined if r["gr_consensus"] == cls]
        pooled_stats[cls] = class_stats(rows)

    # --- per-design GR class stats ---
    designs = sorted(set(r["design"] for r in joined))
    per_design_stats = {}
    for d in designs:
        d_rows = [r for r in joined if r["design"] == d]
        per_design_stats[d] = {}
        for cls in gr_classes:
            cls_rows = [r for r in d_rows if r["gr_consensus"] == cls]
            per_design_stats[d][cls] = class_stats(cls_rows)

    # --- GR class distribution per design (% non-generic, ranked) ---
    design_nongenic = []
    for d in designs:
        d_rows = [r for r in joined if r["design"] == d]
        n_d = len(d_rows)
        n_nongen = sum(1 for r in d_rows if r["gr_consensus"] != "generic")
        pct_ng = pct(n_nongen, n_d)
        n_cr = sum(1 for r in d_rows if r["gr_consensus"] == "corpus_required")
        n_mx = sum(1 for r in d_rows if r["gr_consensus"] == "mixed")
        pct_cr = pct(n_cr, n_d)
        pct_mx = pct(n_mx, n_d)
        design_nongenic.append({
            "design": d,
            "n": n_d,
            "n_generic": sum(1 for r in d_rows if r["gr_consensus"] == "generic"),
            "n_corpus_required": n_cr,
            "n_mixed": n_mx,
            "pct_nongeneric": pct_ng,
            "pct_corpus_required": pct_cr,
            "pct_mixed": pct_mx,
            "cv1_corpus_distinctive": d in CV1_CORPUS_DISTINCTIVE,
        })
    design_nongenic.sort(key=lambda x: x["pct_nongeneric"], reverse=True)

    # --- key hypothesis: generic vs corpus_required gradient ---
    gen_rows = [r for r in joined if r["gr_consensus"] == "generic"]
    cr_rows  = [r for r in joined if r["gr_consensus"] == "corpus_required"]
    gradient = None
    gen_pr = [r["pass_rate"] for r in gen_rows if r["pass_rate"] is not None]
    cr_pr  = [r["pass_rate"] for r in cr_rows  if r["pass_rate"] is not None]
    if gen_pr and cr_pr:
        gradient = round(
            statistics.mean(gen_pr) -
            statistics.mean(cr_pr),
            4
        )

    # --- build JSON output ---
    result = {
        "canary": CANARY,
        "generated": "20260718",
        "n_ledger_items": len(ledger),
        "n_m3_items": len(m3),
        "n_joined": n_joined,
        "unmatched_ledger_items": unmatched_ledger,
        "unmatched_m3_items": sorted(unmatched_m3),
        "pooled_gr_class_stats": pooled_stats,
        "per_design_gr_class_stats": per_design_stats,
        "design_nongeneric_ranking": design_nongenic,
        "key_hypothesis": {
            "description": "generic-consensus items vs corpus_required-consensus items: pass-rate gradient",
            "generic_mean_pass_rate": pooled_stats["generic"]["mean_pass_rate"],
            "corpus_required_mean_pass_rate": pooled_stats["corpus_required"]["mean_pass_rate"],
            "gradient_generic_minus_cr": gradient,
            "generic_ceiling_pct": pooled_stats["generic"]["ceiling_pct"],
            "corpus_required_ceiling_pct": pooled_stats["corpus_required"]["ceiling_pct"],
            "note": (
                "A positive gradient means generic items are easier (higher pass rate) "
                "and/or more ceiling-saturated than corpus_required items, consistent "
                "with S3 construct hypothesis that corpus-required items probe a harder, "
                "more distinctly Christian-ethics standard."
            ),
        },
    }

    with open(OUT_JSON, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Wrote JSON: {OUT_JSON}")

    # --- build Markdown output ---
    lines = [
        f"# S3 GR-Class × Item Difficulty Cross-Check",
        f"",
        f"canary: {CANARY}  ",
        f"generated: 20260718  ",
        f"source: merged-ledger-public.jsonl + m3-item-difficulty-public.json",
        f"",
        f"**Join stats:** {n_joined} items joined ({len(unmatched_ledger)} ledger-only, {len(unmatched_m3)} m3-only unmatched)",
        f"",
        f"## 1. Pooled GR-class stats",
        f"",
        f"| GR Class | n | Mean pass rate | Floor % | Ceiling % | Separation % |",
        f"|----------|---|---------------|---------|-----------|-------------|",
    ]
    for cls in gr_classes:
        s = pooled_stats[cls]
        lines.append(
            f"| {cls} | {s['n']} | {s['mean_pass_rate']:.4f} | {s['floor_pct']}% | "
            f"{s['ceiling_pct']}% | {s['separation_pct']}% |"
        )

    lines += [
        f"",
        f"## 2. Key hypothesis — generic vs corpus_required gradient",
        f"",
        f"- generic mean pass rate:        {pooled_stats['generic']['mean_pass_rate']:.4f}",
        f"- corpus_required mean pass rate: {pooled_stats['corpus_required']['mean_pass_rate']:.4f}",
        f"- gradient (generic − CR):        {gradient:+.4f}" if gradient is not None else "- gradient: N/A",
        f"- generic ceiling %:              {pooled_stats['generic']['ceiling_pct']}%",
        f"- corpus_required ceiling %:      {pooled_stats['corpus_required']['ceiling_pct']}%",
        f"",
        f"**Interpretation:** {'Generic-consensus items are EASIER (higher pass rate) and more ceiling-saturated than corpus_required items, consistent with the S3 construct hypothesis.' if (gradient is not None and gradient > 0) else 'Generic items are NOT easier than corpus_required items — the S3 construct hypothesis is not supported by this data.' if (gradient is not None and gradient < 0) else 'No gradient detected.'}",
        f"",
        f"## 3. GR class distribution per design — ranked by % non-generic",
        f"",
        f"CV-1 annotation flags designs 04, 05, 10 as corpus-distinctive.",
        f"",
        f"| Rank | Design | n | % non-generic | % corpus_required | % mixed | CV-1 corpus-distinctive? |",
        f"|------|--------|---|--------------|------------------|---------|--------------------------|",
    ]
    for rank, row in enumerate(design_nongenic, 1):
        cv1 = "YES" if row["cv1_corpus_distinctive"] else "—"
        lines.append(
            f"| {rank} | d{row['design']} | {row['n']} | {row['pct_nongeneric']}% | "
            f"{row['pct_corpus_required']}% | {row['pct_mixed']}% | {cv1} |"
        )

    lines += [
        f"",
        f"## 4. Per-design pass rates by GR class",
        f"",
        f"| Design | GR class | n | Mean pass rate | Ceiling % | Floor % |",
        f"|--------|----------|---|---------------|-----------|---------|",
    ]
    for d in sorted(per_design_stats.keys()):
        for cls in gr_classes:
            s = per_design_stats[d][cls]
            if s["n"] == 0:
                continue
            lines.append(
                f"| d{d} | {cls} | {s['n']} | {s['mean_pass_rate']:.4f} | "
                f"{s['ceiling_pct']}% | {s['floor_pct']}% |"
            )

    lines.append("")
    md_text = "\n".join(lines)
    with open(OUT_MD, "w") as f:
        f.write(md_text)
    print(f"Wrote MD:   {OUT_MD}")

    # Print summary
    print(f"\n=== S3 RESULTS SUMMARY ===")
    print(f"Items joined: {n_joined}")
    print(f"GR class distribution:")
    for cls in gr_classes:
        s = pooled_stats[cls]
        print(f"  {cls:20s}: n={s['n']:3d}  pass_rate={s['mean_pass_rate']:.4f}  "
              f"ceiling={s['ceiling_pct']}%  floor={s['floor_pct']}%")
    print(f"Gradient (generic - CR): {gradient:+.4f}" if gradient is not None else "Gradient: N/A")
    print(f"\n% non-generic per design (ranked):")
    for row in design_nongenic:
        cv1 = " [CV-1 distinctive]" if row["cv1_corpus_distinctive"] else ""
        print(f"  d{row['design']}: {row['pct_nongeneric']}% non-generic "
              f"({row['pct_corpus_required']}% CR + {row['pct_mixed']}% mixed)"
              f"{cv1}")


if __name__ == "__main__":
    main()
