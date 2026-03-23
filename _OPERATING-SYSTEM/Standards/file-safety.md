# File Safety Standards

**Version:** 1.0
**Created:** 2026-02-02
**Category:** Data Safety (CRITICAL)
**Applies to:** All file operations in CEI Literature Vault

---

## ⛔ CRITICAL RULE: NO FILE DELETIONS

**NEVER use `rm`, `unlink`, `shutil.rmtree()`, or ANY delete command.**

This rule is **absolute** and has **NO EXCEPTIONS**.

---

## Why This Rule Exists

**Session 7 (January 2026):** Accidental deletion destroyed **422 PDF files** using `rm -rf Lit-WS-PDFs/`.

**Impact:**
- 8 hours of recovery work
- Multi-source recovery strategy (Zotero, arXiv, Semantic Scholar)
- Some PDFs permanently lost (unpublished preprints, conference papers)
- Trust in automation damaged

**Root Cause:** Script used destructive `rm` command without safety checks.

**Prevention:** This absolute rule + enforcement in pre-commit hooks + code review.

---

## Required Pattern: Move to RECYCLE-BIN/

### For Single Files

```bash
# ❌ FORBIDDEN
rm unwanted.pdf
unlink old-file.md

# ✅ REQUIRED
mv unwanted.pdf RECYCLE-BIN/
mv old-file.md RECYCLE-BIN/
```

### For Directories

```bash
# ❌ FORBIDDEN
rm -rf old-directory/
shutil.rmtree("old-directory")

# ✅ REQUIRED
mv old-directory/ RECYCLE-BIN/
shutil.move("old-directory", "RECYCLE-BIN/")
```

### For Multiple Files

```bash
# ❌ FORBIDDEN
find . -name "*.tmp" -delete
rm *.log

# ✅ REQUIRED
find . -name "*.tmp" -exec mv {} RECYCLE-BIN/ \;
for f in *.log; do mv "$f" RECYCLE-BIN/; done
```

---

## RECYCLE-BIN/ Management

### Location
- **Main workspace:** `CEI-Lit-WS/RECYCLE-BIN/`
- **External PDFs:** (configured in `.vault-config.json`) has its own RECYCLE-BIN/

### Structure
```
RECYCLE-BIN/
├── YYYY-MM-DD/                    # Dated folders for organization
│   ├── session-N-deletions/       # Session-specific deletions
│   └── script-name-output/        # Script-specific deletions
└── README.md                      # Deletion log
```

### Cleanup Policy
- **Manual review required:** Check RECYCLE-BIN/ contents before permanent deletion
- **Monthly cleanup:** Review files >30 days old, permanently delete if safe
- **Disk space emergency:** Only then consider permanent deletion
- **Never auto-delete:** No scripts automatically empty RECYCLE-BIN/

### Deletion Log Format

**File:** `RECYCLE-BIN/README.md`

```markdown
# Deletion Log

| Date | Source | Reason | Files | Reviewer | Safe to Delete? |
|------|--------|--------|-------|----------|-----------------|
| 2026-02-02 | classify_papers.py | Duplicate PDFs | 5 PDFs | Claude | After verification |
| 2026-01-28 | manual | Test files | 12 .tmp | Human | Yes |
```

---

## Enforcement Mechanisms

### 1. Pre-commit Hook

**File:** `.git/hooks/pre-commit`

```bash
# Check for dangerous commands in staged Python files
if git diff --cached --name-only | grep '\.py$' | xargs grep -l 'rm \|unlink\|rmtree'; then
    echo "ERROR: Detected 'rm', 'unlink', or 'rmtree' in staged files"
    echo "Use 'mv' to RECYCLE-BIN/ instead"
    exit 1
fi

# Check for dangerous commands in staged bash scripts
if git diff --cached --name-only | grep '\.sh$' | xargs grep -l '^rm \|; rm '; then
    echo "ERROR: Detected 'rm' command in staged bash files"
    echo "Use 'mv' to RECYCLE-BIN/ instead"
    exit 1
fi
```

### 2. Code Review Checklist

Before committing any script:
- [ ] Search for `rm ` in code
- [ ] Search for `unlink(` in code
- [ ] Search for `rmtree(` in code
- [ ] Search for `-delete` flag in find commands
- [ ] All removals use `mv` to RECYCLE-BIN/
- [ ] RECYCLE-BIN/ path uses absolute path (from `vault_config.py`)

### 3. AI Agent Instructions

All agent configs (CLAUDE.md, GEMINI.md, OPENAI.md) must include:

```markdown
## File Safety
- **NO DELETIONS:** NEVER use `rm`, `unlink`, or any delete command
- **Move to RECYCLE-BIN/:** Use `mv file RECYCLE-BIN/`
- **No exceptions:** This rule is absolute
- **Reference:** @_OPERATING-SYSTEM/Standards/file-safety.md
```

---

## Safe File Operations Patterns

### Python (Using shutil)

```python
import shutil
from pathlib import Path
from PYTHON.vault_config import RECYCLE_BIN

def safe_remove_file(filepath: Path) -> None:
    """Safely remove file by moving to RECYCLE-BIN/."""
    if not filepath.exists():
        return

    # Create dated subfolder
    today = datetime.now().strftime("%Y-%m-%d")
    recycle_dir = RECYCLE_BIN / today
    recycle_dir.mkdir(parents=True, exist_ok=True)

    # Move (don't delete)
    dest = recycle_dir / filepath.name
    shutil.move(str(filepath), str(dest))
    print(f"Moved to RECYCLE-BIN: {filepath.name} → {dest}")

def safe_remove_directory(dirpath: Path) -> None:
    """Safely remove directory by moving to RECYCLE-BIN/."""
    if not dirpath.exists():
        return

    today = datetime.now().strftime("%Y-%m-%d")
    recycle_dir = RECYCLE_BIN / today
    recycle_dir.mkdir(parents=True, exist_ok=True)

    dest = recycle_dir / dirpath.name
    shutil.move(str(dirpath), str(dest))
    print(f"Moved to RECYCLE-BIN: {dirpath.name} → {dest}")
```

### Bash

```bash
# Source centralized config
source "$(dirname "$0")/vault_config.sh"

safe_remove() {
    local file="$1"
    local today=$(date +%Y-%m-%d)
    local recycle_dir="${RECYCLE_BIN}/${today}"

    mkdir -p "$recycle_dir"
    mv "$file" "$recycle_dir/"
    echo "Moved to RECYCLE-BIN: $(basename "$file")"
}

# Usage
safe_remove "unwanted.pdf"
```

---

## Recovery Procedures

### Immediate Recovery (Within Session)

If file was just moved to RECYCLE-BIN/:

```bash
# Find file
find RECYCLE-BIN/ -name "filename.pdf" -mtime -1

# Restore
mv RECYCLE-BIN/2026-02-02/filename.pdf original/location/
```

### Historical Recovery (After Session)

If file was permanently deleted before this rule:

1. **Check git history** (for text files):
   ```bash
   git log --all --full-history -- path/to/file.md
   git checkout <commit> -- path/to/file.md
   ```

2. **Check Zotero backup** (for PDFs):
   ```bash
   # PDFs in ~/Zotero/storage (read-only reference)
   find ~/Zotero/storage -name "*.pdf" | grep "paper-name"
   ```

3. **Re-download from source**:
   - arXiv: `https://arxiv.org/pdf/{arxiv_id}.pdf`
   - Semantic Scholar: API lookup by DOI
   - Publisher website: Direct download

See `docs/PDF_RECOVERY_GUIDE.md` for full recovery procedures.

---

## Exception Requests

**There are NO exceptions to this rule.**

If you believe you have a legitimate reason to permanently delete files:

1. Document the reason
2. Get explicit approval from vault owner (human)
3. Create backup before deletion
4. Use `mv` to RECYCLE-BIN/ anyway (maintain rule consistency)
5. After 30-day retention, revisit deletion request

**The answer will almost always be: Use RECYCLE-BIN/.**

---

## Related Standards

- **YAML Safety:** `yaml-standards.md` (prevent data corruption)
- **PDF Processing:** `pdf-processing.md` (download, extraction, linking)
- **Data Quality:** `../Learnings/learnings-log.md` (Session 7 deletion incident)

---

## Audit Trail

All file movements to RECYCLE-BIN/ should be logged:

```python
import logging
from datetime import datetime

def log_deletion(filepath: Path, reason: str) -> None:
    """Log file movement to RECYCLE-BIN/."""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "file": str(filepath),
        "reason": reason,
        "moved_to": str(RECYCLE_BIN / datetime.now().strftime("%Y-%m-%d") / filepath.name)
    }
    logging.info(f"DELETION: {log_entry}")

    # Append to deletion log
    with open(RECYCLE_BIN / "README.md", "a") as f:
        f.write(f"| {log_entry['timestamp']} | script | {reason} | {filepath.name} | - | Pending |\n")
```

---

**Remember:** It's easier to restore from RECYCLE-BIN/ than to recover permanently deleted files. Always err on the side of caution.

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial standard created after Session 7 incident |
