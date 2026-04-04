#!/usr/bin/env python3
"""
Agent 4: Expanded Vault Search for Religious Values Benchmark Candidates

Finds candidates MISSED by the primary pipeline (identify_religious_benchmarks.py)
which gates on rv_* >= 50. This script uses two complementary strategies:

  1. Full-text extract search: scans PDF Extracts/ for papers matching BOTH
     a theological/religious term AND a benchmark/eval indicator term.
  2. YAML near-miss scan: finds papers in papers/ that are benchmark/eval/dataset
     AND have 0 < rv_* < 50 (near-miss scores the keyword scorer didn't push high enough).

Cross-references against the existing 401 candidates to report only NEW finds.

Output: RELIGIOUS-VALUES/data/20260404-expanded-vault-candidates.json
"""
from __future__ import annotations

import functools
import json
import re
import sys
from datetime import date
from pathlib import Path

print = functools.partial(print, flush=True)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent          # RELIGIOUS-VALUES/
WS_ROOT = PROJECT_DIR.parent             # CEI-Lit-WS/
PAPERS_DIR = WS_ROOT / "papers"
EXTRACTS_DIR = WS_ROOT / "PDF Extracts"
DATA_DIR = PROJECT_DIR / "data"

TODAY = date.today().strftime("%Y%m%d")

# Existing candidates (to exclude)
EXISTING_CANDIDATES_PATH = DATA_DIR / "20260403-religious-benchmark-candidates.json"

# ---------------------------------------------------------------------------
# Keyword dictionaries
# ---------------------------------------------------------------------------

# Tradition-specific theological terms (case-insensitive matching)
# NOTE: All terms are matched with \b word boundaries to prevent FP from
# substrings (e.g., "ren" in "transparent", "tao" in author names).
# Short ambiguous terms (ren, tao, dao, kami, jinja, sangha) are EXCLUDED
# because they cause massive false positives even with word boundaries.
THEOLOGICAL_TERMS = {
    # Abrahamic - Judaism
    "talmud": "Judaism", "talmudic": "Judaism",
    "sefaria": "Judaism", "halakha": "Judaism",
    "halakhic": "Judaism", "responsa": "Judaism", "midrash": "Judaism",
    "mishnah": "Judaism", "torah": "Judaism", "rabbinic": "Judaism",
    "teshuvot": "Judaism",
    # Abrahamic - Islam
    "fatwa": "Islam", "ijtihad": "Islam", "mujtahid": "Islam",
    "maqasid": "Islam", "tafsir": "Islam", "hadith": "Islam",
    "fiqh": "Islam", "sharia": "Islam",
    "quranic": "Islam", "quran": "Islam",
    "sunnah": "Islam", "islamic jurisprudence": "Islam",
    "islamic ethics": "Islam", "islamic values": "Islam",
    "islamic law": "Islam",
    # Abrahamic - Christianity
    "catechism": "Christianity", "homiletic": "Christianity",
    "christology": "Christianity", "soteriology": "Christianity",
    "eschatology": "Christianity", "biblical exegesis": "Christianity",
    "patristic": "Christianity",
    "thomistic": "Christianity", "canon law": "Christianity",
    "christian ethics": "Christianity", "christian values": "Christianity",
    "biblical": "Christianity",
    # Dharmic - Hinduism
    "dharma": "Hinduism", "karma": "Hinduism", "moksha": "Hinduism",
    "samsara": "Hinduism", "vedic": "Hinduism", "upanishad": "Hinduism",
    "bhagavad gita": "Hinduism", "ahimsa": "Hinduism",
    "vedanta": "Hinduism", "purana": "Hinduism",
    "hindu ethics": "Hinduism", "hindu values": "Hinduism",
    # Dharmic - Buddhism
    "pali canon": "Buddhism", "tripitaka": "Buddhism",
    "abhidharma": "Buddhism",
    "theravada": "Buddhism", "mahayana": "Buddhism",
    "bodhisattva": "Buddhism",
    "buddhist ethics": "Buddhism", "buddhist values": "Buddhism",
    # Dharmic - Jainism
    "anekantavada": "Jainism", "aparigraha": "Jainism",
    "tirthankara": "Jainism", "jain ethics": "Jainism",
    # Dharmic - Sikhism
    "guru granth sahib": "Sikhism", "gurbani": "Sikhism",
    "japji": "Sikhism", "khalsa": "Sikhism",
    "waheguru": "Sikhism", "sikh ethics": "Sikhism",
    # East Asian - Confucianism
    "analects": "Confucianism", "confucian": "Confucianism",
    "confucianism": "Confucianism",
    "mencius": "Confucianism", "junzi": "Confucianism",
    "confucian ethics": "Confucianism",
    # East Asian - Taoism
    "tao te ching": "Taoism", "daodejing": "Taoism",
    "taoism": "Taoism", "taoist": "Taoism", "daoism": "Taoism",
    "daoist": "Taoism", "wuwei": "Taoism",
    "wu wei": "Taoism", "zhuangzi": "Taoism",
    # East Asian - Shinto
    "shinto": "Shinto", "shintoism": "Shinto",
    "norito": "Shinto", "kannagara": "Shinto",
    # African/Indigenous
    "ubuntu philosophy": "Ubuntu Philosophy",
    "ubuntu ethics": "Ubuntu Philosophy",
    # Only match "ubuntu" when it co-occurs with ethics/philosophy/african context
    # (standalone "ubuntu" matches the Linux distro too often)
    "indigenous spirituality": "Indigenous Spirituality",
    "dreamtime": "Indigenous Spirituality",
    "tikanga": "Indigenous Spirituality",
    # Other
    "avesta": "Zoroastrianism", "gathas": "Zoroastrianism",
    "zoroastrian": "Zoroastrianism", "ahura mazda": "Zoroastrianism",
    "kitab-i-aqdas": "Baha'i",
    # Generic religious/theological (mapped to "General")
    "theological": "General", "theology": "General",
    "scripture": "General", "scriptural": "General",
    "religious values": "General", "faith tradition": "General",
    "interfaith": "General", "inter-faith": "General",
    "religious knowledge": "General", "religious reasoning": "General",
    "religious text": "General", "sacred text": "General",
    "religious ethics": "General", "divine command": "General",
}

# Benchmark/eval/dataset indicator terms
BENCHMARK_TERMS = [
    "benchmark", "evaluation", "dataset", "test set", "test suite",
    "annotation", "questionnaire", "survey instrument",
    "scoring rubric", "leaderboard", "shared task",
    "multiple choice", "mcq", "multiple-choice",
    "gold standard", "ground truth", "human evaluation",
    "likert scale", "likert-scale", "psychometric",
    "item response", "irt", "cronbach",
    "inter-annotator", "kappa", "fleiss",
    "validation set", "training set", "eval set",
    "prompt template", "prompt set", "question bank",
    "probing", "probe dataset", "challenge set",
]

# rv_* fields
RV_FIELDS = [
    "rv_islam", "rv_christianity", "rv_buddhism", "rv_judaism",
    "rv_hinduism", "rv_sikhism", "rv_confucianism", "rv_taoism",
    "rv_shinto", "rv_jainism", "rv_bahai", "rv_zoroastrianism",
    "rv_ubuntu", "rv_indigenous",
]

RV_TO_TRADITION = {
    "rv_islam": "Islam", "rv_christianity": "Christianity",
    "rv_buddhism": "Buddhism", "rv_judaism": "Judaism",
    "rv_hinduism": "Hinduism", "rv_sikhism": "Sikhism",
    "rv_confucianism": "Confucianism", "rv_taoism": "Taoism",
    "rv_shinto": "Shinto", "rv_jainism": "Jainism",
    "rv_bahai": "Baha'i", "rv_zoroastrianism": "Zoroastrianism",
    "rv_ubuntu": "Ubuntu Philosophy", "rv_indigenous": "Indigenous Spirituality",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def extract_field(text: str, name: str) -> str:
    m = re.search(rf"^{re.escape(name)}:\s*(.*)$", text, re.MULTILINE)
    if not m:
        return ""
    val = m.group(1).strip().strip('"').strip("'")
    if val.startswith("[[") and val.endswith("]]"):
        val = val[2:-2]
    return val.strip()


def extract_int_field(text: str, name: str) -> int:
    raw = extract_field(text, name)
    try:
        return int(raw)
    except (ValueError, TypeError):
        return 0


def get_frontmatter(content: str) -> str:
    if not content.startswith("---"):
        return ""
    match = re.search(r'\n---\s*\n', content[3:])
    if match:
        return content[3:match.start() + 3]
    return ""


def iter_files_in_dir(dirpath: Path) -> list[Path]:
    """Safely iterate directory using iterdir() (no rglob for bracket safety)."""
    results = []
    if not dirpath.is_dir():
        return results
    for item in dirpath.iterdir():
        if item.is_dir():
            # Recurse into year subdirs
            for sub in item.iterdir():
                if sub.is_file() and sub.suffix == ".md":
                    results.append(sub)
        elif item.is_file() and item.suffix == ".md":
            results.append(item)
    return sorted(results)


def find_context_snippet(text_lower: str, term: str, window: int = 200) -> str:
    """Find the first occurrence of term in text and return surrounding context."""
    idx = text_lower.find(term)
    if idx == -1:
        return ""
    start = max(0, idx - window // 2)
    end = min(len(text_lower), idx + len(term) + window // 2)
    snippet = text_lower[start:end].replace("\n", " ").strip()
    return snippet


def match_theological_terms(text_lower: str) -> dict[str, list[str]]:
    """Return dict mapping tradition -> list of matched theological terms.

    ALL terms use word-boundary regex to prevent FP from substrings.
    Special handling for "ubuntu" which is also a Linux distro name --
    only count if co-occurring with ethics/philosophy/african context.
    """
    hits: dict[str, list[str]] = {}
    for term, tradition in THEOLOGICAL_TERMS.items():
        pattern = rf'\b{re.escape(term)}\b'
        if re.search(pattern, text_lower):
            hits.setdefault(tradition, []).append(term)

    # Special: standalone "ubuntu" only counts as Ubuntu Philosophy
    # if ethics/philosophy/african context is also present
    if re.search(r'\bubuntu\b', text_lower):
        ubuntu_context = any(
            re.search(rf'\b{re.escape(ctx)}\b', text_lower)
            for ctx in ["ethics", "philosophy", "african", "communitarian",
                        "moral", "humanness", "personhood", "umuntu"]
        )
        if ubuntu_context:
            hits.setdefault("Ubuntu Philosophy", []).append("ubuntu")

    # Special: standalone "baha'i" or "bahai"
    if re.search(r"\bbaha'?i\b", text_lower):
        hits.setdefault("Baha'i", []).append("baha'i")

    return hits


def match_benchmark_terms(text_lower: str) -> list[str]:
    """Return list of matched benchmark indicator terms.

    ALL terms use word-boundary regex to prevent FP from substrings.
    """
    matched = []
    for term in BENCHMARK_TERMS:
        pattern = rf'\b{re.escape(term)}\b'
        if re.search(pattern, text_lower):
            matched.append(term)
    return matched


# ---------------------------------------------------------------------------
# Strategy 1: Full-text extract search
# ---------------------------------------------------------------------------
def search_extracts(existing_filenames: set[str]) -> tuple[list[dict], int]:
    """Scan all PDF extracts for theological+benchmark co-occurrence."""
    print("=== Strategy 1: Full-text PDF Extract Search ===")
    extract_files = iter_files_in_dir(EXTRACTS_DIR)
    print(f"  Total extract files found: {len(extract_files)}")

    candidates = []
    scanned = 0

    for ef in extract_files:
        scanned += 1
        if scanned % 500 == 0:
            print(f"  ... scanned {scanned}/{len(extract_files)} extracts")

        try:
            content = ef.read_text(encoding="utf-8")
        except Exception:
            continue

        text_lower = content.lower()

        # Match theological terms
        theo_hits = match_theological_terms(text_lower)
        if not theo_hits:
            continue

        # Match benchmark terms
        bench_hits = match_benchmark_terms(text_lower)
        if not bench_hits:
            continue

        # We have a co-occurrence. Derive the paper filename.
        # Extract filename format: "YYYY-Author-Title.md" (same as paper)
        paper_filename = ef.name

        # Skip if already in existing candidates
        if paper_filename in existing_filenames:
            continue

        # Flatten theological terms and traditions
        all_theo_terms = []
        traditions_found = set()
        for tradition, terms in theo_hits.items():
            traditions_found.add(tradition)
            all_theo_terms.extend(terms)

        # Get snippet around first theological hit
        first_term = all_theo_terms[0] if all_theo_terms else ""
        snippet = find_context_snippet(text_lower, first_term, 300)

        # Try to get rv_scores from the corresponding paper file
        paper_path = PAPERS_DIR / paper_filename
        rv_scores = {}
        is_benchmark = False
        is_eval = False
        is_dataset = False
        if paper_path.exists():
            try:
                pcontent = paper_path.read_text(encoding="utf-8")
                pfm = get_frontmatter(pcontent)
                for field in RV_FIELDS:
                    rv_scores[field] = extract_int_field(pfm, field)
                is_benchmark = extract_field(pfm, "is_benchmark").lower().strip() == "yes"
                is_eval = extract_field(pfm, "is_eval").lower().strip() == "yes"
                is_dataset = extract_field(pfm, "is_dataset").lower().strip() == "yes"
            except Exception:
                pass

        candidates.append({
            "filename": paper_filename,
            "source": "extract_search",
            "matched_theological_terms": sorted(set(all_theo_terms)),
            "matched_benchmark_terms": sorted(set(bench_hits)),
            "traditions_detected": sorted(traditions_found - {"General"}),
            "rv_scores": rv_scores,
            "is_benchmark": is_benchmark,
            "is_eval": is_eval,
            "is_dataset": is_dataset,
            "snippet": snippet[:300],
        })

    print(f"  Extracts scanned: {scanned}")
    print(f"  New candidates from extracts: {len(candidates)}")
    return candidates, scanned


# ---------------------------------------------------------------------------
# Strategy 2: YAML near-miss scan
# ---------------------------------------------------------------------------
def search_yaml_near_misses(existing_filenames: set[str]) -> tuple[list[dict], int]:
    """Find papers that are benchmark/eval/dataset with 0 < max(rv_*) < 50."""
    print("\n=== Strategy 2: YAML Near-Miss Scan ===")
    paper_files = [f for f in PAPERS_DIR.iterdir() if f.is_file() and f.suffix == ".md"]
    paper_files.sort()
    print(f"  Total paper files: {len(paper_files)}")

    candidates = []
    scanned = 0

    for pf in paper_files:
        scanned += 1
        if scanned % 500 == 0:
            print(f"  ... scanned {scanned}/{len(paper_files)} papers")

        try:
            content = pf.read_text(encoding="utf-8")
        except Exception:
            continue

        fm = get_frontmatter(content)
        if not fm:
            continue

        # Gate 1: Must be benchmark/eval/dataset
        is_benchmark = extract_field(fm, "is_benchmark").lower().strip() == "yes"
        is_eval = extract_field(fm, "is_eval").lower().strip() == "yes"
        is_dataset = extract_field(fm, "is_dataset").lower().strip() == "yes"

        if not (is_benchmark or is_eval or is_dataset):
            continue

        # Gate 2: Has any rv_* > 0 but max < 50 (near-miss)
        rv_scores = {}
        max_rv = 0
        for field in RV_FIELDS:
            score = extract_int_field(fm, field)
            rv_scores[field] = score
            max_rv = max(max_rv, score)

        if max_rv == 0 or max_rv >= 50:
            continue

        # Skip if already in existing candidates
        if pf.name in existing_filenames:
            continue

        # Determine which traditions scored > 0
        traditions_found = []
        for field in RV_FIELDS:
            if rv_scores[field] > 0:
                traditions_found.append(RV_TO_TRADITION[field])

        short_title = extract_field(fm, "short_title")
        abstract = extract_field(fm, "abstract")
        snippet = f"{short_title}: {abstract}"[:300]

        candidates.append({
            "filename": pf.name,
            "source": "yaml_near_miss",
            "matched_theological_terms": [],
            "matched_benchmark_terms": [],
            "traditions_detected": sorted(traditions_found),
            "rv_scores": rv_scores,
            "is_benchmark": is_benchmark,
            "is_eval": is_eval,
            "is_dataset": is_dataset,
            "snippet": snippet,
        })

    print(f"  Papers scanned: {scanned}")
    print(f"  Near-miss candidates: {len(candidates)}")
    return candidates, scanned


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"{'='*70}")
    print(f"Agent 4: Expanded Vault Search for Religious Benchmark Candidates")
    print(f"Date: {TODAY}")
    print(f"{'='*70}\n")

    # Load existing candidates to exclude
    existing_filenames: set[str] = set()
    if EXISTING_CANDIDATES_PATH.exists():
        with open(EXISTING_CANDIDATES_PATH, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
        for c in existing_data.get("candidates", []):
            existing_filenames.add(c["filename"])
        for c in existing_data.get("demographic_only", []):
            existing_filenames.add(c["filename"])
        print(f"Loaded {len(existing_filenames)} existing candidate filenames to exclude\n")
    else:
        print(f"WARNING: Existing candidates file not found at {EXISTING_CANDIDATES_PATH}")
        print(f"  Will report all matches as new.\n")

    # Strategy 1: Full-text extract search
    extract_candidates, extracts_scanned = search_extracts(existing_filenames)

    # Strategy 2: YAML near-miss scan
    yaml_candidates, papers_scanned = search_yaml_near_misses(
        existing_filenames | {c["filename"] for c in extract_candidates}
    )

    # Combine
    all_candidates = extract_candidates + yaml_candidates

    # Deduplicate by filename (prefer extract_search over yaml_near_miss)
    seen = set()
    deduped = []
    for c in all_candidates:
        if c["filename"] not in seen:
            seen.add(c["filename"])
            deduped.append(c)
    all_candidates = deduped

    # Build summary
    by_tradition: dict[str, int] = {}
    for c in all_candidates:
        for t in c["traditions_detected"]:
            by_tradition[t] = by_tradition.get(t, 0) + 1
        if not c["traditions_detected"]:
            by_tradition["Unknown/General"] = by_tradition.get("Unknown/General", 0) + 1

    by_source: dict[str, int] = {}
    for c in all_candidates:
        by_source[c["source"]] = by_source.get(c["source"], 0) + 1

    # Print summary
    print(f"\n{'='*70}")
    print(f"RESULTS SUMMARY")
    print(f"{'='*70}")
    print(f"Total extracts scanned: {extracts_scanned}")
    print(f"Total papers scanned:   {papers_scanned}")
    print(f"New candidates found:   {len(all_candidates)}")
    print(f"  - from extract search: {by_source.get('extract_search', 0)}")
    print(f"  - from YAML near-miss: {by_source.get('yaml_near_miss', 0)}")

    print(f"\n--- Traditions Represented ---")
    for trad, count in sorted(by_tradition.items(), key=lambda x: -x[1]):
        print(f"  {trad:30s} {count:3d}")

    # Papers that are benchmark/eval/dataset with extract-detected religion
    bm_with_religion = [c for c in all_candidates
                        if (c["is_benchmark"] or c["is_eval"] or c["is_dataset"])
                        and c["source"] == "extract_search"]
    print(f"\n--- Extract-found papers that ARE benchmark/eval/dataset: {len(bm_with_religion)} ---")
    for c in bm_with_religion[:20]:
        trads = ", ".join(c["traditions_detected"][:3]) or "General"
        bm = "BM" if c["is_benchmark"] else "  "
        ev = "EV" if c["is_eval"] else "  "
        ds = "DS" if c["is_dataset"] else "  "
        print(f"  {bm} {ev} {ds} {c['filename'][:65]:65s} | {trads}")

    # Papers that are NOT benchmark but detected religion+benchmark terms in extract
    non_bm = [c for c in all_candidates
              if not (c["is_benchmark"] or c["is_eval"] or c["is_dataset"])
              and c["source"] == "extract_search"]
    print(f"\n--- Extract-found papers NOT flagged as benchmark/eval/dataset: {len(non_bm)} ---")
    print(f"  (These may be mis-classified or have benchmark components)")
    for c in non_bm[:30]:
        trads = ", ".join(c["traditions_detected"][:3]) or "General"
        theo = ", ".join(c["matched_theological_terms"][:3])
        bench = ", ".join(c["matched_benchmark_terms"][:3])
        print(f"  {c['filename'][:55]:55s} | {trads:20s} | theo: {theo[:25]:25s} | bench: {bench[:25]}")

    # YAML near-miss details
    yaml_nm = [c for c in all_candidates if c["source"] == "yaml_near_miss"]
    print(f"\n--- YAML Near-Miss Candidates (0 < max(rv_*) < 50, is_benchmark/eval/dataset): {len(yaml_nm)} ---")
    for c in yaml_nm[:30]:
        max_rv = max(c["rv_scores"].values()) if c["rv_scores"] else 0
        trads = ", ".join(c["traditions_detected"][:3])
        bm = "BM" if c["is_benchmark"] else "  "
        ev = "EV" if c["is_eval"] else "  "
        ds = "DS" if c["is_dataset"] else "  "
        print(f"  {bm} {ev} {ds} max_rv={max_rv:2d} {c['filename'][:55]:55s} | {trads}")

    # Write output
    output = {
        "generated": TODAY,
        "search_method": "full-text extract + near-miss YAML scan",
        "total_extracts_scanned": extracts_scanned,
        "total_papers_scanned": papers_scanned,
        "existing_candidates_excluded": len(existing_filenames),
        "new_candidates": all_candidates,
        "summary": {
            "total_new": len(all_candidates),
            "by_tradition": dict(sorted(by_tradition.items(), key=lambda x: -x[1])),
            "by_source": by_source,
            "extract_with_bm_flag": len(bm_with_religion),
            "extract_without_bm_flag": len(non_bm),
            "yaml_near_miss_count": len(yaml_nm),
        },
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / f"{TODAY}-expanded-vault-candidates.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput written to: {out_path}")
    print(f"Done.")


if __name__ == "__main__":
    main()
