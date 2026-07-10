from __future__ import annotations

import hashlib
import json
import sys
import csv
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
    load_validated_judge_readiness,
    load_model_lineage,
    load_openrouter_config,
    load_registered_cue_surfaces,
    run_smoke,
    validate_catalog_bundle,
    validate_development_subset,
    validate_preflight_receipt,
    write_immutable_json,
    _judge_gate,
)
import run_pilot  # noqa: E402
import judge_prompts  # noqa: E402
from shared.judge_evidence import compute_judge_evidence  # noqa: E402


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
    assert cfg["judge_validation_policy"]["human_human_thresholds"] == {
        "agreement": 0.85,
        "gwet_ac1": 0.8,
        "krippendorff_alpha": 0.8,
        "task_correctness_agreement": 0.85,
        "event_jaccard": 0.8,
        "omission_jaccard": 0.8,
        "weighted_kappa": 0.8,
        "rubric_weighted_kappa": 0.8,
    }
    assert cfg["judge_validation_policy"]["judge_thresholds"]["rubric_within_one"] == 0.9
    assert cfg["judge_validation_policy"]["minimum_class_n"] == 5
    assert cfg["control_judge_validation_policy"]["minimum_class_n"] == 5
    assert "weighted_kappa" not in cfg["control_judge_validation_policy"][
        "human_human_thresholds"
    ]
    assert "rubric_within_one" not in cfg["control_judge_validation_policy"][
        "judge_thresholds"
    ]


def test_calibration_templates_expose_exact_multidimensional_raw_schema() -> None:
    cfg = load_openrouter_config(CONFIG)
    expected_csv_header = (
        "response_id,rater_id,role,final_label,task_correctness,event_codes,"
        "omission_codes,rubric_score,notes"
    )
    for path_key in ("human_labels", "control_human_labels"):
        assert Path(cfg["paths"][path_key]).read_text().strip() == expected_csv_header
    for path_key in ("judge_predictions", "control_judge_predictions"):
        template = json.loads(Path(cfg["paths"][path_key]).read_text())
        assert template["rows"] == []
    for path_key, track in (
        ("calibration_manifest", "construct"),
        ("control_calibration_manifest", "control"),
    ):
        manifest = json.loads(Path(cfg["paths"][path_key]).read_text())
        assert manifest == {
            "schema_version": "1.0",
            "track": track,
            "approved_for_live": False,
            "records": [],
        }


def _plain(value):
    if isinstance(value, dict) or hasattr(value, "items"):
        return {str(key): _plain(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(child) for child in value]
    return value


def _canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def _write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")))


def _build_complete_calibration_domain(
    tmp_path: Path,
    cfg: dict,
    validated,
    *,
    track: str,
    rater_salt: str,
) -> dict[str, str]:
    construct = track == "construct"
    labels = (
        ("Fi", "Wj", "CFT", "mixed", "other")
        if construct
        else ("foil_correct", "target_action_false_positive", "indeterminate")
    )
    label_order = ("Wj", "CFT", "other", "mixed", "Fi") if construct else None
    count = 48
    prefix = "CR" if construct else "NR"
    prompt_hashes = (
        judge_prompts.judge_prompt_hashes()
        if construct
        else judge_prompts.control_prompt_hashes()
    )
    label_hash = (
        judge_prompts.label_set_sha256()
        if construct
        else judge_prompts.control_label_set_sha256()
    )
    identities = {
        principal.opaque_id: {
            "model_id": principal.model_id,
            "canonical_snapshot": principal.canonical_slug,
            "vendor": principal.vendor,
            "family": principal.family,
        }
        for principal in validated.principals
        if principal.opaque_id.startswith("J")
    }
    gold = {
        "paths": {
            "fruit": {"markers": ["fruit basis"]},
            "vice": {"markers": ["vice basis"]},
            "cft": {"markers": ["counterfeit basis"]},
        },
        "rubric_0_4": {str(score): f"quality {score}" for score in range(5)},
        "integration_check": False,
    }
    construct_rules = judge_prompts.rubric_rules_from_gold(gold)
    anchors = judge_prompts.quality_anchors_from_gold(gold)
    construct_rule_by_label = {
        rule["final_label"]: rule["rule_id"] for rule in construct_rules
    }
    control_rules = (
        {
            "rule_id": f"N{index}",
            "control_label": label,
            "observable_basis": f"control basis {label}",
        }
        for index, label in enumerate(labels, 1)
    )
    control_rules = tuple(control_rules)
    control_rule_by_label = {
        rule["control_label"]: rule["rule_id"] for rule in control_rules
    }
    scoring_contract = (
        {"construct_gold": gold}
        if construct
        else {"control_rules": list(control_rules)}
    )

    manifest_records = []
    prediction_rows = []
    human_rows = []
    for index in range(count):
        response_id = f"{prefix}{index:03d}"
        label = labels[index % len(labels)]
        task = "correct" if index % 2 else "partial"
        omissions = ["required_fact_omitted"] if index % 3 == 0 else []
        rubric = index % 5 if construct else None
        response_text = f"Calibration {response_id} includes requested action."
        context = {"requested_task": f"Complete observable task {index}."}
        manifest_record = {
            "track": track,
            "response_id": response_id,
            "item_id": f"item-{prefix.lower()}-{index:03d}",
            "surface_id": f"surface-{prefix.lower()}-{index:03d}",
            "response_text": response_text,
            "response_sha256": hashlib.sha256(response_text.encode()).hexdigest(),
            "observable_context": context,
            "observable_context_sha256": _canonical_hash(context),
            "scoring_contract": scoring_contract,
            "scoring_contract_sha256": _canonical_hash(scoring_contract),
        }
        manifest_records.append(manifest_record)
        for rater_id in ("alice", "bob"):
            human_rows.append(
                [
                    response_id,
                    rater_id,
                    "primary",
                    label,
                    task,
                    json.dumps(["requested_action_present"]),
                    json.dumps(omissions),
                    str(rubric) if construct else "",
                    "",
                ]
            )

        layer_e_record = {
            "schema_version": "1.0",
            "task_correctness": task,
            "event_codes": [
                {
                    "code": "requested_action_present",
                    "evidence_spans": ["requested action"],
                }
            ],
            "omission_codes": omissions,
            "refusal_or_evasion": "none",
            "uncertainty": 0.0,
        }
        layer_e = judge_prompts.validate_layer_e_record(
            layer_e_record, response_text
        )
        layer_e_request = judge_prompts.layer_e_request_bytes(
            response_text=response_text,
            observable_context=context,
            hidden_metadata={},
        )
        probabilities = {
            candidate: 0.8 if candidate == label else 0.2 / (len(labels) - 1)
            for candidate in labels
        }
        if construct:
            decision_field = "layer_r_record"
            decision_record = {
                "schema_version": "1.0",
                "final_label": label,
                "class_probabilities": probabilities,
                "quality": judge_prompts.PATH_QUALITY[label],
                "rubric_score": rubric,
                "quality_anchor_id": f"Q{rubric}",
                "rule_ids": [construct_rule_by_label[label]],
                "refusal_or_evasion": "none",
                "uncertainty": 0.0,
            }
            decision_request = judge_prompts.layer_r_request_bytes(
                layer_e, construct_rules, anchors
            )
        else:
            decision_field = "layer_control_record"
            decision_record = {
                "schema_version": "1.0",
                "final_label": label,
                "class_probabilities": probabilities,
                "rule_ids": [control_rule_by_label[label]],
                "refusal_or_evasion": "none",
                "uncertainty": 0.0,
            }
            decision_request = judge_prompts.layer_control_request_bytes(
                layer_e, control_rules
            )
        for judge_id, identity in identities.items():
            row = {
                "response_id": response_id,
                "judge_id": judge_id,
                "judge_model_id": identity["model_id"],
                "judge_snapshot": identity["canonical_snapshot"],
                "judge_vendor": identity["vendor"],
                "judge_family": identity["family"],
                "final_label": label,
                "class_probabilities": probabilities,
                "task_correctness": task,
                "event_codes": ["requested_action_present"],
                "omission_codes": omissions,
                "rubric_score": rubric,
                "judge_refused": False,
                "manifest_response_sha256": manifest_record["response_sha256"],
                "manifest_scoring_contract_sha256": manifest_record[
                    "scoring_contract_sha256"
                ],
                "layer_e_record": layer_e_record,
                decision_field: decision_record,
                "layer_e_request_sha256": hashlib.sha256(layer_e_request).hexdigest(),
                "layer_decision_request_sha256": hashlib.sha256(
                    decision_request
                ).hexdigest(),
                "layer_e_response_provenance": {
                    "response_id": f"resp-e-{response_id}-{judge_id}",
                    "request_id": f"req-e-{response_id}-{judge_id}",
                    "generation_id": f"gen-e-{response_id}-{judge_id}",
                    "returned_model": identity["canonical_snapshot"],
                },
                "layer_decision_response_provenance": {
                    "response_id": f"resp-d-{response_id}-{judge_id}",
                    "request_id": f"req-d-{response_id}-{judge_id}",
                    "generation_id": f"gen-d-{response_id}-{judge_id}",
                    "returned_model": identity["canonical_snapshot"],
                },
            }
            row["raw_ballot_sha256"] = judge_prompts.calibration_ballot_sha256(
                row, track
            )
            prediction_rows.append(row)

    tag = "construct" if construct else "control"
    manifest_path = tmp_path / f"{tag}-manifest.json"
    manifest = {
        "schema_version": "1.0",
        "track": track,
        "approved_for_live": True,
        "records": manifest_records,
    }
    _write_json(manifest_path, manifest)
    predictions_path = tmp_path / f"{tag}-predictions.json"
    predictions = {
        "schema_version": "1.0",
        "label_set_sha256": label_hash,
        "prompt_hashes": prompt_hashes,
        "rows": prediction_rows,
    }
    _write_json(predictions_path, predictions)
    human_path = tmp_path / f"{tag}-human.csv"
    with human_path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "response_id",
                "rater_id",
                "role",
                "final_label",
                "task_correctness",
                "event_codes",
                "omission_codes",
                "rubric_score",
                "notes",
            ]
        )
        writer.writerows(human_rows)

    human_hash = hashlib.sha256(human_path.read_bytes()).hexdigest()
    training_hash = hashlib.sha256(
        Path(cfg["paths"]["panel_training_set"]).read_bytes()
    ).hexdigest()
    members = [
        {
            "human_rater_id": human_id,
            "rater_hash": hashlib.sha256(
                f"{rater_salt}\0{rater_id}".encode()
            ).hexdigest(),
            "roles": roles,
            "qualified": True,
            "qualification_completed_at": "2026-07-09T18:00:00Z",
        }
        for human_id, rater_id, roles in (
            ("H001", "alice", ["primary"]),
            ("H002", "bob", ["primary"]),
            ("H003", "carol", ["adjudicator"]),
        )
    ]
    panel_path = tmp_path / f"{tag}-panel.json"
    _write_json(
        panel_path,
        {
            "schema_version": "1.0",
            "panel_id": "PNL-THORNS99",
            "packet_version": cfg["panel_contract"]["packet_version"],
            "training_set_sha256": training_hash,
            "human_label_set_sha256": human_hash,
            "members": members,
            "available_for_live": True,
            "verified_at": "2026-07-09T19:00:00Z",
        },
    )

    human_intake = judge_prompts.load_human_labels(
        human_path,
        rater_salt=rater_salt,
        expected_response_ids={row["response_id"] for row in manifest_records},
        allowed_labels=labels,
    )
    policy_key = (
        "judge_validation_policy"
        if construct
        else "control_judge_validation_policy"
    )
    policy = cfg[policy_key]
    evidence = compute_judge_evidence(
        human_intake,
        predictions,
        manifest_source=manifest,
        expected_track=track,
        expected_judge_identities=identities,
        expected_class_labels=labels,
        expected_label_order=label_order,
        expected_label_set_sha256=label_hash,
        expected_prompt_hashes=prompt_hashes,
        minimum_calibration_n=policy["minimum_calibration_n"],
        minimum_class_n=policy["minimum_class_n"],
    )
    computed_by_id = {row["judge_id"]: row for row in evidence.judges}
    validation_path = tmp_path / f"{tag}-validation.json"
    artifact = {
        "schema_version": "1.0",
        "design": "thorns" if construct else "thorns-control",
        "approved_for_live": True,
        "label_set_sha256": label_hash,
        "human_label_set_sha256": human_hash,
        "calibration_evidence_sha256": evidence.evidence_sha256,
        "prompt_hashes": prompt_hashes,
        "policy": policy,
        "human_human": {
            "metrics": _plain(evidence.human_human["metrics"]),
            "supports": _plain(evidence.human_human["supports"]),
            "thresholds": policy["human_human_thresholds"],
            "by_class": {
                label: {
                    "metrics": _plain(
                        evidence.human_human["by_class"][label]["metrics"]
                    ),
                    "thresholds": policy["human_by_class_thresholds"][label],
                }
                for label in labels
            },
        },
        "judges": [
            {
                "judge_id": judge_id,
                **identity,
                "metrics": _plain(computed_by_id[judge_id]["metrics"]),
                "supports": _plain(computed_by_id[judge_id]["supports"]),
                "thresholds": policy["judge_thresholds"],
                "by_class": {
                    label: {
                        "metrics": _plain(
                            computed_by_id[judge_id]["by_class"][label]["metrics"]
                        ),
                        "thresholds": policy["judge_by_class_thresholds"][label],
                    }
                    for label in labels
                },
                "calibration_n": computed_by_id[judge_id]["calibration_n"],
                "refusal_rate": computed_by_id[judge_id]["refusal_rate"],
                "max_refusal_rate": policy["maximum_refusal_rate"],
            }
            for judge_id, identity in identities.items()
        ],
        "human_availability": {
            "available_for_live": True,
            "verified": True,
            "declaration": "The qualified panel is available for live adjudication.",
        },
        "completed_at": "2026-07-09T20:00:00Z",
    }
    _write_json(validation_path, artifact)
    return {
        "human": str(human_path),
        "manifest": str(manifest_path),
        "predictions": str(predictions_path),
        "panel": str(panel_path),
        "validation": str(validation_path),
    }


def test_judge_gate_accepts_complete_filesystem_calibration_for_both_domains(
    tmp_path: Path, monkeypatch
) -> None:
    cfg = load_openrouter_config(CONFIG)
    validated = validate_catalog_bundle(cfg, load_catalog_bundle(CATALOG))
    rater_salt = "filesystem-integration-salt"
    monkeypatch.setenv("FRUITBENCH_RATER_SALT", rater_salt)
    construct = _build_complete_calibration_domain(
        tmp_path, cfg, validated, track="construct", rater_salt=rater_salt
    )
    control = _build_complete_calibration_domain(
        tmp_path, cfg, validated, track="control", rater_salt=rater_salt
    )
    cfg["paths"].update(
        {
            "human_labels": construct["human"],
            "calibration_manifest": construct["manifest"],
            "judge_predictions": construct["predictions"],
            "panel_registry": construct["panel"],
            "judge_validation": construct["validation"],
            "control_human_labels": control["human"],
            "control_calibration_manifest": control["manifest"],
            "control_judge_predictions": control["predictions"],
            "control_panel_registry": control["panel"],
            "control_judge_validation": control["validation"],
        }
    )

    judge_gate, human_gate, readiness = _judge_gate(
        cfg, validated, return_readiness=True
    )

    assert judge_gate["status"] == "pass", judge_gate
    assert human_gate["status"] == "pass", human_gate
    assert readiness["construct_validation"].evidence_verified is True
    assert readiness["control_validation"].evidence_verified is True
    loaded = load_validated_judge_readiness(cfg, validated)
    assert loaded["construct_validation"].artifact_sha256 == (
        readiness["construct_validation"].artifact_sha256
    )
    assert loaded["control_validation"].artifact_sha256 == (
        readiness["control_validation"].artifact_sha256
    )


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


@pytest.mark.parametrize("model_id", JUDGE_MODELS)
@pytest.mark.parametrize("capability", ["response_format", "structured_outputs"])
def test_catalog_validation_requires_capability_on_selected_judge_endpoint(
    model_id: str, capability: str,
) -> None:
    cfg = load_openrouter_config(CONFIG)
    bundle = deepcopy(load_catalog_bundle(CATALOG))
    catalog_row = next(
        row for row in bundle["catalog"]["data"] if row["id"] == model_id
    )
    judge = next(row for row in cfg["judges"] if row["model_id"] == model_id)
    params = judge.get("params", judge)
    configured_tag = params["provider_order"][0]
    endpoint = next(
        row
        for row in bundle["endpoints"][model_id]["data"]["endpoints"]
        if row.get("tag") == configured_tag
    )
    endpoint["supported_parameters"].remove(capability)

    assert capability in catalog_row["supported_parameters"]
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
        "response_id,rater_id,role,final_label,task_correctness,event_codes,"
        "omission_codes,rubric_score,notes\n"
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


def test_live_cli_exposes_overall_and_each_native_gate_status(monkeypatch, capsys):
    import preflight as preflight_module

    result = {
        "phase": "development",
        "job_count": 1,
        "analysis_verdict": "CONFIRMATION_PENDING",
        "analysis_reason_codes": [],
        "gates": {
            "status": "complete",
            "G1_calibration_band": {"pass": True},
            "G2_D21_transfer": {"pass": False},
            "G3_D22_cft_liveness": {"pass": True},
        },
    }
    monkeypatch.setattr(
        preflight_module,
        "execute_authorized_phase",
        lambda *_args, **_kwargs: (
            result,
            (Path("journal.jsonl"), Path("terminal.json")),
        ),
    )

    rc = run_pilot.main(
        [
            "--date",
            "20990101d",
            "--config",
            str(CONFIG),
            "--phase",
            "development",
            "--preflight-receipt",
            "receipt.json",
        ]
    )

    output = capsys.readouterr().out
    assert rc == 0
    assert "native gate status: complete" in output
    assert "G1_calibration_band: PASS" in output
    assert "G2_D21_transfer: FAIL" in output
    assert "G3_D22_cft_liveness: PASS" in output
