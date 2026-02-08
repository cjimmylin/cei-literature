# Knowledge Index: CEI Literature Vault
**Last Updated**: January 24, 2026
**For**: Future LLM sessions, developers, and AI assistants

---

## Quick Start for New Sessions

### 🎯 First Time Here?

Read these in order:
1. `README.md` - Vault overview
2. `CLAUDE.md` - How to work with Claude Code
3. `YAML_SAFEGUARDS.md` - Critical YAML rules (Jan 2026 learnings)
4. `DEVELOPER_PLAYBOOK.md` - How to write safe scripts
5. `LLM_CONTEXT.md` - Classification system

**Time investment**: ~30 minutes for complete context

### 🔧 Need to Modify Paper Metadata?

1. Read `DEVELOPER_PLAYBOOK.md` (5 min)
2. Choose a template from "Script Templates" section
3. Follow the pattern exactly
4. Test on sample papers first
5. Use validation commands to verify

### 🐛 Found a YAML Issue?

1. Run: `python3 PYTHON/yaml_frontmatter_utils.py papers/problematic_paper.md`
2. Read the issue description
3. Check `YAML_SAFEGUARDS.md` "Common Pitfalls" section
4. Use utilities library to fix
5. Validate result

### 📚 Want to Understand the Classification System?

1. Read `LLM_CONTEXT.md` sections 2-7
2. Check the specific script mentioned (e.g., `classify_ethics.py`)
3. Review keywords for each category
4. Look at example papers in each category

---

## Document Map

### Core Architecture Documents
| Document | Purpose | For Whom |
|----------|---------|----------|
| `README.md` | Vault overview, structure, scripts | Everyone |
| `CLAUDE.md` | Claude Code-specific guidance | Claude Code users |
| `LLM_CONTEXT.md` | Classification logic and standards | Anyone modifying metadata |

### YAML & Code Quality (Jan 2026)
| Document | Purpose | For Whom |
|----------|---------|----------|
| `YAML_SAFEGUARDS.md` | **[CRITICAL]** YAML standards and prevention | All developers |
| `DEVELOPER_PLAYBOOK.md` | **[CRITICAL]** How-to guide for safe scripts | All developers |
| `SESSION_LEARNING_2026_01_24.md` | How the fix was designed and executed | Research/understanding |
| `FIX_SUMMARY_2026_01_24.md` | What was fixed and verification results | Reference/history |
| `KNOWLEDGE_INDEX.md` | This file - navigation guide | Everyone |

### Utility Library
| File | Purpose |
|------|---------|
| `PYTHON/yaml_frontmatter_utils.py` | **[REQUIRED]** Safe YAML operations library |
| `PYTHON/fix_yaml_tags.py` | Fix script for orphaned tags (reference) |

### Scripts & Tools
| Directory | Purpose |
|-----------|---------|
| `PYTHON/` | Classification, report generation, utilities |
| `.agent/` | Skills for PDF processing, research, classification |
| `.claude/` | Claude Code commands and workflows |
| `STATISTICS/` | Generated reports (auto-generated) |
| `papers/` | Individual paper markdown files (580 papers) |

### Configuration & Data
| File | Purpose |
|------|---------|
| `Base.md` | CSV export from Zotero (primary data source) |
| `.obsidian/` | Obsidian vault configuration |

---

## How to Find Answers

### "I need to add a new field to all papers"
→ Read: `DEVELOPER_PLAYBOOK.md` → Task 1: Add New Field

### "I got a YAML error, how do I fix it?"
→ Read: `YAML_SAFEGUARDS.md` → "Common Pitfalls" OR
→ Run: `python3 PYTHON/yaml_frontmatter_utils.py <paper>`

### "How does the classification system work?"
→ Read: `LLM_CONTEXT.md` → Sections 2-7

### "What was fixed in January 2026?"
→ Read: `FIX_SUMMARY_2026_01_24.md` (summary) OR
→ Read: `SESSION_LEARNING_2026_01_24.md` (detailed)

### "How do I write a script that modifies papers?"
→ Read: `DEVELOPER_PLAYBOOK.md` → "Script Templates"

### "What's the complete reference for YAML operations?"
→ Read: `YAML_SAFEGUARDS.md` → Complete technical guide

### "I want to understand how the fix was developed"
→ Read: `SESSION_LEARNING_2026_01_24.md` → "Learnings" section

### "How do I validate my changes?"
→ Read: `DEVELOPER_PLAYBOOK.md` → "Testing & Validation" section

---

## Navigation by Role

### 👨‍💻 Developers

**Essential reading**:
1. `YAML_SAFEGUARDS.md` (critical standards)
2. `DEVELOPER_PLAYBOOK.md` (how-to guide)
3. `PYTHON/yaml_frontmatter_utils.py` (API reference)

**When you write code**:
- Use the templates in DEVELOPER_PLAYBOOK.md
- Always validate before writing
- Test on samples first

**Key utilities**:
```python
from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter, write_paper, validate_frontmatter
)
```

### 🤖 LLM Sessions

**First session?**
1. Read: `README.md` (5 min)
2. Read: `CLAUDE.md` (5 min)
3. Read: `DEVELOPER_PLAYBOOK.md` (10 min)
4. Skim: `LLM_CONTEXT.md` (5 min)

**Modifying papers?**
1. Check: Does your task involve YAML?
2. If yes → Read: `YAML_SAFEGUARDS.md`
3. Use: `DEVELOPER_PLAYBOOK.md` templates
4. Test: On sample papers first
5. Validate: Using utilities library

**Troubleshooting?**
1. Error message → Search this file for key words
2. Run utilities diagnostic
3. Check `YAML_SAFEGUARDS.md` "Common Pitfalls"
4. Check `DEVELOPER_PLAYBOOK.md` "Troubleshooting"

### 📊 Researchers

**Understanding the vault**:
1. `README.md` - Overview
2. `LLM_CONTEXT.md` - Classification logic
3. `STATISTICS/` - Reports (auto-generated)

**Using classification data**:
- Papers organized by ethics/topic/cultural values
- See `STATISTICS/20260119-paper-statistics-1.md` for overview
- Use Obsidian graph view to see relationships

**Regenerating reports**:
```bash
python3 .agent/skills/generate_reports/scripts/run_reports.py
```

### 📚 Maintainers

**Regular tasks**:
1. Update papers (import from Zotero)
2. Run classification pipeline
3. Generate reports
4. Monitor YAML integrity

**Monthly**:
- Backup papers directory
- Check for any YAML issues: `for f in papers/*.md; do python3 PYTHON/yaml_frontmatter_utils.py "$f" 2>&1 | grep -i error && echo "$f"; done`
- Run: `python3 .agent/skills/generate_reports/scripts/run_reports.py`

**When modifying scripts**:
- Use `DEVELOPER_PLAYBOOK.md` standards
- Test thoroughly
- Update `PYTHON/README.md` documentation
- Add entry to this knowledge index if new

---

## Critical YAML Rules (Mandatory)

**These rules prevent data corruption. Violate at your peril.**

### Rule 1: Always Use Utilities Library
```python
# ✅ CORRECT
from PYTHON.yaml_frontmatter_utils import extract_frontmatter, write_paper
fm, body = extract_frontmatter(content)
write_paper(filepath, fm, body, validate=True)

# ❌ WRONG
content = content.replace('old', 'new')  # Dangerous!
```

### Rule 2: Validate Before Writing
```python
# ✅ CORRECT
is_valid, issues = validate_frontmatter(fm)
if not is_valid:
    raise ValueError(f"YAML invalid: {issues}")
write_paper(filepath, fm, body, validate=True)

# ❌ WRONG
filepath.write_text(new_content)  # No validation!
```

### Rule 3: Proper YAML Closing Marker
```python
# ✅ CORRECT
content = f"---\n{frontmatter}\n---\n{body}"

# ❌ WRONG
content = f"---\n{frontmatter}---"  # Missing newlines!
```

### Rule 4: No Orphaned List Items
```yaml
# ✅ CORRECT
tags:
  - TagOne
  - TagTwo

# ❌ WRONG
pdf: "..."
  - TagOne  # No parent key!
```

### Rule 5: String vs List Formats
```yaml
# ✅ CORRECT
newtags: "Tag1, Tag2"    # String (comma-separated)
tags:                    # List
  - Tag1
  - Tag2

# ❌ WRONG
newtags:                 # Should be string!
  - Tag1
  - Tag2
```

---

## Quick Reference: Common Commands

### Validation
```bash
# Single paper
python3 PYTHON/yaml_frontmatter_utils.py papers/2016-Amodei-Concrete.md

# Find all broken papers
for f in papers/*.md; do
    python3 PYTHON/yaml_frontmatter_utils.py "$f" 2>&1 | grep -q "Issue" && echo "❌ $f"
done
```

### Counting
```bash
# Total papers
find papers -name "*.md" | wc -l

# Papers with tags section
grep -l "^tags:" papers/*.md | wc -l

# Papers with orphaned items
grep -n "^  - [a-zA-Z]" papers/*.md | wc -l
```

### Generation
```bash
# All reports
python3 .agent/skills/generate_reports/scripts/run_reports.py

# Specific report
python3 PYTHON/generate_stats.py
```

---

## History: What Changed in January 2026

### The Problem
- 530 papers had corrupted YAML with orphaned list items
- Obsidian properties panel couldn't display metadata
- Root cause: Scripts writing YAML incorrectly

### The Fix
- Created utilities library: `yaml_frontmatter_utils.py`
- Fixed 3 problematic scripts
- Implemented validation system
- Fixed all 530 papers

### Prevention
- Centralized utilities library (required for all YAML work)
- Comprehensive documentation
- Developer playbook with templates
- Mandatory validation before writes

### Files Added
- `PYTHON/yaml_frontmatter_utils.py`
- `YAML_SAFEGUARDS.md`
- `DEVELOPER_PLAYBOOK.md`
- `SESSION_LEARNING_2026_01_24.md`
- `FIX_SUMMARY_2026_01_24.md`

### Scripts Fixed
- `.agent/skills/extract_pdf_text/scripts/extract.py`
- `.agent/skills/download_pdf/scripts/download.py`
- `PYTHON/add_newtags.py`

---

## How to Keep This Knowledge Up-to-Date

### For Future Sessions
When you complete significant work on this vault:
1. **Document learnings** in a new `SESSION_LEARNING_YYYY_MM_DD.md` file
2. **Update** relevant sections of this Knowledge Index
3. **Update** related documents (README, LLM_CONTEXT, etc.)
4. **Create playbooks** if you develop new patterns or techniques

### Template for Session Learning
```markdown
# Session Learning Documentation
**Date**: YYYY-MM-DD
**Task**: [What you did]
**Status**: [Complete/Ongoing]

## What Accomplished
[Summary of work]

## Key Learnings
[What you learned]

## How to Replicate
[Steps for next session]

## Files Changed
[List of modified/created files]

## Recommendations for Future Work
[What should be done next]
```

### When to Update This Index
- Add new document → Add to Document Map
- Fix new issue → Add to "How to Find Answers"
- Add new process → Add to role-specific section
- Discover new pattern → Add to Critical Rules

---

## Support & Troubleshooting

### "I don't understand the classification system"
→ Read: `LLM_CONTEXT.md` section 2-7
→ Check: Example papers in each category

### "I broke something with my script"
→ Check: Did you follow `DEVELOPER_PLAYBOOK.md`?
→ Run: `python3 PYTHON/yaml_frontmatter_utils.py <affected_paper>`
→ Restore: From backup if needed
→ Read: Relevant section of troubleshooting guide

### "I need to audit all scripts"
→ Script Audit Pattern in `DEVELOPER_PLAYBOOK.md`
→ Check: All scripts use utilities library
→ Verify: Validation calls present

### "I want to contribute/extend this"
→ Read: This Knowledge Index (you're here!)
→ Read: Relevant documentation for your task
→ Follow: Template patterns from playbooks
→ Document: Your work for future sessions

---

## Related Documents (External)

These documents provide additional context but aren't strictly necessary:
- `LLM_CONTEXT.md` - Classification logic details
- `PYTHON/README.md` - Individual script documentation
- `.claude/` - Claude Code skills and commands

---

## Checksum for Health

To verify vault health, run:
```bash
#!/bin/bash
echo "=== CEI Literature Vault Health Check ==="
echo "Papers: $(find papers -name "*.md" | wc -l)"
echo "Valid YAML: $(grep -l "^tags:" papers/*.md | wc -l)"
echo "YAML Issues: $(for f in papers/*.md; do python3 PYTHON/yaml_frontmatter_utils.py "$f" 2>&1 | grep -c "Issue"; done | paste -sd+ | bc)"
echo "Latest reports: $(ls -t STATISTICS/*.md | head -1 | xargs ls -la)"
```

---

**Version**: 1.0
**Last Updated**: January 24, 2026
**Maintained by**: CEI Vault Team & LLM Sessions
**Next Review**: February 2026

Questions? Check this index, then consult the relevant document.
