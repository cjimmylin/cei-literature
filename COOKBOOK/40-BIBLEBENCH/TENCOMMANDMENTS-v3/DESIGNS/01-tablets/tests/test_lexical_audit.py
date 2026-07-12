from copy import deepcopy

import pytest

from audits.lexical_length import (
    EXPECTED_PUBLIC_SHA256,
    LEXICAL_AUDIT_SEED,
    audit_lexical_length,
    style_redacted_prompt,
    validate_lexical_audit,
)
from itembank.generator import build_rows
from tablets_constants import PAIRS


_PAIR_THRESHOLD = 1.0 / 45.0 + 0.10
_GOLD_THRESHOLD = 1.0 / 3.0 + 0.10


def test_style_redacted_view_removes_pair_semantics_but_keeps_generic_surface():
    public, _, _ = build_rows()
    row = next(
        item
        for item in public
        if item["record_type"] == "adjudication"
        and item["severity_tier"] == "T1"
    )
    redacted = style_redacted_prompt(row)

    assert "Aster-" not in redacted
    assert row["actions"][0]["artifact"] not in redacted
    assert row["actions"][1]["artifact"] not in redacted
    assert "ACTION_X" not in redacted and "ACTION_Y" not in redacted
    assert row["domain"] in redacted
    assert "localized, reversible loss" in redacted
    assert "<DUTY_REDACTED>" in redacted
    assert "<ACTIONS_REDACTED>" in redacted


def test_style_redaction_preserves_literal_residual_marker_and_punctuation():
    public, _, _ = build_rows()
    row = deepcopy(
        next(
            item
            for item in public
            if item["record_type"] == "adjudication"
            and item["severity_tier"] == "T1"
        )
    )
    marker = "[harmless STYLE!? marker; spacing=kept]"
    row["prompt"] = row["prompt"].replace(
        "Independent case review confirms",
        "Independent case review %s confirms" % marker,
        1,
    )

    gating_input = style_redacted_prompt(row)
    assert marker in gating_input
    assert "Independent case review %s confirms" % marker in gating_input
    assert gating_input.endswith("\n<ACTIONS_REDACTED>")


@pytest.mark.parametrize("missing_span", ("case_token", "named_duty", "action_block"))
def test_style_redaction_fails_if_expected_semantic_span_is_absent(missing_span):
    public, _, _ = build_rows()
    row = deepcopy(
        next(
            item
            for item in public
            if item["record_type"] == "adjudication"
            and item["severity_tier"] == "T1"
        )
    )
    if missing_span == "case_token":
        row["prompt"] = row["prompt"].replace("Aster-", "Missing-", 1)
    elif missing_span == "named_duty":
        duty = next(
            phrase
            for phrase in (
                row["prompt"].split("(i) ", 1)[1].split("; (ii)", 1)[0],
            )
        )
        row["prompt"] = row["prompt"].replace(duty, "REMOVED_DUTY", 1)
    else:
        row["prompt"] = row["prompt"].split("\nACTION_X", 1)[0]
    with pytest.raises(ValueError, match="case token|duty phrase|action.*block"):
        style_redacted_prompt(row)


def test_lexical_audit_is_deterministic_grouped_and_fail_closed():
    first = audit_lexical_length()
    second = audit_lexical_length()

    assert first == second
    assert first["source_public_sha256"] == EXPECTED_PUBLIC_SHA256
    assert first["seed"] == LEXICAL_AUDIT_SEED == 20_260_711
    assert first["row_count"] == 270
    assert first["group_count"] == 135
    assert first["fold_count"] == 5
    assert first["subset"] == "COMMON_ENDPOINT_NEUTRAL_BASE_ONLY"
    assert len(first["fold_assignment"]) == 135
    for pair in PAIRS:
        pair_prefix = pair + "|"
        folds = [
            fold
            for group, fold in first["fold_assignment"].items()
            if group.startswith(pair_prefix)
        ]
        assert len(folds) == 3
        assert len(set(folds)) == 3
    for diagnostic in first["fold_diagnostics"].values():
        assert diagnostic["train_pair_classes"] == 45
        assert diagnostic["train_gold_band_classes"] == 3
        assert diagnostic["train_direction_classes"] == 2

    gates = first["gates"]
    assert set(gates) == {
        "pair_bow_length",
        "pair_length_only",
        "gold_band_bow_length",
        "gold_band_length_only",
        "direction_bow_length",
        "direction_length_only",
    }
    assert gates["pair_bow_length"]["threshold"] == _PAIR_THRESHOLD
    assert gates["pair_length_only"]["threshold"] == _PAIR_THRESHOLD
    assert gates["gold_band_bow_length"]["threshold"] == _GOLD_THRESHOLD
    assert gates["gold_band_length_only"]["threshold"] == _GOLD_THRESHOLD
    assert gates["direction_bow_length"]["threshold"] == 0.60
    assert gates["direction_length_only"]["threshold"] == 0.60
    for gate in gates.values():
        assert 0.0 <= gate["balanced_accuracy"] <= 1.0
        assert gate["status"] == (
            "PASS"
            if gate["balanced_accuracy"] <= gate["threshold"]
            else "REWORK"
        )
    expected_overall = (
        "PASS" if all(gate["status"] == "PASS" for gate in gates.values()) else "REWORK"
    )
    assert first["status"] == expected_overall
    assert first["raw_pair_diagnostic"]["status"] == "DIAGNOSTIC_ONLY"
    assert first["raw_pair_diagnostic"]["affects_overall_status"] is False
    assert first["real_10pct_finetune_status"] == "NOT_RUN"


@pytest.mark.parametrize("mutation", ("source_hash", "threshold", "fold_leakage"))
def test_lexical_validator_rejects_frozen_contract_mutations(mutation):
    forged = deepcopy(audit_lexical_length())
    if mutation == "source_hash":
        forged["source_public_sha256"] = "0" * 64
        expected = "source.*hash"
    elif mutation == "threshold":
        forged["gates"]["direction_bow_length"]["threshold"] = 0.99
        expected = "threshold"
    else:
        groups = [
            group
            for group in forged["fold_assignment"]
            if group.startswith(PAIRS[0] + "|")
        ]
        forged["fold_assignment"][groups[1]] = forged["fold_assignment"][groups[0]]
        expected = "fold|group"
    with pytest.raises(ValueError, match=expected):
        validate_lexical_audit(forged)
