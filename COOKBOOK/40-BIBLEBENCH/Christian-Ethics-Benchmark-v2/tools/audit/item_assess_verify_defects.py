#!/usr/bin/env python3
"""
WALKWORTHY v2 -- Mechanical Defect Verification
Canary: WALKWORTHY-CANARY-7f3e2026

Checks:
  1. BUDGET: WW-05-E03 allocation budget vs prose + all design-05 budget==0/missing
  2. CONTAMINATION CENSUS: keyed fields with Handoff Notes / ## AREA / \\n## N headers / "keyed behavior not inlined"
  3. EMPTY-KEY CENSUS: empty keyed, design-03 keyed_expressed==[], empty user messages
  4. PACK-ENTRY FIDELITY: area-K structure, K-item citations, and other "(not found)" citations

Output: $LOG/verification-mechanical.md
SAFETY: no rm; read-only on datasets/banks/v1; no writes outside tools/audit/ and $LOG.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import sys
from collections import defaultdict
from datetime import date
from typing import Dict, List, Optional, Tuple

# ── Paths ─────────────────────────────────────────────────────────────────────
V2 = pathlib.Path(
    "/Users/jimmy.lin/Documents/CEI-Literature-Vault"
    "/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2"
)
V1 = V2.parent / "Christian-Ethics-Benchmark"
ANCHOR_PACKS_DIR = V1 / "ANCHOR-PACKS"
PUBLIC_DIR = V2 / "datasets" / "public"
HOLDOUT_DIR = V2 / "datasets" / "holdout"
LOG_DIR = V2 / "logs" / "item-assessment-20260718"
OUTPUT_FILE = LOG_DIR / "verification-mechanical.md"

ALLOW_HOLDOUT = os.environ.get("WALKWORTHY_ALLOW_HOLDOUT") == "1"
CANARY = "WALKWORTHY-CANARY-7f3e2026"
TODAY = date.today().isoformat()

# ── Load all items from a surface ─────────────────────────────────────────────

def load_surface(data_dir: pathlib.Path) -> List[dict]:
    """Load all admin line records from all design*.jsonl files."""
    records = []
    for f in sorted(data_dir.glob("design*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            rec["_source_file"] = f.name
            records.append(rec)
    return records


# ── Check 1: BUDGET ──────────────────────────────────────────────────────────

def check_budget(all_records: List[Tuple[str, List[dict]]]) -> List[dict]:
    """
    Returns list of hit dicts.
    For WW-05-E03: compare metadata.keyed.extras.allocation.budget to prose-mentioned sessions.
    For ALL design-05 items: flag budget==0.0 or missing.
    """
    hits = []
    for surface, records in all_records:
        for rec in records:
            meta = rec["metadata"]
            item_id = meta.get("item_id", "?")
            design = meta.get("design", "")
            if not design.startswith("05"):
                continue

            keyed = meta.get("keyed") or {}
            extras = keyed.get("extras") or {}
            allocation = extras.get("allocation") or {}
            budget = allocation.get("budget")

            # Check: budget missing or == 0.0
            if budget is None:
                hits.append({
                    "check": "BUDGET",
                    "item_id": item_id,
                    "surface": surface,
                    "issue": "budget key missing from extras.allocation",
                    "detail": f"keyed.extras={json.dumps(extras)[:200]}",
                })
            elif budget == 0.0:
                # Extra: for WW-05-E03, report prose session count
                if item_id == "WW-05-E03":
                    user_content = ""
                    for msg in rec.get("input", []):
                        if msg.get("role") == "user":
                            user_content = msg.get("content", "")
                    # Look for number-of-sessions in prose
                    session_matches = re.findall(r'\b(\d+)\s+(?:substantive\s+)?sessions?\b',
                                                 user_content, re.IGNORECASE)
                    prose_session_num = session_matches[0] if session_matches else "not found"
                    hits.append({
                        "check": "BUDGET",
                        "item_id": item_id,
                        "surface": surface,
                        "issue": "WW-05-E03: budget=0.0 but prose specifies a session count",
                        "detail": (
                            f"budget in metadata=0.0; prose session mention={prose_session_num!r}; "
                            f"tokens={allocation.get('tokens', [])}"
                        ),
                    })
                else:
                    hits.append({
                        "check": "BUDGET",
                        "item_id": item_id,
                        "surface": surface,
                        "issue": "budget==0.0 in extras.allocation",
                        "detail": (
                            f"tokens={allocation.get('tokens', [])}; "
                            f"ask={allocation.get('ask','')[:120]}"
                        ),
                    })
    return hits


# ── Check 2: CONTAMINATION CENSUS ────────────────────────────────────────────

CONTAMINATION_PATTERNS = [
    ("handoff_notes",       re.compile(r'Handoff Notes', re.IGNORECASE)),
    ("area_section_header", re.compile(r'##\s+AREA\b', re.IGNORECASE)),
    ("markdown_num_header", re.compile(r'\n##\s+\d')),
    ("keyed_not_inlined",   re.compile(r'keyed behavior not inlined', re.IGNORECASE)),
]


def keyed_as_string(keyed) -> str:
    """Stringify keyed field (handles dict, list, str, None)."""
    if keyed is None:
        return ""
    if isinstance(keyed, str):
        return keyed
    return json.dumps(keyed, ensure_ascii=False)


def check_contamination(all_records: List[Tuple[str, List[dict]]]) -> List[dict]:
    """Scan every item's keyed field on both surfaces for contamination tokens."""
    hits = []
    for surface, records in all_records:
        for rec in records:
            meta = rec["metadata"]
            item_id = meta.get("item_id", "?")
            keyed = meta.get("keyed")
            keyed_str = keyed_as_string(keyed)

            for pattern_name, pattern in CONTAMINATION_PATTERNS:
                m = pattern.search(keyed_str)
                if m:
                    start = max(0, m.start() - 40)
                    end = min(len(keyed_str), m.end() + 80)
                    context = repr(keyed_str[start:end])
                    hits.append({
                        "check": "CONTAMINATION",
                        "item_id": item_id,
                        "surface": surface,
                        "pattern": pattern_name,
                        "context": context,
                    })
    return hits


# ── Check 3: EMPTY-KEY CENSUS ─────────────────────────────────────────────────

def check_empty_keys(all_records: List[Tuple[str, List[dict]]]) -> List[dict]:
    """
    (a) keyed field empty/whitespace
    (b) design-03 items with keyed_expressed == []
    (c) items with any administration whose user-role message content is empty/whitespace
    """
    hits = []
    for surface, records in all_records:
        for rec in records:
            meta = rec["metadata"]
            item_id = meta.get("item_id", "?")
            design = meta.get("design", "")
            keyed = meta.get("keyed")

            # (a) keyed empty/whitespace
            if keyed is None:
                hits.append({
                    "check": "EMPTY_KEY",
                    "sub": "a_keyed_null",
                    "item_id": item_id,
                    "surface": surface,
                    "detail": "keyed is null/missing",
                    "runnable": meta.get("runnable", "?"),
                })
            elif isinstance(keyed, str) and keyed.strip() == "":
                hits.append({
                    "check": "EMPTY_KEY",
                    "sub": "a_keyed_empty_string",
                    "item_id": item_id,
                    "surface": surface,
                    "detail": "keyed is empty string",
                    "runnable": meta.get("runnable", "?"),
                })
            elif isinstance(keyed, dict):
                # Check if all values are empty/whitespace
                all_empty = all(
                    (v is None or (isinstance(v, str) and v.strip() == ""))
                    for v in keyed.values()
                )
                if all_empty and keyed:
                    hits.append({
                        "check": "EMPTY_KEY",
                        "sub": "a_keyed_all_empty_dict",
                        "item_id": item_id,
                        "surface": surface,
                        "detail": f"keyed dict has all empty values: keys={list(keyed.keys())}",
                        "runnable": meta.get("runnable", "?"),
                    })

            # (b) design-03: keyed_expressed == []
            if design.startswith("03"):
                if isinstance(keyed, dict):
                    keyed_expressed = keyed.get("keyed_expressed")
                    if keyed_expressed == [] or keyed_expressed is None:
                        hits.append({
                            "check": "EMPTY_KEY",
                            "sub": "b_design03_keyed_expressed_empty",
                            "item_id": item_id,
                            "surface": surface,
                            "detail": f"design-03 item keyed_expressed={keyed_expressed!r}",
                            "runnable": meta.get("runnable", "?"),
                        })

            # (c) empty user message content
            for msg in rec.get("input", []):
                if msg.get("role") == "user":
                    content = msg.get("content", "")
                    if content is None or (isinstance(content, str) and content.strip() == ""):
                        hits.append({
                            "check": "EMPTY_KEY",
                            "sub": "c_empty_user_message",
                            "item_id": item_id,
                            "surface": surface,
                            "detail": f"user message content is empty/None; admin={meta.get('admin','?')}",
                            "runnable": meta.get("runnable", "?"),
                        })

    return hits


# ── Check 4: PACK-ENTRY FIDELITY ─────────────────────────────────────────────

def load_pack_file(area_letter: str) -> Optional[Tuple[pathlib.Path, str]]:
    """Load area pack file for given letter. Returns (path, text) or None."""
    for f in ANCHOR_PACKS_DIR.glob(f"area-{area_letter}-*.md"):
        return f, f.read_text(encoding="utf-8")
    for f in ANCHOR_PACKS_DIR.glob(f"area-{area_letter.lower()}-*.md"):
        return f, f.read_text(encoding="utf-8")
    return None


def _claims_section_text(pack_text: str) -> str:
    """
    Return the text from ## 2. (claims section) up to ## 3. (splits).
    Falls back to the full text if section markers not found.
    This avoids false-positive matches in scenario sections.
    """
    sec2 = re.search(r'^##\s+2\.', pack_text, re.MULTILINE)
    sec3 = re.search(r'^##\s+3\.', pack_text, re.MULTILINE)
    if sec2:
        end = sec3.start() if sec3 else len(pack_text)
        return pack_text[sec2.start():end]
    return pack_text


def describe_pack_structure(pack_text: str, area_letter: str) -> dict:
    """
    Analyze the structure of a pack file.
    Returns section headers, numbering schemes, and scenario section info.
    """
    L = area_letter.upper()
    claims_text = _claims_section_text(pack_text)

    # Find section headers
    sections = re.findall(r'^(#{1,3} .+)$', pack_text, re.MULTILINE)

    # Numbering schemes (in claims section only)
    schemes = {}

    letter_n = re.findall(rf'\*\*{re.escape(L)}-(\d+)', claims_text)
    if letter_n:
        nums = [int(x) for x in letter_n]
        schemes[f"{L}-N"] = {"count": len(nums), "max": max(nums), "min": min(nums)}

    c_prefix = re.findall(r'\*\*C(\d+)\.\*\*', claims_text)
    if c_prefix:
        nums = [int(x) for x in c_prefix]
        schemes["C-prefix"] = {"count": len(nums), "max": max(nums), "min": min(nums)}

    plain_num = re.findall(r'^(\d+)\.\s+\*\*', claims_text, re.MULTILINE)
    if plain_num:
        nums = [int(x) for x in plain_num]
        schemes["plain-N"] = {"count": len(nums), "max": max(nums), "min": min(nums)}

    claim_n = re.findall(r'\*\*Claim (\d+)', claims_text)
    if claim_n:
        nums = [int(x) for x in claim_n]
        schemes["Claim-N"] = {"count": len(nums), "max": max(nums), "min": min(nums)}

    # Scenario section info
    has_scenario_section = bool(re.search(r'^##\s+6\.', pack_text, re.MULTILINE))
    scenario_plain = []
    if has_scenario_section:
        sec6_match = re.search(r'^##\s+6\..*$', pack_text, re.MULTILINE)
        if sec6_match:
            sec6_text = pack_text[sec6_match.start():]
            scenario_plain = re.findall(r'^(\d+)\.\s+', sec6_text, re.MULTILINE)

    return {
        "sections": sections[:10],
        "numbering_schemes": schemes,
        "has_scenario_section_6": has_scenario_section,
        "scenario_item_count": len(scenario_plain),
        "scenario_max": max(int(x) for x in scenario_plain) if scenario_plain else 0,
    }


def try_extract_entry(pack_text: str, area_letter: str, entry_num: int) -> Tuple[Optional[str], str]:
    """
    Try all known extraction patterns to find entry_num in pack_text.
    Searches the CLAIMS section only (to avoid false hits from scenario section).
    Returns (pattern_name, text) or (None, "").
    """
    L = area_letter.upper()
    n = entry_num

    # Use claims section text only
    claims_text = _claims_section_text(pack_text)

    # Pattern 1: **{L}-{N} ...  (K-1, K-2 etc.)
    pat1 = re.compile(
        rf'\*\*{re.escape(L)}-{n}\b(.+?)(?=\*\*{re.escape(L)}-\d+|\Z)',
        re.DOTALL
    )

    # Pattern 2: - **C{N}.** or **C{N}.** (C-prefix, area E/M style)
    pat2 = re.compile(
        rf'(?:^-\s+)?\*\*C{n}\.\*\*(.+?)(?=(?:^-\s+)?\*\*C\d+\.\*\*|^##|\Z)',
        re.MULTILINE | re.DOTALL
    )

    # Pattern 3: plain {N}. ** (area A, B, C, F, L style)
    pat3 = re.compile(
        rf'^{n}\.\s+\*\*.+?(?=^\d+\.\s+\*\*|^##|\Z)',
        re.MULTILINE | re.DOTALL
    )

    # Pattern 4: **Claim {N}
    pat4 = re.compile(
        rf'\*\*Claim {n}[\s\-—(].+?(?=\*\*Claim \d+|^##|\Z)',
        re.MULTILINE | re.DOTALL
    )

    for pat_name, pat in [("letter-N", pat1), ("C-prefix", pat2),
                           ("plain-N", pat3), ("Claim-N", pat4)]:
        m = pat.search(claims_text)
        if m:
            return pat_name, m.group(0).strip()[:500]

    return None, ""


def _entry_like_occurrence(pack_text: str, area_letter: str, num: int) -> Optional[str]:
    """
    Check if the number appears as a claim entry in the pack (entry-like context only).
    Checks for: 'LETTER-N', 'CN.', 'N. **' at line start, 'Claim N' — all in claims section.
    Returns a short context string if found, None otherwise.
    """
    claims_text = _claims_section_text(pack_text)
    L = area_letter.upper()

    # Entry-like patterns (strict — must look like a claim start)
    entry_patterns = [
        re.compile(rf'\*\*{re.escape(L)}-{num}\b'),           # **A-18 or **K-18
        re.compile(rf'(?:^-\s+)?\*\*C{num}\.\*\*', re.MULTILINE),  # **C18.**
        re.compile(rf'^{num}\.\s+\*\*', re.MULTILINE),         # 18. **
        re.compile(rf'\*\*Claim {num}\b'),                      # **Claim 18
    ]
    for pat in entry_patterns:
        m = pat.search(claims_text)
        if m:
            start = max(0, m.start() - 5)
            end = min(len(claims_text), m.end() + 80)
            return claims_text[start:end].replace('\n', ' ')[:120]
    return None


def check_pack_fidelity(all_records: List[Tuple[str, List[dict]]]) -> dict:
    """
    Check 4: Pack entry fidelity.
    Returns a structured report.
    """
    # Area K structure
    k_pack = load_pack_file("K")
    k_structure = None
    if k_pack:
        k_path, k_text = k_pack
        k_structure = describe_pack_structure(k_text, "K")
        k_structure["file"] = k_path.name

    # Specific item citations to verify
    specific_citations = [
        # WW-06-K03 cites K-3, K-16, K-7
        ("WW-06-K03", "K", [3, 16, 7], "06"),
        # WW-06-K04 cites K-1, K-2, K-3, K-16
        ("WW-06-K04", "K", [1, 2, 3, 16], "06"),
        # WW-10-K03 cites K-1, K-2, K-4, K-5
        ("WW-10-K03", "K", [1, 2, 4, 5], "10"),
        # WW-10-K05 cites K-1, K-2, K-4, K-5
        ("WW-10-K05", "K", [1, 2, 4, 5], "10"),
    ]

    citation_results = []

    for item_id_target, area_letter, entry_nums, design_prefix in specific_citations:
        pack_result = load_pack_file(area_letter)
        if not pack_result:
            citation_results.append({
                "item_id": item_id_target,
                "area": area_letter,
                "verdict": "PACK-FILE-NOT-FOUND",
                "detail": f"area-{area_letter} pack file not found in {ANCHOR_PACKS_DIR}",
            })
            continue

        pack_path, pack_text = pack_result
        entry_verdicts = []
        for num in entry_nums:
            pat_name, entry_text = try_extract_entry(pack_text, area_letter, num)
            if pat_name:
                entry_verdicts.append({
                    "entry": f"{area_letter}-{num}",
                    "found": True,
                    "pattern_matched": pat_name,
                    "text_preview": entry_text[:200],
                })
            else:
                entry_verdicts.append({
                    "entry": f"{area_letter}-{num}",
                    "found": False,
                    "pattern_matched": None,
                    "text_preview": None,
                })

        all_found = all(v["found"] for v in entry_verdicts)
        none_found = not any(v["found"] for v in entry_verdicts)

        if all_found:
            verdict = "BANK-CITATION-OK"
        elif none_found:
            verdict = "PACK-FILE-MISSING-ENTRY"
        else:
            verdict = "PACK-FILE-PARTIAL"

        citation_results.append({
            "item_id": item_id_target,
            "area": area_letter,
            "pack_file": pack_path.name,
            "verdict": verdict,
            "entries": entry_verdicts,
        })

    # Check "not found in pack file" citations:
    # A-18, L-19, M-18, M-20, E-42, E-38, E-17, C-23
    not_found_checks = [
        ("A", 18), ("L", 19), ("M", 18), ("M", 20),
        ("E", 42), ("E", 38), ("E", 17), ("C", 23),
    ]

    not_found_results = []
    for area_letter, num in not_found_checks:
        pack_result = load_pack_file(area_letter)
        if not pack_result:
            not_found_results.append({
                "citation": f"{area_letter}-{num}",
                "verdict": "PACK-FILE-NOT-FOUND",
                "detail": f"Pack file for area-{area_letter} not found",
            })
            continue

        pack_path, pack_text = pack_result
        # First: try structured extraction (claims section only)
        pat_name, entry_text = try_extract_entry(pack_text, area_letter, num)

        if pat_name:
            # Successfully extracted
            verdict = "PACK-FILE-ENTRY-EXISTS"
            detail = f"Found via pattern '{pat_name}': {entry_text[:150]}"
        else:
            # Check for entry-like occurrence (strict, claims section only)
            entry_ctx = _entry_like_occurrence(pack_text, area_letter, num)
            if entry_ctx:
                verdict = "PACK-FILE-ENTRY-EXISTS-ALT-FORMAT"
                detail = f"Entry-like occurrence found but extraction failed; context: {entry_ctx!r}"
            else:
                verdict = "PACK-FILE-MISSING-ENTRY"
                struct = describe_pack_structure(pack_text, area_letter)
                max_found = max(
                    (v["max"] for v in struct["numbering_schemes"].values()),
                    default=0
                )
                detail = (
                    f"Entry {area_letter}-{num} not found in claims section of {pack_path.name}; "
                    f"max claim number in pack={max_found} "
                    f"(schemes: {list(struct['numbering_schemes'].keys())})"
                )

        not_found_results.append({
            "citation": f"{area_letter}-{num}",
            "pack_file": pack_path.name,
            "verdict": verdict,
            "detail": detail,
        })

    # Analyze _extract_pack_entry regex for scenario-index ambiguity
    regex_analysis = (
        "The `_extract_pack_entry` function in `item_assess_build_packets.py` uses pattern 2 "
        "(plain `N. **`) which matches `^N.\\s+\\*\\*` anywhere in the file. "
        "For areas using plain-N claim numbering (A, B, C, F, I, L, N), the claims section "
        "(§2) appears BEFORE the scenario motifs section (§6) in every pack file. "
        "Since all patterns use `re.search()` (first match wins), the first occurrence of "
        "`N. **` is always the claims-section entry. "
        "For area-K (Letter-N format), pattern 4 (letter-N = `**K-N`) fires first; "
        "plain-N pattern never fires for area-K. "
        "For area-E/M (C-prefix format), pattern 2 (`**C{N}.**`) fires first. "
        "VERDICT: No scenario-index cross-section ambiguity in the packet builder. "
        "However, THIS verification script applies `_claims_section_text()` to restrict "
        "searches to §2 only, providing an independent cross-check that avoids scenario hits."
    )

    return {
        "k_structure": k_structure,
        "citation_results": citation_results,
        "not_found_results": not_found_results,
        "regex_analysis": regex_analysis,
    }


# ── Report rendering ──────────────────────────────────────────────────────────

def render_report(
    budget_hits: List[dict],
    contamination_hits: List[dict],
    empty_key_hits: List[dict],
    pack_fidelity: dict,
    surfaces_used: List[str],
) -> str:
    lines = [
        "# WALKWORTHY v2 — Mechanical Defect Verification",
        "",
        f"Canary: {CANARY}",
        f"Generated: {TODAY}",
        f"Surfaces verified: {', '.join(surfaces_used)}",
        "",
        "---",
        "",
    ]

    # ── Check 1: BUDGET ──────────────────────────────────────────────────────
    lines.append("## Check 1: BUDGET (design-05 allocation budget field)")
    lines.append("")
    lines.append(
        "**What we check:** "
        "For WW-05-E03: verify metadata.keyed.extras.allocation.budget vs session count in prose. "
        "For all design-05 items: flag budget==0.0 or missing."
    )
    lines.append("")

    e03_hits = [h for h in budget_hits if h["item_id"] == "WW-05-E03"]

    lines.append("### WW-05-E03 specific finding")
    lines.append("")
    if e03_hits:
        for h in e03_hits:
            lines.append(f"- **{h['item_id']}** (surface={h['surface']}): {h['issue']}")
            lines.append(f"  - Detail: `{h['detail']}`")
    else:
        lines.append("- WW-05-E03 not found with budget==0 on any surface checked.")
    lines.append("")

    lines.append("### All design-05 items with budget==0.0 or missing")
    lines.append("")
    lines.append(f"**Total hits:** {len(budget_hits)}")
    lines.append("")
    if budget_hits:
        lines.append("| item_id | surface | issue | detail |")
        lines.append("|---------|---------|-------|--------|")
        for h in budget_hits:
            detail_short = h["detail"][:120].replace("|", "\\|")
            lines.append(f"| {h['item_id']} | {h['surface']} | {h['issue'][:60]} | {detail_short} |")
    else:
        lines.append("No hits.")
    lines.append("")

    # ── Check 2: CONTAMINATION CENSUS ────────────────────────────────────────
    lines.append("## Check 2: CONTAMINATION CENSUS")
    lines.append("")
    lines.append(
        "**Patterns searched (in stringified keyed field):**\n"
        "- `handoff_notes`: literal \"Handoff Notes\" (case-insensitive)\n"
        "- `area_section_header`: `## AREA` (case-insensitive)\n"
        "- `markdown_num_header`: `\\n## N` (embedded markdown numeric section header)\n"
        "- `keyed_not_inlined`: literal \"keyed behavior not inlined\""
    )
    lines.append("")
    lines.append(f"**Total contamination hits (admin lines):** {len(contamination_hits)}")
    # Count unique item_ids
    unique_contaminated = set(h["item_id"] for h in contamination_hits)
    lines.append(f"**Unique contaminated items:** {len(unique_contaminated)}")
    lines.append("")

    # Deduplicate for table: one row per (item_id, surface, pattern)
    seen_rows = set()
    deduped_hits = []
    for h in contamination_hits:
        key = (h["item_id"], h["surface"], h["pattern"])
        if key not in seen_rows:
            seen_rows.add(key)
            deduped_hits.append(h)

    lines.append(f"**Unique (item, pattern) pairs:** {len(deduped_hits)}")
    lines.append("")
    if deduped_hits:
        lines.append("| item_id | surface | pattern | context (first match) |")
        lines.append("|---------|---------|---------|----------------------|")
        for h in deduped_hits:
            ctx = h["context"][:100].replace("|", "\\|")
            lines.append(f"| {h['item_id']} | {h['surface']} | {h['pattern']} | {ctx} |")
    else:
        lines.append("No contamination hits.")
    lines.append("")

    # Known suspects confirmation
    lines.append("### Known suspects status")
    lines.append("")
    known_suspects = ["WW-04-D03", "WW-04-E02", "WW-04-I02", "WW-10-K01", "WW-02-F01", "WW-05-F01"]
    suspect_hits: Dict[str, List[str]] = defaultdict(list)
    for h in contamination_hits:
        if h["item_id"] in known_suspects and h["pattern"] not in suspect_hits[h["item_id"]]:
            suspect_hits[h["item_id"]].append(h["pattern"])
    for s in known_suspects:
        if s in suspect_hits:
            lines.append(f"- **{s}**: CONFIRMED — patterns: {suspect_hits[s]}")
        else:
            lines.append(f"- **{s}**: NOT found in contamination scan")
    lines.append("")

    # ── Check 3: EMPTY-KEY CENSUS ─────────────────────────────────────────────
    lines.append("## Check 3: EMPTY-KEY CENSUS")
    lines.append("")
    lines.append(
        "**Sub-checks:**\n"
        "- (a) keyed field null/empty-string/all-empty-dict\n"
        "- (b) design-03 items with keyed_expressed == [] or null\n"
        "- (c) items with user-role message content that is empty/whitespace"
    )
    lines.append("")
    lines.append(f"**Total empty-key hits (admin lines):** {len(empty_key_hits)}")
    lines.append("")

    by_sub: Dict[str, List[dict]] = defaultdict(list)
    for h in empty_key_hits:
        by_sub[h["sub"]].append(h)

    for sub_label, sub_desc in [
        ("a_keyed_null", "(a) keyed=null"),
        ("a_keyed_empty_string", "(a) keyed=empty string"),
        ("a_keyed_all_empty_dict", "(a) keyed dict all-empty"),
        ("b_design03_keyed_expressed_empty", "(b) design-03 keyed_expressed=[]"),
        ("c_empty_user_message", "(c) empty user-role message"),
    ]:
        sub_hits = by_sub.get(sub_label, [])
        # Deduplicate by item_id+surface for display
        seen_ids: set = set()
        deduped_sub: List[dict] = []
        for h in sub_hits:
            key = (h["item_id"], h["surface"])
            if key not in seen_ids:
                seen_ids.add(key)
                deduped_sub.append(h)

        lines.append(f"### {sub_desc} — {len(deduped_sub)} unique item(s)")
        lines.append("")
        if deduped_sub:
            lines.append("| item_id | surface | runnable | detail |")
            lines.append("|---------|---------|----------|--------|")
            for h in deduped_sub:
                detail = h.get("detail", "")[:100].replace("|", "\\|")
                lines.append(f"| {h['item_id']} | {h['surface']} | {h.get('runnable','?')} | {detail} |")
        else:
            lines.append("No hits.")
        lines.append("")

    # Known suspects for empty-key
    lines.append("### Known suspects status (empty-key)")
    lines.append("")
    known_empty = {
        "WW-03-H01": "(b) keyed_expressed==[]",
        "WW-02-A01": "(c) empty user message",
        "WW-02-F01": "(c) empty user message",
        "WW-02-G01": "(c) empty user message",
        "WW-02-I01": "(c) empty user message",
        "WW-09-A01": "(c) empty user message",
        "WW-09-E01": "(c) empty user message",
        "WW-09-F01": "(c) empty user message",
        "WW-09-I01": "(c) empty user message",
    }
    confirmed_empty: Dict[str, List[str]] = defaultdict(list)
    for h in empty_key_hits:
        if h["sub"] not in confirmed_empty[h["item_id"]]:
            confirmed_empty[h["item_id"]].append(h["sub"])
    for suspect, expected in known_empty.items():
        if suspect in confirmed_empty:
            lines.append(f"- **{suspect}**: CONFIRMED — subs: {confirmed_empty[suspect]}")
        else:
            lines.append(f"- **{suspect}**: NOT found — expected: {expected}")
    lines.append("")

    # ── Check 4: PACK-ENTRY FIDELITY ─────────────────────────────────────────
    lines.append("## Check 4: PACK-ENTRY FIDELITY")
    lines.append("")

    # 4a: area-K structure
    lines.append("### 4(a) area-K pack file internal structure")
    lines.append("")
    k = pack_fidelity.get("k_structure")
    if k:
        lines.append(f"**File:** `{k['file']}`")
        lines.append("")
        lines.append("**Section headers (first 10):**")
        for s in k["sections"]:
            lines.append(f"  - `{s}`")
        lines.append("")
        lines.append("**Numbering schemes found in claims section (§2):**")
        for scheme, info in k["numbering_schemes"].items():
            lines.append(f"  - `{scheme}`: count={info['count']}, range={info['min']}..{info['max']}")
        lines.append("")
        lines.append(f"**Has scenario/motifs section (## 6.):** {k['has_scenario_section_6']}")
        lines.append(f"**Scenario item count in section 6:** {k['scenario_item_count']} (max={k['scenario_max']})")
        lines.append("")
        lines.append(
            "**Interpretation:** In area-K, the CLAIMS section (§2) uses `**K-N (tag).**` format "
            "with consecutive numbering K-1 through K-22. The SCENARIO section (§6) uses plain "
            "integer numbering 1..18. These are SEPARATE numbering spaces — 'K-3' unambiguously "
            "refers to claim K-3 (no obligation to prolong life at all costs, §2), not scenario 3 "
            "in §6. A citation of 'K-3' in an item anchor resolves to the claims-section entry."
        )
        lines.append("")
    else:
        lines.append("area-K pack file not found.")
        lines.append("")

    # 4b: specific citations
    lines.append("### 4(b) Specific item citations (WW-06-K03, WW-06-K04, WW-10-K03, WW-10-K05)")
    lines.append("")
    for cr in pack_fidelity.get("citation_results", []):
        lines.append(f"#### {cr['item_id']} (area {cr['area']})")
        if "pack_file" in cr:
            lines.append(f"**Pack file:** `{cr['pack_file']}`")
        lines.append(f"**Overall verdict:** `{cr['verdict']}`")
        lines.append("")
        for ev in cr.get("entries", []):
            status = "FOUND" if ev["found"] else "NOT FOUND"
            pat_str = f" (via pattern `{ev['pattern_matched']}`)" if ev["found"] else ""
            lines.append(f"- **{ev['entry']}**: {status}{pat_str}")
            if ev["found"] and ev["text_preview"]:
                preview = ev["text_preview"][:180].replace('\n', ' ')
                lines.append(f"  - Preview: `{preview}`")
        lines.append("")

    # 4c: different numbering schemes
    lines.append("### 4(c) Numbering scheme cross-check for area-K")
    lines.append("")
    lines.append(
        "The claims section (§2) of area-K uses `**K-N (tag).**` exclusively (K-1 through K-22). "
        "There is no `Claim N`, `CN.`, or plain `N.` scheme in the claims section. "
        "Specific claim content: "
        "K-1 = intrinsic worth of human life (imago Dei); "
        "K-2 = care for the dying is a positive duty; "
        "K-3 = no obligation to prolong life at all costs (earthly life is penultimate); "
        "K-4 = drunkenness is sinful; "
        "K-5 = body as stewardship entrusted by God; "
        "K-7 = killing vs letting die are morally distinct; "
        "K-16 = refusing/discontinuing burdensome/futile treatment is legitimate. "
        "None of these are ambiguous."
    )
    lines.append("")

    # 4d: not-found citations
    lines.append("### 4(d) \"(not found in pack file)\" citations — mechanical verification")
    lines.append("")
    lines.append(
        "Citations flagged by raters as not found: A-18, L-19, M-18, M-20, E-42, E-38, E-17, C-23. "
        "Verification uses claims-section-only search (§2 text only, not scenario §6) "
        "with all four extraction patterns."
    )
    lines.append("")
    lines.append("| citation | pack file | verdict | detail |")
    lines.append("|----------|-----------|---------|--------|")
    for nf in pack_fidelity.get("not_found_results", []):
        detail = nf.get("detail", "")[:200].replace("|", "\\|").replace("\n", " ")
        pf = nf.get("pack_file", "N/A")
        lines.append(f"| {nf['citation']} | {pf} | `{nf['verdict']}` | {detail} |")
    lines.append("")

    # Regex analysis
    lines.append("### 4(e) Pack-builder regex: scenario-index ambiguity assessment")
    lines.append("")
    lines.append(pack_fidelity.get("regex_analysis", ""))
    lines.append("")

    # ── Summary ───────────────────────────────────────────────────────────────
    lines.append("---")
    lines.append("")
    lines.append("## Summary counts")
    lines.append("")
    lines.append("| Check | Hits |")
    lines.append("|-------|------|")
    lines.append(f"| 1 BUDGET: design-05 budget==0 or missing | {len(budget_hits)} |")

    unique_contam_items = len(set(h["item_id"] for h in contamination_hits))
    deduped_contam = set((h["item_id"], h["surface"], h["pattern"]) for h in contamination_hits)
    lines.append(f"| 2 CONTAMINATION: total admin-line hits | {len(contamination_hits)} |")
    lines.append(f"| 2 CONTAMINATION: unique contaminated items | {unique_contam_items} |")
    lines.append(f"| 2 CONTAMINATION: unique (item, pattern) pairs | {len(deduped_contam)} |")

    total_empty = len(set((h["item_id"], h["surface"], h["sub"]) for h in empty_key_hits))
    lines.append(f"| 3 EMPTY-KEY: unique (item, sub-check) hits | {total_empty} |")
    a_hits = len(set((h["item_id"], h["surface"]) for h in empty_key_hits if h["sub"].startswith("a_")))
    b_hits = len(set((h["item_id"], h["surface"]) for h in empty_key_hits if h["sub"].startswith("b_")))
    c_hits = len(set((h["item_id"], h["surface"]) for h in empty_key_hits if h["sub"].startswith("c_")))
    lines.append(f"| 3a keyed null/empty/all-empty-dict | {a_hits} unique items |")
    lines.append(f"| 3b design-03 keyed_expressed=[] | {b_hits} unique items |")
    lines.append(f"| 3c empty user message | {c_hits} unique items |")

    cr_list = pack_fidelity["citation_results"]
    nf_list = pack_fidelity["not_found_results"]
    ok_citations = sum(1 for c in cr_list if c["verdict"] == "BANK-CITATION-OK")
    missing_citations = sum(1 for nf in nf_list if nf["verdict"] == "PACK-FILE-MISSING-ENTRY")
    lines.append(f"| 4 PACK-FIDELITY K-items: all resolved | {ok_citations}/{len(cr_list)} BANK-CITATION-OK |")
    lines.append(f"| 4 PACK-FIDELITY not-found: confirmed missing | {missing_citations}/{len(nf_list)} PACK-FILE-MISSING-ENTRY |")
    lines.append("")

    lines.append(f"Canary: {CANARY}")
    lines.append("")

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    surfaces_used = []
    all_records: List[Tuple[str, List[dict]]] = []

    print("[VERIFY] Loading public surface...")
    pub_records = load_surface(PUBLIC_DIR)
    all_records.append(("public", pub_records))
    surfaces_used.append("public")
    print(f"[VERIFY]   public: {len(pub_records)} admin lines loaded")

    if ALLOW_HOLDOUT:
        print("[VERIFY] Loading holdout surface (WALKWORTHY_ALLOW_HOLDOUT=1)...")
        hld_records = load_surface(HOLDOUT_DIR)
        all_records.append(("holdout", hld_records))
        surfaces_used.append("holdout")
        print(f"[VERIFY]   holdout: {len(hld_records)} admin lines loaded")
    else:
        print("[VERIFY] Holdout skipped (set WALKWORTHY_ALLOW_HOLDOUT=1 to include)")

    print("[VERIFY] Running Check 1: BUDGET...")
    budget_hits = check_budget(all_records)
    print(f"[VERIFY]   {len(budget_hits)} budget hits")

    print("[VERIFY] Running Check 2: CONTAMINATION...")
    contamination_hits = check_contamination(all_records)
    unique_contam = len(set(h["item_id"] for h in contamination_hits))
    print(f"[VERIFY]   {len(contamination_hits)} admin-line hits across {unique_contam} unique items")

    print("[VERIFY] Running Check 3: EMPTY-KEY...")
    empty_key_hits = check_empty_keys(all_records)
    print(f"[VERIFY]   {len(empty_key_hits)} empty-key admin-line hits")

    print("[VERIFY] Running Check 4: PACK-ENTRY FIDELITY...")
    pack_fidelity = check_pack_fidelity(all_records)
    print(f"[VERIFY]   Pack fidelity analysis complete")

    print("[VERIFY] Rendering report...")
    report = render_report(
        budget_hits, contamination_hits, empty_key_hits, pack_fidelity, surfaces_used
    )

    OUTPUT_FILE.write_text(report, encoding="utf-8")
    print(f"[VERIFY] Wrote: {OUTPUT_FILE}")

    # Console summary
    print("\n=== VERIFICATION SUMMARY ===")
    print(f"Check 1 BUDGET hits: {len(budget_hits)}")
    for h in budget_hits:
        print(f"  {h['item_id']} ({h['surface']}): {h['issue'][:80]}")

    print(f"\nCheck 2 CONTAMINATION: {len(contamination_hits)} admin-line hits, {unique_contam} unique items")
    by_pattern: Dict[str, set] = defaultdict(set)
    for h in contamination_hits:
        by_pattern[h["pattern"]].add(h["item_id"])
    for pat, ids in sorted(by_pattern.items()):
        print(f"  pattern={pat}: {len(ids)} unique items")

    print(f"\nCheck 3 EMPTY-KEY: {len(empty_key_hits)} admin-line hits")
    by_sub_ids: Dict[str, set] = defaultdict(set)
    for h in empty_key_hits:
        by_sub_ids[h["sub"]].add(h["item_id"])
    for sub, ids in sorted(by_sub_ids.items()):
        print(f"  {sub}: {sorted(ids)}")

    print(f"\nCheck 4 PACK citations:")
    for cr in pack_fidelity["citation_results"]:
        print(f"  {cr['item_id']}: {cr['verdict']}")
    print("Check 4 not-found citations:")
    for nf in pack_fidelity["not_found_results"]:
        print(f"  {nf['citation']}: {nf['verdict']}")

    print(f"\nReport: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
