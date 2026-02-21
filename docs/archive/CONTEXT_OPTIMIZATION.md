# Context Optimization Guide

**Created:** Jan 24, 2026
**Status:** MANDATORY - All future sessions must follow these rules

---

## MANDATORY RULES

### Rule 1: Never Bloat CLAUDE.md

| Do | Don't |
|----|-------|
| Keep under 100 lines | Add session history |
| One-line summaries only | Add detailed examples |
| Link to `docs/` for details | Duplicate information |
| Update stats table only | Add new sections |

### Rule 2: Never Bloat Root Directory

| Do | Don't |
|----|-------|
| Keep only 5 essential files | Create new `.md` files in root |
| Put docs in `docs/` | Put reports in root |
| Put logs in `logs/` | Put JSON/logs in root |
| Put scripts in `PYTHON/` | Put scripts in root |

### Rule 3: File Placement Rules

**ALWAYS place new files in the correct directory:**

| File Type | Directory | Examples |
|-----------|-----------|----------|
| Documentation | `docs/` | Reports, guides, summaries, session notes |
| Python scripts | `PYTHON/` | Any `.py` file |
| Log files | `logs/` | `.log`, `.json` reports, `.txt` outputs |
| Skills | `.claude/skills/` | Claude skill definitions |
| Commands | `.claude/commands/` | Slash command definitions |
| Agent skills | `.agent/skills/` | Antigravity/agent skills |
| Paper files | `papers/` | Individual paper metadata |
| PDF files | `PDFs/` | Downloaded PDFs |
| PDF extracts | `PDF Extracts/` | Extracted text as markdown |
| Author profiles | `Authors/` | Author profile files |
| Statistics | `STATISTICS/` | Generated reports |

---

## Root Directory Structure (Permanent)

**Only these 5 files belong in root:**

```
Root/
├── CLAUDE.md                    # Main context (~85 lines max)
├── YAML_SAFEGUARDS.md          # YAML rules (~85 lines max)
├── LLM_CONTEXT.md              # Classification logic (can be large)
├── README.md                   # Standard repo readme
└── Base Source from Zotero.md  # Primary data (read-only)
```

**Everything else goes in subdirectories.**

---

## Progressive Disclosure Principle

### How It Works

1. **CLAUDE.md loads automatically** with minimal essentials
2. **Read additional docs only when needed** for specific tasks
3. **Never load everything** - context bloat wastes tokens

### Progressive Documentation Table

This table lives in `CLAUDE.md` and guides when to load more context:

| Task | Read |
|------|------|
| Running classification/scripts | `docs/SCRIPTS.md` |
| Common workflows | `docs/WORKFLOWS.md` |
| Slash commands reference | `docs/COMMANDS.md` |
| YAML issues | `YAML_SAFEGUARDS.md` |
| Classification logic | `LLM_CONTEXT.md` |
| Session history | `docs/SESSION_HISTORY.md` |
| Maintaining doc structure | `docs/CONTEXT_OPTIMIZATION.md` |

---

## Adding New Content

### New Script Created
1. Save to `PYTHON/`
2. Add entry to `docs/SCRIPTS.md`
3. Do NOT add to `CLAUDE.md`

### New Workflow Documented
1. Add to `docs/WORKFLOWS.md`
2. Do NOT add to `CLAUDE.md`

### New Slash Command
1. Create in `.claude/commands/`
2. Add skill in `.claude/skills/`
3. Add one-line entry to `docs/COMMANDS.md`
4. Add to quick list table in `CLAUDE.md` (one line only)

### New Documentation File
1. Save to `docs/`
2. Link from relevant existing doc
3. Do NOT create in root

### Session Notes/Handover
1. Add to `docs/SESSION_HISTORY.md`
2. Create `docs/SESSION_HANDOVER_YYYY_MM_DD.md` if detailed
3. NEVER add session history to `CLAUDE.md`

### Log/Report Output
1. Save to `logs/`
2. Reference from relevant doc if needed

---

## CLAUDE.md Template

Keep `CLAUDE.md` structured like this:

```markdown
# CLAUDE.md
[1 line description]

## Quick Reference
[Status table - 5 rows max]

## Essential Rules
[3 rules max, each under 5 lines]

## Directory Structure
[Simple tree, 8 lines max]

## Progressive Documentation
[Link table - when to read what]

## Key Metadata Fields
[Bullet list - field names only]

## Slash Commands (Quick List)
[Category table - one-line per command]
```

**Target: 80-100 lines total**

---

## Detecting Bloat

### Signs CLAUDE.md is Bloated
- Exceeds 100 lines
- Contains session history
- Has detailed code examples
- Has "Recent Updates" section
- Duplicates info from other docs

### Signs Root is Bloated
- More than 5 markdown files
- Any `.log`, `.json`, `.txt` files
- Any Python scripts
- Session handover files
- Report files

### How to Fix Bloat

1. **Identify bloated content**
2. **Move to appropriate `docs/` file**
3. **Replace with one-line link** in `CLAUDE.md`
4. **Update `docs/SESSION_HISTORY.md`** with what was moved

---

## Reduction Achieved (Jan 2026)

| Metric | Before | After |
|--------|--------|-------|
| `CLAUDE.md` | ~450 lines | ~85 lines |
| `YAML_SAFEGUARDS.md` | ~320 lines | ~85 lines |
| Root files | 68 items | 5 files + directories |
| Initial context load | ~770 lines | ~170 lines |
| **Reduction** | - | **79%** |

---

## Why This Matters

1. **Token efficiency**: Every line in CLAUDE.md consumes tokens before work begins
2. **Focus**: Minimal context = clearer task understanding
3. **Maintainability**: Organized structure = easier updates
4. **Scalability**: Progressive loading = vault can grow without bloat

---

## Checklist for Future Sessions

Before ending a session, verify:

- [ ] No new files created in root directory
- [ ] `CLAUDE.md` still under 100 lines
- [ ] Session notes added to `docs/SESSION_HISTORY.md`
- [ ] New scripts in `PYTHON/`, not root
- [ ] New docs in `docs/`, not root
- [ ] Log outputs in `logs/`, not root

---

## Related Files

- [CLAUDE.md](../CLAUDE.md) - Main context file
- [YAML_SAFEGUARDS.md](../YAML_SAFEGUARDS.md) - YAML rules
- [LLM_CONTEXT.md](../LLM_CONTEXT.md) - Classification logic
- [SESSION_HISTORY.md](SESSION_HISTORY.md) - Past session notes
