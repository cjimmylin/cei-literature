"""Make `runner`, `analysis`, and the shared fixtures importable without installing a package."""
import os
import sys

_P0_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../DUPLEX-P0
_TESTS = os.path.dirname(os.path.abspath(__file__))
for p in (_P0_ROOT, _TESTS):
    if p not in sys.path:
        sys.path.insert(0, p)

CONFIG_ROSTER = os.path.join(_P0_ROOT, "config", "p0-roster.yaml")
