"""Make the package root importable so tests can `import fairgold` and
`import tests.fixtures` when pytest is run from this directory.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
