#!/usr/bin/env python3
"""Parse 10-references.md and create BACKGROUND-registry.json + per-folder YAML stubs."""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
BG_DIR = SCRIPT_DIR.parent                       # CULTURAL-GLOBAL/BACKGROUND/
PAPER_DIR = BG_DIR.parent / "PAPER"
REF_FILE = PAPER_DIR / "10-references.md"
REGISTRY_FILE = BG_DIR / "BACKGROUND-registry.json"

# ── Folder mapping: author last-name → folder ────────────────────────────────
AUTHOR_FOLDER_MAP: dict[str, str] = {
    # 01 WEIRD / cross-cultural psychology
    "Henrich":     "01-weird-cross-cultural-psychology",
    "Apicella":    "01-weird-cross-cultural-psychology",
    "Rad":         "01-weird-cross-cultural-psychology",
    "Atari":       "01-weird-cross-cultural-psychology",
    "Hofstede":    "01-weird-cross-cultural-psychology",
    "Schwartz":    "01-weird-cross-cultural-psychology",
    "Inglehart":   "01-weird-cross-cultural-psychology",
    "Gilligan":    "01-weird-cross-cultural-psychology",
    "Held":        "01-weird-cross-cultural-psychology",
    # 02 AI ethics landscape
    "Jobin":       "02-ai-ethics-landscape",
    "Hagerty":     "02-ai-ethics-landscape",
    "Schiff":      "02-ai-ethics-landscape",
    "Floridi":     "02-ai-ethics-landscape",
    "UNESCO":      "02-ai-ethics-landscape",
    "Whittlestone":"02-ai-ethics-landscape",
    "Madaio":      "02-ai-ethics-landscape",
    "Zhang":       "02-ai-ethics-landscape",
    "Ciston":      "02-ai-ethics-landscape",
    "Bender":      "02-ai-ethics-landscape",
    "Zuboff":      "02-ai-ethics-landscape",
    # 03 Values alignment
    "Gabriel":     "03-values-alignment",
    "Russell":     "03-values-alignment",
    "Sorensen":    "03-values-alignment",
    "Kirk":        "03-values-alignment",
    "Durmus":      "03-values-alignment",
    # 04 Confucian
    "Wong":        "04-confucian-ethics-ai",
    "Hou":         "04-confucian-ethics-ai",
    "Angle":       "04-confucian-ethics-ai",
    "So":          "04-confucian-ethics-ai",
    "Deng":        "04-confucian-ethics-ai",
    "Qian":        "04-confucian-ethics-ai",
    "Yao":         "04-confucian-ethics-ai",
    # 05 Ubuntu
    "Mhlambi":     "05-ubuntu-philosophy-ai",
    "Birhane":     "05-ubuntu-philosophy-ai",   # default; 2024 w/ Guest overridden below
    "Gwagwa":      "05-ubuntu-philosophy-ai",
    "Mokoena":     "05-ubuntu-philosophy-ai",
    "van Norren":  "05-ubuntu-philosophy-ai",
    "Suliman":     "05-ubuntu-philosophy-ai",
    # 06 Islamic
    "Alyemny":     "06-islamic-ethics-ai",
    "Munshi":      "06-islamic-ethics-ai",
    "Abdalla":     "06-islamic-ethics-ai",
    # 07 Buddhist
    "Hongladarom": "07-buddhist-ethics-ai",
    # 08 Dharmic
    "Varshney":    "08-dharmic-ethics-ai",
    # 09 Indigenous
    "Carroll":     "09-indigenous-relational-ai",
    "Brown":       "09-indigenous-relational-ai",
    "Munn":        "09-indigenous-relational-ai",
    "Keegan":      "09-indigenous-relational-ai",
    # 11 Decolonial
    "Mohamed":     "11-decolonial-ai-power",
    "Prabhakaran": "11-decolonial-ai-power",
    "Sambasivan":  "11-decolonial-ai-power",
    "Adams":       "11-decolonial-ai-power",
    "Dobbe":       "11-decolonial-ai-power",
    "Zong":        "11-decolonial-ai-power",
    # 12 Methodology
    "Greenacre":   "12-methodology-references",
    "Benzecri":    "12-methodology-references",
    # 13 Cross-cultural AI fairness
    "Awad":        "13-cross-cultural-ai-fairness",
    "Zimerman":    "13-cross-cultural-ai-fairness",
    "Talat":       "13-cross-cultural-ai-fairness",
    "Jakesch":     "13-cross-cultural-ai-fairness",
}

# Special overrides for authors appearing under multiple folders
# Key = (first_author_last, year_str)
OVERRIDE_MAP: dict[tuple[str, str], str] = {
    ("Birhane", "2024"): "11-decolonial-ai-power",  # Birhane & Guest 2024 → decolonial
}

# ── References cited in 02-background.md (get priority "must_read") ──────────
# Identified by reading the background section
MUST_READ_KEYS: set[tuple[str, str]] = {
    ("Henrich", "2010"),
    ("Awad", "2018"),
    ("Rad", "2018"),
    ("Apicella", "2020"),
    ("Russell", "2019"),
    ("Gabriel", "2020"),
    ("Angle", "2021"),
    ("Mhlambi", "2020"),
    ("Floridi", "2018"),
    ("Wong", "2020"),
    ("Hou", "2023"),
    ("So", "2024"),
    ("Gwagwa", "2022"),
    ("Mokoena", "2024"),
    ("Suliman", "2024"),
    ("Munshi", "2021"),
    ("Alyemny", "2023"),
    ("Hongladarom", "2020"),
    ("Varshney", "2024"),
    ("Carroll", "2020"),
    ("Keegan", "2024"),
    ("Brown", "2024"),
    ("Jobin", "2019"),
    ("Hagerty", "2019"),
    ("Birhane", "2021"),
    ("Sambasivan", "2021"),
    ("Munn", "2023"),
}

# ── Topic tags by folder ─────────────────────────────────────────────────────
FOLDER_TAGS: dict[str, list[str]] = {
    "01-weird-cross-cultural-psychology": ["WEIRD", "cross-cultural-psychology"],
    "02-ai-ethics-landscape":            ["AI-ethics", "guidelines-landscape"],
    "03-values-alignment":               ["values-alignment", "pluralistic-alignment"],
    "04-confucian-ethics-ai":            ["Confucian-ethics", "AI-governance"],
    "05-ubuntu-philosophy-ai":           ["Ubuntu", "relational-ethics"],
    "06-islamic-ethics-ai":              ["Islamic-ethics", "Maqasid-al-Shariah"],
    "07-buddhist-ethics-ai":             ["Buddhist-ethics", "AI-ethics"],
    "08-dharmic-ethics-ai":              ["Dharmic-ethics", "Hindu-philosophy"],
    "09-indigenous-relational-ai":       ["Indigenous-AI", "data-sovereignty"],
    "10-buen-vivir-ai":                  ["Buen-Vivir", "Sumak-Kawsay"],
    "11-decolonial-ai-power":            ["decolonial-AI", "power-structures"],
    "12-methodology-references":         ["correspondence-analysis", "methodology"],
    "13-cross-cultural-ai-fairness":     ["cross-cultural", "AI-fairness"],
}


# ── Parser ────────────────────────────────────────────────────────────────────

def parse_references(text: str) -> list[dict]:
    """Parse the references markdown into structured records."""
    entries: list[dict] = []

    # Split on blank-line-separated paragraphs (each reference is one paragraph)
    paragraphs = re.split(r'\n\n+', text.strip())

    for para in paragraphs:
        para = para.strip()
        if not para or para.startswith('#'):
            continue

        record = parse_one_reference(para)
        if record:
            entries.append(record)

    return entries


def parse_one_reference(raw: str) -> dict | None:
    """Parse a single APA-style reference string into a structured dict."""
    # Normalise whitespace
    raw = re.sub(r'\s+', ' ', raw).strip()

    # ── Authors & year ───────────────────────────────────────────────────
    # Pattern: Authors (YYYY). or Authors (YYYYa). or Authors (YYYYb).
    m = re.match(r'^(.+?)\s*\((\d{4}[a-z]?)\)\.\s*', raw)
    if not m:
        print(f"  [WARN] Could not parse: {raw[:80]}...")
        return None

    author_str = m.group(1).strip()
    year = m.group(2)
    rest = raw[m.end():]

    authors = parse_authors(author_str)
    first_author_last = authors[0].split(',')[0].strip() if authors else ""

    # ── Title ────────────────────────────────────────────────────────────
    title = ""
    source = ""
    doi = ""
    url = ""
    doc_type = "journal_article"

    # Strategy: find the first *italicised* block — that's either:
    #   (a) the full title of a book (no journal afterwards), or
    #   (b) the journal/proceedings name (title precedes it).
    # Look for pattern: <stuff> *Italic Block*
    italic_m = re.search(r'\*(.+?)\*', rest)

    if italic_m:
        before_italic = rest[:italic_m.start()].strip()
        italic_text = italic_m.group(1).strip()
        after_italic = rest[italic_m.end():].strip().lstrip(',').strip()

        # Is the italic block a venue/journal (keywords)?
        venue_keywords = ('Proceedings', 'Conference', 'Journal', 'Nature',
                          'Science', 'Patterns', 'IEEE', 'Minds and Machines',
                          'Philosophy', 'Ethics', 'Online Readings',
                          'Data Science', 'AI & Society', 'AI & Ethics',
                          'Behavioral and Brain', 'Evolution and Human',
                          'Personality and Social', 'National Academy',
                          'Annual Meeting', 'Carr Center')
        is_venue = any(kw.lower() in italic_text.lower() for kw in venue_keywords)

        if before_italic and is_venue:
            # Pattern: Title. In *Venue* or Title. *Journal*, vol...
            title = re.sub(r'[\.\s]*(In\s*)?$', '', before_italic).strip()
            source = italic_text
            if 'Proceedings' in source or 'Conference' in source:
                doc_type = "conference_paper"
        elif not before_italic and not is_venue:
            # Pattern: *Book Title*. Publisher.  (italic is at start, not a venue)
            title = italic_text.rstrip('.')
            doc_type = "book"
            source = after_italic.split('.')[0].strip() if after_italic else ""
            source = re.sub(r'\s*\(Original work.*?\)', '', source).strip()
        elif not before_italic and is_venue:
            # Edge case: the "title" was consumed as venue — shouldn't happen
            title = italic_text
            source = ""
        else:
            # before_italic exists but italic is not a venue — title. *arXiv*
            title = re.sub(r'[\.\s]*$', '', before_italic).strip()
            source = italic_text
            if 'arXiv' in italic_text:
                doc_type = "preprint"
    else:
        # No italics at all — plain text reference
        parts = rest.split('. ', 1)
        title = parts[0].strip().rstrip('.')
        if 'arXiv' in raw:
            doc_type = "preprint"
            source = "arXiv"

    # Clean title
    title = title.replace('---', '\u2014').replace('--', '\u2013')
    title = re.sub(r'\*', '', title)

    # ── DOI ──────────────────────────────────────────────────────────────
    doi_m = re.search(r'(?:doi:\s*|https?://doi\.org/)?(10\.\d{4,}/\S+)', raw)
    if doi_m:
        doi = doi_m.group(1).rstrip('.')

    # ── URL ──────────────────────────────────────────────────────────────
    url_m = re.search(r'(https?://\S+)', raw)
    if url_m:
        url = url_m.group(1).rstrip('.')
        if 'doi.org' in url:
            url = ""  # Don't duplicate DOI as URL

    # ── Determine folder ─────────────────────────────────────────────────
    year_clean = re.sub(r'[a-z]$', '', year)  # strip 'a'/'b' suffix
    override_key = (first_author_last, year_clean)
    if override_key in OVERRIDE_MAP:
        folder = OVERRIDE_MAP[override_key]
    elif first_author_last in AUTHOR_FOLDER_MAP:
        folder = AUTHOR_FOLDER_MAP[first_author_last]
    else:
        folder = "02-ai-ethics-landscape"  # fallback

    # ── Priority ─────────────────────────────────────────────────────────
    # Match on year without letter suffix
    priority_key = (first_author_last, year_clean)
    priority = "must_read" if priority_key in MUST_READ_KEYS else "important"

    # ── Expert source ────────────────────────────────────────────────────
    expert_source: list[int] = []  # will be populated manually later

    # ── Short title (max 5 words, title-cased) ───────────────────────────
    words = re.sub(r'[^\w\s]', '', title).split()
    short_title = ' '.join(words[:5]) if len(words) > 5 else ' '.join(words)
    # Title-case each word for filename
    short_title_tc = ' '.join(w.capitalize() for w in short_title.split())

    filename = f"{year_clean}-{first_author_last}-{short_title_tc}.md"
    local_doc = f"Documents/{year_clean}-{first_author_last}-{short_title_tc}.pdf"

    # ── Topic tags ───────────────────────────────────────────────────────
    topic_tags = list(FOLDER_TAGS.get(folder, ["AI-ethics"]))

    # ── Relevance note (auto-generated placeholder) ──────────────────────
    relevance_note = ""

    # ── Clean source ─────────────────────────────────────────────────────
    source = re.sub(r'\s*\(.*?\)\s*$', '', source).strip().rstrip(',').rstrip('.')

    return {
        "title": title,
        "authors": authors,
        "year": year_clean,
        "year_suffix": year if year != year_clean else "",
        "doi": doi,
        "url": url,
        "source": source,
        "type": doc_type,
        "priority": priority,
        "expert_source": expert_source,
        "topic_tags": topic_tags,
        "relevance_note": relevance_note,
        "local_document": local_doc,
        "document_acquired": False,
        "file": f"{folder}/{filename}",
        "folder": folder,
    }


def parse_authors(author_str: str) -> list[str]:
    """Parse APA author string into list of 'Last, First' entries."""
    # Handle special cases
    if author_str.startswith('UNESCO'):
        return ["UNESCO"]

    # Replace ' & ' with ', ' for uniform splitting
    author_str = re.sub(r'\s*&\s*', ', ', author_str)

    # Split on ', ' but be careful about 'Last, First' pairs
    # APA format: Last, F. M., Last2, F., & Last3, F.
    # Strategy: split on ', ' then re-pair consecutive elements
    parts = [p.strip() for p in author_str.split(', ') if p.strip()]

    authors: list[str] = []
    i = 0
    while i < len(parts):
        last_name = parts[i]
        # Check if next part looks like initials/first name
        if i + 1 < len(parts):
            next_part = parts[i + 1]
            # Initials: single letters with dots, or short first names
            if re.match(r'^[A-Z]\.', next_part) or (len(next_part) <= 3 and next_part.endswith('.')):
                authors.append(f"{last_name}, {next_part}")
                i += 2
                continue
            # Full first names that are clearly not last names
            elif re.match(r'^[A-Z][a-z]+$', next_part) and not (i + 2 < len(parts) and re.match(r'^[A-Z]\.', parts[i + 2])):
                # Could be "Last, Firstname" (non-initial style)
                # Check if the part after next looks like initials (meaning next_part is a last name)
                if i + 2 < len(parts) and re.match(r'^[A-Z]', parts[i + 2]) and len(parts[i + 2]) <= 4:
                    # next_part is a last name
                    authors.append(last_name)
                    i += 1
                    continue
                else:
                    authors.append(f"{last_name}, {next_part}")
                    i += 2
                    continue

        authors.append(last_name)
        i += 1

    # Cleanup
    cleaned: list[str] = []
    for a in authors:
        a = a.strip().rstrip('.').rstrip(',').strip()
        # Remove trailing comma after initials like "S. J.,"
        a = re.sub(r',\s*$', '', a)
        if a and a not in ('.', ','):
            cleaned.append(a)

    return cleaned


# ── YAML stub writer ─────────────────────────────────────────────────────────

def write_yaml_stub(record: dict) -> None:
    """Write a YAML frontmatter stub file for one reference."""
    folder_path = BG_DIR / record["folder"]
    folder_path.mkdir(parents=True, exist_ok=True)

    filepath = BG_DIR / record["file"]
    if filepath.exists():
        print(f"  [SKIP] Already exists: {record['file']}")
        return

    # Build YAML manually to preserve exact formatting
    lines = ["---"]
    lines.append(f'title: "{escape_yaml(record["title"])}"')

    lines.append("authors:")
    for a in record["authors"]:
        lines.append(f'  - "{escape_yaml(a)}"')

    lines.append(f'year: {record["year"]}')
    lines.append(f'doi: "{record["doi"]}"')
    lines.append(f'url: "{record["url"]}"')
    lines.append(f'source: "{escape_yaml(record["source"])}"')
    lines.append(f'type: "{record["type"]}"')
    lines.append(f'priority: "{record["priority"]}"')

    lines.append(f'expert_source: {json.dumps(record["expert_source"])}')

    tags_str = json.dumps(record["topic_tags"])
    lines.append(f'topic_tags: {tags_str}')

    lines.append(f'relevance_note: "{escape_yaml(record["relevance_note"])}"')
    lines.append(f'local_document: "{record["local_document"]}"')
    lines.append(f'document_acquired: false')
    lines.append("---")
    lines.append("")

    filepath.write_text('\n'.join(lines), encoding='utf-8')


def escape_yaml(s: str) -> str:
    """Escape characters problematic in YAML double-quoted strings."""
    return s.replace('\\', '\\\\').replace('"', '\\"')


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    print(f"Reading references from: {REF_FILE}")
    text = REF_FILE.read_text(encoding='utf-8')

    entries = parse_references(text)
    print(f"\nParsed {len(entries)} references.\n")

    # Write registry JSON
    # Remove internal helper field before writing
    registry = []
    for e in entries:
        rec = dict(e)
        rec.pop("year_suffix", None)
        registry.append(rec)

    REGISTRY_FILE.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f"Wrote registry: {REGISTRY_FILE}")

    # Write YAML stubs
    stubs_created = 0
    for e in entries:
        write_yaml_stub(e)
        stubs_created += 1

    # Summary by folder
    folder_counts: dict[str, int] = {}
    for e in entries:
        folder_counts[e["folder"]] = folder_counts.get(e["folder"], 0) + 1

    print(f"\n{'='*60}")
    print(f"SUMMARY: {len(entries)} references parsed, {stubs_created} stubs created")
    print(f"{'='*60}")
    for folder in sorted(folder_counts):
        count = folder_counts[folder]
        must = sum(1 for e in entries if e["folder"] == folder and e["priority"] == "must_read")
        print(f"  {folder}: {count} papers ({must} must_read)")

    print(f"\nRegistry: {REGISTRY_FILE}")
    print("Done.")


if __name__ == "__main__":
    main()
