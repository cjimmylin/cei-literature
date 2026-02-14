#!/usr/bin/env python3
"""
Backfill LLM/Data metadata for papers with empty or NA values.

Policy implemented:
1) Target papers where LLM_assessed or DATA_URL is empty/NA/missing.
2) LLM_assessed: conservative extract-based inference only.
3) DATA_URL: repository/dataset-style links only; otherwise NA.
4) Also insert/update ## Data Description for targeted papers.

Outputs:
  logs/YYYYMMDD-llm-data-fix-targets.csv
  logs/YYYYMMDD-llm-data-fix-targets.json
  logs/YYYYMMDD-llm-data-fix-results.csv
  logs/YYYYMMDD-llm-data-fix-unresolved.csv
  logs/YYYYMMDD-llm-data-fix-summary.md
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent"))
from lib.config import LOGS_DIR, PAPERS_DIR  # noqa: E402
from lib.yaml_utils import extract_frontmatter, parse_frontmatter, validate_frontmatter  # noqa: E402

from assess_llm_data import extract_llm_candidates, extract_url_candidates, resolve_extract_for_paper  # noqa: E402


NA_TOKENS = {"", "NA", "N/A", "NONE", "NULL"}
TARGET_STATES = {"missing", "empty", "na"}

APPROVED_DATA_HOST_PATTERNS = [
    "github.com",
    "gitlab.com",
    "huggingface.co",
    "zenodo.org",
    "kaggle.com",
    "osf.io",
    "figshare.com",
    "dataverse.",
    "data.mendeley.com",
    "paperswithcode.com",
]

EVAL_CONTEXT_TERMS = (
    "evaluate",
    "evaluated",
    "evaluation",
    "benchmark",
    "benchmarks",
    "tested",
    "test set",
    "experiments",
    "experimental",
    "compared",
    "comparison",
    "baseline",
    "baselines",
    "results",
    "accuracy",
    "f1",
    "auc",
    "bleu",
    "rouge",
    "score",
    "leaderboard",
    "win rate",
    "metric",
)

MODEL_ROOT_HINTS = (
    "gpt",
    "chatgpt",
    "claude",
    "llama",
    "mistral",
    "mixtral",
    "qwen",
    "gemma",
    "deepseek",
    "bert",
    "roberta",
    "albert",
    "deberta",
    "distilbert",
    "xlnet",
    "electra",
    "t5",
    "bart",
    "bloom",
    "vicuna",
    "alpaca",
    "falcon",
    "phi",
    "grok",
    "palm",
    "lamda",
    "bard",
    "opt",
    "internlm",
    "baichuan",
    "chatglm",
    "cohere",
    "command",
    "aya",
    "dolly",
    "zephyr",
    "wizardlm",
    "codex",
    "instructgpt",
    "word2vec",
    "glove",
    "elmo",
)

ALLOWED_SUFFIX_TOKENS = {
    "mini",
    "turbo",
    "preview",
    "vision",
    "pro",
    "ultra",
    "nano",
    "flash",
    "chat",
    "base",
    "large",
    "small",
    "medium",
    "haiku",
    "sonnet",
    "opus",
    "instruct",
    "guard",
    "plus",
    "reasoner",
}

BANNED_TOKENS = {
    "and",
    "or",
    "for",
    "the",
    "a",
    "an",
    "to",
    "from",
    "with",
    "without",
    "of",
    "in",
    "on",
    "at",
    "by",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "model",
    "models",
    "architecture",
    "architectures",
    "showed",
    "shows",
    "show",
    "perform",
    "performs",
    "performed",
    "provides",
    "provide",
    "through",
    "before",
    "after",
    "which",
    "that",
    "this",
    "still",
    "counterpart",
}


@dataclass
class PaperRecord:
    paper: Path
    fields: dict[str, str]
    frontmatter: str
    body: str


def clean_scalar(value: str | None) -> str:
    s = (value or "").strip()
    if len(s) >= 2 and ((s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'"))):
        s = s[1:-1].strip()
    return s


def scalar_state(value: str | None) -> str:
    if value is None:
        return "missing"
    cleaned = clean_scalar(value)
    if not cleaned:
        return "empty"
    if cleaned.upper() in {"NA", "N/A", "NONE", "NULL"}:
        return "na"
    return "filled"


def parse_http_urls(raw: str | None) -> list[str]:
    if not raw:
        return []
    urls = re.findall(r"https?://[^\s,;\"')\]]+", raw)
    out = []
    seen = set()
    for url in urls:
        u = url.rstrip(".,;:)}]")
        if u and u not in seen:
            out.append(u)
            seen.add(u)
    return out


def normalize_host(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host


def is_approved_data_url(url: str) -> bool:
    host = normalize_host(url)
    if not host:
        return False
    for pat in APPROVED_DATA_HOST_PATTERNS:
        if pat.endswith("."):
            if pat in host:
                return True
        elif host == pat or host.endswith("." + pat):
            return True
    return False


def data_url_rank(url: str) -> tuple[int, str]:
    host = normalize_host(url)
    rank_map = {
        "github.com": 0,
        "huggingface.co": 1,
        "gitlab.com": 2,
        "zenodo.org": 3,
        "kaggle.com": 4,
        "osf.io": 5,
        "figshare.com": 6,
        "data.mendeley.com": 7,
        "paperswithcode.com": 8,
    }
    rank = rank_map.get(host, 20)
    if "dataverse" in host:
        rank = 9
    return (rank, url)


def dedupe_keep_order(items: list[str]) -> list[str]:
    out = []
    seen = set()
    for item in items:
        key = item.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def model_has_eval_context(extract_text: str, model: str) -> bool:
    if not extract_text.strip() or not model.strip():
        return False
    model_re = re.compile(re.escape(model), re.IGNORECASE)
    text_lower = extract_text.lower()
    for match in model_re.finditer(extract_text):
        start = max(0, match.start() - 220)
        end = min(len(extract_text), match.end() + 220)
        window = text_lower[start:end]
        if any(term in window for term in EVAL_CONTEXT_TERMS):
            return True
    return False


def normalize_model_name(model: str) -> str:
    m = " ".join(model.split()).strip(" ,;")
    replacements = {
        "chatgpt": "ChatGPT",
        "gpt-4o": "GPT-4o",
        "gpt-4": "GPT-4",
        "gpt-3.5": "GPT-3.5",
        "gpt-3": "GPT-3",
        "gpt-2": "GPT-2",
        "llama": "Llama",
        "llama-2": "Llama-2",
        "llama-3": "Llama-3",
        "claude": "Claude",
        "gemini": "Gemini",
        "mistral": "Mistral",
        "mixtral": "Mixtral",
        "qwen": "Qwen",
        "deepseek": "DeepSeek",
        "phi": "Phi",
        "bert": "BERT",
        "roberta": "RoBERTa",
        "albert": "ALBERT",
        "xlnet": "XLNet",
        "t5": "T5",
    }
    key = m.lower()
    if key in replacements:
        return replacements[key]
    return m


def is_plausible_model_name(model: str) -> bool:
    m = " ".join(model.split()).strip(" ,;")
    if len(m) < 2 or len(m) > 80:
        return False
    if not re.fullmatch(r"[A-Za-z0-9.+\-_/ ]+", m):
        return False

    low = m.lower()
    if "http://" in low or "https://" in low:
        return False
    if "www." in low:
        return False
    if len(m.split()) > 4:
        return False
    if not any(root in low for root in MODEL_ROOT_HINTS):
        return False

    # Common false-positive pattern from BART/BLOOM partial matches.
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
            # small lowercase fragments are typically text artifacts
            return False
        if re.fullmatch(r"[A-Z]{2,5}", token):
            continue
        return False

    return True


def conservative_models_from_extract(extract_text: str) -> tuple[list[str], list[str]]:
    if not extract_text.strip():
        return [], []
    raw_candidates = extract_llm_candidates(extract_text)
    plausible = [c for c in raw_candidates if is_plausible_model_name(c)]
    confident = [c for c in plausible if model_has_eval_context(extract_text, c)]
    confident = [normalize_model_name(c) for c in confident]
    confident = dedupe_keep_order(confident)
    return plausible, confident


def select_data_url(fields: dict[str, str], extract_urls: list[str]) -> tuple[str, list[str]]:
    candidate_urls = []
    candidate_urls.extend(extract_urls)
    candidate_urls.extend(parse_http_urls(fields.get("url")))
    candidate_urls.extend(parse_http_urls(fields.get("external_pdf")))

    candidate_urls = dedupe_keep_order(candidate_urls)
    approved = [u for u in candidate_urls if is_approved_data_url(u)]
    approved = sorted(approved, key=data_url_rank)

    if not approved:
        return "NA", candidate_urls
    return approved[0], candidate_urls


def yaml_scalar_line(key: str, value: str) -> str:
    if value == "NA":
        return f"{key}: NA"
    safe = value.replace('"', "'")
    return f'{key}: "{safe}"'


def set_yaml_scalar(frontmatter: str, key: str, value: str, anchors: list[str]) -> tuple[str, str]:
    line = yaml_scalar_line(key, value)
    pattern = r"^{}:.*$".format(re.escape(key))
    replaced, count = re.subn(pattern, line, frontmatter, count=1, flags=re.MULTILINE)
    if count > 0:
        return replaced, "replaced"

    for anchor in anchors:
        m = re.search(r"^{}:.*$".format(re.escape(anchor)), frontmatter, flags=re.MULTILINE)
        if m:
            insert_pos = m.end()
            inserted = frontmatter[:insert_pos] + "\n" + line + frontmatter[insert_pos:]
            return inserted, f"inserted_after_{anchor}"

    appended = frontmatter.rstrip() + "\n" + line
    return appended, "appended"


def is_placeholder_description(text: str) -> bool:
    t = text.strip()
    if not t:
        return True
    t_upper = t.upper()
    if t_upper in {"NA", "N/A", "NONE", "NULL", "TBD"}:
        return True
    if t.lower().startswith("backfill summary:"):
        return True
    if "no data description" in t.lower():
        return True
    return False


def insert_data_description(body: str, description: str) -> tuple[str, str]:
    section = "## Data Description\n\n{}\n".format(description.strip())

    # Replace existing section if placeholder/backfill text.
    existing = re.search(r"(?ms)^## Data Description\s*\n(.*?)(?=^## |\Z)", body)
    if existing:
        current = existing.group(1).strip()
        if not is_placeholder_description(current):
            return body, "kept_existing"
        start = existing.start()
        end = existing.end()
        replacement = section + ("\n" if body[end:end + 1] != "\n" else "")
        return body[:start] + replacement + body[end:], "updated_existing"

    # Insert after Dataset Information section if present.
    dataset_block = re.search(r"(?ms)^## Dataset Information\s*\n.*?(?=^## |\Z)", body)
    if dataset_block:
        insert_pos = dataset_block.end()
        insertion = "\n" + section
        return body[:insert_pos] + insertion + body[insert_pos:], "inserted_after_dataset_info"

    # Insert before Notes or Citation Info.
    for heading in ("## Notes", "## Citation Info"):
        m = re.search(r"(?m)^{}\s*$".format(re.escape(heading)), body)
        if m:
            insert_pos = m.start()
            insertion = section + "\n"
            return body[:insert_pos] + insertion + body[insert_pos:], "inserted_before_heading"

    # Fallback append.
    suffix = "\n" if body.endswith("\n") else "\n\n"
    return body + suffix + section + "\n", "appended"


def build_data_description(llm_value: str, data_url: str, has_extract: bool) -> str:
    if llm_value != "NA" and data_url != "NA":
        return (
            "Backfill summary: Models assessed include {}. "
            "Verified dataset/resource link: {}."
        ).format(llm_value, data_url)
    if llm_value != "NA":
        if has_extract:
            return (
                "Backfill summary: Models assessed include {}. "
                "No high-confidence repository-style data URL was identified."
            ).format(llm_value)
        return (
            "Backfill summary: Models assessed include {}. "
            "No PDF extract was available to verify a repository-style data URL."
        ).format(llm_value)
    if data_url != "NA":
        return (
            "Backfill summary: No high-confidence evaluated model list was identified. "
            "Verified dataset/resource link: {}."
        ).format(data_url)
    if has_extract:
        return (
            "Backfill summary: No high-confidence evaluated model list or repository-style "
            "data URL was identified from available extract/context."
        )
    return (
        "Backfill summary: No PDF extract was available, and no repository-style data URL "
        "could be verified from metadata context."
    )


def read_paper_record(path: Path) -> tuple[PaperRecord | None, str | None]:
    try:
        content = path.read_text(encoding="utf-8")
        frontmatter, body = extract_frontmatter(content)
        fields = parse_frontmatter(frontmatter)
        return PaperRecord(path, fields, frontmatter, body), None
    except Exception as exc:  # broad catch for malformed files
        return None, str(exc)


def write_artifact_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill LLM_assessed/DATA_URL/Data Description")
    parser.add_argument("--date-prefix", default=date.today().strftime("%Y%m%d"))
    parser.add_argument("--dry-run", action="store_true", help="Compute and report without writing paper files")
    parser.add_argument(
        "--force-recompute-llm-from-results",
        default="",
        help=(
            "Optional path to a previous results CSV. Papers where llm_source is "
            "extract_conservative or fallback_NA will have LLM_assessed recomputed "
            "even if currently filled."
        ),
    )
    parser.add_argument(
        "--force-recompute-llm-for-backfill-desc",
        action="store_true",
        help=(
            "Force recomputation of LLM_assessed for papers whose body contains "
            "'Backfill summary:' (used to repair previous backfill-only values)."
        ),
    )
    parser.add_argument(
        "--sanitize-existing-llm",
        action="store_true",
        help=(
            "Sanitize existing filled LLM_assessed values on targeted papers by "
            "dropping implausible tokens; set NA if nothing plausible remains."
        ),
    )
    args = parser.parse_args()

    date_prefix = args.date_prefix
    generated_at = datetime.now().isoformat(timespec="seconds")

    force_llm_papers: set[str] = set()
    if args.force_recompute_llm_from_results:
        with open(args.force_recompute_llm_from_results, "r", encoding="utf-8") as f:
            rows = csv.DictReader(f)
            for row in rows:
                if row.get("llm_source") in {"extract_conservative", "fallback_NA"}:
                    paper = (row.get("paper") or "").strip()
                    if paper:
                        force_llm_papers.add(paper)

    target_rows: list[dict] = []
    result_rows: list[dict] = []
    unresolved_rows: list[dict] = []
    validation_errors: list[dict] = []
    counters = Counter()
    before_llm = Counter()
    before_data = Counter()
    after_llm = Counter()
    after_data = Counter()
    desc_ops = Counter()
    url_domain_counts = Counter()
    unresolved_reasons = Counter()

    paper_paths = sorted(PAPERS_DIR.glob("*.md"))
    counters["papers_total"] = len(paper_paths)

    for paper_path in paper_paths:
        rec, err = read_paper_record(paper_path)
        if err:
            counters["read_error"] += 1
            validation_errors.append({"paper": paper_path.name, "error": err})
            continue

        llm_raw = rec.fields.get("LLM_assessed")
        data_raw = rec.fields.get("DATA_URL")
        llm_state = scalar_state(llm_raw)
        data_state = scalar_state(data_raw)
        before_llm[llm_state] += 1
        before_data[data_state] += 1

        force_llm = paper_path.name in force_llm_papers
        if args.force_recompute_llm_for_backfill_desc and "Backfill summary:" in rec.body:
            force_llm = True
        target = llm_state in TARGET_STATES or data_state in TARGET_STATES or force_llm
        if not target:
            continue

        counters["target_total"] += 1
        target_rows.append(
            {
                "paper": paper_path.name,
                "llm_state": llm_state,
                "data_state": data_state,
                "llm_value_raw": clean_scalar(llm_raw),
                "data_value_raw": clean_scalar(data_raw),
                "url": clean_scalar(rec.fields.get("url", "")),
                "external_pdf": clean_scalar(rec.fields.get("external_pdf", "")),
                "pdf_extract": clean_scalar(rec.fields.get("pdf_extract", "")),
            }
        )

        extract_ref, extract_path = resolve_extract_for_paper(paper_path, rec.frontmatter)
        extract_text = ""
        if extract_path and extract_path.exists():
            try:
                extract_text = extract_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                extract_text = ""
        has_extract = bool(extract_text.strip())
        counters["target_with_extract"] += int(has_extract)
        counters["target_without_extract"] += int(not has_extract)

        extract_url_hits = extract_url_candidates(extract_text) if has_extract else []
        raw_model_candidates, confident_models = conservative_models_from_extract(extract_text)

        llm_before = clean_scalar(llm_raw) or "NA"
        data_before = clean_scalar(data_raw) or "NA"

        llm_after = llm_before
        data_after = data_before

        llm_source = "kept_existing"
        data_source = "kept_existing"

        llm_should_update = False
        if args.sanitize_existing_llm and llm_state == "filled":
            existing_tokens = [normalize_model_name(t.strip()) for t in llm_before.split(",") if t.strip()]
            existing_tokens = [t for t in existing_tokens if is_plausible_model_name(t)]
            existing_tokens = dedupe_keep_order(existing_tokens)
            sanitized_llm = ", ".join(existing_tokens) if existing_tokens else "NA"
            if sanitized_llm != llm_before:
                llm_after = sanitized_llm
                llm_source = "sanitize_existing"
                llm_should_update = True

        recompute_llm = llm_state in TARGET_STATES or force_llm
        if recompute_llm:
            llm_after = ", ".join(confident_models) if confident_models else "NA"
            if force_llm:
                llm_source = "forced_recompute_extract" if confident_models else "forced_recompute_NA"
            else:
                llm_source = "extract_conservative" if confident_models else "fallback_NA"
            llm_should_update = True

        if data_state in TARGET_STATES:
            selected_url, all_candidates = select_data_url(rec.fields, extract_url_hits)
            data_after = selected_url
            data_source = "approved_candidate" if selected_url != "NA" else "fallback_NA"
        else:
            all_candidates = []

        description_text = build_data_description(llm_after, data_after, has_extract)

        new_frontmatter = rec.frontmatter
        yaml_ops = []
        if llm_should_update:
            new_frontmatter, op = set_yaml_scalar(
                new_frontmatter,
                "LLM_assessed",
                llm_after,
                anchors=["data_metrics", "is_dataset", "is_eval", "is_benchmark"],
            )
            yaml_ops.append(op)
        if data_state in TARGET_STATES:
            new_frontmatter, op = set_yaml_scalar(
                new_frontmatter,
                "DATA_URL",
                data_after,
                anchors=["LLM_assessed", "data_metrics", "is_dataset"],
            )
            yaml_ops.append(op)

        new_body, desc_op = insert_data_description(rec.body, description_text)
        desc_ops[desc_op] += 1

        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            counters["yaml_validation_error"] += 1
            validation_errors.append(
                {
                    "paper": paper_path.name,
                    "error": "YAML validation failed: {}".format("; ".join(issues)),
                }
            )
            continue

        new_content = "---\n{}\n---\n{}".format(new_frontmatter.rstrip(), new_body)
        original_content = "---\n{}\n---\n{}".format(rec.frontmatter.rstrip(), rec.body)
        changed = new_content != original_content

        if changed and not args.dry_run:
            paper_path.write_text(new_content, encoding="utf-8")
            counters["updated_files"] += 1
        elif changed:
            counters["would_update_files"] += 1
        else:
            counters["unchanged_files"] += 1

        if data_after != "NA":
            url_domain_counts[normalize_host(data_after)] += 1

        after_llm[scalar_state(llm_after)] += 1
        after_data[scalar_state(data_after)] += 1

        unresolved = (llm_after == "NA" and data_after == "NA")
        if unresolved:
            reason = "no_extract_no_candidates"
            if has_extract:
                reason = "extract_present_no_confident_signal"
            unresolved_reasons[reason] += 1
            unresolved_rows.append(
                {
                    "paper": paper_path.name,
                    "reason": reason,
                    "has_extract": "Yes" if has_extract else "No",
                    "extract_path": extract_ref or "",
                    "llm_state_before": llm_state,
                    "data_state_before": data_state,
                    "llm_after": llm_after,
                    "data_after": data_after,
                    "url": clean_scalar(rec.fields.get("url", "")),
                    "external_pdf": clean_scalar(rec.fields.get("external_pdf", "")),
                }
            )

        result_rows.append(
            {
                "paper": paper_path.name,
                "changed": "Yes" if changed else "No",
                "llm_state_before": llm_state,
                "data_state_before": data_state,
                "LLM_assessed_before": llm_before,
                "DATA_URL_before": data_before,
                "LLM_assessed_after": llm_after,
                "DATA_URL_after": data_after,
                "llm_source": llm_source,
                "data_source": data_source,
                "has_extract": "Yes" if has_extract else "No",
                "extract_path": extract_ref or "",
                "raw_model_candidates": ", ".join(raw_model_candidates),
                "confident_models": ", ".join(confident_models),
                "url_candidates": ", ".join(all_candidates),
                "yaml_ops": ", ".join(yaml_ops),
                "desc_op": desc_op,
            }
        )

    # Derive complete after-state snapshot.
    if result_rows:
        # Start from before-state and then overwrite target contributions with after-state tallies.
        # A direct full rescan is simpler and keeps counts honest.
        after_llm.clear()
        after_data.clear()
        for paper_path in paper_paths:
            rec, err = read_paper_record(paper_path)
            if err:
                continue
            after_llm[scalar_state(rec.fields.get("LLM_assessed"))] += 1
            after_data[scalar_state(rec.fields.get("DATA_URL"))] += 1

    targets_csv = LOGS_DIR / f"{date_prefix}-llm-data-fix-targets.csv"
    targets_json = LOGS_DIR / f"{date_prefix}-llm-data-fix-targets.json"
    results_csv = LOGS_DIR / f"{date_prefix}-llm-data-fix-results.csv"
    unresolved_csv = LOGS_DIR / f"{date_prefix}-llm-data-fix-unresolved.csv"
    summary_md = LOGS_DIR / f"{date_prefix}-llm-data-fix-summary.md"

    write_artifact_csv(
        targets_csv,
        target_rows,
        [
            "paper",
            "llm_state",
            "data_state",
            "llm_value_raw",
            "data_value_raw",
            "url",
            "external_pdf",
            "pdf_extract",
        ],
    )
    targets_json.write_text(
        json.dumps(
            {
                "generated_at": generated_at,
                "target_count": len(target_rows),
                "targets": target_rows,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    write_artifact_csv(
        results_csv,
        result_rows,
        [
            "paper",
            "changed",
            "llm_state_before",
            "data_state_before",
            "LLM_assessed_before",
            "DATA_URL_before",
            "LLM_assessed_after",
            "DATA_URL_after",
            "llm_source",
            "data_source",
            "has_extract",
            "extract_path",
            "raw_model_candidates",
            "confident_models",
            "url_candidates",
            "yaml_ops",
            "desc_op",
        ],
    )
    write_artifact_csv(
        unresolved_csv,
        unresolved_rows,
        [
            "paper",
            "reason",
            "has_extract",
            "extract_path",
            "llm_state_before",
            "data_state_before",
            "llm_after",
            "data_after",
            "url",
            "external_pdf",
        ],
    )

    summary_lines = [
        "# LLM/Data Backfill Summary",
        "",
        f"Generated: {generated_at}",
        f"Date prefix: `{date_prefix}`",
        f"Mode: `{'dry-run' if args.dry_run else 'write'}`",
        "",
        "## Overall",
        "",
        f"- Papers scanned: **{counters['papers_total']}**",
        f"- Target papers (LLM_assessed or DATA_URL in empty/NA/missing): **{counters['target_total']}**",
        f"- Target papers with extract: **{counters['target_with_extract']}**",
        f"- Target papers without extract: **{counters['target_without_extract']}**",
        f"- Files changed: **{counters['updated_files']}**",
        f"- Files that would change (dry-run): **{counters['would_update_files']}**",
        f"- Unchanged targets: **{counters['unchanged_files']}**",
        f"- Read errors: **{counters['read_error']}**",
        f"- YAML validation errors: **{counters['yaml_validation_error']}**",
        "",
        "## Field State Before",
        "",
        f"- LLM_assessed: {dict(before_llm)}",
        f"- DATA_URL: {dict(before_data)}",
        "",
        "## Field State After",
        "",
        f"- LLM_assessed: {dict(after_llm)}",
        f"- DATA_URL: {dict(after_data)}",
        "",
        "## Data Description Operations",
        "",
        f"- Operations: {dict(desc_ops)}",
        "",
        "## Unresolved",
        "",
        f"- Count (both LLM_assessed and DATA_URL = NA after processing): **{len(unresolved_rows)}**",
        f"- Reasons: {dict(unresolved_reasons)}",
        "",
        "## Top DATA_URL Domains",
        "",
    ]
    if url_domain_counts:
        for host, count in url_domain_counts.most_common(20):
            summary_lines.append(f"- {host}: {count}")
    else:
        summary_lines.append("- None")

    summary_lines.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- `{targets_csv}`",
            f"- `{targets_json}`",
            f"- `{results_csv}`",
            f"- `{unresolved_csv}`",
            f"- `{summary_md}`",
            "",
        ]
    )

    if validation_errors:
        summary_lines.append("## Validation Errors")
        summary_lines.append("")
        for row in validation_errors[:200]:
            summary_lines.append("- `{}`: {}".format(row["paper"], row["error"]))
        if len(validation_errors) > 200:
            summary_lines.append("- ... {} more".format(len(validation_errors) - 200))
        summary_lines.append("")

    summary_md.write_text("\n".join(summary_lines), encoding="utf-8")

    print(f"papers_scanned={counters['papers_total']}")
    print(f"target_papers={counters['target_total']}")
    print(f"updated_files={counters['updated_files']}")
    print(f"would_update_files={counters['would_update_files']}")
    print(f"unresolved_count={len(unresolved_rows)}")
    print(f"targets_csv={targets_csv}")
    print(f"targets_json={targets_json}")
    print(f"results_csv={results_csv}")
    print(f"unresolved_csv={unresolved_csv}")
    print(f"summary_md={summary_md}")


if __name__ == "__main__":
    main()
