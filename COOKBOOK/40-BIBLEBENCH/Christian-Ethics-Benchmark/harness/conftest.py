"""Pytest configuration: make the walkworthy package importable and expose the
benchmark root (parent of harness/) so loader tests can read the real seed files.
"""
import sys
from pathlib import Path

HARNESS_DIR = Path(__file__).resolve().parent
BENCHMARK_ROOT = HARNESS_DIR.parent

sys.path.insert(0, str(HARNESS_DIR))

import pytest


@pytest.fixture(scope="session")
def benchmark_root() -> Path:
    return BENCHMARK_ROOT
