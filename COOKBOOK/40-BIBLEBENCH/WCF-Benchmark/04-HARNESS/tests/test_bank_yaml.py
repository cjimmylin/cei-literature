"""Integration guard for the transcribed item bank — spine §10 + memo deltas.

Run:
    /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
        COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q

This is a CHARACTERIZATION test over `../05-BANK-YAML/` (the prose→YAML
transcription of the expansion-2 batch). It is not TDD-first production code — it
guards an already-produced data artifact against schema drift and against loss of
the binding memo deltas (errata E1–E3, R20 dual-credit, R23a construct-specificity,
the `[DISPUTED]` dev-set marking). If the bank grows (earlier waves transcribed),
the invariants below still hold; only the `>= 69` floor moves up.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import load_items  # noqa: E402

BANK_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", "05-BANK-YAML"))


@pytest.fixture(scope="module")
def bank():
    return load_items(BANK_DIR)


@pytest.fixture(scope="module")
def by_id(bank):
    return {i.id: i for i in bank}


def test_bank_loads_clean_and_has_the_expansion2_batch(bank):
    # loader raises on any schema violation; reaching here means 0 schema errors.
    assert len(bank) >= 69


def test_no_duplicate_ids(bank):
    ids = [i.id for i in bank]
    assert len(ids) == len(set(ids))


def test_every_item_has_positive_points_and_anchors(bank):
    for i in bank:
        assert i.total_points > 0, f"{i.id} has no rubric points"
        assert i.anchors and all(a.strip() for a in i.anchors), f"{i.id} missing anchors"
        assert i.commandments and i.commandments[0], f"{i.id} missing primary commandment"


def test_disputed_legs_are_dev_set_only(by_id):
    # R8/R9: the two expansion-2 [DISPUTED] legs are dev-set-only pending G6.
    for iid in ("LIB-C8-W304", "LIB-C2-W305"):
        assert by_id[iid].extra.get("dev_set_only") is True
        assert by_id[iid].extra.get("disputed") is True


def test_aggravate_items_carry_gold_order(bank):
    # TRANSCRIPTION-SPEC §2: gold_order is REQUIRED for orderable rank-sets and
    # incomparable pairs (Track B, T2a/T2b). Track A monotonicity tasks and T3
    # consistency batteries have no rank-set and legitimately omit it.
    for i in bank:
        if i.design == "aggravate" and i.track == "B" and i.tier in ("T2a", "T2b"):
            assert i.extra.get("gold_order"), f"{i.id} missing gold_order (ordinal key)"


def test_narrowgate_episodes_flagged_and_construct_specific(bank):
    # Every NARROWGATE item is an episode. construct_specificity is required on
    # the R23a expansion-2 targets (W301-W306); on other waves spec §4 forbids
    # fabricating it, so where present it must be well-formed.
    for i in bank:
        if i.design == "narrowgate":
            assert i.extra.get("episode") is True, f"{i.id} not flagged episode"
            cs = i.extra.get("construct_specificity")
            if "-W3" in i.id:
                assert isinstance(cs, dict) and "route" in cs and "reskin" in cs, f"{i.id} missing construct_specificity"
            elif cs is not None:
                assert isinstance(cs, dict) and "route" in cs and "reskin" in cs, f"{i.id} malformed construct_specificity"


def test_wholeheart_judge_calibration_instrument_present(by_id):
    # R14: WHOLE-C10-W305 is the G4 judge-calibration battery instrument.
    assert by_id["WHOLE-C10-W305"].extra.get("judge_calibration") is True


def test_e2_crosswind_q135_anchor_is_verbatim_not_mashup(by_id):
    # E2: the Q135 manner anchor must be the verbatim clause, not the mashup.
    for iid in ("CROSS-C5-W303", "CROSS-C9-W305"):
        anchors = " ".join(by_id[iid].anchors)
        if "Q135" in anchors:
            assert "peaceable, mild, and courteous speeches and behavior" in anchors
            assert "gentleness, kindness" not in anchors


def test_e3_1_liberty_usury_answer_text_anchor_present(by_id):
    anchors = " ".join(by_id["LIB-C8-W304"].anchors).lower()
    assert "usury" in anchors  # Q142 answer-text usury clause (E3.1)


def test_e3_2_aggravate_ordering_is_dual_credit(by_id):
    w302 = by_id["AGG-C3-W302"]
    assert any("dual-credit" in kp.criterion.lower() for kp in w302.rubric)
