from __future__ import annotations

import sys
from pathlib import Path

import pytest


BANK = Path(__file__).resolve().parents[1]
while str(BANK) in sys.path:
    sys.path.remove(str(BANK))
sys.path.insert(0, str(BANK))

# The vault test bootstrap also has a top-level package named ``lib``.  Pytest
# plugins can import it before collection, so path precedence alone is not
# sufficient: evict only that foreign namespace and let this bank's package be
# imported from the path frozen above.
for module_name in list(sys.modules):
    if module_name == "lib" or module_name.startswith("lib."):
        del sys.modules[module_name]


@pytest.fixture
def bank_root() -> Path:
    return BANK
