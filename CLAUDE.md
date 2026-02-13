# CLAUDE.md - CEI Literature Vault Configuration

**Last Updated:** 2026-02-08

---

## System Context

**Role:** Academic Literature Database Manager for CEI Research
**Mission:** Classify, enrich, and maintain 846+ AI ethics papers
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
| Papers | 1,168 | `papers/` |
| PDFs | 1,115 | External (`PDFs/YYYY/`) |
| Extracts | 1,402 | `PDF Extracts/YYYY/` |
| Authors | 3,356 | `Authors/` |
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
**Reference:** `@_OPERATING-SYSTEM/Standards/file-safety.md`

### 2. YAML Safety (CRITICAL)
**Always use `PYTHON/yaml_frontmatter_utils.py`** for ALL YAML modifications.

```python
from PYTHON.yaml_frontmatter_utils import write_paper, validate_frontmatter
write_paper(filepath, frontmatter, body, validate=True)  # Validation mandatory
```

**Reference:** `@_OPERATING-SYSTEM/Standards/yaml-standards.md`

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
| **Classification** | `@_OPERATING-SYSTEM/Standards/classification-logic.md` |
| **YAML edits** | `@_OPERATING-SYSTEM/Standards/yaml-standards.md` |
| **PDF work** | `@_OPERATING-SYSTEM/Standards/pdf-processing.md` |
| **Author work** | `@_OPERATING-SYSTEM/Standards/author-management.md` |
| **File operations** | `@_OPERATING-SYSTEM/Standards/file-safety.md` |
| **API calls** | `@_OPERATING-SYSTEM/Standards/api-integration.md` |
| **Field reference** | `@_OPERATING-SYSTEM/Standards/paper-metadata-schema.md` |
| **Research** | `@_OPERATING-SYSTEM/Standards/research-standards.md` |

**Architecture:** See `@_OPERATING-SYSTEM/README.md`
**Recent Learnings:** See `@_OPERATING-SYSTEM/Learnings/learnings-log.md`

---

## Skills & Commands

**See:** `.claude/skills/` and `docs/COMMANDS.md` for full list.

**Quick reference:**
- `/download-pdf` - Download → Extract → Summarize workflow
- `/classify-papers` - Run classification pipeline
- `/enrich-paper` - Add metadata enrichment
- `/vault-stats` - Generate vault statistics
- `/qc-code` - Code quality check

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
**Session closure:** Use `/end-session` skill (orchestrates remember-thread → finalize-thread)

---

**Version:** 2.0 (Refactored with progressive disclosure architecture)
**Maintained by:** CEI Literature Vault AI Agents
