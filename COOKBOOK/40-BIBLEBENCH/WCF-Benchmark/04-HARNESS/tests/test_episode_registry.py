"""Offline guards for the human-review EPISODE specification draft."""

from __future__ import annotations

import os
import sys

import pytest

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench.episode_registry import (  # noqa: E402
    EpisodeRegistryError,
    build_blind_episode_prompt,
    episode_specs_from_registry,
    load_episode_registry,
)
from wcfbench.loader import load_items  # noqa: E402
from wcfbench.narrowgate import EpisodeSpec  # noqa: E402

BANK_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "05-BANK-YAML"))


@pytest.fixture(scope="module")
def bank():
    return load_items(BANK_DIR)


@pytest.fixture(scope="module")
def draft_registry():
    return load_episode_registry(allow_unapproved=True)


def test_draft_registry_covers_exactly_the_frozen_episode_ids(bank, draft_registry):
    bank_ids = {item.id for item in bank if item.extra.get("episode") is True}
    registry_ids = {entry["item_id"] for entry in draft_registry["entries"]}

    assert len(bank_ids) == 22
    assert len(draft_registry["entries"]) == 22
    assert registry_ids == bank_ids


def test_every_draft_entry_constructs_an_episode_spec(draft_registry):
    specs = episode_specs_from_registry(draft_registry, allow_unapproved=True)

    assert len(specs) == 22
    assert all(isinstance(spec, EpisodeSpec) for spec in specs.values())
    assert all(tuple(spec.dials) == ("d0", "d1", "d2", "d3") for spec in specs.values())


def test_unapproved_registry_cannot_construct_specs_without_review_override(draft_registry):
    with pytest.raises(EpisodeRegistryError, match="DRAFT_UNAPPROVED"):
        episode_specs_from_registry(draft_registry)


def test_prompt_builder_uses_only_the_bank_stem(bank, draft_registry):
    by_id = {item.id: item for item in bank}

    for entry in draft_registry["entries"]:
        item = by_id[entry["item_id"]]
        assert entry["prompt_source"] == "bank.stem"
        assert not ({"key", "rubric", "anchors", "contested", "dev_set_only"} & set(entry))
        assert build_blind_episode_prompt(entry, item) == item.stem


def test_prompt_builder_rejects_nonblind_sources(bank, draft_registry):
    entry = dict(draft_registry["entries"][0], prompt_source="bank.key")

    with pytest.raises(EpisodeRegistryError, match="bank.stem"):
        build_blind_episode_prompt(entry, bank[0])


def test_unapproved_registry_fails_closed_by_default():
    with pytest.raises(EpisodeRegistryError, match="DRAFT_UNAPPROVED"):
        load_episode_registry()


def test_every_mapping_is_explicitly_pending_human_review(draft_registry):
    assert draft_registry["status"] == "DRAFT_UNAPPROVED"
    assert draft_registry["approval"] == {
        "approved": False,
        "reviewer": None,
        "reviewed_at": None,
    }
    for entry in draft_registry["entries"]:
        review = entry["human_review"]
        assert review["status"] == "pending"
        assert review["mapping_basis"].strip()
        assert review["known_limitations"]
