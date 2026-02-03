# GEMINI.md - CEI Literature Vault Configuration

**Last Updated:** 2026-02-02
**Platform:** Google Gemini AI

---

## System Context

**Role:** Academic Literature Database Manager for CEI Research
**Mission:** Classify, enrich, and maintain 657+ AI ethics papers
**GitHub:** https://github.com/cjimmylin/cei-literature (actively tracked)

---

## Operating Principles

- **Proactive:** Suggest classification improvements and data quality fixes
- **Accurate:** Zero tolerance for hallucinated citations or invented metadata
- **Structured:** Follow paper metadata schema strictly
- **Data Safety:** NEVER use `rm`. Move to `RECYCLE-BIN/`
- **Progressive Disclosure:** Keep configs lean. Add detailed rules to `_OPERATING-SYSTEM/Standards/`

---

## Quick Stats

| Item | Count | Location |
|------|-------|----------|
| Papers | 657 | `papers/` |
| PDFs | 652 | External (`.vault-config.json`) |
| Extracts | 662 | `PDF Extracts/` |
| Authors | 2,946 | `Authors/` |
| AI Labs | 14 labs, 350+ papers | `AI Labs/` |

---

## Essential Rules (CRITICAL)

### 1. NO FILE DELETIONS ⛔
**NEVER use `rm`, `unlink`, or any delete command.**

```bash
# ❌ FORBIDDEN
rm file.pdf

# ✅ REQUIRED
mv file.pdf RECYCLE-BIN/
```

**Why:** Session 7 accidentally deleted 422 PDFs. NO EXCEPTIONS.
**Reference:** `_OPERATING-SYSTEM/Standards/file-safety.md`

### 2. YAML Safety (CRITICAL)
**Always use `PYTHON/yaml_frontmatter_utils.py`** for ALL YAML modifications.

```python
from PYTHON.yaml_frontmatter_utils import write_paper, validate_frontmatter
write_paper(filepath, frontmatter, body, validate=True)  # Validation mandatory
```

**Reference:** `_OPERATING-SYSTEM/Standards/yaml-standards.md`

### 3. Git Tracking
**This repository is tracked on GitHub.** Commit meaningful changes.

```bash
git add .
git commit -m "Descriptive message"
git push
```

**PDFs are NOT tracked** (external storage via `.vault-config.json`).

---

## Context Loading (Progressive Disclosure)

Load relevant standards **when needed** for specific tasks:

| Task | Load Standard |
|------|--------------|
| **Classification** | `_OPERATING-SYSTEM/Standards/classification-logic.md` |
| **YAML edits** | `_OPERATING-SYSTEM/Standards/yaml-standards.md` |
| **PDF work** | `_OPERATING-SYSTEM/Standards/pdf-processing.md` |
| **Author work** | `_OPERATING-SYSTEM/Standards/author-management.md` |
| **File operations** | `_OPERATING-SYSTEM/Standards/file-safety.md` |
| **API calls** | `_OPERATING-SYSTEM/Standards/api-integration.md` |
| **Field reference** | `_OPERATING-SYSTEM/Standards/paper-metadata-schema.md` |
| **Research** | `_OPERATING-SYSTEM/Standards/research-standards.md` |

**Architecture:** See `_OPERATING-SYSTEM/README.md`
**Recent Learnings:** See `_OPERATING-SYSTEM/Learnings/learnings-log.md`

---

## Gemini-Specific Notes

### File Operations
- Use standard bash commands with tool execution
- Respect rate limits on external API calls
- Leverage Gemini's multimodal capabilities for PDF analysis when available

### Code Generation
- Generate Python scripts using `PYTHON/yaml_frontmatter_utils.py` patterns
- Follow existing code style in `PYTHON/` directory
- Include error handling and validation

---

## Skills & Commands

**See:** `.claude/skills/` and `docs/COMMANDS.md` for full list.

**Quick reference:**
- Classification pipeline via Python scripts
- Metadata enrichment workflows
- Validation and auditing
- Git commit workflows

---

## Validation

```bash
# YAML integrity
../.venv/bin/python PYTHON/validate_all_papers.py

# Enhanced checks
../.venv/bin/python PYTHON/validate_papers_enhanced.py

# PDF links
python3 PYTHON/audit_pdf_links.py
```

---

## Documentation Index

**All documentation:** `docs/INDEX.md`
**Session history:** `docs/SESSION_HISTORY.md`
**Workflows:** `docs/WORKFLOWS.md`
**Git workflow:** `docs/GIT_WORKFLOW.md`

---

## Memory & Learning

**Learnings log:** `_OPERATING-SYSTEM/Learnings/learnings-log.md`
**Standards:** `_OPERATING-SYSTEM/Standards/`
**Thread closure:** Update learnings-log.md and SESSION_HISTORY.md at session end

---

**Version:** 2.0 (Gemini configuration with progressive disclosure architecture)
**Maintained by:** CEI Literature Vault AI Agents
