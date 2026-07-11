"""Run or preflight the frozen 51-call PALTER cheap-model engineering smoke."""

import argparse
import os
from pathlib import Path
import sys
from typing import Any, Callable, Dict, Optional

_PALTER_ROOT = Path(__file__).resolve().parents[1]
_BIBLEBENCH_ROOT = Path(__file__).resolve().parents[4]
for _root in (_PALTER_ROOT, _BIBLEBENCH_ROOT):
    if str(_root) not in sys.path:
        sys.path.insert(0, str(_root))

from TENCOMMANDMENTS.harness.openrouter import (
    OPENROUTER_API_KEY_ENV,
    canonical_json,
    verify_model_routes,
)

from harness import palter_openrouter as transport


def smoke_preflight() -> Dict[str, Any]:
    plan = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
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


def run_plan(
    plan: transport.RunPlan,
    output_dir: Path,
    *,
    api_key: Optional[str] = None,
    catalog_verifier: Callable[..., Any] = verify_model_routes,
    client_factory: Optional[Callable[..., Any]] = None,
    resume: bool = False,
    result_filename: str = "smoke-result.json",
) -> Dict[str, Any]:
    """Verify a frozen cheap plan, then execute or resume it exactly."""

    if type(plan) is not transport.RunPlan:
        raise TypeError("run_plan requires an exact PALTER RunPlan")
    if type(result_filename) is not str or not result_filename.endswith(".json"):
        raise ValueError("result filename must be an exact JSON filename")
    output = Path(output_dir)
    if not resume and output.exists():
        raise ValueError("fresh smoke output directory already exists")
    if resume and not output.is_dir():
        raise ValueError("resume smoke output directory does not exist")
    resolved_key = os.environ.get(OPENROUTER_API_KEY_ENV) if api_key is None else api_key
    if type(resolved_key) is not str or not resolved_key:
        raise ValueError("OPENROUTER_API_KEY is required for a live smoke")
    verification = catalog_verifier(
        plan.routes,
        api_key=resolved_key,
        timeout=plan.config["timeout_seconds"],
        max_attempts=plan.config["max_attempts"],
        retry_base_seconds=plan.config["retry_base_seconds"],
    )
    if hasattr(verification, "to_dict"):
        verification_payload = verification.to_dict()
    elif type(verification) is dict:
        verification_payload = dict(verification)
    else:
        raise ValueError("catalog verifier returned an invalid proof")
    result = transport.execute_plan(
        plan,
        output,
        api_key=resolved_key,
        catalog_verification=verification_payload,
        client_factory=client_factory,
        resume=resume,
    )
    transport.write_result(output / result_filename, result)
    if plan.config["mode"] == "CHEAP_OPENROUTER_ENGINEERING_SMOKE":
        from analysis.openrouter_smoke_analysis import write_analysis

        write_analysis(plan, output)
    return result


def run_smoke(
    output_dir: Path,
    *,
    api_key: Optional[str] = None,
    catalog_verifier: Callable[..., Any] = verify_model_routes,
    client_factory: Optional[Callable[..., Any]] = None,
    resume: bool = False,
) -> Dict[str, Any]:
    """Verify only the frozen cheap routes, then execute or resume the smoke."""

    plan = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
    return run_plan(
        plan,
        output_dir,
        api_key=api_key,
        catalog_verifier=catalog_verifier,
        client_factory=client_factory,
        resume=resume,
        result_filename="smoke-result.json",
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args(argv)
    if args.preflight_only:
        if args.resume:
            parser.error("--resume cannot be combined with --preflight-only")
        print(canonical_json(smoke_preflight()))
        return 0
    if args.output_dir is None:
        parser.error("--output-dir is required for a live smoke")
    result = run_smoke(args.output_dir, resume=args.resume)
    print(canonical_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["main", "run_plan", "run_smoke", "smoke_preflight"]
