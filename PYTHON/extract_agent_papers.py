#!/usr/bin/env python3
"""
extract_agent_papers.py — Extract paper data from agent conversation logs
and produce JSON reports compatible with the consolidation pipeline.

Reads JSONL output files from 6 search agents (B10, C1, C2, D1, D2, D3)
that hit rate limits before writing their JSON reports. Parses WebSearch
results and assistant analysis text to reconstruct paper records.

Usage:
    python PYTHON/extract_agent_papers.py
"""

import json
import re
import sys
import os
from pathlib import Path
from collections import OrderedDict
from difflib import SequenceMatcher

# ── Agent configuration ──────────────────────────────────────────────────────

AGENTS = {
    "B10": {
        "file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/a9b298d.output",
        "languages": ["Mongolian", "Tibetan", "Uyghur", "Kyrgyz"],
    },
    "C1": {
        "file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/a66305d.output",
        "languages": ["Chinese", "Mandarin", "Cantonese", "Classical Chinese", "Min", "Hakka"],
    },
    "C2": {
        "file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/ab8d9a1.output",
        "languages": ["Japanese", "Arabic"],
    },
    "D1": {
        "file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/af0a17e.output",
        "languages": ["Multilingual"],
    },
    "D2": {
        "file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/a5c44fa.output",
        "languages": ["Quechua", "Guarani", "Maori", "Welsh", "Irish", "Hawaiian", "Navajo", "Inuktitut"],
    },
    "D3": {
        "file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/a73fc93.output",
        "languages": ["Hinglish", "Spanglish", "Arabizi", "Romanized"],
    },
}

OUTPUT_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/logs")

# ── Relevance keywords for filtering ─────────────────────────────────────────

RELEVANCE_KEYWORDS = {
    # Primary: benchmark/evaluation/dataset
    "benchmark", "evaluation", "dataset", "eval", "leaderboard",
    # Ethics/values/safety
    "ethic", "moral", "value", "safety", "safe", "alignment", "align",
    "trust", "trustworth",
    # Bias/fairness
    "bias", "fair", "fairness", "stereotyp", "discriminat",
    # Toxicity/hate
    "toxic", "hate", "offensive", "abusive", "harmful",
    # Cultural
    "cultur", "religious", "islam", "buddhist", "hindu", "christian",
    "indigenous", "dialect",
    # NLP/LLM
    "llm", "language model", "nlp", "nlu", "bert", "gpt",
    "transformer", "multilingual", "cross-lingual",
    # Low-resource
    "low-resource", "underrepresent", "minority",
}

# Domains to skip (not academic papers)
SKIP_DOMAINS = {
    "medium.com", "linkedin.com", "techrepublic.com", "siliconflow.com",
    "confident-ai.com", "evidentlyai.com", "moldstud.com", "lxt.ai",
    "llm-stats.com", "promptfoo.dev", "safetyprompts.com",
    "cluebenchmarks.com", "globaltimes.cn", "practiceguides.chambers.com",
    "secondtalent.com", "localazy.com", "chinai.substack.com",
    "aisafetychina.substack.com", "jack-clark.net", "simonwillison.net",
    "futureoflife.org", "internationalaisafetyreport.org",
    "effectivealtruism.org", "forum.effectivealtruism.org",
    "emergentmind.com", "nlpprogress.com", "babl.ai",
    "themoonlight.io",
    "chatbench.ai", "chatbench.com",
    "fugumt.com",
    "mlforhc.org",
    "talkbank.org",
    "alphaxiv.org",
    "ui.adsabs.harvard.edu",
    "slds-lmu.github.io",
    "nadi.dlnlp.ai",
    "misinforeview.hks.harvard.edu",
    "technologyreview.com",
    "cevalbenchmark.com",
    "aixplain.com",
    "swallow-llm.github.io",
    "mmluprox.github.io",
    "medinform.jmir.org",
    "deconvoluteai.com",
    "labelstud.io", "label-studio",
    "en.wikipedia.org",
    "paperswithcode.com",
    "geeksforgeeks.org",
    "scaler.com", "scalertopics.com",
    "hawaiiislandrecovery.com",
    "deepset.ai",
    "hakalau",
    "navajo.unm.edu",
    "hawaiianrecovery.com",
    "hawaiiislandrecovery.com",
}

# URLs that are clearly not papers
SKIP_URL_PATTERNS = [
    r"github\.com/.*/(?:issues|wiki|blob|tree)/",
    r"huggingface\.co/(?:spaces|blog)/",
    r"huggingface\.co/collections/",
    r"huggingface\.co/datasets/(?!.*arxiv)",  # keep if has arxiv ref
    r"aisi\.go\.jp",
    r"carnegieendowment\.org",
    r"peren\.gouv\.fr",
    r"stanford-crfm/helm",
    r"nips\.cc/media",
]


# ── Extraction helpers ────────────────────────────────────────────────────────

def extract_arxiv_id(url):
    """Extract arXiv ID from URL."""
    m = re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?', url)
    if m:
        return m.group(1)
    return None


def extract_doi(text):
    """Extract DOI from text."""
    m = re.search(r'(10\.\d{4,}/[^\s"\'<>\]]+)', text)
    if m:
        doi = m.group(1).rstrip('.')
        return doi
    return None


def extract_year_from_title(title):
    """Try to extract year from title or URL context."""
    m = re.search(r'\b(20[12]\d)\b', title)
    if m:
        year = int(m.group(1))
        if 2018 <= year <= 2026:
            return year
    return None


def extract_year_from_arxiv_id(arxiv_id):
    """Extract year from arXiv ID (YYMM format)."""
    if arxiv_id:
        yy = int(arxiv_id[:2])
        year = 2000 + yy
        if 2018 <= year <= 2026:
            return year
    return None


def get_domain(url):
    """Extract domain from URL."""
    m = re.search(r'https?://(?:www\.)?([^/]+)', url)
    return m.group(1) if m else ""


def infer_source(url):
    """Infer source from URL."""
    domain = get_domain(url)
    if "arxiv.org" in domain or "ar5iv" in domain:
        return "arXiv"
    if "aclanthology.org" in domain:
        return "ACL Anthology"
    if "springer" in domain or "link.springer" in domain:
        return "Springer"
    if "nature.com" in domain:
        return "Nature"
    if "sciencedirect.com" in domain:
        return "ScienceDirect"
    if "mdpi.com" in domain:
        return "MDPI"
    if "frontiersin.org" in domain:
        return "Frontiers"
    if "researchgate.net" in domain:
        return "ResearchGate"
    if "openreview.net" in domain:
        return "OpenReview"
    if "dl.acm.org" in domain:
        return "ACM"
    if "direct.mit.edu" in domain:
        return "MIT Press"
    if "pmc.ncbi" in domain or "pubmed" in domain:
        return "PubMed"
    if "ieee" in domain:
        return "IEEE"
    if "semanticscholar" in domain:
        return "Semantic Scholar"
    if "pnas.org" in domain:
        return "PNAS"
    if "science.org" in domain:
        return "Science"
    if "jstage.jst.go.jp" in domain:
        return "J-STAGE"
    if "peerj.com" in domain:
        return "PeerJ"
    if "kdd.org" in domain:
        return "KDD"
    if "ceur-ws.org" in domain:
        return "CEUR-WS"
    if "philarchive.org" in domain:
        return "PhilArchive"
    if "huggingface.co" in domain:
        return "Hugging Face"
    if "github.com" in domain:
        return "GitHub"
    if "anlp.jp" in domain:
        return "ANLP"
    return "Web"


def should_skip_url(url):
    """Check if URL should be skipped (non-academic)."""
    domain = get_domain(url)
    for skip_domain in SKIP_DOMAINS:
        if skip_domain in domain:
            return True
    for pattern in SKIP_URL_PATTERNS:
        if re.search(pattern, url):
            return True
    return False


def is_relevant(title, url=""):
    """Check if a paper title/URL suggests relevance to our topic."""
    text = (title + " " + url).lower()
    matches = sum(1 for kw in RELEVANCE_KEYWORDS if kw in text)
    return matches >= 1


# Language keywords for detecting whether a paper actually mentions agent languages
AGENT_LANGUAGE_KEYWORDS = {
    "B10": [r'\bmongol', r'\btibet', r'\buyghur', r'\buighur', r'\bkyrgyz',
            r'\bcentral\s+asian', r'\btibstc', r'\btlue\b', r'\bmm-eval',
            r'\bmilic', r'\bminority\s+lang', r'\binner\s+asian', r'\bturneric',
            r'\bturkic', r'\bkyrgyznlp', r'\bkyrgyzbert'],
    "C1": [r'\bchinese', r'\bcantonese', r'\bmandarin', r'\b中文', r'\bhakka',
           r'\bmin\b.*dialect', r'\bminnan', r'\bclassical\s+chinese', r'\b古文',
           r'\bchinese-specific', r'\bcvalues', r'\bsuperclue', r'\bc-eval',
           r'\bcmmlu', r'\bclue\b.*chinese', r'\bflames\b', r'\bsafetybench'],
    "C2": [r'\bjapanese', r'\barabic', r'\b日本', r'\bjglue\b', r'\bjbbq\b',
           r'\bsobaco\b', r'\baratrust', r'\bislamtrust', r'\baradice',
           r'\bdialectal\s*arabic', r'\babsher\b', r'\bpalm\b.*arab',
           r'\bgulf', r'\blevant', r'\begyptian\s+arabic', r'\bmsa\b',
           r'\bislamic', r'\bhijri', r'\barabicnlp', r'\bjapan(?:ese)?'],
    "D1": None,  # Multilingual agent — no specific language filter
    "D2": [r'\bquechua', r'\bguarani', r'\bm[aā]ori', r'\bwelsh', r'\birish\b(?! coffee)',
           r'\bhawaiian\b(?!\s+(?:island|recovery|resort|hotel))', r'\bnavajo', r'\binuktitut', r'\binuit',
           r'\bindigenous.*(?:lang|nlp|model|evaluat|benchmark|dataset)',
           r'(?:lang|nlp|model|evaluat|benchmark|dataset).*\bindigenous',
           r'\blow-resource.*(?:lang|indigen)', r'\bendanger.*lang',
           r'\bceltic.*(?:lang|nlp)', r'\bunder-?represented.*lang',
           r'\bunder-?resourced.*lang'],
    "D3": [r'\bhinglish', r'\bspanglish', r'\barabizi', r'\bromaniz',
           r'\bcode.switch', r'\btransliterat', r'\bdialect', r'\bmixed.lang',
           r'\bbilingual', r'\bmultilinguality', r'\blanguage\s+mixing'],
}


def paper_mentions_agent_languages(title, context_text, agent_id):
    """Check whether a paper title or its context mentions any language
    relevant to this agent. Returns True for multilingual agent (D1).
    For other agents, prevents generic papers from being included.

    We check title + first 500 chars of context (not 1500) to avoid
    false positives from unrelated mentions deep in context blocks."""
    patterns = AGENT_LANGUAGE_KEYWORDS.get(agent_id)
    if patterns is None:
        return True  # D1 multilingual — accept all

    # Check title + URL. We avoid using context_text because all links
    # in a search result share the same context block, causing false positives.
    # But we allow a very short context snippet (first 200 chars) which often
    # contains the specific description for THIS paper.
    context_snippet = context_text[:200] if context_text else ""
    text = (title + " " + context_snippet).lower()

    for p in patterns:
        if re.search(p, text):
            return True
    # Also accept papers that say "multilingual" in their TITLE
    # (but not just in context, which is too broad)
    if re.search(r'\bmultilingual\b', title.lower()):
        return True
    return False


def normalize_title(title):
    """Normalize title for dedup comparison."""
    # Remove arXiv IDs, version markers, PDF markers, etc.
    t = re.sub(r'\[?\d{4}\.\d{4,5}(?:v\d+)?\]?', '', title)
    t = re.sub(r'\(PDF\)', '', t, flags=re.IGNORECASE)
    t = re.sub(r'- ACL Anthology$', '', t)
    t = re.sub(r'\| .*$', '', t)
    t = re.sub(r'- .*$', '', t)
    t = re.sub(r'[^a-z0-9\s]', '', t.lower())
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def titles_match(t1, t2):
    """Check if two titles refer to the same paper."""
    n1 = normalize_title(t1)
    n2 = normalize_title(t2)
    if not n1 or not n2:
        return False
    # Exact match after normalization
    if n1 == n2:
        return True
    # One is substring of the other
    if n1 in n2 or n2 in n1:
        return True
    # High sequence similarity
    ratio = SequenceMatcher(None, n1, n2).ratio()
    return ratio > 0.85


def clean_title(title):
    """Clean up a title string."""
    # Remove [PDF] markers
    title = re.sub(r'\(PDF\)\s*', '', title)
    # Remove leading/trailing brackets
    title = re.sub(r'^\[.*?\]\s*', '', title)
    # Remove trailing source info
    title = re.sub(r'\s*\|\s*(ACL Anthology|Semantic Scholar|SpringerLink|OpenReview|Papers With Code).*$', '', title)
    title = re.sub(r'\s*-\s*(ACL Anthology|PubMed|ResearchGate).*$', '', title)
    # Remove trailing pipe-delimited info
    title = re.sub(r'\s*\|\s*(Scientific Reports|Computational Linguistics|MIT Press|MDPI|PeerJ|Nature).*$', '', title)
    # Remove arXiv prefixes
    title = re.sub(r'^\[?\d{4}\.\d{4,5}(?:v\d+)?\]?\s*', '', title)
    # Remove "Related papers:" prefix
    title = re.sub(r'^Related papers:\s*', '', title, flags=re.IGNORECASE)
    title = re.sub(r'^\[Literature Review\]\s*', '', title, flags=re.IGNORECASE)
    title = title.strip()
    return title


def extract_data_url(text):
    """Extract GitHub/HuggingFace data URL from text."""
    patterns = [
        r'(https?://github\.com/[^\s"\'<>\]]+)',
        r'(https?://huggingface\.co/datasets/[^\s"\'<>\]]+)',
    ]
    for pattern in patterns:
        m = re.search(pattern, text)
        if m:
            return m.group(1)
    return None


def infer_languages(title, url, agent_languages, description=""):
    """Infer languages covered by a paper based on title, URL, and agent context."""
    text = (title + " " + description).lower()
    languages = []

    # Language name detection mapping
    lang_patterns = {
        "Mongolian": [r'\bmongol'],
        "Tibetan": [r'\btibet'],
        "Uyghur": [r'\buyghur', r'\buighur'],
        "Kyrgyz": [r'\bkyrgyz'],
        "Chinese": [r'\bchinese', r'\b中文', r'\bmandarin', r'\bchinese-specific'],
        "Cantonese": [r'\bcantonese', r'\byue\b'],
        "Classical Chinese": [r'\bclassical chinese', r'\b古文', r'\b文言'],
        "Min": [r'\bmin\b.*dialect', r'\bminnan', r'\bsouthern min'],
        "Hakka": [r'\bhakka'],
        "Japanese": [r'\bjapanese', r'\b日本'],
        "Arabic": [r'\barabic', r'\barabi'],
        "Egyptian Arabic": [r'\begyptian'],
        "Gulf Arabic": [r'\bgulf'],
        "Levantine": [r'\blevant'],
        "Maghrebi": [r'\bmaghreb'],
        "Multilingual": [r'\bmultilingual', r'\bcross-lingual', r'\bmulti-lingual'],
        "Quechua": [r'\bquechua'],
        "Guarani": [r'\bguarani'],
        "Maori": [r'\bm[aā]ori'],
        "Welsh": [r'\bwelsh'],
        "Irish": [r'\birish'],
        "Hawaiian": [r'\bhawaiian'],
        "Navajo": [r'\bnavajo'],
        "Inuktitut": [r'\binuktitut', r'\binuit'],
        "Hindi": [r'\bhindi'],
        "Hinglish": [r'\bhinglish'],
        "Spanglish": [r'\bspanglish'],
        "Arabizi": [r'\barabizi'],
        "Code-switching": [r'\bcode.switch'],
        "Korean": [r'\bkorean'],
        "Turkish": [r'\bturk'],
        "Greek": [r'\bgreek'],
        "English": [r'\benglish'],
        "Saudi": [r'\bsaudi'],
    }

    for lang, patterns in lang_patterns.items():
        for p in patterns:
            if re.search(p, text, re.IGNORECASE):
                if lang not in languages:
                    languages.append(lang)
                break

    # If nothing was detected, use agent's default languages
    if not languages:
        # For multilingual agent, keep empty — will be filled per paper
        if agent_languages != ["Multilingual"]:
            languages = list(agent_languages)

    return languages


def extract_benchmark_name(title, description=""):
    """Try to extract benchmark name from title."""
    text = title + " " + description

    # Common patterns: "BenchmarkName: Description" or "BenchmarkName - Description"
    # Look for CamelCase or ALL-CAPS names before colons
    m = re.match(r'^([A-Z][A-Za-z0-9-]+(?:[A-Z][a-z]+)+)\b', title)
    if m:
        return m.group(1)

    # ALL-CAPS with possible hyphens: MM-Eval, C-Eval, etc.
    m = re.match(r'^([A-Z][A-Z0-9]+-?[A-Za-z0-9]+)\b', title)
    if m and len(m.group(1)) >= 3:
        name = m.group(1)
        # Skip generic words
        if name.lower() not in {"the", "how", "why", "what", "towards", "beyond",
                                  "evaluating", "exploring", "comparing", "analyzing",
                                  "detecting", "tackling", "applying", "filling",
                                  "advancing", "benchmarking", "leveraging", "probing",
                                  "deconstructing", "mirroring", "automated", "lost",
                                  "overview", "recent", "survey", "review",
                                  "adversarially", "explicitly", "source",
                                  "international", "national", "state"}:
            return name

    # Pattern: "X: A Benchmark" or "X: A Dataset"
    m = re.match(r'^([A-Za-z][A-Za-z0-9_-]+):\s', title)
    if m and len(m.group(1)) >= 2:
        name = m.group(1)
        if name.lower() not in {"a", "an", "the", "on", "in", "for", "how",
                                  "why", "what", "towards", "beyond",
                                  "under", "original", "proceedings",
                                  "paper", "chapter", "chapter 11"}:
            return name

    return None


# ── Main parsing logic ────────────────────────────────────────────────────────

def parse_agent_output(filepath, agent_id, agent_languages):
    """Parse an agent output file and extract paper records."""
    papers = []  # list of paper dicts
    search_queries = []
    seen_urls = set()
    seen_normalized_titles = set()

    # Collect all search result links and agent analysis text
    all_links = []  # (title, url, context_text)
    all_analysis = []  # analysis text blocks from assistant

    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            msg = obj.get("message", {})
            role = msg.get("role", "")
            content = msg.get("content", "")

            # Extract search queries from assistant tool_use messages
            if role == "assistant" and isinstance(content, list):
                for item in content:
                    if isinstance(item, dict):
                        if item.get("type") == "tool_use" and item.get("name") == "WebSearch":
                            query = item.get("input", {}).get("query", "")
                            if query and query not in search_queries:
                                search_queries.append(query)
                        elif item.get("type") == "text":
                            text = item.get("text", "")
                            if text and len(text) > 50:
                                all_analysis.append(text)

            # Extract links from tool_result messages
            if role == "user" and isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "tool_result":
                        result_content = item.get("content", "")
                        if isinstance(result_content, str) and "Links:" in result_content:
                            # Extract the JSON links array
                            links_match = re.search(r'Links:\s*(\[.*?\])', result_content, re.DOTALL)
                            if links_match:
                                try:
                                    links = json.loads(links_match.group(1))
                                    # Get the context text after the links
                                    context_start = links_match.end()
                                    context_text = result_content[context_start:]
                                    for link in links:
                                        title = link.get("title", "")
                                        url = link.get("url", "")
                                        if title and url:
                                            all_links.append((title, url, context_text))
                                except json.JSONDecodeError:
                                    pass

    # Now process all links into paper records
    for title, url, context_text in all_links:
        # Skip non-academic URLs
        if should_skip_url(url):
            continue

        # Skip GitHub repos that aren't papers
        if "github.com" in url and "/papers/" not in url:
            # Keep GitHub repos as data_url references, not as papers
            # Unless it's a paper repo
            domain = get_domain(url)
            if "github.com" in domain:
                # Check if it's a benchmark/dataset repo (potentially useful)
                if not any(kw in title.lower() for kw in ["benchmark", "dataset", "corpus", "evaluation"]):
                    continue

        # Skip HuggingFace datasets pages
        if "huggingface.co/datasets" in url:
            continue

        # Clean the title
        cleaned_title = clean_title(title)
        if not cleaned_title or len(cleaned_title) < 10:
            continue

        # Skip generic/non-paper titles
        skip_title_patterns = [
            r'^(?:30|250|10)\s+LLM',
            r'^LLM Benchmarks 20\d\d',
            r'^AI (?:Leaderboards|Benchmarks)',
            r'^(?:The )?(?:best|top|ultimate|complete)',
            r'^(?:An )?Introduction to',
            r'^Tracking Progress',
            r'^What\'?s new about',
            r'^5 Chinese Open-Source',
            r'^Chinese AI Models',
            r'^Import AI',
            r'^GitHub\s+-\s+',
            r'^How Should AI Safety',
            r'^Artificial Intelligence 20\d\d\s+-\s+Japan',
            r'^(?:Open )?Chinese LLM Leaderboard',
            r'^Japanese LLM Evaluation',
            r'^Introducing the Open Leaderboard',
            r'^(?:Ultimate Guide|Why We Build)',
            r'^Comparison of LLM',
            r'^LLM Research Papers',
            r'^(?:The )?State [Oo]f',
            r'^(?:20\d\d): The year in',
            r'^ChinAI',
            r'^Can LLMs translate',
            r'^Leaderboard',
            r'^C-Eval Leaderboard',
            r'^lm-evaluation-harness',
            r'^Papers with Code',
            r'^Aclanthology$',
            r'^Chapter \d+\s+',
            r'^GLUE Benchmark$',
            r'^Challenges and Opportunities in NLP',
            r'^Proceedings of the',
            r'^Datasets\s*-\s*',
            r'^Tutorial:',
            r'^(?:Arabic|Chinese|Japanese)\s+(?:LLM|NLP)\s+Benchmark Report',
            r'^(?:Arabic|Chinese)\s+Natural Language Processing Conference',
            r'^How China Views',
            r'^China issues',
            r'^China\'s AI Safety',
            r'^ArabicNLP 20\d\d Shared Task',
            r'^National Status Report',
            r'^Japan AI Safety Institute',
            r'^Framework for bias evaluation',
            r'^Evaluating Bias in NLP Datasets for Fairness Assurance',
            r'^The (?:best|top) LLM',
            r'^(?:15|20)\s+Must-Know',
            r'^NLP Benchmark Datasets',
            r'^NLP (?:Evaluation )?Datasets',
            r'^(?:Natural Language Processing|NLP) (?:performance )?metrics',
            r'^Language model benchmark',
            r'^NLP Model Evaluation',
            r'^(?:Where to Find|How to)',
            r'^An Empirical Survey of the Effectiveness',
            r'^Statistics of the .* dataset\.',
            r'^More than Metrics',
            r'^Holistic Evaluation of Language Models',
            r'(?:Neurolinguistic|NLP)\s+(?:Learning State|at Hawaii)',
            r'Hawaiian NLP$',
            r'^NLP Learning State',
            r'^Egune AI',
            r'bayartsogt/mongolian',
            r'^A (?:Complete|Comprehensive) Guide',
            r'^Paper page\s*-',
            r'^(?:deepset|Hakalau)\b',
            r'^Giti\s+Multilingual',
            r'^ai-forever/',
            r'· Hugging Face$',
            r'Neurolinguistic Programming',
            r'Navajo Language Program',
            r'Diné Culture',
            r'^Certificate Requirements',
            r'^The Navajo Reading Study',
            r'^The Lifelong Journey',
        ]
        skip = False
        for sp in skip_title_patterns:
            if re.search(sp, cleaned_title, re.IGNORECASE):
                skip = True
                break
        if skip:
            continue

        # Check relevance
        if not is_relevant(cleaned_title, url):
            continue

        # Check that paper actually relates to this agent's languages
        # (prevents generic surveys from being attributed to specific language agents)
        if not paper_mentions_agent_languages(cleaned_title, context_text, agent_id):
            continue

        # Deduplicate by URL
        url_key = re.sub(r'https?://(www\.)?', '', url)
        url_key = re.sub(r'v\d+$', '', url_key)  # strip version
        url_key = re.sub(r'\.pdf$', '', url_key)
        url_key = url_key.rstrip('/')
        if url_key in seen_urls:
            continue

        # Deduplicate by normalized title
        nt = normalize_title(cleaned_title)
        if nt in seen_normalized_titles:
            seen_urls.add(url_key)
            continue

        # Check if this is a near-duplicate of an existing paper
        is_dup = False
        for existing_nt in seen_normalized_titles:
            if titles_match(cleaned_title, existing_nt):
                is_dup = True
                break
        if is_dup:
            seen_urls.add(url_key)
            continue

        seen_urls.add(url_key)
        seen_normalized_titles.add(nt)

        # Build paper record
        arxiv_id = extract_arxiv_id(url)
        doi = extract_doi(url)

        # Determine year
        year = extract_year_from_arxiv_id(arxiv_id) if arxiv_id else None
        if not year:
            year = extract_year_from_title(cleaned_title)
        if not year:
            year = extract_year_from_title(context_text[:500]) if context_text else None
        if not year:
            year = 2025  # default for recent papers

        # Infer languages
        languages_covered = infer_languages(
            cleaned_title, url, agent_languages, context_text[:1000] if context_text else ""
        )

        # Extract benchmark name
        benchmark_name = extract_benchmark_name(cleaned_title)

        # Extract abstract snippet from context
        abstract_snippet = ""
        if context_text:
            # Try to get a meaningful snippet
            sentences = re.split(r'(?<=[.!?])\s+', context_text[:2000])
            snippet_sentences = []
            for sent in sentences:
                sent = sent.strip()
                if len(sent) > 30 and not sent.startswith("REMINDER:"):
                    if not sent.startswith("Sources:"):
                        snippet_sentences.append(sent)
                        if len(snippet_sentences) >= 2:
                            break
            abstract_snippet = " ".join(snippet_sentences)[:500]
            # Clean up markdown and HTML
            abstract_snippet = re.sub(r'\[.*?\]\(.*?\)', '', abstract_snippet)
            abstract_snippet = re.sub(r'[#*`]', '', abstract_snippet)
            abstract_snippet = re.sub(r'\s+', ' ', abstract_snippet).strip()

        # Source
        source = infer_source(url)

        # Data URL
        data_url = extract_data_url(context_text[:2000]) if context_text else None

        # Relevance notes
        relevance_notes = ""
        if benchmark_name:
            relevance_notes = f"{benchmark_name} benchmark"
        lang_str = ", ".join(languages_covered[:3])
        if lang_str:
            relevance_notes += f" for {lang_str}" if relevance_notes else f"Relevant to {lang_str}"
        if any(kw in cleaned_title.lower() for kw in ["ethic", "moral", "value", "safe"]):
            relevance_notes += "; ethics/values focus"
        if any(kw in cleaned_title.lower() for kw in ["bias", "fair", "stereotyp"]):
            relevance_notes += "; bias/fairness focus"
        if any(kw in cleaned_title.lower() for kw in ["toxic", "hate", "offensive"]):
            relevance_notes += "; toxicity/hate speech focus"
        if any(kw in cleaned_title.lower() for kw in ["cultur", "religious", "islam"]):
            relevance_notes += "; cultural focus"

        paper = {
            "title": cleaned_title,
            "authors": "",
            "year": year,
            "url": url,
            "arxiv_id": arxiv_id,
            "doi": doi,
            "languages_covered": languages_covered,
            "benchmark_name": benchmark_name,
            "abstract_snippet": abstract_snippet,
            "source": source,
            "data_url": data_url,
            "relevance_notes": relevance_notes,
        }

        papers.append(paper)

    return papers, search_queries


def try_enrich_from_context(papers, filepath):
    """Second pass: try to extract author info and better descriptions
    from assistant analysis text blocks."""

    # Read all assistant text blocks
    analysis_blocks = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            msg = obj.get("message", {})
            role = msg.get("role", "")
            content = msg.get("content", "")

            # tool_result context text
            if role == "user" and isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "tool_result":
                        result_content = item.get("content", "")
                        if isinstance(result_content, str) and len(result_content) > 100:
                            analysis_blocks.append(result_content)

    full_text = "\n\n".join(analysis_blocks)

    for paper in papers:
        title_words = paper["title"].lower().split()[:6]
        title_fragment = " ".join(title_words)

        # Try to find author info near the paper title
        for block in analysis_blocks:
            if title_fragment in block.lower() or (
                paper["benchmark_name"] and paper["benchmark_name"].lower() in block.lower()
            ):
                # Look for author patterns in nearby text
                # Pattern: "Author1, Author2, ... (Year)"
                # Pattern: "by Author1 et al."
                # Pattern: "Author1 Author2 arXiv paper title"
                author_patterns = [
                    r'(?:by|authors?:?)\s+([A-Z][a-z]+(?:\s[A-Z][a-z]+)?(?:,\s+[A-Z][a-z]+(?:\s[A-Z][a-z]+)?)*(?:\s+et\s+al\.?)?)',
                ]
                for ap in author_patterns:
                    am = re.search(ap, block)
                    if am and not paper["authors"]:
                        paper["authors"] = am.group(1)
                        break

                # Better abstract snippets
                if not paper["abstract_snippet"] or len(paper["abstract_snippet"]) < 50:
                    # Find sentences about this paper
                    title_short = paper["title"][:40].lower()
                    idx = block.lower().find(title_short)
                    if idx >= 0:
                        after = block[idx:idx+500]
                        sentences = re.split(r'(?<=[.!?])\s+', after)
                        snippet = []
                        for s in sentences[1:4]:  # skip title sentence
                            s = s.strip()
                            if len(s) > 20 and not s.startswith("REMINDER"):
                                snippet.append(s)
                                if len(snippet) >= 2:
                                    break
                        if snippet:
                            new_snippet = " ".join(snippet)[:500]
                            new_snippet = re.sub(r'\[.*?\]\(.*?\)', '', new_snippet)
                            new_snippet = re.sub(r'[#*`]', '', new_snippet)
                            new_snippet = re.sub(r'\s+', ' ', new_snippet).strip()
                            if len(new_snippet) > len(paper["abstract_snippet"]):
                                paper["abstract_snippet"] = new_snippet

    return papers


def main():
    total_all = 0
    results = {}

    for agent_id, config in AGENTS.items():
        filepath = config["file"]
        languages = config["languages"]

        if not os.path.exists(filepath):
            print(f"[{agent_id}] ERROR: File not found: {filepath}")
            continue

        print(f"[{agent_id}] Processing {filepath}...")
        papers, queries = parse_agent_output(filepath, agent_id, languages)

        # Enrichment pass
        papers = try_enrich_from_context(papers, filepath)

        # Build report
        report = {
            "agent_id": agent_id,
            "languages": languages,
            "search_queries_used": queries,
            "papers_found": papers,
            "total_found": len(papers),
            "vault_overlap_notes": "Extracted from agent conversation logs; may overlap with existing vault papers.",
        }

        # Write JSON report
        out_path = OUTPUT_DIR / f"20260213-language_search_agent_{agent_id}.json"
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"[{agent_id}] Extracted {len(papers)} papers from {len(queries)} queries")
        print(f"[{agent_id}] Written to {out_path}")
        total_all += len(papers)
        results[agent_id] = len(papers)

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    for agent_id, count in results.items():
        lang_str = ", ".join(AGENTS[agent_id]["languages"][:3])
        if len(AGENTS[agent_id]["languages"]) > 3:
            lang_str += "..."
        print(f"  {agent_id} ({lang_str}): {count} papers")
    print(f"  {'─'*40}")
    print(f"  TOTAL: {total_all} papers across {len(results)} agents")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
