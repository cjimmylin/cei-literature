"""Write the deterministic, zero-spend PF-002 owner-review packet."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from biblebench_pilot.preflight import write_preflight_bundle  # noqa: E402


if __name__ == "__main__":
    for path in write_preflight_bundle(ROOT):
        print(path)
