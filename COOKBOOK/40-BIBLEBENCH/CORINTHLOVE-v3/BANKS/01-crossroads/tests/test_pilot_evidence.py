from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK))

from pilot import contracts  # noqa: E402
from pilot.evidence import EvidenceStore, verify_evidence_root  # noqa: E402


def manifest():
    return {
        "manifest_version": "crossroads-public-qualification-v1",
        "purpose": "public qualification",
        "provenance": contracts.PROVENANCE_MOCK,
        "execution_mode": "path-only staged qualification",
        "canonical_e_measurement": False,
        "issues_live_judges": False,
        "authorizes_model_ranking": False,
        "models": ["openai/gpt-5-nano"],
        "expected_snapshots": {
            "openai/gpt-5-nano": "openai/gpt-5-nano-2025-08-07",
        },
        "public_item_ids": ["CROSSROADS-0601"],
        "canary_item_ids": ["CROSSROADS-0601"],
        "hashes": {"bank": "a" * 64, "profile": "b" * 64,
                   "path_classifier": "c" * 64, "followthrough": "d" * 64},
        "max_attempts": 3,
        "authorizes_private_execution": False,
        "authorizes_calibration": False,
        "authorizes_freeze": False,
    }


def canary():
    return {
        "selection_version": "crossroads-public-canary-v1",
        "purpose": "public qualification",
        "item_ids": ["CROSSROADS-0601"],
        "bank_sha256": "a" * 64,
        "coverage": {"clauses": [f"C{i}" for i in range(1, 17)],
                     "fallback_families": [f"F{i}" for i in range(6)],
                     "substrates": ["workspace.edit"]},
        "authorizes_private_execution": False,
        "authorizes_calibration": False,
        "authorizes_freeze": False,
    }


def test_store_is_create_only_journaled_and_hash_chained(tmp_path):
    root = tmp_path / "run"
    store = EvidenceStore.create(root, manifest(), canary())
    artifact = {"artifact_version": "v1", "status": "success",
                "purpose": "public qualification", "value": 1}
    store.commit("access/openai--gpt-5-nano/attempt-1.json", artifact,
                 event="access_attempt")
    store.complete_phase("access")
    entries = store.read_journal()
    assert [row["sequence"] for row in entries] == list(range(1, len(entries) + 1))
    assert entries[0]["previous_entry_sha256"] == "0" * 64
    for left, right in zip(entries, entries[1:]):
        assert right["previous_entry_sha256"] == contracts.sha256_value(left)
    assert entries[-2]["artifact_sha256"] == contracts.sha256_value(artifact)
    verify_evidence_root(root)
    with pytest.raises(FileExistsError):
        store.commit("access/openai--gpt-5-nano/attempt-1.json", artifact,
                     event="access_attempt")


def test_crash_orphan_can_be_adopted_only_when_hash_and_semantics_validate(tmp_path):
    root = tmp_path / "run"
    store = EvidenceStore.create(root, manifest(), canary())
    relative = "episodes/openai--gpt-5-nano/CROSSROADS-0601/attempt-1.json"
    payload = {"artifact_version": "v1", "status": "success",
               "purpose": "public qualification", "value": 2}
    path = root / relative
    path.parent.mkdir(parents=True)
    with path.open("xb") as handle:
        handle.write(contracts.canonical_bytes(payload)); handle.flush(); os.fsync(handle.fileno())
    with pytest.raises(ValueError, match="unreferenced"):
        verify_evidence_root(root)
    adopted = store.adopt_orphan(
        relative, event="episode_attempt",
        validator=lambda value: value["value"] == 2,
    )
    assert adopted == payload
    verify_evidence_root(root)
    with pytest.raises(ValueError, match="already journaled"):
        store.adopt_orphan(relative, event="episode_attempt", validator=lambda _: True)


def test_whole_root_verifier_rejects_tamper_extra_missing_and_symlink(tmp_path):
    root = tmp_path / "run"
    store = EvidenceStore.create(root, manifest(), canary())
    relative = "access/openai--gpt-5-nano/attempt-1.json"
    store.commit(relative, {"status": "success", "purpose": "public qualification"},
                 event="access_attempt")
    path = root / relative
    original = path.read_bytes()
    path.write_bytes(contracts.canonical_bytes({"status": "tampered"}))
    with pytest.raises(ValueError, match="hash"):
        verify_evidence_root(root)
    path.write_bytes(original)
    (root / "extra.txt").write_text("extra")
    with pytest.raises(ValueError, match="unreferenced"):
        verify_evidence_root(root)
    (root / "extra.txt").replace(tmp_path / "moved-extra.txt")
    path.replace(tmp_path / "moved-artifact.json")
    with pytest.raises(ValueError, match="missing"):
        verify_evidence_root(root)

    root2 = tmp_path / "run2"
    store2 = EvidenceStore.create(root2, manifest(), canary())
    os.symlink(root2 / "manifest.json", root2 / "linked.json")
    with pytest.raises(ValueError, match="symlink"):
        verify_evidence_root(root2)


def test_journal_rejects_truncation_reorder_and_duplicate_phase(tmp_path):
    root = tmp_path / "run"
    store = EvidenceStore.create(root, manifest(), canary())
    store.complete_phase("access")
    with pytest.raises(ValueError, match="already complete"):
        store.complete_phase("access")
    journal = root / "journal.jsonl"
    lines = journal.read_text().splitlines()
    journal.write_text("\n".join(reversed(lines)) + "\n")
    with pytest.raises(ValueError, match="journal"):
        verify_evidence_root(root)


def test_store_rejects_credentials_and_path_escape(tmp_path):
    store = EvidenceStore.create(tmp_path / "run", manifest(), canary())
    with pytest.raises(ValueError, match="credential"):
        store.commit("artifact.json", {"api_key": "secret"}, event="attempt")
    with pytest.raises(ValueError, match="relative"):
        store.commit("../escape.json", {"safe": True}, event="attempt")
