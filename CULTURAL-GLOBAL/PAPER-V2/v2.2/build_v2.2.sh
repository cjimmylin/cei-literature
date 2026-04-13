#!/usr/bin/env bash
# Single authorized invocation for building the v2.2 combined PDF.
# Run from anywhere — script resolves its own directory.
set -euo pipefail
cd "$(dirname "$(realpath "$0")")"

PYTHON="${PYTHON:-/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python}"
if [ ! -x "$PYTHON" ]; then
  PYTHON="python3"
fi

echo "=== v2.2 build starting ==="
echo "Python: $PYTHON"
echo "CWD:    $(pwd)"
echo

"$PYTHON" generate_combined_pdf_v2.2.py
echo
echo "=== v2.2 build complete ==="
