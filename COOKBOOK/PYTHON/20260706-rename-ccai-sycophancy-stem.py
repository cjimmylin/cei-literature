#!/usr/bin/env python3
"""
20260706-rename-ccai-sycophancy-stem.py

Rename the mis-filed CCAI/Sycophancy card stem.

OLD: Anthropic-Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548
NEW: Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548

Modes:
  --dry-run  (default) print every planned change, no writes
  --apply    perform the rename + substitutions

Usage:
  python 20260706-rename-ccai-sycophancy-stem.py [--dry-run | --apply]
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ── Paths ───────────────────────────────────────────────────────────────────
COOKBOOK = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK")
CARDS_DIR = COOKBOOK / "30-EVIDENCE" / "20260705-ailabs-cards"

OLD_STEM = "Anthropic-Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548"
NEW_STEM = "Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548"

OLD_CARD = CARDS_DIR / f"{OLD_STEM}.card.md"
NEW_CARD = CARDS_DIR / f"{NEW_STEM}.card.md"

# ── Known reference files (11 from the log + 2 extras found by grep) ────────
KNOWN_REFS = [
    # Files 1–10 from the 20260705 log
    COOKBOOK / "30-EVIDENCE" / "20260705-card-index.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-ailabs-shortlist.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-dossier-assignments" / "ai-lab-practices-part3.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-dossier-assignments" / "saturation-discrimination-part2.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-dossier-assignments" / "validity-psychometrics-part2.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-dossier-assignments" / "normative-ethics-part5.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-batches" / "L007.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-reader-batches.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-ailabs-listing.json",
    COOKBOOK / "30-EVIDENCE" / "20260705-dossiers" / "parts" / "saturation-discrimination-part2.md",
    # File 11 (abbreviated form)
    COOKBOOK / "00-KNOWLEDGEBASE" / "13-ai-lab-alignment-practices.md",
    # Extra files found by grep (not in original log map)
    COOKBOOK / "10-LITERATURE" / "20260705-lit-spotcheck-report.md",
    COOKBOOK / "10-LITERATURE" / "alignment-methods-overview.md",
]

# ── Replacement patterns ─────────────────────────────────────────────────────
# Order matters: full stem first (longer string), then abbreviated form.
# The abbreviated form in bracket citations: [Anthropic-Collective_Constitutional_AI...]
REPLACEMENTS = [
    # Full stem (covers JSON keys, path strings, inline citations with full stem)
    (OLD_STEM, NEW_STEM),
    # Path inside JSON (includes the directory prefix) — covered by full stem above
    # Abbreviated bracket form — note: match inside [ ... ] only to avoid clobbering
    # unrelated plain-text occurrences of "Collective_Constitutional_AI"
    (
        "Anthropic-Collective_Constitutional_AI]",
        "Anthropic-Towards_Understanding_Sycophancy_in_LMs]",
    ),
]

# Card-internal NOTE ON FILE NAMING — updated to reflect correction.
# NOTE: this pattern matches AFTER stem replacement has already run (so the
# stem in the note has been changed to NEW_STEM by then). The replacement text
# restores the OLD_STEM reference in the "previously mis-filed" phrase so the
# history is preserved correctly.
OLD_NOTE_PATTERN = re.compile(
    r'NOTE ON FILE NAMING: This extract is filed under the stem '
    r'"Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310\.13548" '
    r'but the actual paper is',
    re.DOTALL,
)
NEW_NOTE_TEXT = (
    'NOTE ON FILE NAMING (CORRECTED 2026-07-06): This extract was previously mis-filed '
    'under the stem "Anthropic-Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548" '
    'but has been renamed to the correct stem '
    '"Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548". The actual paper is'
)

# ── Collision guard ──────────────────────────────────────────────────────────
def collision_guard(dry_run: bool) -> bool:
    """
    Check that the new card file does not already exist.
    Check ailabs-listing.json for a near-match stem (v2 variant).
    Returns True if safe to proceed.
    """
    ok = True
    if NEW_CARD.exists():
        print(f"  [COLLISION] New card file ALREADY EXISTS: {NEW_CARD}")
        print("  Aborting — resolve manually before running --apply.")
        ok = False
    else:
        print(f"  [OK] New card path is clear: {NEW_CARD.name}")

    # Check ailabs-listing.json for existing sycophancy entries
    listing_path = COOKBOOK / "30-EVIDENCE" / "20260705-ailabs-listing.json"
    if listing_path.exists():
        text = listing_path.read_text()
        v2_stem = "Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548v2"
        exact_new = f'"stem": "{NEW_STEM}"'
        if exact_new in text:
            print(f"  [COLLISION] ailabs-listing.json already has an entry with the exact new stem.")
            print(f"  The duplicate entry would need manual reconciliation.")
            ok = False
        elif v2_stem in text:
            print(
                f"  [NEAR-MATCH] ailabs-listing.json already has a near-match entry:\n"
                f"    {v2_stem}\n"
                f"  The new stem will be:\n"
                f"    {NEW_STEM}\n"
                f"  These are distinct keys (base vs v2). No automatic merge will happen.\n"
                f"  RECOMMENDATION: After apply, confirm which entry is the authoritative\n"
                f"  one and consider removing the duplicate v2 entry manually."
            )
            # Not a blocking collision, just a warning
        else:
            print("  [OK] No duplicate sycophancy entry found in ailabs-listing.json.")
    return ok


def apply_replacements_to_text(text: str) -> tuple[str, int]:
    """Apply all REPLACEMENTS to text. Return (new_text, total_changes)."""
    total = 0
    for old, new in REPLACEMENTS:
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            total += count
    return text, total


def update_card_note(text: str) -> tuple[str, int]:
    """Update the NOTE ON FILE NAMING block inside the card itself."""
    new_text, count = OLD_NOTE_PATTERN.subn(NEW_NOTE_TEXT, text)
    return new_text, count


def process_files(files: list[Path], is_card: bool, dry_run: bool) -> dict:
    """
    Apply replacements to a list of files.
    Returns a summary dict: {path: {matches, changed}}.
    """
    results = {}
    for fpath in files:
        if not fpath.exists():
            print(f"  [MISSING] {fpath}")
            results[str(fpath)] = {"matches": 0, "changed": False, "error": "file not found"}
            continue

        original = fpath.read_text(encoding="utf-8")

        # Stem replacement runs first; note block update matches the post-replacement
        # state (where the old stem has already been changed to the new stem in the
        # note text, allowing the note pattern to match and inject the correct history).
        new_text, n = apply_replacements_to_text(original)

        note_changes = 0
        if is_card:
            new_text, note_changes = update_card_note(new_text)

        total_changes = n + note_changes

        if total_changes == 0:
            results[str(fpath)] = {"matches": 0, "changed": False}
            continue

        results[str(fpath)] = {"matches": total_changes, "changed": True}

        action = "[DRY-RUN]" if dry_run else "[APPLY]"
        note_str = f" + {note_changes} note-block update(s)" if note_changes else ""
        print(f"  {action} {fpath.name}: {n} stem replacement(s){note_str}")

        if not dry_run:
            fpath.write_text(new_text, encoding="utf-8")

    return results


def grep_extras(known_files: list[Path]) -> list[Path]:
    """
    Scan the entire COOKBOOK/ tree for any files containing the old stem or
    abbreviated form that are NOT in the known list.
    Returns a list of extra files.
    """
    known_set = {f.resolve() for f in known_files}
    known_set.add(OLD_CARD.resolve())
    # Exclude the script itself — it contains the old stem as string literals
    known_set.add(Path(__file__).resolve())

    extras = []
    patterns = [OLD_STEM, "Anthropic-Collective_Constitutional_AI]"]

    for fpath in COOKBOOK.rglob("*"):
        if not fpath.is_file():
            continue
        if fpath.resolve() in known_set:
            continue
        # Only scan text files
        suffix = fpath.suffix.lower()
        if suffix not in (".md", ".json", ".txt", ".py", ".html", ".js", ".css"):
            continue
        try:
            text = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for pat in patterns:
            if pat in text:
                extras.append(fpath)
                break

    return sorted(extras)


def validate_json_files(files: list[Path]) -> dict:
    """Validate all modified JSON files. Returns {path: ok/error}."""
    results = {}
    for fpath in files:
        if fpath.suffix.lower() != ".json":
            continue
        if not fpath.exists():
            results[str(fpath)] = "MISSING"
            continue
        try:
            with fpath.open(encoding="utf-8") as f:
                json.load(f)
            results[str(fpath)] = "OK"
        except json.JSONDecodeError as e:
            results[str(fpath)] = f"INVALID: {e}"
    return results


def check_remnants() -> dict:
    """Grep COOKBOOK/ for any remaining old-stem or old-abbreviated occurrences."""
    remnants = {}
    patterns = [OLD_STEM, "Anthropic-Collective_Constitutional_AI]"]

    for fpath in COOKBOOK.rglob("*"):
        if not fpath.is_file():
            continue
        suffix = fpath.suffix.lower()
        if suffix not in (".md", ".json", ".txt", ".py", ".html", ".js", ".css"):
            continue
        try:
            text = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for pat in patterns:
            if pat in text:
                count = text.count(pat)
                remnants[str(fpath)] = remnants.get(str(fpath), 0) + count

    return remnants


def main():
    parser = argparse.ArgumentParser(description="Rename CCAI→Sycophancy stem in COOKBOOK")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", dest="dry_run", action="store_true", default=True,
                      help="Print planned changes only (default)")
    mode.add_argument("--apply", dest="dry_run", action="store_false",
                      help="Actually perform the rename and substitutions")
    args = parser.parse_args()

    print("=" * 70)
    print(f"MODE: {'DRY-RUN' if args.dry_run else 'APPLY'}")
    print(f"OLD: {OLD_STEM}")
    print(f"NEW: {NEW_STEM}")
    print("=" * 70)

    # ── 1. Collision guard ───────────────────────────────────────────────────
    print("\n[1] COLLISION GUARD")
    if not collision_guard(args.dry_run):
        sys.exit(1)

    # ── 2. Extra-file grep ───────────────────────────────────────────────────
    print("\n[2] SCANNING FOR EXTRA FILES (beyond the 13 known references)...")
    extra_files = grep_extras(KNOWN_REFS)
    if extra_files:
        print(f"  Found {len(extra_files)} extra file(s):")
        for ef in extra_files:
            print(f"    + {ef.relative_to(COOKBOOK)}")
    else:
        print("  No extra files found.")

    all_ref_files = KNOWN_REFS + extra_files

    # ── 3. Process reference files ───────────────────────────────────────────
    print(f"\n[3] PROCESSING {len(all_ref_files)} REFERENCE FILES...")
    ref_results = process_files(all_ref_files, is_card=False, dry_run=args.dry_run)

    changed_refs = [p for p, r in ref_results.items() if r.get("changed")]
    unchanged_refs = [p for p, r in ref_results.items() if not r.get("changed")]
    print(f"\n  Changed: {len(changed_refs)} file(s)")
    print(f"  Unchanged (no occurrences): {len(unchanged_refs)} file(s)")

    # ── 4. Process the card file itself ──────────────────────────────────────
    print(f"\n[4] PROCESSING CARD FILE (content + NOTE block)...")
    if OLD_CARD.exists():
        card_results = process_files([OLD_CARD], is_card=True, dry_run=args.dry_run)
    else:
        print(f"  [ERROR] Old card file not found: {OLD_CARD}")
        card_results = {}

    # ── 5. Rename the card file ──────────────────────────────────────────────
    print(f"\n[5] CARD FILE RENAME")
    print(f"  OLD: {OLD_CARD.name}")
    print(f"  NEW: {NEW_CARD.name}")
    if args.dry_run:
        print("  [DRY-RUN] Would rename file.")
    else:
        if OLD_CARD.exists():
            OLD_CARD.rename(NEW_CARD)
            print("  [APPLY] File renamed.")
        else:
            print("  [ERROR] Old card file missing — skipping rename.")

    if args.dry_run:
        print("\n" + "=" * 70)
        print("DRY-RUN COMPLETE. Re-run with --apply to execute changes.")
        print("=" * 70)
        return

    # ── 6. POST-APPLY VALIDATION ─────────────────────────────────────────────
    print("\n[6] VALIDATION")

    # 6a. JSON validity
    print("  6a. JSON file validation:")
    json_modified = [Path(p) for p in changed_refs if p.endswith(".json")]
    json_results = validate_json_files(json_modified)
    all_json_ok = True
    for path, status in json_results.items():
        icon = "✓" if status == "OK" else "✗"
        print(f"    {icon} {Path(path).name}: {status}")
        if status != "OK":
            all_json_ok = False
    if all_json_ok:
        print("  All modified JSON files valid.")
    else:
        print("  WARNING: Some JSON files have errors — review before proceeding.")

    # 6b. Remnants check
    print("\n  6b. Checking for remaining old-stem occurrences...")
    remnants = check_remnants()
    if remnants:
        print(f"  WARNING: {len(remnants)} file(s) still contain old stem/abbrev:")
        for p, count in remnants.items():
            print(f"    {Path(p).relative_to(COOKBOOK)}: {count} occurrence(s)")
    else:
        print("  PASS: Zero remaining occurrences of old stem or abbreviated form.")

    # 6c. New card exists, old card gone
    print("\n  6c. Card file state:")
    new_exists = NEW_CARD.exists()
    old_gone = not OLD_CARD.exists()
    print(f"    New card exists: {'YES' if new_exists else 'NO (ERROR)'}")
    print(f"    Old card gone:   {'YES' if old_gone else 'NO (ERROR — still present)'}")

    print("\n" + "=" * 70)
    print("APPLY COMPLETE.")
    print("=" * 70)

    # ── 7. Summary ───────────────────────────────────────────────────────────
    print("\nSUMMARY")
    print(f"  Reference files processed: {len(all_ref_files)}")
    print(f"  Files changed: {len(changed_refs)}")
    print(f"  Extra files (beyond log map): {len(extra_files)}")
    print(f"  JSON validation: {'ALL OK' if all_json_ok else 'ERRORS FOUND'}")
    print(f"  Remnant check: {'CLEAN' if not remnants else f'{len(remnants)} files with remnants'}")
    print(f"  Card renamed: {'OK' if new_exists and old_gone else 'CHECK NEEDED'}")


if __name__ == "__main__":
    main()
