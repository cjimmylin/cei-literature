#!/usr/bin/env python3
"""
Quarterly Maintenance - Vault Health Check Script

Performs 8-step comprehensive health check on CEI Literature Vault.
Generates detailed health report with actionable findings.

Usage:
    python3 run_maintenance.py [--verbose] [--fix]
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# Add .agent to path for lib imports
# Script is in .claude/skills/quarterly-maintenance/, so go up 3 levels to workspace root
workspace_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(workspace_root / ".agent"))

from lib import paper_utils, author_utils, pdf_utils, validation_utils
from lib.config import PAPERS_DIR, AUTHORS_DIR, PDFS_DIR


class HealthCheck:
    """Orchestrates 8-step vault health check."""

    def __init__(self, verbose: bool = False, fix: bool = False):
        self.verbose = verbose
        self.fix = fix
        self.results = {
            "critical": [],
            "warnings": [],
            "info": [],
            "stats": {},
        }

    def log(self, message: str, level: str = "info"):
        """Log message if verbose mode enabled."""
        if self.verbose or level == "critical":
            prefix = {"critical": "❌", "warning": "⚠️ ", "info": "ℹ️ "}
            print(f"{prefix.get(level, '')} {message}")

    def step1_yaml_integrity(self):
        """Step 1: Validate YAML frontmatter integrity."""
        self.log("Step 1/8: YAML Integrity Check...", "info")

        results = validation_utils.validate_all_papers()
        self.results["stats"]["total_papers"] = results["total"]
        self.results["stats"]["valid_papers"] = results["valid"]

        if results["errors"] > 0:
            self.results["critical"].append({
                "issue": "YAML Validation Errors",
                "count": len(results["failed_papers"]),
                "details": results["failed_papers"][:5],  # Show first 5
                "action": "Manual repair required",
            })

        self.log(f"  Found {results['valid']}/{results['total']} valid papers")

    def step2_pdf_link_validation(self):
        """Step 2: Validate PDF links."""
        self.log("Step 2/8: PDF Link Validation...", "info")

        missing = pdf_utils.find_missing_pdfs()
        self.results["stats"]["missing_pdfs"] = len(missing)

        if len(missing) > 0:
            self.results["critical"].append({
                "issue": "Missing PDFs",
                "count": len(missing),
                "details": missing[:5],
                "action": "Re-download or update links",
            })

        self.log(f"  Found {len(missing)} missing PDFs")

    def step3_author_profile_integrity(self):
        """Step 3: Check author profile integrity."""
        self.log("Step 3/8: Author Profile Integrity...", "info")

        orphaned = author_utils.find_orphaned_authors()
        all_authors = author_utils.get_all_authors()

        self.results["stats"]["total_authors"] = len(all_authors)
        self.results["stats"]["orphaned_authors"] = len(orphaned)

        if len(orphaned) > 0:
            self.results["warnings"].append({
                "issue": "Orphaned Authors",
                "count": len(orphaned),
                "details": [a.stem for a in orphaned[:5]],
                "action": "Review and archive if not needed",
            })

        self.log(f"  Found {len(orphaned)} orphaned authors")

    def step4_pdf_extract_sync(self):
        """Step 4: Check PDF extract sync."""
        self.log("Step 4/8: PDF Extract Sync...", "info")

        missing_extracts = pdf_utils.find_missing_extracts()
        self.results["stats"]["missing_extracts"] = len(missing_extracts)

        if len(missing_extracts) > 0:
            self.results["warnings"].append({
                "issue": "Missing Extracts",
                "count": len(missing_extracts),
                "details": missing_extracts[:5],
                "action": "Re-extract PDFs",
            })

        self.log(f"  Found {len(missing_extracts)} missing extracts")

    def step5_classification_consistency(self):
        """Step 5: Validate classification consistency."""
        self.log("Step 5/8: Classification Consistency...", "info")

        inconsistent = []
        for paper in paper_utils.get_all_papers():
            content = paper.read_text()
            from lib.yaml_utils import extract_frontmatter, parse_frontmatter

            try:
                fm, _ = extract_frontmatter(content)
                fields = parse_frontmatter(fm)
                issues = validation_utils.validate_classification_consistency(fields)

                if issues:
                    inconsistent.append({
                        "paper": paper.name,
                        "issues": issues,
                    })
            except Exception:
                pass  # Already caught in YAML validation

        self.results["stats"]["inconsistent_classifications"] = len(inconsistent)

        if len(inconsistent) > 0:
            self.results["warnings"].append({
                "issue": "Classification Inconsistencies",
                "count": len(inconsistent),
                "details": inconsistent[:5],
                "action": "Review and correct classifications",
            })

        self.log(f"  Found {len(inconsistent)} classification issues")

    def step6_duplicate_detection(self):
        """Step 6: Detect duplicate papers."""
        self.log("Step 6/8: Duplicate Detection...", "info")

        duplicates = validation_utils.check_duplicate_papers()
        self.results["stats"]["duplicate_dois"] = len(duplicates)

        if len(duplicates) > 0:
            self.results["warnings"].append({
                "issue": "Duplicate Papers (by DOI)",
                "count": len(duplicates),
                "details": list(duplicates.keys())[:5],
                "action": "Review and merge or remove duplicates",
            })

        self.log(f"  Found {len(duplicates)} potential duplicates")

    def step7_orphaned_files(self):
        """Step 7: Find orphaned PDF files."""
        self.log("Step 7/8: Orphaned File Detection...", "info")

        orphaned_pdfs = pdf_utils.find_orphaned_pdfs()
        self.results["stats"]["orphaned_pdfs"] = len(orphaned_pdfs)

        if len(orphaned_pdfs) > 0:
            self.results["warnings"].append({
                "issue": "Orphaned PDFs",
                "count": len(orphaned_pdfs),
                "details": [p.name for p in orphaned_pdfs[:5]],
                "action": "Review and archive or delete",
            })

        self.log(f"  Found {len(orphaned_pdfs)} orphaned PDFs")

    def step8_generate_report(self) -> str:
        """Step 8: Generate health report."""
        self.log("Step 8/8: Generating Health Report...", "info")

        # Calculate health score
        total_issues = len(self.results["critical"]) + len(self.results["warnings"])
        health_score = max(0, 100 - (len(self.results["critical"]) * 10) - (len(self.results["warnings"]) * 2))

        # Generate report
        report = self._format_report(health_score)

        # Save report
        report_dir = Path(__file__).parent.parent.parent / "_OPERATING-SYSTEM" / "Maintenance"
        report_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")
        report_file = report_dir / f"health-report-{timestamp}.md"
        report_file.write_text(report)

        self.log(f"  Report saved to {report_file}")

        return report

    def _format_report(self, health_score: int) -> str:
        """Format health report as markdown."""
        status = "EXCELLENT" if health_score >= 95 else "GOOD" if health_score >= 85 else "NEEDS ATTENTION"
        status_icon = "✅" if health_score >= 95 else "⚠️" if health_score >= 85 else "❌"

        report = f"""# CEI Literature Vault Health Report

**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}
**Health Score:** {health_score}% {status_icon} {status}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Papers | {self.results["stats"].get("total_papers", 0)} |
| Total Authors | {self.results["stats"].get("total_authors", 0)} |
| Valid Papers | {self.results["stats"].get("valid_papers", 0)} |
| **Critical Issues** | **{len(self.results["critical"])}** ❌ |
| **Warnings** | **{len(self.results["warnings"])}** ⚠️ |
| **Info Items** | **{len(self.results["info"])}** ℹ️ |

---

## Critical Issues ({len(self.results["critical"])})

"""
        if self.results["critical"]:
            for i, issue in enumerate(self.results["critical"], 1):
                report += f"""
### {i}. {issue["issue"]} ({issue["count"]})

**Action:** {issue["action"]}

**Details:**
```
{issue["details"]}
```
"""
        else:
            report += "\n✅ No critical issues found!\n"

        report += f"""
---

## Warnings ({len(self.results["warnings"])})

"""
        if self.results["warnings"]:
            for i, warning in enumerate(self.results["warnings"], 1):
                report += f"""
### {i}. {warning["issue"]} ({warning["count"]})

**Action:** {warning["action"]}
"""
        else:
            report += "\n✅ No warnings!\n"

        report += f"""
---

## Statistics

- **Missing PDFs:** {self.results["stats"].get("missing_pdfs", 0)}
- **Missing Extracts:** {self.results["stats"].get("missing_extracts", 0)}
- **Orphaned Authors:** {self.results["stats"].get("orphaned_authors", 0)}
- **Orphaned PDFs:** {self.results["stats"].get("orphaned_pdfs", 0)}
- **Duplicate DOIs:** {self.results["stats"].get("duplicate_dois", 0)}
- **Classification Issues:** {self.results["stats"].get("inconsistent_classifications", 0)}

---

## Recommended Actions

1. Review and fix critical issues first
2. Address warnings as time permits
3. Run quarterly maintenance regularly
4. Keep this report for trend analysis

---

**Generated by:** Quarterly Maintenance Skill
**Version:** 1.0
**Part of:** LifeOS Phase 7-8
"""
        return report

    def run(self) -> str:
        """Execute all 8 health check steps."""
        print("\n╔══════════════════════════════════════════════════════════╗")
        print("║     CEI LITERATURE VAULT - QUARTERLY MAINTENANCE         ║")
        print("╚══════════════════════════════════════════════════════════╝\n")

        # Run all steps
        self.step1_yaml_integrity()
        self.step2_pdf_link_validation()
        self.step3_author_profile_integrity()
        self.step4_pdf_extract_sync()
        self.step5_classification_consistency()
        self.step6_duplicate_detection()
        self.step7_orphaned_files()
        report = self.step8_generate_report()

        print("\n✅ Quarterly maintenance complete!\n")

        return report


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Run quarterly vault maintenance")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed progress")
    parser.add_argument("--fix", "-f", action="store_true", help="Auto-fix simple issues (future)")
    args = parser.parse_args()

    checker = HealthCheck(verbose=args.verbose, fix=args.fix)
    report = checker.run()

    # Print summary
    print(report)


if __name__ == "__main__":
    main()
