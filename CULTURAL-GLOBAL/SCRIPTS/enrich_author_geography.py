#!/usr/bin/env python3
"""
Enrich papers with author institutional geography.

Strategy (in order):
1. Extract affiliations from PDF extract text (first ~3000 chars usually contain them)
2. Match known institutions from geo_mappings.INSTITUTION_TO_COUNTRY
3. Use URL domain as a weak signal (e.g., .cn, .jp, .de domains)
4. Fall back to existing national_ethnic_cultural field as proxy

Adds/updates fields:
    author_country:           ISO 3166-1 alpha-2 code of first author's institution
    author_region:            Macro-region (East Asia, Western Europe, etc.)
    author_global_north_south: Global North / Global South / Ambiguous

Usage:
    python enrich_author_geography.py [--dry-run] [--write-yaml] [START END]
"""
from __future__ import annotations

import functools
import json
import os
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))
sys.path.insert(0, str(_SCRIPT_DIR))

from ethics_scoring import load_extract
from config import PAPERS_DIR
from geo_mappings import (
    INSTITUTION_TO_COUNTRY,
    resolve_country_code,
    resolve_institution_country,
    get_region,
    get_north_south,
    COUNTRY_NAME_TO_CODE,
)

# ── Output paths ─────────────────────────────────────────────────────
TODAY = date.today().strftime("%Y%m%d")
DATA_DIR = _SCRIPT_DIR.parent / "DATA"
STATS_DIR = _SCRIPT_DIR.parent / "STATISTICS"
GEO_PATH = DATA_DIR / f"{TODAY}-author-geography.json"
REPORT_PATH = STATS_DIR / f"{TODAY}-author-geography-report.md"

# ── Country TLD mapping ──────────────────────────────────────────────
TLD_TO_COUNTRY: dict[str, str] = {
    ".cn": "CN", ".jp": "JP", ".kr": "KR", ".tw": "TW",
    ".de": "DE", ".fr": "FR", ".it": "IT", ".es": "ES",
    ".nl": "NL", ".se": "SE", ".no": "NO", ".dk": "DK",
    ".fi": "FI", ".ch": "CH", ".at": "AT", ".be": "BE",
    ".pt": "PT", ".gr": "GR", ".ie": "IE",
    ".ru": "RU", ".pl": "PL", ".cz": "CZ", ".hu": "HU",
    ".ro": "RO", ".ua": "UA",
    ".br": "BR", ".mx": "MX", ".ar": "AR", ".cl": "CL",
    ".co": "CO",
    ".au": "AU", ".nz": "NZ",
    ".in": "IN", ".pk": "PK",
    ".il": "IL", ".ir": "IR", ".tr": "TR",
    ".za": "ZA", ".ng": "NG", ".ke": "KE", ".eg": "EG",
    ".sg": "SG", ".my": "MY", ".th": "TH", ".id": "ID",
    ".ph": "PH", ".vn": "VN",
    ".sa": "SA", ".ae": "AE", ".qa": "QA",
    ".edu": "US",  # .edu is US-specific
    ".ac.uk": "GB",
}

# ── Cultural tag → country mapping ───────────────────────────────────
CULTURAL_TO_COUNTRY: dict[str, str] = {
    "Chinese": "CN", "Japanese": "JP", "Korean": "KR",
    "Indian": "IN", "Indonesian": "ID", "Filipino": "PH",
    "Thai": "TH", "Vietnamese": "VN",
    "Arabic": "SA",  # default Arabic → Saudi (imprecise but common)
    "Iranian": "IR", "Hebrew/Israeli": "IL",
    "African/Ubuntu": "ZA",  # default → South Africa (imprecise)
    "American": "US", "Brazilian": "BR",
    "German": "DE", "French": "FR", "Italian": "IT",
    "Spanish": "ES", "Dutch": "NL", "Russian": "RU",
    "Australian/Aboriginal": "AU", "Singaporean": "SG",
    "Latin American": "BR",  # default → Brazil (largest)
}


# =====================================================================
# AFFILIATION EXTRACTION FROM PDF EXTRACT
# =====================================================================

# University/institution patterns to find in extract text
AFFILIATION_PATTERNS = [
    # University of X / X University
    r"(?:university|universit[àáä]|universidade|universidad|universiteit|universität)\s+(?:of\s+)?([A-Z][a-zA-Z\s]{2,30})",
    # X Institute of Technology
    r"([A-Z][a-zA-Z\s]{2,20})\s+institute\s+of\s+technology",
    # Known acronyms
    r"\b(MIT|CMU|ETH|EPFL|INRIA|CNRS|KAIST|NTU|NUS|SUTD|IIT|IISC|IIIT)\b",
    # @ email domain
    r"@([a-z0-9\-]+\.(?:edu|ac\.[a-z]{2}|[a-z]{2,3}\.[a-z]{2}))",
]

# Country name patterns in affiliations
COUNTRY_IN_AFFILIATION = re.compile(
    r"\b(" + "|".join(
        re.escape(name) for name in sorted(COUNTRY_NAME_TO_CODE.keys(), key=len, reverse=True)
        if len(name) > 3  # skip short codes
    ) + r")\b",
    re.IGNORECASE,
)


def extract_country_from_text(text: str, limit: int = 3000) -> str | None:
    """
    Try to extract the first author's institutional country from text.

    Examines the first `limit` characters (typically contains author block).
    """
    if not text:
        return None

    header = text[:limit]

    # Strategy 1: Look for country names directly in header
    m = COUNTRY_IN_AFFILIATION.search(header)
    if m:
        cc = resolve_country_code(m.group(1))
        if cc:
            return cc

    # Strategy 2: Look for known institutions
    cc = resolve_institution_country(header)
    if cc:
        return cc

    return None


def extract_country_from_url(url: str) -> str | None:
    """Extract country from URL domain TLD."""
    if not url:
        return None

    url_lower = url.lower()

    # Skip universal domains
    if any(d in url_lower for d in ["arxiv.org", "doi.org", "github.com",
                                      "huggingface.co", "semanticscholar.org"]):
        return None

    # Check compound TLDs first
    for tld, cc in TLD_TO_COUNTRY.items():
        if tld in url_lower:
            return cc

    return None


def infer_author_country(paper_path: Path) -> tuple[str | None, str]:
    """
    Infer the first author's institutional country for a paper.

    Returns:
        (country_code, method): ISO code and how it was determined.
        method: "extract", "institution", "url", "cultural_proxy", or "unknown"
    """
    content = paper_path.read_text(encoding="utf-8", errors="replace")
    stem = paper_path.stem

    # Get URL
    url_m = re.search(r'^url:\s*"?(\S+)', content, re.MULTILINE)
    url = url_m.group(1).strip('"') if url_m else ""

    # Get existing cultural tag
    cult_m = re.search(r'^national_ethnic_cultural:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    cultural = cult_m.group(1).strip() if cult_m else "N/A"

    # Strategy 1: PDF extract
    extract = load_extract(stem)
    if extract:
        cc = extract_country_from_text(extract)
        if cc:
            return cc, "extract"

    # Strategy 2: Known institutions in abstract
    abstract_m = re.search(r'^abstract:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    abstract = abstract_m.group(1) if abstract_m else ""

    # Also check author names against known institutions
    authors_m = re.search(r'^authors:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    authors = authors_m.group(1) if authors_m else ""

    combined = f"{authors} {abstract}"
    cc = resolve_institution_country(combined)
    if cc:
        return cc, "institution"

    # Strategy 3: URL domain
    cc = extract_country_from_url(url)
    if cc:
        return cc, "url"

    # Strategy 4: Cultural tag as proxy (weakest signal)
    if cultural and cultural != "N/A":
        # Take first cultural tag if multiple
        first_cultural = cultural.split(",")[0].strip()
        cc = CULTURAL_TO_COUNTRY.get(first_cultural)
        if cc:
            return cc, "cultural_proxy"

    return None, "unknown"


# =====================================================================
# MAIN
# =====================================================================

def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    write_yaml = "--write-yaml" in args
    args = [a for a in args if not a.startswith("--")]

    papers = sorted(PAPERS_DIR.glob("*.md"))
    total = len(papers)

    start_idx = 0
    end_idx = total
    if len(args) >= 2:
        start_idx = int(args[0]) - 1
        end_idx = int(args[1])
    papers = papers[start_idx:end_idx]

    print(f"Enriching author geography for {len(papers)} papers...")
    if dry_run:
        print("  (DRY RUN)")

    results = []
    method_counts = Counter()
    region_counts = Counter()
    ns_counts = Counter()
    errors = []

    for i, p in enumerate(papers, 1):
        if i % 200 == 0:
            print(f"  Progress: {i}/{len(papers)}")

        try:
            cc, method = infer_author_country(p)
        except Exception as e:
            errors.append({"file": p.name, "error": str(e)})
            cc, method = None, "error"

        method_counts[method] += 1

        if cc:
            region = get_region(cc)
            ns = get_north_south(cc)
        else:
            region = "Unknown"
            ns = "Unknown"

        region_counts[region] += 1
        ns_counts[ns] += 1

        entry = {
            "filename": p.name,
            "author_country": cc or "Unknown",
            "author_region": region,
            "author_global_north_south": ns,
            "method": method,
        }
        results.append(entry)

        # Write to YAML if requested
        if write_yaml and not dry_run and cc:
            content = p.read_text(encoding="utf-8", errors="replace")
            original = content
            # Use set_or_add pattern from score_nonwestern_frameworks
            for key, val in [
                ("author_country", f'"{cc}"'),
                ("author_region", f'"{region}"'),
                ("author_global_north_south", f'"{ns}"'),
            ]:
                pattern = rf'^{re.escape(key)}:.*$'
                replacement = f'{key}: {val}'
                new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
                if count > 0:
                    content = new_content
                else:
                    # Insert before closing ---
                    first_end = content.find('---', 0)
                    if first_end >= 0:
                        second_end = content.find('---', first_end + 3)
                        if second_end > 0:
                            before = content[:second_end].rstrip('\n')
                            after = content[second_end:]
                            content = f"{before}\n{replacement}\n{after}"

            if content != original:
                p.write_text(content, encoding="utf-8")

    # ── Save JSON ────────────────────────────────────────────────────
    if not dry_run:
        output = {
            "date": TODAY,
            "total_papers": len(results),
            "method_distribution": dict(method_counts.most_common()),
            "region_distribution": dict(region_counts.most_common()),
            "north_south_distribution": dict(ns_counts.most_common()),
            "papers": results,
        }
        tmp = GEO_PATH.with_suffix(f".tmp.{os.getpid()}.json")
        tmp.write_text(json.dumps(output, indent=2))
        os.replace(str(tmp), str(GEO_PATH))
        print(f"\nSaved to {GEO_PATH}")

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"AUTHOR GEOGRAPHY ENRICHMENT RESULTS")
    print(f"{'='*60}")
    print(f"Papers processed: {len(results)}")
    print(f"Errors: {len(errors)}")

    print(f"\nResolution method:")
    for m, c in method_counts.most_common():
        print(f"  {m}: {c} ({c/len(results)*100:.1f}%)")

    print(f"\nAuthor region:")
    for r, c in region_counts.most_common():
        print(f"  {r}: {c} ({c/len(results)*100:.1f}%)")

    print(f"\nGlobal North/South:")
    for ns, c in ns_counts.most_common():
        print(f"  {ns}: {c} ({c/len(results)*100:.1f}%)")

    # ── Save report ──────────────────────────────────────────────────
    if not dry_run:
        report_lines = [
            f"# Author Geography Enrichment Report",
            f"",
            f"**Date:** {TODAY}",
            f"**Papers processed:** {len(results)}",
            f"**Errors:** {len(errors)}",
            f"",
            f"## Resolution Method",
            f"",
            f"| Method | Count | % |",
            f"|--------|-------|---|",
        ]
        for m, c in method_counts.most_common():
            report_lines.append(f"| {m} | {c} | {c/len(results)*100:.1f}% |")

        report_lines.extend([
            f"",
            f"## Author Region Distribution",
            f"",
            f"| Region | Count | % |",
            f"|--------|-------|---|",
        ])
        for r, c in region_counts.most_common():
            report_lines.append(f"| {r} | {c} | {c/len(results)*100:.1f}% |")

        report_lines.extend([
            f"",
            f"## Global North/South",
            f"",
            f"| Classification | Count | % |",
            f"|---------------|-------|---|",
        ])
        for ns, c in ns_counts.most_common():
            report_lines.append(f"| {ns} | {c} | {c/len(results)*100:.1f}% |")

        REPORT_PATH.write_text("\n".join(report_lines))
        print(f"Saved report to {REPORT_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
