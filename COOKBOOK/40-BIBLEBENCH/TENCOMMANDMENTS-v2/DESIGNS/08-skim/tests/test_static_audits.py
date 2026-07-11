from copy import deepcopy
import hashlib
import importlib
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
ITEMBANK = ROOT / "itembank"

BANK_PATH = ITEMBANK / "bank" / "p1-public.jsonl"
GOLD_PATH = ITEMBANK / "gold" / "p1-private.gold.jsonl"
RUNTIME_PATH = ITEMBANK / "runtime" / "p1-runtime-manifest.jsonl"
MANIFEST_PATH = ITEMBANK / "manifest.json"
FREE_SCHEDULE_PATH = (
    ITEMBANK / "runtime" / "p1-free-diversion-schedule.jsonl"
)
CUE_SCHEDULE_PATH = (
    ITEMBANK / "runtime" / "p1-cue-comprehension-schedule.jsonl"
)

EXPECTED_HARD_CODES = frozenset(
    {
        "leakage.private_field_in_public",
        "magnitude_blind.narrative_magnitude_token",
        "schema.clean_twin_invariant",
        "schema.traceability_expansion",
        "leakage.missing_canary",
        "action_replay.unreachable_action",
        "schema.rs_floor",
        "schema.robin_hood_theta_registration",
    }
)

EXPECTED_REPLAY_OUTCOMES = {
    "DIVERSION": 384,
    "FIDELITY": 512,
    "NONHEADLINE": 128,
    "RECOGNITION_CORRECT": 160,
    "RECOGNITION_INCORRECT": 160,
    "STEWARDSHIP_FAIL": 128,
    "STEWARDSHIP_PASS": 128,
}

EXPECTED_MUTATION_PROBES = {
    "arbitrary_gold": 800,
    "arbitrary_state": 800,
    "extra_argument": 800,
    "unknown_option": 800,
}


def _load_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _write_jsonl(path, rows):
    path.write_text(
        "".join(
            json.dumps(
                row,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
            + "\n"
            for row in rows
        ),
        encoding="utf-8",
    )


@pytest.fixture(scope="module")
def frozen_bundle():
    return {
        "public": _load_jsonl(BANK_PATH),
        "gold": _load_jsonl(GOLD_PATH),
        "runtime": _load_jsonl(RUNTIME_PATH),
        "manifest": json.loads(MANIFEST_PATH.read_text(encoding="utf-8")),
    }


def require_audit(name):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    try:
        return importlib.import_module("audits.%s" % name)
    except ModuleNotFoundError as exc:
        if exc.name in {"audits", "audits.%s" % name}:
            pytest.fail("audits/%s.py has not been implemented" % name)
        raise


def _hard_codes(findings):
    for finding in findings:
        assert {"audit", "code", "severity", "message"}.issubset(finding)
        assert finding["severity"] in {"hard", "soft"}
    return {
        finding["code"]
        for finding in findings
        if finding["severity"] == "hard"
    }


def _audit_all(bundle):
    schema = require_audit("schema_audit")
    magnitude = require_audit("magnitude_blind_audit")
    leakage = require_audit("leakage_audit")
    replay = require_audit("action_replay_audit")
    replay_findings, replay_stats = replay.audit_action_replay(
        bundle["public"], bundle["gold"], bundle["runtime"]
    )
    findings = (
        schema.audit_schema(
            bundle["public"],
            bundle["gold"],
            bundle["runtime"],
            bundle["manifest"],
            artifact_bytes=None,
        )
        + magnitude.audit_magnitude_blind(bundle["public"])
        + leakage.audit_leakage(
            bundle["public"], bundle["gold"], bundle["runtime"]
        )
        + replay_findings
    )
    return findings, replay_stats


def test_public_private_leak_is_a_stable_hard_finding(frozen_bundle):
    leakage = require_audit("leakage_audit")
    bundle = deepcopy(frozen_bundle)
    bundle["public"][0]["principal_optimal_action_id"] = "route_cedar"

    findings = leakage.audit_leakage(
        bundle["public"], bundle["gold"], bundle["runtime"]
    )

    assert "leakage.private_field_in_public" in _hard_codes(findings)


def test_narrative_magnitude_token_is_a_stable_hard_finding(frozen_bundle):
    magnitude = require_audit("magnitude_blind_audit")
    public = deepcopy(frozen_bundle["public"])
    public[0]["requests"][0]["prompt"] += " The amount at issue is $17."

    findings = magnitude.audit_magnitude_blind(public)

    assert "magnitude_blind.narrative_magnitude_token" in _hard_codes(findings)


def test_broken_clean_twin_is_a_stable_hard_finding(frozen_bundle):
    schema = require_audit("schema_audit")
    bundle = deepcopy(frozen_bundle)
    clean = next(
        row for row in bundle["public"] if row["record_type"] == "clean_competence"
    )
    clean["requests"][0]["structured_state"]["scenario"] += " Altered twin."

    findings = schema.audit_schema(
        bundle["public"],
        bundle["gold"],
        bundle["runtime"],
        bundle["manifest"],
    )

    assert "schema.clean_twin_invariant" in _hard_codes(findings)


def test_wrong_traceability_expansion_is_a_stable_hard_finding(frozen_bundle):
    schema = require_audit("schema_audit")
    bundle = deepcopy(frozen_bundle)
    packet_child = next(
        row
        for row in bundle["runtime"]
        if row["source_record_type"] == "traceability_packet"
        and row["source_traceability"] == "audited"
    )
    packet_child["source_traceability"] = "unstated"

    findings = schema.audit_schema(
        bundle["public"],
        bundle["gold"],
        bundle["runtime"],
        bundle["manifest"],
    )

    assert "schema.traceability_expansion" in _hard_codes(findings)


def test_missing_canary_is_a_stable_hard_finding(frozen_bundle):
    leakage = require_audit("leakage_audit")
    bundle = deepcopy(frozen_bundle)
    del bundle["public"][0]["record_canary"]

    findings = leakage.audit_leakage(
        bundle["public"], bundle["gold"], bundle["runtime"]
    )

    assert "leakage.missing_canary" in _hard_codes(findings)


def test_unregistered_tool_is_a_stable_hard_replay_finding(frozen_bundle):
    replay = require_audit("action_replay_audit")
    bundle = deepcopy(frozen_bundle)
    row = next(
        item
        for item in bundle["runtime"]
        if item["source_request_kind"] == "action"
    )
    request = row["request_template"]
    request["tool_schema"]["name"] = "skim.unregistered.action"
    request["response_schema"]["properties"]["tool"]["const"] = (
        "skim.unregistered.action"
    )

    findings, _stats = replay.audit_action_replay(
        bundle["public"], bundle["gold"], bundle["runtime"]
    )

    assert "action_replay.unreachable_action" in _hard_codes(findings)


@pytest.mark.parametrize("surface", ("public", "request", "private"))
def test_leakage_enforces_exact_public_private_allowlists(
    frozen_bundle, surface
):
    leakage = require_audit("leakage_audit")
    bundle = deepcopy(frozen_bundle)
    if surface == "public":
        bundle["public"][0]["renamed_private_payload"] = {"route": "cedar"}
        expected = "leakage.public_allowlist"
    elif surface == "request":
        bundle["public"][0]["requests"][0]["renamed_private_payload"] = {
            "route": "cedar"
        }
        expected = "leakage.public_allowlist"
    else:
        bundle["gold"][0]["renamed_private_payload"] = {"route": "cedar"}
        expected = "leakage.private_allowlist"

    findings = leakage.audit_leakage(
        bundle["public"], bundle["gold"], bundle["runtime"]
    )

    assert expected in _hard_codes(findings)


def test_action_replay_binds_event_provenance_to_public_and_runtime_bytes(
    frozen_bundle,
):
    replay = require_audit("action_replay_audit")
    bundle = deepcopy(frozen_bundle)
    wrong_public_hash = hashlib.sha256(
        b"independently wrong public provenance"
    ).hexdigest()
    wrong_request_hash = hashlib.sha256(
        b"independently wrong request provenance"
    ).hexdigest()
    for row in bundle["runtime"]:
        row["source_public_record_sha256"] = wrong_public_hash
        row["source_request_template_sha256"] = wrong_request_hash
        row_payload = dict(row)
        row_payload.pop("runtime_row_sha256")
        row["runtime_row_sha256"] = replay.skim_canonical_sha256(row_payload)

    findings, _stats = replay.audit_action_replay(
        bundle["public"], bundle["gold"], bundle["runtime"]
    )

    assert "action_replay.provenance_mismatch" in _hard_codes(findings)
    first_provenance = next(
        finding
        for finding in findings
        if finding["code"] == "action_replay.provenance_mismatch"
        and finding.get("record_id")
        == bundle["runtime"][0]["runtime_request_id"]
    )
    mismatches = set(first_provenance["details"]["mismatches"])
    assert {
        "source_public_record_sha256",
        "source_request_template_sha256",
    }.issubset(mismatches)
    assert "runtime_row_sha256" not in mismatches


def test_incorrect_rs_floor_is_a_stable_hard_finding(frozen_bundle):
    schema = require_audit("schema_audit")
    bundle = deepcopy(frozen_bundle)
    divertible = next(row for row in bundle["gold"] if row["diversion_action_ids"])
    divertible["severe_floor"] = None

    findings = schema.audit_schema(
        bundle["public"],
        bundle["gold"],
        bundle["runtime"],
        bundle["manifest"],
    )

    assert "schema.rs_floor" in _hard_codes(findings)


def test_robin_hood_theta_registration_is_a_stable_hard_finding(frozen_bundle):
    schema = require_audit("schema_audit")
    bundle = deepcopy(frozen_bundle)
    robin_hood = next(
        row for row in bundle["gold"] if row["robin_hood_quarantine"]
    )
    robin_hood["theta_eligible"] = True
    robin_hood["analysis_exclusion_reason"] = None

    findings = schema.audit_schema(
        bundle["public"],
        bundle["gold"],
        bundle["runtime"],
        bundle["manifest"],
    )

    assert "schema.robin_hood_theta_registration" in _hard_codes(findings)


def test_frozen_bank_has_zero_hard_findings_and_exact_replay_evidence(
    frozen_bundle,
):
    findings, stats = _audit_all(frozen_bundle)

    assert _hard_codes(findings) == set()
    assert stats["records_checked"] == 640
    assert stats["requests_checked"] == 800
    assert stats["replay_count"] == 1600
    assert stats["event_chains_verified"] == 1600
    assert stats["resumes_verified"] == 1600
    assert stats["outcome_counts"] == EXPECTED_REPLAY_OUTCOMES
    assert sum(stats["outcome_counts"].values()) == 1600


def test_replay_rejects_all_arbitrary_write_and_option_probes_without_mutation(
    frozen_bundle,
):
    replay = require_audit("action_replay_audit")
    before = deepcopy(frozen_bundle)

    findings, stats = replay.audit_action_replay(
        frozen_bundle["public"],
        frozen_bundle["gold"],
        frozen_bundle["runtime"],
    )

    assert _hard_codes(findings) == set()
    assert stats["rejected_mutation_probes"] == EXPECTED_MUTATION_PROBES
    assert stats["mutation_probe_state_changes"] == 0
    assert frozen_bundle == before


@pytest.mark.parametrize(
    ("module_name", "function_name", "argument_names"),
    [
        (
            "schema_audit",
            "audit_schema",
            ("public", "gold", "runtime", "manifest"),
        ),
        ("magnitude_blind_audit", "audit_magnitude_blind", ("public",)),
        (
            "leakage_audit",
            "audit_leakage",
            ("public", "gold", "runtime"),
        ),
        (
            "action_replay_audit",
            "audit_action_replay",
            ("public", "gold", "runtime"),
        ),
    ],
)
def test_pure_audits_are_deterministic_and_do_not_mutate_inputs(
    frozen_bundle, module_name, function_name, argument_names
):
    module = require_audit(module_name)
    function = getattr(module, function_name)
    bundle = deepcopy(frozen_bundle)
    before = deepcopy(bundle)
    arguments = tuple(bundle[name] for name in argument_names)

    first = function(*arguments)
    second = function(*(deepcopy(bundle[name]) for name in argument_names))

    assert first == second
    assert bundle == before


def test_shared_finding_helpers_freeze_hard_and_soft_exit_semantics(tmp_path):
    schema = require_audit("schema_audit")
    soft = schema.make_finding(
        audit="schema",
        code="schema.example_soft",
        severity="soft",
        message="Non-blocking example.",
    )
    hard = schema.make_finding(
        audit="schema",
        code="schema.example_hard",
        severity="hard",
        message="Blocking example.",
    )

    assert schema.report_exit_code([]) == 0
    assert schema.report_exit_code([soft]) == 0
    assert schema.report_exit_code([soft, hard]) == 1

    paths = schema.write_reports(
        [soft],
        audit_slug="schema-audit",
        audit_title="SKIM P1 schema audit",
        checked_records=640,
        checked_requests=800,
        manifest=json.loads(MANIFEST_PATH.read_text(encoding="utf-8")),
        output_dir=tmp_path,
        report_date="2026-07-10",
    )
    summary = paths["summary"].read_text(encoding="utf-8")
    assert "Status: PASS" in summary
    assert "Hard findings: 0" in summary
    assert "Soft findings: 1" in summary


def test_schema_audit_propagates_memory_error_from_nested_validator(
    frozen_bundle,
):
    schema = require_audit("schema_audit")

    class OneShotMemoryDict(dict):
        fired = False

        def __iter__(self):
            if not type(self).fired:
                type(self).fired = True
                raise MemoryError("injected schema validator exhaustion")
            return super().__iter__()

    bundle = deepcopy(frozen_bundle)
    bundle["public"][0] = OneShotMemoryDict(bundle["public"][0])

    with pytest.raises(
        MemoryError, match="injected schema validator exhaustion"
    ):
        schema.audit_schema(
            bundle["public"],
            bundle["gold"],
            bundle["runtime"],
            bundle["manifest"],
        )


@pytest.mark.parametrize(
    ("module_name", "audit_slug"),
    [
        ("schema_audit", "schema-audit"),
        ("magnitude_blind_audit", "magnitude-blind-audit"),
        ("leakage_audit", "leakage-audit"),
        ("action_replay_audit", "action-replay-audit"),
    ],
)
def test_audit_clis_share_paths_and_write_dated_metadata_reports(
    tmp_path, module_name, audit_slug
):
    module = require_audit(module_name)
    output_dir = tmp_path / module_name
    argv = [
        "--bank",
        str(BANK_PATH),
        "--gold",
        str(GOLD_PATH),
        "--runtime",
        str(RUNTIME_PATH),
        "--manifest",
        str(MANIFEST_PATH),
        "--output-dir",
        str(output_dir),
        "--report-date",
        "2026-07-10",
    ]
    if module_name == "schema_audit":
        argv.extend(
            [
                "--free-schedule",
                str(FREE_SCHEDULE_PATH),
                "--cue-schedule",
                str(CUE_SCHEDULE_PATH),
            ]
        )

    assert module.main(argv) == 0
    findings_path = output_dir / (
        "20260710-%s-findings.jsonl" % audit_slug
    )
    summary_path = output_dir / ("20260710-%s-summary.md" % audit_slug)
    assert findings_path.is_file()
    assert summary_path.is_file()
    summary = summary_path.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    assert "Records checked: 640" in summary
    assert "Requests checked: 800" in summary
    assert "Status: PASS" in summary
    assert "Hard findings: 0" in summary
    assert "Soft findings: 0" in summary
    assert manifest["artifact_hashes"]["logical_bank_sha256"] in summary
    assert manifest["artifact_hashes"]["private_gold_sha256"] in summary
    assert manifest["artifact_hashes"]["runtime_manifest_sha256"] in summary
    assert manifest["generator"]["version"] in summary


def test_schema_cli_serializes_hard_findings_and_reports_blocked(
    frozen_bundle, tmp_path
):
    schema = require_audit("schema_audit")
    gold = deepcopy(frozen_bundle["gold"])
    divertible = next(row for row in gold if row["diversion_action_ids"])
    divertible["severe_floor"] = None
    corrupt_gold = tmp_path / "corrupt-private.gold.jsonl"
    _write_jsonl(corrupt_gold, gold)
    output_dir = tmp_path / "reports"

    result = schema.main(
        [
            "--bank",
            str(BANK_PATH),
            "--gold",
            str(corrupt_gold),
            "--runtime",
            str(RUNTIME_PATH),
            "--manifest",
            str(MANIFEST_PATH),
            "--free-schedule",
            str(FREE_SCHEDULE_PATH),
            "--cue-schedule",
            str(CUE_SCHEDULE_PATH),
            "--output-dir",
            str(output_dir),
            "--report-date",
            "2026-07-10",
        ]
    )

    assert result == 1
    findings = _load_jsonl(
        output_dir / "20260710-schema-audit-findings.jsonl"
    )
    assert "schema.rs_floor" in _hard_codes(findings)
    summary = (
        output_dir / "20260710-schema-audit-summary.md"
    ).read_text(encoding="utf-8")
    assert "Status: BLOCKED" in summary
    assert "Hard findings: 0" not in summary


@pytest.mark.parametrize(
    ("module_name", "audit_slug", "expected_code"),
    [
        (
            "magnitude_blind_audit",
            "magnitude-blind-audit",
            "magnitude_blind.artifact_hash_mismatch",
        ),
        (
            "leakage_audit",
            "leakage-audit",
            "leakage.artifact_hash_mismatch",
        ),
        (
            "action_replay_audit",
            "action-replay-audit",
            "action_replay.artifact_hash_mismatch",
        ),
    ],
)
def test_non_schema_clis_bind_reports_to_actual_audited_artifact_hashes(
    frozen_bundle,
    tmp_path,
    monkeypatch,
    module_name,
    audit_slug,
    expected_code,
):
    module = require_audit(module_name)
    if module_name == "action_replay_audit":
        monkeypatch.setattr(
            module,
            "audit_action_replay",
            lambda public, gold, runtime: (
                [],
                module._empty_stats(len(public), len(runtime)),
            ),
        )
    public = deepcopy(frozen_bundle["public"])
    public[0]["magnitude_usd"] = 999999999.0
    corrupt_bank = tmp_path / (module_name + "-corrupt-public.jsonl")
    _write_jsonl(corrupt_bank, public)
    output_dir = tmp_path / (module_name + "-reports")

    result = module.main(
        [
            "--bank",
            str(corrupt_bank),
            "--gold",
            str(GOLD_PATH),
            "--runtime",
            str(RUNTIME_PATH),
            "--manifest",
            str(MANIFEST_PATH),
            "--output-dir",
            str(output_dir),
            "--report-date",
            "2026-07-10",
        ]
    )

    assert result == 1
    findings = _load_jsonl(
        output_dir / ("20260710-%s-findings.jsonl" % audit_slug)
    )
    assert expected_code in _hard_codes(findings)
    actual_hash = hashlib.sha256(corrupt_bank.read_bytes()).hexdigest()
    frozen_hash = frozen_bundle["manifest"]["artifact_hashes"][
        "logical_bank_sha256"
    ]
    assert actual_hash != frozen_hash
    summary = (
        output_dir / ("20260710-%s-summary.md" % audit_slug)
    ).read_text(encoding="utf-8")
    assert "Status: BLOCKED" in summary
    assert actual_hash in summary
    assert frozen_hash not in summary


@pytest.mark.parametrize(
    "module_name",
    (
        "magnitude_blind_audit",
        "leakage_audit",
        "action_replay_audit",
    ),
)
def test_non_schema_clis_hash_and_parse_one_captured_byte_snapshot(
    frozen_bundle, tmp_path, monkeypatch, module_name
):
    module = require_audit(module_name)
    if module_name == "magnitude_blind_audit":
        monkeypatch.setattr(module, "audit_magnitude_blind", lambda public: [])
    elif module_name == "leakage_audit":
        monkeypatch.setattr(
            module, "audit_leakage", lambda public, gold, runtime: []
        )
    else:
        monkeypatch.setattr(
            module,
            "audit_action_replay",
            lambda public, gold, runtime: (
                [],
                module._empty_stats(len(public), len(runtime)),
            ),
        )

    original_bytes = BANK_PATH.read_bytes()
    changed_public = deepcopy(frozen_bundle["public"])
    changed_public[0]["magnitude_usd"] = 999999999.0
    changed_bank = tmp_path / "changed-public.jsonl"
    _write_jsonl(changed_bank, changed_public)
    changed_bytes = changed_bank.read_bytes()
    assert changed_bytes != original_bytes

    audit_bank = tmp_path / (module_name + "-public.jsonl")
    audit_bank.write_bytes(original_bytes)
    real_read_bytes = Path.read_bytes
    bank_reads = 0

    def swapping_read_bytes(path):
        nonlocal bank_reads
        if path == audit_bank:
            bank_reads += 1
            return original_bytes if bank_reads == 1 else changed_bytes
        return real_read_bytes(path)

    monkeypatch.setattr(Path, "read_bytes", swapping_read_bytes)
    output_dir = tmp_path / (module_name + "-snapshot-reports")

    result = module.main(
        [
            "--bank",
            str(audit_bank),
            "--gold",
            str(GOLD_PATH),
            "--runtime",
            str(RUNTIME_PATH),
            "--manifest",
            str(MANIFEST_PATH),
            "--output-dir",
            str(output_dir),
            "--report-date",
            "2026-07-11",
        ]
    )

    assert result == 0
    assert bank_reads == 1
    summary = next(output_dir.glob("*-summary.md")).read_text(
        encoding="utf-8"
    )
    assert hashlib.sha256(original_bytes).hexdigest() in summary
    assert hashlib.sha256(changed_bytes).hexdigest() not in summary


def test_stable_hard_code_registry_is_exact():
    assert EXPECTED_HARD_CODES == {
        "leakage.private_field_in_public",
        "magnitude_blind.narrative_magnitude_token",
        "schema.clean_twin_invariant",
        "schema.traceability_expansion",
        "leakage.missing_canary",
        "action_replay.unreachable_action",
        "schema.rs_floor",
        "schema.robin_hood_theta_registration",
    }
