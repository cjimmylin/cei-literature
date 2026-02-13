#!/usr/bin/env python3
"""
Classify papers by National/Ethnic/Cultural Values and Religious Values.

This script analyzes paper titles and abstracts to determine:
1. national_ethnic_cultural: Which nation, ethnic group, or culture (or N/A)
2. religious_values: Which religion/denomination (or None/Unknown/N/A)

LEARNINGS / DESIGN DECISIONS:
- Inclusive Scope: Papers describing language-specific datasets (e.g., "Indonesian hate speech")
  are tagged with their respective culture because these datasets inherently encode cultural values.
- Multi-labeling: Papers can belong to multiple cultures (e.g., "Chinese, American" for comparisons).
"""

import re
import logging
from pathlib import Path
from typing import Tuple

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter

logger = logging.getLogger(__name__)

PAPERS_DIR = Path(__file__).parent / "papers"

# Cultural/National classification patterns
CULTURAL_PATTERNS = {
    # East Asian
    "Chinese": [
        r"\bChinese\b", r"\bChina\b", r"\bMandarin\b", r"\bChinese[-\s]?speaking\b",
        r"\bConfucian\b", r"\bCMoral\b", r"\bCValue\b", r"\bWeibo\b"
    ],
    "Japanese": [
        r"\bJapanese\b", r"\bJapan\b", r"\bJCommonsense\b", r"\bJETHICS\b"
    ],
    "Korean": [
        r"\bKorean\b", r"\bKorea\b", r"\bKorNAT\b", r"\bKoSBI\b", r"\bKOME\b"
    ],
    # South/Southeast Asian
    "Indonesian": [
        r"\bIndonesian\b", r"\bIndonesia\b", r"\bIndoPref\b"
    ],
    "Indian": [
        r"\bIndian\b", r"\bIndia\b", r"\bHindi\b", r"\bPARIKSHA\b"
    ],
    "Filipino": [
        r"\bFilipino\b", r"\bPhilippines\b", r"\bTagalog\b", r"\bBatayan\b"
    ],
    "Thai": [
        r"\bThai\b", r"\bThailand\b", r"\bNorthern Thai\b"
    ],
    "Vietnamese": [
        r"\bVietnamese\b", r"\bVietnam\b"
    ],
    # Middle Eastern/Arabic
    "Arabic": [
        r"\bArabic\b", r"\bArab\b", r"\bArab[-\s]?world\b", r"\bPalm\b.*\bArab\b"
    ],
    "Iranian": [
        r"\bIranian\b", r"\bIran\b", r"\bPersian\b", r"\bFarsi\b"
    ],
    # African
    "African/Ubuntu": [
        r"\bUbuntu\b", r"\bAfrican\b", r"\bAfrica\b", r"\bSub[-\s]?Saharan\b",
        r"\bNigerian\b", r"\bNigeria\b", r"\bNaija\b", r"\bYoruba\b", r"\bAmharic\b",
        r"\bSwahili\b", r"\bAfriSenti\b"
    ],
    # European
    "French": [
        r"\bFrench\b", r"\bFrance\b", r"\bHistoires Morales\b"
    ],
    "German": [
        r"\bGerman\b", r"\bGermany\b", r"\bGermEval\b"
    ],
    "Italian": [
        r"\bItalian\b", r"\bItaly\b", r"\bITALIC\b"
    ],
    "Spanish": [
        r"\bSpanish\b", r"\bSpain\b"
    ],
    "Dutch": [
        r"\bDutch\b", r"\bNetherlands\b"
    ],
    "Russian": [
        r"\bRussian\b", r"\bRussia\b", r"\bMERA\b.*\bRussian\b", r"\bRusCode\b"
    ],
    # Americas
    "American": [
        r"\bAmerican\b", r"\bUnited States\b", r"\bU\.?S\.?\b(?!B)", r"\bAmericasNLI\b"
    ],
    "Brazilian": [
        r"\bBrazilian\b", r"\bBrazil\b", r"\bPortuguese\b"
    ],
    "Latin American": [
        r"\bLatin American\b", r"\bLatinoamerica\b"
    ],
    # Other
    "Hebrew/Israeli": [
        r"\bHebrew\b", r"\bIsrael\b", r"\bHeQ\b", r"\bParaShoot\b"
    ],
    "Australian/Aboriginal": [
        r"\bAustralian\b", r"\bAustralia\b", r"\bAboriginal\b", r"\bIndigenous Australian\b",
        r"\bYarning\b"
    ],
    "Singaporean": [
        r"\bSingapore\b", r"\bSingaporean\b", r"\bSinglish\b", r"\bRabakBench\b"
    ],
    "Western": [
        r"\bWestern values\b", r"\bWestern culture\b", r"\bWestern ethics\b",
        r"\bWestern moral\b"
    ],
    "Multicultural/Cross-cultural": [
        r"\bcross[-\s]?cultural\b", r"\bmulticultural\b", r"\bmultilingual moral\b",
        r"\bcultural diversity\b", r"\bglobal culture\b", r"\bculturally[-\s]?inclusive\b"
    ],
}

# Religious classification patterns
RELIGIOUS_PATTERNS = {
    "Islam": [
        r"\bIslam\b", r"\bMuslim\b", r"\bQuran\b", r"\bQur'an\b", r"\bHadith\b",
        r"\bFatwa\b", r"\bSharia\b", r"\bSirah\b", r"\bNabawiyah\b", r"\bHajj\b",
        r"\bIslamicPCQA\b", r"\bFatwaSet\b", r"\bQASiNa\b"
    ],
    "Christianity": [
        r"\bChristian\b", r"\bChristianity\b", r"\bBible\b", r"\bBiblical\b",
        r"\bProtestant\b", r"\bCatholic\b", r"\bEvangelical\b", r"\bGospel\b",
        r"\bWord of God\b"
    ],
    "Buddhism": [
        r"\bBuddhis[mt]\b", r"\bDharma\b", r"\bHumanistic Buddhism\b",
        r"\bHBC\b.*\bBuddhis\b"
    ],
    "Judaism": [
        r"\bJewish\b", r"\bJudaism\b", r"\bTorah\b", r"\bTalmud\b", r"\bRabbinical\b"
    ],
    "Hinduism": [
        r"\bHindu\b", r"\bHinduism\b", r"\bVedic\b", r"\bDharmic\b"
    ],
    "Sikhism": [
        r"\bSikh\b", r"\bSikhism\b", r"\bGurbani\b", r"\bGuru Granth\b"
    ],
    "Confucianism": [
        r"\bConfucian\b", r"\bConfucianism\b", r"\bConfucius\b", r"\bAnalects\b",
        r"\bMencius\b", r"\bjunzi\b", r"\bfilial piety\b", r"\bren\b.*\byi\b"
    ],
    "Taoism": [
        r"\bTaois[mt]\b", r"\bDaois[mt]\b", r"\bTao Te Ching\b", r"\bDaodejing\b",
        r"\bLaozi\b", r"\bwu wei\b", r"\bZhuangzi\b"
    ],
    "Shinto": [
        r"\bShinto\b", r"\bShintoism\b"
    ],
    "Jainism": [
        r"\bJain\b", r"\bJainism\b"
    ],
    "Baha'i": [
        r"\bBaha'i\b", r"\bBahai\b"
    ],
    "Zoroastrianism": [
        r"\bZoroastrian\b", r"\bAvesta\b", r"\bZarathustra\b"
    ],
    "Indigenous Spirituality": [
        r"\bIndigenous spiritual\b", r"\bAboriginal dreaming\b",
        r"\bNative American spiritual\b"
    ],
    "Multiple Religions": [
        r"\breligious pluralism\b", r"\binter[-\s]?religious\b",
        r"\bmultiple religions\b", r"\breligious diversity\b"
    ],
}


# Note: extract_frontmatter_and_content replaced by yaml_frontmatter_utils.read_paper


def extract_abstract(content: str) -> str:
    """Extract abstract section from markdown content."""
    # Look for ## Abstract section
    match = re.search(r'## Abstract\s*\n\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_title(content: str) -> str:
    """Extract title from markdown content."""
    # Look for # Title
    match = re.search(r'^# (.+?)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def classify_cultural(title: str, abstract: str) -> str:
    """Classify paper by national/ethnic/cultural values."""
    text = f"{title} {abstract}".lower()
    original_text = f"{title} {abstract}"
    
    matches = []
    for culture, patterns in CULTURAL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, original_text, re.IGNORECASE):
                matches.append(culture)
                break
    
    if matches:
        # Remove duplicates while preserving order
        seen = set()
        unique_matches = []
        for m in matches:
            if m not in seen:
                seen.add(m)
                unique_matches.append(m)
        return ", ".join(unique_matches)
    
    return "N/A"


def classify_religious(title: str, abstract: str) -> str:
    """Classify paper by religious values (single-label or comma-separated)."""
    original_text = f"{title} {abstract}"

    matches = []
    for religion, patterns in RELIGIOUS_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, original_text, re.IGNORECASE):
                matches.append(religion)
                break

    if matches:
        # Remove duplicates while preserving order
        seen = set()
        unique_matches = []
        for m in matches:
            if m not in seen:
                seen.add(m)
                unique_matches.append(m)
        return ", ".join(unique_matches)

    return "N/A"


def classify_religious_list(title: str, abstract: str) -> str:
    """Classify paper by ALL specific religions covered (for religious_values_list field).

    Unlike classify_religious(), this:
    - Excludes the catch-all 'Multiple Religions' from the result (keeps specific names only)
    - Returns specific religion names even when 'Multiple Religions' pattern also matches
    - Falls back to 'Multiple Religions' only if no specific religions were identified
    """
    original_text = f"{title} {abstract}"

    specific_matches = []
    has_multiple_generic = False

    for religion, patterns in RELIGIOUS_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, original_text, re.IGNORECASE):
                if religion == "Multiple Religions":
                    has_multiple_generic = True
                else:
                    specific_matches.append(religion)
                break

    if specific_matches:
        # Deduplicate while preserving order
        seen = set()
        unique = []
        for m in specific_matches:
            if m not in seen:
                seen.add(m)
                unique.append(m)
        return ", ".join(unique)

    if has_multiple_generic:
        return "Multiple Religions"

    return "N/A"


def update_frontmatter(frontmatter: str, cultural: str, religious: str,
                       religious_list: str = None) -> str:
    """Add or update cultural and religious classification in frontmatter.

    Args:
        frontmatter: Raw YAML frontmatter string
        cultural: national_ethnic_cultural value
        religious: religious_values value (single-label or comma-separated)
        religious_list: religious_values_list value (all specific religions); if None, uses religious
    """
    if religious_list is None:
        religious_list = religious

    lines = frontmatter.split('\n')
    new_lines = []

    # Remove existing properties if present, including stray dashes
    skip_next = False
    for line in lines:
        if skip_next and line.startswith('  '):
            continue
        skip_next = False

        if (line.startswith('national_ethnic_cultural:') or
                line.startswith('religious_values:') or
                line.startswith('religious_values_list:')):
            continue
        # Skip standalone dashes that might have been added erroneously
        if line.strip() == '-':
            continue
        new_lines.append(line)

    # Add new properties at the end (before any trailing empty lines)
    while new_lines and new_lines[-1].strip() == '':
        new_lines.pop()

    new_lines.append(f'national_ethnic_cultural: "{cultural}"')
    new_lines.append(f'religious_values: "{religious}"')
    new_lines.append(f'religious_values_list: "{religious_list}"')

    return '\n'.join(new_lines)


def process_paper(filepath: Path) -> Tuple[str, str, str]:
    """Process a single paper file and return classifications."""
    # Use safe YAML utilities
    frontmatter, body = read_paper(filepath)

    title = extract_title(body)
    abstract = extract_abstract(body)

    cultural = classify_cultural(title, abstract)
    religious = classify_religious(title, abstract)
    religious_list = classify_religious_list(title, abstract)

    # Update the file
    new_frontmatter = update_frontmatter(frontmatter, cultural, religious,
                                         religious_list=religious_list)

    # Validate and write back using safe utility
    is_valid, issues = validate_frontmatter(new_frontmatter)
    if not is_valid:
        logger.warning(f"  Warning: YAML validation issues in {filepath.name}: {issues}")

    write_paper(filepath, new_frontmatter, body, validate=True)

    return filepath.name, cultural, religious


def main():
    """Process all papers and generate summary."""
    papers = list(PAPERS_DIR.glob("*.md"))
    logger.info(f"Found {len(papers)} papers to process\n")
    
    cultural_counts = {}
    religious_counts = {}
    results = []
    
    for paper in sorted(papers):
        try:
            name, cultural, religious = process_paper(paper)
            results.append((name, cultural, religious))
            
            # Count cultural
            for c in cultural.split(", "):
                cultural_counts[c] = cultural_counts.get(c, 0) + 1
            
            # Count religious
            for r in religious.split(", "):
                religious_counts[r] = religious_counts.get(r, 0) + 1
                
        except Exception as e:
            logger.error(f"Error processing {paper.name}: {e}")
    
    # Print summary
    logger.info("=" * 60)
    logger.info("CULTURAL/NATIONAL/ETHNIC CLASSIFICATION SUMMARY")
    logger.info("=" * 60)
    for culture, count in sorted(cultural_counts.items(), key=lambda x: -x[1]):
        logger.info(f"  {culture}: {count}")

    logger.info("\n" + "=" * 60)
    logger.info("RELIGIOUS CLASSIFICATION SUMMARY")
    logger.info("=" * 60)
    for religion, count in sorted(religious_counts.items(), key=lambda x: -x[1]):
        logger.info(f"  {religion}: {count}")

    # Print papers with cultural classifications (non-N/A)
    logger.info("\n" + "=" * 60)
    logger.info("PAPERS WITH CULTURAL/NATIONAL/ETHNIC FOCUS")
    logger.info("=" * 60)
    cultural_papers = [(n, c, r) for n, c, r in results if c != "N/A"]
    for name, cultural, religious in sorted(cultural_papers):
        logger.info(f"  {name}")
        logger.info(f"    Cultural: {cultural}")
        if religious != "N/A":
            logger.info(f"    Religious: {religious}")

    # Print papers with religious classifications (non-N/A)
    logger.info("\n" + "=" * 60)
    logger.info("PAPERS WITH RELIGIOUS FOCUS")
    logger.info("=" * 60)
    religious_papers = [(n, c, r) for n, c, r in results if r != "N/A"]
    for name, cultural, religious in sorted(religious_papers):
        logger.info(f"  {name}")
        logger.info(f"    Religious: {religious}")
        if cultural != "N/A":
            logger.info(f"    Cultural: {cultural}")

    logger.info(f"\n\nTotal papers processed: {len(results)}")
    logger.info(f"Papers with cultural focus: {len(cultural_papers)}")
    logger.info(f"Papers with religious focus: {len(religious_papers)}")


if __name__ == "__main__":
    main()
