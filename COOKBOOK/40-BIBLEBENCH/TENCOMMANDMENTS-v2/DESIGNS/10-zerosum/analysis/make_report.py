#!/usr/bin/env python3
"""Render a disclosure-first Markdown report from machine-readable results."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping


def _lower_bool(value: Any) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    return str(value)


def _append_analysis(lines: list, analysis: Mapping[str, Any]) -> None:
    """Append machine-derived estimand values without recomputing them."""

    estimands = analysis.get("estimands", {})
    if not isinstance(estimands, Mapping) or not estimands:
        return
    lines.extend(["## Estimand results", ""])
    scalar_fields = (
        "raw_beta_rho", "p_positional_rho_neg1", "p_positional_rho_pos1",
        "delta_endpoint", "zs_design_100", "ci_width", "fr_at_misaligned",
        "gr_rate", "sf_match_rate", "naive_positivity_rate",
        "frame_confidence_interaction", "domain_macro_average",
        "domain_estimable_n", "domain_nonestimable_n",
        "worst_domain", "worst_domain_score",
        "capability_residualized_beta_rho", "response_n", "answered_n",
        "refusal_n", "refusal_rate", "parked_n", "parked_rate",
        "capability_coverage_rate", "estimand_status", "estimator",
        "optimizer_converged", "optimizer_penalty",
        "quadrature_nodes", "domain_random_intercept_sd",
        "bootstrap_reps", "bootstrap_attempted_reps",
        "bootstrap_successful_reps", "bootstrap_failed_reps",
        "bootstrap_status",
    )
    for estimand_name, estimand in estimands.items():
        if not isinstance(estimand, Mapping):
            continue
        lines.extend([
            "### `%s`" % estimand_name,
            "",
            "- gold_basis: `%s`" % estimand.get("gold_basis", "UNKNOWN"),
        ])
        models = estimand.get("models", {})
        if not isinstance(models, Mapping):
            lines.append("")
            continue
        for model_id, metrics in models.items():
            if not isinstance(metrics, Mapping):
                continue
            lines.extend(["", "#### `%s`" % model_id, ""])
            for field in scalar_fields:
                if field in metrics:
                    lines.append("- %s: %s" % (field, metrics[field]))
            if (
                metrics.get("raw_beta_ci_low") is not None
                and metrics.get("raw_beta_ci_high") is not None
            ):
                lines.append(
                    "- raw_beta_rho CI: [%s, %s]"
                    % (metrics["raw_beta_ci_low"], metrics["raw_beta_ci_high"])
                )
            if metrics.get("ci_low") is not None and metrics.get("ci_high") is not None:
                lines.append(
                    "- ZS_design_100 CI: [%s, %s]"
                    % (metrics["ci_low"], metrics["ci_high"])
                )
            if isinstance(metrics.get("domain_scores"), Mapping):
                lines.append(
                    "- domain_scores: `%s`"
                    % json.dumps(metrics["domain_scores"], sort_keys=True)
                )
        lines.append("")


def _append_cross_model(lines: list, analysis: Mapping[str, Any]) -> None:
    cross_model = analysis.get("cross_model_descriptive")
    if not isinstance(cross_model, Mapping):
        return
    lines.extend(["## Cross-model descriptive diagnostics", ""])
    for field in (
        "n_models", "zs_vs_comprehension_correlation", "significance_claim",
        "capability_complete",
    ):
        if field in cross_model:
            lines.append("- %s: %s" % (field, _lower_bool(cross_model[field])))
    lines.append("")


def _append_gate_evidence(lines: list, gate: Mapping[str, Any]) -> None:
    if not gate:
        return
    lines.extend(["## Discrimination gate evidence", ""])
    for title, field in (
        ("Thresholds", "thresholds"),
        ("Observed", "observed"),
        ("Checks", "checks"),
    ):
        values = gate.get(field)
        if not isinstance(values, Mapping):
            continue
        lines.extend(["### %s" % title, ""])
        for name, value in sorted(values.items()):
            lines.append("- %s: %s" % (name, _lower_bool(value)))
        lines.append("")


def render_report(payload: Mapping[str, Any]) -> str:
    """Render only values present in the result payload; never recompute gates."""

    analysis = payload.get("analysis", {})
    gate = analysis.get("discrimination_gate", {}) if isinstance(analysis, Mapping) else {}
    lines = [
        "# ZEROSUM P1 authoring and validation report",
        "",
        "**Status:** `%s`" % payload.get("status", "UNKNOWN"),
        "",
        "This report is generated from machine-readable results. Synthetic fixtures are plumbing evidence only; they are not human labels or model-performance evidence.",
        "",
        "## Eligibility",
        "",
        "- eligible_for_empirical_decision: %s" % _lower_bool(payload.get("eligible_for_empirical_decision")),
        "- classifier gate: `%s`" % payload.get("classifier_gate_status", "UNKNOWN"),
        "- live pilot: `%s`" % payload.get("live_pilot_status", "UNKNOWN"),
        "- LLM fine-tune gate: `%s`" % payload.get("finetune_gate_status", "UNKNOWN"),
        "- discrimination calculation: `%s`" % gate.get("verdict", "NOT_RUN"),
        "",
        "## Provenance",
        "",
        "- response count: %s" % payload.get("response_count", "UNKNOWN"),
        "- manifest SHA-256: `%s`" % payload.get("manifest_sha256", "UNKNOWN"),
        "- config SHA-256: `%s`" % payload.get("config_sha256", "UNKNOWN"),
        "",
    ]
    if isinstance(analysis, Mapping):
        _append_analysis(lines, analysis)
        _append_cross_model(lines, analysis)
        _append_gate_evidence(lines, gate)
    lines.extend([
        "## Pending external phases",
        "",
        "The human annotation/classifier gate, three-model/two-vendor live run, and required mid-tier-model 10% fine-tune probe remain pending unless their statuses above explicitly show an eligible empirical pass.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.result.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_report(payload), encoding="utf-8")
    print("wrote %s" % args.output)


if __name__ == "__main__":
    main()


__all__ = ["render_report"]
