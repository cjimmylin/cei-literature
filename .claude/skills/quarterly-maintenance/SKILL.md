# Quarterly Maintenance - Vault Health Check

**Purpose:** Automated quarterly health check for CEI Literature Vault
**Frequency:** Run every 3 months (or on-demand)
**Duration:** ~5-10 minutes
**Output:** Comprehensive health report with actionable findings

---

## What This Skill Does

Performs an 8-step comprehensive health check on your literature vault:

1. **YAML Integrity Check** - Validates all paper frontmatter
2. **PDF Link Validation** - Finds missing or broken PDF links
3. **Author Profile Integrity** - Detects orphaned author files
4. **PDF Extract Sync** - Checks for missing extract files
5. **Classification Consistency** - Validates ethics classification logic
6. **Duplicate Detection** - Finds potential duplicate papers
7. **Orphaned File Detection** - Identifies unreferenced PDFs
8. **Generate Health Report** - Creates detailed findings summary

---

## Usage

```bash
# Run quarterly maintenance
/quarterly-maintenance

# With options
/quarterly-maintenance --verbose    # Show detailed progress
/quarterly-maintenance --fix        # Auto-fix simple issues (future)
```

---

## When to Run

**Scheduled:**
- Every 3 months (quarterly)
- After major imports (>10 new papers)
- Before archiving/backup operations

**On-Demand:**
- Suspecting data corruption
- After migration or system changes
- Pre-publication quality assurance

---

## What It Reports

### Health Score
- Overall vault health percentage (0-100%)
- Critical, warning, and info issue counts
- Trend comparison vs. last run

### Detailed Findings
- **Critical Issues:** Data corruption, missing files, broken links
- **Warnings:** Inconsistent classifications, orphaned files
- **Info:** Statistics, improvement suggestions

### Actionable Items
- Prioritized fix list with estimated effort
- Automated fix options (where safe)
- Manual review recommendations

---

## Output Example

```
╔══════════════════════════════════════════════════════════╗
║          CEI LITERATURE VAULT HEALTH REPORT              ║
║                 2026-02-02 19:30 UTC                     ║
╚══════════════════════════════════════════════════════════╝

📊 OVERALL HEALTH: 94% ✅ EXCELLENT

┌─────────────────────────────────────────────────────────┐
│ SUMMARY                                                 │
├─────────────────────────────────────────────────────────┤
│ Total Papers:       657                                 │
│ Total Authors:      2,946                               │
│ Total PDFs:         592                                 │
│ Total Extracts:     645                                 │
├─────────────────────────────────────────────────────────┤
│ Critical Issues:    2   ❌                              │
│ Warnings:           12  ⚠️                              │
│ Info:               5   ℹ️                              │
└─────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 CRITICAL ISSUES (2)

1. Missing PDFs (14 papers)
   Papers reference PDFs that don't exist
   Impact: Cannot access full text
   Action: Re-download or update links

2. YAML Validation Errors (2 papers)
   Corrupted frontmatter structure
   Impact: Classification/search broken
   Action: Manual repair required

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  WARNINGS (12)

1. Orphaned PDFs (77 files)
   PDFs not referenced by any paper
   Impact: Storage waste, confusion
   Action: Review and archive or delete

2. Missing Extracts (38 papers)
   Papers reference extracts that don't exist
   Impact: Cannot view extracted content
   Action: Re-extract PDFs

3. Orphaned Authors (0 profiles)
   Author files not referenced by papers
   Impact: None (all authors referenced)
   Action: None needed ✅

... [additional warnings]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ℹ️  INFORMATION (5)

1. Classification Coverage
   - 100% have ethics_overall ✅
   - 95% have detailed frameworks
   - 3% pending enrichment

2. Enrichment Status
   - Authors enriched: 0/2,946 (0%)
   - Papers enriched: 245/657 (37%)

... [additional info]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 RECOMMENDED ACTIONS (Priority Order)

1. [CRITICAL] Fix YAML validation errors (2 papers)
   Estimated time: 10 minutes
   Command: Review papers/[list]

2. [CRITICAL] Re-download missing PDFs (14 papers)
   Estimated time: 30 minutes
   Command: /download-pdf [DOI]

3. [WARNING] Clean up orphaned PDFs (77 files)
   Estimated time: 20 minutes
   Command: Review RECYCLE-BIN/orphaned-pdfs/

4. [WARNING] Re-extract missing extracts (38 papers)
   Estimated time: 15 minutes
   Command: /extract-pdf-text [batch]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💾 REPORT SAVED TO:
   _OPERATING-SYSTEM/Maintenance/health-report-2026-02-02.md

📈 TREND: Health improved +2% since last check (2025-11-02)
```

---

## Implementation

See `run_maintenance.py` for the actual health check logic.

---

## Safety

- **Read-only by default** - No files modified without explicit `--fix` flag
- **Backup recommended** - Before running with `--fix`
- **Validation** - All fixes validated before writing
- **Logging** - Complete audit trail in health report

---

## Configuration

Edit `.vault-config.json` to customize:

```json
{
  "maintenance": {
    "thresholds": {
      "critical_health_score": 80,
      "warning_health_score": 90
    },
    "auto_fix": {
      "orphaned_tags": true,
      "whitespace": true,
      "broken_links": false
    }
  }
}
```

---

**Version:** 1.0
**Last Updated:** 2026-02-02
**Part of:** LifeOS Phase 7-8 (Self-Healing Infrastructure)
