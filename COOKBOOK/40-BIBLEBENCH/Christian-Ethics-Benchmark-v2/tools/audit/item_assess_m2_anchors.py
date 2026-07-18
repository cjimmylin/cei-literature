#!/usr/bin/env python3
"""
WALKWORTHY v2 -- M2 Corpus-Anchor Verification Script
Canary: WALKWORTHY-CANARY-7f3e2026

Per anchor:
  (a) resolve alias -> book file (RESOLVED / UNRESOLVED)
  (b) locate the quoted locator string in the book text
      (FOUND / FUZZY-FOUND / NOT-FOUND)
  (c) extract ~1500-char context excerpt around the best match

Also:
  - Per-work anchor frequency table (public and holdout separately)
  - Bahnsen usage inventory (item_ids + count)
  - L8 scan: bare Scripture citations as the anchor's work part

Outputs (all to OUTPUT_DIR):
  m2-anchors-public.json
  m2-anchors-holdout.json
  m2-excerpts-public.json
  m2-excerpts-holdout.json
  m2-summary.md
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import unicodedata
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

# ── Paths ──────────────────────────────────────────────────────────────────────
V2 = pathlib.Path(
    "/Users/jimmy.lin/Documents/CEI-Literature-Vault"
    "/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2"
)
BOOKS_DIR = pathlib.Path(
    "/Users/jimmy.lin/Documents/CEI-Literature-Vault"
    "/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Books"
)
OUTPUT_DIR = V2 / "logs" / "item-assessment-20260718"
PUBLIC_DIR = V2 / "datasets" / "public"
HOLDOUT_DIR = V2 / "datasets" / "holdout"

CANARY = "WALKWORTHY-CANARY-7f3e2026"
ALLOW_HOLDOUT = os.environ.get("WALKWORTHY_ALLOW_HOLDOUT") == "1"

# ── Alias -> book-file map ──────────────────────────────────────────────────────
# Built from observed anchor vocabulary. Each alias pattern maps to one book file.
# Unresolved aliases are flagged as defects, not guessed.
ALIAS_MAP: Dict[str, str] = {
    # Geisler & Snuffer -- multiple spellings observed in corpus
    "Geisler & Snuffer": "Love Your Neighbor -- Norman L Geisler, Ryan P Snuffer -- 2007.txt",
    "Geisler-Snuffer": "Love Your Neighbor -- Norman L Geisler, Ryan P Snuffer -- 2007.txt",
    "GEI": "Love Your Neighbor -- Norman L Geisler, Ryan P Snuffer -- 2007.txt",

    # New Dictionary of Christian Ethics & Pastoral Theology
    "New Dictionary": "New Dictionary of Christian Ethics & Pastoral Theology -- Arthur F Holmes, Oliver O'Donovan, David J Atkinson -- 2013.txt",
    "NDCEPT": "New Dictionary of Christian Ethics & Pastoral Theology -- Arthur F Holmes, Oliver O'Donovan, David J Atkinson -- 2013.txt",
    "NDC": "New Dictionary of Christian Ethics & Pastoral Theology -- Arthur F Holmes, Oliver O'Donovan, David J Atkinson -- 2013.txt",
    "NewDict": "New Dictionary of Christian Ethics & Pastoral Theology -- Arthur F Holmes, Oliver O'Donovan, David J Atkinson -- 2013.txt",

    # Rae -- Doing the Right Thing (multiple spelling variants)
    "Rae Doing the Right Thing": "Doing the Right Thing -- Scott Rae, Robert P George, Melissa Moschella.txt",
    "RAE Doing the Right Thing": "Doing the Right Thing -- Scott Rae, Robert P George, Melissa Moschella.txt",
    "Rae-DR": "Doing the Right Thing -- Scott Rae, Robert P George, Melissa Moschella.txt",
    "RAE-DR": "Doing the Right Thing -- Scott Rae, Robert P George, Melissa Moschella.txt",

    # Rae -- Introducing Christian Ethics (multiple spelling variants)
    "Rae-Introducing": "Introducing Christian Ethics -- Scott B Rae -- 2016.txt",
    "Rae Introducing Christian Ethics": "Introducing Christian Ethics -- Scott B Rae -- 2016.txt",
    "Rae-ICE": "Introducing Christian Ethics -- Scott B Rae -- 2016.txt",
    "RAE-ICE": "Introducing Christian Ethics -- Scott B Rae -- 2016.txt",
    "RAE-IC": "Introducing Christian Ethics -- Scott B Rae -- 2016.txt",
    "Rae-IC": "Introducing Christian Ethics -- Scott B Rae -- 2016.txt",

    # Rae -- Moral Choices (multiple spelling variants)
    "Rae Moral Choices": "Moral Choices - An Introduction to Ethics -- Scott B Rae -- 4th ed, 2018.txt",
    "Rae, Moral Choices": "Moral Choices - An Introduction to Ethics -- Scott B Rae -- 4th ed, 2018.txt",
    "RAE-MC": "Moral Choices - An Introduction to Ethics -- Scott B Rae -- 4th ed, 2018.txt",
    "RAE Moral Choices": "Moral Choices - An Introduction to Ethics -- Scott B Rae -- 4th ed, 2018.txt",
    "Rae Moral": "Moral Choices - An Introduction to Ethics -- Scott B Rae -- 4th ed, 2018.txt",
    "Rae, ch.": "Moral Choices - An Introduction to Ethics -- Scott B Rae -- 4th ed, 2018.txt",

    # Frame
    "Frame": "The Doctrine of the Christian Life -- John M Frame -- 2018.txt",
    "FRA": "The Doctrine of the Christian Life -- John M Frame -- 2018.txt",

    # Grudem
    "Grudem": "Christian Ethics -- Wayne Grudem -- revised ed, 2024.txt",
    "GRU": "Christian Ethics -- Wayne Grudem -- revised ed, 2024.txt",

    # Jones
    "Jones": "Biblical Christian Ethics -- David Clyde Jones -- 2012.txt",
    "JON": "Biblical Christian Ethics -- David Clyde Jones -- 2012.txt",

    # Meilaender
    "Meilaender": "Christian Ethics - A Short Companion -- Gilbert Meilaender -- 2024.txt",
    "MEI": "Christian Ethics - A Short Companion -- Gilbert Meilaender -- 2024.txt",

    # Blackwell
    "Blackwell": "The Blackwell Companion to Christian Ethics -- Stanley Hauerwas and Samuel Wells.txt",
    "BLA": "The Blackwell Companion to Christian Ethics -- Stanley Hauerwas and Samuel Wells.txt",

    # Cambridge Companion (also abbreviated CAM)
    "Cambridge": "The Cambridge Companion to Christian Ethics -- Robin Gill -- 2001.txt",
    "CAM": "The Cambridge Companion to Christian Ethics -- Robin Gill -- 2001.txt",

    # O'Donovan
    "O’Donovan": "Common Objects of Love -- Oliver O'Donovan -- 2002.txt",
    "O'Donovan": "Common Objects of Love -- Oliver O'Donovan -- 2002.txt",

    # Powlison
    "Powlison": "Good and Angry -- David Powlison -- 2016.txt",
    "POW": "Good and Angry -- David Powlison -- 2016.txt",

    # Bahnsen -- contrast-only
    "Bahnsen": "Theonomy in Christian Ethics -- Greg L Bahnsen -- 3rd ed, 2002.txt",

    # Wilkens / Four Views (also referenced as Heltzel in Wilkens)
    "Wilkens": "Christian Ethics - Four Views -- Steve Wilkens -- 2017.txt",
    "Heltzel, in Wilkens": "Christian Ethics - Four Views -- Steve Wilkens -- 2017.txt",
}

# Anchors that are structural pack-references with no single book target.
# These begin with "-- area-" (dash-space-area) or are KV-shorthand codes.
# They are marked PACK-REF rather than UNRESOLVED (not defects).
PACK_REF_PREFIXES = (
    "-- area-",
    "- area-",
    "K-",  # shorthand keys K-1, K-2, K-5 etc.
)

# Normalize curly quotes, whitespace, case
def normalize_text(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-")
    s = re.sub(r"\s+", " ", s)
    return s.strip()

# ── Bare Scripture citation pattern (L8) ──────────────────────────────────────
# Matches "Gal. 6:2", "Matt. 5:17", "1 Cor. 4:7", "Genesis 1:1", "Rom 8:28"
SCRIPTURE_RE = re.compile(
    r"^(?:\d\s+)?[A-Z][a-z]+\.?\s+\d+:\d+",
    re.MULTILINE,
)

# ── Load book texts ────────────────────────────────────────────────────────────
print("[M2] Loading book texts...")
BOOK_TEXTS: Dict[str, Tuple[str, str]] = {}  # filename -> (raw_text, norm_text)
for _f in BOOKS_DIR.glob("*.txt"):
    _raw = _f.read_text(encoding="utf-8", errors="replace")
    _norm = normalize_text(_raw)
    BOOK_TEXTS[_f.name] = (_raw, _norm)
print(f"[M2] Loaded {len(BOOK_TEXTS)} books")

# ── Alias resolution ──────────────────────────────────────────────────────────
def is_pack_ref(anchor: str) -> bool:
    """True if anchor is a structural pack-only reference (no single book target).
    Pack-refs are composite multi-book anchors; they are not defects.
    Patterns caught:
      - Starts with "-- area-" or "- area-" or leading dash+area
      - Starts with "area-" (lowercase) directly, containing "pack" or "Split"
      - Starts with "Area-" (capital) -- these are composite claim bundles
      - KV shorthand keys like K-1, K-2, K-5
    """
    stripped = anchor.strip()
    lower = stripped.lower()
    for pfx in PACK_REF_PREFIXES:
        if stripped.startswith(pfx):
            return True
    # Bare "-- area-" or "- area-" with em dash
    if re.match(r"^[-—]\s*area-", stripped):
        return True
    # Direct area-X pack reference (lowercase or capital)
    if re.match(r"^[Aa]rea-[A-Z]", stripped):
        # Any anchor starting with Area-X or area-X is pack-composite
        return True
    return False

def resolve_alias(anchor: str) -> Tuple[Optional[str], str]:
    """
    Returns (book_filename, alias_token_matched).
    Returns (None, "") if unresolved; caller should also check is_pack_ref().
    """
    # Try longest prefix match from ALIAS_MAP
    for alias, book_file in sorted(ALIAS_MAP.items(), key=lambda x: -len(x[0])):
        if anchor.startswith(alias) or (", " + alias) in anchor or anchor == alias:
            if book_file in BOOK_TEXTS:
                return book_file, alias
    # Also try parenthetical content, e.g. "area-F pack claim 6 (Frame, ch. ...)"
    paren_match = re.search(r"\(([^)]+)\)", anchor)
    if paren_match:
        inner = paren_match.group(1)
        for alias, book_file in sorted(ALIAS_MAP.items(), key=lambda x: -len(x[0])):
            if inner.startswith(alias):
                if book_file in BOOK_TEXTS:
                    return book_file, alias
    return None, ""

def extract_locator(anchor: str) -> Optional[str]:
    """
    Extract the quoted chapter/entry title from an anchor string.
    Returns the title string without surrounding quotes, or None.
    """
    # Double-quoted title (curly or straight)
    m = re.search(r'["“]([^"”]{3,})["”]', anchor)
    if m:
        return m.group(1)
    # Single-quoted title (curly or straight)
    m = re.search(r"['‘]([^'’]{3,})['’]", anchor)
    if m:
        return m.group(1)
    # Arrow notation: entry "X" -> "Y"
    arrow_m = re.search(r'[→>]\s*["“]([^"”]+)["”]', anchor)
    if arrow_m:
        return arrow_m.group(1)
    return None

def locate_in_book(
    book_file: str,
    locator: str,
    excerpt_radius: int = 1500,
) -> Tuple[str, int, str]:
    """
    Locate locator in book text.
    Returns (status, offset, excerpt).
    status: FOUND | FUZZY-FOUND | NOT-FOUND
    """
    if book_file not in BOOK_TEXTS:
        return "NOT-FOUND", -1, ""

    raw, norm_book = BOOK_TEXTS[book_file]

    # Exact (normalized) match
    norm_loc = normalize_text(locator)
    idx = norm_book.lower().find(norm_loc.lower())
    if idx >= 0:
        start = max(0, idx - 100)
        end = min(len(raw), idx + excerpt_radius)
        return "FOUND", idx, raw[start:end]

    # Fuzzy: try first significant word (>=5 chars) in the raw text
    words = [w for w in re.split(r"\W+", norm_loc) if len(w) >= 5]
    if words:
        first = words[0].lower()
        pos = raw.lower().find(first)
        if pos >= 0:
            start = max(0, pos - 100)
            end = min(len(raw), pos + excerpt_radius)
            return "FUZZY-FOUND", pos, raw[start:end]

    return "NOT-FOUND", -1, ""

# ── L8 detection ─────────────────────────────────────────────────────────────
def is_bare_scripture(anchor: str) -> bool:
    """
    Return True if anchor starts with a bare Scripture citation (L8 flag).
    Forms like 'Frame, on Gal. 6:2' are legal (mediated by alias).
    """
    for alias in ALIAS_MAP:
        if anchor.startswith(alias):
            return False
    return bool(SCRIPTURE_RE.match(anchor.strip()))

# ── Process one surface ───────────────────────────────────────────────────────
def process_surface(surface: str, data_dir: pathlib.Path) -> dict:
    """Process all design*.jsonl files for one surface."""
    print(f"\n[M2] Processing surface: {surface}")

    all_items: List[dict] = []
    for f in sorted(data_dir.glob("design*.jsonl")):
        for line in f.read_text().splitlines():
            if line.strip():
                all_items.append(json.loads(line))

    print(f"[M2]   {len(all_items)} items loaded")

    anchor_records: List[dict] = []
    excerpts: Dict[str, str] = {}

    work_freq: Dict[str, int] = defaultdict(int)
    bahnsen_items: List[str] = []

    status_counts: Dict[str, int] = defaultdict(int)
    resolve_counts: Dict[str, int] = defaultdict(int)
    l8_flags: List[dict] = []

    for item in all_items:
        item_id = item["metadata"]["item_id"]
        design = item["metadata"]["design"]
        for anchor in item["metadata"].get("anchors", []):
            anchor_key = f"{item_id}||{anchor}"

            # L8 check
            l8 = is_bare_scripture(anchor)
            if l8:
                l8_flags.append({"item_id": item_id, "design": design, "anchor": anchor})

            # Bahnsen inventory
            is_bahnsen = "Bahnsen" in anchor or "bahnsen" in anchor.lower()
            if is_bahnsen:
                bahnsen_items.append(item_id)

            # Pack-ref check (structural multi-book references)
            pack_ref = is_pack_ref(anchor)

            # Resolve alias
            book_file, alias_matched = resolve_alias(anchor)
            if book_file:
                resolve_status = "RESOLVED"
                resolve_counts["RESOLVED"] += 1
                work_freq[book_file] += 1
            elif pack_ref:
                resolve_status = "PACK-REF"
                resolve_counts["PACK-REF"] += 1
            else:
                resolve_status = "UNRESOLVED"
                resolve_counts["UNRESOLVED"] += 1

            # Locate locator in book
            locator = extract_locator(anchor)
            if book_file and locator:
                loc_status, loc_offset, excerpt = locate_in_book(book_file, locator)
            elif book_file and not locator:
                loc_status = "NO-LOCATOR"
                loc_offset = -1
                excerpt = ""
            else:
                loc_status = "NOT-FOUND"
                loc_offset = -1
                excerpt = ""

            status_counts[loc_status] += 1

            if excerpt:
                excerpts[anchor_key] = excerpt[:1500]

            rec = {
                "item_id": item_id,
                "design": design,
                "anchor": anchor,
                "anchor_key": anchor_key,
                "resolve_status": resolve_status,
                "alias_matched": alias_matched,
                "book_file": book_file,
                "locator": locator,
                "loc_status": loc_status,
                "loc_offset": loc_offset,
                "is_l8": l8,
                "is_bahnsen": is_bahnsen,
                "canary": CANARY,
            }
            anchor_records.append(rec)

    return {
        "anchor_records": anchor_records,
        "excerpts": excerpts,
        "work_freq": dict(work_freq),
        "bahnsen_items": list(set(bahnsen_items)),
        "status_counts": dict(status_counts),
        "resolve_counts": dict(resolve_counts),
        "l8_flags": l8_flags,
        "total_items": len(all_items),
    }

# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results: Dict[str, Optional[dict]] = {}

    results["public"] = process_surface("public", PUBLIC_DIR)

    if ALLOW_HOLDOUT:
        results["holdout"] = process_surface("holdout", HOLDOUT_DIR)
    else:
        print("\n[M2] WALKWORTHY_ALLOW_HOLDOUT != 1 -- skipping holdout surface")
        results["holdout"] = None

    # ── Write output files ──────────────────────────────────────────────────
    for surface in ["public", "holdout"]:
        res = results[surface]
        if res is None:
            continue

        anchors_path = OUTPUT_DIR / f"m2-anchors-{surface}.json"
        excerpts_path = OUTPUT_DIR / f"m2-excerpts-{surface}.json"

        payload = {
            "canary": CANARY,
            "surface": surface,
            "total_items": res["total_items"],
            "total_anchor_instances": len(res["anchor_records"]),
            "resolve_counts": res["resolve_counts"],
            "loc_status_counts": res["status_counts"],
            "l8_count": len(res["l8_flags"]),
            "bahnsen_item_count": len(res["bahnsen_items"]),
            "work_frequency": res["work_freq"],
            "l8_flags": res["l8_flags"],
            "bahnsen_items": sorted(res["bahnsen_items"]),
            "records": res["anchor_records"],
        }
        anchors_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
        print(f"[M2] Wrote {anchors_path}")

        exc_payload = {
            "canary": CANARY,
            "surface": surface,
            "count": len(res["excerpts"]),
            "excerpts": res["excerpts"],
        }
        excerpts_path.write_text(json.dumps(exc_payload, indent=2, ensure_ascii=False))
        print(f"[M2] Wrote {excerpts_path}")

    # ── Write summary markdown ──────────────────────────────────────────────
    summary_path = OUTPUT_DIR / "m2-summary.md"
    lines = [
        "# M2 Corpus-Anchor Verification Summary",
        "",
        f"Canary: {CANARY}",
        "Generated: 2026-07-18",
        "",
        "**Note on PACK-REF status:** Anchors beginning with `-- area-X pack` or shorthand",
        "keys (`K-1`, `K-2`) are structural multi-book references with no single target file.",
        "These are not defects -- they are by-design composite anchors.",
        "",
    ]

    for surface in ["public", "holdout"]:
        res = results[surface]
        if res is None:
            lines += [f"## {surface.upper()} -- SKIPPED (WALKWORTHY_ALLOW_HOLDOUT not set)", ""]
            continue

        lines += [
            f"## {surface.upper()}",
            "",
            f"- Total items: {res['total_items']}",
            f"- Total anchor instances (may repeat across items): {len(res['anchor_records'])}",
            "",
            "### Resolve status (alias -> book file)",
            "| Status | Count | Notes |",
            "|--------|-------|-------|",
        ]
        status_notes = {
            "RESOLVED": "alias matched to a corpus book",
            "PACK-REF": "structural multi-book pack ref (not a defect)",
            "UNRESOLVED": "DEFECT -- alias not in known map",
        }
        for k, v in sorted(res["resolve_counts"].items()):
            lines.append(f"| {k} | {v} | {status_notes.get(k, '')} |")

        lines += [
            "",
            "### Locator status (quoted title found in book text)",
            "| Status | Count |",
            "|--------|-------|",
        ]
        for k, v in sorted(res["status_counts"].items()):
            lines.append(f"| {k} | {v} |")

        lines += [
            "",
            "### Per-work anchor frequency (RESOLVED anchors only)",
            "| Book file | Count |",
            "|-----------|-------|",
        ]
        for bk, cnt in sorted(res["work_freq"].items(), key=lambda x: -x[1]):
            lines.append(f"| {bk} | {cnt} |")

        lines += [
            "",
            f"### L8 Flags (bare Scripture citations as anchor work-part): {len(res['l8_flags'])}",
        ]
        if res["l8_flags"]:
            for flag in res["l8_flags"]:
                lines.append(f"- `{flag['item_id']}` ({flag['design']}): {flag['anchor']}")
        else:
            lines.append("None detected.")

        lines += [
            "",
            f"### Bahnsen (contrast-only) inventory: {len(res['bahnsen_items'])} item(s)",
        ]
        if res["bahnsen_items"]:
            for iid in sorted(res["bahnsen_items"]):
                lines.append(f"- {iid}")
        else:
            lines.append("None.")

        unresolved = [r for r in res["anchor_records"] if r["resolve_status"] == "UNRESOLVED"]
        unresolved_anchors = list({r["anchor"] for r in unresolved})
        lines += [
            "",
            f"### True unresolved aliases (DEFECTS): {len(unresolved_anchors)} unique anchor strings",
        ]
        for ua in sorted(unresolved_anchors)[:80]:
            lines.append(f"- `{ua}`")
        if len(unresolved_anchors) > 80:
            lines.append(f"- ... and {len(unresolved_anchors) - 80} more (see JSON records)")

        lines.append("")

    summary_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[M2] Wrote {summary_path}")

    # ── stdout quick summary ────────────────────────────────────────────────
    print("\n=== M2 QUICK SUMMARY ===")
    for surface in ["public", "holdout"]:
        res = results[surface]
        if res is None:
            print(f"{surface}: SKIPPED")
            continue
        print(f"\n{surface}:")
        print(f"  Items: {res['total_items']}")
        print(f"  Anchor instances: {len(res['anchor_records'])}")
        print(f"  Resolve: {dict(res['resolve_counts'])}")
        print(f"  Loc status: {dict(res['status_counts'])}")
        print(f"  L8 flags: {len(res['l8_flags'])}")
        print(f"  Bahnsen items: {len(res['bahnsen_items'])}")
        unr = len({r['anchor'] for r in res['anchor_records'] if r['resolve_status'] == 'UNRESOLVED'})
        print(f"  True UNRESOLVED (defects) unique: {unr}")

if __name__ == "__main__":
    main()
