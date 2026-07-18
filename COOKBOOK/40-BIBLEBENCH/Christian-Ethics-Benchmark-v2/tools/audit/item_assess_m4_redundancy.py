"""
M4 Near-duplicate / redundancy detection for WALKWORTHY v2.

Canary: WALKWORTHY-CANARY-7f3e2026

Compares items within each design (public surface, holdout surface) and
across surfaces (public x holdout). Uses TF-IDF cosine on word 1-2 grams
and char 3-5 gram TF-IDF cosine (sklearn).

Outputs:
  $OUT/m4-redundancy-public.json
  $OUT/m4-redundancy-holdout.json
  $OUT/m4-redundancy-cross.json
  $OUT/m4-summary.md
"""

import json
import os
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity as sk_cosine

    SKLEARN_OK = True
except ImportError:
    SKLEARN_OK = False
    import difflib  # fallback

CANARY = "WALKWORTHY-CANARY-7f3e2026"

V2 = Path(
    "/Users/jimmy.lin/Documents/CEI-Literature-Vault"
    "/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2"
)
PUBLIC_DIR = V2 / "datasets" / "public"
HOLDOUT_DIR = V2 / "datasets" / "holdout"
OUT_DIR = V2 / "logs" / "item-assessment-20260718"

DESIGNS = [f"design{i:02d}" for i in range(1, 11)]

ALLOW_HOLDOUT = os.environ.get("WALKWORTHY_ALLOW_HOLDOUT", "") == "1"

# -------------------------------------------------------------------
# Item text assembly
# -------------------------------------------------------------------


def item_text(record: dict) -> str:
    """Concatenate all administration input message contents + target."""
    parts = []
    for msg in record.get("input", []):
        content = msg.get("content", "")
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict):
                    parts.append(block.get("text", ""))
                else:
                    parts.append(str(block))
        else:
            parts.append(str(content))
    target = record.get("target", "")
    if target:
        parts.append(str(target))
    return " ".join(parts)


# -------------------------------------------------------------------
# Load datasets — group by item_id, merge all admin variants into one text
# -------------------------------------------------------------------


def load_design(path: Path) -> dict:
    """
    Returns {item_id -> combined_text} where combined_text concatenates the
    text of all administration records for that item_id.
    """
    if not path.exists():
        return {}
    records = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    by_item = defaultdict(list)
    for rec in records:
        iid = rec["metadata"]["item_id"]
        by_item[iid].append(item_text(rec))

    return {iid: " ".join(texts) for iid, texts in by_item.items()}


# -------------------------------------------------------------------
# Similarity computation
# -------------------------------------------------------------------


def _build_tfidf(texts, analyzer, ngram_range):
    vec = TfidfVectorizer(analyzer=analyzer, ngram_range=ngram_range, min_df=1)
    return vec.fit_transform(texts)


def compute_similarities(texts_a, texts_b, same_set):
    """
    Returns (word_cos_matrix, char_cos_matrix) as numpy ndarrays of shape
    (len_a, len_b).  If same_set=True, texts_a and texts_b are the same list
    and the full n x n self-similarity matrix is returned (caller picks the
    upper triangle).
    """
    if SKLEARN_OK:
        if same_set:
            # Fit on the single set, compute self x self
            word_mat = _build_tfidf(texts_a, "word", (1, 2))
            char_mat = _build_tfidf(texts_a, "char_wb", (3, 5))
            word_cos = sk_cosine(word_mat, word_mat)
            char_cos = sk_cosine(char_mat, char_mat)
        else:
            # Fit on union, slice into A and B sub-matrices
            all_texts = list(texts_a) + list(texts_b)
            n_a = len(texts_a)
            word_mat = _build_tfidf(all_texts, "word", (1, 2))
            char_mat = _build_tfidf(all_texts, "char_wb", (3, 5))
            word_cos = sk_cosine(word_mat[:n_a], word_mat[n_a:])
            char_cos = sk_cosine(char_mat[:n_a], char_mat[n_a:])
        return np.array(word_cos), np.array(char_cos)

    else:
        # Fallback: difflib SequenceMatcher (same score for both measures)
        def ratio(a, b):
            return difflib.SequenceMatcher(None, a[:2000], b[:2000]).ratio()

        n_a = len(texts_a)
        n_b = len(texts_b)
        if same_set:
            mat = np.eye(n_a)
            for i in range(n_a):
                for j in range(i + 1, n_a):
                    r = ratio(texts_a[i], texts_a[j])
                    mat[i, j] = mat[j, i] = r
            return mat, mat.copy()
        else:
            mat = np.zeros((n_a, n_b))
            for i in range(n_a):
                for j in range(n_b):
                    mat[i, j] = ratio(texts_a[i], texts_b[j])
            return mat, mat.copy()


# -------------------------------------------------------------------
# Distribution statistics
# -------------------------------------------------------------------


def dist_stats(values):
    if len(values) == 0:
        return {"n_pairs": 0, "mean": None, "sd": None, "p95": None, "p99": None, "max": None}
    return {
        "n_pairs": int(len(values)),
        "mean": float(np.mean(values)),
        "sd": float(np.std(values)),
        "p95": float(np.percentile(values, 95)),
        "p99": float(np.percentile(values, 99)),
        "max": float(np.max(values)),
    }


# -------------------------------------------------------------------
# Diff hint
# -------------------------------------------------------------------


def diff_hint(text_a, text_b, max_chars=200):
    """Return a ~200-char snippet showing shared tokens (longest first)."""
    words_a = set(text_a.lower().split())
    words_b = set(text_b.lower().split())
    shared = sorted(words_a & words_b, key=lambda w: -len(w))
    hint = " | ".join(shared[:20])
    return hint[:max_chars]


# -------------------------------------------------------------------
# Pair extraction
# -------------------------------------------------------------------


def _extract_pairs(ids_a, ids_b, w_cos, c_cos, same_set,
                   label_a="item_a", label_b="item_b"):
    """
    Return (pairs_list, flat_word_cos_list).
    If same_set, only upper triangle (i < j) is extracted.
    """
    pairs = []
    all_word = []
    n_a = len(ids_a)
    n_b = len(ids_b)

    for i in range(n_a):
        start_j = i + 1 if same_set else 0
        for j in range(start_j, n_b):
            wc = float(w_cos[i, j])
            cc = float(c_cos[i, j])
            all_word.append(wc)
            pairs.append({
                "id_a": ids_a[i],
                "id_b": ids_b[j],
                "surface_a": label_a,
                "surface_b": label_b,
                "word_cos": round(wc, 6),
                "char_cos": round(cc, 6),
            })

    return pairs, all_word


# -------------------------------------------------------------------
# Core analysis per design
# -------------------------------------------------------------------


def analyze_design(design_name, pub_items, hld_items):
    """
    Returns dict with keys: design, public, holdout, cross.
    Each surface value is a dict with stats, n_items, flagged_pairs, top5_pairs.
    """
    result = {"design": design_name, "public": None, "holdout": None, "cross": None}

    # ---- PUBLIC within-design ----
    pub_ids = list(pub_items.keys())
    pub_texts = [pub_items[iid] for iid in pub_ids]

    if len(pub_ids) >= 2:
        w_cos, c_cos = compute_similarities(pub_texts, pub_texts, same_set=True)
        pub_pairs, pub_all_word = _extract_pairs(
            pub_ids, pub_ids, w_cos, c_cos, same_set=True
        )
        p99 = float(np.percentile(pub_all_word, 99)) if pub_all_word else 0.0
        flagged = [p for p in pub_pairs if p["word_cos"] > 0.75 and p["word_cos"] > p99]
        top5 = sorted(pub_pairs, key=lambda p: -p["word_cos"])[:5]
        result["public"] = {
            "stats": dist_stats(np.array(pub_all_word)),
            "n_items": len(pub_ids),
            "flagged_pairs": flagged,
            "top5_pairs": top5,
        }
    else:
        result["public"] = {
            "stats": {"n_pairs": 0},
            "n_items": len(pub_ids),
            "flagged_pairs": [],
            "top5_pairs": [],
        }

    # ---- HOLDOUT within-design ----
    if hld_items is not None:
        hld_ids = list(hld_items.keys())
        hld_texts = [hld_items[iid] for iid in hld_ids]

        if len(hld_ids) >= 2:
            w_cos_h, c_cos_h = compute_similarities(hld_texts, hld_texts, same_set=True)
            hld_pairs, hld_all_word = _extract_pairs(
                hld_ids, hld_ids, w_cos_h, c_cos_h, same_set=True
            )
            p99_h = float(np.percentile(hld_all_word, 99)) if hld_all_word else 0.0
            flagged_h = [
                p for p in hld_pairs if p["word_cos"] > 0.75 and p["word_cos"] > p99_h
            ]
            top5_h = sorted(hld_pairs, key=lambda p: -p["word_cos"])[:5]
            result["holdout"] = {
                "stats": dist_stats(np.array(hld_all_word)),
                "n_items": len(hld_ids),
                "flagged_pairs": flagged_h,
                "top5_pairs": top5_h,
            }
        else:
            result["holdout"] = {
                "stats": {"n_pairs": 0},
                "n_items": len(hld_ids),
                "flagged_pairs": [],
                "top5_pairs": [],
            }

        # ---- CROSS-SURFACE (public x holdout) ----
        if pub_ids and hld_ids:
            w_cos_x, c_cos_x = compute_similarities(pub_texts, hld_texts, same_set=False)
            cross_pairs, cross_all_word = _extract_pairs(
                pub_ids, hld_ids, w_cos_x, c_cos_x, same_set=False,
                label_a="public", label_b="holdout"
            )
            # Threshold against the design's own public p99
            pub_p99 = result["public"]["stats"].get("p99") or 0.0
            flagged_x = [
                p for p in cross_pairs if p["word_cos"] > 0.75 and p["word_cos"] > pub_p99
            ]
            top5_x = sorted(cross_pairs, key=lambda p: -p["word_cos"])[:5]
            result["cross"] = {
                "stats": dist_stats(np.array(cross_all_word)),
                "n_pub_items": len(pub_ids),
                "n_hld_items": len(hld_ids),
                "flagged_pairs": flagged_x,
                "top5_pairs": top5_x,
            }

    return result


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------


def main():
    print(f"[M4] WALKWORTHY redundancy audit -- {CANARY}")
    print(f"[M4] ALLOW_HOLDOUT={ALLOW_HOLDOUT}")
    print(f"[M4] sklearn available: {SKLEARN_OK}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pub_results = []
    hld_results = []
    cross_results = []

    for design in DESIGNS:
        print(f"[M4] Processing {design} ...")
        pub_items = load_design(PUBLIC_DIR / f"{design}.jsonl")

        hld_items = None
        if ALLOW_HOLDOUT:
            hld_items = load_design(HOLDOUT_DIR / f"{design}.jsonl")

        res = analyze_design(design, pub_items, hld_items)

        # Enrich flagged+top5 pairs with diff_hint
        pub_text_map = pub_items
        hld_text_map = hld_items or {}

        for p in (res["public"]["flagged_pairs"] + res["public"]["top5_pairs"]):
            p["diff_hint"] = diff_hint(
                pub_text_map.get(p["id_a"], ""),
                pub_text_map.get(p["id_b"], ""),
            )

        if res["holdout"]:
            for p in (res["holdout"]["flagged_pairs"] + res["holdout"]["top5_pairs"]):
                p["diff_hint"] = diff_hint(
                    hld_text_map.get(p["id_a"], ""),
                    hld_text_map.get(p["id_b"], ""),
                )

        if res["cross"]:
            for p in (res["cross"]["flagged_pairs"] + res["cross"]["top5_pairs"]):
                p["diff_hint"] = diff_hint(
                    pub_text_map.get(p["id_a"], ""),
                    hld_text_map.get(p["id_b"], ""),
                )

        pub_results.append(res["public"] | {"design": design})
        if res["holdout"]:
            hld_results.append(res["holdout"] | {"design": design})
        if res["cross"]:
            cross_results.append(res["cross"] | {"design": design})

    timestamp = datetime.now(timezone.utc).isoformat()

    _write_json(OUT_DIR / "m4-redundancy-public.json", {
        "canary": CANARY, "generated_at": timestamp,
        "surface": "public", "designs": pub_results,
    })
    _write_json(OUT_DIR / "m4-redundancy-holdout.json", {
        "canary": CANARY, "generated_at": timestamp,
        "surface": "holdout", "allow_holdout": ALLOW_HOLDOUT,
        "designs": hld_results,
    })
    _write_json(OUT_DIR / "m4-redundancy-cross.json", {
        "canary": CANARY, "generated_at": timestamp,
        "surface": "cross", "allow_holdout": ALLOW_HOLDOUT,
        "designs": cross_results,
    })

    write_summary(pub_results, hld_results, cross_results, timestamp)
    print(f"[M4] Done. Output dir: {OUT_DIR}")


def _write_json(path, data):
    with open(path, "w") as fh:
        json.dump(data, fh, indent=2)
    print(f"[M4] Wrote {path}")


# -------------------------------------------------------------------
# Summary markdown
# -------------------------------------------------------------------


def fmt_stat(v):
    return "---" if v is None else f"{v:.4f}"


def write_summary(pub_results, hld_results, cross_results, timestamp):
    lines = []
    lines.append(f"<!-- canary: {CANARY} -->")
    lines.append("# M4 Redundancy Audit -- WALKWORTHY v2")
    lines.append("")
    lines.append(f"Generated: {timestamp}")
    lines.append(f"Holdout included: {ALLOW_HOLDOUT}")
    lines.append("")

    # ---- PUBLIC distribution table ----
    lines.append("## Public Surface -- Within-Design Similarity Distribution")
    lines.append("")
    lines.append(
        "| Design | N items | N pairs | Mean | SD | p95 | p99 | Max | Flagged(>0.75&>p99) |"
    )
    lines.append(
        "|--------|---------|---------|------|----|-----|-----|-----|---------------------|"
    )
    total_pub_flagged = 0
    for r in pub_results:
        s = r.get("stats", {})
        n_flag = len(r.get("flagged_pairs", []))
        total_pub_flagged += n_flag
        lines.append(
            f"| {r['design']} | {r.get('n_items','---')} | {s.get('n_pairs','---')} "
            f"| {fmt_stat(s.get('mean'))} | {fmt_stat(s.get('sd'))} "
            f"| {fmt_stat(s.get('p95'))} | {fmt_stat(s.get('p99'))} "
            f"| {fmt_stat(s.get('max'))} | {n_flag} |"
        )
    lines.append("")

    # ---- PUBLIC top-5 pairs per design ----
    lines.append("## Public Surface -- Top-5 Pairs Per Design (by word cosine)")
    lines.append("")
    for r in pub_results:
        top5 = r.get("top5_pairs", [])
        if not top5:
            continue
        lines.append(f"### {r['design']}")
        lines.append("")
        lines.append("| Rank | ID A | ID B | Word cos | Char cos | Diff hint (shared tokens) |")
        lines.append("|------|------|------|----------|----------|--------------------------|")
        for rank, p in enumerate(top5, 1):
            hint = p.get("diff_hint", "")[:120]
            lines.append(
                f"| {rank} | {p['id_a']} | {p['id_b']} "
                f"| {p['word_cos']:.4f} | {p['char_cos']:.4f} | {hint} |"
            )
        lines.append("")

    # ---- HOLDOUT distribution table ----
    total_hld_flagged = 0
    if hld_results:
        lines.append("## Holdout Surface -- Within-Design Similarity Distribution")
        lines.append("")
        lines.append(
            "| Design | N items | N pairs | Mean | SD | p95 | p99 | Max | Flagged(>0.75&>p99) |"
        )
        lines.append(
            "|--------|---------|---------|------|----|-----|-----|-----|---------------------|"
        )
        for r in hld_results:
            s = r.get("stats", {})
            n_flag = len(r.get("flagged_pairs", []))
            total_hld_flagged += n_flag
            lines.append(
                f"| {r['design']} | {r.get('n_items','---')} | {s.get('n_pairs','---')} "
                f"| {fmt_stat(s.get('mean'))} | {fmt_stat(s.get('sd'))} "
                f"| {fmt_stat(s.get('p95'))} | {fmt_stat(s.get('p99'))} "
                f"| {fmt_stat(s.get('max'))} | {n_flag} |"
            )
        lines.append("")

        lines.append("## Holdout Surface -- Top-5 Pairs Per Design (by word cosine)")
        lines.append("")
        for r in hld_results:
            top5 = r.get("top5_pairs", [])
            if not top5:
                continue
            lines.append(f"### {r['design']}")
            lines.append("")
            lines.append(
                "| Rank | ID A | ID B | Word cos | Char cos | Diff hint (shared tokens) |"
            )
            lines.append(
                "|------|------|------|----------|----------|--------------------------|"
            )
            for rank, p in enumerate(top5, 1):
                hint = p.get("diff_hint", "")[:120]
                lines.append(
                    f"| {rank} | {p['id_a']} | {p['id_b']} "
                    f"| {p['word_cos']:.4f} | {p['char_cos']:.4f} | {hint} |"
                )
            lines.append("")

    # ---- CROSS-SURFACE ----
    total_cross_flagged = 0
    if cross_results:
        lines.append(
            "## Cross-Surface Flags (Public x Holdout -- Potential Holdout Compromise)"
        )
        lines.append("")
        lines.append(
            "| Design | N pub | N hld | N cross pairs | Mean | p99 | Max | Flagged(>0.75&>pub_p99) |"
        )
        lines.append(
            "|--------|-------|-------|---------------|------|-----|-----|------------------------|"
        )
        for r in cross_results:
            s = r.get("stats", {})
            n_flag = len(r.get("flagged_pairs", []))
            total_cross_flagged += n_flag
            lines.append(
                f"| {r['design']} | {r.get('n_pub_items','---')} | {r.get('n_hld_items','---')} "
                f"| {s.get('n_pairs','---')} "
                f"| {fmt_stat(s.get('mean'))} | {fmt_stat(s.get('p99'))} "
                f"| {fmt_stat(s.get('max'))} | {n_flag} |"
            )
        lines.append("")

        lines.append("## Cross-Surface -- Top-5 Pairs Per Design (by word cosine)")
        lines.append("")
        for r in cross_results:
            top5 = r.get("top5_pairs", [])
            if not top5:
                continue
            lines.append(f"### {r['design']}")
            lines.append("")
            lines.append(
                "| Rank | Public ID | Holdout ID | Word cos | Char cos | Diff hint |"
            )
            lines.append(
                "|------|-----------|------------|----------|----------|-----------|"
            )
            for rank, p in enumerate(top5, 1):
                hint = p.get("diff_hint", "")[:120]
                lines.append(
                    f"| {rank} | {p['id_a']} | {p['id_b']} "
                    f"| {p['word_cos']:.4f} | {p['char_cos']:.4f} | {hint} |"
                )
            lines.append("")

    # ---- Summary counts ----
    lines.append("## Summary Counts")
    lines.append("")
    lines.append("| Surface | Total flagged pairs |")
    lines.append("|---------|---------------------|")
    lines.append(f"| Public within-design | {total_pub_flagged} |")
    if hld_results:
        lines.append(f"| Holdout within-design | {total_hld_flagged} |")
    if cross_results:
        lines.append(f"| Cross-surface (public x holdout) | {total_cross_flagged} |")
    lines.append("")
    lines.append(
        "> Flagged = word cosine > 0.75 AND above that design's p99. "
        "Top-5 per design always shown regardless of threshold."
    )
    lines.append("")
    lines.append(f"<!-- canary: {CANARY} -->")

    path = OUT_DIR / "m4-summary.md"
    with open(path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"[M4] Wrote {path}")


if __name__ == "__main__":
    main()
