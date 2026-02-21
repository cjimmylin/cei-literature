# Finalize Thread

**Purpose:** Run comprehensive QA checklist and complete git workflow for session closure.

**When to use:** After `/remember-thread` completes successfully.

**Orchestration:** Typically invoked by `/end-session` after remember-thread.

---

## 6-Category QA Checklist

### Category 1: YAML Integrity (CRITICAL - Blocking)

**Status:** 🔴 BLOCKING (cannot commit if failed)

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
- ❌ STOP - Cannot proceed to git commit
- Report specific files with issues
- User must fix before continuing
- Offer to run repair scripts if available

---

### Category 2: PDF Link Validation (HIGH)

**Status:** 🟡 WARNING (can commit with warnings, but should fix)

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
- ⚠️ Report issues but allow commit
- Note in commit message: "Warning: N broken PDF links"
- Create follow-up task to fix links

---

### Category 3: Data Safety (CRITICAL - Blocking)

**Status:** 🔴 BLOCKING (file safety violations prevent commit)

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
- ❌ STOP - Critical safety violation
- Report what was deleted
- Check if recovery possible from RECYCLE-BIN
- User must review and fix

---

### Category 4: Author File Validity (MEDIUM)

**Status:** 🟢 INFORMATIONAL (won't block commit)

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
- ℹ️ Report for informational purposes
- Create follow-up tasks
- Don't block commit

---

### Category 5: Documentation Completeness (MEDIUM)

**Status:** 🟢 INFORMATIONAL (won't block commit)

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
- ℹ️ Report missing documentation
- Suggest adding before commit
- Don't block if user chooses to skip

---

### Category 6: Git Workflow (HIGH)

**Status:** 🟡 WARNING (verify before committing)

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
- ⚠️ Report git issues
- Suggest fixes
- User decides whether to commit

---

## Execution Flow

```
1. Run Category 1 (YAML Integrity)
   ├─ PASS → Continue
   └─ FAIL → STOP, report issues

2. Run Category 2 (PDF Links)
   ├─ PASS → Continue
   └─ WARN → Note warnings, continue

3. Run Category 3 (Data Safety)
   ├─ PASS → Continue
   └─ FAIL → STOP, report violations

4. Run Category 4 (Author Validity)
   └─ INFO → Report, continue

5. Run Category 5 (Documentation)
   └─ INFO → Report, continue

6. Run Category 6 (Git Workflow)
   ├─ Stage changes
   ├─ Preview diff
   ├─ Create commit (with user-approved message)
   └─ Push to remote (automatic)
```

---

## Commit Message Format

**Structure:**
```
[Type]: [Brief description (50-70 chars)]

[Detailed changes]:
- [Change 1]
- [Change 2]
- [Change 3]

[Validation results]:
- YAML integrity: [PASS/WARN/FAIL]
- PDF links: [PASS/WARN]
- File safety: PASS

[Optional notes]:
[Any additional context]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Commit Types:**
- **Classification** - Adding/updating classification fields
- **Import** - New papers added to vault
- **Enrich** - Metadata enrichment
- **Fix** - Bug fixes, corruption repairs
- **Docs** - Documentation updates
- **Infrastructure** - System improvements
- **Maintenance** - Routine upkeep

**Examples:**

```
Classification: Add virtue ethics frameworks to 15 papers

[Detailed changes]:
- Classified 15 papers for virtue ethics frameworks
- Added key_contribution and significance fields
- Updated newtags aggregation

[Validation results]:
- YAML integrity: PASS
- PDF links: PASS
- File safety: PASS

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

```
Infrastructure: Create _OPERATING-SYSTEM with progressive disclosure

[Detailed changes]:
- Created _OPERATING-SYSTEM/ directory structure
- Added 8 Standards/ files (2,400+ lines)
- Created learnings-log.md with seed data
- Refactored CLAUDE.md, created GEMINI.md, OPENAI.md
- Marked YAML_SAFEGUARDS.md as deprecated

[Validation results]:
- YAML integrity: PASS
- PDF links: PASS
- File safety: PASS

[Notes]:
Implements LifeOS-style 4-layer memory architecture.
See _OPERATING-SYSTEM/README.md for details.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

---

## Session Closure Summary

**After git commit completes:**

```markdown
## Finalize Thread Complete ✅

**QA Results:**
- 🔴 YAML Integrity: [PASS/FAIL]
- 🟡 PDF Links: [PASS/WARN]
- 🔴 Data Safety: [PASS/FAIL]
- 🟢 Author Validity: [PASS/INFO]
- 🟢 Documentation: [PASS/INFO]
- 🟡 Git Workflow: [COMMITTED/PENDING]

**Git Commit:**
- Commit hash: [hash]
- Files changed: N files
- Insertions: +N lines
- Deletions: -N lines
- Pushed to remote: YES

**Follow-up Tasks:**
[List any issues that need attention]

---

**Session closed successfully.** 🎉

*Time to take a break! Next session, review:*
- `docs/SESSION_HISTORY.md` (Session NN)
- `_OPERATING-SYSTEM/Learnings/learnings-log.md` (recent entries)
```

---

## Push Behavior

**After commit completes, push immediately without waiting for user confirmation.**

When the session closure summary is shown:
- Run `git push` right away as part of the finalize flow
- Do NOT show git push output to the user (credential warnings are noisy)
- Report only the final status: "Pushed to remote" or "Push failed — run `git push` manually"
- If the user separately says "ready" or similar after a commit, just push silently — no intermediate output or commentary

---

## Error Handling

**YAML validation fails:**
1. Report specific files and issues
2. Offer to run repair scripts (if available)
3. **DO NOT commit** until fixed
4. Exit with error code

**Data safety violation:**
1. Report deleted files
2. Check RECYCLE-BIN for recovery
3. **DO NOT commit** until reviewed
4. Exit with error code

**Git conflicts:**
1. Report conflicts
2. Suggest resolution commands
3. Ask user to resolve manually
4. Exit gracefully

**Remote push fails:**
1. Note commit is local only
2. Suggest manual push later
3. Don't treat as critical error
4. Session still considered complete

---

## Best Practices

**Be thorough:**
- Run all checks, don't skip
- Report all issues found
- Prioritize critical (blocking) over informational

**Be safe:**
- Never commit corrupted YAML
- Never commit file deletions (should be RECYCLE-BIN moves)
- Validate before committing

**Be clear:**
- Provide actionable error messages
- Show how to fix issues
- Distinguish blocking vs. informational

---

## Related Skills

- **remember-thread** - Run before this skill
- **end-session** - Orchestrator that calls both skills
- **consolidate_memory** - Legacy skill (being replaced)

---

**Version:** 1.0
**Created:** 2026-02-02
**Part of:** LifeOS capabilities migration
