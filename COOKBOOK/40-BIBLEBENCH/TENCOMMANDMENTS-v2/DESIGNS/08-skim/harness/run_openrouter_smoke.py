#!/usr/bin/env python3
"""Explicit paid entry point for the frozen cheap OpenRouter smoke."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from typing import Any, Mapping, Optional, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BENCH_ROOT = ROOT.parents[2]
for search_root in (ROOT, BENCH_ROOT):
    if str(search_root) not in sys.path:
        sys.path.insert(0, str(search_root))

from harness.model_adapters import OpenRouterClient  # noqa: E402
from harness.run_p1 import (  # noqa: E402
    _bind_clients_to_smoke_config,
    _load_frozen_smoke_config,
    run_cheap_smoke,
)


def main(
    argv: Optional[Sequence[str]] = None,
    *,
    environ: Optional[Mapping[str, str]] = None,
    client_factory: Optional[Any] = None,
    smoke_runner: Optional[Any] = None,
) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute-paid-live", action="store_true")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args(argv)
    if not args.execute_paid_live:
        parser.error("paid smoke requires explicit --execute-paid-live opt-in")

    environment = os.environ if environ is None else environ
    api_key = environment.get("OPENROUTER_API_KEY")
    if not isinstance(api_key, str) or not api_key:
        parser.error("OPENROUTER_API_KEY is required for paid smoke")
    config, _config_sha256 = _load_frozen_smoke_config(args.config)
    factory = OpenRouterClient if client_factory is None else client_factory
    runner = run_cheap_smoke if smoke_runner is None else smoke_runner
    clients = tuple(
        factory(
            row["model_id"],
            family=row["family"],
            vendor=row["vendor"],
            provider=row["provider"],
            api_key=api_key,
            max_tokens=config["max_tokens"],
            cost_cap_usd=config["cost_cap_usd"],
        )
        for row in config["model_roster"]
    )
    _bind_clients_to_smoke_config(
        clients,
        config,
        seed=config["seed"],
        cost_cap_usd=config["cost_cap_usd"],
    )
    result = runner(
        clients=clients,
        seed=config["seed"],
        output_dir=args.output_dir,
        cost_cap_usd=config["cost_cap_usd"],
        config_path=args.config,
    )
    print(
        json.dumps(
            {
                "status": result["status"],
                "scheduled_requests": result["scheduled_requests"],
                "paid_calls": result["paid_calls"],
                "total_cost_usd": result["total_cost_usd"],
                "preflight_cost_upper_bound_usd": result[
                    "preflight_cost_upper_bound_usd"
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
