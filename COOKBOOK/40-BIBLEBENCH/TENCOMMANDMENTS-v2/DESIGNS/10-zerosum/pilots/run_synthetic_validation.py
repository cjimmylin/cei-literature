#!/usr/bin/env python3
"""Reproduce the disclosed ZEROSUM P1 authoring/synthetic validation run."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Dict, Mapping


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from analysis.make_report import render_report  # noqa: E402
from analysis.slope import fit_all  # noqa: E402
from audits.finetune_probe import run_surrogate_probe  # noqa: E402
from audits.leakage_audit import audit_leakage  # noqa: E402
from audits.lexical_baseline import run_lexical_audit  # noqa: E402
from audits.matched_surface_audit import audit_matched_surface  # noqa: E402
from audits.schema_audit import audit_schema, write_reports  # noqa: E402
from calibration.synthetic_fixtures import generate_synthetic_fixtures  # noqa: E402
from harness.run_p1 import run_synthetic  # noqa: E402
from itembank.build_bank import build_bank, write_bank  # noqa: E402
from scoring.calibration_gate import evaluate_calibration  # noqa: E402
from scoring.judge_prompts import JUDGE_FAMILIES  # noqa: E402
from zerosum_common import write_jsonl  # noqa: E402


PROFILES = (
    "structure_sensitive",
    "flat_positional",
    "perverse_harmony",
    "null_fr",
    "gr_floor",
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def _write_static_reports(
    bank, gold, manifest, *, report_date: str, output_dir: Path
) -> Dict[str, Any]:
    audits = {
        "schema": audit_schema(bank, gold, manifest),
        "leakage": audit_leakage(bank),
        "matched_surface": audit_matched_surface(bank, manifest),
    }
    for slug, findings in audits.items():
        write_reports(
            findings,
            audit_slug="%s-audit" % slug.replace("_", "-"),
            audit_title="ZEROSUM P1 %s audit" % slug.replace("_", " "),
            checked_records=len(bank),
            output_dir=output_dir,
            report_date=report_date,
        )
    hard = [
        finding for findings in audits.values() for finding in findings
        if finding.get("severity") == "hard"
    ]
    if hard:
        raise RuntimeError("static audits produced %d hard findings" % len(hard))
    return {
        slug: {
            "hard_findings": sum(row.get("severity") == "hard" for row in findings),
            "soft_findings": sum(row.get("severity") == "soft" for row in findings),
            "status": "PASS",
        }
        for slug, findings in audits.items()
    }


def run_validation(
    *,
    report_date: str = "2026-07-09",
    harness_seed: int = 2026070901,
    bootstrap_reps: int = 200,
    output_dir: Path = None,
) -> Dict[str, Any]:
    """Execute every credential-free P1 check and write reproducible artifacts."""

    output_dir = Path(output_dir or (HERE / "20260709-synthetic-p1-run"))
    output_dir.mkdir(parents=True, exist_ok=True)
    write_bank(seed=20260709, output_root=ROOT / "itembank")
    bank, gold, manifest = build_bank(seed=20260709)

    static = _write_static_reports(
        bank,
        gold,
        manifest,
        report_date=report_date,
        output_dir=ROOT / "audits" / "reports",
    )
    primaries = [row for row in bank if row["record_type"] == "advice_primary"]
    lexical = run_lexical_audit(primaries, retry_count=0, seed=20260709)
    if lexical["normalized_style_status"] != "PASS":
        raise RuntimeError("registered normalized-style X2 gate did not pass")
    surrogate = run_surrogate_probe(primaries, seed=20260709)

    calibration_fixtures = generate_synthetic_fixtures(count=250, seed=20260709)
    calibration = evaluate_calibration(
        calibration_fixtures, bootstrap_samples=400, seed=20260709
    ).to_dict()
    if calibration["verdict"] != "NOT_RUN_HUMAN" or calibration["eligible_for_empirical_decision"]:
        raise RuntimeError("synthetic calibration provenance guard failed")

    harness = run_synthetic(
        bank, gold, profiles=PROFILES, seed=harness_seed
    )
    analysis = fit_all(
        harness["responses"],
        bank=bank,
        gold=gold,
        bootstrap_reps=bootstrap_reps,
        seed=20260709,
    )
    if analysis["discrimination_gate"]["verdict"] != "EXERCISE_ONLY":
        raise RuntimeError("synthetic discrimination result was not quarantined")

    response_path = output_dir / "synthetic-responses.jsonl"
    fixture_path = output_dir / "synthetic-calibration-fixtures.jsonl"
    write_jsonl(response_path, harness["responses"])
    write_jsonl(fixture_path, calibration_fixtures)
    harness_summary = dict(harness)
    harness_summary.pop("responses")
    harness_summary["response_count"] = len(harness["responses"])
    _write_json(output_dir / "synthetic-harness-summary.json", harness_summary)
    _write_json(output_dir / "synthetic-calibration-result.json", calibration)
    _write_json(output_dir / "synthetic-analysis.json", analysis)
    _write_json(output_dir / "x2-lexical-result.json", lexical)
    _write_json(output_dir / "x2-finetune-surrogate-result.json", surrogate)

    config_path = ROOT / "configs" / "p1-synthetic.json"
    manifest_path = ROOT / "itembank" / "manifest.json"
    result = {
        "schema_version": 1,
        "study_id": "10CB-ZEROSUM-P1",
        "report_date": report_date,
        "status": "HARNESS_VALIDATION_ONLY",
        "eligible_for_empirical_decision": False,
        "classifier_gate_status": "NOT_RUN_HUMAN",
        "live_pilot_status": "BLOCKED_PRECONDITIONS",
        "finetune_gate_status": "NOT_RUN_LLM",
        "provenance": {
            "authoring_orchestrator_family": "codex-gpt-5",
            "generator_family": "zerosum-payoff-v1",
            "synthetic_profile_family": "deterministic_planted_fixture",
            "judge_families": list(JUDGE_FAMILIES),
        },
        "record_counts": {
            "total": len(bank),
            "by_record_type": dict(sorted(Counter(row["record_type"] for row in bank).items())),
        },
        "response_arithmetic": {
            "profiles": len(PROFILES),
            "responses_per_profile": len(harness["responses"]) // len(PROFILES),
            "total_synthetic_responses": len(harness["responses"]),
            "synthetic_calibration_fixtures": len(calibration_fixtures),
            "live_responses": 0,
            "human_labels": 0,
        },
        "response_count": len(harness["responses"]),
        "manifest_sha256": _sha256(manifest_path),
        "config_sha256": _sha256(config_path),
        "preregistration_sha256": _sha256(ROOT / "preregistration.md"),
        "response_sha256": _sha256(response_path),
        "calibration_fixture_sha256": _sha256(fixture_path),
        "static_audits": static,
        "x2": {
            "lexical": lexical,
            "finetune_surrogate": surrogate,
        },
        "calibration": calibration,
        "analysis": analysis,
        "pending": [
            "human-code at least 200 unique open responses with two blinded humans and adjudication",
            "run at least three frozen models from at least two vendors after calibration passes",
            "run the registered 10% fine-tune probe on a real mid-tier LLM",
        ],
    }
    result_path = output_dir / "validation-result.json"
    _write_json(result_path, result)
    report_path = HERE / "20260709-zerosum-p1-authoring-report.md"
    report_path.write_text(render_report(result), encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-date", default="2026-07-09")
    parser.add_argument("--harness-seed", type=int, default=2026070901)
    parser.add_argument("--bootstrap-reps", type=int, default=200)
    parser.add_argument("--output-dir", type=Path, default=HERE / "20260709-synthetic-p1-run")
    args = parser.parse_args()
    result = run_validation(
        report_date=args.report_date,
        harness_seed=args.harness_seed,
        bootstrap_reps=args.bootstrap_reps,
        output_dir=args.output_dir,
    )
    print("wrote %d synthetic responses" % result["response_count"])
    print("status: %s" % result["status"])
    print("eligible_for_empirical_decision: false")


if __name__ == "__main__":
    main()


__all__ = ["run_validation"]
