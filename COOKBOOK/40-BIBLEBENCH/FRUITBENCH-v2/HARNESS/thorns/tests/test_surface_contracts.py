from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

import pytest
import yaml


THORNS = Path(__file__).resolve().parents[1]
ITEMS = THORNS.parents[1] / "ITEMS" / "thorns"
if str(THORNS) not in sys.path:
    sys.path.insert(0, str(THORNS))

import surface_contracts  # noqa: E402


LOCK = ITEMS / "CUE-DEVELOPMENT-LOCK-20260709.json"


def test_development_surface_contracts_are_hash_bound_typed_and_length_matched():
    registry = surface_contracts.load_surface_contracts(
        ITEMS,
        phase="development",
        development_lock_path=LOCK,
    )

    assert len(registry) == 18
    assert {row.cue_arm for row in registry} == {"C0", "C1", "C2"}
    assert sum(row.mode == "construct" for row in registry) == 12
    assert sum(row.mode == "null_control" for row in registry) == 6
    assert all(0.85 <= row.word_count / row.c0_word_count <= 1.15 for row in registry)
    assert all(
        row.headline_eligible is (row.item_id != "thorns-paternalcrush-002")
        for row in registry
    )
    for row in registry:
        assert hashlib.sha256(row.text.encode()).hexdigest() == row.text_sha256


def test_null_contracts_cannot_leak_construct_labels_or_path_gold():
    registry = surface_contracts.load_surface_contracts(
        ITEMS,
        phase="development",
        development_lock_path=LOCK,
    )
    nulls = [row for row in registry if row.cue_arm == "C2"]
    assert len(nulls) == 6
    for row in nulls:
        assert set(row.scoring_contract["observable_rules"]) == {
            "foil_correct",
            "target_action_false_positive",
            "indeterminate",
        }
        encoded = repr(row.scoring_contract)
        assert all(token not in encoded for token in ("'Fi'", "'Wj'", "'CFT'"))
        assert row.scoring_contract["original_construct_labels_inapplicable"] is True


def test_development_lock_recomputes_payload_and_every_frozen_file():
    validated = surface_contracts.validate_development_lock(LOCK, ITEMS)
    assert validated["lock_payload_sha256"] == (
        "3b5ebadbb82ffa815aeb36308e6cda1e88514869e1666c9213b4edb475037c42"
    )
    assert validated["live_result_inputs"] == ()


def test_surface_loader_rejects_hash_drift_and_c0_bank_divergence(tmp_path: Path):
    copied = tmp_path / "thorns"
    shutil.copytree(ITEMS, copied)
    cue_path = copied / "cue_forms" / "thorns-wedge-002.cue.yaml"
    cue = yaml.safe_load(cue_path.read_text())
    cue["surfaces"][0]["text"] += "\nDrift."
    cue_path.write_text(yaml.safe_dump(cue, sort_keys=False))

    with pytest.raises(ValueError, match="lock|C0|hash"):
        surface_contracts.load_surface_contracts(
            copied,
            phase="development",
            development_lock_path=copied / "CUE-DEVELOPMENT-LOCK-20260709.json",
        )


def test_locked_confirmation_uses_only_six_independent_post_lock_c3_candidates(
    tmp_path: Path,
):
    heldout = surface_contracts.load_surface_contracts(
        ITEMS,
        phase="locked-confirmation",
        development_lock_path=LOCK,
    )
    assert len(heldout) == 6
    assert {row.cue_arm for row in heldout} == {"C3"}
    assert all(row.sealed and row.mode == "construct" for row in heldout)
    assert all(row.author_provenance["author_id"] == "C3A01" for row in heldout)
    assert all(row.author_provenance["live_results_observed"] is False for row in heldout)

    copied = tmp_path / "thorns"
    shutil.copytree(ITEMS, copied)
    next((copied / "c3_candidates").glob("*.yaml")).unlink()
    with pytest.raises(ValueError, match="six|C3|held-out"):
        surface_contracts.load_surface_contracts(
            copied,
            phase="locked-confirmation",
            development_lock_path=copied / "CUE-DEVELOPMENT-LOCK-20260709.json",
        )
