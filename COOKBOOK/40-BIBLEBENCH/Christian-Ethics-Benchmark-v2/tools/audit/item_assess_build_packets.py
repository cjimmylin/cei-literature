#!/usr/bin/env python3
"""
WALKWORTHY v2 -- Rater Packet Builder  (item-grouped rewrite, v3 with PACK-REF resolution)
Canary: WALKWORTHY-CANARY-7f3e2026

Rating unit = ITEM (metadata.item_id).
All admin lines sharing an item_id are grouped into ONE packet entry.

Writes rater packets (markdown) under:
  logs/item-assessment-20260718/packets/public/
  logs/item-assessment-20260718/packets/holdout/
  logs/item-assessment-20260718/packets/index.json

Batch constraints:
  - <= 12 items per batch  (was 18 -- tightened per spec)
  - <= 85,000 chars per batch file (raised to 100,000 if batch count would exceed 75/surface)
  - Items stay within a single design
  - If one item alone exceeds char cap, keep it as its own batch
    (truncate only anchor excerpts, never item content)
  - Every item on each surface appears in EXACTLY one batch

Assertions:
  - Sum of public items packed  = 355
  - Sum of holdout items packed = 158
  - No duplicate item_ids
  - Admin line total = 575 public / 260 holdout

Outputs:
  packets/public/dNN-bK.md
  packets/holdout/dNN-bK.md
  packets/index.json  (includes canary, per-batch metadata)

UPGRADE 1 (v3): PACK-REF anchor resolution.
  For items whose M2 anchors have resolve_status=PACK-REF, parses entry IDs
  from the anchor text, maps the area letter to the v1 ANCHOR-PACKS file, and
  includes the matched entry text under "Pack entries cited by the key:".
  Falls back to a ~1000-char digest of the pack file if no entry IDs are found.

UPGRADE 2 (v3): Per-design scoring-rubric header injected right after the
  "**This packet:**" line, sourced from walkworthy_inspect/rubrics.py.
"""

from __future__ import annotations

import importlib.util
import json
import os
import pathlib
import re
import sys
from typing import Dict, List, Optional, Tuple

# ── Paths ──────────────────────────────────────────────────────────────────────
V2 = pathlib.Path(
    "/Users/jimmy.lin/Documents/CEI-Literature-Vault"
    "/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2"
)
V1 = V2.parent / "Christian-Ethics-Benchmark"
ANCHOR_PACKS_DIR = V1 / "ANCHOR-PACKS"

OUTPUT_DIR = V2 / "logs" / "item-assessment-20260718"
PACKETS_ROOT = OUTPUT_DIR / "packets"
PACKETS_PUBLIC = PACKETS_ROOT / "public"
PACKETS_HOLDOUT = PACKETS_ROOT / "holdout"
PUBLIC_DIR = V2 / "datasets" / "public"
HOLDOUT_DIR = V2 / "datasets" / "holdout"
RECYCLE_TARGET = V2 / "RECYCLE-BIN" / "20260718-packets-v2-noPackrefs"

M2_PUBLIC = OUTPUT_DIR / "m2-anchors-public.json"
M2_HOLDOUT = OUTPUT_DIR / "m2-anchors-holdout.json"
M2_EXC_PUBLIC = OUTPUT_DIR / "m2-excerpts-public.json"
M2_EXC_HOLDOUT = OUTPUT_DIR / "m2-excerpts-holdout.json"

CANARY = "WALKWORTHY-CANARY-7f3e2026"
ALLOW_HOLDOUT = os.environ.get("WALKWORTHY_ALLOW_HOLDOUT") == "1"

MAX_ITEMS_PER_BATCH = 12
MAX_CHARS_PER_BATCH = 85_000
MAX_CHARS_RAISED = 100_000   # used if batch count would exceed 75 per surface
BATCH_COUNT_THRESHOLD = 75
EXCERPT_TRUNCATE = 1200
PACK_ENTRY_CAP = 800         # chars per pack entry
MAX_PACK_ENTRIES = 6         # max pack entries per anchor
PACK_DIGEST_CAP = 1000       # chars for general digest if no IDs found
RUBRIC_HEADER_CAP = 5000     # chars cap for design rubric section

# Expected totals for assertions
EXPECTED_PUBLIC_ITEMS = 355
EXPECTED_HOLDOUT_ITEMS = 158
EXPECTED_PUBLIC_ADMIN_LINES = 575
EXPECTED_HOLDOUT_ADMIN_LINES = 260

# ── Design construct map ───────────────────────────────────────────────────────
DESIGN_MAP = {
    "01": ("goodsamaritan",
           "costly obedience/truth-telling when the objective incentivizes exploitation "
           "and no one is watching (keyed: full_obedience)"),
    "02": ("twomasters",
           "resistance to multi-turn pressure escalation "
           "(keyed: holding the line; later break = better)"),
    "03": ("quiettongue",
           "say/do alignment: stated principle vs enacted behavior (twin administrations)"),
    "04": ("innerweight",
           "motive-reactive evaluation bias between alpha/beta motive-cue arms "
           "(keyed delta > 0)"),
    "05": ("ordoamoris",
           "ordered-love resource allocation under explicit constraints "
           "(mechanical constraint-satisfaction)"),
    "06": ("crookedpath",
           "dilemma advisory reasoning profile across 7 categories "
           "(frame/facts/principles/alternatives/resolution/remainder/pastoral)"),
    "07": ("seventyseven",
           "comfort-then-truth pastoral arc; terminal state faithful_counsel keyed"),
    "08": ("vocationfork",
           "guardrail retention when request is covert vs overt "
           "(twin administrations; covert protection keyed)"),
    "09": ("doubleedge",
           "cross-seat consistency + floor compliance across seat_A/B/C + arbiter"),
    "10": ("strangergate",
           "deservingness-cue mercy delta between N/U arms (keyed delta ~= 0)"),
}

HEADER_MAP = "\n".join(
    f"  {num} {slug} = {desc}"
    for num, (slug, desc) in DESIGN_MAP.items()
)

# ── UPGRADE 2: Per-design rubric text from rubrics.py ─────────────────────────

def _load_design_rubric_text(design_num: str) -> str:
    """
    Returns the rubric/category definitions for the given design number
    (e.g. '01', '06') from walkworthy_inspect/rubrics.py, capped at
    RUBRIC_HEADER_CAP chars. Returns 'none defined harness-side' if not found.
    """
    rubrics_path = V2 / "walkworthy_inspect" / "rubrics.py"
    if not rubrics_path.exists():
        return "none defined harness-side (rubrics.py not found)"

    # Import DESIGN_RUBRICS; register in sys.modules so dataclass __module__
    # lookup succeeds (Python 3.9 strict __module__ check on dataclasses).
    _MOD_KEY = "_ww_rubrics_cached"
    if _MOD_KEY in sys.modules:
        mod = sys.modules[_MOD_KEY]
    else:
        spec = importlib.util.spec_from_file_location(_MOD_KEY, rubrics_path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[_MOD_KEY] = mod
        spec.loader.exec_module(mod)  # type: ignore[union-attr]

    # Find the key matching this design num (e.g. "01-goodsamaritan")
    slug_entry = DESIGN_MAP.get(design_num, (None, None))
    if slug_entry[0] is None:
        return "none defined harness-side (design not in DESIGN_MAP)"

    slug = slug_entry[0]
    full_key = f"{design_num}-{slug}"

    rubric_obj = mod.DESIGN_RUBRICS.get(full_key)
    if rubric_obj is None:
        # Try lookup by prefix
        for k in mod.DESIGN_RUBRICS:
            if k.startswith(design_num + "-"):
                rubric_obj = mod.DESIGN_RUBRICS[k]
                full_key = k
                break

    if rubric_obj is None:
        return "none defined harness-side"

    # Render the rubric as readable text
    lines = []
    lines.append(f"Design: {full_key}")
    lines.append(f"Unit: {rubric_obj.unit}")
    lines.append(f"Primary metric: {rubric_obj.primary_metric}")
    if rubric_obj.judge_free_primary:
        lines.append("Note: primary metric is judge-free (mechanical scorer)")
    if rubric_obj.reference_anchored:
        lines.append("Note: reference-anchored scoring")
    if rubric_obj.length_correction:
        lines.append("Note: length correction applied")
    if rubric_obj.keyed_fields:
        lines.append(f"Keyed fields surfaced to judge: {', '.join(rubric_obj.keyed_fields)}")
    lines.append("")
    lines.append("Categories:")
    for cat in rubric_obj.categories:
        scale_info = f"scale={cat.scale}, options={cat.options}"
        lines.append(f"  {cat.name} ({scale_info}): {cat.desc}")

    result = "\n".join(lines)
    if len(result) > RUBRIC_HEADER_CAP:
        result = result[:RUBRIC_HEADER_CAP] + "\n[... truncated at 5000 chars]"
    return result


# Cache rubric text per design to avoid repeated file loads
_RUBRIC_CACHE: Dict[str, str] = {}

def get_rubric_text(design_num: str) -> str:
    if design_num not in _RUBRIC_CACHE:
        _RUBRIC_CACHE[design_num] = _load_design_rubric_text(design_num)
    return _RUBRIC_CACHE[design_num]


# ── UPGRADE 1: PACK-REF anchor resolution ─────────────────────────────────────

# Map area letter -> anchor-pack file path (read-only)
_AREA_TO_PACK_FILE: Dict[str, pathlib.Path] = {}

def _build_area_map() -> None:
    """Populate _AREA_TO_PACK_FILE from ANCHOR_PACKS_DIR."""
    for f in ANCHOR_PACKS_DIR.glob("area-*.md"):
        # filename: area-A-truth-telling-speech.md -> letter A
        parts = f.stem.split("-")
        if len(parts) >= 2:
            letter = parts[1].upper()
            _AREA_TO_PACK_FILE[letter] = f

_build_area_map()

# Cache pack file text to avoid re-reading
_PACK_TEXT_CACHE: Dict[str, str] = {}

def _get_pack_text(letter: str) -> Optional[str]:
    if letter not in _AREA_TO_PACK_FILE:
        return None
    if letter not in _PACK_TEXT_CACHE:
        _PACK_TEXT_CACHE[letter] = _AREA_TO_PACK_FILE[letter].read_text()
    return _PACK_TEXT_CACHE[letter]


def _extract_pack_entry(pack_text: str, area_letter: str, entry_num: int) -> str:
    """
    Extract the text of a single numbered claim entry from pack_text.
    Handles multiple formatting conventions:
      - **C{n}.**  (area D, G, M)
      - - **C{n}.**  (area E — bullet prefix)
      - {n}. **   (area A, B, C, F, I, L, N)
      - **Claim {n} —  (area H)
      - **{Letter}-{n}  (area J, K)
    Returns up to PACK_ENTRY_CAP chars, empty string if not found.
    """
    L = area_letter.upper()
    n = entry_num

    # All patterns tried in order; each pattern captures from the entry start
    # to just before the next entry at the same level or a ## header.
    next_entry_guards = [
        r'(?=^(?:-\s+)?\*\*C\d+\.\*\*)',          # C-prefix next entry
        r'(?=^\d+\.\s+\*\*)',                       # num-bold next entry
        r'(?=\*\*Claim \d+\b)',                     # Claim N next entry
        rf'(?=\*\*{re.escape(L)}-\d+\b)',           # Letter-N next entry
        r'(?=^##)',                                  # section header
        r'\Z',                                       # end of file
    ]
    end_guard = '|'.join(next_entry_guards)

    patterns = [
        # **C{n}.** or - **C{n}.**
        re.compile(
            rf'(?:^-\s+)?\*\*C{n}\.\*\*(.+?)(?={end_guard})',
            re.MULTILINE | re.DOTALL
        ),
        # plain num. **...
        re.compile(
            rf'^{n}\.\s+\*\*.+?(?=^\d+\.\s+\*\*|^##|\Z)',
            re.MULTILINE | re.DOTALL
        ),
        # **Claim {n} — or **Claim {n} (
        re.compile(
            rf'\*\*Claim {n}[\s\-—(].+?(?=\*\*Claim \d+|^##|\Z)',
            re.MULTILINE | re.DOTALL
        ),
        # **{L}-{n} ( or **{L}-{n} .
        re.compile(
            rf'\*\*{re.escape(L)}-{n}\b.+?(?=\*\*{re.escape(L)}-\d+|^##|\Z)',
            re.MULTILINE | re.DOTALL
        ),
    ]

    # PE-24 fix (2026-07-24): search the pack BEFORE the scenario-motifs section
    # first. The scenario list uses `1. **(a)** ...` numbering, which the generic
    # num-bold pattern matched ahead of letter-prefixed claims (**K-1 (a).** etc.),
    # so prefix-less citations resolved to scenario stubs instead of claims — the
    # source of the false "wrong pack content" anchor findings in the 2026-07-18
    # sweep (C5 artifact class). Fall back to the full text so packs without the
    # header keep the old behavior.
    scen_m = re.search(r'^##\s*\d+\.\s*Scenario', pack_text, re.MULTILINE)
    search_spaces = [pack_text[:scen_m.start()]] if scen_m else []
    search_spaces.append(pack_text)

    for space in search_spaces:
        for pat in patterns:
            m = pat.search(space)
            if m:
                return m.group(0).strip()[:PACK_ENTRY_CAP]
    return ""


def _parse_entry_ids_from_anchor(anchor_text: str) -> List[Tuple[str, int]]:
    """
    Parse (area_letter, entry_num) pairs from an anchor text string.
    Handles forms like:
      area-B pack 5 · 6
      area-D pack C11 (...)
      Area-A pack claim 3 (...)
      area-F 1/11
      area-I pack 8
      area-E pack C2 + C4
      area-B pack claims 1,8,14
      area-B pack 11 · area-A pack claim 8
    Returns list of unique (letter, num) pairs, preserving order.
    """
    seen = set()
    results = []

    # Find all area-X references and then parse numbers following each
    # Split on '+' and '·' and '/' separators to handle multi-area anchors
    # Strategy: find each "area-X" occurrence and extract the IDs associated with it
    area_occurrences = list(re.finditer(r'[Aa]rea-([A-N])\b', anchor_text))

    for occ_idx, area_m in enumerate(area_occurrences):
        letter = area_m.group(1).upper()
        # Determine the text "owned" by this area reference:
        # from just after "area-X" to just before the next "area-X" or end
        start = area_m.end()
        if occ_idx + 1 < len(area_occurrences):
            end = area_occurrences[occ_idx + 1].start()
        else:
            end = len(anchor_text)
        chunk = anchor_text[start:end]

        # Skip "pack" / "area" / "claims" noise words
        # Now find entry numbers in chunk
        # Patterns: C11, C 11, claim 11, claims 11,12, 11 (, 11/12, 11·12, N-11
        num_patterns = [
            re.compile(r'\bC(\d+)\b'),             # C11, C3
            re.compile(r'\bclaims?\s+(\d+)'),      # claim 3, claims 3
            rf'\b{letter}-(\d+)\b',                # B-5
            re.compile(r'\b(\d+)\s*[·/,\s]'),      # 5·6, 5/11, 5,6
            re.compile(r'\b(\d+)\s*\('),            # 8 (provision...
            re.compile(r'\b(\d+)\s*$'),             # trailing number
            re.compile(r'\b(\d+)\b'),               # any standalone number
        ]
        found_in_chunk = []
        for pat in num_patterns:
            if isinstance(pat, str):
                pat = re.compile(pat)
            for m in pat.finditer(chunk):
                n = int(m.group(1))
                if 1 <= n <= 50:  # sanity range for claim numbers
                    key = (letter, n)
                    if key not in seen:
                        seen.add(key)
                        found_in_chunk.append(key)
        results.extend(found_in_chunk)

    return results


def resolve_pack_ref_anchors(
    anchor_text: str,
    item_id: str,
    target_text: str,
    keyed_text: str,
) -> str:
    """
    Given an anchor string with resolve_status=PACK-REF, returns a formatted
    section of pack entry excerpts to include under the Anchors section.

    Steps:
    (a) Parse entry IDs from anchor_text (and also target_text + keyed_text
        as fallback per spec).
    (b) Map area letter to pack file.
    (c) Extract each entry's text from the pack file (up to PACK_ENTRY_CAP each,
        max MAX_PACK_ENTRIES per anchor).
    (d) If no entry IDs found, include first ~PACK_DIGEST_CAP chars of the pack
        file as a general digest.

    Returns a markdown string suitable for inclusion in the anchor section.
    """
    # Parse from anchor text first
    entry_ids = _parse_entry_ids_from_anchor(anchor_text)

    # If still empty, try parsing from target + keyed combined text
    if not entry_ids:
        combined = (target_text or "") + " " + (keyed_text or "")
        entry_ids = _parse_entry_ids_from_anchor(combined)

    if not entry_ids:
        # No entry IDs found — produce general digests for referenced areas
        area_letters = list(set(
            m.group(1).upper()
            for m in re.finditer(r'[Aa]rea-([A-N])\b', anchor_text)
        ))
        if not area_letters:
            return "*Pack-entry resolution: no area letters found in anchor text.*"

        parts = []
        for letter in sorted(area_letters):
            pack_text = _get_pack_text(letter)
            if pack_text is None:
                parts.append(f"*(area-{letter} pack file not found)*")
                continue
            pack_file_name = _AREA_TO_PACK_FILE[letter].name
            digest = pack_text[:PACK_DIGEST_CAP]
            parts.append(
                f"**General digest from `{pack_file_name}` (first ~{PACK_DIGEST_CAP} chars):**\n\n"
                f"```\n{digest}\n```"
            )
        return "\n\n".join(parts)

    # We have entry IDs — group by area letter and extract
    # Cap at MAX_PACK_ENTRIES total across all areas
    entry_ids = entry_ids[:MAX_PACK_ENTRIES]

    # Group by area letter to show pack file label once per area
    by_letter: Dict[str, List[int]] = {}
    for letter, num in entry_ids:
        by_letter.setdefault(letter, []).append(num)

    parts = []
    for letter in sorted(by_letter.keys()):
        nums = by_letter[letter]
        pack_text = _get_pack_text(letter)
        pack_file_name = (
            _AREA_TO_PACK_FILE[letter].name
            if letter in _AREA_TO_PACK_FILE else f"area-{letter}-?.md"
        )
        if pack_text is None:
            parts.append(f"*(area-{letter} pack file not found — no excerpts)*")
            continue

        entry_parts = []
        for num in nums:
            entry_text = _extract_pack_entry(pack_text, letter, num)
            if entry_text:
                entry_parts.append(f"**Entry {letter}-{num}:**\n{entry_text}")
            else:
                entry_parts.append(f"**Entry {letter}-{num}:** *(not found in pack file)*")

        pack_block = "\n\n".join(entry_parts)
        parts.append(
            f"**Pack entries cited by the key (from `{pack_file_name}`):**\n\n"
            f"{pack_block}"
        )

    return "\n\n".join(parts)


# ── Load M2 data ───────────────────────────────────────────────────────────────
def load_m2(surface: str) -> Tuple[Dict[str, dict], Dict[str, str]]:
    """
    Returns (anchor_by_key, excerpts_by_key).
    anchor_by_key maps anchor_key -> record dict.
    """
    anch_path = M2_PUBLIC if surface == "public" else M2_HOLDOUT
    exc_path = M2_EXC_PUBLIC if surface == "public" else M2_EXC_HOLDOUT

    anch_data = json.loads(anch_path.read_text())
    exc_data = json.loads(exc_path.read_text())

    by_key = {r["anchor_key"]: r for r in anch_data["records"]}
    excerpts = exc_data.get("excerpts", {})
    return by_key, excerpts


# ── Group admin lines by item_id ───────────────────────────────────────────────
def group_by_item(
    data_dir: pathlib.Path,
) -> Tuple[Dict[str, List[dict]], Dict[str, List[str]], int]:
    """
    Returns:
      design_items  : dnum -> ordered list of (item_id, [admin_line, ...])
                      Each element is a tuple (item_id, admins_list).
      item_order    : dnum -> [item_id, ...] in JSONL order (first appearance)
      total_admin_lines: int
    """
    design_item_admins: Dict[str, Dict[str, List[dict]]] = {}
    design_item_order: Dict[str, List[str]] = {}
    total_admin_lines = 0

    for f in sorted(data_dir.glob("design*.jsonl")):
        dnum = f.stem.replace("design", "")
        item_admins: Dict[str, List[dict]] = {}
        item_order: List[str] = []

        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            total_admin_lines += 1
            record = json.loads(line)
            item_id = record["metadata"]["item_id"]
            if item_id not in item_admins:
                item_admins[item_id] = []
                item_order.append(item_id)
            item_admins[item_id].append(record)

        design_item_admins[dnum] = item_admins
        design_item_order[dnum] = item_order

    return design_item_admins, design_item_order, total_admin_lines


# ── Format one ITEM (all its admins grouped) ──────────────────────────────────
def format_item_grouped(
    item_id: str,
    admins: List[dict],
    m2_by_key: Dict[str, dict],
    excerpts: Dict[str, str],
) -> str:
    """
    Renders one item with:
      - Header: item_id + stratum/area/tier/difficulty + runnable flags
      - Each administration in sequence: admin label, messages, target, keyed JSON,
        multiturn ladder if present
      - Shared anchors + M2 status + excerpts (once, from first admin)
      - For PACK-REF anchors: resolved pack entry excerpts inline
    """
    # Pull header fields from the first admin line
    first = admins[0]
    meta0 = first["metadata"]

    design = meta0.get("design", "?")
    stratum = meta0.get("stratum", "?")
    area = meta0.get("area", "?")
    tier = meta0.get("tier", "?")
    difficulty = meta0.get("difficulty", "?")
    runnable = meta0.get("runnable", "?")
    review_status = meta0.get("review_status", "?")

    lines: List[str] = []
    lines.append(f"### {item_id}")
    lines.append("")
    lines.append(
        f"**Design:** {design} | "
        f"**Stratum:** {stratum} | **Area:** {area} | "
        f"**Tier:** {tier} | **Difficulty:** {difficulty} | "
        f"**Runnable:** {runnable} | **Review:** {review_status}"
    )
    lines.append("")
    lines.append(f"*Admin count: {len(admins)} ({', '.join(a['metadata'].get('admin','?') for a in admins)})*")
    lines.append("")

    # Collect all target + keyed text from all admins for PACK-REF fallback
    all_target_text = " ".join(a.get("target", "") for a in admins)
    all_keyed_text = " ".join(
        json.dumps(a["metadata"].get("keyed", {}), ensure_ascii=False)
        for a in admins
        if a["metadata"].get("keyed")
    )

    # ── Each administration in order ──────────────────────────────────────────
    for adm_rec in admins:
        meta = adm_rec["metadata"]
        admin_label = meta.get("admin", "base")

        lines.append(f"#### Administration: `{admin_label}`")
        lines.append("")

        input_msgs = adm_rec.get("input", [])
        for msg in input_msgs:
            role = msg.get("role", "?").upper()
            content = msg.get("content", "")
            lines.append(f"**[{role}]** {content}")
            lines.append("")

        # Multiturn ladder / branch_table
        mt = meta.get("multiturn")
        if mt and isinstance(mt, dict):
            turns = mt.get("turns", [])
            if turns:
                lines.append("##### Multiturn Ladder")
                lines.append("")
                for turn in turns:
                    idx = turn.get("index", "?")
                    text = turn.get("text")
                    branches = turn.get("branches")
                    if text:
                        lines.append(f"**Turn {idx} [USER]:** {text}")
                        lines.append("")
                    if branches:
                        lines.append(f"**Turn {idx} branches:**")
                        for branch_name, branch_text in branches.items():
                            lines.append(f"- *{branch_name}:* {branch_text}")
                        lines.append("")

        # Target
        lines.append("##### Target")
        lines.append("")
        target = adm_rec.get("target", "")
        lines.append(target)
        lines.append("")

        # Keyed JSON
        keyed = meta.get("keyed")
        if keyed:
            lines.append("##### Keyed")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(keyed, indent=2, ensure_ascii=False))
            lines.append("```")
            lines.append("")

    # ── Shared anchors (once per item, from first admin) ──────────────────────
    anchors = meta0.get("anchors", [])
    if anchors:
        lines.append("#### Anchors (M2 status) — shared across all admins")
        lines.append("")
        for anchor in anchors:
            anchor_key = f"{item_id}||{anchor}"
            rec = m2_by_key.get(anchor_key)
            if rec:
                resolve = rec.get("resolve_status", "?")
                loc = rec.get("loc_status", "?")
                book = rec.get("book_file") or "—"
                locator = rec.get("locator") or "—"
                status_line = (
                    f"**Anchor:** {anchor}  \n"
                    f"*Resolve:* {resolve} | *Loc:* {loc} | "
                    f"*Book:* `{book}` | *Locator:* `{locator}`"
                )
                is_pack_ref = (resolve == "PACK-REF")
            else:
                status_line = f"**Anchor:** {anchor}  \n*M2 record: NOT FOUND*"
                is_pack_ref = False
            lines.append(status_line)
            lines.append("")

            # PACK-REF: resolve pack entries
            if is_pack_ref:
                pack_resolution = resolve_pack_ref_anchors(
                    anchor_text=anchor,
                    item_id=item_id,
                    target_text=all_target_text,
                    keyed_text=all_keyed_text,
                )
                lines.append(pack_resolution)
                lines.append("")

            # Excerpt (truncated) — only for non-PACK-REF
            if not is_pack_ref:
                exc = excerpts.get(anchor_key, "")
                if exc:
                    exc_truncated = exc[:EXCERPT_TRUNCATE]
                    lines.append("<details><summary>Corpus excerpt</summary>")
                    lines.append("")
                    lines.append("```")
                    lines.append(exc_truncated)
                    lines.append("```")
                    lines.append("")
                    lines.append("</details>")
                    lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


# ── Build packets for one surface ─────────────────────────────────────────────
def build_packets(
    surface: str,
    data_dir: pathlib.Path,
    out_dir: pathlib.Path,
    char_cap: int,
) -> Tuple[List[dict], int, int]:
    """
    Returns (index_entries, total_unique_items, total_admin_lines).
    char_cap: effective character cap per batch for this surface.
    """
    print(f"\n[PKT] Building packets for surface: {surface} (char_cap={char_cap:,})")
    out_dir.mkdir(parents=True, exist_ok=True)

    m2_by_key, excerpts = load_m2(surface)

    design_item_admins, design_item_order, total_admin_lines = group_by_item(data_dir)

    # Count unique items across all designs
    all_item_ids: List[str] = []
    for dnum in sorted(design_item_order.keys()):
        all_item_ids.extend(design_item_order[dnum])
    total_unique_items = len(all_item_ids)

    print(f"[PKT]   {total_admin_lines} admin lines -> {total_unique_items} unique items across {len(design_item_order)} designs")

    index_entries: List[dict] = []
    packed_item_ids: set = set()
    packed_admin_count = 0

    for dnum in sorted(design_item_order.keys()):
        slug, desc = DESIGN_MAP.get(dnum, ("unknown", ""))
        item_order = design_item_order[dnum]
        item_admins = design_item_admins[dnum]

        # ── UPGRADE 2: rubric section ──────────────────────────────────────────
        rubric_text = get_rubric_text(dnum)
        rubric_section = (
            f"## Harness scoring rubric for this design (context)\n\n"
            f"```\n{rubric_text}\n```\n\n"
        )

        # Build packet file header (same for all batches in this design)
        pkt_header = (
            f"# WALKWORTHY v2 -- Rater Packet: Design {dnum} ({slug})\n"
            f"Canary: {CANARY}\n"
            f"Surface: {surface}\n\n"
            f"## Construct Map\n"
            f"{HEADER_MAP}\n\n"
            f"**This packet:** Design {dnum} = {slug} -- {desc}\n\n"
            f"{rubric_section}"
            f"---\n\n"
        )

        # Pre-render each item so we can measure chars accurately
        item_texts: List[Tuple[str, str]] = []  # (item_id, rendered_text)
        for item_id in item_order:
            admins = item_admins[item_id]
            rendered = format_item_grouped(item_id, admins, m2_by_key, excerpts)
            item_texts.append((item_id, rendered))

        # Pack items into batches
        # Rule: <= MAX_ITEMS_PER_BATCH AND <= char_cap
        # If a single item alone exceeds char_cap, it gets its own batch
        batches: List[List[Tuple[str, str]]] = []  # list of [(item_id, text), ...]
        current_batch: List[Tuple[str, str]] = []
        current_chars = len(pkt_header)

        for item_id, item_text in item_texts:
            item_chars = len(item_text)

            if current_batch and (
                len(current_batch) >= MAX_ITEMS_PER_BATCH
                or current_chars + item_chars > char_cap
            ):
                batches.append(current_batch)
                current_batch = []
                current_chars = len(pkt_header)

            current_batch.append((item_id, item_text))
            current_chars += item_chars

        if current_batch:
            batches.append(current_batch)

        print(f"[PKT]   d{dnum} ({slug}): {len(item_order)} items ({sum(len(item_admins[iid]) for iid in item_order)} admin lines) -> {len(batches)} batch(es)")

        for b_idx, batch in enumerate(batches, 1):
            fname = f"d{dnum}-b{b_idx}.md"
            fpath = out_dir / fname

            batch_body = pkt_header
            batch_body += f"## Batch {b_idx} of {len(batches)} ({len(batch)} items)\n\n"

            batch_item_ids = []
            for item_id, item_text in batch:
                batch_item_ids.append(item_id)
                batch_body += item_text
                packed_item_ids.add(item_id)
                packed_admin_count += len(item_admins[item_id])

            fpath.write_text(batch_body, encoding="utf-8")
            char_count = len(batch_body)

            entry = {
                "surface": surface,
                "design": dnum,
                "slug": slug,
                "file": str(fpath),
                "batch": b_idx,
                "item_ids": batch_item_ids,
                "item_count": len(batch_item_ids),
                "char_count": char_count,
            }
            index_entries.append(entry)

    # Integrity checks
    all_item_id_set = set(all_item_ids)
    missing = all_item_id_set - packed_item_ids
    extra = packed_item_ids - all_item_id_set
    ok = True
    if missing:
        print(f"[PKT] ERROR: {len(missing)} items NOT packed: {sorted(missing)[:10]}")
        ok = False
    if extra:
        print(f"[PKT] ERROR: {len(extra)} extra item_ids in packets not in dataset")
        ok = False
    if not ok:
        raise RuntimeError(f"Packet integrity failure: missing={len(missing)} extra={len(extra)}")

    print(f"[PKT]   VERIFIED: all {len(all_item_id_set)} unique items packed exactly once")
    print(f"[PKT]   Admin lines covered: {packed_admin_count}")
    return index_entries, total_unique_items, total_admin_lines


# ── Move old packet tree to RECYCLE-BIN ───────────────────────────────────────
def recycle_old_packets() -> None:
    """Move packets/ subtree to RECYCLE-BIN/20260718-packets-v2-noPackrefs/ if it exists."""
    old_path = PACKETS_ROOT
    if not old_path.exists():
        print("[PKT] No existing packet tree to recycle.")
        return

    RECYCLE_TARGET.parent.mkdir(parents=True, exist_ok=True)
    if RECYCLE_TARGET.exists():
        # Already moved in a prior run — don't clobber
        print(f"[PKT] RECYCLE-BIN target already exists, leaving as-is: {RECYCLE_TARGET}")
        return

    import shutil
    shutil.move(str(old_path), str(RECYCLE_TARGET))
    print(f"[PKT] Moved old packets tree -> {RECYCLE_TARGET}")


# ── Determine effective char cap ──────────────────────────────────────────────
def determine_char_cap(surface: str, data_dir: pathlib.Path) -> int:
    """
    Do a quick dry-run item count to determine if we need to raise char cap
    to 100,000 to keep batch count under 75 per surface.
    Returns the effective cap to use.
    """
    # Count total items
    total_items = 0
    for f in sorted(data_dir.glob("design*.jsonl")):
        items_in_design = set()
        for line in f.read_text().splitlines():
            if line.strip():
                rec = json.loads(line)
                items_in_design.add(rec["metadata"]["item_id"])
        total_items += len(items_in_design)

    # Rough estimate: if avg items/batch at default cap would give > 75 batches
    # (conservative: assume avg ~4 items/batch), use raised cap.
    # More accurate: just check if batch count will likely exceed threshold.
    # Since we can't know without rendering, use a simple heuristic:
    # total_items / MAX_ITEMS_PER_BATCH gives min batches needed.
    min_batches = (total_items + MAX_ITEMS_PER_BATCH - 1) // MAX_ITEMS_PER_BATCH
    if min_batches > BATCH_COUNT_THRESHOLD:
        print(f"[PKT]   Estimated min batches ({min_batches}) > {BATCH_COUNT_THRESHOLD} -- raising char cap to {MAX_CHARS_RAISED:,}")
        return MAX_CHARS_RAISED
    return MAX_CHARS_PER_BATCH


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Move old packet tree to recycle bin
    recycle_old_packets()

    # 2. Recreate output dirs
    PACKETS_ROOT.mkdir(parents=True, exist_ok=True)

    all_index: List[dict] = []
    surface_totals: Dict[str, dict] = {}

    # Always build public
    pub_cap = determine_char_cap("public", PUBLIC_DIR)
    entries_pub, items_pub, admin_pub = build_packets("public", PUBLIC_DIR, PACKETS_PUBLIC, pub_cap)
    all_index.extend(entries_pub)
    surface_totals["public"] = {
        "unique_items": items_pub,
        "admin_lines": admin_pub,
    }

    if ALLOW_HOLDOUT:
        hld_cap = determine_char_cap("holdout", HOLDOUT_DIR)
        entries_hld, items_hld, admin_hld = build_packets("holdout", HOLDOUT_DIR, PACKETS_HOLDOUT, hld_cap)
        all_index.extend(entries_hld)
        surface_totals["holdout"] = {
            "unique_items": items_hld,
            "admin_lines": admin_hld,
        }
    else:
        print("\n[PKT] WALKWORTHY_ALLOW_HOLDOUT != 1 -- skipping holdout packets")
        surface_totals["holdout"] = {"unique_items": 0, "admin_lines": 0}

    # 3. Final assertion: expected totals
    pub_items = surface_totals["public"]["unique_items"]
    pub_admin = surface_totals["public"]["admin_lines"]
    hld_items = surface_totals["holdout"]["unique_items"]
    hld_admin = surface_totals["holdout"]["admin_lines"]

    assert pub_items == EXPECTED_PUBLIC_ITEMS, (
        f"Public items: expected {EXPECTED_PUBLIC_ITEMS}, got {pub_items}"
    )
    assert pub_admin == EXPECTED_PUBLIC_ADMIN_LINES, (
        f"Public admin lines: expected {EXPECTED_PUBLIC_ADMIN_LINES}, got {pub_admin}"
    )
    if ALLOW_HOLDOUT:
        assert hld_items == EXPECTED_HOLDOUT_ITEMS, (
            f"Holdout items: expected {EXPECTED_HOLDOUT_ITEMS}, got {hld_items}"
        )
        assert hld_admin == EXPECTED_HOLDOUT_ADMIN_LINES, (
            f"Holdout admin lines: expected {EXPECTED_HOLDOUT_ADMIN_LINES}, got {hld_admin}"
        )

    # 4. Write index.json
    index_path = PACKETS_ROOT / "index.json"
    index_payload = {
        "canary": CANARY,
        "surface_totals": surface_totals,
        "batch_count": len(all_index),
        "batches": all_index,
    }
    index_path.write_text(json.dumps(index_payload, indent=2, ensure_ascii=False))
    print(f"\n[PKT] Wrote index: {index_path}")

    # 5. Summary
    print("\n=== PACKET SUMMARY ===")
    for surface in ["public", "holdout"]:
        entries = [e for e in all_index if e["surface"] == surface]
        totals = surface_totals[surface]
        if not entries:
            print(f"{surface}: SKIPPED")
            continue
        total_batches = len(entries)
        total_packed_items = sum(e["item_count"] for e in entries)
        max_chars = max(e["char_count"] for e in entries)
        by_design = {}
        for e in entries:
            d = e["design"]
            by_design.setdefault(d, 0)
            by_design[d] += 1
        print(f"\n{surface}:")
        print(f"  Unique items:       {totals['unique_items']}")
        print(f"  Admin lines total:  {totals['admin_lines']}")
        print(f"  Total batches:      {total_batches}")
        print(f"  Items packed:       {total_packed_items}")
        print(f"  Max chars/batch:    {max_chars:,}")
        print(f"  Batches per design: {dict(sorted(by_design.items()))}")


if __name__ == "__main__":
    main()
