"""CLI for the immutable TABLETS aggregate synthetic-validation bundle."""

import argparse
from pathlib import Path
import sys


TABLETS_ROOT = Path(__file__).resolve().parents[1]
if str(TABLETS_ROOT) not in sys.path:
    sys.path.insert(0, str(TABLETS_ROOT))

from analysis.synthetic_validation import (  # noqa: E402
    check_synthetic_bundle,
    write_synthetic_bundle,
)


DEFAULT_OUTPUT_DIR = (
    Path(__file__).resolve().parent / "20260711-synthetic-validation-r1"
)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify an existing bundle against current frozen inputs and code",
    )
    args = parser.parse_args(argv)
    if args.check:
        check_synthetic_bundle(args.output_dir)
        print("status=VALID")
        return 0
    written = write_synthetic_bundle(args.output_dir)
    for name in ("result", "report", "manifest"):
        print("%s=%s" % (name, written[name]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["DEFAULT_OUTPUT_DIR", "main"]
