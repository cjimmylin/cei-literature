#!/usr/bin/env python3
"""Explicit public-only GPT-5.4-mini Azure qualification entry point."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

if __package__ in {None, ""}:
    _BANK_ROOT = Path(__file__).resolve().parents[1]
    if os.fspath(_BANK_ROOT) not in sys.path:
        sys.path.insert(0, os.fspath(_BANK_ROOT))

from pilot import manifest
from pilot import run_cheap_openrouter as qualification


def build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Run the public-only CHARITROC GPT-5.4-mini Azure "
            "OpenRouter qualification"
        )
    )
    children = parser.add_subparsers(dest="command", required=True)
    for command in qualification.COMMANDS:
        child = children.add_parser(command)
        child.add_argument("--out", required=True)
        child.add_argument(
            "--run-mode", choices=qualification.RUN_MODES, required=True
        )
        if command in {"access", "canary", "smoke"}:
            child.add_argument("--retry-failed", action="store_true")
        if command == "verify":
            child.add_argument(
                "--scope", choices=qualification.VERIFY_SCOPES,
                default="all",
            )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.run_mode == "mock":
        raise SystemExit(
            "mock CLI execution has no hidden fake dependencies; use the "
            "explicit programmatic mock harness"
        )
    runner = qualification.CheapOpenRouterQualificationRunner(
        bank_root=Path(__file__).resolve().parents[1],
        out_dir=args.out,
        run_mode=args.run_mode,
        profile_id=manifest.GPT54_MINI_PROFILE_ID,
    )
    if args.command == "access":
        result = runner.access(retry_failed=args.retry_failed)
    elif args.command == "canary":
        result = runner.canary(retry_failed=args.retry_failed)
    elif args.command == "smoke":
        result = runner.smoke(retry_failed=args.retry_failed)
    elif args.command == "verify":
        result = runner.verify(args.scope)
    else:
        result = runner.report()
    sys.stdout.write(
        qualification._canonical_bytes(result).decode("utf-8") + "\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
