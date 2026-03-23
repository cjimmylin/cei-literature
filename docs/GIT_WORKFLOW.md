# Git Workflow - Ongoing GitHub Tracking

**Repository**: https://github.com/cjimmylin/cei-literature
**Branch**: `main`
**Status**: Active tracking enabled

This document provides guidance for Claude Code and future sessions on maintaining continuous GitHub tracking of this repository.

---

## Repository Configuration

```bash
# Remote
origin: https://github.com/cjimmylin/cei-literature.git

# User identity (configured locally in this repo)
user.name: jimmylin
user.email: mail@drjimmylin.com

# Current branch
main (tracking origin/main)
```

---

## When to Commit and Push

### ✅ ALWAYS Commit After:

1. **Adding/modifying papers**
   - New papers imported
   - Paper metadata enriched
   - Classifications updated

2. **Creating/updating PDF extracts**
   - New PDF extracts generated
   - Extracts moved to proper locations

3. **Author enrichment**
   - Author profiles created/updated
   - First author enrichment completed

4. **Script modifications**
   - Python scripts updated
   - New utilities added
   - Bug fixes

5. **Documentation updates**
   - README changes
   - CLAUDE.md updates
   - New docs created

6. **AI Labs additions**
   - New lab papers added
   - Lab documentation updated
   - Completion reports generated

7. **Session completion**
   - End of significant work session
   - Before Claude Code session ends

### ❌ DO NOT Commit:

- Changes to `.vault-config.json` (already gitignored)
- PDFs (external storage, already gitignored)
- Log files (already gitignored)
- Python cache files (already gitignored)
- RECYCLE-BIN contents (already gitignored)

---

## Standard Workflow

### After Making Changes

```bash
# 1. Check what changed
git status

# 2. Review changes (optional)
git diff

# 3. Stage all changes
git add .

# 4. Verify no PDFs are staged
git status | grep -i "\.pdf$"
# Should return nothing (all PDFs ignored)

# 5. Commit with descriptive message
git commit -m "Brief summary of changes

- Bullet point details
- What was added/modified
- Why changes were made"

# 6. Push to GitHub
git push
```

### Quick Commit (for minor changes)

```bash
git add . && git commit -m "Brief description" && git push
```

---

## Commit Message Guidelines

### Format

```
Short summary (50 chars or less)

Optional detailed description:
- What changed
- Why it changed
- Any important notes

Examples of affected files or areas
```

### Good Examples

```bash
# Feature addition
git commit -m "Add 15 new OpenAI papers with extracts

- Downloaded GPT-4o and o3 system cards
- Generated PDF extracts for all papers
- Enriched metadata with ethics classifications"

# Bug fix
git commit -m "Fix YAML parsing error in author enrichment script

- Added proper escaping for special characters
- Updated yaml_frontmatter_utils.py
- All papers now validate correctly"

# Documentation
git commit -m "Update documentation for new AI Labs structure

- Document PDF migration to external directory
- Add Git workflow guide
- Update CLAUDE.md with GitHub info"

# Routine update
git commit -m "Weekly maintenance: enrich 50 author profiles"
```

### Bad Examples

```bash
git commit -m "updates"  # Too vague
git commit -m "fix"      # What was fixed?
git commit -m "stuff"    # Not descriptive
```

---

## Common Operations

### Check Repository Status

```bash
# See what's changed
git status

# See commit history
git log --oneline -10

# See recent commits with details
git log -5

# Check remote connection
git remote -v
```

### Pull Latest Changes (if working from multiple locations)

```bash
# Fetch and merge changes from GitHub
git pull

# Or step by step
git fetch origin
git merge origin/main
```

### Undo Staged Changes (before commit)

```bash
# Unstage specific file
git reset HEAD path/to/file

# Unstage all
git reset
```

### View Commit History

```bash
# Recent commits
git log --oneline -20

# Commits with file changes
git log --stat -10

# Commits by specific author
git log --author="jimmylin" -10
```

---

## What Gets Tracked vs. Not Tracked

### ✅ Tracked by Git (Synced to GitHub)

- **Papers metadata** (`papers/`)
  - YAML frontmatter
  - Markdown content
  - All 657 paper files

- **PDF extracts** (`PDF Extracts/`)
  - Markdown extracts
  - All 662 extract files

- **Author profiles** (`Authors/`)
  - All 2,946 author files

- **AI Labs** (`AI Labs/`)
  - Markdown documentation
  - README files
  - Completion reports
  - Model documentation

- **Scripts** (`PYTHON/`)
  - All Python scripts
  - Utilities and helpers

- **Documentation** (`docs/`)
  - All markdown docs
  - Guides and workflows

- **Configuration templates**
  - `.vault-config.json.example`
  - `requirements.txt`

- **Statistics** (`STATISTICS/`)
  - Generated reports
  - Analysis outputs

### ❌ NOT Tracked (Ignored by Git)

- **PDFs** (1,048 files)
  - External `Lit-WS-PDFs/` directory
  - External `AI-Lab-Lit-WS-PDFs/` directory
  - Stub PDFs in workspace

- **User configuration**
  - `.vault-config.json`

- **Logs**
  - `logs/*.json`
  - `logs/*.log`

- **RECYCLE-BIN**
  - All deleted/archived files

- **Python cache**
  - `__pycache__/`
  - `*.pyc`, `*.pyo`

- **OS files**
  - `.DS_Store`, `Thumbs.db`

---

## Session End Protocol

At the end of each significant work session, commit and push changes:

```bash
# Quick check
git status

# If changes exist
git add .
git commit -m "Session summary: [describe what was accomplished]

Key changes:
- [Major change 1]
- [Major change 2]
- [Major change 3]

Files affected: [number] papers, [number] extracts, etc."

git push

# Verify push succeeded
git status
```

---

## Troubleshooting

### If Push Fails (Authentication)

```bash
# GitHub may prompt for credentials
# Use Personal Access Token (PAT) instead of password
# Create PAT at: https://github.com/settings/tokens

# Or set up SSH keys for easier authentication
```

### If Merge Conflicts Occur

```bash
# Pull latest changes first
git pull

# If conflicts, resolve manually in affected files
# Look for markers: <<<<<<, ======, >>>>>>

# After resolving
git add .
git commit -m "Resolve merge conflicts"
git push
```

### If You Need to Undo Last Commit (not pushed)

```bash
# Keep changes, undo commit
git reset --soft HEAD^

# Discard changes and commit
git reset --hard HEAD^  # USE WITH CAUTION
```

### If PDFs Accidentally Staged

```bash
# Check what's staged
git status | grep -i "\.pdf$"

# If PDFs found, unstage them
git reset

# Verify .gitignore has:
# - AI Labs/**/*.pdf
# - RECYCLE-BIN/

# Re-stage without PDFs
git add .
```

---

## Repository Metrics

Track these metrics when committing major changes:

- **Papers**: Currently 657
- **Extracts**: Currently 662
- **Authors**: Currently 2,946
- **AI Labs coverage**: 14 labs, 350+ papers
- **Repository size**: ~50-100 MB (text only)

Example commit with metrics:
```bash
git commit -m "Add DeepSeek papers and extracts

Stats after this commit:
- Papers: 670 (+13)
- Extracts: 675 (+13)
- AI Labs: DeepSeek coverage now 100%"
```

---

## Best Practices for Future Sessions

### For Claude Code / LLM Sessions:

1. **At session start**: Check git status to see current state
   ```bash
   git status
   git log --oneline -5
   ```

2. **During session**: Make incremental commits for major milestones
   ```bash
   # After completing a task
   git add . && git commit -m "Task completed: [description]" && git push
   ```

3. **At session end**: Always commit and push remaining changes
   ```bash
   git add .
   git commit -m "Session end: [summary of session work]"
   git push
   ```

4. **For large operations**: Commit in batches
   ```bash
   # After enriching 100 papers
   git add . && git commit -m "Enrich 100 papers (batch 1/5)" && git push
   ```

### Commit Frequency

- **Minimum**: Once per session (at end)
- **Recommended**: After each major task completion
- **Ideal**: Every 50-100 file changes or 30-60 minutes of work

---

## Quick Reference Commands

```bash
# Status check
git status

# Commit and push (standard)
git add . && git commit -m "message" && git push

# View recent commits
git log --oneline -10

# Check remote
git remote -v

# Pull latest (if needed)
git pull

# Verify no PDFs staged
git status | grep -i "\.pdf$"
```

---

## Important Reminders

🔴 **NEVER commit PDFs** - They're stored externally and gitignored
🟡 **Always write descriptive commit messages** - Future you will thank you
🟢 **Push regularly** - Don't accumulate too many local-only commits
🔵 **Check status before committing** - Know what you're committing
🟣 **Pull before push if working from multiple locations** - Avoid conflicts

---

**Last Updated**: February 2, 2026
**Initial Push**: Commit `9a076a2` - 5,266 files
**GitHub**: https://github.com/cjimmylin/cei-literature
