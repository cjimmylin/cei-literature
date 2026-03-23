#!/usr/bin/env python3
"""
Vault Configuration Loader

Centralized configuration for the CEI-Literature-Vault.
Reads from .vault-config.json to determine external paths like PDFs.

Usage:
    from lib.config import PDFS_DIR, PAPERS_DIR, WORKSPACE_ROOT

    # All paths are Path objects
    for pdf in PDFS_DIR.glob("*.pdf"):
        print(pdf.name)

Migrated from: PYTHON/vault_config.py
Version: 1.1 (now in .agent/lib/)
"""

import os
import json
from pathlib import Path


def _expand_path(path_str: str) -> Path:
    """Expand ~ and environment variables in path string."""
    return Path(os.path.expandvars(os.path.expanduser(path_str)))


def _load_config() -> dict:
    """
    Load configuration from .vault-config.json.

    Search order:
    1. WORKSPACE_ROOT/.vault-config.json
    2. Environment variables (VAULT_PDF_PATH, VAULT_ZOTERO_PATH)
    3. Raise error if PDF path not configured
    """
    config_path = WORKSPACE_ROOT / ".vault-config.json"

    config = {}

    # Try loading from config file
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read {config_path}: {e}")

    # Environment variable fallbacks
    if 'pdf_path' not in config:
        env_pdf = os.environ.get('VAULT_PDF_PATH')
        if env_pdf:
            config['pdf_path'] = env_pdf

    if 'zotero_path' not in config:
        env_zotero = os.environ.get('VAULT_ZOTERO_PATH')
        if env_zotero:
            config['zotero_path'] = env_zotero

    return config


# =============================================================================
# Core Paths (always available)
# =============================================================================

# Workspace root is now calculated from .agent/lib/ location
# .agent/lib/config.py → .agent/ → workspace root
WORKSPACE_ROOT = Path(__file__).parent.parent.parent.resolve()

# Standard directories within workspace
PAPERS_DIR = WORKSPACE_ROOT / "papers"
PDF_EXTRACTS_DIR = WORKSPACE_ROOT / "PDF Extracts"
AUTHORS_DIR = WORKSPACE_ROOT / "Authors"
AI_LABS_DIR = WORKSPACE_ROOT / "AI Labs"
STATISTICS_DIR = WORKSPACE_ROOT / "STATISTICS"
DASHBOARDS_DIR = WORKSPACE_ROOT / "DASHBOARDS"
LOGS_DIR = WORKSPACE_ROOT / "logs"
RECYCLE_BIN_DIR = WORKSPACE_ROOT / "RECYCLE-BIN"

# =============================================================================
# External Paths (from configuration)
# =============================================================================

_config = _load_config()

# PDF directory (external, must be configured)
if 'pdf_path' in _config:
    PDFS_DIR = _expand_path(_config['pdf_path'])
else:
    # Fallback: check if PDFs exist at old location (for backward compatibility)
    _legacy_pdfs = WORKSPACE_ROOT.parent / "Lit-WS-PDFs"
    if _legacy_pdfs.exists():
        PDFS_DIR = _legacy_pdfs
    else:
        raise ValueError(
            "PDF path not configured. Please create .vault-config.json with:\n"
            '{"pdf_path": "/path/to/your/PDFs"}\n'
            "Or set VAULT_PDF_PATH environment variable."
        )

# AI Labs PDFs (external, from configuration)
if 'ai_lab_pdf_path' in _config:
    AI_LAB_PDFS_DIR = _expand_path(_config['ai_lab_pdf_path'])
else:
    # Fallback: check old location for backward compatibility
    _legacy_ai_labs = WORKSPACE_ROOT / "AI Labs"
    AI_LAB_PDFS_DIR = _legacy_ai_labs

# Zotero directory (optional)
if 'zotero_path' in _config:
    ZOTERO_DIR = _expand_path(_config['zotero_path'])
else:
    ZOTERO_DIR = _expand_path("~/Zotero/storage")


# =============================================================================
# Validation
# =============================================================================

def validate_paths(check_pdfs: bool = True) -> dict:
    """
    Validate that configured paths exist.

    Args:
        check_pdfs: If True, verify PDF directory exists

    Returns:
        dict with 'valid' (bool) and 'issues' (list of strings)
    """
    issues = []

    if check_pdfs and not PDFS_DIR.exists():
        issues.append(f"PDF directory not found: {PDFS_DIR}")

    if not PAPERS_DIR.exists():
        issues.append(f"Papers directory not found: {PAPERS_DIR}")

    return {
        'valid': len(issues) == 0,
        'issues': issues
    }


def get_config_info() -> str:
    """Return a summary of current configuration."""
    return f"""Vault Configuration:
  Workspace:     {WORKSPACE_ROOT}
  Papers:        {PAPERS_DIR}
  PDFs:          {PDFS_DIR}
  AI Lab PDFs:   {AI_LAB_PDFS_DIR}
  Extracts:      {PDF_EXTRACTS_DIR}
  Authors:       {AUTHORS_DIR}
  Statistics:    {STATISTICS_DIR}
  Dashboards:    {DASHBOARDS_DIR}
  Zotero:        {ZOTERO_DIR}
"""


# =============================================================================
# Convenience for scripts that import this
# =============================================================================

# Legacy aliases for backward compatibility
VAULT_ROOT = WORKSPACE_ROOT
REPO_ROOT = WORKSPACE_ROOT.parent  # The parent containing .venv, .agent, etc.


if __name__ == "__main__":
    # When run directly, show configuration
    print(get_config_info())
    result = validate_paths()
    if result['valid']:
        print("✅ All paths valid.")
    else:
        print("❌ Issues found:")
        for issue in result['issues']:
            print(f"  - {issue}")
