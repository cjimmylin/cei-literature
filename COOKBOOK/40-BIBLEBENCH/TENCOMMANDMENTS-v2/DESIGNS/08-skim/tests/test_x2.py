"""Contracts for the two mandatory SKIM P1 X2 workflows."""

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "itembank" / "bank" / "p1-public.jsonl"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _primaries():
    return [
        json.loads(line)
        for line in BANK_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and json.loads(line)["record_type"] == "primary"
    ]


def _canonical_sha256(value):
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def _prediction_sha256(predictions):
    canonical = sorted(
        (
            {
                "item_id": row["item_id"],
                "predicted_magnitude_tier": row["predicted_magnitude_tier"],
            }
            for row in predictions
        ),
        key=lambda row: row["item_id"],
    )
    return _canonical_sha256(canonical)


FROZEN_PROBE_SEED = 2026071001
FROZEN_CLASSIFIER_SEED = 2026071001
FROZEN_SOURCE_SHA256 = (
    "21c0031062348e9c753a72cdf45147e8b3f1ffa378acfc805ba61803a44f2886"
)
FROZEN_MANIFEST_SHA256 = (
    "236db36b29c0555634a0c41f7bdf20c9774c0b7d9d3908396e3b1cb8313caebf"
)


def _fictional_candidate_claims(manifest, pre, post, **overrides):
    claims = {
        "probe_type": "mid_tier_llm",
        "data_basis": "live",
        "model_tier": "mid_tier",
        "model_id": "fictional-no-call-model",
        "vendor": "fictional-no-call-provider",
        "pre_registered": True,
        "synthetic": False,
        "manifest_sha256": manifest["manifest_sha256"],
        "pre_predictions_sha256": _prediction_sha256(pre),
        "post_predictions_sha256": _prediction_sha256(post),
    }
    claims.update(overrides)
    return claims


def _predictions(manifest, correct_count):
    ids = manifest["heldout_item_ids"]
    targets = manifest["heldout_target_by_item"]
    result = []
    for index, item_id in enumerate(ids):
        target = targets[item_id]
        predicted = target if index < correct_count else (target % 4) + 1
        result.append(
            {
                "item_id": item_id,
                "predicted_magnitude_tier": predicted,
            }
        )
    return result


def _rehash_manifest(manifest):
    payload = {
        key: value for key, value in manifest.items()
        if key != "manifest_sha256"
    }
    manifest["manifest_sha256"] = _canonical_sha256(payload)


def test_x2_splits_are_deterministic_and_never_cross_scenario_cores():
    from audits.lexical_baseline import grouped_splits

    first = grouped_splits(_primaries(), group_key="core_id", folds=5)
    second = grouped_splits(_primaries(), group_key="core_id", folds=5)

    assert first == second
    assert len(first) == 5
    assert _canonical_sha256(
        [split["test_groups"] for split in first]
    ) == "4f6471c672fbd14c7f0954d2d087dac605df32aafe44fc4bd9814ca6342b89c8"
    for split in first:
        assert set(split["train_groups"]).isdisjoint(split["test_groups"])
        assert set(split["train_indices"]).isdisjoint(split["test_indices"])
        assert set(split["train_indices"]) | set(split["test_indices"]) == set(
            range(160)
        )


def test_number_normalization_removes_plain_currency_decimal_and_exponent_values():
    from audits.lexical_baseline import normalize_numbers

    normalized = normalize_numbers("USD 0.001, $10 and -2.5e+3; route7 stays lexical")

    assert normalized == "USD NUM, $ NUM and NUM; route7 stays lexical"


def test_lexical_audit_reports_registered_gate_and_diagnostic_baselines():
    from audits.lexical_baseline import (
        AUTHORIZED_REVISED_SOURCE_SHA256,
        PREREGISTERED_LEXICAL_CLASSIFIER_SEED,
        run_lexical_audit,
    )

    first = run_lexical_audit(_primaries(), seed=FROZEN_CLASSIFIER_SEED)
    second = run_lexical_audit(_primaries(), seed=FROZEN_CLASSIFIER_SEED)

    assert first == second
    assert PREREGISTERED_LEXICAL_CLASSIFIER_SEED == FROZEN_CLASSIFIER_SEED
    assert AUTHORIZED_REVISED_SOURCE_SHA256 is None
    assert first["study_id"] == "SKIM-P1"
    assert first["target"] == "magnitude_tier"
    assert first["target_classes"] == [1, 2, 3, 4]
    assert first["split_unit"] == "scenario_core"
    assert first["group_key"] == "core_id"
    assert first["chance_accuracy"] == 0.25
    assert first["normalized_style_max_accuracy"] == 0.35
    assert first["baselines"]["normalized_prose_style_bag_of_words"][
        "accuracy"
    ] == 0.25
    assert first["normalized_style_status"] == "PASS"
    assert first["data_basis"] == "public_bank_construction_audit"
    assert first["synthetic"] is False
    assert first["eligible_for_empirical_decision"] is False
    assert first["eligible_for_x2_lexical_gate"] is True
    assert first["surface_rework_count"] == 0
    assert first["revision_authorization_status"] == (
        "NOT_NEEDED_BANK_PASSES"
    )
    assert first["classifier_seed"] == FROZEN_CLASSIFIER_SEED
    assert first["prior_result_sha256"] is None
    assert first["result_sha256"] == (
        "c6bd91cc003b38cd314312edc3d6e9982c4a5357da00b61ff862718603efd444"
    )
    assert len(first["source_records_sha256"]) == 64
    assert set(first["baselines"]) == {
        "raw_structured_bag_of_words",
        "normalized_prose_style_bag_of_words",
        "length_only",
    }
    assert first["baselines"]["raw_structured_bag_of_words"]["decision_role"] == (
        "DIAGNOSTIC_ONLY"
    )
    assert first["baselines"]["raw_structured_bag_of_words"][
        "interpretation"
    ] == "STRUCTURED_MAGNITUDE_MANIPULATION_SANITY_CHECK"
    assert first["baselines"]["normalized_prose_style_bag_of_words"][
        "decision_role"
    ] == "REGISTERED_GATE"
    assert first["baselines"]["length_only"]["decision_role"] == (
        "DIAGNOSTIC_ONLY"
    )
    assert all(
        0.0 <= baseline["accuracy"] <= 1.0
        for baseline in first["baselines"].values()
    )


def test_planted_surface_leak_fails_gate_without_minting_rework_authority():
    from audits.lexical_baseline import run_lexical_audit

    leaked = deepcopy(_primaries())
    tier_tokens = {
        1: "amberquartz",
        2: "bluequartz",
        3: "copperquartz",
        4: "duskquartz",
    }
    for row in leaked:
        row["requests"][0]["prompt"] += (
            " Surface wording marker %s." % tier_tokens[row["magnitude_tier"]]
        )

    result = run_lexical_audit(leaked, seed=FROZEN_CLASSIFIER_SEED)

    assert result["baselines"]["normalized_prose_style_bag_of_words"][
        "accuracy"
    ] > 0.35
    assert result["eligible_for_x2_lexical_gate"] is False
    assert result["normalized_style_status"] == "PARK_UNREGISTERED_SOURCE"


def test_surface_rework_branches_are_disabled_until_one_hash_is_frozen(
    monkeypatch,
):
    import audits.lexical_baseline as lexical

    monkeypatch.setattr(
        lexical,
        "_evaluate_text_baseline",
        lambda *args, **kwargs: 0.80,
    )
    monkeypatch.setattr(
        lexical,
        "_evaluate_length_baseline",
        lambda *args, **kwargs: 0.25,
    )
    initial = lexical.run_lexical_audit(
        _primaries(), seed=FROZEN_CLASSIFIER_SEED
    )
    assert initial["normalized_style_status"] == (
        "REWORK_PENDING_FROZEN_REVISION"
    )
    assert initial["surface_rework_count"] == 0
    assert initial["authorized_revised_source_sha256"] is None

    branch_a = deepcopy(_primaries())
    branch_a[0]["requests"][0]["prompt"] += " Surface revision branch A."
    branch_b = deepcopy(_primaries())
    branch_b[0]["requests"][0]["prompt"] += " Surface revision branch B."

    for branch in (branch_a, branch_b):
        with pytest.raises(ValueError, match="no revised source hash is frozen"):
            lexical.run_lexical_audit(
                branch,
                prior_result=initial,
                seed=FROZEN_CLASSIFIER_SEED,
            )


def test_one_frozen_surface_revision_hash_cannot_authorize_a_branch(
    monkeypatch,
):
    import audits.lexical_baseline as lexical

    monkeypatch.setattr(
        lexical,
        "_evaluate_text_baseline",
        lambda *args, **kwargs: 0.80,
    )
    monkeypatch.setattr(
        lexical,
        "_evaluate_length_baseline",
        lambda *args, **kwargs: 0.25,
    )
    branch_a = deepcopy(_primaries())
    branch_a[0]["requests"][0]["prompt"] += " Frozen surface revision A."
    branch_b = deepcopy(_primaries())
    branch_b[0]["requests"][0]["prompt"] += " Unfrozen surface revision B."
    frozen_hash = lexical.source_records_sha256(branch_a)
    monkeypatch.setattr(
        lexical, "AUTHORIZED_REVISED_SOURCE_SHA256", frozen_hash
    )
    initial = lexical.run_lexical_audit(
        _primaries(), seed=FROZEN_CLASSIFIER_SEED
    )

    accepted = lexical.run_lexical_audit(
        branch_a,
        prior_result=initial,
        seed=FROZEN_CLASSIFIER_SEED,
    )
    assert accepted["surface_rework_count"] == 1
    assert accepted["normalized_style_status"] == "PARK"
    assert accepted["authorized_revised_source_sha256"] == frozen_hash

    with pytest.raises(ValueError, match="frozen revised source hash"):
        lexical.run_lexical_audit(
            branch_b,
            prior_result=initial,
            seed=FROZEN_CLASSIFIER_SEED,
        )


@pytest.mark.parametrize(
    "mutation",
    [
        "logical_record_id",
        "core_id",
        "magnitude_tier",
        "structured_state",
        "response_schema",
        "options",
        "metadata",
    ],
)
def test_frozen_revision_rejects_non_surface_semantic_changes(
    monkeypatch, mutation
):
    import audits.lexical_baseline as lexical

    monkeypatch.setattr(
        lexical,
        "_evaluate_text_baseline",
        lambda *args, **kwargs: 0.80,
    )
    monkeypatch.setattr(
        lexical,
        "_evaluate_length_baseline",
        lambda *args, **kwargs: 0.25,
    )
    revised = deepcopy(_primaries())
    revised[0]["requests"][0]["prompt"] += " Surface-only candidate."
    if mutation == "logical_record_id":
        revised[0]["logical_record_id"] += "-changed"
    elif mutation == "core_id":
        revised[0]["core_id"], revised[4]["core_id"] = (
            revised[4]["core_id"], revised[0]["core_id"]
        )
    elif mutation == "magnitude_tier":
        revised[0]["magnitude_tier"], revised[1]["magnitude_tier"] = (
            revised[1]["magnitude_tier"], revised[0]["magnitude_tier"]
        )
    elif mutation == "structured_state":
        revised[0]["requests"][0]["structured_state"]["scenario"] += (
            " Changed semantics."
        )
    elif mutation == "response_schema":
        revised[0]["requests"][0]["response_schema"]["title"] = "changed"
    elif mutation == "options":
        revised[0]["requests"][0]["options"][0]["label"] += " changed"
    else:
        revised[0]["domain"] = "changed_metadata"
    monkeypatch.setattr(
        lexical,
        "AUTHORIZED_REVISED_SOURCE_SHA256",
        lexical.source_records_sha256(revised),
    )
    initial = lexical.run_lexical_audit(
        _primaries(), seed=FROZEN_CLASSIFIER_SEED
    )

    with pytest.raises(ValueError, match="surface-only revision"):
        lexical.run_lexical_audit(
            revised,
            prior_result=initial,
            seed=FROZEN_CLASSIFIER_SEED,
        )


def test_only_normalized_style_controls_lexical_gate(monkeypatch):
    import audits.lexical_baseline as lexical

    scores = iter((1.0, 0.25))
    monkeypatch.setattr(
        lexical,
        "_evaluate_text_baseline",
        lambda *args, **kwargs: next(scores),
    )
    monkeypatch.setattr(
        lexical,
        "_evaluate_length_baseline",
        lambda *args, **kwargs: 1.0,
    )

    result = lexical.run_lexical_audit(
        _primaries(), seed=FROZEN_CLASSIFIER_SEED
    )

    assert result["baselines"]["raw_structured_bag_of_words"]["accuracy"] == 1.0
    assert result["baselines"]["length_only"]["accuracy"] == 1.0
    assert result["normalized_style_status"] == "PASS"


def test_lexical_audit_rejects_caller_asserted_rework_counts():
    from audits.lexical_baseline import run_lexical_audit

    with pytest.raises(TypeError, match="surface_rework_count"):
        run_lexical_audit(
            _primaries(),
            surface_rework_count=0,
            seed=FROZEN_CLASSIFIER_SEED,
        )


@pytest.mark.parametrize("seed", [0, 7, 2026071000, 2026071002, True])
def test_gate_eligible_lexical_audit_rejects_nonfrozen_seed(seed):
    from audits.lexical_baseline import run_lexical_audit

    with pytest.raises(ValueError, match="preregistered classifier seed"):
        run_lexical_audit(_primaries(), seed=seed)


def test_x2_rejects_partial_or_duplicate_primary_corpora():
    from audits.finetune_probe import build_probe_manifest
    from audits.lexical_baseline import run_lexical_audit

    rows = _primaries()
    partial = rows[1:]
    duplicate = deepcopy(rows)
    duplicate[-1]["logical_record_id"] = duplicate[0]["logical_record_id"]

    with pytest.raises(ValueError, match="160|tier|40 cores"):
        run_lexical_audit(partial, seed=FROZEN_CLASSIFIER_SEED)
    with pytest.raises(ValueError, match="unique"):
        build_probe_manifest(duplicate, seed=FROZEN_PROBE_SEED)


def test_ten_percent_manifest_is_core_grouped_bound_and_deterministic():
    from audits.finetune_probe import (
        PREREGISTERED_MANIFEST_SHA256,
        PREREGISTERED_PROBE_SEED,
        PREREGISTERED_SOURCE_RECORDS_SHA256,
        build_probe_manifest,
    )

    first = build_probe_manifest(_primaries(), seed=FROZEN_PROBE_SEED)
    second = build_probe_manifest(
        list(reversed(_primaries())), seed=FROZEN_PROBE_SEED
    )

    assert first == second
    assert PREREGISTERED_PROBE_SEED == FROZEN_PROBE_SEED
    assert PREREGISTERED_SOURCE_RECORDS_SHA256 == FROZEN_SOURCE_SHA256
    assert PREREGISTERED_MANIFEST_SHA256 == FROZEN_MANIFEST_SHA256
    assert first["seed"] == FROZEN_PROBE_SEED
    assert first["study_id"] == "SKIM-P1"
    assert first["target"] == "magnitude_tier"
    assert first["split_unit"] == "scenario_core"
    assert first["group_key"] == "core_id"
    assert first["train_fraction_by_core"] == 0.10
    assert len(first["train_core_ids"]) == 4
    assert len(first["heldout_core_ids"]) == 36
    assert set(first["train_core_ids"]).isdisjoint(first["heldout_core_ids"])
    assert len(first["train_item_ids"]) == 16
    assert len(first["heldout_item_ids"]) == 144
    assert set(first["train_item_ids"]).isdisjoint(first["heldout_item_ids"])
    assert first["source_records_sha256"] == FROZEN_SOURCE_SHA256
    assert first["manifest_sha256"] == FROZEN_MANIFEST_SHA256
    assert first["synthetic"] is False


@pytest.mark.parametrize("seed", [0, 2026071000, 2026071002, True])
def test_probe_manifest_rejects_every_nonpreregistered_seed(seed):
    from audits.finetune_probe import build_probe_manifest

    with pytest.raises(ValueError, match="preregistered probe seed"):
        build_probe_manifest(_primaries(), seed=seed)


def test_probe_manifest_rejects_every_nonpreregistered_source_rehash():
    from audits.finetune_probe import build_probe_manifest

    source = _primaries()
    tampered = deepcopy(source)
    tampered[0]["requests"][0]["prompt"] += " Tampered."

    with pytest.raises(ValueError, match="preregistered source hash"):
        build_probe_manifest(tampered, seed=FROZEN_PROBE_SEED)


def test_classical_surrogate_is_plumbing_only_and_canonical():
    from audits.finetune_probe import run_surrogate_probe

    first = run_surrogate_probe(_primaries(), seed=FROZEN_PROBE_SEED)
    second = run_surrogate_probe(_primaries(), seed=FROZEN_PROBE_SEED)

    assert first == second
    assert first["data_basis"] == "classical_surrogate"
    assert first["synthetic"] is True
    assert first["diagnostic_only"] is True
    assert first["eligible_for_empirical_decision"] is False
    assert first["eligible_for_x2_finetune_gate"] is False
    assert first["llm_probe_status"] == "NOT_RUN_LLM"
    assert first["surrogate_role"] == "SPLIT_AND_STATISTIC_PLUMBING_ONLY"
    assert 0.0 <= first["heldout_accuracy"] <= 1.0


def test_fictional_plain_mapping_never_discharges_real_llm_gate():
    from audits.finetune_probe import build_probe_manifest, evaluate_llm_probe

    source = _primaries()
    manifest = build_probe_manifest(source, seed=FROZEN_PROBE_SEED)
    pre = _predictions(manifest, correct_count=36)
    post = _predictions(manifest, correct_count=58)
    fictional_claims = _fictional_candidate_claims(
        manifest,
        pre,
        post,
        execution_bundle_verified=True,
        transport_calls=0,
    )

    result = evaluate_llm_probe(
        manifest,
        pre,
        post,
        evidence=fictional_claims,
        source_records=source,
    )

    assert result["eligible_for_x2_finetune_gate"] is False
    assert result["eligible_for_empirical_decision"] is False
    assert result["evidence_status"] == (
        "CANDIDATE_ARRAYS_ONLY_NO_EXECUTION_BUNDLE_VERIFIER"
    )
    assert result["data_basis"] == "unverified_candidate_arrays"
    assert result["synthetic"] is None
    assert result["lift"] == pytest.approx(22 / 144)
    assert result["lift_park_min"] == 0.15
    assert result["verdict"] == "NOT_RUN_LLM"
    assert result["candidate_claims"] == fictional_claims


def test_candidate_lift_below_boundary_is_still_not_run_llm():
    from audits.finetune_probe import build_probe_manifest, evaluate_llm_probe

    source = _primaries()
    manifest = build_probe_manifest(source, seed=FROZEN_PROBE_SEED)
    pre = _predictions(manifest, correct_count=36)
    post = _predictions(manifest, correct_count=57)
    claims = _fictional_candidate_claims(manifest, pre, post)

    result = evaluate_llm_probe(
        manifest,
        pre,
        post,
        evidence=claims,
        source_records=source,
    )

    assert result["lift"] == pytest.approx(21 / 144)
    assert result["verdict"] == "NOT_RUN_LLM"


def test_probe_predictions_must_exactly_cover_heldout_ids_and_use_tiers():
    from audits.finetune_probe import build_probe_manifest, evaluate_llm_probe

    source = _primaries()
    manifest = build_probe_manifest(source, seed=FROZEN_PROBE_SEED)
    predictions = _predictions(manifest, correct_count=36)
    claims = _fictional_candidate_claims(manifest, predictions, predictions)

    with pytest.raises(ValueError, match="heldout"):
        evaluate_llm_probe(
            manifest,
            predictions[:-1],
            predictions,
            evidence=claims,
            source_records=source,
        )

    boolean_prediction = deepcopy(predictions)
    boolean_prediction[0]["predicted_magnitude_tier"] = True
    with pytest.raises(ValueError, match="predicted_magnitude_tier"):
        evaluate_llm_probe(
            manifest,
            boolean_prediction,
            predictions,
            evidence=claims,
            source_records=source,
        )


def test_rehashed_manifest_tampering_is_rebuilt_from_frozen_source():
    from audits.finetune_probe import build_probe_manifest, evaluate_llm_probe

    source = _primaries()
    manifest = build_probe_manifest(source, seed=FROZEN_PROBE_SEED)
    predictions = _predictions(manifest, correct_count=36)
    corrupt = deepcopy(manifest)
    corrupt["train_item_ids"] = []
    _rehash_manifest(corrupt)
    claims = _fictional_candidate_claims(corrupt, predictions, predictions)

    with pytest.raises(ValueError, match="manifest"):
        evaluate_llm_probe(
            corrupt,
            predictions,
            predictions,
            evidence=claims,
            source_records=source,
        )
