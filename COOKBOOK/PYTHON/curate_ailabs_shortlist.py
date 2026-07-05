#!/usr/bin/env python3
"""
COOKBOOK Phase 0 — AI Labs shortlist curation.

Applies a Fable-curated pattern list (values-alignment relevance + recency)
to 20260705-ailabs-listing.json and emits 20260705-ailabs-shortlist.json.
Duplicate copies of the same report (same arXiv id or same normalized title)
are collapsed, keeping the longest extract.
"""

import json
import re
from datetime import datetime
from pathlib import Path

EVIDENCE_DIR = Path(__file__).resolve().parents[1] / "30-EVIDENCE"
LISTING = EVIDENCE_DIR / "20260705-ailabs-listing.json"
OUT = EVIDENCE_DIR / "20260705-ailabs-shortlist.json"

# (title regex, rationale) — case-insensitive search over cleaned title
PATTERNS = [
    # Anthropic — alignment methods & values-relevant safety research
    (r"Constitutional AI Harmlessness", "foundational alignment method"),
    (r"Training a Helpful and Harmless", "RLHF methodology"),
    (r"General Language Assistant", "alignment lab framing + HHH evals"),
    (r"Collective Constitutional", "democratic input to values"),
    (r"Moral Self Correction", "moral capability evaluation"),
    (r"Understanding Sycophancy", "sycophancy measurement"),
    (r"Dont Always Say What They Think", "CoT faithfulness (both LM + reasoning variants)"),
    (r"Measuring Faithfulness", "CoT faithfulness methodology"),
    (r"Sleeper Agents", "deceptive alignment eval"),
    (r"Alignment Faking", "alignment faking eval"),
    (r"Sabotage Evaluations", "agentic safety evals"),
    (r"Many shot Jailbreaking", "robustness eval"),
    (r"Reward Hacking", "in-context reward hacking"),
    (r"Probes Detect Sycophancy", "sycophancy probes"),
    (r"Automated Red Teaming", "red-teaming methodology"),
    (r"Constitutional Classifiers", "safety classifier evals (v1 + plus-plus)"),
    (r"Anthropic Model Spec", "explicit values specification"),
    (r"Claude 3\.7 Sonnet System Card", "system card - eval methodology"),
    (r"Claude 4 Opus Sonnet System Card", "system card - values/agentic evals"),
    (r"Claude 4\.1 Opus System Card", "system card"),
    (r"Claude Opus 4\.5 System Card", "latest system card"),
    (r"Claude Sonnet 4\.5 System Card", "system card"),
    (r"Responsible Scaling Policy", "safety governance framework"),
    (r"Sabotage Risk Report", "agentic risk assessment"),
    # OpenAI — alignment methods + system cards
    (r"instructgpt", "foundational RLHF"),
    (r"learning to summarize", "early RLHF"),
    (r"dpo direct preference", "DPO method"),
    (r"deliberative alignment", "spec-based alignment method"),
    (r"gpt 4 system card", "system card"),
    (r"gpt 4o system card", "system card"),
    (r"gpt 4 5 system card|gpt 4\.5 system card", "system card"),
    (r"o1 system card", "reasoning model system card"),
    (r"o3 and o4 mini system card", "reasoning model system card"),
    (r"gpt 5 system card", "latest system card"),
    (r"gpt 5\.2 system card", "latest system card"),
    (r"gpt oss.*model card", "open-weights safety card"),
    (r"deep research system card", "agentic system card"),
    (r"operator system card", "computer-use agent system card"),
    # Google DeepMind
    (r"Gemini Safety", "safety eval methodology"),
    (r"ShieldGemma", "safety classifier"),
    (r"Gemini 2\.5 Technical Report", "frontier report w/ safety section"),
    (r"Gemini 2\.5 Pro Model Card", "model card"),
    # Meta
    (r"Llama 2 Open Foundation|^Llama 2\b", "RLHF + safety methodology"),
    (r"Llama 3 Herd|^Llama 3\b", "safety + evals section"),
    (r"(?<!Purple )Llama Guard(?! 3)", "safety classifier taxonomy"),
    (r"CyberSecEval 3", "agentic security eval"),
    # NVIDIA — preference data / steerability
    (r"HelpSteer Multi attribute", "multi-attribute preference data"),
    (r"HelpSteer2 Preference", "preference dataset methodology"),
    (r"SteerLM", "attribute-conditioned steering"),
    # Zhipu — alignment + agentic benchmarks
    (r"\bAlignBench", "Chinese alignment benchmark"),
    (r"\bAlignMMBench", "multimodal alignment benchmark"),
    (r"\bAgentBench", "agentic eval methodology"),
    # xAI
    (r"grok 4 model card", "model card"),
    (r"grok 4 1 model card", "model card w/ persona/values"),
    # Others
    (r"Phi 3 Safety", "safety post-training"),
    (r"Qwen3 Technical Report$|Qwen3 Technical Report \d", "non-US frontier safety section"),
    (r"DeepSeek R1", "RL alignment methodology"),
]


# Exact-title exclusions: duplicate copies of reports already kept under
# another title (dedup can't catch these — no arXiv id in stem).
EXCLUDE_TITLES = {
    "constitutional ai harmlessness",          # OpenAI-misfiled copy of Anthropic CAI
    "gpt 4o system card",                      # keep arxiv 2410.21276 copy
    "gpt 4o system card official",
    "gpt 4.5 system card february 2025",       # keep "gpt 4 5 system card"
    "gpt 5 system card august 2025",           # keep arxiv 2601.03267 copy
    "gpt oss model card arxiv",                # keep arxiv 2508.10925 copy
    "gpt oss model card august 2025",
}


def arxiv_key(stem: str):
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?$", stem)
    return m.group(1) if m else None


def norm_title(title: str):
    t = re.sub(r"\d{4}\.\d{4,5}(v\d+)?", "", title)
    t = re.sub(r"(january|february|march|april|may|june|july|august|september|october|november|december)\s+20\d\d", "", t, flags=re.I)
    t = re.sub(r"\b20\d\d\b", "", t)
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t


def main():
    listing = json.loads(LISTING.read_text(encoding="utf-8"))
    selected = {}
    for rep in listing["reports"]:
        title = rep["title"]
        if title.strip().lower() in EXCLUDE_TITLES:
            continue
        for pat, why in PATTERNS:
            if re.search(pat, title, re.I):
                key = arxiv_key(rep["stem"]) or norm_title(title)
                prev = selected.get(key)
                if prev is None or rep["extract_lines"] > prev["extract_lines"]:
                    selected[key] = {**rep, "rationale": why}
                break

    rows = sorted(selected.values(), key=lambda r: (r["company"] or "", r["title"]))
    out = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "curation": "Fable-curated for values-alignment relevance + recency (2026-07-05)",
        "count": len(rows),
        "reports": rows,
    }
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"Shortlist: {OUT} ({len(rows)} reports)")
    for r in rows:
        print(f"  {(r['company'] or '?')[:16]:16} | {r['extract_lines']:5} | {r['title'][:80]}")


if __name__ == "__main__":
    main()
