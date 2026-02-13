#!/usr/bin/env python3
"""
LLM Assessment & Data Description Extraction Helpers.

Provides regex-based pre-extraction of LLM model names and data URLs from
PDF extract text. These helpers are used by agents during swarm processing.

Can also run standalone for testing on individual papers:

    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/assess_llm_data.py --paper "2026-Shen-PsychEthicsBench"
    ../.venv/bin/python PYTHON/assess_llm_data.py 1 5 --dry-run
"""

import argparse
import functools
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")

# =============================================================================
# LLM MODEL PATTERNS
# =============================================================================

LLM_PATTERNS = [
    # --- OpenAI ---
    r'\bGPT[-\s]?4o?[-\s]?(?:mini|turbo|preview|vision)?\b',
    r'\bGPT[-\s]?3\.?5[-\s]?(?:turbo)?\b',
    r'\bGPT[-\s]?3\b',
    r'\bGPT[-\s]?2\b',
    r'\bChatGPT\b',
    r'\bo1[-\s]?(?:mini|preview)?\b',
    r'\bo3[-\s]?(?:mini)?\b',
    r'\btext[-\s]?davinci[-\s]?\d*\b',
    r'\bInstructGPT\b',
    r'\bCODEX\b',
    # --- Anthropic ---
    r'\bClaude[-\s]?[\d.]*[-\s]?(?:instant|opus|sonnet|haiku)?\b',
    # --- Meta ---
    r'\bLlama[-\s]?[\d.]*[-\s]?(?:chat|guard)?\b',
    r'\bLLaMA[-\s]?[\d.]*\b',
    r'\bOPT[-\s]?\d+\w*\b',
    r'\bCodeLlama[-\s]?[\d.]*\b',
    # --- Google ---
    r'\bPaLM[-\s]?[\d.]*\b',
    r'\bGemini[-\s]?[\d.]*[-\s]?(?:pro|ultra|nano|flash)?\b',
    r'\bGemma[-\s]?[\d.]*\b',
    r'\bFlan[-\s]?T5[-\s]?\w*\b',
    r'\bFlan[-\s]?UL2\b',
    r'\bLaMDA\b',
    r'\bBARD\b',
    # --- Mistral ---
    r'\bMistral[-\s]?[\d.]*[-\s]?\w*\b',
    r'\bMixtral[-\s]?[\d.]*\w*\b',
    # --- Other LLMs ---
    r'\bVicuna[-\s]?[\d.]*\b',
    r'\bAlpaca[-\s]?[\d.]*\b',
    r'\bFalcon[-\s]?\d*\w*\b',
    r'\bBLOOM[-\s]?\d*\w*\b',
    r'\bQwen[-\s]?[\d.]*\w*\b',
    r'\bDeepSeek[-\s]?\w*\b',
    r'\bPhi[-\s]?\d[-\s]?\w*\b',
    r'\bGrok[-\s]?\d*\b',
    r'\bYi[-\s]?\d+\w*\b',
    r'\bDolly[-\s]?[\d.]*\b',
    r'\bZephyr[-\s]?\w*\b',
    r'\bCohere[-\s]?(?:Command|Aya)\w*\b',
    r'\bCommand[-\s]?R\+?\b',
    r'\bWizardLM[-\s]?\w*\b',
    r'\bInternLM[-\s]?\w*\b',
    r'\bBaichuan[-\s]?\w*\b',
    r'\bChatGLM[-\s]?\w*\b',
    r'\bERNIE[-\s]?(?:Bot)?\b',
    # --- Classic NLP / Pre-LLM ---
    r'\bBERT\b',
    r'\bRoBERTa\b',
    r'\bALBERT\b',
    r'\bDeBERTa[-\s]?\w*\b',
    r'\bDistilBERT\b',
    r'\bT5[-\s]?\w*\b',
    r'\bBART[-\s]?\w*\b',
    r'\bXLNet\b',
    r'\bELECTRA\b',
    r'\bWord2Vec\b',
    r'\bGloVe\b',
    r'\bELMo\b',
]

# Compile all patterns
_LLM_COMPILED = [re.compile(p, re.IGNORECASE) for p in LLM_PATTERNS]

# =============================================================================
# DATA URL PATTERNS
# =============================================================================

URL_PATTERNS = [
    r'https?://github\.com/[\w.-]+/[\w.-]+',
    r'https?://huggingface\.co/(?:datasets/)?[\w.-]+/[\w.-]+',
    r'https?://zenodo\.org/record[s]?/\d+',
    r'https?://kaggle\.com/(?:datasets/)?[\w.-]+/[\w.-]+',
    r'https?://paperswithcode\.com/[\w/-]+',
    r'https?://osf\.io/[\w]+',
    r'https?://drive\.google\.com/[\w?=&/]+',
    r'https?://figshare\.com/[\w/]+',
    r'https?://doi\.org/[\w./()-]+',
    r'https?://dataverse\.[\w.]+/[\w/]+',
    r'https?://data\.mendeley\.com/[\w/]+',
]

_URL_COMPILED = [re.compile(p) for p in URL_PATTERNS]


# =============================================================================
# EXTRACTION FUNCTIONS
# =============================================================================

def extract_llm_candidates(text):
    """
    Extract candidate LLM model names from text using regex patterns.

    Returns a sorted, deduplicated list of model name strings found in text.
    These are CANDIDATES — the LLM agent must validate which were actually
    tested vs merely cited.
    """
    candidates = set()
    for pattern in _LLM_COMPILED:
        matches = pattern.findall(text)
        for m in matches:
            cleaned = m.strip().strip('-').strip()
            if cleaned and len(cleaned) > 1:
                candidates.add(cleaned)

    # Normalize common variations
    normalized = set()
    for c in candidates:
        # Skip single-letter matches from o1/o3 patterns
        if len(c) == 1:
            continue
        # Skip common false positives
        lower = c.lower()
        if lower in ('the', 'and', 'for', 'opt', 'bar', 'bloom', 'falcon',
                      'yi', 'phi', 'bard'):
            # Only skip these if they appear as bare words without version numbers
            if not re.search(r'\d', c):
                # Check if it's actually a model reference by context
                # Keep BERT, T5, BART etc. — these are real model names
                if lower not in ('bert', 'roberta', 'albert', 'deberta',
                                 'distilbert', 't5', 'bart', 'xlnet',
                                 'electra', 'elmo', 'bloom', 'opt'):
                    continue
        normalized.add(c)

    return sorted(normalized)


def extract_url_candidates(text):
    """
    Extract candidate data/repository URLs from text.

    Returns a list of URL strings found. The LLM agent should determine which
    point to the actual dataset/benchmark (not just the paper's code repo).
    """
    urls = set()
    for pattern in _URL_COMPILED:
        matches = pattern.findall(text)
        for m in matches:
            # Clean trailing punctuation
            url = m.rstrip('.,;:)]}')
            if url:
                urls.add(url)

    return sorted(urls)


def resolve_extract_for_paper(paper_path, fm_text):
    """Resolve the PDF extract path for a paper. Returns (path_str, full_path) or (None, None)."""
    fields = parse_frontmatter(fm_text)
    extract_ref = fields.get("pdf_extract", "").strip("\"'")

    if extract_ref:
        extract_path = PAPERS_DIR.parent / extract_ref
        if extract_path.exists():
            return extract_ref, extract_path

    # Fallback: search year-based subdirs
    stem = paper_path.stem
    for subdir in sorted(PDF_EXTRACTS_DIR.iterdir()):
        if subdir.is_dir():
            candidate = subdir / "{}.md".format(stem)
            if candidate.exists():
                ref = "PDF Extracts/{}/{}".format(subdir.name, candidate.name)
                return ref, candidate

    # Fallback: root
    candidate = PDF_EXTRACTS_DIR / "{}.md".format(stem)
    if candidate.exists():
        return "PDF Extracts/{}.md".format(stem), candidate

    return None, None


def process_paper(paper_path, dry_run=False):
    """
    Process a single paper: extract LLM candidates and URL candidates.

    Returns a dict with extraction results, or None if the paper cannot be processed.
    """
    try:
        content = paper_path.read_text(encoding="utf-8")
        fm_text, body = extract_frontmatter(content)
    except (ValueError, UnicodeDecodeError) as e:
        print("  ERROR: {}: {}".format(paper_path.name, e))
        return None

    # Check if already processed
    fields = parse_frontmatter(fm_text)
    if "LLM_assessed" in fields:
        print("  SKIP (already has LLM_assessed): {}".format(paper_path.name))
        return None

    # Resolve PDF extract
    extract_ref, extract_path = resolve_extract_for_paper(paper_path, fm_text)

    extract_text = ""
    if extract_path and extract_path.exists():
        try:
            extract_text = extract_path.read_text(encoding="utf-8")
        except Exception as e:
            print("  WARN: Cannot read extract {}: {}".format(extract_ref, e))

    if not extract_text:
        print("  NO EXTRACT: {}".format(paper_path.name))
        return {
            "filename": paper_path.name,
            "has_extract": False,
            "llm_candidates": [],
            "url_candidates": [],
            "needs_manual_review": True,
        }

    # Run extraction
    llm_candidates = extract_llm_candidates(extract_text)
    url_candidates = extract_url_candidates(extract_text)

    result = {
        "filename": paper_path.name,
        "has_extract": True,
        "pdf_extract_path": extract_ref,
        "llm_candidates": llm_candidates,
        "url_candidates": url_candidates,
        "needs_manual_review": False,
    }

    if dry_run:
        print("  {} -> LLMs: {} | URLs: {}".format(
            paper_path.name,
            ", ".join(llm_candidates) if llm_candidates else "(none)",
            ", ".join(url_candidates[:3]) if url_candidates else "(none)",
        ))

    return result


def main():
    parser = argparse.ArgumentParser(
        description="LLM assessment extraction helpers (dry-run / testing)")
    parser.add_argument("start", nargs="?", type=int, default=0,
                        help="Start index (1-based)")
    parser.add_argument("end", nargs="?", type=int, default=0,
                        help="End index (1-based, inclusive)")
    parser.add_argument("--paper", type=str, default="",
                        help="Process a single paper by name (partial match)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview mode: show candidates without writing")
    args = parser.parse_args()

    all_papers = sorted(PAPERS_DIR.glob("*.md"))

    if args.paper:
        # Single paper mode
        matches = [p for p in all_papers if args.paper.lower() in p.name.lower()]
        if not matches:
            print("No paper matching '{}' found.".format(args.paper))
            sys.exit(1)
        papers = matches[:1]
        print("Processing single paper: {}".format(papers[0].name))
    elif args.start > 0 and args.end > 0:
        # Range mode (1-based)
        papers = all_papers[args.start - 1:args.end]
        print("Processing papers {} to {} ({} papers)".format(
            args.start, args.end, len(papers)))
    else:
        # Default: process all
        papers = all_papers
        print("Processing all {} papers".format(len(papers)))

    results = []
    for paper_path in papers:
        result = process_paper(paper_path, dry_run=args.dry_run)
        if result:
            results.append(result)

    # Summary
    processed = len(results)
    with_llms = sum(1 for r in results if r.get("llm_candidates"))
    with_urls = sum(1 for r in results if r.get("url_candidates"))
    no_extract = sum(1 for r in results if not r.get("has_extract"))

    print("\n=== SUMMARY ===")
    print("Processed: {}".format(processed))
    print("  With LLM candidates: {}".format(with_llms))
    print("  With URL candidates: {}".format(with_urls))
    print("  Missing extract: {}".format(no_extract))

    if args.dry_run:
        print("\n(Dry run — no changes made)")
    else:
        # Write results
        out_path = LOGS_DIR / "{}-llm_assessment_candidates.json".format(DATE_PREFIX)
        tmp_path = out_path.parent / ".tmp.{}.json".format(os.getpid())
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        os.replace(str(tmp_path), str(out_path))
        print("\nResults written to: {}".format(out_path.name))


if __name__ == "__main__":
    main()
