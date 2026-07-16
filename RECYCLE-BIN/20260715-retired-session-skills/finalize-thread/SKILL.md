---
name: finalize-thread
description: Run 6-category QA checklist and complete git commit/push workflow for session closure. Use after remember-thread completes.
disable-model-invocation: true
---

# Finalize Thread

**Purpose:** Run comprehensive QA checklist and complete git workflow for session closure.

**When to use:** After `/remember-thread` completes successfully.

**Orchestration:** Typically invoked by `/end-session` after remember-thread.

---

## 6-Category QA Checklist

For detailed checks, bash commands, pass criteria, and failure handling for each category, see [qa-checklist.md](qa-checklist.md).

**Category Summary:**

| # | Category | Severity | Blocking? |
|---|----------|----------|-----------|
| 1 | YAML Integrity | CRITICAL | Yes — cannot commit if failed |
| 2 | PDF Link Validation | HIGH | No — commit with warnings |
| 3 | Data Safety | CRITICAL | Yes — file safety violations block |
| 4 | Author File Validity | MEDIUM | No — informational only |
| 5 | Documentation Completeness | MEDIUM | No — informational only |
| 6 | Git Workflow | HIGH | No — verify before committing |

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
