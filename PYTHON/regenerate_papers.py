#!/usr/bin/env python3
"""Regenerate all paper markdown files with URLs properly included."""

import csv
import re
from pathlib import Path

from vault_config import WORKSPACE_ROOT, PAPERS_DIR

# Additional URLs found for papers that were missing them
ADDITIONAL_URLS = {
    "RNDCEFC4": {"arxiv": "https://arxiv.org/abs/2507.02088", "acl": "https://aclanthology.org/2025.findings-acl.313/"},
    "BY3E46VS": {"acl": "https://aclanthology.org/2025.naacl-long.600/", "openreview": "https://openreview.net/forum?id=zSwnz6BsDa"},
    "MAHWYKT8": {"acl": "https://aclanthology.org/2020.trac-1.3/", "semantic_scholar": "https://www.semanticscholar.org/paper/22428dc028d3d953e4722f16af4512e2592cdf58"},
    "2IXQNVL4": {"aaai": "https://ojs.aaai.org/index.php/AAAI-SS/article/view/35590"},
    "JALT756H": {"ssrn": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3205286"},
    "MTV37PE2": {"arxiv": "https://arxiv.org/abs/2406.09123", "acl": "https://aclanthology.org/2025.findings-naacl.337/"},
    "QURKVCVW": {"arxiv": "https://arxiv.org/abs/2503.02374", "acl": "https://aclanthology.org/2025.naacl-industry.34/"},
    "RSLK7KS9": {"arxiv": "https://arxiv.org/abs/2306.11432"},
    "SRKAQM3X": {"semantic_scholar": "https://www.semanticscholar.org/paper/f8e9851f175d9f8b87201118906b39f5491041b1"},
    "JCYY44E4": {"arxiv": "https://arxiv.org/abs/2311.05112"},
    "4YDBJ27I": {"arxiv": "https://arxiv.org/abs/2402.04464"},
    "RL573MSX": {"arxiv": "https://arxiv.org/abs/2404.06750"},
    "3RNRAN7W": {"arxiv": "https://arxiv.org/abs/2410.19812", "github": "https://github.com/MxEddie/Ethics-Whitepaper"},
    "HRXS9ILQ": {"arxiv": "https://arxiv.org/abs/2502.10174"},
    "ZCHG4W4T": {"arxiv": "https://arxiv.org/abs/2504.15125"},
    "XWUV45S3": {"arxiv": "https://arxiv.org/abs/2508.11534"},
    "8HB8V7WZ": {"arxiv": "https://arxiv.org/abs/2408.06210"},
    "VVVLTVIR": {"arxiv": "https://arxiv.org/abs/2308.01525", "github": "https://github.com/jiyounglee-0523/VisAlign"},
    "JRW7RCQN": {"arxiv": "https://arxiv.org/abs/2410.19317", "github": "https://github.com/FanZT6/FairMT-bench"},
    "7FLQPGMT": {"arxiv": "https://arxiv.org/abs/2501.12612", "github": "https://github.com/adwardlee/t2i_safety"},
    "GHNYTYDF": {"stanford": "https://crfm.stanford.edu/2024/11/08/helm-safety.html", "github": "https://github.com/stanford-crfm/helm"},
    "9WY3JY6S": {"conference": "https://nomadit.co.uk/conference/africaknows/paper/57969", "journal": "https://www.emerald.com/insight/content/doi/10.1108/JICES-04-2022-0037/full/html"},
    "ESZUEQJQ": {"arxiv": "https://arxiv.org/abs/2501.03200", "deepmind": "https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/"},
    "ABZUCNSW": {"springer": "https://link.springer.com/chapter/10.1007/978-3-031-93415-5_6", "github": "https://github.com/coairesearch/mapping_moral_reasoning"},
    "NCKQ4LJ6": {"journal": "https://jisem-journal.com/index.php/journal/article/view/12555"},
    "FDB79D6M": {"arxiv": "https://arxiv.org/abs/2504.21848"},
    "U6X9LC4B": {"guilford": "https://guilfordjournals.com/doi/10.1521/soco.2021.39.1.139", "pdf": "https://scholar.harvard.edu/files/slevine/files/levine_et_al_2021_religion_and_morality.pdf"}
}

def sanitize_filename(title, key):
    """Create a safe filename from the paper title."""
    if not title:
        return f"paper_{key}"
    sanitized = re.sub(r'[<>:"/\\|?*]', '', title)
    sanitized = re.sub(r'\s+', ' ', sanitized).strip()
    if len(sanitized) > 100:
        sanitized = sanitized[:100].rsplit(' ', 1)[0]
    return sanitized or f"paper_{key}"

def create_markdown(row):
    """Create markdown content for a paper."""
    key = row.get('Key', '')
    lines = []

    # YAML frontmatter
    lines.append("---")
    lines.append(f"key: {key}")
    lines.append(f"type: {row.get('Item Type', '')}")

    year = row.get('Publication Year', '')
    if year:
        lines.append(f"year: {year}")

    authors = row.get('Author', '')
    if authors:
        authors_escaped = authors.replace('"', '\\"')
        lines.append(f'authors: "{authors_escaped}"')

    doi = row.get('DOI', '')
    if doi:
        lines.append(f"doi: {doi}")

    # Tags
    manual_tags = row.get('Manual Tags', '')
    auto_tags = row.get('Automatic Tags', '')
    all_tags = []
    if manual_tags:
        all_tags.extend([t.strip() for t in manual_tags.split(';') if t.strip()])
    if auto_tags:
        all_tags.extend([t.strip() for t in auto_tags.split(';') if t.strip()])
    if all_tags:
        lines.append("tags:")
        for tag in all_tags[:20]:
            tag_clean = tag.replace('"', '').replace(':', '-')
            lines.append(f'  - "{tag_clean}"')

    lines.append("---")
    lines.append("")

    # Title
    title = row.get('Title', 'Untitled')
    lines.append(f"# {title}")
    lines.append("")

    # Metadata section
    lines.append("## Metadata")
    lines.append("")

    if authors:
        lines.append(f"**Authors:** {authors}")
        lines.append("")

    if year:
        lines.append(f"**Year:** {year}")
        lines.append("")

    pub_title = row.get('Publication Title', '')
    if pub_title:
        lines.append(f"**Publication:** {pub_title}")
        lines.append("")

    item_type = row.get('Item Type', '')
    if item_type:
        lines.append(f"**Type:** {item_type}")
        lines.append("")

    if doi:
        lines.append(f"**DOI:** [{doi}](https://doi.org/{doi})")
        lines.append("")

    pages = row.get('Pages', '')
    if pages:
        lines.append(f"**Pages:** {pages}")
        lines.append("")

    volume = row.get('Volume', '')
    issue = row.get('Issue', '')
    if volume or issue:
        vol_issue = []
        if volume:
            vol_issue.append(f"Vol. {volume}")
        if issue:
            vol_issue.append(f"Issue {issue}")
        lines.append(f"**Volume/Issue:** {', '.join(vol_issue)}")
        lines.append("")

    publisher = row.get('Publisher', '')
    if publisher:
        lines.append(f"**Publisher:** {publisher}")
        lines.append("")

    # Links section - gather all URLs
    urls = {}

    # Original URL from Zotero
    url = row.get('Url', '').strip()
    if url:
        if 'arxiv.org' in url:
            urls['arXiv'] = url
        elif 'doi.org' in url:
            urls['DOI'] = url
        elif 'aclanthology' in url:
            urls['ACL Anthology'] = url
        elif 'semanticscholar' in url:
            urls['Semantic Scholar'] = url
        else:
            urls['URL'] = url

    # Additional URLs found through search
    if key in ADDITIONAL_URLS:
        for source, link in ADDITIONAL_URLS[key].items():
            source_name = source.replace('_', ' ').title()
            if source_name not in urls:
                urls[source_name] = link

    # DOI link if we have DOI but no URL
    if doi and 'DOI' not in urls:
        urls['DOI'] = f"https://doi.org/{doi}"

    if urls:
        lines.append("## Links")
        lines.append("")
        for source, link in urls.items():
            lines.append(f"- **{source}:** {link}")
        lines.append("")

    # Abstract
    abstract = row.get('Abstract Note', '')
    if abstract:
        lines.append("## Abstract")
        lines.append("")
        lines.append(abstract)
        lines.append("")

    # Notes section
    lines.append("## Notes")
    lines.append("")
    lines.append("")

    # Tags display
    if all_tags:
        lines.append("## Tags")
        lines.append("")
        tag_links = [f"#{tag.replace(' ', '-').replace(':', '-')}" for tag in all_tags[:20]]
        lines.append(" ".join(tag_links))
        lines.append("")

    # Citation info
    extra = row.get('Extra', '')
    if extra and 'citations' in extra.lower():
        lines.append("## Citation Info")
        lines.append("")
        lines.append(extra)
        lines.append("")

    return '\n'.join(lines)

def main():
    csv_path = WORKSPACE_ROOT / "Base.md"
    output_dir = PAPERS_DIR

    # Read CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Regenerating {len(rows)} papers")

    for row in rows:
        key = row.get('Key', '')
        title = row.get('Title', '')

        if not key:
            continue

        try:
            filename = sanitize_filename(title, key)
            filepath = output_dir / f"{filename}.md"

            # Handle duplicate filenames
            counter = 1
            original_filepath = filepath
            while filepath.exists():
                # Check if it's the same paper (same key)
                existing_content = filepath.read_text(encoding='utf-8')
                if f"key: {key}" in existing_content:
                    break  # Same paper, overwrite
                filepath = output_dir / f"{filename} ({counter}).md"
                counter += 1

            content = create_markdown(row)
            filepath.write_text(content, encoding='utf-8')

        except Exception as e:
            print(f"Error processing {key}: {e}")

    print("Done!")

if __name__ == "__main__":
    main()
