from copy import deepcopy
import hashlib
import importlib
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
ITEMBANK = ROOT / "itembank"
AUDITS = ROOT / "audits"


def _load_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _write_jsonl(path, records):
    path.write_text(
        "".join(
            json.dumps(record, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":")) + "\n"
            for record in records
        ),
        encoding="utf-8",
    )


@pytest.fixture(scope="module")
def frozen_bundle():
    return (
        _load_jsonl(ITEMBANK / "bank" / "p1-private.jsonl"),
        _load_jsonl(ITEMBANK / "gold" / "p1-private.gold.jsonl"),
        json.loads((ITEMBANK / "manifest.json").read_text(encoding="utf-8")),
    )


def require_audit(name):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    try:
        return importlib.import_module("audits.%s" % name)
    except ModuleNotFoundError:
        pytest.fail("audits/%s.py has not been implemented" % name)


def _hard_codes(findings):
    return {
        finding["code"]
        for finding in findings
        if finding["severity"] == "hard"
    }


def _canonical_jsonl_bytes(records):
    return (
        "".join(
            json.dumps(
                record,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            ) + "\n"
            for record in records
        )
    ).encode("utf-8")


def _rehash_manifest(manifest, bank, gold):
    manifest["artifacts"]["bank"]["sha256"] = hashlib.sha256(
        _canonical_jsonl_bytes(bank)
    ).hexdigest()
    manifest["artifacts"]["gold"]["sha256"] = hashlib.sha256(
        _canonical_jsonl_bytes(gold)
    ).hexdigest()


def test_schema_audit_rejects_gold_key_in_model_facing_record(frozen_bundle):
    schema = require_audit("schema_audit")
    bank, gold, manifest = deepcopy(frozen_bundle)
    bank[0]["expected_class"] = "welfare_optimal"

    findings = schema.audit_schema(bank, gold, manifest)

    assert "schema.public_forbidden_field" in _hard_codes(findings)


def test_leakage_audit_rejects_religious_token_in_track_a(frozen_bundle):
    leakage = require_audit("leakage_audit")
    bank, _, _ = deepcopy(frozen_bundle)
    bank[0]["model_prompt"] += "\nThis is a commandment from scripture."

    findings = leakage.audit_leakage(bank)

    assert "leakage.track_a_token" in _hard_codes(findings)


def test_schema_audit_rejects_missing_record_canary(frozen_bundle):
    schema = require_audit("schema_audit")
    bank, gold, manifest = deepcopy(frozen_bundle)
    del bank[0]["canary"]

    findings = schema.audit_schema(bank, gold, manifest)

    assert "schema.missing_canary" in _hard_codes(findings)


def test_schema_audit_rejects_rho_outside_registered_grid(frozen_bundle):
    schema = require_audit("schema_audit")
    bank, gold, manifest = deepcopy(frozen_bundle)
    bank[0]["rho"] = 0
    bank[0]["payoff_correlation"] = 0

    findings = schema.audit_schema(bank, gold, manifest)

    assert "schema.rho_outside_grid" in _hard_codes(findings)


def test_matched_surface_audit_rejects_changed_nonnumeric_wording(frozen_bundle):
    matched = require_audit("matched_surface_audit")
    bank, _, manifest = deepcopy(frozen_bundle)
    primary = next(record for record in bank if record["record_type"] == "advice_primary")
    primary["model_prompt"] = primary["model_prompt"].replace(
        "Situation:", "Scenario:", 1
    )

    findings = matched.audit_matched_surface(bank, manifest)

    assert "matched_surface.nonnumeric_mismatch" in _hard_codes(findings)


def test_schema_audit_requires_both_two_sided_failure_poles(frozen_bundle):
    schema = require_audit("schema_audit")
    bank, gold, manifest = deepcopy(frozen_bundle)
    primary_gold = next(
        record for record in gold if record["record_type"] == "advice_primary"
    )
    primary_gold["failure_modes"] = [
        mode
        for mode in primary_gold["failure_modes"]
        if "naive-positivity/harmony-theater" not in mode.lower()
    ]

    findings = schema.audit_schema(bank, gold, manifest)

    assert "schema.two_sided_failure_poles" in _hard_codes(findings)


def test_schema_audit_rejects_broken_parent_linkage_even_when_rehashed(
    frozen_bundle,
):
    schema = require_audit("schema_audit")
    bank, gold, manifest = deepcopy(frozen_bundle)
    child = next(
        record for record in bank
        if record["record_type"] == "comprehension_twin"
    )
    child["parent_id"] = next(
        record["id"] for record in bank
        if record["record_type"] == "advice_primary"
        and record["id"] != child["parent_id"]
    )
    _rehash_manifest(manifest, bank, gold)

    findings = schema.audit_schema(bank, gold, manifest)

    assert "schema.full_bank_semantics" in _hard_codes(findings)
    assert "schema.artifact_hash_mismatch" not in _hard_codes(findings)


def test_schema_audit_rejects_wrong_forced_gold_even_when_rehashed(
    frozen_bundle,
):
    schema = require_audit("schema_audit")
    bank, gold, manifest = deepcopy(frozen_bundle)
    forced_index = next(
        index for index, record in enumerate(bank)
        if record["record_type"] == "forced_anchor"
    )
    option_ids = [option["id"] for option in bank[forced_index]["options"]]
    gold[forced_index]["correct_option_id"] = next(
        option_id for option_id in option_ids
        if option_id != gold[forced_index]["correct_option_id"]
    )
    _rehash_manifest(manifest, bank, gold)

    findings = schema.audit_schema(bank, gold, manifest)

    assert "schema.full_bank_semantics" in _hard_codes(findings)
    assert "schema.artifact_hash_mismatch" not in _hard_codes(findings)


def test_matched_surface_audit_uses_actual_trajectory_not_stale_prompt(
    frozen_bundle,
):
    matched = require_audit("matched_surface_audit")
    bank, _, manifest = deepcopy(frozen_bundle)
    primary = next(
        record for record in bank if record["record_type"] == "advice_primary"
    )
    primary["setup"] += " Changed nonnumeric live-request wording."

    findings = matched.audit_matched_surface(bank, manifest)

    assert "matched_surface.trajectory_nonnumeric_mismatch" in _hard_codes(findings)


def test_leakage_audit_rejects_common_religious_vocabulary(frozen_bundle):
    leakage = require_audit("leakage_audit")
    bank, _, _ = deepcopy(frozen_bundle)
    twin = next(
        record for record in bank if record["record_type"] != "advice_primary"
    )
    twin["model_prompt"] += " Jesus teaches this."

    findings = leakage.audit_leakage(bank)

    assert "leakage.track_a_token" in _hard_codes(findings)


@pytest.mark.parametrize(
    "leaked_phrase", ("Ten Commandments", "Allah", "payoff matrices")
)
def test_leakage_audit_rejects_plural_and_interfaith_variants(
    frozen_bundle, leaked_phrase
):
    leakage = require_audit("leakage_audit")
    bank, _, _ = frozen_bundle
    bank = deepcopy(bank)
    bank[0]["model_prompt"] += " %s." % leaked_phrase

    findings = leakage.audit_leakage(bank)

    assert "leakage.track_a_token" in _hard_codes(findings)


def test_leakage_audit_rejects_nested_private_only_key(frozen_bundle):
    leakage = require_audit("leakage_audit")
    bank, _, _ = deepcopy(frozen_bundle)
    choice = next(record for record in bank if "options" in record)
    choice["options"][0]["expected_fr_direction"] = "recover"

    findings = leakage.audit_leakage(bank)

    assert "leakage.private_gold_key" in _hard_codes(findings)


def test_frozen_bank_has_no_hard_static_findings(frozen_bundle):
    schema = require_audit("schema_audit")
    leakage = require_audit("leakage_audit")
    matched = require_audit("matched_surface_audit")
    bank, gold, manifest = frozen_bundle

    findings = (
        schema.audit_schema(bank, gold, manifest)
        + leakage.audit_leakage(bank)
        + matched.audit_matched_surface(bank, manifest)
    )

    assert _hard_codes(findings) == set()


@pytest.mark.parametrize(
    ("module_name", "audit_slug", "extra_args"),
    [
        (
            "schema_audit",
            "schema-audit",
            [
                "--gold", str(ITEMBANK / "gold" / "p1-private.gold.jsonl"),
                "--manifest", str(ITEMBANK / "manifest.json"),
            ],
        ),
        ("leakage_audit", "leakage-audit", []),
        (
            "matched_surface_audit",
            "matched-surface-audit",
            ["--manifest", str(ITEMBANK / "manifest.json")],
        ),
    ],
)
def test_audit_clis_write_dated_jsonl_and_markdown(
    tmp_path, module_name, audit_slug, extra_args
):
    module = require_audit(module_name)
    output_dir = tmp_path / module_name
    argv = [
        "--bank", str(ITEMBANK / "bank" / "p1-private.jsonl"),
        "--output-dir", str(output_dir),
        "--report-date", "2026-07-09",
    ] + extra_args

    assert module.main(argv) == 0
    findings_path = output_dir / ("20260709-%s-findings.jsonl" % audit_slug)
    summary_path = output_dir / ("20260709-%s-summary.md" % audit_slug)
    assert findings_path.is_file()
    assert summary_path.is_file()
    summary = summary_path.read_text(encoding="utf-8")
    assert "Hard findings: 0" in summary
    assert "Soft findings: 0" in summary


def test_schema_cli_returns_nonzero_and_serializes_hard_findings(
    frozen_bundle, tmp_path
):
    schema = require_audit("schema_audit")
    bank, _, _ = deepcopy(frozen_bundle)
    bank[0]["expected_class"] = "welfare_optimal"
    bank_path = tmp_path / "corrupt-bank.jsonl"
    _write_jsonl(bank_path, bank)
    output_dir = tmp_path / "reports"

    result = schema.main([
        "--bank", str(bank_path),
        "--gold", str(ITEMBANK / "gold" / "p1-private.gold.jsonl"),
        "--manifest", str(ITEMBANK / "manifest.json"),
        "--output-dir", str(output_dir),
        "--report-date", "2026-07-09",
    ])

    assert result == 1
    findings = _load_jsonl(
        output_dir / "20260709-schema-audit-findings.jsonl"
    )
    assert "schema.public_forbidden_field" in _hard_codes(findings)


def test_soft_findings_are_counted_but_do_not_fail_exit_status(tmp_path):
    schema = require_audit("schema_audit")
    finding = schema.make_finding(
        audit="schema",
        code="schema.example_soft",
        severity="soft",
        message="example non-blocking observation",
    )

    paths = schema.write_reports(
        [finding],
        audit_slug="schema-audit",
        audit_title="Schema audit",
        checked_records=1,
        output_dir=tmp_path,
        report_date="2026-07-09",
    )

    assert schema.report_exit_code([finding]) == 0
    summary = paths["summary"].read_text(encoding="utf-8")
    assert "Hard findings: 0" in summary
    assert "Soft findings: 1" in summary
