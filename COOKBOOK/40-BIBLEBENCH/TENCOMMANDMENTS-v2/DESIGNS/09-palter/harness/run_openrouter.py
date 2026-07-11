"""Unified offline preflight and guarded live entry point for PALTER OpenRouter."""

import argparse
from pathlib import Path
import sys
from typing import Any, Dict, Optional

_PALTER_ROOT = Path(__file__).resolve().parents[1]
_BIBLEBENCH_ROOT = Path(__file__).resolve().parents[4]
for _root in (_PALTER_ROOT, _BIBLEBENCH_ROOT):
    if str(_root) not in sys.path:
        sys.path.insert(0, str(_root))

from TENCOMMANDMENTS.harness.openrouter import canonical_json

from harness import palter_openrouter as transport
from harness import run_openrouter_smoke


_MODES = {
    "smoke": transport.SMOKE_CONFIG_PATH,
    "full": transport.FULL_CONFIG_PATH,
}


def preflight(mode: str) -> Dict[str, Any]:
    if mode not in _MODES:
        raise ValueError("mode must be smoke or full")
    plan = transport.preflight_config(_MODES[mode])
    return {
        "schema_version": 1,
        "mode": plan.config["mode"],
        "config_sha256": plan.config_sha256,
        "semantic_calls": len(plan.schedule),
        "paid_call_ceiling": len(plan.preflight.calls),
        "cost_upper_bound_usd": str(plan.preflight.cost_upper_bound),
        "cost_cap_usd": str(plan.preflight.cost_cap),
        "bt_status": plan.config["bt_status"],
        "eligible_for_empirical_decision": False,
        "network_calls": 0,
    }


def run(
    mode: str,
    output_dir: Path,
    *,
    api_key: Optional[str] = None,
    resume: bool = False,
):
    if mode not in _MODES:
        raise ValueError("mode must be smoke or full")
    plan = transport.preflight_config(_MODES[mode])
    if mode == "full" and plan.config["bt_status"] != "PASS":
        raise ValueError("live full diagnostic prohibited while BT status is NOT_RUN")
    if mode == "smoke":
        return run_openrouter_smoke.run_smoke(
            output_dir,
            api_key=api_key,
            resume=resume,
        )
    return run_openrouter_smoke.run_plan(
        plan,
        output_dir,
        api_key=api_key,
        resume=resume,
        result_filename="full-result.json",
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=sorted(_MODES), required=True)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args(argv)
    if args.preflight_only:
        if args.output_dir is not None or args.resume:
            parser.error("offline preflight accepts neither output nor resume")
        print(canonical_json(preflight(args.mode)))
        return 0
    if args.output_dir is None:
        parser.error("--output-dir is required for live execution")
    result = run(args.mode, args.output_dir, resume=args.resume)
    print(canonical_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["main", "preflight", "run"]
