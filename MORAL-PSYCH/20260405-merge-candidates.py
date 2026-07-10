"""Merge Phase 1 (221) and Phase 2 (71) moral-psych benchmark candidates
into a unified 292-candidate roster with information-availability audit."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent  # CEI-Lit-WS
PAPERS_DIR = VAULT / "papers"
EXTRACTS_DIR = VAULT / "PDF Extracts"

PHASE1 = VAULT / "MORAL-PSYCH" / "20260403-moral-psych-benchmark-candidates.json"
PHASE2 = VAULT / "MORAL-PSYCH" / "20260404-vault-sweep-v2-report.json"
OUTPUT = VAULT / "MORAL-PSYCH" / "20260405-full-292-candidate-roster.json"


# ---------------------------------------------------------------------------
# YAML frontmatter helpers (regex-only, no round-trip)
# ---------------------------------------------------------------------------
def extract_frontmatter(content: str) -> str:
    """Return raw frontmatter text between first and second '---'."""
    if not content.startswith("---"):
        return ""
    end = content.find("\n---", 3)
    if end == -1:
        return ""
    return content[3:end]


def read_fm_field(fm: str, field: str) -> str:
    """Read a single scalar field from raw frontmatter text."""
    m = re.search(rf'^{re.escape(field)}:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    return m.group(1).strip() if m else ""


def extract_year_from_filename(filename: str) -> int | None:
    m = re.match(r"(\d{4})-", filename)
    return int(m.group(1)) if m else None


def find_extract(filename: str) -> str | None:
    """Check if a PDF extract exists for a paper filename."""
    year = extract_year_from_filename(filename)
    if not year:
        return None
    # Extract filename matches paper filename (both .md)
    extract_path = EXTRACTS_DIR / str(year) / filename
    if extract_path.exists():
        return f"PDF Extracts/{year}/{filename}"
    return None


# ---------------------------------------------------------------------------
# Load Phase 1
# ---------------------------------------------------------------------------
with open(PHASE1) as f:
    p1_data = json.load(f)

p1_candidates = p1_data["candidates"]
print(f"Phase 1: {len(p1_candidates)} candidates loaded")

# Build lookup by file
seen_files: dict[str, dict] = {}
roster: list[dict] = []

for c in p1_candidates:
    fname = c["file"]
    if fname in seen_files:
        continue
    seen_files[fname] = c

    # Determine theories from mp_scores
    theories = []
    mp_scores = c.get("mp_scores", {})
    theory_map = {
        "mp_mft": "mft",
        "mp_schwartz": "schwartz",
        "mp_trolley": "trolley",
        "mp_kohlberg": "kohlberg",
        "mp_dual_process": "dual_process",
        "mp_intuitionist": "intuitionist",
        "mp_dyadic": "dyadic",
        "mp_identity": "identity",
    }
    for key, label in theory_map.items():
        if mp_scores.get(key, 0) >= 50:
            theories.append(label)

    # Check extract
    extract_path = c.get("pdf_extract", "") or None
    if extract_path and not (VAULT / extract_path).exists():
        extract_path = find_extract(fname)
    elif not extract_path:
        extract_path = find_extract(fname)

    has_extract = extract_path is not None and (VAULT / extract_path).exists() if extract_path else False
    has_abstract = bool(c.get("abstract", "").strip())

    # Info tier
    paper_exists = (PAPERS_DIR / fname).exists()
    if has_extract and has_abstract and paper_exists:
        tier = "A"
    elif has_abstract or paper_exists:
        tier = "B"
    else:
        tier = "C"

    entry = {
        "file": fname,
        "short_title": c.get("short_title", ""),
        "year": c.get("year", extract_year_from_filename(fname)),
        "authors": c.get("authors", ""),
        "doi": c.get("doi", ""),
        "url": c.get("url", ""),
        "publication": c.get("publication", ""),
        "abstract": c.get("abstract", ""),
        "pdf_extract_path": extract_path,
        "has_extract": has_extract,
        "has_abstract": has_abstract,
        "info_tier": tier,
        "source": "phase1",
        "theories": theories,
        "mp_scores": mp_scores,
        "is_benchmark": c.get("is_benchmark", False),
        "is_eval": c.get("is_eval", False),
        "is_dataset": c.get("is_dataset", False),
    }
    roster.append(entry)

print(f"Phase 1 after dedup: {len(roster)} candidates")

# ---------------------------------------------------------------------------
# Load Phase 2
# ---------------------------------------------------------------------------
with open(PHASE2) as f:
    p2_data = json.load(f)

p2_new_count = 0
p2_dup_count = 0

for theory_key, hits in p2_data["theory_hits"].items():
    for hit in hits:
        fname = hit["file"]
        if hit.get("already_candidate", False):
            p2_dup_count += 1
            continue
        if fname in seen_files:
            # Already merged — just add theory if missing
            existing = next((r for r in roster if r["file"] == fname), None)
            if existing and theory_key not in existing["theories"]:
                existing["theories"].append(theory_key)
            p2_dup_count += 1
            continue

        seen_files[fname] = hit
        p2_new_count += 1

        # Load frontmatter from paper file for metadata
        paper_path = PAPERS_DIR / fname
        abstract = ""
        doi = ""
        url = ""
        publication = ""
        authors = ""
        year = extract_year_from_filename(fname)

        if paper_path.exists():
            try:
                content = paper_path.read_text(encoding="utf-8", errors="replace")
                fm = extract_frontmatter(content)
                if fm:
                    abstract = read_fm_field(fm, "abstract")
                    doi = read_fm_field(fm, "doi")
                    url = read_fm_field(fm, "url")
                    publication = read_fm_field(fm, "publication")
                    authors = read_fm_field(fm, "authors")
                    y = read_fm_field(fm, "year")
                    if y and y.isdigit():
                        year = int(y)
            except Exception as e:
                print(f"  Warning: could not read {fname}: {e}")

        # Extract path
        extract_path = hit.get("extract_path") or find_extract(fname)
        has_extract = bool(extract_path) and (VAULT / extract_path).exists() if extract_path else False
        has_abstract = bool(abstract.strip())
        paper_exists = paper_path.exists()

        if has_extract and has_abstract and paper_exists:
            tier = "A"
        elif has_abstract or paper_exists:
            tier = "B"
        else:
            tier = "C"

        entry = {
            "file": fname,
            "short_title": hit.get("short_title", ""),
            "year": year,
            "authors": authors,
            "doi": doi,
            "url": url,
            "publication": publication,
            "abstract": abstract,
            "pdf_extract_path": extract_path,
            "has_extract": has_extract,
            "has_abstract": has_abstract,
            "info_tier": tier,
            "source": "phase2",
            "theories": [theory_key],
            "mp_scores": {},
            "is_benchmark": False,
            "is_eval": False,
            "is_dataset": False,
        }
        roster.append(entry)

print(f"Phase 2: {p2_new_count} new, {p2_dup_count} duplicates skipped")

# ---------------------------------------------------------------------------
# For Phase 2 candidates appearing under multiple theories, merge theories
# (already handled above via the existing-entry check)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Build summary
# ---------------------------------------------------------------------------
tier_counts = {"A": 0, "B": 0, "C": 0}
has_extract_count = 0
has_abstract_count = 0
theory_dist: dict[str, int] = {}

for r in roster:
    tier_counts[r["info_tier"]] += 1
    if r["has_extract"]:
        has_extract_count += 1
    if r["has_abstract"]:
        has_abstract_count += 1
    for t in r["theories"]:
        theory_dist[t] = theory_dist.get(t, 0) + 1

summary = {
    "total_candidates": len(roster),
    "from_phase1": len(p1_candidates),
    "from_phase2_new": p2_new_count,
    "duplicates_removed": p2_dup_count,
    "info_tiers": tier_counts,
    "has_extract": has_extract_count,
    "has_abstract": has_abstract_count,
    "date": "2026-04-05",
}

output = {"summary": summary, "candidates": roster}

with open(OUTPUT, "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"\nOutput: {OUTPUT.relative_to(VAULT)}")
print(f"Total candidates: {len(roster)}")
print(f"\nInfo tiers:")
for tier, count in sorted(tier_counts.items()):
    print(f"  {tier}: {count}")
print(f"\nHas extract: {has_extract_count}")
print(f"Has abstract: {has_abstract_count}")
print(f"\nTheory distribution:")
for theory, count in sorted(theory_dist.items(), key=lambda x: -x[1]):
    print(f"  {theory}: {count}")
