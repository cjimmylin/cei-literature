#!/usr/bin/env python3
"""
Phase 2: Fix PDF YAML references for papers with missing/broken local_pdf fields.

Actions:
1. Add local_pdf to ~45 papers that have PDFs on disk but no field
2. Fix 3 "PENDING - paywall restricted" local_pdf fields (2 have PDFs, 1 does not)
3. Mark 5 non-downloadable papers (no_pdf_applicable or local_pdf: N/A)
4. Fix 2 corrupted external_pdf fields (Zhang, Myers)
5. Add missing pdf_extract for Kreutz

Safety: Uses regex line replacement only — NO parse/rebuild round-trip.
"""

import functools
import os
import re
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

os.chdir(Path(__file__).parent.parent)  # CEI-Lit-WS/

PAPERS_DIR = Path("papers")
PDFS_DIR = Path("../PDFs")  # Relative from CEI-Lit-WS/

# ── Build PDF stem → path map ──────────────────────────────────────────
pdf_map = {}  # stem → relative path from repo root (e.g., "Lit-WS-PDFs/2024/file.pdf")
for pdf_path in PDFS_DIR.rglob("*.pdf"):
    stem = pdf_path.stem
    # Convert to repo-relative path for wikilinks
    rel = str(pdf_path).replace("../", "")  # "Lit-WS-PDFs/2024/file.pdf"
    if stem not in pdf_map:
        pdf_map[stem] = rel
    else:
        # Prefer year-subdir paths over ethics-framework paths
        existing = pdf_map[stem]
        year_match = re.match(r'^Lit-WS-PDFs/\d{4}/', rel)
        if year_match:
            pdf_map[stem] = rel

print(f"Loaded {len(pdf_map)} unique PDF stems from disk")

# ── Counters ──────────────────────────────────────────────────────────
added_local_pdf = 0
fixed_pending = 0
marked_non_downloadable = 0
fixed_external_pdf = 0
added_pdf_extract = 0
errors = []

# ── Non-downloadable papers ───────────────────────────────────────────
NO_PDF_APPLICABLE = {
    "2023-Lakera-GandalfIgnoreInstructions",
    "2025-Center-Personal Consultations Case Study Database",
    "2025-Consortium-The Vals Legal AI Report (VLAIR)",
}
LOCAL_PDF_NA = {
    "2025-Elder-The Ethics of Digital Ghosts",
    "2025-Rourke-Mind Crime",
}

# ── Corrupted external_pdf fields ─────────────────────────────────────
CORRUPTED_EXTERNAL_PDF = {
    "2022-Zhang-Artificial Intelligence and Moral Dilemmas": 'external_pdf: ""',
    "2024-Myers-People Expect Artificial Moral Advisors": 'external_pdf: ""',
}


def make_wikilink(pdf_rel_path: str) -> str:
    """Construct local_pdf YAML value from relative path."""
    return f'"[[{pdf_rel_path}]]"'


def add_field_after(frontmatter: str, anchor_key: str, new_line: str) -> str:
    """Insert new_line after the line starting with anchor_key in frontmatter."""
    lines = frontmatter.split('\n')
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and line.startswith(f'{anchor_key}:'):
            new_lines.append(new_line)
            inserted = True
    if not inserted:
        # Fallback: append before end
        new_lines.append(new_line)
    return '\n'.join(new_lines)


def process_paper(paper_path: Path) -> None:
    global added_local_pdf, fixed_pending, marked_non_downloadable, fixed_external_pdf, added_pdf_extract

    stem = paper_path.stem
    content = paper_path.read_text(encoding='utf-8')

    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        errors.append(f"{stem}: Could not parse frontmatter")
        return

    frontmatter = fm_match.group(1)
    body = content[fm_match.end():]
    modified = False

    # ── 1. Fix corrupted external_pdf fields ──────────────────────────
    if stem in CORRUPTED_EXTERNAL_PDF:
        # These have lines like:
        #   external_pdf:
        #   publication: "Journal..."
        # The publication line is NOT a sub-field of external_pdf; it's a
        # separate corrupted field. We fix external_pdf to empty string.
        # Check if external_pdf line is empty/malformed
        ext_match = re.search(r'^external_pdf:\s*$', frontmatter, re.MULTILINE)
        if ext_match:
            # Replace empty external_pdf with ""
            frontmatter = re.sub(
                r'^external_pdf:\s*$',
                CORRUPTED_EXTERNAL_PDF[stem],
                frontmatter,
                count=1,
                flags=re.MULTILINE
            )
            print(f"  FIXED external_pdf for {stem}")
            fixed_external_pdf += 1
            modified = True
        else:
            # Check if it has the publication text directly in external_pdf line
            ext_match2 = re.search(r'^external_pdf:\s+publication:', frontmatter, re.MULTILINE)
            if ext_match2:
                frontmatter = re.sub(
                    r'^external_pdf:\s+publication:.*$',
                    CORRUPTED_EXTERNAL_PDF[stem],
                    frontmatter,
                    count=1,
                    flags=re.MULTILINE
                )
                print(f"  FIXED external_pdf (inline corruption) for {stem}")
                fixed_external_pdf += 1
                modified = True

    # ── 2. Handle non-downloadable papers ─────────────────────────────
    if stem in NO_PDF_APPLICABLE:
        has_field = re.search(r'^no_pdf_applicable:', frontmatter, re.MULTILINE)
        if not has_field:
            frontmatter = add_field_after(frontmatter, 'pdf_extract', 'no_pdf_applicable: "true"')
            print(f"  MARKED no_pdf_applicable: {stem}")
            marked_non_downloadable += 1
            modified = True
        else:
            print(f"  SKIP (already has no_pdf_applicable): {stem}")
        # Write and return
        if modified:
            new_content = f"---\n{frontmatter}\n---{body}"
            paper_path.write_text(new_content, encoding='utf-8')
        return

    if stem in LOCAL_PDF_NA:
        has_local = re.search(r'^local_pdf:', frontmatter, re.MULTILINE)
        if not has_local:
            frontmatter = add_field_after(frontmatter, 'pdf_extract', 'local_pdf: N/A')
            print(f"  MARKED local_pdf N/A: {stem}")
            marked_non_downloadable += 1
            modified = True
        elif re.search(r'^local_pdf:\s*N/A', frontmatter, re.MULTILINE):
            print(f"  SKIP (already N/A): {stem}")
        else:
            frontmatter = re.sub(
                r'^local_pdf:.*$',
                'local_pdf: N/A',
                frontmatter,
                count=1,
                flags=re.MULTILINE
            )
            print(f"  SET local_pdf to N/A: {stem}")
            marked_non_downloadable += 1
            modified = True
        if modified:
            new_content = f"---\n{frontmatter}\n---{body}"
            paper_path.write_text(new_content, encoding='utf-8')
        return

    # ── 3. Fix PENDING local_pdf fields ───────────────────────────────
    pending_match = re.search(r'^local_pdf:\s*"?PENDING', frontmatter, re.MULTILINE)
    if pending_match:
        if stem in pdf_map:
            wikilink = make_wikilink(pdf_map[stem])
            frontmatter = re.sub(
                r'^local_pdf:.*$',
                f'local_pdf: {wikilink}',
                frontmatter,
                count=1,
                flags=re.MULTILINE
            )
            print(f"  FIXED PENDING → {wikilink}: {stem}")
            fixed_pending += 1
            modified = True
        else:
            # No PDF on disk — leave as-is (will be handled after download attempts)
            print(f"  SKIP PENDING (no PDF on disk): {stem}")

    # ── 4. Add local_pdf to papers with PDFs on disk ──────────────────
    has_local_pdf = re.search(r'^local_pdf:', frontmatter, re.MULTILINE)
    if not has_local_pdf and stem in pdf_map:
        wikilink = make_wikilink(pdf_map[stem])
        # Insert after url: or external_pdf: or pdf_extract: (whichever comes last)
        for anchor in ['pdf_extract', 'external_pdf', 'url']:
            if re.search(rf'^{re.escape(anchor)}:', frontmatter, re.MULTILINE):
                frontmatter = add_field_after(frontmatter, anchor, f'local_pdf: {wikilink}')
                print(f"  ADDED local_pdf (after {anchor}): {stem} → {wikilink}")
                added_local_pdf += 1
                modified = True
                break
        else:
            # Fallback: insert before ethics_overall or at end
            if re.search(r'^ethics_overall:', frontmatter, re.MULTILINE):
                frontmatter = re.sub(
                    r'^(ethics_overall:)',
                    f'local_pdf: {wikilink}\n\\1',
                    frontmatter,
                    count=1,
                    flags=re.MULTILINE
                )
            else:
                frontmatter += f'\nlocal_pdf: {wikilink}'
            print(f"  ADDED local_pdf (fallback): {stem} → {wikilink}")
            added_local_pdf += 1
            modified = True

    # ── 5. Add missing pdf_extract for Kreutz ─────────────────────────
    if stem == "2019-Kreutz-GermEval 2019 Task 2":
        has_extract = re.search(r'^pdf_extract:', frontmatter, re.MULTILINE)
        if not has_extract:
            extract_path = '"PDF Extracts/2019/2019-Kreutz-GermEval 2019 Task 2.md"'
            frontmatter = add_field_after(frontmatter, 'local_pdf', f'pdf_extract: {extract_path}')
            print(f"  ADDED pdf_extract: {stem}")
            added_pdf_extract += 1
            modified = True

    # ── Write back ────────────────────────────────────────────────────
    if modified:
        new_content = f"---\n{frontmatter}\n---{body}"
        paper_path.write_text(new_content, encoding='utf-8')


# ── Main ──────────────────────────────────────────────────────────────
print("=" * 70)
print("Phase 2: Fix PDF YAML References")
print("=" * 70)

all_papers = sorted(PAPERS_DIR.glob("*.md"))
print(f"Scanning {len(all_papers)} papers...\n")

for paper in all_papers:
    try:
        process_paper(paper)
    except Exception as e:
        errors.append(f"{paper.stem}: {e}")
        print(f"  ERROR: {paper.stem}: {e}")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"  Added local_pdf:         {added_local_pdf}")
print(f"  Fixed PENDING fields:    {fixed_pending}")
print(f"  Marked non-downloadable: {marked_non_downloadable}")
print(f"  Fixed external_pdf:      {fixed_external_pdf}")
print(f"  Added pdf_extract:       {added_pdf_extract}")
print(f"  Errors:                  {len(errors)}")
if errors:
    for e in errors:
        print(f"    - {e}")
print("=" * 70)
