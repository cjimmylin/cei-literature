# 🚀 START HERE
**For**: New LLM sessions, future developers
**Updated**: January 24, 2026
**Time**: 2 minutes to read

---

## Current Vault Status ✅

**Status:** Production-ready, fully operational

| Component | Count | Status |
|-----------|-------|--------|
| Papers | 580 | ✅ Complete |
| PDFs | 396 (68%) | ✅ Indexed |
| PDF Extracts | 396 | ✅ Searchable (.md format) |
| Abstracts | 454 (78%) | ✅ Enriched |
| YAML Validity | 100% | ✅ All validated |
| Author Profiles | 2,766+ | ✅ Created |
| Benchmarks | 231 | ✅ Classified |
| Evaluations | 350 | ✅ Classified |
| Datasets | 273 | ✅ Classified |

---

## Where Am I?

You're in the **CEI Literature Vault** - a curated collection of 580 academic papers on AI ethics and safety, enriched with classification metadata.

**Quick Stats**:
- 580 papers with full YAML metadata
- 396 PDFs extracted to searchable markdown
- Organized by ethics frameworks, topics, cultural values
- All searchable in Obsidian

---

## What's Complete?

| Task | Status |
|------|--------|
| YAML corruption fixed | ✅ 580/580 papers valid |
| PDF extraction to Markdown | ✅ 396 files searchable |
| Author metadata complete | ✅ 2,766+ profiles |
| Classification pipeline | ✅ All 7 stages run |
| Statistics reports | ✅ All 4 reports current |
| Safety documentation | ✅ Complete |

**Known Limitations:**
- 38 papers have abbreviated author lists → `AUTHOR_LOOKUP_RESEARCH_TASKS.md`
- 184 papers lack local PDFs (paywalled sources)

---

## The Most Important Rule

**NEVER write YAML directly.** Always:
```python
from PYTHON.yaml_frontmatter_utils import write_paper
write_paper(filepath, frontmatter, body, validate=True)
```

---

## Read These First (In Order)

1. **This file** (you're reading it now) - 2 min
2. **`KNOWLEDGE_INDEX.md`** - Quick nav guide - 5 min
3. **`DEVELOPER_PLAYBOOK.md`** - If you'll code - 15 min
4. **`YAML_SAFEGUARDS.md`** - If you need rules - 10 min

Total: **30 minutes** to be ready to work

---

## Quick Answers

### "I need to modify paper metadata"
→ Read: `DEVELOPER_PLAYBOOK.md` → Copy a template → Modify only the logic part

### "YAML error - what do I do?"
→ Run: `python3 PYTHON/yaml_frontmatter_utils.py papers/problemname.md`
→ Read: Error message
→ Check: `YAML_SAFEGUARDS.md` common pitfalls

### "How do I...?"
→ Check: `KNOWLEDGE_INDEX.md` → "How to Find Answers"

### "I want to understand everything"
→ Read: `SESSION_ARTIFACTS_2026_01_24.md` → Then dive into specific docs

---

## Files You'll Need

### Always Reference
- `PYTHON/yaml_frontmatter_utils.py` - The utilities library (USE THIS!)
- `YAML_SAFEGUARDS.md` - The rules
- `DEVELOPER_PLAYBOOK.md` - The how-to guide

### For Context
- `KNOWLEDGE_INDEX.md` - Navigation
- `SESSION_LEARNING_2026_01_24.md` - How this was done
- `LLM_CONTEXT.md` - Classification system

### For Information
- `README.md` - Vault overview
- `CLAUDE.md` - Claude Code instructions
- `STATISTICS/` - Generated reports

---

## Three Quick Tests

### Test 1: Validate all YAML
```bash
python3 PYTHON/validate_all_papers.py
# Should show: "Valid papers: 580/580" and "0 errors"
```

### Test 2: Check PDF extracts
```bash
ls "PDF Extracts"/*.md | wc -l
# Should show: 396
```

### Test 3: All papers present?
```bash
ls papers/*.md | wc -l
# Should show: 580
```

If all three pass → Everything is working ✅

---

## The Golden Rules

```
✅ DO:
  - Use utilities library for all YAML operations
  - Validate before writing
  - Test on samples first
  - Follow playbook templates
  - Document your changes

❌ DON'T:
  - Use regex on YAML directly
  - Concatenate YAML strings manually
  - Write without validation
  - Forget newlines in closing markers
  - Create orphaned list items
```

---

## When to Do What

### "I'm a developer/AI session"
1. Read: `DEVELOPER_PLAYBOOK.md` (15 min)
2. Use: Templates from that file
3. Test: On sample papers first
4. Validate: Before running on all papers

### "I'm a researcher"
1. Read: `README.md` + `LLM_CONTEXT.md`
2. Use: Obsidian to browse papers
3. Check: STATISTICS/ for reports
4. Run: `python3 .agent/skills/generate_reports/scripts/run_reports.py`

### "I'm maintaining this"
1. Read: `KNOWLEDGE_INDEX.md`
2. Monthly: Check YAML health
3. Backups: Keep recent backups
4. Documentation: Update when you learn something new

---

## Key Concepts in 60 Seconds

**YAML Frontmatter**: Metadata at top of each paper markdown file
```yaml
---
key: "value"
list_field:
  - item1
  - item2
---
```

**The Problem**: Scripts wrote bad YAML that broke Obsidian
**The Solution**: Utilities library + mandatory validation
**The Prevention**: This documentation + playbook templates

---

## Next Steps

Pick your path:

### Path A: I just want to understand (30 min)
1. Read `KNOWLEDGE_INDEX.md`
2. Skim `SESSION_ARTIFACTS_2026_01_24.md`
3. Bookmark `YAML_SAFEGUARDS.md` for reference
4. You're ready to use the system

### Path B: I need to write scripts (45 min)
1. Read `DEVELOPER_PLAYBOOK.md`
2. Read `YAML_SAFEGUARDS.md`
3. Copy a template
4. Test on sample papers
5. You're ready to code

### Path C: I want to understand deeply (2 hours)
1. Read this file
2. Read `KNOWLEDGE_INDEX.md`
3. Read `DEVELOPER_PLAYBOOK.md`
4. Read `SESSION_LEARNING_2026_01_24.md`
5. Review `PYTHON/yaml_frontmatter_utils.py`
6. You understand the full system

---

## Emergency: YAML Corruption Found

Don't panic. Here's what to do:

```bash
# 1. Find the problem
python3 PYTHON/yaml_frontmatter_utils.py papers/problem_paper.md

# 2. Understand it
# Read the error message, check YAML_SAFEGUARDS.md "Common Pitfalls"

# 3. Have a backup?
# If you made a backup before your script, restore it

# 4. Use the fix
# See: DEVELOPER_PLAYBOOK.md "Troubleshooting"

# 5. Ask for help
# Check: YAML_SAFEGUARDS.md "Migration & Cleanup" section
```

The utilities library was designed exactly for this scenario.

---

## One More Time: The Rules

Copy this to your mental RAM:

1. **Import utilities**: `from PYTHON.yaml_frontmatter_utils import ...`
2. **Extract safely**: `fm, body = extract_frontmatter(content)`
3. **Validate before writing**: `validate_frontmatter(fm)` must pass
4. **Write safely**: `write_paper(filepath, fm, body, validate=True)`
5. **Test on samples**: Always test on 1-2 papers before batch operations

That's it. Follow that 5-step pattern and you'll never corrupt YAML.

---

## You're Ready! 🚀

- ✅ You understand what happened
- ✅ You know where to find things
- ✅ You know the golden rules
- ✅ You can read the documentation

**Pick a task and go.** Everything is documented.

---

## Questions?

| Question | Answer |
|----------|--------|
| Where's the navigation? | `KNOWLEDGE_INDEX.md` |
| How do I write code? | `DEVELOPER_PLAYBOOK.md` |
| What are the YAML rules? | `YAML_SAFEGUARDS.md` |
| What was the problem? | `FIX_SUMMARY_2026_01_24.md` |
| How was it solved? | `SESSION_LEARNING_2026_01_24.md` |
| How do I get started? | You're reading it! 👋 |

---

**Time to proceed**: Now ✅
**Status**: Ready for work
**Contact**: Follow the docs for answers

Good luck! 🎯
