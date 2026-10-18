#!/usr/bin/env python3
"""
InsightLogger — Persistent insight capture for classification scripts.

Captures reclassifications, anomalies, coverage gaps, false positive patterns,
and other findings during batch processing. Writes both JSON (machine-readable)
and Markdown (human-readable) logs to the vault's logs/ directory.

Usage:
    from lib.insight_logger import InsightLogger

    ilog = InsightLogger("classify_ethics")

    ilog.reclassification("2024-Smith-AI Safety.md", "ethics_overall", 30, 72)
    ilog.anomaly("2024-Doe-Strange.md", "Score jumped by 80 points")
    ilog.stat("Processed 2043 papers, 0 failed")

    summary = ilog.finalize()  # writes files, prints 1-line summary

Design:
    - All insights accumulated in-memory (no I/O during logging)
    - finalize() writes atomically via os.replace() with PID-scoped temp files
    - PID in filename ensures parallel-batch safety
    - Only stdlib imports; config.py LOGS_DIR used as default if available
    - Pass logs_dir= for cross-vault use (e.g. CEI-AI-Statements)
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


# Import LOGS_DIR from config — graceful fallback for cross-vault use
try:
    from lib.config import LOGS_DIR as _DEFAULT_LOGS_DIR
except ImportError:
    try:
        from config import LOGS_DIR as _DEFAULT_LOGS_DIR
    except ImportError:
        _DEFAULT_LOGS_DIR = None


# Severity levels in display order (critical first)
SEVERITY_ORDER = ["critical", "notable", "info"]
VALID_SEVERITIES = set(SEVERITY_ORDER)

# Category display names for markdown reports
CATEGORY_DISPLAY = {
    "reclassification": "Reclassifications",
    "anomaly": "Anomalies",
    "coverage_gap": "Coverage Gaps",
    "false_positive": "False Positives",
    "disagreement": "Disagreements",
    "data_quality": "Data Quality Issues",
    "stat": "Statistics",
    "temporal": "Temporal Patterns",
}


class InsightLogger:
    """Accumulates processing insights and writes them to dated log files."""

    def __init__(self, script_name: str, logs_dir: Path = None):
        self.script_name = script_name
        self.logs_dir = Path(logs_dir) if logs_dir else _DEFAULT_LOGS_DIR
        self.pid = os.getpid()
        self.started = datetime.now()
        self._insights: List[Dict[str, Any]] = []
        self._counter = 0

    # ── Typed convenience methods ────────────────────────────────────

    def reclassification(self, paper: str, field: str, old_value: Any,
                         new_value: Any, message: str = None):
        """A field crossed a meaningful threshold (e.g. <50 -> >=50)."""
        msg = message or f"{field} crossed threshold: {old_value} -> {new_value}"
        self.log("reclassification", msg, severity="notable", paper=paper,
                 details={"field": field, "old_value": old_value, "new_value": new_value})

    def anomaly(self, paper: str, message: str, details: Dict = None):
        """Something unexpected that may indicate a bug."""
        self.log("anomaly", message, severity="critical", paper=paper, details=details)

    def coverage_gap(self, topic: str, message: str, details: Dict = None):
        """A topic/area with insufficient coverage."""
        self.log("coverage_gap", message, severity="notable", paper=None,
                 details={"topic": topic, **(details or {})})

    def false_positive(self, paper: str, pattern: str, matched_text: str,
                       message: str = None):
        """A keyword pattern fired incorrectly."""
        msg = message or f"FP: pattern '{pattern}' matched '{matched_text}'"
        self.log("false_positive", msg, severity="notable", paper=paper,
                 details={"pattern": pattern, "matched_text": matched_text})

    def disagreement(self, paper: str, field: str, old_value: Any,
                     new_value: Any):
        """Old and new values differ by more than 20 points."""
        delta = abs(new_value - old_value) if isinstance(new_value, (int, float)) else None
        severity = "notable" if delta and delta > 20 else "info"
        self.log("disagreement",
                 f"{field}: {old_value} -> {new_value} (delta={delta})",
                 severity=severity, paper=paper,
                 details={"field": field, "old_value": old_value,
                          "new_value": new_value, "delta": delta})

    def data_quality(self, paper: str, issue_type: str, message: str):
        """A data quality issue (missing abstract, malformed YAML, etc.)."""
        self.log("data_quality", message, severity="info", paper=paper,
                 details={"issue_type": issue_type})

    def stat(self, message: str, details: Dict = None):
        """A routine statistic (counts, averages, distributions)."""
        self.log("stat", message, severity="info", details=details)

    def temporal(self, message: str, details: Dict = None):
        """A temporal pattern (year-over-year changes, trends)."""
        self.log("temporal", message, severity="info", details=details)

    # ── Generic log method ───────────────────────────────────────────

    def log(self, category: str, message: str, severity: str = "info",
            paper: str = None, details: Dict = None):
        """Core logging method — all convenience methods delegate here."""
        if severity not in VALID_SEVERITIES:
            severity = "info"

        self._counter += 1
        entry = {
            "id": self._counter,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "category": category,
            "severity": severity,
            "message": message,
        }
        if paper:
            entry["paper"] = paper
        if details:
            entry["details"] = details

        self._insights.append(entry)

    # ── Finalize: write files ────────────────────────────────────────

    def finalize(self) -> Dict[str, Any]:
        """Write JSON + Markdown log files and print a 1-line summary.

        Returns a summary dict with counts and file paths.
        """
        finished = datetime.now()
        duration = (finished - self.started).total_seconds()
        date_prefix = self.started.strftime("%Y%m%d")

        # Build summary counts
        by_category: Dict[str, int] = {}
        by_severity: Dict[str, int] = {}
        for ins in self._insights:
            cat = ins["category"]
            sev = ins["severity"]
            by_category[cat] = by_category.get(cat, 0) + 1
            by_severity[sev] = by_severity.get(sev, 0) + 1

        meta = {
            "script": self.script_name,
            "pid": self.pid,
            "started": self.started.isoformat(timespec="seconds"),
            "finished": finished.isoformat(timespec="seconds"),
            "duration_seconds": round(duration, 1),
            "total_insights": len(self._insights),
            "by_category": by_category,
            "by_severity": by_severity,
        }

        # Validate logs_dir is set
        if self.logs_dir is None:
            raise RuntimeError(
                "InsightLogger: logs_dir is not set and no default LOGS_DIR "
                "found in config.py. Pass logs_dir= to the constructor."
            )

        # File stems
        stem = f"{date_prefix}-insights-{self.script_name}-{self.pid}"
        json_path = self.logs_dir / f"{stem}.json"
        md_path = self.logs_dir / f"{stem}.md"

        # Ensure logs/ directory exists
        self.logs_dir.mkdir(parents=True, exist_ok=True)

        # Write JSON atomically
        json_data = {"meta": meta, "insights": self._insights}
        tmp_json = self.logs_dir / f".tmp.{self.pid}.json"
        tmp_json.write_text(
            json.dumps(json_data, indent=2, ensure_ascii=False, default=str),
            encoding="utf-8",
        )
        os.replace(str(tmp_json), str(json_path))

        # Write Markdown
        md_content = self._render_markdown(meta)
        tmp_md = self.logs_dir / f".tmp.{self.pid}.md"
        tmp_md.write_text(md_content, encoding="utf-8")
        os.replace(str(tmp_md), str(md_path))

        # Print 1-line summary
        critical = by_severity.get("critical", 0)
        notable = by_severity.get("notable", 0)
        info = by_severity.get("info", 0)
        print(f"[InsightLogger] {len(self._insights)} insights "
              f"({critical} critical, {notable} notable, {info} info) "
              f"-> {json_path.name}")

        return {
            "total": len(self._insights),
            "by_category": by_category,
            "by_severity": by_severity,
            "json_path": str(json_path),
            "md_path": str(md_path),
        }

    # ── Markdown rendering ───────────────────────────────────────────

    def _render_markdown(self, meta: Dict) -> str:
        """Render insights as a human-readable Markdown report."""
        lines = []
        lines.append(f"# Insight Log: {self.script_name}")
        lines.append("")
        lines.append(f"**Date:** {meta['started'][:10]}")
        lines.append(f"**Script:** {self.script_name}")
        lines.append(f"**PID:** {self.pid}")
        lines.append(f"**Duration:** {meta['duration_seconds']}s")
        lines.append(f"**Total insights:** {meta['total_insights']}")
        lines.append("")

        # Summary table
        lines.append("## Summary")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("|----------|-------|")
        for cat, count in sorted(meta["by_category"].items(),
                                 key=lambda x: -x[1]):
            display = CATEGORY_DISPLAY.get(cat, cat.replace("_", " ").title())
            lines.append(f"| {display} | {count} |")
        lines.append("")

        lines.append("| Severity | Count |")
        lines.append("|----------|-------|")
        for sev in SEVERITY_ORDER:
            count = meta["by_severity"].get(sev, 0)
            if count > 0:
                lines.append(f"| {sev.capitalize()} | {count} |")
        lines.append("")

        # Group insights: severity (critical first), then category
        for sev in SEVERITY_ORDER:
            sev_insights = [i for i in self._insights if i["severity"] == sev]
            if not sev_insights:
                continue

            lines.append(f"## {sev.capitalize()} ({len(sev_insights)})")
            lines.append("")

            # Sub-group by category
            cats_seen = []
            for ins in sev_insights:
                if ins["category"] not in cats_seen:
                    cats_seen.append(ins["category"])

            for cat in cats_seen:
                cat_insights = [i for i in sev_insights if i["category"] == cat]
                display = CATEGORY_DISPLAY.get(cat, cat.replace("_", " ").title())
                lines.append(f"### {display}")
                lines.append("")

                for ins in cat_insights:
                    paper = ins.get("paper", "")
                    paper_str = f" `{paper}`" if paper else ""
                    lines.append(f"- {ins['message']}{paper_str}")
                    if ins.get("details"):
                        details_str = ", ".join(
                            f"{k}={v}" for k, v in ins["details"].items()
                            if k not in ("field", "old_value", "new_value",
                                         "delta", "pattern", "matched_text",
                                         "issue_type", "topic")
                        )
                        if details_str:
                            lines.append(f"  - {details_str}")
                lines.append("")

        return "\n".join(lines)
