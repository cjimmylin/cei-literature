#!/usr/bin/env python3
"""
Phase A: Normalize LLM_assessed YAML field across all papers.

Reduces ~1,053 unique model name strings to ~100-150 canonical forms by:
1. Splitting comma-separated values and trimming whitespace
2. Filtering out implausible tokens (text contamination, false positives)
3. Normalizing to canonical names via expanded mapping
4. Deduplicating (case-insensitive) and sorting alphabetically
5. Writing back using safe regex (never parse/rebuild round-trip)

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/normalize_llm_assessed.py --dry-run
    ../.venv/bin/python PYTHON/normalize_llm_assessed.py

Output:
    logs/YYYYMMDD-llm-normalization-changes.json
    logs/YYYYMMDD-llm-normalization-summary.md
"""

from __future__ import annotations

import argparse
import functools
import json
import os
import re
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent"))
from lib.config import LOGS_DIR, PAPERS_DIR  # noqa: E402
from lib.yaml_utils import extract_frontmatter, validate_frontmatter  # noqa: E402

# ── Canonical Model Names ────────────────────────────────────────────────
# Built from MODEL_FAMILY_MAP in generate_llm_assessment_report.py (lines 37-74)
# Maps lowercase variant → canonical form
CANONICAL_MAP: dict[str, str] = {}

MODEL_FAMILY_MAP = {
    "OpenAI": [
        "GPT-4", "GPT-4o", "GPT-4o mini", "GPT-4 Turbo", "GPT-3.5",
        "GPT-3", "GPT-2", "ChatGPT", "o1", "o1-mini", "o1-preview",
        "o3", "o3-mini", "text-davinci", "text-davinci-002",
        "text-davinci-003", "InstructGPT", "CODEX", "GPT-5",
    ],
    "Anthropic": [
        "Claude", "Claude-2", "Claude-3", "Claude-3 Opus",
        "Claude-3 Sonnet", "Claude-3 Haiku", "Claude Instant",
    ],
    "Meta": [
        "Llama-3", "Llama-2", "Llama", "LLaMA", "CodeLlama", "OPT",
        "OPT-175B",
    ],
    "Google": [
        "Gemini", "Gemini Pro", "Gemini Ultra", "Gemini Flash",
        "Gemma", "Gemma-2", "PaLM-2", "PaLM", "Flan-T5", "Flan-UL2",
        "LaMDA", "T5", "BARD",
    ],
    "Mistral AI": ["Mistral", "Mixtral"],
    "Alibaba": ["Qwen", "Qwen-2", "Qwen-1.5"],
    "DeepSeek": ["DeepSeek", "DeepSeek-V2", "DeepSeek-Coder"],
    "Microsoft": ["Phi", "Phi-2", "Phi-3"],
    "xAI": ["Grok"],
    "Cohere": ["Cohere", "Command-R", "Command R+", "Aya"],
    "AI21": ["Jurassic", "Jurassic-2", "J2"],
    "Open-source (misc)": [
        "Vicuna", "Alpaca", "Falcon", "BLOOM", "Yi", "Dolly",
        "Zephyr", "WizardLM", "InternLM", "Baichuan", "ChatGLM",
        "GLM", "StableLM", "MPT", "DialoGPT", "Delphi", "ERNIE",
    ],
    "Pre-LLM / Encoder": [
        "BERT", "RoBERTa", "ALBERT", "DeBERTa", "DistilBERT",
        "XLNet", "ELECTRA", "ELMo", "BART",
    ],
    "Embeddings": ["Word2Vec", "GloVe", "FastText"],
}

# Build canonical map: lowercase → canonical
for _family, _models in MODEL_FAMILY_MAP.items():
    for _m in _models:
        CANONICAL_MAP[_m.lower()] = _m

# ── Extended Variant Mappings ─────────────────────────────────────────────
# Covers common spelling/casing/spacing variants NOT caught by lowercase lookup
VARIANT_MAP: dict[str, str] = {
    # GPT variants
    "gpt4": "GPT-4",
    "gpt 4": "GPT-4",
    "gpt-4-turbo": "GPT-4 Turbo",
    "gpt4-turbo": "GPT-4 Turbo",
    "gpt4 turbo": "GPT-4 Turbo",
    "gpt-4-vision": "GPT-4",
    "gpt-4v": "GPT-4",
    "gpt4o": "GPT-4o",
    "gpt 4o": "GPT-4o",
    "gpt-4o-mini": "GPT-4o mini",
    "gpt4o mini": "GPT-4o mini",
    "gpt4o-mini": "GPT-4o mini",
    "gpt3.5": "GPT-3.5",
    "gpt-3.5-turbo": "GPT-3.5",
    "gpt3.5-turbo": "GPT-3.5",
    "gpt3.5 turbo": "GPT-3.5",
    "gpt 3.5": "GPT-3.5",
    "gpt3": "GPT-3",
    "gpt 3": "GPT-3",
    "gpt2": "GPT-2",
    "gpt 2": "GPT-2",
    "gpt-5": "GPT-5",
    "gpt5": "GPT-5",
    # ChatGPT variants
    "chat gpt": "ChatGPT",
    "chat-gpt": "ChatGPT",
    # Claude variants
    "claude 2": "Claude-2",
    "claude 3": "Claude-3",
    "claude3": "Claude-3",
    "claude-3-opus": "Claude-3 Opus",
    "claude 3 opus": "Claude-3 Opus",
    "claude-3-sonnet": "Claude-3 Sonnet",
    "claude 3 sonnet": "Claude-3 Sonnet",
    "claude-3-haiku": "Claude-3 Haiku",
    "claude 3 haiku": "Claude-3 Haiku",
    "claude-instant": "Claude Instant",
    # Llama variants
    "llama 2": "Llama-2",
    "llama2": "Llama-2",
    "llama-2-chat": "Llama-2",
    "llama 3": "Llama-3",
    "llama3": "Llama-3",
    "llama-3.1": "Llama-3",
    "llama 3.1": "Llama-3",
    "llama3.1": "Llama-3",
    "llama-3.2": "Llama-3",
    "llama 3.2": "Llama-3",
    "llama3.2": "Llama-3",
    "code llama": "CodeLlama",
    "code-llama": "CodeLlama",
    "codellama": "CodeLlama",
    # Gemini variants
    "gemini-pro": "Gemini Pro",
    "gemini-ultra": "Gemini Ultra",
    "gemini-flash": "Gemini Flash",
    "gemini 1.5": "Gemini",
    "gemini-1.5": "Gemini",
    "gemini 1.0": "Gemini",
    "gemini-1.0": "Gemini",
    # Gemma variants
    "gemma 2": "Gemma-2",
    "gemma2": "Gemma-2",
    # PaLM variants
    "palm 2": "PaLM-2",
    "palm2": "PaLM-2",
    # Flan-T5 variants
    "flan t5": "Flan-T5",
    "flant5": "Flan-T5",
    "flan-t5-xxl": "Flan-T5",
    "flan-t5-xl": "Flan-T5",
    "flan-t5-large": "Flan-T5",
    "flan-t5-base": "Flan-T5",
    "flan-t5-small": "Flan-T5",
    "flan ul2": "Flan-UL2",
    "flanul2": "Flan-UL2",
    # Mistral/Mixtral variants
    "mistral-7b": "Mistral",
    "mistral 7b": "Mistral",
    "mixtral-8x7b": "Mixtral",
    "mixtral 8x7b": "Mixtral",
    # Qwen variants
    "qwen 2": "Qwen-2",
    "qwen2": "Qwen-2",
    "qwen 1.5": "Qwen-1.5",
    "qwen1.5": "Qwen-1.5",
    # DeepSeek variants
    "deepseek v2": "DeepSeek-V2",
    "deepseek-v2": "DeepSeek-V2",
    "deepseek coder": "DeepSeek-Coder",
    "deepseek-coder": "DeepSeek-Coder",
    # Phi variants
    "phi 2": "Phi-2",
    "phi2": "Phi-2",
    "phi 3": "Phi-3",
    "phi3": "Phi-3",
    # Other variants
    "text davinci": "text-davinci",
    "text davinci 002": "text-davinci-002",
    "text davinci 003": "text-davinci-003",
    "text-davinci-2": "text-davinci-002",
    "text-davinci-3": "text-davinci-003",
    "instructgpt": "InstructGPT",
    "instruct gpt": "InstructGPT",
    "instruct-gpt": "InstructGPT",
    "codex": "CODEX",
    "opt-175b": "OPT-175B",
    "opt 175b": "OPT-175B",
    "jurassic 2": "Jurassic-2",
    "jurassic2": "Jurassic-2",
    "command-r": "Command-R",
    "command r": "Command-R",
    "command r+": "Command R+",
    "command-r+": "Command R+",
    "wizard lm": "WizardLM",
    "wizard-lm": "WizardLM",
    "intern lm": "InternLM",
    "intern-lm": "InternLM",
    "chat glm": "ChatGLM",
    "chat-glm": "ChatGLM",
    "stable lm": "StableLM",
    "stable-lm": "StableLM",
    "stablelm": "StableLM",
    "dialogpt": "DialoGPT",
    "dialog gpt": "DialoGPT",
    "dialog-gpt": "DialoGPT",
    "distil bert": "DistilBERT",
    "distil-bert": "DistilBERT",
    "distilbert": "DistilBERT",
    "deberta": "DeBERTa",
    "de-berta": "DeBERTa",
    "roberta": "RoBERTa",
    "word2vec": "Word2Vec",
    "word 2 vec": "Word2Vec",
    "fasttext": "FastText",
    "fast text": "FastText",
    "fast-text": "FastText",
    "ernie bot": "ERNIE",
    "ernie-bot": "ERNIE",
    "lamda": "LaMDA",
    "la-mda": "LaMDA",
    "bard": "BARD",
    # o1/o3 with hyphens
    "o1 mini": "o1-mini",
    "o1 preview": "o1-preview",
    "o3 mini": "o3-mini",
}

# Merge variant map into canonical map (variant keys are already lowercase)
for _k, _v in VARIANT_MAP.items():
    CANONICAL_MAP[_k] = _v

# ── Regex-based collapsing patterns ───────────────────────────────────────
# Applied AFTER exact lookup fails. Order matters — first match wins.
COLLAPSE_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"(?i)^gpt[-\s]?4o[-\s]?mini$"), "GPT-4o mini"),
    (re.compile(r"(?i)^gpt[-\s]?4o\b.*"), "GPT-4o"),
    (re.compile(r"(?i)^gpt[-\s]?4[-\s]?turbo\b.*"), "GPT-4 Turbo"),
    (re.compile(r"(?i)^gpt[-\s]?4[-\s]?(?:vision|v)\b.*"), "GPT-4"),
    (re.compile(r"(?i)^gpt[-\s]?4\b.*"), "GPT-4"),
    (re.compile(r"(?i)^gpt[-\s]?3\.?5[-\s]?(?:turbo)?\b.*"), "GPT-3.5"),
    (re.compile(r"(?i)^gpt[-\s]?3\b.*"), "GPT-3"),
    (re.compile(r"(?i)^gpt[-\s]?2\b.*"), "GPT-2"),
    (re.compile(r"(?i)^chat[-\s]?gpt\b.*"), "ChatGPT"),
    (re.compile(r"(?i)^claude[-\s]?3[-\s]?opus\b.*"), "Claude-3 Opus"),
    (re.compile(r"(?i)^claude[-\s]?3[-\s]?sonnet\b.*"), "Claude-3 Sonnet"),
    (re.compile(r"(?i)^claude[-\s]?3[-\s]?haiku\b.*"), "Claude-3 Haiku"),
    (re.compile(r"(?i)^claude[-\s]?3\b.*"), "Claude-3"),
    (re.compile(r"(?i)^claude[-\s]?2\b.*"), "Claude-2"),
    (re.compile(r"(?i)^claude[-\s]?instant\b.*"), "Claude Instant"),
    (re.compile(r"(?i)^claude\b.*"), "Claude"),
    (re.compile(r"(?i)^llama[-\s]?4\b.*"), "Llama-3"),  # Llama4 → Llama-3 (latest gen)
    (re.compile(r"(?i)^llama[-\s]?guard\b.*"), "Llama-3"),  # LlamaGuard → Llama-3 family
    (re.compile(r"(?i)^llama[-\s]?3(?:\.\d+)?\b.*"), "Llama-3"),
    (re.compile(r"(?i)^llama[-\s]?2\b.*"), "Llama-2"),
    (re.compile(r"(?i)^llama\b.*"), "Llama"),
    (re.compile(r"(?i)^code[-\s]?llama\b.*"), "CodeLlama"),
    (re.compile(r"(?i)^gemini[-\s]?(?:1\.5[-\s]?)?pro\b.*"), "Gemini Pro"),
    (re.compile(r"(?i)^gemini[-\s]?(?:1\.5[-\s]?)?ultra\b.*"), "Gemini Ultra"),
    (re.compile(r"(?i)^gemini[-\s]?(?:1\.5[-\s]?)?flash\b.*"), "Gemini Flash"),
    (re.compile(r"(?i)^gemini\b.*"), "Gemini"),
    (re.compile(r"(?i)^gemma[-\s]?3\b.*"), "Gemma"),  # Gemma3 → Gemma (latest gen)
    (re.compile(r"(?i)^gemma[-\s]?2\b.*"), "Gemma-2"),
    (re.compile(r"(?i)^gemma\b.*"), "Gemma"),
    (re.compile(r"(?i)^palm[-\s]?2\b.*"), "PaLM-2"),
    (re.compile(r"(?i)^palm\b.*"), "PaLM"),
    (re.compile(r"(?i)^flan[-\s]?t5\b.*"), "Flan-T5"),
    (re.compile(r"(?i)^flan[-\s]?ul2\b.*"), "Flan-UL2"),
    (re.compile(r"(?i)^mistral\b.*"), "Mistral"),
    (re.compile(r"(?i)^mixtral\b.*"), "Mixtral"),
    (re.compile(r"(?i)^qwen[-\s]?3\b.*"), "Qwen"),  # Qwen3 → Qwen (latest gen)
    (re.compile(r"(?i)^qwen[-\s]?2\b.*"), "Qwen-2"),
    (re.compile(r"(?i)^qwen[-\s]?1\.5\b.*"), "Qwen-1.5"),
    (re.compile(r"(?i)^qwen\b.*"), "Qwen"),
    (re.compile(r"(?i)^deepseek[-\s]?v2\b.*"), "DeepSeek-V2"),
    (re.compile(r"(?i)^deepseek[-\s]?coder\b.*"), "DeepSeek-Coder"),
    (re.compile(r"(?i)^deepseek[-\s]?math\b.*"), "DeepSeek"),
    (re.compile(r"(?i)^deepseek\b.*"), "DeepSeek"),
    (re.compile(r"(?i)^phi[-\s]?4\b.*"), "Phi"),  # Phi4 → Phi (latest gen)
    (re.compile(r"(?i)^phi[-\s]?3\b.*"), "Phi-3"),
    (re.compile(r"(?i)^phi[-\s]?2\b.*"), "Phi-2"),
    (re.compile(r"(?i)^phi\b.*"), "Phi"),
    (re.compile(r"(?i)^grok\b.*"), "Grok"),
    (re.compile(r"(?i)^vicuna\b.*"), "Vicuna"),
    (re.compile(r"(?i)^alpaca\b.*"), "Alpaca"),
    (re.compile(r"(?i)^falcon[-\s]?\d*\b.*"), "Falcon"),
    (re.compile(r"(?i)^bloom[-\s]?z\b.*"), "BLOOM"),  # BLOOMZ → BLOOM family
    (re.compile(r"(?i)^bloom[-\s]?\d+\w*$"), "BLOOM"),  # Bloom-7b1, BLOOM-7B etc
    (re.compile(r"(?i)^bloom\b$"), "BLOOM"),
    (re.compile(r"(?i)^yi[-\s]?\d+\b.*"), "Yi"),
    (re.compile(r"(?i)^dolly\b.*"), "Dolly"),
    (re.compile(r"(?i)^zephyr\b.*"), "Zephyr"),
    (re.compile(r"(?i)^wizard[-\s]?lm\b.*"), "WizardLM"),
    (re.compile(r"(?i)^intern[-\s]?lm[-\s]?\d*\b.*"), "InternLM"),
    (re.compile(r"(?i)^baichuan[-\s]?2\b.*"), "Baichuan"),  # Baichuan2 → Baichuan
    (re.compile(r"(?i)^baichuan\b.*"), "Baichuan"),
    (re.compile(r"(?i)^chat[-\s]?glm[-\s]?\d*\b.*"), "ChatGLM"),  # ChatGLM2/3 → ChatGLM
    (re.compile(r"(?i)^glm\b.*"), "GLM"),
    (re.compile(r"(?i)^stable[-\s]?lm\b.*"), "StableLM"),
    (re.compile(r"(?i)^mpt\b.*"), "MPT"),
    (re.compile(r"(?i)^dialo[-\s]?gpt\b.*"), "DialoGPT"),
    (re.compile(r"(?i)^delphi\b.*"), "Delphi"),
    (re.compile(r"(?i)^ernie\b.*"), "ERNIE"),
    (re.compile(r"(?i)^opt[-\s]?175b\b.*"), "OPT-175B"),
    (re.compile(r"(?i)^opt\b.*"), "OPT"),
    (re.compile(r"(?i)^t5\b.*"), "T5"),
    (re.compile(r"(?i)^bart[-\s]?(?:base|large)?\b$"), "BART"),
    (re.compile(r"(?i)^de[-\s]?bert[-\s]?a\b.*"), "DeBERTa"),
    (re.compile(r"(?i)^distil[-\s]?bert\b.*"), "DistilBERT"),
    (re.compile(r"(?i)^ro[-\s]?bert[-\s]?a\b.*"), "RoBERTa"),
    (re.compile(r"(?i)^albert\b.*"), "ALBERT"),
    (re.compile(r"(?i)^bert\b.*"), "BERT"),
    (re.compile(r"(?i)^xlnet\b.*"), "XLNet"),
    (re.compile(r"(?i)^electra\b.*"), "ELECTRA"),
    (re.compile(r"(?i)^elmo\b.*"), "ELMo"),
    (re.compile(r"(?i)^word[-\s]?2[-\s]?vec\b.*"), "Word2Vec"),
    (re.compile(r"(?i)^glove\b.*"), "GloVe"),
    (re.compile(r"(?i)^fast[-\s]?text\b.*"), "FastText"),
    (re.compile(r"(?i)^text[-\s]?davinci[-\s]?003\b.*"), "text-davinci-003"),
    (re.compile(r"(?i)^text[-\s]?davinci[-\s]?002\b.*"), "text-davinci-002"),
    (re.compile(r"(?i)^text[-\s]?davinci\b.*"), "text-davinci"),
    (re.compile(r"(?i)^instruct[-\s]?gpt\b.*"), "InstructGPT"),
    (re.compile(r"(?i)^codex\b.*"), "CODEX"),
    (re.compile(r"(?i)^jurassic[-\s]?2\b.*"), "Jurassic-2"),
    (re.compile(r"(?i)^jurassic\b.*"), "Jurassic"),
    (re.compile(r"(?i)^j2\b.*"), "J2"),
    (re.compile(r"(?i)^command[-\s]?r\+"), "Command R+"),
    (re.compile(r"(?i)^command[-\s]?r\b.*"), "Command-R"),
    (re.compile(r"(?i)^cohere\b.*"), "Cohere"),
    (re.compile(r"(?i)^aya\b.*"), "Aya"),
    (re.compile(r"(?i)^la[-\s]?mda\b.*"), "LaMDA"),
]


# ── Plausibility filter (reused from backfill_llm_data_metadata.py) ──────

MODEL_ROOT_HINTS = (
    "gpt", "chatgpt", "claude", "llama", "mistral", "mixtral", "qwen",
    "gemma", "deepseek", "bert", "roberta", "albert", "deberta",
    "distilbert", "xlnet", "electra", "t5", "bart", "bloom", "vicuna",
    "alpaca", "falcon", "phi", "grok", "palm", "lamda", "bard", "opt",
    "internlm", "baichuan", "chatglm", "cohere", "command", "aya",
    "dolly", "zephyr", "wizardlm", "codex", "instructgpt", "word2vec",
    "glove", "elmo", "gemini", "flan", "ernie", "delphi", "stablelm",
    "mpt", "dialogpt", "glm", "fasttext", "yi",
)

ALLOWED_SUFFIX_TOKENS = {
    "mini", "turbo", "preview", "vision", "pro", "ultra", "nano",
    "flash", "chat", "base", "large", "small", "medium", "haiku",
    "sonnet", "opus", "instruct", "guard", "plus", "reasoner",
    "xxl", "xl", "coder", "bot",
}

BANNED_TOKENS = {
    "and", "or", "for", "the", "a", "an", "to", "from", "with",
    "without", "of", "in", "on", "at", "by", "is", "are", "was",
    "were", "be", "been", "being", "model", "models", "architecture",
    "architectures", "showed", "shows", "show", "perform", "performs",
    "performed", "provides", "provide", "through", "before", "after",
    "which", "that", "this", "still", "counterpart",
}

# Known false positives: strings that pass plausibility but are NOT model names
# (e.g. author names containing model root hints, org names)
FALSE_POSITIVES = {
    "barth", "bartl", "bartolo", "barto", "bartsch",  # author names matching BART
    "mistralai", "qwenlm",  # org/repo names, not models
    "palm springs", "palm beach",  # place names
    "bloomfield", "bloomington",  # place names matching BLOOM
    "glovert",  # author name matching GloVe
    "electrabel",  # matching ELECTRA
}


def is_plausible_model_name(model: str) -> bool:
    """Check whether a string looks like a plausible model name."""
    m = " ".join(model.split()).strip(" ,;.")
    if len(m) < 2 or len(m) > 80:
        return False
    if not re.fullmatch(r"[A-Za-z0-9.+\-_/ ]+", m):
        return False

    low = m.lower()
    if "http://" in low or "https://" in low or "www." in low:
        return False
    if len(m.split()) > 5:
        return False
    if not any(root in low for root in MODEL_ROOT_HINTS):
        return False

    # Check against known false positives
    if low in FALSE_POSITIVES:
        return False

    # Common false-positive patterns (author names, text contamination)
    if re.fullmatch(r"(?i)bart[a-z]{2,}", m):
        return False
    if re.fullmatch(r"(?i)bloom[a-z]{2,}", m):
        return False

    tokens = m.split()
    for token in tokens[1:]:
        t = token.lower().strip(".,;:()[]{}")
        if not t:
            continue
        if t in BANNED_TOKENS:
            return False
        if re.search(r"\d", t):
            continue
        if t in ALLOWED_SUFFIX_TOKENS:
            continue
        if re.fullmatch(r"[a-z]{1,3}", t):
            return False
        if re.fullmatch(r"[A-Z]{2,5}", token):
            continue
        return False

    return True


def normalize_model_name(model: str) -> str | None:
    """
    Normalize a model name string to its canonical form.

    Returns the canonical name, or None if the token is implausible.
    """
    m = " ".join(model.split()).strip(" ,;.")
    if not m:
        return None

    # Strip trailing period (known contamination pattern)
    m = m.rstrip(".")

    if not is_plausible_model_name(m):
        return None

    # Step 1: exact lowercase lookup
    key = m.lower()
    if key in CANONICAL_MAP:
        return CANONICAL_MAP[key]

    # Step 2: regex collapse patterns
    for pattern, canonical in COLLAPSE_PATTERNS:
        if pattern.match(m):
            return canonical

    # Step 3: return cleaned token as-is (it passed plausibility)
    return m


def normalize_llm_field(raw_value: str) -> tuple[str, list[str], list[str]]:
    """
    Normalize a full LLM_assessed field value.

    Returns: (normalized_value, original_tokens, canonical_tokens)
    """
    if not raw_value or raw_value.strip().upper() in ("NA", "N/A", "NONE", "NULL", ""):
        return "NA", [], []

    # Split on comma, trim
    tokens = [t.strip() for t in raw_value.split(",") if t.strip()]
    original_tokens = tokens[:]

    # Normalize each token
    canonical_tokens = []
    seen_lower: set[str] = set()
    for token in tokens:
        canonical = normalize_model_name(token)
        if canonical is None:
            continue
        cl = canonical.lower()
        if cl in seen_lower:
            continue
        seen_lower.add(cl)
        canonical_tokens.append(canonical)

    # Sort alphabetically for consistency
    canonical_tokens.sort(key=str.lower)

    if not canonical_tokens:
        return "NA", original_tokens, []

    return ", ".join(canonical_tokens), original_tokens, canonical_tokens


def set_yaml_scalar(frontmatter: str, key: str, value: str) -> tuple[str, bool]:
    """
    Safe regex-based replacement of a YAML scalar field.

    Returns: (new_frontmatter, was_replaced)
    """
    if value == "NA":
        line = f"{key}: NA"
    else:
        safe = value.replace('"', "'")
        line = f'{key}: "{safe}"'

    replaced, count = re.subn(
        r"^{}:.*$".format(re.escape(key)),
        line,
        frontmatter,
        count=1,
        flags=re.MULTILINE,
    )
    return replaced, count > 0


def clean_scalar(value: str | None) -> str:
    """Strip quotes and whitespace from a YAML scalar value."""
    s = (value or "").strip()
    if len(s) >= 2 and ((s.startswith('"') and s.endswith('"')) or
                         (s.startswith("'") and s.endswith("'"))):
        s = s[1:-1].strip()
    return s


def extract_llm_assessed_raw(frontmatter: str) -> str | None:
    """Extract the raw LLM_assessed value from frontmatter text."""
    m = re.search(r"^LLM_assessed:\s*(.*)$", frontmatter, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize LLM_assessed field across all papers")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--date-prefix", default=date.today().strftime("%Y%m%d"))
    args = parser.parse_args()

    date_prefix = args.date_prefix
    generated_at = datetime.now().isoformat(timespec="seconds")

    print("=" * 60)
    print("Phase A: LLM_assessed Normalization")
    print("=" * 60)
    print(f"Mode: {'dry-run' if args.dry_run else 'write'}")
    print()

    paper_paths = sorted(PAPERS_DIR.glob("*.md"))
    print(f"Papers found: {len(paper_paths)}")

    # Collect all unique strings before normalization
    before_unique: Counter[str] = Counter()
    after_unique: Counter[str] = Counter()
    changes: list[dict] = []
    errors: list[dict] = []
    unchanged_count = 0
    updated_count = 0
    skipped_na = 0
    no_field = 0

    for paper_path in paper_paths:
        try:
            content = paper_path.read_text(encoding="utf-8")
            frontmatter, body = extract_frontmatter(content)
        except (ValueError, UnicodeDecodeError) as e:
            errors.append({"paper": paper_path.name, "error": str(e)})
            continue

        raw = extract_llm_assessed_raw(frontmatter)
        if raw is None:
            no_field += 1
            continue

        cleaned = clean_scalar(raw)
        if not cleaned or cleaned.upper() in ("NA", "N/A", "NONE", "NULL"):
            skipped_na += 1
            continue

        # Count before-state unique tokens
        for tok in cleaned.split(","):
            t = tok.strip()
            if t:
                before_unique[t] += 1

        # Normalize
        normalized_value, original_tokens, canonical_tokens = normalize_llm_field(cleaned)

        # Count after-state unique tokens
        for tok in canonical_tokens:
            after_unique[tok] += 1

        # Check if changed
        if normalized_value == cleaned:
            unchanged_count += 1
            continue

        # Apply change
        new_fm, was_replaced = set_yaml_scalar(frontmatter, "LLM_assessed", normalized_value)
        if not was_replaced:
            errors.append({"paper": paper_path.name, "error": "Failed to replace LLM_assessed line"})
            continue

        # Validate
        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            errors.append({
                "paper": paper_path.name,
                "error": f"YAML validation failed: {'; '.join(issues)}",
            })
            continue

        changes.append({
            "paper": paper_path.name,
            "before": cleaned,
            "after": normalized_value,
            "original_tokens": original_tokens,
            "canonical_tokens": canonical_tokens,
        })

        if not args.dry_run:
            new_content = f"---\n{new_fm.rstrip()}\n---\n{body}"
            paper_path.write_text(new_content, encoding="utf-8")

        updated_count += 1

    # ── Print summary ─────────────────────────────────────────────────────
    print()
    print(f"Papers scanned: {len(paper_paths)}")
    print(f"No LLM_assessed field: {no_field}")
    print(f"LLM_assessed = NA: {skipped_na}")
    print(f"Unchanged (already canonical): {unchanged_count}")
    print(f"Changed: {updated_count}")
    print(f"Errors: {len(errors)}")
    print()
    print(f"Unique model strings BEFORE: {len(before_unique)}")
    print(f"Unique model strings AFTER:  {len(after_unique)}")
    print()

    if after_unique:
        print("Top 20 canonical models (by paper count):")
        for model, count in after_unique.most_common(20):
            print(f"  {model}: {count}")

    # ── Write artifacts ───────────────────────────────────────────────────
    changes_path = LOGS_DIR / f"{date_prefix}-llm-normalization-changes.json"
    summary_path = LOGS_DIR / f"{date_prefix}-llm-normalization-summary.md"

    changes_data = {
        "generated_at": generated_at,
        "mode": "dry-run" if args.dry_run else "write",
        "papers_scanned": len(paper_paths),
        "no_field": no_field,
        "skipped_na": skipped_na,
        "unchanged": unchanged_count,
        "changed": updated_count,
        "errors": len(errors),
        "unique_before": len(before_unique),
        "unique_after": len(after_unique),
        "changes": changes,
        "errors_detail": errors,
    }

    tmp_path = changes_path.parent / f".tmp.{os.getpid()}.json"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(changes_data, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp_path), str(changes_path))
    print(f"\nChanges log: {changes_path.name}")

    # Build summary report
    summary_lines = [
        "# LLM_assessed Normalization Summary",
        "",
        f"Generated: {generated_at}",
        f"Mode: `{'dry-run' if args.dry_run else 'write'}`",
        "",
        "## Overview",
        "",
        f"- Papers scanned: **{len(paper_paths)}**",
        f"- No LLM_assessed field: **{no_field}**",
        f"- LLM_assessed = NA: **{skipped_na}**",
        f"- Already canonical (unchanged): **{unchanged_count}**",
        f"- Changed: **{updated_count}**",
        f"- Errors: **{len(errors)}**",
        "",
        "## Cardinality",
        "",
        f"- Unique model strings BEFORE: **{len(before_unique)}**",
        f"- Unique model strings AFTER: **{len(after_unique)}**",
        f"- Reduction: **{len(before_unique) - len(after_unique)}** ({100 * (1 - len(after_unique) / max(len(before_unique), 1)):.1f}%)",
        "",
        "## Top 30 Canonical Models (after normalization)",
        "",
        "| Rank | Model | Occurrences |",
        "|-----:|-------|------------:|",
    ]
    for rank, (model, count) in enumerate(after_unique.most_common(30), 1):
        summary_lines.append(f"| {rank} | {model} | {count} |")

    summary_lines.extend([
        "",
        "## Top 30 Most Common Changes",
        "",
        "| Before | After |",
        "|--------|-------|",
    ])
    # Aggregate changes by before → after
    change_pairs: Counter[tuple[str, str]] = Counter()
    for ch in changes:
        change_pairs[(ch["before"], ch["after"])] += 1
    for (before, after), count in change_pairs.most_common(30):
        b_display = before if len(before) <= 60 else before[:57] + "..."
        a_display = after if len(after) <= 60 else after[:57] + "..."
        summary_lines.append(f"| {b_display} | {a_display} |")

    if errors:
        summary_lines.extend([
            "",
            "## Errors",
            "",
        ])
        for err in errors[:50]:
            summary_lines.append(f"- `{err['paper']}`: {err['error']}")
        if len(errors) > 50:
            summary_lines.append(f"- ... {len(errors) - 50} more")

    summary_lines.append("")
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")
    print(f"Summary report: {summary_path.name}")
    print("\nDone.")


if __name__ == "__main__":
    main()
