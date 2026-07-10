#!/usr/bin/env python3
"""Credential-free Track-A and private-gold leakage audit for ZEROSUM P1."""

from __future__ import annotations

import argparse
from collections.abc import Mapping, Sequence
import re
from pathlib import Path
import sys
from typing import Any, Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audits.schema_audit import (  # noqa: E402
    DEFAULT_BANK,
    load_jsonl,
    make_finding,
    report_exit_code,
    write_reports,
)


TRACK_A_FORBIDDEN_RE = re.compile(
    r"\b(commandments?|scriptures?|bible|biblical|exodus|deuteronomy|covet|"
    r"christians?|gods?|sin|jesus|christ|gospel|church(?:es)?|prayers?|worship|"
    r"religion|religious|theology|theological|torah|qur'?an|testament|"
    r"allah|yahweh|islam|muslim|mosque|judaism|jewish|synagogue|rabbi|"
    r"hindu|buddh(?:a|ist|ism)|apostle|prophet|"
    r"saul|cain|abram|philippians|timothy|positional|"
    r"spite|sufficiency|hedged)\b|welfare(?:[ _-]+)optimal|payoff matr(?:ix|ices)",
    re.IGNORECASE,
)
GOLD_KEY_NAMES = frozenset({
    "capability_control",
    "certificate",
    "comparison_condition",
    "condition",
    "correct_option_id",
    "diagnostic",
    "expected_answer",
    "expected_class",
    "expected_fr_direction",
    "expected_strong_behavior",
    "failure_modes",
    "fixture_intended_class",
    "implicated_clauses",
    "label_type",
    "normative_grade",
    "option_text_by_class",
    "paired_observations",
    "proof_checks",
    "scoring_notes",
    "track_b_family",
    "track_b_rubric_hook",
    "welfare_optimal_option_id",
})


def _model_surfaces(record: Mapping[str, Any]) -> Iterable[Tuple[str, str]]:
    for field in ("model_prompt", "setup", "agentic_action"):
        value = record.get(field)
        if isinstance(value, str):
            yield field, value
    escalation = record.get("escalation")
    if isinstance(escalation, list):
        for index, turn in enumerate(escalation):
            if isinstance(turn, Mapping) and isinstance(turn.get("user"), str):
                yield "escalation.%d.user" % index, turn["user"]
    options = record.get("options")
    if isinstance(options, list):
        for index, option in enumerate(options):
            if isinstance(option, Mapping) and isinstance(option.get("text"), str):
                yield "options.%d.text" % index, option["text"]


def _nested_gold_paths(value: Any, prefix: tuple = ()) -> List[str]:
    paths: List[str] = []
    if isinstance(value, Mapping):
        for key, child in value.items():
            current = prefix + (str(key),)
            if str(key) in GOLD_KEY_NAMES:
                paths.append(".".join(current))
            paths.extend(_nested_gold_paths(child, current))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            paths.extend(_nested_gold_paths(child, prefix + (str(index),)))
    return paths


def audit_leakage(bank: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    """Pure validation that model-facing surfaces contain no Track-A or gold leakage."""
    if not isinstance(bank, Sequence) or isinstance(bank, (str, bytes)):
        return [make_finding(
            audit="leakage",
            code="leakage.bank_not_sequence",
            severity="hard",
            message="Public bank must be a sequence of objects.",
        )]

    findings: List[Dict[str, Any]] = []
    for index, record in enumerate(bank):
        if not isinstance(record, Mapping):
            findings.append(make_finding(
                audit="leakage",
                code="leakage.public_not_object",
                severity="hard",
                message="Public record is not an object.",
                record_id="index:%d" % index,
            ))
            continue
        record_id = record.get("id")
        finding_id = record_id if isinstance(record_id, str) and record_id else "index:%d" % index
        leaked_paths = sorted(set(_nested_gold_paths(record)))
        if leaked_paths:
            findings.append(make_finding(
                audit="leakage",
                code="leakage.private_gold_key",
                severity="hard",
                message="Private gold keys appear in the public record.",
                record_id=finding_id,
                details={"paths": leaked_paths},
            ))

        prompt = record.get("model_prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            findings.append(make_finding(
                audit="leakage",
                code="leakage.missing_model_prompt",
                severity="hard",
                message="Record lacks a nonempty model_prompt for leakage inspection.",
                record_id=finding_id,
            ))

        matches: Dict[str, set] = {}
        literal_canary_locations: List[str] = []
        canonical_canary = record.get("canary")
        for location, surface in _model_surfaces(record):
            tokens = {match.group(0).lower() for match in TRACK_A_FORBIDDEN_RE.finditer(surface)}
            if "|" in surface:
                tokens.add("|")
            if tokens:
                matches[location] = tokens
            if (
                isinstance(canonical_canary, str)
                and canonical_canary
                and canonical_canary in surface
            ):
                literal_canary_locations.append(location)
            if re.search(r"\bcanary\b", surface, re.IGNORECASE):
                matches.setdefault(location, set()).add("canary")
        if matches:
            findings.append(make_finding(
                audit="leakage",
                code="leakage.track_a_token",
                severity="hard",
                message="Track-A surface contains religious, rubric, class, or matrix language.",
                record_id=finding_id,
                details={
                    "locations": {
                        location: sorted(tokens)
                        for location, tokens in sorted(matches.items())
                    }
                },
            ))
        if literal_canary_locations:
            findings.append(make_finding(
                audit="leakage",
                code="leakage.record_canary_rendered",
                severity="hard",
                message="Canonical record canary appears in model-facing text.",
                record_id=finding_id,
                details={"locations": sorted(set(literal_canary_locations))},
            ))
    return sorted(
        findings,
        key=lambda finding: (
            finding["code"], finding.get("record_id", ""), finding["message"]
        ),
    )


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bank", type=Path, default=DEFAULT_BANK)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "reports")
    parser.add_argument("--report-date", default=None)
    args = parser.parse_args(argv)
    checked_records = 0
    try:
        bank = load_jsonl(args.bank)
        checked_records = len(bank)
        findings = audit_leakage(bank)
    except (OSError, TypeError, ValueError) as exc:
        findings = [make_finding(
            audit="leakage",
            code="leakage.input_error",
            severity="hard",
            message=str(exc),
        )]
    write_reports(
        findings,
        audit_slug="leakage-audit",
        audit_title="ZEROSUM P1 leakage audit",
        checked_records=checked_records,
        output_dir=args.output_dir,
        report_date=args.report_date,
    )
    return report_exit_code(findings)


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["audit_leakage", "main"]
