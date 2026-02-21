# CLAUDE.md — CEI-Lit-WS Sub-Project Configuration

**Last Updated:** 2026-02-21

> Safety rules, vault structure, and utilities are in the **root CLAUDE.md** (auto-loaded).
> This file covers sub-project specifics only.

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
- `/download-pdf` — Download → Extract → Summarize workflow
- `/classify-papers` — Run classification pipeline
- `/enrich-paper` — Add metadata enrichment
- `/vault-stats` — Generate vault statistics
- `/identify-targets` — Find papers needing attention

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

## Documentation

**All documentation:** `docs/INDEX.md`
**Session history:** `docs/SESSION_HISTORY.md`
**Workflows:** `docs/WORKFLOWS.md`
**Git workflow:** `docs/GIT_WORKFLOW.md`

---

**Version:** 3.0 (Refactored 2026-02-21 — safety rules moved to root CLAUDE.md)
