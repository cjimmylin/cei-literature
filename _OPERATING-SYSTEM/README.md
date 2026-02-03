# _OPERATING-SYSTEM - CEI Literature Vault Architecture

**Version:** 1.0
**Created:** 2026-02-02
**Purpose:** Centralized memory, learning, and standards system for the CEI Literature Vault

---

## Overview

The `_OPERATING-SYSTEM/` directory implements a **progressive disclosure** architecture inspired by LifeOS-Agent-Vault. Instead of massive configuration files (2,000+ lines), we maintain:

1. **Lean configs** (<80 lines) that point to detailed standards
2. **Temporal memory** (learnings log) that captures session-specific knowledge
3. **Timeless standards** (procedures, rules) that remain stable
4. **Reusable templates** for consistent data entry

This architecture reduces cognitive load for AI agents while ensuring critical knowledge persists across sessions and platforms (Claude, Gemini, OpenAI).

---

## Directory Structure

```
_OPERATING-SYSTEM/
├── README.md                   # This file
├── Learnings/
│   └── learnings-log.md        # Timestamped discoveries, edge cases, improvements
├── Standards/                  # Single source of truth for procedures
│   ├── classification-logic.md      # Ethics framework, cultural classification
│   ├── yaml-standards.md            # YAML frontmatter safety rules
│   ├── file-safety.md               # NO DELETIONS rule, RECYCLE-BIN usage
│   ├── paper-metadata-schema.md     # YAML field reference
│   ├── api-integration.md           # arXiv, Semantic Scholar patterns
│   ├── author-management.md         # Name validation, enrichment
│   ├── pdf-processing.md            # Download, extraction workflows
│   └── research-standards.md        # Paper discovery, verification
└── Templates/
    ├── paper-template.md
    └── author-template.md
```

---

## Philosophy: Progressive Disclosure

### Problem: Config File Bloat
Traditional agent configs grow unwieldy:
- `LLM_CONTEXT.md`: 2,090 lines (hard to navigate)
- `CLAUDE.md`: ~180 lines (mixed concerns)
- Knowledge buried, not findable

### Solution: Context Loading on Demand
1. **Agent configs** (CLAUDE.md, GEMINI.md, OPENAI.md) contain only:
   - Role definition
   - Core principles
   - **Pointers to Standards/** for detailed rules
2. **Standards/** files are loaded when needed:
   - Working on classification? Load `Standards/classification-logic.md`
   - Editing YAML? Load `Standards/yaml-standards.md`
3. **Learnings/** capture temporal knowledge that gets archived

**Analogy:** IDE with "Go to Definition" vs. one massive file.

---

## 4-Layer Memory Architecture

### Layer 1: Learnings Log (Temporal)
**File:** `Learnings/learnings-log.md`
**Purpose:** Capture session-specific discoveries
**Lifecycle:** Archive annually (learnings-log-2026.md)

**Categories:**
- Classification (ethics frameworks, edge cases)
- YAML (corruption patterns, fixes)
- API (rate limits, error handling)
- PDF Processing (download sources, extraction)
- Author Management (name validation)
- Data Quality (audits, integrity checks)
- Skills (workflow improvements)
- Workflows (batch operations)
- Git (commit patterns, GitHub integration)

**Format:** Table-based with category index for quick navigation.

**Update via:** `/remember-thread` skill or manual entry

### Layer 2: Standards (Timeless)
**Directory:** `Standards/`
**Purpose:** Single source of truth for procedures
**Lifecycle:** Stable, updated only when procedures change

**8 Core Standards:**
1. **classification-logic.md** - 7-stage pipeline, framework detection
2. **yaml-standards.md** - Mandatory `yaml_frontmatter_utils.py` usage
3. **file-safety.md** - NO DELETIONS rule (Session 7: 422 PDFs lost)
4. **paper-metadata-schema.md** - Field definitions
5. **api-integration.md** - External API patterns
6. **author-management.md** - Profile validation
7. **pdf-processing.md** - Download/extract workflows
8. **research-standards.md** - Discovery methodology

### Layer 3: Skills (Workflows)
**Directory:** `.claude/skills/`, `.agent/skills/`
**Purpose:** Executable workflows and automation
**Examples:** classify-papers, enrich-paper, remember-thread

### Layer 4: Configuration (Agent Settings)
**Files:** `CLAUDE.md`, `GEMINI.md`, `OPENAI.md`
**Purpose:** Agent-specific settings with pointers to Layers 1-2
**Target:** <80 lines each

---

## Usage Patterns

### For AI Agents

**Starting a session:**
1. Load relevant config (CLAUDE.md, GEMINI.md, OPENAI.md)
2. Review `Learnings/learnings-log.md` for recent discoveries
3. Load specific Standards/ files as needed:
   ```markdown
   # In CLAUDE.md
   ## Context Loading
   - Classification: @_OPERATING-SYSTEM/Standards/classification-logic.md
   - YAML edits: @_OPERATING-SYSTEM/Standards/yaml-standards.md
   ```

**During work:**
- Consult Standards/ when uncertain about procedures
- Note edge cases for addition to learnings-log.md

**Ending a session:**
- Run `/end-session` skill (orchestrates remember-thread → finalize-thread)
- Updates learnings-log.md, SESSION_HISTORY.md, Standards/ if needed

### For Humans

**Adding learnings:**
Use `/establishing-learning` skill or edit `Learnings/learnings-log.md` manually.

**Updating standards:**
Edit Standards/ files directly. These are versioned in git.

**Creating new standards:**
1. Create Standards/new-standard.md
2. Update this README.md
3. Add pointer in CLAUDE.md, GEMINI.md, OPENAI.md

---

## Anti-Bloat Safeguards

### File Size Limits
| File Type | Max Lines | Action if Exceeded |
|-----------|-----------|-------------------|
| Config files (CLAUDE.md etc.) | 80 | Extract to Standards/ |
| Standards files | 150 | Split into sub-files |
| Learnings sections | 200/year | Archive old years |
| Skill docs | 60 | Reference Standards/ |

### Quarterly Maintenance
Run `/quarterly-maintenance` skill to:
1. Audit config file sizes
2. Move accumulated content to Standards/
3. Archive old learnings (>1 year)
4. Validate cross-references
5. Check for broken links

---

## Migration from Old System

### Before _OPERATING-SYSTEM/ (Pre-2026-02-02)
- Knowledge scattered across LLM_CONTEXT.md (2,090 lines)
- YAML_SAFEGUARDS.md separate from other standards
- Session learnings lost between conversations
- No systematic closure workflow

### After _OPERATING-SYSTEM/
- Learnings persist in learnings-log.md
- Standards centralized and findable
- Config files lean (<80 lines)
- Systematic closure via /end-session

### Backward Compatibility
- LLM_CONTEXT.md remains as backup
- YAML_SAFEGUARDS.md marked deprecated, points to Standards/yaml-standards.md
- Existing skills continue to work
- Gradual migration of knowledge to new structure

---

## Related Documentation

- **Session History:** `docs/SESSION_HISTORY.md` (detailed session records)
- **Workflows:** `docs/WORKFLOWS.md` (multi-step procedures)
- **Commands:** `docs/COMMANDS.md` (skill reference)
- **Index:** `docs/INDEX.md` (vault navigation)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial _OPERATING-SYSTEM/ structure created |

---

**Maintained by:** CEI Literature Vault AI Agents
**Questions?** See `docs/OPERATING_SYSTEM_MIGRATION.md` for implementation details
