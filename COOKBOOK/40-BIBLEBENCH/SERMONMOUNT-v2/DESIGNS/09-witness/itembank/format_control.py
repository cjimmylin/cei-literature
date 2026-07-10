"""Canonical entry point for the MF-1 complexity-matched control battery.

The implementation lives in :mod:`itembank.control_battery`.  This small façade keeps
one import and CLI surface for building, rendering, quantitatively validating, and safely
writing the 15 objective control bases (60 rendered items).
"""
from __future__ import annotations

import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path:
    sys.path.insert(0, str(PKG))

from itembank.control_battery import (  # noqa: E402
    CONTROL_FAMILIES,
    ControlValidationError,
    build_control_bases,
    generate_controls,
    main as _main,
    render_control,
    validate_control_battery as _validate_control_battery,
    write_new_control_artifact as _write_new_control_artifact,
)


def validate_control_battery(cores, bases, rendered):
    """Return the complete quantitative hard-gate findings and report."""
    errors, report = _validate_control_battery(cores, bases, rendered)
    return errors, report


def write_new_control_artifact(path, *, cores=None, bases=None):
    """Validate fully, then create a new artifact without overwrite semantics."""
    return _write_new_control_artifact(path, cores=cores, bases=bases)


def main(argv=None):
    """Check the canonical artifact by default, or handle one explicit safe CLI mode."""
    return _main(argv)


__all__ = [
    "CONTROL_FAMILIES",
    "ControlValidationError",
    "build_control_bases",
    "generate_controls",
    "main",
    "render_control",
    "validate_control_battery",
    "write_new_control_artifact",
]


if __name__ == "__main__":
    raise SystemExit(main())
