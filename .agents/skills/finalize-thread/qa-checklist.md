# 6-Category QA Checklist

Detailed checks for each QA category. Referenced by [SKILL.md](SKILL.md).

---

### Category 1: YAML Integrity (CRITICAL - Blocking)

**Status:** BLOCKING (cannot commit if failed)

**Checks:**

```bash
# 1. Basic YAML structure validation
python3 PYTHON/validate_all_papers.py
# Expected: "All papers valid" or specific error count

# 2. Enhanced validation (extended checks)
python3 PYTHON/validate_papers_enhanced.py
# Expected: Detailed report of any issues

# 3. Check for orphaned list items
grep -n "^  - " papers/*.md | wc -l
# Expected: 0 (any non-zero means orphaned tags)

# 4. Check for unquoted wikilinks
grep -l "^local_pdf: \[\[" papers/*.md | wc -l
grep -l "^first_author: \[\[" papers/*.md | wc -l
# Expected: 0,0 (both should be 0)

# 5. Check for hash prefixes in tags
grep -n '^  - "#' papers/*.md | wc -l
# Expected: 0

# 6. Verify newtags is string (not list)
grep -A1 "^newtags:$" papers/*.md | wc -l
# Expected: 0 (newtags should be inline string)
```

**Pass Criteria:**
- All validation scripts return success
- No orphaned list items
- No unquoted wikilinks
- No hash prefixes in tags
- newtags is always string format

**If Failed:**
- STOP - Cannot proceed to git commit
- Report specific files with issues
- User must fix before continuing
- Offer to run repair scripts if available

---

### Category 2: PDF Link Validation (HIGH)

**Status:** WARNING (can commit with warnings, but should fix)

**Checks:**

```bash
# 1. Audit PDF links
python3 PYTHON/audit_pdf_links.py 2>/dev/null

# 2. Check for missing PDFs (papers reference but file doesn't exist)
# (audit script reports this)

# 3. Check for orphaned PDFs (files exist but no paper references)
python3 PYTHON/find_orphaned_pdfs.py 2>/dev/null

# 4. Empty extracts
find "PDF Extracts" -name "*.md" -size 0 2>/dev/null

# 5. Missing extracts (paper has PDF but no extract)
# (Check papers with local_pdf but no pdf_extract)
```

**Pass Criteria:**
- All papers with local_pdf have valid PDF files
- All papers with pdf_extract have valid extract files
- No empty extracts
- Orphaned PDFs documented or moved to RECYCLE-BIN

**If Warnings:**
- Report issues but allow commit
- Note in commit message: "Warning: N broken PDF links"
- Create follow-up task to fix links

---

### Category 3: Data Safety (CRITICAL - Blocking)

**Status:** BLOCKING (file safety violations prevent commit)

**Checks:**

```bash
# 1. Git should NOT show deleted PDFs
git status | grep -E "deleted.*\.pdf$"
# Expected: Empty output

# 2. Git should NOT show deleted paper files
git status | grep -E "deleted.*papers/.*\.md$"
# Expected: Empty output

# 3. Check RECYCLE-BIN for appropriate moves
ls -lt RECYCLE-BIN/ 2>/dev/null | head -10
# Expected: If files deleted, they should be in RECYCLE-BIN

# 4. Verify no rm/unlink in staged Python files
git diff --cached --name-only | grep '\.py$' | xargs grep -l '\brm \|unlink\|rmtree' 2>/dev/null
# Expected: Empty output

# 5. Check for accidentally staged large files
git diff --cached --numstat | awk '$1 > 10000 || $2 > 10000 {print $3}'
# Expected: Empty (no huge diffs - might be binary)
```

**Pass Criteria:**
- No deleted PDFs or papers in git status
- All removals documented in RECYCLE-BIN
- No rm/unlink/rmtree in staged code
- No suspiciously large staged files

**If Failed:**
- STOP - Critical safety violation
- Report what was deleted
- Check if recovery possible from RECYCLE-BIN
- User must review and fix

---

### Category 4: Author File Validity (MEDIUM)

**Status:** INFORMATIONAL (won't block commit)

**Checks:**

```bash
# 1. Find orphaned authors
python3 PYTHON/find_orphaned_authors.py 2>/dev/null

# 2. Check for broken author links in papers
python3 PYTHON/audit_author_links.py 2>/dev/null

# 3. Authors missing enrichment data (if first authors)
grep -L "enriched: true" Authors/*.md 2>/dev/null | wc -l

# 4. Check for duplicate author files (case differences)
ls -1 Authors/ | tr '[:upper:]' '[:lower:]' | sort | uniq -d
```

**Pass Criteria:**
- Minimal orphaned authors (or documented)
- No broken author links
- First author enrichment >90%
- No duplicate author files

**If Issues:**
- Report for informational purposes
- Create follow-up tasks
- Don't block commit

---

### Category 5: Documentation Completeness (MEDIUM)

**Status:** INFORMATIONAL (won't block commit)

**Checks:**

```bash
# 1. Check for PENDING/TODO/FIXME markers
grep -r "PENDING\|TODO\|FIXME" papers/*.md docs/*.md _OPERATING-SYSTEM/ 2>/dev/null | wc -l

# 2. Verify SESSION_HISTORY.md updated
tail -20 docs/SESSION_HISTORY.md | grep -i "$(date +%Y-%m-%d)"
# Expected: Today's date should appear (session entry added)

# 3. Check learnings-log.md updated (if session had learnings)
tail -50 _OPERATING-SYSTEM/Learnings/learnings-log.md | grep -i "$(date +%Y-%m-%d)"
# Expected: Today's date should appear if learnings added

# 4. Verify Standards/ updated (if procedures changed)
git diff --cached _OPERATING-SYSTEM/Standards/

# 5. Check for uncommitted documentation
git status docs/ _OPERATING-SYSTEM/ | grep "modified\|new file"
```

**Pass Criteria:**
- SESSION_HISTORY.md has today's entry
- learnings-log.md updated if applicable
- No unresolved TODO/PENDING markers
- All relevant docs staged for commit

**If Issues:**
- Report missing documentation
- Suggest adding before commit
- Don't block if user chooses to skip

---

### Category 6: Git Workflow (HIGH)

**Status:** WARNING (verify before committing)

**Checks:**

```bash
# 1. Show current git status
git status

# 2. Preview what will be committed
git diff --cached --stat

# 3. Show first 50 lines of diff for review
git diff --cached | head -50

# 4. Check for merge conflicts
git status | grep -i "conflict"
# Expected: Empty

# 5. Verify not on detached HEAD
git branch | grep "^* (HEAD"
# Expected: Empty (should be on a branch)

# 6. Check if remote is available (for push)
git remote -v | grep origin
# Expected: GitHub remote configured

# 7. Check if branch is ahead/behind remote
git status | grep "Your branch is"
# Note for user
```

**Actions:**

**Stage all changes:**
```bash
git add .
# Review what's staged
git status
```

**Create commit:**
```bash
# Determine commit type based on session
# Format: "[Type]: [Brief description]
#
# [Details]
#
# Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Examples:
# - "Classification: Add ethics frameworks to 15 papers"
# - "Import: Add 5 new papers from arXiv"
# - "Fix: Repair YAML corruption in 12 papers"
# - "Enrich: Add key_contribution to virtue ethics papers"
# - "Docs: Update SESSION_HISTORY with Session 30"
# - "Infrastructure: Create _OPERATING-SYSTEM structure"

git commit -m "$(cat <<'EOF'
[Type]: [Brief description]

[Detailed changes]:
- [Change 1]
- [Change 2]
- [Change 3]

[Validation results]:
- YAML integrity: PASS
- PDF links: PASS
- File safety: PASS

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

**Push to remote:**
```bash
# Push immediately after commit
git push
```

**Pass Criteria:**
- Clean git status (no conflicts)
- On a proper branch (not detached HEAD)
- Remote configured
- Commit message follows format

**If Issues:**
- Report git issues
- Suggest fixes
- User decides whether to commit
