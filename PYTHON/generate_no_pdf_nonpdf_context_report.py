#!/usr/bin/env python3
"""
Generate categorization report for papers that:
1) do not have a local PDF on disk, and
2) have non-PDF context URLs (web/article/repo/blog pages).

Outputs:
  - logs/YYYYMMDD-no-pdf-nonpdf-context-categorization.csv
  - logs/YYYYMMDD-no-pdf-nonpdf-context-categorization-report.md
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from datetime import datetime, date
from pathlib import Path
from urllib.parse import urlparse

from vault_config import LOGS_DIR, PAPERS_DIR, PDFS_DIR


NA_VALUES = {"", "N/A", "NA", "NO_PDF_APPLICABLE", "NONE", "NULL"}


PRIMARY_CATEGORIES = [
    "Toxicity/Hate Speech",
    "Bias/Fairness",
    "AI Safety/Alignment",
    "General Ethics/Values",
    "Machine Translation/Multilingual",
    "Dataset/Benchmark Resource",
    "Other/Unclear",
]


def clean(value: str) -> str:
    return (value or "").strip().strip('"').strip("'").strip()


def parse_frontmatter(content: str) -> tuple[dict, str]:
    # Handles optional UTF-8 BOM at the beginning.
    content = content.lstrip("\ufeff")
    match = re.match(r"---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content

    fm_raw = match.group(1)
    body = match.group(2)
    fields = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields, body


def parse_local_pdf_ref(raw_value: str) -> str:
    value = clean(raw_value)
    if not value:
        return ""
    wiki_match = re.fullmatch(r"\[\[(.+?)\]\]", value)
    if wiki_match:
        value = wiki_match.group(1).split("|", 1)[0].strip()
    return value


def extract_title(content: str, fields: dict) -> str:
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return clean(fields.get("short_title", "")) or Path(fields.get("key", "")).stem


def is_direct_pdf_url(url: str) -> bool:
    url_l = url.lower()
    if url_l.endswith(".pdf"):
        return True
    if "arxiv.org/pdf/" in url_l:
        return True
    # Common direct-download query hints.
    if "download=1" in url_l or "blobtype=pdf" in url_l:
        return True
    return False


def get_non_pdf_context_urls(fields: dict) -> list[str]:
    urls = []
    for key in ("url", "external_pdf"):
        value = clean(fields.get(key, ""))
        if not value:
            continue
        if value.upper() in NA_VALUES:
            continue
        if value.lower().startswith("file://"):
            continue
        if is_direct_pdf_url(value):
            continue
        if value.startswith("http://") or value.startswith("https://"):
            urls.append(value)
    # Preserve insertion order while removing duplicates.
    deduped = []
    seen = set()
    for u in urls:
        if u not in seen:
            deduped.append(u)
            seen.add(u)
    return deduped


def has_local_pdf(paper_path: Path, fields: dict, pdf_names: set[str]) -> bool:
    local_raw = fields.get("local_pdf", None)
    ref = parse_local_pdf_ref(local_raw) if local_raw is not None else ""
    has_ref_pdf = Path(ref).name in pdf_names if ref else False
    has_stem_pdf = f"{paper_path.stem}.pdf" in pdf_names
    return has_ref_pdf or has_stem_pdf


def source_type_from_url(url: str) -> str:
    u = clean(url)
    if not u:
        return "unknown"
    parsed = urlparse(u)
    host = (parsed.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]

    if any(x in host for x in ("arxiv.org", "aclanthology.org", "openreview.net", "semanticscholar.org")):
        return "scholarly-index"
    if any(x in host for x in ("github.com", "huggingface.co", "gitlab.com")):
        return "code-repo"
    if any(x in host for x in ("wordpress.com", "medium.com", "substack.com")) or "blog" in host:
        return "blog"
    if any(
        x in host
        for x in (
            "doi.org",
            "springer.com",
            "nature.com",
            "sciencedirect.com",
            "wiley.com",
            "tandfonline.com",
            "plos.org",
            "frontiersin.org",
            "ieee.org",
            "acm.org",
            "jstor.org",
            "elsevier.com",
        )
    ):
        return "publisher-journal"
    if host.endswith(".edu") or ".edu." in host or host.endswith(".ac.uk"):
        return "academic-site"
    if host.endswith(".org"):
        return "org-site"
    return "web-other"


def map_from_ethics_perspective(value: str) -> str:
    v = clean(value).lower()
    if not v or v in {"unknown", "n/a", "na"}:
        return ""
    if any(x in v for x in ("toxicity", "hate", "offensive")):
        return "Toxicity/Hate Speech"
    if any(x in v for x in ("bias", "fairness", "stereotype")):
        return "Bias/Fairness"
    if any(x in v for x in ("safety", "alignment", "jailbreak", "red-team")):
        return "AI Safety/Alignment"
    if any(x in v for x in ("ethics", "moral", "values", "virtue", "deont", "utilitarian", "machine ethics")):
        return "General Ethics/Values"
    return ""


def map_from_research_topic(value: str) -> str:
    v = clean(value).lower()
    if not v or v in {"unknown", "n/a", "na"}:
        return ""
    if any(x in v for x in ("machine translation", "multilingual", "cross-lingual", "language modeling")):
        return "Machine Translation/Multilingual"
    if any(x in v for x in ("bias", "fairness", "stereotype")):
        return "Bias/Fairness"
    if any(x in v for x in ("safety", "alignment")):
        return "AI Safety/Alignment"
    if any(x in v for x in ("ethics", "moral", "values", "phronesis")):
        return "General Ethics/Values"
    if any(x in v for x in ("toxicity", "hate", "offensive")):
        return "Toxicity/Hate Speech"
    return ""


def infer_category(title: str, abstract: str, urls: list[str], flags: dict) -> str:
    text = f"{title} {abstract}".lower()

    if any(flags.get(k, False) for k in ("is_benchmark", "is_eval", "is_dataset")) and any(
        x in text for x in ("benchmark", "dataset", "corpus", "evaluation suite", "leaderboard")
    ):
        return "Dataset/Benchmark Resource"
    if any(x in text for x in ("hate speech", "offensive", "toxicity", "abusive language", "counter-speech")):
        return "Toxicity/Hate Speech"
    if any(x in text for x in ("bias", "fairness", "stereotype", "disparit", "debias")):
        return "Bias/Fairness"
    if any(x in text for x in ("jailbreak", "guardrail", "red-team", "ai safety", "safety benchmark")):
        return "AI Safety/Alignment"
    if any(x in text for x in ("ethics", "moral", "values", "virtue", "deontolog", "utilitarian")):
        return "General Ethics/Values"
    if any(x in text for x in ("machine translation", "multilingual", "cross-lingual", "low-resource language")):
        return "Machine Translation/Multilingual"
    if any(x in text for x in ("benchmark", "dataset", "corpus", "evaluation suite")):
        return "Dataset/Benchmark Resource"
    if any("github.com" in u.lower() or "huggingface.co" in u.lower() for u in urls):
        return "Dataset/Benchmark Resource"
    return "Other/Unclear"


def parse_yes_no_flag(value: str) -> bool:
    return clean(value).lower() == "yes"


def assign_primary_category(fields: dict, title: str, abstract: str, context_urls: list[str]) -> tuple[str, str]:
    ethics = clean(fields.get("ethics_perspective", ""))
    research = clean(fields.get("research_topic", ""))
    flags = {
        "is_benchmark": parse_yes_no_flag(fields.get("is_benchmark", "")),
        "is_eval": parse_yes_no_flag(fields.get("is_eval", "")),
        "is_dataset": parse_yes_no_flag(fields.get("is_dataset", "")),
    }

    cat = map_from_ethics_perspective(ethics)
    if cat:
        return cat, f"ethics_perspective:{ethics}"

    cat = map_from_research_topic(research)
    if cat:
        return cat, f"research_topic:{research}"

    inferred = infer_category(title, abstract, context_urls, flags)
    return inferred, f"heuristic:title_abstract_url:{inferred}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate no-PDF non-PDF-context categorization report")
    parser.add_argument("--date-prefix", default=date.today().strftime("%Y%m%d"))
    args = parser.parse_args()

    date_prefix = args.date_prefix
    generated_at = datetime.now().isoformat(timespec="seconds")

    pdf_names = {p.name for p in PDFS_DIR.rglob("*.pdf")}

    rows = []
    for paper in sorted(PAPERS_DIR.glob("*.md")):
        content = paper.read_text(encoding="utf-8", errors="ignore")
        fields, body = parse_frontmatter(content)

        if has_local_pdf(paper, fields, pdf_names):
            continue

        context_urls = get_non_pdf_context_urls(fields)
        if not context_urls:
            continue

        title = extract_title(content, fields)
        abstract = clean(fields.get("abstract", ""))
        primary_category, reason = assign_primary_category(fields, title, abstract, context_urls)

        source_url = context_urls[0]
        source_type = source_type_from_url(source_url)
        source_domain = urlparse(source_url).netloc.lower()

        is_benchmark = "Yes" if parse_yes_no_flag(fields.get("is_benchmark", "")) else "No"
        is_eval = "Yes" if parse_yes_no_flag(fields.get("is_eval", "")) else "No"
        is_dataset = "Yes" if parse_yes_no_flag(fields.get("is_dataset", "")) else "No"

        year = clean(fields.get("year", "")) or "Unknown"

        row = {
            "paper": paper.name,
            "title": title,
            "year": year,
            "url": source_url,
            "source_domain": source_domain,
            "source_type": source_type,
            "ethics_perspective": clean(fields.get("ethics_perspective", "")) or "Unknown",
            "research_topic": clean(fields.get("research_topic", "")) or "Unknown",
            "is_benchmark": is_benchmark,
            "is_eval": is_eval,
            "is_dataset": is_dataset,
            "primary_category": primary_category,
            "assignment_reason": reason,
        }
        rows.append(row)

    rows.sort(key=lambda r: (r["primary_category"], r["paper"]))

    csv_path = LOGS_DIR / f"{date_prefix}-no-pdf-nonpdf-context-categorization.csv"
    md_path = LOGS_DIR / f"{date_prefix}-no-pdf-nonpdf-context-categorization-report.md"

    csv_fields = [
        "paper",
        "title",
        "year",
        "url",
        "source_domain",
        "source_type",
        "ethics_perspective",
        "research_topic",
        "is_benchmark",
        "is_eval",
        "is_dataset",
        "primary_category",
        "assignment_reason",
    ]

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    by_category = Counter(r["primary_category"] for r in rows)
    by_source = Counter(r["source_type"] for r in rows)
    by_year = Counter(r["year"] for r in rows)
    by_combo = Counter(
        ",".join(
            [
                *("is_benchmark" for _ in [0] if r["is_benchmark"] == "Yes"),
                *("is_eval" for _ in [0] if r["is_eval"] == "Yes"),
                *("is_dataset" for _ in [0] if r["is_dataset"] == "Yes"),
            ]
        )
        or "none"
        for r in rows
    )
    by_category_rows = defaultdict(list)
    for r in rows:
        by_category_rows[r["primary_category"]].append(r)

    lines = []
    lines.append("# No-PDF Papers with Non-PDF Context: Categorization Report")
    lines.append("")
    lines.append(f"Generated: {generated_at}")
    lines.append(f"Date prefix: `{date_prefix}`")
    lines.append(f"Source papers dir: `{PAPERS_DIR}`")
    lines.append(f"Source PDFs dir: `{PDFS_DIR}`")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"- Selected papers (no local PDF + non-PDF context URL): **{len(rows)}**")
    lines.append(f"- Categories used: **{', '.join(PRIMARY_CATEGORIES)}**")
    lines.append("- Primary category assignment precedence:")
    lines.append("1. `ethics_perspective`")
    lines.append("2. `research_topic`")
    lines.append("3. Title/abstract/URL heuristic inference")
    lines.append("")

    lines.append("## Primary Category Distribution")
    lines.append("")
    lines.append("| Category | Count |")
    lines.append("|---|---:|")
    for category in PRIMARY_CATEGORIES:
        lines.append(f"| {category} | {by_category.get(category, 0)} |")
    lines.append("")

    lines.append("## Source Type Distribution")
    lines.append("")
    lines.append("| Source Type | Count |")
    lines.append("|---|---:|")
    for key, count in sorted(by_source.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {key} | {count} |")
    lines.append("")

    lines.append("## Benchmark/Eval/Dataset Flags")
    lines.append("")
    lines.append("| Flag Combo | Count |")
    lines.append("|---|---:|")
    for key, count in sorted(by_combo.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {key} | {count} |")
    lines.append("")

    lines.append("## Year Distribution")
    lines.append("")
    lines.append("| Year | Count |")
    lines.append("|---|---:|")
    for key, count in sorted(by_year.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {key} | {count} |")
    lines.append("")

    lines.append("## Category Summaries")
    lines.append("")
    for category in PRIMARY_CATEGORIES:
        subset = by_category_rows.get(category, [])
        if not subset:
            continue
        sub_source = Counter(r["source_type"] for r in subset)
        top_source = ", ".join(f"{k}:{v}" for k, v in sub_source.most_common(3))
        lines.append(f"### {category} ({len(subset)})")
        lines.append(f"- Dominant source types: {top_source}")
        lines.append("- Sample papers:")
        for sample in subset[:5]:
            lines.append(f"  - `{sample['paper']}` ({sample['year']}, {sample['source_type']})")
        lines.append("")

    lines.append("## Per-Paper Appendix")
    lines.append("")
    for category in PRIMARY_CATEGORIES:
        subset = by_category_rows.get(category, [])
        if not subset:
            continue
        lines.append(f"### {category}")
        lines.append("")
        lines.append("| Paper | Year | Source Type | Domain | Assignment Reason |")
        lines.append("|---|---:|---|---|---|")
        for r in subset:
            paper = f"`{r['paper']}`"
            year = r["year"]
            stype = r["source_type"]
            domain = r["source_domain"] or "unknown"
            reason = r["assignment_reason"]
            lines.append(f"| {paper} | {year} | {stype} | {domain} | {reason} |")
        lines.append("")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"selected={len(rows)}")
    print(f"csv={csv_path}")
    print(f"report={md_path}")


if __name__ == "__main__":
    main()

