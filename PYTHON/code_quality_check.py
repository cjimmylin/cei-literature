#!/usr/bin/env python3
"""
Code Quality Check Script for CEI Literature Vault

Performs automated QC/QA checks on:
- Python scripts in PYTHON/
- Skill definitions in .claude/commands/
- Skill scripts in .agent/skills/

Run with: python3 PYTHON/code_quality_check.py [--fix] [--verbose]
"""

import re
import sys
import ast
from pathlib import Path
from datetime import datetime
from typing import List, Tuple
from collections import defaultdict


# Directories - use vault_config
from vault_config import WORKSPACE_ROOT, REPO_ROOT
VAULT_ROOT = WORKSPACE_ROOT
PYTHON_DIR = VAULT_ROOT / "PYTHON"
COMMANDS_DIR = REPO_ROOT / ".claude" / "commands"
SKILLS_DIR = REPO_ROOT / ".agent" / "skills"


class Issue:
    """Represents a code quality issue"""
    def __init__(self, severity: str, category: str, file: str, line: int, message: str, fixable: bool = False):
        self.severity = severity  # critical, high, medium, low
        self.category = category
        self.file = file
        self.line = line
        self.message = message
        self.fixable = fixable

    def __str__(self):
        loc = f"{self.file}:{self.line}" if self.line else self.file
        return f"[{self.severity.upper()}] {self.category}: {loc} - {self.message}"


class CodeQualityChecker:
    """Main checker class"""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.issues: List[Issue] = []

    def log(self, message: str):
        if self.verbose:
            print(f"  {message}")

    # =========================================================================
    # Python Script Checks
    # =========================================================================

    def check_python_scripts(self):
        """Check all Python scripts"""
        print("\n[1/4] Checking Python scripts...")

        py_files = list(PYTHON_DIR.glob("*.py"))
        self.log(f"Found {len(py_files)} Python files")

        for filepath in py_files:
            self.check_python_file(filepath)

        # Also check skill scripts
        skill_scripts = list(SKILLS_DIR.glob("**/scripts/*.py"))
        self.log(f"Found {len(skill_scripts)} skill scripts")
        for filepath in skill_scripts:
            self.check_python_file(filepath)

    def check_python_file(self, filepath: Path):
        """Check a single Python file"""
        self.log(f"Checking {filepath.name}")

        try:
            content = filepath.read_text(encoding='utf-8')
            lines = content.split('\n')
        except Exception as e:
            self.issues.append(Issue(
                "critical", "file-read", str(filepath), 0,
                f"Cannot read file: {e}"
            ))
            return

        # Check 1: Hardcoded absolute paths
        self.check_hardcoded_paths(filepath, content, lines)

        # Check 2: Bare except clauses
        self.check_bare_excepts(filepath, content, lines)

        # Check 3: Missing docstring
        self.check_docstring(filepath, content)

        # Check 4: Unused imports
        self.check_unused_imports(filepath, content)

        # Check 5: YAML utility usage
        self.check_yaml_utility_usage(filepath, content, lines)

        # Check 6: Print statements without context
        self.check_print_statements(filepath, content, lines)

    def check_hardcoded_paths(self, filepath: Path, content: str, lines: List[str]):
        """Check for hardcoded absolute paths"""
        # Pattern for absolute paths (macOS/Linux)
        patterns = [
            r"['\"]\/Users\/[^'\"]+['\"]",
            r"['\"]\/home\/[^'\"]+['\"]",
            r"Path\(['\"]\/Users\/",
            r"Path\(['\"]\/home\/",
        ]

        for i, line in enumerate(lines, 1):
            # Skip comments
            if line.strip().startswith('#'):
                continue

            for pattern in patterns:
                if re.search(pattern, line):
                    self.issues.append(Issue(
                        "critical", "hardcoded-path", str(filepath.name), i,
                        f"Hardcoded absolute path found",
                        fixable=True
                    ))
                    break

    def check_bare_excepts(self, filepath: Path, content: str, lines: List[str]):
        """Check for bare except clauses"""
        patterns = [
            r'except\s*:',  # bare except
            r'except\s+Exception\s*:\s*pass',  # except Exception: pass
        ]

        for i, line in enumerate(lines, 1):
            if re.search(r'except\s*:', line) and 'Exception' not in line:
                self.issues.append(Issue(
                    "high", "bare-except", str(filepath.name), i,
                    "Bare except clause - use 'except Exception:' instead",
                    fixable=True
                ))

    def check_docstring(self, filepath: Path, content: str):
        """Check for module docstring"""
        try:
            tree = ast.parse(content)
            docstring = ast.get_docstring(tree)
            if not docstring:
                self.issues.append(Issue(
                    "medium", "missing-docstring", str(filepath.name), 1,
                    "Missing module docstring"
                ))
        except SyntaxError:
            pass  # Syntax errors are caught elsewhere

    def check_unused_imports(self, filepath: Path, content: str):
        """Check for potentially unused imports"""
        try:
            tree = ast.parse(content)
        except SyntaxError:
            return

        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name
                    imports.append((name.split('.')[0], node.lineno))
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name != '*':
                        name = alias.asname if alias.asname else alias.name
                        imports.append((name, node.lineno))

        # Simple check: if import name not found elsewhere in content
        for name, lineno in imports:
            # Count occurrences (excluding the import line itself)
            lines = content.split('\n')
            occurrences = 0
            for i, line in enumerate(lines, 1):
                if i != lineno and re.search(rf'\b{re.escape(name)}\b', line):
                    occurrences += 1

            if occurrences == 0:
                self.issues.append(Issue(
                    "low", "unused-import", str(filepath.name), lineno,
                    f"Potentially unused import: {name}"
                ))

    def check_yaml_utility_usage(self, filepath: Path, content: str, lines: List[str]):
        """Check if scripts modifying YAML use yaml_frontmatter_utils"""
        # Skip the utility itself and known exceptions
        YAML_SAFETY_EXCEPTIONS = {
            'yaml_frontmatter_utils.py',
            'generate_report_v2.py',  # Only writes to STATISTICS/, not papers
            'fix_yaml_tags.py',       # Fixes malformed YAML that can't use standard utilities
            'identify_benchmarks.py',  # Only writes to STATISTICS/benchmark_papers_list.json
        }
        if filepath.name in YAML_SAFETY_EXCEPTIONS:
            return

        # Check if file modifies papers
        modifies_papers = any([
            '.write_text(' in content,
            'open(' in content and "'w'" in content,
            'write_paper' in content,
        ])

        if not modifies_papers:
            return

        # Check if it imports yaml_frontmatter_utils
        uses_utility = 'yaml_frontmatter_utils' in content or 'write_paper' in content

        if not uses_utility and 'papers/' in content:
            self.issues.append(Issue(
                "high", "yaml-safety", str(filepath.name), 0,
                "Modifies papers but doesn't use yaml_frontmatter_utils.py"
            ))

    def check_print_statements(self, filepath: Path, content: str, lines: List[str]):
        """Check for excessive bare print statements"""
        print_count = len(re.findall(r'\bprint\s*\(', content))
        if print_count > 20:
            self.issues.append(Issue(
                "low", "logging", str(filepath.name), 0,
                f"High number of print statements ({print_count}) - consider using logging"
            ))

    # =========================================================================
    # Skill Definition Checks
    # =========================================================================

    def check_skill_definitions(self):
        """Check all skill definitions"""
        print("\n[2/4] Checking skill definitions...")

        if not COMMANDS_DIR.exists():
            self.log("Commands directory not found")
            return

        md_files = list(COMMANDS_DIR.glob("*.md"))
        self.log(f"Found {len(md_files)} skill files")

        for filepath in md_files:
            self.check_skill_file(filepath)

    def check_skill_file(self, filepath: Path):
        """Check a single skill definition file"""
        self.log(f"Checking {filepath.name}")

        try:
            content = filepath.read_text(encoding='utf-8')
            lines = content.split('\n')
        except Exception as e:
            self.issues.append(Issue(
                "critical", "file-read", str(filepath), 0,
                f"Cannot read file: {e}"
            ))
            return

        # Check 1: Required sections
        self.check_skill_sections(filepath, content)

        # Check 2: Script references
        self.check_script_references(filepath, content)

        # Check 3: Outdated format references
        self.check_outdated_references(filepath, content, lines)

        # Check 4: Error handling section
        self.check_error_handling_section(filepath, content)

    def check_skill_sections(self, filepath: Path, content: str):
        """Check for required sections in skill files"""
        required_markers = ['## Usage', '##']  # At least usage and one more section
        optional_sections = ['## Arguments', '## Instructions', '## Related', '## Example']

        has_usage = '## Usage' in content or '## Process' in content

        if not has_usage:
            self.issues.append(Issue(
                "medium", "skill-structure", str(filepath.name), 0,
                "Missing ## Usage or ## Process section"
            ))

    def check_script_references(self, filepath: Path, content: str):
        """Check that referenced scripts exist"""
        # Find Python script references
        script_refs = re.findall(r'python3?\s+([^\s]+\.py)', content)

        for script_ref in script_refs:
            # Normalize path
            if script_ref.startswith('PYTHON/'):
                script_path = VAULT_ROOT / script_ref
            elif script_ref.startswith('.agent/'):
                script_path = VAULT_ROOT / script_ref
            else:
                script_path = VAULT_ROOT / 'PYTHON' / script_ref

            if not script_path.exists():
                self.issues.append(Issue(
                    "high", "missing-script", str(filepath.name), 0,
                    f"Referenced script not found: {script_ref}"
                ))

    def check_outdated_references(self, filepath: Path, content: str, lines: List[str]):
        """Check for outdated file format references"""
        # Check for .txt references when .md is the current format
        for i, line in enumerate(lines, 1):
            if 'PDF Extracts' in line and '.txt' in line:
                self.issues.append(Issue(
                    "critical", "outdated-format", str(filepath.name), i,
                    "References .txt format - PDF extracts are now .md format",
                    fixable=True
                ))

    def check_error_handling_section(self, filepath: Path, content: str):
        """Check for error handling documentation"""
        error_keywords = ['error', 'fail', 'exception', '403', '401', 'rate limit']
        has_error_section = any(kw in content.lower() for kw in error_keywords)

        # Skills that should definitely have error handling
        needs_error_handling = ['download', 'fetch', 'check-publication', 'research']
        skill_name = filepath.stem

        if any(kw in skill_name for kw in needs_error_handling) and not has_error_section:
            self.issues.append(Issue(
                "medium", "missing-error-handling", str(filepath.name), 0,
                "Skill involves network calls but lacks error handling documentation"
            ))

    # =========================================================================
    # Consistency Checks
    # =========================================================================

    def check_consistency(self):
        """Check for consistency issues across files"""
        print("\n[3/4] Checking consistency...")

        self.check_duplicate_functionality()
        self.check_naming_consistency()

    def check_duplicate_functionality(self):
        """Check for scripts with potentially duplicate functionality"""
        # Group scripts by prefix
        prefixes = defaultdict(list)
        for filepath in PYTHON_DIR.glob("*.py"):
            name = filepath.stem
            # Extract prefix (first word before _)
            prefix = name.split('_')[0]
            prefixes[prefix].append(name)

        # Report groups with many similar scripts
        for prefix, scripts in prefixes.items():
            if len(scripts) >= 3:
                self.issues.append(Issue(
                    "medium", "duplicate-functionality", "PYTHON/", 0,
                    f"Multiple scripts with prefix '{prefix}': {', '.join(scripts[:4])}"
                ))

    def check_naming_consistency(self):
        """Check for naming consistency"""
        # Check skill files use kebab-case
        for filepath in COMMANDS_DIR.glob("*.md"):
            if '_' in filepath.stem:
                self.issues.append(Issue(
                    "low", "naming", str(filepath.name), 0,
                    "Skill uses underscore - should use kebab-case"
                ))

        # Check Python files use snake_case
        for filepath in PYTHON_DIR.glob("*.py"):
            if '-' in filepath.stem:
                self.issues.append(Issue(
                    "low", "naming", str(filepath.name), 0,
                    "Python file uses hyphen - should use snake_case"
                ))

    # =========================================================================
    # Documentation Checks
    # =========================================================================

    def check_documentation(self):
        """Check documentation quality"""
        print("\n[4/4] Checking documentation...")

        # Check CLAUDE.md exists and is up to date
        claude_md = VAULT_ROOT / "CLAUDE.md"
        if not claude_md.exists():
            self.issues.append(Issue(
                "critical", "documentation", "CLAUDE.md", 0,
                "CLAUDE.md not found"
            ))
        else:
            self.log("CLAUDE.md exists")

        # Check docs directory structure
        docs_dir = VAULT_ROOT / "docs"
        expected_docs = ['SCRIPTS.md', 'COMMANDS.md', 'WORKFLOWS.md']
        for doc in expected_docs:
            if not (docs_dir / doc).exists():
                self.issues.append(Issue(
                    "medium", "documentation", f"docs/{doc}", 0,
                    f"Expected documentation file not found"
                ))

    # =========================================================================
    # Report Generation
    # =========================================================================

    def generate_report(self) -> str:
        """Generate the QC/QA report"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Count by severity
        severity_counts = defaultdict(int)
        category_counts = defaultdict(int)
        for issue in self.issues:
            severity_counts[issue.severity] += 1
            category_counts[issue.category] += 1

        report = f"""# Code Quality Check Results

**Generated:** {timestamp}
**Total Issues:** {len(self.issues)}

## Summary by Severity

| Severity | Count |
|----------|-------|
| Critical | {severity_counts['critical']} |
| High | {severity_counts['high']} |
| Medium | {severity_counts['medium']} |
| Low | {severity_counts['low']} |

## Summary by Category

| Category | Count |
|----------|-------|
"""
        for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
            report += f"| {cat} | {count} |\n"

        report += "\n## All Issues\n\n"

        # Group by severity
        for severity in ['critical', 'high', 'medium', 'low']:
            issues = [i for i in self.issues if i.severity == severity]
            if issues:
                report += f"### {severity.title()} ({len(issues)})\n\n"
                for issue in issues:
                    fixable = " [FIXABLE]" if issue.fixable else ""
                    report += f"- **{issue.category}** - {issue.file}"
                    if issue.line:
                        report += f":{issue.line}"
                    report += f": {issue.message}{fixable}\n"
                report += "\n"

        return report

    def run(self) -> Tuple[int, str]:
        """Run all checks and return (exit_code, report)"""
        self.check_python_scripts()
        self.check_skill_definitions()
        self.check_consistency()
        self.check_documentation()

        report = self.generate_report()

        # Determine exit code based on critical/high issues
        critical_high = sum(1 for i in self.issues if i.severity in ['critical', 'high'])
        exit_code = 1 if critical_high > 0 else 0

        return exit_code, report


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Code Quality Check for CEI Vault')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--fix', action='store_true', help='Attempt to fix issues (not yet implemented)')
    parser.add_argument('--output', '-o', type=str, help='Output file for report')
    args = parser.parse_args()

    print("=" * 60)
    print("CODE QUALITY CHECK - CEI Literature Vault")
    print("=" * 60)

    checker = CodeQualityChecker(verbose=args.verbose)
    exit_code, report = checker.run()

    # Print summary
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(report)

    # Save report if requested
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(report, encoding='utf-8')
        print(f"\nReport saved to: {output_path}")
    else:
        # Default: save to logs directory
        logs_dir = VAULT_ROOT / "logs"
        logs_dir.mkdir(exist_ok=True)
        report_path = logs_dir / f"code_quality_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_path.write_text(report, encoding='utf-8')
        print(f"\nReport saved to: {report_path}")

    if args.fix:
        print("\n[!] --fix flag specified but auto-fix not yet implemented")
        print("    Fixable issues are marked with [FIXABLE] in the report")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
