import os
import sys

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BANK not in sys.path:
    sys.path.insert(0, BANK)
