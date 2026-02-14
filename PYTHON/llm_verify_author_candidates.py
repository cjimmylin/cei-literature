#!/usr/bin/env python3
"""
LLM verification for parsed author candidates against PDF extract evidence.

Supports two-model consensus across OpenAI, Anthropic, and Gemini providers.

Input record shape (minimum):
{
  "paper_filename": "...",
  "title": "...",
  "parsed_authors": ["..."],
  "evidence_snippet": "...",
  "source_type": "pdf_extract|api",
  "pdf_extract": "PDF Extracts/....md"
}
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


SYSTEM_PROMPT_A = """You are validating paper author extraction.
Return ONLY a JSON object with this exact schema:
{
  "decision": "accept" | "reject" | "unsure",
  "normalized_authors": ["Author One", "Author Two"],
  "confidence": 0.0,
  "reason_codes": ["code1", "code2"],
  "notes": "short note"
}

Rules:
- Use the evidence snippet to determine true author names.
- Reject headers, journal boilerplate, affiliations, institutions, emails, and section titles.
- Keep author order when recoverable.
- If evidence is ambiguous, use "unsure".
- If parsed_authors are wrong but snippet clearly contains correct authors, return decision "accept" with corrected normalized_authors.
"""

SYSTEM_PROMPT_B = """You are a skeptical second-pass validator for paper author extraction.
Return ONLY a JSON object with this exact schema:
{
  "decision": "accept" | "reject" | "unsure",
  "normalized_authors": ["Author One", "Author Two"],
  "confidence": 0.0,
  "reason_codes": ["code1", "code2"],
  "notes": "short note"
}

Rules:
- Be conservative and reject uncertain names.
- Accept only if the evidence clearly shows author names (not title text, venue headers, affiliations, institutions, or keywords).
- Preserve author order when recoverable.
- If parsed_authors are partly wrong but evidence supports corrected names, return "accept" with corrected normalized_authors.
"""


@dataclass
class ModelSpec:
    provider: str
    model: str
    temperature: float = 0.0
    timeout: float = 45.0


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        out = float(value)  # type: ignore[arg-type]
    except Exception:
        return default
    if out < 0.0:
        return 0.0
    if out > 1.0:
        return 1.0
    return out


def _canonical_name(name: str) -> str:
    value = " ".join((name or "").strip().split())
    value = value.strip(",;.")
    return value


def _normalize_author_list(values: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen = set()
    for value in values:
        name = _canonical_name(str(value))
        if not name:
            continue
        key = name.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(name)
    return out


def _json_from_text(text: str) -> Dict[str, object]:
    raw = (text or "").strip()
    if not raw:
        raise ValueError("Empty model response")

    try:
        obj = json.loads(raw)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass

    # Fallback: extract first JSON object substring.
    start = raw.find("{")
    end = raw.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("Could not parse JSON object from model response")

    obj = json.loads(raw[start : end + 1])
    if not isinstance(obj, dict):
        raise ValueError("Parsed JSON payload is not an object")
    return obj


def _coerce_verdict(payload: Dict[str, object]) -> Dict[str, object]:
    decision = str(payload.get("decision", "")).strip().lower()
    if decision not in {"accept", "reject", "unsure"}:
        decision = "unsure"

    raw_authors = payload.get("normalized_authors", [])
    if isinstance(raw_authors, str):
        raw_authors = [raw_authors]
    if not isinstance(raw_authors, list):
        raw_authors = []

    authors = _normalize_author_list([str(x) for x in raw_authors])
    confidence = _safe_float(payload.get("confidence", 0.0))

    reason_codes = payload.get("reason_codes", [])
    if isinstance(reason_codes, str):
        reason_codes = [reason_codes]
    if not isinstance(reason_codes, list):
        reason_codes = []
    reasons = [str(x).strip() for x in reason_codes if str(x).strip()]

    notes = str(payload.get("notes", "")).strip()

    return {
        "decision": decision,
        "normalized_authors": authors,
        "confidence": confidence,
        "reason_codes": reasons,
        "notes": notes,
    }


def _authors_equivalent(left: List[str], right: List[str]) -> bool:
    if not left or not right:
        return False

    def _norm(name: str) -> str:
        base = re.sub(r"[^a-z0-9 ]", " ", name.casefold())
        return " ".join(base.split())

    left_norm = [_norm(x) for x in left]
    right_norm = [_norm(x) for x in right]

    if left_norm == right_norm:
        return True
    if left_norm[0] != right_norm[0]:
        return False

    overlap = set(left_norm) & set(right_norm)
    ratio = len(overlap) / float(max(len(set(left_norm)), len(set(right_norm))))
    return ratio >= 0.7


def _build_user_prompt(record: Dict[str, object], max_snippet_chars: int = 6000) -> str:
    title = str(record.get("title", "")).strip()
    parsed_authors = record.get("parsed_authors", [])
    if not isinstance(parsed_authors, list):
        parsed_authors = []
    parsed = [str(x) for x in parsed_authors if str(x).strip()]

    source_type = str(record.get("source_type", "")).strip()
    paper_filename = str(record.get("paper_filename", "")).strip()
    pdf_extract = str(record.get("pdf_extract", "")).strip()

    snippet = str(record.get("evidence_snippet", "")).strip()
    if len(snippet) > max_snippet_chars:
        snippet = snippet[:max_snippet_chars]

    return (
        f"paper_filename: {paper_filename}\n"
        f"title: {title}\n"
        f"source_type: {source_type}\n"
        f"pdf_extract: {pdf_extract}\n"
        f"parsed_authors: {json.dumps(parsed, ensure_ascii=False)}\n\n"
        "Evidence snippet:\n"
        f"{snippet}"
    )


def _http_json_request(url: str, payload: Dict[str, object], headers: Dict[str, str], timeout: float) -> Dict[str, object]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={**headers, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise ValueError("Provider response is not a JSON object")
    return parsed


def _call_openai(spec: ModelSpec, user_prompt: str, system_prompt: str) -> Dict[str, object]:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY")

    payload: Dict[str, object] = {
        "model": spec.model,
        "temperature": spec.temperature,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    headers = {"Authorization": f"Bearer {api_key}"}
    parsed = _http_json_request(
        "https://api.openai.com/v1/chat/completions",
        payload,
        headers,
        spec.timeout,
    )

    choices = parsed.get("choices", [])
    if not isinstance(choices, list) or not choices:
        raise RuntimeError("OpenAI response has no choices")
    msg = choices[0].get("message", {}) if isinstance(choices[0], dict) else {}
    content = msg.get("content", "") if isinstance(msg, dict) else ""
    if not isinstance(content, str):
        raise RuntimeError("OpenAI message content is not a string")
    return _coerce_verdict(_json_from_text(content))


def _call_anthropic(spec: ModelSpec, user_prompt: str, system_prompt: str) -> Dict[str, object]:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("Missing ANTHROPIC_API_KEY")

    payload: Dict[str, object] = {
        "model": spec.model,
        "max_tokens": 800,
        "temperature": spec.temperature,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": user_prompt},
        ],
    }
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    parsed = _http_json_request(
        "https://api.anthropic.com/v1/messages",
        payload,
        headers,
        spec.timeout,
    )

    content = parsed.get("content", [])
    if not isinstance(content, list) or not content:
        raise RuntimeError("Anthropic response has no content")

    text_chunks: List[str] = []
    for block in content:
        if not isinstance(block, dict):
            continue
        if block.get("type") == "text" and isinstance(block.get("text"), str):
            text_chunks.append(block["text"])
    raw = "\n".join(text_chunks).strip()
    if not raw:
        raise RuntimeError("Anthropic content text is empty")
    return _coerce_verdict(_json_from_text(raw))


def _call_gemini(spec: ModelSpec, user_prompt: str, system_prompt: str) -> Dict[str, object]:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip() or os.environ.get("GOOGLE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY or GOOGLE_API_KEY")

    model = spec.model.strip()
    if not model:
        raise RuntimeError("Gemini model name is empty")

    # Accept both "gemini-2.0-flash" and full "models/gemini-2.0-flash".
    model_path = model if model.startswith("models/") else f"models/{model}"
    encoded_model_path = urllib.parse.quote(model_path, safe="/-._")
    url = f"https://generativelanguage.googleapis.com/v1beta/{encoded_model_path}:generateContent?key={urllib.parse.quote(api_key, safe='')}"

    payload: Dict[str, object] = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_prompt}],
            }
        ],
        "generationConfig": {
            "temperature": spec.temperature,
            "responseMimeType": "application/json",
        },
    }

    parsed = _http_json_request(url, payload, headers={}, timeout=spec.timeout)
    candidates = parsed.get("candidates", [])
    if not isinstance(candidates, list) or not candidates:
        raise RuntimeError("Gemini response has no candidates")

    first = candidates[0] if isinstance(candidates[0], dict) else {}
    content = first.get("content", {}) if isinstance(first, dict) else {}
    parts = content.get("parts", []) if isinstance(content, dict) else []
    if not isinstance(parts, list) or not parts:
        raise RuntimeError("Gemini candidate has no content parts")

    text_chunks: List[str] = []
    for part in parts:
        if isinstance(part, dict) and isinstance(part.get("text"), str):
            text_chunks.append(part["text"])
    raw = "\n".join(text_chunks).strip()
    if not raw:
        raise RuntimeError("Gemini content text is empty")
    return _coerce_verdict(_json_from_text(raw))


def run_model_verification(record: Dict[str, object], spec: ModelSpec, system_prompt: str) -> Dict[str, object]:
    prompt = _build_user_prompt(record)
    provider = spec.provider.strip().lower()
    if provider == "openai":
        return _call_openai(spec, prompt, system_prompt)
    if provider == "anthropic":
        return _call_anthropic(spec, prompt, system_prompt)
    if provider == "gemini":
        return _call_gemini(spec, prompt, system_prompt)
    raise RuntimeError(f"Unsupported provider: {spec.provider}")


def _consensus(verdict_a: Dict[str, object], verdict_b: Dict[str, object]) -> Tuple[str, bool, List[str]]:
    a_decision = str(verdict_a.get("decision", "unsure"))
    b_decision = str(verdict_b.get("decision", "unsure"))
    a_authors = verdict_a.get("normalized_authors", [])
    b_authors = verdict_b.get("normalized_authors", [])
    if not isinstance(a_authors, list):
        a_authors = []
    if not isinstance(b_authors, list):
        b_authors = []

    a_authors_norm = _normalize_author_list([str(x) for x in a_authors])
    b_authors_norm = _normalize_author_list([str(x) for x in b_authors])

    if a_decision == "accept" and b_decision == "accept":
        if _authors_equivalent(a_authors_norm, b_authors_norm):
            # Keep the longer list if one includes extra valid names.
            authors = a_authors_norm if len(a_authors_norm) >= len(b_authors_norm) else b_authors_norm
            return "accept", True, authors
        return "disagree_authors", False, []

    if a_decision == "reject" and b_decision == "reject":
        return "reject", False, []

    if a_decision == "unsure" and b_decision == "unsure":
        return "unsure", False, []

    return "disagree_decision", False, []


def verify_records(
    records: List[Dict[str, object]],
    model_a: ModelSpec,
    model_b: ModelSpec,
) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    for record in records:
        row = dict(record)
        row["llm_model_a_provider"] = model_a.provider
        row["llm_model_a"] = model_a.model
        row["llm_model_b_provider"] = model_b.provider
        row["llm_model_b"] = model_b.model

        try:
            verdict_a = run_model_verification(row, model_a, SYSTEM_PROMPT_A)
            row["llm_model_a_error"] = ""
        except Exception as exc:
            verdict_a = {"decision": "unsure", "normalized_authors": [], "confidence": 0.0, "reason_codes": ["model_error"], "notes": ""}
            row["llm_model_a_error"] = str(exc)

        try:
            verdict_b = run_model_verification(row, model_b, SYSTEM_PROMPT_B)
            row["llm_model_b_error"] = ""
        except Exception as exc:
            verdict_b = {"decision": "unsure", "normalized_authors": [], "confidence": 0.0, "reason_codes": ["model_error"], "notes": ""}
            row["llm_model_b_error"] = str(exc)

        row["llm_model_a_verdict"] = verdict_a
        row["llm_model_b_verdict"] = verdict_b

        consensus_decision, approved, consensus_authors = _consensus(verdict_a, verdict_b)
        row["llm_consensus_decision"] = consensus_decision
        row["llm_consensus_approved"] = approved
        row["llm_consensus_authors"] = consensus_authors

        out.append(row)
    return out


def summarize_verified_rows(rows: Iterable[Dict[str, object]]) -> Dict[str, int]:
    summary = {
        "rows_total": 0,
        "consensus_accept": 0,
        "consensus_reject": 0,
        "consensus_unsure": 0,
        "consensus_disagree_decision": 0,
        "consensus_disagree_authors": 0,
        "model_a_errors": 0,
        "model_b_errors": 0,
    }
    for row in rows:
        summary["rows_total"] += 1
        decision = str(row.get("llm_consensus_decision", ""))
        key = f"consensus_{decision}"
        if key in summary:
            summary[key] += 1
        if row.get("llm_model_a_error"):
            summary["model_a_errors"] += 1
        if row.get("llm_model_b_error"):
            summary["model_b_errors"] += 1
    return summary


def _read_json_records(path: Path) -> List[Dict[str, object]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and isinstance(data.get("records"), list):
        records = data["records"]
    elif isinstance(data, list):
        records = data
    else:
        raise ValueError("Input JSON must be a list or an object with a 'records' list")
    out: List[Dict[str, object]] = []
    for item in records:
        if isinstance(item, dict):
            out.append(item)
    return out


def _write_csv(rows: List[Dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "paper_filename",
        "title",
        "source_type",
        "pdf_extract",
        "parsed_authors",
        "llm_consensus_decision",
        "llm_consensus_approved",
        "llm_consensus_authors",
        "llm_model_a_provider",
        "llm_model_a",
        "llm_model_a_error",
        "llm_model_a_verdict",
        "llm_model_b_provider",
        "llm_model_b",
        "llm_model_b_error",
        "llm_model_b_verdict",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            write_row = dict(row)
            for key in ("parsed_authors", "llm_consensus_authors", "llm_model_a_verdict", "llm_model_b_verdict"):
                if key in write_row:
                    write_row[key] = json.dumps(write_row[key], ensure_ascii=False)
            writer.writerow({k: write_row.get(k, "") for k in fields})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="LLM verification for author candidates.")
    parser.add_argument("--input-json", type=Path, required=True, help="Input candidates JSON.")
    parser.add_argument("--output-json", type=Path, required=True, help="Output verified JSON.")
    parser.add_argument("--output-csv", type=Path, default=None, help="Optional output CSV path.")
    parser.add_argument("--model-a-provider", choices=["openai", "anthropic", "gemini"], required=True)
    parser.add_argument("--model-a", type=str, required=True)
    parser.add_argument("--model-b-provider", choices=["openai", "anthropic", "gemini"], required=True)
    parser.add_argument("--model-b", type=str, required=True)
    parser.add_argument("--timeout", type=float, default=45.0)
    parser.add_argument("--temperature", type=float, default=0.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rows = _read_json_records(args.input_json)

    model_a = ModelSpec(
        provider=args.model_a_provider,
        model=args.model_a,
        timeout=args.timeout,
        temperature=args.temperature,
    )
    model_b = ModelSpec(
        provider=args.model_b_provider,
        model=args.model_b,
        timeout=args.timeout,
        temperature=args.temperature,
    )

    verified = verify_records(rows, model_a, model_b)
    summary = summarize_verified_rows(verified)

    payload = {
        "summary": summary,
        "records": verified,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.output_csv:
        _write_csv(verified, args.output_csv)

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
