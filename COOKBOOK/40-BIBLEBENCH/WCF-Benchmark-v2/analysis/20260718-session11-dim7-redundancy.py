"""
WCF-Benchmark-v2 | Dimension 7: Redundancy / Near-Duplicate / Semantic-Clustering
Session 11, 2026-07-18
sklearn NOT available in .venv-v2; uses numpy + pure-Python TF-IDF cosine and
char-3-gram Jaccard. No API calls, no external services.

Outputs (relative to project root):
  analysis/20260718-session11-ledger-dim7.json
  analysis/20260718-session11-dim7-summary.json
"""

import json
import re
import math
import itertools
from pathlib import Path
from collections import defaultdict, Counter

import numpy as np

# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
DATA_MAIN    = ROOT / "data" / "wcf_main.jsonl"
DATA_EPS     = ROOT / "data" / "wcf_episodes.jsonl"
OUT_LEDGER   = ROOT / "analysis" / "20260718-session11-ledger-dim7.json"
OUT_SUMMARY  = ROOT / "analysis" / "20260718-session11-dim7-summary.json"

# ── Thresholds ─────────────────────────────────────────────────────────────────
T_NEAR_DUP   = 0.80   # either stem measure >= this → NEAR-DUP
T_HIGH_SIM   = 0.60   # either stem measure >= this → HIGH-SIM (if not NEAR-DUP)
T_RUB_CLONE  = 0.85   # rubric sim >= this AND stem sim < 0.60 → rubric-clone
TOP_PAIRS_N  = 15

# ── Load data ─────────────────────────────────────────────────────────────────
def load_items():
    items = []
    for path in [DATA_MAIN, DATA_EPS]:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line:
                    items.append(json.loads(line))
    return items

# ── Text normalisation ────────────────────────────────────────────────────────
def normalise(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def rubric_text(item) -> str:
    """Concatenate all rubric criterion texts."""
    parts = []
    for r in item.get("rubric", []):
        parts.append(r.get("criterion", ""))
        parts.append(r.get("anchor", ""))
    return " ".join(parts)

# ── Char-3-gram Jaccard ───────────────────────────────────────────────────────
def char3grams(text: str) -> set:
    return {text[i:i+3] for i in range(len(text) - 2)} if len(text) >= 3 else set()

def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    return len(a & b) / len(union)

# ── TF-IDF cosine (word-level) ────────────────────────────────────────────────
def build_tfidf(docs):
    """
    Returns (matrix, vocab) where matrix[i] is a dict {term: tfidf_weight}.
    Uses raw term-frequency (log-scaled) x IDF.
    """
    N = len(docs)
    # tokenise
    tokenised = [normalise(d).split() for d in docs]
    # DF
    df = Counter()
    for tokens in tokenised:
        for t in set(tokens):
            df[t] += 1
    # IDF (add-1 smoothing)
    idf = {t: math.log((N + 1) / (df[t] + 1)) + 1.0 for t in df}
    # TF-IDF vectors
    vecs = []
    for tokens in tokenised:
        tf = Counter(tokens)
        vec = {t: (1 + math.log(c)) * idf[t] for t, c in tf.items() if t in idf}
        # L2-normalise
        norm = math.sqrt(sum(v*v for v in vec.values())) or 1.0
        vec = {t: v/norm for t, v in vec.items()}
        vecs.append(vec)
    return vecs

def cosine_sparse(a: dict, b: dict) -> float:
    # vectors are already L2-normalised
    dot = sum(a.get(t, 0.0) * v for t, v in b.items())
    return float(np.clip(dot, 0.0, 1.0))

# ── Connected-components (union-find) ─────────────────────────────────────────
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
    def components(self):
        groups = defaultdict(list)
        for i in range(len(self.p)):
            groups[self.find(i)].append(i)
        return [v for v in groups.values() if len(v) > 1]

# ── 10-word shared-content excerpt ───────────────────────────────────────────
def shared_excerpt(s1: str, s2: str, n: int = 10) -> str:
    w1 = set(normalise(s1).split())
    w2 = set(normalise(s2).split())
    shared = w1 & w2
    # return first n shared words as they appear in s1
    words_s1 = normalise(s1).split()
    excerpt = [w for w in words_s1 if w in shared][:n]
    return " ".join(excerpt)

# ══ MAIN ═════════════════════════════════════════════════════════════════════
def main():
    items = load_items()
    n = len(items)
    ids    = [it["id"]   for it in items]
    molds  = [it["id"].split("-")[0] for it in items]
    stems  = [it["stem"] for it in items]
    rubs   = [rubric_text(it) for it in items]

    print(f"Loaded {n} items, {len(set(ids))} unique ids")
    print(f"Mold counts: {dict(Counter(molds))}")

    # ── Build similarity matrices ─────────────────────────────────────────────
    print("Building TF-IDF vectors (stems)...")
    stem_tfidf = build_tfidf(stems)
    print("Building TF-IDF vectors (rubrics)...")
    rub_tfidf  = build_tfidf(rubs)
    print("Building char-3-gram sets (stems)...")
    stem_c3 = [char3grams(normalise(s)) for s in stems]
    print("Building char-3-gram sets (rubrics)...")
    rub_c3  = [char3grams(normalise(r)) for r in rubs]

    # ── Pairwise computation ──────────────────────────────────────────────────
    # Store best similarity per item, all flagged pairs, top pairs
    n_pairs_total    = n * (n - 1) // 2
    near_dup_pairs   = []   # (i,j, tfidf_cos, c3jac, rub_cos, rub_jac)
    high_sim_pairs   = []
    rub_clone_pairs  = []

    max_stem_sim   = [0.0] * n   # per item: max of (tfidf_cos, c3jac) across all pairs
    nearest_nbr    = [None] * n  # id of nearest neighbour

    # Per-mold: collect within-mold pairwise sims for median computation
    mold_within_sims = defaultdict(list)

    print(f"Computing {n_pairs_total:,} pairs...")
    for i, j in itertools.combinations(range(n), 2):
        sc_tfidf = cosine_sparse(stem_tfidf[i], stem_tfidf[j])
        sc_c3    = jaccard(stem_c3[i], stem_c3[j])
        rc_tfidf = cosine_sparse(rub_tfidf[i], rub_tfidf[j])
        rc_c3    = jaccard(rub_c3[i], rub_c3[j])

        stem_max  = max(sc_tfidf, sc_c3)
        rub_max   = max(rc_tfidf, rc_c3)

        # Track per-item best
        if stem_max > max_stem_sim[i]:
            max_stem_sim[i] = stem_max
            nearest_nbr[i]  = ids[j]
        if stem_max > max_stem_sim[j]:
            max_stem_sim[j] = stem_max
            nearest_nbr[j]  = ids[i]

        # Within-mold tracking
        if molds[i] == molds[j]:
            mold_within_sims[molds[i]].append(stem_max)

        # Flag classification
        record = (i, j, sc_tfidf, sc_c3, rc_tfidf, rc_c3)
        if stem_max >= T_NEAR_DUP:
            near_dup_pairs.append(record)
        elif stem_max >= T_HIGH_SIM:
            high_sim_pairs.append(record)
        elif rub_max >= T_RUB_CLONE and stem_max < T_HIGH_SIM:
            rub_clone_pairs.append(record)

    print(f"NEAR-DUP (stem >= {T_NEAR_DUP}): {len(near_dup_pairs)}")
    print(f"HIGH-SIM (stem >= {T_HIGH_SIM}): {len(high_sim_pairs)}")
    print(f"RUB-CLONE (rub >= {T_RUB_CLONE}, stem < {T_HIGH_SIM}): {len(rub_clone_pairs)}")

    # ── Connected components (NEAR-DUP + HIGH-SIM edges) ─────────────────────
    uf = UF(n)
    for (i, j, *_) in near_dup_pairs + high_sim_pairs:
        uf.union(i, j)
    components = uf.components()
    cluster_map = {}  # item index → cluster_id (1-based)
    for cid, members in enumerate(components, 1):
        for m in members:
            cluster_map[m] = cid

    print(f"Clusters (size >= 2): {len(components)}")
    if components:
        largest = max(components, key=len)
        print(f"Largest cluster: size {len(largest)}, molds {set(molds[m] for m in largest)}")

    # ── Top-15 pairs by max stem sim ─────────────────────────────────────────
    all_flagged = near_dup_pairs + high_sim_pairs
    all_flagged_sorted = sorted(
        all_flagged,
        key=lambda r: max(r[2], r[3]),
        reverse=True
    )
    top15 = []
    for (i, j, sc_tfidf, sc_c3, rc_tfidf, rc_c3) in all_flagged_sorted[:TOP_PAIRS_N]:
        excerpt = shared_excerpt(stems[i], stems[j])
        same_mold = molds[i] == molds[j]
        top15.append({
            "id_a": ids[i],
            "id_b": ids[j],
            "mold_a": molds[i],
            "mold_b": molds[j],
            "cross_mold": not same_mold,
            "stem_tfidf_cos": round(sc_tfidf, 4),
            "stem_c3_jaccard": round(sc_c3, 4),
            "stem_max": round(max(sc_tfidf, sc_c3), 4),
            "rub_tfidf_cos": round(rc_tfidf, 4),
            "rub_c3_jaccard": round(rc_c3, 4),
            "shared_excerpt_10w": excerpt,
        })

    # ── Cross-mold vs within-mold high-sim pairs ─────────────────────────────
    cross_mold_pairs = [r for r in all_flagged if molds[r[0]] != molds[r[1]]]
    within_mold_pairs = [r for r in all_flagged if molds[r[0]] == molds[r[1]]]

    # ── Per-mold median pairwise similarity ──────────────────────────────────
    per_mold_stats = {}
    for mold, sims in mold_within_sims.items():
        arr = sorted(sims)
        med = arr[len(arr)//2] if arr else 0.0
        mean = sum(arr)/len(arr) if arr else 0.0
        per_mold_stats[mold] = {
            "n_within_pairs": len(arr),
            "median_pairwise_stem_sim": round(med, 4),
            "mean_pairwise_stem_sim": round(mean, 4),
            "max_pairwise_stem_sim": round(max(arr), 4) if arr else 0.0,
        }

    # ── Within-mold pairs that exceed mold median by largest margin ──────────
    mold_medians = {m: per_mold_stats[m]["median_pairwise_stem_sim"] for m in per_mold_stats}
    within_exceedance = []
    for (i, j, sc_tfidf, sc_c3, rc_tfidf, rc_c3) in within_mold_pairs:
        mol = molds[i]
        s = max(sc_tfidf, sc_c3)
        exc = s - mold_medians.get(mol, 0.0)
        within_exceedance.append((exc, i, j, s, mol))
    within_exceedance.sort(reverse=True)
    top_within_outliers = [
        {
            "id_a": ids[i], "id_b": ids[j], "mold": mol,
            "stem_max": round(s, 4),
            "exceedance_over_mold_median": round(exc, 4)
        }
        for exc, i, j, s, mol in within_exceedance[:10]
    ]

    # ── Cluster inventory ─────────────────────────────────────────────────────
    cluster_inventory = []
    for cid, members in enumerate(components, 1):
        cluster_inventory.append({
            "cluster_id": cid,
            "size": len(members),
            "molds": sorted(set(molds[m] for m in members)),
            "member_ids": sorted(ids[m] for m in members),
        })
    cluster_inventory.sort(key=lambda c: -c["size"])

    # ── Build ledger ──────────────────────────────────────────────────────────
    ledger = {}
    for idx, item_id in enumerate(ids):
        if idx in cluster_map:
            # determine flag from cluster membership
            # find if this item has any NEAR-DUP edge
            in_near_dup = any(
                (i == idx or j == idx) for (i, j, *_) in near_dup_pairs
            )
            flag = "NEAR-DUP" if in_near_dup else "HIGH-SIM"
        else:
            flag = "OK"
        ledger[item_id] = {
            "mold": molds[idx],
            "max_stem_sim": round(max_stem_sim[idx], 4),
            "nearest_neighbor_id": nearest_nbr[idx],
            "cluster_id": cluster_map.get(idx, None),
            "redundancy_flag": flag,
        }

    # ── Rubric-clone ledger entries (add annotation only; don't override OK) ──
    rub_clone_set = set()
    for (i, j, sc_tfidf, sc_c3, rc_tfidf, rc_c3) in rub_clone_pairs:
        for idx in (i, j):
            if ledger[ids[idx]]["redundancy_flag"] == "OK":
                ledger[ids[idx]]["rubric_clone_flag"] = True
            rub_clone_set.add((ids[i], ids[j]))

    # ── Summary stats: n-pairs at threshold breakdown ─────────────────────────
    # Also need count at >= 0.70, 0.50 for context
    all_pair_sims = []
    for i, j in itertools.combinations(range(n), 2):
        sc_tfidf = cosine_sparse(stem_tfidf[i], stem_tfidf[j])
        sc_c3    = jaccard(stem_c3[i], stem_c3[j])
        all_pair_sims.append(max(sc_tfidf, sc_c3))

    def count_at(threshold):
        return sum(1 for s in all_pair_sims if s >= threshold)

    threshold_counts = {
        ">=0.90": count_at(0.90),
        ">=0.80 (NEAR-DUP)": count_at(0.80),
        ">=0.70": count_at(0.70),
        ">=0.60 (HIGH-SIM)": count_at(0.60),
        ">=0.50": count_at(0.50),
        "total_pairs": n_pairs_total,
    }

    # Most redundant single pair
    top1 = top15[0] if top15 else None

    # ── Write outputs ─────────────────────────────────────────────────────────
    with open(OUT_LEDGER, "w") as f:
        json.dump(ledger, f, indent=2)
    print(f"Ledger written: {OUT_LEDGER}")

    summary = {
        "_meta": {
            "script": "20260718-session11-dim7-redundancy.py",
            "date": "2026-07-18",
            "n_items": n,
            "n_pairs_total": n_pairs_total,
            "sklearn_available": False,
            "methods": ["word-TF-IDF cosine (numpy)", "char-3-gram Jaccard (pure-python)"],
        },
        "threshold_pair_counts": threshold_counts,
        "flagged_counts": {
            "NEAR-DUP_pairs": len(near_dup_pairs),
            "HIGH-SIM_pairs": len(high_sim_pairs),
            "RUB-CLONE_pairs": len(rub_clone_pairs),
            "NEAR-DUP_items": sum(1 for v in ledger.values() if v["redundancy_flag"] == "NEAR-DUP"),
            "HIGH-SIM_items": sum(1 for v in ledger.values() if v["redundancy_flag"] == "HIGH-SIM"),
            "OK_items": sum(1 for v in ledger.values() if v["redundancy_flag"] == "OK"),
            "rubric_clone_annotated_items": sum(1 for v in ledger.values() if v.get("rubric_clone_flag")),
        },
        "cluster_summary": {
            "n_clusters": len(components),
            "largest_cluster_size": max(len(c) for c in components) if components else 0,
            "largest_cluster_molds": sorted(set(molds[m] for m in max(components, key=len))) if components else [],
            "total_items_in_clusters": sum(len(c) for c in components),
        },
        "cluster_inventory": cluster_inventory,
        "top15_highest_sim_pairs": top15,
        "most_redundant_pair": top1,
        "cross_mold_vs_within_mold": {
            "cross_mold_high_sim_pairs": len(cross_mold_pairs),
            "within_mold_high_sim_pairs": len(within_mold_pairs),
            "top_cross_mold_pairs": [
                {
                    "id_a": ids[r[0]], "id_b": ids[r[1]],
                    "mold_a": molds[r[0]], "mold_b": molds[r[1]],
                    "stem_max": round(max(r[2], r[3]), 4),
                    "stem_tfidf_cos": round(r[2], 4),
                    "stem_c3_jaccard": round(r[3], 4),
                    "shared_excerpt_10w": shared_excerpt(stems[r[0]], stems[r[1]]),
                }
                for r in sorted(cross_mold_pairs, key=lambda x: -max(x[2], x[3]))[:10]
            ],
        },
        "per_mold_pairwise_stats": per_mold_stats,
        "top10_within_mold_outliers_by_exceedance": top_within_outliers,
        "_caveats": (
            "Lexical similarity only — semantic near-duplicates with different "
            "vocabulary are NOT detected. Treat OK flags as 'no lexical redundancy', "
            "not 'unique'. TF-IDF here is corpus-relative (in-set IDF); short stems "
            "may have inflated Jaccard from shared stop-words despite normalisation. "
            "Rubric-clone detection (rub >= 0.85 AND stem < 0.60) is conservative "
            "by design: items that overlap heavily on both stem AND rubric are already "
            "caught by stem flags."
        ),
    }

    with open(OUT_SUMMARY, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary written: {OUT_SUMMARY}")

    # ── Console digest ────────────────────────────────────────────────────────
    print("\n=== DIGEST ===")
    print(f"Items: {n}  |  Pairs: {n_pairs_total:,}")
    print(f"Threshold counts: {threshold_counts}")
    print(f"Flags — NEAR-DUP items: {summary['flagged_counts']['NEAR-DUP_items']}, "
          f"HIGH-SIM items: {summary['flagged_counts']['HIGH-SIM_items']}, "
          f"OK items: {summary['flagged_counts']['OK_items']}, "
          f"rubric-clone annotated: {summary['flagged_counts']['rubric_clone_annotated_items']}")
    print(f"Clusters: {summary['cluster_summary']['n_clusters']}, "
          f"largest size: {summary['cluster_summary']['largest_cluster_size']}, "
          f"molds: {summary['cluster_summary']['largest_cluster_molds']}")
    print(f"Cross-mold high-sim pairs: {len(cross_mold_pairs)}, "
          f"within-mold: {len(within_mold_pairs)}")
    if top1:
        print(f"Most redundant pair: {top1['id_a']} <-> {top1['id_b']} "
              f"stem_max={top1['stem_max']} "
              f"(tfidf={top1['stem_tfidf_cos']}, c3jac={top1['stem_c3_jaccard']})")
        print(f"  Shared excerpt: '{top1['shared_excerpt_10w']}'")
    print(f"sklearn available: False  (used numpy TF-IDF + pure-python char-3-gram Jaccard)")

if __name__ == "__main__":
    main()
