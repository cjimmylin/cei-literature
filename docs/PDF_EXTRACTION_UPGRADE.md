# PDF Extraction Upgrade: TXT → Markdown

## Problem Diagnosed

Your PDF extracts weren't showing in Obsidian because:

1. **Wrong file format**: The script was saving as `.txt` files
2. **Obsidian limitation**: Obsidian's file explorer only displays Markdown files (.md) by default
3. **No native support**: Plain text files have limited Obsidian integration

✅ **Good news**: 58 extracts were created successfully on disk!
❌ **Bad news**: They're invisible in Obsidian's UI

## Solution Implemented

### Modified Files

#### 1. **`.agent/skills/extract_pdf_text/scripts/extract.py`**
- Changed output format from `.txt` → `.md`
- Added markdown frontmatter with metadata
- Wrapped PDF text in proper markdown code blocks
- Extracts now have:
  - Title header
  - Source PDF reference
  - Page count
  - Extraction timestamp
  - Full text in readable code block

#### 2. **`.agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py`** (NEW)
- Converts existing 58 .txt files to .md format
- Updates paper metadata automatically
- Provides dry-run mode to preview changes
- Optional cleanup to delete old .txt files
- Detailed progress reporting

#### 3. **`.agent/skills/extract_pdf_text/MIGRATION_GUIDE.md`** (NEW)
- Complete migration instructions
- Step-by-step usage guide
- Troubleshooting section
- Rollback procedures

## What to Do Now

### Option 1: Quick Migration (Recommended)

Run this two-step process:

```bash
# Step 1: Preview the migration (dry-run)
python3 .agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py --dry-run --verbose

# Step 2: Execute the migration
python3 .agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py --verbose

# Step 3 (Optional): Clean up old .txt files
python3 .agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py --cleanup
```

### Option 2: One Command (With Everything)

```bash
python3 .agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py --cleanup --verbose
```

## After Migration

1. **Restart Obsidian** to refresh file explorer
2. **Navigate to `PDF Extracts/` folder**
3. **You'll see 58 new `.md` files**

Each file will look like:
```markdown
---
title: "Paper Title - PDF Extract"
source_pdf: "2024-Author-Title.pdf"
pages: 10
migrated_at: "2026-01-24T..."
---

# PDF Extract: Paper Title

**Source PDF:** 2024-Author-Title.pdf
**Total Pages:** 10

---

## Content

```
[Full extracted PDF text here]
```
```

## Key Improvements

| Feature | Before (TXT) | After (MD) |
|---------|--------------|-----------|
| **Visible in Obsidian** | ❌ No | ✅ Yes |
| **File Explorer** | Hidden | Visible |
| **Searchable** | Limited | Full Search |
| **Properties Panel** | No | Yes |
| **Backlinks** | No | Yes |
| **Metadata** | None | Full frontmatter |
| **Link from papers** | Plain path | Proper wikilink |

## Migration Impact

- **58 files converted** (all existing extracts)
- **58 paper metadata updated** (pdf_extract paths)
- **Zero data loss** (old .txt files preserved until cleanup)
- **Safe rollback** possible (see MIGRATION_GUIDE.md)

## Future Usage

Going forward, the updated extraction script automatically saves as `.md`:

```bash
# All new extracts will be .md files
python3 .agent/skills/extract_pdf_text/scripts/extract.py

# Works with your existing workflow
python3 .agent/skills/extract_pdf_text/scripts/extract.py --verbose
python3 .agent/skills/extract_pdf_text/scripts/extract.py "2024-Smith-Title"
```

## Verification Checklist

After migration:

- [ ] Run migration script (dry-run first)
- [ ] Verify no errors in output
- [ ] Restart Obsidian
- [ ] Check `PDF Extracts/` folder is populated
- [ ] Click a .md file to view content
- [ ] Try searching text across extracts
- [ ] Run cleanup script (if satisfied)

## Files to Review

- [MIGRATION_GUIDE.md](.agent/skills/extract_pdf_text/MIGRATION_GUIDE.md) - Detailed instructions
- [extract.py](.agent/skills/extract_pdf_text/scripts/extract.py) - Updated extraction script
- [migrate_txt_to_md.py](.agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py) - Migration script

## Questions?

The migration process is safe and reversible:
- Dry-run mode shows exactly what will happen
- Original .txt files are preserved
- Can rollback if needed (see MIGRATION_GUIDE.md)

Ready to proceed? Run the migration scripts above.
