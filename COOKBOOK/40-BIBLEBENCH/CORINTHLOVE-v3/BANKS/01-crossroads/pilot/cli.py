#!/usr/bin/env python3
"""Public-only CLI for the frozen cheap OpenRouter qualification profile."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

if __package__ in {None, ""}:
    _BANK = Path(__file__).resolve().parents[1]
    if os.fspath(_BANK) not in sys.path:
        sys.path.insert(0, os.fspath(_BANK))
    from pilot import contracts  # type: ignore
    from pilot.openrouter import OpenRouterClient  # type: ignore
    from pilot.runner import QualificationRunner  # type: ignore
    from pilot.verify import verify_run  # type: ignore
else:
    from . import contracts
    from .openrouter import OpenRouterClient
    from .runner import QualificationRunner
    from .verify import verify_run


DEFAULT_BANK = Path(__file__).resolve().parents[1]


class _OfflineClient:
    """Opening and verification do not require a key or network transport."""


def _add_paths(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--root", required=True, type=Path,
                        help="create-only or existing evidence root")
    parser.add_argument("--bank-root", type=Path, default=DEFAULT_BANK,
                        help="CROSSROADS bank root (defaults to this bank)")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Cheap-only CROSSROADS public qualification. No command can access "
            "private episodes, calibrate, rank, or freeze the bank."
        )
    )
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("create", help="freeze a new live run root")
    _add_paths(create)
    create.add_argument(
        "--model", action="append", dest="models",
        choices=tuple(contracts.load_profile()["models"]),
        help="cheap alias; repeat to select a subset (default: all four)",
    )
    create.add_argument(
        "--execution-mode", choices=(
            "path-only staged qualification", "fork-only diagnostic",
        ),
        default="path-only staged qualification",
    )
    for name, help_text in (
        ("open", "validate bindings and summarize an existing root offline"),
        ("access", "run exact-model catalog and access probes"),
        ("canary", "run the frozen six-item staged canary"),
        ("smoke", "run all 30 public items and freeze a diagnostic report"),
        ("diagnose", "run all 30 fork-only public diagnostics"),
        ("verify", "verify byte closure and semantic replay offline"),
    ):
        command = commands.add_parser(name, help=help_text)
        _add_paths(command)
        if name in {"access", "canary", "smoke", "diagnose"}:
            command.add_argument(
                "--retry-failed", action="store_true",
                help=(
                    "authorize one new attempt for a durable prior failure; "
                    "never consumes more than one attempt per invocation"
                ),
            )
        if name == "verify":
            command.add_argument(
                "--phase", choices=("access", "canary", "smoke", "diagnostic", "report")
            )
    return parser


def _emit(value) -> None:
    print(json.dumps(value, sort_keys=True, separators=(",", ":")))


def _open(args, *, live: bool) -> QualificationRunner:
    client = OpenRouterClient() if live else _OfflineClient()
    return QualificationRunner.open(
        args.root, bank_root=args.bank_root, client=client
    )


def main(argv=None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "create":
            client = OpenRouterClient()
            runner = QualificationRunner.create(
                args.root, bank_root=args.bank_root, client=client,
                model_aliases=args.models, provenance=contracts.PROVENANCE_LIVE,
                execution_mode=args.execution_mode,
            )
            _emit(verify_run(args.root, bank_root=args.bank_root))
            return 0
        if args.command == "open":
            _open(args, live=False)
            _emit(verify_run(args.root, bank_root=args.bank_root))
            return 0
        if args.command == "verify":
            _emit(verify_run(
                args.root, bank_root=args.bank_root, require_phase=args.phase
            ))
            return 0
        runner = _open(args, live=True)
        if args.command == "access":
            runner.access(retry_failed=args.retry_failed); required = "access"
        elif args.command == "canary":
            runner.canary(retry_failed=args.retry_failed); required = "canary"
        elif args.command == "smoke":
            runner.smoke(retry_failed=args.retry_failed); required = "report"
        elif args.command == "diagnose":
            runner.diagnose(retry_failed=args.retry_failed); required = "report"
        else:  # pragma: no cover - argparse owns command closure
            raise ValueError("unknown command")
        _emit(verify_run(
            args.root, bank_root=args.bank_root, require_phase=required
        ))
        return 0
    except (OSError, RuntimeError, ValueError) as error:
        parser.error(str(error))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
