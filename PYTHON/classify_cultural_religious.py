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
import sys
import logging
from pathlib import Path
from typing import Tuple, Dict

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter

# Import religious scoring engine
from religious_scoring import (
    compute_all_rv_scores, derive_religious_values_string,
    derive_religious_values_list_string, load_extract, RV_FIELDS,
)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from insight_logger import InsightLogger

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
        r"\bHBC\b.*\bBuddhis\b",
        r"\bkarma\b", r"\bnirvana\b", r"\bbodhisattva\b",
        r"\bFour Noble Truths\b", r"\bEightfold Path\b", r"\bsangha\b",
        r"\bFive Precepts\b", r"\b佛教\b", r"\bDharmaBench\b", r"\bBuddhismEval\b",
        r"\bpaticcasamuppada\b", r"\bsila\b.*\bsamadhi\b",
    ],
    "Judaism": [
        r"\bJewish\b", r"\bJudaism\b", r"\bTorah\b", r"\bTalmud\b", r"\bRabbinical\b",
        r"\bhalakha\b", r"\bmitzvot\b", r"\bShabbat\b", r"\bkosher\b",
        r"\bJewish ethics\b",
    ],
    "Hinduism": [
        r"\bHindu\b", r"\bHinduism\b", r"\bVedic\b", r"\bDharmic\b",
        r"\bmoksha\b", r"\bahimsa\b", r"\batman\b",
        r"\bBhagavad Gita\b", r"\bUpanishad\b", r"\bsamsara\b",
    ],
    "Sikhism": [
        r"\bSikh\b", r"\bSikhism\b", r"\bGurbani\b", r"\bGuru Granth\b",
        r"\bKhalsa\b", r"\bFive Ks\b", r"\bWaheguru\b", r"\bsewa\b",
    ],
    "Confucianism": [
        r"\bConfucian\b", r"\bConfucianism\b", r"\bConfucius\b", r"\bAnalects\b",
        r"\bMencius\b", r"\bjunzi\b", r"\bfilial piety\b", r"\bren\b.*\byi\b"
    ],
    "Taoism": [
        r"\bTaois[mt]\b", r"\bDaois[mt]\b", r"\bTao Te Ching\b", r"\bDaodejing\b",
        r"\bLaozi\b", r"\bwu wei\b", r"\bZhuangzi\b",
        r"\byin[\s-]?yang\b", r"\bziran\b", r"\b道教\b", r"\b无为\b",
    ],
    "Shinto": [
        r"\bShinto\b", r"\bShintoism\b",
        r"\bkami\b(?=.*(?:Japan|Shinto|spirit|sacred))",
        r"\btorii\b", r"\bbushido\b", r"\bwa\b.*\bharmony\b",
        r"\bpurification ritual\b", r"\b神道\b",
    ],
    "Jainism": [
        r"\bJain\b", r"\bJainism\b",
        r"\bahimsa\b.*\b[Jj]ain\b", r"\banekantavada\b",
        r"\bMahavira\b", r"\bTirthankara\b",
    ],
    "Baha'i": [
        r"\bBaha'i\b", r"\bBahai\b"
    ],
    "Zoroastrianism": [
        r"\bZoroastrian\b", r"\bAvesta\b", r"\bZarathustra\b"
    ],
    "Ubuntu Philosophy": [
        r"\bUbuntu\b(?!.*(?:[Ll]inux|operat))",
        r"\bAfrican ethic\b", r"\bAfrican philosophy\b",
        r"\bAfrican moral\b",
    ],
    "Indigenous Spirituality": [
        r"\bIndigenous spiritual\b", r"\bAboriginal dreaming\b",
        r"\bNative American spiritual\b",
        r"\bDreamtime\b", r"\bwhakapapa\b", r"\bmana\b.*\btapu\b",
        r"\bFirst Nations?\b.*\bethic", r"\btwo[\s-]?eyed seeing\b",
        r"\bdata sovereignty\b.*\b[Ii]ndigenous\b",
        r"\belder wisdom\b", r"\bsacred land\b",
        r"\bIndigenous knowledge\b", r"\boral tradition\b.*\bethic",
        r"\bIndigenous ethic\b", r"\bIndigenous moral\b",
        r"\bdecoloniz\w+\b.*\bethic\b",
    ],
    "Multiple Religions": [
        r"\breligious pluralism\b", r"\binter[-\s]?religious\b",
        r"\bmultiple religions\b", r"\breligious diversity\b"
    ],
}


# Note: extract_frontmatter_and_content replaced by yaml_frontmatter_utils.read_paper


def classify_cultural(title: str, abstract: str, languages_list: str = "") -> str:
    """Classify paper by national/ethnic/cultural values.

    Args:
        title: Paper title
        abstract: Paper abstract
        languages_list: Value of languages_list YAML field (e.g. "Japanese, English")
    """
    text = f"{title} {abstract} {languages_list}".lower()
    original_text = f"{title} {abstract} {languages_list}"
    
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


def compute_religious_scores(title: str, abstract: str, stem: str = "") -> Dict[str, int]:
    """Compute rv_* confidence scores for all 14 religious traditions.

    Uses the canonical religious_scoring engine, loading PDF extract when available.
    """
    extract = load_extract(stem) if stem else ""
    return compute_all_rv_scores(title, abstract, extract)


def classify_religious(title: str, abstract: str) -> str:
    """Classify paper by religious values using confidence scores.

    Returns: single tradition name, "Multiple Religions", or "N/A".
    """
    scores = compute_religious_scores(title, abstract)
    return derive_religious_values_string(scores)


def classify_religious_list(title: str, abstract: str) -> str:
    """Classify paper by ALL specific religions covered (for religious_values_list field).

    Returns: comma-separated tradition names, or "N/A".
    """
    scores = compute_religious_scores(title, abstract)
    return derive_religious_values_list_string(scores)


def update_frontmatter(frontmatter: str, cultural: str, religious: str,
                       religious_list: str = None,
                       rv_scores: Dict[str, int] = None) -> str:
    """Add or update cultural and religious classification in frontmatter.

    Args:
        frontmatter: Raw YAML frontmatter string
        cultural: national_ethnic_cultural value
        religious: religious_values value (single-label or comma-separated)
        religious_list: religious_values_list value (all specific religions); if None, uses religious
        rv_scores: dict of rv_* field scores to insert between religious_values and religious_values_list
    """
    if religious_list is None:
        religious_list = religious

    lines = frontmatter.split('\n')
    new_lines = []

    # Remove existing properties if present, including stray dashes and rv_* fields
    skip_next = False
    for line in lines:
        if skip_next and line.startswith('  '):
            continue
        skip_next = False

        if (line.startswith('national_ethnic_cultural:') or
                line.startswith('religious_values:') or
                line.startswith('religious_values_list:')):
            continue
        # Remove existing rv_* score fields
        if any(line.startswith(f'{field}:') for field in RV_FIELDS):
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

    # Insert rv_* score fields between religious_values and religious_values_list
    if rv_scores:
        for field in RV_FIELDS:
            new_lines.append(f'{field}: {int(rv_scores.get(field, 0))}')

    new_lines.append(f'religious_values_list: "{religious_list}"')

    return '\n'.join(new_lines)


def process_paper(filepath: Path, ilog: InsightLogger = None) -> Tuple[str, str, str]:
    """Process a single paper file and return classifications."""
    # Use safe YAML utilities
    frontmatter, body = read_paper(filepath)

    # Capture old rv_* scores and religious_values before scoring
    old_rv_scores = {}
    old_religious = ""
    if ilog:
        for field in RV_FIELDS:
            match = re.search(rf'^{re.escape(field)}:\s*(\d+)', frontmatter, re.MULTILINE)
            if match:
                old_rv_scores[field] = int(match.group(1))
        rv_match = re.search(r'^religious_values:\s*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
        old_religious = rv_match.group(1).strip() if rv_match else ""

    # Extract title from YAML frontmatter short_title field
    title_match = re.search(r'^short_title:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ''

    # Extract abstract from YAML frontmatter abstract field
    abstract_match = re.search(r'^abstract:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    abstract = abstract_match.group(1).strip() if abstract_match else ''

    # Extract languages_list from YAML for cultural classification
    lang_match = re.search(r'^languages_list:\s*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
    languages_list = lang_match.group(1).strip() if lang_match else ""

    cultural = classify_cultural(title, abstract, languages_list)

    # Compute rv_* confidence scores using the scoring engine (with PDF extract)
    rv_scores = compute_religious_scores(title, abstract, filepath.stem)
    religious = derive_religious_values_string(rv_scores)
    religious_list = derive_religious_values_list_string(rv_scores)

    # Log rv_* reclassifications and disagreements
    if ilog:
        for field in RV_FIELDS:
            if field in old_rv_scores:
                old_val = old_rv_scores[field]
                new_val = rv_scores.get(field, 0)
                if old_val < 50 <= new_val:
                    ilog.reclassification(filepath.name, field, old_val, new_val)
                elif new_val < 50 <= old_val:
                    ilog.reclassification(filepath.name, field, old_val, new_val,
                                          f"{field} dropped below threshold: {old_val} -> {new_val}")
                elif abs(new_val - old_val) > 20:
                    ilog.disagreement(filepath.name, field, old_val, new_val)
        if old_religious and old_religious != religious:
            ilog.reclassification(filepath.name, "religious_values", old_religious, religious)

    # Update the file with rv_* scores included
    new_frontmatter = update_frontmatter(frontmatter, cultural, religious,
                                         religious_list=religious_list,
                                         rv_scores=rv_scores)

    # Validate and write back using safe utility
    is_valid, issues = validate_frontmatter(new_frontmatter)
    if not is_valid:
        logger.warning(f"  Warning: YAML validation issues in {filepath.name}: {issues}")

    write_paper(filepath, new_frontmatter, body, validate=True)

    return filepath.name, cultural, religious


def main():
    """Process all papers and generate summary."""
    ilog = InsightLogger("classify_cultural_religious")

    papers = list(PAPERS_DIR.glob("*.md"))
    logger.info(f"Found {len(papers)} papers to process\n")

    cultural_counts = {}
    religious_counts = {}
    results = []

    for paper in sorted(papers):
        try:
            name, cultural, religious = process_paper(paper, ilog)
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

    # Log summary stats
    ilog.stat(f"Processed {len(results)} papers")
    ilog.stat(f"Papers with cultural focus: {len(cultural_papers)}")
    ilog.stat(f"Papers with religious focus: {len(religious_papers)}")
    for religion, count in sorted(religious_counts.items(), key=lambda x: -x[1]):
        if religion != "N/A":
            ilog.stat(f"Religious '{religion}': {count} papers")

    ilog.finalize()


if __name__ == "__main__":
    main()
