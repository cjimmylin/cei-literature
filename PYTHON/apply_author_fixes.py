#!/usr/bin/env python3
"""
Apply Author Fixes — Script 2 of 2

Reads the reviewed logs/20260208-unknown_authors_resolved.json and applies all updates:
  A. Update YAML frontmatter (safe regex in-place)
  B. Update paper body (Authors section, metadata block)
  C. Rename paper file
  D. Rename PDF file (main + framework subfolders)
  E. Rename PDF extract + update its internal references
  F. Wikilink propagation across all .md files
  G. Create author profiles for new authors
  H. Validate

Usage:
    # Dry run (preview changes)
    python apply_author_fixes.py --dry-run

    # Apply changes
    python apply_author_fixes.py

    # Skip specific steps
    python apply_author_fixes.py --skip-wikilinks --skip-authors
"""

import argparse
import functools
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Force flush
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from vault_config import (
    PAPERS_DIR, PDF_EXTRACTS_DIR, PDFS_DIR, AUTHORS_DIR,
    LOGS_DIR, RECYCLE_BIN_DIR, WORKSPACE_ROOT as WS_ROOT,
)

INPUT_JSON = LOGS_DIR / "20260216-unknown_authors_resolved.json"
AUTHOR_TEMPLATE = AUTHORS_DIR / "TEMPLATE.md"


def normalize_entry(entry: Dict) -> Dict:
    """Convert Session-84 agent JSON format to script's expected format.

    Agent produces:  {resolved: true, first_author: "Last, First", full_authors: "A; B; C", source: "web"}
    Script expects:  {status: "resolved", resolved_authors: [...], first_author_surname: "Last",
                      new_filename: "YYYY-Last-Title.md", resolution_source: "web"}
    """
    out = dict(entry)  # shallow copy

    # Status
    out["status"] = "resolved" if entry.get("resolved") else "unresolved"

    # Resolution source
    out["resolution_source"] = entry.get("source", "unknown")

    # Authors list (split on "; ")
    full_authors = entry.get("full_authors", "")
    if "; " in full_authors:
        out["resolved_authors"] = [a.strip() for a in full_authors.split("; ")]
    elif full_authors:
        out["resolved_authors"] = [full_authors.strip()]
    else:
        out["resolved_authors"] = []

    # First author surname
    first_author = entry.get("first_author", "")
    if ", " in first_author:
        # "Ramponi, Alan" → "Ramponi"
        surname = first_author.split(",")[0].strip()
    elif "(" in first_author:
        # "Ministry of Industry and Information Technology (MIIT)" → "MIIT"
        m = re.search(r'\(([^)]+)\)', first_author)
        surname = m.group(1) if m else first_author.split()[0]
    elif first_author:
        # "Krutrim AI Team" → "Krutrim"
        surname = first_author.split()[0]
    else:
        surname = "Unknown"
    out["first_author_surname"] = surname

    # Compute new_filename: replace author segment in YYYY-Author-Title.md
    filename = entry["filename"]
    parts = filename.split("-", 2)
    if len(parts) >= 3:
        year, _old_author, rest = parts
        out["new_filename"] = f"{year}-{surname}-{rest}"
    else:
        out["new_filename"] = filename

    return out


# ============================================================
# A. YAML Frontmatter Updates (SAFE regex in-place)
# ============================================================

def safe_replace_field(frontmatter: str, key: str, new_value: str) -> Tuple[str, int]:
    """
    Safely replace a YAML field value in-place using regex.
    NEVER uses parse→rebuild round-trip (would destroy list fields).

    Returns: (updated_frontmatter, replacement_count)
    """
    # Handle quoting: if value contains special chars, wrap in quotes
    safe_value = new_value.replace('"', "'")  # per MEMORY.md: no \" escaping
    if any(c in safe_value for c in (':', '[', ']', '{', '}', '#', '&', '*', '!', '|', '>', "'", ',')):
        replacement = f'{key}: "{safe_value}"'
    else:
        replacement = f'{key}: {safe_value}'

    pattern = rf'^{re.escape(key)}:\s*.*$'
    result, count = re.subn(pattern, replacement, frontmatter, count=1, flags=re.MULTILINE)
    return result, count


def update_yaml_frontmatter(content: str, paper_info: Dict) -> str:
    """
    Update YAML frontmatter fields for a resolved paper.

    Updates: authors, first_author, last_author, authors_incomplete, local_pdf, pdf_extract
    """
    fm_match = re.match(r"---\n(.*?)\n---\n", content, re.DOTALL)
    if not fm_match:
        return content

    frontmatter = fm_match.group(1)
    body = content[fm_match.end():]
    old_filename = paper_info["filename"]
    new_filename = paper_info["new_filename"]
    authors = paper_info["resolved_authors"]
    old_stem = old_filename.rsplit(".", 1)[0]
    new_stem = new_filename.rsplit(".", 1)[0]

    # 1. Update authors field
    authors_str = "; ".join(authors)
    frontmatter, _ = safe_replace_field(frontmatter, "authors", authors_str)

    # 2. Update first_author (with wikilink) — use JSON first_author directly
    first_author_val = paper_info.get("first_author", "")
    if first_author_val:
        fa_safe = first_author_val.replace('"', "'")
        fa_replacement = f'first_author: "[[{fa_safe}]]"'
        fa_pattern = r'^first_author:\s*.*$'
        frontmatter, count = re.subn(fa_pattern, fa_replacement, frontmatter, count=1, flags=re.MULTILINE)
        if count == 0:
            frontmatter = re.sub(
                r'^(authors:\s*.*)$',
                rf'\1\nfirst_author: "[[{fa_safe}]]"',
                frontmatter, count=1, flags=re.MULTILINE
            )

    # 3. Update last_author (with wikilink) — use JSON last_author directly
    last_author_val = paper_info.get("last_author", "")
    if last_author_val:
        la_safe = last_author_val.replace('"', "'")
        la_replacement = f'last_author: "[[{la_safe}]]"'
        la_pattern = r'^last_author:\s*.*$'
        frontmatter, count = re.subn(la_pattern, la_replacement, frontmatter, count=1, flags=re.MULTILINE)
        if count == 0:
            frontmatter = re.sub(
                r'^(first_author:\s*.*)$',
                rf'\1\nlast_author: "[[{la_safe}]]"',
                frontmatter, count=1, flags=re.MULTILINE
            )

    # 4. Reset authors_incomplete to false
    frontmatter, _ = safe_replace_field(frontmatter, "authors_incomplete", "false")

    # 5. Update local_pdf and pdf_extract references (if filename changed)
    #    Use stem replacement — stems like "2022-Unknown-Addressing Religious..." are unique
    #    This handles year-based paths (PDFs/YYYY/stem.pdf) correctly
    if old_stem != new_stem:
        frontmatter = frontmatter.replace(old_stem, new_stem)

    return f"---\n{frontmatter}\n---\n{body}"


# ============================================================
# B. Paper Body Updates
# ============================================================

def update_paper_body(content: str, paper_info: Dict) -> str:
    """Update the paper body: Authors section and metadata block."""
    authors = paper_info["resolved_authors"]
    old_filename = paper_info["filename"]

    if not authors:
        return content

    # Build author wikilinks
    author_wikilinks = ", ".join(f"[[{a}]]" for a in authors)
    authors_plain = "; ".join(authors)

    # 1. Replace [[Unknown]] or [[Authors]] in ## Authors section
    # Match the line(s) after "## Authors" heading
    content = re.sub(
        r'(## Authors\s*\n\s*)\[\[(?:Unknown|Authors|Authors not fully specified[^\]]*)\]\]',
        rf'\1{author_wikilinks}',
        content
    )

    # 2. Replace **Authors:** Unknown / **Authors:** Authors in metadata block
    content = re.sub(
        r'\*\*Authors:\*\*\s*(?:Unknown|Authors|Authors not fully specified[^\n]*)',
        f'**Authors:** {authors_plain}',
        content
    )

    return content


# ============================================================
# C. Rename Paper File
# ============================================================

def rename_paper_file(old_path: Path, new_filename: str, dry_run: bool) -> Optional[Path]:
    """Rename paper .md file. Returns new path or None if no rename needed."""
    if old_path.name == new_filename:
        return None

    new_path = old_path.parent / new_filename

    # Check for collision
    if new_path.exists():
        print(f"    WARNING: Collision! {new_filename} already exists, adding suffix")
        stem, ext = new_filename.rsplit(".", 1)
        new_path = old_path.parent / f"{stem}-2.{ext}"

    if dry_run:
        print(f"    [DRY] Rename: {old_path.name} → {new_path.name}")
    else:
        shutil.move(str(old_path), str(new_path))
        print(f"    Renamed: {old_path.name} → {new_path.name}")

    return new_path


# ============================================================
# D. Rename PDF Files
# ============================================================

def rename_pdf_files(old_stem: str, new_stem: str, dry_run: bool) -> int:
    """Rename all PDF copies (main + framework subfolders). Returns count.

    Uses iterdir() instead of rglob() to avoid issues with glob
    metacharacters like [ ] in filenames (e.g. '[[Unknown]]').
    """
    if old_stem == new_stem:
        return 0

    count = 0
    old_pdf_name = f"{old_stem}.pdf"
    new_pdf_name = f"{new_stem}.pdf"

    # Iterate year subdirectories explicitly (avoids glob metachar issues)
    for subdir in PDFS_DIR.iterdir():
        if not subdir.is_dir():
            continue
        pdf_path = subdir / old_pdf_name
        if not pdf_path.exists():
            continue
        new_pdf_path = subdir / new_pdf_name
        if new_pdf_path.exists():
            print(f"    WARNING: PDF collision at {new_pdf_path}")
            continue
        if dry_run:
            print(f"    [DRY] Rename PDF: {pdf_path.relative_to(PDFS_DIR)} → {new_pdf_name}")
        else:
            shutil.move(str(pdf_path), str(new_pdf_path))
            print(f"    Renamed PDF: {pdf_path.relative_to(PDFS_DIR)} → {new_pdf_name}")
        count += 1

    # Also check PDFS_DIR root (legacy flat layout)
    root_pdf = PDFS_DIR / old_pdf_name
    if root_pdf.exists():
        new_root = PDFS_DIR / new_pdf_name
        if new_root.exists():
            print(f"    WARNING: PDF collision at {new_root}")
        elif dry_run:
            print(f"    [DRY] Rename PDF: {old_pdf_name} → {new_pdf_name}")
            count += 1
        else:
            shutil.move(str(root_pdf), str(new_root))
            print(f"    Renamed PDF: {old_pdf_name} → {new_pdf_name}")
            count += 1

    return count


# ============================================================
# E. Rename PDF Extract + Update Internal References
# ============================================================

def rename_pdf_extract(old_stem: str, new_stem: str, dry_run: bool) -> bool:
    """Rename PDF extract and update its internal references.

    Searches year-based subdirectories (PDF Extracts/YYYY/) for the extract.
    """
    if old_stem == new_stem:
        return False

    # Search year subdirectories for the extract
    old_extract = None
    for subdir in PDF_EXTRACTS_DIR.iterdir():
        if not subdir.is_dir():
            continue
        candidate = subdir / f"{old_stem}.md"
        if candidate.exists():
            old_extract = candidate
            break

    # Fallback: check flat layout (legacy)
    if old_extract is None:
        flat = PDF_EXTRACTS_DIR / f"{old_stem}.md"
        if flat.exists():
            old_extract = flat

    if old_extract is None:
        print(f"    No extract found: {old_stem}.md")
        return False

    # Place new extract in same directory as old
    new_extract = old_extract.parent / f"{new_stem}.md"

    if new_extract.exists():
        print(f"    WARNING: Extract collision at {new_extract.name}")
        return False

    # Read and update internal references
    content = old_extract.read_text(encoding="utf-8")
    content = content.replace(old_stem, new_stem)

    if dry_run:
        rel = old_extract.relative_to(PDF_EXTRACTS_DIR)
        print(f"    [DRY] Rename extract: {rel} → {new_extract.name}")
    else:
        # Write updated content to new path
        new_extract.write_text(content, encoding="utf-8")
        # Move old to recycle bin
        recycle_dest = RECYCLE_BIN_DIR / f"extract_{old_extract.name}"
        shutil.move(str(old_extract), str(recycle_dest))
        rel = old_extract.relative_to(PDF_EXTRACTS_DIR)
        print(f"    Renamed extract: {rel} → {new_extract.name}")

    return True


# ============================================================
# F. Wikilink Propagation
# ============================================================

def propagate_wikilinks(rename_map: Dict[str, str], dry_run: bool) -> int:
    """
    Scan all .md files and update wikilinks from old stems to new stems.
    Must run AFTER all file renames are complete.

    Returns count of files modified.
    """
    if not rename_map:
        return 0

    print(f"\n  Propagating wikilinks ({len(rename_map)} renames)...")

    files_modified = 0

    # Scan all .md files in workspace (skip RECYCLE-BIN and .agent)
    for md_path in WS_ROOT.rglob("*.md"):
        rel = md_path.relative_to(WS_ROOT)
        # Skip directories we don't want to touch
        if any(part in str(rel) for part in ["RECYCLE-BIN", ".agent", "node_modules", ".git"]):
            continue

        try:
            content = md_path.read_text(encoding="utf-8")
        except Exception:
            continue

        original = content

        for old_stem, new_stem in rename_map.items():
            if old_stem not in content:
                continue

            # Replace [[old_stem]] → [[new_stem]]
            content = content.replace(f"[[{old_stem}]]", f"[[{new_stem}]]")

            # Replace [[old_stem|display text]] → [[new_stem|display text]]
            content = re.sub(
                rf'\[\[{re.escape(old_stem)}\|([^\]]+)\]\]',
                rf'[[{new_stem}|\1]]',
                content
            )

            # Replace bare references in paths (e.g., in PDF Extracts/, PDFs/)
            content = content.replace(old_stem, new_stem)

        if content != original:
            if dry_run:
                print(f"    [DRY] Update wikilinks in: {rel}")
            else:
                md_path.write_text(content, encoding="utf-8")
                print(f"    Updated wikilinks in: {rel}")
            files_modified += 1

    return files_modified


# ============================================================
# G. Create Author Profiles
# ============================================================

def create_author_profiles(all_authors: List[str], rename_map: Dict[str, str],
                          paper_lookup: Dict[str, Dict], dry_run: bool) -> int:
    """Create author profile pages for new authors. Returns count created."""
    if not AUTHOR_TEMPLATE.exists():
        print("    WARNING: Author template not found, skipping profile creation")
        return 0

    template = AUTHOR_TEMPLATE.read_text(encoding="utf-8")
    created = 0
    existing_authors = {f.stem for f in AUTHORS_DIR.glob("*.md")
                        if f.name not in ("README.md", "TEMPLATE.md")}

    for author_name in sorted(set(all_authors)):
        if not author_name or author_name.lower() in ("unknown", "authors", "et al", "et al."):
            continue

        # Sanitize for filename
        safe_name = author_name.strip().replace("/", "-").replace("\\", "-").replace(":", "-")
        if not safe_name:
            continue

        if safe_name in existing_authors:
            continue

        author_file = AUTHORS_DIR / f"{safe_name}.md"
        if author_file.exists():
            continue

        # Find papers by this author
        papers_for_author = []
        for paper_info in paper_lookup.values():
            if author_name in paper_info.get("resolved_authors", []):
                new_fn = paper_info.get("new_filename", paper_info["filename"])
                stem = new_fn.rsplit(".", 1)[0]
                short_title = stem.split("-", 2)[-1] if "-" in stem else stem
                papers_for_author.append(f"[[{stem}|{short_title}]]")

        if dry_run:
            print(f"    [DRY] Create author: {safe_name} ({len(papers_for_author)} papers)")
        else:
            content = template.replace("Full Name", safe_name)
            content = content.replace('name: "Full Name"', f'name: "{safe_name}"')
            papers_list = "\n".join(f"- {p}" for p in sorted(papers_for_author)) if papers_for_author else "- (none yet)"
            content = content.replace("- [[PaperFilename|Paper Title]]", papers_list)
            # Also replace in YAML if template has it
            content = content.replace('- [[YYYY-Author-ShortTitle|Full Paper Title]]', papers_list)
            author_file.write_text(content, encoding="utf-8")
            print(f"    Created author: {safe_name}")

        created += 1

    return created


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Apply author fixes from resolved JSON")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--skip-wikilinks", action="store_true", help="Skip wikilink propagation")
    parser.add_argument("--skip-authors", action="store_true", help="Skip author profile creation")
    parser.add_argument("--only", type=str, default=None, help="Only process this filename")
    args = parser.parse_args()

    print("=" * 80)
    print(f"APPLY AUTHOR FIXES {'(DRY RUN)' if args.dry_run else '(LIVE)'}")
    print("=" * 80)

    # Load resolved JSON
    if not INPUT_JSON.exists():
        print(f"ERROR: {INPUT_JSON} not found. Run discover_unknown_authors.py first.")
        sys.exit(1)

    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        all_papers = json.load(f)

    # Normalize agent JSON format to script's expected format
    all_papers = [normalize_entry(p) for p in all_papers]

    # Filter to resolved papers only
    papers = [p for p in all_papers if p["status"] == "resolved"]
    if args.only:
        papers = [p for p in papers if p["filename"] == args.only]

    print(f"Loaded {len(all_papers)} entries, {len(papers)} resolved to process")

    unresolved = [p for p in all_papers if p["status"] == "unresolved"]
    if unresolved:
        print(f"  ({len(unresolved)} unresolved papers will be skipped)")

    # --- Check for filename collisions before starting ---
    new_filenames = {}
    collisions = []
    for p in papers:
        nf = p["new_filename"]
        if nf in new_filenames:
            collisions.append((p["filename"], new_filenames[nf], nf))
        else:
            new_filenames[nf] = p["filename"]

    if collisions:
        print("\nWARNING: Filename collisions detected!")
        for old1, old2, new in collisions:
            print(f"  {old1} AND {old2} → {new}")
        print("  Will add disambiguation suffixes.")

    # Build rename map for wikilink propagation
    rename_map = {}  # old_stem → new_stem
    all_new_authors = []
    paper_lookup = {p["filename"]: p for p in papers}

    # === Process each paper ===
    stats = {"yaml_updated": 0, "renamed": 0, "pdfs_renamed": 0,
             "extracts_renamed": 0, "errors": 0}

    for i, paper_info in enumerate(papers, 1):
        filename = paper_info["filename"]
        new_filename = paper_info["new_filename"]
        old_stem = filename.rsplit(".", 1)[0]
        new_stem = new_filename.rsplit(".", 1)[0]

        print(f"\n[{i}/{len(papers)}] {filename}")
        print(f"  → {new_filename} (by {paper_info['first_author_surname']}, "
              f"via {paper_info['resolution_source']})")

        paper_path = PAPERS_DIR / filename
        if not paper_path.exists():
            print(f"  ERROR: Paper file not found!")
            stats["errors"] += 1
            continue

        # Collect authors for profile creation
        all_new_authors.extend(paper_info.get("resolved_authors", []))

        try:
            # A. Update YAML + B. Update body
            content = paper_path.read_text(encoding="utf-8")
            content = update_yaml_frontmatter(content, paper_info)
            content = update_paper_body(content, paper_info)

            if not args.dry_run:
                paper_path.write_text(content, encoding="utf-8")
            print(f"  [A+B] YAML + body updated")
            stats["yaml_updated"] += 1

            # C. Rename paper file
            if old_stem != new_stem:
                new_path = rename_paper_file(paper_path, new_filename, args.dry_run)
                if new_path:
                    stats["renamed"] += 1
                    rename_map[old_stem] = new_stem

            # D. Rename PDF files
            pdf_count = rename_pdf_files(old_stem, new_stem, args.dry_run)
            stats["pdfs_renamed"] += pdf_count

            # E. Rename PDF extract
            if rename_pdf_extract(old_stem, new_stem, args.dry_run):
                stats["extracts_renamed"] += 1

        except Exception as e:
            print(f"  ERROR: {e}")
            stats["errors"] += 1

    # === F. Wikilink propagation ===
    if not args.skip_wikilinks and rename_map:
        print(f"\n{'='*80}")
        print("WIKILINK PROPAGATION")
        print(f"{'='*80}")
        wl_count = propagate_wikilinks(rename_map, args.dry_run)
        print(f"  Updated {wl_count} files")
    else:
        print(f"\n  Wikilink propagation: {'skipped' if args.skip_wikilinks else 'no renames to propagate'}")

    # === G. Author profiles ===
    if not args.skip_authors and all_new_authors:
        print(f"\n{'='*80}")
        print("AUTHOR PROFILE CREATION")
        print(f"{'='*80}")
        author_count = create_author_profiles(all_new_authors, rename_map, paper_lookup, args.dry_run)
        print(f"  Created {author_count} author profiles")
    else:
        print(f"\n  Author profiles: {'skipped' if args.skip_authors else 'no new authors'}")

    # === Summary ===
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"  YAML + body updated:  {stats['yaml_updated']}")
    print(f"  Papers renamed:       {stats['renamed']}")
    print(f"  PDFs renamed:         {stats['pdfs_renamed']}")
    print(f"  Extracts renamed:     {stats['extracts_renamed']}")
    print(f"  Errors:               {stats['errors']}")
    print(f"  Rename map entries:   {len(rename_map)}")

    if not args.dry_run:
        print(f"\n  Run validation: ../.venv/bin/python PYTHON/validate_all_papers.py")


if __name__ == "__main__":
    main()
