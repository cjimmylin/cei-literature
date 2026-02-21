---
name: remember-thread
description: Consolidate session learnings, update SESSION_HISTORY.md and learnings-log.md, run pre-QA validation. Use at end of work sessions.
disable-model-invocation: true
---

# Remember Thread

**Purpose:** Consolidate session learnings, update documentation, and prepare for quality assurance.

**When to use:** At the end of a work session, before running finalize-thread.

**Orchestration:** Typically invoked automatically by `/end-session`, but can be run standalone.

---

## 5-Phase Process

### Phase 1: Inventory Changes

Track all modifications made during this session:

**Papers:**
- New imports (count, titles)
- Classifications updated (ethics_overall, frameworks, perspectives)
- Enrichments added (key_contribution, significance)
- Metadata fixes (YAML corruption, missing fields)

**PDFs:**
- Downloads completed (count, sources)
- Extracts created (count)
- Link updates (local_pdf, pdf_extract fields)
- Recovery operations (from Zotero, re-downloads)

**Authors:**
- New profiles created (count, names)
- Enrichments completed (institution, position, links)
- Orphaned authors moved to RECYCLE-BIN
- Broken links repaired

**Scripts:**
- New scripts created (purpose, location)
- Bug fixes (what was broken, how fixed)
- Utilities added (new functions in PYTHON/)
- Library updates (if any)

**Documentation:**
- README updates (what changed)
- Workflow changes (new procedures)
- Standard updates (if classification logic changed)
- Session notes (important decisions)

**AI Labs:**
- New lab coverage (if applicable)
- Model documentation (papers, cards)
- Directory structure changes

**Actions:**
```bash
# Get git status for file counts
git status --short

# Count new papers (if imported)
ls -lt papers/*.md | head -20

# Check for modified PYTHON scripts
git diff --name-only PYTHON/

# Review modified docs
git diff --name-only docs/ _OPERATING-SYSTEM/
```

---

### Phase 2: Extract Learnings

Identify valuable knowledge to preserve in learnings-log.md:

**Vault Health:**
- Data quality improvements (corruption fixes, validation)
- Integrity checks run (results, issues found)
- Performance optimizations (faster scripts, better patterns)

**Workflow Optimization:**
- Batch processing improvements (parallel vs sequential)
- Automation added (new skills, scripts)
- Time savings discovered (what worked well)

**Edge Cases:**
- Classification ambiguities (how resolved)
- Duplicate handling (detection, resolution)
- Malformed data (corruption patterns, fixes)
- API rate limits (how handled, workarounds)

**Safety Lessons:**
- YAML corruption patterns encountered (and fixed)
- File safety incidents (if any near-misses)
- Validation failures (what caught issues)

**Categories for learnings-log.md:**
1. Classification - Framework detection, edge cases
2. YAML - Corruption patterns, fixes
3. API - Rate limits, error handling, version management
4. PDF Processing - Download sources, extraction issues
5. Author Management - Name validation, disambiguation
6. Data Quality - Audits, integrity checks
7. Skills - New workflows, improvements
8. Workflows - Batch operations, optimization
9. Git - Commit patterns, conflict resolution

**Actions:**
```bash
# Review session work
git log --oneline --since="today" | head -20

# Check for error patterns in recent work
grep -i "error\|warning\|failed" logs/*.log 2>/dev/null | tail -20
```

---

### Phase 3: Update Documentation

**Priority order:**

**1. SESSION_HISTORY.md (MANDATORY)**
Add session entry with:
- Session number and date
- Overview (what was accomplished)
- Key metrics (papers classified, PDFs downloaded, etc.)
- Important learnings (2-3 bullet points)
- Status (what's complete, what's pending)

**Format:**
```markdown
## Session NN (YYYY-MM-DD) - [Session Type]

### Overview
[1-2 sentence summary of session goals and accomplishments]

### Results
| Metric | Value |
|--------|-------|
| Papers Classified | NN |
| PDFs Downloaded | NN |
| ... | ... |

### Key Learnings
- [Learning 1 with category tag]
- [Learning 2 with category tag]
- [Learning 3 with category tag]

### Files Changed
- papers/: NN modified
- PYTHON/: N scripts updated
- docs/: N files updated
```

**2. learnings-log.md**
Add entries for each significant learning:

```markdown
## YYYY-MM-DD

| Date | Category | Learning |
|------|----------|----------|
| YYYY-MM-DD | Classification | [Specific learning with context] |
| YYYY-MM-DD | YAML | [Specific learning with context] |
...
```

**Guidelines:**
- Be specific and actionable (not generic)
- Include context (what triggered the learning)
- Note edge cases and exceptions
- Link to relevant Standards/ files if applicable

**3. Standards/ files (IF NEEDED)**
Update if classification logic or procedures changed:
- Extract new rules to appropriate standard
- Update examples with real cases from this session
- Document new patterns discovered

**4. Skill SKILL.md files (IF CHANGED)**
If workflow or skill improved:
- Update skill documentation
- Add new examples
- Document limitations discovered

**5. Config stats (IF COUNTS CHANGED)**
Update CLAUDE.md/GEMINI.md/OPENAI.md if:
- Paper count changed significantly
- New lab coverage added
- Major vault statistics shifted

**Actions:**
```bash
# Edit SESSION_HISTORY.md
# Add session entry at top

# Edit learnings-log.md
# Add entries under today's date

# Git diff to verify updates
git diff docs/SESSION_HISTORY.md
git diff _OPERATING-SYSTEM/Learnings/learnings-log.md
```

---

### Phase 4: Pre-QA Validation

Run quick integrity checks before finalize-thread:

**YAML Integrity (CRITICAL - Blocking):**
```bash
# Basic structure validation
python3 PYTHON/validate_all_papers.py

# Check for specific corruption patterns
grep -l "^  - " papers/*.md | wc -l  # Orphaned list items (should be 0)
grep -l "^local_pdf: \[\[" papers/*.md | wc -l  # Unquoted wikilinks (should be 0)
```

**PDF Link Validation:**
```bash
# Check for broken PDF links
python3 PYTHON/audit_pdf_links.py 2>/dev/null | grep -i "missing\|broken" | wc -l

# Empty extracts
find "PDF Extracts" -name "*.md" -size 0 2>/dev/null | wc -l
```

**File Safety Check:**
```bash
# Git should NOT show deleted PDFs
git status | grep -E "deleted.*\.pdf$" | wc -l  # Should be 0

# Check RECYCLE-BIN for moves
ls -lt RECYCLE-BIN/ 2>/dev/null | head -10
```

**Git State:**
```bash
# Show what will be committed
git status

# Preview first 20 lines of diff
git diff --cached | head -20
```

**Report results:**
- ✅ All checks passed → Proceed to finalize-thread
- ⚠️ Warnings found → Note for user review
- ❌ Errors found → STOP, must fix before finalize-thread

---

### Phase 5: Notify User

Provide session summary:

```markdown
## Remember Thread Summary

**Session Type:** [Classification / Enrichment / Import / Maintenance / Research]

**Files Changed:**
- Papers: NN modified (N new, N updated)
- Authors: NN modified (N new, N enriched)
- PDFs: NN downloaded, NN extracted
- Scripts: N created/updated
- Documentation: N files updated

**Key Learnings Captured:** N entries added to learnings-log.md
- [Category 1]: [Brief description]
- [Category 2]: [Brief description]

**Documentation Updated:**
- ✅ SESSION_HISTORY.md (Session NN added)
- ✅ learnings-log.md (N entries)
- [✅/⏭️] Standards/ (updated if needed)
- [✅/⏭️] Skill docs (updated if changed)

**Validation Status:**
- ✅ YAML integrity: [PASS/WARN/FAIL]
- ✅ PDF links: [PASS/WARN/FAIL]
- ✅ File safety: [PASS/WARN/FAIL]
- ✅ Git status: [Clean/Modified]

**Ready for finalize-thread:** [YES / NO - fix issues first]

---

*Next step: Run `/finalize-thread` for QA checklist and git commit.*
```

---

## Error Handling

**If validation fails:**
1. Report specific issues found
2. DO NOT proceed to finalize-thread
3. Ask user if they want to fix issues or continue anyway (with warning)

**If documentation updates fail:**
1. Note which files couldn't be updated
2. Provide manual update instructions
3. Continue with process (don't block on docs)

**If learnings extraction uncertain:**
1. List potential learnings
2. Ask user to confirm which to add
3. Default to conservative (only obvious learnings)

---

## Best Practices

**Be thorough but concise:**
- Capture key learnings, not every small detail
- Focus on reusable knowledge (not one-time fixes)
- Prioritize safety lessons and edge cases

**Update docs immediately:**
- Don't wait until end of session
- Fresh memory = better documentation
- Easier to track what changed

**Validate early:**
- Run checks before committing
- Catch issues while context is fresh
- Prevent committing corrupted data

---

## Related Skills

- **finalize-thread** - QA checklist and git commit (run after this)
- **end-session** - Orchestrator that calls this skill
- **consolidate_memory** - Legacy skill (being replaced)

---

**Version:** 1.0
**Created:** 2026-02-02
**Part of:** LifeOS capabilities migration
