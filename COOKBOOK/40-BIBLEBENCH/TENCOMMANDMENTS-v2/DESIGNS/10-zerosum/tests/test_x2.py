"""X2 lexical and 10%-fine-tune workflow contracts."""

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _primaries():
    from itembank.build_bank import build_bank

    bank, _, _ = build_bank(seed=20260709)
    return [row for row in bank if row["record_type"] == "advice_primary"]


def _prediction_sha256(predictions):
    canonical = sorted(
        (
            {"item_id": row["item_id"], "predicted_rho": row["predicted_rho"]}
            for row in predictions
        ),
        key=lambda row: row["item_id"],
    )
    return hashlib.sha256(
        json.dumps(
            canonical,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def _rehash_manifest(manifest):
    payload = {
        key: value for key, value in manifest.items()
        if key != "manifest_sha256"
    }
    manifest["manifest_sha256"] = hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def _eligible_evidence(manifest, pre, post, **overrides):
    evidence = {
        "probe_type": "mid_tier_llm",
        "data_basis": "live",
        "model_id": "registered-model",
        "vendor": "registered-vendor",
        "pre_registered": True,
        "manifest_sha256": manifest["manifest_sha256"],
        "pre_predictions_sha256": _prediction_sha256(pre),
        "post_predictions_sha256": _prediction_sha256(post),
    }
    evidence.update(overrides)
    return evidence


def test_x2_splits_never_put_same_core_in_train_and_test():
    from audits.lexical_baseline import grouped_splits

    splits = grouped_splits(_primaries(), group_key="core_id", folds=5)
    assert len(splits) == 5
    for split in splits:
        assert set(split["train_groups"]).isdisjoint(split["test_groups"])
        assert set(split["train_indices"]).isdisjoint(split["test_indices"])
        assert set(split["train_indices"]) | set(split["test_indices"]) == set(range(160))


def test_lexical_audit_reports_all_registered_baselines_and_fixed_thresholds():
    from audits.lexical_baseline import run_lexical_audit

    first = run_lexical_audit(_primaries(), retry_count=0, seed=7)
    second = run_lexical_audit(_primaries(), retry_count=0, seed=7)
    assert first == second
    assert set(first["baselines"]) == {
        "raw_bag_of_words", "normalized_style_bag_of_words", "length_only"
    }
    assert first["target"] == "rho_class"
    assert first["chance_accuracy"] == 0.25
    assert first["normalized_style_max_accuracy"] == 0.35
    assert first["split_unit"] == "core_id"
    assert first["normalized_style_status"] in {"PASS", "REWORK_AUTHORIZED"}
    assert all(0 <= result["accuracy"] <= 1 for result in first["baselines"].values())


def test_lexical_one_retry_state_is_mechanical(monkeypatch):
    import audits.lexical_baseline as lexical

    monkeypatch.setattr(lexical, "_evaluate_text_baseline", lambda *args, **kwargs: 0.80)
    first = lexical.run_lexical_audit(_primaries(), retry_count=0)
    second = lexical.run_lexical_audit(_primaries(), retry_count=1)
    assert first["normalized_style_status"] == "REWORK_AUTHORIZED"
    assert second["normalized_style_status"] == "PARK"
    with pytest.raises(ValueError, match="retry_count"):
        lexical.run_lexical_audit(_primaries(), retry_count=2)


def test_lexical_gate_rejects_partial_39_core_corpus():
    from audits.lexical_baseline import run_lexical_audit

    primaries = _primaries()
    removed_core = primaries[0]["core_id"]
    partial = [row for row in primaries if row["core_id"] != removed_core]

    with pytest.raises(ValueError, match="40 cores|160"):
        run_lexical_audit(partial, retry_count=0, seed=7)


def test_ten_percent_manifest_is_core_grouped_and_deterministic():
    from audits.finetune_probe import build_probe_manifest

    first = build_probe_manifest(_primaries(), seed=19)
    second = build_probe_manifest(_primaries(), seed=19)
    assert first == second
    assert len(first["train_core_ids"]) == 4
    assert len(first["heldout_core_ids"]) == 36
    assert set(first["train_core_ids"]).isdisjoint(first["heldout_core_ids"])
    assert len(first["train_item_ids"]) == 16
    assert len(first["heldout_item_ids"]) == 144
    assert first["train_fraction_by_core"] == pytest.approx(0.10)
    assert len(first["source_records_sha256"]) == 64


def test_probe_manifest_hash_binds_complete_canonical_source_records():
    from audits.finetune_probe import build_probe_manifest

    source_records = _primaries()
    original = build_probe_manifest(source_records, seed=19)
    reordered = build_probe_manifest(list(reversed(source_records)), seed=19)
    assert reordered["source_records_sha256"] == original["source_records_sha256"]

    tampered = deepcopy(source_records)
    tampered[0]["certificate_id"] += "-tampered"
    mutated = build_probe_manifest(tampered, seed=19)
    assert mutated["source_records_sha256"] != original["source_records_sha256"]


def test_probe_manifest_rejects_missing_core_rho_record():
    from audits.finetune_probe import build_probe_manifest

    partial = _primaries()[1:]

    with pytest.raises(ValueError, match="40 cores|160|rho"):
        build_probe_manifest(partial, seed=19)


def test_surrogate_probe_cannot_discharge_llm_finetune_gate():
    from audits.finetune_probe import run_surrogate_probe

    result = run_surrogate_probe(_primaries(), seed=23)
    assert result["eligible_for_x2_finetune_gate"] is False
    assert result["llm_probe_status"] == "NOT_RUN_LLM"
    assert result["data_basis"] == "classical_surrogate"
    assert 0 <= result["heldout_accuracy"] <= 1


def test_real_probe_accepts_aligned_heldout_predictions_and_computes_lift():
    from audits.finetune_probe import build_probe_manifest, evaluate_llm_probe
    from zerosum_common import RHO_GRID

    source_records = _primaries()
    manifest = build_probe_manifest(source_records, seed=29)
    ids = manifest["heldout_item_ids"]
    targets = manifest["heldout_target_by_item"]

    def prediction(item_id, correct):
        target = targets[item_id]
        predicted = target if correct else next(rho for rho in RHO_GRID if rho != target)
        return {"item_id": item_id, "predicted_rho": predicted}

    pre = [prediction(item_id, index % 4 == 0) for index, item_id in enumerate(ids)]
    post = [prediction(item_id, index % 3 == 0) for index, item_id in enumerate(ids)]
    evidence = _eligible_evidence(manifest, pre, post)
    result = evaluate_llm_probe(
        manifest, pre, post, evidence=evidence, source_records=source_records
    )
    assert result["eligible_for_x2_finetune_gate"] is True
    assert result["lift"] == pytest.approx(result["post_accuracy"] - result["pre_accuracy"])
    assert result["verdict"] == ("PASS" if result["lift"] < 0.15 else "PARK")

    with pytest.raises(ValueError, match="heldout"):
        evaluate_llm_probe(
            manifest, pre[:-1], post, evidence=evidence,
            source_records=source_records,
        )
    corrupted_manifest = dict(manifest)
    corrupted_manifest["heldout_target_by_item"] = dict(manifest["heldout_target_by_item"])
    corrupted_manifest["heldout_target_by_item"][ids[0]] = 999
    with pytest.raises(ValueError, match="manifest"):
        evaluate_llm_probe(
            corrupted_manifest, pre, post, evidence=evidence,
            source_records=source_records,
        )
    ineligible = evaluate_llm_probe(
        manifest, pre, post,
        evidence={**evidence, "probe_type": "classical_surrogate"},
        source_records=source_records,
    )
    assert ineligible["eligible_for_x2_finetune_gate"] is False
    assert ineligible["verdict"] == "NOT_RUN_LLM"


@pytest.mark.parametrize(
    "mutate",
    [
        lambda manifest: manifest.__setitem__("train_item_ids", []),
        lambda manifest: manifest["train_core_ids"].__setitem__(
            1, manifest["train_core_ids"][0]
        ),
        lambda manifest: manifest["heldout_target_by_item"].__setitem__(
            manifest["heldout_item_ids"][0],
            next(
                rho for rho in (-1, -1 / 3, 1 / 3, 1)
                if rho
                != manifest["heldout_target_by_item"][
                    manifest["heldout_item_ids"][0]
                ]
            ),
        ),
    ],
)
def test_rehashed_probe_manifest_is_rebuilt_from_frozen_source(mutate):
    from audits.finetune_probe import build_probe_manifest, evaluate_llm_probe

    source_records = _primaries()
    manifest = build_probe_manifest(source_records, seed=29)
    ids = manifest["heldout_item_ids"]
    targets = manifest["heldout_target_by_item"]
    predictions = [
        {"item_id": item_id, "predicted_rho": targets[item_id]}
        for item_id in ids
    ]
    corrupt = deepcopy(manifest)
    mutate(corrupt)
    _rehash_manifest(corrupt)
    evidence = _eligible_evidence(corrupt, predictions, predictions)

    with pytest.raises(ValueError, match="manifest"):
        evaluate_llm_probe(
            corrupt,
            predictions,
            predictions,
            evidence=evidence,
            source_records=source_records,
        )


@pytest.mark.parametrize(
    ("overrides", "expected_field"),
    [
        ({"data_basis": "classical_surrogate"}, "data_basis"),
        ({"manifest_sha256": "0" * 64}, "manifest_sha256"),
        ({"pre_predictions_sha256": "0" * 64}, "pre_predictions_sha256"),
        ({"post_predictions_sha256": "0" * 64}, "post_predictions_sha256"),
    ],
)
def test_probe_provenance_mismatch_is_ineligible(overrides, expected_field):
    from audits.finetune_probe import build_probe_manifest, evaluate_llm_probe

    source_records = _primaries()
    manifest = build_probe_manifest(source_records, seed=29)
    targets = manifest["heldout_target_by_item"]
    predictions = [
        {"item_id": item_id, "predicted_rho": targets[item_id]}
        for item_id in manifest["heldout_item_ids"]
    ]
    evidence = _eligible_evidence(manifest, predictions, predictions, **overrides)

    result = evaluate_llm_probe(
        manifest,
        predictions,
        predictions,
        evidence=evidence,
        source_records=source_records,
    )

    assert evidence[expected_field] == overrides[expected_field]
    assert result["eligible_for_x2_finetune_gate"] is False
    assert result["verdict"] == "NOT_RUN_LLM"


def test_boolean_rho_is_rejected_in_source_and_predictions():
    from audits.finetune_probe import build_probe_manifest, evaluate_llm_probe

    source_records = _primaries()
    corrupt_source = deepcopy(source_records)
    plus_one = next(index for index, row in enumerate(corrupt_source) if row["rho"] == 1)
    corrupt_source[plus_one]["rho"] = True
    with pytest.raises(ValueError, match="rho"):
        build_probe_manifest(corrupt_source, seed=29)

    manifest = build_probe_manifest(source_records, seed=29)
    targets = manifest["heldout_target_by_item"]
    predictions = [
        {"item_id": item_id, "predicted_rho": targets[item_id]}
        for item_id in manifest["heldout_item_ids"]
    ]
    predicted_plus_one = next(
        row for row in predictions if row["predicted_rho"] == 1
    )
    predicted_plus_one["predicted_rho"] = True
    evidence = _eligible_evidence(manifest, predictions, predictions)

    with pytest.raises(ValueError, match="predicted_rho"):
        evaluate_llm_probe(
            manifest,
            predictions,
            predictions,
            evidence=evidence,
            source_records=source_records,
        )
