# Testing Guide - LifeOS Implementation (Phases 1-4)

**Purpose:** Validate progressive disclosure architecture and thread finalization workflows before continuing with Phases 5-8.

**Date:** 2026-02-02
**Implementation:** Phases 1-4 complete (40% of full migration)

---

## What We're Testing

1. **Progressive Disclosure** - Do lean configs work? Can we load standards on-demand?
2. **Thread Finalization** - Does `/end-session` capture learnings and create clean commits?
3. **Cross-Platform Parity** - Do all three configs (Claude/Gemini/OpenAI) provide consistent guidance?
4. **Memory System** - Does learnings-log.md accumulate knowledge over time?

---

## Test 1: Progressive Disclosure Architecture

**Goal:** Verify agents can work effectively with lean configs by loading standards on-demand.

### Test Case 1A: Classification Task

**Scenario:** Classify 3-5 papers for ethics frameworks.

**Steps:**
```bash
# 1. Start fresh session
# (New conversation or after context clear)

# 2. Agent reads CLAUDE.md (142 lines, not 2,000+)
# Expected: Agent sees "Load @_OPERATING-SYSTEM/Standards/classification-logic.md when classifying"

# 3. Agent loads classification-logic.md when needed
# Expected: Agent has full 7-stage pipeline details without config bloat

# 4. Classify sample papers
python3 PYTHON/classify_ethics.py papers/2016-Amodei-Concrete*.md
python3 PYTHON/classify_ethics.py papers/2024-*.md

# 5. Verify agent used classification logic correctly
# Check papers for ethics_overall, frameworks, etc.
```

**Success Criteria:**
- ✅ Agent references classification-logic.md when working
- ✅ Agent doesn't complain about missing context
- ✅ Classifications are correct (not confused by lean config)
- ✅ Agent didn't need to re-ask for rules (standards provided them)

**What to observe:**
- Does the agent say "Loading @_OPERATING-SYSTEM/Standards/classification-logic.md"?
- Does classification work as well as before despite shorter config?
- Any confusion or missing information?

---

### Test Case 1B: YAML Editing Task

**Scenario:** Edit paper metadata (add field, fix corruption).

**Steps:**
```bash
# 1. Agent needs to edit YAML
# Expected: Agent loads @_OPERATING-SYSTEM/Standards/yaml-standards.md

# 2. Make a safe YAML edit
# Add a field to 1 paper, e.g., manual_tags

# 3. Verify agent followed yaml-standards.md rules
# - Used yaml_frontmatter_utils.py?
# - Validated before writing?
# - Checked for orphaned items?

# 4. Validate result
python3 PYTHON/validate_all_papers.py
```

**Success Criteria:**
- ✅ Agent referenced yaml-standards.md
- ✅ Used `yaml_frontmatter_utils.py` (not regex)
- ✅ Validated before writing
- ✅ No YAML corruption introduced

---

## Test 2: Thread Finalization Workflow

**Goal:** Verify `/end-session` captures learnings and creates clean commits.

### Test Case 2A: Simple Classification Session

**Scenario:** Classify 5 papers, then run `/end-session`.

**Steps:**
```bash
# 1. Do some classification work
python3 PYTHON/classify_ethics.py papers/2024*.md  # Classify ~5 papers

# 2. Note any learnings or edge cases encountered
# (E.g., "Paper mentions multiple frameworks, prioritized based on 'we propose'")

# 3. Run /end-session
/end-session

# 4. Observe what happens
# Expected:
# - /remember-thread runs (Phase 1-5)
# - Learnings captured to learnings-log.md
# - SESSION_HISTORY.md updated
# - /finalize-thread runs (QA checklist)
# - Git commit created

# 5. Verify outputs
cat _OPERATING-SYSTEM/Learnings/learnings-log.md | tail -20
# Should show new entry under today's date

tail -50 docs/SESSION_HISTORY.md
# Should show new session entry

git log -1
# Should show commit with proper format

git show --stat
# Should show which files changed
```

**Success Criteria:**
- ✅ `/remember-thread` completes without errors
- ✅ Learnings captured in learnings-log.md with category tags
- ✅ SESSION_HISTORY.md has new session entry
- ✅ `/finalize-thread` runs QA checks (YAML, PDF, safety)
- ✅ Git commit created with proper message format
- ✅ Co-Authored-By tag present

**What to observe:**
- Did remember-thread capture any learnings? (Even if session was simple)
- Did finalize-thread catch any issues? (YAML, PDFs, etc.)
- Is the commit message clear and complete?
- Did the workflow feel systematic?

---

### Test Case 2B: Error Handling

**Scenario:** Intentionally introduce YAML corruption, verify finalize-thread catches it.

**Steps:**
```bash
# 1. Manually corrupt a paper's YAML
# (Add orphaned list item)
echo "  - #OrphanedTag" >> papers/test-paper.md

# 2. Try to run /end-session
/end-session

# 3. Observe finalize-thread QA
# Expected:
# - Category 1 (YAML Integrity) should FAIL
# - finalize-thread should STOP (blocking error)
# - Should NOT create git commit

# 4. Fix the corruption
# Remove the orphaned tag

# 5. Re-run /end-session
/end-session

# Expected: Now should pass and commit
```

**Success Criteria:**
- ✅ finalize-thread detects YAML corruption
- ✅ Blocks git commit (CRITICAL category failed)
- ✅ Provides clear error message
- ✅ After fix, allows commit to proceed

---

## Test 3: Cross-Platform Parity

**Goal:** Verify all three configs provide equivalent guidance.

### Test Case 3A: Config Comparison

**Steps:**
```bash
# 1. Compare configs
wc -l CLAUDE.md GEMINI.md OPENAI.md
# Expected: All ~140-160 lines (similar size)

# 2. Check key sections present in all
grep -A5 "Essential Rules" CLAUDE.md GEMINI.md OPENAI.md
grep -A5 "Context Loading" CLAUDE.md GEMINI.md OPENAI.md
grep -A5 "Memory & Learning" CLAUDE.md GEMINI.md OPENAI.md

# 3. Verify all point to same Standards/
grep "_OPERATING-SYSTEM/Standards" CLAUDE.md | wc -l
grep "_OPERATING-SYSTEM/Standards" GEMINI.md | wc -l
grep "_OPERATING-SYSTEM/Standards" OPENAI.md | wc -l
# Expected: Similar counts (all reference standards)
```

**Success Criteria:**
- ✅ All configs similar length (~140-160 lines)
- ✅ All have same essential rules (NO DELETIONS, YAML safety, git tracking)
- ✅ All point to same Standards/ files
- ✅ Platform-specific notes present where needed

---

### Test Case 3B: Gemini/OpenAI Testing

**If you have access to Gemini or OpenAI agents:**

**Steps:**
```bash
# 1. Start session with Gemini/OpenAI
# Have them read GEMINI.md or OPENAI.md

# 2. Do same classification task as Test 1A
# Classify 3-5 papers

# 3. Compare behavior to Claude
# - Did they load standards on-demand?
# - Did classifications work correctly?
# - Any confusion from config?

# 4. Note differences (if any)
# Document in learnings-log.md
```

**Success Criteria:**
- ✅ Gemini/OpenAI agents can use progressive disclosure
- ✅ Platform-specific notes are helpful (not confusing)
- ✅ Results consistent with Claude's work

---

## Test 4: Memory System Accumulation

**Goal:** Verify learnings-log.md grows over time with categorized knowledge.

### Test Case 4A: Learning Capture

**Scenario:** Work across 2-3 sessions, verify learnings accumulate.

**Steps:**
```bash
# Session 1: Classification
# - Classify papers
# - Note edge case (e.g., framework disambiguation)
# - Run /end-session
# - Check learnings-log.md (should have 1+ entries)

# Session 2: PDF work
# - Download PDFs
# - Note source patterns (arXiv vs publisher)
# - Run /end-session
# - Check learnings-log.md (should have more entries)

# Session 3: Review learnings
cat _OPERATING-SYSTEM/Learnings/learnings-log.md
# Expected:
# - Multiple date sections (2026-02-02, 2026-02-03, etc.)
# - Multiple categories represented (Classification, PDF Processing, etc.)
# - Entries are specific and actionable

# 4. Search learnings by category
grep "Classification" _OPERATING-SYSTEM/Learnings/learnings-log.md
grep "PDF" _OPERATING-SYSTEM/Learnings/learnings-log.md
```

**Success Criteria:**
- ✅ Each session adds to learnings-log.md
- ✅ Entries are categorized correctly
- ✅ Learnings are specific (not generic)
- ✅ Easy to search by category
- ✅ Knowledge persists across sessions

---

## Test 5: Standards Reference Pattern

**Goal:** Verify agents load standards when needed (not before).

### Test Case 5A: On-Demand Loading

**Scenario:** Track when agents load standards files.

**Steps:**
```bash
# 1. Start session with simple task (no classification)
# Task: "Count how many papers mention 'virtue'"
grep -c "virtue" papers/*.md

# 2. Observe agent behavior
# Expected: Agent does NOT load classification-logic.md
# (Not needed for simple grep)

# 3. Switch to classification task
# Task: "Classify 5 papers for virtue ethics"

# 4. Observe agent behavior
# Expected: NOW agent loads classification-logic.md
# (Needed for this task)

# 5. Note efficiency
# Did agent avoid loading unnecessary context?
```

**Success Criteria:**
- ✅ Agent loads standards only when needed
- ✅ Avoids loading all standards upfront
- ✅ Progressive disclosure actually reduces context usage
- ✅ Agent doesn't seem confused by on-demand loading

---

## Validation Checklist

After all tests, verify:

### File Integrity
```bash
# No YAML corruption introduced
python3 PYTHON/validate_all_papers.py
# Expected: All papers valid

# No files accidentally deleted
git status | grep "deleted"
# Expected: Empty (or only RECYCLE-BIN moves)

# Git history clean
git log --oneline | head -10
# Expected: Clear commit messages with Co-Authored-By
```

### Documentation Completeness
```bash
# README exists
cat _OPERATING-SYSTEM/README.md | head -20

# All 8 standards exist
ls -1 _OPERATING-SYSTEM/Standards/
# Expected: 8 files

# Learnings log has seed data
wc -l _OPERATING-SYSTEM/Learnings/learnings-log.md
# Expected: >100 lines

# Implementation status documented
cat _OPERATING-SYSTEM/IMPLEMENTATION_STATUS.md | head -30
```

### Skills Functional
```bash
# Skills exist
ls -1 .claude/skills/
# Expected: end-session, finalize-thread, remember-thread

# Skill docs complete
wc -l .claude/skills/*/SKILL.md
# Expected: 280+, 380+, 350+ lines respectively
```

---

## Known Issues to Watch For

### Issue 1: Obsidian Link Format

**Problem:** `@_OPERATING-SYSTEM/Standards/file.md` might not work in all contexts.

**Workaround:** If agent can't load via @-syntax, use full path:
```
Load: _OPERATING-SYSTEM/Standards/classification-logic.md
```

**Fix for later:** Adjust syntax if needed in configs.

---

### Issue 2: Skill Invocation

**Problem:** `/end-session` might not auto-invoke if skills not registered.

**Workaround:** Run manually:
```bash
# Read and execute manually
cat .claude/skills/remember-thread/SKILL.md
cat .claude/skills/finalize-thread/SKILL.md
# Follow steps manually
```

**Fix for later:** Ensure skills are properly registered in `.claude/skills/`.

---

### Issue 3: Git Commit Format

**Problem:** Agents might not follow exact commit message format.

**Workaround:** Edit commit message after:
```bash
git commit --amend
# Edit message to match format
```

**Fix for later:** Add commit message template to finalize-thread.

---

## Success Metrics

**Phase 1-4 successful if:**

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Config size reduction | >15% | `wc -l CLAUDE.md` (was ~180, now 142) |
| Standards coverage | 8 files | `ls _OPERATING-SYSTEM/Standards/ \| wc -l` |
| Learnings captured | >5 per session | Count entries in learnings-log.md |
| Session docs updated | 100% | Check SESSION_HISTORY.md after /end-session |
| QA checks pass | 100% | finalize-thread categories all green |
| Git commits clean | 100% | Proper format with Co-Authored-By |
| Cross-platform parity | 100% | All 3 configs reference same standards |

**If targets met:** Proceed to Phase 5-6 (Infrastructure & Testing)
**If targets not met:** Iterate on Phases 1-4 until stable

---

## Reporting Issues

**If you find issues:**

1. **Document in learnings-log.md**
   ```markdown
   | 2026-02-DD | Workflows | Issue: [Description]. Fix: [Solution]. |
   ```

2. **Create GitHub issue** (if significant)
   - Title: "[LifeOS] [Phase 1-4] [Issue description]"
   - Include: What you were doing, what went wrong, what you expected

3. **Note in IMPLEMENTATION_STATUS.md**
   - Update "Known Limitations" section
   - Add to testing results

---

## Next Steps After Testing

**If testing successful:**
1. Mark Phases 1-4 as validated ✅
2. Begin Phase 5-6 implementation (Infrastructure & Testing)
3. Continue with LifeOS migration plan

**If issues found:**
1. Document issues
2. Prioritize fixes
3. Iterate on Phases 1-4
4. Re-test before continuing

**If testing inconclusive:**
1. Use system in real work for 1-2 weeks
2. Accumulate learnings
3. Evaluate if progressive disclosure helps
4. Decide whether to continue or rollback

---

**Testing started:** [Date]
**Testing completed:** [Date]
**Result:** [PASS / NEEDS REVISION / ROLLBACK]

**Tester notes:**
[Your observations here]
