#!/usr/bin/env python3
"""
DEPRECATED: Vault Configuration Loader (Shim)

This module is deprecated and now re-exports from lib.config.
All new code should import directly from lib.config instead.

Old usage (still works):
    from PYTHON.vault_config import PDFS_DIR, PAPERS_DIR

New usage (preferred):
    from lib.config import PDFS_DIR, PAPERS_DIR

Migration: This shim ensures backward compatibility for 78 existing scripts.
Will be removed after gradual migration to lib.config.

Version: 1.1 (compatibility shim)
Migrated to: .agent/lib/config.py
"""

import sys
from pathlib import Path

# Add .agent to path so we can import from lib
_agent_path = Path(__file__).parent.parent / ".agent"
if str(_agent_path) not in sys.path:
    sys.path.insert(0, str(_agent_path))

# Re-export everything from lib.config
from lib.config import (
    # Core paths
    WORKSPACE_ROOT,
    PAPERS_DIR,
    PDF_EXTRACTS_DIR,
    AUTHORS_DIR,
    AI_LABS_DIR,
    STATISTICS_DIR,
    DASHBOARDS_DIR,
    LOGS_DIR,
    RECYCLE_BIN_DIR,

    # External paths
    PDFS_DIR,
    AI_LAB_PDFS_DIR,
    ZOTERO_DIR,

    # Functions
    validate_paths,
    get_config_info,

    # Legacy aliases
    VAULT_ROOT,
    REPO_ROOT,
)

# Expose all for backward compatibility
__all__ = [
    "WORKSPACE_ROOT",
    "PAPERS_DIR",
    "PDF_EXTRACTS_DIR",
    "AUTHORS_DIR",
    "AI_LABS_DIR",
    "STATISTICS_DIR",
    "DASHBOARDS_DIR",
    "LOGS_DIR",
    "RECYCLE_BIN_DIR",
    "PDFS_DIR",
    "AI_LAB_PDFS_DIR",
    "ZOTERO_DIR",
    "validate_paths",
    "get_config_info",
    "VAULT_ROOT",
    "REPO_ROOT",
]

if __name__ == "__main__":
    # When run directly, show configuration
    print("⚠️  DEPRECATED: This module is now a shim to lib.config")
    print("   New code should use: from lib.config import ...\n")
    print(get_config_info())
    result = validate_paths()
    if result['valid']:
        print("✅ All paths valid.")
    else:
        print("❌ Issues found:")
        for issue in result['issues']:
            print(f"  - {issue}")
