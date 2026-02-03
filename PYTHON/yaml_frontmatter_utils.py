#!/usr/bin/env python3
"""
DEPRECATED: YAML Frontmatter Utilities (Shim)

This module is deprecated and now re-exports from lib.yaml_utils.
All new code should import directly from lib.yaml_utils instead.

Old usage (still works):
    from PYTHON.yaml_frontmatter_utils import extract_frontmatter, write_paper

New usage (preferred):
    from lib.yaml_utils import extract_frontmatter, write_paper

Migration: This shim ensures backward compatibility for 51 existing scripts.
Will be removed after gradual migration to lib.yaml_utils.

Version: 1.1 (compatibility shim)
Migrated to: .agent/lib/yaml_utils.py
"""

import sys
from pathlib import Path

# Add .agent to path so we can import from lib
_agent_path = Path(__file__).parent.parent / ".agent"
if str(_agent_path) not in sys.path:
    sys.path.insert(0, str(_agent_path))

# Re-export everything from lib.yaml_utils
from lib.yaml_utils import (
    # Extraction & parsing
    extract_frontmatter,
    parse_frontmatter,

    # Validation
    validate_frontmatter,

    # Reconstruction
    rebuild_frontmatter,

    # Reading & Writing
    read_paper,
    write_paper,

    # Cleaning
    clean_orphaned_tags,
)

__all__ = [
    "extract_frontmatter",
    "parse_frontmatter",
    "validate_frontmatter",
    "rebuild_frontmatter",
    "read_paper",
    "write_paper",
    "clean_orphaned_tags",
]

if __name__ == "__main__":
    print("⚠️  DEPRECATED: This module is now a shim to lib.yaml_utils")
    print("   New code should use: from lib.yaml_utils import ...")
    print("\n✅ All functions re-exported successfully from lib.yaml_utils")
