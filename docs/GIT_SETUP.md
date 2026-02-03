# Git Repository Setup

**Date**: February 2, 2026
**Status**: ✅ CONFIGURED - PDFs Protected from GitHub Sync

## Repository Structure

```
/Users/jimmy.lin/Documents/CEI-Literature-Vault/
├── .gitignore                 # ROOT: Protects PDF directories
├── PDFs/                      # ✅ NOT TRACKED (652 files, external)
├── AI-Lab-PDFs/               # ✅ NOT TRACKED (392 files, external)
└── CEI-Lit-WS/                # ✅ TRACKED (Git repository)
    ├── .git/                  # Git repository (initialized)
    ├── .gitignore             # WORKSPACE: Ignores stub PDFs, logs, config
    ├── papers/                # Tracked (metadata only)
    ├── PDF Extracts/          # Tracked (markdown files)
    ├── AI Labs/               # Tracked (markdown/README files)
    │   └── **/*.pdf           # ✅ IGNORED (4 stub files)
    ├── PYTHON/                # Tracked (scripts)
    ├── docs/                  # Tracked (documentation)
    └── ...                    # All other workspace files tracked
```

## Protection Layers

### Layer 1: Git Scope (Primary Protection)
**Repository location**: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/`

Git only tracks files **within** the repository directory. The PDF directories are outside:
- `PDFs/` is at `../PDFs/` (parent directory)
- `AI-Lab-PDFs/` is at `../AI-Lab-PDFs/` (parent directory)

Git cannot see or track files outside its repository boundary.

### Layer 2: Workspace .gitignore (Secondary Protection)
**File**: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/.gitignore`

Ignores stub PDFs within the workspace:
```gitignore
# AI Labs PDFs (stub files - actual PDFs are in external AI-Lab-PDFs directory)
AI Labs/**/*.pdf
```

**Result**: 4 stub PDF files in `AI Labs/` are ignored.

### Layer 3: Root .gitignore (Safety Net)
**File**: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.gitignore`

If someone accidentally initializes a Git repo at the vault root, this protects:
```gitignore
PDFs/
AI-Lab-PDFs/
.venv/
.agent/
```

## Verification Results

✅ **All protections working correctly:**

1. **Git repository scope**:
   ```bash
   # Repository is in workspace only
   ls -la CEI-Lit-WS/.git  # ✅ Exists
   ls -la .git             # ✅ Does not exist (not at root)
   ```

2. **PDF directories not visible to Git**:
   ```bash
   cd CEI-Lit-WS
   git status | grep "PDFs/"         # ✅ Not listed
   git status | grep "AI-Lab-PDFs/"  # ✅ Not listed
   ```

3. **Stub PDFs ignored**:
   ```bash
   git check-ignore "AI Labs/Anthropic/Papers/Claude_Character_2024.pdf"
   # ✅ Returns: .gitignore:22:AI Labs/**/*.pdf
   ```

4. **Untracked files count**:
   - Total untracked files: 20 (workspace files only)
   - PDF directories: 0 (not visible to Git)
   - Stub PDFs: 0 (ignored by .gitignore)

## GitHub Sync Workflow

When you push to GitHub:

1. **Only workspace files are synced**:
   - Paper metadata (657 YAML files)
   - PDF extracts (662 markdown files)
   - Python scripts
   - Documentation
   - AI Labs markdown files

2. **Never synced**:
   - 652 PDFs in `PDFs/`
   - 392 PDFs in `AI-Lab-PDFs/`
   - 4 stub PDFs in workspace
   - Local config (`.vault-config.json`)
   - Log files

3. **Repository size**:
   - With protections: ~50-100 MB (text files only)
   - Without protections: ~1.5 GB (would include PDFs)

## Initial GitHub Setup

```bash
# 1. Add remote
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS
git remote add origin <your-github-repo-url>

# 2. Stage files
git add .

# 3. Verify PDFs are NOT staged
git status | grep -i pdf
# Should return nothing (all PDFs ignored)

# 4. Commit
git commit -m "Initial commit: CEI Literature Vault workspace"

# 5. Push to GitHub
git push -u origin main
```

## What Gets Tracked vs Not Tracked

### ✅ Tracked (Will Sync to GitHub)
- YAML frontmatter & markdown content in `papers/`
- Markdown extracts in `PDF Extracts/`
- Python scripts in `PYTHON/`
- Documentation in `docs/`
- Markdown files in `AI Labs/`
- README, CLAUDE.md, requirements.txt
- Statistics and reports

### ❌ Not Tracked (Will NOT Sync)
- **PDFs** (all 1,048 binary PDF files)
- `.vault-config.json` (user-specific paths)
- Log files (`logs/*.json`, `logs/*.log`)
- Python cache (`__pycache__/`, `*.pyc`)
- OS files (`.DS_Store`)
- Temporary files (`*.tmp`, `*.bak`)

## Backup Strategy

Since PDFs are not in GitHub:

1. **Workspace (GitHub)**: Automatically backed up via Git
2. **PDFs**: Require separate backup solution
   - `PDFs/` - 652 files (~800 MB)
   - `AI-Lab-PDFs/` - 392 files (~500 MB)
   
Recommended: Use Time Machine, cloud storage, or external drive for PDF directories.

## Safety Checklist

Before pushing to GitHub:

- [ ] Git repository is in `CEI-Lit-WS/` (not vault root)
- [ ] `.gitignore` files exist at both workspace and root
- [ ] Run `git status` and verify no `.pdf` files listed
- [ ] Check repository size: should be <100 MB
- [ ] Verify `.vault-config.json` is ignored (contains user paths)

## Troubleshooting

**If PDFs appear in `git status`**:
```bash
# Check which .gitignore is active
git check-ignore -v "AI Labs/Anthropic/Papers/somefile.pdf"

# Force Git to respect .gitignore
git rm --cached "AI Labs/**/*.pdf"
git rm --cached -r PDFs/ AI-Lab-PDFs/  # If accidentally tracked
```

**If repository is at wrong level**:
```bash
# Remove Git from vault root (if accidentally initialized there)
rm -rf /Users/jimmy.lin/Documents/CEI-Literature-Vault/.git

# Keep Git only in workspace
# (Already done - workspace .git exists)
```

---

**Summary**: Three layers of protection ensure PDF directories never sync to GitHub. Git repository scope provides primary protection, with .gitignore files as additional safety measures.

---

## Ongoing Tracking (Post-Initial Setup)

**Status**: ✅ Repository now actively tracked on GitHub

### Current Configuration

- **GitHub Repository**: https://github.com/cjimmylin/cei-literature
- **Remote**: `origin` → https://github.com/cjimmylin/cei-literature.git
- **Branch**: `main`
- **Initial commit**: `9a076a2` (5,266 files, Feb 2, 2026)

### For Future Sessions

This repository is now continuously tracked on GitHub. All Claude Code sessions and future work should follow the Git workflow:

1. **Check status** at session start:
   ```bash
   git status
   git log --oneline -5
   ```

2. **Commit regularly** during work:
   ```bash
   git add .
   git commit -m "Descriptive message"
   git push
   ```

3. **Always push** at session end:
   ```bash
   git add .
   git commit -m "Session end: [summary]"
   git push
   ```

### Key Documentation

- **Ongoing workflow**: [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Daily Git operations
- **Initial setup**: This document - One-time configuration (completed)
- **CLAUDE.md**: Main guidance file - Updated with Git tracking info

### What to Track

✅ **Always commit and push**:
- New/modified papers
- PDF extracts (markdown)
- Author profiles
- Script changes
- Documentation updates
- AI Labs additions

❌ **Never commit** (already gitignored):
- PDFs (external storage)
- `.vault-config.json`
- Log files
- RECYCLE-BIN contents

---

**Setup Complete**: February 2, 2026
**Next Steps**: See [GIT_WORKFLOW.md](GIT_WORKFLOW.md) for ongoing Git operations
