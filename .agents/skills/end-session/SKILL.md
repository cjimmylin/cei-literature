---
name: end-session
description: Orchestrate systematic session closure with memory consolidation and quality assurance. Runs remember-thread then finalize-thread.
disable-model-invocation: true
---

# End Session

**Purpose:** Orchestrate systematic session closure with memory consolidation and quality assurance.

**When to use:** At the end of any work session to ensure learnings are captured and changes are validated.

**Workflow:** Executes remember-thread → finalize-thread in sequence.

---

## Overview

The end-session skill implements a **2-phase closure workflow**:

```
Phase 1: Remember Thread (Memory Consolidation)
  ├─ Inventory changes
  ├─ Extract learnings
  ├─ Update documentation
  ├─ Pre-QA validation
  └─ Notify user

Phase 2: Finalize Thread (QA & Git)
  ├─ 6-category QA checklist
  ├─ Git workflow
  ├─ Commit changes
  ├─ Push to remote
  └─ Session closure summary
```

**Why this matters:**
- **Prevents knowledge loss** - Learnings persist across sessions
- **Ensures data integrity** - QA catches issues before commit
- **Maintains git hygiene** - Clean, well-documented commits
- **Creates audit trail** - SESSION_HISTORY.md tracks all work

---

## Execution Flow

### Step 1: Execute remember-thread

**Command:**
```bash
/remember-thread
```

**Expected output:**
- Inventory of all changes
- Learnings captured to learnings-log.md
- Documentation updated (SESSION_HISTORY.md, etc.)
- Pre-QA validation results
- Ready status for finalize-thread

**If remember-thread fails:**
- ⚠️ Review errors reported
- Fix issues (e.g., documentation not updated)
- Re-run remember-thread
- **Do not proceed to finalize-thread** until successful

---

### Step 2: Execute finalize-thread

**Command:**
```bash
/finalize-thread
```

**Expected output:**
- 6-category QA results
- Git commit created
- Push to remote (automatic)
- Session closure summary

**If finalize-thread fails:**
- 🔴 **CRITICAL failures** (YAML, data safety) - MUST fix before commit
- 🟡 **Warnings** (PDF links, docs) - Note for follow-up
- 🟢 **Informational** (author validity) - Optional to fix

**Resolution:**
- Fix critical issues
- Re-run finalize-thread
- Session not closed until successful

---

## Step 3: Verify Closure

**Check git status:**
```bash
git status
# Expected: "Your branch is up to date" or "Your branch is ahead by 1 commit"
```

**Review commit:**
```bash
git log -1 --stat
# Expected: Shows commit with proper message and file changes
```

**Verify push:**
```bash
git status | grep "Your branch is"
# Expected: "Your branch is up to date with 'origin/main'"
```

---

## Usage Patterns

### After Classification Session

```
Work done:
- Classified 20 papers for ethics frameworks
- Added key_contribution to 10 virtue ethics papers
- Updated newtags aggregation

Session closure:
/end-session

Expected:
- learnings-log.md: Classification edge cases added
- SESSION_HISTORY.md: Session entry with metrics
- Git commit: "Classification: Add ethics frameworks to 20 papers"
```

### After Import Session

```
Work done:
- Imported 5 new papers from arXiv
- Downloaded PDFs and created extracts
- Created 3 new author profiles

Session closure:
/end-session

Expected:
- learnings-log.md: API patterns, metadata extraction learnings
- SESSION_HISTORY.md: Import session with paper list
- Git commit: "Import: Add 5 papers on AI safety from arXiv"
```

### After Infrastructure Work

```
Work done:
- Created _OPERATING-SYSTEM/ structure
- Migrated 8 standards files
- Refactored AGENTS.md

Session closure:
/end-session

Expected:
- learnings-log.md: Workflow optimization, progressive disclosure
- SESSION_HISTORY.md: Infrastructure changes documented
- Git commit: "Infrastructure: Create _OPERATING-SYSTEM with progressive disclosure"
```

---

## Error Handling

### remember-thread Fails

**Scenario:** Documentation update fails, learnings not captured.

**Action:**
1. Review remember-thread output
2. Manually update missing documentation
3. Re-run `/remember-thread`
4. Once successful, continue to finalize-thread

**Do NOT skip remember-thread** - Learnings are valuable!

---

### finalize-thread Fails (YAML Issues)

**Scenario:** YAML validation finds orphaned list items in 3 papers.

**Action:**
1. Review reported files
2. Run repair script: `python3 PYTHON/repair_yaml_corruption.py`
3. Validate fix: `python3 PYTHON/validate_all_papers.py`
4. Re-run `/finalize-thread`

**Do NOT force commit** - Corrupted YAML breaks Obsidian!

---

### finalize-thread Fails (Data Safety)

**Scenario:** Git shows deleted PDFs.

**Action:**
1. Check RECYCLE-BIN for moved files
2. If files actually deleted, recover from Zotero backup
3. Move to RECYCLE-BIN if needed
4. Re-run `/finalize-thread`

**Do NOT commit deletions** - File safety rule is absolute!

---

### Git Push Fails

**Scenario:** Remote push fails (network issue, merge conflict).

**Action:**
1. Note commit is saved locally
2. Session closure is still successful
3. Push manually later: `git push`
4. Not critical for session closure

---

## Manual Execution (Without Skills)

If skills are not available, run manually:

### Manual remember-thread

```bash
# 1. Review git status
git status --short

# 2. Count changes
echo "Papers modified: $(git status --short papers/ | wc -l)"
echo "Scripts changed: $(git status --short PYTHON/ | wc -l)"

# 3. Update SESSION_HISTORY.md
# (Add session entry manually)

# 4. Update learnings-log.md
# (Add learnings manually)

# 5. Run pre-QA
python3 PYTHON/validate_all_papers.py
```

### Manual finalize-thread

```bash
# 1. Run QA checks
python3 PYTHON/validate_all_papers.py
python3 PYTHON/validate_papers_enhanced.py
python3 PYTHON/audit_pdf_links.py

# 2. Check data safety
git status | grep "deleted.*\.pdf$"  # Should be empty

# 3. Stage changes
git add .

# 4. Create commit
git commit -m "[Type]: [Brief description]

[Detailed changes]

Co-Authored-By: Codex Sonnet 4.5 <noreply@anthropic.com>"

# 5. Push
git push
```

---

## Best Practices

### Run at end of EVERY session

**Benefits:**
- Learnings persist (not lost when context clears)
- Documentation stays current
- Git history is clean and meaningful
- QA catches issues early

**Even for small sessions:**
- Fixed a single typo? Still run end-session.
- Only read files? Skip end-session (nothing to commit).
- Made any changes? Always run end-session.

### Don't skip steps

**Tempting to skip:**
- "Just a quick fix, don't need documentation"
- "YAML looks fine, skip validation"
- "Will push later, commit is enough"

**Why not to skip:**
- Quick fixes often reveal edge cases (learning!)
- YAML corruption is subtle (validation catches it)
- Local-only commits get forgotten (push immediately)

### Review before confirming

**Before git push:**
- Review commit message (accurate? complete?)
- Check file changes (anything unexpected?)
- Verify QA results (all green or noted?)

**If uncertain:**
- Ask user to review
- Show git diff preview
- Explain what will be committed

---

## Session Closure Ritual

**End-of-session checklist:**

1. ✅ All work completed (or paused with notes)
2. ✅ File safety verified (no rm, all moves to RECYCLE-BIN)
3. ✅ YAML integrity checked (no corruption)
4. ✅ Learnings captured (in learnings-log.md)
5. ✅ Documentation updated (SESSION_HISTORY.md)
6. ✅ Git committed (with good message)
7. ✅ Git pushed (to remote)

**When all ✅:**
- Session closed successfully 🎉
- Safe to end conversation
- Next session can start fresh

---

## What Gets Preserved

**Across sessions (persists in files):**
- ✅ Learnings (learnings-log.md)
- ✅ Session history (SESSION_HISTORY.md)
- ✅ Standards updates (Standards/)
- ✅ Code changes (PYTHON/, papers/)
- ✅ Git commits (permanent record)

**Lost between sessions (context clears):**
- ❌ Conversation history
- ❌ In-memory state
- ❌ Temporary files
- ❌ Unwritten insights

**That's why end-session matters** - It transfers knowledge from temporary (conversation) to permanent (files).

---

## Frequency

**Run end-session when:**
- ✅ Finishing work for the day
- ✅ After completing a major task (e.g., classification batch)
- ✅ Before switching to different task (preserve context)
- ✅ When conversation is getting long (commit work so far)
- ✅ After any significant changes

**Don't run end-session when:**
- ❌ Only read files (no changes)
- ❌ Just asking questions (no work done)
- ❌ Exploring/investigating (not ready to commit)

---

## Related Documentation

**How it works:**
- `@_OPERATING-SYSTEM/README.md` - 4-layer memory architecture
- `.Codex/skills/remember-thread/SKILL.md` - Memory consolidation
- `.Codex/skills/finalize-thread/SKILL.md` - QA and git workflow

**What gets updated:**
- `docs/SESSION_HISTORY.md` - Session records
- `_OPERATING-SYSTEM/Learnings/learnings-log.md` - Learnings
- `_OPERATING-SYSTEM/Standards/` - Procedures (if changed)

---

**Version:** 1.0
**Created:** 2026-02-02
**Part of:** LifeOS capabilities migration

---

## Quick Reference

```bash
# Full workflow
/end-session
# → Runs /remember-thread
# → Runs /finalize-thread
# → Session closed

# Individual steps (if needed)
/remember-thread    # Memory consolidation only
/finalize-thread    # QA and git only

# Manual fallback (if skills unavailable)
# See "Manual Execution" section above
```
