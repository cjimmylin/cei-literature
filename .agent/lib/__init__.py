"""
CEI Literature Vault - Centralized Library

This package provides shared utilities for the CEI Literature Vault:
- config: Vault configuration and path management
- yaml_utils: YAML frontmatter operations (CRITICAL - use for all YAML edits)
- paper_utils: Paper file operations
- author_utils: Author profile operations
- pdf_utils: PDF and extract operations
- validation_utils: Integrity checks and validation

Usage:
    from lib.config import VAULT_ROOT, PDFS_DIR
    from lib.yaml_utils import write_paper, extract_frontmatter
    from lib.paper_utils import get_all_papers, update_paper_field

Version: 1.0
Created: 2026-02-02
Part of: LifeOS capabilities migration (Phase 5-6)
"""

__version__ = "1.0.0"
__author__ = "CEI Literature Vault AI Agents"

# Version check for Python 3.8+
import sys
if sys.version_info < (3, 8):
    raise RuntimeError("CEI Literature Vault requires Python 3.8 or higher")

# Modules are imported by users directly, not pre-loaded here
# This avoids circular import issues during development

__all__ = [
    "config",
    "yaml_utils",
    "paper_utils",
    "author_utils",
    "pdf_utils",
    "validation_utils",
    "insight_logger",
    "__version__",
]
