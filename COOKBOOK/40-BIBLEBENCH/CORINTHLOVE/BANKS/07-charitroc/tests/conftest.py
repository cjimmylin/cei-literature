import os
import sys


BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BANK in sys.path:
    sys.path.remove(BANK)
sys.path.insert(0, BANK)

# The workspace test harness preloads its own top-level ``lib`` package. This
# bank intentionally follows the reference layout (``lib/``), so evict only the
# preloaded external package before collection and let Python resolve this bank's
# package from BANK at sys.path[0].
loaded_lib = sys.modules.get("lib")
if loaded_lib is not None:
    loaded_path = getattr(loaded_lib, "__file__", "") or ""
    if not loaded_path.startswith(BANK):
        for name in [key for key in sys.modules if key == "lib" or key.startswith("lib.")]:
            del sys.modules[name]
