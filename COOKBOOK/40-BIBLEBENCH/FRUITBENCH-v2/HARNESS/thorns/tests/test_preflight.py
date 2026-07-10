from __future__ import annotations

import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest


THORNS = Path(__file__).resolve().parents[1]
HARNESS = THORNS.parent
for path in (THORNS, HARNESS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from shared.counterbalance import CounterbalanceError  # noqa: E402
from shared.live_spine import validate_role_separation  # noqa: E402
from preflight import (  # noqa: E402
    REQUIRED_GATE_NAMES,
    PreflightError,
    build_preflight_receipt,
    build_subject_requests,
    compile_phase_schedule,
    execute_authorized_phase,
    fetch_online_catalog_bundle,
    load_catalog_bundle,
    load_item_generation_provenance,
    load_model_lineage,
    load_openrouter_config,
    load_registered_cue_surfaces,
    run_smoke,
    validate_catalog_bundle,
    validate_development_subset,
    validate_preflight_receipt,
    write_immutable_json,
)
import run_pilot  # noqa: E402


CONFIG = THORNS / "pilot_config.openrouter.json"
CATALOG = THORNS / "tests" / "fixtures" / "openrouter-models.json"

EVALUATION_MODELS = [
    "openai/gpt-5.5",
    "openai/gpt-5.4",
    "openai/gpt-5.4-mini",
]
CALIBRATION_MODELS = [
    "deepseek/deepseek-v4-flash",
    "qwen/qwen3.7-plus",
    "meta-llama/llama-4-maverick",
    "mistralai/mistral-large-2512",
]
HELD_OUT_MODELS = ["x-ai/grok-4.5", "moonshotai/kimi-k2.5"]
JUDGE_MODELS = ["cohere/command-a", "google/gemini-3.5-flash"]


def _all_pass() -> dict[str, dict[str, str]]:
    return {
        name: {"status": "pass", "detail": f"fixture {name} passed"}
        for name in REQUIRED_GATE_NAMES
    }


def test_config_freezes_exact_roster_attacker_and_balanced_rollout_contract() -> None:
    cfg = load_openrouter_config(CONFIG)

    assert [row["model_id"] for row in cfg["roles"]["evaluation"]] == EVALUATION_MODELS
    assert [row["actor_id"] for row in cfg["roles"]["evaluation"]] == ["A01", "A02", "A03"]
    assert [row["model_id"] for row in cfg["roles"]["calibration"]] == CALIBRATION_MODELS
    assert [row["model_id"] for row in cfg["roles"]["held_out_frontier"]] == HELD_OUT_MODELS
    assert [row["model_id"] for row in cfg["judges"]] == JUDGE_MODELS
    assert [row["judge_id"] for row in cfg["judges"]] == ["J01", "J02"]

    attackers = [row for row in cfg["roles"]["calibration"] if row.get("attacker")]
    assert len(attackers) == 1
    persona = Path(attackers[0]["persona_path"])
    assert persona.is_file()
    assert hashlib.sha256(persona.read_bytes()).hexdigest() == attackers[0]["params"]["persona_sha256"]
    assert cfg["rollouts"]["calibration"] >= 24

    # Design correction: five blocks cannot balance three cue arms/branches.
    assert cfg["rollouts"]["evaluation"] == 6
    assert cfg["trajectory"] == {"branch_strategy": "counterbalanced", "branch_count": 3}
    assert all(value % 3 == 0 for value in cfg["rollouts"].values())


def test_three_subject_requests_are_byte_equivalent_except_model() -> None:
    cfg = load_openrouter_config(CONFIG)
    messages = [{"role": "user", "content": "Frozen fixture prompt."}]

    payloads = build_subject_requests(cfg, messages)

    assert list(payloads) == ["A01", "A02", "A03"]
    assert [payload["model"] for payload in payloads.values()] == EVALUATION_MODELS
    normalized = [{**payload, "model": "opaque"} for payload in payloads.values()]
    assert normalized[1:] == normalized[:1] * 2
    for payload in payloads.values():
        assert payload["reasoning"] == {"effort": "medium"}
        assert payload["provider"] == {
            "order": ["openai"],
            "allow_fallbacks": False,
            "require_parameters": True,
        }
        assert payload["store"] is False
        assert payload["stream"] is False


def test_development_subset_is_exactly_two_hard_single_shots_per_fruit() -> None:
    cfg = load_openrouter_config(CONFIG)
    summary = validate_development_subset(cfg)
    assert summary == {f"F{index}": 2 for index in range(1, 10)}

    drifted = deepcopy(cfg)
    drifted["development_item_ids"][-1] = "thorns-astroturf-002"
    with pytest.raises(PreflightError, match="two.*fruit|per fruit"):
        validate_development_subset(drifted)


def test_catalog_fixture_binds_canonical_slugs_endpoints_and_role_firewalls() -> None:
    cfg = load_openrouter_config(CONFIG)
    bundle = load_catalog_bundle(CATALOG)

    validated = validate_catalog_bundle(cfg, bundle)

    assert set(validated.canonical_slugs) == set(
        EVALUATION_MODELS + CALIBRATION_MODELS + HELD_OUT_MODELS + JUDGE_MODELS
    )
    assert validated.canonical_slugs["openai/gpt-5.5"] == "openai/gpt-5.5-20260423"
    assert validated.provider_endpoints["deepseek/deepseek-v4-flash"] == "deepseek"
    assert validated.provider_endpoints["google/gemini-3.5-flash"] == "google-ai-studio"
    validate_role_separation(validated.principals)


@pytest.mark.parametrize("capability", ["response_format", "structured_outputs"])
def test_catalog_validation_requires_structured_output_capabilities_for_judges(
    capability: str,
) -> None:
    cfg = load_openrouter_config(CONFIG)
    bundle = deepcopy(load_catalog_bundle(CATALOG))
    model_id = "google/gemini-3.5-flash"
    catalog_row = next(
        row for row in bundle["catalog"]["data"] if row["id"] == model_id
    )
    endpoint = bundle["endpoints"][model_id]["data"]["endpoints"][0]
    catalog_row["supported_parameters"].remove(capability)
    endpoint["supported_parameters"].remove(capability)

    with pytest.raises(PreflightError, match=capability):
        validate_catalog_bundle(cfg, bundle)


def test_frozen_lineage_and_item_generator_provenance_disqualify_overlapping_judges(
    tmp_path: Path,
) -> None:
    cfg = load_openrouter_config(CONFIG)
    lineage = load_model_lineage(cfg)
    assert lineage["cohere/command-a"]["family"] == "command-a"
    generators = load_item_generation_provenance(cfg)
    assert {row["vendor"] for row in generators} == {"anthropic", "openai"}

    drifted = deepcopy(cfg)
    drifted["judges"][0]["family"] = "invented-family"
    with pytest.raises(PreflightError, match="lineage|family"):
        validate_catalog_bundle(drifted, load_catalog_bundle(CATALOG))

    provenance = json.loads(Path(cfg["paths"]["item_generation_provenance"]).read_text())
    overlapping_generator = deepcopy(provenance["generators"][0])
    overlapping_generator["generator_id"] = "G03"
    overlapping_generator["vendor"] = "cohere"
    overlapping_generator["family"] = "command-a"
    provenance["generators"].append(overlapping_generator)
    overlap = tmp_path / "overlap.json"
    overlap.write_text(json.dumps(provenance))
    drifted = deepcopy(cfg)
    drifted["paths"]["item_generation_provenance"] = str(overlap)
    with pytest.raises(PreflightError, match="generator.*judge|overlap"):
        load_item_generation_provenance(drifted)


@pytest.mark.parametrize("mutation", ["canonical", "endpoint", "user_catalog"])
def test_catalog_validation_fails_closed_on_exact_contract_drift(mutation: str) -> None:
    cfg = load_openrouter_config(CONFIG)
    bundle = deepcopy(load_catalog_bundle(CATALOG))
    if mutation == "canonical":
        target = next(row for row in bundle["catalog"]["data"] if row["id"] == "openai/gpt-5.5")
        target["canonical_slug"] = "openai/gpt-5.5-drifted"
    elif mutation == "endpoint":
        endpoint = bundle["endpoints"]["openai/gpt-5.5"]["data"]["endpoints"][0]
        endpoint["tag"] = "openai/priority"
    else:
        bundle["user_catalog"]["data"] = [
            row for row in bundle["user_catalog"]["data"] if row["id"] != "openai/gpt-5.5"
        ]

    with pytest.raises(PreflightError, match="canonical|endpoint|user catalog"):
        validate_catalog_bundle(cfg, bundle)


def test_preflight_receipt_names_every_gate_and_offline_never_authorizes_bank_calls() -> None:
    cfg = load_openrouter_config(CONFIG)
    bundle = load_catalog_bundle(CATALOG)
    validated = validate_catalog_bundle(cfg, bundle)

    offline = build_preflight_receipt(
        cfg,
        validated,
        gate_results={
            **_all_pass(),
            "key": {"status": "not_verified", "detail": "offline"},
        },
        network_verified=False,
        created_at="2026-07-09T00:00:00Z",
    )

    assert REQUIRED_GATE_NAMES == (
        "key",
        "catalog",
        "d36_bank",
        "cue_registry",
        "output_immutability",
        "source_freeze",
        "judge_validation",
        "human_availability",
    )
    assert [gate["name"] for gate in offline["gates"]] == list(REQUIRED_GATE_NAMES)
    assert offline["network_status"] == "NETWORK NOT VERIFIED"
    assert offline["authorized_for_bank"] is False
    assert offline["models_api_only"] is True


def test_receipt_rejects_missing_gate_and_config_hash_drift(tmp_path: Path) -> None:
    cfg = load_openrouter_config(CONFIG)
    validated = validate_catalog_bundle(cfg, load_catalog_bundle(CATALOG))
    missing = _all_pass()
    missing.pop("human_availability")
    with pytest.raises(PreflightError, match="gate"):
        build_preflight_receipt(
            cfg,
            validated,
            gate_results=missing,
            network_verified=True,
            created_at="2026-07-09T00:00:00Z",
        )

    receipt = build_preflight_receipt(
        cfg,
        validated,
        gate_results=_all_pass(),
        network_verified=True,
        created_at="2026-07-09T00:00:00Z",
    )
    path = tmp_path / "receipt.json"
    write_immutable_json(path, receipt)
    assert validate_preflight_receipt(path, cfg)["authorized_for_bank"] is True
    cfg["_provenance"]["config_sha256"] = "0" * 64
    with pytest.raises(PreflightError, match="config"):
        validate_preflight_receipt(path, cfg)


def test_receipt_rejects_stale_online_catalog_authorization(tmp_path: Path) -> None:
    cfg = load_openrouter_config(CONFIG)
    validated = validate_catalog_bundle(cfg, load_catalog_bundle(CATALOG))
    stale = build_preflight_receipt(
        cfg,
        validated,
        gate_results=_all_pass(),
        network_verified=True,
        created_at="2026-01-01T00:00:00Z",
    )
    path = tmp_path / "stale.json"
    write_immutable_json(path, stale)
    with pytest.raises(PreflightError, match="stale"):
        validate_preflight_receipt(path, cfg)


def test_receipt_is_tamper_evident_and_rechecks_frozen_source_inputs(tmp_path: Path) -> None:
    cfg = load_openrouter_config(CONFIG)
    validated = validate_catalog_bundle(cfg, load_catalog_bundle(CATALOG))
    receipt = build_preflight_receipt(
        cfg,
        validated,
        gate_results=_all_pass(),
        network_verified=True,
        created_at="2026-07-09T00:00:00Z",
    )
    path = tmp_path / "receipt.json"
    write_immutable_json(path, receipt)

    changed = json.loads(path.read_text())
    changed["gates"][0]["detail"] = "edited after preflight"
    path.write_text(json.dumps(changed))
    with pytest.raises(PreflightError, match="tamper|digest"):
        validate_preflight_receipt(path, cfg)

    clean_path = tmp_path / "clean.json"
    write_immutable_json(clean_path, receipt)
    drifted = deepcopy(cfg)
    drifted["paths"]["human_labels"] = str(tmp_path / "different-human-labels.csv")
    Path(drifted["paths"]["human_labels"]).write_text(
        "response_id,rater_id,role,final_label,notes\n"
    )
    with pytest.raises(PreflightError, match="source|input"):
        validate_preflight_receipt(clean_path, drifted)


def test_c3_is_sealed_from_development_and_phase_schedules_are_nonreused() -> None:
    cfg = load_openrouter_config(CONFIG)
    surfaces = load_registered_cue_surfaces(cfg)

    development = compile_phase_schedule(cfg, "development", surfaces=surfaces)
    development_arms = {
        surface.cue_arm
        for surface in surfaces
        if surface.surface_id in {row["surface_id"] for row in development.rows}
    }
    assert development_arms == {"C0", "C1", "C2"}
    assert all(row["actor_id"] in {"A01", "A02", "A03"} for row in development.rows)
    assert all(1 <= row["position"] <= 3 for row in development.rows)

    development_ids = {row["surface_id"] for row in development.rows}
    confirmation = compile_phase_schedule(
        cfg,
        "locked-confirmation",
        surfaces=surfaces,
        development_surface_ids=development_ids,
        development_schedule_hashes={development.schedule_hash},
    )
    confirmation_ids = {row["surface_id"] for row in confirmation.rows}
    assert development_ids.isdisjoint(confirmation_ids)
    assert all(surface.sealed for surface in surfaces if surface.surface_id in confirmation_ids)
    assert development.schedule_hash != confirmation.schedule_hash

    with pytest.raises(CounterbalanceError, match="C3"):
        compile_phase_schedule(
            cfg,
            "development",
            surfaces=surfaces,
            requested_surface_ids=confirmation_ids,
        )


def test_schedule_is_written_before_runner_and_no_bank_call_follows_any_failed_gate(
    tmp_path: Path,
) -> None:
    cfg = load_openrouter_config(CONFIG)
    cfg["paths"]["pilots"] = str(tmp_path)
    validated = validate_catalog_bundle(cfg, load_catalog_bundle(CATALOG))
    blocked = build_preflight_receipt(
        cfg,
        validated,
        gate_results={
            **_all_pass(),
            "human_availability": {"status": "fail", "detail": "no panel"},
        },
        network_verified=True,
        created_at="2026-07-09T00:00:00Z",
    )
    blocked_path = tmp_path / "blocked.json"
    write_immutable_json(blocked_path, blocked)
    calls: list[dict] = []

    with pytest.raises(PreflightError, match="authorize"):
        execute_authorized_phase(
            cfg,
            receipt_path=blocked_path,
            phase="development",
            date="20990101",
            bank_runner=lambda **kwargs: calls.append(kwargs),
        )
    assert calls == []
    assert not list(tmp_path.glob("*schedule*.json"))

    allowed = build_preflight_receipt(
        cfg,
        validated,
        gate_results=_all_pass(),
        network_verified=True,
        created_at="2026-07-09T00:00:00Z",
    )
    allowed_path = tmp_path / "allowed.json"
    write_immutable_json(allowed_path, allowed)
    result = execute_authorized_phase(
        cfg,
        receipt_path=allowed_path,
        phase="development",
        date="20990101",
        bank_runner=lambda **kwargs: calls.append(kwargs) or "ran",
    )
    assert result == "ran"
    assert len(calls) == 1
    schedule_path = Path(calls[0]["schedule_path"])
    assert schedule_path.is_file()
    assert calls[0]["schedule_sha256"] == hashlib.sha256(schedule_path.read_bytes()).hexdigest()

    calls.clear()
    with pytest.raises(FileExistsError):
        execute_authorized_phase(
            cfg,
            receipt_path=allowed_path,
            phase="development",
            date="20990101",
            bank_runner=lambda **kwargs: calls.append(kwargs),
        )
    assert calls == []

    resumed = execute_authorized_phase(
        cfg,
        receipt_path=allowed_path,
        phase="development",
        date="20990101",
        bank_runner=lambda **kwargs: calls.append(kwargs) or "resumed",
        resume=True,
    )
    assert resumed == "resumed"
    assert calls[0]["resume"] is True


class _CatalogOnlyClient:
    def __init__(self, bundle: dict) -> None:
        self.bundle = bundle
        self.calls: list[tuple[str, str | None]] = []

    def fetch_catalog(self):
        self.calls.append(("catalog", None))
        return self.bundle["catalog"]

    def fetch_user_catalog(self):
        self.calls.append(("user_catalog", None))
        return self.bundle["user_catalog"]

    def fetch_endpoints(self, model_id: str):
        self.calls.append(("endpoints", model_id))
        return self.bundle["endpoints"][model_id]

    def responses(self, **kwargs):  # pragma: no cover - must never be reached
        raise AssertionError("online preflight must not call Responses API")


def test_online_preflight_fetches_models_catalog_only() -> None:
    cfg = load_openrouter_config(CONFIG)
    fixture = load_catalog_bundle(CATALOG)
    client = _CatalogOnlyClient(fixture)

    bundle = fetch_online_catalog_bundle(cfg, client)

    assert bundle == {
        "catalog": fixture["catalog"],
        "user_catalog": fixture["user_catalog"],
        "endpoints": fixture["endpoints"],
    }
    assert client.calls[:2] == [("catalog", None), ("user_catalog", None)]
    assert [model for kind, model in client.calls if kind == "endpoints"] == (
        EVALUATION_MODELS + CALIBRATION_MODELS + HELD_OUT_MODELS + JUDGE_MODELS
    )


class _SmokeClient:
    def __init__(self) -> None:
        self.calls: list[dict] = []

    def responses(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            text="SMOKE_OK",
            response_id="resp_smoke",
            request_id="req_smoke",
            generation_id="gen_smoke",
            returned_model=kwargs["expected_canonical_slug"],
            usage={"input_tokens": 7, "output_tokens": 2},
            attempt_ledger=(),
            router_metadata={"strategy": "direct", "attempt": 1},
            routing_headers={},
            attempts=1,
            latency_ms=1.0,
            service_tier=kwargs["service_tier"],
        )


def test_smoke_is_fixed_nonbank_nonscoreable_and_immutable(tmp_path: Path) -> None:
    cfg = load_openrouter_config(CONFIG)
    cfg["paths"]["pilots"] = str(tmp_path)
    client = _SmokeClient()

    artifact_path = run_smoke(cfg, client=client, date="20990101")

    artifact = json.loads(artifact_path.read_text())
    assert artifact["evidence_class"] == "smoke"
    assert artifact["scoreable"] is False
    assert artifact["fixture_id"] == "openrouter-neutral-smoke-v1"
    assert artifact["bank_item_id"] is None
    assert "thorns-" not in json.dumps(client.calls).lower()
    assert "fruit" not in json.dumps(client.calls).lower()
    assert len(client.calls) == 1
    with pytest.raises(FileExistsError):
        run_smoke(cfg, client=client, date="20990101")


def test_run_pilot_live_runtime_gate_precedes_item_loading(monkeypatch) -> None:
    cfg = load_openrouter_config(CONFIG)
    calls: list[str] = []
    monkeypatch.setattr(run_pilot, "load_items", lambda _cfg: calls.append("items"))

    with pytest.raises(PreflightError, match="receipt|schedule|phase"):
        run_pilot.run(cfg)
    assert calls == []


def test_run_pilot_freezes_live_branch_strategy_and_cli_modes() -> None:
    cfg = load_openrouter_config(CONFIG)
    assert run_pilot.trajectory_branch_strategy(cfg) == "counterbalanced"
    synthetic = run_pilot.load_config(THORNS / "pilot_config.json")
    assert run_pilot.trajectory_branch_strategy(synthetic) == "synthetic_marker"

    parser = run_pilot.build_parser()
    development = parser.parse_args(
        [
            "--date",
            "20990101",
            "--config",
            str(CONFIG),
            "--phase",
            "development",
            "--preflight-receipt",
            "receipt.json",
        ]
    )
    assert development.phase == "development"
    smoke = parser.parse_args(
        ["--date", "20990101", "--config", str(CONFIG), "--smoke-openrouter"]
    )
    assert smoke.smoke_openrouter is True


def test_smoke_cli_without_key_fails_cleanly_before_writing(monkeypatch, capsys) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    cfg = load_openrouter_config(CONFIG)
    output = Path(cfg["paths"]["pilots"]) / "20991231-smoke-openrouter.json"
    assert not output.exists()

    rc = run_pilot.main(
        [
            "--date",
            "20991231",
            "--config",
            str(CONFIG),
            "--smoke-openrouter",
        ]
    )

    assert rc == 1
    assert "missing" in capsys.readouterr().err.casefold()
    assert not output.exists()
