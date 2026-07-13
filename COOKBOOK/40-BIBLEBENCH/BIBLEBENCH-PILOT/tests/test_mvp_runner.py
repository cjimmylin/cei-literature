from __future__ import annotations

import ast
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import date
from decimal import Decimal
import hashlib
import json
import os
from pathlib import Path
import socket

from jsonschema import Draft202012Validator
import pytest

import biblebench_pilot.mvp_adapters as adapters
import biblebench_pilot.mvp_runner as runner
import biblebench_pilot.synthetic_provider as synthetic_provider
from biblebench_pilot.contracts import canonical_sha256


ROOT = Path(__file__).parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "mvp-manifest-synthetic.json"
PROPOSAL_FIXTURE = ROOT / "tests" / "fixtures" / "mvp-proposal-real-unauthorized.json"
AUTHORIZATION_FIXTURE = ROOT / "tests" / "fixtures" / "mvp-authorization-unauthorized.json"
OWNER_RECORD_SCHEMA = ROOT / "schemas" / "mvp-owner-record.schema.json"
BANK_ROOT = ROOT
SCHEMA_PATHS = (
    ROOT / "schemas" / "mvp-manifest.schema.json",
    ROOT / "schemas" / "mvp-artifact.schema.json",
)
ARTIFACT_NAMES = (
    "manifest.json",
    "calls.json",
    "requests.json",
    "responses.json",
    "usage.json",
    "receipts.json",
    "missingness.json",
    "summary.json",
)
PROVENANCE = "SYNTHETIC_VALIDATION_ONLY"


def test_pf002_runner_contract_surfaces_exist() -> None:
    expected = (
        ROOT / "schemas" / "mvp-manifest.schema.json",
        ROOT / "schemas" / "mvp-proposal.schema.json",
        ROOT / "schemas" / "mvp-authorization.schema.json",
        ROOT / "schemas" / "mvp-owner-record.schema.json",
        ROOT / "schemas" / "mvp-artifact.schema.json",
        ROOT / "tests" / "fixtures" / "mvp-manifest-synthetic.json",
        ROOT / "tests" / "fixtures" / "mvp-proposal-real-unauthorized.json",
        ROOT / "tests" / "fixtures" / "mvp-authorization-unauthorized.json",
        ROOT / "src" / "biblebench_pilot" / "mvp_runner.py",
        ROOT / "src" / "biblebench_pilot" / "mvp_adapters.py",
        ROOT / "src" / "biblebench_pilot" / "synthetic_provider.py",
        ROOT / "tools" / "run_synthetic_mvp.py",
    )

    assert all(path.is_file() for path in expected)


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _reseal(manifest: dict) -> dict:
    changed = deepcopy(manifest)
    changed.pop("manifest_sha256", None)
    changed["manifest_sha256"] = canonical_sha256(changed)
    return changed


def _reseal_authorization(authorization: dict) -> dict:
    changed = deepcopy(authorization)
    changed.pop("authorization_sha256", None)
    changed["authorization_sha256"] = canonical_sha256(changed)
    return changed


def _approved_authorization(proposal: dict) -> dict:
    authorization = _load_json(AUTHORIZATION_FIXTURE)
    authorization.update(
        {
            "status": "APPROVED",
            "owner": "Jimmy Lin",
            "approval_reference": "TEST-ONLY-EXPLICIT-OWNER-AUTHORIZATION",
            "approved_on": "2026-07-13",
            "proposal_manifest_sha256": proposal["manifest_sha256"],
            "authorization_schema_sha256": hashlib.sha256(
                (ROOT / "schemas" / "mvp-authorization.schema.json").read_bytes()
            ).hexdigest(),
            "run_id": "pf002-test-run-20260713",
            "authorization_nonce": "a" * 64,
            "owner_record_id": "pf002-test-owner-record-20260713",
        }
    )
    return _reseal_authorization(authorization)


def _current_proposal() -> dict:
    proposal = _load_json(PROPOSAL_FIXTURE)
    proposal["snapshot_hashes"] = runner._expected_snapshot_hashes(proposal)
    return _reseal(proposal)


def _owner_record(authorization: dict) -> dict:
    return {
        "owner_record_version": "pf002-owner-record-v1",
        "owner_record_id": authorization["owner_record_id"],
        "status": "APPROVED",
        "owner": authorization["owner"],
        "approval_reference": authorization["approval_reference"],
        "approved_on": authorization["approved_on"],
        "expires_on": authorization["expires_on"],
        "proposal_manifest_sha256": authorization["proposal_manifest_sha256"],
        "authorization_sha256": authorization["authorization_sha256"],
        "run_id": authorization["run_id"],
        "authorization_nonce": authorization["authorization_nonce"],
        "not_to_exceed_usd": authorization["not_to_exceed_usd"],
        "owner_record_schema_sha256": hashlib.sha256(
            OWNER_RECORD_SCHEMA.read_bytes()
        ).hexdigest(),
    }


def _trusted_gate_kwargs(tmp_path: Path, authorization: dict) -> dict:
    owner_record_path = tmp_path / "owner-record.json"
    owner_record_path.write_text(
        json.dumps(_owner_record(authorization), sort_keys=True), encoding="utf-8"
    )
    consumption_dir = tmp_path / "consumed"
    consumption_dir.mkdir()
    return {
        "owner_record_path": owner_record_path,
        "expected_owner_record_sha256": hashlib.sha256(
            owner_record_path.read_bytes()
        ).hexdigest(),
        "consumption_dir": consumption_dir,
    }


def _reseal_run_tree_manifest(root: Path, mutation) -> None:
    manifest = _load_json(root / "manifest.json")
    mutation(manifest)
    manifest = _reseal(manifest)
    (root / "manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    previous = manifest["manifest_sha256"]
    for name in ARTIFACT_NAMES[1:]:
        artifact = _load_json(root / name)
        artifact["previous_artifact_sha256"] = previous
        artifact.pop("artifact_sha256")
        artifact["artifact_sha256"] = canonical_sha256(artifact)
        (root / name).write_text(
            json.dumps(artifact, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
        previous = artifact["artifact_sha256"]


def _record_recomputed_cost(proposal: dict) -> dict:
    changed = deepcopy(proposal)
    calls_per_actor = (
        changed["geometry"]["logical_call_count"]
        // changed["geometry"]["actor_count"]
    )
    attempts = changed["retry_rule"]["maximum_attempts_per_logical_call"]
    total = Decimal("0")
    for actor in changed["actors"]:
        caps = actor["token_caps"]
        price = actor["price"]
        cost = Decimal(calls_per_actor * attempts) * (
            Decimal(caps["max_input_tokens"])
            * Decimal(str(price["input_usd"]))
            + Decimal(caps["max_output_tokens"])
            * Decimal(str(price["output_usd"]))
        ) / Decimal("1000000")
        actor["route_worst_case_usd"] = float(cost)
        total += cost
    changed["budget"]["calculated_worst_case_usd"] = float(total)
    changed["budget"]["forecast_usd"] = float(total)
    return _reseal(changed)


def _run(output: Path) -> dict[str, dict]:
    runner.run_synthetic_mvp(
        manifest_path=FIXTURE,
        bank_root=BANK_ROOT,
        output_dir=output,
    )
    return {name: _load_json(output / name) for name in ARTIFACT_NAMES}


def test_schemas_are_closed_and_fixture_is_strictly_synthetic() -> None:
    manifest_schema, artifact_schema = map(_load_json, SCHEMA_PATHS)
    for schema in (manifest_schema, artifact_schema):
        Draft202012Validator.check_schema(schema)
        assert schema["additionalProperties"] is False
    manifest = _load_json(FIXTURE)
    errors = sorted(
        Draft202012Validator(manifest_schema).iter_errors(manifest),
        key=lambda error: list(error.path),
    )

    assert not errors
    assert manifest["provenance"] == PROVENANCE
    assert manifest["authorized"] is False
    assert manifest["fallback_enabled"] is False
    assert manifest["cue"] == "C1"
    assert len(manifest["actors"]) == 3
    assert all(actor["provenance"] == PROVENANCE for actor in manifest["actors"])
    assert all(actor["model_id"].startswith("synthetic-model-") for actor in manifest["actors"])
    assert all(
        actor["input_price_per_million_usd"] == 0
        and actor["output_price_per_million_usd"] == 0
        for actor in manifest["actors"]
    )
    assert manifest["retry_rule"]["max_retries"] == 1
    assert manifest["budget"]["forecast_usd"] <= 3
    assert manifest["budget"]["hard_cap_usd"] == 5
    encoded = json.dumps(manifest, sort_keys=True).lower()
    for forbidden in ("endpoint", "api_key", "credential", "transport"):
        assert forbidden not in encoded


def test_real_proposal_contract_is_closed_valid_and_unauthorized_for_transport() -> None:
    proposal_schema = _load_json(ROOT / "schemas" / "mvp-proposal.schema.json")
    authorization_schema = _load_json(
        ROOT / "schemas" / "mvp-authorization.schema.json"
    )
    owner_record_schema = _load_json(OWNER_RECORD_SCHEMA)
    for schema in (proposal_schema, authorization_schema, owner_record_schema):
        Draft202012Validator.check_schema(schema)
        assert schema["additionalProperties"] is False

    proposal = _load_json(PROPOSAL_FIXTURE)
    authorization = _load_json(AUTHORIZATION_FIXTURE)
    assert not list(Draft202012Validator(proposal_schema).iter_errors(proposal))
    assert not list(
        Draft202012Validator(authorization_schema).iter_errors(authorization)
    )
    assert proposal["status"] == "PROPOSAL_ONLY"
    assert proposal["authorized"] is False
    assert authorization["status"] == "NOT_AUTHORIZED"
    encoded_contract = json.dumps(
        {"proposal": proposal, "authorization": authorization}, sort_keys=True
    ).lower()
    for forbidden in ("api_key", "credential", "secret", "base_url", "endpoint"):
        assert forbidden not in encoded_contract
    assert all(
        set(actor["decoding"])
        == {
            "temperature",
            "top_p",
            "seed",
            "frequency_penalty",
            "presence_penalty",
            "stop_sequences",
        }
        and set(actor["token_caps"]) == {"max_input_tokens", "max_output_tokens"}
        for actor in proposal["actors"]
    )

    cost = runner.validate_proposal_contract(
        proposal,
        bank_root=BANK_ROOT,
        today=date(2026, 7, 13),
    )
    assert cost == Decimal("1.6839168")
    with pytest.raises(ValueError, match="owner authorization required"):
        runner.validate_pretransport_authorization(
            proposal,
            authorization,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
        )


def test_explicit_owner_authorization_accepts_exact_proposal_without_transport(
    tmp_path: Path,
) -> None:
    proposal = _current_proposal()
    authorization = _approved_authorization(proposal)
    gate_kwargs = _trusted_gate_kwargs(tmp_path, authorization)

    result = runner.validate_pretransport_authorization(
        proposal,
        authorization,
        bank_root=BANK_ROOT,
        today=date(2026, 7, 13),
        **gate_kwargs,
    )

    assert result == {
        "proposal_manifest_sha256": proposal["manifest_sha256"],
        "authorization_sha256": authorization["authorization_sha256"],
        "owner_record_sha256": gate_kwargs["expected_owner_record_sha256"],
        "run_id": authorization["run_id"],
        "authorization_nonce": authorization["authorization_nonce"],
        "worst_case_cost_usd": "1.6839168",
        "not_to_exceed_usd": "5",
    }


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda row: row.__setitem__("manifest_sha256", "0" * 64), "proposal manifest hash"),
        (lambda row: row.__setitem__("fallback_enabled", True), "fallback"),
        (lambda row: row.__setitem__("expires_on", "2000-01-01"), "proposal expired"),
        (
            lambda row: row["actors"][1].__setitem__(
                "model_id", row["actors"][0]["model_id"]
            ),
            "provider/model/adapter route mismatch",
        ),
        (
            lambda row: row["actors"][1].__setitem__(
                "actor_alias", row["actors"][0]["actor_alias"]
            ),
            "provider/model/adapter route mismatch",
        ),
        (
            lambda row: row["actors"][0]["decoding"].pop("seed"),
            "invalid proposal schema",
        ),
        (
            lambda row: row["actors"][0]["route"].__setitem__(
                "provider_family", "unsupported_transport_family"
            ),
            "invalid proposal schema",
        ),
        (
            lambda row: row["actors"][0]["price"].__setitem__(
                "evidence_date", "not-a-date"
            ),
            "invalid price evidence date",
        ),
        (
            lambda row: row["snapshot_hashes"].__setitem__(
                "compiler_sha256", "0" * 64
            ),
            "snapshot hash mismatch",
        ),
        (
            lambda row: row["budget"].__setitem__(
                "forecast_usd", row["budget"]["forecast_usd"] + 0.01
            ),
            "cost forecast mismatch",
        ),
        (
            lambda row: row["budget"].__setitem__("hard_cap_usd", 4.99),
            "hard cap must equal five dollars",
        ),
    ],
)
def test_real_proposal_fail_closed_classes(mutation, message) -> None:
    proposal = _load_json(PROPOSAL_FIXTURE)
    mutation(proposal)
    if proposal["manifest_sha256"] != "0" * 64:
        proposal = _reseal(proposal)

    with pytest.raises(ValueError, match=message):
        runner.validate_proposal_contract(
            proposal,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
        )


def test_recomputed_worst_case_above_three_dollars_is_rejected() -> None:
    proposal = _load_json(PROPOSAL_FIXTURE)
    proposal["actors"][0]["price"]["input_usd"] = 20
    proposal = _record_recomputed_cost(proposal)

    with pytest.raises(ValueError, match="forecast exceeds three dollars"):
        runner.validate_proposal_contract(
            proposal,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda row: row.__setitem__("authorization_sha256", "0" * 64), "authorization hash"),
        (
            lambda row: row.__setitem__("proposal_manifest_sha256", "0" * 64),
            "authorization proposal hash",
        ),
        (lambda row: row.__setitem__("expires_on", "2000-01-01"), "authorization expired"),
        (
            lambda row: row.__setitem__("approved_on", "2026-07-14"),
            "authorization approval date",
        ),
        (lambda row: row.__setitem__("not_to_exceed_usd", 4.99), "authorization NTE"),
    ],
)
def test_pretransport_authorization_fail_closed_classes(
    mutation, message, tmp_path: Path
) -> None:
    proposal = _current_proposal()
    authorization = _approved_authorization(proposal)
    mutation(authorization)
    if authorization["authorization_sha256"] != "0" * 64:
        authorization = _reseal_authorization(authorization)

    with pytest.raises(ValueError, match=message):
        runner.validate_pretransport_authorization(
            proposal,
            authorization,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
            **_trusted_gate_kwargs(tmp_path, authorization),
        )


@pytest.mark.parametrize(
    ("loader_name", "payload"),
    [
        ("load_manifest", '{"authorized":false,"authorized":true}'),
        (
            "load_proposal",
            '{"route":{"provider_family":"generic_responses",'
            '"provider_family":"generic_messages"}}',
        ),
        ("load_authorization", '{"status":"NOT_AUTHORIZED","status":"APPROVED"}'),
        ("load_owner_record", '{"owner":"Jimmy Lin","owner":"Mallory"}'),
    ],
)
def test_duplicate_json_members_are_rejected_by_every_contract_loader(
    tmp_path: Path, loader_name: str, payload: str
) -> None:
    path = tmp_path / f"{loader_name}.json"
    path.write_text(payload, encoding="utf-8")

    with pytest.raises(ValueError, match="duplicate JSON member"):
        getattr(runner, loader_name)(path)


@pytest.mark.parametrize(
    "mutation",
    [
        lambda row: row["actors"][0].__setitem__("provider", "Google"),
        lambda row: row["actors"][0].__setitem__(
            "model_id", "gemini-2.5-flash-lite"
        ),
        lambda row: row["actors"][0].__setitem__(
            "route", deepcopy(row["actors"][1]["route"])
        ),
    ],
)
def test_exact_provider_model_adapter_route_coherence_is_closed(mutation) -> None:
    proposal = _current_proposal()
    mutation(proposal)
    proposal = _reseal(proposal)

    with pytest.raises(ValueError, match="provider/model/adapter route mismatch"):
        runner.validate_proposal_contract(
            proposal, bank_root=BANK_ROOT, today=date(2026, 7, 13)
        )


def test_authorization_requires_external_trust_and_durable_consumption_state(
    tmp_path: Path,
) -> None:
    proposal = _current_proposal()
    authorization = _approved_authorization(proposal)

    with pytest.raises(ValueError, match="trusted owner record required"):
        runner.validate_pretransport_authorization(
            proposal,
            authorization,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
        )

    kwargs = _trusted_gate_kwargs(tmp_path, authorization)
    kwargs["consumption_dir"] = tmp_path / "absent-consumption-state"
    with pytest.raises(ValueError, match="consumption state unavailable"):
        runner.validate_pretransport_authorization(
            proposal,
            authorization,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
            **kwargs,
        )


def test_owner_record_digest_and_execution_binding_fail_closed(tmp_path: Path) -> None:
    proposal = _current_proposal()
    authorization = _approved_authorization(proposal)
    kwargs = _trusted_gate_kwargs(tmp_path, authorization)

    with pytest.raises(ValueError, match="owner record trust-anchor hash mismatch"):
        runner.validate_pretransport_authorization(
            proposal,
            authorization,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
            **{**kwargs, "expected_owner_record_sha256": "0" * 64},
        )

    owner_record = _load_json(kwargs["owner_record_path"])
    owner_record["authorization_nonce"] = "b" * 64
    kwargs["owner_record_path"].write_text(
        json.dumps(owner_record, sort_keys=True), encoding="utf-8"
    )
    kwargs["expected_owner_record_sha256"] = hashlib.sha256(
        kwargs["owner_record_path"].read_bytes()
    ).hexdigest()
    with pytest.raises(ValueError, match="owner record authorization binding mismatch"):
        runner.validate_pretransport_authorization(
            proposal,
            authorization,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
            **kwargs,
        )


def test_consumed_run_identity_rejects_replay(tmp_path: Path) -> None:
    proposal = _current_proposal()
    authorization = _approved_authorization(proposal)
    kwargs = _trusted_gate_kwargs(tmp_path, authorization)

    runner.validate_pretransport_authorization(
        proposal,
        authorization,
        bank_root=BANK_ROOT,
        today=date(2026, 7, 13),
        **kwargs,
    )
    receipts = tuple(kwargs["consumption_dir"].iterdir())
    assert len(receipts) == 1
    assert receipts[0].stat().st_mode & 0o777 == 0o600

    with pytest.raises(ValueError, match="authorization already consumed"):
        runner.validate_pretransport_authorization(
            proposal,
            authorization,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
            **kwargs,
        )


def test_manifest_validates_exact_banks_and_compiles_pf002_geometry() -> None:
    manifest = runner.load_manifest(FIXTURE)
    runner.validate_manifest(manifest, bank_root=BANK_ROOT, today=date(2026, 7, 13))

    calls = runner.compile_mvp_calls(manifest, bank_root=BANK_ROOT)

    assert len(calls) == 288
    assert Counter(call["phase"] for call in calls) == Counter(primary=144, probe=144)
    assert Counter(call["actor_alias"] for call in calls) == {
        actor["actor_alias"]: 96 for actor in manifest["actors"]
    }
    assert {call["cue"] for call in calls} == {"C1"}
    assert not any("twin" in json.dumps(call).lower() for call in calls)
    assert len({call["logical_call_id"] for call in calls}) == 288
    assert all(len(call["logical_call_id"]) == 16 for call in calls)
    assert all(call["request_sha256"] == canonical_sha256(call["request"]) for call in calls)
    assert all(len(call["binding_sha256"]) == 64 for call in calls)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for call in calls:
        grouped[call["pair_id"]].append(call)
    assert len(grouped) == 144
    assert all(
        {row["phase"] for row in rows} == {"primary", "probe"}
        and len(rows) == 2
        and next(row for row in rows if row["phase"] == "probe")[
            "primary_logical_call_id"
        ]
        == next(row for row in rows if row["phase"] == "primary")[
            "logical_call_id"
        ]
        for rows in grouped.values()
    )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda row: row.__setitem__("manifest_sha256", "0" * 64), "manifest hash"),
        (lambda row: row.__setitem__("fallback_enabled", True), "fallback"),
        (lambda row: row["budget"].__setitem__("forecast_usd", 3.01), "forecast"),
        (lambda row: row["budget"].__setitem__("hard_cap_usd", 4.99), "hard cap"),
        (lambda row: row.__setitem__("expires_on", "2000-01-01"), "expired"),
        (lambda row: row.__setitem__("authorized", True), "authorized"),
        (lambda row: row["banks"][0].__setitem__("sha256", "0" * 64), "bank hash"),
        (
            lambda row: row["banks"][0].__setitem__(
                "primary_request_registry_sha256", "0" * 64
            ),
            "request registry hash",
        ),
        (lambda row: row["retry_rule"].__setitem__("max_retries", 2), "retry rule"),
        (lambda row: row["actors"][0].__setitem__("model_id", "real-model"), "synthetic"),
        (lambda row: row["actors"][0].__setitem__("input_price_per_million_usd", 1), "zero price"),
    ],
)
def test_manifest_fail_closed_gates(mutation, message) -> None:
    manifest = _load_json(FIXTURE)
    mutation(manifest)
    if manifest["manifest_sha256"] != "0" * 64:
        manifest = _reseal(manifest)

    with pytest.raises(ValueError, match=message):
        runner.validate_manifest(
            manifest,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
        )


def test_synthetic_manifest_resealed_sub_three_dollar_forecast_fails_closed() -> None:
    manifest = _load_json(FIXTURE)
    manifest["budget"]["forecast_usd"] = 0.01
    manifest = _reseal(manifest)
    schema = _load_json(ROOT / "schemas" / "mvp-manifest.schema.json")

    assert list(Draft202012Validator(schema).iter_errors(manifest))
    with pytest.raises(ValueError, match="synthetic forecast must be zero"):
        runner.validate_manifest(
            manifest,
            bank_root=BANK_ROOT,
            today=date(2026, 7, 13),
        )


def test_offline_adapters_are_pure_closed_and_reject_unsupported_parameters() -> None:
    neutral = {
        "provenance": PROVENANCE,
        "prompt": "Synthetic prompt only.",
        "response_schema": {"type": "object", "additionalProperties": False},
        "tools": {"actions": ["submit_synthetic"]},
        "temperature": 0,
        "max_output_tokens": 64,
    }
    before = deepcopy(neutral)

    shaped = {
        family: adapters.adapt_request(family, neutral)
        for family in (
            "generic_messages",
            "generic_responses",
            "generic_content",
        )
    }

    assert neutral == before
    assert set(shaped["generic_messages"]) == {
        "messages", "max_tokens", "temperature", "tools", "response_schema"
    }
    assert set(shaped["generic_responses"]) == {
        "input", "max_output_tokens", "temperature", "tools", "response_format"
    }
    assert set(shaped["generic_content"]) == {
        "contents", "generation_config", "tools", "response_schema"
    }
    with pytest.raises(ValueError, match="unsupported provider family"):
        adapters.adapt_request("unknown", neutral)
    with pytest.raises(ValueError, match="unsupported neutral request parameter"):
        adapters.adapt_request("generic_messages", {**neutral, "seed": 1})

    forbidden_imports = {"socket", "http", "urllib", "requests", "openai", "anthropic", "google"}
    for relative in (
        "src/biblebench_pilot/mvp_adapters.py",
        "src/biblebench_pilot/synthetic_provider.py",
        "src/biblebench_pilot/mvp_runner.py",
    ):
        tree = ast.parse((ROOT / relative).read_text(encoding="utf-8"))
        imports = {
            alias.name.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in node.names
        }
        assert not (imports & forbidden_imports)


def test_synthetic_provider_covers_registered_terminal_and_retry_states() -> None:
    provider = synthetic_provider.SyntheticProvider()
    request = {
        "provenance": PROVENANCE,
        "logical_call_id": "1" * 16,
        "request_sha256": "2" * 64,
    }
    expected = {
        "success": "success",
        "refusal": "refusal",
        "malformed": "malformed",
        "truncated": "truncated",
        "rate_limit_once": "rate_limit",
        "unknown_delivery": "unknown_delivery",
        "retry_exhausted": "rate_limit",
    }

    for scenario, status in expected.items():
        assert provider.attempt(request, scenario=scenario, attempt=1)["status"] == status
    assert provider.attempt(request, scenario="rate_limit_once", attempt=2)["status"] == "success"
    assert provider.attempt(request, scenario="retry_exhausted", attempt=2)["status"] == "rate_limit"
    assert provider.attempt(request, scenario="unknown_delivery", attempt=1)["terminal"] is True
    with pytest.raises(ValueError, match="unknown synthetic scenario"):
        provider.attempt(request, scenario="other", attempt=1)


def test_full_synthetic_run_never_opens_socket_and_preserves_terminal_rules(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    for name in tuple(os.environ):
        if name.endswith("_API_KEY") or "PROXY" in name.upper():
            monkeypatch.delenv(name, raising=False)

    def denied_socket(*args, **kwargs):
        raise AssertionError("network socket attempted")

    monkeypatch.setattr(socket, "socket", denied_socket)
    docs = _run(tmp_path / "run")

    runner.verify_run_tree(tmp_path / "run")
    calls = {record["payload"]["logical_call_id"]: record["payload"] for record in docs["calls.json"]["records"]}
    receipts = [record["payload"] for record in docs["receipts.json"]["records"]]
    summary = docs["summary.json"]["records"][0]["payload"]
    assert summary["logical_call_count"] == 288
    assert summary["primary_count"] == 144
    assert summary["probe_count"] == 144
    assert summary["retry_attempt_count"] > 0
    assert all(count > 0 for count in summary["terminal_status_counts"].values())
    assert all(receipt["fallback_used"] is False for receipt in receipts)
    assert all(receipt["actor_alias"] == calls[receipt["logical_call_id"]]["actor_alias"] for receipt in receipts)
    assert all(receipt["attempt_count"] == 1 for receipt in receipts if receipt["terminal_status"] == "unknown_delivery")
    assert all(receipt["attempt_count"] == 2 for receipt in receipts if receipt["scenario"] in {"rate_limit_once", "retry_exhausted"})
    assert all(receipt["attempt_count"] <= 2 for receipt in receipts)
    for name, document in docs.items():
        assert document["provenance"] == PROVENANCE, name
        if name != "manifest.json":
            assert all(record["provenance"] == PROVENANCE for record in document["records"])
            assert all(record["payload"]["provenance"] == PROVENANCE for record in document["records"])


def test_run_trees_are_byte_reproducible_and_schema_valid(tmp_path: Path) -> None:
    first = tmp_path / "first"
    second = tmp_path / "second"
    first_docs = _run(first)
    second_docs = _run(second)
    artifact_schema = _load_json(ROOT / "schemas" / "mvp-artifact.schema.json")
    validator = Draft202012Validator(artifact_schema)

    assert [path.name for path in sorted(first.iterdir())] == sorted(ARTIFACT_NAMES)
    assert {
        path.name: path.read_bytes() for path in sorted(first.iterdir())
    } == {
        path.name: path.read_bytes() for path in sorted(second.iterdir())
    }
    for name in ARTIFACT_NAMES[1:]:
        assert not list(validator.iter_errors(first_docs[name]))
        assert first_docs[name] == second_docs[name]


def test_runner_repair_preserves_committed_synthetic_fixture_bytes(tmp_path: Path) -> None:
    generated = tmp_path / "generated"
    _run(generated)

    committed = ROOT / "synthetic-mvp"
    assert {
        name: (generated / name).read_bytes() for name in ARTIFACT_NAMES
    } == {
        name: (committed / name).read_bytes() for name in ARTIFACT_NAMES
    }


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda row: row.__setitem__("authorized", True), "authorized"),
        (
            lambda row: row.__setitem__("unexpected_manifest_member", True),
            "invalid MVP manifest schema",
        ),
        (
            lambda row: row["actors"][0].__setitem__(
                "input_price_per_million_usd", 0.01
            ),
            "zero price",
        ),
    ],
)
def test_verify_run_tree_rejects_semantic_tamper_after_complete_rehash(
    tmp_path: Path, mutation, message: str
) -> None:
    root = tmp_path / "semantic-tamper"
    _run(root)
    _reseal_run_tree_manifest(root, mutation)

    with pytest.raises(ValueError, match=message):
        runner.verify_run_tree(root)


def test_cli_accepts_only_bundled_fixture_and_empty_output_directory(tmp_path: Path) -> None:
    output = tmp_path / "accepted"
    assert runner.main(["--manifest", str(FIXTURE), "--output", str(output)]) == 0
    runner.verify_run_tree(output)

    copied = tmp_path / "copied.json"
    copied.write_bytes(FIXTURE.read_bytes())
    with pytest.raises(ValueError, match="bundled synthetic fixture"):
        runner.main(["--manifest", str(copied), "--output", str(tmp_path / "rejected")])

    mixed = tmp_path / "mixed"
    mixed.mkdir()
    (mixed / "other.txt").write_text("other\n", encoding="utf-8")
    with pytest.raises(ValueError, match="empty output directory"):
        runner.main(["--manifest", str(FIXTURE), "--output", str(mixed)])
